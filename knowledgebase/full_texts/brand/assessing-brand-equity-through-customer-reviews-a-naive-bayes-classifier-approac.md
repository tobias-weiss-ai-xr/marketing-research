---
title: 'Assessing brand equity through customer reviews: a naïve Bayes classifier approach'
url: https://doi.org/10.1504/ijbis.2026.154480
category: brand
subcategory: measurement
date: 2026-01
venue: International Journal of Business Information Systems
authors:
- Jaesun Yeom
- JiYu Kim
- Han Gyun Woo
source: openalex-oa
pdf_url: https://doi.org/10.1504/ijbis.2026.154480
pages: 23
chars: 61597
fetched_at: '2026-11-08T18:03:25+00:00'
kb_version: 1
---

# Assessing brand equity through customer reviews: a naïve Bayes classifier approach

International Journal of Business Information Systems

ISSN online: 1746-0980 - ISSN print: 1746-0972
https://www.inderscience.com/ijbis

Assessing brand equity through customer reviews: a naïve
Bayes classifier approach

Jaesun Yeom, JiYu Kim, Han-Gyun Woo

DOI: 10.1504/IJBIS.2025.10077419

Article History:
Received:
Accepted:
Published online: 30 June 2026
Powered by TCPDF (www.tcpdf.org)
Copyright © 2026 Inderscience Enterprises Ltd.

   Int. J. Business Information Systems, Vol. 52, No. 5, 2026 21

   Copyright © The Author(s) 2026. Published by Inderscience Publishers Ltd. This is an Open Access Article
distributed under the CC BY license. (http://creativecommons.org/licenses/by/4.0/)

Assessing brand equity through customer reviews:
a naïve Bayes classifier approach
Jaesun Yeom
Department of Industrial Management Engineering,
Hanbat National University,
125 Dongseo-daero, Daejeon, South Korea
Email: jsyeom@hanbat.ac.kr
JiYu Kim
School of Business Administration,
Ulsan National Institute of Science and Technology,
50 UNIST-gil, Ulsan, South Korea
Email: gu1305@unist.ac.kr
Han-Gyun Woo*
Graduate School of Management of Technology,
Sogang University,
35 Baekbeom-ro, Mapo-gu, Seoul, South Korea
Email: hwoo@sogang.ac.kr
*Corresponding author
Abstract: Customer-based brand equity has been critical to gaining a
competitive advantage in the marketplace. Despite the usefulness of
conventional survey-based measurement, many scholars and practitioners face
difficulties in comparing brand equity across brands, sectors, and products
owing to the limitations of survey-bas ed measurement. This study proposes a
machine learning method to complement  traditional survey-based measures.
Our approach comprises four major stages: 1) extracting seed phrases from
brand equity survey questionnaires; 2) identifying response sentences from
customer reviews; 3) assigning scores to  brand equity; 4) replicating regression
models from previous empirical studies to  validate our approach. Our analysis
examined 65,057 vacuum cleaner customer reviews from an online
e-commerce platform, (e.g., Amazon.com) representing six major brands. This
paper complements traditional studies by presenting a consistent and reliable
measurement methodology.
Keywords: brand equity; machine learning;  naïve Bayes classification;
customer reviews.
Reference to this paper should be made as follows: Yeom, J., Kim, J. and
Woo, H-G. (2026) ‘Assessing brand equity  through customer reviews: a naïve
Bayes classifier  approach’, Int. J. Business Information Systems , Vol. 52,
No. 5, pp.21–42.

   22 J. Yeom et al.

Biographical notes: Jaesun Yeom is an Assistant Professor of the Department
of Industrial Management Engineering at Hanbat National University. He
earned his PhD in Management E ngineering and BA in Technology
Management at the Ulsan National In stitute of Science and Technology
(UNIST). His scholarly pursuits are centred around examining fundamental
dynamics inherent in industrial phenom ena through the proxies derived from
graph network theory. His contributions have been disseminated through
Technology Analysis and Strategic Management , Smart Structures and
Systems, and Heliyon among others.
JiYu Kim earned her PhD in Manageme nt Engineering at the Ulsan National
Institute of Science and Technology (UNI ST). Her research interests include
the dynamics in digital platform ecosyst ems, strategic decision making of
platform participants, and AI technology acceptance.
Han-Gyun Woo is an Associate Professor of the Graduate School of
Management of Technology  at Sogang University. He earned his PhD in
Computer Information Systems at the Georgia State University, MS and BA in
Business Administration at the Seoul National University. His research
interests centre around technological innova tion, managerial issues of machine
learning, and industrial a pplications of AI. His work has been published in
Technovation, Technological Forecasting and Social Change , and IEEE
Software among others.
This paper is a revised and expanded version of a paper entitled ‘Measuring
brand equity using customer reviews: Naïve-Bayes classifier approach’
presented at International Conference on Electronic Commerce, Busan, South
Korea, 3–5 July 2019.

1 Introduction
Brand equity has been regarded as a critical indicator of a firm’s competitive advantage
since it reflects customer perceptions. It allows firms to enjoy substantial benefits such as
sustained price premiums, inelastic price sensitivity, competitive cost structures, and high
market share (Leuthesser et al., 1995; Ailawadi et al., 2003). Prior literature has
suggested numerous survey-bas ed brand equity measures to quantify brand equity as a
tangible index (Shankar et al., 2008; Chakraborty and Biswal, 2020). Scholars have
presented a variety of brand equity dimensions, such as brand loyalty, brand awareness,
perceived quality, and customer satisfaction, and questionnaires to measure brand equity
in various contexts (Farris et al., 2010).
Despite the advantages of conventional survey-based measurement methods, i.e., a
direct way of measuring customer perceptions, executable for general customers, and
facilitates easy understanding of the correlation among multiple dimensions, several
scholars have raised concerns about the shortcomings of conventional measures (Pappu
et al., 2005). First, measuring brand equity based on a large group of customers is
challenging due to sample size constraints. Second, conducting a survey involves high
costs and can be time-consuming (Aaker, 1996). Third, scholars often counter issues
when analysing survey data with time series (Park and Srinivasan, 1994). Lastly, survey
results tend to be inconsistent when repeated; therefore, scholars and marketing
practitioners face difficulties in conducting event studies, trend analyses, and comparative

    Assessing brand equity through customer reviews 23

analyses (Zarantonello and Schmitt, 2013). Notably, in a rapidly changing market
situation characterised by the evolving competition among brands and shifting brand
positions, there has been a growing need for consistent instruments that can grasp instant
changes in brand equity patterns and are repeatedly executable (Knox and Walker, 2001).
Customer reviews provide a significant opportunity to glimpse a firm’s overall brand
equity without posing direct questions to actual customers. Customer reviews are vital for
capturing immediate changes in customer perceptions, which cannot be assessed using
survey-based measures (Elwalda et al., 2016). Customers typically leave reviews for
products and brands they have consumed. Moreover, they voluntarily provide their
opinions, which can serve as direct answers to brand equity survey questions. By
identifying these opinions, we can gain insight into an alternative method for quantifying
brand equity by analysing customer reviews rather than relying solely on survey data.
This paper proposes a new method of measuring brand equity using customer
reviews, which is expected to complement conventional survey-based measurements. Our
approach comprises three major stages:
1 extracting brand equity phrase patterns from existing survey questionnaires
2 identifying response sentences via a machine learning technique
3 measuring brand equity through scoring processes.
The proposed method utilises seed phrase patterns from survey items, trains a naive
Bayes classifier to identify response sent ences, and extracts brand equity scores by
applying the model trained to unlabelled customer reviews across different units.
This paper is organised as follows: Sec tion 2 reviews related literature, while
Section 3 explains the research methodology. Next, Section 4 discusses implementation
of the proposed approach. Finally, Section 5 presents the conclusions of this study.
2 Related works
Brand equity has received significant attention from managers and marketing researchers
owing to its essential role as an intangible asset in firms (Aaker, 1996). Prior literature
has presented various perspectives on brand equity. Among these, the three major
perspectives are the financial, customer, and employee perspectives (Farjam and Hongyi,
2015). The financial perspective considers brand equity as the added value of having a
brand name (Simon and Sullivan, 1993; Shankar et al., 2008). Various financial indexes,
such as the return on investment (ROI) of research and development (R&D) expenditure
or marketing spending, have been used to measure financial brand equity (Oliveira et al.,
2015). Although this perspective helps to confirm the existence of  brand equity, it does
not provide a clear view of how brand equity is built.
The customer perspective of brand equity focuses on what customers think of a brand.
This perspective is such a multidimensional and complex concept that previous studies
have noted that many different types of measurements are required (Keller, 2003).
Furthermore, most academics and practitioners prefer this perspective because a brand is
of no value to shareholders unless it has customers (Farjam and Hongyi, 2015). Most
current literature has adopted this perspective in determining how brand equity is built
(Hoeffler and Keller, 2002).

   24 J. Yeom et al.

Some recent studies have argued that a brand’s value comes from within the brand
(King et al., 2012; Berger-Remy and Michel , 2015), i.e., the employees. The employee
perspective focuses on employee responses to work environments and cultures (King and
Grace, 2009). Despite its usefulness in explaining the nature of a brand, this perspective
requires the establishment of more linkages between the process of building brand equity
and its outcomes (King and Grace, 2010).
Among the various brand equity perspectives, customer-based brand equity has been
accepted and studied widely due to its direct  relationship to a firm’s decision-making
process and profits (Farjam and Hongyi, 2015). To better understand the dominant brand
equity perspective, the scope of this study is constrained to customer-based brand equity.
To date, numerous studies have explored the positive influence of customer-based
brand equity on purchase intention (Cobb-Walgren et al., 1995), future price premium
(Ailawadi et al., 2003), and firm performance (Kim and Kim, 2005). The conventional
way of measuring brand equity involves surveying customer perceptions (Aaker, 1996).
Table 1 show that several questionnaires have been designed to measure each dimension
of customer-based brand equity (Atilgan et  al., 2005; Bravo Gil et al., 2007). These
questionnaires have been used to measure consumer brand perceptions for decades.
Despite the convenience of survey-based m easurement, several studies have raised
concerns about the weaknesses associated with  the survey method (Park and Srinivasan,
1994). First, prior studies employed survey -based measurements to confirm the positive
relationship between brand equity and various marketing constructs. However, surveys
are less appropriate to provide real-time fee dback or track changes in brand equity over
time. Second, while surveys are useful for understanding the perceptions of a small
sample group, they are expensive and time-consuming when used to gauge the overall
attitudes of a larger sample group. Few studie s have attempted to employ an alternative
way of measuring brand equity using time-series financial data such as stock prices and
expected future earnings (Mizik, 2014). However, this data does not reflect customer
perceptions, which is essential for understanding the process of how brand equity is built.
Hence, significant gaps remain in the lite rature regarding how to measure real-time
customer brand equity based on a large group of people.
However, the advent of online shopping platforms has made it possible to measure
customer-based brand equity in real time. Customers began writing reviews on online
shopping platforms, which greatly influenced  customers’ purchase intentions, loyalty,
and attitudes toward products or brands (Xia et al., 2021; Du et al., 2022). Moreover,
people gradually came to care about the qua lity, valence, and credibility of customer
reviews (Teng et al., 2017; Chakraborty and Bhat, 2018; Yagci and Das, 2018; Wang
et al., 2021). Many studies have utilised cu stomer reviews as a legitimate source of
consumers’ overall sentiments regarding products  and services (Bagheri et al., 2013). A
recent study employed customer reviews as a core antecedent of a customer’s decision.
This study found that customer reviews are hi ghly credible and influential because they
do not originate from the product or service providers (Mudambi and Schuff, 2010).
Arguably, most advanced approaches have so ught to analyse customer reviews based on
brand constructs because customer reviews pr ovide a vibrant voice of consumers, which
affects the purchasing behaviour of potentia l customers (Ho-Dac et al., 2013; Kostyra
et al., 2016). Furthermore, many recent st udies have attempted to examine detailed
customer status or behaviour through customer reviews such as predicting customer
emotional categories, detecting self-disclosure behaviours, exploring customer’s
two-sided perspectives, and extracting actionable insights (Choi et al., 2022; Deng and

    Assessing brand equity through customer reviews 25

Ravichandran, 2023; Yang and Subramanyam, 2023; Yu et al., 2023b). Despite the
reliability of their content, online customer reviews have yet to become a source for
measuring brand equity.
Table 1 Brand equity dimensions  and measurement type
Authors Brand equity dimens ions Measurement type
Aaker (1996) Brand loyalty Survey
Perceived quality
Brand awareness
Brand associations
Customer satisfaction
Yoo and Donthu (2001) Brand loyalty Survey
Perceived quality
Brand awareness/associations
Atilgan et al. (2005) Brand loyalty Survey
Perceived quality
Brand awareness
Brand associations
Brand trust
Bravo Gil et al. (2007) Brand loyalty Survey
Perceived quality
Brand awareness
Brand associations
Mishra et al. (2011) Brand name Survey
Brand communication
Brand associations
Brand personality
Brand awareness
Brand image
Perceived brand quality
Brand loyalty
Another potential source of brand equity measurement is machine learning. Machine
learning utilises computational statistics to allow computers to learn from data. Several
researchers have attempted to use machine l earning techniques to analyse social media
content (Batrinca and Treleaven , 2015). Most of these appr oaches address the influence
of customer opinions provided via social media on various brand-related constructs, such
as purchase intention or customer retention (Sashi, 2012). Previous machine
learning-based approaches cannot be applied directly to measure brand equity for the
following reasons: First, regarding learning patterns, the method of constructing a feature
set, which is essential for learning patterns, varies based on the context. The patterns for
distinguishing positive and negative opinions differ from those for identifying response
sentences provided for brand equity questions. Second, the unit of analysis must be

   26 J. Yeom et al.

subdivided at the sentence level. Although previous approaches can be used to classify an
opinion as positive or negative, they can only be employed when dealing with paragraphs
and comments. These methods are likely to miss the characteristics contained within each
sentence. Thus, more integrated and spec ialised machine-learni ng approaches are
required to measure the brand equity of a large group of customers.
3 Methods
As shown in Figure 1, our proposed approach is designed to be executed in four discrete
stages:
1 extracting brand equity seed phrase  patterns from survey questionnaires
2 identifying response sentences using machine learning
3 measuring brand equity through scoring processes
4 validating the proposed approach through conducting linear regression used in
previous empirical studies.
Throughout these stages, our approach supports the conventio nal survey-based
measurement approach.
Figure 1 Research framework (see online version for colours)

The premises of our proposed approach are threefold. First, customer review authors
voluntarily respond to brand equity survey questions while expressing their opinions.
Second, these voluntary responses can be identified by searching for sentences containing
specific seed phrases. Third, these seed phrase patterns can be derived from brand equity
survey items. These premises provide hints for complementing traditional survey-based
measurements by identifying the response sentences correspondin g to brand equity
questions. In this context, a response senten ce is a naturally occurring sentence that can

    Assessing brand equity through customer reviews 27

serve as an answer to brand equity questionnaires. In this manner, we can quantify brand
equity based on response sentences in customer reviews.
Traditionally, the proper answer to the question of brand loyalty (brand loyalty is a
dimension of brand equity), ‘Will you recommend this product to others?’ involves
selecting a score from 1 to 7 on a Likert s cale. Alternatively, if  an author leaves a
comment, ‘I will recommend this product to others’; this comment can serve as an
alternative answer to the previous question,  i.e., ‘Will you recommend this product to
others?’ Although the survey method is still used to measure individual perception, it is
challenging for researchers to apply it to millions of people with limited time. In addition,
it is difficult to track changes in brand e quity over time. By quantifying response
sentences, our approach partially overcomes the survey-based approach’s challenges
while maintaining its basic framework.
Subsequently, the next question is, ‘How do we identify a response sentence among
multiple sentences?’ A response sentence is ch aracterised as containing a key phrase. In
the previous example, ‘recommend to others’ is the key seed phrase that distinguishes a
response from other general opinions. In addition to ‘recommend to others’, many other
key seed phrases can be extracted from previous survey items. Using these phrases, we
constructed a regular pattern for identifying a response sentence. After quantifying
response sentences using these phrase patterns, we calculated a brand equity score based
on the scoring process.
3.1 Extracting key seed phrase patterns of brand equity
In this initial stage, we extracted key seed phrase patterns from prior brand equity survey
questionnaires. These patterns play a significant role in identifying sentences that respond
to the items in brand equity questionnaire s. To extract these key phrases, we first
reviewed previous brand equity studies that utilised brand equity survey items. Second,
we selected common brand equity dimensi ons from multiple brand equity constructs.
Third, we manually extracted the key phrases from the survey items for each brand equity
dimension.
3.1.1 Extracting key seed phrases
Among the diverse brand equity dimensions, we identified the commonly recognised
dimensions and derived key seed phrases from the survey items employed to measure
these selected dimensions. Previous studies have suggested various brand equity models
(Aaker, 1996; Yoo and Donthu, 2001; Farjam and Hongyi, 2015), and each model is
based on a different perspective of the dimensions that comprise brand equity. We
reviewed these brand equity models and selected four dimensions commonly adopted in
several research studies: brand awarene ss, brand loyalty, perceived quality, and
satisfaction. Similarly, we adopted survey items frequently used to measure each brand
equity dimension as a source of key phrases. Each survey item that measures a brand
equity dimension has a distinctive phrase th at characterises a general sentence as a
response sentence. For example, sentences  containing phrases such as ‘highly
recommendable’, ‘buy again’, ‘refund’, and ‘money back’ are likely to be response
sentences to brand loyalty questions. We manually extracted these key seed phrases from
each of the survey items used to measure the four brand equity dimensions.

   28 J. Yeom et al.

3.1.2 Dealing with reverse-coded survey items
This step expands the key seed phrases by adding the antonyms and negation forms of
these phrases to deal with reverse-coded survey items. Reverse coding is a common
validation technique for survey items and involves negatively rephrasing a positive
survey item. For example, when measuring retirement confidence, we asked respondents
to indicate the extent to which they agreed  with the statement ‘H ow confident are you
that you will be able to live comfortably in  retirement?’ and ‘How worried are you about
being able to make ends meet in retiremen t?’ The forms of both these questions are
different but convey the same meaning. In this way, reverse-coded questionnaires help to
confirm the consistency of responses.
Adding antonyms and negation forms can identify response sentences that include
negative perceptions of brands. In survey practice, a typical method for brand equity
questionnaires is asking positive questions. To express their negative perceptions toward
brand equity, respondents usually select a score ranging from 1 to 3 on a seven-Likert
scale for positive questions. However, customer reviews should include direct mentions
of negative terms or phrases to express the customers’ negative perceptions. Since key
seed phrases from positive ques tionnaires tend to all be in the positive form, it is less
efficient to find negative mentions only with  these initial seed phrases. To identify a
response sentence that expresses a negativ e perception toward brand equity, it is
necessary to consider antonyms and negation forms along with the key phrases extracted
from the preceding step.
One of the most crucial factors in recogn ising a response sentence is whether the
corresponding sentence includes a key seed phrase. Therefore, the more key seed phrases
are included in the key phrase set, the more likely the proposed approach will identify
various response sentences. In the above example, including the key seed phrase ‘worried
about’ helps us identify that ‘I’m worried about being able to make ends meet in
retirement’ as a response sentence among the various sentences in the customer review.
Therefore, extracting key seed phrases from reverse-coded survey items is necessary to
identify as many response sentences as possible from customer reviews.
3.1.3 Enriching key seed phrases
Based on the key seed phrases obtained in the preceding step, we expand the key phrases
set by adding synonyms and extended forms of expression. These key seed phrases are
revised versions of original key seed phrases with diverse forms but similar meanings.
The purpose of enriching key seed phrases is to identify the various types of response
sentences. For instance, responses to the qu estion ‘Are you willing to buy this product
again?’ would differ from customer to customer . We can find ‘I want to repurchase it
next time’ as well as ‘I will buy it again next  time’ as response se ntences from customer
reviews. With the key phrase, ‘buy again’ al one, it is difficult to identify ‘I want to
repurchase it next time’ as a response sentence. To capture both types of response
sentences, we should enrich the key seed phrases by adding synonyms and similar
expressions.
Enriched key seed phrases are utilised as the features of each brand equity dimension.
These extended phrases play an essential role in capturing the characteristics of response
sentences corresponding to each brand equity dimension.

    Assessing brand equity through customer reviews 29

Table 2 The phrase-dimension matrix converted from survey questions

Survey questionnaire/key phrase Be satisfied I would switch Consistent in the quality High reputation … Exceeded my expectations Right thing to buy The first choice Brand equity dimensions
In general, I am satisfied with this product 1 0 0 0 … 0 0 0 Satisfaction
I try to use this product every time I need it 0 0 0 0 … 0 0 0 Loyalty
The quality of this product is extremely high 0 0 0 0 … 0 0 0 Perceived
quality
Doubt that I would switch 0 1 0 0 … 0 0 0 Loyalty
This product is consistent in the quality it
offers
0 0 1 0 … 0 0 0 Perceived
quality
This product is the first choice that I need it 0 0 0 0 … 0 0 1 Loyalty
I am familiar with this product 0 0 0 0 … 0 0 0 Awareness
… … … … … … … … … …
I am sure that it was rig ht thing  to buy this
product
0 0 0 0 … 0 1 0 Satisfaction
This product has high reputation 0 0 0 1 … 0 0 0 Awareness
I consider myself to be loyal to this product 0 0 0 0 … 0 0 0 Loyalty
I recommend this product to other people 0 0 0 0 … 0 0 0 Loyalty
This product has exceeded my highest
expectations
0 0 0 0 … 1 0 0 Satisfaction
Intend to continue using 0 0 0 0 … 0 0 0 Loyalty

   30 J. Yeom et al.

3.2 Identifying response sentences
This substage identifies response sentence s by learning the key seed phrase patterns
extracted in the preceding stages. The subsequent steps are as follows:
1 pre-processing customer review s in machine-readable format
2 constructing a phrase-dimension matrix based on the key seed phrase patterns
3 detecting response sentences using a naïve-Bayes classifier.
3.2.1 Pre-processing customer reviews
This step entails pre-processing the customer reviews dataset obtained from the online
e-commerce platform, expressed in natural language. The pre-processing involves
removing noise reviews, (e.g., duplicated customer reviews and non-English reviews that
fall outside the scope of our research) and sp litting customer reviews into sentence-level.
Since the proposed approach aims to identify response sentences, paragraph-level
reviews should be tokenised by the sentence-level. After tokenising the reviews, we
eliminated noise characters that were less appropriate as sentence features.
3.2.2 Construction of phr ase-dimension matrix
This step constructs a phrase-dimension matrix using the key seed phrases obtained in the
preceding step and the brand equity dimensions. We built this phrase-dimension matrix
since it fundamentally represents machine- learnable sentences. Table 2 presents the
phrase-dimension matrix developed from the survey questions. The matrix serves as the
training data in our approach. In this study , the phrase-dimension matrix comprises two
parts:
1 the contents of sentences repres ented as key seed phrase vectors
2 the brand equity dimensions that comprise four categories.
First, the contents of a sentence are represen ted as the phrase vectors of an individual
sentence with several key seed phrases in the sentence. Here, these phrases become an
essential feature distinguishing a general sent ence as a response sentence for each brand
equity dimension. Second, the brand equity dimensions comprise four distinct categories:
brand awareness, brand loyalty, perceived quality, and satisfaction. Each category
distinguishes which response sentences are included under each dimension.
3.2.3 Detecting response sentence using naïve-Bayes classifier
This step classifies the input sentences into five classes: brand awareness, brand loyalty,
perceived quality, satisfaction, and neutral. To do so, we employed a naïve Bayes
classification model, a popular machine learning algorithm (Devroye et al., 2013).
The naïve Bayes classification model has been adopted widely in numerous fields
(Bermejo et al., 2014; Zhang and Liang, 2 016; Li et al., 2019). This technique was
introduced in the 1950s and has been applied to solve various classification problems
such as document categorisation and spam filtering (Yan and Liu, 2011). At the heart of
the naïve Bayes model is Bayes’ rule, which is based on conditional probability.
Equation (1) presents the primary form of a naïve Bayes classifier.

    Assessing brand equity through customer reviews 31

() (){1,..., } 1 ˆ arg max
n
kK k i k i y pC pxC∈ = = ∏  (1)
In equation (1), ˆy  denotes the class label, k denotes the number of classes, Ck represents
class K, xi is one element in vector space X, and i is the number of f eatures that vector X
has.
The naïve Bayes classification model has been used in its various extended forms
depending on the nature of the data. Among various naïve Bayes classification models,
we selected the Gaussian naïve Bayes mo del. The Gaussian Naïve-Bayes model is
suitable when the data is continuous. Equation (2) represents the basic form of the
Gaussian naïve Bayes model.
()
22
2
1(| )
2
c
c
v μ
σ
c
px v c e
πσ
−−
==  (2)
In equation (2), x denotes the continuous attribute of training data, μc is the mean of the
values in x associated with Class c, and 2cσ  is the variance of the values in x associated
with Class c. The probability distribution of v given a Class c, p ( x = v| c) can be
computed by plugging v into the equation for a normal distribution parameterised by μc
and 2 .cσ
The benefits of using the naïve Bayes model in the current approach are as follows.
First, since the naïve Bayes model is based on conditional probability, it is suitable for
identifying response sentences from customer reviews based on the presence of the key
seed phrases. Second, the naive Bayes classi fier enables the identification of diverse
response sentences with a limited number of training sets.
To maximise classification performance, we  stacked four binary  classifiers rather
than using a one-shot multi-class classifier. The strengths of employing a stacking
classifier are as follows. First, the classi fier can detect multi-dimensional response
sentences. For example, some sentences c ontain answers to multiple questions that
measure different brand equity dimensions. By identifying these response sentences, the
model can accurately categorise sentences w ith multi-dimensional responses. Secondly,
binary classification yields better performance with a limited training set than a
multi-category classification model. Given that each training set is derived from key seed
phrases extracted from a limited number of survey items, the total size of the training set
is insufficient to support mu lti-category classification. By stacking binary classifiers, the
proposed model can accurately classify the sentences with the constrained size of the
training set.
3.3 Scoring brand equity
This stage quantifies the bran d equity score of each dimens ion based on the response
sentences identified in the previous stage. Measuring the brand equity score involves
three steps:
1 sentence-level scoring
2 individual-level scoring
3 brand-level scoring.

   32 J. Yeom et al.

3.3.1 Sentence-level scoring
We assumed one response sentence could represent positive or negative polarity
regarding one brand equity dimension. Based on the classification results obtained in the
preceding step, we selected sentences that were  classified under one of four brand equity
dimensions: brand awareness,  brand loyalty, perceived quality, and satisfaction. We
considered these sentences as response sentences. By checking
1 whether the response sentence contained a negation form in front of key phrases
2 whether the response sentence contained antonyms of key seed phrases; we assigned
a score of –1 to the response sentences.
We allocated a score of +1 to the remai nder of the response sentences. For neutral
sentences, we allocated a score of 0. Among the response sentences, we assigned scores
of +2 and –2 to response sentences containing adverbs and adjectives in consideration of
their strength of expression. Consequently, we scored each brand equity dimension at the
sentence level by assigning scores of +2, +1, 0, –1 and –2 to one of the four dimensions
in one sentence.
There were some exceptional cases where we scored multiple dimensions in one
sentence. If a sentence’s structure was a parallel structure connected by ‘and’ or ‘or’, two
response sentences for different dimensions appeared in one sentence. For example, for a
sentence, ‘The quality of this product is pe rfect, and I will recommend it to others’, the
classifier tags it under the dimensions of perceived quality and brand loyalty. We
allocated a score of +1 to both dimensions for this sentence.
3.3.2 Individual-level scoring
The individual-level scoring begins with aggregating each dimension’s score allocated to
each sentence in the preceding step. By adding up the sentence-level score, we can
1 measure the individual level of brand equity
2 imitate the way of measuring the strength  of brand equity in existing surveys.
The typical way of measuring the strength of each brand equity dimension is to ask
survey participants to select a score on a Likert scale. Participants select extreme numbers
within the range of 1 to 7 when they have a strong attitude toward a question. Our
approach utilises the total score for each br and equity dimension as a proxy for how
strongly people responded to a given question. For example, a review that scored +2 on
brand loyalty is more likely to represent stronger perceptions of brand loyalty questions
than a review that scored +1 on brand loya lty. As shown in Figure 2, aggregating the
scores of each brand equity dimension is essential for measuring individual-level brand
equity.
3.3.3 Brand-level scoring
By accumulating the individual-l evel brand equity scores from the preceding step, we
obtained a brand-level brand equity score, which was used to compare the relative
positions of multiple brands.
Accumulating individual brand equity scores has two advantages that complement the
conventional survey-based measurement approa ch. First, since only the actual customer

    Assessing brand equity through customer reviews 33

can leave customer reviews, we can obtain an actual aggregated brand equity score.
Second, we can track changes in aggregated brand equity scores in real-time.
After accumulating the individual-level bran d equity scores into the brand-level
score, we normalised the brand-level score using the number of reviews for each brand.
Since the number of reviews in a brand exaggerates or reduces the overall brand equity
score, the accumulated brand equity scores need to be normalised.
Figure 2 Aggregating sentence-level brand equity  score (see online version for colours)

3.4 Validation
Since our approach is the first attempt to measure the brand equity score based on
customer reviews using a naïve Bayes classifier, no existing index is comparable to ours.
Although there are several commercial brand equity scores, such as Brand-Z and BAV, it
is not easy to compare our brand equity scor e with these commercial scores due to the
different units of measurement used (Zaichkowsky et al., 2010). Instead, we validated our
approach by replicating path analysis from prior studies. The advantages of using linear
regressions are twofold. First, we can reconfirm the relationship between brand equity
concepts by testing the consistency of our resu lts with the results of previous studies.
Second, we can check the future applicability of our approach to brand equity studies.
4 Results
4.1 Data
We adopted a customer review dataset introduc ed in a previous study (McAuley et al.,
2015). This dataset contains product reviews and metadata from an online e-commerce
platform, including 142.8 million reviews from May 1996 to July 2014. Specifically, the
customer reviews from this dataset include reviewer ID, ASIN number (product ID),
reviewer name, review text, review time, an d overall score as me ta information. The
reason for using this dataset is two-fold:

   34 J. Yeom et al.

1 the products available on this online e-commerce platform encompass several
categories, allowing us to test our model across a variety of brand settings
2 the dataset offers an adequate number of reviews for each product, which is crucial
for developing a brand equity metric.
Among the numerous product categories, we se lected the vacuum cleaner category. We
extracted customer reviews for the top six v acuum cleaner brands based on their market
shares as of 2016.
Table 3 Data description (vacuum cleaner industry)
Brand (coded name) # of products # of reviews # of sentences
DS 37 8,816 70,916
BL 55 10,820 66,068
DD 53 8,608 46,159
HV 45 20,448 136,566
SH 23 3,735 26,631
EU 46 12,630 73,612
Table 3 presents detailed information about each brand and its customer reviews.
We selected vacuum cleaner brands as our experimental focus for the following
reasons: First, the vacuum cleaner market has sufficient brands for competition, allowing
the comparison of numerous brands’ brand equity scores. Second, since multiple products
tend to exist under a vacuum cleaner brand, measuring whic h product contributes to the
overall brand equity score and which product diminishes the overall score is possible.
Table 4 Seed key seed phrase of ea ch brand equity dimensions
Brand equity dimensions Prior studies Seed phrase sets
Brand awareness Aaker (1996) Heard of, stand for, think of,
come to mind, aware of,
recognise Yoo and Donthu (2001)
Mishra et al. (2011)
Brand loyalty Aaker (1996) Buy again, best choice, loyal
patron, committed to, willing to
pay Yoo and Donthu (2001)
Mishra et al. (2011)
Perceived quality Aaker (1996) Hi gh quality, consistent quality,
good quality, poor quality Yoo and Donthu (2001)
Mishra et al. (2011)
Satisfaction Aaker (1996) Satisfied with, exceed
expectations, right thing to do,
delighted with, what I need Nam et al. (2011)
4.2 Extracting brand equity phrase patterns
We extracted key seed phrase patterns from previous brand equity survey questionnaires
(Yoo and Donthu, 2001; Mishra et al., 2011). We manually extracted four different seed
phrase patterns composed of 4–6 phrases. The extracted seed phrase sets are presented in

    Assessing brand equity through customer reviews 35

Table 4. Consequently, we extracted 20 phrase patterns from previous brand equity
questionnaires.
We expanded the size of these phrase patterns by employing synonyms, antonyms,
and negation forms. These patterns distinguish response sentences from ordinary
sentences. Finally, we obtained 101 phrase patterns from the conventional survey
measurement. Table 5 represents the finalised key phrase patterns.
Table 5 Enriched key seed phrases
Brand equity
dimensions
Seed phrase
patterns Synonyms Related forms/antonyms Negation forms
Brand
awareness
Heard of Thought of Familiar with Do not + patterns
Stand for Recognised Well known Does not + patterns
Think of Stands for Vi sible Did not +patterns
Come to mind Have recognised Heard a lot Not + patterns
Aware of Have heard of Famous Never + patterns
Recognise Notorious
Unfamiliar with
Brand
loyalty
Buy again Bought again Purchase again Do not + patterns
Best choice Willing to pay Tr ustworthy Does not + patterns
Loyal patron Will buy again T humbs up Did not +patterns
Committed to Will purchase
again
Paid full price Not + patterns
Worth it Never + patterns
Perceived
brand quality
High quality Great Work well Do not + patterns
Consistent
quality
Incredible Performed well Does not + patterns
Good quality Amazing Poor quality Did not +patterns
Superb Inconsistent Not + patterns
Best Quality Never + patterns
Satisfaction Satisfied with Satisfying Perfect Do not + patterns
Exceed
expectations
Exceed
standards
Cool Does not + patterns
Right thing to
do
Satisfaction Awesome Did not +patterns
Delighted with Expectation I like Not + patterns
What I needed I love Never + patterns
Looking for
What I look for
4.3 Identifying response sentences via machine learning technique
We utilised 65,057 customer reviews to m easure brand equity. The Python natural
language toolkit (NLTK) package is used to construct the phrase-dimension matrix. First,
we split the reviews at the sentence level af ter eliminating any noise characters. Second,

   36 J. Yeom et al.

we vectorised each sentence using key phrase patterns obtained in the preceding stages. A
total of 101 key phrases became a feature of the input vectors.
We adopted Python’s scikit-learn package to identify response sentences using the
Gaussian naïve Bayes classifier. We utilised four stacked naïve Bayes classifiers to
determine whether each sentence is a response sentence and to which dimension the
sentence belongs. We identified that a total of 85,709 out of the 419,952 sentences were
response sentences, which are possible answers to brand equity questions.
4.4 Measuring brand equity  through scoring processes
We quantified brand equity through a scoring process. First, we allocated a brand equity
score for each sentence based on which categ ories the sentence belonged to. Second, we
aggregated the sentence-level brand equity scores and converted them into individual-
level scores. Third, we aggregated the individua l-level scores to the brand-level scores to
identify which brands had a higher position based on the customers’ perceptions. Finally,
we normalised each brand equity score by dividing the number of reviews for each brand.
To present the results, we measured the 2 014 brand equity score of vacuum cleaner
brands, as shown in Table 6. Each brand had a brand equity score in each dimension.
Table 6 Brand equity score of each vacuum cleaner brand in 2014
Brand (coded-name) Brand awareness Brand lo yalty Perceived qual ity Satisfaction
DS 0.018 0.121 0.786 0.596
BL 0.003 0.174 1.017 0.528
DD 0.004 0.125 0.916 0.514
HV 0.006 0.140 0.698 0.520
SH 0.004 0.171 0.984 0.534
EU 0.004 0.133 0.673 0.509
4.5 Validation
To validate our proposed approach, we ex amined four studies that confirmed the
relationship between brand equity dimensions (Bloemer et al., 1998; Olsen, 2002; Yang
and Peterson, 2004; Nam et al., 2011). Th e reasons for employing these studies are
twofold:
1 for robustness, the research models in these studies confirm the direction between
brand equity dimensions in a different industry
2 they include as many dimensions as po ssible to demonstrate the dynamics among
each brand equity dimension.
Consequently, our regression model tested th e relationships between perceived quality,
customer satisfaction, and brand loyalty, which were widely tested in previous studies.
Since previous studies have illuminated the mediating role of customer satisfaction on
the effect of perceived quality on brand loyalty , we tested the mediating role of customer
satisfaction. To test the research model, we eliminated individual-level observations that
scored zero under each brand equity dimension. The reason for removing zero-scored
observations is that the extreme inclusion of zero observation dilutes the statistical

    Assessing brand equity through customer reviews 37

significance among brand equity dimensions. We obtained 3,492 samples from the
elimination process. To present the results of the validation model for the latest year
2014, we utilised 672 out of 3,492 samples.
We conducted a linear regression to conf irm the dynamics among the various brand
equity dimensions. Table 7 presents the descriptive statistics among brand equity
variables. Since the variables, i.e., percei ved quality, customer satisfaction, and loyalty
are correlated, we checked for multicollinearity by calculating the variance inflation
factors (VIF). Our models exhibited no multicollinearity problem since the variance
inflation factors were all less than 10.
Table 7 Descriptive statistics of variables
 Perceived quality Sa tisfaction Loyalty
1 Perceived quality 1.00
2 Satisfaction 0.23** 1.000
3 Loyalty 0.13** 0.08** 1.00
Mean 1.56 1.49 0.71
SD 1.20 1.08 0.98
 3,491 3,491 3,491
Note: **Correlation is significant at the 0.01 level (two-tailed).
Table 8 The result of the regression analysis

Dependent variables:
Customer satisfaction Loyalty
(1) (2) (3) (4)
Perceived quality 0.202***  0.107*** 0.097**
Customer satisfaction  0.073***  0.049***
Constant 1.174*** 0.597*** 0.539*** 0.481***
Observations 3,491 3,491 3,491 3,491
R-square 0.050 0.006 0.017 0.020
Adjusted R-square 0.050 0.006 0.017 0.019
F Statistic 186.64*** 23.353*** 61.908*** 36.063***
Note: *p < 0.1; **p < 0.05; ***p < 0.01.
Consistent with past research, our approach reconfirmed the correlations among brand
equity dimensions proved by prior studies (Bei and Chiao, 2001; Olsen, 2002). As shown
in Table 8, our regression analysis confirms the positive relationship between
1 perceived quality and satisfaction
2 satisfaction and brand loyalty.
This result indicates that customer satisfacti on is partially mediated by the effect of
perceived quality on brand loyalty. We also confirmed our regression models using the
Baron and Kenny validation process and the Sobe l test to validate this partial mediation
effect. These consistent regression results may guarantee that this approach is worthwhile
for measuring brand equity when traditional methods are unavailable. A key advantage of

   38 J. Yeom et al.

our approach is that it can be used to measure brand equity dimensions repeatedly over
time with much larger samples.
5 Conclusions
5.1 Contributions
This study proposed a machine-learning approach to measure brand equity based on
customer reviews. We employed traditional brand-equity questionnaires to extract key
phrases vital to distinguishing response sentences from ordinary sentences. Additionally,
we enriched key seed phrase patterns using reversely coded questions and constructed a
phrase dimension matrix to learn Gaussian naïve Bayes classifiers. Furthermore, we
measured both brand and individual-level brand equity by aggregating and normalising a
sentence-level brand equity score. Integrating these methods overcomes the limitations of
conventional survey-based brand equity measurements by providing a consistent way of
quantifying measures that can evaluate bran d equity in real time, reflecting immediate
customer feedback. The case of the vacuum cl eaner industry verifies that our proposed
approach complements the conventional brand-equity measurement approach. Despite its
methodological usefulness and convenience, the conventional survey-based approach’s
limitations, such as the lack of validation t ools, limited ability to verify the accuracy of
brand equity scores, and absence of expression intensity, still need to be addressed.
This study has unique contributions in the following aspects. First, from an academic
perspective, our brand equity measurement approach, which utilises customer reviews,
complements the conventional survey-based approach to ensure consistency of the results
and the reliability of the measuring process.  In previous studies, researchers faced
challenges in conducting empirical analysis, such as events or comparative studies, due to
the time and costs involved in using conven tional measurement. Moreover, researchers
faced challenges in determining the impact  of brand equity changes. Our proposed
approach is expected to provide a possible solution for examining the relationships
among various brand-equity-related constructs  without the constraints of excessive cost.
Second, from a practical standpoint, we expect our approach to provide a useful index for
tracing customers’ overall responses to products, especially in a rapidly changing market
situation. Although some firms provide co mmercial brand equity indexes, they are
measured in long-term intervals (semi-annu ally or quarterly), making it difficult for
marketing practitioners to adopt these tools in their decision-making processes or
marketing plans.
5.2 Limitations
Despite the usefulness of the proposed approach, our work has some limitations. First,
while the suggested measurement method is useful for scoring brand equity dimensions,
it does not grasp the relationships among them. Therefore, it is still challenging to
compare the score of each brand equity dimension within a brand. This can be attributed
to how customers write when they leave their reviews. For example, customers may have
a high perceived ‘brand awareness’ even if they  do not directly state that they have heard
of or are aware of a brand. In other words, the fact that customers do not respond to brand
awareness questionnaires does not guarant ee they have a low perception of brand

    Assessing brand equity through customer reviews 39

awareness. In the conventional  survey-based approach, we do not have to worry about
this issue because survey participants are as ked to reply to every questionnaire related to
each brand equity dimension. Since our ap proach measures brand equity based on
voluntary response sentences included in customer reviews, not every question is
answered by one single customer.
Second, the accuracy of the brand equity sc ore must be confirmed. Since there is no
direct benchmark index to compare the brand equity score generated by our approach, it
is necessary to examine how accurately our approach measures brand equity.
Finally, diverse adjectives and adverbs should be included when considering the
strength of expressions. The proposed approach consists of five levels of expression
intensity. The principle of assigning each level is to allocate a higher score to response
sentences that have adverbs and adjectives in front of verb clau ses. Each response
sentence is assigned a score of either –2, –1, 0, 1, or 2 for each brand equity dimension. If
some new adverbs or adjectives emphasise the original expression but are not included in
the original set, the response sentence would not precisely represent the intensity of the
key expression. Thus, future research should develop a systematic way of including
diverse adjectives and adverbs.
5.3 Future research directions
Apart from resolving methodological limitations, our future research avenue is
intertwined with considering diverse types of customer review platforms that reflect
detailed customer intention, motivation, and behaviour. Recent studies are gradually
attempting to explore various contexts or situations through in-depth elaboration of
review content (Choi et al., 2022; Qahri-Sare mi and Montazemi, 2023; Yu et al., 2023a).
We plan to adjust the brand equity score to  reflect customers’ co ntext, allowing more
accurate product and brand comparisons. In line with recent literature, it is necessary to
study how the brand equity score affects organisational and corporate activities, such as
decision-making timing and sales performan ce, including empirical case studies in
multiple domains (Ren et al., 2023; Yin et al., 2023).
References
Aaker, D.A. (1996) ‘Measuring brand equity across products and markets’, California Management
Review, Vol. 38, No. 3, pp.102–120.
Ailawadi, K.L., Lehmann, D.R. and Neslin, S.A. (2003) ‘Revenue premium as an outcome measure
of brand equity’, Journal of Marketing, Vol. 67, No. 4, pp.1–17.
Atilgan, E., Aksoy, Ş. and Akinci, S. (2005) ‘Determinants of the brand equity’, Marketing
Intelligence and Planning, Vol. 23, No. 3, pp.237–248.
Bagheri, A., Saraee, M. and Jong,  F.D. (2013) ‘Care more a bout customers: unsupervised
domain-independent aspect detection for sentiment analysis of customer reviews’, Knowledge-
Based Systems, Vol. 52, pp.201–213.
Batrinca, B. and Treleaven, P.C. (2015) ‘Social me dia analytics: a survey of techniques, tools and
platforms’, AI and Society, Vol. 30, No. 1, pp.89–116.
Bei, L-T. and Chiao, Y-C. (2001) ‘An integrat ed model for the effects of perceived product,
perceived service quality, and perceived price fairness on consumer satisfaction and loyalty’,
The Journal of Consumer Satisfaction,  Dissatisfaction and Complaining Behavior , Vol. 14,
pp.125–140.

   40 J. Yeom et al.

Berger-Remy, F. and Michel, G. (2015) ‘How brand gives employees meaning: Towards an
extended view of brand equity’, Recherche et Applications en  Marketing (English Edition) ,
Vol. 30, No. 2, pp.30–54.
Bermejo, P., Gámez, J.A. and Puerta, J.M. (2014) ‘Speeding up incremental wrapper feature subset
selection with naive Bayes classifier’, Knowledge-Based Systems, Vol. 55, pp.140–147.
Bloemer, J., Ruyter, K.D. and Peeters, P. (1998) ‘Investigating drivers of bank loyalty: the complex
relationship between image, service quality and satisfaction’, International Journal of Bank
Marketing, Vol. 16, No. 7, pp.276–286.
Bravo Gil, R., Fraj Andrés, E. and Martínez Salinas, E. (2007) ‘Fam ily as a source of
consumer‐based brand equity’, Journal of Product and Brand Management , Vol. 16, No. 3,
pp.188–199.
Chakraborty, U. and Bhat, S. (2018) ‘The effects of credible online reviews on brand equity
dimensions and its conseque nce on consumer behavior’, Journal of Promotion Management ,
Vol. 24, No. 1, pp.57–82.
Chakraborty, U. and Biswal, S.K. (2020) ‘Impact of online reviews on consumer’s hotel booking
intentions: does brand image mediate?’, Journal of Promotion Management , Vol. 26, No. 7,
pp.943–963.
Choi, H.B.S., Oh, W., Kwak, C., Lee, J. and L ee, H. (2022) ‘Effects of online crowds on self-
disclosure behaviors in online reviews: a multidimensional examination’, Journal of
Management Information Systems, Vol. 39, No. 1, pp.218–246.
Cobb-Walgren, C.J., Ruble, C.A. and Donthu, N.  (1995) ‘Brand equity, brand preference, and
purchase intent’, Journal of Advertising, Vol. 24, No. 3, pp.25–40.
Deng, C. and Ravichandran, T. (2023) ‘Manageria l response to online positive reviews: helpful or
harmful?’, Information Systems Research, Vol. 35, No. 4, pp.1802–1823.
Devroye, L., Györfi, L. and Lugosi, G. (2013) A Probabilistic Theory of  Pattern Recognition ,
Springer, New York.
Du, H.S., Xu, J., Tang, H. and Ji ang, R. (2022) ‘Repurchase intention in online knowledge service:
the brand awareness perspective’, Journal of Computer Information Systems, Vol. 62, No. 1,
pp.174–185.
Elwalda, A., Lü, K. and Ali, M. (2016) ‘Perceived  derived attributes of online customer reviews’,
Computers in Human Behavior, Vol. 56, pp.306–319.
Farjam, S. and Hongyi, X. (2015) ‘Reviewing the concept of brand equity and evaluating
consumer-based brand equity (CBBE) models’, International Journal of Management Science
and Business Administration, Vol. 1, No. 8, pp.14–29.
Farris, P.W., Bendle, N., Pfeifer,  P.E. and Reibstein, D. (2010) Marketing Metrics: The Definitive
Guide to Measuring Marketing Performance, Pearson Education, London, UK.
Ho-Dac, N.N., Carson, S.J. and Moore, W.L. (2013) ‘The effect s of positive and negative online
customer reviews: do brand strength and category maturity matter?’, Journal of Marketing ,
Vol. 77, No. 6, pp.37–53.
Hoeffler, S. and Keller, K.L. (2002) ‘Building br and equity through corporate societal marketing’,
Journal of Public Policy and Marketing, Vol. 21, No. 1, pp.78–89.
Keller, K.L. (2003) ‘Brand synthesis: the multidimensionality of brand knowledge’, Journal of
Consumer Research, Vol. 29, No. 4, pp.595–600.
Kim, H. and Kim, W.G. (2005) ‘T he relationship between brand equ ity and firms’ performance in
luxury hotels and chain restaurants’, Tourism Management, Vol. 26, No. 4, pp.549–560.
King, C. and Grace, D. (2009) ‘Employee based brand equity: a third perspective’, Services
Marketing Quarterly, Vol. 30, No. 2, pp.122–147.
King, C. and Grace, D. (2010) ‘Building and measuring employee ‐based brand equity’, European
Journal of Marketing, Vol. 44, Nos. 7/8, pp.938–971.
King, C., Grace, D. and Funk,  D.C. (2012) ‘Employee brand equity: scale development and
validation’, Journal of Brand Management, Vol. 19, No. 4, pp.268–288.

    Assessing brand equity through customer reviews 41

Knox, S. and Walker, D. (2001) ‘Meas uring and managing brand loyalty’, Journal of Strategic
Marketing, Vol. 9, No. 2, pp.111–128.
Kostyra, D.S., Reiner, J., Natter, M. and Klappe r, D. (2016) ‘Decomposing the effects of online
customer reviews on brand, pr ice, and product attributes’, International Journal of Research
in Marketing, Vol. 33, No. 1, pp.11–26.
Leuthesser, L., Kohli, C.S. an d Harich, K.R. (1995) ‘Brand equ ity: the halo effect measure’,
European Journal of Marketing, Vol. 29, No. 4, pp.57–66.
Li, L., Zhang, Y., Chen, W., Bose, S.K., Zukerman, M. and Shen, G. (2019) ‘Naïve Bayes
classifier-assisted least loaded routing for circuit-switched networks’, IEEE Access , Vol. 7,
pp.11854–11867.
McAuley, J., Targett, C., Shi, Q. and Van de n Hengel, A. (2015) ‘Image-based recommendations
on styles and substitutes’, Proceedings of the 38th Inter national ACM SIGIR Conference on
Research and Development in  Information Retrieval , pp.43–52, Association for Computing
Machinery, New York, NY, USA.
Mishra, P., Datta, B. and Gupta,  V. (2011) ‘Perpetual asset mana gement of customer-based brand
equity – the PAM evaluator’, Current Research Journal of Social Sciences , Vol. 3, No. 1,
pp.34–43.
Mizik, N. (2014) ‘Assessing the tota l financial performance  impact of brand equity with limited
time-series data’, Journal of Marketing Research, Vol. 51, No. 6, pp.691–706.
Mudambi, S.M. and Schuff, D. (2010) ‘Researc h note: what makes a helpful online review? A
study of customer reviews on Amazon.com’, MIS Quarterly, Vol. 34, No. 1, pp.185–200.
Nam, J., Ekinci, Y. and Whyatt, G. (2011) ‘Brand equity, brand loyalty and consumer satisfaction’,
Annals of Tourism Research, Vol. 38, No. 3, pp.1009–1030.
Oliveira, M.O.R., de Silveira, C.S. and Luce, F.B. (2015) ‘Brand equity estimation model’, Journal
of Business Research, Vol. 68, No. 12, pp.2560–2568.
Olsen, S.O. (2002) ‘Comparative evaluation and the relationship between quality, satisfaction, and
repurchase loyalty’, Journal of the Academy of Marketing Science , Vol. 30, No. 3,
pp.240–249.
Pappu, R., Quester, P.G. and Cooksey, R.W. (2005) ‘Consumer ‐based brand equity: improving the
measurement – empirical evidence’, Journal of Product and Brand Management , Vol. 14,
No. 3, pp.143–154.
Park, C.S. and Srinivasan, V. (1994) ‘A survey -based method for measuring and understanding
brand equity and its extendibility’, Journal of Marketing Research , Vol. 31, No. 2,
pp.271–288.
Qahri-Saremi, H. and Montazemi, A.R. (2023) ‘Negativity bias in the diagnosticity of online
review content: the effects of consumers’  prior experience and need for cognition’, European
Journal of Information Systems, Vol. 32, No. 4, pp.717–734.
Ren, F., Tan, Y. and Wan, F. (2023) ‘Know y our firm: managing social  media engagement to
improve firm sales performance’, MIS Quarterly, Vol. 47, No. 1, pp.227–262.
Sashi, C.M. (2012) ‘Customer engagement, buyer ‐seller relationships, and social media’,
Management Decision, Vol. 50, No. 2, pp.253–272.
Shankar, V., Azar, P. and Fuller, M. (2008) ‘BR AN*EQT: a multicategory brand equity model and
its application at Allstate’, Marketing Science, Vol. 27, No. 4, pp.567–584.
Simon, C.J. and Sullivan, M.W. (1993) ‘The meas urement and determinants of brand equity: a
financial approach’, Marketing Science, Vol. 12, No. 1, pp.28–52.
Teng, S., Khong, K.W., Chong, A.Y- L. and Lin, B. (2017) ‘Examin ing the impacts of electronic
word-of-mouth message on consumers’ attitude’, Journal of Computer Information Systems ,
Vol. 57, No. 3, pp.238–251.
Wang, Y., Tariq, S. and Alvi, T.H. (2021) ‘H ow primary and supplementary reviews affect
consumer decision making? Roles of psyc hological and manage rial mechanisms’, Electronic
Commerce Research and Applications, Vol. 46, p.101032.

   42 J. Yeom et al.

Xia, H., Pan, X., An, W. and Zhang, Z. (2021) ‘Can online rating reflect authentic customer
purchase feelings? Understanding how customer dissatisfaction relates to negative reviews’,
Journal of Computer Information Systems, Vol. 61, No. 4, pp.314–327.
Yagci, I.A. and Das, S. (2018) ‘Measuring desi gn-level information quality in online reviews’,
Electronic Commerce Research and Applications, Vol. 30, pp.102–110.
Yan, H-B. and Liu, Y-S. (2011) ‘Spam fi lter based on incremental Bayes arithmetic’, 2011
International Conference on Electrical and Control Engineering, pp.6111–6114.
Yang, Y. and Subramanyam, R. (2023) ‘Extracting actionable insights from text data: a stable topic
model approach’, MIS Quarterly, Vol. 47, No. 3, pp.923–954.
Yang, Z. and Peterson, R.T. (2004) ‘Customer perceived value, satisfaction, and loyalty: the role of
switching costs’, Psychology and Marketing, Vol. 21, No. 10, pp.799–822.
Yin, D., Vreede, T.D., Steele, L. M. and Vreede, G.J.D. (2023) ‘Deci de now or later: making sense
of incoherence across online reviews’, Information Systems Research , Vol. 34, No. 3,
pp.1211–1227.
Yoo, B. and Donthu, N. (2001) ‘Developing an d validating a multidimensional consumer-based
brand equity scale’, Journal of Business Research, Vol. 52, No. 1, pp.1–14.
Yu, Y., Khern-am-nuai, W., Pinsonneault, A. and Wei,  Z. (2023a) ‘Impacts of social interactions
and peer evaluations on online review platforms’, Journal of Management Information
Systems, Vol. 40, No. 4, pp.1271–1300.
Yu, Y., Yang, Y., Huang, J. and Tan, Y. (2023b) ‘Unifying algorithmic and theoretical
perspectives: Emotions in online reviews and sales’, MIS Quarterly , Vol. 47, No. 1,
pp.127–160.
Zaichkowsky, J.L., Parlee, M. and Hill, J. (2010) ‘Managing industrial brand equity: developing
tangible benefits for intangible assets’, Industrial Marketing Management , Vol. 39, No. 5,
pp.776–783.
Zarantonello, L. and Sc hmitt, B.H. (2013) ‘The impact of event marketing on brand equity’,
International Journal of Advertising, Vol. 32, No. 2, pp.255–280.
Zhang, Y. and Liang, J. (2016) ‘A vi sion based method for object recognition’, Proceedings of the
3rd International Conference on Informati on Science and Control Engineering (ICISCE) ,
pp.139–142.
