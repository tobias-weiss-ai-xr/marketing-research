---
title: Edge AI Frameworks for Real-Time Personalised Marketing Communication in 6G Networks
url: https://doi.org/10.59543/jidmis.v3.856
category: brand
subcategory: empirical
date: 2026-07
venue: Journal of Intelligent Decision Making and Information Science
authors:
- Berrin Ergin
source: openalex-oa
pdf_url: https://jidmis.org/index.php/jidmis/article/download/856/209
pages: 19
chars: 53879
fetched_at: '2026-11-08T18:18:06+00:00'
kb_version: 1
---

# Edge AI Frameworks for Real-Time Personalised Marketing Communication in 6G Networks

Journal of Intelligent Decision Making and Information Science, Volume 3(3s), 2026, 966-984

966

Journal of Intelligent Decision Making
and Information Science

www.jidmis.org
eISSN: 3079-0875

Edge AI Frameworks for Real-Time Personalised Marketing
Communication in 6G Networks

Dr. Berrin Ergin
Istanbul Gelişim University, Istanbul, Türkiye
Corresponding author email: b.ergin@duhaaviation.com

ARTICLE INFO ABSTRACT
Article history:
Received 14 March 2026
Received in revised form 25 April 2026
Accepted 10 May 2026

The recent development of Artificial Intelligence (AI) has brought about
dramatic changes to digital marketing, allowing personalised and real -time
communication with clients. Nevertheless, with the further sophistication of
AI systems, their efficiency de pends on the possibility of providing
personalised marketing messages in real time. The 6G networks and the Edge
AI integration are an innovative solution to this issue that provides the
possibility of ultra-low latency and high bandwidth to provide real -time and
personalised customer experiences. The paper suggests a new Edge AI
architecture that can support customised marketing communication in 6G
contexts. With machine learning models, e.g., Gradient Boosting Machine
(GBM), Random Forest (RF), and Suppor t Vector Machine (SVM), the
framework predicts customer engagement and loyalty, providing customised
content on the basis of real -time customer data. Key metrics used to assess
the performance of the proposed models were accuracy, AUC-ROC, precision,
recall, and F1-score. Results show that GBM outperforms both RF and SVM in
all evaluated metrics. Moreover, the low -latency features of 6G can also
improve the responsiveness in real -time, which will raise brand loyalty,
customer engagement, and satisfaction. T he Structural Equation Modelling
(SEM) demonstrated that AI communication systems have a significant
influence on engagement, which, in its turn, leads to brand loyalty. This study
explains why the integration of Edge AI and 6G networks can be used to
streamline personalised marketing tactics and provide businesses with an
edge in terms of providing customers with timely and relevant information.

Keywords: Edge AI; 6G Networks; Real-Time
Marketing; Personalised Communication;
Customer Engagement; Brand Loyalty; AUC-
ROC; Structural Equation Modelling (SEM);
Gradient Boosting Machine (GBM); Machine
Learning in Marketing

1. Introduction
Artificial Intelligence (AI) has become a critical factor in the redesign of digital marketing. The use of
AI-based systems, chatbots, and recommendation engines in particular is changing the way
businesses interact with their customers (Masa'deh, Almajali & Alsmadi, 2025; Lin, 2025) . Such
systems have enabled organisations to quit the old, one-directional communication models for more
dynamic, personalised and interactive communication. AI -based chatbots enable businesses to
provide individualised customer experiences and responses a t scale through real -time interactions

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
967
with customers. Equally, AI-driven recommendation systems select highly relevant content, products,
and services based on user behaviour, previous interaction, and preferences, which further
intensifies customer interaction (Jadiga, 2025). Such systems not only assist businesses in enhancing
customer experience but also create essential results such as higher conversion, brand loyalty, and
retention. As AI becomes more widespread, its contribution to improving customer interaction is
unquestionably a major success factor in the success of contemporary marketing (Chataut, Nankya
& Akl, 2024)
At the same time, the development of 6G networks is likely to bring digital communication to a new
level. In contrast to its predecessors, 6G networks will have low latency, high reliability, and
exceptional throughput, which will be used to offer the required infrastructure for real-time and data-
intensive applications (Shahraki et al., 2021) . Further, Mahmood (2025) coined that u sing 6G, the
businesses will have an opportunity to use AI -based marketing solutions with unprecedented speed
and precision, making personalised content, ads, and services almost instantaneous. Edge AI will also
enable these functionalities by taking computational functions nearer to the user in 6G networks,
and thus call for less data transmission to the centralised cloud servers (Letaief et al., 2021) . Such
proximity guarantees faster decision -making, personalisation in real -time and a generally smooth
experience for the customer. Consequently, the development of AI -based communication
technologies will be driven by 6G networks, b ecoming the core of the next -generation marketing
systems.
The need for marketing personalisation is accelerating in a very competitive environment in the
digital world today. Consumers are demanding purposeful, customised relationships with brands, and
communication that appeals to their needs, preferences, and b ehaviours (Ravisankar et al., 2024) .
With the increasing nature of digital channels, firms are turning to AI technology to fulfil such needs.
Customised marketing helps companies not just to provide the right content, but also to establish
even more emotio nal ties with consumers, which leads to brand loyalty and customer satisfaction
(Moshed & Al -Jabaly, 2024) . In this digital age of endless online interactions, live personalised
marketing driven by AI is no longer a luxury, but also a compulsion of the business that wants to
remain relevant and competitive.
Although the use of AI in marketing communication has been extensively researched, the modern
literature tends to dwell on the specific tools of AI-based communication (chatbots, recommendation
systems, etc.) without reflecting on the potential of the entire next-generation network, like 6G. The
current body of research on AI -driven marketing has been widely focused on 5G networks or even
lower networks, where latency and bandwidth constraints are more apparent. Moreover, although
AI and machine learning ar e effective for personalisation, their combination with 6G networks to
form real -time personalised marketing systems is underutilised  (Sarwar & Malik, 2025) . Another
aspect that has not been adequately researched concerning marketing communication is the capacity
of 6G networks to facilitate edge AI, which offers the processing power required to make
instantaneous decisions and process.
This research aims to bridge the gap by proposing a novel Edge AI model of real -time personalised
marketing communication in the 6G network. The combination of 6G with ultra-low latency and high-

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
968
speed communication and Edge AI will enhance customer interaction, real-time decision-making, and
provide a personalised experience at a new level in this framework. The paper will look at how 6G
networks can serve to power AI -driven marketing systems so t hat companies can not only serve
customers with higher speed but also increase their confidence, satisfaction, and loyalty in real-time.
The main aim of this research is to develop and validate an Edge AI framework that will enable real -
time personalised marketing communication in the context of 6G networks. The Edge AI framework
will use AI -based communication systems, including chatbots, AI recommendation engines, and
custom content delivery systems, to enable real -time marketing engagement and enhance the
overall customer experience. The research will be based on machine learning algorithms, including
Gradient Boosting Machines (GBM), Ran dom Forest (RF) and Support Vector Machines (SVM) to
examine customer behaviour and engagement metrics, and Structural Equation Modelling (SEM) to
evaluate the relationship among AI communication effectiveness, engagement, and customer
satisfaction.
The novelty of this research is the combination of Edge AI and 6G networks to achieve real -time
personalised marketing communication. Although there are studies regarding AI-powered marketing
and 6G networks, this paper will attempt to merge these two comp onents in a manner that will
increase the effectiveness and scalability of personalised marketing systems. This paper provides a
new dimension of the use of AI to provide consumers with a hyper -targeted and personalised
experience, both in terms of speed a nd efficiency, not achievable in previous network generations.
Finally, the framework presented in this study will have a tremendous implication for businesses that
would want to optimise their marketing strategies by using real-time and AI-based personalisation to
increase customer engagement and brand loyalty.
2. Related Work
2.1 AI in Marketing
The introduction of Artificial Intelligence (AI) into marketing systems transformed the way businesses
deal with customers. Among the most remarkable developments, the massive use of AI -driven
chatbots can be mentioned (Butt & Shah, 2025 ; Jawabreh, Masa'deh & Al Fahmawee, 2025 ). Such
systems allow businesses to connect with customers instantly in a way that provides customised
responses to user queries and preferences. Chatbots are based on natural language processing (NLP)
to mimic human-like dialogues and can serve customers immediately and efficiently (Boateng et al.,
2025). These AI systems have been found to have a significant positive impact on customer
engagement by providing timely interactions, creating less effort for customers and improving
customer satisfaction. Chatbots that run on AI are now primary tools to addre ss common customer
questions and are often the main elements of online digital marketing.
Similarly, AI-driven recommendation engines have also proved to be essential in the personalisation
of online shopping. Such engines process huge amounts of consumer data to provide individualised
product suggestions, affecting purchasing habits and raisin g conversion rates (Vallabhaneni et al,
2024). Large e-commerce sites, like Amazon and Netflix, use AI to recommend products or content
based on personal preferences and past actions. These recommendation systems enhance customer

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
969
experience in that they predict what will be desired by the customers based on sophisticated machine
learning models, including collaborative and content -based filtering, which leads to increased
customer engagement and loyalty  (Beyari & Hashem, 2025) . The latest study has shown that AI -
driven personalised marketing results in greater customer satisfaction because they tend to interact
with more content or products that address their unique needs (Anh, 2024; Sarfaraz, 2024).
Moreover, AI technologies have made it possible to run hyper -targeted marketing campaigns, in
which companies are able to divide the customers based on their behaviour, demographics, and
purchase history. The AI models optimise customer segmentation to pro vide customised marketing
messages to create an efficient utilisation of advertisement budgets and improve customer
experience (Wang, 2025) . Delivering personalised content at the appropriate time will allow
businesses to create a stronger customer relationship and boost brand loyalty.
2.2 AI in 5G/6G Networks
The advent of 5G networks has provided the framework to improve AI applications in the marketing
field, whereas 6G networks are expected to elevate them to new levels. The main strength of 6G as
compared to 5G is that it has very low latency, high reliability, and massive throughput (Mohammed,
Al-Barrak & Mahmood, 2024) . These aspects are essential to the creation of real -time AI-powered
applications, including individualist marketing systems, where data processing and quick decision -
making are necessary  (Ali, 2025; Ahmad & Alshuaibany, 2026) . With the development of 6G
networks, they will support Edge AI, where more computing and data processing is done at the end-
users, instead of using centralised cloud servers. It is especially notable in the context of real -time
personalised marketing, where AI models will be able to process customer data at the network edge,
which will decrease the time gap between data acquisition and decision-making (Paul et al., 2024).
With the potential to optimise real-time communication systems, edge AI will allow processing data
on devices or edge servers. This enables quicker decision-making, which is critical to the provision of
individualised content promptly. As an example, AI -based chatbots and recommendation systems
would be able to answer the question of a customer or give them a personalised product suggestion
in real-time, which greatly enhances the customer experience (Rinne, 2025). The latest studies have
emphasised that Edge AI can minimise latency and optimise bandwidth utilisation, which is why it is
the best choice to increase customer engagement in 6G settings (Sharma, Tilwari & Packs, 2024).
In addition, distributed AI systems can also maximise real-time decision-making when communicating
with customers. These systems spread the computational load among other edge devices and, as
such, more efficient processing and a quicker response time are possible. As an example, 6G networks
will help to support AI -based predictive maintenance, inventory management, and targeted
advertising with the help of sensors, mobile devices, and other connected objects (Sheraz et al.,
2024). This decentralised method ology assists in targeting marketing according to the current
customer behaviour, as well as making AI-based communication responsive and efficient.
2.3 Personalisation and Trust in AI Communication
Personalisation is one of the most important components of successful AI-driven marketing systems
that have been proven to influence customer trust, engagement, and loyalty. Studies have shown

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
970
that personalised communication, whether it is AI chatbots, a recommendation system, or
personalised ads, enhances customer satisfaction by providing relevant content that appeals to them
(Vashishth et al., 2024). One-to-one marketing makes the customers feel important and appreciated,
and this increases their connexion with the brands. Customised experiences make customers come
back and interact more often, thus creating loyalty to a brand in the long run.
Nevertheless, the success of individualised marketing strategies depends on the trust in AI
communication systems. Although AI systems can greatly personalise, the trust of customers in the
manner in which their data is processed, as well as their decision -making, is a major determinant of
their readiness to work with AI. Studies have demonstrated that an apparent lack of transparency
and the understandability of AI models contribute immensely to the development of this trust (Kaur
& Gupta, 2025). Clients will become more willing to communicate with AI-driven systems when they
believe that the technology is clear, moral, and conscious of their privacy. When AI models are
explainable and have justifications for how they make their decisions, they will be more accepted by
the users, thereby engaging and satisfying them more (Sun et al., 2025).
Although there are some advantages of personalisation, there are knowledge gaps in the literature
as far as 6G networks and AI communication systems of real -time personalised marketing are not
investigated (Moiz, 2026). Despite using AI in marketing in the form of chatbots and recommendation
engines, the implementation of 6G functionalities to increase the real -time communication of the
systems is also a little -understood area (Zawish et al., 2024) . In particular, little is known about the
way Edge AI in 6G  settings would enhance personalised marketing communication and respond to
the demand to establish trust and transparency. The fact that low -latency, high-reliability networks
can be complemented by AI systems that can make real-time decisions will present a unique chance
to enhance customer interactions and make communication personal on an unprecedented scale
(Salh et al., 2021).
2.4 Research Gap
Despite the fact that the use of AI in marketing communication has achieved much success, the
literature fails to address the topic of integrating 6G network capabilities with AI systems to facilitate
real-time personalised marketing. Even though researche rs have proven that AI -based marketing
solutions can be effective in personalisation and engagement, the role of Edge AI and 6G networks
in facilitating quick, responsive solutions is not yet investigated extensively. With 6G networks
starting to be deployed, the prospect of real-time, AI-based marketing systems capable of processing
and analysing massive amounts of customer data at the edge will continue to gain significance. Thus,
further studies should be conducted to determine how Edge AI, as implemented in 6G networks, can
transform personalisation communications and customer engagement, trust, and loyalty of
marketing systems. The study will help fill the literature gap and offer insights to businesses
interested in using AI -based communication technol ogies within the next -generation marketing
strategies.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
971
3. Methodology
3.1 Dataset Selection
In the paper, we have used Ecommerce Customer Data  that contains information on customer
interactions, behaviours and demographics. This data includes the most significant numeric
characteristics that are minimal in the analysis of customer behaviour in digital marketing systems.
The main characteristics that will be used in the research are customer profiles, including age and
duration of customer visit (length of visit to the site), their purchase behaviour (amount they spend)
and performance (frequency of visits, number of views and clicks) of the site.  These capabilities are
essential in forecasting customer activity and determining the aspects that determine brand loyalty.
In order to make the analysis reliable, standard data -cleaning methods have been applied to the
dataset. This was done by managing missing values, removing outliers and standardising numerical
features to place them on a similar scale. Popular data manipul ation libraries such as pandas and
NumPy were used in Python. Precisely, the missing values were imputed with the mean using pandas
to clean the data or eliminate the records with missing essential features. NumPy also offered
standardisation of numerical operations, which allowed all features of numbers to be normalised in
a range. The feature selection methods were used to maintain the most important variables that
influence the engagement of customers and remove redundant features. The data was then divided
into training and testing datasets in order to support the model development process.
3.2 Model Development
During the model development stage, we applied three popular machine learning models (Gradient
Boosting Machines, Random Forest, and Support Vector Machines) to predict customer engagement
and loyalty. The models were selected because they are effective in  managing complex and non -
linear relationships in data and are able to handle big data.
Gradient Boosting Machine (GBM)
Gradient Boosting Machine (GBM) is an ensemble learning algorithm which trains a sequence of weak
learners, usually decision trees, sequentially. The successive trees are trained to rectify the mistakes
committed by the earlier tree in the series. GBM can be used further to both regress and classify, and
thus it can be used to predict continuous scores of customer engagement, like brand loyalty and
categorical ones, such as loyal and non-loyal customers.
The loss function on which the model is formulated is as follows:
ℒ(𝐹) = ∑(𝑦𝑖 − 𝐹(𝑥𝑖))2
𝑁
𝑖=1
+ 𝜆 ∑ ∣ 𝑤𝑗 ∣
𝑀
𝑗=1

where:
• 𝑦𝑖 is the actual value,
• 𝐹(𝑥𝑖) is the predicted value,
• 𝑤𝑗 represents the model weights,

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
972
• 𝜆 is the regularisation parameter,
• 𝑁 is the number of samples, and
• 𝑀 is the number of features.
The model in our case was applied to forecast both the continuous variables, such as the length of
session and the binary variables, such as customer loyalty (loyal vs. non-loyal).
Random Forest (RF)
Random Forest (RF) is an ensemble algorithm which employs bagging to build a combination of
decision trees. The major benefit of Random Forest is that it can process massive and high -
dimensional data, and it is resistant to overfitting. It works by buildin g decision trees and averaging
the predictions in several trees to enhance accuracy and reduce overfitting. It is also an efficient
predictor of customer engagement because it is capable of dealing with a wide variety of features
(e.g., continuous or categorical) and modelling their interactions.
The main formula of a Random Forest model may be represented as follows:
𝑦̂ = 1 𝑇 ∑ 𝑓𝑡
𝑇
𝑡=1
(𝑥)
where:
• 𝑇 is the total number of decision trees,
• 𝑓𝑡(𝑥) is the prediction of the 𝑡-th tree, and
• 𝑦̂ is the final prediction averaged over all trees.
In the case of our marketing communication model, the RF was applied to forecast customer
interaction depending on session time and spending patterns.
Support Vector Machine (SVM)
The Support Vector Machine (SVM) is a supervised learning algorithm that is mostly applied in
classification problems. The principle of SVM is to identify a hyperplane that separates the data in
different classes in the most effective way. The hyperplane is optimised to grow the gap between the
nearest points of both classes, which are referred to as the support vectors.
In our research, we have used SVM to categorise the customers as loyal and non -loyal, i.e. their
patterns of interaction. The equation of an SVM classifier is as follows:
min⁡
𝑤
1
2 ∥ 𝑤 ∥2 subject to𝑦𝑖(𝑤𝑇𝑥𝑖 + 𝑏) ≥ 1, ∀𝑖
where:
• 𝑤 is the weight vector that defines the hyperplane,
• 𝑏 is the bias term,
• 𝑦𝑖⁡is the class label of the 𝑖-th sample,

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
973
• 𝑥𝑖 is the feature vector of the 𝑖-th sample.
SVM works especially well with complex patterns in customer behaviour data, including the level of
engagement and brand loyalty, according to the engagement and purchase history based on session
data.
Model Training
The training was conducted with the help of Google Colab in a Python environment, and the scikit -
learn libraries were used to carry out all three machine learning algorithms. The work on
hyperparameter tuning was implemented with the help of GridSearchCV, which tests the
combination of hyperparameters systematically through the predetermined set of them to identify
the best combination that provides the most appropriate results. The training phase was applied
using cross-validation to avoid overfitting and guarantee the generalisability of the models.
In both models, the k -fold cross-validation was used to evaluate the performance of the model on
several subsets of the training data. This was implemented in order to make sure that no data
partition was biased to the performance of the model.
3.3 Edge AI Framework
Edge AI Deployment
After training the models, they were put on the edge, where the computational power of 6G
networks was used to process data nearer to the customer. Through the use of ultra-low-latency and
high-speed data processing of the 6G networks, the framework guaran tees real -time decision -
making. Edge AI allows edge device data processing (e.g. customer smartphones or IoT devices),
shortening the time lag in providing customer-specific marketing messages.
The deployed models are able to assess customer data in real time and modify advertisements,
recommendations, and messages with consideration to user behaviour and engagement metrics. This
enables 6G capabilities to be integrated with Edge AI to sustain mo nitoring and adaptability, and
increase customer satisfaction and long-term brand loyalty.
Real-Time Personalised Communication
It operates an AI -driven chatbot and recommendation engine, which uses the trained models to
deliver a personalised marketing message to customers. These AI systems engage with the users at
all times and respond in real time depending on their actions, int erests, and previous interactions.
Individual product recommendations are offered in real time, and customer inquiries are resolved in
real time, which result in a more convenient user experience.
This is essential and needs to be used in order to maximise customer engagement since it makes
contextual suggestions during the interaction, so that the content is relevant and timely.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
974
3.4 Evaluation Metrics
Performance Metrics
The models were tested on the basis of conventional classification and regression measures to
determine the efficiency of the models in customer engagement, satisfaction, and loyalty. These
metrics include:
• Accuracy: The proportion of correctly predicted instances over the total number of instances.
Accuracy = Correct Predictions Total Predictions
• Precision and Recall: These metrics are especially important for evaluating the performance
of classification models, particularly in the case of imbalanced datasets.
Precision = True Positives True Positives + False Positives
call = True Positives True Positives + False Negatives
• F1-Score: The harmonic mean of precision and recall, providing a balance between the two.
𝐹1 = 2 × Precision × Recall Precision + Recall
• AUC-ROC: The area under the Receiver Operating Characteristic curve is used to evaluate the
trade-off between sensitivity and specificity across different thresholds.
AUC = ∫ ROC curve
1
0

Structural Equation Modelling (SEM)
Structural Equation Modelling (SEM) was used to assess the connections among AI communication
systems, customer engagement, and trust. Complex models with a number of variables and
interrelationships can be tested using SEM. The SEM model, which will be im plemented in this
research, will discuss the impact of AI communication efficacy on customer engagement and vice
versa on the brand loyalty variable.
The SEM equation may be expressed as:
Engagement = 𝛽1(AI Communication) + 𝜖1
Brand Loyalty = 𝛽2(Engagement) + 𝛽3(AI Communication) + 𝜖2
Where:
• 𝛽1, 𝛽2, 𝛽3are path coefficients, indicating the strength of relationships,
• 𝜖1, 𝜖2are error terms.
Using SEM, this study will offer a detailed study of the effects of AI -driven communication on
customer engagement and trust and the way they promote long-term brand loyalty.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
975

Fig 1. Proposed Methodology Framework
Figure 1 presents the steps to creating an Edge AI framework in real -time personalised marketing
communication on 6G networks. It starts by selecting datasets, as it concentrates on major customer
demographics and engagement rates. Then, data preprocessing  makes sure that there is clean and
relevant data by selecting and standardising features. The stage of model development entails the
training of AI models such as Gradient Boosting Machines (GBM), Random Forest (RF) and Support
Vector Machines (SVM). Mode ls in the Edge AI are deployed after training, and they facilitate real -
time communication through AI chatbots and recommendation engines. Lastly, the performance of
the framework is measured by such measures as accuracy, precision, and SEM to examine customer
engagement and brand loyalty.
4. Results and Analysis
This section will compare the performance of three machine learning models, including Gradient
Boosting Machine (GBM), Random Forest (RF) and Support Vector Machine (SVM), based on various
important measures: accuracy, AUC -ROC, precision, recall, and F1 -score. These models have been
used on customer engagement data from an online shopping site. It aimed to forecast customer
engagement and brand loyalty using the data on customer interactions. K -fold cross-validation was
used to evaluate the models in order to reduce overfitting and test generalisation to various subsets
of the data.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
976
4.1 Model Comparison
Table I summarises the outcomes of the model performance comparing GBM, RF, and SVM in the
above-mentioned metrics. According to the table, GBM has the highest performance in terms of
accuracy (0.87) and AUC-ROC (0.91), then RF with an AUC -ROC of 0.88 and an accuracy of 0.85. The
three models are best described by SVM as the worst model with an accuracy of 0.84 and an AUC -
ROC of 0.87.
TABLE I.  Model Comparison Based on Evaluation Metrics
Model Accuracy AUC-
ROC
Precision Recall F1-
Score
Gradient Boosting
Machine (GBM)
0.87 0.91 0.85 0.88 0.86
Random Forest (RF) 0.85 0.88 0.83 0.85 0.84
Support Vector
Machine (SVM)
0.84 0.87 0.82 0.84 0.83

The findings suggest that GBM is the best model used in predicting customer engagement and brand
loyalty because it performs better on all the metrics. RF has a moderate score in its performance,
which is not as stable as GBM. Although SVM is a very popula r tool, it did not do well in performing
the task of customer engagement, particularly when compared with GBM and RF.
GBM performed better than the other when comparing customer engagement, in terms of session
length and frequency of interaction. This finding implies that GBM is highly applicable in real -time
personalised marketing applications because it is capable of es timating the metrics that are critical
in interacting with customers. Comparatively, RF and SVM did not perform well in predicting longer
session duration and increased frequency of interaction, which is imperative in establishing customer
loyalty and retention.

Fig 1. Model Comparison
Figure 2 contrasts the performance of the GBM, RF and SVM models using various measures:
accuracy, AUC-ROC, precision, recall and F1 -score. The chart has shown clearly that GBM is always

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
977
better than RF and SVM in every measure, in the most important measures such as accuracy and
AUC-ROC that are used to measure model performance in customer engagement and marketing. RF
is slightly less effective than GBM, whereas SVM demonstrates poor perf ormance in most of the
measures, signifying its rather inferior adequacy to the task.

Fig 2. Combined ROC Curve for All Models
Figure 3 shows the True Positive Rate (TPR) against the False Positive Rate (FPR) of both models. GBM
performs best with an AUC of 0.91, then RF with an AUC of 0.88 and SVM with an AUC of 0.87. The
curve graphically justifies that GBM is more balanced in t erms of sensitivity and specificity, which is
indicated by its higher AUC -ROC. The random classifier is represented as the diagonal dashed line,
which forms a point of benchmarking. The graph shows that GBM has greater discriminatory force,
which makes the choice of GBM as the best model.
4.2 Performance in Real-Time Communication
The section tests the effectiveness of the Edge AI framework in real -time personalised marketing
communication. The Edge AI system uses the most effective model, GBM, which runs at the network
edge with the ultra -low latency of 6G networks. The main aim of  the framework is to enhance
customer communication and satisfaction by allowing real-time one-on-one interaction with the help
of AI chatbots and recommendation engines.
AI Communication Systems
The combination of Edge AI and 6G networks proved to have significant response time improvement.
Data was handled in the Edge AI system locally, which means that its response time was about 0.02
seconds, which is much lower than that of the cloud -based AI system, which was 0.15 seconds. The
6G low-latency and high -speed features were used to achieve this improvement in response time
and are required when interacting with customers through real-time communication.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
978

Fig 3. Response Time Comparison: Edge AI vs Cloud-based AI
The Edge AI system is far more efficient, as it will provide users with a real -time experience, as seen
in Figure 4. The system has a very low latency due to processing data at the edge therefore unlike the
traditional cloud -based systems, which rely on ce ntralised servers. This is very important in a
marketing aspect, where delays can harm customer interaction and satisfaction.
Trust and Loyalty Analysis
Brand loyalty was also dependent on customer trust. According to a survey, after using the AI -
powered communication system, it was found that 85% of users felt more satisfied when the system
could give personalised answers and make timely and relevant sugg estions. That is a direct pointer
to the role of trust in AI communication systems. Those consumers who had an adequate level of
trust in the AI system to give them pertinent advice were much more likely to revisit and interact
with the brand.
This strengthens the notion that brand loyalty is greatly determined by faith in AI communication.
Edge AI supports both customer satisfaction and builds a stronger brand loyalty and long -term
relationships with consumers because of the personalised and real-time communication it provides.
4.3 Quantitative Insights
The relationships between AI communication and customer engagement, and brand loyalty were
quantitatively analysed in this section using Structural Equation Modelling (SEM). SEM offers
information on the impact of AI communication effectiveness on customer  outcomes in terms of
engagement and loyalty.
SEM Path Coefficients
SEM analysis found the following meaningful path coefficients, indicating the direct and indirect
relationship between AI communication and customer engagement and brand loyalty:

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
979
TABLE II.  Sem Path Coefficients
Path Coefficient p-
value
AI Communication →
Engagement
0.78 < 0.05
Engagement → Brand
Loyalty
0.85 < 0.01
AI Communication →
Brand Loyalty
0.45 < 0.01

The path coefficient β_1=0.78 implies that AI communication has a significant effect on customer
engagement that is statistically significant. The path coefficient β_2=0.85 shows that the engagement
has a significant positive influence on brand loyalty. Mo reover, it was discovered that the direct
impact of AI communication on brand loyalty was quite considerable, with the coefficient of
β_3=0.45. This finding is reassuring that AI communication systems are a key factor that motivates
customer interaction and brand loyalty (Table II).
Trust is also crucial in the communication systems of AI, as stated by the SEM model. The customers
with confidence in the system had higher chances of interacting with the brand and staying in the
long term.
5. Discussion
5.1 Impact of AI-Powered Marketing
By combining Edge AI with 6G networks, businesses are able to establish a strong platform to offer
real-time, personalised marketing. Edge AI allows processing customer data at the network edge to
minimise latency and achieve almost real -time responses to interactions with customers. This
enables companies to connect with customers in a more relevant and timely fashion, provide
personalised content, product suggestions and offers, based on real -time behavioural information.
As an example, chatbots with AI c an instantly answer a customer's question, whereas AI
recommendation systems can dynamically propose a product/service depending on the customer's
browsing history and preferences, as well as situational information (Rosário & Dias, 2025) . This
interactive experience provides a better customer experience, developing a feeling of urgency and
topicality in communication.
Through the power of Edge AI, companies can build a better and more efficient marketing campaign
tailored towards individual customers. The live data processing enables companies to make
marketing decisions in real -time to increase engagement rates, conver sion rates, and eventually
customer satisfaction. Edges AI can be used in such industries as e -commerce, finance, and
entertainment, where customer needs and interests evolve fast, and companies cannot afford to
miss the chance of keeping their customers satisfied with using their products or services.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
980
The possibilities of the 6G network to deliver low and impeccable latency, a high bandwidth, and
secure communication are essential to the improvement of real -time marketing. The 6G also
supports edge computing that processes data faster and with reduced delay, unlike its predecessors,
which allows AI systems to react to customer interactions in real-time. As an illustration, on a website
or mobile app, customers can get real-time product recommendations depending on their real-time
behaviour, like viewing a particular item or leaving a shopping cart, with the low latency of 6G
providing the customer with a seamless and interactive experience (Nawaz et al., 2021). Moreover,
6G networks will allow businesses to process large volumes of data, and since personalisation can be
scaled without loss of performance.
This is a strong competitive edge of businesses due to the enhancement of customer interaction in
real-time. Today, customers demand fast and timely responses from brands. The ability to respond
in real-time by 6G enables dynamic and personalised marketing on a level that could not be achieved
before in the previous networks. By having Edge AI deployed in 6G settings, businesses, in addition
to being able to respond to customers faster, would be able to provide contextually relevant
marketing material that would spur greater engagement, customer loyalty, and conversion rates.
5.2 Challenges and Limitations
Although Edge AI and 6G network integration have a lot of opportunities, various challenges also
need to be resolved to ensure that the potential of this integration is achieved.
Such a large amount of customer data collected and processed at the edge of a network brings
significant concerns of data privacy. Since personal data is becoming a central part of AI marketing,
companies need to make sure that the information on customers is gathered, stored, and processed
in line with privacy laws, including the General Data Protection Regulation (GDPR) in Europe or the
CCPA in California. The data security at the edge is an essential factor to make sure that breaches and
unauthorised acc ess are minimised. Companies need to implement privacy -saving methods,
including differential privacy, to safeguard the information of their customers and still be able to
market their niche effectively.
The other difficulty is the ability of Edge AI systems to be scalable to large numbers of customers.
Although Edge AI is useful to process data locally and minimise latency, the scalability becomes
problematic with the increase in the number of devices and users. Businesses should make sure that
their Edge AI systems are capable of processing significant amounts of real -time data from many
sources (e.g., IoT, mobile apps, websites, etc.) without impacting their performance. Effective load
balancing and distributed AI models will be critical in scaling up operations without sacrificing speed
or accuracy.
With more complex AI models, model interpretability is an important issue as well. Companies
applying AI to communicate with their clients need to make sure that AI -based decisions are clear
and comprehensive. This is particularly significant in marketing,  where the customers might be
interested in receiving some recommendations or offers. In the absence of transparency, customers
will be afraid of AI -based decisions, which may hurt their trust in the brand. Thus, the creation of

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
981
explainable AI (XAI) models that could provide insights into decision -making will be essential in
ensuring customer retention and loyalty.
5.3 Future Work
In the future, research needs to be dedicated to resolving the issues related to data privacy,
scalability, and model interpretability of Edge AI and 6G networks.
A major area that future research could focus on is the creation of explainable AI (XAI) methods,
especially in complicated models like deep and reinforcement learning. In creating ways of describing
the choices of AI systems, businesses are likely to win more customers and make them more
accepting of AI -based communication systems. To illustrate, making some clarifications as to why
some recommendations are offered or why a particular customer was offered a particular
advertisement will allow the customers  to perceive the value of the AI systems and enhance their
interaction with the brand.
There is also the scalability of Edge AI systems to large-scale marketing as another significant research
direction. With more companies embracing AI-based marketing systems, there will be a multifold rise
in the need to process data in real time. Future s tudies ought to look at how to streamline Edge AI
infrastructure so that businesses can work with huge databases without affecting real -time
communication.
Finally, the research on integrating Edge AI and 6G networks to support real -time decision-making
and hyper-personalisation on a large scale has a lot of potential. It is also possible to explore new
distributed AI designs that leverage the 6G ultra -low latency and massive bandwidth opportunities
to the fullest and optimise AI models to run in a 6G environment. This might open the door to new
AI-based marketing innovations that utilise real-time and context-based communication to improve
customer interactions.
6. Conclusion
This paper presents an Edge AI architecture of real -time customised marketing communication in a
6G network context. Using Edge AI and ultra-low latency of 6G, companies are able to develop highly
responsive, personalised marketing systems, which can provide real-time response and personalised
content to clients. It has been shown that GBM is the best model to predict customer engagement,
being superior to RF and SVM in important evaluation measures.
The Edge AI platform has great potential to enhance customer interaction and brand retention
through real-time personalised communication. The 6G networks enable fast processing of data at
the network edge, enhancing reduced latency and a smooth customer e xperience. Moreover, the
belief in AI communication systems is an important consideration that leads to long -term customer
relationships since customers will be inclined to interact with brands that offer relevant and timely
information.
The future of AI-driven marketing is the smooth collaboration of the Edge AI and 6G networks. With
real-time communication becoming a more vital asset, 6G -powered Edge AI systems will provide
businesses with an in -scale opportunity to provide personalised,  engaging experiences. Ultra -low

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
982
latency, high bandwidth, and AI-chemicalised personalisation are going to make businesses relate to
their consumers differently, and real -time and context-sensitive communication will become a new
general standard in online marketing.
Author Contributions
B.E contributed to the conceptualisation, design, methodology development, data collection and
analysis of the study. B.E also carried out the interpretation of findings, prepared the original
manuscript draft, critically revised the content, and approved the final version of the manuscript. B.E
is accountable for all aspects of the work and ensured the accuracy, integrity, and completion of the
research.
Funding
This research received no external funding
Conflicts of Interest
The authors declare that they have no known competing financial interests or personal relationships
that could have appeared to influence the work reported in this paper.
Acknowledgement
This research was not funded by any grant
References
[1] Ahmad, S., & Alshuaibany, Y. (2026). Implementing AI -Driven Decision Support Systems in Data Management.
Precision Journal of Information Technology & Scientific Innovation 1 (1), pp. 1-15.
[2] Ali, H. (2025). The Influence of Machine Learning on Consumer Decision-Making Patterns in Germany: The Mediating
Role of AI Recommendation Systems for Achieving Sales and Customer Satisfaction. Advance Journal of Business
Management and Social Science 1(1), pp. 1-11. doi: https://doi.org/10.65080/c0nevs55
[3] Anh, V. T. K. (2024, October). The rise of AI in 6G networks: A comprehensive review of opportunities, challenges,
and applications. In  2024 International Conference on Advanced Technologies for Communications (ATC)  (pp. 333-
338). IEEE. doi: https://doi.org/10.1109/ATC63255.2024.10908115.
[4] Beyari, H., & Hashem, T. (2025). The role of artificial intelligence in personalizing social media marketing strategies
for enhanced customer experience. Behavioral Sciences, 15(5), 700. https://doi.org/10.3390/bs15050700
[5] Boateng, G. O., Sami, H., Alagha, A., Elmekki, H., Hammoud, A., Mizouni, R., ... & Guizani, M. (2025). A survey on
large language models for communication, network, and service management: Application insights, challenges, and
future directions. IEEE Communications Surveys & Tutorials. doi: https://doi.org/10.48550/arXiv.2412.19823.
[6] Butt, I. N., & Shah, S. (2025). The convergence of artificial intelligence and 6G networks: A transformative shift in
computing and communications.  Journal of Engineering and Computational Intelligence Review , 3(1), 68-81. doi:
https://jecir.com/index.php/jecir/article/view/13.
[7] Chataut, R., Nankya, M., & Akl, R. (2024). 6G networks and the AI revolution —Exploring technologies, applications,
and emerging challenges. Sensors, 24(6), 1888. doi: https://doi.org/10.3390/s24061888.
[8] Jadiga, S. (2025). Understanding the Role of AI in Personalized Recommendation Systems, Applications, Concepts,
and Algorithms.  International Journal of Computer Trends and Technology (IJCTT) , 73(1), 106 -118. doi:
https://doi.org/10.14445/22312803/IJCTT-V73I1P113.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
983
[9] Jawabreh, O., Masa’deh, R. E., & Al Fahmawee, E. A. D. (2025). Adoption of Artificial Intelligence Chatbots in Tourism
in Jordan. In  Generative AI in Creative Industries  (pp. 101 -116). Cham: Springer Nature Switzerland.
https://doi.org/10.1007/978-3-031-89175-5_7
[10] Kaur, N., & Gupta, L. (2025). Securing the 6G–IoT environment: A framework for enhancing transparency in artificial
intelligence decision -making through explainable artificial intelligence.  Sensors, 25(3), 854.  doi:
https://doi.org/10.3390/s25030854.
[11] Letaief, K. B., Shi, Y., Lu, J., & Lu, J. (2021). Edge artificial intelligence for 6G: Vision, enabling technologies, and
applications. IEEE journal on selected areas in communications , 40(1), 5 -36. doi:
https://doi.org/10.1109/JSAC.2021.3126076.
[12] Lin, P. (2025, June). The Rise of AI Communication: Opportunities, Challenges, and the Path Forward. In  2025 IEEE
International Symposium on Broadband Multimedia Systems and Broadcasting (BMSB)  (pp. 1 -5). IEEE. doi:
https://doi.org/10.1109/BMSB65076.2025.11165632.
[13] Mahmood, C. K. (2025). The Moderating Role of Content Creation Cost on the Relationship Between Generative
Adversarial Network (GAN) Usage and Marketing Success in Content Marketing: Empirical Evidence from the
Automotive Industry of the UK. Advance Journal of Business Management and Social Science 1 (1), pp. 1 -13. doi:
https://doi.org/10.65080/2nz9tz75
[14] Masa'deh, R. E., Almajali, D. A., & Alsmadi, L. A. (2025). Acceptance of Artificial Intelligence in a Jordanian Firm: An
Overview. https://doi.org/10.1108/978-1-83662-518-620251001
[15] Mohammed, S. M., Al-Barrak, A., & Mahmood, N. T. (2024). Enabling Technologies for Ultra -Low Latency and High-
Reliability Communication in 6G Networks.  Ingenierie des Systemes d'Information , 29(3). doi:
https://doi.org/10.18280/isi.290336.
[16] Moiz, A. (2026). Algorithmic Intimacy: How AI -Personalised Marketing Shapes Brand Trust and Brand Loyalty.
Majestic Global Trends in Marketing & Supply Chain Management 2 (1), pp. 1 -15. doi:
https://doi.org/10.65080/mgtmscm.v2.CM2602112011
[17] Moshed, A., & Al-Jabaly, S. (2024). Enhancing marketing success in Jordanian telecom: Strategic IoT integration and
brand relationship management for maximized consumer loyalty.  Journal of Infrastructure, Policy and
Development, 8(6), 3858. doi: https://doi.org/10.24294/jipd.v8i6.3858.
[18] Nawaz, S. J., Sharma, S. K., Patwary, M. N., & Asaduzzaman, M. (2021). Next -generation consumer electronics for
6G wireless era. IEEE Access, 9, 143198-143211. doi: https://doi.org/10.1109/ACCESS.2021.3121037.
[19] Paul, R., Islam, S. M., Sarkar, A., Khan, A. O. R., Islam, T., & Bari, M. S. (2024). The role of edge computing in driving
real-time personalized marketing: A data -driven business perspective.  International Journal For Multidisciplinary
Research, 6(5), 28494. https://doi.org/10.36948/ijfmr.2024.v06i05.28494
[20] Ravisankar, A., Shanthi, A. L., Lavanya, S., Ramaratnam, M. S., Krishnamoorthy, V., & Boopathi, S. (2024). Harnessing
6G for Consumer -Centric Business Strategies Across Electronic Industries. In  AI Impacts in Digital Consumer
Behavior (pp. 241-270). IGI Global Scientific Publishing. doi: https://doi.org/10.4018/979-8-3693-1918-5.ch010
[21] Rinne, K. J. A. (2025). AI -Powered Customer Engagement: How Personalization, Chatbots, and Recommendation
Systems Influence E-commerce Customer Satisfaction?. doi: https://urn.fi/URN:NBN:fi:amk-2025053018187.
[22] Rosário, A. T., & Dias, J. C. (2025). AI -Driven Consumer Insights in Business: A Systematic Review and Bibliometric
Analysis of Opportunities and Challenges. International Journal of Marketing, Communication and New Media, (15).
doi: https://doi.org/10.54663/2182-9306.2024.SpecialIssueMBP.6-35.
[23] Salh, A., Audah, L., Shah, N. S. M., Alhammadi, A., Abdullah, Q., Kim, Y. H., ... & Almohammedi, A. A. (2021). A survey
on deep learning for ultra -reliable and low -latency communications challenges on 6G wireless systems.  IEEe
Access, 9, 55098-55131. doi: https://doi.org/10.1109/ACCESS.2021.3069707.

Journal of Intelligent Decision Making and Information Science
Volume 3(3s), (2026) 966-984
984
[24] Sarfaraz, T. (2025). Generative AI -Driven Personalised Content and Its Impact on Consumer Engagement in
Destination Marketing in the UK: The Moderating Role of Normative Influence. Majestic Global Trends in Marketing
& Supply Chain Management 1(1), pp. 1-12. doi: https://doi.org/10.65080/mgtmscm.v1i1.5
[25] Sarwar, M. A., & Malik, M. (2025). The Impact of AI -Powered Personalisation on Consumer Trust and Purchase
Intention: A Cross -Cultural Comparative Study of Gen Z Consumers in the United Kingdom and Pakistan. Majestic
Global Trends in Marketing & Supply Chain Management 1 (1), pp. 1 -14. doi:
https://doi.org/10.65080/mgtmscm.v1i1.4
[26] Shahraki, A., Abbasi, M., Piran, M. J., & Taherkordi, A. (2021). A comprehensive survey on 6G networks: Applications,
core services, enabling technologies, and future challenges.  arXiv preprint arXiv:2101.12475 . doi:
https://doi.org/10.48550/arXiv.2101.12475.
[27] Sharma, D., Tilwari, V., & Pack, S. (2024). An overview for designing 6G networks: Technologies, spectrum
management, enhanced air interface, and AI/ML optimization.  IEEE Internet of Things Journal , 12(6), 6133-6157.
doi: https://doi.org/10.1109/JIOT.2024.3505617.
[28] Sheraz, M., Chuah, T. C., Lee, Y. L., Alam, M. M., Al -Habashna, A. A., & Han, Z. (2024). A comprehensive survey on
revolutionizing connectivity through artificial intelligence -enabled digital twin network in 6G.  IEEE Access , 12,
49184-49215. doi: https://doi.org/10.1109/ACCESS.2024.3384272.
[29] Sun, H., Liu, Y., Al -Tahmeesschi, A., Nag, A., Soleimanpour, M., Canberk, B., ... & Ahmadi, H. (2025). Advancing 6G:
Survey for explainable AI on communications and network slicing.  IEEE Open Journal of the Communications
Society, 6, 1372-1412. doi: https://doi.org/10.1109/OJCOMS.2025.3534626.
[30] Vallabhaneni, A. S., Perla, A., Regalla, R. R., & Kumari, N. (2024). The power of personalization: AI -driven
recommendations. In Minds unveiled (pp. 111-127). Productivity Press.
[31] Vashishth, T. K., Sharma, K. K., Kumar, B., Chaudhary, S., & Panwar, R. (2024). Enhancing customer experience
through AI-enabled content personalization in e -commerce marketing. Advances in digital marketing in the era of
artificial intelligence, 7-32.
[32] Wang, Z. (2025). Optimizing marketing strategies and personalized recommendation systems through precision
advertising and customer segmentation with artificial intelligence and business intelligence.  Advances in Operation
Research and Production Management, 4(1), 18-22. doi: https://doi.org/10.54254/3029-0880/2025.21864.
[33] Zawish, M., Dharejo, F. A., Khowaja, S. A., Raza, S., Davy, S., Dev, K., & Bellavista, P. (2024). AI and 6G into the
metaverse: Fundamentals, challenges and future research trends.  doi:
https://doi.org/10.1109/OJCOMS.2024.3349465.
