---
title: 'SAGraph: A Large-Scale Social Graph Dataset with Comprehensive Context for Influencer Selection
  in Marketing'
url: https://arxiv.org/abs/2403.15105
category: digital-marketing
subcategory: measurement
date: 2024-03
venue: arXiv (Cornell University)
authors:
- Xiaoqing Zhang
- Yuhan Liu
- Jianzhou Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2403.15105
pages: 10
chars: 53141
fetched_at: '2026-11-08T12:57:13+00:00'
kb_version: 1
---

# SAGraph: A Large-Scale Social Graph Dataset with Comprehensive Context for Influencer Selection in Marketing

SAGraph: A Large-Scale Social Graph Dataset with
Comprehensive Context for Influencer Selection in Marketing
Xiaoqing Zhang
Gaoling School of Artificial
Intelligence, Renmin University of
China
Beijing, China
xiaoqingz@ruc.edu.cn
Yuhan Liu
Gaoling School of Artificial
Intelligence, Renmin University of
China
Beijing, China
yuhan.liu@ruc.edu.cn
Jianzhou Wang
Moonshot AI
Beijing, China
wangjianzhou@msh.team
Zhenxing Hu
Moonshot AI
Beijing, China
huzhenxing@msh.team
Xiuying Chen∗
Mohamed bin Zayed University of
Artificial Intelligence
Abu Dhabi, UAE
xiuying.chen@mbzuai.ac.ae
Rui Yan∗
Gaoling School of Artificial
Intelligence, Renmin University of
China
Beijing, China
ruiyan@ruc.edu.cn
Abstract
Influencer marketing campaign success heavily depends on identi-
fying key opinion leaders who can effectively leverage their cred-
ibility and reach to promote products or services. The selecting
influencers process is vital for boosting brand visibility, foster-
ing consumer trust, and driving sales. While traditional research
often simplifies complex factors like user attitudes, interaction
frequency, and advertising content, into simple numerical values.
However, this reductionist approach fails to capture the dynamic
nature of influencer marketing effectiveness. To bridge this gap,
we present SAGraph, a novel comprehensive dataset from Weibo
that captures multi-dimensional marketing campaign data across
six product domains. The dataset encompasses 345,039 user pro-
files with their complete interaction histories, including 1.3M com-
ments and 554K reposts across 44K posts, providing unprecedented
granularity in influencer marketing dynamics. SAGraph uniquely
integrates user profiles, content features, and temporal interac-
tion patterns, enabling in-depth analysis of influencer marketing
mechanisms. Experimental results using both traditional baselines
and state-of-the-art large language models (LLMs) demonstrate
the crucial role of content analysis in predicting advertising effec-
tiveness. Our findings reveal that LLM-based approaches achieve
superior performance in understanding and predicting campaign
success, opening new avenues for data-driven influencer marketing
strategies. We hope that this dataset will inspire further research:
https://github.com/xiaoqzhwhu/SAGraph/.
∗Corresponding authors.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
SIGIR ’25, Padua, Italy
© 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/2018/06
https://doi.org/XXXXXXX.XXXXXXX
CCS Concepts
• Information systems→ Social Advertising.
Keywords
Ads, Influencer Selection, Agent Simulation, LLM
ACM Reference Format:
Xiaoqing Zhang, Yuhan Liu, Jianzhou Wang, Zhenxing Hu, Xiuying Chen,
and Rui Yan. 2018. SAGraph: A Large-Scale Social Graph Dataset with Com-
prehensive Context for Influencer Selection in Marketing. In Proceedings of
(SIGIR ’25). ACM, New York, NY, USA, 10 pages. https://doi.org/XXXXXXX.
XXXXXXX
Figure 1: (a) An illustration of influence factors. (b) The pro-
cess of influencer selection involves the information diffu-
sion across various influence factors. “𝐼1” and “𝐼2” represent
influencers selected due to their larger influence.
1 Introduction
Social networks and media platforms have revolutionized our in-
teractions and information sharing, with influencers significantly
impacting their followers’ decisions through recommendations
on products, services, and lifestyle choices. In digital advertis-
ing, promoters strategically select a limited number of influencers
arXiv:2403.15105v3  [cs.SI]  27 May 2025

SIGIR ’25, July 13–18, 2025, Padua, Italy Zhang et al.
Table 1: Comparison of related datasets. ‘Net’ denotes the
graph structure. ‘Interaction’ denotes the interaction be-
tween different nodes in the Net. ‘Text’ denotes the inter-
action details that are described in text format.
Dataset Scenario Net Interaction Text Nodes
Blog [15] knowledge ✓ × × 45,000
Reddit [4] knowledge × ✓ ✓ -
Wiki Vote [17] rumor ✓ ✓ × 7,115
Tweet List [17] rumor ✓ × × 23,370
Google+ [17] rumor ✓ ✓ × 23,628
Email [16] rumor ✓ ✓ × 1,005
Facebook [14] rumor ✓ × × 135
Twitter [12] voting × × ✓ 38,020
Twitter [26] election × × ✓ 2
Twitter [11] marketing × ✓ ✓ 3,853
Twitter [23] marketing ✓ ✓ ✓ 37
SAGraph marketing ✓ ✓ ✓ 345,039
to maximize their product’s influence and visibility in the mar-
ket [13, 23, 25, 32]. This approach benefits both advertisers and
consumers alike. As shown in Figure 1(a), key factors in influencer
selection include relationships, number of friends, preferences, and
behaviors such as comments and reposts. Figure 1(b) illustrates the
information diffusion process, which leads influencers𝐼1 and𝐼2 to
gain large influence due to their extensive reach. Numerous studies
have focused on influencer selection, leading to the development of
datasets designed to enhance the effectiveness of influencer market-
ing strategies. For example, Lahuerta-Otero and Cordero-Gutiérrez
analyzed 30,000 tweets from 3,853 users to explore how factors such
as writing style, user sentiment, and follower count impact the cal-
culation of influence. Additionally, Mallipeddi et al . constructed
a Twitter dataset featuring profiles of 37 influencers who posted
18,571 tweets. By collecting retweet data, they built a social net-
work to further investigate the effects of repeated exposure and the
forgetting effect on influence calculation.
Expanding on this, datasets across various scenarios also concen-
trate on selecting important nodes within a graph, which is essen-
tially similar to the influencer selection task. For example, Leskovec
et al. used extensive links to construct a social network of blogs. By
analyzing the social network’s connections, they found influential
blogs for spreading information effectively. Another widely used
real-world dataset, SNAP[18], includes Wiki Vote, Twitter Lists, and
Google+ datasets. These datasets consist of directed social networks
where nodes represent users and edges represent user interactions,
such as voting on Wikipedia edits, following on Twitter, or adding
users to circles on Google+. All datasets are for influencer selection,
particularly to combat rumors in social networks.
However, a significant issue with existing datasets is that they
oversimplify complex social networks. In marketing scenarios, for
example, the network is often reduced by filtering tweets or user
nodes based on keywords, which undermines the integrity of the
social network. This oversimplification not only erases the intri-
cate relationships within the network but also leads to misjudg-
ments about the potential influence of individuals or content. In
non-marketing contexts, social networks are often distilled into
numerical representations, ignoring the subtle semantic meanings
in text and the emotional nuances of interactions. People’s opin-
ions are nuanced and diverse, and the mechanisms of influence
are intricate. For example, the persuasive power of an influencer’s
message can be deeply intertwined with the language used, the
context in which it is presented, and the emotional resonance it
creates with the audience, aspects that are not fully captured by
numerical metrics alone.
To address this gap, we present a comprehensive social advertis-
ing graph dataset, SAGraph, which includes multi-domain contex-
tual data sourced from Weibo [6, 20, 30], one of the most popular
social networking platforms. The dataset includes user informa-
tion with domain-specific preferences such as interests, post data,
and interaction context, all tailored for advertising and marketing
scenarios. Specifically, we begin with a set of ground truth influ-
encers—product promoters—and a group of influencers who share
the same domain and interests but are not product promoters. For
each user, we collect personal information such as friend numbers,
bio details, posts, and interaction data, which includes comments
and reposts. Subsequently, we proceed iteratively to expand the
graph. In summary, our graph centers around 6 product campaigns
in diverse domains, encompasses 345,039 users, each with their
profile information, and published posts, and includes interaction
data comprising 1,302,109 comments and 554,629 reposts. In Ta-
ble 1, we compare our dataset with existing ones. SAGraph is the
first comprehensive social advertising graph dataset with detailed
elements that integrate users, products, social relationships, in-
teractions, and textual information to simulate real-world social
environments. It significantly surpasses previous datasets in terms
of scale, completeness, and domain diversity.
For evaluation, we experiment with several influencer selection
baselines, including those in the simulation, proxy, sketch, and
context-aware categories, as well as the latest LLMs on SAGraph.
The experiments show that classic baselines, which do not con-
sider textual information, perform poorly on this task. Meanwhile,
context-aware methods and LLMs show great potential in modeling
user profiles and influencer prediction.
The contribution of our work can be summarized as follows:
• A comprehensive social advertising graph dataset : We in-
troduce the large-scale SAGraph dataset, featuring domain-specific
interest tags from Weibo, which is publicly available for advertising
campaigns. This dataset includes a comprehensive graph structure
and rich textual data from user profiles and interaction content,
supporting the development of advanced algorithms for influencer
selection and consumer behavior analysis.
• Demonstration of benchmarks: We evaluate influencer se-
lection baselines on our dataset, showing text’s role in influence
calculation. For advertising, we offer an LLM-based tool to improve
influencer selection using rich text, aiding strategic campaign deci-
sions to increase brand visibility and sales. This underscores the
dataset’s practical value and potential for marketing research.
2 Related Work
Influencer Selection Methods. Influencer selection methods have
significant potential for applications in areas such as public opin-
ion monitoring, advertising promotion, and epidemic prediction.

SAGraph: A Large-Scale Social Graph Dataset with Comprehensive Context for Influencer Selection in Marketing SIGIR ’25, July 13–18, 2025, Padua, Italy
Figure 2: An example of the SAGraph, which includes users with interest tags, ads as posts, and evolving interaction data.
Traditional simulation-based methods model information diffu-
sion using a large number of Monte Carlo(MC) simulations to esti-
mate the spread of influence. Notable methods include CELF [15],
CELF++ [7], and GREEDY [9]. While these methods are adaptable
to various diffusion models, they come with a substantial compu-
tational cost. To identify near-optimal seed sets more efficiently,
proxy-based methods approximate the spread of influence using
proxies like PageRank, shortest paths, and others. These methods
generally have lower computational complexity and can deliver
results in less time. Methods include EIGEN-CENTRALITY [ 34],
DEGREE [24], SIGMA [29], and PI [33]. However, these methods
lack theoretical approximation guarantees and are highly sensitive
to minor changes in network structure, often leading to unsta-
ble results. Sketch-based methods, on the other hand, precompute
“sketches” based on specific diffusion models and evaluate the spread
of influence on these sketches, avoiding the need for repeated time-
consuming MC simulations. While maintaining theoretical guaran-
tees, these methods significantly improve computational efficiency.
Representative examples include RIS [1], TIM [28], IMM [27], and
EaSyIM [5]. Additionally, to better simulate real-world information
diffusion and enhance result stability, context-aware methods in-
tegrate various contextual information such as topics, time, and
location. This approach improves influencer selection performance
by fully leveraging the potential of contextual data, enabling the
development of more effective influencer selection algorithms [22].
Influencer Selection Datasets. Influencer selection datasets
span multiple domains. In marketing, the Twitter dataset in [11] is
used to analyze the importance of text features for influence cal-
culation but does not address the construction of a social network.
Another Twitter dataset, which includes 37 influencers over a max-
imum period of 10 months, constructs a social network to examine
the impact of multiple exposures and forgetting effects on influence
calculation [23]. However, the network is small, and tweets were
filtered based on keywords, leading to missing information about
the influencers and an incomplete social network for the specified
group. In non-marketing domains, datasets such as Blog [15], Tweet
List [17], and Facebook [14] are based on user-following relation-
ships. By analyzing follower counts and the rate of content spread
over a specific period, influencers can be predicted. For datasets
containing interaction data, such as Wiki Vote [ 17], Email [ 16],
Google+ [17], and Twitter [23], the interactions are typically di-
rect, involving information dissemination through targeted emails,
knowledge sharing, and voting. The study in [10] identifies influ-
ential users on Twitter by analyzing the timing and popularity of
topic propagation. However, these datasets lack a comprehensive
analysis of user content and fail to capture the nuances of text-
based interactions and direct content feedback. As a result, they
are inadequate for supporting in-depth research on the sources of
influence, propagation factors, and propagation trajectories.
3 Dataset Overview
To our knowledge, there is no comprehensive benchmark dataset
that includes advertisement, influencer, influencee, and interaction
information within a social network. To fill this void, we compile
such a dataset from Weibo, one of China’s most widespread social

SIGIR ’25, July 13–18, 2025, Padua, Italy Zhang et al.
Algorithm 1 SAGraph Collection
1: Initialize the seed user set 𝑆 with𝑘 influencers’ IDs who have more
than 100k followers,𝐹 as the set of influencees.
2: Set the user queue𝑄𝑈 =𝑆, the post queue𝑄𝑃 =∅, the whole collection
rounds𝑁 = 6, the current iteration𝑖 = 0.
3: while 𝑖 <𝑁 do
4: while 𝑄𝑈 is not empty do
5: Dequeue a user𝑢 from𝑄𝑈 .
6: Collect the profile information of𝑢.
7: Fetch all the posts’s IDs from𝑢′𝑠 first page as𝑃𝑢.
8: Enqueue𝑃𝑢 to the queue of posts𝑄𝑃 .
9: end while
10: while 𝑄𝑃 is not empty do
11: Dequeue a post𝑝 from𝑄𝑃 .
12: Collect all interaction data under the post 𝑝 and select users
with more than 100k followers as the new seed users𝑈𝑝.
13: Enqueue𝑈𝑝 without duplication back into the queue𝑄𝑈 for
further data collection.
14: end while
15: end while
16: We organize users, profile information, posts, and interaction data into
our SAGraph dataset.
media platforms. In this section, we initially outline the schema
of the SAGraph, which encompasses advertising products, influ-
encer details, and interaction data. Subsequently, we elucidate our
collection strategy and finally, we describe the statistics of the data.
3.1 Dataset Schema
Advertising products. In our study, we identify and choose a trend-
ing product within each of the six domains—education, technology,
hygiene, skincare, linguistics, and home—for promotion. These
products include ‘Spark Thinking’, an educational platform that
fosters creativity and learning; the ‘Intelligent Floor Scrubber’, rep-
resenting advanced cleaning technology; the ‘Electric Toothbrush’,
used for oral hygiene; the ‘Ruby Face Cream’, for daily skincare;
the ‘ABCReading’, for encouraging reading and communication
for language enhancement, and the ‘SUPOR Boosted Showerhead’
for providing an invigorating shower experience at home. Each
product is chosen for its distinct appeal and market potential. The
advertising data encompasses the names of the promoted products,
their respective domains, and the promotional copy. We show the
translated version of all content in this paper.
Influencer details. For each influencer, we collect their profiles,
which include friend numbers, bio information, and the most re-
cent posts as part of the influencer details. The number of friends is
included to initially estimate the exposure range of influencer mar-
keting campaigns. Biographical details illuminate the influencer’s
areas of interest and expertise, aligning them with their audience’s
interests. Recent posts reflect current engagement topics, enabling
timely and targeted influencer strategies. For influencers in each
domain and their interacting influencees, we utilize the profiles and
historical interaction content to invoke GPT-4(gpt-4-1106-preview),
generating preferences such as interest tags for each user. This
text-rich dataset refines our selection of influencers for effective
marketing initiatives. Our influencers include at least four individ-
uals who are promoters as well as candidate influencers.
Interaction data . We collect the interaction data consisting of
reposts and comments originating from posts. Just like comments,
reposts also include text content that expresses opinions. Figure
2 illustrates the interaction detail of each influencer. For each mi-
croblog post, we collect comprehensive interaction information,
which includes not only direct interactions such as user comments
and reposts but also multiple interactions between users under the
host’s post and consecutive multi-round interactions of users. This
extensive data engagement guarantees a more holistic and multi-
faceted perspective on user interactions. Finally, we get a detailed
list of users interacting with the influencers.
3.2 Dataset Construction
3.2.1 Data Collection. Social networks based on follow-up rela-
tionships tend to be sparse, with the presence of inactive users
and fake accounts. To enrich our network with more meaningful
interaction data, we incorporate comments and reposts into the
social network construction process. First, we select at least four
bloggers who have promoted the assigned products. Utilizing the
Weibo platform, which regularly offers a curated list of related users
for each account—based on shared interests, follower overlap, and
similar domains—we proceed to choose additional users from this
list who have not engaged in product promotion. These selected
users, both promoters and non-promoters, serve as our initial seed
users, totaling ten. To ensure fairness, we select non-promoters
with a follower count comparable to that of the promoters. Next,
we collect all posts from these seed users’ pages and identify users
who have commented or reposted from the interaction data under
the posts to construct the nodes and edges for the social network.
To ensure continuous expansion of the social network, we iterate
this process six times, adhering to the Six Degrees of Separation
principle [8]. Each iteration we seek new seed users to expand our
collection of posts and interaction data. We specifically target users
with more than 100k followers within the already-established social
network to serve as our new seed users. In our data collection exper-
iment, we set the threshold at 100k followers to balance the recall
of users within the target domain while preventing the exponential
growth of the social network, which could disrupt the data collec-
tion process. By setting the 100k threshold, we ensure that the data
expansion remains stable, with each iteration growing by no more
than an order of magnitude of 10. The overall process is shown
in Social Advertisement Graph Collection Algorithm 1. SAGraph
is released under the Creative Commons CC-BY 4.0 license that
academics and industry may use.
3.2.2 Dataset Anonymization. We anonymize the collected user
information to ensure the protection of user privacy. First, we trans-
formed potentially revealing usernames and real names by assign-
ing each user a new ID and username. Next, we filtered sensitive
fields such as regions, locations, and gender. In interaction con-
tent, we replaced the original usernames with the transformed
ones and used special placeholders to handle sensitive information,
such as phone numbers. These measures effectively conceal users’
real information while preserving the original interaction relation-
ships through the generated user IDs and usernames. For detailed
processing steps, please refer to our GitHub repository.

SAGraph: A Large-Scale Social Graph Dataset with Comprehensive Context for Influencer Selection in Marketing SIGIR ’25, July 13–18, 2025, Padua, Italy
Table 2: Statistics of SAGraph across construction. ‘R’ represents the collection round.
Product
#Infuencers
#User #Interaction #Comment #Repost #Interaction Per #Follower Variance of #Followers Variance of #InteractionsR1 R2 R3 R4 R5 R6
Electric Toothbrush 10 17 26 44 46 48 43,611 163,016 88,214 74,804 3.73 120.12 97.9
Spark Thinking 10 11 17 35 88 201 58,510 490,431 390,718 99,713 8.38 167.17 134.66
Intelligent Floor Scrubber 10 20 27 58 98 190 63,619 370,176 269,769 100,407 5.82 200.21 130.35
Ruby Face Cream 10 11 12 14 19 55 66,248 126,859 76,349 50,510 1.91 132.65 108.3
ABCReading 10 14 25 41 90 206 70,258 458,513 343,882 114,631 6.52 225.16 149.1
SUPOR Boosted Showerhead 10 27 31 58 74 81 138,427 247,741 133,177 114,564 1.79 102.25 98.61
Table 3: Statistics of SAGraph across six domains.
Product Domain #User #Tagged User #Tags #Duplicated Tags #Influencers #Posts of Influencers #Prompted Influencers #Label Examples
Electric Toothbrush Hygiene 43,611 22,675 50,990 9,427 48 1,766 8 Healthy,Cleaning
Spark Thinking Education 58,510 27,413 74,831 11,311 201 34,058 5 Education,Parenting,Mathematics
Intelligent Floor Scrubber Technology 63,619 33,025 85,734 13,025 190 2,490 5 Digital,Technology
Ruby Face Cream Skincare 66,248 27,257 58,289 9,488 55 844 14 Beauty,Skincare,Makeup,Shopping
ABCReading Linguistics 70,258 34,341 88,546 13,107 206 3,176 4 Language,English
SUPOR Boosted Showerhead Home 138,427 121,649 228,761 19,050 81 1,848 6 Home,Daily Life,Furniture
3.2.3 Dataset Ethics. Our data construction adheres to Chapter
III, Process and Use of Data, from the Measures for Data Security
Management [3]. We only scrape content that is publicly acces-
sible and ensure its anonymization by removing all personally
identifiable information. Compared to previous work on Weibo
data [2, 19, 21, 31, 32], our processing procedures are more strin-
gent. We have also provided the complete code, including data
collection and anonymization process, allowing anyone to replicate
the acquisition of the SAGraph dataset easily. Additionally, we will
provide the original data upon request, subject to a thorough review
and upon signing a consent agreement, ensuring compliance with
our data use policies.
+\JLHQH (GXFDWLRQ 7HFKQRORJ\ 6NLQFDUH /LQJXLVWLFV +RPH
+\JLHQH(GXFDWLRQ7HFKQRORJ\6NLQFDUH/LQJXLVWLFV+RPH
     
     
     
     
     
     





3HUFHQWDJH
Figure 3: The percentage of user overlap across domains.
3.3 Dataset Statistics
The graph dataset statistics for each advertising product are shown
in Table 2. During the iterative process, noticeable variations are
observed in the rate of user expansion across different domains.
Products like the Electric Toothbrush, Ruby Face Cream, and SUPOR
Boosted Showerhead exhibit a steady rise in new seed users. While
domains like ABCReading, Spark Thinking, and Intelligent Floor
Scrubber experience a pronounced escalation in the recruitment of
seed users, showing a trend of doubling with each successive itera-
tion. This trend aligns with the interaction metrics of these domains.
The former group has a lower variance of 101.6 in user interactions,
indicating stable and focused engagement. In contrast, the latter
group displays higher interaction rounds of 6 per follower and a
larger variance of 138, suggesting a dynamic and swiftly growing
user base. These observations highlight the intricate dynamics of
user engagement and expansion across various markets.
The statistics for the domain data are presented in Table 3 and
Figure 3. Table 3 offers a detailed overview of each domain, includ-
ing the number of users, the number of users with interest tags,
the total number of tags, the number of duplicated tags, the num-
ber of influencers, the number of posts made by influencers, and
the number of influencers who have conducted advertising promo-
tions within each domain. We also list the typical user labels for
each domain. Approximately 60% of users successfully generated
interest tags. Users without interest tags either lacked personalized
signatures or did not engage in interactions such as comments or
reposts, thus failing to provide sufficient data for the generation of
interest tags. On average, each influencer published over a hundred
posts, with a series of interactions forming around these posts, pro-
viding abundant information for user behavior analysis. Figure 3
illustrates the overlap of users across the six domains. The lower
triangle values represent the proportion of overlapping users in
the domain on the horizontal axis, while the upper triangle values
represent the proportion of overlapping users in the domain on
the vertical axis. Clear differences are observed among users in
different domains, with an average overlap rate of 18%. However,
some commonalities also emerge. For instance, overlapping users
from all domains represent a notable proportion in the education
domain (close to 20%), while the hygiene domain shows the least
overlap with other domains (around 3%). The highest overlap is
seen between the linguistics and technology domains, at 52%.

SIGIR ’25, July 13–18, 2025, Padua, Italy Zhang et al.
Table 4: Performance comparison of simulation baselines and proxy baselines on six datasets.
Models
Electric Toothbrush Spark Thinking
P@5 P@10 R@5 R@10 G@5 G@10 P@5 P@10 R@5 R@10 G@5 G@10
Simulation-based
CELF 0.40 0.40 0.40 0.80 0.51 0.73 0.20 0.20 0.25 0.50 0.15 0.28
CELF++ 0.40 0.20 0.40 0.40 0.32 0.32 0.40 0.20 0.50 0.50 0.64 0.64
GREEDY 0.20 0.30 0.20 0.60 0.15 0.37 0.40 0.20 0.50 0.50 0.64 0.64
Proxy-based
EIGEN-CENTRALITY 0.40 0.40 0.40 0.80 0.36 0.60 0.20 0.20 0.25 0.50 0.17 0.29
DEGREE 0.40 0.40 0.40 0.80 0.51 0.74 0.20 0.30 0.25 0.75 0.25 0.48
SIGMA 0.20 0.30 0.20 0.60 0.15 0.37 0.00 0.20 0.00 0.5 0.00 0.23
PI 0.40 0.30 0.40 0.60 0.37 0.46 0.00 0.20 0.00 0.50 0.00 0.23
Ruby Face Cream Intelligent Floor Scrubber
Simulation-based
CELF 0.40 0.40 0.29 0.57 0.35 0.46 0.00 0.20 0.00 0.50 0.00 0.26
CELF++ 0.40 0.20 0.29 0.29 0.51 0.41 0.40 0.20 0.50 0.50 0.64 0.64
GREEDY 0.40 0.20 0.29 0.29 0.51 0.41 0.40 0.20 0.50 0.50 0.44 0.44
Proxy-based
EIGEN-CENTRALITY 0.60 0.50 0.43 0.71 0.62 0.68 0.20 0.20 0.25 0.50 0.17 0.17
DEGREE 0.80 0.50 0.57 0.71 0.79 0.72 0.20 0.30 0.25 0.75 0.15 0.40
SIGMA 0.60 0.40 0.43 0.57 0.53 0.53 0.20 0.20 0.25 0.50 0.25 0.36
PI 0.60 0.40 0.43 0.57 0.66 0.63 0.20 0.20 0.25 0.50 0.25 0.36
ABC Reading SUPOR Boosted Showerhead
Simulation-based
CELF 0.20 0.20 0.25 0.50 0.39 0.50 0.20 0.20 0.25 0.50 0.20 0.33
CELF++ 0.40 0.30 0.50 0.75 0.35 0.49 0.20 0.10 0.25 0.25 0.25 0.25
GREEDY 0.20 0.10 0.25 0.25 0.39 0.39 0.40 0.20 0.50 0.50 0.64 0.64
Proxy-based
EIGEN-CENTRALITY 0.20 0.30 0.25 0.75 0.15 0.41 0.00 0.10 0.00 0.25 0.00 0.11
DEGREE 0.00 0.20 0.00 0.50 0.00 0.25 0.00 0.10 0.00 0.25 0.00 0.11
SIGMA 0.00 0.20 0.00 0.50 0.00 0.25 0.20 0.10 0.25 0.25 0.39 0.39
PI 0.00 0.20 0.00 0.50 0.00 0.25 0.20 0.10 0.25 0.25 0.39 0.39
4 Task Definition
Before introducing our dataset construction process, we first give
a formal definition of the influencer selection task. We denote a
social network as𝐺 =(𝑉,𝐸). Here, each node 𝑣𝑖 corresponds to
a user, including personal details such as friends number and bio
information.𝑉 is divided into two distinct categories: one is defined
as𝑉1 that comprises normal users with fewer than 100K follow-
ers, and the other is defined as𝑉2 that consists of seed users with
100K followers or more. The edges𝐸 denote various interactions
between users, including commenting and reposting content, along
with the associated original post content. Multiple edges can exist
between users if there are repeated interactions, such as a follower
commenting on different posts by the same blogger. For a prod-
uct that requires promotion, our objective is to identify a list of
influencers from𝑉2, specifically those with the greatest potential to
influence their influencees. In our framework,influence is defined as
the ability of an influencer to increase the likelihood of a follower
purchasing an advertised product by eliciting a stronger intent to
purchase through their actions or content.
5 Experimental Studies
5.1 Baselines and Test Settings
5.1.1 Baselines. We first evaluate our dataset with several classic
influencer selection models. For simulation baselines which esti-
mate the influence of specific nodes by modeling the spread of
information, we include CELF [15], CELF++ [7] and GREEDY [9].
For proxy baselines which use simplified models for approximating
influence to reduce computational complexity, we include EIGEN-
CENTRALITY [34], DEGREE [24], SIGMA [29], and PI [33].
For sketch baselines we experiment RIS [1] for efficient influence
estimation in networks.
We also employed the context-based method KB-TIM [22] to
evaluate our dataset, which incorporates the topic of users into the
calculation of influence propagation. Given the significant advan-
tages of LLMs in text processing and social network simulation, we
further used GPT-4 and Kimi 1 to model influence propagation and
compared it with the following three types of baselines:• GPT-4
serves as the LLM baseline. For each influencer candidate, we simu-
late their posting of advertisements and model the behavior of users
within their social network. The behaviors include ignoring, com-
menting, and reposting. Each generated comment is evaluated with
a purchase likelihood score (on a scale of 0-10) using GPT-4. Finally,
we aggregate the purchase scores of all simulated comments for
each advertisement to determine the overall purchase inclination,
which serves as the measure of the influencer’s influence.• GPT-4
w/ profile integrates the interests of influencers and users into the
prompt for simulating comments, thereby enhancing the realism
and relevance of the generated content.• GPT-4 w/ profile&CoT
incorporates an additional step-by-step reasoning process into the
comment simulation. It mimics how influencees behave in the real
world, with the goal of further improving the effectiveness of the
simulated comment generation.
5.1.2 Test Settings. In the task of advertising campaigns, we have
the IDs of real promoters. At the same time, we employed vari-
ous baselines for comparison. With the budget set to 10, we com-
pared the 10 most influential users identified by the baselines to
the ground truth. During the graph construction process, we used
interaction heat as the activation weight, calculated by dividing
1https://platform.moonshot.cn

SAGraph: A Large-Scale Social Graph Dataset with Comprehensive Context for Influencer Selection in Marketing SIGIR ’25, July 13–18, 2025, Padua, Italy
Table 5: Performance of sketch-based and context-based methods on six datasets.
Models
Electric Toothbrush Spark Thinking
P@5 P@10 R@5 R@10 G@5 G@10 P@5 P@10 R@5 R@10 G@5 G@10
RIS 0.40 0.30 0.40 0.60 0.36 0.47 0.00 0.10 0.00 0.25 0.00 0.12
KB-TIM 0.20 0.30 0.20 0.60 0.21 0.56 0.40 0.30 0.50 0.75 0.35 0.60
Ruby Face Cream Intelligent Floor Scrubber
RIS 0.60 0.40 0.43 0.57 0.53 0.52 0.20 0.30 0.25 0.75 0.20 0.43
KB-TIM 0.60 0.40 0.43 0.57 0.53 0.61 0.40 0.30 0.50 0.75 0.41 0.67
ABC Reading SUPOR Boosted Showerhead
RIS 0.20 0.20 0.25 0.50 0.15 0.26 0.20 0.10 0.25 0.25 0.39 0.39
KB-TIM 0.20 0.30 0.25 0.75 0.20 0.45 0.20 0.20 0.25 0.50 0.17 0.42
the historical interaction frequency by the highest interaction fre-
quency in the network. For information diffusion, all classic meth-
ods employed the Independent Cascade Model [9] for simulation,
with the number of diffusion rounds set to 100 for each model. We
adopt standard Top-𝑘 ranking metrics to assess the quality of our
recommendations. These metrics include Precision (𝑃@𝑘), which
measures the proportion of relevant items within the top-𝑘 recom-
mendations, Recall (𝑅@𝑘), which evaluates how many of the total
relevant items are captured in the top-k recommendations, and Nor-
malized Discounted Cumulative Gain (𝐺@𝑘), which assesses the
ranking quality by valuing correct recommendations that appear
higher in the list more favorably.
5.2 Baseline Results and Analysis
We show the overall performance of all baselines in Table 4, 5, and 6.
5.2.1 Simulation-based. . The results of simulation-based methods
in Table 4 show relatively consistent performance across different
products. While the recall and accuracy metrics are generally low,
the NDCG metric is higher in some domains, suggesting that within
the selected influencers, the ground truth rankings are relatively
strong. However, these methods do not perform equally well for
all products. GREEDY demonstrates better stability compared to
CELF++, while CELF performs the worst overall. Interestingly, CELF
performs the best for the “Electric Toothbrush”. This discrepancy
may be due to differences in user behavior and data distribution
across products. For example, the user interaction patterns for
certain products, such as the “Electric Toothbrush”, may be more
aligned with the CELF algorithm, while other products might be
better suited to GREEDY or CELF++.
5.2.2 Proxy-based. . Proxy-based methods exhibit similar perfor-
mance characteristics to simulation-based methods, displaying no-
table instability. This instability can be quite pronounced. For in-
stance, DEGREE performs well on several products but shows ex-
tremely low NDCG metrics for “ABC Reading” and “SUPOR Boosted
Showerhead”. Among the methods compared, SIGMA and PI demon-
strate the best stability, while EIGEN-CENTRALITY exhibits the
worst stability. In terms of average performance, DEGREE stands
out as the best-performing method.
5.2.3 Sketch-based. . Compared to simulation-based and proxy-
based methods, sketch-based methods such as RIS in Table 5 demon-
strate the most stable performance, with real promoters consistently
appearing in the Top 5 results. However, its average performance
is relatively weaker. This phenomenon may be linked to the im-
plementation mechanism of RIS. RIS relies on random sampling to
estimate node influence. While this method theoretically can cover
key nodes in the network, in practice, the sampling process may
introduce biases. Specifically, when using interaction frequency
between users as sampling weights, the model may overly focus on
users with high interaction rates, while neglecting the preference
characteristics between users. This bias could prevent the model
from fully capturing the diverse patterns of influence propagation
within the network, thereby affecting its overall performance.
5.2.4 Context-based. . In Table 5, the context-based method KB-
TIM builds upon RIS by incorporating user interest information. The
results show that KB-TIM significantly improves average perfor-
mance across various recommendation metrics for the six products
compared to RIS, while maintaining the stability of RIS. This phe-
nomenon further emphasizes the importance of textual information
in calculating influence.
5.2.5 LLM-based. GPT-4 outperforms all classic influencer selec-
tion baselines in terms of average performance at G@10, showing a
significant improvement over the consistently stable performance
of KB-TIM. However, GPT-4 does not excel in terms of optimal per-
formance across individual datasets. This is attributed to the LLMs’
tendency to produce indistinguishable outputs in the absence of
specific expressive personas. Secondly, GPT-4 significantly outper-
forms all the classic influencer selection baselines when augmented
with the profile and CoT modules. By leveraging our user profile
generation module, the LLM generates highly matched statements
for the user population. With the CoT execution, the precision
of the outputs increases, leading to a continuous enhancement in
overall performance. This improvement is not only reflected in the
significant boost in average performance but also in achieving the
best performance on all the datasets except Ruby Face Cream. The
underperformance of the classic baselines may be attributed to their
simulation logic, which emphasizes the number of nodes an influ-
encer can reach and the extent of their subsequent network impact,
without taking into account the semantic alignment between the

SIGIR ’25, July 13–18, 2025, Padua, Italy Zhang et al.
Table 6: Performance of LLM-based methods on six datasets.
Models
Electric Toothbrush Spark Thinking
P@5 P@10 R@5 R@10 G@5 G@10 P@5 P@10 R@5 R@10 G@5 G@10
GPT-4 0.40 0.40 0.40 0.80 0.36 0.60 0.40 0.20 0.50 0.50 0.35 0.35
GPT-4 w/ Profile 0.40 0.40 0.40 0.80 0.49 0.71 0.40 0.30 0.50 0.75 0.41 0.54
GPT-4 w/ Profile&CoT 0.40 0.40 0.40 0.80 0.55 0.77 0.40 0.30 0.50 0.75 0.56 0.68
Ruby Face Cream Intelligent Floor Scrubber
GPT-4 0.60 0.50 0.43 0.71 0.53 0.61 0.20 0.20 0.25 0.50 0.39 0.51
GPT-4 w/ Profile 0.40 0.40 0.29 0.57 0.38 0.49 0.40 0.30 0.50 0.75 0.54 0.68
GPT-4 w/ Profile&CoT 0.60 0.50 0.43 0.71 0.53 0.60 0.40 0.30 0.50 0.75 0.59 0.72
ABC Reading SUPOR Boosted Showerhead
GPT-4 0.40 0.20 0.50 0.50 0.32 0.32 0.40 0.20 0.50 0.50 0.40 0.40
GPT-4 w/ Profile 0.40 0.20 0.50 0.50 0.36 0.36 0.40 0.20 0.50 0.50 0.49 0.40
GPT-4 w/ Profile&CoT 0.40 0.30 0.50 0.75 0.64 0.75 0.40 0.20 0.50 0.50 0.40 0.40
influencer’s content and the products. Consequently, many influ-
encers in the network may share the same interest domain but are
still unsuitable for the product like Influencer 2 in the case study of
Figure 4. The performance of GPT-4 w/ profile&CoT varies across
products due to differences in their social networks. Datasets like
Spark Thinking feature large, information-rich networks with 490k
interactions and a follower variance of over 130, enabling effective
influencer identification. In contrast, the smaller interaction fre-
quency and a low variance of 98 in the SUPOR Boosted Showerhead
dataset lead to poorer performance, as the LLM struggles to extract
meaningful insights and distinguish influencers.
5.3 Analysis of LLM-based Methods
In this section, we mainly discuss the performance of LLMs due to
their state-of-the-art performance in sophisticated text processing.
5.3.1 Case study. . In Figure 4, we compare the selected influencer’s
advertisement with the profiles and historical interactions of sam-
pled influencees, along with their simulated behaviors and purchase
likelihood. For the chosen Influencer 1, the advertisement focuses
on young child education, aligning well with its profile. Examining
its Follower 1, we observe past interactions with the influencer on
this product, and a history of strong support for the product. Con-
sequently, this user will probably maintain their support, reflected
in a predicted likelihood of 7. In contrast, the selected Influencer 2
has a mismatch as his followers are interested in pregnancy, not
align with the ad that focuses on parenting. Therefore, although
the influencees have shown strong support for previous posts, GPT-
4 predicts they will not support this product. In Figure 7(b), we
present the normalized average distributions of comments and
purchase likelihood for the top 10 influencers versus others. Top
influencers attract more comments and higher purchase intentions.
Two illustrative examples highlight this contrast: Comments from
influencers outside the top 10 tend to be off-topic and less indicative
of purchase intent (e.g., ‘Is there a business cooperation opportu-
nity?’ and ‘Can this course be used for fitness?’ regarding the Spark
Thinking education product). Conversely, sample comments from
the top influencers, such as ‘Spark Thinking, my top choice!’ and
‘A great product, useful, I want to buy’, demonstrate a genuine
Figure 4: The comparison of influencers under LLM’s simu-
lation: The “comment” action is associated with a purchase
likelihood, while the “ignore” action outputs “None”.

SAGraph: A Large-Scale Social Graph Dataset with Comprehensive Context for Influencer Selection in Marketing SIGIR ’25, July 13–18, 2025, Padua, Italy
interest in the product. These cases demonstrate the role of text in
simulating and predicting varying responses from influencees by
considering multiple factors.
5.3.2 Ablation of Human Preferences and Behavioral Patterns. We
conduct two extra modules to enhance LLM-based method. Firstly,
compared with directly feeding influencer and influencee informa-
tion into behavior prediction, we integrate the profile generation
module in GPT-4 w/ Profile to provide the human preference of in-
fluencees, offering a personal profile of whether the influencees are
interested in the posts the influencer makes and take corresponding
actions. Secondly, in GPT-4 with profile&CoT, we incorporate an
additional procedural introduction for behavior prediction, com-
bining behavioral patterns with step-by-step generation prompts.
Results in Table 4 show each component’s critical role in enhancing
overall effectiveness.
Figure 5: The interest distribution for the product ‘Spark
Thinking’ at the start and the final stage. The proportions
of ‘parenting’ and ‘life sharing’ increase, consistent with the
product’s educational nature.
5.3.3 Interest develoment visualization. . In Figure 5, we present the
evolution of candidate influencer interests from their original state
to the final distribution of GPT-4 w/ profile&CoT for the product
‘Spark Thinking’, an educational product for children. Initially, the
seed influencers in our dataset span diverse areas like Gourmet and
Travel, which are not directly related to our product. However, after
the simulation, the percentage of influencers focused on parenting
increased from 15% to 40%, life sharing from 20% to 30%, and educa-
tion from 0% to 10%. This indicates that LLM’s simulation effectively
matches influencers from domains similar to those advertised for
the product. Additionally, there are interests in other areas such as
health and photography, suggesting that the matching process is
not a simple keyword match within a single domain.
5.3.4 Simulation scale. . We conduct a parameter study to investi-
gate the impact of varying simulation scales, specifically focusing
on the number of sampled simulated influencees for each seed in-
fluencer. Illustrated in Figure 6, we found that the performance
trajectory initially demonstrates fluctuating growth, which then
stabilizes upon exceeding a count of 20 influencees. These findings
support our choice to use a sample size between 30 and 50, find-
ing a good balance between capturing enough detail and keeping
our simulations practical to run. This careful choice helps make
sure our simulations are reliable and fit with our aim to accurately
understand how influencers affect the digital world.
Figure 6: Performance on different simulation scales.
Figure 7: (a) Comparison of GPT-4 and Kimi results with
profile&CoT module. (b) The percentage of comments from
influencees of the top 10 influencers versus those after the
top 10, indicating higher engagement among the top 10’s
influencees.
5.3.5 Performance on different LLMs. . To showcase the broad ap-
plicability of our framework, which is not limited to specific LLM
backbones, we experiment with alternative open APIs such as Kimi,
developed by Moonshot AI. The results are presented in Figure 7(a).
It is evident that both models perform well, with Kimi exhibit-
ing a slight edge in performance. The comparison result further
demonstrates the effectiveness of various components when work-
ing with Kimi. This advantage could potentially be attributed to
Kimi’s tailored design for the Chinese language.
6 Conclusion
We introduce SAGraph, the first comprehensive, text-rich large-
scale social advertisement graph dataset, designed to simulate in-
fluencer selection and optimize the effectiveness of advertising
campaigns based on social networks. It includes static social rela-
tionships and dynamic interactions towards specific posts, captur-
ing key factors of influencer selection from digital associations to
textual connotations, enabling large language models to be more
naturally applied in advertising tracks, and creating more possibili-
ties. Our experiment has demonstrated the effectiveness of LLM-
based methods over traditional approaches in influencer selection.
We hope researchers will engage in the study of SAGraph, clarifying
how to scientifically simulate the spread of influence for specific
products on social networks, and opening up an exciting future for
advertising campaigns in the era of prevailing self-media.

SIGIR ’25, July 13–18, 2025, Padua, Italy Zhang et al.
References
[1] Christian Borgs, Michael Brautbar, Jennifer Chayes, and Brendan Lucier. 2014.
Maximizing social influence in nearly optimal time. In Proceedings of the twenty-
fifth annual ACM-SIAM symposium on Discrete algorithms . SIAM, 946–957.
[2] Qi Cao, Huawei Shen, Jinhua Gao, Bingzheng Wei, and Xueqi Cheng. 2020.
Popularity prediction on social platforms with coupled graph neural networks.
In Proceedings of the 13th international conference on web search and data mining .
70–78.
[3] Covington & Burling LLP. 2019. Measures for Data Security Management .
Technical Report Draft for Comments. Covington & Burling LLP, Washing-
ton, D.C. https://www.insideprivacy.com/wp-content/uploads/sites/51/2019/05/
Measures-for-Data-Security-Management_Bilingual-1.pdf
[4] Subhabrata Dutta, Sarah Masud, Soumen Chakrabarti, and Tanmoy Chakraborty.
2020. Deep exogenous and endogenous influence combination for social chat-
ter intensity prediction. In Proceedings of the 26th ACM SIGKDD International
Conference on Knowledge Discovery & Data Mining . 1999–2008.
[5] Sainyam Galhotra, Akhil Arora, and Shourya Roy. 2016. Holistic influence
maximization: Combining scalability and efficiency with opinion-aware models.
In Proceedings of the 2016 international conference on management of data . 743–
758.
[6] Shen Gao, Xiuying Chen, Piji Li, Zhaochun Ren, Lidong Bing, Dongyan Zhao,
and Rui Yan. 2019. Abstractive text summarization by incorporating reader
comments. In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 33.
6399–6406.
[7] Amit Goyal, Wei Lu, and Laks VS Lakshmanan. 2011. Celf++ optimizing the
greedy algorithm for influence maximization in social networks. In Proceedings
of the 20th international conference companion on World wide web . 47–48.
[8] John Guare. 2016. Six degrees of separation. In The Contemporary Monologue:
Men. Routledge, 89–93.
[9] David Kempe, Jon Kleinberg, and Éva Tardos. 2003. Maximizing the spread of
influence through a social network. In Proceedings of the ninth ACM SIGKDD
international conference on Knowledge discovery and data mining . 137–146.
[10] H Kwak. 2010. What is Twitter, a social network or a news media? Department
of Computer Science, KAIST (2010).
[11] Eva Lahuerta-Otero and Rebeca Cordero-Gutiérrez. 2016. Looking for the perfect
tweet. The use of data mining techniques to find influencers on twitter.Computers
in human behavior 64 (2016), 575–583.
[12] Vasileios Lampos, Nikolaos Aletras, Daniel Preoţiuc-Pietro, and Trevor Cohn.
2014. Predicting and characterising user impact on Twitter. In Proceedings of
the 14th Conference of the European Chapter of the Association for Computational
Linguistics. 405–413.
[13] Aslı Diyadin Lenger. 2022. How to choose the right influencer for a marketing
strategy. Applied Marketing Analytics 8, 1 (2022), 89–104.
[14] Jure Leskovec, Jon Kleinberg, and Christos Faloutsos. 2007. Graph evolution:
Densification and shrinking diameters. ACM transactions on Knowledge Discovery
from Data (TKDD) 1, 1 (2007), 2–es.
[15] Jure Leskovec, Andreas Krause, Carlos Guestrin, Christos Faloutsos, Jeanne Van-
Briesen, and Natalie Glance. 2007. Cost-effective outbreak detection in networks.
In Proceedings of the 13th ACM SIGKDD international conference on Knowledge
discovery and data mining . 420–429.
[16] Jure Leskovec and Julian Mcauley. 2012. Learning to discover social circles in
ego networks. Advances in neural information processing systems 25 (2012).
[17] Jure Leskovec and Rok Sosic. 2014. SNAP: A general purpose network analysis
and graph mining library in C++.
[18] Jure Leskovec and Rok Sosič. 2016. Snap: A general-purpose network analysis and
graph-mining library. ACM Transactions on Intelligent Systems and Technology
(TIST) 8, 1 (2016), 1–20.
[19] Jiawei Li, Qing Xu, Raphael Cuomo, Vidya Purushothaman, Tim Mackey, et al.
2020. Data mining and content analysis of the Chinese social media platform
Weibo during the early COVID-19 outbreak: retrospective observational infoveil-
lance study. JMIR Public Health and Surveillance 6, 2 (2020), e18700.
[20] Mingzhe Li, Xiuying Chen, Shen Gao, Zhangming Chan, Dongyan Zhao, and Rui
Yan. 2020. VMSMO: Learning to Generate Multimodal Summary for Video-based
News Articles. In Proceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP) . 9360–9369.
[21] Qian Li, Xiaojuan Li, Bin Wu, and Yunpeng Xiao. 2018. Retweeting prediction
based on social hotspots and dynamic tensor decomposition. IEICE TRANSAC-
TIONS on Information and Systems 101, 5 (2018), 1380–1392.
[22] Yuchen Li, Dongxiang Zhang, and Kian-Lee Tan. 2015. Real-time targeted influ-
ence maximization for online advertisements. (2015).
[23] Rakesh R Mallipeddi, Subodha Kumar, Chelliah Sriskandarajah, and Yunxia Zhu.
2022. A framework for analyzing influencer marketing in social networks: selec-
tion and scheduling of influencers. Management Science 68, 1 (2022), 75–104.
[24] Alex Arenas Manlio De Domenico, Vincenzo Nicosia and Vito Latora. 2013.
Centrality measures in multilayer networks. (2013).
[25] Jiezhong Qiu, Jian Tang, Hao Ma, Yuxiao Dong, Kuansan Wang, and Jie Tang.
2018. Deepinf: Social influence prediction with deep learning. In Proceedings of
the 24th ACM SIGKDD international conference on knowledge discovery & data
mining. 2110–2119.
[26] Lucía Rivadeneira, Jian-Bo Yang, and Manuel López-Ibáñez. 2021. Predicting
tweet impact using a novel evidential reasoning prediction method. Expert
Systems with Applications 169 (2021), 114400.
[27] Youze Tang, Yanchen Shi, and Xiaokui Xiao. 2015. Influence maximization in
near-linear time: A martingale approach. InProceedings of the 2015 ACM SIGMOD
international conference on management of data . 1539–1554.
[28] Youze Tang, Xiaokui Xiao, and Yanchen Shi. 2014. Influence maximization: Near-
optimal time complexity meets practical efficiency. In Proceedings of the 2014
ACM SIGMOD international conference on Management of data . 75–86.
[29] Ruidong Yan, Deying Li, Weili Wu, Ding-Zhu Du, and Yongcai Wang. 2019.
Minimizing influence of rumors by blockers on social networks: algorithms
and analysis. IEEE Transactions on Network Science and Engineering 7, 3 (2019),
1067–1078.
[30] Fan Yang, Yang Liu, Xiaohui Yu, and Min Yang. 2012. Automatic detection of
rumor on sina weibo. In Proceedings of the ACM SIGKDD workshop on mining
data semantics. 1–7.
[31] Jing Zhang, Biao Liu, Jie Tang, Ting Chen, and Juanzi Li. 2013. Social influence
locality for modeling retweeting behaviors. In Twenty-third international joint
conference on artificial intelligence . Citeseer.
[32] Jing Zhang, Jie Tang, Juanzi Li, Yang Liu, and Chunxiao Xing. 2015. Who influ-
enced you? predicting retweet via social influence locality. ACM Transactions on
Knowledge Discovery from Data (TKDD) 9, 3 (2015), 1–26.
[33] Zonghan Zhang, Subhodip Biswas, Fanglan Chen, Kaiqun Fu, Taoran Ji, Chang-
Tien Lu, Naren Ramakrishnan, and Zhiqian Chen. 2022. Blocking Influence at
Collective Level with Hard Constraints (Student Abstract). In Proceedings of the
AAAI Conference on Artificial Intelligence , Vol. 36. 13115–13116.
[34] Lin-Feng Zhong, Ming-Sheng Shang, Xiao-Long Chen, and Shi-Ming Cai. 2018.
Identifying the influential nodes via eigen-centrality from the differences and
similarities of structure. Physica A: Statistical Mechanics and its Applications 510
(2018), 77–82.
