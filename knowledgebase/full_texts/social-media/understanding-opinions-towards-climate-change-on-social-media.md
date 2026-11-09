---
title: Understanding Opinions Towards Climate Change on Social Media
url: https://arxiv.org/abs/2312.01217
category: social-media
subcategory: empirical
date: 2023-12
venue: ''
authors:
- Yashaswi Pupneja
- Joseph Zou
- Sacha Lévy
- Shenyang Huang
source: arxiv
pdf_url: https://arxiv.org/pdf/2312.01217
pages: 10
chars: 28995
fetched_at: '2026-11-08T13:10:20+00:00'
kb_version: 1
---

# Understanding Opinions Towards Climate Change on Social Media

Understanding Opinions Towards Climate Change on
Social Media
Yashaswi Pupneja1,2 Joseph Zou3 Sacha Lévy4 Shenyang Huang1,3
1Mila 2Université de Montréal 3McGill University 4Yale University
yashaswi.pupneja@umontreal.ca yuesong.zou@mail.mcgill.ca
sacha.levy@yale.edu shenyang.huang@mail.mcgill.ca
Abstract
Social media platforms such as Twitter (now known as X) have revolutionized how
the public engage with important societal and political topics. Recently, climate
change discussions on social media became a catalyst for political polarization
and the spreading of misinformation. In this work, we aim to understand how
real world events influence the opinions of individuals towards climate change
related topics on social media. To this end, we extracted and analyzed a dataset
of 13.6 millions tweets sent by 3.6 million users from 2006 to 2019. Then, we
construct a temporal graph from the user-user mentions network and utilize the
Louvain community detection algorithm to analyze the changes in community
structure around Conference of the Parties on Climate Change (COP) events. Next,
we also apply tools from the Natural Language Processing literature to perform
sentiment analysis and topic modeling on the tweets. Our work acts as a first step
towards understanding the evolution of pro-climate change communities around
COP events. Answering these questions helps us understand how to raise people’s
awareness towards climate change thus hopefully calling on more individuals to
join the collaborative effort in slowing down climate change.
1 Introduction
Climate change is a widely debated topic, and a significant number of individuals still denies the effect
of climate change. Hence, we seek to understand how real-world events would influence opinions
regarding climate change on social media platforms. According to a survey by the Pew Research
Center, 15% of adults in the US do not believe that the Earth is warming, and 36% believe that it
is due to natural causes rather than human activity. The spread of misinformation and propaganda
campaigns on social media has contributed to skepticism around climate change [14].
To address these challenges, we aim to analyze the growth or contraction of communities of climate
change supporters and non-supporters on social media platforms. This analysis will provide insights
into how real-world events such as the Conference of the Parties (COP) events shape public opinion
on climate change. By analyzing the patterns of social media interactions and the spread of climate
change discourse on social media platforms, effective communication strategies can be developed to
promote climate change awareness and counter misinformation campaigns. The stakeholders of this
study include policymakers, environmental organizations, and the general public.
2 Background and Related Work
Climate Change on Social Media. Social media have created new arenas for public debates and
revolutionized the discussion of prominent issues such as global climate change [ 20]. Various
research on this topic have been conducted. [11] looked into user profile, tweet attitude, discussion
Tackling Climate Change with Machine Learning: workshop at NeurIPS 2023.
arXiv:2312.01217v1  [cs.SI]  2 Dec 2023

topics, and climate phenomenons. [2] built a random forest (RF) model to predict people’s attitude
towards climate change and environment protection based on psychological and demographic factors.
Furthermore, [25] modeled the relationship between perceived climate change efficacy and news and
user activities on social media by using multilevel regression.
Temporal Graph Learning. Social networks can be modeled as a temporal graph where users are
nodes and interactions are edges while the nodes and edges in the graph would naturally change
over time [23, 29, 28]. The dynamic community detection task which aims to identify groups of
individuals who are closely connected to each other on the temporal graph [ 21, 7, 4, 22]. Qin et
al. [21] and Boudebza et al. [4] both proposed novel methods to detect stable communities, groups of
nodes forming a coherent community throughout a period of time. In this work, we first apply the
well-know Louvain community detection algorithm [3] to identify the growth or contraction of user
communities of climate change topics on twitter.
Misinformation detection. Misinformation related to climate change is a significant problem that
has been widely researched. Several studies have examined the relationship between social media
usage, belief in conspiracy theories, and misinformation, highlighting the gravity of the issue [12].
The adverse impact of such misinformation has been well-documented, underscoring the importance
of inoculating people against misinformation related to climate change [18]. Research on debunking
strategies has produced mixed results, highlighting the continued influence of misinformation and
the need for effective measures [ 17, 5]. The identification of psychological factors that drive
misinformation and hinder debunking [ 9] indicates the complexity of the issue and the need for
targeted interventions to tackle it.
Political polarization detection. Political polarization [8] is one of the crucial socio-political issues
in twenty-first century. It intensifies political debates and may even threaten civil society. [ 8]
demonstrated that political polarization happens naturally when the observable indicators of policy
outcomes are not monotonic. Hence due to its commonness and harmfulness, it is important to
monitor political polarization and its impact especially in public discussions about climate. [ 16]
demonstrated that public opinion toward climate politics is closely consistent with people’s positions
on parties and the US general public has become quite politically polarized in recent years. Further
studies [6, 19] showed similar alignment between polarized public opinions toward climate politics
and partisan sorting. Considering the effect of events, [13] highlighted a large increase in polarization
in 2021 during the 26th United Nations Conference of the Parties on Climate Change (COP26)
and attributed it to growing right-wing activity. Moreover, [26] investigated hostile communication
between polarized competing groups.
3 Dataset
In this section, we first discuss how we constructed the twitter dataset which we used for this project
in Section 3.1. Then we extract the user-user mentions temporal network from the full dataset to
examine the user interactions on twitter 3.2.
3.1 Collecting Twitter Dataset
To understand how people engage with climate change related topics on social media, we first collect
dataset of tweets from Twitter, a popular social network for discussing trending topics. In particular,
we focus our collection process on climate change related tweets, posts made by users on Twitter. We
leveraged a recently released Kaggle dataset [ 11, 10] containing climate change related tweets and
their attributes for our study. However, the dataset lacks the raw tweet text and other information.
Therefore, we use the tweet ID from the dataset to recollect the tweets using the Twitter API for
Academic Research. Our dataset contains 13.6 millions tweets sent by 3.6 million users from 2006
to 2019. Each tweet contains various information such as the sender, any mentions of other users,
timestamp, any hashtags and the raw text of the tweet. We have also collected dates for relevant
Conference of the Parties (COP) Events in the duration of the dataset (as seen in Appendix C).
3.2 Constructing Temporal Graph
From the collected meta-data of tweets, we construct the user-user mentions network to be a weekly
temporal graph. This network naturally shows how users interact with each other over time. However,
2

the edges might not necessarily indicate that two users shares the same opinion. For example, it is
possible for a climate change supporter to mention another user who doesn’t believe in climate change.
In this work, we discretize the mentions network to be a weekly temporal graph. More specifically, we
represent the temporal graph G as a series of graph snapshots, G = {Gt}T t=1 where Gt = {Vt, At}
is the graph snapshot at time t and Vt, At represent the set of nodes and the adjacency matrix of Gt
respectively.
While processing the tweet dataset, we find that there exist a large number of users which only send
climate related tweets sparsely. Therefore, the constructed temporal graph is disconnected and sparse
thus forming isolated components rather communities of users. To increase the density of the network
while focusing on users that are more active on climate change topics, we remove all users that have
less than 100 edges (across all steps) from the network (both outgoing and incoming edges). In this
way, we only preserve a dense core set of users.
4 Methodology
climatechange
47.8%
climateaction
38.8%
environment
5.8% energy
5.4%
globalwarming
1.5% creativity0.7%
(a) Distribution of top Hashtags in tweets.
 (b) Distribution of positive, negative and neutral tweets.
Figure 1: Analysis of a). hashtags and b). sentiment in extracted tweets.
Hashtags Analysis. The top [YP: 8] most used hashtags from tweets are shown in Figure 1a. Some
interesting hashtags include creativity, spirituality, economy, education and "its time to change". In
particular, the hashtags themselves might already contain views or opinion towards climate change
topics such as "its time to change".
Sentiment Analysis. Sentiment analysis is a technique used to determine the emotional tone behind
a piece of text. We analyze the overall sentiment of tweets to understand the emotions associated
with different topics related to climate change such as climate policy, environmental disasters or
scientific research. Sentiment analysis also helps identify patterns in the emotional tone of different
groups, such as climate change supporters or deniers. Here, we used the TextBlob library to detect
the sentiments of the tweets which determined whether the texts were positive, negative or neutral.
The results are summarized in the pie chart in Figure 1b. The majority of tweets are neutral while
there remains 19.0% of tweets that have a negative sentiment. This shows that most users share a
neutral sentiment towards climate change and it calls for more actions to engage the public in more
positive involvement in climate change actions. We also acknowledge that negative sentiments such
as fear and discontent are also considered as negative but can show awareness towards climate events.
Temporal Graph Analysis
Figure 2 shows the evolution of the number of edges and graph density over time. We also marked
COP events by grey vertical lines. COP events are often accompanied by local peaks in the number
of edges. This is likely because more discussion on climate change related topics happen around
COP events annually. For graph density, we observe large peaks around COP 13, 14 and 17. The
3

11/22/200705/07/200901/18/201010/01/201006/15/201105/01/201203/31/201302/08/201411/26/201408/14/201506/06/201604/11/201701/15/201811/26/201808/13/2019
Time (weeks)
0
50000
100000
150000
200000
250000
300000
350000Number of edges
COP13
COP14
COP15
COP16
COP17
COP18
COP19
COP20
COP21
COP22
COP23
COP24
COP25
(a) number of edges
11/22/200705/07/200901/18/201010/01/201006/15/201105/01/201203/31/201302/08/201411/26/201408/14/201506/06/201604/11/201701/15/201811/26/201808/13/2019
Time (weeks)
0.0
0.2
0.4
0.6
0.8
1.0Density
COP13
COP14
COP15
COP16
COP17
COP18
COP19
COP20
COP21
COP22
COP23
COP24
COP25 (b) density of graph snapshots
Figure 2: The evolution of a). the number of edges and b). graph density in the temporal user-user
mentions network constructed from tweets.
08/09/2012 09/16/2012 11/11/2012 12/13/2012 02/11/2013
Time (weeks)
0
100
200
300
400
500
600Number of communities
COP18
Number of communities over time (weekly)
(a) COP 18
07/31/2013 09/01/2013 10/07/2013 12/01/2013 01/23/2014
Time (weeks)
0
100
200
300
400
500
600Number of communities
COP19
Number of communities over time (weekly) (b) COP 19
Figure 3: The number of communities detected around a). COP 18 and b). COP 19
peaks around COP 13 and 14 can be a result of noise in data collection in early years of twitter. The
peaks around COP 17 signals increased discussion between active twitter users around this time. This
coincides with the fact that COP 17 has one of the most significant achievements as all countries
agree to the reduction of emissions, including the US and emerging countries such as Brazil, China,
India and South Africa [1]. Details on the time of COP events are in Appendix C.
Community Detection on Temporal Graph. In this work, we aim to examine changes to the
community structure of the user-user mentions network around the time of COP events. To this end,
we utilize the fast and scalable Louvain algorithm [3] to detect communities on individual snapshots
of the temporal graph. The Louvain algorithm optimizes the modularity Q of the graph, defined as
follows in a directed graph,
Q = 1 2m X ij [Aij − kikj 2m ]δ(ci, cj) (1)
where A is the weighed adjacency matrix of the graph, ki and kj are the sum of the weights of edges
of nodes i, jrespectively, m is the sum of all of the edge weights in the graph, ci and cj are the
communities of nodes i, jand lastly, δ is the kronecker delta function. The complexity of the Louvain
algorithm is O(n · log n) where n is the number of nodes. More details can be found in Appendix B.
Overall, The number of communities seem to increase over time with local peaks periodically. We
also examine the community structure of graph snapshots surround COP events (10 weeks before and
10 weeks after) with the Louvain algorithm. Figure 3 shows the change in number of communities
around COP 18 and COP 19. For COP 18 and 19, there is a decrease in the number of communities.
This shows that larger communities are formed likely due to increased user discussions. However, for
COP 20 and COP 21, there is an increase of communities. Therefore, it is difficult to clearly draw
conclusions based on the number of communities around COP events. This is also expected as the
Louvain algorithm is computed based the graph structure alone and doesn’t utilize the tweet text and
other edge features. More community detection results are reported in Appendix D.
4

Figure 4: Significant topics extracted from the corpus.
Topic Modeling. Topic models are a class of unsupervised machine learning that allows us to extract
topics from a large corpus of text data. They are powerful techniques that are commonly used for
identifying patterns and themes in large text datasets. A typical topic model works by identifying
groups of words that tend to co-occur in the same documents or tweets. These groups of words are
known as "topics" and can provide insights into the underlying themes and issues that are present in
the data. In our analysis of opinions on Twitter, we used topic modeling to identify the main topics of
conversation related to climate change. By using the mini-batch non-negative matrix factorization
(NMF) algorithm [15], we were able to efficiently extract topics from a large-scale dataset and gain
insights into the key themes and issues that are salient to the public.
We first tokenized the tweets data and then trained the mini-batch NMF model on the preprocessed
corpus by setting the number of topics as 10. We utilized the scikit-learn toolkit to run mini-batch
NMF model. The training algorithm was run for iterations until convergence, i.e., a set of stable topics
was obtained. After the matrix factorization had been done, we looked at the topic-word score matrix
W and described each topic by the words with the highest relevance score. Figure 4 shows three
obtained representative topics with their top 20 words aboutpolitics, CO2 emission, and weather. The
politics topic is related to politicians (e.g., Trump), organizations (e.g., EPA) and actions to address
and mitigate climate change. The CO2 emission topic includes global warming, Arctic ice melting,
and sea level rising as consequences of CO2 emission. The weather topic shows people’s concern
about extreme and abnormal weather caused by global warming.
5 Pathway to Impact
This project aims to provide valuable insights into opinions about climate change on Twitter, poten-
tially impacting many stakeholders. For policy makers, our approach provides an understanding of
public opinion and sentiment as guidance to decision-making. For Researchers in social sciences,
our project contributes to the study of the patterns and dynamics of climate change-related online
communication. For journalists, our study provides insights about when and how to report on climate
change topics. For the public, this project can inform them about potential negative sentiment and
opinions towards climate change events on social media thus help more individuals raise awareness
of climate change topics. Future work can extend our work and apply more recent techniques such as
Large Language Models [24] and Graph Neural Networks [27].
6 Acknowledgement
We thank Prof. David Rolnick and TA Michelle Lin for their support and guidance throughout the
duration of this project. We also thank prof. Reihaneh Rabbany and prof. Guillaume Rabusseau for
their discussions and support in this project. This research was supported by the Canadian Institute for
Advanced Research (CIFAR AI chair program), Natural Sciences and Engineering Research Council
of Canada (NSERC) Postgraduate Scholarship-Doctoral (PGS D) Award and Fonds de recherche du
Québec – Nature et Technologies (FRQNT) Doctoral Award.
5

References
[1] Achievements of the conference of the parties. https://www.activesustainability.
com/climate-change/achievements-of-the-conference-of-the-parties/?_
adin=02021864894. Accessed: 2023-09-27.
[2] L. F. Beiser-McGrath and R. A. Huber. Assessing the relative importance of psychological
and demographic factors for predicting climate and environmental attitudes. Climatic change,
149:335–347, 2018.
[3] V . D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. Fast unfolding of communities
in large networks. Journal of statistical mechanics: theory and experiment, 2008(10):P10008,
2008.
[4] S. Boudebza, R. Cazabet, O. Nouali, and F. Azouaou. Detecting stable communities in link
streams at multiple temporal scales. In Machine Learning and Knowledge Discovery in
Databases: International Workshops of ECML PKDD 2019, Würzburg, Germany, September
16–20, 2019, Proceedings, Part I, pages 353–367. Springer, 2020.
[5] M.-p. S. Chan, C. R. Jones, K. H. Jamieson, and D. Albarracín. Debunking: A meta-analysis of
the psychological efficacy of messages countering misinformation. Association for psychologi-
cal Sciences, 28(11):1531–1546, 2017.
[6] T. H. Y . Chen, A. Salloum, A. Gronow, T. Ylä-Anttila, and M. Kivelä. Polarization of climate
politics results from partisan sorting: Evidence from finnish twittersphere.Global Environmental
Change, 71:102348, 2021.
[7] R. Clark, G. Punzo, and M. Macdonald. Network communities of dynamical influence.Scientific
reports, 9(1):1–13, 2019.
[8] A. K. Dixit and J. W. Weibull. Political polarization. Proceedings of the National Academy of
Sciences, 104(18):7351–7356, 2007.
[9] U. K. Ecker, S. Lewandowsky, J. Cook, P. Schmid, L. K. Fazio, N. Brashier, P. Kendeou,
E. K. Vraga, and M. A. Amazeen. The psychological drivers of misinformation belief and its
resistance to correction. Nature Reviews Psychology, 1(1):13–29, 2022.
[10] D. Effrosynidis, A. I. Karasakalidis, G. Sylaios, and A. Arampatzis. The climate change twitter
dataset. Expert Systems with Applications, 204:117541, 2022.
[11] D. Effrosynidis, G. Sylaios, and A. Arampatzis. Exploring climate change on twitter using
seven aspects: Stance, sentiment, aggressiveness, temperature, gender, topics, and disasters.
Plos one, 17(9):e0274213, 2022.
[12] A. Enders, J. Uscinski, and M. Seelig. The relationship between social media use and beliefs in
conspiracy theories and misinformation. In Polit Behav, 2021.
[13] M. Falkenberg, A. Galeazzi, M. Torricelli, N. Di Marco, F. Larosa, M. Sas, A. Mekacher,
W. Pearce, F. Zollo, W. Quattrociocchi, et al. Growing polarization around climate change on
social media. Nature Climate Change, pages 1–8, 2022.
[14] C. Funk and M. Hefferon. Us public views on climate and energy. Pew Research Center, 25,
2019.
[15] C. Févotte and J. Idier. Algorithms for Nonnegative Matrix Factorization with theβ-Divergence.
Neural Computation, 23(9):2421–2456, 09 2011.
[16] L. C. Hamilton and K. Saito. A four-party view of us environmental concern. Environmental
Politics, 24(2):212–227, 2015.
[17] S. Lewandowsky, U. K. H. Ecker, C. M. Seifert, N. Schwarz, and J. Cook. Misinformation
and its correction: Continued influence and successful debiasing. Psychological Science in the
Public Interest, 13(3):106–131, 2012.
[18] S. v. d. Linden, A. Leiserowitz, S. Rosenthal, and E. Maibach. Inoculating the public against
misinformation about climate change. In Proceedings of the 28th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, 2017.
[19] A. M. McCright, R. E. Dunlap, and S. T. Marquart-Pyatt. Political ideology and views about
climate change in the european union. Environmental Politics, 25(2):338–358, 2016.
6

[20] W. Pearce, S. Niederer, S. M. Özkula, and N. Sánchez Querubín. The social media life of
climate change: Platforms, publics, and future imaginaries. Wiley interdisciplinary reviews:
Climate change, 10(2):e569, 2019.
[21] H. Qin, R.-H. Li, G. Wang, X. Huang, Y . Yuan, and J. X. Yu. Mining stable communities in
temporal networks by density-based clustering. IEEE Transactions on Big Data, 8(3):671–684,
2020.
[22] G. Rossetti and R. Cazabet. Community discovery in dynamic networks: a survey. ACM
computing surveys (CSUR), 51(2):1–37, 2018.
[23] E. Rossi, B. Chamberlain, F. Frasca, D. Eynard, F. Monti, and M. Bronstein. Temporal graph
networks for deep learning on dynamic graphs. arXiv preprint arXiv:2006.10637, 2020.
[24] R. Tang, Y .-N. Chuang, and X. Hu. The science of detecting llm-generated texts. 2023.
[25] L. Tuitjer and P. Dirksmeier. Social media and perceived climate change efficacy: A european
comparison. Digital Geography and Society, 2:100018, 2021.
[26] A. Tyagi, J. Uyheng, and K. M. Carley. Affective polarization in online climate change
discourse on twitter. In 2020 IEEE/ACM International Conference on Advances in Social
Networks Analysis and Mining (ASONAM), pages 443–447, 2020.
[27] K. Xu, W. Hu, J. Leskovec, and S. Jegelka. How powerful are graph neural networks? arXiv
preprint arXiv:1810.00826, 2018.
[28] J. You, T. Du, and J. Leskovec. Roland: graph learning framework for dynamic graphs. In
Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
pages 2358–2366, 2022.
[29] H. Zhou, D. Zheng, I. Nisa, V . Ioannidis, X. Song, and G. Karypis. Tgl: a general framework
for temporal gnn training on billion-scale graphs. Proceedings of the VLDB Endowment ,
15(8):1572–1580, 2022.
7

Table 1: Conference of the Parties (COP) Events present in the Twitter dataset.
Name Date Location
COP13 03 Dec 2007 - 17 Dec 2007 "Bali, Indonesia"
COP14 01 Dec 2008 - 12 Dec 2008 "Poznan, Poland"
COP15 07 Dec 2009 - 18 Dec 2009 "Copenhagen, Denmark"
COP16 28 Nov 2010 - 10 Dec 2010 "Cancun, Mexico"
COP17 28 Nov 2011 - 09 Dec 2011 "Durban, South Africa"
COP18 26 Nov 2012 - 07 Dec 2012 "Doha, Qatar"
COP19 11 Nov 2013 - 23 Nov 2013 "Warsaw, Poland"
COP20 01 Dec 2014 - 12 Dec 2014 "Lima, Peru"
COP21 30 Nov 2015 - 12 Dec 2015 "Paris, France"
COP22 07 Nov 2016 - 18 Nov 2016 "Marrakech, Morocco"
COP23 06 Nov 2017 - 17 Nov 2017 "Bonn, Germany"
COP24 03 Dec 2018 - 14 Dec 2018 "Katowice, Poland"
COP25 02 Dec 2019 - 13 Dec 2019 "Madrid, Spain"
A General Considerations
We encountered several general considerations that we believe are worth noting.
Ethical Considerations: Respecting the privacy and confidentiality of Twitter users is crucial, and we
have taken steps to de-identify individual users in our analysis and focus on trends of the population
instead of investigating individuals. However, we acknowledge that social media data analysis can
raise ethical concerns, and urge researchers and practitioners to be mindful of potential harms and
take appropriate measures.
Data Quality Considerations: Slang, buzzwords, and sarcasm can be challenging to interpret in
social media data analysis. To address this, we employed natural language processing and sentiment
analysis techniques, but acknowledge that our analysis may still be subject to noise and bias.
Limitations of Twitter Data: While Twitter can provide valuable insights into public opinions,
it is important to recognize its limitations. Twitter users may not be representative of the broader
population, and the topics and issues discussed on Twitter may not be indicative of those that are
most relevant to the public.
Opportunities for Future Research: Our analysis suggests several avenues for future research on
climate-change-related opinion on social media, such as exploring demographic differences in how
climate change is perceived and discussed on Twitter, or tracking shifts in public opinion over time.
B Louvain Community Detection Algorithm
The Louvain algorithm has two phases which are interactively applied. First, all nodes in the graph
is assigned its own unique community. Then, the algorithm decides if moving a node from its own
community to its neighbors’ community improves the modularity score Q. The node is then placed
into its neighbor’s community which sees the most increase in modularity. In the second phase,
the algorithm groups all nodes in the same community and builds a new network where nodes are
the communities from before. After this creation, the first phase then starts again. The algorithm
terminates when no modularity increase can be observed. The complexity of the Louvain algorithm is
O(n · log n) where n is the number of nodes. Note that by design, the Louvain algorithm constructs
hierarchical communities as it iteractively groups communities into larger ones.
C COP Events Details
We report the COP events present in the Twitter dataset in Table 1.
8

11/22/200712/24/200805/07/200909/12/200901/18/201005/26/201010/01/201002/07/201106/15/201110/21/201105/01/201210/02/201203/31/201308/16/201302/08/201407/21/201411/26/201404/07/201508/14/201501/20/201606/06/201610/22/201604/11/201709/09/201701/15/201805/23/201811/26/201804/07/201908/13/2019
Time (weeks)
0
200
400
600
800
1000
1200Number of communities
Number of communities over time (weekly)
Figure 5: The evolution of number of clusters in each snapshot of the temporal graph.
09/15/2014 10/17/2014 11/18/2014 12/20/2014 01/24/2015
Time (weeks)
100
200
300
400
500
600
700
800Number of communities
COP20
Number of communities over time (weekly)
(a) COP 20
08/14/2015 10/02/2015 11/08/2015 12/19/2015 01/20/2016
Time (weeks)
200
400
600
800
1000Number of communities
COP21
Number of communities over time (weekly) (b) COP 21
Figure 6: The number of communities detected by the Louvain algorithm around a). COP 20 and b).
COP 21 event.
D Additional Community Detection Results
Figure 5 shows the change in number of communities detected by the Louvain algorithm in the
temporal graph. Here we provide additional community mining results for all the COP events present
in our dataset including COP 13 to COP 24.
9

11/22/2007 07/15/2008 09/18/2008
Time (weeks)
1.0
1.5
2.0
2.5
3.0
3.5
4.0Number of communities
COP13
Number of communities over time (weekly)
(a) COP 13
04/18/2008 09/10/2008 11/09/2008 12/15/2008 01/21/2009
Time (weeks)
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0Number of communities
COP14
Number of communities over time (weekly) (b) COP 14
09/20/2009 10/22/2009 11/23/2009 12/25/2009 01/26/2010
Time (weeks)
50
100
150
200
250
300Number of communities
COP15
Number of communities over time (weekly)
(c) COP 15
09/07/2010 10/09/2010 11/11/2010 12/13/2010 01/14/2011
Time (weeks)
50
100
150
200
250
300
350Number of communities
COP16
Number of communities over time (weekly) (d) COP 16
09/11/2011 10/13/2011 11/14/2011 12/16/2011 02/24/2012
Time (weeks)
0
100
200
300
400
500Number of communities
COP17
Number of communities over time (weekly)
(e) COP 17
08/01/2016 09/12/2016 10/14/2016 11/26/2016 12/29/2016
Time (weeks)
0
200
400
600
800
1000
1200Number of communities
COP22
Number of communities over time (weekly) (f) COP 22
08/11/2017 09/17/2017 10/19/2017 11/20/2017 12/22/2017
Time (weeks)
200
400
600
800
1000
1200Number of communities
COP23
Number of communities over time (weekly)
(g) COP 23
08/21/2018 09/22/2018 10/24/2018 12/20/2018 01/24/2019
Time (weeks)
200
400
600
800
1000
1200Number of communities
COP24
Number of communities over time (weekly) (h) COP 24
Figure 7: The number of communities detected by the Louvain algorithm around
10
