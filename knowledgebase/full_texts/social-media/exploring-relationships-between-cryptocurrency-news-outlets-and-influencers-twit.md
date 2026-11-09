---
title: Exploring Relationships Between Cryptocurrency News Outlets and Influencers' Twitter Activity and
  Market Prices
url: https://arxiv.org/abs/2411.05577
category: social-media
subcategory: empirical
date: 2024-11
venue: ''
authors:
- Meysam Alizadeh
- Yasaman Asgari
- Zeynab Samei
- Sara Yari
- Shirin Dehghani
source: arxiv
pdf_url: https://arxiv.org/pdf/2411.05577
pages: 16
chars: 44759
fetched_at: '2026-11-08T13:00:44+00:00'
kb_version: 1
---

# Exploring Relationships Between Cryptocurrency News Outlets and Influencers' Twitter Activity and Market Prices

Exploring Relationships Between Cryptocurrency
News Outlets and Influencers’ Twitter Activity
and Market Prices
Meysam Alizadeh1, Yasaman Asgari2, Zeynab Samei3, Sara Yari1,
Shirin Dehghani4, Mael Kubli1, Darya Zare5, Juan Diego Bermeo1,
Veronika Batzdorfer6, and Fabrizio Gilardi1
1 Digital Democracy Lab, University of Zurich, Zurich, Switzerland
{syarim, alizadeh, kubli, jbermeo, gilardi} @ipz.uzh.ch
2 Digital Society Initiative and Department of Mathematical Modeling and Machine
learning, University of Zurich, Zurich, Switzerlandyasaman.asgari@math.uzh.ch
3 Department of Computer Science, IPM, Tehran, Iranzsamei@ipm.edu
4 Department of Computer Engineering, Allameh Tabataba’i University, Tehran,
Iran sh.dehghani@atu.ac.ir
5 Department of Informatics, University of Zurich, Zurich, Switzerland
daryazm@uzh.ch
6 Institute for Sociology and Computational Social Science, Karlsruhe Institute of
Technology, Karlsruhe, Germanyvbatzdorfer@kit.de
Abstract. Academics increasingly acknowledge the predictive power of
social media for a wide variety of events and, more specifically, for finan-
cial markets. Anecdotal and empirical findings show that cryptocurren-
cies are among the financial assets that have been affected by news and
influencers’ activities on Twitter. However, the extent to which Twitter
crypto influencer’s posts about trading signals and their effect on market
prices is mostly unexplored. In this paper, we use LLMs to uncover buy
and not-buy signals from influencers and news outlets’ Twitter posts and
use a VAR analysis with Granger Causality tests and cross-correlation
analysis to understand how these trading signals are temporally cor-
related with the top nine major cryptocurrencies’ prices. Overall, the
results show a mixed pattern across cryptocurrencies and temporal pe-
riods. However, we found that for the top three cryptocurrencies with
the highest presence within news and influencer posts, their aggregated
LLM-detected trading signal over the preceding 24 hours granger-causes
fluctuations in their market prices, exhibiting a lag of at least 6 hours.
In addition, the results reveal fundamental differences in how influencers
and news outlets cover cryptocurrencies.
Keywords: Social Prediction· NLP· LLM · Prompt Engineering· Time
Series Analysis
1 Introduction
Cryptocurrencies are a form of digital money that utilizes blockchain technology,
agroundbreaking,decentralized,andencryption-basedsystemthatallowsforthe
arXiv:2411.05577v1  [cs.SI]  8 Nov 2024

2 M. Alizadeh et al.
digital establishment of trust [26]. Since the introduction of Bitcoin in 2009, the
disruptive capabilities of cryptocurrencies have sparked significant growth and
interest [10]. This surge was mainly driven by media coverage highlighting the
extraordinary returns on cryptocurrency investments, which led to a modern-
day gold rush [16]. Moreover, the current international regulatory landscape for
cryptocurrencies remains sparse, as they are mostly not yet recognized as a fully
developed asset class [26]. This lack of regulation, combined with their immense
popularity and absence of institutional backing, contributes to the cryptocur-
rency market’s extreme volatility and unpredictability, earning it the nickname
“Wild West” [16].
The instability of the cryptocurrency market is significantly driven by news
and social media posts [2]. This dynamic is exacerbated by investors’ challenges
in verifying the accuracy of such information [16]. Given the relatively recent
emergence of the cryptocurrency market, traditional media often lag in report-
ing developments, making social media a key information source for investors.
Twitter (now re-branded as X), in particular, serves as a crucial platform for ob-
taining real-time updates and sentiment analysis on cryptocurrencies, allowing
users to express their opinions and feelings [12].
According to behavioral economics, emotions and sentiment can greatly in-
fluence individual actions and decision-making processes [11]. Previous research
explored the effect of public Twitter sentiment on cryptocurrency prices [16],
Elon Musk’s Twitter activity on the cryptocurrency market [2], Twitter effect
on stock market decisions during pandemics [27], and the predictive power of
Twitter for Bitcoin price [25] (see [5] for a recent review).
Given the abundance of Twitter data that captures the sentiments of cryp-
tocurrency participants, the extent to which Twitter posts can help traders make
informed decisions is mostly unexplored. Previous research on the association of
Twitter posts with the cryptocurrency market suffers from at least two signif-
icant drawbacks. First, they mostly fail to account for fake accounts, such as
bots and marketing campaigns. Indeed, previous research has shown that about
14% of the active accounts in the cryptocurrency space are bots [16]. Second,
the efficiency of the traditional sentiment analysis methods in capturing the true
opinion of users is questionable, and more explicitly defined machine learning
models that generate buy and sell signals [17] may produce better results.
In this paper, our goal is to determine whether LLM-detected trading signals
from news outlets and crypto influencers’ Twitter posts reflect cryptocurrency
market dynamics. Our study utilizes text classification, network science meth-
ods, and times series analysis to analyze the retweet and co-mention networks.
This structure consists of undirected links between cryptocurrencies that appear
together in a tweet. In summary, we aim to answer two key research questions:
1. How do the cryptocurrencies that are frequently co-mentioned together cor-
relate with each other in their market prices? Do the links in the co-mention
network reveal shared characteristics among cryptocurrencies, such as their
technology or use cases?

Cryptocurrency News and Influencers’ Twitter Activity, and Market Prices 3
2. Do the LLM-detected trading signals (buy or not-buy) of top cryptocurren-
cies obtained from news outlets and influencers’ Twitter posts demonstrate
a (lagged) correlation with their market prices?
2 Background
2.1 Effect of Sentiment on Financial Markets
Kaplanski and Levy [13] describe sentiment as any misconception that may lead
to a deviation from the true fundamental value of an asset. Baker and Wurgler [3]
note that the key factor distinguishing highly speculative assets is the difficulty
and subjectivity involved in valuing them accurately. Fama et al. [6] argued
that stock prices are unpredictable due to the erratic nature of news. According
to Peterson [24], financial markets are considerably influenced by news, which
in turn impacts sentiment. Traditionally, sentiment has been measured through
investorsurveyslikethosebytheAmericanAssociationofIndividualInvestorsor
Investor Intelligence. However, these methods are somewhat constrained by their
dependence on achieving representative sample sizes. Recent advancements have
seen a rise in the use of Natural Language Processing (NLP) to assess sentiment
from news sources [20].
2.2 Twitter Sentiment Analysis
TheeffectivenessofusingTwittersentimentanalysistoforecastfinancialmarkets
is prominently illustrated in the study by Bollen et al. [4], and further supported
by Li et al. [19]. In their research, Li et al. [19] employ a Naive Bayes sentiment
classifier and regression models to demonstrate that Tweets about stocks can
predict daily stock returns. The findings also indicate that increases in Twitter
activityfollowhighermarketvolatilityfromthepreviousday,positioningTwitter
sentiment as both a predictor and a result of market movements. Furthermore,
Mao et al. [22] found that, unlike traditional investor sentiment, Twitter senti-
ment significantly predicts stock returns over the following 1–2 days. In general,
the predictive power of Twitter sentiment for financial markets is generally ob-
served to be the strongest between 1–4 days [4, 22, 28].
2.3 Twitter and Cryptocurrency Market
Social media has become the main source of information for cryptocurrencies.
Several studies have analyzed user discussions on forums like Reddit and Bit-
cointalk.org (e.g. [15, 14]). Many researchers recognize the short-term (1–7 days)
and long-term (30–90 days) forecasting abilities of social media and news sen-
timent on Bitcoin’s price and trading volumes. The quantity of posts [21] and
Elon Musk’s activity on Twitter [2] have been linked to the trading volume of
Bitcoin [21]. Similarly, Zou et al. [29] proposed a multimodal model for Bitcoin
extreme price movement prediction using Twitter.

4 M. Alizadeh et al.
Twitter sentiment analysis has been used to predict changes in Bitcoin price.
Georgoula et al. [8] utilized a SVM to predict these fluctuations. Garcia and
Schweitzer [7] applied a lexicon-based method along with a Vector Autoregres-
sive (VAR) model and Granger-causality tests, discovering that rises in Twitter
sentiment polarity often precede shifts in Bitcoin prices. Mai et al. [21] performed
intradayanalysisandfoundTwitterpostseffectiveinforecastingBitcoin’shourly
returns. Overall, the most effective number of lags is observed from 1–5 lags for
interday analysis and 2–4 lags for intraday analysis [21, 14].
2.4 Limitations of Current Literature
The extant literature suffers from at least three major drawbacks: (1) much of
the current literature is dedicated to Bitcoin, and other major coins have been
neglected; (2) the vital role of the Twitter influencers has not been explored.
Nearly all previous work has not distinguished between the original content
produced by crypto experts and the content produced by lay users or even bots
andmarketing campaigns.(3)themeaning of“Twitter sentiment"is rathervague
as it may refer to emotion, stance, or buy or sell signals.
3 Methods and Data
3.1 Twitter Data
We collect four different Twitter datasets. First, we used Twitter Academic API
between 07/01/2022 and 14/01/2022 and between 01/03/2022 and 07/03/2022
and queried for ‘crypto’ and a list of the top 200 cryptocurrencies to collect
all tweets containing them (11.83M tweets posted by 2.1M unique users). Sec-
ond, we manually searched for all authentic news outlets that have finance or
cryptocurrency sections and have active Twitter accounts (74 accounts). Next,
we collected all tweets posted by these 74 accounts between 01/01/2023 and
16/09/2023 (122,837 tweets). These two datasets serve for our influencer iden-
tification (see Section 3.4) and model training purposes (see Section 3.3 and
3.5). Our third and fourth datasets are created by continuously crawling Twitter
data of the crypto-related influencers and news outlets between 10/06/2023 and
02/28/2024.
3.2 Cryptocurrency Data
We consider nine major cryptocurrencies according to their market capitaliza-
tion. This includes Bitcoin (BTC), Ethereum (ETH), Ripple (XRP), Solana
(SOL), Dogecoin (DOGE), Binance coin (BNB), Ada (ADA), Polkadot (DOT),
and Shiba Inu (SHIB). The financial information for these nine studied cryp-
tocurrencies was obtained from CoinMarketCap (https://coinmarketcap.com)
from October 2023 to March 2024. CoinMarketCap is commonly used as a refer-
ence for cryptocurrency prices as it aggregates prices from numerous exchanges,
providing a composite and more stable price estimate that avoids the biases of
individual exchange prices.

Cryptocurrency News and Influencers’ Twitter Activity, and Market Prices 5
3.3 Twitter Data Pre-processing
To prune out irrelevant tweets from our corpus, we trained and compared two
classifiers and five LLMs on 500 annotated tweets. Tweets were classified as “rel-
evant” if they were directly related to cryptocurrencies or related to economic
or policy topics related to cryptocurrency market (e.g., US interest rate and
cryptocurrency regulations). Out of the six classification models (CyptoBERT,
BERTweet, GPT-3.5 trained with two distinct prompts,Random Forest with
CryptoBERT Embedding, and Random Forest and CryptoBERT-kk08 Embed-
ding), we achieved the maximum accuracy of 0.94 on a 20% unseen out-of-sample
test data for GPT-3.5 with optimized prompt. Therefore, for all four datasets
we used GPT-3.5 with an optimized prompt to exclude irrelevant tweets.
model balancing method accuracy f1-score
CoinBER T unbalance 92% 91%
BER T weet gpt3.5 augmentation 92% 91%
CoinGPT - 96% 94%
GPT-4 - 93% 91%
Random forest+cryptobert embedding smote 88% 82%
Random forest+cryptobert-kk08 embedding smote 86% 81%
T able 1.Comparing the accuracy of various classifiers for pruning irrelevant tweets.
3.4 Influencer Identification
We use four different methodologies to identify crypto-related influencers on
Twitter.First,weusedournearly12milliontweetsdatasettoconstructaretweet
network. Following Kwak et al. [18], we calculate three centrality metrics, includ-
ing PageRank, Betweenness, andCloseness scores for all users within the retweet
network. From each centrality measure, we select the top 1000 accounts. After
combining these lists, we obtained 1,283 users.
Second, we examined the marketing campaigns of 10 coins that were launched
in 2023. Through the retweet network analysis, we identified the influential ac-
counts.Thisledtoidentifying87newinfluencersbasedontheir PageRank scores.
Third, we crafted a list of 50 non-major cryptocurrency coins and their related
keywords and collected all tweets posted between 01/01/2024 to 01/02/2024.
This process yielded 11,408 users who were potential influencers. Finally, we
used LunarCrush (https://lunarcrush.com/) website and scraped the list of top
1000 influencers for each of the leading 100 coins. After removing mutual influ-
encers, we obtained 36,311 unique users from LunarCrush.
After combining these four lists and excluding duplicates, we collected user
profile information (bio descriptions and follower counts) and the 10 most recent
tweets for each account. Users with irrelevant descriptions, fewer than 5000 fol-
lowers, no tweets in the last 3 months, and users with an average engagement of
fewer than 200 in their last 10 tweets were excluded. Overall, we obtained 2,687
cryptocurrency influencers on Twitter.

6 M. Alizadeh et al.
3.5 Trading Signal Detection
We use CryptoBERT[17] to detect buy, sell, and neutral signals from the text of
the influencers’ tweets. CryptoBERT is trained on a corpus of over 3.2 million
crypto-related social media posts. We compare its performance withRandom
Forests, Logistic Regression, SVM, and XGBoost. Our feature engineering in-
cludes content features such as top unigrams, top bigrams, top hashtags, top
mentions, number of mentions, number of emojis, and number of hashtags. Con-
sidering the previous findings on the ability of ChatGPT [9] and open-source
LLMs [1] in text annotation tasks, we included GPT-4, GPT-3.5, LlaMa-2 (7b),
LlaMa-2 (70b), FLAN-T5 (L), and FLAN-T5 (XL) in our comparison. We ran-
domly selected 600 tweets from influencers and 200 tweets from news outlets’
datasets, and labeled them for buy, sell, and neutral signals (Table 2). As can be
seen in Table 2, Since the frequency of ‘sell (bearish)’ signal in the influencer’s
data is low (5.5% of total labeled data), we combined the ‘sell’ and ‘neutral’
classes into one class and called it the ‘not-buy’ class.
T able 2.The distribution of signals across annotated datasets.
Dataset Class names % samples
Twitter Influencers Buy (Bullish) 56.8
Sell (Bearish) 5.50
Neutral 37.7
News Outlets Buy (Bullish) 30.5
Sell (Bearish) 25.5
Neutral 44.0
In Figure 1, we see the CryptoBert model outperforms all other models for
the influencers dataset. However, for the news outlets’ data, GPT-4 and GPT-3.5
are the two best-performing models and slightly outperform CryptoBERT. Since
CryptoBERT’s performance is strong across both datasets, and it is open-source
(and thus more ethical for academic purposes) and free to use, we selected it as
our final choice.
3.6 Constructing Co-mention Network
In a co-mention network, nodes represent individual cryptocurrency coins, and
edges symbolize the two coins that were mentioned together in a tweet. The net-
work is undirected and weighted, characterized by symmetric adjacency matrix
A with entries wij ∈ N corresponding to the frequency of co-mentions between
coins i and j.
3.7 Time series processing
Time series data consist of a sequence of values or observations recorded over
time.Mathematically,atimeseriescanbedefinedasasetoforderedobservations

Cryptocurrency News and Influencers’ Twitter Activity, and Market Prices 7
0% 20% 40% 60% 80% 100%
Accuracy
SVM
XGBoost
Random Forest
Logistic Regression
FLAN(large)
FLAN(xl)
LlaMa2-7b
LlaMa2-70b
GPT-3.5
GPT-4
cryptoBERT
A: Influencers
0% 20% 40% 60% 80% 100%
Accuracy
B: News Outlets
Fig. 1. Choosing the best AI model for the trading signal detection task.
X = {x1, x2, . . . , xn}, where eachxi corresponds to the value of the series at the
ith time point.
The Granger causality test assesses whether one time series can predict an-
other, a method commonly used to investigate economic time series interactions.
The null hypothesis states thatX does not cause Y in the Granger sense. The
procedure involves formulating a vector autoregression (VAR) model for the time
series under study. For two variablesX and Y, the model can be specified as:
Yt = α +
kX
i=1
βiYt−i +
kX
i=1
γiXt−i + ϵt (1)
Xt = δ +
kX
i=1
ϕiXt−i +
kX
i=1
ψiYt−i + ηt (2)
Here, α and δ represent constant terms,βi, γi, ϕi, and ψi are the coefficients,
and ϵt and ηt denote the error terms of the model. The parameterk signifies
the number of lagged observations in the model. An F-statistic is calculated
to evaluate the null hypothesis. Granger causality testing identifies patterns of
lagged correlation but does not confirm causality. This concept is akin to how
observing cloud cover, which often precedes rain, can help predict rain but does
not cause it.
Cross-correlation evaluates the degree to which two series are correlated at
different time lags k. If we denote another time series asY = {y1, y2, . . . , yn},
the cross-correlationγ at lagk can be computed using (3). The numerator of the
formula represents the covariance between thex series shifted byk units in time
and they series. The denominator normalizes this value, ensuring that the cross-
correlation coefficientγ lies between -1 and 1, inclusive. The sign and magnitude
of γ at different values of k can reveal the leading and lagging relationships
between the two-time series.
γ =
P
i(xi+k − ¯X)(yi − ¯Y )qP
i(xi+k − ¯X)2
qP
i(yi − ¯Y )2
(3)

8 M. Alizadeh et al.
4 Results
4.1 Description of Influencers and News Outlets Twitter Data
ThefinalTwitterdatasetusedinthisexperimentcontains470,658Englishtweets
from influencers and news outlet’s Twitter accounts, between 10/06/2023 and
02/28/2024. Tweets written by influencers dominate the dataset with 413,071
tweets (87.8%), while news outlets account for 57,587 tweets (12.2%). This un-
derscores the pivotal role of influencers in shaping discussions and influencing
trading decisions within the cryptocurrency market (Figure 2-A). Moreover, Bit-
coin appears in 340,193 tweets (34.8%), followed by Ethereum and Solana with
39,742 (9.9%) and 27,688 (6.9%) tweets, respectively (Figure 2-B). Figure 2-C
illustrates the coin mention share distribution, highlighting structural variations
between influencers and news outlets. An interesting observation here is that
the share of Bitcoin mentions in news outlets’ tweets (61.9%) is higher than
influencers’ tweets (48.2%).
Figure 2-D shows the dataset predominantly contains ‘not buy’ signal, repre-
senting 54.39% (256,016 tweets), while ‘buy’ signals account for 45.60% (214,629
tweets). Figure 2-E details the signal distribution across nine major coins. BTC,
XRP, and DOT predominantly feature ‘not buy’ signals, whereas ETH, SOL,
ADA, DOGE, SHIB, and BNB mainly show ‘buy’ signals. Notably, DOGE has
2.53 times more ‘buy’ than ‘not buy’ signals, the highest ratio amongst all ex-
amined coins.
B CA
D
 E
Fig. 2. Exploratory Analysis : (A) User Type Distribution (B) Frequency of Tweets
by Major Coin, with Bitcoin as the Most Mentioned (C) Comparison of 9-major coins’
mentions in News Outlets versus Influencer Tweets (D) Signal Distribution (E) ’Not
Buy’ signals predominant for BTC, XRP, and DOT, while ’Buy’ Signals are more
common for ETH, SOL, ADA, DOGE, SHIB, and BNB.

Cryptocurrency News and Influencers’ Twitter Activity, and Market Prices 9
4.2 Analyzing the cryptocurrencies co-mention network
Exploratory Analysis of the Co-Mention NetworkThis study focuses on
the co-mention network of the top 100 coins according to their market capitaliza-
tion. The dataset includes tweets mentioning between zero (generally discussing
the cryptocurrency financial market) to over 40 coins, with the most common
scenario involving single-coin mentions (44.4% of tweets). We also examine the
differences in how influencers and news outlets reference cryptocurrencies. Ac-
cording to Figure 3-A, influencers tend to mention more coins per tweet (0.9)
compared to news outlets (0.56). This suggests that influencers may discuss a
broader range of coins, likely to engage a larger audience or to demonstrate their
knowledge across various market segments.
Furthermore, Figure 3-B reveals distinct characteristics in tweets signaling
‘buy’ versus ‘not buy’ intentions. Tweets encouraging buying typically mention
at least one specific coin, suggesting a direct investment recommendation. In
contrast, ‘no buy’ tweets often do not specify any coins and focus more on
general market conditions or cautions. The average number of coins mentioned
in ‘buy’ tweets is higher (0.96) compared to ‘not buy’ tweets (0.77), showing a
more targeted approach to investment suggestions.
We reveal key patterns in the co-mention network using the k-core method
to filter the network, where nodes must have connections involving at least 1% of
the total degree sum. Figure 3-C shows this filtered k-core network of 24 nodes.
The edge thickness represents the edge weight, while the node size indicates the
node’s degree of centrality. The data highlights several key connections: BTC to
ETH with 14,062 connections (5.16 %), BTC to USDT (3.54 %), BTC to BCH
(2.37 %), ETH to SOL (2.14 %), BTC to XRP (1.81 %), BTC to SOL (1.79
%), BTC to ADA (1.25 %), and XRP to ETH (1.18 %). Bitcoin (BTC) and
Ethereum (ETH) are frequently featured, with a notable connection between
Ethereum Classic (ETC) and Non-Fungible Tokens (NFT).
Interplay between the co-mention network and cryptocurrency at-
tributes Next, We investigate whether the connections in the co-mention net-
work indicate common features among cryptocurrencies, such as their technology
or applications. Following Mungo et al [23], we utilize tags from Coinmarketcap
that describe various cryptocurrencies’ primary attributes. These tags detail
each cryptocurrency’s blockchain technology and information about its ecosys-
tem, such as whether the cryptocurrency is built on an independent or existing
blockchain and is involved in decentralized finance (DeFi) projects. Additionally,
the tags describe the specific functions and utilities of the cryptocurrencies, for
instance, their use in distributed storage, as fan tokens, or as digital stores of
value like digital gold.
Following the methodology suggested by Mungo et al. ([23]), we assign a
vector xi to each cryptocurrency, where each tagj is represented as xi,j = 1
if it applies to the cryptocurrency andxi,j = 0 otherwise. We then calculate
the cosine similarity in the characteristics space between each pair of cryptocur-
rencies to create a similarity matrix. Next, we compute a Pearson correlation

10 M. Alizadeh et al.
Fig. 3. Structure of the cryptocurrencies co-mention network: (A) Influencers mention
more coins in their tweets than news outlets do. (B) Tweets signaling a buy mention
more coins than tweets not signaling a buy. (C) The co-mention network of top 24
coins. There exists a notable connection between NFT and ETC.
between the weighted adjacency and similarity matrices. The correlation coeffi-
cient of 0.1735 with a p-value of< 0.001 suggests that the patterns observed in
the co-mention network are only slightly correlated with the coin characteristics,
and there are other mechanisms run by the influencers and news outlets on the
mentioning patterns within the social media.
Interplay between the co-mention network structure and cryptocur-
rency price returns We analyze pairs of coins in the co-mention network
that constitute at least 1% of the total connections. From the initial set of 24
cryptocurrencies considered, we exclude two: NFT and USDT. NFTs, or non-
fungible tokens, differ from cryptocurrencies as they do not have standard prices
listed on platforms like CoinMarketCap due to the unique nature of each NFT,
which contrasts with fungible assets like Bitcoin or Ethereum where each unit is
interchangeable. Additionally, USDT is excluded because it is a stablecoin.
We construct a22 × 22 correlation matrix, denoted asC, in which each cell
Cij, represents the cross-correlation at zero lag between coinsi and j. This cor-
relation is calculated differently depending on the time scale: for pairs where

Cryptocurrency News and Influencers’ Twitter Activity, and Market Prices 11
i > j, we use hourly log returns, while fori < j, we use log returns for mean
weekly prices. This dual-time approach allows us to capture both short-term and
long-term interdependencies between cryptocurrencies. In Figure 4, the lower
triangle displays the correlations computed from hourly data, and the upper
triangle shows the correlations from weekly data. Prior to conducting the cor-
relation analysis, an Augmented Dickey-Fuller test confirmed that all price log
return series are stationary, each with a p-value of< 0.001. All the correlation
values are statistically significant with p-value< 0.001.
The correlation values for short-term dynamics consistently exceed 0.3 across
all pairs except for SHIB. However, for the long-term test, several pairs show
zero or negative correlations. The highest correlation is 0.89 for the long term
between XLM and XRP and 0.78 for the short term. Following closely behind for
short-term dynamics are DOT-ADA (0.73) and BTC-ETH (0.72). Conversely,
thestrongestcorrelationsforlong-termdynamicsarenotedforSHIB-DOT(0.87)
and DOT-ATOM (0.84). The lowest short-term correlation values are predomi-
nantly between SHIB and all other coins, with the lowest long-term correlation
being between ARB and RNDR (-0.35).
We hypothesize that a higher weight between pairs in the co-mention network
leads to higher similarity in the logarithmic returns of their hourly and mean
weekly prices. To test this hypothesis, we perform a Pearson correlation analysis
between the adjacency matrix of the co-mention network and the correlation
matrix C for the log returns of hourly and weekly prices. The resulting correla-
tion coefficient for hourly prices is 0.154, with a p-value of 0.019, and for weekly
prices is 0.16, with a p-value of 0.015. This indicates that while there is a statisti-
cally significant relationship, the effect size is relatively small. This suggests that
factors other than social media co-mentions likely play a more significant role
in influencing financial market movements. Examples of these influential factors
can be shared with Investors because investors often move in herds; thus, if a
significant investor adjusts their portfolio across several assets, it could lead to si-
multaneous price movements in those assets. Similar Technological Foundations
or common applications could also be another factor.
4.3 Correlation of LLM-detected signals and cryptocurrency prices
In this section, we examine the existence of Granger causality and lagged cross-
correlation between the market prices of nine major cryptocurrencies and their
associated social signals. Our goal is to identify the presence of these relation-
ships and the specific lags where they become significant. This analysis also
investigates if the optimal lag differs among cryptocurrencies, indicating that
the interplay between market dynamics and social signals may be coin-specific.
The 24-hour Twitter social signal for each cryptocurrencyi at timet is quan-
tified as (4). An increase in SSi t is hypothesized to correlate with a rise in the
cryptocurrency’s price.
SSi(t) =

1 + N i Buy(t)
1 + N i Not buy (t)
!
(4)

12 M. Alizadeh et al.
SOL ARB AVAX SHIB INJ ADA MATIC XLM ETC DOGE HBAR QNT ATOM DOT XRP BTC LINK RNDR TRX BCH BNB ETH
Hourly
SOLARBAVAXSHIBINJADAMATICXLMETCDOGEHBARQNTATOMDOTXRPBTCLINKRNDRTRXBCHBNBETH
0.36 0.58 0.66 0.48 0.49 0.67 0.56 0.35 0.44 0.3 0.59 0.64 0.76 0.6 0.38 0.57 0.27 0.28 0.3 0.4 0.25
-0.022 0.26 0.24 0.17 0.34 0.28 0.46 -0.009 0.021 0.39 0.14 0.33 0.4 0.35 0.3 -0.35 0.068 0.36 0.45 0.36
0.59 0.49 0.74 0.41 0.12 0.15 0.45 0.37 0.23 0.69 0.67 0.17 0.24 0.2 0.42 -0.037 -0.07 0.034 0.14
0.46 0.78 0.67 0.71 0.5 0.84 0.58 0.62 0.74 0.87 0.69 0.68 0.56 0.3 0.26 0.52 0.39 0.63
0.57 0.2 0.29 0.11 0.21 0.41 0.32 0.5 0.52 0.4 0.24 0.29 0.17 -0.18 -0.084 0.24 0.14
0.56 0.6 0.31 0.67 0.66 0.52 0.79 0.84 0.62 0.47 0.39 0.45 0.12 0.22 0.34 0.46
0.68 0.48 0.67 0.52 0.73 0.75 0.79 0.67 0.46 0.59 0.39 0.58 0.5 0.63 0.57
0.42 0.69 0.54 0.75 0.61 0.72 0.89 0.56 0.52 0.32 0.43 0.6 0.54 0.58
0.35 0.06 0.32 0.38 0.48 0.55 0.43 0.49 -0.078 0.26 0.54 0.19 0.73
0.47 0.56 0.68 0.67 0.64 0.64 0.6 0.37 0.33 0.45 0.18 0.6
0.44 0.56 0.62 0.49 0.31 0.14 0.61 0.28 0.15 0.56 0.47
0.54 0.77 0.57 0.38 0.51 0.32 0.18 0.58 0.7 0.44
0.84 0.68 0.33 0.45 0.35 0.35 0.16 0.41 0.48
0.67 0.46 0.47 0.42 0.22 0.43 0.56 0.52
0.6 0.69 0.17 0.53 0.49 0.48 0.68
0.58 0.23 0.42 0.71 0.16 0.73
0.12 0.48 0.39 0.24 0.54
0.22 0.042 0.24 0.28
0.42 0.33 0.48
0.42 0.64
0.39
0.44
0.62 0.54
-0.021 -0.016 -0.02
0.48 0.44 0.52 -0.024
0.59 0.55 0.61 0.006 0.44
0.55 0.6 0.58 -0.041 0.44 0.65
0.49 0.57 0.57 -0.025 0.47 0.64 0.6
0.45 0.64 0.52 -0.009 0.41 0.57 0.62 0.63
0.51 0.46 0.49 0.006 0.4 0.62 0.58 0.59 0.54
0.52 0.52 0.58 -0.045 0.43 0.61 0.63 0.59 0.53 0.54
0.46 0.55 0.53 -0.039 0.46 0.54 0.56 0.59 0.57 0.5 0.54
0.5 0.57 0.6 -0.017 0.49 0.62 0.63 0.65 0.6 0.55 0.59 0.59
0.56 0.54 0.6 -0.024 0.43 0.73 0.65 0.62 0.58 0.6 0.63 0.55 0.65
0.47 0.43 0.46 -0.023 0.37 0.62 0.52 0.76 0.51 0.59 0.5 0.46 0.52 0.58
0.58 0.49 0.53 -0.014 0.41 0.63 0.56 0.57 0.54 0.57 0.52 0.5 0.53 0.58 0.56
0.53 0.52 0.53 -0.03 0.4 0.59 0.63 0.56 0.53 0.56 0.54 0.49 0.57 0.61 0.51 0.54
0.42 0.37 0.41 -0.031 0.34 0.43 0.5 0.4 0.39 0.43 0.48 0.39 0.41 0.48 0.37 0.43 0.43
0.35 0.4 0.39 -0.038 0.33 0.4 0.45 0.52 0.44 0.41 0.42 0.42 0.48 0.44 0.41 0.45 0.42 0.35
0.43 0.42 0.43 -0.037 0.34 0.51 0.54 0.55 0.57 0.51 0.48 0.46 0.49 0.53 0.49 0.55 0.5 0.4 0.41
0.41 0.46 0.49 -0.057 0.39 0.47 0.52 0.55 0.51 0.44 0.5 0.5 0.53 0.45 0.4 0.48 0.43 0.39 0.41 0.42
0.52 0.67 0.53 -0.033 0.4 0.63 0.66 0.59 0.69 0.58 0.56 0.54 0.58 0.6 0.54 0.72 0.6 0.46 0.46 0.52 0.55
Weekly
Fig. 4. Correlation matrix for log returns of prices for pairs of coins in the network
holding at least 1% degree share. Upper triangle: Long-term weekly cross-correlation
analysis (k = 0). Lower triangle: Short-term hourly cross-correlation analysis (k = 0).
We can also include information about the cryptocurrency market (Tweets re-
lated to crypto but without mentioning any coin) in our analysis because the
market status influences prices simultaneously.
SSi Crypto(t) =

1 + N i Buy (t) + N Crypto Buy (t)
1 + N i Not buy (t) + N Crypto Not buy (t)
!
(5)
The log return of the social signal for cryptocurrencyi from time t − 1 to t is
denoted by ri SS(t). Similarly, cryptocurrency prices exhibit non-stationary be-
havior, and the log-returns of the prices are denoted byri CP(t).
Table3illustratesaGrangercausalityanalysisbetweenTwittersocialsignals,
ri SScrypto (t), and price changes of nine major cryptocurrencies,ri CP(t), highlighting
how these signals may predict price movements. BTC and ETH demonstrate
significant predictive correlations at multiple hourly lags of less than 10 hours,
whereas DOGE exhibits signs of correlation after 10 hours, and SOL for the
entire 24 hours, suggesting a robust effect of influencers and news outlets on coins
prices. In contrast, ADA, XRP, and DOT show significant Granger causal links
predominantly within the first three hours, indicating a rapid market response
to new social data. Conversely, BNB exhibits week predictive lags, implying that
Twitter data does not hugely influence price changes. SHIB reveals predictive
power specifically at 21-22 hour lags, showcasing delayed market reactions to
social signals. DOGE and SOL also present varied predictive lags, reflecting their
community-driven market dynamics. This analysis underscores the diverse ways
different cryptocurrencies respond to social media, driven by unique investor
behaviors and market conditions.

Cryptocurrency News and Influencers’ Twitter Activity, and Market Prices 13
ADA BNB BTC DOGE DOT ETH SHIB SOL XRP
1H 0.040 0.111 0.001 0.017 0.043 0.002 0.812 0.001 0.021
2H 0.077 0.080 0.003 0.025 0.085 0.003 0.898 0.001 0.053
3H 0.047 0.090 0.001 0.006 0.063 0.003 0.978 0.001 0.047
4H 0.063 0.083 0.002 0.013 0.103 0.008 0.961 0.003 0.070
5H 0.100 0.118 0.001 0.013 0.185 0.010 0.972 0.004 0.101
6H 0.091 0.180 0.001 0.020 0.215 0.006 0.887 0.003 0.058
7H 0.094 0.230 0.002 0.031 0.297 0.012 0.236 0.006 0.072
8H 0.104 0.300 0.004 0.015 0.353 0.015 0.324 0.005 0.065
9H 0.144 0.383 0.006 0.021 0.435 0.024 0.320 0.008 0.091
10H 0.187 0.466 0.008 0.001 0.266 0.023 0.412 0.011 0.141
11H 0.209 0.560 0.012 0.003 0.334 0.025 0.490 0.014 0.105
12H 0.230 0.640 0.014 0.004 0.414 0.019 0.523 0.009 0.127
13H 0.282 0.647 0.023 0.006 0.429 0.026 0.438 0.011 0.158
14H 0.339 0.655 0.034 0.009 0.509 0.041 0.275 0.005 0.193
15H 0.296 0.687 0.046 0.008 0.545 0.051 0.330 0.007 0.214
16H 0.318 0.735 0.057 0.009 0.469 0.042 0.330 0.003 0.253
17H 0.375 0.793 0.078 0.008 0.493 0.062 0.241 0.004 0.292
18H 0.435 0.843 0.111 0.013 0.521 0.065 0.215 0.002 0.263
19H 0.366 0.794 0.099 0.009 0.580 0.078 0.277 0.002 0.261
20H 0.192 0.795 0.116 0.006 0.502 0.059 0.272 0.001 0.105
21H 0.217 0.808 0.137 0.006 0.543 0.079 0.046 0.001 0.126
22H 0.263 0.823 0.158 0.009 0.591 0.090 0.042 0.001 0.161
23H 0.291 0.861 0.166 0.013 0.633 0.110 0.051 0.002 0.150
24H 0.398 0.859 0.355 0.007 0.386 0.060 0.169 0.001 0.112
T able 3.GrangercausalityanalysisbetweenTwittersocialsignal ri SScrypto (t)andprices
changes of 9 major cryptocurrenciesri CP(t). Blue color showsp−value < 0.01, orange
shows p−value < 0.05 and green, p−value < 0.1.
T able 4. Highest correlation coefficient with associated lags for 9 major coins with
different formulas
Price Social signal ADA BNB BTC DOGE DOT ETH SHIB SOL XRP
CPi (t) SSi (t) 0.09(7D) −0.15(5D) −0.15(6D) −0.25(2H) −0.35(3D) 0.23(1H) −0.05(6D) 0.31(6D) 0.06(2H)
CPi (t) SSi crypto (t) 0.25(0H) 0.06(0H) −0.03(6D) 0.22(1H) 0.19(0H) 0.23(0H) 0.25(0H) 0.33(10H) 0.44(2H)
ri CP (t) ri SS (t) 0.03(6D) 0.03(18H) 0.08(0H) 0.04(0H) 0.05(0H) 0.07(1H) 0.03(20H) 0.04(1H) 0.04(8H)
ri CP (t) ri SS, crypto (t) 0.04(0H) 0.05(0H) 0.08(0H) 0.05(0H) 0.04(0H) 0.06(1H) 0.04(7H) 0.06(1H) 0.04(20H)
Table 4 illustrates the highest cross-correlation values between each cryp-
tocurrency’s price and its LLM-detected trading signal aggregated on influencers
and news outlets using hourly (24 hours) and daily lags (up to 7 days) to capture
short-term and long-term market behaviors. Each row represents a different com-
putation formula for the price and social trading signals, and each cell below the
cryptocurrency names columns shows the highest correlation value for a cryp-
tocurrency with the associated lag. In general, we can see that the coefficients
for price are much larger than the coefficients for the log return when market so-
cial signals are included. For most of the cryptocurrencies, the cross-correlation
values are highest when considering no lag, meaning that the 24-hour social sig-
nal instantly affects the price. Adding the information about the crypto-market
increases the correlation coefficient. Additionally, the correlation coefficient and
the associated lags differ from one coin to another, spanning from hour delays
to daily ones. This suggests both short-term and long-term impacts of social

14 M. Alizadeh et al.
signals from news outlets and influencers, warranting further investigation in
future studies.
5 Conclusion
In this paper, we investigated an ecosystem of 2,687 cryptocurrency influencers
and 74 financial news outlets on Twitter. We have collected all tweets posted
by influencers and news outlets between 10/06/2023 and 02/28/2024 and used
ChatGPT and CryptoBERT to exclude irrelevant content (94% accuracy) and
detect ‘buy’ and ‘not-buy’ signals (84% accuracy) from their tweets text respec-
tively. We have also gathered time series data of the top 9 major cryptocurrency
prices and explored whether (1) aggregated LLM-detected ‘buy’ and ‘not-buy’
signals correlate with price and (2) co-mentioned cryptocurrencies exhibit cor-
relation in their prices.
Our exploratory results showed that (1) influencers post about 9 times as
many tweets as news outlets about cryptocurrencies; (2) of the 470,658 tweets
postedbyinfluencersandnewsoutletsbetween10/06/2023and02/28/2024,54%
were classified as implying a ‘buy’ signal and 66% implying a ‘not-buy’ signal;
(3) 44.4% of all tweets posted by influencers and news outlets only contain a
single coin name; and (4) tweets containing a ‘buy’ signal typically mention at
least one specific coin, whereas, ‘not-buy’ tweets often do not specify any coin
name and usually focus on general market conditions.
Our time series analysis results showed that while there is a statistically
significant correlation between the attributes of the co-mentioned cryptocurren-
cies, the effect size is small (0.17). This suggests that influencers and news outlets
run other mechanisms to influence the mentioning patterns within their Twitter
posts. With respect to the correlation between the co-mentioned cryptocurren-
cies and their market prices, our analyses revealed that while the correlation
values for short-term dynamics consistently exceed 0.3 except for SHIB across all
pairs, when examining long-term dynamics, several pairs show correlations close
to zero or even negative values. Finally, our analysis of cryptocurrency prices
and social signals revealed mixed results, with some cryptocurrencies showing
a positive correlation with trading signals and others showing zero or negative
correlations.
Furthermore, this research limited its scope by testing only a few formulas for
obtaining social signals. However, there are additional possibilities to explore.
For instance, one could assign more weight to users with larger followings or
those who are more central within the follower network according to central-
ity measures. Similarly, greater weight could be given to tweets with numerous
likes and retweets. Another avenue for improvement is developing methods to
identify fake accounts, bots, misinformation spreaders, and campaigns attempt-
ing to manipulate the market.Future research should study other social media
platforms where cryptocurrency supporters and influencers are actively posting,
such as Reddit, Telegram, and YouTube, as well as exploring mechanisms that
could explain the sort of relationships we found in this paper.

Cryptocurrency News and Influencers’ Twitter Activity, and Market Prices 15
Acknowledgments. We thank Atena Jafari, Daria Stetsenko, Mahdis Abbasi, Dina
Della Casa, Zahra Baghshahi, Fabio Melliger, Sarvenaz Ebrahimi, and Maria Ko-
robeynokiva for their outstanding research assistance. Yasaman Asgari thanks the
University of Zurich and the Digital Society Initiative for (partially) financing this
project.
Disclosure of Interests. The authors declare that they have no competing interests.
References
[1] Meysam Alizadeh et al. “Open-source large language models outperform
crowd workers and approach ChatGPT in text-annotation tasks”. In:arXiv
preprint arXiv:2307.02179 (2023).
[2] Lennart Ante. “How Elon Musk’s twitter activity moves cryptocurrency
markets”. In: Technological Forecasting and Social Change186 (2023),
p. 122112.
[3] Malcolm Baker and Jeffrey Wurgler. “Investor sentiment in the stock mar-
ket”. In:Journal of economic perspectives21.2 (2007), pp. 129–151.
[4] Johan Bollen, Huina Mao, and Xiaojun Zeng. “Twitter mood predicts the
stock market”. In:Journal of computational science2.1 (2011), pp. 1–8.
[5] EnriqueCano-Marin,MarçalMora-Cantallops,andSalvadorSánchez-Alonso.
“Twitter as a predictive system: a systematic literature review”. In:Journal
of Business Research157 (2023), p. 113561.
[6] Eugene F Fama et al. “The adjustment of stock prices to new information”.
In: International economic review10.1 (1969), pp. 1–21.
[7] DavidGarciaandFrankSchweitzer.“Socialsignalsandalgorithmictrading
of Bitcoin”. In:Royal Society open science2.9 (2015), p. 150288.
[8] Ifigeneia Georgoula et al. “Using time-series and sentiment analysis to de-
tect the determinants of bitcoin prices”. In:Available at SSRN 2607167
(2015).
[9] Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli. “ChatGPT outper-
forms crowd workers for text-annotation tasks”. In:Proceedings of the Na-
tional Academy of Sciences120.30 (2023), e2305016120.
[10] Barbara Guidi. “When blockchain meets online social networks”. In:Per-
vasive and Mobile Computing62 (2020), p. 101131.
[11] Daniel Kahneman. “Maps of bounded rationality: Psychology for behav-
ioral economics”. In: American economic review 93.5 (2003), pp. 1449–
1475.
[12] Jermain Kaminski. “Nowcasting the bitcoin market with twitter signals”.
In: arXiv preprint arXiv:1406.7577(2014).
[13] Guy Kaplanski and Haim Levy. “Sentiment and stock prices: The case of
aviation disasters”. In:Journal of financial economics95.2 (2010), pp. 174–
201.
[14] Vytautas Karalevicius, Niels Degrande, and Jochen De Weerdt. “Using
sentiment analysis to predict interday Bitcoin price movements”. In:The
Journal of Risk Finance19.1 (2018), pp. 56–75.

16 M. Alizadeh et al.
[15] Young Bin Kim et al. “When Bitcoin encounters information in an on-
line forum: Using text mining to analyse user opinions and predict value
fluctuation”. In:PloS one 12.5 (2017), e0177630.
[16] Olivier Kraaijeveld and Johannes De Smedt. “The predictive power of
public Twitter sentiment for forecasting cryptocurrency prices”. In:Jour-
nal of International Financial Markets, Institutions and Money65 (2020),
p. 101188.
[17] Mikolaj Kulakowski and Flavius Frasincar. “Sentiment Classification of
Cryptocurrency-Related Social Media Posts”. In:IEEE Intelligent Systems
38.4 (2023), pp. 5–9.
[18] Haewoon Kwak et al. “What is Twitter, a social network or a news media?”
In: Proceedings of the 19th international conference on World wide web.
2010, pp. 591–600.
[19] Ting Li, Jan van Dalen, and Pieter Jan van Rees. “More than just noise?
Examining the information content of stock microblogs on financial mar-
kets”. In:Journal of Information Technology33.1 (2018), pp. 50–69.
[20] Xiaodong Li et al. “News impact on stock price return via sentiment anal-
ysis”. In:Knowledge-Based Systems69 (2014), pp. 14–23.
[21] Feng Mai et al. “The impacts of social media on Bitcoin performance”. In:
(2015).
[22] Huina Mao, Scott Counts, and Johan Bollen. “Predicting financial mar-
kets: Comparing survey, news, twitter and search engine data”. In:arXiv
preprint arXiv:1112.1051 (2011).
[23] Luca Mungo, Silvia Bartolucci, and Laura Alessandretti. “Cryptocurrency
co-investment network: token returns reflect investment patterns”. In:EPJ
Data Science13.1 (2024), p. 11.
[24] Richard L Peterson. Trading on sentiment: The power of minds over mar-
kets. John Wiley & Sons, 2016.
[25] Dehua Shen, Andrew Urquhart, and Pengfei Wang. “Does twitter predict
Bitcoin?” In: Economics letters174 (2019), pp. 118–122.
[26] Michael Sockin and Wei Xiong. “Decentralization through tokenization”.
In: The Journal of Finance78.1 (2023), pp. 247–299.
[27] David Valle-Cruz et al. “Does twitter affect stock market decisions? finan-
cial sentiment analysis during pandemics: A comparative study of the h1n1
and the covid-19 periods”. In:Cognitive computation14.1 (2022), pp. 372–
387.
[28] Xue Zhang, Hauke Fuehres, and Peter A Gloor. “Predicting stock market
indicators through twitter “I hope it is not as bad as I fear””. In:Procedia-
Social and Behavioral Sciences26 (2011), pp. 55–62.
[29] Yanzhao Zou and Dorien Herremans. “PreBit—A multimodal model with
Twitter FinBERT embeddings for extreme price movement prediction of
Bitcoin”. In:Expert Systems with Applications233 (2023), p. 120838.
