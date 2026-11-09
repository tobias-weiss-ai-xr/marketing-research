---
title: Predicting Residential Rents in Dakar Using Machine Learning
url: https://arxiv.org/abs/2608.30865
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Amadou Tidiane Kassa Diallo
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.30865
pages: 19
chars: 40787
fetched_at: '2026-11-08T13:21:59+00:00'
kb_version: 1
---

# Predicting Residential Rents in Dakar Using Machine Learning

Predicting Residential Rents in Dakar Using
Machine Learning
Amadou Tidiane kassa Diallo
Dakar, Senegal
kassadiallo@gmail.com
1. Introduction
Dakar’s residential rental market is a particularly relevant field of study for analyzing the mech-
anisms of rent formation. Despite its economic and social importance, this market remains
relatively under-documented from a quantitative standpoint. The Dakar region had 4,004,426
inhabitants in 2023 according to the Agence nationale de la statistique et de la démographie
(ANSD). It thus concentrates a significant share of Senegal’s population within a relatively small
territory. This high demographic concentration is accompanied by strong housing demand and
a particularly developed rental market. According to ANSD data, 54.4% of households in Dakar
are renters, compared to 23.3% nationwide.
In this context, understanding and evaluating rents represents an important issue for households,
landlords, real estate professionals, and public authorities. However, Dakar’s rental market re-
mains characterized by relatively fragmented information. The prices available on real estate
platforms mainly correspond to asking prices rather than actually negotiated prices. Information
on completed transactions also remains difficult to access. This situation can create an infor-
mation asymmetry between the various market participants and make it difficult to objectively
assess the rental value of a property.
This issue can be studied through the hedonic pricing theory proposed by Rosen in 1974. Ac-
cording to this approach, the price of a real estate asset implicitly depends on its various charac-
teristics, such as surface area, location, number of bedrooms, and amenities. This theory has for
several decades constituted an important reference in the economic analysis of real estate mar-
kets and has been widely used in econometric models designed to explain variations in housing
prices.
Machine learning has progressively complemented these traditional approaches by making it pos-
sible to model nonlinear relationships and complex interactions between housing characteristics.
Random forests in particular have shown their value for real estate price prediction. Gradi-
ent boosting methods such as XGBoost and LightGBM have subsequently made it possible to
achieve high performance on tabular data. Several studies have thus demonstrated the value of
these methods for real estate price prediction, particularly in contexts where the relationships
between housing characteristics and their prices are difficult to represent with linear models.
The literature devoted to African real estate markets nevertheless remains relatively fragmented.
Studies based on the hedonic approach have notably been conducted in Lagos, with the work of
Abidoye in 2018, and in Kampala, with that of Irumba in 2015. Approaches based on machine
learning have also been applied more recently to various African real estate markets.
As in the short-term rental sector, the 2025 study by Samb devoted to the Greater Banjul
region constitutes a particularly relevant reference for the West African context. This study
1
arXiv:2608.30865v1  [cs.AI]  31 Aug 2026

compares several tree-based machine learning models and uses SHAP values to interpret model
predictions. This approach provides an interesting methodological framework for analyzing the
determinants of real estate prices in a regional context close to that of Dakar.
Despite these advances, Dakar’s long-term residential rental market remains little studied using
interpretable machine learning methods. To our knowledge, no study has so far proposed a
systematic analysis combining rent prediction, model optimization, SHAP interpretability, and
uncertainty quantification based on a corpus of Dakar real estate listings.
This article aims to address this gap by developing a complete pipeline for collecting, preparing,
modeling, and interpreting real estate data. The objective is not only to obtain a first dataset
on rentals in Dakar, but also to identify the main determinants of prices and to assess the
uncertainty associated with the predictions.
The main contributions of this study are as follows
•The construction of an original dataset of 1,507 rental listings in Dakar, obtained through
systematic scraping and subjected to a documented cleaning and normalization pipeline
•The optimization of the XGBoost and LightGBM models through Bayesian search with Op-
tuna, in order to identify the configurations offering the best predictive performance
•A comparative analysis of feature importance based on XGBoost gain and SHAP values, in
order to study the main determinants of rents
•A quantification of predictive uncertainty via quantile regression, allowing predictions to be
complemented with prediction intervals and their calibration to be assessed
This approach thus aims to combine predictive performance, interpretability, and uncertainty
quantification, while taking into account the specificities and limitations of the data available
on Dakar’s residential rental market.
2. Literature Review
We first briefly present the four families of algorithms evaluated in this study, as well as the two
interpretability approaches selected, before detailing the complete methodology in the following
section.
2.1 Linear Regression
Linear regression estimated by the ordinary least squares method constitutes the reference model
of this study. It relies on the assumption of a linear relationship between the explanatory
variables and the target variable. This model thus provides a benchmark for evaluating the
performance gain brought by approaches capable of modeling nonlinear relationships.
2.2 Random Forest
Random Forest is an ensemble learning method based on the construction of a large number of
decision trees. Each tree is trained on a bootstrap sample of the data and, at each step, uses a
random subset of the explanatory variables. The individual tree predictions are then aggregated
by averaging in the case of regression.
This dual source of randomization helps reduce the model’s variance and limit the overfitting
associated with a single decision tree considered in isolation. Direct interpretation of the results
is less straightforward than in the case of linear regression.
2

2.3 XGBoost (Extreme Gradient Boosting)
XGBoost is a gradient boosting method that builds trees sequentially. Each new tree aims to
correct the residual errors produced by the previously built trees. Learning is thus based on
gradient descent applied to a regularized loss function. When building the trees, the choice of
splits is notably based on the gain, which corresponds to the local reduction in the loss function
induced by a split.
2.4 LightGBM
LightGBM is an implementation of gradient boosting designed to improve computational effi-
ciency and reduce memory usage. Unlike methods that grow trees level by level, LightGBM
favors leaf-wise growth, which generally makes it possible to achieve good performance with
reduced training time. The model also relies on the discretization of numerical variables using
histograms in order to speed up the search for the best splits. It also offers native handling of cat-
egorical variables, with training times generally shorter than those of XGBoost for comparable
data volumes.
2.5 Interpretability
Two complementary approaches are used to interpret the tree-based models: gain-based impor-
tance and SHAP values.
Gain-based importance is a measure directly provided by tree-based models. For each variable,
it evaluates the average reduction in the loss function associated with the splits in which that
variable is involved. The values are then normalized so that their sum corresponds to 100%
across all variables. This measure has the advantage of being fast to compute, but it reflects an
average importance at the level of splits rather than a cumulative impact on predictions. Thus,
a boolean variable used in a limited number of particularly decisive splits can obtain a high
importance, whereas a continuous variable used frequently but with a smaller individual effect
may appear less important (see §4.7).
SHAP (SHapley Additive exPlanations) values, for their part, are based on Shapley values from
cooperative game theory. They make it possible to attribute to each variable, for each observa-
tion, a specific contribution to the difference between the model’s prediction and its reference
value. For tree-based models, the TreeSHAP algorithm makes it possible to compute these con-
tributions exactly and efficiently. An essential property of SHAP values is their local additivity.
For each observation, the sum of the contributions of all variables corresponds exactly to the
gap between the individual prediction and the model’s reference prediction. This property dis-
tinguishes SHAP values from global importance measures such as gain-based importance, which
do not make it possible to directly identify the contribution of each variable to an individual
prediction.
3. Materials and Methods
3.1 Study Area
Dakar is the capital of Senegal. It is located on the Cap Vert peninsula, at the western tip of
Senegal. It constitutes the country’s main economic and administrative hub and experiences
strong pressure on land and rental prices, particularly in coastal areas and the main business
districts such as Almadies, Ngor, Ouakam, Point E, and Dakar Plateau.
The corpus covers 24 localities, ranging from upscale residential areas such as Almadies, Ngor,
and the Corniche to more working-class or peripheral neighborhoods such as Parcelles Assainies,
3

Grand Yoff, Guédiawaye, and Keur Massar.
3.2 Dataset
Data were collected through automated scraping of online real estate listing platforms between
January 2024 and June 2025. The collection focuses on residential properties for rent in the
Dakar region.
The initial collection comprises 1,654 listings and 36 variables. A seven-step preprocessing
procedure was then applied in order to obtain a homogeneous dataset.
•Filtering listings by locality
•Removing listings without a valid rental price
•Restricting to properties intended for residential rental
•Normalizing housing types into six categories: F2, F3, F4, F5, F6, and Studio
•Excluding short-term rentals
•Standardizing more than 130 locality labels into 24 geographic categories
•Handling outliers, missing values, and redundant variables
3.3 Feature Engineering
Four derived variables were created in order to enrich the information available in the raw data.
•luxury_scoreis a synthetic score based on seven attributes associated with the upscale
character of the property. It takes into account the swimming pool, sea view, penthouse,
standing, elevator, garage, and air conditioning.
•nbre_chambre 2 is a quadratic term used to capture a possible nonlinear relationship be-
tween the number of bedrooms and the rent level.
•ratio_sdb_chcorresponds to the ratio between the number of bathrooms and the number
of bedrooms. It serves as a proxy variable for the property’s comfort level.
•kw_scoreis a weighted score built from 18 keywords associated with the premium posi-
tioning of properties. Each term is given a weight according to its indicative power. The
terms "corniche" and "haut standing" are for example weighted at 3, while "piscine" receives
a weight of 2 and "meublé" a weight of 1.
Following preprocessing and feature engineering, the final dataset comprises1,507 listings
and 33 variables. The structure and nature of the main variables retained are presented in
the following table.
4

Variable Description Type
price Monthly rent requested (FCFA) — target variable int
location Dakar locality (24 canonical values) categorical
type_appartement Normalized type: F2, F3, F4, F5, F6, Studio categorical
surface Living area (m2) float
nbre_chambre Number of bedrooms int
nbre_salle_de_bain Number of bathrooms int
etage Floor (0 = ground floor) int
luxury_score Weighted sum of 7 premium attributes int
kw_score Premium keyword score extracted from the description
(derived)
int
nbre_chambre2 the square of the number of bedrooms int
23 boolean columns Amenities: elevator, swimming pool, parking, air con-
ditioning, sea view, standing, furnished, etc.
bool
Table 1: Description of dataset variables
3.4 Methodological Pipeline
The methodological approach comprises five main steps: data preparation, feature engineering,
preprocessor setup, model training and optimization, and finally their evaluation and interpre-
tation. The whole is structured within a coherent pipeline presented in the figure below.
Collection
& cleaning
(1 654→1 507)
Feature
engineering
(luxury,
kw_score...)
Leak-free
preprocessor
(KFold Tar-
get Enc.)
Training
LR•RF•
XGB•LGBM
Bayesian
optimization
(Optuna,
100 trials)
Evaluation
MAE•
RMSE•R 2
(5-fold CV)
Interpretability
XGBoost
Gain + SHAP
Quantile
regression
[q10 - q50 - q90]
Figure 1: pipeline diagram
3.5 Leak-Free KFold Target Encoding
The target variable exhibits strong right skewness, with a skewness coefficient of 1.55. A loga-
rithmic transformation is therefore applied according to the relation
y= log(1 +price)(1)
Predictions are then converted back to the original scale using the inverse transformation
[price= exp(ˆy)−1(2)
The33explanatoryvariablesaredividedintofourblocksprocessedwithinascikit-learnColumnTransformer.
•Numerical blockcomposed of 8 variables. Missing values are replaced with the median,
and the variables are then standardized usingStandardScaler
•Categorical blockcorresponding to thetype_appartementvariable. Missing values are
replaced with the most frequent category, and the variable is then transformed via One-Hot
Encoding
•Location blockprocessed via KFold Target Encoding in order to incorporate neighborhood-
related information while avoiding data leakage
5

•Boolean blockgrouping the 23 amenities. Missing values are replaced with the most fre-
quent category
A naive target encoding consists of computing, for each locality, a price statistic based on the
entire set of observations before splitting the data into training and test sets. This practice
introduces data leakage and can lead to an overestimation of performance.
To avoid this bias, aKFoldTargetEncoder, implemented as a scikit-learn transformer, was used.
During training, the encoding is computed solely from the observations available in the training
set
enc(neighborhoodk) = median{yi :neighborhood i =k, i∈train}(3)
When a locality is absent from the training set and appears in the test data, the overall median
of the training set is used. This procedure ensures a strict separation between the training and
test data and thus limits the risk of information leakage.
3.6 Models and Hyperparameter Optimization
Five modeling approaches were compared. Linear regression serves as the reference model. It
is compared to a Random Forest configured with 300 trees, a maximum depth of 20, and a
minimum of 2 observations per leaf. A baseline XGBoost is also used with 1,000 estimators, a
learning rate of 0.03, and a maximum depth of 6. Finally, optimized versions of XGBoost and
LightGBM are trained.
The hyperparameters of the optimized models are determined through Bayesian optimization
with Optuna using the Tree-structured Parzen Estimator algorithm. The search space comprises
8 to 9 hyperparameters, covering notably the number of trees, the learning rate, the maximum
depth, the observation and feature subsampling rates, as well as the L1 and L2 regularizations
and the minimum weight associated with a leaf.
3.7 Evaluation Metrics
Performance is evaluated using three main metrics: MAE, RMSE, and the coefficient of deter-
mination R2. The metrics are computed after inverse transformation of the predictions in order
to preserve the original price scale in FCFA.
M AE= 1 n ∑ |ˆyi−y i|(4)
RM SE=
√
1
n
∑
(ˆyi−y i)2 (5)
R2 = 1−
∑(ˆyi−y i)2 ∑(yi−¯y)2 (6)
wherenrepresents the number of observations,y i the actual value,ˆyi the predicted value, and
¯ythe mean of the observed values.
The main protocol relies on an 80%/20% split of the data for training and testing. A 5-fold
cross-validation complements this evaluation in order to examine the robustness and stability of
the performance obtained, as presented in Section 4.6.
6

3.8 Model Interpretability
Two complementary approaches are applied to the optimized XGBoost model, retained as the
best model. The first relies on the native gain-based importance, computed from the average
reduction in the loss function brought about by the different variables in the trees. The second
uses SHAP values computed on the test set.
SHAP values allow for a global interpretation based on the mean of the absolute values per vari-
able, as well as a local interpretation through the decomposition of each variable’s contributions
to an individual prediction. The comparison of these two approaches is presented in Section 4.7.
3.9 Quantile Regression
Three additional XGBoost models are trained with thereg:quantileerrorobjective for the
0.10, 0.50, and 0.90 quantiles. The optimal hyperparameters identified in Section 3.6 are re-
tained.
The interval between q10 and q90 targets a nominal coverage of 80% on the test set. This ap-
proach makes it possible to associate an estimate of predictive uncertainty with each prediction.
3.10 Software Environment
The entire pipeline is developed in Python 3.12.3 with pandas 3.0.3, numpy 2.4.6, scikit-learn
1.9.0, XGBoost 3.3.0, LightGBM 4.6.0, Optuna 4.9.0, and SHAP 0.52.0 on a Linux environment.
The complete code, as well as the Jupyter notebook documenting the various steps of the
pipeline, are available upon request from the author.
4. Results and Analysis
4.1 Dataset Overview
The final dataset comprises 1,507 real estate listings spread across 24 localities. The median
monthly rent is 700,000 FCFA, compared to a mean of 950,411 FCFA, with a standard deviation
of 796,534 FCFA. The median living area is 189 m2, and the median number of bedrooms is 3.
The majority of properties are of type F4, accounting for 53.4% of listings, followed by F3 at
23.6%.
The geographic distribution remains concentrated in a few neighborhoods. The most represented
are Almadies with 19.5% of listings, followed by Ouakam with 11.9%, followed by Mermoz with
10.4%, followed by Point E with 7.2%, and Fann with 6.6%. These five neighborhoods alone
account for 55.6% of the corpus.
7

Figure 2: median rental price by locality (Dakar neighborhood)
This geographic concentration represents an imbalance to be taken into account when interpret-
ing the results, particularly when analyzing model performance by neighborhood, as presented
in Section 5.4.
4.2 Price Distribution
The distribution of rents exhibits strong right skewness, with a skewness coefficient of 1.55.
The majority of listings fall between 300,000 and 1,300,000 FCFA per month, while a long tail
comprises upscale properties whose rents can exceed 2,000,000 FCFA.
In order to limit the influence of extreme values, a logarithmic transformation of the target
variable according to the relationlog(1 +price)was applied before training the models. This
transformation reduces the dispersion of high values and produces a more balanced distribution,
as shown in the figure below.
Figure 3: logarithmic transformation of price
8

4.3 Spatial Structure of Prices and Correlations
The figure below presents the correlation matrix between the main numerical variables. The
strongest correlations with price concern the number of bedrooms, the surface area, and the
luxury_score. These results are consistent with the hedonic approach, according to which
property characteristics contribute to rent formation.
However, these relationships, taken individually, do not fully explain the variations observed in
rents. This limitation justifies the use of models capable of accounting for nonlinear relationships
and interactions between the different characteristics of properties.
Figure 4: correlation matrix
4.4 Comparative Model Evaluation
The table below gathers the performance of the five models on the test set, evaluated after
inverse transformation to the FCFA scale.
Model MAE (FCFA) RMSE (FCFA) R2
Linear Regression 257147 470262 0.679
Random Forest 222201 363525 0.808
XGBoost baseline 221405 350685 0.821
XGBoost tuned (Optuna) 210902 324195 0.847
LightGBM tuned (Optuna) 215259 329978 0.842
Table 2: Comparative performance on the test set
The XGBoost model optimized with Optuna achieves the best performance, with an R2 of
0.847, closely followed by the optimized LightGBM with an R2 of 0.842. The gap of 16.8 R2
points between linear regression, which reaches 0.679, and XGBoost highlights the importance
9

of nonlinear relationships in determining rents in Dakar. These results show the value of ma-
chine learning models in capturing the interactions and complex effects between the various
characteristics of properties.
4.5 Prediction Accuracy
Figure 5: Actual vs. predicted price on the test set
Linearregressionshowsgreaterdispersionaroundthediagonal, particularlyforhigherrents. The
optimized XGBoost and LightGBM models produce a tighter cluster of points. A significant
residual dispersion is nevertheless still observed for certain upscale properties whose rent exceeds
2,000,000 FCFA.
4.6 Cross-Validation and Robustness
A 5-fold cross-validation was carried out in order to assess the stability of performance beyond
the single 80/20 split. Table 3 presents the mean R2 and its standard deviation, computed on
thelog(1 +price)scale used for training the models.
10

Model Mean R2 (log) R2 Std. Dev. Mean RMSE (log)
Linear Regression 0.814 0.013 0.350
Random Forest 0.832 0.021 0.331
XGBoost baseline 0.839 0.015 0.325
XGBoost tuned 0.852 0.011 0.312
LightGBM tuned 0.851 0.013 0.312
Table 3: 5-fold cross-validation
The results obtained on the logarithmic scale during cross-validation confirm the performance
observed on the single split. The optimized XGBoost and LightGBM models achieve the best
results, with a mean R2 of approximately 0.852.
In order to more precisely assess the robustness of the retained model, optimized XGBoost,
a second 5-fold cross-validation was carried out directly on the original price scale in FCFA,
after inverse transformation. This approach makes it possible to express performance in directly
interpretable monetary units and to obtain a more concrete measure of prediction error.
Figure 6: Distribution of residuals by fold
This check reveals a gap between the performance obtained via cross-validation and that pre-
sented in Section 4.4. The mean R2 reaches0.782, with a standard deviation of0.034and a
range between0.750 and 0.848, compared to 0.847 for the single 80/20 split. The mean RMSE
stands at369,744 FCFA, with a standard deviation of26,230 FCFA, compared to 324,195
FCFA for the single split.
The single split should be interpreted with caution and complemented by cross-validation in
order to assess the robustness and stability of the model.
11

4.7 Feature Importance According to XGBoost Gain
The analysis of feature importance according to XGBoost’s native metric, based on the average
gain per split, highlights several variables strongly associated with the model’s predictions. The
mainonesareluxury_scorewith23.7%ofthetotalgain, followedbynbre_chambrewith14.4%,
nbre_chambre_sqwith 12.3%,vue_merwith 7.7%,kw_scorewith 7.3%,location_encoded
with 3.4%, andparkingwith 2.9%.
The 23 binary variables corresponding to amenities collectively account for 28% of the total
gain. This substantial contribution should nevertheless be interpreted with caution, as some
variables may be correlated or provide similar information to the model.
The comparison with SHAP values presented in the following section makes it possible to com-
plement this analysis and to better assess the actual influence of the different variables on the
predictions.
Figure 7: Feature importance by gain
4.8 Interpretability via SHAP Values
In order to more precisely analyze the influence of variables on the model’s predictions, SHAP
values were computed on the test set.
The model’s base value, corresponding to the mean predicted log price, is13.44, or approxi-
mately686,870 FCFAafter conversion back to the price scale.
As shown in Figure 8, the ranking based on the mean of the absolute SHAP values highlights
the most influential variables. The six main ones areluxury_scorewith 0.163, followed by
location_encodedwith 0.155,kw_scorewith 0.132,surfacewith 0.107,nbre_chambrewith
0.075, andvue_merwith 0.072.
12

Figure 8: SHAP summary plot
Figure 9: Mean SHAP importance (|SHAP value|)
Unlike XGBoost’s native importance presented in Section 4.7, SHAP values make it possible to
assess the contribution of each variable to individual predictions. They thus offer a complemen-
tary interpretation of feature importance and make it possible to better understand their actual
influence on the model’s predictions.
The scatter plot of the summary plot (Figure 8) confirms, for the top six features, a monotoni-
cally increasing relationship between the feature value (color) and its SHAP impact (horizontal
position). Pearson correlation coefficients between feature value and the associated SHAP value
13

exceed 0.90 forlocation_encoded,luxury_score,kw_score,surface,nbre_chambre, and
vue_mer(Table 4).
Feature Correlation (value, SHAP)
location_encoded 0.932
luxury_score 0.897
kw_score 0.952
surface 0.920
nbre_chambre 0.910
vue_mer 0.993
Table 4: Correlation between feature value and its associated SHAP value
Divergence Between Gain and SHAP Values: The Case of Location
The interpretability analysis reveals a significant difference in the ranking oflocation_encoded
depending on the measure used. With XGBoost gain-based importance, this variable occupies
the 6th position with 3.4% of the total gain. With the mean of the absolute SHAP values, it
ranks 2nd, behindluxury_score.
Thisdifferencedoesnotreflectmodelinstabilitybutratherresultsfromthecalculationprinciples
specific to the two measures. XGBoost gain evaluates the average reduction in the loss function
brought about by a split, and thus does not directly measure a variable’s overall impact on the
full set of predictions. Sincelocation_encodedis a continuous variable resulting from a KFold
encoding of location, it can appear in many splits at different thresholds. Each split may then
bring a relatively small improvement. Conversely, a binary variable such asvue_meroffers fewer
splitting possibilities. When it is used for a split, that split can be highly discriminative and
produce a high average gain despite less frequent use.
SHAP values take a different approach by measuring each variable’s contribution to individual
predictions and then aggregating these contributions across all observations. They thus make
it possible to better represent the actual influence of variables on the model’s predictions. The
resulting ranking confirms that location constitutes one of the main determinants of rents in
Dakar. This result is consistent with the hedonic approach and with the results presented in
Figure 4 and the correlation Table 2 in Section 4.3.
This difference also holds methodological interest. When location is represented by a single
continuous variable derived from target encoding, its importance may be underestimated by the
gain measure in tree-based models. The use of SHAP values as a complement to XGBoost’s
native importance therefore appears relevant for obtaining a more complete interpretation of
the variables.
Local Explanation via Waterfall Decomposition
SHAP values make it possible to explain each individual prediction thanks to their additivity
property. A prediction can thus be decomposed starting from the model’s base value and then
completed by the contribution of each variable.
For a listing whose predicted price deviates from the average market level, this decomposition
makes it possible to identify the characteristics that explain this gap. It can notably highlight
the influence of location, surface area, number of bedrooms, and amenities.
This approach provides a detailed and verifiable interpretation of individual predictions. An
example is presented in the accompanying notebook in the form of a waterfall chart.
14

SHAP Waterfall — decomposition of the prediction for a listing
4.9 Prediction Intervals via Quantile Regression
In order to quantify the uncertainty associated with the predictions, three additional XGBoost
modelscorrespondingtotheq10, q50, andq90quantilesweretrainedwiththereg:quantileerror
objective and the optimal hyperparameters defined in Section 3.6.
The q10 and q90 quantiles define a prediction interval targeting a nominal coverage of 80% of
observations. The q50 quantile corresponds to the median rent estimate.
This method thus makes it possible to complement the point prediction with an uncertainty
estimate and to assess the possible dispersion of rents around the predicted value.
Quantile Regression — CI [q10–q90]
Theempirical coverage rateobtained on the test set is64.2%, which remains well below
15

thetargeted nominal coverage of 80%. Themedian width of the prediction intervals
reaches376,376 FCFA.
This undercoverage indicates that the intervals produced by the quantile models are not yet
properly calibrated. For a significant proportion of listings, the lower bound q10 is too high, as
is the upper bound q90, which is too low. The resulting intervals are thus too narrow relative
to the actual variability of rents.
5. Discussion
5.1 Interpretation of Performance
The R2 of 0.847 obtained with the optimized XGBoost model on the single split shows that
the characteristics extracted from real estate platforms contain significant information about
rent variation in Dakar. This performance remains close to that obtained in other real estate
contexts, while being slightly below certain benchmark results.
Truong et al. (2020) notably obtain an R2 of 0.88 on an Australian corpus of more than 20,000
transactions. Their study benefits from detailed geospatial variables such as distance to schools,
transportation, and green spaces. This information is not available in our corpus. The gap of 3
to 4 R2 points can therefore be partly explained by the smaller size of our sample, with 1,507
observations, and by the absence of precise geographic coordinates.
Despite these limitations, the results show that the variables available in real estate listings
make it possible to capture a significant share of the rent variation observed in Dakar.
5.2 Gain and SHAP: Methodological Implications
The difference observed between XGBoost gain-based importance and that obtained with SHAP
valuesconstitutesanimportantmethodologicalfindingofthisstudy. Therankingoflocation_encoded
varies significantly depending on the measure used. This variable occupies a relatively low po-
sition according to gain, whereas it ranks among the most influential variables according to
SHAP.
This divergence shows that the choice of interpretability method can significantly alter the
analysis of real estate price determinants. In our case, it notably changes the relative importance
attributed to location compared to the property’s characteristics.
For hedonic studies using ensemble models and target encoding, these results demonstrate the
value of not relying on a single importance measure. Combining XGBoost gain and SHAP values
allows for a more comprehensive analysis and limits the risk of conclusions based on a single
metric.
5.3 Selection Bias and Price Negotiability
The corpus likely presents an overrepresentation of upscale properties and listings marketed
on online real estate platforms. Part of Dakar’s rental market, particularly properties offered
through informal networks or without online publication, remains absent from the data.
The results must therefore be interpreted within the limits of the observed distribution and
cannot be directly generalized to the entire Dakar rental market.
Another limitation concerns the nature of the prices used. The data correspond toasking
pricesrather thanactually negotiated prices. Since negotiation between landlords and
tenants is common, the rents ultimately agreed upon may differ from the amounts displayed.
16

Thisdifferencecanintroduceanupwardbiasinthedatausedtotrainthemodel. Thepredictions
should thus be interpreted as estimates of the asking price level rather than as a direct measure
of the rent actually paid.
5.4 Robustness and Limitations of the Corpus
The concentration of observations in certain Dakar localities also constitutes a limitation for
interpreting performance across geographic areas. The most represented neighborhoods have
a larger volume of observations, while less represented areas in the corpus may be less well
represented by the model.
This unbalanced distribution may limit the model’s ability to generalize its predictions in neigh-
borhoods with few observations. A broader and more geographically balanced data collection
would improve the representativeness of the corpus and allow for a more precise assessment of
performance differences between neighborhoods.
5.5 Imperfect Calibration of Prediction Intervals
The empirical coverage rate of 64.2% obtained in Section 4.9 remains well below the nominal
coverage of 80%. This result constitutes an important limitation for the use of the prediction
intervals.
Several factors may explain this undercoverage. The size of the test set, with 302 observations,
first limits the precision of the coverage estimate. XGBoost’sreg:quantileerrorobjective can
also be sensitive to hyperparameter choices.
The heterogeneity of Dakar’s rental market can also complicate the estimation of extreme quan-
tiles. Properties with similar characteristics may indeed display very different rent levels de-
pending on their standing or environment.
The resulting intervals should therefore not be considered perfectly calibrated for operational
use. Future work could notably focus on hyperparameter optimization specific to each quantile
and on post-hoc recalibration using methods such asconformal prediction. These approaches
could improve coverage while maintaining sufficiently precise intervals.
6. Conclusion
This study proposes an interpretable machine learning approach for predicting residential rents
in Dakar. Starting from 1,654 raw listings, a rigorous preprocessing procedure made it possible
to build a final corpus of 1,507 observations.
The XGBoost model optimized with Optuna achieves the best performance on the single split,
with an R2 of 0.847, an MAE of 210,902 FCFA, and an RMSE of 324,195 FCFA.
The SHAP analysis furthermore shows that location constitutes one of the main determinants
of rents in Dakar and reveals significant differences from the importance computed via XGBoost
gain. These results underscore the value of combining several interpretability methods.
Finally, the intervals obtained via quantile regression show a coverage of 64.2% against a target
of 80%. Recalibration therefore remains necessary before any operational use.
Implications for Housing Policy
The rent differences observed between neighborhoods highlight the potential value of a predictive
model for tracking market pressures and contributing to urban planning and affordable housing
policies.
17

The main limitation remains the absence of data on actually negotiated rents. Establishing a
structured system for collecting rental transaction data would improve the quality of available
data and strengthen the tools available for analyzing Dakar’s real estate market.
Limitations and Perspectives
This study remains limited by the availability of online listings, the use of asking prices, the
absence of precise geographic coordinates, and the uneven geographic coverage of the corpus.
The prediction intervals also require recalibration.
Future work could incorporate more geospatial and temporal data, broaden data collection to
different sources, and use actual transaction prices. Recalibration via conformal prediction could
also improve the reliability of the prediction intervals.
Perspectives
Several avenues could extend this work. Continuous data collection would make it possible to
build a larger corpus and to better track market developments over time.
Adding precise geospatial variables such as distances to urban centers, transportation, beaches,
and services would also help to better measure the effect of location.
Recalibrating the prediction intervals, notably usingconformal predictionmethods, constitutes
another priority for improving their reliability.
In the longer term, the creation of a national registry of rental transactions would make it
possible to use actually negotiated rents and to develop models more representative of Senegal’s
real estate market.
Declaration
Funding: this research received no external funding.
Conflicts of interest: no conflicts of interest declared.
Data and code availability: the dataset (dataset.csv, CC BY 4.0 license) and the complete
notebook documenting the entire pipeline are available upon request from the author.
References
ANSD: Population datahttps://www.ansd.sn/Indicateur/donnees-de-population
PressAfrik ANSD Study: Dakar, capital of rentershttps://www.pressafrik.com/
Etude-de-l-Ansd-Dakar-capitale-des-locataires_a219825.html
Cybergeo Article on the real estate market in Dakar
https://journals.openedition.org/cybergeo/26146
Abidoye, R. B., & Chan, A. P. C. (2018). Hedonic valuation of real estate properties in
Nigeria.Journal of African Real Estate Research, 3(1), 122–140.
https://pdfs.semanticscholar.org/9dd3/ef8baea1541e7438928532ebd498c89ffa88.pdf
Chau, K. W., & Chin, T. L. (2003). A critical review of literature on the hedonic price model.
International Journal for Housing Science and Its Applications, 27(2), 145–165.
https://ssrn.com/abstract=2073594
18

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. InProceedings of
the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining
(pp. 785–794). ACM.https://doi.org/10.1145/2939672.2939785
Chica-Olmo, J., González-Morales, J. G., & Zafra-Gómez, J. L. (2020). Effects of location on
Airbnb apartment pricing in Málaga.Tourism Management, 77, 103981.
https://doi.org/10.1016/j.tourman.2019.103981
Irumba, R. (2015). An empirical examination of the effects of land tenure on housing values in
Kampala, Uganda.International Journal of Housing Markets and Analysis, 8(3), 359–374.
https://doi.org/10.1108/IJHMA-11-2014-0044
Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., & Liu, T.-Y. (2017).
LightGBM: A highly efficient gradient boosting decision tree. InAdvances in Neural
Information Processing Systems, 30.https://proceedings.neurips.cc/paper/2017/hash/
6449f44a102fde848669bdd9eb6b76fa-Abstract.html
Limsombunchai, V. (2004). House price prediction: Hedonic price model vs. artificial neural
network. InProceedings of the New Zealand Agricultural and Resource Economics Society
Conference.
Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. In
Advances in Neural Information Processing Systems, 30, 4765–4774.https://papers.
neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html
Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M., Nair, B., Katz, R.,
Himmelfarb, J., Bansal, N., & Lee, S.-I. (2020). From local explanations to global
understanding with explainable AI for trees.Nature Machine Intelligence, 2(1), 56–67.
https://doi.org/10.1038/s42256-019-0138-9
Pargent, F., Pfisterer, F., Thomas, J., & Bischl, B. (2022). Regularized target encoding
outperforms traditional methods in supervised machine learning with high cardinality features.
Computational Statistics, 37(5), 2671–2692.
https://doi.org/10.1007/s00180-022-01207-6
Pérez-Rave, J. I., Correa-Morales, J. C., & González-Echavarría, F. (2019). A machine
learning approach to big data regression analysis of real estate prices for inferential and
predictive purposes.Journal of Property Research, 36(1), 59–96.
https://doi.org/10.1080/09599916.2019.1587489
Rosen, S. (1974). Hedonic prices and implicit markets: Product differentiation in pure
competition.Journal of Political Economy, 82(1), 34–55.https://doi.org/10.1086/260169
Samb, R., Roy, U. K., & Suneja, M. (2025). Modeling the determinants of urban short-term
rental prices in Gambia: A case of Greater Banjul Area.Research Square[Preprint].
https://doi.org/10.21203/rs.3.rs-8074344/v1
Truong, Q., Nguyen, M., Dang, H., & Mei, B. (2020). Housing price prediction via improved
machine learning techniques.Procedia Computer Science, 174, 433–442.
https://doi.org/10.1016/j.procs.2020.06.111
19
