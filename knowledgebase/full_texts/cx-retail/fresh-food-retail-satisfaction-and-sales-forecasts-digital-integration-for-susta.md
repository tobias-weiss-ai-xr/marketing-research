---
title: 'Fresh food retail satisfaction and sales forecasts: digital integration for sustainability in
  Guiyang, China'
url: https://doi.org/10.3389/fsufs.2026.1866736
category: cx-retail
subcategory: empirical
date: 2026-07
venue: Frontiers in Sustainable Food Systems
authors:
- Changpeng Yang
- Keyan He
- Fu Hong
source: openalex-oa
pdf_url: https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2026.1866736/pdf
pages: 21
chars: 100352
fetched_at: '2026-11-08T18:19:08+00:00'
kb_version: 1
---

# Fresh food retail satisfaction and sales forecasts: digital integration for sustainability in Guiyang, China

Frontiers in Sustainable Food Systems 01 frontiersin.org
Fresh food retail satisfaction and
sales forecasts: digital integration
for sustainability in Guiyang,
China
Changpeng Yang 1†, Keyan He 2†, Fu Hong 3†, Yufeng Zhu 4 and
Liming Chen 1*
1School of Tourism and Resource Environment, Qiannan Normal University for Nationalities, Duyun,
China, 2Party School of the Libo County Committee of the Communist Party of China, Libo, Guizhou,
China, 3School of Digital and Statistical Sciences, Guizhou University of Finance and Economics,
Guiyang, China, 4Shandong Youth University of Political Science, School of Modern Service
Management, Jinan, Shandong, China
Introduction: Driven by the digital economy, China’s fresh food retail sector is
accelerating its transition toward omnichannel integration. However, existing
research has largely focused on first-tier cities in eastern China, paying insuffi -
cient attention to the heterogeneity of underdeveloped regions in southwestern
China, and lacking a systematic analytical framework that integrates multi-source
data and multiple methodologies.
Methods: This study takes six mainstream online fresh food platforms in Guiyang,
China (including the local platform ‘Guihuihui’) as its research subjects. By integrating
two rounds of stratified sampling questionnaire surveys (1,744 valid responses) with
16,321 online review data points, we constructed a multi-model integrated analyti-
cal framework comprising an LDA topic model, an improved intuitive fuzzy TOPSIS
method, and the AT-DeepAR deep learning model. This framework was used to sys-
tematically investigate the mechanisms underlying the evolution of fresh food retail
formats, the factors influencing consumer satisfaction, and market sales forecasting.
Results: The study found that: (1) transaction costs and service quality are the core
drivers of digital transformation in fresh food retail, with consumers placing the great-
est emphasis on delivery speed and shopping experience; (2) platform satisfaction
rankings are as follows: Duoduo Grocery > Meituan Youxuan > JD NOW > Freshippo
> Guihuihui > Dingdong Maicai, with national platforms enjoying significantly higher
brand recognition than local platforms; (3) the AT-DeepAR model, incorporating an
attention mechanism, can accurately capture the seasonal fluctuations in fresh pro-
duce sales, with predicted values closely matching actual figures (within a 95% confi-
dence interval). It forecasts that the average monthly sales of fresh produce platforms
in Guiyang will steadily increase to approximately 340 million yuan by 2025.
Discussion: At the theoretical level, this paper fills a research gap on fresh food
e-commerce in southwestern China by establishing an integrated analytical paradigm
combining questionnaire data, text mining, and deep learning. At the practical level,
it provides empirical evidence to support differentiated competition, transaction cost
optimization, and the digital upgrading of the regional fresh food industry for local
platforms in Guiyang. It holds significant practical value for promoting the sustain-
able development of fresh food retail, enhancing the efficiency of urban–rural food
distribution, and facilitating the low-carbon transition of supply chains.
KEYWORDS
AT-DeepAR, consumer satisfaction, digital economy, fresh food retail, Guiyang,
LDA-intuitive fuzzy TOPSIS, multi-model analysis, sustainability
TYPE Original Research
PUBLISHED 02 July 2026
DOI 10.3389/fsufs.2026.1866736
OPEN ACCESS
EDITED BY
Ivan Antonio Garcia-Montalvo,
National Institute of Technology of
Mexico, Mexico
REVIEWED BY
Jessa Frida Festijo,
Lyceum of the Philippines University,
Philippines
Oliver Eboy,
Universiti Malaysia Sabah, Malaysia
*CORRESPONDENCE
Liming Chen
 slmyyaxx@163.com
†These authors share first authorship
RECEIVED 27 April 2026
REVISED 01 June 2026
ACCEPTED 10 June 2026
PUBLISHED 02 July 2026
CITATION
Yang C, He K, Hong F, Zhu Y and
Chen L (2026) Fresh food retail
satisfaction and sales forecasts: digital
integration for sustainability in Guiyang,
China.
Front. Sustain. Food Syst. 10:1866736.
doi: 10.3389/fsufs.2026.1866736
COPYRIGHT
© 2026 Yang, He, Hong, Zhu and Chen.
This is an open-access article distributed
under the terms of the Creative
Commons Attribution License (CC BY).
The use, distribution or reproduction in
other forums is permitted, provided the
original author(s) and the copyright
owner(s) are credited and that the
original publication in this journal is
cited, in accordance with accepted
academic practice. No use, distribution
or reproduction is permitted which does
not comply with these terms.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 02 frontiersin.org
1 Introduction
The rapid development of internet technology and shifts in con-
sumer behavior have made online shopping an integral part of daily
life. Against this backdrop, online fresh food shopping has emerged
and is growing rapidly. As a key province in south-western China,
Guizhou has seen sustained growth in the demand for fresh produce
in recent years, driven by both urbanization and consumption
upgrades (Guizhou Provincial Bureau of Statistics, Guizhou Provincial
Office of the Leading Group for the Seventh National Population
Census, 2021). Fueled by the pandemic, more consumers have turned
to ‘online shopping’ , presenting numerous challenges to traditional
fresh food retail models, which suffer from low delivery efficiency,
high costs and a lack of personalized service.
In recent years, the evolution of the fresh food retail sector has
become increasingly evident. Traditional farmers’ markets and super-
markets have gradually shifted from offline to online operations, while
new retail models such as front-end warehouses (e.g., Freshippo,
Dingdong Maicai) and community group-buying platforms (e.g.,
Meituan Y ouxuan, Duoduo Grocery) have rapidly emerged. These
platforms meet consumers’ demands for timeliness and convenience
through an ‘online ordering + offline delivery’ model, making the inte-
grated online-offline retail model increasingly prominent.
Against this background, Guizhou Province launched the
“Guihuihui” online fresh produce platform in 2022, integrating high-
quality fresh produce resources from Guiyang and its surrounding
areas (Zhongwang News, 2022). The platform breaks through the spa-
tial and temporal barriers of traditional retail, centring on the digital
reconstruction of the “people-goods-place” model to drive the trans-
formation of supermarket retail formats. Through efficient service and
high-quality products, it has rapidly gained market recognition and
consumer trust, demonstrating strong growth momentum.
As a critical link in the food supply chain, the digital transforma-
tion and service optimization of fresh food retail have a direct bearing
on food security, resource conservation, the reduction of wastage and
losses, and the improvement of the quality of life for urban and rural
residents. This study focuses on consumer groups in Guiyang, China,
conducting an empirical analysis of consumer satisfaction through a
questionnaire survey (Hongxin and Yuhui, 2015). It examines online
fresh produce platforms in Guiyang, analyses the evolution of the
fresh produce retail sector, explores the extent to which these plat-
forms meet consumer needs and their impact on market development,
reviews the current state of the fresh produce market, identifies short-
comings, and offers constructive suggestions and references for the
market’s future development.
2 Literature review
Driven by the dual forces of the digital economy and consumption
upgrades, China’s fresh food retail sector is rapidly shifting from tra-
ditional offline models toward diverse business formats such as
omnichannel integration, community group buying and forward-
depot models. Online fresh food retail has become the mainstream
consumption channel due to its convenience, efficiency and value for
money. The evolution of fresh food retail formats is the result of the
combined influence of transaction costs, digital technology, cold-
chain logistics and consumer behavior, whilst consumer satisfaction
serves as a core indicator influencing repeat purchases and brand loy-
alty. Existing research has yielded substantial findings regarding the
mechanisms of business model evolution, factors influencing satisfac-
tion, evaluation models and sales forecasting; however, studies have
generally focused on first-tier cities in the east and national platforms.
There remains a notable lack of integrated research that targets south-
western China, focuses on provincial capitals, compares local and
national platforms, and combines multi-source data with multiple
methodologies. This paper systematically reviews the relevant litera-
ture and identifies research gaps, thereby providing a theoretical foun-
dation for subsequent empirical analysis.
2.1 Research on the evolution of fresh
produce retail formats
2.1.1 The evolutionary trajectory of fresh produce
retail formats
Existing literature has established a relatively systematic research
framework concerning the evolution of fresh produce retail formats.
This framework primarily unfolds along three main threads: the
iteration of new retail models, the integration of digital technologies,
and consumer behavior-driven trends. It provides a theoretical foun-
dation for understanding the transformation of China’s fresh pro-
duce distribution system from traditional channels toward an
integrated online-offline model characterized by intelligence, effi -
ciency and diverse coexistence. Regarding new retail models and
business formats, the digital economy has driven the rapid prolifera-
tion of models such as forward-depot logistics, store-warehouse
integration and community group buying, which have become the
core directions for business format upgrading. Relevant studies,
using cases such as Freshippo, have revealed the organizational logic,
supply chain coordination and fulfilment efficiency characteristics
of new retail models ( Chen et al., 2022 ; Zhang et al., 2024 ).
Omnichannel integration is regarded as a core feature of new retail,
capable of significantly enhancing consumer engagement and chan-
nel loyalty (Chen et al., 2022) Meanwhile, traditional farmers’ mar-
kets have achieved modernisation through semi-formalization,
forming a complementary and co-existing relationship with e-com-
merce platforms ( Y ao, 2025; Yuan et al., 2026 ). The retail sector’s
overall evolution toward digitalisation, sustainability, platformisa -
tion and ecosystem-based models aligns closely with the reality of
multi-platform coexistence in Guiyang ( Akhtoian, 2023). In terms
of digital technology integration, big data, artificial intelligence and
supply chain optimization are deeply intertwined, driving the fresh
produce retail sector toward precision and intelligence. Blockchain
and green low-carbon technologies help reduce coordination costs
and enhance supply chain transparency ( Chen and Yin, 2023); the
integration of online and offline channels significantly improves ser-
vice quality and customer loyalty ( Zhang and Liang, 2023 ); deep
learning models based on LSTM and GWO-LSTM have been widely
applied to sales forecasting and pricing optimization ( Wang et al.,
2024). Innovations in logistics models and carbon reduction prac -
tices play a crucial role in ensuring fresh produce quality and stabi -
lizing supply (He and Sun, 2025 ). On the consumer-driven front,
consumption preferences, value perceptions and channel choices
directly shape the retail landscape. Research indicates that segmenta-
tion of consumption motives, quality demands, freshness prefer -
ences and price sensitivity significantly influence channel decisions

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 03 frontiersin.org
(Kamal, 2025; Naveuler, 2025; Sarker et al., 2024), whilst consump-
tion upgrades are driving the fresh produce supply chain toward
greater health-consciousness, experiential value and immediacy
(White, 2022). These findings provide the theoretical foundation for
this study’s examination of business format evolution, consumer
behavior and service experience in Guiyang. At the same time, digi-
tal transformation not only improves operational efficiency but also
reduces wastage of fresh produce through accurate forecasting, opti-
mizes delivery routes, and facilitates low-carbon logistics and the
sustainable use of resources.
2.1.2 Factors influencing the evolution of fresh
food retail formats
Existing research has systematically analyzed the driving mecha-
nisms behind the evolution of fresh food retail formats from multiple
perspectives, including digitalisation, consumer behavior, product
quality, supply chain efficiency, physical retail environments and the
policy landscape. Digital transformation and the O2O model are the
core drivers of format upgrading, whilst the optimization of digital
processes can reduce wastage and enhance fulfilment efficiency (Ma
et al., 2022; Y ang et al., 2022; Belwal et al., 2024). Consumer perceived
value, service quality and trust in food safety significantly influence
purchase intention and channel loyalty (Činčalová et al., 2021; Xing et
al., 2024; Thuannadee and Praneetpholkrang, 2025), whilst product
safety, traceability and supply chain efficiency constitute key con -
straints on the sustainable development of business formats (Cheng et
al., 2026; Lestari et al., 2024). The physical environment, spatial layout
and location selection of brick-and-mortar stores also influence the
consumer experience (Maciel et al., 2023). At the macro level, policy
regulations, urbanization and consumption upgrading collectively
drive the transformation of traditional retail formats ( Yuan et
al., 2026).
2.2 Theoretical framework and influencing
factors of consumer satisfaction with online
fresh food purchases
2.2.1 Theoretical foundations of consumer
satisfaction
The theoretical framework of consumer satisfaction is well-estab-
lished, providing a solid academic foundation for research into satis-
faction with online fresh produce. Cardozo (Cardozo, 1965) pioneered
the revelation of the role satisfaction plays in promoting repeat pur-
chases (Cardozo, 1965); the Expectation-Confirmation Theory (ECT)
is widely used to explain the mechanisms underlying the formation of
satisfaction (Shen et al., 2022). Satisfaction is a multidimensional con-
struct influenced by multiple factors such as product attributes, demo-
graphic characteristics and context (Yılmaz and Balcıoğlu, 2026), and
its application continues to expand across scenarios including
omnichannel retail, service interactions and green consumption
(Y aqub et al., 2022; Xu et al., 2022; Wang et al., 2023). In marketing
and logistics theory, satisfaction often serves as a core mediating or
outcome variable, significantly driving customer loyalty and willing-
ness to continue using a product or service (Kerschbaumer et al., 2022;
El Moussaoui et al., 2022; Kovalskii, 2024). This theoretical framework
lays the foundation for the use of LDA and the improved intuitive
fuzzy TOPSIS method in this study to evaluate satisfaction.
2.2.2 Factors influencing satisfaction with online
fresh food
In the context of online fresh food, satisfaction is driven by mul-
tiple factors, including logistics services, product quality, service qual-
ity and brand image. Confirmed that logistics services are the most
significant factor influencing satisfaction (Guan et al., 2022); product
quality, freshness and safety also play a crucial role ( Kang and
Namkung, 2024); service quality indirectly influences behavioral
intention through perceived value (Wang and Theerakittikul, 2022;
Thuannadee and Praneetpholkrang, 2025); and brand image has a
significant positive effect on satisfaction and purchase intention
(Erkmen and Turegun, 2022). These findings provide direct justifica-
tion for the selection of evaluation indicators in this study, including
product source safety, product integrity, delivery service, and after-
sales response. Furthermore, from a sustainability perspective, high
satisfaction levels help to improve user retention, reduce customer
acquisition costs and minimize waste of resources, and are central to
the platform’s long-term sustainable operation.
2.3 Research progress on evaluation
methods and sales forecasting models for
fresh food E-commerce
2.3.1 Satisfaction evaluation models and methods
Traditional satisfaction evaluation has primarily relied on meth-
ods such as IPA and TOPSIS; in recent years, it has been upgraded
through the integration of positive text mining and machine learning.
Developed a food quality evaluation mode (Valderrama et al., 2021);
emphasized the necessity of a multi-dimensional service quality
framework (Yuan et al., 2026); and (Mao, 2025) highlighted the supe-
rior accuracy and adaptability of intelligent models. With the digital
transformation, technologies such as AI-powered recommendations,
dynamic pricing and sentiment analysis have been employed to
enhance satisfaction (Dai and Liu, 2024; Kumari et al., 2024; Mittal,
2025). Text mining and LDA topic modeling can efficiently extract
consumer concerns and sentiment tendencies, thereby enhancing the
objectivity of evaluations (Singh and Glińska-Neweś, 2022; Song et al.,
2022; Arifin and Purnama, 2023), providing methodological support
for the adoption of LDA and the improved intuitive fuzzy TOPSIS in
this study.
2.3.2 Deep learning models for sales forecasting
Deep learning has demonstrated superior capabilities in capturing
time-series patterns and volatility in sales forecasting. LSTM and its
variants are widely used in retail sales forecasting ( Hu et al., 2022;
Samonte et al., 2022), and the introduction of self-attention mecha-
nisms can further enhance the capture of key information (Kossen et
al., 2021). Confirmed the accuracy advantages of deep learning in time
series forecasting (Messaoudi et al., 2023); however, research also sug-
gests a risk of overfitting in scenarios involving small sample sizes and
high volatility (Peng et al., 2022; Tilshi and Punsisi, 2022). Accordingly,
this paper introduces the AT-DeepAR model—which utilizes an atten-
tion mechanism to enable accurate sales forecasting, thereby

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 04 frontiersin.org
significantly reducing inventory wastage in the fresh produce sector
and lowering energy consumption in the cold chain. It serves as a key
technological enabler for achieving low-carbon, efficient and sustain-
able operations in fresh produce retail.
2.4 Research on the sustainable
development of fresh food
Existing research provides a solid foundation for the sustainable
development of fresh food and highlights the intrinsic links between
food safety, environmental sustainability and economic viability.
Enhancing the environmental sustainability of food supply chains is
crucial to achieving several of the United Nations Sustainable
Development Goals (SDGs), particularly Zero Hunger (Goal 2) and
Responsible Consumption and Production (Goal 12); They emphasize
that food safety measures must be balanced against environmental
factors to avoid adverse effects (López-Gálvez et al., 2021). Further
research supports this view, highlighting the necessity of establishing
a sustainable fresh food cold chain system that balances environmen-
tal, social and economic benefits; a systematic review indicates that
sustainable practices in this field can enhance market viability and
resource utilization efficiency (Liao et al., 2021). Furthermore, innova-
tions in food packaging, such as biodegradable materials, and the
application of smart technologies within the supply chain are regarded
as key avenues for reducing fresh produce wastage and enhancing sus-
tainability levels (Versino et al., 2023; Xu et al., 2025; Shen et al., 2025).
Such innovations align with broader sustainable development goals by
minimizing environmental impact whilst ensuring food safety.
2.5 Literature review and research gaps
Overall, existing research still exhibits three notable shortcom-
ings: firstly, the geographical focus of studies is heavily concentrated
on eastern regions and first-tier cities, with a scarcity of empirical
research comparing local platforms with national platforms in south-
western provincial capitals such as Guiyang; secondly, research meth-
ods are relatively limited, with few integrated analytical frameworks
that combine questionnaire data, sentiment analysis of online reviews,
and deep learning-based forecasting; Third, there is insufficient inte-
gration between business model evolution, satisfaction and sales fore-
casting, with a lack of systematic characterization of platform
competitiveness, transaction costs and consumer behavior. Fourthly,
existing research has largely failed to link fresh food retail operations
with the Sustainable Development Goals, and there is a lack of quan-
titative analysis of sustainable dimensions such as waste reduction,
low-carbon practices and supply chain resilience. In light of these
gaps, this paper takes Guiyang as its research setting and employs a
multi-model integration approach combining LDA, an improved
intuitive fuzzy TOPSIS method, and AT-DeepAR to investigate the
mechanisms of business model evolution, the factors influencing sat-
isfaction, and the precise forecasting of sales volume. The aim is to
address the shortcomings of existing research and provide empirical
evidence to support the upgrading of regional fresh food e-commerce.
2.6 Summary
Regional disparities in China’s fresh food e-commerce sector are
pronounced. Whilst supply chains in the eastern regions and first-tier
cities are mature and highly competitive, southwestern cities such as
Guiyang possess significant potential for consumption upgrading, yet
lag behind in terms of cold chain infrastructure, supply chain develop-
ment and digitalisation. Existing research has focused heavily on
national platforms, with insufficient attention paid to the development
mechanisms, user satisfaction and market competitiveness of regional,
local fresh food platforms. Empirical studies specifically targeting pro-
vincial capitals in the southwest and comparing local platforms with
national ones are particularly scarce, making it difficult to support the
high-quality development of the regional fresh food industry. Existing
literature exhibits clear methodological limitations: firstly, regional
samples are concentrated in the east, lacking targeted examination of
the south-west; secondly, most studies employ single models, with few
integrated frameworks combining questionnaire data, text mining and
deep learning; thirdly, there is a lack of systematic analysis of the
intrinsic links between business model evolution, consumer satisfac-
tion and sales forecasting. At the same time, existing research pays
insufficient attention to the sustainability aspects of fresh produce
retail—such as wastage rates, carbon emissions reduction and supply
chain resilience—making it difficult to guide the green transition of
the regional fresh produce industry. This study focuses on six major
online fresh food platforms in Guiyang City and employs a multi-
model integration approach for empirical analysis, yielding three key
conclusions. Conclusions: Firstly, it fills a gap in research on fresh food
e-commerce in underdeveloped regions of south-west China and
reveals the unique patterns of evolution in the regional fresh food
retail sector; secondly, it establishes an integrated analytical frame-
work combining multi-source data and multiple methodologies-
namely ‘questionnaire data + text mining + deep learning’-thereby
enhancing the scientific rigor and reliability of the research findings;
and thirdly, it marks the first application of the Modified Intuitive
Fuzzy TOPSIS and AT-DeepAR models to fresh food e-commerce
research in the south-west region. By incorporating a sustainability
perspective, the study provides methodological guidance for the low-
carbon, waste-reduction and efficiency-enhancing transformation of
fresh food retail, whilst also offering insights for methodological inno-
vation in related fields.
3 Research design
Against the backdrop of the internet driving the shift toward
online consumption, this study employed a blended online-offline
approach to survey fresh produce consumers in Guiyang. The research
primarily relied on questionnaire surveys, supplemented by literature
reviews and interviews. Two rounds of questionnaires were designed
and distributed: the first round targeted all fresh produce consumers,
whilst the second round focused on users of online fresh produce plat-
forms. The questionnaire design was optimized based on preliminary
research involving literature reviews and interviews to enhance the
response rate (see Appendices 1, 3 for details). The study aims to sys-
tematically analyze consumer satisfaction with online fresh food plat-
forms in Guiyang, China, to identify the potential of the local fresh
food market, and to provide insights for optimizing platform opera-
tions, ensuring sustainable development and improving supply chain
efficiency. The survey covers fresh food consumers of all age groups in
Guiyang and involves two rounds of questionnaire collection and

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 05 frontiersin.org
validation. To ensure the authenticity and reliability of the data,
random sampling was employed throughout the survey. Returned
questionnaires were rigorously screened to exclude invalid responses,
such as those with excessively short completion times, no variation in
responses or extreme choices, internal contradictions, all questions
selected identically, failure to answer key questions, or the inclusion
of inappropriate content.
3.1 First round of questionnaires
This paper analyses the 27 scale items in the questionnaire, catego-
rizing them into four dimensions based on the survey content: plat-
form supply, delivery speed, pricing and promotions, and feedback on
physical products after purchase. A total of 1,028 valid questionnaires
were ultimately returned, representing a response rate of 85.67%.
3.1.1 Reliability testing
As can be seen from Tables 1, 2, the coefficients for all four dimen-
sions are above 0.9, indicating excellent reliability. This suggests that
the questionnaire is scientifically and reasonably structured, and that
the scale exhibits a high level of internal consistency.
3.1.2 Validity testing
Logical analysis was employed to assess the validity of the research
content; feedback was sought from experts and questionnaire items
were revised to ensure the validity of the scale. The specific results are
shown in Tables 3, 4.
A KMO value of 0.9 or above indicates a very good fit. The test
results show that the KMO value is highly appropriate; furthermore,
the p-value for Bartlett’s sphericity test is less than 0.05, which is sta-
tistically significant.
3.1.3 Tests of randomness—run tests
To ensure the randomness of the sample, a run test was con -
ducted on the categorical variable. The run test statistic is the number
of runs, with the sequence consisting of 0 s and 1 s. In this paper, the
gender of the respondents was used as the variable to test the ran -
domness of the questionnaire data. The hypothesis testing questions
were: H1: The order of the sample data in the sequence is random;
HO: The order of the sample data in the sequence is not random. A
run test was conducted using SPSS to obtain the p-value and test
results. At a given significance level of α = 0.05, the critical values c1
and c2 for the rejection region were derived using an approximation
formula, satisfying P(R ≤ c1) ≤ α and P(R ≥ c2) ≤ α. The results
showed that the p-value of the Z-statistic was 0.858, which is greater
than 0.05; therefore, the null hypothesis was accepted, indicating that
the sample data is random. Additional run tests were conducted on
other categorical variables, including age group, occupation, and
monthly income. All yielded non-significant results (p > 0.05), fur-
ther supporting the randomness of the sample. The results indicate
that the order of the sample data for most variable sequences is
random, suggesting that the data obtained from this survey exhibit a
high degree of randomization.
3.2 Second round of questionnaires
Following standardized screening, a total of 716 valid ques -
tionnaires were recovered from the second round, yielding a valid
response rate of 89.5%. A normality test was conducted using
SPSS, with gender as the test variable; at the α = 0.05 level, the
Z-statistic p = 0.575 > 0.05, leading to the acceptance of the null
hypothesis. Furthermore, most variables passed the randomness
test, indicating that the sample possessed good randomness and
representativeness.
The construct of consumer satisfaction was operationalized based
on Expectation-Confirmation Theory (ECT) and prior literature on
online fresh food retail [( Guan et al., 2022); Wang and Liu, 2015].
Seven core items (Q6, Q7, Q10, Q11, Q17–Q23) were selected from
the questionnaire to capture four theoretically derived dimensions:
product quality (freshness, source safety, and integrity), delivery ser-
vice (speed, attitude, and packaging), price perception (reasonableness
TABLE 1 Satisfaction reliability test table.
Dimension Cronbach alpha
number of items
Reliability
assessment
Platform supply 0.956 3 Great
Delivery stage 0.951 4 Great
Pricing and
promotions
0.930 3 Great
Feedback on physical
products
0.951 3 Great
TABLE 2 Significance and reliability test table.
Dimension Cronbach alpha number of items
reliability assessment
Platform supply 0.942 3 Great
Delivery stage 0.972 4 Great
Pricing and promotions 0.966 3 Great
Feedback on physical
products
0.973 3 Great
TABLE 3 KMO and Bartlett’s test of sphericity.
KMO 0.926
Bartlett’s test of
sphericity
Approximate chi-squared 14,403
df 78
p 0.000***
***indicates p < 0.001.
TABLE 4 KMO and Bartlett’s test of sphericity.
KMO 0.936
Bartlett’s test of
sphericity
Approximate chi-squared 31274.13
df 78
p 0.000***
***indicates p < 0.001.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 06 frontiersin.org
and promotions), and after-sales response (returns and compensa-
tion). The questionnaire items were self-developed by the authors
based on the standard Likert scale format and informed by prior lit-
erature. No existing scale was directly adopted or adapted. All items
were measured on a 10-point Likert scale.
Reliability tests showed that the Cronbach’s α coefficients for the
core scale items were all above 0.8, indicating excellent internal con-
sistency. Structural validity was assessed via KMO and Bartlett’s sphe-
ricity tests (KMO = 0.936, p < 0.001), with results indicating suitability
for factor analysis.
3.3 Public data sources
In addition to the two rounds of questionnaire surveys described
in Sections 4.1 and 4.2, this study also utilized several publicly avail-
able datasets.
 (1) Online review data: A total of 16,321 valid reviews were
crawled from six fresh food platforms in Guiyang (Guihuihui,
Meituan Y ouxuan, Dingdong Maicai, Duoduo Grocery,
Freshippo, and JD NOW) using Octopus software. The top 30
products on each platform were selected, and reviews were
sorted by date from most recent to oldest. The data collection
period was from July 4, 2024 to October 4, 2024. Spam com-
ments were removed, and the remaining 16,321 reviews were
used for LDA topic modeling and sentiment analysis in
Section 6.1.
 (2) Sales and operational data: Monthly sales data for the period
2022–2024 were collected from the six platforms, including
monthly sales volume, number of visitors, number of items
added to cart, average order value, number of Direct Express
visitors, and number of collectors. These data were used for
the AT-DeepAR sales forecasting model in Section 6.2.
 (3) Population data: The permanent resident population data for
Guizhou Province (38.5621 million) and Guiyang City (5.98
million) were sourced from the Seventh National Population
Census bulletins ( Guiyang Municipal Bureau of Statistics,
Guiyang Municipal Office of the Leading Group for the
Seventh National Population Census, 2021 ; Guizhou
Provincial Bureau of Statistics, Guizhou Provincial Office of
the Leading Group for the Seventh National Population
Census, 2021 ). These data were used in the Introduction
(Section 1) to contextualize market demand.
4 Analysis of the online fresh produce
market
Based on the valid sample described above, this paper further
examines the basic characteristics of fresh food consumers in Guiyang
and their platform preferences, thereby providing a practical founda-
tion for subsequent analyses of satisfaction and sales, as well as for the
formulation of sustainable operational strategies. The basic character-
istics of users are as follows: regarding basic information on fresh pro-
duce platform users, in terms of gender, the proportion of male
respondents was slightly higher than that of females, at approximately
56%; in terms of age, those under 19 accounted for the largest propor-
tion, at approximately 56%, followed by those aged 20–29, accounting
for approximately 43%; In terms of occupation, students and workers
in agriculture, animal husbandry, fisheries and water conservancy
accounted for the largest proportions, at approximately 33 and 28%
respectively, whilst military personnel and other occupations
accounted for only about 1 and 2% respectively, with other occupa-
tions distributed evenly; regarding monthly household income, the
300–5,000 yuan bracket accounted for approximately 22%, with the
remaining income brackets distributed relatively evenly. The analysis
of fresh produce platform user preferences is as follows:
4.1 How user age influences the choice of
fresh produce platforms
As shown in the histogram in Figure 1, the horizontal axis rep-
resents the age of respondents, the vertical axis represents the six
fresh produce platforms in Guiyang, and the height of the bars indi-
cates the age distribution of users across these six platforms. It can
be seen that in this sample, the age distribution of users varied across
platforms. For Guihuihui, the most frequent age group was
FIGURE 1
Relationship Ridge Plot.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 07 frontiersin.org
25–30 years. For Meituan Y ouxuan, users aged 19 years were the
most frequent, whilst other age groups show a relatively flat distribu-
tion; Dingdong Maicai’s users are distributed fairly evenly across all
age groups, with a higher proportion in the 50–55 age bracket;
Duoduo Grocery has a smaller user base around the age of 30, with
concentrations around 27 and 36; Freshippo’s user base peaks around
the age of 27 and is distributed evenly across the 30–40 age group; JD
NOW’s user distribution is relatively flat across a broader age range,
namely 40–55, with the highest concentration around the age of 37.
4.2 The impact of monthly household
income on the choice of fresh food delivery
platforms
As shown in Figure 2  and the pie chart, monthly household
income also influences the choice of fresh food delivery platforms.
In this sample, households with a monthly income below 3,000
yuan most frequently reported using Freshippo and JD NOW ,
whilst their choices across the other four platforms are relatively
evenly distributed, though less frequent than for the first two plat -
forms; those with a monthly income of 3,000–5,000 yuan predom -
inantly choose Guihuihui, followed by Freshippo; Households
with a monthly income of 5,000–8,000 yuan typically choose
Duoduo Grocery and Dingdong Maicai, with the others being less
popular; those with 8,000–15,000 yuan see half opting for Meituan
Y ouxuan, followed by JD NOW and Duoduo Grocery; whilst those
earning over 15,000 yuan show a more even distribution across
platforms.
4.3 Differences in fresh food platform
choice by user gender
As shown in Figure 3, the gender distribution of users on fresh
food platforms varies. Whilst the male-to-female ratio on JD NOW is
almost identical, in this sample, the proportion of female users was
higher than male users for Freshippo, Duoduo Grocery, Meituan
Y ouxuan, and Guihuihui; only Dingdong Maicai has a higher propor-
tion of male users than female users.
FIGURE 2
Relationship and chord diagram.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 08 frontiersin.org
4.4 Types of products purchased by users
As shown by the pie chart in Figure 4 , when it comes to pur -
chasing choices on fresh food platforms, the majority of users opt
for vegetables, followed by seafood, fruit, and meat and poultry.
A small number of users choose to purchase dairy and baked
goods, alcoholic beverages and soft drinks, ready-to-eat and
frozen foods, snacks, and grains, oils and seasonings; virtually no
users choose to purchase paper products or cleaning supplies on
fresh food platforms. This indicates that users are more inclined
to purchase agricultural products on the platform. A stable supply
and guaranteed quality of high-frequency, essential fresh food
FIGURE 3
Relationship diagram.
FIGURE 4
Petal diagram.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 09 frontiersin.org
products are fundamental to enhancing customer loyalty, reduc -
ing customer churn and ensuring the platform’s sustainable
operation.
4.5 Users purchasing different types of
items on different fresh food platforms
As shown in the bubble chart in Figure 5, the vertical axis rep -
resents the six fresh food platforms in Guiyang, the horizontal axis
represents the types of items available on these platforms, and the
size of the bubbles indicates the frequency with which users choose
to purchase different types of items on different platforms. It can be
seen that users select fewer product categories on Dingdong Maicai,
whilst they select more on Meituan Y ouxuan and Freshippo. In the
‘Paper and Cleaning Products’ column, however, almost no users
choose to purchase these items on fresh food platforms.
Based on the aforementioned analysis of user characteristics
and consumption preferences in Guiyang’s online fresh produce
market, this paper conducts a multi-model empirical study from
the perspectives of text mining and deep learning to systematically
reveal consumer sentiment trends, differences in platform
competitiveness,and patterns in sales volume evolution,it also
provides data support for sustainable objectives in the fresh food
retail sector, such as reducing wastage and losses, low-carbon
delivery and supply chain optimization. In the following sections,
we will successively employ the LDA topic model and an improved
intuitive fuzzy TOPSIS method to perform sentiment analysis and
satisfaction evaluation of online reviews, and utilize the
AT-DeepAR model—which incorporates an attention mecha -
nism—to conduct time-series forecasting of fresh produce sales,
thereby comprehensively characterizing the operational charac -
teristics and development trends of the regional fresh pro -
duce market.
5 Market research and analysis
5.1 LDA-based topic analysis and an
improved intuitive fuzzy TOPSIS sentiment
analysis algorithm
5.1.1 Data sources and notes
This paper uses six online fresh food platforms—Guihuihui,
Meituan Y ouxuan, Dingdong Maicai, Duoduo Grocery, Freshippo
and JD NOW—as sources of data for analysis. By setting the
names of each platform as keywords and sorting the reviews by
date from most recent to oldest, the top 30 products on each plat -
form were selected as the subjects of analysis, and product review
data was scraped using the Octopus software. These platforms
boast a vast user base and a diverse range of review styles; how -
ever, they contain a proportion of spam comments, such as
“hahaha” and “awesome, ” which lack substantive content. After
removing these spam comments, a total of 16,321 valid review
entries were obtained, forming the data foundation for the experi -
ments in this paper. The pre-processing of the review data was
carried out as follows: the Jieba tokenisation package in Python
was used to tokenise the review data; stopword lists from the
Machine Intelligence Laboratory at Sichuan University, Harbin
Institute of Technology, Baidu, and Chinese-English stopword lists
were collected, merged and deduplicated to form a stopword list,
and Python programming was used to remove stopwords from the
product reviews. Finally, the vocabulary in the reviews was fil -
tered, scored according to sentiment and part-of-speech, and a
sentiment lexicon was constructed. The accuracy of the lexicon
was manually verified, and it was supplemented based on the
characteristics of fresh produce to ensure the accuracy and com -
prehensiveness of the sentiment analysis (see Appendix 2  for the
Python code).
FIGURE 5
Relationship bubble chart.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 10 frontiersin.org
5.1.2 LDA topic modeling
As a typical hierarchical Bayesian probabilistic graphical model,
LDA comprises a three-layer structure characterized by coupled rela-
tionships between the document layer, the topic layer and the vocabu-
lary layer. The model assumes that the parameter distributions of both
the document–topic layer and the topic–vocabulary layer follow a
multinomial distribution, and achieves semantic analysis of text
through probabilistic mapping in the latent topic space. From the per-
spective of generative modeling, the LDA algorithm training process
can be formally described as follows (Hongxin and Yuhui, 2015):
 (1) Text of a single comment m of feature capacity mN  follows a
Poisson distribution, that is ∼mN Pois  ( î) .among which î
distribution parameters.
 (2) With regard to the text of the commentary in section m com-
ments, ( { }m 1,2, ,M∈  ) that is mθ∼ Dirichlet (á ),among
which M indicates the total number of comments on the data-
set, mθ  indicates the m probability distribution of comment
topics, α  the Dirichlet prior parameters for the multinomial
distribution underlying each comment.
 (3) Regarding the topic n generate feature word distributions,
among which { } kz 1,2, ,K , φ∈∼   Dirich- let ( ),Kβ  total
number of topics, β the Dirichlet prior parameters for the
multinomial distribution of words under each topic.
 (4) The generation process of the feature word
{ }( )m,n mw n 1,2, ,N∈   in Comment m, let mN  be the key-
word contained in the m-th topic,generate the feature word
themes for comment mw ,n  based on the distribution of
themes in mθ , that is mz ,n ~Multinomial ( )mm,z ,nθ  refers
to the topic of the a-th word in the m-th comment. Generate
the selected topic terms based on the term distribution g
φ mz ,n , that is ∼mw ,n  Multinomial (φ mz ,n) .
 (5) The calculation method for the probability distribution of fea-
ture words is as shown in Equation 1:
 ( )αβ α= ∗, , ( ,) ( )P wz P wzw P z  (1)
 (6) Based on this, we further calculate the expected values of the
Dirichlet distribution, obtaining the expected values of the
document-topic distribution and the topic-term distribution
respectively. The calculation Equations 2, 3 respectively:

( )
( )
α
θ
α
=
+
=
+∑
,
,
,
1
kmk
mk K
mk
k
n
n

(2)

( )
( )
β
ϕ
β
=
+
=
+∑
,
,
,
1
tkt
kt V
kt
t
n
n

(3)
In the equation: m,kθ  indicates that in the expression: indicates
the theme in data m, the probability of k. denotes the probability of
the feature word t in topic k, ( )m, kn indicates the keywords associated
with topic k in comment m, ( )k, tn  this represents the number of times
the feature word t appears in topic k.
T o estimate the parameters of the LDA model, exact inference is
intractable. Therefore, we employ Gibbs sampling, a Markov Chain
Monte Carlo (MCMC) method, to approximate the posterior distribu-
tion. The conditional probability for assigning a topic to a word, given
all other assignments, is derived as follows:
 (7) T o achieve efficient inference of model parameters, we employ
the Gibbs sampling algorithm, and the calculation formula for
its conditional probability is shown in Equation 4:

( )
( )
( )
( )
( )
11
|,
tk
tmk ki KV kt
mk t k
kt
nnP z kwz
nn
ε εε
ε ε
βα
αβ
= =
++= = ∗
++∑∑

(4)
In the equation: ( ) ε knm the number of features in data set m that have
not been assigned to topic k, ( ) ε tnk the number of times a feature word
has not been assigned to subject term k.
 (8) Confusion measures the accuracy with which the LDA
topic model predicts samples ( Guan et al., 2022 ); it is cur -
rently the most widely used method for determining the
optimal number of topics, and serves as a metric of the
model’ s predictive ability for new document collections. It
reflects the degree of confusion the model experiences
when predicting word sequences in new documents, as fol -
lows. Its definition is as shown in Equation 5:

( )
( )
=
=


= − 


∑
∑
1
1
log
exp
M
d
d
M
d
d
Pw
Perplexity D
N

(5)
Among which, D for the set of documents to be tested, dw  a
sequence of words in text D, dN  the number of words in document
d, ( )dPw the probability of dw  occurring in the document.
5.1.3 Constructing a sentiment lexicon for online
fresh produce platforms
By analyzing review data from online fresh produce platforms, we
aim to uncover the latent thematic structures within the reviews. These
themes reflect the key areas of consumer concern, such as product quality,
delivery services and value for money. We employ the LDA model to
achieve this objective; this model is a widely used topic model in the field
of text mining, capable of automatically identifying latent thematic distri-
butions within large volumes of text data. By applying Jieba word segmen-
tation and stop-word filtering to the crawled review documents, the raw
text is converted into a sequence of words that the model can process;
subsequently, keywords carrying thematic information are filtered based
on part-of-speech, and further screening is conducted according to part-
of-speech against HowNet, NTUSD and Chinese positive/negative

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 11 frontiersin.org
sentiment dictionaries to enhance the quality of the lexical resources. To
address the complexity of Chinese grammar, auxiliary dictionaries cover-
ing punctuation, conjunctions and phrases are further introduced. Finally,
terms are merged and deduplicated by part-of-speech category, and
manually annotated to construct a sentiment lexicon comprising adverbs,
conjunctions, negation words, phrases, positive and negative terms, and
punctuation marks. These steps collectively form the foundational frame-
work of an LDA model suitable for analyzing reviews on online fresh
produce platforms, providing a reliable tool for subsequent topic mining
and sentiment classification.
5.1.4 An improved intuitive fuzzy TOPSIS model
Intuitive fuzzy set theory is a useful tool for handling fuzziness and
uncertainty; intuitive fuzzy sets can simultaneously reflect the degrees
of support, uncertainty and opposition. Based on intuitive fuzzy set
theory, the sentiment analysis of online reviews following keyword
searches can be represented simply and comprehensively using intui-
tive fuzzy numbers. The expression is as shown in Equation 6:

( )1,2, , ; 1,2,
pos
ijpos
ij pos neg neu
ijij ij
k
q i nj m
kkk
= = =
++


(6)
The TOPSIS method avoids the subjectivity inherent in data,
requires no objective function, and is well-suited to capturing the
combined influence of multiple evaluation criteria. Furthermore, it
imposes no strict requirements regarding data distribution or sample
size, making it equally applicable to small-sample data and large-sam-
ple data involving multiple evaluation units and criteria, thus demon-
strating strong versatility. Following a keyword search, the overall
fuzziness scores of the products are used to construct the decision
matrix ( )= ij nmAa , among which =ij ijaA ,the intuitive fuzzy measure of attribute jf  of product a following iA  keyword search, n the number
of products found following a keyword search, where m is the number
of product attributes.
Before the calculation, the original data is first standardized using
Equation 7 to eliminate the influence of units. The calculation method
of the elements in the standardized decision matrix follows Equation 8:

( )1,2, , ; 1,2,ij j ij
j
aab i nj m s −= = =   (7)
Of these:

( )
=
= = − ∑
1
1 , m j ij j ij j
i
a as a an  (8)
After data standardization, a weighted normalization matrix as
shown in Equation 9 is constructed:
 ( ) ( )1,2, , ; 1,2,w ij nmc c i nj m ∗= = =   (9)
Regarding the determination of the weights of each evaluation
attribute, this paper adopts two methods. Firstly, the
comment-attribute distribution is obtained through the LDA model,
and the initial weights are calculated based on the frequency of attri-
bute occurrence. The specific formula is shown in Equation 10. At the
same time, in order to more objectively reflect the information content
of the data itself, an entropy-based weight calculation method, namely
the entropy weight method, is introduced. The core calculation
Equation 11:
 ( )12, ,, T kmW ww w=   (10)

( ) ( )
( ) ( )
=
= =
−
=
−
∑
∑∑
1
11
11 lnln
11 lnln
n
ij ij
ioj mn
ij ij
ji
PPn
W
PPn
(11)
To take into account both subjective preferences and objective
information, based on the principle of minimum relative information
entropy, the aforementioned weights are optimized and combined.
The optimization problem and its solution are respectively given by
Formulas Equation 12 and 13. Additionally, another set of weights is
constructed based on the frequency of each attribute being mentioned
in all comments. The calculation method is shown in Equations 14, 15:

( ) ( )
= =
= −+ −∑∑
n
11
min F ln ln ln ln
n
jj k jj o j
jj
WW W WW W

(12)
 =
= ≥=∑ 
1
s.t : 1; 0, 1,2, ,
n
jj
i
WW j n

( )λλ
=

= +−  ∑ 1 , min 1
n
jj
j
Lw F w
 (13)

0Order 0 then 2ln ln ln _ 2 _ 0jk j
j
L wwww λ∂ = −− =∂

( )
11
222 10 20211
1
and 1
j
nknn
j kjjj
j
ww
W e ww
e
λ
λ
λ
λ
∗ +
+= =
=
= = = ∗∑∑ ∑

( )
( )
( )
1
20
1
201
1,2,3,
kj
j
n
kjj
ww
sow j n
ww=
∗
= =
∗∑

 (14)
 ( )1,2, , ; 1,2,w ij j ijC w b i nj m∗= = =   (15)
After determining the final weights, the TOPSIS method is used
for comprehensive evaluation. First, according to Equations 16, 17, the
distances of each evaluation object to the positive ideal solution and

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 12 frontiersin.org
the negative ideal solution are calculated. The distances of each plan
to the positive ideal solution C+ and the negative ideal solution C- are
calculated. The distance of the searched-for keyword-related products
to the positive ideal solution can be obtained in the same way as
follows:

( ) ( )
2
1
1,2, ,
m
i j ij j
j
S wc c i n++
=
= −=∑ 

(16)

( ) ( )
2
1
1,2, ,
m
i j ij j
j
S wc c i n−−
=
= −=∑ 

(17)
Finally, the relative closeness degree of each object to the positive
ideal solution is calculated through Equation 18. The larger this value
is, the higher the consumer satisfaction level is:

( )1,2, ,ii
ii
SC in
SS
−
+−= = +   (18)
Among which ∗∈0,1iC , the higher the overall score, the greater
the level of satisfaction.
5.1.5 Sentiment analysis of online reviews on fresh
food platforms
This paper utilizes the gensim machine learning library within
the Python ecosystem to conduct LDA topic modeling research on
review data, successfully extracting seven latent topics and their cor-
responding probability distributions. For the sake of brevity, only the
top 10 word distributions for four of these topics are listed here, as
shown in Tables 5, 6. LDA topic mining enables classification based
on semantics, using semantically related words to express multiple
latent themes. For example, the vocabulary set of Theme 1 predomi-
nantly reflects the theme of ‘freshness’; the vocabulary combination
of Theme 2 focuses on ‘delivery’-related aspects; the vocabulary
composition of Theme 3 outlines the theme of ‘after-sales service’;
and the vocabulary presentation of Theme 4 revolves around ‘experi-
ence’ . By extension, the specific themes described by the results of
the remaining three themes are ‘product’ , ‘price’ and ‘discounts’
respectively.
Calculations based on the formula yield the TOPSIS decision
matrix composed of the intuitive fuzzy numbers for online fresh food
platforms. The decision matrices for the seven themes across the six
online fresh food platforms are presented below, as shown in Table 7.
The table illustrates the distribution of product–theme–sentiment ori-
entations. For example, in Platform 1, Theme 1 (Freshness) has an
intuitive fuzzy matrix of [0.828, 0.046], where 0.828 represents the
proportion of positive comments relating to Theme 1 (Freshness) in
Platform 1’s reviews, and 0.046 represents the proportion of negative
comments relating to Theme 1 (Freshness) in Platform 1’s reviews. It
is evident that the number of positive reviews for Theme 1 on Platform
1 far exceeds the number of negative reviews, indicating that the prod-
uct attribute of ‘freshness’ on Platform 1 meets the needs of the vast
majority of consumers purchasing this product.
The decision matrix constructed from the aggregate fuzzy num-
bers of the online fresh produce platform is standardized; combined
with feature weights, a weighted normalized matrix is calculated, as
shown in Tables 8, 9.
This paper calculates the positive and negative sentiment scores
for online reviews on each online fresh produce platform, as well as
the overall sentiment score for these reviews:
This study examined satisfaction levels with online fresh food
platforms in Guiyang, employing a text analysis algorithm based on
the LDA topic model and the intuitive fuzzy TOPSIS method to ana-
lyze user reviews. The results (Table 10) show that the platforms are
ranked from highest to lowest as follows: Duoduo Grocery, Meituan
Y ouxuan, JD NOW , Freshippo, Guihuihui and Dingdong Maicai.
 (1) In terms of thematic weighting, ‘delivery’ (0.177) and ‘experi-
ence’ (0.183) carry the highest weights, indicating that con-
sumers place particular emphasis on the quality of delivery
services and the overall shopping experience when selecting
online fresh food platforms. The top-ranked platforms,
Duoduo Grocery and Meituan Y ouxuan, likely excel in areas
such as delivery speed, punctuality and customer service,
thereby enhancing consumer satisfaction and loyalty. Efficient
delivery not only enhances the customer experience but also
reduces transit times for fresh produce and lowers wastage
rates, thereby aligning with sustainability goals aimed at mini-
mizing waste. Meanwhile, JD NOW and Freshippo also hold
certain advantages in the ‘Experience’ theme, likely having
earned consumer recognition through a wide range of prod-
ucts, user-friendly interface design and excellent after-sales
service.
 (2) The weights for the ‘Freshness’ (0.151) and ‘Products’ (0.121)
themes are also relatively high, indicating that consumers have
TABLE 5 Thematic feature keywords.
Topic 1 Topic 2 Topic 3 Topic 4
Fresh,
0.04189596
On time,
0.08927697
Quickly,
0.05266603
Cheap,
0.03847729
Moisture,
0.03495985
Order placed,
0.08625184
Replace,
0.05220864
Poor,
0.03709938
Freshly mined,
0.02902574
Time, 0.0735576 Free shipping,
0.04693572
Complaints,
0.02961587
Y es, 0.02789335 Good attitude,
0.04321172
The feedback was
good, 0.03704721
Few, 0.02351570
Delicious,
0.02562058
Convenient,
0.02447371
Send, 0.03644631 Out of stock,
0.02351571
Tender,
0.02182365
Very fast,
0.02269945
Positive review,
0.03337435
Not enough,
0.02063292
wilted,
0.02174213
Hard work,
0.02029562
No compensation
will be given,
0.03261657
Bad, 0.01846059
Look,
0.01968939
It does not
match,
0.01790208
Call 0.03097264 Clean,
0.01590792
It has a smell,
0.01933344
Packaging,
0.01786819
Take a photo,
0.02588461
Fake,
0.01571093
Taste,
0.01834386
Unable to find,
0.01614105
Deflecting
responsibility,
0.02289389
Generous,
0.01519336

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 13 frontiersin.org
high expectations regarding the quality and variety of fresh
produce. As a local platform, Guihuihui may hold certain
advantages in product freshness and the supply of locally
sourced goods; however, its performance in other themes may
require improvement, resulting in a relatively lower ranking.
Although Dingdong Maicai carries some weight in the
‘Product’ theme, its performance in other key themes is not
sufficiently prominent, which has impacted its overall ranking.
TABLE 6 Weight allocation table for fresh food theme.
Topic 1 2 3 4 5 6 7
Mining results Fresh Delivery
After-sales
service
Experience product price discount
Weight 0.151 0.177 0.105 0.183 0.121 0.147 0.116
TABLE 7 Self-adjoint fuzzy matrix table.
Topic Autocorrelation matrix
Platform1 Platform2 Platform3 Platform4 Platform5 Platform6
1 [0.828,0.046] [0.814,0.070] [0.775,0.038] [0.767,0.041] [0.772,0.114] [0.781,0.109]
2 [0.915,0.880] [0.880,0.028] [0.730,0.108] [0.865,0.032] [0.891,0.020] [0.912,0.029]
3 [0.744,0.049] [0.775,0.075] [0.450,0.225] [0.659,0.146] [0.701,0.052] [0.720,0.120]
4 [0.791,0.044] [0.800,0.063] [0.634,0.037] [0.782,0.010] [0.769,0.092] [0.725,0.072]
5 [0.782,0.034] [0.744,0.064] [0.631,0.123] [0.733,0.067] [0.732,0.065] [0.670,0.115]
6 [0.755,0.041] [0.814,0.034] [0.695,0.051] [0.733,0.067] [0.661,0.054] [0.609,0.043]
7 [0.800,0.096] [0.898,0.036] [0.773,0.068] [0.870,0.031] [0.788,0.061] [0.827,0.072]
TABLE 8 Corresponding numbers for online fresh food platforms.
Platform1 Platform2 Platform3 Platform4 Platform5 Platform6
Dingdong Maicai Guihuihui Duoduo Grocery Freshippo JD NOW Meituan Y ouxuan
TABLE 9 Improved specification weighting matrix.
Topic Weighting matrix
Platform1 Platform2 Platform3 Platform4 Platform5 Platform6
1 [0.025,-0.010] [0.022,-0.003] [0.014,-0.013] [0.013,-0.012] [0.014,0.011] [0.016,0.010]
2 [0.070,0.448] [0.059,-0.030] [0.009,0.015] [0.054,-0.027] [0.062,-0.034] [0.069,-0.029]
3 [0.012,-0.004] [0.016,0.003] [−0.023,0.046] [0.002,0.024] [0.007,-0.003] [0.009,0.016]
4 [0.019,-0.007] [0.020,-0.001] [−0.002,-0.009] [0.018,-0.017] [0.016,0.008] [0.010,0.002]
5 [−0.019,-0.051] [−0.025,-0.027] [−0.044,0.022] [−0.027,-0.024] [−0.027,-0.025] [−0.038,0.015]
6 [0.011,-0.003] [0.015,-0.004] [0.007,-0.001] [0.004,-0.004] [0.005,0.000] [0.002,-0.002]
7 [0.006,0.010] [0.028,-0.021] [−0.047,-0.011] [0.022,-0.024] [0.004,-0.008] [0.012,-0.002]
TABLE 10 Results of the improved intuitive fuzzy TOPSIS evaluation.
Online fresh food
platform
Positive ideal
distance
Negative ideal
distance
Overall evaluation index Sort by
1 1.768 0.499 0.042 6
2 1.768 0.090 0.048 5
3 1.811 0.168 0.085 1
4 1.778 0.094 0.053 4
5 1.781 0.119 0.063 3
6 1.792 0.140 0.071 2

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 14 frontiersin.org
Product freshness and quality are at the heart of fresh food
retail; a consistent supply of high-quality produce helps reduce
returns and waste, thereby enhancing supply chain
sustainability.
 (3) The themes of after-sales service (0.105), price (0.147) and pro-
motions (0.116) carry relatively lower weights, yet they remain
factors of concern to consumers. Platforms ranking higher may
offer a better experience in these areas, such as providing pro-
motional activities and good after-sales service on top of rea-
sonable pricing, thereby enhancing consumer satisfaction.
Platforms ranking lower may need to make improvements in
these areas to boost their market competitiveness.
5.2 Deep learning-based fresh produce
sales forecasting model
It should be noted that the AT-DeepAR sales forecasting model
(Section 6.2) uses structured sales and operational data (monthly sales
volume, number of visitors, etc.), not the online review text. The
online reviews are used exclusively for LDA topic modeling and senti-
ment analysis in Section 6.1.
Sales forecasting is a crucial component of production decision-mak-
ing for fresh produce businesses. Developing sound ordering strategies,
reducing stock levels and optimizing inventory structure based on sales
forecasts for fresh produce are key objectives for businesses in their day-
to-day operations. Accurate forecasting can effectively minimize excess
stock and wastage due to expiry, reduce energy consumption in the cold
chain, and achieve low-carbon, efficient and sustainable inventory man-
agement (Sajja et al., 2021). This paper uses an improved DeepAR model
(Xin et al., 2024) to forecast sales volumes for major fresh produce plat-
forms in Guiyang (see Appendix 2 for Python code).
5.2.1 Construction of the AT-DeepAR model
incorporating an attention mechanism
Construction of the AT-DeepAR model with embedded attention
mechanism: The model predicts future sales by learning from historical
sales data and related covariates. To explain it more clearly, the core
mathematical framework of the model is presented first. The
construction of its joint probability distribution is shown in Equation
19, and the overall network architecture of the model is depicted in
Figure 6.
 ( )00, : ,1: 1 ,1:|, P it T i t i TPz z x −  (19)
We define the sales value of the i-th fresh product at time t as zi,t,
The entire time horizon T is split at time point 0t , resulting in the joint
conditional probability distribution ( )00, : ,1: 1 ,1:|, P it T i t i TPz z x − . Based
on historical sales data −0,1: 1itz  and product characteristic covariates
(i.e., p-dimensional product attribute features) ,1: P iTx , we model the
future sales volume of apparel products
0,:it Tz . The model framework
is given as follows:
As illustrated in Figure 6 , an attention mechanism is incor -
porated into the original DeepAR model to refine its network
architecture, allowing the model to prioritize sales data that have
a more significant impact on the current sales time step. The
conditional probability distribution within the model is formu -
lated as the product of likelihood factors across a sequence of
time steps. Its formal expression is as shown in Equation 20 :

( ) ( )
( )( )
00 00
0
0
, : ,1: 1 ,1: , : ,1: 1 ,1:
,,
|,
,|
|,
T
PP
it T i t i T it T i t i T
tt
T
ti it
tt
Qz z x Qz z x
z Ahθ
Θ− Θ−
=
=
=
= Θ
∏
∏

(20)
Within this framework, the update process of the network at each
time step is defined by Equation 21.
 ( ), ,1 ,1 , 1 : , ,, P it it it i TAh h Ah Z x −−= Θ  (21)
Where: h represents a recurrent network that synergizes LSTM
and an attention mechanism; ,itAh  is the output of an autoregressive
recurrent network integrated with an attention mechanism, indicating
the importance of historical sales of fresh products and their charac-
teristic covariates at different time points in predicting the output. T o
obtain ,itAh  at time t, the following are input into the network: the
FIGURE 6
Construction diagram of the AT-DeepAR model with embedded attention mechanism.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 15 frontiersin.org
output of the network at the previous time step, −,1itAh ; the historical
sales of fresh products at the previous time step, −,1itZ ; the character-
istic covariates of fresh products at the current time step, −,1itZ ; and
the model parameters, Θ .
The specific steps are as follows:
The introduction of the attention mechanism is the key feature of
the model in this paper. The specific operation steps are as follows:
Firstly, the encoder processes the input data, and its output is then sent
to the attention layer. During this process, the calculation of the atten-
tion weight vector involves the hidden states and cell states of the
encoder, and the specific calculation methods can be found in
Equations 22–24.
 ( )−= +, , ,1tanh ;it d it it de Whs b  (22)

( )
( )
=
=
∑
,
,
,
1
exp
exp
it
it T
it
t
ee
e

(23)

β=∑, ,,
T
it it it
t
Ah h

(24)
dW  is the weight matrix to be learned by the model; ,ith  is the
encoder’ s hidden state; −,1its  is the encoder’ s cell state at the previous
time step; db  is the bias vector of the fully connected layer.
After multiple training iterations, the model produces ,ite ,
which represents the correlations between hidden states; this is
normalized via the softmax function to yield the attention prob -
abilities β ,it  for each time step. The output of the attention layer
is ultimately fed into the vector ,itAh  of the LSTM gating unit in
the decoder layer.
After the model has undergone multiple training sessions, it
obtains the result representing the correlation of hidden states. After
the function is normalized, the attention probability for each moment
is obtained. The final output of the attention layer will serve as the
input vector for the decoder LSTM unit, and the calculation process
is as shown in Equation 25.
The information is integrated and output using the LSTM network
structure. LSTM precisely controls the information flow through the
forget gate, input gate, and output gate. First, the forget gate decides
which old information to discard based on the current input and the
previous moment’ s hidden state, and its calculation is as shown in
Equation 26.
Subsequently, the input gate decides which new information to
store in the cell state, and its calculation is as shown in Equation 27.
Equation 28 is used to calculate the candidate values of the cell state at
the current moment.
Based on the above results, Equation 29 is used to update the cell
state. Finally, the output gate calculates the hidden state at the current
moment based on the updated cell state using Equation 30, thus com-
pleting a time step cycle.
 ( )σ ∗ −= +, ,1 , ,it f it it ff W h Ah b  (25)
 ( )σ ∗ −= +, ,1 , ,it i it it ii W h Ah b  (26)
 ( )
∗
−= + ' , ,1 ,tanh ,it c it it cC W h Ah b  (27)
 −= ⊗ +⊗ ' , , ,1 , ,it it it it itC fc iC  (28)
 ( )σ ∗ −= +, ,1 , ,it o it it oo W h Ah b  (29)
 ( )= ⊗,, , tanhit it itho C  (30)
Finally, an LSTM network architecture is used to integrate and
output information. The forget gate uses the sigmoid function σ to
determine whether to discard certain information from memory cell
,itC ; it then combines and weights the values received from input ,itAh
and the hidden state −,1ith  of the previous layer to produce coefficient
−,1ith . The forget gate determines whether to discard certain informa-
tion from the current input ,itAh , generating coefficient ,iti . The neuron
updates to generate the current state tC , which requires the use of the
tanh function to compute the candidate values −,1itc  for the memory
cells, where ⊗ denotes the matrix multiplication operation. The output
gate determines whether to discard certain information regarding the
new memory based on tC , and then outputs the hidden state hi,t. W and
b represent the weight matrix and bias vector, respectively.
5.2.2 Application of the model
This paper utilizes data such as monthly sales volumes and the
number of followers from major fresh produce platforms in Guiyang.
The collected data was pre-processed and analyzed; this involved data
cleansing to remove outliers and imputing missing values using linear
interpolation. Finally, monthly sales data for the period from 2022 to
2024 was obtained, as shown in Figure 7.
Characteristics of the product data and their descriptive statistics
(Table 11).
The model results show that the AT-DeepAR model achieves sales
forecasting through the following process:
In terms of model design, a network architecture based on LSTM is
constructed, with parameters such as the number of hidden layer nodes
and the number of layers set to generate preliminary sales forecast values;
the LSTM output is weighted and aggregated via an attention mechanism,
and time-step weights are calculated to generate a sales vector; combined
with maximum likelihood estimation, a conditional probability distribu-
tion of future sales is constructed, and probabilistic forecast results are
output. The implementation steps include: dividing the pre-processed
data into training and test sets, training the model to generate probabilistic
forecasts; evaluating model performance using the test set, and iteratively
adjusting parameters to optimize forecasting accuracy; comparing the
forecast values with actual data; if the results are not optimal, returning to
adjust the model structure or parameters, and repeating the optimization
cycle until the forecasting performance meets the requirements.
As shown in Figure 8 above, there is a weak positive correlation
between the number of visitors and the number of items added to the
shopping basket, suggesting that an increase in visitor numbers may
have a certain promotional effect on the number of items added to the
basket, though the impact is not significant. There is also a weak posi-
tive correlation between the number of items added to the basket and
the number of items favourited, indicating that adding items to the
basket may be somewhat linked to favouriting items. There is a weak

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 16 frontiersin.org
positive correlation between the number of Direct Express visitors and
sales volume, suggesting that an increase in Direct Express visitors
may have a certain promotional effect on sales volume. The correla-
tions between the other variables are weak or virtually non-existent,
indicating that the linear relationships between them are not
significant.
Figure 9 illustrates the trend in numerical changes for each month of
2024. The observed values reflect the actual data recorded each month,
showing a certain degree of fluctuation: they are lower at the beginning of
the year, reach a peak in the middle of the year, and rise again toward the
end of the year. The predicted values from the AT-DeepAR model are
relatively close to the observed values, indicating that the model fits the
data well and is able to capture the trend in numerical changes effectively;
furthermore, both the observed and predicted values fall within the 95%
confidence interval. Overall, the AT-DeepAR model is able to accurately
predict the trend in sales revenue for the fresh produce platform in 2024:
sales revenue for the platform shows an overall upward trend with minor
fluctuations. Based on this, we have forecast the fresh produce sales
revenue for 2025. As can be seen from Figure 10 below, the average sales
revenue for 2025 is around 3.4, and the overall trend is upward.
This paper proposes an AT-DeepAR model incorporating an atten-
tion mechanism for fresh produce sales forecasting, with the aim of opti-
mizing inventory management and production decisions. By introducing
the attention mechanism, the model is able to dynamically focus on key
sales data, thereby enhancing forecasting accuracy. Experiments were
conducted using sales data from Guiyang City for the period 2022 to
2024. The results demonstrate that the model’s predicted values closely
align with actual values, validating its effectiveness and reliability in fresh
produce sales forecasting. This model can effectively guide fresh produce
companies in placing accurate orders, reducing stock wastage and lower-
ing energy consumption in the cold chain, thereby providing technical
support for low-carbon and sustainable operations in fresh produce retail.
This research offers technical support for fresh produce companies to
optimize their management, whilst also providing new insights into the
application of deep learning in time series forecasting.
6 Conclusions and recommendations
6.1 Research findings
Driven by the digital economy, China’s fresh food retail sector is accel-
erating its transition from traditional single-channel models to a diverse
range of business formats characterized by the integration of online and
offline channels. However, existing research has largely focused on devel-
oped regions in the east, paying insufficient attention to the regional het-
erogeneity of less developed provincial capitals in the southwest, and
lacking systematic analysis that integrates multi-source data and multiple
methodologies. This study takes six mainstream online fresh food plat-
forms in Guiyang (including the local platform ‘Guihuihui’) as its research
subjects. By integrating two rounds of stratified sampling questionnaire
surveys (1,744 valid samples) with 16,321 online review data points, utiliz-
ing LDA, an improved intuitive fuzzy TOPSIS, and the AT-DeepAR
multi-model integration analysis framework. It systematically investigates
the mechanisms underlying the evolution of fresh food retail formats, the
factors influencing consumer satisfaction, the market competition land-
scape, and sales forecasting. The main conclusions are as follows:
Firstly, an empirical analysis based on 1,744 valid samples from
Guiyang, China, indicates that users of online fresh food platforms exhibit
TABLE 11 Product data characteristics and descriptive statistics.
Name Describe Example
Date Product sales date April 2022
Transaction value Total transaction
amount of the product
230 million yuan
Number of visitors Number of visitors to all
pages of the store
75.21 million people
Number of items
added to basket
The number of items
added to the shopping
cart
20.24 million pieces
Average order value Average amount of
money customers spend
on products
12.56 yuan
Number of visitors
from Direct Express
Number of visitors to
the express lane
10.53 million
Sales volume Monthly product sales
volume
17.56 million
Number of collectors Number of users
clicking to favorite
2.56 million
FIGURE 7
Monthly sales data for 2022 to 2024.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 17 frontiersin.org
distinct age stratification and income differentiation. In terms of age dis-
tribution, the under-19 age group accounts for the highest proportion
(56%), followed by the 20–29 age group (43%), reflecting a predominantly
young user base; There are marked generational differences in platform
choice: Guihuihui covers all age groups, Meituan Y ouxuan is highly con-
centrated among 19-year-olds, whilst JD NOW shows a steady distribu-
tion across the 40–55 age bracket. In terms of income, low-income groups
tend to favor Freshippo and JD NOW , middle-income groups prefer
Duoduo Grocery and Dingdong Maicai, and half of the high-income
group is concentrated on Meituan Y ouxuan. In terms of gender, with the
exception of Dingdong Maicai, most platforms have a higher proportion
of female users. Regarding product category composition, vegetables, sea-
food and fruit are the core purchase categories, whilst the penetration rate
for paper and cleaning products is extremely low; Meituan Y ouxuan and
FIGURE 8
Thermal map of feature variables.
FIGURE 9
Trends in numerical changes for 2024 and AT-DeepAR forecast chart.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 18 frontiersin.org
Freshippo offer the widest range of categories, whilst Dingdong Maicai
has a higher concentration of product categories. The above findings pro-
vide a systematic user research foundation for satisfaction assessments,
sales forecasting and the formulation of sustainable operational strategies.
Secondly, the online fresh food market in Guiyang exhibits a com-
petitive landscape characterized by ‘national platforms dominating and
local platforms catching up’ , with consumer satisfaction closely correlated
with platform brand awareness. The satisfaction evaluation results using
LDA – an improved version of the intuitive fuzzy TOPSIS algorithm –
show that the platform satisfaction rankings are as follows: Duoduo
Grocery > Meituan Y ouxuan > JD NOW > Freshippo > Guihuihui >
Dingdong Maicai; The dimensions of greatest concern to consumers are
the overall shopping experience (weight 0.183) and delivery service
(weight 0.177), followed by product freshness (0.151) and price reason-
ableness (0.147). Brand awareness analysis based on the Graveyard model
indicates that Meituan Y ouxuan and Freshippo enjoy the highest market
recognition, followed by JD NOW and Duoduo Grocery, whilst local plat-
forms Guihuihui and Dingdong Maicai have significantly lower brand
awareness. Consumers’ high focus on delivery and experience points the
way for platforms to optimize services, reduce wastage and enhance
sustainability.
Thirdly, the AT-DeepAR deep learning model, which incorporates an
attention mechanism, is capable of accurately capturing the seasonal fluc-
tuations in fresh produce sales, with a higher prediction accuracy than
traditional time series models. Empirical testing using fresh produce sales
data from Guiyang City for the period 2022–2024 showed that the
AT-DeepAR model’s predicted values closely matched the actual values,
with all predictions falling within the 95% confidence interval; The model
predicts that fresh produce platform sales in Guiyang will maintain a
steady growth trend in 2025, with average monthly sales reaching approx-
imately 340 million yuan. By dynamically allocating attention weights
across different time steps, the model effectively addresses the shortcom-
ing of traditional models in capturing dependencies within long-term
time series data, thereby providing reliable technical support for fresh
produce enterprises in optimizing inventory, reducing wastage and losses,
and achieving low-carbon operations.
6.2 Policy recommendations
Based on the above conclusions, and taking into account the
actual development of the fresh produce retail market in Guiyang,
the following targeted recommendations are proposed, closely
aligned with the objectives of sustainable development (waste reduc-
tion, low-carbon, efficiency and inclusivity):
Firstly, optimize the structure of transaction costs to promote the
deep integration of omnichannel operations and low-carbon prac-
tices. Platforms should reduce delivery costs and improve delivery
times by integrating logistics resources, optimizing delivery routes
and promoting community collection points, thereby reducing
carbon emissions from delivery vehicles. They should also strengthen
direct procurement partnerships with upstream agricultural suppli-
ers to minimize intermediaries, thereby lowering procurement costs
and reducing fresh produce wastage. Drawing on new retail concepts,
platforms should develop a hybrid model of ‘online ordering + offline
collection/instant delivery’ to achieve complementary advantages
between online traffic and offline experiences, thereby establishing
an efficient and low-carbon fresh produce distribution system.
Secondly, focus on core consumer needs, address service shortcom-
ings, and enhance sustainable service capabilities. Prioritize the standard-
ization of delivery services to ensure timely delivery and the integrity of
goods, whilst improving the professional competence of delivery person-
nel. Focus on resolving pain points regarding product quality and after-
sales service by establishing strict supplier onboarding and quality
inspection systems, refining after-sales return and exchange mechanisms,
and shortening response times. Optimize the platform app’s functionality
and interface design, and strengthen the protection of personal informa-
tion and transaction security. By maintaining stable service quality, reduce
returns and waste, thereby enhancing supply chain sustainability.
Thirdly, implement a differentiated competitive strategy to enhance
the competitiveness of local platforms and promote the sustainable devel-
opment of the regional fresh produce sector. National platforms should
leverage their brand and scale advantages to increase the supply of
Guizhou’s distinctive agricultural products and adapt to local consumer
FIGURE 10
Trends in numerical changes for 2024–2025 and AT-DeepAR forecast chart.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 19 frontiersin.org
demand. The local platform ‘Guihuihui’ should focus on its local
strengths, creating a dedicated channel for ‘Qianhuo Chushan’ (Guizhou
produce reaching wider markets), strengthening cooperation with local
farmers’ markets and supermarkets, and building a city-wide delivery
network; it should also enhance brand awareness through targeted com-
munity promotion and word-of-mouth marketing. Platforms with lower
brand recognition should target niche markets such as high-end organic
fresh produce and ready-to-cook meals, avoiding direct competition with
leading platforms, and thereby supporting the sustainable distribution of
local specialty agricultural products.
Fourth, strengthen the application of digital technologies to achieve
refined operations and green development. Promote the application of the
AT-DeepAR model for sales forecasting, and optimize inventory manage-
ment by incorporating multi-dimensional factors such as weather and
public holidays to reduce fresh produce wastage. Utilize LDA topic mod-
eling and sentiment analysis technology to monitor consumer reviews in
real time, enabling rapid responses to changes in demand and service
complaints. Establish a digital supply chain management platform to
achieve visualization and intelligence across the entire procurement,
warehousing and delivery process. Use digital technology to drive fresh
produce retail toward reduced wastage, lower consumption and lower
carbon emissions, achieving a win-win outcome for both economic and
environmental benefits.
6.3 Limitations of the study and future
prospects
This study has certain limitations: firstly, the sample is confined to
Guiyang City, and the generalisability of the conclusions requires further
verification; secondly, the data covers a relatively short time span and fails
to capture long-term trends in the fresh food retail market; thirdly, the
study does not fully account for the impact of external factors such as
macroeconomic fluctuations, policy adjustments and unforeseen events;
fourthly, there is a lack of measurement of quantitative indicators for the
sustainability of fresh food retail (such as wastage rates, carbon emissions
and supply chain resilience).
Future research could be conducted in the following three areas: firstly,
expanding the research area to conduct a comparative analysis of the
developmental differences in fresh food retail markets across cities in the
eastern, central and western regions, thereby revealing regional patterns in
the evolution of China’s fresh food retail sector; secondly, extending the
data time span to conduct longitudinal tracking studies, providing an in-
depth analysis of the dynamic changes in consumer behavior and market
structures; thirdly, introducing more external variables, such as macroeco-
nomic indicators, policy documents and social media data, to construct a
more comprehensive analytical model, thereby enhancing the explanatory
power and predictive capability of the research findings; and fourthly,
incorporating sustainability indicators (waste rates, carbon footprint,
resource utilization rates) into the model to conduct quantitative assess-
ments and optimization studies on the sustainability of fresh food retail.
6.4 Alignment with the sustainable
development goals (SDGs)
The findings of this study support three United Nations Sustainable
Development Goals ( United Nations General Assembly, 2015 ).
Specifically, the AT-DeepAR model reduces fresh food waste and
improves supply chain stability, contributing to SDG 2 (Zero Hunger).
The empirical evidence from Guiyang offers practical insights for building
sustainable urban food distribution systems, aligning with SDG 11
(Sustainable Cities and Communities). Additionally, the LDA-TOPSIS
analysis identifies drivers of responsible consumption while the
AT-DeepAR model optimizes inventory management, both reducing
food waste and directly supporting SDG 12.3 under SDG 12 (Responsible
Consumption and Production).
Data availability statement
The original contributions presented in the study are included in
the article/Supplementary material, further inquiries can be directed
to the corresponding author.
Ethics statement
Ethical approval was not required for the studies involving
humans. The studies were conducted in accordance with the local
legislation and institutional requirements. The participants provided
their written informed consent to participate in this study.
Author contributions
CY: Conceptualization, Data curation, Investigation,
Methodology, Project administration, Writing  – original draft,
Writing – review & editing, Visualization. KH: Conceptualization,
Data curation, Methodology, Writing – original draft, Formal analysis,
Investigation. FH: Conceptualization, Data curation, Investigation,
Methodology, Writing  – original draft, Visualization. YZ:
Conceptualization, Data curation, Investigation, Methodology,
Software, Writing – original draft. LC: Conceptualization, Data cura-
tion, Methodology, Visualization, Writing – original draft, Project
administration, Writing – review & editing.
Funding
The author(s) declared that financial support was not received for
this work and/or its publication.
Conflict of interest
The author(s) declared that this work was conducted in the
absence of any commercial or financial relationships that could be
construed as a potential conflict of interest.
Generative AI statement
The author(s) declared that Generative AI was not used in the
creation of this manuscript.

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 20 frontiersin.org
Any alternative text (alt text) provided alongside figures in this
article has been generated by Frontiers with the support of artificial
intelligence and reasonable efforts have been made to ensure accuracy,
including review by the authors wherever possible. If you identify any
issues, please contact us.
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their affiliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsed by the publisher.
Supplementary material
The Supplementary material for this article can be found online
at: https://www.frontiersin.org/articles/10.3389/fsufs.2026.1866736/
full#supplementary-material
References
Akhtoian, A. (2023). Peculiarities of retail development in the context of a new paradigm
of economic development. Proc. Sci. Works Cherkasy State 24, 56–68. doi: 10.62660/
ebcstu/4.2023.56
Arifin, R., and Purnama, D. A. (2023). Identifying customer preferences on two competi-
tive Startupproducts: an analysis of sentiment expressions and textmining from Twitter
data. Jurnal Infotel 15, 66–74. doi: 10.20895/infotel.v15i1.906
Belwal, R., Belwal, S., Morgan, Z., and Al Badi, L. H. (2024). Profiling consumers for their
shopping motivations in modern retail formats in Oman. Int. J. Retail Distribut. 53, 74–93.
doi: 10.1108/IJRDM-09-2023-0581
Cardozo, R. N. (1965). An experimental study of customer effort, expectation, and satis-
faction. J. Mark. Res. 2, 244–249. doi: 10.1177/002224376500200303
Chen, X., Xiaofeng, S., Lin, W ., Anxin, X., Chen, J., and Zheng, Q. (2022). The effect of
Omnichannel integration on fresh food customer engagement from the viewpoint of flow
experience. Sustainability 14:13914. doi: 10.3390/su142113914
Chen, H., and Yin, L. (2023). Research on the coordination of fresh food supply chain
based on the perspective of blockchain and low carbon. Discret. Dyn. Nat. Soc. 2023, 1–20.
doi: 10.1155/2023/6156039
Chen, J., Zhang, B., and Zhu, Q.. (2022) Advantages of the new retail model in fresh
E-Commerce supply chain management: a case study of HEMA. Proceedings of the 2022
13th International Conference on 2022.
Cheng, L., Tan, F ., Jia, T., Y ang, X., and He, Z. (2026). Assessment of technical and
management practice gaps in controlling microbial hazards in fresh vegetables
among small-medium retailers in China. J. Food Prot.  89:100738. doi: 10.1016/j.
jfp.2026.100738
Činčalová, S., Suchánek, P ., and Prokop, M. (2021). Modelling customer satisfaction with
food. Qual. Innov. Prosperity 25, 65–84. doi: 10.12776/qip.v25i3.1618
Dai, X., and Liu, Q. (2024). Impact of artificial intelligence on consumer buying behaviors:
study about the online retail purchase. J. Infrastruct. Policy Dev. 8:7700 doi: 10.24294/jipd.
v8i9.7700
El Moussaoui, A. E., Benbba, B., and El Andaloussi, Z. (2022). Impact of logistics perfor-
mance on the store image, consumer satisfaction and loyalty: a quantitative case study.
Arab Gulf J. Sci. Res. 41, 226–239. doi: 10.1108/AGJSR-09-2022-0201
Erkmen, E., and Turegun, N. (2022). Success model of online food delivery system: the
role of brand image in customer responses. Innov. Mark. 18, 148–160. doi: 10.21511/
im.18(2).2022.13
Guan, G., Liu, D., and Zhai, J. (2022). Factors influencing consumer satisfaction of fresh
produce E-Commerce in the background of COVID-19—A hybrid approach based on
LDA-SEM-XGBoost. Sustainability 14:16392. doi: 10.3390/su142416392
Guiyang Municipal Bureau of Statistics, Guiyang Municipal Office of the Leading Group
for the Seventh National Population Census. (2021) Guiyang Municipal Bulletin on the
Seventh National Population Census (No. 1) — City-wide Population Situation. Available
online at: https://www.guiyang.gov.cn/zwgk/zfxxgks/fdzdgknr/tjxx/tjgb/202105/
t20210531_68342004.html (Accessed September 20, 2024)
Guizhou Provincial Bureau of Statistics, Guizhou Provincial Office of the Leading Group for
the Seventh National Population Census. (2021) Bulletin on the Seventh National Population
Census of Guizhou Province (No. 1) — Population Situation of the Province. Available online
at: https://www.guizhou.gov.cn/home/tzgg/202109/t20210913_70093110.html
(Accessed September 20, 2024)
He, P ., and Sun, Y . (2025). Research on a new fresh food logistics sharing mode
under carbon tax policy. Modern Supply Chain Res. Appl.  doi: 10.1108/
MSCRA-01-2024-0001
Hongxin, W ., and Yuhui, L. (2015). An empirical study on factors influencing consumer
satisfaction with online purchases of fresh agricultural products. Consumer Econ. 31,
81–86. doi: 10.19333/j.mfkj.20230400608
Hu, S., Zhang, J., and Zhu, Y . (2022). Zero to One: sales prospecting with augmented
recommendation. SSRN Electron. J. doi: 10.2139/ssrn.4006841
Kamal, A. M. (2025). Determinants of consumer choices: a deep dive into shopping pat-
terns. OTS Canadian J. 4:12. doi: 10.58840/g0nw3e51
Kang, J.-W ., and Namkung, Y . (2024). The role of service quality attributes and perceived
value in US consumers' impulsive buying intentions for fresh food E-commerce. J. Theor.
Appl. Electron. Commer. Res. 19, 1893–1906. doi: 10.3390/jtaer19030093
Kerschbaumer, R. H., Kreimer, D., Foscht, T., and Eisingerich, A. B. (2022). Subscription
commerce: an attachment theory perspective. Int. Rev. Retail Distrib. 33, 92–115. doi:
10.1080/09593969.2022.2134173
Kossen, J., Band, N., Lyle, C., Gomez, A. N., Rainforth, T., and Gal, Y . (2021). Self-
attention between datapoints: going beyond individual input-output pairs in deep learn-
ing. NIPS. doi: 10.48550/arXiv.2106.02584
Kovalskii, Y . V . (2024). The theoretical foundations of optimization of logistics chains in
the grain market. Bus. Inform 6, 399–406. doi: 10.32983/2222-4459-2024-6-399-406
Kumari, P ., Kumar, A., Burman, R. K., and Kumar, B.. (2024). Dynamic pricing strategies
of product for minimizing booking cancellation: using machine learning algorithm. 2024
IEEE International Women in Engineering (WIE).
Lestari, M., Romadlon, F ., and Nurisusilawati, I. (2024). Procurement strategy for fresh
vegetable produces to mitigate food waste in the retail sector. Sustinere. doi: 10.22515/
sustinere.jes.v8i3.384
Liao, J., Danese, P ., Vinelli, A., Xie, R., and Tang, J. (2021) A systematic literature review
on sustainable fresh food cold supply chain: state-of-the-art and future direction.
SDconference Proceedings.
López-Gálvez, F ., Gómez, P . A., Artés, F ., Artés-Hernández, F ., and Aguayo, E. (2021).
Interactions between microbial food safety and environmental sustainability in the fresh
produce supply chain. Foods 10:1655. doi: 10.3390/foods10071655
Ma, K., He, R.-K., and Gao, M. (2022). Design for product-service system innovation of
the new fresh retail in the context of chinese urban community. Ergon. Des. 186–193. doi:
10.54941/ahfe1001936
Maciel, W . R. E., LIMa-Filho, D. D. O., and Silva, F . Q. P . d. O. E. (2023). Perceived value
in food retail: moderating effect of store format. Caderno Pedagógico 20, 2179–2203. doi:
10.54033/cadpedv20n6-023
Mao, X. (2025). Online education quality assessment model based on deep learning. Mao
Discover Artif. Intel. 5:152. doi: 10.1007/s44163-025-00421-7
Messaoudi, F ., Loukili, M., and Ghazi, M. E.. (2023) Demand Prediction Using Sequential
Deep Learning Model. International Conference on Information Technology (ICIT),
Amman, Jordan, pp. 577–582.
Mittal, V . P . (2025). A comparative study of consumer satisfaction with online vs. offline
grocery shopping in Uttarakhand. Int. J. Sci. Res. Eng. doi: 10.55041/IJSREM55362
Naveuler, K. (2025). What drives purchases? A closer look at shopping determinants. OTS
Canadian J. 4, 42–46. doi: 10.58840/5mt68g63
Peng, L., Huan, W ., Gao, M., Yi, H., Xiong, Q., Y ang, L., et al. (2022). TLT: recurrent fine-
tuning transfer learning for water quality long-term prediction. Water Res. 225:119171.
doi: 10.1016/j.watres.2022.119171
Sajja, S., Aggarwal, N., Mukherjee, S., Manglik, K., Dwivedi, S., and Raykar, V .. (2021)
Explainable AI Based Interventions for Pre-season Decision Making in Fashion Retail.
8TH ACM IKDD CODS and 26TH COMAD.
Samonte, M. J., Britanico, E., Antonio, K. E. M., and Dela Vega, J. E. J.. (2022). Applying
deep learning for the prediction of retail store sales. Proceedings of the International
Conference on Industrial.
Sarker, M., Munerah, S., Yinyi, A. T., Kasem, N., and Hoque, I. (2024). What makes
consumers buy from the informal rather than formal retail market? A consumption value
perspective. Bottom Line 37, 309–331. doi: 10.1108/BL-07-2023-0225
Shen, A., He, Z., Zhang, J., Li, S., and Y ang, W . (2025). Development of biodegradable
modified starch composite films with Pleurotus Citrinopileatus polysaccharide and Nano

Yang et al. 10.3389/fsufs.2026.1866736
Frontiers in Sustainable Food Systems 21 frontiersin.org
titanium dioxide for enhanced fresh-cut yam preservation. Food Qual. Safety 9:fyaf011.
doi: 10.1093/fqsafe/fyaf011
Shen, L., Zhang, Y ., Fan, Y ., Chen, Y ., and Zhao, Y . (2022). Improving consumer stickiness
in livestream E-commerce: a mixed-methods study. Front. Psychol. 13:962786. doi:
10.3389/fpsyg.2022.962786
Singh, A., and Glińska-Neweś, A. (2022). Modeling the public attitude towards organic
foods: a big data and text mining approach. J. Big Data  9:2. doi: 10.1186/
s40537-021-00551-6
Song, C., Zheng, L., and Shan, X. (2022). An analysis of public opinions regarding inter-
net-famous food: A 2016–2019 case study on Dianping. Br. Food J. 124, 4462–4476. doi:
10.1108/BFJ-05-2021-0510
Thuannadee, S., and Praneetpholkrang, P . (2025). Effects of service quality, perceived
value, customer satisfaction on behavioral intentions in platform-based online food deliv-
ery services. Br. Food J. 128, 1874–1892. doi: 10.1108/BFJ-05-2025-0611
Tilshi, A., and Punsisi, P .. (2022). Special event item prediction system for retails using
neural network approach. Proceedings of the SLIIT International Conference on Engineering
and Technology.
United Nations General Assembly. (2015). Transforming our world: The 2030 Agenda for
Sustainable Development (A/RES/70/1). United Nations. Available online at: https://sdgs.
un.org/2030agenda
Valderrama, L., Valderrama, P ., and Carasek, E. (2021). A semi-quantitative model
through PLS-DA in the evaluation of Carbendazim in grape juices. Food Chem.
368:130742. doi: 10.1016/j.foodchem.2021.130742
Versino, F ., Ortega, F ., Monroy, Y ., Rivero, S., López, O. V ., and García, M. A. (2023).
Sustainable and bio-based food packaging: a review on past and current design innova-
tions. FOODS 12:1057. doi: 10.3390/foods12051057
Wang, Z., Liu, X., and Wang, Y . (2024). Research on vegetable sales volume and pricing
strategy based on GWO-LSTM modeling. J. Comput. Electron. Informat. Manag. 12,
64–70. doi: 10.54097/g2xl0vlzbh
Wang, J., Shiwei, X., Zhang, S., Sun, C., and Linhai, W . (2023). Research on the impact of
consumer experience satisfaction on green food repurchase intention. Foods 12:4510. doi:
10.3390/foods12244510
Wang, Z., and Theerakittikul, S.. (2022). Factors affecting customer satisfaction with
Haidilao Hot Pot in Bangkok", 2022 7th International Conference on Business.
Wang, H. X., and Liu, Y . H. (2015). An empirical study on factors
influencing consumer satisfaction in online purchasing
of fresh agricultural products. Consumer Economics, 31, 81–86.
White, B. L. (2022). Insights-driven development of humanized foods for pets. Meat
Muscle Biol. 6, 1–12. doi: 10.22175/mmb.14397
Xin, L., Y ongshi, H., Bo, S., et al. (2024). Development of a deep learning-based sales
forecasting model for fast fashion apparel products. Wool Textile Sci. Technol. 52, 80–87.
doi: 10.19333/j.mfkj.20230400608
Xing, J., Zhang, J., and Wang, X. (2024). Understanding the Chinese online fresh agricul-
tural market through the extended technology acceptance model: the moderating role of
food safety trust. Asia Pac. J. Mark. Logist.  36, 1576–1594. doi: 10.1108/
apjml-08-2023-0794
Xu, J., Luo, Z., Zhang, X., Li, Z., Li, D., Chen, Y ., et al. (2025). Revolutionizing fresh
food quality control in supply chains with machine learning: current advances and
future challenges. Compr. Rev. Food Sci. Food Saf.  25:e70360. doi:
10.1111/1541-4337.70360
Xu, Y ., Zhang, J., and Deng, G. (2022). Enhancing customer satisfaction with Chatbots:
the influence of communication styles and consumer attachment anxiety. Front. Psychol.
13:902782. doi: 10.3389/fpsyg.2022.902782
Y ang, Q., Xiong, L., Li, Y ., Chen, Q., Yijing, Y ., and Wang, J. (2022). Contract coordination
of fresh agri-product supply chain under O2O model. Sustainability 14:8771. doi:
10.3390/su14148771
Y ao, J. (2025). An exploration of the evolution of China's retail channels - a case study of
Procter & Gamble. Adv. Econ. Manag. Polit. Sci. doi: 10.54254/2754-1169/2025.GL28413
Y aqub, R. M. S., Azhar, M. S., Hameed, W ., and Murad, M. (2022). Role of Web
Design, E-Payment and E-Traceability with mediating role of consumer behavior
to develop customer satisfaction for emerging bricks and clicks business model
trends in south Punjab. Rev. Educ. Adm. Law . 5, 123–135. doi: 10.47067/real.
v5i2.224
Yılmaz, Ci̇han, and Balcıoğlu, Y . S. (2026). Consumer preferences and satisfaction pat-
terns across food categories: A large-scale analysis of product attributes, market segments
and temporal dynamics in online food reviews. Br. Food J. , 1–28. doi: 10.1108/
BFJ-09-2025-1159
Yuan, Y ., Si, Z., and Zhong, T. (2026). The semi-formalization of wet markets in Urban
China: a hybrid social infrastructure for urban resilience and food security. Sustainability
18:1613. doi: 10.3390/su18031613
Zhang, Z., and Liang, H. (2023). Research on the relationship between service quality and
customer loyalty for fresh food E-commerce in the background of new retail. J. Bus.
Manag. Sci. 11, 83–89. doi: 10.12691/jbms-11-1-6
Zhang, E., Zhou, Y ., Chen, G., and Wang, G. (2024). Classified spatial clustering and
influencing factors of new retail stores: a case study of Freshippo in Shanghai.
Sustainability 16:6643. doi: 10.3390/su16156643
Zhongwang News. (2022) “Guihuihui” Online Fresh Produce Mall Officially Launched.
Available online at: http://swt.guizhou.gov.cn/xwzx/gzdt/202204/t20220407_73268079.html
(Accessed September 20, 2024)
