---
title: Evaluating the Effectiveness of Digital Product Advertisement Type using Machine Learning and Shapley
  Additive Explanations Analysis
url: https://doi.org/10.32890/jict2026.25.1.5
category: survey
subcategory: review
date: 2026-01
venue: Journal of Information and Communication Technology
authors:
- Khinsa Fairuz Zahirah
- Winarto Poernomo
- Eddy Yusuf
source: openalex-oa
pdf_url: https://e-journal.uum.edu.my/index.php/jict/article/download/28081/5015
pages: 28
chars: 80106
fetched_at: '2026-11-08T17:16:17+00:00'
kb_version: 1
---

# Evaluating the Effectiveness of Digital Product Advertisement Type using Machine Learning and Shapley Additive Explanations Analysis

Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

79

How to cite this article:
Zahirah, K. F., Poernomo, W., Yusuf, E., & Bernardus, D. (2026). Evaluating the effectiveness of digital product advertisement
type using machine learning and shapley additive explanations analysis. Journal of Information and Communication
Technology, 25(1), 79-106. https://doi.org/10.32890/jict2026.25.1.5

Evaluating the Effectiveness of Digital Product Advertisement  Type
using Machine Learning and Shapley Additive Explanations Analysis

1Khinsa Fairuz Zahirah, 2Winarto Poernomo, 3Eddy Yusuf & 4Denny Bernardus
1School of Information System, Universitas Ciputra Surabaya, Indonesia
2&4School of Business and Management, Universitas Ciputra Surabaya, Indonesia
3School of Information Technology, Universitas Ciputra Surabaya, Indonesia

*1khinsa.zahirah@ciputra.ac.id
2winarto.poernomo@ciputra.ac.id
3eddy.yusuf@ciputra.ac.id
4denny@ciputra.ac.id
*Corresponding author

Received: 20/1/2025 Revised: 19/1/2026  Accepted: 19/1/2026 Published: 31/1/2026

ABSTRACT

Digital advertising continues to grow rapidly, yet advertisers face persistent uncertainty in selecting the
most effective ad format for different campaign objectives and audience segments. Prior studies often
rely on limited metrics or lack interpretability, making it difficult to explain why certain formats
perform better.  This study addresses t his gap by evaluating ad format effectiveness using explainable
machine learning. This study evaluates the effectiveness of image and video advertisements (ads) across five
key performance indicators (KPIs):  reach, impressions, link clicks , cost per click (CPC), and cost per
thousand impressions (CPM). A dataset of 4,526 campaigns from Meta Ads Manager (July 2021 –August
2024) was analysed using machine learning models integrated with Shapley Additive Explanations (SHAP).
Model performance was assessed using  Mean Squared Error (MSE), Root Mean Squared Error (RMSE),
Mean Absolute Error (MAE), and R -squared (R²). The results showed that video ads achieve d higher
reach and impressions with lower CPM. Meanwhile, image ads delivered lower CPCs and stronger click
performance, particularly among users aged 13–17 and 55+. Aside from confirming established format
patterns, this study made certain contributions  by applying explainable machine learning in a large -
scale, non-Western context and by clarifying the mechanisms behind ad performance. The findings
offered actionable guidance ; for example , video ads were optimal for awareness and visibility
objectives. Additionally, image ads were preferable for engagement-driven campaigns.

Keywords: Ad type, digital advertising, machine learning, SHAP analysis.

JOURNAL OF INFORMATION AND
COMMUNICATION TECHNOLOGY
e-journal.uum.edu.my/index.php/jict

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

80

INTRODUCTION

Global digital ad spending is expected to exceed $400 billion, representing over 60% growth from 2022
(Yoon, 2022). This growth showed the influence of digital marketing on consumer behaviour. In
addition, image and video advertisements (ads) dominated the diverse formats, with each characterised
by distinct advantages. Previous studies reported that image ads were simple and easy to process, while
video ads provided valuable storytelling and emotional appeal (Grewal et al., 2021). Selecting the
appropriate format was essential to  maximising return on investment (ROI). It required more than
surface comparisons ; it demanded a thorough examination of the factors that triggered consumer
responses. Traditional statistical methods were unsuccessful in analysing digital ad performance. These
methods struggled with complex human behaviours, which failed to account for endogenous variables,
and often introduce d specification errors (Farahat & Shanahan, 2013). Outdated information bias
detected during collection further undermine d accuracy (Prosekov, 2020). Prior studies reported that
interpreting ad platform data remained a challenge due to  limited ability to draw actionable insights
(Braun et al., 2023).

Aside from being foundational, traditional analytics were unable to keep pace with the complexity of
modern digital data, which includes  high-dimensional variables, intricate interactions, and  non-linear
relationships. These factors often obscured critical insights, creating gaps in understanding the variables
that drove ad success. Additionally, there was a need for tools that could thoroughly process the
complexity. Recent studies have focuse d on how artificial intelligence and network analytics are
shaping digital marketing decisions. For example, Abu Bakar et al. (2025) reported that AI-driven
social-network models effectively identif ied influential sellers and products in e -commerce
environments, reinforcing the strategic significance of data-driven engagement measurement in online
advertising contexts. In this context, machine learning (ML) offered a major advantage over traditional
methods by avoiding subjective judgment. It improved precision and enabled more accurate predictions
of consumer behaviour (Osakwe et al., 2023). ML models also uncovered subtle patterns and
relationships in complex data, which offered a more precise evaluation of ad performance. The models
helped explain the functions and performances of certain ad features.

The Shapley Additive Explanations (SHAP) analysis was conducted to evaluate and incorporate model
outputs into value -based contributions from each feature , thereby improving interpretability. In
addition, this method was used to translate ML results into meaningful, strategic insights. The method
has also been proven useful in other fields such as public policy, energy and business, where it extracted
insights from consumer satisfaction data (de Carvalh o & da Silva, 2021), supported grid stability
planning (Hamilton & Papadopoulos, 2023), and clarified demand forecasts in direct sales (Arboleda-
Florez & Castro -Zuluaga, 2023) , respectively . Furthermore, SHAP is prominent for its theoretical
soundness and practical relevance , compared to tools such as Local Interpretable Model -agnostic
Explanations (LIME) and permutation importance (Kedar, 2024).

Previous studies had three limitations: first, the majority focused on a single metric , namely click-
through rate (CTR) or conversions, excluding visibility–cost trade-offs (i.e., reach, impressions, CPC,
cost per mille (CPM)). For example, Patil et al. (2022) adopted CTR and click data to improve campaign
strategies. Lakshmanarao et al. (2021) also used reinforcement learning to optimise ad positioning.
Second, few studies adopted explainable ML methods to show why format effects differ ed across
audience segments and campaign objectives. Third, most large -scale analyses were conducted  in
Western or platform -agnostic settings, leaving a gap in evidence from non -Western, platform-native
contexts. Therefore, the present study addressed these gaps by applying ML models and SHAP analysis

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

81

to evaluate image and video ads across multiple key performance indicators (KPIs), explicitly modelling
interactions among format, audience, and objective. The insights guided advertisers in selecting creative
formats that aligned with campaign objectives and demographics. Based on this perspective, the present
study aimed to:

1. Compare the effectiveness of image and video ads across reach, impressions, link clicks, CPC,
and CPM.
2. Examine how demographics interact with ad formats to affect outcomes.
3. Identify significant performance drivers and provide actionable guidance for ad optimisation.

The combination of ML and SHAP analysis enabled performance assessment and  explained the
associated mechanisms. These insights helped marketers match ad formats to audience preferences and
campaign objectives, improving both cost efficiency and engagement.

RELATED WORKS

The combination of ML models and SHAP analysis was a promising approach for evaluating  the
effectiveness of image and video advertisements across various KPIs. This review synthesised studies
on the application of ML to ad performance, the role of KPIs in digital advertising, the comparative
effectiveness of image and video ad formats, and the interpretability provided by SHAP analysis.

Comparing Image and Video Ad Effectiveness

The effectiveness of image and video ads dep ended on audience engagement and campaign KPIs.
Previous studies reported that video ads generally outperformed images in terms of reach, impressions,
and interaction rates, making them effective for cost-efficient engagement and emotional storytelling
(Grewal et al., 2021; Tavares et al., 2023). Video content enhanced brand recall and consumer interest,
with emotional messaging driving stronger engagement and conversions than static images
(Prihatiningsih et al., 2024; Félegyházi, 2024). In context-related settings, midroll video ads were most
effective at boosting brand recall and  shaping related attitudes (Stewart et al., 2023).  Image ads
performed better in direct engagement, particularly in transactional or community -driven campaigns.
These ads often achieved higher CTR and were more cost-efficient per view (Northcott et al., 2021;
Mihajlović et al., 2024). The clarity and visual simplicity prompted quick actions, such as app
downloads or ticket purchases, outperforming video ads in reactions, comments, and shares (Tavares et
al., 2023; Stewart et al., 2023). Ad -context congruence also influenced performance, while image ads
benefited more with consistent content across digital platforms (Xie et al., 2024).

The s trategic combination of both formats, based on campaign objectives and audience behaviour,
maximised results. Video and image ads supported long-term brand building and immediate responses,
respectively (Grewal et al., 2021; Northcott et al., 2021). Moreover, Chumwatana (2018) explored
comment- and sentiment -analysis methods using Thai social -media reviews to assess customer
satisfaction. This study described the relevance of linguistic and cultural factors in interpreting
consumer reactions to visual content, an aspect that complemented analyses comparing the effectiveness
of image and video ad s. The findings described the significance of selecting ad formats based on
context, audience segmentation, and marketing objectives, as shown in Table 1.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

82

Table 1

Related Works for Image and Video Ad Effectiveness

System Methodology Results
Grewal et al. (2021)
Used multimedia data (video, image, text,
audio) with ML and NLP fusion to
analyse and predict ad outcomes.
Video ads drive stronger emotion and
storytelling; image ads perform better
for direct response. Combining both
maximises effectiveness.
Tavares et al. (2023)
Analysed Facebook campaigns
comparing video and image formats
across engagement metrics (reach,
impressions, CPM, cost, reactions,
shares).
Video ads outperformed in reach,
impressions, and CPM; image ads led
in comments, reactions, and shares.
Prihatiningsih
et al. (2024)
Applied quantitative survey with
descriptive and inferential analysis to
assess ad engagement.
Video content sustains attention longer
and delivers higher engagement and
conversion than static images.
Félegyházi (2024)
Conducted A/B testing of visual ad
formats to evaluate engagement and
performance.
Video ads achieved lower click costs
and higher engagement; optimising
visual content boosts campaign
success.
Stewart et al. (2023)
Combined online experiment and field
study comparing Facebook ad formats
using vividness and fit theory.
Image ads generated more purchase
clicks; video ads increased social
engagement.
Northcott et al. (2021)
Compared image vs. video ads by cost
efficiency and engagement (CTR,
downloads).
Image ads were more cost -effective
and achieved higher reach and
engagement.
Mihajlovic et al.
(2024)
Used A/B testing on static vs. animated
images and carousel posts.
Static image a ds had lower CPC and
higher ROI; carousel posts
outperformed video ads by ~32% ROI.
Xie et al. (2024)
Analysed 6 million Snapchat user
sessions to assess ad -context and format
congruence.
Content congruence increased viewing
time; format congruence benefi ted
image ads but reduced video ad views.

ML in Advertising Performance

ML has transformed digital advertising by replacing intuition -based methods with data -driven
strategies. These technologies enable d precise predictions of campaign performance, audience
targeting, and ad optimisation, leading to improved engagement, including ROI (Chavda & Patel, 2024).
The significant  applications included intelligent bidding, audience segmentation, and automated ad
placements, which ensured ads reached the appropriate audiences and at the right time (Booth, 2019).
Additionally, d eep learning and natural language processing (NLP) enhance d personalisation by
analysing sentiment and refining campaigns in real time (Nwaimo et al., 2024; Ji et al., 2024).

Yang et al. (2019) reported that tools such as Baidu’s AiAds system influenced ML by refining bidding
strategies and maximi sing performance. Furthermore, a dvanced algorithms such as  reinforcement
learning optimised ad positioning. Predictive models also forecasted essential metrics, including CTR,
campaign profitability, and return on ad spending (ROAS) (Lakshmanarao et al., 2021; Jha et al., 2024).
These innovations empowered advertisers to make informed decisions, alloc ate resources effectively,
and achieve measurable outcomes. Complementing the advances, Ismail and Yusof (2022)

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

83

systematically reviewed ten years of machine -learning prediction studies based on open data . It was
reported that integrating open datasets and ML methods enabled more accurate, scalable forecasting
across social-network and marketing applications. The findings outlined the value of transparent, data-
rich environments for improving predictive accuracy and guiding marketing optimisation. The ongoing
evolution of ML further enhanced the efficiency  and strategic impact of advertising. Table 2 presents
related work on ML in advertising.

Table 2

Related Works for ML in Advertising

Authors Methodology Results
Patil et al. (2022)
ML models were developed and
evaluated to predict CTR and ad clicks on
social media platforms.
The study developed a n ML model to
predict CTR and ad  clicks, providing
insights to optimise the effectiveness and
efficiency of advertising campaigns.
Lakshmanarao et al.
(2021)
The study utili sed a Kaggle dataset and
applied two reinforcement learning
algorithms, Upper Confidence Bound and
Thompson Sampling, to predict ad
positions based on ad clicks,
implemented in Python.
The study achieved high accur acy and
demonstrated that ad placement
significantly influences click rates.
Chavda and Patel
(2024)
Systematic review of the existing
literature on using ML to enhance online
advertising ROI
Integrating ML enhances online
advertising by analysing large data sets to
identify target audiences, predict
potential customers, and maximise ROI.
Ji et al. (2024)
The study used ML models to analyse
customer behaviour data, predict user
intent, and enhance personali sation in e -
commerce and targeted advertising.
ML has transformed advertising by
enabling precise targeting and engaging
experiences through advanced data
processing and analysis, surpassing
traditional intuition-based methods.
Yang et al. (2019)
The stud y included the design,
development, and implementation of the
AiAds system by Baidu, leveraging ML
methods to automate core components of
the sponsored search process.
The AiAds system significantly
enhances advertiser campaign
performance, user experience , and
advertising platform revenue in the
sponsored search ecosystem.
Jha et al. (2024)
The study conducts experimental
simulations of various RTB methods
using real-world datasets and advertising
campaigns, analysing its performance
across metrics.
The analysis identifies that the
Constrained Markov Decision Process -
based model outperformed other
methods across key metrics, achieving
higher CTRs, CRs, and ROI, while
optimising win rates, CPM, and E-CPC.
Kedi et al. (2024)
The study analyses existing lit erature,
case studies, and tools to evaluate how
ML enhances social media advertising
through audience segmentation,
predictive analytics, and campaign
optimisation.
ML enhanced advertising efficiency and
personalisation. This method  helped
SMEs overcome r esource constraints .
However, challenges such as data quality
and technical expertise persisted.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

84

SHAP Analysis in ML for Ad Interpretability

SHAP analysis is a significant tool for improving the interpretability of ML models in marketing
analytics. Developed by Lundberg and Lee (2017), this tool assigned importance scores to features,
offering clear insights into how each input affected model predictions. Its flexibility made it worthwhile
across a range of complex models, including deep neural networks and ensemble methods (Rodríguez-
Pérez & Bajorath, 2020).

In marketing and sales, SHAP help ed refine demand forecasting by isolating the impact of individual
features, enabling businesses to effectively integrate ML insi ghts into decision -making (Arboleda-
Florez & Castro-Zuluaga, 2023). Considering computational advertising, it clarified both global model
behaviour and feature importance across categories. For example, visual content played a relevant role,
with SHAP showing how its impact varied by product type and supporting  more designed strategies
(Santos, 2023). Regarding advertising, SHAP helped interpret the outcomes of high-accuracy models.
For example, this tool was used to explain a Random Forest model that predicted user behaviour with
97.67% accuracy (Al -Khafaji & Karan, 2024). The insights enable d advertisers to understand the
diverse variables, such as ad type, content, and targeting, that  impact performance (Zhao & Harinen,
2019). Even when general and c ategory-specific click models performed similarly, SHAP reveal ed
feature patterns that support ed personalised strategies (Santos, 2023). At the individual level, it also
helped reduce misclassification and supported predictions aligned with business objectives.

These findings outlined the value of explainable Artificial Intelligence (AI) in marketing. Furthermore,
tools such as SHAP helped marketers to strike a balance between predictive accuracy and transparency,
enabling the ethical and effective applications of ML. SHAP also played a major role in building trust,
driving the adoption of AI in advertising.  Previous studies on online advertising reviewed three main
gaps. First, the majority optimised a single outcome , such as CTR or conversions , without jointly
modelling visibility and cost metrics. As a result, the trade-offs among CPM, CPC, reach, impressions,
and clicks were not fully understood (Yang & Zhai, 2022; Asdemir, Kumar, & Jacob, 2012). Second,
explainable ML methods, including SHAP, have been applied in other domains, but advertising analysis
has not systematically used them to identify how demographic factors, budgets, and objectives interact
with creative formats (Lundberg & Lee, 2017; Cunha & Barbosa, 2024). Third, the existing evidence
base was dominated by Western or platform -agnostic datasets, ignoring large-scale, platform-native
studies in non-Western contexts (Huang et al., 2020).

This study addresse d the gaps by comparing image and video ads across five KPIs , namely reach,
impressions, link clicks, CPM, and CPC , using an explainable ML framework. A model format -
audience-objective interactions was explicitly incorporated in first-party Meta Ads Manager data from
Indonesia, thereby extending the evidence base beyond Western contexts.

THE PROPOSED METHOD

This study adopted a multi -outcome modelling method that combine d predictive accuracy with
interpretability. ML was used to predict campaign outcomes, while SHAP values provided transparent,
feature-level attributions. This integrated  design allow ed the (i) comparison of image and video
performances across five KPIs, (ii) attributed differences to campaign features such as budget, audience
age, and objective, as well as (iii) translated results into actionable recommendations for advertisers. In
addition, the study advance d beyond average -effect comparisons , offering goal-conditioned
prescriptions for creative choice.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

85

The analysis used data from the Meta Ads Manager platform, designed by an educational institution in
Indonesia. The dataset included 4,526 ad campaign records collected between July 2021 and August
2024. All data handling procedures adhered to ethical guidelines approved by the institution’s review
board, ensuring compliance with privacy regulations. Personal information was anonymised to protect
individuals’ privacy, thereby supporting applicable data protection laws. The analysis was conducted
mainly in Google Colab for its accessibility and ease of use. Python 3.10.12 was also used with the
necessary libraries preloaded for efficiency.

Dataset

The original dataset comprised 13 columns, with 2 additional features engineered to enrich the dataset.
Furthermore, the campaign duration was calculated by subtracting the start date from the end date. The
ad type was derived from patterns in the campaign name and ad set name, classifying each as either
image-based or video-based. After feature engineering, the campaign name, ad set name, start, and end
were removed from the dataset to focus the analysis on relevant variables. A detailed description of the
refined dataset is shown in Table 3.

Table 3

Refined Dataset Description

Column
No. Column Name Column Type Description
1 Objective Feature
The goal of the ad campaign ( e.g., brand awareness,
conversions, lead generation, link clicks, outcome
awareness, outcome engagement, outcome leads, and
outcome sales).
2 Age Feature The age group targeted by the ad (13 -17, 18-24, 25- 34, 35-44, 45-54, 55-64, 65+).
3 Gender Feature The gender targeted by the ad (male, female).
4 Reach Target The number of unique users who saw the ad at least once.
5 Impressions Target The total number of times the ad was shown to users (may include repeats).
6 Amount spent (IDR) Feature The total cost spent on the ad campaign in Indonesian Rupiah (IDR).
7 Link clicks Target The number of times users clicked on the ad link.
8 CPC Target The average cost for each link click (Amount spent/Link clicks).
9 CPM Target The cost of the ad per 1,000 impressions (Amount spent / Impressions × 1,000).
10 Campaign Duration Feature The length of time the ad campaign was active (e.g., 7 days, 14 days, 30 days, etc.).
11 Ad type Feature The format of the ad (image, video).

Campaigns with zero values in KPIs such as reach, impressions, link clicks, CPC, and CPM were
excluded to ensure solid analysis. The removal of those with missing values  reduced the dataset from
4,526 to 4,289 rows. These steps helped maintain a dataset tha t was both comprehensive and relevant
for addressing the proposed study questions (Das et al., 2023).

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

86

Data Pre-processing

The dataset was subjected to pre-processing before analysis, with categorical variables, namely gender,
age group , objective, and ad type, transformed into numerical format . It was realised using label
encoding, which assigned a unique integer value to each category (Das et al., 2023). Binary variables
such as gender and ad type were encoded as 0 and 1, respectively. Gender was encoded as 0 for female
and 1 for male, while ad type was encoded as 0 for image and 1 for video. For multi-category features,
age group (seven age ranges) and objective (eight distinct campaign objectives) were encoded
sequentially as 0-6 and 0-7, respectively.

Label encoding was preferred over one-hot encoding to maintain data compactness and computational
efficiency, particularly considering the presence of multiple categorical features (Kosaraju et al., 2023).
This method ensured uniqueness within feature clas ses while minimising dimensionality (Hancock &
Khoshgoftaar, 2020).  Following encoding, numerical variables were normali sed to standardi se
respective scales and enhance model interpretability , including performance (Das et al., 2023). Min -
max scaling was applied to transform each feature to a [0, 1] range, using the formula in Equation 1.

xscaled = (x – xmin) / (xmax – xmin) (1)

Where x is the original data value, xmin denotes the minimum value of x in the dataset, xmax refers to the
maximum value of x in the dataset, and xscaled is the normalised (scaled) value of x.

This normali sation prevent ed features with larger magnitudes (e.g., amount spent) from
disproportionately influencing the model over smaller -scale features (e.g., C PC), thereby improving
learning stability and comparability (scikit -learn, 2019; mljourney, 2024). Considering alternative
normalisation methods, such as Z-score standardisation, robust scaling, and log transformation, Min -
max scaling was selected for two main reasons. First, the dataset lacked significant outliers, reducing
the risk of distortion . Second, it preserved the original distribution shape of the features, which is
important for interpretability.  Before training the models, exploratory data analy sis (EDA) was
conducted to understand feature relationship s. It included comparison charts, heatmaps, and feature -
importance scores. In addition, the findings from this phase were discussed in the results section.

ML

ML was applied in two main stages, namely (i) prediction of advertising KPIs and (ii) interpretation of
feature contributions using SHAP. The prediction of ad effectiveness led to splitting the dataset into
training (80%) and test (20%). It followed standard practice to ensure sufficient data for model learning
and unbiased evaluation (Das et al., 2023). Meanwhile, t hree supervised regression models were
implemented, namely Linear Regression, Decision Tree, and Random Forest . These were selected for
their complementary strengths in handling feature imbalances and non -linear relationships.  Linear
Regression served as the baseline due to its simplicity, speed, and interpretability (Das et al., 2023).
This model also assumed a linear connection between features and their target, using Ordinary Least
Squares (OLS) to minimise residual errors. It struggled with non-linear patterns, despite enabling the
understanding of the relationship strength and direction. Linear Regression  also relied on strict
assumptions, including linearity, normal residuals, and low multicollinearity.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

87

Decision Trees provided more flexibility, capturing non -linear relationships through recursive splits
based on feature values (Das et al., 2023). Its structure is easy to interpret, with clear decision paths
(Kovalerchuk et al., 2023). The model also handled imbalanced features effectively by prioritising more
informative variables (Liu et al., 2021), and processed  both categorical and numerical data without
transformation. Random Forest extended Decision Tree functionality by averaging predictions across
multiple trees trained on random subsets of data and features (Das et al., 2023). This ensemble method
reduced overfitting and improve d generalisation, specifically with imbalanced data. The model
minimised feature dominance and increased model diversity by introducing randomness into sampling
and feature selection (Ye et al., 2020). It also outputted feature importance metrics, thereby helping
identify significant performance drivers.

These models collaboratively offered a balanced framework , realised by combining interpretability,
complexity handling, and robustness . The essence was to generate meaningful insights into ad
performance, even in data with feature imbalances (Liu et al., 2021; Ye et al., 2020; Balcan & Sharma,
2024). After identifying the best -performing model, SHAP analysis was conducted to enhance
interpretability. The values quantified the marginal contribution of each feature to the model’s
predictions, thereby connecting predictive performance with actionable business insights. It led to the
use of ML to improve predictive accuracy and to explain the drivers of ad effectiveness.

Evaluation Metrics

Evaluation metrics played an essential role in assessing ML models. It led to the adoption  of four
metrics, namely Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error
(MAE), and R -squared (R²). Additionally, e ach metric offered a distinct perspective on model
performance, ensuring a  comprehensive evalu ation. MSE measure d the average of the squared
differences between predicted and actual values. The metric detected larger errors, leading to significant
deviations and an overly sensitive respons e to outliers (Das et al., 2023). RMSE is the square root of
MSE, which provides error magnitude in the same units as the target variable . Additionally, it was
specifically helpful when significant errors were a concern (Das et al., 2023). MAE calculate d the
average absolute difference between predicted and actual values. Compared to MSE and RMSE, it does
not square errors, which reduces sensitivity to outliers. The metric produced a straightforward measure
of average error (Das et al., 2023) , with R² (coefficient of determination) measuring the proportion of
variance in the target variable explained by the model. Moreover, higher values within the range of 0
to 1 represented a better fit. Unlike error metrics, R² measures how well the model captures basic data
patterns (Chicco et al., 2021). The formulas used to calculate each metric are presented in Equations 2-5.

MSE =
1
𝑛 ∑ (𝑦𝑎𝑐𝑡𝑢𝑎𝑙,𝑖 − 𝑦𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑,𝑖)2𝑛 𝑖=1  (2)

RMSE =√1 𝑛 ∑ (𝑦𝑎𝑐𝑡𝑢𝑎𝑙,𝑖 − 𝑦𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑,𝑖)2𝑛 𝑖=1  (3)

MAE =
1
𝑛 ∑ |𝑦𝑎𝑐𝑡𝑢𝑎𝑙,𝑖 − 𝑦𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑,𝑖|𝑛 𝑖=1  (4)

R2 = 1 −  ∑ (𝑦𝑎𝑐𝑡𝑢𝑎𝑙,𝑖−𝑦𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑,𝑖)2𝑛 𝑖=1
∑ (𝑦𝑎𝑐𝑡𝑢𝑎𝑙,𝑖−y̅)2𝑛 𝑖=1  (5)

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

88

Where n is the total number of data points, 𝑦𝑎𝑐𝑡𝑢𝑎𝑙,𝑖 denotes the actual (true) value for the 𝑖𝑡ℎ data point,
𝑦𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑,𝑖 refers to the predicted value for the 𝑖𝑡ℎ data point, and 𝑦̅ represents the mean of all actual
target values. Each metric captured a different dimension of model performance, MSE focused on large
errors, RMSE present ed error in usa ble units, MAE offer ed robustness to outliers, and R² disclosed
explanatory power. However, when combined, the metrics provided a complete view of accuracy and
generalisability.

SHAP Analysis

Post hoc SHAP analysis was conducted to enhance interpretability and complement model evaluation.
The analysis  interpreted ML predictions by attributing contributions to individual features  using
cooperative game theory (Lundberg & Lee, 2017). It explain ed the model’s prediction by distributing
the difference between the output and baseline values  across all input features (Das et al., 2023). The
values obtained were derived using the Shapley value formula, stated in Equation 6.

𝜑𝑖 = ∑ |𝑆|!(|𝐹|−|𝑆|−1)! |𝐹|!𝑆⊆𝐹{𝑖} [𝑓(𝑆 ∪ {𝑖}) − 𝑓(𝑆)]    (6)

Where 𝜑𝑖 is the Shapley value for feature I (represent ing the contribution of feature i to the model’s
prediction), 𝑆 refers to a subset of features from 𝐹 that does not include feature I, 𝐹 denotes the set of
all features, 𝑓(𝑆) represents the model prediction using only the features in subset 𝑆, and 𝑓(𝑆 ∪ {𝑖}) is
the model prediction which adopted the features in 𝑆, including those in i.

This formula calculated the average marginal contribution of each feature across all possible subsets .
Based on previous studies, the formula ensured a fair and comprehensive assessment of feature
influence (Lundberg & Lee, 2017). SHAP bridged accuracy and interpretability by clearly showing how
features triggered predictions. It also provided a transparent breakdown of model behaviour, helping
identify which variables most influenced campaign success. It produced results that were  both
technically rigorous and practically valuable for optimi sing advertising strategies.  The experimental
setup consisted of training three regression models , namely Linear Regression, Decision Tree, and
Random Forest, on 4,289 campaigns, using demographic and campaign features to predict five KPIs.
An 80/20 train –test split was used to evaluate the models using MSE, RMSE, MAE, and R², while
SHAP was applied to the best model for interpretation.

EVALUATION AND RESULTS

Descriptive Statistics and Preliminary Analysis

Descriptive analysis was conducted to examine the overall structure and distribution of the dataset
before the application of ML models. Table 4 shows the summary statistics for all normalised numerical
features. Most variables exhibited low means, such as reach (0.02), impressions (0.03), and link clicks
(0.01), representing modest campaign engagement. The age distribution was skewed toward younger
users, and the low mean of ad type (0.04) suggested that image ads dominated the dataset. The gender
balance was evidence of equal representation (mean = 0.50, standard deviation = 0.50), reflecting equal
representation of male- and female-targeted ads.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

89

Table 4

Descriptive Statistics

Statistics (n=4,289) Mean Standard Deviation (SD) Min 25% 50% 75% Max
Objective 0.55 0.36 0.00 0.14 0.43 0.86 1.00
Age 0.27 0.28 0.00 0.00 0.17 0.50 1.00
Gender 0.50 0.50 0.00 0.00 0.00 1.00 1.00
Reach 0.02 0.04 0.00 0.00 0.01 0.02 1.00
Impressions 0.03 0.06 0.00 0.00 0.01 0.03 1.00
Amount spent (IDR) 0.05 0.07 0.00 0.01 0.03 0.06 1.00
Link clicks 0.01 0.03 0.00 0.00 0.00 0.01 1.00
CPC 0.01 0.03 0.00 0.00 0.00 0.01 1.00
CPM 0.02 0.03 0.00 0.01 0.01 0.03 1.00
Campaign duration 0.36 0.19 0.00 0.20 0.39 0.49 1.00
Ad type 0.04 0.20 0.00 0.00 0.00 0.00 1.00

The descriptive statistics outlined the dominance of image-based ads. The ad type variable had a mean
of 0.04 and extremely low percentiles, which confirmed a sharply imbalanced distribution. This
imbalance was retained to mirror real -world campaign conditions and preserve external validity
(Johnson & Khoshgoftaar, 2019; Lusito et al., 2023). Figure 1 shows the visualised distribution of ad
type.

Figure 1

Distribution of Ad Type

Descriptive statistics for reach, impressions, link clicks, CPC, and CPM show ed a transparent age
gradient. Reach peaks in the 13 to 24 segment for video ads, comprising more than 200,000 users aged
13 to 17. However, this declined sharply in older groups, as shown in Figure 2. Impressions followed a
similar pattern to Figure 3, with video ads dominating across every cohort except users  aged 25 to 34,
due to lower engagement.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

90

Figure 2

Reach by Age and Ad Type

Figure 3

Impressions by Age and Ad Type

Engagement patterns diverge d when examining link clicks , with  video ads outperform ing images
among 35 to 54-year-olds. Meanwhile, image ads were for users aged 13–34, including those aged 55
and above, as shown in Figure 4. Gender played a minor role, and video ads were more effective for
men, but neither was statistically significant (Figure 5).

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

91

Figure 4

Link clicks by Age and Ad Type

Figure 5

Link clicks by Gender and Ad Type

Figure 6  describes video ads’ higher CPC, specifically within the 13 –17 and 35 –54 age ranges.
Furthermore, image ads maintained more consistent and lower CPCs across age groups.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

92

Figure 6

CPC by Age and Ad Type

Figure 7 shows that video ads were more cost-efficient (i.e., CPM) for impressions across all age groups.
The highest CPM s for image ads were recorded in the 35 –64 age range, while video ads ha d lower
CPMs in that age range. However, even in age groups with low video engagement (e.g., 25–34), video
ads still achieved better CPM, suggesting efficient budget allocation in auctions.

Figure 7

CPM by Age and Ad Type

The Spearman rank correlation was used to assess the strength and direction of the variables'
relationship and to better understand the relationship. The heatmap in Figure 8 visuali sed the strength
of correlations between variables, with red indicating positive correlations and blue negative ones. The
intensity of the shades reflect ed the strength of the correlation . Additionally, darker shades indicated
stronger correlations, as discussed in detail in the following section. The initial observation was that ad
type, gender, and campaign duration did not correlate with the remaining variables. It suggested that ad
type, gender, and campaign duration do not significantly influence the ads’ KPIs. Age showed a
negative correlation with reach and impression, implying that older age groups were less engaged with

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

93

ads. It was consistent with the finding that age showed a strong positive correlation with CPM, as lower
engagement in older age groups was associated with higher CPM. The analysis also suggested that age
does not have a noticeable influence on campaign duration, spending, or link clicks.

A significant positive correlation existed between the amount spent and several performance metrics,
including reach, impressions, and link clicks. The ad type variable showed weak correlations with other
metrics, suggesting that the choice between video and image ads does not strongly affect KPIs. The
most significant correlation was the negative relationship with CPM (-0.22), suggesting that certain ad
formats slightly influenced cost per thousand impressions. However, its correlations with reach (0.14)
and impressions (0.09) were weak, showing that ad format does not significantly determine visibility.
The weak correlation with the objective ( -0.09) indicated that cam paign objectives were not strongly
influenced by the type of ad used.

The objective variable has moderate negative correlations with reach ( -0.28) and impressions (-0.29),
suggesting that different campaign objectives affected audience visibility. For exa mple, objectives
focused on conversions might not generate as many impressions as awareness -based campaigns. A
weak positive correlation with CPM (0.22) indicated that objectives had a slight influence on advertising
costs, but the overall relationship rem ained minor. The interpretation of this variable should be
approached with caution, as the analysis does not disaggregate the eight specific objective categories.
As a result, these correlations may obscure important differences between campaign goals.

Figure 8

Features Heatmap

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

94

Reach showed a strong positive correlation with impressions, spend , and link clicks. This result was
intuitive because as reach grew, impressions also tended to increase, leading to higher spend and more
link clicks. Logically, higher reach led to lower CPM, consistent with the analysis’s finding that large-
scale campaigns were cost-efficient. In this context, reach does not affect CPC. Impressions and reach
also had strong positive correlations with amount spent and link clicks, and a negative correlation with
CPM.

Amount spent (IDR) is a significant driver of link clicks, implying that larger ad investments translate
into higher visibility and user interactions. However, the increased spending does not significantly raise
CPC, indicating budget efficiency. Link clicks showed no correlation with CPC; however, there was a
negative correlation with CPM, suggesting cost-efficient ads. CPC also showed the strongest correlation
with CPM (0.41), indicating that campaigns with higher CPCs tended to have higher CPM s. Feature
importance was used to identify the most impactful factors in decision -making by quantifying each
input variable’s contribution to  a model’s predictions. Figure 9 shows the Feature Importance of the
main variables used.

Figure 9

Feature Importance

The amount spent was identified as the most influential factor with a score of 0.47, which was
significantly greater than the other features. It strongly demonstrated that budget drove ad performance,
outlining the impact of increased spending on metrics such as reach and impressions. Age is another
important feature that supports demographic targeting and strongly impacts ad effectivenes s. It is
consistent with findings that different age groups responded differently to image and video ads, as well
as to  engagement metrics. Objective and campaign duration showed moderate feature importance ,
implying that the specific goals of a campaign , including its duration, influenced ad outcomes.
Campaign objective s prioriti sed conversions or engagement to influence performance results .
Meanwhile, longer campaign durations improve d reach and link clicks, providing ads with adequate
time to be seen and reviewed. Ad type and gender have relatively low feature importance scores.
Considering that ad type and gender had some impact on ad performance, they  were not as critical as
budget, age, or campaign characteristics. Gender had the least importance, indicating that gender-based
targeting did not signifi cantly impact the dataset ’s performance. Additionally, these results laid the
groundwork for further analysis using ML models to identify  complex patterns and interactions in the
data.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

95

ML Model Performance Comparison

The study applied three ML models, namely Linear Regression, Decision Tree, and Random Forest, to
predict ad effectiveness across various KPIs. The predictive accuracy of the models was evaluated by
calculating MSE, MAE, R², and RMSE for each KPI. Table 5 presents the calculated MSE, MAE, R²,
and RMSE for reach, impressions, link clicks, CPC, and CPM across  the three models considered in
this work.

Table 5

ML Evaluation Models

Metric Model MSE MAE R2 RMSE
Reach
Linear Regression 0.00020 0.010 0.50 0.01
Random Forest 0.00008 0.005 0.80 0.01
Decision Tree 0.00014 0.006 0.65 0.01
Impression
Linear Regression 0.00060 0.018 0.55 0.02
Random Forest 0.00020 0.007 0.85 0.01
Decision Tree 0.00032 0.008 0.76 0.02
Link clicks
Linear Regression 0.00007 0.006 0.59 0.01
Random Forest 0.00004 0.003 0.78 0.01
Decision Tree 0.00007 0.004 0.61 0.01
CPC
Linear Regression 0.00003 0.004 0.03 0.01
Random Forest 0.00002 0.003 0.41 0.00
Decision Tree 0.00003 0.003 0.08 0.01
CPM
Linear Regression 0.00035 0.014 0.37 0.02
Random Forest 0.00015 0.007 0.73 0.01
Decision Tree 0.00023 0.008 0.59 0.02

Random Forest outperformed both Linear Regression and Decision Tree across all KPIs. For example,
on reach, Random Forest improved R² by 30 percentage points over Linear Regression (0.80 vs 0.50),
reducing MAE by half (0.005 vs 0.010). On the impressions dataset, it achieved an R² of 0.85, compared
to 0.55  for Linear Regression, representing a 54% relative improvement. The results described the
benefits of an ensemble -based architecture for c apturing complex, non -linear relationships, enabling
the model to achieve consistently high accuracy and robust generalisation.

Interpretive Analysis using SHAP

The SHAP values for the Random Forest model were calculated to show how features affe cted ad
performance. These values enabled the identification of both the direction and magnitude of influence
for each feature, offering a detailed prediction of ad effectiveness across KPIs. Although the objective
was an influential feature in certain SHAP plots, this analysis failed to disaggregate the eight specific
objective categories. The observed SHAP effects were interpreted with caution , and future studies
would benefit from a more granular exploration of how distinct campaign goals influence ad
performance metrics, such as reach.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

96

Figure 10 shows the SHAP distribution, which describes how different features impact the model ’s
prediction of  reach. In addition, the amount spent was the most impactful predictor of  reach. The
distribution of SHAP values was skewed toward the positive side, indicating that the model predicted
that reach increased with spending , as shown by the red dots. Age had a significant impact on reach,
with the distribution of SHAP values centred around zero and showing  a distinct pattern. Younger
demographics, represented by blue dots, were clustered toward positive values, while older
demographics, represented by red dots, tended toward  negative values. It suggested that targeting
younger demographics increased predicted reach, and the older age groups were associated with lower
predicted reach. The scattered distribution of SHAP values implie d that age did not consistently push
the prediction towards a preferred direction. Other factors, such as ad type or campaign objective, also
influenced reach.

The objective feature exhibited mixed SHAP values clustered around zero, suggesting that its influence
on reach was highly context-dependent. This pattern reflected the fact that some campaign objectives
were inherently aligned with reach-maximising strategies, while others prioritised alternative outcomes,
such as conversions or engagement. Ad type, encoded as image and video ads, was associated with 0
and 1, respectively. The distribution of SHAP values for ad type was highly skewed toward the positive
side, with Video ads dominating and represented by red dots. It implied that ad type was an effective
predictor of reach, with the model suggesting that the presence of Video ads increased the likelihood of
higher reach. Campaign Duration exhibit ed a balanced distribution of SHAP values around zero ,
implying that duration did not consistently drive reach. However, this variable was influenced alongside
other factors, such as budget or target age group. Gender had minimal influence on reach, with SHAP
values clustered near zero, suggesting it was not a significant predictor in this dataset.

Figure 10

SHAP Distribution for Reach

Figure 11 shows the distribution of SHAP values for impressions, alongside several similarities a nd
certain significant differences in  reach observed in Figure 10. The amount spent remained the most
impactful feature, with its  impact on Impressions being more pronounced. In addition, SHAP values
reached approximately 0.08, compared to 0.04 for reach. It exhibited a strong relationship between
budget allocation and impressions. Regarding reach, age showed a variable impact, scattered and
centred around zero, with younger audiences associated with positive SHAP values. This variability
suggested that age was not the sole predictor of Impressions. It is context -dependent and potentially

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

97

interacts with other features, such as ad type or objective. The role of ad type was consistent with the
analysis shown in Figure 10. Moreover, video ads correlated positively with impressions. Gender and
campaign duration had minimal influence on impressions, with SHAP values clustered around zero. It
showed that the variables were not significant predictors of impressions.

A significant difference between the charts centred on  the impact of the objective was that the
impressions chart showed greater variability . It suggested that campaign objectives play ed a slightly
greater role in determining impressions than in determining  reach. The overall SHAP value range is
wider for impressions, reflecting more substantial or variable feature contributions in the impressions
model. Given that both charts showed similar trends, the impressions model indicated that spending had
a stronger influence on campaign objectives than reach did.

Figure 11

SHAP Distribution for Impressions

The distribution of SHAP values for link clicks is shown in Figure 12, and the predictions were mainly
driven by the amount spent, indicating that budget was the key to engagement. Age had a weaker, less
consistent impact, while campaign duration and gender had virtually no influence, as indicated by near-
zero SHAP values. Ad type’s effect was negligible for link clicks, suggesting that content format could
not reliably predict click behaviour.

Figure 12

SHAP Distribution for Link Clicks

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

98

The SHAP plot for CPC is shown in Figure 13, and the maximum value was less than the previous values
within the range of -0.01 to 0.01. Given the preferred directions for some features, such as amount spent and
campaign duration, the overall SHAP scale was extremely narrow, making it difficult to draw meaningful
inferences. The model failed to  detect certain signals in the prediction with minimal impact, including
bearing the weight for drawing meaningful predictions. It was inferred that CPC was insensitive to the
features considered in the present study.

Figure 13

SHAP Distribution for CPC

The final metric evaluated was CPM, with the SHAP distribution shown in Figure 14. Age was the most
influential factor, with older demographics (represented by red dots) associated with higher CPM. It showed
that campaigns targeting older demographics were predicted to have higher CPM. Based on this perspective,
objective and campaign duration had significant impacts on CPM. Positive SHAP values were realised for
certain campaign objectives, namely engagement, leads, and sales, which increased CPM, due to the need
for more targeted or intensive ad placements. Campaign duration exhibited a varied impact, suggesting that
both brief and lengthy campaigns influenced CPM, possibly reflecting different pricing models.  Amount
Spent had a relatively low influence on CPM compared to other KPIs. It showed that increasing the budget
did not significantly affect CPM outcomes. Gender and ad type were the least influential features, with SHAP
values approaching zero. Although video ads represented by the red dots had slightly lower CPM, the overall
impact remained minimal. CPM identified demographic -driven cost sensitivity and targeted older age
groups, resulting in a significant increase. Compared to other KPIs, where budget allocation or campaign
objectives played leading roles, CPM was strongly influenced by audience age. It showed that cost efficiency
for impressions varied considerably by demographic factors.

Figure 14

SHAP Distribution for CPM

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

99

Comparison of Statistical, ML, and SHAP Findings

This section discusses insights from descriptive statistics, Spearman ’s correlation, Random Forest
results, and SHAP interpretations  to provide a comprehensive perspective on ad effectiveness.
Statistical analysis showed clear performance differences between ad type and demographic groups.
Video ads consistently exhibited greater reach and impressions, particularly among younger audiences
aged 13-24. However, image ads excelled at generating link clicks across both younger (13 -17) and
older (55+) demographics, underscoring their  effectiveness in engagemen t-driven campaigns. These
findings outlined the importance of selecting an ad type based on specific campaign objectives and
target demographics.

Based on this perspective, Random Forest  was perceived as having the best predictive power .
Furthermore, the amount spent was identified as the dominant predictor of ad performance across all
KPIs. It outlined budget allocation as the main driver for campaign success. Given that age and ad type
were crucial predictors, they had little  influence compared to spending. The models described trade-
offs among cost metrics, such as CPM and CPC, and ad effectiveness, underscoring the need for careful
resource allocation to optimise outcomes. SHAP analysis provided detailed insights into how different
features influence d ad performance. For example,  budget is a consistent positive driver of reach,
impressions, and link clicks, with its impact on CPM and CPC less pronounced. Age showed varying
levels of influence, with younger demographics  associated with increased reach and impressions. Ad
type also exhibited context-dependent effects. It was observed that video ads tended to boost visibility
metrics, namely reach and impressions.

Furthermore, image ads were more cost-efficient, contributing to lower CPC. Campaign object ives
emerged as critical drivers of CPC, with engagement - and conversion-focused goals associated with
higher CPC. These findings described the strategic importance of supporting campaign objectives with
performance priorities.  The integration of these met hods showed a comprehensive picture of ad
performance. Moreover, statistical analysis explored relationships and patterns among variables, with
Random Forest providing predictive accuracy of the fundamental model, and SHAP offering insights
into how the diverse features influenced model predictions. The amount spent, age, and ad type were
identified as significant influential factors for ad performance across all analyses . Meanwhile, the
delicate interplay between budget, demographics, and campaign ob jectives drove cost -efficiency
dynamics. The analysis showed that data-driven decision-making balanced cost efficiency, visibility,
and engagement to achieve campaign success. A summary of performance metrics by ad type and age
groups is shown in Table 6.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

100

Table 6

Performance Summary of Ad Type across Age Groups and Key Metrics

Ad
Type Audience Visibility (Reach & Impressions) Engagement (Link Clicks) CPM CPC
Video
Ads
Younger
(13–24)
High – Strong
visibility due to
multimedia
engagement
Moderate – Less
effective for clicks
than image ads
Low – More cost-
efficient for
reaching a broad
audience
High – Less
efficient for
engagement-driven
campaigns
Adult (25–
34)
High – Maintains
strong reach
Moderate –
Performs well but
behind image ads
for clicks
Low – Cost-
effective for broad
visibility
High – Higher cost
per click makes
engagement
campaigns pricier
Midlife
(35–54)
High – Strong
brand awareness
potential
High – Effective in
engagement for this
age group
Low – Keeps
impression costs
lower while
maintaining reach
Moderate –
Balanced cost-
efficiency and
engagement
Older
(55+)
Moderate –
Lower reach than
younger groups
Low – Limited
engagement for
clicks
Low – Remains
cost-efficient for
visibility
campaigns
Moderate –
Engagement costs
remain manageable
but not optimal
Image
Ads
Younger
(13–24)
Low – Less reach
than video ads
High – Best for
engagement (clicks,
reactions)
High – Less cost-
efficient for
visibility
campaigns
Low – Cost-
effective for
engagement-
focused objectives
Adult (25–
34)
Moderate –
Performs
adequately but
behind video ads
High – Best for
direct engagement
actions
High – Higher
cost per thousand
impressions
compared to video
ads
Low – Lower cost
per click makes it
ideal for
engagement-
focused goals
Midlife
(35–54)
Moderate –
Visibility remains
stable but not as
strong as video
ads
Moderate –
Performs well but
video ads generate
more engagement
in this group
High – Costs
more for
impressions,
making it less
ideal for
awareness
campaigns
Low – Cost-
effective for
driving direct
engagement
Older
(55+)
Low – Least
effective for
visibility
Low – Struggles to
drive engagement
in this demographic
High – Expensive
for impressions
with limited reach
Low – Remains
cost-effective for
engagement but
struggles with
visibility

Discussions

This study confirmed that video ads drove higher reach and impressions, specifically among audiences
aged 13–24. The findings support ed previous studies, which stated video content was more engaging
for younger demographics due to its dynamic nature and storytelling capabilities (Grewal et al., 2021;
Tavares et al., 2023). It was further supported by Tavares et al. (2023), who analysed the effectiveness

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

101

of video ads in broad engagement campaigns. The Attention, Interest, Desire, Action (AIDA) model
was used to show that video ads played a significant role in the attention and interest stages due to their
visual appeal and narrative strength. However, this study does not directly measure the action phase;
the high engagement suggests that video content triggered desire, which eventually drove  action over
time. Image ads were more effective at motivating direct engagement, particularly among younger (13–
17) and older (55+) users. The simplicity and low CPC made it a cost-effective option for action-driven
campaigns, supporting prior findings (Stewart et al., 2023; Northcott et al., 2021). These were also
consistent with the study by Xie et al. (2024), which focused on the role of ad -context congruence in
enhancing engagement, specifically for image-based formats. In the AIDA framework, image ads were
more effective in the desire and action stages, prompting users to click, engage, or convert.

SHAP analysis and feature importance identified budget allocation as the most influential factor in ad
performance. Spending also directly impact ed visibility and engagement metrics, reinforcing its
strategic role in campaign success. Trade-offs detected between CPM and CPC must be managed
carefully. Considering that video ads offered lower CPMs and greater visibility, higher CPCs reduced
efficiency for conversion -focused goals. Image ads provide d a more cost -efficient solution for
engagement-driven strategies (Tavares et al., 2023; Stewart et al., 2023 ). These findings were in line
with the studies by Félegyházi (2024) and Mihajlovic et al. (2024), which stated that video ads increased
reach, while static image ads delivered better ROI during engagement. ML models, particularly Random
Forest, played a significant role in identifying these patterns. Its ability to handle complex , non-linear
relationships enabled accurate predictions for reach, impressions, and link clicks. SHAP analysis further
enhanced these insights by showing how individual features influenced outcomes. For example, higher
ad spending correlated with stronger reach and impressions for video ads targeted at younger users. Age
also played a mixed role ; video ads resonated more with younger users, while older demographics
preferred image formats. These insights were consistent with studies by Lakshmanarao et al. (2021) and
Patil et al. (2022), which described the value of ML in optimising ad performance.

This data-driven method helped marketers support ad formats with both campaign goals and audience
preferences. In the AIDA framework, it enabled the design of video and image ads to different stages
of the customer journey , capturing attention, building interest, triggering desire, and driving action.
Video ads were suited for visibility -focused objectives, while image ads exce lled in engagement -
focused campaigns. The findings were in line with  those of Xie et al. (2024), which highligh ted the
importance of format -goal support. SHAP also contribute d to the growing role of explainable AI in
advertising. It enabled campaign planners to make informed decisions  by translating predictions into
actionable insights. It was supported by Zhao and Harinen (2019) and Al -Khafaji and Karan (2024),
who also described SHAP’s strategic utility. The studies by Chavda and Patel (2024) and Ji et al. (2024)
showed that ML enhanced ROI by enabling more precise and optimised targeting.

The contributions of this study were threefold: first, it provide d large-scale confirmation in a non -
Western, platform-native context. The analysis of 4,526 Meta campaigns from Indonesia (2021–2024)
validated established format patterns. Video ads outperformed in terms of visibility and CPM, while
image ads were more cost -efficient ( i.e., CPC). The extension beyond small -scale A/B tests and
Western-focused samples strengthen ed the generalisability of prior findings. Second, the study went
beyond reporting outcomes to explain relevant occurrences . The integrated ML and SHAP analyses
showed that budget allocation (amount spent) was the dominant driver of visibility. Additionally, age
demographics and campaign objectives strongly influenced CPM and CPC, respectively. This multi -
KPI, explainable modelling method clarified the mechanisms behind format differences, contributing
both methodological and substantive insights to the literature. Third, the study translated these insights

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

102

into actionable guidance , reporting the optimal nature of  video ads in terms of visibility and CPM .
Meanwhile, image ads were preferable for engagement and cost -efficient clicks—particularly among
younger (13–17) and older (55+) audiences.

From a managerial perspective, these findings outlined the need to align creative formats with campaign
objectives and audience segmentation. Advertisers should avoid reliance on average effects and instead
match format choice to specific goals. Videos were used for awareness and broader reach, while images
were adopted for engagement and cost-efficient clicks. Budget allocation remained the strongest driver
of performance, with its influence differing across metrics. In practice, marketers treated budget as the
lever for scaling visibility, allowing demographic and objective considerations guide creative decisions
when optimising CPC. These designed strategies ensured more efficient resource allocation, improved
ROI, and shifted campaign planning away from one -size-fits-all assumptions toward evidence-based,
goal-conditioned choices.

This study offer ed data-driven insights into the effectiveness of image and video ads, but several
limitations must be acknowledged to contextuali se the findings and guide future analyses. First, the
analysis was limited to data from Meta Ads Manager. The extensive dataset reflect ed only an
advertising platform. Since audience behaviour and algorithmic mechanics differ ed across platforms
such as Google Ads, TikTok, or Snapchat, future studies should include multi-platform data to improve
generalisability. Second, the study did not account for content quality variables , such as creativity,
message clarity, or design appeal. These qualitative aspects affect ed ad performance, which was not
measured. Future studies will integrate methods, such as sentiment analysis and computer vision, to
assess how creative elements influence outcomes.

Third, temporal factors, including seasonal patterns, holidays, and campaign timing, were not examined.
In this context, the factors significantly affected user behaviour and ad engagement. Incorporating time-
based variables allow ed future studies to identify trends associated with timing. Fourth, the dataset
excluded campaigns with zero values for key metrics, introducing  selection bias. Excluding
underperforming campaigns led the analysis to overrepresent successful ad strategies. Furthermore,
including the full spectrum of campaign outcomes provide d a more balanced view. Addressing these
limitations in future studies enhanced the robustness and applicability of findings in digital advertising.

CONCLUSION

In conclusion, t his study provided a comprehensive analysis of how video and image ads performed
across key metrics, including reach, impressions, link clicks, CPC, and CPM. The findings showed that
video ads were more effective at increasing visibility, particularly among younger audiences, due to
their dynamic,  attention-grabbing nature. Image ads were more cost -efficient for engagement,
especially with older demographics, making them effective for interaction-focused campaigns under
budget constraints. SHAP analysis and feature importance modelling proved that ad performance was
mainly driven by budget allocation, with age and campaign duration influencing outcomes. These
results outlined the value of demographic targeting when selecting ad formats, as diverse age groups
responded differently to content type. For example, younger users preferred video ads, while older
individuals responded to simpler, static image content.

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

103

From a strategic perspective, align ing ad formats with campaign goals and audience profiles
significantly improved cost efficiency and engagement outcomes. Video ads offered broader exposure
at competitive CPM  during visibility-driven campaigns. Image ads tend ed to achieve lower CPC for
action-oriented goals . SHAP analysis show ed minimal feature influence on CPC, suggesting that
unmeasured variables, such as content quality or audience context, shape i t. These findings were
consistent with the AIDA framework. Video ads strongly captured Attention and built interest, while
image ads effectively generated desire, motivating action. The insights helped marketers design diverse
advertising strategies to achieve optimal results. Future studies should address additional factors that
shape ad effectiveness to strengthen the insights further. Content quality, including creativity, emotional
tone, and visual design, was assessed using  sentiment analysis or computer vision methods. Seasonal
and temporal trends also prompted an investigation using time-series data to capture variations in user
behaviour over time. Contextual variables, namely device type, browsing environment, or time, showed
further nuances in engagement patterns.

Evolving ad formats such as short-form videos, interactive content, and augmented reality offered new
opportunities for brand storytelling. Moreover, psychographic segmentation account ed for audience
attitudes, values, and motivations, provid ing deeper insights for personal ised ad experiences.
Addressing these areas  enabled future studies to expand on the current findings and  supported the
development of more adaptive, targeted, and high-performing digital advertising strategies.

ACKNOWLEDGMENT

This study received no specific grant from any funding agency in the public, commercial, or not -for-
profit sectors.

REFERENCES

Abu Bakar  et al.  (2025). AI -driven influencer and market analysis: A social network approach to
measure e -commerce relationships.  Journal of Information and Communication
Technology, 24(3), 1–21. https://doi.org/10.32890/jict2025. 24.3.1
Al-Khafaji, A., & Karan, O. (2024). Explainable AI for predicting user behaviour in digital advertising.
In Lecture Notes in Networks and Systems , (pp. 520–531). Springer. https://doi.org/10.1007/
978-3-031-56728-5_43
Arboleda-Florez, M., & Castro -Zuluaga, C. (2023). Interpreting direct sales’ demand forecasts using
SHAP values. Production, 33. https://doi.org/10.1590/0103-6513.20220035
Asdemir, K., Kumar, N., & Jacob, V. S. (2012). Pricing models for online advertising: CPM vs. CPC.
Information Systems Research, 23(3), 804–822. https://doi.org/10.1287/isre.1110.0391
Balcan, M., & Sharma, D. (2024). Learning accurate and interpretable decision trees. Proceedings of
the Fortieth Conference on Uncertainty in Artificial Intelligence, in Proceedings of Machine
Learning Research, 244, 288–307. https://proceedings.mlr.press/v244/balcan24a.html
Booth, D. (2019). Marketing analytics in the age of machine learning. Applied Marketing Analytics,
4(3), 214. https://doi.org/10.69554/krmg2945
Braun, M., de Langhe, B., Puntoni, S., & Schwartz, E. M. (2023). Leveraging digital advertising
platforms for consumer research. SSRN Electronic Journal.  https://doi.org/10.2139/ssrn.
4589567

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

104

Chavda, V., & Patel, S. (2024). Review on boosting online advertising ROI: Using machine learning.
International Journal of Advanced Networking and Applications, 15 (4), 69–73. https://www.
researchgate.net/publication/378190219_Review_on_Boosting_Online_Advertising_ROI_Usi
ng_Machine_Learning
Chicco, D., Warrens, M. J., & Jurman, G. (2021). The coefficient of determination R -squared is more
informative than SMAPE, MAE, MAPE, MSE and RMSE in r egression-analysis evaluation.
PeerJ Computer Science, 7(5), e623. https://doi.org/10.7717/peerj-cs.623
Chumwatana, T. (2018). Comment analysis for product and service satisfaction from Thai cu stomers’
review in social network. Journal of Information and Communication Technology, 17(2), 271–
289. https://doi.org/10.32890/jict2018.17.2.8254
Cunha, B. M., & Barbosa, S. D. J. (2024). Evaluating the effectiveness of visual representations of
SHAP values toward explainable artificial intelligence . Proceedings of the XXIII Brazilian
Symposium on Human Factors in Computing Systems (pp. 1 -11). ACM. https://doi.org/10.
1145/3702038.3702093
Das, L. B., George, S. N., & Aprem, A. (2023). Artificial intelligence and machine learning: Theory
and practice. IK International Pvt. Limited. https://books.google.co.id/books?id=K9oFEQAA
QBAJ
de Carvalho, M. S., & da Silva, G. L. (2021). Inside the black box: Using explainable AI to impr ove
evidence-based policies. 2021 IEEE 23rd Conference on Business Informatics (CBI)  (pp. 57–
64). IEEE. https://doi.org/10.1109/CBI52690.2021.10055
Farahat, A., & Shanahan, J. (2013). Econometric analysis and digital marketing.  Proceedings of the
Sixth ACM International Conference on Web Search and Data Mining (WSDM ’13).
Association for Computing Machinery. https://doi.org/10.1145/2433396.2433502
Félegyházi, Z. (2024). Facebook hirdetések vizuális hatékonyságának növelése és helyzete az online
hirdetések piacán. Acta Carolus Robertus, 14(1), 65–77. https://doi.org/10.33032/acr.4870
Grewal, R., Gupta, S., & Hamilton, R. (2021). Marketing insights from multimedia data: Text, image,
audio, and video. Journal of Marketing Research, 58 (6), 1025–1033. https://doi.org/10.1177/
00222437211054601
Hamilton, R. I., & Papadopoulos, P. N. (2023). Using SHAP values and machine learning to understand
trends in the transient -stability limit. IEEE Transactions on Power Systems,  Advance online
publication. https://doi.org/10.1109/TPWRS.2023.3248941
Hancock, J. T., & Khoshgoftaar, T. M. (2020). Survey on categorical data for neural networks. Journal
of Big Data, 7(1). https://doi.org/10.1186/s40537-020-00305-w
Huang, S., Aral, S., Hu, Y. J., & Brynjolfsson, E. (2020). Social advertising effectiveness across
products: A large-scale field experiment. Marketing Science, 39(6), 1142–1165. https://doi.org/
10.1287/mksc.2020.1240
Ismail, N., & Yusof, U. K. . (2022). Recent trends of machine learning predictions using open data: A
systematic review. Journal of Information and Communication Technology , 21(3), 337–381.
https://doi.org/10.32890/jict2022.21.3.3
Jha, A., Jain, H., Sharma, P., Sharma, Y., & Tiwari, K. (2024). Optimising real-time bidding strategies:
An experimental analysis of reinforcement -learning and machine -learning techniques.
Procedia Computer Science, 235, 2017–2026. https://doi.org/10.1016/j.procs.2024.04.191
Ji, H., Xu, X., Su, G., Qang, J., & Wang, Y. (2024). Utilising  machine learning for precise audience
targeting in data science and targeted advertising. Academic Journal of Science and
Technology, 9(2), 215–220. https://doi.org/10.54097/r7gek671
Johnson, J. M., & Khoshgoftaar, T. M. (2019). Survey on deep learning with class imbalance. Journal
of Big Data, 6(1). https://doi.org/10.1186/s40537-019-0192-5

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

105

Kedar, M. M. (2024). Exploring the effe ctiveness of SHAP over other explainable -AI methods.
International Journal of Scientific Research in Engineering and Management, 8 (6), 1 –5.
https://doi.org/10.55041/ijsrem35556
Kedi, W. E., Eji muda, C., Idemudia, C., & Ijomah, T. I. (2024). Machine-learning software for
optimising SME social-media marketing campaigns. Computer Science & IT Research Journal,
5(7), 1634–1647. https://doi.org/10.51594/csitrj.v5i7.1349
Kosaraju, N., Sankepally, S. R., & Rao, K. M. (2023). Categorical data: Need, encoding, selection of
encoding method and its emergence in machine-learning models—A practical review study on
heart-disease prediction dataset using Pearson correlation. In Lecture Notes in Networks and
Systems, 551 (pp. 369–382). Springer. https://doi.org/10.1007/978-981-19-6631-6_26
Kovalerchuk, B., Dunn, A., Worland, A., & Wagle, S. (2024). Interactive decision tree creation and
enhancement with complete visualisati on for explainable modeling. In Artificial Intelligence
and Visualization: Advancing Visual Knowledge Discovery  (Studies in Computa tional
Intelligence, Vol. 1126, pp. 3–40). Springer. https://doi.org/10.1007/978-3-031-46549-9_1
Lakshmanarao, A., Ushanag, S., & Leela, B. S. (2021). Ad prediction using click -through rate and
machine learning with reinforcement learning.  2021 Fourth International Conference on
Electrical, Computer and Communication Technologies (ICECCT). https://ieeexplore.ieee.org/
document/9616653
Liu, Z., Yao, Y., Liu, C., & Sun, Z. (2021). Handling inter-class and intra-class imbalance in class -
imbalanced learning. arXiv. https://doi.org/10.48550/arxiv.2111.12791
Lundberg, S., & Lee, S.-I. (2017). A unified approach to interpreting m odel predictions. Advances in
Neural Information Processing Systems  (Vol. 30, pp. 4765 –4774). Curran Associates.
https://proceedings.neurips.cc/paper_files/paper/2017/file/8a20a8621978632d76c43dfd28b67
767-Paper.pdf
Lusito, S., Pugnana, A., & Guidotti, R. (2023). Solving imbalanced learning with outlier detection and
features reduction. Machine Learning,  Advance onlin e publication. https://doi.org/10.1007/
s10994-023-06448-0
Mihajlović, A., Gajić, J., & Papić, T. (2024). Analysis of the cost -effectiveness of the university
Instagram marketing campaign using A/B testing . Sinteza 2024 Conference Proceedings  (pp.
266–273). https://doi.org/10.15308/sinteza-2024-266-273
mljourney. (2024, June 15). Importance of feature scaling in machine learning.  ML Journey.
https://mljourney.com/importance-of-feature-scaling-in-machine-learning/
Northcott, C., Herbert, J., Barrea, A., & Maher, C. (2021). Should Facebook advertisements promoting
a physical-activity smartphone app be image- or video-based, and should they promote benefits
of being active or the app attributes? Translational Behavioural Medicine, 11(12), 2136–2143.
https://doi.org/10.1093/tbm/ibab101
Nwaimo, C. S., Adegbola, A. E., & Adegbola, M. D. (2024). Data-driven strategies for enhancing user
engagement in digital platforms. International Journal of Management & Entrepreneurship
Research, 6(6), 1854–1868. https://doi.org/10.51594/ijmer.v6i6.1170
Osakwe, J., Shilongo, A., & Ziezo, M. M. (2023). Optimising customer segmentation in digital
marketing using predictive analytics: A review of literature. SSRN Electronic Journal. https://
doi.org/10.2139/ssrn.4662191
Patil, S., Raut, K., Palsodkar, P., Singh, T., Dubey, Y., & Umate, R. (2022). Click-prediction learning
for effective advertising . 2022 International Conference on Emerging Trends in Engineering
and Management Science (ICETEMS 2022).  IEEE. https://doi.org/10.1109/ICETEMS56252.
2022.10093291

 Journal of Information and Communication Technology, Vol. 25, Number 1 (January) 2026, pp: 79-106

106

Prihatiningsih, T., Panudju, R., & Prasetyo, I. J. (2024). Digital advertising trends and effectiveness in
the modern era: A systematic literature review. Golden Ratio of Marketing and Applied
Psychology of Business, 4(2). https://doi.org/10.52970/grmapb.v4i2.505
Prosekov, A. Y. (2020). Characteristics and key limitations of traditional methods for accounting
hunting animals and digital technologies for solving the existing pro blems (Review).
Agricultural Science Euro -North-East, 21 (4), 341 –354. https://doi.org/10.30766/2072-9081.
2020.21.4.341-354
Raufi, B., Finnegan, C., & Longo, L. (2024). A comparative analysis of SHAP, LIME, ANCHORS,
and DICE for interpreting a dense neural  network in  credit-card fraud detection . In
Communications in Computer and Information Science  (pp. 365 –383). Springer. https://
doi.org/10.1007/978-3-031-63803-9_20
Rodríguez-Pérez, R., & Bajorath, J. (2020). Interpretation of machine-learning models using Shapley
values: Application to compound potency and multi -target activity predictions. Journal of
Computer-Aided Molecular Design, 34 (10), 1013–1026. https://doi.org/10.1007/s10822-020-
00314-0
Santos, C. (2023). Towards an interpretable advertisement click prediction  [Unpublished master’s
thesis]. Universidade Católica Portuguesa.
scikit-learn. (2019). sklearn. pre-processing.MinMaxScaler—scikit-learn 0.22.1 documentation. Scikit-
learn. https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMax Scaler.html
Stewart, K., Dalakas, V., & Eells, D. (2023). If a picture is worth 1000 words, how much is a video
worth? The influ ence of ad format on ticket purchasers’ ad clicks. Journal of Promotion
Management, Advance online publication. https://doi.org/10.1080/10496491.2023.2279767
Tavares, D., Remondes, J., & Lima, A. M. (2023). Facebook ads interaction campaigns. In Advances in
Marketing, Customer Relationship Management, and E -Services (pp. 23 –51). IGI Global.
https://doi.org/10.4018/978-1-6684-9146-1.ch002
Xie, W., Dotsch, R., Bos, M., Bart, Y., Han, Z., & Liu, Y. (2024). Congruence affects story -ad
engagement on social media. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.4790627
Yang et al . (2019). AiAds: Automated and intelligent advertising sys tem for sponsored search.
Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery &
Data Mining (KDD ’19, pp. 1881–1890). ACM. https://doi.org/10.1145/3292500.3330782
Yang, Y., & Zhai , P. (2022). Click -through rate prediction in online advertising: A literature review.
Information Processing & Management, 59 (2), Article 102853. https://doi.org/10.1016/j.ipm.
2021.102853
Ye, H.-J., Chen, H.-Y., Zhan, D.-C., & Chao, W.-L. (2020). Identifying and compensating for feature
deviation in imbalanced deep learning. arXiv. https://doi.org/10.48550/arxiv.2001.01385
Yoon, S. (2022). Introduction to the special issue on the future of advertising. International Journal of
Advertising, 41(5), 823–826. https://doi.org/10.1080/02650487.2022.2074557
Zhao, Z., & Harinen, T. (2019). Uplift modeling for multiple treatm ents with cost optimisation . 2019
IEEE International Conference on Data Science and Advanced Analytics (DSAA)  (pp. 422-
431). IEEE. https://doi.org/10.1109/DSAA.2019.00057
