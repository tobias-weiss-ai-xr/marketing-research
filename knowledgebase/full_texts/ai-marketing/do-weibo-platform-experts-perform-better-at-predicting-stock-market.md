---
title: Do Weibo platform experts perform better at predicting stock market?
url: https://arxiv.org/abs/2403.00772
category: ai-marketing
subcategory: empirical
date: 2024-02
venue: ''
authors:
- Ziyuan Ma
- Conor Ryan
- Jim Buckley
- Muslim Chochlov
source: arxiv
pdf_url: https://arxiv.org/pdf/2403.00772
pages: 12
chars: 30059
fetched_at: '2026-11-08T13:19:03+00:00'
kb_version: 1
---

# Do Weibo platform experts perform better at predicting stock market?

Do Weibo platform experts perform better at
predicting stock market?
Ziyuan Ma1, Conor Ryan 2, Jim Buckley 2, and Muslim Chochlov 2
1 University of Limerick, Department of Computer Science and Information
Systems, Limerick, Ireland
curlyjuanjuan@foxmail.com
2 University of Limerick, LERO, Limerick, Ireland
{Conor.Ryan,Jim.Buckley}@ul.ie Muslim.Chochlov@lero.ie
Abstract. Sentiment analysis can be used for stock market prediction.
However, existing research has not studied the impact of a user’s finan-
cial background on sentiment-based forecasting of the stock market using
artificial neural networks. In this work, a novel combination of neural net-
works is used for the assessment of sentiment-based stock market predic-
tion, based on the financial background of the population that generated
the sentiment. The state-of-the-art language processing model Bidirec-
tional Encoder Representations from Transformers (BERT) is used to
classify the sentiment and a Long-Short Term Memory (LSTM) model
is used for time-series based stock market prediction. For evaluation, the
Weibo social networking platform is used as a sentiment data collection
source. Weibo users (and their comments respectively) are divided into
Authorized Financial Advisor (AF A) and Unauthorized Financial Advi-
sor (UF A) groups according to their background information, as collected
by Weibo. The Hong Kong Hang Seng index is used to extract historical
stock market change data. The results indicate that stock market pre-
diction learned from the AF A group users is 39.67% more precise than
that learned from the UF A group users and shows the highest accuracy
(87%) when compared to existing approaches.
Keywords: Sentiment analysis · Artificial neural networks · Stock pre-
diction · Chinese natural language processing.
1 Introduction
There is a wide range of factors affecting the stock market: national policies,
exchange rates, epidemics, amongst others [1].
Recently, several sentiment-based stock market prediction approaches have
relied on social media comments and short texts (for example, ’tweets’) towards
stock market prediction [2,3,4,5]. The existing approaches, however, do not dif-
ferentiate sentiments according to the users’ financial background.
Weibo is the largest social media platform in China that allows for qualifica-
tion certificates to be provided by users as evidence of their professional back-
ground. This allows for more reliable user grouping into an Authorized Finan-
cial Advisor (AF A) group and an Unauthorized Financial Advisor (UF A) group
arXiv:2403.00772v1  [q-fin.ST]  12 Feb 2024

2 Ma, Ziyuan et al.
(unauthorized and without certificates). However, to the best of our knowledge,
there is currently no comparative study on the financial background of users on
the Weibo platform towards the accuracy of stock market prediction. Such a
study could be used towards the improvement of existing sentiment-based stock
market prediction systems: for example, higher weights could be given to sen-
timents published by a certain user group (if known for its better prediction
accuracy). The research question of this paper, therefore, is: How do senti-
ments of AF A users compare to UF A users in terms of stock market
prediction accuracy?
To address this question, this work extracts stock market related comments
of AF A and UF A users on the Weibo platform, uses these comments with a
novel combination of neural networks for stock market prediction, and compares
whether there is a difference between AF A and UF A users’ comments in predict-
ing the stock market. The main contributions of this paper can be summarized
as follows:
– A novel combination of natural language processing neural network (BERT)
and LSTM neural network towards stock market prediction;
– Implementation of this prediction model (along with data of this experiment)
that is publicly available on Github 3;
– Resulting from the first contribution, the finding that financial experts (AF A
group) are 39.67% more accurate in their stock market predictions than UF A
group.
The remaining chapters of this paper are as follows. Section Two discusses
related work in sentiment analysis and development of stock market forecasting
models. Section Three explains the structure of the stock market prediction
system used in this work, as well as the functions and implementation details
of each module in the system. Section Fourpresents the empirical design of the
study and Section Five describes the results of the empirical study. Section Six
summarizes threats to the validity of the experiment and Section Seven draws
conclusions and suggests possible future work.
2 Related work
Brown and Cliff [6] have proposed the possibility of using collective sentiment
indicators to predict the stock market, opening up a new research direction. For
example, [4,5] used comments on the stock market and then categorize them by
sentiment. Based on these results, a causal relationship between the movement
of the stock market and comment sentiment was derived. More recently, Chu
et al. proposed a wavelet [7] method to identify the causal relationship between
stock market returns and investor sentiment[8]. These (social media sentiments
and time series based stock prediction) are the basis of this work.
3 https://github.com/majuanjuan/Doexpertsperformbetter

Do Weibo platform experts perform better at predicting stock market? 3
2.1 Sentiment analysis using neural networks
In the field of natural language processing, the methods employed in sentiment
analysis problems can be divided into statistics-based sentiment dictionary meth-
ods and machine learning methods [9].
In machine learning approaches, texts are converted into vectors, and then the
classification of a vector is obtained [10]. Language models such as word2vec[11],
given texts, can produce word embeddings (word representations as numeric
vectors) for further use in downstream tasks such as classification. However, the
word2vec model cannot efficiently handle synonyms and polysemy. The BERT
model solves the above-mentioned problems of the word2vec model [12]. BERT
uses transformers for representation, supplemented by a new masked language
model technology to achieve bidirectional information acquisition, and can be
fine-tuned for application in a wide range of natural language downstream tasks
[12].
2.2 Machine learning in stock market prediction
Traditional machine learning models such as K-Nearest Neighbors (KNN) and
Support Vector Machines (SVM) were applied to stock market prediction. Wuht-
rich et al. [13] used several KNN to classify the stock trends by analyzing financial
newspaper, the best accuracy rate was 53%. In another research [14], SVM was
used by analyzing collected news data from PRNewswire (company-specific press
releases). They showed that the average accuracy rate was 82%. Zhenkun et al.
studied stock market prediction based on Weibo comments’ sentiments using
SVM [15] and reported prediction accuracy of 67%. Zhao et al. [16] investigated
the prediction of financial assets (housing prices, stocks, gold, etc.), created a
financial dictionary for sentiment analysis, and then used this with SVM for
stock market prediction.
Kaastra and Boyd have found that deep learning models can capture rules in
complex financial scenarios [17]. Amongst these, LSTM seems to show a better
ability to deal with long time series data [18]. Zhuge et al. used LSTM as a regres-
sion model to analyze [19] stocks. The experiment used sentiment data collected
from Eastmoney, stock data, and Shanghai Composite Index. This experiment
used mean square error (MSE) for evaluation, the value in this experiment is
in the range from 0.000152 to 0.000513, which suggests that models with sen-
timent analysis can perform better than those only input technical (e.g., price
and volume) stock data. Recently, Jiawei and Murata [20] used word2vec and
LSTM with a set of sentiment data to analyze the movement of the Shanghai
Composite Stock Index. This research achieved an accuracy of 66%.
Our study uses BERT for sentiment analysis combined with LSTM for time
series analysis.
3 Stock market prediction system
Figure 1 describes the structure of our stock market prediction system. First,
a data collection module is used to collect Weibo text data, then the data is

4 Ma, Ziyuan et al.
processed using a data cleaning module. This data is passed to the sentiment
classification module for analysis and finally is used by the LSTM-based regres-
sion module for stock market price prediction. The system is our development,
and the sentiment analyzing module and stock predicting module is developed
based on the existing project [21,22]. The code of the prediction system used in
this work is publicly available (see Introduction section).
Sentiment classification  model
Data cleaning module
Hang Seng
Index Data
Calculate sentiment
value of each day
LSTM stock prediction module
AFA group
data
Time window
choosing
LSTM regression model
Classified
UFA data
AFA group
result
UFA group
result
Data collection module
Group dividing based on weibo authoriza-
tion information
AFA group
data
UFA group
data
UFA group
data
Classified
AFA data
Fig. 1.Stock market prediction system structure
3.1 Data collection module
The data collection module collects raw Weibo data by crawling the Weibo
platform (see Figure 1) and collecting historical stock data from Investing.com 4.
4 https://www.investing.com/

Do Weibo platform experts perform better at predicting stock market? 5
It is a financial news website that includes daily information on the stock markets
of all countries in the world and provides historical data download functions. The
data set collected in this module include:
W eibo data: Weibo text data includes text, the user id, the release time,
the number of comments, the number of reposts, and the number of likes. During
the data collection process, Weibo text messages containing the keyword “Hang
Seng Index” (case-insensitive) in the text field were selected to extract sentiment
tendency towards this index. The time range was set to January 1, 2018 and
going to December 31, 2019. There were 7,169 posts, total, in the AF A group
and 164,760 posts, total, in the UF A group.
Stock data: The stock market data for the Hang Seng Index was downloaded
starting on January 1, 2018 and going to December 31, 2019. Daily data includes
the date, closing price, opening price, highest price, lowest price, total transaction
amount, and the rate of change compared to the previous day.
3.2 Data cleaning module
The data cleaning module cleans the raw data collected by the data collection
module. Specifically, this module includes text clean-up (such as special charac-
ters that cannot be processed are deleted) and duplicate removal.
3.3 Sentiment analysis module
The sentiment analysis module is used to classify the Weibo data. The structure
of this module applied a fully connected layer outside of the BERT model to
process the output sentence vectors from the BERT model, this method is also
suggested in BERT [12] and has been used in existing researches [23,24]. The fully
connected layer’s size is 768 to fit the size of the output vector. The fine-tuning
step used a set of labeled data that was collected from the Weibo platform.
Subsequently, in the training step, the Weibo data is tagged with a sentiment
label used to indicate whether the user’s view of the stock market is positive(1)
(expecting prices to increase) or negative(0) (expecting prices to decrease).
3.4 LSTM stock prediction module
The structure of the stock predicting module uses two layers of LSTM cells, the
structure of the LSTM cell follows the design in [25]. LSTM model can handle
longer time series and is suitable for use in learning scenarios with strong time
dependence such as the stock market [26].
The stock market prediction module has two parts. The first part calculates
the daily average sentiment value for both two user groups. It then calculates
the causal coefficient value based on the daily sentiment value combined with
stock market data based on a time-window sliding value. In this work, T is used
to represent this time-window value.
The second part is used to offset the calculated daily sentiment value ac-
cording to the original date, according to T. The module then converts it into a

6 Ma, Ziyuan et al.
feature and sends it to a two-layer LSTM network, the parameters can be found
in 3.5. In this work, two input features of the LSTM network are historical stock
opening price and daily sentiment value, shifted by the value of T. The output
of this module is a prediction for the opening price for the next day.
3.5 Implementation details
The data collection module is developed based on the Weibo-search [27]: Weibo
platform’s data crawler.
The BERT pre-trained model (its Chinese version) loaded by the module
comes from the official BERT project [28]. This original BERT model used here
includes 110M parameters and 12 layers. The pre-training process was done
by Google, using Wikipedia and BookCorpus data. Fine-tuning dataset of this
model comes from ’weibo senti 100k’ data set in SophonPlus [29] and can be
accessed and downloaded publicly. The SophonPlus is a widely used project
for the Chinese language and already has 3,000 stars on Github (a measure
of a project’s popularity). This data set contains a total of 10,000 Weibo text
comments in the Chinese language that have been tagged with a sentiment label.
The length of each Weibo text is within 140 characters, including the plain text,
emojis, and other special characters. The ratio of positive examples to negative
examples here is 1:1. The BERT hyper-parameters are as follows: batch size is 64,
the learning rate is 2e-5, the epoch is 3, and the warm-up proportion is 0.1. Sun
[30] found that these parameters can lead to a good classification with BERT.
The output size of Bert for each Weibo sentence is 768 and after processed by
the fully connected layer, the vector size reshapes to 2.
The LSTM stock predicting module includes an LSTM time series prediction
layer and a linear regression output layer. In the model, the hidden size is 128,
layer number is 2, the dropout rate is 0.001, and batch size is 64. The input
features are pairs of previous opening price and previous sentiment value. The
output of this module is the predicted opening price of the next day. The data
set includes 602 rows of data from January 2018 to December 2019, 60% of data
is used for training and 40% for testing. Due to this experiment was not looking
to tune hyperparameters and thus validation set was excessive here.
4 Methodology
To explore how AF A users’ predictions on the stock market compare to UF A
users, this study collects comments from these user groups, performs sentiment
analysis on these comments, and uses the two sets of sentiments to predict the
Hang Seng Index separately, calculating their prediction accuracy.
4.1 User grouping method
Liang’s research [31] uses the Naive Bayes method to analyze the Weibo posted
by users, and divides users into celebrities, organizations/media accounts, and

Do Weibo platform experts perform better at predicting stock market? 7
grassroots stars. However, the purpose of grouping in this experiment is not user
attributes, but user experience background, so the method of designing grouping
in this experiment is to access Weibo API and query the public user information.
For an AF A user authentication, a qualification certificate is needed [32]. Thus,
the definition of AF A user in this experiment is that the user’s account is authen-
ticated by Weibo, and the authentication description includes the finance-related
keywords. The users whose “certified” field was TRUE and authentication de-
scription included financial keywords were assigned to the AF A group. The users
whose “certified” field was F ALSE or did not include any financial keyword in
the description field were assigned to the UF A group. As a result, 3,535 users
were assigned to the AF A group and 17,675 to the UF A group.
4.2 Daily sentiment analysis method
In order to compare the predictive ability of users in the AF A group with those in
the UF A group, it is first necessary to fit the relationship between sentiment value
and stock market trends to a LSTM model. For this, a daily sentiment value,
based on each specific user group category was calculated. In the experiment,
the average of sentiment values in a day was used to measure the daily sentiment
value of a user group:
Sentimentd =
Pn
i=1 Labeli
n (1)
In Formula 1, Sentimentd stands for the sentiment value of day d, n means the
number of texts in Weibo for this date, Labeli is the sentiment label value of
a Weibo texti that is found on that date. The higher the sentiment value, the
more positive the general feeling is because, as mentioned earlier, the label for
positive is 1 and for negative is 0.
4.3 Time window calculation method
Zhang et al. [33] claimed that there is a delay between prediction and stock
market movements. The delay to take effect is the T value. The calculation
process is based on the following assumption: the result of sentiment analysis
has a significant correlation with the stock market after it is shifted by T days.
And the final value of T is which that makes the correlation maximum. Zhang et
al. studied the selection of an appropriate T and found the maximal correlation
between prediction and stocks when T was 15.
Likewise in this research, the T value was obtained empirically. Different
time values between 3 to 30 were probed for correlation results. The calculation
results after different T-value offsets are shown in Figure 2.

8 Ma, Ziyuan et al.
Fig. 2.Pearson’s correlation for different T values.
As can be seen from the Figure 2, for both groups, the strongest correlation
occurs when the time window value is 12 (although for the UF A group it is not as
pronounced as for the AF A group). For the AF A group, Pearson’s value reached
above 0.200. For the UF A group, the value peaked at 0.200. Therefore, in this
work, the value was set to 12 for both groups.
4.4 Stock prediction model evaluation metrics
As this is a regression model, the mean square error (MSE) is used to evaluate the
neural network’s performance. To evaluate prediction results, the confusion ma-
trix, which is commonly used to evaluate classification models [34], is calculated.
The definition of F1 score and precision used here can be found in Sammut’s
research [34]. Finally, to compare to other research, accuracy was used, which is
a fraction of all correct predictions (true positives and true negatives) out of all
predictions given.
The predicted results are classified as ’rising or steady’ or ’falling’ based on
the next day’s value. And the actual rise and fall are compared according to the
trend classification results to evaluate whether the prediction is accurate. Then
’rising or steady’ is assumed as a positive sample, and ’falling’ is assumed as a
negative sample. The actual price trend will then be compared to the predicted
price trend.
5 Results
In this regression model, MSE is used for evaluation. For the AF A group, the
MSE was 0.149 and the valid loss was 0.140. For the UF A group, the MSE was
0.076 and the valid loss was 0.211. The results of using two sets of Weibo data
for prediction are shown in Figure 3 (y-axis in the figure shows the opening price
for Hang Seng Index).

Do Weibo platform experts perform better at predicting stock market? 9
Fig. 3.Predict price
From Figure 3 it can be observed that the forecasts of the two groups are
generally in line with the trend of the stock market, to a certain extent.
Then the results of two user groups are filled into the confusion matrix as
shown in Table 1. Because the number of data in the two groups is different, the
totals are not equal.
Result matrix for AF A group Result matrix for UF A group
Predicted positive Predicted negative Predicted positive Predicted negative
Actual positive 119 20 181 115
Actual negative 13 103 99 172
Precision 0.9015 0.6464
F1 score 0.2196 0.1571
T able 1.Resultant confusion matrix and precision for AF A and UF A groups
It can be observed from Table 1 that the prediction precision of the AF A
group is 90.15%. The prediction precision of the UF A group is 64.64%. Therefore,
the prediction precision of the AF A group for the stock market is 39.67% higher
than that of the UF A group. The F1 score that represents the average precision
and recall also shows a better score in the AF A group than the UF A group.
Author Approach Stocks/Index predicted Accuracy (%)
W uhtrich1998 [13] kNN Hang Seng Index 53
Mittermayer 2006 [14] SVM S&P 500 stocks 82
Zhenkun 2016 [15] SVM Shanghai Composite Index 67
Jiawei 2019 [20] word2vec + LSTM Shanghai Composite Index and other 6 stocks 66
This work BER T + LSTM (AF A) Hang Seng Index 87 BER T + LSTM (UF A) Hang Seng Index 62
T able 2.Comparing accuracy of this work to other reported stock prediction ap-
proaches

10 Ma, Ziyuan et al.
When comparing the accuracy of the other existing stock prediction models
(using accuracy results reported in their papers) (see Table 2), the model used
in this work with the AF A group’s sentiment-based prediction demonstrates the
best accuracy results (87%).
6 Threats to validity
In the prediction result, the MSE of the AF A group model is higher than that
of the UF A group’s. This may be due to the difference in the size of the data set
[35]. The data volume of the UF A group is 20 times that of the AF A group, so
the model might learn more to fit the price better than in the case of the AF A
group. Besides, in future work, oversampling to the AF A group can be used for
balancing the scale of two data sets.
In the user grouping method, the authentication is checked by applying
a financial keyword filter, users with authenticated financial keywords will be
grouped into the AF A group, UF A group includes both authenticated with no
financial background and non-authenticated users. Meanwhile, the classification
of users is based on the authentication of Weibo: there may exist users with
professional backgrounds who have not applied for certification, which leads to
inaccurate grouping. Likewise, personal authentication may not be as stringent
as government or enterprise authentication.
Finally, grouping rising and steady prediction results into a single group can
make the comparison to other reported results inaccurate.
7 Conclusions and Future Work
The goal of this work was to study whether there is a difference between financial
professionals (AF A group) and ordinary people (UF A group) on the Weibo social
networking platform in predicting the stock market using a combination of state-
of-the-art sentiment classification BERT and LSTM for stock prediction. In the
study, Weibo was used as the source of sentiment extraction, and the historical
data related to the Hang Seng Index was extracted.
In this study, it was found that the AF A group performs better at predicting
the stock market than the UF A group: the precision of the AF A group is 39.67%
higher than that of the UF A group’s. Hence, it seems that AF A posts are a
much stronger foundation on which to base market predictions. The further
filtering of authorization to enterprise and government-level authorization may
further impact these strength-of-authorization findings and in future work, we
will refine our analysis accordingly. Of course, the context of these findings should
also be considered, where advisors with government authorization in a Chinese
context may be considered to have heightened authority and thus may serve to
make those posts have a self-fulfilling prophecy. This may have impacted our
findings. and so, all three categories (personal, enterprise, and government) will
be considered in isolation in our future work.

Do Weibo platform experts perform better at predicting stock market? 11
Acknowledgement
This work was supported with the financial support of the Science Foundation
Ireland grant 13/RC/2094 2.
References
1. K. R. French, G. W. Schwert, and R. F. Stambaugh, “Expected stock returns and
volatility,” Journal of Financial Economics , vol. 19, no. 1, pp. 3–29, 1987.
2. Y. Xu, Z. Liu, J. Zhao, and C. Su, “Weibo sentiments and stock return: A
time-frequency view,” PLOS ONE , vol. 12, no. 7, pp. 1–21, 07 2017. [Online].
Available: https://doi.org/10.1371/journal.pone.0180723
3. T. O. Sprenger, A. Tumasjan, P. G. Sandner, and I. M. Welpe, “Tweets and trades:
The information content of stock microblogs,” European Financial Management ,
vol. 20, no. 5, pp. 926–957, 2014.
4. J. Bollen, H. Mao, and X. Zeng, “Twitter mood predicts the stock market,”Journal
of computational science , vol. 2, no. 1, pp. 1–8, 2011.
5. A. Mittal and A. Goel, “Stock prediction using twitter sentiment analysis,” Stand-
ford University, CS229 (2011 http://cs229. stanford. edu/proj2011/GoelMittal-
StockMarketPredictionUsingTwitterSentimentAnalysis. pdf ), vol. 15, 2012.
6. G. W. Brown and M. T. Cliff, “Investor sentiment and the near-term stock market,”
Journal of empirical finance , vol. 11, no. 1, pp. 1–27, 2004.
7. X. Chu, C. Wu, and J. Qiu, “A nonlinear granger causality test between stock re-
turns and investor sentiment for chinese stock market: a wavelet-based approach,”
Applied Economics, vol. 48, no. 21, pp. 1915–1924, 2016.
8. X. Jin, D. Shen, and W. Zhang, “Has microblogging changed stock market behav-
ior? evidence from china,” Physica A: Statistical Mechanics and its Applications ,
vol. 452, pp. 151–156, 2016.
9. H. Peng, E. Cambria, and A. Hussain, “A review of sentiment analysis research in
chinese language,” Cognitive Computation, vol. 9, no. 4, pp. 423–435, 2017.
10. Y. Rao, J. Lei, L. Wenyin, Q. Li, and M. Chen, “Building emotional dictionary for
sentiment analysis of online news,” World Wide Web , vol. 17, no. 4, pp. 723–742,
2014.
11. T. Mikolov, K. Chen, G. S. Corrado, and J. Dean, “Efficient estimation of word
representations in vector space,” 2013.
12. J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of
deep bidirectional transformers for language understanding,” arXiv preprint
arXiv:1810.04805, 2018.
13. B. Wuthrich, V. Cho, S. Leung, D. Permunetilleke, K. Sankaran, and J. Zhang,
“Daily stock market forecast from textual web data,” vol. 3, 11 1998, pp. 2720 –
2725 vol.3.
14. M. A. Mittermayer and G. Knolmayer, “Newscats: A news categorization and
trading system,” pp. 1002–1007, 2006.
15. Z. Zhou, J. Zhao, and K. Xu, “Can online emotions predict the stock market
in china?” in International conference on web information systems engineering .
Springer, 2016, pp. 328–342.
16. W. Zhao, F. Wu, Z. Fu, Z. Wang, and X. Zhang, “Sentiment analysis on weibo plat-
form for stock prediction,” in International Conference on Artificial Intelligence
and Security. Springer, 2020, pp. 323–333.

12 Ma, Ziyuan et al.
17. I. Kaastra and M. Boyd, “Designing a neural network for forecasting financial and
economic time series,” Neurocomputing, vol. 10, no. 3, pp. 215 – 236, 1996, financial
Applications, Part II.
18. S. Hochreiter and J. Schmidhuber, “Lstm can solve hard long time lag problems,”
in Advances in neural information processing systems , 1997, pp. 473–479.
19. Q. Zhuge, L. Xu, and G. Zhang, “Lstm neural network with emotional analysis for
prediction of stock price.” Engineering letters, vol. 25, no. 2, 2017.
20. X. Jiawei and T. Murata, “Stock market trend prediction with sentiment analysis
based on lstm neural network,” inProceedings of the International MultiConference
of Engineers and Computer Scientists , 2019, pp. 13–15.
21. Tracy-Talent, “tracy-talent/curriculum.” [Online]. Available: https://github.com/
tracy-talent/curriculum/tree/master/DataMining/sentiment
22. rguthrie3, “rguthrie3/deeplearningfornlpinpytorch.” [Online]. Available: https:
//github.com/rguthrie3/DeepLearningForNLPInPytorch
23. A. Karimi, L. Rossi, A. Prati, and K. Full, “Adversarial training for aspect-based
sentiment analysis with bert,” arXiv preprint arXiv:2001.11316 , 2020.
24. P.-H. Chi, P.-H. Chung, T.-H. Wu, C.-C. Hsieh, Y.-H. Chen, S.-W. Li, and H.-y.
Lee, “Audio albert: A lite bert for self-supervised learning of audio representation,”
in 2021 IEEE Spoken Language Technology Workshop (SLT) . IEEE, 2021, pp.
344–350.
25. F. A. Gers, J. Schmidhuber, and F. Cummins, “Learning to forget: Continual
prediction with lstm,” 1999.
26. K. Chen, Y. Zhou, and F. Dai, “A lstm-based method for stock returns prediction:
A case study of china stock market,” in 2015 IEEE international conference on big
data (big data) . IEEE, 2015, pp. 2823–2824.
27. Dataabc, “dataabc/weibo-search.” [Online]. Available: https://github.com/
dataabc/weibo-search
28. Google-Research, “google-research/bert.” [Online]. Available: https://github.com/
google-research/bert
29. SophonPlus, “Sophonplus/chinesenlpcorpus.” [Online]. Available: https://github.
com/SophonPlus/ChineseNlpCorpus/tree/master/datasets/
30. C. Sun, X. Qiu, Y. Xu, and X. Huang, “How to fine-tune bert for text classi-
fication?” in China National Conference on Chinese Computational Linguistics .
Springer, 2019, pp. 194–206.
31. L. Guo, W. Wang, S. Cheng, and X. Que, “Event-based user classification in weibo
media,” The Scientific World Journal , vol. 2014, 2014.
32. W. platform, “Weibo customer service.” [Online]. Available: https://kefu.weibo.
com/faqdetail?id=20831
33. Kaihui Zhang, Lei Li, Peng Li, and Wenda Teng, “Stock trend forecasting method
based on sentiment analysis and system similarity model,” in Proceedings of 2011
6th International Forum on Strategic Technology , vol. 2, 2011, pp. 890–894.
34. C. Sammut and G. I. Webb, Encyclopedia of machine learning and data mining .
Springer, 2017.
35. T. Linjordet and K. Balog, “Impact of training dataset size on neural answer
selection models,” in European Conference on Information Retrieval . Springer,
2019, pp. 828–835.
