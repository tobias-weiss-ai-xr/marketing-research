---
title: Social Network Datasets on Reddit Financial Discussion
url: https://arxiv.org/abs/2410.05002
category: social-media
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Zezhong Wang
- Siyang Hao
- Inez Maria Zwetsloot
- Simon Trimborn
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.05002
pages: 11
chars: 22589
fetched_at: '2026-11-08T13:01:57+00:00'
kb_version: 1
---

# Social Network Datasets on Reddit Financial Discussion

Social Network Datasets on Reddit Financial Discussion
Zezhong Wang1, Siyang Hao2, Inez Maria Zwetsloot3,*, and Simon Trimborn4,5,6,*
1Department of Systems Engineering, City University of Hong Kong, Hong Kong
2College of Business, City University of Hong Kong, Hong Kong
3Department of Business Analytics, Amsterdam School of Business, University of
Amsterdam, The Netherlands
1,4Amsterdam School of Economics, University of Amsterdam, The Netherlands
5Tinbergen Institute, The Netherlands
6Department of Management Sciences, City University of Hong Kong, Hong Kong
*corresponding author(s): i.m.zwetsloot@uva.nl, simon.trimborn@uva.nl
Abstract
Stock markets are impacted by a large variety of factors including news and discussions among investors
about investment opportunities. With the emergence of social media, new opportunities for having financial
discussions arose. The market frenzy surrounding GameStop (GME) on the Reddit subreddit Wallstreetbets,
caused financial discussion forums to receive widespread attention and it was established that Wallstreetbets
played a leading role in the stock market movements of GME. Here, we present a new data set for exploring
the effect of social media discussion forums on the stock market. The dataset consists of posts published on
various Reddit subreddits concerning the popular meme stocks GameStop (GME), American Multi-Cinema
Entertainment Holdings (AMC), and BlackBerry (BB). We document the data collection and processing
steps and show that the posts and comments about these meme stocks are related to their market movements.
1
arXiv:2410.05002v1  [cs.SI]  7 Oct 2024

Background & Summary
Reddit is a social platform where millions of users globally communicate in different communities every
day. A community, also called a subreddit, is organized according to users’ interests, such as movies, mu-
sic, programming, politics, and even finance. Users can post, vote, and comment in subreddits to exchange
information and express opinions [1]. WallStreetbets (WSB), shown as r/wallstreetbets on Reddit, is a com-
munity where participants discuss stocks and share their investing strategies. It was even suggested that WSB
contributes to financial literacy [2]. WSB (https://www.reddit.com/r/wallstreetbets/) was created on January
31, 2012, and it has 15 million subscribers at the time of writing. It became notable for its major role in the
GameStop short squeeze.
GameStop (NYSE: GME), an offline video game retailer, struggled with competition from digital distri-
bution services and the negative economic impact of the COVID-19 pandemic. As a result, the stock price
declined, and many hedge funds short-sold the stock because of the prediction of its further decrease. At
that time, WSB users began to buy and hold GME stocks in bulk. Excess demand combined with limited
availability drove the stock price and ultimately triggered a short squeeze. The stock price of GME rose
from $18.80 on 31 December 2020 to $483 on 28 January 2021. Short sellers like Melvin Capital suffered
considerable losses in this short squeeze.
Sentiment can be a driver of market excesses and therefore various studies focused on the discussions on
WSB and investigated the sentiment users reflect in posts and comments towards GME. It was indeed shown
that sentiment on Reddit affects GME’s stock price.[3, 4, 5, 6] Reddit, being a social network, allows also
for the analysis of users interactions and the potential impact on others or even stocks. The foundation for
network-based analysis is the existence of comment trees on Reddit. A comment tree consists of comments to
a post and comments to comments within a post, which are the conversations between users. Various studies
utilized users’ interaction data on WSB to construct networks for analysis.[7, 8, 9] These networks change
over time because of the dynamics of users behaviour and are shown to relate to GameStop’s stock price
fluctuations. Lucchini et al. (2022) [8] identified a group of committed users who occupied central positions
in the early conversation networks. These studies on sentiment and network interactions for GME and WSB
have shown the existence of a relationship between WSB and GME’s stock price.
The articles mentioned above are based on different underlying data sets. Lucchini et al. (2022) [8]
identified 36,128 events of commitment by 30,133 users on WSB from 27 Nov 2020 to 3 Feb 2021.Zheng et
al. (2021)[7] collected 6,330,271 posts and 8,666,673 comments published on the subreddit r/WSB from 08
Dec 2020 to 03 Feb 2021. Mancini et al. (2022)[9] rely on 22,099,235 comments and 865,597 posts on WSB
from 01 Sep 2019 to 01 Feb 2021. The Pushshift Reddit dataset, presented byBaumgartner et al. (2020)[10],
includes all the posts and comments published on Reddit between Jun 2005 and Apr 2019. In the meantime,
access to the database is restricted to Reddit Moderators. A dataset focused on GME data across 4 subreddits
was presented by J.J. Han (2022)[11]. To allow for analysis of additional companies and the impact social
networks such as Reddit have on them, we provide a dataset spanning more companies and subreddits to make
this possible. Hence, in this data descriptor, we present three datasets for analyzing social networks’ impact
on stock markets. Besides GME data, our datasets include users’ interactions focused on American Multi-
Cinema (AMC) and BlackBerry (BB) on Reddit, which are three popular meme stocks. The data contain
users, posts, interactions, and publishing time on Reddit, starting from 01.06.2020, 6 months before the first
meme stock frenzy (GME) happened. For GME, the dataset ends on 31.08.2021, 8 months after the market
frenzy took place, allowing for comprehensive post-event analysis. The market frenzies of AMC and BB took
place later, hence their datasets end on the 31.12.2021. We design a framework for collecting and processing
data from Reddit based on API and keywords, which can be generalized to other companies, topics of interest,
or search queries. The datasets allow for several kinds of analysis, for example analyzing social networks’
impact on the markets but also for network modeling, longitudinal network analysis, network monitoring,
influencer identification, and bot detection.
2

Methods
Data collection
The data was obtained via the Reddit Data API. In this section, we describe in detail how the data was
collected, processed and what actions were taken to validate the results and algorithms. The process consists
of three steps, see Figure 1. Below we describe each step in detail in its respective subsection.
Post Identification
The first step of the data collection process is ‘Post Identification’. This step results in a list of posts that
fall within the search criteria. To obtain this list, one first needs to select the subreddit of interest, the key-
words to search for, and the time period to include. Table 1 shows an overview of the settings selected for
our data collection efforts. For example, we collected GME-related data from the subreddit WallStreetBets
from 01 Jun 2020 to 31 August 2021. We include all posts with the keywords ‘GME’ and/or ‘GameStop’
in their title. Note that we lowercase every character in the collected titles and compare them to ensure
capitalization does not influence the results. We use the Python Pushshift.io API Wrapper (PSAW) [12]
https://psaw.readthedocs.io/en/latest/ to obtain the post titles and ids. This wrapper takes in a period, one
keyword, and the subreddit of interest and returns a list of post ids. We repeat this procedure for each key-
word and obtain multiple lists with post ids (one for each keyword). To ensure that the used wrappers work
correctly, we have used PSAW to obtain post id’s for the GME stock at two different time points, 3 months
apart. We got the same results list with one post extra identified in the later validation. Then we use Python
Reddit API Wrapper (PRAW) to extract the title associated with each post id. Finally, we need to clean and
filter the obtained lists. This entails deleting duplicate posts (this may happen when there are multiple key-
words in the title) and deleting those identified posts that have the keyword only in the main text (and not in
the title).
Comment Extraction
The second step of the data collection process is ‘Comment Extraction’. We use the Python Reddit API
Wrapper (PRAW) https://praw.readthedocs.io/en/stable/index.html for extracting the comment tree post-by-
post. Note that for the GME dataset, extracting the comment tree for eight posts gave us an HTTP413 response
exception. For these eight posts we have therefore not included the comment trees in the final dataset. The
result of this step is our datasets which requires cleaning and data wrangling.
Data Wrangling
The final step is to perform data wrangling on the obtained list of posts and comments. The following actions
are taken:
• Matching of comments to parent comment author: for each comment, we identify the author of the
parent comment and use this user id as the ‘to’ variable.
• For the posts, we set the ‘to’ variable equal to the author’s id and the comment id equal to the post id.
• We define a unified user dictionary: each user name is recorded.
• Filter on the time period to only include posts and comments in the period as mentioned in Table 1.
Especially the comments collected can exceed these dates if the comment was posted (long) after the
original post.
3

• Set the timezone to UTC.
This results in the final datasets.
Data Records
We provide a CSV file for the network data from Reddit for each stock. A user name dictionary for the three
networks and a post dictionary are also available. Table 2 summarizes all files with brief introductions. The
GME data are collected from the WSB subreddit as it was the most important subreddit for GME discussions
during the frenzy. Besides WSB, the AMC data are collected from four additional subreddits, which were
chosen due to the popularity of AMC in these forums. Likewise the BB data are collected from WSB and
three additional subreddits. Figure 2 shows the detailed subreddits of AMC and BB records. Comparative
information about the three user interaction files is summarized in Table 3.
Table 4 explains the variables in the interaction files. Each row indicates an interaction in the network,
f romand to indicate users on Reddit or vertices in the network.post.id, comment.id, and parent.id determine
the user behaviors and interactions, in other words, edges among vertices. These variables can describe the
comment tree for a post on Reddit and build a network according to the following rules:
1. When f rom= to and post.id = parent.id = comment.id, the user f rompublished a post on Reddit.
2. When f rom= to and post.id = parent.id ̸= comment.id, the user f romcomments to a post published
by itself.
3. When f rom = to and post.id ̸= parent.id ̸= comment.id, the user f rom published a sub-comment to
its comment in a post.
4. When f rom̸= to and post.id = parent.id ̸= comment.id, the user f romcomments to user to’s post.
5. When f rom ̸= to and post.id ̸= parent.id ̸= comment.id, user f rom published a sub-comment to user
to’s comment in a post.
The ‘user_dictionary.csv’ file links the user to the three topics. This dictionary includes usernames and
three bivariate variables representing users’ participation in different topics. For example, users will have a
label 1 for GME if they have participated in GME-related discussions; otherwise, they get 0. Figure 3a shows
users’ participation in different topics. Figure 3b shows number of posts in different topics.
Technical Validation
In our datasets, the user name ‘None/NA’ is abnormal, indicating a group of users who have deactivated or
deleted their accounts or were shadowbanned by Reddit. To eliminate the potential effect from these abnormal
accounts, we remove ‘None’-related records before executing the following validation analysis.
Validation with reported events
The literature review in Background & Summary shows that users behavior on WSB can affect the stock price
of GME, we use this conclusion to validate our data. We compare daily user activities about each topic with
the corresponding daily stock price. The daily price data are easily accessed online, so we do not include and
provide them in our data sets. We compute the logarithm of daily activities to make them scale comparable to
daily stock price and draw the time series and scatter plots in Figure 4. As shown in Figure 4a, user activities
4

in WSB increase with the stock price, and both variables peaked in week 25 Jan 2021 to 31 Jan 2021; the
GME short squeeze also occurred in this week. The scatter plot in Figure 4b shows a positive correlation
between stock price and Reddit users’ behaviors.
Figure 4c shows that the discussion about AMC on Reddit increased abruptly in Jan 2021, and the stock
price increased in the same period. At the beginning of June 2021, user activities reached another peak, and
the stock price soared from around 10 to as much as 40. Traders on the wrong side of that bet are exposed to
severe losses. To the best of our knowledge, no research has analyzed the relationship between this market
frenzy and Reddit users, which could be an interesting project. The scatter plot for AMC (Figure 4d) also
shows that more user activities on Reddit relate to higher stock prices. Figure 4e shows two peaks in Reddit
user activities and two corresponding peaks in stock price. Figure 4f shows a strong positive correlation,
which confirms the relationship between user activity and stock price. These two datasets can be used for
factor analysis or predicting the stock price of AMC and BB.
User behavior
Figure 4 shows the temporal user activities on Reddit. As different users may have different characteristics,
we count the number of activities for each user based on the three interaction files. Table 5 presents the
summary statistics. The range of user activities is from 1 to thousands, and the standard deviations also show
that users have quite different activity levels. Most users have few actions within the selected period about
these three stocks; the medians are close to or equal to the minimum.
Usage Notes
Our datasets are available at request for research purposes. As our datasets keep the detailed user interactions
on Reddit, they can be immediately applied to a wide range of different research topics, including:
• Relationship between user behaviors, stock prices, and big events. Research has shown that Reddit
user behavior can affect GME stock prices and cause a short squeeze. Our datasets allow us to expand
this conclusion to stocks such as AMC and BB. Also, user activities on Reddit may be impacted by
other factors, such as policies, the economy, and company news. These factors could be used to explain
changes in Reddit users behavior and then explain the changes in stock prices. Hence, involving extra
events in the relationship analysis between Reddit and the stock market might be interesting.
• Sentiment and corresponding structures. Post’ titles have been frequently used for sentiment analysis[13,
3, 4], hence we provide a post dictionary for the datasets. Identifying the relationship between senti-
ment in the title and the post structure can reflect which type of post title can attract more attention and
participation from users, which can help Reddit to improve user experience and engagement. Combin-
ing post structure with sentiment analysis may also shed light on how Reddit affects the stock market.
• Bot detection. Bot detection for social media is a hot topic since they have been extensively used
for disingenuous purposes, such as perpetuating scams, swaying political opinions, and manipulating
the stock market [14]. We identify bots by the activity frequencies in data validation. There is a
graph-based bot detection method in the political subreddit proposed by Hurtado et al. (2019) [15].
We attempted to apply the graph-based method to the GME dataset, but the network is too big and
complex to process the method in reasonable computing time. There are limited methods designed for
identifying bots on Reddit. Hence, developing a bot detection algorithm for large scale social networks
such as Reddit remains an open research question which can be tackled based on our dataset.
• Network analysis. The provided interaction files can be used for network analysis, such as building a
sparse network model, monitoring temporal changes, identifying influential nodes/users, and detecting
5

changepoint. It was shown that network changes can be used to explain the return movements and
realized volatility of GME[16].
References
[1] Reddit. https://www.reddit.com/. Accessed: 2023-02-08.
[2] Klein, T. A note on gamestop, short squeezes, and autodidactic herding: An evolution in financial
literacy? Finance Research Letters 46, 102229 (2022).
[3] Long, S., Lucey, B., Xie, Y . & Yarovaya, L. “i just like the stock”: The role of reddit sentiment in the
gamestop share rally. Financial Review (2022).
[4] Haq, E.-U. et al. Short, colorful, and irreverent! a comparative analysis of new users on wallstreetbets
during the gamestop short-squeeze. In Companion Proceedings of the Web Conference 2022 , 52–61
(2022).
[5] Wang, C. & Luo, B. Predicting gme stock price movement using sentiment from reddit r/wallstreetbets.
In Proceedings of the Third Workshop on Financial Technology and Natural Language Processing ,
22–30 (2021).
[6] Machavarapu, A. Reddit sentiments effects on stock market prices. In Smart Intelligent Computing
and Applications, Volume 1: Proceedings of Fifth International Conference on Smart Computing and
Informatics (SCI 2021), 75–84 (Springer, 2022).
[7] Zheng, X. et al. Game starts at gamestop: Characterizing the collective behaviors and social dynamics
in the short squeeze episode. IEEE Transactions on Computational Social Systems 9, 45–58 (2021).
[8] Lucchini, L. et al. From reddit to wall street: the role of committed minorities in financial collective
action. Royal Society Open Science 9, 211488 (2022).
[9] Mancini, A., Desiderio, A., Di Clemente, R. & Cimini, G. Self-induced consensus of reddit users to
characterise the gamestop short squeeze. Scientific reports 12, 13780 (2022).
[10] Baumgartner, J., Zannettou, S., Keegan, B., Squire, M. & Blackburn, J. The pushshift reddit dataset. In
Proceedings of the international AAAI conference on web and social media, vol. 14, 830–839 (2020).
[11] Han, J. J. Reddit dataset on meme stock: Gamestop. Journal of Open Humanities Data 8 (2022).
[12] Psaw: Python pushshift.io api wrapper (for comment/submission search). https://psaw.readthedocs.io/
en/latest/. Accessed: 2023-05-30.
[13] Anand, A. & Pathak, J. The role of reddit in the gamestop short squeeze. Economics Letters 211,
110249 (2022).
[14] Kudugunta, S. & Ferrara, E. Deep neural networks for bot detection. Information Sciences 467, 312–
322 (2018).
[15] Hurtado, S., Ray, P. & Marculescu, R. Bot detection in reddit political discussion. In Proceedings of
the fourth international workshop on social sensing, 30–35 (2019).
[16] Trimborn, S. & Zwetsloot, I. M. Reddit users unleashed - understanding user behaviour and their impact
on meme stocks (2023). Working paper.
Figures & Tables
6

Table 1: Overview of Post Identification criteria
Stock Subreddit Keywords Time period
GameStop (GME) wallstreetbets GME, GameStop 01 Jun 2020 - 31 Aug 2021
AMC Entertain-
ment (AMC)
wallstreetbets, WallStreetbesELITE,
amcstock, AMCSTOCKS, Superstonk,
wallstreetbetsnews
AMC 01 Jun 2020-31 Dec 2021
BlackBerry (BB) wallStreetbets, BB_Stock, WallStreet- betsELITE, wallstreetbetsnew BB, BlackBerry, Black Berry 01 Jun 2020 - 31 Dec 2021
Table 2: Summary of files
File name Description
gme_interactions.csv User interactions about GME from 01 June 2020 to 31 Aug 2021 UTC
amc_interactions.csv User interactions about AMC from 01 June 2020 to 31 Dec 2021 UTC
bb_interactions.csv User interactions about BB from 01 June 2020 to 31 Dec 2021 UTC
user_dictionary.csv Include user names, user IDs, and stock
post_dictionary Include post title, post ID, posting time, posting time in utc, user_no, and stock
Figure 1: Webscraping process step-by-step
7

(a) Distribution of records from different subreddits for
AMC
 (b) Distribution of records from different subreddits for BB
Figure 2: Distribution of records from different subreddits for AMC and BB
Table 3: Summary of network data for GME, AMC, and BB.
Information GME AMC BB
Variables
from, to, time, utc, post.id,
comment.id, parent.id, sub-
reddit
from, to, time, utc, post.id,
comment.id, parent.id, sub-
reddit
from, to, time, utc, post.id,
comment.id, parent.id, sub-
reddit
Start Date 2020-06-01 2020-06-01 2020-06-01
End Date 2021-08-31 2021-12-31 2021-12-31
Number of Records 4,766,814 2,671,047 506,460
Number of Posts 175,237 215,151 37,888
Number of Comments 4,591,577 2,455,795 468,572
Number of Users 543,439 334,166 117,165
8

Table 4: Explanation of variables in interaction data files.
Variable Description
from A unique username for a Reddit user who publishes a comment or a post.
to A unique username for a Reddit user who receives a comment or publishes a post.
time The publishing time of comments and posts from user from.
utc UNIX time stamp.
post.id A string of characters with numbers and letters, unique for each post.
comment.id A string of characters with numbers and letters, unique for a comment.
parent.id A string of characters with numbers and letters, unique for a comment or a post that the comment is replying to.
subreddit The subreddit for corresponding activities.
(a) Users’ activities across different topics.
 (b) Posts across different topics.
Figure 3: Users and posts by topic
9

(a) Daily user activities regarding GME and its stock price
 (b) Scatter plot of GME daily user activities and stock price
(c) Daily user activities regarding AMC and its stock price
 (d) Scatter plot of AMC daily user activities and stock price
(e) Daily user activities regarding BB and its stock price
 (f) Scatter plot of BB daily user activities and stock price
Figure 4: Change of user activities and stock price
10

Table 5: Degree (number of activities, both in and out degree) for users in GME, AMC, and BB.
Statistics GME AMC BB
Minimum 1 1 1
10th Percentile 1 1 1
25th Percentile 1 1 1
50th Percentile 2 2 2
75th Percentile 7 7 5
90th Percentile 22 21 12
Maximum 955,971 75,701 37,481
Mean 15.9 14.4 7.7
Standard Deviation 1322.2 224.5 140.0
11
