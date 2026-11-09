---
title: Quantifying Influencer Impact on Affective Polarization
url: https://arxiv.org/abs/2405.15893
category: social-media
subcategory: empirical
date: 2024-05
venue: ''
authors:
- Rezaur Rashid
- Joshua Melton
- Ouldouz Ghorbani
- Siddharth Krishnan
- Shannon Reid
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.15893
pages: 8
chars: 37162
fetched_at: '2026-11-08T13:12:13+00:00'
kb_version: 1
---

# Quantifying Influencer Impact on Affective Polarization

Quantifying Influencer Impact on Affective
Polarization
Rezaur Rashid
Department of Computer Science
UNC Charlotte
Charlotte, USA
mrashid1@charlotte.edu
Joshua Melton
Department of Computer Science
UNC Charlotte
Charlotte, USA
jmelton30@charlotte.edu
Ouldouz Ghorbani
Department of Computer Science
UNC Charlotte
Charlotte, USA
oghorban@charlotte.edu
Siddharth Krishnan
Department of Computer Science
UNC Charlotte
Charlotte, USA
skrishnan@charlotte.edu
Shannon Reid
Department of Criminal Justice and Criminology
UNC Charlotte
Charlotte, USA
sreid33@charlotte.edu
Gabriel Terejanu
Department of Computer Science
UNC Charlotte
Charlotte, USA
gabriel.terejanu@charlotte.edu
Abstract—In today’s digital age, social media platforms play a
crucial role in shaping public opinion. This study explores how
discussions led by influencers on Twitter, now known as ‘X’,
affect public sentiment and contribute to online polarization. We
developed a counterfactual framework to analyze the polarization
scores of conversations in scenarios both with and without the
presence of an influential figure. Two case studies, centered on
the polarizing issues of climate change and gun control, were
examined. Our research highlights the significant impact these
figures have on public discourse, providing valuable insights into
how online discussions can influence societal divisions.
Index Terms —social networks, twitter, stance labeling, gun
control, climate change
I. I NTRODUCTION
The transformative impact of social media on political
communication cannot be overstated. As a platform for in-
stantaneous information exchange, social media has redefined
the way individuals engage with political content, debate
policy, and form community bonds [1], [2]. However, this
digital revolution has also given rise to a less auspicious
phenomenon: affective polarization [3]–[5]. The term, affective
polarization refers to the phenomenon where individuals feel
more positively towards members of their political group while
simultaneously harboring negative sentiments towards those of
opposing groups [6], [7].
Affective polarization on social media is especially harmful
because it can undermine healthy democratic discussions. In-
stead of encouraging thoughtful debate, it often leads to hostile
confrontations [8], [9]. The effects of this trend go beyond the
online world, influencing real-world political engagement and
the broader societal fabric [10], [11].
At the heart of this polarization are influential
users—individuals and entities with large followings who
can significantly shape public discourse. These influencers
can either deepen existing divides or help bridge gaps in
understanding through their discussions on controversial
topics [12], [13]. Nowadays, the reach and impact of such
figures are greater than ever before, making it essential
to closely examine their role in the process of affective
polarization. [14].
In this study, we aim to measure the impact of conversations
started by influential users on the polarization seen in Twit-
ter/X discussions. Our paper makes the following contributions
to understand how these influencers shape public sentiment
and contribute to polarization in online communities.
• This research presents a new framework using counterfac-
tual analysis to quantitatively measure how conversations
led by influencers affect polarization on Twitter/X. By
comparing polarization scores with and without these
influential conversations, we reveal their impact on public
discourse.
• We offer a detailed analysis of how influential users shape
emotional dynamics within contentious topics such as
climate change and gun control, providing quantifiable
measures of their influence on affective polarization.
This study not only advances our understanding of affective
polarization but also has practical implications for the design
and governance of social media platforms. By identifying the
influential figures and the factors that exacerbate or mitigate
polarization, platform designers and policymakers can better
navigate the challenges posed by this phenomenon and work
towards a more informed and less divided public discourse.
II. L ITERATURE REVIEW
The phenomenon of affective polarization has been ex-
tensively documented in political psychology, with recent
studies revealing its escalation on social media platforms [15],
[16]. Affective polarization extends beyond ideological dis-
agreements, encapsulating emotional responses that manifest
as mutual dislike and distrust among those with opposing
political allegiances [17].
Research highlights a complex interplay between media,
political figures, and entrenched ideologies that magnifies soci-
arXiv:2405.15893v2  [cs.SI]  16 Sep 2024

etal divisions. Social media platforms enhance these divisions
through algorithmically curated content that often promotes in-
flammatory and polarizing material [18]–[20]. Echo chambers,
a topic of much debate, are often criticized for reinforcing
ideological conformity and shielding users from opposing
viewpoints, which can intensify affective polarization [21].
Conversely, some research suggests that even when individuals
are exposed to contrary opinions, this exposure does not neces-
sarily mitigate polarization and may, under certain conditions,
actually exacerbate it [22], [23].
Advancements in quantifying affective polarization have
led to the development of metrics that capture the emotional
content and toxicity in social media interactions [10], [24].
Studies now classify users by political partisanship and ana-
lyze the emotions and language used in their communications,
providing a subtle understanding of the affective component
of polarization [6], [25]. This line of research highlights that
negative emotions and toxicity are not randomly distributed
but correlate with the network distance in social media in-
teractions, suggesting structural properties of these networks
influence the emotional tone of online discourse [26].
Kramer et al. [27] assert that emotional states are contagious
so whether expressed by other people or appears on Newsfeed
(a personalized stream of content provided by social media
platforms) has a direct impact on our emotions. Another find-
ing of their study is that as opposed to prevalent perception,
non-verbal language, and inter-personal interactions are not
required for contagion of emotions. The study by Cha et al.
[28] explores influence patterns on social media and identifies
the most important role-playing factors. Betts and Bliuc [29]
shows that an influencer with extreme opinions will invariably
accelerate the pace of polarization, and this impact grows
in proportion to their influence and level of engagement.
The impact of a neutral influencer, however, depends on the
society’s openness to differing viewpoints.
Despite extensive research on affective polarization, much
of the current literature focuses on the consequences of po-
larization without a clear methodology to quantify its emer-
gence and escalation directly from influencer interactions. In
addition, there is a limited exploration into the specific role of
influential users within these divisive dynamics, particularly in
how their conversations shape public sentiment over time [14].
Our research builds upon these findings by specifically ex-
amining how influential figures impact the affective landscape
of online discourses. By systematically evaluating the presence
and absence of high-profile conversations, we offer a unique
perspective on the role influencers play in either mitigating
or exacerbating affective polarization. Through this lens, we
contribute to a deeper understanding of the dynamics at play
in social media’s political discourse to provide insights into
digital communication strategies aimed at reducing polariza-
tion.
III. M ETHODOLOGY
The goal of this study is to methodically quantify the impact
of influencers on affective polarization on social media plat-
forms. To achieve this, we implement a counterfactual analysis
framework, which involves constructing hypothetical scenarios
to understand what might happen if certain influencer-led con-
versations did not occur. This approach, illustrated in Figure 1,
allows us to isolate the effects of these conversations on polar-
ization dynamics, providing a clearer picture of their influence.
The following subsections introduce the specifics of our data
collection strategies, the construction of interaction networks,
and the application of sentiment analysis and quantifying
polarization metrics, providing a comprehensive understanding
of our methodological approach and the analytical techniques
employed to evaluate the influencer impact on online social
interactions.
A. Data
1) Data Collection: Our research employed a comprehen-
sive dataset, we extracted from Twitter, covering tweets related
to two prominent and contentious political issues–climate
change and gun control. We used specific Hashtags relevant
to each topic to scrape the initial set of tweets using the
Twitter API before its restrictions were imposed in 2023. To
ensure a thorough capture of conversation cascades and user
interactions, we expanded our data collection by recursively
retrieving all referenced tweets linked to the initial set. This
method allowed us to include all pertinent discussions, cap-
turing the depth and breadth of conversations. User metadata
such as the number of likes, replies, and retweets was also
retrieved, as shown in Table I.
2) Data Exploration: In analyzing the dataset, we identified
a significant number of conversation threads with limited
active engagement, defined as the number of distinct users
replying within each thread. This measure focuses on direct
interactions rather than passive activities like retweets and
likes, aiming to capture meaningful exchanges. Many threads
exhibited minimal interaction, often involving less than ten
participants (Figure 2). To ensure the analytical robustness of
our study, we established minimum engagement criteria based
on discussions with domain experts. Only threads with at least
20 tweets and participation from at least 10 distinct users were
included.
3) Influential Users: Our methodology involved identifying
influential users within each dataset based on their ability to
engage substantial audience interactions, primarily measured
by the total number of likes their posts received. Influential
users were determined by sorting all users in descending order
based on their like counts and selecting those at the top of
this list (Table II), which indicates a significant impact on
online discourse. Although Table II shows only the top five
for illustrative purposes, our analysis included a broader set of
influential figures, with 2,103 users for the gun control dataset
and 3,701 for the climate change dataset. We examined 5,500
gun control and 8,421 climate change conversations initiated
by these users over a period of one year.
B. Quantifying Polarization with E/I Index
Our study employs a multi-model sentiment analysis ap-
proach using V ADER, BERTweet, and RoBERTa to evaluate

Fig. 1: Interaction networks with and without a specific conversation. The left panel displays the network including the
conversation (circled), while the right panel shows the network without it, highlighting the dense areas where ongoing
interactions among the influencer’s followers persist through other conversations.
TABLE I: Dataset details
Dataset Timeline Total Tweets (million) Total Conversations (million) Total Users (million) #likes (billion) #replies (million) #retweets (billion)
Gun Control 2022.01.01 - 2022.12.31 2.65 2.26 0.94 1.46 120.69 7.49
Climate Change 2021.06.01 - 2022.05.31 7.24 6.46 2.04 30.39 149.05 2.64
TABLE II: Top 5 influential users for each dataset
Dataset User Tweet Count Total Likes (million) Stance
Gun-
Control
User 1 1,241 272.40 anti
User 2 1,665 66.79 pro
User 3 1,750 37.74 pro
User 4 1,760 31.75 pro
User 5 746 22.81 pro
Climate-
Change
User 1 1,766 190.47 believe
User 2 76 185.99 believe
User 3 1,945 57.79 believe
User 4 33 26.43 believe
User 5 55 24.12 believe
the emotional content of tweets. This comprehensive senti-
ment profiling forms the basis for our subsequent analysis of
affective polarization.
We utilize the E/I Index methodology, adopted from Tyagi
et al. [10], to quantify affective polarization by measuring the
ratio of external (between-group) to internal (within-group)
interactions within Twitter discourse networks. This method
allows us to assess the degree of in-group cohesion and out-
group engagement. The E/I Index is derived by evaluating
the balance of positive and negative interactions within and
between groups. We compute the difference between the E/I
indices of positive and negative interactions to discern the
polarization valence. For further details on the computations
and equations underlying the E/I Index, we refer readers to
the original work by Tyagi et al. [10].
This approach is akin to the P-Index proposed by Guerra
et al. [30], albeit tailored specifically for Twitter’s unique
interaction dynamics. Through this framework, we focus on:
• In-group Solidarity: Gauged through the frequency and
sentiment of interactions within a group.
• Out-group Engagement: Characterized by the nature of
interactions across different stance groups, often high-
lighting conflict or disagreement.
In practical applications, such as in gun control debates, this
index helps us identify and describe patterns like Pro-Anti and
Anti-Pro, indicating shifts from passive support or opposition
to active advocacy or contention. While Bestvater et al. [31]
caution against using sentiment as a standalone measure for
polarization or stance, our study integrates these insights as
part of a broader, multi-faceted approach to understanding
affective polarization.
C. User Stance Labeling using Graph Neural Networks
(GNNs)
Our approach to user stance labeling employs a two-stage
pipeline that integrates textual and social interaction data, as
established in [32].
a) Initial Label Generation: Our stance labeling process
begins with the construction of a user-hashtag bipartite graph,
where one set of nodes represents users and the other set
represents hashtags used in their tweets. This graph forms the
basis for applying a reciprocal label propagation algorithm,
initially assigning stance labels based on users’ engagements
with specific hashtags. We identify seed labels from a subset of
users who frequently use hashtags that are strongly associated

(a) Gun Control Dataset
(b) Climate Change Dataset
Fig. 2: Conversation characteristics: (a) Gun Control and (b)
Climate Change topics, displaying the frequency of conversa-
tions by number of tweets (left) and number of users (right).
with known stances. This preliminary method generates labels
for approximately 500,000 users in the gun control dataset and
1.6 million users in the climate change dataset, providing an
initial but incomplete picture of user stances, and does not
take into account any social interactions between users.
b) Expanding Stance Labeling with GNNs: To enhance
and refine our stance labeling, we construct a comprehensive
user-user interaction network. In this network, nodes represent
users and edges signify direct interactions such as retweets or
replies. Leveraging BERTweet, we embed the textual content
of tweets into node features to capture linguistic nuances.
Subsequently, we employ a Graph Neural Network (GNN)
classifier (GraphSAGE), trained on the interaction graph with
seed labels derived from the initial hashtag-based method.
This two-stage approach integrates both textual content and
interaction patterns to predict user stances more accurately,
resulting in expanded stance labels for 2.6 million users in
the gun control context and 4.7 million users in the climate
change context. Moreover, the GNN predicts node labels by
generating a probability distribution over possible stances for
each user. Detailed information on the GNN’s architecture,
parameter settings, and performance evaluation can be found
in the work by Melton et al. [32].
c) Optimization of Classification Thresholds: To more
accurately delineate users into distinct stance groups, we
adopted a dual-threshold strategy for classifying user stances
based on their stance probability scores. We identified op-
timal thresholds, Threshold 1 and Threshold 2, through a
comprehensive grid search methodology designed to refine the
decision boundary by optimizing the F1 score. This process
entailed meticulously comparing predicted labels against a
benchmark set comprising both heuristic stances derived from
our initial hashtag-based labeling and a subset of users manu-
ally annotated by domain experts. This dual-source validation
approach ensured robustness in threshold selection by integrat-
ing empirical data with expert judgment. The final thresholds
were determined as follows: Threshold 1 (≤ 0.40) for identi-
fying ’pro’ or ’believers’ stances, and Threshold 2 ( ≥ 0.60)
for ’anti’ or ’disbelievers’. Users with probabilities falling
between these thresholds were classified as ’undecided’, and
subsequently, their data were excluded from further analysis
in both datasets.
D. Approach to Quantifying Influencer Impact on Affective
Polarization
We center our methodology around the concept of a coun-
terfactual scenario within a subgraph of influence, where
polarization scores are calculated in scenarios both with and
without specific influencer-led conversations, as illustrated in
Figure 1. This comparative method is crucial for isolating
the shifts in polarization attributable to these conversation
networks, providing insights into how individual conversations
can sway public sentiment.
To enhance our analysis, we focus on constructing sub-
graphs around specific influencers and their follower networks,
recognizing that the comprehensive interaction graphs on plat-
forms like Twitter, which involve millions of daily interactions,
can obscure the effects of smaller-scale conversation networks.
For instance, in our detailed case study of ’User X’s Twitter in-
teractions, we selectively identified a subset of approximately
1,000 followers from a larger pool of 15,000 active users.
We constructed a subgraph that included these followers and
their adjacent connections, encompassing around 2,000 users
in total.
This subgraph methodology provides a focused lens through
which we can observe and analyze the polarization dynamics
more clearly. Initially, we compute the polarization within this
subgraph by including ’User X’s conversation. Subsequently,
to distinctly understand the conversation’s specific impact,
we recalibrated the polarization after removing the 400 users
directly involved in the conversation. This technique of con-
trasting polarization scores with and without the conversation
offers a transparent view of how specific conversations influ-
ence the network’s polarization dynamics.
By focusing on influencer-centric subgraphs, we uncover
the subtle yet significant impacts of specific conversations on

affective polarization, avoiding the dilution of findings by the
broader network’s noise.
IV. R ESULTS
Our analysis reveals a temporal sensitivity in polarization,
underscored by fluctuations that correspond closely with real-
world events and influencer-led conversations. Specifically, our
temporal examination—illustrated in Figures 3 and 4—high-
lights notable shifts in polarization within the contexts of gun
control and climate change discourse.
For instance, in Figure 3a during the summer of 2022, the
gun control dataset exhibited significant spikes in the daily
Twitter conversation, correlating with high-profile shooting
incidents in the United States. This period, notably marked
by the tragic Texas Robb Elementary School shooting, saw
intensified influencer activity leading conversations that either
amplified or attempted to bridge divides in public sentiment.
Similarly, in the climate change discourse (Figure 3b), pivotal
events such as the release of the Intergovernmental Panel on
Climate Change (IPCC) report and the United Nations Climate
Change Conference were mirrored by peaks, pointing to the
reactive nature of online discourse to global climate events.
Following these events, Figure 4 illustrates how influential-
led conversation changes the dynamic of polarization. For
both, gun-control and climate-change datasets, we observe
that when a certain event occurs, the polarization score in-
creases compared to the situation it was before the event
happened. Statistical significance tests confirm that many of
these observed shifts are significant, reinforcing polarization’s
temporal alignment with external events. These observations
highlight the critical role of influencers in steering the conver-
sation and the powerful impact that influencers and real-world
events can have affecting the polarization landscape.
A. Effect of an Influential-led Conversation
The shifts in polarization are quantified by examining the
changes in polarization scores when specific influencer-led
conversation is either included or excluded from the analysis.
This approach helps isolate the direct impact of a single
conversation on the overall polarization score that day.
For example, as illustrated in Table III, the removal of
a conversation by ’User 3’, a prominent disbeliever in cli-
mate change, resulted in a notable shift in the polarization
scores. Specifically, the polarization score for the believer-to-
disbeliever direction increased from 0.471 to 0.633, indicating
a more pronounced divide when the disbeliever’s influence
was absent from the conversation. This change, representing a
magnitude of 0.162 in the polarization score, underscores the
significant role that influencer-led interactions play in shaping
public sentiment and polarization.
Similarly, in the context of gun control as detailed in
Table IV, the exclusion of a conversation led by an anti-gun
control user (i.e. ’User 2’) resulted in a decrease in the anti-pro
polarization score. This demonstrates how conversations led
by users opposed to gun control amplify polarization towards
anti-gun stances when present, and reduce it when removed.
(a) Gun Control Dataset
(b) Climate Change Dataset
Fig. 3: Daily conversation counts over the specified time
frame, stratified by topic: (a) Gun Control and (b) Climate
Change.
B. Insight of Influential Users
In this section, we examine the collective influence of
conversations initiated by influential users on shaping public
sentiment and polarization across various themes. We employ
a systematic approach to quantify the impact of these users
by assessing the frequency and effect of their conversations
on polarization shifts.
Tables V and VI present data on influential users who ac-
tively engage in discussions and initiate several conversations
related to gun control and climate change, respectively. These
tables reveal the percentage of conversations that increase or
decrease polarization, given a specified number of conversa-
tions within the context of these topics, thereby illuminating
the effects of influential users on social media dynamics.
C. Insight of Conversations Within Stance-Group
Table VII provides a more comprehensive view by analyzing
all the conversations initiated by users within a certain stance.
Interestingly, we observe that conversations led by users with
anti or disbeliever stances often result in decreased polarization
compared to their opposing stance group. However, it’s impor-
tant to note the observational nature of our approach; while

(a) Texas Shooting
 (b) Illinois Shooting
 (c) Colorado Shooting
(d) Hurricane Ida
 (e) Heat Wave
 (f) IPCC Annual Report
Fig. 4: Temporal dynamics of polarization scores in response to events. The top trio of subfigures (a-c) illustrates changes
in polarization preceding and following events related to gun control, with ’(P → A)’ denoting shifts from pro-to-anti gun
control stance and ’(A → P)’ denoting shifts from anti-to-pro stance. The bottom trio (d-f) depicts similar changes for climate
change-related events, with ’(B → D)’ representing shifts from believe-to-disbelieve in climate change and ’(D → B)’ for
shifts from disbelieve-to-believe stance direction. P-values indicate the statistical significance of changes, confirming that these
shifts are not random but are influenced by the events.
TABLE III: Climate Change Dataset: The effect of a single conversation by influential users on daily polarization score.
User User’s Stance Number of Tweets in the Conversation Number of Followers in the Conversation (#disbelieve / #believe) Number of Followers Interacting on That Day (#disbelieve / #believe) Stance Direction Polar. Score Without Conv. Polar. Score With Conv.
User 1 believe 104 41 / 50 904 / 1,332 disbelieve → believe -0.091 -0.135 believe → disbelieve 0.463 0.398
User 2 believe 187 131 / 24 457 / 333 disbelieve → believe 0.115 0.185 believe → disbelieve 0.378 0.402
User 3 disbelieve 157 68 / 14 302 / 100 disbelieve → believe -0.137 -0.136 believe → disbelieve 0.633 0.471
User 4 believe 134 51 / 37 356 / 356 disbelieve → believe 0.149 0.181 believe → disbelieve -0.228 -0.247
User 5 disbelieve 66 43 / 2 395 / 86 disbelieve → believe 0.144 0.152 believe → disbelieve 0.248 0.237
TABLE IV: Gun Control: The effect of a single conversation by influential users on daily polarization score.
User User’s Stance Number of Tweets in the Conversation Number of Followers in the Conversation (#anti / #pro) Number of Followers Interacting on That Day (#anti / #pro) Stance Direction Polar. Score Without Conv. Polar. Score With Conv.
User 1 pro 746 334 / 325 1,211 / 1,040 anti → pro 0.147 0.252 pro → anti 0.247 -0.200
User 2 anti 1,333 497 / 391 856 / 707 anti → pro 0.079 0.229 pro → anti 0.220 -0.087
User 3 pro 57 20 / 22 312 / 356 anti → pro 0.085 0.099 pro → anti -0.022 0.121
User 4 anti 164 37 / 100 176 / 286 anti → pro 0.247 0.121 pro → anti 0.204 0.241
User 5 pro 129 16 / 50 867 / 1,879 anti → pro 0.043 0.041 pro → anti 0.069 0.085
it reveals significant insights into the dynamics of influencer
conversations, it does not assert direct causation. Overall,
the insights gleaned from these influencer-led conversations
across different thematic areas demonstrate the critical role
of influential users in modulating the affective landscape of
online communities.

TABLE V: Gun Control Dataset: Impact of conversation initialized by influential authors (Twitter users) on polarization scores.
The ’% increase’ or ’% decrease’ denotes the percentage of cases, (how) polarization score changes upon adding a conversation
compared to the total number of conversations.
Twitter User User Type Stance (Gun Control) Number of Conversations Polarization: Change (pro → anti) Polarization: Change (anti → pro)
User 1 Media Outlet anti 5 100.0 % - decrease 100.0 % - increase
User 2 Media Outlet pro 6 66.67 % - decrease 100.0 % - decrease
User 3 Commentator pro 9 88.89 % - decrease 77.78% - decrease
User 4 Journalist anti 18 88.89 % - decrease 61.11% - increase
User 5 Politician pro 7 85.71 % - increase 85.71% - decrease
TABLE VI: Climate Change Dataset: Impact of conversation initialized by influential authors (Twitter users) on polarization
scores. The ’% increase’ or ’% decrease’ denotes the percentage of cases, (how) polarization score changes upon adding a
conversation compared to the total number of conversations.
Twitter User User Type Stance (Climate Change) Number of Conversations Polarization: Change (believe → disbelieve) Polarization: Change (disbelieve → believe)
User 1 Scientific Org. believe 5 60.00% - decrease 100.0 % - increase
User 2 Public Figure disbelieve 5 80.00% - decrease 100.0 % - increase
User 3 Media Personality disbelieve 8 50.00% - increase 87.5 % - decrease
User 4 Politician believe 7 85.71% - decrease 57.14 % - decrease
User 5 Media Outlet believe 41 51.22% - decrease 85.37 % - increase
TABLE VII: Details of conversations’ effects based on stances for both gun control and climate change. The ’% increase’ or
’% decrease’ denotes the percentage of cases, (how) polarization score changes upon adding a conversation compared to the
total number of conversations.
Dataset Stance Number of Conversations Polarization Score: Change
Gun Control
(pro → anti) (anti → pro)
pro 1,940 63.40% - decrease 52.99% - increase
anti 1,704 55.52% - decrease 53.28% - decrease
Climate Change
(believe → disbelieve) (disbelieve → believe)
believe 1,561 50.99% - decrease 64.25% - increase
disbelieve 596 50.67% - decrease 58.22% - decrease
V. C ONCLUSION
This study provides a detailed analysis of the mechanics
of affective polarization on social media, particularly high-
lighting the crucial role of influential users in modulating
public sentiment on platforms like Twitter. By implementing a
counterfactual framework, which evaluates scenarios with and
without specific influencer-led conversations, we offer a unique
methodological contribution that allows us to isolate and
quantify the influence of such conversations on the dynamics
of polarization. Our findings demonstrate that influencers have
the potential to amplify or mitigate divisiveness across polariz-
ing topics like gun control and climate change. We reveal how
subtle shifts in influencer-driven dialogues can significantly
affect public discourse by employing a comparative analysis
coupled with computational techniques, such as subgraph
construction. This approach deepens our understanding of how
specific conversations impact polarization that are critical to
social media dynamics.
Despite these promising results, our study faces method-
ological challenges, particularly due to limitations inherent in
calculating the polarization scores based on sentiment analysis.
This depends on the presence of positive or negative words in
tweets and it is negatively impacted by the sporadic nature of
meaningful social media interactions. These challenges under-
score the complexity of capturing the sophisticated landscape
of online discourse and point to the need for developing
more refined metrics and methodologies that leverage current
advancements in language understanding that go beyond sen-
timent analysis.
ACKNOWLEDGEMENT
The research was sponsored by the Army Research Office
and was accomplished under Grant Number W911NF-22-1-
0035. The views and conclusions contained in this document
are those of the authors and should not be interpreted as
representing the official policies, either expressed or implied,
of the Army Research Office or the U.S. Government. The
U.S. Government is authorized to reproduce and distribute
reprints for Government purposes notwithstanding any copy-
right notation herein.

REFERENCES
[1] P. Dahlgren, Media and political engagement: Citizens, communication
and democracy. Cambridge University Press, 2009.
[2] D. Chambers, Social media and personal relationships: Online intima-
cies and networked friendship . Springer, 2013.
[3] O. Yair, “A note on the affective polarization literature,” Available at
SSRN 3771264, 2020.
[4] X. Yu, M. Wojcieszak, and A. Casas, “Affective polarization on social
media: In-party love among american politicians, greater engagement
with out-party hate among ordinary users,” 2021.
[5] T. J. Rudolph and M. J. Hetherington, “Affective polarization in political
and nonpolitical settings,” International Journal of Public Opinion
Research, vol. 33, no. 3, pp. 591–606, 2021.
[6] D. Feldman, A. Rao, Z. He, and K. Lerman, “Affective polarization in
social networks,” arXiv preprint arXiv:2310.18553 , 2023.
[7] J. Serrano-Puche, “Digital disinformation and emotions: exploring the
social risks of affective polarization,” International Review of Sociology,
vol. 31, no. 2, pp. 231–245, 2021.
[8] T. O. Harel, J. K. Jameson, and I. Maoz, “The normalization of hatred:
Identity, affective polarization, and dehumanization on facebook in the
context of intractable political conflict,” Social Media+ Society , vol. 6,
no. 2, p. 2056305120913983, 2020.
[9] L. Jenke, “Affective polarization and misinformation belief,” Political
Behavior, pp. 1–60, 2023.
[10] A. Tyagi, J. Uyheng, and K. M. Carley, “Affective polarization in online
climate change discourse on twitter,” in 2020 IEEE/ACM International
Conference on Advances in Social Networks Analysis and Mining
(ASONAM), pp. 443–447, IEEE, 2020.
[11] J. Beel, T. Xiang, S. Soni, and D. Yang, “Linguistic characterization
of divisive topics online: Case studies on contentiousness in abortion,
climate change, and gun control,” in Proceedings of the International
AAAI Conference on Web and Social Media , vol. 16, pp. 32–42, 2022.
[12] B. K. Johnson, R. L. Neo, M. E. Heijnen, L. Smits, and C. van
Veen, “Issues, involvement, and influence: Effects of selective exposure
and sharing on polarization and participation,” Computers in Human
Behavior, vol. 104, p. 106155, 2020.
[13] S. Balietti, L. Getoor, D. G. Goldstein, and D. J. Watts, “Reducing
opinion polarization: Effects of exposure to similar people with differing
political views,” Proceedings of the National Academy of Sciences ,
vol. 118, no. 52, p. e2112552118, 2021.
[14] R. Recuero, G. Zago, and F. Soares, “Using social network analysis and
social capital to identify user roles on polarized political conversations
on twitter,” Social media+ society, vol. 5, no. 2, p. 2056305119848745,
2019.
[15] P. T ¨ornberg, C. Andersson, K. Lindgren, and S. Banisch, “Modeling the
emergence of affective polarization in the social media society,” PLoS
One, vol. 16, no. 10, p. e0258259, 2021.
[16] N. Gillani, A. Yuan, M. Saveski, S. V osoughi, and D. Roy, “Me, my
echo chamber, and i: introspection on social media polarization,” in
Proceedings of the 2018 World Wide Web Conference , pp. 823–831,
2018.
[17] J. N. Druckman, S. Klar, Y . Krupnikov, M. Levendusky, and J. B. Ryan,
“(mis) estimating affective polarization,” The Journal of Politics, vol. 84,
no. 2, pp. 1106–1117, 2022.
[18] M. Su ´arez Estrada, Y . Juarez, and C. Pi ˜na-Garc´ıa, “Toxic social media:
Affective polarization after feminist protests,” Social Media+ Society ,
vol. 8, no. 2, p. 20563051221098343, 2022.
[19] K. A. Heatherly, Y . Lu, and J. K. Lee, “Filtering out the other side?
cross-cutting and like-minded discussions on social networking sites,”
New Media & Society , vol. 19, no. 8, pp. 1271–1289, 2017.
[20] L. Mason, “A cross-cutting calm: How social sorting drives affective
polarization,” Public Opinion Quarterly , vol. 80, no. S1, pp. 351–377,
2016.
[21] M. Cinelli, G. De Francisci Morales, A. Galeazzi, W. Quattrociocchi, and
M. Starnini, “The echo chamber effect on social media,” Proceedings
of the National Academy of Sciences , vol. 118, no. 9, p. e2023301118,
2021.
[22] S. Lee, H. Rojas, and M. Yamamoto, “Social media, messaging apps,
and affective polarization in the united states and japan,” Mass Commu-
nication and Society , vol. 25, no. 5, pp. 673–697, 2022.
[23] S. Iyengar, Y . Lelkes, M. Levendusky, N. Malhotra, and S. J. Westwood,
“The origins and consequences of affective polarization in the united
states,” Annual review of political science , vol. 22, pp. 129–146, 2019.
[24] A. Tyagi, J. Uyheng, and K. M. Carley, “Heated conversations in a
warming world: affective polarization in online climate change discourse
follows real-world climate anomalies,” Social Network Analysis and
Mining, vol. 11, pp. 1–12, 2021.
[25] E. C. Connors, “Social desirability and affective polarization,” Public
Opinion Quarterly, vol. 87, no. 4, pp. 911–934, 2023.
[26] M. Nordbrandt, “Affective polarization in the digital age: Testing the
direction of the relationship between social media and users’ feelings
for out-group parties,” New media & society , vol. 25, no. 12, pp. 3392–
3411, 2023.
[27] A. D. Kramer, J. E. Guillory, and J. T. Hancock, “Experimental evi-
dence of massive-scale emotional contagion through social networks,”
Proceedings of the National academy of Sciences of the United States
of America, vol. 111, no. 24, p. 8788, 2014.
[28] M. Cha, H. Haddadi, F. Benevenuto, and K. Gummadi, “Measuring user
influence in twitter: The million follower fallacy,” in Proceedings of the
international AAAI conference on web and social media , vol. 4, pp. 10–
17, 2010.
[29] J. M. Betts and A.-M. Bliuc, “The effect of influencers on societal
polarization,” in 2022 Winter Simulation Conference (WSC) , pp. 370–
381, IEEE, 2022.
[30] P. Guerra, W. Meira Jr, C. Cardie, and R. Kleinberg, “A measure of
polarization on social media networks based on community boundaries,”
in Proceedings of the international AAAI conference on web and social
media, vol. 7, pp. 215–224, 2013.
[31] S. E. Bestvater and B. L. Monroe, “Sentiment is not stance: Target-aware
opinion classification for political text analysis,” Political Analysis ,
vol. 31, no. 2, pp. 235–256, 2023.
[32] J. Melton, S. Reid, G. Terejanu, and S. Krishnan, “Two-stage stance
labeling: User-hashtag heuristics with graph neural networks,” arXiv
preprint arXiv:2404.10228, 2024.
