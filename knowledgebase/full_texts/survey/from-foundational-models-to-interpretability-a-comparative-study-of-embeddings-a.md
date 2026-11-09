---
title: 'From foundational models to interpretability: a comparative study of embeddings and feature engineering
  for smallholder irrigation detection in Sub-Saharan Africa'
url: https://doi.org/10.3389/frsen.2026.1895172
category: survey
subcategory: empirical
date: 2026-08
venue: Frontiers in Remote Sensing
authors:
- Hasan Siddiqui
- Christopher Small
- Vijay Modi
source: openalex-oa
pdf_url: https://www.frontiersin.org/journals/remote-sensing/articles/10.3389/frsen.2026.1895172/pdf
pages: 12
chars: 52496
fetched_at: '2026-11-08T19:48:44+00:00'
kb_version: 1
---

# From foundational models to interpretability: a comparative study of embeddings and feature engineering for smallholder irrigation detection in Sub-Saharan Africa

TYPE Original Research
PUBLISHED 28 August 2026
DOI 10.3389/frsen.2026.1895172
From foundational models to
interpretability: a comparative
study of embeddings and feature
engineering for smallholder
irrigation detection in
Sub-Saharan Africa
Hasan Siddiqui1*, Christopher Small2 and Vijay Modi1
1Department of Mechanical Engineering, Columbia University, New York, NY, United States, 2Lamont
Doherty Earth Observatory, Columbia University, Palisades, NY, United States
Smallholder irrigation is crucial to livelihoods and growth in rural agro-
economies. Identifying where it occurs provides valuable insights for
agriculture extension, water management, infrastructure investments,
marketing and energy provision. Remote sensing methods can aid but have
been stymied by the small plot sizes, especially of irrigated plots. Humid
tropical climates are characterized by high temperatures and heavy seasonal
or year-round rainfall. This adds an additional layer of challenge due to fewer
cloud-free imagery from persistent cloud cover. This study focuses on these
settings to compare the performance, interpretability and transferability of
classification using embeddings versus a feature engineering approach.
Geospatial foundation models such as AlphaEarth Foundations (AEF) have
emerged to address the contrasting scarcity of high-quality labels in
comparison to increasing volumes of earth observation data. The embeddings
from these models have been shown to generate maps from sparse labels
outperforming traditional machine learning approaches in certain cases. In this
study, we utilize a nation-wide smallholder irrigation survey data from Uganda as a
data-rich region and pilot surveys from Zambia as a data-sparse region. We
present a reproducible cloud-native Earth observation workflow in Google Earth
Engine that discusses the tradeoffs and performance of the feature engineering
approach compared to foundational model embeddings. The results show that a
model trained on AEF embeddings outperforms a traditional feature engineering
approach on a rich label dataset. The performance is similar in a data-sparse
region. However, the embedding models do not lend themselves to auditable
methods for applicability to regions where no data is available.
KEYWORDS
alphaearth foundations embeddings, google earth engine (GEE), irrigation, phenology,
SHAP (shapley additive exPlanations), Uganda, Zambia
1 Introduction
Irrigation systems are vital to food security as they help meet crop water requirements
and facilitate the production of additional cash crops during the dry season. A review by
Giller et al., 2021 highlights the lack of significant growth in agricultural production in Africa
compared to the rest of the world. While increases of more than two to four-fold have been
OPEN ACCESS
EDITED BY
Qian Yu,
University of Massachusetts Amherst,
United States
REVIEWED BY
Bereket Tsehaye Haile,
University of Pretoria, South Africa
Zolo Kiala,
International Water Management Institute,
South Africa
*CORRESPONDENCE
Hasan Siddiqui,
hss2152@columbia.edu
RECEIVED 29 May 2026
REVISED 17 July 2026
ACCEPTED 31 July 2026
PUBLISHED 28 August 2026
CITATION
Siddiqui H, Small C and Modi V (2026)
From foundational models to
interpretability: a comparative study of
embeddings and feature engineering for
smallholder irrigation detection in Sub-
Saharan Africa.
Front. Remote Sens. 7:1895172.
doi: 10.3389/frsen.2026.1895172
COPYRIGHT
© 2026 Siddiqui, Small and Modi. This is an
open-access article distributed under the
terms of the Creative Commons
Attribution License (CC BY). The use,
distribution or reproduction in other
forums is permitted, provided the original
author(s) and the copyright owner(s) are
credited and that the original publication
in this journal is cited, in accordance with
accepted academic practice. No use,
distribution or reproduction is permitted
which does not comply with these terms.
Frontiers in Remote Sensing frontiersin.org01

observed across Asia, Europe, North America and Latin America
since the 1960s, only a modest 70% increase is associated with Africa.
Despite the stagnation in crop yields, Africa has seen a massive 250%
increase in cultivated area since the 1960s compared to a 60%
increase across Latin America or even a 20% decrease observed
across North America and Europe. Bjornlund et al., 2022 describes
the agricultural policies that are focused on exports as the reason
why food insecurity still exists in Africa. This focus has led to the
neglect of investment in infrastructure, introduction of technologies
and development of supply chains and markets.
Opportunities exist for expansion of smallholder irrigation in
East Africa. However, access to reliable markets, irrigation
technologies, credit services and poor water resource
management are some of the key challenges to adoption of
smallholder irrigation. Area under irrigation and thus agricultural
productivity can be improved by adopting a water-energy-food
(WEF) nexus perspective (Mabhaudhi et al., 2018). Smallholder
irrigation schemes are often located away from any prevalent grid
presence and rely on manual or diesel-powered pumps. The energy
demand associated with pumping water and agro-processing
present opportunities as a captive power. This combined with
household demand can be used for planning a mini-grid and off-
grid as the viable least cost solutions (Conlon et al., 2020). Irrigation
loads provide a unique energy flexibility option by shifting the load
during the daytime that complements the night time household
loads associated with lighting, e-cooking etc. (Kocaman et al., 2020).
African countries are characterized by infrequent census and
surveys marring the ability to monitor the progress. A review by
Burke et al., 2021 showed that the agricultural census in majority
African countries is 10–20 years apart. The increasing availability of
remote sensing data of varying temporal and spatial resolution
paired with machine learning models can detect patterns and
indicators of progress. (Ozdogan et al., 2010) provides a review
of different remote sensing methods utilized for mapping irrigated
areas. This paired with increasing earth observation data provides an
opportunity to reduce the overhead associated with national surveys
by allowing for more targeted survey methods.
A number of large-scale geospatial foundation models have been
released recently such as OlmoEarth developed by the Allen Institute
for Artificial Intelligence (Herzog et al., 2025), TESSERA (Temporal
Embeddings of Surface Spectra for Earth Representation and
Analysis) from University of Cambridge (Feng et al., 2025),
Prithvi-EO-2.0 from IBM in collaboration with European Space
Agency (Szwarcman et al., 2024) and AlphaEarth Foundations
(AEF) from Google (Brown et al., 2025). These transformer-
based vision models assimilate vast spatial, temporal and
measurement contexts enabling production of classification maps
from sparse labels. These foundation models have demonstrated
state-of-the-art performance on a number of EO applications such
as flood mapping, land cover mapping and crop mapping, etc.
However, the use case for other problems that might not be as
well-posed such as smallholder irrigation detection in Sub-Saharan
Africa compared to traditional feature engineering methods remains
unknown. This study aims at comparing the performance,
interpretability and transfer learning capabilities of the two
approaches.
In our previous work, we utilized a phenology map of the Sahel
to characterize the Sub-Saharan African landscape into regions with
single cropping cycles per year, dual cropping cycles per year and
evergreen vegetation (Siddiqui et al., 2025). This is dependent on the
onset and cessation of seasonal rainfall over Africa (Dunning et al.,
2016). A dry season irrigation detection methodology developed for
Ethiopian highlands was shown to be applicable in regions with
single cropping cycles such as Northern Nigeria and Burkina Faso
(Conlon et al., 2022). An extension of the work implemented the dry
season irrigation methodology using Google Earth Engine tools to
model temporal changes in irrigated areas (Siddiqui and Modi,
2024). However, these methods were only applicable to areas with a
prolonged dry season. In humid environments such as Uganda,
longer rainfall periods do not allow for vegetation to senesce thus
rendering irrigated croplands indistinguishable from non-
irrigated ones.
To address this limitation, this study considers two approaches.
First is a feature engineering approach that incorporates
topographic, climatic and anthropic variables in addition to the
vegetation phenologies used in the earlier work. Second is to utilize
embeddings from geospatial foundational models that compress
vast amounts of earth observation datasets for semantic search and
rapid classification tasks. In doing so, we compare and contrast the
two approaches for smallholder irrigation detection in Sub-Saharan
Africa. We define smallholder farms as plots that are of the order of a
10th of a hectare or less and often rely on surface water for irrigation
(extracting water from swamps and dambos). A national scale
survey dataset from Uganda serving as a data-rich region and
pilot surveys from Zambia serving as a data-sparse region are
used to quantify the performance of the two approaches. The
main contribution of this work is a novel workflow to extend
smallholder irrigation detection across humid tropical
environments thus addressing the limitations of our earlier work
(Siddiqui et al., 2025) which was limited only to dry-season
irrigation detection.
2 Materials and methods
This section provides a brief description of the survey dataset
collected in Uganda and Zambia and the remote sensing features
and datasets utilized in the study. Additional detail is provided in the
Supplementary Material including a table of input features.
2.1 Study regions and survey data
(Uganda; Zambia)
The first study region is Uganda which is characterized by
biannual rainfall in the South in the crescent along Lake Victoria
whereas the North receives annual rainfall with a short dry season
(Uganda Observed Climatology of Precipitation, 2026). A
classification of irrigation schemes in Uganda by scale of
irrigated area, water source and method of conveyance to the
field is provided by Wanyama et al., 2017. Smallholder farms are
usually informal irrigation systems developed without planning and
with little or no technical assistance. The majority of these systems
are located on the fringes of swamps.
The second study region is Zambia where the smallholder
farmers rely on dambos. Dambos are seasonally waterlogged
areas found in the headwater zones of drainage systems or
Frontiers in Remote Sensing frontiersin.org02
Siddiqui et al. 10.3389/frsen.2026.1895172

alongside streams. These areas provide grazing in the dry season.
They also retain enough moisture to grow dry season crops using
small-scale irrigation schemes (Turner, 1986). Several studies
provide an assessment of dambo hydrology in Southern Africa
and estimate the density of dambos in Zambia to be 15%–20% of
the total land area (Boast, 1990; Bullock, 1992).
A national scale survey designed to study irrigation among other
productive uses of energy (PUE) was conducted in Uganda. Due to
the focus on PUEs, a non-irrigated farm plot was only recorded
within a sample area if no irrigated farm plot was found. This
resulted in an imbalanced dataset of more irrigated (11,021) than
non-irrigated (3818) farm plots. Similarly a pilot survey was
conducted in Zambia to collect PUE data around proposed Rural
Electrification Master Plan (REMP) sites (Haanyika, 2008). The plot
coordinates from the survey were then used with high resolution
satellite imagery to draw polygons around irrigated farm plots
resulting in 217 irrigated polygons across Zambia. Similarly, a
total of 109 non-irrigated polygons were generated covering a
total area roughly similar to the irrigated polygons. More details
of the survey is provided in Section 1 of the Supplementary Material
and data can be accessed using the CWP data platform (Columbia
World Projects Energy for Productive Use, 2026).
2.2 Earth observation data and features
2.2.1 Optical imagery and vegetation indices
We rely on MODIS and Sentinel 2 imagery as the basis for all our
analysis. A false color composite of dry season imagery reveals large
scale irrigation schemes such as those shown in Figure 1 for Zambia.
Enhanced Vegetation Index (EVI) time series are used to capture
vegetation phenologies to train classifiers on the temporal modality
of cropping cycles of the agricultural farm plots.
2.2.2 Topographical datasets
Topographic features provide insight on accumulation of
moisture and are thus critical to methodology for detecting
smallholder irrigation reliant on surface water. We utilize a
HydroSHEDS void-filled DEM for elevation data obtained in
2000 by NASA’s Shuttle Radar Topography Mission (SRTM)
visualized in Figure 2 (Lehner et al., 2008). We also utilize other
products derived from DEM such as slope which indicates areas that
are unsuitable for agriculture due to the gradient, HAND and MTPI
which provide information about local features such as ridges and
valley bottoms.
Height Above Nearest Drainage (HAND) is a terrain analysis
technique that calculates the vertical distance between a point on the
landscape and its nearest drainage channel or river. It normalizes
elevation data based on the local drainage network, effectively
representing how high or low a location is relative to the nearest
stream (Nobre et al., 2011). Figure 3 shows a visualization of HAND
FIGURE 1
Dry season false color composite of Sentinel 2 imagery for
Central Zambia. SWIR, NIR and Blue are shown in the RGB channels
respectively. High resolution Google Earth imagery is shown for large
scale center-pivot irrigation schemes. Such schemes are easy to
identify using the Sentinel 2 false color composite.
FIGURE 2
Visualization of African topography which is a key indicator of
locations where surface water accumulates. A zoomed in view of
Uganda’s topography is shown.
FIGURE 3
Height Above Nearest Drainage (HAND) visualization for Uganda with
areas North of Mount Elgon and West Nile zoomed in. Ridges are shown in
red, drainage channels in blue and other areas in green.
Frontiers in Remote Sensing frontiersin.org03
Siddiqui et al. 10.3389/frsen.2026.1895172

for Uganda (Donchyts et al., 2016). The SRTM Multi-Scale
Topographic Position Index (MTPI) is used to characterize
landforms by comparing the elevation of a specific location to
the mean elevation of its surrounding neighborhood across
multiple spatial scales (Theobald et al., 2015). Derived from the
Shuttle Radar Topography Mission (SRTM) 30-m Digital Elevation
Model (DEM), MTPI is particularly effective for identifying
geomorphological features such as valley bottoms, ridge tops, and
mid-slope benches.
2.2.3 Climatic variables
We analyze feature variables such as precipitation and land
surface temperature. In the context of smallholder irrigation
detection, Land Surface Temperature (LST) is a critical climatic
variable that acts as a thermodynamic proxy for soil moisture and
evapotranspiration (ET). While vegetation indices like EVI measure
the “greenness” of a plant, LST provides insights into the plant’s
actual water stress and the cooling effect of irrigation. MODIS
(MOD11A1/A2) provides high temporal resolution (daily) but at
a coarse spatial resolution (1 km). CHIRPS provides precipitation
data. The WorldClim V1 Bioclim dataset provides 19 bioclimatic
variables derived from monthly temperature and precipitation data.
It covers the period from 1960 to 1991 and has a resolution of
927.67 m (Hijmans et al., 2005). This product was preferred over the
more recent but coarse ERA5-land product with a resolution of
11,132 m. A scatter plot comparing ERA5-land temperature and
precipitation data for 2023 to BIO1 and BIO12 is added to the
Supplementary Material. The plot reveals a spatial correlation
between the two products despite the temporal mismatch
justifying their inclusion in the feature set.
2.2.4 Anthropic variables
Proximity to surface water (such as rivers, streams or
permanent wetlands), high resolution settlements, and
markets dictate the feasibility of irrigation. Therefore we
incorporate anthropic variables that represent the human-
driven factors and infrastructure constraints that dictate
where irrigation is socio-economically feasible. A description
of the datasets used are described in the subsequent paragraph.
We threshold the raster layers to obtain a binary mask of the
relevant feature and utilize a euclidean-based distance kernel to
calculate the distance to the feature. This results in input feature
layers such as distance to surface water, distance to night lights,
etc., To train the classifiers.
The Global Surface Water (GSW) provides the location and
persistence of available surface water (Pekel et al., 2016). Meta
formerly Facebook in partnership with CIESIN utilized computer
vision techniques to map population density in the High-Resolution
Settlement Layer (HRSL). This layer provides a proxy for labor
availability and urban intensity. Nighttime light (VIIRS) also
provides similar insights and therefore is used as part of the
feature set. Reliable road access allows for the transport of
surplus perishables to urban markets before they spoil. The
Global Roads Inventory Project (GRIP) dataset provides recent
and consistent global roads dataset (Meijer et al., 2018).
Protected areas (national parks, wildlife reserves) represent a
hard constraint on agricultural expansion. Distance to Protected
Areas World Database on Protected Areas (WDPA) is therefore
considered in our feature study to determine its impact.
2.2.5 Phenology maps
Phenology maps provide a spatiotemporal characterization of
vegetation cycles (Small, 2012). Consistent with our previous study
pertaining to dry season smallholder irrigation detection across sub-
Saharan Africa, we generate a phenology map of Uganda. We extract
temporal end members that represent distinct MODIS 250 m
Enhanced Vegetation Index (EVI) time series. Next, we use a
MinMaxScaler (Xscaled � X − Xmin Xmax − Xmin ) to scale the MODIS EVI
values to Sentinel 2 to generate a phenology map at 10 m shown
in Figure 4. A comparison of the phenology maps from MODIS and
Sentinel 2 is provided in the Supplementary Material for validity.
The benefits are two-fold. Firstly it allows us to encode the
annual temporal signature of the vegetation through mixture
modeling of the temporal end members derived from distinct
MODIS 250 m Enhanced Vegetation Index (EVI) time series.
This reduces the dataset from 12 dimensions corresponding to
monthly mean EVI of each pixel for the year to 3 dimensions
corresponding to single cropping cycle, dual cropping cycle and
evergreen vegetation. The second benefit lies in being able to isolate
geographic regions dominated by specific phenologies to assess
model performance in those regions.
2.3 Classification, feature selection and
validation
Species Distribution Models (SDM) are used to model the
habitat suitability for a species by identifying the predictor
variables (Crego et al., 2022). We adapt this methodology to
model smallholder irrigation patterns in Sub-Saharan Africa after
identifying key predictor variables. This methodology requires
information about the occurrence of irrigation which is obtained
from survey datasets and various topographic, climatic and
anthropic variables described in the previous section. The
workflow shown in Figure 5 is as follows:
1. Collection and preprocessing of survey data
2. Generate a stack of datasets and variables to use for
predictions
3. Feature selection to identify key predictors
4. Generation of pseudo-absence data to augment survey data
5. Model fitting and prediction
6. Accuracy assessment
We generate a stack of input features described earlier (see
Section 2 of the Supplementary Material). Using farm plot locations
with labels (irrigated, non-irrigated) from the surveys, we extract
feature values for each location. This results in a tabular dataset of
features values paired with a target binary irrigation class. Next step
involves identifying highly correlated feature values to reduce data
redundancy, prevent model overfitting and improve computational
efficiency. Removing such features increases feature independence
enhancing model interpretability by avoiding misleading feature
importances.
Frontiers in Remote Sensing frontiersin.org04
Siddiqui et al. 10.3389/frsen.2026.1895172

FIGURE 4
Phenology Map of Uganda created using MODIS 250 m and Central Uganda using Sentinel 2 10 m EVI timeseries (zoomed in) for a region North of
Lake Kyoga. The corresponding temporal End Members relating to the distinct phenologies from MODIS used for mixture modeling are shown in the
subplot. Regions with single cropping cycles per year, dual cropping cycles per year and evergreen regions are shown in red, blue and green channels
respectively.
FIGURE 5
Flowchart of smallholder irrigation detection methodology to compare classifiers based on AEF embeddings and feature engineering. The feature
engineering workflow from collection, analysis, selection and classification is shown.
Frontiers in Remote Sensing frontiersin.org05
Siddiqui et al. 10.3389/frsen.2026.1895172

SHAP (SHapley Additive exPlanations) is a unified framework
that utilizes a game-theoretic approach to calculate the marginal
contribution of each feature to the model’s output (Lundberg and
Lee, 2017). In this study, we use SHAP to evaluate the specific
predictive importance value of each feature for feature selection. The
CatBoost machine learning model is used for irrigation classification
which is shown to outperform other gradient boosting frameworks
like XGBoost or LightGBM with default hyperparameters
(Prokhorenkova et al., 2017).
The classifier is trained on input features and the feature
importance is ranked by SHAP in descending order. The top
20 features are shown in Figure 6. Area of the plots which is
obtained from survey data by multiplying the short and long side
of the plot is ranked as the most important feature (see Uganda in
Supplementary Figure S5 for the full plot). While area is not used
for irrigation predictions in our study, it can be incorporated
through segmentation of smallholder plots from high-resolution
imagery or utilizing existing agricultural field boundary datasets
(Kerner et al., 2024). A beeswarm plot of the area feature reveals
that from the surveyed plots (that do not include the large
irrigation schemes), a plot is more likely to be irrigated if it is
a smallholder plot. The next two most important features are
HAND and SRTMmTPI suggesting that topography is a good
predictor of irrigation patterns. Similarly we would expect annual
EVI to be a good indicator of irrigation. The model also ranks the
latitude of the farm locations as important input features. While
we do not use the coordinates for our predictions to enable
transfer learning, we hypothesize that this is due to distinct
vegetation phenologies across Uganda. Therefore a breakdown
of the feature importances across Northern, Central and Southern
Uganda is added to the Supplementary Figure S5 of the
Supplementary Material.
SHAP cannot be used for causal inference. To drive conclusions
that extend beyond the model to enable transfer learning, we
examine the distributions of the feature values of the irrigated
and non-irrigated labels by utilizing a violin plot. Looking at the
anthropic variables in Figure 7, we see that these plots are closer to
settlements (as shown by DHRSL values) and further from protected
areas (as shown by DIPA/DNPA values). DOR1/DOR2 values
(distance to major and minor roads) show that irrigated areas
are situated closer to infrastructure. While the distributions of
these features across irrigated and non-irrigated plots do not
provide a meaningful way of segregating the two, we utilize these
features to exclude regions where we do not expect irrigation. For
example, a buffer of 5 km is applied to the DHRSL feature to reduce
the computation cost of identifying irrigated areas. This allows us to
develop other similar thresholds if needed to further
exclude regions.
Due to the class imbalance of more irrigation data points than
non-irrigated data points in the survey data, we generate pseudo-
absence data points where we expect irrigation to not exist. This is a
key step in SDM and can be approached through multiple
techniques. One technique involves masking out regions using
phenology maps where we do not expect irrigation to exist such
as evergreen and barren areas. Another technique used in this
methodology generates a 5 km distance buffer layer around the
survey data points to sample absence points for non-irrigated areas.
It is important to acknowledge the limitation and potential errors of
this method that the generation of these pseudo-absence points
might involve irrigated areas that were not captured in the survey.
We tested two sampling strategies of pseudo-absence points using
non-cropped areas from a cropland mask and using a 5 km distance
buffer layer. The results can be viewed in the Supplementary Table
S2. The 5 km distance buffer layer performed slightly better than the
cropland mask suggesting that the results are not an artifact of the
negative sampling strategy used. Another technique is to utilize
clustering algorithms to generate clusters of presence (irrigated
areas) and absence (non-irrigated areas) and sample more
pseudo-absence points from the latter cluster.
2.4 Ethics statement
Survey approval was obtained from local authorities along with
IRB approval for the 13,840 farmers that were interviewed in
Uganda. IRB approval was also obtained for the 95 sites surveyed
across Zambia. No uniquely identifiable data of the farmers was
collected.
3 Results
3.1 Benchmark performance (Uganda
and Zambia)
To assess model performance over a balanced dataset, we first
use a subset of the irrigation dataset from the Uganda survey so that
the number of irrigated and non-irrigated points are the same. This
helps to establish a baseline and facilitate a direct comparison
between the data-rich region in Uganda and a data-sparse region
in Zambia. To evaluate classifier performance, the dataset consisting
FIGURE 6
SHAP beeswarm plot showing distributions of feature values for
top 20 features ranked for a CatBoost model. Details of feature names
are listed in Section 2 of the Supplementary Material. Area and lat/lon
are excluded from the plot. The distributions of the feature values
show the impact of higher or lower values on the model output.
Frontiers in Remote Sensing frontiersin.org06
Siddiqui et al. 10.3389/frsen.2026.1895172

of irrigated and non-irrigated farm plot locations are split into 70%
training, 30% testing. Next we utilize methods in the Uganda dataset
such as pseudo-absence points to augment non-irrigated data points
and spatial block cross validation to reduce the impact of spatial
autocorrelation between training and testing datasets and improve
model generalizability.
Table 1 benchmarks the performance metrics of embeddings vs.
feature engineering approach across the two regions. To understand
how the embeddings contribute to the final outputs, we compared
Linear Regression with a Random Forest model for Uganda. This
provides insight into how the structure of the embedding space helps
with land cover classification. While a Random Forest model or a
neural network might improve the accuracy of the model, it masks
whether the information contained in the embedding space is
structured and lends to transfer learning. For smallholder
irrigation detection in Uganda, the Linear Regression model
performs similar to the Random Forest model revealing there is
not much non-linear structure to exploit.
In Zambia, the irrigated and non-irrigated polygons are
randomly split into the training (70% of polygons) and testing
set (30% of polygons). We compare three sampling strategies to
sample points from the polygons to study the impact of spatial
autocorrelation. The first strategy was to sample all 10 m pixels from
the polygons. The other two strategies involved decimation of the
nearest one and two neighbors along all four sides of the pixel
effectively being sampled at 20m and 30 m scale. This was repeated
three times across all sampling strategies for the two methods (AEF
embeddings and selected features) for cross-validation. A maximum
of 2% increase in average F1 score and accuracy was observed across
the sampling strategies with 30 m sampling showing higher
performance for both methods. Additionally, the smallholder
irrigated plots are of the order of a 10th of a hectare with
irrigation methods employed and irrigated crops grown differing
across each farmer. Therefore, the marginal F1 change observed
from the pixel-decimation robustness check can therefore be used to
conclude that a 30 m sampling strategy reasonably reduces spatial
autocorrelation effects. Table 1 reports the average performance
metrics for 30 m sampling across three different random splits of
polygons into training and testing sets. Detailed performance
metrics for all sampling strategies are added to the
Supplementary Material.
Figure 8 shows the output of a Random Forest model trained
using AEF embeddings and selected features for Zambia. We see
that the outputs based on embeddings overpredict irrigation across
Central Zambia away from settlement. These areas are masked using
distance to high resolution settlement in the feature engineering
approach demonstrating the benefits of interpretable features and
extension of conclusions drawn from the feature study in Uganda.
FIGURE 7
Violin plot of anthropic feature distribution values for irrigated and non-irrigated croplands shown. Distributions in light pink correspond to non-
irrigated croplands and in light blue are irrigated croplands. Distance to High Resolution Settlement Layer (DHRSL) is shown zoomed in.
TABLE 1 Performance metrics of models trained on AEF embeddings and selected features for Uganda (primary evaluation on balanced subset of survey data)
and Zambia.
Region Method Algorithm F1 score Precision Recall Accuracy
Uganda AEF Embeddings Linear Regression 0.711 0.703 0.718 0.716
Random Forest 0.702 0.702 0.703 0.718
Selected features Random Forest 0.733 0.710 0.760 0.722
Zambia AEF Embeddings Random Forest 0.940 0.942 0.939 0.923
Selected features Random Forest 0.942 0.935 0.950 0.924
Bold values represent higher performance metrics across the two methods.
Frontiers in Remote Sensing frontiersin.org07
Siddiqui et al. 10.3389/frsen.2026.1895172

Next using a spatial block cross-validation approach using the
entire Uganda survey data, we train 5 Random Forest models using
AEF embeddings and a selection of input features. The spatial
blocking ensures cross-validation across the distinct phenologies
in Uganda shown in Figure 4 earlier. Looking across the
performance metrics in Table 2, we see that the AEF embeddings
outperform the selected features for Uganda. The irrigation
predictions using these models is shown in Figure 9. Overall
similar patterns of irrigation are observed across the two outputs
with higher irrigation predictions across South-Western Uganda
and the crescent along Lake Victoria. The AEF embeddings based
model output predicts more irrigation than the selected features
based output especially along the cattle corridor. Another noticeable
feature of the latter output is the reliance on topography (from
HAND) to predict irrigation patterns in Central Uganda.
3.2 Feature interpretation and
variable ablation
To understand where smallholder farmers are irrigating in
Uganda, different remote sensing features for the locations
identified from the survey as irrigated and non-irrigated fields
FIGURE 8
Irrigation predictions for Zambia using (a) AEF embeddings and (b) selected features. Irrigated pixels are shown in green against a non-irrigated
background in black. Permanent water bodies are overlayed in white.
TABLE 2 Average performance metrics of 5 Random Forest models trained on
AEF embeddings and selected features for Uganda using spatial block cross
validation approach. Higher performance metrics across the two methods
are represented in bold.
Method F1 Precision Recall AUC Accuracy
AEF
Embeddings
0.824 0.777 0.876 0.886 0.886
Selected Features 0.809 0.796 0.822 0.863 0.788
Bold values represent higher performance metrics across the two methods.
FIGURE 9
Probability of irrigation in Uganda shown using a viridis color palette predicted using (a) AEF embeddings and (b) selected features as input features.
Permanent water bodies are overlayed in white.
Frontiers in Remote Sensing frontiersin.org08
Siddiqui et al. 10.3389/frsen.2026.1895172

are compared through a violin plot. This allows us to see if the
distribution for each feature varies significantly for irrigated vs. non-
irrigated croplands and to judge if the feature would be useful for
training a classifier. Feature distribution for annual EVI (Enhanced
Vegetation Index) show higher values for irrigated croplands as one
would expect. Irrigated areas are found at lower lying areas where
water accumulates and this is evident by looking at the distribution
of the multi-scale topographic index which shows the mean
elevation of a region. Another method of judging the importance
of a set of variables can be achieved by omitting them from the
model. Figure 10 shows an example of this where the omission of
anthropic variables results in the model predicting irrigation in the
cattle corridor in South Western Uganda.
In Zambia, smallholder irrigation is heavily reliant on the
riverine areas (dambos) which can be identified from Digital
Elevation Models (DEM). By examining Sentinel 2 dry season
imagery, we can identify irrigated croplands because they remain
greener than surrounding vegetation. However, this greenness alone
does not distinguish irrigated croplands from riparian vegetation.
This can be observed by looking at the monthly Sentinel 2 EVI time
series of irrigated, non-irrigated and forests/riparian areas in
Figure 11. In some cases, the EVI patterns of riparian areas are
very similar to those of irrigated croplands, making those areas
difficult to distinguish using EVI alone.
3.3 Transferability
To assess transferability, we perform a quantitative out of region
validation. This is done by visual labeling of polygons around other
REMP sites. While this method is not as definitive as ground-
collected labels used for training, high quality labels can be collected
by examining high-resolution imagery. Different historic dates are
examined using Google Earth Pro imagery to find traits similar to
those observed while labeling polygons around ground truth. If an
area appears to be cropped near dambos which is easily
differentiable from uncropped riparian vegetation due to crop-
spacing and hedges on the outskirts used to deter livestock, it is
labeled as irrigated. This process resulted in 881 visually labeled
irrigated polygons. We then utilize a cropland mask to sample non-
irrigated points outside the cropped areas.
The performance of the two approaches assessed on this dataset
is shown in Table 3. On average, the Random Forest model trained
on AEF embeddings has a higher F1 score and Recall whereas the
model based on feature engineering has a higher overall accuracy
and Precision. Qualitatively we observe in Figure 8 that the model
trained on embeddings overpredicts irrigation in Central Zambia.
4 Discussion
Our findings demonstrate a clear trade-off between model
efficiency and interpretability. In regions like Zambia where
labels are scarce, AEF embeddings perform at par with the
traditional feature engineering approach. This suggests that
FIGURE 10
Probability of irrigation in Uganda shown using a viridis color palette predicted using models trained (a) with anthropic variables and (b) without
anthropic variables. Permanent water bodies are overlayed in white.
FIGURE 11
Plots of Sentinel 2 EVI time series of mean, 25th and 75th
percentiles for Zambian Eastern Province. Irrigated, non-irrigated and
forests are shown in blue, red and green colors respectively.
Frontiers in Remote Sensing frontiersin.org09
Siddiqui et al. 10.3389/frsen.2026.1895172

foundation models offer a great alternative for rapid land cover
classification in areas with limited ground-truth data. This offers a
practical pathway in the absence of a well-defined feature set
constructed through the analysis of labor-intensive ground-truth
survey data. In the data-rich context of Uganda, the embeddings
based classifier outperformed the feature engineering approach on
most performance metrics.
While embedding models are highly effective for classification,
they function largely as “black boxes.” Furthermore geospatial
foundational models suffer from lack of standardization in
evaluations, testing and training protocols and release of pretrained
weights (Corley et al., 2026). This lack of transparency presents
challenges for researchers who require auditable results for policy
or causal inference. Conversely, the feature engineering approach
provides a clear, operational workflow. Analysis through SHAP and
feature distribution plots revealed that topography and vegetation
phenology from EVI time series remain the most potent indicators
of smallholder irrigation. These variables successfully capture the
preference of farmers to irrigate in low-lying areas where surface
water naturally accumulates. Such interpretability allows for the
development of specific thresholds to mask out regions for
inference reducing the computational cost. It also provides insights
into the socio-economic drivers of irrigation, such as proximity to
surface water and infrastructure.
Certain methodological choices made in this study might affect
results when applied using different techniques or to other regions.
This includes the choice of pseudo-absence sampling strategy. While
a comparison of using a 5 km buffer around irrigated samples
performed similar to utilizing a cropland mask (see Supplementary
Table S2), other strategies such as using phenology maps for
negative sampling might yield different results. Similarly another
caveat is the transferability which was assessed using visually labeled
irrigated polygons and non-irrigated points sampled from a
cropland mask. Finally, the choice of embeddings from the
geospatial foundation models mentioned in the introduction can
impact performance. These foundational models offer different
embedding dimensions such as 64 for AlphaEarth Foundations,
128 for OlmoEarth, 256 for TESSERA and 1024 dimensions for
Prithvi-EO-2.0. However, a PCA variance analysis revealed that
most embedding dimensions are redundant suggesting that the extra
capacity adds noise rather than signal (Robinson and Corley, 2026).
Beyond agricultural monitoring, the ability to map irrigation
clusters has direct implications for energy infrastructure.
Smallholder irrigation often represents a concentrated captive
power demand that can justify the deployment of mini-grids or
the extension of the national grid. By accurately detecting these
areas, developers can better estimate energy and water requirements,
facilitating the transition from manual labor or diesel generators to
more sustainable, electricity-based pumping solutions.
5 Conclusion
The identification of smallholder irrigation is fundamental to
understanding the productive uses of energy in Sub-Saharan Africa.
This study provides a comprehensive benchmarking of two distinct
remote sensing paradigms: the geospatial foundation model
embeddings from AlphaEarth Foundations (AEF) and a
traditional feature engineering approach incorporating
topographic, climatic, and anthropic variables. By utilizing survey
data from Uganda and Zambia, we evaluated how these methods
perform across varying levels of data density and climatic
complexity.
This research highlights that geospatial foundation models like
AlphaEarth Foundations provide quick classification that
outperform or remain on par with feature engineering methods
for smallholder irrigation detection in Sub-Saharan Africa. However
the feature engineering approach remains indispensable for
generating interpretable, auditable, and transferable insights.
Future efforts should focus on hybrid workflows that leverage the
predictive power of embeddings while maintaining the transparency
necessary for impactful policy decisions and energy access planning.
Data availability statement
The Google Earth Engine scripts and the Zambia training data
used for the results in this paper are available on Github at github.
TABLE 3 Performance metrics for different model runs for transferability in Zambia. Higher performance metrics across the two methods are represented in
bold.
Method Sampling Run F1 score Precision Recall Accuracy
AEF Embeddings 30 m 1 0.721 0.652 0.806 0.704
2 0.738 0.616 0.919 0.691
3 0.726 0.601 0.918 0.673
Average 0.728 0.623 0.881 0.689
Selected features 30 m 1 0.608 0.673 0.555 0.664
2 0.731 0.693 0.774 0.732
3 0.756 0.619 0.973 0.740
Average 0.700 0.661 0.767 0.712
Bold values represent higher performance metrics across the two methods.
Frontiers in Remote Sensing frontiersin.org10
Siddiqui et al. 10.3389/frsen.2026.1895172

com/hssiddiqui/Irrigation-Detection-Uganda-Zambia. The Uganda
Geodata can be requested via Redivis (The Quadracci Sustainable
Engineering Lab, 2026). A district level summary of the Uganda
survey data is available on the CWP data platform.
Ethics statement
The studies involving humans were approved by Institutional
Review Board (IRB). The studies were conducted in accordance with
the local legislation and institutional requirements. The participants
provided their written informed consent to participate in this study.
Author contributions
HS: Investigation, Writing – original draft, Formal Analysis,
Data curation, Visualization, Validation, Conceptualization,
Writing – review and editing. CS: Supervision, Writing – review
and editing. VM: Writing – review and editing, Funding acquisition,
Supervision.
Funding
The author(s) declared that financial support was received for
this work and/or its publication. Partial support for this effort was
provided by the National Science Foundation (INFEWS Award
Number 1639214), Columbia World Projects, Rockefeller
Foundation (eGuide Grant 2018POW004), OPML
United Kingdom (DFID) and Technoserve (BMGF).
Acknowledgments
The authors acknowledge Markus Walsh for discussion about
relevant feature sets and ensemble methods. The authors also
acknowledge the role of Edwin Adkins and Aftab Zindani in
survey design and training the survey teams to collect data
without which this study would not have been possible.
Conflict of interest
The author(s) declared that this work was conducted in the
absence of any commercial or financial relationships that could be
construed as a potential conflict of interest.
Generative AI statement
The author(s) declared that generative AI was used in the
creation of this manuscript. Generative AI (Gemini 2.5 Series)
was used in the creation of this manuscript. The tool was used
exclusively to write Google Earth Engine code which was modified
later by the authors and enhance the readability of the manuscript.
The AI system was not used to generate scientific ideas, perform data
analysis, or interpret results. All study design, data processing,
analyses, and conclusions are entirely the work of the authors,
who reviewed and verified all manuscript content.
Any alternative text (alt text) provided alongside figures in this
article has been generated by Frontiers with the support of artificial
intelligence and reasonable efforts have been made to ensure
accuracy, including review by the authors wherever possible. If
you identify any issues, please contact us.
Publisher’s note
All claims expressed in this article are solely those of the authors
and do not necessarily represent those of their affiliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsed by the publisher.
Supplementary material
The Supplementary Material for this article can be found online
at: https://www.frontiersin.org/articles/10.3389/frsen.2026.1895172/
full#supplementary-material
References
Bjornlund, V., Bjornlund, H., and Van Rooyen, A. (2022). Why food insecurity persists
in Sub-Saharan Africa: a review of existing evidence. Food Secur. 14 (4), 845–864. doi: 10.
1007/s12571-022-01256-1
Boast, R. (1990). Dambos: a review. Prog. Phys. Geogr. Earth Environ. 14 (2), 153–177.
doi: 10.1177/030913339001400201
Brown, C. F., Kazmierski, M. R., Pasquarella, V. J., Rucklidge, W. J., Samsikova, M.,
Zhang, C., et al. (2025). AlphaEarth foundations: an embedding field model for accurate
and efficient global mapping from sparse label data. arXiv. doi: 10.48550/ARXIV.2507.
22291
Bullock, A. (1992). Dambo hydrology in southern Africa—Review and reassessment.
J. Hydrology 134 (1–4), 373–396. doi: 10.1016/0022-1694(92)90043-U
Burke, M., Driscoll, A., Lobell, D. B., and Ermon, S. (2021). Using satellite imagery to
understand and promote sustainable development. Science 371 (6535), eabe8628. doi: 10.
1126/science.abe8628
Columbia World Projects Energy for Productive Use (2026). Available online at: https://
qsel.columbia.edu/cwp-epu-data-platform/.
Conlon, T., Wu, Y., Small, C., Siddiqui, H., Adkins, E., Modi, V., et al. (2020). A novel
method of irrigation detection and estimation of the effects of productive electricity
demands on energy System planning. AGU Fall Meet. Abstr., GC034–GC038.
Conlon, T., Small, C., and Modi, V. (2022). A multiscale spatiotemporal approach for
smallholder irrigation detection. Front. Remote Sens. 3, 871942. doi: 10.3389/frsen.2022.
871942
Corley, I., Lehmann, N., Robinson, C., Tseng, G., Fuller, A., Alemohammad, H., et al.
(2026). No one knows the state of the art in geospatial foundation models. arXiv. doi: 10.
48550/ARXIV.2605.12678
Crego, R. D., Stabach, J. A., and Connette, G. (2022). “Implementation of species
distribution models in Google Earth engine,” Divers. Distrib. Edited by B. Leroy, 28(5),
pp. 904–916. doi: 10.1111/ddi.13491
Donchyts, G., Winsemius, H., Schellekens, J., Erickson, T., Gao, H., Savenije, H. G., et al.
(2016). “Global 30m height above the nearest drainage. doi: 10.13140/RG.2.1.3956.8880
Dunning, C. M., Black, E. C. L., and Allan, R. P. (2016). The onset and cessation of
seasonal rainfall over Africa. J. Geophys. Res. Atmos. 121 (19). doi: 10.1002/2016jd025428
Frontiers in Remote Sensing frontiersin.org11
Siddiqui et al. 10.3389/frsen.2026.1895172

Feng, Z., Atzberger, C., Jaffer, S., Knezevic, J., Sormunen, S., and Young, R. (2025).
TESSERA: temporal embeddings of surface spectra for Earth representation and
analysis. arXiv. doi: 10.48550/ARXIV.2506.20380
Giller, K. E., Delaune, T., Silva, J. V., Descheemaeker, K., van de Ven, G., Schut, A. G.,
et al. (2021). The future of farming: who will produce our food? Food Secur. 13 (5),
1073–1099. doi: 10.1007/s12571-021-01184-6
Haanyika, C. M. (2008). Rural electrification in Zambia: a policy and institutional
analysis. Energy Policy 36 (3), 1044–1058. doi: 10.1016/j.enpol.2007.10.031
Herzog, H., Bastani, F., Zhang, Y., Tseng, G., Redmon, J., and Sablon, H. (2025).
OlmoEarth: stable latent image modeling for multimodal Earth observation. arXiv. doi:
10.48550/ARXIV.2511.13655
Hijmans, R. J., Cameron, S. E., Parra, J. L., Jones, P. G., and Jarvis, A. (2005). Very high
resolution interpolated climate surfaces for global land areas. Int. J. Climatol. 25 (15),
1965–1978. doi: 10.1002/joc.1276
Kerner, H., Chaudhari, S., Ghosh, A., Robinson, C., Ahmad, A., and Choi, E. (2024).
Fields of the world: a machine learning benchmark dataset for global agricultural field
boundary segmentation. arXiv. doi: 10.48550/ARXIV.2409.16252
Kocaman, A. S., Ozyoruk, E., Taneja, S., and Modi, V. (2020). A stochastic framework to
evaluate the impact of agricultural load flexibility on the sizing of renewable energy
systems. Renew. Energy 152, 1067–1078. doi: 10.1016/j.renene.2020.01.129
Lehner, B., Verdin, K., and Jarvis, A. (2008). New global hydrography derived from spaceborne
elevation data. Eos, Trans. Am. Geophys. Union 89 (10), 93–94. doi: 10.1029/2008EO100001
Lundberg, S. M., and Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions.
31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA.
Curran Associates, Inc. Available online at: http://papers.nips.cc/paper/7062-a-unified-
approach-to-interpreting-model-predictions.pdf(Accessed August 29, 2025).
Mabhaudhi, T., Mpandeli, S., Nhamo, L., Chimonyo, V., Nhemachena, C., Senzanje, A.,
et al. (2018). Prospects for improving irrigated agriculture in Southern Africa: linking
water, energy and food. Water 10 (12), 1881. doi: 10.3390/w10121881
Meijer, J. R., Huijbregts, M. A. J., Schotten, K. C. G. J., and Schipper, A. M. (2018). Global
patterns of current and future road infrastructure. Environ. Res. Lett. 13 (6), 064006. doi:
10.1088/1748-9326/aabd42
Nobre, A. D., Cuartas, L., Hodnett, M., Rennó, C., Rodrigues, G., Silveira, A., et al.
(2011). Height above the Nearest drainage – a hydrologically relevant new terrain model.
J. Hydrology 404 (1–2), 13–29. doi: 10.1016/j.jhydrol.2011.03.051
Ozdogan, M., Yang, Y., Allez, G., and Cervantes, C. (2010). Remote sensing of irrigated
agriculture: opportunities and challenges. Remote Sens. 2 (9), 2274–2304. doi: 10.3390/
rs2092274
Pekel, J.-F., Cottam, A., Gorelick, N., and Belward, A. S. (2016). High-resolution
mapping of global surface water and its long-term changes. Nature 540 (7633),
418–422. doi: 10.1038/nature20584
Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., and Gulin, A. (2017).
CatBoost: unbiased boosting with categorical features. arXiv. doi: 10.48550/ARXIV.
1706.09516
Robinson, C., and Corley, I. (2026). Compressing Earth Embeddings. Available online at:
https://geospatialml.com/posts/compressing-earth-embeddings/.
Siddiqui, H., and Modi, V. (2024). “Monitoring the impacts of disruption events on
agriculture through irrigation detection with remote sensing,” in 2024 IEEE Global
Humanitarian Technology Conference (GHTC). 2024 IEEE Global Humanitarian
Technology Conference (GHTC) (Radnor, PA, USA: IEEE), 286–291. doi: 10.1109/
GHTC62424.2024.10771556
Siddiqui, H., Small, C., and Modi, V. (2025). Operationalizing remote sensing methods
for smallholder dry season irrigation detection in Sub-Saharan Africa. Front. Remote
Sens. 6, 1661528. doi: 10.3389/frsen.2025.1661528
Small, C. (2012). Spatiotemporal dimensionality and Time-space characterization of
multitemporal imagery. Remote Sens. Environ. 124, 793–809. doi: 10.1016/j.rse.2012.
05.031
Szwarcman, D., Roy, S., Fraccaro, P., Gíslason, P. E., Blumenstiel, B., and Ghosal, R.
(2024). Prithvi-EO-2.0: a versatile multi-temporal foundation model for Earth
observation applications. arXiv. doi: 10.48550/ARXIV.2412.02732
The Quadracci Sustainable Engineering Lab (2026). Uganda geodata. Redivis. doi: 10.
71778/V2DW-7A53
Theobald, D. M., Harrison-Atlas, D., Monahan, W. B., and Albano, C. M. (2015).
“Ecologically-Relevant maps of landforms and physiographic diversity for climate
adaptation planning,”. Editor Y. Carmel, 10, e0143619. doi: 10.1371/journal.pone.
0143619
Turner, B. (1986). The importance of dambos in African agriculture. Land Use Policy 3
(4), 343–347. doi: 10.1016/0264-8377(86)90030-X
Uganda Observed Climatology of Precipitation (no date) Climate Change
Knowledge Portal (2026). Available online at: https://climateknowledgeportal.
worldbank.org/country/uganda/climate-data-historical (Accessed: May 19,
2022).
Wanyama, J., Ssegane, H., Kisekka, I., Komakech, A. J., Banadda, N., Zziwa, A., et al.
(2017). Irrigation development in Uganda: constraints, lessons learned, and future
perspectives. J. Irrigation Drainage Eng. 143 (5), 04017003. doi: 10.1061/(asce)ir.1943-
4774.0001159
Frontiers in Remote Sensing frontiersin.org12
Siddiqui et al. 10.3389/frsen.2026.1895172
