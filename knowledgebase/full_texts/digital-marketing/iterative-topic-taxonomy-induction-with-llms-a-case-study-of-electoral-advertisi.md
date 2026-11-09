---
title: 'Iterative Topic Taxonomy Induction with LLMs: A Case Study of Electoral Advertising'
url: https://arxiv.org/abs/2510.15125
category: digital-marketing
subcategory: empirical
date: 2025-10
venue: ''
authors:
- Alexander Brady
- Tunazzina Islam
source: arxiv
pdf_url: https://arxiv.org/pdf/2510.15125
pages: 15
chars: 63807
fetched_at: '2026-11-08T13:17:46+00:00'
kb_version: 1
---

# Iterative Topic Taxonomy Induction with LLMs: A Case Study of Electoral Advertising

Iterative Topic Taxonomy Induction with LLMs: A Case Study of Electoral
Advertising
Alexander Brady*
Department of Computer Science
ETH Zurich
Zurich, Switzerland
bradya@ethz.ch
Tunazzina Islam*
Department of Computer Science
Purdue University
West Lafayette, IN 47907, USA
islam32@purdue.edu
Abstract
Social media platforms play a pivotal role in
shaping political discourse, but the scale and
rapid evolution of online content make sys-
tematic analysis difficult. We introduce an
end-to-end framework for inducing an inter-
pretable topic taxonomy from unlabeled text
corpora. The framework combines embedding-
based clustering with iterative large language
model (LLM) inference to construct a topic
taxonomy without requiring predefined labels
or seed topics. It first synthesizes candidate
topics from document clusters and then uses
the resulting taxonomy to assign consistent
topic labels across clusters. We evaluate the
approach through a case study of political ad-
vertising ahead of the 2024 U.S. presidential
election. We use the induced taxonomy to sup-
port downstream analyses of issue prevalence,
moral framing, advertising spend, and demo-
graphic exposure patterns. These results sug-
gest that iterative taxonomy construction can
provide a scalable and interpretable approach to
organizing large unlabeled text corpora while
supporting substantive downstream analysis.
1 Introduction
Modern political campaigns have been fundamen-
tally transformed by the rise of social media plat-
forms. Platforms such as Facebook and Instagram
have become important venues for political ad-
vertising, enabling campaigns and advocacy or-
ganizations to reach voters with issue-specific ap-
peals. Prior work has shown that voters respond
more favorably to advertisements addressing issues
they personally prioritize, irrespective of partisan-
ship (Chu et al., 2024). Understanding the content
and structure of these messages is critical for study-
ing contemporary political communication.
The scale and rapid evolution of social me-
dia content make manual analysis difficult. Tra-
*Equal contribution.
(a) Iteratively build a shared topic taxonomy
Cluster 1 Cluster 2 Cluster 3
· · ·
No existing
topic matches.
Add new topic:
Economy.
Matches existing
topic (Economy).
No new topic
added.
No existing
topic matches.
Add new topic:
Education.
Current taxonomy
Economy
Current taxonomy
Economy
Current taxonomy
Economy
Education
(b) Assign topic labels to all clusters
Final topic taxonomy
Economy
Immigration
Education
V oting
· · ·
 Economy Immigration Education V oting
· · ·
Figure 1:Overview of the proposed framework. Documents
are first embedded and clustered. (a) Cluster representatives
are processed sequentially by the LLM to induce a shared
topic taxonomy. (b) The LLM assigns one topic label to each
cluster from the completed taxonomy.
ditional topic modeling methods such as Latent
Dirichlet Allocation (LDA) (Blei et al., 2003)
and non-negative matrix factorization (NMF) (Lee
and Seung, 1999) provide unsupervised mech-
anisms for discovering latent structure in text
corpora, but their outputs often require addi-
tional interpretation or manual labeling. Prior
work has therefore explored automated topic la-
beling through probabilistic methods (Magatti
et al., 2009), summarization-based approaches
(Wan and Wang, 2016; Cano Basave et al., 2014),
and sequence-to-sequence models (Alokaili et al.,
2020).
More recently, embedding-based approaches
such as BERTopic (Grootendorst, 2022) have
combined contextualized text representations with
density-based clustering to produce more coherent
topic groupings. Large language models (LLMs)
have also enabled more semantically expressive
approaches to topic discovery and labeling (Islam,
arXiv:2510.15125v3  [cs.CL]  1 Oct 2026

2026a; Sudhoff et al., 2026; Pham et al., 2024).
However, several recent LLM-based approaches
assume either an initial seed set of themes or a
predefined set of topics (Islam and Goldwasser,
2025b,d).
In this work, we introduce a seed-free frame-
work for inducing an interpretable topic taxon-
omy from unlabeled text corpora (Figure 1). Our
method first uses embedding-based clustering to
identify groups of semantically related documents.
It then processes these clusters sequentially with
an LLM, which determines whether each cluster
is adequately represented by an existing topic or
whether a new topic should be added to the tax-
onomy. In a second pass, the complete induced
taxonomy is used to assign a single topic label to
each cluster. This iterative procedure is designed
to promote consistency across cluster labels while
allowing the taxonomy to expand as new themes
are encountered.
Unlike methods that require human-provided
seed labels, our framework constructs the taxon-
omy directly from the corpus. The method is also
distinct from single-shot LLM labeling: rather than
generating each cluster label independently, previ-
ously induced topics remain available throughout
the synthesis process, creating a shared and evolv-
ing label space across clusters. The resulting taxon-
omy can then be used for downstream annotation
and analysis.
We evaluate the framework through a case study
of political advertisements collected from the Meta
Ad Library during the month preceding the 2024
U.S. presidential election1. The induced taxonomy
captures a range of political issues represented in
the advertising corpus. We further extend our anal-
ysis by examining the moral framings underlying
these ads through the lens of Moral Foundations
Theory (Iyer et al., 2012; Haidt and Graham, 2007;
Haidt and Joseph, 2004). By examining political
issue framing and its associations with observed
audience demographics, the case study illustrates
the substantive analyses enabled by the proposed
framework.
Our contributions are:
1. A general, seed-free, LLM-guided framework
for inducing interpretable topic taxonomies
from unlabeled corpora without human inter-
vention.
1Code, prompts and dataset are available at: https://
github.com/alexander-brady/llm-topic-synthesis
2. An iterative topic synthesis mechanism that
yields more consistent and better-aligned topic
labels than classical topic models and single-
shot LLM labeling under human evaluation.
3. A case study of 2024 U.S. political adver-
tising demonstrating how the induced taxon-
omy can support downstream analyses of is-
sue salience, moral framing, ad spending, and
demographic exposure.
4. Release of a curated dataset of 2024 U.S.
presidential election ads to support future re-
search.
2 Related Work
Political advertising and microtargeting.So-
cial media has become an important venue for po-
litical communication, campaign messaging, and
voter mobilization (Islam, 2025b; Aggarwal et al.,
2023; Capozzi et al., 2021; Goldberg et al., 2021;
Ribeiro et al., 2019; Silva et al., 2020; Fulgoni et al.,
2016; Teresi and Michelson, 2015; Hersh, 2015).
A substantial body of work has examined politi-
cal microtargeting and the ways campaigns tailor
messages to specific audiences (Islam and Gold-
wasser, 2025c; Islam, 2025a; Tappin et al., 2023;
Zuiderveen Borgesius et al., 2018; Hersh, 2015).
Related studies have analyzed the strategic dis-
semination of campaign content across platforms
and the relationship between targeted advertising
and voter responses (Hackenburg and Margetts,
2024; Islam et al., 2023a; Hirsch et al., 2024).
These settings motivate scalable methods for orga-
nizing and interpreting large collections of political
messages.
Topic modeling and automated topic labeling.
Traditional topic modeling methods have been
widely used to analyze large text corpora in do-
mains including social media (Chen et al., 2019;
Ozer et al., 2016) and political discourse (Math-
aisel and Comm, 2021; Lahoti et al., 2018). How-
ever, classical approaches can produce topics that
are difficult to interpret and often require hu-
man inspection or post-hoc labeling (Chang et al.,
2009; Mei et al., 2007). More recent embedding-
based approaches such as BERTopic (Grootendorst,
2022) combine contextualized representations with
density-based clustering to improve topic coher-
ence and interpretability.
Large language models have enabled a further
shift toward direct topic synthesis and labeling.
TopicGPT (Pham et al., 2024), for example, uses

LLMs to construct and refine topic taxonomies
and has demonstrated strong performance in terms
of coherence and interpretability. More broadly,
LLMs have also shown strong performance on an-
notation tasks traditionally performed by human
coders (Gilardi et al., 2023). These results moti-
vate the use of LLM inference not only for labeling
existing clusters but also for constructing a shared
topic inventory.
Recent LLMs-in-the-loop methods have ex-
plored fine-grained theme and argument discov-
ery, for example using an initial seed set of themes
to guide topic discovery or uncover associated ar-
guments (Islam and Goldwasser, 2025d,b; Islam
et al., 2023b; Islam and Goldwasser, 2022). Lam
et al. (2024) introduced LLooM, which iteratively
induces and scores higher-level concepts from text,
with optional analyst-provided seeds. In contrast,
our framework incrementally constructs a shared
topic inventory over document clusters and then
relabels all clusters using the completed taxonomy.
Moral framing in political discourse.Moral
Foundations Theory provides a widely used frame-
work for analyzing the moral dimensions of politi-
cal language (Iyer et al., 2012; Haidt and Graham,
2007; Haidt and Joseph, 2004). Earlier compu-
tational approaches typically relied on manually
annotated datasets to train classifiers for detect-
ing moral appeals (Pacheco et al., 2022; Roy et al.,
2021). More recently, LLM-based approaches have
been used to generate moral labels and explanations
directly from political text (Islam and Goldwasser,
2025a). We build on this line of work by using the
induced topic taxonomy as the basis for a down-
stream analysis of moral framing in political ad-
vertisements. In our setting, moral annotations are
used as an exploratory analytical layer rather than
as independent validation of the induced topics.
3 Methodology
We propose a framework for inducing an inter-
pretable topic taxonomy from an unlabeled text
corpus. This framework consists of three main
stages: (1) embedding-based clustering, (2) LLM-
based taxonomy induction, (3) cluster-level topic
assignment. We formalize the iterative topic syn-
thesis and annotation procedure in Algorithm 1.
3.1 Embedding-Based Clustering
Given a corpus of documents, we first encode each
document into a dense vector representation using
Algorithm 1Iterative Topic Taxonomy Induction
Require: Document clusters C={C 1, . . . , Cn},
cluster representativesR(C i), LLMM
Ensure: Topic taxonomy T and cluster-topic as-
signments
1:Initialize topic listT ← ∅
2:foreach clusterC i ∈ Cdo
3:ifT=∅then
4: Prompt M to generate a topic t from
R(Ci)
5:T ← T ∪ {t}
6:else
7:PromptMwithR(C i)and topicsT
8:Constrain output to {yes,no}
9:ifnothen
10: Prompt M to generate a new topic t
fromR(C i)
11:T ← T ∪ {t}
12:end if
13:end if
14:end for
15:foreach clusterC i ∈ Cdo
16:PromptMwithR(C i)and topicsT
17:Constrain output to select one topict∈ T
18:Assign topictto clusterC i
19:end for
20:returnTand cluster-topic assignments
a pretrained sentence embedding model such as
Sentence-BERT (Reimers and Gurevych, 2019).
We then apply UMAP (McInnes et al., 2020) to
reduce the dimensionality of the embedding space
before clustering.
We cluster the reduced embeddings using HDB-
SCAN (McInnes et al., 2017), a density-based clus-
tering algorithm that can identify clusters of vary-
ing density while leaving low-confidence points
unassigned. This property is useful for noisy text
corpora in which not every document necessarily
belongs to a well-defined topical cluster.
For each cluster Ci, we select the five documents
with the highest HDBSCAN membership probabil-
ities as its representative set R(Ci). These repre-
sentative documents are used as the textual input
to the LLM during both taxonomy induction and
subsequent topic assignment. Restricting LLM in-
ference to a small representative set reduces the
amount of text that must be processed while em-
phasizing documents that are most characteristic of
each cluster.

3.2 Iterative Topic Taxonomy Induction
The goal of the next stage is to construct a shared
topic inventory directly from the document clusters,
without requiring human-provided seed labels. We
initialize the topic taxonomy T as an empty set and
process the clusters sequentially.
For the first cluster, the LLM is prompted to gen-
erate a concise topic label from its representative
documents. This label becomes the first element
of T . For each subsequent cluster, the LLM is
shown the cluster representatives together with the
topics currently in T and asked whether any exist-
ing topic adequately describes the cluster. We use
constrained decoding (Beurer-Kellner et al., 2024)
to restrict this decision to yes or no. If the model
returns no, it is then prompted to generate a new
concise topic label, which is then added toT.
In this way, previously generated labels remain
available while later clusters are processed. Unlike
independent, single-shot labeling, the procedure
therefore constructs an evolving shared label space
and only introduces a new topic when the model de-
termines that the existing inventory is insufficient.
For our experiments, clusters were processed in
ascending HDBSCAN label order. Because HDB-
SCAN cluster identifiers are arbitrary rather than
semantically ordered, this corresponds to a fixed
but otherwise arbitrary traversal of the induced clus-
ters. We treat robustness to cluster ordering as a
limitation and direction for future work.
3.3 Cluster-Level Topic Assignment
The first pass determines which topics belong in the
taxonomy but does not necessarily provide the final
assignment for every cluster. After the complete
topic inventory has been constructed, we therefore
perform a second pass over all clusters.
For each cluster, the LLM receives its represen-
tative documents together with the complete tax-
onomy T . We use constrained decoding to require
the model to select exactly one label from the avail-
able topic inventory. This second pass allows every
cluster to be evaluated against the same final label
space, including topics that may have been intro-
duced only after that cluster was first encountered.
The output of the framework is therefore (1) an
induced topic taxonomy and (2) a topic assignment
for each document cluster.
4 Case Study: Experimental Setup
We apply the proposed framework to political ad-
vertisements from the 2024 U.S. election cycle.
The goal of the case study is twofold: first, to eval-
uate the quality of the induced topic taxonomy; and
second, to demonstrate how the resulting annota-
tions can support downstream analyses.
4.1 Dataset
We collected political advertisements running on
Facebook and Instagram in the United States during
October 2024 using the Meta Ad Library, starting
one month before the 2024 presidential election.
The resulting dataset contains 8,047 unique adver-
tisements. The ads cover election-related messag-
ing at both the local and federal levels. 99% of the
advertisements are in English, with a small fraction
in Spanish.
For each advertisement, the Meta Ad Library
provides a unique ad identifier, title, body text,
URL, creation time, campaign duration, page au-
thor, funding entity, and advertising spend reported
as a range. We represent spend using the midpoint
of the reported range. Meta also reports impres-
sions as a range, for which we similarly use the
midpoint, together with aggregate audience distri-
butions by gender, age group, and U.S. state.
Because these demographic statistics describe
observed ad delivery rather than necessarily the
advertiser’s intended targeting criteria, we refer to
them throughout asaudience exposureordelivery
patternsrather than direct targeting decisions.
4.2 Taxonomy Induction
We embed the advertisement body texts using the
all-MiniLM-L6-v2 sentence-transformer model.
To reduce near-duplicate content, we remove adver-
tisements whose embedding has cosine similarity
greater than 0.95 to another advertisement. We
then apply HDBSCAN to the UMAP-reduced em-
beddings with a minimum cluster size of15.
This procedure assigns 4,510 advertisements to
73 clusters. For each cluster, we select the five ad-
vertisements with the highest HDBSCAN member-
ship probabilities as cluster representatives. These
are given to the LLM during taxonomy induction
and cluster-level topic assignment.
We use a locally hosted Llama-3.2-3B
model (Grattafiori et al., 2024) to execute our
framework, without GPU acceleration.
We initialize the topic inventory with no seed

labels. Processing the 73 clusters using the pro-
cedure described in Section 3 produces a taxon-
omy containing 15 generated topics. During the
second-pass cluster assignment stage, the model
is additionally allowed to assign the labelother
when none of the induced topics adequately de-
scribes a cluster. Althoughborder securityappears
in the generated taxonomy, no cluster is ultimately
assigned this label. The final topic set and cluster
counts are shown in Table 1. The complete prompts
are provided in App. A.
4.3 Human Evaluation: Topic Labels
To evaluate the quality of the induced labels, we
compare our method with two baselines. The first
is BERTopic (Grootendorst, 2022). We use the
same underlying clusters for both approaches and
provide the same LLM with the cluster represen-
tative documents; for the BERTopic condition, the
model additionally receives the ten highest-ranked
cluster keywords.
The second baseline is inspired by Top-
icGPT (Pham et al., 2024). For each cluster, the
LLM receives the representative advertisements
and generates a concise topic label independently,
without access to previously generated labels or
an evolving shared taxonomy. This comparison is
intended to isolate the effect of iterative taxonomy
construction relative to single-shot LLM labeling.
Two volunteer annotators (one female and one
male) with backgrounds in natural language pro-
cessing (NLP) and computational social science
(CSS), age range 25-40, evaluate the resulting la-
bels. Each annotator is given the same set of 10
advertisements. For each evaluated advertisement,
the labels produced by BERTopic, the TopicGPT-
style baseline, and our framework are presented
in randomized order. Annotators select the label
that best represents the advertisement and rate each
candidate label from 1 (irrelevant) to 5 (perfect fit).
4.4 Moral Foundation Annotation
We use Moral Foundations Theory (Iyer et al.,
2012; Haidt and Graham, 2007; Haidt and
Joseph, 2004) as an exploratory framework for
examining the moral framing of political ad-
vertisements. We consider six foundations:
Care/Harm, Fairness/Cheating, Loyalty/Betrayal,
Authority/Subversion, Sanctity/Degradation, and
Liberty/Oppression. For more information on
Moral Foundations Theory, see App. B.
For each topic-labeled cluster, we first prompt
the LLM to summarize the primary argument ex-
pressed by its representative advertisements with
respect to the assigned topic. We then provide the
model with definitions of the six moral foundations
and use constrained decoding to require selection
of a single foundation. The complete prompts are
provided in App. A.
Because these moral labels are generated using
the topic annotation as part of the prompting pro-
cedure, we treat subsequent relationships between
topics and moral foundations as exploratory down-
stream analyses rather than independent validation
of the topic taxonomy.
4.5 Document-Level Classification
The taxonomy-induction framework produces
cluster-level labels, while HDBSCAN leaves a sub-
stantial fraction of advertisements unassigned. To
examine whether the induced topic labels can be
propagated to individual advertisements, we con-
duct a separate supervised classification experi-
ment.
We construct a pseudo-labeled training set from
advertisements assigned to clusters with HDB-
SCAN membership probability greater than 0.98.
This produces 2,337 advertisements. The resulting
class distribution is highly imbalanced: the four
largest classes—voting rights( 26%),crime/justice
(19%),education( 17%), andabortion( 11%)—
account for 73% of the pseudo-labeled advertise-
ments, while the smallest classes,healthcare ac-
cessandproperty taxes, each account for0.64%.
We additionally sample200 advertisements from
among the unassigned documents and annotate
them manually with topic labels. These annota-
tions serve as human-labeled evaluation data for
the document-level classification task.
We compare Logistic Regression, XG-
Boost (Chen and Guestrin, 2016), RoBERTa (Liu
et al., 2019), and SetFit (Tunstall et al., 2022).
For classifiers operating on fixed embeddings,
advertisement texts are represented using
all-MiniLM-L6-v2. Hyperparameters are se-
lected using GridSearchCV , and performance
is reported using macro F1 and accuracy. The
manually annotated advertisements were held out
entirely for final evaluation.
4.6 Ad-Level Annotation
For downstream descriptive analyses, we addition-
ally assign topic and moral-foundation labels to
individual advertisements using the induced tax-

Issue #Clusters Example Ad
economy 15 Molly Buck’s agenda is failing Iowa families. We can’t afford Molly Buck in the
State House.
voting rights 13 Make Your Vote Count. RE-register to Vote in the District of Your Second Home.
crime/justice 12Orange County Firefighters Trust Dave Min To Keep Our Communities Safe.
personal freedom 4Tim Sheehy will always fight for Montana Values in the Senate!
voting 4Vote Rebecca for State Rep by Nov 5th!
education 4Vote for students. Vote for teachers. Support our public schools.
affordable housing 4Catherine has supported more multi-family housing so we can afford homes in
the communities we grew up in. Vote Stefani!
environmental protection 4 We can count on Lucy Rehm to be a responsible leader and protect our clean air
and water.
immigration 3Yadira Caraveo supported efforts to defund ICE and the border patrol. Now
Colorado is being overwhelmed with illegal immigration.
election integrity 3Question 3 will change our state’s Constitution and weaken our democracy by
throwing away thousands of ballots over minor errors. Vote NO on Question 3.
abortion 2Defend reproductive freedom - VOTE on Tuesday, November 5th!
healthcare access 1 Lucy Rehm cares about improving conditions in your local hospital. That’s why
Minnesota Nurses endorsed Lucy Rehm!
property taxes 1Caleb will work to stop reckless spending and oppose tax and fee increases.
sewer sale 1Get the facts on the Gloucester Township sewer sale, visit
VoteYesGloucesterTownship.com!
other 2LISCOMB - thanks for welcoming me at the little street where old and new
friends meet!
Table 1:Topics identified by the LLM in the political ads dataset. ‘#Clusters’ column gives the number of unique clusters
assigned to each topic by the LLM.
Model Average Score Best Label
BERTopic 1.2 3
TopicGPT-style 2.7 5
Our Method 2.8 12
Table 2:Annotation results. The average score is out of 5,
and the best label is the number of times that model’s label
was selected as the most fitting (among all annotators).
onomy. We use mistralai/Mistral-7B-v0.1
(Jiang et al., 2023) for this ad-level annotation stage.
This model is used only for the downstream case-
study analyses and is separate from the Llama-3.2-
3B model used to induce and evaluate the cluster-
level taxonomy.
Using these document-level annotations together
with Meta’s spend and impression data, we exam-
ine issue prevalence, advertising expenditure, fund-
ing concentration, moral framing, and demographic
exposure patterns.
To characterize associations between adver-
tisement content and demographic groups, we
compute positive pointwise mutual information
(PPMI) (Church and Hanks, 1990) between topic
or moral-foundation annotations and observed audi-
ence attributes. Higher PPMI indicates that a topic
or moral frame occurs disproportionately among
advertisements delivered to a given demographic
group. We interpret these associations descriptively
as exposure patterns rather than direct evidence of
Model Macro F1 Accuracy
Logistic Regression 0.37 0.55
XGBoost 0.31 0.53
RoBERTa 0.32 0.53
SetFit 0.36 0.60
Table 3:Document-level classification performance for topic
assignment.
advertisers’ targeting intent.
5 Results and Analysis
We first evaluate the quality of the induced topic la-
bels and the feasibility of propagating those labels
to individual advertisements. We use the result-
ing annotations for exploratory analyses of issue
salience, moral framing, advertising expenditure,
funding concentration, and demographic exposure.
5.1 Topic Label Evaluation
Table 2 summarizes the human evaluation of topic
labels generated by BERTopic, the TopicGPT-style
single-shot baseline, and our iterative framework.
The iterative framework receives the highest av-
erage rating (2.8), compared with 2.7 for the single-
shot baseline and 1.2 for BERTopic. The difference
in mean rating between our method and the single-
shot baseline is small. However, the labels pro-
duced by our method are selected as the best-fitting

Healthcare access
Voting
Election integrity
Voting rightsImmigration
AbortionEconomy
Personal freedomAffordable housingProperty taxes
Environmental protection
Crime / justice
Education
Other
Political issue
Sanctity / Degradation
Fairness / Cheating
Liberty / Oppression
Authority / Subversion
Loyalty / Betrayal
Care / Harm
Moral foundation
(a) Proposed Framework Topics
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Political issue
Sanctity / Degradation
Fairness / Cheating
Liberty / Oppression
Authority / Subversion
Loyalty / Betrayal
Care / Harm
Moral foundation
(b) LDA Topics
−0.75
−0.50
−0.25
0.00
0.25
0.50
0.75
Figure 2:Associations between moral-foundation labels and
topic labels for (a) the proposed taxonomy and (b) LDA topics.
Cells show Pearson correlations between one-hot topic and
moral-foundation assignments.
$0 $250 $500 $750 $1,000
Average spend (USD)
Sewer sale
Property taxes
Voting
Education
Affordable housing
Economy
Environmental protection
Healthcare access
Crime/justice
Other
Election integrity
Immigration
Border security
Voting rights
Personal freedom
Abortion
 $50
 $87
 $269
 $324
 $340
 $423
 $480
 $514
 $540
 $546
 $603
 $629
 $694
 $817
 $818
 $997
0 20,000 40,000 60,000
Average impressions
 1,166
 4,984
 20,894
 25,019
 28,215
 32,013
 32,433
 31,762
 39,417
 43,061
 40,959
 49,506
 45,572
 60,005
 64,265
 55,659
Figure 3:Average advertising spend and impressions per ad
by annotated topic.
label in 12 judgments, compared with 5 for the
single-shot baseline and3for BERTopic.
These results suggest that maintaining a shared,
evolving topic inventory can improve label con-
sistency relative to generating cluster labels inde-
pendently, although the small scale of the human
evaluation limits the strength of this conclusion.
The strongest contrast is with BERTopic-based la-
beling, while the difference between iterative and
single-shot LLM labeling is more modest in aver-
age rating.
The annotators achieve a Cohen’s κ (Cohen,
1960) of 0.66, indicating substantial agreement un-
der this evaluation setup. For5 out of the 20 rounds,
the annotators gave the same score for all models
(in all cases, a score of 1).
5.2 Document-Level Classification Results
We next evaluate whether the cluster-derived labels
can be propagated to individual advertisements.
Table 3 reports performance across the four su-
pervised classifiers. Logistic Regression achieves
the highest macro F1 score ( 0.37), while SetFit
achieves the highest overall accuracy (0.60). Per-
formance is modest across all models, reflecting
the difficulty of the task and the substantial class
imbalance in the pseudo-labeled training data.
These results indicate that the induced labels can
provide supervision for document-level classifica-
tion, but they also show that propagating cluster-
level topic labels to individual advertisements re-
mains challenging. We therefore treat the super-
vised classifier as a downstream extension of the
framework rather than evidence of high-quality an-
notation for all advertisements.
5.3 Topic Salience and Moral Framing
We next examine how the induced topics relate to
the moral-foundation annotations. For each adver-
tisement, we construct one-hot representations of
its topic and moral-foundation labels and compute
pairwise Pearson correlations.
Figure 2 compares these relationships for the
induced taxonomy and an LDA baseline. In the
induced taxonomy, several topic–foundation pairs
show comparatively strong associations. For exam-
ple,Fairness/Cheatingis strongly associated with
crime/justice, whileLoyalty/Betrayalis strongly
associated withimmigration. The corresponding
LDA topics show weaker associations with the
moral-foundation labels.
Because the moral labels are themselves gen-
erated using topic-conditioned LLM inference,
these relationships should be interpreted as descrip-
tive properties of the resulting annotation pipeline
rather than independent validation of the topic tax-
onomy. Nevertheless, they illustrate how an inter-
pretable topic inventory can support subsequent
analysis of moral framing.
5.4 Ad-Level Analysis
We further use the document-level annotations to
examine advertising expenditure, audience expo-
sure, funding concentration, and moral framing.
These analyses are descriptive and are intended to
demonstrate the analytical affordances of the in-
duced taxonomy rather than establish causal claims
about campaign strategy.

$0k $15k $30k $45k $60k
Spend, top economy funders (USD)
Investing in Arkansas
Americans For Prosperity
Congressional Leadership
Fund
Americans For Prosperity
Action, Inc.(AFP Action)
Stand with Crypto
Alliance, Inc.
 $17.1k
 $17.3k
 $22.0k
 $26.4k
 $47.8k
$0k $15k $30k $45k $60k
Spend, top crime/justice funders (USD)
Safer LA County (Hochman
for DA)
Stop Houston Murders PAC
Smart and Safe Florida
Judicial Fairness PAC
Preserve America PAC
 $21.0k
 $25.7k
 $26.7k
 $43.6k
 $47.5k
$0k $15k $30k $45k $60k
Spend, top abortion funders (USD)
Montanans Securing
Reproductive Rights
Colin Allred For Senate
Republic Restoratives Inc
Last Best Place PAC
Florida Voters Against
Extremism
 $17.2k
 $17.5k
 $17.5k
 $18.0k
 $62.7k
Care/Harm Fairness/Cheating Loyalty/Betrayal Authority/Subversion Sanctity/Degradation Liberty/Oppression
Figure 4:Spend by the top five funders of economy, crime/justice, and abortion ads, segmented by moral foundation.
4%
59%
12%
25%
Economy
$576k total
5%
11%
43%
14%
26%
Crime/justice
$432k total
11%
7%
34%
48%
Abortion
$350k total
Care/Harm Fairness/Cheating Loyalty/Betrayal Authority/Subversion Sanctity/Degradation Liberty/Oppression
Figure 5:Distribution of advertising spending across moral
foundations within economy, crime/justice, and abortion ad-
vertisements. Percentages indicate within-topic spending
shares; total spending is shown beneath each chart.
5.4.1 Spending and Impressions by Topic
Figure 3 compares average advertising spend and
average impressions across topics.Abortion,per-
sonal freedom, andvoting rightshave among the
highest average spending levels in the annotated
corpus. By contrast,immigrationandborder secu-
rityreceive comparatively high impressions relative
to their average spending.
Lower-volume issues such asproperty taxesand
local-service topics receive substantially less ex-
penditure and exposure. Overall, the differences
between spending and impressions illustrate that
issue categories vary not only in advertiser invest-
ment but also in the amount of observed audience
exposure associated with that investment.
5.4.2 Leading Funders by Issue
Figure 4 compares estimated advertising expen-
diture among the five highest-spending funders
within each of three issue categories:economy,
abortion, andcrime/justice 2 . For economy and
abortion advertisements, the largest displayed fun-
der spends substantially more than each of the other
four. In contrast, crime/justice has two leading fun-
ders with similar expenditures, followed by three
funders with lower, broadly comparable spending.
2https://www.pewresearch.org/politics/2024/09/
09/issues-and-the-2024-election/
These results illustrate differences in expenditure
patterns among the leading funders across issue cat-
egories in the observed corpus. Because the com-
parison is restricted to the five highest-spending
funders in each category, it does not establish dif-
ferences in overall funding concentration or in the
total number of organizations supporting each is-
sue. Assessing those questions requires the com-
plete funder-level expenditure distribution. Further
analysis is provided in Appendix D.1.
5.4.3 Moral Framing and Advertising Spend
Figure 5 shows the distribution of estimated adver-
tising expenditure across moral foundations within
each issue category. Economic advertising pri-
marily emphasizesFairness/Cheating(59%) and
Liberty/Oppression(25%), while crime/justice ad-
vertising primarily emphasizesLoyalty/Betrayal
(43%) andLiberty/Oppression(26%). Abortion ad-
vertising primarily emphasizesLiberty/Oppression
(48%) andSanctity/Degradation(34%).
Figure 4 shows that the composition of expen-
diture also varies among the highest-spending fun-
ders within each category. For example, the dis-
played abortion funders include expenditure as-
sociated withCare/Harm, in addition to the two
largest aggregate foundations. These findings
describe differences in spending associated with
LLM-generated moral annotations; they do not
independently establish funder motives or moral
polarization. Further analysis is provided in Ap-
pendix D.2.
5.4.4 Demographic Exposure Patterns
Finally, we use PPMI to identify topic and moral-
foundation labels that occur disproportionately
among advertisements delivered to particular de-
mographic groups.
Figure 6 shows several descriptive differences
in exposure. In Florida, younger audiences receive
a disproportionate share ofaffordable housingad-

Female AL Female WA
Demographic group
economy
voting rights
education
crime/justice
abortion
environmental protection
(a) Females: AL vs W A
18–24 25–34 35–44 45–54 55–64 65+
Demographic group
economy
affordable housing
crime/justice
abortion (b) All age groups: FL
Male MT Male VA
Demographic group
voting rights
voting
abortion
environmental protection
personal freedom
election integrity
(c) Males: MT vs V A
California
T exas New York Florida
Pennsylvania
Ohio
Demographic group
Care / Harm
Liberty / Oppression
Fairness / Cheating
Authority / Subversion
Loyalty / Betrayal
Sanctity / Degradation (d) Moral framing across selected states
0.0
0.5
1.0
1.5
2.0
2.5
3.0
PPMI
Figure 6:PPMI associations between political issue or moral-foundation labels and observed audience demographics. Higher
values indicate that a label occurs disproportionately among advertisements delivered to the corresponding demographic group.
vertisements, while older audiences show stronger
associations withabortion-related advertising. Ge-
ographic variation is also visible among male audi-
ences: advertisements delivered to males in Mon-
tana show stronger associations withenvironmen-
tal protectionandpersonal freedom, whereas ad-
vertisements delivered to males in Virginia show
stronger associations withvoting.
These patterns demonstrate that issue exposure
varies across demographic groups in the observed
Meta delivery data. Because the dataset describes
realized audience exposure rather than the full set
of advertiser-selected targeting parameters, wedo
notinterpret these associations as direct evidence
of advertiser targeting intent.
6 Conclusion
We introduced a seed-free framework for induc-
ing interpretable topic taxonomies from unlabeled
text corpora. The framework combines embedding-
based clustering with iterative LLM inference,
maintaining a shared topic inventory that expands
as new clusters are processed and is subsequently
used to assign labels across the complete set of
clusters.
We evaluated the framework through a case
study of political advertisements from the month
preceding the 2024 U.S. presidential election. In a
small-scale human evaluation, the induced labels
received similar average ratings to a single-shot
LLM baseline but were selected as the best-fitting
labels more often. We further showed that the re-
sulting taxonomy can support downstream analyses
of issue prevalence, moral framing, advertising ex-
penditure, funding concentration, and demographic
exposure.
The framework is not specific to political ad-
vertising and can be applied to other large, un-
labeled text corpora in which interpretable topic
organization is useful. Future work should evalu-
ate the stability of induced taxonomies across do-
mains, clustering configurations, LLMs, prompts,
and cluster-processing orders, and explore methods
for constructing more robust or hierarchical topic
inventories.
7 Limitations
Our framework depends on the quality of the un-
derlying embeddings and clustering procedure, and
the resulting taxonomy may be sensitive to cluster-
ing parameters and the order in which clusters are
processed. The human evaluation is also small in
scale, and the difference in average rating between
our framework and the single-shot LLM baseline

is modest. Larger evaluations across datasets and
models are needed to assess the robustness of the
approach.
The framework also relies on LLM-generated
labels, which may introduce bias, oversimplify am-
biguous texts, or produce misleading interpreta-
tions (Islam, 2026b; Ji et al., 2023; Blodgett et al.,
2020; Brown et al., 2020). The moral-foundation
labels are generated using topic-conditioned in-
ference and should therefore be interpreted as ex-
ploratory rather than as independent validation of
the induced topics.
Finally, the case study covers approximately one
month of Meta political advertising during the 2024
U.S. election cycle. Its substantive findings may
not generalize to other periods, platforms, or polit-
ical contexts. Meta reports spending and impres-
sions as ranges, and its demographic statistics de-
scribe observed ad delivery rather than necessarily
reflecting advertiser targeting intent.
8 Ethical Considerations
This study uses political advertising data made pub-
licly available through the Meta Ad Library. The
data contain aggregate audience statistics and do
not include personally identifiable information.
As the topic and moral annotations are partly
generated by LLMs, they may reflect model biases
or simplify nuanced political discourse. We there-
fore interpret the resulting patterns descriptively
and avoid treating demographic exposure patterns
as evidence of individual political preferences or
advertiser intent. We report the models, prompts,
and processing details used in our experiments to
support transparency and reproducibility.
9 Acknowledgments
We would like to thank Lightning AI Studio for pro-
viding compute resources. We also thank the anony-
mous reviewers for their thoughtful feedback.
References
Minali Aggarwal, Jennifer Allen, Alexander Coppock,
Dan Frankowski, Solomon Messing, Kelly Zhang,
James Barnes, Andrew Beasley, Harry Hantman, and
Sylvan Zheng. 2023. A 2 million-person, campaign-
wide field experiment shows how digital advertis-
ing affects voter turnout.Nature Human Behaviour,
7(3):332–341.
Areej Alokaili, Nikolaos Aletras, and Mark Stevenson.
2020. Automatic generation of topic labels. InPro-
ceedings of the 43rd international ACM SIGIR con-
ference on research and development in information
retrieval, pages 1965–1968.
Luca Beurer-Kellner, Marc Fischer, and Martin Vechev.
2024. Guiding llms the right way: fast, non-invasive
constrained generation. InProceedings of the 41st In-
ternational Conference on Machine Learning, pages
3658–3673.
David M Blei, Andrew Y Ng, and Michael I Jordan.
2003. Latent dirichlet allocation.Journal of machine
Learning research, 3(Jan):993–1022.
Su Lin Blodgett and 1 others. 2020. Language (technol-
ogy) is power: A critical survey of “bias” in nlp. In
ACL.
Tom Brown and 1 others. 2020. Language models are
few-shot learners.Advances in neural information
processing systems, 33:1877–1901.
Amparo Elizabeth Cano Basave, Yulan He, and Ruifeng
Xu. 2014. Automatic labelling of topic models
learned from twitter by summarisation. Association
for Computational Linguistics (ACL).
Arthur Capozzi, Gianmarco de Francisci Morales, Ye-
lena Mejova, Corrado Monti, André Panisson, and
Daniela Paolotti. 2021. Clandestino or rifugiato?
anti-immigration facebook ad targeting in italy. In
Proceedings of the 2021 CHI Conference on Human
Factors in Computing Systems, pages 1–15.
Jonathan Chang, Sean Gerrish, Chong Wang, Jordan
Boyd-Graber, and David Blei. 2009. Reading tea
leaves: How humans interpret topic models.Ad-
vances in neural information processing systems.
Tianqi Chen and Carlos Guestrin. 2016. Xgboost: A
scalable tree boosting system. InProceedings of
the 22nd acm sigkdd international conference on
knowledge discovery and data mining, pages 785–
794.
Yong Chen, Hui Zhang, Rui Liu, Zhiwen Ye, and Jiany-
ing Lin. 2019. Experimental explorations on short
text topic mining between lda and nmf based schemes.
Knowledge-Based Systems, 163:1–13.
Xiaotong Chu, Lukas Otto, Rens Vliegenthart, Sophie
Lecheler, Claes de Vreese, and Sanne Kruikemeier.
2024. On or off topic? understanding the effects
of issue-related political targeted ads.Information,
Communication & Society, 27(7):1378–1404.
Kenneth Church and Patrick Hanks. 1990. Word associ-
ation norms, mutual information, and lexicography.
Computational linguistics, 16(1):22–29.
Jacob Cohen. 1960. A coefficient of agreement for
nominal scales.Educational and psychological mea-
surement, 20(1):37–46.

Gian M Fulgoni, Andrew Lipsman, and Carol Davidsen.
2016. The power of political advertising: Lessons for
practitioners: How data analytics, social media, and
creative strategies shape us presidential election cam-
paigns.Journal of Advertising Research, 56(3):239–
244.
Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli.
2023. Chatgpt outperforms crowd workers for
text-annotation tasks.Proceedings of the National
Academy of Sciences, 120(30):e2305016120.
Matthew H Goldberg, Abel Gustafson, Seth A Rosen-
thal, and Anthony Leiserowitz. 2021. Shifting re-
publican views on climate change through targeted
advertising.Nature Climate Change, 11(7):573–577.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, and 1 others. 2024. The llama 3 herd
of models.arXiv preprint arXiv:2407.21783.
Maarten Grootendorst. 2022. Bertopic: Neural topic
modeling with a class-based tf-idf procedure.arXiv
preprint arXiv:2203.05794.
Kobi Hackenburg and Helen Margetts. 2024. Evaluating
the persuasive influence of political microtargeting
with large language models.Proceedings of the Na-
tional Academy of Sciences, 121(24):e2403116121.
Jonathan Haidt and Jesse Graham. 2007. When morality
opposes justice: Conservatives have moral intuitions
that liberals may not recognize.Social Justice Re-
search, 20(1):98–116.
Jonathan Haidt and Craig Joseph. 2004. Intuitive ethics:
How innately prepared intuitions generate culturally
variable virtues.Daedalus, 133(4):55–66.
Eitan D Hersh. 2015.Hacking the electorate: How
campaigns perceive voters. Cambridge University
Press.
Melanie Hirsch, Marlis Stubenvoll, Alice Binder, and
Jörg Matthes. 2024. Beneficial or harmful? how
(mis) fit of targeted political advertising on social me-
dia shapes voter perceptions.Journal of Advertising,
53(1):19–35.
Tunazzina Islam. 2025a.Understanding and Analyzing
Microtargeting Pattern on Social Media. Ph.D. thesis,
Purdue University.
Tunazzina Islam. 2025b. Understanding microtargeting
pattern on social media. InProceedings of the AAAI
Conference on Artificial Intelligence, volume 39,
pages 29269–29270.
Tunazzina Islam. 2026a. Reasoning-based refinement
of unsupervised text clusters with LLMs. InFind-
ings of the Association for Computational Linguistics:
ACL 2026, pages 9899–9917, San Diego, California,
United States. Association for Computational Lin-
guistics.
Tunazzina Islam. 2026b. Who gets which message?
auditing demographic bias in LLM-generated tar-
geted text. InFindings of the Association for Com-
putational Linguistics: ACL 2026, pages 9270–9297,
San Diego, California, United States. Association for
Computational Linguistics.
Tunazzina Islam and Dan Goldwasser. 2022. Under-
standing covid-19 vaccine campaign on facebook us-
ing minimal supervision. In2022 IEEE International
Conference on Big Data (Big Data), pages 585–595.
IEEE.
Tunazzina Islam and Dan Goldwasser. 2025a. Can llms
assist annotators in identifying morality frames? -
case study on vaccination debate on social media. In
Proceedings of the 17th ACM Web Science Confer-
ence 2025, Websci ’25, page 169–178, New York,
NY , USA. Association for Computing Machinery.
Tunazzina Islam and Dan Goldwasser. 2025b. Discov-
ering latent themes in social media messaging: A
machine-in-the-loop approach integrating llms. In
Proceedings of the International AAAI Conference on
Web and Social Media, volume 19, pages 859–884.
Tunazzina Islam and Dan Goldwasser. 2025c. Post-hoc
study of climate microtargeting on social media ads
with LLMs: Thematic insights and fairness evalu-
ation. InFindings of the Association for Compu-
tational Linguistics: EMNLP 2025, pages 15838–
15859, Suzhou, China. Association for Computa-
tional Linguistics.
Tunazzina Islam and Dan Goldwasser. 2025d. Uncov-
ering latent arguments in social media messaging
by employing LLMs-in-the-loop strategy. InFind-
ings of the Association for Computational Linguistics:
NAACL 2025, pages 7412–7444, Albuquerque, New
Mexico. Association for Computational Linguistics.
Tunazzina Islam, Shamik Roy, and Dan Goldwasser.
2023a. Weakly supervised learning for analyzing
political campaigns on facebook. InProceedings
of the International AAAI Conference on Web and
Social Media, volume 17, pages 411–422.
Tunazzina Islam, Ruqi Zhang, and Dan Goldwasser.
2023b. Analysis of climate campaigns on social me-
dia using bayesian model averaging. InProceedings
of the 2023 AAAI/ACM Conference on AI, Ethics, and
Society, pages 15–25.
Ravi Iyer, Spassena Koleva, Jesse Graham, Peter Ditto,
and Jonathan Haidt. 2012. Understanding libertar-
ian morality: The psychological dispositions of self-
identified libertarians.PLoS ONE, 7(8).
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan
Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea
Madotto, and Pascale Fung. 2023. Survey of hal-
lucination in natural language generation.ACM com-
puting surveys, 55(12):1–38.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego

de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, and 1 others. 2023.
Mistral 7b.arXiv preprint arXiv:2310.06825.
Preethi Lahoti, Kiran Garimella, and Aristides Gionis.
2018. Joint non-negative matrix factorization for
learning ideological leaning on twitter. InProceed-
ings of the Eleventh ACM International Conference
on Web Search and Data Mining.
Michelle S Lam, Janice Teoh, James A Landay, Jeffrey
Heer, and Michael S Bernstein. 2024. Concept in-
duction: Analyzing unstructured text with high-level
concepts using lloom. InProceedings of the 2024
CHI Conference on Human Factors in Computing
Systems, pages 1–28.
Daniel D Lee and H Sebastian Seung. 1999. Learning
the parts of objects by non-negative matrix factoriza-
tion.nature, 401(6755):788–791.
Yinhan Liu and 1 others. 2019. Roberta: A robustly
optimized bert pretraining approach.arXiv preprint
arXiv:1907.11692.
Davide Magatti, Silvia Calegari, Davide Ciucci, and
Fabio Stella. 2009. Automatic labeling of topics. In
2009 Ninth International Conference on Intelligent
Systems Design and Applications, pages 1227–1232.
IEEE.
Dennis FX Mathaisel and Clare L Comm. 2021. Politi-
cal marketing with data analytics.Journal of Market-
ing Analytics, 9(1).
Leland McInnes, John Healy, and Steve Astels. 2017.
hdbscan: Hierarchical density based clustering.
JOSS.
Leland McInnes, John Healy, and James Melville.
2020. Umap: Uniform manifold approximation
and projection for dimension reduction.Preprint,
arXiv:1802.03426.
Qiaozhu Mei, Xuehua Shen, and ChengXiang Zhai.
2007. Automatic labeling of multinomial topic mod-
els. InProceedings of the 13th ACM SIGKDD in-
ternational conference on Knowledge discovery and
data mining, pages 490–499.
Mert Ozer, Nyunsu Kim, and Hasan Davulcu. 2016.
Community detection in political twitter networks us-
ing nonnegative matrix factorization methods. In
2016 IEEE/ACM international conference on ad-
vances in social networks analysis and mining
(ASONAM), pages 81–88. IEEE.
Maria Leonor Pacheco, Tunazzina Islam, Monal Maha-
jan, Andrey Shor, Ming Yin, Lyle Ungar, and Dan
Goldwasser. 2022. A holistic framework for analyz-
ing the covid-19 vaccine debate. InProceedings of
the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 5821–5839.
Chau Minh Pham, Alexander Hoyle, Simeng Sun, Philip
Resnik, and Mohit Iyyer. 2024. TopicGPT: A prompt-
based topic modeling framework. InProceedings of
the 2024 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long
Papers), pages 2956–2984, Mexico City, Mexico. As-
sociation for Computational Linguistics.
Nils Reimers and Iryna Gurevych. 2019. Sentence-bert:
Sentence embeddings using siamese bert-networks.
arXiv preprint arXiv:1908.10084.
Filipe N Ribeiro and 1 others. 2019. On microtargeting
socially divisive ads: A case study of russia-linked ad
campaigns on facebook. InProceedings of the con-
ference on fairness, accountability, and transparency.
Shamik Roy, Maria Leonor Pacheco, and Dan Gold-
wasser. 2021. Identifying morality frames in political
tweets using relational learning. InProceedings of
the 2021 Conference on Empirical Methods in Natu-
ral Language Processing, pages 9939–9958.
Mirela Silva, Luiz Giovanini, Juliana Fernandes,
Daniela Oliveira, and Catia S Silva. 2020. Face-
book ad engagement in the russian active measures
campaign of 2016.arXiv preprint arXiv:2012.11690.
Samantha Sudhoff, Pranav Perumal, Zhaoqing Wu, and
Tunazzina Islam. 2026. Paid voices vs. public feeds:
Interpretable cross-platform theme-based analysis of
climate discourse.arXiv preprint arXiv:2601.13317.
Ben M Tappin and 1 others. 2023. Quantifying the po-
tential persuasive returns to political microtargeting.
Proceedings of the National Academy of Sciences.
Holly Teresi and Melissa R Michelson. 2015. Wired
to mobilize: The effect of social networking mes-
sages on voter turnout.The Social Science Journal,
52(2):195–204.
Lewis Tunstall, Nils Reimers, Unso Eun Seo Jo, Luke
Bates, Daniel Korat, Moshe Wasserblat, and Oren
Pereg. 2022. Efficient few-shot learning without
prompts.arXiv preprint arXiv:2209.11055.
Xiaojun Wan and Tianming Wang. 2016. Automatic
labeling of topic models using text summaries. In
Proceedings of the 54th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 2297–2305.
Frederik Zuiderveen Borgesius and 1 others. 2018. On-
line political microtargeting: Promises and threats
for democracy.Utrecht Law Review, 14(1):82–96.
A Prompts
Below are the prompts used in the various steps of
the framework. Constrained decoding was imple-
mented with the guidance framework3.
System Prompt
3https://github.com/guidance-ai/guidance

You are a political analyst. You are given
the following set of political ads to ana-
lyze. You will assign the ads a topic that
best summarizes the key issue discussed
in these ads.
A.1 Topic Synthesis
Binary Output
Is there a topic in the following list that
well describes the key issue discussed in
these ads?
Topics:
{{ topics }}
Can the ads be summarized by one of the
previous topics? Answer with "yes" or
"no".
Generate New Topic (User)
In three words or less, describe the is-
sue that ads discuss, summarizing the
topic. Examples: "Abortion", "Climate
Change", etc.
Generate New Topic (Assistant)
A better topic for these ads is: "
The LLM would finish the above, with the quote
(") as a stop token.
A.2 Annotation
System Prompt
You are a political analyst. You are given
the following set of political ads to ana-
lyze: {{ ads }}
Select Topic (User)
Which of the following topics best de-
scribes the key issue discussed in these
ads? Select exactly one topic from the
provided list.
Topics:
{{ topics }}
Summarize (User)
Summarize the main talking point of the
ads. Do so in a single sentence.
Select Moral Foundation (User)
Which of the following moral founda-
tions best describes the arguments used
in the ads about {{ topic }}?
{{ MFs_with_definitions }}
B Moral Foundations Theory
Moral Foundations Theory (MFT) (Iyer et al.,
2012; Haidt and Graham, 2007; Haidt and Joseph,
2004) suggests a theoretical framework for analyz-
ingsixmoral values (i.e., foundations, each with
a positive and a negative polarity) central to hu-
man moral sentiment. MFT states that political
attitudes are shaped bysixcore moral dimensions:
care/harm, fairness/cheating, loyalty/betrayal, au-
thority/subversion, sanctity/degradation, and lib-
erty/oppression.
The definitions given in Table 4 correspond to
the same definitions given to the LLM when assign-
ing moral foundations.
C Substantive Insights: Topic Salience
and Moral Framing
We analyze the distribution of moral framings and
political issues across different demographics to
uncover political microtargeting strategies. We
used the positive pointwise mutual information
(PPMI) to detect topics that appear disproportion-
ately in ads shown to specific demographics, po-
tentially indicating targeted messaging. We vi-
sualize the results of the PPMI analysis in Fig-
ure 6. The plots show the distribution of moral
framings and political issues across different de-
mographics. Some interesting observations include
the differences in ads targeting different states, or
the shift in topics among different age groups in
Florida (Figure 6b). For example,youngpeople
in Florida are more likely to be targeted with ads
related toaffordable housing, whileolderpeople
are more likely to be targeted with ads related to
abortion. This shows generational targeting strate-
gies, where economic concerns are emphasized
for younger groups, while older groups are mobi-
lized onmoralized issueslike abortion.
On the other hand, Figure 6c shows thatenvi-
ronmental protectionandpersonal freedomare
heavily overrepresented amongmaleaudiences
in Montana, whileabortionalso appears mod-
erately elevated. By contrast,maleaudiences
in Virginia are disproportionately exposed tovot-
ing-related advertising. These contrasts highlight

CARE/HARM:It suggests that someone other than the speaker is worthy of compassion or is experiencing harm,
grounded in the values of kindness, tenderness, and care.
FAIRNESS/CHEATING:Emphasizes justice, personal rights, and independence; involves comparing with other groups.
Advocates for equal opportunity and resists those who benefit without contributing (“Free Riders").
LOYALTY/BETRAYAL:Based on the values of loyalty to one’s country and willingness to sacrifice for the group.
Activated by a sense of unity and collective responsibility—“one for all, and all for one".
AUTHORITY/SUBVERSION:Centers on showing respect (or resistance) toward established authority and following
long-standing traditions. It includes maintaining social order and fulfilling the duties tied to hierarchical roles, such as
obedience, respect, and role-based responsibilities.
SANCTITY/DEGRADATION:Beyond religion, this value highlights respect for human dignity and aversion to moral or
physical corruption, promoting purity, self-control, and the belief that the body is sacred and vulnerable to defilement.
LIBERTY/OPPRESSION:Captures the feelings of reactance and resentment people experience when their freedom
is restricted, often leading to collective disdain for authoritarian figures and motivating unity and resistance against
oppression.
Table 4: Six basic moral foundations (Iyer et al., 2012; Haidt and Graham, 2007; Haidt and Joseph, 2004).
how campaign strategies selectively target local-
ized demographic niches: progressive-leaning
issue frames resonate more strongly in
Montana male audiences, whereas mobilization
around law-and-order and electoral process
is more pronounced among Virginia males.
D Substantive Insights: Ad-Level
Analysis
Using the synthesized topics, we annotate individ-
ual ads to enable ad-level analysis. Cluster-level
annotations reveal latent issue and moral structure,
while ad-level annotations enable analysis of spend-
ing, funder concentration, and targeting strategies.
D.1 Top Funders
We examine the concentration of advertising spend
among funding entities across major issue domains.
Figure 4 presents the top 5 funding entities by to-
tal spend for three central issues in the 2024 elec-
tion—economy,abortion, andcrime/justice.
For theeconomy, Figure 4 shows substantial
variation in advertising expenditure among the five
highest-spending funders in the observed corpus.
Stand with Crypto Alliance, Inc. is the largest
displayed spender, at approximately $47,800, fol-
lowed by Americans for Prosperity Action, Inc.
($26,400) and the Congressional Leadership Fund
($22,000). Americans for Prosperity and Invest-
ing in Arkansas spend approximately $17,300 and
$17,100, respectively. These results describe spend-
ing differences among the leading funders; assess-
ing concentration across all economy-related adver-
tising requires accounting for expenditure by the
remaining funding entities.
Forabortion, Figure 4 shows a substantial spend-
ing gap among the five highest-spending funders
in the observed corpus. Florida V oters Against
Extremism4 is the largest displayed spender, with
estimated expenditure of approximately $62,700.
The other four funders spend comparatively similar
amounts: Last Best Place PAC ($18,000), Republic
Restoratives Inc. ($17,500), Colin Allred for Senate
($17,500), and Montanans Securing Reproductive
Rights5 ($17,200). These results highlight differ-
ences in expenditure among the leading funders,
with a pronounced drop from the largest spender to
the remaining four. Assessing concentration across
all abortion-related advertising requires accounting
for expenditure by the remaining funding entities.
In contrast, forcrime/justice, the two highest-
spending funders have similar estimated expendi-
tures: Preserve America PAC ($47,500) and Judi-
cial Fairness PAC ($43,600). The remaining dis-
played funders—Smart and Safe Florida ($26,700),
Stop Houston Murders PAC ($25,700), and Safer
LA County (Hochman for DA) ($21,000)—have
lower, broadly comparable expenditures. These
amounts show a gap between the leading pair and
the other three funders within the displayed group.
Overall, Figure 4 illustrates differences in expen-
diture patterns among the five highest-spending fun-
ders within each issue category. Foreconomyand
abortion, the largest displayed funder spends sub-
stantially more than each of the other four, whereas
crime/justicehas two leading funders with simi-
lar expenditures. These comparisons characterize
spending differences among the leading funders in
4https://dos.elections.myflorida.com/committees
5https://www.influencewatch.org/organization/
montanans-securing-reproductive-rights/

the observed corpus. They do not establish whether
overall spending is more concentrated in one issue
category or whether an issue involves a broader
set of funding entities; evaluating those questions
requires the complete funder-level expenditure dis-
tribution.
D.2 Moral Foundations in Funded Messaging
We examine the relationship between annotated
moral framing and estimated advertising expen-
diture across three issue categories:economy,
crime/justice, andabortion. Figure 5 presents the
distribution of spending across moral foundations
within each topic, together with the corresponding
total expenditure. This aggregate view summarizes
the moral-foundation composition of spending in
the analyzed corpus without disaggregating it by
funding entity.
Figure 4 complements this aggregate view by
comparing the five highest-spending funders within
each of the three issue categories. Each funder’s
expenditure is segmented according to the moral-
foundation labels assigned to its advertisements.
These funder-level comparisons describe the dis-
played organizations rather than the complete pop-
ulation of funders.
For theeconomy,Fairness/Cheatingaccounts
for approximately 59% of topic-level expendi-
ture, followed byLiberty/Oppressionat 25%.
The displayed funders differ in the composi-
tion of their spending. Stand with Crypto Al-
liance, Inc. has expenditure predominantly asso-
ciated withLiberty/Oppression-annotated adver-
tisements. In contrast, Americans for Prosperity
Action, Inc., Americans for Prosperity, and In-
vesting in Arkansas have expenditure primarily
associated withFairness/Cheating. The Congres-
sional Leadership Fund’s expenditure includes both
Fairness/CheatingandLiberty/Oppression, while
smallerLoyalty/Betrayalcomponents appear for
some displayed funders. These patterns show varia-
tion in the annotated moral framing associated with
expenditure among the leading economy-related
funders.
Forcrime/justice, the largest aggregate spending
shares are associated withLoyalty/Betrayal(43%)
andLiberty/Oppression(26%). The funder-level
breakdown reveals different compositions within
this issue category. Preserve America PAC’s ex-
penditure is predominantly associated withLib-
erty/Oppression, whereas Stop Houston Murders
PAC’s expenditure is predominantly associated
withLoyalty/Betrayal. Judicial Fairness PAC has
substantial expenditure associated with bothAu-
thority/SubversionandLoyalty/Betrayal. Thus, the
aggregate distribution does not imply that all dis-
played funders exhibit the same moral-framing pro-
file.
Forabortion,Liberty/OppressionandSanc-
tity/Degradationaccount for approximately 48%
and 34% of topic-level expenditure, respectively.
Among the displayed funders, Florida V oters
Against Extremism and Last Best Place PAC
have expenditure primarily associated withSanc-
tity/Degradation. Republic Restoratives Inc. and
Montanans Securing Reproductive Rights have
expenditure predominantly associated withLib-
erty/Oppression. However, Colin Allred for Sen-
ate’s displayed expenditure is associated with
Care/Harm. The funder-level results therefore in-
clude additional moral foundations beyond the two
largest aggregate categories and should not be re-
duced to a uniform split between liberty-based and
sanctity-based framing.
Taken together, Figures 4 and 5 show differences
in the moral-foundation composition of advertising
expenditure across issue categories and among their
highest-spending funders. These findings describe
spending associated with LLM-generated annota-
tions; they do not independently establish funder
motives, specific policy arguments, or moral polar-
ization. We therefore interpret them as exploratory
patterns in the annotated corpus rather than as inde-
pendently validated accounts of the organizations’
moral or political positions.
