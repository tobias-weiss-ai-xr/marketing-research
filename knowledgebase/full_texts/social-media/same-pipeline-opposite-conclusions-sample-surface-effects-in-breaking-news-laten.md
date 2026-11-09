---
title: 'Same Pipeline, Opposite Conclusions: Sample-Surface Effects in Breaking-News Latency'
url: https://arxiv.org/abs/2605.21521
category: social-media
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Farhad Bazyari
- Xianghang Liu
- Sean Moran
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.21521
pages: 5
chars: 23104
fetched_at: '2026-11-08T12:59:36+00:00'
kb_version: 1
---

# Same Pipeline, Opposite Conclusions: Sample-Surface Effects in Breaking-News Latency

Same Pipeline, Opposite Conclusions:
Sample-Surface Effects in Breaking-News Latency
Farhad Bazyari, Xianghang Liu, Sean Moran
TWG AI
{fbazyari, xliu, smoran}@twg.ai
Abstract
Osborne and Dredze (2014) reported that Twitter was the
timeliest social-media source of breaking news, trailing only
newswire. Twelve years on, the platform landscape has
shifted — Google+ is gone, X replaced Twitter, Bluesky
and Threads have appeared — and platform data now
flows almost exclusively through commercial social-listening
providers that redact key fields. We revisit the question
with two sampling designs run through the same down-
stream pipeline.Sample AdrawsN= 50events from the
Wikipedia Current Events Portal (WCEP) ranked by article
pageviews.Sample BdrawsN= 109events from Polymar-
ket prediction markets ranked by USD trading volume, with
each event’s news moment pinned to the largest 1-hour trade-
volume spike. Both samples are pulled from one commercial
provider across nine indexed channels. We report three find-
ings.(1) The X-vs-news direction depends on the sample.
News leads X by a median of21.6min on Sample A (n= 6
paired); the same comparison is tied at−0.02min on Sam-
ple B (n= 16paired, X earliest in38%).(2) The channel
ecosystem has diversified.Bluesky, Facebook public, and
YouTube together account for24–32%of earliest-channel
wins; the2014“X versus newswire” framing no longer fits.
(3) Coverage gaps are structural.Even with U.S.-relevance
filtering and a pageview prior, the provider’s index returns
no on-topic evidence on24%of randomly-sampled WCEP
events. The paper’s contribution is the cross-surface design
that exposes the sample dependency in (1).
Introduction
Osborne and Dredze (2014) asked, twelve years ago,
whether Twitter was the earliest source of breaking news,
and reported that across29hand-picked events from De-
cember2013, Twitter “almost consistently” led other so-
cial media but trailed newswire. The platform landscape has
since changed substantially: Google+ has been retired; Twit-
ter has become X with a new API regime; Bluesky, Threads,
and TikTok have entered as news-bearing surfaces; Face-
book’s role as a public news vector has receded; and re-
searcher access has narrowed — the free1%Streaming API
is gone, and most platform data now flows through commer-
cial providers that redact key fields (Davidson et al. 2023;
Pfeffer et al. 2023).
A second, methodological shift matters as much.
Breaking-news latency studies have traditionally used hand-
curated event lists — Osborne and Dredze (2014) hand-
picked29events; subsequent work followed the same con-
vention. Hand-curation samples from the events the analyst
already believes the index will cover, an invisible bias by
construction. We address this by running the same down-
stream measurement pipeline against two independently-
constructed event samples, each derived from a public atten-
tion surface rather than analyst judgement. The two samples
prove to disagree on the central question, and that disagree-
ment is the paper’s main finding.
Our contributions are:
1.A two-surface comparison.Sample A draws events
from the Wikipedia Current Events Portal (WCEP) with
a U.S. filter and a Wikipedia-pageviews prior. Sample B
draws events from Polymarket prediction markets with
a USD-trading-volume prior and pins each event’s news
moment to the timestamp of the market’s largest 1-hour
volume spike.
2.A direction-reversed primary finding.On Sample A
(n= 6paired events) news leads X by a median of
21.6minutes. On Sample B (n= 16) the same com-
parison is tied at the median (−0.02min, IQR−0.20
to+2.50min), with X earliest in38%of paired events.
Channel-as-earliest puts X at38%on Sample B (vs16%
on Sample A) and news at27%(vs53%).
3.A sample-source-agnostic protocol.The pipeline
— LLM-assisted boolean drafting, single-query
commercial-provider pulls, snowflake-decoded X
publish times, oEmbed-based on-topic verification —
accepts any seeding source; adding a third sampling
surface requires only a new seeding script.
Related Work
The closest prior work is Osborne and Dredze (2014), who
compared Twitter, Facebook, and Google+ to newswire
across29events from December2013and found Twitter
consistently led other social media but lagged newswire.
Petrovi´c et al. (2013) addressed the related “can Twitter
replace newswire” question, and Petrovi ´c, Osborne, and
Lavrenko (2010) laid out the streaming first-story-detection
framework that powered much of this era’s work. Morstatter
et al. (2013) showed that the1%Streaming sample is not
random with respect to all queries — a foundational caveat
arXiv:2605.21521v1  [cs.SI]  18 May 2026

we revisit on different sampling axes. Farzindar and Khre-
ich (2015) and Kwak et al. (2010) provide further context
for Twitter’s role through that era.
Subsequent work continued to use Twitter as the dominant
data source for crisis, health, and political-event detection
(Olteanu et al. 2019; Imran et al. 2020; Sakaki, Okazaki, and
Matsuo 2010; Leskovec, Backstrom, and Kleinberg 2009).
Cross-platform breaking-news comparisons in the years that
followed were rare. With the contraction of free academic
API access on X (T ¨ornberg 2023; Davidson et al. 2023; Pf-
effer et al. 2023) and the rise of Bluesky and Threads, the
question ofwhichcontemporary channel breaks news first
has not, to our knowledge, been re-examined at the breadth
of Osborne and Dredze (2014). T ¨ornberg (2023) provides
a baseline for LLM use in social-science text analysis that
we draw on for feature extraction and boolean drafting. The
use of prediction-market trade activity as a proxy for atten-
tion — via the public Polymarket data mirror (SII-W ANGZJ
2026) — is, to our knowledge, novel for the breaking-news-
latency setting.
Method
The pipeline has six stages: (i) event sampling, (ii) feature
extraction (used as covariates), (iii) LLM-assisted boolean
drafting, (iv) commercial-provider mention pulls, (v) side-
channel publish-time recovery for X, and (vi) on-topic veri-
fication. Stages (ii)–(vi) are identical between Sample A and
Sample B; only stage (i) differs.
Sample A: random WCEP, U.S.-filtered,
pageview-ranked
We scrape the Wikipedia Current Events Portal for the30-
day window2026-04-12to2026-05-11(586candidates).
We apply a U.S.-relevance substring filter (U.S. state and
major-city names, “United States”, “U.S.”, “American”, and
U.S.-institutional terms such as “Federal Reserve” and “Pen-
tagon”);171of586candidates (29.2%) pass. For each
passing candidate we fetch the linked Wikipedia article’s
English-edition pageviews from the public REST endpoint
over the event day and the day after, and rank by total
pageviews. To prevent umbrella-article concentration, we
cap at3bullets per linked article and take the top50. The
finalN A = 50spans39distinct Wikipedia articles across
10event categories.
Sample B: attention-weighted Polymarket markets
We use the public Polymarket data mirror (SII-
W ANGZJ 2026), which provides market metadata
(markets.parquet) and second-resolution trade history
(trades.parquet). We filtermarkets.parquet
to markets whose resolution-window overlaps2026-
02-13to2026-05-13(90days) with lifetime USD
volume≥$100,000; we cap at one binary market per
event title(one news event→one chosen market)
and take the top130by lifetime volume. For each chosen
market we scan its trades within the same window, compute
the per-market rolling 1-hour USD-volume sum, and pint e
to the timestamp of the largest 1-hour spike. Markets with
no in-window trade activity are dropped (21of130). The
finalN B = 109spans76distinct prediction events, with
median lifetime volume $6.1M.
The Polymarket sampling design has three properties
worth flagging. First, the prior isUSD-weighted attention
rather than editorial notability; high-volume events are by
construction events traders judged worth real money to pre-
dict. Second, the spike timestamp is a much sharpert e than
WCEP’s day-level event date; the median spike is a single-
minute window. Third, the categorical mix is determined by
what Polymarket lists, not by an editorial portal: in our run,
sports (66), politics (28), macro/crypto (9), other (6).
Feature extraction
For each sampled event, we use a large language model to
extract a structured feature vector along five descriptive axes
(clock-edge,live-visible,institutional-source,geographic-
scope,language-primary). These axes are retained as co-
variates in the result tables but are not used to stratify the
sample.
LLM-assisted boolean drafting
For each event the LLM draftstwoboolean queries: a tight
news boolean(3–4 AND-clusters of named-entity anchors),
and apermissive X boolean(1–2 AND-clusters of broader
OR-sets, reflecting that short-form X mentions rarely use the
formal phrasings news articles do). For Sample B the prompt
is extended to handle prediction-market-style descriptions:
“WillXhappen byY?” is treated as a search for entity-
level news aroundt e regardless of outcome, so the prompt
forbids encoding the predicted outcome or the deadline date
into the X boolean. The pipeline issues a single permissive
query per event and lets the downstream verifier (the on-
topic verifier subsection below) filter pollution channel by
channel; a preliminary two-query design produced a50%
zero-hit rate because the tight news boolean over-anchored
on disambiguators. Both booleans are auto-approved when
they pass a model-supplied specificity score.
Mention pulls and side-channel publish-time
recovery for X
We retrieve all cross-channel mentions through the Brand-
watch Consumer Research API (Brandwatch 2026), our sin-
gle social-listening provider for this study. For each event
we create one saved query with the permissive boolean,
wait for the provider’s backfill to reach at least the50–90%
mark (we cap at90seconds and proceed with whatever par-
tial coverage the index reports), pull a date-sorted page of
up to100mentions across all source types, then issue an
X-filtered pull of the same window. The pull window is
[te −30min, te + 24h]on both samples. We delete the saved
query after pulling. A sliding-window rate limiter caps re-
quests at28per rolling10minutes to stay below the trial-tier
limit of30.
The commercial provider redacts X’sdatefield at the
bulk-API level as a condition of its X licensing, so pub-
lish time is unavailable through the standard channels these
APIs expose. However, an X tweet’s snowflakeguid

Category Sample A Sample B
(WCEP) (Polymarket)
Sports5/5(100%)39/66(59%)
Politics & conflict22/29(76%)10/28(36%)
Macro & tech6/10(60%)4/9(44%)
Other5/6(83%)2/6(33%)
All38/50(76%)56/109(51%)
Table 1: Per-category hit rate, both samples. “Hits” counts
events with≥1on-topic mention on any of the nine chan-
nels. Sample A’s WCEP categories are regrouped into the
Sample B four-bucket scheme for direct comparison.
encodes its publish time at millisecond precision in the
high-order bits of a64-bit identifier:ms= (guid≫
22) + 1,288,834,974,657, where the constant is the Twit-
ter epoch (2010-11-04 01:42:54UTC). For tweet text and
author, we use X’s unauthenticated public oEmbed endpoint
(publish.twitter.com/oembed), which is not sub-
ject to the bulk-content licensing wall and supplies the con-
tent for on-topic verification (the on-topic verifier subsection
below).
On-topic verification
Mentions returned by a permissive boolean are not all on-
topic. For each candidate earliest, we verify against the event
description before counting it as evidence. For X we require
at least two distinct keyword matches from the union of the
news and X booleans, run against the oEmbed-recovered
tweet body; ambiguous cases are adjudicated by a separate
LLM call. For non-X channels we use the mention’s title
plus article snippet and a single-match threshold. A candi-
date that fails verification is treated as polluted and the event
falls back to the next-earliest mention on the same chan-
nel. The full pipeline forN= 109events completes in ap-
proximately five and a half hours of wall-clock under the
provider’s trial-tier rate cap.
Findings
Coverage profile
Coverage rates are reported in Table 1. Sample A:38/50 =
76%of WCEP events return on-topic evidence;12(24%) re-
turn none. Sample B:56/109 = 51%. The Sample B drop is
driven by deadline-resolution markets in the politics cluster,
where the volume spike sits at the moment a yes/no deadline
passes with no concrete news to anchor on (e.g., “Khamenei
out by Feb 28”). Sports markets, whose spike sits at a kick-
off or final-whistle moment with concrete news content, hit
59%and supply most of the paired-events cell.
The Sample A24%zero-hit rate is load-bearing: the sam-
ple was already filtered to U.S. relevance and ranked by
pageviews, so these are not obscure stories. A progressive-
broadening probe on one zero-hit event (the2026-04-15
Markazi High School strike on the Pakistan–Afghanistan
border) ran five booleans against the provider’s index, from
the as-drafted permissive boolean down to a country-only
broad-topic query. The first three returned0mentions; only
the country-only query returned hits, and the earliest was a
Channel Sample A Sample B A vs B
share share∆
twitter (X)16%38% +22
news53% 27%−26
bluesky11% 16% +5
facebook public13% 7%−6
youtube5% 5% 0
instagram public0% 4% +4
forum3% 2%−1
Table 2: Earliest-channel winner share, per sample. Sam-
ple A:38verified-with-evidence WCEP events. Sample B:
56verified-with-evidence Polymarket events.
Event PV∆(min)
2026 Antiguan election17,430−7.1
US gerrymandering4,617−10.0
2025 C. Texas floods9,018−11.2
Death of Rivas Hernandez150,383−32.0
2026 NFL draft436,044−33.4
Billy Idol46,326−53.7
median —−21.6
IQR —−33.4to−10.0
Table 3: Sample A paired X-vs-news latency on the six
WCEP events with both on-topic X and on-topic news. PV
is enwiki pageviews; convention is∆>0means X earlier
(so all∆<0here means news first).
different event (a Pakistan polio-team attack the same day).
The provider index supportsbroad topical streamsbut not
named-incident reporting, even when WCEP editors judged
the latter encyclopedically notable.
Channel-as-earliest winner distribution
Table 2 reports the earliest-channel share across the two
samples. The shift between the two samples is the central
observation of the paper. On Sample A, news is the modal
earliest channel (53%) and X is second-tier (16%). On Sam-
ple B the ranking inverts: X is modal (38%) and news drops
to27%. Bluesky persists at11–16%across both samples;
the four non-news, non-X social channels together account
for32%on Sample A and34%on Sample B. The implicit
two-class framing of Osborne and Dredze (2014) — X (then
Twitter) versus newswire, with Facebook and Google+ as
also-rans — no longer matches either sample.
Paired X-vs-news latency on Sample A
The six WCEP events for which we recovered both an on-
topic news article and an on-topic X mention are reported in
Table 3. In all six, the news article precedes the X mention;
the median lead is21.6minutes and the interquartile range
is10.0to33.4minutes. The smallest lead is7.1minutes; the
largest is53.7minutes. Direction is consistent atn= 6; the
magnitude is in tens of minutes, not seconds.
The six events span sports (NFL draft), celebrity death
(Billy Idol, Rivas Hernandez), election outcome (Antigua),
structured-policy reporting (gerrymandering), and natural-
disaster reporting (Texas floods) — a deliberately heteroge-

Event cat∆(min)
Iran/US conflict ends? pol−34.23
UFC Strickland v Hernandez spt−0.62
Axiom insider trading? oth−0.50
Mavericks v Lakers spt−0.26
Hungary election (Jobbik) pol−0.20
Nuggets v Thunder spt−0.10
Real Madrid 2026-02-25 spt−0.06
FC Barcelona 2026-03-18 spt−0.02
Aston Villa 2026-02-27 spt−0.02
Spurs v Pistons spt−0.02
Thunder v Pistons spt+1.20
UCLA v UConn spt+1.26
Olympique Lyonnais 2026-02-15 spt+2.50
Schauffele wins 2026 Masters spt+14.19
LoL G2 v Bilibili spt+143.80
Atl´etico Madrid 2026-02-14 spt+552.17
median —−0.02
IQR —−0.20to+2.50
Table 4: Sample B paired X-vs-news latency on the16Poly-
market events with both on-topic X and on-topic news. Con-
vention:∆>0means X earlier,∆<0means news earlier.
neous slice for ann= 6result.
Paired X-vs-news latency on Sample B
The16Polymarket-derived paired events are reported in Ta-
ble 4. The median delta is−0.02minutes, essentially a tie at
the median, and8of the16events have|∆|<0.20minutes
— i.e., when both channels are indexed for the same event,
they typically report within seconds. The interquartile range
is−0.20to+2.50minutes; both sides of zero.6of16events
(38%) have X first;10of16(62%) have news first. The bot-
tom two rows of the table (+143.80and+552.17min) are
large positive outliers — an esports semifinal and a Span-
ish football match — where the verifier matched an on-topic
pre-event X mention from earlier in the day; the median is
robust to their removal.
Comparison across the two samples
The same downstream pipeline, applied to two
independently-constructed samples, produces a differ-
ent direction at the median (news leads by21.6min on
Sample A; the cell is tied at−0.02min on Sample B) and
a different dispersion (∼20×tighter on Sample B). Then
of paired events on Sample B is large enough to express a
confidence interval; on Sample A it is not.
Discussion
The sampling surface drives the headline.The answer to
the2014-style “is X still first?” question depends on which
kind of events you ask about. WCEP events are events an
editorial process has judged encyclopedically notable —
exactly the story shapes the modern 24/7 news pipeline
is optimised for, with standing alerts and pre-staged copy
desks. Polymarket events are events traders found worth real
money to predict, and the informational community for these
events is often already concentrated on X. The two samples
measure the same latency variable on different populations,
and each produces a coherent within-sample result. Reading
2014-era results as platform-deterministic treats a sample-
driven finding as a statement about the platform; a more pre-
cise framing is “which channel surfaces a given kind of event
first?”
A diversified channel ecosystem.Across both samples,
the four non-news non-X channels (Bluesky, Facebook pub-
lic, YouTube, Instagram public) together account for32–
34%of earliest-channel wins. Bluesky alone surfaces as
the earliest channel on11–16%of verified events. A first-
to-cover study that compares only X and news will under-
represent roughly a third of the actually-earliest publications
— a finding both samples agree on. This is the strongest
robustness check available from the cross-surface design:
where the samples disagree on the X-vs-news direction, they
agree that the X-vs-news framing alone is incomplete.
Future Work
The two-surface comparison opens several natural exten-
sions.Expanding the paired cell.Both paired cells are
modest (n= 6on Sample A,n= 16on Sample B); widen-
ing the sampling windows or relaxing the per-event cap
would push the paired count into a range where category-
level subgroup analysis becomes statistically meaningful.
More sampling surfaces.The pipeline is sample-source ag-
nostic, so adding a third or fourth surface (Google Trends
spike points, Reddit r/all resolutions, GDELT spike clusters)
requires only a new seeding script; a Polymarket category-
quota seeder or a non-English WCEP prior would similarly
broaden the comparison on additional axes.
Acknowledgements
Use of generative AI.Anthropic’s Claude (Sonnet and
Opus) was used in the pipeline for feature extraction,
boolean drafting, and verifier adjudication.
References
Brandwatch. 2026. Brandwatch Consumer Research.
https://www.brandwatch.com/products/consumer-research/.
Social-listening platform accessed via the Consumer
Research API; data used under Brandwatch’s trial-tier
licence.
Davidson, B. I.; Wischerath, D.; Racek, D.; Parry, D. A.;
Godwin, E.; Hinds, J.; van der Linden, D.; Roscoe, J. F.;
and Ayravainen, L. 2023. Platform-Controlled Social Media
APIs Threaten Open Science.Nature Human Behaviour, 7:
2054–2057.
Farzindar, A.; and Khreich, W. 2015. A Survey of Tech-
niques for Event Detection in Twitter.Computational Intel-
ligence, 31(1): 132–164.
Imran, M.; Ofli, F.; Caragea, D.; and Torralba, A. 2020. Us-
ing AI and Social Media Multimodal Content for Disaster
Response and Management: Opportunities, Challenges, and
Future Directions.Information Processing & Management,
57(5): 102261.

Kwak, H.; Lee, C.; Park, H.; and Moon, S. 2010. What is
Twitter, a Social Network or a News Media? InProceed-
ings of the 19th International Conference on World Wide
Web (WWW), 591–600.
Leskovec, J.; Backstrom, L.; and Kleinberg, J. 2009. Meme-
Tracking and the Dynamics of the News Cycle. InProceed-
ings of the 15th ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining (KDD), 497–506.
Morstatter, F.; Pfeffer, J.; Liu, H.; and Carley, K. M. 2013. Is
the Sample Good Enough? Comparing Data from Twitter’s
Streaming API with Twitter’s Firehose. InProceedings of
the Seventh International AAAI Conference on Weblogs and
Social Media (ICWSM), 400–408. AAAI Press.
Olteanu, A.; Castillo, C.; Diaz, F.; and Kıcıman, E. 2019.
Social Data: Biases, Methodological Pitfalls, and Ethical
Boundaries.Frontiers in Big Data, 2: 13.
Osborne, M.; and Dredze, M. 2014. Facebook, Twitter and
Google Plus for Breaking News: Is There a Winner? InPro-
ceedings of the Eighth International AAAI Conference on
Weblogs and Social Media (ICWSM), 611–614. AAAI Press.
Petrovi´c, S.; Osborne, M.; and Lavrenko, V . 2010. Stream-
ing First Story Detection with Application to Twitter. In
Human Language Technologies: The 2010 Annual Confer-
ence of the North American Chapter of the Association for
Computational Linguistics (NAACL-HLT), 181–189.
Petrovi´c, S.; Osborne, M.; McCreadie, R.; Macdonald, C.;
Ounis, I.; and Shrimpton, L. 2013. Can Twitter Replace
Newswire for Breaking News? InProceedings of the Sev-
enth International AAAI Conference on Weblogs and Social
Media (ICWSM). AAAI Press.
Pfeffer, J.; Matter, D.; Jaidka, K.; Varol, O.; Mashhadi, A.;
Lasser, J.; Assenmacher, D.; Wu, S.; Yang, D.; Brantner, C.;
Romero, D. M.; Otterbacher, J.; Schwemmer, C.; Joseph, K.;
Garcia, D.; and Morstatter, F. 2023. Just Another Day on
Twitter: A Complete 24 Hours of Twitter Data. InProceed-
ings of the Seventeenth International AAAI Conference on
Web and Social Media (ICWSM).
Sakaki, T.; Okazaki, M.; and Matsuo, Y . 2010. Earthquake
Shakes Twitter Users: Real-Time Event Detection by Social
Sensors. InProceedings of the 19th International Confer-
ence on World Wide Web (WWW), 851–860.
SII-W ANGZJ. 2026. Polymarket Markets and Trades
Dataset. https://github.com/SII-W ANGZJ/Polymarket data.
Public dataset of Polymarket prediction-market meta-
data (markets.parquet) and processed trade his-
tory (trades.parquet), fetched from the Polygon
blockchain and Gamma API; used here as an attention-
weighted sampling source for breaking-news events.
T¨ornberg, P. 2023. How to Use Large Language Models for
Text Analysis.arXiv preprint arXiv:2307.13106.
