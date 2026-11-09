---
title: Improvements to the post-processing of weather forecasts using machine learning and feature selection
url: https://arxiv.org/abs/2604.19340
category: ai-marketing
subcategory: measurement
date: 2026-04
venue: ''
authors:
- Kazuma Iwase
- Tomoyuki Takenawa
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.19340
pages: 24
chars: 55177
fetched_at: '2026-11-08T13:28:26+00:00'
kb_version: 1
---

# Improvements to the post-processing of weather forecasts using machine learning and feature selection

Improvements to the post-processing of weather forecasts using
machine learning and feature selection
Kazuma Iwase 1 and Tomoyuki Takenawa1∗
1Graduate School of Marine Science and Technology, Tokyo University of Marine Science and Technology,
2-1-6 Etchujima, Koto-ku, Tokyo 135-8533, Japan
Abstract
This study aims to develop and improve machine learning-based post-processing models
for precipitation, temperature, and wind speed predictions using the Mesoscale Model (MSM)
dataset provided by the Japan Meteorological Agency (JMA) for 18 locations across Japan,
including plains, mountainous regions, and islands. By incorporating meteorological variables
from grid points surrounding the target locations as input features and applying feature selection
based on correlation analysis, we found that, in our experimental setting, the LightGBM-based
models achieved lower RMSE than the specific neural-network baselines tested in this study,
including a reproduced CNN baseline, and also generally achieved lower RMSE than both the
raw MSM forecasts and the JMA post-processing product, MSM Guidance (MSMG), across
many locations and forecast lead times. Because precipitation has a highly skewed distribution
with many zero cases, we additionally examined Tweedie-based loss functions and event-weighted
training strategies for precipitation forecasting. These improved event-oriented performance
relative to the original LightGBM model, especially at higher rainfall thresholds, although the
gains were site dependent and overall performance remained slightly below MSMG.
Keywords:Weather prediction; post-processing; machine learning; feature selection
1 Introduction
1.1 Research Background and Objectives
Numerical weather prediction (NWP) is a primary method of weather forecasting that represents
future atmospheric states using mathematical models based on observation data. Over the years, it
has evolved through advancements in the representation of physical processes, model initialization,
including assimilation, and the introduction of ensemble modeling (Bauer et al., 2015). However,
NWP is not without its limitations, such as forecast errors and biases. While forecast variance
might be unavoidable, several post-processing techniques using machine learning models have been
developed to mitigate these biases (Liu et al., 2023; Rojas-Campos et al., 2023; Yoshikane and
Yoshimura, 2022; Zhang and Ye, 2021; Kudo, 2022; Peng et al., 2020; Tang et al., 2021; Salazar
et al., 2022; Xu et al., 2020).
The Japan Meteorological Agency (JMA) has also introduced a post-processing method called
the MSM Guidance (MSMG) to correct the errors of the Mesoscale Model (MSM), which has a
finer grid spacing (5 km) and targets areas around Japan compared to global models (JMA, 2024).
In MSMG, JMA primarily employs statistical methods, such as the Kalman filter, frequency bias
correction, and neural networks, to reduce the systematic biases in MSM.
This study aims to develop machine learning-based post-processing models for precipitation,
temperature, and wind speed predictions—representative meteorological variables—using MSM data
for 18 locations across Japan, including plains, mountainous regions, and islands. Meteorological
∗Corresponding author. Email: takenawa@kaiyodai.ac.jp
1
arXiv:2604.19340v1  [physics.ao-ph]  21 Apr 2026

variables from grid points surrounding the prediction locations were used as input features, and
feature selection based on correlation analysis was applied. In our experimental setting, the
LightGBM-based models achieved lower RMSE than the tested neural-network baselines, including
the reproduced CNN baseline, and also generally achieved lower RMSE than both the raw MSM
forecasts and the JMA post-processing product, MSM Guidance (MSMG). Among the LightGBM-
based models, those using surrounding-grid information with correlation-based feature selection
showed the lowest RMSE across many locations and forecast lead times.
For precipitation, we further examined Tweedie-based loss functions and event-weighted training
strategies, which improved event-oriented metrics for some sites and rainfall thresholds even when
the gains in RMSE were limited.
1.2 Related Work
Several studies have developed post-processing models for precipitation using methods such as
convolutional neural networks (CNNs), neural networks, and Support Vector Machines (Zhang and
Ye, 2021; Liu et al., 2023; Rojas-Campos et al., 2023; Yoshikane and Yoshimura, 2022). Among
them, Zhang and Ye (2021) conducted comparative experiments on machine learning models, input
parameters, and training data periods for precipitation prediction, and concluded that LightGBM
provides the most balanced performance among the tested models.
For temperature post-processing models, CNNs, neural networks, and LightGBM have been
employed (Kudo, 2022; Peng et al., 2020; Tang et al., 2021). Kudo (2022) developed a CNN-based
temperature post-processing model targeting the Kanto region of Japan and demonstrated its
superior performance over the JMA’s MSMG.
Windspeedpost-processingmodelshavealsobeenexploredusingneuralnetworksandLightGBM
(Salazar et al., 2022; Tang et al., 2021; Xu et al., 2020). Xu et al. (2020) utilized LightGBM for
wind speed prediction, analyzing feature importance derived from the model. Their study revealed
that using all features, including various weather elements, as input outperformed models where
features were limited primarily to wind speed.
In addition to using NWP outputs, some studies have leveraged meteorological forecast data
from existing weather forecasting services (Iwase and Takenawa, 2024; Tsipis et al., 2023). Iwase
and Takenawa (2024) employed machine learning models such as LightGBM, XGBoost, and neural
networks to predict temperature and precipitation in mountainous regions. By incorporating
surrounding weather forecast data as input variables, the results were superior to existing weather
forecast services.
In recent machine learning research, deep learning methods have been developed significantly in
fields such as natural language processing and image recognition. In contrast, for tabular data,
tree-based models currently outperform deep learning models in terms of accuracy and require
less hyperparameter tuning costs (Shwartz-Ziv and Armon, 2022; Grinsztajn et al., 2022). The
utility of tree-based models has also been demonstrated in post-processing NWP outputs, which
often involve tabular data (Zhang and Ye, 2021; Xu et al., 2020). Recently, Hieta and Partio (2025)
reported that a tree-based gradient-boosting post-processing scheme (XGBoost) reduces RMSE for
short-range near-surface forecasts.
The remainder of this paper is organized as follows. Section 2 defines the methods and data
used in this study. Section 3 presents the results and discussion. Finally, Section 4 concludes the
study.
2 Methods
2.1 Data
In this study, we use MSM data from the JMA as the input for the model and observation data as
the target data for training. The MSM data were collected and distributed by Research Institute
2

for Sustainable Humanosphere, Kyoto University (RISH, 2024). The observation data from JMA
include cumulative precipitation over the past three hours, hourly temperature, and wind speed.
We selected the 18 observation sites from all over Japan (Figure 1, Table 1). Additionally, in order
to compare the forecast results, we collected MSMG data, a post-processed forecast provided by
JMA and distributed by the Japan Meteorological Business Support Center (JMBSC).
Figure 1:Map showing the 18 selected locations.
MSM consists of three-dimensional gridded predictions of future atmospheric conditions, in-
cluding temperature, wind, moisture, and solar radiation, with fine grid spacing of approximately
5 km. The forecasts cover Japan and surrounding sea areas (JMA, 2024). Surface-level data are
available at hourly intervals, while pressure-level data are available at three-hour intervals. The
forecasts are issued every three hours (00, 03, 06, 09, 12, 15, 18, 21 UTC) and extend up to 39
hours ahead. The surface grid comprises 505×481 points (grid spacing: 0.05°latitude×0.0625°
longitude), while the pressure-level grid consists of 253×241 points (grid spacing: 0.1°latitude×
0.125°longitude), covering the area from the northwest corner (47.6°N, 120°E) to the southeast
corner (22.4°N, 150°E).
MSM outputs a variety of meteorological elements on the surface and on multiple standard
pressure levels. In this study, we use the elements listed in Table 2 as predictors. For pressure-level
variables, although MSM provides outputs at more pressure levels, we use only three representative
levels (850, 500, and 200 hPa), following prior work (Liu et al., 2023), to capture information from
the lower, middle, and upper atmosphere while reducing dimensionality. The CNN baseline uses a
different input configuration following prior work (including additional near-surface pressure levels);
see Section 2.5.
For each station, we train an independent regression model. Except for the CNN-based model,
3

T able 1:Latitude, longitude, altitude, and station numbers of the 18 sites shown in Figure 1.
Latitude Longitude Altitude Station Number
Ashimine 26.193 127.638 3 0
Uchinoura 31.277 131.055 8 1
Minamiaso 32.832 131.013 394 2
Uwanokogen 35.432 134.583 540 3
Imabari 34.053 132.975 27 4
Sakai 34.555 135.485 20 5
Kuwana 35.050 136.693 3 6
Sekigahara 35.363 136.467 130 7
Itoigawa 37.043 137.875 8 8
Nobeyama 35.948 138.472 1350 9
Niijima 34.368 139.268 29 10
Tsujido 35.320 139.450 5 11
Saitama 35.875 139.587 8 12
Kusatsu 36.617 138.592 1223 13
Kamaishi 39.270 141.878 5 14
Oma 41.527 140.912 14 15
Ishikari 43.193 141.370 5 16
Kamikawa 43.847 142.753 324 17
Table 2:Meteorological elements used as predictors, including names and units. A✓ indicates that the
element is used at the surface and/or at the representative pressure levels (850, 500, and 200 hPa). (Relative
humidity is used at 850/500 hPa only.)
Element Name Surface Pressure Level Unit
(hourly) (every 3 hours)
Temperature✓ ✓ ◦C
Relative humidity✓850/500 hPa only %
Hourly precipitation✓mm
Wind speed✓ ✓m s −1
U wind component✓ ✓m s −1
V wind component✓ ✓m s −1
Vertical velocity✓hPa s −1
Surface pressure✓hPa
Sea level pressure✓hPa
Geopotential height✓m
Solar radiation✓W m −2
Total cloud cover✓%
Low cloud cover✓%
Mid-level cloud cover✓%
High cloud cover✓%
4

the inputs to LightGBM and the neural network are one-dimensional feature vectors constructed
by concatenating (i) surface variables within a temporal window(t,t− 1,t− 2), (ii) pressure-level
variables at the target timet only (850, 500, and 200 hPa), and (iii) auxiliary scalar features (lead
time, month, and hour of day). All gridded predictors are flattened before concatenation. The
temporal window length was chosen to match the 3-hourly forecast cycle of MSM/MSMG, so that
a consistent set of predictors is available across lead times and forecast cycles.
The input variables consist of 13 surface variables and 7 pressure-level variables as summarized
in Table 2. Among the pressure-level variables, relative humidity is available only at two levels
(850 and 500 hPa), whereas the other six variables are available at all three levels.
We prepared two input configurations. In the first, only the grid cell closest to the prediction
point is used. In this configuration, the total number of input features is 62, computed as
13×3 + (6×3 + 2) + 3 = 62,
where13×3accounts for the 13 surface variables at three time steps,(6×3 + 2)counts pressure-level
combinations (six variables at three levels plus relative humidity at two levels) at timet, and+3
accounts for lead time, month, and hour of day.
In the second, surrounding grid cells are included to assess the benefit of spatial context. Because
the pressure-level fields have twice the horizontal grid spacing of the surface fields, we use an11× 11
grid for surface variables and a7× 7grid for pressure-level variables so that the covered areas are
comparable. Under this surrounding-grid configuration, the total number of input features is 5,702,
computed as
13×3×11×11 + (6×3 + 2)×7×7 + 3 = 5702,
where13is the number of surface variables,3is the number of time steps for surface variables,
11× 11is the surface grid,(6× 3 + 2)counts pressure-level combinations at timet,7 × 7is the
pressure-level grid, and+3accounts for lead time, month, and hour of day.
The output variables are the cumulative precipitation over the past three hours, as well as
hourly temperature and wind speed. Observation data from 2019 to 2021 were used for training,
2022 for validation, and 2023 for testing, as shown in Table 3. Since the MSM provides complete
fields without missing values, only observation samples containing missing values were excluded
from the dataset. The validation data were used solely for model selection and hyperparameter
tuning, and were not used to retrain the model prior to testing. Figure 2 presents box plots for
each location and meteorological variable.
For MSMG, the accumulated surface precipitation over the past three hours and hourly surface
temperature and wind speed are predicted up to 39 hours ahead, with forecast outputs available
every three hours (00, 03, 06, 09, 12, 15, 18, and 21 UTC). Precipitation forecasts are provided
on a grid with dimensions of 560 (longitude)×480 (latitude), corresponding to a grid spacing of
0.05◦ in latitude and 0.0625◦ in longitude, covering the area from (47.975◦N, 120.03125◦E) in the
northwest to (20.025◦N, 149.96875◦E) in the southeast. In contrast, forecasts for temperature and
wind speed are provided at the locations of JMA observation stations.
The dataset is summarized as follows. The outputs consist of three variables (precipitation,
temperature, and wind speed), while the inputs are identical across them. Missing values occur only
in the observation data. The period covers the entire span of the training (2019–2021), validation
(2022), and test (2023) sets. The total number of rows is determined by the combination of period,
forecast cycles, lead times, and locations, while the number of columns differs according to the
input configuration.
Period:2019–2023 (1,826 days)
F orecast cycles per day:8 (3-hourly)
Lead times per cycle:13 (3–39 h)
Locations:18
T otal rows:3,418,272 (before removing missing observations)
5

Table 3:The number of samples in the training, validation, and test datasets, and the total number of
features when using the surrounding grids of the prediction point, as well as the number of features after
feature selection based on correlation analysis.
Train samples Validation samples Test samples Original Features Dropped features
Ashimine 113854 37882 37934 5702 239
Uchinoura 113854 37843 37947 5702 296
Minamiaso 113828 37830 37960 5702 502
Uwanokogen 108642 37570 37947 5702 385
Imabari 113802 37830 37934 5702 408
Sakai 113776 37830 37947 5702 455
Kuwana 111891 37817 37960 5702 354
Sekigahara 113568 37830 37934 5702 437
Itoigawa 113609 37843 37817 5702 516
Nobeyama 113022 37544 37791 5702 869
Niijima 113477 37778 37921 5702 236
Tsujido 113763 37791 37960 5702 416
Saitama 113789 37817 37960 5702 248
Kusatsu 112359 37271 37752 5702 733
Kamaishi 113464 37687 37921 5702 295
Oma 113815 37804 37895 5702 256
Ishikari 113243 37791 37934 5702 271
Kamikawa 113607 36907 37791 5702 413
2.2 LightGBM
Several previous studies on tabular data and post-processing model development have reported
that decision tree-based models outperform other machine learning models in terms of training
cost and performance scores. Among decision tree-based models, LightGBM (Ke et al., 2017) is
particularly fast and high-performing (Iwase and Takenawa, 2024). Therefore, this study adopts
LightGBM for the development of the post-processing model. LightGBM is an ensemble model
based on decision trees, employing a boosting algorithm that sequentially adds decision trees and
uses a quadratic optimization method.
Since LightGBM cannot handle multiple output variables simultaneously, a separate model
should be created for each output variable. During training, Early Stopping was applied using
validation data with a patience of 10 epochs, and the loss function was set to Mean Squared Error
(MSE).
MSE= 1 N N∑ i=1 (ˆyi−yi)2 (1)
whereNis the number of data points,ˆyi is the predicted value, andyi is the observed value.
2.3 Feature Selection
When surrounding grids are included, the number of features reached 5,702, which is excessive
for LightGBM. Feature selection is necessary to reduce training time and prevent overfitting. To
achieve this, the correlation analysis method proposed in (Bedi and Toshniwal, 2018), denoted as
FS0 hereafter, was applied. FS0 computes pairwise absolute Pearson correlations among candidate
features and removes redundancies.
To avoid removing critical input information, we exclude features at the grid closest to the
prediction target and calendar variables from the analysis by dropping columns. Thus, the
correlation analysis is performed solely among features from surrounding grids.
Let τ denote the correlation threshold. FS0 builds the absolute correlation matrix[|r(xi,xj)|]i,j
and scans features in their column order. For each featurexj, if there exists any earlier featurexi
(i<j )with |r(xi,xj)|>τ , thenxj is dropped (left-to-right rule). Based on validation data, the
6

(a)Precipitation
(b)Temperature
(c)Wind Speed
Figure 2:Box plots of the distributions of each meteorological variable at each location. For precipitation,
only nonzero values are shown (values> 0mm) to avoid the dominance of zero precipitation and to provide
an informative visualization; the precipitation axis is displayed on a logarithmic scale. The green triangle
markers indicate the mean values.
threshold was set toτ = 0.9. The number of features after correlation analysis for each location is
summarized in Table 3.
After applying the aforementioned feature selection process or in the case where only single-grid
data were used, the following three further feature selection methods were applied to determine the
optimal number of features:
FS1. A method based on the correlation coefficient between each feature and the output variable.
FS2. A method based on the mutual information between each feature and the output variable.
FS3. A method based on feature importance calculated by LightGBM.
7

While many feature selection methods exist, this study adopted representative approaches
(Chandrashekar and Sahin, 2014; Ross, 2014). The correlation coefficient-based method calculates
the correlation coefficient between each feature and the output variable, and selects features in
descending order of the correlation coefficient. The mutual information-based method uses mutual
information between each feature and the output variable, where mutual information measures the
degree of dependence between two variables (Ross, 2014). The LightGBM feature importance-based
method calculates the contribution of each feature to reducing the loss function during tree splitting
in LightGBM. Additionally, an analysis of the number of selected features was conducted. Variables
such as prediction time, month, and hour were included in the final selected features regardless of
the feature selection results.
2.4 Parameter Tuning
Parameter tuning was conducted using Optuna (Akiba et al., 2019), a parameter optimization library
based on Bayesian optimization algorithms. Specifically, this study employed LightGBMTuner
(OPTUNA, 2024) to compute optimal values for each parameter iteratively. The tuning process
was performed using a single representative location, and the tuned parameters were applied to
other locations. The chosen representative location was Sekigahara, situated near the center of all
target locations. Since LightGBM cannot handle multiple output variables, tuning was conducted
separately for each output variable.
2.5 Neural Network and CNN
To provide comparisons with neural-network-based approaches used in previous studies, we also
implemented a feedforward neural network and a CNN model. The structure of the neural network,
implemented using TensorFlow (TensorFlow, 2024) with keras.layers, is as follows:
•Dense(1000, activation=’relu’)
•Dense(500, activation=’relu’)
•Dense(100, activation=’relu’)
•Dense(3)
The input dimension corresponds to the number of features after FS0 selection, and the output
dimension (3) corresponds to precipitation, temperature, and wind speed.
The model was trained with the Adam optimizer (learning rate 0.001) (Kingma, 2014), MSE as
the loss, and Root Mean Squared Error (RMSE) :
RMSE=
/radicaltp/radicalvertex/radicalvertex√ 1
N
N∑
i=1
(ˆyi−yi)2 (2)
as a metric. Training used early stopping with a patience of 10 epochs, based on validation RMSE.
We set a maximum of 1000 epochs with a batch size of 64; in practice, training typically converged
within about 25–50 epochs due to early stopping.
CNN models have many possible variations, including the number of layers, kernel sizes, numbers
of channels, the use of skip connections, and the choice of optimization and regularization methods.
A comprehensive comparison of these architectures is beyond the scope of the present paper.
Accordingly, we limited the comparison to a CNN model based on prior work that used CNNs for
post-processing MSM data. For the CNN baseline, we followed the experimental setting of Kudo
(2022) to reproduce a representative prior CNN-based approach under comparable data conditions.
Accordingly, the CNN was applied only to temperature prediction, as in the original study.
Our CNN uses a single forecast-time spatial field without a lookback window. The input is
a64 × 64× 7tensor centered at each of the 18 locations. The seven channels consist of four
8

surface-level fields (surface temperature, mean sea-level pressure, and surface wind componentsU
andV) and temperature at three pressure levels (975, 925, and 850 hPa). Because the pressure-level
grid is coarser than the surface grid, the pressure-level temperature fields are first cropped as
32× 32patches on the pressure-level grid and then upsampled to64× 64to match the surface
fields. The architecture of the CNN is shown in Figure 3 and summarized in Table 4.
Normalization for CNN was performed as follows:
x′ = x−x min
xmax−x min
(3)
where x′ represents the normalized value,x is the original value, andxmin and xmax are the
minimum and maximum values of the MSM input data. These minimum and maximum values were
calculated for each prediction time (data sample) rather than across the entire training dataset.
For temperature,xmin was adjusted toxmin− 3and xmax to xmax + 3. An inverse normalization
step was applied after the output layer, defined as:
y′ =y·(x max−x min) +x min (4)
where y is the output from the output layer, andy′ is the value after inverse normalization. These
normalization and inverse-normalization procedures were introduced to reproduce the prior study
as closely as possible, and should thus be understood as part of the baseline implementation rather
than as independently optimized design choices in this study.
The learning settings for CNN, including the optimizer, loss function, and batch size, were the
same as for NN. We set a maximum of 1000 epochs; in practice, training typically converged within
about 15–20 epochs due to early stopping.
Figure 3:Architecture of the CNN.
2.6 Evaluation Metrics
In addition to RMSE, we used Mean Error (ME),
ME= 1 N N∑ i=1 (ˆyi−yi),
to assess model bias, whereN is the number of data points,ˆyi is the predicted value, andyi is the
observed value.
In addition, the following metrics were used to further assess model performance for specific
variables.
2.6.1 Statistical T ests for T emperature and Wind Speed
Statistical comparisons were conducted using paired absolute errors. Let
emain i = ⏐⏐⏐ˆymain i −yi ⏐⏐⏐, e base i = ⏐⏐⏐ˆybase i −yi ⏐⏐⏐
9

Table 4:Summary of processing at each CNN layer. Each layer’s implementation is described using
TensorFlow (TensorFlow, 2024) keras.layers.
Layer F unction
ZeroPadding2D(padding=(2, 2))
Conv2D(32, kernel_size=5, strides=1, padding=’valid’)
Conv1MaxPooling2D(pool_size=2, strides=2)
BatchNormalization()
Activation(’relu’)
ZeroPadding2D(padding=(2, 2))
Conv2D(64, kernel_size=5, strides=1, padding=’valid’)
Conv2MaxPooling2D(pool_size=2, strides=2)
BatchNormalization()
Activation(’relu’)
Dense(4096)
FC1BatchNormalization()
Activation(’relu’)
FC2Dense(1)
denote the absolute errors of the main and baseline models for samplei. Then the mean absolute
errors (MAEs) are defined as
MAEmain = 1 N N∑ i=1 emain i ,MAE base = 1 N N∑ i=1 ebase i ,
and the paired differences are defined by
di =e main i −e base i .
Based on these paired differences, we conducted a pairedt-test and a Wilcoxon signed-rank test for
temperature and wind speed. Because of the very large sample size, these tests are interpreted only
as supplementary information, and practical significance is assessed mainly from the error metrics
themselves.
2.6.2 Event-Based Metrics for Precipitation
For precipitation, forecast skill was additionally evaluated using event-based metrics. For each
precipitation thresholdτ, forecasts and observations were converted into binary events. LetH(τ ),
M (τ ), andF (τ )denote the numbers of hits, misses, and false alarms, respectively, at thresholdτ.
Then, the event-based metrics were defined as
TS(τ) = H(τ) H(τ) +M(τ) +F(τ) ,
POD(τ) = H(τ) H(τ) +M(τ) ,
F AR(τ) = F(τ) H(τ) +F(τ) ,
Bias(τ) = H(τ) +F(τ) H(τ) +M(τ) .
2.7 Weighted Tweedie Model for Precipitation
Precipitation is a nonnegative variable with a highly skewed distribution and many zero or near-zero
values. Under such conditions, standard regression training based on mean squared error tends to
10

be dominated by the large number of weak-rainfall or no-rainfall samples, and may therefore lead to
predictions biased toward intermediate values, without sufficiently improving forecast accuracy for
moderate to heavy precipitation events. To address these characteristics, in this study we examined
a model that uses a Tweedie loss function with sample weight coefficients in LightGBM training for
precipitation prediction (hereafter referred to as the weighted Tweedie model) (Jørgensen, 1997;
Ke et al., 2017; Dunn and Smyth, 2005). In preliminary experiments for a few sites, the weighted
Tweedie model showed more improvements than the variants using only weighting or only the
Tweedie loss, so we focus on this variant here.
Let yi≥ 0denote the observed precipitation for samplei, and letµi> 0denote the predicted
mean precipitation. The Tweedie distribution belongs to the exponential dispersion family and
satisfies (Jørgensen, 1997; Dunn and Smyth, 2005)
Var(Yi) =ϕµ p i,
where ϕ> 0is the dispersion parameter andp is the Tweedie variance power. In this study, the
exponentpwas treated as a tunable hyperparameter.
The sample weights were defined as a monotone nondecreasing piecewise linear function of the
observed precipitation. Let the knot positions be
x0 = 0, x 1 = 5, x 2 = 10, x 3 = 15, x 4 = 20 mm,
and the corresponding weight values be
w0, w1, w2, w3, w4.
A monotonicity constraint,
1 =w 0≤w 1≤w 2≤w 3≤w 4,
was imposed. Then, the sample weight functionw(y)was defined by linear interpolation between
adjacent knots as follows:
w(y) =



w0 + w1−w 0 x1−x 0 (y−x 0), x 0≤y≤x 1,
w1 + w2−w 1 x2−x 1 (y−x 1), x 1<y≤x 2,
w2 + w3−w 2 x3−x 2 (y−x 2), x 2<y≤x 3,
w3 + w4−w 3 x4−x 3 (y−x 3), x 3<y.
In the implementation, the resulting weights were clipped to the range
1≤w(y)≤w max,
where wmax = 10. Thus, samples with higher precipitation intensity contributed more strongly
to training, while the monotonicity constraint maintained the stability and interpretability of the
weighting scheme.
Using these weights, the precipitation model was trained by minimizing the weighted Tweedie
loss
Ltrain =
N∑
i=1
w(yi)ℓ Tw(yi,µi),
where ℓTw(yi,µi)denotes the Tweedie loss for sample i. In this study, we used the Tweedie
objective implemented in LightGBM (Ke et al., 2017; LightGBM Contributors, 2026). Except
for the precipitation loss function and sample-weighting scheme described below, the input data
configuration and the tree-related LightGBM settings were the same as those of the “around all
tune” model.
11

Although the model was trained using the weighted Tweedie loss, the hyperparameters were
selected in Optuna based on an event-based evaluation score, because the purpose of weighting was
to improve performance at relevant precipitation thresholds. The tuned hyperparameters were the
Tweedie variance powerp and the parameters determining the shape of the weight function, and
the tuning was carried out separately for each observation site because the behavior of the weighted
Tweedie model showed strong site dependence. A monotone nondecreasing constraint was imposed
on the weight function so that the weight would not decrease as precipitation intensity increased.
Using the event-based metrics defined in Section 2.6.2, the TS values across thresholds were
aggregated using a geometric mean:
Sgeo = exp
(
1
|T|
∑
τ∈T
log
(
max(TS(τ),ε)
)
)
.
Furthermore, to suppress overprediction or underprediction of event frequency, a penalty was
imposed on the forecast Bias at selected thresholds. Using this, the total score employed in Optuna
was defined as
Stotal =S geo−
∑
τ∈T bias
γτ
⏐⏐log ( max(Bias(τ),b min) )⏐⏐.
Here, γτ≥ 0denotes the penalty coefficient,Tbias denotes the set of thresholds to which the bias
penalty is applied, andbmin is a small positive constant for numerical stability. This objective
function was intended to encourage models with balanced detection skill across multiple thresholds
while reducing substantial overprediction or underprediction of event frequency.
In the present implementation, the thresholds used for optimization were set to
T={1,2,...,20}mm,
and equal weights were used for all thresholds in the geometric mean. In addition, the bias penalty
was applied at 1, 5, 10, and 15 mm withγτ = 0.05for all of these thresholds, andε = 10−6 and
bmin = 10−6 were set for numerical stability. The resulting model is referred to as the weighted
Tweedie model in the following sections.
3 Results and Discussion
3.1 Model Comparison
3.1.1 RMSE and ME
First, Table 5 and Table 6 present the RMSE and ME of each model, as well as for MSM and
MSMG, on the validation and test datasets.
For RMSE, both validation and test datasets show that the models using LightGBM outperform
MSM and MSMG. Similarly, the neural network and CNN models perform worse compared to those
using LightGBM. Moreover, models incorporating data from surrounding grids (around) exhibit
slightly better performance than those using only the nearest grid (1grid). This indicates that
leveraging features from surrounding grids and reducing them through feature selection allows for
the inclusion of informative data that improves accuracy. The correlation analysis-based feature
selection (FS0) of surrounding grid data yielded the best results in most cases. Among the three
feature selection methods (FS1 - FS3) described in Section 2.3, no performance improvement was
observed. For the number of features in FS1 to FS3, we used the values that performed best for
each feature selection method and each output variable in Section 3.2.
For ME, models using LightGBM tended to reduce bias in both validation and test datasets.
However, for precipitation in the validation dataset, MSM achieved the best ME, while for
temperature in the test dataset, MSMG performed the best.
For subsequent predictions in this study, we used the “around all tune” model, which showed
the best overall performance; here, “around” indicates the use of surrounding-grid predictors, “all”
12

indicates that all selected predictors were retained without further reduction, and “tune” indicates
hyperparameter optimization.
Figure 4 shows the prediction results for test data compared with MSM, MSMG, and observed
values at selected locations and prediction times. In the case of 3-hour precipitation at Kamikawa
and 18-hour wind speed at Itoigawa, post-processing models corrected the apparent large bias. On
the other hand, for 18-hour temperature at Itoigawa, partial corrections by the post-processing
model were observed.
Table 5:RMSE and ME for validation data. “1grid” represents models using data from only one grid,
“around” indicates the use of surrounding grid data, “nn” denotes neural network, “all” refers to data before
three feature selection methods (FS1 - FS3), “pcc” indicates the correlation coefficient-based method (FS1),
“mi” denotes the mutual information method (FS2), “gbm” represents the feature importance method by
LightGBM (FS3), and “tune” refers to parameter tuning. Averages are calculated across prediction times
and locations.
RMSE ME
Precip. Temp. Wind Precip. Temp. Wind
MSM 2.948 1.836 2.096 0.048 -0.405 0.753
1grid nn 2.555 1.472 1.167 -0.075 0.130 -0.013
1grid all 2.510 1.364 1.070 -0.007 0.084 -0.018
1grid pcc 2.526 1.367 1.070 -0.003 0.085 -0.018
1grid mi 2.535 1.420 1.070 -0.0010.096-0.016
1grid gbm 2.518 1.363 1.073 -0.006 0.085 -0.018
around all 2.501 1.332 1.050 0.0010.081 -0.025
around pcc 2.496 1.344 1.053 0.006 0.082 -0.026
around mi 2.505 1.342 1.051 0.004 0.083 -0.026
around gbm 2.502 1.333 1.051 -0.002 0.080 -0.027
around all tune 2.489 1.326 1.046 0.0090.074-0.023
CNN 1.487 0.086
T able 6:RMSE and ME for test data.
RMSE ME
Precip. Temp. Wind Precip. Temp. Wind
MSM 2.759 1.811 1.999 0.085 -0.340 0.673
MSMG 2.726 1.394 1.237 0.1070.0140.159
1grid nn 2.439 1.485 1.175 -0.064 0.143 -0.060
1grid all 2.387 1.368 1.075 0.020 0.110 -0.058
1grid pcc 2.390 1.369 1.076 0.0160.109 -0.058
1grid mi 2.409 1.428 1.075 0.028 0.117-0.057
1grid gbm 2.392 1.368 1.078 0.017 0.111 -0.058
around all 2.358 1.341 1.053 0.031 0.111 -0.062
around pcc 2.374 1.349 1.056 0.030 0.124 -0.062
around mi 2.381 1.347 1.055 0.033 0.119 -0.061
around gbm 2.361 1.3411.052 0.028 0.112 -0.063
around all tune 2.344 1.335 1.052 0.033 0.106 -0.059
CNN 1.501 0.179
3.1.2 Statistical T ests and Event-Based Metrics
For temperature and wind speed, Table 7 summarizes the pairedt-test and Wilcoxon signed-rank
test results comparing the main model (around all tune) with the baseline models (MSM and
13

(a)Accumulated precipitation for the 0–3 h forecast interval at Kamikawa
(b)18-h lead temperature at Itoigawa
(c)18-h lead wind speed at Itoigawa
Figure 4:Examples of prediction results for the test data in February, compared with MSM, MSMG, and
observed values. Panel (a) shows accumulated precipitation for the 0–3 h forecast interval, while panels (b)
and (c) show temperature and wind speed at the 18-h forecast lead time, respectively.
14

MSMG), based on the metrics defined in Section 2.6.1. The table reportsMAEmain, MAEbase, the
standard deviation of the paired differences, and the corresponding one-sidedp-values. Because
of the very large sample size, these test results should be interpreted only as supplementary
information, and practical significance should be assessed mainly from the error metrics themselves.
For precipitation, Table 8 summarizes the event-based metrics defined in Section 2.6.2—TS,
POD, F AR, and Bias—for four precipitation thresholds. Here, “around all tune” denotes our
original LightGBM-based post-processing model, and “weighted Tweedie” denotes the weighted
Tweedie model.
Overall, MSMG showed favorable performance among the compared models. The “around all
tune” model achieved the highest POD at the 1.0 mm threshold, indicating high sensitivity to
light precipitation events. However, its FAR and Bias were also the largest, suggesting that it
tended to overpredict precipitation occurrence. At thresholds of 5.0 mm and above, its TS and
POD became lower than those of MSM and MSMG, and its Bias fell well below 1 at 10.0 mm and
15.0 mm, indicating underdetection of heavier precipitation events. Compared with this behavior,
the weighted Tweedie model improved TS and Bias at 10.0 mm and increased POD at 5.0 mm.
Although its overall performance was still slightly below that of MSMG, it showed a better balance
across the precipitation thresholds.
T able 7:Paired t-test and Wilcoxon signed-rank test results comparing the LightGBM “around all tune”
model (main model) with the baseline models for temperature and wind speed. The table reports the mean
absolute errors (MAEs) of the main and baseline models, the standard deviation of the paired differences in
absolute error (SDdiff), and the corresponding one-sidedp-values. All tests were performed overN = 682,305
paired samples.
Variable Baseline MAE main MAEbase SDdiff pt pW
Temperature MSM 0.9888 1.3964 1.08400.000 0.000
Temperature MSMG 0.9888 1.0275 0.76750.000 0.000
Wind Speed MSM 0.7549 1.4186 1.35300.000 0.000
Wind Speed MSMG 0.7549 0.9035 0.69800.000 0.000
3.2 Comparison of Feature Selection Methods
Here, we conducted experiments at a single location in Sekigahara, similar to parameter tuning, to
evaluate the influence of the number of selected features in the three feature selection methods
(FS1 - FS3) proposed in Section 2.3. For both cases where only the data of the grid closest to the
prediction point (1grid) and the data including surrounding grids (around) were used, the three
feature selection methods were applied, and models were constructed by incrementally increasing
the number of selected featuresk by 10. Figure 5 summarizes the RMSE on the validation data for
each feature countk. The results indicate that the accuracy tends to improve as the number of
features increases, but stabilizes when the number of features exceeds a certain threshold. This
suggests that further feature selection after correlation analysis does not enhance accuracy.
3.3 Results by Location and Prediction Time
3.3.1 Location-Based Results
Figure 6 summarizes the RMSE on test data for each observation location. Our post-processing
model consistently outperformed MSM and showed comparable or slightly better performance than
MSMG across most sites. For precipitation, relatively large RMSE values were observed in the
southwestern part of Japan, including Ashimine and Uchinoura. This is likely associated with the
frequent occurrence of typhoons and strong convective rainfall events in these regions. In contrast,
the lowest precipitation RMSE values were found in inland and mountainous areas such as Kusatsu
and Nobeyama.
15

T able 8:Event-based verification metrics for precipitation, pooled over all locations and forecast lead times.
Higher TS and POD indicate better detection skill, lower FAR indicates fewer false alarms, and Bias values
closer to 1 indicate better frequency matching. Here, “around all tune” denotes the original LightGBM-based
post-processing model.
Threshold (mm) Model TS POD FAR Bias
1.0 MSM 0.4311 0.6373 0.4287 1.1156
1.0 MSMG0.45550.65580.4014 1.0956
1.0 around all tune 0.4293 0.6931 0.4699 1.3075
1.0 weighted Tweedie 0.44350.70050.4527 1.2800
5.0 MSM 0.3226 0.5061 0.5293 1.0753
5.0 MSMG0.33440.5014 0.49911.0009
5.0 around all tune 0.3059 0.39430.42280.6831
5.0 weighted Tweedie 0.33160.52080.5228 1.0912
10.0 MSM 0.2450 0.4084 0.6201 1.0749
10.0 MSMG 0.24850.41220.6152 1.0713
10.0 around all tune 0.1966 0.23560.45710.4340
10.0 weighted Tweedie0.25200.3979 0.59270.9771
15.0 MSM 0.1902 0.3189 0.67960.9956
15.0 MSMG0.2096 0.35510.6616 1.0492
15.0 around all tune 0.1251 0.14200.48770.2772
15.0 weighted Tweedie 0.1883 0.2719 0.6201 0.7158
For wind speed, extremely high RMSE values in MSM were observed in island and coastal
areas such as Niijima and Oma. Our model significantly reduced these errors, achieving RMSE
values comparable to those in other regions. Overall, the regional pattern of RMSE reduction
indicates that the post-processing model effectively mitigates the biases and noise that are spatially
correlated with topography and surrounding meteorological conditions.
T able 9:Average RMSE by terrain category and model. The three terrain categories are defined as follows:
mountain(Kusatsu, Kamikawa, Nobeyama, Uwanokogen, Minamiaso),island(Ashimine, Niijima), and
coastal/plain(Ishikari, Oma, Imabari, Kamaishi, Tsujido, Itoigawa, Uchinoura, Sekigahara, Saitama,
Kuwana, Sakai).
Region around_all_tune MSM MSMG
Precip. Temp. Wind Precip. Temp. Wind Precip. Temp. Wind
coastal/plain 1.982 1.343 1.002 2.454 1.793 1.864 2.400 1.363 1.211
island 2.951 1.003 1.576 3.492 1.654 2.550 3.349 1.106 1.647
mountain 2.369 1.398 0.822 2.630 1.804 1.337 2.605 1.508 1.038
As shown in Table 9, the selectedaround_all_tunemodel achieved the lowest RMSE across all
terrain types and variables. The improvement was most pronounced in mountainous and island
areas, where spatial heterogeneity in meteorological conditions is large. This demonstrates that
incorporating spatial context from surrounding grids improves model robustness under complex
terrain and coastal influences.
3.3.2 Prediction-Time-Based Results
Figure 7 summarizes the RMSE on test data for each prediction time. In terms of RMSE, the
selected around_all_tune model outperformed both MSM and MSMG at almost all forecast lead
times. For all methods, RMSE increased as prediction time became longer, which is a common
characteristic of numerical weather prediction (NWP) models, where forecast accuracy declines
16

(a)Precipitation
(b)Temperature
(c)Wind Speed
Figure 5:Changes in accuracy based on the number of selected features for the feature selection methods
on validation data in Sekigahara. Results are averaged over prediction times.
with lead time. A similar trend was observed in our post-processing results, indicating that the
residual errors of the base NWP propagate into the corrected predictions as forecast uncertainty
accumulates. Nevertheless, the selected around_all_tune model maintained lower RMSE than
MSM and, in many cases, MSMG across forecast horizons, confirming its stability over time.
3.3.3 Scatter Plots Against Observations
Figure 8 compares observations with the model outputs at Sekigahara during the test period. For
readability, all lead times are pooled and a random subset of 150 samples is plotted.
17

(a)Precipitation
(b)Temperature
(c)Wind Speed
Figure 6:RMSE by location on test data. Results are averaged over prediction times.
3.4 Site-Dependent Behavior of the Weighted Tweedie Model
The effect of the weighted Tweedie model was strongly site dependent. To illustrate this point,
we compare two representative examples: Kamikawa, where the improvement was limited, and
Saitama at the 18-h lead time, where the weighted Tweedie model showed clearer improvement in
the time-series comparison.
Figure 9(a) shows the 0–3 h accumulated precipitation at Kamikawa. In this case, the weighted
Tweedie model remained close to the original “around all tune” model, and the difference between
the two predictions was small for many events. This behavior is consistent with the site-wise
aggregated verification results summarized in Table 10. At Kamikawa, the weighted Tweedie model
produced only a slight change at the 1.0 mm threshold and did not improve TS at 5.0 mm, although
18

(a)Precipitation
(b)Temperature
(c)Wind Speed
Figure 7:RMSE by prediction time on test data. Results are averaged over locations.
TS and POD were slightly improved at 10.0 and 15.0 mm. Overall, however, the weighted Tweedie
model still remained clearly below MSMG for this site, indicating that the modification was not
sufficient to overcome the difficulty of precipitation forecasting at this site.
By contrast, Figure 9(b) shows a case at Saitama for the 15–18 h accumulated precipitation,
where the weighted Tweedie model more clearly modified the predicted peaks and, for several
events, tracked the observed precipitation more closely than “around all tune”. This behavior is
also reflected in the site-wise aggregated results in Table 10. At Saitama, the weighted Tweedie
model improved TS relative to “around all tune” at all four thresholds and substantially increased
POD at 5.0, 10.0, and 15.0 mm, while also moving Bias much closer to 1 than the original model
at 5.0 and 10.0 mm. At 15.0 mm, the weighted Tweedie model still showed the best TS among the
19

(a)Precipitation
 (b)Temperature
 (c)Wind speed
Figure 8:Scatter plots at Sekigahara on the test period (all lead times pooled). Each panel shows
observations versus model outputs for the same randomly sampled points.
compared models, although its Bias remained below 1. These results suggest that the weighted
Tweedie model can improve event-oriented behavior for some sites, especially when the original
model underdetects moderate to heavy precipitation.
Taken together, these examples indicate that the weighted Tweedie model is useful mainly
as a site-dependent adjustment rather than as a uniformly superior replacement for the original
LightGBM model. This observation is consistent with the need for site-wise hyperparameter tuning
discussed in Section 2.7.
Table 10:Site-wise precipitation verification metrics for two representative cases. Higher TS and POD
indicate better detection skill, while Bias values closer to 1 indicate better frequency matching.
Site Model Threshold (mm) TS POD Bias
Kamikawa
MSMG 1.0 0.38020.5501 0.9933
around all tune 1.0 0.3817 0.5311 0.9367
weighted Tweedie 1.00.38630.5319 0.9276
MSMG 5.00.2447 0.3897 0.9464
around all tune 5.0 0.1541 0.1852 0.3492
weighted Tweedie 5.0 0.1264 0.1488 0.3057
MSMG 10.00.1278 0.2802 0.9973
around all tune 10.0 0.0267 0.0275 0.0687
weighted Tweedie 10.0 0.0471 0.0522 0.0962
MSMG 15.00.0667 0.1703 0.9725
around all tune 15.0 0.0000 0.0000 0.0000
weighted Tweedie 15.0 0.0055 0.0055 0.0055
Saitama
MSMG 1.00.43910.63831.0919
around all tune 1.0 0.4150 0.6911 1.3563
weighted Tweedie 1.0 0.43300.71601.3696
MSMG 5.00.3549 0.4994 0.9065
around all tune 5.0 0.2308 0.2521 0.3444
weighted Tweedie 5.0 0.3429 0.4959 0.9420
MSMG 10.0 0.1935 0.3231 0.9923
around all tune 10.0 0.1493 0.1538 0.1846
weighted Tweedie 10.00.3395 0.4962 0.9577
MSMG 15.0 0.20480.36751.1624
around all tune 15.0 0.0678 0.0684 0.0769
weighted Tweedie 15.00.26000.33330.6154
20

(a)Accumulated precipitation for the 0–3 h forecast interval at Kamikawa
(b)Accumulated precipitation for the 15–18 h forecast interval at Saitama
Figure 9:Comparison of precipitation forecasts for two representative cases. Panel (a) shows Kamikawa,
where the weighted Tweedie model remained close to the original “around all tune” model and the improvement
was limited. Panel (b) shows Saitama, where the weighted Tweedie model showed improved event-oriented
behavior for several precipitation events.
4 Conclusion
In this study, we developed machine learning-based post-processing models for precipitation,
temperature, and wind speed using observation data and MSM data across 18 locations in Japan,
including plains, mountainous areas, and islands. The main findings are summarized as follows:
1. The use of surrounding grid data together with correlation-based feature selection improved
prediction accuracy compared with using only the single nearest grid. This result supports
the effectiveness of incorporating spatial information from surrounding grids while controlling
feature dimensionality through feature selection. In contrast, further feature selection beyond
this correlation-based reduction did not provide additional improvement in our experiments.
2. In our experimental setting, the LightGBM-based models achieved lower RMSE than the
tested neural-network baselines, including the reproduced CNN baseline, and also generally
achieved lower RMSE than the JMA guidance product MSMG. However, because the neural-
network comparison was limited to specific baseline implementations, the present results do
not exclude the possibility that stronger deep-learning architectures could perform better.
3. For precipitation, the results showed that optimizing only standard regression-oriented
objectives is not necessarily sufficient, especially when the forecasting goal is to improve
21

the prediction of moderate and heavy rainfall events. To address this issue, we introduced
Tweedie-based loss functions and event-weighted training strategies. These approaches
improved event-oriented behavior, including better detection of stronger rainfall events
at some sites and thresholds. However, the gains were not uniform across locations and
conditions, indicating that further improvement is still needed. This site dependence suggests
that inter-station differences related to topography and site characteristics, such as latitude,
longitude, and altitude, may need to be considered more explicitly in future work.
To complement the representative examples and pooled results shown in the main text, detailed
verification results by site and forecast lead time are provided in the Supplementary Material. These
include RMSE and ME of MSM, MSMG, and “around all tune” for precipitation, temperature,
and wind speed, as well as precipitation event-based metrics (TS, POD, FAR, and Bias), including
those of the weighted Tweedie model.
Data and Code A vailability
The code used in this study is available at:https://github.com/ttakenawa/PostMSM. Due to
data licensing restrictions, the repository provides a synthetic/derived dataset for demonstration,
which may not exactly reproduce the paper results.
Declaration of generative AI and AI-assisted technologies in the manuscript preparation
process
During the preparation of this manuscript, the authors used ChatGPT to assist with code editing
and language proofreading. All AI-assisted outputs were reviewed and revised by the authors as
needed, and the authors take full responsibility for the content of the manuscript.
Acknowledgements
The authors thank the reviewers for their careful reading and helpful comments. The first author
was supported by the WISE Program for the Development of AI Professionals in the Marine
Industry at Tokyo University of Marine Science and Technology; the second author was supported
by the Japan Society for the Promotion of Science, Grant-in-Aid (C) (22K03383).
References
Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori Koyama. Optuna:
A next-generation hyperparameter optimization framework. InProceedings of the 25th ACM
SIGKDD international conference on knowledge discovery & data mining, pages 2623–2631, 2019.
Peter Bauer, Alan Thorpe, and Gilbert Brunet. The quiet revolution of numerical weather prediction.
Nature, 525(7567):47–55, 2015.
Jatin Bedi and Durga Toshniwal. Attribute selection based on correlation analysis. InAdvances in
big data and cloud computing, pages 51–61. Springer, 2018.
Girish Chandrashekar and Ferat Sahin. A survey on feature selection methods.Computers &
electrical engineering, 40(1):16–28, 2014.
Peter K. Dunn and Gordon K. Smyth. Series evaluation of tweedie exponential dispersion model
densities.Statistics and Computing, 15(4):267–280, 2005.
Léo Grinsztajn, Edouard Oyallon, and Gaël Varoquaux. Why do tree-based models still outperform
deep learning on typical tabular data?Advances in neural information processing systems, 35:
507–520, 2022.
Leila Hieta and Mikko Partio. Operational machine learning post-processing of short-range
temperature, humidity, wind speed and gust forecasts.Meteorological Applications, 32:e70074,
2025.
22

Kazuma Iwase and Tomoyuki Takenawa. Interpolation of mountain weather forecasts by machine
learning.Journal of Information Processing, 32:873–880, 2024.
JMA. Outline of the operational numerical weather prediction at the japan meteorological agency.
https://www.jma.go.jp/jma/jma-eng/jma-center/nwp/outline2024-nwp/index.htm, 2024.
(Accessed: 22 September 2024).
Bent Jørgensen.The Theory of Dispersion Models. Chapman & Hall, 1997.
Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and
Tie-Yan Liu. Lightgbm: A highly efficient gradient boosting decision tree.Advances in neural
information processing systems, 30, 2017.
Diederik P Kingma. Adam: A method for stochastic optimization.arXiv preprint arXiv:1412.6980,
2014.
Atsushi Kudo. Statistical post-processing for gridded temperature prediction using encoder–decoder-
based deep convolutional neural networks.Journal of the Meteorological Society of Japan. Ser.
II, 100(1):219–232, 2022.
LightGBM Contributors. Lightgbm parameters.https://lightgbm.readthedocs.io/en/latest/
Parameters.html, 2026. Accessed: 2026-03-18.
Qi Liu, Xiao Lou, Zhongwei Yan, Yajie Qi, Yuchao Jin, Shuang Yu, Xiaoliang Yang, Deming Zhao,
and Jiangjiang Xia. Deep-learning post-processing of short-term station precipitation based on
nwp forecasts.Atmospheric Research, 295:107032, 2023.
OPTUNA. optuna.integration.lightgbm.lightgbmtuner; optuna 2.0.0 documentation.
https://optuna.readthedocs.io/en/v2.0.0/reference/generated/optuna.integration.
lightgbm.LightGBMTuner.html, 2024. (Accessed: 5 December 2024).
Ting Peng, Xiefei Zhi, Yan Ji, Luying Ji, and Ye Tian. Prediction skill of extended range 2-m
maximum air temperature probabilistic forecasts using machine learning post-processing methods.
Atmosphere, 11(8):823, 2020.
RISH. Welcome to rish www data server.http://database.rish.kyoto-u.ac.jp/index-e.html,
2024. (Accessed: 22 September 2024).
Adrian Rojas-Campos, Martin Wittenbrink, Pascal Nieters, Erik J Schaffernicht, Jan D Keller, and
Gordon Pipa. Postprocessing of nwp precipitation forecasts using deep learning.Weather and
Forecasting, 38(3):487–497, 2023.
Brian C Ross. Mutual information between discrete and continuous data sets.PloS one, 9(2):
e87357, 2014.
Andrés A Salazar, Yuzhang Che, Jiafeng Zheng, and Feng Xiao. Multivariable neural network
to postprocess short-term, hub-height wind forecasts.Energy Science & Engineering, 10(7):
2561–2575, 2022.
Ravid Shwartz-Ziv and Amitai Armon. Tabular data: Deep learning is not all you need.Information
Fusion, 81:84–90, 2022.
Rongnian Tang, Yuke Ning, Chuang Li, Wen Feng, Youlong Chen, and Xiaofeng Xie. Numerical
forecast correction of temperature and wind using a single-station single-time spatial lightgbm
method.Sensors, 22(1):193, 2021.
TensorFlow. Tensorflow.https://www.tensorflow.org/, 2024. (Accessed: 8 December 2024).
23

Evangelos Tsipis, Konstantina Banti, Malamati Louta, and Nikos Dimokas. Improving open
weather prediction data accuracy using machine learning techniques. In2023 14th International
Conference on Information, Intelligence, Systems & Applications (IISA), pages 1–8. IEEE, 2023.
Wenqing Xu, Like Ning, and Yong Luo. Wind speed forecast based on post-processing of numerical
weather predictions using a gradient boosting decision tree algorithm.Atmosphere, 11(7):738,
2020.
Takao Yoshikane and Kei Yoshimura. A bias correction method for precipitation through recognizing
mesoscale precipitation systems corresponding to weather conditions.PLoS Water, 1(5):e0000016,
2022.
Yuhang Zhang and Aizhong Ye. Machine learning for precipitation forecasts postprocessing:
Multimodel comparison and experimental investigation.Journal of Hydrometeorology, 22(11):
3065–3085, 2021.
24
