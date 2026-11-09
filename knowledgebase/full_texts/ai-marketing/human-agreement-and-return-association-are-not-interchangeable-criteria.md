---
title: Human Agreement and Return Association Are Not Interchangeable Criteria
url: https://arxiv.org/abs/2609.11144
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- AS Aravinthakshan
- Laven Srivastava
- Harsh Nandwani
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.11144
pages: 14
chars: 54445
fetched_at: '2026-11-08T13:21:46+00:00'
kb_version: 1
---

# Human Agreement and Return Association Are Not Interchangeable Criteria

Human Agreement and Return Association Are Not Interchangeable
Criteria
AS Aravinthakshan
Manipal Institute of Technology
Perssonify
Laven Srivastava
Perssonify
Harsh Nandwani
Perssonify
research@perssonify.com
Abstract
Financial NLP has a standard workflow: val-
idate a sentiment tool against human labels,
then trust it to extract market signal. This as-
sumes the two evaluations measure the same
thing. We test that assumption in a set-
ting where both can be measured at once:
a corpus of securities class actions (2002–
2025) linking 70,500 X 1 messages to abnor-
mal stock returns, with a single-annotator hu-
man labelled gold sample. Running five in-
struments (V ADER, Loughran–McDonald, Fin-
BERT, Twitter-RoBERTa, and an LLM annota-
tor) through one identical pipeline, we find that
the relationship between construct and predic-
tive validity depends on the sampling conven-
tion and score representation. Under conven-
tional method-specific sampling, human agree-
ment aligns more closely with graded same-
day associations than with one-day leads. On a
fixed-n panel, however, agreement has similar
graded rank correlations at both horizons, while
the coarse ordering remains weak. Benchmark
agreement therefore establishes semantic valid-
ity but does not by itself determine predictive
rankings. In a conversation that is 17.6% spam,
message volume predicts neither market dam-
age nor settlement size.
1 Introduction
Sentiment instruments are validated in natural lan-
guage processing the way classifiers are generally
validated: by agreement with human annotation on
a labeled sample. In finance, they are used for a
different purpose, to capture a signal that is associ-
ated with, and ideally precedes, movements in asset
prices. These two criteria are routinely treated as
though the first implied the second. An instrument
that scores well on a sentiment benchmark is as-
sumed to be the better instrument for market signal
extraction. That assumption is rarely tested, be-
cause the two evaluations are normally conducted
1formerly Twitter
on different corpora, human labeled benchmarks
carry no market outcomes and market datasets carry
no human labels.
This paper tests the assumption directly: We con-
struct a corpus in which the same messages carry
both. Securities class actions provide the linkage:
court complaints supply event anchors and litiga-
tion metadata, the defendant’s price history sup-
plies abnormal returns, and the surrounding social
media conversation supplies text that we annotate
both automatically, with five instruments, and man-
ually, on a gold sample. All instruments use the
same aggregation and testing procedures. We com-
pare both method-specific samples and a shared set
of days, since the days retained can also affect the
results.
The domain is deliberately adverse; corrective
disclosures and filings generate genuine investor
discussion, but also plaintiff firm solicitation, re-
peated news headlines, and automated promotion.
The solicitation is structural, the PSLRA requires
the first filing plaintiff to publish notice inviting
other investors to seek lead plaintiff appointment,
so every case mechanically produces a burst of law
firm press releases (Choi et al., 2024). Headline
repetition is a known feature of financial news (Tet-
lock, 2011), and bots piggyback the cashtags of
newsworthy firms to promote unrelated securities
(Cresci et al., 2019). Spam is 17.6% of our cor-
pus, and solicitation and spam together account
for 25,166 messages. Counting is therefore a poor
measure by construction: a count absorbs all of
these sources equally. We ask three questions.
• RQ1.Does agreement with human sentiment
judgments predict the strength of an instru-
ment’s association with abnormal returns?
• RQ2.If agreement and association diverge,
at what horizon do they diverge, and what are
the instruments responding to?
arXiv:2609.11144v2  [cs.AI]  24 Sep 2026

• RQ3.Which conclusions about litigation dis-
course are invariant to the choice of instru-
ment, and which are not?
Our contributions are as follows.
1. A dual validity corpus, released.We release
66,890 event anchored messages across 845
securities class actions (2002–2025), carry-
ing five instrument sentiment labels and multi
axis LLM annotation, anchored by a 400 mes-
sage human gold standard with its codebook
and agreement statistics; to our knowledge,
the first public financial social media corpus
in which the same messages carry human
annotation and linked market outcomes, so
both validities can be measured through one
pipeline.2
2. A sampling dependent relationship be-
tween the two validities.Under con-
ventional method-specific sampling, human
agreement aligns more closely with graded
same-day associations than with one-day
leads. On the fixed- n panel, the graded or-
dering is similar at both horizons, whereas the
coarse ordering remains weak. The relation-
ship between construct and predictive validity
therefore depends on horizon, representation,
and the treatment of zero-score days.
3. Mechanism, and instability of instrument
rankings.Under conventional method-
specific sampling, the instrument with the
largest one-day point estimate is pretrained
on financial news; news accounts carry the
strongest attributed signal (ρ=−0.261 ), and
the local-projection placebo fails at negative
horizons.
4. Domain result and informative nulls.Con-
tent is informative where volume is not, de-
spite systematic pollution; message volume
predicts neither the depth of the price decline
nor dollar settlement size.
2 Related Work
Content and volume in financial discourse.
The distinction between what market participants
say and how much they post originates in the mes-
sage board literature: Tumarkin and Whitelaw
2https://bit.ly/4iSUf6d
(2001) find little return information in posting ac-
tivity, while Antweiler and Frank (2004) show
that messagecontentcarries signal where volume
mainly predicts volatility, and Das and Chen (2007)
build the first purpose made sentiment classifier for
stock talk. Media pessimism predicts market ac-
tivity (Tetlock, 2007), firm level language predicts
fundamentals (Tetlock et al., 2008), and the con-
tent of crowd-sourced investment opinions predicts
returns and earnings surprises (Chen et al., 2014).
Message volume is one member of a family of
attention measures that includes search intensity
(Da et al., 2011) and the attention driven trading it
induces (Barber and Odean, 2008). We treat this
content over volume regularity as established and
use it as a domain check; the paper’s claim con-
cerns how the instruments that measure content
should be evaluated.
Sentiment instruments and their benchmark
evaluation.The instruments we compare span
the standard toolkit: a social media lexicon (Hutto
and Gilbert, 2014), a finance dictionary (Loughran
and McDonald, 2011), and transformers pretrained
on financial news (Araci, 2019) and on tweets (Bar-
bieri et al., 2020). Such instruments are standardly
evaluated by agreement with human annotation,
with Financial PhraseBank (Malo et al., 2014) the
reference benchmark; recent suites extend the same
paradigm to financial large language models (Xie
et al., 2023, 2024), making the question of what
agreement predicts downstream more consequen-
tial, not less. Loughran and McDonald (2016)
argue that measurement choices dominate down-
stream conclusions; our results give that argument
a sharp form: the choice between two validated
instruments changes which temporal conclusions
are recoverable.
Intrinsic versus extrinsic evaluation.The dis-
tinction we draw between agreement with human
labels and association with outcomes is the psycho-
metric distinction between construct and predictive
validity (Cronbach and Meehl, 1955), and it has an
NLP precedent: intrinsic evaluations of word repre-
sentations fail to predict extrinsic task performance
(Chiu et al., 2016), and measurement-theoretic cri-
tiques argue that NLP systems routinely opera-
tionalise constructs without testing what the opera-
tionalisation measures (Jacobs and Wallach, 2021).
To our knowledge the two evaluations have not
previously been conducted on the same financial
messages with linked market outcomes, which is

what permits the horizon localised comparison in
Section 7.
LLMs in financial text.Large language mod-
els extract return relevant signal from headlines
(Lopez-Lira and Tang, 2023) and outperform trans-
former and dictionary sentiment in trading settings
(Kirtac and Germano, 2024); LLM annotation can
match or exceed crowd workers (Gilardi et al.,
2023). Two caveats shape our design: LLM senti-
ment can embed look ahead information from the
pretraining window (Glasserman and Lin, 2023),
motivating the contamination analysis of Section 9,
with chronologically consistent training the pro-
posed remedy (He et al., 2025).
Social media, returns, and securities litigation.
Relations between social media mood and mar-
ket movement are established (Bollen et al., 2011;
Sprenger et al., 2014; Ranco et al., 2015), as is the
link from investor disagreement to trading volume
(Cookson and Niessner, 2020); class action event
studies measure shareholder wealth effects, litiga-
tion risk, and reputational penalties without social
media text (Gande and Lewis, 2009; Kim and Skin-
ner, 2012; Karpoff et al., 2008). Our setting differs
in being event anchored by court filings, carrying
eventual legal outcomes, and evaluating the mea-
surement instruments themselves rather than any
one instrument’s signal. The press is a documented
fraud detection channel (Miller, 2006; Dyck et al.,
2010), consistent with our attribution result that
news accounts carry the strongest price relevant
signal and with the news arrival reading of the lead-
ing component.
3 Corpus and Annotation
3.1 Corpus construction
The corpus contains 845 securities class actions
in three cohorts (Table 1): prospective 2024 and
2025 cohorts and a retrospective archive of re-
solved cases from 2002–2021. Court filings supply
company identity, class period bounds, corrective
disclosure dates, allegation summaries, defendants,
and litigation metadata. Filings are ingested from
PDF and converted to structured records. High
value fields (company name, ticker, class period
bounds, defendants, and disclosure dates) receive
an independent extraction pass, and disagreements
are manually reconciled. These dates define the
message retrieval and event windows.
Cohort Cases Ticker Stock Social Msgs.
2024 204 204 162 56 15,984
2025 182 180 154 51 10,178
Archive 459 305 180 161 44,338
Total 845 689 496 268 70,500
Table 1: Corpus by cohort. “Social” counts cases with
collected messages; “Msgs.” counts annotated mes-
sages.
3.2 Composition of the conversation
The label distributions in this subsection are pro-
duced by the LLM instrument described in Sec-
tion 3.4. The relevance, topic, and polarity tax-
onomies are closed sets fixed in the annotation
prompt, which is released with the code and data.
Of 70,500 messages, 62.0% are relevant, 20.3%
tangential, and 17.6% spam. The largest top-
ics are news reporting (13,880), law firm solici-
tation (12,901), automated spam (12,265), legal
procedure (9,658), equity analysis (8,055), and di-
rect fraud allegations (7,835). Polarity is 41.0%
negative and 7.2% positive. Relevance and po-
larity agree substantially with human annotation
(κ= 0.746 and 0.741; Section 3.5), while the topic
taxonomy is not separately validated and is there-
fore used descriptively only.
A count based attention measure aggregates in-
formative reporting, investor reaction, solicitation,
and automation into a single number, motivating
the comparison in Section 5.
3.3 Event and market linkage
Messages are assigned to a pre class period base-
line, the alleged class period, the corrective disclo-
sure window, and post disclosure and post filing
windows, retaining text, timestamp, impressions,
and likes where available. For company i on day
t, let Ri,t denote the realised return and Rm,t the
market return. A market model
Ri,t =α i +β iRm,t +ϵ i,t (1)
is estimated over the 120 trading days ending ten
days before the class period begins, so the parame-
ters are fitted on pre event data only. Theabnormal
returnis the part of the day’s return the market does
not explain,
ARi,t =R i,t −

ˆαi + ˆβiRm,t  ,(2)
and thecumulative abnormal returnover an event
windowWis its sum,CAR i = P t∈W ARi,t.

3.4 Scoring instruments
Five instruments score message sentiment:
V ADER, a social media lexicon (Hutto and Gilbert,
2014); Loughran–McDonald, a finance dictionary
(Loughran and McDonald, 2011); FinBERT and
Twitter-RoBERTa, transformers pretrained on
financial news and on tweets (Araci, 2019; Barbieri
et al., 2020); and Claude Haiku, an LLM annotator.
The instruments produce different outputs, so we
derive coarse and graded negativity scores, with
higher values indicating more negative sentiment.
Thecoarsescore discards magnitude. Each
message is assigned to one of three classes and
mapped to {+1,0,−1} with +1 negative, using
the predicted class for the transformers and the
LLM, and the sign of the score for the lexicons.
Thegradedscore keeps magnitude, oriented so
that larger is more negative: the negated V ADER
compound score, the Loughran–McDonald
net-negative word ratio, p(neg)−p(pos) for the
transformers, and the negated −2 to +2 intensity
label for the LLM.
Both scores are averaged over the messages for
each case day. All instruments use the same ag-
gregation and tests, but the conventional samples
differ because zero-score days are excluded sepa-
rately for each instrument. Section 7.1 repeats the
comparison on a shared set of days.
3.5 Construct validity
We assess agreement with human judgment on a
gold set of 400 messages, labelled by a single an-
notator blind to all model outputs and presented in
randomised order. Messages were drawn by strat-
ified random sampling across predicted relevance
× polarity × cohort (26 strata); inverse probability
weighted accuracy (0.861 polarity, 0.860 relevance)
matches the unweighted estimates, so stratification
does not drive the reported agreement.
Table 2 reports polarity agreement for all five
instruments. We report Cohen’s κ (Cohen, 1960)
alongside accuracy because the corpus is 41.0%
negative and 7.2% positive, so an instrument that
predicts the majority class attains substantial ac-
curacy while carrying no information. FinBERT
is precisely this case: accuracy 0.538 with κ=
0.079. Under conventional benchmarks (Landis
and Koch, 1977) only the LLM instrument reaches
substantial agreement; Twitter-RoBERTa is mod-
erate, Loughran–McDonald fair, and FinBERT in-
distinguishable from chance. V ADER’s accuracy
Instrument Accuracy Macro-F1κ
Claude Haiku 0.860 [0.825, 0.893] 0.878 0.741
RoBERTa 0.733 [0.693, 0.778] 0.594 0.449
LM 0.553 [0.508, 0.598] 0.446 0.210
FinBERT 0.538 [0.490, 0.588] 0.379 0.079
V ADER 0.385 [0.338, 0.438] 0.373 0.171
Table 2: Polarity agreement with human gold labels on
the same 400 messages. Brackets give 95% bootstrap
intervals from 1,000 resamples (Efron and Tibshirani,
1993). LM denotes Loughran–McDonald; RoBERTa
denotes Twitter-RoBERTa.
is below the majority class rate.
The LLM instrument’s polarity errors concen-
trate at the negative neutral boundary and are di-
rectionally one sided: it labels human neutral mes-
sages negative in 49 of 56 disagreements, so LLM
derived negativity is if anything slightly inflated.
On relevance it achieves 0.860 accuracy, 0.797
macro-F1, and κ= 0.746 . This evaluation mea-
sures agreement with the intended linguistic con-
structs; it makes no claim about association with
returns, which is the subject of the next two sec-
tions.
4 Empirical Setup
We report Spearman ρ for monotonic associations,
which is robust to the heavy tails of daily returns.
Daily analyses pool case days; cross sectional anal-
yses collapse each case to one observation. Sig-
nificance markers are ∗∗∗p <0.001, ∗∗p <0.01,
∗p <0.05, †p <0.1. New baseline families use
Benjamini–Hochberg FDR adjustment (Benjamini
and Hochberg, 1995). Because the daily panel is
large, statistical significance is easily attained; we
therefore compare instruments on effect size and
treat p-values as evidence only that an association
is nonzero.
Timing proceeds from descriptive to conditional
tests. Lead lag correlations compare sentiment
on t−ℓ with ARt. Order two Granger tests ask
whether lagged sentiment improves prediction be-
yond return history (Granger, 1969). A distributed
lag model,
ARi,t =
3X
k=0
βksi,t−k +η i +u i,t,(3)
uses case fixed effects and case clustered standard
errors (Petersen, 2009). Local projections (Jordà,
2005) estimate ARi,t+h on si,t for h∈[−5,5] ,
with negative horizons serving as a placebo. These

tests establish predictive precedence, not structural
causation. Between-instrument differences in ρ
are not directly tested; comparisons of their magni-
tudes are therefore descriptive point-estimate com-
parisons, and significance for one instrument but
not another does not establish a significant differ-
ence between them.
The panel contains 179 cases and 103,542 case
days.3 The conventional correlation sample drops
days on which a method emits zero, so n differs by
method; Section 7.1 reports a common day inter-
section in whichnis held fixed.
5 Predictive Validity: Content versus
Counting
At case level, attention does not track damage. In
the 2025 cohort, total message volume is uncor-
related with the worst single-day abnormal return
(ρ=−0.083 , p= 0.60 , n= 43 ) and with CAR
(ρ= +0.003,p= 0.99,n= 36).
The daily panel establishes the comparison pre-
cisely (Table 3, summarised in Figure 1). Tweet
volume reaches ρ=−0.0311 . Every sentiment
family contains a representation with a larger as-
sociation, and the strongest instruments exceed
volume by a factor of two to three. Loughran–
McDonald coarse (0.80×) is the single exception,
so the claim applies to method families rather than
to every threshold choice. Impressions, the natural
reach based count, are not significant at all.
Two features of this table matter for what follows.
First, the strongest same day instrument is Twitter
RoBERTa, not the LLM, so the content over count-
ing result does not depend on the LLM annotation.
Second, the p-values are not comparable across
rows: RoBERTa graded attains p= 5.27×10 −18
on 12,910 case days while FinBERT coarse attains
p= 1.87×10 −6 on 5,056, and the difference is
largely sample size. We compare the ρ column
throughout.
6 Temporal Structure
Table 4 reports lead lag correlations. Every in-
strument shows a negative and significant same
day association, so the contemporaneous result
of Section 5 is not instrument specific. Under
3The panel was re fetched because the original price series
were unavailable. Of 273 archive tickers, 74 no longer re-
solve. Published values reproduce within |∆ρ| ≤0.002, with
identical signs and significance ordering. All cross method
comparisons use the refreshed same data panel.
Metricρ p n×vol.
Counts
Tweet volume−0.0311 ∗∗∗ 4.14×10−4 12,9101.00×
Impressions−0.0317 † 0.06343,4391.02×
Negative count−0.0380 ∗ 0.01354,2191.22×
Lexicons
V ADER c.−0.0454 ∗∗∗ 8.86×10−6 9,5661.46×
V ADER g.−0.0454 ∗∗∗ 3.78×10−6 10,3391.46×
LM c.−0.0249 ∗ 0.04146,7130.80×
LM g.−0.0559 ∗∗∗ 3.60×10−6 6,8711.80×
Transformers
FinBERT c.−0.0670 ∗∗∗ 1.87×10−6 5,0562.16×
FinBERT g.−0.0526 ∗∗∗ 2.29×10−9 12,9101.69×
RoBERTa c.−0.0967 ∗∗∗ 7.91×10−9 3,5453.11×
RoBERTa g.−0.0760 ∗∗∗ 5.27×10−18 12,9102.45×
LLM instrument
Claude c.−0.0822 ∗∗∗ 5.77×10−9 5,0002.65×
Claude g.−0.0821 ∗∗∗ 6.12×10−9 5,0042.64×
Table 3: Same day correlation with the daily abnormal
return. LM denotes Loughran–McDonald; RoBERTa
denotes Twitter-RoBERTa; c. and g. denote coarse and
graded scores.×vol. is|ρ|relative to tweet volume.
Methodρ 0 ρ1 q1 ρ2
V ADER c.−0.0454 ∗∗∗ −0.01360.286+0.0025
V ADER g.−0.0454 ∗∗∗ −0.0193∗ 0.100−0.0034
LM c.−0.0249 ∗ −0.00570.810+0.0168
LM g.−0.0559 ∗∗∗ −0.0263∗ 0.067−0.0057
FinBERT c.−0.0670 ∗∗∗ −0.0466∗∗∗ 0.003+0.0010
FinBERT g.−0.0526 ∗∗∗ −0.0292∗∗∗ 0.003−0.0022
RoBERTa c.−0.0967 ∗∗∗ −0.00580.879+0.0010
RoBERTa g.−0.0760 ∗∗∗ −0.0272∗∗ 0.006−0.0202 ∗
Claude c.−0.0822 ∗∗∗ −0.0227—−0.0022
Claude g.−0.0821 ∗∗∗ −0.0376∗∗ —−0.0373 ∗∗
Table 4: Lead lag correlations, all messages; c. and g.
denote coarse and graded scores;n per row as in Table 3.
q values are FDR adjusted across the baseline family;
the pre existing LLM reference is not included in that
correction.
the conventional method-specific nonzero-day sam-
ples, the one-day results differ across instruments.
FinBERT coarse has the largest ℓ= 1 point esti-
mate (−0.0466, pFDR = 0.003); FinBERT graded
and Twitter-RoBERTa graded also survive FDR,
whereas V ADER and Loughran–McDonald do not.
At ℓ= 2 , Claude graded and Twitter-RoBERTa
graded are significant at the unadjusted 5% level.
These comparisons describe point estimates and
do not establish statistically significant differences
between instruments.
Conditional tests give the same picture.
Four baseline specifications survive FDR on
forward Granger tests: Loughran–McDonald
coarse/relevant ( F= 4.388 , q= 0.034 ),
Loughran–McDonald graded/all (F= 4.056 , q=

Figure 1: Content over volume across scoring instruments. Panel (a) shows the strongest same day representation in
each method family; n differs because the conventional analysis drops method specific zero days. Panel (b) uses the
identical 134 cases for event minus baseline sentiment shift versus CAR. Bars report exact ρ values without treating
any instrument as the contribution.
0.040), FinBERT coarse/relevant ( F= 3.907 ,
q= 0.044 ), and FinBERT graded/all (F= 4.316 ,
q= 0.034 ). The LLM reference also passes (F=
5.435, p= 0.0051 coarse/all). Twitter-RoBERTa
never survives, despite having the strongest same
day association. Same day distributed lag coeffi-
cients are negative and significant for almost every
instrument; their magnitudes are not comparable
across instruments because the underlying signals
differ in scale. Full results appear in Appendix B.
7 Where the Two Validities Diverge
Sections 3.5 and 6 measure two different properties
of the same five instruments on the same corpus:
agreement with human judgment, and association
with abnormal returns. Table 5 places them side by
side. This is the paper’s central comparison, and it
is not visible from either table in isolation.
Conventional samples show contemporaneous
alignment. For the graded representation in Table 5,
the ordering by human agreement closely matches
the ordering by same-day association: the rank cor-
relation is +0.90 with κ and +1.00 with accuracy.
Thus, under this representation and the conven-
tional method-specific sampling rule, benchmark
agreement is informative about contemporaneous
association.
The one-day relationship is weaker and depends
on the score representation. For graded scores,
the rank correlations are +0.40 with κ and +0.70
with accuracy; for coarse scores, they are −0.30
and −0.10. Under conventional sampling, Fin-
BERT has the strongest coarse one-day association
(ρ1 =−0.0466 ) despite its low human agreement;
Claude’s corresponding value is −0.0227. Sec-
tion 7.1 shows how these rankings change when all
instruments are evaluated on the same case-day set.
Interpretation.Table 4 shows a horizon contrast
under the conventional, method-specific samples,
but Table 6 shows that this contrast is not invari-
ant to sample construction or score representation.
On the fixed- n graded panel, agreement has the
same rank correlation with association at ℓ= 0
and ℓ= 1 ; on the coarse panel, both relationships
are weak. We therefore make the narrower claim
that benchmark agreement does not, by itself, de-
termine predictive rankings, and that comparisons
should be reported with the horizon, representation,
and zero-day inclusion rule explicitly stated.
7.1 Instrument rankings are unstable
The conventional analysis drops case days on
which a given method emits zero, so n differs
across instruments in Tables 3 and 4 and the com-
parison is not made on identical data. Table 6 re-
stricts to case days on which every instrument emits
a nonzero score, holdingnfixed.
Applying the Table 5 rank comparison to the
fixed-n panels gives correlations with κ of +0.00
and +0.10 for coarse scores at ℓ= 0 and 1, and
+0.80 at both horizons for graded scores. The cor-
responding values for accuracy and macro-F1 are
+0.40 and +0.20 for coarse scores, and +0.90 at
both graded horizons. The exact two-sided permu-
tation p-values are 1.000, 0.950, 0.133, and 0.133
for κ, and 0.517, 0.783, 0.083, and 0.083 for ac-
curacy and macro-F1, respectively. None of these
correlations survives BH adjustment within the 12
fixed-nconstruct–predictive comparisons.

Construct validity Predictive validity (|ρ|)
InstrumentκAccuracy Macro-F1 coarseρ 0 coarseρ 1 gradedρ 0 gradedρ 1
Claude Haiku 0.741 0.860 0.878 0.0822 0.02270.0821 0.0376
Twitter-RoBERTa 0.449 0.733 0.5940.09670.0058 0.0760 0.0272
Loughran–McDonald 0.210 0.553 0.446 0.0249 0.0057 0.0559 0.0263
V ADER 0.171 0.385 0.373 0.0454 0.0136 0.0454 0.0193
FinBERT 0.079 0.538 0.379 0.06700.04660.0526 0.0292
Rank correlation withκ+0.50−0.30 +0.90 † +0.40
Rank correlation with accuracy+0.60−0.10 +1.00 ∗ +0.70
Table 5: Construct validity from Table 2 joined to predictive validity from Tables 3 and 4, ordered by κ. On
conventional method-specific nonzero-day samples, human-agreement rankings align most closely with graded
same-day association and less consistently with the one-day lead. Rank correlations are Spearman correlations over
five instruments, with exact two-sided p-values from all 120 permutations. These comparisons are descriptive, and
no cell survives adjustment for the 12 comparisons in this table. The corresponding fixed-n comparison is reported
in Table 6 and Section 7.1.
Methodρ 0 ρ1 ρ2
Coarse, all messages(n= 1,518)
Claude−0.0851 ∗∗∗ −0.0323−0.0101
V ADER−0.0068−0.0165 +0.0300
LM−0.0460 † −0.0501† −0.0333
FinBERT−0.1259 ∗∗∗ −0.0315−0.0116
RoBERTa−0.0667 ∗∗ −0.0073−0.0030
Graded, all messages(n= 3,890)
Claude−0.0696 ∗∗∗ −0.0438∗∗ −0.0467∗∗
V ADER−0.0288 † −0.0173 +0.0081
LM−0.0411 ∗ −0.0339∗ −0.0035
FinBERT−0.0385 ∗ −0.0297† +0.0215
RoBERTa−0.0723 ∗∗∗ −0.0561∗∗∗ −0.0189
Table 6: Common-case-day intersection, all messages.
Relevant-message panels appear in Appendix C.
Three observations follow. First, the same day
ranking reverses: on the coarse common days Fin-
BERT is strongest (−0.1259), where the conven-
tional sample placed Twitter-RoBERTa first. Sec-
ond, V ADER is indistinguishable from zero on
common days, so its apparent advantage in Ta-
ble 3 was substantially a matter of which days
it scored. Third, several sentiment measures re-
main associated with returns on the shared days,
although the strongest instrument changes. Table 6
does not compare sentiment with volume on those
same days, so it does not establish that the content-
over-counting result is unchanged. Claims about
the strongest instrument therefore need to specify
the sample used.
7.2 Divergence at the case level
A cross sectional test reproduces the divergence in
a different form. For each case we compute the
event minus baseline change in mean negativity
and correlate it with the event window CAR (Ta-
Instrumentρ p q
Claude Haiku−0.3106 ∗∗∗ 0.0003 —
FinBERT−0.1961 ∗ 0.0231 0.185
Twitter-RoBERTa−0.1651 † 0.0566 0.226
Loughran–McDonald−0.08190.3470 0.596
V ADER−0.06630.4466 0.596
Table 7: Event-minus-baseline change in the share of
negative messages versus CAR, using the same 134
cases for all instruments and including all messages.
ble 7). The LLM instrument attains ρ=−0.3106
(p= 0.0003 , n= 134 ), several times any daily
panel effect. No baseline survives FDR correc-
tion: FinBERT reaches −0.1961 (p= 0.0231 )
but q= 0.185 , and Twitter-RoBERTa −0.1651
(p= 0.0566 ). The case level shift is a contempo-
raneous contrast between two windows rather than
a lead, so the ℓ= 0 pattern of Table 5 would pre-
dict the best agreeing instrument to perform well
here, which it does. We do not press that reading
further, for two reasons. With n= 134 and five
instruments the comparison is underpowered, so
the ordering among the baselines is not resolvable;
and the result is sensitive to how the case level
measure is constructed. Substituting mean window
negativity for negative share, on a reconstruction of
the panel, raises Loughran–McDonald and Twitter-
RoBERTa to the same range as the LLM instrument.
The robust content of this table is that a case level
contrast exists and is several times larger than any
daily panel effect; the identity of the strongest in-
strument at this level is not established. Restricting
to relevant messages reduces the sample to n= 50
and renders every instrument nonsignificant.

8 What the Leading Signal Responds To
Section 7 shows that the relationship between con-
struct validity and the one-day lead depends on
the sampling convention and score representation.
Two pieces of evidence bear on what the observed
leading associations reflect.
The largest conventional-sample lead is pro-
duced by an instrument trained on news.Fin-
BERT is pretrained on financial news and evaluated
on sentence-level news sentiment. On tweets about
securities fraud, it agrees with human polarity at
close to chance, yet its coarse score has the largest
one-day point estimate under conventional method-
specific sampling. The natural reading is that it
detects the vocabulary of adverse financial news
rather than the polarity of investor expression, and
that this vocabulary arrives shortly before the price
adjustment completes.
News accounts carry the strongest signal.We
classify accounts from topic mix, cross-case activ-
ity, and spam fraction. News accounts have the
strongest association ( ρ=−0.261 , p <0.001 ),
followed by cross-case broadcasters ( −0.161),
other multi-case accounts (−0.115), and retail ac-
counts (−0.083). The associations for bot/spam ac-
counts (+0.064) and law firm solicitation (+0.040)
are not significant. The strongest observed sig-
nal therefore comes from news accounts, while
these two sources of additional volume show no
detectable association with returns.
9 Robustness
Look ahead contamination.The archive cohort
(2002–2021) lies inside the LLM’s pretraining win-
dow, so its results could in principle reflect recog-
nition of publicised cases rather than message level
reading (Glasserman and Lin, 2023). The base-
lines provide a control: the two dictionaries have
no training window at all, and the two transform-
ers were pretrained without these outcome labels.
Contamination would therefore show up as an
LLM advantage that is larger in the archive than
in the 2024–2025 cohorts. On the daily panel
it is not. Across 1,000 case level bootstrap re-
samples, the archive minus recent difference in
the LLM’s advantage is +0.0091 (graded, same
day; 95% CI [−0.027,+0.046] ), −0.0013 (graded,
one day lag; CI [−0.047,+0.052] ), +0.0061 and
+0.0017 (coarse). Every interval includes zero.
The LLM’s own association is also similar across
cohorts (−0.081 in the archive and −0.090 in the
recent cohorts). These results do not reveal a clear
difference between cohorts, but they do not rule
out contamination. The LLM’s own association
is stable across cohorts ( −0.081 archive, −0.090
recent). We retain the archive for the daily analy-
ses. The case level measure of Section 7.2 is less
settled: split by cohort (80 archive, 47 recent), the
LLM’s advantage is larger in the archive the direc-
tion contamination predicts. The subsample is too
small to treat as evidence either way, so the paper
rests its claims on the daily panel and reports the
case level result as corroborative (decomposition
in Appendix D).
Relevance filtering.Restricting to relevant mes-
sages shifts same day correlations by at most
0.0164; the central result is present on all mes-
sages. Since the relevance labels come from the
LLM instrument, this removes a circularity concern
(Appendix A).
Attention and legal materiality.Among 133
resolved cases with settlements, total message
volume is uncorrelated with settlement amount
(ρ=−0.041 , p= 0.64 ), as are relevant message
(−0.062) and negative message (−0.093) volume;
median settlements do not differ across volume ter-
tiles (H= 0.83 , p= 0.66 ). Public attention is
orthogonal to legal materiality, as it was to price
damage depth.
10 Discussion and Conclusion
We introduce a corpus linking 845 securities class
actions to 70,500 event-anchored messages, pairing
a 400-message single-annotator human reference
sample with abnormal-return series linked to the
messages. Evaluating five instruments through one
pipeline, we find that the relationship between hu-
man agreement and return association is sensitive
to sampling and representation. On conventional
method-specific samples, human agreement closely
orders graded contemporaneous associations but
not one-day leads; on the fixed- n panel, graded
rankings are similar at both horizons, while coarse
rankings remain weak.
Agreement with human labels is therefore evi-
dence of semantic validity, not a sufficient basis
for selecting an instrument for predictive use. Con-
struct and predictive validity should be reported
together with the horizon, score representation, and
zero-day inclusion rule.

The account-level results and the failed placebo
are consistent with a leading signal that partly
reflects news arrival. The daily-panel compari-
son finds no clear archive-recent difference in the
LLM’s relative advantage, but does not rule out
contamination. The domain result stands: in a
conversation that is 17.6% spam, content informs
where counting does not, and volume predicts nei-
ther the depth of the price decline nor the size of
the eventual settlement. The contribution is an
evaluation design and a measurement result, not a
classifier.
Limitations
Human validation covers polarity and relevance
but not intensity, emotion, severity, or topic, and it
reflects agreement with a single careful annotator
rather than inter annotator reliability; no human
to human agreement figure is available, so the κ
values in Table 2 have no measured ceiling.
The rank comparisons are based on five instru-
ments and are therefore descriptive. Under conven-
tional method-specific sampling, human agreement
aligns more closely with graded same-day asso-
ciations than with one-day leads. We therefore
conclude only that benchmark agreement does not
by itself determine predictive rankings and that
the sampling convention and score representation
must accompany such comparisons. Widening the
instrument battery is a natural next step.
FinBERT’s low agreement is partly attributable
to domain shift: it was tuned on Financial Phrase-
Bank sentences rather than on tweets. We regard
this as consistent with, rather than an alternative
to, our reading, since practitioners apply it off the
shelf to exactly this kind of text; but it means that
κ= 0.079 should be read as agreement in deploy-
ment rather than as an intrinsic property of the
model.
Account types are behavioural rather than pro-
file derived. Relevance filtered case level windows
become sparse ( n falls from 134 to 50). Reach
weighted variants have been evaluated only for the
LLM instrument. Timing tests establish predic-
tive precedence rather than structural causality or
tradeability, and the local projection placebo fails
at negative horizons. Effect sizes throughout are
small.
The corpus is specific to securities-class-action
discourse, where solicitation, repeated headlines,
and cashtag piggybacking are unusually prevalent.
Although the evaluation design is portable, whether
the observed relationships generalize to ordinary
stock discussion requires cross-domain validation.
In addition, 74 of 273 archive tickers no
longer resolve through the original price API. If
unresolved symbols disproportionately represent
delisted firms, their absence from the refreshed
price panel may truncate the adverse-return tail
and attenuate estimated negative associations. The
reported return relationships should therefore be
interpreted subject to this potential survivorship
bias.
Ethics Statement
The corpus consists of public X/Twitter posts col-
lected via the platform API. No author profile
lookups were performed; account categories are
derived solely from posting behaviour, and all at-
tribution results are reported at the aggregate class
level. No personally identifying information is in-
cluded in released artifacts. Court filings are public
records. In accordance with the platform’s devel-
oper terms, the released artifact contains message
identifiers and our annotations rather than message
text, together with a script for retrieving text from
the platform.
Data and Code Availability
The provided archive contains the classification
prompts and configuration, the 400 message gold
annotation file, message identifiers with all model
and human labels, per instrument daily sentiment
series, the computed abnormal return panel, and
analysis code sufficient to reproduce every table.
The abnormal return panel is included directly be-
cause 74 of 273 archive tickers no longer resolve
through the original price API.
Acknowledgements
We extend our gratitude to Perssonify LLC. for
their continued support of our work, and allocating
resources that made this work possible. In particu-
lar we thank Stefan Persson for his valuable inputs
and guidance.
References
Werner Antweiler and Murray Z. Frank. 2004. Is all
that talk just noise? The information content of inter-
net stock message boards.The Journal of Finance,
59(3):1259–1294.

Dogu Araci. 2019. FinBERT: Financial sentiment analy-
sis with pre-trained language models.arXiv preprint
arXiv:1908.10063.
Brad M. Barber and Terrance Odean. 2008. All that
glitters: The effect of attention and news on the buy-
ing behavior of individual and institutional investors.
Review of Financial Studies, 21(2):785–818.
Francesco Barbieri, Jose Camacho-Collados, Luis Es-
pinosa Anke, and Leonardo Neves. 2020. TweetEval:
Unified benchmark and comparative evaluation for
tweet classification. InFindings of the Association
for Computational Linguistics: EMNLP 2020, pages
1644–1650.
Yoav Benjamini and Yosef Hochberg. 1995. Controlling
the false discovery rate: A practical and powerful
approach to multiple testing.Journal of the Royal
Statistical Society: Series B, 57(1):289–300.
Johan Bollen, Huina Mao, and Xiaojun Zeng. 2011.
Twitter mood predicts the stock market.Journal of
Computational Science, 2(1):1–8.
Hailiang Chen, Prabuddha De, Yu (Jeffrey) Hu, and
Byoung-Hyoun Hwang. 2014. Wisdom of crowds:
The value of stock opinions transmitted through so-
cial media.Review of Financial Studies, 27(5):1367–
1403.
Billy Chiu, Anna Korhonen, and Sampo Pyysalo. 2016.
Intrinsic evaluation of word vectors fails to predict
extrinsic performance. InProceedings of the 1st
Workshop on Evaluating V ector-Space Representa-
tions for NLP (RepEval), pages 1–6.
Stephen J. Choi, Jessica Erickson, and A. C. Pritchard.
2024. The business of securities class action lawyer-
ing.Indiana Law Journal, 99(3).
Jacob Cohen. 1960. A coefficient of agreement for
nominal scales.Educational and Psychological Mea-
surement, 20(1):37–46.
J. Anthony Cookson and Marina Niessner. 2020. Why
don’t we agree? Evidence from a social network of
investors.The Journal of Finance, 75(1):173–228.
Stefano Cresci, Fabrizio Lillo, Daniele Regoli, Serena
Tardelli, and Maurizio Tesconi. 2019. Cashtag piggy-
backing: Uncovering spam and bot activity in stock
microblogs on Twitter.ACM Transactions on the
Web, 13(2):1–27.
Lee J. Cronbach and Paul E. Meehl. 1955. Construct va-
lidity in psychological tests.Psychological Bulletin,
52(4):281–302.
Zhi Da, Joseph Engelberg, and Pengjie Gao. 2011.
In search of attention.The Journal of Finance,
66(5):1461–1499.
Sanjiv R. Das and Mike Y . Chen. 2007. Yahoo! for
Amazon: Sentiment extraction from small talk on the
web.Management Science, 53(9):1375–1388.
Alexander Dyck, Adair Morse, and Luigi Zingales.
2010. Who blows the whistle on corporate fraud?
The Journal of Finance, 65(6):2213–2253.
Bradley Efron and Robert J. Tibshirani. 1993.An Intro-
duction to the Bootstrap. Chapman & Hall.
Amar Gande and Craig M. Lewis. 2009. Shareholder-
initiated class action lawsuits: Shareholder wealth
effects and industry spillovers.Journal of Financial
and Quantitative Analysis, 44(4):823–850.
Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli.
2023. ChatGPT outperforms crowd workers for
text-annotation tasks.Proceedings of the National
Academy of Sciences, 120(30):e2305016120.
Paul Glasserman and Caden Lin. 2023. Assessing
look-ahead bias in stock return predictions gener-
ated by large language models.arXiv preprint
arXiv:2309.17322.
Clive W. J. Granger. 1969. Investigating causal relations
by econometric models and cross-spectral methods.
Econometrica, 37(3):424–438.
Songrun He, Linying Lv, Asaf Manela, and Jimmy Wu.
2025. Chronologically consistent large language
models.arXiv preprint arXiv:2502.21206.
C. J. Hutto and Eric Gilbert. 2014. V ADER: A parsi-
monious rule-based model for sentiment analysis of
social media text. InProceedings of the Eighth In-
ternational AAAI Conference on Weblogs and Social
Media, pages 216–225.
Abigail Z. Jacobs and Hanna Wallach. 2021. Measure-
ment and fairness. InProceedings of the 2021 ACM
Conference on Fairness, Accountability, and Trans-
parency, pages 375–385.
Òscar Jordà. 2005. Estimation and inference of impulse
responses by local projections.American Economic
Review, 95(1):161–182.
Jonathan M. Karpoff, D. Scott Lee, and Gerald S.
Martin. 2008. The cost to firms of cooking the
books.Journal of Financial and Quantitative Analy-
sis, 43(3):581–611.
Irene Kim and Douglas J. Skinner. 2012. Measuring
securities litigation risk.Journal of Accounting and
Economics, 53(1–2):290–310.
Kemal Kirtac and Guido Germano. 2024. Sentiment
trading with large language models.arXiv preprint
arXiv:2412.19245.
J. Richard Landis and Gary G. Koch. 1977. The mea-
surement of observer agreement for categorical data.
Biometrics, 33(1):159–174.
Alejandro Lopez-Lira and Yuehua Tang. 2023. Can
ChatGPT forecast stock price movements? Return
predictability and large language models.arXiv
preprint arXiv:2304.07619.

Tim Loughran and Bill McDonald. 2011. When is a
liability not a liability? Textual analysis, dictionaries,
and 10-Ks.The Journal of Finance, 66(1):35–65.
Tim Loughran and Bill McDonald. 2016. Textual anal-
ysis in accounting and finance: A survey.Journal of
Accounting Research, 54(4):1187–1230.
Pekka Malo, Ankur Sinha, Pekka Korhonen, Jyrki Wal-
lenius, and Pyry Takala. 2014. Good debt or bad
debt: Detecting semantic orientations in economic
texts.Journal of the Association for Information
Science and Technology, 65(4):782–796.
Gregory S. Miller. 2006. The press as a watchdog for
accounting fraud.Journal of Accounting Research,
44(5):1001–1033.
Mitchell A. Petersen. 2009. Estimating standard errors
in finance panel data sets: Comparing approaches.
Review of Financial Studies, 22(1):435–480.
Gabriele Ranco, Darko Aleksovski, Guido Caldarelli,
Miha Grˇcar, and Igor Mozetiˇc. 2015. The effects of
Twitter sentiment on stock price returns.PLOS ONE,
10(9):e0138441.
Timm O. Sprenger, Andranik Tumasjan, Philipp G.
Sandner, and Isabell M. Welpe. 2014. Tweets and
trades: The information content of stock microblogs.
European Financial Management, 20(5):926–957.
Paul C. Tetlock. 2007. Giving content to investor sen-
timent: The role of media in the stock market.The
Journal of Finance, 62(3):1139–1168.
Paul C. Tetlock. 2011. All the news that’s fit to reprint:
Do investors react to stale information?The Review
of Financial Studies, 24(5):1481–1512.
Paul C. Tetlock, Maytal Saar-Tsechansky, and Sofus
Macskassy. 2008. More than words: Quantifying lan-
guage to measure firms’ fundamentals.The Journal
of Finance, 63(3):1437–1467.
Robert Tumarkin and Robert F. Whitelaw. 2001. News
or noise? Internet postings and stock prices.Finan-
cial Analysts Journal, 57(3):41–51.
Qianqian Xie, Weiguang Han, Zhengyu Chen, Ruoyu
Xiang, Xiao Zhang, Sophia Ananiadou, Jimin Huang,
et al. 2024. FinBen: A holistic financial benchmark
for large language models. InAdvances in Neural
Information Processing Systems 37 (Datasets and
Benchmarks Track).
Qianqian Xie, Weiguang Han, Xiao Zhang, Yanzhao
Lai, Min Peng, Alejandro Lopez-Lira, and Jimin
Huang. 2023. PIXIU: A comprehensive benchmark,
instruction dataset and large language model for fi-
nance. InAdvances in Neural Information Process-
ing Systems 36 (Datasets and Benchmarks Track).
Method Scoreρ 0 ρ1 q1 n
V ADER coarse−0.0464 ∗∗∗ −0.01950.268 5,071
graded−0.0417 ∗∗ −0.02190.194 5,502
LM coarse−0.0293 † −0.01600.415 4,302
graded−0.0425 ∗∗ −0.01890.306 4,372
FinBERT coarse−0.0834 ∗∗∗ −0.0457∗∗ 0.023 3,247
graded−0.0527 ∗∗∗ −0.0259∗ 0.088 6,167
RoBERTa coarse−0.0835 ∗∗∗ −0.00070.972 2,511
graded−0.0853 ∗∗∗ −0.0350∗∗ 0.016 6,167
Claude coarse−0.0866 ∗∗∗ −0.0239— 4,279
graded−0.0874 ∗∗∗ −0.0336∗ — 4,301
Table 8: Lead–lag correlations restricted to relevant mes-
sages. LM denotes Loughran–McDonald; RoBERTa
denotes Twitter-RoBERTa.q1 is FDR-adjusted across
the baseline family; the LLM reference is not included
in that correction (—). Significance as in Section 4.
Method Score All Relevant∆
Claude coarse−0.0822−0.0866−0.0044
graded−0.0821−0.0874−0.0053
V ADER coarse−0.0454−0.0464−0.0010
graded−0.0454−0.0417 +0.0037
LM coarse−0.0249−0.0293−0.0044
graded−0.0559−0.0425 +0.0134
FinBERT coarse−0.0670−0.0834−0.0164
graded−0.0526−0.0527−0.0002
RoBERTa coarse−0.0967−0.0835 +0.0132
graded−0.0760−0.0853−0.0093
Table 9: Effect of relevance filtering on the same-day
correlation.∆is relevant minus all.
A Relevance Filtering
Table 8 repeats the lead–lag analysis of Table 4 on
messages the LLM instrument labelsrelevant, and
Table 9 reports the change against the all-message
baseline. Filtering shifts the same-day correlation
by at most 0.0164 and never reverses a sign, so
the central result is not produced by the relevance
labels. This matters because those labels come
from one of the instruments under evaluation; if
the result depended on them the comparison would
be circular. At case level, filtering reduces the
common sample from 134 to 50 because windows
containing no relevant message become undefined,
and every instrument becomes nonsignificant.
B Forward-Granger and Distributed-Lag
Tests
Table 10 gives the complete battery summarised in
Section 6. Distributed-lag coefficients are not com-
parable across instruments because the underlying
signals differ in scale; only sign and significance
transfer.

Forward Granger Distributed lag
Method Score SampleF p q β 0 qβ
Claude coarse all5.435 ∗∗ 0.0051 —−0.0086 ∗∗∗ —
rel.7.888 ∗∗∗ 0.0005 —−0.0089 ∗∗∗ —
graded all3.909 ∗ 0.0218 —−0.0071 ∗∗∗ —
rel.4.717 ∗ 0.0101 —−0.0071 ∗∗∗ —
V ADER coarse all0.8700.4207 0.434−0.0016 ∗ 0.050
rel.2.406 † 0.0932 0.130−0.0020 † 0.133
graded all0.4470.6403 0.640−0.0035 ∗ 0.069
rel.0.8790.4169 0.434−0.00380.245
LM coarse all3.062 ∗ 0.0493 0.072−0.0043 ∗∗∗ <0.001
rel.4.388 ∗ 0.01390.034−0.0067 ∗∗∗ <0.001
graded all4.056 ∗ 0.01890.040−0.0895 ∗∗∗ <0.001
rel.3.265 ∗ 0.0406 0.065−0.1140 ∗∗∗ <0.001
FinBERT coarse all3.341 ∗ 0.0376 0.063−0.0049 ∗∗ 0.003
rel.3.907 ∗ 0.02190.044−0.0084 ∗∗∗ <0.001
graded all4.316 ∗ 0.01480.034−0.0062 ∗∗∗ 0.001
rel.3.466 ∗ 0.0335 0.059−0.0102 ∗∗∗ 0.001
RoBERTa coarse all2.1110.1242 0.159−0.0088 ∗∗∗ <0.001
rel.0.9440.3910 0.431−0.0106 ∗∗∗ <0.001
graded all1.5890.2069 0.245−0.0144 ∗∗∗ <0.001
rel.1.5340.2185 0.250−0.0166 ∗∗∗ <0.001
Table 10: Forward-Granger and distributed-lag results. Bold q marks the four specifications that survive FDR
correction. All-message rows use nF = 103,184 and nβ = 103,005; relevant-message rows use 99,328 and 99,157.
Coefficients are not comparable across instruments (see text). Significance as in Section 4.
Panel Methodρ 0 ρ1 ρ2
C/rel. Claude−0.0910 ∗∗∗ −0.0395−0.0288
V ADER+0.0084−0.0043 +0.0442
LM−0.0564 ∗ −0.0467† −0.0446
FinBERT−0.1417 ∗∗∗ −0.0357−0.0153
RoBERTa−0.0517 † +0.0105−0.0208
G/rel. Claude−0.0711 ∗∗∗ −0.0298† −0.0514∗∗
V ADER−0.0216−0.0098 +0.0109
LM−0.0357 ∗ −0.0154−0.0139
FinBERT−0.0295 † −0.0144 +0.0206
RoBERTa−0.0706 ∗∗∗ −0.0368∗ −0.0262
Table 11: Common case day intersection on relevant
messages. C and G denote coarse and graded; n=
1,328and3,295respectively.
C Common Day Intersection, Relevant
Messages
Table 6 in the main text holds n fixed across instru-
ments using all messages. Table 11 repeats that in-
tersection on relevant messages only. The reorder-
ing described in Section 7.1 persists: FinBERT is
strongest same day on the coarse panel and Twitter-
RoBERTa on the graded panel, while V ADER re-
mains indistinguishable from zero throughout.
D Look Ahead Contamination
Section 9 reports the headline contamination test.
This appendix gives the decomposition. Table 12
reports the difference in differences against each
baseline separately rather than against their mean,
so the null is not an artifact of averaging: all sixteen
estimates lie between −0.0400 and +0.0281 and
every interval spans zero.
Within the archive cohort, splitting at the median
case year gives an LLM advantage of +0.0395 for
older cases against +0.0363 for newer ones on the
coarse same day measure, and +0.0153 against
+0.0127 at a one day lag. The advantage is slightly
larger for older cases, but the differences are small.
This comparison alone does not establish contami-
nation.
We are more cautious about the case level mea-
sure. Splitting that test by cohort leaves 80 archive
and 47 recent cases, and on a reconstruction of the
panel the LLM’s advantage is larger in the archive
than in the recent cohorts, which is the direction
contamination predicts. The subsample is small
and we do not treat this as evidence of contamina-
tion, but the daily panel null does not extend to it,
which is why the paper rests its claims on the daily
panel.

Repr. vs baseline DiD (ℓ= 0) DiD (ℓ= 1)
coarse FinBERT+0.0175 +0.0281
Loughran–McDonald−0.0170−0.0400
Twitter-RoBERTa+0.0035 +0.0078
V ADER+0.0202 +0.0111
graded FinBERT+0.0044 +0.0134
Loughran–McDonald−0.0156−0.0277
Twitter-RoBERTa+0.0221 +0.0066
V ADER+0.0254 +0.0026
Table 12: Per baseline difference in differences. Each
cell is the LLM’s |ρ| advantage over that baseline in the
archive cohort minus the same advantage in the 2024–
2025 cohorts. No estimate is distinguishable from zero
at 95% over 1,000 case level bootstrap resamples.
E Retained Null Results
For completeness: the fear/panic/outrageshareis
insignificant at every lag, while its daily count is
not; several event window specifications lose sig-
nificance once firm and sector controls are added;
relevance filtering does not create the daily result;
the filtered case level measure becomes sparse and
nonsignificant; negative horizon local projections
limit causal interpretation and total, relevant, and
negative message volume all fail to predict settle-
ment size or case level price damage depth.
F Event Validation and Local Projections
Mean negative message share rises from 11.8% in
the baseline window to 46.7% in the disclosure
window (n= 184 , paired t= 10.97 , p <10−21),
confirming that the complaint derived disclosure
dates coincide with an information shock rather
than background chatter. With controls for log mar-
ket capitalisation, class period length, defendant
count, and sector, class period negative share pre-
dicts maximum drawdown ( n= 41 , t=−3.24 ,
p= 0.003, adjustedR 2 = 0.60).
Local projections (Figure 2, bottom) peak at
h= 0 (β=−0.0079 , p <0.001), remain signifi-
cant at h= 1 (β=−0.0022 , p <0.05), and are
indistinguishable from zero by h= 2 . Coefficients
at negative horizons are also significantly nega-
tive, and a reverse next-day correlation is present
(ρ=−0.046,p <0.01).
G Rank Correlations Between the Two
Validities
Table 13 gives every correlation between a con-
struct validity measure and a predictive validity
column, completing Table 5. With five instruments
Figure 2: Top: the complaint derived disclosure window
is a sharp negativity shock. Bottom: local projection
coefficients peak contemporaneously and decay after
one day; the significantly negative coefficients at nega-
tive horizons are a failed placebo and caution against a
causal interpretation.
the asymptotic p-values reported by standard soft-
ware are unreliable, so we compute exact two sided
p-values by enumerating all 5! = 120 permuta-
tions.
coarse graded
Measure|ρ 0| |ρ 1| |ρ 0| |ρ 1|
κ+0.50−0.30 +0.90 +0.40
(0.450) (0.683) (0.083) (0.517)
Accuracy+0.60−0.10 +1.00 +0.70
(0.350) (0.950) (0.017) (0.233)
Macro-F1+0.60−0.10 +1.00 +0.70
(0.350) (0.950) (0.017) (0.233)
Table 13: Spearman rank correlation between each con-
struct validity measure and each predictive validity col-
umn, over the five instruments. Exact two sidedp-values
from all 120 permutations in parentheses. Accuracy and
macro-F1 give identical values because they order the
five instruments identically. Only the graded same day
column is nominally significant, and no cell survives
adjustment for twelve comparisons.
Across all three agreement measures, the closest
alignment is with graded same-day associations.
At one day, the relationship is weaker for graded
scores and weakly negative for coarse scores. None
of the twelve comparisons survives multiple-testing

Figure 3: Target Corporation over its class period. Top: daily closing price. Bottom: messages per day, coloured by
the share of negative messages. Negative-heavy days concentrate around the major price declines.
correction. With only five instruments, we treat
these patterns as descriptive.
H Case Study: Target Corporation
A large cap example shows the mechanism: Fig-
ure 3 overlays Target Corporation’s stock price
with its daily message volume coloured by neg-
ative share over the class period. Days on which
more than half the messages are negative cluster
around the two largest price declines, while low
negativity days dominate the calm stretches and
carry little price information. Messagevolumeis
similar in negative and quiet periods; it is the clas-
sified sentiment that lines up with the moves. The
case illustrates at the single case level the domain
result of Section 5.
