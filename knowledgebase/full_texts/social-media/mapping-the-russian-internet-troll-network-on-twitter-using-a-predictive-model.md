---
title: Mapping the Russian Internet Troll Network on Twitter using a Predictive Model
url: https://arxiv.org/abs/2409.08305
category: social-media
subcategory: empirical
date: 2024-09
venue: ''
authors:
- Sachith Dassanayaka
- Ori Swed
- Dimitri Volchenkov
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.08305
pages: 17
chars: 44199
fetched_at: '2026-11-08T13:09:21+00:00'
kb_version: 1
---

# Mapping the Russian Internet Troll Network on Twitter using a Predictive Model

Mapping the Russian Internet Troll Network on Twitter
using a Predictive Model
Sachith Dassanayaka1, Ori Swed 2, and Dimitri Volchenkov 3
1,3Department of Mathematics and Statistics, Texas Tech University, Lubbock,
Texas
2Department of Sociology, Anthropology, and Social Work, Texas Tech
University, Lubbock, Texas
Abstract
Russian Internet Trolls use fake personas to spread disinformation through multiple
social media streams. Given the increased frequency of this threat across social media plat-
forms, understanding those operations is paramount in combating their influence. Building
on existing scholarship on the inner functions within influence networks on social media,
we suggest a new approach to map those types of operations. Using Twitter content iden-
tified as part of the Russian influence network, we created a predictive model to map the
network operations. We classify accounts type based on their authenticity function for a
sub-sample of accounts by introducing logical categories and training a predictive model to
identify similar behavior patterns across the network. Our model attains 88% prediction
accuracy for the test set. Validation is done by comparing the similarities with the 3 mil-
lion Russian troll tweets dataset. The result indicates a 90.7% similarity between the two
datasets. Furthermore, we compare our model predictions’ on a Russian tweets dataset,
and the results state that there is 90.5% correspondence between the predictions and the
actual categories. The prediction and validation results suggest that our predictive model
can assist with mapping the actors in such networks.
keywords: Predictive Model, Authenticity Function, Validation
1 Introduction
Internet troll networks (ITN) or troll networks—entities that spread disinformation on social
media through fake accounts—have become a serious threat to democratic discourse. Under-
standing and detecting those operations turns paramount. One of the leading state actors in
this field was Russia [1], using ITN across multiple platforms and in different countries as an
influence tool[2, 3]. Examination of the Russian trolling operation indicates that Russian ITN
was fragmented and run by multiple entities. One of those was the Internet Research Agency
(IRA), a company affiliated with the Kremlin and located in St. Petersburg. The IRA has been
involved with multiple overseas political activities, among them the 2016 U.S. presidential elec-
tion interference [2, 4, 5]. In the 2016 campaign, the IRA accounts concealed their true identity
by presenting themselves as legitimate social media users such as regular folks from rural and
suburban America [6]. This common tactic makes it harder for users and regulators to identify
1
arXiv:2409.08305v1  [cs.SI]  11 Sep 2024

and prevent ITNs and influence operations. Thus, the problem is differentiating fake actors
that pretend to be legitimate users from the rest. Due to the hidden nature of the Russian ITN,
differentiating actors based on their activities is an open challenge. Furthermore, researchers’
difficulties with identifying the fake users pose a significant challenge for understanding those
types of operations and consequently make it harder for us to devise ways to stop them. To
address this problem, in this study, we use artificial intelligence as an ancillary instrument to
map trolls’ activities across influence networks.
The principal obstacle scholars that study ITN face is the amorphous nature of the network.
Paradoxically, the personae that the network introduces maintain a legible and influential social
appearance. However, these personae are fake and, as such, offer a limited foothold on the
perpetrators. Moreover, they are hard to detect, differentiating between authentic users and
socket puppets. Following existing methods in this field, our study addresses this obstacle
by studying exposed trolls’ networks, suggesting a machine learning predictive model to map
network operations and classify the actors. The predictive model focuses on different types of
actors in the Russian ITN, their distribution, and their activities. Building on studies that
identified organizational order and functions assigned to specific accounts, we assert that this
division of roles is meaningful enough to help with mapping those networks [7, 8].
We used English language tweets from the IRA tweets dataset that was linked with the IRA,
from the Alliance for Security Democracy data (https://securingdemocracy.gmfus.org/)
and mapped them according to their authenticity function. In other words, the different ways
they presented themselves. We recognized four conceptual categories: Fake News, Organi-
zations, Political Affiliates, and Individuals. Next, we trained a machine learning predictive
model to identify the category of each account in the network using several features, such as
the number of tweets, retweets,and followers. One-third of the English language dataset data
were partially hashed, which means there was no available information on the account in its
description and name to assert into which categories they fit. As such, we used our predictive
model on one-third of hashed data. Moreover, we validated our predictive model with the 3
million Russian Troll tweets dataset [7]. Russian speakers assisted us with manual coding of the
accounts per the four categories on the Russian language dataset, a subset of the IRA tweets
dataset, to further evaluate the predictive model’s accuracy.
2 Background and Related Work
Russian ITN on social media has received much attention from scholars and practitioners at-
tempting to better understand this trend and phenomenon. The 2016 Russian influence troll
campaign on social media was excessively studied by cyber security experts and scholars. This
event reoriented discussion on ITN and brought much attention to Russia as a perpetrator
of influence campaigns in social media and the 2016 elections as a case study [2]. Focusing
on the IRA operation between 2015 to 2017, Boatwright, Linvill, and Warren (2018) explored
how the organization weaponized social media and spread its agenda and messaging across
multiple platforms [7]. The researchers shed light on the network, from the way it created a
network of fake personae, organizations, and websites to the way that it spread messaging in
fabricated echo chambers. They recognized five types of Twitter actors whose behaviors were
drastically dissimilar: right troll, left troll, news feed, hashtag gamer,and fearmonger based
on the IRA. In the same context, they pointed out that the Russian intervention in overseas
political activities through fake personae exacerbated social drift by misusing the social media
streams such as Twitter. Another study, which replicated Boatwright, Linvill, and Warren’s
(2018) research concerning category mapping, was conducted by Lewinski and Hasan [9]. The
researchers attempted to replicate the original categories in the 3 million Russian Troll Tweets
2

dataset and automate the classification using a machine learning model.
Elaborating on their earlier work, Linvill et al. (2019) examined tweets connected with the
IRA, creating a more comprehensive categorization of behaviors within the network related to
the 2016 U.S. Presidential election [10]. They tested tweets that were released by the ITN a
month before the election and examined the communication distinctions among Twitter actors.
They came up with seven behavioral categories actors produce in the network: attack left,
support right, attack right, support left, attack media, attack civil institutions, and camouflage.
The scholarship on ITN went beyond theoretical and conceptual discussions, focusing on de-
tection. Methods of detection on Twitter were frequently using a predictive model that focused
on specific aspects of the actors or their behavior, for example, the political role of Internet trolls
(Atanasov et al. 2019) [11]. The researchers examined behavior patterns of political trolls on
the IRA Russian Troll dataset and automated the classification using supervised, and distance
supervised learning machine learning methods to treat categorized and non-categorized trolls,
respectively. Bidirectional Encoding Representations from Transformers (BERT) was used to
build a machine learning model to determine the political tendency of trolls with the Russian
Troll dataset by Chun et al. [12]. Kim et al. (2019)[13] suggested a text distance metric (i.e.,
a time-sensitive semantic edit distance) and applied it to classify the Russian trolls.
Although several studies have addressed the importance of Internet troll classification in
the literature, due to the artificially generated nature of the Russian ITN, differentiating the
actors and revealing the structure still pose a challenge. Some common issues, such as abstract
categorization based on actors’ behavior, automating the operation of this categorization, and
testing the proposed solution on a publicly available troll dataset, are still open to scholars.
3 Dataset Description
This study made use of a publicly available dataset of identified troll activity in social media.
The data, which covers multiple actors and operations, is presented by the Alliance for Security
Democracy. Our study focused on a particular actor, operation, and platform. Namely, the
IRA operation of Twitter in the period leading to the 2016 intervention operation in the US
elections and the time-frame right after [5, 14]. The dataset consisted of about nine million
tweets using 58 languages, and some information had been hashed, i. e., some information
such as “user profile description” was unavailable due to the privacy concerns by Twitter. We
recognized about forty features in the dataset, including profile-related features, qualitative
behavioral measures, and tweet-related linguistic features. We extracted the English language
tweets (henceforth: 1st dataset) and Russian language tweets (henceforth:2nd dataset), which
were about three million and four million tweets, respectively. There were 2,832 unique Twitter
actors that linked with the IRA English dataset, and the tweets were posted between November
2009 and May 2018. Out of those, about 36% of the accounts were hashed, including nearly
21% accounts that had at least one hashtag. The rest of the 15% hashed accounts were not
included in any hashtags. Since we used a machine learning predictive model to recognize
the accounts based on their activities, we had to validate our model to ensure it performed
well beyond the training data. Therefore, for the validation purpose, we used the 3 million
Russian Troll tweets dataset (henceforth: 3rd dataset) and the 2nd dataset. The 3rd dataset
includes 1,133 IRA-related actors, while the2nd dataset consisted of 1,554 actors in total, but
we removed 119 accounts due to lack of information, and we used the remaining 1,435 actors
from the 2nd dataset to validate the predictive model.
3

4 Approach
In this section, we report the hypothetical categories and feature selection of our study. We
created a unique filter for the actors in the Russian IRA network by introducing a concep-
tual categorization of troll actors. The user profile description feature carried more valuable
information regarding the actors’ interest and their unique backgrounds. Across all cases, the
Russian trolls attempted to promote directly or indirectly a specific agenda while maintaining
the façade of a real user (not a “sack puppet”). Keeping that façade, which allowed them to
maintain authenticity, forced the users to specific patterns of behavior and specifically identifi-
able categorizations. To identify those actors and describe their behaviors within the Russian
ITN, we introduced four conceptual categories, which based on the fake authenticity of actors:
• Fake News: Accounts whose description was of a news outlet, including government
news, private news organization, and specialty news such as UFO, military, regional, city,
etc. Some of the actors introduced themselves to the network as online news sources,
such asSan Jose Daily, San Francisco Daily, Novosibirsk Bulletin,and Memphis Online,
to imply that they provided updates by connecting with authorized local news sources
and tweets regarding local news trends. These actors’ portrayals benefited the image of
original news mediums rather than a news fan or an individual that shared the news
on a specific subject. This description differed from the News Feeds category of Linvill
and Warrens’ (2018) research study. Under the News Feeds category, some actors in the
network were pretending to be individuals who talk political interests, such asTENGOP,
Political Observer,and Special Affair.
• Organizations: Accounts whose description was of non-governmental organizations or
businesses, including volunteer organizations. News organizations were not included in
that category. Some Twitter actors let others imagine that they were a group of people
who could support the community, such asHeart Of Texasand Black To Live,pretending
to be social movements or commercial entities.
• Political Affiliates: Accounts whose description was politics-related or seems to present
as individuals that are overtly politically affiliated. Here we could find accounts such as
Jenna Abram that provide unfiltered political commentary.
• Individuals: Accounts whose description was of individuals or seems to present as indi-
viduals that are not overtly politically affiliated. Lastly, the ITN is full of “regular folks”
that function as the core of the network, directing real users into the network and echoing
its messages.
We extracted features such asuser id, user name, user profile description, user mentioned
count, tweet count, retweet count, followers, followings, reply,and likes from the 1st dataset
and associating them with each category, using them as the indicators for the actors’ behavior.
We applied the authenticity function on theuser profile descriptionfeature to assign categories
to the actors in this social network. Although we performed a manual categorization based on
user profile descriptionfor about eighteen hundred actors, nearly a thousand of them did not
have this feature available due to hashed data. Thus, we had to find a way to treat those actors
whohadahashed user profile descriptionbyproposingamathematicalapproachapproximating
the corresponding categories.
4.0.1 Relative frequency of actors’ categories
At this stage, we categorized about 65% of the hashed accounts in the1st dataset using their
user profile description. This sample size was not sufficient for the training of the AI (see
4

Appendix-A). To increase our sample, we used repeating hashtags that appeared in the identi-
fied and categorized accounts to match with similar clusters of hashtags in accounts that have
no description (hashed accounts). By accounting for similarities in hashtags and using them as
a key, we were able to add an additional 21% of the sample. This addition improves the robust-
ness of our model. Therefore, we used 85% of the data from the dataset for the following stages
of our study. There were two types of real-time complications that we had to face while we were
analyzing hashtags. The first problem was dealing with text or human languages in order to
process hashtags. The second problem was that the usage of a hashtag could be changed with
time; in other words, a particular hashtag became more prevalent during an election and then
disappeared. We treated those complications simultaneously by using open-source libraries and
taking subsamples with fixed time frames. Natural language processing (NLP) is the key to
dealing with human languages as we used the natural language toolkit (NLTK) platform in
Python, which has over 50 corpora and lexical supports, to process tweets and hashtags [15].
We used these libraries to analyze the data in individual subsets from July 2009 to June 2018,
with each subset representing six months of fixed time in that span (see Fig. 1). Each subset
was analyzed separately. It was an important task to clean some unnecessary symbols and
convert all of the hashtags to either capital or simple letters. This prevented the capitalization
and symbolical errors that may occur during the analysis and was done through the NLTK
package.
Figure 1: Process of identifying categories for 21% hashed actors in the1st dataset according
to the four conceptual categories.
First, the initial subspan and all of the unique hashtags used by both groups of actors in the
first span were compiled into a list, and this list was used to create a collection of vectors for each
actor. To form the vector, we cross-referenced every actor in both the unhashed (categorized)
and hashed (uncategorized) groupings with each of the unique hashtags. Each row represented
a unique hashtag, and if the actor used a given hashtag, it was represented with a 1 (true) or
a 0 (false).
Consider the collection of vectors of uncategorized actors denoted byU, as in:
5

U = {u.1, u.2, · · ·, u.s} =





u11
u21
...
um1

 ,


u12
u22
...
um2

 , · · ·,


u1s
u2s
...
ums




 , (1)
where m, s represent the total number of unique hashtags, and number of hashed actors
in the current time span, respectively. In the same fashion, the collection of the vectors of
categorized actors in the same span denoted byV, as in:
V = {v.1, v.2, · · ·, v.k} =





v11
v21
...
vm1

 ,


v12
v22
...
vm2

 , · · ·,


v1k
v2k
...
vmk




 , (2)
where k represents the total number of unhashed actors in the current time span.
Algorithm:
• Let i ∈ s and j ∈ k
– Now, consider the current span
– From i = 1(until i = s)
∗ Next, we can calculate the cosine similarity value betweenu.i’s and v.j’s via,
CS (u.i, v.j) = u.i.v.j
||u.i|| ||v.j|| , (3)
where i ≤ s and j ≤ k
∗ find max CS(u.i, v.j)
∗ category (u.i) = category (v.j)
∗ i = i + 1
– Repeat above steps for the next span
• Finally, consider the relative frequency distribution of each actor in uncategorized set
across all spans(∈ B) to approximate their abstract category.
Per the algorithm, we assigned an impermanent category tou.i of the corresponding actorv.j
by considering max(CS (u.i, v.j)) [16, 17]. We continued this process until the categories for all
the u.i’s (hashed actors) were approximated in the current subset. This process was recursive,
continuing until determining the categories of all hashed actors in all the subsets. Finally, we
listed the relative frequency distributions for all hashed actors regarding their impermanent
categories across the subsets and the highest frequent category assigned to the particular actor.
No more than one mode (the highest frequent categories) appeared in each relative frequency
distribution during the calculation. This analytical approximation assisted us in approximating
categories for all of the hashed actors in this dataset, and then we could implement a model
that can be used to recognize actors.
After the categorization, the frequency distribution of conceptual categories illustrated that
the IRA English tweets dataset was imbalanced due to some categories having fewer observa-
tions than the other categories [18, 19, 20] (see Fig. 2).
6

Figure 2: Frequency distribution of abstract categories for 2,408 actors in IRA English dataset.
Table 1: Ranking important features of IRA English dataset using the “SelectKBest” class in
scikit-learn library.
Features Score
followers count 9867.6
hashtags count 9619.8
tweets count 2739.45
usersMentioned 2269.14
retweets count 1448.3
followings count 1324.99
likes count 1262.93
replies count 876.12
quotes count 9.3207
urls count 2.9191
polls count 2.7328
retweet tweet ratio 1.4898
· · · · · ·
retweeters category 0.12836
4.1 Feature Selection
After completing the approximation of categories for the 21% of the hashed actors, we rec-
ognized about 85% of the actors in the IRA English dataset, fitting with the four conceptual
categories. At the following stage, with 2,408 categorized actors (85%), we used features that
are associated with each account to enhance accuracy and reduce over-fitting and training time.
The IRA English dataset had more than 30 features (see Appendix-B for the list of features in
the 1st dataset). Not all features demonstrate meaningful relations with our categorization, and
consequently, we dropped them out of the model. We determine the strength of these features
by using a statistical-based feature selection criterion, the “SelectKBest” class in the scikit-learn
library, for our univariate feature selection criterion in Python. The “SelectKBest” algorithm
uses the chi-square test as the scoring function sequential procedure, which measures the con-
nection between two categorical features, and ranks the features according to their importance
[21, 22].
7

The selected features are tweets count, retweets count, followers count, followings count,
replies count, likes count, users Mentioned,and hashtag counts(see Table. 1). Furthermore, we
check Pearson’s correlation coefficient of the selected eight features [23]. The selected features
reduce the multicollinearity, which is the occurrence of high correlations among two or more
independent variables in the dataset (see Appendix-C). To avoid the effect of different scales
across features, we normalized the dataset. For example, thefollowers countcould be thousands
for a particular actor, butuser Mentioned count was less than ten. Therefore, the scales for
these two features are different, so we reduced the effect of this scale difference by normalizing
(L1) the set. Next, we applied supervised machine learning techniques to build a predictive
model by considering 85% of accounts (2,408) from the1st dataset. Normalization was not
enough since there was still an imbalance in the sample that can affect the supervised learning
classification [24, 25]. Our imbalance dataset consisted of majority and minority categories that
had a larger number of samples and a smaller number of samples, respectively. Thus, there was
a higher chance of miscategorizing the minority classes than the majority classes when training
the predictive model, which could impede performance [25]. To address that, we used stratified
subsampling and Bootstrapping technique [19].
We used three traditional measurements precision, recall, andf1-score to measure the pre-
dictability of the model [26, 27].
Figure 3: Classification accuracy for each conceptual category under different classifiers with
the selected eight features.
Given that our metric of success was classification accuracy, we used a classifier that also
provided a solution for the imbalance in the sample. We used seven frequently use classifiers
(Naïve Bayes, Support Vector Machine, Adaboost, K Nearest Neighbor, Random Forest, De-
cision Tree, Logistic Regression) to compare overall predictability, [28, 29, 30, 31, 32, 33]. A
comparison of the classifiers showed variation in accuracy scores (see Fig. 3). The Naïve Bayes
classifier was 40%, 15%, 90%, and 33% accuracy for Fake News, Organizations, Individuals,
and Political Affiliates, respectively, while the Decision Tree classifier provided 39%, 0%, 92%,
and 44% accuracy for the same abstract categories (see Table 2). Further, although Logistic
8

Table 2: Overall classification accuracy for different classifiers.
Classifier Weighted average f1-score
Naïve Bayes 81.67
Decision Tree 85.18
Random Forest 88.15
K Nearest Neighbor 85.93
AdaBoost 79.26
Support Vector Machine 84.04
Logistic Regression 82.22
Regression and Support Vector Machine could classify the Individuals category with about 90%
accuracy, both Fake News and Organizations categories have 0% support while Logistic Regres-
sion indicated 15% accuracy for Fake News abstract category. On the other hand, AdaBoost,
K Nearest Neighbour, and Random Forest classifiers were 23%, 62%, 88% for the Fake News
and 32%, 55%, 81% for Organizations, respectively. The Individual category had the highest
accuracy of 91%, 89%, 92% while Political Affiliates indicated 24%, 63%, 84% for AdaBoost,
K Nearest Neighbour, and Random Forest classifiers separately. Thus, the Random Forest
classifier provided greater accuracy for each abstract category.
Since Random Forest Classifier is a straightforward machine learning algorithm that learns
imbalanced data, we used this cost-sensitive learner to develop our predictive model [28, 33].
The random forest is a collection of many decision trees that keeps the minimum relationship
among trees. In this forest, we could see the performance, in other words, the predictability,
change with the depth of the trees (see Fig. 4). Controlling the optimum depth of the tree
was significant because too few levels lead the tree to under-fit, and a higher number of levels
prone the model to over-fit to the training samples. Our forest, theoretically, provided a higher
accuracy for five average trees depth without under-fit or over-fit.
Figure 4: Accuracy score (averagef1-score) of the forest changes with the average depth of the
trees.
The Scikit-learn library in Python supports Random Forest Classifier that allowed us to
control the subsample through the parameterclass weight set equals to balanced subsample
[21]. The balanced subsample mode allowed the classifier to regulate weights automatically
according to the inverse proportional to the class frequency with data based on bootstrap
samples [19]. In return, the effect of imbalanced data was reduced. Furthermore, through the
9

Table 3: Predictability measures for each class based on precision, recall, and f1-score on the
test dataset.
Category precision recall f1-score
Fake News 0.94 0.82 0.88
Organizations 0.82 0.80 0.81
Individuals 0.88 0.96 0.92
Political Affiliates 0.83 0.85 0.84
Scikit-learn, we used Gini Index to measure the probability of features being wrongly classified
and identify the root node of the decision trees [34, 35]. The Gini index values are bounded
between 0 and 1, inclusive, while 0 represents the purity of the classification, and one expresses
the randomness. Let us suppose that there arek ∈ Z+ classes in the dataset, and the Gini
impurity can be defined via,
G(S) =
kX
i=1
Pi(1 − Pi), (4)
where S denotes the dataset and Pi represents the probability of selecting a observation
from ith class. The Random Forest Classifier controls the greatest possible depth of each
decision tree by expanding nodes until each branch of a tree classifies into a unique category.
At this point, we built our predictive model and tested the predictability of the model using
traditional measurements results based on the precision, recall, andf1-score on the test set,
which illustrates the model accuracy, not only the overall but the individual categories as well
(see Table. 3).
After the stratified 5-fold cross-validation, the result was 88% of predictability accuracy on
the test set.
4.2 Predictive model validation
Before we applied our predictive model to a random dataset and differentiated the actors of the
particular network, the best practice was to validate the model’s accuracy with known data.
We performed the stratified fivefold cross-validation on the test set, reaching 88% accuracy.
For validation of this prediction, we tested the model performance on other datasets. To assure
maximum compatibility in our first validation test, which used a similar dataset as we did, we
used our prediction model to categorize the missing 15% (about four hundred) hashed accounts
that we could not either identify manually or match with hashtags in the1st dataset. This
increased our sample to 2,832 accounts (see Fig. 5) and improved the compatibility with the
Linvill and Warren database, which we used for our first validation test.
4.2.1 The first validation: with 3rd dataset
The 3 million Russian Troll Tweets dataset was published by FiveThirtyEight and Linvill, and
Warren in 2018, based on their research study [7]. In their study Linvill and Warren created
a unique set of categorizations for different accounts, identifying them by functions. Our four
conceptual categories do not fit with most of their functional classification (for example, left
or right leaning trolls). The only similar comparable groups, and the ones we could use for
the validation test, were theNews Feed from their study andFake News from our research
study. Those were not fully compatible since Linvill and Warren’sNews Feedcategory included
accounts that pretended to be individuals that specialized in sharing news. Yet, this specific
10

Figure 5: Frequency distribution of conceptual categories for 2,832 actors in the 1st dataset,
including all hashed accounts.
category was similar enough, so it should include all the accounts we identified asFake News.
This means that we could expect to see over 88% of the accounts, our model identified asFake
News and that shared with the Linvill and Warren data to be categorized under theirNews
Feedgroup. We filtered the unique actors who were labeled asFake Newsin our1st dataset and
the actors who fitted intoNews Feedgroup in the 3 million Russian Troll Tweets dataset as the
second stage of our validation. We observed that there were forty-ninefake newsaccounts that
match withnews feedout of fifty-four handles. At the same time, fiveNews Feedhandles were
misclassified asindividuals by our predictive model. The result of this validation test suggested
that our model prediction was 90.7% accurate forFake Newsconceptual category.
4.2.2 The second validation: with 2nd Dataset
In a second validation test, we tested our model predictions with the2nd dataset. Here we ran
a similar process of identifying users and categorizing them manually. Next, we compared our
manual categorization with the model’s prediction. We assumed that our model would achieve
the 88% prediction level. Since we were working with the Russian language in the2nd dataset,
we used theGoogle Translate Application Programming Interface(API)to translate the Russian
profile descriptionsto English. At the same time, Russian speakers verified the validity of 1,435
translated Russian language content and then assigned categories manually to the actors in the
2nd dataset based on the same authenticity function. The manual categorization was used
as a reference for the predictive model. We compared the manual categorization of actors in
the four groups to the predictive model results on the dataset, testing for similarities between
our predictions and the actual categories, namely, the manual categorization was done by the
Russian speakers (see Fig. 6).
Fig.6 illustrates the comparison between the manual coding and the predictive model’s
results. It also captures the proportion of matching results. This validation test of the IRA
Russian set shows that the predictive model achieves overall 90.5% prediction accuracy, which
is higher than anticipated.
11

Figure 6: Comparison between number of actual and predicted accounts.
5 Discussion
Russian trolls that linked with IRA spread out disinformation on Twitter by concealing their
true nature and allowing them to engage in act of information warfare. Differentiate actors in
such networks helped researchers to reveal and understand the structure of the troll networks
and behaviors.
In this study, we offered a mechanism that helps identify the actors in the Russian troll
networks through a predictive model that has the ability to map the actors in the Russian
troll network. Our model builds on four conceptual categories and assigns them to each actor
based on their behaviors. The IRA dataset, which we used for our study, consists of about
nine million tweets using 58 languages, including English and Russian. From this dataset, we
used English tweets to propose conceptual categories and implemented a predictive model that
provided 88% prediction accuracy for the test set.
We verified our model predictions on the publicly available 3 million Russian troll tweets
dataset, and the comparison result showed 90.7% accuracy in prediction. Moreover, we vali-
dated the accuracy of our model predictions on the Russian language troll tweets set, which was
a subset of the IRA dataset, by conducting a human evaluation. The outcome was 90.5% sim-
ilarity between the predictions and classification of the Russian language troll tweets dataset.
Lewinski and Hasan attempted a similar analysis using a Support Vector Machine (SVM) model
[9]. With the SVM model, they tried to map Facebook’s ads accounts while building on Linvill
and Warren’s categorization. Although their goal was not to focus on automating Linvill and
Warren’s categorization, their SVM model provided 75.5% accuracy for theNews Feedcategory
when Lewinski and Hasan applied to the 3 million Russian Troll Tweets dataset. The result
demonstrated that our predictive model provided comparatively higher accurate predictions
(90.7%) than the SVM model to theNews Feedcategory in the 3 million Russian Troll Tweets
dataset.
6 Conclusion
This study presents a path to reveal and study the structure of the IRA network; a hostile
network that tried to promote a seditious agenda while concealing its activities and real identity.
12

Since this study focuses on Twitter, the proposed solution (the predictive model) is based on
troll networks that have been conducted on Twitter only. The organized nature of the tweets,
either from a person or a computer, can be simplified using our conceptual categories, and
the proposed model is a tweet language free network model that is useful to map the IRA
network in order to differentiate actors in ITN. Since the model is free of language, the process
of classifying fake personas is not affected by the Twitter content’s language as long as the
samples are taken from the IRA network. We have to align with the IRA network because we
have yet to test our predictive model against other networks outside the IRA.
Future research can build on this predictive model to better analyze and understand specif-
ically the IRA network and influence operations online in general. Our model utilizes Twitter
activities such as tweets, retweets, likes, and replies can be used to examine activity patterns
in the network and visualize them in 3-dimensional space. Moreover, while the model was
designed for Twitter, it can be reproduced for other social media platforms such as Instagram
and Facebook. The predictive model offers us a stable baseline for further mathematical pre-
dictions and analysis of those actors and activities. Mathematical models that draw on our
model can potentially identify actors. Further, thistweet language freenetwork model can be
used to examine other influence networks on Twitter, among them the Chinese and Iranian net-
works, and analyze and compare these networks to reveal their typical patterns and behaviors.
Although the research focuses on classifying fake personas, the foundations this study offers
can potentially assist with improving existing tools that specialize in real-time identification of
Troll activities on Twitter and differentiate them from legitimate users’ activities.
References
[1] Llewellyn, C., Cram, L., Hill, R. L., and Favero, A. (2019), For whom the bell trolls:
Shifting troll behaviour in the Twitter Brexit debate.JCMS: Journal of Common Market
Studies, 57(5), 1148–1164.
[2] Mueller III, R. S. (2019), Report On The Investigation Into Russian Interference In The
2016 Presidential Election, Volumes I & II, (Redacted version of 4/18/2019).
[3] Golovchenko, Y., Buntain, C., Eady, G., Brown, M. A., and Tucker, J. A. (2020). Cross-
platform state propaganda: Russian trolls on Twitter and YouTube during the 2016 US
presidential election.The International Journal of Press/Politics, 25(3), 357-389.
[4] Bey, M. (2018), Great Powers in Cyberspace: The Strategic Drivers Behind US, Chinese
and Russian Competition.The Cyber Defense Review, 3(3), 31-36.
[5] Bail, C. A., Guay, B., Maloney, E., Combs, A., Hillygus, D. S. et al. (2020), Assessing
the Russian Internet Research Agency’s impact on the political attitudes and behaviors
of American Twitter users in late 2017,Proceedings of the national academy of sciences,
117(1), 243–250.
[6] Xia, Y., Lukito, J., Zhang, Y., Wells, C., Kim, S.J. and Tong, C. (2019), Disinforma-
tion, performed: Self-presentation of a Russian IRA account on Twitter,Information,
Communication & Society, 22(11), 1646–1664.
[7] Boatwright, B.C., Linvill, D.L. and Warren, P.L. (2018), Troll factories: The internet
research agency and state-sponsored agenda building,Resource Centre on Media Freedom
in Europe, 29.
13

[8] Kim, D., Graham, T., Wan, Z., and Rizoiu, M. A. (2019), Tracking the digital traces of
russian trolls: Distinguishing the roles and strategy of trolls on twitter.arXiv preprint
arXiv:1901.05228.
[9] Lewinski, D. and Hasan, M. R. (2021), Russian Troll Account Classification with Twitter
and Facebook Data,arXiv preprint arXiv:2101.05983.
[10] Linvill, D. L., Boatwright, B. C., Grant, W. J., and Warren, P. L. (2019). “THE RUS-
SIANS ARE HACKING MY BRAIN!” investigating Russia’s internet research agency
twitter tactics during the 2016 United States presidential campaign,Computers in Hu-
man Behavior, 99, 292–300.
[11] Atanasov, A., Morales, G.F. and Nakov, P. (2019), Predicting the role of political trolls
in social media,arXiv preprint arXiv:1910.02001.
[12] Chun, S. A., Holowczak, R. D., Dharan, K., Wang, R., Basu, S., and Geller, J. (2019),
Detecting Political Bias Trolls in Twitter Data.In WEBIST, 334–342.
[13] Kim, D., Graham, T., Wan, Z., and Rizoiu, M. A. (2019), Tracking the digital traces of
russian trolls: Distinguishing the roles and strategy of trolls on twitter,arXiv preprint
arXiv:1901.05228.
[14] François, C., Nimmo, B. and Eib, C.S. (2019), The IRA CopyPasta Campaign,Graphika,
okt.
[15] Bird, S., Klein, E. and Loper, E. (2009),Natural language processing with Python: ana-
lyzing text with the natural language toolkit, “ O’Reilly Media, Inc.”.
[16] Rahutomo, Faisal, Kitasuka, T. and Aritsugi, M. (2012, October), Semantic cosine simi-
larity,In The 7th International Student Conference on Advanced Science and Technology
ICAST, 4(1), 1.
[17] Li, B. and Han, L. (2013, October), Distance weighted cosine similarity measure for
text classification,International conference on intelligent data engineering and automated
learning, Springer, Berlin, Heidelberg, 611–618.
[18] Japkowicz, N. and Stephen, S. (2002), The class imbalance problem: A systematic study,
Intelligent Data Analysis, 6(5), 429–449.
[19] Dupret, G.andKoda, M.(2001), Bootstrapre-samplingforunbalanceddatainsupervised
learning, European Journal of Operation research, 134(1), 141–156.
[20] Liu, X., Wu, J. and Zhou, Z. (2009), Exploratory Undersampling for Class-Imbalance
Learning, IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics),
39(2), 539–550.
[21] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B. et al. (2011), Scikit-
learn: Machine learning in Python,The Journal of machine Learning research, 12, 2825–
2830.
[22] Pope, P.T. and Webster, J.T. (1972), The use of an F-statistic in stepwise regression
procedures,Technometrics, 14(2), 327–340.
[23] Hauke, J., and Kossowski, T. (2011), Comparison of values of Pearson’s and Spearman’s
correlation coefficient on the same sets of data.
14

[24] Japkowicz, N. (2000, June), The class imbalance problem: Significance and strategies.In
Proc. of the Int’l Conf. on Artificial Intelligence, 56.
[25] Abd Elrahman, S. M. and Abraham, A. (2013), A review of class imbalance problem,
Journal of Network and Innovative Computing, (1), 332–340.
[26] Powers, D., (2011), Ailab, Evaluation: From Precision, Recall and F-measure to ROC,
Informedness, Markedness & Correlation, Journal of Machine Learning Technologies,
2(22293981), 1.
[27] Opitz, J. and Burst, S. (2019), Macro f1 and macro f1,arXiv preprint arXiv:1911.03347.
[28] Breiman, L. (2001), Random forests,Machine learning, 45(1), 5–32.
[29] Murphy, K. P. (2006), Naive bayes classifiers,University of British Columbia, 18(60),
1–8.
[30] Peterson, L. E. (2009), K-nearest neighbor,Scholarpedia, 4(2), 1883.
[31] Ng, A.Y.andJordan, M.I.(2002), Ondiscriminativevs.generativeclassifiers: Acompar-
ison of logistic regression and naive bayes,In Advances in neural information processing
systems, 841–848.
[32] Li, X., Wang, L., and Sung, E. (2008), AdaBoost with SVM-based component classifiers,
Engineering Applications of Artificial Intelligence, 21(5), 785–795.
[33] Devetyarov, D. and Nouretdinov, I. (2010, October), Prediction with confidence based
on a random forest classifier,In IFIP International Conference on Artificial Intelligence
Applications and Innovations, Springer, Berlin, Heidelberg, 37–44.
[34] Raileanu, L.E. and Stoffel, K. (2004), Theoretical comparison between the Gini Index
and Information Gain criteria,Annals of Mathematics and Artificial Intelligence, 41(1),
77—93.
[35] Rickard, S., and Fallon, M. (2004, March), The Gini index of speech,In Proceedings of
the 38th Conference on Information Science and Systems (CISS’04).
Appendix-A
Suppose that we considered 64% (about 1,800) actors in the 1st dataset and applied the
above classifiers to the data in order to determine the “the best” classifier to train a predictive
model. Classification accuracy was measured for different classifiers and conceptual categories
(see Fig. 7). According to Fig. 7, regardless of the classifiers, accuracy declined, due to the
sample size. Some categories did not have “large enough” samples, such asOrganizations to
train the model. However, since the samples are small, models become biased, and the models
predictability decreases.
The overall accuracy of the model decreases as accuracy for each category decreases. On
the other hand, the majority of this unhashed data includesIndividuals actors, and it causes
the misrepresents the overall accuracy. Therefore, considering hashed data as much as possible
is the solution to overcome this issue. As a result, we used 21% samples from hashed IRA
English dataset to train our predictive model.
Appendix-B
15

Table 4: The list of features in the1st dataset.
Feature Description
tweetid Unique id for each tweet content
userid Unique id for each actor
user_display_name Actor name that public can see
user_screen_name Actor name on the account.
user_reported_location Physical location of the actor when sending the tweet
user_profile_description Profile description of the actor
user_profile_url Profile url of the actor
follower_count Number of followers related to the actor
following_count Number of followings related to the actor
account_creation_date Account creation date
account_language Language registered with the account
tweet_language Language of the tweet content
tweet_text Tweet content
tweet_time Time of the tweet sent
tweet_client_name Name of the internet service provider
in_reply_to_tweetid Replied tweets id
in_reply_to_userid Replied actors id
quoted_tweet_tweetid Quoted tweet tweet id
is_retweet Whether tweet or retweet (True or False)
retweet_userid Retweet actor id
retweet_tweetid Retweet tweet id
latitude Latitude of the physical location of the actor
longitude Longitude of the physical location of the actor
quote_count Number of quotes in the tweet
reply_count Number of reported replies to the tweet
like_count Number of reported likes to the tweet
retweet_count Number of reported retweets to the tweet
hashtags Hashtags mentioned in the tweet
urls Urls mentioned in the tweet
user_mentions User ids mentioned in the tweet
poll_choices Polls mentioned in the tweet
retweet tweet ratio Ratio between number of tweets and retweets
usersMentioned Number of actors mentioned in the tweet
hashtags count Number of hashtags mentioned in the tweet
16

Figure 7: Classification accuracy for each conceptual category under different classifiers with
the selected eight features for unhashed accounts (64%).
Appendix-C
Figure 8: Correlation matrix of the selected features.
17
