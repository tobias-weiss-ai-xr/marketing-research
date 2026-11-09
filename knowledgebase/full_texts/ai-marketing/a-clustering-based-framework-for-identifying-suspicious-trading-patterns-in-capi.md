---
title: A Clustering-Based Framework for Identifying Suspicious Trading Patterns in Capital Market
url: https://arxiv.org/abs/2607.04184
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Asif Zaman
- Romona Magdalene Sarkar
- Sabiha Khair Ohi
- Iftekharul Mobin
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.04184
pages: 6
chars: 22569
fetched_at: '2026-11-08T13:08:35+00:00'
kb_version: 1
---

# A Clustering-Based Framework for Identifying Suspicious Trading Patterns in Capital Market

A Clustering-Based Framework for Identifying
Suspicious Trading Patterns in Capital Market
Asif Zaman
Department of Computer Science & Engineering
American International University-Bangladesh
Dhaka,Bangladesh
25-93713-1@student.aiub.edu
Romona Magdalene Sarkar
Department of Computer Science & Engineering
American International University-Bangladesh
Dhaka,Bangladesh
24-93338-1@student.aiub.edu
Sabiha Khair Ohi
Department of Computer Science & Engineering
American International University-Bangladesh
Dhaka,Bangladesh
25-93714-1@student.aiub.edu
Iftekharul Mobin
Department of Computer Science & Engineering
American International University-Bangladesh
Dhaka, Bangladesh
iftekhar.mobin@aiub.edu
Abstract—Market manipulation is the dubious practice of
manipulating stock prices in order to make a quick profit,
which truly degrades confidence on trading platforms. We
implemented an unsupervised fraud-detection toolkit that
begins with K-Means++ clustering to address this issue.
A dataset of roughly one million financial transactions
from 2012 to 2024 is used. In order to identify fraudulent
trades and categorize them using market practice heuristic
thresholds, the study suggests a clustering-based pipeline.
The method highlights 2.02% of trades as suspicious where
51.10% clearly indicate spoofing, 0.10% indicate pump and
dump, 0.55% indicate insider trading, 1.43% indicate a
fake breakout, and 46.83% are unclassified. Despite the
lack of ground truth, the model’s performance is confirmed
by a Silhouette Score of 0.561.
Index Terms—Manipulation, Stock Market, Detection,
Price, Visualization.
I. INTRODUCTION
Every nation’s infrastructure is extremely dependent
on the state of its economy. An essential component
of the nation’s economic growth is the stock market.
As new products and trends shape the market, stock
markets are evolving. The idea of a stock market is slowly
gaining momentum in Bangladesh. Despite improvements
in financial literacy, DSE participation is still low. Growth
is still low because of investor mistrust, anticipated
dangers, and previous market fraud incidents [1]. Due
to its isolation from international markets the DSE has
limited growth especially in times of crisis like COVID-19
[2]. The Dhaka Stock Exchange shows chronic volatility
clustering due to severe volatility of the Bangladeshi stock
market. Macroeconomic factors such as inflation, interest
rates, currency rates, and external shocks had a significant
impact on it [3]. Investor trust has been damage and long-
term economic progress has been hampered by problems
including insider trading and manipulation [4].
Because they rely on labeled data and predefined
patterns, traditional regulatory and supervised machine
learning approaches frequently fail to identify complex
fraudulent activities in financial markets [5]. K-Means
clustering has demonstrated promise in fraud detection
by rapidly classifying regular and suspicious transactions
[6]. A lightweight, unsupervised, clustering-based fraud
detection framework that can adaptively identify suspi-
cious trading behaviors from evolving market data is
critically needed.This study develops a generic pipeline
capable of detecting potential market manipulation and
manipulative behaviors in historical stock trading data.
The main contributions of this research include -
1) We propose a scalable unsupervised Stock Mar-
ket Manipulation Detection (SMMD) framework
that integrates clustering-based structural anomaly
detection with behavioral financial heuristics.
2) We extract nine technical indicators using 30-
day rolling windows to capture temporal patterns
indicative of abnormal trading behavior.
3) K-Means outperforms DBSCAN, OPTICS, and hi-
erarchical clustering in accuracy (0.987), silhouette
score (0.965), and scalability, making it highly
effective for detecting sparse fraudulent trading
patterns [7].The proposed KMeans clustering al-
gorithm marks outliers as potential indicators of
suspicious activity and natural clusters of regular
trading patterns.
4) We provide interpretable fraud-type categorization
aligned with real-world manipulation patterns.
5) We present an adaptive percentile-based risk cate-
gorization approach and a symbol-level suspicion
rating system.
6) To minimize false positives, we develop a hybrid
1
arXiv:2607.04184v1  [cs.AI]  5 Jul 2026

Fig. 1: Market manipulation detection workflow
anomaly filtering system that combines percentile-
based behavioral criteria with distance-based outlier
detection.
II. LITERATUREREVIEW
Traditional supervised learning models have been
widely used for fraud detection, but their effectiveness is
confined by the need for enormous volumes of labeled
data and inability to identify key fraud patterns. Currently,
more researchers are focusing on unsupervised learning
methods that could overcome these issues, especially
clustering algorithms, which enable anomaly detection
in unlabeled information.
Zengyi et al. [6] performed actual transaction data
analysis in the identification of financial fraud using
the K-means unsupervised clustering technique. Principal
Component Analysis was used for the simplification of
data and the identification of key elements useful in fraud
detection.
SimCLR and its usage were introduced by Xuan
Li et al. in 2024 [8]. SimCLR identifies transaction
patterns and identifies unusual transaction activities
without requiring supervision. The authors conducted
an experiment on an eBay transaction data set which
contained all sorts of actions. The research used various
ways of data preparation and an exclusive technique
which uses SimCLR contrastive learning.
To be able to detect anomalies within stock price
time series data, Wenjie, Ruofan, and Bofan (2020) [9]
designed a deep learning model that incorporated Conv1D
and LSTM. Conv1D enabled it to divide data into 30-day
chunks. Subsequent LSTM layers enabled it to detect
long-term trends. The model also incorporated three dense
layers for forecasting.
Li et al. (2025) [10] developed an ensemble machine
learning framework to identify unusual trading by APAC
investors in U.S. markets. It removed the error rates
by 34.7% and obtained an AUC-ROC of 0.971 using
data from approximately 847,000 accounts across twelve
APAC economies.The study emphasizes the significance
of incorporating behavioral economics and advanced
machine learning into RegTech. To detect fintech fraud
Darwish et al. (2025) [11] presented a multi-stage
hybrid methodology. To solve class imbalance, they used
rule-based filtering, K-means clustering, Artificial Bee
Colony (ABC) optimization, and KNN classification
with ABC-sampling.On e-commerce datasets, it obtained
95.0% accuracy.It reduces false positives and improves
robustness in fraud detection using unbalanced data.
III. RESEARCHMETHODOLOGY
An unsupervised learning model is proposed to detect
the manipulated stocks of daily stock data from 2012 to
2024. Necessary steps have been taken to preprocess the
data.
Fig. 1 outlines our study’s process.
A. Data Preprocessing
To ensure the quality and reliability of the stock market
dataset, a series of preprocessing steps were implemented:
2

• The ”Date” field was converted to the right datetime
format, and duplicate, erroneous, and incomplete
entries were eliminated from the data.
• Dropna() was used to eliminate missing values in
the rows, leaving a clean dataset with 1,019,783
rows.
B. Feature Engineering
To enhance the model’s ability to detect suspicious trad-
ing patterns, multiple features were engineered from the
cleaned stock dataset. Nine new features were developed
using a 30-day rolling frame to capture trading trends and
detect anomalies. Infinite division values were substituted
with NaNs, then replaced with default values.Before being
employed in anomaly detection clustering, all features
were standardized.
C. Feature Scaling
In machine learning, feature scaling is a method
for normalizing independent variables or features to
a specific range [12]. After cleaning all features were
consistent. Then, we standardized the selected features
with StandardScaler, which gives a mean of 0 and a
standard deviation of 1. This phase guarantees that all
features contribute equally to the clustering procedure by
increasing model performance and stability. The pseu-
docode for Algorithm 1 outlines a six-phase unsupervised
pipeline to detect anomalous trading patterns in daily
stock data spanning 2012–2024. The definitions of all the
variables used in the pseudocode are provided in Table I.
D. Model Training
Clustering is an unsupervised classification method
that divides a set of multidimensional data into clusters
based on a predetermined criterion [13].
1) K-means++ Clustering Algorithm:K-means++ is
a popular variant of K-means for minimizing the Sum
of Squared Euclidean Distances (SSEDM). K-means++
iteratively selects initial cluster centres in a way that
spreads them out, allowing the algorithm to converge
faster and avoid poor local minima [14].
2) Clustering with K-Means++ using the Elbow
Method:To establish a k value, which is applied to cluster
the datasets into k sets, we used the elbow approach to
calculate the number of clusters. From the plot, we can
see a significant decrease in inertia from k = 2 to 6.
Fig. 2 shows the elbow method used for optimal k
clusters.
3) K-Means++ Algorithm Implementation Steps:This
whole algorithm operates in the following steps [15]:
• In order to find the value of k we used the technique
of Elbow. The value of k is chosen where the
reduction in inertia slows down.
• The initial location of the centroid is random. For
each observation, the closest centroid in Euclidean
distance is assigned. Then the center of mass is
found for each of the k groups.
• The process is stopped when there is less than a
certain fixed distance between the two centers of
mass. Otherwise, the process is repeated.
E. Proposed Algorithm: Stock Market Manipulation
Detection (SMMD)
Algorithm 1SMMD: Stock Market Manipulation Detec-
tion
Require: Excel sheets 2010–2020, 2021–2024; exclude {2010,2011} ;
k= 5,p 95,∆p thr = 10
Ensure:Flagged trades, fraud type, risk score, metrics
// Load & Clean
1df←CONCAT(Load(2010–2020),Load(2021–2024))
2Filter out years∈ {2010,2011}; replaceNULL→NaN
3cleaned_df←DROPNA(d f)
// F eatures
4foreach row∈cleaned_dfdo
5∆P%← C−O O ×100
6R←H−L
7end for
8Group bySymbol→G
9foreachg∈Gdo
10V 30 ←ROLLMEAN(g.V ol,30)
11T 30 ←ROLLMEAN(g.Trade,30)
12σ 30 ←ROLLSTD(g.Close,30)
13S V =V /V30, ST =T /T30, ST urn=T urn/T urn30
14V W AP=T urn/V, P avg = (O+C)/2
15end for
// Scale & Cluster
16X←[∆P%, R, σ 30, SV , ST , ST urn, V W AP]
17X←REMOVEINFNAN(X)
18X s ←STANDARDIZE(X)
19M←KMEANS(X s, k)
20Cluster←PREDICT(M)
// Anomaly Detection
21d i ← ∥xi −c cluster∥2
22t d ←QUANTILE(d,0.95)
23t V , tT ←95 th percentile ofS V , ST
24foreach rowdo
25ifd i > td ∧(|∆P%|>10∨S V > tV ∨S T > tT )then
26Suspicious←True
27end if
28end for
// Risk & Fraud Labeling
29Group bySymbol→G s
30foreachg∈G s do
31Score←(%suspicious)×100
Risk=



Critical RiskScore >90
High Risk75< Score≤90
Medium Risk50< Score≤75
Low Risk25< Score≤50
Minimal RiskScore≤25
32Sort byDate
→ Check 5-day future:pump-and-dump,rug pull,spoofing,
etc.
33end for
// Evaluate
34Sil←SILHOUETTE(Sample(X s ≤10k),Cluster)
35Plot fraud type distribution; output ranked symbols
3

TABLE I: Variable definitions used in the Stock Market Manipulation Detection (SMMD) pseudocode.
Symbol Description
C, O, H, LDaily closing, opening, high, and low prices
V, T, T urnTrading volume, number of trades, and turnover (monetary value)
∆P%Percentage price change: C−O O ×100 RIntraday price range:H−L
V30, T30 30-day rolling average of volume and number of trades
σ30 30-day rolling standard deviation of closing price (volatility)
SV , ST , ST urn Spike ratios:V /V30,T /T30,T urn/T urn30
V W APV olume-weighted average price:T urn/V
Pavg Average of open and close:(O+C)/2
X, Xs Feature matrix and its standardized version
k, MNumber of clusters (k= 5) and fitted K-Means model
di Euclidean distance of pointito its cluster center
td, tV , tT 95th percentile thresholds for distance and spike features
ScoreSuspicion score: percentage of flagged days per stock
Fig. 2: Elbow Method for Optimal k
F . Model Evaluation
Silhouette Score: Silhouette analysis mainly checks
how close each item in the cluster is to items in other
clusters. The score value ranges from -1 to +1. A score
value of +1 indicates that objects are well-clustered,
whereas a score value of -1 shows that the objects are
not correctly clustered [16].
For a single samplei:
s(i) = b(i)−a(i) max{a(i),b(i)} (1)
Where:
1) a(i) = average distance between i and all other
points in the same cluster.
2) b(i) = average distance between i and all points
reside in any other cluster.
IV. RESULT ANDDISCUSSION
A. Anomaly Detection Results
Outliers were spotted by calculating how far each trade
was from its cluster’s center.The top 5% farthest labeled
as structural outliers. To detect suspicious trades, behav-
ioral thresholds such as volume spikes, transaction count,
turnover which is above the 95th percentile [17],and
price fluctuations greater than 10% were observed. Only
a trade that is distant from a cluster and exhibited at
least one of the following behaviors would be considered
suspicious. Lastly,the suspicious trade is processed by a
fraud detection scoring system.
B. Suspicious Symbol Scoring
The suspicion score for stocks is calculated by combin-
ing fraud frequency and anomaly severity.The Frequency
indicates if the unusual activity happen frequently and
the Severity determines how extreme the unusual trades
are.The formula is defined in the equation 2 :
Suspicion score=α
 F
T ×100

+ (1−α)

P R(D)

(2)
where:
•F = Number of flagged trades.
•T = Total number of stock trades.
•PR(D) = Percentile rank of the anomaly distance.
•α= Weight parameter for frequency.
•1−α= Weight parameter for severity.
C. Risk Categorization Method
The next stage of the study is to classify stocks into
various risk levels after calculating each stock’s final
suspicion score. Table II shows the risk category and its
percentile range.
D. Fraud Type Classification
The flagged trades were examined and sorted into six
fraud categories. Fig. 5 shows fraud pattern breakdown
of top 20 suspicious stocks.
• Pump & Dump: A stock’s price quickly rises by
over 10% [18] along with high trading volume, and
then the price falls again within five days.
4

Fig. 3: DSE Stocks closing price with detected suspicious
trades (2012–2024)
Fig. 4: NSE Stocks closing price with detected suspicious
trades (2012–2025)
Fig. 5: Fraud Pattern Breakdown of Top 20 Suspicious Stocks
TABLE II: Adaptive Risk Categorization Based on
Percentile Thresholds
Risk Category Percentile Range
Critical Risk ≥90 th
High Risk 75th −90 th
Medium Risk 50th −75 th
Low Risk 25th −50 th
Minimal Risk ≤25 th
• Spoofing: High order or transaction volume with
minor price fluctuation [19].
• Rug Pull: A sharp rise in both price and volume
was followed by a steep decline [20].
• Insider Trading:A sharp increase of more than ten
percent on a low-volume spike of less than one point,
which suggests possible insider trading.
• Fake Breakout: The price increased over 10% with
high volatility, but reversed within a week.
• Unclassified Fraud: If none of the above fits, we
toss the odd data point into unclassified.
E. Fraud Type Classification Criteria
Based on observable features, heuristic rules classified
suspicious trading behavior to match real-world fraud
patterns. . The Table III shows the particular criteria used
to classify flagged trades as known fraud types.
TABLE III: Heuristic Rules and Feature Thresholds Used
for Fraud Type Classification
Fraud Type Price (%) Vol. Spike Trades Spike Range Lookahead
Pump & Dump +10→ −10 >95 th pct – – 5 days
Spoofing <5 >95 th pct >95 th pct – Same day
Rug Pull +10→ −10>95 th →<0.5× – – 5 days
Insider Trading >10 <1.0× – – Same day
Fake Breakout >10(reversal) – – >90 th pct 5 days
Unclassified Any >95 th pct >95 th pct – N/A
F . Visualization of fraud trades
Each stock’s closing price is plotted alongside red
markers that indicate suspicious trades in the visual-
ization. According to their Suspicion Scores, stocks
like UNILEVERCL (44.1%), SQURPHARMA (22.1%),
5

ACI (19.3%), HEIDELBCEM (18.2%), MEGCONMILK
(18.9%), and BEXIMCO (17.9%) display a variety of
anomalous density. To understand when these suspicious
trades happened, a chart of flagged trades marked by red
‘×’ symbols. Fig. 3 depicts some random 6 suspicious
stocks of DSE. Our proposed manipulation detection
system is applied on the NSE (National stock market of
India) dataset to test its effectiveness in a global market
context in Fig. 4 .
G. Model Evaluation
The assessment of the clustering-based anomaly de-
tection system relied primarily on the Silhouette Score
which served as the main indicator of model performance.
The obtained scores of 0.561 and 0.292 show well-
defined and separated clusters for both exchanges.
H. Result Summary
The Clustering Model performed effectively by achiev-
ing a silhouette score of 0.561. 2.02% of deals were
reported as suspicious which indicates a suitable de-
tection rate for identifying anomalies in DSE financial
data.Spoofing was the most frequent containing 51.1%
cases while other types of fraud were less frequent.This
approach should work with datasets from around the
globe which remain unlabeled dataset. It worked well
even in Bangladesh’s unstable trading conditions.
V. CONCLUSION
The system detects, visualizes, and interprets unusual
trading behavior in real-world market data. This checked
more than one million trades from the Dhaka Stock
Exchange with the help of rules and grouping, yielding a
varying verification rate of 2.02% with a silhouette score
of 0.561. It performs well on noisy and irregular data.It
works well on global data and help label trading dataset
that isn’t structured.
The lack of confirmed ground-truth data in the study is
a disadvantage.In addition,the thresholds could not adapt
well to highly dynamic marketplaces. While calculating
suspicion scores, the 60/40 weight distribution is a
heuristic that may need to be adjusted for other trading en-
vironments.The system emphasizes classifying anomalous
stock returns rather than precise classification. Advanced
clustering techniques like DBSCAN/HDBSCAN and
scalable real-time processing are the indications of future
enhancements.The system may become more effective
and flexible for market analysts and regulators by ensuring
stability and market transparency in global markets.
REFERENCES
[1] N. T. Chowdhury, N. S. Mahdzan, and M. Rahman. Beyond intu-
ition: The role of financial knowledge in navigating investments
in emerging markets.International Journal of Economics and
Financial Issues, 14(4):267–281, 2024.
[2] F. A. B. Habib. Evaluating the effectiveness of macroeconomic
determinants on the performance of the dhaka stock exchange:
A time series approach.Journal of Ekonomi, XX(XX):XX–XX,
2024.
[3] M. Jakaria, H. Shikder, N. M. Himel, N. Siddiqui, and M. M.
Rahman. Analyzing stock price volatility: A statistical study
of three listed companies on the dhaka stock exchange.Asian
Business Review, 2025.
[4] M. I. Wahab and F. Olakkodu. Insider trading: An overview in
indian and global markets.Journal of Informatics Education and
Research, 5(XX):XX–XX, 2025.
[5] S. K. Vangibhurathachhi. Machine learning for fraud detection
in financial transactions.International Journal on Science and
Technology, 16(XX):XX–XX, 2025.
[6] Z. Huang, H. Zheng, C. Li, and C. Che. Application of machine
learning-based k-means clustering for financial fraud detection.
Academic Journal of Science and Technology, 10(1):33–39, 2024.
[7] V . N. Mandhala et al. Comparative analysis of clustering
algorithms for financial fraud detection.International Journal of
Safety & Security Engineering, 15(4), 2025.
[8] Y . Peng, X. Sun, Y . Duan, Z. Fang, and T. Tang. Unsupervised de-
tection of fraudulent transactions in e-commerce using contrastive
learning. arXiv preprint arXiv:2503.18841, 2024. Accessed:
2026-02-20.
[9] W. Yang, R. Wang, and B. Wang. Detection of anomaly stock
price based on time series deep learning models. InProc. 2020
Management Science Informatization and Economic Innovation
Development Conf. (MSIEID), pages 110–114, December 2020.
[10] Y . Li, S. Fan, and H. Wang. Machine learning-based identification
of anomalous trading behavior patterns among asia-pacific in-
vestors in u.s. securities markets.Spectrum of Research, 5(1):XX–
XX, 2025.
[11] S. M. Darwish, A. I. Salama, and A. A. Elzoghabi. Intelligent
approach to detecting online fraudulent trading with solution for
imbalanced data in fintech forensics.XX, 15(1):17983, 2025.
[12] R. Hasan, B. Biswas, M. Samiun, M. A. Saleh, M. Prabha, J. Akter,
F. H. Joya, and M. Abdullah. Enhancing malware detection with
feature selection and scaling techniques using machine learning
models.Scientific Reports, 15(XX):XX–XX, 2025.
[13] G. Oyewole and G. Thopil. Data clustering: Application and
trends.Artificial Intelligence Review, 56:6439–6475, 2022.
[14] R. Aliguliyev and S. F. Tahirzada. Performance comparison of k-
means, parallel k-means and k-means++. Unpublished manuscript,
2023.
[15] R. H. Khan, D. F. Dofadar, and M. G. R. Alam. Explainable
customer segmentation using k-means clustering. InProc.
UEMCON 2021, pages 639–643, 2021.
[16] J. Meng, A. M. Abed, M. G. Elsehrawy, A. D. Al Agha, N. Ab-
dullah, S. Elattar, M. Abbas, H. Al Garalleh, and H. Assilzadeh.
Nano-integrating green and low-carbon concepts into ideological
and political education in higher education institutions through
k-means clustering.Heliyon, 10:e31244, 2024.
[17] T. Fabre and I. M. Toke. High-frequency market manipulation
detection with a markov-modulated hawkes process. arXiv preprint
arXiv:2502.04027, 2025. Accessed: 2026-02-20.
[18] B. Rizvi, A. Belatreche, A. Bouridane, and I. Watson. Detection of
stock price manipulation using kernel-based principal component
analysis and multivariate density estimation.IEEE Access,
8:135989–136003, 2020.
[19] J. Hambuckers, L. Sun, and L. Trapin. Measuring tail risk at high-
frequency: An L1-regularized extreme value regression approach
with unit-root predictors. arXiv preprint, 2023.
[20] Y . Li, N. Yao, Y . Huo, and W. Cai. Trust dynamics and bot-driven
responses: An approach to rug pulls in solana meme coin markets.
InProc. 17th ACM Web Science Conf. (WebSci), 2025.
6
