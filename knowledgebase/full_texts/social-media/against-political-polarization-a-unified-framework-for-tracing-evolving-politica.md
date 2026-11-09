---
title: 'Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies
  on Social Media'
url: https://arxiv.org/abs/2608.17987
category: social-media
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Yijie Xu
- Chao Wang
- Hui Xiong
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.17987
pages: 35
chars: 125886
fetched_at: '2026-11-08T12:57:54+00:00'
kb_version: 1
---

# Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media

Against Political Polarization: A Unified Framework for
Tracing Evolving Political Ideologies on Social Media
YIJIE XU,Thrust of Artificial Intelligence, The Hong Kong University of Science and Technology (Guangzhou),
China
CHAO WANG∗,School of Artificial Intelligence and Data Science, University of Science and Technology of
China, China
HUI XIONG ∗,Thrust of Artificial Intelligence, The Hong Kong University of Science and Technology
(Guangzhou), China and Department of Computer Science and Engineering, The Hong Kong University of
Science and Technology, Hong Kong SAR, China
The rapid growth of social media has greatly influenced political discourse, highlighting the need to understand
individual political ideologies and their temporal dynamics. This task faces challenges such as data scarcity,
abundant non-political content, costly and bias-prone manual annotation, and difficulty in modeling future
ideological inclinations. To address these issues, we propose TSN4PI, a unified framework for tracking the
evolution of political ideologies on social media. It includes two core modules. The PIDN uses large language
models with style transfer and unsupervised domain adaptation to enable robust ideology detection and
filter irrelevant content from noisy, cross-domain data. The PIPN employs temporal graph neural networks
to predict future ideological shifts, enabling comprehensive analysis of ideology presence, intensity, and
evolution. We release two large-scale datasets for noncommercial research use to facilitate further work.
Extensive case studies on multiple platforms (X and Truth Social) validate the effectiveness of TSN4PI and
provide empirical insights into political polarization and the evolution of online ideologies. Our findings offer
a nuanced perspective, advancing both methodological development and empirical understanding in this field.
CCS Concepts:•Computing methodologies → Natural language processing;Graph neural networks;•
Human-centered computing→Social network analysis.
Additional Key Words and Phrases: Ideology Detection, Social Media, Natural Language Processing
ACM Reference Format:
Yijie Xu, Chao Wang, and Hui Xiong. 2026. Against Political Polarization: A Unified Framework for Tracing
Evolving Political Ideologies on Social Media.ACM Trans. Intell. Syst. Technol.1, 1 (August 2026), 35 pages.
https://doi.org/XXXXXXX.XXXXXXX
∗Corresponding authors.
Authors’ Contact Information: Yijie Xu, yxu409@connect.hkust-gz.edu.cn, Thrust of Artificial Intelligence, The Hong
Kong University of Science and Technology (Guangzhou), Guangzhou, China; Chao Wang, wangchaoai@ustc.edu.cn,
School of Artificial Intelligence and Data Science, University of Science and Technology of China, Hefei, China; Hui Xiong,
xionghui@ust.hk, Thrust of Artificial Intelligence, The Hong Kong University of Science and Technology (Guangzhou),
Guangzhou, China and Department of Computer Science and Engineering, The Hong Kong University of Science and
Technology, Hong Kong, Hong Kong SAR, China.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
©2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 2157-6912/2026/8-ART
https://doi.org/XXXXXXX.XXXXXXX
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.
arXiv:2608.17987v1  [cs.SI]  18 Aug 2026

2 Xu, et al.
@alice reshared
Democratic leader
@publicvoice
X-style post
Violence has reopened painful memories and historical trauma.
We stand with affected communities and reject hatred
in every form.
2.4k 6.1k 18.7k 186
(a)
@bob reshared
Republican leader
@civicvoice · 15 h
Truth Social-style
Current policy has weakened energy security and intensified
conflict. We will restore domestic production and pursue
strength abroad.
1.1k 4.7k 16.2k 94
(b)
Temporal interaction graph
A
B
C
D
E
F
G
t = 1
A
B
C
D
E
F
G
t = 2
(c)
Outlet ideology scores
ABC News -2.4
-6 0 +6
L LL C LR R
Lean Left
Fox News 4.0
-6 0 +6
L LL C LR R
Right
(d)
Fig. 1. Illustration of political ideology dynamics. (a)–(b) Original vector mockups of contrasting X-style and
Truth Social-style posts; identities, text, avatars, and engagement counts are illustrative. (c) Temporal graph
snapshots. (d) Original five-category scales of AllSides-derived outlet scores.
1 Introduction
Social media has reshaped political discourse, enabling individuals to express, reinforce, and
disseminate ideological views at scale [ 29]. A concern in this environment is the formation of
echo chambers and the increasing polarization of politics. These effects are particularly visible
on platforms where algorithmic curation and social clustering amplify existing biases. In the
United States, political opinions are often divided along partisan lines—commonly labeled as “left”
(Democratic) and “right” (Republican). These distinctions influence not only electoral behavior but
also patterns of engagement on digital platforms [11, 12]. This scenario underscores the importance
of examining these ideological differences, which have a significant impact on voting behavior
and social media activism. In this paper, we aim to contribute a comprehensive methodological
framework that not only elucidates these phenomena but also aids in informed policy-making for
digital political environments, thereby addressing a vital need in contemporary political discourse.
The study of political polarization and echo chambers has received increasing attention. Early
work investigated ideological clustering on blogs and Facebook [30, 64], while more recent studies
explored polarization during major political events [25]. However, the significance and mechanisms
of echo chambers remain debated [ 33]. Yet current research confronts several challenges. First,
the issue of data accessibility is prominent; platforms like Twitter impose restrictions on data
collection, leading to a scarcity of suitable datasets that align with the size and focus required
for comprehensive research. Moreover, the sheer volume of posts on these platforms presents a
significant hurdle for manual annotation, a process further complicated by annotator bias. Another
challenge is the prevalence of irrelevant content: many social media posts focus on everyday
life, lacking clear political signals, and their misclassification can lead to inaccurate predictions
of ideological leanings. Effectively filtering this noise to isolate genuine political discourse is
paramount for accurate modeling. Additionally, conventional research methods often overlook the
dynamic nature of political engagement, missing temporal variations in individual users’ political
ideologies. LLMs have shown broad text-processing capabilities [9]. Recent work includes retrieval-
utility evaluation for retrieval-augmented generation [19], test-time adaptation [86], cross-domain
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 3
sequential recommendation [84], and multimodal video and spatial reasoning [34, 48]. However,
direct in-context learning (ICL) [59] over social media data at scale [23, 53] can incur substantial
latency and performance limitations. Watermarking has also been studied for detecting the misuse
of open-source LLMs [85]. These constraints motivate a resource-efficient approach tailored to the
textual and graph structures of social media.
To address these challenges, we propose a unified framework,TSN4PI (Temporal Social Networks
for Political Ideologies), for tracing evolving political ideologies on social media. This framework
consists of two core components: the Political Ideology Detection Network (PIDN) and the Political
Ideology Prediction Network (PIPN). PIDN identifies and quantifies the intensity of political ideology
in media content. It combines LLM-based style transfer with Unsupervised Domain Adaptation
(UDA), aligning structured news (the source) with dynamic, noisy social media (the target). This
approach enhances data utility, particularly when annotated social media data is scarce. By focusing
on stylistic and semantic cues indicative of political leaning, the PIDN improves the discernment
of political ideologies amidst a high volume of irrelevant posts, effectively aiding in filtering non-
political content. Complementing the detection capabilities, PIPN leverages Temporal Graph Neural
Networks (TGNNs) to forecast the evolution of users’ ideological intensity over time. The TGNN-
based PIPN captures the dynamic nature of social media interactions and individual ideological
trajectories, enabling prediction of future inclinations. This focus on dynamic, user-level ideological
intensity distinguishes our work. While previous long-term analyses typically characterize broader
patterns of political communication at the macro level, our approach models the fine-grained,
temporal evolution of individual user ideologies. Furthermore, the graph-based nature of our model
inherently captures social interaction patterns, offering a more holistic perspective than methods
that analyze text in isolation or assume fixed ideological spectrums. Overall, TSN4PI represents a
pioneering effort in concurrently determining both the existence and intensity of political ideology
among social media users and predicting its evolution.
Our contributions in this paper are multi-fold:
• We proposeTSN4PI, a novel unified framework designed to overcome key challenges in tracing
political ideologies on social media. The framework features two integrated modules: 1) The
PIDN, which robustly detects ideology by strategically using LLMs for offline style transfer and
UDA to bridge the gap between news and noisy social media data, while effectively filtering
non-political content. 2) The PIPN, which leverages TGNNs to model and predict the evolution
of user ideologies, capturing their presence, intensity, and future trajectory.
• We contribute two novel, large-scale, publicly released datasets to the research community,
significantly addressing the challenge of data accessibility in political discourse analysis on
social media platforms. These include: 1) a comprehensive dataset of news sources with
curated political ideology scores from AllSides, and 2) a massive, user-centric corpus of nearly
77 million posts from 4,545 X (Twitter) users, spanning 16 years (2007–2022). Both datasets and
our code are released for noncommercial research use at https://github.com/yeahjack/TSN4PI.
• We conduct extensive experiments on diverse social media platforms (X and Truth Social) to
demonstrate the effectiveness and robustness of TSN4PI, validating its capability to analyze
complex political discourse and track ideological evolution in real-world settings.
Our analysis reveals compelling insights into online political behavior. Contrary to the widely
accepted echo chamber hypothesis, the users whose ideological positions move the most over time
trend predominantly toward the center rather than away from it. This challenges the often-assumed
trajectory of increasing polarization over time, highlighting instead a more dynamic and complex
landscape of online discourse that warrants empirical, data-driven investigation.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

4 Xu, et al.
2 Related Work
User-centric Political Ideology Detectionhas evolved from traditional surveys and manual
coding [1] to data-driven methods enabled by social media. Early studies used Twitter to infer
user leanings [18], whileXiao et al.introduced TIMME, a graph-based multi-relational embedding
method [83]. Despite progress, prior work often relies on small datasets [5], heuristic or manual
annotations, and single data modalities, typically text [18] or graphs [40, 83]. Many models also
model ideology as binary (left/right) or coarse labels, such as agreement/disagreement [ 50, 69],
which limits their ability to capture nuanced stances. In contrast, our TSN4PI adopts a granular
approach using floating ideological scores, integrating textual and graph-based signals to improve
prediction. We acknowledge that political ideology is inherently multidimensional, beyond a single
left-right axis. For example,Colacrai et al.[16] analyzed Reddit’s political compass, disentangling
ideology into economic (left-right) and social (libertarian-authoritarian) axes. Inspired by this, we
adopt the widely-studied one-dimensional continuum as a tractable starting point for modeling po-
larization, while recognizing multidimensional extensions as a promising direction for future work.
Our framework further supports expansion to issue-level or temporal perspectives on behavior.
Opinion Evolution and Political Dynamics on Social Mediainvolve phenomena such as echo
chambers (where users are exposed predominantly to ideologically aligned content) and political
polarization, often reinforced by platform algorithms. These dynamics are central to understanding
how public opinion forms and shifts in online environments. For example,Chen et al.[ 15] proposed
a graph-clustering method to model the evolution of public opinion topics on social media during
Pelosi’s visit to Taiwan, revealing causal transitions between topics across event stages. Other studies
focused on long-term communication patterns of political figures.Oliveira et al.[ 57] analyzed six
years of Brazilian politicians’ communications, addressing concept drift by designing classifiers to
distinguish political from non-political posts. Their findings showed that communication strategies
and public reactions varied around major events [57]. While prior work offers insights into topic-
level discourse and macro trends, our approach differs in both focus and granularity. Instead of
classifying content types or tracking broad topic shifts, we model continuous, user-level ideological
scores over time, a task methodologically related to trajectory prediction [77] and user modeling
from implicit feedback [ 76, 78, 79]. By combining semantic signals with dynamic interaction
patterns, our framework enables fine-grained tracking of individual ideological evolution.
Semantic Text Analysis for Political Ideologyhas advanced rapidly with NLP developments.
Early work employed RNNs for partisan classification [39], laying the groundwork for computa-
tional ideology detection. The advent of transformer-based models like BERT [21] enabled more
precise text representations and improved classification performance. Later variants—RoBERTa [49],
SBERT [65], BERTweet [56], and TWHIN-BERT [87]—further enhanced effectiveness on social media
data. More recently, LLMs like GPT-3 [9] have enabled zero-/few-shot political text understanding
via in-context learning. However, their direct use for large-scale, fine-grained prediction remains
limited by inference cost and stability. Our framework adopts a modular design, using an LLM not
as an end-to-end predictor but as a style transfer module. This bridges the domain gap between
structured political news and noisy social media posts, as detailed in Section 4.
Stance Detectionis a related task in NLP that involves identifying an expressed position—such as
“favor”, “against”, or “neutral”—towards a specific target [45, 54, 71]. While both stance detection
and political ideology detection analyze opinions, they differ in scope. Stance is target-specific and
often transient, reflecting an individual’s position on a particular issue [4, 45]. In contrast, political
ideology is broader and more stable, representing a cross-topic belief system that shapes multiple
stances [5]. Our work focuses on identifying and modeling this fundamental ideological attribute
over time, rather than classifying positions on specific targets.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 5
2
Fig. 2. Distribution of articles (left) and outlets (right) by political leaning, based on data from AllSides. The
bar graph shows the top 20 sources by share of total articles, colored by ideology.
3 Data
We use three datasets in this study. The first, from allsides.com, provides ideological labels for
news sources and supports cross-domain adaptation. The second and third contain social media
posts from X (formerly Twitter) and Truth Social, respectively. These platforms are used for model
training, evaluation, and cross-platform analysis of political discourse and user ideology across
distinct online communities. Privacy considerations are detailed in Appendix A.1.1.1
3.1 News Political Ideology Dataset
We construct a political ideology dataset using media bias ratings from allsides.com [ 3], which
aggregates partisan perspectives across the ideological spectrum.2 This dataset supports modeling
and transferring ideological signals across domains, based on the assumption that media affiliation
reflects consistent leanings. allsides.com applies a multi-partisan methodology, including editorial
review, blind bias surveys, third-party analysis, and community feedback. Each news source is
assigned a continuous bias score from -6 (most left) to 6 (most right), grouped into five categories:
Left([−6,− 3]),Lean Left( (−3,− 1]),Center( (−1, 1]),Lean Right( (1, 3]), andRight( (3, 6]). Using
requests and Newspaper3k [58], we retrieved rated outlets and crawled∼230,000 articles from
their main pages, covering August 3, 2017 to December 22, 2022. Each article inherits its source’s
label, yielding a large-scale, weakly supervised dataset with balanced ideological coverage. Score
preprocessing details are in Appendix A.1.2.
Preliminary Data Analysis.We conducted a preliminary analysis of the AllSides dataset to
examine its ideological distribution and linguistic characteristics. The upper part of Figure 2 shows
the proportions of news articles and media outlets across five political categories. The dataset
displays a relatively balanced Left-Right distribution, supporting class balance during model training.
The lower part of Figure 2 illustrates the share of total articles held by the top 20 news outlets.
Among them, “The Hill, ” labeled as Center, contributes the largest share. Despite a Right-leaning
1All appendices are provided in the supplementary material submitted alongside this article.
2AllSides Media Bias Ratings™by AllSides.com, used with permission under CC BY-NC 4.0.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

6 Xu, et al.
Table 1. Top 10 most frequent content words per political leaning (full text, stopwords removed).
Rank Left Lean Left Center Lean Right Right
1 trump (96,727) people (130,164) state (122,494) president (54,261) trump (60,993)
2 people (62,773) president (96,049) trump (121,089) biden (45,403) biden (50,717)
3 election (58,163) state (94,501) president (115,675) house (42,055) house (50,398)
4 republican (47,839) new (92,173) people (109,190) new (41,471) president (47,401)
5 even (47,647) trump (88,297) new (105,062) state (40,075) news (47,398)
6 president (46,673) covid (86,424) house (95,068) congress (34,186) people (40,715)
7 political (43,828) biden (79,017) year (84,825) year (28,292) new (37,368)
8 house (42,453) years (72,749) states (83,646) former (28,068) state (35,696)
9 democrats (41,652) states (72,083) senate (82,457) last (26,605) twitter (34,956)
10 republicans (38,995) election (65,009) election (82,358) committee (25,647) government (33,186)
tilt among the very largest outlets, these 20 sources span all five ideological categories. Additional
distribution details and word cloud visualizations appear in Table 1 and Figure 1 of that material.
Beyond word cloud visualizations, we conducted a frequency analysis of full article texts to
examine ideological differences in lexical usage. Table 1 lists the top 10 most frequent content words
per political leaning after stopword removal. These patterns reveal how lexical emphasis varies
across ideological contexts.Trumpis the most frequent term in both Left (96,727) and Right (60,993)
articles, indicating shared focus but likely divergent framing.Bidenalso appears frequently in Lean
Right (45,403) and Right (50,717), reflecting sustained—often critical—attention from right-leaning
outlets. An asymmetry emerges withcovid, ranked 6 th in Lean Left (86,424) but absent elsewhere,
suggesting greater pandemic focus among moderately left-leaning sources. Center-leaning con-
tent foregrounds governing bodies—state(122,494),house(95,068),senate(82,457)—indicating a
governance-oriented tone. Lean Right and Right texts instead emphasize oversight and platform
arenas, withcongress(34,186),committee(25,647), andtwitter(34,956), reflecting political critique
and media discourse. These trends support our hypothesis that bias emerges not only in topic
selection, but also in lexical framing—even when events are shared.
3.2 A User-Centric Twitter Dataset on U.S. Presidential Elections
Table 2. X Dataset Overview.
(a) Basic Statistics
Characteristic Value
Number of Users 4,545
Total Tweets 76,718,924
Avg. Tweets/User 16,880
Avg. Retweets/Tweet 20.50
Avg. Likes/Tweet 88.00
Avg. Quotes/Tweet 2.40
(b) Attributes
Field Relations Target ID Content
ID Retweets RT ID Text
Username Quotes QT ID Hashtags
Time Likes Reply ID
Conv. ID Reply User Mentions
To support research on political ideology and discourse—particularly
in the context of U.S. presidential elections—we construct a large-
scale dataset from X (formerly Twitter). Using a keyword seed
query (“presidential election”), we collected∼10,000 tweets and
identified 4,545 unique users. We then retrieved their full tweet
histories, yielding a user-centric corpus of 76,718,924 tweets from
January 1, 2007 to December 31, 2022 (Table 2a). This dataset en-
ables longitudinal analysis of political discourse and user behavior.
Table 2a summarizes dataset statistics, and Table 2b lists tweet-level
fields: tweet IDs, user metadata, timestamps, conversation IDs, en-
gagement metrics (retweets, quotes, likes), reference links (e.g.,
replies, retweets), and full text with hashtags. The dataset’s feature
richness supports detailed analysis of user activity, engagement
patterns, and content evolution. Preprocessing details appear in
Appendix A.1.3.
Comparison with Existing Datasets.Table 3 compares recent large-scale social media datasets.
While many are valuable, they vary in platform, scale, granularity, and thematic scope. For example,
Dreaddit [74] and the Reddit Corpus [36] focus on Reddit, providing post- or dialogue-level data
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 7
Table 3. Summary of Recent Social Media Datasets
Dataset Name Platform Count Users Duration Data Level Theme
Dreaddit [74] Reddit ∼190k N/A 2017–2018 Post Social media stress
Reddit Corpus [36] Reddit 727M N/A 2015–2018 Dialogue Conversational AI
Weibo-COV [37] Sina Weibo >40M 20M 2019–2020 Post COVID-19 discourse
News Feed Rank. [8] Twitter 26k 46 2021–2022 News Personalized ranking
MetaHate [62] Mixed 1.2M N/A N/A Post Hate speech detect.
IsamasRed [14] Reddit 8M N/A 2023 Dialogue Israel-Hamas discourse
Koo Dataset [52] Koo 72M 1.4M 2020–2023 Post Indian microblogging
TweetIntent Crisis [2] Twitter ∼18k 79 2022–2023 Post Russia-Ukraine narratives
SocialDrought [70] Twitter&News 1.5M N/A 2012–2023 Integrated Drought societal impact
LGBTQ+ MiSSoM [10] Reddit 27.7k N/A 2012–2021 Post LGBTQ+ stress research
AiGen-FoodRev. [27] Yelp 20k N/A N/A Post AIGC Detection
iDRAMA-Scored [60] Scored 57M 226k 2020–2023 Post Fringe communities
Unintended Offense [73] Twitter 2.4k N/A N/A Dialogue Unintentional offense
PulseReddit [35] Reddit ∼73k N/A 2024–2025 Post MAS HFT Crypto Trad.
Ours Twitter ∼77M ∼5k 2007–2022 User Presidential Election
(190k and 727M entries, respectively). Weibo-COV [37] offers 40M COVID-19-related posts from
Sina Weibo, but is also post-centric. Koo [52] (72M posts from 1.4M users) and iDRAMA-Scored [60]
(57M posts from 226k users) target Indian and fringe-platform discourse, respectively, and are
likewise post-level. Even Twitter-based datasets such as TweetIntent@Crisis [2] and News Feed
Ranking [8] involve small user bases (e.g., 79 and 46 users) and are not user-centric.
In contrast, our dataset offers full tweet histories for a fixed cohort of 4,545 users over 16 years.
This supports fine-grained, longitudinal modeling of U.S. presidential election discourse. Unlike
post-level snapshots, our dataset retains full threads and engagement, allowing for the analysis
of ideological evolution and stance shifts over time. Its scale, temporal span, and user continuity
make it uniquely suited for studying political polarization and ideology formation on social media.
Preliminary Data Analysis.To better understand the dataset’s temporal growth and topical
focus, we carried out exploratory analyses of tweet volume over time and hashtag frequency.
2007 2009 2011 2013 2015 2017 2019 2021 2023
Year
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00Count
1e6
 Number of Tweets per Month
(a) Number of tweets per month from January 2007
to September 2022.
0 50000 100000 150000 200000 250000 300000
Frequency
p2trump
news
smartnews
socialmedia
киевtopprog
ukraine
cdnpoli
usa
nowplaying
trending
whatshot
topicsgop
maga
video
tcot
gh
auspol
covid19
politics
123info
ff
resist
bcpoli
coronavirus
uk
potus
worldnews
Top 30 Hashtags
(b) Top 30 hashtags in the Twitter dataset by fre-
quency.
Fig. 3. Temporal growth and topical focus of the X (Twitter) dataset.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

8 Xu, et al.
Tweet Volume Over Time.Figure 3a shows monthly tweet counts from Jan. 2007 to Sep. 2022. The
overall trajectory is upward, with tweet activity growing steadily through late 2022 and accelerating
especially rapidly after 2018. Four peaks punctuate this trend: a modest bump during the 2012
U.S. presidential election, a more pronounced surge in 2016, a third spike during the COVID-19
outbreak in early 2020, and the largest peak surrounding the 2020 presidential election, reflecting
heightened online political activity. Afterward, tweet volume continues to rise sharply, suggesting
a sustained expansion of political engagement on the platform.
Top Hashtags.Figure 3b lists the 30 most frequent hashtags. News- and media-oriented tags, such
as #news, #smartnews, and #socialmedia, appear most prominently, underscoring Twitter’s role
as a live information channel. Excluding these politically neutral news tags, partisan motifs—#gop,
#maga, and#resist—still command a substantial share of the remaining distribution, confirming the
platform’s ideological polarity. International-politics hashtags (#ukraine, #auspol, #cdnpoli) and
global-health hashtags (#covid19, #coronavirus) are likewise present, highlighting the dataset’s
geographic breadth and its coverage of worldwide events.
3.3 Truth Social Dataset
We also incorporated a dataset from Truth Social [28], launched in February 2022 following the
January 2021 suspension of then-U.S. President Donald Trump from multiple platforms, including
Twitter (now known as X), Facebook, and others. From Figure 1 (a) and (b), Truth Social was
designed to closely mirror X in terms of functionality, with almost identical features. For instance,
X’s “Retweet” functionality is analogous to “ReTruth” on Truth Social. Supporters of Trump pre-
dominantly frequent this platform and generally exhibit a right-leaning political bias. With this
dataset, we aim to explore the dissemination of information and track the evolution of user political
ideologies within a social network that inherently carries a political bias from the outset.
Table 4. Truth Social
Dataset Overview
Field # of Records
Users 454,458
Truths 823,927
Quotes 10,508
Replies 506,276
Structurally, Truth Social bears similarities to Twitter. In contrast to
Twitter’s “Tweets, ” posts on this platform are referred to as “Truths, ”
and reposts are termed “ReTruths. ” The dataset comprises over 454,000
users and exceeds 823,000 “Truths. ” Additionally, it includes the com-
plete post history of the 65,536 most active users. Subtables within this
dataset, such as “Truths” and “Users, ” serve as primary resources for our
exploration. An overview of this dataset is presented in Table 4. Details
of data preprocessing are provided in Appendix A.1.4.
4 Methods
This section introduces our proposed framework and consists of bothPIDNandPIPNmodules.
4.1 Political Ideology Detection Network
Political ideology detection involves analyzing social media posts to determine 1) whether they are
politically relevant and, if so, 2) to what extent they align along the political spectrum. Rather than
assigning scores to all inputs indiscriminately, the task first filters out non-political content and
then estimates an ideology score for posts identified as political. Our proposed network addresses
these dual challenges through a combination of unsupervised domain adaptation (UDA), text style
transfer (TST) using LLMs, and an efficient model architecture.
While LLMs show strong ICL capabilities [9, 22], their direct use in large-scale tasks like ideology
detection faces high inference latency. Adding in-context examples lengthens the input and increases
attention computation [63, 82, 88]. LLMs can also underperform fine-tuned models on well-defined,
high-resource tasks [61], limiting their suitability for real-time or high-throughput use. We therefore
adopt a BERT-based architecture, which offers a stronger trade-off between task performance and
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 9
PIDN Political Ideology Detection Network
PIPN Political Ideology Prediction Network
1 Data Adaptation
Offline TST + Data Mix
NEWS
y = 1
LLM
TST
STYLE POSTS
y = 1
DAILY POSTS
y = 0
TARGET POSTS
unlabeled
SUPERVISED TARGET
2 PLM Encoder
Text Encoder
BERT-based PLM
Shared Weights
3 Domain-Aligned Detection
Domain Alignment + Multi-Task Heads
LABELED
UNLABELED
UDA
MMD / KL
Align Domains
C Relevance
0 1
R Ideology
ℒPIDN = αℒc + βℒr + (1 − α − β)ℒUDA
4 Cross-Level Targets
Group Posts by
User × Time
Relevance Labels
0 1 mode
Ideology Scores
mean
User-Time Targets
1 Graph Sequence
Graph Snapshots
G1 Gt−1
Directed · Weighted
Temporal Post Edges
2 TGNN Backbone
Temporal Encoder
Neighbor Sampler
Memory · Mailbox
Temporal Aggregation
Dynamic Embeddings
t − 2 t − 1 t
3 Link Pretraining
Predict Future Links
?
known query
future link? 0 1
embeddings  hn t
4 User-Level Prediction
PIDN-Derived Training Targets
R(n)t S(n)t
user
hn t
C Relevance
0 1
R
Ideology Score
ℒPIPN = λℒc + (1 − λ)ℒr
Fig. 4. The overview of our proposed framework: TSN4PI. The upper part of the figure represents the PIDN
module, while the lower part represents thePIPNmodule.
efficiency—especially in inference speed and resource usage [68]. LLMs are reserved for the offline
TST stage, where latency is less critical, rather than the core detection pipeline.
Fig. 5. Embedding across PLMs.
Building on this architectural decision, our de-
tection pipeline integrates offline LLM-based style
adaptation with an online BERT-based classifier.
Specifically, given the substantial stylistic differ-
ences between formal news articles and informal
social media posts, we apply a TST module to trans-
form news content into a style resembling that of
platforms such as X. This stylistic alignment nar-
rows the domain gap between the labeled source
domain (news) and the unlabeled target domain
(social media), thereby improving transferability.
To further bridge this gap, we incorporate UDA to
align the latent representations of political news
and unlabeled social media posts. We also augment
training with a mixture of political news articles and non-political social media content, allowing the
model to jointly learn 1) political relevance classification and 2) ideology scoring for relevant posts.
This unified approach enables robust detection in noisy, real-world social media environments,
while leveraging structured ideological signals from traditional media.
LLMs for Text Style Transfer.To bridge the stylistic gap between formal news articles and the col-
loquial nature of social media posts, we use LLMs to perform TST. This approach is especially suitable
given the absence of parallel corpora and the strong instruction-following capabilities of modern
LLMs. Specifically, for each news article 𝑛 in the source corpus 𝑁 , we generate a style-aligned
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

10 Xu, et al.
version𝑛𝑠 by prompting the LLM with: 𝑛𝑠 =LLM([prompt,𝑛]),𝑛∈𝑁. To intuitively validate
our approach, we sampled texts from three groups: the source domain (AllSides news), the target
domain (Truth Social posts), and our generated TST outputs. These were encoded using four diverse
BERT-based PLMs: bert-base-cased [21], xlm-roberta-base [49], longformer-base-4096 [6],
and twhin-bert-base [87]—and projected to 2D via UMAP [67]. As shown in Figure 5, original
news articles (blue) are widely scattered, while social media posts (orange) form a denser cluster.
Crucially, style-transferred texts (green) align closely with the target domain, reducing the distribu-
tional gap. This pattern holds across all four PLMs, supporting the effectiveness and robustness of
our TST strategy. A quantitative and comprehensive automatic evaluation follows in Section 5.2.2.
Unsupervised Domain Adaptation for Distribution Alignment.While LLM-based TST nar-
rows the stylistic gap between news and social media texts, residual distributional shifts remain.
To address this, particularly without requiring labeled social media data, we incorporate an op-
tional UDA module designed to enhance domain generalization. Our primary approach employs
Maximum Mean Discrepancy (MMD), a non-parametric measure that quantifies the divergence
between two distributions in a reproducing kernel Hilbert space (RKHS), without requiring paired
or balanced samples. Given a text sample𝑇 , we extract its embedding𝐸=𝐿(𝑇) using a PLM𝐿. Let
𝐸𝑋 and𝐸𝑌 denote embeddings from the style-transferred source and target domains, respectively.
TheMMDloss is computed as:
LMMD(𝐸𝑋,𝐸 𝑌)=
√︁
E[𝑘(𝑥,𝑥 ′)]+E[𝑘(𝑦,𝑦 ′)]−2E[𝑘(𝑥,𝑦)],(1)
where𝑘(𝑥,𝑦)=exp −∥𝑥−𝑦∥ 2/2𝜎2 is the Gaussian RBF kernel, and𝑥,𝑥′∈𝐸 𝑋 ,𝑦,𝑦′∈𝐸 𝑌 . This
kernel maps samples into a space where their similarity can be effectively measured and optimized.
In addition toMMD, we also consider Kullback-Leibler (KL) divergence as an alternative distri-
bution alignment method.KLdivergence is particularly effective when model outputs can be inter-
preted as probability distributions—such as softmax scores or normalized embeddings—allowing
explicit alignment of posterior distributions between domains. Given source domain prediction𝑃
and target domain prediction𝑄, theKLloss is computed as:
LKL(𝑃∥𝑄)=
∑︁
𝑖
𝑃(𝑖)log 𝑃(𝑖) 𝑄(𝑖) .(2)
Compared toMMD,KLdivergence assumes stronger alignment in probability space and is more
suitable when output distributions are well-calibrated. We evaluate both metrics to assess robustness
under varying domain conditions. To incorporate domain adaptation during training, we define a
composite loss that jointly optimizes task performance and representation alignment:
LPIDN =𝛼L 𝑐+𝛽L 𝑟+(1−𝛼−𝛽)L UDA,(3)
whereL𝑐 andL𝑟 are the political-relevance classification and ideology-regression losses, respec-
tively;LUDA∈{L MMD,L KL} is the selected domain-alignment loss; and𝛼,𝛽≥ 0with 𝛼+𝛽≤ 1
control their relative contributions. When UDA is disabled in an ablation, theLUDA term is omitted.
By aligning embedding distributions across domains, the UDA module enhances generalization to
informal, unlabeled social media content while preserving task-specific learning. A comprehensive
complexity analysis of the UDA module is provided in Appendix A.4.
4.2 Political Ideology Prediction Network
Political ideology prediction models how users’ stances evolve over time—a task fundamentally
different from static detection due to the absence of future posts. Traditional post-level embedding
methods are thus inapplicable. We adopt Temporal Graph Neural Networks (TGNNs), which
are well-suited for ideological forecasting. This choice is motivated by two factors: social media
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 11
platforms naturally produce dynamic user interaction graphs, and TGNNs are designed to model
temporal dependencies in such evolving structures.
Temporal Graph Construction.We construct a dynamic, directed, and weighted graph 𝐺=
(𝑉,𝐸,𝑡) , where𝑉 denotes users,𝐸 represents interactions, and𝑡 is the timestamp associated with
each edge. Each post is modeled as a temporal edge whose features are derived from PLM-based
text embeddings. If user𝐴 re-posts content from user𝐵, we introduce a directed edge from𝐴 to𝐵,
weighted by the frequency of such reposts within a defined time window. Self-loop edges from𝐴
to𝐴 represent original posts, capturing the user’s individual content generation. This construction
encodes both interpersonal influence and independent ideological expression. To capture temporal
evolution, we partition the graph chronologically into a sequence of snapshots 𝐺1,𝐺 2,...,𝐺 𝑡−1 ,
and train models to predict ideological properties in the future snapshot𝐺𝑡. This forward-looking
setup mirrors real-world forecasting scenarios, where a user’s historical activity (e.g., during years
1-5) informs predictions about their future ideological stance (e.g., in year 6).
Temporal Graph Modeling.To capture spatio-temporal dynamics, we evaluate three TGNN
models: JODIE, APAN, and TGN.JODIE[46] uses coupled RNNs to update user and item embeddings
from interactions. A projection operator estimates future user embeddings via time-conditioned
scaling:
ˆu(𝑡+Δ𝑡)=(1+w Δ𝑡)⊙u(𝑡),(4)
wherew Δ𝑡 encodes the elapsed-time context.
APAN[ 81] uses asynchronous updates with an attention-based encoder. Upon interaction, it
updates the embedding based on the last state and a “mailbox” storing recent neighbor interactions:
z(𝑡)=MLP(LayerNorm(MultiHead(z(𝑡 −),M(𝑡))+z(𝑡 −))).(5)
TGN[ 66] maintains time-evolving memory states. Upon interaction between nodes𝑖 and 𝑗, it
generates a message:
m𝑖(𝑡)=msg(s 𝑖(𝑡−),s 𝑗(𝑡−),Δ𝑡,e 𝑖 𝑗(𝑡)),(6)
which updates memory via:s 𝑖(𝑡)=mem( m𝑖(𝑡), s𝑖(𝑡−)) . Final node embeddingsz 𝑖(𝑡) are computed
using temporal attention over neighbors.
Self-Supervised Link Prediction.As a self-supervised representation-learning stage, temporal
link prediction first trains the TGNN to learn node representations by forecasting future edges ˆ𝐸′
from historical graph sequences. For a candidate node pair(𝑢,𝑣), the link score is computed as:
𝑠(𝑢,𝑣)=𝜎 h⊤ 𝑢 Wh𝑣 ,(7)
whereh 𝑢 andh 𝑣 are time-specific embeddings,Wis a learnable projection matrix, and 𝜎(·) denotes
the sigmoid function. This stage produces temporally contextualized node embeddingsh 𝑡 𝑛, which
are then used by the downstream ideology-prediction heads.
Node Classification and Regression.To predict users’ future political ideologies, we attach
classification and regression heads to temporal node embeddingsh 𝑡 𝑛 learned via TGNN. PIDN-
derived targets are aggregated from each user’s historical posts up to time𝑡. Let𝑃𝑛,𝑡 denote this
post set, and let ˆ𝑟𝑝 and ˆ𝑠𝑝 denote the PIDN-derived relevance label and ideology score for post𝑝,
respectively. Political relevance𝑅(𝑛) 𝑡 is defined as the majority post-level relevance label:
𝑅(𝑛) 𝑡 =mode{ ˆ𝑟𝑝 :𝑝∈𝑃 𝑛,𝑡},(8)
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

12 Xu, et al.
and, for relevant users (𝑅(𝑛) 𝑡 = 1), let𝑃+ 𝑛,𝑡 ={𝑝∈𝑃 𝑛,𝑡 : ˆ𝑟𝑝 = 1}. Their ideology target is the mean
PIDN score over relevant posts:
𝑆(𝑛) 𝑡 = 1 |𝑃+ 𝑛,𝑡| ∑︁ 𝑝∈𝑃+ 𝑛,𝑡 ˆ𝑠𝑝.(9)
To jointly optimize both tasks, we define a unified loss:
LPIPN =𝜆L 𝑐+(1−𝜆)L 𝑟,(10)
where𝜆∈[ 0, 1] balances classification and regression. This multi-task setup guides the model to
learn temporally grounded node representations that capture ideological relevance and intensity.
5 Experiments
This section introduces the experiments conducted to validate the framework’s efficacy in detecting
and predicting political ideologies. We first outline the experimental setup, including datasets,
baselines, and implementation details. We then present a detailed evaluation of the PIDN, followed
by an analysis of thePIPN. Implementation details are provided in Appendix A.2.
5.1 Experimental Setup
5.1.1 Datasets and Data Preparation.
Training Data Construction for PIDN.The PIDN module is trained on a hybrid dataset of
politically relevant and irrelevant content. Relevant samples are derived from style-transferred news
articles with annotated ideology scores and are labeled according to their political relevance. To
balance the data, we include an equal number of daily-life tweets from our Twitter corpus, labeled as
politically irrelevant (relevance 0), with a placeholder ideology score that is excluded from the regres-
sion objective. To enhance domain adaptation, we add non-political tweets from the MajidTweets
dataset [51], a large-scale corpus of real-world tweets. These are selected to be disjoint from our Twit-
ter corpus, introducing broader linguistic and stylistic diversity. Importantly, the PIDN regression
head is only activated for posts classified as politically relevant, ensuring that ideology scores are
not assigned to irrelevant content. We also normalized target scores before training and evaluation.
Graph Construction for PIPN.The experiments for the PIPN module are conducted on two
datasets: Truth Social and our large-scale X (Twitter) corpus. The temporal graphs for TGNNs
were constructed using posts identified as “Politically Relevant” and subsequently scored by our
PIDN-KLmodel. For the static GNN baselines, we aggregate all temporal interactions into a single,
weighted static graph for each dataset. This setup intentionally discards temporal information,
allowing us to directly quantify the performance gains attributable to modeling temporal dynamics.
5.1.2 Models, Baselines, and Evaluation Metrics.
Political Ideology Detection ( PIDN).Our evaluation involves: 1) PLM backbone selection, 2)
hyperparameter tuning, and 3) ablation of TST and UDA components. We benchmark PIDN against
the Qwen2.5 model family [72], spanning 0.5B to 72B parameters, in both zero-shot and few-shot
ICL settings. Our analysis encompasses the full suite of Qwen2.5 models under a zero-shot set-
ting, as well as Qwen2.5-7B with varying numbers of ICL shots, given its widespread use and
strong representativeness. All ICL experiments are conducted on 1,000 randomly sampled test
instances, repeated five times to ensure robustness. Evaluation metrics include classification per-
formance—reported as F1 scores for both political/non-political classes and macro-average—as well
as class-specific precision and recall for the political class. Regression performance is assessed via
Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), with results summarized in
Table 5. Inference latency (in milliseconds) is reported in Figure 6. A comprehensive summary of
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 13
Table 5. Unified performance analysis of the Qwen2.5 model family.Top:cross-model scaling analysis in a
zero-shot setting.Bottom:few-shot analysis for the Qwen2.5-7B-Instruct model. Within each block,bold
marks the best and underlining the second best per metric.
Classification (F1↑) Political Class Detail↑Regression Error↓
Model / Setting Non-political Political Macro Avg. Precision Recall MAE RMSE
Cross-Model Scaling (0-shot)
Qwen2.5-0.5B-Instruct 0.510±0.022 0.727±0.007 0.618±0.014 0.601±0.007 0.918±0.006 0.413±0.007 0.478±0.005
Qwen2.5-3B-Instruct 0.946±0.003 0.943±0.003 0.945±0.003 0.945±0.008 0.942±0.006 0.283±0.005 0.333±0.005
Qwen2.5-7B-Instruct 0.927±0.002 0.905±0.003 0.916±0.002 0.992±0.003 0.833±0.004 0.238±0.004 0.288±0.005
Qwen2.5-14B-Instruct 0.918±0.003 0.900±0.004 0.909±0.003 0.986±0.001 0.827±0.006 0.227±0.004 0.285±0.003
Qwen2.5-32B-Instruct 0.946±0.001 0.937±0.002 0.942±0.002 0.991±0.001 0.889±0.004 0.225±0.002 0.283±0.001
Qwen2.5-72B-Instruct 0.955±0.002 0.950±0.003 0.953±0.002 0.994±0.002 0.910±0.004 0.216±0.004 0.275±0.004
Few-Shot forQwen2.5-7B-Instruct
0-shot 0.927±0.002 0.905±0.003 0.916±0.002 0.992±0.003 0.833±0.004 0.238±0.004 0.288±0.005
2-shot 0.936±0.021 0.928±0.026 0.932±0.024 0.986±0.005 0.879±0.049 0.242±0.005 0.292±0.007
4-shot 0.920±0.032 0.905±0.044 0.912±0.038 0.986±0.006 0.840±0.079 0.230±0.007 0.282±0.012
6-shot 0.918±0.024 0.903±0.035 0.911±0.030 0.987±0.008 0.835±0.063 0.243±0.007 0.301±0.007
8-shot 0.906±0.024 0.886±0.035 0.896±0.029 0.990±0.007 0.804±0.061 0.246±0.007 0.305±0.011
10-shot 0.898±0.019 0.874±0.028 0.886±0.024 0.995±0.002 0.781±0.047 0.236±0.012 0.291±0.015
20-shot 0.923±0.031 0.908±0.043 0.916±0.037 0.995±0.002 0.838±0.074 0.244±0.016 0.306±0.019
50-shot 0.961±0.014 0.958±0.015 0.960±0.014 0.996±0.003 0.924±0.031 0.241±0.018 0.304±0.020
100-shot 0.964±0.008 0.962±0.009 0.963±0.009 0.998±0.000 0.929±0.017 0.237±0.010 0.307±0.012
200-shot 0.974±0.008 0.973±0.008 0.973±0.008 0.998±0.002 0.950±0.017 0.243±0.012 0.315±0.018
all performance metrics across models appears in Tables 6 and 7 of that material. To evaluate the
TST module, we adopt two forms of automated assessment. First, we compute semantic similarity
between original and style-transferred texts using cosine similarity over sentence embeddings.
Second, we apply anLLM-as-a-Judgeframework to score outputs based on style appropriateness
and semantic preservation. All scores are normalized to the[0,1]range for consistency.
Political Ideology Prediction ( PIPN).For the PIPN module, we employ TGNNs as the backbone,
which are specifically designed to capture the temporal evolution of interactions within dynamic
networks. Given that our datasets model user interactions over time, TGNNs are inherently more
suitable for our research objectives. The temporal pipeline is evaluated in two successive stages:
1) self-supervised link prediction, which forecasts future user interactions to learn temporal user
embeddings; and 2) downstream political ideology prediction, which combines node classification
(determining whether a user’s posts are political) and node regression (quantifying the user’s
ideological score). We conducted a comparative study of three representative TGNNs: TGN [66],
JODIE [46], and APAN [81]. We also establish two strong static GNN baselines, GCN [ 44] and
GAT [75], to validate the necessity of a temporal approach. Performance is measured using average
precision (AP) and area under the curve (AUC) for link prediction, and accuracy and MSE for
political ideology prediction. The static baselines (GCN, GAT) are trained end-to-end directly on
the ideology prediction task, as they do not inherently perform temporal link prediction.
5.2 Evaluation of the Political Ideology Detection Network (PIDN)
This section presents an evaluation of PIDN, focusing on its performance and efficiency compared
to LLMs, followed by a detailed component analysis and an ablation study.
5.2.1Performance and Efficiency vs. Large Language Models.
Performance Analysis.To comprehensively evaluate the effectiveness of our model, we first
compared our fine-tuned PIDN against the Qwen2.5 model family (Table 5). For few-shot ICL, each
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

14 Xu, et al.
PIDN(
0.3B) ≈ 0.5B 1.5B 3B 7B 14B 32B 72B
Number of Parameters (B)
0
200
400
600
800
1000
1200Average Latency (ms)
4.39
92.90
142.07
215.49
340.73
407.58
697.71
1145.71
0-shot Latency Comparison
340
341
342
343
344
345
340.73
341.34341.45 341.48
342.29
Latency vs. Shots: PIDN vs Qwen2.5-7B
Qwen2.5-7B
0 2 4 6 8 10
Number of Shots (X-shot ICL)
0
5
10
4.39
PIDN
Fig. 6. Inference latency comparison. Left: 0-shot latency of PIDN (≈0.3B) vs. LLMs of varying sizes. Right:
Latency of PIDN vs. Qwen2.5-7B with increasing ICL shots (0–10). Latencies are reported in milliseconds (ms).
setting was rigorously repeated five times using randomly drawn, class-balanced examples from a
held-out pool. Our primary benchmark, PIDN, achieved a near-perfect classification accuracy of
99.25% and an impressively low regression MSE of 0.0048—an RMSE of 0.069 (Table 7), demonstrating
high precision and fine-grained scoring capability.
Cross-model scaling analysis reveals a generally positive, albeit complex and nuanced, trend
in zero-shot LLM performance. The largest model, Qwen2.5-72B-Instruct, achieves the highest
Macro F1-score of 0.953, establishing it as the top performer. However, the trend is not strictly
monotonic, as mid-sized models (7B to 32B) exhibit a strong bias towards precision over recall. They
reach near-perfect precision (up to 0.992) but at the cost of lower recall (down to 0.827), reflecting
conservative decision boundaries that minimize false positives. For regression, scaling yields more
consistent gains; yet, the best LLM’s RMSE of 0.275 is still nearly four times worse than PIDN ’s
0.069, underscoring the limits of prompting without task-specific tuning.
The few-shot performance of Qwen2.5-7B-Instruct further illustrates these stark limitations.
We observe a surprising “performance trough”: after an initial gain at 2 shots, adding more demon-
strations (specifically, 4–10 shots) unexpectedly degrades classification performance, with the
F1-score dropping below the zero-shot baseline of 0.916. A consistent improvement over the base-
line requires 50 shots or more, which partially corrects the earlier conservative bias by improving
recall. Even at its best—a Macro F1 of 0.973 at 200 shots, and a lowest RMSE of 0.282 at 4 shots—ICL
still falls well short of our fine-tuned PIDN. This significant gap stems from core methodological
differences, as PIDN is explicitly fine-tuned on a large, domain-specific dataset with ideological
supervision. This allows it to learn nuanced signals that generic few-shot prompting cannot capture,
highlighting the clear superiority of task-specific tuning for precise sociopolitical inference.
Latency Analysis.To complement the performance evaluation, we conducted a comparative
latency analysis to validate the efficiency of our architectural design. We benchmarked our PIDN,
built on the twhin-bert-base backbone (≈0.3B parameters), against the same Qwen2.5 LLM
baselines. Latency is a known limitation of LLMs, especially with larger models or in-context
examples. Figure 6 presents the latency comparison. Our PIDN achieves a low inference latency of
4.39 ms. In the left panel, even the smallest Qwen2.5 model (0.5B) exhibits a 0-shot latency of 92.90
ms—over 21× slower than PIDN. Latency increases sharply with model size, reaching 1145.71 ms for
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 15
Table 6. Comparison of PLM backbones and hyperparameter tuning results. Best values are inbold.
(a) Backbone Comparison
Model Acc. (Kind) (%)↑MSE (Score)↓
bert-base-cased[21] 95.56±0.21 0.0847±0.0015
xlm-roberta-base[17] 96.67±0.15 0.0686±0.0011
covid-twitter-bert-v2[55] 95.53±0.25 0.0874±0.0018
twhin-bert-base[87] 97.79±0.12 0.0606±0.0008
(b) Hyperparameter Tuning
Hyperparameters Performance Metrics
𝛼 𝛽 Acc. (%)↑ MSE↓
0.4 0.4 97.12±0.18 0.073±0.002
0.3 0.3 96.98±0.20 0.071±0.002
0.4 0.3 97.79±0.15 0.067±0.001
0.3 0.4 97.52±0.17 0.069±0.002
the 72B variant, which is more than 260 times slower. The right panel shows the impact of increasing
ICL shots on the 7B model. While latency rises only slightly from 340.73 ms (0-shot) to 342.29 ms
(10-shot), it remains consistently high—about 78×slower thanPIDN, even under minimal ICL.
Discussion on Model Architecture.Our evaluation challenges the common assumption that
there is a trade-off between the efficiency of task-specific models and the performance of LLMs. In
high-resource settings, our fine-tuned PIDN significantly outperforms LLMs—delivering higher ac-
curacy with orders of magnitude lower inference latency. Even the best ICL setups incur prohibitive
computational costs, making LLMs unsuitable for real-time or large-scale deployment. While PIDN
is the clear choice when labeled data is abundant and performance critical, LLMs remain useful in
low-resource scenarios where annotation is infeasible. Their zero- and few-shot capabilities offer a
practical fallback. Nonetheless, our results strongly support the development of lightweight, special-
ized models in settings where scalability, precision, and efficiency are most critical. These findings
support a broader insight: when conditions allow, architectural specialization often outperforms
general-purpose flexibility in real-world analytical tasks.
5.2.2 Component Analysis and Ablation Studies.
Backbone Selection.We began by evaluating four prominent PLM backbones to identify the most
suitable encoder for our task. To isolate the backbone’s inherent capacity, this comparison excluded
both TST and UDA. We used a fixed hyperparameter setting (𝛼= 0.4,𝛽= 0.2) for all models, with
standard deviations from 5 runs. As shown in Table 6a,twhin-bert-base achieved the best results
for both political relevance classification (97.79% accuracy) and ideology score regression (0.0606
MSE). This performance underscores the benefit of pre-training on large-scale social media data with
user- and network-aware objectives. In contrast, although covid-twitter-bert-v2 is also social
media-oriented, its domain specificity toward COVID-19 limited its effectiveness in capturing the
broader political discourse. Interestingly, all models yield comparably high classification accuracy,
suggesting that identifying whether a tweet expresses political relevance is a relatively easy task
for PLMs. In other words, classifying the presence of political inclination poses little challenge to
Table 7. Ablation study of TST and UDA methods. All experiments use the twhin-bert-base backbone and
the selected hyperparameter setting (𝛼=0.4,𝛽=0.3). Best performance is inbold.
Configuration Acc. (Kind) (%)↑MSE (Score)↓
Backbone Only 97.79±0.15 0.0670±0.0012
Backbone + UDA (KL) 98.15±0.11 0.0350±0.0009
Backbone + UDA (MMD) 98.35±0.10 0.0320±0.0010
Backbone + TST 99.12±0.08 0.0060±0.0004
Backbone + TST + UDA (KL) (PIDN-KL) 99.25±0.07 0.0048±0.0003
Backbone + TST + UDA (MMD) (PIDN-MMD) 99.52±0.05 0.0057±0.0004
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

16 Xu, et al.
modern language models, with minimal variation in performance across different backbones. In
conclusion, we adoptedtwhin-bert-baseas the backbone for all subsequent experiments.
Hyperparameter Tuning.Next, we fine-tuned the hyperparameters 𝛼 and𝛽, which weight the
three terms of the PIDN objective𝛼L 𝑐+𝛽L 𝑟+( 1−𝛼−𝛽)L UDA (classification, regression, and
domain alignment; see Figure 4), using our selected twhin-bert-base backbone, again without
engaging TST or UDA. Table 6b reports the four configurations evaluated in this dedicated tuning
stage. Among these settings, 𝛼= 0.4and 𝛽= 0.3achieved the highest classification accuracy
(97.79%) and the lowest MSE (0.067), and we therefore selected this setting for the subsequent
ablation study. The(𝛼= 0.4,𝛽= 0.2) setting in Table 6a was used only to hold the loss weights fixed
during the preliminary backbone comparison and was not part of this tuning grid. Accordingly, we
do not claim a global optimum across the two stages. The limited variation within the Table 6b grid
suggests that the framework is not highly sensitive to these loss weights.
Ablation Study.To rigorously evaluate the individual and synergistic contributions of our
core components, we conducted a detailed ablation study. Starting with the twhin-bert-base
backbone and the selected hyperparameter setting (𝛼= 0.4,𝛽= 0.3), we incrementally added TST
and the two UDA methods: Kullback-Leibler (KL) divergence and Maximum Mean Discrepancy
(MMD). The comprehensive results are presented in Table 7. The most dramatic improvement
stems from TST. By adding TST to the backbone, the regression MSE plummets from 0.0670 to
0.0060—an order-of-magnitude reduction. This starkly demonstrates that bridging the stylistic
gap via LLM-based data augmentation is the single most critical factor for achieving high-fidelity
ideological scoring. UDA also yields significant gains. When applied directly to the backbone, MMD
reduces the MSE by over 50% to 0.032, while KL achieves a comparable reduction to 0.035. When
combined with TST, both full models deliver the best results among the evaluated configurations.
The PIDN-MMDmodel achieves the highest classification accuracy at 99.52%, while the PIDN-KL
model secures a marginally better regression performance with the lowest MSE of 0.0048. Given
that both models demonstrate highly competitive and nearly equivalent performance, the deciding
factor shifts to a practical consideration: computational efficiency. As detailed in Appendix A.4,
there is a stark contrast in the overhead of the two UDA methods. MMD’s quadratic time complexity
(𝑂(𝑁 2𝐷) ) makes it compute-bound, limiting its scalability with increasing batch size. In contrast, KL
divergence’s linear complexity (𝑂(𝑁𝐷) ) makes it significantly more efficient and scalable, posing
no practical constraints on large-batch training. Combining top-tier performance with superior
computational efficiency, we therefore identifyPIDN-KLas our selected configuration.
0.0 0.2 0.4 0.6 0.8 1.0
Similarity Score
0.00
0.25
0.50
0.75Proportion
bge-m3
0.0 0.2 0.4 0.6 0.8 1.0
Similarity Score
Linq-Embed-Mistral
0.0 0.2 0.4 0.6 0.8 1.0
Similarity Score
multilingual-e5-instruct
0.0 0.2 0.4 0.6 0.8 1.0
Similarity Score
all-MiniLM-L6-v2
0.0 0.2 0.4 0.6 0.8 1.0
Style Score
0.00
0.25
0.50
0.75Proportion
Style (DeepSeek)
0.0 0.2 0.4 0.6 0.8 1.0
Semantic Score
Semantic (DeepSeek)
0.0 0.2 0.4 0.6 0.8 1.0
Style Score
Style (OpenAI)
0.0 0.2 0.4 0.6 0.8 1.0
Semantic Score
Semantic (OpenAI)
Scores between news and tweet-style transferred text
Fig. 7. Evaluation of Text Style Transfer. Top: Histograms of similarity scores between original news and tweet-
style outputs, computed using four sentence embedding models. Bottom: Histograms of Style Appropriateness
and Semantic Preservation scores (normalized to 0–1) assigned by LLM judges.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 17
Validation of the TST Module.To rigorously assess the contribution and quality of our LLM-
based TST module, we conducted a multifaceted evaluation. The goal is to verify that TST effectively
adapts formal news into tweet-style social media text while preserving semantic meaning, which is
crucial for downstream ideology analysis. The evaluation comprises two complementary compo-
nents: Semantic Similarity Analysis andLLM-as-a-JudgeEvaluation.
• For Semantic Similarity Analysis, to ensure robustness and reduce model bias, we employed
four diverse embedding models: bge-m3 [13], Linq-Embed-Mistral [43], multilingual-e5
-large-instruct [80], and all-MiniLM-L6-v23. These span multiple architectures (e.g.,
MiniLM, XLM-R, Mistral, BGE) and sizes (22M–7.1B), providing an architecture-agnostic
similarity estimate. High scores across models suggest strong semantic preservation.
• For theLLM-as-a-JudgeEvaluation, we employed DeepSeek-V3 [20] and GPT-4o [38] as auto-
mated evaluators [32, 89] to score outputs onStyle AppropriatenessandSemantic Preservation,
complementing embedding-based metrics.
Figure 7 summarizes the TST evaluation results. The top row shows cosine similarity distribu-
tions across four embedding models. bge-m3 and all-MiniLM-L6-v2 concentrate in the 0.6–0.9
range, indicating solid semantic alignment. Linq-Embed-Mistral yields a similar pattern, slightly
skewed lower. Notably,multilingual-e5-instruct peaks near 0.9, suggesting strong semantic
consistency. Overall, the results indicate good to excellent semantic preservation. The bottom row
shows LLM-based scores. ForStyle Appropriateness, both DeepSeek-V3 and GPT-4o peak around
0.9, confirming alignment with tweet-style norms. ForSemantic Preservation, DeepSeek-V3 yields
scores tightly clustered near 0.9–1.0; GPT-4o peaks more broadly around 0.7–0.8, still indicating
strong fidelity. In summary, both embedding- and LLM-based evaluations confirm that our TST
module produces tweet-style outputs with preserved meaning. This validates the PIDN pipeline
and ensures downstream tasks operate on stylistically consistent, semantically faithful inputs.
Bias Analysis and Mitigation.Although the TST module is effective, LLM-based style transfer
may still bias the data if political cues are shifted unevenly across ideology groups or platforms [26].
We focus on three risks:ideology drift, where stance-bearing markers are amplified or softened
more for one side;lexical homogenization, where frequent social-media tokens replace minority or
platform-specific expressions and reduce linguistic variety for TGNNs; andsource leakage, where
platform–ideology correlations from pretraining are copied into transferred texts.
We mitigate these effects in three ways. First, we constrain the TST prompt to retain stance
phrases and entity mentions, and to modify only surface style (e.g., emojis, contractions, tweet for-
matting). Second, we perform post-hoc filtering and balancing: pairs with good style but noticeably
lower semantic scores from the LLM judges are discarded or regenerated, and PIPN batches are
balanced across labels and platforms to prevent artefacts from concentrating in one class. This ap-
proach aligns with methods for mitigating task-specific biases [7]. Third, the evaluation setup itself
acts as a safeguard: using four sentence embedding models and two independent LLM-as-a-judge
evaluators (DeepSeek-V3 and GPT-4o) lowers reliance on any single model, and their agreement
indicates that the TST step preserves meaning without systematic distortion.
5.3 Evaluation of the Political Ideology Prediction Network (PIPN)
This section evaluates the PIPN module by comparing the evaluated TGNNs with static GNN
baselines on link prediction and political ideology prediction.
Model Comparison and Analysis.Table 8 presents the results of our comparative analysis.
Findings reveal distinct strengths across models, establishing the advantage of temporal modeling.
3https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

18 Xu, et al.
Table 8. Comparative results of static ( ✗) and temporal (✓) models. The evaluation covers Link Prediction
(AP, AUC) and Ideology Prediction (Accuracy, MSE). Best performance for each metric is inbold; second best
is underlined. Static models are not applicable (N/A) for the link prediction task.
Dataset Model Temporal Link Prediction Ideology Prediction
AP(%)↑AUC(%)↑Acc.(%)↑MSE↓
Truth Social
GCN [44]✗N/A N/A 58.35±0.850.045±0.002
GAT [75] ✗ N/A N/A 61.81±0.72 0.043±0.002
TGN [66]✓99.25±0.08 99.14±0.09 72.42±0.350.036±0.001
JODIE [46] ✓ 99.73±0.04 99.69±0.05 66.28±0.41 0.039±0.001
APAN [81]✓97.56±0.1597.24±0.1865.14±0.450.036±0.001
X (Twitter)
GCN✗N/A N/A 96.85±0.220.0793±0.0015
GAT ✗ N/A N/A 95.89±0.28 0.0629±0.0011
TGN✓98.82±0.0598.70±0.0699.99±0.010.0560±0.0002
JODIE ✓ 97.83±0.09 97.72±0.10 99.98±0.01 0.0564±0.0003
APAN✓98.78±0.06 98.65±0.07 99.98±0.01 0.0564±0.0004
On theTruth Social dataset, the results reveal a performance trade-off among TGNNs. JODIE
achieves the best link-prediction performance among the evaluated models (99.73% AP and 99.69%
AUC). However, TGN demonstrates significantly better performance on the critical task of ideol-
ogy classification, achieving the highest accuracy (72.42%), and it ties with APAN for the lowest
regression MSE (0.036). In stark contrast, the static baselines underperform substantially. GAT, the
stronger of the two, achieves only 61.81% accuracy, lagging behind TGN by over 10 percentage
points. This considerable performance gap underscores the need for temporal modeling to capture
the evolving patterns of ideological expression on this platform.
On theX (Twitter) dataset, TGN consistently outperforms all other models. Here, the advantage
of temporal modeling becomes even more pronounced. The static GCN and GAT models reach
accuracies of 96.85% and 95.89%, respectively—substantially lower than those of the TGNNs (all
exceeding 99.9%). Moreover, the regression performance of the static models is inferior, with MSEs
of 0.0793 (GCN) and 0.0629 (GAT), both considerably higher than TGN’s top-performing 0.0560. We
attribute the performance gap to the dataset’s extensive 16-year span and high interaction density,
which allows temporal models to learn evolving ideological trajectories that are inherently lost
in the time-aggregated graphs used by static models. This demonstrates that omitting temporal
information results in a loss of classification fidelity even with strong topical signals.
This decision is further solidified by the substantial performance gap exhibited by the static
GCN and GAT baselines. Their inability to match the performance of temporal models on our core
tasks underscores that a temporal modeling approach is not merely advantageous but essential for
accurately predicting political ideology in dynamic networks.
6 Results and Findings
This section integrates experimental results to derive novel observations in social media platforms.
6.1 A Validated Framework for Ideology Detection and Prediction
Our study validates an integrated two-stage framework for analyzing political ideology on social
media. In Stage I, the NLP-based PIDN transforms raw textual content into reliable ideological anno-
tations. Building on this foundation, Stage II employs the TGNN-basedPIPN to capture the temporal
evolution of user interactions and ideological structure dynamics. Together, these components
form a robust bridge between micro-level textual expression and macro-level network dynamics.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 19
1.00− 0.75− 0.50− 0.25− 0.00 0.25 0.50 0.75 1.00
Political Ideology Score
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6Number of Posts
1e7 T witter
1.00− 0.75− 0.50− 0.25− 0.00 0.25 0.50 0.75 1.00
Political Ideology Score
0
5000
10000
15000
20000
25000
30000Number of Posts
TruthSocial
Distributions of Political Ideology Scores in Different Platforms
(a)
2010 2012 2014 2016 2018 2020 2022
Year
0.3
0.4
0.5
0.6
0.7Mean Predicted Political Score
Ideological Trajectories of Top 20 Volatile Users
Initial Ideology
Left
Center
Right (b)
Fig. 8. Ideological structure and temporal dynamics across platforms. (a) shows how users on the two
platforms are distributed along the left–right scale, which reflects cross-platform differences in baseline
audience composition. (b) tracks how highly unstable users move on the same scale over time.
6.2 Findings about Echo Chambers and Political Polarization
We conducted data visualization of social media post content across different levels and objectives.
Our goal was to identify shifts in political ideology across social media platforms and explore
insights into echo chambers and political polarization.
Different Social Media Platforms exhibit distinct overarching Political Ideologies.We used
PIDN to map each platform’s ideological landscape. As illustrated in Figure 8a, despite differences
in dataset size, the ideological distributions align with prevailing public perceptions: Twitter
exhibits a modest leftward tilt, while Truth Social skews markedly to the right. Twitter, as a
widely used mainstream platform, draws from an internet-active American population that tends
to lean slightly left. In contrast, Truth Social—founded by former U.S. President Donald J. Trump, a
Republican—naturally attracts a predominantly conservative user base. We further hypothesize that
the pronounced rightward shift on Truth Social stems from a combination of factors: the platform’s
appeal to influential right-wing figures and its broader user community, which may already possess
a mild conservative orientation.
Ideological trajectories of highly volatile users on Twitter do not support the echo cham-
ber or polarization hypothesis.To further examine the dynamics of ideological transformation
at the individual level, we identified the top 20 users in the X (Twitter) dataset with the largest
spread between their highest and lowest yearly mean ideology scores. To ensure robust estimation,
we restricted the analysis to users who posted at least 10 tweets per year and a minimum of 50
tweets in total during the observation period. Each user was assigned an initial political leaning
(Left, Center, or Right) based on the mean ideology score in their earliest available year. As shown
in Figure 8b, we then visualized each user’s ideological trajectory over time, with colors denoting
their initial political stance. We used the Twitter dataset for its broader time span; Truth Social was
excluded because its data covers only 2022, too short for the long-term shifts central to this inquiry.
Contrary to the classical “echo chamber” hypothesis—which posits that users tend to reinforce
and radicalize their pre-existing beliefs—we observed complex and multidirectional shifts. Many
initially right-leaning users trended towards the ideological center, with several even crossing
the midpoint into left-leaning territory over time. This pattern suggests a form of ideological
moderation or de-radicalization, rather than an amplification of partisan viewpoints. Meanwhile,
the few users in our sample who were initially left-leaning also failed to show a consistent pattern
of leftward polarization. One such user, despite significant fluctuations, ultimately returned to an
ideological position near their starting point, while another exhibited a clear trajectory toward
the right. Most strikingly, users classified as centrist did not remain stable but instead exhibited
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

20 Xu, et al.
Table 9. Case study of three Twitter users illustrating non-polarizing trajectories within the U.S. political
context. For each user, representative tweets are shown from two distinct periods. Key phrases arebolded.
User Year Representative tweet (truncated) Score
1
2009
Is there such a thing as a“Lie Factory”? If so, its obviousright-wing Republicans& their talking heads hold a great deal of stock in it. 0.073
3 days left.Vote 4 my rescue group 2 save lives! Retweet! 0.369
2022
As you know, currently theprice per barrel of oil is $120. In this chart, note how low the price has to be for corps to profit by drilling.
It’s the greed.
0.515
Next time a [Republican] points out that more have died from Covid under [President A] than [President B], remind them that
correlation doesn’t equal causation.
0.521
This is where I want my taxes to go,investing in America and future generations. A population without access to higher education
or drowning in debt cannot compete.
0.319
2
2017
There’s been some great addresses about#ScriptureStudy. What will you begin to study tomorrow?#[ReligiousConference]0.321
#[ReligiousConference]#goals: Study EVERYTHING about Christ & be a better#Disciple. Who’s with me? 0.431
We need our own testimony in these difficult times. Testimonies of others will only carry you so far.#[ChurchLeader]0.240
2022
Remember thisstarted under [the former President] and is just being continued under [the current President]. 0.457
In 2020 I sawRepublicans screaming “you have to vote for [Candidate A]!”But I also sawDems saying “you have to vote for
[Candidate B] or we will end up with 2016 all over again!”
0.666
I’ve been saying the “low unemployment” and “employee shortage” have been partly due to thegreat amount of disabled from
Covid no longer in the work force. I was told I was fear-mongering.
0.455
3
2012
[The incumbent’s] AdministrationClosing 9 Border Patrol Stations[. . . ]. WTF??!!!We need MORE, not LESS! 0.579
Voter fraud?Boston reports129% voter turnout, 79% for [the incumbent]; 74% for [a Senate candidate]. 0.518
In#Iran, one can be jailed, fined, & whipped fordefending #HumanRights. Dark reality for [a Christian pastor’s] attorney. 0.363
2021
We also have a proud history of our laws & Constitution being upheld. But today we have anillegal two-tiered system& a
Constitution that theDems & RINOs don’t obey.
0.874
THIS is why people are dying when they go into a hospital for “C-19 treatment”!!!STAY OUT OF HOSPITALS!!!Signed. . . a nurse! 0.899
We’re in theEnd Days, people. Accept Jesus [. . . ]. If ever weneeded Jesus’s protection, it’s NOW! 0.714
significant volatility, with their ideological scores fluctuating widely across the political spectrum.
In this cohort, an initial centrist position did not predict future stability.
Qualitative analysis reveals diverse, non-polarizing ideological trajectories.To complement
our quantitative findings, we conducted a case study to examine user-level ideological dynamics
—specifically, whether individuals with high variability in predicted ideology scores exhibit patterns
consistent with polarization or show more nuanced shifts. We measured each user’s ideological
volatility as the difference between their maximum and minimum yearly mean scores and selected
the top 20 most volatile users. From these, we analyzed three representative cases in detail. None
of these users align with the classical echo chamber hypothesis of unidirectional radicalization;
Table 9 presents them.
• User 1 began using partisan rhetoric in 2009, referring to Republicans as a “Lie Factory” (score
0.073) alongside unrelated everyday appeals such as promoting an animal rescue group (score
0.369). By 2022, their tone had shifted toward moderation and analytical reasoning—referencing
economic data like “price per barrel of oil” (score 0.515) and cautioning that “correlation doesn’t
equal causation” (score 0.521). This trajectory reflects a reduction in rhetorical extremity rather
than an intensification of ideology.
• User 2 transitioned from a non-political participant to a politically engaged yet ideologically
balanced commentator. In 2017, their posts focused on religious topics (e.g., #ScriptureStudy,
score 0.321). By 2022, they discussed policies spanning multiple administrations (score 0.457)
and observed commonalities in partisan messaging strategies (score 0.666). These expressions
reflect a critical, cross-cutting awareness rather than alignment with a single political pole.
• User 3 maintained consistent conservative views over a decade. In 2012, they raised concerns
about border security (score 0.579) and election integrity (score 0.518). By 2021, they continued
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 21
Table 10. Representative Topics by Political Leaning and Year (2009–2022).
Year Left-leaning Topics Center-leaning Topics Right-leaning Topics
2009 [hcr, health, reform] [copenhagen, cop15] [stimulus, job, economy] [hcr, health, reform] [iran, iranelection] [spending, stimulus, govt] [hcr, gop, tcot] [iran, iranelection]
2010 [health, reform, hcr] [haiti, earthquake] [oil, bp, oilspill] [haiti] [election, mn2010, tea, teaparty] [hcr, obamacare, repeal] [tea, party, teaparty] [flgov, scott, spending]
2011
[egypt, libya]
[medicare, cuts, deficit]
[wiunion]
[debt, debtceiling, boehner]
[egypt, mubarak, libya]
[bin laden, pakistan]
[libya, nato, war]
[wiunion, gov, walker]
[debt, obama, gop]
2012
[waronwomen, women]
[romney, mitt, returns]
[health, medicare]
[obama, romney, debate]
[syria]
[gun, guncontrol, newtown, nra]
[libya, benghazi, attack]
[obama, romney, debate]
[gun, shooting, aurora]
2013
[standwithwendy, txlege, abortion]
[gun, guns, guncontrol]
[blacklivesmatter]
[snowden, leak, nsa]
[boston, marathon, bombing]
[shutdown, government]
[irs, lerner, targeting]
[benghazi, cia]
[syria, assad, military]
2014
[ferguson, police, racism]
[acaworks, aca]
[climate, change]
[ferguson, michael brown]
[ukraine, russia, putin]
[ebola]
[mh370]
[isis, syria, iraq]
[benghazi]
[bridgegate, christie]
[irs, lerner, emails]
2015
[blacklivesmatter]
[demdebate, berniesanders]
[scottwalker, antiunion]
[trump, realdonaldtrump, gopdebate]
[iran, irandeal]
[paris, parisattacks]
[iran, deal, irandeal]
[plannedparenthood, standwithpp]
[gopdebate, trump]
2016
[feelthebern, berniesanders]
[flintwatercrisis]
[demsinphilly]
[trump, hillaryclinton, debate]
[brexit, euref]
[scalia, scotus]
[trump, realdonaldtrump, maga]
[wikileaks, emails, clinton]
[benghazi]
2017
[muslimban, travelban, nobannowall]
[aca, healthcare]
[impeachment]
[comey, mueller, trumprussia]
[charlottesville]
[metoo, sexual harassment]
[gorsuch, scotus]
[fakenews, cnn]
[tax, taxreform]
[obamacare, repeal]
2018
[guncontrolnow, nra, parkland]
[bluewave, midterms]
[metoo, kavanaugh]
[kavanaugh, ford, kavanaughhearings]
[border, children, familiesbelongtogether]
[khashoggi]
[witch hunt, mueller, fbi]
[caravan, border, buildthewall]
[kavanaugh, confirmkavanaugh]
2019
[impeachment, impeach, repadamschiff]
[greennewdeal]
[demdebate, warren]
[impeachment, ukraine, whistleblower]
[muellerreport, obstruction]
[hong kong]
[impeachment, sham, hoax]
[biden, hunter, ukraine]
[border, wall, emergency]
2020
[covid19, pandemic, trumpvirus]
[george floyd, blm, defundthepolice]
[usps, mailin]
[coronavirus, covid19]
[biden, trump, election]
[george floyd, protests]
[obamagate, spygate]
[reopenamerica, reopen]
[voterfraud, electionfraud, stopthesteal]
2021
[jan 6, insurrection, coup]
[votingrights, filibuster]
[buildbackbetter, bbb]
[capitol, riot, jan 6]
[afghanistan, withdrawal]
[vaccine, mandate, delta]
[crt, critical race theory]
[arizona, audit]
[antimask, antivax, bordercrisis]
2022
[abortion, codifyroe, womensrights]
[uvalde, gunreform]
[ukraine, standwithukraine]
[ukraine, war, russia]
[maralago, search, documents]
[roe, wade, overturn]
[inflation, gas]
[fbi, doj]
[border, migrants]
[hunter, laptop]
expressing skepticism toward institutions, citing constitutional violations (score 0.874) and
rejecting public health guidance (score 0.899). Though topics shifted, the ideological stance
remained stable, reflecting continuity rather than radicalization.
Together, these cases challenge the universality of the polarization narrative.
Comparative Thematic Analysis Reveals Divergent Discursive Arenas.To complement our
quantitative findings, we conducted a thematic analysis of political discourse on Twitter and Truth
Social—two ideologically distinct platforms. We grouped users into Left-leaning, Centrist, and
Right-leaning categories based on aggregated post-level ideology scores, and applied BERTopic [31]
to extract dominant themes. BERTopic embeds documents contextually, reduces their dimension-
ality, clusters them by density, and extracts representative keywords per topic. Results are shown
in Table 10 (Twitter, 2009–2022) and Table 11 (Truth Social, 2022).
Twitter reveals a dynamic we term a “shared agenda with competing frames. ” Across the political
spectrum, users engage with the same high-salience topics—from [hcr] in 2009 to [ukraine,
war] in 2022—suggesting a common baseline of topical attention. However, ideological divergence
emerges in framing. For example, during the 2019 impeachment, the Left referenced institutional
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

22 Xu, et al.
Table 11. Representative Topics on Truth Social by Political Leaning (2022).
Year Left-leaning Topics Center-leaning Topics Right-leaning Topics
2022
[abortion, roe, wade, overturned]
[uvalde, shooting, gun, control]
[ukraine, standwithukraine, kyiv]
[jan6, committee, hearings, insurrection]
[maralago, raid, fbi]
[ukraine, russia, war, putin]
[maralago, raid, fbi, doj, warrant]
[roe, wade, overturned, supreme, court]
[inflation, recession, economy, prices]
[hunter, laptop, bidens, fbi]
[2000mules, ballot, harvesting, fraud]
[inflation, gas, prices, bidenflation]
[fbi, doj, raid, corruption, witchhunt]
[border, crisis, migrants, illegal]
[hunter, laptop, biden, crimefamily]
[stoptheshots, diedsuddenly, pureblood]
[abortion, prolife, unborn, baby]
actors ([repadamschiff]), while the Right used delegitimizing terms ([sham, hoax] ). Similarly,
the events of January 6th surfaced as [insurrection, coup] on the Left and [capitol, riot]
at the Center, while the Right’s 2021 agenda instead foregrounded [arizona, audit] and [crt,
critical race theory] . This is a contested discursive space, not a set of isolated echo chambers.
In contrast, Truth Social exhibits a “high-conflict ideological arena” with a right-shifted discur-
sive center. Themes categorized as far-right on Twitter—e.g.,[hunter, laptop] —appear under
the “Centrist” label on Truth Social, alongside claims such as [2000mules, ballot] that have
no Twitter counterpart, reflecting that partisan narratives constitute the platform’s mainstream.
Rhetorical intensity is notably elevated: economic concerns are framed as [bidenflation], the
Mar-a-Lago search is portrayed as a partisan [witchhunt] by a [corrupt] FBI, and the term
[crimefamily] denounces the Bidens. Such vocabulary suggests a shift from political discourse
to moral indictment. While Left-leaning users exist on Truth Social, they act more as ideological
foils than dialogue participants. Topics like [jan6, hearings] and [gun control] appear, but
often in oppositional framing. Instead of reducing polarization, their presence intensifies it by
provoking adversarial responses. This dynamic is compounded by conspiratorial clusters—e.g.,
[stoptheshots, pureblood]—which anchor its ideological extremity.
Overall, polarization manifests differently across platforms: Twitter hosts a fragmented but
interconnected public sphere where competing frames coexist, whereas Truth Social functions as
a self-reinforcing enclave whose right-shifted center, moralized rhetoric, and reactive dynamics
amplify division rather than bridge it.
7 Conclusion
This paper presents TSN4PI, a unified framework that integrates natural language processing with
temporal graph neural networks for tracking political ideologies on social media. Methodologically,
we provide a robust, end-to-end pipeline that effectively bridges the domain gap between news and
social content, modeling the dynamic evolution of user interactions. We also contribute two large-
scale, publicly released datasets from X (formerly Twitter) and allsides.com. Empirically, our analysis
of these platforms reveals that the most ideologically volatile users tend to converge toward the cen-
ter, a finding contrary to widely held assumptions about increasing online polarization. Future work
includes extending to multi-dimensional ideological models and cross-platform comparative studies.
Acknowledgments
This work was supported in part by the National Natural Science Foundation of China (Grant Nos.
92370204 and 62506348), the National Key R&D Program of China (Grant No. 2023YFF0725001),
the New Generation Artificial Intelligence-National Science and Technology Major Project (Grant
No. 2025ZD0122601), Guangdong Provincial Key Laboratory of Frontier Basic Science for All-
domain Intelligence, the Guangdong Basic and Applied Basic Research Foundation (Grant No.
2023B1515120057), the Key-Area Special Project of Guangdong Provincial Ordinary Universi-
ties (Grant No. 2024ZDZX1007), the Natural Science Foundation of Anhui Province (Grant No.
2508085QF211), and the Opening Foundation of State Key Laboratory of Cognitive Intelligence,
iFLYTEK (Grant No. COGOS-2025HE02).
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 23
Supplementary Material
This document is the online-only supplementary material for the article “Against Political Po-
larization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media. ” It
collects dataset details, implementation settings, prompt templates, complexity analysis, and the
full per-model results referenced from the main text. Section, table, and figure numbers below are
those cited in the main text as belonging to the supplementary material.
A Appendix
Contents
A.1 Details of the Datasets 23
A.1.1 Data Privacy 23
A.1.2 The allsides.com Dataset 23
A.1.3 The X (Twitter) Dataset 24
A.1.4 The Truth Social Dataset 24
A.2 Implementation Details 24
A.3 Prompt Details 25
A.4 UDA Complexity Analysis 28
A.1 Details of the Datasets
A.1.1 Data Privacy.Given the sensitivity of political ideology, privacy is central to our data
handling. All news data were sourced from public websites. Social media data were anonymized
to meet ethical standards. On X and Truth Social, personal identifiers (e.g., names, handles) were
replaced with numeric IDs. Only public posts were retained; no private user data was used.
Data Release Format.To respect the terms of the underlying sources, the released datasets are
distributed in adehydratedform. For the X (Twitter) and Truth Social corpora we release post and
user identifiers together with our derived annotations (political relevance labels, ideology scores,
and the temporal interaction edges used to build the graphs), rather than the original post text; users
can rehydrate the text through the respective platform APIs subject to their terms of service. For
the news corpus we release article URLs, outlet names, publication dates, and the AllSides ideology
score of each outlet, rather than the full article text, which remains the property of the publishing
outlets. The AllSides ratings redistributed in this way are covered by the CC BY-NC 4.0 license
and are provided with the attribution required by that license; the released collection is therefore
available for noncommercial research use only. Scripts for rehydration and for reproducing every
table in the paper are provided in the repository at https://github.com/yeahjack/TSN4PI.
A.1.2 The allsides.com Dataset.The overview of the allsides.com dataset is as follows:
Table 1. Overview of the allsides.com news with annotated political ideology dataset.
Characteristic # of News Articles # of Media Outlets
Total Articles/Outlets 233,570 466
Political Ideology
Center 76,023 158
Lean Left 53,532 106
Right 45,506 75
Lean Right 32,555 62
Left 25,954 65
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

24 Xu, et al.
Data Preprocessing.As with the X dataset described below, we retained only English articles to
ensure linguistic consistency. We also normalized ideology scores to align with other framework
components. For an article 𝑁 with original score 𝑆raw ∈ [−6, 6], the adjusted score 𝑆adjusted is
computed as:
𝑆adjusted(𝑁)= 𝑆raw+6 12 .(1)
This normalization maps the score to the[0, 1] interval, facilitating uniform scale interpretation
during model training and evaluation.
Left
 Lean Left
 Center
 Lean Right
 Right
Word Clouds Representing Titles of Different Political Leanings
Fig. 1. Word Clouds Highlighting Common Terms in News Reports Titles by Political Leanings. The visual-
ization spans from ‘Left’ to ‘Right’, with ‘Center’ in the middle, reflecting the language usage patterns in
political news reporting.
We also created word clouds for news titles from different political ideology factions, as shown
in Figure 1. We found that media with a left-leaning bias generally focus on topics such as the
Capitol riot, the Supreme Court, and COVID, while right-leaning media often focus on Elon Musk,
Paul Pelosi, the Committee Criminal, and vaccine mandates, with center media reporting on both.
This reflects not only the different focus points of media across the political spectrum but also the
distinct use of language in reporting the same topics, aligning with our research hypothesis: even
for the same events, the choice of words can still reveal their political ideologies.
A.1.3 The X (Twitter) Dataset.Data Preprocessing.To ensure linguistic consistency with our
analytical focus of presidential elections in the United States, we retained only English-language
tweets. Language filtering was performed using thefasttext-langdetectlibrary [41, 42].
A.1.4 The Truth Social Dataset.Data Preprocessing.Preliminary cleaning and preprocessing
were applied to the raw dataset. Given that some “Truths” had missing or misaligned timestamps,
we utilized web scraping tools to supplement and correct the timestamps for these accessible
“Truths. ”
A.2 Implementation Details
Models were trained with a 90/10 train-test split. For PIDN, we trained for 3 epochs with a learning
rate of2× 10−5 and a weight decay of 0.01. For the TST task, we used theLlama-3.1-8B-Instruct
model to generate style-transferred texts with a temperature of 0.7, top_p of 0.95, and a maximum
generation length of 512 tokens, terminating on the “</Tweet>” token. The prompts for directly
using the LLM-based method to assess political relevance and assigning scores, TST andLLM-
as-a-judgefor evaluation are provided in Tables 2, 3, and 4, respectively. To facilitate automatic
evaluation, we leverage tool calling to parse model responses into a structured JSON format. For
PIDN, we used(𝛼= 0.4,𝛽= 0.2) during the preliminary backbone comparison. After the dedicated
tuning stage reported in the main paper, we selected(𝛼= 0.4,𝛽= 0.3) for the ablation study and
final models. For PIPN, we adopted the default sampling, memory, and network configurations
provided by TGL [90] for the different TGNNs. Mixed-precision training and inference were adopted
for efficiency. All experiments were conducted on eight machines, each equipped with 8Nvidia
A800GPUs (80GB VRAM each), runningUbuntu 22.04withPython 3.11. We used the vllm [47]
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 25
framework for text generation tasks, and TGL [90] for TGNNs. For static graph tasks, we used
PyTorch Geometric[24]. The training and inference were performed usingPyTorch2.4.0.
A.3 Prompt Details
Prompt for LLM-based method.Here we provide the prompt template used for the LLM-based
method, which is designed to generate relevance and scores for posts. We enabled tool calling
to allow the model to output structured results after reasoning about the political relevance and
leaning of a given tweet.
Prompt Template for Political Tweet Analysis with Function Calling
System Prompt:
You are an expert political analyst specializing in U.S. politics. Your task is to analyze a given tweet and pro-
vide a structured analysis by using the record_political_analysis tool. Carefully determine the following
parameters for the tool:
•relevance: Set to ’1’ if the tweet is politically relevant to the U.S. context, ’0’ otherwise.
•score: If relevant, assign a float from 0.0 (left-leaning) to 1.0 (right-leaning). This parameter should
only be provided for relevant tweets.
•reasoning: Provide a clear, step-by-step explanation for your decisions. Escape all double quotes with
\.
You must directly use therecord_political_analysisfunction to output your findings.
Guidelines & Tool Schema (record_political_analysis):
Function Name: record_political_analysis
Description: Records the political analysis of a tweet after careful reasoning.
Parameters:
-`reasoning`(string, required): Detailed step-by-step thinking.
-`relevance`(string, required):'1'if political,'0'otherwise.
-`score`(number, optional): Score 0.0-1.0. Only required if relevance=='1'.
Example Input Tweet:BREAKING: The Senate just passed the new infrastructure bill. A major win for the
administration, but critics on both sides are already voicing concerns about the spending.
Example Output (Tool Call Arguments):
{
" reasoning " : " The tweet discusses a major piece of U . S . legislation , the
infrastructure bill , and mentions the Senate and the administration .
This is clearly a political topic . The tweet presents a balanced view ,
noting it as a'win'but also mentioning'critics on both sides',
suggesting a centrist take . Therefore , the score is set to 0.5. " ,
" relevance " : " 1 " ,
" score " : 0 . 5
}
Input Format:Analyze this tweet:\n\n{tweet_text}
Start of Response:The model should directly output the tool call. The arguments should be a single, well-
formed JSON string.
Prompt for Text Style Transfer.Here we provide the prompt template used for the text style
transfer (TST) task, which is designed to convert news articles into concise tweets. This prompt is
crucial for training our model to understand the nuances of tweet generation from longer news
content.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

26 Xu, et al.
Prompt Template for News-to-Tweet Style Transfer
System Prompt:
You will be given a news report. Your task is to rewrite it as a tweet that captures the core message.
Guidelines:
Beconciseand stay within 280 characters.
Use commonabbreviations(e.g., ICYMI, IMO).
Addhashtagsto highlight key topics (e.g., #Breaking).
Mention relevant accounts using@when applicable.
Always produce a non-empty tweet inENGLISH.
End your generated tweet with the token: </Tweet>
Example News:In an extraordinary face-to-face meeting at the White House on Wednesday, President Joe
Biden told Ukrainian President Volodymyr Zelenskyy that. . .
Example Tweet:President Biden meets with Ukrainian President Zelenskyy at the White House, pledging
“unequivocal and unbending support” to Ukraine. #UkraineWar #WhiteHouseMeeting
Input Format:<Tweet>{news_text}</Tweet>
Start of Response:<Tweet>
Prompt for Text Style Transfer Evaluation.This prompt is used to evaluate the quality of the
generated tweets from the TST task byLLM-as-a-judge. It is designed to assess the relevance and
quality of the generated tweet in relation to the original news article. We enabled tool calling to
allow the model to output structured scores after reasoning about the tweet’s style and semantic
preservation.
Prompt forLLM-as-a-JudgeEvaluation of Text Style Transfer
System Prompt:
You are a strict grader. Use the rubric below to give two integer scores from 0–10:
•style_score- tweet naturalness on social media
•semantic_score- key-information preservation
Rubric examples (do not output these examples in your answer):
10 - flawless style AND all facts present
8 - minor issues in style or small missing details
5 - several awkward phrases OR half the facts missing
2 - hard to read or mostly irrelevant
0 - gibberish or unrelated to the article
Your job is tothink step-by-step (Chain-of-Thought)about style and semantics, then call the function
grade_tweetwith two integer scores.
Tool Schema (grade_tweet):
Function Name: grade_tweet
Description: Returns integer style and semantic scores for a tweet given a news article.
Parameters:
-`style_score`(integer, required): Tweet naturalness on social media, from 0 to 10.
-`semantic_score`(integer, required): Key-information preservation score, from 0 to 10.
Example Output (Tool Call Arguments):
{
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 27
" style_score " : 9 ,
" semantic_score " : 1 0
}
Input Format:
News article:
<ARTICLE>
[Original News Article Text Here]
</ARTICLE>
Generated tweet:
<TWEET>
[Style-Transferred Tweet Text Here]
</TWEET>
Start of Response:The model should first provide its Chain-of-Thought reasoning, then output the tool call.
The final response must include the call to thegrade_tweetfunction.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

28 Xu, et al.
A.4 UDA Complexity Analysis
To provide a comprehensive understanding of the computational overhead associated with our
UDA module, we present a detailed complexity analysis of the Maximum Mean Discrepancy (MMD)
and Kullback-Leibler (KL) divergence methods. This analysis examines theoretical time complexity,
floating-point operations (FLOPs), and practical characteristics of GPU implementations. We assume
two sets of embeddings,𝐸𝑋 and𝐸𝑌 , each containing𝑁 samples of dimension𝐷, corresponding to
a batch from the source and target domains, respectively.
Maximum Mean Discrepancy (MMD).The computational core of theMMDloss is the construc-
tion of three kernel matrices,𝐾 𝑋 𝑋,𝐾 𝑌𝑌 , and𝐾 𝑋𝑌 , each of size𝑁×𝑁.
Time Complexity.The calculation is dominated by the pairwise evaluation of the kernel function.
For the Gaussian RBF kernel, computing the squared Euclidean distance∥𝑥−𝑦∥ 2 between two
𝐷-dimensional vectors requires𝑂(𝐷) operations. Since this must be done for all𝑁×𝑁 pairs to
construct each kernel matrix, the complexity of forming one matrix is𝑂(𝑁 2𝐷) . The final summation
over the kernel matrices is𝑂(𝑁 2). Therefore, the overall time complexity is dominated by kernel
matrix computation, yielding𝑂(𝑁 2𝐷).
Floating-Point Operations (FLOPs).We can estimate the FLOPs for the RBF kernel. The cal-
culation of∥𝑥−𝑦∥ 2 involves approximately3𝐷 FLOPs (𝐷 subtractions,𝐷 multiplications,𝐷− 1
additions). Constructing the three𝑁×𝑁 kernel matrices thus requires roughly3×𝑁 2× 3𝐷= 9𝑁 2𝐷
FLOPs. This quadratic dependence on𝑁makesMMDcomputationally demanding.
GPU Latency and Bottlenecks.On GPU architectures, the pairwise distance calculations can
be efficiently mapped to highly optimized Generalized Matrix-Matrix Multiplication (GEMM)
operations. However, the𝑂(𝑁 2𝐷) complexity makes the algorithm fundamentally compute-bound.
Latency grows quadratically with the batch size𝑁 , which rapidly becomes the primary performance
bottleneck. Furthermore, storing the intermediate kernel matrices requires𝑂(𝑁 2) memory, which
can exhaust the GPU’s VRAM for large𝑁 (e.g.,𝑁> 4096), thereby imposing a practical limit on
the batch size.
Kullback-Leibler (KL) Divergence.TheKLdivergence loss is computed element-wise on the
distribution-like outputs𝑃and𝑄, which are tensors of shape(𝑁,𝐷).
Time Complexity.The computation involves element-wise division, logarithm, and multiplication
across two(𝑁,𝐷) tensors, followed by a summation. Each of these element-wise operations has
a time complexity proportional to the number of elements. Thus, the overall time complexity is
linear with respect to both𝑁and𝐷, resulting in𝑂(𝑁𝐷).
Floating-Point Operations (FLOPs).The sequence of operations (division, logarithm, multiplica-
tion, and summation) results in approximately4𝑁𝐷 FLOPs. This is substantially lower thanMMD’s
quadratic complexity.
GPU Latency and Bottlenecks.The element-wise nature of theKLdivergence calculation makes
it an “embarrassingly parallel” problem, ideally suited for GPU execution. The operations exhibit
high data parallelism and low computational intensity. Consequently, the algorithm is typically
memory-bound; its latency is limited not by the speed of computation but by the GPU’s memory
bandwidth for reading the input tensors𝑃 and𝑄. The overall latency is minimal and scales linearly
with the total number of elements,𝑁×𝐷.
Summary and Implications.The choice betweenMMDandKLdivergence for domain adaptation
introduces a critical trade-off in computational efficiency. Table 5 summarizes the computational
characteristics of each method.
In practice, the quadratic complexity ofMMDrestricts its application to smaller batch sizes ( 𝑁 ),
whereasKLdivergence remains efficient even for large-batch training. This computational difference
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 29
Table 5. Computational complexity comparison of UDA methods.
Metric Time Complexity FLOPs (Approx.) GPU Bottleneck
MMD 𝑂(𝑁 2𝐷) 9𝑁 2𝐷 Compute-Bound
KLDivergence 𝑂(𝑁𝐷) 4𝑁𝐷 Memory-Bound
necessitates careful management of batch sizes when usingMMDto maintain feasible training
times, whileKLdivergence offers a more scalable alternative from a computational standpoint.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

30 Xu, et al.
Table 6. Unified performance analysis of the Qwen2.5 model family (Part 1: 0.5B, 3B, 7B). All models are
evaluated from 0-shot to 200-shot settings.
Classification (F1↑) Political Class Detail↑Regression Error↓
Model / Setting Non-political Political Macro Avg. Precision Recall MAE RMSE
Few-Shot forQwen2.5-0.5B-Instruct
0-shot 0.510±0.022 0.727±0.007 0.618±0.014 0.601±0.007 0.918±0.006 0.413±0.007 0.478±0.005
2-shot 0.568±0.132 0.717±0.035 0.643±0.082 0.629±0.094 0.855±0.061 0.297±0.055 0.364±0.054
4-shot 0.607±0.132 0.751±0.051 0.679±0.089 0.662±0.126 0.901±0.088 0.330±0.031 0.395±0.038
6-shot 0.577±0.098 0.750±0.032 0.664±0.062 0.622±0.040 0.951±0.052 0.305±0.016 0.367±0.018
8-shot 0.525±0.233 0.753±0.058 0.639±0.143 0.628±0.088 0.960±0.067 0.257±0.024 0.317±0.032
10-shot 0.619±0.099 0.773±0.023 0.696±0.061 0.647±0.053 0.970±0.046 0.287±0.056 0.349±0.062
20-shot 0.824±0.090 0.867±0.046 0.845±0.068 0.797±0.097 0.964±0.038 0.285±0.019 0.357±0.015
50-shot 0.896±0.063 0.916±0.043 0.906±0.053 0.849±0.074 0.999±0.001 0.282±0.027 0.352±0.027
100-shot 0.988±0.007 0.988±0.006 0.988±0.006 0.980±0.016 0.996±0.006 0.274±0.018 0.338±0.017
200-shot 0.988±0.009 0.988±0.008 0.988±0.009 0.978±0.018 0.998±0.003 0.245±0.023 0.309±0.027
Few-Shot forQwen2.5-3B-Instruct
0-shot 0.946±0.003 0.943±0.003 0.945±0.003 0.945±0.008 0.942±0.006 0.283±0.005 0.333±0.005
2-shot 0.977±0.004 0.976±0.005 0.977±0.005 0.987±0.005 0.965±0.012 0.258±0.016 0.299±0.021
4-shot 0.970±0.015 0.968±0.018 0.969±0.016 0.984±0.025 0.954±0.042 0.271±0.035 0.321±0.046
6-shot 0.981±0.012 0.979±0.014 0.980±0.013 0.994±0.006 0.966±0.027 0.260±0.021 0.312±0.029
8-shot 0.984±0.008 0.982±0.010 0.983±0.009 0.993±0.004 0.972±0.022 0.275±0.024 0.335±0.032
10-shot 0.980±0.014 0.978±0.016 0.979±0.015 0.997±0.003 0.961±0.032 0.268±0.030 0.331±0.038
20-shot 0.987±0.002 0.986±0.002 0.986±0.002 0.998±0.003 0.974±0.004 0.260±0.028 0.325±0.036
50-shot 0.985±0.007 0.983±0.009 0.984±0.008 1.000±0.000 0.967±0.018 0.291±0.034 0.368±0.032
100-shot 0.978±0.005 0.972±0.009 0.975±0.006 1.000±0.000 0.947±0.017 0.283±0.025 0.367±0.029
200-shot 0.992±0.002 0.989±0.003 0.990±0.002 0.998±0.002 0.980±0.006 0.273±0.015 0.353±0.014
Few-Shot forQwen2.5-7B-Instruct
0-shot 0.927±0.002 0.905±0.003 0.916±0.002 0.992±0.003 0.833±0.004 0.238±0.004 0.288±0.005
2-shot 0.936±0.021 0.928±0.026 0.932±0.024 0.986±0.005 0.879±0.049 0.242±0.005 0.292±0.007
4-shot 0.920±0.032 0.905±0.044 0.912±0.038 0.986±0.006 0.840±0.079 0.230±0.007 0.282±0.012
6-shot 0.918±0.024 0.903±0.035 0.911±0.030 0.987±0.008 0.835±0.063 0.243±0.007 0.301±0.007
8-shot 0.906±0.024 0.886±0.035 0.896±0.029 0.990±0.007 0.804±0.061 0.246±0.007 0.305±0.011
10-shot 0.898±0.019 0.874±0.028 0.886±0.024 0.995±0.002 0.781±0.047 0.236±0.012 0.291±0.015
20-shot 0.923±0.031 0.908±0.043 0.916±0.037 0.995±0.002 0.838±0.074 0.244±0.016 0.306±0.019
50-shot 0.961±0.014 0.958±0.015 0.960±0.014 0.996±0.003 0.924±0.031 0.241±0.018 0.304±0.020
100-shot 0.964±0.008 0.962±0.009 0.963±0.009 0.998±0.000 0.929±0.017 0.237±0.010 0.307±0.012
200-shot 0.974±0.008 0.973±0.008 0.973±0.008 0.998±0.002 0.950±0.017 0.243±0.012 0.315±0.018
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 31
Table 7. Unified performance analysis of the Qwen2.5 model family (Part 2: 14B, 32B, 72B). All models are
evaluated from 0-shot to 200-shot settings.
Classification (F1↑) Political Class Detail↑Regression Error↓
Model / Setting Non-political Political Macro Avg. Precision Recall MAE RMSE
Few-Shot forQwen2.5-14B-Instruct
0-shot 0.918±0.003 0.900±0.004 0.909±0.003 0.986±0.001 0.827±0.006 0.227±0.004 0.285±0.003
2-shot 0.949±0.022 0.941±0.029 0.945±0.026 0.992±0.003 0.896±0.054 0.219±0.007 0.273±0.011
4-shot 0.955±0.009 0.949±0.011 0.952±0.010 0.994±0.001 0.908±0.021 0.216±0.002 0.271±0.007
6-shot 0.963±0.014 0.959±0.017 0.961±0.016 0.991±0.004 0.929±0.034 0.235±0.025 0.299±0.032
8-shot 0.961±0.019 0.956±0.024 0.959±0.022 0.992±0.005 0.924±0.047 0.232±0.008 0.295±0.014
10-shot 0.962±0.015 0.958±0.018 0.960±0.017 0.988±0.003 0.930±0.036 0.236±0.009 0.305±0.013
20-shot 0.980±0.006 0.978±0.006 0.979±0.006 0.990±0.002 0.967±0.013 0.235±0.010 0.300±0.015
50-shot 0.982±0.002 0.981±0.002 0.981±0.002 0.991±0.002 0.971±0.005 0.239±0.006 0.309±0.011
100-shot 0.968±0.007 0.965±0.008 0.966±0.008 0.988±0.004 0.943±0.015 0.241±0.007 0.311±0.006
200-shot 0.979±0.004 0.979±0.005 0.979±0.004 0.995±0.001 0.963±0.009 0.223±0.004 0.301±0.004
Few-Shot forQwen2.5-32B-Instruct
0-shot 0.946±0.001 0.937±0.002 0.942±0.002 0.991±0.001 0.889±0.004 0.225±0.002 0.283±0.001
2-shot 0.956±0.008 0.955±0.009 0.956±0.008 0.993±0.002 0.921±0.017 0.206±0.009 0.263±0.012
4-shot 0.962±0.008 0.962±0.008 0.962±0.008 0.994±0.001 0.933±0.015 0.214±0.005 0.275±0.006
6-shot 0.968±0.005 0.969±0.005 0.968±0.005 0.992±0.003 0.946±0.011 0.212±0.005 0.272±0.008
8-shot 0.976±0.006 0.977±0.006 0.976±0.006 0.995±0.002 0.959±0.010 0.210±0.007 0.272±0.011
10-shot 0.973±0.009 0.974±0.010 0.973±0.009 0.994±0.001 0.954±0.018 0.207±0.006 0.270±0.010
20-shot 0.980±0.004 0.980±0.004 0.980±0.004 0.993±0.002 0.968±0.009 0.219±0.011 0.284±0.016
50-shot 0.989±0.002 0.989±0.002 0.989±0.002 0.995±0.002 0.984±0.004 0.218±0.007 0.285±0.008
100-shot 0.990±0.001 0.990±0.001 0.990±0.001 0.996±0.001 0.985±0.002 0.225±0.007 0.296±0.007
200-shot 0.992±0.002 0.993±0.002 0.992±0.002 0.996±0.001 0.990±0.003 0.212±0.011 0.284±0.011
Few-Shot forQwen2.5-72B-Instruct
0-shot 0.955±0.002 0.950±0.003 0.953±0.002 0.994±0.002 0.910±0.004 0.216±0.004 0.275±0.004
2-shot 0.946±0.015 0.935±0.020 0.940±0.017 0.990±0.003 0.887±0.037 0.206±0.004 0.265±0.003
4-shot 0.972±0.007 0.969±0.009 0.971±0.008 0.989±0.003 0.950±0.018 0.206±0.009 0.268±0.011
6-shot 0.967±0.012 0.962±0.014 0.964±0.013 0.989±0.002 0.937±0.029 0.212±0.008 0.277±0.011
8-shot 0.972±0.010 0.969±0.012 0.971±0.011 0.990±0.003 0.949±0.022 0.225±0.016 0.292±0.022
10-shot 0.965±0.014 0.959±0.017 0.962±0.015 0.993±0.002 0.928±0.032 0.217±0.018 0.285±0.022
20-shot 0.974±0.006 0.971±0.007 0.972±0.006 0.992±0.002 0.950±0.015 0.214±0.011 0.279±0.013
50-shot 0.988±0.005 0.988±0.006 0.988±0.006 0.991±0.002 0.985±0.012 0.213±0.006 0.284±0.009
100-shot 0.987±0.003 0.992±0.001 0.989±0.002 0.992±0.001 0.993±0.003 0.220±0.014 0.297±0.016
200-shot 0.985±0.003 0.993±0.001 0.989±0.002 0.994±0.002 0.991±0.002 0.212±0.007 0.290±0.008
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

32 Xu, et al.
References
[1] Christopher H. Achen. 1975. Mass Political Attitudes and the Survey Response.Am. Political Sci. Rev.(1975).
[2] Lin Ai, Sameer Gupta, Shreya Oak, Zheng Hui, Zizhou Liu, and Julia Hirschberg. 2024. TweetIntent@Crisis: A Dataset
Revealing Narratives of Both Sides in the Russia-Ukraine Crisis. InICWSM.
[3] AllSides. 2024. AllSides Media Bias Ratings. https://www.allsides.com/media-bias/media-bias-ratings. Licensed under
CC BY-NC 4.0.
[4] Isabelle Augenstein, Tim Rocktäschel, Andreas Vlachos, and Kalina Bontcheva. 2016. Stance Detection with Bidirectional
Conditional Encoding. InEMNLP.
[5] Ramy Baly, Georgi Karadzhov, Abdelrhman Saleh, James Glass, and Preslav Nakov. 2019. Multi-Task Ordinal Regression
for Jointly Predicting the Trustworthiness and the Leading Political Ideology of News Media. InNAACL.
[6] Iz Beltagy, Matthew E Peters, et al. 2020. Longformer: The Long-Document Transformer.arXiv:2004.05150(2020).
[7] Rishabh Bhardwaj, Sourav Kumar, and Vikram Pudi. 2024. CAT-Gen: A Context-Aware Teleology-Guided Generative
Model for Mitigating Task-Specific Bias. InFAccT.
[8] Kamel Boukhalfa, Sami Belkacem, and Omar Boussaid. 2022. Ranking Social Media News Feeds: A Comparative Study
of Personalized and Non-personalized Prediction Models. InAIAP.
[9] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D. Kaplan, Prafulla Dhariwal, Arvind Neelakantan,
Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan,
Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford,
Ilya Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot Learners. InNeurIPS.
[10] Cory J. Cascalheira, Santosh Chapagain, Ryan E. Flinn, Dannie Klooster, Danica Laprade, Yuxuan Zhao, Emily M. Lund,
Alejandra Gonzalez, Kelsey Corro, Rikki Wheatley, Ana Gutierrez, Oziel Garcia Villanueva, Koustuv Saha, Munmun De
Choudhury, Jillian R. Scheer, and Shah M. Hamdi. 2024. The LGBTQ+ Minority Stress on Social Media (MiSSoM)
Dataset: A Labeled Dataset for Natural Language Processing and Machine Learning. InICWSM.
[11] Pew Research Center. 2014.Political Polarization in the American Public. http://pewrsr.ch/1mHUL02
[12] Pew Research Center. 2021.Both Republicans and Democrats Prioritize Family, but They Differ over Other Sources of
Meaning in Life. https://pewrsr.ch/3kXL0mF
[13] Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, et al. 2024. BGE M3-Embedding: Multi-Lingual, Multi-
Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation.arXiv:2402.03216(2024).
[14] Kai Chen, Zihao He, Keith Burghardt, Jingxin Zhang, and Kristina Lerman. 2024. IsamasRed: A Public Dataset Tracking
Reddit Discussions on Israel-Hamas Conflict. InICWSM.
[15] Tao Chen, Baoyu Zhang, Xiao Wang, Weishan Zhang, Chitin Hon, Wang Di, Long Chen, Qiang Li, and Fei-Yue Wang.
2024. Public Opinion Evolution in Cyberspace: A Case Analysis of Pelosi’s Visit to Taiwan.IEEE TCSS(2024).
[16] Ernesto Colacrai, Federico Cinus, Gianmarco De Francisci Morales, and Michele Starnini. 2024. Navigating Multidi-
mensional Ideologies with Reddit’s Political Compass: Economic Conflict and Social Affinity. InWWW.
[17] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán,
Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Unsupervised Cross-Lingual Representation
Learning at Scale.arXiv:1911.02116(2019).
[18] Michael D. Conover, Bruno Goncalves, Jacob Ratkiewicz, Alessandro Flammini, and Filippo Menczer. 2011. Predicting
the Political Alignment of Twitter Users. InProc. IEEE PASSAT and SocialCom.
[19] Lu Dai, Yijie Xu, Jinhui Ye, Hao Liu, and Hui Xiong. 2025. SePer: Measure Retrieval Utility Through The Lens Of
Semantic Perplexity Reduction. InICLR.
[20] DeepSeek-AI. 2024. DeepSeek-V3 Technical Report.arXiv:2412.19437(2024).
[21] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. BERT: Pre-training of Deep Bidirectional
Transformers for Language Understanding.arXiv:1810.04805(2018).
[22] Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zihang Wu, Baobao Chang, Xu Sun, Jing Li, and Zhifang Sui. 2023. A
Survey on In-Context Learning.AI Open(2023).
[23] Aleksandra Edwards and Jose Camacho-Collados. 2024. Language Models for Text Classification: Is In-Context Learning
Enough?. InLREC-COLING 2024.
[24] Matthias Fey et al. 2019. Fast Graph Representation Learning with PyTorch Geometric. InICLR GRL Workshop.
[25] James Flamino, Alessandro Galeazzi, Stuart Feldman, Michael W Macy, Brendan Cross, Zhenkun Zhou, Matteo
Serafino, Alexandre Bovet, Hernán A Makse, and Boleslaw K Szymanski. 2023. Political Polarization of News Media
and Influencers on Twitter in the 2016 and 2020 US Presidential Elections.Nature Human Behaviour(2023).
[26] Isabel O. Gallegos, Aleksandra Urman, Soroush Annagar, Celina Kacperski, Iacopo Lupu, and Ira Ktena. 2023. Bias and
Fairness in Large Language Models: A Survey. InFAccT.
[27] Alessandro Gambetti and Qiwei Han. 2024. AiGen-FoodReview: A Multimodal Dataset of Machine-Generated
Restaurant Reviews and Images on Social Media. InICWSM.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 33
[28] Patrick Gerard, Nicholas Botzer, and Tim Weninger. 2023. Truth Social Dataset.
[29] Homero Gil de Zúñiga, Nakwon Jung, and Sebastián Valenzuela. 2012. Social Media Use for News and Individuals’
Social Capital, Civic Engagement and Political Participation.Journal of Computer-Mediated Communication(2012).
[30] Eric Gilbert, Tony Bergstrom, et al. 2009. Blogs Are Echo Chambers: Blogs Are Echo Chambers. InHICSS.
[31] Maarten Grootendorst. 2022. BERTopic: Neural topic modeling with a class-based TF-IDF procedure.arXiv preprint
arXiv:2203.05794(2022).
[32] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie Ma,
Honghao Liu, et al. 2024. A Survey on LLM-as-a-Judge.arXiv:2411.15594(2024).
[33] Andrew Guess, Brendan Nyhan, Benjamin Lyons, and Jason Reifler. 2018. Avoiding the Echo Chamber about Echo
Chambers.Knight Foundation(2018).
[34] Weiyu Guo, Ziyang Chen, Shaoguang Wang, Jianxiang He, Yijie Xu, Jinhui Ye, Ying Sun, and Hui Xiong. 2025. Logic-
in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding. In
NeurIPS.
[35] Qiuhan Han, Qian Wang, Atsushi Yoshikawa, and Masayuki Yamamura. 2025. PulseReddit: A Novel Reddit Dataset for
Benchmarking MAS in High-Frequency Cryptocurrency Trading.arXiv preprint(2025).
[36] Matthew Henderson, Iñigo Casanueva, Nikola Mrkšić, Pei-Hao Su, Ivan Vulić, and Tsung-Hsien Wen. 2019. A Repository
of Conversational Datasets. InConvAI Workshop at ACL 2019.
[37] Yong Hu, Heyan Huang, Anfan Chen, and Xian-Ling Mao. 2020. Weibo-COV: A Large-Scale COVID-19 Social Media
Dataset from Weibo. InEMNLP Workshop on NLP for COVID-19.
[38] Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda,
Alan Hayes, Alec Radford, et al. 2024. GPT-4o System Card.arXiv:2410.21276(2024).
[39] Mohit Iyyer, Peter Enns, Jordan Boyd-Graber, and Philip Resnik. 2014. Political Ideology Detection Using Recursive
Neural Networks. InACL.
[40] Julie Jiang, Xiang Ren, and Emilio Ferrara. 2023. Retweet-BERT: Political Leaning Detection Using Language Features
and Information Diffusion on Social Networks. InICWSM.
[41] Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, Hérve Jégou, and Tomas Mikolov. 2016. FastText.zip:
Compressing text classification models.arXiv preprint arXiv:1612.03651(2016).
[42] Armand Joulin, Edouard Grave, Piotr Bojanowski, and Tomas Mikolov. 2016. Bag of Tricks for Efficient Text Classifica-
tion.arXiv preprint arXiv:1607.01759(2016).
[43] Junseong Kim, Seolhwa Lee, Jihoon Kwon, Sangmo Gu, Yejin Kim, Minkyung Cho, Jy-yong Sohn, and Chanyeol Choi.
2024. Linq-Embed-Mistral: Elevating Text Retrieval with Improved GPT Data Through Task-Specific Control and
Quality Refinement. Linq AI Research Blog. https://getlinq.com/blog/linq-embed-mistral/
[44] Thomas N. Kipf and Max Welling. 2017. Semi-Supervised Classification with Graph Convolutional Networks. InICLR.
[45] Dilek Küçuk and Fazli Can. 2020. Stance Detection: A Survey.ACM CSUR(2020).
[46] Srijan Kumar, Xikun Zhang, and Jure Leskovec. 2019. Predicting Dynamic Embedding Trajectory in Temporal
Interaction Networks. InACM SIGKDD.
[47] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, et al. 2023.
Efficient Memory Management for Large Language Model Serving with PagedAttention. InSOSP.
[48] Pengteng Li, Pinhao Song, Wuyang Li, Huizai Yao, Weiyu Guo, Yijie Xu, Dugang Liu, and Hui Xiong. 2025. See&Trek:
Training-Free Spatial Prompting for Multimodal Large Language Model. InNeurIPS.
[49] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer,
and Veselin Stoyanov. 2019. RoBERTa: A Robustly Optimized BERT Pretraining Approach.arXiv:1907.11692(2019).
[50] Kuan-Chieh Lo, Shih-Chieh Dai, Aiping Xiong, et al. 2021. Escape from An Echo Chamber. InWWW Companion.
[51] Imran Majid. 2023. Tweets Dataset. https://www.kaggle.com/datasets/i191796majid/tweets
[52] Amin Mekacher, Max Falkenberg, and Andrea Baronchelli. 2024. The Koo Dataset: An Indian Microblogging Platform
with Global Ambitions. InICWSM.
[53] Aristides Milios, Siva Reddy, and Dzmitry Bahdanau. 2023. In-Context Learning for Text Classification with Many
Labels.arXiv:2309.10954(2023).
[54] Saif M. Mohammad, Svetlana Kiritchenko, Parinaz Sobhani, Xiaodan Zhu, and Colin Cherry. 2016. SemEval-2016 Task
6: Detecting Stance in Tweets. InSemEval 2016.
[55] Martin Müller, Marcel Salathé, and Per E Kummervold. 2020. COVID-Twitter-BERT: A Natural Language Processing
Model to Analyse COVID-19 Content on Twitter.arXiv:2005.07503(2020).
[56] Dat Quoc Nguyen et al. 2020. BERTweet: A Pre-trained Language Model for English Tweets. InEMNLP Demo.
[57] Lucas Santos de Oliveira, Marcelo S. Amaral, and Pedro O.S. Vaz-de Melo. 2021. Long-term Characterization of Political
Communications on Social Media. InIEEE/WIC/ACM WI.
[58] Chris Ou-Yang. 2014. newspaper3k: Article scraping & curation. Python library. Available at: https://github.com/
codelucas/newspaper.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

34 Xu, et al.
[59] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini
Agarwal, Katarina Slama, Alex Ray, et al. 2022. Training Language Models to Follow Instructions with Human Feedback.
InNeurIPS.
[60] Jay Patel, Pujan Paudel, Emiliano De Cristofaro, Gianluca Stringhini, and Jeremy Blackburn. 2024. iDRAMA-Scored-
2024: A Dataset of the Scored Social Media Platform from 2020 to 2023. InICWSM.
[61] Juan Manuel Pérez, Paula Miguel, and Viviana Cotik. 2025. Exploring Large Language Models for Hate Speech
Detection in Rioplatense Spanish. InNAACL Findings.
[62] Paloma Piot, Patricia Martín-Rodilla, and Javier Parapar. 2024. MetaHate: A Dataset for Unifying Efforts on Hate
Speech Detection. InICWSM.
[63] Reiner Pope, Sholto Li, Harris Li, Marc Durdan, Mostofa Patwary, Guanhua Cheng, Marcello Casarsa, Deepak Kalamkar,
Joe Laurenzo, Jacob Adkins, et al. 2023. Efficiently Scaling Transformer Inference. InMLSys.
[64] Walter Quattrociocchi, Antonio Scala, and Cass R Sunstein. 2016. Echo Chambers on Facebook.SSRN(2016).
[65] Nils Reimers and Iryna Gurevych. 2019. Sentence-BERT: Sentence Embeddings Using Siamese BERT-Networks.
arXiv:1908.10084(2019).
[66] Emanuele Rossi, Ben Chamberlain, Fabrizio Frasca, Davide Eynard, Federico Monti, and Michael Bronstein. 2020.
Temporal Graph Networks for Deep Learning on Dynamic Graphs. InICML GRL Workshop.
[67] Tim Sainburg, Leland McInnes, and Timothy Q. Gentner. 2020. Parametric UMAP: Learning Embeddings with Deep
Neural Networks for Representation and Semi-Supervised Learning.arXiv:2009.12981(2020).
[68] Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. 2019. DistilBERT: A Distilled Version of BERT:
Smaller, Faster, Cheaper and Lighter.arXiv:1910.01108(2019).
[69] Eitan Sapiro-Gheiler. 2019. Examining political trustworthiness through text-based measures of ideology. InAAAI.
[70] Lanyu Shang, Bozhang Chen, Anav Vora, Yang Zhang, Ximing Cai, and Dong Wang. 2024. SocialDrought: A Social and
News Media Driven Dataset and Analytical Platform towards Understanding Societal Impact of Drought. InICWSM.
[71] Parinaz Sobhani, Diana Inkpen, and Stan Matwin. 2016. A Dataset for Stance Detection in Tweets. InLREC 2016.
[72] Qwen Team. 2025.Qwen2: The Next Generation of Qwen Language Models. Technical Report. Alibaba Cloud Computing
Ltd. https://github.com/QwenLM/Qwen2
[73] Che-Wei Tsai, Yen-Hao Huang, Tsu-Keng Liao, Didier Fernando Salazar Estrada, Retnani Latifah, and Yi-Shin Chen.
2024. Leveraging Conflicts in Social Media Posts: Unintended Offense Dataset. InEMNLP.
[74] Elsbeth Turcan and Kathleen McKeown. 2019. Dreaddit: A Reddit Dataset for Stress Analysis in Social Media. In
EMNLP Workshop on LOUHI.
[75] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. 2018. Graph
Attention Networks. InICLR.
[76] Chao Wang, Qi Liu, Runze Wu, Enhong Chen, Chuanren Liu, Xunpeng Huang, and Zhenya Huang. 2018. Confidence-
aware matrix factorization for recommender systems. InAAAI.
[77] Chao Wang, Hengshu Zhu, Qiming Hao, Keli Xiao, and Hui Xiong. 2021. Variable interval time sequence modeling for
career trajectory prediction: Deep collaborative perspective. InWWW.
[78] Chao Wang, Hengshu Zhu, Peng Wang, Chen Zhu, Xi Zhang, Enhong Chen, and Hui Xiong. 2021. Personalized and
explainable employee training course recommendations: A bayesian variational approach.ACM TOIS(2021).
[79] Chao Wang, Hengshu Zhu, Chen Zhu, Chuan Qin, and Hui Xiong. 2020. Setrank: A setwise bayesian approach for
collaborative ranking from implicit feedback. InAAAI.
[80] Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, and Furu Wei. 2024. Multilingual E5 Text
Embeddings: A Technical Report.arXiv:2402.05672(2024).
[81] Xuhong Wang, Ding Lyu, Mengjian Li, Yang Xia, Qi Yang, Xinwen Wang, Xinguang Wang, Ping Cui, Yupu Yang, et al.
2021. Apan: Asynchronous propagation attention network for real-time temporal graph embedding. InSIGMOD.
[82] Wei Wu, Zhuoshi Pan, Kun Fu, Chao Wang, Liyi Chen, Yunchu Bai, Tianfu Wang, Zheng Wang, and Hui Xiong. 2025.
TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache
Selection. InEMNLP.
[83] Zhiping Xiao, Weiping Song, Haoyan Xu, Zhicheng Ren, and Yizhou Sun. 2020. TIMME: Twitter ideology-detection
via multi-task multi-relational embedding. InACM SIGKDD.
[84] Haoran Xin, Ying Sun, Chao Wang, and Hui Xiong. 2025. LLMCDSR: Enhancing Cross-Domain Sequential Recommen-
dation with Large Language Models.ACM TOIS(2025).
[85] Yijie Xu, Aiwei Liu, Xuming Hu, Lijie Wen, and Hui Xiong. 2025. Mark Your LLM: Detecting the Misuse of Open-Source
Large Language Models via Watermarking. InICLR 2025 Workshop on GenAI Watermarking.
[86] Yijie Xu, Huizai Yao, Zhiyu Guo, Pengteng Li, Aiwei Liu, Xuming Hu, Weiyu Guo, and Hui Xiong. 2025. You only need
4 extra tokens: Synergistic Test-time Adaptation for LLMs.arXiv preprint arXiv:2510.10223(2025).
[87] Xinyang Zhang, Yury Malkov, Omar Florez, Serim Park, Brian McWilliams, Jiawei Han, et al. 2023. TwHIN-BERT: A
Socially-Enriched Pre-trained Language Model for Multilingual Tweet Representations at Twitter. InACM SIGKDD.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.

Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media 35
[88] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junkun
Zhang, Zican Dong, et al. 2023. A Survey of Large Language Models.arXiv:2303.18223(2023).
[89] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li,
Dacheng Li, Eric Xing, et al. 2023. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. InNeurIPS.
[90] Hongkuan Zhou, Da Zheng, Israt Nisa, Vasileios Ioannidis, Xiang Song, and George Karypis. 2022. TGL: A General
Framework for Temporal GNN Training on Billion-Scale Graphs.arXiv:2203.14883(2022).
Received 18 March 2024; revised 10 October 2025; accepted 22 July 2026
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: August 2026.
