---
title: 'Smart Profit-Aware Crop Advisory System: Kisan AI'
url: https://arxiv.org/abs/2605.00133
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Debasis Dwibedy
- Avyay Nishtala
- Pranathi Mukku
- D Snehaja
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.00133
pages: 13
chars: 25277
fetched_at: '2026-11-08T13:06:58+00:00'
kb_version: 1
---

# Smart Profit-Aware Crop Advisory System: Kisan AI

Smart Profit-Aware Crop Advisory System:
Kisan AI
Debasis Dwibedy 1,2, Avyay Nishtala1,3, Pranathi Mukku 1,4, and D. Snehaja 1,5
School of Computer Science and Engineering,
VIT-AP University, Amaravati, Andhra Pradesh, India
2d.dwibedy@vitap.ac.in
3avyay.22bce9292@vitapstudent.ac.in
4pranathi.22bce7816@vitapstudent.ac.in
5snehaja.22bce9458@vitapstudent.ac.in
Abstract.Modern crop advisory systems exhibit a critical limitation
termedeconomic blindness. These systems primarily optimize for bio-
logical yield, often overlooking market price, which can lead farmers
toward agronomically sound yet financially unviable decisions. In this
paper, we develop Kisan AI, a smart profit-aware crop advisory system
that resolves the above-mentioned limitation through a research-driven,
full-stack application. We train the Random Forest(RF) classifier model
on a nine-feature benchmark dataset, the standard seven agronomic at-
tributes augmented with amarket pricevariable, and evaluated against
eight baseline models, considering the evaluation matrices, such as, accu-
racy, precision, recall, F1-score, and Log Loss. The RF model achieves the
highest accuracy of 99.3% and the lowest Log Loss, confirming that the
inclusion of market price as a predictive feature is both valid and impact-
ful. We then implement the RF model within a multilingual progressive
Web App alongside a Facebook Prophet six-month price forecasting en-
gine and a MobileNetV2 disease detection module. A nine-language AI
chatbot powered by the Anthropic Claude API unifies all modules into
a single, mobile-installable platform accessible to farmers across India.
Keywords:Crop Recommendation, Market Price Forecasting, Random
Forest, Prophet, MobileNetV2, Precision Agriculture, Economic Blind-
ness
1 Introduction
Agricultural productivity has multi-dimensional aspects and thus needs integra-
tion of environmental as well as chemical data [8]. In practice, even when the
soil is ideal for a given crop, farmers may find that its market price has dropped
considerably by the time of harvest [1]. Current advisory systems might tell
the farmer what can grow well on their field, but not whether that crop will
bring any real return on investment [5]. This is the main challenge that preci-
sion and future agriculture face, i.e., to leverage available data and technology to
compute the biological yield, but more importantly, the potential profit for the
arXiv:2605.00133v1  [cs.LG]  30 Apr 2026

2 D. Dwibedy et al.
farmer [7]. Although several well-known systems and approaches use soil param-
eters as predictors of crop productivity [6], market factors also play a significant
role and, if overlooked, can substantially influence agricultural productivity and
decision-making [7]. Despite being scientifically sound, eco-friendly crop advisory
solutions may not always be economically viable for farmers [1]. Taken together,
these challenges highlight the need to move beyond traditional classification-only
approaches toward more holistic, integrated crop advisory systems [3].
Recent studies [2] [9] demonstrated the potential of ensemble learning for site-
specific agriculture. However, as highlighted by Kiran et al. [4], most current
systems remainmarket-blindproviding agronomic suggestions without consid-
ering the fluctuating economic value of the harvest. Although such systems are
able to predict the soil classification with high accuracy [6], they fall short in in-
corporating other multi-factor decision making dimensions in a modular fashion
[3]. The primary goal of our study is to tackle crop recommendation while uni-
fying both aspects of soil suitability and economic price volatility. In this paper,
we make an attempt to present a system for agricultural productivity prediction
using soil health parameters along with economic market forecasts.
Our Contributions:We make the following contributions in this paper:
–Addressing Economic Blindness:We augment standard agronomic features
with amarket pricevariable to train a profit-aware Random Forest recom-
mender.
–Comparative Study:We conduct a rigorous nine-model study (5 ML vs 4
DL), demonstrating that Random Forest achieves 99.3% accuracy and out-
performs deep learning architectures on structured data.
–Full-Stack Deployment:We deploy the validated system as Kisan AI, a Pro-
gressive Web App integrating Prophet forecasting, MobileNetV2 disease de-
tection, and a nine-language AI chatbot.
Organization:We organize the remaining sections of the paper as follows. In
Section 2, we present the basic terms, notations, definitions used throughout
the paper along with an overview of the state-of-the-art literature identifying
the research gaps. We formally define the problem statement in Section 3 along
with an illustration. In Section 4, we highlight the dataset used, our proposed
methodology, and the 3-tiered model architecture. We present our evaluated
results, system deployment, model outputs, and a comparative analysis with the
baseline models in Section 5. Section 6 concludes the paper.
2 Background Studies
2.1 Basic T erminologies, Notations, and Definitions
–Suitability Index (S):The potential of a crop to thrive based on levels of
Nitrogen (N), Phosphorus (P) and Potassium (K).
–Profitability Margin (P):The expected market value of a crop at the time of
harvest as predicted by time-series analysis.
–Multilingual Interface:A deployment strategy for digital accessible solutions
for farmers in different language speaking areas.

Smart Profit-Aware Crop Advisory System 3
2.2 Literature Survey
Doshi et al. [1] explored intelligent crop recommendation using a system called
AgroConsultant. They build a Naive Bayes model that achieves a 96% accuracy.
However, the authors did not consider real-time price APIs and mobile-accessible
deployment.
Jung et al. [3] researched deep learning-based plant disease detection. The au-
thors utilized the PlantVillage dataset to propose a MobileNetV2 architecture.
While results were strong for disease classification, the study did not include
crop recommendation and financial forecasting.
Motamedi et al. [6] evaluated the performance of fine-tuned SVMs for crop rec-
ommendations using soil and climate parameters. The best results were obtained
by the RF model with 100 trees, achieving an accuracy of 99.2%. However, the
authors did not consider the economic variables in the recommendation logic.
Senapaty et al. [7] presented a decision support system for Indian soil data using
NPK and soil type datasets. They developed an ensemble of RF and Extreme
Gradient Boosting (XGBoost) to classify and predict different soil types from
NPK values. The model achieves an accuracy of 98.5%. However, the authors
did not consider the detection and market forecasting modules in the proposed
ensemble model.
Kiran et al. [4] introduced a decision support system that uses a proprietary soil
database as well as Majority Voting of SVM and ANN techniques. This strategy
achieves a high accuracy of 97.2%. The authors considered the localized weather
data in order to predict climate trends, but they did not consider the crop’s
market price fluctuations. Additionally, the absence of multilingual support and
disease detection functionality limits the applicability of the proposed system.
Shinde et al. [9], however, have most recently proposed ensemble model for crop
recommendations and yield prediction. The combination of RF and XGBoost
models achieves a 98.1% accuracy as well as incorporation of Agmarknet datasets
for yield predictions. Nevertheless, their model was limited in its scope and could
only provide information pertaining to a single crop without a platform for its
implementation in real time.
Shastri et al. [8] used supervised machine learning approach to advance crop rec-
ommendation. The authors considered the Kaggle Crop Dataset and proposed
an ensemble of ANN, PBIL, and SHAP. The model achieves a result of 97.8%
accuracy. However, the findings lack real-world implementation in terms of inte-
gration with current market prices and physical implementation. Kumar et al.
[5] studied AI-smart agriculture using Agmarknet and NPK dataset. The au-
thors proposed an optimized Random Forest Classifier. The model achieves an
accuracy of 97% and featured a multilingual PW A deployment.
Gupta et al. [2] developed a crop recommendation system using Majority Voting
Ensemble of SVM, Naive Bayes, ANN, and RF models. Although, the ensemble
led to a very high accuracy of 98.5% for soil suitability, however, the model does
not consider the economic feasibility of the crops recommended. We develop the
Kisan AIapplication to fill this gap by including a profit prediction stage that
makes the crop advisory system economically feasible as well.

4 D. Dwibedy et al.
3 Problem Statement
We formulate a multi-objective problem in the crop advisory paradigm by incor-
porating economic feasibility alongside traditional biological feasibility. In this
study, we define the optimal crop setC ∗ as the candidate set that maximizes a
joint probabilistic measure of growth capability and market feasibility.
Weighted Probabilistic Framework:To quantify the crop selection decision based
on both growth capability and market feasibility, we adopt an integrated scor-
ing model in which each candidate crop is evaluated through a total weighted
probabilityP(C), defined as:
P(C) =w 1 ·P(yield|S) +w 2 ·P(profit|M) (1)
Where:
–P(yield|S) is the agronomic fitness probability generated by the classi-
fication model, representing the likelihood of successful growth given soil
parametersS(N, P, K, pH, Temperature, Humidity, and Rainfall).
–P(profit|M) is the economic viability score derived from the time-series
forecasting of market dataM.
–w 1 andw 2 are weighting coefficients set at 0.6 and 0.4, respectively, to bal-
ance biological necessity with financial gain.
Our objective is to optimize the total weighted probability function to minimize
log loss, while also supporting improved predictive accuracy.
3.1 Illustration of the Problem Statement
Necessity of the two-factors model can be best illustrated by considering its
comparative advantage compared to a conventional system of recommendations
based on a single variable. Table 1 presents an example when a more suitable soil-
wise crop is overshadowed by another choice because of its economic stability.
We can infer from the data provided that although being 13% less favorable
Table 1: Comparative Decision Logic: Traditional vs. Profit-Aware
Crop Candidate Suitability (P y) Economic Score (P p) Final Score Outcome
Crop A (e.g., Rice) 0.98 0.15 0.648 Rejected
Crop B (e.g., Maize) 0.85 0.800.830 Optimal
in terms of biological suitability,Crop Bis chosen as the optimal option. It
highlights the problem ofEconomic Blindnessand prevents the farmer from
planting perfect crops leading to bankruptcy due to oversupply.

Smart Profit-Aware Crop Advisory System 5
4 Our Proposed Methodology
4.1 Dataset(s) Description
We develop our research framework using a multi-modal data architecture com-
prising five specialized datasets that collectively capture the agronomic, eco-
nomic, and pathological parameters required for holistic agricultural decision
support. We summarize the structural attributes and feature sets of these datasets
in Table 2. We utilize the Crop Recommendation dataset 1, the Fertilizer Pre-
diction dataset 2, and the PlantVillage dataset 3. Additionally, we analyze the
market price trends using the official Agmarknet government records 4.
Table 2: Summary of Multi-Modal Datasets and Feature Sets
Module Records Classes Key F eatures
Benchmarking 2,200 22 CropsN, P, K, pH, T emp, Hum, Rain, P rice
Recommendation 2,200 22 CropsN, P, K, pH, T emp, Hum, Rain
Fertilizer 500 7 TypesN, P, K, Soil T ype, M oisture, T emp
Forecasting 3,100 11 CropsCrop, M onth, Y ear, P rice
Disease 16,500 16 Path.RGB P ixels, LeafGeometry
F eature Engineering and Benchmarking: TheCroprec with market price
dataset (N= 2,200) served as the main experimental corpus for benchmarking
models. This corpus includes seven environmental variables, Nitrogen (N), Phos-
phorus (P), Potassium (K), temperature, humidity,pH, and rainfall along with
the croplabeland price index. We establish a reference model using all nine
variables, based on which Random Forest emerges as the best-performing esti-
mator for the recommendation task.
Specialized Advisory Streams: From a deployment perspective, we organize
the overall data architecture into three distinct functional streams:
Agronomic Stream:We perform the growth suitability predictions using the
Crop recommendationdataset. Additionally, we use theFertilizer Prediction
dataset to train models based on soil nutrient concentrations (N, P, K), along
with temperature and moisture variables, to generate fertilizer recommenda-
tions.
Economic Stream:Themarket prices historicaldataset captures historical price
volatility for 11 crops using temporal features (month, year) along with price
attributes, and we use it to forecast future price trends.
Pathological Stream:Here, we use a sample of 16,500 images from thePlantVil-
lagedataset, transforming unstructured data into 16 different pathological classes
1 Crop Recommendation:https://www.kaggle.com/datasets/atharvaingle/
crop-recommendation-dataset/data
2 Fertilizer Prediction:https://www.kaggle.com/datasets/mohitsingh1804/
fertilizer-prediction-dataset
3 PlantVillage:https://www.tensorflow.org/datasets/catalog/plant_village
4 Agmarknet Gov Portal:https://agmarknet.gov.in/

6 D. Dwibedy et al.
based on specific crops (Potato, Tomato, and Pepper). We then use the modified
dataset to train the MobileNetV2 model using image pixel intensities and leaf
morphology as input features.
4.2 Proposed Methodology
Our proposed system architecture is implemented as a modular pipeline, pro-
gressing from raw data integration to a cloud-deployed advisory interface, as we
illustrate in Figure 1.
Fig. 1: Methodology Pipeline illustrating the transition from data integration to
system deployment.
Data Integration and Pre-processing: We develop a unified data pipeline by
integrating multiple secondary data sources to support comprehensive agronomic
analysis. We then perform feature scaling usingStandardScalerto normalize vari-
ations across the nine-dimensional feature vector. In parallel, the pathological
image dataset undergoes geometric transformations and color space augmenta-
tions to enhance invariance to environmental variations and improve the gener-
alization capability of the vision module.
Model Benchmarking and Selection: We select the final model through a detailed
benchmarking process involving five classical machine learning baselines and four
deep learning models. Although the high-capacity neural networks showed good
training performance,Random Forestemerged as the most reliable estimator
because of its higher F1-score and stronger resistance to overfitting under tabu-
lar agronomic constraints. Its ability to capture non-linear relationships between
soil chemistry and market-price volatility further supported its selection as the
core recommendation engine of our system.
Multi-Module Integration and Deployment: We develop the final architecture by
including three sub-systems: a Random Forest–based recommendation engine,
a transfer learning–basedMobileNetV2model for leaf disease detection, and an
FB Prophetmodel for economic forecasting. We unify these sub-systems through
aFastAPIback-end, which serves as a high-performance computation layer for
aProgressive Web App (PWA)interface. This deployment strategy enables the
integration of complex multi-modal intelligence into a lightweight and accessible
interface suitable for real-world applications.
4.3 Our Proposed 3-tiered System Architecture
We present our 3-tiered model architecture illustrating the flow between the
PW A Frontend, FastAPI Backend, and the multi-modal Intelligence tiers in Fig-
ure 2.

Smart Profit-Aware Crop Advisory System 7
Fig. 2: Three-tier System Architecture.

8 D. Dwibedy et al.
Tiered Infrastructure: TheFrontend Layeris a Progressive Web App (PW A)
consisting of a single-page application based on HTML5 and CSS3. It supports
service workers for offline operation. TheBackend Layercomprises an orchestra-
tion component constructed using the FastAPI framework, having eleven REST
endpoints. These endpoints take care of data routing and multilingual trans-
lations for chatbot in three regional languages. TheModels Layerforms the
intelligence part containing serialized AI sub-systems.
Crop Recommendation and Profit Scoring: To quantify profit-aware decision sup-
port, the system maps a nine-feature input vectorX= (N, P, K, pH, T, H, R, Mt)
to a ranked recommendation list. The ranking is governed by a composite profit
score (S):
S(C) =w 1 ·P(C|X soil) +w 2 ·G(M t, C),(2)
where,P(C|X soil) is the Random Forest posterior probability, whereasG(Mt, C)
refers to the normalized market price. Values ofw 1 andw 2 are empirically set
to 0.6 and 0.4 respectively.
Price Forecasting and Disease Detection: We consider the Facebook Prophet
model to address the problem of market fluctuations, where the price time-series
y(t) can be decomposed into:
y(t) =g(t) +s(t) +ϵ(t),(3)
where,g(t) denotes the trend, ands(t) presents seasonality. Additionally, the
disease detection mechanism employs MobileNetV2 architecture. In this case, the
1,280-dimensional feature vector is passed through Softmax to provide instant
diagnosis for 16 plant diseases.
Table 3: AI Model Specifications and Configurations
Module Algorithm F rameworkKey Configuration
Crop Recommendation Random Forest Scikit-learn 500 trees, sqrt features
Price Forecasting FB Prophet Prophet Yearly seasonality
Disease Detection MobileNetV2 TensorFlow Fine-tuned, 16 classes
Chatbot Claude API Anthropic 3 languages, fallback rules
5 Results and Discussion
5.1 Performance Evaluation of Recommendation Engine
We identify the best-performing model for the recommendation module through
an experimental evaluation of nine supervised learning algorithms. We assess
their performance considering standard evaluation metrics, such as, accuracy,
precision, recall, and F1-score.
Model Benchmarking:Following our performance evaluation results, as shown

Smart Profit-Aware Crop Advisory System 9
in Table 4, we select theRandom Forest (RF)as the best model for the cur-
rent system development, achieving the highest accuracy of 99.54%. Its strong
performance can be attributed to its ability to capture non-linear agronomic
interactions within the multi-modal dataset.
Table 4: Performance Comparison of Benchmarked Models
Model Accuracy Precision Recall F1-Score
Random F orest 0.9954 0.99 0.99 0.99
XGBoost 0.9912 0.99 0.99 0.99
Gaussian NB 0.9901 0.99 0.99 0.99
Decision Tree 0.9854 0.98 0.98 0.98
KNN 0.9745 0.97 0.97 0.97
Logistic Regression 0.9523 0.95 0.95 0.95
SVM 0.9120 0.91 0.91 0.91
Random Forest (OOB) 0.8950 0.89 0.89 0.89
Gradient Boosting 0.8810 0.88 0.88 0.88
Error Analysis and Feature Significance: The confusion matrix as shown in
Figure 3 validates the classification precision, while the feature importance analy-
sis as shown in Figure 4 illustrates the weight of specific environmental variables.
These metrics provide the empirical foundation for the deployment phase.
Fig. 3: Confusion Matrix for the Champion Random Forest Model

10 D. Dwibedy et al.
Fig. 4: Relative Feature Importance in Crop Suitability Prediction
5.2 System Deployment and Module Outputs: Kisan AI
We implement the RF model into a single unified web application calledKisan
AI. The introduction of Kisan AI allow us to effectively deploy the complex ma-
chine learning estimators into a usable form for the farmers.
User Authentication and Centralized Dashboard: Deployment of the application
requires user authentication and a centralized dashboard. We illustrate the dash-
board ofKisan AIin Figure 5. The dashboard contains three main intelligence
streams: Agronomy, Pathology, and Economics.
(a)
 (b)
Fig. 5: Kisan AI support features providing (a) Secure Authentication and, (b)
User Dashboard.
Agronomic Advisory Results: The Crop and Fertilizer modules implements
the RF model. Figure 6 shows the capacity of the model to take in soil com-
position data, including N-P-K content and soil pH level, and give specific crop
recommendations and further fertilization advice based on it.
Pathological Diagnosis and Economic Forecasting: The vision module, which
employs MobileNetV2, reached validation accuracy of 96.2% on 16 disease cat-
egories. Meanwhile, the FB Prophet model generates graphs of the future price
trends. In Figure 7, the output of these components is shown; it allows farmers

Smart Profit-Aware Crop Advisory System 11
(a)
 (b)
Fig. 6: Kisan AI support features providing (a) Crop Advisor and (b) Fertilizer
Advisor.
to identify crop leaf diseases through uploading a picture and understand the
future price fluctuations of 11 main crop types.
(a)
 (b)
Fig. 7: Kisan AI support features providing (a) Disease Detection and (b) Price
Trend Analysis.
Ancillary Support Features: To improve the robustness of the advisory sys-
tem,Kisan AIintegrates weather alerts and an AI-powered multilingual chatbot
to support farmer consultations. As illustrated in Figure 8, these components
complement the advisory service by delivering timely, context-aware, and scien-
tifically grounded recommendations across multiple languages.
5.3 Comparison with the Best-known Baselines
As demonstrated in Table 5, the proposed system Kisan AI is either comparable
or better than any other previously published results (99.3% on augmented data).
Nevertheless, accuracy is not enough to overcome real-life agricultural problems.
The majority of studies have two crucial weaknesses in common; first, the lack
of inclusion of economic factors like market price, and second, the inability of
deploying the systems. In contrast, the proposed Kisan AI system bridges these
gaps by utilizing both approaches at once.

12 D. Dwibedy et al.
(a)
 (b)
Fig. 8: Kisan AI support features providing (a) Weather Alerts and (b) AI Chat
Assistant support.
Table 5: Comparative Analysis of Kisan AI against the Baselines
Study / Y ear Model(s) Used Accuracy Market Price Deployed
Doshi et al. (2018) [1] Naive Bayes 96.0%× ×
Motamedi et al. (2023) [6] RF + SVM 99.2%× ×
Senapaty et al. (2024) [7] RF + XGBoost 98.5%× ×
Gupta et al. (2024) [2] Voting Ensemble 98.5%× ×
Kiran et al. (2024) [4] SVM + ANN 97.2%× ×
Shinde et al. (2025) [9] RF + XGB 98.1%✓×
Shastri et al. (2025) [8] ANN + SHAP 97.8%× ×
Kisan AI (Ours) RF + Prophet 99.3%✓ ✓
6 Conclusion and Future Scope
We developed the research-driven full-stack applicationKisan AI, a multi-modal
crop advisory system to help farmers making agricultural decisions. We selected
and implemented the RF model, which achieved 99.3% accuracy for crop predic-
tion, based on our experimental comparisons with state-of-the-art recommenda-
tion models. By using market price prediction through FB Prophet and pathol-
ogy detection through MobileNetV2, our Kisan AI application becomes holistic,
transcending the bounds of single-utility agronomic systems. We will extend the
current version of ourKisan AIapplication in the following directions in future.
–Multilingual Expansion:In order to overcome the gap in terms of digital lit-
eracy of the target audience, we will include the robust multilingual support.
–Transition to Open-Source APIs:In order to maintain long-term financial
stability of the system, it is planned to replace costly third-party APIs with
free versions provided either by governments or open sources.
–IoT Integration:We will include an IoT component that allows the system
to give dynamic predictions without any user inputs.

Smart Profit-Aware Crop Advisory System 13
References
1. Doshi Z, Nadkarni S, Agrawal R, Shah N. AgroConsultant: Intelligent crop recom-
mendation system using machine learning algorithms. In:IEEE ICCUBEA, 2018.
2. Gupta S, Sharma R, Jain P. Crop Recommendation System Using ML Algorithms.
In:IRJET Conference Proceedings, 2024.
3. Jung M, Song J S, Shin A Y. Construction of deep learning-based disease detection
model in plants.Scientific Reports, 2023.
4. Kiran P S, Reddy R, Rajak R K. A system for crop recommendation using SVM
and ANN majority voting technique.International Journal of Recent Technology
and Engineering, 8(211):1125-1130, 2024.
5. Kumar R, Singh A, Patel V. AI-based Smart Crop Recommendation System for
Sustainable Agriculture in India.Madras Agricultural Journal, 112(4):57-65, 2025.
6. Motamedi A, et al. Crop recommendation with fine-tuned SVM and Random Forest.
In:CEUR Workshop Proceedings, vol. 3992, 2023.
7. Senapaty M K, Ray A, Padhy N. Decision support system for crop recommendation
using machine learning classification algorithms.Agriculture14(8):1256, 2024.
8. Shastri S, Kumar S, Mansotra V. Advancing crop recommendation system with su-
pervised machine learning and explainable artificial intelligence.Scientific Reports,
15(25498), 2025.
9. Shinde A D, Patel M J, et al. Ensemble machine learning for crop recommendation
and yield prediction. In:ICCES Conference, 2025.
