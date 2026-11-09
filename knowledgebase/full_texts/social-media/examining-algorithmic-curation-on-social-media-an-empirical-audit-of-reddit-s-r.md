---
title: 'Examining Algorithmic Curation on Social Media: An Empirical Audit of Reddit''s r/popular Feed'
url: https://arxiv.org/abs/2502.20491
category: social-media
subcategory: empirical
date: 2025-02
venue: ''
authors:
- Jackie Chan
- Fred Choi
- Koustuv Saha
- Eshwar Chandrasekharan
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.20491
pages: 15
chars: 78992
fetched_at: '2026-11-08T13:07:42+00:00'
kb_version: 1
---

# Examining Algorithmic Curation on Social Media: An Empirical Audit of Reddit's r/popular Feed

Examining Algorithmic Curation on Social Media:
An Empirical Audit of Reddit’s r/popular Feed
Jackie Chan, Fred Choi, Koustuv Saha, Eshwar Chandrasekharan
University of Illinois Urbana-Champaign
{jackiec3, fc20, ksaha2, eshwar}@illinois.edu
Abstract
Platforms are increasingly relying on algorithms to curate the
content within users’ social media feeds. However, the grow-
ing prominence of proprietary, algorithmically curated feeds
has concealed what factors influence the presentation of con-
tent on social media feeds and how that presentation affects
user behavior. This lack of transparency can be detrimental
to users, from reducing users’ agency over their content con-
sumption to the propagation of misinformation and toxic con-
tent. To uncover details about how these feeds operate and in-
fluence user behavior, we conduct an empirical audit of Red-
dit’s algorithmically curated trending feed called r/popular.
Using 10K r/popular posts collected by taking snapshots of
the feed over 11 months, we find that recent comments help a
post remain on r/popular longer and climb the feed. We also
find that posts below rank 80 correspond to a sharp decline in
activity compared to posts above. When examining the effects
of having a higher proportion of undesired behavior—i.e.,
moderator-removed and toxic comments—we find no signif-
icant evidence that it helps posts stay on r/popular for longer.
Although posts closer to the top receive more undesired com-
ments, we find this increase to coincide with a broader in-
crease in overall engagement—rather than indicating a dis-
proportionate effect on undesired activity. The relationships
between algorithmic rank and engagement highlight the ex-
tent to which algorithms employed by social media platforms
essentially determine which content is prioritized and which
is not. We conclude by discussing how content creators, con-
sumers, and moderators on social media platforms can benefit
from empirical audits aimed at improving transparency in al-
gorithmically curated feeds.
1 Introduction
Social media platforms are flooded with immense amounts
of new content every day. This constant stream of content
has led to the reliance on algorithms to curate the content
in users’ social media feeds. Algorithmic curation is defined
as the process of “organizing, selecting, and presenting sub-
sets of a corpus of information for consumption” (Rader and
Gray 2015). In recent times, the most prominent examples of
algorithmic curation are on short-form video platforms like
TikTok, YouTube Shorts, and Instagram Reels. However,
less thought of are the “hot” and “popular” feeds on multi-
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
Figure 1: A snapshot of the r/popular feed on Reddit.
ple platforms (e.g., GitHub, Reddit, X/Twitter) that also use
algorithms to curate what is “trending” (Gillespie 2016).
Despite the prominent usage of algorithmic curation on
social media, uncovering what factors influence curation al-
gorithms is challenging. This is because curation algorithms
are proprietary, preventing those on the outside from know-
ing how these algorithms work, thus protecting companies’
intellectual property. Additionally, algorithmic curation on
social media is mostly done for specific users, i.e., what
these algorithms recommend changes for each individual
user. The prominence of personalized recommendations on
social media presents two challenges: (1) understanding how
these systems affect users more broadly, and (2) collecting
enough data to support studies into these systems. To alle-
viate these challenges, we present a study that examines the
trending feed on Reddit called r/popular.
Before describing r/popular in further detail, we em-
phasize the importance of transparency in algorithmic
curation—particularly ranking. Ranking shapes online be-
havior (Salganik, Dodds, and Watts 2006; Piccardi et al.
2024) and is often interpreted as a signal of qual-
ity (Joachims et al. 2017). This gives platforms significant
influence over what content receives attention and how users
engage with it (Poudel and Weninger 2024), with down-
arXiv:2502.20491v3  [cs.HC]  7 Aug 2025

stream effects on political beliefs (Epstein and Robertson
2015; Kulshrestha et al. 2017) and the ability to assess truth
online (Pogacar et al. 2017). We extend research on algorith-
mic transparency by examining what drives and is driven by
content ranking in social media feeds.
Reddit’s r/popular Feed
The r/popular feed1 on Reddit is one of the default feeds that
is available to all users, with and without an account. The
posts on the r/popular feed come from nearly all consent-
ing communities on the platform—however, there are some
subreddits, particularly “not safe for work” (NSFW) com-
munities, that are omitted. The r/popular feed is aranked list
(see Figure 1) where the rankings are based on a calculated
“hot” score (likely based on recency, comment rate, and up-
vote score) as well as some measures for post and discussion
quality.2 At a high level, the r/popular feed consolidates the
most active posts on Reddit from numerous subreddits and
serves as the front page to the platform.
Studying Reddit’s r/popular feed comes with several ben-
efits: (1) it is highly visited, (2) it is available to all users, and
(3) it orders the posts consistently for all users, making it im-
pactful for broad population. Its prominence also allows us
to collect significant amounts of data to uncover what goes
into Reddit’s ranking decisions. Thus, analyzing the r/pop-
ular feed can provide key insights into how algorithmically
curated feeds work and how algorithmic ranking decisions
can impact user behaviors on platforms like Reddit.
Our Contributions
In this paper, we conduct an algorithmic audit of r/popular
with two key objectives. The first is to understand what fac-
tors influence algorithmic ranking on r/popular. The second
is to quantify how those decisions, specifically the feed’s
ranking decisions, affect the engagement on posts. Toward
these goals, we ask three research questions.
(RQ1) What factors are associated with how long a post
stays on the r/popular feed (i.e., the post’s tenure
on the feed)?
(RQ2) What factors are associated with the assigned rank/-
position of the post on the r/popular feed?
(RQ3) How is the post’s rank on the r/popular feed associ-
ated with the engagement on the post?
RQ1 and RQ2 examine the factors that influence Reddit’s
ranking algorithm on r/popular. Specifically, what factors af-
fect how long a post stays and where it is placed on the feed.
RQ3 aims to quantify how algorithmic ranking decisions af-
fect subsequent engagement on posts.
To answer these research questions, we capture a snapshot
of the r/popular feed every 2 minutes over an 11-month pe-
riod. Using over 1.5M consistently collected snapshots, we
employ multiple regression analyses to examine the activity
and movements (i.e., changes in position on the r/popular
feed) of 10K posts from 694 distinct subreddits.
1https://reddit.com/r/popular
2https://reddit.com/9n3ix9
Through our analyses, we find that the total number of
comments, along with recent commenting and voting ac-
tivity, were the most predictive factors for a longer stay
on the r/popular feed (RQ1) and for upward movement on
the feed (RQ2). We also find that undesired comments (i.e.,
toxic and moderator-removed comments) were also predic-
tive of a longer stay and upward movement, but to a lesser
degree. Regarding how ranking on r/popular affects engage-
ment (RQ3), we find that posts which were higher on the
feed received comments at a higher rate, as well as a greater
proportion of undesired comments.
We employ multiple regression models to obtain relation-
ships between post engagement and rank/position or move-
ment on the r/popular feed. To complement these corre-
lational insights, we employ a causal inference approach
drawing on the potential outcomes framework (Rubin 2005)
to assess causal relationships (detailed in Section 4). This
analysis provides evidence that increased commenting activ-
ity helps posts remain on r/popular longer (RQ1) and move
up the feed (RQ2). We also find that upward movement on
the feed leads to more commenting engagement (RQ3), in-
cluding both overall and undesired engagement. However,
we observe no disproportionate effect of rank on undesired
engagement specifically.
By systematically analyzing snapshots of r/popular, we
provide insights into how a prominent, algorithmically cu-
rated trending feed made its ranking decisions and how those
decisions may influence user engagement on the platform.
Understanding how these opaque algorithms operate as an
external party is inherently difficult. The internal workings
of curation algorithms are proprietary and therefore inac-
cessible to users and researchers. This lack of access limits
transparency regarding how user engagement is driven by
content ranking and how the content users interact with is in-
fluenced by engagement. Our approach can empower users
and researchers to examine the algorithmically curated feeds
that determine what they interact with on social media.
2 Related Work
In this section, we review prior work on trending feeds/pop-
ularity, algorithmic curation systems, and algorithmic audits.
Popularity & Trending Feeds
Popularity on social media has been studied before; how-
ever, these studies often focus on how users (DeVito 2022),
communities (Maldeniya et al. 2020; Chan et al. 2024), or
topics (Schlessinger et al. 2023) change after becoming vi-
ral. For example, Gurjar et al. (2022) found that after users
became viral, they increased their posting frequency and
changed their posts to be similar to the post that made them
viral. In general, the focus of these studies is the impact
of popularity on (groups of) users. However, missing from
prior work are investigations into why content or users be-
came viral in the first place.To address this gap, we examine
the factors that influence the systems that determine what
is viral on social media, specifically the r/popular feed on
Reddit. It is important to understand how these algorithmic
curation systems work because they are pervasive on social
media and the popularity they induce can be a double-edged

sword, particularly for those of marginalized identities (De-
Vito 2022). Additionally, these systems can also propagate
inflammatory content, as noted by mainstream media in re-
cent times (O’Sullivan 2019; Wu 2019).
Algorithmic Curation & Ranking
According to Rader and Gray (2015), algorithmic curation
is the process of “organizing, selecting, and presenting sub-
sets of a corpus of information for consumptions.” Within
this definition, we are particularly focused on the organiz-
ing and presenting aspect because Reddit algorithmically
ranks posts on r/popular. However, there exist other defini-
tions (Cotter, Cho, and Rader 2017; Eckles 2022; He et al.
2023). Algorithmic ranking is only one key mechanism in
which algorithmic curation systems can exert power (Di-
akopoulos 2013). By ranking content, specifically on social
media feeds, these algorithms essentially have the power to
determine what is important by prioritizing content or users
over one another. To show how impactful algorithmic rank-
ing can be, Joachims et al. (2017) examined users’ click-
through behavior on Google’s result page and found that
participants’ trust in Google’s retrieval/ranking function led
them to click on highly ranked links regardless of their qual-
ity or relevance to the query. Additionally, Salganik, Dodds,
and Watts (2006) found that ranking songs in music mar-
kets by total downloads produced more unpredictability and
inequality compared to groups who had songs ranked ran-
domly. We extend this line of work by examining the influ-
ence of algorithmic ranking on social media trending feeds.
Algorithmic Audits
Per Metaxa et al. (2021), an algorithmic audit is “a method
of repeatedly and systematically querying an algorithm with
inputs and observing the corresponding outputs in order to
draw inferences about its opaque inner workings.” In this
paper, we query the r/popular feed for 11 months and ex-
amine its ranking decisions to infer details about its inter-
nals and impact on engagement. Our study complements
the large corpus of existing social media algorithm au-
dits performed on platforms like X/Twitter (Wang et al.
2024), YouTube (Ribeiro et al. 2020; Liu, Wu, and Resnick
2024), Facebook (Gonz ´alez-Bail´on et al. 2023), and Tik-
Tok (Mousavi, Gummadi, and Zannettou 2024) to name a
few. Additionally, prior studies often focus on political bias
that may be built into curation algorithms which differs from
our focus on the factors that influence, and are influenced by,
popularity. We extend this line of work and conduct an au-
dit of algorithmic ranking on a relatively underexplored site,
Reddit’s r/popular feed.
To conduct these algorithmic audits, researchers com-
monly utilize sock-puppet accounts (Bartley et al. 2021;
Bandy and Diakopoulos 2021; Mousavi, Gummadi, and
Zannettou 2024) that “use code scripts to create simulated
users” (Liu, Wu, and Resnick 2024). Sock-puppet accounts
are necessary because platforms often do user-specific rec-
ommendations based on the user’s activity. However, that
raises the challenge of simulating realistic user behavior
which is a limitation to these types of studies. By studying a
trending feed that is available to everyone, we avoid having
to use sock-puppet accounts.
3 Data
To retrieve posts from the r/popular feed, we used PRAW—
a Python wrapper for Reddit’s API. Extending Chan et al.
(2024)’s methodology, every 2 minutes, we captured asnap-
shot of the r/popular feed’s top 100 posts from March 23,
2022, to February 8, 2023—approximately 11 months. A
single API request returns at most 100 posts. Although the
feed goes beyond the top 100, we settled on only requesting
the top 100 posts to avoid having to make multiple requests
for a single snapshot and to stay within Reddit API rate lim-
its. Thus, during the study period, we made only one request
every 2 minutes.
Sampling Approach
By taking snapshots of r/popular every 2 minutes, totaling
224,121 feed snapshots, we collected 134,661 unique posts
from 1,423 distinct subreddits. For clarity, feed snapshots
refer to a capture of the entire feed whereas a snapshot from
now on refers to a capture of an individual post within a feed
snapshot of which there are 22,412,100 snapshots—100 per
feed snapshot because there are 100 posts in a feed snapshot.
For tractability, we randomly sampled 10,000 posts from
the 134,661 posts observed. The resulting sample contains
694 subreddits and 1,548,266 snapshots. For the rest of the
paper, our findings are based on this representative sample
of 10,000 posts and their respective snapshots. From the
sample, we found that posts stay on r/popular for about 164
snapshots on average (µ = 163.63, σ = 140.25). Addition-
ally, posts from the sample, on average, stay on r/popular’s
top 100 for 6.1 hours ( µ = 6.11, σ = 5.09). Along with
these snapshots, we use Pushshift (Baumgartner et al. 2020)
to obtain the comments for each post.
Identifying Undesirable Activity
In recent years, news outlets have suggested that so-
cial media platforms are intentionally promoting antiso-
cial content through algorithmic prioritization to drive
greater user engagement (Wu 2019; O’Sullivan 2019). To
investigate whether antisocial behavior has any interac-
tions with algorithmic curation, specifically on r/popular,
we employ Almerekhi, Kwak, and Jansen (2022)’s fine-
tuned BERT model, which assigns three toxicity-related
scores for each comment: NON TOXIC , SLIGHTLY TOXIC ,
and HIGHLY TOXIC . Each score ranges from 0 to 1. If a
comment exceeds a score of 0.5—a threshold used in prior
work (Bao et al. 2021)—for either SLIGHTLY TOXIC or
HIGHLY TOXIC , then we label it as toxic. Almerekhi, Kwak,
and Jansen (2022) fine-tuned the model using r/AskReddit
comments and showed its generalizability to 99 other large
subreddits. Since the subreddits that appear on r/popular are
mostly large, we claim that using this model is well suited
for identifying toxic comments made within our r/popular
posts. Additionally, some comments were removed, presum-
ably by a moderator or bot, before they could be archived
by Pushshift. To better capture antisocial behavior, we com-
bine comments that contained “[removed]” with the ones

flagged by the BERT model under an umbrella term: “unde-
sired comments. ”
Features
In this section, we describe the features we use for our re-
gression models and provide a brief justification for inclu-
sion. This feature list applies to posts captured at a specific
snapshot/time. Thus, the features are measured at a specific
time, e.g., the number of comments at a particular snapshot.
The first feature is:
1. Content Type: Whether the post contains a link, video,
image, or just text. This is a categorical variable where
image posts are the reference category, i.e., the category
in which all other content types are compared to.
Content type functions as a control variable to capture dif-
ferences between posts that include images (49.19%), links
(16.19%), text (12.45%), and videos (22.17%).
2. Rank: Where the post is on r/popular where rank 1 is the
top of the feed and rank 100 is the bottom.
3. Age (hours): The amount of time, in hours, since the
post’s creation.
Rank is the focus of our audit and because r/popular em-
phasizes content that is currently popular, the recency of a
post is a natural feature to include.
The next set captures the activity within the post’s thread,
i.e., comment section. We also have features that utilized the
labels produced by the BERT model described previously.
4. Num. Comments: The total number of comments at the
time the snapshot was taken.
5. Recent Comments: The number of comments made in the
previous 10 minutes.
6. Proportion Undesired: The proportion of comments that
were labeled as undesired comments.
7. Proportion Recent Undesired: The proportion of com-
ments labeled as undesirable in the last 10 minutes.
8. Score: The number of upvotes on the post minus the
number of downvotes.
9. Recent Votes: The number of votes the post received in
the last 10 minutes.
10. Proportion Upvotes: The proportion of all votes that
were upvotes.
We include recent activity because there is a “hot”
calculation2 that likely includes comment and vote veloc-
ity, i.e., how many comments are coming in currently. We
define recent activity as the activity in the past 10 minutes
because posts stay at a rank for an average 7.5 of minutes
before moving onto another ( µ = 7.49, σ = 7.77). Cal-
culating the proportion of undesired comments helps us test
whether Reddit’s ranking algorithm is in any way influenced
by the presence of undesired activity.
11. Num. Subscribers: The number of subscribers the post’s
origin subreddit has.
Feature Unit µ σ Median
Age (hours) 2x 8.738 1.644 9.067
Num. Comments 2x 745.569 3.130 864
Rec. Comments 2x 11.829 3.164 12
Prop. Undesired 2x 0.189 1.660 0.190
Rec. Prop. Undesired 2x 0.160 2.417 0.201
Score 2x 13.161K 2.587 13.697K
Rec. V otes 2x 357.792 3.021 396
Prop. Upvotes 1.05x 0.917 1.065 0.930
Num. Subscribers 2x 3.781M 3.704 3.411M
Table 1: Descriptive statistics for the features used in the
regression analyses where µ and σ are the geometric mean
and standard deviation, respectively. The regression results
in the following sections are scaled using the “Unit” column
informed by σ. ‘K’ is for thousand,‘M’ is for million.
Lastly, communities are integral to Reddit, which is why
we include their size as a control variable in the models.
Table 1 provides the geometric mean and standard devi-
ations for each feature. We use the geometric versions of
these measures because the variables are log-transformed
in our regression analyses. Additionally, the geometric stan-
dard deviations are used to inform the units we use to scale
the regression coefficients which are also shown in Table 1.
The consistency to use 2x for all units except the proportion
of upvotes is to assist with interpretability.
4 Overarching Causal Inference Design
To complement our regression analysis, we adopt a causal
inference approach drawing on the potential outcomes
framework (Rubin 2005). Our goal is to examine the causal
effects of a post receiving various “treatments” (e.g., mov-
ing up the feed) compared to what would have happened
if the treatments were not administered (i.e., the “counter-
factuals”). Although our work relies on observational data,
the potential outcomes framework allows us to estimate
the missing “counterfactual” for each treated post based
on the outcomes of similar (i.e., matched), observed posts
that were not treated. In other words, matching enables a
quasi-experimental setup to estimate counterfactuals while
accounting for numerous covariates.
We use this causal framework to conduct a time series
analysis, matching on covariates measured in the snapshots
leading up to the treatment. We employ stratified propensity
score matching (Austin 2011) to identify comparable control
snapshots for each treatment. Following matching, we apply
generalized linear models (GLMs) to estimate the effects of
the treatments on outcomes measured in the snapshots im-
mediately following the treatment.
Treatment Definitions
The treatments in our causal analysis include changes in the
number of recent comments (TC), the proportion of unde-
sired comments during that time (TU), and rank movements
on the r/popular feed (TR). We define treatment and control
groups using consistent percentile-based thresholds, and we
define weak and strong versions of each treatment.

For recent comments, the weak treatment (TC-W) is de-
fined as receiving more comments in the past 10 minutes
than the median (> 11 comments), and the strong treatment
(TC-S) is defined as receiving at least the 75th percentile
(≥ 24 comments). The control is defined as receiving at
most the median (≤ 11 comments).
For undesired comments, we define treatments based on
the proportion of undesired comments received in the past
10 minutes. We use the proportion of undesired comments
to define our treatment instead of the number of undesired
comments, as the latter would be confounded by the over-
all number of recent comments. The weak treatment (TU-
W) is defined as receiving a proportion of undesired com-
ments greater than the median (> 18.75%), the strong treat-
ment (TU-S) is greater than or equal to the 75th percentile
(≥ 31.25%), and the control is less than or equal to the me-
dian (≤ 18.75%).
Finally, for rank movement, the weak treatment (TR-W)
is defined as moving at least one rank up the feed, and the
strong treatment (TR-S) is defined as moving up by at least
five ranks (75th percentile for rank movement). If the post
does not climb the feed—i.e., either stays in the same posi-
tion or falls—then it is considered a control sample.
These cutoffs are summarized in Appendix B, which also
includes information regarding filtering. For each treatment,
we estimate its effect on outcomes of tenure (RQ1), rank
movement (RQ2), and engagement (RQ3).
Stratified Propensity Score Matching
For a quasi-experimental design, we conduct matching to
find comparable treated and control groups. A propen-
sity score model matches snapshots based on their like-
lihood of receiving the treatment, quantified as propen-
sity scores. In particular, we conduct stratified propensity
score matching—which balances the bias-variance tradeoff
of comparing too biased (one-to-one matched) or too variant
(unmatched) samples (Kiciman, Counts, and Gasser 2018).
This approach distributes groups with similar propensity
scores into strata, and is a well-established method adopted
in prior work (Saha et al. 2021; Verma et al. 2022; Yuan et al.
2023; Lambert, Saha, and Chandrasekharan 2025).
For each treatment, we train an AdaBoost classifier to
estimate propensity scores using the following covariates:
(1) post age, (2) title text (top 200 bi-grams), (3) rank, (4)
time at rank, (5) number of comments, (6) number of unde-
sired comments, (7) overall comment rate, and (8) undesired
comment rate. Snapshots are then sorted by their propen-
sity scores and partitioned into equally sized strata, such that
snapshots within a stratum are similarly likely to receive the
treatment based on the covariates.
To ensure high-quality strata, we exclude any stratum with
fewer than 200 treatment or control snapshots, as well as
strata where the standardized mean difference (SMD) be-
tween treatment and control groups exceeds 0.3—a common
threshold in prior work (Kampenes et al. 2007; Kiciman,
Counts, and Gasser 2018). This matching approach approxi-
mates the presence of a counterfactual snapshot that was not
treated, enabling us to assess causal relationships between
treatments and outcomes. Further details on the number of
strata pre- and post-filtering are provided in Appendix B.
Generalized Linear Models (GLMs)
After filtering for high-quality strata, we employ GLMs and
use Bayesian inference to estimate whether the treatment
had any effect on the outcome of interest. We use a hier-
archical Bayesian model to pool effects across strata, where
within-stratum effects are sampled from a global distribution
whose mean represents the average treatment effect.
We present our findings with probability of direction (pd)
and region of practical equivalence (ROP E) (full) as these
are commonly used when communicating the strength and
significance of findings in a Bayesian context (Makowski
et al. 2019). The probability in ROP Ecan be interpreted
as the probability that a significant effect does not exist, and
pd can be interpreted as the probability that an effect is in a
particular direction. To facilitate discussion of whether the
effect size is large enough to be “significant,” we define our
ROP Eto be between -4.8% and 5%, and we consider ef-
fect sizes within the ROPE to be “not significant.” We also
report the mean of the estimated effect size along with 95%
credible interval.
5 RQ1: Tenure on r/popular
RQ1 asks what factors are associated with how long a post
stays on r/popular (i.e., tenure). To conduct this analysis,
we built logistic regression models to estimate whether the
post continues to exist on the feed in the next snapshot—
approximately 2 minutes later. Additionally, we fit a set of
GLMs to assess causal links between commenting activity
and tenure. This section describes the models and their find-
ings in further detail.
Logistic Regression
Essentially, the task is to take an r/popular post during a
snapshot and predict whether the same post continues to
be on r/popular during the next snapshot. Thus, factors that
helped a post stay on the feed in the next snapshot also
helped elongate its tenure on r/popular. Because we did
not observe posts outside the top 100, we built three mod-
els for the top 50 ( M50), top 25 ( M25), and top 10 ( M10) to
have enough observations of posts both inside and outside of
these intervals. Additionally, testing multiple rank intervals
helped examine the robustness of our results. Each respec-
tive model only includes posts that, at some point, reached
its respective rank interval (see Table 2 for the exact number
of posts). For example, if a post p is in n snapshots before it
reaches the top 50 and m snapshots after, then M50 uses only
the m snapshots after its initial breakthrough.
Causal Inference Analysis
We examined the causal relationship between commenting
activity and post tenure by using a set of logistic regression
models. We apply these models on our stratified data to es-
timate the effects of recent commenting activity (TC) and
undesired activity (TU) on the odds of appearing within the
top 50, 25, 10 ranks in the next snapshot.

Feature M50 M25 M10
Link (vs. image) 88.93%* 9.77%* -18.32%*
Text (vs. image) 47.98%* 11.12%* -2.21%
Video (vs. image) -0.13% -6.24%* 12.01%*
Age -38.91%* -39.16%* -43.14%*
Num. Comments 91.52%* 105.37%* 84.11%*
Rec. Comments 19.08%* 23.71%* 27.76%*
Prop. Undesired 2.64%* 5.26%* 16.80%*
Prop. Rec. Undesired 3.18%* 2.93%* 3.94%*
Score -47.89%* -52.84%* -57.45%*
Rec. V otes 161.14%* 125.10%* 74.51%*
Prop. Upvotes -0.60% 4.10%* -4.72%*
Num. Subscribers 3.01%* 2.39%* 10.76%*
Num. Posts 5,697 3,499 1,875
Num. Snapshots 1,062,717 687,386 391,167
R2 0.230 0.261 0.285
Table 2: Results from the three logistic regression models
(M50, M25, M10) predicting a post’s tenure on the r/popular
feed (* p < 0.05, Bonferroni-adjusted). Percentages indi-
cate the expected change in odds that a post will stay on the
top 50 ( M50), 25 ( M25), and 10 ( M10) in the next snapshot—
approximately 2 minutes later—given a unit increase in each
respective feature (see Table 1). For example, a post with 2
times the number of comments as another post is expected
to have 91.52% greater odds of staying in the top 50.
Results
Table 2 presents our findings from the three logistic regres-
sion models we built. The percentages in Table 2 correspond
to the change in odds of staying in the top 50, 25, or 10 when
the respective feature increases multiplicatively by its stan-
dardized unit listed in Table 1.
Impact of Overall Engagement. The strongest factors
associated with an increase in odds of staying near the top of
the feed are the number of total comments, recent comments,
and recent votes. We also found age (i.e., time since post
creation) to be a strong factor associated with decreases in
the odds of staying near the top. These are consistent across
all rank intervals and are natural for an engagement-based
popular feed.
We also observed that increasing the score on a post cor-
responds to a drastic decrease in the odds of staying on the
feed. According to the R2 values from each model, a sub-
stantial amount of variance remains unexplained. This sug-
gests that unmodeled factors may be strongly correlated with
score, contributing to the strong negative relationship ob-
served in Table 2.
From our causal analysis, we found that increasing the
number of comments increased a post’s tenure on r/pop-
ular in some cases. We found strong evidence that both
the weak (TC-W) and the strong (TC-S) treatments had
a significant effect on the odds of appearing within the
top 10 (0.23% in ROPE), with a probability of >99.98%
(pd) that the effect was positive for the weak treatment
(mean=17.59%, CI[9.53%, 25.86%]), and a probability of
99.88% ( pd) that the effect was positive for the strong
treatment (mean=28.15%, CI[14.23%, 45.06%]). However,
0 2 4 6 8 10 12
Hours
1
20
40
60
80
100 Rank
Figure 2: The rank trajectories of 10 r/popular posts where
hour 0 is the first moment they reached the top 100. Note
the stepwise movement as posts tended to jump to different
ranks instead of gradually shifting between nearby ranks.
there was little evidence that either treatment significantly
increased the odds of staying in the top 25 and top 50
(≥18.45% in ROPE). Thus, we were only able to causally
link an increase in recent comments to tenure on the top 10.
Impact of Undesired Activity. According to Table 2, we
found that increasing the proportion of undesired comments
and the number of subscribers has a comparatively small
but significant positive relationship with the odds that a post
stays within the top 50 and top 25, with a stronger effect
in the top 10. While these effects do not necessarily indi-
cate that the ranking algorithm is intentionally designed to
promote antisocial content to drive more user engagement,
these results fail to rule it out. These relationships also hint
at an interaction between undesired comments and the rank
of a post, and that the relationship with undesired comments
is strongest for posts at the top of the feed.
From our causal analysis, we found that increasing the
proportion of undesired comments could increase a post’s
tenure on r/popular in some limited cases. We found evi-
dence that the strong version of the treatment (TU-S) had
a significant effect on the odds of appearing in the top 10
(2.58% in ROPE), with a probability of 99.93% ( pd) that
this effect is positive (mean=13.09%, CI[5.34%, 21.90%]).
However, we found little evidence that the weak treatment
(TU-W) had any significant effect on appearing within any
rank threshold (≥64.73% in ROPE), or that the strong treat-
ment had any significant effect on the odds of appearing the
top 25 or top 50 (≥88.70% in ROPE).
6 RQ2: Rank on r/popular
In this section, we describe what factors are associated with
a post’s rank on r/popular. As seen in Figure 2, posts do not
gradually change between nearby ranks over time. Instead,
the typical rank trajectory of a post consists of two parts: (1)
where the post stays at one rank for several minutes, and (2)
where the post suddenly jumps to another, distant rank. To
characterize this discontinuous behavior, we used two sepa-
rate regression models to determine which factors affect: (1)
when a post changes rank, and (2) how far it moves when it
does.

1 10 20 30 40 50 60 70 80 90 100
Rank
0%
5%
10%
15%
20%Probability
Up
Down
Figure 3: The probability of a post moving up or down on
r/popular in the next snapshot across ranks estimated by a
multinomial logistic regression. Note that most of the time a
post did not move in the next snapshot.
Multinomial Regression (Rank Movement)
The first model is a multinomial regression that estimated
whether a post will move up the feed, down the feed, or stay
in its current position in the next snapshot. Posts tend to stay
at the same rank for several minutes at a time (see Figure 2),
and this model helped us determine which factors acceler-
ated the movement of a post, and in which direction.
Ordinal Regression (Rank)
We also aimed to estimate how far a post moves when it
does, so we employed a second model: an ordinal regression
that estimated the post’s next rank. Only snapshots where a
post changed rank were considered so that we could get a
more detailed picture of which rank a post changed to when
it moved. We constructed a latent-variable model, where a
post’s rank is determined by a continuous latent variable
(z), and the observed rank depends on which cut points
z falls between. The model estimated both the cut points
and the association between each feature and the expected
value of z. The flexibility of the cut points within the model
makes it well suited to handle the uneven “distances” be-
tween ranks—e.g., it might be less likely for a post to move
from rank 2 to rank 1 than it is from rank 99 to 98. We im-
plemented this model in a Bayesian framework with strongly
informative priors on the cut points and weakly informative
priors on the coefficients. We provided more details on the
priors in Appendix A.
Causal Inference Analysis
We examined the causal relationship between commenting
activity and rank movement using an approach similar to the
earlier multinomial regression. We used a set of multinomial
regression models on our stratified data to estimate the im-
pacts of recent commenting activity (TC) and undesired ac-
tivity (TU) on the odds of upward movement and downward
movement against no movement in the next snapshot.
Results
Starting with the multinomial regression, Table 3 shows
the associations between a twofold increase to a feature—
excluding the proportion of upvotes—and the probability
Feature Up Down
Link (vs. image) 2.757% 4.812%*
Text (vs. image) 0.401% 7.842%*
Video (vs. image) 1.147% -0.727%
Age 4.117%* 10.114%*
Num. Comments -1.997%* -7.200%*
Rec. Comments 7.333%* -4.127%*
Prop. Undesired 0.751% -2.681%*
Prop. Rec. Undesired 0.285% -0.801%
Score -11.626%* 11.018%*
Rec. V otes 14.796%* 3.886%*
Prop. Upvotes 1.393%* 0.803%
Num. Subscribers 0.097% -2.937%*
Num. Observations 1,548,266
Nagelkerke R2 0.043
Table 3: Results from the multinomial regression model pre-
dicting when a post moves and in which direction (* p <
0.05, Bonferroni-adjusted). Percentages represent expected
change in odds of moving up or down the feed (compared
to no movement) in the next snapshot, given a unit increase
in each respective feature (see Table 1). For example, a post
that is 2 times as old as another post is expected to have
4.117% greater odds of moving up the feed and 10.114%
lower odds of moving down the feed in next snapshot.
of a post moving up or down the feed. Additionally, Fig-
ure 3 shows the baseline probabilities for each rank move-
ment across ranks. Note that the probability of moving up
and down do not sum to 100% as the remainder reflects the
likelihood that the post remains in the same position in the
next snapshot.
Association Between Rank & Movement.We found that
posts closer to the top of the feed moved less frequently and
less far. Figure 3 shows that the probability that a post moves
in either direction reduces as its rank gets closer to 1, and
Figure 4 that shows the gaps between cut points close to
rank 1 are wider than cut points closer to rank 100. This is
consistent with the intuition that there would be less compe-
tition toward the top of the feed as it would be rare for posts
to achieve that level of “quality.”
Impact of Overall Activity on Rank. Similar to our re-
sults in RQ1, the number of recent comments and recent
votes are strong factors associated with increases in the
probability moving up in rank, as seen in Table 3. In terms of
how far a post moves, Table 4 indicates that the total number
of comments, recent comments, and recent votes have a sim-
ilar magnitude relationship. However, Table 3 shows that the
total number of comments tends to “stabilize” the rank of a
post, decreasing the odds of movement in either direction,
but still favoring upward movement. Similarly, the number
of subscribers is not associated with an increase in proba-
bility of upward movement directly, but it still favored up-
ward movement by decreasing the probability of downward
movement (-2.937%). These findings are consistent with an
engagement-based ranking algorithm, but they highlight the
influence of recent activity.
Our causal analysis found that increasing the number of

Feature ∆z
Link (vs. image) 0.001
Text (vs. image) 0.033**
Video (vs. image) -0.015*
Age 0.163**
Num. Comments -0.053**
Rec. Comments -0.062**
Prop. Undesired -0.021**
Prop. Rec. Undesired -0.008**
Score 0.132**
Rec. V otes -0.081**
Prop. Upvotes -0.018**
Num. Subscribers -0.028**
Table 4: Results from the ordinal regression model estimat-
ing how far a post jumps in rank. Values represent expected
change in the latent variable z representing rank on r/pop-
ular (Figure 4 shows the cut points which map z to ranks)
given a unit increase to a feature (see Table 1). For example,
a post that is 2 times older than another post is expected
to have a 0.163 increase in z in the next snapshot where
the rank changes. Parameters whoseprobability of direction,
a Bayesian analog of p-values (Makowski et al. 2019), are
greater than 0.95 are denoted with a single asterisk (*), and
those greater than 0.999 are denoted with two (**).
comments caused posts to move up the feed by simultane-
ously increasing the odds of moving up the feed and de-
creasing the odds of moving down the feed. Specifically, we
found strong evidence that the receiving more than 11 re-
cent comments (TC-W) had a significant effect on the odds
of moving upward ( <0.03% in ROP E), and a >99.98%
probability ( pd) that this effect is positive (mean=10.63%,
CI[8.65%, 12.52%]). We also found strong evidence that re-
ceiving more than 10 recent comments (TC-W) had a sig-
nificant effect on the odds of moving downward (<0.03% in
ROP E), and a >99.98% probability (pd) that this effect is
negative (mean=-11.57%, CI[-13.67%, -9.79%]).
We found similar results with the strong treatment (TC-S),
though with slightly lower confidence due to the relative lack
of suitable strata (see Appendix B). Specifically, we found
evidence that receiving at least 24 recent comments (TC-S)
had a significant effect ( <4.53% in ROP E) on the odds
of moving upward, and a 99.58% probability ( pd) that this
effect is positive (mean=11.40%, CI[3.15%, 19.48%]). We
also found strong evidence that the same treatment (TC-S)
had a significant effect on the odds of moving downward
(0.1% in ROPE), and a >99.98% probability ( pd) that this
effect is negative (mean=-17.80%, CI[-24.19%, -10.60%]).
Impact of Undesired Activity on Rank. Table 3 shows
that the proportion of undesired comments slightly associ-
ated with a decrease in the likelihood of moving down the
feed, and Table 4 indicates that undesired comments has a
relatively small but positive relationship with how far a post
moves up the feed (negative in terms of z). This is in con-
trast with Table 3 that only identifies a negative relationship
between undesired comments and posts moving downwards.
However, from our causal analysis, we found little evi-
dence that the proportion of undesired comments has any
1 10 20 30 40 50 60 70 80 90 100
10
20
30
Rank Latent Space
(z)
Cut points
1 10 20 30 40 50 60 70 80 90 100
Rank
0.25
0.50
0.75
1.00
Gaps Between Ranks
(z)
Distance Between n and n-1
Figure 4: The ordinal regression model’s estimated cut
points for each rank and the distances between adjacent
ranks in the latent space used to represent rank. The inde-
pendent feature associations in Table 3 correspond to this
latent space.
significant effect on rank movement up or down, with a
probability in ROP Eof 97.98% or greater for both the
weak (TU-W) and strong versions of the treatment (TU-S).
7 RQ3: Engagment on r/popular
Our analyses from RQ1 and RQ2 provided empirical in-
sights into the factors are associated with rank on r/popular.
Finally, for RQ3, we investigated how rank on the r/popu-
lar feed influences the engagement on posts, specifically the
frequency of comments gained before the next snapshot.
Negative Binomial Regression
To estimate the relationship between each feature in Sec-
tion 3 and the comment rate on a post during the next
snapshot—measured as the number of new comments be-
tween two snapshots—we trained a single negative binomial
regression to estimate both the rate of non-undesired com-
ments and undesired comments by using an interaction term
that indicates whether the model is estimating the former or
the latter. Thus, by default, the model measures the asso-
ciation between each feature and the rate of non-undesired
comments and the interaction term measures whether there
is any difference in the relationship when estimating the rate
of undesired comments instead.
Causal Inference Analysis
To estimate whether moving up the feed causally increases
the rate of comments overall, undesired comments, or the
proportion of undesired comments, we trained a set of nega-
tive binomial regression models. These models utilize our
stratified data to estimate the impact moving up the feed
one rank (TR-W) and five ranks (TR-S)—i.e., the 75th
percentile—on commenting activity. More specifically, we

Feature ¬Und. Und: ¬Und. Net Und.
Link (vs. image) -3.440%* +0.342% -3.110%
Self (vs. image) -2.179%* +0.650% -1.543%
Video (vs. image) 0.924%* +0.006% 0.930%
Age -13.140%* -0.467% -13.545%
Num. Comments 22.331%* -2.601%* 19.149%
Rec. Comments 61.740%* +1.056%* 63.449%
Prop. Undesired -14.467%* +115.633%* 84.437%
Prop. Rec. Und. -1.500% +8.713%* 7.082%
Score -13.992%* +2.062%* -12.218%
Rec. V otes 13.530%* -3.422%* 9.645%
Prop. Upvotes 3.519%* -1.077%* 2.405%
Num. Subscribers 1.414%* -0.344%* 1.066%
Pseudo R2 0.29
Table 5: Results from the negative binomial regression
model predicting the rate of non-undesired and undesired
comments (* p < 0.05, Bonferroni-adjusted). Percentages
in “¬Und.” denote expected change in non-undesired com-
ments given a unit increase in the respective feature (see Ta-
ble 1). Percentages in “Und:¬Und.” denote expected change
in the ratio of undesired to non-undesired comments gained.
Net expected change to undesired comments is shown in the
“Net Und.” column. For example, a post that is 2 times older
than another is expected to have 13.1% fewer non-undesired
comments and a further 0.47% fewer undesired comments,
for a net of 13.5% fewer undesired comments.
measure each treatment’s effect on the overall commenting
rate, undesired commenting rate, and proportion of unde-
sired comments during the period before the next snapshot.
Results
Table 5 shows how our feature set from Section 3—
excluding rank which is visualized in Figure 5—is associ-
ated with the rate of non-undesired comments and the rate
of undesired comments.
Association Between Engagement & Non-Undesired
Activity. From Table 5, we found that the number of com-
ments, recent commenting activity, and recent voting activ-
ity have the strongest associations with future non-undesired
activity. Additionally, the relationship recent commenting
activity has with non-undesired commenting rate (61.74%)
is greater than the one found with the comments overall
(22.33%). This hints that the active discussions plays a more
important role to future engagement than the total number
of discussions that have already occurred.
Association Between Engagement & Undesired Activ-
ity. For undesired activity, we found that the proportion of
undesired comments has the strongest association (84.43%)
out of all the ones found in Table 5. This potentially suggests
that having a greater proportion of undesired activity invites
similarly undesired activity in the future.
Impact of Rank on Commenting Activity. Regarding
rank’s associations with commenting rate, we found that
the rate of non-undesired comments falls fairly consistently
from ranks 2 through 80, visualized in the first subplot in
Figure 5. Afterward, the rate of non-undesired comments
1 10 20 30 40 50 60 70 80 90 100
1.00
1.25
1.50
1.75
2.00
# Non-Und.
Comments Gained
1 10 20 30 40 50 60 70 80 90 100
Rank
77%
76%
75%
74%
73%
72%
Ratio of Und. to Non-Und.
 Comments Gained
Figure 5: Plots of the intercepts for non-undesired comments
(top) and undesired comments (bottom). Error bars indicate
95% confidence intervals. Assuming a “standard” post with
features equal to µ (see Table 1), the top plot can be inter-
preted as the expected number of non-undesired comments
gained in 2 minutes at a given rank, and the bottom plot can
be interpreted as the expected ratio of undesired comments
to non-undesired comments gained at a given rank. For ex-
ample, a “standard” post at rank 1 is expected to gain about 2
non-undesired comments every 2 minutes, and is expected to
gain 72.4% fewer undesired comments than non-undesired
comments. The bottom plot also shows a decreasing trend in
the ratio of undesired comments with increasing rank, at a
rate of about 0.064% per rank (red dashed line).
falls precipitously below rank 80.
From our causal analysis, we found strong evidence that
moving up the feed increases the comment rate experi-
enced by the post. Both our weak (TR-W) and strong (TR-
S) treatments increase commenting rate. Specifically, the
weak treatment (i.e., moving up the feed at least one rank)
had significant (0.03% in ROP E) mean effect of 8.00%
(CI[5.76%, 10.41%]) with a >99.98% probability (pd) that
this effect is positive. Similarly, for our strong treatment
(i.e., moving up the feed at least five ranks) had a signifi-
cant (0.05% in ROP E) mean effect of 10.19% (CI[7.14%,
13.09%]) with a >99.98% probability (pd) that this effect is
positive. Thus, we found strong evidence that higher posi-
tions on the feed incur more comments.
Impact of Rank on Undesired Activity. From the sec-
ond subplot in Figure 5, we observed that the ratio of un-
desired comments falls as the post is placed lower on the
feed. Specifically, the ratio of undesired comments to non-
undesired comments falls at a rate of 0.064% per rank ( p <
0.05). Additionally, ranks 2 and 3 may indicate that there is a
sharp rise in the ratio at the peak of the r/popular feed, how-
ever, it is difficult to be sure given the confidence intervals.
Although Figure 5 shows a slight increase in the pro-

portion of undesired comments at higher ranks, our causal
analysis found no disproportionate increase in undesired
comments relative to overall commenting. Both treatments
had a statistically significant (0.1% in ROP E) effect
on the number of undesired comments: 8.65% mean for
TR-W (CI[6.29%, 11.18%]) and 10.74% mean for TR-S
(CI[7.57%, 13.77%]). However, these effect sizes are com-
parable to those observed for overall commenting. When an-
alyzing the proportion of undesired comments—thus con-
trolling for the overall comment volume—we found no sig-
nificant effect ( >99.98% in ROP E). This suggests that
the increase in undesired comments likely coincides with a
broader increase in overall engagement, rather than indicat-
ing a targeted or disproportionate effect.
8 Discussion
Here, we discuss the implications of our methodology and
findings for future audits of algorithmically curated feeds.
Empowerment Through Transparency
Prior literature has shown that people are often unaware that
algorithms control what they see and, in turn, how their
content is spread (Rader, Cotter, and Cho 2018; Hsu et al.
2020). This unawareness can lead to harm (Eslami et al.
2015) resulting in calls for greater transparency regarding
these algorithmic systems (Alvarado and Waern 2018). Our
study enables transparency by quantifying how factors like
commenting rate and undesirable activity affect algorithmic
ranking on a prominent social media feed.
Implications for Content Creators.Our study has impli-
cations for content creators, particularly those whose liveli-
hoods are tied to algorithmic decision making. The relation-
ship we identified between algorithmic rank and engagement
highlights how the algorithms employed by social media
platforms essentially get to decide which content is priori-
tized and which is not. This has led content creators on plat-
forms like YouTube to blindly attempt to appease algorithms
by adjusting their content creation process (Choi et al. 2023).
Audits of algorithmic feeds can empower creators by provid-
ing accurate information about how their actions can affect
content prioritization on their respective platforms.
Implications for Content Consumption. We found that
the order in which content is ranked can influence the
levels and types of user engagement within algorithmi-
cally curated feeds. Similarly, the types of content that
are recommended and where they are positioned can af-
fect users’ content consumption practices (Piccardi et al.
2024; Poudel and Weninger 2024). Prior work has exam-
ined this impact through users’ trust in Google’s ranking al-
gorithm, which leads to a greater number of clicks on top-
ranked links regardless of their accuracy or relevance to the
query (Joachims et al. 2017). This trust bias that Joachims
et al. (2017) refer to, coupled with the increased engagement
levels observed in our analysis (see Section 7), can catalyze
the spread of misinformation—especially if higher ranks
within feeds are misconstrued as an indicator of content
quality and trustworthiness. To alleviate some of these pit-
falls, some platforms have provided explanations for their al-
gorithmic recommendations, however, Mousavi, Gummadi,
and Zannettou (2024) found that those on TikTok in partic-
ular were generic and inapplicable to the user. Further re-
search is needed to empirically understand how algorithmic
rank affects users’ perceptions of content highlighted on so-
cial media feeds.
Implications for Content Moderation
Prior work has shown that sudden popularity can be dis-
ruptive to moderation teams that have to manage increased
activity, particularly from newcomers (Kiene, Monroy-
Hern´andez, and Hill 2016; Chan et al. 2022, 2024). Despite
how integral algorithmic curation is to social media plat-
forms, moderators currently have little influence on algo-
rithmic curation systems. This lack of agency impedes their
ability to direct their communities and highlight desirable
content—an idea that has been explored in prior work (Choi
et al. 2025). Given that moderators have little influence on
these systems, there is a need for design interventions that
provide moderators with more controls or ways to “over-
ride” algorithmic curation systems. These additional affor-
dances can be used to highlight desirable content in feeds,
which has theoretical foundations (Kraut and Resnick 2012)
and is currently done with existing mechanisms such as
awards, upvotes, pins, and flairs (Lambert, Choi, and Chan-
drasekharan 2024). These additional controls may take the
form of various sliders that adjust latent weights on the feed
to emphasize different priorities (e.g., increase user diversity
on the feed), visual indicators for moderator-assigned con-
tributions, or specific feeds that filter for moderator-selected
contributions—similar to the ones the New York Times has
to filter for reader- and editor-selected comments (Wang and
Diakopoulos 2022).
Implications for Future Empirical Audits
Despite the pervasiveness of algorithmic curation on social
media, studying it as external researchers is exceedingly
difficult. This difficulty is compounded by data access re-
strictions as platforms lock down their APIs, e.g., X/Twit-
ter (Calma 2023) and Reddit (Reddit 2023). The reduction
in API accessibility has led researchers to use other methods
like sock-puppet accounts (Perriam, Birkbak, and Freeman
2020; Bartley et al. 2021; Bandy and Diakopoulos 2021;
Liu, Wu, and Resnick 2024; Mousavi, Gummadi, and Zan-
nettou 2024) and data donations (Jhaver et al. 2023; Chouaki
et al. 2024) that each have their own set of drawbacks.
These restrictions have led to the reliance on externally-
maintained datasets like the now defunct Pushshift—which
has been heavily used in prior research (Jhaver, Bruckman,
and Gilbert 2019; Atcheson, Koshy, and Karahalios 2024;
Kou et al. 2024; August et al. 2024). To avoid these chal-
lenges, we developed a robust pipeline to collect large-scale
high-fidelity snapshots of Reddit’s trending feed r/popular
which can be adapted for other platforms with similar feeds.
However, we recognize that these approaches are ex-
tremely time- and resource-intensive, posing significant
challenges for scalability without adequate financial back-
ing and collaborative support. Although partnerships be-
tween academia and industry have yielded important re-
search outcomes, such collaborations are increasingly rare.

Given these circumstances, and echoing a theme identified
in a 2024 CCC Workshop Visioning Report (Eslami et al.
2024), this presents an opportunity for researchers to share
auditing infrastructures and data-sharing protocols that sup-
port the collection, storage, and access of social media data
for research purposes. For example, in the industry circuit,
data clean rooms (Herbrich 2022) are emerging for sev-
eral companies to have a shared and secure data infras-
tructure. However, the creation of these infrastructures must
also adhere to relevant privacy and legal standards such as
GDPR (GDRP 2023) or CCPA (CCPA 2018), especially for
sensitive data. This would enable more research like ours, in-
forming future regulation, while safeguarding the rights and
privacy of social media users.
Limitations & Future Directions
We recognize that our study bears limitations, however,
these limitations also suggest interesting future directions.
Our findings are shaped by the demographics of Reddit
users. Applying them elsewhere requires careful attention
to demographic similarities between Reddit and the plat-
form in question. Our study employed a robust causal in-
ference design that mitigated potential confounds and led to
stronger inferences than purely correlational methods. How-
ever, we cannot cannot claim “true causality,” due to the lack
of “true counterfactuals” and the potential for unobserved
confounders. Future research can build on our work through
controlled experimental studies to further validate and ex-
tend these insights.
The relatively low R2 our models exhibited indicate that
there are other factors outside of the ones we have included
that influence the outcomes. One such factor may include
details about surrounding posts on the r/popular feed. A hint
that our model is incomplete is the observation that increas-
ing the score on a post corresponds to a drastic decrease
in the odds of staying on the feed, as found in RQ1 and
RQ2. This counterintuitive result may be due to a correla-
tion between a post’s score and some unobserved influence.
Regardless, future work can build upon these models by in-
cluding more factors about surrounding posts that are com-
peting for the same finite number of spots on these feeds.
Furthermore, future work could also employ more advanced
statistical methods like a stochastic transitivity model (John-
son and Kuhn 2013).
Lastly, because our findings were based on observational
data, future work will have to examine more user-centered
effects of algorithmic ranking—similar to Salganik, Dodds,
and Watts (2006); Joachims et al. (2017), but on social me-
dia. Specifically, future work could design controlled exper-
iments to examine how algorithmic rank influences individ-
ual users and shapes their perceptions of highly ranked con-
tent. These studies can also incorporate interviews or sur-
veys to investigate user perceptions of content quality and
relevance, as well as affective responses (e.g., trust), and
how these factors relate to user engagement and online con-
tent consumption. Together, these studies can offer comple-
mentary insights that provide a more comprehensive under-
standing of algorithmic ranking on social media platforms.
9 Conclusion
Now that algorithmic curation has become integral to online
ecosystems, examining it and its effects on user behavior be-
comes critical. In this paper, we conducted a comprehensive
empirical audit of one such system: Reddit’s r/popular feed.
Through this, we successfully quantified how recent com-
menting rate and other factors influence algorithmic ranking
on r/popular, as well as how rank/position on r/popular im-
pact subsequent engagement and undesirable behavior. Our
findings are based on millions of snapshots of the top 100
ranks on r/popular consistently collected over 11 months,
an approach that can be applied to other platforms. Addi-
tionally, we discussed the implications of our findings for
stakeholders, including content creators, highlighted moder-
ators’ lack of agency in community curation systems, and
proposed future research directions on algorithmic curation
amid reduced data access. All in all, studying algorithmic
curation goes back to user agency: should users have control
over how they interact with content and how their content
is distributed online? To address this, we must first under-
stand how these systems are embedded in our online en-
vironments, thus enabling us to make informed decisions
about governing them.
References
Almerekhi, H.; Kwak, H.; and Jansen, B. J. 2022. Investigating
toxicity changes of cross-community redditors from 2 billion posts
and comments. PeerJ Computer Science.
Alvarado, O.; and Waern, A. 2018. Towards Algorithmic Experi-
ence: Initial Efforts for Social Media Contexts. In CHI.
Atcheson, A.; Koshy, V .; and Karahalios, K. 2024. Not What
it Used to Be: Characterizing Content and User-base Changes in
Newly Created Online Communities. In CHI.
August, T.; Lo, K.; Smith, N. A.; and Reinecke, K. 2024. Know
Your Audience: The benefits and pitfalls of generating plain lan-
guage summaries beyond the “general” audience. In CHI.
Austin, P. C. 2011. An Introduction to Propensity Score Methods
for Reducing the Effects of Confounding in Observational Studies.
Multivariate Behavioral Research.
Bandy, J.; and Diakopoulos, N. 2021. More Accounts, Fewer
Links: How Algorithmic Curation Impacts Media Exposure in
Twitter Timelines. PACM HCI.
Bao, J.; Wu, J.; Zhang, Y .; Chandrasekharan, E.; and Jurgens, D.
2021. Conversations Gone Alright: Quantifying and Predicting
Prosocial Outcomes in Online Conversations. In WWW.
Bartley, N.; Abeliuk, A.; Ferrara, E.; and Lerman, K. 2021. Audit-
ing Algorithmic Bias on Twitter. In WebSci.
Baumgartner, J.; Zannettou, S.; Keegan, B.; Squire, M.; and Black-
burn, J. 2020. The Pushshift Reddit Dataset. arXiv:2001.08435.
Calma, J. 2023. Scientists say they can’t rely on Twitter anymore.
The Verge.
CCPA. 2018. California Consumer Privacy Act (CCPA). State of
California - Department of Justice - Office of the Attorney General.
Chan, J.; Atreyasa, A.; Chancellor, S.; and Chandrasekharan, E.
2022. Community Resilience: Quantifying the Disruptive Effects
of Sudden Spikes in Activity within Online Communities. CHI EA.
Chan, J.; Lambert, C.; Choi, F.; Chancellor, S.; and Chandrasekha-
ran, E. 2024. Understanding Community Resilience: Quantifying
the Effects of Sudden Popularity via Algorithmic Curation. In
ICWSM.
Choi, F.; Lambert, C.; Koshy, V .; Pratipati, S.; Do, T.; and Chan-
drasekharan, E. 2025. Creator Hearts: Investigating the Impact Pos-
itive Signals from YouTube Creators in Shaping Comment Section
Behavior. In CHI.

Choi, Y .; Kang, E. J.; Lee, M. K.; and Kim, J. 2023. Creator-
friendly Algorithms: Behaviors, Challenges, and Design Opportu-
nities in Algorithmic Platforms. In CHI.
Chouaki, S.; Chakraborty, A.; Goga, O.; and Zannettou, S. 2024.
What News Do People Get on Social Media? Analyzing Exposure
and Consumption of News through Data Donations. In WWW.
Cotter, K.; Cho, J.; and Rader, E. 2017. Explaining the News Feed
Algorithm: An Analysis of the “News Feed FYI”’ Blog. In CHI
EA.
DeVito, M. A. 2022. How Transfeminine TikTok Creators Nav-
igate the Algorithmic Trap of Visibility Via Folk Theorization.
PACM HCI.
Diakopoulos, N. 2013. Algorithmic accountability reporting: On
the investigation of black boxes. Tow Center for Digital Journal-
ism.
Eckles, D. 2022. Algorithmic transparency and assessing effects of
algorithmic ranking.
Epstein, R.; and Robertson, R. E. 2015. The search engine manip-
ulation effect (SEME) and its possible impact on the outcomes of
elections. PNAS.
Eslami, M.; Gilbert, E.; Schoenebeck, S.; Baumer, E. P. S.; Chan-
drasekharan, E.; Mooy, M. D.; Karahalios, K.; Karger, D.; Cottom,
T. M.; Monroy-Hern´andez, A.; Terveen, L.; and Wihbey, J. 2024.
The Future of Research on Social Technologies: CCC Workshop
Visioning Report. arXiv:2404.10897.
Eslami, M.; Rickman, A.; Vaccaro, K.; Aleyasen, A.; Vuong, A.;
Karahalios, K.; Hamilton, K.; and Sandvig, C. 2015. “I always
assumed that I wasn’t really that close to [her]”: Reasoning about
Invisible Algorithms in News Feeds. In CHI.
GDRP. 2023. Data Sharing: A Code of Practice.Information Com-
missioner’s Office.
Gillespie, T. 2016. #trendingistrending: when algorithms become
culture. In Algorithmic Cultures. Routledge.
Gonz´alez-Bail´on, S.; Lazer, D.; Barber´a, P.; Zhang, M.; Allcott, H.;
Brown, T.; Crespo-Tenorio, A.; Freelon, D.; Gentzkow, M.; Guess,
A. M.; Iyengar, S.; Kim, Y . M.; Malhotra, N.; Moehler, D.; Ny-
han, B.; Pan, J.; Rivera, C. V .; Settle, J.; Thorson, E.; Tromble, R.;
Wilkins, A.; Wojcieszak, M.; de Jonge, C. K.; Franco, A.; Mason,
W.; Stroud, N. J.; and Tucker, J. A. 2023. Asymmetric ideological
segregation in exposure to political news on Facebook. Science.
Gurjar, O.; Bansal, T.; Jangra, H.; Lamba, H.; and Kumaraguru, P.
2022. Effect of popularity shocks on user behaviour. In ICWSM.
He, W.; Gordon, M. L.; Popowski, L.; and Bernstein, M. S. 2023.
Cura: Curation at Social Media Scale. PACM HCI.
Herbrich, T. 2022. Data Clean Rooms. Computer Law Review
International.
Hsu, S.; Vaccaro, K.; Yue, Y .; Rickman, A.; and Karahalios, K.
2020. Awareness, Navigation, and Use of Feed Control Settings
Online. In CHI.
Jhaver, S.; Bruckman, A.; and Gilbert, E. 2019. Does Transparency
in Moderation Really Matter? User Behavior After Content Re-
moval Explanations on Reddit. PACM HCI.
Jhaver, S.; Garimella, K.; De Choudhury, M.; Wilson, C.;
Vashistha, A.; and Mitra, T. 2023. Getting Data for CSCW Re-
search. In CSCW Companion.
Joachims, T.; Granka, L.; Pan, B.; Hembrooke, H.; and Gay, G.
2017. Accurately Interpreting Clickthrough Data as Implicit Feed-
back. SIGIR.
Johnson, T. R.; and Kuhn, K. M. 2013. Bayesian Thurstonian mod-
els for ranking data using JAGS. Behavior Research Methods.
Kampenes, V . B.; Dyb˚a, T.; Hannay, J. E.; and Sjøberg, D. I. K.
2007. A systematic review of effect size in software engineering
experiments. Information and Software Technology.
Kiciman, E.; Counts, S.; and Gasser, M. 2018. Using longitudi-
nal social media analysis to understand the effects of early college
alcohol use. In ICWSM.
Kiene, C.; Monroy-Hern´andez, A.; and Hill, B. M. 2016. Surviving
an ”Eternal September”: How an Online Community Managed a
Surge of Newcomers. In CHI.
Kou, Y .; Ma, R.; Zhang, Z.; Zhou, Y .; and Gui, X. 2024. Commu-
nity Begins Where Moderation Ends: Peer Support and Its Impli-
cations for Community-Based Rehabilitation. In CHI.
Kraut, R. E.; and Resnick, P. 2012.Building successful online com-
munities: Evidence-based social design. MIT Press.
Kulshrestha, J.; Eslami, M.; Messias, J.; Zafar, M. B.; Ghosh, S.;
Gummadi, K. P.; and Karahalios, K. 2017. Quantifying Search
Bias: Investigating Sources of Bias for Political Searches in Social
Media. In CSCW.
Lambert, C.; Choi, F.; and Chandrasekharan, E. 2024. “Positive
reinforcement helps breed positive behavior”’: Moderator Perspec-
tives on Encouraging Desirable Behavior. PACM HCI.
Lambert, C.; Saha, K.; and Chandrasekharan, E. 2025. Does Posi-
tive Reinforcement Work?: A Quasi-Experimental Study of the Ef-
fects of Positive Feedback on Reddit. In CHI.
Liu, A.; Wu, S.; and Resnick, P. 2024. How to Train Your YouTube
Recommender to Avoid Unwanted Videos. In ICWSM.
Makowski, D.; Ben-Shachar, M. S.; Chen, S. A.; and L ¨udecke, D.
2019. Indices of effect existence and significance in the Bayesian
framework. Frontiers in psychology.
Maldeniya, D.; Budak, C.; Robert Jr., L. P.; and Romero, D. M.
2020. Herding a Deluge of Good Samaritans: How GitHub Projects
Respond to Increased Attention. In WWW.
Metaxa, D.; Park, J. S.; Robertson, R. E.; Karahalios, K.; Wilson,
C.; Hancock, J.; Sandvig, C.; et al. 2021. Auditing algorithms: Un-
derstanding algorithmic systems from the outside in. Foundations
and Trends® in Human–Computer Interaction.
Mousavi, S.; Gummadi, K. P.; and Zannettou, S. 2024. Auditing
algorithmic explanations of social media feeds: A case study of
tiktok video explanations. In ICWSM.
O’Sullivan, D. 2019. How fake accounts pushing inflammatory
content went viral – with the help of YouTube’s algorithms | CNN
Business. CNN.
Perriam, J.; Birkbak, A.; and Freeman, A. 2020. Digital methods in
a post-API environment. International Journal of Social Research
Methodology.
Piccardi, T.; Saveski, M.; Jia, C.; Hancock, J.; Tsai, J. L.; and Bern-
stein, M. S. 2024. Reranking Social Media Feeds: A Practical
Guide for Field Experiments. arXiv:2406.19571.
Pogacar, F. A.; Ghenai, A.; Smucker, M. D.; and Clarke, C. L. 2017.
The Positive and Negative Influence of Search Results on People’s
Decisions about the Efficacy of Medical Treatments. In ICTIR.
Poudel, A.; and Weninger, T. 2024. Navigating the Post-API
Dilemma. In WWW.
Rader, E.; Cotter, K.; and Cho, J. 2018. Explanations as Mecha-
nisms for Supporting Algorithmic Transparency. In CHI.
Rader, E.; and Gray, R. 2015. Understanding User Beliefs About
Algorithmic Curation in the Facebook News Feed. In CHI.
Reddit. 2023. Reddit Data API Update: Changes to Pushshift Ac-
cess.
Ribeiro, M. H.; Ottoni, R.; West, R.; Almeida, V . A. F.; and Meira,
W. 2020. Auditing radicalization pathways on YouTube. In FAT*.
Rubin, D. B. 2005. Causal inference using potential outcomes:
Design, modeling, decisions. Journal of the American Statistical
Association.
Saha, K.; Liu, Y .; Vincent, N.; Chowdhury, F. A.; Neves, L.; Shah,
N.; and Bos, M. W. 2021. Advertiming matters: Examining user ad
consumption for effective ad allocations on social media. In CHI.
Salganik, M. J.; Dodds, P. S.; and Watts, D. J. 2006. Experimen-
tal study of inequality and unpredictability in an artificial cultural
market. Science.
Schlessinger, J.; Garimella, K.; Jakesch, M.; and Eckles, D. 2023.
Effects of Algorithmic Trend Promotion: Evidence from Coordi-
nated Campaigns in Twitter’s Trending Topics. InICWSM.

Verma, G.; Bhardwaj, A.; Aledavood, T.; De Choudhury, M.; and
Kumar, S. 2022. Examining the impact of sharing COVID-19 mis-
information online on mental health. Scientific Reports.
Wang, S.; Huang, S.; Zhou, A.; and Metaxa, D. 2024. Lower Quan-
tity, Higher Quality: Auditing News Content and User Perceptions
on Twitter/X Algorithmic versus Chronological Timelines. PACM
HCI.
Wang, Y .; and Diakopoulos, N. 2022. Highlighting High-quality
Content as a Moderation Strategy: The Role of New York Times
Picks in Comment Quality and Engagement. TSC.
Wu, K. J. 2019. Radical ideas spread through social media. Are the
algorithms to blame? PBS.
Yuan, Y .; Saha, K.; Keller, B.; Isomets¨a, E. T.; and Aledavood, T.
2023. Mental Health Coping Stories on Social Media: A Causal-
Inference Study of Papageno Effect. In WWW.
10 Ethics Statement
We acknowledge that curation algorithms are often kept
secret not only to safeguard intellectual property but also
to prevent manipulation by users seeking undue attention
or prioritization. Although our findings improve our under-
standing of these systems, we do not believe that they pro-
vide actionable strategies for malicious actors to compro-
mise trending feeds, such as r/popular. Instead, by examin-
ing these systems, our work promotes transparency by as-
sessing the factors that influence these systems. This analy-
sis is valuable to a variety of stakeholders, as outlined earlier.
Regarding consent, the data used in this study was col-
lected via a publicly accessible API and did not require In-
stitutional Review Board (IRB) approval from our institu-
tion(s). To protect user privacy, no identities have been dis-
closed and we are not releasing the dataset. However, this
study is fully replicable by collecting data snapshots using
Reddit’s API (see Section 3). The dataset is securely stored
on a firewalled, password-protected server at our institu-
tion(s). Additionally, the content of the comments used were
not revealed and were only used to label them as undesired
or non-undesired using an offline instance of Almerekhi,
Kwak, and Jansen (2022)’s BERT model.
A Bayesian Priors for Model 2.2
0 20 40 60 80 100
Current Rank
2.5
5.0
7.5
10.0
12.5Var(Next Rank)
Figure 6: Variance of a post’s rank in the next snapshot (y-
axis) plotted against a post’s rank in the current snapshot
(x-axis).
Our intuition is that it is “easier” to move between ranks
further down the feed (e.g., from 95 to 91) than it is to move
between ranks higher up the feed (e.g., from 5 to 1). In-
deed, based on Figure 6, we saw that the variance of rank in
the next snapshot appears to increase approximately linearly
with the rank in the current snapshot, up until rank 60-80.
Beyond that, the variance appears to decrease due to the fact
that ranks beyond 100 were censored from our dataset. We
used this observation to set strongly informative priors on
our cut points.
First, we assumed that the variance of next rank increases
linearly with the current rank, then the standard deviation
would increase proportionally to the square root of the cur-
rent rank. In other words, this means that posts tend to tra-
verse more ranks the further down the feed, and the number
of ranks they typically traverse increases proportionally to
the square root of the current rank. We can capture this no-
tion in the priors for our cut points by making the gap be-
tween cut points inversely proportional to the square root of
rank. Thus we chose the following priors for our cut points
κk for each rank k:
κk − κk−1 ∼ LogNormal(µ = α√ k , σ= 0.1)
α is a scaling factor with a weakly informative prior of
α ∼ Exponential(λ = 1), and κ1 is fixed to κ1 = α.
We also assume that a post’s next rank will be close
to its current rank. Thus, the intercepts for each current
rank k were given weakly informative priors of βrank=k ∼
Normal(µ = κk, σ= 1).
Finally, the remaining coefficients were given weakly in-
formative priors: β ∼ Normal(µ = 0, σ= 1).

B Stratified Propensity Score Matching
Strata Samples
RQ Variable Strength Cutoff (Control, Treatment) Pre-Filter Post Per Stratum Total
1 & 2 Rec. Comments Weak ≤ Q(0.5) (11), > Q(0.5) 200 97 7,333 711,297
1 & 2 Rec. Comments Strong ≤ Q(0.5) (11), ≥ Q(0.75) (24) 200 14 5,679 79,506
1 & 2 Rec. Und. Weak 0, ≥1 200 124 7,348 911,174
1 & 2 Rec. Und. Strong 0, ≥ Q(0.75) (5) 200 39 2,283 153,342
1 & 2 Prop. Und. Weak ≤ Q(0.5) (18.75%), > Q(0.5) 200 166 6,989 1,160,062
1 & 2 Prop. Und. Strong ≤ Q(0.5) (18.75%), ≥ Q(0.75) (31.25%) 200 89 5,260 468,167
3 Rank Movement Weak ≥0 (down), <0 (up) 100 93 2,521 234,510
3 Rank Movement Strong ≥0 (down), ≤ Q(0.25) (up 3) 100 87 1,672 147,283
Table 6: Summary of the stratified propensity score matching approach adopted to estimate causal effects on the r/popular feed.
Q(n) denotes the percentile cutoff used to binarize treatment and control snapshots—e.g., Q(0.5) is the 50th percentile. The
number following Q(n) denotes the absolute number or percentage resulting from that percentile cutoff—e.g., in the first row
it takes 11 recent comments to reach the 50th percentile.

C GLMs/Hierarchical Bayesian Models
Here, we detail the models used for our causal inference
analyses in Sections 5-7.
RQ1
Recall that we tested multiple treatments and outcomes, with
four treatments (TC-W, TC-S, TU-W, TU-S), and three out-
comes (top 10, 20, and 50). Each treatment/outcome pair
was modeled separately for a total of 4 × 3 = 12 separate
models.
For a particular treatment, let xi = 1 if the i-th observa-
tion was in the treatment condition, and xi = 0 if it was in
the control condition. Then, for a particular outcome Y , the
probability P (Yi|xi) = pi that a post would appear in the top
10 (20, or 50) in the next snapshot was modeled as follows:
logit(pi) = αs[i] + βs[i] xi
Here, s[i] denotes the stratum that the i-th observation was
assigned to, and with separate intercepts αj and coefficients
βj for each stratum. Each interceptαj represents the baseline
(i.e., control) log-odds of appearing in the top 10 (20, or
50) within the j-th stratum. Each coefficient βj corresponds
to the treatment effect in the j-th stratum. To compute the
average treatment effect across all strata, the coefficients βj
were sampled from a hyper-distribution with mean µβ and
standard deviation σβ (the intercepts were pooled in a similar
manner):
βj ∼ Normal(µβ, σβ)
The scalar µβ thus represents the average treatment ef-
fect. Weakly informative priors were placed on these hyper-
parameters (with similar priors on the hyper-parameters for
the intercepts):
µβ ∼ Normal(0, 1)
σβ ∼ HalfCauchy(β = 1)
A posterior distribution for the average treatment effect µβ
was sampled for each treatment/outcome pair with Monte-
Carlo Markov Chain sampling using PyMC. 3
RQ2
Again, recall that we tested multiple conditions and out-
comes, with the same four treatment as before, and three
outcomes (movement up, movement down, no movement).
Each treatment was modeled separately, but the outcomes
were modeled jointly using multinomial logistic regressions,
yielding a total of just 4 models, one for each treatment.
Let the possible values of the outcome Y be up, none,
and down. For each observation i, let P (Yi=up|xi) P (Yi=none|xi) = oup,i be
the odds that the post would move up the feed in the next
snapshot against the not moving in the next snapshot, and
similarly for odown,i. We modeled these odds as follows:
log(oup,i) = αup,s[i] + βup,s[i] xi
log(odown,i) = αdown,s[i] + βdown,s[i] xi
Again, s[i] denotes the stratum that the i-th observation was
assigned to, and with separate intercepts ( αup,j and αdown,j)
3https://github.com/pymc-devs/pymc
and coefficients ( βup,j, βdown,j) for each stratum. Each in-
tercept αup,j represents the baseline (i.e., control) log-odds
of moving up the feed against no movement within the j-
th stratum. Each coefficient βup,j corresponds to the treat-
ment effect in the j-th stratum. The similar applies to αdown,j
and βdown,j. The average treatment effect was modeled in
a similar way as above, with similar priors on the hyper-
parameters. Finally, posterior distributions for average treat-
ment effects µβup and µβdown were sampled for each treatment.
RQ3
For RQ3, we combined consecutive snapshots where there
was no movement in rank into a single observation, yield-
ing observations that spanned varying amounts of time, and
which had rank movements just prior and just after the
spanned time window. For the first two parts, where we in-
vestigated the impact on the number of overall comments
and the number of undesired comments, we followed a sim-
ilar procedure: Let ∆ti be the time spanned during the i-th
observation window, and let Yi be the number of comments
received during that window. We modeled Yi using a nega-
tive binomial distribution with dispersion parameter α:
Yi ∼ NBinom(µ = λi ∆ti, α)
log(λi) = γs[i] + xi βs[i]
Here, λi can be interpreted as the predicted commenting rate
for the i-th observation, which is multiplied by ∆ti to get
the expected number of comments over that time window.
Again, s[i] denotes the stratum that the i-th observation was
assigned to, and with separate intercepts γj and coefficients
βj for each stratum. Each intercept γj represents the base-
line (i.e. control) log-odds of commenting rate within the j-
th stratum. Each coefficient βj corresponds to the treatment
effect in the j-th stratum. The average treatment effect was
modeled in a similar way as above, with similar priors on
the hyper-parameters. Finally, posterior distributions for av-
erage treatment effect µβ were sampled for each treatment.
For the third part, where we investigated the impact on the
proportion of undesired comments, we followed a slightly
different procedure. Let Yi be the number of undesired com-
ments and let ni be the total number of comments received
in the i-th observation window. We modeledYi as follows:
Yi ∼ NBinom(µ = pi ni, α)
logit(pi) = γs[i] + xi βs[i]
Here, pi can be interpreted as the predicted proportion of
undesired comments out of all comments received in the i-
th observation. Each intercept γj represents the baseline log
ratio of undesired comments, and each coefficient βj corre-
sponds to the treatment effect. Average treatment effects µβ
for each treatment were computed in a similar manner as
before.
