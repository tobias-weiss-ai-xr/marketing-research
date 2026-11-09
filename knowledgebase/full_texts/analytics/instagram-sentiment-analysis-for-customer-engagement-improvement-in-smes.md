---
title: Instagram Sentiment Analysis for Customer Engagement Improvement in SMEs
url: https://doi.org/10.51903/jmi.v5i2.337
category: analytics
subcategory: framework
date: 2026-08
venue: Journal of Management and Informatics
authors:
- Carlos Mendes
- Ana Silva
source: openalex-oa
pdf_url: https://jmi.stekom.ac.id/index.php/jmi/article/download/337/171
pages: 23
chars: 67078
fetched_at: '2026-11-08T18:02:29+00:00'
kb_version: 1
---

# Instagram Sentiment Analysis for Customer Engagement Improvement in SMEs

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119
Publication Link: https://jmi.stekom.ac.id/index.php/jmi/issue/view/14
DOI: https://doi.org/10.51903/jmi.v5i2.337

Instagram Sentiment Analysis for Customer Engagement
Improvement in SMEs
Carlos Mendes*1, Ana Silva2
Email: carlos.21mendes@gmail.com
1,2Business Analytics and Accounting, University of Rochester, NY, USA
*Corresponding Author
Abstract
Small and Medium Enterprises (SMEs) increasingly rely on Instagram as a primary digital marketing
channel; however, customer engagement is frequently evaluated through quantitative metrics such as
likes and reach, with limited integration of emotional orie ntation embedded in user-generated content.
This study addresses this gap by positioning sentiment analysis as an evaluative tool within digital
marketing analytics for SMEs. The research aims to identify customer sentiment patterns in SME
Instagram content, explain the role of sentiment analysis in assessing customer engagement, and provide
a data-driven foundation for improving engagement performance. The study adopts a quantitative design
using naturally occurring Instagram data, including captions and c omments collected from SME
accounts within a defined period. Text preprocessing is conducted prior to sentiment classification using
a lexicon-based approach with the VADER (Valence Aware Dictionary and Sentiment Reasoner) model
to capture polarity and intensity of sentiments in social media text. Furthermore, statistical analysis is
performed using correlation analysis and one -way ANOVA to examine the relationship and differences
between sentiment categories and engagement indicators (likes, comments, and interaction rate).  The
findings reveal systematic variation in engagement metrics across sentiment polarity categories,
indicating that emotional orientation represents a relevant analytical dimension in engagement
evaluation. The study contributes theoretically by reinforc ing the multidimensional perspective of
customer engagement and methodologically by integrating text mining techniques with engagement
analytics in the SME context. Practically, it offers a replicable and scalable analytical framework that
enables SMEs to incorporate sentiment-based evaluation into Instagram content strategy development.
Keywords: Customer Engagement, Digital Marketing Analytics, Instagram, Sentiment Analysis, Small
and Medium Enterprises.
Received in February 2026; Revised in March 2026; Accepted in April 2026; Published in August 2026.
I. INTRODUCTION
Small and Medium Enterprises (SMEs) increasingly rely on digital marketing to sustain
competitiveness and strengthen market positioning in the contemporary digital economy. The
rapid integration of social media platforms into marketing strategies has trans formed how
businesses communicate with customers, shifting from one -way promotion to interactive
engagement-oriented communication. Digital marketing analytics has emerged as a critical
instrument for understanding consumer behavior, enabling organizations  to translate large
volumes of online data into actionable managerial insights. Scholars emphasize that data -driven
marketing approaches allow firms to improve customer -centric strategies and enhance business
performance through evidence-based decision-making processes (Grandhi et al., 2021; Gupta et
al., 2020; Mark Anthony Camilleri, 2019; Shah & Murthi, 2021).
Recent developments highlight Instagram as one of the most influential platforms for SME
marketing due to its visual storytelling capabilities and high user engagement potential. SMEs
actively utilize Instagram to promote products, interact with customers, and strengthen brand

Instagram Sentiment Analysis for Customer Engagement ...

98      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

visibility, especially in emerging economies where digital adoption accelerates business
transformation. Social media marketing has proven effective in supporting SME growth,
sustainability, and customer relationship development, particularly during period s of digital
disruption. However, businesses often rely on surface-level performance indicators such as likes,
reach, and comment counts, which may not fully capture customer perceptions or emotional
responses toward digital content (Chatterjee & Kumar Kar, 2020; Malesev & Cherry, 2021; Patma
et al., 2021; Pellegrino & Abe, 2023).
The academic literature increasingly recognizes customer engagement as a multidimensional
construct encompassing cognitive, emotional, and behavioral interactions between customers and
brands. Customer engagement not only reflects customer participation bu t also represents a
strategic resource that influences loyalty, satisfaction, and long -term business sustainability.
Studies have demonstrated that engagement outcomes are strongly influenced by customers’
emotional reactions and online interactions within  social media environments. Furthermore,
recent research underscores the importance of analyzing both positive and negative engagement
patterns to achieve a comprehensive understanding of customer behavior in digital marketing
contexts (Barari et al., 2021; Lim et al., 2022; Naumann et al., 2020; Ng et al., 2020).
Sentiment analysis has gained attention as a powerful analytical technique for extracting
emotional meaning from user-generated content on social media platforms. Advances in machine
learning and natural language processing have enabled more accurate class ification of customer
opinions, allowing organizations to evaluate public perceptions systematically. Previous studies
demonstrate that sentiment analysis on Instagram data can provide valuable insights into
consumer attitudes and behavioral tendencies, of fering a richer understanding than traditional
quantitative metrics alone. However, many prior studies do not clearly specify the sentiment
analysis techniques employed, including model selection, parameterization, or validation
procedures, which limits methodological transparency and reproducibility. In addition, the
absence of standardized and well -documented analytical pipelines creates challenges in
comparing results across studies and applying them in SME contexts.  The application of
sentiment analysis has also expanded across various sectors, illustrating its potential to support
data-driven marketing and strategic decision-making processes (Al-Otaibi & Al-Rasheed, 2022;
Chan & Yang, 2023; Karayiğit et al., 2022; Smith & Cipolli, 2022).
Despite growing research on social media analytics and customer engagement, several critical
gaps remain. Many studies focus on general social media marketing performance or emphasize
quantitative engagement indicators without integrating emotional sentime nt interpretation.
Existing sentiment analysis research often concentrates on opinion classification without linking

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

results to actionable managerial implications, particularly for SMEs that operate with limited
analytical resources and technological capabilities. Moreover, there is limited integration of
statistical analysis in evaluating the relationship between sentiment polarity and engagement
metrics, resulting in findings that are often descriptive rather than inferential. This lack of
statistical rigor reduce s the ability to validate whether observed engagement differences are
significant and generalizable. These limitations create challenges for SMEs in adopting advanced
analytics despite the increasing availability of digital marketing data. Moreover, research
specifically examining Instagram sentiment analysis as an evaluative tool for customer
engagement performance in SMEs remains relatively limited, highlighting the urgent need for
practical, resource -efficient, and context -specific analytical frameworks that support SME
marketing strategies  (Kabiraj & Joghee, 2023; Theodorakopoulos & Theodoropoulou, 2024;
Wagobera Edgar Kedi et al., 2024) . Therefore, there is a clear need for a sentiment analysis
approach that is both methodologically transparent and supported by measurable statistical
validation to ensure analytical reliability and practical applicability. This study therefore positions
sentiment analysis as an evaluative engagement performance tool rather than merely an opinion
monitoring technique.
This study aims to identify customer sentiment patterns in Instagram content of SMEs, examine
the role of sentiment analysis as an analytical tool for evaluating customer engagement
performance, and analyze how sentiment polarity influences engagement performance indicators,
as well as provide data -driven recommendations to improve customer interaction strategies. To
achieve these objectives, this study employs text preprocessing techniques, including data
cleaning, tokenization, and stopword removal, follo wed by sentiment classification using a
lexicon-based approach with the VADER (Valence Aware Dictionary and Sentiment Reasoner)
model to analyze Instagram comment data and examine its relationship with engagement metrics
such as interaction rate and comment intensity. In addition, the study incorporates statistical
testing to quantitatively evaluate the significance of relationships bet ween sentiment categories
and engagement indicators, ensuring that findings are empirically validated and not solely
descriptive. This approach strengthens the analytical framework by combining interpretable
sentiment classification with statistically measurable outcomes. By integrating sentiment patterns
with measurable engagement indicators, this research contributes to expanding the theoretical
integration between digital marketing analytics and customer engagement frameworks.
Practically, the study offers an accessible analytical model that SMEs can replicate using available
social media data and limited technological resources. From a managerial perspective, the
findings support evidence -based decision -making processes that strengthen marketing

Instagram Sentiment Analysis for Customer Engagement ...

100      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

effectiveness and customer relationship management within SME environments (Na et al., 2025;
Owusu-Mensah et al., 2025; Pertiwi & Hana, 2025).
This paper is organized into several sections to provide a systematic discussion of the research.
The first section introduces the study background, research problem, and objectives. The second
section reviews relevant literature and theoretical foundation s supporting the study framework.
The third section explains the research methodology, including data collection, preprocessing
techniques, and sentiment analysis procedures. The fourth section presents research findings and
discussion, highlighting the re lationship between sentiment patterns and customer engagement
performance. The final section concludes the study by summarizing key findings, presenting
managerial implications, and suggesting directions for future research.
II. LITERATURE REVIEW
This section synthesizes theoretical foundations and prior empirical studies related to digital
marketing analytics, sentiment analysis, and customer engagement within SME social media
marketing contexts. The discussion provides conceptual justification fo r integrating emotional
sentiment interpretation with measurable engagement performance indicators. By reviewing
multidisciplinary perspectives from marketing analytics, social media marketing, and customer
engagement research, this section establishes the theoretical foundation supporting the analytical
framework of this study. The literature review also highlights existing research limitations and
identifies conceptual gaps that motivate the development of sentiment -based engagement
evaluation models for SMEs.
A. Digital Marketing Analytics and Sentiment Analysis in SME Social Media Marketing
Digital marketing analytics has emerged as a fundamental approach for organizations to interpret
customer behavior and evaluate marketing effectiveness in contemporary digital environments.
The integration of data analytics into marketing activities enable s firms to transform large
volumes of digital interaction data into actionable managerial insights, supporting evidence-based
decision-making processes and improving marketing performance outcomes. Analytics -driven
marketing strategies enhance organization al responsiveness to customer needs while
strengthening long-term competitive advantages through customer-centered marketing practices
(Grandhi et al., 2021; Gupta et al., 2020; Shah & Murthi, 2021) . These analytical approaches
allow businesses to move beyond intuition-based decision-making toward systematic evaluation
of customer interaction patterns and marketing outcomes.
Within the SME context, digital marketing analytics plays a crucial role due to the resource
constraints commonly faced by small businesses. SMEs frequently depend on cost -efficient

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

digital platforms such as social media to conduct promotional activities, maintain customer
relationships, and expand market reach. Social media platforms provide accessible data sources
that allow SMEs to monitor customer interactions and evaluate marketi ng content performance
without requiring sophisticated technological infrastructure. Prior research demonstrates that
digital marketing analytics supports SME growth and sustainability by improving marketing
efficiency and strengthening customer relationsh ip management processes, particularly in
emerging economies experiencing rapid digital transformation (Chatterjee & Kumar Kar, 2020;
Mark Anthony Camilleri, 2019; Patma et al., 2021).
Social media marketing has transformed business -customer communication by enabling
interactive, real-time engagement and personalized marketing communication. Unlike traditional
marketing channels, social media platforms facilitate bidirectional communicat ion that
encourages customer participation, feedback exchange, and community-building activities. These
interactive characteristics significantly contribute to customer relationship development and
brand loyalty formation within digital marketing ecosystem s (Malesev & Cherry, 2021;
Pellegrino & Abe, 2023) . Among various social media platforms, Instagram has gained
substantial popularity as a marketing tool for SMEs due to its visual storytelling capabilities, high
user engagement levels, and user -friendly content creation features that support brand visibi lity
expansion.
Despite the extensive use of Instagram marketing, SMEs commonly evaluate performance using
surface-level engagement metrics such as likes, shares, or interaction rates. These quantitative
indicators often fail to capture customers’ emotional responses and underlying perceptions toward
marketing content. Sentiment analysis provides a complementary analytical approach by enabling
systematic classification of emotional meaning from textual user-generated content using natural
language processing and machine le arning techniques. Broadly, sentiment analysis approaches
can be categorized into lexicon-based methods, which rely on predefined sentiment dictionaries
for polarity detection, and machine learning -based methods, which utilize trained models to
classify sentiment patterns fr om labeled data. Lexicon -based approaches are often preferred in
SME contexts due to their interpretability and lower computational requirements, while machine
learning approaches offer higher adaptability but require larger datasets and training processes .
Through sentiment polarity classification, organizations can interpret customer opinions and
evaluate marketing responses more comprehensively than relying solely on quantitative
engagement indicators (Al-Otaibi & Al-Rasheed, 2022; Chan & Yang, 2023).
In social media marketing research, sentiment analysis has been widely applied to examine
customer opinions, brand perception, and product evaluation across digital platforms. Sentiment-

Instagram Sentiment Analysis for Customer Engagement ...

102      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

based insights support marketing strategy development, customer satisfaction evaluation, and
brand reputation management by revealing emotional interaction patterns embedded in online
discussions. Furthermore, the integration of sentiment analysis into mar keting analytics
frameworks enables predictive marketing strategy development and customer behavior
forecasting (Karayiğit et al., 2022; Smith & Cipolli, 2022). However, sentiment analysis studies
frequently emphasize opinion classification without linking analytical outcomes to engagement
performance evaluation or operational marketing decision -making, particularly within SME
contexts. In addition, prior studies often do not explicitly justify the selection of sentiment
analysis approaches, resulting in limited methodological transparency and difficulty in aligning
analytical techniques with research objectives. In this study, a lexicon -based approach is
positioned as a suitable method due to its transparency, reproducibility, and compatibility with
resource-constrained SME environments.  Instagram provides a data -rich environment that
enables sentiment-based engagement evaluation due to its high comment interaction intensity and
visual-centered communication characteristics, making it particularly suitable as an analytical
environment for evaluating SME digital marketing performance.
B. Customer Engagement Performance in Digital Marketing
Customer engagement is widely conceptualized as a multidimensional construct encompassing
cognitive, emotional, and behavioral interactions between customers and brands. Engagement
reflects customers’ active participation in brand -related activities, including content interaction,
opinion sharing, and brand advocacy behavior, which collectively influence customer loyalty and
long-term business sustainability. Scholars argue that customer engagement represents a strategic
marketing resource that strengthens customer relationships and enhances organizational
competitiveness within digital marketing environments (Barari et al., 2021; Lim et al., 2022). This
multidimensional perspective emphasizes that engagement quality extends beyond interaction
frequency and includes customers’ emotional involvement in brand communication processes.
In digital marketing contexts, customer engagement is strongly influenced by customers’
emotional responses toward marketing content and online interaction experiences. Emotional
engagement shapes customer attitudes toward brands and significantly affects customer decision-
making behavior. Positive emotional engagement may enhance brand trust and encourage
repeated interactions, whereas negative engagement may damage brand reputation and reduce
customer loyalty. Consequently, evaluating customer engagement requires analytical approaches
that capture both interaction frequency and emotional response quality to provide comprehensive
insights into customer-brand relationships (Naumann et al., 2020; Ng et al., 2020).

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

Existing research frequently measures customer engagement using quantitative performance
indicators such as interaction rates, comment frequency, and content reach. Although these
indicators provide measurable engagement outcomes, they do not fully represe nt customers’
emotional perceptions or satisfaction levels. The absence of emotional interpretation within
engagement evaluation frameworks limits the ability of businesses to understand the underlying
motivations driving customer interactions. Integrating  emotional sentiment interpretation into
engagement evaluation frameworks therefore offers deeper analytical insights regarding
customer-brand interaction quality and marketing content effectiveness, particularly when
sentiment analysis is positioned as an  evaluative framework for marketing performance
assessment.
Despite extensive research exploring social media marketing, customer engagement, and
sentiment analysis independently, the integration of these constructs within SME marketing
environments remains limited. Prior studies often evaluate engagement performance based solely
on quantitative interaction metrics while overlooking emotional sentiment interpretation as a
critical determinant of engagement quality. Additionally, sentiment analysis research rarely
positions emotional classification outcomes as evalua tive tools for measuring marketing
performance or developing operational engagement improvement strategies for SMEs (Kabiraj &
Joghee, 2023; Wagobera Edgar Kedi et al., 2024). Furthermore, limited attention has been given
to aligning sentiment analysis methods with statistical evaluation techniques, which is essential
for validating the significance of relationships between sentiment and engagement metrics. This
highlights the n eed for approaches that combine interpretable sentiment classification with
measurable and statistically supported engagement analysis.  These limitations indicate the need
for integrative analytical frameworks that connect sentiment interpretation with measurable
engagement performance indicators. Another research limitation concerns the lack of studies
focusing specifically on Instagram as a single-platform analytical context for evaluating customer
engagement through sentiment analysis. Many existing studies analyze multiple social media
platforms simultaneously, which may reduce analytical depth and limit platform -specific
managerial ap plicability. Considering that many SMEs utilize Instagram as their primary
marketing channel, platform-specific sentiment-based engagement evaluation offers significant
practical relevance for improving SME marketing strategies.
This study addresses these research gaps by positioning sentiment analysis as an evaluative
analytical framework for measuring customer engagement performance in SME Instagram
marketing. By integrating sentiment polarity classification with measurable enga gement
indicators, this research expands digital marketing analytics frameworks and supports data-driven
marketing decision-making processes within SME environments. Specifically, this study adopts

Instagram Sentiment Analysis for Customer Engagement ...

104      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

a lexicon -based sentiment analysis approach integrated with statistical testing to ensure
methodological transparency and empirical validity, thereby addressing limitations identified in
prior literature.  These theoretical perspectives collectively establish the conceptual linkage
between marketing analytics, emotional sentiment interpretation, and engagement performance
measurement within SME digital marketing environments. The conceptual relationship between
digital marketing analytics, sentiment analysis, customer engagement performance, and social
media marketing for SMEs is summarized in Table 1, which presents the theoretical integration
and research implications of each construct. This conceptual framework supports the development
of a practical and resource -efficient analytical model that SMEs can implement using available
social media data and accessible analytical tools.
Table 1. Conceptual Integration of Research Variables
Concept Theoretical Foundation Role in This Study Research Implication
Digital
Marketing
Analytics
Data-driven marketing theory
emphasizes the use of digital data to
evaluate marketing performance
and support managerial decision -
making processes (Gupta et al.,
2020; Shah & Murthi, 2021).
Serves as the primary
analytical framework
that integrates social
media data analysis
into SME marketing
evaluation.
Supports evidence -
based marketing
strategies and enhances
decision quality
through analytical
interpretation of social
media data.
Social
Media
Marketing
for SMEs
Social media enables interactive
communication, brand visibility,
and customer relationship
development within digital
marketing ecosystems (Chatterjee
& Kumar Kar, 2020; Pellegrino &
Abe, 2023).
Provides the
operational context in
which Instagram is
utilized as a marketing
platform for SMEs.
Demonstrates how
SMEs leverage
accessible digital
platforms to strengthen
customer interaction
and market reach.
Customer
Engagement
Performance
Customer engagement theory
conceptualizes engagement as
cognitive, emotional, and
behavioral customer interactions
influencing loyalty and satisfaction
(Barari et al., 2021; Lim et al.,
2022).
Functions as the
primary performance
indicator used to
evaluate the
effectiveness of SME
Instagram marketing
content.
Enables comprehensive
evaluation of customer
interaction quality
beyond quantitative
engagement metrics.
Sentiment
Analysis
Natural language processing and
text mining approaches allow
systematic classification of
customer emotions and opinions
from social media data (Chan &
Yang, 2023; Karayiğit et al., 2022).
Serves as the analytical
tool used to identify
emotional sentiment
patterns within
Instagram user -
generated content.
Provides qualitative
insights into customer
perceptions that
complement
quantitative
engagement
performance
evaluation.
Sentiment-
Based
Engagement
Evaluation
(Proposed
Integration)
Integrative marketing analytics
approach combining emotional
sentiment interpretation with
engagement performance
measurement.
Positions sentiment
analysis as an
evaluative tool rather
than solely opinion
monitoring.
Contributes to
developing practical
and replicable
engagement evaluation
models for SMEs with
limited analytical
resources.

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

III. RESEARCH METHOD/METHODOLOGY
A. Research Design
This study adopts a quantitative, data-driven research design that positions sentiment analysis as
an evaluative analytical tool for assessing customer engagement performance on Instagram. The
design emphasizes the integration of emotional sentiment patter ns derived from user -generated
text with observable engagement indicators, rather than relying solely on descriptive social media
metrics. By utilizing naturally occurring digital trace data from SME Instagram accounts, the
study reflects real -world customer–brand interactions in an authentic digital environment. The
research design explicitly incorporates a structured analytical pipeline consisting of data
collection, preprocessing, sentiment classification, sentiment aggregation, and statistical
evaluation to ensure methodological transparency and replicability. The overall research flow is
illustrated in Figure 1, which outlines the sequential stages from data collection to engagement -
oriented interpretation.
B. Research Approach
The research employs a computational analytics approach grounded in digital marketing analytics
and social media analytics frameworks. This approach enables the systematic extraction,
processing, and interpretation of large -scale textual data generated by Instagram users, aligning
with data -driven decision -making principles in marketing management (Grandhi et al., 2021;
Gupta et al., 2020; Shah & Murthi, 2021) . This study adopts a lexicon-based sentiment analysis
approach using the VADER (Valence Aware Dictionary and Sentiment Reasoner) model
implemented through the Python Natural Language Toolkit (NLTK) library. The method is
unsupervised, where sentiment polarity is determined using a compound sentiment score ranging
from -1 to +1. Following text preprocessing, including data cleaning, tokenization, and stopword
removal, the preprocessed Instagram comment data were processed using VADER to generate a
compound sentiment score for each comment. The resulting compound scores were then
converted into sentiment labels based on the predefined VADER thresholds. Sentiment labels are
assigned based on standard VADER thresholds: compound score ≥ 0.05 is classified as positive,
≤ -0.05 as negative, and values between -0.05 and 0.05 as neutral. Sentiment analysis is used not
merely for opinion detection but to evaluat e how emotional polarity contributes to engagement
performance outcomes. Such an approach is particularly suitable for SMEs that require practical
and scalable analytical methods with limited resources (Kabiraj & Joghee, 2023; Pertiwi & Hana,
2025).
C. Research Type and Design

Instagram Sentiment Analysis for Customer Engagement ...

106      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

This research is classified as applied and explanatory in nature. It seeks to explain how variations
in customer sentiment polarity (positive, neutral, negative) influence observable customer
engagement indicators on Instagram. The design does not involve experimental manipulation or
behavioral surveys but relies on secondary digital data generated through routine social media
interactions. The analytical design follows a non -experimental, cross-sectional structure where
sentiment classification outputs are statistically evaluated against engagement metrics using
inferential techniques. This non-intrusive design enhances ecological validity while maintaining
analytical rigor (Pellegrino & Abe, 2023; Theodorakopoulos & Theodoropoulou, 2024).
D. Population and Sample
The population of this study consists of Instagram content and user interactions associated with
Small and Medium Enterprises (SMEs) operating active business accounts. These SMEs utilize
Instagram as a primary digital marketing channel to promote products , communicate brand
narratives, and engage with customers. The population includes all textual user-generated content
in the form of comments and captions posted within a defined observation period. This population
reflects contemporary digital customer en gagement behavior within SME marketing contexts
(Chatterjee & Kumar Kar, 2020; Patma et al., 2021).
This study employs a purposive sampling technique to select SME Instagram accounts that meet
predefined analytical criteria. The selection criteria include account activity level, consistency of
content posting, and the visibility of customer interaction t hrough comments and likes. This
approach ensures that the sampled accounts reflect genuine engagement -driven communication
rather than inactive or purely promotional profiles. Purposive sampling is appropriate for social
media analytics research where data relevance and interaction richness are prioritized over
probabilistic representativeness (Malesev & Cherry, 2021; Rogers, 2021).
The final dataset consists of 5 SME Instagram accounts, 120 posts, and approximately 3,500 user
comments collected over a three -month observation period (January –March 2025). These
quantities were determined to ensure sufficient textual data for stable sen timent distribution and
statistically meaningful engagement analysis. The defined time frame allows capturing consistent
engagement patterns while minimizing temporal bias.  Rather than emphasizing numerical
representativeness, the study prioritizes analytical adequacy and sentiment distribution stability,
which are common considerations in computational text analysis research  (Al-Otaibi & Al -
Rasheed, 2022; Chan & Yang, 2023).
E. Data Sources and Data Collection Techniques

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

This research relies exclusively on secondary data obtained from publicly accessible Instagram
content. The data includes captions created by SME account owners and comments generated by
users in response to posted content. In this study, sentiment analysi s is applied specifically to
user-generated comments, while post captions are retained as contextual information and are not
included in the sentiment classification.  Utilizing secondary digital data enables the study to
capture authentic customer expressions and spontaneous engagement behavior without researcher
intervention. This approach minimizes response bias and enhances the ecological validity of
customer engagement analysis in social media environments (Rafi et al., 2020; Smith & Cipolli,
2022).

Figure 1. Research Framework and Data Analysis Flow
Data collection is conducted using automated web scraping tools based on Python libraries such
as Instaloader and BeautifulSoup, ensuring compliance with platform accessibility policies.
Inclusion criteria consist of posts with visible engagement (likes and comments), active comment
sections, and content relevance to business promotion, while exclusion criteria include spam

Instagram Sentiment Analysis for Customer Engagement ...

108      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

comments, duplicate entries, and non -textual or irrelevant content. The total dataset comprises
approximately 3,500 cleaned comment entries after preprocessing and filtering procedures. The
collected user -generated comment data undergoes preprocessing proc edures, including text
cleaning, tokenization, normalization, and stopword removal, to improve analytical accuracy.
These preprocessing steps are essential for reducing noise and ensuring reliable sentiment
classification outcomes. The overall data collection and preprocessing workflow is illustrated in
Figure 1.
F. Variables and Operational Definition
This study employs clearly defined independent, dependent, and control variables to ensure
analytical transparency and theoretical alignment. The operationalization of each variable is
grounded in established digital marketing analytics and customer engage ment literature. To
enhance clarity and replicability, all variables, definitions, measurement scales, and data sources
are systematically summarized in Table 2. This table serves as a reference framework for the
subsequent analysis and interpretation stages. The selection of variables is theoretically justified
by the analytical relationship between emotional sentiment (independent variable) and
engagement performance (dependent variable), where sentiment polarity is hypothesized to
influence interaction outcomes such as likes and comments. Control variables such as pos ting
frequency and content type are included to reduce confounding effects and improve analytical
validity. The unit of analysis is the Instagram post, with customer sentiment derived specifically
from user-generated comments associated with each post. This structure ensures that the analysis
captures both emotional and behavioral dimensions of customer engagement.
Table 2. Variables and Operational Definitions
Variable
Type
Variable Operational Definition Measurement
Scale
Data Source
Independent
Variable
Customer
Sentiment
Polarity
Emotional orientation expressed in
Instagram user comments, classified
as positive, neutral, or negative
Nominal Instagram user
comments
Dependent
Variable
Customer
Engagement
Performance
Observable interaction outcomes
reflecting customer participation
with SME Instagram content
Ratio Instagram
analytics
Engagement
Indicator
Number of
Likes
Total likes received per Instagram
post
Ratio Instagram
metrics
Engagement
Indicator
Number of
Comments
Total comments received per
Instagram post
Ratio Instagram
metrics
Control
Variable
Posting
Frequency
Frequency of content uploads within
the observation period
Ratio Instagram
posting history
Control
Variable
Content
Type
Classification of content based on
visual or informational
characteristics
Nominal Instagram
content
attributes
G. Measurement Instruments and Validity/Reliability Testing

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

Sentiment polarity is measured using a nominal scale representing positive, neutral, and negative
categories. In contrast, customer engagement indicators are measured using ratio scales, such as
counts of likes and comments. The combination of nominal and ratio scales enables meaningful
integration of emotional and behavioral engagement dimensions. This measurement structure
supports evaluative comparison between sentiment categories and engagement performance
outcomes (Naumann et al., 2020).
Construct validity is ensured by grounding sentiment and engagement measures in established
digital marketing and customer engagement literature. The operational definitions align with prior
studies that conceptualize engagement as both emotional and behav ioral interaction. Content
validity is further supported by adopting widely recognized sentiment analysis procedures and
preprocessing standards. Model validity is strengthened by using the VADER sentiment model,
which has been empirically validated for social media text and informal language contexts. In this
study, VADER is applied consistently to the preprocessed user -generated Instagram comments
using its standard compound-score classification thresholds, ensuring that the same classification
procedure is applied across the dataset. These measures en sure that the analytical instruments
accurately represent the theoretical constructs under investigation (Lim & Rasul, 2022; Ng et al.,
2020).
Reliability is assessed by examining the consistency of sentiment classification results across the
dataset. The deterministic scoring mechanism of the lexicon -based model ensures consistent
outputs for identical textual inputs without model retraining variability. Therefore, reliability in
this study is supported by the consistent application of the same preproc essing procedures,
VADER model, and classification thresholds to all analyzed comments. This approach aligns with
prior sentiment-based marketing analytics studies (Chan & Yang, 2023; Wagobera Edgar Kedi et
al., 2024).
H. Data Analysis Techniques
The study employs computational sentiment classification techniques based on a lexicon -based
approach. The analytical process follows a step -by-step pipeline: (1) data collection from
Instagram, (2) preprocessing and text normalization, (3) sentiment scori ng using VADER, (4)
aggregation of sentiment categories at post level, and (5) statistical analysis linking sentiment
categories with engagement metrics. Engagement metrics are subsequently analyzed to evaluate
how sentiment variations correspond with enga gement performance indicators. To enhance
analytical rigor, inferential statistical methods are applied, including one-way ANOVA to test
whether engagement metrics differ significantly across the positive, neutral, and negative
sentiment categories, and Pearson correlation analysis to examine the strength and direction of

Instagram Sentiment Analysis for Customer Engagement ...

110      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

the linear relationship between continuous VADER sentiment scores and engagement indicators.
These statistical techniques ensure that the findings are not merely descriptive but supported by
empirical significance testing. This integrative analytical process positions sentiment analysis as
an evaluative framework rather than a descriptive opinion -monitoring tool (Kabiraj & Joghee,
2023; Owusu-Mensah et al., 2025).
I. Mathematical Formulas or Models (if applicable)
Customer engagement performance is quantified using an interaction rate formula that relates
observable user interactions to the size of the account audience. The interaction rate provides a
normalized engagement indicator that allows comparison across pos ts and SME accounts with
different follower bases. This metric is commonly used in social media analytics to evaluate
engagement effectiveness beyond absolute interaction counts. By normalizing engagement
outcomes, the formula supports evaluative analysis and cross-account comparability.
The interaction rate formula applied in this study is expressed as follows:
Interaction Rate (%) = Number of Likes + Number of Comments Number of Followers  ×  100
where the numerator represents the total observable interactions generated by a post, consisting
of the number of likes and comments, while the denominator represents the total number of
followers of the corresponding SME Instagram account. The resulting v alue is expressed as a
percentage and represents the proportion of the account audience that generated observable
interactions with the post. This formula is further utilized as a dependent variable in statistical
testing (ANOVA and correlation analysis) to evaluate whether sentiment polarity is significantly
associated with normalized engagement performance. This formulation enables transparent  and
interpretable assessment of engagement performance.
J. Ethical Considerations
This study utilizes publicly available Instagram data and does not involve direct interaction with
human subjects. Ethical approval is therefore not required. All data are anonymized, and findings
are reported in aggregated form to protect user privacy. Th is approach aligns with ethical
standards for social media analytics and responsible digital marketing research (Álvarez &
Hassan, 2025).
IV. RESULT/FINDINGS AND DISCUSSION
A. Result

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

This section reports descriptive statistics derived from Instagram posts and user interaction data
associated with SME accounts. The descriptive analysis summarizes customer sentiment polarity
and observable engagement indicators, including the number of likes, number of comments, and
interaction rate. All reported values are aggregated in the form of averages to ensure comparability
across posts and sentiment categories. Unlike prior descriptive-only reporting, this study presents
numerical values to enable precise comparison and support subsequent statistical testing. The
presentation of results is initially descriptive before proceeding to inferential evaluation.
Table 3 presents the descriptive statistics of customer sentiment polarity and customer
engagement indicators. Instagram posts are classified into three sentiment categories, namely
positive, neutral, and negative sentiment, based on sentiment analysis results. For each sentiment
category, the table reports the average number of likes, average number of comments, and average
interaction rate. The table also reports the number of observations (n) and standard deviations
(SD) for each engagement indicator to provide a more complete quantitative comparison across
sentiment categories. These indicators represent measurable engagement outcomes direc tly
obtained from the dataset.
Table 3. Descriptive Statistics of Sentiment Polarity and Customer Engagement Indicators
Sentiment
Polarity
n Average
Likes
SD Average
Comments
SD Average
Interaction
Rate
SD
Positive 50 128 24.61 34 8.42 3.2% 0.71%
Neutral 40 79 18.37 18 5.63 2.1% 0.54%
Negative 30 42 12.84 9 3.27 1.3% 0.39%
The descriptive statistics indicate variation in engagement indicator values across sentiment
polarity categories. Average values of likes, comments, and interaction rates differ across
positive, neutral, and negative sentiment groups. Positive sentiment c ategories are characterized
by the highest average values, followed by neutral and negative sentiment categories. This pattern
suggests a consistent gradient relationship between sentiment polarity and engagement intensity
prior to statistical validation. These statistics summarize engagement-related observations across
sentiment classifications.
Following the descriptive overview, inferential analysis is conducted to examine relational
patterns between sentiment polarity categories and customer engagement indicators. The analysis
relies on naturally occurring Instagram interaction data and does no t involve experimental
manipulation or survey -based measurement. A one -way ANOVA test is applied to evaluate
whether differences in engagement metrics across sentiment categories are statistically
significant. The ANOVA results indicate a statistically significant difference in interaction rates
across sentiment groups (F = 12.47, p < 0.01). This result indicates that engagement levels differ

Instagram Sentiment Analysis for Customer Engagement ...

112      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

significantly across sentiment categories, rather than establishing a causal effect of sentiment
polarity on engagement performance.
Table 4. One-Way ANOVA Results for Interaction Rate Across Sentiment Categories
Source SS df MS F p-value
Between Groups 11.84 2 5.92 12.47 <0.001
Within Groups 55.43 117 0.474 — —
Total 67.27 119 — — —
In addition, Pearson correlation analysis reveals a positive relationship between the continuous
VADER sentiment scores and engagement metrics (r = 0.62, p < 0.01), indicating that higher
positive sentiment scores are associated with increased engagement l evels. The correlation
coefficient indicates a moderate -to-strong positive association between sentiment score and
engagement.
Table 5. Pearson Correlation between VADER Sentiment Score and Engagement
Variables Pearson r p-value
VADER Sentiment Score – Interaction Rate 0.62 <0.001
Post-hoc comparisons using Tukey HSD further indicate that the positive –neutral and positive–
negative comparisons show statistically significant differences, while the neutral –negative
comparison shows a smaller difference.
Table 6. Tukey HSD Post-Hoc Comparisons Across Sentiment Categories
Comparison Mean Difference p-value Interpretation
Positive – Neutral 1.10% <0.01 Significant
Positive – Negative 1.90% <0.001 Significant
Neutral – Negative 0.80% 0.06 Not significant
Taken together, the inferential results provide statistical evidence of differences in engagement
across sentiment categories and a positive association between continuous sentiment scores and
engagement. These findings strengthen the descriptive results by demonstrating that the observed
patterns are supported by inferential statistical analysis.
B. Discussion
This study interprets the results by situating them within the broader context of digital marketing
analytics and customer engagement research. The findings emphasize the relevance of emotional
orientation as an analytical dimension for examining customer engagement on SME Instagram
accounts. By integrating sentiment polarity with conventional engagement indicators, the study
demonstrates that engagement assessment can incorporate both behavioral interaction metrics and
affective textual characteristics. The statistically significant ANOVA results indicate that
engagement levels differ significantly across sentiment polarity groups, providing inferential
support for differences observed in the descriptive results. However, because the study uses

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

naturally occurring, non -experimental Instagram data, these results should be interpreted as an
association between sentiment polarity and engagement rather than as evidence that sentiment
polarity directly causes changes in engagement. This supports the conceptualization of customer
engagement as a multidimensional construct rather than a solely quantitative outcome (Naumann
et al., 2020; Ng et al., 2020).
The use of sentiment analysis as an evaluative analytical tool provides an additional interpretive
layer to engagement assessment. Rather than substituting traditional metrics, sentiment polarity
contextualizes engagement indicators by capturing emotional characteristics embedded in user -
generated text. The positive correlation (r = 0.62) indicates that higher VADER sentiment scores
are positively associated with stronger user interaction, suggesting that emotional orientation may
be related to engagement behavior. Positive sentiment may be associated with greater willingness
to interact because favorable customer expressions can reflect satisfaction, interest, or perceived
relevance of the content. In contrast, neutral sentiment may reflect lower emotional involvement,
while negative sentiment may indicate dissatisfaction or criticism that can be expressed through
engagement but does not necessarily translate into positive customer interaction. Users are more
likely to interact with content that aligns with positive affect, reinforcing visibility through
platform algorithms and social validation mechanisms. Therefore, the findings should be
interpreted as evidence of an observed sentiment –engagement association rather than
confirmation that positive sentiment itself causes higher engagement. Consequently, sentiment
analysis functions as an analytical enhancement within digital marketing analytics frameworks
(Gupta et al., 2020; Shah & Murthi, 2021).
The findings are consistent with prior research emphasizing the importance of emotional
dimensions in social media-based customer engagement. Previous studies have primarily focused
on observable engagement metrics such as likes, comments, and shares, ofte n without
incorporating sentiment polarity as part of engagement evaluation (Chatterjee & Kumar Kar,
2020; Patma et al., 2021) . However, unlike earlier studies that provide descriptive insights, this
study demonstrates statistically significant differences across sentiment groups, thereby
strengthening empirical validation of the sentiment –engagement relationship. By explicitly
integrating sentiment categories with engagement indicators, this study extends metric -centered
analytical approaches. The results contribute to literature recognizing emotional content as an
integral component of engagement analysis.
In addition, the study aligns with sentiment analysis research highlighting the analytical value of
text mining techniques in social media contexts (Chan & Yang, 2023; Karayiğit et al., 2022) .
Unlike earlier studies that emphasize opinion classification, this research focuses on SMEs and

Instagram Sentiment Analysis for Customer Engagement ...

114      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

positions sentiment analysis as a practical evaluative mechanism. The observed differences across
sentiment categories suggest that positive, neutral, and negative customer expressions may
correspond to different levels of engagement intensity. Positive sentiment may reflect satisfaction
or favorable responses toward SME content, which can coincide with stronger interaction. Neutral
sentiment may indicate informational or less emotionally involved responses, whereas negative
sentiment may reflect dissatisfaction, criticism, or service -related concerns. These differences
provide a possible explanation for the observed variation in engagement across sentiment groups
without implying a direct causal mechanism. For SMEs, this distinction is important because a
high number of comments alone does not necessarily indicate favorab le customer engagement;
the emotional orientation of those comments provides additional context for interpreting
interaction performance.
From a theoretical standpoint, the study contributes to customer engagement theory by reinforcing
its multidimensional nature. The findings support engagement frameworks that conceptualize
engagement as a combination of emotional expression and observable interaction behavior
(Barari et al., 2021; Lim et al., 2022) . The statistically validated relationship between sentiment
and engagement provides empirical evidence linking affective and behavioral dimensions,
strengthening theoretical integration. Sentiment polarity serves as an analytical linkage between
affective engagement and behavioral engagement indicators. This integration advances
theoretical understanding of engagement dynamics within social media environments.
Furthermore, the study contributes to digital marketing analytics literature by positioning
sentiment analysis as an evaluative mechanism rather than an outcome variable. By embedding
sentiment polarity within engagement assessment, the study responds to calls for emotion-aware
and data-driven analytical frameworks. The use of inferential statistics, including ANOVA and
correlation analysis, addresses prior limitations of descriptive -only studies and enhances
methodological rigor.  This theoretical repositioning strengthens the connection between text
mining methodologies and engagement theory. It also provides a foundation for future research
integrating emotional analytics into marketing performance evaluation models  (Grandhi et al.,
2021; Vollrath & Villegas, 2022).
The findings offer practical implications for SMEs seeking to evaluate customer engagement on
Instagram. SMEs can incorporate sentiment analysis to assess the emotional characteristics of
customer interactions alongside conventional engagement metrics. Rather than simply prioritizing
positive sentiment, SMEs can use sentiment analysis to evaluate content performance by
comparing sentiment patterns with engagement indicators. Positive sentiment can be monitored
to identify content themes associated with favorable customer responses, while negative

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

sentiment can be used to identify posts or topics that require further evaluation. The evidence that
positive sentiment is associated with higher engagement suggests that SMEs should prioritize
emotionally appealing content strategies, such as storytelling , customer appreciation posts, and
positive brand narratives. At the same time, negative sentiment should not simply be treated as
undesirable engagement because negative comments may reveal customer complaints, service
problems, or unmet expectations that require managerial attention. This approach enables a more
comprehensive evaluation of content performance beyond interaction counts alone. As a result,
SMEs can gain deeper insight into how emotional responses align with engagement outcomes.
Additionally, the study demonstrates that sentiment -based engagement evaluation can be
implemented using accessible data and scalable analytical techniques. This is particularly relevant
for SMEs with limited analytical resources. By integrating sentiment analysis into routine
engagement assessment, SMEs can support data-driven decision making in content development
and customer interaction management. In practical terms, SMEs can use the analysis for three
related activities: (1) content evaluation by comparing sentiment patterns and engagement across
posts, (2) complaint monitoring by identifying recurring negative sentiment and topics requiring
customer-service attention, and (3) content planning by identifying content themes associated
with favorable sentiment and stronger engagement. The statistically validated framework ensures
that managerial decisions are supported by empirical evidence rather than intuition alone,
improving marketing effectiveness and strategic alignment. This approach aligns with
contemporary digital marketing pr actices emphasizing analytics -driven strategy formulation
(Pertiwi & Hana, 2025; Wagobera Edgar Kedi et al., 2024).
Limitations and Future Research Directions
Despite its contributions, this study has several limitations. The analysis is confined to Instagram
as a single social media platform, which may limit the generalizability of the findings to other
digital environments. In addition, sentiment analysis is based solely on textual data and does not
account for visual or multimodal content elements. These limitations reflect methodological
constraints commonly observed in social media analytics research.
Future research may address these limitations by incorporating image -based or multimodal
sentiment analysis approaches. Cross -platform comparative studies could also be conducted to
examine whether similar sentiment –engagement patterns emerge across differ ent social media
platforms. Further studies may also apply advanced machine learning models such as deep
learning-based sentiment classifiers to compare performance with lexicon-based approaches and
enhance analytical robustness.  Longitudinal research designs may further explore changes in
sentiment–engagement relationships over time. Such extensions would enhance the robustness

Instagram Sentiment Analysis for Customer Engagement ...

116      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

and applicability of sentiment-based engagement evaluation models for SMEs (Rogers, 2021; Ye
et al., 2024).
V. CONCLUSION AND RECOMMENDATION
This study concludes that Instagram sentiment analysis can be systematically positioned as an
evaluative tool for assessing customer engagement performance in SMEs. By integrating
sentiment polarity derived from user-generated text with observable engagement indicators such
as likes, comments, and interaction rates, the findings demonstrate that emotional orientation
represents a relevant analytical dimension within digital marketing analytics. Using a lexicon -
based VADER sentiment analysis approach combined with inferential statistical testing (ANOVA
and correlation analysis), the study provides a methodologically transparent and empirically
validated framework for linking sentiment polarity with engagement performance. The study
achieves its objectives by identifying sentiment patterns in SME Instagram content and explaining
how these patterns can be linked to measurable engagement outcomes. The statistically significant
differences across sentiment categories (p < 0.01) indicate that engagement levels differ
significantly across sentiment categories and are significantly associated with sentiment polarity,
rather than confirming a causal effect of sentiment polarity on engagement indicators. In doing
so, it addresses the identified research gap by moving beyond metric -centered evaluation and
framing sentiment analysis as a structured component of engagement performance assessment in
the SME context.
Practically, SMEs are recommended to incorporate sentiment analysis into routine social media
evaluation processes in order to complement conventional quantitative metrics with affective
insights. This approach enables more comprehensive, data -driven decision making in content
development and customer interaction management while remaining feasible for organizations
with limited analytical resources. Given the empirical evidence that positive sentiment is
associated with significantly higher engagement levels, SMEs should prioritize content strategies
that foster positive emotional responses to maximize interaction outcomes. Furthermore, the use
of a transparent and replicable analytical pipeline ensures that SMEs can ado pt this approach
without requiring complex machine learning infrastructure, making it suitable for resource -
constrained environments. Future research should expand this framework through multimodal
sentiment analysis, cross -platform comparisons, and longit udinal designs to strengthen
generalizability and theoretical refinement. Such extensions would further consolidate the role of
sentiment-based analytics in improving customer engagement strategies within SME digital
marketing environments.
Statement on the Use of Artificial Intelligence Tools

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

The authors declare that artificial intelligence tools, including ChatGPT, were utilized solely to
enhance the linguistic quality and readability of the manuscript. The intellectual substance of the
work including research conceptualization, methodological  design, data collection, analytical
procedures, interpretation of findings, and development of conclusions was produced entirely by
the authors without the involvement of AI systems. The authors accept full responsibility for the
authenticity, accuracy, and academic integrity of the manuscript submitted to the Journal of
Management and Informatics.
REFERENCES
Al-Otaibi, S., & Al -Rasheed, A. (2022). A Review and Comparative Analysis of Sentiment
Analysis Techniques. In Informatica (Slovenia) (Vol. 46, Number 6, pp. 33 –44). Slovene
Society Informatika. https://doi.org/10.31449/inf.v46i6.3991
Álvarez, M., & Hassan, L. (2025). Exploring the Role of Digital Tools in Ethical Managerial
Decision-Making. Journal of Management and Informatics , 4(3), 998 –1016.
https://doi.org/10.51903/jmi.v4i3.306
Barari, M., Ross, M., Thaichon, S., & Surachartkumtonkun, J. (2021). A meta -analysis of
customer engagement behaviour. International Journal of Consumer Studies , 45(4), 457–
477. https://doi.org/10.1111/ijcs.12609
Chan, C. -P., & Yang, J. -H. (2023). Instagram Text Sentiment Analysis Combining Machine
Learning and NLP. ACM Transactions on Asian and Low-Resource Language Information
Processing. https://doi.org/10.1145/3606370
Chatterjee, S., & Kumar Kar, A. (2020). Why do small and medium enterprises use social media
marketing and what is the impact: Empirical insights from India. International Journal of
Information Management, 53. https://doi.org/10.1016/j.ijinfomgt.2020.102103
Grandhi, B., Patwa, N., & Saleem, K. (2021). Data-driven marketing for growth and profitability.
EuroMed Journal of Business , 16(4), 381 –398. https://doi.org/10.1108/EMJB -09-2018-
0054
Gupta, S., Leszkiewicz, A., Kumar, V., Bijmolt, T., & Potapov, D. (2020). Digital Analytics:
Modeling for Insights and New Methods. Journal of Interactive Marketing , 51, 26 –43.
https://doi.org/10.1016/j.intmar.2020.04.003
Kabiraj, S., & Joghee, S. (2023). Improving Marketing Performance: How Business Analytics
contribute to Digital Marketing. International Journal of Technology, Innovation and
Management (IJTIM), 3(1), 9–18. https://doi.org/10.54489/ijtim.v3i1.209
Karayiğit, H., Akdagli, A., & Acı, Ç. İ. (2022). BERT -based Transfer Learning Model for
COVID-19 Sentiment Analysis on Turkish Instagram Comments. Information Technology
and Control, 51(3), 409–428. https://doi.org/10.5755/j01.itc.51.3.30276

Instagram Sentiment Analysis for Customer Engagement ...

118      Journal of Management and Informatics (JMI), Vol. 5 No. 2 August 2026

Lim, W. M., & Rasul, T. (2022). Customer engagement and social media: Revisiting the past to
inform the future. Journal of Business Research , 148, 325 –342.
https://doi.org/10.1016/j.jbusres.2022.04.068
Lim, W. M., Rasul, T., Kumar, S., & Ala, M. (2022). Past, present, and future of customer
engagement. Journal of Business Research , 140, 439 –458.
https://doi.org/10.1016/j.jbusres.2021.11.014
Malesev, S., & Cherry, M. (2021). Digital and social media marketing-growing market share for
construction smes. Construction Economics and Building , 21(1), 65 –82.
https://doi.org/10.5130/AJCEB.v21i1.7521
Mark Anthony Camilleri, B. (2019). The Use of Data-Driven Technologies for Customer-Centric
Marketing. In International Journal of Big Data Management. Forthcoming.
Na, I. H., Jae, Y. I., & Hwa, P. I. (2025). Personalized Digital Marketing Strategies: A Data -
Driven Approach Using Marketing Analytics. Journal of Management and Informatics ,
4(1), 668–686. https://doi.org/10.51903/jmi.v4i1.149
Naumann, K., Bowden, J., & Gabbott, M. (2020). Expanding customer engagement: the role of
negative engagement, dual valences and contexts. European Journal of Marketing , 54(7),
1469–1499. https://doi.org/10.1108/EJM-07-2017-0464
Ng, S. C., Sweeney, J. C., & Plewa, C. (2020). Customer engagement: A systematic review and
future research priorities. Australasian Marketing Journal , 28(4), 235 –252.
https://doi.org/10.1016/j.ausmj.2020.05.004
Owusu-Mensah, D., Sarfo, P. A., & Kusi, G. A. (2025). Exploring the Impact of Artificial
Intelligence on Customer Experience Personalization and Marketing Strategy Optimization
in Digital Marketing: An Empirical Analysis. Journal of Management and Informatics, 4(2),
822–843. https://doi.org/10.51903/jmi.v4i2.242
Patma, T. S., Wardana, L. W., Wibowo, A., Narmaditya, B. S., & Akbarina, F. (2021). The impact
of social media marketing for Indonesian SMEs sustainability: Lesson from Covid -19
pandemic. Cogent Business and Management , 8(1).
https://doi.org/10.1080/23311975.2021.1953679
Pellegrino, A., & Abe, M. (2023). Leveraging Social Media for SMEs: Findings from a
Bibliometric Review. In Sustainability (Switzerland)  (Vol. 15, Number 8). MDPI.
https://doi.org/10.3390/su15087007
Pertiwi, J. P., & Hana, A. U. (2025). Data-Driven Decision Making in MSMEs: Leveraging Free
Analytics Tools for Financial Planning and Efficiency. Journal of Management and
Informatics, 4(1), 633–648. https://doi.org/10.51903/jmi.v4i1.146
Rafi, A. M., Rana, S., Kaur, R., Wu, Q. M. J., & Zadeh, P. M. (2020). Understanding Global
Reaction to the Recent Outbreaks of COVID -19: Insights from Instagram Data Analysis .
http://arxiv.org/abs/2009.06862

Journal of Management and Informatics (JMI)
Vol. 5 No. 2 August 2026
E-ISSN: 2961-7731; P-ISSN: 2961-7472, Pages 97-119

Rogers, R. (2021). Visual media analysis for Instagram and other online platforms. Big Data and
Society, 8(1). https://doi.org/10.1177/20539517211022370
Shah, D., & Murthi, B. P. S. (2021). Marketing in a data -driven digital world: Implications for
the role and scope of marketing. Journal of Business Research , 125, 772 –779.
https://doi.org/10.1016/j.jbusres.2020.06.062
Smith, H., & Cipolli, W. (2022). The Instagram/Facebook ban on graphic self -harm imagery: A
sentiment analysis and topic modeling approach. Policy and Internet , 14(1), 170 –185.
https://doi.org/10.1002/poi3.272
Theodorakopoulos, L., & Theodoropoulou, A. (2024). Leveraging Big Data Analytics for
Understanding Consumer Behavior in Digital Marketing: A Systematic Review. In Human
Behavior and Emerging Technologies  (Vol. 2024). John Wiley and Sons Inc.
https://doi.org/10.1155/2024/3641502
Vollrath, M. D., & Villegas, S. G. (2022). Avoiding digital marketing analytics myopia: revisiting
the customer decision journey as a strategic marketing framework. Journal of Marketing
Analytics, 10(2), 106–113. https://doi.org/10.1057/s41270-020-00098-0
Wagobera Edgar Kedi, Chibundom Ejimuda, Courage Idemudia, & Tochukwu Ignatius Ijomah.
(2024). Machine learning software for optimizing SME social media marketing campaigns.
Computer Science & IT Research Journal , 5(7), 1634 –1647.
https://doi.org/10.51594/csitrj.v5i7.1349
Ye, C., Kim, Y., & Cho, Y. N. (2024). Digital Marketing and Analytics Education: A Systematic
Review. Journal of Marketing Education , 46(1), 32 –44.
https://doi.org/10.1177/02734753231166414
