---
title: Evaluating and improving crop-yield forecasting methods during extreme drought
url: https://arxiv.org/abs/2608.17971
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Shrey Gupta
- Yi Ming
- George Mohler
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.17971
pages: 32
chars: 54773
fetched_at: '2026-11-08T13:30:15+00:00'
kb_version: 1
---

# Evaluating and improving crop-yield forecasting methods during extreme drought

Evaluating and improving crop-yield forecasting
methods during extreme drought
Shrey Gupta1*, Yi Ming1 and George Mohler1
1Boston College, US.
*Corresponding author(s). E-mail(s): shrey.gupta.skg@gmail.com;
Contributing authors: Yi.Ming@bc.edu; mohlerg@bc.edu;
Abstract
The impact of climate variability on food production has led to the creation of
various forecasting models that uses machine learning (ML), numerical weather
predictors (NWP) or a hybrid of ML-NWP models to identify structural and
physical relationships between meteorological drivers and crop growth, in order
to predict crop yield. Droughts, for example the 2012 Midwestern US (Corn Belt)
drought, are extreme events that affect crop production and test the limits of
these forecasting models. Using 16 meteorological drivers as predictors, we com-
pare ML (non-deep learning) and deep learning forecasting models to predict
the county-level corn yield for the extreme drought year, 2012. This forecasting
problem is characterized by a dissimilarity between the feature distributions of
the training and test data, where the meteorological conditions of the extreme
drought year fall outside the range of historically observed values. Additionally,
the dataset consists of spatial and temporal irregularities where counties with
missing yields introduce spatial sparsity and the use of only a subset of daily
values per year introduce temporal sparsity. To overcome this, we use sample
weighting and feature selection as modifications to improve our forecasting mod-
els. These modifications lead to an improvement for ML models; however, the
deep learning model VITA shows little to no improvement. While VITA outper-
forms the ML models with or without modifications, our current study sheds
light on the effect of dissimilarity between train and test feature distributions
on forecasting models, compares deep learning versus non-deep learning models,
and introduces modifications that are effective for non-deep learning models.
Keywords:Crop yield forecasting, Extreme events, Feature distribution mismatch
1
arXiv:2608.17971v1  [cs.LG]  18 Aug 2026

1 Introduction
Climate variability (natural fluctuations in climate) and anthropogenic climate change
(long-term shifts driven by human activity) has influenced the global agricultural pro-
ductivity by altering the frequency and intensity of extreme events such as droughts
and floods [1–3]. Among these extremes events, droughts are considered highly con-
sequential as they affect (reduce) the soil moisture, surface energy and hydrological
cycles. This directly impacts the crop yield with cascading economic and societal con-
sequences [4]. The 2012 year drought that took place in the Midwestern United States
(US) (also called the Corn Belt) was one of the most severe droughts witnessed by the
region in the last 50 years. It affected over 80% of the contiguous United States and
reduced the national corn yields for that year by approximately 13% [5].
A range of approaches exist for crop yield forecasting that include statistical learn-
ing, machine learning (ML), and deep learning (DL) models[6–13]. We consider ML
and DL models as two independent sets where the former does not use neural net-
works. These ML and DL models struggle to forecast extreme events (droughts, floods,
and more) as the data consist of very few representative samples. This under repre-
sentation is caused due to (1) a dissimilarity between the feature distributions of the
training and test data, where the meteorological conditions of the extreme drought
year fall outside the range of historically observed values, and (2)Data irregulari-
ties, a scenarios where missing spatiotemporal data affects the model’s performance.
For conceptual shorthand, we refer to this dissimilarity between train and test fea-
ture distributions asfeature distribution mismatchthroughout this study.Therefore,
the goal of this study is to evaluate and improve the performance of yield
forecasting models during extreme drought by considering it a feature
distribution mismatch and data irregularity problem.
Much of the recent progress in crop yield forecasting has been driven by using
large neural networks and rich training datasets with the assumption that performance
2

improves under scaling laws, i.e., model and dataset size [14], even for extreme events.
While solutions based on scaling improves the forecasting model’s performance, they
remain a black box as they are unable to explain the underlying agroclimatic processes
that affect crop yield. Therefore,we answer the following three questions in this
work: (1) How do ML and DL models perform under feature distribution
mismatch and data irregularity constraints and does the model complexity
impact generalization (prediction performance)? (2) Are meteorological
drivers in the data enough to capture the variations in the crop yield
and which drivers are most useful in capturing these variations? (3) Do
explainable AI techniques further improve the model performance?
Our study addresses the problem of accurately estimating annual county-level corn
yield under the constraints of feature distribution mismatch and data irregularities
and utilizing only meteorological drivers to analyze the performance of the forecast-
ing models. The data consists of annual county-level corn yield combined with daily
meteorological drivers (features) across the Midwestern US. The data irregularities
emerge due to inconsistency in (1)spatial coverage(spatial irregularities) from missing
county-level yield data, and (2)temporal coverage(temporal irregularities) as daily
measurements do not span the full year. We improve the model performance by using
sample weighing and selecting important features derived using the SHAP analysis.
In Section 2, we discuss the relevant background and related work in this problem
space. Then we discuss the model and modifications employed in Section 3 and their
forecasting results in Section 4. Our study’s takeaway and future work is discussed in
Section 5.
2 Background and Related Works
Crop yield is a challenging prediction problem, as yields are affected by a confluence of
meteorological drivers, land-use patterns, and crop management practices where each
3

(a) Gridmet data coverage
 (b) NASA Power data
Fig. 1: Region of coverage for (a) Gridmet data (US Cornbelt) with counties where
grey are the total number of counties and green are the available county data from
the year 2012, and (b) NASA Power data (North and South America) with 5x8 grids.
vary across space and time. Meteorological drivers influence yield indirectly compared
to the dependent factors such as soil properties, crop physiology, and management
practices [15]. However, these meteorological drivers alone are able to explain greater
than one-third of yield variability [16–18], which is a motivation to study the impact
of these variations on the crop yield when observations are in-situ and aggregated over
a large area (US county). Previous studies have introduced ML and DL frameworks
that forecast the 2012 drought in the Midwestern US. In the following sections, we
discuss the various yield forecasting models from the literature as well as the datasets
used – gridMET and NASA power.
gridMET Dataset
The gridMET dataset [11, 19] spans the US Corn belt, that is geographically located
between latitudes 35.58°to 49.58°and longitudes 80.8°to 102.8°, and includes 1,413
counties as shown in Figure 1a. The dataset spans 1980 to 2018 and consist of two
types of data irregularities: spatial irregularities due to missing yields across certain
4

counties and years, and temporal irregularities, as the daily measurements only cover
the crop phases, sowing, growing, and harvesting phases, than the complete year. The
county-level corn yields were obtained from the USDA National Agricultural Statistics
Service and the daily meteorological data of the gridMET dataset was collected and
processed by Abatzoglou et al. [20] at a 1/24°(∼4 km) resolution. The dataset includes
16 meteorological drivers (features), namely specific humidity, mean vapor pressure
deficit, precipitation, minimum and maximum relative humidity, downwelling solar
radiation, minimum and maximum air temperature, wind speed and direction, refer-
ence grass and alfalfa evapotranspiration, energy release component, burning index,
and 100-hour and 1000-hour dead fuel moisture (FM100 and FM1000). The crop
phases cover 210 days ranging from 10 April to 6 November per year.
Nasa Power Dataset
The NASA Power dataset, generated using the NASA Power API by Hasan et al. [21],
contains 39 years (1984-2022) of data at 0.5°spatial resolution. It is used by the VITA
(Variational Inference Transformer for Asymmetric data) model [21] as a pretraining
dataset. Whereas, the gridMET dataset is used for finetuning and forecasting. The
NASA Power dataset consists of 116 grid tiles (160 geo-referenced points per tile)
spanning the Americas as shown in Figure 1b. It includes 31 meteorological drivers
measured at daily granularity, normalized to a sequence length of 365 per year, with
missing values backward filling and leap year days omitted. These daily sequences are
then aggregated to weekly measurements and standardized using the mean and stan-
dard deviation of the continental US, which generates approximately 100K sequences,
that are used for pretraining the model.
Yield F orecasting
There exist numerous studies that focus on crop yield forecasting using various ML
models [6–13, 22]. Therefore, a critical open question is then determining models,
5

trained on meteorological features, that are useful forecasters during extreme droughts.
It should be noted that the data used in these studies usually contain high-resolution
satellite or in-situ data or a combination of both. Within the in-situ data, there
are both meteorological and land-use drivers, such as soil moisture, that directly
impact the crop yield. For this problem, we focus on the transfer learning model,
Tradaboost.R2, extreme-value model,Extreme Lasso, and the deep learning model,
VITA[21]. These models show promise given the drought scenario when only meteo-
rological drivers are present, and the dataset consists of spatiotemporal irregularities.
In the following sections, we elaborate on the studies that use forecasting models for
yield prediction during extreme droughts.
2.1 Crop yield forecasting models
Zhong et al. [23] provides a multi-task learning framework that embeds attention in
a LSTM architecture to capture seasonality and periods of extreme stress during the
crop growing phases. Their model shows a strong yield forecasting performance where
the drought indicator (derived feature),Killing Degree Days, which measures heat
stress experienced by crop, is the indicative feature for variations in the yield. However,
their dataset consists of meteorological, soil, and vegetation index (NDVI) drivers that
improves their model’s performance in capturing high spatiotemporal variability. Xu
et al. [24] utilize a similar heterogeneous and rich dataset with meteorological, soil, and
management practice drivers, to forecast corn yield. They determinevapor pressure
deficit(VPD) and temperature as major meteorological drivers of yield variability
and soil’s water capacity and organic matter content as land drivers. Shahhosseini et
al. [25] show that combining ML models with process-based models can improve the
accuracy of crop yield prediction. They do this by using outputs of these process-based
models like DSSAT [26] as inputs to the ML models. The process-based model output
is calculated using important indicators such as soil-water balance, phenology, and
6

canopy development. While the above models have a strong forecasting performance,
they utilize a rich heterogeneous dataset, compared to our study that focuses on
answering yield variability captured by meteorological drivers for extreme events.
2.2 Drought forecasting models
Drought indicators are derived features that quantify the onset, and intensity of
drought conditions. Several studies focus on forecasting these indicators rather than
yield or soil moisture. Brust et al. [27] introduce Droughtcast, an LSTM model, to pre-
dict Evaporative Stress Index (ESI), for forecasting flash droughts. The authors use
meteorological drivers and vegetation indices to predict upcoming changes in drought
conditions. Their model effectively captures the rapid transitions that indicate flash
droughts by learning temporal patterns indicative of the decline in Evaporative Stress
Index (ESI). Similarly, Deangelis et al. [28], evaluate forecasting performance for the
Subseasonal Experiment (SubX) models to capture the rapid intensification of the
2012 US drought. The SubX models showed low forecasting performance for spring and
early-summer precipitation deficits and moderate forecasting performance for temper-
ature anomalies, leading to a failure in anticipating the final drought patterns. While
these studies demonstrate the use of drought indicators such as ESI (remote-sensing
based), NDVI (vegetation based), and more, for capturing land-atmosphere dynamics,
our setting is intentionally constrained to meteorological drivers.
3 Methodology
We first introduce the models we use for our comparative study along with the feature
engineering and model modifications we use in combination with the existing models.
7

3.1 Prediction Models
For our experiments, we consider a roster of machine learning models and the deep
learning model, VITA. Our goal here is to compare various forecasting models that
use kernels, trees, heuristics to overcome extreme-values, and transfer learning. VITA
(Variational Inference Transformer for Assymetric data) is a more recent DL model
that forecasts crop yield. It has shown promise to identify and capture similar drought
patterns in the dataset, i.e. temporal sequences of meteorological drivers, similar to
the test (drought) year, using its variational inference and attention architecture.
The ML models we use differ in how they learn the relationship between the fea-
tures and the labels where the features (meteorological drivers) are standardized before
modeling. For a given feature vectorx i, the model prediction is denoted as ˆyi =f(x i)
and the corresponding residual isr i =y i −f(x i), wherey i is the observed target
value. A model is denoted using the functional form,f(·), and the loss function is
defined over the residuals (r i) between the model outputs (f(x i)) and the observed
ground-truth (yi).
Machine learning models:
For the machine learning models, we assume a linear relationship between the fea-
tures and the target, such that the model output isf(x i) =x ⊤ i β, whereβare the
coefficients. We use approaches such asRidgeandLasso, which apply regularization
(L2 and L1, respectively) for generalization. In Ridge regression, the coefficientsβare
calculated by minimizing the L2 regularized squared–error loss,
LRidge(β) = 1 n
nX
i=1
(yi −x ⊤ i β)2 +λ∥β∥ 2 2
8

Whereas, in Lasso regression, the coefficientsβare calculated by minimizing the
L1 regularized squared–error loss,
LLasso(β) = 1 n
nX
i=1
(yi −x ⊤ i β)2 +λ∥β∥ 1.
wherenis the total number of training samples,λis the regularization parameter
that controls the penalty applied to the coefficients,∥β∥ 2 2 and∥β∥ 1 are the squared
ℓ2 andℓ 1 norm respectively.
We use tree-based models,Random F orestandGradient Boosting regressor,
which do not assume a linear relationship forf(·), but instead recursively partition the
feature space to learn predictions. Each tree in the Random Forest minimizes the mean-
squared error,L tree = 1 nT P i∈T (yi − ˆyi)2 ,where a single decision treeT(·) is denoted
by ˆyi =T(x i), andn T denotes the number of samples in the node. The Random
Forest model hasMtrees where the ensemble prediction is defined as,f RF(xi) =
1
M
PM
m=1 Tm(xi)
We use a kernel-based model,Support V ector Regressor (SVR), which uses
kernel function to operate in a reproducing kernel Hilbert space. We use a linear kernel
k(xi,x j) =x ⊤ i xj, such that the prediction function isf(x i) = Pn j=1 wj k(xj,x i) +b=
w⊤xi +b.
LSVR(β) = 1 2 ∥w∥2 2 +C
nX
i=1
Lϵ

yi −f(x i)

,
whereL ϵ(r) = max

0,|r| −ϵ

is theϵ-insensitive loss,C >0 is the regularization
parameter, andϵ >0 controls the insensitivity, such that —r— is the error.
We use extreme-value model,Extreme Lasso[29] andHuber regression[30].
Letr i =y i −x ⊤ i βbe the residuals (error) andδ >0 be the threshold (also known as
Huber threshold) for the Huber model. The loss for a single residual in the model is
9

defined as,
ρδ(r) =



1
2 r2,if|r| ≤δ,
δ

|r| −1 2 δ  ,if|r|> δ,
and the loss function for Huber regression is defined as
LHuber(β) = 1 n
nX
i=1
ρδ

yi −x ⊤ i β  .
Similarly for the Extreme Lasso model,γ >2 represents the weight given to the
extreme residuals. The loss function for the model can then be written as,
LExtremeLasso(β) = 1 n
nX
i=1

yi −x ⊤ i β

γ +λ∥β∥ 1,
whereλ >0 controls theL 1 regularization strength.
Transfer learning models are known to handle feature distribution mismatch
observed when the test data is a different domain. We useT rAdaBoost.R2, a
boosting-based regression transfer approach that combines the source data (domain
to learn from; large sample set) and target data (domain to predict upon; fewer sam-
ple set) and reweights source samples that are dissimilar to the target samples [31].
If the source and target domains are,D S ={(x S i , yS i )}nS i=1 andD T ={(x T j , yT j )}nT j=1,
wherew (t) S,i andw (t) T,j denote the weights at each boosting iterationt. At iterationt,
TrAdaBoost.R2 learns a base regressorh t :R d →R, similar to the prediction function
f(·), by minimizing the weighted normalized absolute error as,
L(t)(β) =
nSX
i=1
w(t) S,i e(t) S,i +
nTX
j=1
w(t) T,j e(t) T,j ,
wheree (t) S,i =

yS i −h(xS i )

D(t) ,e (t) T,j =

yT j −h(xT j )

D(t) andD (t) = max k

yk −h(x k)

. After
training theh t learner, the weights are updated differently for target and source
10

points to focus on high residual target samples and dissimilar source samples. For a
normalization constantZ t and a transfer parameterβ∈(0,1), the updates are
w(t+1) T,j = w(t) T,j β−e(t) T ,j Zt , w (t+1) S,i = w(t) S,i β e(t) S,i Zt .
Hence, the source samples with larger residualse (t) S,i are exponentially down-weighted
over iterations, while the target samples are up-weighted.
Deep learning model:
We use VITA [21], which is a decoder-free variational transformer model, which learns
latent weather representations from the satellite data during pretraining and trans-
fers the learned weather representation to a sparse subset of features at finetuning.
The yield for a sampleiis represented as ˆyi =f VITA(xi;θ),wherex i denotes the
meteorological drivers andθrepresents the neural network parameters to be learned.
The input for the pretraining stage consists of a weekly time-series,x={x t}T t=1,
such thatx t ∈R 34,where the number of meteorological drivers is 31 along with spa-
tial and temporal features (latitude, longitude, and year), andT= 364 denotes the
sequence length. At each timestept, the input feature vectorx t ∈R 34 is first mapped
to a higher-dimensional embedding space via a linear projection,e t =Wx t +b, where
W∈R 200×34 andb∈R 200. To preserve the temporal order of the sequence, a sinu-
soidal positional encodingp t ∈R 200 is added to the embedding as, ˜et =e t +p t, which
allows the Transformer encoder to recognize different timesteps. Next, the embedded
sequence{ ˜et}T t=1 is processed by a Transformer encoder with four layers.‘ Each layer
consists of multi-headed self-attention (10 heads) and a position-wise feedforward net-
work of width 800 with GELU activations and residual connections, that generates
the contextual representation,h t ∈R 200.
The contextual representationsh t ∈R 200 produced by the Transformer encoder
summarizes the meteorological conditions at each time stept, and also accounts for
11

temporal dependencies present in the sequence. These contextual representations are
then mapped into a latent space that captures the underlying meteorological conditions
in a probabilistic manner. VITA achieves this by assuming that at each time stept,
the latent weather statez t ∈R 31 follows a Gaussian variational posterior distribution
conditioned on the input sequence,
qϕ(zt |x t) =N

µt,diag(σ 2 t )  ,
whereϕdenotes the parameters of the variational inference network. The mean vector
µt represents the inferred latent weather state at timet, while the diagonal covariance
diag(σ2 t ) quantifies uncertainty associated with this inference. The parametersµ t and
logσ 2 t are obtained via a linear projection of the Transformer outputh t fromR 200 to
R62, split equally into mean and log-variance. The variance is enforced to be positive
through the exponential transformation,
σ2 t = exp  logσ 2 t  .
This variational formulation allows the model to represent meteorological condi-
tions as distributions rather than deterministic embeddings, which allows to capture
uncertainty in the sequences.
During the pretraining stage, VITA is trained in a self-supervised manner using
only meteorological drivers as inputs. A subset of these drivers is randomly masked
across all timesteps, and the model reconstructs the masked values from the latent
variablesz={z t}T t=1. This forces the latent space to capture coherent temporal and
cross-feature dependencies. The pretraining loss function is defined as
Lpretrain =−logp(x masked |z) +αKL (qϕ(z|x)∥p(z) ) ,
12

where the first term corresponds to a Gaussian negative log-likelihood over the masked
entries. The second term is the Kullback–Leibler divergence between the variational
posterior and the seasonality-aware prior, weighted byα, which regularizes the latent
representations and prevents deviation from physically plausible seasonal patterns.
For yield prediction, the pretrained Transformer encoder is reused to infer latent
states{z t}T t=1. These states are aggregated using a learned temporal attention
mechanism. First, scalar attention scores are computed as
st = MLP(zt),
where MLP is the Multi-layer Perceptron. This is followed by normalizing attention
weights,α t = exp(st)PT
k=1 exp(sk) .The aggregated latent representation is then
¯z=
TX
t=1
αtzt, ¯z∈R 31.
The attention MLP has architecture 31→16→1 with GELU activation, pro-
ducing a scalar weightα t per timestep. The latent vector ¯z= P t αtzt ∈R 31
is concatenated withn past historical yield values, capturing soil and management
effects. This combined representation is passed through a yield prediction MLP with
architecture,
(31 +n past)→120→1
with GELU activation to produce the final yield, ˆyi. During fine-tuning, the recon-
struction term is disabled, and the model is optimized using a mean-squared error loss
with a KL regularization term retained to preserve the pretrained latent structure,
Lfinetune = 1 n
nX
i=1
(yi − ˆyi)2 +βKL (qϕ(z|x)∥p(z) ) .
13

3.2 Data and model adaptation
We describe the preprocessing steps applied to the gridMET dataset for regres-
sion modeling, the explainability analysis used for feature selection, and the sample
reweighting applied to extreme event years. We apply these collectively across our
models and refer to them as data and model adaptation.
F eature Engineering
The gridMET dataset consists of 210 days of meteorological observations (drivers)
per county per year. For the ML models, we aggregate the daily observations into
a rolling 3-month seasonal window spanning from April to October. For each win-
dow, we compute summary statistics such as the window’s mean, standard deviation,
minimum & maximum values, quartiles, skewness, and kurtosis capturing the dis-
tribution’s variance. We also expand the yield feature using its historical values to
introduce features such as previous 5-year yield mean as well as minimum, maximum,
mean, standard deviation and trend for the all the previous yield years. We avoid
time-series detrending methodologies such as windowed averaging, linear regression,
and more. Dessavre et al. [32] argue that detrending either over-smooths (reduces
variance) or under-smooths (increases oscillations) the time-series, and consequently
destroying the structure of the series. Instead we use the trend feature that captures
the change (increase/decrease) in yield for each county.
Explainability analysis
SHAP (SHapley Additive exPlanations) [33] is a model-agnostic explainability
methodology that uses game theory to identify essential features for forecasting. It
computes Shapley values, which represent the average marginal contribution of each
feature to the model’s predictions across all possible feature combinations, thereby
determining feature importance. We first aggregate the features annually (across the
210 days) and subsequently train a Lasso regression model on samples before 2007,
14

(a) SHAP:2012.
 (b) SHAP:2013.
Fig. 2: SHAP analysis for the test years (a) 2007 to 2011 trained on historical years
before 2007 and (b) 2008 to 2012 trained on historical years before 2008. Impact on
model output (x-axis) equates to yield (bushels/acre).
testing on the window from 2007 to 2011. While we aim not to use the extreme event
year (2012) directly, the 5-year test window allows us to identify short-term meteo-
rological drivers that influence yield forecasting. Figure 2 shows the SHAP summary,
which identifiesvapor pressure deficit(VPD) andevapotranspiration(ETR) as the
most influential meteorological drivers for yield forecasting during 2007 to 2011, while
other drivers show little to no influence.
Extreme event years weighting
We additionally identify 4 previous extreme event years in the U.S. Corn Belt – 1983,
1988, 1993, and 2002 – that substantially impacted crop production. These years wit-
nessed high moisture deficits and heat stress during the growing season that resulted
in significant yield reductions. We apply weighting and attention to the samples of
these years in our models to improve forecasting.
15

Fig. 3: Capturing attention using line plots (top) and heatmaps (bottom), where
the heatmaps (legend: colorbar) represent the average attention weights for the year.
The 4 plots are for (a) 2012 year with all features (VITA), (b) 2012 year with SHAP
features (VITA[+]), (c) 2013 year with all features (VITA), and (d) 2013 year with
SHAP features (VITA[+]).
Model adaptation
The SHAP-selected features are applied across both ML and deep learning models.
However, extreme years sample weighting and attention is only applied to
T radaboost.R2 and VIT A models.
Since Tradaboost.R2 requires source and target datasets, we split the training data
(data before 2012) strategically. The samples from the extreme event years and the
previous 5 years (2007 to 2011) are considered as the target dataset, and the remaining
sample from the training dataset are considered as the source dataset. The choice
of the target dataset is intentional as it allows the model to focus on samples that
experience the feature distribution mismatch (extreme event years) as well as capture
time-series trends from previous 5 years (since Tradaboost.R2 is a boosting based
model). We refer to this modified model as Tradaboost.R2[+].
For the VITA model, we assign higher weights to extreme years and introduce
an attention bias toward the meteorological conditions of 2012’s sowing and growing
season; we refer to this adapted model as VITA[+]. It modifies the fine-tuning loss
16

function by introducing a per-sample importance weightw i,
LVITA[+] = 1 n
nX
i=1
wyear i (yi − ˆyi)2 +βKL (qϕ(z|x)∥p(z) ) ,
wherew year i >1 for the identified extreme years 1983, 1988, 1993, and 2002, and
wyear i = 5.0 for the 2012 extreme year. To bias training toward 2012’s meteorological
conditions, VITA[+] computes a drift-distance using the SHAP-identified VPD fea-
ture. Note that ETR is excluded here as the NASA Power dataset does not contain
ETR measurements mappable to the gridMET dataset. Using 2012’s sowing and grow-
ing season window (weeks 15 to 35), we construct a reference distribution (µ ref, σref)
from VPD. For each training samplei, the VPD sequence is constrained to the same
growing-season window, and the distance at each timestep is computed as
δi,t =

 VPDi,t −µ ref σref

 ,
with the drift-distance for each sample obtained by averaging over timesteps,
di = 1 |Ti| X t∈Ti δi,t
The base VITA model computes attention as,
si,t = MLP(zt), α i,t = exp(si,t) PT
k=1 exp(si,k)
.
VITA[+] modifies the attention scores by subtracting the scaled drift-distance,
s+ i,t =s i,t −λ attn di, λ attn = 0.5, yielding the adapted attention weights,
α+ i,t = exp(s+ i,t) PT
k=1 exp(s+ i,k) .
17

This biases attention toward weeks whose VPD distribution most closely resembles
the 2012 growing season.
4 Evaluation
We evaluate the model performance based on 4 performance metrics described below.
We also elaborate on the modeling parameters for (1) All features and (2) SHAP
features. Our results validate the model performance on extreme drought and normal
year with the VITA model’s attention weights explored for each year.
4.1 Metrics
We evaluate the performance of the machine learning models using 4 metrics: Coeffi-
cient of determination (R2), Root Mean Squared Error (RMSE), bias, and variance.
The R2 measures the variance in the observed values that the model can capture. It
is defined asR 2 = 1−
Pn
i=1(yi−ˆyi)2 Pn
i=1(yi−¯y)2 , wherey i is the observed value for thei-th sam-
ple and ˆyi is the model predictions. The Root Mean Squared Error (RMSE) measures
the square root of the average of the squared difference between observed and pre-
dicted values as, RMSE =
q
1
n
Pn
i=1(yi − ˆyi)2. The bias is the mean of the prediction
errors, Bias = 1 n Pn i=1 ei, wheree i =y i − ˆyi denotes the prediction error for sample
i. A positive bias indicates underprediction and a negative bias indicates overpredic-
tion. The variance is how the residuals vary around their mean and is calculated as
Variance = 1 n Pn i=1(ei − ¯e)2, where a high variance means that the model has varying
performance across different observed values. Hence, Mean Squared Error can also be
written as, MSE = Bias 2 + Variance.
4.2 Model Parameters
The performance of the models is compared on two test scenarios, (1) theextreme
drought year(2012) and (2) thenormal year(2013) to compare model performance.
18

Each model is evaluated under two feature subsets: using all available features and
SHAP features.For Tradaboost.R2 and VITA, the SHAP feature setting in Table 1
corresponds to models Tradaboost.R2[+] and VITA[+] inculcated with their respective
modifications as described in Section 3.2.
4.2.1 Extreme drought year (2012)
All models use standardized features and a 20-fold cross-validation. The baseline Lasso
model (Lasso 80:20) usesα= 0.5 (All features) andα= 0.05 (SHAP features)
for its L1 penalty. The Lasso regressor usesα= 0.005 (All features) andα= 0.1
(SHAP features) for its L1 penalty; Ridge regression usesα= 0.5 (All features) and
α= 500.0 (SHAP features) for its L2 penalty. The Random Forest regressor uses 200
estimators, a min sample split size of 2, and a min sample leaf size of 1 (All fea-
tures & SHAP features). The XGBoost regressor uses 500 estimators, a learning rate
of 0.05, and a mean squared error loss function (All features & SHAP features). The
Support Vector Regressor (SVR) uses a linear kernel whereC= 10.0 (All features)
andC= 0.1 (SHAP features),ϵ= 0.1, and max iterations = 5000. For the Trad-
aboost.R2, we use Ridge regressor as base estimator (α= 500.0,n estimators = 2.0)
with the target domain having the previous 5 years from 2007 to 2011 (All features)
andα= 1000.0,n estimators = 4) (SHAP features) with the target domain having
years as{1983,1988,1993,2002,2007,2008,2009,2010,2011}. The source domain is
the remaining pre-2012 years. The Huber regressor uses the Huber lossδ= 1.35 and
L2 penalty asα= 0.01 (All features & SHAP features). The Extreme Lasso regres-
sor usesγ= 3 withλ= 0.001, a learning rate ofη= 10 −5, for 2000 iterations (All
features & SHAP features).
4.2.2 Normal year (2013)
For testing on the normal year, all models were similarly standardized as before and a
20-fold cross-validation was used. The Lasso base regressor usesα= 0.05 (All features)
19

andα= 0.05 (SHAP features) for its L1 penalty. The Lasso regressor usesα= 0.05
(All features) andα= 0.05 (SHAP features) for its L1 penalty. For the Tradaboost.R2,
we use Lasso regressor as base estimator (α= 1.0,n estimators = 1) with the target
domain having the previous 5 years from 2008 to 2012 (All features) andα= 1.0,
nestimators = 2) (SHAP features) with the target domain having only normal previous
years,{2007,2008,2009,2010,2011}. The source domain is the remaining pre-2012
years.
4.2.3 Extreme drought & Normal year for VIT A model
The VITA model is fine-tuned on the checkpoint using the ’small’ pretrained model
with the following architecture (for both 2012 and 2013 years): a Transformer
encoder withL= 4 layers,H= 10 attention heads, hidden dimensiond= 200
(hidden dim factor= 20,d= 20×10), and feedforward dimension 4d= 800. The
sinusoidal prior usesk= 1 seasonal component. A lightweight attention pooling head
(Linear(d, 16)→GELU→Linear(16, 1)) reduces the sequence to a fixed-size repre-
sentation, which is concatenated withn past = 5 prior-year yields and fed to a two-layer
yield MLP (Linear(d+ 6, 120)→GELU→Linear(120, 1)). The model is trained for
40 epochs with Adam (lr = 10 −4, 10 warmup epochs), batch size 16, minimizing the
ELBO withβ= 10 −4, wherep(z) is the learned sinusoidal prior. Historical extreme
years{1988,1993,2002}receive a weight = 3.0 (no 1983 since VITA pretraining starts
from year 1984). For training, we uses prior 28 years data, with 5-fold cross validation.
The source code can be accessed at:github.com/shrey-gupta/soil-land-crop
4.3 Results
We first compare all models on the extreme year 2012, and then select the two best-
performing models along with the Lasso baseline for analysis on the normal year
2013. Table 1 reports R 2, RMSE, bias, and variance for each model under the two
feature subsets: (1)All featuresand (2)SHAP features(VPD and ETR). The baseline
20

T able 1: Performance comparison for extreme (2012) and normal (2013) years
All F eatures SHAP F eatures
ModelR 2 RMSE Bias √ V ar.R 2 RMSE Bias √ V ar.
Extreme Y ear (2012)
Lasso (80:20) 0.788 19.0 -1.96 18.9 0.808 18.1 -0.09 18.1
Lasso 0.411 31.4 3.13 31.2 0.459 30.1 -2.70 30.0
Ridge 0.382 32.1 -7.25 31.3 0.438 30.6 -6.02 30.0
Support Vector 0.418 31.2 -4.12 30.9 0.434 30.8 -6.26 30.1
Random Forest 0.140 37.9 19.3 32.6 0.142 37.9 18.4 33.1
(X)GB 0.220 36.1 17.1 31.8 0.269 35.0 14.4 31.8
Huber 0.430 30.9 -0.403 30.9 0.440 30.6 -3.34 30.4
Tradaboost.R2 0.399 31.7 -3.44 31.5 0.490 28.2 -5.43 28.7
Extreme Lasso 0.045 40.0 -1.75 39.9 0.059 39.7 -24.4 31.3
VITA 0.559 27.1 4.15 26.8 0.560 27.1 1.53 27.1
Normal Y ear (2013)
Lasso 0.403 23.9 -15.3 18.4 0.496 25.7 -7.14 24.6
Tradaboost.r2 0.356 24.9 -15.9 19.1 0.421 23.6 -13.9 19.0
VITA 0.581 20.0 -5.68 19.2 0.593 19.7 -6.99 18.5
regression model, Lasso (80:20), is trained and tested on the extreme drought year
data using an 80:20 split. It is a useful upper-bound for the comparative models.
4.3.1 Extreme Drought Y ear (2012)
All models are trained on the years 1980 to 2011, and tested on the year 2012
as shown in Table 1. We observe that the models trained on only SHAP features
show an improvement in prediction performance. It should be noted that both VITA
and VITA[+] have comparable perfromace (R2 and RMSE scores) and the VITA
model, without any modifications, outperforms all competitive models.These results
validate our questions raised in the Section 1: (1) VIT A, a large-scale
DL model, performs well under feature distribution mismatch and data
irregularities unlike classical ML models. (2) Models trained only on mete-
orological drivers are able to explain more than half the variations in
the crop yield. (3) Classical ML models require feature engineering and
selection (SHAP) to improve their forecasting performance.Conventionally
precipitation and temperature are considered important drivers for estimating crop
21

yield, however, the SHAP analysis recognizes VPD and ETR as influential drivers as
they include the combined effects of temperature, humidity, and radiation. Addition-
ally, we believe that data irregularities further suppresses the relationship between
precipitation/temperature and yield as the effects of these meteorological drivers can
be captured using the full annual cycle.
4.3.2 Normal Y ear (2013)
We validate the modified models on the normal year (2013) using Lasso, TrAd-
aBoost.R2, and VITA models as shown in Table 1. VITA[+] has the best forecasting
performance. Unlike the extreme drought year, TrAdaBoost.R2[+] does not show an
improvement over TrAdaBoost.R2 using SHAP features. This suggests that transfer
learning models are most effective when the target and source datasets are dissimilar
such as the feature distribution mismatch that exists for the 2012 yield forecast-
ing. Since, 2013 year does not consists of such mismatch, the underliying domain
adaptation model which Tradaboost.R2 utilizes, is ineffective.
4.3.3 Analyzing Attention for VIT A
In Figure 3, we analyze the attention weights given by the VITA model during the
finetuning stage with a context window of 5 years. Each plot consists of a line plot
representing the attention weights for the test year and a heatmap of the weights for
the 5 year context window. In Figure 3(A) to (D), we observe that both VITA and
VITA[+] models have higher attention for weeks 25 to 33, i.e., the months June to July
(growing season for the corn). This is most pronounced in Figure 3(b), where attention
is almost entirely focused on these weeks. The fact that VITA consistently emphasizes
the growing season across both 2012 and 2013 validates its attention mechanism, where
it learns to prioritize growing phase months using self-supervision.
22

T able 2: Ablation study
ConfigurationR 2 RMSE Bias √ V ar.
VIT A[+]
All features, no attention, weights 0.540 27.7 0.598 27.7
VPD only, attention, no weights 0.554 27.3 4.00 27.0
VPD only, no attention, no weights 0.524 28.2 5.75 27.6
T radaBoost.R2[+]
All features, weights 0.372 32.4 -1.87 32.3
SHAP features, no weights 0.478 29.5 2.65 29.4
4.4 Ablation Study
We disseminate methodological modifications of VITA[+] and Tradaboost.R2[+] using
the ablation study shown in Table 2. There are 3 variations of VITA[+] model that
we use for the ablation experiments. The first one usesVIT A[+]model withyear
weights = 3.0,all featuresandattention =0.0 for the growing season. The second
usesVIT A[+]model withno year weights,VPD featureandattention =0.5
on the growing season. The third usesVIT A[+]model withno year weights,VPD
featureandattention =0.0. From the VITA[+] ablation results, we observe that not
having year weights, or feature attention, affects the model’s performance. Moreover,
attention on the growing season has the most effect on VITA[+]’s performance. It
should be noted that VITA still outperforms all variations of VITA[+] (comparing
Table 4 and Table 2), validating the fact that year weights and attention over the
growing season are useful when applied together as modifications.
Similarly, there are 2 variations of the TrAdaBoost.R2[+] model in the ablation
experiments shown in Table 2. The first uses theT rAdaBoost.R2[+]model with
all features,extreme year weightsandα= 5000.0. The second uses theT rAd-
aBoost.R2[+]model withSHAP features,no extreme year weightsand and
α= 500.0. From the Tradaboost.R2[+] ablation results, we see that the SHAP fea-
tures (VPD, ETR) play an important role for improving the performance whereas
23

(a) Plot showing performance of Lasso regressor when the
samples from test data (2012 year) varies from 5 to 20 along
with their weights.
(b) Map plot for the 20 coun-
ties (samples) where sampling
is random v. stratified.
Fig. 4: Machine learning using ’few’ test data samples.
extreme year weights actually reduce the performance when tagged with all features,
highlighting the importance of applying the two modifications together.
4.5 Machine learning using ’few’ test data samples
We extend our experiments by using ’few’ data samples from the extreme years as
shown in Figure 4. We use 5 to 30 samples selected randomly where weights varying
from 5 to 200 is assigned to each of them and the Lasso regressor withalpha= 0.05
is used. In Figure 4a, we observe that forn= 20, the model has the best perfor-
mance which improves with the weights for the samples. We also plot these 20 samples
(counties) in Figure 4b, where counties highlighted in blue are the randomly selected
20 samples. Based on these results, we performed stratified sampling forn= 20 data
samples (counties). To ensure an equal coverage, we first sorted the counties based on
the mean of the growing-season (April–August) of vapor pressure deficit (VPD). Then
we selected 20 counties via uniform sampling across the sorted counties. The results of
this sampling is present in Figure 4a and the (black) highlighted counties in Figure 4b.
While stratification can be performed in numerous ways such as selecting large num-
ber of VPD stress counties, our motivation was to improve generalizability. We observe
that the model with stratified sampling underperform compared to random sampling
24

(a) Annual aggregated values of features across all coun-
ties
(b) Density plots for extreme and
normal years
Fig. 5: Measuring feature distribution mismatch for the extreme event years using (a)
Aggregated annual feature values across all counties over the years, (b) Density plot of
daily values for extreme (2012 and 1993) and normal (2009) years across all counties.
in Figure 4a indicating that yield variability cannot be solely determined using VPD
stress on crops.
These experiments give insights into the advantages of having ’few’ labeled county
data for the extreme drought year. While having meteorological data from the growing
season is possible for forecasting the yield variability, there still remains the question
of knowing the optimal number of ’few’ test samples (nranging from 5 to 20) that
requires the labeled test data itself.
5 Discussion and Future Work
The gridMET dataset has spatiotemporal irregularities that are common across
environmental and climate science domains and consequently shapes the goal of this
study. Since our models are adapted to work with feature distribution mismatch sce-
narios, we first discuss how changes in data distribution is observed for the extreme
25

drought year. We then discuss the data and modeling extensions that the future work
can entail.
F eature distribution mismatch
As defined previously, feature distribution mismatch is observed when the feature
distribution of the training and test datasets differ. In Figure 5, we observe how the
feature values change over the years where Figure 5(a) shows the number of standard
deviations by which the aggregated feature value (aggregated across days and counties)
deviates from the mean across all the years. We use the z-scores to measure deviations
from the mean and observe that 2012 show large deviations, especially for the SHAP
features VPD (Vapor Pressure Deficit) and ETR (Evapotranspiration). Moreover, not
all features show such deviations from the mean like Precipitation (PR) and Minimum
temperature (TMMN) which are less skewed compared to their observed values for
the years 1992 and 1998.
We observe a similar trend in the density plot shown in Figure 5(b) which cal-
culates the standard deviation for a feature across all counties in a given year. We
compare three years – 1993 (extreme drought year), 2009 (normal year) and 2012
(extreme drought year). Then we bin them using 60 bins and clip values more than
the 99th percentile to avoid long tails and improve visual representation. We observe
that VPD and ETR show a heavy tail compared to the normal year (2009) and the
extreme drought year (1993). While a deviation from the normal year is expected, it
is interesting to see the deviation of 2012 from an earlier extreme drought year, 1993.
This also validate the claim that the 2012 year has samples with more extreme values
than observed historically.
Overcoming Data Scarcity
Data availability and granularity are central to effective modeling. Even robust mod-
els can underperform when training data is scarce, though open-source datasets and
26

collaborative efforts can mitigate unnecessary constraints. Here we discuss the data
limitations of the current study and outline directions for addressing them.
1.Removing spatiotemporal irregularitiesThe gridmet dataset has spatiotemporal
irregularities where only 210/365 days of daily data is used, which might not be
able to capture long-term precipitation and temperature trends that contribute to
the variations in the yield. A study that employs complete data will be useful to
capture these trends.
2.Improving resolution for the pretrained modelThe deep learning model, VITA,
relies on the coarse NASA Power dataset with a lower resolution of 0.5 ◦. A higher
resolution grid data using climate models such as GFDL AM4 [34, 35] or the ERA5
dataset can be used here to improve the pretraining accuracy of the model.
3.Increasing granularity for the region of coverForecasting yields for a larger region
(counties) as compared to smaller areas, ranging within the 5x5 km scale, affects
the forecasting results. A more local forecasting within a smaller region will be
useful to test VITA’s learning and performance.
6 Conclusion
In this study, we observe that large-scale models such as VITA are highly effective
for forecasting crop yield under feature distribution mismatch scenarios like the 2012
drought in the US Corn belt. Moreover, with or without modifications, which we call
model adaptation for the data, VITA consistently outperforms machine learning (non-
deep learning) models. This indicates that pretrained deep learning models like VITA
are able to overcome feature distribution mismatch, and spatiotemporal irregularities
in the dataset, achieving strong prediction performance from meteorological drivers
alone. However, the model adaptation using SHAP feature selection and extreme-
year weighting shows that the performance of ML models can also be improved for
this scenario. Overall, this study suggest that ML explainability based modifications
27

are most useful when large-scale models cannot be deployed. Whereas, deep learning
models performance, despite their black box nature, improves as data quality and
quality increases (pretrained v. non-pretrained deep learning models).
References
[1] Ortiz-Bobea, A., Ault, T.R., Carrillo, C.M., Chambers, R.G., Lobell, D.B.:
Anthropogenic climate change has slowed global agricultural productivity growth.
Nature Climate Change11(4), 306–312 (2021)
[2] Yang, Y., Tilman, D., Jin, Z., Smith, P., Barrett, C.B., Zhu, Y.-G., Burney, J.,
D’Odorico, P., Fantke, P., Fargione, J.,et al.: Climate change exacerbates the
environmental impacts of agriculture. Science385(6713), 3747 (2024)
[3] Shi, Y., Pan, S., You, Y., Prior, S.A., Tian, D., Yu, H., Yu, Q., Tian, H.: Extreme
dry-heat climate impacts on greenhouse gas emission intensity in wheat pro-
duction: Insights and mitigation strategies. Global Change Biology31(7), 70349
(2025)
[4] Lobell, D.B., Roberts, M.J., Schlenker, W., Braun, N., Little, B.B., Rejesus, R.M.,
Hammer, G.L.: Greater sensitivity to drought accompanies maize yield increase
in the us midwest. Science344(6183), 516–519 (2014)
[5] Boyer, J., Byrne, P., Cassman, K., Cooper, M., Delmer, D., Greene, T., Gruis,
F., Habben, J., Hausmann, N., Kenny, N.,et al.: The us drought of 2012 in
perspective: a call to action. Global Food Security2(3), 139–143 (2013)
[6] You, Y., Tian, H., Pan, S., Shi, H., Bian, Z., Gurgel, A., Huang, Y., Kicklighter,
D., Liang, X.-Z., Lu, C.,et al.: Incorporating dynamic crop growth processes and
management practices into a terrestrial biosphere model for simulating crop pro-
duction in the united states: Toward a unified modeling framework. Agricultural
28

and Forest Meteorology325, 109144 (2022)
[7] Lemercier, M., Salvi, C., Damoulas, T., Bonilla, E., Lyons, T.: Distribution regres-
sion for sequential data. In: International Conference on Artificial Intelligence and
Statistics, pp. 3754–3762 (2021). PMLR
[8] You, J., Li, X., Low, M., Lobell, D., Ermon, S.: Deep gaussian process for crop
yield prediction based on remote sensing data. In: Proceedings of the AAAI
Conference on Artificial Intelligence, vol. 31 (2017)
[9] He, E., Xie, Y., Liu, L., Chen, W., Jin, Z., Jia, X.: Physics guided neural networks
for time-aware fairness: an application in crop yield prediction. In: Proceedings of
the AAAI Conference on Artificial Intelligence, vol. 37, pp. 14223–14231 (2023)
[10] Liu, Z., Liu, L., Xie, Y., Jin, Z., Jia, X.: Task-adaptive meta-learning framework
for advancing spatial generalizability. In: Proceedings of the AAAI Conference on
Artificial Intelligence, vol. 37, pp. 14365–14373 (2023)
[11] Liu, Q., Yang, M., Mohammadi, K., Song, D., Bi, J., Wang, G.: Machine learn-
ing crop yield models based on meteorological features and comparison with a
process-based model. Artificial Intelligence for the Earth Systems1(4), 220002
(2022)
[12] Wang, A.X., Tran, C., Desai, N., Lobell, D., Ermon, S.: Deep transfer learning for
crop yield prediction with remote sensing data. In: Proceedings of the 1st ACM
SIGCAS Conference on Computing and Sustainable Societies, pp. 1–5 (2018)
[13] Ansarifar, J., Wang, L., Archontoulis, S.V.: An interaction regression model for
crop yield prediction. Scientific reports11(1), 17754 (2021)
[14] Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B., Child, R.,
29

Gray, S., Radford, A., Wu, J., Amodei, D.: Scaling laws for neural language
models. arXiv preprint arXiv:2001.08361 (2020)
[15] Petrovic, B., Paluba, D., Nofrizal, A.Y., Kucera, A.: Analyzing meteorological
effects on crop yield and yield prediction through machine learning with differ-
ent data partitioning approaches: A case study from czech republic. Journal of
Agriculture and Food Research, 102662 (2026)
[16] Knight, C., Khouakhi, A., Waine, T.W.: The impact of weather patterns on inter-
annual crop yield variability. Science of The Total Environment955, 177181
(2024)
[17] Ray, D.K., Gerber, J.S., MacDonald, G.K., West, P.C.: Climate variation explains
a third of global crop yield variability. Nature communications6(1), 5989 (2015)
[18] Teasdale, J.R., Cavigelli, M.A.: Meteorological fluctuations define long-term crop
yield patterns in conventional and organic production systems. Scientific Reports
7(1), 688 (2017)
[19] Abatzoglou, J.T.: Development of gridded surface meteorological data for eco-
logical applications and modelling. International journal of climatology33(1),
121–131 (2013)
[20] Abatzoglou, J.T.: Development of gridded surface meteorological data for eco-
logical applications and modelling. International Journal of Climatology33(1),
121–131 (2013) https://doi.org/10.1002/joc.3413 . Dataset available at University
of California Merced Climatology Lab
[21] Hasan, A., Roozbehani, M., Dahleh, M.: Vita: Variational pretraining of trans-
formers for climate-robust crop yield forecasting. arXiv preprint arXiv:2508.03589
(2025)
30

[22] Fan, J., Bai, J., Li, Z., Ortiz-Bobea, A., Gomes, C.P.: A gnn-rnn approach for
harnessing geospatial and temporal information: application to crop yield predic-
tion. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 36,
pp. 11873–11881 (2022)
[23] Zhong, R., Zhu, Y., Wang, X., Li, H., Wang, B., You, F., Rodr ´ ıguez, L.F., Huang,
J., Ting, K.C., Ying, Y.,et al.: Detect and attribute the extreme maize yield losses
based on spatio-temporal deep learning. Fundamental Research3(6), 951–959
(2023)
[24] Xu, T., Guan, K., Peng, B., Wei, S., Zhao, L.: Machine learning-based modeling
of spatio-temporally varying responses of rainfed corn yield to climate, soil, and
management in the us corn belt. Frontiers in Artificial Intelligence4, 647999
(2021)
[25] Shahhosseini, M., Hu, G., Huber, I., Archontoulis, S.V.: Coupling machine learn-
ing and crop modeling improves crop yield prediction in the us corn belt. Scientific
reports11(1), 1606 (2021)
[26] Hoogenboom, G., Porter, C.H., Boote, K.J., Shelia, V., Wilkens, P.W., Singh, U.,
White, J.W., Asseng, S., Lizaso, J.I., Moreno, L.P.,et al.: The dssat crop modeling
ecosystem. In: Advances in Crop Modelling for a Sustainable Agriculture, pp.
173–216. Burleigh Dodds Science Publishing, ??? (2019)
[27] Brust, C., Kimball, J.S., Maneta, M.P., Jencso, K., Reichle, R.H.: Droughtcast:
A machine learning forecast of the united states drought monitor. Frontiers in
big Data4, 773478 (2021)
[28] DeAngelis, A.M., Wang, H., Koster, R.D., Schubert, S.D., Chang, Y., Marshak, J.:
Prediction skill of the 2012 us great plains flash drought in subseasonal experiment
31

(subx) models. Journal of Climate33(14), 6229–6253 (2020)
[29] Chang, A., Wang, M., Allen, G.I.: Sparse regression for extreme values. Electronic
Journal of Statistics15(2), 5995–6035 (2021)
[30] Huber, P.J.: Robust estimation of a location parameter. In: Breakthroughs in
Statistics: Methodology and Distribution, pp. 492–518. Springer, ??? (1992)
[31] Pardoe, D., Stone, P.: Boosting for regression transfer. In: Proceedings of the 27th
International Conference on International Conference on Machine Learning, pp.
863–870 (2010)
[32] Dessavre, A.G., Southall, E., Tildesley, M.J., Dyson, L.: The problem of
detrending when analysing potential indicators of disease elimination. Journal of
theoretical biology481, 183–193 (2019)
[33] Lundberg, S.M., Lee, S.-I.: A unified approach to interpreting model predictions.
Advances in neural information processing systems30(2017)
[34] Zhao, M., Golaz, J.-C., Held, I., Guo, H., Balaji, V., Benson, R., Chen, J.-
H., Chen, X., Donner, L., Dunne, J.,et al.: The gfdl global atmosphere and
land model am4. 0/lm4. 0: 2. model description, sensitivity studies, and tuning
strategies. Journal of Advances in Modeling Earth Systems10(3), 735–769 (2018)
[35] Horowitz, L.W., Naik, V., Paulot, F., Ginoux, P.A., Dunne, J.P., Mao, J., Schnell,
J., Chen, X., He, J., John, J.G.,et al.: The gfdl global atmospheric chemistry-
climate model am4. 1: Model description and simulation characteristics. Journal
of Advances in Modeling Earth Systems12(10), 2019–002032 (2020)
32
