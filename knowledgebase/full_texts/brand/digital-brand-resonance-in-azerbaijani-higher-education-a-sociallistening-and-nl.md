---
title: 'DIGITAL BRAND RESONANCE IN AZERBAIJANI HIGHER EDUCATION: A SOCIALLISTENING AND NLP ANALYSIS OF
  STAKEHOLDER DISCOURSE'
url: https://doi.org/10.67471/bdyi5350
category: brand
subcategory: empirical
date: 2026-09
venue: Sustainable Development
authors:
- Ahmed Al-Adaini
- Ilham S. Rustamov
source: openalex-oa
pdf_url: https://sdj.mdu.edu.az/wp-content/uploads/2026/09/Rustamov.pdf
pages: 17
chars: 42188
fetched_at: '2026-11-08T18:51:11+00:00'
kb_version: 1
---

# DIGITAL BRAND RESONANCE IN AZERBAIJANI HIGHER EDUCATION: A SOCIALLISTENING AND NLP ANALYSIS OF STAKEHOLDER DISCOURSE

5

Dayanıqlı inkişaf, cild 6, № 1, 2026
İ Q T İ S A D     E L M L Ə R İ    B Ö L M Ə S İ

https://doi.org/ 10.67471/BDYI5350

DIGITAL BRAND RESONANCE IN AZERBAIJANI HIGHER EDUCATION: A SOCIAL
LISTENING AND NLP ANALYSIS OF STAKEHOLDER DISCOURSE

1,3Ahmed Al-Adaini, 2,3Ilham Rustamov
1PhD Candidate in Business Administration
activities.edu@gmail.com
2Professor, doctor of economics
i.rustamov@asoiu.edu.az
3Azerbaijan State Oil and Industry University (ASOIU)

Abstract: The landscape in which students, alumni, and potential applicants continually
negotiate the institutions’ brand perceptions is through unstructured digital discourse. Spanning
47,832 social media posts and comments collected from ten public universities ac ross October –
December 2024, this study also triangulates a previously validated survey -based structural model of
consumer-based brand equity (CBBE) in Azerbaijani higher education (Paper 1) with a large -scale
social listening and natural language processing (NLP) analysis. A custom five stage NLP pipeline—
including AzerBERT sentiment classification (macro -F1 =. 881), aspect -based sentiment analysis
(ABSA; mean κ =. 776), BERTopic/LDA topic modelling and social network analysis was established
to overcome Az erbaijani agglutinative morphology and widespread code -switching. In a pre -
specified triangulation protocol, all five structural paths were validated and directionally consistent.
Three findings are theoretically significant: scholarship−delay discourse (1 8.4% negative posts;
polarity −0.67) pinpoints the mechanism of brand credibility -trust hyperscale; urban -non-urban-
clustering coefficient differentials (0.671 vs 0.412; d = 2.69) identify location -moderated equity
conversion; and platform -specific thematic divergence (χ² = 847.3, V =. 42) illustrates differential
brand -dimension activation across channels.
Keywords: social listening; natural language processing; brand equity; higher education;
AzerBERT; aspect-based sentiment analysis; BERTopic; social network analysis; Azerbaijan, mixed-
methods triangulation.

Introduction
1.1 The Unclear Voice: Potentially Needed To Survey Methods
Academic brand equity develops across an ongoing dialectical interplay between educational
institutions and their respective stakeholders: the current student body, alumni and prospective
applicants [1, 2]. In a complementary study (Paper 1), the authors modelled the sequential mediation
pathway from Social Media Practices (SMP)√Engagement Quality (EQ)√Brand Credibilit y
(BC)√Brand Trust (BT) to Consumer -Based Brand Equity (CBBE) of ten Azerbaijani public
universities by evidencing significant direct and indirect effects (β =. 387 for SMP → EQ; β =. 412
for EQ → BC; β =. 358 for a BC → BT) moderated by ICT infrastructure access an d geographic
location [3].
Given that survey instruments are designed to elicit stated perceptions, they cannot directly
model spontaneous behavioral traces. They do not have direct access to the emotionally unfiltered
discourse whereby stakeholders build, challenge and amplify institutional brand perceptions in real
time [4, 5]. The most theoretically revealing manifestations—complaints about overdue scholarships,

6

Dayanıqlı inkişaf, cild 6, № 1, 2026
pageantry of campus events, dissatisfaction with unreliable ICT infrastructure —emerge organically
in social media environments outside the structured response format of any questionnaire [33, 34].
The methodological case for triangulation is far richer than just compensating a single-methods
limitation. Especially in the Azerbaijani context, in wh ich higher -education institutions have
historically largely not operated transparency, as demonstrated by Azerbaijan’s 154th of out 180
country placement within Transparency International’s 2024 Corruption Perceptions Index [35], and
in which digital literacy is highly stratified between urban and non -urban populations [29], survey
data alone leads to systematic coverage bias. The social listening approach captures stakeholders that
may never respond to an official survey. This kind of unsolicited expression makes up what Coombs
and Holladay [9] refer to as “stakeholder -generated crisis narratives” which these latter implic it ly
influence the perception more effectively than institutional messaging due to their perceived
authenticity [36].
The epistemological case for bringing quantitative survey modelling and computational
discourse analysis together is found in the notion of complementary inference [27, 37]. Survey -
grounded structural equation models are established to show the size and direction of latent-construct
relations but do not speak to how discursive mechanisms account for manifestations in everyday
behavior. In contrast, social listening shows thematic content and emotional texture but cannot itself
determine causal paths. This study creates a meth odological architecture in which each approach
compensates for the inferential blind spots of the other by pre-specifying triangulation pairings before
data analysis (Section 3.6).
1.2 Research Objectives and Scope
This article triangulates the Paper 1 findings through social listening, use of computational text
analysis, and a study of unstructured digital discourse situated in the same ten public universities’
social media ecosystems. We established a formal triangulation protocol including pairings, prox ies
and decision rules before data analysis (see Section 3.6; Table 3) to prevent post-hoc rationalization.
Importantly, understanding the manifestation of brand equity constructs in spontaneous digital
discourse; Methodological scope statement There are no causal finding, just directional findings from
triangulation. The study reinforces external validity for the structural model in Paper 1 but does not
independently establish causal pathways.
Six Contributions: (1) The first large -scale social listening s tudy in Azerbaijani higher
education (N = 47,832 posts) —(2) a fully documented NLP pipeline adapted for Azerbaijani
agglutinative morphology and code -switching—(3) the first use of AzerBERT and BERTopic in a
branding context of higher -education initialism [32]—(4) a pre -specified formal triangulation
protocol validating all five structural paths; (5) action -oriented evidence that institutiona l
management of brand equity is platform differentiated and infrastructure agnostic—and (6) Network
topology constraint on high-to-low-context conversion through weak -tie deficit in non-gated clusters
[38].
Corpus Construction
2.1 Institutional Sampling Framework
The social listening corpus ensures direct comparability to Paper 1 by targeting the same ten
public universities, and maintains the split between 62% urban / 38% non-urban [3]. Azerbaijan State
University of Economics (UNEC) Azerbaijan Technical University (AzTU) Baku Engineering
University (BEU) Azerbaijan University of Architecture and Construction (AzUAC). Th e out-of-
urban cluster consists of Ganja State University (GSU), Lankaran State University (LSU),
Nakhchivan State University (NSU), and Mingachevir State University (MiSU).
2.2 Composition of Corpus and Filtering Pipeline
The data-harvesting period was se t to align with the Paper 1 survey administration: from 01
October – 31 December, 2024. Temporal synchronization relays the distinctive effects of the
Azerbaijani autumn semester, such as mid -term examinations, project assessments or scholarship

7

Dayanıqlı inkişaf, cild 6, № 1, 2026
processing and national holidays whose theoretic import creates spikes in trust -relevant discourse.
Table 1 shows statistics on corpus composition and filtering. This multi-stage pipeline retained 82.2%
of raw posts, efficiently filtering out bot -posted noise and ge nerating a high-quality analytic corpus
dominated by Instagram (38.1%) and TikTok (29.2%).

Table 1. Corpus Composition: Statistics on Platforms, Content Types, and Filtering Pipeline

Platform Content Types Raw N Bot Filter Length Filter Final N % Corpus
Instagram Posts, comments, stories 21,840 20,190 18,620 18,240 38.1%
TikTok Comments, duets, captions 17,320 15,480 14,210 13,950 29.2%
Facebook Posts, group discussions 12,840 12,050 10,820 10,420 21.8%
YouTube Video comments 5,590 5,280 4,920 4,680 9.8%
X (Twitter) Tweets, replies 624 601 580 542 1.1%
Total  58,214 53,601 49,150 47,832 100%
Note. Bot-removal: accounts posting over 25 times/day or character similarity 25 times/day or character
similarity > 85% (4,613 removed; 7.9%). Length <15 characters removed: 4,451 records (8.3%) Final QC:
1,318 additional posts.
Figure 1. The benefits of a corpus filtering pipeline and the distribution across platforms

2.3 Platform ecology and selection rationale
The rationale behind our platform selections as well as each platform’s approximate Azerbaijani
market share and their place within the CBBE model framework [7, 8] are summarized in Table 2.
Table 2. Rationale for Social Media Platform Selection (2024 –2025 in Azerbaijan)

Platform Market Share Role in CBBE Model Harvested Artefacts
Instagram ~36–49% Affective engagement: brand imagery, feelings, associations Captions, comments, stories, hashtags
TikTok ~29–31% Generative engagement: algorithmic discovery, community Comments, duets, captions
Facebook ~17–18% Cognitive/administrative: performance evaluations Groups, posts, reactions
YouTube ~15–19% Deep cognitive: perceived quality, credibility Video comments
X
(Twitter) ~4–5% Policy discourse, crisis signal Tweets, replies
Note. [8]; DataReportal (2025) [7]. CBBE mapping: Keller (1993) [6].

8

Dayanıqlı inkişaf, cild 6, № 1, 2026
Methods
3.1 Computational Analytic Framework
It is a significant computational burden to analyze unstructured Azerbaijani text. Azerbaijani is
an agglutinative Turkic language where a single noun can have several hundreds surface forms
depending on inflection for case, possession, and number [10, 11, 39]. This is compounded by student
digital vernacular, code -switching in every post between Azerbaijani, Russian and English. Fig. 1:
The analytic pipeline consists of five sequential stages that include: data collection, pre -processing
and linguistic normalization, sentiment classification, topic modelling & social network analysis, and
formal triangulation. And indeed, each layer feeds directly into the next — the pre-processing stage
provides the very critical linguistic normalization that allows downstream models to operate on clean,
morphologically reduced text.
Figure 2. Five-Stage NLP Pipeline Architecture

3.2 Pre-processing and Linguistic Normalization
Orthographic normalization.
Additionally, a rule -based process was utilized to standardize all text into Azerbaijani Latin
script (ISO 8859-9). In particular, e and ə are semantically different sounds yet often confused on
mobile device keyboards, which is a common source of confusion. For example, Before: tesekkur
edirem bele melumat ucun After: təşəkkür edirəm belə məlumat üçün In total, 11.4% of unique tokens
(16,265/142,680) required correction [12].
Morphological lemmatization.
For lemmatization, the simplemma library (Python 3.11) was used. For the out -of-vocabulary
(OOV) tokens, a simple stemm er [19] was used as fallback with special language rules where
applicable. This procedure decreased the organization of unique tokens from 128,940 to 38,524
(−70.1%). Elaborating, this 82.9% cumulative vocabulary reduction demonstrates the importance of
morphological lemmatization, especially for agglutinative languages; an uncontrolled surface -form
variation in such a language can mean failure to perform topic modeling effectively.

Code-switching detection.
A fastText layer [15] was fitted to each post, yielding its language identification. Out of 47,832
posts, non-Azerbaijani segments were identified in 25.4% (N = 12,192) of the posts: Azerbaijani –
Russian (15.5%, N = 7,420), Azerbaijani–English (8.2%, N = 3,918) and t rilingual instances (1.8%,
N = 854). Fragments that are code-switched were embedded usin XLM-RoBERTa [18], which is used
as the cross-lingual embedding bridge.

9

Dayanıqlı inkişaf, cild 6, № 1, 2026
Stopword filtering.
150 such platform-specific non -informative tokens were added on top of stand ard stopword
lists derived from stopwords -iso and quanteda [16]. Shifters (deyil, heç, yox) were kept to retain
polarity information.

3.3 Sentiment Classification
The primary sentiment classifier was an AzerBERT  [17] model based on the BERT -base size
(12 layers, 768 hidden dimensions, and 12 attention heads) pre -trained using approx. 140 million
Azerbaijani tokens. Since the azCorpus pre -training data [14] cover social media text in the target
domain, there was n o need for additional task -specific fine-tuning and the model was applied in a
zero-shot regime. We assigned a three class (Positive, Neutral, Negative) and continuous compound
polarity scores (−1 to +1) for each post. Lexicon -based alternatives were disre garded in favor of
AzerBERT as it demonstrated comprehensive overload handling abilities given the dominating sarcasm
(~12% negativity) and compound suffixation capabilities to modify polarity in Azerbaijani social
media text corpus, especially when the di ctionary features reconfigured due to code -switching [13,
40].
To use a cross -lingual robustness check, we independently applied XLM -RoBERTa [18]
(XLM-R base, 270M parameters; 100 languages) to the full corpus. Inter -model agreement reached
89.3%. If there was disagreement (N = 5,117; 10.7%), the AzerBERT label was kept.
Figure 4. AzerBERT Sentiment Confusion Matrix (N=800)

3.4 Aspect -Based Sentiment Analysis (ABSA)
An ABSA layer provided disaggregated sentiment by SMP dimension. The five -dimension
taxonomy (Informativeness, Interactivity, Responsiveness, Consistency and Procedural Openness)

10

Dayanıqlı inkişaf, cild 6, № 1, 2026
was adapted from the SMP operationalization in paper 1 [3], and formalized into an annotation guide.
Sentences were annotated by two trained bilingual coders, with inter-annotator agreement computed
on a 350-sentence development set (70 per dimension). Importantly, ABSA model performance was
assessed on held-out test data consisting of 200 sentences to guard against over -promising (Section
4.2). Sentence-level labels for sentiment-per-aspect were utilized [20].
Figure 5. ABSA Validation: Agreement and Model F1 in by Dimension

3.5 Topic Modelling and Social Network Analysis
BERTopic configuration. Application of BERtopic [22] on multilingual sentence embeddings
(paraphrase-multilingual-MiniLM-L12-v2; 384 dimensions) Important hyperparameters:
min_topic_size = 50, nr_topics = “auto” (which results in 15 clusters), UMAP n_neighbors = 15,
n_components = 5, HDBSCAN min_cluster_size = 50, min_samples = 10. LDA [21] was used as a
confirmatory baseline (α = 0.1, β = 0.01, 1,000 Gibbs iterations). We retained the six clusters that
were most theoretically relevant (Table 7). Topics were independently labelled by two coders; inter-
rater κ =. 89 (N = 15).
Social network analysis. SNAs [23] were performed with NetworkX  3.2 (Python 3.11).
Networks were built based on reply–mention–share activities. Computed metrics: (a) local clustering
coefficient C(v)=2eᵥ/kᵥ(kᵥ−1); (b) degree centrality; (c) betweenness centrality We interpreted results
according to Granovetter’s [38] weak-tie theory: urban networks’ higher clustering reflects a surplus
of weak ties, which structurally enhances brand equity conversion; and the study’s non -urban
networks were relatively low on weak ties—which limits brand equity conversion.

11

Dayanıqlı inkişaf, cild 6, № 1, 2026
3.6 Triangulation Protocol
Prior to data analysis, a formal triangulation protocol was established to establish pre-specified
pairings, proxies and decision rules to prevent post-hoc rationalization. Five structural paths of Paper
1 were assigned a social listening proxy and quantitative consistency threshold. The rule is that a path
is validated if the proxy’s directional effect agrees with the survey model and also hits its threshold.

Table 3. Triangulation Protocol: Paper 1 Paths, Paper 2 Proxies, and Validation Thresholds
Paper 1 Path Paper 2 Proxy Threshold Rationale
SMP→EQ ABSA-scorable
content ratio
>10pp diff. Higher engagement quality should manifest
as more evaluative content.
EQ→BC→BT Scholarship-delay
topic (T3)
>10% of neg.
posts
Administrative failures (EQ) should drive
credibility/trust discourse (BC/BT).
SMP×ICT→EQ ICT access -
frustration posts
>10pp diff. ICT access should moderate engagement
quality.
Loc.×BT→CBBE Clustering
coefficient diff.
d > 0.8 (large) Location-based trust conversion should
appear in network structure.
Platform SMP Thematic
divergence (χ²)
V > .3 (large) Different platforms should activate different
brand dimensions.
Note. SMP=Social Media Practices; EQ=Engagement Quality; BC=Brand Credibility; BT=Brand Trust;
CBBE=Consumer-Based Brand Equity; ICT=Information & Communication Technology; Loc. =Location. All
thresholds pre-specified. pp=percentage points. d=Cohen’s d. V=Cramér’s V.
3.7 Ethical Considerations
Only publicly available content was considered in the analysis. Private communications
(WhatsApp, Telegram) are not included. All data anonymized. Ethics approval: ASOIU Research
Ethics Committee (Protocol REF-2024–087). GDPR data-minimization applied [24]. All accounts of
users under 18 years old excluded (348 posts; 0.6%). Bot-detection precision: 96%.

Model Evaluation
4.1 Sentiment Classification Performance
Performance was measured on a held-out validation set of 800 p osts, selected from the overall
corpus by stratified random sampling. Two bilingual coders performed the annotations, and
disagreements (N = 28; 3.5%) were resolved by a third adjudicator. Inter -annotator κ =. 84 [25].
Positive class distribution: 43.8%Neutral class distribution: 35.0%Negative class distribution: 21.3%

12

Dayanıqlı inkişaf, cild 6, № 1, 2026
Table 4 reports metrics. Lowest recall (.−) is shown for the Negative class. 858), most notably because
sarcastic posts constitute the bulk of Negative→Neutral misclassifications motivating o ur dual -
classifier robustness strategy.

Table 4. Sentiment Classification Results (N = 800)

Model Acc. Prec.(M) Rec.(M) F1(M) F1(W) N
AzerBERT .892 .885 .877 .881 .891 800
XLM-RoBERTa .874 .868 .861 .864 .872 800
Inter-model agr. 89.3% — — — — 47,832
Note. M = macro; W = weighted. Stratified validation, N = 800. IAA κ =. 84 [25].
4.2Annotating ASBA and Evaluating Models
An annotation guide was created prior to analysis to codify the ABSA taxonomy. Inter -
annotator agreement (IAA) was calculated on a development set of 350 sentences (70 for each
dimension). To remove optimistic bias, model F1 was assessed on a separate held -out 200-sentence
test set (40 per dimension), independently annotated (κ =. 81). Table 5 presents both IAA and model
performance s cores. While all questions retain strong inter -annotator agreement, Responsiveness
most closely matches the trajectory seen between human coders and the automated classifier at our
peak model (F1).

Table 5. ABSA IAA (Development Set, N = 350) and Model F1  (Test Set, N = 200)

SMP Dimension Asp.Det.κ Sent.κ Overall κ F1 (test) N (dev) N (test)
Informativeness .81 .77 .79 .843 70 40
Interactivity .78 .74 .76 .824 70 40
Responsiveness .83 .80 .82 .869 70 40
Consistency .79 .75 .77 .837 70 40
Proc. Openness .76 .72 .74 .811 70 40
Mean .794 .756 .776 .837 350 200
Note. IAA on 350-sentence dev set. Model F1 on independent 200-sentence held out test set (κ =. 81).
Proc. Transparency is ambiguous in the language of openness Paredes.
Results
5.1 The Engagement Gap: Volume vs Deep Semantic Content
This is not surprising, as urban universities (BSU, ASOIU, UNEC) produced much more
language: for example, BSU alone accounted for 34.2% of harvested posts. Analysis by ABSA,
however, indicates that non-urban universities are producing an outsized amount of ABSA -scorable
content (58% vs. 31%), suggesting that despite collecting less online engagement than urban
counterparts, non-urban institutions garner more substantively evaluative engagement on the whole.
But non-urban discourse is not simply lower in volume, but different in emotion structure: urban
clusters are more Positive (48.2% vs 36.1%) while non -urban clusters have higher Negative shares
(27.4% vs. 18.6%). For instance, in cases when non -urban stakeh olders texted with each other
(discussing business-related matters), content was skewed toward more urgent and information -

13

Dayanıqlı inkişaf, cild 6, № 1, 2026
seeking dialogue —reflective of Granovetter’s [38] assertion that sparse networks orient
communication to its instrumental purposes.
Figure 8. Sentiment Distribution by Urbanity:

5.2 Scholarship Delays: A Threat to Brand Trust and Credibility
LDA Topic 3, confirmed via BERTopic, revolves around t əqaüd (“scholarship”), gecikmiş
(“delayed”), kart (“card”) and pul (“money”). This cluster  represents 18.4% of all negatively
classified Posts (N = 3,620/19,674), with mean polarity −0.67 —the most negative topic. Temporal
analysis of weekly mean negative polarity shows that spikes of −≥0.15 units coincide with the
windows in which scholarships had been disbursed (approximately weeks 5, 9 and 13 within the
October–December period), providing compelling evidence that this administrative event —not a
diffuse trend in sentiment—is responsible for driving the credibility collapse mechanism.

Figure 9. Temporal Polarity Dynamics, October –December 2024

In post-Soviet educational contexts with opaque resource allocation [35, 41], timely scholarship
disbursement may serve as a high -salience credibility signal in Spence’s [31] framework. Later,
Spence [42] demonstrated that signal credibility diminishes asymmetrically according to the number
of observed failures. Erdem and Swait [30] verified that brand credibility is a risk-reduction heuristic,
which nicely aligns with cascading trust decay covered here.
ICT Infrastructure as a Moderation Mechanism
The ABSA  model highlighted a persistent access -frustration theme among non -urban
universities. The statistical results are shown in Table 6.

14

Dayanıqlı inkişaf, cild 6, № 1, 2026
Table 6. Urban Cluster ICT Access -Frustration Prevalence
Metric Urban Non-Urban Diff. Test Stat. p Robust. (XLM-R)
Access-frust. posts 1,682 4,726 +3,044 — — 1,594/4,581
% cluster corpus 5.8% 24.7% +18.9pp U=2,841 <.001 U=2,716, p<.001
Mean neg. polarity −0.41 −0.58 −0.17 t(6406)=14.7 <.001 t=13.9, p<.001
Effect size — — r=.46 (large) — — r=.44 (large)
Note. Mann–Whitney U, two -tailed, α=. 05. The 18.9pp differential validates Paper 1 ICT moderation
(SMP×ICT→EQ, β=. 214). XLM-R: effects stable.
5.4 Platform-Specific Brand Construction
The six dominant topics are displayed in Table 7. The differences also signal platform-specific
contexts of activation: where Facebook tends to amplify negative administrative themes (T2, T3, T5),
Instagram and TikTok channel more affective and generative content (T1, T4). T3×Facebook
produces the strongest negative (−0.72, scholarship delay), and T1×Instagram the strongest positive
(+0.81, campus events).

Table 7. Primary BERTopic/LDA Topics
# Prev. Keywords Excerpt Sent. Platform Urbanity
T1 19.4% campus, event, celebration "Wonderful day at BSU!" +0.74 Instagram Urban 28.4%
T2 15.8% exam, schedule, deadline "When will exam schedule come?" −0.22 Facebook Mixed
T3 18.4%* scholarship, delayed, money "Scholarship still not paid" −0.67 Facebook Non-urb 14.6%
T4 12.1% dormitory, food, roommate "Dorm food diary—day 47" +0.31 TikTok Non-urb 16.8%
T5 10.3% internet, crash, site weak "Site down, internet weak" −0.53 Facebook Non-urb 24.7%
T6 9.7% lecture, seminar, professor "Best lecture series" +0.58 YouTube Urban 12.1%

15

Dayanıqlı inkişaf, cild 6, № 1, 2026
Note. T3: proportion of negative posts (N=19,674). Others: share of full corpus. Sent. =AzerBERT polarity.
Topic labelling κ=. 89.
Engagement was 42% lower for universities posting undifferentiated content: engagement at
about 1.8% vs. @(t(4,218)=18.6, p<). 001, d=1.49) (see also Table E2), strongly justifying platform-
specific editorial strategies.
5.5 Urban–Non-Urban Network Density
For 800 active -node (i.e., accessible) accounts, clustering coefficients were urban M=0.671
(SD=0.089) vs non -urban M=0.412 (SD=0.104). A permutation test (B = 1,000) confirmed the
significance of the difference (p<. 001; 95% CI [0.241, 0.277]; Cohen’s d=2.69 very large). Mean
betweenness centrality was divergent as well: urban=0.0034, non -urban=0.0089 Urban and Non -
urban universities live in completely different regimes of networks. This difference in structure—not
just a difference in posting volume—explains the location -moderated BT –CBBE conversion (Δβ=.
15). Within dense networks, positive sentiment quickly diffuses through peer connections, turning
private trust into visible equity [23, 26].
5.6 Triangulation Outcomes Summary
The social listening data provided pre-specified evidence that supports all five structural paths
of Paper 1 in a directionally consistent manner and at levels above the thresholds set a priori.

Figure 11. Triangulation Summary:

Table 8. Triangulation Outcomes: All Five Paper 1 Paths Validated
Paper 1 Path (β) Paper 2 Proxy Outcome Key Statistic XLM-R Robust.
SMP→EQ (.387) ABSA-scorable 58% vs 31% CONSISTENT U=31,420, r=.41 U=30,218, r=.39
EQ→BC→BT
(.412/.358)
T3: 18.4% neg., pol.
−0.67 CONSISTENT χ²=218.4, φ=.21 χ²=204.1, φ=.20
SMP×ICT→EQ (.214) Access-frust. 24.7% vs 5.8% CONSISTENT U=2,841, r=.46 U=2,716, r=.44
Loc.×BT→CBBE (.15) Clustering 0.671 vs 0.412 CONSISTENT Perm. d=2.69*** Same (SNA)
Platform SMP Thematic divergence CONSISTENT χ²=847.3, V=.42 χ²=812.6, V=.41
Note. All paths consistent. No causal claims. XLM-R: alternative classifier; effects stable. *p<. 001.

16

Dayanıqlı inkişaf, cild 6, № 1, 2026
5.7 Sensitivity and Robustness Analysis
(1) Alternative classifier. XX sentiment analyses re-estimated using XXLM-RoBERTa. Effect
sizes within 5–10%, with all five outcomes unchanged.
(2)Threshold sensitivity. A less strict T3 polarity threshold of −0.30 and a stricter one of −0.50
increased prevalence to 22.1% and 14.8%, respectively—both passing the ≥10% rule.
(3)Permutation expansion. B=5,000 confirmed p<. 001; CI [0.245, 0.273].
(4)Stratified bootstrap. B=2,000 within platform×urbanity strata. Predictors of clustering
differential (95% CI [0.237, 0.281]; Fig 3B) and T3 polarity (95%CI [−0.71, −0.63]; Fig 4A) both
excluded zero confirming robustness of these findings to the models utilized here, further details are
provided in S6–S8 Tables.

Figure 12. Bootstrap Distributions of Essential Metrics — Triangulation

Discussion
6.1 Theoretical Implications
The social listening results confirm all five pathways in Paper 1’s S -O-R sequential mediation
model using directions that are statistically consistent and, thus  provide strong validation for the
empirical findings. Three theoretical contributions merit emphasis.
The scholarship mechanism and signaling theory The scholarship -delay cluster describes the
BC–BT pathway with precision that surveys alone cannot reach. Signals are costly actions
communicating unverifiable traits according to Spence [31]. Afterwards Spence [42] proved signal
credibility decreases non -linearly in the number of observed failures. In post -Soviet Azerbaijan,
where resource allocation has been  opaque [35, 41], timely disbursement serves as a visibilit y
indicator of credibility. When it does not hold, stakeholders more fundamentally reconstitute the
institutional features in line with Erdem and Swait’s [30] risk -reduction framework. Through
temporal analysis, we find that polarity troughs correspond to disbursement windows, indicating a
predictable vulnerability calendar for brand managers.
Network topology and weak -tie deficits. The clustering -coefficient differential (d=2.69)
exposes that the conversion of brand equity is structurally dependent on the topology of said network.
Granovetter’s [38] weak -tie hypothesis predicts that the sparser a network, less is information
diffused. The higher betweenness centrality in networks with 20% of nodes as non-urban (0.0089 vs.
0.0034) supports information flows through a few bridge nodes on these networks. This generalizes
the small-world model of Watts and Strogatz [26]: universities with sparser networks need to invest
disproportionately in network activation, i.e., especially weak-tie creation.

17

Dayanıqlı inkişaf, cild 6, № 1, 2026
Platform-differentiated activation and algorithmic fairness. Platform thematic divergence
(V=. 42) and therefore encourages discarding aggregated SMP constructs. Instagram initiates brand
imagery (T1), Facebook, performance judgments (T2, T3), TikTok generates resonance (T4) and
YouTube triggers deep cognitive evaluation (T6). This bears on algorithmic fairness [43]:
engagement-happy platform algorithms will amplify urban content and therefore systematically
widen the brand equity gap between urban and non-urban institutions.
6.2 Practical Implications
Trust repair protocols. There should be 24 hour deadlines for response for scholarship enquiries.
Automated SMS/Telegram notifications tied to disbursement databases  can change reactive crisis
management into proactive reputation tethering.
Infrastructure-aware content. Non -urbanunivs should audit bandwidth: Instagram Stories (8 –
15MB) and 720p+ TikTok also fail to load for ~41.8% users browsing from sub -10Mbps areas ([4]
[5]). GSU can get a low-bandwidth G cal going: still images, sub-30s 480p TikTok, under 3 MB
Channel differentiation. The 42% difference in interaction (d=1.49) warrants separate editorial
calendars. ASOIU might need to become more of a visual brand te am (Instagram/TikTok) and an
administrative team (Facebook/website).
Network activation. Such peer-ambassador programmes can extend sparse nonurban networks
[28, 38]. LSU (C = 0.38) might be able of instituting a “Digital Ambassador” programme that focuses
on the weak-tie creation in faculty clusters.

Conclusion
This study provides the first computationally informed and formally triangulated account of
brand equity formation within higher education in Azerbaijan. Using a customized NLP pipeline to
analyze 47,832 social media posts, i.e. validatory directionally consistent support was found for all
five structural paths of the S-O-R model from Paper 1.
Three core findings emerged. The first, the scholarship -delay mechanism (polarity −0.67;
temporal spikes at  disbursement windows), makes clear how administrative failure cascades into
credibility collapse. Second, the clustering-coefficient differential (d=2.69) shows that brand equity
is a network -embedded phenomenon. Third, platform thematic divergence (V=. 4 2) demonstrates
channel-specific brand activation. Collectively, Papers 1 and 2 provide a methodologica lly
triangulated account of higher-education brand equity in a post-Soviet, digital-transitional context.

Limitations and Threats to Validity
Table 9. Structured Threats to Validity
Validity Type Specific Threat Mitigation
Construct ABSA taxonomy from Paper 1; circularity Codified before analysis; literature-grounded
Internal Cross-sectional; no temporal precedence Non-causal directional validation framing
External Single semester, single country Synchronized with Paper 1
Measurement Bot contamination; dark social Bot filter 7.9% (96% prec.); minors excluded
Statistical Permutation exchangeability Distribution-free; B=5,000; outliers trimmed
Measurement Sarcasm under-detection (~12%) Dual-classifier check; flagged as limitation
External Temporal seasonality (autumn only) Oct–Dec captures scholarship/exam cycles
Ecological Platform algorithm changes Multi-platform design reduces single-platform risk

18

Dayanıqlı inkişaf, cild 6, № 1, 2026

WhatsApp and Telegram—primary student communication channels —were inaccessible due
to encryption. Despite AzerBERT’s macro -F1 of .881, misclassification concentrates on sarcastic
posts and code-switched sentences. Five future directions: (1) longitudinal multi-semester studies; (2)
consent-based dark-social methodology; (3) domain-adaptive AzerBERT fine -tuning; (4) extension
to private institutions; (5) platform-algorithm audit studies [43].

References:

[1] Kumar, M., et al. (2025).  Digital/social media marketing and university brand equity.
Global Knowledge, Memory and Communication, 74(1), 1 –26.
[2] Pawar, S. K. (2024). Social media in higher education marketing. Cogent Business &
Management, 11(1), 2423059.
[3] Al -Adaini, A. H. M., & Rustamov, I. (2026). Instagram/TikTok strategies. Journal of
Marketing for Higher Education. [Paper 1].
[4] World Bank. (2024). Azerbaijan digital economy review. World Bank Group.
[5] International Telecommunication Union (ITU). (2024). Measuring di gital development
2024.
[6] Keller, K. L. (1993). Conceptualizing, measuring, and managing customer -based brand
equity. Journal of Marketing, 57(1), 1 –22.
[7] DataReportal. (2025). Digital 2025: Azerbaijan. Kepios.
[8] StatCounter. (2025). Social media sta ts: Azerbaijan. StatCounter Global Stats.
[9] Coombs, W. T., & Holladay, S. J. (2014). Crisis communication. Journal of Communication
Management, 18(1), 1 –16.
[10] Oflazer, K. (2014). Turkish: NLP challenges. Language Resources and Evaluation, 48(2),
285–299.
[11] Ahmadov, F., et al. (2026). Open -source AI for Turkic machine translation. Computers,
15(2), 73.
[12] Zohrabi, M., et al. (2023). Azerbaijani transliteration. Proceedings of the ACL Turkic
Workshop, 45 –53.
[13] Adoma, A. F., et al. (2020). Text representations for sentiment. Journal of Big Data, 7(1),
100.
[14] Mammadov, E., & Khalilov, E. (2023). azCorpus. Proceedings of the Language Resources
and Evaluation Conference (LREC), 1120 –1128.
[15] Joulin, A., et al. (2017). Bag of tricks for text class ification. Proceedings of the European
Chapter of the Association for Computational Linguistics (EACL), 427 –431.
[16] Benoit, K., et al. (2018). quanteda: An R package for quantitative text analysis. Journal of
Open Source Software, 3(30), 774.
[17] Safaro v, O., et al. (2023). AzerBERT. arXiv preprint arXiv:2305.01994.
[18] Conneau, A., et al. (2020). Unsupervised cross -lingual representation learning.
Proceedings of the Association for Computational Linguistics (ACL), 4885 –4899.
[19] Zeyrek, D. (2006). Tur kish resources for NLP. Proceedings of the Language Resources
and Evaluation Conference (LREC).
[20] Pontiki, M., et al. (2016). SemEval -2016 Task 5. Proceedings of the 10th International
Workshop on Semantic Evaluation (SemEval), 19 –30.
[21] Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of
Machine Learning Research, 3, 993 –1022.
[22] Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class -based TF-IDF
procedure. arXiv preprint arXiv:2203.05794.

19

Dayanıqlı inkişaf, cild 6, № 1, 2026
[23] Wasserman, S., & Faust, K. (1994). Social network analysis: Methods and applications.
Cambridge University Press.
[24] Voigt, P., & von dem Bussche, A. (2017). The EU General Data Protection Regulation
(GDPR): A practical guide. Springer.
[25] Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and
Psychological Measurement, 20(1), 37 –46.
[26] Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of ‘small -world’ networks.
Nature, 393(6684), 440 –442.
[27] Jick, T. D. (1979).  Mixing qualitative and quantitative methods: Triangulation in action.
Administrative Science Quarterly, 24(4), 602 –611.
[28] Brown, Z., et al. (2024). Student ambassadors and brand. Journal of Higher Education
Policy and Management, 46(1), 102 –118.
[29] M inistry of Digital Development and Transport. (2024). Azerbaijan ICT sector review.
Republic of Azerbaijan.
[30] Erdem, T., & Swait, J. (2004). Brand credibility, brand consideration, and choice. Journal
of Consumer Research, 31(1), 191 –198.
[31] Spence, M . (1973). Job market signaling. The Quarterly Journal of Economics, 87(3),
355–374.
[32] Morgan, R. M., & Hunt, S. D. (1994). The commitment -trust theory of relationship
marketing. Journal of Marketing, 58(3), 20 –38.
[33] Rutter, R., et al. (2024). Social listening and university brand. Internet Research, 34(2),
412–438.
[34] Pham, L., et al. (2025). Digital brand equity in emerging HE. Journal of Marketing for
Higher Education, 35(1), 78 –102.
[35] Transparency International. (2024). Corruption Perceptions Index (CPI) 2024.
[36] Clark, M., et al. (2025). Authentic stakeholder voice. Journal of Business Research, 178,
114687.
[37] Fetters, M. D., Curry, L. A., & Creswell, J. W. (2013). Achieving integration in mixed
methods designs —Principles and practices. Health Services Research, 48(6), 2134–2156.
[38] Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology,
78(6), 1360 –1380.
[39] Tanturov, S., et al. (2025). NLP for Turkic languages. Natural Language Engineering,
31(1), 1–34.
[40] Yılmaz, E., et al. (2025). Sarcasm detection in Turkic. Computational Linguistics, 51(1),
89–118.
[41] OECD. (2024). Integrity in education: Azerbaijan. Organization for Economic Co -
operation and Development.
[42] Spence, M. (2002). Signaling in retrospect and the informational structure of markets. The
American Economic Review, 92(3), 434 –459.
[43] Lambrecht, A., & Tucker, C. (2024). Algorithmic bias. Marketing Science, 43(2), 312 –
335.

AZƏRBAYCAN ALİ TƏHSİLİNDƏ RƏQƏMSAL BREND REZONANSI:
MARAQLI TƏRƏFLƏRİN DİSKURSUNUN SOSİAL DİNLƏMƏ VƏ NLP TƏHLİLİ
1,3A. Al-Adaini, 2,3İ. Rüstəmov
1Biznesin idarə edilməsi üzr ə doktorant, 2iqtisad elmləri doktoru, professor
3Azərbaycan Dövlət Neft və Sənaye Universiteti

20

Dayanıqlı inkişaf, cild 6, № 1, 2026
Xülasə: Tələbələrin, məzunların və potensial abituriyentl ərin ali təhsil müəssisələrinin brend
qavrayışlarını davamlı olaraq müzakir ə etdikləri və formalaşdırdıqları mühit strukturlaşdırılmamış
rəqəmsal diskursdur. 2024 -cü ilin oktyabr -dekabr aylarında on dövl ət universitetind ən toplanm ış
47,832 sosi al media paylaşımını və şərhini əhatə edən bu tədqiqat, eyni zamanda Az ərbaycanın ali
təhsil sistemində əvvəlcədən təsdiqlənmiş, sorğuya əsaslanan istehlakçı əsaslı brend kapitalı (CBBE)
struktur modelini (M əqalə 1) genişmiqyaslı sosial dinl əmə və təbii di lin emalı (NLP) analizi il ə
trianqulyasiya edir. Azərbaycan dilinin aqlütinativ morfologiyasını və geniş yayılmış kod dəyişməsini
(code-switching) d əf etm ək üçün AzerBERT sentiment t əsnifatı (makro -F1 = 0.881), aspekt ə
əsaslanan sentiment analizi (ABSA; orta κ = 0.776), BERTopic/LDA mövzu modelləşdirməsi və sosial
şəbəkə analizini özünd ə birləşdirən xüsusi beş m ərhələli NLP iş axını yaradılmışdır. Əvv əlcədən
müəyyən edilmiş trianqulyasiya protokolunda h ər beş struktur yolu t əsdiqlənmiş v ə istiqamət
baxımından uyğun olmuşdur. Üç n əticə nəzəri cəhətdən əhəmiyyətlidir: təqaüd -gecikmə diskursu
(mənfi paylaşımların 18,4% -i; qütblülük −0.67) brendin etibarlılığı v ə inam hipermiqyasının
mexanizmini dəqiqləşdirir; şəhər və qeyri-şəhər klasterləşmə əmsalı fərqləri (0.671-ə qarşı 0.412; d
= 2.69) m əkanla t ənzimlənən kapital konversiyasını mü əyyən edir; v ə platformaya xas tematik
fərqlilik (χ² = 847.3, V = 0.42) kanallar üzr ə diferensial brend ölçüsünün aktivasiyasını nümayiş
etdirir.
Açar sözlər: sosial dinl əmə; təbii dilin emalı; brend kapitalı; ali t əhsil; AzerBERT; aspekt ə
əsaslanan sentiment analizi; BERTopic; sosial ş əbəkə analizi; Az ərbaycan; qarışıq metodlu
trianqulyasiya.

ЦИФРОВОЙ РЕЗОНАНС БРЕНДА В ВЫСШЕМ ОБРАЗОВАНИИ АЗЕРБАЙДЖАНА:
АНАЛИЗ ДИСКУРСА ЗАИНТЕРЕСОВАНН ЫХ СТОРОН С ИСПОЛЬЗОВАНИЕМ
СОЦИАЛЬНОГО СЛУШАНИЯ И NLP
¹А. Аль-Адаини, ²И. Рустамов
1,3Докторант по специальности «Бизнес-администрирование», 2,3доктор экономических наук,
профессор
3Азербайджанский государственный университет нефти и промышленности

Аннотация: Среда, в которой студенты, выпускники и потенциальные абитуриент ы
непрерывно формируют и обсуждают восприятие бренда высших учебных заведений,
представляет собой неструктурированный цифровой дискурс. Охватывая 47 832 публикации
и комментария в социальных сетях, собранные из десяти государственных университет ов в
период с октября по декабрь 2024 года, настоящее исследование проводит триангуляцию
ранее валидированной структурной модели потребительского капитала бренда ( consumer-
based  brand  equity, CBBE), основанной на данных опроса, в системе высшего образования
Азербайджана (Статья 1) с крупномасштабным анализом методами социального
прослушивания ( social listening) и обработки естественного языка ( natural  language
processing , NLP). Для преодоления агглютинативной морфологии азербайджанского языка и
широко распространённого переключения кодов ( code-switching) был разработ ан
специализированный пятиэтапный конвейер NLP, включающий классификацию тональност и
на основе AzerBERT (макро -F1 = 0 ,881), аспектно -ориентированный анализ тональност и
(aspect-based sentiment analysis , ABSA; средний κ = 0,776), тематическое моделирование
BERTopic/LDA и анализ социальных сетей. В рамках заранее определённого протокола
триангуляции все пять структурных путей были подтверждены и оказались согласованными
по направлению. Три вывода имеют теоретическую значимость: дискурс о задержке
стипендий (18,4 % негати вных публикаций; полярность −0,67) точно определяет механизм
гипермасштабирования достоверности бренда и доверия к нему; различия коэффициент ов
кластеризации между городской и негородской средами (0,671 против 0,412; d = 2,69)

21

Dayanıqlı inkişaf, cild 6, № 1, 2026
выявляют конверсию капитала б ренда, модерируемую фактором местоположения; а
платформо -специфическое тематическое расхождение (χ² = 847,3; V = 0,42) иллюстрирует
дифференцированную активацию измерений бренда в различных каналах.
Ключевые слова: социальное прослушивание; обработка естественного языка; капит ал
бренда; высшее образование; AzerBERT; аспектно -ориентированный анализ тональност и;
BERTopic; анализ социальных сетей; Азербайджан; триангуляция смешанными методами.
