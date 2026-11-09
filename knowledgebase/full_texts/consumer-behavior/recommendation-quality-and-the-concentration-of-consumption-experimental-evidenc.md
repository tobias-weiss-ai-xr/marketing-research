---
title: 'Recommendation Quality and the Concentration of Consumption: Experimental Evidence from Netflix'
url: https://arxiv.org/abs/2608.21274
category: consumer-behavior
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Guy Aridor
- Winston Chou
- Nathan Kallus
- Antoine Scheid
- Allen Tren
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.21274
pages: 29
chars: 73225
fetched_at: '2026-11-08T13:01:36+00:00'
kb_version: 1
---

# Recommendation Quality and the Concentration of Consumption: Experimental Evidence from Netflix

Recommendation Quality and the Concentration of Consumption:
Experimental Evidence from Netflix ∗
Guy Aridor Winston Chou Nathan Kallus
Antoine Scheid Allen Tran Kevin Zielnicki
August 24, 2026
Abstract
We study an experiment with 8.5 million users on Netflix’s recommender system to measure how
improvements in recommendation technology affect the set of products that get consumed. Improvements
increase total consumption and users’ reliance on recommendations while diffusing recommendations and
consumption away from the most popular titles (“superstars”) toward a larger number of moderately
popular titles (“middle-tail”), with minimal effects on the most niche titles (“long-tail”). Our results
challenge the notion that recommender systems polarize consumption – raising the consumption shares
of the head and tail at the expense of the middle – and suggest that the returns to investing in middle-tail
products grow as algorithms improve and platforms scale.
∗Contact: Aridor: Netflix and Northwestern Kellogg, garidor@netflix.com. Chou: Netflix, wchou@netflix.com. Kallus:
Netflix and Cornell University and Cornell Tech, nkallus@netflix.com. Scheid: Netflix, ascheid@netflix.com. Tran: Netflix,
atran@netflix.com, Zielnicki: Netflix, kzielnicki@netflix.com. All authors were employed at Netflix during the duration of this
project. We thank Rafael Jim´ enez-Dur´ an and Malika Korganbekova for helpful feedback and suggestions. We thank audiences
at AI Algorithms and Markets Symposium (LUISS), Cornell Johnson, Conference on AI and Human Decisions (CMU), and
Research Roundtable on Platform Dynamics (Northwestern) for helpful comments. All errors are our own.
arXiv:2608.21274v1  [econ.GN]  21 Aug 2026

1 Introduction
Recommender systems (RecSys), ubiquitous in the digital economy, use historical interaction data to connect
users with relevant products (Resnick and Varian, 1997). Their efficacy depends on extracting meaningful
signals about consumer preferences from limited data. As this technology has improved, it has reshaped
which products are consumed, with a large literature debating whether it concentrates consumption among
the most popular products or spreads it across a long tail of niche products (Brynjolfsson et al., 2003;
Salganik et al., 2006; Fleder and Hosanagar, 2009; Calvano et al., 2025), with the products in the middle
losing share to the extremes (Bar-Isaac et al., 2012). However, the state-of-the-art algorithms have improved
dramatically over the past several decades – from item-based collaborative filtering algorithms (Sarwar et al.,
2001), to matrix factorization techniques (Bennett and Lanning, 2007; Koren et al., 2009), to deep learning-
based recommenders (He et al., 2017), and, more recently, to sequence and foundation models (Quadrana
et al., 2018; Zhao et al., 2024; Hsiao et al., 2025). These improvements continuously expand the frontier of
goods that a RecSys can effectively target, yet the implications of these improvements for the concentration
of consumption remain unknown.
This paper studies how improvements to recommendations reshape viewership using a unique experiment
on Netflix’s RecSys involving more than 8.5 million subscribers. The experiment, a “long-term holdback,”
compares a frozen algorithm with an evolving production treatment incorporating all algorithmic innovations
deployed during a 60-day experimental period. We find that ongoing improvements to the RecSys increase
overall engagement on the platform and users’ reliance on the recommendations for plays, primarily by shift-
ing the recommendations – and subsequently plays – away from the most popular titles (“superstars”) and
toward moderately popular titles (“middle-tail”), with minimal effects on the long-tail. As recommendation
technology matures, then, the plausible set of targetable titles continues to shift toward the middle-tail.
We argue that these results are consistent with a stylized model in which algorithmic improvements
allow the RecSys to better infer consumer preferences from a fixed amount of title-level interaction data.
Since less popular titles generate fewer interactions, the model captures this data constraint as a tendency
for the RecSys to default toward popular titles when preference signals for less popular titles are weak. 1
Improvements in recommendation technology attenuate this bias by allowing the RecSys to identify relevant
titles with less data. The gains are largest for middle-tail titles: unlike superstars, they are not already
reliably matched, and unlike long-tail titles, they generate enough data and command a large enough audience
for better inference to matter. Improvements therefore shift recommendations toward these better-matched
titles, raising overall engagement.
This paper contributes to a long-standing literature on how digitization has reshaped the types of goods
that get consumed (Goldfarb and Tucker, 2019), and in particular to conflicting findings on whether rec-
ommendation systems concentrate or disperse consumption. Several early studies document that online
consumption shifted away from popular titles (Brynjolfsson et al., 2003; Zentner et al., 2013), with a dra-
matic increase in the number of new products brought to market and substantial welfare gains (Waldfogel,
2017; Aguiar and Waldfogel, 2018; Reimers and Waldfogel, 2026). Experimental evidence comparing per-
sonalized recommendations to non-personalized benchmarks similarly finds that personalization can increase
engagement while dispersing aggregate consumption across products (Holtz et al., 2020). On the other hand,
these technologies reduce search costs and thus concentrate consumption among superstars (Rosen, 1981)
1The microfoundation for this assumption comes from the literature in recommender systems documenting apopularity bias
– an inherent tendency of deployed algorithms to favor popular titles because they learn from interaction data, which popular
titles generate far more of (Celma and Cano, 2008; Abdollahpouri et al., 2017; Klimashevskaia et al., 2024).
1

and polarize the product distribution at the expense of middle-tail titles (Bar-Isaac et al., 2012). Empirically,
Salganik et al. (2006) shows that popularity information can increase superstar concentration, while Fleder
and Hosanagar (2009) and Calvano et al. (2025) show that popularity bias in classic RecSys algorithms can
concentrate aggregate consumption on popular products.
These distributional effects are not fixed properties of recommendation systems. Tucker and Zhang
(2011) show that popularity information reinforces superstar concentration under homogeneous preferences
but can benefit niche products when preferences are heterogeneous. Our contribution is to identify a second,
dynamic dimension – algorithm maturity and the volume of title-level interaction data – that changes which
titles benefit as recommendation quality improves. 2 In our empirical context, Zielnicki et al. (2026) show
using a structural model that previous RecSys improvements lift engagement by better identifying users with
high incremental consumption from recommendations, and that this value is largest for middle-tail titles.
We provide experimental evidence that continued improvements to the RecSys further shift consumption
toward precisely this part of the distribution: away from superstars and toward middle-tail titles, while
lifting engagement overall.
These findings have important implications for online platforms. By identifying which titles become more
targetable as recommendation quality improves, our results speak to the frontier of products that benefit
the most from algorithmic recommendation. In particular, continued improvements in recommendation
technology mainly amplify products whose audiences can be reached through better targeting, but whose
demand is difficult to realize under less mature systems or platforms with limited scale. This interpretation
echoes supply-side evidence that digitization and streaming have increasingly supported middle-tail products:
Benner and Waldfogel (2023) document the sustainable production of medium-budget “middle-tail” films,
while L¨ uke (2025) finds that middle-tail books are overrepresented in online bookstores relative to brick-
and-mortar retailers.
2 Conceptual Model
To tie together our empirical findings on the effects of improving recommendation technology, we provide a
stylized conceptual model.
2.1 Setup
We consider a representative useriwhose true utility from consuming titlejis given by:
Uij =µ j +θ ij,
whereµ j ∈Ris baseline popularity andθ ij is drawn i.i.d. across (i, j) with bounded, strictly positive
density onRand finite mean. Thus, each title’s utility is a combination of a vertical component (µ j) and a
horizontal, idiosyncratic component (θ ij), so a randomly selected user would be more likely to prefer a more
popular than a less popular title, but for some users a less popular title can provide higher utility.
We consider a stylized setup where there are three “representative” titles – long-tail (L), middle-tail (M),
2Tucker (2023) highlights that algorithmic systems systematically underserve those for whom interaction data are sparse –
in our context, this manifests as a built-in disadvantage for less popular titles, consistent with broader evidence of diminishing
returns to data (Bajari et al., 2019; Peukert et al., 2024). Our results show that this disadvantage is not permanent but
diminishes as the algorithm matures.
2

and superstar (S) – and the user consumes at most one title. 3 We assume thatµ L < µM < µS and that user
ihas a titlejthat provides the highest utility – we denote this byj ∗ i = arg maxj Uij. Under this formulation,
pj := Pr(j ∗ i =j)∈(0,1) denotes the probability that titlejis useri’s best title. Thus, the goal of the
RecSys is to identify this title.
User Choice.The representative user receives a singleton recommendationR i ⊂ {L, M, S}and chooses
from the three titles and an outside option. The user’s decision utilityVij is influenced by the recommendation
via a “utility bonus”b >0 that makes them more likely to consume the recommended title. The bonus
captures, in reduced form, the role of recommendations in reducing informational frictions (Aridor et al.,
2023; Zielnicki et al., 2026). The user’s decision utility for titlejis therefore given by:
Vij :=U ij +b·1{j∈ R i},
whereb >0. The user chooses the title with the highest decision utility or the outside option (normalized
toV i0 = 0), and we write the choice asc i = argmaxj∈{0,S,L,M} Vij.4
Platform Recommendation T echnology .The platform’s recommendation technology is indexed by a
single parameterδand we make the following assumptions about it.
Assumption 1(Recommendation Technology).The RecSys attempts to identify the user’s best title with a
classifier whose accuracy is summarized by the indexδ. We assume:
•Popularity default.Conditional onj ∗ i =jand the user’s full utility, the recommender identifiesj
with probabilityq j(δ)and otherwise outputsS(i.e., for useri,Pr(R i ={j} |Ui, j⋆ i =j) =q j(δ)).
•Monotonicity.The functionsq L, qM are differentiable and weakly increasing inδ.
•Middle-tail dominance.Over the empirically relevant range ofδ, the marginal precision gain is
largest for the middle-tail:p M q′ M (δ)> p L q′ L(δ)≥0.
The primary justification for this assumption comes from thepopularity biaswidely documented in the
recommendation systems literature (Celma and Cano, 2008; Klimashevskaia et al., 2024), by which deployed
algorithms over-recommend popular titles because less popular titles generate too little data to extract a
reliable signal. Appendix C motivates the assumption with a Bayesian recommender that generates this bias
endogenously and shows the popularity bias and, over the relevant range ofδ, that the weighted identification
gainp jq′ j(δ) is largest for the middle-tail: the superstar’sq ′ S(δ) is small, since it is already well targeted, and
while the long-tail’sq ′ L(δ) may be sizeable, too few users rank it first for the identification gain to matter.
2.2 Empirical Predictions
Our experimental intervention involves an increase in the effectiveness of recommendation technology (δ) and
we characterize directional predictions from this change, holding all other parameters fixed. Each prediction
relies on Assumption 1 with proofs deferred to Appendix B. 5
3While the treatment can, in principle, shift the popularity distribution, we validate in Appendix Figure A.1 that the
treatment in our empirical context is incremental enough that it does not dramatically change the title classification.
4We assume that, as our experiment is conducted over 60 days, the experimental intervention only changeswhichtitles
enter intoR i and not how users internalize the signal provided by the recommendations. Thus, the value ofbremains constant
throughout the experiment.
5The empirical measures and predictions are those that are derived from our theory – they are not the core product metrics
that Netflix optimizes for.
3

The first natural consequence of the improvement in recommendation technology is that it shifts rec-
ommendation share away from the popularity default and to the tail of the distribution. We define the
recommendation probabilityf j(δ) := Pr(j∈ Ri(δ)) and characterize how it changes:
Prediction 1(Hump-shaped recommendations).An increase inδresults in a hump-shaped redistribution
of recommendation share with the largest gains for the middle-tail (M):f ′ M (δ)> f ′ L(δ)> f ′ S(δ).
Intuitively, Prediction 1 follows since some users preferMtoS, but the platform observes too noisy
of a signal forθ iM in order to recommendMoverS. Increasingδprovides additional precision for the
platform’s estimated score for titleM, leading to an increased fraction of users who preferMto receive it
in the recommendations instead ofS. A similar pattern holds for users who preferL, but the magnitude
is smaller since the popularity gap betweenLandSis bigger and the signal is still noisy even after the
technology improvement.
If recommendations change (Prediction 1) and recommendations matter for choice (b >0), then nat-
urally consumption should shift to the newly recommended titles. We denoteπ j(δ) := Pr(c i =j) as the
consumption probability for titlejand characterize how it changes across the three titles:
Prediction 2(Play Share Rotation).An increase inδshifts consumption from the superstars to the middle-
tail and long-tail:π ′ M (δ)>0andπ ′ L(δ)≥0, whileπ ′ S(δ)<0.
Predictions 1 and 2 establish that recommendations and consumption shift toward the middle-tail, but
redistribution alone does not reveal whether users are better served: an algorithm could diversify recommen-
dations across the middle-tail without those being titles users want to consume (Chen et al., 2024). The key
test is whether the redistribution raises overallengagement– the likelihood that a user does not take the
outside option – since users consume the newly recommended titles only if they prefer them to the outside
option:
Prediction 3(Engagement Levels).An increase inδincreases total engagement:Pr(c i ̸= 0)is strictly
increasing inδ.
The main force behind this prediction is that some users who preferredMorLoverSwere previously
recommendedSdue to the popularity bias, which led them to consume nothing; as the RecSys shifts to their
preferred title, they consume it and the outside-option share falls. Because this newly realized consumption
comes from the recommended title, the share of consumption originating from recommendations should rise
as well:
Prediction 4(Share of Plays from Recommendation).An increase inδresults in a larger share of con-
sumption originating from recommendations:Pr(c i ∈ Ri |c i ̸= 0)is strictly increasing inδ.
Finally, it is important to understand whether, conditional on consumption, the improved recommen-
dations lead users to better-matched titles. This is theoretically ambiguous in our model as there are
two counteracting forces:inframarginal switchingmay increase average match quality if the improved rec-
ommendations shift a user’s consumption fromSto their preferred title, butextensive-margin entrymay
decrease average match quality by inducing users who would otherwise consume the outside option to con-
sume marginal titles. This leads to our final prediction (which is formally stated in Appendix B), which
ultimately will be an empirical question to understand which force wins out:
Prediction 5(Match Quality).An increase inδresults in weakly better average match quality if and only
if the match-quality gains from inframarginal switching weakly exceed the composition effect from extensive-
margin entry.
4

3 Data and Field Experiment
Figure 1: Netflix Homepage
Data and Empirical Setting.Our empirical context is the video-streaming platform Netflix. Users pay
a subscription fee to access Netflix and can then costlessly play any title on the platform. We therefore
operationalize consumption in our empirical context as playing a title, and define engagement as the overall
volume of consumption. The set of titles consists of television shows (which have multiple episodes and
seasons) and movies. The platform’s homepage – which is personalized to each user – is shown in Figure
1. Users can directly play titles from the recommendations (defined as titles on the homepage), continue
watching titles they had started before, or manually search for titles using the search bar. Our analysis uses
platform data on plays and recommendations for each user in the experiment.
Field Experiment.To evaluate the empirical implications of our model, we analyze an experiment on
Netflix on 8,559,252 subscribers over a 60-day period from February to April 2025. This experiment was
designed as a “cumulative holdback” test to measure the collective impact of multiple innovations to person-
alization algorithms during this period. The control arm of the experiment corresponds to the state of the
recommendation system prior to the start of the test, whereas the treatment arm corresponds to the “pro-
duction” state of Netflix that is experienced by the majority of Netflix members and continuously updated
during the test as new innovations (e.g., algorithmic updates) are released. These releases are held back
from the control group, which continues to experience the pre-experiment version of the recommendation
system. Such holdback tests are run periodically on a small fraction of the Netflix member base in order to
measure long-term progress on personalization (Kohavi et al., 2020).
The algorithmic innovations deployed during the experiment encompass twelve major changes spanning
roughly four categories: dedicated rankers for specific homepage rows, feature engineering, revised model
5

architectures such as modeling certain outcomes jointly rather than independently, and different model
weights on prediction targets. Most were deployed near the start of the intervention, with a smaller number
released closer to the end. These innovations are purely algorithmic and do not change the user interface,
thus map to increases inδin the language of our model.
This experiment represents an ideal testing ground for our model for several reasons. First, the treatment
includes all innovations made to personalization algorithms during the experiment timeframe. As such, it
is broadly representative of ongoing efforts to improve personalized recommendations at Netflix. Second,
because each subrelease is individually A/B tested and chosen based on evidence of a better member expe-
rience, we can be highly confident that the treatment represents a significant improvement to personalized
recommendations. Lastly, the relatively long duration of the experiment helps us confirm that the following
impacts are stable and persistent.
4 Distributional Shifts in Recommendations and Plays
In this section we characterize thedistributionalshifts as a result of the technology increase by first exploring
its impact on the distribution of recommendations (Section 4.1) and then its subsequent impact on the
distribution of played titles (Section 4.2).
A key challenge is measuring distributional impacts without letting our intervention contaminate the
play distribution itself. Unfortunately, as the environment is dynamic with many titles entering and exiting
the platform, pre-experimental shares are not representative of shares during the experiment. As such, we
partition titles into the same buckets as in the conceptual model and assign them based on their percentile
on the aggregate play distribution across the treatment and control groups: “long-tail” (L), “middle-tail”
(M), or “superstar” (S) buckets – where “superstar” is defined as the top 5 percentile, the “long-tail” as the
bottom 50 percentile, and the “middle-tail” as the set of titles in between. 6
Our primary specification measures how treatment reallocates a user’s recommendations and plays across
title buckets. Letc o ik be the total number of instances for outcomeofor a given useriand titles in bucket
k. The outcome of interest is the within-user shares o ik =c o ik/ P k′ co ik′ for users with at least one outcome.
We estimate, separately for each outcomeoand each bucketk:
so ik =α o k +β o k Ti +ε o ik,(1)
whereT i is an indicator for useribeing assigned to the treatment arm,α o k is the mean share in the control
andβ o k is the average treatment effect on that share. We compute robust standard errors.
4.1 Recommendations Shift to the Middle-Tail
The first implication of an increase in the efficacy of recommendation technology, as stated in Prediction 1,
is that recommendations redistribute away from superstars toward the middle-tail, with minimal effects on
the long-tail. We test this by estimating specification (1) on the recommendations users observe during the
experiment for each of the title buckets{L, M, S}.
Figure 2a confirms the hump shape predicted by Prediction 1: recommendation share shifts away from
superstar titles and primarily gets redirected to middle-tail titles, with quantitatively small changes to the
6While the treatment can influence the empirical popularity distribution, we empirically confirm in Figure A.1 that these
buckets remain similar between our treatment and control groups.
6

Figure 2: Treatment Effects on Recommendation Shares
Long Tail Middle Tail Superstar
Title Bucket
−0.010
−0.005
0.000
0.005
0.010
Treatment Effect
(a) Shares by Bucket
0-5 5-10 10-15 15-20 20-25 25-30 30-35 35-40 40-45 45-50 50-55 55-60 60-65 65-70 70-75 75-80 80-85 85-90 90-95 95-100
Title Play Percentile Bin
−0.010
−0.005
0.000
0.005
0.010
Treatment Effect
Middle Tail Starts
Superstar Starts (b) Shares by Ventile Bins
HHI
−6%
−4%
−2%
0%
2%
4%
6%
Relative Treatment Effect
 (c) HHI
Notes: Estimated Average Treatment Effects (ATEs) on the distribution of recommendations. Panel (a) presents coefficient
estimates from (1) with the dependent variable of the share of an individual’s recommendations accounted for by each bucket.
Panel (b) presents treatment effects on recommendation share within each pooled ventile, where the ventiles are defined using
the pooled play distribution across the treatment and control groups. Panel (c) presents coefficient estimates for the changes
in the recommendations HHI, where we compute standard errors using a delete-one jackknife. Bars denote 95% confidence
intervals.
long-tail. Figure 2b shows that this same pattern persists using more granular ventile buckets and Appendix
Figure A.3 shows that these patterns replicate when we take the most conservative approach of defining the
percentiles purely in terms of the play percentile in the control group. 7
An important consequence of this redistribution is that it shifts recommendation share from a small
number of superstar titles and disperses it to a large number of middle-tail titles that are better fits for
users. As such, the shift to the middle-tail should decrease the amount of concentration in recommendations
across users. We estimate the effects of the technology improvement on the Herfindahl–Hirschman Index
(HHI = PN j=1 s2 j ) – a standard measure for the degree of concentration that we compute at the title level –
to test this. Figure 2c confirms that HHI has a statistically and economically significant decrease of 5.7%.
4.2 Plays Shift to the Middle-Tail
A natural implication of the shift in the distribution of recommendations is that it may also shift the
distribution of plays. As shown in our conceptual model, plays depend on the title’s recommendation
probabilityandthe probability that the user follows the recommendation. If the RecSys diversified the
recommendations by replacing superstar titles with middle-tail titles that were not appealing, then users
could still seek out the superstars via search or decide not to play anything on the platform at all, leading to
minimal differences in the play share. Prediction 2 indicates that play share shifts if the recommendations
are sufficiently consequential in user choices (i.e.,b >0).
We test Prediction 2 by estimating specification (1) for each title bucket, reporting the estimates in
Figure 3a. The results confirm the prediction: superstar play share falls with most of the redistribution
going to the middle-tail, with the long-tail quantitatively unchanged. Figure 3b shows that this same
pattern persists using more granular ventile buckets and Appendix Figure A.5 shows that these patterns
replicate when we take the most conservative approach of defining the percentiles purely in terms of the play
7Appendix Figure A.2 additionally shows that within the superstars the effect is most stark for the highest percentile.
7

Figure 3: Treatment Effects on Play Shares
Long Tail Middle Tail Superstar
Title Bucket
−0.006
−0.004
−0.002
0.000
0.002
0.004
0.006
Treatment Effect
(a) Shares by Bucket
0-5 5-10 10-15 15-20 20-25 25-30 30-35 35-40 40-45 45-50 50-55 55-60 60-65 65-70 70-75 75-80 80-85 85-90 90-95 95-100
Title Play Percentile Bin
−0.006
−0.004
−0.002
0.000
0.002
0.004
0.006
Treatment Effect
Middle Tail Starts
Superstar Starts (b) Shares by Ventile Bins
HHI
−1.5%
−1.0%
−0.5%
0.0%
0.5%
1.0%
1.5%
Relative Treatment Effect
 (c) HHI
Notes: Estimated ATEs on the distribution of title plays during the experiment. Panel (a) presents coefficient estimates from
specification (1) with the dependent variable of the share of an individual’s plays accounted for by each bucket. Panel (b)
presents treatment effects on play share for each pooled ventile, where ventiles are defined using the pooled play distribution
across the treatment and control groups. Panel (c) presents coefficient estimates for the changes in the Herfindahl-Hirschman
Index of plays, where we compute standard errors using a delete-one jackknife. Bars denote 95% confidence intervals.
percentile in the control group. 8
Finally, we measure whether this corresponds to a reduction in play concentration: Figure 3c shows that
HHI falls by a statistically and economically significant 1.2%, consistent with viewership dispersing from
superstar titles to more personalized middle-tail titles.
5 Engagement Levels and Match Quality
While the results in Section 4 document that both recommendations and plays shift toward the middle-tail
and subsequently become less concentrated, the key test of whether this shift is a “technological improve-
ment” is if these distributional shifts translate into a corresponding improvement in the consumer experience
that is driven by the recommendations. We assess this in this section by first characterizing whether and
why the improvement leads to an increase in theoverall levelof engagement (Section 5.1) and then assessing
whether the played titles had similar match quality (Section 5.2).
For most of this analysis, we compareuser-leveloutcomes across the experimental period and estimate
average treatment effects using the following regression:
Yi =α+β T i +ε i,(2)
with similar notation as before and compute robust standard errors.
5.1 Overall Engagement and Recommendation Dependence
The simple conceptual model from Section 2 predicts that the recommendations should be more relevant
to consumers, inducing increased engagement (Prediction 3) that is driven by increased play share coming
from the recommendations (Prediction 4). In this section, we test these predictions.
8Appendix Figure A.4 additionally shows that within the superstars the effect is most stark for the highest percentile.
8

Figure 4: Treatment Effects on Overall Engagement
View Hours Overall Plays Days with Play Distinct Titles Played
0.0%
0.5%
1.0%
1.5%
Relative Treatment Effect
Notes: Estimated ATEs from (2) on account-level engagement outcomes: view hours, overall plays, days with at least one
play, and distinct titles played. All effects are reported as relative percent change against the control mean. Bars denote 95%
confidence intervals computed via robust standard errors.
Figure 4 presents the estimates ofβfrom (2) across four different measures of engagement: total view
hours, number of plays, the number of days with at least one play, and the number of distinct titles played.
The results confirm Prediction 3: view hours increased by 0.37%, the total number of titles played by 0.62%,
the distinct number of titles played by 1.2%, and the number of days with at least one play by 0.21%. 9,10
As context for the magnitudes, Zielnicki et al. (2026) estimate via a structural model that reverting to the
predominant RecSys algorithm from 10 years ago (matrix factorization) would reduce days with a play by
4%, with economic effects comparable to those of reverting from matrix factorization to popularity-based
ranking (then valued at more than$1 billion by Gomez-Uribe and Hunt (2015)). Our estimate of the effects
of roughly two months of algorithmic innovation – a 0.21% increase in days with a play – represents about
5% of this magnitude. Crucially, it implies that the shift away from superstars documented in Section 4 is
not diversification for diversification’s sake, but actually coincides with improved engagement.
The intuition from our conceptual model forwhythe improvement leads to an increase in overall en-
gagement is simple: the RecSys replaces less well-matched superstars with better matched middle-tail titles
which results in users being more likely to find content to play from the recommender system. In our empir-
ical context, we can validate this by measuring whether the reliance on the recommendations for generating
plays increases – which is the crux of Prediction 4.
To test Prediction 4, we restrict focus to the first play per session in order to rule out effects coming
from continuation play and classify each play as either coming from recommendations, manual search, play
continuation, or previously saved (e.g., my list). We then estimate (2) for the ratio of plays to visits,
the share of plays that originate from recommendations, and the mean reciprocal rank (MRR) of plays. 11
9For television shows, total and distinct title counts can diverge, since each episode is counted separately toward the total
but does not count as a distinct title. Appendix Figure A.7 shows that the increase in engagement is for both TV shows and
movies, but leads to larger increases for TV shows.
10Appendix Figure A.6 shows that the treatment effects are stable or increasing, indicating sustained improvements in
engagement throughout the intervention period.
11MRR measures the reciprocal of the row number on the homepage from which the play was derived and is a common
9

Figure 5: Treatment Effects on Reliance on Recommendations
Plays per Visit Recs MRR Share of Plays from Recs
0.0%
0.1%
0.2%
0.3%
0.4%
0.5%
0.6%
Relative Treatment Effect
Notes: Estimated ATEs from (2) for measures of reliance on recommendations: plays per visit, mean reciprocal rank (MRR),
and the share of first-in-session plays sourced from recommendations rather than other navigation. MRR is computed using
the reciprocal of the row at which the played title appears on the homepage. All effects are reported as relative percent change
against the control mean. Bars denote 95% confidence intervals computed using robust standard errors.
Figure 5 shows that the ratio of plays to visits increases by 0.47%, the share of plays originating from the
recommendations increases by 0.5%, and MRR increases by 0.1% – all consistent with Prediction 4.
5.2 Match Quality
We now evaluate Prediction 5 – how match quality changes due to the treatment. We rely on two proxies
for match quality. The first is whether users continue watching the titles they start. As titles have different
runtimes, we denote a title ascompletedif the user watched it for at least min{X,runtime}minutes for
varying values ofXon the first day of viewing the title. The second proxy is whether a user provided a
positive “thumbs” rating to a title. We restrict ourselves to titles for which the user was shown the thumbs
prompt, which asks the user for a negative thumb (thumbs down) or a positive thumb (single or double
thumbs up).
First, we measure whether users find more titles that they complete or thumb positively. We estimate (2)
on the number of titles satisfying each of these measures and report the results in Figure 6a: users complete
1.3% more titles at each of theX={15,30,45}-minute thresholds and provide 0.57% more positive thumbs.
A natural question – and the crux of Prediction 5 – is whether the average title that a user plays is of
comparable match quality. For each user, we compute the share of these outcomes out of their plays and
estimate (2) for each. Figure 6b shows statistically significant and negative effects on the probability of
completing at least 30 minutes and on the share of positive thumbs, precise nulls on the probabilities of the
15- and 45-minute completion shares and the positive thumbs ratio, and insignificant effects on the share of
measure used to assess recommendation quality (Gunawardana and Shani, 2009) with a larger value indicating that the played
title was ranked higher in the recommendations.
10

Figure 6: Treatment Effects on Match Quality
15 min 30 min 45 min Positive Thumbs
0.0%
0.2%
0.4%
0.6%
0.8%
1.0%
1.2%
1.4%
1.6%
Relative Treatment Effect
(a) Total Number of Played Titles
15 min 30 min 45 min Positive Share Negative Share Positive Ratio
−0.9%
−0.8%
−0.7%
−0.6%
−0.5%
−0.4%
−0.3%
−0.2%
−0.1%
0.0%
0.1%
0.2%
0.3%
Relative Treatment Effect
 (b) Fraction of Played Titles
Notes: Estimated ATEs from (2) on match-quality measures: shares of titles thumbed positively/negatively, and shares watched
at least 15, 30, or 45 minutes (or full runtime, if shorter) on the first viewing day. Watch-duration shares use all plays; thumbs
shares are restricted to plays long enough to trigger the thumbs prompt. Panel (a) shows estimates for the total titles per
user reaching the watch-time threshold or receiving a positive thumbs; Panel (b) shows the user-level fraction of titles meeting
each duration, receiving a positive/negative thumbs, or the positive-to-negative thumbs ratio. Bars are 95% CIs from robust
standard errors.
negative thumbs. From our conceptual model, these results are a combination of the counteracting forces
of extensive-margin entry and inframarginal switching. 12 While we parse these two effects in the Appendix,
overall, our results indicate that users found more “high quality” titles to play and that the average title is
of comparable quality, especially once we account for extensive-margin selection into additional plays due to
the treatment.
6 Conclusion
This paper studied how advances in recommendation technology reallocate the concentration of consumption.
Using a unique experiment on Netflix’s recommender system encompassing 8.5 million users, we show that
such improvements redistribute plays from a small number of superstar titles to a larger number of middle-tail
titles while also increasing overall engagement and user reliance on recommendations. These results stand
in contrast to previous work that hypothesized that increased personalization would lead to an increasing
consumption share of long-tail and superstar titles at the expense of the middle-tail. Our model provides a
rationalization for this: in markets with horizontal preference heterogeneity, improving the RecSys allows it
to extract more precise signals out of limited data, which attenuates the popularity bias inherent in existing
algorithms.
These results have important managerial implications, as they suggest that the returns of middle-tail
products to platforms depend on algorithmic maturity and the ability of the RecSys to exploit limited data.
As recommendation technology continues to improve, it becomes more feasible for platforms to target an
increasingly broad set of middle-tail titles that earlier generations of recommendation technologies were less
able to personalize. This frontier remains bounded, however: long-tail titles generate very sparse interaction
data, making targeting difficult for even mature technologies. Furthermore, it may be difficult to predict
ex antewhich titles will fall into this margin. Even so, our findings reframe the long-running debate over
12To isolate the latter, we temporally order each user’s played titles and plot the match quality measures for thek-th played
title in Appendix Figure A.8. Users play titles of lower match quality as they play more titles, suggesting the negative point
estimates could be due to playing marginal titles that users would not have played without the improved recommendations. To
conservatively account for extensive-margin entry and isolate the effects of inframarginal switching, we compute Lee bounds
(Lee, 2009) on match quality for thek-th played title in Figure A.9 which suggest that we cannot consistently sign whether
the newly played titles are higher or lower quality. The assumption of monotonicity required for the validity of Lee bounds –
treatment inducing additional consumption compared to the control – is reasonable given the results in Section 5.1.
11

whether recommendation systems concentrate or disperse consumption: the answer is neither fixed nor
universal but evolves with algorithmic maturity. At the current frontier, continued improvement lifts overall
engagement and reallocates it toward the middle-tail.
References
Abdollahpouri, H., R. Burke, and B. Mobasher (2017). Controlling popularity bias in learning-to-rank
recommendation. InProceedings of the Eleventh ACM Conference on Recommender Systems, pp. 42–46.
Aguiar, L. and J. Waldfogel (2018). Quality predictability and the welfare benefits from new products:
Evidence from the digitization of recorded music.Journal of Political Economy 126(2), 492–524.
Aridor, G., D. Goncalves, D. Kluver, R. Kong, and J. Konstan (2023). The economics of recommender
systems: Evidence from a field experiment on movielens. InProceedings of the 24th ACM Conference on
Economics and Computation, pp. 117–117.
Bajari, P., V. Chernozhukov, A. Horta¸ csu, and J. Suzuki (2019). The impact of big data on firm performance:
An empirical investigation.AEA Papers and Proceedings 109, 33–37.
Bar-Isaac, H., G. Caruana, and V. Cu˜ nat (2012). Search, design, and market structure.American Economic
Review 102(2), 1140–1160.
Benner, M. J. and J. Waldfogel (2023). Changing the channel: Digitization and the rise of “middle tail”
strategies.Strategic Management Journal 44(1), 264–287.
Bennett, J. and S. Lanning (2007). The netflix prize.
Brynjolfsson, E., Y. Hu, and M. D. Smith (2003). Consumer surplus in the digital economy: Estimating the
value of increased product variety at online booksellers.Management Science 49(11), 1580–1596.
Calvano, E., G. Calzolari, V. Denicolo, and S. Pastorello (2025). Artificial intelligence, algorithmic recom-
mendations and competition.
Celma, `O. and P. Cano (2008). From hits to niches? or how popular artists can bias music recommendation
and discovery. InProceedings of the 2nd KDD Workshop on Large-Scale Recommender Systems and the
Netflix Prize Competition, pp. 1–8.
Chen, G., T. Chan, D. Zhang, S. Liu, and Y. Wu (2024). The impact of a more diversified recommender
system on digital platforms: Evidence from a large-scale field experiment.
Fleder, D. and K. Hosanagar (2009). Blockbuster culture’s next rise or fall: The impact of recommender
systems on sales diversity.Management Science 55(5), 697–712.
Goldfarb, A. and C. Tucker (2019). Digital economics.Journal of Economic Literature 57(1), 3–43.
Gomez-Uribe, C. A. and N. Hunt (2015). The netflix recommender system: Algorithms, business value, and
innovation.ACM Transactions on Management Information Systems (TMIS) 6(4), 1–19.
Gunawardana, A. and G. Shani (2009). A survey of accuracy evaluation metrics of recommendation tasks.
Journal of Machine Learning Research 10(12).
12

He, X., L. Liao, H. Zhang, L. Nie, X. Hu, and T.-S. Chua (2017). Neural collaborative filtering. InProceedings
of the 26th International Conference on World Wide Web, pp. 173–182.
Holtz, D., B. Carterette, P. Chandar, Z. Nazari, H. Cramer, and S. Aral (2020). The engagement-diversity
connection: Evidence from a field experiment on spotify. InProceedings of the 21st ACM Conference on
Economics and Computation, pp. 75–76.
Hsiao, K.-J., Y. Feng, and S. Lamkhede (2025). Foundation model for personalized recommendation.Netflix
Tech Blog.
Klimashevskaia, A., D. Jannach, M. Elahi, and C. Trattner (2024). A survey on popularity bias in recom-
mender systems.User Modeling and User-Adapted Interaction 34(5), 1777–1834.
Kohavi, R., D. Tang, and Y. Xu (2020).Trustworthy online controlled experiments: A practical guide to a/b
testing. Cambridge University Press.
Koren, Y., R. Bell, and C. Volinsky (2009). Matrix factorization techniques for recommender systems.
Computer 42(8), 30–37.
Lee, D. S. (2009). Training, wages, and sample selection: Estimating sharp bounds on treatment effects.
The Review of Economic Studies 76(3), 1071–1102.
L¨ uke, D. (2025). Tales of tails: sales distribution and the role of retail channels in the german book market.
Journal of Cultural Economics, 1–23.
Peukert, C., A. Sen, and J. Claussen (2024). The editor and the algorithm: Recommendation technology in
online news.Management Science 70(9), 5816–5831.
Quadrana, M., P. Cremonesi, and D. Jannach (2018). Sequence-aware recommender systems.ACM Com-
puting Surveys 51(4), 1–36.
Reimers, I. and J. Waldfogel (2026). Ai and the quantity and quality of creative products: Have llms boosted
creation of valuable books?
Resnick, P. and H. R. Varian (1997). Recommender systems.Communications of the ACM 40(3), 56–58.
Rosen, S. (1981). The economics of superstars.American Economic Review 71(5), 845–858.
Salganik, M. J., P. S. Dodds, and D. J. Watts (2006). Experimental study of inequality and unpredictability
in an artificial cultural market.Science 311(5762), 854–856.
Sarwar, B., G. Karypis, J. Konstan, and J. Riedl (2001). Item-based collaborative filtering recommendation
algorithms. InProceedings of the 10th International Conference on World Wide Web, pp. 285–295.
Tucker, C. (2023). Algorithmic exclusion: The fragility of algorithms to sparse and missing data.Report,
Brookings Center on Regulation and Markets, Washington, DC, 1–26.
Tucker, C. and J. Zhang (2011). How does popularity information affect choices? a field experiment.
Management Science 57(5), 828–842.
Waldfogel, J. (2017). How digitization has created a golden age of music, movies, books, and television.
Journal of Economic Perspectives 31(3), 195–214.
13

Zentner, A., M. Smith, and C. Kaya (2013). How video rental patterns change as consumers move online.
Management Science 59(11), 2622–2634.
Zhao, Z., W. Fan, J. Li, Y. Liu, X. Mei, Y. Wang, Z. Wen, F. Wang, X. Zhao, J. Tang, et al. (2024).
Recommender systems in the era of large language models (llms).IEEE Transactions on Knowledge and
Data Engineering 36(11), 6889–6907.
Zielnicki, K., G. Aridor, A. Bibaut, A. Tran, W. Chou, and N. Kallus (2026). The value of personalized
recommendations: Evidence from netflix.International Journal of Industrial Organization, 103304.
14

Online Appendix
A Additional Results, Figures and Tables
Figure A.1: Confusion Matrix of Title Bucket Assignment across Treatments
long-tail
middle-tail superstar
Control Group Bucket
long-tail
middle-tail
superstar
Treatment Group Bucket
0.95 0.05 0.00
0.06 0.93 0.00
0.00 0.03 0.97
0.0
0.2
0.4
0.6
0.8
Notes: This figure shows the confusion matrix for title categorization into long-tail, middle-tail, and superstars. For each
treatment group, we compute each title’s percentile rank in the empirical play distribution within that group. We then classify
titles as long-tail if they fall in the bottom 50% of the distribution, middle-tail if they fall in the next 45%, and superstars if
they fall in the top 5%. The confusion matrix shows the agreement in categorization across groups.
Figure A.2: Recommendation Percentile-Bin Treatment Effects
0-10 10-20 20-30 30-40 40-50 50-60 60-70 70-80 80-90 90-91 91-92 92-93 93-94 94-95 95-96 96-97 97-98 98-99 99-100
Title Play Percentile Bin
−0.010
−0.005
0.000
0.005
0.010
Treatment Effect
Middle Tail Starts
Superstar Starts
Notes: Estimated ATEs on recommendation share within percentile buckets defined using the pooled play distribution across
the treatment and control groups.
15

Figure A.3: Treatment Effects on Recommendation Shares (Control Group Ordering)
Long Tail Middle Tail Superstar
Title Bucket
−0.010
−0.005
0.000
0.005
0.010
Treatment Effect
(a) Shares by Bucket
0-5 5-10 10-15 15-20 20-25 25-30 30-35 35-40 40-45 45-50 50-55 55-60 60-65 65-70 70-75 75-80 80-85 85-90 90-95 95-100
Title Play Percentile Bin
−0.010
−0.005
0.000
0.005
0.010
Treatment Effect
Middle Tail Starts
Superstar Starts (b) Shares by Ventile Bins
Notes: Estimated ATEs on the distribution of recommendations. Panel (a) presents coefficient estimates from (1) with the
dependent variable of the share of an individual’s recommendations accounted for by each bucket. Panel (b) presents treatment
effects on recommendation share within each ventile. In both panels the buckets and ventiles are defined using the control
group play distribution. Bars denote 95% confidence intervals.
Figure A.4: Play Percentile-Bin Treatment Effects
0-10 10-20 20-30 30-40 40-50 50-60 60-70 70-80 80-90 90-91 91-92 92-93 93-94 94-95 95-96 96-97 97-98 98-99 99-100
Title Play Percentile Bin
−0.006
−0.004
−0.002
0.000
0.002
0.004
0.006
Treatment Effect
Middle Tail Starts
Superstar Starts
Notes: Estimated ATEs on play share within the percentile buckets defined using the pooled play distribution across the
treatment and control groups.
16

Figure A.5: Treatment Effects on Play Shares (Control Group Ordering)
Long Tail Middle Tail Superstar
Title Bucket
−0.006
−0.004
−0.002
0.000
0.002
0.004
0.006
Treatment Effect
(a) Shares by Bucket
0-5 5-10 10-15 15-20 20-25 25-30 30-35 35-40 40-45 45-50 50-55 55-60 60-65 65-70 70-75 75-80 80-85 85-90 90-95 95-100
Title Play Percentile Bin
−0.006
−0.004
−0.002
0.000
0.002
0.004
0.006
Treatment Effect
Middle Tail Starts
Superstar Starts (b) Shares by Ventile Bins
Notes: Estimated ATEs on the distribution of title plays during the experiment. Panel (a) presents coefficient estimates from
specification (1) with the dependent variable of the share of an individual’s plays accounted for by each bucket. Panel (b)
presents treatment effects on play share for each pooled ventile. In both panels the buckets and ventiles are defined using the
control group play distribution. Bars denote 95% confidence intervals.
Figure A.6: Overall Engagement Treatment Effects over Time
0 1 2 3 4 5 6 7 8
Week
0.0%
0.1%
0.2%
0.3%
0.4%
Relative Treatment Effect
(a) Days with Play
0 1 2 3 4 5 6 7 8
Week
0.0%
0.2%
0.4%
0.6%
0.8%
1.0%
Relative Treatment Effect
 (b) Overall Plays
0 1 2 3 4 5 6 7 8
Week
0.0%
0.1%
0.2%
0.3%
0.4%
0.5%
0.6%
0.7%
Relative Treatment Effect
 (c) View Hours
Notes: Estimated ATEs from specification (2) for the three primary engagement outcomes – days with play, overall plays, and
view hours – estimated separately each week of the experimental intervention. Shaded bands denote 95% confidence intervals
computed via robust standard errors.
17

Figure A.7: Engagement by Title Type
Movies TV Shows
Outcome
0.0%
0.5%
1.0%
1.5%
2.0%
Relative Treatment Effect
Notes: The figure decomposes the distinct-titles-played in Figure 4 by content type, reporting relative treatment effects on the
number of distinct movies and the number of distinct TV shows watched per account. Bars denote 95% confidence intervals
computed via robust standard errors.
Figure A.8: Match Quality for First-k Plays
0 20 40 51+
kth Watched Title
−40%
−35%
−30%
−25%
−20%
−15%
−10%
−5%
0%
% Change in Positive Thumb Rate
control (holdback)
treatment
(a) Positive Thumb Rate
0 20 40 51+
kth Title Played
−24%
−22%
−20%
−18%
−16%
−14%
−12%
−10%
−8%
−6%
−4%
−2%
0%
% Change in Reached 15 min
control (holdback)
treatment (b) Share Watched At Least 15 Minutes
0 20 40 51+
kth Title Played
−24%
−22%
−20%
−18%
−16%
−14%
−12%
−10%
−8%
−6%
−4%
−2%
0%
% Change in Reached 30 min
control (holdback)
treatment
(c) Share Watched At Least 30 Minutes
0 20 40 51+
kth Title Played
−26%
−24%
−22%
−20%
−18%
−16%
−14%
−12%
−10%
−8%
−6%
−4%
−2%
0%
% Change in Reached 45 min
control (holdback)
treatment (d) Share Watched At Least 45 Minutes
Notes: The figure plots the underlying level of positive thumb rate (Panel a) and the share of plays watched at least 15, 30,
and 45 minutes during the first day of viewing (Panels b–d) against the exactkth title played, one line per treatment arm,
shown up tok= 50 and then a single pooled 51+ point. The positive thumb rate is only computed for titles that were watched
sufficiently long to have the thumbs prompt appear. TV shows are considered one title, regardless of how many episodes were
watched. For each measure, we report percent deviations from the values fork= 1.
18

Figure A.9: Lee Bounds on Match Quality for First-k Plays
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
kth Watched Title
−0.4%
−0.2%
0.0%
0.2%
0.4%
Positive Thumb Share: Identified Set
(a) Positive Thumb Share
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
kth Title Played
−0.4%
−0.2%
0.0%
0.2%
0.4%
Share Reaching 15 min: Identified Set
 (b) Share Watched At Least 15 Minutes
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
kth Title Played
−0.4%
−0.2%
0.0%
0.2%
0.4%
Share Reaching 30 min: Identified Set
(c) Share Watched At Least 30 Minutes
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
kth Title Played
−0.4%
−0.2%
0.0%
0.2%
0.4%
Share Reaching 45 min: Identified Set
 (d) Share Watched At Least 45 Minutes
Notes: The figure presents the estimated Lee bounds (Lee, 2009) for eachk-th play on positive thumb share (Panel a) and the
share of plays watched at least 15, 30, and 45 minutes during the first day of viewing (Panels b–d). For panel a,kindexes the
account’sk-th distinct title across all content that was watched sufficiently long to trigger the prompt for querying whether a
user dislikes the title (negative thumb) or likes the title (single or double positive thumbs up). For panels b–d,kindexes any
title that was started. TV shows are considered one title, regardless of how many episodes were watched. The shaded area
represents the Lee bounds for eachk.
B Omitted Proofs
Note that for all the proofs, because the utility shocks have a continuous density, ties occur with probability
zero.
Proof of Prediction 1.For any parameterδ, and any titlek∈ {L, M, S}, the law of total probability applied
to the partition{j ⋆ i =j} j∈{L,M,S} gives
fk(δ) = Pr(k∈ Ri(δ)) =
X
j∈{L,M,S}
Pr(k∈ Ri(δ)|j ⋆ i =j)p j.(3)
By Assumption 1 (popularity default), conditional onj ⋆ i =jthe recommender outputs eitherj(with
probabilityq j(δ)) or the superstarS(with probability 1−q j(δ)).
19

Writing (3) fork∈ {L, M, S}, we obtain
fL(δ) =p L qL(δ),(4)
fM (δ) =p M qM (δ),(5)
fS(δ) =p S +p M (1−q M (δ)) +p L (1−q L(δ)).(6)
(4) holds sinceLis recommended only whenj ⋆ i =L, and similarly for (5). (6) reflects the fact thatSis
recommended both whenj ⋆ i =S(in which case Pr(S∈ R i(δ)|j ⋆ i =S) = 1) and whenj ⋆ i ∈ {L, M}in
the case where the recommender defaults toS(which happens respectively with probability (1−q L(δ)) and
(1−q M (δ))).
By Assumption 1 (monotonicity), we can differentiatef L, fM , andf S with respect toδ, which gives that
f ′ M (δ)−f ′ L(δ) =p M q′ M (δ)−p L q′ L(δ)>0,
f ′ S(δ)−f ′ L(δ) =−p M q′ M (δ)−p L q′ L(δ)−p Lq′ L(δ)<0,
where both inequalities follow from Assumption 1, hence the result.
Proof of Prediction 2.We definedπ k(δ) = Pr(c i =k) as the probability that usericonsumes titlek.
Applying the law of total probability to the partition{j ⋆ i =j} j∈{L,M,S} , we can write
πk(δ) =
X
j∈{L,M,S}
pj Pr(ci =k|j ⋆ i =j).
Forj∈ {L, M}, conditional onj ⋆ i =jthe recommender outputsjwith probabilityq j(δ) andSwith
probability 1−q j(δ); forj=S, the recommender always outputsSregardless ofδ. Therefore, we have that
fork∈ {L, M, S}
Pr(ci =k|j ⋆ i =j) =q j(δ) Pr(c i =k|j ⋆ i =j,R i ={j}) + (1−q j(δ)) Pr(ci =k|j ⋆ i =j,R i ={S}).
The conditional consumption probabilities Pr(c i =k|j ⋆ i =j,R i ={r}) depend only on (U iL, UiM , UiS, b),
not onδ. Differentiating, we obtain
π′ k(δ) = X
j∈{L,M}
pj q′ j(δ)  Pr(ci =k|j ⋆ i =j,R i ={j})−Pr(c i =k|j ⋆ i =j,R i ={S})  .(7)
We use a key observation to simplify (7). Conditional onj ⋆ i =j, we haveU ij ≥U ik for allk. Under
Ri ={j}, the bonus onjreinforces this ranking, so the user consumes eitherjor the outside option. Under
Ri ={S}, the bonus onScan liftSabovejbut cannot lift any third title abovej, so the user consumes
eitherj,S, or the outside option. In particular, fork /∈ {j, S},
Pr(ci =k|j ⋆ i =j,R i ={j}) = Pr(c i =k|j ⋆ i =j,R i ={S}) = 0.
The bracketed term in (7) is therefore nonzero only whenk∈ {j, S}.
This observation partitions the analysis into two structurally distinct cases. Whenkis a non-default title
(k∈ {L, M}), only thej=kterm in (7) survives: the only way a precision gain changes the consumption of
kis by correctly identifying ak-type user and redirecting them from the popularity defaultSto their best
20

titlek. Whenkis the popularity default (k=S), bothj=Landj=Mterms contribute: every precision
gain redirects mass away fromSas someL- andM-type users are correctly identified and shifted away. We
handle these two cases in turn.
Casek∈ {L, M}.Only thej=kterm contributes:
π′ k(δ) =p k q′ k(δ)  Pr(ci =k|j ⋆ i =k,R i ={k})−Pr(c i =k|j ⋆ i =k,R i ={S})  .
Conditional on{j ⋆ i =k}, the bonus onkunderR i ={k}makesc i =kweakly more likely than under
Ri ={S}, where the bonus instead pushes consumption towardS. To establish strict inequality, consider
the event{j ⋆ i =k,−b < Uik <0, UiS +b <0}, which has positive measure by the bounded, strictly positive
density ofθ. On this event:
•UnderR i ={S},U iS +b <0 andU ik <0, so the user takes the outside option andc i = 0.
•UnderR i ={k},V ik =U ik +b >0, so the user consumesk.
Hence the bracketed term is strictly positive. By Assumption 1,p M q′ M (δ)>0 andp Lq′ L(δ)≥0, hence
π′ M (δ)>0 andπ ′ L(δ)≥0.
Casek=S.Bothj=Landj=Mcontribute:
π′ S(δ) = X
j∈{L,M}
pj q′ j(δ)  Pr(ci =S|j ⋆ i =j,R i ={j})−Pr(c i =S|j ⋆ i =j,R i ={S})  .
Conditional onj ⋆ i =jforj∈ {L, M}, the bonus underR i ={j}is onjrather thanS, soSis weakly less
likely to be consumed than underR i ={S}. Each bracketed term is nonpositive.
Thej=Mterm is strictly negative. Consider the event{j ⋆ i =M,0< U iM −U iS < b, UiS +b >0},
which has positive measure by the bounded, strictly positive density ofθ. On this event:
•UnderR i ={S}, the bonus liftsU iS +baboveU iM (sinceU iM −U iS < b) and aboveU iL (since
UiL ≤U iM ) and above 0 (sinceU iS +b >0), so the user consumesS.
•UnderR i ={M}, the bonus is onMinstead, soV iM =U iM +b > ViS =U iS, and the user does not
consumeS.
Hence Pr(ci =S|j ⋆ i =M,R i ={S})>Pr(c i =S|j ⋆ i =M,R i ={M}), and thej=Mbracketed term in
π′ S(δ) is strictly negative. Sincep M q′ M (δ)>0 by Assumption 1, we obtainπ ′ S(δ)<0.
Proof of Prediction 3.The overall strategy is to decompose engagement by the user’s best titlej ⋆ i and show
that improvements inδraise the engagement ofL- andM-type users by redirecting them from the popularity
defaultSto their true best title, where the recommendation bonusb >0 makes consumption more likely.
LetE(δ) := Pr(ci ̸= 0) denote the engagement probability. Applying the law of total probability to the
partition{j ⋆ i =j} j∈{L,M,S} , we can write
E(δ) = Pr(c i ̸= 0) =
X
j∈{L,M,S}
pj Pr(ci ̸= 0|j ⋆ i =j).
TheS-type term contributes nothing toE ′(δ): whenj ⋆ i =S, the popularity default coincides with the user’s
best title, henceR i ={S}with probability one regardless ofδ. Therefore Pr(c i ̸= 0|j ⋆ i =S) = Pr(U iS +b >
0|j ⋆ i =S) is independent ofδ.
21

The main consequence of the increase inδcomes from theL- andM-type terms, whereδshifts the
recommendation away from the defaultStoward the user’s actual best title.
Forj∈ {L, M}, conditional onj ⋆ i =jthe recommender outputsjwith probabilityq j(δ) andSwith
probability 1−q j(δ):
Pr(ci ̸= 0|j ⋆ i =j) =q j(δ) Pr(c i ̸= 0|j ⋆ i =j,R i ={j}) + (1−q j(δ)) Pr(c i ̸= 0|j ⋆ i =j,R i ={S}).
The conditional consumption probabilities givenR i are functions of (U iL, UiM , UiS, b) alone and do not
depend onδ. Differentiating with respect toδgives that
d
dδ Pr(ci ̸= 0|j ⋆ i =j) =q ′ j(δ)  Pr(ci ̸= 0|j ⋆ i =j,R i ={j})−Pr(c i ̸= 0|j ⋆ i =j,R i ={S})  .
Since theS-type term inE(δ) is constant inδ, multiplying byp j and summing overj∈ {L, M}gives that
E′(δ) = X
j∈{L,M}
pj q′ j(δ)  Pr(ci ̸= 0|j ⋆ i =j,R i ={j})−Pr(c i ̸= 0|j ⋆ i =j,R i ={S})  .(8)
Each term measures the engagement gain from redirecting aj-type user’s recommendation away fromS
towardj, weighted by the marginal precision gainp jq′ j(δ).
We now show that each redirection gain is strictly positive. For anyj∈ {L, M}, conditional on{j⋆ i =j},
we haveU ij ≥U iS, thus recommendingj(which gets the bonus) gives a higher decision utilityV ij than
recommendingS. The recommendation bonus thus makes consumption weakly more likely underR i ={j}.
To get strict inequality, we identify a set of users for whom the recommendation directly flips the consumption
decision: those whose true best titlejhas utility just below the outside option, whileSremains below even
with the bonus. Since theθ ij have bounded, strictly positive density onR,
Pr

−b < Uij ≤0, U iS +b≤0

 j⋆ i =j  >0.
On this event,U ik ≤U ij ≤0 for allkandU iS +b≤0, hence underR i ={S}the user takes the outside
option (ci = 0), while underR i ={j}the bonus pushesV ij =U ij +b >0 and the user consumesj(c i ̸= 0).
Therefore
Pr(ci ̸= 0|j ⋆ i =j,R i ={j})>Pr(c i ̸= 0|j ⋆ i =j,R i ={S}).
By Assumption 1,p Lq′ L(δ)≥0 andp M q′ M (δ)>0. Combining it with the bracketed term in (8) being strictly
positive, theL-type term is nonnegative and theM-type term is strictly positive. ThereforeE ′(δ)>0.
Proof of Prediction 4.The strategy is to show that improvements inδraise the probability of recommendation-
driven consumption faster than they raise overall engagement, so the conditional share of consumption coming
from recommendations rises.
Letρ(δ) := Pr(ci ∈ Ri |c i ̸= 0) denote the recommendation share. Since{c i ∈ Ri} ⊂ {ci ̸= 0},
ρ(δ) = Pr(ci ∈ Ri, ci ̸= 0) Pr(ci ̸= 0) = Pr(ci ∈ Ri) E(δ) .
22

We first show that d dδ Pr(ci ∈ Ri)≥E ′(δ). From (8) in the proof of Prediction 3, we can write
E′(δ) = X
j∈{L,M}
pj q′ j(δ)  Pr(ci ̸= 0|j ⋆ i =j,R i ={j})−Pr(c i ̸= 0|j ⋆ i =j,R i ={S})  .(9)
An analogous decomposition of Pr(c i ∈ Ri) gives
d
dδ Pr(ci ∈ Ri) =
X
j∈{L,M}
pj q′ j(δ)  Pr(ci ∈ Ri |j ⋆ i =j,R i ={j})−Pr(c i ∈ Ri |j ⋆ i =j,R i ={S})  .(10)
We compare the two derivatives term by term. Conditional on{j ⋆ i =j}andR i ={j}, the user either
consumes the recommended titlejor takes the outside option, thus the events{c i ∈ Ri}and{c i ̸= 0}
coincide:
Pr(ci ∈ Ri |j ⋆ i =j,R i ={j}) = Pr(c i ̸= 0|j ⋆ i =j,R i ={j}).
Conditional onj ⋆ i =jandR i ={S}, the user may consumeS(the recommended title) or some other
title outside the recommendation, thus consuming the recommendation is weakly less likely than consuming
anything:
Pr(ci ∈ Ri |j ⋆ i =j,R i ={S})≤Pr(c i ̸= 0|j ⋆ i =j,R i ={S}).
Subtracting the second from the first, the bracketed term in (10) weakly exceeds the bracketed term in (9).
Since the weightsp jq′ j(δ) are nonnegative withp M q′ M (δ)>0,
d
dδ Pr(ci ∈ Ri)≥E ′(δ)>0.
Applying the quotient rule, we can write
ρ′(δ) =
d
dδ Pr(ci ∈ Ri)·E(δ)−Pr(c i ∈ Ri)·E ′(δ)
E(δ) 2 .
Substituting d dδ Pr(ci ∈ Ri)≥E ′(δ) and usingE ′(δ)>0 from Prediction 3, we can write
ρ′(δ)≥ E′(δ)·E(δ)−Pr(c i ∈ Ri)·E ′(δ) E(δ) 2 = E′(δ)  E(δ)−Pr(c i ∈ Ri)  E(δ) 2 .
We finally showE(δ)>Pr(c i ∈ Ri), which gives the strict inequality. Consider users withj ⋆ i =Mand
Ri ={S}. By the bounded, strictly positive density ofθ, there is a positive-measure set of such users with
UiM >max{U iS +b, UiL,0}. On this event, the user consumesM— outside the singleton recommendation
{S}— hencec i ̸= 0 whilec i /∈ Ri. This event occurs with positive probability wheneverq M (δ)<1, thus
E(δ)>Pr(c i ∈ Ri).(11)
Combined withE ′(δ)>0, (11) yieldsρ ′(δ)>0, and we can conclude that Pr(c i ∈ Ri |c i ̸= 0) is strictly
increasing inδ.
23

F ormal condition for Prediction 5.For anyj∈ {L, M}, define the event
Sj :={U iS >−b,0< U ij −U iS < b}.
Conditional on{j ⋆ i =j}, the eventS j identifies users who undergo an inframarginal consumption switch when
the recommendation is corrected fromStoj. The conditionU ij −U iS < bmeans that the recommendation
bonus onSoverturns the user’s true-utility ranking whenSis recommended. The conditionU iS >−b
ensures that the user consumes rather than taking the outside option.
For anyj∈ {L, M}, define the event
Ej :={U iS <−b < Uij <0}.
On this event,U ij <0 andU iS +b <0, hence the user takes the outside option whenSis recommended.
However, whenjis recommended,U ij +b >0, hence the user consumesj.
We now introduce
rinf (δ) :=
X
j∈{L,M}
pjq′ j(δ) Pr(Sj |j ⋆ i =j),(12)
ginf (δ) :=
P
j∈{L,M} pjq′ j(δ)E[(U ij −U iS)1{S j} |j⋆ i =j]
rinf (δ) ,
uext(δ) :=
P
j∈{L,M} pjq′ j(δ)E[U ij1{E j} |j⋆ i =j]
E′(δ) .
Prediction 3 establishesE ′(δ)>0, and we show in the proof thatr inf (δ)>0, hence the ratios are well-
defined. We refer tor inf (δ) as the rate of inframarginal switching (fromSto the user’s best title), tog inf (δ)
as the expected true-utility gain conditional on an inframarginal switch, and tou ext(δ) as the expected true
utility conditional on extensive-margin entry. These expectations aggregate across best-title realizations
using the marginal precision gainsp jq′ j(δ). These definitions weight best-title realizations by the same
marginal precision gainsp jq′ j(δ) that determine which recommendations are marginally corrected.
LetQ(δ) :=E
hP
k∈{L,M,S} Uik1{c i =k}
i
denote expected realized true utility, assigning zero utility
when the user takes the outside option. Average match quality can then be written as
U(δ) =
E
hP
k∈{L,M,S} Uik1{c i =k}
i
E(δ) .
Prediction 5(Formal). U(δ) is weakly increasing inδif and only if
rinf (δ)
E′(δ)| {z }
inframarginal switches
per extensive-margin entry
ginf (δ)| {z }
true-utility gain per
inframarginal switch
≥ U(δ)−u ext(δ)| {z }
match-quality gap per
extensive-margin entry
.(13)
Average match quality is strictly increasing when the inequality is strict, locally unchanged when it holds
with equality, and decreasing when it is reversed.
Proof of Prediction 5.The overall strategy is to decompose the effect of a marginal increase inδinto an
inframarginal change in which title the user consumes and an extensive-margin change in whether the user
24

consumes. We then apply the quotient rule to the average match quality. Letc i(r) denote the user’s choice
when the recommendation isR i ={r}.
Fixj∈ {L, M}and condition onj⋆ i =j. Conditional on{j ⋆ i =j}, we have that{U ij > Uik for anyk̸=j}
almost surely.
WhenR i ={j}, the recommendation bonus reinforces the user’s true-utility ranking, hence the user
chooses eitherjor the outside option:
ci(j) =



j,ifU ij +b >0,
0,ifU ij +b <0.
WhenR i ={S}, the recommendation bonus can liftSabovej, but no third title can be chosen, as shown
previously. Therefore
ci(S) =



S,ifU iS +b >max{U ij,0},
j,ifU ij >max{U iS +b,0},
0,if 0>max{U ij, UiS +b}.
Conditional onS j andj ⋆ i =j, correcting the recommendation changes which title the user consumes but
not whether the user consumes, hence
1{c i(j)̸= 0} −1{c i(S)̸= 0}= 0.(14)
The resulting increase in realized true utility isU ij −U iS ∈(0, b).
Conditional onE j andj ⋆ i =j, correcting the recommendation raises engagement by one, following
1{c i(j)̸= 0} −1{c i(S)̸= 0}= 1,(15)
and changes the realized true utility byU ij ∈(−b,0) (decrease).
In all other preference realizations, correcting the recommendation leaves both engagement and realized
true utility unchanged. Therefore, it follows pointwise from (14) and (15) that
1{c i(j)̸= 0} −1{c i(S)̸= 0}=1{E j},
and we refer to1{E j}as theextensive-margin entry. The change in utility can be written
X
k∈{L,M,S}
Uik1{c i(j) =k} −
X
k∈{L,M,S}
Uik1{c i(S) =k}= (U ij −U iS)1{S j}| {z }
true-utility gain from
an inframarginal switch
+U ij1{E j}| {z }
true utility loss from
extensive-margin entry
.(16)
We now aggregate across the preference realizations whose recommendations are marginally changed by an
increase inδ. From (8) in the proof of Prediction 3, we can write
E′(δ) = X
j∈{L,M}
pj q′ j(δ)  Pr(ci ̸= 0|j ⋆ i =j,R i ={j})−Pr(c i ̸= 0|j ⋆ i =j,R i ={S})  .
The difference in engagement probabilities is exactly the probability that correcting the recommendation
25

induces extensive-margin entry, hence
Pr(ci ̸= 0|j ⋆ i =j,R i ={j})−Pr(c i ̸= 0|j ⋆ i =j,R i ={S}) = Pr(U ij +b >0, Uij <0, UiS +b <0|j ⋆ i =j)
= Pr(Uij >−b, Uij <0, UiS <−b|j ⋆ i =j)
= Pr(UiS <−b < Uij <0|j ⋆ i =j)
= Pr(Ej |j ⋆ i =j),
and we obtain that
E′(δ) = X
j∈{L,M}
pjq′ j(δ) Pr(Ej |j ⋆ i =j)
| {z }
rate of extensive-margin entry
.
By the strictly positive density of the utility shocks, the event{j ⋆ i =M, UiS >−b,0< U iM −U iS <
b}={j ⋆ i =M,S M }has strictly positive probability. Sincep M q′ M (δ)>0 by Assumption 1 (middle-tail
dominance), it follows thatr inf (δ)≥p M q′ M (δ) Pr(SM |j ⋆ i =M)>0, wherer inf (δ) is defined in (12).
Conditional on{S j, j⋆ i =j},0< U ij −U iS < b, hence
0<
P
j∈{L,M} pjq′ j(δ)E[(U ij −U iS)1{S j} |j⋆ i =j]
rinf (δ) <
P
j∈{L,M} pjq′ j(δ)E[b1{S j} |j⋆ i =j]
rinf (δ)
=b
P
j∈{L,M} pjq′ j(δ) Pr(Sj |j ⋆ i =j)
rinf (δ)
=b,
which implies that 0< ginf (δ)< b. Conditional on{E j, j⋆ i =j}, Uij ∈(−b,0) and the same algebra as above
gives that−b < uext(δ)<0.
Conditional onj ⋆ i =j∈ {L, M}, the recommendation isjwith probabilityq j(δ) andSwith probability
1−q j(δ). Hence,
Q(δ) =p SE
" X
k∈{L,M,S}
Uik1{c i(S) =k} |j⋆ i =S
#
+
X
j∈{L,M}
pjqj(δ)E
" X
k∈{L,M,S}
Uik1{c i(j) =k} |j⋆ i =j
#
+
X
j∈{L,M}
pj

1−q j(δ)

E
" X
k∈{L,M,S}
Uik1{c i(S) =k} |j⋆ i =j
#
.
The first term does not depend onδ, and in the remaining terms, onlyq j(δ) depends onδ. Therefore,
Q′(δ) = X
j∈{L,M}
pjq′ j(δ)E
" X
k∈{L,M,S}
Uik1{c i(j) =k} −
X
k∈{L,M,S}
Uik1{c i(S) =k} |j⋆ i =j
#
=
X
j∈{L,M}
pjq′ j(δ)E
"
(Uij −U iS)1{S j}+U ij1{E j} |j⋆ i =j
#
=r inf (δ)ginf (δ)| {z }
true-utility gains from
inframarginal switches
+E ′(δ)uext(δ)| {z }
true utility contributed by
extensive-margin entry
,(17)
26

where we use (16) in the penultimate equality, and the definition ofrinf (δ), ginf (δ), uext(δ) in the last equality.
Since we can write U(δ) =Q(δ)/E(δ), applying the quotient rule gives
U
′
(δ) = Q′(δ)E(δ)−Q(δ)E ′(δ) E(δ) 2 = 1 E(δ)  Q′(δ)− U(δ)E ′(δ)  = E′(δ) E(δ)  Q′(δ) E′(δ) − U(δ)  .
Substituting (17), we obtain
U
′
(δ) = E′(δ) E(δ) " rinf (δ) E′(δ) ginf (δ) | {z }
inframarginal true-utility gains
per extensive-margin entry
−

U(δ)−u ext(δ)

| {z }
match-quality gap per
extensive-margin entry
#
.(18)
SinceE(δ)>0 andE ′(δ)>0, the sign of U ′ (δ) is exactly the sign of the difference between the two
underbraced terms in (18). Therefore, average match quality is weakly increasing if and only if (13) holds.
It is strictly increasing when the inequality is strict, locally unchanged when it holds with equality, and
decreasing when it is reversed.
C Bayesian Recommender System Microfoundation
In this section we describe a simple Bayesian RecSys that microfounds the two key components of Assump-
tion 1: the popularity default and the larger marginal gains for middle-tail titles. Assumption 1 directly
imposes these, but in this section we show that they can arise endogenously from a RecSys that forms beliefs
about user preferences under noisy signals, where less popular titles are observed less precisely.
The Bayesian recommender system directly observes the vertical component of preferences (µ j) and
a noisy, unbiased signal about the horizontal component of preferences (θ ij). For expositional ease we
impose a Gaussian assumption onθ ij such thatθ ij ∼ N(0, σ2 θ ) and the platform observes a noisy signal
ηij =θ ij +ϵ ij/√αj forj∈ {L, M, S}, withϵij ∼ N(0,1) independent across (i, j) and acrossθso that
ηij |θ ij ∼ N(θij,1/α j). The RecSys holds a correctly specified prior over the unobservedθ ij – namely its
true marginalN(0, σ 2 θ ).
The key assumption on the recommendation technology is that the signal precision is given byα j =δλ j,
whereδindexes technology quality as in our primary model andλ L < λM < λS captures the fact that more
popular titles have more interaction data. The latter component captures the popularity bias that has been
widely documented and studied in the RecSys literature (Celma and Cano, 2008; Abdollahpouri et al., 2017;
Klimashevskaia et al., 2024).
Sinceµ j is known and the prior onθ ij is conjugate to the Gaussian signal, the posterior mean of utility
Uij =µ j +θ ij is:
sij =µ j +w(α j)η ij, w(α) = ασ2 θ 1 +ασ 2 θ , j∈ {L, M, S},
where the shrinkage weightw(α j) is the posterior precision ratio from the Gaussian Bayesian update. The
recommender scores each title by this posterior mean and recommendsR i ={arg max j∈{L,M,S} sij}.
This structure motivates each component of Assumption 1:
(i)Popularity default.In the limit case when the recommendation technology is very poor (i.e.,δclose
to 0),w(α j)→0 for allj∈ {L, M, S}. In this case, the score assigned by the RecSys to each title
27

collapses to the vertical component (s ij →µ j) and consequently the recommender selectsSfor every
user asµ S > µM > µL. Thus, in this limit case only the superstar title can be recommended to users.
Asδincreases, the RecSys puts more weight on the horizontal component and decreases the degree
of this popularity default but does not remove it entirely. The consequence is that a less popular
titlejis recommended overSonly when its weighted signal overcomes the popularity advantage ofS,
namely whenw(α j)η ij −w(α S)η iS > µS −µ j. Sincew(α j) is increasing inδ, the RecSys correctly
recommendsjto a larger share of the users who prefer it as the technology improves. The popularity
default nonetheless persists at every finiteδ– a user is still recommendedSwhenever the signal for
their preferred title is insufficiently favorable – but this bias weakens as the technology improves. This
is the stylized “popularity default” of Assumption 1: the recommender defaults toSwhenever the
signal for a user’s preferred title is insufficiently favorable, which weakens asδincreases but always
persists unless the technology is perfect.
(ii)q j monotonicity inδ.The weightw(α j) is strictly increasing inδfor eachj∈ {L, M, S}, so the score
puts increasing weight on the horizontal componentθ ij relative to the vertical componentµ j. As a
result, the probability that the recommender identifies the user’s best title,q j(δ), is weakly increasing
inδfor eachj. ForS, this monotonicity may be nearly flat asq S is precise at realistic values forδ.
(iii)Middle-tail dominance.Assumption 1 requires the marginal gain in correctly matched users,p jq′ j(δ)
– the marginal precision gainq ′ j(δ) weighted by the share of usersp j for whomjis the preferred title
– to be larger for the middle-tailMthan for the long-tailLin the empirically relevant range ofδ.
This follows since the long-tailLhas low baseline popularityµ L – a large gap between it and the
superstar title – and low signal precisionλ L – a direct consequence ofLgenerating less interaction
data. Together these causeL’s effective precisionα L =δλ L to advance slowly, so at empirically relevant
δits noisy signal remains far from the threshold to switch the recommendation fromStoL, andq ′ L(δ)
stays modest. The middle-tailM, on the other hand, is closer to that threshold to begin with and,
becauseλ M > λL, crosses it faster asδimproves. Together these lead to
pM q′ M (δ)> pLq′ L(δ),
as long asL’s marginal precision gain does not outweighM’s larger share of users for whom it is their
preferred title. This need not hold for allδ– at very highδ,Msaturates whileLcontinues to advance
– but should hold for the relevant portion ofδwhen the RecSys is not already matchingMusers to
their preferred titles.
28
