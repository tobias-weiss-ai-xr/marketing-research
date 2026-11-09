---
title: Big Data-Based Sentiment Analysis Using the Theory of Planned Behavior Framework to Evaluate Customer
  Attitudes Toward Banking
url: https://doi.org/10.20473/tijab.v10.i3.2026.91592
category: consumer-behavior
subcategory: framework
date: 2026-09
venue: TIJAB (The International Journal of Applied Business)
authors:
- Bikorin Bikorin
- Muhammad Sholeh
- Aulia Nurmalasari
source: openalex-oa
pdf_url: https://e-journal.unair.ac.id/TIJAB/article/download/91592/40746
pages: 15
chars: 44028
fetched_at: '2026-11-08T18:56:43+00:00'
kb_version: 1
---

# Big Data-Based Sentiment Analysis Using the Theory of Planned Behavior Framework to Evaluate Customer Attitudes Toward Banking

Available online at https://e-journal.unair.ac.id/TIJAB
TIJAB (The International Journal of Applied Business)
e-ISSN: 2599-0705
Vol. 10 No. 3, September 2026, pp. 344-358

Big Data-Based Sentiment Analysis Using the Theory of Planned Behavior
Framework to Evaluate Customer Attitudes Toward Banking
Bikorin a 1 , Muhammad Sholeh b, Anggun Sulistyowati a, Auliya Nurmalasari a, Yoshua Ronaldo
Primartono a

a Management, Faculty of Communication and Business, Universitas AKPRIND Indonesia, Indonesia
b Computer Science, Faculty of Science and Information Technology, Universitas AKPRIND Indonesia,
Indonesia

APA Citation:
Bikorin, B., Sholeh, M., Nurmalasari, A., Sulistyowati, A., & Primartono, Y. R. (2026). Big Data-Based Sentiment Analysis Using the Theory
of Planned Behavior Framework to Evaluate Customer Attitudes Toward Banking.  TIJAB (The International Journal of Applied Business) ,
10(3), 344-358.
Submission Date: 20/05/2026
Revision Date: 18/07/2026
Acceptance Date: 01/09/2026
Published Date: 28/09/2026
Abstract

Background: This study, based on the phenomenon that consumer reviews reflect perceptions of product quality,
analyzes big data from user reviews using the Theory of Planned Behavior framework. This study is useful for
both academics and practitioners in uncovering consumer behavior based on big data from user reviews.
Objective: This study aims to analyze consumer behavior based on sentiment big data using the Theory of Planned
Behavior framework.
Method: This study employs a quantitative approach by analyzing user sentiment. The dataset consists of 7,000
BRImo reviews from the Play Store. Data analysis is based on a lexical approach, in which the data is categorized
into positive, negative, and neutral l abels. Subsequently, the data is analyzed using the Theory of Planned
Behavior.
Results: This study yielded a variety of sentiment analysis results, with negative sentiment at 83.9%, positive
sentiment at 12.2%, and neutral sentiment at 3.9%. This indicates that the majority of BRImo users expressed
negative sentiment, with reviews focusing on login difficulties, app performance, and the presence of bugs.
Furthermore, model evaluation showed a high level of accuracy based on KNN and Confusion Matrix analysis.
Based on a theoretical approach, reviews that are mostly negative indicate a percept ion of dissatisfaction and a
lack of consumer trust in BRI’s financial platform services.
Conclusion: The findings of this study provide insights into the integration of sentiment analysis with consumer
behavior approaches. This study offers both academic and practical implications for maintaining customer
satisfaction through high-quality service systems.

Keywords: Sentiment Analysis; Big Data; Consumer Behavior; Mobile Banking; Theory of Planned Behavior

1 Corresponding author.
   E-mail address: bikorin@akprind.ac.id

 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358 345

This is an open access article under the CC BY-NC-SA license.

1. Introduction
Efficiency and effectiveness are outcomes of technological disruption that compel organizations to
change and adapt. Entities have been forced to adjust their communication strategies due to the
technological shift from desktop computers to wireless mobile applications (Crompton & Burke, 2020).
The rapid advancement of digitalization has intensified competition among businesses on digital
platforms, making the need for predictive market strategies crucial for managing consumer behavior
(Harwati et al., 2025). The success of technological innovations depends on the extent to which users
are willing to adopt and use them, thereby facilitating the organization’s objectives (Armanda et al.,
2025).
Current business trends are pushing organizations to provide services that are easy and fast. The
digital age has brought about fundamental changes in shopping preferences and behavior, leading to a
massive shift toward e -commerce platforms (Prayuti, 2024) . Today, user reviews are one of the key
indicators for assessing business quality. Public sentiment is a key determinant of behavior and is often
used to identify hidden challenges and opportunities across various fields (Qazi et al., 2022).
This phenomenon is part of the use of big data that is, a vast amount of dispersed data. According to
Abdalla (2022), Gartner gave a more point-by-point definition of big data: 'Big data is described as high-
speed, or potentially high-volume, high-assortment data resources that demand new types of handling
measures to empower improved dynamic, knowledge-revelation and cycle advancement'. Big Data has
become a key solution for supporting fast, accurate, and data-driven business decision-making (Zega &
Sianturi, 2025). Today, big data analysis is widely used as the basis for decision -making by various
entities.
Sentiment analysis is a natural language processing (NLP) technique used to decide if the underlying
sentiment is positive, negative, or neutral (Aftab et al., 2023). Public sentiment analysis is a
computational study of the opinions or views expressed by the public or individuals, which may reflect
positive, neutral, or negative sentiment (Lutfina et al., 2024). Sentiment comes in many forms, and often
changes over time as circumstances evolve (Qazi et al., 2023). The assessment aims to determine
whether the writer has a negative, positive, or neutral attitude toward a particular matter, institution,
individual, or location (Nandwani & Verma, 2021). Words with emotional connotations in an opinion
piece are categorized into several sentiment classes (Qazi et al., 2023).
Sentiment analysis has proven effective in processing large volumes of user review data to support
data-driven decision-making (Hasibuan & Heriyanto, 2022). Furthermore, advancements in machine
learning and deep learning methods have further improved the a ccuracy of sentiment classification,
enabling a deeper understanding of the user experience (Mulyati et al., 2025). Efforts to collect all
reviews and process them into information that can answer users' questions are necessary to determine
the quality of a product or service; this is achieved by utilizing sentiment analysis techniques (Rozi et
al., 2019). Sentiment analysis is a field worthy of research because it has strengths and weaknesses that
influence an individual’s decision-making process (Zhou et al., 2023).
The Theory of Planned Behavior (TPB) has been widely applied to predict and change behavior
(Ajzen, 2020). The TPB is used in research because of the importance of psychological factors,
particularly regarding consumer behavior (Michael et al., 2024). Rese arch by Putra et al. (2020)
indicates that attitudes influence the intention to use digital applications. Within the TPB, attitudes serve
as a dominant element in efforts to identify consumer behavior.
The integration of big data, sentiment analysis, and the Theory of Planned Behavior is necessary to
complement each other’s approaches. Research by Qazi et al. (2023) shows that user sentiment has a
significant influence on consumer intent, particularly re garding technology adoption. Research by
Karasenko & Baier (2025) shows that online review data can be used to measure consumer perceptions
through machine learning techniques. Sentiment analysis provides big data -based evidence, while the

346 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358

Theory of Planned Behavior offers relevant theoretical guidance. Based on the above discussion, this
study aims to integrate big data and sentiment analysis approaches into the TPB framework to measure
users’ attitudes toward technological innovations.

2. Literature Review
2.1. Sentiment Analysis
Sentiment analysis, also known as opinion mining, deals with inspecting these sentiments directed
towards any entity (Yadav & Vishwakarma, 2020). Sentiment analysis is a natural language processing
(NLP) technique used to decide if the underlying sentiment is positive, negative, or neutral (Aftab et al.,
2023). This approach is commonly used in the field of computer science to analyze user attitudes toward
technological innovations.
Receiving information via mobile devices elicits various types of emotional reactions (i.e., positive,
negative, and neutral) that are often expressed through sentiment (Qazi et al., 2023). The presence of
stimuli triggers the need for cognition to process  the message and convert it into a cognitive response,
which subsequently gives rise to the behavioral intention to respond to the message (Bikorin et al.,
2025). Stimuli that are responded to positively will result in positive cognition, whereas stimuli that are
responded to negatively will result in negative cognition.
Emotions are a classic example of sentiment; various emotional manifestations are reflected in
sentiment (Firdaus et al., 2022). Integrating relevant theories is useful for understanding how digital
sentiment influences market behavior and economic decisio n-making (Das et al., 2025). When people
interact with something, their subsequent motivations and behaviors regarding the targeted opinion are
influenced by their sentiment (Zafar et al., 2021). Therefore, sentiment and motivation are important
factors that need to be studied (Qazi et al., 2023).
In 2017, Koto & Rahmaningtyas developed the Indonesian Sentiment Lexicon (InSet), an
Indonesian-language sentiment lexicon containing 3,609 positive words and 6,609 negative words
(Nurkasanah & Hayaty, 2022). The sentiment polarity of each analysis has been weighted according to
the appropriate polarity. InSet was developed using microblogs relevant to Indonesian-language texts.
2.2. Theory of Planned Behavior (TPB)
The Theory of Planned Behavior (TPB) has been widely applied to predict and change behavior
(Ajzen, 2020). This theory is an extension of a series of related theories that are constantly evolving,
including the Theory of Reasoned Action (TRA) (Conner, 2020). In the TPB model, intention is assumed
to capture the motivational factors that influence an individual’s behavior (Putra et al., 2020). This
theory has been widely developed within the field of management, particularly for measuring consumer
behavior.
The TRA, TPB, and RAA all suggest that the key proximal determinant of action/behavior is one’s
behavioral intention to engage in that behavior (Conner, 2020). Attitudes refer to the degree to which
an individual evaluates a specific behavior positively or negatively (Savari et al., 2023). Subjective norm
refers to the impact of social pressure on an individual’s choice to participate in or refrain from a specific
activity (Michael et al., 2024). Meanwhile, behavioral intention measures an individual’s tend ency to
perform a specific action (Michael et al., 2024).
The Theory of Planned Behavior (TPB) has been widely applied to predict and change behavior,
including behavior related to technology use (Ajzen, 2020). According to Michael et al. (2024), actions
are the fundamental elements of behavioral activity. Behavioral implications are the user’s response to
an intention following exposure to a stimulus, in this case, the implementation of technological
innovations. Public sentiment influences behavioral intentions, and technology cannot be utilized
without a shared understanding (Qazi et al., 2023).

 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358 347

2.3. Novelty
The novelty of this study lies in the use of sentiment analysis in management science research, which
has been rarely done before. Another novelty is the use of big data as the basis for data analysis, which
is still uncommon in the field of management. A further distinguishing feature is the integration of
sentiment analysis with a management theory approach, namely the Theory of Planned Behavior.
Based on the integration of computer science and management approaches, this research has broader
implications. In the academic realm, it certainly represents a new approach that will continue to be
developed in future research. In the practical realm, this research is beneficial for business stakeholders
and software developers to better understand customer needs and behavior.
3. Method
3.1. Sample / Participants
The sample for this study consists of users of the BRImo app available on the Google Play Store.
Bank Rakyat Indonesia (BRI) was selected as the subject of this study because it has the largest number
of branches in Indonesia, operating more than 7,000 branches since 1962. According to data, the number
of BRI branches as of September 2024 reached 7,594 (BRI, 2024).
Figure 1. Load Research Dataset
This study utilized a dataset of 7,000 records obtained through data mining of BRImo user reviews
on the Play Store. The initial stage involved data cleaning (as illustrated in Figure 1) to consolidate the
raw data, thereby facilitating subsequent processe s. Data processing begins with a raw CSV file
containing 7,000 user reviews of the BRImo app, which is loaded into a DataFrame using the Pandas
library with a semicolon as the delimiter. Next, the data structure is verified by checking the number of
rows and column names to ensure that the file has been read correctly, followed by a preview of the first
five rows as an initial check. Once these verification steps are complete, the validated DataFrame is
passed on to the next stage of text preprocessing.

348 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358

As illustrated in Figure 1, the BRImo app review data obtained from the Google Play Store (7,000
data points) first underwent standard text preprocessing, which included case folding, cleaning (removal
of URLs, numbers, punctuation, and emojis), tokenizati on, normalization of non -standard words,
stopword removal, and stemming using the Sastrawi library.
The next steps were sentiment labeling into positive, neutral, and negative classes; feature extraction
using TF-IDF weighting; splitting the data into training and test sets; and evaluating model performance
using a confusion matrix and the metrics accuracy, precision, recall, and F1-score. K-Nearest Neighbors
(KNN), with TF-IDF vectors as input and a value of K determined through experimentation with several
values, is used as the classification model. The evaluation metrics for K include the cosine simil arity
metric, a distance-weighted weighting scheme, and model validation using k-fold cross-validation.
3.2. Instrument(s)
In terms of the methodology, the next step involved a lexicon -based process. This stage involved
classifying the data according to the desired sentiment categories: positive, negative, and neutral (as
illustrated in Figure 2).
Figure 2. Lexicon-Based Instrument Processing
At this stage, the previously disorganized data was categorized according to the desired sentiment
patterns. This will facilitate the process of interpreting the data in line with the research objectives. The
lexical labeling process begins by loading two reference word lists: the positive and negative lexicons
of the Indonesian language. Starting from the database, these are converted into a dictionary structure
that maps each word to a corresponding score weight. Next, each token is processed one by one, and the
polarity score is accumulated cumulatively —increasing if the token matches the positive lexicon and
decreasing if it matches the negative lexicon. Next comes score evaluation: Positive if the score is greater
than zero, Negative if it is less than zero, and Neutral if it is equal to zero. The next stage involves
classifying the results into two new columns in the dataset: Polarity Score and Sentiment. These then
serve as ground-truth labels used to train and evaluate the KNN classification model.
3.3. Data collection procedures
The data collection process was conducted by mining data from the Google Play Store regarding user
reviews of the BRImo app. The next step was to define data criteria based on relevant Indonesian -

 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358 349

language reviews. The subsequent process involved selecting and validating the data, removing
irrelevant and duplicate entries. Finally, 7,000 data points were prepared for the analysis phase.

Figure 3. Data Collection Procedures
Figure 3 shows a flowchart of the data collection procedure. The data collection process involves
four main steps, ranging from defining the data sources to finalizing a total of 7,000 reviews ready for
analysis.
3.4. Data analysis
The data analysis approach in this study employs the Indonesian Sentiment Lexicon (InSet). InSet is
an Indonesian-language sentiment lexicon developed by Koto and Rahmaningtyas (2017), consisting of
3,609 positive words and 6,609 negative words (Nurkasanah  & Hayaty, 2022). InSet is related to data
source management in research based on sentiment analysis.
Sentiment analysis in this study was conducted using the Python programming language, which was
run online via the Google Colaboratory platform. Google Colab is frequently used by researchers for
data processing, artificial intelligence model development, data analysis, and machine learning model
training (Andarsyah & Yanuar, 2024).
The data analysis phase of this study consists of four stages (as illustrated in Figure 4). The process
of analyzing 7,000 data points begins with the most critical procedure —sentiment labeling—followed
by visualizing representative sentiments, testing the model, and analyzing dominant features.

350 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358

Figure 4. Data Analysis
The data analysis phase of this study begins with the sentiment labeling process, which utilizes a
lexicon-based approach to classify data into three main sentiment categories: positive, negative, and
neutral. Next is the word cloud analysis process, which  visualizes various data representative of each
sentiment. Following that is the model analysis process, which validates the model’s accuracy using the
Confusion Matrix and KNN features. The final process involves analyzing the dominant features that
frequently appear using ABSA analysis.
4. Results
4.1. Sentiment Labeling
In the first stage of data analysis, the sentiment data was labeled. Based on the results of data
processing using a lexicon-based approach, the sentiment distribution was determined. Table 1 shows
that the sentiment distribution is dominated by negative s entiment with 5,873 data points, followed by
positive sentiment with 854 data points, and neutral sentiment with 273 data points.
Table 1. Data Distribution Table by Sentiment
 Negative Sentiment Positive Sentiment    Neutral
Sentiment
Amount of Data 5,873 854 273

The results of the data processing during the labeling stage, when presented as percentages, are
shown in Figure 5. The data analysis results indicate that negative sentiment accounts for approximately
83.9% of the total data, while positive sentiment acco unts for approximately 12.2% and neutral
sentiment accounts for approximately 3.9%.

 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358 351

Figure 5. Percentage of Sentiment Distribution Analysis
The results of the sentiment analysis show that the majority of BRImo users have negative
sentiments, as evidenced by the highest percentage of 83.9%. This means that the majority of BRI
customers are not yet satisfied with the financial platform’s services. This indicates a red flag that BRI
customers have a poor perception of these banking services; if no improvements are made, adverse
consequences may occur, such as a decline in trust and a change in customers’ intentions regarding their
relationship with BRI.
The subsequent labeling results show that positive sentiment ranked second with 12.2%. These data
analysis results indicate that customers’ positive perceptions of BRI’s financial services are minimal.
This serves as a serious reminder that BRI’s financial  services have not yet been fully able to meet
customers’ needs adequately. There is a need for continuous evaluation and improvement to prevent
customers from switching to other banks. Next, the results of the neutral sentiment analysis showed the
lowest percentage, at 3.9%. These results indicate that 273 BRI customers provided neutral reviews —
that is, they expressed neither positive nor negative sentiment. This implies that BRI needs to improve
its services to better meet customer needs.
4.2. Word Cloud Analysis
The next step is word cloud analysis, which visualizes text data by highlighting dominant words.
This analysis technique allows us to identify which topics frequently appear in reviews based on existing
sentiment classifications.

Figure 6. Negative Sentiment from Visualization Results

352 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358

The word cloud visualization shown in Figure 6 reveals that several keywords dominate the negative
sentiment. These words include 'app', 'open' and 'login'. These words indicate that BRImo app users are
experiencing difficulties accessing this digital platform, particularly with the login feature. BRI must be
aware of these sentiment results and immediately make improvements to its financial technology
services.

Figure 7. Positive Sentiment from Visualization Results
The next word cloud visualization shows positive sentiment, as shown in Figure 7. The words that
appear most frequently are 'transaction' 'open' and 'BRImo'. These words reflect customers’ positive
perceptions when using the BRImo service. Naturally, this is a point of focus for BRI to ensure that the
service—which is already good and has received positive feedback—can be maintained and its quality
further improved.

Figure 8. Neutral Sentiment Visualization Results
A word cloud visualizing neutral sentiment is shown in Figure 8. The results indicate that the
dominant words are 'notification' 'BRImo' and 'open' These words reflect the neutral perceptions of BRI
customers, which are not aligned with either positive or negative attitudes. This implies that BRI must
be able to address these customer reactions through continuous service improvements.
4.3. Model Analysis
The next step is to test the model using confusion matrix analysis and KNN. Model analysis is
necessary to evaluate the data classification model against the 7,000 reviews in the dataset.

 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358 353

Figure 9. Confusion Matrix of the KNN Model Classification Results on the Test Data
The confusion matrix results in Figure 9 indicate that the sentiment classification model used in this
study performs well. This is evident from the values along the main diagonal: 1,184 data points for
negative sentiment, 48 for neutral sentiment, and 161  for positive sentiment were classified correctly.
The number of classification errors is also very small, with only 1 negative data point, 6 positive data
points, and no errors in the neutral data. Overall, this model performs well in sentiment classification.
Figure 9 shows the confusion matrix resulting from the evaluation of the classification model on the
same test data (a total of 1,400 data points), with the following distribution of true labels: Negative:
1,185, Neutral: 48, Positive: 167. The model succe ssfully classified 1,184 negative reviews correctly
(only 1 negative review was misclassified as positive), classified all 48 neutral reviews correctly without
any errors, and classified 161 positive reviews correctly (with 6 positive reviews misclassified  as
negative).   Overall, this model achieved an accuracy rate of 99.50% on the test data (1,393 out of 1,400
data points were classified correctly). This percentage confirms very high classification performance
and is even slightly better than the results of the KNN model in Figure 10 (accuracy of 98.79%).

Figure 10. Confusion Matrix of the KNN Model Classification Results on the Test Data
The results of the KNN model in Figure 10 demonstrate good performance in sentiment
classification. For negative sentiment, 1,177 data points were correctly classified, with only 8 errors.
For neutral sentiment, there were 48 data points with no errors. For positive sentiment, 158 data points

354 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358

were classified correctly, with 5 misclassified as negative and 4 as neutral. These KNN analysis results
indicate that the model can measure sentiment effectively.
The 'True Label' axis label in the figure indicates the actual sentiment labels (the results of labeling
the test data). Furthermore, 'Predicted Label' shows the prediction results obtained from the KNN model
using TF-IDF features from the BRImo app review data. The explanation in Figure 10 shows that out of
a total of 1,400 test data points, the KNN model successfully classified 1,177 negative reviews correctly
(with 8 negative reviews misclassified as neutral). All 48 neutral reviews were classified corre ctly
without any errors, and 158 positive reviews were classified correctly (with 5 positive reviews
incorrectly classified as negative and 4 as neutral). Overall, this KNN model achieved an accuracy of
98.79% on the test data, confirming its excellent classification performance.
4.4. ABSA Analysis
The final stage is Aspect -Based Sentiment Analysis (ABSA), which is used to identify the priority
areas that users have rated.
This ABSA study was conducted by identifying ten predefined aspects (transfer features, login
process, user interface, security, bugs/errors, notifications, customer service, transaction speed, ease of
use, and app updates) using a keyword -based (keyword/r ule-based) approach. Reviews containing
relevant keywords were labeled with the corresponding aspects and could encompass more than one
aspect at a time.
Sentiment toward each aspect was then analyzed separately using a KNN classification model with
TF-IDF features, yielding a more granular sentiment polarity for each specific aspect compared to the
overall sentiment of the review. The results provide senti ment polarity (positive, neutral, or negative)
specific to each aspect, rather than just the overall sentiment of the review; this approach allows the
study to identify which aspects users complain about most (e.g., bugs/errors or the login process) as well
as which aspects receive the most positive sentiment (e.g., ease of use), making the analysis results more
granular and practical for BRImo app developers.

Figure 11. Sentiment Analysis Results Using ABSA
The results of the Aspect -Based Sentiment Analysis (ABSA) in Figure 11 show that the system
analysis grouped user opinions into several main aspects. These aspects are representative of frequently
discussed feature reviews. Consequently, this can generate more specific and targeted keywords. As
seen in Figure 11, specific aspects include 'transfer features', 'login process', 'user interface' and 'app
updates'.
For example, the term 'transfer features' is a priority for BRImo users, whether their perceptions are
positive, neutral, or negative. This means that transfer features are a flagship service for BRI, and
customers feel that this service is important and s upports their activities. Therefore, BRI must
consistently ensure that these transfer features remain fully functional and free of issues, as they are
fundamental to customers’ financial activities.
The next feature that is a priority for customers is the 'login process,' which customers consider
important because it serves as the main gateway to accessing BRImo services. If the login process fails,
customers cannot access the various services and oth er features on the app. Therefore, BRI must

 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358 355

continuously develop a login feature that is user -friendly for all types of users without compromising
the security of the service and data.
Next is the 'user interface' feature —the visual display within the app that allows users to navigate
various other features. The 'user interface' is important because it reflects how BRI develops and
maintains the quality of its banking app services. Ther efore, BRI must consistently ensure the app’s
reliability and develop features that meet user needs while upholding the principle of inclusivity.
The next priority for customers is 'app updates,' a feature that allows them to update the app. This
feature enables customers to update various relevant features and to fix bugs or software development
errors. Therefore, BRI must develop the 'app updates'  feature effectively, meaning it must ensure the
feature does not cause difficulties for customers due to device specifications or complexity.
The implications of this priority feature analysis indicate that BRI can utilize the results of this ABSA
study to evaluate and analyze specific user needs, thereby enabling the development of a system aligned
with the actual needs of BRI customers. These features are components of the ease-of-use aspect, which
is a crucial variable in the Technology Acceptance Model (TAM). For consumers, how easy it is to
operate the app is a top priority. Users will feel comfortable and be willing to spend time interactin g
with a user-friendly platform, thereby strengthening their engagement with the company.
5. Discussion
The results of this study show that the majority of users rate BRImo’s performance as poor. Based
on the labeling test, the majority of sentiment was negative, totaling 5,873 or 83.9%. This was followed
by positive sentiment, which was only a minority at 854 or 12.2%, and neutral sentiment at 273, or 3.9%.
Undoubtedly, these sentiment analysis results pose a serious problem, particularly regarding quality and
customer service.
The findings of this study contrast with those of Marwa & Kristanto (2022), who found that
manufacturing companies in Indonesia tend to exhibit more positive sentiment than negative sentiment,
as managers are reluctant to disclose bad news that could affect stock market valuations. However, the
findings of this study are consistent with the research conducted by Basri & Budi (2024), which states
that sentiment analysis based on app reviews indicates that negative sentiment is often more dominant
because users tend to be more active in voicing complaints than in sharing positive experiences. It can
be concluded that this reflects genuine dissatisfaction felt by users, which they then express through the
provided channels. This makes sense because if users feel that an entity’s service is subpar, their natural
response is to immediately leave a negative review. Conversely, when users are satisfied with an entity’s
service, they typically forget the experience and are reluctant to leave positive comments, as exc ellent
service is an expectation for any business entity.
Furthermore, from a theoretical perspective, the results of this study imply that perceptions of the
service will influence sentiment reviews, which in turn can affect overall consumer behavioral intent.
According to the study Sebayang et al. (2024), factors such as system performance, ease of use, and app
reliability are the primary determinants in shaping perceptions and acceptance of technological
innovations. In the context of the research findings, the presence of a majority of negative sentiments
toward the BRImo app may lead to distrust in the BRI institution as a whole. According to the Theory
of Planned Behavior (TPB), negative perceptions and attitudes can influence consumer behavioral
intentions. In the Technology Acceptance Model (TAM), BRI has n ot fully addressed a crucial aspect
of the theory namely, ease of use as reflected in the ABSA testing.
Furthermore, the results of this study also confirm that sentiment analysis serves to evaluate the
performance and services of entities based on big data mining. Previous research by Marwa & Kristanto
(2022), Qazi et al. (2023), and Karasenko & Baier (2025) evaluated user sentiment to test their findings,
with the aim of comprehensively validating organizational phenomena and performance. Undoubtedly,
the results of this study provide insights that complement the findings of previous research.

356 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358

6. Conclusions
Based on the Word Cloud analysis, the results of this study narrow down to three findings that shed
light on users’ perceptions of the BRImo service. Terms that frequently appear in positive perceptions
are 'transaction,' 'open,' and 'BRImo,' which reflect  customers’ sense of trust when using the BRImo
service. Furthermore, the terms that frequently appeared in neutral comments were 'BRImo,'
'notification,' and 'open,' which reflect general feedback. Meanwhile, the terms that frequently appeared
in negative  comments were 'app,' 'open,' and 'login,' which reflect challenges encountered when
accessing the BRImo app.
The results of a Word Cloud -based study show that the majority of users expressed negative
sentiment toward BRI’s services via the BRImo platform. This confirms that most customers are
dissatisfied with the app’s performance, particularly regarding the platform’s quality. These findings are
further reinforced by ABSA testing, which classified frequently mentioned features. The ABSA test
results show that the frequently mentioned features are fundamental aspects of customer activity relevant
to all three sen timent classifications. This means that ABSA labeling and testing are relevant for
confirming BRI customers’ dissatisfaction with specific features of the digital service.
Based on the results of the data analysis, BRI must conduct an evaluation and implement
improvements to address dissatisfaction with its mobile banking services. Addressing dissatisfaction—
particularly regarding negative perceptions —is crucial to maintaini ng service quality. These various
negative reviews represent the genuine voices of customers who are providing information about various
issues, concerns, and operational challenges with the app. BRI can comprehensively manage and analyze
this negative sentiment, and subsequently implement various improvements based on available scientific
data. Similarly, regarding neutral and positive sentiment, these reviews remain useful as notes for BRI
to identify services that are already optimal, in order to create differentiation and provide excellent
service to customers.
Furthermore, from a theoretical perspective, the results of this study validate the Theory of Planned
Behavior (TPB), which posits that perception is a fundamental aspect influencing consumer sentiment
and attitudes toward taking action. The majority of negative sentiments in this study indicate that users
are dissatisfied with BRImo’s performance, leading them to leave negative reviews. This serves as a
warning to stakeholders such as BRI and the app’s developers to pay attention to consumer feedback
and promptly implement improvements in the future.
In response to dissatisfaction with mobile banking services, both BRI and the app development
vendor need to establish systematic and integrated measures. The first step is to identify the issues by
managing data and verifying reviews that specifically add ress service challenges. Next is to prioritize
improvements; by analyzing various complaints about service features, they can identify which services
should be prioritized for improvement. The next step is to improve service quality, as continuous
improvement is a guarantee of the company’s quality. The final step is to maintain the credibility of
customer service; this is crucial because excellent service is a key indicator of customer satisfaction and
a means of fostering customer loyalty.

Declaration of generative AI and AI-assisted technologies in the writing process
During the preparation of this article, the author used Claude AI to develop the conceptual framework
and DeepL to refine the English grammar and structure. Having used these services, the author has
reviewed and re-edited the final result as necessary, an d takes full responsibility for the entire content
of the published article.
References
Abdalla, H. B. (2022). A brief survey on big data: technologies, terminologies and data -intensive
applications. Journal of Big Data, 9(1). https://doi.org/10.1186/s40537-022-00659-3

 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358 357

Aftab, F., Bazai, S. U., Marjan, S., Baloch, L., Aslam, S., Amphawan, A., & Neo, T. K. (2023). A
Comprehensive Survey on Sentiment Analysis Techniques. International Journal of Technology,
14(6), 1288–1298. https://doi.org/10.14716/ijtech.v14i6.6632
Ajzen, I. (2020). The theory of planned behavior: Frequently asked questions. Human Behavior and
Emerging Technologies, 2(4), 314–324. https://doi.org/10.1002/hbe2.195
Andarsyah, R., & Yanuar, A. (2024). Sentimen Analisis Aplikasi Posaja Pada Google Playstore Untuk
Peningkatan Pospay Superapp Menggunakan Support Vector Meachine. Jurnal Teknik
Informatika, 16(2).
Armanda, F. I., Pradana, F., & Nugraha Putra, W. H. (2025). Analisis Penerimaan Teknologi Sistem
Informasi Manajemen Tugas Menggunakan Model Task Technology Fit (TTF). Jurnal Teknologi
Informasi Dan Ilmu Komputer, 12(2), 339–350. https://doi.org/10.25126/jtiik.2025129414
Basri, M. H., & Budi, I. (2024). Pemodelan Topik dan Analisis Sentimen pada Teks Ulasan Pengguna
Aplikasi Perbankan Seluler di Indonesia. The Indonesian Journal of Computer Science , 13(4).
https://doi.org/10.33022/ijcs.v13i4.4200
Bikorin, B., Sulistyowati, A., Primartono, Y. R., Wahyudi, I., & Nurmalasari, A. (2025). Pengaruh Need
for Cognition serta Proses Kognisi Pesan Iklan pada Niat Perilaku. JNANALOKA, 57 –65.
https://doi.org/10.36802/jnanaloka.2025.v6-no2-57-65
Conner, M. (2020). Theory of Planned Behavior (Handbook of Sport Psychology, Ed.; Fourth Edition,
Vol. 1). John Wiley & Sons, Inc.
Crompton, H., & Burke, D. (2020). Mobile learning and pedagogical opportunities: A configurative
systematic review of PreK -12 research using the SAMR framework. Computers and Education,
156. https://doi.org/10.1016/j.compedu.2020.103945
Das, S., Mondal, S., Majerova, J., Vartiak, L., & Vrana, V. G. (2025). Tweet Sentiments: Understanding
X (Twitter) Users’ Perceptions of the Russia –Ukrainian Crisis on Consumer Behavior and the
Economy. International Journal of Consumer Studies, 49(1). https://doi.org/10.1111/ijcs.70009
Firdaus, M., Chauhan, H., Ekbal, A., & Bhattacharyya, P. (2022). EmoSen: Generating Sentiment and
Emotion Controlled Responses in a Multimodal Dialogue System. IEEE Transactions on Affective
Computing, 13(3), 1555–1566. https://doi.org/10.1109/TAFFC.2020.3015491
Harwati, Rosidah, L. A., & Milya, R. R. (2025). Penerapan Deep Learning untuk Analisis Sentimen
Ulasan Produk dalam Memprediksi Perubahan Permintaan Pasar pada Platform E -Commerce.
Inventa: Journal of Science, Technology, and Innovation.
Hasibuan, E., & Heriyanto, E. A. (2022). Analisis Sentimen Pada Ulasan Aplikasi Amazon Shopping di
Google Play Store Menggunakan Naive Bayes Classifier. Jurnal Teknik Dan Science, 1(3).
Karasenko, A., & Baier, D. (2025). Beyond sentiment analysis of online customer reviews: an approach
to automated measurement of technology acceptance from online customer reviews. Journal of
Business Economics, 95(7), 917–955. https://doi.org/10.1007/s11573-025-01232-z
Lutfina, E., Andriana, W., Quamila, S., Wiratmaja, P., & Febrianti, E. (2024). Science, Technology and
Management Journal Metode dan Algoritma Dalam Sentimen Analisis: Systematic Literature
Review Info Artikel. Science Technology and Management Journal .
https://doi.org/10.53416/stmj.v4i2
Marwa, E. A., & Kristanto, A. B. (2022). Analisis Sentimen Pengungkapan Informasi Manajemen: Text
Mining Berbasis Metode VADER. Owner, 6(3), 2853 –2864.
https://doi.org/10.33395/owner.v6i3.895
Michael, L. K., Hungund, S. S., & Sriram, K. V. (2024). Factors influencing the behavior in recycling
of e -waste using integrated TPB and NAM model. Cogent Business and Management , 11(1).
https://doi.org/10.1080/23311975.2023.2295605

358 Bikorin et al. / TIJAB (The International Journal of Applied Business), 10( 3) (2026) 344–358

Mulyati, E., Muhammad Ibnu Choldun Rachmatullah, & Adri Sapta Firmansyah. (2025). Sentiment
Analysis of Pospay Application Reviews Using the Bert Deep Learning Method. Jurnal Teknik
Informatika, 18(2), 173–183. https://doi.org/10.15408/jti.v18i2.41116
Nandwani, P., & Verma, R. (2021). A review on sentiment analysis and emotion detection from text. In
Social Network Analysis and Mining  (Vol. 11, Number 1). Springer.
https://doi.org/10.1007/s13278-021-00776-6
Nurkasanah, A., & Hayaty, M. (2022). Feature Extraction using Lexicon on the Emotion Recognition
Dataset of Indonesian Text. Ultimatics : Jurnal Teknik Informatika, 14(1).
Prayuti, Y. (2024). Dinamika Perlindungan Hukum Konsumen di Era Digital: Analisis Hukum Terhadap
Praktik e -Commerce dan Perlindungan Data Konsumen di Indonesia . 5, 2746 –5047.
https://doi.org/10.55637/juinhum.5.1.8482.903-913
Putra, H. B., Pradita, N., & Hayuningtias, K. A. (2020). Prediksi Niat Penggunaan Aplikasi Dan
Permainan Daring Freemium Versi Berbayar Dengan Menggunakan Model TPB. Managament
Insight: Jurnal Ilmiah Manajemen, 15(2), 130–143. https://doi.org/10.33369/insight.15.2.130-143
Qazi, A., Hasan, N., Owusu-Ansah, C. M., Hardaker, G., Dey, S. K., & Haruna, K. (2023). SentiTAM:
Sentiments centered integrated framework for mobile learning adaptability in higher education.
Heliyon.
Qazi, A., Qazi, J., Naseer, K., Zeeshan, M., Khan, B. A., & Dey, S. K. (2022). Sentiment Analysis of
Nationwide Lockdown amid COVID 19: Evidence from Pakistan. Proceedings of the 2022 IEEE
7th International Conference on Information Technology and Digital Applications, ICITDA 2022.
https://doi.org/10.1109/ICITDA55840.2022.9971397
Rozi, N. F., Arianto, F., & Hapsari, D. P. (2019). Analisis Sentimen Pada Opini Pengguna Maskapai
Penerbangan Menggunakan Hybrid Cuckoo Search. Jurnal Teknologi Informasi Dan Ilmu
Komputer (JTIIK), 6(3), 321–326. https://doi.org/10.25126/jtiik.201961337
Savari, M., Damaneh, H. E., Damaneh, H. E., & Cotton, M. (2023). Integrating the norm activation
model and theory of planned behaviour to investigate farmer pro -environmental behavioural
intention. Scientific Reports, 13(1). https://doi.org/10.1038/s41598-023-32831-x
Sebayang, T. E., Hakim, D. B., Bakhtiar, T., & Indrawan, D. (2024). What Accelerates the Choice of
Mobile Banking for Digital Banks in Indonesia? Journal of Risk and Financial Management, 17(1).
https://doi.org/10.3390/jrfm17010006
Yadav, A., & Vishwakarma, D. K. (2020). Sentiment analysis using deep learning architectures: a
review. Artificial Intelligence Review , 53(6), 4335 –4385. https://doi.org/10.1007/s10462 -019-
09794-5
Zafar, A. U., Qiu, J., Li, Y., Wang, J., & Shahzad, M. (2021). The impact of social media celebrities’
posts and contextual interactions on impulse buying in social commerce. Computers in Human
Behavior, 115. https://doi.org/10.1016/j.chb.2019.106178
Zega, A. S., & Sianturi, F. A. (2025). Pemanfaatan Big Data Dalam Sistem Pendukung Keputusan
Bisnis. Jurnal Kolaborasi Sains Dan Ilmu Terapan , 3(2), 2025 –2060.
https://doi.org/10.69688/juksit.v3i2.67
Zhou, C., Yang, S., Chen, Y., Zhou, S., Li, Y., & Qazi, A. (2023). How does topic consistency affect
online review helpfulness? The role of review emotional intensity. Electronic Commerce Research,
23(4), 2943–2978. https://doi.org/10.1007/s10660-022-09597-x
