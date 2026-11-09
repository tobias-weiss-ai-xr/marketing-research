---
title: 'Buy the Rumor, Sell the News: When Is News Priced In?'
url: https://arxiv.org/abs/2608.14014
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Alireza Kargarzadeh
- Nariman Khaledian
- Navid Parvini
- Sid Ghatak
- Arman Khaledian
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.14014
pages: 9
chars: 48573
fetched_at: '2026-11-08T13:21:51+00:00'
kb_version: 1
---

# Buy the Rumor, Sell the News: When Is News Priced In?

Buy the Rumor, Sell the News: When Is News Priced In?
Alireza Kargarzadeh∗
TailState Intelligence Ltd
London, United Kingdom
alireza.kargarzadeh@tailstate.ai
Nariman Khaledian
Independent Researcher
Antibes, France
nariman.khaledian@gmail.com
Navid Parvini
Zanista AI Ltd
London, United Kingdom
navid.parvini@zanista.ai
Sid Ghatak
Increase Alpha, LLC
Miami, United States
s.ghatak@increasealpha.com
Arman Khaledian
Zanista AI Ltd
London, United Kingdom
arman.khaledian@zanista.ai
Abstract
Two old market sayings hold that news is already priced in by the
time it is published, and that the rumor is bought while the news
is sold. Both are empirical claims about event time: they place the
price move associated with a piece of news before and at publication
rather than after it. Whether the claims hold, for which kinds of
news, and by how much are basic questions about how fast markets
absorb public information. We test them on 4.57 million financial
news articles covering roughly 3,000 US stocks (2023–2026). A
large language model teacher, distilled into a compact classifier
through active learning, assigns each article one of 17 event tags
and five attributes; articles are clustered into stories to separate
first reports from follow-up coverage; and beta-adjusted abnormal
returns are measured around the resulting 1.68 million stock-day
events, with 364,405 neutral-sentiment events as a placebo group.
Three results follow. First, the price move associated with news
concentrates before and at publication: pooled across all signed
events, the cumulative move in the news direction by the close
of publication day is 2.8 times its value twenty days later, and for
rumor-flagged events the directional return is concentrated around
the rumor event, with little incremental return at the subsequent
linked non-rumor event. Second, measured against the placebo of
comparable stocks, markets underreact to numbers and overreact to
stories: quantified fundamental news (earnings, dividends, guidance,
analyst actions) keeps drifting in the direction of the news for
weeks, while soft story-driven news (launches, macro commentary,
leadership) gives back its move. Third, news carries width as well as
direction: neutral news raises publication-day volatility. The study
also produces a table of measured drift for each event tag, usable
as a prior in news-conditioned forecasting models.
CCS Concepts
•Applied computing → Economics;•Computing methodolo-
gies→Natural language processing.
Keywords
Financial news, Event study, LLM distillation, Market efficiency
1 Introduction
Every trading day, thousands of news articles are written about
individual stocks, and a growing share of quantitative systems read
them. Two old sayings surround this flow: that news is already
∗Corresponding author.
priced in by the time it is published, and that the rumor is bought
while the news is sold. Taken literally, both locate the price move
connected to a news event before and at publication rather than
after it. Watching a live news feed makes the question concrete:
often enough, a stock receives plainly good news and its price falls
anyway, or drifts down for weeks after upbeat coverage. Seeing
this repeatedly was the direct motivation for this study. Whether
that is accurate, for which kinds of news, and by how much are
basic questions about how fast markets absorb public information,
and their answers determine what news can and cannot contribute
to forecasting and trading systems.
These questions have stayed open at the scale of the full news
flow because three layers of measurement infrastructure were miss-
ing. The first is tagged events: an earnings report, a lawsuit, and a
promotional listicle are different economic objects that move prices
differently, so each article must be labeled with the kind of event it
reports, at high accuracy and for millions of articles. The second is
story structure: the same event is syndicated and followed up for
days, so repeated coverage must be grouped into one story before
events can be counted. The third is a benchmark for publicity itself:
separating the effect of a news direction from the effect of merely
being in the news requires knowing what happens to a stock that
receives coverage with no direction at all. The recent literature that
applies large language models to financial news documents genuine
return predictability, but it concentrates on prediction and builds
none of these measurement layers.
This paper builds the three layers and runs the measurement.
We introduce a taxonomy of 17 news tags and five attributes, fixed
before this study. Its design drew on a pilot of a subset of large
stocks under an earlier system of 63 loosely defined tags, where the
behavior of prices around each tag guided which tags were kept,
merged, or dropped. A two-step pipeline tags the full corpus: an
Azure-hosted GPT teacher labels a sample, and a small distilled
classifier, refined with active learning, extends the labels to all
4.57 million articles covering roughly 3,000 US stocks (2023 to
2026) at 95 percent fidelity to the teacher and negligible cost. A
clustering step then groups articles into stories, so first reports
separate from follow-up coverage. On this foundation we measure,
quantitatively: when news is priced in and to what extent the two
sayings hold; what pure publicity does to prices, as distinct from
positive or negative coverage; how news moves volatility; and
how story-driven news differs from fundamental news. Returns are
measured as beta-adjusted abnormal returns around 1.68 million
(stock, day, tag) events, with significance from a bootstrap that
1
arXiv:2608.14014v2  [cs.AI]  18 Oct 2026

AI4F ’26, November 14, 2026, Milan, Italy Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Sid Ghatak, and Arman Khaledian
resamples trading dates, and with 364,405 neutral-sentiment events
serving as the built-in placebo for publicity.
The two expressions hold, and the placebo reveals a third fact that
reinterprets much of the raw picture. The news-aligned move sits
overwhelmingly before and at publication, and for rumor-flagged
events, the directional return is concentrated around the rumor
event. A drift that exists with or without news, the residual of the
return benchmark over this sample, is behind what otherwise looks
like widespread post-news reversal; the placebo design removes it.
Net of it, markets underreact to quantified fundamental news and
overreact to soft stories. Section 5 develops each finding with the
evidence.
Contributions.Our contribution is measurement and reinter-
pretation, not methodological novelty. (1) A scalable recipe for
labeling multi-million article corpora by distilling a large language
model teacher into a compact classifier, at 95 percent agreement
with its Azure GPT teacher and negligible cost. (2) The largest
tagged, placebo-controlled measurement of where news-aligned
price moves sit in event time that we are aware of. (3) The background-
drift correction, which reinterprets post-news reversal, the apparent
asymmetry between good and bad news, and a class of news-fading
strategies. (4) A per-tag, per-attribute, per-size drift table usable
as a ranking and importance-sampling prior for news-conditioned
forecasting models.
2 Related work
Recent work on LLMs and equity news splits into three strands. The
first asks whether LLM-extracted sentiment predicts returns: Lopez-
Lira and Tang [17] show ChatGPT headline scores predict next-day
returns, Chen et al. [2] extend the exercise to market and macro
prediction, Kirtac and Germano [14] trade LLM sentiment signals,
and Iacovides et al. [9] fine-tune open models for the same task; Kim
et al. [13]apply LLMs to fundamental analysis and Papasotiriou et al.
[19] to stock ratings, and Ghafouri et al. [6] probe the behavioral
signatures of the models themselves. Kargarzadeh [11] and Ghatak
et al. [7] combine LLM news signals with macroeconomic and
technical indicators in trading frameworks. Chen et al. [3] extract
news embeddings across 16 markets and find short-horizon news
momentum that persists for days in small stocks, a finding our
adjusted earnings and analyst drifts echo from the event side. Jadhav
and Mirza [10] review LLM applications in equity markets and find
the literature concentrated on sentiment extraction and return
prediction; Cao et al . [1] draw the same picture for quantitative
investment more broadly, with news entering models as a predictive
feature rather than as an object of measurement. Our question is
different: we do not build a predictor, we measure where in event
time the news-aligned move sits, and our placebo design shows
that a naive reading of post-news drift would mislead exactly the
strategies this strand builds.
The second strand structures news into events rather than senti-
ment scalars. Li et al. [15] learn structured event representations
for return prediction, Wang et al. [20] maintain an event memory
for forecasting, and Li et al. [16] train end-to-end event-driven trad-
ing policies. These systems need to know which event tags matter
and how fast their information decays; our measured drift table
is exactly that prior, estimated on 1.68 million events rather than
learned end to end.
The third strand is methodological. Pangakis and Wolken [18]
and Xia et al. [21] show that distilling LLM-generated labels into
small supervised classifiers matches human annotation quality at
a fraction of the cost; our tagging pipeline is an industrial-scale
instance with per-tag validation, and Khaledian et al. [12] cut the
cost of retrieval over financial text along similar lines. Gao et al .
[5] and Chen and Pu [4] document look-ahead risks when LLMs
generate forecasts from text they may have memorized, and He
et al. [8] train chronologically consistent models to avoid them; our
design sidesteps the problem, since the LLM only assigns event tags
and attributes, never forecasts, and the corpus is produced daily in
live operation.
3 Data
The corpus comes from NewsWitch, a commercial financial-news
product developed by Zanista AI Ltd that has run in daily pro-
duction since the beginning of 2024. 1 Each day it processes over
a quarter million news URLs concerning the roughly 3,000 most-
covered US-listed stocks, drawn from a crawl of more than half
a million sources; over the sample this amounts to more than 70
million raw articles. The 4.57 million retained here are the impor-
tant ones: deduplicated, financial in nature, and directly related
to the covered stock universe. For every crawled article, the title,
body, and metadata are read by an LLM that decides whether the
article is genuinely related to the stock and important enough to
keep, assigns a sentiment direction on five levels from strongly neg-
ative to strongly positive, and writes a summary; retained articles
carry these fields along with the publication timestamp and source
domain. The corpus has supported earlier studies of LLM-driven
trading and retrieval [7, 11, 12]. Sentiment and summaries in the
live period are produced day by day, with no access to subsequent
returns. Our event tags were assigned retrospectively, by a classifier
trained later; they are descriptive labels of what an article reports,
not forecasts, and the teacher-only cut in Section 5.3 shows the
findings do not depend on the classifier or its training vintage. The
2023 portion was backfilled in bulk, is under 3% of signed events,
and shows the same patterns as the live years. Prices are daily ad-
justed closes for 2,591 tradeable symbols; 3.4% of articles reference
symbols without price history (delistings skew small), and 9.7% of
events are skipped for missing price windows.
4 Method
Our method has three stages: tag every article with a distilled LLM
tagger, group articles into stories and events, and measure abnormal
returns around those events against a placebo.
4.1 Distilled LLM tagging
A frozen prompt presents 17 event-tag definitions, five binary at-
tribute definitions (scheduled, forward looking, primary source,
quantified, rumor), and four example articles with their completed
labels to a small GPT teacher (gpt-5-mini, hosted on Azure) with
a strict JSON schema, at about $0.0002 per article. The taxonomy
covers real corporate events (earnings, guidance, analyst actions,
1For access to NewsWitch data, contact info@zanista.ai.
2

Buy the Rumor, Sell the News: When Is News Priced In? AI4F ’26, November 14, 2026, Milan, Italy
launches, M&A, legal and regulatory, and so on) and deliberately in-
cludes two junk categories, price commentary and promotional con-
tent, so that articles describing price action or promotion have some-
where to go other than a real event tag. The teacher labeled 29,472
random articles; a distilroberta-base student (82M parameters, seven
heads: primary tag, secondary tag, five attributes) trained on these
labeled 600,000 fresh articles; the 100,000 lowest-confidence articles
went back to the teacher (uncertainty sampling, with a quota for
rare tags); and the student was retrained on the merged 129,463
labels (29,472 + 99,991; nine of the 100,000 produced no usable la-
bel). On a held-out 10,000-article sample labeled independently by
both, the student agrees with the teacher on 87.5% of primary tags
overall and 94.0% at confidence≥ 0.8(85% of articles); attribute
agreement is 92–99%. Deployment uses the classifier everywhere,
routes the 15% low-confidence tail back to the teacher, and keeps
teacher labels where they exist, for an estimated 95% corpus-wide
teacher fidelity at a cost of $29.34 for the 139,464 teacher calls that
trained and validated the classifier, and $156.29 in total including
the routed tail. Every article records its label source, which powers
a robustness check below. Inference runs at 125–160 articles per
second on a MacBook Pro laptop (M4 Pro, 24 GB RAM).
4.2 From articles to events
Bundling repeated coverage into distinct events is a hard problem
in its own right, and we solve it with a two-step, embedding-based
clustering. Within each stock-day, articles are clustered on the
cosine similarity of their title-and-summary embeddings (threshold
0.80), restricted to the same primary tag; each day-cluster is then
matched against the stock’s running stories, so an event continues
across days when later coverage stays close to the story’s frozen
centroid. The clustering quantifies how much news repeats itself:
it reveals that 55% of all articles are follow-up coverage of a story
already running, and it flags each article as the first report (NEW) or
follow-up. How long a story may stay open depends on its tag: we
calibrated per-tag lifetimes by tracking how the similarity of later
same-story coverage to the first-day centroid decays with story
age, and capped each tag where continued matches become rare.
M&A and legal sagas stay open for up to 90 days, leadership and
operations stories for weeks, commentary for two days; measured
persistence per tag is reported in Table 1. For the event study, an
event is a (stock, trading day, tag) aggregate: articles published after
16:00 New York time roll to the next trading day, and the article
count is retained as an attention measure. The event’s impact comes
from the vendor sentiment: each article carries one of five levels,
and the event’s impact averages its articles. An event is neutral
when every one of its articles is Neutral, and signed otherwise. The
drift tables use only the sign of the impact. This yields 1,862,297
events, of which 1,681,657 are scored against prices: 1,317,252 signed
(73% positive) and 364,405 neutral.
4.3 Measurement design
Let𝑟𝑡 be the stock’s daily return and 𝑟𝑚,𝑡 the daily return of the
S&P 500 index, measured through SPY, the exchange-traded fund
that tracks it. The abnormal return is𝐴𝑅𝑡 =𝑟𝑡−𝛽𝑡𝑟𝑚,𝑡 with𝛽𝑡 a
rolling 252-day OLS beta of the stock against the S&P 500, as of
day𝑡 (minimum 126 observations, missing betas set to 1). Around
Table 1: Story persistence by tag, measured from the cluster-
ing: number of stories and mean lifetime in trading days.
Tag Stories Days Tag Stories Days
M&A deal 22,596 12.9 Macro through stock 322,666 1.1
Legal, regulatory 46,846 10.6 Financing, dilution 11,497 0.9
Insider, ownership 119,394 4.0 Product launch 159,672 0.9
Analyst action 99,847 2.5 Competition 32,131 0.8
Leadership 53,794 2.4 Partnership 103,199 0.8
Operations, supply 89,071 2.3 Price commentary 220,451 0.6
Earnings results 89,433 2.3 Other corporate 100,891 0.5
Capital returns 21,796 1.6 Promotional 93,974 0.4
Guidance, outlook 24,343 1.4
each event day we cumulate 𝐴𝑅 over four windows: days−5..0
(which includes day 0), day 0, days +1..+ 5, and days+6..+ 20.
Signed events are stacked by sentiment sign 𝑠∈ {−1,+ 1}, so a
move in the direction of the news counts as positive whether the
news was good or bad. Significance comes from a cluster bootstrap
that resamples trading dates (5,000 draws), because events on the
same day are cross-sectionally correlated. For size buckets, stocks
are split each year into three equal-sized groups (small, mid, large)
by dollar volume.
The placebo and the adjusted estimator.A single-beta bench-
mark is deliberately simple: transparent, replicable, and standard.
No fixed benchmark tracks every stock perfectly, and whatever
residual drift a benchmark leaves behind flows into every event win-
dow measured against it. The design therefore includes a placebo
rather than a bet on the benchmark. Neutral events carry coverage
without direction, so their drift measures what happens to compa-
rable stocks of the same size around news days in general. Call that
the baseline𝑏𝑘,𝑤 , the mean abnormal return of neutral events in
size bucket𝑘 over window𝑤. When we want the effect of the news
direction itself, we subtract the baseline from the event’s abnormal
return before applying the sign: 𝑠(𝐴𝑅 𝑤−𝑏𝑘,𝑤). Throughout the
paper,adjustedmeans exactly this, the move in the news direction
in excess of what comparable stocks drifted anyway, andrawmeans
no subtraction. Because the baseline is measured against the same
benchmark as the events, any benchmark misfit appears on both
sides of the subtraction and cancels: a richer factor model would
shrink the baseline itself but leave the adjusted estimates essentially
unchanged. Raw and adjusted columns are reported side by side.
Two implementation details matter for inference. First, the base-
line is pooled across event tags within a size bucket, which assumes
coverage drift is tag-independent. A tag-matched variant, which
subtracts each tag’s own neutral baseline per bucket, leaves the
earnings continuation and the macro, leadership, and competition
reversals essentially unchanged, while the capital-returns estimate
shrinks and the launch estimate crosses zero; neutral coverage of
those two tags selects unusual stocks (dividend payers, promoted
small caps), so their magnitudes are more model-dependent than
their signs. Second, the baseline is estimated once, on the full neu-
tral sample; a bootstrap that re-estimates it inside every draw gives
the same or slightly stronger significance for every headline tag, so
ignoring baseline noise in the reported p-values is conservative.
What this design can and cannot claim.Sentiment is assigned
to articles, and articles are written about moves as well as before
3

AI4F ’26, November 14, 2026, Milan, Italy Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Sid Ghatak, and Arman Khaledian
them, so the pre-publication drift mixes genuine anticipation with
reporting on moves that already happened. We quantify this with
the NEW-only rerun: restricting to first reports shrinks the earnings
pre-window from+1.41%to+1.02%, so follow-up coverage inflates
measured anticipation by roughly a third, and all post-publication
conclusions are unchanged. Articles can also describe moves that
already happened, so sentiment labels may partly encode realized
returns. Our study is a descriptive account of where the news-
aligned move sits in event time, not a causal claim about news
moving prices.
5 Results
Our main findings are as follows. First, the news-aligned move sits
before and at publication, and rumor-flagged events show the buy
the rumor, sell the news pattern literally (Section 5.1). Second, a
background drift that exists with or without news explains most of
the raw post-news picture (Section 5.2). Third, net of the baseline,
quantified fundamental news drifts and soft news reverses, and the
pattern survives every robustness cut (Section 5.3). The remain-
ing sections measure source differences, volatility, and economic
significance.
5.1 The move sits before and at publication
Table 2 is the master table; Figure 1 (left) shows the event-time
picture. Almost every pre and day-0 column in the raw table is pos-
itive: whatever the market does around news, it agrees in direction
with the news before the news is out. For the quantified fundamen-
tal tags the pattern is extreme: earnings +1.41%pre and +0.42%
on the day against−0.05%afterwards; analyst actions+1.12%and
+0.22%against−0.13%; price commentary, guidance, and competi-
tion all show the same shape. A useful summary comes from the
running total plotted in Figure 1: starting five days before publi-
cation, add up each day’s average abnormal return in the news
direction. Pooled across all signed events, this running total reaches
+0.579%by the close of publication day, then falls back and ends
day+20at+0.204%. The ratio of the two levels is 2.84: by the clos-
ing bell of publication day the market had already moved almost
three times as far as where it would stand a month later, and the
extra ground was given back over the following weeks. The ratio
measures how complete the move was, not how large: earnings
events have the largest moves but almost no give-back, so their
ratio is 1.06, against 1.20 for analyst actions and 1.08 for guidance;
at or above one throughout, the move was finished, or more than
finished, when publication day ended. The pooled ratio is higher
than any single tag’s because the pooled after-window also inherits
the background drift examined in Section 5.2.
The rumor attribute makes the expression measurable (Table 3).
Among 18,618 rumor-flagged signed events, 94% are followed by
a non-rumor event with the same tag within 60 trading days (me-
dian gap two trading days). The rumor day delivers+0.36%in the
rumor’s direction. Between rumor and confirmation the stock adds
nothing (−0.09%). The confirmation day itself is worth+0.01%, and
days +6 to +20 after confirmation give back−0.06%. M&A rumors
are the sharpest case:+0.24%on rumor day, then−0.32%into the
confirmation,−0.10%on the news, and−0.37%after it. Note that the
linked event is the next same-tag, non-rumor event for the same
stock; therefore these numbers represent returns around linked
pairs. Consistent with this, events preceded by a same-tag rumor
in the prior month show no additional drift after the news.
5.2 The background drift and the placebo
The placebo was designed as a calibration check and became a
finding. Neutral events measure what happens to a stock around
news days that carry no direction; quiet stock-days, defined as days
with no event for the stock and none in the prior five trading days,
measure the same windows with no news at all. Both drift down.
Over the following month, stocks with neutral coverage trail their
beta benchmark by−0.92%among small caps,−0.58%among mid
caps, and−0.34%among large caps; quiet days drift−0.74%,−0.88%,
and−0.59%in the same buckets (Figure 2). The two sets of numbers
tell one story. The drift is not caused by publicity: it is the residual
of the single-beta benchmark over this sample, present with news
and without, of the same order across size groups, with covered
small caps adding a modest0.2%per month on top and covered mid
and large caps adding none. This is exactly why the design subtracts
a placebo instead of trusting any benchmark: news studies inherit
a drift that exists with or without news, and any measurement or
strategy that scores news direction without a placebo of comparable
stocks will misread that drift as directional information.
To see how this distorts directional measurements, take an aver-
age positive-news event in a small cap. Its raw post-event drift is
the sum of two parts: the market’s reaction to the news direction,
plus the−0.9%that any covered small cap drifts over the following
month anyway. Measured in the direction of the news, that second
part shows up asreversalof good news. Now take a negative-news
event in the same stock: the same−0.9%drift now points in the
same direction as the news, so it shows up ascontinuationof bad
news. One underlying drift, two apparent behaviors. Because 73%
of signed events are positive, the pooled average is dominated by
the first case, which is why the raw table looks like widespread
reversal.
The adjusted estimator of Section 4.3 removes exactly this con-
found, and three apparent anomalies disappear at once (Figure 3).
The apparent asymmetry between good and bad news: raw drift
over days +6 to +20 is−0.62%after positive news (looks like over-
reaction to good news) and+0.63%after negative news (looks like
underreaction to bad news); after the baseline is subtracted, both
are within0 .02%of zero ( 𝑝≈ 0.9). The size gradient: small caps
appear to reverse 2.4 times more than large caps in the raw data
(−0.41%against−0.17%per month), and adjusted, the gradient is
gone. And the one apparent continuation winner in the raw table,
legal and regulatory news (+0.29%,𝑝< 0.001): legal news is one of
only two tags where most events are negative (83%; competition is
the other, at 60%), so for this tag the baseline reads as continuation
rather than reversal; adjusted, legal news drifts−0.08%(𝑝= 0.22),
indistinguishable from any other covered stock.
5.3 What survives: the tag map
Figure 4 and the adjusted columns of Table 2 give the residual struc-
ture, and it is orderly. On the continuation side sit the quantified fun-
damental tags: capital returns+0.35%, earnings+0.22%, guidance
+0.13%, analyst actions+0.10%over days +6 to +20, all significant;
4

Buy the Rumor, Sell the News: When Is News Priced In? AI4F ’26, November 14, 2026, Milan, Italy
Table 2: Signed abnormal drift by event tag, sorted by adjusted post-event drift. All columns are percent, in the direction of the
news. “%pos” is the share of positive-sentiment events. “adj. ” subtracts the baseline of the event’s size bucket before signing
(Section 4.3);𝑝 adj is the date-bootstrap p-value of the adjusted days+6..+20drift.
Event tag𝑛%pos−5..0day 0+1..+5+6..+20adj.+6..+20𝑝 adj
Capital returns 26,273 90 +0.22 +0.06 -0.01 -0.14 +0.35<0.001
Earnings results 107,174 72 +1.41 +0.42 -0.04 -0.05 +0.22<0.001
Guidance and outlook 24,828 69 +1.43 +0.56 -0.02 -0.09 +0.13 0.046
Analyst action 134,464 70 +1.12 +0.22 -0.05 -0.13 +0.10 0.012
Price commentary 174,087 61 +1.55 +0.43 -0.02 -0.03 +0.09 0.053
Promotional content 55,230 96 -0.01 0.00 -0.11 -0.43 +0.08 0.274
Financing and dilution 9,161 78 +0.77 +0.30 +0.02 -0.28 +0.07 0.554
Operations and supply 59,613 57 +0.45 +0.14 +0.02 -0.05 +0.04 0.314
Insider and ownership 238,236 70 +0.16 +0.04 -0.06 -0.21 +0.03 0.459
M&A deal 25,962 84 +0.17 +0.04 -0.23 -0.46 -0.05 0.498
Partnership, customer 76,848 97 +0.08 +0.05 -0.19 -0.63 -0.08 0.317
Legal and regulatory 46,057 17 +0.83 +0.19 +0.11 +0.29 -0.08 0.220
Other corporate 47,485 82 0.00 +0.04 -0.16 -0.48 -0.09 0.200
Competition 20,744 40 +0.90 +0.32 -0.09 -0.08 -0.17 0.026
Leadership, governance 30,388 75 +0.28 +0.08 -0.10 -0.51 -0.18 0.016
Product launch 101,425 96 -0.03 +0.03 -0.22 -0.73 -0.18 0.022
Macro through stock 139,277 82 +0.04 +0.05 -0.22 -0.76 -0.34<0.001
−5 0 5 10 15 20
Trading day relative to publication
−1.0
−0.5
0.0
0.5
1.0
1.5
Cumulative abnormal return
in news direction (%)
Raw
−5 0 5 10 15 20
Trading day relative to publication
0.0
0.5
1.0
1.5
2.0
Net of the background drift
Earnings
Analyst
Product launch
Macro through stock
Legal and regulatory
Neutral news (placebo)
Figure 1: Cumulative abnormal return in the news direction around publication (day 0), five event tags plus the neutral placebo.
Left: raw. Right: net of the background drift. Bands are ±2date-clustered standard errors. Raw curves show the priced-in
signature (the move precedes publication) and near-universal post-news decay tracking the placebo. Adjusted curves separate
genuine continuation (earnings, analyst) from genuine reversal (launches, macro), and flatten legal and regulatory news to the
baseline.
the earnings figure is the familiar post-earnings-announcement
drift recovered at corpus scale from tagged news alone. On the re-
versal side sit the soft, attention-driven tags: macro read-throughs
−0.34%, product launches−0.18%, leadership stories−0.18%, compe-
tition−0.17%. Launch and partnership coverage is 96–97% positive,
the most promotional corner of the corpus, and it is precisely where
prices overshoot.
5

AI4F ’26, November 14, 2026, Milan, Italy Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Sid Ghatak, and Arman Khaledian
Table 3: Buy the rumor, sell the news. Mean abnormal return
in the rumor’s direction (percent) at each stage, for rumor-
flagged events with a same-tag non-rumor event within 60
trading days.
Sample𝑛Rumor day Rumor→news News day+1..+5+6..+20
All rumor events 17,510 +0.36 -0.09 +0.01 -0.14 -0.06
M&A deal 3,335 +0.24 -0.32 -0.10 -0.16 -0.37
Legal and regulatory 1,452 +0.55 -0.01 -0.01 +0.17 -0.17
Product launch 2,316 +0.13 +0.12 -0.08 -0.35 +0.02
Days -5..0 Day 0 Days +1..+5 Days +6..+20
−0.8
−0.6
−0.4
−0.2
0.0
Abnormal return of stocks with
neutral coverage (%)
Dollar-volume group
Small
Mid
Large
Figure 2: The background drift: abnormal returns of stocks
receiving neutral news, by window and size group. Quiet
stock-days with no recent news drift similarly (Section 5.2):
the drift is the residual of the single-beta benchmark over
this sample, not an effect of publicity, and the placebo adjust-
ment removes it either way.
Positive news Negative news
−0.6
−0.4
−0.2
0.0
0.2
0.4
0.6
Drift +6..+20 in
news direction (%)
Raw
Net of background drift
Figure 3: The asymmetry illusion. Raw post-news drift sug-
gests good news reverses and bad news continues. Once the
baseline is subtracted, both collapse to zero: the apparent
asymmetry is the baseline interacting with the 73% positive
share of news sentiment.
Table 4 stress-tests the map with three cuts. The first keeps
only NEW articles (1.09M events), removing all follow-up coverage.
The second addresses simultaneous stories: a covered stock-day
typically carries more than one event tag at once (the median is
two), so drift attributed to a launch could in principle belong to a
co-occurring earnings story; restricting to stock-days with exactly
−0.8 −0.6 −0.4 −0.2 0.0 0.2 0.4
Abnormal drift, days +6 to +20,
in news direction (%)
Macro through stock
Product launch
Leadership
Competition
Other corporate
Legal and regulatory
Partnership
M&A
Insider and ownership
Operations
Financing and dilution
Promotional
Price commentary
Analyst
Guidance
Earnings
Capital returns
Raw drift
Figure 4: The tag map: adjusted drift over days +6 to +20 in the
news direction (bars; pale bars not significant at 5%) against
raw drift (circles). Adjustment moves every tag toward zero
and reorders them: quantified fundamentals drift, soft news
reverses.
Table 4: Robustness of the adjusted days+6..+ 20drift (per-
cent). Columns: all events; NEW articles only; stock-days
with one event tag; events labeled directly by the GPT teacher.
Event tag All events NEW only Single-tag days Teacher labels
Capital returns +0.35 +0.33 +0.47 +0.34
Earnings results +0.22 +0.11 +0.17 +0.11
Guidance and outlook +0.13 +0.06 +0.34 +0.08
Analyst action +0.10 +0.07 -0.05 +0.08
Legal and regulatory -0.08 -0.07 -0.25 -0.01
Product launch -0.18 -0.18 -0.48 -0.14
Leadership, governance -0.18 -0.14 -0.26 -0.17
Macro through stock -0.34 -0.26 -0.52 -0.24
one event tag removes that contamination. The third addresses
classifier error: recomputing only on events whose articles were
labeled directly by the GPT teacher, bypassing the distilled clas-
sifier entirely, tests whether tagging mistakes create the patterns.
Across the three cuts the headline tags keep their signs and simi-
lar magnitudes, with one exception: analyst actions flip to−0.05%
on single-tag days. The exception has a natural reading: analyst
notes rarely appear without other same-day coverage (fewer than
seven percent of analyst events sit on single-tag days), so that
cell is a small and unusual subsample. Single-tag days otherwise
strengthen the survivors (capital returns+0.47%, launches−0.48%,
macro−0.52%). By year, the raw pooled reversal halves from 2024
(−0.49%) to 2026 (−0.18%), and the adjusted pooled drift is small
in every year (−0.16%to+0.07%). Finally, because seventeen tags
are tested at once, we apply Benjamini-Hochberg control to the
adjusted p-values of Table 2: at a 5 percent false discovery rate the
macro reversal and the capital-returns and earnings continuations
survive, the analyst, leadership, launch, and competition results
sit at the boundary (𝑞 between 0.05 and 0.07), and the guidance
continuation is suggestive rather than decisive.
6

Buy the Rumor, Sell the News: When Is News Priced In? AI4F ’26, November 14, 2026, Milan, Italy
Table 5: News source groups. NEW share is the fraction of
articles that are the first report of their story; day-0|𝐴𝑅| ratio
is the publication-day absolute move as a multiple of the
stock’s normal day. Events here are (stock, day, tag, source
group) aggregates, so a story covered by several source groups
appears once per group; counts therefore exceed the number
of signed events.
Source group𝑛NEW share−5..0day 0 day-0|𝐴𝑅|ratio adj.+6..+20
Retail analysis 224,122 50% +1.07 +0.41 1.28 +0.09
Portals 294,359 55% +0.92 +0.28 1.22 +0.11
Mainstream media 70,616 49% +0.86 +0.38 1.26 +0.01
Aggregators 544,809 38% +0.80 +0.21 1.12 +0.06
Other 475,705 63% +0.46 +0.17 1.07 -0.12
Press wires 117,517 60% -0.06 +0.05 1.17 -0.19
Attributes slice the same way (not tabulated for space): scheduled
events show more anticipation and slightly positive adjusted drift
(+0.08%,𝑝= 0.03), unscheduled events none; quantified articles
show no drift, unquantified ones reverse (−0.12%,𝑝= 0.01); rumor-
flagged events show the largest pre-windows. Publication timing
matters for the day itself: articles published during market hours
land on a day that moves 1.18 times the stock’s normal absolute
move, against 1.05 for overnight publications.
5.4 Sources are not interchangeable
Grouping events by the kind of outlet that wrote them (Table 5)
separates anticipation from information. Retail-analysis sites, por-
tals, mainstream media, and aggregators all show+0.8%to+1.1%
of pre-publication drift: they write about moves in progress. Press
wires, which carry company and regulator releases, show none
at all (−0.06%): the release is the event, not commentary on one.
Wire-sourced positive tilt also reverses hardest (−0.19%adjusted,
marginal), consistent with promotional press releases overselling.
At the level of individual outlets, which we leave unnamed, the
two with the most promotional catalogs show economically large
negative adjusted drift (−0.4%to −0.8%per month), suggesting
a source-quality signal that survives the baseline; we leave a full
source-reputation study to future work.
5.5 Second moments: news carries width
Neutral news is directionally empty but not informationless. Neu-
tral guidance events come with publication-day moves 1.29 times
the stock’s normal day and 1.23 times over the following week;
neutral earnings 1.11 times. Attention scales the effect: days with
ten or more articles move 1.36 times normal against 1.05 for single-
article days. All of these are ratios of a stock’s absolute move to its
own typical day, so the background drift of Section 5.2, tiny at the
daily scale, does not enter them. A distributional forecaster should
therefore read event tags as width signals, widening on scheduled
disclosure events, independent of direction.
5.6 Economic significance
Table 6 is an in-sample diagnostic of the two raw patterns a practi-
tioner would be tempted to trade, not evidence of a tradable strategy.
Both are calendar-time portfolios built the same way: a position
opens at the close of day +5 after a qualifying event and closes at
Table 6: Calendar-time portfolios, days +6 to +20, abnormal
returns, 2023 to 2026. Net Sharpe ratios charge the stated cost
per side.
Strategy Events Ann. ret. Sharpe Sharpe 5 bps 10 bps 20 bps
Fade small-cap launch, partnership 52,149 15.8% 1.35 1.20 1.06 0.77
Short any covered small cap 260,472 15.9% 1.35 1.21 1.07 0.78
Follow legal and regulatory 46,057 4.1% 0.66 0.39 0.12 -0.43
2023 2024 2025 2026
0
20
40
60Cumulative return (%)
Fade small-cap launch and partnership
Short any covered small cap
Follow legal and regulatory
S&P 500 buy and hold
Figure 5: Cumulative returns of the calendar-time portfolios,
each hedged with a beta-sized index position, next to an S&P
500 buy and hold. The sentiment-fading strategy (orange)
is indistinguishable from shorting every covered small cap
(dashed): the news direction adds nothing.
the close of day +20 (the window where the drift lives), all open
positions are equally weighted and rebalanced daily, and returns
are measured on beta-hedged abnormal returns, so the portfolios
are market-neutral overlays. Concretely, each position is a stock leg
plus an offsetting beta-sized position in the index, so the returns and
Sharpe ratios reported here are the realized returns of that hedged
implementation. The first strategyfadessmall-cap launch and part-
nership news: after a positive-sentiment launch or partnership
event in a small cap it shorts the stock, after a negative-sentiment
one it buys, betting that the sentiment move reverses. It earns 15.8%
annualized gross with a Sharpe ratio of 1.35 and survives 20 bps of
cost per side (Sharpe 0.77). The benchmark strategy ignores sen-
timent entirely: it shortseverysmall-cap stock that appeared in
the news at all, neutral or signed, over the same windows. It earns
15.9% with the same Sharpe of 1.35, and the two cumulative curves
lie on top of each other (Figure 5). The fading strategy’s entire edge
is the background drift; the news direction contributes nothing.
Following legal and regulatory news direction, the raw table’s con-
tinuation candidate, earns a Sharpe of 0.66 gross that dies at 10 bps,
as the composition argument predicts. Both headline strategies are
predominantly short books, and the cost model charges only a flat
fee per side: borrow fees and locate availability are not modeled,
and for small caps they would consume a further slice of the returns.
The residual tag-map alphas (earnings continuation at+0.22%per
event over 15 days) are real but thin relative to plausible costs.
7

AI4F ’26, November 14, 2026, Milan, Italy Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Sid Ghatak, and Arman Khaledian
6 Implications for news-conditioned forecasting
These measurements bear directly on the design of news-conditioned
forecasting systems, in three ways. First, ranking: when a day’s
news must be compressed into a short context, event lines should
be ordered by the measured per-tag, per-attribute, per-size drift
priors rather than by source reputation heuristics. Second, represen-
tation: since direction is mostly priced in at publication while width
effects persist, the text should be encoded as tagged, flagged event
lines (tag, scheduled, rumor, primary source, NEW or follow-up
age) rather than as sentiment scalars; the tag and flags carry the
durable information. Third, evaluation: any claimed news alpha
should be benchmarked against a coverage-presence baseline of
the kind measured here, or it will rediscover the baseline and call it
signal.
7 Limitations
Five limitations frame how far these results reach, and each points
at follow-up work. The first concerns labels. Sentiment and sum-
maries come from the corpus vendor’s LLM, and our event tags are
layered on top by a distilled classifier that disagrees with its teacher
on about one article in eight. Those disagreements concentrate
in the two junk categories, price commentary and promotional
content, where a wrong label matters least, and the teacher-only
check in Table 4 shows the conclusions do not depend on them.
Still, a mislabeled article can end up attached to the wrong story,
so cleaner labels would sharpen the clustering as well. The second
concerns the return benchmark. Each stock is hedged with a single
market beta, so style effects such as size are not explicitly modeled;
the placebo adjustment absorbs much of this, because the baseline
is measured within size buckets, but a formal multi-factor treatment
is a natural next step. Third, timing. Daily closes cannot separate
the trading-hours reaction from the overnight gap, and the sample
covers 2023 to 2026, a single market regime whose year-by-year
decay suggests the residual patterns are already fading; the 2023
slice is backfilled rather than live. Fourth, the corpus is public news,
the news available on the open internet, which is what most market
participants actually read. It is in the nature of public information
that by the time an event is written up in an article anyone can
access, some of it has already moved through filings, terminals,
and professional channels; this holds for any collection of public
news, and part of what we measure as anticipation is this property
of public information itself. Public news is largely priced by the
time it appears, but it is not empty: Kargarzadeh[11] builds trading
strategies on public news of this kind, combined with macroeco-
nomic indicators in a momentum-style framework, and reports
good results, and our tag map shows where such residual informa-
tion lives. Finally, the economic significance exercise is deliberately
simple: fixed windows, equal weights, flat costs. It is built to price
the measured patterns, not to be a trading system. Richer strategies
can certainly be developed on this data; here the focus is on how
news is priced, and we leave strategy design to future work.
8 Conclusion
We asked when news is priced in, and we answered it at the scale
of the full news flow. Both market sayings describe the data well.
Across 1.68 million tagged events, the price move connected to
a news event lives before and at publication: anticipation builds
over the preceding days, publication day absorbs what remains,
and the weeks after add nothing that was not already there. For
rumor-flagged events, the directional return is concentrated around
the rumor, with little added at the next linked event.
The measurement also shows how easily news gets more credit
than it deserves. Stocks drifted below a standard beta benchmark
across this sample whether they were in the news or not, and
without a placebo of comparable stocks that drift reads as reversal
of good news, continuation of bad news, and profitable-looking
strategies that fade news sentiment. Subtracting the placebo makes
these illusions disappear together, and what remains is our simplest
lesson about how news is priced: markets underreact to numbers
and overreact to stories. Hard, quantified disclosures keep drifting
in their own direction for weeks after publication, and soft narrative
coverage gives back its move.
For anyone building forecasting or trading systems on news, the
durable information is the kind of event, the fact and intensity of
coverage, and its width.
Acknowledgments
This work was carried out at TailState Intelligence Ltd. The NewsWitch
news corpus and its data infrastructure were provided by Zanista
AI Ltd. We thank the Zanista AI team for data access and support.
References
[1] Bokai Cao, Saizhuo Wang, Xinyi Lin, Xiaojun Wu, Haohan Zhang, Lionel M. Ni,
and Jian Guo. 2025. From Deep Learning to LLMs: A Survey of AI in Quantitative
Investment.arXiv preprint arXiv:2503.21422(2025).
[2] Jian Chen, Guohao Tang, Guofu Zhou, and Wu Zhu. 2025. ChatGPT and
DeepSeek: Can They Predict the Stock Market and Macroeconomy?arXiv preprint
arXiv:2502.10008(2025).
[3] Yifei Chen, Bryan T. Kelly, and Dacheng Xiu. 2026. Expected Returns and Large
Language Models. SSRN working paper 4416687, revised February 2026. https:
//ssrn.com/abstract=4416687
[4] Zefeng Chen and Darcy Pu. 2026. Autonomous Market Intelligence: Agentic AI
Nowcasting Predicts Stock Returns.arXiv preprint arXiv:2601.11958(2026).
[5] Zhenyu Gao, Wenxi Jiang, and Yutong Yan. 2025. Detecting Lookahead Bias in
LLM Forecasts.arXiv preprint arXiv:2512.23847(2025).
[6] Mohammadreza Ghafouri, Nazanin Yousefi, Arian Akbari, Reza Tavakoli, Farbod
Davoodi, Gholamali Aminian, Nariman Khaledian, and Arman Khaledian. 2025.
Risk, Ambiguity, and Infinity: Behavioral Signatures of Modern Large Language
Models. SSRN working paper 5688064. doi:10.2139/ssrn.5688064
[7] S. Ghatak, Arman Khaledian, N. Parvini, and Nariman Khaledian. 2025. Increase
Alpha: Performance and Risk of an AI-Driven Trading Framework.arXiv preprint
arXiv:2509.16707(2025).
[8] Songrun He, Linying Lv, Asaf Manela, and Jimmy Wu. 2025. Chronologically
Consistent Large Language Models.arXiv preprint arXiv:2502.21206(2025).
[9] Giorgos Iacovides et al. 2024. FinLlama: LLM-Based Financial Sentiment Analysis
for Algorithmic Trading. InProceedings of the 5th ACM International Conference
on AI in Finance (ICAIF).
[10] Aakanksha Jadhav and Vishal Mirza. 2025. Large Language Models in Equity
Markets: Applications, Techniques, and Insights.Frontiers in Artificial Intelligence
8 (2025), 1608365. doi:10.3389/frai.2025.1608365
[11] Alireza Kargarzadeh. 2024.Developing and Backtesting a Trading Strategy Using
Large Language Models, Macroeconomic and Technical Indicators. Master’s thesis.
Imperial College London.
[12] Arman Khaledian, A. Ghadiridehkordi, and Nariman Khaledian. 2025. PCA-RAG:
Principal Component Analysis for Efficient Retrieval-Augmented Generation.
arXiv preprint arXiv:2504.08386(2025).
[13] Alex Kim, Maximilian Muhn, and Valeri Nikolaev. 2024. Financial Statement
Analysis with Large Language Models.arXiv preprint arXiv:2407.17866(2024).
[14] Kemal Kirtac and Guido Germano. 2024. Sentiment Trading with Large Language
Models.Finance Research Letters62 (2024), 105227. doi:10.1016/j.frl.2024.105227
[15] Gang Li, Dandan Qiao, and Mingxuan Zheng. 2025. Structured Event Represen-
tation and Stock Return Predictability.arXiv preprint arXiv:2512.19484(2025).
[16] Xiang Li, Zikai Wei, Yiyan Qi, Wanyun Zhou, Xiang Liu, Penglei Sun, Jian Guo,
Yongqi Zhang, and Xiaowen Chu. 2026. Janus-Q: End-to-End Event-Driven
8

Buy the Rumor, Sell the News: When Is News Priced In? AI4F ’26, November 14, 2026, Milan, Italy
Trading via Hierarchical-Gated Reward Modeling.arXiv preprint arXiv:2602.19919
(2026).
[17] Alejandro Lopez-Lira and Yuehua Tang. 2026. Can ChatGPT Forecast Stock
Price Movements? Return Predictability and Large Language Models.Journal of
Financial Economics184 (2026), 104335. doi:10.1016/j.jfineco.2026.104335
[18] Nicholas Pangakis and Sam Wolken. 2024. Knowledge Distillation in Automated
Annotation: Supervised Text Classification with LLM-Generated Training La-
bels. InProceedings of the Sixth Workshop on Natural Language Processing and
Computational Social Science (NLP+CSS 2024). Association for Computational
Linguistics, Mexico City, Mexico, 113–131. doi:10.18653/v1/2024.nlpcss-1.9
[19] Kassiani Papasotiriou, Srijan Sood, Shayleen Reynolds, and Tucker Balch. 2024. AI
in Investment Analysis: LLMs for Equity Stock Ratings. InProceedings of the 5th
ACM International Conference on AI in Finance (ICAIF). Association for Computing
Machinery, New York, NY, USA, 419–427. doi:10.1145/3677052.3698694
[20] He Wang, Wenyilin Xiao, Songqiao Han, and Hailiang Huang. 2025. StockMem:
An Event-Reflection Memory Framework for Stock Forecasting.arXiv preprint
arXiv:2512.02720(2025).
[21] Mingxuan Xia, Haobo Wang, Yixuan Li, Zewei Yu, Jindong Wang, Junbo Zhao, and
Runze Wu. 2025. Prompt Candidates, then Distill: A Teacher-Student Framework
for LLM-driven Data Annotation. InProceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers). Association for
Computational Linguistics, Vienna, Austria, 2750–2770. doi:10.18653/v1/2025.acl-
long.139
9
