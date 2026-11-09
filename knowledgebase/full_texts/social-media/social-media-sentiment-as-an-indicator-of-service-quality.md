---
title: Social media sentiment as an indicator of service quality
url: https://doi.org/10.7200/esicm.57.485
category: social-media
subcategory: review
date: 2026-09
venue: ESIC MARKET Economic and Business Journal
authors:
- Mayte García-García
- Alba Adá Lameiras
- Javier de Esteban Curiel
source: openalex-oa
pdf_url: https://revistasinvestigacion.esic.edu/esicmarket/index.php/esicm/article/download/485/978
pages: 23
chars: 60456
fetched_at: '2026-11-08T19:12:49+00:00'
kb_version: 1
---

# Social media sentiment as an indicator of service quality

Esic Market Economics and Business Journal
Vol. 57, n.º 3, September-December 2026, e485
Social media sentiment as an indicator of
service quality
Mayte García-García
Rey Juan Carlos University, Spain
mt.garcia.2022@alumnos.urjc.es
https://orcid.org/0009-0003-6883-3519
Alba Adá-Lameiras*
Rey Juan Carlos University, Spain
alba.ada.lameiras@urjc.es
https://orcid.org/0000-0002-3092-1463
Javier de Esteban Curiel
Rey Juan Carlos University, Spain
javier.deesteban@urjc.es
https://orcid.org/0000-0001-9735-286X
Received: 04-08-2025; Accepted: 12-05-2026; Published: 09-09-2026
Abstract
Objective: The main objective of this study is to examine service quality in Spain’s insur -
ance sector by analysing customer sentiment in social media comments, with a view to
understanding users’ perceptions and emotional assessments of their experiences with
insurance companies.
Methodology: A dataset of 1,953 user comments from X, Facebook and Google Reviews
was compiled using both automated scraping tools and manual collection methods. Insur-
ance companies were selected based on their net promoter scores (NPS), which served as
a criterion for identifying providers with a high level of reported satisfaction. Sentiment
analysis was performed using manual annotations and automated classification with a
Hugging Face model.
Results: The results reveal a predominance of negative sentiment, especially in comments
relating to claims management and customer service. Insurers tended to interact more with
ISSN 0212-1867 / e-ISSN 1989-3574
CC-BY
ESIC University
https://revistasinvestigacion.esic.edu/esicmarket
How to cite:
García-García, M., Adá-Lameiras, A. & de Esteban
Curiel, J. (2026). Social media sentiment as an
indicator of service quality. ESIC Market. Eco-
nomics and Business Journal, 57(3), e485. DOI:
10.7200/esicm.57.485
*Corresponding author: Alba Adá-Lameiras, alba.ada.lameiras@urjc.es

2
Mayte García-García et al.
operational queries than with marketing-related posts. A behaviour pattern was observed
whereby users repeated their complaints when they did not receive a response, while this
tendency decreased when companies responded proactively.
Practical implications: The study highlights the importance of actively managing customer
service on social media as a key strategy for strengthening reputation and perceived service
quality. Failure to respond or interact with user complaints increases negative comments,
underscoring the need for proactive and consistent digital communication protocols in the
insurance sector.
Keywords: sentiment analysis; customer experience; social media; insurance sector; online
reputation
JEL codes: M31; D83; L86
1. Introduction
Service quality was originally conceptualised as the difference between customer
expectations and perceived performance (Parasuraman et al., 1988), as well as the
result of interaction between technical quality and functional quality in service deliv-
ery (Grönroos, 1984). Today, it is a determining factor in customer satisfaction and
loyalty (Elizalde-Elizalde, 2023; Arguello-Lara, 2023), as a positive experience drives
differentiation and long-term competitive advantage (Sheth et al., 2023). Therefore, in
this study, the following aspects are interrelated: service quality, defined as the extent
to which insurers meet expectations (Parasuraman et al., 1988; Grönroos, 1984);
customer experience, referring to emotional and relational aspects (Wirtz & Lovelock,
2021; Sheth et al., 2023); and sentiment analysis, empirically capturing these emotions
in digital contexts (Guerola-Navarro et al., 2024). These three factors form an inte -
grated framework for interpreting users’ expressions about their insurance providers.
In 2023, the insurance sector experienced 0.4% growth in Spain, consolidating
its position as a key player in the national economy, with a contribution of 5.2% to
gross domestic product (GDP) (Dirección General de Seguros y Fondos de Pensiones
[DGSFP], 2024). However, despite its economic weight and growing digitalisation,
there is a research gap surrounding the evaluation of service quality through senti -
ment analysis, a tool that complements traditional metrics by capturing the emo -
tional and attitudinal aspects of customer opinions, providing real-time information
on their satisfaction and perception of the service (Guerola-Navarro et al., 2024).
This analysis helps fill this gap by analysing sentiment in user comments on social
media, with the aim of examining how customers express and emotionally evaluate
their experiences regarding the quality of service offered by insurance companies.
The analysis was carried out using a mixed strategy of manual annotation and
automated classification with a pre-trained Hugging Face model, which ensured the
validity and accuracy of the textual data processing.
Although customer satisfaction and service quality are classic topics in service
marketing (Parasuraman et al., 1988; Grönroos, 1984; Wirtz & Lovelock, 2021),

3
Social media sentiment as an indicator of service quality
there is still little evidence on how these perceptions manifest in digital environments,
especially in the insurance sector. Understanding these expressions is key to improv-
ing service management and corporate reputation. This study addresses this gap
by focusing on user-generated comments as a source of insight into service quality,
customer experience and corporate reputation.
1.1. Literature review: services marketing, sentiment analysis and customer
satisfaction in social media
Services marketing generates value through experiences and emotional per -
ceptions that determine customer satisfaction and loyalty (Pedreschi-Caballero &
Nieto-Lara, 2023). In this context, sentiment analysis allows us to measure users’
emotions and complement traditional service quality metrics (Martin-Domingo et
al., 2019). Therefore, integrating sentiment analysis into service marketing enables a
more accurate assessment of customer satisfaction and improvement of user experi -
ence (Mostafa, 2013; Sharma et al., 2025).
In services marketing, the development of long-term relationships has evolved
towards approaches that incorporate not only functional satisfaction but also an
emotional bond with the brand (Wirtz & Lovelock, 2021; Chinomona & Maziriri,
2017). Services marketing literature has shown that delivering high-quality customer
service enables companies to set themselves apart from competitors, achieve sustain-
able competitive advantages and enhance operational efficiency (Sheth et al., 2023).
This affective perspective, typical of sentiment-based marketing, has been linked to
higher levels of customer loyalty and repurchase intention (Apria & Parahiyanti,
2023). In the financial and insurance sectors, where trust is a key factor, emotional
connection helps strengthen the customer–brand relationship (Levy & Hino, 2016).
Customer service, traditionally seen as an operational function, has taken on a
strategic role within relationship marketing (Rosário & Casaca, 2023). This is espe-
cially relevant in digital environments, where visibility and speed are critical (Amin
et al., 2025). Responsiveness, communicative tone, effective problem-solving and
incident follow-up are valued by users and determine their overall perception of the
company (Guerola-Navarro et al., 2024).
Sentiment analysis, a technique used in the field of natural language processing
(NLP), enables the extraction, classification and quantification of the opinions and
emotions expressed in written texts (Tan et al., 2023). It has become a key tool
for capturing the voice of the customer in digital environments (Wewelwala &
Sumanathilaka, 2025). This methodological approach is gaining traction in busi -
ness research, including recent studies that apply text mining and NLP techniques
to innovation data (Cano-Marin, 2024). Its application to social media and review
platforms is particularly valuable due to the spontaneous, public and unstructured
nature of the interactions that occur in these spaces (Zaman et al., 2025). Through
either manual or automated analysis of comment polarity, companies can identify

4
Mayte García-García et al.
patterns of digital behaviour, detect recurring issues and assess the impact of their
responses on customer perception (Chikersal et al., 2015; Ghasemaghaei et al.,
2016).
However, social media has profoundly changed the relationship between consum-
ers and businesses, becoming key channels for customer interaction and customer
service (Song, 2023). Unlike traditional channels, on social media, users can see how
other customers are treated, creating a phenomenon of observational attention that
amplifies reputational reach (Wang et al., 2021). Furthermore, the public nature of
social media enables users to evaluate a company’s digital behaviour without any
prior direct interaction, thereby increasing the importance of every visible exchange
(Istanbulluoglu, 2017). This mechanism, unique to digital contexts, grants social
media a dual function: as a customer service channel and as a public showcase for
business management practices (Ocaña & Freire, 2022).
At the heart of this dynamic lie the reviews and comments generated by cus -
tomers on social platforms, which reflect their emotional state and influence other
consumers (Hu et al., 2017). Singh and Rios (2022) emphasise that customer service
and review management are critical to customer satisfaction and brand positioning.
Kapeš et al. (2022) show that prompt, professional and empathetic handling of
negative reviews not only restores customer perception but also builds trust and
can transform reputational threats into opportunities for improvement. An effective
feedback management strategy, combined with automated analysis tools, improves
understanding of consumer expectations and enables more timely and accurate
responses, showing a high degree of company engagement with its customer base
(Haupt et al., 2023).
Consumer opinions on social media directly impact brand image, customer
satisfaction and purchase decisions (Hossain & Kibria, 2024). As Hu et al. (2017)
demonstrate, public reviews can either deter or encourage potential customers to
interact with a company, influencing not only individual behaviour but also the
collective construction of corporate reputation (Khan et al., 2022). Therefore, posi -
tive, prompt and empathetic customer interaction can yield tangible benefits for the
company (van-Noort & Willemsen, 2012).
Customer satisfaction is, therefore, a key determinant of business success (Calle-
García et al., 2024). Numerous studies have shown that high satisfaction is asso -
ciated with higher levels of loyalty, positive recommendations and better financial
performance (Huang et al., 2025). This relationship has been widely corroborated
in service environments, where service quality and customer experience are key com-
petitive differentiators, directly influencing customers’ value perception and loyalty
(Elizalde-Elizalde, 2023). The benefits of effective service quality management are
extensive and well documented: higher satisfaction, increased retention, positive
referrals, lower staff turnover, reduced operational costs, greater market share and
stronger financial outcomes (Pei et al., 2020). Consequently, service quality has
remained a central focus of service marketing research over recent decades (Arguello-
Lara, 2023).

5
Social media sentiment as an indicator of service quality
In the insurance sector, satisfaction plays an especially important role due to
the intangible nature of the service, the low frequency of interactions and the high
emotional involvement of customers. These services require high levels of trust and
carry a significant degree of perceived risk (Wirtz & Lovelock, 2021). According to
Ghasemaghaei et al. (2016), sentiment analysis can help reduce negative attitudes
and attract new customers, making it a high-value tool for insurers. A thorough
understanding of consumers’ digital behaviour patterns is, therefore, essential for
designing effective loyalty strategies.
2. Methodology
The main objective of this research is to analyse the sentiment of comments made
by home insurance company customers on social media and their relationship with
the perceived quality of the service received. How does the sentiment expressed in
customer comments on social media influence the perception of service quality in this
sector? To address this question, the following specific objectives were established:
RO1:  To determine the predominant sentiment in user comments, classifying
them as negative, neutral or positive.
RO2:  To investigate how insurers respond to comments on social media in order
to assess their level of engagement.
RO3:  To compare the results of manual and automated sentiment analysis, using
Hugging Face models, to evaluate their overall accuracy, completeness and
precision.
RO4:  To categorise key terms used by customers in their posts, with the aim of
identifying recurring concepts associated with either positive or negative
service experiences.
The selection of the insurers analysed was based on the results of the customer
experience ranking published by the consultancy firm Stiga CX, which identifies
providers with the highest net promoter score (NPS) in the home insurance segment
in Spain. The NPS, introduced by Reichheld (2003), has become a benchmark metric
across many industries, including insurance, due to its simplicity and comparability.
However, its predictive validity as an indicator of satisfaction and growth has been
questioned by subsequent research (Keiningham et al., 2008). In the case of insur -
ance companies, a high NPS tends to be associated with greater profitability (Jahnert
& Schmeiser, 2022), reinforcing the idea that investing in customer satisfaction is
not merely a reputational concern but also a strategic imperative. In this study, NPS
served solely as a selection criterion rather than a comparative variable.
According to the Stiga CX report, the top three companies in terms of NPS in
the home insurance category are Mutua Madrileña, Mapfre and Santalucía. These
companies, therefore, constitute the focus of this study. We chose to concentrate

6
Mayte García-García et al.
on providers with high levels of customer satisfaction in order to explore whether
digital conversations reflect this positive perception or whether, conversely, social
media are the preferred channel for expressing complaints and dissatisfaction.
This approach is aligned with marketing analytics research from the last decade,
highlighting the importance of linking customer experience metrics, such as NPS,
to digital engagement and sentiment analysis (Logan et al., 2025; Weinstein, 2024;
Chun et al., 2021).
2.1. Sample
The sample analysed consists of 1,953 user comments collected from three digital
platforms: X (formerly Twitter), Facebook and Google Reviews. These platforms
were selected based on two main criteria. Firstly, they concentrate a high volume of
public and spontaneous user posts related to customer service, unlike platforms such
as Instagram or LinkedIn, where content tends to be predominantly visual or profes-
sional and contains few comments relevant to this type of analysis. Secondly, they
provide direct access to textual content, which is essential for applying automated
sentiment analysis techniques.
The use of social media data as a valid source for studying customer experience
and corporate communication has been widely supported in marketing and infor -
mation systems research. According to Stieglitz et al. (2018), social media analytics
enable real-time observation of public opinion and stakeholder interaction, provid -
ing valuable insights into user behaviour and perception. Recent reviews also high -
light the growing significance and methodological maturity of sentiment analysis in
social media research (Rodríguez-Ibáñez et al., 2023). This approach is particularly
relevant in service sectors such as insurance, where customer interactions are infre -
quent but emotionally charged, making social media a valuable natural setting for
observing authentic expressions of satisfaction and dissatisfaction.
Data collection took place during the second half of 2024, coinciding with the
NPS measurement period used as a reference. This temporal alignment ensures
greater consistency between the opinions analysed and the reputational context of
the insurers at the time of the study.
Data extraction from X and Facebook was carried out using open-source scrap -
ing tools, specifically Apify and Twikit, which enable the automated collection of
public posts based on defined search parameters (e.g. company name or associated
hashtags) (Blanco-Ruiz et al., 2024).
Prior to analysis, a data cleaning phase was conducted. Only clearly irrelevant
records were removed, such as messages of an advertising nature, corporate content
issued by the companies themselves, or mentions that did not contain information
that could be analysed. Duplicate messages were not removed, given that, in certain
situations (particularly observed on Facebook), users intentionally repeated the same
comment across multiple posts as a pressure mechanism in the absence of a response

7
Social media sentiment as an indicator of service quality
from the company. This behaviour pattern was considered relevant for the analysis,
as it reflected specific dynamics of interaction between customers and insurers in the
digital environment.
2.2. Content analysis
To analyse the emotional polarity of the comments, a dual coding approach
was applied. Firstly, a manual classification was performed on all 1,953 comments,
assigning each one a sentiment category: negative, positive or neutral (Adá-Lameiras
et al., 2024; Abuín-Penas et al., 2025). Manual labelling remains an essential step
in sentiment analysis, particularly in domains where emotional expression can be
context-dependent or culturally nuanced. Adá-Lameiras et al. (2024) demonstrate
that integrating qualitative annotation enhances interpretability and helps identi -
fy latent meanings often overlooked by automated models. This approach aligns
with current best practices in hybrid sentiment analysis methodologies. Automated
sentiment analysis was then conducted using a pre-trained model available on the
Hugging Face platform, widely recognised as a current reference in the NLP field
(Jain, 2022).
The choice of Hugging Face was based on several technical and scientific consid-
erations. Firstly, Hugging Face is currently one of the most widely used environments
in the NLP field, both in academic research and industrial applications, thanks to its
large developer community, accessible interface and comprehensive documentation
(Kaur et al., 2024). In addition, the platform is able to fine-tune and customise the
available models according to the specific needs of each task.
The context of this study was marked by a high degree of emotional expression
and complex linguistic nuances in user comments, similar to those found in other
sensitive domains such as love letters, as noted by Kaur et al. (2024). The trans -
former-based architecture provided by Hugging Face offers superior capabilities for
capturing subtle sentiment cues compared to more traditional approaches. This is
particularly relevant in the analysis of customer messages in the insurance sector,
where irony, sarcasm, ambiguity or emotionally charged language are frequently
encountered.
Although the pre-trained Hugging Face model used provides state-of-the-art per-
formance in generic sentiment analysis tasks, its ability to detect irony, sarcasm or
context-dependent expressions in the insurance domain may be limited. Future work
should, therefore, consider fine-tuning transformer architectures with sector-specific
corpora or adopting hybrid approaches that combine lexicon-based enrichment with
deep learning models to improve domain sensitivity.
Before applying the automated sentiment analysis model, the comments under -
went a text cleaning and preparation process. This pre-processing involved removing
non-linguistic noise, such as URLs, emojis, user mentions (@), hashtags and special
characters, as well as normalising capitalisation and adjusting spacing.

8
Mayte García-García et al.
Following this, basic linguistic processing tasks such as tokenisation, lemmati -
sation and named entity recognition were performed to improve the quality of the
text processed by the model. These operations helped to reduce semantic noise and
improve the accuracy of the automatic classification.
The descriptive statistical analysis of the data was carried out using Microsoft
Excel, which enabled the calculation of absolute and relative frequencies, the con -
struction of cross-tabulations and the generation of visual representations of key
study variables such as sentiment, publication platform and referenced company.
Excel was also used for data cleaning, coding, while the automated sentiment anal -
ysis was performed in a Python environment.
2.3. Validation of the automatic model
To validate the quality of the automatic sentiment analysis model (based on
Hugging Face), a direct comparison was made between the results of the automatic
classification and the manual coding previously performed on the sample of 1,953
comments.
A confusion matrix was constructed by crossing both codings, so that the rows
represent the manual sentiment (considered as a reference) and the columns repre -
sent the sentiment classified by the model.
From the confusion matrix, the usual evaluation metrics for supervised mul -
ti-class classification tasks were calculated: precision, recall, F1-score and accuracy,
widely used in machine learning literature to evaluate supervised classifiers (Santra
& Christy, 2012).
The metrics were calculated according to the following formulas:
- Precision:
Precision =       TP TP + FP
- Recall:
Recall =       TP TP + FN
- F1-score:
F1 = 2 x    Precision x Recall Precision + Recall
- Overall accuracy (accuracy):
Accuracy =          TP + TN TP + TN + FP + FN

9
Social media sentiment as an indicator of service quality
Where:
- TP (true positives): Number of correctly classified instances for a given class.
- FP (false positives): Number of instances incorrectly assigned to a class.
-  FN ( false negatives): Number of instances that the model failed to correctly
identify as belonging to a class.
The coded comments were classified into six thematic categories defined in the
manual coding process:
-  CUS (customer service/management): Evaluations related to service received,
responsiveness or staff treatment.
-  CLA (claims/service/coverage): Comments related to claims management, ser-
vice quality or satisfaction with insurance coverage.
-  TEC (technical issues/tools): References to technological aspects, such as app
or website functionality or access problems.
-  ECO (economic/billing/cancellations): Mentions of pricing, billing or contract
termination issues.
-  OPI (spontaneous opinions): Comments spontaneously posted about the
insurance companies under analysis.
-  OTH (other): Interactions unrelated to the direct insurance experience, such
as contest participation or general mentions.
In cases where a comment included references to more than one topic, a pri -
ority coding criterion was applied: the comment was assigned to the category
representing the main reason for the complaint or rating, i.e. the root cause of
the dissatisfaction or satisfaction expressed. This criterion avoids duplication and
ensures consistent and useful coding for analysing the sentiment associated with
each theme.
Word clouds were created using the online tool nubedepalabras.es  to generate
graphical representations of term frequency from text lists. Before generating the
clouds, a basic process of text cleaning and normalisation was carried out, con -
sisting of:
-  Removal of common Spanish stop words (articles, prepositions, pronouns,
etc.).
- Conversion of all terms to lower case.
- Removal of punctuation marks and special characters.
-  Manual grouping of equivalent or derived terms (e.g. ‘ siniestro’ and
‘siniestros’).
-  Exclusion of insurers’ names to prevent their high frequency from distorting
the analysis.
This exploratory analysis allows us to complement the quantitative results by
providing a visual representation of the dominant terms in customers’ discourse
on social media. This analysis aims to identify the most recurrent terms in users’
discourse and visualise language patterns associated with different themes and emo -
tional polarities.

10
Mayte García-García et al.
2.4. Ethical principles
This research adheres to the ethical principles governing the use of publicly avail-
able online data. All analysed content was obtained from open-access platforms (X,
Facebook and Google Reviews) where users voluntarily share opinions. No private,
sensitive or identifiable data were collected, and all posts were anonymised and
aggregated before analysis. The study followed the principles established by the
Regulation (EU) 2016/679 (2016), the European Code of Conduct for Research
Integrity (All European Academies [ALLEA], 2023) and the Association of Internet
Researchers’ Ethical Guidelines (Franzke et al., 2019), ensuring compliance with
transparency, data protection and respect for users’ digital rights.
3. Results
The sample analysed consists of a total of 1,953 comments collected from users
on X (formerly Twitter), Facebook and Google Reviews, directed at the insurers
Mutua Madrileña, Mapfre and Santalucía.
Regarding the distribution by platform (see Table 1), Facebook concentrates
the largest volume of comments, with 1,195 (61.19%), followed by X with 642
(32.87%) and Google Reviews with 116 (5.94%). This distribution reflects the
relative importance of each platform in the digital interaction dynamics between
customers and insurance providers.
Table 1. Distribution of comments by platform and company
Platform / Company Comments
Platform Facebook 1,195
Platform X (formerly Twitter) 642
Platform Google Reviews 116
Company Mapfre 1,038
Company Santalucía 565
Company Mutua Madrileña 350
Source: Own elaboration.
In terms of distribution by company (see Table 1), Mapfre received 1,038 com -
ments (53.25% of the total), followed by Santalucía with 565 comments (28.93%)
and Mutua Madrileña with 350 comments (17.92%). This distribution primarily
reflects differences in each company’s digital engagement strategy and the nature of
user participation dynamics on social media, rather than market share or direct busi-
ness volume. In particular, the number of comments directed at Santalucía is notably
influenced by the implementation of giveaways and promotional campaigns, which
significantly boost user engagement.

11
Social media sentiment as an indicator of service quality
3.1. Predominant sentiment in user comments
The majority of comments analysed displayed a negative tone, accounting for
67.84% of the total sample (1,325 comments). Neutral comments represented
22.58% (441), while positive comments made up 9.58% (187).
Sentiment analysis by company reveals clear differences in the tone of the com -
ments received by each insurer. Mutua Madrileña presents the highest proportion of
negative comments, with 86% of mentions expressing dissatisfaction. For Mapfre,
negative comments account for 73.31% of the total, while Santalucía shows a lower
proportion of negative sentiment, at 46.55% (see Table 2).
Table 2. Distribution of sentiment by company
Company Negative Positive Neutral
Mapfre 761 (73.31%) 117 (11.27%) 160 (15.41%)
Santalucía 263 (46.55%) 61 (10.80%) 241 (42.65%)
Mutua Madrileña 301 (86%) 9 (2.57%) 40 (11.43%)
Source: Own elaboration.
These results highlight distinct interaction dynamics for each company. In
the case of Santalucía, the volume of comments is strongly influenced by pro -
motional campaigns and prize draws, while Mapfre shows a notable presence
of spontaneous positive opinions, often associated with active brand defence by
loyal customers.
Regarding the distribution of comments by topic and polarity, the categories
related to claims (CLA) and customer service (CUS) account for the majority of
mentions. In both cases, the proportion of negative sentiment is especially high,
reflecting customer sensitivity regarding the management of these aspects (see
Table 3).
Table 3. Distribution of sentiment by topic
Topic Negative Positive Neutral TOTAL
CUS 275 11 41 327
CLA 460 8 9 477
TEC 40 0 12 52
ECO 258 0 8 266
OPI 151 48 0 199
OTH 141 120 371 632
TOTAL 1,325 187 441 1,953
Source: Own elaboration.

12
Mayte García-García et al.
In contrast, the OPI and OTH categories show a greater proportion of positive
or neutral comments. The former is associated with active brand advocacy – par -
ticularly evident among Mapfre supporters – while the latter includes interactions
related to promotional campaigns or prize draws, which are especially common on
Santalucía’s social media channels.
The concentration of comments around claims and customer service reinforces
the idea that users turn to social platforms mainly for problem resolution rather than
for relational or promotional engagement.
3.2. Response management by insurance companies
Of the total number of comments analysed, 57.86% received a response from the
company, while 42.14% did not receive a reply. This indicates the level of activity
and responsiveness maintained by insurers in their digital customer service channels.
When disaggregated by company, significant differences emerge: Mapfre shows the
highest response rate (63.29%), followed by Mutua Madrileña (57.43%) and Santa-
lucía (48.14%). This lower percentage in the case of Santalucía may be explained by
the high volume of comments related to prize draws, to which the company typically
does not respond. When these entries (228 comments) are excluded, Santalucía’s
response rate rises to 80.71%.
Differences also appear when analysing the response rate by comment topic.
Insurers tend to respond more frequently to comments related to claims (response
rate: 79.66%) and customer service (83.79%), suggesting greater responsiveness to
operational issues that require direct management. In contrast, comments related
to prize draws, promotions or general mentions, grouped under the OTH category,
receive responses in only 17.56% of cases, likely because they do not require per -
sonalised attention.
Although NPS was only a selection criterion, the predominance of negative sen -
timent suggests that high satisfaction scores do not necessarily yield positive public
discourse online.
3.3. Comparison of manual versus automatic sentiment analysis
The overall accuracy (accuracy) achieved by the model was 80.08% across the
full dataset. As shown in Table 4, the evaluation metrics by sentiment class indicate
that the model performs well in detecting negative comments, achieving an F1-score
of 87.84%, which is especially significant given that this is the most frequent senti -
ment in the dataset. The classification of positive and especially neutral comments
proves more challenging. This is consistent with known difficulties in sentiment
analysis tasks, where distinguishing neutral tone from slight positivity or negativity
is often ambiguous in natural language.

13
Social media sentiment as an indicator of service quality
Table 4. Evaluation metrics by sentiment class
Class Accuracy Recall F1-score
Negative 93.07% 83.17% 87.84%
Neutral 56.59% 76.87% 65.19%
Positive 72.35% 65.78% 68.91%
Source: Own elaboration.
Figure 1. Word cloud of comments with negative sentiment
Source: Own elaboration.
These results suggest that the Hugging Face model provides high reliability in iden-
tifying negative sentiment but has more difficulty accurately classifying ambiguous or
moderately toned comments, particularly those falling into the neutral category.
3.4. Exploratory lexical analysis of key terms used by customers
As a complement to the sentiment and thematic analyses, an exploratory lexical
frequency analysis was conducted on the comments collected. This section presents
only the cloud corresponding to comments labelled as negative, as this is the most
representative category in the corpus analysed.
The negative word cloud (see Figure 1) clearly highlights the most frequent the -
matic elements in comments with a negative tone. There is a strong presence of terms

14
Mayte García-García et al.
related to claims management, such as ‘parte’ (claim report), ‘siniestro’ (claim) or
‘perito’ (loss adjuster), as well as references to customer service channels, with words
such as ‘llamadas’ (calls), ‘esperando’ (waiting) or ‘respuesta’ (response). Company
names also appear prominently, with ‘Mapfre’ being the most frequently mentioned,
reflecting its higher comment volume within the dataset.
The word cloud also reveals a notable emotional intensity, with terms such as
‘vergüenza’ (shame/ashamed) indicating the discomfort and frustration experienced
by users due to unresolved issues or the perceived inefficiency of the service.
The positive comments reveal a clearly distinct lexical field. It is dominated by
terms such as ‘ thank you’, ‘always’, ‘best’, or ‘love it’, suggesting that favourable
evaluations centre on satisfactory service experiences, personalised attention or effi -
cient management. This contrast reinforces the findings of the thematic analysis, in
which personalisation and responsiveness are linked to positive perceptions, while
structural or procedural issues tend to generate negative sentiment.
4. Discussion
The results obtained in this study provide a deeper understanding of customer
behaviour patterns on social media within the Spanish insurance sector. Most of the
comments analysed display a negative tone (RO1), consistent with prior research
on consumer behaviour in digital environments (Ward & Ostrom, 2006; Kim
et al., 2016). This behaviour has also been documented in other sectors. In a study
on internet services, Kusumawati et al. (2024) describe how users utilise social media
to publicly express their frustration, expecting the company to react more quickly
due to the visibility of the complaint. This emotional and strategic dimension of
public complaints coincides with the observations made in the present study, where
the absence of corporate response activated patterns of replication and pressure in
the digital environment. This negativity is particularly concentrated in two critical
areas: claims management (CLA) and customer service (CUS), which account for a
high percentage of complaints, claims and unsatisfactory ratings regarding incident
handling, the quality of service received or communication with the company. This
finding is also in line with the results of Rajendran et al. (2023), who, based on the
analysis of online reviews of insurance companies, identified the main causes of dis -
satisfaction as inadequate customer service, ineffective claims handling, issues related
to payments or tariffs and a lack of response from back-office services. These areas
are thus the main pain points in the insurance experience as expressed by customers
themselves and reinforce the importance of optimising claims handling processes and
digital customer service channels. This is consistent with broader findings on how
negative sentiment expressed in digital contexts can impact corporate reputation
and influence customer behaviour (Pérez-Elizundia et al., 2021). This predominance
of negative sentiment suggests that social media channels are primarily used by cus -
tomers to report incidents and express dissatisfaction, rather than to acknowledge

15
Social media sentiment as an indicator of service quality
satisfactory experiences. This pattern aligns with previous research highlighting that
users tend to share negative experiences more frequently in public online spaces than
positive ones (Wang et al., 2021; Istanbulluoglu, 2017).
Although the volume of positive comments is comparatively low, differential
phenomena were identified in two of the companies analysed. In the case of Map -
fre, there is a significant volume of spontaneous positive opinions (OPI), in which
customers voluntarily express their satisfaction with the company through direct
messages posted in various publications, not necessarily in response to previous crit-
icism. This reflects the presence of a group of satisfied customers who proactively
generate positive content in the brand’s digital environments. For Santalucía, the
volume of positive and neutral comments is influenced by two specific factors: first -
ly, the organisation of promotional giveaways on social media, which generate high
levels of participation through user mention mechanisms; and secondly, the dissem -
ination of an emotionally charged advertising campaign that prompted numerous
expressions of sympathy towards the company from its customers. These elements
show how certain digital marketing actions can generate specific peaks in positive
polarity, unrelated to the direct insurance experience.
The analysis of the companies’ responses reveals relevant differences in their level
of involvement and active management across digital channels (RO2). Companies
show higher response rates for claims-related (CLA) and customer service (CUS)
comments, where public incident management is likely to have a greater reputational
impact. In contrast, promotional (OTH) or economic (ECO) comments receive sig -
nificantly fewer responses, which may reflect a prioritisation of resources towards
areas perceived as more critical for customer satisfaction and loyalty. These results
are consistent with patterns described in previous studies. Gunarathne et al. (2018)
found that airlines prioritise their social media responses to complaints with poten -
tial reputational impact, while promotional queries receive less attention. Istanbul -
luoglu (2017) showed that faster response times to social media complaints lead to
higher customer satisfaction, suggesting that content-type-based management could
be an effective strategy for reputational protection and enhancing customer experi -
ence. This aligns with prior research showing a focus on operational issue resolution
over relational engagement (Istanbulluoglu, 2017; Wang et al., 2021).
Regarding the validation of the automatic sentiment analysis model (Hugging
Face), the results show satisfactory performance in classifying negative comments
but greater difficulty in discriminating neutral and positive ones (RO3). These lim -
itations may partly stem from the linguistic particularities of the insurance sector
on social media. On the one hand, irony, sarcasm, double meanings and ambiguity
are frequently used, especially in comments critical of insurers. These rhetorical
devices pose a major challenge for sentiment analysis models based on machine
learning, as the emotional tone often does not align with the literal text. Several
studies highlight these difficulties. Bhargava et al. (2025) show that models trained
in technical domains have low accuracy when classifying sarcastic comments, though
performance improves significantly when such expressions are excluded. Similarly,

16
Mayte García-García et al.
Potamias et al. (2020) note that irony and sarcasm hinder the ability of NLP systems
to accurately detect emotional polarity. The use of technical terminology specific to
the insurance domain introduces additional nuances that complicate the automatic
classification of certain messages, particularly when criticism is implicit or under -
stated. These specificities highlight the importance of considering sector-specific
contexts when applying sentiment analysis models trained on generalist corpora, as
is the case with the Hugging Face model used here. According to a recent systematic
review by Hakim et al. (2025), generic sentiment analysis models often fail to inter -
pret technical insurance jargon (e.g. ‘rating’, ‘coverage’, ‘indemnity’) and sectoral
metaphors, leading to polarity and neutrality misclassifications. Furthermore, Claus
and Stella (2022) argue that models must adapt lexicons and be trained on insur -
ance-specific texts to accurately interpret terms such as ‘excess’ or ‘parties’ in the
context of customer experience.
Finally, during the exploratory lexical analysis of the corpus, there was a
high frequency of terms related to claims management, with a strong emotional
charge, highlighting ‘shame/ashamed’ as an indicator of users’ discomfort with
the perceived inefficiency of the service (RO4). A recurring pattern emerged:
many users who posted comments on social media did so after experiencing pri -
or difficulties with other customer service channels, such as telephone or email.
In numerous messages, customers describe long waits, dropped calls, repeated
transfers between departments or even disconnection when attempting to file
a formal complaint. Some users report that when they express the intention to
lodge a formal complaint, communication is cut, whereas assistance is offered if
they request a different administrative or commercial service. This suggests that,
for a significant number of customers, social media acts as a last resort channel,
used after they perceive a lack of resolution or inadequate service via traditional
channels. This phenomenon helps to explain, at least in part, the high proportion
of negative comments recorded on the insurers’ digital profiles. It is consistent
with the findings of Hogreve et al. (2019), who highlight the growing use of social
media by consumers as a public forum for complaints, which increases companies’
reputational exposure.
5. Conclusions
The study results show that insurers who actively manage customer service on
social media improve their reputation and perceived service quality, while a lack of
response or interaction is associated with an increase in negative sentiment. These
findings underscore the strategic importance of proactive and empathetic digital
communication as a central element of the customer experience. The study provides
empirical evidence linking classic service quality models such as SERVQUAL (Para -
suraman et al., 1988) and the functional-technical model (Grönroos, 1984) with
current approaches to digital experience and corporate reputation, showing that

17
Social media sentiment as an indicator of service quality
sentiment analysis enables real-time observation of the emotional and relational
dimensions of interactions between customers and companies.
From a practical perspective, the results reaffirm the need to monitor and respond
quickly and empathetically to conversations on social media in order to reduce
negative sentiment and strengthen customer trust. Overall, this study broadens our
understanding of service quality in digital environments, demonstrating that custom-
er experience is co-constructed through visible and collective interactions on social
media, thereby redefining the relationship between communication, reputation and
perceived value in the digital age.
The use of a pre-trained general-purpose model may have limited sensitivity to
industry-specific language, and the analysis was restricted to Spanish-language com-
ments. Future studies should adjust transformer-based models with domain-specific
data and incorporate multilingual and multimodal approaches to more accurately
capture the diversity of expressions and emotional nuances in digital environments.
Author’s contribution
Mayte García-García: Conceptualization; Data curation; Formal analysis; Investi-
gation; Methodology; Project administration; Software; Validation; Writing – original
draft.
Alba Adá-Lameiras:  Formal analysis; Resources; Supervision; Visualization;
Writing – review and editing.
Javier de Estaban Curiel: Methodology; Supervision; Validation; Writing – review
and editing.
Acknowledgements
The authors would like to thank Stiga CX for their support in identifying the
home insurance companies in Spain with the highest Net Promoter Score (NPS),
which served as the basis for the case selection in this study.
References
Abuín-Penas, J., Adá-Lameiras, A., & Blanco-Ruiz, M. (2025). Social Influence of
the# SeAcabó Case: Analysis of Messages Received by Spanish National Team
Players on Social Media. Géneros, 14(3), 178-200.
Adá-Lameiras, A., Abuín-Penas, J., & Blanco-Ruiz, M. (2024). Giving voice to the
protagonists: The impact of social networks as a source of information in the case
of Jennifer Hermoso and the #SeAcabó movement. Dígitos. Revista de Comuni-
cación Digital, 10, 46–73. https://doi.org/10.7203/drdcd.v0i10.279

18
Mayte García-García et al.
All European Academies. (ALLEA). (2023). European Code of Conduct for Research
Integrity (Revised Edition). https://allea.org/wp-content/uploads/2023/06/Euro-
pean-Code-of-Conduct-Revised-Edition-2023.pdf
Amin, M., Gohar, M., & Ali, I. (2025). Impact of digital transformation on SME’s
marketing performance: role of social media and market turbulence. Discover
Sustainability, 6(1), 1–24. https://doi.org/10.1007/s43621-025-01228-3
Apria, A.  L., & Parahiyanti, C.  R. (2023). Customer Satisfaction, Brand Love,
and Emotional Brand Attachment: Building Loyalty for Hospital Marketing.
In I. Zutiasari & D. T. Kurniawan (Eds.), Proceedings of the BISTIC Business
Innovation Sustainability and Technology International Conference (BISTIC)
(pp. 196–206). Atlantis Press. https://doi.org/10.2991/978-94-6463-302-3_23
Arguello-Lara, P. B. (2023). Service marketing and its impact on customer service:
a case study. Social and Administrative Perspectives , 1(1), 5–16. https://doi.
org/10.61347/psa.v1i1.54
Bhargava, N., Radaideh, M. I., Kwon, O. H., Verma, A., & Radaideh, M. I. (2025).
On the Impact of Language Nuances on Sentiment Analysis with Large Language
Models: Paraphrasing, Sarcasm, and Emojis . arXiv. https://doi.org/10.48550/
arXiv.2504.05603
Blanco-Ruiz, M., Adá-Lameiras, A., & Atauri-Mezquida, D. (2024). New Trends in
Digital Marketing: Analysis of the Social Conversation on X.com About Metaverse
and Artificial Intelligence. FIIB Business Review, 23197145241281033. https://
doi.org/10.1177/23197145241281033
Calle-García, A.  J., Conforme-Merchan, Y.  M., Magallanes-Bueno, E.  L., Teje-
na-Vargas, N.  D., & García-Santana, M.  L. (2024). Market Research Design
for Customer Satisfaction Evaluation: Effective Methods and Tools. Ciencia y
Desarrollo, 27(1), 31–41. http://dx.doi.org/10.21503/cyd.v27i1.2538
Cano-Marin, E. (2024). The transformative potential of Generative Artificial Intel -
ligence (GenAI) in business: a text -mining analysis on innovation data sources.
ESIC Market, 55(2), e333. https://doi.org/10.7200/esicm.55.333
Chikersal, P., Poria, S., & Cambria, E. (2015). SeNTU: Sentiment analysis of tweets
by combining a rule-based classifier with supervised learning. In P. Nakov, T.
Zesch, D. Cer, & D. Jurgens (Eds.), Proceedings of the 9th International Work -
shop on Semantic Evaluation (SemEval 2015)  (pp.  647–651). Association for
Computational Linguistics. https://doi.org/10.18653/v1/S15-2112
Chinomona, R., & Maziriri, E. T. (2017). The influence of brand awareness, brand
association and product quality on brand loyalty and repurchase intention: a case
of male consumers for cosmetic brands in South Africa. Journal of Business and
Retail Management Research, 12(1). https://doi.org/10.24052/JBRMR/V12IS01/
TIOBABAAPQOBLARIACOMCFCBISA
Chun, H., Leem, B-H., & Suh, H. (2021). Using text analytics to measure an effect
of topics and sentiments on social-media engagement: Focusing on Facebook fan
page of Toyota. International Journal of Engineering Business Management , 13.
https://doi.org/10.1177/18479790211016268

19
Social media sentiment as an indicator of service quality
Claus, S., & Stella, M. (2022). Natural Language Processing and Cognitive Net -
works Identify UK Insurers’ Trends in Investor Day Transcripts. Future Internet,
14(10), 291. https://doi.org/10.3390/fi14100291
Dirección General de Seguros y Fondos de Pensiones. (2024). Seguros y Fondos de
Pensiones. Informe 2023. Ministerio de Economía, Comercio y Empresa, Gobier-
no de España. https://dgsfp.mineco.gob.es/es/Publicaciones/DocumentosPublica-
ciones/V6%20Memoria%20informe%20del%20sector%202023.pdf
Elizalde-Elizalde, I. G. (2023). La calidad del servicio al cliente como diferenciador
estratégico en las empresas de pintura en Guayaquil. ASCE Magazine , 2(2),
33–47. https://doi.org/10.70577/ASCE/33.47/2023
Franzke, A.  S., Bechmann, A., Zimmer, M., Ess, C., & Association of Internet
Researchers. (2019). Internet Research: Ethical Guidelines 3.0 . Association of
Internet Researchers. https://aoir.org/reports/ethics3.pdf
Ghasemaghaei, M., Eslami, S.  P., Deal, K., & Hassanein, K. (2016). Consumers’
Attitude toward Insurance Companies: A Sentiment Analysis of Online Consum-
er Reviews. AMCIS 2016 Proceedings , 10. https://aisel.aisnet.org/amcis2016/
Decision/Presentations/10
Grönroos, C. (1984). A service quality model and its marketing implications.
European Journal of Marketing , 18(4), 36–44. https://doi.org/10.1108/
EUM0000000004784
Guerola-Navarro, V., Gil-Gomez, H., Oltra-Badenes, R., & Soto-Acosta, P. (2024).
Customer relationship management and its impact on entrepreneurial marketing:
A literature review. International Entrepreneurship and Management Journal ,
20(2), 507–547. https://doi.org/10.1007/s11365-022-00800-x
Gunarathne, P., Rui, H., & Seidmann, A. (2018). When Social Media Delivers
Customer Service. MIS Quarterly , 42(2), 489–520. https://doi.org/10.25300/
MISQ/2018/14290
Hakim, L., Nuryasin, I., & Nugroho, S. (2025). Sentiment analysis in insurance: A
systematic review of approaches, techniques, and applications. Multidisciplinary
Reviews, 8(10), 2025323–2025323. https://doi.org/10.31893/multirev.2025323
Haupt, M., Rozumowski, A., Freidank, J., & Haas, A. (2023). Seeking empathy or
suggesting a solution? Effects of chatbot messages on service failure recovery.
Electronic Markets, 33(1), 56. https://doi.org/10.1007/s12525-023-00673-0
Hogreve, J., Bilstein, N., & Hoerner, K. (2019). Service recovery on stage: Effects
of social media recovery on virtually present others. Journal of Service Research,
22(4), 421–439. https://doi.org/10.1177/1094670519851871
Hossain, M. Z., & Kibria, H. (2024). Exploring the evolution of brand loyalty in the
age of social media. Journal of Service Science and Management, 17(3), 219–247.
https://doi.org/10.4236/jssm.2024.173011
Hu, G., Bhargava, P., Fuhrmann, S., Ellinger, S., & Spasojevic, N. (2017). Analyzing
Users’ Sentiment Towards Popular Consumer Industries and Brands on Twitter.
In R. Gottumukkala, X. Ning, G. Dong, V. Raghavan, S. Aluru, G. Karypis, L.

20
Mayte García-García et al.
Miele, & X. Wu (Eds.), 2017 IEEE International Conference on Data Mining
Workshops (pp. 381–388). IEEE. https://doi.org/10.1109/ICDMW.2017.55
Huang, Y., Li, M., Tsung, F., & Chang, X. (2025). Mining social media data via
supervised topic model: Can social media posts inform customer satisfaction?
Decision Sciences, 56, 423–442. https://doi.org/10.1111/deci.12660
Istanbulluoglu, D. (2017). Complaint handling on social media: The impact of mul -
tiple response times on consumer satisfaction. Computers in Human Behavior ,
74, 72–82. https://doi.org/10.1016/j.chb.2017.04.016
Jahnert, J. R., & Schmeiser, H. (2022). The relationship between net promoter score
and insurers’ profitability: An empirical analysis at the customer level. The Gene-
va Papers on Risk and Insurance - Issues and Practice , 47(4), 944–972. https://
doi.org/10.1057/s41288-021-00237-3
Jain, S. M. (2022). Hugging Face. In S. M. Jain (Ed.), Introduction to Transformers
for NLP (pp. 51–67). Apress. https://doi.org/10.1007/978-1-4842-8844-3_4
Kapeš, J., Keča, K., Fugošić, N., & Čuić Tanković, A. (2022). Management response
strategies to a negative online review: Influence on potential guests’ trust. Tourism
and Hospitality Management, 28(1), 1–27. https://doi.org/10.20867/thm.28.1.1
Kaur, G., Kaur, A., Khurana, M., & Damaševičius, R. (2024). Sentiment Polarity
Analysis of Love Letters: Evaluation of TextBlob, Vader, Flair, and Hugging Face
Transformer. Computer Science and Information Systems , 21(4), 1411–1433.
https://doi.org/10.2298/CSIS240328040K
Keiningham, T.  L., Aksoy, L., Cooil, B., & Andreassen, T.  W. (2008). A holistic
examination of Net Promoter. Journal of Database Marketing & Customer Strat-
egy Management, 15, 79–90. https://doi.org/10.1057/dbm.2008.4
Khan, R. U., Salamzadeh, Y., Iqbal, Q., & Yang, S. (2022). The impact of custom -
er relationship management and company reputation on customer loyalty: The
mediating role of customer satisfaction. Journal of Relationship Marketing ,
21(1), 1–26. https://doi.org/10.1080/15332667.2020.1840904
Kim, S.  J., Wang, R.  J.  H., Maslowska, E., & Malthouse, E.  C. (2016). “Under-
standing a fury in your words”: The effects of posting and viewing electronic
negative word-of-mouth on purchase behaviors. Computers in Human Behavior,
54, 511–521. https://doi.org/10.1016/j.chb.2015.08.015
Kusumawati, N., Suhandi, A. T., & Purwanegara, M. S. (2024). Why do customers
decide to complain on social media? And how to produce customer forgiveness.
Review of Integrative Business and Economics Research , 13(3), 235–254.
Levy, S., & Hino, H. (2016). Emotional brand attachment: a factor in custom -
er-bank relationships. International Journal of Bank Marketing, 34(2), 136–150.
https://doi.org/10.1108/IJBM-06-2015-0092
Logan, J., Doneddu, D., McLafferty, K., Ahmad, M. I., & Micallef, N. (2025). Behind
Customer Satisfaction Metrics: Exploring User Perceptions of Net Promoter Score
(NPS) as a Measure of Satisfaction. In C. Ardito, S. D. J. Barbosa, T. Conte, A. Freire,
I. Gasparini, P. Palanque, & R. Prates (Eds.), Human-Computer Interaction – INTER-
ACT 2025 (pp. 135–156). Springer. https://doi.org/10.1007/978-3-032-05002-1_7

21
Social media sentiment as an indicator of service quality
Martin-Domingo, L., Martín, J.  C., & Mandsberg, G. (2019). Social media as
a resource for sentiment analysis of Airport Service Quality (ASQ). Jour-
nal of Air Transport Management , 78, 106–115. https://doi.org/10.1016/j.
jairtraman.2019.01.004
Mostafa, M. M. (2013). More than words: Social networks’ text mining for con -
sumer brand sentiments. Expert Systems with Applications, 40(10), 4241–4251.
https://doi.org/10.1016/j.eswa.2013.01.019
Ocaña, P., & Freire, T. (2022). Impact of social media management in gastronomic
businesses. Chakiñan. Revista de Ciencias Sociales y Humanidades , 16, 52–67.
https://doi.org/10.37135/chk.002.16.03
Parasuraman, A. B. L. L., Zeithaml, V. A., & Berry, L. (1988). SERVQUAL: A mul-
tiple-item scale for measuring consumer perceptions of service quality. Journal of
Retailing, 64(1), 12–40.
Pedreschi-Caballero, R. J., & Nieto-Lara, O. M. (2023). La importancia del market-
ing de servicios y la calidad de atención al cliente. Revista Colegiada de Ciencia,
5(1), 107–118. https://doi.org/10.48204/j.colegiada.v5n1.a4410
Pei, X. L., Guo, J. N., Wu, T. J., Zhou, W. X., & Yeh, S. P. (2020). Does the effect
of customer experience on customer satisfaction create a sustainable competitive
advantage? A comparative study of different shopping situations. Sustainability,
12(18), 7436. https://doi.org/10.3390/su12187436
Pérez-Elizundia, G., Delgado-Guzmán, J.  A., & Lampón, J.  F. (2021). COV -
ID-19 liquidity crisis: May reverse factoring be the solution to SME financ -
ing in Mexico. ESIC Market , 52(3), 571–596. https://doi.org/10.7200/
esicm.168.0523.3
Potamias, R.  A., Siolas, G., & Stafylopatis, A.  G. (2020). A transformer-based
approach to irony and sarcasm detection. Neural Computing and Applications ,
32(23), 17309–17320. https://doi.org/10.1007/s00521-020-05102-3
Rajendran, S., Srinivas, S., & Pagel, E. (2023). Mining voice of customers and
employees in insurance companies from online reviews: a text analytics approach.
Benchmarking: An International Journal , 30(1), 1–22. https://doi.org/10.1108/
BIJ-12-2020-0650
Regulation (EU) 2016/679 of the European Parliament and of the Council of
27 April 2016 on the protection of natural persons with regard to the processing
of personal data and on the free movement of such data, and repealing Directive
95/46/EC (General Data Protection Regulation), 2016. https://eur-lex.europa.eu/
eli/reg/2016/679/oj/eng
Reichheld, F.  F. (2003). The One Number You Need to Grow. Harvard Business
Review, 81(12), 46–55.
Rodríguez-Ibáñez, M., Casánez-Ventura, A., Castejón-Mateos, F., & Cuenca-Jimén-
ez, P. M. (2023). A review on sentiment analysis from social media platforms.
Expert Systems with Applications, 223, 119862.

22
Mayte García-García et al.
Rosário, A.  T., & Casaca, J.  A.  C. (2023). Relationship marketing and customer
satisfaction: a systematic review of the literature. Estudios Gerenciales, 39(169),
516–532. https://doi.org/10.18046/j.estger.2023.169.6218
Santra, A.  K., & Christy, C.  J. (2012). Genetic algorithm and confusion
matrix for document clustering. International Journal of Computer Sci -
ence Issues (IJCSI) , 9(1), 322–328. https://www.proquest.com/scholarly-jour-
nals/genetic-algorithm-confusion-matrix-document/docview/963361837/
se-2?accountid=201395
Sharma, N.  A., Ali, A.  B.  M.  S., & Kabir, M.  A. (2025). A review of sentiment
analysis: tasks, applications, and deep learning techniques. International Jour-
nal of Data Science and Analysis , 19, 351–388. https://doi.org/10.1007/
s41060-024-00594-x
Sheth, J. N., Jain, V., & Ambika, A. (2023). The growing importance of custom -
er-centric support services for improving customer experience. Journal of Busi -
ness Research, 164, 113943. https://doi.org/10.1016/j.jbusres.2023.113943
Singh, S., & Rios, A. (2022). Linguistic elements of engaging customer service dis -
course on social media. arXiv. https://doi.org/10.48550/arXiv.2212.12801
Song, H. (2023). A Review of the Impact of Social Media in Customer Rela -
tionship Management of Large Corporations in the UK. Advances in Eco -
nomics, Management and Political Sciences , 22, 144–150. https://doi.
org/10.54254/2754-1169/22/20230302
Stieglitz, S., Mirbabaie, M., Ross, B., & Neuberger, C. (2018). Social media ana -
lytics—Challenges in topic discovery, data collection, and data preparation.
International Journal of Information Management , 39, 156–168. https://doi.
org/10.1016/j.ijinfomgt.2017.12.002
Tan, K.  L., Lee, C.  P., & Lim, K.  M. (2023). A survey of sentiment analysis:
Approaches, datasets, and future research. Applied Sciences, 13(7), 4550. https://
doi.org/10.3390/app13074550
van-Noort, G., & Willemsen, L.  M. (2012). Online damage control: The effects
of proactive versus reactive webcare interventions in consumer-generated and
brand-generated platforms. Journal of Interactive Marketing , 26(3), 131–140.
https://doi.org/10.1016/j.intmar.2011.07.001
Wang, F., Wang, M., Wan, Y., Jin, J., & Pan, Y. (2021). The power of social learning:
How do observational and word-of-mouth learning influence online consumer
decision processes? Information Processing & Management , 58(5), 102632.
https://doi.org/10.1016/j.ipm.2021.102632
Ward, J. C., & Ostrom, A. L. (2006). Complaining to the masses: The role of protest
framing in customer-created complaint web sites. Journal of Consumer Research,
33(2), 220–230. https://doi.org/10.1086/506303
Weinstein, A. (2024). In search of customer delight: Integrating customer satisfaction
and NPS metrics. Applied Marketing Analytics: The Peer-Reviewed Journal, 9(4),
320–329. https://doi.org/10.69554/QNUB2426

23
Social media sentiment as an indicator of service quality
Wewelwala, S. H., & Sumanathilaka, T. G. D. K. (2025). Hybrid Emotion Recogni-
tion: Enhancing Customer Interactions Through Acoustic and Textual Analysis .
arXiv. https://doi.org/10.48550/arXiv.2503.21927
Wirtz, J., & Lovelock, C. (2021). Services marketing: People, technology, strategy .
World Scientific.
Zaman, S.  U., Haider, S.  M.  R., & Alam, S.  H. (2025). Exploring the Impact of
E-Service Quality, Trust, and Social Media on Consumer Satisfaction and Loyal-
ty. Journal of Regional Studies Review, 4(1), 184–197. https://doi.org/10.62843/
jrsr/2025.4a063
