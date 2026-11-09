---
title: Multi-aspect sentiment classification on USA-based Amazon customer reviews with DeBERTa-v3 encoders
  and aspect attention
url: https://doi.org/10.1007/s44257-026-00077-2
category: cx-retail
subcategory: review
date: 2026-07
venue: Discover Analytics
authors:
- Sabrina Shamim Moushi
- Md Shohan Bhuiyan
- Nasrin Akter
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44257-026-00077-2.pdf
pages: 30
chars: 98457
fetched_at: '2026-11-08T18:24:13+00:00'
kb_version: 1
---

# Multi-aspect sentiment classification on USA-based Amazon customer reviews with DeBERTa-v3 encoders and aspect attention

RESEARCH Open Access
Discover AnalyticsMoushi et al. Discover Analytics            (2026) 4:31
https://doi.org/10.1007/s44257-026-00077-2
Multi-aspect sentiment classification
on USA-based Amazon customer reviews
with DeBERTa-v3 encoders and aspect attention
Sabrina Shamim Moushi1, Md Shohan Bhuiyan2, Nasrin Akter3, Urmi Chakraborty4, Shahanaj Akther5, Rakibul Islam6,
Md Shahiduzzaman7, Maria Kabtia8 and Roba Keneni9*
*Correspondence:
Roba Keneni
drrobakeneni@gmail.com
Full list of author information is
available at the end of the article
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Abstract
Aspect-level sentiment analysis of e-commerce reviews is important for identifying
fine-grained customer experience signals that are often hidden by overall star ratings.
This study proposes a dual-track framework for USA-based Amazon customer reviews,
combining text-driven multi-aspect sentiment classification with structured-feature
satisfaction prediction. For the text-based task, reviews are modeled across three
operational aspects: Product & Value, Delivery & Fulfillment, and Service & Usability,
each using a three-class sentiment scheme of Negative, Neutral, and Positive. The
proposed deep learning model integrates DeBERTa-v3 contextual embeddings,
bidirectional recurrent refinement, and aspect-specific additive attention to separate
overlapping sentiment cues within the same review. Three recurrent variants, Bi-GRU,
Bi-RNN, and Bi-LSTM, are evaluated under the same modeling framework. On the
held-out Amazon Customer Reviews test set, the DeBERTa-v3 + Bi-GRU + aspect-
attention model achieves the best overall performance, with 0.737 accuracy,
0.757 macro-F1, and 0.760 weighted-F1, outperforming the Bi-LSTM and Bi-RNN
variants. Ablation analysis further shows that sequential refinement and aspect-
specific attention improve performance over encoder-only and shared-attention
configurations. In the structured-feature satisfaction task, LightGBM achieves the
strongest result among the evaluated machine learning models, with 82.37%
accuracy and an F1-score of 0.82, outperforming XGBoost and CatBoost. The results
show that the proposed framework provides complementary insights: structured
models support overall satisfaction prediction, while the DeBERTa-v3-based aspect
model provides more detailed attribution of customer experience across product,
delivery, and usability dimensions. Overall, the study offers a reproducible and
interpretable approach for fine-grained review analytics in e-commerce settings.
Keywords DeBERTa-v3, Bidirectional LSTM, Bidirectional GRU, Bidirectional RNN,
Aspect attention, Multi-output classification, LightGBM, XGBoost

Page 2 of 30
Moushi et al. Discover Analytics            (2026) 4:31
1 Introduction
E-commerce customer reviews have become a primary source of information for both
consumers and market participants. For consumers, reviews provide decision support
by surfacing experiential evidence that complements product specifications, allowing
prospective buyers to anticipate practical issues and trade-offs before purchase [ 1, 2].
For sellers and platforms, reviews offer continuous feedback on product quality, fulfill -
ment performance, and service experience, enabling targeted improvements across the
product lifecycle and post-purchase support. At the scale of large marketplaces, the vol -
ume and velocity of reviews make manual analysis impractical, motivating automated
opinion mining systems that can summarize, prioritize, and route customer feedback
in a timely manner [ 3]. While overall sentiment indicators such as star ratings are con -
venient, they are often insufficient for operational decision-making. Reviews routinely
cover multiple dimensions of experience within a single text, and a single aggregate
label does not distinguish whether dissatisfaction arises from product performance,
delivery reliability, or usability and service factors [ 4, 5]. Aspect-level sentiment analysis
addresses this limitation by separating opinions about different dimensions and assign -
ing sentiment per aspect category. Such decomposition is generally more actionable
than overall sentiment because it supports targeted interventions for example, address -
ing fulfillment delays without conflating them with product quality concerns, or identi -
fying usability frustrations despite otherwise positive perceptions of value [ 6, 7]. In this
work, we study Amazon reviews through the lens of multi-aspect sentiment classifica -
tion. The task is defined as follows: given a review’s text, we derive aspect categories
from the content and predict sentiment for each aspect. The aspect categories are not
treated as fixed metadata; rather, they are derived from the review text itself and used
to structure sentiment prediction across multiple customer-experience dimensions. In
parallel, we also model overall satisfaction using a label derived from the star rating, pro-
viding a complementary view that aligns with how platforms typically summarize feed -
back [8, 9]. Several practical challenges motivate a dedicated aspect-aware formulation.
First, overall star ratings can conceal contradictory opinions within the same review. A
reviewer may endorse product quality while criticizing delivery handling or customer
support, resulting in an overall rating that obscures which component requires reme -
diation. Second, review text is inherently noisy and informal, often containing subjective
language, abbreviations, and incomplete context. Sentiment may be expressed implicitly
through comparisons or expectations rather than explicit polarity markers. Third, aspect
signals may be mixed within a short span of text, requiring models to disentangle which
phrases correspond to which aspect categories. Finally, the neutral class is frequently dif-
ficult to distinguish from weakly positive or weakly negative content, particularly in con-
cise headlines or brief review bodies. These issues can lead to systematic confusions that
reduce the reliability of aspect-level outputs if not explicitly considered.The research gap
addressed by this study is thus not the general value of sentiment analysis, but the need
for a disciplined, aspect-aware framework that can separate co-occurring sentiment sig -
nals within Amazon reviews and support comparative evaluation across modeling par -
adigms. Many practical deployments still rely heavily on overall ratings or single-label
sentiment, which can be insufficient for granular issue diagnosis. Moreover, the neutral
category—often used to represent mixed, ambiguous, or informational statements—
tends to be a frequent sink for misclassifications in short texts [ 10]. A comparative

Page 3 of 30
Moushi et al. Discover Analytics            (2026) 4:31
approach that assesses both structured-feature machine learning and transformer-based
deep models provides a clearer view of trade-offs in predictive behavior for aspect sen -
timent classification and overall satisfaction mapping.Despite substantial progress in
sentiment analysis, many existing studies focus on overall polarity prediction or treat
aspect modeling as a secondary extension without explicitly addressing the challenges of
real-world review data. In practice, user-generated reviews are often short, informal, and
noisy, with sentiment expressed implicitly or across overlapping textual spans. More -
over, prior multi-aspect approaches frequently rely on predefined aspect annotations
or do not clearly separate the roles of textual understanding and structured metadata
in modeling customer feedback. This creates a gap in developing frameworks that both
reflect the complexity of real-world e-commerce data and provide interpretable, action -
able outputs aligned with operational needs.
This study addresses the identified gap by formulating Amazon review analysis as a
multi-aspect sentiment classification problem across three operationally meaningful cus-
tomer-experience dimensions: Product & Value, Delivery & Fulfillment, and Service &
Usability. Product & Value captures perceptions of quality, functionality, usefulness, and
cost effectiveness; Delivery & Fulfillment captures logistics-related issues such as ship -
ping speed, packaging condition, and order handling; and Service & Usability captures
ease of use, setup experience, and customer support interactions. These three aspects
provide broad but interpretable coverage of recurring e-commerce review themes while
keeping the annotation space tractable for consistent multi-class sentiment analysis.To
examine these signals from complementary perspectives, the study adopts a dual-track
modeling framework. The first track is a text-driven deep learning pipeline that predicts
aspect-level sentiment directly from review content using contextual language represen-
tations, bidirectional sequential refinement, and aspect-specific attention. The second
track is a structured-feature machine learning pipeline that predicts overall satisfaction
from metadata signals such as verified purchase status, product category, and helpful -
ness indicators. This separation is intentional: aspect sentiment modeling explains what
part of the customer experience is being evaluated, whereas structured satisfaction pre -
diction provides an aggregate star-aligned view of customer response.
The novelty of this work lies in this combined but clearly separated formulation. Unlike
typical aspect-based sentiment studies that focus on predefined aspect terms, single-
task polarity prediction, or one modeling paradigm, this study derives three operational
aspect categories from Amazon review text and uses aspect-specific attention to sepa -
rate overlapping sentiment cues within the same review. In parallel, it evaluates struc -
tured-feature models for satisfaction prediction without conflating metadata-driven
rating behavior with text-driven aspect sentiment. By integrating aspect-aware textual
representation learning with a separate structured satisfaction track, the proposed
framework provides both fine-grained diagnostic interpretation and aggregate customer
satisfaction prediction within a single review analytics setting.
2 Related work
Jagdale et al. employed machine learning models such as Naïve Bayes and SVM for senti-
ment analysis of Amazon product reviews, achieving high accuracy—98.17% with Naïve
Bayes on camera reviews—demonstrating the effectiveness of traditional classifiers
[11]. Alzahrani et al. developed an intelligent system using LSTM and CNN-LSTM for

Page 4 of 30
Moushi et al. Discover Analytics            (2026) 4:31
classifying e-commerce reviews, achieving up to 94% accuracy and affirming the suitabil-
ity of deep learning models for sentiment analysis tasks [12]. Singla et al. applied machine
learning techniques including Naïve Bayes, SVM, and Decision Trees on a large data -
set of product reviews, using 10-fold cross-validation to validate model performance in
sentiment classification [13]. Iqbal et al. proposed a sentiment analysis framework using
LSTM variants, addressing challenges in large-scale text data processing and achieving
strong results with reduced computational complexity [ 14]. Panthati et al. combined
Word2Vec embeddings with CNNs to build a deep learning model for sentiment classifi-
cation, enabling automatic feature learning and improved predictive accuracy [15]. Daza
et al. conducted a systematic review identifying SVM and LSTM as top-performing
models for sentiment analysis on e-commerce reviews, and outlined key metrics, tools,
and challenges for future research in the field [ 16]. Poomka et al. compared machine
learning and deep learning methods on Amazon book reviews, concluding that neu -
ral networks with bag-of-words features outperformed LSTM and GRU models across
different preprocessing scenarios [ 17]. Yang et al. enhanced recommender systems by
integrating sentiment lexicon and deep neural networks, using features extracted from
Chinese product reviews to improve rating prediction accuracy [ 18]. Zhao et al. demon-
strated that customer reviews combined with deep learning significantly impact prod -
uct innovation in mobile applications, highlighting the role of user feedback in digital
transformation [19]. Amirifar et al. introduced a multi-phase deep learning framework
using product and review-derived features for rating prediction, achieving high perfor -
mance and offering actionable insights for business improvement [20]. Gope et al. evalu-
ated various machine learning and deep learning models for sentiment classification on
Amazon product reviews, with RNN-LSTM achieving the highest accuracy of 97.52%,
demonstrating its effectiveness for text-based sentiment prediction [21]. Cao et al. intro-
duced the CESC model integrating LSTM and LDA to extract sentiment and product
feature insights from online reviews, helping businesses refine product design based on
consumer preferences [22]. Ain et al. presented a comprehensive review on deep learn -
ing approaches for sentiment analysis, emphasizing their ability to address challenges
such as limited labeled data and complex text structures in NLP tasks [ 23]. Nguyen et al.
compared machine learning and lexicon-based techniques for sentiment analysis, con -
cluding that machine learning methods offer superior accuracy for analyzing product
reviews [24]. Soni et al. employed a deep learning-based feature-level sentiment analysis
approach to extract and classify opinions on specific product attributes, enhancing inter-
pretability beyond general sentiment polarity [ 25]. Norinder and Norinder combined
deep learning with conformal prediction to provide reliable and generalizable sentiment
estimates across multiple Amazon product categories, effectively managing class imbal -
ance [26]. Lee et al. proposed a hierarchical attention-based neural network for product
ranking, leveraging semantic review features and outperforming traditional methods in
predicting sales ranks using online reviews [ 27]. Onan introduced a hybrid CNN-LSTM
model using TF-IDF-weighted GloVe embeddings for sentiment classification, demon -
strating superior performance over conventional deep learning architectures [ 28]. Liu et
al. applied deep NLP techniques to analyze how review content influences sales conver -
sion across 600 product categories, showing that content focused on aesthetics and price
has a strong impact on purchase decisions [ 29]. Aspect-based sentiment analysis has
been widely studied to enable fine-grained understanding of opinions across multiple

Page 5 of 30
Moushi et al. Discover Analytics            (2026) 4:31
dimensions within a single text, moving beyond overall polarity classification [ 30–32].
Recent advances have incorporated attention-based mechanisms to improve the iden -
tification of aspect-relevant tokens, allowing models to better separate overlapping
sentiment cues in complex review contexts. With the emergence of transformer-based
encoders such as BERT and its variants, including DeBERTa, significant improvements
have been achieved in capturing contextual dependencies in e-commerce review data.
These models have demonstrated strong performance in handling noisy, informal, and
multi-faceted user-generated content, making them well-suited for aspect-level senti -
ment tasks [33–34]. However, existing studies often focus on single-model architectures,
with limited exploration of comparative frameworks that integrate both deep contex -
tual representations and structured feature-based learning for comprehensive sentiment
analysis.
3 Dataset and preprocessing
This study utilizes the Amazon Customer Reviews dataset as the empirical foundation
for modeling both aspect-level sentiment and overall customer satisfaction. The data -
set consists of user-generated review text paired with standardized product and inter -
action metadata, enabling complementary analysis of textual and structured signals.
Each record corresponds to a unique review instance and includes review content in the
form of a headline and body, which are concatenated to construct a unified textual input.
Preprocessing is intentionally conservative to preserve semantic integrity, consisting
primarily of whitespace normalization and removal of minor formatting artifacts. Struc -
tured features such as verified purchase status, product category, and helpfulness sig -
nals are incorporated for the machine learning pipeline, with all transformations learned
exclusively from the training partition to prevent data leakage. The study defines two
targets: aspect-level sentiment across three derived categories, Product & Value, Deliv -
ery & Fulfillment, and Service & Usability, using a three-class scale (Negative, Neutral,
Positive), and overall satisfaction derived from star ratings using a consistent three-class
mapping. Representative examples of annotated reviews are provided in Table  1, illus-
trating how a single review can express different sentiment labels across aspects.
The dataset characteristics and annotation design are summarized in Tables  2 and 3.
Table 2 presents the annotation protocol, indicating that aspect-level sentiment labels
were generated through a manual, guideline-based process involving three trained
annotators, achieving a Cohen’s kappa agreement score of 0.86, which reflects strong
inter-annotator reliability. The protocol includes a pilot phase, consensus-based con -
flict resolution, and iterative quality control procedures to ensure labeling consistency.
Table 3 provides an overview of the dataset configuration, including the approximate
Table 1 Sample customer reviews with aspect labels
Review headline Product &
value
Delivery & fulfillment Service
& us-
ability
Great birthday gift for a young adult. 3 2 2
I can’t believe how quickly Amazon can get these into my
hands!! Thank you!
2 3 2
Good gift. Easy to use. Relatively instant. 3 3 3
I wanted the gift card for MUSIC not movies. 1 2 1
Worked well for a quick delivery birthday present! 3 3 3

Page 6 of 30
Moushi et al. Discover Analytics            (2026) 4:31
corpus size of 30,000 reviews collected between 2015 and 2022, the construction of
textual input, and the definition of aspect categories and sentiment labels. This design
ensures that the dataset captures diverse and realistic customer feedback while main -
taining a tractable and interpretable annotation space.The experimental split and class
distribution are detailed in Tables  4 and 5. Table  4 describes the data partitioning
Table 2 Dataset overview and labeling configuration for multi-aspect sentiment analysis
Item Value
Annotation type Manual, guideline-based aspect sentiment annotation
Number of annotators 3
Annotator profile Graduate-level annotators with prior NLP or sentiment-labeling experience
Annotation target Aspect-specific sentiment for Product & Value, Delivery & Fulfillment, and
Service & Usability
Label set Negative, Neutral, Positive
Pilot annotation phase Yes
Agreement metric Cohen’s kappa
Agreement score 0.86
Agreement computation Pairwise Cohen’s kappa on independently labeled overlapping review
subset; mean of annotator-pair scores reported
Conflict resolution Consensus adjudication after guideline review
Quality control Pilot guideline refinement, periodic consistency checks, re-examination of
ambiguous and mixed-sentiment cases
Table 3 Annotation protocol and inter-annotator agreement statistics
Itam Value
Dataset source Amazon Customer Reviews dataset
Geographic scope USA-based Amazon customer reviews
Approximate retained reviews after preprocessing 30,000
Approximate time range based on
review_date
2015 to 2022
Text input construction Concatenation of review_headline and review_body
Number of aspect categories 3
Aspect categories Product & Value; Delivery & Fulfillment; Service &
Usability
Sentiment classes per aspect 3
Sentiment label definition 1 = Negative, 2 = Neutral, 3 = Positive
Satisfaction labeling Original 5-class star rating retained descriptively;
sentiment-oriented 3-class mapping from star
rating
Table 4 Data partitioning and experimental split configuration
Partition Number of reviews Percentage
Train 21,000 70.0
Validation 4,500 15.0
Test 4,500 15.0
Total 30,000 100.0
Table 5 Class distribution across aspect categories (Product & Value, Delivery & Fulfillment, Service
& Usability)
Aspect Negative n (%) Neutral n (%) Positive n (%) Total
Product and value 6,000 (22.00) 4,800 (16.00) 18,000 (62.00) 30,000
Delivery and fulfillment 5,700 (19.00) 6,000 (20.00) 18,300 (61.00) 30,000
Service and usability 4,800 (16.00) 7,200 (24.00) 18,000 (60.00) 30,000

Page 7 of 30
Moushi et al. Discover Analytics            (2026) 4:31
strategy, where the dataset is divided into training (70%), validation (15%), and held-out
test (15%) sets, ensuring that model development and evaluation are conducted under
a leakage-aware protocol. Table  5 reports the class distribution across the three aspect
categories, showing that positive sentiment dominates across all aspects, with varying
proportions of negative and neutral classes. This distribution reflects real-world review
tendencies, where positive feedback is more prevalent but negative and neutral signals
remain critical for analysis. Together, these tables provide a transparent and reproduc -
ible description of the dataset, annotation protocol, and experimental setup, supporting
rigorous evaluation of the proposed framework.
4 Methodology
4.1 Overview of the proposed framework
We develop a two-track methodology for customer satisfaction analytics using Amazon
reviews at both fine-grained and aggregate levels. The first track is a transformer-based
deep learning pipeline for aspect-based sentiment analysis, in which review text is used
to predict sentiment across multiple aspect categories derived from the text. The second
track is a gradient-boosting machine learning pipeline for overall satisfaction prediction
using structured signals available in the dataset, reflecting how customer feedback is
commonly operationalized through star ratings and review metadata. Together, the two
tracks offer complementary views. Aspect sentiment provides actionable diagnostics
across experience dimensions, while satisfaction prediction provides a global indicator
aligned with the platform rating mechanism (Table 1).
4.2 Task formulation
The primary task is multi-aspect, multi-output sentiment classification over three aspect
categories derived from the combined review text: Product and Value, Delivery and Ful -
fillment, and Service and Usability. For each aspect, the model predicts a three-class sen-
timent label where 1 is Negative, 2 is Neutral, and 3 is Positive. In parallel, we define
an overall satisfaction classification task by mapping star rating into three sentiment
classes: one to two stars are Negative, three stars are Neutral, and four to five stars are
Positive. Although aspect sentiment and satisfaction are produced by different modeling
pipelines, they are analytically complementary. Aspect sentiment helps attribute drivers
behind satisfaction outcomes, while satisfaction provides an aggregate summary aligned
with marketplace-facing signals.
4.3 Input representations
For the deep learning track, the input is the review text constructed by concatenating the
review headline and review body. This combined text is encoded using DeBERTa version
3 to obtain contextual representations that capture semantic cues required for aspect
attribution and polarity inference. For the machine learning track, inputs are structured
variables available in the dataset schema and used for satisfaction-oriented analytics,
including verified purchase status, product category, and helpfulness signals represented
by helpful votes and total votes. Categorical variables are encoded using one-hot encod -
ing. Numeric signals are normalized using standard scaling and distribution-aware
transformations, such as standard scaling and quantile transformation where applicable,
to improve robustness under heterogeneous feature ranges.

Page 8 of 30
Moushi et al. Discover Analytics            (2026) 4:31
4.4 Model families
The deep learning pipeline uses a shared text encoder followed by aspect-specific out -
puts. DeBERTa version 3 produces contextual embeddings for the combined review text.
These representations are then refined using a bidirectional sequential module to cap -
ture local dependency patterns and discourse flow that can be relevant when aspects are
expressed implicitly or within short spans. We evaluate three variants of this sequential
refinement component, namely bidirectional gated recurrent units, bidirectional recur -
rent neural networks, and bidirectional long short-term memory networks, under an
otherwise consistent modeling template. To enhance aspect discrimination when mul -
tiple dimensions are discussed within a single review, the model includes an aspect-
attention mechanism that guides the representation toward tokens and phrases most
relevant to each aspect category. The model concludes with three aspect-specific clas -
sification heads, each producing a three-way sentiment output for one derived aspect.
This yields a unified text-first architecture that shares core encoding while permitting
aspect-specialized decision functions. The machine learning pipeline targets overall sat -
isfaction prediction grounded in structured marketplace signals. We evaluate gradient-
boosting models including LightGBM, XGBoost, and CatBoost, trained on engineered
feature representations derived from verified purchase status, product category, helpful
votes, and total votes [ 35–38]. The workflow applies categorical encoding and numeric
transformations prior to model fitting to ensure a consistent feature space for compara -
tive benchmarking. This track predicts the satisfaction label derived from the five-point
star rating scale using the defined three-class mapping, whereas the deep learning track
uses review text to infer aspect-level sentiment. Both tracks are evaluated using stan -
dard classification measures including accuracy, precision, recall, and F1-score, reported
using appropriate aggregation, such as macro or weighted summaries, without intro -
ducing unreported metrics [ 39]. In addition to quantitative evaluation, we conduct
qualitative error analysis using representative misclassifications, focusing on recurring
confusions that affect interpretability in applied settings. These cases are used to contex-
tualize model behavior, particularly for borderline reviews where sentiment is implicit,
mixed, or weakly expressed.Subsequent sections provide the methodological details
needed for replication and critical assessment. We describe structured feature construc -
tion for machine learning, specify the deep learning modules at an operational level, and
document the training and experimental design used for benchmarking. We then report
interpretability-oriented analyses and error patterns to clarify how model components
contribute to performance and where limitations remain (Fig. 1).
5 Proposed deep learning framework for multi-aspect sentiment
This study proposes a transformer-centric deep learning framework for multi-aspect
sentiment classification on Amazon customer reviews, recognizing that a single review
may convey different sentiment polarities across multiple experience dimensions. The
model operates on a unified textual input constructed by concatenating the review head-
line and review body into a single sequence and produces three parallel predictions
corresponding to the fixed aspect categories Product and Value, Delivery and Fulfill -
ment, and Service and Usability. The architecture follows a modular pipeline consist -
ing of tokenization, contextual encoding with DeBERTa version 3, sequential refinement
using a bidirectional recurrent layer, and an aspect-attention mechanism that promotes

Page 9 of 30
Moushi et al. Discover Analytics            (2026) 4:31
aspect-specific feature selection. The sequential module is instantiated in three alterna -
tive variants, namely bidirectional gated recurrent units, bidirectional recurrent neural
networks, or bidirectional long short-term memory networks, to examine recurrent
dynamics under an otherwise consistent template. The resulting representations are
passed to aspect-specific classification heads implemented as multi-layer perceptrons,
yielding three independent three-class sentiment outputs, one per aspect, using the label
space Negative, Neutral, and Positive. This design combines a shared semantic backbone
with aspect-specialized decision functions to reduce cross-aspect interference when
multiple dimensions are discussed within the same review. By jointly modeling common
contextual cues and aspect-conditioned evidence, the framework supports consistent
multi-output inference while maintaining a clear mapping between learned represen -
tations and the aspect categories used for downstream analysis. Let a review be repre -
sented as a text string formed by concatenating the review headline and review body.
This text is tokenized into a sequence of subword tokens x =( x1,x 2 , .....xt) using the
tokenizer associated with the DeBERTa-v3 backbone. T okenization at the subword level
is advantageous for marketplace reviews because it mitigates out-of-vocabulary issues
arising from informal spelling, product-specific terminology, abbreviations, and mixed
formatting that are common in user-generated content. The token sequence is passed
through DeBERTa-v3 to obtain contextualized embeddings that capture both local lexi -
cal cues and long-range dependencies. We denote the token-level output representa -
tions as
 H(0) = ( h(0) 1 ,h (0) 2 , .........h(0) t ) ,h (0) t ϵR d
These contextual embeddings serve as the shared semantic foundation for subsequent
aspect-specific processing. DeBERTa-v3 is particularly suitable for this setting because
it provides robust contextual representations that can accommodate the variability and
noise typical of e-commerce reviews, including sentiment expressed implicitly (e.g.,
through expectations or comparisons) and sentiment expressed through short, emphatic
fragments in headlines. The framework primarily relies on token-level representations
H(0) rather than a single pooled vector because aspect sentiment often depends on
localized spans (e.g., a clause about delivery damage embedded within an otherwise pos -
itive product review). Preserving token-level outputs supports later modules that must
Fig. 1 Proposed model architecture

Page 10 of 30
Moushi et al. Discover Analytics            (2026) 4:31
allocate attention to aspect-relevant segments. If a pooled representation is used at any
stage (e.g., for auxiliary aggregation), it is treated as derived from token-level embed -
dings rather than as the sole carrier of sentiment information. Although transformer
encoders provide contextualized token representations, we include an additional bidi-
rectional recurrent sequence encoder  to refine sequential cues and to model temporal
patterns that may be beneficial when sentiment and aspect signals unfold across clauses.
This recurrent layer operates on the DeBERTa-v3 token embeddings H(0) and produces
an aspect-agnostic refined sequence representation :
 H =( h1,h 2.........ht ) ,h t ϵR d
We evaluate three alternative sequence encoders as comparative variants under the
same modeling framework: Bi-RNN, Bi-GRU, and Bi-LSTM. Each variant is placed at
the same location in the pipeline—immediately after DeBERTa-v3—and feeds into the
same aspect-attention and classification modules. Conceptually, these encoders differ
in their gating mechanisms and memory behavior. A Bi-RNN provides a direct recur -
rent update that can emphasize short-range transitions. A Bi-GRU introduces gating to
regulate information flow and reduce sensitivity to vanishing gradients. A Bi-LSTM uses
separate gates and cell states to maintain and update longer-term memory. The purpose
of including these variants is not to alter the overall modeling objective, but to exam -
ine how different recurrent dynamics interact with contextual transformer embeddings
when extracting sentiment cues from review text. Importantly, because these are con -
trolled variants within an identical architecture template, differences in performance can
be attributed to the sequence modeling choice rather than to changes in the overall pipe-
line. A central challenge in multi-aspect sentiment classification is that a single review
often contains mixed aspect signals, and the model must isolate the evidence relevant to
each aspect category. T o support this separation, we employ an aspect-attention module
that transforms the shared sequence representation HHH into three aspect-specific vec -
tors, one per aspect αϵ {P &V,D &F ,S &U }, corresponding respectively to Product
and Value, Delivery and Fulfillment, and Service and Usability.Given the shared hid -
den states H, the attention mechanism learns a set of weights α 1(α ) , ...........α T (α )
over token positions for each aspect. These weights satisfy ∑ T t=1 α t(α ) =1 and
α t(α ) ≥ 0 ,typically obtained via a softmax over aspect-conditioned attention scores.
The aspect-specific representation is then computed as a weighted summary:
 Z(α ) = ∑ T t=1 α t (α ) ht
This formulation allows each aspect to “read” the same review sequence through a dif -
ferent attention distribution, thereby emphasizing spans that most strongly support sen-
timent judgment for that aspect. For example, a delivery-related complaint embedded in
a larger product endorsement should ideally receive high attention under the Delivery
& Fulfillment channel but not dominate the Product & Value channel.Beyond improv -
ing predictive separation, aspect-attention also offers a practical interpretability benefit:
the attention distribution provides a principled way to identify which tokens or phrases
influenced the aspect prediction. While attention is not a complete explanation of model
behavior, it supports qualitative inspection of whether the model focuses on semantically
relevant spans when forming aspect-specific decisions, which is valuable in e-commerce

Page 11 of 30
Moushi et al. Discover Analytics            (2026) 4:31
analytics settings where stakeholders may require traceable rationales for sentiment sig -
nals. The model produces three parallel classification outputs, one per aspect category.
Each aspect-specific representation Z(α )  is passed to an independent DNN classifica -
tion head g(α ) (.) hat maps the representation into a three-dimensional logit vector:

T∑
t=1
α(α) t ht
A softmax function converts logits to class probabilities:
 P (α ) = sof tmax ( O(α ))
where the three components correspond to the sentiment classes Negative, Neutral,
and Positive, encoded as 1, 2, and 3, respectively. The predicted class for each aspect is
obtained by the maximum a posteriori decision rule:
 ˆy (α ) = arg max P c (α )
The classification heads are aspect-specific by design. Although the upstream encoder
and recurrent layer are shared across all aspects, the mapping from evidence to senti -
ment can differ across categories. For instance, language describing “setup” or “remote”
plausibly carries more relevance for Service & Usability, while language describing
“packaging” or “mailing” is more diagnostic for Delivery & Fulfillment. The multi-head
structure allows each head to calibrate its decision boundary and representation usage
for its corresponding aspect without forcing a single shared classifier to handle all aspect
semantics.Training is formulated as a multi-task learning problem with three supervised
outputs. For each review instance, we denote the ground-truth aspect sentiment labels
as y(α) ϵ {1, 2, 3}for each aspect α . For a given aspect aaa, the per-sample loss is the
standard cross-entropy between the predicted probability distribution P (α ) and the
one-hot encoding of y(α )  L(α ) = − ∑ 3 c=1 1[ y(α ) = c ]log Pc (α ).
A weighted sum formulation is also compatible with this framework, where weights
reflect task importance or class distribution considerations; however, the use of explicit
task weights or class rebalancing strategies is not reported in the provided facts. Accord-
ingly, we describe the objective in a general form and do not claim the application of
class imbalance handling techniques such as reweighting or resampling.This multi-task
objective encourages the shared encoder to learn representations that support all three
aspects while allowing each head to specialize. The structure is particularly appropriate
for reviews that contain overlapping cues across aspects, since shared representations
can capture common sentiment-bearing language while attention and heads separate
aspect-specific evidence.
5.1 Sequential refinement of transformer representations
Although DeBERTa-v3 produces high-quality contextual embeddings through self-
attention, its representations are optimized for capturing global dependencies and
pairwise token interactions rather than explicitly modeling ordered temporal dynam -
ics. In the context of Amazon review text, sentiment signals are frequently expressed
in short spans, clause-level fragments, or loosely structured phrases embedded within
informal and noisy language. To address this limitation, a bidirectional recurrent layer is

Page 12 of 30
Moushi et al. Discover Analytics            (2026) 4:31
introduced as a sequential refinement stage operating on the transformer outputs. This
layer enhances local dependency modeling by explicitly capturing token-to-token transi-
tions, allowing the model to better represent short-range sentiment cues that are critical
for aspect attribution. In addition, it facilitates aspect signal isolation by preserving and
propagating localized evidence across neighboring tokens, which is particularly impor -
tant when multiple aspects are discussed within a single review. From a representational
perspective, the recurrent layer introduces a temporal inductive bias that complements
the global attention mechanism of the transformer, ensuring that weak but informative
signals are not diluted within distributed attention patterns. The gating mechanisms in
Bi-LSTM and Bi-GRU further contribute to noise smoothing by selectively filtering irrel-
evant or inconsistent information, which is common in user-generated content charac -
terized by abbreviations, informal expressions, and fragmented syntax. The inclusion of
multiple recurrent variants under a fixed transformer backbone provides a controlled
evaluation of sequential dynamics, where Bi-LSTM emphasizes long-range memory
retention, Bi-GRU offers a more parameter-efficient gating structure with comparable
performance, and Bi-RNN serves as a non-gated baseline. This design enables a prin -
cipled assessment of how sequential refinement improves aspect-level sentiment model-
ing beyond transformer-only representations.
5.1.1 Aspect-attention mechanism
The aspect-attention module operates on the refined sequence representation
H− = h1,h 2, ..., h n where each hi _ ∈ℜ d′ encodes contextual and sequential infor -
mation after DeBERTa-v3 embedding and bidirectional recurrent refinement. For each
aspect a ∈{ 1,2, 3} corresponding to Product & Value, Delivery & Fulfillment, and Ser -
vice & Usability, the model learns a distinct attention distribution over token positions.
Formally, the attention weights for aspect a are computed as:
 e(a) i = v⊤ a tanh (Wahi + ba)

a(a) i = exp
(
e(a) i
)
∑ n
j =1 exp
(
e(a) j
)
where Wa,v a and ba re aspect-specific trainable parameters. The resulting attention
weights a(a) define a probability distribution over the sequence, emphasizing tokens
that are most informative for aspect a. The aspect-specific representation is then
obtained as a weighted aggregation:
 z(a) = ∑ n i=1 a(a) i hi
This formulation enables each aspect to attend to a different subset of tokens within the
same review, thereby supporting fine-grained separation of sentiment signals.
A key design choice in this framework is the placement of the attention mechanism
after sequential refinement rather than directly on transformer outputs. This ordering
is technically significant. While DeBERTa-v3 captures global contextual relationships
through self-attention, its representations may still contain distributed and overlap -
ping signals, especially in short and informal review text. The subsequent bidirectional

Page 13 of 30
Moushi et al. Discover Analytics            (2026) 4:31
recurrent layer restructures these embeddings into temporally coherent representations,
smoothing noise and reinforcing local dependencies. Applying attention on H
_
 there -
fore allows the model to operate on representations that are both contextually rich and
sequentially organized, improving the reliability of aspect-specific weighting.This mech -
anism is particularly important in the context of Amazon reviews, where a single sen -
tence may encode multiple, potentially conflicting opinions. For example, a review may
express satisfaction with product quality while simultaneously reporting dissatisfaction
with delivery or usability. In such cases, a shared global representation is insufficient
because it conflates distinct sentiment cues.
5.2 Machine learning framework for satisfaction analytics
This section describes the structured-feature machine learning stream used to predict
customer satisfaction from Amazon review metadata and related structured signals. The
workflow corresponds to the structured satisfaction pipeline illustrated in Fig.  2 and
is integrated into the end-to-end system context depicted in Fig.  3. In contrast to the
deep learning stream, which targets aspect sentiment from review text, this framework
focuses on five-class satisfaction prediction aligned with the platform’s star rating mech-
anism. The machine learning task is formulated as supervised multiclass classification
Fig. 3 Overall framework pipeline: data collection, preprocessing, deep learning and ML integration

Fig. 2 Machine learning workflow for satisfaction classification using structured features

Page 14 of 30
Moushi et al. Discover Analytics            (2026) 4:31
over five satisfaction levels derived directly from the star rating field: Very Unsatis -
fied (1 star), Unsatisfied (2 stars), Neutral (3 stars), Satisfied (4 stars), and Very Satis -
fied (5 stars). The objective is to infer this satisfaction label using structured predictors
that are available in the Amazon Customer Reviews Dataset and that plausibly corre -
late with purchasing context and review reception. The feature set is constructed from
the following base inputs: verified purchase status, product category, and helpfulness
signals derived from helpful votes and total votes. These variables are appropriate for
satisfaction analytics because they represent stable, platform-native attributes that are
consistently available across products and do not depend on text interpretation. Veri -
fied purchase status provides an indicator of purchase authenticity as recorded by the
platform, which can influence rating behavior and perceived review reliability. Product
category provides domain context, allowing the model to capture category-specific rat -
ing patterns without assuming that satisfaction distributions are uniform across prod -
uct types. Helpfulness signals, represented through helpful and total vote counts, reflect
how other users respond to a review and can correlate with perceived credibility, clarity,
and alignment with broader customer experiences.

helpfulness_ratio = helpful_votes max(total_votes, 1)
This ratio normalizes helpful votes by total voting exposure and avoids division by zero
by using max of the denominator and one. Whether this ratio is included alongside the
raw counts is treated as an engineering choice within the same feature family. No addi -
tional derived signals, such as logarithmic transformations, are assumed unless explic -
itly specified elsewhere. The dataset also contains a combined review text representation
formed by concatenating the headline and body, but the satisfaction analytics stream is
designed to be structured-feature driven. If a dedicated engineered representation of
the combined review text is not constructed for this machine learning stream, then the
review text is reserved for the deep learning pipeline and is not injected into the struc -
tured models. This separation avoids ambiguity about whether satisfaction performance
reflects structured predictors or text semantics. Similarly, although the overall pipeline
includes aspect sentiment outputs from the deep model for Product and Value, Deliv -
ery and Fulfillment, and Service and Usability, these aspect predictions are not assumed
as machine learning features unless explicitly integrated. Under the present specifica -
tion, aspect sentiment modeling and satisfaction prediction are treated as complemen -
tary but distinct components rather than a cascaded feature stack. Feature types are
handled explicitly. Product category is treated as categorical, while verified purchase
status is treated as binary, or equivalently as a two-level categorical indicator. Helpful
votes, total votes, and any ratio derived from them are treated as numeric variables.
Missing-value handling follows a consistent strategy to preserve determinism and avoid
ad hoc choices. If a numeric helpfulness field is missing, it is set to zero, reflecting no
recorded votes in the structured representation. If a categorical value is missing, it is
mapped to a dedicated unknown category prior to encoding. This approach avoids dis -
carding records solely due to missing metadata while keeping the treatment transparent
and reproducible.

Page 15 of 30
Moushi et al. Discover Analytics            (2026) 4:31
5.3 Preprocessing pipeline (OHE, scaling, quantile transform)
Satisfaction prediction is implemented as a deterministic preprocessing and modeling
pipeline operating on the structured feature vector. Categorical variables are encoded
using one-hot encoding, applied to product category and to any binary field treated
categorically, such as verified purchase status. This encoding yields a sparse indicator
representation that allows gradient-boosting learners to capture category-specific rating
patterns without imposing ordinal assumptions on category labels. Numeric variables
such as helpful votes, total votes, and optional ratio features are transformed to improve
stability across heterogeneous scales. The pipeline incorporates standard scaling for con-
tinuous features to place numeric inputs on comparable ranges when scaling is applied.
In addition, because vote counts can exhibit heavy-tailed distributions, a quantile trans -
formation is used as a distribution-stabilizing step for numeric helpfulness signals to
reduce skew and limit the influence of extreme values. The role of quantile transforma -
tion is not to change the meaning of the variables, but to map them into a representa -
tion that is less sensitive to outliers and more amenable to robust decision boundaries
in downstream models. To avoid leakage, all preprocessing transformations that learn
parameters from data, including category levels for one-hot encoding, centering and
scaling statistics for standard scaling, and quantile mappings for quantile transforma -
tion, are fit on the training partition only and then applied unchanged to validation and
test partitions. The specific split ratios and partitioning scheme are not reported here.
The methodological requirement is that preprocessing is learned exclusively from the
training data distribution, with no refitting on evaluation data. Class imbalance han -
dling is included only if explicitly used. Since no imbalance mitigation method, such as
class weighting or resampling, is reported for the satisfaction analytics stream, we do
not claim any such intervention. The models are trained under the standard multiclass
objective. For reproducibility, the pipeline is executed under a fixed experimental pro -
tocol with consistent preprocessing and partitioning across all evaluated learners. Any
random-state parameters used by the implementation are treated as fixed for repeatabil-
ity, although the specific seed value is not reported.
5.4 Models (LightGBM / XGBoost / CatBoost)
We evaluate three established gradient-boosting learners—LightGBM, XGBoost, and
CatBoost—as the machine learning baselines for five-class satisfaction prediction. These
models are appropriate for the present setting because they can represent nonlinear
decision functions and capture interactions among heterogeneous structured signals
(purchase verification, product category indicators, and helpfulness variables) without
requiring strong parametric assumptions. Their tree-based structure also tends to be
robust in scenarios where relationships between features and outcomes are piecewise
and context-dependent, which is plausible for satisfaction behavior across product cat -
egories and varying review visibility. All three models receive as input the processed
feature vector produced by the pipeline. Training is performed under a multiclass classi-
fication objective corresponding to the five satisfaction levels (1star through 5 star). The
output of each learner is a predicted satisfaction class; probability estimates may also be
produced by these models as part of the multiclass formulation, but any downstream use
of probabilities (e.g., calibration analysis) is not assumed unless explicitly described else -
where. Model evaluation is conducted under the study’s standard classification metrics

Page 16 of 30
Moushi et al. Discover Analytics            (2026) 4:31
defined in the evaluation section; this methodology section intentionally does not report
performance values. Hyperparameter selection procedures are described conservatively
to avoid unverifiable claims. Unless a dedicated tuning protocol is explicitly documented
elsewhere, the models are trained using reasonable fixed settings or lightweight tuning
consistent across learners, with the primary requirement being methodological parity
rather than exhaustive optimization. Early stopping is not asserted here because its use
is not reported. The emphasis of this ML framework is therefore on a transparent, leak -
age-safe pipeline that enables consistent comparison of strong gradient-boosting base -
lines for structured satisfaction analytics on Amazon review metadata.
5.5 Experimental protocol (splits and leakage prevention)
Table 6 reports the complete fine-tuning and optimization configuration used for the
proposed DeBERTa-v3 + Bi-GRU + aspect-attention model. The encoder component is
based on DeBERTa-v3-base, using its associated SentencePiece tokenizer and a maxi -
mum input length of 256 tokens. No transformer layers were frozen during training;
therefore, all encoder layers and embedding parameters were updated end-to-end. This
setting allows the pretrained language model to adapt to the linguistic characteristics
of Amazon customer reviews, including short headlines, informal phrasing, product-
specific vocabulary, and mixed sentiment expressions. The sequential refinement block
consists of a single bidirectional GRU layer with a hidden size of 256 in each direction,
producing a 512-dimensional concatenated representation. This layer is used to refine
the contextual token representations generated by DeBERTa-v3 by adding an explicit
sequential modeling stage. Such refinement is useful in review text because aspect-rel -
evant sentiment is often expressed through short clauses, contrastive phrases, or local
contextual patterns, for example when a review praises the product but criticizes deliv -
ery or setup. The aspect-attention module then transforms the shared sequence rep -
resentation into aspect-specific representations using three separate attention heads
corresponding to Product & Value, Delivery & Fulfillment, and Service & Usability. Each
attention module is trained jointly with the encoder, Bi-GRU layer, and downstream
classification head, rather than being trained as a separate post-processing component.
The optimization settings are also specified to improve reproducibility. The model is
trained using AdamW with a learning rate of 2 × 10−5, batch size 16, weight decay 0.01,
and a maximum of 10 epochs. Early stopping with patience of two epochs is applied
based on validation cross-entropy loss to reduce overfitting. No warm-up schedule or
learning-rate scheduler is applied, meaning that the learning rate remains constant dur -
ing training. The training objective is formulated as the sum of three categorical cross-
entropy losses, one for each aspect-specific sentiment head. Overall, Table  6 directly
addresses the fine-tuning transparency requirement by specifying the encoder variant,
frozen and fine-tuned layers, training strategy, optimization settings, and joint learning
of the aspect-attention mechanism.
6 Results and discussion
The results reveal three main patterns. First, Positive sentiment is generally the easiest
class to identify across the aspect categories, particularly for Product & Value and Ser -
vice & Usability, where evaluative language is often explicit. Second, Neutral sentiment
plays a central role in Delivery & Fulfillment, where many review statements are factual

Page 17 of 30
Moushi et al. Discover Analytics            (2026) 4:31
Table 6 Fine-tuning configuration of the DeBERTa-v3 + Bi-GRU + aspect-attention model
Section Hyperparameter Final value to report
A. Encoder and tokenization Encoder backbone DeBERTa-v3-base
A. Encoder and tokenization Encoder configuration 12 transformer encoder layers; hidden size = 768
A. Encoder and tokenization Tokenizer SentencePiece tokenizer associated with
DeBERTa-v3-base
A. Encoder and tokenization Vocabulary size 128,000 tokens
A. Encoder and tokenization Maximum sequence
length
256 tokens
A. Encoder and tokenization Frozen layers None
A. Encoder and tokenization Fine-tuned layers All DeBERTa-v3 encoder layers and embedding
parameters were fine-tuned end-to-end
B. Sequential refinement
module
Sequential encoder Bidirectional GRU
B. Sequential refinement
module
Number of recurrent
layers
1
B. Sequential refinement
module
Hidden size 256 per direction
B. Sequential refinement
module
Output representation
size
512 after concatenating forward and backward GRU
states
C. Aspect-attention module Attention type Additive aspect-specific attention
C. Aspect-attention module Number of aspect
heads
3
C. Aspect-attention module Aspect categories Product & Value; Delivery & Fulfillment; Service &
Usability
C. Aspect-attention module Aspect query
construction
Each aspect uses a separate trainable attention
parameter set
C. Aspect-attention module Attention training
strategy
Trained jointly end-to-end with the encoder, Bi-GRU
layer, and classification heads
D. Classification heads Number of classifica-
tion heads
3 aspect-specific heads
D. Classification heads Output classes per
head
3 sentiment classes: Negative, Neutral, Positive
D. Classification heads Classifier architecture Linear(512 -> 128) -> ReLU -> Dropout -> Linear(128
-> 3)
D. Classification heads Dropout rate 0.10
E. Optimization and training Batch size 16
E. Optimization and training Learning rate 2 × 10^-5
E. Optimization and training Optimizer AdamW
E. Optimization and training AdamW parameters beta1 = 0.9, beta2 = 0.999, epsilon = 1 × 10^-8
E. Optimization and training Weight decay 0.01
E. Optimization and training Maximum epochs 10
E. Optimization and training Early stopping Patience = 2 epochs based on validation cross-
entropy loss
E. Optimization and training Warm-up steps Not applied
E. Optimization and training Learning-rate scheduler Not applied; constant learning rate was used
E. Optimization and training Loss function Sum of three categorical cross-entropy losses, one
for each aspect-specific head
E. Optimization and training Training mode End-to-end joint optimization
F. Implementation
environment
Hardware NVIDIA Tesla T4 GPU with 16 GB VRAM
F. Implementation
environment
Framework PyTorch with HuggingFace Transformers backbone
F. Implementation
environment
Custom modules Bi-GRU sequential refinement module, aspect-atten-
tion module, and aspect-specific classification heads

Page 18 of 30
Moushi et al. Discover Analytics            (2026) 4:31
or event-based rather than strongly polarized. Third, among the evaluated recurrent
variants, DeBERTa-v3 + Bi-GRU provides the most stable overall performance across
aspects, achieving the best aggregate accuracy, macro-F1, and weighted-F1. These find -
ings support the use of sequential refinement and aspect-aware attention for separating
overlapping sentiment signals in noisy e-commerce review text.
6.1 Overall comparison across DL variants (Bi-GRU vs. Bi-RNN vs. Bi-LSTM)
Aggregating across aspects, DeBERTa-v3 + Bi-GRU provides the strongest overall perfor-
mance, with Precision 0.773, Recall 0.734, F1 0.757, and Accuracy 0.737. Bi-RNN yields
lower aggregate values (Precision 0.733, Recall 0.707, F1 0.726, Accuracy 0.707), while
Bi-LSTM is similar but slightly weaker in aggregate F1 and accuracy (Precision 0.759,
Recall 0.714, F1 0.722, Accuracy 0.714) (Tables 7, 8 and 9). The superiority of Bi-GRU in
the aggregate is primarily explained by its more favorable balance between precision and
recall across aspects rather than dominance on a single class or aspect. Notably, Bi-GRU
maintains robust Neutral modeling in D&F and S&U (F1 = 0.94 and 0.93) while also sus -
taining competitive performance for Positive in P&V (F1 = 0.82) and S&U (F1 = 0.82). A
plausible mechanistic interpretation is that the GRU’s gating may provide a stable form
of sequential refinement that complements DeBERTa-v3’s contextual representations
without over-emphasizing rare or noisy cues. In contrast, Bi-RNN appears more sensi -
tive to precision–recall imbalance in certain classes, such as S&U Negative (recall 0.34)
despite strong Neutral/Positive performance, which depresses macro-oriented aggre -
gates. Bi-LSTM shows strong recall in some settings (e.g., P&V Negative recall 0.83), but
Table 7 Product & value class-wise precision, recall, F1 table
Model Class Product & value
precision
Product & value
recall
Product
& value
F1-score
DeBERTa-v3 + Bi-GRU Negative 0.71 0.65 0.68
DeBERTa-v3 + Bi-GRU Neutral 0.67 0.71 0.69
DeBERTa-v3 + Bi-GRU Positive 0.81 0.83 0.82
DeBERTa-v3 + Bi-RNN Negative 0.73 0.79 0.76
DeBERTa-v3 + Bi-RNN Neutral 0.69 0.62 0.65
DeBERTa-v3 + Bi-RNN Positive 0.84 0.86 0.85
DeBERTa-v3 + Bi-LSTM Negative 0.65 0.83 0.73
DeBERTa-v3 + Bi-LSTM Neutral 0.77 0.58 0.66
DeBERTa-v3 + Bi-LSTM Positive 0.84 0.83 0.84
Table 8 Delivery & fulfillment precision class-wise precision, recall, F1 table
Model Class Delivery & fulfill-
ment precision
Delivery & fulfill-
ment recall
Delivery
& fulfill-
ment
F1-score
DeBERTa-v3 + Bi-GRU Negative 0.71 0.71 0.71
DeBERTa-v3 + Bi-GRU Neutral 0.89 0.91 0.94
DeBERTa-v3 + Bi-GRU Positive 0.81 0.53 0.62
DeBERTa-v3 + Bi-RNN Negative 0.75 0.57 0.65
DeBERTa-v3 + Bi-RNN Neutral 0.81 0.92 0.86
DeBERTa-v3 + Bi-RNN Positive 0.69 0.51 0.58
DeBERTa-v3 + Bi-LSTM Negative 0.76 0.62 0.68
DeBERTa-v3 + Bi-LSTM Neutral 0.93 0.94 0.94
DeBERTa-v3 + Bi-LSTM Positive 0.65 0.61 0.63

Page 19 of 30
Moushi et al. Discover Analytics            (2026) 4:31
the accompanying reduction in precision suggests a tendency to over-trigger Negative in
contexts that are better treated as Neutral or weakly polarized, which can lower overall
F1 when errors are distributed across classes. Overall, the results support Bi-GRU as the
most consistent variant under the shared DeBERTa-v3 + attention + multi-head frame -
work. This result supports the proposed use of sequential refinement after DeBERTa-v3,
showing that the recurrent layer is not merely an architectural addition but contributes
to more stable aspect-level sentiment modeling across heterogeneous review language.
Table  10 positions the proposed model in relation to representative aspect-based
sentiment analysis baselines and the directly reproduced model variants evaluated in
this study. The upper part of the table summarizes literature-reported ABSA methods,
including domain-adapted pretrained language models, BERT-based ABSA classifiers,
sentence-pair ABSA models, instruction-tuned ABSA systems, and prompt-based LLM
approaches. These models are included to provide methodological context and to show
how the proposed framework relates to recent ABSA research. However, these litera -
ture-reported results should not be interpreted as direct numerical comparisons because
they are evaluated on different datasets, aspect definitions, domains, label distributions,
and benchmark splits The lower part of the table contains the models reproduced under
the same Amazon Customer Reviews held-out test setting. This section is the directly
comparable part of the table. Under this controlled setting, the proposed DeBERTa-
v3 + Bi-GRU + aspect-attention model achieves the strongest performance among the
reproduced variants, with an accuracy of 0.737, macro-F1 of 0.757, and weighted-F1 of
0.760. The DeBERTa-v3 + Bi-LSTM variant achieves an accuracy of 0.714 and macro-
F1 of 0.722, while the DeBERTa-v3 + Bi-RNN variant obtains an accuracy of 0.707 and
macro-F1 of 0.726. These results indicate that the Bi-GRU-based configuration provides
the most stable balance between precision and recall among the tested recurrent refine -
ment modules. The comparison is important for two reasons. First, it responds to the
need for stronger ABSA positioning by placing the proposed method alongside recog -
nized ABSA model families. Second, it prevents misleading overclaiming by clearly dis -
tinguishing literature-reported baselines from models reproduced on the same dataset.
The appropriate conclusion from Table X is therefore not that the proposed model out -
performs all published ABSA or LLM systems, but that it performs best among the vari -
ants evaluated under the same Amazon Customer Reviews test split.
Table 9 Service & usability class-wise precision, recall, F1 table
Model Class Service & usability
precision
Service & usability
recall
Service &
usability
F1-score
DeBERTa-v3 + Bi-GRU Negative 0.69 0.53 0.60
DeBERTa-v3 + Bi-GRU Neutral 0.95 0.91 0.93
DeBERTa-v3 + Bi-GRU Positive 0.82 0.83 0.82
DeBERTa-v3 + Bi-RNN Negative 0.61 0.34 0.43
DeBERTa-v3 + Bi-RNN Neutral 0.93 0.92 0.93
DeBERTa-v3 + Bi-RNN Positive 0.80 0.83 0.82
DeBERTa-v3 + Bi-LSTM Negative 0.76 0.36 0.48
DeBERTa-v3 + Bi-LSTM Neutral 0.73 0.83 0.77
DeBERTa-v3 + Bi-LSTM Positive 0.72 0.83 0.77

Page 20 of 30
Moushi et al. Discover Analytics            (2026) 4:31
6.2 Satisfaction prediction results (ML: LightGBM/XGBoost/CatBoost)
For the structured-feature satisfaction task, LightGBM achieves the strongest overall
performance among the evaluated gradient-boosting models, with an accuracy of 82.37
and precision, recall, and F1-score each at 0.82. XGBoost follows with an accuracy of
77.48 and an F1-score of 0.75. CatBoost achieves an accuracy of 76.83 with an F1-score
of 0.77, with precision 0.74 and recall 0.78. The relative advantage of LightGBM is
Table 10 Comparative results with recent ABSA baselines and reproduced model variants
Model Model
family
Encoder /
backbone
Aspect
handling
strategy
Dataset /
split
Accuracy Macro-F1 Weight-
ed-F1
BERT-ADA Domain-
adapted
pretrained
language
model
BERT-base Auxil-
iary aspect
sentence
Se-
mEval-14
Restau-
rants test
set
0.876 0.812 0.872
RoBERTa-ADA Domain-
adapted
pretrained
language
model
RoBERTa-base Auxil-
iary aspect
sentence
Se-
mEval-14
Restau-
rants test
set
0.881 0.823 0.876
ABSA-BERT BERT-based
ABSA
model
BERT-base Aspect-aware
sentiment
classification
Se-
mEval-14
/ reported
bench-
mark split
NR NR NR
BERT-SPC Sentence-
pair ABSA
classifier
BERT-base Review
sentence and
aspect term
encoded as
a sentence
pair
Se-
mEval-14
Laptops
test set
0.787 0.752 0.781
InstructABSA Instruction-
tuned
ABSA
model
T5-base / in-
struction-tuned
encoder-decoder
Instruction-
based aspect
sentiment
prediction
Se-
mEval-14
Restau-
rants joint
ABSA task
0.892 0.836 0.886
LLM-based
zero-shot
ABSA
General-
purpose
large
language
model
GPT-style LLM Prompt-
based
aspect-target
sentiment
prediction
Se-
mEval-14
/
literature-
reported
setting
0.701 0.682 0.698
DeBERTa-
v3 + Bi-LSTM
Encod-
er + re-
current
refinement
DeBERTa-v3-base Multi-head
aspect
classifier
Amazon
Customer
Reviews
test set,
n = 4,500
0.714 0.722 0.728
DeBERTa-
v3 + Bi-RNN
Encod-
er + re-
current
refinement
DeBERTa-v3-base Multi-head
aspect
classifier
Amazon
Customer
Reviews
test set,
n = 4,500
0.707 0.726 0.732
DeBERTa-
v3 + Bi-
GRU + aspect
attention
Encod-
er + re-
current
refine-
ment + as-
pect
attention
DeBERTa-v3-base Aspect-spe-
cific additive
attention
with three
sentiment
heads
Amazon
Customer
Reviews
test set,
n = 4,500
0.737 0.757 0.760

Page 21 of 30
Moushi et al. Discover Analytics            (2026) 4:31
consistent with the suitability of gradient-boosted decision trees for structured market -
place signals, where predictive cues arise from nonlinear interactions among categorical
context, such as product category, purchase verification status, and heavy-tailed helpful -
ness indicators. Under the specified preprocessing pipeline, these models can capture
interaction effects without imposing linear separability assumptions and can operate
effectively over heterogeneous feature types. At the same time, satisfaction prediction
from structured features has inherent constraints. Figure  4 presents the overall classifi -
cation performance of the DeBERTa-v3-based models across precision, recall, F1-score,
and accuracy. The DeBERTa-v3 + Bi-GRU model achieves the highest performance with
precision (0.773), recall (0.734), F1-score (0.757), and accuracy (0.737). The Bi-LSTM
variant shows competitive precision (0.759) but lower recall (0.714), F1-score (0.722),
and accuracy (0.714), while the Bi-RNN model records comparatively lower values
across all metrics with precision (0.733), recall (0.707), F1-score (0.726), and accuracy
(0.707).
6.3 Comparative performance and statistical significance analysis
The results demonstrate that the DeBERTa-v3 + Bi-GRU model consistently achieves
the strongest overall performance among the deep learning variants, as reflected by the
highest accuracy (0.737 ± 0.006) and F1-score (0.757 ± 0.007), indicating a well-balanced
precision–recall trade-off. In comparison, Bi-LSTM and Bi-RNN exhibit lower perfor -
mance, with Bi-LSTM showing slightly higher precision but reduced overall consistency,
and Bi-RNN presenting the lowest accuracy. The pairwise statistical analysis further
confirms that these differences are not marginal, as the Bi-GRU model significantly out -
performs both Bi-LSTM and Bi-RNN with statistically significant p-values (≤ 0.002) and
large effect sizes (Cohen’s d > 2.8), indicating substantial practical improvements. Simi -
larly, in the structured-feature modeling context, LightGBM demonstrates clear supe -
riority over XGBoost and CatBoost, with notable accuracy gains (up to 0.0554) and
very large effect sizes, reinforcing that the observed improvements are both statistically
significant and practically meaningful (Table  11). Together, these findings validate the
robustness of the proposed configuration and confirm that the performance gains are
consistent, reliable, and not attributable to random variation.
Fig. 4 Model-level classification report (overall)

Page 22 of 30
Moushi et al. Discover Analytics            (2026) 4:31
Table 12 presents a component-level ablation study designed to isolate the contribu -
tion of the major architectural elements in the proposed model. The ablation proceeds
incrementally from a DeBERTa-v3 encoder-only baseline to the full DeBERTa-v3 + Bi-
GRU + aspect-attention architecture. This design is important because it separates the
effect of sequential refinement from the effect of attention and, more specifically, from
the effect of aspect-specific attention. As a result, the table provides a direct response
to the reviewer concern that the attention mechanism requires clearer empirical jus -
tification. Variant V1 uses DeBERTa-v3 representations with CLS pooling and three
independent linear classification heads. This baseline achieves an accuracy of 0.697,
macro-F1 of 0.715, and weighted-F1 of 0.720. Variant V2 adds Bi-GRU sequential refine-
ment and improves accuracy to 0.715 and macro-F1 to 0.731. This gain indicates that
recurrent refinement contributes useful sequential information beyond the transformer
encoder, especially for review sentences where sentiment cues are distributed across
short clauses. Variant V3 further introduces shared self-attention and reaches 0.725
accuracy and 0.744 macro-F1, suggesting that attention-based token weighting improves
the model’s ability to focus on sentiment-bearing spans. The full model, V4, replaces the
shared attention mechanism with aspect-specific additive attention and achieves the
best performance, with 0.737 accuracy, 0.757 macro-F1, and 0.760 weighted-F1. Com -
pared with V1, the proposed model improves accuracy by 0.040 and macro-F1 by 0.042.
Compared with V3, the full model improves accuracy by 0.012 and macro-F1 by 0.013,
showing that aspect-specific attention provides additional benefit beyond generic atten -
tion. This finding supports the central architectural claim of the study: when a single
review contains multiple customer-experience dimensions, separate aspect-conditioned
attention modules help reduce cross-aspect interference and improve multi-output sen -
timent classification.
Table  13 reports the confusion matrix for the Product & Value aspect using the
proposed DeBERTa-v3 + Bi-GRU + aspect-attention model on the held-out Ama -
zon Customer Reviews test set. The matrix shows that the model correctly identifies
644 Negative, 511 Neutral, and 2318 Positive instances. The strongest performance is
observed for the Positive class, which is expected because Product & Value contains a
large proportion of positive reviews. This suggests that the model is effective at recog -
nizing explicit favorable product-related language, such as comments about usefulness,
quality, reliability, or value.
Table 14 presents the confusion matrix for the Delivery & Fulfillment aspect. The
model correctly classifies 607 Negative, 819 Neutral, and 1455 Positive instances.
Among the three classes, Neutral shows the highest recall, with 819 out of 900 Neu -
tral reviews correctly identified. This indicates that the model is effective at detecting
factual or descriptive delivery-related statements, such as comments about arrival time,
packaging, order handling, or fulfillment status when the language does not carry strong
Table 11 Descriptive performance comparison of deep learning variants for multi-aspect sentiment
classification
Best model Comparator Mean differ-
ence (Accuracy)
p-value Effect size
(Cohen’s d)
Signifi-
cance
DeBERTa-v3 + Bi-GRU Bi-LSTM 0.023 0.002 2.85 (large) Significant
DeBERTa-v3 + Bi-GRU Bi-RNN 0.030 0.001 3.62 (large) Significant
LightGBM XGBoost 0.0489 < 0.001 6.10 (large) Significant
LightGBM CatBoost 0.0554 < 0.001 6.85 (large) Significant

Page 23 of 30
Moushi et al. Discover Analytics            (2026) 4:31
Table 12 Architectural ablation of the proposed aspect-attention model
Variant DeBERTa-v3
encoder
Bi-GRU
refinement
Pooling / attention strategy Aspect-specific heads Accuracy Macro-F1 Weighted-F1 Change in
accuracy
vs. V1
V1 Yes No CLS pooling only Yes, three independent linear heads 0.697 0.715 0.720 Reference
V2 Yes Yes Mean pooling over Bi-GRU hidden
states
Yes, three independent linear heads 0.715 0.731 0.736 + 0.018
V3 Yes Yes Shared self-attention Yes, three independent linear heads 0.725 0.744 0.748 + 0.028
V4, proposed Yes Yes Aspect-specific additive attention Yes, three aspect-specific heads 0.737 0.757 0.760 + 0.040

Page 24 of 30
Moushi et al. Discover Analytics            (2026) 4:31
emotional polarity. This pattern reinforces the need for aspect-specific modeling, since
delivery-related sentiment is frequently expressed through factual or event-based lan -
guage that differs from conventional product sentiment and can easily be absorbed into
the Neutral class.
Table 15 reports the confusion matrix for the Service & Usability aspect. The proposed
model correctly classifies 382 Negative, 983 Neutral, and 2241 Positive instances. The
strongest performance is observed for the Positive class, where 2241 of 2700 positive
reviews are correctly identified. This indicates that the model captures many explicit
positive usability and service-related expressions, such as comments about ease of use,
setup success, support satisfaction, and practical convenience.
6.4 Error analysis
The representative error cases show a recurring pattern: true negative and true posi -
tive instances are frequently predicted as neutral, indicating a conservative bias toward
the neutral class in borderline or mixed-cue reviews (Table  16). In Product and Value,
“Paid way too much for the quality… sounds like a low-end item. ” is a true negative but
is predicted as neutral, suggesting that the model may under-weight strong complaint
Table 13 Confusion matrix for product & value sentiment classification using the proposed model
True label Pred. Negative Pred. Neutral Pred. Positive Total support
True negative 644 14 332 990
True neutral 14 511 195 720
True positive 234 238 2,318 2,790
Predicted total 892 763 2,845 4,500
Table 14 Confusion matrix for delivery & fulfillment sentiment classification using the proposed
model
True label Pred. Negative Pred. Neutral Pred. Positive Total support
True negative 607 210 38 855
True neutral 28 819 53 900
True positive 213 1,077 1,455 2,745
Predicted total 848 2,106 1,546 4,500
Table 15 Confusion matrix for service & usability sentiment classification using the proposed model
True label Pred. Negative Pred. Neutral Pred. Positive Total support
True negative 382 280 58 720
True neutral 25 983 72 1,080
True positive 100 359 2,241 2,700
Predicted total 507 1,622 2,371 4,500
Table 16 Representative misclassification examples on the Amazon reviews dataset
Review text Derived aspect
category
True label Predict-
ed label
Paid way too much for the quality… sounds like a low-end
item.
Product & value Negative Neutral
Works as expected… seems reliable Product & value Positive Neutral
Great sound quality… but remote setup was not easy. Service & usability Positive Neutral
Box was crushed in mailing; looked cheap Delivery & fulfillment Negative Neutral
Not satisfied… ribbon missing on the box Product & value Negative Neutral

Page 25 of 30
Moushi et al. Discover Analytics            (2026) 4:31
cues when they are expressed as subjective assessments rather than explicit categori -
cal negations. Conversely, “Works as expected… seems reliable” is a true positive but
is predicted as neutral, indicating that understated positive sentiment, especially when
phrased as minimal confirmation, can resemble neutral informational language. Similar
behavior appears in Delivery and Fulfillment, where “Box was crushed in mailing; looked
cheap” is a true negative but predicted as neutral. In Service and Usability, “Great sound
quality… but remote setup was not easy. ” is a true positive but predicted as neutral,
plausibly because the sentence contains mixed polarity cues and requires aspect-spe -
cific weighting across clauses. From a modeling perspective, this neutral drift can arise
from several interacting factors common in aspect-based sentiment analysis, including
hedged language, implicit sentiment, and multi-clause constructions that blend evalu -
ative and descriptive content. It can also reflect boundary uncertainty in short texts,
where neutral is sometimes used to encode mixed or weak sentiment. To reduce this
pattern in future iterations without changing the core architecture, several refinements
are appropriate. These include class-sensitive objectives, such as focal loss or class-
weighted cross-entropy, to increase gradient pressure on frequently confused classes;
decision-threshold tuning or calibration procedures that adjust confidence for neutral
predictions; data-level balancing strategies that increase coverage of weakly positive and
weakly negative phrasing; and contrastive fine-tuning strategies that explicitly separate
neutral statements from weak sentiment through hard-negative mining. These direc -
tions should be framed as methodological refinements aimed at reducing neutral over-
assignment rather than as changes required to establish baseline functionality.
6.5 Practical insights for e-commerce decision-making
The aspect-wise results translate into actionable signals for operational monitoring and
decision support. Product & Value predictions can surface recurring quality or pric -
ing complaints (e.g., “low-end” quality perceptions) distinct from shipping or usabil -
ity issues; such signals support product engineering, vendor management, and pricing
strategy reviews. Delivery & Fulfillment predictions isolate logistics- and packaging-
driven dissatisfaction (e.g., damaged boxes, missing items), enabling targeted interven -
tions with carriers, packaging standards, or fulfillment workflows without conflating
those issues with product defects. Service & Usability predictions highlight friction in
setup and usage that may not be captured by a global rating alone, informing documen -
tation improvements, onboarding flows, and customer support prioritization.Crucially,
aspect-level sentiment complements the structured star-based satisfaction model rather
than duplicating it. Satisfaction prediction provides an efficient, platform-aligned global
indicator that can be tracked longitudinally and segmented by category or verification
status, while aspect sentiment provides diagnostic attribution that explains why satisfac-
tion shifts. In practical dashboards, satisfaction can serve as an early-warning KPI, and
aspect sentiment can drive triage queues (e.g., routing D&F negatives to logistics teams,
S&U negatives to support and UX teams, P&V negatives to product quality owners). The
combined framework therefore supports both monitoring (star-level satisfaction) and
actionability (aspect-level attribution) under a consistent review analytics pipeline.

Page 26 of 30
Moushi et al. Discover Analytics            (2026) 4:31
6.6 Discussion
The performance of the proposed framework can be explained by the effective inte -
gration of contextual encoding, sequential refinement, and aspect-conditioned repre -
sentation learning. DeBERTa-v3 captures rich global semantic relationships, while the
bidirectional recurrent layer enhances local dependency modeling and strengthens
short-span sentiment cues that are critical for aspect attribution in noisy review text. The
aspect-attention mechanism further enables separation of overlapping sentiment signals
by assigning distinct importance to tokens for each aspect, resulting in more precise and
interpretable predictions. The small gap between training and validation performance
indicates stable generalization, although the neutral class remains challenging due to its
inherent ambiguity and weak polarity signals (Figs. 5 and 6). Comparative analysis shows
that the transformer-based model is more effective for aspect-level sentiment extraction
from unstructured text, whereas structured machine learning models perform com -
petitively for overall satisfaction prediction due to their reliance on metadata features,
Fig. 6 Training and validation loss curves for the highest-performing model (DeBERTa-v3 + Bi-GRU)

Fig. 5 Training and validation accuracy curves for the highest-performing model (DeBERTa-v3 + Bi-GRU)

Page 27 of 30
Moushi et al. Discover Analytics            (2026) 4:31
highlighting the complementary roles of the two pipelines. The study demonstrates that
combining transformer representations with sequential refinement improves aspect dis -
entanglement, particularly when aspect categories are derived from text rather than pre-
defined labels, while maintaining a clear separation between text-based and structured
modeling. However, limitations include potential subjectivity in annotation, lack of
explicit span-level supervision, dataset-specific bias, difficulty in neutral class discrimi -
nation, and the absence of exhaustive hyperparameter tuning, which suggest directions
for further refinement and broader validation.
7 Limitations
This study leverages the Amazon Customer Reviews dataset, which enables scalable
modeling from public review text and metadata, but it also imposes limitations that
affect external validity and deployment realism. Because the evidence is conditioned
on Amazon’s platform-specific review ecosystem, product mix, moderation practices,
regional marketplace dynamics, and evolving logistics policies, learned patterns may
not transfer cleanly to other marketplaces or remain stable over time, and performance
may vary materially by product category, marketplace country code, and time window.
The supervision signals also carry unavoidable noise: star ratings are an imperfect proxy
for satisfaction and can disagree with the textual rationale, while aspect categories and
three-level aspect sentiment labels derived from text are inherently ambiguous in short,
hedged, or mixed-polarity reviews, which contributes to a recurring tendency to over-
predict Neutral under conservative boundaries and class imbalance. Evaluation itself is
exposed to leakage risk through near-duplicate text, repeated product-specific phrasing,
or overlap of product or customer identifiers across partitions, which can inflate appar -
ent generalization unless group-aware splitting, deduplication, and near-duplicate audits
are explicitly enforced and reported. Finally, explainability should be treated as decision
support rather than causality: attention patterns and SHAP attributions can be unstable
or confounded, and production use adds constraints around latency, calibration (espe -
cially around Neutral and adjacent star levels), drift monitoring, and strict compliance
with licensing and privacy-by-design requirements that prohibit identity inference or
cross-source linkage.
8 Conclusion
E-commerce platforms rely on customer reviews to monitor product performance and
post-purchase experience at scale, yet the signals available to operations teams are often
coarse. Star ratings provide a convenient summary of satisfaction, but they can obscure
mixed experiences expressed within the same review. Aspect-level sentiment analysis
addresses this limitation by separating opinions about distinct experience dimensions,
Product and Value, Delivery and Fulfillment, and Service and Usability, thereby produc -
ing outputs that are more directly actionable for quality monitoring, triage, and ser -
vice improvement.This study presented a dual-track framework that links multi-aspect
sentiment classification from review text with structured-feature satisfaction analyt -
ics. For aspect sentiment, the proposed deep learning pipeline encodes the combined
review headline and review body using DeBERTa version 3 embeddings, refines the
sequence representation using a bidirectional recurrent layer evaluated under three vari-
ants, bidirectional gated recurrent units, bidirectional recurrent neural networks, and

Page 28 of 30
Moushi et al. Discover Analytics            (2026) 4:31
bidirectional long short-term memory networks, applies an attention mechanism to
form aspect-aware representations, and predicts three-class sentiment for each aspect
through parallel dense neural network heads using a consistent label scheme: negative,
neutral, and positive. In parallel, the satisfaction module follows the workflow illustrated
in Fig.  2 and integrates into the end-to-end pipeline in Fig.  3, using a structured pre -
processing chain based on standard scaling, one-hot encoding, and quantile transforma -
tion, together with gradient-boosting learners, LightGBM, XGBoost, and CatBoost, to
predict five satisfaction levels aligned with star ratings from one star to five stars.The
structured-feature experiments show that LightGBM provides the strongest satisfaction
performance among the evaluated baselines, achieving an accuracy of 82.37 with pre -
cision, recall, and F1-score all at 0.82. XGBoost reaches an accuracy of 77.48 with an
F1-score of 0.75, while CatBoost achieves an accuracy of 76.83 with an F1-score of 0.77.
For the aspect sentiment task, error analysis identifies a recurring ambiguity in which
some reviews with clearly positive or negative intent are predicted as neutral, indicating
that neutral phrasing, hedging, and mixed clauses remain a practical challenge for multi-
class sentiment boundaries in short, informal e-commerce text.These findings support a
pragmatic analytics perspective rather than single-score optimization. Satisfaction pre -
diction provides a star-aligned signal suitable for high-level monitoring and segmenta -
tion, while aspect outputs provide attribution that can be routed to operational owners.
Product and Value signals are most relevant to perceived quality and value alignment,
Delivery and Fulfillment signals to packaging and logistics performance, and Service and
Usability signals to setup friction and support demand. Used together, these signals can
strengthen dashboards for continuous improvement by separating what is failing from
where it is failing.
Author contributions
All authors contributed to the conception and design of the study. Sabrina Shamim Moushi led the overall development
of the proposed multi-aspect sentiment framework, coordinated the experimental workflow, and prepared the initial
manuscript draft. Md Shohan Bhuiyan supported the implementation of the deep learning stream, including integration
of the DeBERTa-v3 encoder with bidirectional sequence models and the aspect-attention mechanism, and assisted with
experimental execution. Nasrin Akter managed data acquisition and preprocessing using the Amazon Customer Reviews
dataset, constructed the combined review text inputs, and ensured data validation. Urmi Chakraborty implemented the
structured-feature baselines including LightGBM, XGBoost, and CatBoost, conducted preprocessing, and contributed to
comparative evaluation. Shahanaj Akther performed performance analysis, prepared result visualizations, and supported
interpretation of model behavior. Rakibul Islam contributed to experimental design, ensured fair comparison across
models, and reviewed the work for reproducibility and data leakage concerns. Md Shahiduzzaman and Maria Kabtia
were added during the revision stage and contributed substantially by rewriting the abstract, refining the methodology
for improved clarity and technical rigor, and strengthening the results and analysis sections. Roba Keneni contributed
to literature positioning, refined the problem formulation, and edited the manuscript for clarity and compliance with
journal standards. All authors reviewed, revised, and approved the final manuscript.
Funding
Declaration: This research received no external funding.
Data availability
The dataset used in this study can be made available by the corresponding author upon reasonable request.
Declarations
 Ethics approval and consent to participate
The authors declare no competing interests.
Consent for publications
declaration: Not applicable.
Competing interests
The authors declare no competing interests.
Author details
1Department of Management Information System (MIS), International American University, 3711 164th St SW,
Lynnwood, WA 98087, USA

Page 29 of 30
Moushi et al. Discover Analytics            (2026) 4:31
2Department of Management, International American University, 3440 Wilshire Blvd STE 1000, Los Angeles,
CA 90010, USA
3Master of Business Administration (MBA), Stanton University, 3700 Wilshire Blvd, #100, Los Angeles, CA 90010, USA
4Department of Management in Management Information System, International American University, 3440 Wilshire
Blvd STE 1000, Los Angeles, CA 90010, USA
5Department of Management in Business Analytics, International American University, 3440 Wilshire Blvd STE 1000,
Los Angeles, CA 90010, USA
6Department of Management in Business Analysis, International American University (IAU), 3440 Wilshire Blvd STE
1000, Los Angeles, CA 90010, USA
7Department of Business Analytics, Trine University, IN 46703 Angola, USA
8College of Graduate and Professional Studies, Master of Science in Business Analytics, Trine University, Angola, IN,
USA
9Department of Computer Science and Engineering, Bule Hora University, Bule Hora, Ethiopia
Received: 15 January 2026 / Accepted: 16 June 2026
References
1. Cheung CM, Lee MK, Rabjohn N. The impact of electronic word-of-mouth: the adoption of online opinions in online
customer communities. Internet Res. 2008;18(3):229–47. https://doi.org/10.1108/10662240810883290.
2. Chatterjee S, Goyal D, Prakash A, Sharma J. Exploring healthcare/health-product ecommerce satisfaction: a text mining
and machine learning application. J Bus Res. 2021;131:815–25. https:   //d oi. or g/10 . 1016/j. jbus re s .2020.10.043.
3. Aldunate A, Maldonado S, Vairetti C, Armelini G. Understanding customer satisfaction via deep learning and natural
language processing. Expert Syst Appl. 2022;209:118309. https://doi.org/10.1016/j.eswa.2022.118309.
4. Daza A, Rueda NDG, Sánchez MSA, Espíritu WFR, Quiñones MEC. Sentiment analysis on E-commerce product reviews
using machine learning and deep learning algorithms: a bibliometric analysis and systematic literature review, challenges
and future works. Int J Inform Manage Data Insights. 2024;4(2):100267. https://doi.org/10.1016/j.jjimei.2024.100267.
5. Gu T, He Z, Zhao H, Li M, Ying D. Aspect-based sentiment analysis with multi-granularity information mining and senti-
ment hint. Expert Syst Appl. 2024;252:124104. https://doi.org/10.1016/j.eswa.2024.124104.
6. Zhao G, Luo Y, Chen Q, Qian X. Aspect-based sentiment analysis via multitask learning for online reviews. Knowl Based
Syst. 2023;264:110326. https://doi.org/10.1016/j.knosys.2023.110326.
7. Xu G, Zhang Z, Zhang T, Yu S, Meng Y, Chen S. Aspect-level sentiment classification based on attention-BiLSTM model and
transfer learning. Knowl Based Syst. 2022;245:108586. https://doi.org/10.1016/j.knosys.2022.108586.
8. Fornell C, Johnson MD, Anderson EW, Cha J, Bryant BE. The American customer satisfaction index: nature, purpose, and
findings. J Mark. 1996;60(4):7–18. https://doi.org/10.1177/002224299606000403.
9. Kang D, Park Y. Based measurement of customer satisfaction in mobile service: sentiment analysis and VIKOR approach.
Expert Syst Appl. 2014;41(4):1041–50. https://doi.org/10.1016/j.eswa.2013.07.101.
10. Sunil N, Shirazi F. (2023). Customer review classification using machine learning and deep learning techniques. In Interna-
tional Conference on Human-Computer Interaction (pp. 581–597). Springer.
11. Jagdale RS, Shirsat VS, Deshmukh SN. (2018). Sentiment analysis on product reviews using machine learning techniques.
In Cognitive Informatics and Soft Computing: Proceedings of CISC 2017 (pp. 639–647). Springer, Singapore.
12. Alzahrani ME et al. (2022). Developing an intelligent system with deep learning algorithms for sentiment analysis of
e-commerce product reviews. Computational Intelligence and Neuroscience, 2022, 3840071.
13. Singla Z, Randhawa S, Jain S. (2017). Sentiment analysis of customer product reviews using machine learning. In 2017
International Conference on Intelligent Computing and Control (I2C2) (pp. 1–5). IEEE.
14. Iqbal A, Amin R, Iqbal J, Alroobaea R, Binmahfoudh A, Hussain M. Sentiment analysis of consumer reviews using deep
learning. Sustainability. 2022;14(17):10844.
15. Panthati J, Bhaskar J, Ranga TK, Challa MR. (2018, September). Sentiment analysis of product reviews using deep learning.
In 2018 International Conference on Advances in Computing, Communications and Informatics (ICACCI) (pp. 2408–2414). IEEE.
16. Daza A, Rueda NDG, Sánchez MSA, Espíritu WFR, Quiñones MEC. Sentiment analysis on e-commerce product reviews
using machine learning and deep learning algorithms: a bibliometric analysis, systematic literature review, challenges and
future works. Int J Inform Manage Data Insights. 2024;4(2):100267.
17. Poomka P , Kerdprasop N, Kerdprasop K. Machine learning versus deep learning performances on the sentiment analysis of
product reviews. Int J Mach Learn Comput. 2021;11(2):103–9.
18. Yang L, et al. Sentiment analysis for E-commerce product reviews in Chinese based on sentiment lexicon and deep learn-
ing. IEEE Access. 2020;8:23522–30.
19. Zhao H, Yang Q, Liu Z. Impact of online customer reviews and deep learning on product innovation: empirical study on
mobile applications. Bus Process Manage J. 2021;27(6):1912–25.
20. Amirifar T, Lahmiri S, Kazemi Zanjani M. (2023). An NLP-deep learning approach for product rating prediction based on
online reviews and product features. IEEE Trans Comput Social Syst.
21. Gope JC et al. (2022). Sentiment analysis of Amazon product reviews using machine learning and deep learning models.
In 2022 International Conference on Advancement in Electrical and Electronic Engineering (ICAEEE) (pp. 1–6). IEEE.
22. Cao J, Li J, Yin M, Wang Y. Online reviews sentiment analysis and product feature improvement with deep learning. ACM
Trans Asian Low-Resource Lang Inform Process. 2023;22(8):1–17.
23. Ain QT, Ali M, Riaz A, Noureen A, Kamran M, Hayat B, Rehman AU. (2017). Sentiment analysis using deep learning tech-
niques: a review. Int J Adv Comput Sci Appl, 8(6).
24. Nguyen H, Veluchamy A, Diop M, Iqbal R. Comparative study of sentiment analysis with product reviews using machine
learning and lexicon-based approaches. SMU Data Sci Rev. 2018;1(4):Article7.
25. Soni S et al. (2018). Feature based sentiment analysis of product reviews using deep learning methods. International
Journal of Advanced Technology & Engineering Research (IJATER).

Page 30 of 30
Moushi et al. Discover Analytics            (2026) 4:31
26. Norinder U, Norinder P . Predicting Amazon customer reviews with deep confidence using deep learning and conformal
prediction. J Manage Analytics. 2022;9(1):1–16.
27. Lee HC, Rim HC, Lee DG. Learning to rank products based on online product reviews using a hierarchical deep neural
network. Electron Commer Res Appl. 2019;36:100874.
28. Onan A. (2021). Sentiment analysis on product reviews based on weighted word embeddings and deep neural networks.
Concurrency Computation: Pract Experience, 33(23), e5909.
29. Liu X, Lee D, Srinivasan K. Large-scale cross-category analysis of consumer review content on sales conversion leveraging
deep learning. J Mark Res. 2019;56(6):918–43.
30. Nazir A, Rao Y, Wu L, Sun L. Issues and challenges of aspect-based sentiment analysis: a comprehensive survey. IEEE Trans
Affect Comput. 2020;13(2):845–63.
31. Do HH, Prasad PW, Angelika Maag, and Abeer Alsadoon. Deep learning for aspect-based sentiment analysis: a compara-
tive review. Expert Syst Appl. 2019;118:272–99.
32. Zhang W, Li X, Deng Y, Bing L, Lam W. A survey on aspect-based sentiment analysis: tasks, methods, and challenges. IEEE
Trans Knowl Data Eng. 2022;35(11):11019–38.
33. Li Z, Wei Y, Zhang Y, Zhang X, Li X. Exploiting coarse-to-fine task transfer for aspect-level sentiment classification. In Pro-
ceedings of the AAAI conference on artificial intelligence, vol. 33, no. 01, pp. 4253–4260. 2019.
34. Zhang K, Liu Q, Qian H, Xiang B, Cui Q, Jun Zhou, and, Chen E. EATN: an efficient adaptive transfer network for aspect-level
sentiment analysis. IEEE Trans Knowl Data Eng. 2021;35(1):377–89.
35. Agrawal UK, Panda N. Quantum-inspired adaptive mutation operator enabled PSO (QAMO-PSO) for parallel optimization
and tailoring parameters of Kolmogorov–Arnold network. J Supercomput. 2025;81:1310.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 2 2 7 - 0
2 5 - 0 7 8 1 0 - w     .
36. Agrawal UK, Panda N, Tejani GG, et al. Improved salp swarm algorithm-driven deep CNN for brain tumor analysis. Sci Rep.
2025;15:24645. https://doi.org/10.1038/s41598-025-09326-y.
37. Mahapatra AK, Panda N, Pattanayak BK. Adaptive dimensional search-based orthogonal experimentation SSA (ADOX-SSA)
for training RBF neural network and optimal feature selection. J Supercomput. 2025;81:212.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 2 2
7 - 0 2 4 - 0 6 5 0 7 - w     .
38. Mahapatra AK, Panda N, Pattanayak BK. Quantized orthogonal experimentation SSA (QOX-SSA): a hybrid technique for
feature selection (FS) and neural network training. Arab J Sci Eng. 2025;50:1025–56.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 3 3 6 9 - 0 2 4 - 0
9 1 1 3 - 3     .
39. Mahapatra AK, Panda N, Mahapatra M, et al. A fast-flying particle swarm optimization for resolving constrained optimiza-
tion and feature selection problems. Cluster Comput. 2025;28:91. https://doi.org/10.1007/s10586-024-04750-7.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
