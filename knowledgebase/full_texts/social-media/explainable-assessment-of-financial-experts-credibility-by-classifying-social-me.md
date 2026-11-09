---
title: Explainable assessment of financial experts' credibility by classifying social media forecasts
  and checking the predictions with actual market data
url: https://arxiv.org/abs/2406.11924
category: social-media
subcategory: empirical
date: 2024-06
venue: ''
authors:
- Silvia García-Méndez
- Francisco de Arriba-Pérez
- Jaime González-Gonzáleza
- Francisco J. González-Castaño
source: arxiv
pdf_url: https://arxiv.org/pdf/2406.11924
pages: 31
chars: 53331
fetched_at: '2026-11-08T13:05:53+00:00'
kb_version: 1
---

# Explainable assessment of financial experts' credibility by classifying social media forecasts and checking the predictions with actual market data

Explainable assessment of financial experts’ credibility
by classifying social media forecasts and checking the
predictions with actual market data
Silvia Garc ´ ıa-M´ endeza,∗, Francisco de Arriba-P´ ereza, Jaime
Gonz´ alez-Gonz´ aleza, Francisco J. Gonz´ alez-Casta˜ noa
aInformation Technologies Group, atlanTTic, University of Vigo, Vigo, Spain
Abstract
Social media include diverse interaction metrics related to user popularity,
the most evident example being the number of user followers. The latter
has raised concerns about the credibility of the posts by the most popular
creators. However, most existing approaches to assess credibility in social
media strictly consider this problem a binary classification, often based on a
priori information, without checking if actual real-world facts back the users’
comments. In addition, they do not provide automatic explanations of their
predictions to foster their trustworthiness. In this work, we propose a credi-
bility assessment solution for financial creators in social media that combines
Natural Language Processing and Machine Learning. The reputation of the
contributors is assessed by automatically classifying their forecasts on asset
values by type and verifying these predictions with actual market data to
approximate their probability of success. The outcome of this verification
is a continuous credibility score instead of a binary result, an entirely novel
contribution by this work. Moreover, social media metrics (i.e., user context)
are exploited by calculating their correlation with the credibility rankings,
providing insights on the interest of the end-users in financial posts and their
forecasts ( i.e., drop or rise). Finally, the system provides natural language
explanations of its decisions based on a model-agnostic analysis of relevant
∗Corresponding author: sgarcia@gti.uvigo.es
Email addresses: sgarcia@git.uvigo.es (Silvia Garc ´ ıa-M´ endez),
farriba@gti.uvigo.es (Francisco de Arriba-P´ erez),jaimegonzalez@gti.uvigo.es
(Jaime Gonz´ alez-Gonz´ alez),javier@det.uvigo.es (Francisco J. Gonz´ alez-Casta˜ no)
Preprint submitted to Expert Systems with Applications June 19, 2024
arXiv:2406.11924v1  [cs.SI]  17 Jun 2024

features.
Keywords: Artificial Intelligence, explainability, financial user credibility,
Machine Learning, Natural Language Processing
1. Introduction
Data credibility depends on the information source (e.g., humans or bots),
the content, and its context (e.g., user relations, content domain, etc.). This
problem has gained renewed attention owing to the popularity of social me-
dia (Kaliyar et al., 2021; Nian et al., 2021) and their anonymity and ef-
fortless fast information-sharing features (Huang et al., 2021). Social media
posts and user profiles are valuable input data to assess creators’ credibil-
ity for decision-making (Kurniati & Widyantoro, 2017). For example, iden-
tifying reliable and trustworthy creators is crucial to fight disinformation
from fake news ( i.e., deliberate disinformation) (Kozik et al., 2022; Verma
et al., 2022). Nevertheless, social media platforms lack, in general, appropri-
ate mechanisms to distinguish valuable from useless data (Kamkarhaghighi
et al., 2016; Hanaforoosh et al., 2021), hence the interest in these mechanisms
(Huang et al., 2021; Jing et al., 2021).
Most existing research on user credibility has focused on analyzing shared
content, rather than considering the context of the creators and their pro-
files (Asfand-E-Yar et al., 2023; Li et al., 2023). We can identify different
approaches: ( i ) graph-based (i.e., measuring the users’ credibility from other
directly or indirectly connected users) (Qureshi et al., 2021), ( ii ) those per-
forming Sentiment Analysis ( sa) of the content (Kurniati & Widyantoro,
2017), and ( iii ) solutions with domain-dependent features (Huang et al.,
2019). Additional features related to the users’ profiles ( i.e., the number
of followers) and their demographic data ( e.g., age) have been identified as
helpful (Verma et al., 2022). As an example of a complete approach combin-
ing diverse strategies, the recent work by Li et al. (2023) describes a Machine
Learning (ml) based assessment tool of Twitter profiles applyingsa, content-
based features and user-context features. It is also interesting to observe that
most current solutions for credibility analysis tend to approach the problem
as a strictly binary classification task, instead of producing continuous rank-
ings (Zhou et al., 2017).
Moreover, eXplainable Artificial Intelligence ( xai) techniques are scarce
in the literature on the target problem. These techniques take advantage
2

of the intrinsically interpretable nature of some ml models, or are ad hoc
solutions to circumvent the opacity of black-box algorithms (Jung et al.,
2022; Akbar et al., 2023). They help professionals and end-users better un-
derstand the decisions of the ml models to foster their trustworthiness. The
most popular xai approaches are (i ) counterfactual descriptions (Chen et al.,
2023), ( ii ) feature importance (Huang et al., 2021), ( iii ) natural language
explanations (Cambria et al., 2023), and (iv ) visual dashboards (Batic et al.,
2024).
Summing up, our work focuses on the financial domain, owing to the many
credibility concerns about stock market forecasts (Huang et al., 2019). It
contributes to the investors’ well-informed decision-making through reliable
and updated information from social media (Evans et al., 2021). Specifically,
we classify financial posts in forecast categories and automatically verify if
actual market events back these predictions to measure the level of success
of the users. This success percentage is presented as a continuous credibility
score instead of a binary result. Additionally, user context is exploited by
comparing credibility scores with social media user metrics, providing insights
related to the user interests about the forecasts in financial posts. Finally,
the model predictions are automatically explained in natural language.
The rest of this paper is organized as follows. Section 2 reviews the rele-
vant works on user credibility assessment. Section 3 introduces the proposed
solution. Section 4 describes the experimental data set, the implementations,
and the results obtained. Finally, Section 5 highlights the contributions and
proposes future research.
2. Related work
2.1. Social media and ml for credibility assessment
Since the information in social media may come from untrustworthy users,
filtering advertisements, scams, and spam from credible data is crucial in
professional domains (Huang et al., 2019).
There exists plenty of prior work on social media credibility assessment
(Huang et al., 2019), covering domains such as business (Abdullah et al.,
2021; Al-Yazidi et al., 2022), disaster scenarios (Assery et al., 2022), news
(Pelau et al., 2023; Shrestha et al., 2024), politics (Page & Duffy, 2018) and
finance (Evans et al., 2021).
Two typical limitations of current works on credibility assessment are that
(i ) they often approach the problem as a binary classification in which user
3

credibility is not ranked as a continuous variable; and (ii ) they do not provide
explanations on their predictions. Also, many works ignore the user’s context
and focus on the content. The latter is not the case, for example, in the
work by Prada & Iglesias (2020), who presented a user reputation prediction
solution for Wallapop based on generalized linear models (glms) (parametric
models that are more straightforward than non-parametric traditional ml
algorithms). The features included elementary linguistic ones, the bad word
ratio, and the user’s Twitter profile data.
Earlier works by Zhou et al. (2017); Abu-Salih et al. (2019) assessed
the credibility of diverse sources based on rules. The analysis by Alrubaian
et al. (2017) relied on the relations in a network of reputable individuals to
detect and prevent malicious events in social networks. Bukhari et al. (2017)
classified tweets into high- and low-impact ones by analyzing their content
with sa. They also predicted the users’ areas of expertise by considering
some user-context features.
2.2. Social media and ml for financial credibility assessment
In the financial domain, we should mention the work by Kamkarhaghighi
et al. (2016), which measured credibility from the number of seed tweets of
a user, the number of stock market-oriented followers identified with $cash-
tags, and the ratio between these and other followers. Conversely, Huang
et al. (2019) calculated trust scores based on PageRank ( pr) and Hyperlink-
Induced Topic Search ( hits) models to identify credible data in financial
tweets. A list of credible users was extracted from prestigious independent
financial authorities. Four trust filters were proposed: experience, expertise,
authority, and reputation. The first two considered the user posting fre-
quency, while the others were based on the user’s social network structure,
favoring well-connected users. Then, the authors applied sa to the tweet
content. Evans et al. (2021) followed a supervised classification approach
trained with metadata from the content and the user context, obtaining the
best results with tree-based models. They employed counters of Bag of Words
(bow), Part of Speech ( pos) tags, and urls. Moreover, Huang et al. (2021)
proposed a solution to identify credible Twitter users based on trustworthy
experts. As Kamkarhaghighi et al. (2016), they filtered finance-oriented users
with $cashtags and took financial experts from well-known sources. Then,
they trained an ml model with content-oriented and user context features.
Interpretability was provided by checking the importance of the features of
a Random Forest (rf) classifier.
4

2.3. Contribution
In light of the comparison with competing solutions in Table 1, our work
is the first that ( i ) assesses user credibility from social media financial posts
that are automatically classified into types of forecasts and then validated
with actual market data, ( ii ) provides a credibility ranking as a continuous
scale, (iii ) analyzes the correlations between this credibility ranking and di-
verse user context metrics to gain insights on the interest of the audience
in financial posts, and ( iv ) describes the model predictions with natural lan-
guage explainability techniques. Our solution has been validated using finan-
cial posts, and unlike other xai-based systems in the literature, it exploits
the relevance of the features to create natural language descriptions. Even
though the training process is time-consuming compared to rule-based ap-
proaches presented by Kamkarhaghighi et al. (2016) and Huang et al. (2021),
and the approach based on pr and hits by Huang et al. (2019), the predic-
tion is performed in real-time. In contrast to Evans et al. (2021) and Huang
et al. (2021), it offers a credibility ranking on a continuous scale.
Table 1: Comparison of financial user credibility solutions considering the approach, type
of features used (content and user context), and availability of continuous-scale ranking
(Rank), real-world validation (Val.), and explainability (Ex.)—including feature relevance
(fr) and natural language ( nl).
Authorship Social Approach F eatures Rank V al. Ex.
media
Kamkarhaghighi et al. (2016) Twitter Rules User ✓ ✗ ✗ml
Huang et al. (2019) Twitter pr, hits Content ✓ ✗ ✗User
Evans et al. (2021) Twitter ml Content ✗ ✗ ✗User
Huang et al. (2021) Twitter Rules Content ✗ ✗ frml User
Proposed solution Twitter ml Content User ✓ ✓ fr Yahoo nl
5

3. Methodology
Figure 1 shows the scheme of the proposed solution for the credibility
assessment of finance-oriented users. Firstly, the pre-processing module pre-
pares the textual content. Then, the feature engineering module generates
n-grams and side features. The hybrid classification module automatically
classifies posts in types of forecasts with term detectors and ml algorithms.
Prediction quality is ranked by the quality assessment module and described
by the explainability module.
3.1. Pre-processing module
Prior to feature extraction is essential to remove meaningless data to
ensure optimal knowledge extraction from the textual content. Regular ex-
pressions are applied to remove links to external sources (e.g., journals, blogs,
etc.) and images. Stop words and special characters ( e.g., currency symbols,
percentage symbols, etc.) and emoticons are discarded. Finally, the remain-
ing textual content is lemmatized.
3.2. Feature engineering module
Regarding content-based features, we focus on stylistic data such as read-
ability score, reading time, and the number of complex words in the post.
Emotion and polarity data are also considered. Textual features are obtained
as char and word n-grams. Table 2 details the features engineered. Some
require ad hoc processing, as explained in Section 4.3.
3.3. Classification module
The hybrid classification module combines categorization based on term
detection and ml prediction. As forecast categories, we consider short-term
drops, short-term rises, and ‘other,’ a third category for any other post men-
tioning stock values. As for the short-term time range, we consider up to four
weeks. For term-based detection, a term lexicon is defined for each target
category. The system considers that a post belongs to a specific category if it
contains at least one term in the corresponding lexicon 1, generated in prac-
tice as described in Section 4.4. This prior term-based detection increases
the system’s efficiency, leaving the remaining posts to be classified using su-
pervised ml models trained with the features detailed in Section 3.2. The ml
1These lexica are composed of unique terms.
6

Figure 1: System scheme.
7

Table 2: Features engineered by data type.
Type ID Name Description
Boolean 1 Emotion
Indicates if the content expresses
anger, fear, happiness, sadness, or
surprise.
Numerical
2 Complex word counter Number of complex words in the content.
3 fre
Flesch reading ease score to assess
readability based on the number of
words and the number of syllables
per word.
4 Hashtag counter Number of hashtags in the content.
5 mer
McAlpine eflaw Readability score
considering the number of words and
mini-words (up to 3 characters) and
the number of sentences.
6 Neg. num. Amount of negative numerical val- ues referring to a stock or market.
7 Neg. per. Amount of negative percentages.
8 Polarity
Indicates the sentiment of the con-
tent, negative (-1), neutral (0), or
positive (+1).
9 pos distributions
Percentages of adjectives, adverbs,
auxiliary elements, determiners,
nouns, pronouns, and punctuation
marks.
10 Pos. num. Amount of positive numerical values referring to a stock or market.
11 Pos. per. Amount of positive percentages.
12 Reading time Estimated time needed to read the content, 14.69 ms per character.
13 Word count Number of words in the content.
Textual
14 Char-grams List of char n-grams in the content.
15 Word-grams List of word n-grams in the content.
16 Word tokens List of char n-grams only from text inside word boundaries.
8

algorithms selected, based on their satisfactory performance in the literature
(Huang et al., 2021; Ryans, 2021; Alzanin et al., 2022; Gonz´ alez-Gonz´ alez
et al., 2022; Hudon et al., 2022; Jalal et al., 2022; Raheja & Asthana, 2022;
Bengesi et al., 2023; Darad & Krishnan, 2023), are (i) Linear Support Vector
Machines (lsvm), (ii ) Decision Trees (dt), (iii ) k-Nearest Neighbors (knn),
(iv ) Naive Bayes (nb), (v ) Random Forest (rf), and (vi ) Gradient Boosting
(gb).
3.4. Quality assessment module
This module computes the quality of the predictions according to the cat-
egory they were classified into. It compares the predicted forecast with the
actual evolution of the stock values, identified with $cashtags and financial
tickers. The final quality rank depends on the number of successful predic-
tions. Only posts mentioning stocks or markets are considered for quality
evaluation.
3.5. Explainability module
In order to foster the trustworthiness of the automatic analysis, this mod-
ule presents explanations in natural language based on relevant terms or fea-
tures. In the case of posts directly classified by term-based detection, the
corresponding terms are included in the explanations. The system employs
a model-agnostic approach for posts classified by the ml models to extract
all the relevant features as explained in Section 4.6. The explanations are
presented in natural language using templates. Finally, Figure 2 shows the
block diagram of the system from the pre-processing stage to the final quality
assessment.
Figure 2: System’s block diagram.
9

4. Evaluation and discussion
This section presents the experimental data set, the implementations of
the modules, and the results obtained. The experiments were performed on
a computer with the following specifications:
• Operating System . Ubuntu 20.04.3 lts 64 bits
• Processor. amd® Ryzen 7 3800X 3.9 GHz
• RAM. 32 gb ddr4
• Disk. 1 tb ssd
4.1. Experimental data set
The experimental data set contains 15 000 tweets published by 12 Spanish
trading advisors (1000 posts per advisor) between January 16, 2017, and
June 5, 2023. Following a prior screening using ChatGPT, these posts were
manually annotated by financial experts into three categories: ( i ) short-
term drop, (ii ) short-term rise, and ( iii ) other, as previously described. The
profiles of the creators were selected to ensure diversity in Twitter statistics
(e.g., number of followers, posts per day, etc.). Table 3 shows the distribution
of the samples in the experimental data set by category and advisor, while
Table 4 details the global distribution of samples by category.
4.2. Pre-processing module
$cashtags, images, links, and special characters were identified using the
regular expressions in Listing 1.
LISTING 1: Regular expressions applied to detect $cashtags, images, links, and special
characters.
$casthtags = r ’ \ $ [ a−zA−Z0 −9=][ a−zA−Z ] [ a−zA−Z0−9=]+’
r ’ \ ˆ [ a−zA−Z0 −9=][ a−zA−Z ] [ a−zA−Z0−9=]+’
Images/links = r ” ( ? : ( p i c .| h t t p|www| \w+ ) ?\ : ( / / )∗ ) \ S+”
Special char. = r ” ( \ ∗ | \[ | \] | = | \( | \) | \$ | \” | \ } | \ { | \ | | \+ | & | € | £ | / | °)+”
Other financial tickers not expressed in $cashtag format (i.e., lacking the
“$” symbol or written as hashtags) were detected using regular expressions
10

Table 3: Distribution of the samples by advisor and category.
Ad. Short-term drop (%) Short-term rise (%) Other (%)
1 3.55 31.81 64.64
2 17.64 42.89 39.48
3 10.26 27.97 61.77
4 13.81 26.23 59.96
5 9.70 39.19 51.11
6 5.00 77.70 17.30
7 16.35 29.49 54.16
8 5.94 30.38 63.68
9 10.09 23.41 66.50
10 7.34 34.31 58.35
11 35.43 27.02 37.55
12 11.42 23.75 64.83
Table 4: Global distribution of samples by category.
Category % samples
Short-term drop 12.20
Short-term rise 34.53
Other 53.26
11

combined with dictionaries from the main American 2 and European 3 stock
markets. Moreover, stop words were removed using the Spanish nltk stop
word list 4 while Emoticons by applying the nfkd Unicode normalization
form5. Finally, posts were lemmatized using the es core news md core model
of the spaCy Python library6.
4.3. Feature engineering module
Emotion and polarity (features 1 and 8 in Table 2) were calculated with
the text2emotion7 and textblob tools8 from the spaCy Python library,
respectively.
Stylistic features related to complex word count (feature 2), Flesch read-
ing ease (feature 3), McAlpine eflaw Readability (feature 5), and reading
time (feature 12) were obtained with the textstat9 Python library.
The distribution of pos tags in the posts (feature 9) was computed using
the textdescriptives10 Python library.
To compute the textual features, that is, char and wordn-grams and word
tokens (features 14, 15, and 16), the system employs the CountVectorizer
function11 from the scikit-learn Python library. Listings 2-4 shows the op-
timal parameters in bold. Even though the ranges provided were established
based on preliminary coarse experiments, the best values were identified us-
ing the GridSearchCV12 function from the scikit-learn Python library, as
commonly used in the literature (Evans et al., 2021).
The rest of the features in Table 2 were computed using regular expres-
sions or standard procedures in Python, as in the case of the hashtag counter
2Available at https://www.sec.gov/file/company-tickers, June 2024.
3Available at https://www.cboe.com/europe/equities/market_statistics/
symbols_traded, June 2024.
4Available at https://www.nltk.org, June 2024.
5Available at https://unicode.org/reports/tr15, June 2024.
6Available at https://spacy.io/models/es, June 2024.
7Available at https://pypi.org/project/text2emotion, June 2024.
8Available at https://spacy.io/universe/project/spacy-textblob, June 2024.
9Available at https://pypi.org/project/textstat, June 2024.
10Available at https://pypi.org/project/textdescriptives, June 2024.
11Available at https://scikit-learn.org/stable/modules/generated/sklearn.
feature_extraction.text.CountVectorizer.html, June 2024.
12Available at https://scikit-learn.org/stable/modules/generated/sklearn.
model_selection.GridSearchCV.html, June 2024.
12

(feature 4 13), and the negative and positive number counters (features 6, 7,
10 and 11 14). After content tokenization, feature 13 is engineered using the
Python len function.
LISTING 2: Parameter selection for char-grams (best values in bold).
max df = [ 0 . 1 , 0 . 1 2 , 0 . 1 4 , 0 . 1 6 , 0 . 1 8 , 0 . 2 , 0 . 2 2 , 0 . 2 4 , 0 . 2 6 ,
0 . 2 8 , 0 . 3 , 0 . 3 2 , 0 . 3 4 , 0 . 3 6 , 0 . 3 8 , 0.4 ] ,
m i n d f = [ 0 . 0 1 , 0 . 0 2 , 0.03 , 0 . 0 4 , 0 . 0 5 ] ,
ngram range = [ (3, 4), ( 3 , 5 ) , ( 3 , 6 ) , ( 3 , 7 ) , ( 4 , 5 ) , ( 4 , 6 ) ,
( 5 , 6 ) ] ,
m a x f e a t u r e s = [ 1 0 0 , 1 0 0 0 ,None ]
LISTING 3: Parameter selection for word-grams (best values in bold).
max df = [ 0 . 1 7 , 0 . 2 0 , 0.23 , 0 . 2 6 , 0 . 2 9 , 0 . 3 2 , 0 . 3 5 , 0 . 3 8 , 0 . 4 1 ,
0 . 4 4 , 0 . 4 7 , 0 . 5 ] ,
m i n d f = [ 0.01 , 0 . 0 2 , 0 . 0 3 , 0 . 0 4 , 0 . 0 5 ] ,
ngram range = [ (1, 1), ( 1 , 2 ) , ( 1 , 3 ) , ( 2 , 2 ) , ( 2 , 3 ) ] ,
m a x f e a t u r e s = [ 1 0 0 , 1 0 0 0 ,None ]
LISTING 4: Parameter selection for word tokens (best values in bold).
max df = [ 0 . 1 7 , 0 . 2 0 , 0 . 2 3 , 0.26 , 0 . 2 9 , 0 . 3 2 , 0 . 3 5 , 0 . 3 8 , 0 . 4 1 ,
0 . 4 4 , 0 . 4 7 , 0 . 5 ] ,
m i n d f = [ 0 . 0 1 , 0.02 , 0 . 0 3 , 0 . 0 4 , 0 . 0 5 ] ,
ngram range = [ ( 3 , 4 ) , (3, 5), ( 3 , 6 ) , ( 3 , 7 ) , ( 4 , 5 ) , ( 4 , 6 ) ,
( 5 , 6 ) ] ,
m a x f e a t u r e s = [ 1 0 0 , 1 0 0 0 ,None ]
4.4. Classification module
The representative terms for each category lexicon were created using
CountVectorizer11. For each category, we selected the 10 % most frequent
unique terms ( i.e., those which only appear in posts of a given category).
If one post contained at least one term from the list of a category, it was
assigned to that category. For the rest of the posts, the implementations for
ml classification algorithms used were:
13r’#[a-zA-Z0-9]+’$.
14r’-?[0-9.,]+[$€%]’.
13

• lsvm. LinearSVC implementation15 from the scikit-learn Python
library.
• dt. DecisionTreeClassifier algorithm 16 from the scikit-learn
Python library.
• knn. KNeighborsClassifier implementation17 from the scikit-learn
Python library.
• nb. Two configurations, Complement Naive Bayes ( cnb) and Multi-
nomial Naive Bayes ( mnb). The corresponding implementations were
ComplementNB18 and MultinomialNB19, both from the scikit-learn
Python library.
• rf. RandomForestClassifier function20 from the scikit-learn Python
library.
• gb. GradientBoosting Classifierfunction21 from the scikit-learn
Python library.
We estimated the optimal hyperparameters22 for these models using Grid
SearchCV12, similarly to the feature engineering module. Listings 5-11 con-
tain the ranges of values tested. In the case of knn, the only valid setting for
the metric parameter was Minkowski, as the input matrix was not square.
15Available at https://scikit-learn.org/stable/modules/generated/sklearn.
svm.LinearSVC.html, June 2024.
16Available at https://scikit-learn.org/stable/modules/generated/sklearn.
tree.DecisionTreeClassifier.html, June 2024.
17Available at https://scikit-learn.org/stable/modules/generated/sklearn.
neighbors.KNeighborsClassifier.html, June 2024.
18Available at https://scikit-learn.org/stable/modules/generated/sklearn.
naive_bayes.ComplementNB.html, June 2024.
19Available at https://scikit-learn.org/stable/modules/generated/sklearn.
naive_bayes.MultinomialNB.html, June 2024.
20Available at https://scikit-learn.org/stable/modules/generated/sklearn.
ensemble.RandomForestClassifier.html, June 2024.
21Available at https://scikit-learn.org/stable/modules/generated/sklearn.
ensemble.GradientBoostingClassifier.html, June 2024.
22Note that we refer to parameters when generating features, while hyperparameters
are those applied in ml models.
14

Term-based detection allowed predicting 62 .99 % of the samples in the
experimental data set, considerably saving computing resources and time.
For the subsequent evaluation with ml classification algorithms, we ap-
plied 10-fold cross-validation (Aoumeur et al., 2023), implemented using the
StratifiedKFold23 function from the scikit-learn Python library.
LISTING 5: Hyperparameter selection for lsvm (best values in bold).
c l a s s w e i g h t = [ None , b a l a n c e d ] ,
l o s s = [ hinge , s q u a r e d h i n g e ] ,
m a x i t e r = [ 5 0 0 , 1000 , 2 0 0 0 ] ,
m u l t i c l a s s = [ ovr ] ,
t o l = [ 0 . 0 0 0 0 0 1 , 0 . 0 0 0 0 1 , 0 . 0 0 0 1 , 0 . 0 0 1 ,0.01 ] ,
p e n a l t y = [l2 ] ,
d u a l = [ T rue] ,
C = [ 0 . 0 0 0 1 , 0 . 0 0 1 , 0 . 0 1 , 0.1 , 1 , 1 0 ]
LISTING 6: Hyperparameter selection for dt (best values in bold).
c r i t e r i o n = [ gini , e n t r o p y ] ,
s p l i t t e r = [ best , random ] ,
c l a s s w e i g h t = [ None , b a l a n c e d ] ,
m a x f e a t u r e s = [ None , sqrt , l o g 2 ] ,
max depth = [ 5 , 1 0 , 5 0 , 100 ] ,
m i n s a m p l e ss p l i t = [ 0 . 0 0 0 1 , 0 . 0 0 1 , 0.01 , 0 . 1 , 1 ] ,
m i n s a m p l e sl e a f = [ 0 . 0 0 0 1 , 0 . 0 0 1 , 0 . 0 1 , 0 . 1 , 1 ]
LISTING 7: Hyperparameter selection for knn (best values in bold).
n n e i g h b o r s = [ 5 , 10 , 2 5 ] ,
w e i g h t s = [ uniform , distance ] ,
a l g o r i t h m = [ auto , b a l l t r e e , kd tree , b r u t e ] ,
l e a f s i z e = [ 5 , 10 , 1 5 , 2 5 , 3 0 , 5 0 ] ,
p = [ 1 , 2 ] ,
m e t r i c = [ minkowski ]
LISTING 8: Hyperparameter selection for cnb (best values in bold).
a l p h a = [ 0 , 0.25 , 0 . 5 , 0 . 7 5 , 1 ] ,
f i t p r i o r = [ T rue, F a l s e ] ,
norm = [ True , F alse]
23Available at https://scikit-learn.org/stable/modules/generated/sklearn.
feature_selection.SelectPercentile.html, June 2024.
15

LISTING 9: Hyperparameter selection for mnb (best values in bold).
a l p h a = [ 0 , 0.25 , 0 . 5 , 0 . 7 5 , 1 ] ,
f i t p r i o r = [ T rue, F a l s e ]
LISTING 10: Hyperparameter selection for rf (best values in bold).
n e s t i m a t o r s = [ 5 0 , 1 0 0 ,250 , 5 0 0 , 1 0 0 0 ] ,
c r i t e r i o n = [ gini , e n t r o p y ] ,
c l a s s w e i g h t = [ None , b a l a n c e d ] ,
m a x f e a t u r e s = [ None , sqrt , l o g 2 ] ,
max depth = [ 5 , 1 0 , 50 , 1 0 0 ] ,
m i n s a m p l e ss p l i t = [ 0 . 0 0 0 1 , 0.001 , 0 . 0 1 , 0 . 1 , 1 ] ,
m i n s a m p l e sl e a f = [ 0.0001 , 0 . 0 0 1 , 0 . 0 1 , 0 . 1 , 1 ]
LISTING 11: Hyperparameter selection for gb (best values in bold).
l e a r n i n gr a t e = [ 0 . 0 0 1 , 0 . 0 1 , 0 . 1 , 1 ] ,
n e s t i m a t o r s = [ 1 0 , 1 0 0 ,1000 ] ,
max depth = [ 5 , 1 0 0 , 100 , 1 0 0 0 ] ,
m i n s a m p l e ss p l i t = [ 0 . 0 0 0 1 , 0 . 0 0 1 , 0 . 0 1 , 0 . 1 , 1 ] ,
m i n s a m p l e sl e a f = [ 0 . 0 0 0 1 , 0 . 0 0 1 , 0 . 0 1 , 0 . 1 , 1 ] ,
m a x f e a t u r e s = [sqrt , None ] ,
subsample = [ 0 . 1 , 0 . 5 , 1 ] ,
t o l = [ 0 . 0 0 0 0 0 1 , 0 . 0 0 0 0 1 , 0 . 0 0 0 1 ,0.001 ] ,
Table 5 shows the combined results of term-based and ml classifications.
The best values for each measurement are expressed in bold. Note that the
best model varies depending on the metric analyzed (i.e., precision, recall,
and F -measure) and the target category (i.e., drop and rise). In the particu-
lar application of this work, it is necessary to maximize precision by assuming
that the quality assessment module receives enough correctly predicted sam-
ples.
In light of the results obtained, we can conclude that the most promising
models are knn, mnb, rf, and gb with the best values superior to 80 % for all
metrics. However, other aspects must also be considered, such as computing
time. In this regard, knn and gb are highly demanding. Lastly, taking into
account the interpretable nature of the rf model in favor of explainability,
it was selected. On the other hand, Table 6 shows the performance of the
final hybrid classification module.
4.5. Quality assessment module
In order to assess the predictions, we obtained the actual market prices
for the stocks mentioned in the posts. A valuable resource for this purpose
16

Table 5: Classification metrics (lexica + ml).
Model Precision (%) Recall (%) F1 (%) Time (s)
Drop Rise Drop Rise Drop Rise Fit Predict
lsvm 93.51 91.29 71.22 84.47 80.86 87.75 55.70 0.0057
dt 91.08 88.76 68.75 81.82 78.36 85.15 0.03 0.0006
knn 91.32 91.47 71.50 81.70 80.20 86.31 0.01 0.8525
mnb 72.13 90.75 82.83 80.24 77.11 85.17 0.02 0.0005
cnb 80.83 89.08 77.34 82.40 79.05 85.61 0.02 0.0005
rf 93.77 89.39 72.39 85.87 81.71 87.60 1.89 0.0508
gb 88.90 90.36 76.99 88.25 82.52 89.29 39.73 0.1174
Table 6: Classification metrics by advisor (lexica + rf).
Ad. Samples Precision (%) Recall (%)
Drop Rise Other Drop Rise Drop Rise
1 35 314 638 86.67 97.35 74.29 93.63
2 176 428 394 97.33 90.00 82.95 94.63
3 102 278 614 95.45 84.78 61.76 84.17
4 138 262 599 92.00 84.54 50.00 66.79
5 96 388 506 88.89 86.93 66.67 84.02
6 50 777 173 100.00 93.67 76.00 98.97
7 163 294 540 99.15 87.26 71.78 93.20
8 59 302 633 95.12 86.27 66.10 58.28
9 100 232 659 92.31 83.43 60.00 65.09
10 73 341 580 96.00 93.00 65.75 81.82
11 350 267 371 91.74 85.08 85.71 94.01
12 114 237 647 91.30 87.55 73.68 86.08
17

is the yfinance Python library 24, which retrieves information about stock
prices from Yahoo®finance api25.
In this research, the posts were annotated as short-term forecasts or one
type or another if they referred to a maximum time range of about four weeks.
The latter is because, in short-term trading, the results of the predictions are
checked weekly (Weng et al., 2018; Shen & Shafiq, 2020; Duarte et al., 2021).
Our assessment considered a drop (/rise) for a particular stock if its minimum
(/maximum) price during three work weeks from Monday to Friday was at
least 3 % lower (/higher) 26 than the stock’s closing price the day the post
was published. Listing 12 shows examples of two correctly classified posts,
one of each essential category.
LISTING 12: Example of two correctly classified posts.
Short-term rise. $NNOX Est´ a alcista en el corto plazo y mejorar ´ ıa bastante si superase
los 14,73.
$NNOX i s b u l l i s h i n t h e s h o r t term and w i l l improve i f i t g e t s
o v e r 1 4 . 7 3 .
Short-term drop. $ASML inmerso en un canal bajista de corto plazo
$ASML l o s t on a downward c h a n n e l i n t h e s h o r t term .
Figure 3 shows the evolution of these stocks’ prices from the post’s pub-
lication until the end of the 4-week window. Both plots clearly show that
the predictions of the posts’ forecasts are coherent with the evolution of the
stock values. A colored dot marks the first day the 3% difference was fulfilled.
Therefore, both predictions were correct, and the respective quality rankings
were updated.
Moreover, Table 7 shows the quality rankings of the predictions estimated
per advisor as success probabilities, which are continuous variables, as de-
sired. In light of the results, we can observe three different profiles: one more
balanced, represented by advisors 2 and 12, with similar qualities for both
drops and rises; another better in drops, like that of advisors 4, 5, and 7; and
another in rises, like advisors 1 and 6.
Additionally, Table 8 shows the social network metrics (user-context met-
rics) of the advisors’ accounts on June 5, 2023. The peak and average likes,
24Available at https://pypi.org/project/yfinance, June 2024.
25Available at https://finance.yahoo.com, June 2024.
26Established based on experimental tests.
18

(a) Nano-X Imaging Ltd stock price evolution.
(b) asml stock price evolution.
Figure 3: Evolution of $NNOX and $ASML stocks.
19

retweets, and replies were calculated using the last 1,000 published posts.
Finally, we studied the correlations between the continuous quality rank-
ings and the user-context metrics of the users’ accounts, the number of fol-
lowers, and the average and peak number of likes, retweets, and replies. This
test offered insights into the reputation of the advisors in the social network
and why the users preferred them. Table 9 shows the correlations.
Table 7: Advisors’ rankings.
Ad. Prediction quality (%)
Drop Rise Global
1 50.00 83.33 80.77
2 76.04 78.00 77.27
3 70.00 76.00 73.24
4 79.63 66.10 69.61
5 73.17 62.21 64.18
6 60.61 67.49 67.36
7 77.91 63.27 67.70
8 80.95 75.86 76.25
9 75.76 72.86 73.58
10 90.91 84.34 85.26
11 73.95 69.28 72.29
12 64.37 63.37 63.91
The strongest correlations in the table suggest that users are more fond of
advisors who correctly predict rises and do not value those who predict drops.
However, we can observe a relation between drop predictions with retweets
and replies. The latter suggests that, even though drop predictions are less
popular (as they are more challenging to convert into gains for inexpert
investors) regarding likes, they attract the interest of investors who comment
about them and share them with other users.
4.6. Explainability module
A model-agnostic approach evaluates a model according to its perfor-
mance regardless of its internal structure. The lime27 (Local Interpretable
27Available at https://lime-ml.readthedocs.io/en/latest, June 2024.
20

Table 8: Social network metrics of the advisors.
Ad. Followers Retweets Likes Replies
Avg. Max. Avg. Max. Avg. Max.
1 10800 6.50 66 5.95 404 0.19 22
2 2657 40.57 12 3.74 52 0.73 74
3 33933 176.11 1919 31.61 313 2.25 54
4 18796 187.68 1188 18.74 246 1.18 26
5 5218 245.02 56109 5.04 70 0.78 13
6 891 1.32 8 0.78 11 0.08 2
7 3609 4.39 9 4.36 34 0.34 12
8 12062 37.29 1070 4.86 72 1.08 16
9 8574 210.72 92565 10.55 254 0.84 38
10 3465 183.45 34457 3.54 116 0.77 20
11 4650 106.03 11 5.39 66 0.92 14
12 3662 11.77 1049 2.90 160 0.70 43
Table 9: Correlations between social network metrics and quality rankings.
Social metric Correlations
Drop Rise Global
Followers Num. -0.029 0.184 0.091
Retweets Avg. 0.473 -0.018 0.031 Max. 0.264 -0.007 0.021
Likes Avg. 0.049 0.084 0.011 Max. -0.406 0.403 0.302
Replies Avg. 0.331 0.107 0.056 Max. 0.030 0.284 0.180
21

Model-Agnostic Explanations) algorithm trains a local model that repro-
duces the performance of the original model and evaluates the impact of the
presence (or absence) of a given input feature in the final classification result.
From the resulting most relevant features, we explained in natural lan-
guage the prediction outcome using the template in Listing 13, where<tweet>
represents the original published post, <category> the prediction of the clas-
sification module and <terms> and <f eatures>unique terms and the most
relevant features involved in the classification, respectively.
As the textual features may include char-grams not corresponding to
understandable words, we implemented the methodology in our previous
research (Gonz´ alez-Gonz´ alez et al., 2023), which approximates those char-
grams to the extended most frequent words that contain them.
LISTING 13: Natural language explanation template (in English).
The c l a s s i f i c a t i o n o f t h e p o s t <tweet> a s <category> can be
e x p l a i n e d by t h e p r e s e n c e o f t h e s e terms : <terms> .
A d d i t i o n a l l y , t h e p r o c e s s c o n s i d e r e d t h e f o l l o w i n g f e a t u r e s :
<f eatures>.
Listing 14 contains a real example of an explanation generated for a clas-
sified post.
LISTING 14: Explanation example.
The c l a s s i f i c a t i o n o f t h e p o s t “#SANTANDER Bullish divergence
monitoring 4.54 euros at close a s short-term rise can be e x p l a i n e d by
t h e p r e s e n c e o f t h e s e terms : [‘bullish’, ‘divergence’] .
A d d i t i o n a l l y , t h e p r o c e s s c o n s i d e r e d t h e f o l l o w i n g f e a t u r e s :
[‘Pos. num.’] .
The post, classified as a short-term rise, contains unique terms bullish
and divergence. Additionally, the model-agnostic methodology considered
favorable prices (feature 10 in Table 2) a relevant feature. This explanation
in natural language is descriptive and understandable for a user without
expert knowledge in finance or ml. Figure 4 shows the mobile application.
In the picture on the left (a), the list of posts displayed includes information
about the author, ticker, and short-term prediction. When the end user
selects a particular post, a new window pops up (picture on the right (b)) to
explain the prediction in natural language.
22

(a) List of analyzed posts.
 (b) Selected post explanation.
Figure 4: Mobile application.
23

4.7. Discussion and comparison with prior work
The credibility of social media in finance has already been studied in prior
work. However, this research follows a more integral solution by comparing
automatic classifications of posts’ forecasts with the actual evolution of mar-
ket values. The results are comparable or superior to those in the literature
(Kamkarhaghighi et al., 2016; Evans et al., 2021). Our system offers high
classification performance and a quality ranking that we have compared with
user-context social media metrics. The solution accurately classifies financial
social media posts using a hybrid approach that combines term-based and
ml techniques with average precision values exceeding 90 % in the case of
rf. It then automatically assesses user credibility from social media, provid-
ing a credibility ranking on a continuous scale. As valuable insights toward
understanding human behavior related to stock market predictions, we have
identified a positive correlation between drop predictions and retweets and
replies and an inverse correlation between those predictions and the number
of likes.
As a side contribution to explainability, we offer model-agnostic descrip-
tions using natural language templates, which are legible and easily under-
standable. For example, the latter is more flexible than the approach by
Huang et al. (2021), which requires previous knowledge about the structure
of the dt model and does not provide explanations in natural language.
5. Conclusions
Social media anonymity, fast-spreading, and low-effort information-sharing
have raised credibility concerns about users regarded as experts. Since the
amount of information users post is enormous, there is a need for automatic
mechanisms to evaluate their reputation. Most current works on credibility
assessment have mainly approached this task as a binary classification prob-
lem instead of ranking credibility as a continuous metric and do not compare
their outcome with real-world data. Moreover, they do not have automatic
explainability capabilities.
The main contribution of this research is a credibility assessment method-
ology combining ml and Natural Language Processing ( nlp), applied to fi-
nancial posts’ forecasts, which are automatically classified and compared with
the actual evolution of the market values. This allows ranking credibility to
be a continuous metric of success probability. Moreover, the correlations
between the credibility ranking and the social media metrics ( i.e., the user
24

context) produce insights related to the interest of the end-users regarding
the posts’ forecasts. Concerning explainability, the system generates descrip-
tions of its decisions in natural language, which are legible and easily under-
standable, using a model-agnostic approach. Therefore, the classification can
be entirely modular and interchangeable. This explainable system may al-
low non-expert investors to understand the classifier’s decisions and quickly
judge investment recommendations, thus empowering them with valuable fi-
nancial knowledge on market strategies. The resulting application supports
continuous real-time analysis of the posts (the prediction time with rf was
0.05 seconds).
Furthermore, given the fact that the underlying term-based and ml tech-
niques can be applied to many nlp tasks ( i.e., sa, detection of fake news,
classification of medical or legal texts), the strategy in this work can be ap-
plied to any field with a strong presence in social media in which reputation
assessment has value, such as recommendation platforms or online gaming,
complementing traditional metrics like the past return rate (yield) and per-
centage of success.
In future work, we plan to take advantage of real-time data to train our
models in streaming mode, introduce new approaches ( e.g., reinforcement
learning) to further enhance the system’s adaptability, and analyze how new
features influence the assessment, including the effect of the elapsed time
between the post and the current date, which will be addressed with sliding
windows. We will explore how to improve recall in our system by reducing the
data drift problems in posts written by different authors. We will also study
adaptive precision methods to select the safest investment recommendations
and explore long-term stock market opportunities. Finally, we will consider
the application to other fields, such as online gaming with sports bets.
CRediT authorship contribution statement
Silvia Garc ´ ıa-M´ endez: Conceptualization, Methodology, Software, Val-
idation, Formal analysis, Investigation, Resources, Data Curation, Writing
- Original Draft, Writing - Review & Editing, Visualization, Supervision,
Project administration, Funding acquisition. Francisco de Arriba-P´ erez:
Conceptualization, Methodology, Software, Validation, Formal analysis, In-
vestigation, Resources, Data Curation, Writing - Original Draft, Writing -
Review & Editing, Visualization, Supervision, Project administration, Fund-
ing acquisition. Jaime Gonz´ alez-Gonz´ alez: Software, Validation, Re-
25

sources, Data Curation, Writing – original draft. Francisco J. Gonz´ alez-
Casta˜ no: Conceptualization, Methodology, Investigation, Writing - Review
& Editing, Supervision.
Declaration of competing interest
The authors declare no competing financial interests or personal relation-
ships that could influence the work reported in this paper.
Data availability
Data are available on request from the authors.
Acknowledgments
This work was partially supported by (i ) Xunta de Galicia grants ED481B-
2021-118, ED481B-2022-093, and ED431C 2022/04, Spain; (ii ) Ministerio de
Ciencia e Innovaci´ on grant TED2021-130824B-C21, Spain; and (iii ) Univer-
sity of Vigo/CISUG for open access charge.
References
Abdullah, B., Alosaimi, N., & Almotiri, S. (2021). Reputation Mea-
surement based on a Hybrid Sentiment Analysis Approach for Saudi
Telecom Companies. Int. J. Adv. Comput. Sci. Appl. , 12 , 929–937.
doi:10.14569/IJACSA.2021.01206107.
Abu-Salih, B., Wongthongtham, P., Chan, K. Y., & Zhu, D. (2019). Cred-
SaT: Credibility ranking of users in big social data incorporating seman-
tic analysis and temporal factor. J. Inf. Sci. , 45 , 259–280. doi: 10.1177/
0165551518790424.
Akbar, M. A., Khan, A. A., Mahmood, S., Rafi, S., & Demi, S. (2023).
Trustworthy artificial intelligence: A decision-making taxonomy of poten-
tial challenges. Softw. Pract. Exp. , (pp. 1–30). doi: 10.1002/spe.3216.
Al-Yazidi, S. A., Berri, J., & Hassan, M. M. (2022). Novel hybrid model for
organizations’ reputation in online social networks. J. King Saud Univ.
Comput. Inf. Sci. , 34 , 5305–5317. doi: 10.1016/j.jksuci.2022.01.006.
26

Alrubaian, M., Al-Qurishi, M., Al-Rakhami, M., Hassan, M. M., & Alamri,
A. (2017). Reputation-based credibility analysis of Twitter social network
users. Concurr. Comput. Pract. Exp. , 29 , 1–12. doi: 10.1002/cpe.3873.
Alzanin, S. M., Azmi, A. M., & Aboalsamh, H. A. (2022). Short text classi-
fication for Arabic social media tweets. J. King Saud Univ. Comput. Inf.
Sci., 34 , 6595–6604. doi: 10.1016/j.jksuci.2022.03.020.
Aoumeur, N. E., Li, Z., & Alshari, E. M. (2023). Improving the Polar-
ity of Text through word2vec Embedding for Primary Classical Arabic
Sentiment Analysis. Neural Process. Lett., 55 , 2249–2264. doi: 10.1007/
s11063-022-11111-1 .
Asfand-E-Yar, M., Hashir, Q., Tanvir, S. H., & Khalil, W. (2023). Classify-
ing Misinformation of User Credibility in Social Media Using Supervised
Learning. Comput. Mater. Contin. , 75 , 2921–2938. doi: 10.32604/cmc.
2023.034741.
Assery, N., Xiaohong, Y. D., Xiuli, Q., Kaushik, R., & Almalki, S.
(2022). Evaluating disaster-related tweet credibility using content-based
and user-based features. Inf. Discov. Deliv. , 50 , 45–53. doi: 10.1108/
IDD-04-2020-0044 .
Batic, D., Stankovic, V., & Stankovic, L. (2024). Towards Transparent Load
Disaggregation – A Framework for Quantitative Evaluation of Explain-
ability Using Explainable AI. IEEE Trans. Consum. Electron., (pp. 1–12).
doi:10.1109/TCE.2023.3300530.
Bengesi, S., Oladunni, T., Olusegun, R., & Audu, H. (2023). A Ma-
chine Learning-Sentiment Analysis on Monkeypox Outbreak: An Exten-
sive Dataset to Show the Polarity of Public Opinion From Twitter Tweets.
IEEE Access, 11 , 11811–11826. doi: 10.1109/ACCESS.2023.3242290.
Bukhari, A., Qamar, U., & Ghazia, U. (2017). UR WF: user reputation based
weightage framework for Twitter micropost classification. Inf. Syst. bus.
Manag., 15 , 623–659. doi: 10.1007/s10257-016-0320-0 .
Cambria, E., Malandri, L., Mercorio, F., Mezzanzanica, M., & Nobani, N.
(2023). A survey on XAI and natural language explanations. Inf. Process.
Manag., 60 , 1–16. doi: 10.1016/j.ipm.2022.103111.
27

Chen, R., Li, J., Zhang, H., Sheng, C., Liu, L., & Cao, X. (2023). Sim2Word:
Explaining Similarity with Representative Attribute Words via Counter-
factual Explanations. ACM Trans. Multimedia Comput. Commun. Appl. ,
19 , 220–242. doi: 10.1145/3563039.
Darad, S., & Krishnan, S. (2023). Sentimental analysis of COVID-19 twitter
data using deep learning and machine learning models. Ingenius, 2023 ,
108–117. doi:10.17163/ings.n29.2023.10.
Duarte, J. J., Gonz´ alez, S. M., & Cruz, J. C. (2021). Predicting Stock Price
Falls Using News Data: Evidence from the Brazilian Market. Comput.
Econ., 57 , 311–340. doi: 10.1007/s10614-020-10060-y .
Evans, L., Owda, M., Crockett, K., & Vilas, A. F. (2021). Credibil-
ity assessment of financial stock tweets. Expert Syst. Appl. , 168 , 1–16.
doi:10.1016/j.eswa.2020.114351.
Gonz´ alez-Gonz´ alez, J., Arriba-P´ erez, F., Garc ´ ıa-M´ endez, S., Busto-
Casti˜ neira, A., & Gonz´ alez-Casta˜ no, F. J. (2023). Automatic expla-
nation of the classification of Spanish legal judgments in jurisdiction-
dependent law categories with tree estimators. J. King Saud Univ. Com-
put. Inf. Sci. , (pp. 101634–101645). doi: https://doi.org/10.1016/j.
jksuci.2023.101634.
Gonz´ alez-Gonz´ alez, J., Garc ´ ıa-Mendez, S., Arriba-P´ erez, F. D., Gonz´ alez-
Casta˜ no, F. J., & Barba-Seara, O. (2022). Explainable Automatic Indus-
trial Carbon Footprint Estimation From Bank Transaction Classification
Using Natural Language Processing. IEEE Access , 10 , 126326–126338.
doi:10.1109/ACCESS.2022.3226324.
Hanaforoosh, M., Ashtiani, M., & Azgomi, M. A. (2021). An approach based
on multiplex networks for modeling cascading trust failures in social net-
works. J. Comput. Sci. , 54 , 101430–101446. doi: 10.1016/j.jocs.2021.
101430.
Huang, T.-C., Zaeem, R. N., & Barber, K. S. (2019). It Is an Equal Failing to
Trust Everybody and to Trust Nobody: Stock price prediction using trust
filters and enhanced user sentiment on Twitter. ACM Trans. Internet
Technol., 19 , 1–20. doi: 10.1145/3338855.
28

Huang, T.-C., Zaeem, R. N., & Barber, K. S. (2021). Identifying Real-world
Credible Experts in the Financial Domain. Digit. Threat. Res. Pract. , 2 ,
1–14. doi:10.1145/3446783.
Hudon, A., Beaudoin, M., Phraxayavong, K., Dellazizzo, L., Potvin, S., &
Dumais, A. (2022). Implementation of a machine learning algorithm for au-
tomated thematic annotations in avatar: A linear support vector classifier
approach. Health Inform. J. , 28 , 1–12. doi:10.1177/14604582221142442.
Jalal, N., Mehmood, A., Choi, G. S., & Ashraf, I. (2022). A novel improved
random forest for text classification using feature ranking and optimal
number of trees. J. King Saud Univ. Comput. Inf. Sci. , 34 , 2733–2742.
doi:10.1016/j.jksuci.2022.03.012.
Jing, N., Wu, Z., Lyu, S., & Sugumaran, V. (2021). Information cred-
ibility evaluation in online professional social network using tree aug-
mented na ¨ ıve Bayes classifier. Electron. Commer. Res. , 21 , 645–669.
doi:10.1007/s10660-019-09387-y .
Jung, S., Noh, Y., Moon, J., & Hwang, E. (2022). V APER: A deep learn-
ing model for explainable probabilistic regression. J. Comput. Sci. , 63 ,
101824–101836. doi:10.1016/j.jocs.2022.101824.
Kaliyar, R. K., Goswami, A., & Narang, P. (2021). DeepFakE: improving fake
news detection using tensor decomposition-based deep neural network. J.
Supercomput., 77 , 1015–1037. doi: 10.1007/s11227-020-03294-y .
Kamkarhaghighi, M., Chepurna, I., Aghababaei, S., & Makrehchi, M. (2016).
Discovering Credible Twitter Users in Stock Market Domain. In Proceed-
ings of the IEEE/WIC/ACM International Conference on Web Intelli-
gence (pp. 66–72). IEEE. doi: 10.1109/WI.2016.0020.
Kozik, R., Kula, S., Chora´ s, M., & Wo´ zniak, M. (2022). Technical solution
to counter potential crime: Text analysis to detect fake news and disinfor-
mation. J. Comput. Sci. , 60 , 101576–101583. doi:10.1016/j.jocs.2022.
101576.
Kurniati, R., & Widyantoro, D. H. (2017). Identification of Twitter User
Credibility Using Machine Learning. In Proceedings of the International
29

Conference on Instrumentation, Communications, Information Technol-
ogy, and Biomedical Engineering (pp. 282–286). IEEE. doi: 10.1109/
ICICI-BME.2017.8537765.
Li, J., Paananen, V., Suryanarayana, S. A., Huusko, E., Kuutila, M.,
M¨ antyl¨ a, M., & Hosio, S. (2023). It is an online platform and not the
real world, I don’t care much: Investigating Twitter Profile Credibility
with an Online Machine Learning-Based Tool. In Proceedings of the Con-
ference on Human Information Interaction and Retrieval (pp. 117–127).
Association for Computing Machinery. doi: 10.1145/3576840.3578308.
Nian, F., Shi, Y., & Cao, J. (2021). Modeling information propagation in
high-order networks based on explicit–implicit relationship. J. Comput.
Sci., 55 , 101438–101445. doi: 10.1016/j.jocs.2021.101438.
Page, J. T., & Duffy, M. E. (2018). What Does Credibility Look like? Tweets
and Walls in U.S. Presidential Candidates’ Visual Storytelling. J. Political
Mark., 17 , 3–31. doi: 10.1080/15377857.2016.1171819.
Pelau, C., Pop, M.-I., Stanescu, M., & Sanda, G. (2023). The Breaking News
Effect and Its Impact on the Credibility and Trust in Information Posted on
Social Media. Electronics, 12 , 1–11. doi:10.3390/electronics12020423.
Prada, A., & Iglesias, C. A. (2020). Predicting Reputation in the Sharing
Economy with Twitter Social Data. Appl. Sci. , 10 , 1–18. doi: 10.3390/
app10082881.
Qureshi, K. A., Malick, R. A. S., & Sabih, M. (2021). Social Media and
Microblogs Credibility: Identification, Theory Driven Framework, and
Recommendation. IEEE Access, 9 , 137744–137781. doi:10.1109/ACCESS.
2021.3114417.
Raheja, S., & Asthana, A. (2022). Sentiment Analysis of Tweets During
the COVID-19 Pandemic Using Multinomial Logistic Regression. Int. J.
Softw. Innov. , 11 , 1–16. doi: 10.4018/IJSI.315740.
Ryans, J. P. (2021). Textual classification of SEC comment letters. Rev.
Account. Stud., 26 , 37–80. doi: 10.1007/s11142-020-09565-6 .
30

Shen, J., & Shafiq, M. O. (2020). Short-term stock market price trend pre-
diction using a comprehensive deep learning system. J. Big Data , 7 , 1–33.
doi:10.1186/s40537-020-00333-6 .
Shrestha, A., Duran, J., Spezzano, F., & Serra, E. (2024). Joint Credibility
Estimation of News, User, and Publisher via Role-relational Graph Con-
volutional Networks. ACM Trans. Web , 18 , 1–24. doi: 10.1145/3617418.
Verma, P. K., Agrawal, P., Madaan, V., & Gupta, C. (2022). UCred:
fusion of machine learning and deep learning methods for user credi-
bility on social media. Soc. Netw. Anal. Min. , 12 , 1–10. doi: 10.1007/
s13278-022-00880-1 .
Weng, B., Lu, L., Wang, X., Megahed, F. M., & Martinez, W. (2018). Pre-
dicting short-term stock prices using ensemble methods and online data
sources. Expert Syst. Appl., 112 , 258–273. doi:10.1016/j.eswa.2018.06.
016.
Zhou, F., Jin, J., Du, X., Zhang, B., & Yin, X. (2017). A calculation method
for social network user credibility. In Proceedings of IEEE International
Conference on Communications (pp. 1–6). IEEE. doi:10.1109/ICC.2017.
7997425.
31
