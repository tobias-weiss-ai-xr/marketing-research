---
title: Emotion analysis and management improvement of hotel user online reviews based on BERT-RF and PLS-SEM
  integration
url: https://doi.org/10.1007/s44163-026-02199-8
category: brand
subcategory: framework
date: 2026-09
venue: Discover Artificial Intelligence
authors:
- Xiangwei Xia
- Chao Qu
- Yi Qu
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44163-026-02199-8.pdf
pages: 23
chars: 71446
fetched_at: '2026-11-08T19:02:13+00:00'
kb_version: 1
---

# Emotion analysis and management improvement of hotel user online reviews based on BERT-RF and PLS-SEM integration

Discover Artificial IntelligenceXia et al. Discover Artificial Intelligence          (2026) 6:1174
https://doi.org/10.1007/s44163-026-02199-8
RESEARCH Open Access
Emotion analysis and management
improvement of hotel user online reviews
based on BERT-RF and PLS-SEM integration
Xiangwei Xia1*, Chao Qu1 and Yi Qu1
  * C o r r e s p o n d e n c e :
Xiangwei Xia
xiaxiangwei2024@126.com
1Department of Hospitality
Management, Hospitality Institute
of Sanya, Sanya 572000, China
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m  o  n   s  . o r g / l i c e n s
e s / b y - n c - n d / 4 . 0 /     .
Abstract
Online reviews have become a core factor affecting hotel booking decisions and
brand reputation. Existing research mostly focuses on emotion analysis techniques,
but lacks guidance on the implementation of management strategies, and traditional
single text analysis has limitations. Therefore, to accurately locate hotel service
issues, reduce the impact of negative reviews, enhance customer trust and platform
ratings, an emotion analysis framework and real-time feedback mechanism that
integrates multi-source text features are proposed. This study combines Bidirectional
Encoder Representations from Transformers with Random Forest (BERT-RF) for
emotion analysis, and uses structural equation modeling to model satisfaction and
calculate satisfaction index. The emotion classification accuracy of the BERT-RF
model reached 90%, with a positive review recall rate of 93% and an F1 score of
91%. The value perception had the strongest impact on satisfaction, with customer
satisfaction directly driving loyalty and customer complaints negatively affecting
value perception. The study accurately identifies negative reviews through multi-
modal emotion analysis, and combines PLS-SEM quantitative satisfaction driving
mechanism to provide data support for optimizing service resource allocation in
hotels, promoting the transformation from “passive response to negative reviews” to
“active prevention” management paradigm. Unlike conventional hybrid models that
merely aggregate features, the proposed BERT-RF framework introduces a structured
fusion mechanism. The deep context embedding of BERT is dynamically weighted
and enhanced based on random forest statistics and domain-specific features,
synergistically enhancing the robustness of sentiment classification, especially for
fuzzy and domain-specific expressions in hotel reviews.
Keywords Partial least-square method, Structural equation modeling, Hotel
management, Satisfaction, Emotion analysis
  1 Introduction
With the vigorous development of e-commerce, online reviews have deeply penetrated
into the consumer decision-making chain and become the key driving factor influencing
hotel booking behavior and shaping brand reputation [1]. Nearly 90% of potential guests

Page 2 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
will repeatedly review the reviews of historical guests before confirming their booking,
viewing them as a touchstone for measuring the hotel's true service level [ 2]. More intu-
itively, for every one point increase in a hotel's overall rating on mainstream booking
platforms, there is an average potential premium space of up to 11.2% for its room rate
[3]. This fully demonstrates that positive word-of-mouth evaluation not only symbolizes
reputation, but also directly translates into core competitiveness of economic benefits.
An influential negative review with the potential to cause a loss of up to 10% in hotel
revenue [4]. It may not only scare off potential customers, but also damage brand image
and long-term customer loyalty. Therefore, accurately analyzing the emotion of reviews,
especially quickly identifying the key issues reflected in negative reviews, and making
targeted and systematic improvements is of great significance for improving customer
satisfaction, repeat purchase rates, and establishing strong brand loyalty [ 5, 6]. Existing
research has mostly focused on emotion analysis techniques, but lacks guidance on the
implementation of hotel management strategies, and some hotels rely on short-term
means such as “brushing positive reviews” to truly improve service quality. Therefore,
the study proposes a Partial Least-Square Method-Structural Equation Modeling (PLS-
SEM) using bidirectional encoders and Random Forest (RF), aiming to help hotels accu -
rately locate problems, reduce the impact of negative reviews, improve customer trust,
and improve online platform ratings.
The key contribution of this research lies in explicitly distinguishing methodological
integration from substantive innovation.
(1) For BERT-RF, the innovation lies in a “Feature Importance-Guided Re-weighting”
strategy. Rather than simple feature concatenation, RF is employed during training to
evaluate the incremental information gain contributed by statistical features relative
to BERT’s contextual embeddings. Features with low gain are down-weighted, while
domain-specific cues are amplified, thereby adaptively bridging the gap between
deep semantics and surface statistics, a common challenge in short review texts.
(2) For the PLS-SEM component, the improvement is not algorithmic but architectural
and applicational: the CCSI model is extended with hotel-specific constructs. More
importantly, the quantitative sentiment scores derived from BERT-RF are used as
formative indicators for “Value Perception” and “Quality Perception. ” This transforms
PLS-SEM from a survey-only tool into a hybrid system that directly ingests user-
generated content, enabling more ecologically valid and real-time responsive
satisfaction analysis.
2 Related works
Online reviews have become a key influencing factor for consumers' hotel choices.
Therefore, optimizing the user review management system is crucial for maintain -
ing hotel reputation and market competition. Hidayati used multi-source data analysis
methods, word cloud, topic modeling, regression analysis, and PLS-SEM models, to
address the single data source generalization in hotel and tourism research. The results
indicated significant differences in comment topics, emotion ratings, and length among
different platforms, suggesting that relying on a single data source may lead to bias [7]. Li
et al. proposed an integrated analysis model that combined econometrics and image pro-
cessing techniques to address the unclear role of user generated photos in hotel reviews.
Comments with user generated images were more helpful, providing a new perspective

Page 3 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
and practical inspiration for understanding and managing user generated content [8]. Xu
et al. combined bidirectional encoder and long short-term memory network to address
the ambiguity, insufficient utilization of contextual semantics, and inadequate quantifi -
cation of emotion intensity in fine-grained emotion analysis. The method achieved the
optimal F1 score in multiple datasets such as hotels and food delivery, and the emotional
intensity was quantified. The ablation experiment also verified the effectiveness of each
component of the model [ 9]. Xun et al. proposed a multi-source data analysis method,
combining word cloud, topic modeling, regression analysis, and PLS-SEM model, to
address the potential bias caused by relying on a single data source in hotel and tourism
research. The results showed significant differences in comment topics, emotional ten -
dencies, and length among different platforms, verifying the risk of generalization from
a single data source [ 10]. Kim et al. combined empirical and experimental research on
how cross-cultural differences affect online customer comment generation. The results
indicated that individualistic cultural users were more inclined to comment based on
recent ratings, while collectivist cultural users were more concerned with overall ratings,
revealing that differences in thinking patterns were a key driving factor for cross-cultural
differences [11].
Wąsowicz et al. proposed a content analysis method that combined quantitative and
qualitative methods to assess whether traditional scales accurately reflect consumers'
true emotions in hotel service quality evaluation. The model should be adjusted to better
fit customer feedback and a new service quality measurement tool was proposed [ 12].
Petrescu et al. proposed a two-stage mixed research method on how consumers evaluate
the online reputation of luxury hotel brands and respond to review fraud behavior, com-
bining interpersonal deception theory and social proof theory. Consumers mainly relied
on social proof heuristics and interpersonal communication heuristics to judge the use -
fulness of reviews, providing theoretical support and practical guidance for brand online
reputation management [ 13]. Lopes et al. proposed a machine learning classification
combined with regression analysis method to address the unclear impact of hotel online
review response strategies on bookings. The results indicated that strategies such as
guiding reviewers to private channels and taking defensive measures could significantly
improve bookings. Apologies and informal expressions had negative impacts, providing
data support and practical guidance for hotels to optimize their online response strate -
gies [14]. Guo et al. proposed a two-level empirical analysis method, combining negative
binomial regression and Tobit regression models, to address the impact of online review
information overload on selection decisions. There were differences in the complexity of
reviews among hotels, and consumers relied on different information processing paths,
providing empirical evidence for hotel managers to identify high-value review features
and optimize word-of-mouth management strategies [ 15]. Kazakov et al. proposed a
comprehensive emotion analysis, logistic regression, and semantic network analysis
method to address the lack of attention to service elements that were small but affected
satisfaction in hotel services. This method identified problems and improved services,
enhancing overall satisfaction and providing effective improvement strategies for hotel
and destination management [16].
In summary, in the field of emotion analysis and management of hotel user online
reviews, scholars have addressed the generalization from a single data source. Some
scholars have adopted multi-source data analysis, and teams have proposed integrated

Page 4 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
analysis models to clarify the role of user generated photos. However, existing research
mainly focuses on the method application and specific problems, and there is still insuf -
ficient research on the deep integration of emotion analysis into business scenarios and
multi-modal data. Therefore, the study employs a BERT-RF model for emotion analy -
sis of hotel reviews, leveraging the complementary strengths of deep semantic encoding
and statistical feature extraction. The PLS-SEM is used to analyze customer satisfaction,
thereby supporting hotel review management improvement.
3 Methods and materials
3.1 Emotion analysis method for hotel reviews based on BERT-RF
To address the limitations of existing sentiment analysis methods in handling implicit
expressions and domain-specific terminology in hotel reviews, an enhanced BERT-RF
fusion framework is proposed. Unlike typical ensemble approaches that merely concat -
enate features, the proposed method implements a hierarchical feature integration strat-
egy: BERT-generated embeddings serve as the semantic backbone, while RF performs
a weighted fusion of complementary statistical and lexical features, including TF-IDF,
Word2Vec vectors, and domain emotion dictionary scores, based on their contribu -
tion to classification accuracy. This design ensures that the model leverages both deep
language understanding and discriminative feature selection, thereby improving both
performance and generalizability in hotel review sentiment analysis. In the hotel opera -
tion, factors that affect customer satisfaction are complex and diverse, covering multiple
dimensions such as service, facilities, and perceived value. The core factors include ser -
vice quality, facilities and equipment, and perceived value. The secondary factors include
hygiene and cleanliness, catering services, convenience and location, and environment
and atmosphere. Special influencing factors include disease prevention and control mea-
sures and price sensitivity. Customer factors include the gap between expectations and
reality, personal preferences and needs, and emotions and scenarios. Under different
primary influencing factors, there are also different secondary influencing factors [ 17].
To assist hotel management personnel in finding improvement and optimization solu -
tions for hotel management from customer review results, this study conducts emotion
analysis on hotel reviews to quantify the impact of customer reviews. BERT is a pre-
trained language model with bidirectional Transformer encoders, which is stacked with
multiple layers of Transformer encoders and capture contextual relationships of words
in text through self-attention mechanisms. This model integrates Token Embedding,
Segment Embedding, and Position Embedding when converting text into vectors. The
key components include CLS tags and SEP tags, where CLS tags are added at the begin -
ning of sentences to represent the entire text, and SEP tags separate different sentences
or paragraphs to understand text structure [18]. Figure 1 displays the BERT.
In Fig. 1, the BERT has a three-layer structure, with the top layer being the output layer,
the middle layer being the Transformer layer, and the bottom layer being Token Embed-
ding. The pre-training tasks of the BERT include masking the language model and pre -
dicting the next sentence. The masked language model randomly masks certain words
in a text to predict the masked words based on context. The next sentence prediction is
to determine whether two sentences are consecutive paragraphs and train the model to
understand the semantic coherence. The model needs to obtain data before training. The
study utilizes web crawlers to obtain relevant review data for a certain hotel, including

Page 5 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
customer booking time, room type, review content, and ratings [ 19, 20]. To ensure the
representativeness and quality of the data, a self-built dataset is constructed with a total
of 42,815 online reviews. The reviews come from 32 hotels on China’s three major plat -
forms: Ctrip, Meituan and Fliggy. The data collection period covered from January 2023
to December 2024, ensuring temporal relevance and market contemporaneity. Prior to
analysis, a comprehensive data cleaning pipeline was implemented: (1) Delete duplicate
reviews posted by identical user IDs within a 24-h window; (2) Filter non-textual content
(e.g., pure emoticons, ratings without text) and non-Chinese reviews; (3) Eliminate sus -
pected promotional or “brushed” reviews based on excessively repetitive wording and
abnormal posting frequency patterns; (4) Exclude comments that are officially flagged by
the platform as spam or fake. However, simply mapping numerical ratings to sentiment
labels suffers from the well-known “rating-text inconsistency” problem. To ensure label
reliability, a three-step annotation protocol is designed: (1) Initial mapping—ratings 1–2
as negative (− 1), 3 as neutral (0), 4–5 as positive (+ 1); (2) Conflict detection—for each
review, a text-based sentiment score is computed using the domain lexicon (Eq.  3). If
the rating-based label and the lexicon score exhibit strong opposite polarities, the sam -
ple is flagged as a boundary case; (3) Manual arbitration—all boundary cases are inde -
pendently reviewed by two domain experts (experienced hotel managers), who re-label
based on the textual content, ignoring the numerical rating. Cases with unresolved dis -
agreement are excluded. Inter-annotator agreement (Cohen's Kappa) reached 0.87. After
this procedure, 4.3% of raw samples were re-labeled and 1.2% were excluded, ensuring
Fig. 1 The structure of BERT

Page 6 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
that final labels reflect genuine textual sentiment. Based on the above annotation proto -
col, the finalized sentiment classification tag is determined through a combination of ini-
tial mapping and manual arbitration. The baseline mapping rule is expressed as Eq. ( 1),
which serves only as the initial step before conflict detection and human correction.

𝑇𝑇𝑇𝑇𝑇𝑇 𝑇
⎧{
⎨{⎩
−1, 𝑖𝑖𝑖𝑖 1 ≤ 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 ≤ 2.5
0, 𝑖𝑖𝑖𝑖 2.5 𝑖 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 ≤ 3.5
1, 𝑖𝑖𝑖𝑖 3.5 𝑖 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 ≤ 5
 (1)
In Eq. (1), 𝑇𝑇𝑇𝑇𝑇𝑇 represents the customer comment classification tag. 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠  represents cus-
tomer rating. As emphasized in the three-step protocol, this mapping is not the final
label but the starting point. All samples that pass the conflict detection and manual arbi-
tration receive their final labels accordingly. After the three-step annotation protocol
and manual arbitration, the initial label distribution is heavily skewed toward positive
reviews (approx. 68% positive, 20% neutral, 12% negative). T o prevent the model from
learning a biased decision boundary that favors the majority class, a stratified random
down-sampling strategy is applied within each final label category. Before balancing, the
raw label distribution (after annotation) is approximately 68% positive, 20% neutral, and
12% negative. After down-sampling, the balanced training set contains approximately
33% samples per category (about 12,000 reviews per class, totaling about 36,000 valid
samples). During model training, the training, validation, and test sets are divided in
7:2:1 based on this balanced dataset. The test set comprises approximately 3,600 sam -
ples with equal class proportions, ensuring that the reported accuracy (90%) reflects the
model's genuine discriminative power across all sentiment classes, rather than a trivial
dominance of the positive class [21, 22].
When using the BERT model for emotion analysis of comments, it is necessary to
fine tune the BERT. The study chooses the BERT as the base model. When inputting the
model, CLS tags are added at the beginning of the sentence to generate the overall text
representation. SEP markers are added at the end of the sentence to separate paragraphs
or sentences. When constructing the embedding layer, character embedding maps each
Chinese character into a vector, segment embedding distinguishes different paragraphs,
and position embedding identifies the position information of words in the sequence.
Model adjustment includes modifications to the output layer and regularization strate -
gies. The output layer modification converts the output vector marked with CLS into a 2
× 1 dimension, with the first element containing classification task information and the
second element serving as the classification output. The regularization strategy involves
adding dropout layers and adjusting the final classification output through fully con -
nected testing. T o further enhance the accuracy of the BERT model in text emotion clas-
sification processing, the study takes RF for feature extraction, which is mainly used for
classification and regression tasks. The principle of RF is shown in Fig.  2.
In Fig.  2, RF improves the accuracy of hotel review emotion classification by extract -
ing multidimensional text features and integrating them with the BERT model. When
extracting the features of comment text, the number of Chinese characters in the com -
ment text is extracted through regular expressions as the basic feature. The Word2Vec
model converts segmented words into vectors. The Gensim module loads pre-trained
models. Each word is mapped to a 100-dimensional vector, and all word vectors of a sin-
gle comment are averaged to generate a comment level vector representation, capturing

Page 7 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
semantic relevance [ 23, 24]. In addition to this feature, the study also adds Term Fre -
quency-Inverse Document Frequency (TF-IDF) as a supplementary feature. The TF-IDF
is presented in Eq. (2).
 𝑡𝑡𝑖𝑖 − 𝑖𝑖𝑡𝑡𝑖𝑖 (𝑤𝑤𝑠𝑠𝑠𝑠𝑡𝑡𝑠𝑠 ) 𝑇
∑
𝑊𝑊
𝑖𝑖𝑖𝑖 𝑡𝑡𝑖𝑖 − 𝑖𝑖𝑡𝑡𝑖𝑖 (𝑤𝑤𝑖𝑖 )
5
 (2)
In Eq. ( 2), 𝑡𝑡𝑖𝑖 − 𝑖𝑖𝑡𝑡𝑖𝑖 (𝑤𝑤𝑠𝑠𝑠𝑠𝑡𝑡𝑠𝑠 ) represents the average of the top five TF-IDF ranked terms
in each comment. 𝑊𝑊 represents the number of terms in the top five TF-IDF rankings
in each comment. 𝑡𝑡𝑖𝑖 − 𝑖𝑖𝑡𝑡𝑖𝑖 (𝑤𝑤𝑖𝑖 ) represents the TF-IDF value of the -th term, where
ranges from 1 to 5. After extracting features from hotel reviews, the emotion tendency
of the reviews is calculated based on a general emotion dictionary and a hotel domain
dictionary. The calculation process is shown in Fig. 3.
The general dictionary contains 24,362 positive words and 28,454 negative words, with
an emotional intensity value of ± 1. The domain dictionary contains 187 positive domain
terms and 142 negative domain words. Based on the constructed emotion dictionary,
the emotion tendency of comments is calculated through dictionary matching and rules.
Firstly, the comments are split into multiple short sentence units according to punc -
tuation marks. Next, term matching is performed by traversing the term in each short
sentence, matching emotion terms, degree adverbs, and negation words in the emotion
dictionary. Finally, weight calculation is performed, assigning corresponding weights
based on term types, multiplying and accumulating to obtain the emotion score of the
short sentence, and then summarizing it into the overall comment score [ 25]. The cus -
tomer comment emotion score is shown in Eq. (3).
Fig. 2 Principle of random forest text feature extraction

Page 8 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174

𝑆𝑆𝑇
𝑁𝑁
∑
𝑗𝑗𝑖𝑖
𝑚𝑚
∑
𝑖𝑖𝑖𝑖
(−1) 𝑛𝑛 × 𝜔𝜔𝑎𝑎 × 𝜔𝜔𝑏𝑏 × 𝜔𝜔𝑐𝑐 (3)
In Eq. (3), 𝑁𝑁 represents the number of short sentence units in the comment. 𝜔𝜔𝑐𝑐  signifies
the negative term intensity value. 𝑚𝑚 represents the number of emotional terms in a sin -
gle short sentence. 𝜔𝜔𝑎𝑎  represents the intensity value of emotional words. 𝑛𝑛 signifies the
number of occurrences of negative words in a short sentence. 𝜔𝜔𝑏𝑏  represents the strength
value of degree adverbs. The word count of comments, Word2Vec vector, TF-IDF aver -
age, and emotion dictionary score are taken as combined features, and input them into
the RF model. T o describe the BERT-RF fusion mechanism, the feature construction,
concatenation order, and training paradigm are specified as follows:
(1) BERT embedding extraction (frozen): The pre-trained BERT-base-Chinese model
(12 layers, 768 hidden units) is used as a fixed feature extractor. For each review, the
tokenized text (padded/truncated to 128 tokens) is fed into BERT, and the pooled
output of the [CLS] token is extracted, yielding a 768-dimensional vector 𝐯𝐯𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏
. Crucially, the BERT parameters are frozen during RF training, that is, no back-
propagation flows from RF to BERT. This design choice deliberately decouples deep
semantic representation from statistical feature learning, preventing overfitting on
the limited hotel review dataset and ensuring that the statistical features (which
capture surface-level domain cues) are not suppressed by dominant BERT activations.
(2) Statistical feature construction: In parallel, a 106-dimensional statistical feature
vector 𝐯𝐯𝑠𝑠𝑏𝑏𝑎𝑎𝑏𝑏  is constructed by concatenating:
 Word2Vec average (100 dims): Each segmented word is mapped to a 100-dim pre-
trained vector, and averaged across all words in the review.
 TF-IDF top-5 mean (5 dims): The average of the top-5 TF-IDF values per review (as
defined in Eq. 2).
 Domain lexicon score (1 dim): The final sentence-level sentiment score (as defined in
Eq. 3).
Fig. 3 Comment score calculation process

Page 9 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
(3) Final input vector and RF training: 𝐯𝐯𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏  and 𝐯𝐯𝑠𝑠𝑏𝑏𝑎𝑎𝑏𝑏  are concatenated into a single
874-dimensional vector, which serve as the input feature for each review. The RF
(with 200 trees, Gini impurity as split criterion) is then trained on this combined
feature set using the manually-arbitrated and balanced labels described in the
previous annotation protocol. Since RF inherently performs feature importance
ranking during training, this architecture allows the model to automatically learn
the relative contribution of semantic versus statistical dimensions without requiring
joint gradient updates.
The feature extraction of RF can capture statistical features such as word frequency and
emotion intensity, which complement BERT's contextual semantic understanding and
improve the emotion classification accuracy.
3.2 Hotel customer satisfaction analysis method based on PLS-SEM
After taking the BERT-RF to analyze the emotional tendency of hotel customer reviews
towards the hotel, the influencing factors of customer satisfaction are analyzed to
enhance the hotel management level in a targeted manner. When analyzing hotel cus -
tomer satisfaction, the study uses the CCSI as the benchmark model for analysis. This
model is an indicator system developed and widely applied in China for systematically
measuring and evaluating consumer satisfaction with products/services purchased
and used in the Chinese market [ 26, 27]. The CCSI draws on mature international cus -
tomer satisfaction index models and has been localized based on the characteristics of
the Chinese market. The key variables involve customer expectations, perceived quality,
perceived value, customer satisfaction, customer complaints, and customer loyalty, as
shown in Fig. 4.
In Fig.  4, customer expectations affect their evaluation on perceived quality, and
both customer expectations and perceived quality jointly affect perceived value. Cus -
tomer expectations, perceived quality, and perceived value are the three main anteced -
ent variables that affect the satisfaction. Customer satisfaction directly affects customer
Fig. 4 Chinese customer satisfaction index model

Page 10 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
complaints and customer loyalty, and customer complaints can also have a negative
impact on customer loyalty. Based on the CCSI and the characteristics of the hotel
industry, the latent variables set for research include brand image, customers' overall
impression of hotel brand reputation, and market positioning. Customer expectations
are the expectations for hotel services, facilities, environment, etc. before check-in.
Quality perception evaluates the actual service quality of a hotel after check-in. Value
perception is a subjective judgment of “cost-effectiveness” based-price and experience.
Customer satisfaction exhibits the overall satisfaction. Customer complaints refer to
complaints that arise from dissatisfaction. Customer loyalty refers to the willingness to
repeat purchases or recommendations [28]. The constructed hotel customer satisfaction
index model is presented in Fig. 5.
Based on the model, hypotheses are made regarding the relationship among brand
image, customer expectations, quality perception, value perception, customer satisfac -
tion, and customer complaints. The relationship between brand image and related vari -
ables is as follows:
H1 Brand image actively affects customer expectations;
H2 Brand image actively affects quality perception;
H3 Brand image actively affects customer satisfaction;
H4  Brand image actively affects customer loyalty.
The relationship between customer expectations and related variables is as follows:
H5 Customer expectations actively affect quality perception;
H6 Customer expectations actively affect perceived value;
H7 Customer expectations actively affect customer satisfaction.
The relationship between quality perception and related variables is as follows:
H8  Quality perception positively affects value perception;
H9  Quality perception actively affects customer satisfaction.
The relationship between perceived value and related variables is as follows:
Fig. 5 Hotel customer satisfaction index model

Page 11 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
H10 Value perception has a positive impact on customer satisfaction.
The relationship between customer satisfaction and related variables is as follows:
The relationship between customer complaints and related variables is as follows:
H11  Customer satisfaction negatively affects customer complaints;
H12 Customer satisfaction actively affects customer loyalty.
H13 Customer complaints negatively affect customer loyalty.
The constructed model reflects seven latent variables of customer satisfaction. Corre -
sponding observable and measurable significant variables are designed for these seven
latent variables. Table 1 displays the constructed customer satisfaction evaluation index.
SEM is often used to discuss the relationship between latent variables and explicit
variables. Structural equation models include structural models and measurement mod -
els, where structural models mainly discuss the relationship between latent variables, as
displayed in Eq. (4).
 𝜂𝜂 𝑇𝐵𝐵 𝜂𝜂 + 𝛤𝛤𝛤𝛤 + 𝜁𝜁 (4)
In Eq. ( 4), 𝜂𝜂 signifies a vector composed of endogenous latent variables. 𝐵𝐵 signifies the
path coefficient matrix between endogenous latent variables. 𝛤𝛤  signifies the path coef -
ficient matrix of exogenous latent variables to endogenous latent variables. 𝛤𝛤 signifies
a vector composed of exogenous latent variables. 𝜁𝜁 represents the vector composed
of residual terms. The measurement model mainly discusses the relationship between
latent variables and explicit variables, as shown in Eq. (5).

{
𝑦𝑦𝑇 𝛬𝛬𝑦𝑦 𝜂𝜂 + 𝜀𝜀𝑦𝑦
𝑥𝑥𝑇 𝛬𝛬𝑥𝑥 𝛤𝛤 + 𝜀𝜀𝑥𝑥
 (5)
In Eq. ( 5), 𝑦𝑦 signifies the observation index of 𝜂𝜂. 𝑥𝑥 signifies the observation index of 𝛤𝛤.
𝛬𝛬𝑦𝑦  and 𝛬𝛬𝑥𝑥  represent the load matrix. 𝜀𝜀𝑦𝑦  and 𝜀𝜀𝑥𝑥  represent residual vectors. The modeling
Table 1 Hotel customer satisfaction evaluation index system
Structural
variables (latent
variables)
Measurement variable (significant
variable)
Structural
variables
(latent
variables)
Measurement variable
(significant variable)
Hotel image Overall brand impression Quality
perception
Room cleanliness
Facility and equipment level Comfort level of bedding
Service quality reputation Facility completeness
Environmental Atmosphere Design Bathroom experience
Value perception Price and experience matching degree Front desk response efficiency
Cost effectiveness perception Timeliness of room service
Additional service value Food and beverage quality
Satisfaction with member benefits Problem solving ability
Customer
satisfaction
The gap with the ideal hotel Comfort level in public areas
The gap from expectations Sound insulation effect
Overall satisfaction Security and Privacy
Customer
complaints
Complaint frequency Customer
loyalty
Willingness to stay again
Informal Complaints Recommendation intention
Customer
expectations
Expectations for hardware facilities Brand Priority Selection
Expectations for personalized services / /

Page 12 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
techniques of SEM include linear structural relationship method and PLS method,
among which the linear structural relationship method is based on covariance struc -
ture to construct SEM. In ideal conditions, the modeling effect of this method is better.
PLS increases the minimum value of residual structure on the basis of variance, which
has better application effect in causal prediction. Therefore, PLS is used for SEM. When
using PLS modeling technology, the measurement model has a reflection model and a
composition model, where the former is consistent with Eq.  ( 5) and the composition
model is shown in Eq. (6).

{𝜂𝜂 𝑇 𝜋𝜋𝜂𝜂𝑦𝑦+ 𝛿𝛿𝜂𝜂
𝑥𝑥𝑇 𝜋𝜋𝜉𝜉𝑥𝑥+ 𝛿𝛿𝜉𝜉
 (6)
In Eq.  (6), 𝜋𝜋𝜂𝜂 and 𝜋𝜋𝜉𝜉 represent the coefficient matrix. 𝛿𝛿𝜂𝜂 and 𝛿𝛿𝜉𝜉 represent the residual
vectors that make up the model. After using PLS technology to construct SEM, the
weights of customer satisfaction evaluation indicators can be obtained to calculate cus -
tomer satisfaction, as shown in Eq. (7).

𝜂𝜂 𝑇
𝑘𝑘
∑
𝑖𝑖𝑖𝑖
𝜔𝜔𝑖𝑖 𝑦𝑦𝑖𝑖  (7)
In Eq.  (7), 𝜔𝜔𝑖𝑖  signifies the weight of the indicator. 𝑘𝑘 signifies the number of indicators
corresponding to the latent variable. The customer satisfaction is shown in Eq. (8).

𝑆𝑆𝑆𝑆 𝑇 𝐸𝐸 [𝜂𝜂] − min [𝜂𝜂] max [𝜂𝜂] − min [𝜂𝜂]  (8)
In Eq. (8), 𝑆𝑆𝑆𝑆 represents customer satisfaction. 𝐸𝐸 [𝜂𝜂] represents the mean latent variable
of customer satisfaction. min [𝜂𝜂] and max [𝜂𝜂] represent the minimum and maximum
latent variables of customer satisfaction, respectively. T o rigorously assess the PLS-SEM
model, the evaluation includes: (a) internal consistency via Cronbach's α and composite
reliability (CR, threshold > 0.70); (b) convergent validity via average variance extracted
(AVE, >0.50); (c) discriminant validity via HTMT ratio (< 0.85); (d) predictive relevance
via Stone–Geisser Q 2 (positive values via blindfolding); and (e) path significance via
bootstrapping (5,000 resamples) with 95% bias-corrected confidence intervals. After
completing the PLS-SEM model construction and parameter estimation, it is necessary
to evaluate the goodness of fit of the model and the strength of the influence between
variables. This study mainly reports and explains the following three key indicators: (1)
R2: represents the proportion of variance of endogenous latent variables that can be
explained by other latent variables in the model, with values ranging from 0 to 1. A larger
value indicates a stronger predictive ability of the model. (2) F2: evaluates the strength of
the influence of a specific antecedent variable on endogenous latent variables. F 2 val -
ues greater than 0.02, 0.15, and 0.35 respectively indicate weak, moderate, and strong
effects. (3) H2: evaluates the discriminant validity between latent variables and measures
whether the correlation between measurement items of different latent variables is too
high. Its value is the geometric mean of the correlation coefficients between all measure-
ment items of two latent variables. It is generally believed that HTMT values below 0.85
or 0.90 indicate good discriminant validity. These indicators will provide a quantitative
basis for subsequent model fitting analysis and path effect discussion.

Page 13 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
4 Results
4.1 Hotel review text emotion analysis verification
The research experiment is conducted on a Linux server and the pre-trained language
model is fine-tuned using the PyTorch 1.12 framework. Emotion analysis adopts the
BERT Chinese basic model, where the input text is segmented and truncated to 128
characters, and the embedding layer integrates Token, Segment, and Position vectors.
During the fine-tuning phase, the Adam optimizer is used to train for 10 iteration cycles,
with the training, validation, and test sets divided into 7:2:1 parts. RF feature extraction
integrates Word2Vec word vector, TF-IDF top five word mean, and domain emotion
dictionary score, with a tree size of 200 and node splitting criterion of Gini coefficient.
PLS-SEM is implemented through SmartPLS 4.0, using the Path Weighting Scheme
algorithm with a maximum iteration count of 300 and a convergence threshold of 10 –7.
The experiment takes a self-built dataset, which includes relevant reviews from 32 hotels
on three different platforms. To verify the effectiveness, different features are com -
bined separately, and the accuracy under different feature combinations is analyzed. The
results are shown in Fig. 6.
Figure 6a shows the impact of domain emotion dictionary features, BERT features, and
Word2Vec + BERT features on accuracy. Figure 6b shows the impact of TF-IDF + BERT,
TF-IDF + Word2Vec, and all feature combinations on model accuracy. When combining
domain emotion lexicon features with BERT features, the model accuracy was approxi -
mately 86%. When using only BERT features, the accuracy was about 84%. The accu -
racy of Word2Vec+BERT was about 88%. This indicates that combining BERT features
with other features can improve the analysis accuracy, with the Word2Vec+BERT having
a relatively better effect. The accuracy of the TF-IDF+BERT was about 85%. The accu -
racy of TF-IDF+Word2Vec was about 87%. When all features were combined, the model
accuracy reached about 90%. This further demonstrates that the fused multiple features
can more comprehensively capture emotional information in text, thereby significantly
improving the performance of the model. The combination of all features performs best
in this comparison group. The study further compares the accuracy and loss conver -
gence during model training, and the results are shown in Fig. 7.
Figure 7a shows the training accuracy, and Fig. 7b compares the convergence loss. The
accuracy showed a gradually increasing trend. Starting from the initial stage, the accu -
racy was about 75%. As the number of training iterations increased, the accuracy con -
tinued to improve. After a certain number of training sessions, the accuracy gradually
Fig. 6 The influence of different combination features on accuracy

Page 14 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
stabilized and eventually reached 92%. The model can learn the features in the data
during the training process, and its ability to classify hotel review emotions gradually
increases and stabilizes. The loss degree was relatively high in the early stages of training,
around 0.6, and rapidly decreased as the training progressed. During the training pro -
cess, the loss continued to decrease and eventually stabilized at 0.15. This indicates that
the model can continuously optimize parameters during the training process, reduce the
error between predicted values and actual values, and gradually accurately model hotel
review emotion analysis. The study further analyzes the accuracy changes of different
models on the validation and test sets. The results are shown in Fig. 8.
Figure  8a presents the accuracy changes on the validation set, and Fig.  8b presents
the accuracy changes on the test set. The accuracy of the BERT-RF on the validation set
was about 89%, and the model exhibited high accuracy on the validation set, indicating
that it also has strong emotion classification ability on untrained data. The accuracy of
the RNN on the validation set was about 78%, which was slightly lower than that of the
BERT-RF model, indicating that the generalization ability of the RNN model in handling
hotel review emotion analysis tasks was relatively weak. Overall, the BERT-RF model
shows significant advantages in both the validation and test sets, with significantly
higher accuracy than that of the RNN and LSTM models, and stable performance with
strong generalization ability on both datasets. This fully demonstrates that the BERT-
RF model has better performance and reliability in hotel review emotion analysis tasks,
and can more accurately classify and analyze the emotions of hotel users' online reviews,
Fig. 8 Accuracy changes of different models

Fig. 7 Changes in accuracy and loss during model training

Page 15 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
providing strong model support for subsequent research on improving hotel manage -
ment based on emotion analysis. Further analysis is conducted on the precision, F1
score, and recall using the designed model and other models, as presented in Table 2. To
rigorously evaluate the proposed BERT-RF, the original BERT-base-Chinese is included
as a direct baseline, which shares the same backbone and training setup, thereby isolat -
ing the contribution of the RF-based feature enhancement.
According to Table  2, the BERT-RF model performed the best in hotel review emo -
tion classification tasks, with significantly higher precision, F1 score, and recall rate than
those of RNN and LSTM models in classifying negative, neutral, and positive reviews.
This fully demonstrates that the BERT-RF model has stronger advantages in handling
emotional analysis of hotel users' online reviews, and can more accurately identify and
classify reviews with different emotional tendencies, providing a more reliable basis for
hotels to improve management based on emotional analysis. However, the performance
of RNN and LSTM models in this task is relatively poor, which may have limitations
when dealing with complex text emotion features. Compared with the original BERT,
BERT-RF improves overall accuracy from 88.0% to 90.1%, with a McNemar test chi-
square of 14.73 ( p < 0.001), confirming that the statistical feature fusion yields statisti -
cally significant gains, especially in neutral and negative reviews.
To quantify the individual contribution of each feature module and validate the effec -
tiveness of the dynamic re-weighting fusion mechanism over simple feature concatena -
tion, a systematic ablation experiment is conducted. Five model variants are compared
on the same balanced test set:
Model A (BERT baseline): Only the frozen 768-dim BERT [CLS] embedding is used as
input to a standard RF classifier (no statistical features).
Model B (BERT + RF with concatenation): The 768-dim BERT embedding is concate -
nated with all statistical features (Word2Vec, TF-IDF, lexicon) and fed into RF. This rep-
resents the naive stacking baseline.
Model C (BERT + W2V + TF-IDF, no lexicon): Same as Model B, but excluding the
domain lexicon score.
Model D (BERT + lexicon, no W2V/TF-IDF): Same as Model B, but excluding Word -
2Vec and TF-IDF.
Model E (Full model with dynamic re-weighting): the proposed method, where RF
internally adjusts feature sampling weights based on Gini impurity gain comparison dur-
ing training.
Table 2 The precision, F1 score, and recall of emotion classification for different models
Model Emotion classification Precision F1 score Recall
BERT − 1 0.78 0.79 0.80
0 0.79 0.74 0.69
1 0.87 0.88 0.90
BERT-RF − 1 0.81 0.82 0.83
0 0.82 0.77 0.72
1 0.90 0.91 0.93
RNN − 1 0.68 0.70 0.73
0 0.72 0.68 0.64
1 0.83 0.87 0.91
LSTM − 1 0.66 0.69 0.73
0 0.71 0.66 0.61
1 0.84 0.84 0.84

Page 16 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
Table 3 presents the accuracy, macro F1, and per-class F1 scores for all variants.
The ablation results reveal three key insights. First, comparing Model A vs. Model B,
adding statistical features improves accuracy by 4.5%, demonstrating that BERT's con -
textual embeddings alone are insufficient for capturing domain-specific intensity and
keyword frequency patterns in short hotel reviews. Second, comparing Models C and D
against Model B, both the lexicon score and the TF-IDF/Word2Vec features contribute
positively, but the lexicon score has a slightly stronger effect on negative review iden -
tification (F1 increases from 0.847 to 0.862 when adding the lexicon), confirming its
value for detecting subtle complaint expressions. Most importantly, comparing Model
B (simple concatenation) with Model E (proposed dynamic re-weighting), the latter
achieves a 1.4% absolute accuracy gain and a 0.017 gain in macro F1, even though both
use the same set of features. This improvement is attributed to the adaptive weighting
mechanism, which prevents redundant statistical features from overshadowing BERT
embeddings when they carry little marginal information, while amplifying those that
complement semantic understanding. This confirms that the fusion strategy, rather than
mere feature accumulation, constitutes the substantive algorithmic improvement of the
proposed BERT-RF framework.
4.2 Verification of hotel customer satisfaction analysis
The study first conducts a fitting analysis on the customer satisfaction model, as pre -
sented in Table 4. The H2 of customer expectations was 0.648, with an R 2 value of 0.692
and an F2 value of 0.482. The high values of H 2 and R2 indicate that the customer expec-
tation can be well explained by other variables, and their own influence on other vari -
ables is significant. The F 2 value was 0.482, demonstrating a strong correlation effect
between customer expectations and other variables. From the fitting analysis results,
most of the variables had good fitting indicators, indicating that it could explain the rela-
tionships between these variables. However, the fitting index of customer complaints
was relatively low. This may further analyze its role and influencing factors in the model,
Table 3 Results of ablation test
Model variant Accuracy Macro F1 F1 (Positive) F1 (Neutral) F1 (Negative)
A. BERT only (RF baseline) 0.842 0.812 0.862 0.742 0.832
B. BERT + all stats (concatenation) 0.887 0.865 0.898 0.788 0.862
C. BERT + W2V + TF-IDF (no lexicon) 0.871 0.848 0.885 0.765 0.847
D. BERT + lexicon (no W2V/TF-IDF) 0.863 0.839 0.877 0.758 0.841
E. Full model (dynamic re-weighting) 0.901 0.882 0.91 0.81 0.88
Table 4 Fitting analysis of customer satisfaction model
Variable H2 R2 F2 Cronbach's α CR AVE Highest HTMT Q2
Brand image 0.683 / / 0.813 0.872 0.621 0.341 /
Customer expectations 0.648 0.692 0.482 0.784 0.851 0.584 0.483 0.532
Quality perception 0.672 0.509 0.351 0.836 0.887 0.638 0.524 0.418
Value perception 0.581 0.612 0.391 0.862 0.908 0.712 0.724 0.501
Customer satisfaction 0.759 0.713 0.542 0.801 0.859 0.593 0.724 0.586
Customer complaints 0.492 0.549 0.284 0.761 0.824 0.552 0.643 0.347
Customer loyalty 0.581 0.602 0.313 0.829 0.883 0.651 0.698 0.427
Whole 0.631 0.621 0.392 / / / / /
Thresholds / / / > 0.70 > 0.70 > 0.50 < 0.85 > 0

Page 17 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
or consider modifying and improving the explanatory ability for customer complaints as
a variable.
Table 4 reports all key measurement and structural model evaluations in one consol -
idated view. All Cronbach's α and CR values exceed 0.70, all AVE values exceed 0.50,
and the highest HTMT across all construct pairs is 0.724 (between Value Perception and
Customer Satisfaction), well below the 0.85 threshold, collectively confirming strong
reliability, convergent validity, and discriminant validity. The positive Q2 values (ranging
from 0.347 to 0.586) confirm satisfactory predictive relevance for all endogenous vari -
ables. The R2 and F2 values, as previously interpreted, further indicate adequate explana -
tory power and effect sizes. Bootstrapping (5,000 resamples) confirms that 12 out of 13
hypothesized paths are statistically significant at p < 0.05. The only non-significant path
is H4 (Brand Image → Customer Loyalty, β = 0.068, p = 0.073), which is consequently
excluded from the final revised model. All significant path coefficients and their bias-
corrected 95% confidence intervals are consistent with the directions and magnitudes
reported in Fig. 9.
After correcting the model path coefficient test, the correlation coefficient test is con -
ducted on the latent and significant variables. The correlation coefficient matrix of the
latent variables is presented in Table 5. The correlation coefficient between value percep-
tion and customer satisfaction was 0.774, which was the strongest positive correlation
in the table. This indicates that if customers have a high subjective judgment for “cost-
effectiveness” , their overall satisfaction is also higher, which verifies H10. The correlation
Table 5 Latent variable correlation coefficient matrix
/ Brand
image
Customer
expectations
Quality
perception
Value
perception
Customer
satisfaction
Customer
complaints
Cus-
tomer
loyalty
Brand image 1 / / / / / /
Customer
expectations
0.041 1 / / / / /
Quality
perception
0.162 0.303 1 / / / /
Value
perception
0.113 0.084 0.342 1 / / /
Customer
satisfaction
0.021 0.042 0.093 0.774 1 / /
Customer
complaints
− 0.121 − 0.071 − 0.079 − 0.373 − 0.352 1 /
Customer
loyalty
0.082 0.094 0.102 0.702 0.749 0.327 1
Fig. 9 Revised customer satisfaction model path coefficient test

Page 18 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
coefficient between customer satisfaction and customer loyalty was 0.749, showing a
strong positive correlation. High customer satisfaction may result in repeat purchases
or recommendation behavior, consistent with H12. The correlation coefficient between
value perception and customer loyalty was 0.702, signifying a strong correlation. This
indicates that value perception directly affects satisfaction, and indirectly affects loy -
alty through satisfaction, reflecting the transmission path of “cost-effectiveness → sat-
isfaction → loyalty” . The correlation coefficient was 0.342, showing a moderate positive
correlation. If customers have a high actual evaluation of hotel service quality, they are
more likely to recognize the value of the hotel, supporting H8. The correlation coeffi -
cient between quality perception and customer expectations was 0.303, indicating a
positive correlation. This may reflect the match between customers' expectations before
check-in and their actual quality perception. Customers with higher expectations may
be more sensitive to quality, but the correlation coefficient is lower, indicating limited
correlation between the two. The correlation coefficient between customer complaints
and value perception was − 0.373, and the correlation coefficient with customer satis -
faction was − 0.352, both showing a moderate negative correlation. This indicates that
the lower the perceived value and satisfaction, the more likely customers are to engage
in complaining behavior, verifying H11. The correlation coefficient between customer
complaints and customer loyalty is 0.327, appearing positive at the bivariate level. How -
ever, this zero-order correlation should not be interpreted as evidence that complaints
enhance loyalty. Instead, it reflects a classic statistical suppression effect. In the struc -
tural model, after controlling for Customer Satisfaction and Value Perception, which
mediate the complaint-loyalty relationship, the direct path coefficient for H13 is signif -
icantly negative (β = − 0.242, p < 0.001), consistent with theoretical expectations. The
positive raw correlation is plausibly attributable to the nature of the sample: custom -
ers who are frequent reviewers on OTA platforms (e.g., Ctrip, Meituan) tend to be both
more loyal (higher revisit rates) and more vocal about service failures, thereby creating
a positive confounding at the descriptive level. Thus, caution is advised against equating
complaint frequency with complaint resolution quality. The structural evidence supports
that unaddressed complaints ultimately undermine loyalty, whereas the raw correlation
captures a composition effect of active users rather than a causal benefit of complaints.
The study further analyzes the customer satisfaction index, as displayed in Table  6.
Customers have extremely high expectations for hotel hardware, which may be a key
focus of hotel promotion or a general trend in the industry. It is necessary to ensure that
the actual facilities meet the standards to avoid a gap in expectations. Room cleaning is a
fundamental aspect of hotel services. A high score indicates that this dimension has met
the basic needs and can be maintained as a benchmark for service. The overall satisfac -
tion score was relatively high, indicating that the hotel had not made significant mistakes
in core services and the customer experience was still acceptable. The willingness to stay
again and the priority of brand selection reflect the customer's recognition, which is the
core manifestation of loyalty. This advantage needs to be consolidated through continu -
ous optimization. The score for the gap between the ideal hotel and expectations was
lower than the overall satisfaction, indicating that the customer's actual experience did
not fully meet their psychological expectations. It is necessary to focus on narrowing
the “expectation-experience” gap. There was a significant gap between customer expec -
tations and actual quality perception and value perception. Excessive promises should

Page 19 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
be avoided and the actual service experience can be improved, especially in weak areas
such as front desk response and bathroom facilities. To address the low perceived value
scores, customers can enhance their subjective perception for “cost-effectiveness” by
optimizing the pricing system, adding free additional services, and improving member
benefits.
The study further analyzes the correlation between emotion classification, satisfac -
tion drive, and management shortcomings, as shown in Table  7. The overall accuracy of
emotion classification for all comments reached 90%, and the p-value was below 0.001,
demonstrating that the result had extremely high statistical significance, indicating that
the model performed well in the overall emotion classification task. The value percep -
tion → satisfaction path coefficient was 0.774, with a p-value below 0.001, demonstrating
that value perception has positive direct impacts on satisfaction. The higher the subjec -
tive judgment on the “cost-effectiveness” , the higher their overall satisfaction. The cus -
tomer's expected value for hardware facilities was 7.832, but the actual perceived value
was only 6.325. This reflects a significant gap between the customer's high expectations
for hardware facilities and the actual perceived value, which is one of the important rea -
sons for the low perceived value score. The room cleanliness score of 6.790 was relatively
high, indicating that the hotel performed better in this area and met the basic needs of
Table 6 Satisfaction index of latent and significant variables in customer satisfaction
Structural
variables (la-
tent variables)
Index Measurement vari-
able (significant
variable)
Index Structural
variables
(latent
variables)
Index Measurement vari-
able (significant
variable)
Index
Hotel image 6.242 Overall brand
impression
6.561 Quality
perception
6.353 Room cleanliness 6.790
Facility and equipment
level
6.143 Comfort level of
bedding
6.132
Service quality
reputation
6.542 Facility completeness 6.138
Environmental Atmo-
sphere Design
6.023 Bathroom experience 6.123
Value
perception
6.325 Price and experience
matching degree
6.543 Front desk response
efficiency
6.132
Cost effectiveness
perception
6.261 Timeliness of room
service
6.231
Additional service
value
6.352 Food and beverage
quality
6.325
Satisfaction with mem-
ber benefits
6.143 Problem solving
ability
6.152
Customer
satisfaction
6.389 The gap with the ideal
hotel
6.134 Comfort level in
public areas
6.323
The gap from
expectations
6.210 Sound insulation
effect
6.151
Overall satisfaction 6.523 Security and Privacy 6.173
Customer
complaints
5.670 Complaint frequency Customer
loyalty
6.170 Willingness to stay
again
6.230
Informal Complaints Recommendation
intention
6.110
Customer
expectations
7.447 Expectations for hard-
ware facilities
7.832 Brand Priority
Selection
6.235
Expectations for per-
sonalized services
7.062 / /

Page 20 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
customers. The bathroom experience score of 6.123 was relatively low, which was a weak
link in quality perception and needed to be improved as a key focus.
5 Discussion
The study systematically analyzes the emotional tendencies and satisfaction driving
mechanisms of hotel users' online reviews by integrating multi-feature text analysis
with an improved PLS-SEM model. The research results validate the effectiveness of the
BERT-RF in emotion analysis, and reveal the key role of value perception as the core
driver of satisfaction through PLS-SEM path analysis, as well as the significant negative
impact of customer complaints on value perception.
Existing scholars often rely on single text analysis, while the research method inte -
grates text features, statistical features, and domain emotion dictionaries, significantly
improving classification accuracy. This is consistent with the conclusion drawn by El-
Said O et al. to emphasize the complementarity of multi-source data [ 29]. Further
research quantified the gain mechanism of multi-modal fusion through feature com -
bination experiments, and all feature combinations improved the accuracy from 84 to
90%, verifying the warning about the “risk of generalization from a single data source”
drawn by Wu [30]. Compared to traditional models, BERT-RF performs better in nega -
tive comment recognition and neutral comment classification. This result supports the
improvement approach to the insufficient utilization of contextual semantics drawn by
Rassal et al. [31]. The study further addresses the limitations of BERT in handling sparse
features by introducing the feature extraction capability of RF, providing a new solu -
tion for fine-grained emotion analysis. Path analysis shows that value perception has the
strongest direct impact on satisfaction, far exceeding quality perception and customer
expectations. This discovery echoes the doubts drawn by Rafiki et al. [ 32]. Traditional
service quality scales may underestimate the weight of “cost-effectiveness” in consumer
decision-making. Based on explicit variable measurement, the significant gap between
customers' expectations of “hardware facilities” and their actual “value perception” is a
Table 7 Analysis results of the correlation between emotion classification, satisfaction drive, and
management shortcomings
Dimension Indicators/Variables Classification/Grouping Value Significance
Emotion
classification
performance
Overall accuracy All comments 90% p < 0.001
Positive review recall rate Emotional label = 1 93% p < 0.001
Accuracy rate of negative
comments
Emotional label = − 1 81% p < 0.001
Satisfaction path
coefficient
Value perception → Satisfaction Direct effect 0.774 p < 0.001
Customer Expectations →
Satisfaction
Direct effect − 0.21 p < 0.001
Customer complaints → Value
perception
Direct effect − 0.373 p < 0.001
Satisfaction → Loyalty Direct effect 0.749 p < 0.001
Key significant
variable score
Value perception related Expectations for hardware
facilities
7.832 /
Actual value perception 6.325 /
Quality perception related Room cleaning 6.790 /
Bathroom experience 6.123 /
Complaint handling related Front desk response efficiency 6.132 /
Loyalty related Willingness to stay again 6.230 /

Page 21 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
shortcoming in satisfaction, providing empirical evidence for hotels to optimize pricing
strategies and additional services.
By accurately identifying weak links through satisfaction indices, hotels can prioritize
allocating resources to areas related to “cost-effectiveness perception” rather than blindly
improving all service dimensions. Based on the empirical findings, the study propose
four actionable managerial strategies:
(1) Pinpoint service defects: Focus physical upgrades and staff training on the weakest
links identified by sentiment analysis: bathroom experience (6.123) and front-desk
response (6.132).
(2) Value-driven pricing: Given value perception's strongest impact on satisfaction (β =
0.774) and the large expectation-perception gap (7.832 vs. 6.325), adopt transparent
pricing with added-value bundles (e.g., late check-out, loyalty points) to boost
perceived cost-effectiveness without lowering base rates.
(3) Review triage: Use BERT-RF to classify reviews by sentiment and topic: prioritize
high-intensity negative reviews for immediate response and aggregate recurring low-
score themes for periodic improvement planning.
(4) Proactive complaint interception: Since complaints reduce value perception (β
= − 0.373), set a daily sentiment threshold to trigger alerts, enabling managers to
proactively contact dissatisfied guests before negative reviews are posted.
6 Conclusion
The research aims to construct a closed-loop system of “emotion analysis—problem
diagnosis—management optimization” , which accurately analyzes the emotion of hotel
text reviews and quantifies the satisfaction driving mechanism, helping hotels shift from
passive response to negative reviews to active optimization, and improving customer
trust and platform ratings. The research employed a BERT-RF model that combines
BERT's semantic encoding with RF's feature integration capability for emotion analy -
sis of hotel reviews. Based on the CCSI, a hotel specific indicator system was designed
with seven latent variables. The improved PLS-SEM method was used to analyze path
relationships, and the satisfaction index was calculated using explicit variable weights.
The emotion classification accuracy of the BERT-RF reached 90%, with a positive review
recall rate of 93% and a neutral review accuracy rate of 82%. The customer had high
expectations for hardware facilities, with a score of 7.832, but the lowest perceived value
score was only 6.325, and the “expectation-experience gap” path coefficient significantly
lowered the overall satisfaction. The research has verified that multi-modal data fusion
improves emotion analysis accuracy, and the BERT-RF model serves as an effective
approach for hotel review classification. Hotels need to prioritize optimizing their per -
ceived “cost-effectiveness” and narrowing the gap between “expectation-experience” . The
PLS-SEM model does not consider the potential impact of moderating variables like cul-
tural differences and regional characteristics on satisfaction. Future research will intro -
duce time series analysis to track the long-term evolution of satisfaction driving factors
and verify the differences in the mechanism of negative evaluation generation in cross-
cultural scenarios.
Author contributions
X.X. provided the concept, acquired the funding and wrote the draft, and C.Q. prepared the figures and tables, Y.Q.
revised the paper critically. All authors reviewed this paper carefully and approved this submission.

Page 22 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
Funding
The research is supported by: 2025 Hainan Provincial Department of Education Higher Education Research Project:
Research on the Impact of Corporate Social Responsibility of Tourism Hotel Enterprises Hainan Province on Green
Consumption Behavior Based on S-O-R Theory (Fund Number: Hnky2025-97).
Data availability
All data generated or analyzed during this study are included in this article. Further enquiries can be directed to the
corresponding author.
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Competing interests
The authors declare no competing interests.
Received: 19 May 2026 / Accepted: 3 September 2026
References
1. Gao J. Optimizing hotel revenue management through dynamic pricing algorithms and data analysis. J Comput Methods
Sci Eng. 2025;25(2):1200–9. https://doi.org/10.1177/14727978241298467.
2. Moreno Brito YL, Ban HJ, Kim HS. Ecological hotels’ customer satisfaction through text mining of online reviews: a case of
Ecuador hotels. J Hosp Tour Insights. 2024;7(3):1532–52. https://doi.org/10.1108/JHTI-09-2022-0467.
3. Nicolau JL, Xiang Z, Wang D. Daily online review sentiment and hotel performance. Int J Contemp Hosp Manag.
2024;36(3):790–811. https://doi.org/10.1108/IJCHM-05-2022-0594.
4. Saha P , Biswas A. Seal the deal: unleashing the magnitude of online reviews, website quality and trust for seamless hotel
reservations. Int J Prod Perform Manag. 2025;74(4):1125–55. https://doi.org/10.1108/IJPPM-04-2024-0272.
5. Akel G, Noyan E. Exploring the criteria for a green and smart hotel: insights from hotel managers’ perspectives. J Hosp Tour
Insights. 2024;7(5):2992–3012. https://doi.org/10.1108/JHTI-08-2023-0555.
6. Lee HSK, Wang J, Moreno-Brito YL, et al. Linguistic insights into customer satisfaction: an exploratory analysis of online
reviews for gaming destination resorts in Las Vegas. J Hosp Tour Technol. 2025;16(1):73–90.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / J H T T - 0
5 - 2 0 2 3 - 0 1 4 7     .
7. Hidayati NN. Improving aspect-based sentiment analysis for hotel reviews with latent Dirichlet allocation and machine
learning algorithms. Regist J Ilm Tek Sist Inf. 2023;9(2):144–59. https://doi.org/10.26594/register.v9i2.3441.
8. Li C, Kwok L, Xie KL, Liu J, Ye Q. Let photos speak: the effect of user-generated visual content on hotel review helpfulness. J
Hosp Tour Res. 2023;47(4):665–90. https://doi.org/10.1177/10963480211019113.
9. Xu J, Zhang J, Song LY, et al. Fine-grained sentiment analysis of online reviews based on ROBERTa-BiLSTM-CRF. Syst Eng
Theory Pract. 2023;43(12):3519–36. https://doi.org/10.12011/SETP2022-2001.
10. Xun J, Wang Y, Chong WK, Wong E, Fan X. Maze of conveniences: re-examining hotel reviews and social media data. Ind
Manag Data Syst. 2025;125(5):1946–76. https://doi.org/10.1108/IMDS-09-2024-0881.
11. Kim JM, Lee E, Yoon Y. Bringing culture into the picture: cross-cultural differences in online customer reviews. Int Mark Rev.
2023;40(3):528–46. https://doi.org/10.1108/IMR-07-2020-0167.
12. Wąsowicz-Zaborek E. Content analysis of hotel reviews as a quality management tool: preliminary verification of the
SERVQUAL scale. Turyzm. 2023;33(1):29–40. https://doi.org/10.18778/0867-5856.33.1.03.
13. Petrescu M, Gironda J, O’Leary KB. Consumer-brand heuristics in luxury hotel reviews. J Prod Brand Manag. 2024;33(4):430–
42. https://doi.org/10.1108/JPBM-01-2023-4303.
14. Lopes AI, Malthouse EC, Dens N, De P . Is webcare good for business? A study of the effect of managerial response strate-
gies to online reviews on hotel bookings. J Serv Manag. 2024;35(6):22–41. https://doi.org/10.1108/JOSM-05-2023-0219.
15. Guo Q, Yan J. The impact of online reviews on hotel ratings through the lens of elaboration likelihood model: a text min-
ing approach. KSII Trans Internet Inf Syst. 2023;17(10):2609–26. https://doi.org/10.3837/tiis.2023.10.001.
16. Kazakov S, Cuesta-Valiño P , Butkouskaya V, Muravsky D. Improving guest satisfaction by identifying hotel service micro-
elements failures through deep learning of online reviews. Cuad Gest. 2025;25(1):71–88.  h t t p s : / / d o i . o r g / 1 0 . 5 2 9 5 / c d g . 2 4 2 1
9 1 s k     .
17. Chiu W, Cho H. The model of goal-directed behavior in tourism and hospitality: a meta-analytic structural equation mod-
eling approach. J Travel Res. 2022;61(3):637–55. https://doi.org/10.1177/0047287521991242.
18. Hasan AAT, Rahman MT. Factors influencing green hotel revisit intentions after the COVID-19 in Bangladesh. Int J Tour
Cities. 2023;9(1):143–58. https://doi.org/10.1108/IJTC-03-2022-0065.
19. Shehata AE, Khan MA, Khalid R, Raza M, Selem KM. Consequences of paradoxical leadership in the hotel setting: moderat-
ing role of work environment. J Hosp Mark Manag. 2023;32(5):670–93. https://doi .org/10.108 0/19368623. 2023.219 0318.
20. Rezaei F, Raeesi Vanani I, Jafari A, Kakavand S. Identification of influential factors and improvement of hotel online user-
generated scores: a prescriptive analytics approach. J Qual Assur Hosp Tour. 2024;25(4):1070–109.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 /
1 5 2 8 0 0 8 X . 2 0 2 2 . 2 1 4 6 6 2 0     .
21. Nguyen VT, Phong LT, Chi NTK. The impact of AI chatbots on customer trust: an empirical investigation in the hotel indus-
try. Consum Behav Tour Hosp. 2023;18(3):293–305. https://doi.org/10.1108/CBTH-06-2022-0131.

Page 23 of 23
Xia et al. Discover Artificial Intelligence           (2026) 6:1174
22. Ahmed MEAM. Development of a management framework for energy efficiency for sustainability of hotels in Jeddah,
Saudi Arabia using structural equation modelling. J Adv Res Appl Sci Eng Technol. 2024;36(1):159–75.  h t t p s : / / d o i . o r g / 1 0 . 3 7
9 3 4 / a r a s e t . 3 6 . 1 . 1 5 9 1 7 5     .
23. Christin GAD, Nugraha AKN. The impact of online review and price on hotel booking intention at online travel agency:
trust as a mediating variable. Int J Electron Commer Stud. 2023;13(4):159–84. https://doi.org/10.7903/ijecs.2115.
24. Elshaer AM, Marzouk AM. Memorable tourist experiences: the role of smart tourism technologies and hotel innovations.
Tour Recreat Res. 2024;49(3):445–57. https://doi .org/10.108 0/02508281. 2022.202 7203.
25. Olorunsola VO, Saydam MB, Lasisi TT. Customer experience management in capsule hotels: a content analysis of guest
online review. J Hosp Tour Insights. 2023;6(5):2462–83. https://doi.org/10.1108/JHTI-03-2022-0113.
26. Yu W, Cui F, Hou Z. The evolution of consumers’ demand for hotels under the public health crisis: opinion mining from
online reviews. Curr Issues Tour. 2023;26(12):1974–90. https://doi.org/10.1002/csr.2508.
27. Murtaza SH, Khan A, Mustafa SM. Eco‐centric success: stakeholder approaches to sustainable performance via green
improvisation behavior and environmental orientation in the hotel industry. Bus Strategy Environ. 2024;33(7):7273–86.
https://doi.org/10.1002/bse.3860.
28. Jalali N, Moon S, Kim MY. Profiling diverse reviewer segments using online reviews of service industries. J Mark Anal.
2023;11(2):130–48. https://doi.org/10.1057/s41270-022-00163-w.
29. El-Said O, Elhoushy S, Al Bulushi S. How do online review valence and ratings interact with consumer-generated visuals?
Serv Ind J. 2024;44(15–16):1181–210. https://doi .org/10.108 0/02642069. 2022.214 2214.
30. Wu J, Fu C, Zhao E, Sun S, Wang S. What makes a better hotel selection? A hybrid approach considering tourists’ prefer-
ence and review helpfulness. Curr Issues Tour. 2025;28(10):1570–94.
31. Rassal C, Correia A, Serra F. Understanding online reviews in all-inclusive hotels servicescape: a fuzzy set approach. J Qual
Assur Hosp Tour. 2024;25(6):1607–34. https:   //d oi. or g/10 .1080/15 2800 8X.20 23.2167761.
32. Rafiki A, Nasution MDTP , Rossanty Y. CRM impact on customer satisfaction in Islamic-based hotels: exploring a mediation
model. J Islam Mark. 2024;15(12):3425–44. https://doi.org/10.1108/JIMA-08-2023-0265.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
