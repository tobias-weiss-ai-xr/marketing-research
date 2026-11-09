---
title: 'The predictive power of the Blockhain transaction networks: Towards a new generation of network
  science market indicators'
url: https://arxiv.org/abs/2401.01379
category: social-media
subcategory: empirical
date: 2023-12
venue: ''
authors:
- Mar Grande
- Florentino Borondo
- Javier Borondo
source: arxiv
pdf_url: https://arxiv.org/pdf/2401.01379
pages: 13
chars: 45106
fetched_at: '2026-11-08T13:04:36+00:00'
kb_version: 1
---

# The predictive power of the Blockhain transaction networks: Towards a new generation of network science market indicators

The predictive power of the Blockhain transaction networks: Towards a new generation of network
science market indicators
M. Grande, 1, 2, ∗ F. Borondo,3, † and J. Borondo 2, 4, ‡
1Grupo de Sistemas Complejos; Universidad Politécnica de Madrid; 28035 Madrid (Spain)
2AgrowingData; Navarro Rodrigo 2 AT; 04001 Almería (Spain)
3Departamento de Química; Universidad Autónoma de Madrid; CANTOBLANCO - 28049 Madrid, Spain
4Departamento de Gestión Empresarial; Universidad Pontificia de Comillas ICADE; Alberto Aguilera 23; 28015 Madrid (Spain)
(Dated: January 4, 2024)
Currently cryptocurrencies and Decentralized Finance (DeFi), which enable financial services on public
blockchains, represents a new growing trend in finance. In contrast to financial markets, ruled by traditional
corporations, DeFi is completely transparent as it keeps records of all transactions that occur in the network and
makes them publicly available. The availability of the data represents an opportunity to analyze and understand
the market from the complexity that emerges from the interactions of the actors (users, bots and companies)
operating in the embedded market. In this paper we focus on the Ethereum network and our main goal is to
show that the properties of the underlying transaction network provide further and useful information to fore-
cast the evolution of the market. We aim to separate the non-redundant effects of the blockchain transaction
network properties from classic technical indicators and social media trends in the future price of Ethereum.
To this end, we build two machine learning models to predict the future trend of the market. The first one
serves as a base model and considers a set of the most relevant features according to the current scientific liter-
ature—including technical indicators and social media trends. The second model considers the features of the
base model, together with the network properties computed from the transaction networks. We found that the
full model outperforms the base model and can anticipate 46% more rises in the price than the base model and
19% more falls. Thus, we conclude that indicators based on network properties provide valuable information to
forecast the future direction of the market that can not be explained neither by traditional indicators, or social
media trends. Hence, our results represent a first step towards a new family of DeFi market indicators based on
the complexity of the underlying transaction network.
I. INTRODUCTION
Cryptocurrencies and Decentralized Finance (DeFi), an
emerging financial technology based on secure distributed
ledgers, represent a new trend in finance that is growing expo-
nentially, taking components of traditional financial markets
and transforming them into transparent and decentralized pro-
tocols through smart contracts and tokens.
The appeal that this new paradigm offers to the popula-
tion is clear: access to all imaginable financial services —
savings accounts, insurance, loans, commerce— in an open
and borderless way. In this new scenario, all financial services
are carried out through decentralized applications that run on
the blockchain and therefore eliminate the need for a central
authority, which is its differential advantage over traditional
markets. Moreover, during the last decade the cryptocurren-
cies and DeFi market has become the fastest-growing alter-
native investment option, gaining widespread public and in-
vestors attention due to their extraordinary returns in phases of
extreme price growth. Another differential advantage of this
new market for investors is that, because of its decentralized
nature, it does not react to economic factors. Thus, the failure
of governments and central banks in the 2008 financial cri-
sis alongside the European Sovereign Debt Crisis, represented
an incentive for investors and other economic actors towards
∗ Email address: mar.grande@alumnos.upm.es
† E–mail address: f.borondo@uam.es
‡ Corresponding author email address: jborondo@gmail.com
cryptocurrencies that began to see them as an attractive invest-
ment alternative. However, the cryptocurrency market is still
in the nascent stages which involves a high volatility, present-
ing remarkable fluctuations and unexpected massive crashes.
The dynamics of the cryptocurrency market have attracted
the interest of financial institutions and researchers seeking to
understand its high volatility and price fluctuations. The be-
havior and evolution of all financial markets depends largely
on the behaviors of traders and investors operating in such
markets, and the cryptocurrencies and DeFi markets are no
exception. Seeking to take advantage of this behavior re-
searchers developed over the past century Technical Analy-
sis (TA) [1–3], a methodology to analyze and forecast the di-
rection of prices through the study of past market data (only
considering price and volume). This theory is founded on
the principle that a market’s price time series reflects all rel-
evant information impacting that market. Thus, researchers
in this field have developed over the past decades TA indica-
tors based on the history of an asset or commodity’s trading
patterns. The most well-known types of systems are moving
averages, channels (support and resistance) and momentum
oscillators. Several studies have already applied TA to study
and forecast cryptocurrencies price series, focusing mainly
in Bitcoin and Ethereum, and finding a correlation between
some technical indicators and their future price [4–6]. More
recently, other scholars have highlighted the power of social
media to capture the sentiment and behavior of users. Thus, a
recent line of research focuses on generating indicators based
on social media trends to forecast financial markets. Several
studies have focused on exploring the relation between social
arXiv:2401.01379v1  [cs.SI]  31 Dec 2023

2
media and the price of stocks [7, 8], while more recently, other
researchers have focused on the relation of these indicators to-
wards the cryptocurrency market [9–11].
However, a differential factor of this new system with re-
spect to traditional markets is that it keeps records of all trans-
actions that occur in the network and makes them publicly
available. The open nature of blockchain transactions involves
an opportunity and need to research new tools and methods
to analyze and track the movements of this novel market. In
contrast to other financial markets, we can process all the fi-
nancial interactions taking place on public blockchains, and
model the system as a network [12–14], analyzing it from the
perspective of complex systems [15–17]. This approach en-
ables us to capture the flow of information in the underlying
network and track the global behavior that emerges from the
interactions between users. Hence, the network representa-
tion and analysis of these publicly available transactions en-
ables a new form of financial econometrics—with the empha-
sis on the complexity that emerges from the interactions of
users rather than solely the covariance of historical time series
of prices and volume, how TA does. In this work, we take
advantage of network science to characterize the market, and
track and understand its evolution over time.
Recent scientific contributions have analyzed the transac-
tion network of several cryptocurrencies [18]. In [19] the au-
thors characterize the properties and the temporal evolution of
the transaction network of Bitcoin, Ethereum and Namecoin,
finding significant variations in their structural properties over
time. Other works have gone one step further, exploring the
relationship of network properties with the price, and finding
evidence to support that some subgraphs of the transaction
network can influence Bitcoin price [20]. In the same line
other authors have identified a relation between certain net-
work properties an bitcoin bubbles [21]. All of these works
have focused on analyzing the transaction network separately
and not controlling for other factors that could provide similar
information.
But neither social media trends nor TA indicators are in-
dependent from the network of transactions. All three fami-
lies of indicators seek to capture the behavior of users and are
therefore related. In fact, all the indicators form a network,
where they tend to cluster according to their family, but with
clear relations across the three sets (see Figure 1). Hence, to
properly interpret relationships between the evolution of the
price of cryptocurrencies, and the behavior of users operating
in the market, one needs to separate the effects of the trans-
action network properties from the social media trends and
the information already captured by TA. By separating these
effects we can claim whether the network of transactions con-
tains relevant and novel information about the market or not.
This paper aims to contribute to understanding the crypto
and DeFi markets by taking a first step towards a new line
of research in financial econometrics based on the complex-
ity that arises from the interactions that take place in pub-
lic blockchains (between billions of individuals, entities and
bots). In this work, we focus on Ethereum (ETH) because it
is by far the largest blockchain supporting smart contracts and
the majority of DeFi protocols and applications are built on
it. We puzzle out the effect that the transaction network prop-
erties, TA indicators and social media trends have on the fu-
ture price of ETH. To this end, we build two machine learning
models to predict the future trend of ETH. The first one serves
as a base model and considers a set of the most relevant fea-
tures according to the current scientific literature—including
TA indicators and social media trends. The second model con-
siders the features of the base model, together with the net-
work properties computed from the transaction networks. We
find that even after controlling for TA and social media, the
network properties still provide valuable information to fore-
cast the direction of the price, as the Full Model outperforms
the Base Model. In addition, the variables related to network
properties have a significant effect in the model. Finally, we
argue that our results highlight the need to develop a new fam-
ily of network based indicators for the emerging cryptocurren-
cies market.
II. RESULTS: THE PREDICTIVE POWER OF THE ETH
NETWORK
We begin by developing a machine learning model, based
on the XGBoost algorithm, with the categorized logarithmic
return of the close price as the dependent variable. The loga-
rithmic return is defined as:
rt+1 = ln( pt+1 pt )
where p is the close price at a timestamp t.
Next, to categorize the target, we consider that the logarith-
mic return has increased (decreased) within consecutive days
if the logarithmic return change is greater than 1% (lower than
-1%). Otherwise, we say that the logarithmic return has re-
mained constant. Hence, the target function takes a value of
1 to indicate an uptrend, -1 to indicate a downtrend, and 0
when it remains constant. As explanatory factors we use three
different sets of variables explained in section IV C. The first
set of variables, related to TA, is formed by some trend, vol-
ume, volatility and momentum indicators, which are widely
used in the scientific literature to anticipate the evolution of
markets. The second set of variables, related to social media
trends (SM), is formed by the variablesNumber of Tweetsand
GoogleTrends. This group accounts for the information or im-
pact that social media activity can have on the future prices.
Finally, the third set of variables, related to the network prop-
erties (NP), is formed by the main size, degree and connectiv-
ity properties of the network. Full details of all the variables
build and their description can be fount in section IV C. With
these three sets of variables, we set up two different specifica-
tions of the ML model. The first specification, or Base Model
(BM), serves as a baseline and includes the TA variables plus
the SM variables. The second specification of the model, or
Full Model (FM), adds the NP variables to the BM model.
The results obtained by both models are summarized in Fig-
ure 2. In panel A of this figure we compare the confusion ma-
trix of both models. As it can be seen the FM model achieves

3
FIG. 1. This figure summarizes the relations between the variables of the three family of indicators: network properties, technical analysis
and social media. Panel A show the network resulting from the correlation between all the variables considered in the study. Panel B shows a
filtered version of the network, only including the variables selected by the final model. Note that only significant correlation are represented
as links (p-value < 0.05)
a higher accuracy. To provide extra detail panel B of the figure
compares the precision, recall and F1-score of both models for
all classes, uptrends and downtrends.
The BM model has an accuracy of 37%, a precision of 38%
and a recall of 36%. Analyzing the model in further detail
we show that, anticipating downtrends, the Base Model shows
poor precision (32%) but a reasonably high recall (62%). This
means that the model is capable of anticipating 62% of the
future price drops, but in counterpart only 32% of the down-
trend signals will actually happen. Regarding uptrends, the
BM model exhibits the opposite behavior. The recall of the
model is poor (28%), while the precision increases up to 52%.
Thus, the model only anticipates 28% of the actual uptrends,
but over half of the times this signal is actually true. Next,
we analyze the results of the FM model, which actually sig-
nificantly outperforms the BM model. This model achieves
an accuracy of 44% (19% higher than BM), precision of 46%
(21% higher than BM), and recall of 42% (17% higher than
BM). Regarding the performance of the model on anticipat-
ing uptrends, the FM model increased the up recall on 46%
points in comparison to the BM model, reaching a final recall
of 41%. At the same time, the FM model obtained a higher
precision (59%) in uptrends than the BM model. This means
that the FM model anticipates 41% of the total uptrends, be-
ing almost 60% of these forecasts actually true. Regarding
downtrends, the improvement of the FM is slightly smaller.
However, still the FM has 16% higher precision (PFM = 37%)
and 19% higher recall (RFM = 74%). This means that despite
the model not being very precise anticipating downtrends, it
is capable of alerting almost 3 out of 4 of price drops. Finally,
we analyze the final features selected and their corresponding
importance in the best configuration of the FM model. We
observe that network properties play an important role in this
final best model, where from the final 15 variables 6 of them
are generated from the network properties. This is illustrated
in Figure 1, that shows in panel A a network representation of
all the initially considered variables, and in panel B, the final
variables selected in the FM. In addition, these variables in
general occupy top position in the ranking of feature impor-
tances according to different metrics, including cover, gain, or
mean decrease impurity among others (see the Methods sec-
tion for a full explanation on these metrics, and Appendix for
a table with the full results). We also have to highlight that
all three families of variables are present in the FM model.
Hence, the good performance of the model, that clearly out-
performs the BM model and random guessing, results from
the combination of the information hidden in the price time
series, social media and the network of transactions.
III. DISCUSSION
Today’s society is evolving towards a digital society where
the adoption of cryptocurrencies among citizens and compa-
nies grows every day, being used to trade, invest and specu-
late, as well as to access services. In fact, today, there are

4
FIG. 2. This figure compares the performance of the BM and FM models. Panel A shows a comparison between the confusion matrix of both
models, reflecting that the FM model achieves a higher accuracy. Panel B compares the precision, recall and F1-score of both models for all
classed, uptrends and downtrends. As it can be seen the FM model outperforms in all cases.
more than 1,500 cryptocurrencies and according to a recent
study [22] it is estimated that more than 35 million of private
and institutional investors participate in the different transac-
tion networks. This means that in order to anticipate new eco-
nomic crises, as well as promote a fair economy, it is neces-
sary to know and understand the mechanisms that move the
cryptocurrency market.
One of the key features of this emerging market that dif-
ferentiates it from traditional financial institutions is that it
operates on decentralized networks with verifiable transac-
tions that are publicly available. This availability of the trans-
actions opens an opportunity to analyze the market from a
novel perspective. Thus, we can take advantage of network
science [12–14] to capture the complex global behavior that
emerges from the individual transactions taking place in the
blockchain, and that drives the market. In this work, we have
analyzed the evolution of properties of the transaction net-
work, and shown that the information generated from them
is useful to anticipate the evolution of the prices even after
controlling by TA and social media trends. In fact, this repre-
sents one of the main contributions of our paper. In contrast to
previous studies that have focused on analyzing the effect of
each family of indicators separately, we analyze them together
untangling their impact in the evolution of prices.
The fact that the properties of the transaction network pro-
vide additional information that is not captured by TA indica-
tors, demonstrates that the transaction history includes extra
information that can not be obtained solely from the analyz-
ing the time series of prices and volumes. Hence, this result
has important implications for the Efficient Market Hypoth-
esis (EMH) debate [23, 24]. The EMH, was introduced by
Fama in 1970, and states that new information is immediately
reflected in asset prices, that therefore show martingale behav-
ior. Thus this scenario implies that no trading rules based on
the market time series can obtain returns that surpass the buy-
and-hold strategy. The current literature is full of papers both
supporting and rejecting the EMH [25–29] in several markets.
However, since most of these works focus on markets where
transactions are not public it has not yet been analyzed or dis-
cussed the implications that the network representation of the
transactions have on the predictability of the market.
But do our results mean that the information generated from
the complexity that emerges from the transaction network is
enough to understand the market? Not really. Under the light
of our results, the information generated from the underlying
transaction network is more valuable when combined with the
price time series and social media trends. In fact, we have
shown that these three sources of information are related but
at the same time contain complementary information. Hence,
we argue that the new cryptocurrency market, where trans-
parency and the public nature of transactions are key factors,
opens a new era in financial econometrics. Thus, opening a
new line of research focused on developing new methodolo-
gies and indicators that capture the complexity that emerges

5
from the transaction between users.
Finally, the fact that network properties provide new infor-
mation to understand the cryptocurrency markets invites us
to explore further and more sophisticated network representa-
tions and properties. In this regard, in this paper we have built
a single layer representation of the Ethereum system. How-
ever, there are multiple applications with their own token run-
ning on top of the Ethereum chain. Hence, it would be of
particular interest to model the system as a multiplex network
[30–32], where the nodes (wallets) can interact through mul-
tiple layers, each one representing a different application and
token. In addition, the features built from the network prop-
erties can be expanded in the future. For this work, we have
only included basic network properties to show the potential
of this line of research. However, once that the usefulness of
this information is clear, more research should be conducted
in order to build more informative indicators.
IV . MA TERIALS AND METHODS
A. Dataset
In the present work we analyze the network of transactions
that take place on the Ethereum Blockchain. These trans-
actions are public and real time available through https:
//etherscan.io. We collected all the transactions gener-
ated from January 2018 to January 2021, resulting in more
than 3 billion transactions.
The second part of this work focuseds on analyzing the re-
lation between the properties of the transactions network and
the price of ETH. For this, we consider a second dataset that
includes the time series of the daily price. This second dataset
was collected from Binance exchange, using its API. From
the data sollected from Binance we computed the most widely
used TA indicators that have already reported good results in
current literature for price prediction problems. Finally, we
include a third family of variables in our analysis related to
social media trends. To this end we obtained and computed
the number of tweets mentioning Ethereum and google trend
score for Ethereum.
B. Ethereum transaction network
The Ethereum system is an open source infrastructure built
on and supported by a blockchain, i.e. a decentralized public
ledger which records all transactions that occur in the system.
Once these transactions are uploaded to Ethereum, they can-
not be deleted or modified, which makes the system reliable.
Each transaction consists of a source address (where curren-
cies come from), a target address (where currencies go), the
amount of transferred coins and the timestamp among other
attributes.
In this paper, we built the transaction network between ad-
dresses, in which nodes represent the addresses that operate in
the system and links represent the transactions between them.
The direction of links is determined by the source and target
addresses and the weights are defined as the number of trans-
actions between each pair of nodes for each day. An example
of the network construction is illustrated in Fig. 3.
1. Time aggregation
The Ethereum transaction network is an evolving complex
system. Nodes are added to the network when new addresses
are created and removed when they are no longer involved
in any transaction, while new edges arise when there is a
transaction between two previously unconnected addresses.
Therefore, in order to understand the dynamics of this system,
we need to define dynamic intervals that match its evolution.
The choice of these intervals is key in this work because they
will condition our future analysis. In contrast to other works,
where the time aggregation is fixed and randomly chosen [33],
we apply the method developed by Darst et al. [34] that detects
evolutionary changes in the configuration of a complex system
and generates intervals accordingly. The size of each interval
is determined by maximizing the similarity between the sets
of events within consecutive intervals. In this case, the events
are the transactions recorded in the Ethereum Blockchain and
the similarity metric used is the jaccard index. When applying
this method to our dataset, we found that the optimal intervals
obtained are regular —around 14 days. Figure 4a) shows a
visualization of these intervals, along with the similarity score
obtained.
In Figure 4 b) we compare the evolution of the obtained
similarity score with the time series of the price observing a
strong and significant relation, proxied as the Pearson corre-
lation coefficient (r=-0.67, p-value=3.76e-07 ) with the price.
In summary, we found that the higher the price, the lower the
similarity score. As a lower similarity implies higher den-
sity of events, this result means that there is a positive lin-
ear relation between the number of events —i.e., number of
transactions— and the price.
C. Model features
In this section we describe the construction of the three sets
of variables we use to predict the future trend of ETH price.
To simplify the presentation, we divide our twenty five vari-
ables into three groups: network properties indicators (NP),
TA indicators and social media trends (SM).
The first set describes some important features that capture
the overall structure of the network giving insights into net-
work properties such as its connectivity. Some features are in-
dividual properties of each node, such as thedegree or PageR-
ank. In these cases, we use the mean and standard deviation of
these values as our topological feature for the entire network.
The second set of features considers the most relevant TA
indicators according to the current scientific literature for
price prediction problems —including trend, volatility, vol-
ume and momentum indicators.
The third set is composed by two variables that gather in-
formation about social media trends such as the number of

6
FIG. 3. Network representation of two transactions in the Ethereum system. Nodes represent addresses and the links —denoted with arrows—
represent transactions between two addresses. The property of the edges is the timestamp in which transactions were added to the Blockchain.
FIG. 4. Panel a) shows the time intervals (vertical lines) and similarity score (green lines) computed with Dynamic time-slicing method.
The blue line (y-axis) represents the average number of weighted events by the number of transactions. Panel b) shows the evolution of the
similarity score (green line) with the close price of Ethereum (blue line).
tweets mentioning Ethereum and the score in Google Trends.
1. Network properties
We compute the main properties of the network such as the
number of nodes and links of each network and the degree of
each node and its neighbors. Taking into account the degree
distribution of the nodes, we also build as a feature the slope
of this distribution in a log-log scale (the alpha coefficient if
it can be approximate by a power-law distribution). We also
include the ratio of active addresses (nodes in the network)
versus total addresses that there are in the system.
Other network properties that we included regarding the
connectivity of the network are:
• Assortativity. In this work, we focus on the assortativity
by degree, i.e., the tendency of nodes to connect others
with similar degrees. We compute the assortativity of
the network according to the degree correlation coef-
ficient introduced by Newman[35]. The formula is as

7
follows:
r = ∑
jk
jk(e jk − q jqk)
r2
with
r2 = ∑
k
k2qk −
" jk
∑
k
kqc
#2
where e jk is the probability of finding a link between
the nodes j and k and qk the probability that there is a
degree-k node at the end of the randomly selected link.
• Clustering coefficient. It measures the fraction of pos-
sible triangles that are actually closed. In the context
of transaction networks, a high clustering indicates that
people to whom I make transfers, make transfers be-
tween them. On the other hand, a low clustering means
that my neighbors do not transfer currencies between
them. In this work we calculate the local clustering of
nodes according to the method proposed by Watts &
Strogatz[36]. Thus, for a node of degree ki the local
clustering can be expressed as:
Ci = 2Li ki(ki − 1)
where Li represents the number of links among the
neighbors of node i. Hence, the average clustering co-
efficient of the network can be calculated as the average
of Ci for all nodes:
⟨Ci⟩ = 1 N N ∑ i=1 Ci
• Communities and modularity. A community can be de-
fined as a group of nodes that have a higher likelihood
of connecting to each other than to nodes from others
communities. The quality of a particular partition of a
network into communities can be measured by the mod-
ularity. It can be formulated as follows:
Q = |Ein| − ⟨|Ein|⟩ |E|
where |E| is the number of edges, |Ein| is the number of
edges within the community and ⟨|Ein|⟩ is the expected
number of edges within the community if the topology
were purely random. It ranges between [−1,1], where
1 indicates there are no links across different communi-
ties and -1 indicates that there are no links between the
nodes of a community. In this work, we use the Lou-
vain method proposed by Vincent Blondel et al.[37] in
2008. This method iteratively optimizes local commu-
nities until global modularity can no longer be improved
given perturbations to the current community state.
• Reciprocity. It is a metric for directed networks that
measures how likely is that a node you point to also
points back at you. More concretely, if there is an edge
from node i to node j and there is also an edge from j
to i then we say the edges are reciprocated. The reci-
procity r is defined as the fraction of edges that are re-
ciprocated.
• PageRank (PR). It is a centrality measure that deter-
mines the relative importance of a node within the net-
work. A node has a high PageRank when it is highly
connected or when it is attached to leading ones. The
PageRank value for any node u can be expressed as:
PR(u) = ∑
v∈Bu
PR(v)
L(v)
thus, the PageRank value for a node u depends on the
PageRank of its neighbors (Bu) and the number of links
of its neighbors L(v).
• Largest connected component (LCC). It is a maximal
subgraph in which any two nodes are connected by a
path. In this work, we did not take into account the
direction of the edges in order to compute the LCC.
LCC is an important factor in understanding the net-
work structure and can also be related to price. For in-
stance, we expect that the higher the number of nodes
in the LCC, the higher activity in the network, which
would lead to fluctuations in the price.
2. Technical analysis indicators
• Price trend. It is defined as the difference between the
close and open price.
• Exponential moving average of close price (EMA). We
consider three times windows for this feature: 7, 25 and
99 days.
• Moving average convergence divergence (MACD). It is
a trend-following momentum indicator that shows the
relationship between two moving averages of the price.
It is calculated as the difference between the EMA in a
window of 26 periods and the EMA in a window of 12
periods. A 9 periods EMA of the MACD is considered
as the signal line, which serves as the threshold for the
buy or sell signals.
• Relative strength index (RSI). It is a popular momentum
indicator which determines whether the stock is over-
purchased or over-sold.
• V olume. Total volume traded during the day. We also
consider the trend of the volume define as the change in
percentage with respect to the volume of the previous
day.

8
• On balance volume (OBV). It is a technical indicator
used to find buying and selling trends of a stock, by con-
sidering the cumulative volume: it cumulatively adds
the volumes on days when the prices go up, and sub-
tracts the volume on the days when prices go down,
compared to the prices of the previous day.
• V olatility. It is defined as the standard deviation of the
logarithmic return of the close price. We consider a time
window of 7, 14 and 21 days in order to build this fea-
ture.
• Average true range (ATR). It is a measure of the market
volatility and it is computed as follows:
AT R=
1
n
 n
∑
i=1
T Ri
with
T Ri = max



highi − lowi
|highi − closei−1|
|lowi − closei−1|
(1)
where T Ri is a particular True Range and n is a time
period.
• Price range. It is defined as the difference between the
high price and the low price for each day.
• Bollinger Bands. It is composed by a set of trend lines.
The central band is calculated from a simple moving
average (SMA) of the close price. The upper and lower
bands are then calculated by adding and subtracting two
times the standard deviation of the central band respec-
tively. The time window used to compute the SMA is
21 days. As features for the model we calculate the dis-
tance in percentage between the upper and lower band
and between the close price and each band.
3. Social media trends
• Number of tweets. It is the number of tweets using
#Ethereum hashtag in Twitter for each day. For this fea-
ture, we compute the change in percentage with respect
to the previous day.
• Google Trend score. It is related to the number of
searches in Google mentioning Ethereum. For this fea-
ture, we compute the change in percentage with respect
to the previous day.
D. Machine Learning models
In this work, we use three families of features to forecast
the future trend of the ETH, price and are not only interested
in the predictions, but also in understanding the contribution
of each family of features. In this scenario we have decided
to use machine learning (ML) as it can be successfully ap-
plied to financial problems [38, 39]. We believe ML is the
appropiate decision mainly because we are dealing with high-
dimensional data where the features are interrelated. Thus,
the flexibility of ML in comparison to classical econometric
models makes them a more efficient option to identify com-
plex patterns in a high-dimensional space.
Tree based models are popular machine learning ap-
proaches which can be used to solve a wide range of regres-
sion and classification problems. These models combined
with an ensemble technique have also reported better perfor-
mance than other machine learning algorithms in real world
problems, like stock market forecasting. For instance, in [40]
the authors proposed a system using XGBoost as a classifier
in order to forecast the stock market in 60-day and 90-day
periods and concluded that XGBoost turned out to be better
than other non-ensemble algorithms, such as Support Vector
Machines (SVM) and Artificial Neural Networks (ANN).
In this work, we train an XGBoost (Extreme Gradient
Boosting) [41] algorithm to predict the trend of the logarith-
mic return of the price. This algorithm is based on Tree Boost-
ing, a machine learning technique that attempts to create a
strong learner from a given number of weak learners, that only
performs slightly better than random guessing [42]. The main
principle of boosting is to iteratively fit a sequence of weak
learners to weighted versions of the training data. After each
iteration, misclassified input data gain a higher weight and ex-
amples that are classified correctly lose weight. Thus, future
weak learners focus more on the examples that previous weak
learners misclassified. At the end of the process, all of the suc-
cessive models are weighted according to their performance
and the outputs are combined using voting for classification
problems or averaging for regression problems, creating the
final model.
Once the XGBoost algorithm is trained it is possible to
measure the implication of each feature in the prediction. For
instance, we can rank the features by the number of times they
appear in a tree or by the number of predictions in which each
feature participates. In this work, we use this criteria in order
to measure the contribution of each variable in the model and
select a final set of features that provide the best prediction
results.
1. Training and testing
For training the model, we split the dataset into train and
test sets. The training period starts in January 2018 and ends
in June 2020, then starts the test period. Thus, there are 897
data points in the training set and 258 data points in the testing
set. The training set is used to select the optimal hyperparam-
eters of each model, so the test set is then used to evaluate the
performance of each model on unseen data.

9
2. Hyperparameters
In order to mitigate variability in the results, we have opti-
mized the hyperparameters for the XGBoost models by cross-
validated grid search, maximizing the area under the ROC
curve of the training set. The grid search is composed by the
following parameters:
• n_estimators. It is the number of trees in the algorithm.
• max_depth. It is the maximum depth that a tree can
grow.
• colsample_bytree. It is the subsample ratio of columns
when constructing each tree. Subsampling occurs once
for every tree constructed.
• min_child_weight. It is the minimum sum of instance
weight needed in a child. If the tree partition step results
in a leaf node with the sum of instance weight less than
min_child_weight, then the building process will give
up further partitioning.
• learning_rate. It is the step size shrinkage used in up-
date to prevents overfitting. After each boosting step,
we can directly get the weights of new features, and
learning rate shrinks the feature weights to make the
boosting process more conservative.
• gamma. It is the minimum loss reduction required to
make a further partition on a leaf node of the tree.
• subsample. Subsample ratio of the training instances.
Setting it to 0.5 means that XGBoost would randomly
sample half of the training data prior to growing trees.
and this will prevent overfitting. Subsampling will oc-
cur once in every boosting iteration.
The optimal values obtained in this way for each model can
be seen in table I.
3. Feature selection
Feature selection is the process of selecting a subset of vari-
ables from the input data that reduce effects from noise or
irrelevant variables and still provide good prediction results.
This technique is widely used in machine learning problems
because it helps to reduce the overfitting and complexity of
the model while improving the accuracy.
In this work we take into account the importance of each
feature provided by the XGBoost algorithm in order to select
the best set of features.
V . COMPETING INTERESTS
The authors declare no competing financial or non-financial
interests.
Parameter Base Model Full Model
n_estimators 100 100
max_depth 3 5
colsample_bytree 0.5 0.5
min_child_weight 13 13
learning_rate 0.05 0.01
gamma 0.08 0.05
subsample 0.5 0.5
TABLE I. Optimal hyperparameters used to train the machine learn-
ing models.
VI. AUTHOR CONTRIBUTIONS
All authors developed the idea and the theory. MG per-
formed the calculations and analyzed the data. All authors
contributed to the discussions and interpretations of the results
and wrote the manuscript.
ACKNOWLEDGMENTS
The project that gave rise to these results received the
support DGof Research and Technological Innovation of
the Comunidad de Madrid (Spain) under Contract No.
IND2022/TIC-23716
[1] C.-H. Park and S. H. Irwin, (2004).
[2] D. P. Brown and R. H. Jennings, The Review of Financial Stud-
ies 2, 527 (1989).
[3] J. L. Treynor and R. Ferguson, The Journal of Finance 40, 757
(1985).
[4] N. Gradojevic, D. Kukolj, R. Adcock, and V . Djakovic, Inter-
national Journal of Forecasting 39, 1 (2023).
[5] R. N. Ilham, I. Sinta, and M. Sinurat, Jurnal Ekonomi 11, 1022
(2022).
[6] A. Detzel, H. Liu, J. Strauss, G. Zhou, and Y . Zhu, Financial
Management 50, 107 (2021).
[7] T. H. Nguyen, K. Shirai, and J. Velcin, Expert Systems with
Applications 42, 9603 (2015).
[8] A. Sun, M. Lachanski, and F. J. Fabozzi, International Review
of Financial Analysis 48, 272 (2016).
[9] C. Lamon, E. Nielsen, and E. Redondo, SMU Data Sci. Rev 1,
1 (2017).
[10] R. C. Phillips and D. Gorse, in 2017 IEEE symposium series on
computational intelligence (SSCI) (IEEE, 2017) pp. 1–7.
[11] M. Ortu, N. Uras, C. Conversano, S. Bartolucci, and G. Deste-
fanis, Expert Systems with Applications 198, 116804 (2022).

10
[12] A.-L. Barabási, Philosophical Transactions of the Royal Soci-
ety A: Mathematical, Physical and Engineering Sciences 371,
20120375 (2013).
[13] A.-L. Barabási, Cambridge MA. Perseus (2002).
[14] M. Newman, A.-L. Barabási, and D. J. Watts, The structure
and dynamics of networks (Princeton university press, 2011).
[15] S. Boccaletti, V . Latora, Y . Moreno, M. Chavez, and D.-U.
Hwang, Physics reports 424, 175 (2006).
[16] S. H. Strogatz, nature 410, 268 (2001).
[17] J. Foster, Cambridge Journal of Economics 29, 873 (2005).
[18] N. Vallarano, C. J. Tessone, and T. Squartini, Frontiers in
Physics 8, 286 (2020).
[19] Z. D. Liang J, Li L, PLoS ONE 13 (2019).
[20] C. G. Akcora, M. F. Dixon, Y . R. Gel, and M. Kantarcioglu,
Economics Letters 173, 138 (2018).
[21] A. Bovet, C. Campajola, J. F. Lazo, F. Mottes, I. Pozzana,
V . Restocchi, P. Saggese, N. Vallarano, T. Squartini, and C. J.
Tessone, arXiv preprint arXiv:1805.04460 (2018).
[22] M. Rauchs, A. Blandin, K. Klein, G. Pieters, M. Recanatini,
and B. Zhang, 2nd Global Cryptoasset Benchmarking Study
(SSRN, 2019).
[23] E. F. Fama, The journal of Finance 25, 383 (1970).
[24] E. F. Fama, The journal of finance 46, 1575 (1991).
[25] M. T. Greene and B. D. Fielitz, Journal of Financial Economics
4, 339 (1977).
[26] F. Lillo and J. D. Farmer, Studies in nonlinear dynamics &
econometrics 8 (2004).
[27] B. Jacobsen, Journal of empirical finance 3, 393 (1996).
[28] A. W. Lo and A. C. MacKinlay, A non-random walk down Wall
Street (Princeton University Press, 2011).
[29] T. Di Matteo, T. Aste, and M. M. Dacorogna, Journal of bank-
ing & finance 29, 827 (2005).
[30] S. Boccaletti, G. Bianconi, R. Criado, C. del Genio, J. Gómez-
Gardeñes, M. Romance, I. Sendiña-Nadal, Z. Wang, and
M. Zanin, Physics Reports 544, 1 (2014), the structure and dy-
namics of multilayer networks.
[31] F. Battiston, V . Nicosia, and V . Latora, The European Physical
Journal Special Topics 226, 401 (2017).
[32] S. Gomez, A. Diaz-Guilera, J. Gomez-Gardenes, C. J. Perez-
Vicente, Y . Moreno, and A. Arenas, Physical review letters
110, 028701 (2013).
[33] A. ElBahrawy, L. Alessandretti, A. Kandler, R. Pastor-Satorras,
and A. Baronchelli, Royal Society open science 4, 170623
(2017).
[34] R. K. Darst, C. Granell, A. Arenas, S. Gómez, J. Saramäki, and
S. Fortunato, Scientific reports 6, 39713 (2016).
[35] M. E. Newman, Physical review letters 89, 208701 (2002).
[36] D. J. Watts and S. H. Strogatz, nature 393, 440 (1998).
[37] V . D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre,
Journal of statistical mechanics: theory and experiment 2008,
P10008 (2008).
[38] M. Dixon, I. Halperin, and P. Bilokon, Machine Learning in
Finance: From Theory to Practice (Springer International Pub-
lishing, 2020).
[39] M. de Prado, Advances in Financial Machine Learning (Wiley,
2018).
[40] S. Dey, Y . Kumar, S. Saha, and S. Basak, PESIT South Campus
, 1 (2016).
[41] T. Chen and C. Guestrin, inProceedings of the 22nd acm sigkdd
international conference on knowledge discovery and data min-
ing (2016) pp. 785–794.
[42] Y . Freund, R. Schapire, and N. Abe, Journal-Japanese Society
For Artificial Intelligence 14, 1612 (1999).

11
VII. APPENDIX
A. Features importances
Once an XGBoost is trained it is possible to measure the
implication of each feature in the prediction. For instance, we
can rank the features by the number of times they appear in
a tree or by the number of predictions in which each feature
participates. We use the following criteria in order to measure
the contribution of each feature in the model:
• Gain, it is the average gain (improvement in the score)
of splits which use the feature. A higher value of this
metric when compared to another feature implies it is
more important for generating a prediction.
• Cover, it is the average coverage of splits which use the
feature where coverage is defined as the number of sam-
ples affected by the split. For example, if we have 50
observations, 3 features and 2 trees, and suppose fea-
ture1 is used to decide the leaf node for 8 and 4 obser-
vations in tree1 and tree2 respectively; then the cover-
age for this feature is 8 + 4 = 12 observations. Thus, the
cover of this feature is 12 divided by the total number
of observations.
• Weight, it is the number of times a feature appears in
a tree. In the above example, if feature 1 occurred in 3
splits and 2 splits in tree1 and tree2; then the weight for
feature1 will be 3 + 2 = 5.
In Figures 5,6 and 7 we show the contribution of each feature
in the FM regarding gain, cover and weight respectively.
We also perform a permutation importance analysis. The
full procedure essentially consists in ‘eliminating’ variables,
one at a time, by making them random, and simultaneously
monitoring the loss of in a model score. Here we use the accu-
racy score and the impurity. Figures 9 and 8 show the results
for each feature.

12
FIG. 5. Feature importances measure by the average gain (improvement in the score) of splits which use the feature.
FIG. 6. Feature importances measure by the average coverage of splits which use the feature.
FIG. 7. Feature importances measure by the number of times each feature appears in a tree in the FM.

13
FIG. 8. Feature importances measure by the mean impurity decrease.
FIG. 9. Feature importances measure by the mean accuracy decrease.
