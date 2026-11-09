---
title: Opinion Dynamics Models for Sentiment Evolution in Weibo Blogs
url: https://arxiv.org/abs/2511.15303
category: social-media
subcategory: empirical
date: 2025-11
venue: ''
authors:
- Yulong He
- Anton V. Proskurnikov
- Artem Sedakov
source: arxiv
pdf_url: https://arxiv.org/pdf/2511.15303
pages: 14
chars: 69143
fetched_at: '2026-11-08T13:01:13+00:00'
kb_version: 1
---

# Opinion Dynamics Models for Sentiment Evolution in Weibo Blogs

1
Opinion Dynamics Models for
Sentiment Evolution in Weibo Blogs
Yulong He, Anton V. Proskurnikov,Senior Member, IEEE, and Artem Sedakov
✦
Abstract—Online social media platforms enable influencers to dis-
tribute content and quickly capture audience reactions, significantly
shaping their promotional strategies and advertising agreements. Un-
derstanding how sentiment dynamics and emotional contagion unfold
among followers is vital for influencers and marketers, as these pro-
cesses shape engagement, brand perception, and purchasing behavior.
While sentiment analysis tools effectively track sentiment fluctuations,
dynamical models explaining their evolution remain limited, often ne-
glecting network structures and interactions both among blogs and
between their topic-focused follower groups. In this study, we tracked
influential tech-focused Weibo bloggers over six months, quantifying
follower sentiment from text-mined feedback. By treating each blogger’s
audience as a single “macro-agent”, we find that sentiment trajectories
follow the principle of iterative averaging – a foundational mechanism in
many dynamical models ofopinion formation, a theoretical framework
at the intersection of social network analysis and dynamical systems
theory. The sentiment evolution aligns closely with opinion-dynamics
models, particularly modified versions of the classical French–DeGroot
model that incorporate delayed perception and distinguish between
expressed and private opinions. The inferred influence structures reveal
interdependencies among blogs that may arise from homophily, whereby
emotionally similar users subscribe to the same blogs and collectively
shape the shared sentiment expressed within these communities.
1 INTRODUCTION
Emotional contagion – the transfer of emotional states be-
tween individuals – has been extensively studied in social
psychology and supported by numerous experiments [1]–
[5]. Social media platforms, with their multimodal com-
munication (text, images, video), enable rapid emotional
diffusion, making them ideal for studying contagion. Emo-
tions expressed in posts influence users, with homophily
amplifying this effect by connecting emotionally similar
individuals [6] who often subscribe to the same blogs and
channels, forming new communication pathways. Platforms
like Facebook, YouTube, Weibo, and Twitter provide power-
ful tools for analyzing these dynamics [7]–[10].
As users gain popularity and become influencers, they
become more sensitive to audience feedback, which shapes
their self-promotion strategies and advertising agreements.
Managing emotional contagion is crucial: understanding
how emotions spread among followers and how sentiment
Yulong He and Artem Sedakov are with St. Petersburg State Univer-
sity, St. Petersburg, Russia 199034{st065924@student.spbu.ru;
a.sedakov@spbu.ru.
Anton V . Proskurnikov is with Politecnico di Torino, Turin, Italy, 10129
anton.p.1982@ieee.org.
evolves in response to content helps influencers sustain en-
gagement, protect their public image, and optimize promo-
tions. These dynamics are also central to online marketing
and brand management, offering insights into how emo-
tions drive consumer behavior and brand adoption [11]. Ad-
ditionally, tracking emotional dynamics in public discourse
– especially during crises like the COVID-19 pandemic – is
vital for effective public health communication [12], [13].
Modeling Emotions via Sentiments and Opinions
In computational models of emotion, discrete states – such
as anger, fear, joy, or excitement – are often represented as
points in a two-dimensional [14] or three-dimensional [15]
affective space, defined by valence (pleasure), arousal (ac-
tivation), and optionally, dominance. This representation
supports various dynamical models of emotional contagion,
which describe how emotions evolve through interactions in
social networks [16]. As noted in [17], applying and validat-
ing these models remains challenging even in small groups,
due to technical and ethical constraints, especially given that
emotions are inherently internal and short-lived [18], [19].
In view of these challenges, emotional dynamics in large-
scale social media are typically examined through observ-
able fluctuations insentiments[11], [20] – enduring attitudes
or beliefs that accumulate and integrate transient emotional
states. While there is no consensus on the exact definition of
sentiment in philosophical and psychological literature [19],
in text processing the term generally refers to a scalar value
representing the emotional tone of a text or the writer’s atti-
tude toward a specific issue, which can be positive, negative,
or neutral. Specialized tools for sentiment extraction [21]–
[24] make it possible to trace sentiment dynamics at scale
in social media. From a modeling perspective, sentiment
can be viewed as a special case ofopinion, as defined in
sociology [25], sociophysics [26], economics [27], [28], and
systems theory [29], [30]. However, research on sentiment
dynamics and opinion formation has evolved in parallel,
with limited integration between these fields.
In the literature on sentiment dynamics modeling, the
prevailing approach is macroscopic, emphasizing how sen-
timent distributions evolve across social groups over time.
Representative examples include a model inspired by pop-
ulation games [31], a kinetics-based framework proposed
by Rey [32], hidden Markov models capturing the joint
evolution of sentiment-topic distributions [33], and com-
partmental models adapted from epidemiology [7], [8], [34].
arXiv:2511.15303v1  [cs.SI]  19 Nov 2025

2
In a parallel line of research, opinion formation models
have been actively developed over the past decades [25]–
[30], [35]–[38]. Beyond macroscopic approaches, this field
includes a broad class of microscopic, or agent-based, mod-
els rooted in foundational works such as French’s study of
social power [39] followed by DeGroot’s model of rational
consensus [40] and Abelson’s models of attitude dynam-
ics [41]. Even relatively simple linear models – such as the
Friedkin–Johnsen model [25], [35] – can reproduce complex
emergent behaviors observed in empirical settings and fit
experimental data [42], [43]. Tools from control theory and
signal processing facilitate efficient parameter learning and
prediction of long-term (asymptotic) behaviors [29], [38].
From a sociological perspective, the term “opinion” can
be broadly understood as an individual’s cognitive orienta-
tion toward an issue, person, or event [25]. In contemporary
opinion dynamics research, opinions are often modeled as
numerical variables that represent social actors (individuals
or groups) and evolve through social interactions. Sentiment
scores, which reflect the emotional states of individuals
and communities, can be interpreted as a continuous (real-
valued) opinion, 1 situating them within the framework of
opinion formation modeling in social groups.
Merging T wo Lines of Research: Objectives of This Work
Sentiments expressed by individual users or user groups
(e.g., subscribers to different blogs) on social media can
coevolve [46] due to social ties among users – an effect
that opinion dynamics models are well-equipped to capture.
A natural question arises: Can agent-based opinion for-
mation models – traditionally focused on decision-making,
and information spread rather than emotional contagion –
effectively capture sentiment trends, thereby offering a par-
simonious framework for modeling emotional dynamics?
This question motivates the present study. Modeling sen-
timent spread with parsimonious agent-based frameworks
offers both practical and theoretical advantages. If simple
models like the French–DeGroot or Friedkin–Johnsen mod-
els prove effective, they enable real-time, interpretable fore-
casting of collective mood shifts, valuable for marketers [11],
health authorities [13], and crisis managers [47]. Learning
influence structures also reveals key agents responsible for
sentiment shifts, supporting targeted interventions [36].
An early example of agent-based modeling is the seminal
work by Macropol et al. [48], which applied an averaging-
based model with time-varying activity-driven influence
matrices to political sentiment on Twitter. 2 Similarly, Das
et al. [50] validated a probabilistic averaging-based model
on Twitter data from vaccination debates, demonstrating its
capacity to capture sentiment evolution.
Contributions of This Work
We analyze the sentiment dynamics of subscribers to several
influential self-media blogs on Weibo, a leading Chinese mi-
croblogging platform. The platform offers convenient tools
1. Note that some works in sentiment analysis distinguish between
sentiments and opinions, defining an opinion, for example, as a pair
consisting of a sentiment (a real-valued score) and a discrete topic [44]
or a discrete attribute determined by the sentiment scores [45].
2. More recent work [49] further supports this view, demonstrating
that sentiment updates on VKontakte tend to follow patterns consistent
with iterative averaging.
for tracking user sentiment on specific topics over extended
periods; the typically short length of Weibo comments al-
lows for relatively accurate sentiment analysis.
The fan group of each influencer is modeled as a uni-
fied “macro-agent”, since subscribers are exposed to the
same content, topics, and interaction context. Aggregating
their responses captures the group’s collective emotional
orientation – its “opinion” – framing sentiment evolution
within the opinion dynamics paradigm. This approach is
supported by homophily [6], which promotes sentiment
alignment among like-minded users, and by echo chamber
effects [10], where repeated exposure to similar content
reinforces emotional convergence. Both effects are further
amplified by recommender algorithms [51] that prioritize
content matching users’ prior preferences, increasing intra-
group cohesion and reducing exposure to opposing views.
To compute the collective opinion, we gather comment
data from the fan groups of selected self-media bloggers,
reflecting followers’ subjective sentiments toward the blog-
gers’ posts on a specific topic of high visibility and longevity
– Huawei products. Huawei is a prominent domestic tech
brand that consistently generates high levels of user engage-
ment and discussion on social media. We collect comments
associated with these posts, extract primary comments (i.e.,
those responding directly to the blogger), and perform
sentiment analysis as described in Section 2. The collec-
tive opinion is then computed by averaging the sentiment
scores across followers. The time series describing senti-
ment evolution in each blog are then used to evaluate the
performance and applicability of linear opinion formation
models, as surveyed in Section 2.4. The choice of these
models is motivated by the observed averaging tendency in
the data – specifically, the non-expanding range of opinions
– and by the availability of well-established methodologies
for learning influence matrices [38], [52]. We show that while
the basic DeGroot [40] and Friedkin–Johnsen [25] models
fall short in capturing the dynamics of collective sentiment,
more advanced formulations that incorporate delay effects
and private (undisclosed) opinions [53] can approximate
these dynamics with sufficient accuracy.
Organization of the Paper
Section 2 presents the methodological and algorithmic as-
pects of our approach, including procedures for selecting the
most popular bloggers on Weibo, quantifying the audience
responses with sentiment analysis algorithms, and assessing
sentiment dynamics using opinion dynamics models. Sec-
tion 3 presents the main findings: a general tendency toward
averaging in the observed data and a comparative evalua-
tion of opinion formation models. Models that incorporate
private opinions demonstrate superior performance in fit-
ting the data compared to other classical opinion dynamics
models and exhibit considerable predictive power. Section 4
concludes the paper. Technical details on sentiment analysis
algorithms are provided in the Appendix.
2 METHODS ANDIMPLEMENTATIONASPECTS
This section describes our methodology and its implemen-
tation, with a focus on data collection and the application of
opinion formation models, including parameter estimation.

3
2.1 Influencers and the Followers’ Reactions
Weibo’s user-centric design enables a wide range of individ-
ual viewpoints on diverse topics over various time periods.
Users frequently share their sentiments and opinions in real
time as events unfold, making it well-suited for observing
sentiment dynamics over time. However, the platform’s
broad and varied content poses challenges for isolating
topic-specific posts and comments.
To indicate a blogger’s popularity, Weibo assigns aV
label to their profile and includes them in the V-influence
list.3 This curated list features 200 of the most influential ver-
ified bloggers in a given field. Rather than relying solely on
follower count, Weibo ranks bloggers based on a proprietary
“popularity” metric. The V-influence list (updated monthly)
serves as a benchmark for identifying bloggers who lead
trending discussions and engage millions of users daily.
For our experiments, we selected the top bloggers from
the V-influence list, based on the following criteria: (i) each
must be a media outlet or celebrity with a redVlabel; (ii)
their content must focus on the digital domain (chosen for
its topical neutrality); (iii) they must have at least 1,000,000
followers; and (iv) they must publish at least one Huawei-
related post every 15 days, containing either the keyword华
为or Huawei. Our sentiment analysis is based on top-level
comments rather than the bloggers’ posts themselves.
Of the selected bloggers, only seven met all the
specified criteria (Table 1). We identified them from
the V-influence list and crawled their blogs from
May 16 to November 15, 2023, 4 using the pattern
https://weibo.com/u/{blogger_id}.
TABLE 1: Selected Weibo bloggers, sorted by ID
#Blogger Blogger ID Followers
1科技小辛(Xiaoxin Technology) 1595443924 1.611M
2 李杰灵(Li Jieling) 1783497251 2.982M
3小白测评(Novice Evaluation) 2022252207 3.470M
4 数码疯报(Digital Crazy News) 2561744167 2.656M
5定焦数码(Fixed Focus Digital) 5821279480 1.072M
6 勇气数码君(Courage Digital Master) 7109370363 1.708M
7白问视频(Baiwen Video) 7239083016 1.105M
For each blog, Weibo provides access to a list of
posts along with detailed metadata, including the num-
ber of likes, 5 reposts, and comments (see Table 2). We
extract threads containing the previously specified Huawei-
related keywords, focusing exclusively ontop-levelcom-
ments. These comments capture users’ direct emotional
responses to the influencer’s original posts, rather than
interactions with other commenters.
2.2 Sentiment Analysis
Using a sentiment analysis algorithm, we compute a sen-
timent score for each of the selected comments, ranging
3. Ranking rules are available on https://v6.bang.weibo.com/rule
4. This period spans twelve 15-day intervals, each covering either the
1st-15th or 16th-end of the month. Notably, the Weibo API provides
access to historical data only for the past six months. Measuring
sentiment too frequently (e.g., daily) risks capturing intervals with no
Huawei-related posts, while overly infrequent sampling may not yield
sufficient data for effective model training and validation.
5. The likes (thumbs-up emoji) is the only form of emotional feedback
available on Weibo.
from0(maximally negative) to1(maximally positive).
Sentiment analysis algorithms, typically trained on
datasets like movie and product reviews, often perform
poorly on platforms like Weibo due to the abundance of
slang and platform-specific expressions. To find the most
suitable algorithm for this context, we evaluate several
approaches, including the Naive Bayes model for text clas-
sification [54], the BiLSTM model [55], [56], and a pre-
trained BERT model [57], specificallybert-base-chinese, 6 de-
signed for processing Chinese texts. We fine-tune the al-
gorithms on two publicly available sentiment annotation
datasets. Dataset 1 (ChnSentiCorp-Htl-ba-10000 7) consists of
hotel reviews scraped from https://trip.com, with labeled
sentiments organized into subsets of varying sizes. Dataset 2
(weibo senti 100k[58]) comprises manually labeled positive
and negative posts scraped from Weibo.
To compare different models, we use a manually labeled
2018 Weibo test dataset (see Appendix for technical details).
The BERT model fine-tuned on theweibo senti 100kconsis-
tently outperforms other approaches across standard met-
rics, making it the preferred choice for sentiment analysis
on Weibo blogs (Table 6). Here, we report the Receiver Op-
erating Characteristic (ROC) curves (Fig. 1), which visualize
the diagnostic ability of binary classifiers by plotting the
true positive rate against the false positive rate at various
classification thresholds. A higher area under the ROC curve
(AUC), a standard metric for evaluating sentiment analysis
algorithms, indicates superior overall performance across all
classification thresholds.
0.0 0.2 0.4 0.6 0.8 1.0
False positive rate
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0True positive rate
Naive Bayes model, AUC=0.6044
BiLSTM model, AUC=0.8071
BERT model (dataset 1), AUC=0.8672
BERT model (dataset 2), AUC=0.9469
Fig. 1: Sentiment analysis algorithms: ROC curves.
2.3 Collective Follower Sentiment (Opinion)
After computing sentiment scores for individual posts as
described above, we define the collectiveopinionof a blog’s
subscribers – treated as a single social actor – as the average
sentiment across all posts. The procedure for computing
collective opinion is formalized mathematically as follows.
Let influencers be indexed byB={1, . . . , B}, dis-
seminating content on a specific topic over time periods 8
T={1, . . . , T}. Since the content analyzed is largely
emotionally neutral (e.g., news about Huawei), the observed
6. https://huggingface.co/google-bert/bert-base-chinese.
7. https://ieee-dataport.org/open-access/chnsenticorp.
8. In our experiments, we setB= 7andT= 12.

4
TABLE 2: An extract from a dataset with posts by李杰灵(Li Jieling)
Post ID Post Date and time Likes Reposts Comments
. . . . . . . . . . . .
Msy8qEFGc #趣体. . .一起探索华为. . . 2023-02-11 19:40 1227 3498 1081
Mt0OgwLj3 #趣体. . .我带着华为学. . . 2023-02-14 20:40 2647 6085 1423
MuEs3o7b2兄弟们. . .搞一个华为光. . . 2023-02-25 15:25 619 25 251
Mv9TTmrT4 #趣看. . .次还有华为的. . . 2023-02-28 23:29 195 197 72
Mvx9b5qFR #谁是. . .只蹭了华为的. . . 2023-03-03 10:40 3978 4865 1715
MvH6a0RQz #趣体. . .半的华为Ma. . . 2023-03-04 12:00 384 667 173
. . . . . . . . . . . .
sentiment fluctuations are assumed to arise primarily from
emotional contagion among followers – either within a
single blog or across multiple blogs. Followers’ sentiment
is evaluated by analyzing the comments left in response to
the influencer’s posts. As noted earlier, we focus exclusively
on top-level comments, which respond directly to the influ-
encer’s original post rather than to other users.
In the subsequent text,P b(t)denotes the set of posts
by bloggerb∈ Bduring periodt∈ T. For each post
p∈ Pb(t), we identify the set of top-level commentsC p,b(t)
associated with this post. The Weibo platform supports only
one type of emotional reaction: the thumbs-up. We denote
byλ c(t)the number of thumbs-up votes on a top-level
commentcduring periodt, which serves as a measure of
how much support the comment receives from other users.
Similarly,λ p(t)denotes the number of thumbs-up reactions
received by a postpduring periodt, reflecting the perceived
importance of the blogger’s post within the Weibo audience.
Step 1.Each top-level commentc∈ C p,b(t)is evaluated
using a sentiment analysis algorithm (we use the BERT
model due to its superior performance), which assigns a
sentiment scoreσ c(t)∈[0,1]. As discussed earlier, a senti-
ment score of 0 represents completely negative sentiment,
while 1 corresponds to highly positive sentiment.
Step 2.The average sentiment of followers,σ p(t)∈[0,1],
toward a postp∈ Pb(t)is defined as the weighted average
of the sentiment scores expressed in top-level comments
during the specified period. The weights are proportional to
the number of thumbs-up reactions each comment receives:
σp(t) =
P
c∈Cp,b(t) λc(t)σc(t) P
c∈Cp,b(t) λc(t) , p∈ Pb(t), b∈ B, t∈ T.
A similar approach is used by [59] to assess the political
leanings of Twitter users during the 2012 U.S. election
cycle, where a user’s retweet approval score is calculated
by aggregating the scores of their peers, weighted by the
number of retweets they receive.
Step 3.Next, we define the followers’ sentiment re-
garding the entire topic-related content during periodt
as the weighted average of post-level sentiments, where
the weights are proportional to the number of thumbs-up
reactions each post receives:
σb(t) =
P
p∈Pb(t) λp(t)σp(t) P
p∈Pb(t) λp(t) , b∈ B, t∈ T.
This score reflects followers’ sentiment – not the influ-
encer’s own views – and is derived entirely from their feed-
back by aggregating top-level comments and then averaging
across posts. By selecting prominent blogs with consistent
topic coverage and high engagement, 9 and applying two-
stage averaging, we reduce algorithm-induced noise in in-
dividual sentiment estimates.
Fig. 2 presents the evolution of collective sentiments,
computed as described in Subsect. 2.3, over twelve 15-day
periods. The data show an overall positive 10 attitude of the
subscribers towards the bloggers’ posts, with an average
score of 0.6263 across all bloggers and time intervals.
1 2 3 4 5 6 7 8 9 10 11 12
0.4
0.5
0.6
0.7
0.8
Period,t
Observed sentiments,σ b(t)
σ1(t) σ2(t) σ3(t) σ4(t)
σ5(t) σ6(t) σ7(t)
Fig. 2: Observed collective sentiments in seven blogs.
2.4 Opinion Dynamics Models
Assigning the sentiment scoreσ b(t)to blogblinks senti-
ment analysis to opinion dynamics by treating the blog –
comprising an influencer and their audience – as a collec-
tive social actor. We interpret this sentimentσ b(t)as the
actor’s collective opinion at periodt. Below, we provide a
brief description of the models under consideration that are
summarized (in a compact matrix form) in Table 3.
The models operate on a discrete time scale, aligning
naturally with observations spaced at fixed time intervals.
Iterative Averaging of the Sentiments
While there is no widely accepted agent-based model for
sentiment dynamics in the literature, we begin by testing the
most basic class of opinion formation models, rooted in the
well-known French–DeGroot (FDG) and Friedkin–Johnsen
(FJ) frameworks [25], [38]–[40].
9. Posts receive 60-70 top-level comments and 800+ likes on average.
10. Recall that the scores of 0 and 1 correspond, respectively, to a
maximally negative and a maximally positive audience attitudes.

5
The FDG model:At each step, an agent’s updated
opinion is a (weighted) average of the current opinions:
xb(t+ 1) =
X
k∈B
wbkxk(t), b∈ B,(1)
starting from some initial valuesx b(1). Here the weights
wbk form a row-stochastic matrix11 W, reflecting the relative
influence of agentkon agentb. The FDG model serves as
a basic framework for multi-agent consensus, as opinions
ultimately converge in generic scenarios, e.g., whenWis
irreducible and aperiodic [40] (more generally, when its
graph has a directed spanning tree [60]). Hence, the FDG
model is insufficient to capture social dynamics, exhibiting
persistent disagreement is common over long time intervals.
The FJ model:The FJ model extends the FDG frame-
work by introducing agents who are “anchored” toinnate
opinions12 zb, incorporating these fixed predispositions into
every step of the opinion update process:
xb(t+ 1) =s b
X
k∈B
wbkxk(t) + (1−s b)zb, b∈ B.(2)
The coefficients b ∈[0,1]represents an agent’s suscepti-
bility to social influence, while the complementary quantity
1−s b captures their anchorage to innate opinion, keeping
their individual memory. In generic scenarios, e.g., when
the influence matrixWis irreducible and at least one agent
retains memory (sb <1) – the opinion vector converges to a
unique equilibrium, which generally exhibits disagreement
or polarization rather than consensus [25].
Comparing the FDG and FJ models, one observes that
the former serves as a deterministic analogue of a Markov
chain: each agent’s next opinion depends solely on previous
opinions. The FJ model, by contrast, allows agents to retain
memory of their innate opinionsz b indefinitely, introducing
persistent influence absent in the FDG framework. The
dynamics of sentiments plausibly exhibit memory, as further
supported by the analysis of opinion range dynamics in
the next section. First, some users’ reactions may be de-
layed, as comments are often formed in response to posts
or comments from earlier periods. Consequently, the com-
puted collective sentiment reflects users’ attitudes toward
the blogger’s past activity rather than recent content alone.
Second, Weibo’s recommendation algorithm analyzes users’
past behavior and promotes content accordingly, reinforcing
sentiment persistence over time. However, in rapidly evolv-
ing social media – where blogs can gain and lose millions of
subscribers – it is not obvious whether collective sentiments
can remain indefinitely anchored to fixed memories.
The FDGM model:For this reason, we explore an
extension of the FDG model (1) that allows agents to retain
memory, but only over a finite number of steps. This model,
termed FDGM (the French–DeGroot model with memory),
11. That is, all entries of the matrix are nonnegativew bk ≥0, and
each of its rows sums to 1.
12. In the original FJ model [61], the innate opinionz b of agentbis
typically taken as their initial opinion, which preserves some memory
of past influences on the group. In contrast, unlike in experiments
validating the FJ model [42], [43], [61], we do not observe sentiment
dynamics from the inception of the blog; consequently, the true initial
opinions cannot be directly measured.
resembles the structure of the FJ model; however, the static
innate opinion is replaced by the agent’s previous opinion:
xb(t+ 1) =s b
X
k∈B
wbkxk(t) + (1−sb)xb(t−τ), b∈ B.(3)
T wo-Layer Averaging Models
Models of opinion dynamics derived from the FDG frame-
work typically assume that agents receive the exact opin-
ions of their peers. Recently, models have been proposed
that relax this assumption by incorporating a discrepancy
between private and expressed opinions. In these models,
individuals maintain private beliefs that remain hidden,
while their publicly expressed opinions reflect both personal
convictions and social pressures, such as conformity to
perceived public opinion or a desire for social approval, as
demonstrated in the Asch conformity experiments [53], [62].
Although the opinion in our experiment represents not
an individual view but the collective sentiment of a blog’s
audience, one may argue that publicly expressed sentiments
still do not fully capture users’ true opinions, being shaped
instead by public influence – for example, liking or reposting
a post simply because many others have already done so
(“bandwagon behavior”). In view of this, we consider the
EPO (expressed-private opinion) model from [53], which
naturally extends the FDG framework by assigning each
“macro-agent” two opinions: a private opinionx b(t)rep-
resenting the unobserved genuine sentiment of the blog’s
audience, and an expressed opinionx e b(t)≡σ b(t)identified
with the observed collective sentiment.
The EPO model:The EPO model from [53] follows the
structure of the FJ model, allowing the agents’ anchorage
to static innate opinionsz b. The private and expressed
opinions of each agentb∈ Bevolve as follows
xb(t+ 1) =s bwbbxb(t) +s b
X
k̸=b
wbkxe k(t) + (1−s b)zb,
xe b(t) =φ bxb(t) + (1−φ b) X
k̸=b
abkxe k(t−1). (4)
Compared to the FJ model, the EPO model involves two
additional parameters: the coefficientsφ b ∈[0,1]and the
matrixA. Whenφ b = 1for allb, the second equation in
(4) becomes redundant, and the EPO model reduces to the
standard FJ model. In general, the second equation describes
the “visible” (expressed) layer of opinion formation: the
expressed opinion of each agent arises as a weighted av-
erage of their genuine (private) opinion and the expressed
opinions of their peers. In our context, where peers represent
other blogs in the network, the coefficientφ b regulates the
extent to which the blog’s audience expresses their authentic
sentiment, while1−φ b measures the extent to which they
conform to the opinions of the others. The expressed opinion
of agentkinfluences peerb(whereb̸=k) in two ways:
through weightw bk in the private opinion dynamics (the
“hidden” layer of opinion formation) and through weight
abk in the expressed opinion dynamics.
As discussed in [53], the matricesAandWare likely to
encode the same influence graph and should therefore be
compatible, in the sense thata bk >0(forb̸=k) if and only
ifw bk >0. Rather than enforcing this equivalence directly
– which would introduce numerous nonlinear constraints –

6
TABLE 3: The opinion dynamics models under consideration (in experiments, we test lagsτ= 1andτ= 2).
Model Name Dynamics and V ariables Parameters and Constraints
FDG model x(t+ 1) =W x(t), xb =σ b :sentiment in blogb∈ B W:row-stochastic matrix
FJ model x(t+ 1) =SW x(t) + (I−S)z, xb =σ b :sentiment in blogb∈ B W:row-stochastic matrix, S:diagonal matrix with values in[0,1], z:constant vector with values in[0,1]
EPO model
x(t+ 1) =S(diag(W)x(t) + (W−diag(W))x e(t))
+ (I−S)z,
xe(t) = Φx(t) + (I−Φ)Ax e(t−1),
xe b =σ b :sentiment in blogb∈ B
xb :private opinion in the blog (hidden)
W, A:nonnegative row-stochastic matrices,
S,Φ, D:diagonal matrices with values in[0,1]
withW=D+ (I−D)A,
z:constant vector with values in[0,1]
Reduced
EPO model
(S=I)
x(t+ 1) =diag(W)x(t) + (W−diag(W))x e(t),
xe(t) = Φx(t) + (I−Φ)Ax e(t−1),
xe b, xb :same as in the EPO model
W, A:nonnegative row-stochastic matrices,
Φ, D:diagonal matrices with values in[0,1]
withW=D+ (I−D)A
FDGM model
with lagτ
x(t+ 1) =SW x(t) + (I−S)x(t−τ),
xb =σ b :sentiment in blogb∈ B
W:nonnegative row-stochastic matrix,
S:diagonal matrix with values in[0,1]
EPO model
with lagτ
x(t+ 1) =S(diag(W)x(t) + (W−diag(W))x e(t))
+ (I−S)z,
xe(t) = Φx(t) + (I−Φ)Ax e(t−τ−1),
xe b, xb :same as in the EPO model
same as in the EPO model
Reduced
EPO model
with lagτ
x(t+ 1) =diag(W)x(t) + (W−diag(W))x e(t),
xe(t) = Φx(t) + (I−Φ)Ax e(t−τ−1),
xe b, xb :same as in the EPO model
same as in the reduced EPO model
we impose the structural restrictionW=D+ (I−D)A,
whereD=diag(d 11, . . . , dBB )with entriesd bb ∈[0,1].
This parameterization has a natural interpretation: the in-
fluence weightsw bk anda bk are proportional, withw bk =
(1−d b)abk forb̸=k, where1−d b serves as the proportion-
ality coefficient. Whend bb <1, the compatibility condition
wbk >0⇐ ⇒a bk >0holds automatically for all pairs
b̸=k. The cased bb = 1corresponds to an “internally
stubborn” agent whose private opinion is decoupled from
peer influence:x b(t+ 1) =s bxb(t) + (1−s b)zb.
The Reduced EPO Model:As discussed above, in the
rapidly changing Weibo environment where influencers ac-
quire and lose millions of subscribers, the relevance of long-
term memory – represented by innate opinionszb – becomes
uncertain. In view of this, we consider a reduced form of the
EPO model, corresponding tos b = 1. While the full EPO
model extends the classical FJ framework (and reduces to it
whenφ b = 1), the reduced EPO generalizes the FDG model.
The EPO model with time lag:In a similar spirit to
the FDGM models, we consider modifications of both the
full and reduced EPO models that incorporate delayed
expressed opinions (time lag), replacing the vectorx e(t)
withx e(t−τ), whereτ≥1.
2.5 Parameter Estimation
As is common in the identification of continuous-opinion
models [38], [63], we employ standard least-squares regres-
sion to estimate the unknown parameters. The procedure
is straightforward for the FDG and FJ models, where all
opinions are observed. For instance, for the FDG model, we
we minimize over the set of stochastic matricesWthe sum 13
XTest−1
t=1
∥x(t+ 1)−W x(t)∥ 2.
Parameter estimation in the EPO models is less straight-
forward, as it also involves the unobserved vectors of pri-
vate opinionsx(t). We therefore treatx(t)as additional
unknowns to be determined via least squares, along with
the parameter matrices. For instance, in the reduced (S=I)
EPO model, these unknowns are determined from the fol-
lowing optimization problem:
min
W,A,Φ,x(·)
XTest−1
t=1
Jt,
Jt =∥x(t+ 1)−diag(W)x(t)−(W−diag(W))x e(t)∥2
+∥x e(t+ 1)−Φx(t+ 1)−(I−Φ)Ax e(t)∥2.
HereAis a row-stochastic matrix with zero diagonal (a bb =
0for allb), andW=D+ (I−D)A, whereDandΦare
diagonal matrices with entries in[0,1]. Since the opinions
represent normalized sentiments, we constrain the private
opinions component-wise to[0,1], i.e.,x b(t)∈[0,1]for all
bandt. In the case of the full EPO model, the matrixS
and the innate opinion vectorzare also included among the
parameters to be estimated (see Table 3).
Finally, the time lagτin the FDGM and EPO models
further reduces the number of available observations for
estimation, with the summation starting fromt= 1 +τ.
13. The dataset coversT= 12periods, of which the firstT est = 10
are used for estimation and the final two for performance assessment.

7
1 2 3 4 5 6 7 8 9 10 11 12
−0.5
0
0.5
1
1.5
2
Period,t
µb(t, τ)
τ= 0
µ1(t, τ) µ2(t, τ) µ3(t, τ) µ4(t, τ) µ5(t, τ) µ6(t, τ) µ7(t, τ)
1 2 3 4 5 6 7 8 9 10 11 12
Period,t
τ= 1
1 2 3 4 5 6 7 8 9 10 11 12
Period,t
τ= 2
1 2 3 4 5 6 7 8 9 10 11 12
Period,t
τ= 3
Fig. 3: Functionsµ b(t, τ)under two scenarios: no delay in averaging (τ= 0) and with a delay in averaging for the first
three lags (τ= 1,2,3). The dashed lines indicate a 10% exceedance or shortfall of the admissible values.
3 THERESULTS
Before fitting the opinion dynamics models to data, we
notice one principal obstacle to applying the FDG model (1),
or any similar model that replacesWby a time-varying
matrix (e.g., the Hegselmann–Krause model or gossip-based
models [29]). Namely, the next-step opinions are weighted
averages of current ones. Consequently, the opinion range
(minimum-maximum) cannot expand, e.g., all opinions for
t >1must remain within the range observed att= 1.
A glance at Fig. 2 reveals that even this latter condition
is violated: the collective sentiments of the audiences of
blogs 1, 2, and 7 at some periods fall outside the range
of initially observed sentiments. We begin by computing
therange violation indicesthat quantify deviations of the
opinions from the previous-step range.
3.1 Range Violation Indices
To quantify deviations from the averaging rule, we compare
σb(t)with the previous period’s range[m(t−1), M(t−1)],
wherem(t−1) = min k∈B σk(t−1)andM(t−1) =
maxk∈B σk(t−1)are the minimum and maximum opinions
at the previous period. We define therange violation indexas
µb(t,0) := σb(t)−m(t−1) M(t−1)−m(t−1) , t≥1.
The dynamics of the variablesµ b(t,0)are shown in Fig. 3
(leftmost plot). The solid lines indicate the expected range
[0,1](i.e.,m(t−1)≤σ b(t)≤M(t−1)). As can be seen, the
sentiments of all blogs except blog 4 exceed this range by
10% or more at some steps (the violation is marked by the
dashed lines, corresponding to values of−0.1and1.1).
One explanation for this behavior, suggested by the ob-
served data, is that the opinion formation process involves a
time lag. Recall that an opinion here represents the collective
sentiment of a blog’s audience, reflecting the reactions of
all its subscribers. Although a 15-day sampling period may
seem sufficient, it is plausible that a significant fraction
of subscribers respond with delay. Moreover, since posts
and comments within each 15-day period are temporally
dispersed, some content appearing near the end of one
period may exert its full influence not in the current, but
only in subsequent periods, leading to opinions that appear
to violate the instantaneous averaging rule.
Extending the interval[m(t), M(t)]to an opinion range
that includes the previousτ≥1periods, we define
m(t, τ) = min
0≤h≤τ
min
b∈B
σb(t−h),
M(t, τ) = max
0≤h≤τ
max
b∈B
σb(t−h), t > τ,
and computing the corresponding range violation indices,
µb(t, τ) = σb(t)−m(t−1, τ) M(t−1, τ)−m(t−1, τ) , t > τ, b∈ B,
one may observe (Fig. 3) that most opinions satisfy the con-
ditionm(t, τ)≤σ b(t)≤M(t, τ)(equivalently,µ b(t, τ)∈
[0,1]) forτ= 2(two-step delay), and deviate by no more
than 10% from this range whenτ= 1(one-step delay).
On the other hand, time lag is not the only possible
explanation. Some sentiments leave the extended range at
certain steps, and this effect persists even as the delay
increases. This phenomenon may be explained by hidden
(unobservable) variables, such as the constant innate opin-
ions in the FJ model or evolving private opinions present in
the EPO model. In general, both time-lag effects and hidden
variables may operate simultaneously. This explains why
delayed EPO models exhibit good predictive performance.
3.2 Fitting the Averaging-Based Models
We identify the unknown parameters as described in
Section 2.5. Table 4 summarizes the models’ in-sample
goodness-of-fit and out-of-sample performance, measured
by Mean Absolute Error (MAE), Mean Absolute Percentage
Error (MAPE), and Root Mean Squared Error (RMSE). The
out-of-sample evaluation uses periods 11 and 12.
Anticipating the detailed comparison in the next subsec-
tion, we note some key findings. The delayed EPO models
exhibit the best in-sample fit, which aligns with our finding
from the range violation indices that audience sentiments
have lagged effects extending beyond the immediate next
period. At the same time, introducing delays directly into
the FDG model (as in the FDGM) does not significantly
improve in-sample performance, suggesting that the pres-
ence of unobserved latent variables is more important than

8
TABLE 4: Performance of the opinion dynamics models (best✓, competitive⋆).
Model Sum of MAE MAPE RMSE RMSE RMSE RMSE
residuals Periods 1–10 Period 11 Period 12 Periods 11–12
(in-sample) (out-of-sample) (out-of-sample) (out-of-sample)
FDG model 0.2000 0.1308 7.7957% 0.1461 0.1463 0.1927 0.1711
FJ model 0.1647 0.1257 7.5226% 0.1401 0.1330⋆0.1704 0.1529
EPO model 0.0773 0.1129 6.7539% 0.1319 0.1422 0.1563 0.1494
Reduced EPO model 0.0879 0.1161 6.9463% 0.1347 0.1346 0.1457⋆0.1402✓
FDGM model with lag 1 0.1754 0.1219 7.2959% 0.1423 0.1496 0.1512 0.1504
FDGM model with lag 2 0.1412 0.0987⋆5.8621%⋆0.1242⋆0.1238⋆0.1641 0.1454
EPO model with lag 1 0.0681⋆0.1222 7.3173% 0.1411 0.1335 0.1559 0.1451
Reduced EPO model with lag 1 0.0783 0.1277 7.6704% 0.1434 0.1347 0.1476⋆0.1413⋆
EPO model with lag 20.0530✓0.0883⋆5.2564%⋆0.1154⋆0.15840.1340✓0.1467
Reduced EPO model with lag 2 0.0639⋆0.0854✓5.0497%✓0.1114✓0.1208✓0.1641 0.1441⋆
memory effects. Interestingly, for out-of-sample prediction,
the undelayed reduced EPO model achieves the lowest
RMSE. Fig. 4 illustrates the observed and two-period-ahead
predicted sentiments using the reduced EPO model, demon-
strating the best predictive performance.
1 2 3 4 5 6 7 8 9 10 11 12
0.4
0.5
0.6
0.7
0.8
Period,t
Observed and predicted sentiments
xe 1(t) xe 2(t) xe 3(t) xe 4(t)
bxe 1(t) bxe 2(t) bxe 3(t) bxe 4(t)
xe 5(t) xe 6(t) xe 7(t)
bxe 5(t) bxe 6(t) bxe 7(t)
Fig. 4: Reduced EPO Model: Observed and two-period
ahead predicted sentiments,x e b(t) =σ b(t)and bxe b(t).
Further numerical details are presented in the exhibits
below. The numerical values of estimated parameters are
collected in Table 5. Fig. 5 shows the heatmaps and network
graphs for the fitted matrices cWand bA. Fig. 6 illustrates
the dynamics of fitted sentiments for each model. The next
subsection summarizes findings derived from these results.
3.3 Observations and Discussion
Sparsity:A first observation is that the fitted matri-
ces cW(and bAin EPO models) exhibit emergent sparsity
despite the absence of explicit sparsity constraints such
as a pre-specified influence graph 14 or sparsity-inducing
penalty terms in the cost function. Entries below<10 −5,
reported as zeros, are more than 1000 times smaller than
14. The dependency structure among blog audiences is unknown a
priori, and audience overlap cannot be determined since Weibo API
discloses only a small fraction of the subscribers for each blog.
the minimal non-zero entries, indicating a clear separation
between influential and negligible connections.
Single-layer averaging:The classical FDG model
predictably performs worst, as it both exhibits rapid con-
vergence to consensus (not observed in the sentiments) and
requires that the opinion range not expand over time (a con-
dition violated in our data; see Fig. 3). The FJ model, which
introduces constant “innate” opinions, slightly improves
performance but still predicts rapid convergence to equilib-
ria (Fig. 6) – a pattern not observed in the data. Meanwhile,
the FDGM model with lag2– which uses delayed opinion
vectors rather than static innate opinions – demonstrates
substantially better in-sample performance and ranks sec-
ond for one-step-ahead prediction. This suggests that single-
layer averaging models, inheriting the structure of the
FDG model, might be applicable for modeling sentiments;
however, time lag effects need to be accommodated. These
effects may differ across blogs: e.g., bS11 = 1for the FDGM
withτ= 2indicates that sentiment updates in blog1are not
influenced by lagged opinions from previous steps. Finally,
we note that the FDGM represents the minimal time-lagged
model. More generally, one could incorporate a sliding
window of past opinionsx(t−1), x(t−2), . . . , x(t−τ)rather
than a single lag, thereby introducing additional parameters.
Two-layer averaging:The EPO model, introducing
“hidden” opinions for each macro-agent, demonstrates high
consistency with the data, with performance improving
further when time lags are incorporated. This may appear
to be a simple consequence of increasing model complexity.
However, many of the additional parameters have negli-
gible influence. Beyond the emergent sparsity in cWand
bA, many rows of bAand variables bxe b are ineffective since
φbb = 1(which means that bxe b = bxb).
Even for the most complex EPO models (in terms of
parameters), good in-sample performance is not merely
overfitting, as evidenced by sustained out-of-sample perfor-
mance. For instance, the full EPO with lagτ= 2delivers
the best prediction for periodt= 12. However, reduced
EPO models (S=I,zineffective) match or outperform
full models despite having fewer parameters, with simi-
lar dependency structures (Fig. 5). Moreover, the delayed
(τ= 2) reduced EPO achieves the best in-sample and
one-step prediction, while the undelayed version excels
at two-step-ahead forecasts. This suggests the FJ “innate”
opinion mechanism is unnecessary; reduced EPO models,

9
generalizing the FDG model, suffice to describe sentiments.
The heatmaps in Fig. 5 show that the interblog in-
fluence graphs maintain similar structure across reduced
EPO models with best predictive performance: Bloggers 3
and 5 heavily influence their commenters, with strong inter-
content influence between Bloggers 2 and 6.
Interestingly, in many EPO models, the private opinion
layer remains unused or weakly influences public opinions.
We illustrate using the reduced EPO model, which achieves
the best out-of-sample RMSE (0.1402 for periods 11–12).
Except for Bloggers 3 and 5, users consistently express
genuine opinions ( bφb = 1forb̸= 3,5); for these two
bloggers, users provide authentic feedback in only∼85% of
cases. Furthermore, feedback for Bloggers 3, 5, and to some
extent 7 is primarily content-driven ( bw33 = 1, bw55 = 0.9271,
bw77 = 0.6664), contrasting sharply with Bloggers 1 and 4,
where sentiment is largely influenced by other bloggers
( bw11 = 0.0160, bw44 = 0.0206). Similar patterns across other
EPO models support the conclusion that users generally
express genuine opinions when commenting.
4 CONCLUSIONS ANDFUTUREWORKS
This work contributes to sentiment dynamics modeling on
social media by analyzing sentiment evolution on Weibo.
A fine-tuned BERT model (bert-base-chinese) captures and
quantifies follower sentiments in response to influencer
posts, offering insights into online community dynamics.
We analyze several influential bloggers (each with over one
million followers), tracking sentiment fluctuations toward
topic-specific content over twelve 15-day periods. These
sentiment values, interpreted as collective “opinions” of
each blog’s audience, exhibit clearaveragingdynamics: new
opinions consistently fall within the range of earlier values
(Fig. 3), sometimes with 1–2 period lags. This delay likely re-
flects asynchronous user engagement or responses to earlier
posts. Among several established opinion formation frame-
works we evaluated, a modification of the EPO (expressed-
private opinion) model best fit the data.
The alignment between empirical data and averaging-
based opinion dynamics models underscores their practical
value for capturing sentiment evolution. These parsimo-
nious models offer key advantages: they are interpretable,
well-established, and enable direct learning of influence
matrices from data using dynamical systems identification
tools [38]. Once calibrated, they support sentiment trajectory
prediction, identification of key influencers, and simulation
of targeted interventions. While our study focuses on Weibo
and Huawei-related content, the methodological framework
– sentiment extraction, user aggregation into macro-agents,
and model calibration via opinion dynamics – is topic-
agnostic and applicable to other subjects and platforms.
The two-level aggregation procedure could be refined – for
instance, by incorporating deeper comment levels.
Avenues for future research:First, more macro-
agents could be introduced, such as smaller blogs or in-
dividual users. While the identification procedure extends
in principle, this poses technical challenges. Expanding the
analysis requires longer time frames due to Weibo’s six-
month data retention and lower commenting frequency
in smaller blogs. Additionally, sentiment analysis noise
becomes more pronounced with smaller follower bases.
Individual sentiment estimation is particularly challenging
given variability in writing styles and expressive behaviors;
statistically meaningful insights emerge more reliably from
large-group aggregation. Finally, least squares identification
becomes computationally demanding as influence matrices
grow. We leave these challenges for future work.
Second, broader classes of dynamical models can be
considered. While we use deterministic opinion dynamics
with ordinary least squares (OLS) estimation, alternative
approaches for multivariate time series analysis – such as
vector autoregression (VAR), maximum likelihood estima-
tion (MLE), or Bayesian inference – are viable. Our OLS
approach effectively calibrates a low-order VAR model with
additional constraints (e.g., stochastic matrices). Relaxing
these constraints may improve predictive accuracy but sac-
rifices the guarantee that predictions remain in[0,1], which
is guaranteed by averaging-based models. Advanced sta-
tistical methods impose specific distributional assumptions,
whereas our approach requires only observational data.
While we prioritized compact models with minimal,
easily identifiable parameters, one could also employ ad-
vanced opinion formation models with nonlinear dynamics
(e.g., bounded confidence [37], biased assimilation [64])
or multiple delays (static or time-varying). However, such
extensions require specialized identification techniques, pre-
senting additional research challenges.
REFERENCES
[1] E. Hatfield, J. T. Cacioppo, and R. L. Rapson,Emotional Contagion.
Cambridge University Press, 1993.
[2] S. G. Barsade, “The ripple effect: Emotional contagion in groups,”
Administrative Science Quarterly, vol. 47, no. 4, pp. 644–675, 2002.
[3] S. G. Barsade, C. G. Coutifaris, and J. Pillemer, “Emotional con-
tagion in organizational life,”Research in Organizational Behavior,
vol. 38, pp. 137–151, 2018.
[4] C. Herrando and E. Constantinides, “Emotional contagion: A brief
overview and future directions,”Frontiers in Psychology, vol. 12, p.
712606, 2021.
[5] A. D. I. Kramer, J. E. Guillory, and J. T. Hancock, “Experimental
evidence of massive-scale emotional contagion through social
networks,”Proceedings of the National Academy of Sciences, vol. 111,
no. 24, pp. 8788–8790, 2014.
[6] H. Rosenbusch, A. M. Evans, and M. Zeelenberg, “Multilevel emo-
tion transfer on YouTube: Disentangling the effects of emotional
contagion and homophily on video audiences,”Social Psychological
and Personality Science, vol. 10, no. 8, pp. 1028–1035, 2019.
[7] F. Yin, X. Xia, X. Zhang, M. Zhang, J. Lv, and J. Wu, “Modelling the
dynamic emotional information propagation and guiding the pub-
lic sentiment in the Chinese Sina-microblog,”Applied Mathematics
and Computation, vol. 396, p. 125884, 2021.
[8] F. Yin, X. Xia, Y. Pan, Y. She, X. Feng, and J. Wu, “Sentiment
mutation and negative emotion contagion dynamics in social
media: A case study on the Chinese Sina microblog,”Information
Sciences, vol. 594, pp. 118–135, 2022.
[9] E. A. Meyer, P . Sandner, B. Cloutier, and I. M. Welpe, “High on
bitcoin: Evidence of emotional contagion in the YouTube crypto
influencer space,”Journal of Business Research, vol. 164, p. 113850,
2023.
[10] X. Song, S. Guo, and Y. Gao, “Personality traits and their influence
on echo chamber formation in social media: a comparative study
of Twitter and Weibo,”Frontiers in Psychology, vol. 15, p. 1323117,
2024.
[11] D. Liu, S. Zhang, and Q. Li, “The analysis of dynamic emotional
contagion in online brand community,”Frontiers in Psychology,
vol. 13, p. 946666, 2022.
[12] C. Crocamo, M. Viviani, L. Famiglini, F. Bartoli, G. Pasi, and
G. Carr ´a, “Surveilling COVID-19 emotional contagion on Twitter
by sentiment analysis,”European Psychiatry, vol. 64, no. 1, 2021.

10
TABLE 5: Fitted parameters estimated from periods 1–10. Entries are rounded to10 −5; zeros represent values<10 −5.
FDG model
cW=


0.0244 0.6763 0 0 0 0.2993 0
0 0.1924 0.0989 0 0.0589 0.6498 0
0 0.2177 0.3311 0 0.3025 0.1487 0
0 0.1601 0.7622 0 0.0777 0 0
0 0.1097 0 0 0.8903 0 0
0.2813 0.5685 0 0 0 0.1502 0
0 0.4987 0 0.0847 0.3206 0 0.0960


FJ model
cW=


0 1 0 0 0 0 0
0.1268 0.1422 0.1493 0.1554 0.1422 0.1756 0.1085
0.1051 0.6610 0 0.0029 0 0.2310 0
0 0.2920 0.6933 0 0.0147 0 0
0 0.2000 0 0 0.8000 0 0
0.1731 0.4940 0.2603 0 0 0 0.0726
0 0.3311 0 0 0.6689 0 0


bS=diag{ 0.4861,0,0.3347,0.5676,0.5509,0.6756,0.8905 }
bz= (0.6915,0.6590,0.5748,0.6026,0.5231,0.7394,1 )
FDGM model with lagτ= 1
cW=


0 0.6813 0 0 0 0.3187 0
0 0.1823 0.1652 0 0 0.6525 0
0 0.5703 0 0 0.4297 0 0
0 0.1496 0.8176 0 0.0328 0 0
0 0.7676 0 0 0.2324 0 0
0.4277 0.3967 0 0 0 0 0.1756
0 0.9052 0 0.0246 0.0702 0 0


bS=diag{ 1,1,0.4229,1,0.2877,0.6648,0.6756 }
FDGM model with lagτ= 2
cW=


0 0.6753 0 0 0 0.3247 0
0 0.3628 0 0 0 0.6372 0
0 0.2109 0.1405 0.3481 0.3004 0 0
0 0.3239 0.6637 0 0 0.0124 0
0 0.4657 0.4326 0 0.1017 0 0
0.3881 0.5609 0.0510 0 0 0 0
0 0.7242 0 0.2758 0 0 0


bS=diag{ 1,0.5977,0.5596,0.9146,0.3260,0.7275,0.7103 }
EPO model
cW=


0 1 0 0 0 0 0
0 1 0 0 0 0 0
0 0.5705 0.0789 0 0 0.3506 0
0 0.2846 0.7049 0.0106 0 0 0
0 0 0 0 1 0 0
0.1731 0.494 0.2603 0 0 0 0.0726
0 0 0 0 0 0 1


bA=


0 1 0 0 0 0 0
0.1383 0 0.174 0.1834 0.1646 0.2294 0.1102
0 0.6193 0 0 0 0.3807 0
0 0.2876 0.7124 0 0 0 0
0 1 0 0 0 0 0
0.1731 0.494 0.2603 0 0 0 0.0726
0 1 0 0 0 0 0


bD=diag{ 0,1,0.0789,0.0106,1,0,1 }
bΦ =diag{ 1,1,1,1,0.8158,1,0.6261 }
bS=diag{ 0.4861,0.0288,0.4628,0.5802,0.7539,0.6756,0.8456 }
bz= (0.6915,0.6579,0.5591,0.6016,0.5614,0.7394,0.8018 )
Reduced EPO model (S=I)
cW=


0.0160 0.6758 0 0 0 0.3082 0
0 0.4091 0 0 0.0211 0.5698 0
0 0 1 0 0 0 0
0 0.1506 0.7827 0.0206 0.0461 0 0
0 0.0729 0 0 0.9271 0 0
0 0.5585 0 0 0 0.4415 0
0 0.3336 0 0 0 0 0.6664


bA=


0 0.6868 0 0 0 0.3132 0
0 0 0 0 0.0356 0.9644 0
0 1 0 0 0 0 0
0 0.1537 0.7992 0 0.0471 0 0
0 1 0 0 0 0
0 1 0 0 0 0 0
0 1 0 0 0 0 0


bD=diag{ 0.0160,0.4091,1,0.0206,0.9271,0.4415,0.6664 }
bΦ =diag{ 1,1,0.8629,1,0.8510,1,1 }
EPO model with lagτ= 1
cW=


0.1271 0.8729 0 0 0 0 0
0 1 0 0 0 0 0
0 0.6043 0.0114 0 0 0.3843 0
0 0.6015 0.03 0.3686 0 0 0
0 0.6948 0 0 0.3052 0 0
0.13 0.51 0.3027 0 0 0.0217 0.0356
0 0 0 0 0 0 1


bA=


0 1 0 0 0 0 0
0.1759 0 0.1746 0.1616 0.1743 0.1797 0.1339
0 0.6113 0 0 0 0.3887 0
0 0.9525 0.0475 0 0 0 0
0 1 0 0 0 0 0
0.1329 0.5213 0.3094 0 0 0 0.0363
0 0 0 0 0 1 0


bD=diag{ 0.1271,1,0.0114,0.3686,0.3052,0.0217,1 }
bΦ =diag{ 1,1,1,1,1,1,0.4507 }
bS=diag{ 0.5294,0.0408,0.4494,0.4326,0.2815,0.6997,0.6546 }
bz= (0.687,0.6593,0.5583,0.6178,0.5255,0.7534,0.7391 )
EPO model with lagτ= 2
cW=


0 1 0 0 0 0 0
0 1 0 0 0 0 0
0 0 1 0 0 0 0
0.1640 0.8323 0 0.0037 0 0 0
0 0.6936 0 0 0.3064 0 0
0 0.5321 0 0 0 0.2784 0.1895
0 0.6193 0 0 0 0 0.3807


bA=


0 1 0 0 0 0 0
0.1767 0 0.1766 0.1659 0.1665 0.1865 0.1278
0.8348 0 0 0 0 0.1652 0
0.1646 0.8354 0 0 0 0 0
0 1 0 0 0 0 0
0 0.7374 0 0 0 0 0.2626
0 1 0 0 0 0 0


bD=diag{ 0,1,1,0.0037,0.3064,0.2784,0.380772 }
bΦ =diag{ 1,1,0.4858,0.7465,0.9771,1,1 }
bS=diag{ 0.4613,0.0791,0.8052,0.6506,0.2726,0.8619,0.5673 }
bz= (0.6811,0.6682,0.4374,0.5521,0.5319,0.7374,0.6821 )
Reduced EPO model with lagτ= 1
cW=


0.0943 0.6390 0 0 0 0.2667 0
0 0.3622 0 0 0 0.6378 0
0 0 1 0 0 0 0
0 0.2634 0.5478 0.1508 0 0.0380 0
0 0.0893 0 0 0.9107 0 0
0 0.5562 0 0 0 0.4438 0
0 0.5040 0 0.3012 0 0 0.1948


bA=


0 0.7056 0 0 0 0.2944 0
0 0 0 0 0 1 0
0.1648 0.1537 0 0.1673 0.2361 0.1734 0.1047
0 0.3102 0.6450 0 0 0.0447 0
0 0.9998 0.0001 0 0 0.0001 0
0.0001 0.9999 0 0 0 0 0
0 0.6259 0 0.3741 0 0 0


bD=diag{ 0.0943,0.3622,1,0.1508,0.9107,0.4437,0.1949 }
bΦ =diag{ 1,0.8170,1,1,1,1,1 }
Reduced EPO model with lagτ= 2
cW=


0.0258 0.6680 0 0 0 0.3062 0
0 0.3678 0 0 0 0.6322 0
0.1718 0 0.6286 0 0.1996 0 0
0 0.4676 0.5166 0.0155 0.0003 0 0
0.0495 0 0 0 0.9505 0 0
0 0.5212 0 0 0 0.3034 0.1754
0 0.7728 0 0 0 0 0.2272


bA=


0 0.6857 0 0 0 0.3143 0
0 0 0 0 0 1 0
0.4626 0 0 0 0.5374 0 0
0 0.4750 0.5247 0 0.0003 0 0
0.9997 0 0.0001 0 0 0 0.0002
0 0.7483 0 0 0 0 0.2517
0 1 0 0 0 0 0


bD=diag{ 0.0258,0.3678,0.6286,0.0155,0.9505,0.3034,0.2272 }
bΦ =diag{ 1,1,0.4608,0.7261,0.7869,0.9998,0.8164 }

11
FDG model FJ model FDGM model with lag 1 FDGM model with lag 2
0 0.2 0.4 0.6 0.8 1
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
EPO model EPO model with lag 1 EPO model with lag 2 Reduced EPO model Reduced EPO with lag 1 Reduced EPO with lag 2
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
1
2
3
45
6
7
Fig. 5: Fitted matrices cWand bAas heatmaps and their associated graphs.
[13] M. S. Ahmed, T. T. Aurpa, and M. M. Anwar, “Detecting sentiment
dynamics and clusters of Twitter users for trending topics in
COVID-19 pandemic,”PLoS ONE, vol. 16, no. 8, p. e0253300, 2021.
[14] J. A. Russell, “Core affect and the psychological construction of
emotion,”Psychological Review, vol. 110, no. 1, pp. 145–172, 2003.
[15] A. Mehrabian, “Pleasure-arousal-dominance: A general frame-
work for describing and measuring individual differences in tem-
perament,”Current Psychology, vol. 14, no. 4, pp. 261–292, 1996.
[16] E. S. van Haeringen, C. Gerritsen, and K. V . Hindriks, “Emotion
contagion in agent-based simulations of crowds: a systematic
review,”Autonomous Agents and Multi-Agent Systems, vol. 37, no. 6,
2023.
[17] E. S. van Haeringen, E. A. Veltmeijer, and C. Gerritsen, “Empirical
validation of an agent-based model of emotion contagion,”IEEE
Transactions on Affective Computing, vol. 15, no. 1, pp. 273–284, 2024.
[18] J. Deonna and F. Teroni,The Emotions: A Philosophical Introduction.
London: Routledge, 2008.
[19] I. Vendrell Ferran, “Emotions and sentiments: Two distinct forms
of affective intentionality,”Phenomenology and Mind, vol. 23, pp.
20–34, 2022.
[20] D. Naskar, S. R. Singh, D. Kumar, S. Nandi, and E. O. d. l.
Rivaherrera, “Emotion dynamics of public opinions on Twitter,”
ACM Trans. Inf. Syst., vol. 38, no. 2, Mar. 2020.
[21] P . Nandwani and R. Verma, “A review on sentiment analysis and
emotion detection from text,”Social Network Analysis and Mining,
vol. 11, no. 1, p. 81, 2021.
[22] W. Zhang, X. Li, Y. Deng, L. Bing, and W. Lam, “A survey on
aspect-based sentiment analysis: Tasks, methods, and challenges,”
IEEE Transactions on Knowledge and Data Engineering, vol. 35, no. 11,
pp. 11 019–11 038, 2023.
[23] H. Xu, M. Xu, X. Deng, and B. Wang, “Sentiment diffusion in
online social networks: A survey from the computational perspec-
tive,”ACM Computing Surveys, 2025.
[24] D. Rimpy, A. Dhankhar, and A. Dhankhar, “Sentimental analysis
of social networks: A comprehensive review (2018-2023),”Multi-
disciplinary Reviews, vol. 7, no. 7, p. 2024126, 2024.
[25] N. Friedkin, “The problem of social control and coordination of
complex systems in sociology: A look at the community cleavage
problem,”IEEE Control Syst. Mag., vol. 35, no. 3, pp. 40–51, 2015.
[26] H. Noorazar, “Recent advances in opinion propagation dynamics:

12
1 2 3 4 5 6 7 8 9 10
0.4
0.5
0.6
0.7
0.8
Period,t
Sentiments
FDG model
1 2 3 4 5 6 7 8 9 10
Period,t
FJ model
1 2 3 4 5 6 7 8 9 10
Period,t
FDGM model with lag 1
1 2 3 4 5 6 7 8 9 10
Period,t
FDGM model with lag 2
1 2 3 4 5 6 7 8 9 10
0.4
0.5
0.6
0.7
0.8
Period,t
Sentiments
EPO model
1 2 3 4 5 6 7 8 9 10
Period,t
EPO model with lag 1
1 2 3 4 5 6 7 8 9 10
Period,t
EPO model with lag 2
1 2 3 4 5 6 7 8 9 10
0.4
0.5
0.6
0.7
0.8
Period,t
Sentiments
Reduced EPO model
Blogger 1 Blogger 2 Blogger 3 Blogger 4 Blogger 5 Blogger 6 Blogger 7
1 2 3 4 5 6 7 8 9 10
Period,t
Reduced EPO model with lag 1
1 2 3 4 5 6 7 8 9 10
Period,t
Reduced EPO model with lag 2
Fig. 6: Sentiments for the parameters from Table 5. Transparent line: measured sentimentσ b; solid lines: model estimate bxe b.
A 2020 survey,”The European Physical Journal Plus, vol. 135, p. 521,
2020.
[27] M. Grabisch, A. Mandel, and A. Rusinowska, “On the design of
public debate in social networks,”Operations Research, vol. 71,
no. 2, pp. 626–648, 2023.
[28] L. Mastroeni, P . Vellucci, and M. Naldi, “Agent-based models for
opinion formation: A bibliographic survey,”IEEE Access, vol. 7,
pp. 58 836–58 848, 2019.
[29] A. Proskurnikov and R. Tempo, “A tutorial on modeling and
analysis of dynamic social networks. Part II,”Annu. Rev. Control,
vol. 45, pp. 166–190, 2018.
[30] B. D. Anderson, F. Dabbene, A. V . Proskurnikov, C. Ravazzi, and
M. Ye, “Dynamical networks of social influence: Modern trends
and perspectives,”IFAC-PapersOnLine, vol. 53, no. 2, pp. 17 616–
17 627, 2020.
[31] R. Franke, “Aggregate sentiment dynamics: A canonical modelling
approach and its pleasant nonlinearities,”Structural Change and
Economic Dynamics, vol. 31, pp. 64–72, 2014.
[32] J.-M. Rey, “A mathematical model of sentimental dynamics ac-
counting for marital dissolution,”PLoS ONE, vol. 5, no. 3, p. e9881,
2010.
[33] Y. He, C. Lin, W. Gao, and K.-F. Wong, “Dynamic joint sentiment-
topic model,”ACM Trans. Intell. Syst. Technol., vol. 5, no. 1, 2014.
[34] H. Chen, M. Liu, Y. Zhang, and H. Wang, “Research on propaga-
tion dynamics of emotional contagion using S3EIR model based
on multiple social media platforms,”Frontiers in Communication,
vol. 10, p. 1582974, 2025.
[35] X. Zhou, H. Sun, W. Xu, W. Li, and Z. Zhang, “Friedkin-Johnsen
model for opinion dynamics on signed graphs,”IEEE Transactions
on Knowledge and Data Engineering, vol. 36, no. 12, pp. 8313–8327,
2024.
[36] Q. He, H. Fang, J. Zhang, and X. Wang, “Dynamic opinion max-
imization in social networks,”IEEE Transactions on Knowledge and
Data Engineering, vol. 35, no. 1, pp. 350–361, 2023.
[37] C. Bernardo, C. Altafini, A. Proskurnikov, and F. Vasca, “Bounded
confidence opinion dynamics: A survey,”Automatica, vol. 159, p.
111302, 2024.
[38] C. Ravazzi, F. Dabbene, C. Lagoa, and A. V . Proskurnikov, “Learn-

13
ing hidden influences in large-scale dynamical social networks:
A data-driven sparsity-based approach, in memory of Roberto
Tempo,”IEEE Control Syst. Mag., vol. 41, no. 5, pp. 61–103, 2021.
[39] J. R. French Jr, “A formal theory of social power.”Psychological
review, vol. 63, no. 3, p. 181, 1956.
[40] M. H. DeGroot, “Reaching a consensus,”Journal of the American
Statistical Association, vol. 69, no. 345, pp. 118–121, 1974.
[41] R. Abelson, “Mathematical models of the distribution of attitudes
under controversy,” inContributions to Mathematical Psychology,
N. Frederiksen and H. Gulliksen, Eds. New York: Holt, Rinehart
& Winston, Inc, 1964, pp. 142–160.
[42] N. E. Friedkin, A. Proskurnikov, and F. Bullo, “Group dynamics on
multidimensional object threat appraisals,”Social Networks, vol. 65,
pp. 157–167, 2021.
[43] N. Friedkin, A. Proskurnikov, W. Mei, and F. Bullo, “Mathematical
structures in group decision-making on resource allocation distri-
butions,”Scientific Reports, vol. 5, no. 1, p. 1377, 2019.
[44] B. Liu,Sentiment Analysis: Mining Opinions, Sentiments, and Emo-
tions. Cambridge, UK: Cambridge University Press, 2015.
[45] Y. Lian and X. Dong, “An opinion dynamics model for unrelated
discrete opinions,”Knowledge-Based Systems, vol. 251, p. 109133,
2022.
[46] Q. Zhang, Z. Zhang, M. Yang, L. Zhu, and L. Yang, “Exploring
coevolution of emotional contagion and behavior for microblog
sentiment analysis: A deep learning architecture,”Complexity, vol.
2021, p. 6630811, 2021.
[47] B. Ilyas and A. Sharifi, “A systematic review of social media-based
sentiment analysis in disaster risk management,”International
Journal of Disaster Risk Reduction, vol. 123, p. 105487, 2025.
[48] K. Macropol, P . Bogdanov, A. K. Singh, L. R. Petzold, and X. Yan, “I
act, therefore I judge: Network sentiment dynamics based on user
activity change,” inProceedings of the 2013 IEEE/ACM International
Conference on Advances in Social Networks Analysis and Mining
(ASONAM), 2013, pp. 396–402.
[49] I. V . Kozitsin, “Formal models of opinion formation and their
application to real data: Evidence from online social networks,”
J. Math. Sociol., vol. 46, no. 2, pp. 120–147, 2022.
[50] R. Das, J. Kamruzzaman, and G. Karmakar, “Opinion formation
in online social networks: Exploiting predisposition, interaction,
and credibility,”IEEE Transactions on Computational Social Systems,
vol. 6, no. 3, pp. 554–566, 2019.
[51] E. Bakshy, S. Messing, and L. A. Adamic, “Exposure to ideologi-
cally diverse news and opinion on Facebook,”Science, vol. 348, no.
6239, pp. 1130–1132, 2015.
[52] S. M. Nematollahzadeh, S. Ozgoli, M. S. Haghighi, and A. Jolfaei,
“Learning influential cognitive links in social networks by a new
hybrid model for opinion dynamics,”IEEE Transactions on Compu-
tational Social Systems, vol. 8, no. 5, pp. 1262–1271, 2020.
[53] M. Ye, Y. Qin, A. Govaert, B. D. Anderson, and M. Cao, “An
influence network model to study discrepancies in expressed and
private opinions,”Automatica, vol. 107, pp. 371–381, 2019.
[54] F. Mosteller and D. L. Wallace, “Inference and disputed author-
ship: the federalist,”(No Title), 1964.
[55] M. Schuster and K. K. Paliwal, “Bidirectional recurrent neural
networks,”IEEE Transactions on Signal Processing, vol. 45, no. 11,
pp. 2673–2681, 1997.
[56] S. Hochreiter, “Long short-term memory,”Neural Computation
MIT-Press, 1997.
[57] J. Devlin, M. Chang, K. Lee, and K. Toutanova, “BERT: pre-training
of deep bidirectional transformers for language understanding,”
inProceedings of the 2019 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Tech-
nologies, NAACL-HLT 2019, J. Burstein, C. Doran, and T. Solorio,
Eds., 2019, pp. 4171–4186.
[58] M. Sun, “Weibo senti 100k and THUCnews,” 2022. [Online].
Available: https://dx.doi.org/10.21227/abj8-y636
[59] F. M. F. Wong, C. W. Tan, S. Sen, and M. Chiang, “Quantifying
political leaning from tweets, retweets, and retweeters,”IEEE
Transactions on Knowledge and Data Engineering, vol. 28, no. 8, pp.
2158–2172, 2016.
[60] A. Proskurnikov and R. Tempo, “A tutorial on modeling and
analysis of dynamic social networks. Part I,”Annu. Rev. Control,
vol. 43, pp. 65–79, 2017.
[61] N. E. Friedkin and E. C. Johnsen, “Social influence networks and
opinion change,”Adv. Group Processes, vol. 16, pp. 1–29, 1999.
[62] C. Zhao and E. Parilina, “Opinion dynamics in two-layer networks
with hypocrisy,”Journal of the Operations Research Society of China,
vol. 12, no. 1, pp. 109–132, 2024.
[63] H.-T. Wai, A. Scaglione, and A. Leshem, “Active sensing of social
networks,”IEEE Transactions on Signal and Information Processing
over Networks, vol. 2, no. 3, pp. 406–419, 2016.
[64] P . Dandekar, A. Goel, and D. T. Lee, “Biased assimilation, ho-
mophily, and the dynamics of polarization,”Proceedings of the
National Academy of Sciences, vol. 110, no. 15, pp. 5791–5796, 2013.
[65] R. S. Patil and S. R. Kolhe, “Supervised classifiers with TF-IDF
features for sentiment analysis of Marathi tweets,”Social Network
Analysis and Mining, vol. 12, no. 1, p. 51, 2022.
APPENDIX
To compare the models’ performance on Chinese social
media text, we use a manually labeled 2018 Weibo test
dataset.15 The algorithm performance is evaluated using
standard metrics such as accuracy, precision, recall, F1
score [65], and AUC. Results are summarized in Table 6.
The Naive Bayes Model:The implementation of this
model is based on theSnowNLP 16 library, specially designed
for processing of simplified Chinese text.
The BiLSTM Model:We utilize theKeras 17 library to
implement BiLSTM-based model the objective of enhancing
the accuracy and efficiency of text processing. The first layer
of the model is the embedding layer, which transforms
vocabulary indices into word vector matrices, a prerequisite
for utilizing neural networks to process textual data. Based
on the distribution of token length, as illustrated in Fig. 7,
the model is designed with an input sequence length of 107,
with each word represented as a 300-dimensional vector.
0 107 200 400 600 800 1000 1200 1400
T oken length
0.000
0.200
0.400
0.600
0.800
0.964
1.000
Fig. 7: The CDF of a token length.
The bidirectional layer allows the model to propagate in-
formation in both directions of the input sequence, thereby
improving its information extraction capability. The long
short-term memory (LSTM) layer serves as the core of
the model, while the dense layer maps lower-dimensional
representations to higher dimensions, ultimately producing
a one-dimensional output suitable for binary classification.
The structure of the model is summarized in Table 8.
The BERT Model:The model is implemented using the
Transformers library.18 We start from the pre-trained BERT
15. https://github.com/dengxiuqi/weibo2018.
16. https://github.com/isnowfy/snownlp.
17. https://github.com/fchollet/keras.
18. https://github.com/huggingface/transformers.

14
TABLE 6: Sentiment analysis algorithms: performance
Method Dataset Precision Recall F1 Accuracy AUC
Naive Bayesweibo senti 100k0.7444 0.8609 0.7984 0.7 0.6044
BiLSTMweibo senti 100k0.8950✓0.6174 0.7307 0.686 0.8071
BERTChnSentiCorp-Htl-ba-100000.8754 0.8145 0.8438 0.792 0.8672
BERTweibo senti 100k0.85310.9594✓0.9031✓0.858✓0.9469✓
TABLE 7: Theweibo senti 100kdataset
Label Review
. . . . . .
1 [给力]感谢所有支持雯婕的芝麻！[爱你]
1 2013最后一天，在新加坡开心度过，向所有的朋友们问声：新年快乐！2014年，我们会更好[调...
0大中午出门办事找错路，曝晒中。要多杯具有多杯具。[泪][泪][汗]
0马航还会否认吗？到底在隐瞒啥呢？[抓狂]//@头条新闻:转发微博
0克罗地亚球迷很爱放烟火！球又没进，就硝烟四起。[晕]
1 [抱抱]福芦TangRoulou吉祥书8.8折优惠>>>http://t.cn/z...
1回复@钱旭明QXM:[嘻嘻][嘻嘻] //@钱旭明QXM:杨大哥[good][good][g...
1人家这脸长的!!!!!![哈哈]
1这个价不算高，和一天内训相比相差无几。。[哈哈]//@博通传媒v: 6个月！一个月工资1万，...
0终于收工啦，脚丫子快冻掉了[泪][泪]
. . . . . .
TABLE 8: The structure of the BiLSTM model
Layer Type Output Shape Param #
Embedding (None, 107, 300) 58560600
Bidirectional (None, 107, 64) 85248
LSTM (None, 16) 5184
Dense (None, 1) 17
model, namelybert-base-chinese[57], which has been specif-
ically developed for processing Chinese language texts.
We fine-tune the pre-trained model using two sentiment
annotation datasets:ChnSentiCorp-Htl-ba-10000(Dataset 1)
andweibo senti 100k(Dataset 2) focusing on hotel reviews
and short Weibo texts, respectively. Theweibo senti 100k
dataset [58], illustrated by Table 7, contains over 100,000
anonymous pieces of Weibo text data with sentiment an-
notations. Approximately half of the texts are classified as
positive (label 1), and the other half as negative (label 0).
The fine-tuning process involves adjusting the pre-
trainedbert-base-chinesemodel to more accurately interpret
the sentiment-specific characteristics and patterns present
in the datasets. The objective is to create a model that not
only retains the robust language processing abilities of BERT
but also excels in identifying and categorizing sentiments
expressed in Chinese texts.
