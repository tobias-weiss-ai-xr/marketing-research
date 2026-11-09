---
title: A Sequence-to-Sequence ConvLSTM Approach for Leaf Area Index Forecasting over the South-Central
  United States
url: https://arxiv.org/abs/2608.00879
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Zhixing Ruan
- Lixin Lu
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.00879
pages: 43
chars: 70316
fetched_at: '2026-11-08T13:28:46+00:00'
kb_version: 1
---

# A Sequence-to-Sequence ConvLSTM Approach for Leaf Area Index Forecasting over the South-Central United States

A Sequence-to-Sequence ConvLSTM Approach for Leaf Area
Index Forecasting over the South-Central United States
Zhixing Ruana, Lixin Lua
aCooperative Institute for Research in the Atmosphere, Colorado State University
Fort Collins, Colorado, USA
Abstract
Leaf Area Index (LAI) is a fundamental biophysical variable governing land-
atmosphere interactions; however, LAI forecasting at high spatial resolution
remains an unsolved challenge. While recent machine learning approaches
have demonstrated LAI estimation at point or regional scales, none provides
a gridded, meteorology-driven prognostic forecast suitable for subseasonal
land surface and climate modeling applications. Here we present a sequence-
to-sequence Convolutional LSTM (ConvLSTM) framework that generates
daily 1-km LAI forecasts up to 30 days ahead, driven by historical LAI
sequences and daily meteorological forcing including temperature and pre-
cipitation. Trained and evaluated over the South-Central United States —
a region of strong climate gradients and diverse vegetation — the model
achieves a domain-averaged RMSE of 0.36 at a 30-day lead time, more than
a third lower than the persistence baseline. Forecast skill remains robust
across seasons, geographic distributions, and plant functional types, includ-
ing forests, grasslands, shrublands, and croplands. To our knowledge, this
is the first demonstration of skillful LAI forecasting at a 30-day horizon at
1-km resolution.
Keywords:Leaf Area Index, subseasonal forecasting, ConvLSTM, deep
learning, MODIS, meteorological forcing
Email addresses:zhixing.ruan@colostate.edu(Zhixing Ruan),
lixin.lu@colostate.edu(Lixin Lu)
arXiv:2608.00879v1  [physics.ao-ph]  1 Aug 2026

Highlights
•A sequence-to-sequence ConvLSTM forecasts gridded daily LAI up to
30 days ahead with meteorological predictors
•Forecasts achieve RMSE of 0.36 and R2 of 0.82 at a 30-day lead time,
∼35% below the persistence baseline
•Forecast skill is assessed by season, plant functional type, and bias
structure, beyond aggregate metrics
•Seasonal LAI bias aligns with precipitation anomalies, linking forecast
error to meteorological variability
•Incorporating land cover improves forecasts for vegetation with distinc-
tive phenology (shrublands, croplands)
1. Introduction
Vegetation plays a crucial role in regulating both regional and global cli-
mate systems. Rather than serving as passive landscape cover, the biosphere
dynamically modulates surface energy partitioning, the hydrological cycle,
and carbon fluxes through processes such as transpiration, albedo modifica-
tion, and stomatal regulation (Bonan, 2008). These vegetation dynamics ex-
ert a complex, often non-linear influence on atmospheric processes, including
temperature, precipitation, and boundary layer development (Pielke et al.,
1998). Coupled atmosphere-vegetation modeling has demonstrated that veg-
etation phenology responds strongly to atmospheric forcing on weekly to
annual timescales, and that representing vegetation state in climate models
significantly improves simulated regional climate (Lu et al., 2001).
Leaf area index (LAI), defined as the one-sided green leaf area per unit
groundarea, isakeybiophysicalvariableintegratingvegetationstructureand
physiological state (Chen and Black, 1992). Assimilating satellite-derived
LAI into regional climate models has been shown to produce more realistic
simulations of surface temperature and precipitation compared to prescribed
vegetation parameters (Lu and Shuttleworth, 2002). However, operational
forecasting requires prognostic LAI rather than observed retrievals, and accu-
rately predicting future vegetation states remains challenging. While Earth
2

System Models attempt to simulate future vegetation states, their LAI rep-
resentations often struggle to capture mean state, seasonal cycles, and in-
terannual variability (Mahowald et al., 2016). In addition, running a fully
interactive phenology module inside a climate model is computationally ex-
pensive. These limitations motivate the development of an efficient machine
learning (ML) approach to prognostic LAI modeling.
Several studies have applied traditional ML models to simulate LAI from
meteorological or remote sensing inputs, including support vector regression
(Zhang et al., 2021), random forest (Dong et al., 2025; Du et al., 2022), and
gradient boosting methods (Wang et al., 2023). However, these traditional
ML models lack temporal forecasting capability, as their point-to-point static
mapping fails to capture the cumulative, time-lagged memory of the land sur-
face. Recent deep learning approaches, including attention-enhanced Long
Short-Term Memory (LSTM) (Xiong et al., 2024) and CNN-LSTM hybrids
(Peng et al., 2026), have shown the capacity to capture temporal dependen-
cies in vegetation modeling. Yet, because these methods require concurrent
meteorological observations as inputs, they function primarily as diagnostic
estimations rather than prognostic forecasting models. Convolutional LSTM
(ConvLSTM) extends the standard LSTM with convolutional operations to
jointly capture spatial and temporal dependencies in grid-structure data (Shi
et al., 2015). Kartal et al. (2024) applied ConvLSTM to forecast the Veg-
etation Health Index (VHI) from MODIS time series, achieving RMSE as
low as 0.025 for 8-day ahead predictions using only historical VHI images.
However, their model relies solely on the autoregressive history of the target
variable and incorporates no meteorological forcing, limiting its ability to
predict vegetation responses to weather and climate variations.
Existing satellite-derived LAI products provide accurate retrospective es-
timates but lack forecasting capability, while current ML approaches either
treat vegetation variables as a static mapping target or rely on autoregres-
sive history without meteorological forcing. Yet atmospheric conditions are
known to be primary drivers of LAI variability: Lu (1999) demonstrated,
based on coupled atmospheric-ecological modeling experiments over the cen-
tralUnitedStates, thatprecipitationisthedominantdriverofLAIvariability,
with maximum and minimum temperature playing a secondary but notable
role. Incorporating such forcing variables is critical in the South-Central
United States, a transition zone where rapid shifts between humid and semi-
arid conditions drive high-frequency vegetation dynamics that are difficult to
capture with retrospective or autoregressive methods alone. To address this
3

gap, we developed a sequence-to-sequence ConvLSTM model that generates
gridded, daily, 1-km LAI forecasts driven by daily weather data, explicitly
producing the spatially continuous, prognostic LAI fields suitable for inte-
gration into coupled land-atmosphere and Earth system models. The model
integrates a sequence of historical LAI maps together with observed meteoro-
logical data – including daily maximum temperature, minimum temperature,
and precipitation – to predict LAI up to 30 days ahead across a continuous
spatial domain. We focus model development and evaluation on the South-
Central United States, a region encompassing diverse land cover and strong
seasonal vegetation dynamics, serving as a proof-of-concept before scaling
to the continental United States (CONUS). The remainder of this paper
describes the data and study domain (Section 2), the model architecture
and training configuration (Section 3), evaluation results and comparisons
against baseline forecasts (Section 4), and a discussion of limitations and
future directions (Section 5).
2. Data and Preprocessing Methods
This study integrates two primary data sources: satellite-derived LAI
from MODIS and daily surface meteorological observations from Global His-
torical Climatology Network daily (GHCNd). Both datasets were prepro-
cessed to spatially and temporally consistent 1-km daily grids prior to model
training.
2.1. Study Area
The study domain covers the South-Central United States, spanning
25.87°–37.17°N and 108.22°–92.59°W, encompassing portions of Texas, Ok-
lahoma, Louisiana, Arkansas, New Mexico, and adjacent states. The region
exhibits a pronounced west-to-east climate gradient, transitioning from semi-
arid conditions in western Texas and New Mexico to humid subtropical con-
ditions along the Gulf Coast and lower Mississippi Valley. This gradient
drives strong spatial heterogeneity in vegetation cover and phenology, with
LAI closely coupled to seasonal and interannual variability in temperature
and precipitation. The western portion of the domain is additionally influ-
enced by the North American Monsoon, which delivers a distinct pulse of
summer precipitation that strongly modulates vegetation green up. This
combination of climate diversity and strong atmosphere-vegetation coupling
makes the domain well-suited for developing and evaluating a weather-driven
4

LAI forecasting model. The spatial extent of the study domain and the LAI
averaged over June, July and August (JJA) for 2013 are shown in Fig. 1a
(LAI data described in Section 2.2). Fig. 1b presents the domain-averaged
LAI time series from 2002 to 2025, illustrating both the strong seasonal cycle
and interannual variability.
Figure 1: Study domain and LAI characteristics. (a) Mean JJA LAI over the study domain
for 2013. The red rectangle indicates the domain boundary. (b) Domain-averaged LAI
time series from 2002 to 2025. Shaded regions indicate the training and validation period
(2002–2022, blue), testing period (2023–2025, yellow).
5

2.2. MODIS LAI Data
LAI data were obtained from the MODIS Combined Terra and Aqua
Leaf Area Index product (MCD15A3H, Version 6.1; Myneni et al. 2021),
distributed by the NASA Land Processes Distributed Active Archive Center.
MCD15A3H provides 4-day composite LAI at 500 m resolution by selecting
the best available observation from both Terra and Aqua sensors within each
period.
Preprocessinginvolvedqualitycontrol(QC),spatialaggregation, andtem-
poral resampling to daily resolution. Pixel-level quality filtering was applied
using two QC layers provided with the product: pixels flagged for significant
cloud contamination in LAI/FPAR quality control layer (FparLai_QC) were
excluded, and only land-surface pixels with acceptable aggregated reflectance
quality in extra quality control layer (FparExtra_QC) were retained. Pixels
failing either criterion were marked invalid in a binary LAI validity flag. 500
m pixels were then spatially aggregated to 1 km by averaging all contributing
valid pixels within each target grid cell.
To align the 4-day LAI composites with daily meteorological forcing, LAI
values were temporally resampled to daily resolution using a forward-filling
scheme, in which each observation is held constant until the next valid com-
posite becomes available. This approach preserves the integrity of the orig-
inal retrievals without introducing artificial interpolation signals into model
training. Days carrying forward a prior observation are identified in the LAI
validity flag, distinguishing them from days with direct MODIS retrievals.
The practical implication for model design is that the hidden state evolves
daily with weather forcing while the LAI state is updated only when a real
observation is available. The details are described in Section 3.
2.3. Meteorological Forcing Data
Daily surface meteorological data were obtained from the Global Histori-
cal Climatology Network daily (GHCNd; Menne et al. 2012), maintained by
the National Centers for Environmental Information (NCEI). GHCNd pro-
vides quality-controlled daily summaries of temperature and precipitation
from land surface stations across the study domain. Station density is spa-
tially uneven, with greater concentration in populated lowlands and sparser
coverage across arid and elevated terrain, which can introduce spatial bias in
the interpolated fields, particularly in data-sparse regions.
6

2.3.1. Station Network and Spatial Coverage
The station networks used for interpolation varied in size throughout
the study period. Temperature records were available from approximately
2,000 stations in 2002, declining to 1,325 by 2025, while precipitation records
expanded nearly threefold, from 2,600 to 7,100 stations over the same period
(Fig.2).
Temperature station spacing remained consistent throughout the study
period, with a mean inter-station distance of approximately 19 km and a
90th percentile of 35 km (Fig.2b). Precipitation station spacing decreased
substantially as the network expanded, with the mean inter-station distance
declining from 17 km in 2002 to 6 km by 2025, and the 90th percentile de-
creasing from 30 km to 15 km over the same period. Despite adequate mean
network density, both networks show spatial clustering toward populated
areas, with sparser coverage over the arid western portions of the domain.
Maximum observed inter-station gaps reached 275 km for temperature, moti-
vatingtheuseofa2°bufferzonearoundthetargetdomaintoensureadequate
station coverage at the edges.
2.3.2. Spatial Interpolation to Model Grid
Meteorological station observations were spatially interpolated to the 1
km model grid using variable-specific methods. For temperature, Barnes
analysis (Barnes, 1964) was applied, a Gaussian distance-weighting scheme
designed for interpolating irregularly spaced observations onto a regular grid.
Temperature varies smoothly and continuously in space, making Barnes anal-
ysis physically appropriate. In this scheme, each grid point value is estimated
as a weighted average of nearby station observations, with the weight decay-
ing with distance as:
w(r) = exp

− r2
4κ

(1)
whereris the distance from the station to the grid point andκis the
smoothing parameter controlling the spatial influence. We setκfollowing
Koch et al. (1983) asκ= (1.33 ¯d)2/4, where ¯dis the mean inter-station
spacing (∼19km), yieldingκ≈160km 2. Two iterations were applied, with
the second pass correcting residuals between station observations and the
first-pass interpolated values to improve the fit to the original observations.
For precipitation, inverse distance weighting (IDW) was applied. Unlike
Barnes analysis, IDW makes no assumptions about the spatial continuity or
7

smoothness of the interpolated field — each grid point value is estimated as
a weighted average of nearby station observations, with weights decaying as
1/rp whereristhedistanceandpisthepowerparameter. Amaximumsearch
radius of 50 km and a minimum of 3 stations were required for interpolation.
The nominal 1 km model of grid spacing does not reflect the true spatial
resolution of the interpolated meteorological fields, which is governed by the
station network density. Following Barnes (1964), the effective resolution of
the interpolated temperature field is approximately2¯d≈38km, correspond-
ing to the minimum wavelength in the Fourier decomposition of the spatial
field, given the mean inter-station spacing. Values at finer scales are mathe-
matically interpolated with no gain in physical detail. To reduce introducing
apparent spatial detail unsupported by the station network, temperature and
precipitation fields were first interpolated to intermediate resolutions (20 km
and 10 km) using Barnes analysis and IDW respectively, then bilinearly re-
sampled to the 1 km model grid to match the LAI input resolution. No
DEM-based lapse rate correction was applied to the temperature field, as
the study domain is predominantly low-to-moderate relief terrain, and the
correction would introduce additional uncertainty in areas of complex terrain
where station density is lower.
8

Figure 2: (a) GHCNd station locations with records during 2010, representative of mid-
period network density. Target domain shown as the dashed rectangle, with a station
buffer used during interpolation. (b) Annual station count (solid lines, left axis) and
inter-station distance at the 90th percentile (dashed lines, right axis) for temperature and
precipitation stations, 2002–2025. Dotted vertical line marks the year shown in (a).
3. Spatiotemporal ConvLSTM Framework for LAI Forecasting
The proposed forecasting framework utilizes a sequence-to-sequence Con-
vLSTM architecture to map multi-dimensional atmospheric and vegetation
time series to future LAI states. By integrating spatial convolutions within
recurrent cells, the model preserves the spatial information of gridded mete-
orological forcing while capturing the time-lagged response inherent in veg-
etation phenology. This section details the spatiotemporal configuration of
the model inputs, the model architecture, sampling strategies, and the opti-
mization procedures used for training.
3.1. Spatiotemporal Input and Output Configuration
We developed the model to forecast daily LAI sequences up to two hori-
zons: 14 days and 30 days. In each setting, the model utilizes a historical
time series of length T (where T = 14 or 30) to generate a corresponding
prognostic LAI sequence. A sequence-to-sequence formulation was adopted
rather than training separate models for individual lead times. The primary
9

objective is to produce continuous forecasts spanning subseasonal — from
two weeks to two months in the future — for which a per-lead-time approach
would require an impractically large number of independent models. Further-
more, because MODIS LAI is retrieved at a 4-day composite frequency and
day-to-day LAI changes are small, a sequence-based architecture that shares
temporal representations across lead times is both more efficient and better
matching the slow varying nature of vegetation dynamics.
The selection of input variables was informed by the two-way feedbacks
between LAI and atmospheric variables discussed in Section 1, and finalized
through hyperparameter optimization (Bergstra and Bengio, 2012) on a ran-
domly sampled subset of 8000 spatiotemporal patches with a fixed random
seed for reproducibility (Section 3.5). Predictors are categorized as dynamic
(time-varying) and static (time-invariant), and are summarized in Table 1.
Meteorological forcing includes daily maximum and minimum temperature
and precipitation, interpolated from GHCNd station observations (Section
2.2). A 14-day cumulative precipitation sum is additionally included to cap-
ture antecedent moisture conditions, as vegetation LAI responds to accumu-
lated water availability over multi-day periods. Validity flags are provided
for both the temperature and precipitation fields, marking grid cells where
station coverage was insufficient during spatial interpolation.
10

Table 1: Summary of model input variables. Dynamic predictors vary across both time
and space; static predictors are time-invariant.
Category V ariable Source Channels
Dynamic Predictors (time-varying)
Meteorological Daily max. temperature GHCNd (interpolated) 1
Meteorological Daily min. temperature GHCNd (interpolated) 1
Meteorological Daily precipitation GHCNd (interpolated) 1
Meteorological 14-day cumulative precipitation GHCNd (interpolated) 1
Meteorological Temperature validity flag Derived (Section 2.3) 1
Meteorological Precipitation validity flag Derived (Section 2.3) 1
Vegetation LAI MODIS MCD15A3H 1
Vegetation LAI validity flag Derived (Section 2.2) 1
Land cover Plant functional type (one-hot) MODIS MCD12Q1 6
Static Predictors (time-invariant)
Temporal Day of year (sinusoidal) — 2
Spatial Latitude — 1
Spatial Longitude — 1
T otal 17
Annualplantfunctiontype(PFT)derivedfromMODISMCD12Q1(Friedl
and Sulla-Menashe, 2022) are grouped into 6 classes as evergreen trees, decid-
uous trees, shrubs, grass, cereal croplands and broadleaf croplands. PFT, a
proxy for vegetation parameters used to drive climate models (Harper et al.,
2023), provides a categorical prior that constrains the expected phenological
trajectory based specific vegetation functional traits.
Day of year is encoded using sine and cosine transformations,sin(2π·
DOY/365)andcos(2π·DOY/365), preserving its cyclical continuity such
that late December remains proximate to early January in the feature space.
Latitude and longitude are included as static spatial context, providing geo-
graphic information that would otherwise be lost under the spatial subsam-
pling strategy (Section 3.3).
The model output is a T-day sequence of predicted LAI values at 1 km
resolution. All continuous input variables are z-score normalized prior to
training.
3.2. Model Architecture
The model is based on the ConvLSTM architecture (Shi et al., 2015),
which replaces linear operations in standard LSTM gates with 2D convo-
lutions. This modification enables the network to capture spatiotemporal
11

dependencies jointly. At each timestep the input gateit, forget gatef t, cell
candidateg t, and output gateot are computed as:
it =σ(W xi ∗X t +W hi ∗H t−1 +b i)(2)
ft =σ(W xf ∗X t +W hf ∗H t−1 +b f )(3)
gt = tanh(Wxg ∗X t +W hg ∗H t−1 +b g)(4)
ot =σ(W xo ∗X t +W ho ∗H t−1 +b o)(5)
Ct =f t ⊙C t−1 +i t ⊙g t (6)
Ht =o t ⊙tanh(C t)(7)
whereX t ∈R C×H×W is the input tensor at timestept,∗denotes 2D
convolution,⊙element-wise multiplication, andσthe sigmoid function.W
andbare learnable convolutional weights and biases.
The model follows a sequence-to-sequence encoder-decoder design. Dur-
ing the encoding phase, the model processes the input sequence at each
timestep, updating the hidden and cell states(Ht,C t)to condense the spa-
tiotemporal history of the atmospheric and vegetation variables. The final
states are then transferred to the decoder as its initial conditions. The de-
coder generates the output sequence autoregressively, producing a predicted
LAI map at each lead timeτ:
ˆYτ =f dec

ˆYτ−1 ,H (L) τ−1 ,C (L) τ−1

, τ= 1, . . . , Tout (8)
where ˆY0 =Y Tin is the last observed LAI map and superscript(L)denotes
the final encoder layer. Because each prediction depends on all prior predic-
tions, errors can accumulate over longer horizons as a common limitation of
autoregressive architectures.
We adopt a two-layer stacked ConvLSTM configuration. This stacking
allows the second layer to extract deeper temporal abstractions from the
hidden state representations produced by the first layer. Both layers uti-
lize a hidden dimensionality of 16 channels and 3×3 convolutional kernels.
The 3×3 kernel captures spatial context from the eight immediate neighbors,
corresponding to a 3 km×3 km receptive field at our 1 km resolution.
To mitigate overfitting and improve generalization, dropout with a rate
of 0.2 is applied to the hidden state of the first encoder layer before it is
passed to the second layer. At each timestep, the four ConvLSTM gates –
12

input gate i, forget gate f, output gate o, and cell candidate – control the
flow of information, determining which new features are written to memory
and which past memory should be retained to drive the prognostic output.
The overall architecture is illustrated in Fig. 3
Figure 3: (Top) Internal gate structure of a single ConvLSTM cell, showing the input (i),
forget (f), output (o), and cell candidate (g) gates. (Bottom) Unrolled encoder-decoder
sequence: the encoder processestdays of multivariate spatial inputs augmented with
day-of-year encoding; the decoder autoregressively generates the predicted LAI sequence,
conditioned on the final encoder states.
3.3. Spatial Subsampling Strategy
Training the LAI forecasting model on the full 1 km resolution study do-
main is computationally intensive, with more than 1.7 million pixels. The
scale would grow to approximately 15.3 million pixels at CONUS extent.
Training on all available pixels is also methodologically inadvisable, as spa-
tially adjacent pixels share highly correlated inputs and targets, contributing
redundant information to parameter updates and increasing the risk of over-
fitting.
13

To address this, the domain was partitioned into non-overlapping 100
×100-pixel patches for spatial sampling. For the final models, all patches
across the domain were used for training, ensuring complete spatial coverage
whilereducingspatialredundancybetweenadjacentsamples. Temporally, for
each spatial patch, a stride equal to the input sequence length was applied
so that consecutive temporal samples did not overlap in time, further reduc-
ing redundancy. This procedure yielded approximately 72,000 and 38,000
spatiotemporal training patches for the 14-day and 30-day configurations,
respectively. For the hyperparameter experiments described in Section 3.4,
a randomly sampled subset of 8,000 patches was drawn from this pool to
enable efficient exploration of the configuration space.
3.4. Loss Function and Training
The model is trained by minimizing the mean squared error (MSE) be-
tween predicted and observed LAI, computed on all pixels except those
flagged as invalid (flag=0), such as water bodies and cloud-contaminated re-
trievals. BecauseMODISLAIisavailableonlyasa4-daycompositeproducts,
restricting the loss function to true-retrieval pixels (flag=1) would leave the
most days in the 14- and 30-day prediction sequences without direct super-
vision. In preliminary experiments, this sparse-supervision approach showed
slightly weaker performance, with larger bias in certain regions and seasons.
We nonetheless include forward-filled pixels (flag=2) in the loss computation,
while retaining the validity flag as an input channel (Section 3.1), so the
model can distinguish genuine retrievals from interpolated values. This en-
ables a denser training signal across the full sequence length while preserving
the model’s ability to learn from the timing of true observational updates.
The loss is applied uniformly across all predicted timesteps and valid spatial
pixels, with no seasonal or spatial weighting. Formally, the masked MSE loss
is defined as:
L= 1P
t,i,j 1[ft,i,j ∈ {1,2}]
X
t,i,j
1[ft,i,j ∈ {1,2}]·(ˆyt,i,j −y t,i,j)2 (9)
whereˆyt,i,j andy t,i,j denote the predicted and observed z-scored LAI at
timesteptand spatial location(i, j);f t,i,j ∈ {0,1,2}is the LAI validity flag;
and1[·]is the indicator function that equals 1 whenf t,i,j ∈ {1,2}(valid
MODIS retrieval or interpolated observation) and 0 otherwise.
14

The primary model targets a 30-day forecast horizon and it was trained
using the Adam optimizer with an initial learning rate of 0.0003 and a batch
size of 64. The learning rate was reduced by a factor of 0.5 when the valida-
tion loss showed no improvement for 20 consecutive epochs, with a minimum
learning rate of 1e-6. This learning rate schedule allows the optimizer to
make finer weight adjustments as training progresses. Early stopping was
applied based on validation loss with a patience of 30 epochs and a minimum
improvement threshold of 0.0001. The training data were split chronolog-
ically: samples from 2002 through 2021 were used for training, 2022 was
reserved for validation, and 2023–2025 was held out for independent evalua-
tion. The 30-day model was trained on samples constructed with a 30-day
stride, approximately 33,000 valid training samples.
3.5. Selection of Kernel Size and Input Sequence Length
Selecting model hyperparameters (e.g., learning rate, batch size, hidden
dimensionality, and number of filters) required balancing forecast accuracy
against model complexity, computational cost, and the risk of overfitting. We
conducted a series of exploratory experiments on a randomly sampled subset
of 8,000 spatiotemporal patches (fixed random seed for reproducibility), with
each configuration trained for 20 epochs and repeated across 10 independent
runs to account for initialization variability. While additional hyperparam-
eters (e.g., dropout rate, learning rate schedule, number of stacked layers)
were also tuned during model development, we focus this section on kernel
size and input sequence length — two hyperparameters that directly reflect
the spatial and temporal correlation structure of LAI changes.
Figure 4 presents validation RMSE across kernel sizes of 1×1, 3×3, 5×5,
and 7×7, with all other settings held fixed as described in Section 3.2. Ker-
nel size controls the spatial extent of neighboring information incorporated
at each timestep. Within this reduced-data exploratory setting, the 1×1
(pixel-wise) kernel yielded the highest RMSE, while the 5×5 kernel achieved
slightly lower validation RMSE than the 3×3 kernel (mean RMSE of 0.3965
vs. 0.4008 at a 30-day lead time). The 7×7 showed marginally lower RMSE
still, but this gain was not proportional to its substantially higher parameter
count relative to the other configurations (Table 2). Based on these results,
the 3×3 and 5×5 kernels were selected as candidates for full-scale training
and evaluation on the independent test set. During full-scale training, the
5×5 configuration reached its lowest validation RMSE (0.1137) within 25
epochs before validation loss became increasingly noisy and trended upward,
15

while training loss continued to decrease — a signature of overfitting (Fig. 5).
The 3×3 configuration maintained a more stable validation loss throughout
training and achieved a lower best validation RMSE (0.1121). This pattern
was also reflected in spatial, seasonal, and PFT-stratified error metrics, all of
which favored the 3×3 configuration. We therefore selected the 3×3 kernel
as the final model configuration.
Figure4: Exploratoryexperimentsforhyperparametertuningofkernelsize. (a)Validation
RMSE as a function of lead time for each kernel size. Shaded regions show variation across
10 repetitions. (b) Box plot of validation RMSE at a 30-day lead time.
Table 2: The size of trainable parameters for each model configuration.
Configuration Trainable parameters
Kernel size 1×1 7,635
Kernel size 3×3 66,515
Kernel size 5×5 184,275
Kernel size 7×7 360,915
16

Figure 5: Training and validation loss during full-scale model training for 3×3 and 5×5
kernel configurations. Solid and dashed lines show training and validation RMSE, respec-
tively, as a function of epoch; blue indicates the 3×3 kernel and red indicates the 5×5
kernel. Vertical dotted lines mark the epoch of best validation RMSE for each configura-
tion.
Figure 6 shows validation RMSE as a function of lead time for the input
sequence length experiments, in which input sequences of 7, 14, 30, 45, and
60 days were tested with the output forecast length fixed at 30 days. Input
sequences of 14 and 30 days achieved the lowest validation RMSE, with the
14-day input performing slightly better than the 30-day input. Longer input
sequences did not yield further improvement, and the 60-day input sequence
showed the worst performance, possibly reflecting a general limitation of
recurrent architectures in effectively using very long input histories. Based on
theseresults, twoprimarymodelconfigurationsweredevelopedwithmatched
input and output sequence lengths of 14 and 30 days, respectively. While the
experiments (Fig. 6) indicate that a 14-day input alone achieves comparable
skill for 30-day forecasts, we retained matched input and output lengths to
ensure sufficient historical context across the full forecast horizon, which is
also a common design choice in sequence-to-sequence forecasting.
17

Figure 6: Exploratory experiments for hyperparameter tuning of input sequence length.
(a) Validation RMSE as a function of lead time for each length. Shaded regions show
variation across 10 repetitions. (b) Box plot of validation RMSE at a 30-day lead time.
4. Model Evaluation
Model performance is evaluated across two complementary aspects. First,
overall forecast accuracy is quantified across varying lead times using stan-
dard machine learning metrics: root mean square error (RMSE), which is
sensitive to large errors due to the squared penalty; mean absolute error
(MAE), which provides an interpretable measure of average error magnitude;
and the coefficient of determination (R2), which quantifies the proportion of
LAI variance explained by the model. The second aspect focuses on the bio-
physical interpretation of LAI forecasts, examining model performance across
seasons, geographic distributions, and vegetation types. The pronounced sea-
sonal variability and land cover dependence of LAI produce dynamic, spa-
tially heterogeneous patterns that are challenging to capture, making domain-
specific evaluation essential. Unless otherwise noted, RMSE, MAE, andR2
are computed only on pixels with true MODIS retrievals (flag=1), excluding
forward-filled pixels (flag=2), to ensure that reported skill reflects perfor-
mance against real observations. Metrics are aggregated over all such valid
pixels within the domain and averaged across the full testing period (2023–
2025).
18

4.1. Forecast Skill Across Lead Times
Forecast skill is additionally compared against a persistence forecast as a
reference baseline, defined as:
LAIf orecast(t+τ) =LAI obs(t)
whereτrepresents the lead time in days. Persistence is a standard baseline
in sub-seasonal to seasonal forecasting, representing a particularly meaning-
ful benchmark for vegetation variables given their relatively slow temporal
dynamics.
Both the 14-day and 30-day models demonstrate consistent forecast skill
across their respective lead times, with RMSE and MAE increasing gradually
andR 2 remaining stable as the forecast horizon extends (Fig. 7). For the 14-
day model, RMSE increases from 0.31 to 0.34 (lead time 1–14 days), whileR2
remains high throughout (0.87–0.84), indicating that the model captures the
dominant variance in LAI dynamics even at longer lead times. The 30-day
model shows a similar pattern of gradual skill decrease, with RMSE increas-
ing from 0.30 to 0.36 (lead time 1–30 days) andR2 ranging from 0.87 to
0.82. Both models substantially outperform the persistence baseline across
all lead times — the 14-day model reduces RMSE by 30% relative to persis-
tence, while the 30-day model achieves a 35% reduction — demonstrating
meaningful forecast skill beyond a constant-state assumption.
Domain-level metrics are comparable across the two configurations, sug-
gesting that the model framework is robust for both sequence lengths. How-
ever, aggregated metrics alone may obscure differences in performance at
specific locations, seasons, or vegetation types. These are examined in detail
in subsequent sections.
19

Figure 7: Forecast skill across lead times for the 14-day and 30-day LAI forecasting models,
evaluated over the independent testing period (2023–2025). (a) RMSE (red) and MAE
(blue) for the 14-day model, compared against the persistence forecast RMSE (gray) as
a reference baseline. (b)R 2 for the 14-day model across lead times 1–14 days. (c) Same
as (a) but for the 30-day model across lead times 1–30 days. (d) Same as (b) but for
the 30-day model. All metrics are computed pixel-wise over quality-controlled valid pixels
within the study domain and spatially averaged across the evaluation period. Error units
are LAI units (m2m−2).
4.2. Spatial and Seasonal Distribution of Forecast Errors
LAI exhibits pronounced spatial heterogeneity driven by distinct vegeta-
tion types, geographic constraints, and localized weather conditions. While
the domain-averaged metrics presented in Section 4.1 quantify overall model
accuracy, they can mask regional variation in performance. Characterizing
the spatial and seasonal distribution of forecast errors is therefore essential
for identifying where the model framework underperforms, and provides di-
20

agnostic feedback to guide future expansion to the broader CONUS domain.
4.2.1. Spatial Distribution of Forecast Errors
Figure 8 presents the spatial distribution of pixel-wise RMSE and bias
at lead times of 7, 14, and 30 days from the 30-day model, alongside the
14-day lead time from the 14-day model for comparison. Accompanying
histograms quantify the domain-wide distribution of these errors. Spatial
patterns of RMSE are broadly similar between the two model configurations
at the 14-day lead time, consistent with the comparable domain-averaged
metrics reported in Section 4.1. Because RMSE scales with the magnitude
of the predicted variable, regions with higher LAI values tend to exhibit
larger absolute errors. The highest RMSE values are concentrated in the
eastern portion of the domain, where Deciduous Broadleaf Forest supports
LAI values substantially greater than those in the central and western regions.
These elevated errors are therefore largely proportional to the local leaf area
index rather than indicative of a systematic model deficiency.
While RMSE captures the magnitude of errors, bias maps reveal whether
the model systematically over- or underestimates LAI spatially. A region
with high RMSE but near-zero bias indicates that large errors occur but
cancel across the evaluation period, whereas a region with low RMSE but
notable bias indicates consistent directional error. The 30-day model demon-
strates more spatially balanced bias than the 14-day model. Bias also in-
creases progressively from the 7-day to the 30-day lead time, consistent with
the seq2seq architecture, in which prediction errors can accumulate across
successive forecast steps. Notably, the 14-day model exhibits an overestima-
tion bias of approximately 0.025 LAI units relative to the 30-day model at
the equivalent 14-day lead time — despite being specifically optimized for
shorter-horizon prediction, it shows greater systematic bias than the 30-day
model does at that same horizon. This suggests that extended meteorological
input context may play a more important role in LAI forecasting accuracy
than forecast horizon length alone.
21

Figure 8: Spatial distribution of pixel-wise RMSE (a–d) and bias (e–h) over the indepen-
dent testing period (2023–2025). (a–c, e–g) 30-day model at lead times of 7, 14, and 30
days. (d, h) 14-day model at a 14-day lead time, for comparison. Accompanying his-
tograms show the domain-wide frequency distribution of pixel-wise errors.
4.2.2. Seasonal Bias Patterns
The seasonal spatial bias maps (Figure 9) show pixel-wise bias at lead
timesof7, 14, and30daysacrossthefourmeteorologicalseasons—December–
February (DJF), March–May (MAM), June–August (JJA), and September–
November (SON). MAM and JJA exhibit the largest spatial bias, coinciding
with the active growing season when LAI variability is greatest. Notably, the
30-day model underestimates LAI in the central domain during MAM — a
region predominantly covered by grassland — and overestimates the same
region during JJA. This reversal is consistent with the phenological cycle of
grassland vegetation: during spring green-up, rapid LAI increases outpace
the model’s prediction, while during peak summer the model may anticipate
continued growth that is instead constrained by drought stress or moisture
limitation in the semi-arid central domain. This tendency is amplified at the
30-day lead time, where the model relies on meteorological conditions from
30 days prior and has no knowledge of subsequent weather evolution. This
interpretation is supported by the seasonal meteorological anomalies over the
same period (Figure 10): the central domain received above-normal precipi-
tation during MAM, spatially coincident with the region of LAI underestima-
tion, and below-normal precipitation during JJA, spatially coincident with
22

the region of LAI overestimation. In contrast, TMAX and TMIN anomalies
were positive across nearly the entire domain in both seasons, with compar-
atively little spatial structure distinguishing the central grassland from sur-
rounding regions. The spatial pattern of forecast bias therefore more closely
tracks the heterogeneous precipitation anomaly than the spatially uniform
temperature anomaly, suggesting that precipitation variability, rather than
temperature, is the primary driver of the bias in this grassland region — con-
sistent with the dominant role of precipitation in LAI variability reported
by Lu (1999). DJF and SON show substantially lower and spatially uni-
form bias, reflecting the relatively low LAI variability during dormant and
senescent periods.
Figure 9: Seasonal spatial bias maps from the 30-day model over the independent testing
period (2023–2025). Each row corresponds to a lead time of 7, 14, or 30 days, and each
column corresponds to a meteorological season (DJF, MAM, JJA, SON). Bias is defined
as the mean signed error (predicted minus observed), computed pixel-wise and averaged
across the evaluation period.
23

Figure 10: Seasonal meteorological anomalies and corresponding 30-day-lead-time LAI
bias over the central domain grassland region, for MAM (top row) and JJA (bottom row),
2023–2025. (a, e) TMAX anomaly (z-score) relative to the 2002–2022 climatology. (b, f)
TMIN anomaly (z-score). (c, g) Precipitation anomaly (z-score). (d, h) LAI bias at a
30-day lead time.
Figure 11 presents the corresponding bias distributions quantitatively for
each season and lead time. The center of each distribution indicates the
mean bias direction — a distribution centered to the right of zero indicates
systematic overestimation, while one centered to the left indicates underesti-
mation. The width and shape of the distribution reflect the spread of errors:
a narrow distribution indicates spatially consistent predictions, a wide dis-
tribution indicates high spatial variability in bias, and a skewed distribution
indicates systematic directional errors across the domain. At lead times of 7
and 14 days, bias distributions are narrow and approximately centered near
zero across all four seasons, demonstrating stable seasonal performance. At
a lead time of 30 days, distributions are broader as expected for a longer
forecast horizon, yet remain relatively concentrated near zero. MAM and
JJA show wider and more skewed distributions compared to DJF and SON,
confirming that the model captures the low-variability seasons more easily.
24

Figure 11: Seasonal bias distributions from the 30-day model at lead times of 7 (a), 14
(b), and 30 days (c), over the independent testing period (2023–2025). Each panel shows
the frequency distribution of pixel-wise bias across the domain for the four meteorological
seasons (DJF, MAM, JJA, SON). The vertical dashed line at zero indicates unbiased
prediction.
Figure 12 compares the bias distributions at a 14-day lead time from
the 14-day and 30-day models across all four seasons. Both models exhibit
bias values mainly within±0.2 LAI units and show similar distributions in
DJF and SON. In MAM and JJA, the 30-day model produces a more zero-
centered bias distribution than the 14-day model, consistent with the spatial
bias analysis in Section 4.2.1 and further supporting the selection of the
30-day configuration as the primary model.
25

Figure 12: Comparison of bias distributions at a 14-day lead time between the 14-day and
30-day models across the four meteorological seasons: (a) DJF, (b) MAM, (c) JJA, and
(d) SON. Each panel shows the frequency distribution of pixel-wise bias for both model
configurations over the independent testing period (2023–2025). The vertical dashed line
at zero indicates unbiased prediction.
4.3. Temporal Dynamics of Domain-Averaged LAI
While pixel-wise metrics provide a fundamental assessment of model ac-
curacy, domain-averaged LAI time series provide a complementary perspec-
tive on model skill at the regional scale. By averaging across all valid pixels,
domain-levelLAIminimizeshigh-frequencyspatialnoise. Suchregionalmean
behavior is important for sub-seasonal to seasonal forecasting and land sur-
face modeling, where aggregated vegetation states serve as surface boundary
conditions (Kumar et al., 2019). We evaluate the continuous time series of
domain-averaged LAI over the independent testing period (2023–2025).
Figure 13 and Figure 14 show the domain-averaged LAI time series for
the 14-day and 30-day models, respectively, compared against the MODIS-
26

derived domain-averaged LAI as the observational reference. While the 30-
day model shows lower spatial bias overall, the 14-day model captures the
domain-averaged LAI more accurately during the active growing season of
May–August 2023 and reproduces the elevated LAI variability observed in
late July 2025, despite the two models showing nearly identical RMSE of the
domain-averaged LAI time series (0.062 vs. 0.060 at a 14-day lead time) — a
negligible difference that masks meaningful differences in temporal dynamics.
Spatial averaging over a large domain also suppresses local anomalies, poten-
tially masking model behavior at finer spatial scales. These results suggest
that the 30-day model is the preferred configuration as the primary model;
however, for applications requiring greater sensitivity to temporal variability
or deviations from the regional mean response, the 14-day model may offer
advantages that aggregate metrics alone do not reveal. Further site-specific
evaluation is recommended before applying either configuration for such pur-
poses.
27

Figure 13: Domain-averaged LAI time series from the 14-day model over the indepen-
dent testing period (2023–2025). (a) Observed domain-averaged LAI (black dashed line)
compared against model predictions at lead times of 7 days (orange dots) and 14 days
(blue dots). Seasonal shading indicates DJF (blue), MAM (green), JJA (pink), and SON
(yellow). (b) Temporal evolution of domain-averaged bias (predicted minus observed) at
lead times of 7 days (orange) and 14 days (blue), with shaded areas indicating the bias
magnitude. Summary statistics are reported in the lower right: mean bias, RMSE, and
MAE of the domain-averaged LAI time series for each lead time, computed over the full
evaluation period. Domain averages are computed over all quality-controlled valid pixels
within the study domain.
28

Figure 14: Domain-averaged LAI time series from the 30-day model over the independent
testing period (2023–2025). (a) Observed domain-averaged LAI (black dashed line) com-
pared against model predictions at lead times of 14 days (blue dots) and 30 days (red
dots). Seasonal shading indicates DJF (blue), MAM (green), JJA (pink), and SON (yel-
low). (b) Temporal evolution of domain-averaged bias (predicted minus observed) at lead
times of 14 days (blue) and 30 days (red), with shaded areas indicating the bias magnitude.
Summary statistics are reported in the lower right: mean bias, RMSE, and MAE of the
domain-averaged LAI time series for each lead time, computed over the full evaluation
period. Domain averages are computed over all quality-controlled valid pixels within the
study domain.
4.4. Phenological Variability Across Vegetation Types
LAI magnitudes vary substantially across vegetation types. Forests gener-
ally sustain the highest LAI values, while shrublands and grasslands maintain
comparatively lower values in the semi-arid and arid environments. Vegeta-
tion types also exhibit distinct seasonal dynamics driven by different climate
controls and management regimes. Shrubs in the central-western portion
of the domain follow a monsoon-driven phenology: LAI remains suppressed
through the dry spring, reaches a pre-monsoon minimum in early July, then
rises sharply with the onset of summer convective precipitation, sustaining
peak greenness from JJA into September (Warter et al., 2023). Grasslands
across the domain initiate green-up earlier in spring, with the start of season
controlled by a combination of temperature and soil moisture. In contrast
29

to natural vegetation types, cropland LAI dynamics are largely governed by
agricultural practices such as planting calendars and harvest timing, resulting
in sharp increases and abrupt declines in LAI (Amin et al., 2021).
Figure 15 shows the plant functional type (PFT) map derived from the
MODIS MCD12Q1 product for 2023 (Sulla-Menashe and Friedl, 2022), and
Table 3 summarizes the corresponding land cover composition of the study
domain. Grasses (46.43%), shrubs (20.81%), and deciduous broadleaf trees
(11.16%) are the three dominant PFTs across the study domain, reflecting
the semi-arid to sub-humid vegetation gradient from the Chihuahuan Desert
through the Southern Plains to the eastern deciduous transition. Unlike
other common land cover classification schemes, such as the International
Geosphere-BiosphereProgramme(IGBP)schemeandtheUniversityofMary-
land (UMD) scheme, the PFT scheme distinguishes two crop classes — cereal
crops and broadleaf crops — based on their distinct canopy structures and
phenological behaviors. The following evaluation focuses on model perfor-
mance across the major PFT classes in the domain.
Table 3: Land cover composition of the study domain (MCD12Q1 PFT scheme) for 2023.
Class Label Pixels Percent
0 Water Bodies 135,181 8.41%
1 Evergreen Needleleaf Trees 61,840 3.85%
2 Evergreen Broadleaf Trees 25,443 1.58%
3 Deciduous Needleleaf Trees 2 0.00%
4 Deciduous Broadleaf Trees 179,246 11.16%
5 Shrub 334,320 20.81%
6 Grass 745,942 46.43%
7 Cereal Crop 61,425 3.82%
8 Broadleaf Crop 31,040 1.93%
9 Urban and Built-up Lands 17,838 1.11%
10 Permanent Snow and Ice 14 0.00%
11 Barren 14,434 0.90%
Total valid pixels 1,606,725 100.00%
30

Figure 15: Plant functional type (PFT) classification derived from the MODIS MCD12Q1
LC_Type5 product for 2023.
4.4.1. Model Performance over Forests
Figure 16 presents model performance across three primary tree classifi-
cations: deciduous broadleaf, evergreen needleleaf, and evergreen broadleaf,
which account for approximately 12%, 4%, and 2% of the study domain in
2023 and 2024. The deciduous needleleaf class is excluded, as it comprises
less than 0.0002% of the domain. The model outperforms the persistence
forecast for all three tree types, withR2 exceeding 0.7 across all lead times.
The model successfully captures both seasonal and interannual variability
across all tree types, accurately predicting the anomalously low LAI values
observed in January 2024 even at a 30-day lead time.
31

Figure 16: Model evaluation for tree plant functional types. Left panels show domain-
averaged LAI time series (2023–2025) for (a) evergreen needleleaf trees, (b) evergreen
broadleaf trees, and (c) deciduous broadleaf trees, with observations (dashed line), 14-day
lead time predictions (LT14d, circles), and 30-day lead time predictions (LT30d, triangles).
SeasonalshadingindicatesDJF(blue), MAM(green), JJA(red), andSON(orange). Right
panels show skill metrics as a function of lead time (1–30 days) for all three tree types:
(d) RMSE (solid lines) and persistence baseline RMSE (dotted lines) in LAI units, and (e)
coefficient of determination (R2).
4.4.2. Model Performance Over Grasslands
Grasslands constitute the dominant land cover type across the study do-
main, and the model demonstrates robust predictive skill over these regions.
As illustrated in Figure 17, the model maintains a highR2 of 0.73 even at
a lead time of 30 days. The time series shows several notable phenological
anomalies: a sharp increase in LAI in May 2023, a sudden LAI decline in Jan-
uary 2024, and sustained peak greenness throughout June and July of 2025.
Both the 14-day and 30-day forecasts successfully capture the abrupt LAI
decline in January 2024, and gradually adjust to the rapid spring green-up
in 2023. However, while the 14-day forecast effectively tracks the sustained
high LAI in early summer 2025, the 30-day forecast struggles to capture the
32

magnitude of this trend.
Figure 17: Model evaluation for grasslands. (a) Domain-averaged LAI time series from
2023–2025, with observations (dashed line), 14-day lead time predictions (LT14d, circles),
and 30-day lead time predictions (LT30d, triangles). Seasonal shading: DJF (blue), MAM
(green), JJA (red), and SON (orange). (b) RMSE (solid line) and persistence baseline
RMSE (dotted line) in LAI units as a function of lead time (1–30 days). (c) Coefficient of
determination (R2) as a function of lead time.
Because grasses are shallow-rooted and highly sensitive to recent precipi-
tation pulses (Ogle and Reynolds, 2004), examining the underlying weather
forcing provides important context for this behavior. Figure 18 presents the
domain-averaged daily maximum temperature (Tmax), minimum tempera-
ture (Tmin), and precipitation across the grassland regions. In mid-May
2023, the region experienced a notably higher precipitation pulse compared
to the same period in 2024 and 2025, while temperatures were comparable
across years. This moisture influx was likely one of the drivers of the sharp
LAI increase observed in May 2023. Because 30-day forecasts initialized
prior to this event lacked information about the subsequent precipitation
pulse, green-up was initially underestimated; forecasts initialized closer to
the event correctly captured the LAI response. Similarly, the sustained high
LAI observed in June and July 2025 correlates strongly with higher precipita-
tion and cooler Tmax values relative to 2023 and 2024. The 30-day forecast
for June, driven primarily by the drier meteorological conditions present at
initialization in May, predictably underestimated this growth. In contrast,
14-day forecasts initialized in July, when the wetter conditions were already
established, successfully captured the elevated LAI.
33

Figure 18: Domain-averaged meteorological forcing time series over grassland pixels (2023–
2025): (a) daily minimum temperature (Tmin, ◦C), (b) daily maximum temperature (Tmax,
◦C), and (c) daily precipitation (PRCP, mm day−1). Seasonal shading indicates DJF
(blue), MAM (green), JJA (yellow), and SON (orange).
4.4.3. Model Performance Over Shrubs
Figure 19 presents the model’s predictive skill over shrublands, which pri-
marily occupy the western portion of the domain. These ecosystems exhibit
high seasonality, with a short period of intense greening shortly after the on-
set of North American Monsoon (NAM) precipitation (Forzieri et al., 2011).
Observational LAI time series highlight a contrast with trees and grasses:
shrubland green-up is distinctly delayed, remaining suppressed through the
spring and peaking from summer into early autumn. The 14-day forecast
reproduces this dynamic, achieving anR2 of approximately 0.70 and success-
fully capturing both the delayed onset and the rapid green-up across all three
testing years.
34

Figure 19: Model evaluation for shrublands. (a) Domain-averaged LAI time series from
2023–2025, with observations (dashed line), 14-day lead time predictions (LT14d, circles),
and 30-day lead time predictions (LT30d, triangles). Seasonal shading: DJF (blue), MAM
(green), JJA (yellow), and SON (orange). (b) RMSE (solid line) and persistence baseline
RMSE (dotted line) in LAI units as a function of lead time (1–30 days). (c) Coefficient of
determination (R2) as a function of lead time.
Performance degrades at the 30-day lead time (R2 ≈0.65), primarily
due to a tendency to overestimate early-season LAI. Notably, in February
and March 2024, the 30-day forecast predicted LAI values 0.025–0.05 higher
than observations, before realigning with the observed trajectory in April.
Figure 20 shows that the winter of 2023–2024 was wet; because the 30-day
forecasts for early spring were initialized using these wet conditions, the
model prematurely triggered the green-up phase. The 30-day forecasts for
April were initialized using March conditions, which reflected average precip-
itation, and the predicted trajectory moved closer to the observed delayed
green-up, though not fully converging with observations.
Performance degrades at the 30-day lead time (R2 ≈0.65), primarily
due to a tendency to overestimate early-season LAI. Notably, in February
and March 2024, the 30-day forecast predicted LAI values 0.025–0.05 higher
than observations, before realigning with the observed trajectory in April.
Figure 20 indicates that the winter of 2023–2024 was wet; because the 30-
day forecasts for early spring were initialized using these wet conditions, the
model prematurely triggered the green-up phase. The 30-day forecasts for
April were initialized using March conditions, which reflected average precip-
itation, and the predicted trajectory moved closer to the observed delayed
green-up, though not fully converging with observations.
35

Figure 20: Domain-averaged meteorological forcing time series over shrub pixels (2023–
2025): (a) daily minimum temperature (Tmin, ◦C), (b) daily maximum temperature (Tmax,
◦C), and (c) daily precipitation (PRCP, mm day−1). Seasonal shading indicates DJF
(blue), MAM (green), JJA (yellow), and SON (orange).
Overall, shrublands exhibit the lowest 30-dayR2 among the natural veg-
etation classes. A critical factor worth further investigation is the quality
and spatial density of the precipitation input data. The western domain fea-
tures a notably sparser network of precipitation stations (Figure 2). Given
the high sensitivity of desert shrubs to localized precipitation pulses, sparse
station coverage likely introduces uncertainty into the model initializations,
constraining predictability at longer lead times.
4.4.4. Model Performance Over Croplands
In contrast to natural vegetation, cropland phenology is primarily gov-
erned by human activities rather than climate forcing alone. A major ad-
vantage of this machine learning framework is its capacity to implicitly learn
and generalize these human-driven patterns — such as abrupt harvest events
— directly from historical LAI changes. This remains a significant challenge
for traditional, physics-based vegetation dynamics models.
Figure21presentstheLAIforecastsandassociatedmetricsforbothcereal
and broadleaf crops. Both crop types show meaningful forecast skill at a 30-
36

day lead time, withR2 ranging from 0.53 to 0.55, though performance is more
variable than for natural vegetation types, reflecting the added complexity
of human-driven management practices. Both 14-day and 30-day forecasts
reproduce major interannual phenological shifts and accurately capture the
dual LAI reductions associated with spring and summer harvest windows for
bothcroptypes. However, theforecastsstruggletoresolveminorfluctuations,
suchasthesubtleLAIvariationsobservedincerealcropsfromlateautumnto
winter. These deviations are likely due to the framework’s spatial limitations
when resolving small-scale agricultural parcels, a factor that warrants further
investigation.
Figure 21: Model evaluation for cropland plant functional types. Left panels show domain-
averaged LAI time series from 2023 to 2025 for (a) cereal crops and (b) broadleaf crops,
with observations (dashed line), 14-day lead time predictions (LT14d, circles), and 30-day
lead time predictions (LT30d, triangles). Seasonal shading indicates DJF (blue), MAM
(green), JJA (yellow), and SON (orange). Right panels show skill metrics as a function of
lead time (1–30 days) for both crop types: (c) RMSE (solid lines) and persistence baseline
RMSE (dotted lines) in LAI units, and (d) coefficient of determination (R2).
5. Discussion
The sequence-to-sequence ConvLSTM architecture demonstrates predic-
tive skill up to a 30-day horizon at 1-km resolution, achieving a domain-
averaged RMSE of approximately 0.36, which outperforms the persistence
baseline RMSE of 0.56. Beyond aggregate error metrics, the model main-
tains spatial consistency across the domain and reproduces key phenological
37

features across vegetation types and seasons, supporting its potential utility
as an LAI forcing in land surface and climate models.
LAI dynamics are strongly land-cover dependent. As demonstrated in
Section 4.4, different vegetation types exhibit distinct phenological responses
to meteorological forcing — shrublands show delayed green-up dynamics,
and croplands are strongly modulated by agricultural management. Incor-
porating dynamic land cover as a time-varying input allows the model to
learn PFT-specific LAI response patterns rather than averaging across het-
erogeneous vegetation, which is particularly important when targeting broad
domains such as CONUS. Figure 22 presents a site-level LAI analysis compar-
ing the model with and without land cover predictors. Representative local
regions of approximately 0.1◦ ×0.1 ◦ (∼121 km2) are examined. Two shrub-
land sites in the Chihuahuan Desert ecoregion and one cropland site along
the southeast Texas coast are selected. For the shrubland sites, the model
with land cover predictors better captures the delayed late-summer green-up,
with predicted LAI values more closely following observed ranges and with-
out anomalously large values. For the cropland site, the model with land
cover predictors captures the LAI decline associated with corn and sorghum
harvest beginning in July, while the model without land cover predictors
overestimates LAI during this period. Domain-averaged and PFT-stratified
metrics at a 30-day lead time, however, remain relatively close between the
two configurations, as summarized below:
Table 4: Domain-averaged and PFT-stratified performance metrics at a 30-day lead time,
with and without land cover (LC) as a model predictor.
Configuration RMSE MAER 2 RMSEshrub RMSEcereal RMSEbroadleaf
Model with LC 0.361 0.194 0.823 0.081 0.389 0.358
Model without LC 0.370 0.205 0.814 0.092 0.412 0.376
38

Figure 22: Site-level LAI comparison between the model with land cover predictors (Model
A, red) and without land cover predictors (Model B, blue) at a 30-day lead time. Left
panels (a, c, e) show the spatial extent and land cover composition of each representative
site (white rectangles); the PFT color legend is shown in Figure 15. Right panels (b, d,
f) show the domain-averaged observed LAI (black dashed) alongside Model A and Model
B predictions. Bias and RMSE values for each model configuration are annotated in each
panel.
39

This reflects a common trade-off in machine learning model design — that
architecture complexity and additional predictors do not always yield pro-
portional improvements in aggregate performance. The improvement from
incorporating land cover predictors is not uniform: it benefits vegetation
types with distinctive phenology, such as shrublands and croplands, while
the domain-averaged gain remains modest. From a practical standpoint, the
model without land cover predictors offers a simpler input pipeline, which can
be an advantage in near-real-time forecasting contexts. The choice between
configurations therefore depends on the target application — where PFT-
specific accuracy is required, the additional complexity is justified; where
domain-wide LAI forecasting skill is the primary goal, the simpler configura-
tion remains competitive. Future sensitivity experiments within land surface
and climate modeling frameworks will be needed to quantify whether these
finer-scale RMSE improvements translate into better forecasting skill once
the LAI fields are ingested into such models.
Several limitations warrant consideration. Forecast skill over shrublands
is limited compared to other vegetation types, which may partly reflect the
effective spatial resolution of the interpolated meteorological variables, par-
ticularly given the sparser precipitation station coverage across the western
domain. Additionally, as with other autoregressive sequence-to-sequence ar-
chitectures, prediction errors can accumulate across the forecast horizon, a
limitation that becomes more pronounced at longer lead times. Building on
this proof-of-concept over the South-Central US, future work will extend the
framework toward CONUS-wide application, supporting the broader goal of
operationally relevant LAI forecasting.
Acknowledgments
This research was supported by the NOAA Weather Program Office
(WPO)SubseasonaltoSeasonal(S2S)ProgramunderGrantNA23OAR4590386,
the NASA S2S Program under Award 80NSSC23K0504, and the CSU Scott
Foundation High-Impact Research Fund.
References
Amin, E., Verrelst, J., Rivera-Caicedo, J.P., Pipia, L., Ruiz-Verdú, A.,
Moreno, J., 2021. Prototyping Sentinel-2 green LAI and brown LAI prod-
ucts for cropland monitoring. Remote Sensing of Environment 241, 111712.
doi:10.1016/j.rse.2020.111712.
40

Barnes, S., 1964. A technique for maximizing details in numerical weather
map analysis. Journal of Applied Meteorology 3, 396–409. doi:10.1175/
1520-0450(1964)003<0396:ATFMDI>2.0.CO;2.
Bergstra, J., Bengio, Y., 2012. Random search for hyper-parameter optimiza-
tion. Journal of Machine Learning Research 13.
Bonan, G., 2008. Forests and climate change: forcings, feedbacks, and the
climate benefits of forests. Science 320, 1444–1449. doi:10.1126/science.
1155121.
Chen, J., Black, T., 1992. Defining leaf area index for non-flat leaves.
Plant, Cell & Environment 15, 421–429. doi:10.1111/j.1365-3040.1992.
tb00992.x.
Dong, W., Yuan, H., Lin, W., Liu, Z., Xiang, J., Wei, Z., Li, L., Li, Q., Dai,
Y., 2025. A global urban tree leaf area index dataset for urban climate
modeling. Scientific Data 12, 426. doi:10.1038/s41597-025-04729-y.
Du, L., Yang, H., Song, X., Wei, N., Yu, C., Wang, W., Zhao, Y., 2022.
Estimating leaf area index of maize using UAV-based digital imagery and
machine learning methods. Scientific Reports 12, 15937. doi:10.1038/
s41598-022-20299-0.
Forzieri, G., Castelli, F., Vivoni, E.R., 2011. Vegetation dynamics within
the north american monsoon region. Journal of Climate 24, 1763–1783.
doi:10.1175/2010JCLI3847.1.
Friedl, M., Sulla-Menashe, D., 2022. MODIS/Terra+Aqua Land Cover Type
Yearly L3 Global 500m SIN Grid V061. doi:10.5067/MODIS/MCD12Q1.061.
data set. Accessed: 2026-04-22.
Harper, K.L., Lamarche, C., Hartley, A., Peylin, P., Ottlé, C., Bastrikov, V.,
San Martín, R., Bohnenstengel, S.I., Kirches, G., Boettcher, M., Shevchuk,
R., Brockmann, C., Defourny, P., 2023. A 29-year time series of annual
300 m resolution plant-functional-type maps for climate models. Earth
System Science Data 15, 1465–1499. doi:10.5194/essd-15-1465-2023.
Kartal, S., Iban, M., Sekertekin, A., 2024. Next-level vegetation health in-
dex forecasting: A ConvLSTM study using MODIS time series. Environ-
mental Science and Pollution Research 31, 18932–18948. doi:10.1007/
s11356-024-32430-x.
Koch, S., DesJardins, M., Kocin, P., 1983. An interactive Barnes objective
map analysis scheme for use with satellite and conventional data. Journal
of Applied Meteorology and Climatology 22, 1487–1503.
Kumar, S.V., Mocko, D.M., Wang, S., Peters-Lidard, C.D., Borak, J., 2019.
41

Assimilation of remotely sensed leaf area index into the noah-mp land
surface model: Impacts on water and carbon fluxes and states over the
continental united states. Journal of Hydrometeorology 20, 1359–1377.
doi:10.1175/JHM-D-18-0237.1.
Lu, L., 1999. Implementation of a two-way interactive atmospheric and
ecological model and its application to the central United States. Ph.D.
thesis. Colorado State University.
Lu, L., Pielke, R., Liston, G., Parton, W., Ojima, D., Hartman, M., 2001.
Implementation of a two-way interactive atmospheric and ecological model
and its application to the central United States. Journal of Climate 14,
900–919. doi:10.1175/1520-0442(2001)014<0900:IOATIA>2.0.CO;2.
Lu, L., Shuttleworth, W., 2002. Incorporating NDVI-derived LAI into the
climate version of RAMS and its impact on regional climate. Journal of
Hydrometeorology 3, 347–362. doi:10.1175/1525-7541(2002)003<0347:
INDLIT>2.0.CO;2.
Mahowald, N., Lo, F., Zheng, Y., Harrison, L., Funk, C., Lombardozzi, D.,
Goodale, C., 2016. Projections of leaf area index in earth system models.
Earth System Dynamics 7, 211–229. doi:10.5194/esd-7-211-2016.
Menne, M., Durre, I., Vose, R., Gleason, B., Houston, T., 2012. An
overview of the Global Historical Climatology Network-Daily database.
JournalofAtmosphericandOceanicTechnology29, 897–910. doi:10.1175/
JTECH-D-11-00103.1.
Myneni, R., Knyazikhin, Y., Park, T., 2021. MODIS/Terra leaf area in-
dex/FPAR 8-day L4 global 500m SIN grid V061. doi:10.5067/MODIS/
MOD15A2H.061. [Data set]. NASA Land Processes Distributed Active
Archive Center.
Ogle, K., Reynolds, J.F., 2004. Plant responses to precipitation in desert
ecosystems: integrating functional types, pulses, thresholds, and delays.
Oecologia 141, 282–294. doi:10.1007/s00442-004-1589-1.
Peng, K., Zhang, Y., Liu, T., Li, Z., Liang, W., Liu, H., Bai, Y., 2026.
Research on dynamic prediction of vegetation coverage by precipitation-
evapotranspiration in arid regions based on CNN-LSTM hybrid model.
Scientific Reports 16, 1836. doi:10.1038/s41598-025-31530-z.
Pielke, R., Avissar, R., Raupach, M., Dolman, A., Zeng, X., Denning, A.,
1998. Interactions between the atmosphere and terrestrial ecosystems:
influence on weather and climate. Global Change Biology 4, 461–475.
doi:10.1046/j.1365-2486.1998.00176.x.
42

Shi, X., Chen, Z., Wang, H., Yeung, D., Wong, W., Woo, W., 2015. Con-
volutional LSTM network: A machine learning approach for precipitation
nowcasting, in: Advances in Neural Information Processing Systems, pp.
802–810.
Sulla-Menashe, D., Friedl, M.A., 2022. MODIS Collection 6.1 (C61)
Land Cover Type Product User Guide. Technical Report. LP DAAC.
URL:https://lpdaac.usgs.gov/documents/1409/MCD12_User_Guide_
V61.pdf.
Wang, Q., Lu, X., Zhang, H., Yang, B., Gong, R., Zhang, J., Jin, Z., Xie,
R., Xia, J., Zhao, J., 2023. Comparison of machine learning methods
for estimating leaf area index and aboveground biomass ofCinnamomum
camphorabased on UAV multispectral remote sensing data. Forests 14,
1688. doi:10.3390/f14081688.
Warter, M.M., Singer, M.B., Cuthbert, M.O., Roberts, D., Caylor, K.K.,
Sabathier, R., Stella, J., 2023. Modeling seasonal vegetation phenology
from hydroclimatic drivers for contrasting plant functional groups within
drylands of the Southwestern USA. Environmental Research: Ecology 2,
025001. doi:10.1088/2752-664X/acb9a0.
Xiong, Z., Zhang, Z., Gui, H., Zhu, P., Sun, Y., Zhou, X., Xiao, K., Xin,
Q., 2024. Predicting time series of vegetation leaf area index across
North America based on climate variables for land surface modeling us-
ing attention-enhanced LSTM. International Journal of Digital Earth 17,
2372317. doi:10.1080/17538947.2024.2372317.
Zhang, Z., Xin, Q., Li, W., 2021. Machine learning-based modeling of vegeta-
tion leaf area index and gross primary productivity across North America
and comparison with a process-based model. Journal of Advances in Mod-
eling Earth Systems 13, e2021MS002802. doi:10.1029/2021MS002802.
43
