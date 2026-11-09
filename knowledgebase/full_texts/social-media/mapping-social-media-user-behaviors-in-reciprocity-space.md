---
title: Mapping Social Media User Behaviors in Reciprocity Space
url: https://arxiv.org/abs/2601.15623
category: social-media
subcategory: empirical
date: 2026-01
venue: ''
authors:
- Shiori Hironaka
- Hayato Oshimo
- Mitsuo Yoshida
- Kyoji Umemura
source: arxiv
pdf_url: https://arxiv.org/pdf/2601.15623
pages: 29
chars: 47188
fetched_at: '2026-11-08T13:05:58+00:00'
kb_version: 1
---

# Mapping Social Media User Behaviors in Reciprocity Space

Mapping Social Media User Behaviors in Reciprocity
Space
Shiori Hironakaa, Hayato Oshimob, Mitsuo Yoshidac, Kyoji Umemurab
aAcademic Center for Computing and Media Studies, Kyoto
University, hironaka@media.kyoto-u.ac.jp, Kyoto, Japan
bDepartment of Computer Science and Engineering, Toyohashi University of
Technology, Aichi, Japan
cInstitute of Business Sciences, University of Tsukuba, Tokyo, Japan
Abstract
Social media users exhibit diverse behavioral patterns as platforms func-
tion simultaneously as information and friendship networks. We introduce a
reciprocity-based framework mapping users onto two-dimensional space de-
fined by bidirectional connection ratios. Analyzing 48,830 Twitter users and
149 million connections, we demonstrate that fragmented user types from
prior studies (influencers, lurkers, brokers, and follow-back accounts) emerge
naturally as regions within continuous behavioral space rather than discrete
categories. User properties vary smoothly across the reciprocity dimensions,
revealing clear behavioral gradients. This framework provides the first uni-
fied model encompassing the full spectrum of social media behaviors and
offers interpretable metrics for influence measurement and platform design.
Keywords:social media, user behavior, network analysis, reciprocity
1. Introduction
Socialmediaplatformshavefundamentallytransformedhumancommuni-
cation, creating complex ecosystems where users engage in diverse behavioral
arXiv:2601.15623v1  [cs.SI]  22 Jan 2026

patterns [1, 2, 3, 4]. These platforms uniquely function as both information
networks and friendship networks, enabling users to simultaneously consume
news, maintain social relationships, broadcast content, and seek informa-
tion [5, 6, 7, 8, 9]. This multifaceted nature produces remarkable behavioral
diversity, yet understanding this diversity remains a central challenge in so-
cial media research. A comprehensive framework that can systematically
characterize the full spectrum of user behaviors across these interconnected
functions would be highly beneficial, and researchers continue to pursue such
unifying approaches.
Network structure provides an objective lens for understanding user be-
havior, complementing survey- [10, 11, 12, 13] and content-based [14] ap-
proaches. Early network-based studies laid the foundation for structural
approaches to user classification. Java et al. [5] analyzed Twitter’s net-
work topology and user activity patterns to identify distinct usage behav-
iors, revealing that users adapt platforms for fundamentally different pur-
poses. Building on this foundation, Krishnamurthy et al. [6] pioneered sys-
tematic network-based categorization by examining follower versus following
count relationships, identifying three broad user groups through in-degree
versus out-degree analysis: broadcasters who maintain far more followers
than people they follow (such as media outlets), acquaintances who maintain
roughly reciprocal follower–following numbers (mirroring typical friendship
networks), and evangelists or miscreants who follow many others but have
relatively few followers (often including spammers or aggressive networkers).
This foundational classification revealed distinct behavioral clusters in the
follower–followee space and established the principle that network structure
2

can effectively capture different user intentions and behaviors.
As social media evolved, researchers discovered additional specialized
types:influencersbroadcasting to large audiences [15, 16, 17, 18, 19, 20],
lurkersconsuming content while rarely creating [21, 22, 23, 24, 25],brokers
bridging distinct communities [26], andfollow-back accountsmaintaining re-
ciprocal connections [27, 28, 29]. Each exhibits distinct network signatures,
suggesting that network-based approaches have the potential to become uni-
versal measures of social media usage patterns.
Current network-based taxonomies face three fundamental limitations
that impede a comprehensive understanding of user behavior. First, they
treat user types as discrete categories rather than continuous phenomena,
forcing artificial boundaries on naturally fluid behaviors. Second, existing
metrics provide incomplete behavioral pictures: Followee-to-follower ratios
are inherently one-dimensional, meaning two users with identical 1.0 ratios
might have completely different connection patterns (one maintaining re-
ciprocal friendships, another having separate follower and followee groups).
Third, discovered user types remain fragmented across studies without a uni-
fied theoreticalframework, preventing systematiccomparison and integration
of findings.
Theselimitationsstemfromoverlookingacriticalnetworkdimension[30]—
reciprocity, which represents the extent of bidirectional (i.e., mutual) con-
nections between users [31, 32, 33, 34, 35]. While reciprocity is fundamental
in network theory, existing classification schemes ignore how bidirectional
connections fundamentally alter relationship meaning, distinguishing social
bonds from information channels. Although reciprocity is substantial on so-
3

cial platforms, Twitter exhibits relatively low reciprocity levels (ranging from
22%to58%accordingtovariousstudies[5,7,36,8])comparedtootheronline
social networks [37, 38, 39], indicating predominantly asymmetric relation-
ships that existing one-dimensional metrics fail to capture adequately. This
oversight highlights the need to consider local reciprocity patterns at the
individual user level, where the bidirectional connections vary significantly
among users and reveal distinct behavioral patterns.
We propose a reciprocity-based framework to address these limitations.
Our framework uses two complementary ratios: bidirectional edges to in-
degree (rin) and bidirectional edges to out-degree (r out). This approach
creates a continuous behavioral space where previously isolated user types
emerge naturally as regions rather than discrete categories. Through analy-
sis of 48,830 Twitter users and their complete ego networks comprising over
149 million connections, we conducted comprehensive behavioral character-
ization across multiple dimensions. We first identified four archetypal user
categories at the extremes of the reciprocity space and analyzed their dis-
tinctive behavioral signatures through user property analysis, characteristic
vocabulary extraction, and network formation patterns. We then examined
the continuous nature of user behavior by mapping property variations across
the entire reciprocity space, revealing smooth gradients rather than discrete
boundaries between user types.
Our analysis demonstrates three key findings. First, fragmented user
types from disparate studies unify systematically within our framework, with
influencers, lurkers, brokers, and follow-back accounts occupying distinct
reciprocity regions that correspond to the Feeding, Accumulating, Flow-
4

ing, and Circulating archetypes, respectively. Second, user behavior varies
smoothly across reciprocity space rather than exhibiting categorical bound-
aries, confirming that social media behaviors exist along continuous dimen-
sions. Remarkably, we identify an intermediatehigh engagement zoneat
moderate reciprocity values where content virality peaks, challenging as-
sumptions that pure broadcasting or highly reciprocal relationships optimize
engagement. Third, different user archetypes exhibit systematic connection
formation patterns that reveal underlying network mechanisms; interaction
preferences range from highly insular communities maintaining over 90%
within-group connections to information brokers bridging disparate network
regions. Our reciprocity-based framework is a promising approach that pro-
vides the first unified model encompassing the full spectrum of social media
behaviors. It offers interpretable metrics for influence measurement, content
recommendation, and platform design while illuminating how users navigate
social media’s multifaceted nature as both friendship and information net-
works.
2. Defining the Reciprocity Space
We define a two-dimensional space based on the reciprocity of users’ con-
nectionsindirectedsocialgraphs. Foragivennode, letk m denotethenumber
of bidirectional connections (bidirectional edges),ki the in-degree (number
of followers), andk o the out-degree (number of followees). We define two
5

0.0 0.2 0.4 0.6 0.8 1.0
rin
0.0
0.2
0.4
0.6
0.8
1.0rout
200
400
600
800
1000
1200
1400
1600
Flowing Accumula- ting
Feeding Circulating
other
Figure 1: User density distribution and archetype classification in reciprocity space. The
two-dimensional reciprocity space shows the population distribution of 48,830 users, with
rin (bidirectional edges to in-degree) on the x-axis androut (bidirectional edges to out-
degree) on the y-axis. Colors indicate user density, with four primary archetypes identified
in the corner regions: Feeding (top left), Accumulating (bottom right), Flowing (bottom
left), and Circulating (top right).
6

reciprocity measures:
rin = km + 1 ki + 1,(1)
rout = km + 1 ko + 1,(2)
where the constant+1avoids division by zero and can be interpreted as a
self-edge. This ensures both ratios range from 0 to 1, with the minimum
occurring whenk m = 0. Here,r in represents the proportion of reciprocal
connections among incoming edges (followers), whilerout represents the pro-
portion of reciprocal connections among outgoing edges (followees). While
these individual metrics have been used in previous studies [25, 40], we are
the first to combine them as coordinates in a two-dimensional behavioral
space.
Thistwo-dimensional(r in,r out)spaceprovidesgreaterexpressivenessthan
the traditional followee-to-follower ratiorf alone. The relationship between
these metrics is as follows:
rf = ko + 1 ki + 1 = rin rout .(3)
Thus, users with similar followee-to-follower ratios can occupy different posi-
tions in our reciprocity space, capturing fundamentally different connection
patterns.
3. Data
We collected tweets from Twitter’s 1% sample stream between July 11
and 13, 2021, extracting user IDs of those who posted at least one English
tweet. After deduplication, we randomly selected 50,000 users. For each
7

user, we retrieved up to 3,200 recent tweets and complete followee/follower
information using Twitter’s API between July 21 and 22, 2021. The final
dataset included 48,830 users with complete data.
Asaresult, wecollected42,227,635followingrelationshipsand107,233,898
follower relationships. Merging these datasets yielded 149,368,679 unique
following relationships, of which 21,482,872 were mutual (bidirectional) con-
nections. The overall reciprocal relationship ratio among users connected by
at least one edge in our constructed network was 16.8%. This value is lower
than those reported in other studies (21.1% by Kwak et al. [7] and 42% by
Myers et al. [8]). This difference likely stems from our sampling methodol-
ogy, as we sampled users appearing in Twitter’s sample stream rather than
employing snowball sampling or other network-based approaches.
4. Behavioral Signatures based on User Archetypes
4.1. Archetype Classification and Analysis Methods
To validate that the user reciprocity space captures meaningful behavioral
differences, we identified users occupying the extreme corners of the reci-
procity space, where the most pronounced behavioral patterns are expected
to emerge. We analyzed distinctive behavioral patterns for each user cate-
gory based on user properties, characteristic vocabulary, and inter-category
following relationships. User property analysis employed metrics across three
dimensions: activity patterns, network structure, and content engagement.
Users were classified into four archetypes by dividing reciprocity into
ranges using thresholds of 0.25 and 0.75 (Fig. 1). These thresholds were
chosen to isolate users with pronounced asymmetric (≤0.25) versus predom-
8

inantly reciprocal (≥0.75) connection patterns while maintaining sufficient
sample sizes for robust statistical analysis. This choice is based on the prin-
ciple that users at these extremes would exhibit the clearest manifestations
of distinct behavioral archetypes, allowing us to characterize the fundamen-
tal patterns underlying the reciprocity space. The resulting four archetypes
represent the theoretical extremes of reciprocity behavior:
•Feeding class (lowr in, highr out): These are users who reciprocate with
most accounts they follow but attract many non-reciprocal followers,
wherer in ≤0.25andr out ≥0.75, typical of content broadcasting pat-
terns.
•Accumulating class (highr in, lowr out): These are users who maintain
reciprocal relationships with most of their followers but follow many
accounts without reciprocation, whererin ≥0.75andr out ≤0.25, char-
acteristics of information-seeking behavior.
•Flowing class (lowr in, lowr out): These are users with predominantly
unidirectional connections in both directions, wherer in ≤0.25and
rout ≤0.25, representing minimal reciprocal engagement patterns.
•Circulating class (highr in, highr out): These are users maintaining
high reciprocity in both directions, whererin ≥0.75andr out ≥0.75,
reflecting strong bidirectional connection preferences.
Fromoursampleof48,830users, weidentified5,640Flowingusers(11.6%),
3,998 Accumulating users (8.2%), 1,403 Feeding users (2.9%), and 4,634 Cir-
culating users (9.5%). The remaining 33,155 users (67.9%) occupied interme-
9

diate positions in the reciprocity space, demonstrating the continuous nature
of user behavior patterns that our framework captures.
For activity patterns, we analyzed tweet composition (original posts,
retweets, replies, and quote tweets), posting frequency, total posts and likes,
and account creation date. Tweet ratios were calculated from up to 3,200
collected tweets per user, with retweets, replies, and quote tweets treated as
mutually exclusive categories, by removing retweets from other tweets. Daily
tweet frequency was computed by dividing timeline tweet counts by the time
span between the oldest and newest posts. We plotted the distribution of
thesemetricsbyusingletter-valueplot[41]. Networkstructurewascharacter-
ized using follower and followee counts extracted from user profile data. Con-
tent engagement was measured through average retweeted and liked counts
per tweet. To account for engagement decay, we calculated averages using
only posts made before July 20, 2021 (24+ hours before data collection),
applying original post timestamps for retweets. Metrics were computed both
for all tweets and original content only. To validate that these behavioral
patterns represent distinct user populations, we performed Kruskal–Wallis
tests [42] across all measured properties, followed by Conover’s post-hoc
test [43] for pairwise comparisons between archetype pairs. To address the
multiple testing problem, we applied Holm’s method forp-value adjustment.
Characteristic vocabulary for each archetype was identified using chi-
square statistics on English original tweets. Text preprocessing included
removing mentions, URLs, special characters, emojis, and stopwords, fol-
lowed by tokenization using NLTK’s TweetTokenizer [44]. We calculated
Chi-square values by treating each user’s combined posts as a single docu-
10

ment:
E00 = (N01 +N 00)(N10 +N 00) Nall ,(4)
E01 = (N01 +N 11)(N00 +N 01) Nall ,(5)
E10 = (N10 +N 11)(N00 +N 10) Nall ,(6)
E11 = (N01 +N 11)(N10 +N 11) Nall ,(7)
χ2 = X
w∈{0,1}
X
u∈{0,1}
(Ewu −N wu)2
Ewu
,(8)
whereN 0∗/N1∗ represent users not using/using a word,N∗0/N∗1 represent
users outside/within the category, andNall represents the total users.
Following relationships between archetypes were analyzed by counting
cross-archetype connections and calculating row-normalized values (follow-
ing tendency) and column-normalized values (follower tendency) to reveal
interaction patterns between user categories.
4.2. Behavioral Characteristics of Each Archetype
Figures 2 and 3 and Table 1 present comprehensive behavioral profiles
for each user archetype across multiple analytical dimensions. The letter-
value plots (Figure 2) reveal systematic differences in user properties across
the four archetypes and intermediate users. The characteristic vocabulary
analysis (Table 1) identifies distinctive linguistic features for each archetype
based on chi-square statistics, while the following relationship distributions
(Figure 3) reveal inter-archetype connection patterns. These multifaceted
results demonstrate that the reciprocity-based classification captures funda-
mentally different user behaviors that manifest consistently across diverse
11

metrics. We now examine each archetype’s distinctive behavioral signature
in detail.
Feeding users demonstrated information broadcasting behavior, charac-
terized by significantly lower retweet rates (mean 29%,p <4×10−27) and
higher original content production (mean 34%,p <2×10 −60) compared to
all other archetypes. They maintained dramatically asymmetric networks,
with significantly more followers (median>2,000) than followees (median
230) (Figs. 2i and 2j), and achieved the highest engagement per original
post (median 0.59 retweets,p <1×10 −81; 3.77 likes,p <1×10 −115)
(Figs. 2m and 2n). Their vocabulary focused on scheduling and experiences
(“tonight,” “date,” “weekend,” and“excited”)(Table1). Despiteshowingmod-
erate in-group preference (64.0%), they attracted extensive following from
other archetypes, particularly Flowing (67.8%) and Accumulating (58.3%)
users (Figs. 3a and 3b). These patterns unify influencers and information
broadcasterswithinourreciprocityframework. Unliketraditionalapproaches
focusing solely on asymmetric audiences, our framework reveals that effec-
tive broadcasters strategically maintain high reciprocity in outgoing connec-
tions (rout ≥0.75) while attracting predominantly non-reciprocal followers
(rin ≤0.25). Thisdemonstratesstrategic curationoffolloweenetworksalong-
side broadcasting to wider audiences, with evidence from Niitsuma et al. [45]
that content reposted by highly influential users reaches significantly broader
audiences.
Accumulatingusersdemonstratedclearinformation-seekingbehaviorwith
significantly higher retweet rates than Feeding and Circulating users (mean
51%,p <8×10 −64 vs. Feeding and Circulating) (Fig. 2b), lower activity
12

levels than all other archetypes (median 769 total tweets,p <2×10 −307)
(Fig. 2e), and minimal follower counts (median 22,p <2×10 −230 vs.
all other archetypes) (Fig. 2j). Their tweets received significantly less en-
gagement than all other archetypes (mean retweets:p <4×10 −7; mean
likes:p <2×10 −5) (Figs. 2k and 2l), and their vocabulary consisted of
generic verbs and states (“stay,” “ready,” “drop,” and “rest”) (Table 1). They
distributed follows across archetypes, particularly targeting Feeding users
(58.3%) (Figs. 3a and 3b). These users unify previously scattered observa-
tions of lurkers and information seekers through their distinctive reciprocity
pattern (rout ≤0.25,r in ≥0.75), which captures asymmetric consumption
behavior: following many accounts while maintaining few reciprocal connec-
tions, indicating strategic information gathering rather than social relation-
ship building. While traditional lurker definitions focus on content consump-
tion without creation, our reciprocity-based approach reveals that these users
actively curate their information sources through strategic following patterns
while maintaining minimal public engagement. This aligns with character-
izations of silent users [25] and demonstrates how reciprocity measures can
quantitatively identify information consumption patterns.
Flowing users exhibited information brokering patterns with the high-
est retweet rates among all archetypes (mean 55%,p <0.0008) (Fig. 2b).
Their vocabulary mixed intimate terms with news-related content (“china,”
“election,” “congress,” and “strategy”) (Table 1), and they demonstrated in-
termediate network formation patterns by extensively following Feeding users
(67.8%)whilemaintainingnotablewithin-archetypeconnections(23.8%)(Figs.3a
and 3b). These users unify network brokers within our reciprocity framework
13

by maintaining minimal reciprocal connections in both directions (rin ≤0.25,
rout ≤0.25). This captures the bridging behavior identified by Tsugawa and
Watabe [26] through more complex structural measures. Their mixed vo-
cabulary confirms their role as information intermediaries spanning different
domains, while low reciprocity patterns indicate that they connect disparate
network regions without forming strong mutual bonds.
Circulating users exhibited the strongest interaction orientation, with
significantly higher reply rates (median 34.0%,p <1×10 −20) and quote
tweet usage (mean 9.3%,p <0.002) than all other archetypes (Figs. 2c
and 2d). They maintained balanced followee and follower counts (medians
613 and 614), which differed significantly from other archetypes (number of
followees:p <1×10 −86, number of followers:p <1×10 −39, vs. all other
archetypes) (Figs. 2i and 2j). These users formed highly insular communi-
ties, with 91.5% of their follows and 94.5% of their followers within the same
archetype (Figs. 3a and 3b). Their characteristic vocabulary included inti-
mate expressions (“moot,” “bestie,” and “ily”) and daily social interactions
(“birthday,” “goodnight,” and “morning”) (Table 1). These patterns align
with the follow-back account phenomenon identified by Elmas et al. [29], al-
though our framework reveals that this behavior spans both automated and
human users, as evidenced by the combination of high reciprocity metrics
and intimate vocabulary patterns. Ghosh et al. [28] demonstrated that such
social capitalistswho follow back anyone who follows them are widespread
on Twitter and often engage in link farming strategies to artificially inflate
their follower counts. Notably, this archetype presents an intriguing paradox:
While exhibiting follow-back behaviors that theoretically promote openness,
14

these users simultaneously form highly insular communities. The extreme
insularity combined with intimate vocabulary suggests that this archetype
encompasses both genuine social communities seeking intimate communica-
tion through mutual following and coordinated accounts employing recipro-
cal strategies. These findings that follow-back accounts maintain nearly 1:1
followee-to-follower ratios and tend to have a high number of followers align
with our Circulating users’ high reciprocity patterns.
While the four archetypes represent distinct behavioral patterns at the
extremes of reciprocity space, a substantial portion of users (33,155 out of
48,830, representing 67.9% of our sample) fell into the intermediate regions
between these archetypes. Rather than exhibiting the pronounced charac-
teristics that define the corner positions, these users display moderate reci-
procity patterns that blend elements from multiple archetypes. This distri-
bution demonstrates that the majority of social media users operate within a
behavioral continuum rather than conforming to rigid categorical boundaries.
The prevalence of intermediate users reinforces our framework’s fundamental
premise that user behavior exists along continuous dimensions. In this view,
the four archetypes serve as reference points that anchor a broader spectrum
of social media engagement patterns. These intermediate users represent
the natural variation in how individuals balance information consumption,
content creation, and relationship formation within the constraints and af-
fordances of social media platforms.
15

Flw Acc Fed Cir oth
0.0
0.2
0.4
0.6
0.8
1.0
(a) Percentage of origi-
nal posts
Flw Acc Fed Cir oth
0.0
0.2
0.4
0.6
0.8
1.0
(b) Percentage of
retweets
Flw Acc Fed Cir oth
0.0
0.2
0.4
0.6
0.8
1.0
(c) Percentage of replies
Flw Acc Fed Cir oth
0.0
0.2
0.4
0.6
0.8
1.0 (d) Percentage of quote
posts
Flw Acc Fed Cir oth
101
103
105
(e) Number of total
posts
Flw Acc Fed Cir oth
10 2
100
102
(f) Tweets per day
Flw Acc Fed Cir oth
101
103
105 (g) Number of likes
Flw Acc Fed Cir oth
2008
2010
2012
2014
2016
2018
2020
2022 (h) Account creation
date
Flw Acc Fed Cir oth
100
101
102
103
104
105
(i) Number of followees
Flw Acc Fed Cir oth
101
103
105 (j) Number of followers
Flw Acc Fed Cir oth
10 4
10 2
100
102
104
106
(k) Mean number of
retweeted
Flw Acc Fed Cir oth
10 4
10 2
100
102
104
106
(l) Mean number of liked
Flw Acc Fed Cir oth
10 3
10 1
101
103 (m) Mean number of
retweeted of original
posts
Flw Acc Fed Cir oth
10 3
10 1
101
103
(n) Mean number of
liked of original posts
Figure 2:(For review: To be combined with Table 1 and Fig. 3 in final version.)Behavioral
signatures and network patterns of user archetypes. Letter-value plots show distributions
of user properties across five categories: Flowing (Flw), Accumulating (Acc), Feeding
(Fed), Circulating (Cir), and Other (Oth). Statistical significance across all behavioral
metrics was confirmed through Kruskal–Wallis tests (allp <4×10 −124). (a–d) Tweet
composition patterns showing percentage of original posts, retweets, replies, and quote
tweets. (e–h) Activity and temporal metrics including total posts, daily posting frequency,
total likes made, and account creation dates. (i–j) Network structure showing followee and
follower counts. (k–n) Content engagement metrics measuring mean retweeted and liked
for all posts and original posts specifically.
16

Table 1:(For review: To be combined with Figures 2 and 3 in final version.)Behavioral
signatures and network patterns of user archetypes. Characteristic vocabulary table show-
ing the top 20 words for each archetype with chi-square statistics indicating strength of
association.
Circulatingχ 2 Feedingχ 2 Accumulatingχ 2 Flowingχ 2
moot1299.8tonight427.1stay468.5bestie649.2
bestie1172.6dm408.0morning433.0ily599.7
ily1039.3date342.8ready433.0youuu431.9
tl690.9sent339.0dm427.9moot423.1
youuu647.1weekend333.1drop423.1tl400.4
okay622.1text333.1rest416.9rn385.1
besties618.5saturday328.2night414.1goodnight361.7
birthday613.5room325.7close393.7besties326.1
goodnight604.4tomorrow323.5view390.6okay309.7
aaa586.2send323.5break390.1china306.2
morning569.5excited316.9girl387.9twt293.4
twt539.1friday315.4eye386.8profit277.8
cute512.5later314.1full383.6election271.5
rn510.7gift312.8month382.8congress262.3
dm509.7taking308.9coming382.1im259.1
sm499.1inside308.5waiting380.9idk251.2
rt496.4putting306.9baby374.5fr238.7
happy477.3set306.7mind371.5aaa237.7
love474.4promise305.7soon367.7launch231.5
ofc468.1sunday303.1cover367.2strategy230.2
17

Cir Fed Acc Flw
0.0
0.2
0.4
0.6
0.8
1.0Incoming connections
Circulating
Feeding
Accumulating
Flowing
(a) Distribution of incoming follows by archetype
Cir Fed Acc Flw
0.0
0.2
0.4
0.6
0.8
1.0Outgoing connections
Circulating
Feeding
Accumulating
Flowing (b) Distribution of outgoing follows by archetype
Figure 3:(For review: To be combined with Figure 2 and Table 1 in final version.)Be-
havioral signatures and network patterns of user archetypes. (a–b) Following relationship
patterns showing distribution of incoming and outgoing connections by archetype, reveal-
ing intergroup interaction preferences.
5. Continuous Behavioral Gradients Across Reciprocity Space
Having established four archetypal behaviors at the extremes of the reci-
procity space, we now examine the continuous nature of the behavioral space
where 67.9% of users reside. To visualize behavioral gradients, we divided
the reciprocity space into a10×10grid. For each cell, we calculated median
property values across all users within that reciprocity range and visualized
results as heatmaps with contour lines indicating smooth transitions. This
analysis directly addresses the fundamental limitations of existing classifica-
tion approaches. Unlike HITS scores [46] that lack intuitive interpretation
or simple followee-to-follower ratios that obscure behavioral distinctions, our
reciprocity-based framework reveals the true continuous nature of user be-
havior that previous taxonomies failed to capture. The analysis included
user metrics across activity patterns (tweet composition, posting frequency,
18

and engagement), network structure (follower/followee counts), and content
engagement for both all posts and original posts.
The results are shown in Fig. 4. Most properties showed smooth gradi-
ents across the space, confirming that the four archetypes represent extremes
of continuous distributions rather than discrete categories. This finding fun-
damentally challenges the rigid categorization assumptions underlying pre-
vious studies that treated user types as mutually exclusive groups. Network
structural properties displayed expected patterns: Followee count increased
toward high values of both reciprocity measures, while follower count peaked
at lowrin and highrout (the Feeding region). Account age showed interesting
variation, with newer accounts more prevalent in high-reciprocity regions,
suggesting evolving platform usage patterns over time.
Remarkably, contentengagementmetrics(retweetandlikecounts)peaked
not at the archetype extremes but in an intermediate high engagement zone
(approximatelyr in 0.5–0.7,r out 0.6–0.9). This region, characterized by mod-
erate reciprocity in both dimensions, appears optimal for content virality.
Users in this zone balance sufficient reciprocal connections for initial content
endorsement with enough asymmetric followers for broader reach. This find-
ing directly contradicts the limitations of one-dimensional approaches that
would classify such users identically despite their strategic positioning for
optimal engagement. The discovery of this high engagement zone exempli-
fies how our framework resolves the interpretational ambiguities that plague
existing metrics. Two users with identical followee-to-follower ratios near 1.0,
which traditional approaches would classify similarly, occupy distinct posi-
tions in our reciprocity space with markedly different engagement outcomes.
19

This demonstrates that strategic positioning in intermediate reciprocity re-
gions, rather than pure broadcasting or highly reciprocal relationships, opti-
mizes content virality.
Our reciprocity-based approach reveals that specialized behaviors from
prior studies (influencers, lurkers, brokers, and follow-back accounts) rep-
resent positions within a continuous behavioral space rather than discrete
phenomena. This two-dimensional reciprocity space provides a generalizable
framework applicable across social media platforms, unlike platform-specific
methods or complex structural measures used previously. User types exist
on a spectrum with smooth gradients in properties across reciprocity space,
allowing mixed characteristics and transitions between types over time. The
high engagement zone in intermediate reciprocity regions provides novel in-
sights that challenge assumptions about rigid user categorization while offer-
ing practical guidance for content creators seeking optimal virality.
6. Limitations and Future Directions
Our analysis is based on data from a single social media platform (Twit-
ter) collected from English-language posts in the 1% sample stream during
July 2021. This sampling approach likely overrepresents active users and
English speakers while underrepresenting non-English-speaking communities
and users who rarely or never post content. Despite these sampling con-
straints, we believe that our analysis of 48,830 users provides sufficiently
robust results to establish the validity of our reciprocity-based framework.
Our framework relies exclusively on structural network properties to char-
acterize user behavior. While we demonstrate that these structural features
20

/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj17/aj15/aj17/aj22
/aj17/aj15/aj18/aj17
/aj17/aj15/aj18/aj22
/aj17/aj15/aj19/aj17
/aj17/aj15/aj19/aj22
(a) Percentage of origi-
nal posts
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj17/aj15/aj18
/aj17/aj15/aj19
/aj17/aj15/aj20
/aj17/aj15/aj21
/aj17/aj15/aj22
/aj17/aj15/aj23
/aj17/aj15/aj24
(b) Percentage of
retweets
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj17/aj15/aj18/aj17
/aj17/aj15/aj18/aj22
/aj17/aj15/aj19/aj17
/aj17/aj15/aj19/aj22
/aj17/aj15/aj20/aj17
/aj17/aj15/aj20/aj22
/aj17/aj15/aj21/aj17
(c) Percentage of replies
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj17/aj15/aj17/aj17
/aj17/aj15/aj17/aj18
/aj17/aj15/aj17/aj19
/aj17/aj15/aj17/aj20
/aj17/aj15/aj17/aj21
/aj17/aj15/aj17/aj22
/aj17/aj15/aj17/aj23 (d) Percentage of quotes
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj22/aj17/aj17/aj17
/aj18/aj17/aj17/aj17/aj17
/aj18/aj22/aj17/aj17/aj17
/aj19/aj17/aj17/aj17/aj17
/aj19/aj22/aj17/aj17/aj17
/aj20/aj17/aj17/aj17/aj17
(e) Number of total
posts
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj22
/aj18/aj17
/aj18/aj22
/aj19/aj17
(f) Tweets per day
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj19/aj22/aj17/aj17
/aj22/aj17/aj17/aj17
/aj24/aj22/aj17/aj17
/aj18/aj17/aj17/aj17/aj17
/aj18/aj19/aj22/aj17/aj17
/aj18/aj22/aj17/aj17/aj17
/aj18/aj24/aj22/aj17/aj17 (g) Number of likes
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj19/aj17/aj18/aj20
/aj19/aj17/aj18/aj22
/aj19/aj17/aj18/aj24
/aj19/aj17/aj18/aj26
/aj19/aj17/aj19/aj18 (h) Account created at
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj18/aj17/aj17
/aj19/aj17/aj17
/aj20/aj17/aj17
/aj21/aj17/aj17
/aj22/aj17/aj17
/aj23/aj17/aj17
/aj24/aj17/aj17
(i) Number of followees
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj18/aj17/aj17/aj17
/aj19/aj17/aj17/aj17
/aj20/aj17/aj17/aj17
/aj21/aj17/aj17/aj17
/aj22/aj17/aj17/aj17
/aj23/aj17/aj17/aj17
/aj24/aj17/aj17/aj17
/aj25/aj17/aj17/aj17 (j) Number of followers
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj19/aj22/aj17
/aj22/aj17/aj17
/aj24/aj22/aj17
/aj18/aj17/aj17/aj17
/aj18/aj19/aj22/aj17
/aj18/aj22/aj17/aj17
/aj18/aj24/aj22/aj17
(k) Mean number of
retweeted
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj18/aj17/aj17/aj17
/aj19/aj17/aj17/aj17
/aj20/aj17/aj17/aj17
/aj21/aj17/aj17/aj17
/aj22/aj17/aj17/aj17
/aj23/aj17/aj17/aj17
/aj24/aj17/aj17/aj17
(l) Mean number of liked
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj17/aj15/aj17
/aj17/aj15/aj22
/aj18/aj15/aj17
/aj18/aj15/aj22
/aj19/aj15/aj17 (m) Mean number of
retweeted of original
posts
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
rin
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17rout
/aj19
/aj21
/aj23
/aj25
/aj18/aj17
/aj18/aj19
/aj18/aj21
(n) Mean number of
liked of original posts
Figure 4: Continuous behavioral gradients across reciprocity space. Heatmaps showing
median user property values across a10×10grid of the two-dimensional reciprocity space
(rin,r out), with contour lines indicating smooth transitions between behavioral regions.
(Caption continues on the following page.)
21

Figure 4:(Continued)The analysis reveals that user behavior exists along continuous
quantitative dimensions rather than discrete categories. (a–d) Tweet composition patterns
showing gradual transitions in content creation behavior. (e–h) Activity and temporal
patterns demonstrating smooth gradients in user engagement and platform adoption. (i–j)
Network structure metrics revealing continuous variation in social connectivity patterns.
(k–l) Overall content engagement showing how different reciprocity positions influence
content reach. (m–n) Original content engagement metrics, with peak values occurring
in an intermediate high engagement zone (approximatelyrin 0.5–0.7,r out 0.6–0.9) where
balanced reciprocal connections optimize content virality. Each cell represents the median
value for users within that reciprocity range.
effectively capture patterns in user activity and content engagement, our ap-
proach does not incorporate detailed content analysis or contextual informa-
tion about interaction partners. Consequently, some nuanced aspects of user
behavior and motivation may not be fully reflected in our reciprocity-based
characterization.
Future research should investigate how cultural differences influence user
positioning within the reciprocity space, analyze user interaction patterns
across multiple platforms and time periods, and explore the underlying mech-
anisms that drive different reciprocity patterns. Such studies would provide
in-depth insights into the generalizability and temporal dynamics of the be-
havioral patterns we have identified.
References
[1] d. m. boyd, N. B. Ellison, Social Network Sites: Definition, History, and
Scholarship, Journal of Computer-Mediated Communication 13 (2007)
210–230.
22

[2] B. J. Jansen, M. Zhang, K. Sobel, A. Chowdury, Twitter power: Tweets
as electronic word of mouth, Journal of the American Society for Infor-
mation Science and Technology 60 (2009) 2169–2188.
[3] R. Hanna, A. Rohm, V. L. Crittenden, We’re all connected: The power
of the social media ecosystem, Business Horizons 54 (2011) 265–273.
[4] S. M. Chan-Olmsted, M. Cho, S. Lee, User Perceptions of Social Media:
A Comparative Study of Perceived Characteristics and User Profiles by
SocialMedia, OnlineJournalofCommunicationandMediaTechnologies
3 (2013) 149–178.
[5] A. Java, X. Song, T. Finin, B. Tseng, Why We Twitter: Understanding
Microblogging Usage and Communities, in: Proceedings of the 9th
WebKDD and 1st SNA-KDD 2007 Workshop on Web Mining and Social
Network Analysis, 2007, pp. 56–65.
[6] B. Krishnamurthy, P. Gill, M. Arlitt, A Few Chirps About Twitter, in:
Proceedings of the first Workshop on Online Social Networks, 2008, pp.
19–24.
[7] H. Kwak, C. Lee, H. Park, S. Moon, What is Twitter, a Social Network
or a News Media?, in: Proceedings of the 19th International Conference
on World Wide Web, 2010, pp. 591–600.
[8] S.A.Myers, A.Sharma, P.Gupta, J.Lin, InformationNetworkorSocial
Network? The Structure of the Twitter Follow Graph, in: Proceedings
of the 23rd International Conference on World Wide Web, 2014, pp.
493–498.
23

[9] D.Romero, J.Kleinberg, TheDirectedClosureProcessinHybridSocial-
Information Networks, with an Analysis of Link Formation on Twitter,
Proceedings of the International AAAI Conference on Web and Social
Media 4 (2010) 138–145.
[10] P. B. Brandtzæg, J. Heim, Why People Use Social Networking Sites, in:
Online Communities and Social Computing, 2009, pp. 143–152.
[11] S. Oh, S. Y. Syn, Motivations for Sharing Information and Social Sup-
port in Social Media: A Comparative Analysis of Facebook, Twitter,
Delicious, YouTube, and Flickr, Journal of the Association for Informa-
tion Science and Technology 66 (2015) 2045–2060.
[12] K.-Y. Lin, H.-P. Lu, Why people use social networking sites: An em-
pirical study integrating network externalities and motivation theory,
Computers in Human Behavior 27 (2011) 1152–1161.
[13] T. Tominaga, Y. Hijikata, J. A. Konstan, How self-disclosure in Twitter
profiles relate to anonymity consciousness and usage objectives: a cross-
cultural study, Journal of Computational Social Science 1 (2018) 391–
435.
[14] D. Kim, Y. Jo, I.-C. Moon, A. Oh, Analysis of Twitter Lists as a
Potential Source for Discovering Latent Characteristics of Users, in:
ACM CHI Workshop on Microblogging, 2010, p. 8.
[15] M. Cha, H. Haddadi, F. Benevenuto, K. Gummadi, Measuring User
Influence in Twitter: The Million Follower Fallacy, Proceedings of the
24

International AAAI Conference on Web and Social Media 4 (2010) 10–
17.
[16] E. Bakshy, J. M. Hofman, W. A. Mason, D. J. Watts, Everyone’s an
Influencer: Quantifying Influence on Twitter, in: Proceedings of the
Fourth ACM International Conference on Web Search and Data Mining,
2011, pp. 65–74.
[17] T. Huynh, I. Zelinka, X. H. Pham, H. D. Nguyen, Some measures to de-
tect the influencer on social network based on information propagation,
in: ACM International Conference Proceeding Series, 2019, pp. 1–6.
[18] N. Pagan, W. Mei, C. Li, F. Dörfler, A meritocratic network formation
model for the rise of social media influencers, Nature Communications
12 (2021) 6865.
[19] M. R. DeVerna, R. Aiyappa, D. Pacheco, J. Bryden, F. Menczer, Iden-
tifying and characterizing superspreaders of low-credibility content on
Twitter, PLOS ONE 19 (2024) e0302201.
[20] M. J. Harris, R. Murtfeldt, S. Wang, E. A. Mordecai, J. D. West, Per-
ceived experts are prevalent and influential within an antivaccine com-
munity on Twitter, PNAS Nexus 3 (2024) pgae007.
[21] A. Tagarelli, R. Interdonato, “Who’s out there?”: identifying and rank-
ing lurkers in social networks, in: Proceedings of the 2013 IEEE/ACM
International Conference on Advances in Social Networks Analysis and
Mining, 2013, pp. 215–222.
25

[22] N. Edelmann, Reviewing the definitions of “lurkers” and some impli-
cations for online research, Cyberpsychology, Behavior and Social Net-
working 16 (2013) 645–649.
[23] A. Tagarelli, R. Interdonato, Lurking in social networks: topology-based
analysis and ranking methods, Social Network Analysis and Mining 4
(2014) 230.
[24] N. Sun, P. P.-L. Rau, L. Ma, Understanding lurkers in online commu-
nities: A literature review, Computers in Human Behavior 38 (2014)
110–117.
[25] W. Gong, E.-P. Lim, F. Zhu, Characterizing Silent Users in Social Media
Communities, Proceedings of the International AAAI Conference on
Web and Social Media 9 (2015) 140–149.
[26] S. Tsugawa, K. Watabe, Identifying Influential Brokers on Social Media
from Social Network Structure, Proceedings of the International AAAI
Conference on Web and Social Media 17 (2023) 842–853.
[27] J. Hopcroft, T. Lou, J. Tang, Who Will Follow You Back? Reciprocal
Relationship Prediction, in: Proceedings of the 20th ACM Interna-
tional Conference on Information and Knowledge Management, 2011,
pp. 1137–1146.
[28] S. Ghosh, B. Viswanath, F. Kooti, N. K. Sharma, G. Korlam, F. Ben-
evenuto, N. Ganguly, K. P. Gummadi, Understanding and Combating
Link Farming in the Twitter Social Network, in: Proceedings of the 21st
International Conference on World Wide Web, 2012, pp. 61–70.
26

[29] T.Elmas, M.Randl, Y.Attia, #TeamFollowBack: Detection&Analysis
of Follow Back Accounts on Social Media, Proceedings of the Interna-
tional AAAI Conference on Web and Social Media 18 (2024) 381–393.
[30] A. Almaatouq, L. Radaelli, A. Pentland, E. Shmueli, Are You Your
Friends’ Friend? Poor Perception of Friendship Ties Limits the Ability
to Promote Behavioral Change, PloS ONE 11 (2016) e0151588.
[31] D. Garlaschelli, M. I. Loffredo, Patterns of link reciprocity in directed
networks, Physical review letters 93 (2004) 268701.
[32] T. Squartini, F. Picciolo, F. Ruzzenenti, D. Garlaschelli, Reciprocity of
weighted networks, Scientific Reports 3 (2013) 2729.
[33] B. Jiang, Z.-L. Zhang, D. Towsley, Reciprocity in Social Networks with
Capacity Constraints, in: Proceedings of the 21th ACM SIGKDD In-
ternational Conference on Knowledge Discovery and Data Mining, 2015,
pp. 457–466.
[34] C. Ding, J. Wang, Link reciprocity in directed multiplex networks, in:
Proceedings of the 2021 5th International Conference on Cloud and Big
Data Computing, 2021, pp. 102–108.
[35] A. Gallo, F. Saracco, R. Lambiotte, D. Garlaschelli, T. Squartini, Pat-
terns of link reciprocity in directed, signed networks, Physical Review
E 111 (2025) 024312.
[36] D. Rout, K. Bontcheva, D. Preoţiuc-Pietro, T. Cohn, Where’s @wally?:
A Classification Approach to Geolocating Users Based on their Social
27

Ties, in: Proceedings of the 24th ACM Conference on Hypertext and
Social Media, 2013, pp. 11–20.
[37] R. Kumar, J. Novak, A. Tomkins, Structure and evolution of online so-
cial networks, in: Proceedings of the 12th ACM SIGKDD international
conference on Knowledge discovery and data mining, 2006, pp. 611–617.
[38] M. Cha, A. Mislove, K. P. Gummadi, A measurement-driven analysis of
information propagation in the flickr social network, in: Proceedings of
the 18th international conference on World wide web, 2009, pp. 721–730.
[39] R. Kumar, J. Novak, A. Tomkins, Structure and Evolution of Online
Social Networks, in: P. S. Yu, J. Han, C. Faloutsos (Eds.), Link Mining:
Models, Algorithms, and Applications, Springer New York, 2010, pp.
337–357.
[40] H. Takemura, A. Tanaka, K. Tajima, Classification of Twitter Follow
Links Based on the Followers’ Intention, in: Proceedings of the 30th
Annual ACM Symposium on Applied Computing, 2015, pp. 1174–1180.
[41] H. Hofmann, H. Wickham, K. Kafadar, Letter-Value Plots: Boxplots
for Large Data, Journal of Computational and Graphical Statistics 26
(2017) 469–477.
[42] W. H. Kruskal, W. A. Wallis, Use of Ranks in One-Criterion Variance
Analysis, Journal of the American Statistical Association 47 (1952)
583–621.
[43] W. J. Conover, Practical Nonparametric Statistics, 3rd ed., Wiley,
Hoboken, NJ, 1999.
28

[44] S. Bird, E. Loper, E. Klein, Natural Language Processing with Python,
O’Reilly Media Inc., 2009.
[45] T. Niitsuma, M. Yoshida, H. Tamori, Y. Nakawake, Prestige bias drives
theviralspreadofcontentrepostedbyinfluencersinonlinecommunities,
Scientific Reports 15 (2025) 15282.
[46] J. M. Kleinberg, Authoritative sources in a hyperlinked environment,
Journal of the ACM 46 (1999) 604–632.
29
