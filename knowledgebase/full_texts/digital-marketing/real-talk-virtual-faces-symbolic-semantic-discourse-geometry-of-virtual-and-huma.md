---
title: 'Real Talk, Virtual Faces: Symbolic-Semantic Discourse Geometry of Virtual and Human Influencer
  Audiences'
url: https://arxiv.org/abs/2603.24410
category: digital-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Shahram Chaudhry
- Sidahmed Benabderrahmane
- Talal Rahwan
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.24410
pages: 24
chars: 51247
fetched_at: '2026-11-08T13:08:33+00:00'
kb_version: 1
---

# Real Talk, Virtual Faces: Symbolic-Semantic Discourse Geometry of Virtual and Human Influencer Audiences

Real Talk, Virtual Faces: Symbolic–Semantic
Discourse Geometry of Virtual and Human
Influencer Audiences
Shahram Chaudhry, Sidahmed Benabderrahmane, and Talal Rahwan
New York University (NYUAD), Division of Science, Computer Science Department
sc9425@nyu.edu
Abstract. Virtual influencers (VIs)—digitally constructed social-media
personas—are becoming prominent actors in online culture, marketing,
and identity formation. Yet it remains unclear whether audiences respond
to them through the same behavioural discourse patterns used for human
influencers (HIs), or whether virtuality gives rise to distinctive modes of
reaction. Existing studies often rely on surveys, engagement statistics,
or marginal sentiment distributions, which reveal what audiences say
but not how affective, topical, and psycholinguistic signals are jointly
organised.
We introduce a symbolic–semantic framework for analysing audience dis-
course around virtual and human influencers. First, we use Formal Con-
cept Analysis and association rule mining to extract closed co-occurrence
structures from sentiment labels, topic tags, and Big Five psycholinguistic
cues. Second, we render the extracted formal concepts as natural-language
descriptions, embed them using MiniLM, and compare their semantic
geometry across virtual and human influencer audiences.
Applied to 69,498 YouTube comments from three matched VI–HI in-
fluencer pairs, our analysis reveals three findings. First, HI discourse
is organised around a compact, stability-centred pattern in which low
neuroticism anchors positive sentiment, whereas VI discourse supports
multiple discourse regimes. Second, VI concepts are more semantically
dispersed than HI concepts, while both groups show strong symbolic–
semantic alignment between closed-set structure and embedding geometry.
Third, VI discourse contains a distinct artificial-identity region and a
higher concentration of negative sentiment in psychologically sensitive
topics such as mental health, body image, and artificial identity. Together,
these findings suggest that virtuality reshapes not only the sentiment of
audience reactions, but also the symbolic and semantic organisation of
online social discourse.
Keywords:Virtual influencers·computational social science·social me-
dia analytics·sentiment analysis·symbolic–semantic analysis·audience
behaviour
arXiv:2603.24410v2  [cs.CY]  12 May 2026

2 S. Chaudhry et al.
1 Introduction
Virtual influencers (VIs)—synthetic personas designed to look, speak, and interact
like social-media creators—are increasingly visible in online culture, advertising,
music, fashion, and youth-oriented digital communities. Their rise raises a compu-
tational social science question: do audiences respond to virtual figures through
the same discourse patterns used for human influencers (HIs), or does virtuality
reorganise how users combine emotion, topical attention, and social judgement?
Prior work on virtual influencers has largely relied on surveys, experiments,
or aggregate engagement statistics. These approaches are valuable, but they
usually analyse individual signals in isolation: sentiment scores, authenticity
perceptions, trust, or engagement counts. Such marginal summaries can miss
the structure of audience behaviour. For example, two influencer groups may
show similar prevalence of appearance-related comments, yet differ sharply in
how appearance co-occurs with sentiment, psycholinguistic style, and identity
scrutiny. This motivates a shift from asking onlywhataudiences say to asking
howmultiple behavioural signals are organised.
We address this problem through a symbolic–semantic discourse analysis
framework. The symbolic layer uses Formal Concept Analysis (FCA) and asso-
ciation rule mining to identify closed co-occurrence patterns among sentiment
labels, topic tags, and Big Five psycholinguistic cues. FCA is useful here because
its formal concepts capture maximal bundles of attributes shared by groups of
comments or weeks, revealing co-occurrence structure that cannot be read from
marginal frequencies alone [Ganter and Wille, 1999]. The semantic layer then
renders these formal concepts as short natural-language descriptions, embeds
them using MiniLM, and analyses the resulting concept geometry. This allows us
to test whether symbolic closed-set structure corresponds to coherent semantic
regions and whether VI discourse occupies a broader or more differentiated
semantic space than HI discourse.
A motivating example istopic_appearance. In our data, appearance has
near-equal marginal prevalence in VI and HI comments, yet it participates in
multiple VI rule clusters and in none of the HI rule sets. This is precisely the kind
of behavioural asymmetry that marginal statistics obscure but symbolic–semantic
structure can reveal.
Contributions.We make four contributions:
1. We construct a pair-matched YouTube comment dataset of 69,498 comments
from three virtual–human influencer pairs, enriched with sentiment labels,
topic tags, and psycholinguistic style cues.
2. We introduce a symbolic–semantic discourse analysis pipeline that combines
closed-set mining, association rules, MiniLM concept embeddings, and cluster-
level semantic interpretation.
3. We show that VI and HI audiences differ not only in marginal sentiment and
topic prevalence, but in the organisation of their discourse: VI comments yield
a denser and more diverse rule grammar, including an appearance-discourse
pattern absent from HI despite similar appearance prevalence.

Symbolic–Semantic Discourse Geometry 3
4. We compare symbolic and semantic concept geometries, showing strong
symbolic–semantic alignment for both groups, but higher semantic dispersion
for VI discourse and a VI-specific artificial-identity cluster.
Research questions.
RQ1. (Audience discourse structure.)How do the co-occurrence patterns
of sentiment, topic, and psycholinguistic cues differ between VI and HI
audiences?
RQ2. (Symbolic–semantic geometry.)Do symbolic discourse structures
extracted from formal concepts correspond to coherent semantic regions
in embedding space, and how does this geometry differ between VI and
HI audiences?
RQ3. (Virtuality-sensitive topics.)How do audience reactions around artifi-
cial identity, authenticity, body image, and mental health differ between
virtual and human influencer contexts?
Paper organisation.Section 2 presents the conceptual framework. Section 3
reviews related work on virtual influencers, social-media discourse analysis, and
symbolic–semantic interpretability. Section 4 describes the data and annotation
pipeline. Section 5 presents the symbolic–semantic methodology. Section 6 reports
the empirical results, and Section 7 discusses their implications for computational
social science and AI-mediated social interaction.
2 Conceptual Framework
We conceptualise virtual influencers assynthetic social actors: mediated personas
that perform the interactional role of influencers while foregrounding questions of
artificiality, embodiment, authenticity, and social presence. From a computational
social science perspective, the key question is not only whether comments about
VIsaremorepositiveornegativethancommentsaboutHIs,butwhetheraudiences
organise their reactions through different combinations of affect, topic, and
psycholinguistic style.
Figure 1 summarises the analytical logic. The starting point is the socio-
technical condition ofvirtuality: the audience knows, infers, or debates that the
visible persona is partly or fully synthetic. This condition may activate interpre-
tive frames around authenticity, artificial identity, appearance, and emotional
credibility. These frames become observable in comment discourse through combi-
nations of sentiment, topic, and psycholinguistic style cues. Our goal is therefore
to modeldiscourse organisation: the way these signals co-occur, form closed
symbolic structures, and occupy semantic regions.
This framing leads to two methodological commitments. First, we avoid
reducing audience response to marginal sentiment or topic prevalence alone,
because such summaries cannot show how signals combine. Second, we avoid
interpreting associations as causal effects of virtuality. The matched VI–HI design
supports comparative structural analysis, but unobserved differences in creators,

4 S. Chaudhry et al.
Virtuality as socio-technical condition
⇓
Artificial identity, authenticity ambiguity, synthetic embodiment
⇓
Audience discourse organisation
sentiment×topic×psycholinguistic style
⇓
Symbolic–semantic discourse regimes
closed concepts, association rules, semantic clusters
Fig.1: Conceptual framework. We treat virtuality not as a directly identifiable
causal treatment, but as a socio-technical condition under which audiences may
interpret identity, authenticity, embodiment, and affective credibility differently.
The empirical analysis therefore focuses on discourse organisation: how affective,
topical, and psycholinguistic signals co-occur in VI and HI audience responses.
content, audience composition, and platform dynamics may remain. We therefore
interpret our findings as pair-matched contrasts in discourse organisation.
3 Related Work
3.1 Virtual influencers as synthetic social actors
Research on virtual influencers consistently highlights authenticity, parasocial
relations, realism, and artificial identity as central to audience response. Batista
and Chimenti [da Silva Oliveira and Chimenti, 2021] show that highly human-
ised VIs can produce emotionally complex reactions ranging from admiration
to skepticism. Arsenyan and Mirowska [Arsenyan and Mirowska, 2022] find that
disclosure of virtual status shapes trust and purchase intent, while Xie-Carson et
al. [Xie-Carson et al., 2024] connect VI reception to uncanny-valley dynamics in
tourism contexts. Sands et al. [Sands et al., 2022] and Lou et al. [Lou et al., 2022]
further show that virtual influencer reception involves parasocial bonds, perceived
authenticity, and appearance-based evaluation. Looi et al. [Looi et al., 2025] anal-
yse Instagram comments on Lil Miquela and find polarised reactions associated
with identity ambiguity, and Yan et al. [Yan et al., 2024] show that the design
realism of VIs shapes emotional attachment. These studies motivate our focus
on how audiences organise discourse around artificial identity, appearance, and
emotional response.
3.2 Computational analysis of social-media discourse
Computational social science often studies online discourse through sentiment,
topic, stance, engagement, and language-style indicators. Such signals are useful
for large-scale analysis, but they are often treated independently. In this paper,

Symbolic–Semantic Discourse Geometry 5
Virtual Influencer Subscribers Human Counterpart Niche
Lil Miquela∼271k Samantha Nicole Fashion / lifestyle
APOKI∼329k YOUNG POSSE K-pop / performance
Milla Sofia∼28k Lydia Stoner Fashion lookbooks
Table 1: Selected VI–HI influencer pairs. HI counterparts are chosen by automated
API search within a ±10% subscriber window, then qualitatively aligned on
content niche.
we combine sentiment labels, topic tags, and Big Five psycholinguistic style
cues within a single symbolic context. Big Five cues inferred from text have a
long tradition in computational psycholinguistics [Mairesse et al., 2007]; however,
we use them only as aggregate textual style indicators, not as psychological
measurements of individual commenters. This distinction is important because
the unit of analysis is theorganisation of discourse, not the diagnosis of individual
users.
3.3 Symbolic and semantic interpretability
Formal Concept Analysis (FCA) provides a lattice-theoretic framework for identi-
fyingclosedco-occurrencestructuresinbinaryobject–attributerelations[ Ganter and Wille, 1999].
Prior work links FCA to frequent closed itemset mining [Stumme et al., 2002], ef-
ficient closed-set discovery [Pasquier et al., 1999], and knowledge processing appli-
cations[Poelmans et al., 2013].Associationrulemining[ Agrawal and Srikant, 1994]
provides complementary summaries of directional co-occurrence regularities
through support, confidence, and lift. Our contribution is to connect these sym-
bolic structures to semantic embedding geometry: formal concepts are rendered
as natural-language descriptions, embedded using MiniLM, and compared across
HI and VI audiences. This symbolic–semantic combination supports interpretable
analysis of social discourse by preserving formal co-occurrence structure while
enabling semantic comparison of discourse regimes.
4 Data
4.1 Dataset and influencer pairing
We collect top-level YouTube comments via the YouTube Data API (v3) from
three VI–HI pairs matched on content niche, subscriber scale, and posting fre-
quency. We retain English-language comments (langdetect), remove duplicates
and empty strings, and strip HTML.
Table 1 summarises the pairings. The final dataset contains29,327 VI
commentsand40,171 HI comments. In total, the dataset comprises69,498
comments across both conditions. To mitigate confounding, we match each HI
within a narrow subscriber window and by niche/content format; nevertheless,

6 S. Chaudhry et al.
residual differences (e.g., audience demographics and creator style) may remain,
so our claims are framed aspair-matched structural contrastsrather than causal
effects of virtuality.
4.2 Comment enrichment
Each comment is enriched with three attribute families:
Sentiment.Three-class (positive/neutral/negative) classification via a fine-tuned
RoBERTa classifier.
Big Five personality cues.Continuous scores (Openness, Conscientiousness,
Extraversion, Agreeableness, Neuroticism) inferred via a transformer-based re-
gressor [Mairesse et al., 2007]. Discretised tohigh/low binary attributes at the
group-level mean; ties are rare, and when they occur, we break them determinis-
tically by assigning greater-than-or-equal values tohigh.
We treat inferred Big Five scores aspsycholinguistic style proxiesextracted
from text, not as ground-truth personality measurements of the commenters, and
we use them only forcomparative structural analysisunder an identical pipeline
across conditions.
Topics.Twelve-class taxonomy assigned by Gemini Flash-Lite via zero-shot NLI:
positivity,appearance,authenticity_critique,artificial_identity,
parasocial,brand_ads,criticism,humor,performance,mental_health,
body_image,social_comparison.
The full attribute vocabulary is|M| = 25binary attributes, consisting of
3 sentiment attributes, 12 topic attributes, and 10 personality-bin attributes.
Table 2 reportsmarginalattribute prevalence (how often each signal appears
in isolation). In Section 5.2, we quantify the resultingconcept spaceunder
FCA iceberg filtering, capturing how signalsco-occurstructurally rather than
individually.
5 Methodology
5.1 FCA preliminaries: from formal contexts to rules
Formal Concept Analysis represents data as a binary relation between objects
and attributes. Aformal contextis a triple K = (G, M, I), where G is a set of
objects, M is a set of attributes, andI⊆G×M indicates which object has
which attribute. In our setting, objects are either comments or weekly aggregates,
and attributes are binary discourse signals such as sentiment labels, topic tags,
and discretised psycholinguistic cues.
ForA⊆GandB⊆M, FCA defines two derivation operators:
A′ ={m∈M| ∀g∈A,(g, m)∈I},(1)
B′ ={g∈G| ∀m∈B,(g, m)∈I}.(2)

Symbolic–Semantic Discourse Geometry 7
Attribute HI VI∆(VI−HI)
topic_artificial_identity0.005 0.184+0.179
sentiment_Negative0.067 0.125+0.058
topic_authenticity_critique0.037 0.062+0.025
topic_appearance0.159 0.170+0.011
topic_social_comparison0.007 0.007 0.000
sentiment_Positive0.766 0.669−0.097
topic_positivity0.677 0.472−0.205
Table 2: Attribute prevalence (selected attributes), sorted by∆. The near-equal
appearance prevalence (0.011gap) contrasts sharplywith itsstructural asymmetry
in rule mining (Section 6.2).
ObjectP A G N
c1 ✓ ✓ ✓
c2 ✓ ✓ ✓
c3 ✓ ✓
c4 ✓ ✓
c5 ✓ ✓ ✓ ✓
Table 3: Toy formal context illustrating FCA. Objects are comments and at-
tributes are binary discourse signals:P = positive sentiment,A = appearance
topic,G= high agreeableness, andN= high neuroticism.
Thus, A′ is the set of attributes shared by all objects inA, and B′ is the set of
objects sharing all attributes inB. Aformal conceptis a pair( A, B)such that
A′ = B and B′ = A. The setA is called theextent, and the setB is called the
intent. Intuitively, a formal concept is a maximal closed co-occurrence pattern:
no object can be added without losing an attribute, and no attribute can be
added without losing an object.
Table 3 gives a small illustrative context. Here, five comments are described
using four binary discourse attributes: positive sentiment (P), appearance topic
(A), high agreeableness (G), and high neuroticism (N).
From this context, FCA identifies closed attribute sets such as{P, G}, {A, N},
and {P, A, G}. For instance, the attribute set{A, G}is not closed, because all
comments that have bothA and G also haveP. Its closure is therefore{P, A, G}.
This closed pattern corresponds to the formal concept:
({c1, c2, c5},{P, A, G}).
In discourse terms, this concept represents a group of comments where appearance-
related discourse co-occurs with positive sentiment and high agreeableness.

8 S. Chaudhry et al.
∅
{c1, c2, c3, c4, c5}
{A}
{c1, c2, c3, c5}
{P, G}
{c1, c2, c4, c5}
{A, N}
{c3, c5}
{P, A, G}
{c1, c2, c5}
{P, A, G, N}
{c5}
Fig.2: Toy concept lattice derived from Table 3. Each node shows a closed intent
and its corresponding extent. More specific concepts appear lower in the lattice.
The formal concepts are partially ordered by extent inclusion:
(A1, B1)≤(A 2, B2)⇐ ⇒A1 ⊆A 2,
or equivalently by reverse intent inclusion:
B2 ⊆B 1.
This ordering forms a concept lattice. Figure 2 shows the lattice induced by the
toy context. Moving downward in the lattice corresponds to adding attributes
and obtaining more specific discourse patterns.
Association rules are then derived from co-occurring attribute sets. For two
disjoint attribute sets X, Y⊆M , a rule X⇒Y is evaluated using support,
confidence, and lift:
supp(X⇒Y) =P(X∪Y),(3)
conf(X⇒Y) =P(Y|X),(4)
lift(X⇒Y) = P(Y|X) P(Y) .(5)
For example, in Table 3, the rule
{A, G} ⇒ {P}
has support3 /5, confidence1 .0, and lift1/0.8 = 1.25, because all comments with
both appearance and high agreeableness also have positive sentiment. In the full
study, the same logic is applied to the VI and HI comment-level formal contexts,

Symbolic–Semantic Discourse Geometry 9
Analytical view Captures Contribution to the study
Marginal prevalence Individual sentiment/topic/style
frequencies
Establishes baseline differences and ex-
poses cases where similar frequencies
hide different structures.
FCA concepts Closed co-occurrence bundles Identifies stable symbolic discourse pro-
files that cannot be reduced to individ-
ual attributes.
Association rules Directional co-occurrence regular-
ities
Summarises interpretable discourse
grammars through support, confidence,
and lift.
MiniLM concept ge-
ometry
Semantic proximity among for-
mal concepts
Tests whether symbolic structures cor-
respond to coherent semantic regions.
Cluster labels Human-readable discourse
regimes
Interprets computed semantic regions
without replacing the symbolic evidence.
Table 4: Analytical views in the symbolic–semantic discourse framework.
using support, confidence, and lift thresholds to retain interpretable discourse
rules. Our methodology combines symbolic structure discovery and semantic
geometry. First, FCA extracts closed co-occurrence patterns from weekly and
comment-level formal contexts. Second, association rules summarise directional
regularities among sentiment, topic, and psycholinguistic attributes. Third, we
render formal concepts as natural-language descriptions, embed them using
MiniLM,andcomparesemanticgeometryacrossHIandVIconceptspaces.Finally,
we perform targeted topic-level analyses for psychologically salient domains.
Table 4 summarises the role of each analytical layer. The framework is designed
so that each layer answers a different social-science question: marginal analysis
describes what is frequent, FCA and rules describe what co-occurs, semantic
geometry describes how closed concepts relate in meaning space, and cluster
labels provide human-readable interpretations of computed discourse regions.
Figure 3 previews the semantic concept space used in the final stage of
the analysis. HI and VI concepts partially overlap, indicating shared audience
response modes, while VI concepts occupy a slightly broader region, suggesting
greater discourse heterogeneity.
5.2 Layer 1: Weekly FCA with support-based iceberg filtering
Aggregation.Comments are grouped by calendar week. Within each week, sen-
timent and topic are summarised by modal label; Big Five traits are averaged
across comments and then binarised against the group-level weekly mean. Each
week becomes one binary object in the formal context.
Formal context and concept extraction.We build one binary formal context
Kc = (Gc, M, Ic)per condition c∈ {HI,VI}, where Gc is the set of weeks andM
is the shared attribute vocabulary. FCA extracts formal concepts; aformal concept
(A, B)satisfies A = B′ and B = A′, where B′ = {g∈G c | ∀m∈B : (g, m) ∈I c}
and symmetrically. We order concepts by⊆ on extents to form the concept lattice
L(Kc)[Ganter and Wille, 1999].

10 S. Chaudhry et al.
Fig.3: Semantic geometry of FCA concepts for HI and VI audiences. Each
point represents a formal concept rendered as a natural-language description
and embedded using MiniLM. HI and VI concepts partially overlap, while VI
concepts occupy a slightly more dispersed semantic region.
Iceberg filtering.FCA can generate a large number of concepts, many weakly
supported or short-lived. We retain only those with: (i)minimum tempo-
ral support ≥20%(concept must appear in at least 20% of all weeks), and
(ii)minimum intent size ≥3(concept must encode at least three distinct
attributes).
These thresholds were selected empirically to balance interpretability and
coverage: lower supports produced large numbers of weak concepts, while higher
thresholds eliminated meaningful discourse patterns.
Table 5 shows the dramatic compression achieved: from 1,895 VI concepts to
10 filtered, and from 864 HI concepts to 24. These thresholds balance coverage
and interpretability and are used for all subsequent weekly-level analyses. Unlike
Table 2 (marginals), Table 3 quantifies the size of the closed co-occurrence space
under FCA filtering.
Cross-group comparison.Concepts with identical intents across conditions are
labelledshared; those unique to one condition are labelledVI-onlyorHI-only. We
visualise attribute prevalence within each category using horizontal bar charts.
5.3 Layer 2: Comment-level association rule mining
Context construction.We build a second formal context per condition where
objects are individual comments (not weeks) and attributes are the same 25 binary
signals. For comment-level rules, we discretise continuous personality traits at the

Symbolic–Semantic Discourse Geometry 11
Multilingual Intent Support VI (raw) VI (filtered) HI (raw) HI (filtered)
No>3 0.20 18951086424
No>3 0.10 1895 114 864 152
No>2 0.20 1895 54 864 80
No>2 0.10 1895 241 864 264
Yes>3 0.20 3980 11 1269 24
Yes>3 0.10 3980 124 1269 153
Yes>2 0.20 3980 57 1269 80
Yes>2 0.10 3980 288 1269 268
Table 5: FCA concept counts under different support, intent-size, and language-
inclusion settings (Multilingual = Yes includes non-English comments). Bold row
shows the selected configuration (English-only, intent>3, support≥0.20).
comment level globally, whereas for weekly FCA we discretise weekly-averaged
traits locally.
Rule generation.We use an approximate concept-based rule-mining procedure to
generate candidate association rulesX⇒Y (X∩Y = ∅, |X| ≤3), derived from
closed co-occurrence patterns in the formal context. We then filter candidates by
support, confidence, and lift:
supp(X⇒Y) =P(X∪Y),conf(X⇒Y) =P(Y|X),lift(X⇒Y) = P(Y|X) P(Y) .
(6)
Rules are retained if minsup≥1%, minconf≥0.8, and lift>1.2.
Wereportassociation rules(statisticalregularitiesquantifiedbysupport/confidence/lift),
and do not interpret them as logical implications or compute an implication basis
(e.g., Duquenne–Guigues).
Rule cluster analysis.We group retained rules by the dominant topic attribute
in their antecedent to identifypremise clusters—interpretable discourse sub-
grammars sharing a topic anchor.
5.4 Semantic Geometry of Formal Concepts
To examine whether symbolic FCA structures correspond to meaningful semantic
regions, we transform each formal concept intent into a short natural-language
description. For example, the intent {topic_appearance, sentiment_Positive,
Agreeableness_high, Conscientiousness_low} is rendered as: “Audience dis-
course focused on appearance, with positive sentiment, associated with high
agreeableness and low conscientiousness.”
We embed these concept descriptions using MiniLM and cluster the resulting
vectors using agglomerative clustering with cosine distance. This yields a semantic
concept space in which each point corresponds to a closed symbolic discourse
pattern. We then compare VI and HI concept spaces using two measures. First,
semantic dispersionis computed as the average cosine distance between each

12 S. Chaudhry et al.
concept embedding and the group centroid. Higher dispersion indicates that
extracted discourse concepts occupy a broader semantic region. Second,symbolic–
semantic alignmentis computed by correlating FCA symbolic distance, measured
by Jaccard distance between concept intents, with MiniLM semantic distance.
A high positive correlation indicates that symbolic proximity in the closed-set
structure is reflected in semantic embedding space.
5.5 Complementary topic-level analysis
For topics that may fluctuate week-to-week and therefore resist weekly FCA,
we conduct a direct comment-level analysis (without time aggregation) of four
psychologically salient topics: artificial identity, authenticity critique, body image,
and mental health. For each topic and each condition, we compute: (i) senti-
ment distribution (positive/neutral/negative proportions); (ii) average Big Five
personality profiles, visualised as radar charts.
For clarity of presentation, we report (i) marginal prevalences (Table 2), (ii)
iceberg-filtered concept-space sizes (Table 5), and (iii) clustered rule sets under a
robustness grid (Table 10), aligning each result with RQ1–RQ3.
5.6 Reliability, robustness, and interpretation safeguards
Several design choices are used to make the comparison conservative. First, the
same annotation, binarisation, concept extraction, rule filtering, embedding, and
clustering pipeline is applied to VI and HI comments. Second, association rules
are evaluated under a support–confidence grid rather than a single threshold,
allowing us to check whether key findings, especially the VI-specific appearance
rules, persist across parameter settings. Third, semantic labels are assigned
only after formal concepts have been extracted and embedded; the labels are
used as interpretive summaries of computed clusters, not as evidence-generating
steps. Finally, all findings are reported as structural associations in pair-matched
observational data rather than causal effects of virtuality.
6 Results
6.1 RQ1a: Weekly symbolic discourse profiles
Figure 4 compares HI-only and VI-only stable concept attribute distributions.
HI-only conceptsare sentiment-dominated: positive sentiment and topic
positivity are the most frequent attributes, alongside low neuroticism and high
conscientiousness. This indicates that HI discourse is organised around explicit
affective evaluation in a psychologically stable configuration.
VI-only conceptsare personality-dominated: high openness is the most
frequent attribute, followed by high agreeableness, low conscientiousness, and
high extraversion. Positive sentiment and topic positivity are less prominent.
High neuroticism appears more frequently in VI-only concepts, indicating greater

Symbolic–Semantic Discourse Geometry 13
(a) HI-only stable concepts
 (b) VI-only stable concepts
Fig.4: Dominant attributes in group-specific (HI-only vs. VI-only) stable FCA
concepts. HI-only concepts are sentiment-centred (positive sentiment, topic posi-
tivity, low neuroticism), whereas VI-only concepts are personality-centred (high
openness, high agreeableness, low conscientiousness).
Configuration #HI rules #VI rules
minsup=1%, minconf=0.8, lift>1.2 8 51
Table 6: Rule-set sizes under the approximate concept-based rule-mining proce-
dure, after support, confidence, and lift filtering.
emotional intensity. VI discourse appears exploratory and expressiveness-centred
rather than evaluation-centred.
This structural distinction—sentiment-centred HI vs. personality-centred
VI—constitutes a qualitative difference not visible from Table 2.
6.2 RQ1b: Comment-level rule grammar
Overall density.Table 6 shows that VI yields 51 rules and HI yields 8 under
identical thresholds—a 6.4-fold difference. Table 7 confirms higher average lift in
VI (1.32 vs. 1.23) and much higher maximum support (0.42 vs. 0.09).
HI rule structure.All 8 HI rules share a single premise cluster:topic_positivity
∧Neuroticism_low predicting sentiment_Positive (conf 0.92–0.96, lift 1.20–
1.25). Low neuroticism is the constant structural driver; secondary traits (agree-
ableness, extraversion, conscientiousness) modulate but do not determine the
association. This indicates astability-centreddiscourse architecture: positive
sentiment in HI is anchored in psychological regulation.
VI rule structure.VI rules form three distinct premise clusters:
1. Positivity-framing(40 rules): topic_positivity is the topic anchor; all
Big Five configurations appear as secondary antecedents, including high

14 S. Chaudhry et al.
Metric Mean Median Max
HI rules (8 total)
Support 0.062 0.065 0.090
Confidence 0.92 0.94 0.96
Lift 1.23 1.23 1.25
VI rules (51 total)
Support 0.146 0.080 0.420
Confidence 0.88 0.88 0.96
Lift 1.32 1.32 1.43
Table 7: Rule summary statistics (minsup=1%, minconf=0.8, lift>1.2).
neuroticism (conf=0.92, lift=1.37)—absent from HI. Positivity in VI is
expressiveness-centred: it persists even under emotional intensity.
2. Appearance-discourse(7 rules): topic_appearance is the topic anchor,
predicting sentiment_Positive (conf 0.81–0.88, lift 1.21–1.32). This cluster
isentirely absent from HIdespite near-equal appearance prevalence (0.170
vs. 0.159, Table 2)—the central marginal-versus-structure finding. Importantly,
no HI rules containtopic_appearance under the full grid of tested thresholds
(minsup ∈ {0.005, 0.01, 0.02}, minconf ∈ {0.8, 0.9}); appearance rules remain
VI-specific even when varying minsup and minconf.
3. Personality-only(4rules):notopicattributeinantecedent; Agreeableness_high
∧Neuroticism_low alone predicts sentiment_Positive (conf 0.81–0.85, lift
1.21–1.27).
Tables 8–9 list the full HI rule set and the top VI rules by cluster.
PremiseXConsequentYsupp conf lift
Agreeableness_high∧Neuroticism_low∧
topic_positivity
sentiment_Positive0.060 0.96 1.25
Extraversion_high∧Neuroticism_low∧
topic_positivity
sentiment_Positive0.080 0.95 1.24
Conscientiousness_low∧Neuroticism_low∧
topic_positivity
sentiment_Positive0.070 0.95 1.24
Neuroticism_low∧topic_positivity sentiment_Positive0.090 0.94 1.23
Neuroticism_low∧Openness_high∧
topic_positivity
sentiment_Positive0.090 0.94 1.23
Agreeableness_high∧Neuroticism_low∧
sentiment_Positive
topic_positivity0.060 0.82 1.21
Agreeableness_low∧Neuroticism_low∧
topic_positivity
sentiment_Positive0.030 0.92 1.20
Conscientiousness_high∧Neuroticism_low∧
topic_positivity
sentiment_Positive0.020 0.92 1.20
Table 8: All 8 HI rules. Single cluster:topic_positivity∧Neuroticism_low
anchors all rules.

Symbolic–Semantic Discourse Geometry 15
PremiseXConsequentYsupp conf lift
Positivity-framing cluster (top rules by lift)
Agreeableness_high∧Neuroticism_low∧
topic_positivity
sentiment_Positive0.050 0.96 1.43
Neuroticism_low∧topic_positivity sentiment_Positive0.080 0.94 1.40
Agreeableness_high∧Neuroticism_high∧
topic_positivity
sentiment_Positive0.200 0.92 1.37
topic_positivity sentiment_Positive0.420 0.89 1.33
Appearance-discourse cluster (absent from HI)
Agreeableness_high∧Conscientiousness_low∧
topic_appearance
sentiment_Positive0.070 0.88 1.32
Agreeableness_high∧Neuroticism_high∧
topic_appearance
sentiment_Positive0.070 0.87 1.30
Agreeableness_high∧topic_appearance sentiment_Positive0.090 0.85 1.27
Table9:SelectedVIrules.Toppositivity-framingrulesincludeNeuroticism_high—
absent from HI. Appearance-discourse rules have no HI counterpart despite equal
marginal prevalence.
6.3 Rule Extraction Robustness
To confirm that the 6.4-fold difference in rule counts (and the specific presence of
appearance rules in VI) is not an artifact of the chosen thresholds (minsup=1%,
minconf=0.8), we tested a grid of parameters. Table 10 demonstrates that VI con-
sistently generates substantially more rules than HI, and thattopic_appearance
rules remain exclusively found in VI discourse across all tested configurations.
minsup minconf #HI rules #VI rules
0.005 0.8 22 114
0.005 0.9 14 68
0.010 0.8 8 51
0.010 0.9 6 29
0.020 0.8 3 18
Table 10: Rule counts across extraction thresholds (lift>1.2) for selected config-
urations.
6.4 RQ2: Symbolic–semantic geometry of FCA concepts
To test whether FCA concepts correspond to meaningful semantic regions, we
embedded natural-language renderings of the top closed concepts using MiniLM
and compared their semantic distances with symbolic distances between concept

16 S. Chaudhry et al.
Group Symbolic–Semanticρ p-value Semantic Dispersion
HI 0.614<0.0010.0765
VI 0.640<0.0010.0882
Table 11: Symbolic–semantic geometry of FCA concepts.ρ is the Spearman cor-
relation between FCA symbolic distance, computed from concept intent overlap,
and MiniLM semantic distance, computed from concept-sentence embeddings.
Semantic dispersion is the mean cosine distance from each concept embedding to
the group centroid.
intents. Table 11 reports the resulting alignment and dispersion measures. Both
HI and VI concept spaces show strong symbolic–semantic alignment: Spearman
correlations between FCA symbolic distance and MiniLM semantic distance are
ρ = 0.614for HI and ρ = 0.640for VI (p <0.001in both cases). This indicates
that closed-set structure is not merely a symbolic artefact: concepts that are
close in FCA intent space also tend to be close in semantic embedding space.
At the same time, VI concepts exhibit higher semantic dispersion than HI
concepts (0.0882 vs. 0.0765), suggesting that VI discourse spans a broader and
more heterogeneous semantic region. This refines the rule-mining result: VI
discourse is not simply less coherent; rather, it remains symbolically aligned while
covering a more differentiated semantic space.
Figure 5 shows the semantic clusters of HI and VI concepts. HI clusters
are mainly organised around positivity and appearance-related engagement.
VI clusters include a distinct artificial-identity region in addition to multiple
appearance-relatedmodes,indicatingthataudiencereactionstovirtualinfluencers
are semantically more differentiated around identity, appearance, and emotionally
reactive engagement.
The semantic similarity heatmaps in Figure 6 show clear block structure,
confirming that concept clusters form coherent semantic regions rather than
arbitrary partitions. Compared with HI, the VI heatmap shows slightly stronger
differentiation across regions, consistent with the higher semantic dispersion
observed for VI concepts.
Table 12 summarises the cluster-level interpretation. The labels are used only
as human-readable summaries of clusters computed from FCA-derived concept
embeddings; the underlying evidence remains the symbolic closed-set structure
and the embedding geometry.
6.5 RQ3: Topic-level sentiment and psycholinguistic patterns
Artificial identity.Both groups are predominantly neutral on this topic (47.2% VI,
50.8% HI). However, VI comments show substantially more negative sentiment
(24.8% vs. 12.3%) and less positive sentiment (28.0% vs. 36.9%). The personality
profile (Fig. 8) shows comparable openness and neuroticism, but VI commenters

Symbolic–Semantic Discourse Geometry 17
(a) HI semantic clusters
 (b) VI semantic clusters
Fig.5: Semantic clustering of FCA concepts. Each point corresponds to a closed
concept embedded using MiniLM and coloured by semantic cluster. HI clusters are
mainly organised around positivity and appearance-related engagement, whereas
VI clusters include a distinct artificial-identity region and multiple appearance-
related modes.
(a) HI semantic similarity
 (b) VI semantic similarity
Fig.6: Semantic similarity heatmaps of FCA concepts ordered by semantic cluster.
Block structure indicates coherent semantic regions among closed discourse
patterns. VI concepts show slightly higher semantic dispersion, consistent with a
broader range of audience response modes.
score lower on agreeableness and conscientiousness, suggesting more evaluative
and critical discourse framing in virtual contexts.
Authenticity critique.Both groups are predominantly neutral (41.6% VI, 39.4%
HI), but VI threads exhibit more negative sentiment (36.1% vs. 24.8%) and less
positive (22.3% vs. 35.8%). Personality profiles are broadly similar (Fig. 10),

18 S. Chaudhry et al.
Group Cluster Semantic label
HI C0 Emotionally tense positive discourse
HI C1 High-arousal expressive positivity
HI C2 Tense appearance evaluation
HI C3 Expressive appearance admiration
HI C4 General positivity grammar
VI C0 Emotionally reactive positive framing
VI C1 Artificial identity scrutiny
VI C2 High-arousal expressive engagement
VI C3 Warm but tense appearance evaluation
VI C4 Expressive aesthetic admiration
Table 12: Semantic labels assigned to MiniLM clusters of formal concepts. Labels
summarise clusters of closed itemsets after rendering concept intents as natural-
language descriptions.
Fig.7: Sentiment distribution:
artificial identity. VI shows
≈25% negative vs.≈12% for HI.
 Fig.8: Big Five profile:artificial
identity. VI commenters score
lower on Agreeableness and Con-
scientiousness.
with high openness and neuroticism in both groups, suggesting reflective and
emotionally sensitive engagement regardless of type, but the emotional direction
diverges: VI audiences respond more sceptically to authenticity violations.
Body image.VI body-image comments are overwhelmingly negative or neutral
with virtually no positive sentiment, whereas HI threads include 28.4% positive
(Fig. 11). HI personality profiles show higher agreeableness and conscientiousness
(Fig. 12), indicating more supportive, structured engagement; VI profiles show
higher extraversion and lower conscientiousness, suggesting more expressive but
less moderated discourse.
Mental health.The mental health topic shows the most extreme divergence:
80.6% of VI-associated comments are negative, versus 42.1% for HI; HI retains

Symbolic–Semantic Discourse Geometry 19
Fig.9: Sentiment:authenticity
critique. VI: ≈36% negative; HI:
≈25%.
 Fig.10: Big Five profile:authen-
ticity critique. Personality pro-
filesaresimilar;VIshowsslightly
lower agreeableness.
Fig.11: Sentiment:body im-
age. VI is overwhelmingly neg-
ative/neutral; HI retains≈28%
positive.
 Fig.12: Big Five profile:body im-
age. HI shows higher agreeable-
ness and conscientiousness.
31.4% positive and 26.5% neutral (Fig. 13). VI personality profiles show higher
neuroticism and lower conscientiousness than HI (Fig. 14), consistent with more
emotionally reactive and less structured discourse.
Sentiment–trait cross-section.Table 13 shows that openness is uniformly high
across all conditions, while sentiment-specific differences emerge in agreeable-
ness, neuroticism, and conscientiousness. Positive VI comments show the highest
agreeableness (affiliative, warm); negative VI comments show the lowest agree-
ableness and highest conscientiousness (critical, deliberate). This reinforces the
two-architecture interpretation: VI audiences oscillate between warm expressive-
ness and structured critique, whereas HI discourse is more uniformly regulated.

20 S. Chaudhry et al.
Fig.13: Sentiment:mental health.
VI: ≈81% negative. HI: ≈42%
negative,≈31% positive.
 Fig.14: Big Five profile:men-
tal health. VI shows higher neu-
roticism and lower conscientious-
ness.
Group Sentiment E N A C O
HI Positive 0.89 0.84 0.53 0.20 0.99
VI Positive 0.88 0.82 0.61 0.18 0.99
HI Neutral 0.84 0.93 0.43 0.20 0.99
VI Neutral 0.84 0.89 0.42 0.22 0.99
HI Negative 0.81 0.87 0.44 0.23 0.99
VI Negative 0.81 0.88 0.33 0.27 0.99
Table 13: Average Big Five personality trait profiles by sentiment category
and influencer type. Traits are abbreviated as follows: E = Extraversion, N =
Neuroticism, A = Agreeableness, C = Conscientiousness, O = Openness.
7 Discussion
7.1 What virtuality changes in audience discourse
Across the symbolic, semantic, and topic-level analyses, a consistent picture
emerges: virtual influencer discourse is not simply a shifted version of human
influencer discourse. HI reactions are concentrated around a compact, stability-
centred pattern in which low neuroticism anchors positive sentiment. VI reactions,
by contrast, support multiple discourse regimes, including appearance-related
evaluation, emotionally reactive positivity, and artificial-identity scrutiny. This
suggests that audiences respond to virtual figures through a broader set of inter-
pretive frames involving not only admiration, but also questions of authenticity,
embodiment, and synthetic identity.

Symbolic–Semantic Discourse Geometry 21
The appearance finding is especially informative. Although appearance-related
comments occur at nearly the same marginal rate for VI and HI, appearance
enters multiple VI rule clusters and is absent from the HI rule set under the same
thresholds. Thus, the behavioural difference is not merely how often appearance
is discussed, but how appearance becomes structurally embedded with sentiment
and psycholinguistic style.
7.2 Symbolic–semantic structure of online audience behaviour
The symbolic–semantic analysis strengthens the behavioural interpretation of
the FCA results. Closed-set mining reveals which affective, topical, and style
signals co-occur systematically; MiniLM embeddings show how these symbolic
configurations form semantic regions. The strong symbolic–semantic alignment
observed for both groups indicates that formal concepts are not arbitrary attribute
bundles: symbolic proximity in the FCA space corresponds to semantic proximity
in embedding space.
At the same time, VI concepts exhibit higher semantic dispersion and a distinct
artificial-identity cluster. This indicates that VI discourse remains organised, but
spans a broader semantic space. For computational social science, this is important
because it shows how symbolic pattern mining and semantic embeddings can be
combined to study not only sentiment polarity, but the organisation of social
meaning in large-scale online discourse.
7.3 Sensitive topics and artificial identity
Topic-specific analyses show that VI contexts contain a higher concentration of
negative sentiment in psychologically sensitive domains, especially mental health,
body image, and artificial identity. We interpret these results as associations
between influencer type and discourse organisation, not as causal evidence that
virtuality itself produces negative sentiment. Nevertheless, the co-occurrence
of artificial identity, appearance evaluation, and emotionally reactive discourse
suggests that synthetic embodiment may create distinctive conditions for audience
scrutiny and affective tension.
7.4 Implications for AI-mediated social interaction
The results suggest that virtual influencers should not be treated simply as inter-
changeable substitutes for human creators. Their synthetic identity appears to
introduce additional interpretive frames through which audiences discuss authen-
ticity, appearance, and emotional vulnerability. This is particularly important
for topics such as body image and mental health, where VI-linked discourse
shows a higher concentration of negative sentiment. For platforms, marketers,
and creators, these findings suggest that artificial personas should be deployed
cautiously in psychologically sensitive contexts and that audience responses
should be monitored not only through engagement metrics, but also through the
structure of discourse around identity, embodiment, and wellbeing.

22 S. Chaudhry et al.
7.5 Ethical considerations
All analyses are conducted at aggregate level. We do not attempt to identify
commenters, infer protected attributes, or make psychological claims about
individual users. Big Five outputs are treated as textual style indicators rather
than measurements of actual personality. Because user comments may contain
sensitive expressions, especially around mental health and body image, examples
should be paraphrased or reported only in aggregate unless explicit ethical
approval and anonymisation procedures are in place. The goal of the analysis is
to characterise discourse regimes around synthetic social actors, not to evaluate
or profile individual audience members.
7.6 Limitations
Several limitations should be considered. First, the data are observational, so the
results should be interpreted as pair-matched structural contrasts rather than
causal effects of virtuality. The VI–HI pairs are matched by niche and subscriber
scale, but unobserved differences in audience demographics, creator style, moder-
ation practices, posting schedules, and platform recommendation dynamics may
remain. Second, the study is limited to English-language YouTube comments
and three influencer pairs; replication on other platforms and larger cross-niche
samples is needed before generalising to virtual influencers as a whole. Third,
sentiment, topic, and psycholinguistic attributes are inferred automatically and
may contain classification errors. Personality attributes in particular should be
understood as style proxies extracted from text, not as measurements of individ-
ual commenters. Fourth, rule generation relies on an approximate concept-based
mining procedure; association rules are therefore interpreted as statistical regu-
larities rather than logical implications or causal relationships. Finally, MiniLM
embeddings and cluster labels provide semantic interpretation of formal concepts,
but the underlying evidence remains the closed symbolic structure extracted from
the formal contexts. Future journal extensions should include manual validation
of topic/sentiment labels, independent assessment of cluster labels, alternative
embedding models, and permutation tests for the observed semantic-dispersion
gap.
8 Conclusion
We presented a symbolic–semantic computational social science analysis of au-
dience discourse around virtual and human influencers. Using 69,498 YouTube
comments from three matched VI–HI pairs, we showed that virtuality is asso-
ciated with differences not only in sentiment and topic prevalence, but in the
organisation of discourse itself.
Closed-set and rule-based analysis revealed that HI discourse is concentrated
around a compact stability-centred pattern, whereas VI discourse supports mul-
tiple discourse regimes, including an appearance-related pattern absent from

Symbolic–Semantic Discourse Geometry 23
HI despite similar appearance prevalence. Extending this analysis with MiniLM
concept embeddings showed strong symbolic–semantic alignment in both groups,
while VI concepts exhibited higher semantic dispersion and a distinct artificial-
identity cluster.
Together, these findings suggest that virtual influencers reshape online au-
dience reactions by broadening the semantic space of discourse around identity,
appearance, and emotional engagement. More broadly, the study demonstrates
how symbolic pattern mining and semantic embedding geometry can be combined
to produce interpretable computational social science analyses of large-scale on-
line behaviour, especially in emerging contexts where synthetic social actors blur
the boundaries between authenticity, performance, and artificial identity.
References
[Agrawal and Srikant, 1994]Agrawal, R. and Srikant, R. (1994). Fast algorithms for
mining association rules in large databases. InProceedings of the 20th Interna-
tional Conference on Very Large Data Bases (VLDB 1994), pages 487–499. Morgan
Kaufmann.
[Arsenyan and Mirowska, 2022]Arsenyan, J. and Mirowska, A. (2022). Almost human?
a comparative experiment on the effectiveness of human and virtual influencers.
Psychology & Marketing, 39(12):2273–2287.
[da Silva Oliveira and Chimenti, 2021]da Silva Oliveira, A. B. and Chimenti, P. (2021).
"humanized robots": A proposition of categories to understand virtual influencers.
Australasian Journal of Information Systems, 25.
[Ganter and Wille, 1999]Ganter, B. and Wille, R. (1999).Formal Concept Analysis:
Mathematical Foundations. Springer, Berlin, Heidelberg.
[Looi et al., 2025]Looi, J., Kim, E. A., and E, Z. (2025). Sponsorship disclosure in
virtual influencer marketing: Assessing users’ sentiment and engagement toward
virtual influencer endorsements.Journal of Advertising Research, 0(0):1–23.
[Lou et al., 2022]Lou, C., Kiew, S. T. J., Chen, T., Lee, T. W., Ong, J. E.-C., and
Phua, J. (2022). Authentically fake? how consumers respond to the influence of virtual
influencers.Journal of Advertising, 52(4):540–557.
[Mairesse et al., 2007]Mairesse, F., Walker, M. A., Mehl, M. R., and Moore, R. K.
(2007). Usinglinguisticcuesfortheautomaticrecognitionofpersonalityinconversation
and text. InJournal of Artificial Intelligence Research, volume 30, pages 457–500.
[Pasquier et al., 1999]Pasquier, N., Bastide, Y., Taouil, R., and Lakhal, L. (1999).
Discovering frequent closed itemsets for association rules. InProceedings of the 7th
International Conference on Database Theory (ICDT 1999), pages 398–416. Springer.
[Poelmans et al., 2013]Poelmans, J., Kuznetsov, S. O., Ignatov, D. I., and Dedene, G.
(2013). Formal concept analysis in knowledge processing: A survey on models and
techniques.Expert Systems with Applications, 40(16):6601–6623.
[Sands et al., 2022]Sands, S., Ferraro, C., Campbell, C., and Kietzmann, J. (2022). Un-
real influence: Leveraging AI in influencer marketing.European Journal of Marketing,
56(6):1721–1747.
[Stumme et al., 2002]Stumme, G., Taouil, R., Bastide, Y., Pasquier, N., and Lakhal,
L. (2002). Computing iceberg concept lattices with TITANIC.Data & Knowledge
Engineering, 42(2):189–222.

24 S. Chaudhry et al.
[Xie-Carson et al., 2024]Xie-Carson, L., Benckendorff, P., and Hughes, K. (2024). Keep
it #unreal: Exploring instagram users’ engagement with virtual influencers in tourism
contexts.Journal of Hospitality & Tourism Research, 48(6):1006–1019.
[Yan et al., 2024]Yan, J., Xia, S., Jiang, A., and Lin, Z. (2024). The effect of different
types of virtual influencers on consumers’ emotional attachment.Journal of Business
Research, 177:114646.
