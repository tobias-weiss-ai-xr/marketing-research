---
title: Deep Hybrid CNN-LSTM Framework For Advanced Social Media Sentiment Analysis In Data-Driven Marketing
  Analytic
url: https://doi.org/10.64252/82p5f018
category: analytics
subcategory: framework
date: 2025-08
venue: International Journal of Environmental Sciences
authors:
- Shrabani Mallick
- Mrs. Parul Awasthi
- Anil Kumar Yadav
source: openalex-oa
pdf_url: https://theaspd.com/index.php/ijes/article/download/5768/4182
pages: 12
chars: 37326
fetched_at: '2026-11-08T17:32:22+00:00'
kb_version: 1
---

# Deep Hybrid CNN-LSTM Framework For Advanced Social Media Sentiment Analysis In Data-Driven Marketing Analytic

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
169

Deep Hybrid CNN-LSTM Framework For Advanced Social Media
Sentiment Analysis In Data-Driven Marketing Analytic

Dr. Shrabani Mallick1, Mrs. Parul Awasthi2, Dr. Anil Kumar Yadav3, Bhagya Sri G4, Dr.
Rabins Porwal5*, Nidhi Bhatia6and Jyoti Kataria7

1 Associate Professor, Department of Computer Science and Engineering, Dr. B.R. Ambedkar Institute
of Technology, Sri Vijaya Puram Email: shrabani.reek@gmail.com
2 Assistant Professor, Department of Electronics and Communication Engineering, University Institute
of Engineering and Technology (UIET), Chhatrapati Shahu Ji Maharaj University, Kanpur Email:
parulawasthi@csjmu.ac.in
3 Registrar, Chaudhary Charan Singh University, Meerut, Uttar Pradesh Email: yadanil@gmail.com
4 Senior Assistant Professor, Department of CSE (AI & ML),  CVR College of Engineering, Hyderabad
Email: bhagya.gangji@gmai.com
5 Professor, Department of Computer Application,  School of Engineering & Technology (UIET),
Chhatrapati Shahu Ji Maharaj University (CSJMU), Kanpur, Uttar Pradesh Email: rabins@csjmu.ac.in
6 Assistant Professor, Department of Computer Application,  SCRIET, Chaudhary Charan Singh
University, Meerut Email: nidhibhatia@scriet.ccsuniversty.ac.in
7 Assistant Professor, K. R. Mangalam University, Sohna, Gurugram Email: kataria.jyoti87@gmail.com
Corresponding Author: Rabins Porwal Email: rabins@csjmu.ac.in
Abstract
The aim of the study, the world of data-driven marketing has evolved to the point at which the correct measurement
of the societal mood at all levels of social media is imperative to shaping a responsive and personalized approach. This
paper presents a deep hybrid architecture t hat leverages Convolutional Neural Networks (CNNs) and Long Short -
Term Memory (LSTM) networks to overcome the limitations that the sentiment analysis has in the social media due
to noise and unstructure data. Though CNNs perform better on local patterns and semantic features in the text data,
LSTMs are more effective at reflecting sequential dependencies and contextual meaning, which makes a combination
of the two a potentially effective solution to the problem of complex linguistic forms that user-generated content consists
of. The model was trained and validated on various datasets provided by websites like Twitter, Facebook, Instagram
and YouTube after undergoing tough preprocessing procedures like tokenization, stop word deletion, lemmatization
and sequence padding. Comparative experiments revealed that CNN -LSTM architecture is more competitive in
comparison to standard machine learning models (Naive Bayes, SVM) as well as CNN and LSTM without CNN -
LSTM-like architecture and delivere d the accuracy of 91%, precision of 90%, and F1 score of 90.5%. Additional
assessment of the confusion matrix, ROC curves, and the case -level analysis of predictions indicated how robust the
model was in sentiment classification and how sensitive it could be. The results validate that a hybrid CNN-LSTM
model will be a scalable and efficient solution to real -time sentiment monitoring and therefore there is a strong
implication in the field of marketing analytics, campaign optimization analysis, and dealing w ith the customer
experience. Possible future improvements can involve attention layers, transformer, and multi-lingual adaptability in
order to achieve even better performance in classification and domain generalizability.
Keywords: Sentiment Analysis, Social Media, Cnn -Lstm, Deep Learning, Marketing Analytics, User -Generated
Content, Text Classification.
1. INTRODUCTION
In the era of digitization, as the process of interaction with the audience more often takes place through
online resources, it has become critical to learn how to track the attitudes of the people in order to
establish the means of effective promotion of the product. Sentiment analysis (also referred to as opinion
mining) has become an important sub -discipline of natural language processing (NLP) that allows

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
170

companies to extract and understand the emotional tone of a text in a systematic fashion [1]. In an effort
to be more data-driven, sentiment analysis will provide strong indicators to digital marketers on consumer
perceptions, brand health, and market pulse [2]. As user-generated content on social media continues to
exponentially scale upwards, the applications and presence of sentiment analysis have been dramatically
expanded [3]. But conventional methods cannot possibly be used with the unstructured and uncontrolled
data on these platforms whose environment is too noisy and contains way too much context. The
proposed deep hybrid model in this research is to address these deficits through network usage in the
form of collaborative systems of Convolutional Neural Networks (CNN) and Long Short-Term Memory
(LSTM) networks [4]. The research will deploy the strengths of these two architectures to complement
each other and harness the resultant accuracy and situational sensitivity of sentiment classification to
compute finer and practical marketing analytic.
1.1 Background on Sentiment Analysis in Digital Marketing
Sentiment analysis is one of the potent methods of digital marketing that allows brands to crack the
language of consumer attitude and vibes within their text messages  [5]. Sentiment analysis at its essence
is the study of textual opinion, sentiments, emotions and subjectivity that is computational in nature. On
the part of the marketers, consumer sentiment toward a brand, product or campaign can be a major
determinant of product development, customer service and brand positioning [6]. As digital change gains
pace and online platforms become leading means of consumer interaction, sentiment analysis has
transformed into a staple technology versus an add -on to new consumer intelligence. It has several
applications in marketing such as tracking the performance of a campaign and PR management, as well
as helping identify pain points in customer experience [7]. Sentiment analysis has also become a tool that
the companies use not only to analyze past performance but also determine the response of their
consumers leading to more focused, understanding and sensitive marketing processes. The difficulty with
this, though, is of human expression; to detect the sentiment of one is a troublesome issue, as slang,
sarcasm, context, and emotional layers make this process a difficult one. The complexity requires strong,
flexible and smart models capable of providing fine-grained sentiment results of consumers with very good
accuracy.
1.2 Importance of Social Media as a Rich Data Source
The recent extraordinary proliferation of social media sites like instagram, Twitter, instagram and
YouTube has made them, huge repositories of user -generated content  [8,9]. The sites provide the
unfiltered and real -time voice of the people, opinions, complaints, compliments as well as
recommendations concerning brands and products  [10]. Social media data, as opposed to being
structured through a more conventional feedback procedure like a survey or product review, is organic
and spontaneous, which can sometimes help capture consumer sentiment in its most raw form. To the
digital marketer, the ecosystem is a gold mine of information and gives intimate details about the behavior
of customers and their lifestyles, cultural movements and shifts in sentiment. More so, social media cuts
across different demographies and geographies, which makes the data contained therein a representative
data source of market analysis [11, 12]. The huge number, speed and even type of social data require some
high-end kinds of anal ytical methods that can sift through non structured textual data effectively. The
methods of traditional market research as good as they are, cannot be as responsive and as far-reaching in
real-time as social media analysis can be  [13, 14]. When sentiment analysis is applied to social media
monitoring, businesses can make informed decisions more quickly to adjust their campaigns, mitigate
crises, or capitalize on the trending opportunities, all depending on the assessment of the real-time public
sentiment.
RELATED WORKS

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
171

Singla et.al (2025) “introduced an advanced deep learning system using convolutional neural networks
and long short-term memory architecture to study and predict shopper actions in India. The model uses
CNN networks to collect spatial features from consumer transaction data an d search patterns, while
LSTM networks help recognize time-based behavioral trends. The model achieves superior performance
against conventional machine learning approaches and independent deep learning models, reaching
92.4% accuracy. It shows dependable predictions for consumer behavior, with precision to F1 -score at
91.8%, 92.2%, and 92.7%. Churn prediction accuracy is 18 percentage points higher than baseline
models, and an AUCROC score of 0.92 validates the model as an effective discriminator. The proposed
CNN-LSTM model provides practical recommendations for businesses to refine marketing activities and
enhance customer interactions”.
Anakal et.al (2025) “studied the rise of social media platforms has prompted organizations to improve
their marketing strategies to maximize user engagement and ROI. Current methods struggle to fully
incorporate user emotions and market changes, highlighting the need for innov ative tools. This study
combines sentiment analysis with the Firefly Algorithm to optimize marketing strategies in real -time, a
previously underutilized approach. The system measures social media emotion levels and applies
optimization methods based on feedback. The framework adjusts content strategies dynamically,
maximizing user engagement. The method demonstrated 98.4% precision in forecasting user engagement
metrics and adapting content strategies. This new optimization method offer s companies an effective
method to optimize digital marketplace outcomes”.
AbouGrad et.al (2025) “presented a stock price prediction model using financial time series and news
datasets. The model uses natural language processing (NLP) techniques to evaluate sentiment scores and
incorporate them with historical stock price data from NASDAQ. The data is pre-processed to ensure
consistency and suitability for training the model. A multi-layer LSTM neural network model is identified
as a suitable prediction model for accurate stock price predictions. The model enhances accuracy in
predicting short-term stock price trends for millennials, who are aggressive investors seeking quick profits.
The study highlights the critical role of stakeholders' sentiment in stock market performance and
contributes to the growing field of AI -driven financial sector, demonstrating the viability of integrating
NLP-driven sentiment analysis with deep learning for more informed investment decisions”.
Kumar et.al (2025)  “presented a hybrid deep learning model that combines LSTM with sentimental
analysis to improve stock price prediction in financial markets. The model uses historical price data and
sentiment indicators from live financial news headlines and social media posts. The LSTM subcomponent
monitors long-range temporal dynamics and short-run fluctuations, while the sentiment analysis unit sets
market trading mood. Experimental evaluations show the hybrid model significantly improves over single
model LSTM and traditional machine learning models. This integrated framework offers investors and
business management a more intelligent and adaptive decision-support system in financial prediction”.
Alam et.al (2025) “explored sentiment analysis in informal digital text, focusing on social media content.
The review analyzes 91 peer-reviewed articles between 2010 and 2024 using the PRISMA framework. Key
themes include the evolution of multimodal sentiment analysis, emotion class ification beyond polarity
detection, and the development of multilingual and cross -lingual sentiment systems. The review also
discusses the growing body of research in financial, political, and health-related sentiment analysis, where
domain-specific customization is critical for reliable prediction. However, challenges remain in areas such
as data imbalance, inconsistent evaluation metrics, lack of cross-domain generalizability, and insufficient
attention to ethical concerns. The  review provides a critical understanding of sentiment analysis and
identifies key research gaps, offering a reference point for scholars, developers, and practitioners to
improve sentiment analysis systems' robustness, inclusivity, and ethical grounding”.

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
172

Singgalen et.al (2024)  “discussed the hospitality industry is increasingly relying on online reviews for
decision-making, highlighting the need for robust sentiment analysis methodologies. Traditional models
struggle with unstructured textual data, especially when positive reviews dominate. This study integrates
a hybrid Convolutional Neural Network and Long Short -Term Memory model with the Synthetic
Minority Oversampling Technique (SMOTE) to improve sentiment classification accuracy. Using a
dataset of 665  reviews from THE 1O1 Bandung Dago Hotel, the model captures local features and
handles sequential dependencies, resulting in a more nuanced analysis of customer sentiments. The
approach improves predictive accuracy and provides actionable insights for cus tomer satisfaction
strategies. Future research could focus on model optimization, multilingual sentiment analysis, aspect -
based sentiment insights, and real-time sentiment monitoring”.
Table 1: Comparison table
Study Domain Methodology Key Metrics Contribution
Singla et
al. (2025)
E-commerce
consumer
behavior
CNN-LSTM on
transaction and
search data
Accuracy: 92.4%,
F1: 92.7%, AUC:
0.92
Predictive tool for
marketing
refinement
Anakal et
al. (2025)
Social media
marketing
optimization
Sentiment analysis +
Firefly Algorithm
Precision: 98.4%
(engagement
forecast)
Real-time adaptive
content
optimization
AbouGrad
et al.
(2025)
Stock market
prediction
(millennials)
LSTM + sentiment
from financial/news
data
Short-term stock
accuracy enhanced
Informs investment
decisions via
sentiment
Kumar et
al. (2025)
Financial market
prediction
Hybrid LSTM +
sentiment indicators
Improved over
LSTM and ML
models
Adaptive decision
support in finance
Alam et al.
(2025)
Social media
sentiment analysis
(review)
Review of 91 articles
using PRISMA
Highlights gaps in
current approaches
Guidance for
robust, ethical
systems
Singgalen
et al.
(2024)
Hospitality
sentiment analysis
CNN-LSTM +
SMOTE on hotel
reviews
Improved
sentiment
classification
Actionable insights
for customer
satisfaction
3. RESEARCH METHODOLOGY
The following section lists the systematic procedure to develop and test the proposed deep hybrid CNN-
LSTM model to conduct sentiment analysis within the scope of social media and marketing analytics.
This approach can be broken down into four major parts:  data collection, data preprocessing, model
architecture, and training and evaluation of the model. The design of each step has been done with these
aspects in mind; integrity, reliability and applicability of the model in the real world marketing scenarios.
3.1 Data Collection
To create a quality and diverse sentiment analysis system, data was collected on some of the famous social
media tools, including Twitter, Facebook, Instagram, and YouTube. These sites were deemed as it is
widely used by all kind of people and the frequency at which the consumers discuss products, brands and
services. Authored by users, the data sets include tweets, comments, reviews, captions, etc., filled with
expressions laden with sentiments hugely applicable in the marketing scope. Publicly available posts were
scraped by an API like the Twitter API (v2), Facebook Graph API, and YouTube data API and scraping
tools (with ethical and legal adherence). In order to bring in equal representation, it filtered the data to
contain fine, bad, and neutral sentiments of various industries (e.g., retail, tech, entertainment). Metadata

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
173

including timestamps, hashtags, user engagement indicators (likes, retweets, comments) were also stored,
in the case of an auxiliary analysis.
3.2 Data Preprocessing
Since the data found in social media is very unstructured and noisy, it was necessary to preprocess it
carefully so that the quality and consistency of inputs were good to train the deep learning model. The
initial step is the one of tokenization, which implies that texts are divided into tokens, that could be words
or subwords, through a tokenizer prepared to work with the deep learning frameworks, so that it is
possible to transform raw text with numerical representation into something to be embedded. Fur ther
on, the lowercasing and noise removal were preformed to standardize the text and to remove irrelevant
information like URLs, user mentions, hashtags, emojis, numbers, and special characters that created
data sparsity and obscurity. Signal-to-noise ratio was also improved by removing stop words with the help
of NLTK stop word list to eliminate commonly used words that do not have any sentimental value, e.g.
the, is, or and. This was then preceded by stemming and lemmatization which was the process of reducing
morphed words to their base or root form using such tools, as the Porter Stemmer and WordNet
Lemmatizer, enabling the model to consider such morphed work as a single concept (e.g. running and
ran → run). Finally, to accommodate variable-length inputs of social media data, padding and truncation
methods were used to bring all the input sequences into one constant length (e.g. 100 tokens) so that the
model could process each text snippet consistently within the limits of its architecture. This full fle dged
data pre-processing pipeline helped in getting the data in the right mode for good feature learning and
sentiment classification.
3.3 Model Architecture
The hybrid CNN-LSTM model was designed to exploit both spatial and sequential features in text. The
architecture consists of the following components:
• Embedding Layer : A pretrained word embedding such as GloVe (Global Vectors for Word
Representation) was used to convert words into 100 - or 300 -dimensional dense vectors.
Alternatively, Word2Vec and custom embeddings trained on the domain -specific corpus were
tested. The embeddings allow the model to capture semantic relationships between words.
• CNN Layers: The embedding outputs were passed through one-dimensional convolutional layers
with varying filter sizes (e.g., 3, 4, 5) and ReLU activation functions. These layers act as feature
detectors, identifying local patterns indicative of sentiment (e.g., phras es like “not good” or
“absolutely love”).
• Max-Pooling Layer: After convolution, a global max-pooling layer was applied to extract the most
important features and reduce dimensionality.
• LSTM Layer: The pooled features were fed into a single LSTM layer with 128 hidden units, a
dropout rate of 0.3 to prevent overfitting, and a sequence length of 100. The LSTM captured
long-range dependencies and the contextual flow of sentiments across sentences.
• Fully Connected Layer: The output of the LSTM was passed through a dense layer, followed by
a sigmoid activation  function for binary sentiment classification or softmax for multi -class
classification.
3.4 Training and Evaluation
The model was trained using a supervised learning approach with the following configuration:

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
174

• Loss Function:
➢ For binary classification: Binary Cross-Entropy Loss
➢ For multi-class classification: Categorical Cross-Entropy Loss
• Optimizer:
➢ Adam optimizer was used due to its efficiency in handling sparse gradients and adaptability
to learning rates.
• Batch Size and Epochs:
➢ Batch size: 64
➢ Number of epochs: 10–20, with early stopping applied based on validation loss to prevent
overfitting.
• Train-Test Split and Cross-Validation:
➢ The dataset was split into 80% training and 20% testing sets.
➢ 5-fold cross -validation was used to ensure robustness and reduce variance in model
performance across different data partitions.
• Evaluation Metrics : The performance of the model was measured using multiple evaluation
metrics:
➢ Accuracy: The proportion of correctly predicted sentiments.
➢ Precision: The proportion of positive identifications that were actually correct.
➢ Recall: The proportion of actual positives that were correctly identified.
➢ F1 Score: The harmonic mean of precision and recall, especially useful for imbalanced data.
➢ AUC (Area Under the ROC Curve) : A performance measurement for classification at
various threshold settings, indicating the model's ability to distinguish between classes.
4. RESULTS
The efficacy of the suggested CNN -LSTM hybrid model was assessed by a number of comparison tests
against both stand-alone deep learning architectures and conventional machine learning methods.  The
performance assessment focused on key metrics such as accuracy, precision, recall, and F1 score to ensure
a comprehensive understanding of each model's capabilities in sentiment classification tasks. The
evaluation also included visual analysis tools —such as confusion matrices, ROC curves, and error
frequency distributions—to further interpret the model's behavior and identify patterns of success and
failure. These experimental results not only validate the superiority of the CNN -LSTM approach over
baseline models like Naive Bayes, SVM, CNN, and LSTM but also highlight the importance of integrating
both local feature detection and sequential context learning in sentiment analysis, particularly within the
complex and noisy environment of social media data. What follows is a detailed breakdown of model
performance, visualizations, real-case predictions, and an analysis of observed error patterns.
1. Performance Comparison of CNN-LSTM vs. Baseline Models
The CNN-LSTM model significantly outperformed traditional machine learning models (Naive Bayes,
SVM) and standalone deep learning models (CNN, LSTM) across all key metrics. As shown in the table,

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
175

CNN-LSTM achieved the highest scores in accuracy (0.91), precision (0.90), recall (0.91), and F1 score
(0.905), demonstrating its ability to both extract relevant textual features and capture contextual flow in
sentiment.
Table 1: Performance Comparison of CNN-LSTM and Baseline Models
Model Accuracy Precision Recall F1 Score
Naive Bayes 0.75 0.73 0.74 0.735
SVM 0.78 0.76 0.77 0.765
CNN 0.85 0.84 0.83 0.835
LSTM 0.86 0.85 0.84 0.845
CNN-LSTM 0.91 0.9 0.91 0.905

Figure 1: Accuracy Comparison Bar Chart Across Models
2. Visualization of Results
Four key visualizations were generated:
• Accuracy Comparison Bar Chart : Highlights that CNN -LSTM surpasses all baseline models,
reinforcing its effectiveness in handling social media data.
• Confusion Matrix : The majority of predictions were correct, though some misclassifications
between neutral and negative sentiments were observed.
• ROC Curve: The CNN-LSTM achieved a high AUC score (approx. 0.97), indicating excellent
capability in distinguishing between positive and negative classes.
• Error Type Distribution : Most errors stemmed from mixed sentiment and sarcasm, which
remain challenging even for advanced models.
3. Case Studies: Sample Sentiment Predictions

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
176

Case-based evaluation showed that the CNN -LSTM model performed well on straightforward positive
and negative examples. However, it showed some inconsistency in predicting ambiguous or context -
sensitive texts, especially those with sarcasm or implied sentiments.
Table 2: Case Study of Sample Sentiment Predictions
Sample Text Predicted Sentiment Actual Sentiment
The product is amazing! Positive Positive
Not what I expected. Negative Negative
Absolutely terrible service. Negative Negative
I'm in love with this brand! Positive Positive
Could be better. Neutral Negative

Figure 2: Confusion Matrix for CNN-LSTM Model Predictions
4. Error Analysis and Challenges Encountered
The most frequent prediction errors involved:
• Mixed Sentiments: Posts expressing both positive and negative emotions were difficult to
categorize.
• Sarcasm: Without explicit sentiment words, sarcasm was often misclassified.
• Negations and Ambiguity: Phrases like “not bad” or vague expressions led to occasional
misinterpretation.
• Noisy Inputs: Slang, emojis, or improper grammar posed challenges for embedding and
classification.

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
177

Table 3: Error Analysis Based on Sentiment Misclassification Types
Error Type Frequency
Sarcasm 15
Negation 10
Ambiguity 8
Noise (slang/emoji) 12
Mixed Sentiment 20

Figure 3: ROC Curve for CNN-LSTM Model

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
178

Figure 4: Distribution of Error Types in Sentiment Classification
DISCUSSION
The study's experimental findings support the effectiveness of the suggested CNN -LSTM hybrid model
in gleaning significant sentiment insights from unstructured, noisy social media data.  The model
outperformed both standalone deep learning approaches (CNN and LSTM) and conventional machine
learning techniques (e.g., Naive Bayes and SVM) across a number of performance metrics by fusing the
advantages of Convolutional Neural Networks (CNNs) and Long Short-Term Memory networks (LSTMs).
In order to properly comprehend user-generated material in the marketing domain, it is crucial to capture
the subtleties of natural language. This was accomplished by combining CNNs for local feature extraction
with LSTMs for sequential dependency modeling.
The improved performance of the CNN-LSTM model, particularly its F1 score of 0.905 and high AUC
value (approx. 0.97), demonstrates its ability to balance precision and recall, making it a reliable tool for
real-world sentiment analysis applications. In con trast, traditional models like Naive Bayes and SVM,
while computationally efficient, exhibited limitations in handling the complexity of informal language,
sarcasm, and mixed sentiment often found in social media. Similarly, standalone CNN and LSTM models
delivered strong individual results, but failed to capture the full depth of contextual and semantic
variations compared to the hybrid approach.
The model’s practical implications for digital marketing are substantial. With more accurate sentiment
classification, marketers can better gauge public perception of brands, products, and campaigns in real
time. This allows for more informed decision -making, faster response to public feedback, and more
precise targeting of content based on audience mood and behavior. For example, in the retail or service
industries, real-time sentiment monitoring using CNN -LSTM can help identify dissatisfied customers
quickly, enabling timely intervention to prevent churn or reputational damage. Additionally, the model’s
capability to process large volumes of social media data with high accuracy supports scalable marketing
intelligence solutions that go beyond basic keyword or volume tracking.
Despite the strong results, the model did encounter challenges. Error analysis revealed that sarcasm,
ambiguity, and mixed sentiments were frequent sources of misclassification. For instance, sarcastic
statements that use positive words to imply negativity —such as "Great job on ruining my day" —were

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
179

difficult for the model to detect due to their reliance on deeper contextual or even cultural understanding.
Likewise, posts with conflicting emotions or vague expressions led to ambiguous classifications,
underscoring the limitations of purely text-based sentiment models in fully understanding human affect.
Addressing these limitations may require incorporating multimodal data (e.g., images, emojis, or
metadata) or external knowledge sources to enrich the model's interpretative capability. Another
challenge lies in the diversity of language use across platforms and demographics. Social media text is
often informal, abbreviated, and laden with region -specific slang, making it difficult for pretrained
embeddings and fixed architectures to perform uniformly ac ross datasets. This suggests the need for
continual model retraining and adaptation when applying sentiment analysis in different industries or
cultural contexts. Moreover, the computational complexity of hybrid models like CNN -LSTM, while
manageable in controlled experiments, may present scalability issues when deployed in high-throughput,
real-time systems without sufficient optimization.
Future research could explore enhancements to this model by integrating attention mechanisms,
transformer-based components like BERT, or leveraging multilingual embeddings to improve
generalization across languages. Another promising direction involves dev eloping domain -adaptive
training pipelines that fine-tune the model for specific sectors such as finance, healthcare, or e-commerce.
Finally, augmenting the model with user -level sentiment trends, location-based sentiment clustering, or
topic modeling coul d yield deeper insights for strategic marketing analytics. The hybrid CNN -LSTM
model presents a highly effective and scalable approach to sentiment analysis on social media, delivering
valuable implications for data-driven marketing. Its ability to extract rich, context-aware sentiment signals
positions it as a critical tool for businesses seeking to understand and respond to public sentiment in real
time. While some limitations persist, the framework establishes a solid foundation upon which more
sophisticated and adaptive sentiment analysis systems can be built, contributing significantly to the
evolving field of intelligent marketing analytics.
CONCLUSION
In this research, a profound hybrid CNN -LSTM model contribution was developed to expand on
sentiment analysis functions in the area of information-driven market-based analytics. As the use of social
media as a medium of primary expression by consumers continues to predominantly increase, businesses
experience the problem of having to analyse huge amounts of unstructured and noisy user -generated
contents. The conventional sentiment analysis models tend to be rather weak in recording the contextual
flavor of this data. In addressing such weaknesses, the proposed architecture integrates local pattern
recognition abilities of Convolutional Neural Networks (CNNs) with the contextual sequential modeling
of the Long Short -Term Memory (LSTM) networks. They trained a nd tested the model using data that
was scraped on Twitter, Facebook, Instagram and YouTube with the preprocessing involving tokenization,
stop words removal, lemmatization and padding of sequences. As scientific evidence unequivocally
proved, the CNN-LSTM model was much superior to purely basics particularities models, such as Naive
Bayes, SVM, and traditional isolated CNN or LSTM networks, demonstrating an impressive performance
level represented by accuracy levels exceeding 91% and F1 scores of 90.5%. Fu rther evaluation, ROC
curve and confusion matrices, reinforced the fact that the model was robust and very sensitive in labeling
sentiments within varied social media contents. The results confirm the possibility of the hybrid model
being an effective and scalable entity in real -time sentiment tracking, campaign optimisation, and
customer experience study in digital marketing. Yet, there are still issues to solve like sarcasm detection,
processing ambivalence and domain related language. The next steps of r esearch might involve
incorporating attention mechanisms, transformer-based models, and multilingual text using this model
to achieve a higher-performing and cross-domain applicable system.
REFERENCE
1. jadallah abed Khasawneh, Y., Khasawneh, A. J., & Saleem, M. A. (2024). Cross -Lingual Sentiment Analysis:
Comparative Study of Opinion Expression Across Different Languages. Migration Letters, 21(S1), 548-560.

International Journal of Environmental Sciences
ISSN: 2229-7359
Vol. 11 No. 6, 2025
https://www.theaspd.com/ijes.php
180

2. Chowdhury, R. H. (2024). Sentiment analysis and social media analytics in brand management: Techniques,
trends, and implications. World Journal of Advanced Research and Reviews, 23(2), 287-296.
3. Rasool, G., & Pathania, A. (2021). Reading between the lines: untwining online user-generated content using
sentiment analysis. Journal of Research in Interactive Marketing, 15(3), 401-418.
4. Halbouni, A., Gunawan, T. S., Habaebi, M. H., Halbouni, M., Kartiwi, M., & Ahmad, R. (2022). CNN-LSTM:
hybrid deep neural network for network intrusion detection system. IEEE Access, 10, 99837-99849.
5. Bell, C., Olukemi, A., & Broklyn, P. (2024). Social Media Sentiment Analysis for Brand Reputation
Management.
6. Thomas, S., Jadeja, A., Vaghela, K., & Shreevastava, R. (2022). Investigating the consumers attitude toward
brand and purchase intention within the context of cause -related marketing campaign for a pharmacy
product. International Review on Public and Nonprofit Marketing, 19(4), 691-708.
7. Holz, H. F., Becker, M., Blut, M., & Paluch, S. (2024). Eliminating customer experience pain points in complex
customer journeys through smart service solutions. Psychology & Marketing, 41(3), 592-609.
8. Santos, M. L. B. D. (2022). The “so -called” UGC: an updated definition of user -generated content in the age
of social media. Online Information Review, 46(1), 95-113.
9. Ali, A. (2024). Cultivating connections: exploring the influence of user -generated content on social and
consumer brand engagement.
10. Mahar, D. H. (2025). Leveraging People Analytics for Employer Branding: A Text Mining Study of Employee
Reviews in IT Industry. Journal of Chinese Human Resources Management, 16(2), 97-120.
11. Bernabeu-Bautista, Á., Serrano-Estrada, L., Perez-Sanchez, V. R., & Martí, P. (2021). The geography of social
media data in urban areas: Representativeness and complementarity.  ISPRS International Journal of Geo -
Information, 10(11), 747.
12. Niu, H., & Silva, E. A. (2023). Understanding temporal and spatial patterns of urban activities across
demographic groups through geotagged social media data. Computers, Environment and Urban Systems, 100,
101934.
13. Famoti, O., Omowole, B. M., Okiomah, E., Muyiwa-Ajayi, T. P., Ezechi, O. N., Ewim, C. P. M., & Omokhoa,
H. E. (2024). Enhancing customer satisfaction in financial services through advanced BI
techniques. International Journal of Multidisciplinary Research and Growth Evaluation,  5(06), 1558-1566.
14. Hasanuzzaman, M., Hossain, M., Rahman, M. M., Rabbi, M. M. K., Khan, M. M., Zeeshan, M. A. F., ... &
Shakir, M. N. (2025). Understanding Social Media Behavior in the USA: AI -Driven Insights for Predicting
Digital Trends and User Engagement. Journal of Ecohumanism, 4(4), 119-141.
15. Singgalen, Y. A. (2024). A Hybrid CNN-LSTM Model with SMOTE for Enhanced Sentiment Analysis of Hotel
Reviews.
16. Singla, L., Abrol, S., Bansal, S., Dhiman, A., & Banyal, P (2025). Understanding E -Commerce Consumer
Behavior with CNN-LSTM: A Data-Driven Approach.
17. Anakal, S., Lakshmi, P. N. S., Fofaria, N., Ramesh, J. V. N., Muniyandy, E., Sanjeera, S., ... & Patel, R. (2025).
Optimizing Social Media Marketing Strategies Through Sentiment Analysis and Firefly Algorithm
Techniques. International Journal of Advanced Computer Science & Applications, 16(2).
18. AbouGrad, H., Qadoos, A., & Sankuru, L. (2025). Financial Decision-Making AI-Framework to Predict Stock
Price Using LSTM Algorithm and NLP-Driven Sentiment Analysis Model.
19. Kumar, T. (2025). Deep Learning -Based Stock Price Forecasting for Business Management: A Hybrid
Approach Using LSTM and Sentiment Analysis. EKSPLORIUM-BULETIN PUSAT TEKNOLOGI BAHAN
GALIAN NUKLIR, 46(1), 1598-1613.
20. Alam, M. S., Mrida, M. S. H., & Rahman, M. A. (2025). Sentiment analysis in social media: How data science
impacts public opinion knowledge integrates natural language processing (NLP) with artificial intelligence
(AI). American Journal of Scholarly Research and Innovation, 4(01), 63-100.
21. Singgalen, Y. A. (2024). A Hybrid CNN-LSTM Model with SMOTE for Enhanced Sentiment Analysis of Hotel
Reviews.
