---
title: 'YouTube Clips and Broad but Shallow Attention to Candidates: Evidence from the 2024 Tokyo Gubernatorial
  Election'
url: https://arxiv.org/abs/2610.24387
category: social-media
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Yoshito Miwa
- Kazutoshi Sasahara
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.24387
pages: 8
chars: 42340
fetched_at: '2026-11-08T13:13:56+00:00'
kb_version: 1
---

# YouTube Clips and Broad but Shallow Attention to Candidates: Evidence from the 2024 Tokyo Gubernatorial Election

YouTube Clips and Broad but Shallow Attention to
Candidates: Evidence from the 2024 Tokyo
Gubernatorial Election
1st Yoshito Miwa
Department of Innovation Science
Institute of Science Tokyo
Tokyo, Japan
miwa.y.bf00@m.isct.ac.jp
2nd Kazutoshi Sasahara
Department of Innovation Science
Institute of Science Tokyo
Tokyo, Japan
sasahara.k.6efa@m.isct.ac.jp
Abstract—Video-sharing platforms and social media have
gained influence in election campaigns, and third-party edited
videos (calledkirinukiin Japanese; hereafter, “clip videos”) in
particular have attracted attention. In Japan, Shinji Ishimaru,
previously unknown nationally, finished second in the 2024 Tokyo
gubernatorial election, a result widely attributed to his popularity
on YouTube. Focusing on this case, we analyzed 44,331 YouTube
videos relating to the nine leading candidates, posted between
July 5, 2020, and July 7, 2024. Using cumulative views and
engagement data as of June 25, 2025, we examined the relation-
ship between clip videos and the attention candidates received.
Regression analyses with standard errors clustered by channel
showed that Ishimaru, the most watched candidate, did not draw
the most active engagement. Videos mentioning Ishimaru received
about 36% fewer likes and 41% fewer comments at the same
number of views, whereas some candidates with fewer views
recorded higher engagement rates. Clip videos were associated
with this breadth of attention. They received about 1.8 times more
views but 26% fewer comments at the same number of views, and
mentions of Ishimaru were associated with about 2.6 times more
views among non-clip videos. The interaction between the two,
however, was not significant, and understanding the prominence
of Ishimaru’s cumulative views requires considering both the
number of clip videos about him and the views per video. These
results suggest that the spread of attention through clip videos
may have functioned as a broad but shallow pathway, distinct
from the formation of committed support.
Index Terms—YouTube, clip videos, user engagement, political
communication, elections
I. INTRODUCTION
Where people encounter political information is shifting
from mass media to video platforms. In Japan, average daily
internet use overtook television viewing on weekdays in 2020,
and by 2024 it exceeded television viewing on both weekdays
and holidays for all ages combined [1]. Surveys of political
communication likewise record a growing share of voters
naming social media and video platforms among the sources
they consult [2].
Among political content on video platforms,clip videos
(kirinuki) have become increasingly prominent. In this study,
a clip video is a video in which a third party reassembles
footage that already exists online. Most are short edits that
lift a striking passage out of a long livestream, a council
session or a press conference and add subtitles or music.
The format spread first in entertainment genres such as game
commentary and has since moved into politics. Behind this
lies YouTube’s monetization scheme, under which advertising
revenue is shared according to view counts. Press reporting
indicates that the operators of clip channels devoted to one
candidate were motivated by revenue rather than political
support, some earning several million yen a month [3], [4].
Clip videos are thus a mechanism by which third-party actors
unaffiliated with the candidates generate political attention on
a large scale, driven by financial incentives.
This phenomenon became visible in a Japanese election
in the 2024 Tokyo gubernatorial race. Shinji Ishimaru, the
former mayor of Akitakata (a city of fewer than 30,000 in
Hiroshima Prefecture), was nationally unknown and received
no organized party backing. Nevertheless, he took about 1.66
million votes to finish second behind the incumbent [5]. The
result was labeled the “Ishimaru phenomenon” and was widely
attributed to his online popularity, centered on YouTube [6],
[7]. About half of his supporters named YouTube among the
sources they consulted before voting [8]. Quantitative work on
this election has begun to appear [9]–[11], but little of it has
shown at scale what was happening on YouTube itself.
Nor is it clear what kind of attention this was. Much prior
work on online diffusion treats active audience response, such
as sharing, as its driver [12], [13]. For short videos watched
passively through algorithmic recommendation, however, be-
ing watched widely and being supported strongly need not
coincide. Most of this work also concerns Western settings,
and whether its findings apply to Japan has not been tested.
We therefore examine 44,331 YouTube videos relating to
the nine leading candidates in the 2024 Tokyo gubernatorial
election, and ask three questions.
•RQ1: Were clip videos associated with higher view
counts, and was that association particularly strong for
videos mentioning Ishimaru?
•RQ2: Were high view counts accompanied by active
engagement from viewers?
arXiv:2610.24387v1  [cs.SI]  17 Oct 2026

•RQ3: Did title sentiment and visual features of the
thumbnail account for the view counts of short clip
videos?
RQ3 asks whether the view, repeatedly advanced in prior
work [14], that emotional appeal and visual salience account
for the diffusion of video also holds for the clip format.
This paper makes three contributions. First, it quantitatively
analyzes more than 44,000 YouTube videos on a Japanese
election over four years, including 6,358 clip videos. Second,
it shows that clip videos and mentions of Ishimaru were
each associated with higher view counts, and that this held
when correlation within channels was accounted for and when
the sample was restricted to the official campaign period.
Third, it shows that the most watched candidate ranked low
on engagement per view and that clip videos drew fewer
comments relative to their views, which suggests that attention
spread through clip videos may have functioned as a broad but
shallow pathway to recognition, distinct from the formation of
committed support.
II. RELATEDWORK
The diffusion of political video has been studied mainly
in terms of content and format. Regarding content, material
that evokes high-arousal emotions such as anger or anxiety
is shared more readily [12], [13], and political posts carrying
moral-emotional language spread particularly far [15]. In terms
of format, shorter videos tend to reach more viewers, and
on YouTube, Shorts have been reported to draw far more
views than regular videos [16]. Political influencers have built
audiences by splitting long livestreams into short highlight
videos and reposting them [17], and the business models and
content strategies of such channels have themselves become
an object of study [18]. How young viewers interpret political
messages in such videos has also been examined [19].
Large-scale studies of political video on YouTube have also
accumulated. Some find that the recommendation algorithm
leads viewers toward more radical content [20], while others
attribute skewed consumption to viewers’ own preferences
rather than to the algorithm [21]. This work has concentrated
on which content is watched.
Much research treats active viewer response—likes and
comments—either as the engine of diffusion or as a measure
of influence. In election research, candidates with high en-
gagement on social media have been reported to fare better at
the polls [22], although the overall relationship between social
media activity and political participation is weak [23].
Views and engagement need not measure the same thing.
YouTube’s recommender is designed to optimize predicted
watch time rather than clicks or likes [24]. A video surfaced
by recommendation is often one the viewer did not seek out
but happened upon. Furthermore, users who do not go online
for news are nonetheless incidentally exposed to political
information on social media [25]. Under such passive viewing,
broad reach and active engagement may diverge.
Shallow attention unaccompanied by engagement may still
matter politically. People tend to favor what they have encoun-
tered repeatedly [26], and in elections where information about
candidates is scarce, mere name recognition has been shown
experimentally to raise support [27]. Entertainment-oriented
political content has also been reported to reach audiences
with little interest in politics [28]. Evaluating online attention
therefore requires measuring its breadth of reach and depth of
engagement as separate quantities. Few studies compare the
two in the same data.
Research on clip videos has dealt mainly with revenue
sharing between broadcasters and clip producers, and with
producers’ motives [29]–[31]. Almost no existing research
analyzes political clip videos at scale or examines the nature
of the attention they generate.
Work on Japanese elections and social media has likewise
focused on X, formerly Twitter [10]. Video platforms have
only recently been identified as influencing elections [32], and
quantitative analyses of political video on YouTube remain
limited: the closest precedent for the present election examines
discourse on the platform but not the diffusion of clip videos
or the gap between reach and response [9]. Most prior work
addresses Western settings, and whether its findings carry over
to Japan—where voters without a party affiliation form the
largest bloc [33]—is unclear.
This paper addresses these gaps by examining, in a sin-
gle dataset, how clip videos were associated with candidate
attention and whether that attention was accompanied by
engagement.
III. RESEARCHMETHODS
A. Data Collection
Data were collected through the YouTube Data API v3. To
raise the quota ceiling, we applied for and were accepted into
the YouTube Researcher Program.
Of the 56 candidates who ran in the 2024 Tokyo guber-
natorial election, we focus on the nine who received at least
1% of the vote. This threshold ensures our focus remains on
candidates for whom online attention translated to some degree
into votes. The observation window runs from the polling day
of the previous gubernatorial election (July 5, 2020) to that
of the 2024 election (July 7, 2024)—a span of approximately
four years—in order to capture the long-run development of
attention rather than the campaign period alone.
Collection proceeded in two stages. In the first stage we
searched using ten terms, the nine candidate names plus
“Tokyo gubernatorial election,” and retrieved the identifiers
of the matching videos (late May 2025). Adding every video
from the nine candidates’ official channels gave 111,092 video
identifiers in total. In the second stage we used those identifiers
to retrieve metadata: view, like and comment counts, duration,
title, description, tags and channel information. The second
stage was carried out within a single day, June 25, 2025, so that
views and engagement were measured at the same instant for
every video. These values are therefore cumulative up to that
date, and videos posted earlier had longer to accumulate views.
The regressions address this by controlling for the number of
days from posting to the election.

Fig. 1. Construction of the analysis sample.
B. Preprocessing
Because the search API returns many loosely related videos,
we kept only videos whose title, description, tags, or channel
name contained a candidate name or the term “Tokyo guberna-
torial election.” This left 44,331 distinct videos. A single video
may mention several candidates, giving 53,986 video–keyword
pairs. Of the videos, 86.3% mention exactly one candidate
and 9.5% mention more than one. The remaining 4.2% (1,867
videos) matched only the term “Tokyo gubernatorial election”;
all candidate dummy variables are zero for these, and they
form the reference group. Fig. 1 summarizes the construction
of the sample.
C. Classifying videos
Videos were sorted into official, clip and general videos.
Official videosare posted from a candidate’s own YouTube
channel and mention that candidate.
Clip videosare defined as videos in which a third party
reassembles footage already present online. To extract videos
meeting this definition we treated as clip videos those that
(1) contain the termkirinuki(“clip”) in the title, description,
tags, or channel name, or (2) contain both “quotation” and
“YouTube” in the title, description, or tags. The second condi-
tion reflects the convention of naming the YouTube video a clip
is drawn from. The official-video condition takes precedence,
and videos meeting neither condition aregeneral videos,
a category that includes news reports and commentary by
individuals.
Videos of 60 seconds or less are treated as Shorts and longer
videos as regular videos.
D. Model of view counts
To estimate how clip videos and candidates related to view
counts, we fitted an ordinary least squares regression with the
logarithm of view counts as the dependent variable. No video
had zero views, and all 44,331 videos enter the model.
log(viewsi + 1) =β 0 +β 1Officiali +β 2Clipi
+β 3Ishimarui +β 4(Clipi ×Ishimaru i)
+γ ′Ci +δ 1Durationi +δ 2Daysi +ε i
(1)
OfficialandClipare dummy variables for official and
clip videos, with general videos as the reference category.
Ishimaruis a dummy variable for videos mentioning Shinji
Ishimaru, andCis a vector of dummy variables for the
other eight candidates. The 1,867 videos matching only the
term “Tokyo gubernatorial election” have all candidate dummy
variables set to zero and form the reference group. Because a
video may mention several candidates, the candidate dummy
variables are not mutually exclusive: each coefficient contrasts
videos that mention that candidate with videos that do not,
holding mentions of the other candidates constant. A candidate
with a similar name, Yukito Ishimaru, is included as a separate
variable so that the two are not conflated.Durationis the
length of the video in minutes andDaysthe number of days
from posting to the election (July 7, 2024). The coefficientβ 4
on the interaction term tests whether the association between
clip videos and views differs for videos mentioning Ishimaru.
Videos posted from the same channel share the uploader’s
visibility and subscriber base and are not independent of one
another. Standard errors are therefore robust and clustered by
channel (5,453 clusters). The largest variance inflation factor
among the explanatory variables is 2.11, for the interaction
term, so multicollinearity is not a concern.
E. Model of engagement
To test whether high view counts were accompanied by
active engagement, we fitted the same specification with
engagement as the dependent variable, adding the logarithm
of view counts as a regressor.
log(engagementi+1) =α 0+α1 log(viewsi+1)+· · ·+ui (2)
Hereengagementis either the like count or the comment
count. Using the same set of independent variables as in
Equation (1) (represented by the omitted terms), we estimated
the two models separately. Because a constant of 1 is added
before taking logarithms, videos with zero engagement are
retained, and both models cover the same 44,331 videos as
the view-count model. Videos with comments disabled are
recorded as having zero comments and cannot be distinguished
from videos that received none, so they are included as well.
Standard errors are clustered by channel as in the view-
count model. Because view counts enter as a regressor, each
coefficient is a difference in engagement between videos with
the same number of views; a negative coefficient means that
videos of that kind draw less engagement relative to their
reach.

F . Title sentiment and thumbnail features
An exploratory comparison carried out before this study,
of the ten most and the ten least viewed short clip videos,
suggested that the more viewed videos had more negative titles
and more saturated thumbnails. We tested whether this holds
across the full set of short clip videos (n= 2,631).
Title sentiment was computed withoseti, a sentiment
analysis library built on a Japanese polarity dictionary [34].
osetireturns a polarity score from−1(negative) to+1(pos-
itive) for each sentence; we took the mean over the sentences
of a title as that video’s score. For thumbnails we retrieved
the 480×360 image published by YouTube (hqdefault),
converted it to HSV color space with OpenCV and computed
mean saturation. Images could not be retrieved for 202 videos,
most of them deleted or made private, so the saturation
analysis covers 2,429 videos.
For both measures we computed Spearman rank correlations
with the logarithm of view counts and, for title sentiment,
compared the top and bottom quartiles of view counts with a
Mann–WhitneyUtest.
Analyses were run in Python 3.11, withstatsmodelsfor
the regressions andSciPyfor the tests.
G. Robustness checks
To confirm that the main results are not sensitive to partic-
ular analytical choices, we ran three additional analyses.
1)Restriction to the campaign period.Some clip videos
about Ishimaru were posted while he was mayor of Aki-
takata, so attention accumulated before the gubernatorial
election could be driving the result. We re-estimated the
model on videos posted during the official campaign
period common to all candidates, from the official start
of the campaign on June 20, 2024, to the vote on July
7 (n= 3,748).
2)Common slope in the engagement model.The model
in Equation (2) assumes that the relationship between
views and engagement is log-linear with a slope com-
mon to all groups. We re-estimated the like model with
an interaction betweenlog(views)and the Ishimaru
dummy variable.
3)Regular videos only.Because views are counted on a
different basis for Shorts than for regular videos, we
re-estimated the engagement model on regular videos
alone.
IV. RESULTS
A. Concentration of attention across candidates
Cumulative views were heavily concentrated on one can-
didate. Videos mentioning Ishimaru accumulated about 990
million views, 2.3 times the total for Koike (about 440
million), the second-ranked candidate (Fig. 2). The ordering by
number of videos differed: Koike had the most related videos
(15,335) and Ishimaru less than half that number (6,685). The
concentration arose in views rather than in the volume of
uploads.
Fig. 2. Cumulative views by candidate. Values are cumulative over videos
posted up to each month, measured on June 25, 2025. The dotted line marks
the start of the official campaign period (June 20, 2024).
Fig. 3. Total views by candidate and video type. Videos mentioning several
candidates are counted once for each, so the bars are not mutually exclusive
and do not sum to the dataset total.
Clip videos accounted for much of this concentration. Clip
videos mentioning Ishimaru alone accumulated about 425 mil-
lion views, comparable to the total for all videos mentioning
Koike (Fig. 3). At the channel level, 13 of the 30 channels
with the highest cumulative views posted clip videos, and 9
of these drew more than half their total views from clips. Six
of those channels included “Ishimaru” in their channel names,
indicating the emergence of third-party uploaders specializing
in a single candidate.
B. Clip videos, candidates and view counts
Table I reports the number of videos by type. Clip videos
(6,358) are about 2.9 times as numerous as official videos
(2,210), and 41.4% of them are Shorts of 60 seconds or less—a
proportion markedly higher than for general (19.7%) or official
(12.3%) videos.
To control simultaneously for video format, duration, tim-
ing, and the candidates mentioned, we regressed the logarithm

TABLE I
NUMBER OFVIDEOS BYTYPE
Type Shorts Regular Total Shorts (%)
General 7,051 28,712 35,763 19.7
Clip 2,631 3,727 6,358 41.4
Official 272 1,938 2,210 12.3
Total 9,954 34,377 44,331 22.5
TABLE II
REGRESSION ONLOGVIEWCOUNTS
Full period Campaign period
Variableβ p β p
Official video 1.974<.001 1.006 .001
Clip video 0.577 .020 1.329 .045
Ishimaru S. 0.974 .030 1.491<.001
Clip×Ishimaru 0.116 .854−0.657 .390
Duration (min) 0.008<.001 0.015<.001
Days to election−0.0007 .005 0.028 .034
Koike−0.359 .192−0.009 .961
Renho 0.629 .031 0.020 .916
Himasora 0.504 .069−0.977<.001
Sakurai−1.415<.001 0.084 .835
Tamogami−0.148 .545−0.508 .015
Utsumi−0.313 .482−0.452 .316
Anno 0.170 .743−0.322 .207
Ishimaru Y .−1.602 .025 0.192 .677
N44,331 3,748
R2 0.166 0.134
Dependent variable:log(views+1). For dummy variables,exp(β)is the ratio
of views; for example,exp(0.974)≈2.6. Reference categories are general
videos for video type and, for each candidate, videos that do not mention that
candidate. Because the model includes the Clip×Ishimaru term, Clip video
compares clip with general videos among videos not mentioning Ishimaru,
and Ishimaru S. compares videos that do and do not mention him among
non-clip videos. Among clip videos, the Ishimaru difference is the sum of
the Ishimaru S. and Clip×Ishimaru coefficients. Standard errors are robust
and clustered by channel (5,453 clusters for the full period, 1,069 for the
campaign period). The intercept is omitted.
of view counts on these variables (Table II).
In the full-period model (n= 44,331), holding the other
variables constant, clip videos not mentioning Ishimaru re-
ceived about 1.8 times as many views as general videos
(β= 0.577,p=.020), and non-clip videos mentioning
Ishimaru received about 2.6 times as many views as those
that did not mention him (β= 0.974,p=.030). The
interaction between clip videos and mentions of Ishimaru was
not significant (β= 0.116,p=.854): we find no evidence
that the association between the clip format and views was
especially strong for videos mentioning him.
Robustness.To remove the influence of videos posted
during his tenure as mayor, we restricted the sample to the
official campaign period (n= 3,748). The coefficients for clip
videos (β= 1.329,p=.045) and for Ishimaru (β= 1.491,
p < .001) both remained significant, and the interaction
remained non-significant.
TABLE III
REGRESSION ONLOGLIKES ANDLOGCOMMENTS, CONTROLLING FOR
VIEWS
Likes Comments
Variableβ p β p
Log views 0.829<.001 0.618<.001
Official video 0.307 .199−0.344 .117
Clip video−0.133 .155−0.306 .003
Ishimaru S.−0.440<.001−0.524<.001
Clip×Ishimaru 0.031 .814 0.074 .706
Duration (min)−0.0004 .577−0.0025 .002
Days to election−0.0002 .003 0.0000 .552
Koike−0.243 .007 0.065 .474
Renho−0.050 .654 0.288 .004
Himasora 0.482<.001 0.414<.001
Sakurai 0.629<.001 0.338 .002
Tamogami 0.255<.001 0.163 .071
Utsumi 0.472<.001−0.121 .541
Anno−0.337 .023−0.267 .048
Ishimaru Y .−1.375<.001−0.417 .034
N44,331 44,331
R2 0.822 0.696
Dependent variables:log(likes + 1)andlog(comments + 1). Because log
views is included, each coefficient compares videos with the same number
of views. For dummy variables,exp(β)is the ratio of likes or comments;
for example,exp(−0.440)≈0.64, or about 36% fewer likes. Reference
categories and the reading of the Clip video and Ishimaru S. coefficients are
as in Table II. Standard errors are robust and clustered by channel (5,453
clusters). The intercept is omitted.
C. Divergence between views and engagement
To test whether high view counts were accompanied by
active engagement, we regressed the logarithms of like and
comment counts on the logarithm of view counts and the same
covariates (Table III), using all 44,331 videos.
The coefficient on views is 0.829 in the like model and
0.618 in the comment model, both below one: as views rise,
likes and comments per view both decline.
Holding views and the other conditions constant, non-clip
videos mentioning Ishimaru received about 36% fewer likes
(β=−0.440,p < .001) and about 41% fewer comments
(β=−0.524,p < .001) than those that did not mention
him. Sakurai shows the opposite pattern. Holding the other
conditions constant, videos mentioning him received about
a quarter as many views as those that did not (Table II,
β=−1.415), yet, holding views as well, about 1.9 times
as many likes (β= 0.629,p < .001) and about 1.4 times
as many comments (β= 0.338,p=.002). Himasora is high
on both measures (about 1.6 times for likes and 1.5 times
for comments), while Utsumi is high on likes but shows no
significant difference on comments (β=−0.121,p=.541).
The candidates watched most widely were not those engaged
with most actively (Fig. 4).
Holding views and the other conditions constant, clip videos
not mentioning Ishimaru received about 26% fewer comments
than general videos (β=−0.306,p=.003); their coefficient
for likes is also negative but not significant (β=−0.133,
p=.155). The divergence between views and engagement
is largest at the level of the candidate, but for comments it

Fig. 4. Coefficients by candidate. From left: views, likes adjusted for views,
and comments adjusted for views. Estimates are shown as ratios,exp(β), on a
log scale. Points are point estimates and lines show 95% confidence intervals.
The reference group for each candidate is videos that do not mention that
candidate.
extends to the video format as well. Official videos did not
differ significantly from general videos on either measure.
Robustness.The interaction betweenlog(views)and the
Ishimaru dummy variable in the like model was positive and
significant (β= 0.067,p=.032): the shortfall in likes
is somewhat smaller for videos with more views, so the
common-slope model reports an average gap rather than a
constant one. Because views are counted on a different basis
for Shorts, we also re-estimated the model on regular videos
alone (n= 34,377): the coefficient for Ishimaru is−0.517
(0.596 times,p < .001), slightly larger than in the pooled
sample. The shortfall in likes is not an artifact of how Shorts
views are counted.
D. Title sentiment and thumbnail features
The relationship seen in the exploratory comparison did not
replicate across the full set. Title sentiment was not signifi-
cantly correlated with view counts (Spearmanρ=−0.029,
p=.142), and the top and bottom quartiles did not differ
(p=.167). Thumbnail saturation was likewise unrelated
to view counts (ρ=−0.006,p=.765,n= 2,429).
Within the range of dictionary-based sentiment scores and
thumbnail saturation, then, we found no general association
that accounts for the view counts of short clip videos. This
stands in contrast to commercial video, where the sentiment
of titles and thumbnails has been shown to predict views [14].
Titles of political clip videos often use irony and platform-
specific idioms, which a polarity dictionary may not capture;
the null result therefore does not show that sentiment is
irrelevant, and context-dependent classification may be needed.
The difference observed in the exploratory comparison may be
confined to a small number of outlying videos.
V. DISCUSSION
A. Broad but shallow attention
The central result is that the most watched candidate and
the most actively engaged-with candidate were not the same.
Videos mentioning Ishimaru received about 2.6 times more
views with other conditions held constant, yet, among non-
clip videos, those mentioning him received about 36% fewer
view-adjusted likes than those that did not. Videos mentioning
Sakurai or Himasora, by contrast, received more view-adjusted
likes and comments.
This contrast suggests at least two distinct forms of online
attention. One reaches many viewers but elicits little active
engagement: attention that is broad but shallow. The other
draws strong engagement from a limited audience: narrow
but deep. Given that YouTube’s recommender is built around
watch time [24] and that incidental exposure is widespread
on social media [25], Ishimaru’s videos may have reached
viewers who happened upon them rather than supporters who
sought them out. Which route carried them cannot be identified
from our data: presentation by the recommendation algorithm,
sharing on other platforms, and search traffic driven by news-
worthiness are all consistent with the same observation. Traffic
sources are not available through the platform’s public API and
can be seen only by the channel owner.
This reading may resolve the apparent tension between low
engagement and Ishimaru’s 1.66 million votes. Where infor-
mation about candidates is scarce, mere name recognition has
been shown to raise support [27]. For a candidate previously
unknown nationally, broad exposure through clip videos may
have served to make his name and persona widely known
without producing committed supporters. We do not measure
the relationship between viewing and voting, so this remains
a hypothesis for future work.
B. Clip videos and attention to Ishimaru
The interaction between clip videos and mentions of Ishi-
maru was not significant in any model. From this result we
cannot conclude that the clip format was associated especially
strongly with Ishimaru; nor does it show that the strength of
the association was the same. Understanding the prominence
of his cumulative views requires considering, beyond the
association with clip videos, the attention to Ishimaru himself
and the number of clip videos about him (2,321, the most for
any candidate).
Six clip channels including “Ishimaru” in their names were
among the channels with the highest cumulative views (Sec-
tion IV-A). Producers motivated by revenue select candidates
likely to draw views and produce clip videos of them in vol-
ume, so a cycle may have arisen in which supply concentrates
further on candidates already receiving attention. Whether
attention drew supply or supply generated attention cannot be
determined from our data.
In this design, redistribution by third parties appears on
the explanatory side rather than as an engagement measure,
because a clip video is itself the product of a third party

reassembling and reposting existing footage. That videos men-
tioning Ishimaru were clipped in such volume, to a cumulative
total comparable to all videos mentioning Koike, is itself an
indication of the scale of that redistribution.
C. The Japanese context and generalizability
The association between negative titles and view counts
observed in the exploratory analysis was not confirmed across
all collected clip videos of 60 seconds or less. Comparison
with the Western finding that high-arousal emotion promotes
diffusion [12] must, however, allow for the difference in
measures: the positive–negative polarity of titles measured
here is distinct from emotional arousal, so this result alone
does not show that the finding fails to hold in Japan. Whether
characteristics of Japanese viewers play a role should be ex-
amined through comparison with other countries, after validat-
ing the measurement accuracy of dictionary-based sentiment
analysis. The divergence between views and engagement, by
contrast, need not be specific to Japan. Because third parties
reassemble and repost existing footage in other regions and
on other platforms as well, as in the 2024 U.S. presidential
election [35], testing whether a similar divergence appears
there is a task for future work.
D. Limitations
This study has several limitations. First, it is an analysis
of observational data and does not establish that clip videos
caused higher view counts. Second, we do not measure the re-
lationship between viewing and actual voting behavior. Third,
the analysis covers a single platform and a single election.
Fourth, views and engagement are cumulative values measured
about a year after the election and include views accumulated
afterward. Although we control for the number of days to the
election and re-estimate the view-count model on campaign-
period videos—for which these intervals are nearly equal—
the dynamics of accumulation itself cannot be observed from
a single snapshot. Fifth, engagement metrics are limited to
likes and comments: direct measures of redistribution such
as shares and repeat views are not available through the
platform’s public API and can be seen only by the channel
owner. Furthermore, we do not analyze comment content, and
videos with comments disabled cannot be distinguished from
videos that received zero comments. Sixth, title sentiment is
measured by a dictionary-based method that may not capture
irony or context-dependent expressions.
Future work includes applying the same approach to other
elections in which clip videos have been held to matter, such
as the 2024 Hyogo gubernatorial election; analyzing comment
content; comparing platforms such as TikTok; and linking
viewing exposure to voting behavior through survey data.
VI. CONCLUSION
We analyzed 44,331 YouTube videos related to the nine
leading candidates in the 2024 Tokyo gubernatorial election
and examined how clip videos were associated with the
attention candidates received. Clip videos and mentions of
Shinji Ishimaru were each associated with higher view counts.
Their interaction was not significant, providing no evidence
that the association between clip videos and views was es-
pecially strong for videos mentioning Ishimaru. These results
held when correlation among videos within a channel was
accounted for and when the sample was restricted to videos
posted during the campaign period. Among non-clip videos, by
contrast, those mentioning Ishimaru received about 36% fewer
view-adjusted likes and 41% fewer view-adjusted comments
than those that did not.
These results show that the scale of views of videos about a
candidate and the amount of view-adjusted engagement need
not coincide. Understanding political influence online requires
distinguishing how widely content reached from how deep an
engagement it drew.
STATEMENTS
Data Availability: The collected dataset and code are
available from the authors upon request.
Ethical Statement: All data were collected through the
public YouTube Data API and consist only of publicly avail-
able video metadata, in accordance with YouTube’s Terms of
Service.
Disclosure Statement: The authors declare no potential
conflicts of interest with respect to the research, authorship,
and/or publication of this article.
REFERENCES
[1] Institute for Information and Communications Policy, Ministry of Inter-
nal Affairs and Communications, “Survey on time use and information
behavior for information and communications media, FY2024,” Ministry
of Internal Affairs and Communications, Jun. 27, 2025 (in Japanese).
https://www.soumu.go.jp/menu_news/s-news/01iicp01_02000125.html
[2] M. Taniguchi and S. Omori, “Political communication of the public: Fo-
cusing on information contact behavior with the media,” NIRA Research
Report, no. 3, NIRA Research Institute, Mar. 8, 2023 (in Japanese).
https://www.nira.or.jp/paper/research-report/2023/252301.html
[3] Kyoto Shimbun, “Clip videos: ‘I never thought so many people would
watch’ — channel operators earning pocket money and politicians
spreading their message share an interest,” Kyoto Shimbun, Jun. 25,
2025 (in Japanese). https://www.kyoto-np.co.jp/articles/-/1505873
[4] NHK, “Political clip videos: Over 3.5 billion total views — who
makes them and why?” NHK News, Feb. 22, 2025 (in Japanese).
https://www3.nhk.or.jp/news/html/20250222/k10014725691000.html
[5] Tokyo Metropolitan Election Administration Commission, “Results of
the 2024 Tokyo gubernatorial election,” Jul. 2024 (in Japanese).
https://www.senkyo.metro.tokyo.lg.jp/election/tochiji-all/tochiji-
sokuhou2024/result
[6] Mainichi Shimbun, “Little-known Shinji Ishimaru surges: ‘Of course I
am considering national politics,’” Mainichi Shimbun, Jul. 7, 2024 (in
Japanese). https://mainichi.jp/articles/20240707/k00/00m/010/117000c
[7] Senkyo.com Editorial Department, “Online advertising lit the fuse of
the ‘Ishimaru phenomenon’: A new campaign strategy revealed by
the gubernatorial election,” Senkyo.com, Jul. 19, 2024 (in Japanese).
https://go2senkyo.com/articles/2024/07/19/98232.html
[8] K. Yoneshige, “What was the Ishimaru phenomenon?
Analyzing the composition of Shinji Ishimaru’s 1.65
million votes with original data,” Yahoo! News, Jul. 7,
2024 (in Japanese). https://news.yahoo.co.jp/expert/articles/
3445aa21db852501d2b183d327408c69f5046910
[9] H. Nakamura, “Exploring YouTube’s role in shaping political dis-
course: A case study of the 2024 Tokyo gubernatorial elec-
tion,” in Proceedings of the 2024 IEEE International Confer-
ence on Big Data (BigData), Dec. 2024, pp. 3007–3016, doi:
https://doi.org/10.1109/BigData62323.2024.10825474.

[10] K. Miyazaki, M. Toyoda, T. Uchiba, and T. Anno, “Comparative analysis
of major candidates in the 2024 Tokyo gubernatorial election using X
data,” in Proceedings of the 39th Annual Conference of the Japanese
Society for Artificial Intelligence, 2025, p. 2P5OS2b02 (in Japanese),
doi: https://doi.org/10.11517/pjsai.JSAI2025.0_2P5OS2b02.
[11] M. Ida, “An analysis of the 2024 Tokyo gubernatorial election,” Seikei
Ronso (Review of Economics and Political Science), vol. 93, no. 5–6, pp.
29–50, Mar. 2025 (in Japanese). http://hdl.handle.net/10291/0002001692
[12] J. Berger and K. L. Milkman, “What makes online content viral?”
Journal of Marketing Research, vol. 49, no. 2, pp. 192–205, Apr. 2012,
doi: https://doi.org/10.1509/jmr.10.0353.
[13] J. A. Tucker, A. Guess, P. Barberá, C. Vaccari, A. Siegel, S. Sanovich, D.
Stukal, and B. Nyhan, “Social media, political polarization, and political
disinformation: A review of the scientific literature,” SSRN, Mar. 19,
2018, doi: https://doi.org/10.2139/ssrn.3144139.
[14] G. Cui, Y . Chung, L. Peng, and Q. Wang, “Clicks for money: Predicting
video views through a sentiment analysis of titles and thumbnails,”
Journal of Business Research, vol. 183, art. no. 114849, Oct. 2024,
doi: https://doi.org/10.1016/j.jbusres.2024.114849.
[15] W. J. Brady, J. A. Wills, J. T. Jost, J. A. Tucker, and J. J. Van Bavel,
“Emotion shapes the diffusion of moralized content in social networks,”
Proceedings of the National Academy of Sciences, vol. 114, no. 28, pp.
7313–7318, Jul. 2017, doi: https://doi.org/10.1073/pnas.1618923114.
[16] C. Violot, T. Elmas, I. Bilogrevic, and M. Humbert, “Shorts
vs. regular videos on YouTube: A comparative analysis of user
engagement and content creation trends,” in Proceedings of the
16th ACM Web Science Conference, 2024, pp. 213–223, doi:
https://doi.org/10.1145/3614419.3644023.
[17] R. Lewis, Alternative influence: Broadcasting the reactionary right on
YouTube. New York, NY: Data & Society Research Institute, 2018.
https://datasociety.net/library/alternative-influence/
[18] T.-S. Fischer, C. Kolo, and C. Mothes, “Political influencers on
YouTube: Business strategies and content characteristics,” Media
and Communication, vol. 10, no. 1, pp. 259–271, Feb. 2022, doi:
https://doi.org/10.17645/mac.v10i1.4767.
[19] B. T. Bowyer, J. E. Kahne, and E. Middaugh, “Youth com-
prehension of political messages in YouTube videos,” New Me-
dia & Society, vol. 19, no. 4, pp. 522–541, Apr. 2017, doi:
https://doi.org/10.1177/1461444815611593.
[20] M. H. Ribeiro, R. Ottoni, R. West, V . A. F. Almeida, and W. Meira, Jr.,
“Auditing radicalization pathways on YouTube,” in Proceedings of the
2020 Conference on Fairness, Accountability, and Transparency, 2020,
pp. 131–141, doi: https://doi.org/10.1145/3351095.3372879.
[21] H. Hosseinmardi, A. Ghasemian, A. Clauset, M. Mobius, D. M.
Rothschild, and D. J. Watts, “Examining the consumption of radi-
cal content on YouTube,” Proceedings of the National Academy of
Sciences, vol. 118, no. 32, art. no. e2101967118, Aug. 2021, doi:
https://doi.org/10.1073/pnas.2101967118.
[22] R. Gibson, R. Southern, C. Vaccari, P. Smyth, and J. Musayev, “Does
digital campaigning matter, and if so, how? Testing a broadcast versus
network effects model of candidates’ Twitter use,” Journal of Informa-
tion Technology & Politics, vol. 22, no. 3, pp. 357–372, 2025, doi:
https://doi.org/10.1080/19331681.2024.2387634.
[23] S. Boulianne, “Social media use and participation: A meta-
analysis of current research,” Information, Communication
& Society, vol. 18, no. 5, pp. 524–538, May 2015, doi:
https://doi.org/10.1080/1369118X.2015.1008542.
[24] P. Covington, J. Adams, and E. Sargin, “Deep neural networks
for YouTube recommendations,” in Proceedings of the 10th ACM
Conference on Recommender Systems, 2016, pp. 191–198, doi:
https://doi.org/10.1145/2959100.2959190.
[25] R. Fletcher and R. K. Nielsen, “Are people incidentally exposed
to news on social media? A comparative analysis,” New Me-
dia & Society, vol. 20, no. 7, pp. 2450–2468, Jul. 2018, doi:
https://doi.org/10.1177/1461444817724170.
[26] R. B. Zajonc, “Attitudinal effects of mere exposure,” Journal of Person-
ality and Social Psychology, vol. 9, no. 2, pt. 2, pp. 1–27, Jun. 1968,
doi: https://doi.org/10.1037/h0025848.
[27] C. D. Kam and E. J. Zechmeister, “Name recognition and candidate
support,” American Journal of Political Science, vol. 57, no. 4, pp.
971–986, Oct. 2013, doi: https://doi.org/10.1111/ajps.12034.
[28] M. A. Baum, “Sex, lies, and war: How soft news brings for-
eign policy to the inattentive public,” American Political Sci-
ence Review, vol. 96, no. 1, pp. 91–109, Mar. 2002, doi:
https://doi.org/10.1017/S0003055402004252.
[29] PRESIDENT Online, “Why Hiroyuki succeeded on YouTube: The
money-making mechanics of clip videos,” PRESIDENT Online, Apr.
23, 2022 (in Japanese). https://president.jp/articles/-/56908
[30] Yahoo! News Feature, “Are profit-driven clip videos unlawful?
The 2024 elections and the media,” Yahoo! News, Dec.
29, 2024 (in Japanese). https://news.yahoo.co.jp/articles/
2a3daa4226fcff25c892c4804b40497fa101339b
[31] NHK, “Major freelance marketplace to ban commissions for po-
litical clip videos,” NHK News, Apr. 26, 2025 (in Japanese).
https://www3.nhk.or.jp/news/html/20250426/k10014790021000.html
[32] NHK Broadcasting Culture Research Institute, “What effect did
YouTube have on the Hyogo gubernatorial election?” NHK Bunken
Blog, Apr. 28, 2025 (in Japanese). https://www.nhk.or.jp/bunken-
blog/500/675421.html
[33] NHK, “Party support rates,” NHK Election Web, 2025 (in Japanese).
https://www.nhk.or.jp/senkyo/shijiritsu/
[34] Y . Ikegami, “oseti: A sentiment analysis library for Python using
a Japanese polarity dictionary,” Qiita, Feb. 12, 2019 (in Japanese).
https://qiita.com/yukinoi/items/46aa016d83bb0e64f598
[35] B. Stelter, “How social media video clippers have become some
of the most powerful outlets of the 2024 campaign,” CNN,
Oct. 28, 2024. https://edition.cnn.com/2024/10/28/media/election-social-
media-video-clips-viral
