---
title: 'Detecting Deceptive Recruitment: A Signal-theoretic Machine Learning Framework for Early Identification
  of Labour Exploitation'
url: https://arxiv.org/abs/2609.20336
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Sajid Siraj
- Mahnaz Hosseinzadeh
- Amin Vafadarnikjoo
- Shuyang Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.20336
pages: 32
chars: 82692
fetched_at: '2026-11-08T13:20:15+00:00'
kb_version: 1
---

# Detecting Deceptive Recruitment: A Signal-theoretic Machine Learning Framework for Early Identification of Labour Exploitation

Detecting Deceptive Recruitment: A Signal-theoretic Machine Learning
Framework for Early Identification of Labour Exploitation
Sajid Siraja,b,∗, Mahnaz Hosseinzadehc, Amin Vafadarnikjooc, Shuyang Lid
aLeeds University Business School, University of Leeds, Leeds, UK
bCOMSATS University, Wah Campus, Islamabad, Pakistan
cSheffield University Management School, University of Sheffield, Sheffield, UK
dBirmingham Business School, University of Birmingham, Birmingham, UK
Abstract
Deceptive online job advertisements have emerged as a primary pathway into forced labour, yet
systematic detection methods remain underdeveloped due to data scarcity and absence of em-
pirically validated indicators. We formalise this detection challenge as a classification problem
under signalling theory, where exploiters transmit costless signals mimicking legitimate commu-
nications across textual, visual, and structural dimensions. Using 464 verified cases (164 de-
ceptive, 300 legitimate) collected through anti-slavery charities across nine origin countries and
21 industries, we develop multimodal detection models combining computer vision, natural lan-
guage processing, and semantic embeddings. Through systematic feature ablation experiments
and repeated stratified cross-validation, we demonstrate that individual modalities achieve sub-
stantial discriminatory power (ROC-AUC: 0.87–0.97), whilst their integration yields modest
further gains. SHAP-based analysis reveals that text quality and domain-specific risk language
are the primary discriminators, with readability indices, risk keyword density, and visa sponsor-
ship mentions ranking highest, followed by visual colour and texture features. These production
quality gaps reflect resource constraints that prevent exploiters from maintaining professional
standards across all communication channels simultaneously. We operationalise findings through
a proof-of-concept decision support system providing interpretable risk scores for practitioners.
This work demonstrates how rigorous analytical frameworks can address complex humanitarian
operations challenges characterised by information asymmetry and limited ground-truth data.
Keywords:Machine learning classification; Labour supply chain exploitation; Decision
support systems; Deceptive recruitment detection; Humanitarian operations
∗Corresponding author.
Email addresses:s.siraj@leeds.ac.uk(Sajid Siraj),m.hosseinzadeh@sheffield.ac.uk(Mahnaz
Hosseinzadeh),a.vafadarnikjoo@sheffield.ac.uk(Amin Vafadarnikjoo),s.li.10@bham.ac.uk(Shuyang Li)
arXiv:2609.20336v1  [cs.CY]  17 Sep 2026

1. Introduction
Labour exploitation through deceptive recruitment is a major operational challenge for global
supply chains, with an estimated 28 million people in forced labour worldwide [1, 2]. Unlike
product risks traceable through established logistics frameworks, it arises largely from informa-
tion asymmetries in recruitment markets, where vulnerable workers cannot verify employment
claims before accepting positions [3, 4]. This poses a classification problem: distinguishing le-
gitimate from deceptive offers at initial contact, before exploitation occurs [5]. Audit-based
operational risk tools are reactive, intervening only after workers have entered employment [6].
The Operational Research (OR) community has developed sophisticated methods for supply
chain risk detection [7, 8], quality control [9, 10], and fraud identification [11, 12], yet applic-
ation to labour recruitment remains limited. We address this gap by formulating deceptive
recruitment detection as a supervised classification problem, grounded in information economics
and operationalised through machine learning.
The problem suits OR approaches: it involves decision-making under uncertainty with high-
dimensional, multimodal data (text, images, metadata), with risk minimisation through early
intervention as the operational objective. Unlike typical classification problems, however, forced
labour detection operates under severe data scarcity, since verified cases require collaboration
with anti-trafficking organisations and victim consent [13]. Interventions also remain down-
stream: workplace audits follow exploitation [6, 14], and digital tools, while improving supply
chain visibility, mostly monitor working conditions rather than detecting deceptive signals at
source [15, 16]. The recruitment stage, where workers first encounter misleading offers, thus
remains largely unexamined, creating a need for accessible, theory-driven tools that identify
deceptive cues before exploitation occurs.
This study develops a proof-of-concept AI-driven decision support system (DSS) identify-
ing deceptive job advertisements linked to forced labour. Using 464 verified advertisements
(164 linked to confirmed forced labour cases) collected through partnerships with anti-slavery
organisations in the UK, Nepal, and Bangladesh, we combine machine learning classification
with SHAP (SHapley Additive exPlanations) explainability to identify reliable textual, visual,
and structural indicators of deception. We formalise detection as a classification problem under
signalling theory, in which exploiters transmit costless signals mimicking legitimate communic-
ations across multiple dimensions. The DSS returns interpretable risk scores in real time for
supply chain auditors, digital platforms, and labour market regulators.
2

The research addresses three operational questions:
1. What observable features in job advertisements (textual, visual, structural) discriminate
deceptive from legitimate recruitment offers?
2. How do standard supervised learning algorithms (Logistic Regression, Random Forest,
XGBoost) perform on this classification task when trained on verified ground-truth data,
and what performance trade-offs emerge under class imbalance?
3. How does signalling theory provide a coherent information-theoretic framework for inter-
preting model outputs and explaining why specific features predict exploitation risk?
This work contributes to OR in humanitarian operations by showing how information-
theoretic models can guide feature engineering in resource-constrained classification. SMOTE
(Synthetic Minority Oversampling Technique)-based class balancing with nested cross-validation
offers a template for data scarcity in sensitive social domains where sample expansion faces eth-
ical constraints. That the interpretable NLP+Visual set matches the full multimodal set, with
visual features adding only a modest gain over text alone, is consistent with deceptive signals
manifesting partly through cross-modal inconsistency: professional text paired with comprom-
ised imagery, or the reverse. Practically, the DSS gives auditors, platforms, and regulators a
scalable screening tool, shifting intervention from reactive workplace monitoring to proactive
communication analysis.
Section 2 reviews the literature on labour supply chains, digital detection tools, and signalling
theory, identifying the research gaps this study addresses; Section 3 presents the methodology.
2. Literature review
2.1. Labour supply chain and deceptive recruitment
Forced labour in supply chains is increasingly understood as a structural outcome of global
sourcing regimes rather than isolated non-compliance: cost minimisation and compressed de-
livery timelines systematically generate vulnerabilities that enable exploitation [17, 18, 3, 14].
This literature expanded following regulatory interventions such as the UK Modern Slavery Act
[2], but focuses predominantly on downstream detection and remediation within product and
service supply chains [6, 19, 20], leaving the labour supply chain [21], particularly recruitment,
comparatively under-theorised [22, 4, 5]. This matters because recruitment is the primary entry
point through which structural pressures translate into coercive labour relations.
3

Deceptive recruitment is now recognised as a central pathway into forced labour: workers are
misled about wages, contracts, or conditions and subsequently trapped through debt, document
confiscation, or coercion [17, 23, 24, 25], with intermediaries exploiting migrant vulnerabilities
through contract substitution, fee charging, and misinformation [26]. These practices remain
largely invisible to audit and compliance systems that prioritise workplace conditions over re-
cruitment processes [22, 4], leaving exploitative brokers unchecked [6].
Job advertisements are a primary medium through which such deception is transmitted. As
the first point of contact they often misrepresent pay, hours, or benefits, especially across borders
where verification is difficult [5, 13], allowing intermediaries to exploit workers’ aspirations for
mobility while obscuring risk [27]; workers who respond may enter arrangements bearing little re-
semblance to the original offer [15]. Yet advertisements remain outside due diligence frameworks,
leaving the earliest stage of exploitation unmonitored [28]. Existing responses (targeted audits
and worker interviews) illuminate recruitment pathways ex post [6] but are labour-intensive and
workplace-focused, and regulatory initiatives such as zero-fee recruitment do not capture mis-
leading signals embedded in advertisements [3, 29, 30]. A further constraint is the scarcity of
verified ground-truth data, with prior studies relying on expert judgement or manual coding of
small samples [31, 32, 5].
2.2. Digital tools for labour supply chain monitoring and recruitment detection
Digital technologies are increasingly proposed as complements to audits, which often detect
exploitation only after harm has occurred [18, 33, 6, 34]. Blockchain, mobile reporting, and
traceability systems aim to create tamper-resistant records and direct communication channels
that capture recruitment data audits overlook [15, 28, 35, 16]. Adoption, however, is uneven and
context-dependent: many initiatives operate at pilot scale and presuppose digital infrastructure,
literacy, and worker access often lacking among vulnerable populations [16, 35], since migrants
targeted by deceptive recruiters frequently cannot engage with complex systems such as block-
chain [36], and most intervene after recruitment, monitoring employment conditions rather than
preventing deception at the point of job search [5].
This gap is salient given recruiters’ reliance on online platforms, where brokers disseminate
misleading offers at scale under weak oversight [13], and such postings often carry linguistic
and contextual cues associated with exploitation [5, 32]. AI-based research nonetheless remains
fragmented, focusing largely on sex trafficking detection using public social media datasets with
non-verified labels [27, 37, 13], so empirical work on forced labour indicators embedded in job ad-
4

vertisements remains limited and conceptually underdeveloped [32, 5]. Adjacent work illustrates
the same gap: machine learning models detected fraudulent job advertisements using expert-
labelled data [38], whilst unsupervised topic modelling (LDA and LSI) was applied to Facebook
advertisements in the Dutch labour market in collaboration with law enforcement [39]. Both are
methodologically informative but limited: the former targets financial fraud rather than labour
exploitation, the latter relies on salary discrepancy as a proxy for forced labour outcomes rather
than verified cases, achieving F1 of 0.61.
2.3. Job advertisement and deceptive cues of labour exploitation
Recent studies examine how job advertisements signal pathways into forced labour. Drawing on
UNODC (United Nations Office on Drugs and Crime) indicators [40], observable cues such as
promises of accommodation, absent skill requirements, and excessive hours were operationalised
and applied to online postings [32], an important step toward operationalisation, but one relying
on manual coding and frequency counts rather than empirical validation of predictive power.
Individual indicators rarely signify exploitation in isolation, and risk emerges from combinations
of cues that manual approaches struggle to capture at scale and that remain vulnerable to
subjectivity, leaving existing studies largely descriptive.
Qualitative research reinforces these concerns: digital ethnography shows traffickers deploy-
ing informal language, emojis, urgency cues, and trusted-brand references in social media job
advertisements [5], but the absence of verified ground-truth data constrains generalisability and
prevents such cues from being systematically deployed for automated screening. Advancing the
field therefore requires theory-driven, data-driven methods capable of testing recruitment signals
against confirmed exploitation outcomes, which motivates the framework introduced next.
2.4. Signalling theory and deceptive signalling
Signalling theory offers a lens for examining how information is transmitted and interpreted
under uncertainty [41]. Developed in labour economics, it explains how a signaller and a receiver
communicate under information asymmetry [42]: signallers with high-quality but unobservable
attributes provide credible, costly signals that lower-quality counterparts cannot easily mimic,
allowing receivers to identify quality and allocate resources accordingly [43, 44]. The theory has
been applied to explain why firms attract investors [45, 46], secure customer trust [47], or hire
strong candidates [48].
An important and under-examined stream concernsdeceptivesignalling, that is, signals that
appear costly to receivers but are in fact costless [49], where lower-quality signallers mimic high-
5

quality signals and conceal their weaknesses. Generative AI and the expanded reach of digital
platforms have intensified the problem, making deceptive signals cheaper to produce and faster
to disseminate [49]. Recruitment markets are fertile ground: workers lack reliable information
about job quality and conditions, especially for opportunities advertised online or across borders,
whilst recruiters and brokers control much of the information shaping workers’ perceptions. Here
the signal is the job advertisement itself, conveying the sender’s intentions and abilities [50],
and fraudulent recruiters can mimic legitimate communications (polished language, familiar job
titles, references to well-known brands) at little cost. Little is known, however, about how
exploiters strategically construct and manipulate recruitment signals in digital labour markets,
which requires extending signalling theory to costless, multimodal, strategically deceptive signals
operating across textual, visual, and structural dimensions.
2.5. Research gaps and positioning
The literature reveals four interconnected gaps that this research addresses.
Gap 1: Theoretical framework for deception detection.Signalling theory has been
applied to quality disclosure [43] and supplier selection [46], but its application to labour recruit-
ment remains underdeveloped, lacking formal models of how exploiters strategically manipulate
multimodal signals (text, visuals, structure) to create pooling equilibria in which deceptive of-
fers become indistinguishable from legitimate ones. This limits understanding ofwhycertain
features predict exploitation risk.
Gap 2: Empirically validated detection indicators.Prior work [32, 5] identifies po-
tential deception cues through expert judgement and manual coding, but lacks ground-truth
validation against verified forced labour outcomes, statistical evidence of discriminatory power,
and quantification of effect sizes. Reliance on synthetic [38] or self-labelled [27] data in adjacent
domains (employment scams, sex trafficking) further limits transferability to labour exploitation.
Gap 3: Multimodal feature analysis.Detection approaches focus predominantly on
textual content [32, 37], overlooking visual and structural signals. No prior study systemat-
ically compares the relative importance of textual keywords, visual design attributes (colour,
brightness, object context), and semantic embeddings in predicting forced labour risk, leaving
practitioners without evidence on which signal dimensions to prioritise in screening.
Gap 4: Explainable detection systems.Machine learning has been applied to trafficking
detection [13], but the black-box nature of complex algorithms limits deployment in humanit-
arian contexts requiring stakeholder accountability, offering no interpretable account ofwhy
6

an advertisement is classified high-risk and preventing auditors and regulators from validating
model reasoning or identifying systematic biases.
We address these gaps by (1) formalising deceptive recruitment as a classification problem
under signalling theory, providing information-theoretic foundations for feature engineering; (2)
constructing and validating models on 464 verified cases (164 forced labour, 300 legitimate)
collected through anti-slavery organisations; (3) systematically comparing textual, visual, and
structural features using SHAP-based explainability; and (4) developing a proof-of-concept DSS
that operationalises the findings with interpretable risk scores. This positions the work at
the intersection of operational research methodology, humanitarian operations, and information
economics.
3. Methodology
This section presents the OR framework for deceptive recruitment detection, structured in six
components: problem formalisation, data collection, feature engineering, implementation, ex-
perimental design for feature ablation studies, and evaluation.
3.1. Problem formalisation: Signalling theory framework
We formalise job advertisements as signals transmitted from employers (senders) to jobseekers
(receivers) under information asymmetry. Letθ∈ {L, H}denote the unobservable quality
type of a posting, whereLrepresents deceptive advertisements leading to forced labour and
Hrepresents legitimate employment offers. A signals= (s text, svisual, sstruct)comprises textual
content, visual attributes, and structural features extracted through natural language processing
and computer vision.
In classical signalling equilibria [42], high-quality senders differentiate themselves through
costly signals satisfying the single-crossing property:c(s, H)< c(s, L), wherec(·)denotes
signal production cost. However, digital recruitment markets enable costless mimicry where
c(sdeceptive, L)≈c(s deceptive, H)≈0, producing a pooling equilibrium where low-quality recruit-
ers mimic legitimate communications at minimal expense [49]. Jobseekers facing signalscannot
reliably compute the posterior probabilityP(θ=L|s)without analytical tools.
Our classification framework operationalises the receiver’s inference problem by constructing
f:S →[0,1]estimatingP(θ=L|s) =f(x;β), wherex∈R p is ap-dimensional feature
vector andβrepresents learned parameters. The classifier functions as a signal decoder exploit-
ing distributional differences between deceptive and legitimate signals invisible to individual
7

receivers. The operational objective is improving jobseekers’ risk estimation, enabling better
decision-making under uncertainty.
The framework yields three predictions that we statea priori, before estimating any model,
and evaluate against the empirical results in Sections 4.2–4.3:
•P1 (cost asymmetry).Signals whose production is bound to underlying resource con-
straints, and which therefore remain costly for deceptive senders to fake (vocabulary soph-
istication, domain-specific operational content, image production quality), should carry
greater discriminatory weight than surface cues that are cheap to mimic or post-hoc edit
(e.g. spelling correctness, superficial formatting).
•P2 (cross-modal complementarity).Because exploiters face binding resource con-
straints, deceptive advertisements should exhibit inconsistency across modalities; a mul-
timodal feature set should therefore weakly dominate any single-modality set in discrim-
inatory power, rather than yielding large super-additive gains.
•P3 (partial separability).Observable multimodal signals should partially separate the
latent typesθ∈ {L, H}, so that a decoder trained on them attains substantially better-
than-chance discrimination despite the pooling equilibrium faced by individual receivers.
3.2. Data collection and verification protocol
Data collection for forced labour research faces methodological constraints absent in typical OR
classification problems: verified positive cases require access to victim testimonies and anti-
trafficking case files, imposing strict ethical protocols and limiting sample size. We addressed
these constraints through partnerships with two anti-slavery organisations: Causeway (United
Kingdom) and Migration Dristi (Nepal and Bangladesh). Both organisations maintain detailed
case records with documented victim outcomes, enabling verification that advertisements genu-
inely led to forced labour rather than financial scams or other forms of fraud.
Between April 2022 and April 2024, practitioners systematically collected 164 high-risk ad-
vertisements meeting three criteria: (1) victims responded to the posting and were recruited
through the advertised position; (2) subsequent employment conditions met ILO forced labour
indicators (threat of penalty, restriction of movement, debt bondage, or withholding of wages);
and (3) case documentation included the original advertisement. This verification protocol en-
sures ground-truth accuracy.
8

Ground-truth provenance.The class labels were not produced by a post-hoc annotation
exercise carried out by the research team, so conventional inter-rater agreement statistics do not
apply. The positive class comprises advertisements that the partner anti-slavery organisations
had already verified, through their own casework, as having led to a documented forced-labour
outcome; the organisations supplied the de-identified advertisements together with this verified
status. To protect victims, no victim identities, testimonies, or case files were shared with the
research team, and the organisations’ internal verification procedures are operational records
we are not in a position to document in detail. Each advertisement therefore carries a single
authoritative label, determined by the organisation that handled the case rather than by mul-
tiple independent research coders, so an inter-rater reliability coefficient is neither available nor
meaningful. The negative class was vetted by the partner organisations’ experts for reputa-
tional standing and regulatory compliance. We regard this externally determined ground truth
as a strength: each positive case is a confirmed real-world outcome rather than a proxy or
self-reported label, verified by the practitioners closest to the case.
For negative class representation, we assembled 300 legitimate advertisements from verified
employers across similar job domains, vetted by charity experts to ensure reputational standing
and regulatory compliance. This sampling strategy maintains distributional similarity between
classes (same industries, geographic routes, skill levels) while ensuring outcome differences, crit-
ical for identifying discriminative features rather than spurious correlations.
Advertisement sources.The advertisements were supplied by the partner organisations
as part of documented cases, rather than collected by the research team from named platforms.
They are online recruitment advertisements that the workers concerned had encountered. Sys-
tematic platform-of-origin metadata was not retained for each item, so we characterise the corpus
by its content rather than by source platform. The information available for each advertisement,
and used by the models, is what a jobseeker sees at the point of screening: the advertisement
text, the accompanying image(s), and the advertised contact method (illustrated in Figure 2).
Analysis of source-specific performance would require provenance metadata that this dataset
does not carry, which we note as a direction for future data collection.
The resulting dataset comprisesn= 464advertisements with class distributionn L = 164
(deceptive, 35.3%) andnH = 300(legitimate, 64.7%). Geographic coverage includes nine origin
countries and multiple destination regions (Europe, North America, Middle East, East Asia),
spanning 21 industry sectors: agriculture, hospitality, care work, automotive, manufacturing,
9

retail, logistics, construction, food production, and information technology. Figure 1 summarises
the flow from assembled cases through screening and inclusion to the stratified train–test split.
Verified advertisements assembled
464 advertisements
(164 deceptive forced-labour cases; 300
charity-vetted legitimate postings)
Screened for eligibility
usable image and text con-
firmed; ILO forced-labour out-
come verified for every positive case
Included for analysis
464 advertisements: 164 decept-
ive (35.3%), 300 legitimate (64.7%)
Stratified 80/20 split
Train: 371 (131 deceptive / 240 legitimate)
Test: 93 (33 deceptive / 60 legitimate)
Figure 1: Data flow from verified-case assembly to the analysis sample and the stratified train-test split (PRISMA-
style).
URGENT HIRING — Factory Helpers Needed ABROAD (No Experience)
Good salary guaranteed!Free visa + free accommodationprovided. Immediate
joining. Limited seats!! Company arranges everything.
Roles: packing, loading, general helper. Age 20–40.
Contact on WhatsApp: +xx xxxxx xxxxx — message now, don’t miss this chance!
[Accompanying image: low-resolution photograph of a generic warehouse; no company logo,
address, or registration detail.]
Figure 2: Synthetic, illustrative reconstruction of a deceptive job advertisement, showing the in-situ structure our
features target: urgency and scarcity cues, visa/accommodation sponsorship offers, an informal messaging-app
contact channel, and low-quality imagery lacking verifiable employer detail. This is a fabricated example for
exposition only; no real advertisement, victim, or identifying information is reproduced, in line with safeguarding
requirements. Full original advertisements cannot be shared for the same reason.
3.3. Multimodal feature engineering pipeline
Feature extraction transforms raw advertisement data (images, text, metadata) into feature
vectors spanning three modalities. After zero-variance filtering (removing YOLO object-class
columns never detected across the 464 advertisements), the retained set comprises 922 dimen-
sions in the full configuration and 154 in the NLP+Visual configuration: 94 visual, 60 engineered
10

textual, and 768 embedding dimensions. The complete feature inventory, with per-category di-
mension counts, is given in Supplementary Table S4.
Visual featuresspan low-level pixel intensity and colour statistics, mid-level texture and
composition metrics (Local Binary Patterns, Grey-Level Co-occurrence Matrix, edge density,
sharpness, symmetry), and high-level per-class YOLO object-detection flags. Object detection
uses YOLOv8n trained on the COCO 80-class vocabulary; flags represent pixel-pattern matches
within that vocabulary rather than semantic concept recognition, a distinction relevant to in-
terpreting individual YOLO-derived features (see Section 6).
Textual featuresare extracted via multilingual OCR (EasyOCR; Hindi, Urdu, Bangla,
English) and cover basic text structure, quality metrics (Flesch, Gunning Fog, Coleman-Liau,
and Flesch-Kincaid readability indices, spelling and grammar error rates, sentiment polarity),
domain-specific risk keywords (visa sponsorship, seasonal work, accommodation, work permits,
informal contact channels such as WhatsApp), psychological triggers, NRC Lexicon emotion
intensities, and composite risk indicators.
Structural featurescomprise BERT-base-multilingual-cased embeddings (768 dimensions)
encoding contextual word relationships and rhetorical structures, used in the comprehensive
baseline but excluded from the interpretable NLP+Visual configuration due to inference-time
computational constraints.
3.4. Supervised classification models
We implement three supervised learning algorithms enabling comparative assessment across fea-
ture configurations; results tables abbreviate them as LR, RF, and XGB respectively.Logistic
Regression (LR)estimates deception probability via maximum likelihood withL2 regularisa-
tion (C∈ {0.01,0.1,1,10}), providing maximum interpretability through transparent coefficient
inspection, which is critical for operational deployment.Random Forest (RF)constructs
bootstrap-aggregated decision tree ensembles with variable ensemble size (n_estimators∈
{50,100,200}) and tree complexity (max_depth∈ {None,10,20}), naturally handling nonlinear
relationships though with reduced interpretability.XGBoost (XGB)implements sequential
tree construction with tuned boosting rounds (n_estimators∈ {50,100,200}) and learning rate
(learning_rate∈ {0.01,0.1,0.3}), often achieving superior performance on imbalanced data.
To address the 35.3%/64.7% class imbalance, we apply SMOTE (Synthetic Minority Over-
sampling Technique) during training, generating synthetic minority class examples by interpol-
ating between existing instances, applied only to training folds to ensure evaluation reflects true
11

performance on unseen imbalanced distributions.
3.5. Experimental design: Systematic feature ablation studies
A central methodological contribution is the systematic evaluation of feature modality con-
tributions through controlled ablation experiments. We implement six distinct experimental
configurations isolating and combining feature modalities, enabling direct quantification of each
modality’s marginal contribution through performance comparison.
Configuration 0: Keyword-only baseline(p= 22) uses only the domain-specific risk
keyword and psychological trigger binary features, representing the simplest possible theory-
driven screening rule. This provides a reference point against which the value of adding visual
and quality features can be assessed.Configuration 1: Visual features only(p= 94) isol-
ates visual low-level, mid-level, and high-level features, testing whether image attributes alone
provide sufficient discriminatory power.Configuration 2: NLP features only(p= 60)
includes text basic, text quality, risk keywords, psychological triggers, emotions, and composite
risk indicators, evaluating textual signal detection independent of visual and semantic informa-
tion.Configuration 3: Embeddings only(p= 768) uses solely BERT-generated semantic
representations, assessing whether deep contextual embeddings capture exploitation patterns
without explicit feature engineering.Configuration 4: NLP + Visual(p= 154) combines
textual and visual features while excluding embeddings, testing whether engineered features suf-
fice without deep learning representations.Configuration 5: All features(p= 922) serves as
the comprehensive baseline, incorporating visual, textual, and structural features simultaneously
to establish maximum achievable performance. All feature counts reflect post-filtering values
after zero-variance columns are removed.
For each configurationc∈ {0, . . . ,5}, we train all three algorithms independently, yielding
16 distinct model-configuration combinations (three algorithms across five full feature configur-
ations, plus the keyword-only logistic regression baseline). The ablation framework addresses
three analytical objectives: (i)Modality sufficiency: do visual or textual features alone achieve
competitive performance, or is multimodal integration necessary? (ii)Engineered vs. learned
features: can BERT embeddings replace manual feature engineering, or do explicit indicators
provide complementary information? (iii)Interaction effects: does combining modalities yield
superadditive performance gains, suggesting that deceptive signals manifest through cross-modal
inconsistencies?
12

3.6. Evaluation framework
Model evaluation follows a rigorous train-test protocol applied uniformly across all experimental
configurations. Weimplementstratified80/20train-testsplitting, yielding371traininginstances
(131 deceptive, 240 legitimate) and 93 test instances (33 deceptive, 60 legitimate). Stratification
ensures test set class proportions match the full dataset (35.3%/64.7%), preventing evaluation
bias from unrepresentative sampling.
SMOTE application.SMOTE (Synthetic Minority Oversampling Technique) is applied
exclusively to the training partition after the stratified split, generating synthetic minority-class
examples by interpolating between existing instances. This produces a balanced 480-instance
training set whilst preserving the natural 35.3%/64.7% imbalance in the held-out test partition,
ensuring that reported performance metrics reflect realistic operating conditions rather than an
artificially balanced distribution.
Hyperparameter tuning.For each algorithm-configuration pair, we conduct grid search
with5-foldstratifiedcross-validationonthetrainingset, selectinghyperparameterconfigurations
maximising ROC-AUC score. All continuous features undergo z-score standardisation (zero
mean, unit variance) fitted on training data and applied to test data, preventing data leakage.
Uncertainty quantification.We compute 95% bootstrap confidence intervals (2,000 res-
ampling iterations, percentile method) on both ROC-AUC and PR-AUC for each held-out test
evaluation. To provide generalisation estimates less sensitive to a single partition, we addition-
ally conduct repeated stratifiedk-fold cross-validation (5 folds×10 repeats,k×r= 50outer
folds) with inner 5-fold GridSearchCV for hyperparameter selection within each outer fold, con-
stituting a true nested cross-validation. SMOTE is re-applied inside each training fold to prevent
synthetic samples from appearing in validation partitions. This repeated CV procedure yields
mean±standard deviation performance estimates across 50 fold realisations.
Calibration.We report the Brier score (mean squared error between predicted probabilities
and binary outcomes; lower is better) and produce reliability diagrams (five equal-frequency
bins) for each model (Figure 3), enabling assessment of probabilistic output quality beyond
discrimination metrics.
Performance metrics.We employ six complementary metrics: Accuracy (overall cor-
rectness), Precision (proportion of flagged advertisements truly deceptive), Recall (sensitivity;
reflects operational priority of minimising missed exploitation cases), F1-Score (harmonic mean
of precision and recall, preferable to accuracy under class imbalance), ROC-AUC (Area Under
13

the Receiver Operating Characteristic curve; primary discrimination metric, threshold-invariant
[51]), and PR-AUC (Area Under the Precision-Recall curve; co-primary metric, more inform-
ative than ROC-AUC under class imbalance as it explicitly penalises false positives relative to
true positives).
3.7. Explainability analysis: SHAP decomposition
To ensure model transparency and operational deployability, we implement SHAP analysis [52,
53] on the best-performing model. SHAP assigns each feature a Shapley value representing its
marginal contribution to predictions, computed by averaging contributions across all possible
feature subsets.
We compute SHAP values using algorithm-specific implementations:LinearExplainerfor
Logistic Regression andTreeExplainerfor Random Forest and XGBoost. Analysis yields: (1)
Global feature importance: average absolute SHAP values across all test instances, rank-
ing features by systematic influence on predictions; (2)Local explanations: instance-specific
SHAP values showing why individual advertisements receive particular risk scores; (3)Direc-
tional effects: sign of SHAP value indicates whether feature presence increases or decreases pre-
dicted exploitation risk; (4)Category-level contributions: aggregating SHAP values within
feature categories quantifies modality-specific explanatory power, validating ablation study find-
ings through complementary analysis.
3.8. Statistical comparison framework
To rigorously compare performance across experimental configurations, we report: (1)Within-
configuration model comparison: for each configuration, we identify the best-performing
algorithm via ROC-AUC maximisation, reporting full confusion matrices and all five perform-
ance metrics; (2)Cross-configuration analysis: we compute performance differences∆AUC =
AUCall−AUCsubset betweenthecomprehensivemodelandablatedvariants, quantifyingmarginal
contributions of excluded modalities; (3)Relative performance preservation: we calculate
ρ= AUCsubset AUCall to assess what proportion of maximum performance each subset achieves.
4. Results
Findings are organised in three parts: descriptive feature analysis (Section 4.1), classification
performance across experimental configurations (Section 4.2), and SHAP-based feature import-
ance revealing discriminatory mechanisms (Section 4.3).
14

4.1. Descriptive analysis: Univariate feature distributions
We first establish baseline distributional differences between deceptive (n= 164) and legitimate
(n= 300) advertisements through univariate tests, confirming that observable features carry
discriminatory signal. Full results for continuous features (t-tests with Cohen’sd) and binary
features (chi-square) appear in Supplementary Tables S1 and S2; key findings follow.
4.1.1. Key distributional patterns
Visual featuresshow medium effect sizes for texture and sharpness rather than colour. Decept-
ive advertisements are less sharp (Laplacian varianced=−0.51,p <0.001), with lower textural
contrast (GLCMd=−0.42) and edge density (d=−0.31), consistent with low-resolution, heav-
ily compressed, or screenshot graphics; brightness and saturation show no significant differences
(p >0.05). Object detection is more nuanced: airplane imagery is more prevalent in deceptive
postings (4.9% vs. 0%,p <0.001), whilst books appearmoreoften in legitimate ones (26.0% vs.
8.5%,p <0.001), suggesting richer, contextually appropriate imagery in professionally produced
content. Boats, backpacks, and traffic signage showed no significant differences (p >0.10).
Textual featuresyield the strongest discriminator in the feature set: the Coleman-Liau
readability index (d=−1.21,p <0.001), with deceptive advertisements scoring substantially
lower, indicating simpler, shorter-word vocabulary. Flesch readability (d= 0.87) and Flesch-
Kincaid Grade (d=−0.60) corroborate this. Notably,spelling error rate does not differ sig-
nificantlybetween classes (p= 0.107), challenging the intuitive assumption that deceptive ads
contain more typos; grammar error rate (d= 0.55) and word count (d=−0.51) discriminate
more reliably. Risk keywords show the most extreme prevalence gaps: visa/sponsorship termin-
ology (48.8% vs. 3.7%,χ2 = 134.0) and work permit references (28.7% vs. 0.0%,χ2 = 92.5) are
near-exclusive to deceptive postings, alongside informal contact channels (WhatsApp: 24.4% vs.
7.0%).
Emotional contentis counter-intuitive: all positive emotions (anticipation,d=−0.66;
trust,d=−0.54; joy,d=−0.54) are significantlylowerin deceptive advertisements, as legitim-
ate ones use richer affective language to persuade qualified candidates. The pattern extends to
psychological triggers: money terms (68.0% vs. 47.6%) and urgency language (38.0% vs. 27.4%)
aremore commonin legitimate advertisements (p <0.001andp= 0.029). Deceptive advertise-
ments are thus affectively impoverished, terse and emotionally neutral, rather than manipulative
as originally hypothesised.
These univariate differences are systematic across visual, textual, and emotional dimensions,
15

but differ substantively from prior qualitative accounts. Critically, no single feature separates
the classes perfectly, since even the strongest discriminator (Coleman-Liau,d=−1.21) overlaps,
validating the multivariate approach: reliable detection requires joint consideration of multiple
signals rather than thresholds on individual features.
4.2. Classification performance across experimental configurations
This subsection presents classification results across six experimental configurations designed to
systematically evaluate the discriminatory power of different feature modalities and establish a
keyword-based baseline. Each full configuration was evaluated using three supervised learning
algorithms (Logistic Regression, Random Forest, and XGBoost) trained with SMOTE-based
class balancing and hyperparameter optimisation via 5-fold cross-validation. Performance is
assessed on the held-out test set (93 advertisements: 33 deceptive, 60 legitimate). Bootstrap 95%
confidence intervals for ROC-AUC and PR-AUC are estimated over 2,000 resamples; calibration
quality is measured via the Brier score (lower is better). Generalisation stability is further
evaluated via 5×10 repeated stratified cross-validation on the full training set (Table 3).
4.2.1. Keyword-only baseline and comprehensive feature set
A keyword-only logistic regression baseline on 22 domain-specific risk keyword features (Con-
fig. 0) achieves ROC-AUC 0.867 [95% CI: 0.776–0.940] and PR-AUC 0.806. Simple keyword
matching therefore carries substantive discriminatory power, yet the full multimodal models
add a consistent+0.13 ROC-AUC, justifying the further feature engineering.
The comprehensive model using all 922 features (visual 94, engineered textual 60, and BERT
embeddings 768) establishes the discriminatory ceiling. Table 1 compares the three algorithms
and Table 2 gives the corresponding confusion matrices.XGBoost discriminated best, with
ROC-AUC 0.994 [95% CI: 0.983–1.000], PR-AUC 0.990, and the lowest Brier score overall
(0.034); Logistic Regression attained the highest precision (1.000) and F1 (0.935), with Random
Forest matching its recall (0.879). On the held-out test set XGBoost classified 28 of 33 deceptive
advertisements correctly (five false negatives) and 59 of 60 legitimate ones (one false positive);
all derived metrics in Tables 1 and 2 follow from these counts.
4.2.2. Individual modality performance and combined configurations
We trained models on isolated feature subsets to quantify each modality’s contribution; Table 4
summarises all six configurations.
Visual features alone(94) achieved ROC-AUC 0.866 [CI: 0.782–0.939] with XGBoost,
16

Table 1: Model performance comparison for comprehensive feature set (allp= 922features)
Model Acc. Prec. Rec. F1 ROC-AUC [95% CI] PR-AUC [95% CI] Brier
LR0.957 1.000 0.879 0.9350.988 [0.968–1.000] 0.982 [0.952–1.000] 0.036
RF 0.946 0.9670.8790.921 0.993 [0.977–1.000] 0.989 [0.963–1.000] 0.096
XGB 0.935 0.966 0.848 0.9030.994 [0.983–1.000] 0.990 [0.969–1.000] 0.034
Note:Metrics on held-out test set (n= 93: 33 deceptive, 60 legitimate). 95% CIs via percentile
bootstrap (2,000 iterations). All models trained with SMOTE (training folds only) and 5-fold Grid-
SearchCV. Bold = best value per metric. LR = Logistic Regression, RF = Random Forest, XGB =
XGBoost.
Table 2: Confusion matrices on the held-out test set (n= 93: 33 deceptive, 60 legitimate) for the comprehensive
feature set (p= 922). All metrics in Table 1 are derived from these counts.
Model TP FN FP TN
LR 29 4 0 60
RF 29 4 1 59
XGB 28 5 1 59
Note:Positive class = deceptive. TP+FN= 33(deceptive) and FP+TN= 60(legitimate) for every
model, confirming arithmetic consistency. LR = Logistic Regression, RF = Random Forest, XGB =
XGBoost.
Table 3: Generalisation under 5×10 repeated stratified cross-validation (NLP+Visual,p= 154)
Model Accuracy F1-Score ROC-AUC PR-AUC Brier
LR0.915±0.023 0.880±0.033 0.968±0.016 0.959±0.015 0.062±0.015
RF0.945±0.022 0.920±0.033 0.982±0.010 0.974±0.013 0.065±0.008
XGB0.941±0.024 0.916±0.035 0.982±0.012 0.972±0.0190.048±0.021
Note:Mean±std across 50 outer folds (5 repeats×10 folds). XGBoost and Random Forest achieve
near-identical AUC with XGBoost yielding superior calibration. LR = Logistic Regression, RF =
Random Forest, XGB = XGBoost.
17

0.0 0.2 0.4 0.6 0.8 1.0
Mean predicted probability
0.0
0.2
0.4
0.6
0.8
1.0Fraction of positives
Logistic Regression
(Brier=0.0404)
Perfect
Logistic Regression
0.0 0.2 0.4 0.6 0.8 1.0
Mean predicted probability
Random Forest
(Brier=0.0590)
Perfect
Random Forest
0.0 0.2 0.4 0.6 0.8 1.0
Mean predicted probability
XGBoost
(Brier=0.0316)
Perfect
XGBoost
Reliability Diagrams (Calibration)
Figure 3: Reliability diagrams (five equal-frequency bins) for the three classifiers on the held-out test set
(NLP+Visual configuration). Proximity to the diagonal indicates well-calibrated predicted probabilities; the
corresponding Brier scores are reported in Table 3.
87% of maximum performance (ρ= 0.871) and closely comparable to the keyword-only baseline
(0.868) on a fundamentally different modality, confirming that image quality alone encodes
substantial risk signal and enabling lightweight image-only screening.Engineered NLP fea-
tures alone(61) reached 0.967 [CI: 0.931–0.992] with Logistic Regression, 97% of maximum
(ρ= 0.972), substantially outperforming visual-only models with fewer features, and contradict-
ing the initial hypothesis that visual features are primary discriminators.
BERT embeddings alone(768 dimensions) achieved 0.958 [CI: 0.916–0.987] with Random
Forest, underperforming the 61-feature engineered NLP set by∆AUC =−0.009despite consti-
tuting 83% of the all-features set by dimension, confirming that domain-specific feature engin-
eering captures the semantic signal at least as well as deep contextual embeddings.Combined
NLP+Visual(154 dimensions) achieved 0.992 [CI: 0.978–1.000] with XGBoost, within 0.3 per-
centage points of the comprehensive all-features model (0.994) while using 16.7% of its features,
and recalling all 33 deceptive advertisements (sensitivity 1.00) at PR-AUC 0.985: the inter-
pretable set attains performance statistically indistinguishable from the embeddings-augmented
model, at a fraction of the computational cost and without BERT’s opacity.
4.2.3. Decision-level evaluation: screening-queue simulation
ROC-AUC summarises ranking quality but not how screeningdecisionswould change in prac-
tice. We therefore simulate a screening queue on the held-out test set (n= 93; 33 deceptive), in
which an analyst with a limited review budget inspects advertisements in priority order, com-
paring three strategies: the multimodal model (XGBoost, NLP+Visual); a keyword rule rank-
ing advertisements by their count of risk-keyword and psychological-trigger flags (the simplest
theory-driven heuristic, using the same 23 features as Config. 0); and random ordering.
18

Table 4: Cross-configuration performance comparison: feature modality contributions
ConfigurationpBest Model ROC-AUC [95% CI] PR-AUC F1ρ
All Features 922 XGB0.994[0.983–1.000]0.9900.903 1.000
NLP+Visual (interpretable) 154 XGB 0.992 [0.978–1.000] 0.9850.9430.997
NLP Only 60 LR 0.967 [0.931–0.992] 0.952 0.857 0.972
Embeddings Only 768 RF 0.958 [0.916–0.987] 0.920 0.825 0.963
Keyword Baseline (Config. 0) 22 LR 0.867 [0.776–0.940] 0.806 0.739 0.872
Visual Only 94 XGB 0.866 [0.782–0.939] 0.790 0.710 0.871
Note:Configurations ranked by ROC-AUC.ρ= relative to the comprehensive all-features configur-
ation. Config. 0 uses Logistic Regression on 23 risk keyword features only. 95% CIs via bootstrap
(2,000 iterations). LR = Logistic Regression, RF = Random Forest, XGB = XGBoost.
Table 5 reports the outcome. At a review budget equal to test-set prevalence (33 advertise-
ments), the multimodal model surfaces 30 of 33 deceptive advertisements (91% recall at 91%
precision), against 16 (48%) for the keyword rule and about 12 (35%) for random ordering.
Fixing a target detection rate widens the gap in analyst effort: recovering 90% of deceptive
cases requires reviewing 32 advertisements with the model but 79 with the keyword rule, a
2.5-fold workload reduction for the same case-finding rate, and the model dominates at every
review depth. The performance gap in Section 4.2 therefore translates into materially differ-
ent operational decisions: at any fixed analyst capacity, the model identifies substantially more
exploitation-linked advertisements than the keyword screening characterising current practice.
Table 5: Screening-queue simulation on the held-out test set (n= 93; 33 deceptive). An analyst reviews
advertisements in priority order under each strategy.
Multimodal model Keyword rule Random
Deceptive caught in first 33 reviews 30 (91%) 16 (48%)≈12 (35%)
Reviews to catch 50% of cases 17 36 47
Reviews to catch 80% of cases 28 72 75
Reviews to catch 90% of cases 32 79 83
Reviews to catch 100% of cases 37 89 91
Note:Multimodal model=XGBoost (NLP+Visual). Keyword rule ranks advertisements by the
count of 23 risk-keyword and psychological-trigger flags. Random=expected value at the test-set
prevalence (35.3% deceptive).
4.3. Feature importance and discriminatory mechanisms
To identify which signals drive performance, we apply SHAP (SHapley Additive exPlanations)
analysis to the XGBoost model from the NLP+Visual configuration (ROC-AUC 0.992), which
achieves near-maximum performance whilst remaining fully interpretable. Table 6 gives the top
5 features by mean absolute SHAP value; the full top-15 ranking is in Supplementary Table S3.
19

Table 6: Top 5 features by SHAP importance in NLP+Visual configuration (XGBoost)
Rank Feature Description Category Mean SHAP
1coleman_liau_indexCLI readability score Text Quality 1.853
2risk_keyword_densityKeywords per word Composite Risk 1.227
3visa_sponsorship_mentionedVisa/sponsorship mentioned Risk Keywords 0.882
4red_meanMean red channel intensity Visual Low-Level 0.535
5unique_colorsColour diversity (pixel count) Visual Low-Level 0.474
Note:Features ranked by mean absolute SHAP values (scale reflects XGBoost raw outputs). All
features are directly interpretable. The top three features are textual; visual features first appear at
rank 4.
4.3.1. Category-level contributions
Table 7 aggregates SHAP contributions by feature category.Textual features dominate with
63.9% of explanatory power, led by Text Quality (22.3%), Basic Text (14.1%), Composite
Risk Indicators (12.4%), and Domain-Specific Risk Keywords (9.1%); visual features account for
the remaining 36.0% (Low-Level 18.9%, Mid-Level 12.1%, High-Level 5.0%). This reversal of
the expected visual dominance, with NLP-only models reaching 97% of maximum performance
against visual-only models’ 87.1%, establishes textual signal as the primary discriminator.
Within text, quality metrics (Coleman-Liau, grammar error rate, Flesch readability) out-
weigh domain-specific keywords (22.3% vs. 9.1%), confirming thathowadvertisements are
written discriminates better thanwhatterms they contain; composite risk indicators (12.4%)
form a secondary signal. Visual contribution comes through low-level texture and colour di-
versity (18.9%) rather than high-level object detection (5.0%), consistent with the univariate
finding that YOLO classes showed limited significance.
4.3.2. Discriminatory mechanisms and signalling interpretation
SHAP analysis reveals three mechanisms by which deceptive advertisements reveal themselves,
each interpretable through information economics.
Readability and vocabulary as primary competence signals.The Coleman-Liau In-
dex (mean SHAP 1.853) leads by a substantial margin, followed by composite risk keyword dens-
ity (1.227) and visa/sponsorship mention (0.882). Measuring word and sentence length rather
than syllabic complexity, Coleman-Liau captures vocabulary sophistication: legitimate advert-
isements use the longer, more complex words of professional register, deceptive ones shorter and
simpler vocabulary. This is an involuntary competence signal: exploiters cannot systematically
elevate vocabulary without native linguistic competence or professional copywriting. Unlike
strategic keyword choices, vocabulary level is an inherent sender attribute, costly to fake.
20

Table 7: Feature category contributions to model explanatory power (NLP+Visual configuration)
Category Contribution (%) Modality
Text Quality Features 22.3% NLP
Low-Level Visual Features 18.9% Visual
Basic Text Features 14.1% NLP
Composite Risk Indicators 12.4% NLP
Mid-Level Visual Features 12.1% Visual
Domain-Specific Risk Keywords 9.1% NLP
Emotion Features 5.3% NLP
High-Level Visual Features 5.0% Visual
Psychological Triggers 0.7% NLP
NLP Total 63.9%
Visual Total 36.0%
Note:Percentages represent relative contribution measured via mean absolute SHAP values (XG-
Boost, NLP+Visual configuration). NLP features dominate despite visual features appearing at ranks
4–5 in the individual feature ranking, because the NLP category contains more high-contributing fea-
tures overall.
Domain-specific keyword absence as the clearest indicator.Visa and work permit
terminology appears near-exclusively in deceptive advertisements (48.8% vs. 3.7%; 28.7% vs.
0.0%), the dataset’s strongest binary separation. These keywords carry genuine operational con-
tent: exploiters advertising migration-dependent routes must reference them, whilst legitimate
employers advertising domestic roles almost never do. The risk keyword density composite (rank
2, SHAP 1.227) aggregates these into a robust continuous signal.
Texture and colour diversity as visual quality proxies.Visual features first appear at
ranks 4–5 (red channel mean, SHAP 0.535; unique colours, 0.474), followed by texture metrics
at ranks 10, 13, and 15. Red channel intensity may reflect warning-palette templates, whilst
colour diversity captures palette richness, as professionally designed advertisements use varied,
carefully chosen schemes. Texture metrics (GLCM contrast, LBP mean, gradient variability)
encode sharpness and structural complexity, with legitimate advertisements showing sharper,
more detailed imagery consistent with professional photography. YOLO-detected object classes
contribute only 5.0% of total SHAP, confirming that image semantics discriminate far less than
image statistics.
Acrossallthreemechanisms, deceptivesignalsmanifestasqualitydeficiencies(simplervocab-
ulary, poorer image texture, absent legitimate-domain content) rather than deliberate deception
markers. Resource constraints prevent exploiters from sustaining professional quality across tex-
tual and visual dimensions at once, and detection remains effective as long as that coordination
problem stays intractable.
21

5. Discussion
5.1. Theoretical interpretation through signalling framework
The empirical results validate our central theoretical prediction: while deceptive recruiters can
mimic legitimate communications along individual signal dimensions at low cost, they cannot
maintain consistent professional quality across all channels simultaneously. Three mechanisms
reveal this coordination failure.
Textual quality as the primary involuntary signal.NLP dominance (63.9% SHAP;
NLP-only ROC-AUC 0.967) extends and revises prior qualitative research. Coleman-Liau, the
strongest discriminator (mean SHAP 1.853,d=−1.21), reflects legitimate recruiters writing
in higher-register language as a by-product of professional context; grammar error rate (d=
0.55) and readability indices distinguish classes similarly. Critically,spelling error rate does not
differ significantly(p= 0.107), contradicting the intuitive hypothesis that deceptive ads contain
obvious typos: discrimination lies in vocabulary level, harder to fake than a proofreading pass.
This accords with signalling theory [42], where vocabulary reflects an inherent sender attribute,
educational and professional background, requiring sustained investment to alter.
Domain-specific keywords (visa/sponsorship 48.8% vs. 3.7%; work permit 28.7% vs. 0.0%)
reflect genuine operational differences between migration-oriented exploitation and domestic le-
gitimaterecruitmentratherthandeliberatesignalling: exploitersadvertisingmigration-dependent
routesmustreference these terms or lose their audience.
Visual quality as secondary confirmatory signal.Visual features contribute 36.0% of
SHAP explanatory power. Image sharpness (Laplacian varianced=−0.51), texture contrast
(GLCMd=−0.42), and red-channel/colour-diversity statistics (SHAP 0.535 and 0.474) are the
operative metrics, not brightness or saturation as originally hypothesised. The signal reflects
production quality rather than content: lower-sharpness, less-textured images are consistent
with screenshots, compressed social-media graphics, or low-resolution sources. Object detection
(YOLO) contributes only 5.0%, with boats, backpacks, and stop signs showing no significant uni-
variate differences, artefacts of the prior non-empirical characterisation. Practically, sharpness
and texture statistics act as production-quality proxies that exploiters cannot trivially improve
without professional photography equipment and design software.
BERT embeddings and interpretability trade-offs.BERT embeddings alone achieve
ROC-AUC 0.958, somewhat below engineered NLP features alone (0.967), and adding them to
the NLP+Visual configuration recovers only a modest further gain (∆AUC = +0.002on the
22

all-features model, 0.994 vs. 0.992), indicating that domain-specific feature engineering captures
the great majority of the discriminatory semantic signal on its own. That the interpretable con-
figuration attains performance statistically indistinguishable from the embeddings-augmented
model, with full transparency, favours interpretable features for humanitarian deployment re-
quiring stakeholder accountability.
5.2. Methodological implications for OR under data scarcity
This research demonstrates how OR techniques address classification problems in data-scarce
domains where ground-truth labels are expensive or ethically constrained.
Labelqualityversusquantity.Ourdataset(n= 464)achievesstrongperformance(ROC-
AUC 0.87–0.99 held-out; 0.97–0.98 in repeated stratified CV) through label quality rather than
volume: eachpositivecaseisverifiedforcedlabourwithdocumentedvictimtestimonylinkingad-
vertisement to exploitation. This contrasts with [38] (17,880 postings, expert-judgement labels)
and [5] (social media posts without verified outcomes), suggesting a general principle: where
ground truth is scarce, careful case verification yields better models than expanding samples
with uncertain labels.
Multimodal feature engineering.NLP dominance (97% of maximum performance from
61 interpretable dimensions) was not predicted by prior qualitative research, which emphasised
visual red flags, demonstrating the value of systematic empirical analysis over expert intuition
once ground truth enables validation. Where data is scarce, comprehensive feature engineer-
ing across all signal dimensions, especially text quality, maximises information extraction and
corrects intuitive priors.
Interpretability in stakeholder contexts.XGBoost achieves the best hold-out perform-
ance across most configurations, whilst Logistic Regression offers superior calibration and full
coefficient interpretability. For humanitarian contexts requiring accountability, XGBoost com-
bines superior sensitivity (zero false negatives for the NLP+Visual configuration) with SHAP
TreeExplainer justifications per prediction, the combination motivating its selection for the DSS.
Repeated cross-validation (ROC-AUC≈0.98±0.01for XGBoost and RF) confirms this per-
formance is robust, not an artefact of one favourable split.
5.3. Proof-of-concept DSS
We operationalise the best-performing model (XGBoost, NLP+Visual; ROC-AUC 0.992, PR-
AUC 0.985) as a proof-of-concept DSS. The system takes a job advertisement (image file plus
extracted text), runs the multimodal feature extraction pipeline (Section 3), and returns risk
23

assessments with transparent explanations.1
System outputscomprise: (1) a continuous risk probabilityP(θ=L|x)∈[0,1]; (2) a
categorical classification (Low<0.3, Medium0.3–0.7, High>0.7) on customisable thresholds;
(3) an explanation report giving the top five SHAP contributors with directional effects (e.g.,
“Coleman-Liau score−3.2below legitimate average:+1.4risk contribution; visa/sponsorship
keyword detected:+0.9”); and (4) feature-level transparency showing which textual quality
metrics, risk keywords, or visual attributes triggered the assessment.
Stakeholder customisationaddresses divergent priorities: platforms prioritising precision
can set conservative thresholds (e.g., 0.75) to avoid restricting legitimate opportunities, whilst
labour inspectorates prioritising recall can set sensitive ones (e.g., 0.35), accepting more false
positives to maximise detection. The interpretability layer ensures every risk score carries a
human-readable justification, critical for accountability in humanitarian contexts.
This proof-of-concept shows that rigorous analytical frameworks can become accessible tools
for non-technical practitioners. Full deployment, however, requires addressing adversarial ad-
aptation, fairness validation, and feedback mechanisms for continuous refinement, examined
next.
5.4. Operational deployment and practical challenges
Adversarial adaptation.Deployment requires monitoring for performance degradation as
recruiters adapt. A model trained on 2022–2024 data may not generalise if exploiters learn which
features trigger classification, adopt AI-generated content that improves production quality, or
shift to unrepresented channels; feedback loops in which confirmed false positives and negatives
inform retraining are needed.
The multimodal architecture is inherently robust, but the primary signal’s nature matters for
adversarial resilience. Vocabulary sophistication (Coleman-Liau) is the dominant discriminator
and is hard to fake by simple post-hoc editing, though LLM paraphrasing could plausibly raise
apparent vocabulary level, a genuine threat warranting monitoring as generative AI reaches low-
1TheDeceptiveRecruitmentDetectionSystemcodeispubliclyavailableathttps://github.com/sajidsiraj/
labour_exploitation. GPU-based feature extraction (image captioning and semantic embedding) is not bit-
exact reproducible across hardware and runs; we therefore provide the resulting feature matrix as a fixed artefact
from which all reported tables are exactly reproducible. Across five independent full re-runs of the pipeline from
raw images (i.e. without the fixed matrix), held-out ROC-AUC for a given configuration varied run to run by at
most 0.016 (largest for the embeddings-only configuration; the NLP+Visual configuration varied by only 0.004),
reflecting non-deterministic floating-point reduction order in the GPU feature-extraction step rather than any
instability in the classifiers themselves; the figures reported here, computed from the fixed matrix, sit close to
but not always inside that empirical range, and are reported as the reproducible reference values rather than as
a single favourable run.
24

resourced actors. Domain-specific keywords (visa/sponsorship) are structurally embedded in
exploitation schemes and cannot be removed without undermining the advertisement’s purpose,
and visual quality is similarly constrained by production resources. Complete mimicry across
all modalities remains resource-intensive, but the vocabulary channel is most vulnerable to AI-
assisted improvement and should be the focus of ongoing monitoring.
Ethical considerations.Our findings sharpen the false-positive concern. Because vocab-
ulary sophistication and image production quality are the primary discriminators, the system
may systematically flag legitimate advertisements from low-resourced employers (small busi-
nesses, NGOs, employers in lower-income countries) whose advertisements genuinely show sim-
pler vocabulary and poorer imagery without deceptive intent. The same resource constraints
characterise both exploiters and some legitimate small employers. Platforms should therefore
use graduated responses (high-risk scores triggering enhanced verification rather than automatic
rejection) and segment thresholds by employer type or geography rather than uniform cut-offs.
Falsenegativescarrysevereharmsintheotherdirection, asworkersrespondingtoundetected
deceptive advertisements may enter forced labour; the system should be positioned as a screening
toolforelevatedrisk, notaguaranteeoflegitimacy. Fairnessanalysisexaminingdisparateimpact
across nationalities, employer sizes, sectors, or origin countries is critical and currently absent,
an essential prerequisite before large-scale deployment.
5.5. Limitations
Temporal, contextual and scope validity.Models trained on 2022–2024 data may not
generalise to future practices, other geographic contexts, or recruitment channels beyond job
advertisements. Deceptive strategies evolve as exploiters adapt, regulatory changes alter advert-
isement characteristics, and cultural or linguistic differences may create context-specific signals
not captured in our cross-national sample. Deception also occurs increasingly through informal
networks (social media, messaging apps, in-person referrals) that may present distinct signal
patterns, and our definition of “deceptive” covers advertisements linked to forced labour under
ILO indicators rather than broader recruitment fraud or employment scams. Temporal valid-
ation (2025+ cases) and geographic holdout validation would provide stronger generalisability
evidence but were not feasible given data constraints.
Sample size.The dataset of 464 advertisements with 164 verified forced labour cases is one
of the first ground-truth datasets in this domain, where ethical constraints and victim confiden-
tiality inherently limit sample expansion [31]. It supports reliable training and evaluation under
25

rigorous verification standards, but prevents granular analysis of country–sector interactions
(fewer than 10 cases per combination across 9 countries and 21 sectors).
Causality and spurious correlations.The analysis identifies strong correlations between
features and exploitation outcomes but does not claim causal mechanisms; observed patterns
may reflect resource constraints or design choices rather than deception per se. Similarly, YOLO
objectdetectionscontributedminimallytomodelperformance(5.0%SHAP),andspecificCOCO
classes like boats and backpacks showed no significant univariate differences, and their inclusion
in prior qualitative characterisations was not supported empirically. Qualitative error analysis
with domain experts would help distinguish genuine indicators from artefacts and strengthen
causal understanding.
Negative-class composition.The legitimate class was drawn from employers vetted by
the partner organisations for reputational standing and regulatory compliance, providing a well-
characterised contrast for identifying discriminative signals. We note that this construction may
flatter separability relative to deployment, where some legitimate advertisements from small or
low-resourced employers can share surface features (simpler vocabulary, lower-quality imagery)
with deceptive ones. Consistent with our proof-of-concept framing, we therefore identify evalu-
ation against harder, more representative negatives, with false-positive rates by employer type
and source, as a valuable direction for future work before operational deployment; the graduated-
response and segmented-threshold safeguards discussed above are intended to manage this risk
in practice.
6. Conclusion
This paper addresses detection of deceptive job advertisements leading to forced labour by com-
bining signalling theory with multimodal machine learning. Using 464 verified advertisements
(164 confirmed forced labour cases, 300 legitimate), we make three contributions to OR meth-
odology for humanitarian applications.
Methodologically, combining computer vision, natural language processing, and explainab-
ility achieves strong classification performance (ROC-AUC 0.992, PR-AUC 0.985 for the inter-
pretable NLP+Visual configuration; ROC-AUC≈0.98±0.01in repeated cross-validation) on a
relatively small verified dataset. 154 engineered interpretable features attain performance stat-
istically indistinguishable from the full 922-feature set including BERT embeddings (within 0.3
percentage points), establishing that domain-specific feature engineering can substitute for com-
putationally expensive deep representations at negligible cost. The systematic ablation approach
26

transfers to other classification problems in sensitive social domains where verified ground truth
is scarce.
Theoretically, signalling theory can inform feature engineering where low-quality agents
mimic high-quality communications.Textualfeatures dominate discrimination (63.9% SHAP),
led by vocabulary sophistication (Coleman-Liau,d=−1.21) rather than spelling errors, which
do not differ significantly between classes. This diverges from prior qualitative characterisations
emphasising visual red flags and typos, reframing the primary signal: deceptive recruiters reveal
themselves through systematically simpler vocabulary and domain-specific content (visa termin-
ology, work permit references). The framework should generalise to other contexts involving
strategic deception under information asymmetry.
Practically, we implement a proof-of-concept DSS providing real-time risk assessment with
interpretable explanations: continuous risk probabilities (P(θ=L|x)∈[0,1]), categorical clas-
sifications on customisable thresholds, and SHAP-based justifications identifying which features
(low Coleman-Liau score, visa keyword presence, image texture statistics) drove each assess-
ment. Adjustable thresholds let platforms minimise false positives whilst labour inspectorates
maximise exploitation detection.
We acknowledge several important limitations. The relatively small sample size (464 total,
164 positive cases) limits statistical power and prevents detailed analysis of how patterns vary
across countries and sectors. The results show correlations between features and exploitation
outcomes but do not establish causality; we cannot rule out that some legitimate low-resource
employers might also exhibit poor visual quality. Qualitative error analysis with domain experts
would be valuable before operational deployment. Finally, we have not examined whether the
classifier exhibits disparate impact across nationalities, genders, or job sectors, which is critical
for fairness.
Five research directions seem particularly promising. First, field experiments testing whether
riskwarningsactuallychangejobseekerbehaviourunderdifferenteconomiccircumstances. Second,
longitudinal studies tracking how deceptive patterns evolve as detection systems are deployed.
Third, testing whether the framework transfers to related problems like financial fraud or mis-
information detection. Fourth, systematic fairness analysis to ensure the system does not per-
petuate discrimination against marginalised groups. Fifth, more flexible detection of reciprocity-
based psychological signalling (e.g. embedding- or paraphrase-based matching rather than a fixed
keyword list): an exact-phrase operationalisation of this trigger found essentially no signal in
27

the present corpus and was dropped from the final feature set, but the underlying construct,
employers offering upfront inducements to create a sense of obligation, remains theoretically
motivated and may be detectable with a less brittle measure.
Operational research methods can thus contribute to humanitarian challenges characterised
by information asymmetry and data scarcity. Grounding the approach in signalling theory,
systematic feature ablation, and interpretability provides a methodological template for similar
problems, and the decision support system enables intervention at recruitment rather than after
exploitation. Whilst forced labour remains persistent in global supply chains, rigorous analytical
frameworks offer practical tools for protecting vulnerable workers.
References
[1] ILO, Global estimates of modern slavery: Forced labour and forced marriage, Tech. rep.,
International Labour Organization (ILO), Walk Free, and International Organization for
Migration (IOM) (2022).
[2] M. Hosseinzadeh, R. Alikhani, S. Gold, M. Samadi Foroushani, Assessing the systemic
effects of modern slavery mitigation strategies in supply chains, Annals of Operations Re-
search (2025) 1–38.
[3] G. LeBaron, The role of supply chains in the global business of forced labour, Journal of
Supply Chain Management 57 (2) (2021) 29–42.
[4] L. Marques, A. Erthal, A. Crane, Impact pathways:“follow the labour”. the labour supply
chain and its impact on decent work in product supply chains, International Journal of
Operations & Production Management 45 (7) (2025) 1395–1401.
[5] T. J. Moyo, O. Gunes, M. D. Jirotka, Investigating human trafficking recruitment online:
A study of fraudulent job offers on social media platforms, Proceedings of the ACM on
Human-Computer Interaction 9 (2) (2025) 1–31.
[6] A. V. Benstead, L. C. Hendry, M. Stevenson, Detecting and remediating modern slavery in
supply chains: a targeted audit approach, Production Planning & Control 32 (13) (2021)
1136–1157.
[7] X. Yin, İ. E. Büyüktahtakın, B. P. Patel, Covid-19: Data-driven optimal allocation of
ventilator supply under uncertainty and risk, European Journal of Operational Research
304 (1) (2023) 255–275.
[8] K.-Y. Lin, S.-Y. Wu, K. Matsuno, Generative ai-driven resilience in supply chain manage-
ment: Unisone framework for disruption modelling and capacity optimisation, International
Journal of Production Research (2025) 1–26.
[9] T. Perdikis, G. Celano, S. Chakraborti, Distribution-free control charts for monitoring scale
in finite horizon productions, European Journal of Operational Research 314 (3) (2024)
1040–1051.
28

[10] J. Song, J. Song, M. Vanhoucke, Automatic selection of the best performing control point
approach for project control with resource constraints, European Journal of Operational
Research 322 (1) (2025) 15–38.
[11] S. Höppner, B. Baesens, W. Verbeke, T. Verdonck, Instance-dependent cost-sensitive learn-
ing for detecting transfer fraud, European Journal of Operational Research 297 (1) (2022)
291–300.
[12] D. Ma, X. Wu, K. Li, J. Hu, Can blockchain implementation combat food fraud: Consid-
ering consumers’ delayed quality perceptions, European Journal of Operational Research
324 (3) (2025) 908–924.
[13] P. Ramchandani, H. Bastani, E. Wyatt, Unmasking human trafficking risk in commercial
sex supply chains with machine learning, Manufacturing & Service Operations Management
27 (3) (2025) 700–719.
[14] Meehan, Pinnington, Modern slavery in supply chains: insights through strategic ambiguity,
International Journal of Operations & Production Management 41 (2) (2021) 77–101.
[15] K. L. Christ, C. V. Helliar, Blockchain technology and modern slavery: Reducing deceptive
recruitment in migrant worker populations, Journal of Business Research 131 (2021) 112–
120.
[16] W. Yu, C. Y. Wong, M. Jacobs, R. Chavez, Modern slavery supply chain capabilities: the
effects of blockchain technology and employees’ digital dexterity, International Journal of
Operations & Production Management 45 (1) (2025) 210–235.
[17] A. Crane, Modern slavery as a management practice: Exploring the conditions and capab-
ilities for human exploitation, Academy of Management Review 38 (1) (2013) 49–69.
[18] S. Gold, A. Trautrims, Z. Trodd, Modern slavery challenges to supply chain management,
Supply Chain Management: An International Journal 20 (5) (2015) 485–494.
[19] R. Geng, H. K. Lam, M. Stevenson, Addressing modern slavery in supply chains: an
awareness-motivation-capability perspective, International Journal of Operations & Pro-
duction Management 42 (3) (2022) 331–356.
[20] F. Bodendorf, F. Wonn, K. Simon, J. Franke, Indicators and countermeasures of modern
slavery in global supply chains: Pathway to a social supply chain management framework,
Business Strategy and the Environment 32 (4) (2023) 2049–2077.
[21] V. A. Snyder, W. L. Tate, J.-P. Paraskevas, Labor flows in supply chains: A review of
the literature and future research opportunities, Journal of Business Logistics 47 (2) (2026)
e70056.
[22] V. Soundararajan, M. M. Wilhelm, A. Crane, Humanizing research on working conditions
in supply chains: Building a path to decent work, Journal of Supply Chain Management
57 (2) (2021) 3–13.
[23] A. Crane, G. LeBaron, K. Phung, L. Behbahani, J. Allain, Confronting the business models
of modern slavery, Journal of Management Inquiry 31 (3) (2022) 264–285.
29

[24] D. A. Shepherd, V. Parida, T. Williams, J. Wincent, Organizing the exploitation of vulner-
able people: A qualitative assessment of human trafficking, Journal of Management 48 (8)
(2022) 2421–2457.
[25] D. Simpson, M. Segrave, A. Quarshie, A. Kach, R. Handfield, G. Panas, H. Moore, The
role of psychological distance in organizational responses to modern slavery risk in supply
chains, Journal of Operations Management 67 (8) (2021) 989–1016.
[26] C. Emberson, S. M. Pinheiro, A. Trautrims, Adaptations to first-tier suppliers’ relational
anti-slaverycapabilities, SupplyChainManagement: AnInternationalJournal27(4)(2022)
575–593.
[27] B. B. Keskin, G. J. Bott, N. K. Freeman, Cracking sex trafficking: Data analysis, pattern
recognition, and path prediction, Production and Operations Management 30 (4) (2021)
1110–1135.
[28] M. Jiang, L. Chen, C. Blome, F. Jia, Digital technology adoption for modern slavery risk
mitigation in supply chains: An institutional perspective, Technological Forecasting and
Social Change 192 (2023) 122595.
[29] Institute for Human Rights and Business (IHRB), Leadership group for responsible
recruitment: Six steps to responsible recruitment, accessed October 10, 2025 (2019).
URLhttps://ihrb-org.files.svdcdn.com/staging/assets/uploads/
member-uploads/Six_Steps_to_Responsible_Recruitment_-_Implementing_the_
Employer_Pays_Principle.pdf?dm=1715761515
[30] M. Žilinskait˙ e, A. Hajro, P. Baldassari, C. Miska, Migration, human supply chains, and
the multinational enterprise: Confronting an overlooked global mobility challenge, Human
Resource Management Journal 35 (3) (2025) 742–753.
[31] R. A. Konrad, A. C. Trapp, T. M. Palmbach, J. S. Blom, Overcoming human trafficking
via operations research and analytics: Opportunities for methods, models, and applications,
European Journal of Operational Research 259 (2) (2017) 733–745.
[32] A.Volodko, E.Cockbain, B.Kleinberg, “spottingthesigns” oftraffickingrecruitmentonline:
exploring the characteristics of advertisements targeted at migrant job-seekers, Trends in
Organized Crime 23 (1) (2020) 7–35.
[33] A. V. Benstead, L. C. Hendry, M. Stevenson, Horizontal collaboration in response to mod-
ern slavery legislation: An action research project, International Journal of Operations &
Production Management 38 (12) (2018) 2286–2312.
[34] M. Stevenson, R. Cole, Modern slavery in supply chains: a secondary data analysis of de-
tection, remediation and disclosure, Supply Chain Management: An International Journal
23 (2) (2018) 81–99.
[35] P. Malakar, S. A. Khan, A. Gunasekaran, M. S. Mubarik, Digital technologies for social
supply chain sustainability: An empirical analysis through the lens of dynamic capabilities
and complexity theory, IEEE Transactions on Engineering Management 72 (2025) 664–675.
[36] D. Fletcher, A. Trautrims, Recruitment deception and the organization of labor for ex-
ploitation: A policy–theory synthesis, Academy of Management Perspectives 38 (1) (2024)
43–76.
30

[37] R. Li, M. Tobey, M. E. Mayorga, S. Caltagirone, O. Y. Özaltın, Detecting human trafficking:
Automated classification of online customer reviews of massage businesses, Manufacturing
& Service Operations Management 25 (3) (2023) 1051–1065.
[38] S. Vidros, C. Kolias, G. Kambourakis, L. Akoglu, Automatic detection of online recruitment
frauds: Characteristics, methods, and a public dataset, Future Internet 9 (1) (2017) 6.
[39] G. Cascavilla, G. Catolino, F. Palomba, A. S. Andreou, D. A. Tamburri, W.-J. Van Den
Heuvel, Unsupervised labor intelligence systems: A detection approach and its evaluation,
in: Service-Oriented Computing – SummerSOC 2022, Vol. 1603 of Communications in
Computer and Information Science, Springer, 2022.doi:10.1007/978-3-031-18304-1_5.
[40] UNODC, Human trafficking indicators, [Accessed 5 July 2025] (2018).
URLhttps://www.unodc.org/pdf/HT_indicators_E_LOWRES.pdf
[41] X. Guo, J. Jin, L. Wang, X. Yan, Enhancing decision support for bystander interventions:
The role of victim emotional disclosure and collective signals in social media incivility,
Decision Support Systems (2025) 114556.
[42] M. Spence, Job market signaling, The Quarterly Journal of Economics 87 (3) (1973) 355–
374.
[43] D. D. Bergh, B. L. Connelly, D. J. Ketchen Jr, L. M. Shannon, Signalling theory and equi-
librium in strategic management research: An assessment and a research agenda, Journal
of Management Studies 51 (8) (2014) 1334–1360.
[44] M. Spence, Signaling in retrospect and the informational structure of markets, American
Economic Review 92 (3) (2002) 434–459.
[45] B. L. Connelly, S. T. Certo, R. D. Ireland, C. R. Reutzel, Signaling theory: A review and
assessment, Journal of Management 37 (1) (2011) 39–67.
[46] Y. Wang, M. Zhang, S. Li, F. McLeay, S. Gupta, Corporate responses to the coronavirus
crisis and their impact on electronic-word-of-mouth and trust recovery: Evidence from
social media, British Journal of Management 32 (4) (2021) 1184–1202.
[47] N. Kumar, L. Qiu, S. Kumar, A hashtag is worth a thousand words: An empirical invest-
igation of social media strategies in trademarking hashtags, Information Systems Research
33 (4) (2022) 1403–1427.
[48] A. Krausert, Hrm signals for the capital market, Human Resource Management 55 (6)
(2016) 1025–1040.
[49] N. Steigenberger, Deceptive signalling: Causes, consequences and remedies, International
Journal of Management Reviews 27 (2) (2025) 283–305.
[50] M. Musteen, D. K. Datta, B. Kemmerer, Corporate reputation: do board characteristics
matter?, British Journal of Management 21 (2) (2010) 498–510.
[51] R. Nayak, U. C. Pati, S. K. Das, A comprehensive review on deep learning-based methods
for video anomaly detection, Image and Vision Computing 106 (2021) 104078.
31

[52] S. M. Lundberg, G. Erion, H. Chen, A. DeGrave, J. M. Prutkin, B. Nair, R. Katz, J. Him-
melfarb, N. Bansal, S.-I. Lee, From local explanations to global understanding with ex-
plainable ai for trees, Nature machine intelligence 2 (1) (2020) 56–67.
[53] S. M. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, Advances
in Neural Information Processing Systems 30 (2017).
32
