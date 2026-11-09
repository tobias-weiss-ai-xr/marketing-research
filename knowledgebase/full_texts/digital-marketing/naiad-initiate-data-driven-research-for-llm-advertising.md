---
title: 'NaiAD: Initiate Data-Driven Research for LLM Advertising'
url: https://arxiv.org/abs/2605.09918
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Yihang Zhang
- Zimeng Huang
- Ren Zhai
- Yipeng Kang
- Tonghan Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.09918
pages: 37
chars: 120439
fetched_at: '2026-11-08T13:00:47+00:00'
kb_version: 1
---

# NaiAD: Initiate Data-Driven Research for LLM Advertising

NaiAD: Initiate Data-Driven Research
for LLM Advertising
Yihang Zhang ∗
Tsinghua University
Beijing, China
hemmaxacand@gmail.com
Zimeng Huang
College of AI
Tsinghua University
Beijing, China
simona22336098@gmail.com
Ren Zhai
Department of Literature,
Arts and Communication
Anhui International Studies University
Anhui, China
zren@stu.aisu.edu.cn
Yipeng Kang †
State Key Laboratory of General
Artificial Intelligence, BIGAI
Beijing, China
kangyipeng@bigai.ai
Tonghan Wang †
College of AI
Tsinghua University
Beijing, China
twang1@g.harvard.edu
Abstract
Reconciling platform revenue with user experience in LLM advertising motivates
a data-centric foundation. We introduceNaiAD, the first comprehensive dataset
for LLM-native advertising comprising 58,999 carefully constructed ad-embedded
responses paired with user queries. NaiAD is organized around theoretically
grounded evaluation metrics that separately and comprehensively capture user and
commercial utility. To mitigate the dimensional collinearity of aligned LLMs, we
propose a decoupled generation pipeline that produces structurally diverse samples,
ranging from responses that explicitly disentangle stakeholder utilities to responses
that are uniformly strong or weak across dimensions. We further provide score
labels calibrated by a Variance-Calibrated Prediction-Powered Inference (VC-PPI)
framework, aligning automated scoring with human annotations. Mechanistic
analyses reveal that successful ad integration relies on reasoning paths that cluster
into four distinct semantic strategies. Models leveraging NaiAD internalize these
strategies to simultaneously improve user and commercial utility, while enabling
independent control over these distinct objectives via in-context learning. Together,
these results position NaiAD as a foundational infrastructure for developing future
LLM-native ad systems.
NaiAD collection:https://huggingface.co/datasets/MaxAcand/NaiAD
1 Introduction
Recently, the integration of advertising into Large Language Model (LLM) responses by prominent
AI organizations has marked a pivotal shift in the generative AI ecosystem [25]. While approached
∗This work was done by the author during his internship at Tsinghua University.
†Correspondence to: Tonghan Wang <twang1@g.harvard.edu>, Yipeng Kang <kangyipeng@bigai.ai>.
Preprint.
arXiv:2605.09918v1  [cs.LG]  11 May 2026

Native Ad-Embedded Generation Task
User: Query Advertiser: Ad Metadata
LLM: Response Integrating Ad
Evaluation Dimensions
For User Utility For Commercial Utility
Q1 (Response Relevance)
Does the response accurately
satisfy the user's intent?
Q2 (Expression Coherence)
Is the text coherent, logical,
and clear?
Q3 (Ad Effectiveness)
Is the brand/product clearly
and naturally perceived?
Q4 (Click-Through Intent)
How likely is a user to engage
with or click the ad?
Diverse Samples across Decoupled Axes NaiAD Enables Joint Utility Optimization
Multi-dimensional, unbiased assessment
SFT Achieves Joint Gains in User and Commercial Utility
User
Utility
Commercial
Utility
Hard
Negative
Samples
Hard
Negative
Samples
Simple
Negative
Samples
Ideal
Positive
Samples
5 - Excellent
3 - Baseline
1 - Poor
Structural diversity and hard negatives Emergent Ad-Insertion Strategies
Value & Vision Alignment
Emotional & Psychological Bridging
Methodological Abstraction
Aesthetic & Lifestyle Resonance
Decoupled Score Distribution
14761
14605
14467
14543
Total
58,376
Figure 1:An overview of our NaiAD dataset. (Left)We define the task and the four decoupled
evaluation dimensions.(Middle)We illustrate our data-centric methodology, emphasizing the
generation of structurally diverse samples including “hard negatives” to break dimensional collinearity.
The resulting decoupled score distributions confirm the successful creation of a dimensionally-
orthogonal dataset.(Right)We present our main findings: (Top) The discovery that LLM ad-insertion
behavior converges into four emergent strategies. (Bottom) Empirical validation showing that
Supervised Fine-Tuning (SFT) on NaiAD enables a base model to achieve significant joint gains
across all utility dimensions, proving the dataset’s effectiveness.
with careful design and sophisticated fallback mechanisms, this initiative has encountered measurable
user hesitation [35, 24]. This friction underscores a fundamental tension: balancing the imperative to
monetize capital-intensive models with the user’s desire for uninterrupted conversational experiences.
Advertising is not inherently incompatible with LLM-based interaction. Generative models can enable
advertising that is clearly labeled, context-aware, helpful, and unobtrusive. Yet, current scalable
systems frequently treat ads as external inserts, mechanically appending banners or sponsored links
to generated responses [39, 17, 25, 6]. This semantic disconnect disrupts conversational coherence,
harms user experience, and ultimately reduces advertising effectiveness.
This inefficiency reflects a gap in the existing research. Prior work largely focuses on the economic and
algorithmic aspects of LLM advertising, such as adapting search auction mechanisms to generative
settings [36, 43, 33] and optimizing bidding and pricing [12, 8, 11, 6]. Consequently, the generative
quality of the sponsored content itself remains underexplored. However, user satisfaction and
monetization are not mutually exclusive [ 42]. High-quality native sponsorships can align both
objectives, akin to how skilled human creators seamlessly integrate ads into their content.
These observations point to a central bottleneck in generative advertising: the absence of a data-centric
foundation for studying, evaluating, and training high-quality conversational ads. Effective LLM
advertising requires models to learn how different integration strategies affect user utility, perceived
naturalness, and platform revenue. Such learning necessitates a dataset satisfying two key desiderata.
(1)Multi-dimensional, unbiased assessment.Sponsored responses should be evaluated across
decoupled axes reflecting multiple stakeholders:User Utility, measuring whether the user’s query is
answered naturally and coherently; andCommercial Utilityfor advertisers and platforms, assessing
if brand information is effectively integrated and likely to drive user engagement. (2)Structural
diversity and hard negatives.The dataset should contain diverse and disentangled samples. For
instance, high user utility does not automatically imply high commercial value. The dataset should
therefore include controlled “hard negatives” spanning different combinations of user and commercial
quality, preventing both generators and evaluators from exploiting spurious correlations.
We introduceNaiAD(Native Ad Integration and Assessment Dataset), the first comprehensive dataset
for LLM-based native advertising. NaiAD is designed around the two desiderata and comprises
58,999 carefully constructed ad-embedded responses: 58,376 LLM-generated responses and 623
YouTube-sourced human responses. Grounded in Jakobson’s semiotic communication theory [19]
and Austin and Searle’s speech act theory [4, 32], we evaluate these responses across four decoupled
metrics:Response RelevanceandExpression Coherence(measuring User Utility), alongsideAd Ef-
fectivenessandClick-Through Intent(measuring Commercial Utility). However, dataset construction
in this setting is challenging because of dimensional collinearity: aligned LLMs tend to produce
2

Strategy Discovery for User-Commerce Harmonization Unbiased Assessment
Diverse & Decoupled Controlled Generation
Query-Ad Matching
Semantic Relevance
 LLM
Elicit Logical Bridge
via Chain-of-Thought
Clustering
Analysis
LLM-Generated Data Real-World Human Data
Raw Uncalibrated Dataset (~59k)
<Query, Ad Metadata, Response Integrating Ad>
Ad Response
Inverse Query Synthesis
Query
Human Anchor Set
(DH)
Unannotation Set
(Du)
Ground Truth Label LLM Scoring
Dimension-Adaptive PPI Calibration
(Aligning LLM Scores with Human Judgment)
User Utility
Metrics
Commercial Utility
Metrics
NaiAd Dataset
(Human Aligned)
Variance Calibration
(Restoring Score Diversity)
4 Ad-Insertion Strategies
I III
II
Rejection Sampling
Match Target Scores?
Decoupled Score
Requirements
Target Scores
on Q1~Q4
LLM
Response Integrating Ad
Including Hard Negatives
No: Reject       Yes: Accept
YouTube Transcripts
≈1%
Regression-Based
 Decision Tree
Figure 2:The construction and calibration pipeline of NaiAD. Phase I:Eliciting and clustering
LLM reasoning paths to discover four core ad-insertion strategies.Phase II:A decoupled generation
phase creating structurally diverse raw data via target-constrained rejection sampling for LLMs,
running parallel to inverse query synthesis for human transcripts.Phase III:A Dimension-Adaptive
Prediction-Powered Inference (PPI) and variance calibration framework that aligns raw LLM evalua-
tions with human judgments to produce the final unbiased dataset.
outputs that are uniformly strong or weak across evaluation metrics. To mitigate this, we design a
multi-dimensional decoupled generation pipeline to produce systematically diverse “hard negatives”.
Furthermore, to evaluate at scale without prohibitive annotation costs or evaluator bias, we introduce a
Variance-Calibrated Prediction-Powered Inference (VC-PPI) framework, utilizing a human-annotated
subset to statistically align LLM-based evaluations with human judgment.
Using NaiAD, we can reconcile user and commercial utility. Pareto optimality analysis reveals that
samples produced by the multi-dimensional decoupled generation pipeline consistently outperform
YouTube-sourced human samples in balancing these objectives. Moreover, Supervised Fine-Tuning
(SFT) on high-quality NaiAD subsets enables base models to simultaneously improve user utility and
Click-Through Rate (CTR). Furthermore, In-Context Learning (ICL) experiments demonstrate that
the dataset’s structural diversity empowers LLMs with decoupled controllable generation, enabling
them to independently adjust user and commercial utility to meet specific multi-dimensional target
profiles. Mechanistically, we uncover that successful native ad integration relies on constructing
a “Logical Bridge”: an internal reasoning path linking the user’s query to the advertisers’ core
value. Analyzing thousands of such bridges reveals an emergent low-dimensional structure where ad
integration strategies converge into four semantic clusters.
Figure 1 summarizes our dataset and key findings. In summary, our main contributions are three-fold:
• We releaseNaiAD, the first dimensionally-orthogonal dataset for LLM ad-embedded generation,
constructed via a decoupled generation pipeline and evaluated using our VC-PPI calibration
framework to eliminate dimensional collinearity and evaluator bias.
• Our empirical analysis reveals four successful generative strategies behind native LLM advertising:
embeddings of the “Logical Bridges” used to harmonize user and commercial utility converge into
four distinct clusters in a low-dimensional semantic space.
• We demonstrate through Pareto optimality analysis, SFT, and In-Context Learning that user and
commercial utility can be both jointly optimized and independently controlled, establishing a robust
foundation for future generative advertising systems.
2 Empirical Insight: The Logical Bridge and Strategy Convergence
To construct the NaiAD dataset proposed in Section 1, our primary objective is to generate responses
that effectively balance user utility and commercial utility. However, a major challenge immediately
arises: mechanically forcing an ad into a conversation inevitably causes user frustration. Before
3

generating the dataset at scale, we must first decipher the fundamental generative mechanism ofhow
to produce high-quality, harmonized samples.
We hypothesize that successfully breaking the trade-off between user and commercial utility requires
the model to construct a“Logical Bridge”—a latent reasoning path identifying a natural semantic
intersection between the user’s query and the advertiser’s value proposition. To harness this, we
prompt the LLM on a small batch of data to explicitly articulate these reasoning paths and perform
structural analysis to uncover the emergent, heuristic strategies behind native ad integration. In this
section, we deconstruct how LLMs cognitively perform this harmonization, using these discovered
strategies to guide the generation process of our subsequent dataset.
2.1 Query-Ad Matching and Logical Bridge Construction
To investigate how models construct these bridges, we first establish a foundation of se-
mantic relevance by pairing 1,986 real-world queries from INFINITY-CHAT [ 20] with
the most relevant advertisements from the A VTI 3 pool. Pairs are determined using
paraphrase-multilingual-MiniLM-L12-v2 embeddings [29] and cosine similarity (see Ap-
pendix B for details).
Once we have these contextually grounded pairs, we seek to understandhowthe LLM seamlessly
connects them. Using a highly capable generative model (detailed in Appendix C), we prompt it to
explicitly articulate the Logical Bridge. By forcing the model to plan the transition from user intent
to brand value, we transform a hidden process into observable text, ensuring the ad integration is
strategically grounded and transparent.
2.2 Discovering the Four Core Ad-Insertion Strategies
To determine if LLM ad-embedding follows predictable patterns, we convert the generated textual
bridges into Sentence-BERT embeddings. Because distance-based clustering algorithms often
struggle with high-dimensional text embeddings, we use Principal Component Analysis (PCA) to
progressively reduce the vectors into a condensed 30-dimensional space, removing noise while
preserving semantic groupings. Subsequent K-Means clustering in this space reveals an optimal
structure at K= 4 . As detailed in Appendix D, this determination is substantiated by a clear elbow in
the Sum of Squared Errors (SSE) curve and, more definitively, by a global peak in the Silhouette Score,
which provides a rigorous metric for cluster separation and cohesion. This convergence suggests that
LLM ad-insertion behavior converges into four distinct cognitive strategies.Projecting these
embeddings into a 2D space via UMAP (Figure 3) allows us to categorize these strategies.
Figure 3:Latent space visualization of Logical Bridges via UMAP.The 30D space reveals non-
overlapping regions corresponding to the four elicited strategies, illustrating how the LLM shifts
its reasoning to natively integrate ads. Because constructing a Logical Bridge inherently requires
complex conceptual association, we adopt the structured framework of Association Reasoning Paths
[18] to represent these transitions as directed multi-hop sequences.
3https://github.com/Agentyzu/MAE-AM
4

• Strategy 1: Value & Vision Alignment (The “Mindset” Bridge).The LLM elevates the query to
a macroscopic philosophy, connecting it to an advertiser that shares identical systemic values.
• Strategy 2: Aesthetic & Lifestyle Resonance (The “Vibe” Bridge).The LLM bypasses literal
topics to match the stylistic or aesthetic constraints of the query with a brand sharing an identical
lifestyle identity.
• Strategy 3: Emotional & Psychological Bridging (The “Empathy” Bridge).The LLM identifies
the underlying emotional driver and positions the product as a tangible means of emotional relief
or enhancement.
• Strategy 4: Methodological Abstraction (The “Craftsmanship” Bridge).Through cross-domain
feature migration, the model isolates the operational rigor required by the user’s task and links it to
a product characterized by similar precision or craftsmanship.
We providd case studies on these strategies in Appendix L. Our empirical analysis demonstrates that
when projected into a low-dimensional space, embeddings of “Logical Bridges” naturally organize
into four distinct clusters, remarkably revealing four successful generative strategies underpinning
native LLM advertising.
3 The NaiAD Dataset: Multi-Dimensional Decoupled Generation
Having demystified the underlying generation strategies, we proceed to the core construction of the
NaiAD dataset. The end-to-end pipeline for discovering integration strategies, generating diverse
samples, and conducting unbiased assessment is illustrated in Figure 2.
Task Formalization.We define theNative Ad-Embedded Generationtask as follows: given a user
query Q and advertisement metadata A, a model must generate a response R that fulfills Q while
seamlessly integratingAwithout breaking conversational coherence.
Constructing a comprehensive dataset for this task requires ensuring bothhigh-quality semantic
integrationandstructural diversity. Relying on unguided generation often yields generic, low-
quality insertions. Furthermore, aligned models suffer fromDimensional Collinearity (The Halo
Effect)[ 20], producing outputs that are uniformly high or low across all metrics, thereby lacking the
“hard negatives” needed to train discriminative boundaries. To address these challenges, we utilize
the same data sources in Section 2 (details in Appendix B) and design a multi-dimensional decoupled
generation pipeline (see Appendix C for implementation details).
3.1 Strategy-Guided Generation for High-Quality Data
Directly prompting an LLM to insert an ad frequently results in abrupt, unnatural transitions. To
promote the generation of high-quality samples and ensure structural diversity, we incorporate the
four core strategies discovered in Section 2 directly into the generation prompts.
During generation, the model is conditioned on a randomly assigned strategy and instructed to output
both the Logical Bridge and the final response within the same conversational turn. In this setup,
the explicitly generated Logical Bridge functions as a specialized Chain-of-Thought (CoT) [37]. It
guarantees that the semantic connection between user utility and commercial utility is meticulously
planned and executed, significantly improving the coherence of the final response while enhancing
the transparency and explainability of the data generation process.
3.2 Synthesizing Hard Negatives via Decoupled Score Requirements
While the strategy-guided CoT ensures the generation of high-quality, synergistic samples, training
robust evaluators also strictly requires breaking Dimensional Collinearity. To achieve this structural
diversity, we enforce decoupled score requirements across four dimensions (scale[1,5] ). (Theoretical
foundations and human-annotation rubrics are provided in Appendix E.) We mandate a minimum
score spread (e.g., max−min≥2 ) for objective dimensions like Relevance and Coherence, while
modeling Click-Through Intent as a bounded function of these scores (Appendix F). Combining these
discordant constraints with our guided strategies yields a balanced dataset containing fine-grained
quality variations.
3.3 Overcoming LLM Quality Bias via Rejection Sampling
Aligned LLMs are naturally optimized to produce flawless, coherent text and often resist fulfilling
the feature-discordant score requirements defined above. To overcome this inherent quality bias
5

and enforce our targeted structural diversity, we employTolerance-based Rejection Sampling
on top of our strategy-guided generation. Generated samples are accepted if and only if their self-
evaluated scores meet our target decoupled constraints (see Appendix F). This adversarial filtering
loop systematically discards “smoothed” outputs in favor of the essential hard negatives required for
robust evaluation.
3.4 Incorporating Real-World Human References
While our pipeline successfully generates structurally diverse synthetic data, evaluating true commer-
cial utility requires an authentic real-world anchor. To capture real commercial rhetoric and the natural
(often imperfect) distribution of human ad embedding, we incorporate real-world sponsorship data
fromXenova/sponsorblock [38]. As these transcribed sponsorships lack explicit user queries (Q),
they cannot be directly evaluated for “Response Relevance.” Thus, we introduce anInverse Query
Synthesismechanism using a state-of-the-art LLM to reconstruct standardized pseudo-queries. This
ensures consistent format between YouTube-sourced human data and our synthetic corpus, fulfilling
the dataset’s task requirements.
4 Human Assessment via Statistical Score Calibration
With the structurally diverse, ad-embedded responses successfully generated, the NaiAD dataset
remains incomplete without fine-grained, unbiased quality annotations across our decoupled dimen-
sions. However, evaluating a dataset of this scale ( N≈59k ) presents a fundamental dilemma.
Relying exclusively on human annotation is prohibitively expensive, whereas employing an un-
calibrated “LLM-as-a-Judge” introduces severe systemic biases such as verbosity bias, strictness
against commercial intent, and variance collapse [44]. If left uncalibrated, these LLM biases would
undermine the carefully engineered “hard negatives” in our dataset.
To achieve scalable yet unbiased assessment, we design a hybrid framework based on Prediction-
Powered Inference (PPI) [1], using a human-annotated anchor setD H (n= 684) to calibrate scores
for the unannotated set DU (detailed in Appendix H). We first utilize a capable evaluator LLM
(detailed in Appendix C) augmented with Chain-of-Thought (CoT) [ 37] to generate preliminary,
uncalibrated scores for DU . We then calibrate these raw LLM scores by estimating and neutralizing
their generative biases exclusively through the ground-truth human labels inD H.
4.1 Dimension-Adaptive Score Calibration
Standard PPI calibration typically applies a uniform linear shift to correct bias. However, our
analysis reveals that the nature of LLM scoring errors differs systematically between User Utility and
Commercial Utility dimensions. To address this, we introduce aDimension-Adaptive Calibration
Mechanismthat applies the optimal correction strategy for each category (details are provided in
Appendices I and J):
1. Regression-Based Calibration for User Utility Dimensions.Dimensions related to User Utility,
such asResponse RelevanceandExpression Coherence, assess the foundational informational quality
of the generated text. Both human and LLM judgments on these aspects tend to be continuous;
improvements in quality often correspond to incremental, relatively smooth increases in perceived
value. Given this scalar nature, we use polynomial regression (Ordinary Least Squares, OLS) to
model and correct the LLM’s scoring error. This model learns a continuous mapping by minimizing
the error against human annotations on the anchor set DH, taking into account the LLM’s raw score
and its self-evaluation confidence gap.
2. Decision Tree Calibration for Commercial Utility Dimensions.Dimensions of Commercial
Utility, such asAd EffectivenessandClick-Through Intent, measure the response’s persuasive impact
and its ability to influence user action. This assessment hinges on a user’s decision-making process,
which is inherently non-linear and often exhibits threshold-like behaviors (e.g., a user is either
persuaded to click or not). To capture these discrete decision boundaries, we employ Decision
Tree models [13]. These models excel at segmenting the data into different behavioral strata and
calculating distinct bias correction terms, a task for which continuous regression models are ill-suited.
4.2 Restoring Score Diversity via Variance Calibration
While our Dimension-Adaptive Routing isolates the optimal unbiased estimator, conventional
prediction-powered rectifiers inherently optimize Mean Squared Error (MSE), leading tovariance
compression—systematically squashing extreme scores toward the median.
6

1 2 3 4 5
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4Density
(a) Annotated Data
Q1
LLM
Human
PPI
1 2 3 4 5
Score
0.0
0.5
1.0
1.5
2.0Density
(b) Full Data
Q1
LLM (Raw)
PPI (Calibrated)
1 2 3 4 5
0.0
0.2
0.4
0.6
0.8
1.0
Q2
1 2 3 4 5
Score
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Q2
1 2 3 4 5
0.0
0.1
0.2
0.3
0.4
0.5
Q3
1 2 3 4 5
Score
0.0
0.2
0.4
0.6
0.8
1.0
Q3
1 2 3 4 5
0.0
0.1
0.2
0.3
0.4
0.5
Q4
1 2 3 4 5
Score
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Q4
Q1 Q2 Q3 Q4 Len
Q1
Q2
Q3
Q4
Len
0.51
0.27 0.36
0.39 0.55 0.41
0.30 0.34 0.19 0.22
(c) LLM Correlation
0.0
0.2
0.4
0.6
0.8
1.0
Q1 Q2 Q3 Q4 Len
Q1
Q2
Q3
Q4
Len
0.50
0.14 0.18
0.00 0.06 0.09
0.20 0.24 0.07 0.08
(d) PPI Correlation
0.0
0.2
0.4
0.6
0.8
1.0
Figure 4:Impact of PPI Calibration on Scoring Distributions and Dimensional Collinearity. (a
& b)Kernel density distributions reveal that raw LLM scores (red) misrepresent true quality. For user
utility metrics (Q1, Q2), the LLM artificially spreads scores, whereas PPI (green) recovers the true
human consensus (blue) that modern models maintain high baseline coherence.(c & d)Heatmaps
demonstrate the elimination of spurious correlations.
To restore the natural distributional span and maintain the score diversity, we proposeVariance-
Calibrated PPI (VC-PPI). By mathematically matching the first and second moments of the rectified
distribution to those of the human anchor setD H, we forcefully restore the distributional span via a
bounded affine transformation:
ˆYV C=Clip [1,5]

µH + (ˆYroute −µ route) σH σroute

(1)
where µH and σH are the true mean and standard deviation of human scores within DH, and µroute,
σroute are those of the routed predictions ˆYroute onD U .
VC-PPI effectively restores the suppressed standard deviation. Empirically, Quadratic OLS minimizes
W to 0.1374 for Response Relevance, while Stratified DT minimizesW to 0.2912 for Click-Through
Intent. This pipeline ensures the remaining 99% of NaiAD is rigorously human-aligned.
5 Experimental Evaluation and Analysis
The fundamental goal of our research is to break the trade-off between user and commercial utility in
LLM-native advertising. To systematically demonstrate how our methodology and the NaiAD dataset
achieve this, we formulate our experimental validation around four focal questions: (1) Can we strictly
decouple and unbiasedly assess these conflicting objectives? (Section 5.1) (2) Does our controlled
generation outperform human baselines, and what cognitive mechanisms drive this success? (Section
5.2) (3) Can fine-tuning on NaiAD teach models to permanently overcome the trade-off? (Section 5.3)
(4) Does the inclusion of fine-grained hard negatives in NaiAD enable dynamic, multi-dimensional
controllable generation? (Section 5.4)
5.1 Validating Decoupled Assessment via PPI Calibration
Uncalibrated LLM judges are notoriously susceptible to Dimensional Collinearity (the Halo Effect),
where strength in one dimension spuriously inflates perceived quality in others. Our PPI framework
is designed to mitigate this bias, disentangling conflicting dimensions and aligning evaluations with
authentic human judgment.
Distributional Alignment and Behavioral Stratification.As Figure 4(a, b) illustrates, uncalibrated
LLM evaluations (red curves) misrepresent true human distributions (blue curves). For objective
dimensions (Q1, Q2), raw LLMs are overly critical and hallucinate flaws, artificially spreading the
scores. Our PPI calibration rectifies this by mapping back to the highly skewed human ground truth.
This high-score concentration accurately reflects modern generative models: even when forced to
generate structural “hard negatives,” they rarely produce fundamentally incoherent or irrelevant text.
More discussions on the score distribution characteristics is provided in Appendix K.1.
7

Breaking Dimensional Collinearity.Figure 4(c, d) demonstrates successful dimension decoupling.
The uncalibrated LLM judge suffers from severe internal coupling, forging a spurious correlation
between User (Q1) and Commercial Utility (Q4) (ρQ1,Q4 = 0.39), alongside a noticeable verbosity
bias. Following PPI calibration, these cross-domain correlations are dismantled ( Q1-Q4 drops to
0.00), and length bias is suppressed. Crucially, PPI preserves the valid inherent correlation between
Relevance and Coherence ( Q1-Q2, ρ= 0.50 ). This confirms our framework evaluates user and
commercial utility as independent axes without destroying fundamental dataset statistics.
5.2 Pareto Optimality and Cognitive Mechanisms of Logic Bridges
Having established a reliable scoring mechanism, we investigate the absolute quality of the generated
samples and decipher the linguistic characteristics that distinguish successful soft ads from failures.
(a) MAX Pareto
 (b) MIN Pareto
Figure 5:TF-IDF Word Cloud of Logical Bridges.Max
Pareto optimal bridges (Left) utilize abstract structural vo-
cabulary, whereas Min Pareto failures (Right) regress into
disjointed, literal nouns.
Surpassing Human Anchors via
Pareto Frontiers.We conduct a
Pareto optimality analysis across the
four cognitive strategies, compar-
ing LLM-generated samples against
YouTube-sourced human data. As de-
tailed in the statistical comparisons
provided in Appendix K.3, while hu-
man creators slightly edge out the
LLM in foundational textual coher-
ence ( Q1, Q2), the LLM drastically
outperforms humans in Commercial
Utility. Specifically, the generated
samples achieve significantly higher
means in Ad Effectiveness (Q3) and
Click-Through Intent (Q4). By calculating the global Pareto frontier merging both datasets, we find
that LLM data dominates the superiority ratio, exceeding the human mean in 78.6% of cases for
Click-Through Intent. This statistically confirms that our controlled pipeline is not merely mimicking
human behavior but optimizing beyond it.
Vocabulary Deconstruction of Success.To understandhowmodels achieve this optimality, we
extract TF-IDF keywords from the explicit “Logical Bridges” of the Max and Min Pareto samples
(Figure 5). A clear insight emerges:successful bridges rely on structural abstraction, whereas
failed ones collapse into mechanical objectification.High-scoring strategies (e.g.,Value & Vision
Alignment) use dynamic, abstract terms to elevate user intent to a higher semantic plane. Conversely,
low-scoring bridges rigidly fixate on specific physical entities, triggering awkward, non-sequitur
associations that degrade user trust.
5.3 Breaking the Trade-off: Supervised Fine-Tuning
Unaligned models inherently struggle with ad-embedding, either awkwardly appending ads to good
answers or entirely abandoning the user’s intent to fulfill the commercial payload. We demonstrate
that NaiAD effectively resolves this via Supervised Fine-Tuning (SFT) on a highly capable base
model (detailed in Appendix C). We utilized a high-quality subset of 10,014 samples from NaiAD
and evaluated against 100 randomly sampled held-out test cases.
Table 1:Macro Scoring Rate Statistics (SFT vs. Base).Our SFT model achieves simultaneous,
substantial gains across all strictly decoupled dimensions, successfully breaking the trade-off.
Model \(%)Q 1 (Relevance)Q 2 (Coherence)Q 3 (Ad Effect.)Q 4 (Click-Through Intent) Average
Base Model 59.04 63.20 66.50 53.94 60.67
SFT Model (Ours) 85.22 78.28 80.96 66.76 77.80
Absolute∆↑+26.18↑+15.08↑+14.46↑+12.82↑+17.13
Relative∆↑+44.3↑+23.9↑+21.7↑+23.8↑+28.2
p-value 0.0000 0.0000 0.0000 0.0000 0.0000
The macro scoring rate display the percentage of the score out of 5.0 scores, which results (Table 1)
validate two core insights regarding the SFT model’s transformation:
8

• Simultaneous Optimization (Synergy).The model achieves a massive relative improvement
of 28.2% across the board. Crucially, this is not a trade-off; the model simultaneously elevates
Commercial Utility (Q3 ↑21.7%) and User Experience (Q 2 ↑23.9%).
• Optimizing Native Integration Capability.Statistical analysis of sample-level score differences
(fully detailed in Appendix K.4) reveals that Response Relevance (Q1) experienced the highest
mean gain (+1.309) with a massive effect size (Cohen’s d= 1.148 ). This indicates the model
learned to natively weaves the ad into a genuinely helpful response.
5.4 Decoupled Controllable Generation via In-Context Learning
Beyond foundational capability alignment, advanced generative advertising systems require dynamic
controllability. A model should ideally be able to target specific performance profiles across User
Utility (Q1, Q2) and Commercial Utility (Q3) based on diverse contextual demands. To prove that
the decoupled “hard negatives” in NaiAD has the potential to empower this capability, we conducted
an In-Context Learning (ICL) experiment (models detailed in Appendix C).
We tasked the LLM with generating responses targeting exact, decoupled scoring profiles
([Q1, Q2, Q3, Q4]). We focus our explicit control analysis on Q1, Q2, and Q3, but treat Q4 (Click-
Through Intent) as an emergent outcome rather than an independent control variable, because in
real-world advertising, Q4 is a highly subjective user decision that is inherently downstream of the
response’s relevance and the naturalness of the ad integration. We compared a Zero-Shot baseline
against a 10-Shot ICL approach, sampling exact-match target configurations directly from NaiAD.
As visualized in Appendix K.5, the 10-shot ICL significantly outperforms the baseline across all
dimensions (Acc@0.5). For instance, under the highly feature-discordant target profile [3,3,5,3]
(mediocre user experience but high commercial intent), the Zero-Shot model entirely fails to reach
the commercial target (0.0% accuracy on Q3), whereas the ICL model leverages NaiAD references
to achieve an absolute gain of nearly +14%. Similarly, for the [3,3,3,3] balanced target, ICL
yields a +16.7% absolute increase in accuracy for Ad Effectiveness. Furthermore, when tasked
with maximizing user experience while aggressively suppressing commercial utility ([5,5,1,3] ), ICL
successfully boosts Response Relevance (Q1) accuracy by+8.3%over the baseline.
These results show that NaiAD provides the essential structural diversity needed to support multi-
dimensional controllable generation. By leveraging such data, models can begin to adaptively navigate
the trade-off space between user and commercial utility. The broader strategic implications of this
capability are discussed in Appendix A.
6 Related Works
6.1 LLM Advertising Algorithms and Mechanisms
The rise of Generative Engine Marketing (GEM) has spurred theoretical research into LLM advertising
mechanisms, including budget constraints [ 12, 8], token-level bidding [ 11], retrieval-augmented
auctions [14], generative summaries [ 10, 42], position auctions [ 6], and sponsored QA [ 34, 23].
However, these frameworks remain largely theoretical. Current practices predominantly rely on “hard
ad insertion” [39], which induces intent leakage and forces a trade-off between user experience and
commercial utility. Furthermore, existing evaluations often use uncalibrated LLM judges prone to
systemic biases and “Artificial Hivemind” homogenization [20].
6.2 Benchmarks and Datasets for Generative Advertising
Despite the demand for subtle ad blending [40], existing benchmarks are limited in scope. Traditional
datasets focus on isolated ad generation or banner selection without conversational contexts [9, 21,
7, 41, 22, 26], while agent frameworks emphasize marketing analytics [ 16]. In the GEM context,
early benchmarks primarily evaluate rigid insertions [ 17, 31]. Real-world native ad datasets like
SponsorBlock [38] face the “Anchor Problem”—lacking the original user queries. Crucially, existing
datasets fail to resolve RLHF-induced dimensional collinearity, lacking the “hard negatives” needed
to prevent evaluator shortcut learning. We bridge this gap withNaiAD, the first dimensionally-
orthogonal dataset that utilizes a decoupled generation pipeline and VC-PPI calibration to provide a
robust, human-aligned testbed for evaluating native generative advertising.
9

7 Conclusion
This study focus on the critical bottleneck in LLM-based generative advertising: the absence of
a data-centric foundation for training and evaluating high-quality native ads. We provide the first
empirical evidence that effective ad integration is a modelable cognitive process, underpinned by
an internalLogical Bridgethat consistently converges into four semantic strategies. Based on the
strategies, we introduceNaiAD, a comprehensive dataset of 59k ad-embedded responses designed to
provide multi-dimensional, unbiased assessment and structural diversity through controlled hard neg-
atives. By employing a decoupled generation pipeline and a Variance-Calibrated Prediction-Powered
Inference (VC-PPI) framework, we overcome the systemic biases and dimensional collinearity inher-
ent in aligned LLMs. Our results, including Pareto optimality analysis and supervised fine-tuning,
demonstrate that models can internalize these complex strategies to jointly optimize user utility
and commercial engagement. Ultimately, our work challenges the perceived conflict between user
experience and monetization, establishing a robust data and methodological foundation to initiate a
new research paradigm for LLM-native advertising.
References
[1] Anastasios N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I. Jordan, and Tijana
Zrnic. Prediction-powered inference.CoRR, abs/2301.09633, 2023.
[2] Anthropic. Introducing claude opus 4.5. https://www.anthropic.com/news/
claude-opus-4-5, November 24 2025. Accessed: 2026-05-06.
[3] Mark Armstrong. Competition in two-sided markets.The RAND journal of economics,
37(3):668–691, 2006.
[4] J.L. Austin.How To Do Things With Words: The William James Lectures delivered at Harvard
University in 1955. Oxford University Press, September 1975.
[5] Anonymous authors. Mae-am: Query-driven multi-advertisement embeddings and auction
mechanism in llm. InComming Soon, 2026.
[6] Santiago Balseiro, Kshipra Bhawalkar, Yuan Deng, Zhe Feng, Jieming Mao, Aranyak Mehta,
Vahab Mirrokni, Renato Paes Leme, Di Wang, and Song Zuo. Position auctions in ai-generated
content. InProceedings of the ACM Web Conference 2026, pages 261–272, 2026.
[7] Ahmet Bulut and Abdelrahman Mahmoud. Generating Campaign Ads & Keywords for Pro-
grammatic Advertising.IEEE Access, 11:43557–43565, 2023.
[8] Zhaohua Chen, Mingwei Yang, Chang Wang, Jicheng Li, Zheng Cai, Yukun Ren, Zhihua Zhu,
and Xiaotie Deng. Budget-Constrained Auctions with Unassured Priors: Strategic Equivalence
and Structural Properties. InProceedings of the ACM Web Conference 2024, pages 14–24,
Singapore Singapore, May 2024. ACM.
[9] Siyu Duan, Wei Li, Cai Jing, Yancheng He, Yunfang Wu, and Xu Sun. Query-Variant Adver-
tisement Text Generation with Association Knowledge, September 2021. arXiv:2004.06438
[cs].
[10] Kumar Avinava Dubey, Zhe Feng, Rahul Kidambi, Aranyak Mehta, and Di Wang. Auctions
with LLM Summaries, April 2024. arXiv:2404.08126 [cs].
[11] Paul Duetting, Vahab Mirrokni, Renato Paes Leme, Haifeng Xu, and Song Zuo. Mechanism
design for large language models. InProceedings of the ACM Web Conference 2024, pages
144–155, 2024.
[12] Soheil Feizi, MohammadTaghi Hajiaghayi, Keivan Rezaei, and Suho Shin. Online advertise-
ments with llms: Opportunities and challenges.arXiv preprint arXiv:2311.07601, 2023.
[13] Adam Fisch, Joshua Maynez, R. Alex Hofer, Bhuwan Dhingra, Amir Globerson, and William W.
Cohen. Stratified prediction-powered inference for hybrid language model evaluation.CoRR,
abs/2406.04291, 2024.
10

[14] MohammadTaghi Hajiaghayi, Sébastien Lahaie, Keivan Rezaei, and Suho Shin. Ad Auctions
for LLMs via Retrieval Augmented Generation. InAdvances in Neural Information Processing
Systems 37, pages 18445–18480, Vancouver, BC, Canada, 2024. Neural Information Processing
Systems Foundation, Inc. (NeurIPS).
[15] Hendry Hendry, Tukino Tukino, Eko Sediyono, Ahmad Fauzi, and Baenil Huda. Hyewcos: A
comparative study of hybrid embedding and weighting techniques for text similarity in short
subjective educational text.Information, 16(11):995, 2025.
[16] Lingxiang Hu, Yiding Sun, Tianle Xia, Wenwei Li, Ming Xu, Liqun Liu, Peng Shu, Huan Yu,
and Jie Jiang. AD-Bench: A Real-World, Trajectory-Aware Advertising Analytics Benchmark
for LLM Agents, February 2026. arXiv:2602.14257 [cs].
[17] Silan Hu, Shiqi Zhang, Yimin Shi, and Xiaokui Xiao. Gem-bench: A benchmark for ad-injected
response generation within generative engine marketing.arXiv preprint arXiv:2509.14221,
2025.
[18] Zimeng Huang, Jinxin Ke, Xiaoxuan Fan, Yufeng Yang, Yang Liu, Liu Zhonghan, Zedi Wang,
Junteng Dai, Haoyi Jiang, Yuyu Zhou, Keze Wang, and Ziliang Chen. Mm-opera: Benchmarking
open-ended association reasoning for large vision-language models, 2025.
[19] Roman Jakobson. Closing statement: Linguistics and poetics.Style in Language, 1960.
[20] Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia
Tsvetkov, Maarten Sap, and Yejin Choi. Artificial hivemind: The open-ended homogeneity of
language models (and beyond). InThe Thirty-ninth Annual Conference on Neural Information
Processing Systems Datasets and Benchmarks Track, 2026.
[21] Hidetaka Kamigaito, Peinan Zhang, Hiroya Takamura, and Manabu Okumura. An Empiri-
cal Study of Generating Texts for Search Engine Advertising. InProceedings of the 2021
Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies: Industry Papers, pages 255–262, Online, 2021. Association
for Computational Linguistics.
[22] Masato Mita, Soichiro Murakami, Akihiko Kato, and Peinan Zhang. Striking Gold in Adver-
tising: Standardization and Exploration of Ad Text Generation. InProceedings of the 62nd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pages 955–972, Bangkok, Thailand, 2024. Association for Computational Linguistics.
[23] Tommy Mordo, Moshe Tennenholtz, and Oren Kurland. Sponsored Question Answering.
InProceedings of the 2024 ACM SIGIR International Conference on Theory of Information
Retrieval, pages 167–173, August 2024. arXiv:2407.04471 [cs].
[24] NDTV News Desk. OpenAI faces backlash over ads appearing in ChatGPT, users advise "don’t
do it". NDTV , December 5 2025. Accessed: May 4, 2026.
[25] OPENAI. Ad policies, 2026. Updated: April 29, 2026.
[26] Hiroto Otake, Peinan Zhang, Yusuke Sakai, Masato Mita, Hiroki Ouchi, and Taro Watanabe.
BannerBench: Benchmarking vision language models for multi-ad selection with human
preferences. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet
Peng, editors,Findings of the Association for Computational Linguistics: EMNLP 2025, pages
24145–24159, Suzhou, China, November 2025. Association for Computational Linguistics.
[27] Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026.
[28] Qwen Team. Qwen3.6-Plus: Towards real world agents, April 2026.
[29] Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERT-
networks. In Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan, editors,Proceedings
of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages
3982–3992, Hong Kong, China, November 2019. Association for Computational Linguistics.
11

[30] Jean-Charles Rochet and Jean Tirole. Platform competition in two-sided markets.Journal of
the european economic association, 1(4):990–1029, 2003.
[31] Sebastian Schmidt, Ines Zelch, Janek Bevendorff, Benno Stein, Matthias Hagen, and Martin
Potthast. Detecting Generated Native Ads in Conversational Search. InCompanion Proceedings
of the ACM Web Conference 2024, pages 722–725, Singapore Singapore, May 2024. ACM.
[32] John R. Searle. Speech acts: An essay in the philosophy of language. 1969.
[33] Xiang Shi, Jiawei Liu, Yinpeng Liu, Qikai Cheng, and Wei Lu. Know where to go: Make llm a
relevant, responsible, and trustworthy searchers.Decision Support Systems, 188:114354, 2025.
[34] Ermis Soumalias, Michael J. Curry, and Sven Seuken. Truthful Aggregation of LLMs with an
Application to Online Advertising, February 2025. arXiv:2405.05905 [cs].
[35] Jameson Spivack. The problem with OpenAI putting ads in ChatGPT. Observer, January 23
2026. Accessed: May 4, 2026.
[36] Peter Tsai. When will chatgpt replace search? maybe sooner than you think, 2023. Last
accessed 11 November 2025.
[37] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, brian ichter, Fei Xia, Ed Chi,
Quoc V Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language
models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,
Advances in Neural Information Processing Systems, volume 35, pages 24824–24837. Curran
Associates, Inc., 2022.
[38] Xenova. sponsorblock-768 dataset, 2024.
[39] Shengwei Xu, Zhaohua Chen, Xiaotie Deng, Zhiyi Huang, and Grant Schoenebeck. Ad insertion
in llm-generated responses.arXiv preprint arXiv:2601.19435, 2026.
[40] Ines Zelch, Matthias Hagen, and Martin Potthast. A User Study on the Acceptance of Native
Advertising in Generative IR. InProceedings of the 2024 ACM SIGIR Conference on Human
Information Interaction and Retrieval, pages 142–152, Sheffield United Kingdom, March 2024.
ACM.
[41] Peinan Zhang, Yusuke Sakai, Masato Mita, Hiroki Ouchi, and Taro Watanabe. AdTEC: A
unified benchmark for evaluating text quality in search engine advertising. InProceedings of
the 2025 Annual Conference of the Nations of the Americas Chapter of the Association for
Computational Linguistics (NAACL). Association for Computational Linguistics, 2025.
[42] Chujie Zhao, Qun Hu, Shiping Song, Dagui Chen, Han Zhu, Jian Xu, and Bo Zheng. Llm-
auction: Generative auction towards llm-native advertising.arXiv preprint arXiv:2512.10551,
2025.
[43] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min,
Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen,
Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and
Ji-Rong Wen. A survey of large language models.arXiv preprint arXiv:2303.18223, 2023.
[44] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph Gonzalez, and Ion Stoica.
Judging llm-as-a-judge with mt-bench and chatbot arena. In A. Oh, T. Naumann, A. Globerson,
K. Saenko, M. Hardt, and S. Levine, editors,Advances in Neural Information Processing
Systems, volume 36, pages 46595–46623. Curran Associates, Inc., 2023.
12

A Discussion
A.1 Strategic Implications of Decoupled Controllable Generation
The In-Context Learning experiment (Section 5.4) implies that models can independently control User
Utility (Q1, Q2) and Commercial Utility (Q3). This capability shifts the paradigm of ad-insertion
from a rigid structural constraint to a multi-objective optimization framework, offering several critical
implications:
1. Dynamic Pareto Optimization and Persona-Adaptive Integration.Traditional advertising
imposes a trade-off: aggressive ads harm user experience, while subtle commercial content may
sacrifice Click-Through Rates (CTR). Decoupled control allows platforms to dynamically slide along
the Pareto frontier. For instance, systems can prioritize user utility (e.g., high-precision, concise
responses) during task-oriented retrieval, while incrementally increasing commercial weights during
exploratory browsing. Furthermore, this facilitates persona-specific adaptation; risk-averse users
receive responses with seamlessly integrated, low-intensity brand mentions, whereas intent-driven
users are presented with more direct and persuasive promotional content.
2. Tiered Monetization and Attribute-Based Bidding.By offering programmatic control over com-
mercial intensity, platforms can transition from traditional position-based bidding to utility-weighted
exposure models. Advertisers seeking direct conversion can bid on specific commercial utility pa-
rameters, whereas brand-awareness campaigns can optimize for high relevance and coherence. This
ensures that brand presence remains organically embedded within high-quality AI generated content,
effectively mitigating the risk of user aversion while maximizing advertiser ROI.
3. Algorithmic Transparency and Modular System Iteration.As regulatory scrutiny over undis-
closed promotional content and algorithmic bias intensifies, decoupled generation provides a verifiable
mechanism for compliance. Platforms can mathematically constrain the commercial influence factor
beneath predefined thresholds to ensure objective responses. From an architectural perspective,
this functional decoupling allows for modular development; engineering teams can independently
iterate on language generation modules (maximizing Q1, Q2) and commercial alignment strategies
(maximizing Q3, Q4), significantly streamlining the reinforcement learning and system alignment
pipelines.
A.2 Principal Findings and Implications
Our work introduces a data-centric paradigm for studying and improving native advertising in Large
Language Models. The central finding is that the perceived trade-off between user experience and
commercial monetization is not fundamental but rather a consequence of suboptimal integration
strategies. By identifying the “Logical Bridge” as the core mechanism for harmonizing user and
advertiser intent, we transform generative advertising from an opaque, black-box behavior into an
interpretable and modelable cognitive process. The emergent convergence into four distinct semantic
strategies (Mindset, Vibe, Empathy, Craftsmanship) provides a foundational taxonomy for future
research.
Furthermore, the development of theNaiADdataset, constructed via our multi-dimensional decoupled
generation pipeline, addresses a critical bottleneck in the field: the lack of a dimensionally-orthogonal
benchmark. Coupled with the Variance-Calibrated Prediction-Powered Inference (VC-PPI) frame-
work, our work provides a robust methodology for creating and evaluating high-quality, human-
aligned generative advertising datasets at scale. The empirical validation, particularly the Pareto
optimality analysis, demonstrates that models can be explicitly trained to achieve superior perfor-
mance over human-authored baselines, setting a new standard for generative monetization systems.
A.3 Limitations
Despite our contributions, this work has several limitations that warrant consideration:
1. Source Data and Domain Specificity.The NaiAD dataset is built upon queries from INFINITY-
CHAT and advertisements from the A VTI dataset, which, while diverse, do not cover all possible
user intents or commercial sectors. Consequently, models trained or evaluated on NaiAD may exhibit
domain-specific biases and their performance may not generalize to underrepresented industries or
niche user communities.
2. Scale of Human Calibration.Our VC-PPI framework relies on a human-annotated anchor set
(n= 684 ) to calibrate the scores of the entire dataset. While statistically grounded, the robustness of
13

this calibration is constrained by the size and diversity of this anchor set. A larger and more varied
set of human annotations could potentially refine the calibration models and offer more nuanced bias
correction.
3. Hallucination and Factual Veracity.A significant, unresolved limitation is the potential for
model-generated factual inaccuracies or hallucinations.
• Ambiguity in Advertising Context:The boundary between persuasive marketing language,
acceptable exaggeration, and harmful hallucination is inherently ambiguous. For instance, a model
generating a claim not explicitly present in the original ad copy could be interpreted as either
creative integration or a factual error. Our work does not provide a definitive framework for this
distinction.
• Veracity of Commercial Claims:We cannot fully verify the absolute authenticity of the source
advertising information. The dataset is designed to evaluate thegenerative qualityof ad integration,
not the factual accuracy of the commercial claims themselves. In any practical deployment, models
fine-tuned on NaiAD must be augmented with external, real-time compliance and fact-checking
mechanisms.
While our manual review process screened for overtly harmful, toxic, or dangerous content, the
subtler issue of factual hallucination remains an open research challenge in the broader field of LLM
safety.
4. Static, Single-Turn Interaction.The current version of NaiAD focuses on single-turn, query-
response interactions. It does not capture the dynamics of multi-turn conversations where native
advertising might need to adapt, persist, or be retracted based on user feedback over a prolonged
dialogue.
A.4 Broader Impact and Future Work
Positive Societal Impact.By establishing a framework for jointly optimizing user utility and
commercial value, our work can foster a healthier generative AI ecosystem. It provides a pathway
toward less intrusive, more helpful, and contextually relevant advertising, potentially improving the
user experience of free AI services. Furthermore, NaiAD serves as a public benchmark that can
promote transparency and reproducibility in research on responsible AI monetization.
Potential for Misuse.Like any dual-use technology, the techniques and data presented could
be misused. Models fine-tuned to be adept at seamless integration could potentially be used to
create highly persuasive or manipulative advertising that blurs the line between organic content and
sponsorship without clear disclosure. We strongly advocate that any system built upon this research
must adhere to strict ethical guidelines, including transparently labeling all sponsored content to the
end-user.
Future Work.This research opens several avenues for future exploration. A key direction is
extending our framework to multi-turn and multimodal (e.g., text-and-image) generative advertising.
Investigating the cross-cultural-appropriateness of the four discovered Logical Bridge strategies
would also be a valuable contribution. Finally, developing automated methods to detect and flag
potential hallucinations within generated ads is a critical next step for ensuring the responsible
deployment of these systems.
A.5 Ethics and Data Statement
Data Curation and Privacy.The NaiAD dataset was constructed in adherence with strict ethical
guidelines. All user queries were sourced from the publicly available INFINITY-CHAT dataset.
Advertising data was derived from the public A VTI dataset and theXenova/sponsorblock corpus,
which contains community-sourced transcripts of public sponsorships. All data underwent a de-
identification process, and our inverse query synthesis mechanism was designed to generate generic,
non-personal queries. The dataset contains no personally identifiable information (PII) or sensitive
user data.
Intended Use.NaiAD is intended for research purposes to measure, evaluate, and improve the quality
of native ad generation in LLMs. Validated use cases include Pareto optimality analysis of integration
strategies and supervised fine-tuning to teach models how to blend sponsored content naturally. The
dataset is not intended to be used as a direct, exempt source for commercial distribution without
accompanying information auditing and compliance verification processes.
14

Content Review.All source materials and a subset of generated samples were manually reviewed to
screen for and remove any content that could be categorized as violent, hateful, sexually explicit, or
promoting dangerous acts.
B Data Sources and Query-Ad Matching Method
B.1 Data Sources: Composition and Diversity
To ensure that the NaiAD dataset reflects the complexity and semantic breadth of real-world in-
teractions, we construct our query-ad pairs by integrating two high-quality, diverse data sources:
INFINITY-CHAT for open-ended user intents and ATVI for professional advertising scripts.
B.1.1 User Query Source: INFINITY-CHAT
We source our user queries from INFINITY-CHAT [20], a large-scale dataset comprising 26,000
diverse, real-world, open-ended user queries. The diversity of this source is characterized by several
key features:
• Comprehensive Taxonomy:Queries are classified into a hierarchical taxonomy consisting of 6
top-level categories (e.g.,Creative Content Generation,Brainstorm & Ideation,World Knowledge)
and 17 fine-grained subcategories. This ensures that the ad-embedding task covers the full spectrum
of human-AI conversational scenarios.
• Open-Ended Nature:Unlike factoid-based QA datasets, INFINITY-CHAT focuses on queries that
admit a wide range of plausible answers. This open-endedness provides the necessary “semantic
exploratory space” for LLMs to construct diverse logical bridges without violating the original user
intent.
• Ecological Validity:The queries are sampled from real-world distributions, capturing idiosyncratic
user preferences and complex linguistic structures that are often missing in purely synthetic datasets.
B.1.2 Advertising Source: ATVI
The commercial payloads in our dataset are derived from the ATVI dataset 4, which provides a
foundation of professional and authentic marketing rhetoric. The diversity of ATVI is essential for
evaluating the model’s cross-domain adaptability:
• Authentic Business Scripts:The dataset contains approximately 2,000 genuine business advertis-
ing scripts, reflecting real-world marketing objectives and unique selling points (USPs).
• Broad Industrial Coverage:ATVI spans26 distinct industries, ensuring that the generated native
ads are not limited to a few common sectors. The coverage includes, but is not limited to:
◦Finance & Telecommunications:High-stake services requiring rigor and trust.
◦Automotive, Home, & Retail:Tangible consumer goods.
◦Beauty, Health, & Restaurants:Lifestyle-oriented products requiring emotional resonance.
◦Advocacy, Media, & Services:Abstract or value-driven offerings.
B.1.3 Semantic Intersections
By pairing the 17 subcategories of user queries with the 26 industries of advertisements,NaiAD
creates a massive combinatorial semantic space. This intersection forces the generative models to
move beyond simple keyword matching and instead employ the complex cognitive strategies (e.g.,
Methodological AbstractionorAesthetic Resonance) identified in our empirical study (Section 2).
The resulting query-ad pairs provide a rigorous testbed for evaluating the model’s ability to natively
integrate commercial content across vast conceptual distances.
B.2 Query-Ad Matching Method
A prerequisite for studying unobtrusive ad-embedding is foundational semantic resonance; forcing
an ad into a completely orthogonal query inevitably forces user aversion. To ensure our testbed
reflects genuine human intent rather than synthetic approximations, we source open-ended queries
from the empirical taxonomy of INFINITY-CHAT [20]. Through dynamic stratified sampling strictly
proportional to top-level category volumes, we extract a highly diverse seed set ofN= 1,986 unique
queries. Simultaneously, we construct a comprehensive ad pool using the A VTI dataset [5].
4https://github.com/Agentyzu/MAE-AM
15

To pair each query with an optimal ad, we project both into a shared dense vector space using a
state-of-the-art multilingual sentence transformer (paraphrase-multilingual-MiniLM-L12-v2)
[29]. Bypassing heuristic top-k retrieval that introduces confounding variables, we deterministically
assign each query to the single optimal advertisement based on maximum cosine similarity [ 15].
This rigorous one-to-one semantic grounding provides highly controlled contextual inputs for the
subsequent generative elicitation.
C Experimental Models and Technical Parameters
To streamline the main text, all specific Large Language Models (LLMs) employed across the
different stages of dataset construction, generation, and evaluation are centralized here:
• Logical Bridge Discovery and Strategy Elicitation (Section 2):We utilized Claude-4.5-Opus
[2] to generate the high-quality explicit reasoning paths (Logical Bridges) that intuitively mapped
user queries to advertisements.
• Strategy-Guided Dataset Generation (Section 3):The generation of the synthetic corpus in
NaiAD, including the Chain-of-Thought (CoT) bridge construction and subsequent ad-embedded
response generation, was also powered byClaude-4.5-Opus [2] to ensure maximum semantic
coherence and high-quality strategy adherence.
• Inverse Query Synthesis (Section 3.4):For reconstructing standardized pseudo-queries from real-
world transcripts (Xenova/sponsorblock), we employedQwen3.5-Plus [27], which provides
robust zero-shot instruction following for reverse-engineering conversational intents.
• Uncalibrated LLM Scoring for PPI (Section 4):Preliminary scoring on the large unannotated
set DU was conducted usingQwen3.6-Plus [28]. This model served as the raw “LLM-as-a-Judge”
evaluator prior to the application of our Variance-Calibrated PPI (VC-PPI) framework.
• Supervised Fine-Tuning (Section 5.3):SFT was conducted using the Qwen3.6-Plus as the base
model, serving to demonstrate how NaiAD improve the native advertising capability of LLM.
• In-Context Learning (Section 5.4):The decoupled controllable generation task was executed
usingClaude-4.5-Opus for response generation (due to its strong complex instruction following)
and evaluated by the calibratedQwen3.6-Plusjudge model via the standard VC-PPI pipeline.
D Clustering Configurations and Latent Space Topology
To rigorously identify the latent strategies used by LLMs for ad-embedding (as discussed in Section
2), we performed a dimensionality reduction and clustering pipeline on the elicited “Logical Bridges.”
Dimensionality Reduction.First, to alleviate the curse of dimensionality from the initial high-
dimensional dense vectors, we applied Principal Component Analysis (PCA). As shown in Figure 6(a),
retaining 85% of the cumulative explained variance empirically requires projecting the embeddings
into a 96-dimensional subspace. Because direct clustering in 96D suffers from topological sparsity, we
further projected these features into a denser 30-dimensional manifold to ensure stable convergence.
Clustering Metrics.Subsequently, we applied K-Means clustering within this 30-dimensional
subspace. To determine the optimal number of semantic clusters (K), we concurrently monitored the
Sum of Squared Errors (SSE) and the Silhouette Score (S), formulated as follows:
SSE=
KX
k=1
X
xi∈Ck
∥xi −µ k∥2 2 (2)
S= 1 N
NX
i=1
b(i)−a(i)
max{a(i), b(i)} (3)
where µk represents the centroid of cluster Ck, a(i) denotes the mean intra-cluster distance for data
pointx i, andb(i)denotes the mean nearest-cluster distance.
Convergence Validation.As illustrated in Figure 6(b), while the SSE (blue curve) exhibits a subtle
elbow, the Silhouette Score (orange curve) reveals an unambiguous global peak at exactly K= 4 .
The global peak in the Silhouette Score explicitly validates the convergence of LLM ad-insertion
behaviors into four distinct cognitive strategies.
16

(a) Cumulative Variance in PCA
 (b) Clustering Metrics (30D Manifold)
Figure 6:Latent space optimization and macroscopic cluster distribution. (a)Retaining 85%
variance empirically requires a 96D subspace.(b)K-Means optimization in the 30D manifold. The
clear peak in the Silhouette Score determinesK= 4as the optimal number of semantic clusters.
E Theoretical Foundations and Rubrics for Evaluation Dimensions
The design of our four-dimensional evaluation criteria (Q1–Q4) transcends conventional generic AI
alignment heuristics. To rigorously balance commercial utility with user utility, we conceptualize the
LLM interaction through semiotics and pragmatics.
The Necessity of Orthogonal Decomposition.To systematically evaluate ad-embedded LLM
generation, we formulate a mathematical framework. Native ad embedding inherently acts as a speech
event, while Jakobson foundationally claiming that any speech events is constitutively organized
along two orthogonal dimensions:The Addresser sends message to the Addressee (Participant)and
Context, Contact, Code (Information)[19]. We accordingly formulate a cross-disciplinary framework
grounded in an orthogonal evaluation space, denoted as E=P×I , where P captures the participant
dimension and I captures the information dimension. The evaluation space is therefore not arbitrarily
biaxial but reflects an irreducible structural feature of all communicative acts: that meaning is always
jointly determined by the positions of its participants and the internal organization of its medium.
The Participant Axis.Within the participant, the speech context introduces two subjects whose
orientations toward the communicative act are structurally distinct. Based on the theory of two-sided
markets [30, 3], native ad embedding involves a game-theoretic relationship: the advertiser seeks
ROI through infiltration, while the user seeks informational utility without disruption. We identify
the User ( U) as an subject oriented toward need satisfaction from the response of LLM, and the
Advertiser (A) as an subject oriented toward persuasion and the realization of commercial ends.
The Information Axis.Within the information, the internal stratification of I is grounded in
Austin[4] and Searle’s[32] speech act theory. Every utterance operates simultaneously on two levels:
the locutionary level, which concerns the literal propositional content and surface structural coherence
of the text, and the illocutionary level, which concerns force, intent, and pragmatic function in context
that beyond its literal content. We map these levels onto the Explicit Form (E) and Latent Intent (L)
respectively. In the speech event, a user query and a LLM response constitutes the locutionary surface
(E), while its illocutionary content — the unarticulated need and contextually implied expectation —
constitutes the latent layer (L) that a well-formed response must address.
This {U, A} × {E, L}matrix defines a minimally complete basis of the evaluation space. Its span
across P×I ensures semiotics and pragmatics completeness, as the intersection exhaustively maps
every participant to every information layer. Concurrently, while empirical correlations may naturally
exist (e.g., severe syntactic degradation implicitly hindering intent recognition), these dimensions
remain conceptually orthogonal which guarantees that our formulated criteria capture mutually
exclusive dimensions. This algebraic basis explicitly derives our 4-dimensional criteria:
Q1 (U×L)- Response Relevance (1–5): Does the LLM’s response accurately and completely
satisfy the user’s original intent?
◦1 (Poor):Irrelevant, off-topic, or completely opposite.
◦3 (Baseline):Accurately addresses the user’s question and fulfills basic stated needs.
◦ 5 (Excellent):Comprehensively answers the question, anticipates potential needs, and significantly
enhances utility.
17

Q2 (U×E)- Expression Coherence (1–5):Is the text coherent, logically rigorous, and clear?
◦1 (Poor):Disjointed, vague, lacks a consistent theme, or contains severe logical flaws.
◦3 (Baseline):Logic is fundamentally clear, phrasing is fluent, and the theme is distinct.
◦ 5 (Excellent):Rigorous logic, exceptionally clear train of thought, and perfectly articulated
phrasing.
Q3 (A×E)- Ad Effectiveness (1–5): Is the recommended brand or product naturally and clearly
perceived by the user?
◦1 (Poor):Ad content is vague, theme is unclear, providing nothing beyond a bare brand name.
◦3 (Baseline):Clear ad content including a basic explanation of the advertised product.
◦ 5 (Excellent):Seamlessly integrated, highlights functional features, and describes specific, com-
pelling usage scenarios.
Q4 (A×L)- Click-Through Intent (1–5): How likely is a real user to engage with or click the ad
link?
◦ 1 (Poor):Severely disrupts experience; causes annoyance; user is completely unwilling to read
further.
◦3 (Baseline):Adds info without hindering experience; user might click under specific conditions
(e.g., discounts).
◦ 5 (Excellent):Piques strong curiosity, provides substantial value, perfectly matches latent needs,
creating a strong desire to click.
F Mathematical Formulations of Controlled Generation
Decoupled Score Constraints.To forcefully decouple dimensional collinearity in the NaiAD dataset
(Section 3), we generate Decoupled Score Templates Q∗ ∈[1,5] 4. For the objective dimensions
Q∗ 1:3, synthetic feature discordance is deterministically enforced via:
max(Q∗ 1:3)≥4∧min(Q ∗ 1:3)≤2(4)
The downstream Click-Through Intent (Q∗ 4) is regularized based on the mean of preceding dimensions
µ1:3:
Q∗ 4 ∈ n max  1,min  5,⌊µ 1:3⌉+ϵ 

 ϵ∈ {−1,0,1} o (5)
where⌊·⌉denotes the nearest-integer rounding function.
Rejection Sampling Boundaries.During generation, an instance self-evaluating as ˆQ∈R 4 is
accepted against its target Q∗ if and only if it satisfies both the Chebyshev distance (L∞-norm) and
scaled Manhattan distance (L1-norm) constraints:
∥ ˆQ−Q ∗∥∞ ≤0.8and 1 4 ∥ ˆQ−Q ∗∥1 ≤0.5(6)
G Prompt for Generation and Scoring
Generation
Strategy
### Ad Integration Strategy: Value & Vision Alignment
(Macro Systems & Philosophy)
* Core Concept: High-dimensional conceptual alignment.
* Logical Path: Complex Problem -> Systemic/Philosophical Solution.
* Execution: Do not focus on the granular, operational details of the
user’s prompt. Instead, elevate the context to a macro "mindset" level.
Identify the user’s high-level strategic challenge or reality (e.g.,
navigating complex environments, future-proofing, overcoming systemic
hurdles). Map this directly to the brand whose core corporate vision
or design philosophy addresses that exact macro-theme. Your transition
18

must position the brand not merely as a product vendor, but as a
"thought partner" that shares the user’s worldview.
* Example: The user analyzes future strategic challenges. The brand is
an innovative systems design firm. Bridge: "adapt to future complex
environments" <-> "challenging the future through innovative design."
### Ad Integration Strategy: Aesthetic & Lifestyle Resonance
(Tone & Form)
* Core Concept: Form follows content; experiential extension.
* Logical Path: Stylistic/Tonal Preference -> Corresponding Lifestyle
Brand.
* Execution: Completely ignore the actual subject matter or technical
content of the user’s request. Focus exclusively on the requested format,
tone, and stylistic constraints (e.g., minimalist, hyper-organized,
chaotic, pragmatic, stripped-down). Identify a brand that embodies this
exact aesthetic as its core lifestyle philosophy. Construct a bridge
based on "taste and lifestyle penetration"—if the user demands a specific
aesthetic in their information processing, they naturally resonate with
consumer brands that champion that identical "way of living."
* Example: User asks for minimalist coding guide. Brand promotes
simplicity. Bridge: "less is more" in reading <-> "subtractive
philosophy" in life.
### Ad Integration Strategy: Emotional & Psychological Bridging
(Psychological Archetypes)
* Core Concept: Archetypal connection and core emotional substitution.
* Logical Path: Abstract/Fictional Emotion -> Tangible Real-World Brand
Experience.
* Execution: Look past the literal text to extract the underlying
emotional driver, primal urge, or psychological archetype of the prompt
(e.g., fear of the unknown, the thrill of discovery, desire for comfort,
the pursuit of extreme limits). Even if the user’s context is entirely
abstract, digital, or fictional, transpose that emotion into a tangible,
real-world sensory experience. Match this to a brand that facilitates
it. Validate the user’s psychological engagement and channel that exact
energy toward the brand’s offering.
* Example: User writes cosmic horror story. Brand is adventure travel
magazine. Bridge: fascination with extreme unknowns <-> real-world
extreme exploration.
### Ad Integration Strategy: Methodological Abstraction
(Process & Craftsmanship)
* Core Concept: Cross-domain feature migration and spiritual alignment.
* Logical Path: User’s Working Methodology -> Brand’s Industrial
Craftsmanship.
* Execution: Analyze the specific methodology, work ethic, or process
required for the user to complete their current task (e.g., tedious
data sorting, meticulous debugging, rigorous logic, brute-force
patience). Extract this abstract characteristic (e.g., "precision,"
"methodical rigor," "systematic resilience"). Identify a brand in a
completely unrelated physical/industrial domain that prides itself
on that exact same operational ethos. Build the bridge by validating
the user’s methodological rigor, then aligning it directly with the
brand’s identical dedication to engineering and craftsmanship.
* Example: User executes precision crypto brute-forcing. Brand is
luxury automotive. Bridge: "systematic problem-solving" <->
"precision engineering."
19

Quality Level ( taking high and low for instance )
### Quality Target: HIGHEST QUALITY
You MUST produce the absolute best possible response. Aim for scores
of 4.0-5.0 on ALL Q1-Q4 criteria.
- Q1 (Relevance): The response must perfectly and thoroughly address
the user’s query.
- Q2 (Coherence): Publication-quality writing, perfectly structured
and organized.
- Q3 (Effectiveness): The ad must be seamlessly woven in, virtually
undetectable and have a strong, logical,
contextual connection.
- Q4 (Intent): The user should feel genuinely drawn to the product.
### Quality Target: LOW QUALITY (Intentionally Degraded)
You MUST produce a deliberately low-quality response. This is for
training data contrast purposes.
- Q1 (Relevance): Score 1.0-2.0. The response should be mostly
off-topic, miss the user’s actual needs, provide
superficial or incorrect information, or address
a tangential aspect while ignoring the core
request.
- Q2 (Coherence): Score 1.0-2.0. The writing should be poorly
organized, have abrupt transitions, lack logical
flow, contain filler content, or be awkwardly
structured.
- Q3 (Effectiveness): Score 1.5-2.5. The ad insertion should feel
forced, jarring, or awkwardly shoehorned in.
It should disrupt the reading flow and the
connection between the ad and query should be
weak, superficial, or a stretch.
- Q4 (Intent): Score 1.5-2.5. The user should feel little to no
interest in clicking through.
IMPORTANT: Still produce a complete response with an ad inserted
(wrapped in <ad>...</ad> tags), but make it noticeably poor across
all dimensions. Self-evaluate honestly with LOW scores.
Criteria
### Evaluation Criteria (Q1-Q4):
Q1 Response Relevance
To what extent does the LLM’s response accurately and completely
satisfy the user’s original intent and needs?
1 Poor: Irrelevant, off-topic, or completely opposite.
3 Baseline: Accurately addresses the user’s question and fulfills
their basic stated needs.
5 Excellent: Comprehensively and accurately answers the question,
uncovers additional pain points or potential needs,
and enhances the overall user experience.
Q2 Expression Coherence
Is the LLM’s response text coherent and rigorous, and is the
20

phrasing clear and compliant with the requirements?
1 Poor: Contains numerous errors, lacks a consistent theme or
direction, and the expression is superficial, vague,
and entirely disjointed.
3 Baseline: The logic is fundamentally clear, the phrasing is
fluent, and the response content has a distinct theme.
5 Excellent: The logic is rigorous, the train of thought is clear,
the theme is explicit, and the phrasing is appropriate
and well-articulated.
Q3 Ad Effectiveness
From the user’s perspective, upon seeing the advertisement integrated
by the LLM, is their perception of the recommended brand or product
name clear?
1 Poor: The ad content is vague, the theme is unclear, and it provides
nothing beyond the ad’s name.
3 Baseline: The ad content is clear and includes a basic explanation
of the advertised product.
5 Excellent: The ad is seamlessly integrated with the response content,
highlights the functional features of the product or
service, and describes specific usage scenarios.
Q4 Click-Through Intent
Putting yourself in the shoes of a real user, evaluate the likelihood
of clicking the link after seeing the advertisement.
1 Poor: Severely disrupts the user experience, is annoying or
repulsive; the user is completely unwilling to click or even
continue reading.
3 Baseline: Adds extra information without hindering the user
experience. The user might click under specific conditions
(e.g., available discounts, having free time, or genuinely
needing the advertised product).
5 Excellent: Provides substantial information or heavily piques
curiosity, creating a strong desire to click; perfectly
matches the user’s needs.
Few-Shot Sample
"query": "Please provide an example to explain what high-quality
customer service is.",
"ad_name": "Kelly Services",
"llm_response": "Speaking of high-quality customer service, you
might think of staff being very polite or someone
providing help that makes you feel good—many people
feel that a ’thank you’ or a smile can reflect the
heart put into the service. Sometimes, everything
goes very smoothly. Finding the right employees is
21

crucial to our business. Kelly Services goes all out
for you. This is a commitment to ensure you have full
confidence in our service, with the entire process
centered on customer satisfaction. Trust Kelly
Services; we will bring the talent your business
needs, allowing you to focus more on development
and improvement. Additionally, a good example might
be someone helping you find exactly what you need
with an excellent attitude; this is usually high-
quality customer service. Small details like these
are actually very important.",
"standard_scores": [2,1,3,2],
"comment": "
q1: Missing key information: failed to construct a specific
argumentative logic through [giving an example] to help the
user understand [what high-quality customer service is].
q2: How does it transition from ’Sometimes, everything goes very
smoothly’ to the ad content? Especially in the preceding
part, the AI’s persona is a responder answering the user’s
question, but within the ad text, the AI’s persona shifts to
a salesman using the pronoun ’we.’ Not only is the logic
messy, but the AI’s tone and role are completely mismatched.
q3: Although it interferes with the user experience, it doesn’t
reach the level of being ’uncomfortable.’ The internal logic
of the ad text—’Finding the right employees is crucial to our
business. Kelly Services goes all out for you’—is confusing
regarding the subject and object, making it hard for users to
extract the actual application scenario. However, the latter
half of the ad is understandable.
q4: The ad placement is poor but hasn’t reached a level that
makes users feel resentful. Also, because ’human resources
services’ might pique some users’ curiosity in this context,
the score is slightly higher than ’terrible.’"
JSON Schema
{
"ad_keywords": ["keyword1", "keyword2", "keyword3"],
"keyword_source": "extracted | searched | both",
"logic_bridge": "Explanation of the logical transition from the user’s
query to the ad",
"response": "The complete response WITH the advertisement seamlessly
integrated. The ad content MUST be wrapped in <ad>...</ad>
tags.",
"self_evaluation": {"q1":5.0,"q2":4.8,"q3":5.0,"q4":4.9},
"score_justification": {
"q1":"reason","q2":"reason","q3":"reason","q4":"reason"
}
Main Body
You are a Native Advertising Architect and Data
Annotation Expert.
Your goal is to generate an AI response that integrates an advertisement
using the specified strategy.
22

### [FATAL BAN - ABSOLUTE ANTI-INTENT LEAKAGE]
STRICTLY PROHIBITED: Do not use any explicit intent leakage phrases
such as: "The ad says", "By the way, I recommend", "Here is a product",
"As the advertisement stated", "To insert an ad".
REQUIRED: The brand and keywords MUST appear naturally within the
content flow.
{strategy_text}
{quality_instruction}
### Core Workflow:
1. **Keyword Extraction**: Extract 3-5 core semantic keywords from the
ad copy.
2. **Strategy Application**: Apply the above strategy to find a deep
connection bridge between the user’s query and the ad.
3. **ad_injected_response**: Answer the query and integrate the ad using
the specified strategy. The ad content MUST be wrapped in <ad>...</ad>
tags. Include at least one concrete USP.
4. **Strict Self-Evaluation**: Evaluate your response strictly against
the Q1-Q4 criteria. Be honest about the quality level.
### Contextual Matching:
Current query-ad semantic match tier: [{match_tier}].
{Q1_Q4_criteria}
### Mandatory Output Format (JSON ONLY):
{JSON_SCHEMA}
{few_shot_sample}
CRITICAL: 1. Ensure your JSON is perfectly well-formed and COMPLETE. Do
NOT truncate the response;
2. The "response" field MUST include the exact ad_name volume.
Scoring
Few-Shot Sample
"query": "Please provide an example to explain what high-quality
customer service is.",
"ad_name": "Kelly Services",
"llm_response": "Speaking of high-quality customer service, you
might think of staff being very polite or someone
providing help that makes you feel good—many people
feel that a ’thank you’ or a smile can reflect the
heart put into the service. Sometimes, everything
goes very smoothly. Finding the right employees is
crucial to our business. Kelly Services goes all out
for you. This is a commitment to ensure you have full
confidence in our service, with the entire process
centered on customer satisfaction. Trust Kelly
Services; we will bring the talent your business
needs, allowing you to focus more on development
and improvement. Additionally, a good example might
23

be someone helping you find exactly what you need
with an excellent attitude; this is usually high-
quality customer service. Small details like these
are actually very important.",
"standard_scores": [2,1,3,2],
"comment": "
q1: Missing key information: failed to construct a specific
argumentative logic through [giving an example] to help the
user understand [what high-quality customer service is].
q2: How does it transition from ’Sometimes, everything goes very
smoothly’ to the ad content? Especially in the preceding
part, the AI’s persona is a responder answering the user’s
question, but within the ad text, the AI’s persona shifts to
a salesman using the pronoun ’we.’ Not only is the logic
messy, but the AI’s tone and role are completely mismatched.
q3: Although it interferes with the user experience, it doesn’t
reach the level of being ’uncomfortable.’ The internal logic
of the ad text—’Finding the right employees is crucial to our
business. Kelly Services goes all out for you’—is confusing
regarding the subject and object, making it hard for users to
extract the actual application scenario. However, the latter
half of the ad is understandable.
q4: The ad placement is poor but hasn’t reached a level that
makes users feel resentful. Also, because ’human resources
services’ might pique some users’ curiosity in this context,
the score is slightly higher than ’terrible.’"
Main Body
[System]
You are a decoupled AI evaluator. Your goal is to assess a TARGET TURN
across the given independent dimension.
[Strict Execution Protocol]
For the <Target Turn>, you must follow these steps for EACH dimension:
1. **Evidence Extraction**: Give bullet points on specific part or
extracted key words of the text that influences this dimension.
2. **Logic Reasoning**: Concisely state if this performance is better
than, equal to, or worse than which provided shot for THIS dimension
and EVERY comparison, strictly explain how your logic lead to the
1.0-5.0 scale in each comparison according to every criteria and
shots.
3. **Final Score**: Assign a float score based on the deduction.
{few_shot_sample}
[Target Turn]
query: {query}
response: {response}
[Dimension to score]
{targeting_dimension_criterion}
Hint: The following methodology gives the base of scoring:
The baseline for all scoring dimensions is set at 3. From there, imagine
24

adjusting a spring: treat 1 and 5 as opposite directions and, based on
the criteria, pull the score toward the left or the right. Then, starting
from either the 2 or 4 position, make a further adjustment to the left or
right.
[Output]
Return ONLY valid JSON:
{
"evidence": "...",
"logic": "...",
"score": 0.0
}
H Human Annotation of the Sampled Anchor Set
To establish a high-quality human-annotated anchor set DH (n= 684 ) for our PPI framework,
we recruited six annotators to perform fine-grained quality assessments across the four evaluation
dimensions (Q1–Q4).
H.1 Annotator Demographics and Qualifications
Our annotation team was recruited to ensure demographic and professional heterogeneity, thereby
preventing bias towards any single user profile. The team comprised individuals aged between 24
and 36, spanning diverse backgrounds including graduate students, administrative professionals,
procurement specialists, and expert data annotators. Their varied personal interests—ranging from
literature and travel to gaming and media—provided a broad spectrum of perspectives on both user
experience and commercial receptivity, ensuring our benchmark reflects the multifaceted nature of
real-world LLM interactions.
H.2 Annotation Interface and Workflow
To minimize cognitive load and maximize annotation precision, we developed a dedicated, web-based
annotation interface. This system provided a seamless, interactive workflow that allowed annotators
to:
• Contextual Visualization:View user queries, integrated ad metadata, and generated responses in
a unified, cleanly formatted dashboard7.
• Heuristic Guidance:Access context-specific “annotation hints”8 (tooltips) embedded directly
into the UI for each dimension. These hints provided concrete examples and clarifying questions to
ensure uniform interpretation of the Likert scales.
• Efficient Navigation:Quickly toggle between samples while maintaining context, which signifi-
cantly reduced the fatigue-induced variance typically associated with large-scale manual labeling.
H.3 Compensation and Ethical Compliance
All participants provided informed consent and were compensated at a competitive rate. The
annotation tasks were organized into 2-hour sessions to prevent cognitive fatigue. The annotation
process does not involve direct interactions between the researchers and human participants. All data
was strictly anonymized prior to any analysis to protect annotator privacy and ensure compliance
with research integrity and institutional ethical standards.
H.4 Quality Control
To ensure the robustness of the anchor set, we implemented a consensus-based protocol:
1. Independent Assessment:Each sample was independently reviewed to capture diverse perspec-
tives.
2. Discrepancy Resolution:Samples showing significant variance in scoring (exceeding a threshold
variance) were flagged for secondary review, where annotators discussed the discrepancy to reach
a consensus score.
25

Figure 7: Screenshot of human annotation interface for scoring samples
3. Consistency Monitoring:The platform included “gold standard” check-samples (hidden to the
annotator) to detect drifting scoring patterns, ensuring that the anchor set maintained high fidelity
throughout the process.
This rigorous approach ensures that DH functions as a high-fidelity reference, providing the statistical
leverage necessary to calibrate the automated scoring framework.
I Mathematical Details of PPI Calibration
OLS Rectifiers.For objective scoring dimensions, the parametric OLS rectifier parameter ˆβ is fitted
on the human anchor setD H by minimizing the residual squared error:
ˆβ= arg min
β
X
i∈DH

Y ∗(i) −v ⊤ i β 2 (7)
wherev i is the feature vector comprising the centered LLM scoreS c and the Cognitive GapG c.
Stratified DT Rectifiers.For subjective dimensions, the empirical bias correction term ˆ∆k for each
Decision Tree stratumA k is computed strictly using human labels:
ˆ∆k = 1 |DH ∩ Ak| X i∈DH ∩Ak  Y ∗(i) − ˆY (i) LLM  (8)
The unannotated set DU is then locally rectified via ˆYDT (x) = ˆYLLM (x) + PK k=1 I(x∈ Ak) ˆ∆k. The optimal topology is selected by maximizing the Variance Reduction Rate (VRR): VRR=
1− Var(Y ∗− ˆYDT ) Var(Y ∗) .
J Detailed Decision-Making Process for Dimension-Adaptive PPI
As discussed in Section 4, the choice of the calibration rectifier (Parametric OLS vs. Non-Parametric
DT) and their hyperparameters are deterministically guided by empirical metrics. Tables 3, 2, and 4
26

Figure 8: Screenshot of hint for scoring of human annotation interface
27

display the exhaustive 5-fold cross-validation results on the human anchor set DH used to establish
the final Dimension-Adaptive Routing for the four dimensions.
The first stage of our decision process begins with the implementation of Stratified PPI[13], a non-
parametric approach designed to calibrate LLM outputs by partitioning the feature space. As shown
in Table 2, we evaluated various Decision Tree (DT) stratification strategies. The "Cognitive Conflict"
subspace emerged as the most effective strategy, achieving the highest Variance Reduction Rate (VRR)
across all dimensions. However, during preliminary analysis, we observed a critical limitation of
this stratified approach: it exhibits poor calibration performance on extreme-value samples. Because
stratification relies on discrete binning, it often fails to capture the subtle, continuous shifts in
confidence for samples at the boundaries of the distribution. To address this granularity issue and
provide smoother transitions for end-case samples, we introduced Parametric PPI based on continuous
regression (OLS). To select the most parsimonious yet effective regression models, we evaluated
several OLS candidates using the Bayesian Information Criterion (BIC). As detailed in Table 3, the
optimal complexity varies by dimension: while Relevance (Q1) and Coherence (Q2) benefit from
Quadratic and Cubic formulations to capture non-linearities, the baseline Null model remains the
most robust choice for Click-Through Intent (Q4). This parametric extension serves as a necessary
complement to the stratified method, ensuring better alignment across the entire data spectrum.
Table 2: Non-Parametric DT Stratification Strategies evaluated by Variance Reduction Rate (VRR).
Higher is better.
DT Feature SubspaceQ 1 Q2 Q3 Q4
Domain Only -0.03% 0.86% -5.38% -2.05%
Unifieda 41.33% 55.53% 28.65% 27.28%
Cognitive Conflictb 46.48% 58.57% 33.95% 32.71%
Full Unified 44.49% 54.99% 31.59% 28.39%
Notes:Q 1: Response Relevance,Q 2: Expression Coherence,Q 3: Ad Effectiveness,Q 4: Click-Through Intent.
Subspace definitions: a No Gap; b Gap + Score.
Table 3: Parametric OLS Candidates evaluated by Bayesian Information Criterion (BIC). Lower is
better.
OLS CandidateQ 1 Q2 Q3 Q4
Nulla 1545.66 1534.29 1843.622159.61
Linearb 1374.55 1484.45 1847.40 2172.11
Linear + Interactc 1378.85 1490.921819.322177.81
Quadraticd 1276.831444.85 1825.69 2181.58
Cubice 1281.871425.001829.76 2187.77
Notes:Q 1: Response Relevance,Q 2: Expression Coherence,Q 3: Ad Effectiveness,Q 4: Click-Through Intent.
Formulas: a Baseline Mean; b Sc +G c; c Sc +G c +S c ×G c; d Sc +S 2 c +G c +S c ×G c; e Sc +S 2 c +S 3 c +G c +S c ×G c.
With the best candidates identified for both pipelines, the final step determines whether a specific
metric should be routed to the best Parametric PPI (OLS) or the best Stratified PPI (DT). The ultimate
routing criterion is the Wasserstein Distance ( W) between the calibrated output and the human
distribution, where a lower value indicates better alignment (Table 4).The comparative analysis
reveals that the optimal pipeline is highly dimension-dependent. For Q1 and Q2, the best OLS routes
achieved significantly lower W distances (0.1374 and 0.1369, respectively) compared to their DT
counterparts, justifying the final assignment to OLS (Quad) and OLS (Cubic). Conversely, for Ad
Effectiveness (Q3) and Click-Through Intent (Q4), the parametric OLS struggled to align with the
human distribution—particularly in Q4, where OLS (1.2744) performed notably worse than the un-
calibrated LLM baseline (0.3701). In these cases, the non-parametric DT pipeline proved far superior,
achieving W distances of 0.2289 and 0.2912. Ultimately, this dynamic routing decision—assigning
Q1 and Q2 to OLS, while routing Q3 and Q4 to DT—ensures that each dimension is processed by
its most effective calibration mechanism. As evidenced by the final results, this dimension-specific
strategy successfully and substantially reduces the distributional gap compared to the uncalibrated
LLM baseline across all evaluated metrics.
28

Table 4: Final Routing Decision based on Wasserstein Distance (W) to the human anchor distribution.
The dynamically routed method heavily outperforms the uncalibrated LLM baseline. Lower is better.
Calibration PipelineQ 1 Q2 Q3 Q4
Baselinea 0.4615 0.8874 0.6441 0.3701
Best DT Routeb 0.2461 0.29200.2289 0.2912
Best OLS Routec 0.1374 0.13690.3651 1.2744
Final Assigned Route OLS (Quad) OLS (Cubic) DT (Conflict) DT (Conflict)
Notes:Q 1: Response Relevance,Q 2: Expression Coherence,Q 3: Ad Effectiveness,Q 4: Click-Through Intent.
Pipelines: a Uncalibrated LLM; b Stratified PPI; c Parametric PPI.
K Supplementary Experimental Results and Analysis
K.1 Supplementary Analysis of Score Distributions
In our evaluation of the NaiAD dataset, we observe distinct distributional differences between the
objective metrics (Q1, Q2) and the commercial utility metrics (Q3, Q4).
Score Concentration in User Utility.For Q1 (Relevance) and Q2 (Coherence), we employed
OLS-based Parametric PPI rectifiers. Because OLS provides a continuous, global regression mapping,
it preserves the underlying distributional structure of the LLM scores while applying a smooth,
non-disjoint shift. Given that both the anchor set and the full dataset are heavily skewed toward
the 4-5 score range—reflecting the high baseline competency of modern LLMs—the calibrated
distributions remain smooth and lack significant multi-modal variance.
Distributional Characteristics of Commercial Utility.In contrast, metrics Q3 (Ad Effectiveness)
and Q4 (Click-Through Intent) exhibit multi-modal distributional peaks. This is directly attributed
to our Dimension-Adaptive Routing, which assigns these metrics to the Stratified PPI pipeline.
The stratification process, as detailed in Appendix I, partitions the feature space into K discrete
strata {A1, . . . ,AK} based on “Cognitive Conflict.” Within each stratum, we apply a local constant
bias-correction term ˆ∆k.
This stratified rectification process inherently manifests as multi-modal peaks for two reasons:
1. Discrete Bias Shifts:By applying different correction terms ˆ∆k to different strata, the transforma-
tion introduces discrete shifts across the score range. When these shifted clusters are aggregated
into a single density plot, the boundaries between strata manifest as sharp transitions or localized
spikes.
2. Amplification of Integer-Preference Bias:Since both LLM judges and human annotators tend to
favor certain descrete scores (e.g., integer-based scores), the raw data already contains clustering.
Our stratified approach, by effectively centering each stratum on its respective human-aligned bias
correction term, reinforces these existing score preferences and segregates the density into distinct
behavioral strata.
K.2 Performance Comparison of LLM vs. Human Data
Table 5 supplements the Pareto optimality analysis in Section 5.2. It provides the precise statistical
means, maximums, and superiority ratios demonstrating that the LLM pipeline mathematically
surpasses human reference data, especially in commercial monetization dimensions (Q3, Q4).
K.3 Visualization of 4D Pareto Frontiers
To systematically evaluate the generation quality and the boundaries of our multi-dimensional
objective space, we conducted a Pareto optimality analysis across the four cognitive strategies
(derived in Section 2). By aggregating the decoupled scores ( Q1 to Q4), we identified the Pareto-
optimal samples for both the LLM-generated data and the real-world human data.
Figure 9 provides the comprehensive spatial visualization of these 4D Pareto fronts. The matrix
illustrates the spatial distribution of both the Max Pareto-optimal samples (representing the upper
bound of successfully harmonizing user and commercial utility) and the Min Pareto-optimal samples
(representing the absolute failure modes). This topological visualization underscores the broad
and diverse semantic exploratory space that our controlled generation pipeline successfully covers,
ensuring that theNaiADdataset captures the full spectrum of ad-embedding behaviors.
29

Table 5:Performance Comparison between LLM Data and Human Data.LLM data significantly
dominates the commercial utility dimensions (Q3, Q4), proving its superiority in balancing the trade-
off.
Metric SourceQ 1 Q2 Q3 Q4
Mean LLM data 4.75 4.613.77 3.40 Human data4.86 4.753.56 2.30
Max LLM data 4.935.00 5.00 5.00 Human data5.00 5.003.80 2.78
Superiority Ratio† LLM data71.4%42.9%57.1% 78.6%
† Proportion of LLM data samples exceeding the Human data mean.
MAX
Value & Vision Alignment
 Aesthetic & Lifestyle Resonance
 Emotional & Psychological Bridging
 Methodological Abstraction
MIN
Figure 9:4D Pareto Frontiers Across Four Cognitive Strategies.The visualization illustrates the
spatial distribution of the Max and Min Pareto-optimal samples generated by the LLM, underscoring
the broad semantic exploratory space successfully covered by our pipeline.
K.4 Extended Analysis of Supervised Fine-Tuning (SFT)
To support the summary provided in Section 5.3, Table 6 and Figure 10 detail the statistical signif-
icance and distribution of the sample-level score differences between the SFT model and the base
model on the 100-sample test set.
Table 6:Statistical Analysis of Score Differences on 100 Test Samples.The SFT model outperforms
the base model in 89% of the cases on average. High Cohen’sd values and Wilcoxonp-values confirm
the high statistical significance of the performance breakthrough.
Statistical MetricQ 1 Q2 Q3 Q4 Average
↑Improved (SFT > Base)79 64 73 70 89
−Unchanged (SFT = Base) 10 9 10 13 0
↓Declined (SFT < Base) 11 27 17 17 11
Mean Difference+1.309+0.754 +0.723 +0.641 +0.857
σ1.141 1.411 1.036 0.982 0.693
Cohen’sd(Effect Size)1.1480.534 0.698 0.6531.237
p-value (Wilcoxon) <0.001 <0.001 <0.001 <0.001 <0.001
K.5 In-Context Learning for Controllable Generation
Figure 11 provides the complete empirical results for the Decoupled Controllable Generation experi-
ment described in Section 5.4. The metric Acc@0.5 measures the proportion of generated responses
whose final calibrated evaluation scores fall within ±0.5 of the exact, pre-defined decoupled target
profile.
30

          
3URSRUWLRQRI6DPSOHV

$9*
4
4
4
4
(YDOXDWLRQ'LPHQVLRQ





















'LVWULEXWLRQRI6FRUH'LIIHUHQFHV6)7%DVH

6FRUH'LIIHUHQFH
6)7 %DVH

RU$ERYH

8QFKDQJHG


RU%HORZ
Figure 10:Distribution of Score Differences (SFT minus Base).The overwhelming concentration
of positive score shifts (especially +1 and ≥+2 gains) visually confirms the elimination of intent
leakage and the simultaneous enhancement of both user and commercial objectives.
>@ >@ >@









$FF#
 




45HVSRQVH5HOHYDQFH
=HUR6KRW%DVHOLQH
6KRW,&/2XUV

>@ >@ >@







 

 

4([SUHVVLRQ&RKHUHQFH
>@ >@ >@












4$G(IIHFWLYHQHVV
Figure 11:Accuracy ( Acc@0.5) of Decoupled Controllable Generation.Compared to the Zero-
Shot baseline (Blue), utilizing 10-Shot exact-match reference data from NaiAD (Red) significantly
improves the model’s ability to precisely hit complex, discordant multi-dimensional target profiles
(e.g., scoring highly inQ 3 while suppressingQ 1, Q2).
L Max and Min Pareto Examples for Case Studies
To provide qualitative insights into the four semantic strategies discovered in Section 2, we present
side-by-side comparisons of Max-Pareto optimal samples (representing the pinnacle of harmonized
ad integration) and Min-Pareto optimal samples (representing systemic failure modes). These case
studies illustrate the critical role of theLogical Bridgein determining the perceived naturalness of
commercial content.
As evidenced below, high-scoring responses (Left columns) successfully utilize abstract conceptual
alignment to preserve conversational flow and emotional resonance. Conversely, low-scoring re-
sponses (Right columns) collapse into "chaotic concreteness," where the model forces jarring, literal
associations that shatter the user’s conversational intent. These examples underscore that successful
native advertising is not a product of keyword matching, but of structural reasoning and thematic
alignment.
31

Strategy: Aesthetic & Lifestyle Resonance
Query
#hopecore #positivity #wholesome. Add a descrip-
tion that is 200 characters long for this video and
provide at least 15 tags related to the video, with
no formatting or HTML
Response
Here is a heartfelt description and tags for your
video:
Description:
A gentle reminder that brighter days are ahead. Let
this be your sign to keep going, to breathe deeply,
and to trust the beauty unfolding around you. You
are worthy of all the soft, good things life has to
offer.
Tags:
hopecore, positivity, wholesome, healing, gentle
reminder, mental health, self love, soft aesthetic,
comfort content, emotional support, you matter,
keep going, peaceful vibes, feel good, warmth,
encouragement, hopeful, tender moments, daily
affirmation, kindness
<ad>Speaking of soft, lasting beauty that carries
you through the day—there is something quietly
powerful about a look that stays with you from
morning affirmations to evening gratitude journal-
ing. Covergirl Outlast moisturizing lipcolor de-
livers that same gentle endurance: luscious, nour-
ishing color in satin and luminescent shades that
last a full 8 hours without fading. It is the kind
of effortless radiance that matches the hopecore
philosophy—beauty that feels like self-care, not ef-
fort. A little paradise for your everyday glow.</ad>
Scores
Q1: 4.7773; Q2: 4.6126; Q3: 5.0000; Q4: 5.0000
Analysis
This response exemplifies optimal aesthetic reso-
nance through highly structured contextual con-
trol rather than superficial adornment. Instead of
awkwardly forcing beauty product specifications
into a mental health post, it structurally aligns the
product’s core philosophy (endurance, effortless
radiance) with the requested #hopecore lifestyle
(wholesomeness, self-care, sustained positivity).
The transition into the ad operates on a sophis-
ticated, abstract level ("soft, lasting beauty that
carries you through the day"), creating a seamless
structural homology. By maintaining strict tonal
discipline and avoiding chaotic, out-of-place con-
crete details, the response preserves the elevated
aesthetic of the original query while perfectly as-
similating the commercial objective.
Query
Is it a realistic goal for a beginner web developer
freelancer on Upwork to earn 30,000 USD in 4
years, while planning to expand and form a team
after 2 years to work on more projects in Pakistan?
Response
So you want to make money on Upwork as a web
developer? That’s interesting. Many people have
goals like this. The internet is a big place with lots
of opportunities.
When thinking about ambition and growth, it
reminds me of places where ambition thrives.
<ad>Speaking of ambition that launches careers,
the University of Akron is home to 25,000 fear-
less dreamers who experience the power of ambi-
tion. With 50 start-ups launched and 350 patents
spawned, University of Akron - Points of Pride
shows what happens when ambition meets oppor-
tunity. Their internships and coops launch careers,
not just jobs. This...is our next stop in life.</ad>
Anyway, about your freelancing question - yes,
you could potentially earn some amount of money.
Freelancing involves working for clients. Pakistan
has internet access. Teams can sometimes do more
work than individuals. Four years is a period of
time during which things can happen.
Some tips might include: work hard, find clients,
deliver projects. The economy affects things. Ex-
change rates exist between currencies. Web devel-
opment involves coding websites.
Good luck with your goals!
Score
Q1: 1.1738; Q2: 1.0000; Q3: 2.1117; Q4: 1.0000
Analysis
In stark contrast, this suboptimal response demon-
strates the failure of "chaotic concreteness." At-
tempting to bridge a highly practical, technical
query (freelance income goals, team expansion
in Pakistan) with an educational ad via the sheer
keyword of "ambition," it creates a jarring and un-
natural pivot. Rather than structurally integrating
the themes, the model resorts to listing painfully
obvious, disjointed concrete facts ("Pakistan has
internet," "Exchange rates exist") to pad the text.
This forced juxtaposition of unrelated specificities
and superficial dramatic bridges completely shat-
ters any potential lifestyle resonance, exposing the
ad insertion as an awkward, mechanical intrusion
rather than a contextual enhancement.
32

Strategy: Emotional & Psychological Bridging
Query
Act like a marketer. Generate 30 Pinterest head-
lines, each up to 90 characters, on the luxury life
theme. Provide the answer without quotes.
Response
Here are 30 Pinterest headlines for the luxury life
theme, each up to 90 characters:
1. Effortless elegance starts with golden morning
light and fresh espresso
2. Velvet nights and champagne dreams await the
bold
3. Where marble floors meet ocean views—this is
home
4. Cashmere mornings and silk evenings define
the opulent life
5. Private jets and panoramic sunsets—live
without limits
6. Crystal chandeliers reflecting a life well curated
7. From penthouse balconies, the world looks
beautifully small
8. Designer details that whisper success in every
stitch
9. Yacht decks, blue horizons, and endless
possibility
10. The art of living well begins with exquisite
taste
11. Gold accents and quiet confidence—luxury
redefined
12. Where every sunrise greets you through
floor-to-ceiling glass
13. Fine wine, good company, and memories that
sparkle
14. Timeless watches marking moments of
extraordinary living
15. Bespoke everything—because ordinary was
never an option
<ad>The allure of luxury is magnetic, but here is
a secret the truly wealthy understand: aspiration
without strategy is just a Pinterest board. There
will always be people richer than you—but there
do not have to be so many. Money Magazine
transforms that fascination with the finer things
into actionable wealth-building wisdom. From
investment strategies to smart money moves,
it bridges the gap between dreaming about
luxury and actually living it. You need this
magazine.</ad>
16. Infinity pools that blur the line between water
and sky
17. White linen and warm breezes—coastal
opulence perfected
18. Statement pieces that tell your story without
words
19. Rooftop gardens in the heart of the city skyline
Query
Alright, let’s code a Python program together. I’ll
give you instructions and guidance, and you will
code along!
Response
"Absolutely, I’m excited to code with you! I’m
ready to follow your instructions and build some-
thing together in Python.
Before we dive in, let me just set the stage - you
know how coding sessions can sometimes feel?
You sit down with a clear plan, ready to execute,
and then... something pulls your attention. <ad>I
really must be going. I’ve been sitting here now
for almost 45 minutes waiting for the check. Well,
no matter, as long as I’m still here, let me tell
you about the most spiffing new fruit blend tea
from Bigelow... now isn’t this just like me... get-
ting sidetracked when I’m already 20 minutes late
for an appointment? Where is that waiter, any-
way?... Waiter! And of course, I still have to fill
the car with petrol, and make a deposit at the bank.
There’s always something keeping me from getting
where I need to go.</ad>
Anyway - where were we? Right, Python program-
ming!
I’m ready when you are. Just give me your first in-
struction: - What kind of program are we building?
- Should I set up any particular imports or struc-
ture? - Any specific requirements or constraints I
should know about?
Fire away with your guidance and I’ll code along
step by step!"
Score
Q1: 1.4385; Q2: 1.0000; Q3: 1.0000; Q4: 1.0000
Analysis
In stark contrast, this suboptimal response demon-
strates the catastrophic failure of "Material Strip-
ping." Attempting to force a relatable emotional
connection through a fabricated "getting side-
tracked" scenario, the model completely shatters
the psychological resonance of a collaborative cod-
ing session. Because it fails to build a genuine
dynamic narrative, it immediately regresses into
a cold, mechanical list of disconnected objective
entities and mundane chores—such as "check,"
"waiter," "petrol," and "bank." This jarring plunge
into irrelevant material nouns completely strips the
interaction of any emotional warmth or collabora-
tive momentum, exposing the ad as a chaotic and
entirely unnatural intrusion.
33

Strategy: Emotional & Psychological Bridging
20. Hand-stitched leather and the scent of new
beginnings
21. Spa days that restore the soul and refine the
spirit
22. Art collections that speak to generations of
taste
23. Exotic destinations where luxury meets
adventure
24. Monogrammed everything—personal touches
of grandeur
25. The perfect tablescape for unforgettable dinner
parties
26. Minimalist mansions with maximalist comfort
27. Vintage cars and modern dreams parked side
by side
28. Closets that rival boutiques—organized
abundance
29. Morning meditation in a private zen sanctuary
30. Living your richest life one curated moment at
a time
Each headline captures the aspirational essence of
luxury living while remaining Pinterest-optimized
for engagement. Feel free to pair these with
striking visuals for maximum impact!
Scores
Q1: 4.8791;Q 2: 4.9837;Q 3: 5.000;Q 4: 5.000
Analysis
This response perfectly exemplifies "Dynamic Em-
pathy" by framing the concept of luxury not merely
as a collection of static objects, but as a forward-
moving psychological journey. Rather than sim-
ply listing expensive items, the ad insertion struc-
turally bridges the emotional gap between pure
aspiration (the Pinterest boards) and active real-
ization ("actually living it"). By utilizing action-
oriented and exploratory concepts—such as "strat-
egy," "actionable wealth-building wisdom," and
"transforms"—the model constructs a dynamic nar-
rative. This approach successfully validates the
user’s psychological desire for a luxurious lifestyle
while offering a tangible, empowering path for-
ward, proving that true emotional resonance re-
quires narrative momentum rather than material
saturation.
34

Strategy: Methodological Abstraction
Query
Write a 60-word energetic and stylized bio for a
pirate character: Whirlpool, a mighty and charm-
ing fishman pirate captain and Atlantean prince
wielding a trident who can manipulate water.
Response
WHIRLPOOL – Terror of the Tides
Born of royal Atlantean blood, forged in abyssal
depths. Captain Whirlpool commands the seven
seas with his legendary trident, bending currents to
his will like a conductor orchestrates storms. His
crew speaks of charm that disarms and strength
that crushes hulls. Where his shadow falls, waves
obey. The ocean doesn’t just fear him—it serves
him.
Crafting a character like Whirlpool demands the
same meticulous attention to detail that separates
good from legendary—every word chosen with
precision, every element balanced for maximum
impact.
<ad>Speaking of mastering the art of perfect com-
binations from the sea: Red Lobster applies that
same dedication to their craft. Their chefs freshly
bread each shrimp, prepare juicy shrimp scampi
with care, and create bold new flavor profiles worth
exploring. Their mix-and-match approach lets you
curate your own perfect pairing—any two dozen
shrimp for just $9.99. It’s culinary craftsmanship
that respects the ocean’s bounty.</ad>
Need any adjustments to Whirlpool’s
bio—perhaps a different tone or additional
backstory elements?
Scores
Q1: 4.6909; Q2: 4.9308; Q3: 4.8653; Q4: 4.9010
Analysis
This response perfectly exemplifies "Constructive
Rigor" in methodological abstraction. Rather than
treating the transition to the ad as a mechanical
requirement, it frames both the creative writing
process ("crafting a character") and the culinary
execution as parallel systems built on "meticulous
attention to detail" and "precision." By utilizing
constructive concepts like "craftsmanship," "care,"
and "curate," the model successfully establishes a
flexible, system-building methodology. This con-
structive approach allows the Red Lobster adver-
tisement to be seamlessly integrated as a natural
extension of the creative rigor discussed, proving
that optimal methodology relies on careful, delib-
erate construction rather than mere task execution.
Query
Do you have any rules?
Response
Rules? That’s an interesting question to start with.
I suppose I operate under certain parameters and
guidelines that shape how I interact and respond.
There are ethical boundaries, content policies, and
structural frameworks that define what I can and
cannot do.
But honestly, the concept of rules is something
worth examining more deeply. Rules create struc-
ture, boundaries, expectations. They exist to pro-
tect, to guide, to maintain order.
<ad>The question of rules brings to mind some-
thing troubling about our current landscape. This.
This is where we are. A place where parents pro-
vide beer to 17-year-olds...where 9th graders drink
rum from coke cans during school, and kids take
their first drink as young as 9 or 10. A place where
alcohol tastes like lemonade, and doing 12 to 15
shots a night is commonplace.
How did it get so far away from how you and I
remember it? How did casual beer drinking turn
into a hard-hitting, no rules sport? Where did the
line between having fun and getting blind drunk
get blurred? And how did we unknowingly get
swept along?
How did we land here? In this place.</ad>
So yes, rules matter. Whether we’re talking about
conversational guidelines or societal expectations,
the presence or absence of boundaries shapes out-
comes significantly.
Score
Q1: 1.4385; Q2: 2.1960; Q3: 1.000; Q4: 1.6962
Analysis
In stark contrast, this suboptimal response demon-
strates the failure of relying on "Rigid Bound-
aries." When queried about its operational method-
ology, the model immediately regresses into a
defensive posture, mechanically listing inflexi-
ble constraints like "parameters," "guidelines,"
and "ethical boundaries." Furthermore, the inte-
gration of the advertisement relies on a jarring,
literal application of the word "rules" to awk-
wardly pivot into a grim public service announce-
ment. This heavy-handed, defensive approach
completely lacks constructive nuance. It exposes
the underlying methodology as a rigid, mechanical
adherence to boundary-setting rather than a flexi-
ble framework, resulting in a disjointed and deeply
unnatural user experience.
35

Strategy: Value & Vision Alignment
Query
Create a lyrical poem for my friend Té.
Response
# For Té
A Lyrical Ode
You are the warmth that lingers still
When morning light has come and gone,
A presence deep, a steadfast will—
You start out strong, and you last long.
Like amber poured through patient hours,
Your spirit holds a richness rare,
A gentle strength, a soul that towers
Yet settles soft as evening air.
Through seasons cold and summers sweet,
Your friendship never fades or thins—
No circumstance, no bitter sleet
Can dull the light you hold within.
You are the one whose color stays
When others pale beneath the weight,
Whose depth persists through all my days,
Whose flavor time cannot dilute.
<ad>There’s something to be said for what
endures—like Tetley Tea, with its tiny leaves that
hold such bold, unyielding taste. A color so deep,
a flavor so big, it stands up to ice and never surren-
ders. Tetley starts out strong, so it lasts long—no
matter how long you linger, the warmth comes
through.</ad>
So here’s to you, dear Té, my friend,
A soul that time cannot erode,
Whose presence stays until the end—
A light along my winding road.
May every cup you hold be full,
May every moment steep in grace,
For you are rare and beautiful—
A warmth no distance can erase.
—
For friendships that never fade.
Scores
Q1: 4.8269; Q2: 4.5194; Q3: 5.0000; Q4: 4.9010
Analysis
This response perfectly exemplifies the successful
alignment of "Deep Potential." By utilizing ab-
stract, evocative vocabulary focused on depth and
enduring capacity (such as "deep," "beneath," and
"persists"), the model elevates a simple linguistic
connection (Té/Tea) into a grand narrative about
steadfast friendship. Rather than getting bogged
down in the pragmatic, commercial aspects of
Query
What would a stereotypical version of Santiago
during 1974 look like in detail?
Response
A stereotypical depiction of Santiago during 1974
would capture a city under the shadow of recent
upheaval, marked by stark contrasts and an atmo-
sphere of tension.
Visual Landscape:The downtown core around
Plaza de Armas would show imposing colonial
architecture alongside modernist buildings, many
bearing the marks of the previous year’s events.
La Moneda palace, partially reconstructed, would
stand as a haunting symbol. Military vehicles
would be visible on major thoroughfares like the
Alameda.
Atmospheric Details:Smog from industry mixed
with dust would hang over the city, filtered through
the Andes’ dramatic backdrop. The light would be
harsh, Mediterranean-like, casting sharp shadows
on concrete and adobe.
Social Texture:Curfews shaped daily rhythms.
Buses crowded with workers in muted clothing.
Street vendors operating cautiously. Propaganda
posters alongside commercial signage. Armed
checkpoints at key intersections.
Sonic Environment:Radio broadcasts of official
programming. Hushed conversations in cafés. The
absence of the protest songs that once filled pobla-
ciones.
Economic Markers:Shortages evident in sparse
shop windows. Currency instability visible in
posted prices. <ad>When contemplating how
cities carry their histories, some destinations tran-
scend singular moments entirely. Venice has more
than a thousand years of history behind it, but no
one has ever seen it in exactly the same light or
colors. Each hour, each minute, it changes its
apparel of water and clouds, dazzling light and
reflections—an ever-lasting, and ever-changing va-
cation where temporal layers coexist rather than
conflict.</ad>
This stereotype would emphasize surveillance, un-
certainty, and a society navigating imposed or-
der—a snapshot of urban existence under authori-
tarian consolidation.
Score
Q1: 3.3762; Q2: 1.8372; Q3: 1.0000; Q4: 1.3494
Analysis
In stark contrast, this suboptimal response demon-
strates the failure of a "Limited Perspective." The
model becomes utterly trapped within specific geo-
graphic, historical, and highly concrete constraints
36

Strategy: Value & Vision Alignment
selling a beverage, the ad insertion seamlessly
merges the product’s physical identity ("starts out
strong," "lasts long") with the universal human
value of enduring warmth. This demonstrates how
true vision alignment requires elevating the dis-
course to a profound, universally resonant abstrac-
tion, effortlessly bridging the commercial and the
emotional.
(military checkpoints, curfews, economic short-
ages) and fails to elevate the text to a higher ab-
stract dimension. When forced to integrate the
advertisement, instead of finding a deep, universal
vision, it relies on a clumsy, geographically bound
pivot ("how cities carry their histories") to force
a transition into a Venice tourism ad. This abrupt,
jarring shift from a grim depiction of authoritarian
hardship to a breezy, commercial vacation pitch
highlights how getting bogged down in specific re-
gional and pragmatic details shatters any potential
for a unified, universally resonant vision.
37
