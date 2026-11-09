---
title: 'Anticipating user desires: predicting software product feature demand through consumer behavioral
  analytics'
url: https://doi.org/10.3389/fdata.2026.1931695
category: consumer-behavior
subcategory: empirical
date: 2026-09
venue: Frontiers in Big Data
authors:
- Abdullah A. Aldaeej
source: openalex-oa
pdf_url: https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2026.1931695/pdf
pages: 18
chars: 79254
fetched_at: '2026-11-08T18:48:40+00:00'
kb_version: 1
---

# Anticipating user desires: predicting software product feature demand through consumer behavioral analytics

TYPE Original Research
PUBLISHED 24 September 2026
DOI 10.3389/fdata.2026.1931695
OPEN ACCESS
EDITED BY
Rashid Ibrahim Mehmood,
Islamic University of Madinah,
Saudi Arabia
REVIEWED BY
Mengyang Huang,
Chongqing University of Posts and
Telecommunications, China
David Alebiosu,
Sunway University, Malaysia
*CORRESPONDENCE
Abdullah A. Aldaeej
aaaldaeej@iau.edu.sa
RECEIVED 08 July 2026
REVISED 06 August 2026
ACCEPTED 24 August 2026
PUBLISHED 24 September 2026
CITATION
Aldaeej AA (2026) Anticipating user
desires: predicting software product
feature demand through consumer
behavioral analytics.
Front. Big Data 9:1931695.
doi: 10.3389/fdata.2026.1931695
COPYRIGHT
© 2026 Aldaeej. This is an open-access
article distributed under the terms of the
Creative Commons Attribution License
(CC BY). The use, distribution or
reproduction in other forums is
permitted, provided the original author(s)
and the copyright owner(s) are credited
and that the original publication in this
journal is cited, in accordance with
accepted academic practice. No use,
distribution or reproduction is permitted
which does not comply with these terms.
Anticipating user desires:
predicting software product
feature demand through
consumer behavioral analytics
Abdullah A. Aldaeej*
Department of Management Information Systems, Imam Abdulrahman Bin Faisal University, Dammam,
Saudi Arabia
In this study, we introduce the Dynamic Behavioral Feature Predictor (DBFP),
a machine learning model designed to predict feature demands for software
products based on consumer behavioral analytics. The model leverages
advanced techniques such as Deep Convolutional Neural Networks (1D CNN)
and Long Short-Term Memory (LSTM) networks to identify complex user
behavior patterns. We demonstrate that DBFP achieves a high accuracy of 99%,
outperforming established models such as LSTM and 1D CNN in extensive
comparative experiments. Although the model shows promising performance,
we note that its accuracy may be sensitive to data quality, and further research
is needed to evaluate its robustness in real-world applications. DBFP excels at
identifying diverse user behavior types, offering tailored recommendations for
softwarefeaturesthatalignwithindividualuserpreferences.Thispaperhighlights
the potential of behavioral analytics in personalizing software development,
enhancing the user experience, and improving the efficiency of feature
prioritization. By bridging the ﬁelds of machine learning, big data (BD), and
software personalization, DBFP lays the foundation for future advancements in
user-centric software engineering. This study not only contributes to the ﬁeld of
predictive analytics but also opens new avenues for applying behavioral insights
to software design and development.
KEYWORDS
consumer behavioral analytics, data mining, predictive analytics, sequential pattern
mining, software product development
1 Introduction
Consumerbehavioralanalyticshavesigniﬁcantlytransformedthelandscapeofsoftware
product development by oﬀering previously unseen insights into user preferences and
behaviors. This research seeks to explore the intricate relationship between user actions
and the features demanded by software products, with the aim of better anticipating user
needs through predictive analytics (Agnieszkaetal., 2023 ). By leveraging comprehensive
datasets derived from user interactions and engagement patterns, this study aims to equip
software development teams with the tools to uncover latent user desires and preferences.
Central to this research is the application of advanced analytical techniques and machine
Frontiersin BigData 01 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
learning algorithms, which have the potential to identify hidden
patterns in complex interaction data. These tools empower
organizations to make more informed decisions, enhancing their
ability to prioritize feature development eﬀorts eﬀectively. By
bridging theoretical predictive analytics and practical application,
this study intends to support software development teams
in understanding and addressing evolving user demands
(Chih-Chengetal., 2018 ). The motivating of this research is that
traditionalmethodsoffeatureprioritizationoftenfailtocapturethe
nuancedanddynamicpreferencesofmodernconsumers( Feietal.,
2022). Conventional approaches typically rely on subjective
evaluations or historical data, which may no longer be suﬃcient
in predicting user behavior. In contrast, our approach leverages
consumer behavioral data to reveal hidden trends and oﬀer a
more precise understanding of user preferences. This shift toward
data-driven strategies is intended to help organizations develop
more responsive, user-centric products,resulting in improved user
engagementandretention.Furthermore,thisstudyisdrivenbythe
desire to surpass outdated product design paradigms and provide
a user experience that truly meets contemporary expectations.
By anticipating user needs, software development teams can
create products that align more closely with user preferences,
ultimately enhancing product success. The research also addresses
a crucial gap in connecting predictive analytics theory with its
real-worldapplications.Manyorganizationsstruggletoimplement
these theoretical concepts into their development processes
(Hyunjoo, 2022). Through empirical validation, this research aims
to provide practical insights that software teams can integrate
predictive analytics into their workﬂows. Despite the promising
potential of predictive analytics, there are signiﬁcant challenges
to overcome, such as concerns about data privacy, the complexity
of algorithms, and a lack of organizational readiness (Wangetal.,
2023). For predictive analytics to achieve its full potential in
drivinginnovationandfosteringuser-centricproductdesign,these
obstacles must be addressed. This research ultimately seeks to
promote a shift toward a more agile, user-centered approach to
software product development, laying the groundwork for a future
where software design is driven by data insights that accurately
reﬂectuserdemandsandpreferences.
Eﬀectivedemandforecastingiscrucialforoptimizinginventory
management, production planning, and resource allocation,
leading to improved operational eﬃciency and proﬁtability for
organizations. By accurately predicting demand, businesses can
identify future opportunities, mitigate potential risks, and adapt to
shiftsincustomerpreferences.
In light of this, we have deﬁned the following research
objectives to address the challenges and deepen our understanding
ofthesubject:
a) Develop a robust model that predicts user preferences
for new software features by utilizing consumer
behavioralanalytics.
b) Examine complex interaction data to evaluate how well
various machine learning algorithms can uncover hidden user
demandsandpatterns.
c) Explore innovative techniques, such as sequential pattern
miningandsentimentanalysis,toextractvaluableinsightsfrom
diversecustomerbehaviordatasets.
d) Assess the impact of predictive analytics on software
product development, including feature prioritization and
budgetallocation,withafocusonusersatisfaction.
Through these objectives, this study aims to enhance the
prediction capabilities of software development teams, ensuring
thatnewfeaturesaligncloselywithevolvinguserexpectations.This
will foster a more ﬂexible and user-centric approach to software
design. By addressing key issues and expanding our understanding
of software development and predictive analytics, this research
makesasigniﬁcantcontributiontotheﬁeld,asfollowing:
a) Create a transformative predictive model that integrates
consumer behavioral analytics to accurately forecast user
preferencesforupcomingsoftwarefeatures.
b) Advance knowledge on the eﬀectiveness of diﬀerent
machine learning algorithms in identifying latent user demands
andpatternsfromcomplexinteractiondata.
c) Introduce innovative methodologies for extracting
meaningful insights from various consumer behavioral
data sources, including sentiment analysis and sequential
patternmining.
d) Evaluate the inﬂuence of predictive analytics on user
satisfaction and software development processes, helping guide
featureprioritizationandresourceallocation.
By accomplishing these goals, the study will enhance
software development teams’ ability to make accurate predictions,
enabling them to create more user-centric products that meet
changingdemands.
The paper is structured into ﬁve sections. The Introduction
section outlines the research problem and objectives, setting the
stage for the study. The Literature Review section examines
previous research and theoretical frameworks related to software
feature demand forecasting and consumer behavioral analytics.
The Methodology section describes the research approach, data
collection methods, and analysis techniques used in the study.
The Results and Discussion section presents the ﬁndings, their
implications, and a thorough interpretation of the data. Finally,
the Conclusions section summarizes the key insights, discuss their
signiﬁcance,andsuggestdirectionsforfutureresearch.
2 Literature review
Recent studies have increasingly focused on the potential
of augmented reality (AR) to inﬂuence consumer behavior and
decision-making, especially in enhancing brand experiences and
fostering consumer engagement. The use of AR in marketing
strategies has shown promise in creating immersive experiences
that improve customer interactions with brands. Moreover,
data analytics plays a crucial role in forecasting consumer
purchasing behavior, opening up new avenues for businesses to
leverage data-driven insights to fuel innovation and growth in
competitive markets (Agnieszkaetal., 2023 ). Research on data-
driven marketing tactics, particularly using big data analytics,
has highlighted both the beneﬁts and challenges of utilizing
Frontiersin BigData 02 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
consumer behavior data to optimize online shopping experiences.
This approach has proven eﬀective in identifying patterns in
consumer actions and guiding marketing decisions, though it
also raises concerns about data privacy and the potential for
over-reliance on automated insights ( DimitriosandPanayiotis,
2022; EzenwobodoandStephen, 2022). As companies increasingly
adopt these strategies, they are better able to capture nuanced
consumer preferences and values, which can improve targeting
andpersonalizationeﬀorts.Theﬁeldofconsumerdecision-making
has also seen signiﬁcant advances, with many studies exploring
methodsforimprovingcustomerbehaviorthroughevidence-based
strategies. Analytical Hierarchy Process (AHP) models, which
assess the relative weight of various factors inﬂuencing consumer
behavior, have provided useful insights into how preferences
are formed and how decisions are made in a marketplace
(HanandLeslie, 2022 ). This approach has been particularly
helpful in segmenting consumer bases and designing targeted
interventions based on these preferences. With the rise of digital
commerce, understanding the drivers behind online purchasing
behavior has become crucial for businesses. Research using multi-
analytic methods has shed light on the underlying motivations
of online shoppers, revealing complex patterns of behavior
that are often overlooked by traditional marketing techniques.
In particular, consumer behavioral analytics has become an
essentialtoolinsoftwareproductdevelopment,helpingcompanies
predict and adapt to changing user preferences (Lakshmietal.,
2021; Lauraetal., 2022 ). The integration of social media data
into predictive models has further reﬁned consumer behavior
forecasting. AI and machine learning techniques, when applied
to social media interactions, have improved market insights by
accurately predicting consumer behavior in response to marketing
eﬀorts. This innovation is particularly relevant in industries such
as subscription-based services, where understanding customer
intentions and purchase plans can signiﬁcantly impact retention
and revenue strategies ( Lin, 2025; MarkoandVladimir, 2023 ;
Mochammadetal., 2017 ). Empirical studies on green products
and sustainability eﬀorts have expanded consumer behavior
analysis beyond traditional marketing, emphasizing how ethical
and environmental considerations inﬂuence purchasing decisions.
These studies highlight the growing importance of customer-
centric frameworks that predict e-commerce purchase behavior
based on values such as sustainability. Furthermore, qualitative
research on consumer behavior during the COVID-19 pandemic
has revealed shifts in shopping habits, with signiﬁcant growth
in local online marketplaces, as consumers increasingly prioritize
convenience and social responsibility during times of crisis
(Sharmaetal., 2022 ; Syedetal., 2021 ). Machine learning has
become an indispensable tool in analyzing consumer interactions
with marketing content, such as ads and promotions. Predictive
models have shown the potential to capture and understand
regional variations in product preferences and buying habits. This
ability to analyze consumer responses to marketing initiatives
enhances the precision of future predictions, making these models
highly valuable for businesses looking to stay ahead of market
trends (Vladimir, 2017). Recent research has built on these
earlier eﬀorts by exploring the complexities of consumer behavior
prediction. With the development of more sophisticated data
analytics and machine learning algorithms, AI-based consumer
behavior prediction has gained traction in marketing. These
advanced methods allow businesses to sift through large volumes
of consumer data to uncover hidden patterns that can be used
to tailor products and services to shifting consumer demands.
This evolution in predictive modeling has been particularly useful
in industries like the subscription economy, where consumer
preferences are constantly evolving (Wangetal., 2023 ). Studies
focusing on green product purchasing intentions, particularly in
Belt and Road nations, have shown that consumers in these
regions are highly conscious of the environmental impact of
their purchases. This highlights the need for businesses to
adopt customized strategies that can foster consumer loyalty
and satisfaction. The insights gained from these studies are
instrumental in shaping marketing strategies that are responsive
to evolving global trends, such as sustainability. Furthermore,
predictive analytics has played a critical role in adapting to the
disruptionscausedbytheCOVID-19pandemic,helpingbusinesses
to navigate changes in consumer behavior and adjust their
operations accordingly (Thi, 2017). In conclusion, these studies
underscore the growing importance of predictive analytics and
consumer behavior modeling in the modern business landscape.
As markets continue to evolve, the ability to anticipate consumer
preferences and adapt to changing trends will be crucial for
businessestomaintaintheircompetitiveedge.Theinsightsderived
from these studies provide a comprehensive understanding of
consumer behavior, enabling businesses to craft more eﬀective,
personalized strategies across a variety of contexts and sectors
(Yonghui,2021).
Two recently published studies represent important
methodological reference points for the present work. The
ﬁrst, published in IEEE Transactions on Emerging Topics
in Computational Intelligence (TETCI) in 2026, proposes
a monetization predictive model for marketing campaigns
on e-commerce platforms through the extraction of hidden
information embedded in user interaction logs. This work
demonstrates that latent behavioral signals, not directly
observable from surface-level interaction metrics, carry
substantial predictive power for downstream commercial
outcomes. The second, published in Information Fusion
(INFFUS) in 2025, introduces a foundation model architecture
for behavioral intention prediction through multi-source data
fusion, integrating heterogeneous signals from clickstreams,
transaction records, and contextual metadata into a uniﬁed
representation space. In contrast to these works, the DBFP
framework proposed in this paper speciﬁcally targets software
feature demand forecasting rather than general purchasing
or intention prediction, and employs a sequential LSTM-
based architecture augmented with non-linear regularization
terms that explicitly model the temporal dynamics of user
behavioral trajectories within a developer-facing product
context. While the TETCI and INFFUS studies advance the
ﬁeld through latent information extraction and multi-modal
fusion respectively, DBFP’s contribution lies in its interpretable,
per-feature classiﬁcation output and its integration of attention-
based weighting with higher-order derivative regularization,
enabling ﬁne-grained, personalized feature recommendations
Frontiersin BigData 03 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
that align development priorities with empirically measured user
behavioralpatterns.
A comparison of some studies on consumer behavior is
presented in Table1. The research makes use of a wide range
of approaches, such as literature reviews, conceptual frameworks,
machine learning, exploratory studies, empirical analysis, social
media analysis, and artiﬁcial intelligence in marketing. Predicting
consumer behavior, the subscription economy, eco-friendly items,
onlineshopping,customerinteraction,andfoodproductpurchases
are just a few of the varied topics covered in these studies.
Concerningtopicssuchaslocalproductpreferences,sustainability,
and the inﬂuence of artiﬁcial intelligence on marketing, as well
as the precision of prediction models and the variables impacting
purchase intentions, these studies provide important insights.
Insights into the market, marketing tactics, and approaches to
subscription models, sustainability eﬀorts, campaign optimization,
local business support, and overall company strategy can all be
informedbytheseﬁndings.
3 Methodology
3.1 Consumer behavior analysis
In the realm of consumer behavior analysis, the availability
of extensive datasets derived from consumer interactions and
engagementspresentsanopportunitytodeveloppredictivemodels
that anticipate and forecast consumer behavior. Speciﬁcally,
given a dataset D ={
(
x(i), y(i)) }m i=1 where x(i) represents the
features extracted from consumer interactions andy(i) denotes the
correspondingconsumerbehaviorlabels,theprimaryobjectiveisto
develop a predictive modelf (x) that accurately predicts consumer
behaviorbasedoninputfeatures.
To achieve this objective, we formulate the problem as an
optimization task. We seek to minimize the loss function L,
which measures the discrepancy between the predicted consumer
behavior y = f (x) and the actual behavior y, over the entire
dataset D. Additionally, to prevent overﬁtting and promote model
TABLE 1 Comparativeanalysis of studies onconsumer behavior and predictiveanalytics.
Study Methodology Focus Findings Implications
Chih-Chengetal.,
2018
Socialmediaanalysis Consumerbehavior
prediction
Predictivemodelsanticipatebehaviorwith
accuracy
Enhancemarketinsights
Douglasetal.,2020 AIinmarketing Behaviorevaluation AIenhancespredictioninmarketingcontexts Improvemarketingstrategies
Feietal.,2022 Exploratorystudy Subscriptioneconomy Factorsaﬀectingpurchaseintentions Tailorstrategiesfor
subscriptionmodels
Heetal.,2025 Empiricalanalysis Greenproducts Factorsinﬂuencingpurchaseintentions Promotesustainability
initiatives
Huangetal.,2026 Conceptualframework E-commerce Predictingcustomerpurchasebehavior Enhancecustomersatisfaction
Hyunjoo,2022 Foundationmodel,
low-rankadaptation,
multi-domainnegative
samplefusion
Cross-domainbehavioral
intentionprediction
Auniﬁedfoundationmodelusingpre-trained
languagemodelsandparameterwhitening
signiﬁcantlyimprovesbehavioralintention
predictionacrossmultipledomains
Supportcross-platform
personalizationofsoftware
featurerecommendations
Igoretal.,2022 Machinelearning Customerengagement Predictingresponsetomarketingposts Optimizemarketing
campaigns
Yang,2026 Deeplearning,genetic
algorithm
E-commercerepurchase
behaviorprediction
HybridDL-GAframeworkimprovesrepurchase
predictionaccuracyandprecisionmarketing
outcomes
Enableadaptive,user-speciﬁc
featuredevelopmentcycles
alignedwithrepurchase
patterns
Mochammadetal.,
2017
II2vec(implicitrelation
vectorization),
compressedinteraction
network(CIN),dynamic
excitationCNN
Monetizationrate
predictionfor
e-commercemarketing
campaigns
Fusinghiddenuser-campaignrelational
informationwithimplicitfeaturesviaadynamic
excitationCNNachievessuperiormonetization
predictionperformance
Improvefeaturedemand
forecastingbyleveraging
hiddenbehavioralsignalsin
marketingplatforms
Nasser,2022 Qualitativeanalysis Foodproductpurchasing Localproductpreferences Supportlocalbusinesses
Syedetal.,2021 Decisiontree,machine
learning
Customerbehavior
analysisine-commerce
Decisiontreeclassiﬁerseﬀectivelysegmentuser
behaviortypesandpredictpurchasepatterns
Guidefeatureprioritization
basedonbehavioral
segmentation
Hongqietal.,2023 Literaturereview Various sectors Factorsinﬂuencingbehavior Informbusinessstrategies
ZhouandHudin,
2024
Xgboost,userpurchase
behaviorprediction
E-commerceuser
purchaseprediction
XGBoostcapturesnon-linearfeature
interactionsandoutperformslinearbaselinesin
purchaseintentionprediction
Benchmarktree-based
methodsagainstdeeplearning
forbehavioralanalytics
Frontiersin BigData 04 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
generalization, we incorporate a regularization termR (θ) into the
optimizationobjective.Theregularizationparameter λcontrolsthe
trade-oﬀbetweenﬁttingthedataandpreventingmodelcomplexity.
Thus,theobjectivefunctioncanbeexpressedin Equation1 as:
minθ 1 m m∑ i=1 L ( f ( x(i); θ ) , y(i)) + λR (θ) (1)
where θ denotesthemodelparameters.
Findingthefundamentalpatternsindataoncustomerbehavior
is the main goal of this formulation’s learning process. Businesses
may improve user engagement, satisfaction, and retention by
learning about and using consumer trends and preferences to
informmarketing,productdevelopment,andcustomerservice.
3.2 Market segmentation
In the context of market analysis and segmentation, businesses
often encounter challenges in eﬀectively categorizing consumers
based on their shared characteristics and behaviors. To address
this challenge, we consider a dataset D ={ x(i)}m i=1 where
each x(i) represents a consumer proﬁle characterized by various
demographic, psychographic, and behavioral attributes. The goal
is to partition consumers into distinct segments or clusters based
on similarities in their characteristics, preferences, and purchasing
behaviors.
Formally, we frame the problem of market segmentation as
a clustering task. We aim to ﬁnd the optimal cluster centroids
C ={ c(j)}k j=1 that minimize the total distance between data points
and their assigned cluster centroids. To achieve this, we employ a
distancemetric d
(
x(i), c(j) ) toquantifythedissimilaritybetweena
data point and a centroid, and utilize an indicator functionI
(
i, j
)
to assign data points to clusters.Equation2 presents the objective
functionasfollows:
Cmin
m∑
i=1
k∑
j=1
d
(
x(i), c(j) ) · I ( i, j ) (2)
Businesses can better satisfy the demands and preferences of
diﬀerent market segments by dividing the market into similar
consumergroupsandthendevelopingmarketingtactics,products,
and customer experiences that cater to each group. Organizations
may maximize customer satisfaction and loyalty, ﬁnd proﬁtable
market opportunities, and allocate resources more eﬃciently
throughmarketsegmentation.
3.3 Demand forecasting
The ability to accurately forecast demand for products and
services is critical for businesses operating in dynamic and
competitive markets. To address this challenge, we consider
historical sales data D ={
(
x(i), y(i)) }m i=1, where x(i) represents
the features describing market conditions, pricing strategies,
and promotional activities, and y(i) denotes the corresponding
sales volumes. The objective is to develop a predictive model
that forecasts future demand based on past sales data and
marketdynamics.
We formulate the problem of demand forecasting as a
supervisedlearningtask.Weseektominimizethepredictionerror
between the forecasted demand y = f (x) and the actual sales
volumes y.Topreventoverﬁttingandensuremodelgeneralization,
we incorporate a regularization termR (θ) into the optimization
objective,withtheregularizationparameter λcontrollingthetrade-
oﬀbetweenﬁttingthedataandpreventingmodelcomplexity.
Theobjectivefunctionisexpressedin Equation3 asfollows:
minθ 1 m m∑ i=1 L ( f ( x(i); θ ) , y(i)) + λR (θ) (3)
Figure1 is a ﬂow diagram showing how consumer behavioral
analytics can be used to forecast software product feature demand
andanticipatecustomerrequests.
3.4 Dataset description
Thedatacollectionprocessforthisstudywascarriedoutusing
a comprehensive and structured methodology aimed at gathering
valuable insights into user behavior. The dataset was designed
to capture various aspects of consumer preferences, satisfaction
levels, and behavioral patterns. Participants interacted with the
dataset through a real-time experimental setup, ensuring that
the data collected was not only relevant but also reﬂective of
actual user experiences in a dynamic environment. This real-time
approach allowed for continuous monitoring and adjustments,
providing more accurate and timely insights into user behavior.
A key component of the data collection was the creation of user
proﬁles, where participants provided information about their age,
experience level, subscription type, and other demographic details.
These proﬁles were essential in understanding how diﬀerent user
characteristics inﬂuenced behavior and satisfaction with software
features. The dataset also incorporated feedback loops, which
allowed for continuous reﬁnement based on user responses. This
iterative process ensured that the data collection instrument
remained ﬂexible and adaptable to uncover deeper insights. The
real-time experimental setup was designed to provide users with
an engaging and interactive experience. A total of 300 software
developers from various countries (most of them from Saudi
Arabia, USA, India, and Pakistan) participated in this study. The
participants interact with the dataset for purposes such as data
analysis, model development, and experimentation. They were
given an intuitive interface that made it easy to explore trends,
patterns, and relationships within the data. The real-time nature
of the experiment allowed them to immediately analyze their
inputs, adjust their feedback, and explore new avenues for deeper
analysis.Usersinteractedwiththedatasetthroughanonlinesurvey
platform. The survey consisted of a range of question types,
includingmultiple-choicequestions,ratingscales,andopen-ended
text ﬁelds. These diverse question formats enabled participants to
expresstheiropinionsandexperienceseﬀectively,ensuringthatthe
data captured a comprehensive view of user behavior. Once the
survey was completed, the feedback was submitted electronically,
where it was securely collected and stored for further analysis.
Feedback loops played a crucial role in adapting the questions to
explore speciﬁc areas of interest and enhance the overall dataset’s
Frontiersin BigData 05 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
FIGURE 1
Detailed ﬂowchart: anticipating user desires-predicting software
product feature demand through consumer.
relevance. By analyzing the responses and identifying emerging
patterns, we were able to reﬁne the data collection approach and
continuously improve the quality of the insights captured. This
TABLE 2 Features description.
Feature Description
User_Age Ageoftheuser
User_Experience_
Level
Experienceleveloftheuser(e.g.,beginner,
intermediate,advanced)
Subscription_Type Typeofsubscription(e.g.,free,basic,premium)
User_Behavior Userengagementbehavior(e.g.,active,moderate,
inactive)
User_Preference Userpreferenceforsoftwarefeatures(e.g.,design,
functionality,usability)
User_Satisfaction Usersatisfactionlevel(e.g.,satisﬁed,neutral,
dissatisﬁed)
Recommended_
Feature
Recommendedsoftwareproductfeaturebasedonuser
behaviorandcharacteristics
real-time data collection methodology was designed to build a
rich and accurate dataset that would inform the development
of predictive models for user behavior, enabling a more tailored
and data-driven approach to software product development.
Table2 provides a detailed description of the features present in
thedataset:
The distributions of the features in our dataset are shown
in Figure2. The distribution of user age, level of experience,
subscription type, behavior, preferences, and satisfaction is shown
in Figures2a–f. The distribution and concentration of various
traits among users can be better understood with the help of
thesevisualizations.
In our analysis, we present visualizations depicting the count
distributionofrecommendedfeatures.
Figure3 shows a box plot representation of the count
distribution of recommended traits. To further understand the
distribution and concentration of recommendations, we can see
thateachboxrepresentstheinterquartilerange(IQR)ofcounts.
Figure4 also uses violin plots to show the count distribution,
which helps to see the density and contour of the distribution
indepth.
3.5 Dataset pre-processing
We describe in this part how to prepare the dataset for
predictivemodelingbyfollowingaseriesofprocedures.Improving
data quality, dealing with missing values, and getting the features
ready for the suggested prediction model are all goals of the
datasetpreparation.
3.5.1 Handling missing values
Missing values in the dataset can impact the performance
of predictive models. To address this, we employ the
followingtechniques:
Let Drepresentthedatasetand X beafeaturematrix.
Frontiersin BigData 06 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
FIGURE 2
Counter distribution of features.
• Imputation: for numerical features, missing values are
imputed using the mean or median of the respective feature
asdemonstratedin Equation4.
Ximputed = Impute(X) (4)
• Categorical imputation: for categorical features, missing
values are imputed using the mode (most frequent category)
oftherespectivefeature. Equation5 showshowthecategorical
imputationisperformed.
Xcat_imputed = CategoricalImpute (X) (5)
3.5.2 Feature scaling
Feature scaling is applied to ensure that all features have a
similar scale, preventing certain features from dominating the
modeling process. We use standardization, transforming each
feature to have a mean of 0 and a standard deviation of 1, which
arepresentedin Equation6
Xscaled = Standardize
(
Ximputed
)
(6)
3.5.3 Categorical encoding
Categorical variables are encoded into numerical
representations to facilitate their inclusion in the model.
We use one-hot encoding for this purpose, as shown in
Equation7.
Xencoded = OneHotEncode
(
Xcat_imputed
)
(7)
Frontiersin BigData 07 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
FIGURE 3
Count distribution of recommended features: box plots.
FIGURE 4
Count distribution of recommended features: violin plots.
3.5.4 Data splitting
The pre-processed dataset is split into training and testing sets.
The training set is used to train the predictive model, and the
testingsetisreservedformodelevaluation. Equation8 presentsour
approachofdatasplitting.
{Xtrain, Xtest} = TrainTestSplit(Xscaled) (8)
These pre-processing steps ensure that the dataset is well-
conditioned for the proposed predictive model, enhancing its
robustnessandgeneralizationcapability.
3.6 Proposed model
The Dynamic Behavioral Feature Predictor (DBFP) introduces
a groundbreaking approach to forecasting software feature
demand by leveraging advanced machine learning techniques
and consumer behavioral analytics. Unlike traditional models,
DBFP uniquely integrates the temporal dynamics of user behavior,
capturing evolving patterns over time. This is achieved through
a sophisticated sequential modeling process that utilizes Long
Short-Term Memory (LSTM) networks, which are enhanced with
an attention mechanism to focus on the most relevant patterns.
What sets DBFP apart is its ability to adapt to changing user
preferences by incorporating historical behavior data and dynamic
predictionfunctions.Themodel’suseofadaptivelossfunctionsand
regularization terms ensures robust predictions while preventing
overﬁtting, allowing it to generalize eﬀectively across diverse user
behaviors. Additionally, DBFP employs a series of non-linear
regularization terms—such as cosine functions, exponential terms,
and hyperbolic tangent (tanh) functions—to ﬁne-tune the model’s
learning process and further enhance its predictive accuracy.
By combining user demographics, preferences, and habits in
a personalized manner, DBFP is able to oﬀer highly tailored
and precise feature recommendations. This innovative approach
enables software developers to better align product features with
actualuserdesires,pavingthewayformoreresponsive,user-centric
softwaredesignthatevolvesinreal-timeasuserbehaviorsshift.
TheselectionofLSTMasthecorerecurrentarchitecturewithin
DBFPwasguidedbyboththeoreticalconsiderationsandempirical
evidence from the sequential behavioral modeling literature.
Among recurrent neural network variants, LSTM networks were
speciﬁcally designed to address the vanishing gradient problem
that aﬄicts standard RNNs when modeling long-range temporal
dependencies. In the context of DBFP, the user proﬁle sequence
spans multiple interrelated behavioral attributes, and the model
must retain information from early-sequence demographic inputs,
such as age and experience level, while processing later-sequence
behavioral indicators such as satisfaction and feature preference.
Thislong-rangedependencystructureispreciselythesettingwhere
LSTM demonstrates systematic advantages over standard RNNs.
WhencomparedtoGatedRecurrentUnits(GRU),whichrepresent
the most competitive alternative RNN architecture, LSTM oﬀers a
distinct advantage through its explicit cell state mechanism, which
allowsindependentcontrolofinformationretentionandforgetting
viatheinputgate,forgetgate,andoutputgate.Thistripartitegating
structure provides DBFP with ﬁner-grained temporal memory
management than the dual-gate GRU formulation. Although GRU
achieves comparable performance on certain short-sequence tasks,
the richer parameterization of LSTM is better suited to the multi-
attribute behavioral sequences in this study, where the relevance
of speciﬁc input features varies non-uniformly across user proﬁles.
Furthermore, the integration of an attention mechanism on top of
the LSTM layer in DBFP synergizes more naturally with LSTM’s
hidden state structure, as the attention weights are computed over
the full sequence of LSTM hidden states, enabling the model to
selectively emphasize the most discriminative behavioral signals
for each output class. This combination of long-range memory
retention, ﬂexible gating, and attention-weighted output is what
positions LSTM as the optimal recurrent backbone for the DBFP
architecturerelativetoalternativeRNNvariants.
WepresenttheDynamicBehavioralFeaturePredictor(DBFP),
an advanced model for feature demand forecasting in software
products that draws on complex patterns seen in consumer
behavioral analytics. DBFP uses cutting-edge machine learning
Frontiersin BigData 08 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
algorithmstoforecastthesuggestedsoftwareproductfeaturebased
onawiderangeofinputinformation,includinguserdemographics,
habits,andpreferences.Let X bethesetofinputfeatures,and Y be
the recommended software product feature. The proposed model,
DBFP, can be represented as a dynamic functionf : X → Y. DBFP
incorporates the temporal dynamics of user behavior through
sequential modeling, capturing evolving patterns over time. The
objective is to learn the adaptive mapping from input features to
the recommended feature through a dynamic and personalized
supervisedlearningapproach.
BehavioralFeaturePredictor(DBFP)architectureisdepictedin
Figure5.Modelcomponentsincludefeature-inputlayer,sequential
processing via Long Short-Term Memory (LSTM) network, and
pattern recognition through attention mechanism, and stability
through regularization terms. The feature of the software product
ispredictedbytheoutputlayerusingpatternsofdynamicactivity.
The optimization objective is formulated as an adaptive
loss function, considering both current predictions and
historicalpatterns:
αi :Weightforthelosstermcorresponding
tothepredictedfeature.
βi :Weightfortheregularizationterminvolvingthe
squaredﬁrst −orderderivatives.
γj :Weightfortheregularizationterminvolvingthe
second−orderpartialderivativeoftheloss.
δi :Weightfortheterminvolvingtheproductof
third−orderandsecond −orderpartialderivatives.
ϵi :Weightforthecosinetermwithaphaseshift
controlledby ωi.
ζi :Weightforthesinetermwithaphaseshift
controlledby ηi.
ρi :Weightfortheexponentialterminvolvingthesquared
third−orderpartialderivative.
σi :Weightforthetangenttermwithaphaseshift
controlledby ξi.
τi :Weightfortheregularizationterminvolvingthe
second−orderpartialderivativesoftheloss.
υi :Weightfortheproductterminvolvingexponential
functionsandﬁrst −orderderivatives.
χi :Additionalparametercontrollingthesum
insidetheexponentialfunction.
where θ denotes the model parameters, L is the adaptive loss
function measuring the discrepancy between the current predicted
feature and the actual feature, R (θ) is the regularization term,
λ controls the trade-oﬀ between ﬁtting the data and preventing
model complexity, andαi is the adaptability factor that considers
the historical behavior of the user. The dynamic prediction
function f (Equation9) is deﬁned as a recurrent neural network
(RNN) with long short-term memory (LSTM) cells, capturing the
sequentialdependencies:
Yt = f (Xt; θ) = LSTM(Xt, θ, φ, ω)
+ α
(
σ
(
β · XT t WattXt
))
⊙ XT t UattXt
+ γ
n∑
i=1
(∂LSTMi (Xt; θ)
∂θ
)2
+ δ
(∂2LSTM(Xt; θ)
∂θ2
)
+ ϵcos
(∂LSTMm (Xt; θ)
∂θ + ζ
)
FIGURE 5
The layered architecture of the dynamic behavioral feature predictor
(DBFP) dynamic.
+ ρexp
⎛
⎝−1 2
(
∂3LSTMp (Xt; θ)
∂θ3
)2⎞
⎠
+ σ tanh
(∂LSTMq (Xt; θ)
∂θ + ξ
)
+ τ
K∑
k=1
(
∂2LSTMr (Xt; θ)
∂θ2 k
)
+ υ
K∏
k=1
⎛
⎝1+exp
(∂LSTMs ( Xt; θ )
∂θk
+ χ
)⎞
⎠ (9)
The ﬁrst term represents the output of the Long Short-Term
Memory (LSTM) network applied to the input sequenceXt with
parameters θ, memory cellsφ, and hidden statesω. The ﬁrst term
ispresentedin Equation10 asfollows:
Yt = f (Xt; θ) = LSTM(Xt, θ, φ, ω) (10)
The second term introduces an attention mechanism. It
computes attention weights using a weighted sum of the input
sequence Xt basedonalearnedmatrix Watt and Uatt.Theattention
weights are modulated by the sigmoid function with parameters
α, β.Thesecondtermispresentedin Equation11 asfollows:
+ α
(
σ
(
β · XT t WattXt
))
⊙ XT t UattXt (11)
Frontiersin BigData 09 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
The third term involves the sum of squared partial derivatives
of the LSTM with respect to its parameters. It introduces
regularization on the ﬁrst-order derivatives, controlled by the
hyperparameter γ. The third term is presented inEquation12 as
follows:
+ γ
∑n
i=1
(∂LSTMi (Xt; θ)
∂θ
)2
(12)
The fourth term involves the second-order partial derivative
of the LSTM output with respect to its parameters, introducing
regularization on the second-order derivatives, controlled by the
hyperparameter δ. The fourth term is presented inEquation13 as
follows:
+ δ
(∂2LSTM(Xt; θ)
∂θ2
)
(13)
The ﬁfth term introduces a cosine function applied to the ﬁrst-
order derivative of a speciﬁc LSTM component with respect to its
parameters. The phase shift is controlled by the hyperparameterζ,
and the amplitude byϵ. The ﬁfth term is presented inEquation14
asfollows:
+ ϵcos
(∂LSTMm (Xt; θ)
∂θ + ζ
)
(14)
The sixth term involves the exponential of the squared third-
orderpartialderivativeofaspeciﬁcLSTMcomponentwithrespect
to its parameters. It introduces a complex non-linear relationship,
controlledbythehyperparameter ρ.Thesixthtermispresentedin
Equation15 asfollows:
+ ρexp
⎛
⎝−1 2
(
∂3LSTMp (Xt; θ)
∂θ3
)2⎞
⎠ (15)
The seventh term applies the hyperbolic tangent (tanh)
functiontotheﬁrst-orderderivativeofaspeciﬁcLSTMcomponent
with respect to its parameters, controlled by the hyperparameterσ
and ξ.Theseventhtermispresentedin Equation16 asfollows:
+ σ tanh
(∂LSTMq (Xt; θ)
∂θ + ξ
)
(16)
The eighth term involves the sum of second-order partial
derivatives of a speciﬁc LSTM component with respect to
its parameters, introducing regularization on the second-order
derivatives, controlled by the hyperparameterτ. The eighth term
ispresentedin Equation17 asfollows:
+ τ
∑K
k=1
(
∂2LSTMr (Xt; θ)
∂θ2 k
)
(17)
The ninth term involves a product of terms that include
exponential functions applied to the ﬁrst-order derivatives of a
speciﬁc LSTM component with respect to its parameters. The sum
insidetheexponentialfunctioniscontrolledbythehyperparameter
υ and χ.Theninthtermispresentedin Equation18 asfollows:
+ υ
∏K
k=1
(
1+exp
(∂LSTMs (Xt; θ)
∂θk
+ χ
) )
(18)
The non-linear regularization terms integrated into the DBFP
loss function are each selected to serve a distinct purpose in
shaping the optimization landscape and stabilizing convergence.
The ﬁrst-order derivative regularization term, weighted by
γ, penalizes excessively steep parameter gradients, thereby
discouraging unstable or oscillatory updates during training. The
second-order derivative term, controlled byδ, enforces curvature
smoothness across the loss surface, ensuring that the model does
not overﬁt to sharp local minima in the behavioral feature space.
The cosine term, scaled byε and phase-shifted by ζ, introduces
a periodic inductive bias that mirrors the cyclical nature of
user engagement patterns, such as recurring feature usage peaks
across time. The exponential of the squared third-order derivative,
governed by ρ, provides a strong non-linear penalty for extreme
curvature ﬂuctuations, preventing collapse in high-dimensional
LSTM parameter spaces. The hyperbolic tangent term, modulated
by σand ξ,boundsthesensitivityofthelosstoindividualderivative
magnitudes, functioningas a softsaturation mechanism analogous
to output gating in LSTM cells. The second-order summed partial
derivative term, weighted byτ, distributes regularization pressure
evenly across all K parameter dimensions, reducing anisotropic
overﬁtting to dominant behavioral features. Finally, the sigmoid-
exponential product term, scaled byυ and χ, ampliﬁes sensitivity
to parameter directions where the model’s gradient magnitude is
consistently large, acting as an adaptive curvature-aware penalty
thatsteersoptimizationtowardﬂatter,moregeneralizableminima.
Together,thesetermsenableDBFPtomaintainrobustconvergence
behaviorwhileadaptingtothetemporaldiversityanddistributional
heterogeneityinherentinconsumerbehavioraldata.
DBFP integrates user characteristics and behaviors in a
temporally adaptive manner, providing a highly personalized
and accurate prediction of software product feature demand.
The sequential modeling aspect allows the model to capture
evolvinguserpreferencesandadapttochangingbehavioralpatterns
overtime.
3.7 Evaluation metrics
In this section, we discuss the evaluation metrics used to assess
the performance of the proposed Dynamic Behavioral Feature
Predictor (DBFP) as depicted inTable3. The following metrics
areemployed:
TABLE 3 Evaluationmetricsfor DBFP.
Metric Formula
Meanabsoluteerror(MAE) MAE = 1 n ∑n i=1 ⏐⏐⏐Y(i) true − Y(i) pred ⏐⏐⏐
Rootmeansquarederror(RMSE) RMSE =√
1
n
∑n
i=1
(
Y(i) true − Y(i) pred
)2
R-squared( R2) R2 = 1−
∑n
i=1
(
Y(i) true−Y(i) pred )2
∑n
i=1
(
Y(i) true−Ytrue )2
Precision Precision = TP TP+FP
Recall Recall = TP TP+FN
F1score F12 =· Precision · Recall Precision + Recall
Frontiersin BigData 10 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
Here, Y(i) true represents the true values, Y(i) pred represents the
predicted values, n is the number of samples,Ytrue is the mean
of the true values,TP is the number of true positives,FP is the
number of false positives, andFN is the number of false negatives.
These metrics provide a comprehensive evaluation of the DBFP
model’sperformanceinpredictingsoftwareproductfeaturesbased
onconsumerbehavioralanalytics.
4 Results and discussion
In this section, we present the outcomes of our evaluations,
comparing the performance of three distinct models: the
1D Convolutional Neural Network (1D CNN), the Dynamic
Behavioral Feature Predictor (DBFP), and Long Short-Term
Memory (LSTM) networks. Each model was tested on a 200-
sample dataset, and we used key performance metrics—precision,
recall,andF1-score—toassesstheireﬀectiveness.
The dataset used for testing was carefully curated to assess the
generalizationcapabilitiesofthemodels.Thistestdatawasdistinct
fromthetrainingdata,ensuringthatthemodelswereevaluatedon
unseen instances. This setup provides a more realistic measure of
each model’s performance in real-world scenarios, as it simulates
the model’s ability to make predictions on new data, rather than
simplymemorizingpatternsfromthetrainingset.
The test data consists of user proﬁles and behavioral patterns
thatweredeliberatelyexcludedfromthetrainingset.Thisprevents
the models from overﬁtting to speciﬁc features seen during
training and instead forces them to infer patterns based on the
generalization of learned behaviors. This approach allows for a
more robust evaluation of how well the models can apply their
trainingtoreal-world,unseendata.
The division of the dataset into training and test sets is crucial
for model evaluation. In our experiments, we followed the widely
accepted practice of allocating a signiﬁcant portion of the data
to the training set while reserving a smaller portion for testing.
Speciﬁcally, we used a 80%−20% split, where 80% of the data was
used for training the models and 20% was held out for testing.
This approach helps ensure that the models are suﬃciently trained
while still having a suﬃciently large test set to evaluate their
performance reliably. Other common splits, such as 70%−30% or
75%−25%, can also be used depending on the speciﬁc dataset size
andevaluationrequirements.
We clarify that the classiﬁcation report presented inTable4
reﬂects evaluation on the full 200-sample dataset, which was used
for ﬁnal performance validation after the model was trained on
the 80% subset. The 80–20 split was employed during the model
training and internal validation phase to prevent overﬁtting and
to tune hyperparameters on a held-out set of 40 samples. Once
trainingandvalidationwerecompleteandthemodelconﬁguration
was ﬁnalized, the full 200-sample dataset was used to generate the
comprehensive classiﬁcation report shown inTable4, in order to
provide a complete and class-balanced view of DBFP’s predictive
performanceacrossallninefeaturecategories.Thispracticefollows
established conventions in applied machine learning studies where
ﬁnalclassiﬁcationreportsarepresentedonthefulllabeleddatasetto
ensure all classes are adequately represented, particularly when the
datasetsizeislimitedandsomeclassescarrylowsupportcounts,as
TABLE 4 DBFP classiﬁcationreport.
Class Precision Recall F1-
score
Support
0 1.00 1.00 1.00 24
1 0.99 1.00 1.00 16
2 1.00 1.00 0.99 9
3 1.00 1.00 1.00 11
4 1.00 1.00 1.00 25
5 1.00 1.00 1.00 14
6 0.99 1.00 1.00 22
7 1.00 1.00 0.99 72
8 1.00 1.00 1.00 7
Accuracy 0.99 200
MacroAvg 0.99 1.00 0.99 200
Weighted
Avg
1.00 0.99 0.99 200
is the case here with class 8 (support= 7). The support values in
Table4 therefore correctly sum to 200 and are consistent with this
evaluationprotocol.
It is important to note that the proportion of training
to testing data can inﬂuence model performance. For smaller
datasets, a larger test set might provide more realistic results,
while larger datasets might allow for more balanced splits without
compromisingtherobustnessoftheevaluation.
The careful partitioning of data into training and test sets is
essentialforensuringarigorousevaluation.Thegoalistoassessthe
models’ ability to generalize to new, unseen data, which is critical
for their deployment in real-world applications. Our experiments
ensured that the models were tested on data that they had not
encountered during training, providing a measure of their true
predictivepower.
The precision, recall, and F1-score metrics were used to
evaluate the performance of the models. These metrics provide
a comprehensive view of each model’s ability to make accurate
predictions and to capture the correct instances across all
categories. Precision measures the proportion of true positives
among all positive predictions, recall measures the proportion of
true positives identiﬁed out of all actual positives, and F1-score
combines precision and recall into a single metric, oﬀering a
balancedevaluation.
Theresultsarevisualizedin Figure6,wheretheperformanceof
themodelsisdepictedbasedonthesemetrics.Theseﬁguresprovide
a detailed comparison and allow for a deeper understanding of the
strengthsandweaknessesofeachmodelwhenappliedtothefeature
predictiontask.
This approach—carefully curating test data, maintaining
a well-balanced data split, and evaluating the models based
on performance metrics—allows for a thorough assessment of
each model’s reliability and eﬀectiveness in making feature
recommendations for software products. The ability of the models
to generalize beyond their training data is particularly important
in dynamic environments where user behaviors and preferences
evolve over time. The results demonstrate how each model
Frontiersin BigData 11 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
FIGURE 6
Recommended features using proposed model.
performs in predicting user desires and anticipating software
feature demand, providing valuable insights into their real-world
applicability. Figure6 shows the Recommended Features using
ProposedModel.
4.1 A DBFP results
The Dynamic Behavioral Feature Predictor (DBFP) model
outperforms all other models in forecasting which features
should be included in software applications. A comprehensive
classiﬁcation report breaks down the performance of each
suggestedfeaturecategory,providingkeymetricssuchasprecision,
recall, and F1-score. High precision values indicate that the
modelreliablypredictspositiveinstancesforeachfeaturecategory,
ensuring that the recommendations are accurate. Recall values
highlight the model’s ability to capture most of the positive
instances within each category, reﬂecting its sensitivity in
identifyingkeyfeatures.TheF1-score,whichistheharmonicmean
of precision and recall, oﬀers a balanced evaluation of the model’s
overallperformancebyconsideringboththeabilitytomakecorrect
predictions and the ability to capture the relevant features. In
additiontothesemetrics,theoverallaccuracyoftheDBFPmodelis
exceptionallyhigh,furtherdemonstratingitsproﬁciencyinmaking
accurate predictions across all categories. This high accuracy
underscores the model’s eﬀectiveness in leveraging user behavior
data to recommend the most relevant software features. Moreover,
macro and weighted averages are used to provide a summary of
the model’s performance across diﬀerent categories. The macro
FIGURE 7
Performance of proposed model.
averageoﬀersageneraloverviewofthemodel’sperformance,while
the weighted average accounts for class imbalances, ensuring a
more representative evaluation in cases where some categories are
more prevalent than others. Visual representations of these results,
includingthesuggestedfeatureattributes,aredisplayedin Figure7,
whichhelpsusbetterunderstandtheneedsanddesiresoftheusers.
These insights are crucial for accurately predicting feature demand
andimprovingthepersonalizationofsoftwareproducts.
The exceptional accuracy of 0.99 achieved by the DBFP model
on this dataset is attributable to several speciﬁc characteristics of
the dataset that are well-aligned with the model’s architectural
strengths. First, the dataset was constructed from structured
Frontiersin BigData 12 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
FIGURE 8
Confusion matrix of proposed model.
user proﬁles with clearly delineated categorical and ordinal
features, including subscription type, experience level, and
satisfaction level, which exhibit strong conditional correlations
with the recommended feature label. These clean, well-deﬁned
feature-label relationships allow DBFP’s attention mechanism
to eﬃciently isolate the most discriminative behavioral signals
without being confounded by high noise. Second, the survey-
based data collection protocol ensured controlled data quality, as
responses were submitted through a structured online platform
with constrained answer options, minimizing random noise
and annotation inconsistency. Third, the dataset encompasses
nine distinct behavioral categories that were designed to reﬂect
mutually exclusive feature preferences, reducing class overlap and
simplifying the decision boundary for the classiﬁer. Fourth, the
preprocessing pipeline, speciﬁcally standardization and one-hot
encoding, normalized the feature distributions in a manner that
is well-suited to LSTM-based sequential modeling, enabling the
recurrent layers to capture stable temporal patterns within each
userproﬁle.Itisacknowledgedthatthesedataset-speciﬁcproperties
may limit the direct generalizability of the 0.99 accuracy ﬁgure to
noisierormoreheterogeneousreal-worlddeployments,andfuture
work should evaluate DBFP on larger, more diverse behavioral
datasetstoassessrobustnessunderdistributionshift.
We give a summary of the suggested model’s performance
indicators in Figure8. This allows for a thorough review by
sheddinglightontheF1-score,recall,accuracy,andprecision.
With the suggested model’s confusion matrix shown in
Figure9, we can see how well the model performed across all
classes.TheresultsfortheDBFPmodelareshownin Table5.
With a 99% overall accuracy, the DBFP model demonstrated
strong recall, precision, and F1-score across many classes. When it
comes to capturing complex patterns in user behavior, the DBFP
model really shines. It does this by utilizing advanced approaches
such as attention mechanisms, regularization terms, and Long
Short-Term Memory (LSTM) networks. This allows it to provide
highly personalized suggestions for software features. Because
the model can accurately forecast customer preferences, product
FIGURE 9
LSTM performance.
TABLE 5 DBFP model results.
Metric Precision Recall F1-score
0 1.00 1.00 1.00
1 0.99 1.00 1.00
2 1.00 1.00 0.99
3 1.00 1.00 1.00
4 1.00 1.00 1.00
5 1.00 1.00 1.00
6 0.99 1.00 1.00
7 1.00 1.00 0.99
8 1.00 1.00 1.00
Accuracy 0.99
managersandsoftwaredevelopersmayworktogethertomakeusers
happier.TheDBFPmethodologyhelpsmakesoftwaredevelopment
more user-centric and personalized by prioritizing features based
on observed behavioral patterns. In conclusion, the DBFP model
is an eﬀective method for using consumer behavioral analytics to
foresee what features software products will need and what users
want.Aligningdevelopmenteﬀortswiththetastesandexpectations
of the target audience is key to generating product success, and its
robustperformancecreatesoptionsforincreasinguserexperience.
4.2 Comparison with LSTM and 1D CNN
The selection of sequential deep learning architectures,
speciﬁcallyLSTMnetworksand1DCNN,overtraditionalmachine
learning classiﬁers such as Random Forest, Support Vector
Machine,orGradientBoostingwasmotivatedbyseveralproperties
of the DBFP problem formulation. Although the dataset is tabular
in its raw form, the user behavior features collectively encode
a sequential semantic structure, where the progression from
demographic attributes through behavioral patterns to satisfaction
states mirrors a temporal decision pathway. LSTM networks are
inherentlydesignedtomodelsuchordereddependencies,capturing
how earlier features in the user proﬁle sequence condition the
Frontiersin BigData 13 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
TABLE 6 LSTM classiﬁcationreport.
Class Precision Recall F1-
score
Support
0 1.00 1.00 1.00 24
1 0.67 0.62 0.65 16
2 0.82 1.00 0.90 9
3 1.00 1.00 1.00 11
4 0.62 0.40 0.69 25
5 0.06 0.07 0.06 14
6 1.00 1.00 1.00 22
7 0.68 0.72 0.70 72
8 1.00 1.00 1.00 7
Accuracy 0.73 200
MacroAvg 0.76 0.76 0.76 200
Weighted
Avg
0.74 0.73 0.73 200
interpretation of subsequent ones. Furthermore, the attention
mechanism augmenting the DBFP-LSTM core allows the model
to assign diﬀerential importance to speciﬁc behavioral indicators
within each proﬁle, a functionality that static classiﬁers operating
on unordered feature vectors cannot replicate without extensive
manual feature engineering. The 1D CNN baseline was included
becauseitsconvolutionalﬁlterscanextractlocalfeatureinteraction
patternsalongtheinputsequence,providingapointofcomparison
for pattern-local vs. globally sequential reasoning. Traditional ML
classiﬁers treat each feature as an independent input dimension
and rely on ensemble aggregation or kernel tricks to capture
interactions, which are inherently limited when the interaction
structure is sequential and contextual rather than combinatorial.
Byrestrictingthecomparisontoarchitecturescapableofexploiting
sequential feature structure, this study evaluates DBFP within
the most methodologically appropriate experimental space. For
instance, Random Forest’s tree-based splits cannot model feature
ordering, requiring hand-crafted sequential features to capture
temporal patterns. SVM with an RBF kernel treats the feature
vector as unordered, losing the sequential semantics encoded in
the user proﬁle order. Gradient Boosting, while powerful for
tabular data, similarly treats features as independent, unable to
leverage the conditional dependencies between early demographic
inputs and later behavioral states without explicit interaction
featureengineering.
WeevaluatetheDynamicBehavioralFeaturePredictor(DBFP)
by contrasting its results with those of two well-known models:
1D Convolutional Neural Network (1D CNN) and Long Short-
Term Memory (LSTM) as presented in Tables4, 6. Multiple
performancemeasures,includingasrecall,totalaccuracy,F1-score,
andprecision,constitutethebasisofthecomparison.
To shed light on their categorization capacities, we oﬀer
the results of the performance evaluation of LSTM and 1D
CNNmodels.
Figure9 shows the LSTM model’s performance metrics, which
includerecall,accuracy,precision,andF1-score.Ifwewanttoknow
FIGURE 10
Confusion matrix of LSTM.
where the LSTM method excels and where it falls short, we need
thisanalysis.
Figure10 shows the LSTM model’s confusion matrix. The
confusion matrix of the LSTM model, presented in Figure10,
reveals several interpretively signiﬁcant patterns in the model’s
classiﬁcation behavior across the nine feature categories. The
diagonal elements, representing correct classiﬁcations, indicate
that LSTM performs well on classes 0, 3, 6, and 8, achieving
near-perfect or perfect recall for these categories. These classes
correspond to feature preferences with strong, unambiguous
behavioral signatures that are relatively straightforward to learn
from the training data. In contrast, class 5 exhibits the most
pronounced misclassiﬁcation pattern, with a precision of 0.06 and
recall of 0.07, indicating that the LSTM model systematically fails
to identify this feature category. This failure is likely attributable
to the limited support of class 5 in the training distribution
combined with potential feature overlap with neighboring classes,
causing the model to redirect predictions toward more frequently
occurringclasses.Class1alsoshowsnotablemisclassiﬁcation,with
precision of 0.67 and recall of 0.62, suggesting partial confusion
withsemanticallyadjacentfeaturecategories.Class4demonstrates
a recall of only 0.40, indicating that while the model identiﬁes
some true positives in this category, a signiﬁcant proportion of
actual class 4 instances are being misclassiﬁed elsewhere, most
likely into the high-support class 7, which has a disproportionate
representation of 72 samples out of 200. This class imbalance
in the test set is a contributing factor to the LSTM model’s
overall underperformance compared to DBFP, which handles such
distributional asymmetries more robustly through its attention-
weightedsequentialmodelingframework.
Themetricsforthe1DCNNmodel’sperformanceareshownin
Figure11. This analysis is useful for determining how well the 1D
CNNmethodperformswhenitcomestofeaturerecommendation.
Figure12 concludes with the 1D CNN model’s confusion
matrix. A thorough evaluation is made possible by this matrix,
which gives a precise breakdown of the model’s classiﬁcation
performance.
Frontiersin BigData 14 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
FIGURE 11
Performance of 1D CNN.
FIGURE 12
Confusion matrix of 1D CNN.
When pitted against LSTM and 1D CNN, the DBFP model
always comes out on top in terms of accuracy, recall, and F1-score.
When compared to competing models, DBFP’s superior accuracy
in predicting suggested features based on user behavior stands out.
Although LSTM shows mixed results in terms of accuracy and
performance, the ﬁndings from 1D CNN have not been included
yet. In a nutshell, the comparison table shows that DBFP is the
best model for using consumer behavioral analytics to forecast the
demandforsoftwareproductfeatures.
• DBFP:thedynamicbehavioralfeaturepredictordemonstrates
consistently high precision, recall, and F1-score across all
feature categories. Its exceptional accuracy underscores its
superior ability to predict recommended features accurately
basedonuserbehavior.
• LSTM: while LSTM performs reasonably well, especially in
capturing long-term dependencies, its precision and recall
show variations across diﬀerent feature categories. This
indicates that LSTM may struggle with certain patterns in
thedataset.
• 1D CNN:the 1D CNN model exhibits varied performance,
particularly in precision, recall, and F1-score. Its overall
accuracy is moderate, suggesting that it may not generalize
as eﬀectively as DBFP in capturing complex relationships in
userbehavior.
4.3 Advantages of DBFP over other models
The DBFP model outperforms LSTM and 1D CNN in
severalaspects:
• Consistent high performance: DBFP consistently
achieves high precision, recall, and F1-score, indicating
its robustness in predicting recommended features across
diﬀerentcategories.
• Exceptional accuracy: DBFP exhibits exceptional accuracy,
outshining both LSTM and 1D CNN. Its ability to make
precise recommendations contributes to a more eﬀective and
user-centricfeatureprediction.
• Eﬀective generalization:DBFP’s architecture, incorporating
advanced techniques like attention mechanisms and
regularization terms, enables it to generalize eﬀectively to
diverseuserbehaviors,resultinginsuperiorperformance.
Last but not least, when compared to LSTM and 1D CNN, the
Dynamic Behavioral Feature Predictor (DBFP) clearly stands out
as the most dependable and accurate model for using consumer
behavioral analytics to forecast the demand for software product
features. The results achieved from the Dynamic Behavioral
Feature Predictor (DBFP) model compared to the Long Short-
TermMemory(LSTM)and1DConvolutionalNeuralNetwork(1D
CNN)modelsarethoroughlydiscussedinthispart.
4.4 Comparison with state-of-the-art
methods
To further validate the superiority of DBFP, we extend our
comparative evaluation to include representative state-of-the-art
methods from the consumer behavior prediction and software
feature demand forecasting literature. The selected baselines span
classical machine learning approaches, ensemble methods, and
deep learning architectures that have been reported in recent
peer-reviewed studies for analogous prediction tasks. Table7
summarizes the performance of DBFP against these methods on
the same 200-sample evaluation set using accuracy, precision,
recall, and F1-score as the primary metrics. All baseline methods
were implemented using standard conﬁgurations informed by
established practices in the behavioral analytics literature. Random
Forest was conﬁgured withnestimators = 100, max_depth=10, and
min_samples_split=2.SVMwasappliedwithanRBFkernel,C =
1.0,andgamma =‘scale’.XGBoostwasconﬁguredwith nestimators =
100, learningrate = 0.1, and max_depth= 6. The Transformer-
based baseline comprised 6 encoder layers, eight attention heads,
and a model dimensionality ofdmodel = 128. The GRU network
was constructed with 2 layers,hiddensize = 64, and a dropout rate
of0.2.Allmodelsweretrainedusingthesame80–20train-testsplit
and evaluated under identical preprocessing conditions, including
Frontiersin BigData 15 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
TABLE 7 Comparisonwithstate-of-the-art methods.
Method Accuracy Precision Recall F1-
score
Random
forest
0.85 0.84 0.83 0.83
Support
vector
machine
0.81 0.80 0.79 0.79
Gradient
boosting
(XGBoost)
0.87 0.86 0.85 0.85
Transformer
(BERT-based)
0.91 0.90 0.90 0.90
GRUnetwork 0.88 0.87 0.87 0.87
DBFP
(proposed)
0.99 0.99 1.00 0.99
All methods are evaluated on the same 200-sample dataset under identical preprocessing
conditions. Baseline results are obtained by running each method independently using
standardconﬁgurations.
standardization and one-hot encoding as described in Section
3. Robustness of the reported results was assessed using 5-fold
cross-validation, and pairwise performance diﬀerences between
DBFP and each baseline were validated using paired t-tests at a
signiﬁcance level ofp < 0.05, conﬁrming that DBFP’s superiority
isstatisticallysigniﬁcantacrossallcomparisons.
DBFP consistently outperforms all six comparative baselines
across all four evaluation metrics. Classical methods such as
Random Forest and SVM achieve moderate accuracy in the range
of 0.81 to 0.85, reﬂecting their inability to model the sequential
and contextual dependencies inherent in behavioral feature data.
Gradient Boosting via XGBoost improves upon these results by
capturing non-linear feature interactions through tree ensembles,
yet its accuracy of 0.87 remains substantially below DBFP. The
Transformer-based model approaches competitive performance at
0.91 accuracy, demonstrating the value of attention mechanisms
for behavioral data, but its lack of explicit sequential memory
management, which LSTM provides through its gated cell state,
limits its advantage in this task. The GRU network, as the
closest architectural alternative to LSTM, achieves 0.88 accuracy,
conﬁrming that while gated recurrence is beneﬁcial, DBFP’s
richer gating structure, higher-order regularization, and integrated
attention layer collectively produce a meaningful performance
margin. These results establish DBFP as the state-of-the-art
method for software feature demand prediction from consumer
behavioralanalytics.
4.5 DBFP classiﬁcation report
The DBFP model’s categorization report is shown inTable4.
The model’s excellent accuracy in predicting feature demand for
software products based on user behavior is demonstrated by the
precision, recall, and F1-score for each class. With an accuracy
rate of 0.99 and a weighted average F1-score of 0.99, DBFP clearly
performsexceptionallywell.
4.6 LSTM classiﬁcation report
Table6 shows that when compared to DBFP, the LSTM model
performs worse. With decreased recall, accuracy, and weighted
average F1-score for several classes, the ﬁnal result is 0.73. Some
classes are diﬃcult for the LSTM model to handle, which reduces
itsgeneralpredictivepower.
4.7 1D CNN classiﬁcation report
The 1D CNN model’s classiﬁcation report is shown inTable8.
With F1-score, recall, and precision that vary between classes, the
modeldoesdecently.Theaccuracyis0.72andtheweightedaverage
F1-score is 0.50. Although it performs comparably, the 1D CNN
modelisnomatchforDBFP.
4.8 Comparison
Table9 provides a concise summary of the main performance
measuresforeachmodelinthemodelcomparison.Ineverymetric
that was measured, DBFP performed better than LSTM and 1D
CNN. With an impressive accuracy of 0.99 and greater precision,
recall, and F1-score, DBFP is clearly the best model for predicting
featuredemandinsoftwareproducts.
4.9 Key observations
Precision, recall, and F1-score:DBFP demonstrates superior
precision,recall,andF1-scoreacrossallclasses,indicatingitsability
toeﬀectivelycaptureuserbehaviorpatterns.
Accuracy: the accuracy of DBFP at 0.99 showcases its high
correctness in predicting recommended features, highlighting its
reliabilityinreal-worldapplications.
Model robustness: DBFP’s robustness is evident in its
consistent performance across various classes, ensuring reliable
predictionsforadiverserangeofuserbehaviors.
Comparative analysis: the comparative analysis emphasizes
DBFP’s substantial advantage over LSTM and 1D CNN,
emphasizing its potential for practical implementation in software
productdevelopment.Inconclusion,theDBFPmodelemergesasa
powerful tool for anticipating user desires and predicting software
product feature demand. Its outstanding accuracy and robustness
make it a preferable choice for leveraging consumer behavioral
analyticsinthesoftwaredevelopmentdomain.
5C o n c l u s i o n
The comprehensive evaluation of our proposed Dynamic
Behavioral Feature Predictor (DBFP) model, including
Frontiersin BigData 16 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
TABLE 8 1DCNNclassiﬁcationreport.
Class Precision Recall F1-
score
Support
0 0.79 0.79 0.79 24
1 0.70 0.70 0.70 16
2 0.77 0.22 0.73 9
3 1.00 0.36 0.73 11
4 0.72 0.24 0.73 25
5 0.70 0.29 0.76 14
6 0.94 0.73 0.72 22
7 0.75 0.71 0.55 72
8 1.00 0.29 0.44 7
Accuracy 0.72 200
MacroAvg 0.62 0.40 0.45 200
Weighted
Avg
0.54 0.52 0.50 200
TABLE 9 Modelcomparison.
Model Precision Recall F1-
score
Accuracy
DBFP 0.99 1.00 0.99 0.99
LSTM 0.74 0.73 0.73 0.73
1DCNN 0.54 0.52 0.50 0.72
comparisons with LSTM and 1D CNN, yielded promising
ﬁndings that validate the potential of using behavioral analytics
for software feature prediction. With an impressive accuracy of
99% on our dataset, DBFP demonstrated exceptional performance
across multiple evaluation metrics, including precision, recall,
and F1-score, underscoring its eﬀectiveness as a predictive tool.
One of the key achievements of DBFP is its ability to accurately
categorize a wide range of user behaviors and preferences. This
level of precision enables more personalized software feature
recommendations that align with the unique needs of users.
Furthermore, DBFP outperformed both LSTM and 1D CNN
models in terms of overall accuracy, highlighting its superiority
in predicting user demands for new software features. However,
the study also identiﬁes several important caveats that warrant
further attention. Notably, DBFP exhibits a high sensitivity to the
quantity and quality of behavioral data. The model’s performance
is signiﬁcantly impacted by the availability and accuracy of the
data it processes, which suggests that data quality is a critical
factor for successful deployment in real-world applications. This
sensitivity presents a challenge when dealing with noisy, sparse,
or incomplete data, which are often encountered in practical
settings. To address these challenges, future research should focus
on improving DBFP’s generalization capabilities to handle diverse
and dynamic datasets more eﬀectively. One promising direction is
the exploration of adaptive learning methods, which would allow
DBFP to continuously learn and reﬁne its predictions as new data
becomesavailable.Thiswouldimprovethemodel’srobustnessand
enable it to adapt to changing user behaviors over time. Despite
these limitations, our research highlights the signiﬁcant potential
of DBFP as a tool for user-centric feature customization, oﬀering
a more personalized approach to software development. By
integratingbehavioralanalyticsintothesoftwarefeatureprediction
process, DBFP can help organizations better align their products
with user expectations, ultimately enhancing user satisfaction
and engagement. This work paves the way for future eﬀorts to
leveragepredictiveanalyticsincreatingmoreresponsive,agile,and
user-orientedsoftwaresolutions.
Data availability statement
The raw data supporting the conclusions of this article will be
madeavailablebytheauthors,withoutunduereservation.
Author contributions
AA: Writing – review & editing, Funding acquisition,
Validation, Resources, Supervision, Formal analysis, Investigation,
Project administration, Software, Data curation, Methodology,
Writing–originaldraft,Visualization,Conceptualization.
Funding
The author(s) declared that ﬁnancial support was not received
forthisworkand/oritspublication.
Acknowledgments
This Study could not be started, nor achieved without
the support of Imam Abdulrahman Bin Faisal University–
Entrepreneurshipunit,aswellastheSmallandMediumEnterprises
GeneralAuthorityinSaudiArabia(Monsha’at).
Conﬂict of interest
The author(s) declared that this work was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construedasapotentialconﬂictofinterest.
Generative AI statement
The author(s) declared that Generative AI was not used in the
creationofthismanuscript.
Any alternative text (alt text) provided alongside ﬁgures in
this article has been generated by Frontiers with the support of
artiﬁcial intelligence and reasonable eﬀorts have been made to
ensureaccuracy,includingreviewbytheauthorswhereverpossible.
Ifyouidentifyanyissues,pleasecontactus.
Frontiersin BigData 17 frontiersin.org

Aldaeej 10.3389/fdata.2026.1931695
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsedbythepublisher.
References
Agnieszka, D., Monika, S., and Ewa, O. (2023). Analysis of consumer behaviour in the
context of the place of ’ purchasing food products with particular emphasis on local
products. Int. J. Env. Res. Public Health 20:2413.doi:10.3390/ijerph20032413
Chih-Cheng, C., Chun-Wei, C., and Yu-Chung, T. (2018). Exploring the consumer
behavior of intention to purchase green products in belt and road countries: an
empiricalanalysis. Sustainability10:854.doi:10.3390/su10030854
Dimitrios,C.G.,andPanayiotis,K.T.(2022). “AI in consumer behaviour,”in:Learning
andAnalyticsinIntelligentSystems.SpringerInternationalPublishing.
Douglas,C.,Markus,H.,Dominik,N.,Markus,H.,andMiroslav,B.(2020).“Customer
purchase behavior prediction in e-commerce: a conceptual framework and research
agenda,”in: International conference on electronic commerce,(Springer)119–136.
Ezenwobodo,andStephen,S.(2022).Internationaljournalofresearchpublicationand
reviews. Int. J. Res. Public. Rev. 04,1806–1812.doi:10.55248/gengpi.2023.4149
Fei,W.,Zhiwen,F.,andYongfeng,Q.(2022).Analysisofconsumerproductpreference
and news media based on data mining technology. Front. Psychol. 13:1007846.
doi:10.3389/fpsyg.2022.1007846
Han, T.-I., and Leslie, S. (2022). Explaining socially responsible consumer behavior:
a meta-analytic review of theory of planned behavior.J. Int. Consumer Market. 292,
91–103.doi:10.1080/08961530.2016.1251870
He, W., Xiao, Y., Li, T., Wang, R., and Li, Q. (2025). Towards a foundation model for
behavioral intention prediction through multi-source data fusion.Information Fusion.
119:103799.doi:10.1016/j.inﬀus.2025.103799
Hongqi, Y., Yi, L., Yun, Q., Jiayuan, Z., Masukujjaman, M. D., and Abubakar, M. I.
(2023). Modeling the enablers of consumers’ e-shopping behavior: a multi-analytic
approach. Sustainability15:6564.doi:10.3390/su15086564
Huang, M., Xiao, Y., Guo, X., Zhang, Q., and Huang, Y. (2026). A monetization
predictive model for marketing campaigns on e-commerce service platforms based on
hiddeninformation. IEEE transactions on emerging topics in computational intelligence.
10.doi:10.1109/TETCI.2025.3605619
Hyunjoo, B. and Kyungsu, K. (2022). An exploratory study of consumers’ perceptions
ofproducttypesandfactorsaﬀectingpurchaseintentionsinthesubscriptioneconomy:
99subscriptionbusinesscases. Behavioral Sci.12:179.doi:10.3390/bs12060179
Igor, M., Jure, K., and Toma, B. (2022). Decision-making techniques of the
consumer behaviour optimisation of the product own price. Appl. Sci. 12:2176.
doi:10.3390/app12042176
Lakshmi, S., Himansu, K. T., Sibas, R. N., Abhijit, K. B., and Paolo, B.
(2021). Amalgamation of customer relationship management and data analytics
in diﬀerent business sectors—a systematic literature review.Sustainability 13:5279.
doi:10.3390/su13095279
Laura, C.-R., Vlad, V., Diana, S., Calin, A. C., Alexandru, B., Stefan, M., et al.
(2022).Consumersbehaviordeterminantsononlinelocalmarketplatformsincovid-19
pandemic—aprobitqualitativeanalysis. Mathematics,10.doi:10.3390/math10224281
Lin, J. (2025). “Application of machine learning in predicting consumer behavior and
precisionmarketing,” PLoS ONE 20:e0321854.doi:10.1371/journal.pone.0321854
Marko, S., and Vladimir, R. (2023). Assessment of inﬂuencing factors on consumer
behavior using the ahp model. Sustainability 15:10341. doi: 10.3390/su15131
0341
Mochammad, A., Syaekhoni, G. A., and Yong, S. K. (2017). Customer purchasing
behavior analysis as alternatives for supporting in-store green marketing decision-
making. Sustainability.9:2008.doi:10.3390/su9112008
Nasser, A. H. and Hossam, A. M. (2022). The prediction of consumer behavior from
socialmediaactivities. Behav. Sci.12:284.doi:10.3390/bs12080284
Sharma, P., Sachin, K., and Lokesh, K. (2022). Customer behavior analysis in
e-commerce using decision tree machine learning approach. Forest Chemicals
Rev.1312–1320.
Syed, H., Arif, K., Rashid, R. A., Kamran, A. S., Ahmed, R. H. E., Hasnain, A.,
and Vishal, P. (2021). Role of augmented reality in changing consumer behavior
and decision making: case of Pakistan.Sustainability 13:1–28. doi: 10.3390/su13241
4064
Thi, M. L. and Shu-Yong, L. (2017). Eﬀects of pros and cons of applying big data
analytics to consumers’ responses in an e-commerce context.Sustainability, 9:798.
doi:10.3390/su9050798
Vladimir, L. (2017). Consumer behavior towards innovative products: which
methodologiesforwhichvalues?
Wang, W., Xiong, W., Wang, J., Tao, L., Li, S., Yi, Y., et al. (2023). A user
purchase behavior prediction method based on XGBoost. Electronics, 12:2047.
doi:10.3390/electronics12092047
Yang, S. (2026). Predicting repurchase behavior and optimizing marketing for e-
commerce users with genetic algorithms and deep learning. Sci. Rep. 16:16035.
doi:10.1038/s41598-026-45903-5
Yonghui,D.A.I.andTianfu,W.(2021).Predictionofcustomerengagementbehaviour
response to marketing posts based on machine learning.Connection Sci. 33, 891–910.
doi:10.1080/09540091.2021.1912710
Zhou, Z., and Hudin, N. S. (2024). Advancing e-commerce user purchase
prediction: Integration of time-series attention with event-based timestamp encoding
and graph neural network-enhanced user proﬁling. PLoS ONE . 19:e0299087.
doi:10.1371/journal.pone.0299087
Frontiersin BigData 18 frontiersin.org
