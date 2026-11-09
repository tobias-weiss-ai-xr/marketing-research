---
title: Application and Empirical Analysis of Fuzzy Neural Networks in Mining Social Media Users’ Behavioral
  Characteristics and Formulating Accurate Online Marketing Strategies
url: https://doi.org/10.1007/s44196-024-00675-6
category: social-media
subcategory: theory
date: 2024-11
venue: International Journal of Computational Intelligence Systems
authors:
- Beibei Luo
- Rongfei Luo
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44196-024-00675-6.pdf
pages: 15
chars: 71798
fetched_at: '2026-11-08T17:52:29+00:00'
kb_version: 1
---

# Application and Empirical Analysis of Fuzzy Neural Networks in Mining Social Media Users’ Behavioral Characteristics and Formulating Accurate Online Marketing Strategies

Vol.:(0123456789)
International Journal of Computational Intelligence Systems          (2024) 17:273
https://doi.org/10.1007/s44196-024-00675-6
RESEARCH ARTICLE
Application and Empirical Analysis of Fuzzy Neural Networks in Mining
Social Media Users’ Behavioral Characteristics and Formulating
Accurate Online Marketing Strategies
Beibei Luo1 · Rongfei Luo2
Received: 13 June 2024 / Accepted: 10 October 2024
© The Author(s) 2024
Abstract
In the current digital social environment, social media platforms have become an important position for user behavior insights
and precision marketing. User behavioral data on social media contain rich information, but they are often fuzzy, uncertain
and highly complex. Fuzzy neural network (FNN), as an advanced model combining fuzzy logic and neural network theory,
provides a powerful tool for processing and analyzing social media user behavioral features. This study is dedicated to
exploring the application of fuzzy neural networks in social media user behavior analysis and their key role in the design of
accurate online marketing strategies. We construct and optimize a fuzzy neural network model by meticulously classifying
and quantifying user behavioral features, including behavioral frequency features, content topic features, social interaction
features, and time series features, as well as applying fuzzy set theory to deal with fuzzy features such as emotional states.
Through empirical analysis, we will show how fuzzy neural networks can reveal the intrinsic laws behind user behaviors,
and how these insights can be used to design and implement precise online marketing strategies to improve advertising
effectiveness, user engagement, and brand loyalty.
Keywords Fuzzy neural network · Social media · User behavioral characteristics · Precise online marketing strategy
1 Introduction
With the rapid development of information technology and
the popularization of the internet, social media has become
an indispensable part of the daily life of users around the
world. According to statistics, the scale of global social
media users has exceeded billions, who share opinions,
exchange information, consume content and interact through
various social media platforms [ 1]. This active behavioral
data contains a wealth of valuable information on user pref-
erences, consumption habits, social influence, emotional
tendencies, etc., which provides marketers with a new way
to gain a deeper understanding of their users. Through the
in-depth study of social media user behavior, companies
can not only understand market trends and user needs, but
also use it to formulate marketing strategies that are more
relevant and targeted to consumers, thus enhancing brand
influence, increasing user stickiness, and promoting product
sales and business growth [2].
In the increasingly competitive environment of online
marketing, the traditional “one-size-fits-all” marketing strat-
egy has been difficult to meet the needs of both enterprises
and consumers. Precision Internet marketing aims to cus-
tomize and push the product and service information that is
highly suitable for users based on their personal characteris-
tics, interests, behaviors and other personalized information,
so as to achieve a higher advertising conversion rate and user
satisfaction [3]. However, realizing precision online market-
ing faces multiple challenges: how to effectively collect and
analyze massive user behavioral data; how to accurately por-
tray and predict user behavioral characteristics; and how to
develop and implement effective marketing strategies based
on these characteristics while respecting user privacy.
In Fig.  1, we can see a marketing model based on
machine learning. This model includes several key aspects,
such as user behavior, data, characterization, influence and
 * Beibei Luo
 luobeibei168@hotmail.com
1 New Media E-Commerce College, Chongqing Institute
of Engineering, Chongqing 400056, China
2 School of Humanities and Social Sciences, University
of Nottingham Ningbo, Ningbo 315100, China

 International Journal of Computational Intelligence Systems          (2024) 17:273
  273  Page 2 of 15
marketing. User behavior is the foundation of the entire mar-
keting model. By collecting and analyzing user behavioral
data, we can understand information, such as users’ prefer -
ences, needs and buying habits. This information is crucial
for developing effective marketing strategies. Data is the
key to drive machine learning. By processing and analyzing
large amounts of data, valuable features can be extracted and
used to train machine learning models. Characterization is
then the process of transforming the data into a format that
can be used by machine learning algorithms. In this process,
operations, such as cleaning, preprocessing, and transform-
ing the data, are required to ensure its quality and usability.
Next, impact refers to the influence of machine learning
models on marketing decisions. Using machine learning
models, user behavior can be predicted to optimize market-
ing strategies and improve marketing effectiveness. Finally,
marketing is the application of machine learning results to
actual marketing activities. For example, personalized ads
can be pushed or customized services can be provided based
on user behavioral data. Overall, the machine learning-based
marketing model is a new type of marketing that is user-
centered, data-driven, and uses machine learning as a tool. It
can help enterprises better understand users, more accurately
position the market, and more effectively promote products
and services in the fierce market competition. Fuzzy Neural
Network (FNN), as a kind of intelligent computing model
combining the advantages of fuzzy logic and neural network,
has a natural advantage for dealing with fuzzy, uncertain
and nonlinear complex problems. In fuzzy neural networks,
fuzzy logic empowers the system to deal with uncertainty
and ambiguity, while neural networks provide the model
with powerful learning and adaptive functions. Through
fuzzification and the learning iterations of neural networks,
fuzzy neural networks can better simulate and approximate
the complex relationships of user behavioral features, and
effectively mine the deep information hidden behind the
behavioral data. Specifically, a fuzzy neural network usu-
ally includes a fuzzification layer, a fuzzy rule layer and an
antifuzzification layer. This study focuses on using Fuzzy
Neural Network (FNN) [4], a hybrid intelligence model, to
deeply explore the complexity and diversity of user behav -
ioral features in social media, and to construct accurate
online marketing strategies based on the mined features. The
research aims to overcome the ambiguity and uncertainty of
traditional methods in dealing with user behavior data, and
to achieve efficient extraction and accurate prediction of user
behavioral features by constructing and optimizing a fuzzy
neural network model suitable for the social media environ-
ment. The ultimate goal is to help enterprises accurately
grasp market trends and user needs by scientifically ana -
lyzing user behavior patterns, and develop and implement
targeted and effective online marketing strategies to enhance
brand competitiveness and user satisfaction [5].
The challenges of precision online marketing are far
more complex than they seem. First, fragmentation of data
makes it difficult to build a complete user profile; second,
privacy regulations are increasingly stringent, limiting the
way data is collected and utilized; third, dynamic changes
in user preferences require marketing strategies to respond
quickly to market changes; and, technology is evolving rap-
idly, requiring continuous updating of the latest data analysis
tools and techniques. In response to these challenges, this
study focuses on how to use fuzzy logic and neural network
technology to improve the relevance and personalization of
marketing messages, aiming to optimize marketing effective-
ness through more accurate user behavior predictions.
The primary objective of this study is to develop a
comprehensive framework for understanding and predict-
ing user behavior across multiple dimensions using fuzzy
neural networks (FNNs). Specifically, the research aims
Fig. 1  Machine learning-based
marketing model
Characterization User Behavior
Data User
Merchandise Marketing
Implications
Machine
Learning Social
Media

International Journal of Computational Intelligence Systems          (2024) 17:273
 Page 3 of 15   273
to deeply explore the changing rules of user behavior by
analyzing short-term fluctuations and long-term trends,
seeking to uncover patterns and insights that can inform
marketing strategies. To capture the dynamic nature of user
behavior and its implications for marketing, the study uti-
lizes advanced techniques for data analysis, including time
series analysis, clustering algorithms, and fuzzy neural net-
works. Furthermore, the study aims to prevent overfitting
and enhance model generalization through the application
of L1 and L2 regularization techniques, thereby reducing
model complexity and improving the model's ability to gen-
eralize to unseen data.
The research includes (1) Theoretical foundation and
model construction: systematically introduce the basic
principles and advantages of fuzzy neural networks, design
and construct a fuzzy neural network model specifically for
social media user behavior feature mining. (2) Fuzzy neu-
ral network model training and optimization: use the con-
structed model to train and validate the preprocessed data,
and ensure that the model has good generalization ability
and feature mining effect through parameter adjustment
and model optimization. (3) Social media user behavioral
features mining: apply the optimized fuzzy neural network
model to deeply mine user behavioral features, reveal key
behavioral patterns, such as user preferences, social influ-
ence, and purchase intention, and explore their intrinsic laws
and correlations.
2  Literature Review
2.1  Current Research Status of Social Media User
Behavioral Characteristics
The study of social media users’ behavioral characteristics
is a hot topic at the intersection of information technology
and social sciences, attracting a large number of scholars
to explore in depth [6 ]. Early studies were laid down by
Boyd and Ellison, who defined the concept of social media
and initially explored the basic behavioral patterns of users
on their platforms. With the arrival of the big data era, the
analysis of user behavioral characteristics has become more
refined and diversified, launched a large-scale empirical
study on Twitter user behavior, revealing the characteris-
tics of user participation, frequency of information release,
and information diffusion patterns, and on the other hand,
focused on WeChat’s circle of friends and analyzed users’
content sharing behaviors and their motivations in the Chi-
nese social media environment. Basu et al. [7 ] studied the
self-presentation mode and community interaction charac-
teristics of users on YouTube and Twitter. With the help
of network science methods, we studied how user behavior
in social networks affects their status and influence in the
network. Chiang [8] explored how Instagram users express
emotions and construct identities through visual content.
In addition, Yang et al. [9 ] conducted a detailed analysis
of the social network construction process and behavioral
characteristics of MySpace users. In recent years, with the
continuous enrichment and improvement of the functions
of social media platforms, the study of user behavior has
also shifted from a single dimension to a diversified per -
spective. For example, Sithravel et al. [10] examined the
relationship between users’ information-seeking behavior
and information-sharing behavior on the microblogging plat-
form, and de Oña [11] studied the characteristics of users’
professional identity display and workplace social behavior
with respect to the LinkedIn professional social networking
site. At the same time, many studies began to pay attention
to the individual differences and psychological mechanisms
behind user behavior. Orzan et al. [12] found a close associa-
tion between social media usage habits and personality traits
through empirical studies; Moran et al. [13] explored how
anxiety and depressive symptoms affect adolescents’ online
social behavior on Facebook.
2.2  Application of Neural Networks in User
Behavior Analysis
The application of neural networks in the field of user behav-
ior analysis is becoming more mature, and its powerful non-
linear fitting ability and the advantages of automatic feature
learning have been widely recognized. In Chang et al.’s
study [14], a convolutional neural network (CNN) was used
to recognize handwritten digits, which opened the way for
neural networks to be used in the field of image recognition,
and this technique was subsequently applied to the analysis
of image or video data of user behavior.
In recent years, the application of deep learning tech-
niques in user behavior analysis has become more and more
common. Magdin et al. [15] used Deep Belief Network
(DBN) to model user browsing behavior and achieved accu-
rate prediction of user interests and preferences. Kokkodis
and Ransbothama [16] proposed a GRU4Rec model based
on recurrent neural network (RNN), which was successfully
applied to predict user behavior sequences in recommender
systems. In terms of social media user behavior analysis,
Peng et al. [17] constructed a deep neural network model,
which reveals user social relationship networks and infor -
mation dissemination patterns by analyzing user behaviors,
such as posting, liking and commenting on social media.
In addition, Caescu et al. [18] processed user behavio-
ral sequences using a long-short-term memory network
(LSTM), effectively predicting users’ future behavioral tra-
jectories and potential needs.
In addition to the above applications based on traditional
neural network architectures, there are some studies that

 International Journal of Computational Intelligence Systems          (2024) 17:273
  273  Page 4 of 15
try to incorporate Attention Mechanism (AM) to optimize
user behavior analysis models. Attention Mechanism was
first introduced by Magdin et al. [19] in a machine trans-
lation task, and since then, Liu et al. [20] applied Atten-
tion Mechanism to social media user sentiment analysis to
improve the accuracy and model interpretability of senti-
ment classification.
2.3  The Role of Fuzzy Logic in Uncertainty Data
Analysis
As a powerful tool for dealing with uncertainty, ambiguity
and subjective data, fuzzy logic has demonstrated its unique
application value in several fields since it was first proposed
in Ye et al.’s study [21]. In the field of user behavior anal-
ysis, fuzzy logic is especially suitable for those complex
behavioral features that are difficult to be described by pre-
cise numerical values. Kuo and Cheng [22] was the first to
apply fuzzy logic to decision support systems to deal with
the uncertainty of user preferences and decision-making
behaviors through fuzzy reasoning. Wang and Yang [23]
utilized fuzzy set theory to quantitatively analyze user sat-
isfaction and successfully overcame the difficulty of han -
dling fuzzy evaluation information in traditional satisfac-
tion survey methods. Thereafter, Zhang et al. [24] applied
fuzzy logic to the analysis of consumer shopping behavior in
the e-commerce environment, revealing the ambiguity and
uncertainty in the user’s purchase decision process. In terms
of social media user behavioral characterization, Cai et al.
[25] used fuzzy C-mean clustering (FCM) to classify user
behaviors, which effectively dealt with the ambiguity and
incompleteness of data. In addition, Zhang et al. [26] used
a fuzzy logic system to model user emotions and found that
fuzzy logic can more accurately capture and express users’
complex emotional states on social media. At the same time,
fuzzy logic was combined with machine learning algorithms
to improve the ability to handle uncertain data. Hodges
et al. [27] fused fuzzy logic with support vector machine
(SVM) for predicting users’ evaluation ratings of goods, and
achieved better prediction results than traditional methods.
Ando [28], on the other hand, constructed a deep learning
model based on fuzzy logic for analyzing and predicting the
attention behavior of social media users.
2.4  Shortcomings of Existing Research
and the Entry Point of Research in this Paper
Although existing studies have made significant progress in
social media user behavioral profiling and neural network
applications, there are still several pressing issues that need
to be addressed. First, existing neural network models tend
to ignore the ambiguity and uncertainty of user behaviors,
which may lead to limited accuracy and generalization
ability of model predictions in complex and changing social
media environments [29]. Second, most studies tend to treat
user behaviors as independent and discrete events and fail to
take full advantage of the continuity and correlation between
behaviors [30]. In view of the above research status quo, this
paper introduces fuzzy neural networks into social media
user behavioral feature mining, trying to deal with data
uncertainty through fuzzy logic, combined with the power -
ful learning ability of neural networks, to carry out in-depth
mining and comprehensive analysis of user behavioral fea-
tures. Specifically, the research entry points of this paper
mainly include (1) constructing a fuzzy neural network
model applicable to social media user behavioral data in
order to capture and deal with the vagueness and uncertainty
of the data; (2) investigating the efficacy of fuzzy neural
networks in revealing the complex relationship between user
behavioral features and the dynamic evolution law.
3  Rationale and Methodology
3.1  Theoretical Foundations of Fuzzy Neural
Networks
The proposed method, which uses membership function
to express sentiment tendency, is mainly used for senti -
ment classification at document level, which is indeed
different from the current trend of sentiment analysis at
sentence level and aspect level. However, this method can
provide macro-level sentiment trend analysis when dealing
with large amounts of text data and can effectively deal
with semantic ambiguity. This is important for the study
of online marketing topics: online marketing campaigns
generate a large number of user feedback, comments and
social media posts, which constitute a huge collection
of information. Data sources are wide and diverse, both
structured data and unstructured text. User attitudes and
preferences change with time and social events, resulting
in emotional tendencies evolving. User expressions are
often ambiguous and uncertain, such as sarcasm, irony
and other language phenomena, which increase the diffi-
culty of emotion analysis. In view of these characteristics
of online marketing data, document-level fuzzy sentiment
analysis methods can effectively meet the sentiment anal-
ysis needs of large-scale data sets. It can not only help
marketers quickly grasp the overall emotional trend, but
also solve the emotional classification problem caused by
vague user expression to some extent. In this way, market-
ing teams can understand the overall response of target
audiences in a short period of time and adjust market-
ing strategies accordingly to improve the effectiveness of
marketing campaigns. At the same time, this method can
also be used as a supplementary means, combined with

International Journal of Computational Intelligence Systems          (2024) 17:273
 Page 5 of 15   273
more detailed sentence level and aspect level sentiment
analysis, to provide more dimensional support for online
marketing strategies.
Fuzzy Neural Network (FNN) is an intelligent comput-
ing model that combines a fuzzy logic system (FLS) with a
neural network (NN). Its core concept lies in the introduc-
tion of fuzzy logic inference mechanism by fuzzifying the
input data in order to enhance the neural network’s ability
to process uncertain and fuzzy information.
In a typical fuzzy neural network, three main parts are
included: the Fuzzification Layer, the Fuzzy Inference
Layer and the Defuzzification Layer.
Fuzzy inference layer: based on predefined fuzzy
rules, fuzzy inference and fuzzy logic operations, such
as Max–Min synthesis and center of gravity method, are
performed to form fuzzy conclusions [31].
Defuzzification layer: the results obtained from fuzzy
reasoning are defuzzified, usually using the Center of
Gravity Method (Centroid Method), Maximum Member -
ship Method (Maximum Membership Method) and other
methods, and transformed into clear output signals.
3.2  User Behavior Characteristics Selection
and Quantification Methods
The selection of user behavioral characteristics plays a
crucial role in constructing user behavioral analysis mod -
els in the social media environment. These features can
comprehensively reflect the characteristics of users’ online
activities from multiple dimensions, mainly covering the
following four categories [32]:
(1) Behavioral Frequency Characteristics: These char -
acteristics quantify the intensity of a user’s activities and
the degree of activity during a certain time interval, such
as the number of posts (Post_count_daily), the number of
likes (Like_count_daily), and the number of comments
(Comment_count_daily). These variables can usually be
calculated by statistical methods. Specifically as shown
in Eq. (1 ).
where T represents the total number of days in the observa-
tion period, and Post_countt represents the post count on
day t.
(2) Content topic features: These features focus on the
core information and tendency of the content posted by
users, such as the topic score obtained after analyzing the
text content using a topic model (e.g., Latent Dirichlet Allo-
cation LDA) or the frequency of keyword appearances. Tak-
ing the keyword “AI” as an example, the frequency of its
appearance in all user posts can be expressed by Eq. (2).
(1)Post_count_avg = 1 T /uni2211.s1T t=1 Post_countt
(3) Social interaction characteristics: This category
describes a user’s social network attributes and level
of engagement, and may include the number of friends
( Friend_count ), community activity ( Group_activity ), and
an index that measures a user’s influence ( Inﬂuence_index ).
For example, the influence index may take into account fac-
tors such as the number of followers, the number of times
a user has been retweeted or quoted, etc., and can be calcu-
lated by weighted summation [33].
(4) Time series features: such features reveal the
time pattern of user behavior, such as user active
hours ( Activity_period ) and cyclical behavior pat-
terns ( Cyclic_behavior pattern  ). Using time series
analysis tools, we can extract metrics such as peak
active hours ( Hourly_peak_activity ), defined as
Hourly_peak_activity = arg max h(Activity_counth) . Here,
Activity_counth denotes the count of user activity at the hth
hour.
During the implementation of precision marketing strat-
egies, fuzzy characteristics that are difficult to measure
directly and quantitatively are often encountered, such as
users’ emotional states, satisfaction ratings, and many other
subjective factors. These fuzzy characteristics are crucial
for understanding user needs and preferences, but are dif -
ficult to handle in traditional data analysis methods. For this
reason, fuzzy set theory and its derived fuzzy mathematical
methods provide powerful tools to effectively quantify such
fuzzy features [34].
Take the user’s emotional tendency as an example, it is a
subjective and diversified psychological state, with various
forms of expression, including but not limited to “happy”,
“sad”, “angry”, “surprised” and other emotions, “surprise”
and other emotions. It is difficult to accurately portray this
complex and multi-dimensional emotional space by the con-
ventional binary logic system. Fuzzy set theory, on the other
hand, introduces the concept of degree of affiliation, which
allows an element to both belong and not belong to a certain
set to a certain extent, and this extent is the degree of affilia-
tion. Specifically, in fuzzy sentiment analysis, we can build
a collection of sentiment words and assign a different affilia-
tion function for each sentiment. For example, for a sentence
or a user comment, “I am happy”, we can map it to the senti-
ment category of “happy” by fuzzy sentiment analysis, and
assign it a certain affiliation value, e.g., 0.85, which means
that this comment expresses “happy” to a large extent. This
means that this comment expresses the sentiment tendency
of “happy” to a large extent. Assuming that we have a senti-
ment set E = {happy, sad, neutral, angry}, for any user com-
ment U [35], its sentiment tendency can be represented by
the affiliation function 𝜇U (Ei) , where Ei is an element of
(2)Keyword_freqAI = CountAI Total_word_count

 International Journal of Computational Intelligence Systems          (2024) 17:273
  273  Page 6 of 15
the sentiment set. For example, 𝜇U (happy)=0.85  indicates
that the sentiment affiliation of “happy” in comment U  is
0.85. The fuzzy sentiment analysis model obtained from
the training dataset can automatically calculate the affilia-
tion values of various sentiments in any new user feedback,
thus converting the originally unquantifiable fuzzy senti-
ment characteristics into actionable data indicators, which is
extremely important for the design and adjustment of preci-
sion marketing strategies. This is of great practical value for
the design and adjustment of precision marketing strategies.
In this way, marketers can formulate personalized promotion
plans and optimize user experience based on the quantita-
tive results of users’ emotional tendency in a more scientific
and reasonable way, thus enhancing the effect of marketing
activities and user satisfaction. In this way, the application
of fuzzy set theory and its related technology in the field
of precision marketing greatly expands the possibility and
depth of data-driven decision-making [36].
3.3  Handling of Uncertainty Characterization
In the process of social media user behavior analysis
and precise online marketing strategy development, user
behavior characteristics are often accompanied by differ -
ent degrees of uncertainty. These uncertainties may arise
from the subjectivity of user behavior, the incompleteness
of data collection, and the difficulty of predicting behav -
ioral trends. Fuzzy Neural Network (FNN) shows great
potential in mining and parsing such features by virtue of
its ability to handle vagueness and uncertainty well. As
shown in Fig. 2, in order to deal with uncertain features in
social media data, we can construct a Fuzzy Neural Network
(FNN) that combines the advantages of fuzzy logic and neu-
ral networks. First, by designing appropriate fuzzy member-
ship functions, the vague and uncertain features in social
media can be quantitatively described and transformed into
affiliation values. Then, these fuzzified features are input
into the neural network for training and learning, and the
fuzzy neural network can adaptively adjust according to the
fuzzy characteristics of the input data, and gradually extract
and learn the patterns and rules inherent in the data and
related to uncertainty. Finally, after multi-layer nonlinear
transformation and optimization, the fuzzy neural network
can achieve effective characterization and modeling of the
original uncertain features, so as to convert the fuzzy data
into a relatively specific and easy to understand and process
form [37].
Facing the fuzzy features, such as user satisfaction, inter-
est preference, etc., fuzzy neural networks are quantized by
defining fuzzy affiliation functions. In real life, people’s
judgment and decision-making often rely on fuzzy concepts,
such as good or bad, high or low, big or small. These fuzzy
features are difficult to deal with by traditional numerical
methods, and fuzzy neural networks provide an effective
solution for this. For the fuzzy set A  to which feature x
belongs, its degree of affiliation can be expressed in the form
of Sigmoid function or Gaussian function, etc. Specifically
as shown in Eqs. (3) or (4).
where α and c represent the slope and center position of
the Sigmoid function, respectively, and 𝜎 is the standard
deviation of the Gaussian function. Based on the fuzzified
features, a fuzzy rule base is constructed, such as “If the
user’s activity is high and the frequency of interaction is
moderate, his/her purchase intention may be stronger”. In
the fuzzy neural network, the former part of the fuzzy rules
combines the affiliation degree of each feature through the
“and” operation (taking the minimum value), and the lat-
ter part combines the outputs of all the rules through the
(3)𝜇A(x)= 1 1 + e−𝛼(x−c)
(4)𝜇A(x)= e− (x−c)2 2𝜎2
Fig. 2  Processing flow of uncer-
tain features
Fuzzy features
Interest
Preferences
User
Satisfaction
Input
Implicit
Outputs
Decision
Output

International Journal of Computational Intelligence Systems          (2024) 17:273
 Page 7 of 15   273
“or” operation (taking the maximum value). Specifically as
shown in Eq. (5).
where Wi represents the result of synthesis of the anteced-
ent part of the i th fuzzy rule, ui is the result of aggregation
of the conclusion part of all the rules, m  is the number of
fuzzy rules and n is the number of input features. The results
obtained from fuzzy reasoning need to be converted into
clear decision outputs through defuzzification operations. A
commonly used defuzzification method is Centroid Defuzzi-
fication, which is calculated as Eq. (6). ui denotes the center
value of the output region corresponding to rule i [38].
4  Fuzzy Neural Network Model Construction
and Optimization
4.1  Fuzzy Neural Network Model Architecture
Design
Fuzzy Neural Network (FNN), as a hybrid model integrating
fuzzy logic and neural network, shows unique advantages in
dealing with user behavior analysis, which is a problem with
significant fuzzy and nonlinear characteristics. Its basic archi-
tecture mainly consists of the following core components:
(1) Input layer: The fuzzy neural network first receives the
preprocessed user behavior feature vector X =[ x1, x2, … , xn] .
Each feature xj is converted to an affiliation value in the cor-
responding fuzzy set A by the affiliation function (𝜇A(xj) . For
example, the Sigmoid function is used as the affiliation func-
tion: 𝜇A(xj)= 1 1+e−𝛽j (xj −cj ) . Here, 𝛽j is the slope parameter of the
affiliation function and cj is the center value of the fuzzy set.
The fuzzification layer is responsible for mapping the clear
input features to the fuzzy space to achieve the transformation
from determinism to fuzziness. The fuzzy rule layer performs
fuzzy logic reasoning to construct and execute a series of fuzzy
rules. For each fuzzy rule, its antecedent part is formed by
combining the affiliation degree of each input feature by the
“and” (AND) operation, and the conclusion part aggregates
the outputs of all rules by the “or” (OR) operation. The simpli-
fied representation is as Eq. (7) [39].
(2) Where Wi represents the synthesis result of the ante-
cedent part of the i th fuzzy rule, Zi is the aggregation result
(5)Wi =
n
min
j=1
𝜇Aij (xj), Zi =
m
max
i=1
Wi
(6)̂Y =
∑m
i=1 Zi ⋅ ui
∑m
i=1 Zi
(7)Wi =
n/uni220F.s1
j=1
𝜇Aij (xj), Zi =
m/uni2211.s1
i=1
Wi
of the conclusion part of all rules, and m represents the total
number of fuzzy rules. The defuzzification process aims to
convert the fuzzy conclusions output from the fuzzy infer -
ence layer into clear real-valued predictions. A common
defuzzification method such as the center of gravity method
is expressed by the Eq. (8). ui is the output center value cor-
responding to the i th fuzzy rule. It is worth noting that the
design of the fuzzy neural network also includes the opti-
mized setting of the fuzzy affiliation function parameters,
such as 𝛽j and cj , as well as the strength of the fuzzy rules,
so that the model can be flexibly adapted to different user
behavioral characteristics and their correlations [40].
4.2  Fuzzy Sentiment Analysis Model Architecture
We propose a pioneering fuzzy sentiment analysis model
architecture that deeply integrates the authoritative knowl-
edge base of sentiment dictionaries, rigorous fuzzy logic
inference mechanisms, advanced natural language process-
ing techniques, and powerful deep learning algorithms,
aiming to solve the subjectivity and vagueness problems
prevalent in social media data, and to transform them into
quantitative information that can be metricated and ana-
lyzed, which is specifically shown in Fig. 3.
In order to improve the applicability and scalability of
fuzzy neural network (FNN) models across different social
media platforms or user demographics, the research frame-
work is designed with the following philosophy: social
media data often contains multiple types of information,
such as text, images, and geographic locations. Therefore, it
is critical to employ multimodal fusion methods to combine
these different types of data. This helps capture informa-
tion in different dimensions, which improves the predictive
power of the model. In order to make the most of data from
different sources, different weights can be assigned accord-
ing to their reliability and relevance, and these weights
can be automatically determined by expert evaluation or
machine learning algorithms. Considering the growth rate
of the dataset, a dynamic fusion mechanism was designed to
update the data fusion model periodically to reflect the latest
data trends and developments. This design not only enhances
the generalization ability of the model, but also improves its
ability to handle growing data volumes.
Recent advances in fuzzy sentiment analysis modeling have
incorporated a variety of innovative techniques and mathemat-
ical representations aimed at achieving efficient capture and
quantification of rich sentiment information in unstructured
textual data. Here, we briefly describe an innovative fuzzy sen-
timent analysis framework that combines sentiment lexicon,
(8)̂Y =
∑m
i=1 Zi ⋅ ui
∑m
i=1 Zi

 International Journal of Computational Intelligence Systems          (2024) 17:273
  273  Page 8 of 15
fuzzy logic, natural language processing, and deep learning
techniques with appropriate formulae illustrations.
Suppose there is a text T that can be decomposed into a
sequence of words W ={ w1, w2, … , wn} , and each word wi
has a sentiment vector Vi ∈ ℝ3 based on a sentiment diction-
ary, where the three dimensions correspond to positive senti-
ment E+ , negative sentiment E− and neutral sentiment E0 .
For the word wi , its sentiment vector element Vi(j) denotes
its initial sentiment intensity on the sentiment dimension Ej ,
which can be obtained by querying the pre-trained sentiment
lexicon, and can be further adjusted by the fuzzy affiliation
Eq. (9).
For the interactions between words and contextual effects,
fuzzy association rules or phrase structure trees are intro-
duced to correct the sentiment intensity of individual words.
For example, considering the contextual effects of the com-
bination of two consecutive words wi and wi+1 , a fuzzy syn-
thesis function F ∶ ℝ3 × ℝ3 → ℝ3 can be established, which
can be of the Eq. (10).
where 𝛼 and 𝛽 are weight parameters and 𝜙(wi, wi+1) is a
mapping function representing the gain or loss of a word
pair due to collocation on a particular sentiment dimension.
The computation of the overall sentiment tendency of
a text can be achieved by a weighted fuzzy aggregation
approach, e.g., using an attention mechanism to weight the
sentiment vectors of individual words to give the overall sen-
timent score of the text on each sentiment dimension S(Ej) .
Specifically as shown in Eq. (11).
Here,ai is the attention weight of the word wi , computed
by a context-dependent scoring function ei , which usually
(9)𝜇 ∶ W × E → [0, 1] to make 𝜇(wi, Ej)=V i(j)
(10)
V� i,i+1(j)=F (Vi, Vi+1)(j)=( 1 − 𝛼)Vi(j)+ 𝛼Vi+1(j)+ 𝛽𝜙(wi, wi+1)
(11)S(Ej)=
n�
i=1
ai ⋅ 𝜇(wi, Ej) ai = exp(ei) ∑n
k=1 exp(ek)
involves a dot product or convolution operation of word
embeddings. Further, we adopt a deep learning framework
where the model can be designed as an end-to-end fuzzy
sentiment analyzer that automatically learns sentiment fea-
tures through a multi-layer neural network:
H = f (W, 𝜃) S(Ej)=g(H )j . Among them, f is an encoder
network, which can be a recurrent neural network (RNN), a
long-short-term memory network (LSTM), or a transformer,
which maps the word sequences to the high-level abstract
feature space to obtain H. g is a sentiment decoder network,
whose output S(Ej) directly reflects the probability distribu-
tion of the text on the sentiment dimension Ej.
4.3  Model Training and Parameter Tuning
During the training process of the fuzzy neural network
model, various advanced machine learning strategies are
adopted to improve the model performance and generaliza-
tion ability, including gradient descent method for parameter
updating, cross-validation to ensure the model robustness
and grid search to achieve hyper-parameter preference.
Gradient descent is a widely used and effective means
of parameter updating for fuzzy neural networks. In the
network training phase, we first calculate the gradient of
the loss function with respect to each learnable parameter
(including the affiliation function parameter 𝛽j and the center
value cj , as well as the possible connection weights). Subse-
quently, these parameters are gradually adjusted following
the negative direction of the gradient until a local minima is
reached or a predefined termination condition is satisfied. A
typical gradient update step can be represented as Eq. (12).
where 𝜂 is the learning rate, which controls the magnitude
of parameter changes in each iteration, and E  is the overall
loss function over the entire training set.
(12)𝛽j ← 𝛽j − 𝜂 𝜕E 𝜕𝛽j cj ← cj − 𝜂 𝜕E 𝜕cj
Fig. 3  Fuzzy sentiment analysis
model architecture

International Journal of Computational Intelligence Systems          (2024) 17:273
 Page 9 of 15   273
Cross-validation is an important means to assess the gen-
eralization ability of a model and prevent overfitting. In the
training process of fuzzy neural networks, we can implement
K-fold cross-validation, i.e., the original dataset is divided
into K mutually exclusive subsets, and one of the subsets is
sequentially selected as the test set, and the rest of the sub-
sets are used as the training set, and the process is repeated
for K times in order to obtain the model’s performance index
under different divisions. By observing the average perfor -
mance under different divisions, the most stable model struc-
ture and parameter settings can be selected, and this paper
adopts the method of cross-validation to verify the effective-
ness of the model, and its process is specifically shown in
Fig. 4. Grid search is a method of systematically travers-
ing the hyper-parameter space to find the optimal combina-
tion. In a fuzzy neural network model, the hyperparameters
involved may include, but are not limited to, the learning
rate, the shape parameter of the affiliation function, the num-
ber of fuzzy rules, the strength of regularization, and so on.
Grid search will define a grid of hyper-parameter values and
train independent model instances for each combination of
hyperparameters, and select the optimal set of hyperparam-
eters by comparing the performance on the validation set.
In order to deeply explore the changing rules of user
behavior and its influence on marketing strategy, we will
adopt multi-dimensional method to analyze. First, short-
term fluctuation analysis is used to identify daily or weekly
patterns of user behavior in the time dimension, such as
distinguishing between weekdays and weekends; sec-
ond, long-term trend analysis is used to gain insight into
annual or quarterly trends in user behavior with the help of
time series analysis techniques such as ARIMA models or
seasonal decomposition. In addition, in-depth research will
be conducted through changes within user groups, clustering
algorithms will be used to segment user groups, and differ -
ences in behavior patterns between groups will be identi-
fied, such as product preferences of users of different ages.
Combining fuzzy neural networks to simulate uncertainty in
user behavior changes, and using time series analysis meth-
ods to capture long-term trends and short-term fluctuations
in user behavior, these analyses not only help companies
respond quickly to market changes, but also provide a solid
data base for their long-term strategy development, and
ultimately achieve more accurate target market positioning
and more forward-looking marketing strategy planning to
improve their market adaptability and customer satisfaction.
To prevent overfitting of the model, L1 or L2 regulariza-
tion techniques can be used to limit the size of the model
parameters, thereby reducing the complexity of the model.
L1 regularization tends to produce sparse weight vectors,
which are helpful for feature selection, while L2 regulariza-
tion smooths the model by penalizing large weight values to
avoid overfitting caused by excessive parameters. The choice
of regularization parameter (λ) is crucial, which determines
the extent to which the regularization term affects the loss
function. In order to find the optimal regularization param-
eter values, cross-validation methods can be used. In this
process, the data set is divided into several mutually exclu-
sive subsets, the model is trained and validated on different
subsets, and the parameter minimizing the validation error
is selected as the optimal value by comparing the validation
errors under different regularization parameters. This strat-
egy can not only effectively prevent the model from overfit-
ting, but also improve the generalization ability of the model
on unknown data.
5  Empirical Analysis and Presentation
of Results
5.1  Example of Application of Fuzzy Neural
Networks in User Behavioral Feature Mining
In order to ensure the reliability and repeatability of the
experimental results, this study uses a real user behavior
dataset from a well-known e-commerce platform. This
dataset covers user activity records from January 2022 to
December 2023, including user browsing history, purchase
history, click rate and feedback evaluation. An example may
include fields for a user's unique identifier (e.g., user ID),
visit time, stay time, item ID purchased, and whether the
purchase was completed. To maintain consistency and rep-
resentativeness of the dataset, we split the dataset into train-
ing and testing sets according to chronological order, with
70% of the data used for model training and the remaining
Parameter Dataset
Cross-
vaildation Training data Test data
Best
parameter
Retrained
model
Final
evaluation
Fig. 4  Cross-validation process

 International Journal of Computational Intelligence Systems          (2024) 17:273
  273  Page 10 of 15
30% used for model testing. This partitioning ensures that
the model can accurately learn time series features of user
behavior and can effectively evaluate model performance on
unseen data. In this way, we can not only ensure the accuracy
of experimental results, but also improve the transparency
and verifiability of research results.
This study is based on the analysis of an anonymous user
behavior dataset provided by an internationally renowned
social media platform, which covers the detailed behavioral
records of more than 100,000 users over a period of time,
including but not limited to the basic information of users
(e.g., age, gender, geographic location, etc.), their daily
activity (e.g., daily online hours, frequency of posts, etc.),
their interactive behaviors (e.g., likes, comments, shares,
etc.), and multifaceted characteristics, such as content origi-
nality and coherence of areas of concern, with specific data
description information shown in Table 1.
Before performing the analysis, the necessary preprocess-
ing of the raw data was first carried out, including the steps
of data cleaning, missing value filling, outlier processing,
and feature standardization. Then, the quantified user behav-
ioral features are converted to the affiliation degree of fuzzy
set by fuzzy affiliation function, for example, the fuzzifica-
tion of the user’s online duration can be expressed
as:𝜇Online(t)= 1 1+e−𝛼(t−t0 ) where t represents the online duration
of the user,𝛼 is the slope parameter of the affiliation function,
and t0 is the threshold value for defining “long time online”.
5.2  User Behavior Feature Distribution and Pattern
Recognition Results
In this study, we conducted an in-depth distributional analy-
sis of user behavioral features and revealed the intrinsic cor-
relation patterns among the features by means of correlation
coefficient matrix, user interaction behavior index construc-
tion, and fuzzy inference.
In order to deeply explore the intrinsic correlation
between user behavioral characteristics, we performed
Pearson correlation coefficient analysis on all continuous
variables and compiled an exhaustive correlation coefficient
matrix to visualize the degree of linear dependence between
these characteristics. We take user online time and posting
frequency as an example to illustrate the calculation method.
In order to investigate the relationship between user online
time OnlineTime and posting frequency, we calculated the
Pearson correlation coefficient between them as shown in
Eq. (13).
Table 2 shows the Pearson’s correlation coefficient matrix
of the eight user behavioral characteristics that were care-
fully calculated. 1–8 in Table  2 represent geographic loca-
tion, daily online hours, posting frequency, total number of
likes, total number of comments, total number of shares,
percentage of content originality, and consistency score of
areas of interest, respectively. There is a significant positive
correlation (0.89) between daily online time and posting fre-
quency (serial numbers 2 and 3), indicating that the longer a
user is online, the more likely he or she is to post. The total
number of likes (Serial No. 4) shows a degree of positive
correlation with the total number of comments (Serial No.
5) and the total number of shares (Serial No. 6), reflecting
the fact that users’ activity on social media is consistent with
their interactive behavior, i.e., the higher the degree of users’
participation in interactions, the higher the likelihood that
they will like, comment on and share. There is a positive
correlation (0.45) between the percentage of content origi-
nality (ordinal number 7) and the consistency score of the
area of interest (ordinal number 8), implying that users with
a high level of originality are likely to be more active and
consistent in their area of interest. The correlation between
(13)
r =
∑N
i=1 (OnlineTimei − OnlineTime)(PostingFrequencyi − PostingFrequency) /uni221A.s1∑N
i=1 (OnlineTimei − OnlineTime)2 ∑N i=1 (PostingFrequencyi − PostingFrequency)2
Table 1  Description of data
Serial number Feature name Data type Sample data
1 User ID String (computer science) User A001
2 (A person’s) age Numeric (integer) 25
3 Distinguishing between the sexes Form Male/female/other
4 Geographic location Copies Beijing, capital of People’s Republic of China
5 Daily online hours Numeric (floating point) 120.5 (minutes)
6 Posting frequency Numeric (integer) 15 (number of posts per day)
7 Total number of likes Numeric (integer) 1200 (cumulative number of likes)
8 Total number of comments Numeric (integer) 50 (cumulative number of comments)
9 Total number of shares Numeric (integer) 20 (cumulative number of shares)
10 Proportion of content originality Numerical value (percentage) 70% (percentage of original content)
11 Area of Concern Coherence Score Numeric (floating point) 0.85 (consistency score)

International Journal of Computational Intelligence Systems          (2024) 17:273
 Page 11 of 15   273
geographic location (serial number 1) and several other user
behavioral characteristics is weak, indicating that geographic
location has relatively little influence on users’ behavioral
performance on social media. Through in-depth analysis of
the correlation coefficient matrix in Table  2, we can better
understand the intrinsic connection between user behavio -
ral characteristics, which is crucial for the development of
accurate online marketing strategies, such as more targeted
promotional activities for highly interactive and original user
groups. At the same time, this also provides valuable clues
for further research on user behavior patterns and enhancing
user activity.
(1) Analysis of users’ interactive behavior and social influ-
ence: Considering the interactive behavior characteristics of
users’ TotalLikes, TotalComments and TotalShares, we quan-
tify users’ social influence by constructing a Weighted Inter-
action Index (WII): SocialInﬂuenceIndex = wL ⋅ TotalLikes
+ wC ⋅ TotalComments + wS ⋅ TotalShares . We constructed
the Weighted Interaction Index to quantify the social influ-
ence of users. Among them, wL , wC and wS are the weight-
ing factors of liking, commenting and sharing behaviors,
respectively. The analysis results show that users with higher
interaction index have more social influence on the platform.
(2) Analysis of the association between content
originality and activity: We use fuzzy inference to
study the relationship between the content original-
ity ratio OriginalityRatio and activity. Assuming that
user activity ActivityLevel is determined by online
length and posting frequency, the fuzzy inference rule
can be expressed as: IF Originality Ratio is Relatively
High THEN Activity Level is High  . According to the infer-
ence results of fuzzy neural network, it is found that users
with higher originality tend to have higher activity.
5.3  Accurate Online Marketing Strategy Design
Based on Mining Results
Based on the fuzzy neural network in-depth analysis of the
distribution of social media user behavioral features and the
identified typical patterns, we effectively designed a set of
refined online marketing strategies, as shown in Fig. 5.
First, we implement targeted promotion strategies, target-
ing user groups that show high activity, outstanding content
originality and frequent interactive behavior, and accurately
delivering product and service information that meets their
interests and preferences. We aim to maximize the click-
through rate and conversion efficiency of our advertise-
ments, so that our marketing resources can be accurately
deployed and maximize their effectiveness.
Second, we actively seek cooperation with users with
strong social influence on social media, encouraging them
to create original content in line with the brand image, and
using their fan base and influence to spread, attracting the
attention and participation of more potential consumers, cre-
ating a word-of-mouth effect, thus strengthening the brand’s
popularity and recognition in the market. At the same time,
we adopt a time-sensitive marketing strategy that scientifi-
cally arranges the release time of advertisements based on
the statistics of users’ active hours to ensure that the adver -
tisements are online during the hours when users are the
most active and receptive to information, thus effectively
increasing the exposure rate of the advertisements and the
browsing experience of users, and further strengthening the
effect of the brand’s message delivery. Finally, we focus on
personalized content recommendation, providing custom-
ized content recommendation services for each user based
on the consistency of their areas of interest. The aim is to
cultivate users’ lasting interest, stimulate their continuous
attention and participation in the brand, and ultimately turn
them into loyal advocates and consumers of the brand, so as
to stabilize and expand market share.
5.4  Strategy Validation and Comparative Analysis
This subsection aims to systematically track and validate
the effects generated by the implementation of the pro -
posed precision online marketing strategies and assess their
effectiveness by comparatively analyzing the performance
of different strategies, and will also explore the advantages
Table 2  Correlation analysis
matrix Serial number 1 2 3 4 5 6 7 8
1 1.00 0.65 − 0.32 0.47 − 0.19 0.70 − 0.08 0.53
2 0.65 1.00 0.89 − 0.05 0.72 − 0.23 − 0.56 0.38
3 − 0.32 0.89 1.00 0.54 − 0.02 − 0.75 0.61 − 0.10
4 0.47 − 0.05 0.54 1.00 0.81 0.49 − 0.01 0.29
5 − 0.19 0.72 − 0.02 0.81 1.00 0.56 0.15 − 0.67
6 0.70 − 0.23 − 0.75 0.49 0.56 1.00 0.23 − 0.31
7 − 0.08 − 0.56 0.61 − 0.01 0.15 0.23 1.00 0.45
8 0.53 0.38 − 0.10 0.29 − 0.67 − 0.31 0.45 1.00

 International Journal of Computational Intelligence Systems          (2024) 17:273
  273  Page 12 of 15
demonstrated by the fuzzy neural network model in the strat-
egy formulation process.
5.4.1  Precision Marketing Strategy Implementation
and Effectiveness Tracking
Table 3 shows the changes in key performance indicators
(KPIs) after the implementation of the targeted promo-
tion strategy. Table 3 tracks the changes in four KPIs, user
activity, ad click rate, conversion rate, and user satisfaction,
before and after the implementation of the targeted promo-
tion strategy. The results show that user activity increased
by 13.5 percentage points after implementation, ad click
rate and conversion rate increased by 1.4 and 0.6 percent-
age points respectively, and user satisfaction also increased
by 0.4 points, indicating that the strategy has a significant
promotion effect on user engagement and purchase intention.
Table 4 shows the impact of the social influence market-
ing strategy on the number of cooperative users, the number
of new followers, the number of content shares, and the
interaction rate. After implementation, the number of coop-
erative users doubled, the number of new followers nearly
tripled, the number of content shares doubled, and the inter-
action rate increased by 14.5 percentage points, reflecting
the strategy’s remarkable effectiveness in expanding brand
influence and increasing community activity.
5.4.2  Comparative Analysis of the Effectiveness of Different
Strategies
In order to visually compare the differences in effectiveness
between the strategies, Table  5 summarizes the combined
performance of the strategies over the specified period.
Table 5 carries out a comparative analysis of the three
core dimensions of ROI improvement, customer retention
rate improvement and new user acquisition cost reduction
of different marketing strategies. Among them, the targeted
promotion strategy shows a strong advantage in ROI and
Fig. 5  Framework for a refined
online marketing strategy
Internet
Marketing
Strategy
Regular Promotion
User Collaboration
Time-sensitive marketing
Focuso np ersonalized
content
recommendations
Table 3  Tracking the
effectiveness of the
implementation of the targeted
promotion strategy
Strategy phase Increase in user
activity (%)
Advertisement click-
through rate (%)
Conversion rate
(%)
User
satisfaction
rating
Pre-implementation 65.0 2.8 1.5 3.2
Post-implementation 78.5 4.2 2.1 3.6
Table 4  Social influencer
marketing strategy
implementation effectiveness
tracking
Strategy phase Number of coopera-
tive users
Number of new
followers
Number of content
shares
Increase in
interaction rate
(%)
Pre-implementation 10 500 1500 10.5
Post-implementation 20 1200 3000 25.0

International Journal of Computational Intelligence Systems          (2024) 17:273
 Page 13 of 15   273
new user acquisition cost reduction, while the social influ-
ence strategy is more prominent in customer retention rate
improvement; personalized recommendation and time-sensi-
tive strategy have different degrees of growth in each index,
but relative to the other two strategies, the effect is slightly
weaker in some aspects.
Table 6 focuses on the value enhancement of fuzzy neural
network model in precision marketing. From user segmen-
tation to behavior prediction, the application of the model
increases the segmentation accuracy by 10% and the pre-
diction accuracy by 10%; in terms of marketing resource
allocation, the model helps significantly increase the click
rate and conversion rate of advertisements and effectively
optimize the use of the budget. In addition, the iteration
period of strategy optimization is shortened and the accuracy
is improved, and the accuracy rate of detecting abnormal
behaviors is also significantly increased, thus comprehen-
sively strengthening the precision, timeliness, and security
of the marketing strategy. In addition, the strategy optimiza-
tion iteration cycle was shortened and its accuracy improved,
and the accuracy of abnormal behavior detection increased
significantly.
Through the above comparison, it can be seen that the
application of fuzzy neural network model in the formulation
of precision marketing strategy not only improves the accu-
racy of user segmentation and portrait construction, but
also enhances the prediction ability of future user behav -
iors, which achieves a more effective allocation of market-
ing resources and faster iterative optimization of strate-
gies. At the same time, the model also shows significant
improvement in abnormal behavior detection, which helps
to improve the security and efficiency of the overall market-
ing activities.
6  Conclusion
In this study, we have explored the use of fuzzy neural net-
works (FNNs) in mining user behavioral features from a
large-scale, anonymous dataset provided by an internation-
ally renowned social media platform. The dataset includes
detailed behavioral records of over 100,000 users over a spe-
cific period, encompassing various aspects, such as demo-
graphics, daily activity, and interactive behaviors.
The empirical analysis was conducted in two main parts:
the application of FNNs in user behavioral feature mining
and the distribution and pattern recognition of user behavior
features.
Table 5  Comparative analysis
of the effect of different
strategies
Marketing strategy ROI improve-
ment (%)
Increase in customer
retention rate (%)
Lower cost of new
user acquisition
(%)
Targeted promotion 30 15 20
Social influence 25 20 15
Time-sensitive 18 10 12
Personalized Recommendations 22 18 18
Table 6  Proof of advantages of fuzzy neural network models in strategy formulation
Serial
num-
ber
Model application areas Performance of traditional methods before
fuzzy neural networks
Improved performance after application of
fuzzy neural networks
1 User segmentation and profile building User segmentation accuracy is 75%, portrait
construction is rough
User segmentation accuracy of 85%, portrait
construction refinement, able to capture
subtle behavioral patterns
2 User behavior prediction 60% accuracy in predicting user activity for
the coming week
Prediction accuracy increased to 70% with
more stable prediction results
3 Allocation of marketing resources 10% increase in ad click-through rate and 5%
increase in conversion rate
15% increase in ad click-through rate, 8%
increase in conversion rate, 15% increase in
marketing budget utilization
4 Strategy optimization iteration Strategy optimization cycle is monthly and
slow to respond
Enables weekly or even daily strategy fine-
tuning with fast response times and enhanced
real-time performance
5 Abnormal behavior detection Abnormal behavior recognition accuracy of
70%, more false alarms
Improvement of abnormal behavior recognition
accuracy to 85%, reducing false alarms and
improving risk control capabilities

 International Journal of Computational Intelligence Systems          (2024) 17:273
  273  Page 14 of 15
To ensure the reliability and repeatability of the experi-
mental results, we used a real user behavior dataset from
a well-known e-commerce platform covering user activ -
ity records from January 2022 to December 2023. The
dataset included user browsing history, purchase history,
click rates, and feedback evaluations. An example instance
might include fields, such as a user's unique identifier (e.g.,
user ID), visit time, stay time, item ID purchased, and
whether the purchase was completed. The dataset was split
into training and testing sets according to chronological
order, with 70% of the data used for model training and the
remaining 30% used for model testing. This partitioning
ensured that the model could accurately learn time series
features of user behavior and could effectively evaluate
model performance on unseen data.
We conducted an in-depth distributional analysis of user
behavioral features and revealed the intrinsic correlation
patterns among the features. Through Pearson correlation
coefficient analysis, we compiled an exhaustive correla-
tion coefficient matrix to visualize the degree of linear
dependence between these characteristics. For example,
there was a significant positive correlation (0.89) between
daily online time and posting frequency, indicating that
the longer a user is online, the more likely they are to
post. Additionally, the total number of likes showed a
degree of positive correlation with the total number of
comments and the total number of shares, reflecting the
fact that users' activity on social media is consistent with
their interactive behavior.
The analysis also showed a positive correlation (0.45)
between the percentage of content originality and the con-
sistency score of the area of interest, suggesting that users
who produce more original content tend to have a more
coherent focus in the topics they engage with.
The findings of this study demonstrate the effectiveness
of using fuzzy neural networks in capturing the complex and
nuanced patterns present in user behavior data. The deep
exploration of user behavior patterns through time series
analysis, correlation analysis, and the integration of fuzzy
logic has provided valuable insights into the dynamics of
user engagement on social media platforms. These insights
can inform the development of more targeted and effective
marketing strategies, helping businesses to better understand
and predict user behavior, enhance customer engagement,
and improve overall marketing efficiency. The robustness
of the FNN model, combined with the careful selection of
regularization parameters through cross-validation, has sig-
nificantly reduced the risk of overfitting and improved the
model's generalization ability. Overall, this study contributes
to the field of digital marketing by providing a comprehen-
sive framework for understanding user behavior and leverag-
ing it for strategic advantage.
Author Contributions Beibei Luo, Rongfei Luo wrote the main manu-
script text; Beibei Luo, Rongfei Luo prepared figures, tables, equations;
All authors reviewed the manuscript.
Funding No funding was received.
Data availability The datasets used and/or analyzed during the cur -
rent study are available from the corresponding author on reasonable
request.
Declarations
Conflict of intereset  The authors declare no competing interests.
Open Access  This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and repro-
duction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons
licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and
your intended use is not permitted by statutory regulation or exceeds
the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http:// creat iveco
mmons. org/ licen ses/ by- nc- nd/4. 0/.
References
 1. Teixeira, S., Oliveira, Z., Teixeira, S., Teixeira, S.: Understanding
the impact of online communication strategies on consumer pur -
chase intention for green cosmetics. Sustainability 15(20), 14784
(2023)
 2. Gu, X.W., Angelov, P., Han, J.G., Shen, Q.: Multilayer evolving
fuzzy neural networks. IEEE Trans. Fuzzy Syst. 31(12), 4158–
4169 (2023)
 3. Yu, H., Lu, J., Zhang, G.Q.: Topology learning-based fuzzy ran-
dom neural networks for streaming data regression. IEEE Trans.
Fuzzy Syst. 30(2), 412–425 (2022)
 4. Gao, F.Y., Hsieh, J.G., Kuo, Y.S., Jeng, J.H.: Study on resistant
hierarchical fuzzy neural networks. Electronics 11(4), 598 (2022)
 5. Xu, H., Wu, X.L., Liu, Y.T.: Modelling offline expansion strate-
gies of online companies. Kybernetes 51(1), 302–322 (2022)
 6. Zhou, C., Ma, N.N., Cui, X., Liu, Z.B.: The impact of online refer-
ral on brand market strategies with consumer search and spillover
effect. Soft. Comput. 24(4), 2551–2565 (2020)
 7. Basu, A., Bhaskaran, S., Mukherjee, R.: An analysis of search and
authentication strategies for online matching platforms. Manag.
Sci. 65(5), 2412–2431 (2019)
 8. Chiang, W.Y.: Applying data mining for online CRM marketing
strategy: an empirical case of coffee shop industry in Taiwan. Br.
Food J. 120(3), 665–675 (2018)
 9. Yang, L., Dong, S.Z.: Rebate strategy to stimulate online customer
reviews. Int. J. Prod. Econ. 204, 99–107 (2018)
 10. Sithravel, R., Olsson, T., Aries, M.: Optimizing presence sensing
lighting for energy efficiency and user behavioral needs in small
Swedish homes. Leukos 20(1), 107–125 (2024)
 11. de Oña, J.: Service quality, satisfaction and behavioral intentions
towards public transport from the point of view of private vehicle
users. Transportation 49(1), 237–269 (2022)

International Journal of Computational Intelligence Systems          (2024) 17:273
 Page 15 of 15   273
 12. Orzan, M.C., Florescu, M.S., Macovei, O.I., Burlacu, S., Orzan,
O.A.: The effects of online marketing on financial performance
in the textile industry. Ind. Textila 71(3), 288–293 (2020)
 13. Moran, A.J., Headrick, G., Perez, C., Greatsinger, A., Taillie, L.S.,
Zatz, L., et al.: Food marketing practices of major online grocery
retailers in the United States, 2019–2020. J. Acad. Nutr. Diet.
122(12), 2295–2310 (2022)
 14. Chang, Q., Zhang, Z., Wei, F.Y., Wang, J., Pedrycz, W., Pal, N.R.:
Adaptive nonstationary fuzzy neural network. Knowl.-Based Syst.
288, 111398 (2024)
 15. Magdin, M., Drzík, D., Reichel, J., Koprda, S.: The possibilities
of classification of emotional states based on user behavioral char-
acteristics. Int. J. Interact. Multimed. Artif. Intell. 6 (4), 97–104
(2020)
 16. Kokkodis, M., Ransbothama, S.: Learning to successfully hire in
online labor markets. Manag. Sci. 69(3), 1597–1614 (2023)
 17. Peng, Y., Hou, Y.P., Gao, S.H.: Online car-hailing market regula-
tion strategy in china: from the perspective of quadrilateral evo-
lutionary games. Comput. Econ. 64, 815–840 (2023).
 18. Caescu, S.C., Botezatu, F., Chivu, R.G., Popa, I.C., Florescu,
M.S.: The impact of online marketing on the use of textile pack -
aging: an approach to consumer behaviour. Ind. Textila 72(2),
210–216 (2021)
 19. Magdin, M., Kapusta, J., Koprda, S.: Investigation of behavioral
characteristic parameters intended for emotional state classifica-
tion. IEEE Access 10, 129029–129041 (2022)
 20. Liu, Y., Zhou, Z.L., Li, Y., Jin, D.P.: Urban knowledge graph aided
mobile user profiling. ACM Trans. Knowl. Discov. Data 18(1),
1–30 (2024)
 21. Ye, L., Wu, W.J., Ma, R.T.B., Lui, J.C.S.: On the profitability of
bundling sale strategy for online service markets with network
effects. ACM Trans. Internet Technol. 19(3), 1–32 (2019)
 22. Kuo, R.J., Cheng, W.C.: An intuitionistic fuzzy neural network
with Gaussian membership function. J. Intell. Fuzzy Syst. 36(6),
6731–6741 (2019)
 23. Wang, S., Yang, Y.: M-GAN-XGBOOST model for sales predic-
tion and precision marketing strategy making of each product in
online stores. Data Technol. Appl. 55(5), 749–770 (2021)
 24. Zhang, Y., Lin, H., Zheng, L.N., Yang, X.Y.: Adaptive online port-
folio strategy based on exponential gradient updates. J. Combin.
Optim. 43(3), 672–696 (2022)
 25. Cai, M., Luo, H., Meng, X., Cui, Y.: Differences in behavioral
characteristics and diffusion mechanisms: a comparative analysis
based on social bots and human users. Front. Phys. 10, 875574
(2022)
 26. Zhang, J.H., Li, Z.C., Zhang, H.C., Zhang, W., Ling, Z., Yang,
M.: Sensor-based implicit authentication through learning user
physiological and behavioral characteristics. Comput. Commun.
208, 244–255 (2023)
 27. Hodges, L., Lowery, C.M., Patel, P., McInnis, J., Zhang, Q.: A
systematic review of marketing practices used in online grocery
shopping: implications for WIC online ordering. Nutrients 15(2),
446 (2023)
 28. Ando, T.: Merchant selection and pricing strategy for a platform
firm in the online group buying market. Ann. Oper. Res. 263(1–2),
209–230 (2018)
 29. Li, F., Du, T.C.T., Wei, Y.: Offensive pricing strategies for online
platforms. Int. J. Prod. Econ. 216, 287–304 (2019)
 30. Liu, Y.S., Hou, J., Zhao, W.: Deep learning and user consumption
trends classification and analysis based on shopping behavior. J.
Organ. End User Comput. 36(1), 1–23 (2024)
 31. Drzik, D., Magdin, M.: A comprehensive analysis of the success
of classification algorithms for the classification of emotional
states based on the user’s behavioral characteristics. IEEE Access
11, 24953–24970 (2023)
 32. Wang, P., Xu, K.Q., Ding, Z.H., Du, Y.L., Liu, W.Y., Sun, B.B.,
et al.: An online electricity market price forecasting method via
random forest. IEEE Trans. Ind. Appl. 58(6), 7013–7021 (2022)
 33. Li, K., Lv, T.Y., Shen, H.W., Qiao, L.S., Chen, E.H., Cheng, X.Q.,
Sun, Z.: An empirical analysis on the behavioral differentia of the
“Elite-Civilian” users in Sina microblog. Physica A-Stat. Mech.
Appl. 539, 122974 (2020)
 34. Chen, S., Zhao, R.: Channel encroachment strategy through pure
online or combined offline retailing. IMA J. Manag. Math. 34(4),
801–821 (2023)
 35. Wu, J.H., Huang, Q.: Myopic and far-sighted pricing strategies in
a duopoly market with e-WOM effect. Int. J. Electron. Commer.
22(4), 609–630 (2018)
 36. Saura, J.R., Palos-Sanchez, P., Herráez, B.R.: Digital marketing
for sustainable growth: business models and online campaigns
using sustainable strategies. Sustainability 12(3), 1003 (2020)
 37. Yan, S., Archibald, T.W., Han, X.H., Bian, Y.W.: Whether to adopt
“buy online and return to store” strategy in a competitive market?
Eur. J. Oper. Res. 301(3), 974–986 (2022)
 38. Zhang, Y.Q.: Research on China’s agricultural product sales trans-
formation: online marketing mix strategy and performance on post
pandemic area. Front. Sustain. Food Syst. 7, 1297732 (2024)
 39. Liang, Z.W., Yuan, H., Du, H.W.: Two-stage pricing strategy with
price discount in online social networks. Theoret. Comput. Sci.
882, 1–14 (2021)
 40. Chiang, W.Y.: Identifying high-value airlines customers for strate-
gies of online marketing systems: an empirical case in Taiwan.
Kybernetes 47(3), 525–538 (2018)
Publisher's Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
