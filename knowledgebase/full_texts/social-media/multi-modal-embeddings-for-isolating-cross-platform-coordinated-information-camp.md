---
title: Multi-Modal Embeddings for Isolating Cross-Platform Coordinated Information Campaigns on Social
  Media
url: https://arxiv.org/abs/2309.12764
category: social-media
subcategory: empirical
date: 2023-09
venue: ''
authors:
- Fabio Barbero
- Sander op den Camp
- Kristian van Kuijk
- Carlos Soto García-Delgado
- Gerasimos Spanakis
source: arxiv
pdf_url: https://arxiv.org/pdf/2309.12764
pages: 17
chars: 42552
fetched_at: '2026-11-08T13:01:45+00:00'
kb_version: 1
---

# Multi-Modal Embeddings for Isolating Cross-Platform Coordinated Information Campaigns on Social Media

Multi-Modal Embeddings for Isolating
Cross-Platform Coordinated Information
Campaigns on Social Media
Fabio Barbero, Sander op den Camp, Kristian van Kuijk [0009−0008−3013−8760],
Carlos Soto Garc ´ ıa-Delgado, Gerasimos Spanakis[0000−0002−0799−0241], and
Adriana Iamnitchi[0000−0002−2397−8963]
Department of Advanced Computing Sciences
Maastricht University, The Netherlands
{fabio.barbero,sjgm.opdencamp,kristian.vankuijk,
c.sotogarciadelgado}@student.maastrichtuniversity.nl
{jerry.spanakis,a.iamnitchi}@maastrichtuniversity.nl
Abstract. Coordinated multi-platform information operations are im-
plemented in a variety of contexts on social media, including state-
run disinformation campaigns, marketing strategies, and social activism.
Characterized by the promotion of messages via multi-platform coordi-
nation, in which multiple user accounts, within a short time, post con-
tent advancing a shared informational agenda on multiple platforms,
they contribute to an already confusing and manipulated information
ecosystem. To make things worse, reliable datasets that contain ”ground
truth“ information about such operations are virtually nonexistent. This
paper presents a multi-modal approach that identifies the social media
messages potentially engaged in a coordinated information campaign
across multiple platforms. Our approach incorporates textual content,
temporal information and the underlying network of user and messages
posted to identify groups of messages with unusual coordination pat-
terns across multiple social media platforms. We apply our approach to
content posted on four platforms related to the Syrian Civil Defence or-
ganization known as the White Helmets: Twitter, Facebook, Reddit, and
YouTube. Results show that our approach identifies social media posts
that link to news YouTube channels with similar factuality score, which
is often an indication of coordinated operations.
Keywords: Coordinated Campaigns · Information Operations · Social
media · White Helmets
1 Introduction
While social media platforms may be independently attempting to detect ne-
farious information campaigns within their own platforms, the problems due to
multi-platform coordination are not likely to be addressed in the current envi-
ronment of legislature void and platforms’ competition for user attention.
arXiv:2309.12764v1  [cs.SI]  22 Sep 2023

2 F. Barbero et al.
Previous research has shown that information operations online are now much
more sophisticated than networks of coordinated bots that (re)broadcast some
messages. Instead, such coordinated efforts i) are concurrently deployed on multi-
ple social and alternative news media platforms [19,14]; ii) promote the intended
message by means specific to each platform (such as videos on YouTube and writ-
ten news or opinion articles on alternative media websites) [26,9]; iii) amplify the
same message by repeating it in altered forms (such as including the same video
footage in multiple videos posted on different channels on YouTube) [19,9]; and
iv) amplify the same content via platform-specific affordabilities, such as retweet-
ing on Twitter vs. liking/commenting on YouTube to possibly manipulate the
platform’s content promotion algorithms [17,9].
Due to limited datasets on such covert, often undetected operations, previous
research focused on specific contexts (for example, the Russian Internet Research
Agency’s engagement in influencing the US 2016 elections) and on single plat-
forms, typically the promotion of specific URLs on Twitter. Yet coordinated
online information campaigns continue to be employed by various state, busi-
ness, or social actors for various purposes, from disinformation and monetization
to activism and public health campaigns. Although some are carried out by le-
gitimate groups or individuals, many campaigns may be supported by entities
with undisclosed motivations, such as foreign governments or political parties,
and may not be transparent about their underlying goal [26,17,20]. While so-
cial media platforms reacted to some of such problems and typically blocked
accounts seen to engage in coordinated information operations [1], coordinated
operations deployed on multiple platforms can escape the vigilance of individual
platforms if they keep a low profile on any particular platform.
This paper proposes a methodology that, given a multi-platform collection of
social media posts, identifies a subset of such posts that are likely to be part of a
coordinated information campaign and clusters them based on content and post-
ing time locality. Clusters with only one post are likely to represent messages that
do not participate in a coordinated campaign, thus ignoring them can reduce
the dataset that needs to be further analysed by human operators or via com-
putational means. We show on a multi-platform datasets that includes content
posted on Twitter, Facebook, Reddit and YouTube that by using multi-modal
approaches (text, network structures, and time) we can identify similar messages
that not only link to the same URL (as previous work has been done) but link to
different URLs of similar factuality as reported by the Media Bias/Fact Check
website1. In the lack of ground-truth datasets that clearly mark which messages
are part of a coordinated operation, we use agreement on factuality within a
cluster as a performance metric.
Our approach can work on diverse combinations of platforms and on diverse
topics without the requirement to identify whether messages are factual or not.
This generality is due to the design of our approach that: 1) considers only mes-
1 https://mediabiasfactcheck.com/

Cross-Platform Coordinated Campaigns 3
sages that introduce new information on the platform (e.g., tweets on Twitter
but not retweets; posts and comments on Reddit, etc.), thus not depending on
platform-specific message promotion algorithms or platform-specific functionali-
ties; 2) it detects coordination in the absence of shared tokens (such as hashtags
or URLs). However, our technique works under the assumptions that coordi-
nated campaigns push syntactically similar (but not identical) messages within
a short interval of time.
2 Related Work
Intentional spread of fake news with political or financial objectives has been
studied for cases such as Brexit[7], COVID-19 [8] [11] and the Syrian War [5].
Sometimes, these fake news are known to be posted and promoted by bots [14].
The behaviour of these bots has been studied, and different datasets exist for
their activity on platforms such as Twitter [10] [24].
Furthermore, such campaigns are also known to often be coordinated. One of the
first studies was performed by Ratkiewicz et al. [22]. They describe a machine
learning framework that combines topological, content-based and crowdsourced
features of information diffusion networks to detect the early stages of viral
spreading of political misinformation. Sharma et al. [25] investigates user ac-
tivity embeddings to find coordination between accounts and is trained using
labelled data. Because labelled data are not always available, others have looked
at unsupervised clustering methods. Fazil and Abulasih [13], Pachero et al. [21]
and Magelinski et al. [18] all explored creating a user network based on similari-
ties in user profiles, activity, or post content. They cluster the resulting network
to identify groups of users showing signs of coordination. These methods have
each focused on one category of features but have not looked much at combin-
ing different modalities. In addition, all of them use only single-platform data
collected from Twitter.
However, there is significant evidence to suggest that these coordinated cam-
paigns do not limit themselves to only one social media platform. Lukito et
al. [17] explore the activity of the Internet Research Agency (IRA), a Russian
company engaged in online propaganda and influence operations, on three so-
cial media platforms, Facebook, Twitter, and Reddit, to understand how the
activities on these sites were temporally coordinated. NG et al. [19] studied how
coordinated campaigns occurred for the White Helmets across YouTube, Face-
book and Twitter, and how they can exhibit certain patterns when studying
time and relationships between users and posts. Our paper uses multi-modal
data (text, network structures and time) to identify likely coordinated groups
that post similar content in a synchronized manner on multiple platforms.

4 F. Barbero et al.
3 Datasets
One topic known to have been part of information campaigns is the White Hel-
mets [19]. The White Helmets (WH) [2] is a volunteer organization that operates
in rebel held areas of Syria. They perform medical evacuation, urban search and
rescue in response to bombing, evacuation of civilians from danger areas and
often publish videos showing the human impacts of the conflict. The WH is
known to have been a target of information campaigns by supporters of the Syr-
ian president Bashar al-Assad and Russian state-sponsored media organizations
such as Russia Today (RT) and Sputnik, for instance, accusing the WH of faking
evidence of atrocities or organ-harvesting racket [3].
For this paper, we used data from the White Helmet campaign as described
in [19], which we expanded with our collection of Reddit data and augmented
with factuality scores from Media Bias/Fact Check. This dataset was originally
built by collecting YouTube videos that include ”White Helmets” in different
languages in the video’s title or description. The videos identified this way were
posted between September 2006 and April 2019. Each video is uniquely identified
by a video ID and contains information on the video title, video channel name,
published time and video captions (which can be automatically generated by
YouTube). Comments on the videos are not included, nor the number of users
subscribed to the channel. Using the GNIP Twitter API in early 2019, tweets
that include the YouTube videos URLs on White Helmets in our collection were
collected. Later on, data was collected from CrowdTangle on Facebook messages
posted between April 2018 and April 2019 that include the YouTube video URLs
from the original dataset.
To collect Reddit data, we performed an identical platform search to NG et al [19]
by fetching posts during the same time frame (April 1, 2018 to April 30, 2019)
containing videos from our dataset. We used the Pushshift Reddit Dataset [6]
in March 2023. Pushshift has collected Reddit data and made it available to
researchers since 2015, updated in real-time, and including historical data back
to Reddit’s inception [6]. Pushshift includes submissions (posts) and comments
that have since been deleted by Reddit or subreddit moderators. Because of the
free availability of this data, we also do not have to limit our search to specific
keywords, but can find every submission and comment made that includes any of
the relevant URLs from the collected YouTube data. Nevertheless, shortly after
our data collection, Reddit officially removed their API access. While Pushshift
still retrieves Reddit data, access is only granted for moderation purposes to
approved Reddit moderators.
Each message in our dataset is identified by a uniquepost ID, and has information
on the user ID, published time, platform, text content, action type(whether it is
a post or a reply) and linked video ID. Through a language detection model, we
noticed that more than 83% of the posts are in English, with the second most
used language being Arabic with 6 .9% of posts. We present the characteristics
of our dataset in Table 1.

Cross-Platform Coordinated Campaigns 5
Our cross-platform dataset thus contains posts from Twitter, Facebook and Red-
dit that include URLs to videos that have ”White Helmets” in their descriptions
or titles on YouTube. This dataset may include authentic messages in addition
to messages that may be part of the well-documented coordinated campaign
against the White Helmets. Since the dataset is unlabelled, we augmented it
with the Factuality Score on the Media Bias/Fact Check (MBFC) website [4].
The factuality score is an integer ranging from 0 to 5, with 0 being “Very Low”
and 5 “Very High” that is assigned currently to more than 6 , 800 news web-
sites based on information from fact-checkers that are either a signatory of the
International Fact-Checking Network or have been verified as credible by MBFC.
We labelled ≈ 30 questionable video channels and ≈ 30 mostly factual video
channels, with questionable sources being the most frequent in the dataset. In
fact, the three most posted video channels have a very low factuality score.
Clarity of Signal, RT and Vanessa Beeley are present in 2505 posts, 2073 and
1824 posts, respectively. A total of 9757 posts in our dataset posted a video
labelled with a factuality score, with 7273 posts having a factuality score of 0
(74.5%) and 1888 posts a factuality score of 1 (19 .4%).
Table 1: Characteristics of the multi-platform dataset on White Helmets.
YouTube video URLs are used to collect relevant messages posted on the other
social media platforms during the April 2018–April 2019 interval.
Platform Posts YT URLs YT channels Users
Reddit 481 113 63 266
Twitter 15, 314 666 283 4927
Facebook 1, 146 241 100 684
YouTube – 667 283 –
4 Methodology
Our objective is to design an approach based on content similarity and time
locality that identifies groups of messages that are likely coordinated. Because
we do not have ground truth information at fine granularity—that is, we do
not know which are the particular messages or the user accounts involved in a
campaign—we need to find different ways to evaluate the likelihood that our
groupings make sense.
The approach we propose makes some assumptions about coordinated informa-
tion operations, listed in Section 4.1. It includes two clustering stages, one based
on text and network embeddings and one based on the time lapse between posts
on social media platforms. We experiment with two text embeddings techniques,
Doc2Vec and BERTopic, as presented in Section 4.2. Furthermore, we define a
user-to-content network and extract its network embeddings using Node2Vec [16]

6 F. Barbero et al.
Text Network Time
Doc2VecBERTopic
Text embedding
MetaPathNode2Vec
Network embedding
Concatenated vector for each post
Clustering
algorithm
Introduce time as a
feature and cluster again
Fig. 1: Methodology pipeline overview. Textual and network embeddings are con-
catenated, after which we perform a first clustering on the produced embeddings
and a second clustering on the time component.
and, alternatively, MetaPath [12], that we append to our textual embeddings.
Finally, we account for temporal dynamics by incorporating a final clustering
component based on post time. The final pipeline leverages multimodal em-
beddings by combining text similarity, temporal information and the network
structure of users, posts, and shared links. Figure 1 illustrates our processing
pipeline.
4.1 Assumptions
Our approach makes the following assumptions:
Coordinated campaigns are characterized by messages posted closely in time and
that discuss similar topics. This may not always be the case: a coordinated
campaign may publish posts throughout a longer period of time, and mostly
exploit liking each other posts to make them more visible.
Text embeddings of posts across social media platforms are comparable.This
implies that the language used across social media platforms is similar, and that
the language model used will encode them similarly. In practice, this may not
always be the case, for example, tweets are known to be much shorter than posts
on Reddit.
Links posted by coordinated campaigns are from sources with similar factuality
scores. The underlying idea is that a coordinated campaign is unlikely to be

Cross-Platform Coordinated Campaigns 7
posting about sources with conflicting viewpoints. In practice, we might have
reliable sources being discredited in a coordinated campaign, alongside other
less reliable posts.
Apart from the Node2Vec method, all other methods assume that past user’s
activity is not relevant for identifying coordinated campaigns.This seems to differ
among campaigns, and has been seen to be true in some campaigns, such as
AIMS [14].
Given these assumptions, our methodology builds on temporal, network and
textual proximity of posts with the goal of detecting potential coordinated cam-
paigns. Having specific thresholds for the proximity allows us to identify groups
(clusters) that are potentially part of the same campaign.
4.2 T ext (Semantic) Similarity
We explored two approaches that can handle the text content of posts, namely
Doc2Vec and BERTopic. They are both enhanced by a temporal component, as
described in Section 4.4.
Doc2V ec.Our first approach combines Doc2Vec with K-means. The follow-
ing steps outline the process. We start with a Doc2Vec representation of each
post. This technique enables us to effectively capture the semantic relationships
between posts, facilitating subsequent clustering. We then perform an initial
clustering with K-means to group semantically similar posts together. We de-
termine the number of clusters based on the characteristics of the dataset. To
further refine the clustering results by accounting for temporal dynamics, we
employ the Density-Based Spatial Clustering of Applications with Noise (DB-
SCAN) algorithm. We provide more details on the latter part in Section 4.4.
BER T opic.Our second approach involves BERTopic to obtain clusters for all
posts with a topic representation of the clusters [15]. BERTopic uses Sentence-
BERT to build 384 dimensional embeddings per document. We then apply
UMAP for dimensionality reduction, mainly so the clustering is more efficient.
For clustering, we employ HDBSCAN, a hierarchical density-based clustering
algorithm. Lastly, we obtain our topic representations from clusters with c-TF-
IDF, generating candidates by extracting class-specific words. To improve our
topic representations, we end the pipeline with Maximum Candidate Relevance.
Note, while we implement the same pipeline as the original paper, each com-
ponent could be replaced by alternatives. For instance, one could employ PCA
instead of UMAP for dimensionality reduction. As with Doc2Vec we apply DB-
SCAN to get clusters based on temporal information as well.
4.3 Network Similarity: Random W alks
We define a network that connects users across social media platforms as shown
in Figure 2. In this multipartite network, edges connect users to their posts,

8 F. Barbero et al.
posts to videos, and videos to channels. While this definition is specific to the
dataset and social media platforms we used, it can be generalised to, for ex-
ample, (URLS to) online articles (instead of YouTube videos) and their hosting
websites (instead of YouTube channels). This structure does not capture text
or temporal information but only information on user interaction with content
(URLs). However, this allows us to create graph embeddings for each post using
Node2Vec, as nodes are only sparsely connected. We concatenate these network
embeddings to the text embeddings described in Section 4.2. To align both em-
beddings, we perform dimensionality reduction on both representations, such
that both embedding vectors have the same length (64 in our case).
Fig. 2: Example network structure.
Node2Vec does not take into account the different typed of nodes in a network.
In our network, there are four types of nodes: users, posts, videos and channels.
Since this information might be important and to account for these different
types of nodes, we apply meta-paths [12]. Meta-paths guide the random walks by
only allowing a fixed set of paths. In this paper, we set the following paths: [user,
post, video, post, user]; [video, channel, video]; [post, user, post] and [channel,
video, channel]. This allows us to incorporate semantic information on node
types into the network embeddings.
4.4 T emporal Dynamics
We assume coordinated campaigns occur within a short timeframe. By consid-
ering the temporal dimension, we ensure that we detect subgroups (subclusters)
containing posts that are not only semantically similar, but also close in time
(i.e. posted close in time). Hence, we subdivide clusters obtained from Doc2Vec

Cross-Platform Coordinated Campaigns 9
and BERTopic to account for temporal dynamics through a DBSCAN algorithm.
We choose ϵ = 52 seconds as suggested by [19] for the same dataset we used.
This is the inter-arrival time threshold in seconds between a video’s first share
on any platform (either Twitter or Facebook) and all successive shares. For more
details on our choice of ϵ, we refer to [19]. With this approach accounting for
temporal dynamics, we aim to facilitate the discovery of underlying patterns and
trends, shedding light on coordinated activities that may impact the analysed
content and enhancing our understanding of the data and identifying potential
coordinated efforts.
5 Results
In this section, we first describe the metrics we use to evaluate our methods.
We then perform an ablation study among the three components (text, network
and time) of our approach to evaluate how each affects the performance of our
approach. Finally, we further investigate different values for certain hyperparam-
eters.
5.1 Metrics
To evaluate the effectiveness of our approach, we employ two metrics: the stan-
dard deviation of factuality scores among clusters and the silhouette score for
the clustering of Doc2Vec, BERTopic and Random Walks features before and
after temporal subdivision. The following analysis provides insights into the per-
formance and detection capabilities of our approach.
Silhouette Score: We assess the quality of the clustering results by comput-
ing the silhouette score [23]. The silhouette score measures the cohesion and
separation of data points within clusters. A higher silhouette score indicates
better-defined and more distinct clusters. We compute the silhouette score us-
ing the features before and after applying the temporal subdivision, providing
insights into the improvement achieved through the incorporation of temporal
considerations.
Standard Deviation of F actuality ScoresWe calculate the factuality score
for posts containing YouTube links, which rates the factual accuracy of the infor-
mation in the respective YouTube channels. After executing the entire pipeline,
we analyse the factuality score for each cluster. A low standard deviation among
the factuality scores indicates that our algorithms cluster posts sharing videos of
similar factuality, whether they are questionable or of high factuality, whereas a
higher standard deviation suggests potential variations in the factual accuracy
of the information within the clusters. More specifically, we report the average,
median, standard deviation, and proportion of 0 standard deviation in clusters
among all clusters. As a comparison, we provide the standard deviation of all
posts.

10 F. Barbero et al.
5.2 Evaluation: Ablation Study
In this section, we discuss the performance of the different methods. To evaluate
the performance of our clustering, we compare the silhouette score and the intra-
cluster standard deviation in factuality score. As mentioned in our assumptions
in Section 4.1, we expect coordinated campaigns on social media to share sources
of similar factuality, whether questionable or high factuality. As we end the
pipelines of both methods by subclustering with regards to the posts’ time, we
compare the factuality standard deviation pre- and post-time clustering, and the
effect of our graph embeddings on these metrics. Our evaluation results can be
found in Table 2.
Table 2: Evaluation of the different approaches. We only keep clusters of size of
at least 2 posts to evaluate the factuality standard deviation. ∝ 0 denotes the
proportion of Factuality Standard Deviation of 0 obtained through all clusters.
The total standard deviation in the dataset is of 0 .75. N2V and MP2V denote
Node2Vec and Metapath2Vec, respectively.
Methods Silhouette Score Factuality Standard Deviation Avg Median Std ∝ 0
Doc2Vec 0.04 0 .61 0 .65 0 .49 0.26
Doc2Vec+PostTime −0.17 0 .38 0 .26 0 .41 0.10
BERTopic 0.30 0 .32 0 .18 0 .41 0 .24
BERTopic+PostTime −0.26 0.02 0 .00 0.13 0.96
Doc2Vec+N2V 0.23 0 .52 0 .41 0 .48 0.05
Doc2Vec+PostTime+N2V −0.07 0 .13 1 .45 0 .27 0.33
BERTopic+N2V 0.54 0.09 0.00 0.27 0 .54
BERTopic+PostTime+N2V −0.61 0.02 0 .00 0 .12 0 .96
Doc2Vec+MP2V 0.23 0 .56 0 .57 0 .43 0.2
Doc2Vec+PostTime+MP2V −0.11 0 .19 2 .79 0 .31 0.16
BERTopic+MP2V 0.31 0 .27 0 .00 0 .40 0 .37
BERTopic+PostTime+MP2V −0.44 0.02 0 .00 0.15 0 .94
The silhouette score drops after clustering the time component for both meth-
ods. This is because we obtain clusters of significantly smaller size. Post-time
subclustering is computed on the time component, and not based on the origi-
nal embeddings, while the silhouette score is still computed with respect to the
original embeddings. Due to the temporal subclustering, the new clusters are
no longer optimal in respect to the original embeddings (which are taking into
account only the text content). BERTopic encapsulates the textual information
better than Doc2Vec according to the silhouette score of the two methods. Still,
the silhouette score is far from 1, the optimal value. Values close to 0 signify clus-
ters that overlap. Negative results typically signify that a post was attributed
to a wrong cluster because another cluster would have better fit the post.

Cross-Platform Coordinated Campaigns 11
All methods achieve a better average factuality standard deviation than the total
standard deviation in the dataset. Clustering post-time strongly improves the
factuality standard deviation. This highlights the temporal aspect plays a role
in coordination campaigns, as this improves the clusters’ factuality wise.
BERTopic+PostTime identifies 5, 544 clusters of only one post. We drop those
clusters for our analysis as we judge they are unlikely to be part of a coordinated
campaign. Hence, we suspect the 587 clusters of size at least 2 ( ≈ 10% of the
clusters) to be likely part of a coordinated campaign as they have similar textual
and temporal information (the posts within a cluster have been shared within 52
seconds apart). Interestingly, the factuality standard deviation strongly reduces
to an average of 0 .01 post time ( ≈ 97% lower than pre time), with 98% of the
clusters having a factuality score standard deviation of 0.
Overall, BERTopic+PostTime+N2V performs best in factuality standard devi-
ation. BERTopic produces contextual embeddings that are taking into account
the context of the document as opposed to Doc2Vec, a simple generalization
of Word2Vec. In most cases, incorporating network embeddings improves the
performance, with Node2Vec scoring better. An explanation for the Node2Vec
performing better than MetaPath2Vec could be that we bias random walks in
Node2Vec to be more likely to be directed at nodes that the walk has already vis-
ited. We do this because coordinated posts usually reference the same or similar
videos. These nodes will, therefore, be close together in the graph. Biasing the
random walks to explore less puts more focus on these local subgraphs, which
gives posts close together in this graph more similar embeddings. The exact val-
ues we used were p = 0.25 and q = 4. In the implementation of the meta paths
we use, these cannot be set.
Not included here due to space constraints, we also considered different values
for the hyperparameters K and ϵ. K is used in the K-means algorithm. ϵ is the
radius of the DBSCAN search algorithm, in seconds. Additionally, we consider
two cases Twitter, Facebook as the first case and the Reddit dataset as the second
case. We further investigate the importance of choosing the rightϵ threshold. We
evaluate the factuality standard deviation for different value of ϵ. The optimal
values with regard to the factuality standard deviation seem to lie in the interval
[30, 60] seconds, confirming our choice of 52 seconds remains close to the optimal
choice of ϵ.
5.3 Coordinated Campaigns
BERTopic+PostTime+MP2V performs best in factuality standard deviation.
The clusters obtained by this approach take textual information into account,
through Sentence-BERT embeddings. Furthermore, temporal aspect is incorpo-
rated with our clustering where each post within a cluster must have another
post in that cluster that was posted within 52 seconds. Lastly, it encompasses
the social media interaction through the Node2Vec embeddings of our graph.
Since our clusters incorporate all those aspects, and due to the strong factuality

12 F. Barbero et al.
standard deviation scores, we believe these posts are highly likely to be part of a
coordinated campaign. In the remaining of this section, we perform an analysis
of these clusters.
5 10 15 20 25
Number of posts in a cluster
0
50
100
150
200
250
300Number of clusters
(a) Distribution of posts per cluster.
0 50 100 150 200 250 300 350
Biggest time difference between two posts in a cluster in seconds
0
20
40
60
80
100Number of clusters (b) Time difference between two posts.
Fig. 3: Distribution of posts (Figure 3a) and largest time difference be-
tween two posts within a cluster (Figure 3b) for clusters obtained by
BERTopic+PostTime+N2V.
BERTopic+PostTime+MP2V outputs 591 clusters with 2098 posts in total (1920
tweets, 141 Facebook posts and 37 Reddit comments), which represents 8% of
the total posts in our dataset, hence an average of 3 .37 posts per cluster. Figure
3a shows the distribution of posts per cluster. The distribution is right skewed,
with a maximum of 24 posts within a cluster, despite a significant number of
clusters with only two posts. Despite a low ϵ of 52 seconds in our DBSCAN
algorithm, some clusters have posts separated by up to six minutes (Figure 3b).
This is still a very short timeframe, particularly considering the time span of
our dataset over a year. As a matter of fact, most of the posts within a cluster
are separated by 100 seconds or less. This strong time similitude highlights a
coordination pattern between posts. Most of the clusters have posts with the
exact same textual information and a different post time. We observe that 89%
of the channels embedded in the posts had a factuality score of 0, hinting most
coordinated behaviour covers questionable sources of very low factuality. We
show the 10 most frequent video channels in Table 3.
5.4 Limitations
The limitations of this project can be categorized into two main areas: limita-
tions related to the underlying models’ structure and limitations of the results
obtained from training the models on the given data.

Cross-Platform Coordinated Campaigns 13
Table 3: The 10 most frequent video channels in the clusters computed by
BERTopic+PostTime+MP2V. The description provided below was not used in
our framework for identifying coordinated information operations, and is from
online sources shown in parenthesis and collected in July 2023.
Video channel # Posts Description
Clarity Of Signal 1, 204 Focused on Syrian war, 8 videos and 200 sub-
scribers [YouTube description].
Vanessa Beeley 455 British activist and blogger known for shar-
ing conspiracy theories and disinformation
about the Syrian civil war and the White Hel-
mets.[Wikipedia]
RT 244 “Questionable based on promoting pro-
Russian propaganda, conspiracy theories, nu-
merous failed fact checks, and a lack of author
transparency.” [MBFC]
Corbett Report 76 “Overall, we rate the Corbett Report a Tin
Foil Hat conspiracy and Moderate pseudo-
science website, based on the promotion of
9/11 conspiracies, False Flags, Chemtrails,
and Deep State conspiracies.” [MBFC]
RT UK 20 (see RT)
Corbett Report Extras 16 “This is the secondary channel of The Corbett
Report.” [YouTube description]
Syriana Analysis 14 “Overall, Syriana Analysis has a pro-Assad
view (The Arab Socialist Bath Party – Syria
Region); therefore, we rate Syriana Analysis
Left biased due to their story selection and
pro-Assad view. We also rate them Question-
able due to poor sourcing, opinion-based com-
mentary, lack of transparency, and a failed fact
check” [MBFC]
The Last American Vagabond 12 Meanwhile deleted by YouTube.
Sputnik 11 “Questionable based on the frequent promo-
tion of conspiracies and pro-Russian propa-
ganda, as well as the use of poor sources and
numerous failed fact checks.” [MBFC]
RT America 11 (see RT)

14 F. Barbero et al.
Working with social media data is known to be particularly tricky, and this
project is no exception. In particular, the patterns that our methods are trying
to clusters are the result of controlled human behaviour, meaning that if these
methods were put into place to identify clusters in an online scenario they would
be working against ”attackers” that will try to fool the system. Our solution
would need a dynamically inferred time threshold like the one used to infer the
52 seconds interval in previous work [19].
A limitation of the results stems from the assumption that embeddings across
different social media platforms can be directly compared within the same model,
without considering the platform-specific language and behaviour. However, it
is evident that the language used on Twitter greatly differs from that used on
Facebook or Reddit, meaning the evaluation of our model acts as a lower bound.
Furthermore, attackers are likely to employ different strategies tailored to each
social media platform to exploit each social media’s algorithm effectively.
As discussed in Section 3, there is no ground truth of what posts belong to coor-
dinated campaigns. Our approach to use Media Bias Fact Check for evaluation
has two limitations: one one hand, not all channels are evaluated; on the other
hand, the evaluation is at the news site granularity and not individual content
(video, in our case). Thus, it is theoretically possible that a particular video
in our dataset was fact-based while being hosted on a low factuality YouTube
channel. That is why qualitative analysis of the content flagged by our approach
is recommended.
6 Summary
This paper proposes an approach for identifying likely coordinated messages on
multiple social media platforms that integrates different modalities in addition
to temporal dynamics. We tested our approach on a dataset that includes con-
tent posted on Twitter, Facebook, Reddit, and YouTube related to the White
Helmets, the Syrian Civil Defence organization that was shown to be the tar-
get of discrediting information operations. Our method incorporates three key
modalities relevant for a coordination campaign: i) textual information (through
Doc2Vec and BERTopic); ii) temporal information, to detect social media posts
with good temporal locality; and iii) content and user interactions represented
as Node2Vec embeddings of a multi-modal network of users, posts, YouTube
videos, and YouTube channels.
To evaluate the effectiveness of our approach in the absence of ground truth, we
used metrics such as the standard deviation of factuality scores and the silhou-
ette score. The standard deviation of factuality scores allowed us to assess the
consistency of factual accuracy within clusters, while the silhouette score mea-
sured the quality of clustering results before and after incorporating temporal
considerations. The results strongly hint we managed to find clusters of posts
that are suspiciously coordinated in time and low-credibility content.

Cross-Platform Coordinated Campaigns 15
In the future we plan to test our approach on other multi-platform social media
datasets, some that are likely to contain traces of coordinated information op-
erations and others that do not. While in this paper we focused on designing an
approach that includes the necessary elements of a multi-platform coordinated
campaign—locality in content and in time—we plan to further evaluate the ac-
curacy of our identification approach, and its adaptability to different platforms.
References
1. Moderation Research - Twitter Transparency Center, https://transparency.
twitter.com/en/reports/moderation-research.html
2. Support the White Helmets, https://www.whitehelmets.org/en/
3. Syria war: Jihadist assault ’kills dozens of soldiers’. BBC News (Jan 2020), https:
//www.bbc.com/news/world-middle-east-51221225
4. Media Bias/Fact Check News (Jun 2023), https://mediabiasfactcheck.com/
5. Abu Salem, F.K., Al Feel, R., Elbassuoni, S., Jaber, M., Farah, M.:
F A-KES: A Fake News Dataset around the Syrian War (Jan 2019).
https://doi.org/10.5281/zenodo.2607278, https://zenodo.org/record/2607278
6. Baumgartner, J., Zannettou, S., Keegan, B., Squire, M., Blackburn, J.:
The Pushshift Reddit Dataset (Jan 2020), http://arxiv.org/abs/2001.08435,
arXiv:2001.08435 [cs]
7. Calisir, E., Brambilla, M.: Twitter dataset about Brexit (Dec 2022).
https://doi.org/10.7910/DVN/KP4XRP, https://dataverse.harvard.edu/
dataset.xhtml?persistentId=doi:10.7910/DVN/KP4XRP
8. Chen, E., Lerman, K., Ferrara, E.: Tracking Social Media Discourse About
the COVID-19 Pandemic: Development of a Public Coronavirus Twit-
ter Data Set. JMIR Public Health and Surveillance 6(2), e19273 (May
2020). https://doi.org/10.2196/19273, https://publichealth.jmir.org/2020/2/
e19273, company: JMIR Public Health and Surveillance Distributor: JMIR Public
Health and Surveillance Institution: JMIR Public Health and Surveillance Label:
JMIR Public Health and Surveillance Publisher: JMIR Publications Inc., Toronto,
Canada
9. Choudhury, N., Ng, K.W., Iamnitchi, A.: Strategic Information Operation in
YouTube: The Case of the White Helmets. In: Thomson, R., Bisgin, H., Dancy,
C., Hyder, A., Hussain, M. (eds.) Social, Cultural, and Behavioral Modeling, vol.
12268, pp. 318–328. Springer International Publishing, Cham (2020), series Title:
Lecture Notes in Computer Science
10. Davis, C.A., Varol, O., Ferrara, E., Flammini, A., Menczer, F.: Botornot: A sys-
tem to evaluate social bots. In: Proceedings of the 25th international conference
companion on world wide web. pp. 273–274 (2016)
11. DeVerna, M.R., Pierri, F., Truong, B.T., Bollenbacher, J., Axelrod, D., Loynes,
N., Torres-Lugo, C., Yang, K.C., Menczer, F., Bryden, J.: CoVaxxy: A Collection
of English-language Twitter Posts About COVID-19 Vaccines (Apr 2021), http:
//arxiv.org/abs/2101.07694, arXiv:2101.07694 [cs]
12. Dong, Y., Chawla, N.V., Swami, A.: metapath2vec: Scalable Representation Learn-
ing for Heterogeneous Networks. In: Proceedings of the 23rd ACM SIGKDD In-
ternational Conference on Knowledge Discovery and Data Mining. pp. 135–144.
ACM, Halifax NS Canada (Aug 2017). https://doi.org/10.1145/3097983.3098036,
https://dl.acm.org/doi/10.1145/3097983.3098036

16 F. Barbero et al.
13. Fazil, M., Abulaish, M.: A socialbots analysis-driven graph-based approach
for identifying coordinated campaigns in twitter. Journal of Intelligent &
Fuzzy Systems 38(3), 2961–2977 (Mar 2020). https://doi.org/10.3233/JIFS-
182895, https://www.medra.org/servlet/aliasResolver?alias=iospress&doi=
10.3233/JIFS-182895
14. Ganguly, M.: ‘Aims’: the software for hire that can control 30,000 fake online
profiles. The Guardian (Feb 2023), https://www.theguardian.com/world/2023/
feb/15/aims-software-avatars-team-jorge-disinformation-fake-profiles
15. Grootendorst, M.: BERTopic: Neural topic modeling with a class-based TF-IDF
procedure (Mar 2022), http://arxiv.org/abs/2203.05794, arXiv:2203.05794 [cs]
16. Grover, A., Leskovec, J.: node2vec: Scalable Feature Learning for Networks
(2016). https://doi.org/10.48550/ARXIV.1607.00653, https://arxiv.org/abs/
1607.00653
17. Lukito, J.: Coordinating a Multi-Platform Disinformation Campaign: In-
ternet Research Agency Activity on Three U.S. Social Media Plat-
forms, 2015 to 2017. Political Communication 37(2), 238–255 (Mar 2020).
https://doi.org/10.1080/10584609.2019.1661889, https://www.tandfonline.com/
doi/full/10.1080/10584609.2019.1661889
18. Magelinski, T., Ng, L.H.X., Carley, K.M.: A Synchronized Action Frame-
work for Responsible Detection of Coordination on Social Media (2021).
https://doi.org/10.48550/ARXIV.2105.07454, https://arxiv.org/abs/2105.
07454
19. NG, K.W., Horawalavithana, S., Iamnitchi, A.: Multi-platform Information Oper-
ations: Twitter, Facebook and YouTube against the White Helmets. ICWSM, US
(Jun 2021). https://doi.org/10.36190/2021.36, https://doi.org/10.36190/2021.
36
20. Nghiem, H., Muric, G., Morstatter, F., Ferrara, E.: Detecting cryptocurrency
pump-and-dump frauds using market and social signals. Expert Systems with Ap-
plications 182, 115284 (Nov 2021). https://doi.org/10.1016/j.eswa.2021.115284,
https://linkinghub.elsevier.com/retrieve/pii/S0957417421007156
21. Pacheco, D., Hui, P.M., Torres-Lugo, C., Truong, B.T., Flammini, A., Menczer,
F.: Uncovering Coordinated Networks on Social Media: Methods and Case Studies.
Proceedings of the International AAAI Conference on Web and Social Media 15,
455–466 (May 2021). https://doi.org/10.1609/icwsm.v15i1.18075, https://ojs.
aaai.org/index.php/ICWSM/article/view/18075
22. Ratkiewicz, J., Conover, M., Meiss, M., Gon¸ calves, B., Flammini, A., Menczer,
F.: Detecting and tracking political abuse in social media. In: Proceedings of the
International AAAI Conference on Web and social media. vol. 5, pp. 297–304
(2011), issue: 1
23. Rousseeuw, P.J.: Silhouettes: A graphical aid to the interpretation and validation
of cluster analysis. Journal of Computational and Applied Mathematics 20, 53–
65 (1987). https://doi.org/https://doi.org/10.1016/0377-0427(87)90125-7, https:
//www.sciencedirect.com/science/article/pii/0377042787901257
24. Shao, C., Ciampaglia, G.L., Varol, O., Yang, K.C., Flammini, A., Menczer, F.: The
spread of low-credibility content by social bots. Nature communications 9(1), 1–9
(2018), publisher: Nature Publishing Group
25. Sharma, K., Zhang, Y., Ferrara, E., Liu, Y.: Identifying Coordinated Ac-
counts on Social Media through Hidden Influence and Group Behaviours
(2020). https://doi.org/10.48550/ARXIV.2008.11308, https://arxiv.org/abs/
2008.11308

Cross-Platform Coordinated Campaigns 17
26. Wilson, T., Starbird, K.: Cross-platform Information Operations: Mobilizing Nar-
ratives & Building Resilience through both ’Big’ & ’Alt’ Tech. Proceedings
of the ACM on Human-Computer Interaction 5(CSCW2), 1–32 (Oct 2021).
https://doi.org/10.1145/3476086, https://dl.acm.org/doi/10.1145/3476086
