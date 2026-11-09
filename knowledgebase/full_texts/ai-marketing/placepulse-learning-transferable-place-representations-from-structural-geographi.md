---
title: 'PlacePulse: Learning Transferable Place Representations from Structural Geographic Data'
url: https://arxiv.org/abs/2610.13390
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Lucía García-Duarte
- Miguel Álvarez
- Diego Vicente
- Javier Pérez Trufero
- Javier de la Torre
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.13390
pages: 42
chars: 124016
fetched_at: '2026-11-08T13:25:32+00:00'
kb_version: 1
---

# PlacePulse: Learning Transferable Place Representations from Structural Geographic Data

PlacePulse: Learning Transferable Place Representations from
Structural Geographic Data
Lucía García-Duarte ∗, Miguel Álvarez ∗,
Diego Vicente, Javier Pérez Trufero, Javier de la Torre
(CARTO)
Abstract
Geospatial machine learning often depends on task-specific feature engineering over large
collections of sociodemographic, business, and environmental variables. Geospatial foundation
models offer reusable representations of place, but leading approaches typically encode dynamic
signals, such as mobility and search activity, or visual signals from satellite imagery. Few models
represent the static structural composition of places (who lives and works there, which businesses
operate there, and which risks they face) as transferable embeddings at fine spatial resolution. We
introduce PlacePulse, a structural geospatial foundation model that compresses 572 attributes,
expanded to 2,288 inputs through H3 neighborhood aggregates, into 256-dimensional unit-norm
embeddings for 1,055,537 H3 resolution-7 cells in the United States. We also introduce a reusable
two-axis benchmark that separates intrinsic representation quality from downstream predictive
utility across multiple targets and spatial supports. Intrinsically, the embeddings reconstruct
standardized inputs with meanR2 = 0.853, use 251 of 256 approximately decorrelated dimensions,
and show strong spatial organization, with Moran’sI = 0.93on the leading principal component
and autocorrelation persisting beyond the input radius. Extrinsically, across 74 held-out targets
from 12 external sources and four spatial supports, PlacePulse outperforms a dimensionality-
matched feature-selection baseline on targets unrelated to the training inputs and is competitive
with Google’s Population Dynamics Foundation Model, leading on health, economic, election,
economic-mobility and social-vulnerability outcomes, with relative strengths that vary by domain.
These findings position structural composition as a distinct and complementary modality for
geospatial foundation models, not simply a fallback where behavioral or imagery data are
unavailable.
Keywords:geospatial foundation model; embeddings; self-supervised learning; spatial index;
geographic representation learning; structural characteristics
1 Introduction
Geographic analysis increasingly depends on the ability to characterize places (Singleton and Spiel-
man, 2026). Whether the objective is to identify underserved neighborhoods, estimate environmental
risk, predict retail demand, or support public policy, analysts typically rely on large collections of
demographic, socioeconomic, business, and environmental variables to describe the composition
of geographic areas (Elbers et al., 2003; Luo and Wang, 2003; Mitchell and Chakraborty, 2015;
Roig-Tierno et al., 2013; Singleton and Spielman, 2014). In practice, however, constructing these
representations remains a labor-intensive process. Even relatively simple analyses require assembling
∗Corresponding authors:lgarciaduarte@carto.com,malvarez@carto.com
1
arXiv:2610.13390v1  [cs.LG]  9 Oct 2026

data from multiple sources, harmonizing spatial units, engineering derived variables, and selecting
task-specific features (Noardo, 2022). As the volume and diversity of available geospatial data
continue to grow, this repeated feature engineering has become one of the principal bottlenecks in
applied spatial modeling (Janowicz et al., 2020; Li et al., 2016; Singleton and Spielman, 2026).
Foundation models offer an alternative paradigm. Rather than designing features separately for
each application, a model is pretrained once on broad data to learn transferable representations that
can be reused across many downstream tasks with limited additional supervision (Bommasani et al.,
2021). In the geospatial domain, this idea has evolved from early region representation learning,
where neighborhoods or spatial units were encoded as dense embeddings (Yao et al., 2018), into
a rapidly expanding family of geospatial foundation models capable of producing general-purpose
representations at increasingly large spatial scales (Zhang et al., 2024; Chen et al., 2025). The
central objective is no longer to engineer variables for individual analyses, but to learn reusable
representations that capture meaningful characteristics of place.
Although the field has expanded rapidly, current geospatial foundation models have largely
converged around two dominant sources of information. One family learns representations from
dynamic behavioral signals, including mobility trajectories, visitation patterns, web-search activity,
and related traces of human activity. The Population Dynamics Foundation Model (PDFM)
(Agarwal et al., 2024) exemplifies this approach, demonstrating that behavioral signals can support
transferable geographic representations across diverse downstream prediction tasks. A second family
derives representations directly from visual observations, using self-supervised learning over satellite
or street-level imagery to encode the physical appearance of locations (Cong et al., 2022; Yan
et al., 2024; Brown et al., 2025). These two paradigms have substantially advanced geographic
representation learning and established the current foundation-model landscape.
Yet many applications in geography require representations that capture characteristics of
places that are comparatively stable over time and not directly observable from either behavioral
traces or visual appearance. We refer to this family of information as structural information: the
demographic, socioeconomic, commercial, functional, and environmental attributes that describe
how places are organized. Such information underpins a wide range of applications in urban planning,
public health, environmental assessment, market analysis, and policy evaluation (Elbers et al.,
2003; Elliott and Wartenberg, 2004; Mitchell and Chakraborty, 2015; Singleton and Spielman, 2014;
Wang and Yin, 2023). Despite its central role in geographic analysis, structural information has
received comparatively little attention as the primary basis for learning transferable geographic
representations. Existing work has typically incorporated structural variables as auxiliary inputs
within multimodal models or combined a limited set of demographic attributes with mobility signals
in city-scale settings (Cao et al., 2026; Huang et al., 2022; Wang et al., 2025; Wen and Zhou,
2024). This leaves open the broader question of whether structural information can itself support
general-purpose geographic representations that transfer across downstream tasks.
This gap is not merely methodological; it is also conceptual. Current foundation models implicitly
emphasize two complementary perspectives on geographic space: behavioral representations encode
how places are used, whereas imagery-based representations encode what places look like. We
argue that a third perspective deserves independent investigation: structural representations, which
encode what places are through their relatively stable socioeconomic, commercial, functional,
and environmental composition. Rather than viewing structural variables simply as covariates
to be added to behavioral or imagery models, we investigate whether they constitute a distinct
representation modality capable of supporting transferable geographic embeddings in their own
right.
To address this question, we develop a geospatial foundation model pretrained exclusively on
structural attributes derived from the Applied Geographic Solutions (AGS) national database
2

08/09/2026, 16:05 placepulse_ ﬁgure_editable2 (2).svg
ﬁle:///Users/lgarciaduarte/Downloads/placepulse_ﬁgure_editable2 (2).svg 1/1
Figure 1. Overview of the geospatial foundation model: how the embeddings are extracted and applied
to downstream tasks.A self-supervised autoencoder compresses a broad set of structural attributes per location
(sociodemographic, economic, health, climate, mobility, and others) into a single 256-dimensional, L2-normalized
embedding at H3 resolution 7. This representation drives two families of applications: (1) similarity-based retrieval
for tasks such as white-space analysis, twin-area and look-alike discovery, cannibalization and site screening, or market
segmentation; and (2) supervised prediction, where the embeddings serve as off-the-shelf features for regression and
classification at the native H3 resolution or aggregated to the target’s spatial unit.
(Applied Geographic Solutions, 2025a) (Figure 1). The model is trained in a self-supervised manner
using a masked autoencoder objective (He et al., 2022) over 572 structural variables, augmented with
features derived from neighboring cells to capture local spatial context. It produces compact 256-
dimensional vector embeddings for more than one million H3 resolution-7 cells (Uber Technologies,
2018) covering the United States. The embeddings are constrained to the unit hypersphere, so cosine
similarity is equivalent to the dot product. Nearest-neighbor retrieval across the full million-cell
grid can therefore be implemented as a single matrix product, enabling interactive similarity search
at national scale. We refer to the resulting representations as PlacePulse embeddings.
PlacePulse embeddings are evaluated from two complementary perspectives. Internally, we
assess whether the embeddings preserve the structural information from which they are learned
and examine the organization of the resulting latent space. Externally, we evaluate whether the
representations transfer to downstream prediction tasks across different targets and spatial supports,
including comparisons with PDFM. This allows us to distinguish the intrinsic properties of the
learned representation from its utility as a transferable feature set.
Our contributions are:
1. A new foundation model built on the structural characteristics of place.We develop
PlacePulse, a self-supervised model that learns transferable geographic representations from
demographic, socioeconomic, commercial, functional, and environmental attributes. PlacePulse
compresses 572 attributes and their neighborhood aggregates into 256-dimensional embeddings
for more than one million H3 resolution-7 cells across the United States (Figure 2).
2. A comprehensive benchmark of representation quality and predictive transfer.We
introduce a two-axis evaluation framework that combines intrinsic assessment of reconstruction
fidelity, latent-space structure, effective dimensionality, and spatial organization with extrinsic
evaluation across 74 targets from 12 external sources and four spatial supports, using a fixed
estimator and state-blocked cross-validation. Because the framework is independent of the
3

(a) PC1–PC3 as red, green and blue
PC1
PC2
PC3
(b) PC1 × PC2 bivariate
PC1
PC2
Basemap © CARTO, © OpenStreetMap contributors
Figure 2. Visualizations of the presented embeddings across the contiguous United States (H3 resolution
7,∼1.06M cells), colored by principal component analysis (PCA) of the 256-dimensional embeddings.
(a) The three leading components (PC1–PC3) are min–max scaled to the red, green, and blue channels of an image;
cells with similar colors have similar embeddings. (b) A bivariate map of the two leading components (PC1 and PC2),
each split into terciles and combined into a3×3color scheme, from low–low to high–high.
representation architecture and input data, it provides a common basis for comparing different
geospatial embeddings.
3. A systematic and transparent empirical evaluation of structural embeddings.We ap-
ply the proposed benchmark to characterize PlacePulse across intrinsic properties, downstream
tasks, and spatial supports, reporting both its strengths and limitations. PlacePulse produces
a compact and spatially coherent representation and outperforms a dimensionality-matched,
target-blind baseline on targets not used to train the autoencoder. Comparison with PDFM
reveals that neither representation consistently outperforms the other across domains and
spatial supports, suggesting that structural and behavioral representations capture different
aspects of place.
The remainder of the paper is organized as follows.Section 2reviews related work on geospatial
foundation models and region representation learning and positions our contribution.Section 3
describes the AGS data and preprocessing.Section 4details the model architecture, training, and
evaluation protocol.Section 5reports internal and downstream results.Sections 6and7discuss
implications, limitations, and conclusions.
2 Related work
This section reviews the evolution of geographic representation learning from early region embeddings
to contemporary geospatial foundation models, summarizes the principal self-supervised learning
paradigms underlying these models, and positions structural representations of place within this
broader landscape.
2.1 From region embeddings to geospatial foundation models
The idea that geographic regions can be represented as dense vectors emerged in urban computing,
where embeddings were learned to summarize neighborhoods or functional zones and transferred
across downstream prediction tasks (Yao et al., 2018). Rather than relying on manually engi-
neered geographic indicators, these methods sought to learn latent representations directly from
heterogeneous urban data (Wang et al., 2020; Huang et al., 2022).
4

One of the earliest examples is the work of Yao et al. (2018), who embedded urban zones from
human mobility patterns to recover functional similarity between neighborhoods. This established
the now common view of a geographic region as a learnable representation rather than merely a
collection of attributes. Subsequent work progressively incorporated additional data modalities.
Urban2Veccombinedstreet-viewimagerywithpointsofinteresttoproducemultimodalneighborhood
embeddings (Wang et al., 2020); Huang et al. (2022) learned semantic representations from POI
distributions; UrbanCLIP extended CLIP-style language-image pretraining to urban regions (Yan
et al., 2024); and CaLLiPer employed multimodal contrastive learning over POIs to learn transferable
urban representations while explicitly framing the resulting embeddings as geospatial foundation
models (Wang et al., 2025).
Across this literature, three characteristics are remarkably consistent. First, embeddings are
intended to be reusable representations rather than task-specific features. Second, information from
multiple modalities is increasingly integrated to characterize place. Third, the spatial domain is
typically limited to one or a small number of metropolitan areas. These developments established
the conceptual foundations from which today’s geospatial foundation models emerged.
2.2 Geospatial foundation models
Inspired by the broader foundation-model paradigm (Bommasani et al., 2021), recent work has
shifted from city-specific embeddings toward large-scale pretrained representations intended for
general downstream use. Recent surveys by Zhang et al. (2024), Chen et al. (2025), and Zhou et al.
(2026) document the rapid development of geospatial representation learning toward increasingly
general-purpose and foundation-model approaches, with substantial attention to the role of different
data modalities and heterogeneous spatial context, particularly remote sensing imagery and other
heterogeneous geospatial observations.
The first major family learns representations from dynamic human-behavior signals, including
mobility trajectories, visitation patterns, web-search activity, and related behavioral traces. PDFM
is the canonical example. It combines cartographic information, mobility-derived busyness, search
trends, and environmental variables within a graph neural network to produce transferable em-
beddings for U.S. ZIP Code Tabulation Areas and counties. Its demonstrated performance across
diverse socioeconomic, health, and retail prediction tasks illustrates the effectiveness of behavioral
signals as general-purpose geographic representations.
The second dominant family derives representations directly from Earth-observation and visual
imagery. Early work adapted masked-image modeling to remote sensing through models such as
SatMAE (Cong et al., 2022), Scale-MAE (Reed et al., 2023), Prithvi (Jakubik et al., 2023), and
Clay (Clay Foundation, 2024). Parallel efforts have employed contrastive objectives, including
SatCLIP (Klemmer et al., 2025), which aligns satellite imagery with geographic coordinates, and
UrbanCLIP (Yan et al., 2024), which aligns imagery with textual descriptions. More recently,
global embedding-field models such as AlphaEarth Foundations (Brown et al., 2025) and TESSERA
(Feng et al., 2026) produce dense embeddings for virtually every terrestrial location at fine spatial
resolution.
Although these two families differ substantially in their data sources, their representations
are primarily shaped either by how places are used (behavioral traces) or by what places look
like (imagery). Structural information, though incorporated as auxiliary information, has received
comparatively less attention as a primary signal for learning general-purpose geographic representa-
tions. This motivates investigating whether structural information alone can support transferable
representations of place.
5

2.3 Self-supervised learning for geospatial representations
The success of modern geospatial representations is closely tied to advances in self-supervised
learning, where representations are learned without downstream task labels by optimizing objectives
defined directly on the input data.
Three broad paradigms dominate current geospatial self-supervised learning. Reconstruction-
based methods learn compressed representations by recovering masked or corrupted inputs, an
approach widely adopted in remote sensing (Cong et al., 2022; Reed et al., 2023; Jakubik et al., 2023).
Contrastive methods instead maximize agreement between different views of the same location
while separating unrelated locations, forming the basis of Tile2Vec (Jean et al., 2019), SatCLIP
(Klemmer et al., 2025), UrbanCLIP (Yan et al., 2024), and CaLLiPer (Wang et al., 2025). A third
family learns representations by predicting spatial or temporal context, particularly in trajectory-
and graph-based models (Lin et al., 2021).
Our model belongs to the reconstruction-based family. Like previous self-supervised approaches,
it learns a transferable latent representation without downstream supervision. Unlike most existing
work, however, the reconstruction objective operates on high-dimensional structural tabular data
rather than imagery, trajectories, or graph neighborhoods. As noted by Chen et al. (2025),
structural tabular attributes remain comparatively underexplored as a pretraining signal despite
their importance for many applied geographic analyses.
2.4 Structural representations of place
While most geospatial foundation models derive representations from behavioral traces or imagery,
many applied spatial analyses depend primarily on structural descriptions of place. We use the term
structural representation to refer to a representation learned from relatively stable attributes that
characterize the composition and functional context of a location, rather than its observed activity
patterns or visual appearance. These attributes may include sociodemographic characteristics,
income and employment structure, business composition, commuting patterns, health conditions,
built-environment indicators, and exposure to environmental and climate-related risks.
Despite the central role of structural attributes in applied geography, urban planning, public
health, environmental assessment, and market analysis, they have received comparatively little
attention as the primary signal for transferable representation learning. Existing approaches generally
use such information in one of three ways. First, demographic, socioeconomic, or land-use variables
may appear as auxiliary inputs within multimodal models dominated by mobility, imagery, or textual
data (Cao et al., 2026). Second, POI- and semantics-based approaches capture specific components
of urban structure, particularly land use, business activity, and urban function, without representing
the broader composition of place (Huang et al., 2022; Wang et al., 2025). Third, a smaller body of
work explicitly treats demographic composition as a learnable regional representation (Wen and
Zhou, 2024).
The closest work to ours is Demo2Vec (Wen and Zhou, 2024), which learns region embeddings
using demographic information together with human mobility. Demo2Vec shares our premise that
demographic composition can form part of a transferable representation rather than serving only as
a set of task-specific covariates. It therefore provides an important demonstration that population
structure contains reusable geographic information. However, it is evaluated at the scale of New
York and Chicago, combines demographic variables with mobility traces, and focuses on a narrower
conception of structural information than the one considered here.
Our notion of structural representation is substantially broader than previous work. Rather
than encoding a single component of place, such as demographics, POIs, or land use, we seek to
6

represent its overall structural composition through a wide range of sociodemographic, economic,
commercial, commuting, health, and environmental attributes. We also isolate this modality by
excluding behavioral and imagery inputs, allowing its independent contribution to downstream
prediction to be evaluated directly.
2.5 Positioning our work
The literature reviewed above suggests that geospatial foundation models have largely converged
on two dominant sources of information: behavioral signals and visual observations. Structural
information, despite underpinning many applied geographic analyses, has mostly remained an
auxiliary source of information or has been explored only in city-scale settings.
Our work investigates whether structural information can itself support a general-purpose
geospatial foundation model. We pretrain exclusively on a broad collection of structural attributes
describing the socioeconomic, commercial, functional, and environmental composition of places,
producing transferable embeddings at a fine national scale. Rather than positioning structural
representations as a replacement for behavioral or imagery-based models, we investigate them as
a distinct representation modality and compare them directly with PDFM. By evaluating both
representations across the same downstream tasks, we examine whether their transfer performance
reveals differences in the information captured by structural and behavioral signals. We leave
explicit fusion of these modalities to future work.
3 Data
The proposed foundation model is trained on a comprehensive collection of harmonized structural
attributes describing the demographic, socioeconomic, commercial, functional, and environmental
characteristics of places across the United States. These attributes are assembled from multiple AGS
products and provide a consistent representation of each H3 spatial cell at national scale. This section
covers the data source and spatial frame (Section 3.1), the thematic feature families that form
the base attribute set (Section 3.2), the ring-aggregate features encoding neighborhood context
(Section 3.3), and the external data used only as downstream evaluation targets (Section 3.4).
3.1 Source and spatial frame
We build the model on the2025 Applied Geographic Solutions (AGS) demographic, consumer,
business, and environmental databasesfor the United States, indexed on Uber’s H3 hierarchical
hexagonal grid at resolution 7 (≈5 km2 per cell). The grid covers the populated U.S. footprint at
1,055,537 cells used for training and embedding generation.
We use the vendor-provided H3 resolution-7 product as the native analytical support, avoiding
an additional disaggregation or areal-interpolation step before training. H3 provides a consistent
hierarchical index and efficient neighborhood operations, although cell areas are not perfectly
constant and the choice of resolution still defines the spatial support of the learned representation.
The AGS estimates are modeled current-year values rather than direct observations: H3 res-7
level demographics are derived from private and public sources, including the 2020 Census and
the American Community Survey. Full details of the estimation methodology and source data are
documented by the vendor (Applied Geographic Solutions, 2025b).
7

3.2 Input features
The base feature set is assembled from several AGS source tables at H3 resolution 7. Some attributes
are taken directly from AGS (e.g. raw population and establishment counts), while others are
engineered during preprocessing: derived from raw AGS columns through aggregations, ratios, and
composite indices (e.g. age-band sums, dependency and sex ratios, density and intensity measures).
Grouped thematically, they cover the structural information shown inTable 1. These features are
derived from 1,058 raw AGS variables across the seven products. Additionally, an urbanity flag
(binary variable) engineered from population density, nighttime light, and road density was included
to help the model differentiate between urban and rural areas. A total of 572 base features were
used for training.
Table 1. Applied Geographic Solutions (AGS) data products used to build PlacePulse embeddings.
Product Description What we use from it
Current Year
Demographics
Hundreds of attributes of the
population, households, and
dwellings, with a special emphasis
on the labor force and household
income characteristics, including
discretionary and disposable
income.
Population and age structure, dependency and
sex ratios, educational attainment, household
composition, income distributions, housing
tenure/value/age/type, labor-force participation
and unemployment, commuting time and mode,
vehicle ownership, race/ethnicity and a diversity
index, language spoken at home, marital status,
occupation and industry mix, and class of worker.
Daytime
Demographics
Establishments and employees by
detailed industry, and estimates
of daytime employment by
occupation.
Establishment and employee totals, daytime
population, employment and establishment density,
retail sales, and per-industry and per-occupation
employee and establishment counts.
Non-Resident
Population
Estimates
Estimates of overnight tourist
stays by type of travel and type
of accommodation, including
seasonal estimates.
Visitor and worker flow volumes by type (business,
personal, food & beverage, hotel, etc.) with
quarterly distribution ratios and seasonal volatility
(quarter-over-quarter change and standard
deviation).
Demographic
and Business
Dimensions
Uncorrelated factors summarizing
attributes that describe the
character of neighborhoods and
commercial areas.
AGS’s pre-computed dimension indices capturing
affluence, age, family status, urbanity, density,
sector specialization, and related axes.
Population Health Includes vital statistics, fertility
and mortality by age group,
life expectancy, chronic health
conditions, and health risk
indicators.∗
Total annual births and deaths, death rates by sex,
and life expectancy (total, male, and female).
Journey to Work Summarized commuting flow
patterns that includes most
employees, expressed as inflow,
outflow, and resident workers.
Worker counts capturing both commute ends:
residents who live and work in the same cell,
residents who commute out, and workers who
commute in from elsewhere.
Natural and
Physical
Characteristics
Climate, environmental risks, air
quality, and composite measures,
as well as terrain and elevation.
Air quality (ozone, PM10, carbon monoxide),
annual maximum and minimum temperature,
heating and cooling degree days, terrain slope, a
walkability index, and a composite risk score.
Every product is delivered at H3 resolution 7.
∗The chronic-condition and health-risk variables of this product are held out as downstream evaluation targets (Section 3.4)
and are never model inputs.
8

3.3 Spatial context features: H3 k-ring aggregates
The final model is spatially aware: in addition to each cell’s own attributes, we included aggregate
features computed over its H3 neighborhood on the resolution-7 grid. For a focal celli, let
Rk(i) ={j:d H3(i, j) =k}(1)
denote the set of cells at H3 grid distance exactlyk from i, i.e. a ring rather than a cumulative
disk, where dH3(i, j)is the H3 grid distance between cellsi and j. The focal cell itself is excluded
from all neighborhood aggregates to prevent leakage of the center-cell value into the neighborhood
summaries, and to ensure that the added features represent the surrounding spatial context rather
than the cell’s local profile. For each hexagonal H3 cell the first and second rings contain at most
|R1(i)| = 6and |R2(i)| = 12cells respectively; aggregates are computed over those ring cells present
in the grid.
For each of the 572 base featuresx, we added three unweighted neighborhood statistics: the
mean over the immediate ring, the sample standard deviation over the immediate ring, and the
mean over the second ring.
The ring-kmean is
meank(x)i = 1 |Rk(i)| ∑ j∈Rk(i) xj, k∈{1,2}.(2)
The immediate-ring sample standard deviation is
sd1(x)i =
/radicaltp/radicalvertex/radicalvertex√ 1 |R1(i)|−1 ∑ j∈R1(i) (xj−mean 1(x)i)2.(3)
This procedure produces572×3 = 1 ,716spatial context features. Together with the 572 focal-cell
attributes, the final model input contains 2,288 features. Each embedding therefore encodes not
only a cell’s own profile but also the profile of its surrounding H3 neighborhood.
These spatial context features allow the model to distinguish places with identical focal-cell
statistics but different neighborhood contexts, such as an affluent enclave bordering a deprived area
versus one embedded in a uniformly affluent region. They also encourage embeddings to vary more
smoothly across space rather than changing abruptly at cell boundaries, and they provide additional
signal for cells whose own attributes are sparse or noisy by borrowing information from nearby cells.
3.4 Downstream evaluation targets
To evaluate the learned embeddings (Sections 4.4and5.2) we assemble a battery of target variables
from twelve external sources, spanning different spatial units: H3 res-7, ZCTA, census tract and
voting precinct (seeTable 2). None of these targets are used in training; they serve only to test
how well the embeddings predict held-out quantities. The count targets we construct (POI and
cell-tower counts) and the two Startup Cartography Project targets arelog1p-transformed as they
are extremely right-skewed and span four orders of magnitude.
The evaluation targets were selected to provide both out-of-domain validation and interpretable
links to known socio-economic, health, infrastructure, environmental, and political dimensions. Two
source relationships are useful for interpreting the results. First, the native-resolution health targets
are AGS-modeled disease-prevalence rates, such as diabetes and obesity, whereas the AGS Health
inputs used during training are limited to mortality and life-expectancy measures. Performance
9

on these targets therefore tests whether the embeddings capture broader health-related spatial
structure beyond the specific health variables seen in training. Second, the socio-economic targets,
including income and poverty, are sourced from USDA/Census and are conceptually related to some
AGS income attributes in the input set. These targets therefore provide a check on whether the
embeddings preserve meaningful socio-economic gradients. We note these relationships inTable 2
and return to them when interpreting the downstream results.
Table 2. Downstream evaluation target sources.
Source Year What it measures Native
unit
Evaluation
unit
# targets Relation to
training inputs∗
AGS
Health
2025 Adult disease-
prevalence rates:
diabetes, obesity,
high blood pressure,
cancer, high
cholesterol, stroke
H3
res-7
H3 res-7 6 AGS product
family and
correlated with
inputs, but these
variables are not
model inputs
CARTO
Spatial
Features
2025 Human Activity
Index (HAI, CARTO
derived), nighttime
lights (VIIRS),
cell-tower density
(OpenCellID)
H3
res-8
H3 res-7,
ZCTA (only
HAI)
4 (3 H3 res-7
+ 1 ZCTA)
Independent,
except nighttime
lights, which enter
only indirectly the
inputs through the
urbanity flag
OpenCellID2025 Cell-tower antennas Point ZCTA 1 Independent
Overture
Maps
2025 Point-of-interest
counts by 11
categories
Point H3 res-7,
ZCTA
22 (11 H3 res-
7 + 11 ZCTA)
Independent;
related to AGS
establishment
counts (by industry
rather than place
category)
Google
PDFM
(conus27)
benchmark
Mixed∗∗ CDC PLACES
health indicators;
Census/ACS income
and home value;
nighttime lights,
tree cover, elevation,
population, density
ZCTA ZCTA 28 Independent;
income and health
indicators correlate
to some AGS
inputs, but are
not direct model
inputs (different
source).
USDA
ERS Food
Access
Atlas
2019 Low-food-access
population share,
poverty rate, median
family income
ZCTA ZCTA 3 Independent;
though income and
poverty correlate
with some AGS
inputs (different
source)
NREL /
U.S. DOE
LEAD
2022 Household energy
cost and energy
burden
ZCTA ZCTA 2 Independent
NYT
presidential
election
2024 Percent Democratic
lead
Precinct Precinct 1 Independent
Opportunity
Atlas (Op-
portunity
Insights)
2018 Upward income
mobility at age
∼35 for children of
parents at the 25th
income percentile
Tract Tract 1 Independent;
linked tax/census
records
10

Source Year What it measures Native
unit
Evaluation
unit
# targets Relation to
training inputs∗
FEMA
National
Risk Index
2025 Social vulnerability
to hazard impact,
community resilience
and capacity to
recover
Tract Tract 2 Independent;
indicators are
built from
sociodemographic
variables that
correlate with
inputs
Social
Capital
Atlas
2022 Economic
connectedness (cross-
class bridging),
friending clustering
ZIP ZCTA 2 Independent;
derived from
the Facebook
friendship graph
Startup
Cartogra-
phy Project
2016 Startup formation
rate, Regional
Entrepreneurship
Cohort Potential
Index
ZIP ZCTA 2 Independent;
derived from
business
registration records
Total— — — H3 res-7 20 —
— — — ZCTA 50 —
— — — Others 4 —
— — —All 74—
∗Independentindicates that the target is drawn from a source other than the AGS products used as PlacePulse inputs.
∗∗The Google PDFMconus27 benchmark combines variables from multiple sources. We verified the 2022 vintage for the CDC
PLACES health indicators, but the available documentation does not specify source years for the remaining variables. We
therefore treat the benchmark as mixed-vintage and partially documented.
4 Methods
We learn a transferable structural representation for each H3 resolution-7 cell using a self-supervised
masked autoencoder trained exclusively on the structural attributes described inSection 3, without
downstream task labels. The model compresses the standardized structural feature vector into
a compact 256-dimensional embedding and learns to reconstruct masked portions of the input,
encouraging the latent representation to capture relationships among the structural characteristics
of place. Once trained, the encoder is used as a fixed feature extractor that maps every H3 cell to a
single embedding for reuse across diverse downstream tasks. The following subsections describe the
model architecture (Section 4.1), the masked reconstruction objective (Section 4.2), the training
procedure (Section 4.3), and the evaluation protocol used to assess both the intrinsic properties
and downstream utility of the learned representations.Figure 3summarizes the training and
evaluation methods.
4.1 Architecture
We use a fully-connected (dense) autoencoder where spatial context is incorporated through the
k-ring-aggregate features introduced inSection 3.3, allowing the network to learn from both the
attributes of each cell and those of its surrounding neighborhood without requiring an explicitly
spatial architecture.
The encoder and decoder are symmetric, funnelling the 2,288-dimensional input through pro-
gressively narrower layers to the 256-dimensional bottleneck and mirroring that path back out to
11

(a) Representation learning: masked autoencoder over structural features
H3 res-7 cell + spatial
context (k-ring ≤  2)
1,055,537 cells
2,288 standardized features
30% of positions
masked (learnable
per-column token)
‖e‖ = 1
(unit sphere)
reconstruction
MSE in z-space,
masked positions
only
Loss share, center : ring   (center ×2, ring ×0.667)
25 : 75   uniform
50 : 50   weighted
Per-layer block:  Dense (He-normal) →  LeakyReLU (α = 0.1) →  BatchNorm →  Dropout (0.1)
Training:  Adam (lr 3 × 10−4, clipnorm 1.0), batch 512, ≤  400 epochs, early stopping on validation loss (patience 20), ReduceLROnPlateau (patience 10), 90 / 10 split
Encoder
1024 · 512 · 384
Decoder
384 · 512 · 1024
256-d
572 own 1,716 ring
(b) Evaluation protocol: frozen encoder, two complementary axes
Internal (intrinsic) evaluation: compression and structure
Downstream (extrinsic) evaluation: predictive usefulness
Encoder frozen
no fine-tuning on any target
Embeddings  1,055,537 × 256
one vector per H3 res-7 cell
Reconstruction fidelity
• overall and per-feature R2
• normalized MSE (z-score units)
• no masking: all 2,288 outputs
   predicted from the 256-d code
How much of the 2,288-feature signal
survives the 256-d bottleneck.
Space health and dimensionality
• per-dimension variance and shape
• dead dims (σ < 0.01)
• decorrelated dims (greedy, |r| ≤  0.8)
• PCA participation ratio
• Levina–Bickel k-NN MLE
Reported for the standardized input
and the embedding alike.
Spatial structure
• Neighbourhood coherence
   (H3 k-rings 1–5, ZCTA)
• Moran's I, k-ring = 1–5
• Getis–Ord G * i , k-ring = 3
• mini-batch k-means, k = 10/50/100
Does the space vary coherently across
geography (Tobler's first law).
H3 res-7 (native)
• 20 regression tasks
• PlacePulse: no aggregation, the
   model's own resolution
• compared against a 256-column
   feature selector baseline
Measures what learned compression
adds over raw feature selection.
ZCTA (external benchmark)
• 50 regression targets
• PlacePulse: area-weighted H3 →  ZCTA
• compared against PDFM native ZCTA
   embeddings
Measures both models against an
external embedding benchmark.
Other supports
• 4 regression targets
• PlacePulse: area-weighted H3 →
   target geographic support
• compared against PDFM:
   area-weighted ZCTA →  target
   geographic support
Measures both models' adaptability
to other geographic units.
LightGBM, identical configuration for every target and feature set (500 trees, lr 0.05, 63 leaves)   ·   5-fold cross-validation blocked by U.S. state
Figure 3. Overview of the methodology.(a) A masked autoencoder compresses 2,288 standardized features per
H3 res-7 cell (572 own + 1,716 k-ring aggregates) into a 256-dimensional embedding on the unit sphere, reconstructing
only the 30% of positions masked at each step, with center columns upweighted to offset the 3:1 ring majority. (b) The
frozen encoder is applied to all 1,055,537 cells, and the embeddings are evaluated both intrinsically and as downstream
predictors at three spatial supports (seeSection 4.4).
12

Table 3. Model configuration summary.
Component Specification
Input / output 2,288 features (572 own + 1,716 ring aggregates)
Encoder Dense [1024, 512, 384]→Dense 256 (linear)→L2 (unit) normalization
Decoder Dense [384, 512, 1024]→Dense 2,288 (linear)
Embedding 256-d, constrained to the unit sphere (∥e∥= 1)
Per-layer block Dense (He-normal init)→LeakyReLU (α= 0.1)→BatchNorm→Dropout (0.1)
reconstruct the full vector. Each hidden layer is a standard regularized block (a dense projection
followed by LeakyReLU activation, batch normalization, and dropout) and the bottleneck itself is
a linear projection followed by an explicit L2-normalization layer, which places every embedding
exactly on the unit hypersphere by construction.Table 3summarizes the configuration.
4.2 Masked, spatially-weighted reconstruction loss
The reconstruction objective incorporates two design choices intended to encourage the learned
embeddings to capture relationships among the structural attributes while maintaining a balanced
representation of both focal-cell and neighborhood information.
1. Masked reconstruction.During each training step every input position is independently
masked with probability 0.30; masked positions are replaced with a learnable per-column
“mask token” (a trainable vector initialized to zero) before encoding, and the reconstruction
loss is computed only on the masked positions. This forces the encoder to infer each masked
feature from the others, yielding a representation that captures cross-feature structure rather
than copying inputs. Because a fresh random subset is masked every step, the masking also
acts as input-level data augmentation, keeping the train–validation gap small. Masking is
applied only during training; at inference the encoder receives the complete, unmasked feature
vector to generate the final embeddings.
2. Center-vs-ring loss weighting.Because ring-aggregate columns outnumber a cell’s own
columns 3:1 (1,716 vs 572), an unweighted reconstruction loss starves the gradient on the
cell’s own features and degrades fidelity in dense-urban cells. We therefore apply a two-tier
weighting: the cell’s own (“center”) columns are weighted×2.0and ring columns ×0.667,
rebalancing the effective loss contribution from≈25:75to ≈50:50center:ring. This restores
the encoder’s fidelity to each cell’s own attributes while retaining the neighborhood signal
that the ring aggregates provide.
The objective is then mean squared error in z-score space, evaluated over masked positions only,
with each position scaled by its center/ring group weight. Writingxi∈R D for the standardized
input of cell i with D = 2 ,288, ˆxi for its reconstruction, mid∈{ 0, 1} for the mask indicator of
positiond, andw d for the center/ring group weight of positiond, the loss over a batchBis
L=
∑
i∈B
∑D
d=1 mid wd (xid−ˆxid)2 ∑
i∈B
∑D
d=1 mid wd
, w d =
{
2.0ifdis a center column,
0.667ifdis a ring column. (4)
4.3 Training
We train the model to minimize the masked, group-weighted reconstruction objective ofSection 4.2
using the Adam optimizer (Kingma and Ba, 2015), with early stopping on the validation split to
13

Table 4. Model training summary.
Setting Value
Optimizer Adam, learning rate3×10 −4, gradient clipping (clipnorm= 1.0)
Batch size 512
Max epochs 400
Early stopping on validation loss (patience 20, min-∆ 1×10 −4)
LR schedule ReduceLROnPlateau (patience 10)
Train / validation 90% / 10%, random seed 42
select the final weights. The data are split 90%/10% into training and validation.
Because the model is used as a fixed feature extractor over a closed, fully-observed grid rather
than to predict unseen locations, we do not hold out a separate test set; the validation split governs
early stopping and provides a held-out check on reconstruction quality. After training the encoder is
applied to all 1,055,537 cells to generate the embeddings.Table 4lists the full training configuration.
4.4 Evaluation protocol
We evaluate the embeddings along two complementary axes. Internal (intrinsic) evaluation assesses
the representation on its own terms, without reference to any external labels, measuring how
faithfully it encodes the input and how well-structured the resulting space is. Downstream (extrinsic)
evaluation measures the embeddings’ usefulness as predictors for independent real-world targets.
The two are complementary: a representation may be internally well-conditioned yet of limited
predictive value, or vice versa, so we report both.
Internal evaluation.We assess the representation with three families of diagnostics, all
computed on the released encoder over the full H3-cell grid.
1. Reconstruction fidelity.Because the model is trained only to reconstruct its input, this
directlymeasureshowmuchofthe2,288-featuresignalthe256-dbottleneckpreserves(afaithful,
near-lossless compression is the precondition for the embedding to be useful downstream). We
report overall and per-featureR2 on the raw feature scale, and normalized MSE in z-score
units between the 2,288-d input and its reconstruction. At evaluation we apply no masking
and feed the complete input, so all outputs come from the 256-d code alone.
2. Embedding-space health and dimensionality.We evaluate whether the information
learned by the encoder is effectively distributed across the embedding space rather than
concentrated in a small number of dimensions. We examine per-dimension variance and
distributional shape; the count ofdeaddimensions (per-dimension standard deviation below
0.01); the number of mutually decorrelated dimensions from a greedy test that discards
any dimension whose absolute Pearson correlation with an already-retained one exceeds
0.8; and two intrinsic-dimensionality estimators reported for both the standardized input
and the embedding: (i) the PCAparticipation ratio, equivalently the effective number of
spatial degrees of freedom (Bretherton et al., 1999) or then2 effective-dimensionality index
(Del Giudice, 2021), which measures how evenly variance is spread across components; and (ii)
the Levina–Bickel maximum-likelihood estimator, a local k-NN measure robust to nonlinear
structure (Levina and Bickel, 2005).
3. Spatial structure.Because the embeddings are meant to describe places, we check that they
vary coherently across geography (nearby places should be similar, following Tobler’s first law
14

of geography, Waters, 2017) rather than being spatially random, and characterize the scale
and form of that structure. We measure: (i)neighborhood coherencefor each cell as the cosine
similarity between its embedding and the mean embedding of its surrounding neighborhood (an
H3 k-ring disk within radiusk, fork = 1–5 for adjacency, or its ZCTA for administrative units),
each contrasted with a baseline that compares the cell to a randomly reassigned neighborhood
of the same type (significance is assessed with a 99-run permutation test,p≤ 0.01); and we
report both the raw cosine and a mean-centered variant (embeddings minus the global-mean
vector), under which the random baseline collapses to∼0so the statistic isolates excess
local similarity beyond the national average; (ii)global spatial autocorrelationby computing
Moran’s I (Moran, 1950) over H3 k-ring adjacency with row-standardized weights, computed
on the leading PCA components and on each of the 256 dimensions, with permutation-based
significance and a correlogram over ring distancesk = 1–5; (iii)local hotspot structurethrough
a Getis–Ord G∗ i analysis (Getis and Ord, 1992; Ord and Getis, 1995) with uniform weights
over H3 k-ring-3 neighborhoods, combining the 256 per-dimensionG∗ i z-scores into a single
per-cell statistic through a standardized sum (Stouffer et al., 1949; Whitlock, 2005); and
(iv)mini-batch K-means cluster structure(Sculley, 2010) atk = 10/50/100, measuring size
balance, cluster-size entropyH (Shannon, 1948) and its effective-cluster equivalent2H, the
number of equally-sized clusters carrying the same entropy (Hill, 1973), and within-cluster
sum of squares.
Downstream evaluation.The embeddings are evaluated as predictors across a battery of
supervised regression tasks (20 at native H3 res-7, 50 at ZCTA, and 4 at other geographic support
levels) in every case using 5-fold cross-validation with gradient-boosted decision trees (LightGBM;
Ke et al., 2017). All targets use an identical LightGBM configuration (n_estimators = 500,
learning_rate = 0.05, num_leaves = 63); no per-target or per-feature-set tuning, so differences
reflect the representation, not the estimator.
We report the evaluation in three settings:
1. At the native resolution of the embeddings (H3 res-7).Targets available at H3 res-7
are predicted directly from the 256-d cell embeddings, quantifying how well the structural
representation predicts each target at the model’s native, fine resolution. Because no external
open-source embedding product is available at H3 resolution 7, we compare PlacePulse to
an internal dimensionality-matched, target-blind feature-selectionbaseline. This baseline is
constructed from the original input features: the 2,288 standardized inputs are grouped using
agglomerative clustering and cut into 256 clusters, and one medoid feature is retained from
each cluster. The medoid is defined as the feature with the smallest mean distance to the
other features in its cluster. The resulting 256-feature set is selected once, without access to
any target labels, and is used unchanged across all prediction tasks, preventing label leakage
into any cross-validation fold. The feature-selection baseline is deliberately strong: it retains
interpretable AGS columns, reduces redundancy among correlated inputs, and broadly covers
the original input space. The comparison therefore asks whether the encoder earns its 256
learned dimensions over a simple target-blind selection of 256 representative input features.
2. At ZCTA resolution, against external baselines.Targets defined at ZCTA are predicted
after aggregating PlacePulse embeddings from H3 res-7 up to ZCTA through an area-weighted
mean, each cell contributing in proportion to its area of overlap with the ZCTA. This lets
us benchmark against external baselines, notably Google’s Population Dynamics Foundation
Model (PDFM; Agarwal et al., 2024), which is published natively at ZCTA/county and
therefore enters the comparison with no aggregation of its own. Both models are thus
15

evaluated on the same ZCTA prediction task, but only PlacePulse is aggregated to get there.
The comparison is therefore conservative for our model: PDFM is evaluated at the native
resolution it was trained on, whereas PlacePulse is evaluated through an area-weighted mean
of embeddings learned for H3 cells. Note that the 5-fold cross-validation and LightGBM
configuration differ from the original PDFM evaluation (Agarwal et al., 2024), which used
different LightGBM hyperparameters and a single holdout of 20% of states, so absoluteR2
values are not directly comparable with those reported there.
3. At other target resolutions.The same target-resolution procedure extends to spatial units
other than ZCTA. Here neither model is native to the target unit, so both PlacePulse and
PDFM are area-weighted to the target resolution (i.e. the voting precinct). The transfer
is not symmetric, because the two native supports differ in size and in how they align with
the target units. Because ZCTAs, tracts and precincts are all built from census blocks, most
target units fall almost entirely inside a single ZCTA. PDFM therefore transfers cleanly but
at a coarse resolution (all units inside one ZCTA share one embedding), whereas PlacePulse
transfers at a finer resolution but mixes values across neighbouring units. Because H3 is a
regular hexagonal grid, its cell boundaries are independent of census geography and rarely
coincide with tract or precinct boundaries: units that straddle several cells receive a blend of
their neighbours’ embeddings, while units small enough to fall entirely inside one cell receive
that cell’s embedding unchanged, shared with every other unit in the same cell.
Because all reported targets have nationwide coverage, we usespatially blocked cross-validation
throughout, grouping observations by U.S. state so that all cells from a given state are assigned
to the same fold. Holding out whole states reduces leakage from spatial autocorrelation between
nearby training and test observations and provides a more conservative estimate of geographic
generalization. Folds are constructed to contain approximately similar numbers of H3 cells. We
report the average and standard deviationR2 across the 5 held-out folds for each downstream task.
5 Results
We organize results along the two axes presented inSection 4.4.Section 5.1reports the internal
evaluation (reconstruction fidelity, embedding geometry, and spatial/cluster structure) over the
full 1,055,537-cell grid.Section 5.2reports the downstream evaluation against PDFM and a
feature-selector baseline model.
5.1 Internal evaluation
The intrinsic evaluation examines the properties of the learned embedding space. We first assess
reconstruction fidelity to quantify how accurately the compressed representation preserves the original
structural information. We then analyze the statistical and spatial properties of the embedding
space through complementary measures of representation geometry and spatial organization.
5.1.1 Reconstruction fidelity
The autoencoder reconstructs the standardized input with averageR2 = 0.853, corresponding to
a normalized MSE of 0.147 in z-score units, where 1.0 is a per-feature mean predictor and 0.0 is
perfect reconstruction. The per-featureR2 distribution (Figure 4a) is tight and uniformly positive:
median R2 = 0 .887, with p10 = 0 .686and p90 = 0 .968. None of the 2,288 features hasR2 < 0,
so no feature is reconstructed worse than its own mean. Residuals, computed as observed minus
16

0.0 0.2 0.4 0.6 0.8 1.0
R 2 per feature
0
100
200
300
400Number of features
(a) Reconstruction quality (n = 2,288 features)
median R 2 = 0.887
−1.0 −0.5 0.0 0.5
Pairwise Pearson r (off-diagonal)
0
800
1600
2400Number of dim pairs
(b) Decorrelation (32,640 dim pairs)
median r = +0.000
0 50 100 150 200 250
Number of components
40
60
80
100Cumulative explained variance (%)
(c) Effective dimensionality
80% (n = 60)
90% (n = 95)
99% (n = 156)
−0.4 −0.2 0.0 0.2 0.4
Mean
0
50
100
150
200Number of dims
0.02 0.04 0.06 0.08
Std
0
20
40
60Number of dims
σ < 0.01
−0.6 −0.4 −0.2 0.0
Min
0
15
30
45
60Number of dims
0.0 0.2 0.4
Max
0
15
30
45
60Number of dims
−2 −1 0 1 2
Skewness
0
10
20
30
40Number of dims
|skew| = 2
0 2 4
Kurtosis
0
15
30
45Number of dims
Per-dimension statistic distributions (across 256 dims)(d)
Figure 4. Internal quality diagnostics of the 256-dimensional embeddings, computed over all 1,055,537
H3 res-7 cells.(a) Distribution of per-feature reconstructionR2 across the 2,288 input features; dashed line, median.
(b) Distribution of Pearson correlation coefficients across all 32,640 off-diagonal embedding-dimension pairs; dashed
line, median. (c) Cumulative PCA explained variance against number of components; dashed lines mark the 80%,
90% and 99% levels. (d) Distributions across the 256 embedding dimensions of six per-dimension summary statistics,
each computed over all cells: mean, standard deviation, minimum, maximum, skewness, and excess kurtosis. Red
dashed line, the 0.01 dead-dimension threshold (Section 4.4); orange lines,|skewness|= 2.
reconstructed values, are centered close to zero, indicating no systematic aggregate reconstruction
bias; the remaining error is concentrated in feature-specific tails rather than broad miscalibration.
5.1.2 Embedding space health and dimensionality
Beyond preserving the structural information contained in the input features, a useful embedding
should make effective use of its representational capacity. We therefore examined whether the
learned 256-dimensional space is well-conditioned and free of the degeneracies that commonly afflict
autoencoder bottlenecks.
17

Table 5. Variance structure of the input vs. the embedding.
Measure Input (2,288-d) Embedding (256-d)
PCA participation ratio (evenness of variance spread) 6.6 12.6
Levina–Bickel MLE (nonlinear degrees of freedom) 32.3 25.2
Variance in top-3 PCA components (coverage) 47.8% 35.7%
Unit norm by construction.Every embedding lies exactly on the unit hypersphere: the
L2-normalization layer (Section 4.1) enforces∥e∥ = 1by construction, and the measured norms
confirm this exactly (mean 1.0000, standard deviation 0.0000 across all 1,055,537 cells). A direct
and useful consequence is that cosine similarity between any two embeddings reduces to their dot
product, which makes similarity and nearest-neighbor operations inexpensive at national scale.
High effective rank.The distribution of correlation coefficients across the off-diagonal
embedding-dimension pairs is symmetric and tightly concentrated at zero (medianr = 0.000, with
99% of pairs below|r| = 0.47), and the greedy decorrelation test retains 251 of the 256 dimensions,
so only five are strongly linearly correlated with another: the bottleneck spans a broad effective
subspace rather than collapsing onto a few axes (seeFigure 4b), consistent with the intrinsic-
dimensionality analysis below. This is a linear redundancy diagnostic; because both the encoder and
the downstream models (Section 5.2) are nonlinear, even the few linearly-correlated dimensions
may still carry complementary information that nonlinear models can exploit.
Intrinsic dimensionality.We report the PCA participation ratio and the Levina–Bickel
MLE estimator (Section 4.4) for both the 2,288-d standardized input and the 256-d embedding,
computed on the full grid with the model’s own train-split standardization so the two are directly
comparable (Table 5).
First, the autoencoder decorrelates a highly redundant input. The 2,288 ring-augmented features
are dominated by a few directions (top-3 PCA components alone carry 47.8% of variance, since
each ring aggregate correlates strongly with its center feature), giving a low participation ratio of
6.6. The embedding nearly doubles the participation ratio (to 12.6) while its top-3 coverage drops
to 35.7%. These are two views of the same effect: variance is spread more evenly across directions
rather than piled into a few. Second, the embedding retains most of the input’s nonlinear degrees of
freedom (MLE 25.2 vs 32.3,≈78%) while both estimates sit well below the 256-d bottleneck, so
the representation is compact rather than capacity-bound. The full cumulative explained variance
distribution of the embedding is illustrated inFigure 4c. Rather than collapsing onto a few
dominant axes, the embedding distributes its variance across many components (60 principal
components are needed to reach 80% of the total variance, 95 for 90%, and 156 for 99%).
No dead or degenerate dimensions.No dimension is collapsed or unused and the model
uses its full capacity: as perFigure 4d, the per-dimension standard deviations are small but
tightly clustered (mean 0.023, range 0.018–0.081; above the 0.01 dead-dimension threshold). The
small scale is a structural effect of unit-normalization; the key point is that all 256 dimensions are
nonzero and comparable in magnitude, so the bottleneck is used broadly rather than collapsing onto
a few active dimensions. Additionally, the embedding dimension means are tightly concentrated
at zero; the small, bounded min/max ranges are consistent with the unit-norm (L2) embedding
geometry; and all dimensions are approximately symmetric (|skewness|< 2, orange lines) with only
mild, mostly positive excess kurtosis, indicating well-behaved, near-Gaussian marginals rather than
heavy-tailed or degenerate ones.
18

0.800 0.825 0.850 0.875 0.900 0.925 0.950 0.975 1.000
Cosine similarity
0
10
20
30
40
50Density
H3 k-ring disk
mean: own / permuted
k=1:  0.980 / 0.867   Δ=0.113
k=2:  0.979 / 0.873   Δ=0.106
k=3:  0.975 / 0.877   Δ=0.098
k=4:  0.972 / 0.880   Δ=0.092
k=5:  0.969 / 0.883   Δ=0.086
0.800 0.825 0.850 0.875 0.900 0.925 0.950 0.975 1.000
Cosine similarity
0
10
20
30Density
ZCTA
mean
permuted ZCTA   0.885
own ZCTA   0.965
Absolute cosine (raw embeddings)
−0.6 −0.4 −0.2 0.0 0.2 0.4 0.6 0.8 1.0
Cosine similarity
0
2
4
6Density
H3 k-ring disk
mean: own / permuted
k=1:  0.853 / 0.003   Δ=0.850
k=2:  0.841 / 0.002   Δ=0.839
k=3:  0.810 / 0.002   Δ=0.808
k=4:  0.782 / 0.003   Δ=0.779
k=5:  0.755 / 0.003   Δ=0.752
−0.6 −0.4 −0.2 0.0 0.2 0.4 0.6 0.8 1.0
Cosine similarity
0
1
2
3Density
ZCTA
mean
permuted ZCTA   0.005
own ZCTA   0.703
Mean-centered cosine (deviations from the national mean)
(a) (b)
(c) (d)
Figure 5. Neighborhood coherence of the embeddings as the density of the per-cell cosine similarity
between a cell’s embedding and the mean embedding of its neighborhood.Rows are the two framings:
(a, b) the PlacePulse embeddings, (c, d) the same embeddings minus the global mean vector. Columns are the two
neighborhood definitions: (a, c) the cumulative H3 k-ring disk fork = 1–5, focal cell excluded, over all 1,055,537 cells;
(b, d) the cell’s own ZCTA area-weighted mean, focal cell included, over the 1,001,075 cells assigned to one of 30,283
ZCTAs. Solid step curves are own-neighborhood similarities. Dotted curves are the permuted baseline, in which the
same cell is compared with a randomly reassigned neighborhood of the same type. In (a, c) color encodes the ring
radius, purple to green fork = 1to 5, and all five permuted baselines are orange. Dashed vertical lines mark the
means.
5.1.3 Spatial structure
To assess whether the embeddings preserve local geographic structure, we compare embedding
similarity across adjacent, co-located, and randomly selected cell pairs. We find that the embeddings
are geographically smooth: nearby and co-located cells exhibit substantially higher similarity
than random pairs. These results suggest that the learned representation captures the spatial
autocorrelation inherent in the input attributes, where nearby locations tend to have similar
demographic and business composition, consistent with Tobler’s first law of geography (Waters,
2017). The use of k-ring-aggregate inputs further strengthens this spatial structure by incorporating
information from each cell’s surrounding context.
Neighborhood coherence.We evaluate whether the embeddings preserve local spatial structure
by comparing each cell’s embedding with the mean embedding of its surrounding neighborhood,
and contrasting this with a spatially permuted baseline (Figure 5).
For H3 adjacency (thek = 1ring), the mean cosine similarity between a cell and its neighborhood
mean is 0.980 (p10 = 0.962, p90 = 0.994), versus 0.867 for a permuted-neighborhood baseline (the
same cell compared to a random cell’s neighborhood), a1.13× lift; coherence decays only gradually
with radius, to 0.969 atk = 5(Figure 5a). For ZCTAs, the mean cell-to-ZCTA-mean similarity
is 0.965 (p10 = 0 .939, p90 = 0 .986), versus 0.885 for a permuted-ZCTA baseline, a1.09× lift
19

(Figure 5b). All contrasts are overwhelmingly significant under a 99-permutation null (p≤ 0.01).
The high absolute similarities indicate that the embedding space is geographically smooth, supporting
the use of area-weighted mean aggregation for downstream enrichment (Section 5.2). However,
raw cosine similarities are partly compressed by a shared “national-average” direction in the L2-
normalized embeddings. After mean-centering, this common-direction floor is removed: the permuted
baselines collapse to approximately zero, while own-neighborhood similarity remains high at 0.853
for immediate H3 neighbors and 0.703 for ZCTAs (Figure 5candFigure 5d). This confirms
that the embeddings capture local spatial coherence beyond the global average structure. ZCTA
aggregation is therefore justified because it averages coherent local vectors rather than unrelated
embeddings, although it is not lossless. Quantifying this aggregation loss is left for future work.
Spatial autocorrelation (Moran’sI).In the 256-dimensional embedding space, spatial
autocorrelation is strong and highly significant. For adjacent unitsk = 1, all but one of the 256
embedding dimensions have Moran’sI > 0.50(the weakest is 0.495 and the mean is 0.70) with
permutation p < 0.005against the null expectation E[I]≈ 0. Thus, spatial structure is present
across the embedding coordinates rather than being confined to a small subset of dimensions. We
next examined the same structure after rotating the embedding with PCA. The dominant principal
component, which explains 26% of the variance, is especially spatially autocorrelated, with Moran’s
I = 0.93at k = 1, showing that spatial organization is distributed throughout the representation.
Autocorrelation is not uniform across all PCA directions: some lower-variance components show
weaker spatial autocorrelation, consistent with these components capturing finer-grained, more
localized, or more specialized variation after broad-scale gradients have been accounted for. The
correlogram over ring distancesk = 1–5 shows gradual monotonic decay rather than a sharp drop
(Figure 6a–b). For PC1, Moran’sIdeclines from 0.93 to 0.83, while the mean across embedding
dimensions declines from 0.70 to 0.50. Autocorrelation therefore remains high beyond the two-ring
radius of the model’s own inputs, suggesting that the learned representation reflects broad-scale
spatial organization rather than merely the local ring-aggregate features fed to the encoder.
Local hotspot structure (Getis–OrdG∗ i).As a local companion to the global Moran’sI,
the Getis–Ord G∗ i hotspot analysis confirms pronounced local clustering: the combined statistic
ranges from−18.3to+24 .5, and 55.6% of the cells fall in statistically significant clusters (two-
sided p < 0.05). This local view (seeFigure 6c) reinforces the global autocorrelation result: the
embedding space organizes into coherent regional structures rather than being distributed at random.
Note that because embedding dimensions have arbitrary orientation, the sign of the aggregate is not
semantically directional; the statistic is used here as a spatial-clustering diagnostic, not a labeled
hot/cold map.
Cluster structure.As seen inFigure 7, K-means partitions of the embedding space are
interpretable rather than arbitrary. Atk = 10the partition orders locations by settlement density,
from urban core suburbs to sparse rural land, while also capturing patterns beyond differences in
density alone (seeFigure 7a).Figure 7billustrates how finer partitions mostly refine this structure
rather than reorganizing, which indicates substantial multiscale consistency despite K-means not
being a hierarchical algorithm. In particular, a typicalk = 100cluster draws a median of 70.8%
of its cells from a singlek = 10parent cluster, and a typical k = 50cluster draws a median of
68.4% from its k = 10parent, both well above the 18.5% chance baseline.Table 6shows how
within-cluster inertia declines gradually with increasingk, from 102,239 to 89,946 to 84,510 for
k = 10→ 50→ 100, only a 17% reduction despite a tenfold increase in cluster count. This pattern
is consistent with high neighbor coherence (Section 5.1.3) and modest intrinsic dimensionality
(Section 5.1.2). The partitions also avoid a dominant mode: the largest cluster contains 18.5% of
cells atk= 10and only 2.2% atk= 100, while cluster-size entropy reaches 94–98% of the value a
perfectly even split would give. Fine-grained niche groups still emerge at higherk, with the smallest
20

1 2 3 4 5
H3 ring distance k
0.0
0.2
0.4
0.6
0.8
1.0Moran's I
Global: over the 256 raw dimensions
k-ring aggregate
inputs (k ≤ 2)
E[I] ≈ 0 under the permutation null
1 2 3 4 5
H3 ring distance k
Global: over the 256 principal components
k-ring aggregate
inputs (k ≤ 2)
 PC1 (26% of variance)
 −5
−4
−3
−2
−1
log10 variance explained
Local: combined Getis–Ord G * i  (clustering-strength diagnostic)
(a) (b)
(c)
Figure 6. Spatial autocorrelation of the embeddings across all 1,055,537 H3 resolution-7 cells.(a)
Moran’s I for the 256 original embedding dimensions, using row-standardized H3 ring-neighborhood weights for
k = 1–5. Boxes show the median and interquartile range across dimensions, with individual dimensions shown as
jittered points. (b) The same analysis for the 256 principal components; points are colored bylog10 variance explained,
and the star marks PC1. In both panels, the shaded band marksk≤ 2, the radius of the encoder’s ring-aggregate
inputs, and the horizontal line marksE[I]≈ 0. (c) Combined Getis–Ord G∗ i, as defined inSection 4.4, over
uniform-weight H3 (k = 3) ring neighborhoods. Values are binned into 11 classes, with teal negative and red positive.
The inset gives class edges, cell shares, and dashed±1.96reference lines for a two-sidedp = 0.05threshold. Because
embedding orientation is arbitrary, the sign is not directional.
21

Table 6. Mini-batch K-means cluster structure over the 256-dimensional embeddings.H is the Shannon
entropy of the cluster-size shares, its maximumlog2k attained at equal sizes;2H is the equivalent number of equally-
sized clusters; inertia is the within-cluster sum of squares.
kLargest cluster Smallest cluster EntropyH H/ max Effective clusters Inertia
10 195,375 (18.5%) 36,385 (3.45%) 3.14 (max 3.32) 94.5% 8.8 102,239
50 39,340 (3.7%) 4,939 (0.47%) 5.50 (max 5.64) 97.5% 45.4 89,946
100 22,963 (2.2%) 696 (0.07%) 6.48 (max 6.64) 97.5% 89.1 84,510
Table 7. Downstream performance at native H3 res-7 resolution (PlacePulse vs. the target-blind,
dimensionality-matched baseline).The average per-foldR2 of the tasks in each category is reported; seeTable B.1
for the uncertainty of each individual task.
Category What it covers # PlacePulseR 2 BaselineR 2
Public Health Adult health-risk prevalence: diabetes, obesity,
high blood pressure, cancer, high cholesterol,
stroke.
6 0.707 0.738
Points of Interest(log
space)
POI counts by type: total plus retail, food
& drink, healthcare, offices, finance, leisure,
education, public services, tourism, transport.
11 0.772 0.724
Population Activity Human-footprint proxies: human activity index,
nighttime lights (raw VIIRS radiance), cell-
tower density.
3 0.801 0.788
k= 100cluster containing approximately 700 cells. Refer toAppendix Afor more details.
5.2 Downstream predictive utility
The downstream evaluation examines the utility of the learned embeddings in applied predictive
tasks. We assess whether the representations capture information that is useful for modeling
real-world outcomes across different domains and spatial resolutions. This analysis provides an
external measure of how well the embeddings generalize beyond their training objectives and support
practical geospatial modeling workflows.
5.2.1 Native resolution (H3 res-7)
To our knowledge, no comparable public embedding product is natively available at H3 resolution 7,
so the native-resolution comparison is limited to PlacePulse and the baseline representation defined
inSection 4.4.Table 7summarizes performance across the 20 native-resolution targets listed in
Table 2.Figure 8andTable B.1give the full per-target results.
Public Health is the category most closely aligned with the training distribution. As noted
inSection 3.4, these targets are AGS-modeled disease-prevalence rates from the same product
family as the mortality and life-expectancy variables used during training, although they are not
themselves training inputs. PlacePulse trails the baseline modestly in this category, with an average
R2 of 0.707 versus 0.738. This suggests that the baseline retains an advantage on health-adjacent
variables, whereas PlacePulse allocates its fixed-dimensional capacity across a broader set of place
attributes.
PlacePulse performs better in the two categories with no direct relationship to the training
inputs. For Points of Interest, PlacePulse outperforms the baseline by a substantial margin:R2
is 0.772 versus 0.724. For Population Activity, PlacePulse also leads, though by a smaller margin,
22

K-means partitions and cluster sizes(a)
(b)
Figure 7. K-means cluster structure over all H3 res-7 cells.Color identifies the cluster and is shared across
all plots: clusters close in embedding space take close colors, and atk = 50and 100 each cluster takes the hue of the
k = 10cluster holding most of its cells and varies only in lightness. (a) Partitions atk = 10(top), 50 (middle) and 100
(bottom). Left to right: the conterminous United States, a New York metro close-up, a Dallas–Fort Worth close-up,
and the cluster sizes sorted largest to smallest on a log axis, annotated with the largest and smallest share. (b) Cell
flows from the coarse to the fine partition, fork = 10→ 50,10 → 100and50 → 100(left to right). Ribbon width is
proportional to the number of cells. Only the largest ribbons carrying 95% of cells are drawn, and each diagram states
how many flows it omits.
23

Figure 8. Downstream predictive performance at native H3 res-7 resolution.PlacePulse (256-d) vs. the
target-blind, dimensionality-matched baseline, per target within each of the three native-resolution categories, under
5-fold spatially-blocked cross-validation. Each row is one target: the two dots are that target’s per-fold meanR2 under
the two representations, the connector takes the color of the leading one, and the shaded band spans±1standard
deviation across the 5 held-out folds.
with R2 of 0.801 versus 0.788. The strongest individual result is for the Human Activity Index,
where PlacePulse achievesR2 = 0.930. These results suggest that PlacePulse learns a more general
representation of place structure, retaining functional and activity-related information beyond what
is captured by a compact target-blind subset of the original inputs.
5.2.2 External baseline’s resolution (ZCTA)
At ZCTA resolution, PlacePulse embeddings are evaluated after aggregation from H3 resolution 7
to ZCTAs using an area-weighted mean, as described inSection 4.4. They are compared with
Google’s Population Dynamics Foundation Model (PDFM; Agarwal et al., 2024), which is published
natively at ZCTA resolution. This comparison is conservative for PlacePulse, because PDFM is
evaluated at the native resolution it was trained on, whereas PlacePulse is evaluated at ZCTA
through an area-weighted mean of embeddings learned for H3 cells. Targets span seven categories,
summarized inTable 8and fully described inFigure 9andTable B.2.
On average, PlacePulse achieves a higherR2 than PDFM in the Public Health (0.610 versus
0.573) and Economic status (0.633 versus 0.605) categories, while Population Activity is close to
parity (0.863 versus 0.855). Part of these gains may stem from overlap between model inputs and
24

Table 8. Downstream performance at ZCTA resolution (PlacePulse vs. PDFM).The average per-foldR2
of the tasks in each category is reported; seeTable B.2for the uncertainty of each individual task.
Category What it covers # PlacePulseR 2 PDFMR 2
Public Health Health indicators: chronic-disease prevalence,
health behaviors, self-rated physical and mental
health, preventive-care access.
21 0.610 0.573
Economic status Economic standing and hardship: median family
and household income, median home value,
poverty rate, energy burden and cost, low-food-
access population share.
7 0.633 0.605
Population Activity
(mixed scales)
Population, population density, nighttime lights;
human activity index and cell-tower density.
5 0.863 0.855
Physical Geography Natural land signals: mean elevation and tree-
canopy share.
2 0.628 0.744
Points of Interest(log
space)
POI counts by type, the same 11 classes as at
H3.
11 0.784 0.906
Social capital Cross-status economic connectedness and
friendship clustering.
2 0.715 0.713
Entrepreneurship(log
space)
Startup formation rate and regional
entrepreneurship cohort potential.
2 0.765 0.822
evaluation targets, as the CDC PLACES and economic targets are partly derived from census and
ACS covariates that also inform the AGS inputs. At the target level, PlacePulse exceeds PDFM
on three of the five Population Activity outcomes: Human Activity Index (0.935 versus 0.834),
nighttime lights (0.955 versus 0.903), and population density (0.933 versus 0.865). PDFM leads on
raw population count (0.723 versus 0.825) and cell-tower density (0.768 versus 0.850), bringing the
category-level average close to a tie. Social capital is effectively tied across the two representations,
while PDFM achieves higherR2 on Entrepreneurship (0.822 versus 0.765).
PDFM also achieves higher R2 on Points of Interest (0.906 versus 0.784). This pattern is
consistent with a closer match between PDFM’s inputs and these targets. PDFM’s inputs include
place counts from Google Maps (Agarwal et al., 2024), which, like the Overture targets, are derived
from listings of places. PlacePulse includes AGS establishment counts, which are derived from
business records and classified by industry (NAICS) rather than by place category. Physical
Geography also favors PDFM, especially for elevation, where it achievesR2 = 0 .821compared
with 0.555 for PlacePulse. TheR2 spread across held-out folds is large in both cases, suggesting
that ZCTA-level physical-geography prediction is difficult, mostly for PlacePulse, where little input
contains information relative to this category.
The results suggest that the two embeddings behave as distinct model families rather than
interchangeable representations. PlacePulse, which is trained to encode structural relationships
among place attributes, performs slightly better on Public Health, Economic status, and Population
Activity. These categories depend strongly on persistent socioeconomic, demographic, and insti-
tutional structure, and the gains are largest for health and economic outcomes. PDFM performs
better on Physical Geography, Points of Interest, and Entrepreneurship, with the largest advantage
for POI counts. This pattern is consistent with PDFM capturing more directly observable or
dynamic signals of place intensity, land use, and economic activity, whereas PlacePulse captures
more latent structural variation in the social and health environment. These differences may also
partly reflect the input data of each model, which in some cases overlap with the evaluation targets,
either directly or through shared covariates (e.g., census-derived demographics for PlacePulse on
25

Figure 9. Downstream predictive performance at ZCTA resolution.PlacePulse embeddings, area-weighted
from H3 resolution 7 to ZCTAs, are compared with Google PDFM embeddings at native ZCTA resolution. The
50 targets are grouped into the seven ZCTA-level categories and split across two columns, under 5-fold spatially
blocked cross-validation. Each row is one target: the two dots are that target’s per-fold meanR2 under the two
representations, the connector takes the color of the leading one, and the shaded band spans±1standard deviation
across the 5 held-out folds.
health and economic targets, or map-derived POIs for PDFM and AGS establishment counts for
PlacePulse on POI counts). Thus, the comparison should not be read simply as one embedding
dominating the other; rather, the two model families appear to encode different but complementary
aspects of place.
5.2.3 Other target resolutions (voting precinct, census tract)
For targets observed at voting-precinct and census-tract resolutions, neither representation is
evaluated on its native spatial support. Both PlacePulse and PDFM are transferred to the target
units using the area-weighting procedure described inSection 4.4. The four targets span three
categories, summarized inTable 9.
26

Table 9. Downstream performance at non-native target resolutions: voting precincts and census tracts.
Both representations are area-weighted from their original resolution (H3 res-7 for PlacePulse, ZCTA for PDFM)
to the target resolution. The average per-foldR2 of the tasks in each category is reported; seeTable B.3for the
uncertainty of each individual task.
Category What it covers # PlacePulseR 2 PDFMR 2
Elections(precinct)2024 U.S. presidential result by voting precinct. 1 0.737 0.709
Economic Mobility
(tract)
Opportunity Atlas intergenerational mobility for
children raised at the 25th income percentile.
1 0.546 0.508
Social Vulnerability and
Resilience(tract)
Social-vulnerability and community-resilience
scores.
2 0.435 0.302
Figure 10. Downstream predictive performance at non-native target resolutions.PlacePulse and Google
PDFM are both area-weighted from their native spatial supports to voting precincts or census tracts, under 5-fold
spatially blocked cross-validation. Each row is one target: the two dots are that target’s per-fold meanR2 under
the two representations, the connector takes the color of the leading one, and the shaded band spans±1standard
deviation across the 5 held-out folds.
PlacePulse outperforms PDFM in every category in the non-native-resolution evaluation. For the
2024 presidential election result at the precinct level, PlacePulse achievesR2 = 0.737, compared with
0.709 for PDFM, consistent with the embedding capturing structural sociodemographic variation
strongly associated with spatial patterns in voting behavior. For intergenerational economic mobility,
PlacePulse also leads, withR2 = 0.546compared with 0.508 for PDFM. Social Vulnerability and
Resilience shows the largest differences: PlacePulse leads on both social vulnerability (R2 = 0.384
versus 0.269) and community resilience (R2 = 0.486versus 0.335), while both models fail to estimate
such targets correctly. Both indices are built from census socioeconomic indicators that overlap
with AGS inputs, which may contribute to the PlacePulse advantage.
In this setting, both representations must be transferred from their original spatial supports
to the target units. PlacePulse leads across all three categories and nearly all evaluation views,
with the main exception being the shared failure of both representations to generalize on Social
Vulnerability and Resilience. However, because each representation reaches the target units through
a different transfer, these results are best read as a practical comparison: for analyses carried out at
tract or precinct level, the pattern suggests that PlacePulse captures structural place information
that is more stable across such spatial scales and target domains, particularly for outcomes shaped
by persistent socioeconomic, demographic, and institutional context.
27

6 Discussion
6.1 A compact, faithful re-encoding of structural place data
The internal evaluation shows that a purely structural autoencoder yields a faithful and well-
conditioned representation of place. The model reconstructs the 2,288 standardized inputs with an
average R2 of 0.853 (median 0.887), and no feature is reconstructed worse than its own mean, so the
256-dimensional bottleneck preserves the bulk of the structural signal rather than discarding it. The
resulting space is also well-behaved: it is unit-norm by construction, has no dead dimensions, and
retains 251 of 256 mutually decorrelated axes. Its effective dimensionality is nonetheless modest:
the participation ratio rises from 6.6 in the input to 12.6 in the embedding while the nonlinear
estimate falls from 32.3 to 25.2, indicating that the encoder redistributes a highly redundant input
across a broader set of directions instead of piling variance onto a few. The embedding is therefore a
compact, near-lossless re-encoding of the structural feature set, which is the precondition for using
it as a general-purpose feature.
The representation additionally recovers geographic organization that it was never explicitly
trained to produce. Global Moran’sI reaches 0.93 on the dominant principal component and exceeds
0.50 on every dimension but one, and a Getis–OrdG∗ i analysis places 55.6% of cells in significant
clusters. Crucially, this autocorrelation persists beyond the two-ring radius of the model’s own
inputs, so the smoothness reflects genuine broad-scale spatial organization inherited from the data
(Tobler’s first law) rather than an artefact of the ring-aggregate features. K-means partitions of the
space are correspondingly interpretable and balanced: they order locations along a settlement-density
gradient, reach 94–98% of maximum size entropy, and refine rather than reorganize ask grows.
Settlement density is one recognizable axis of that partition, but it is not the only one: income
separates suburban types that sit at comparable densities, so the embedding is not reducible to a
density index.
6.2 Structural and dynamic representations encode complementary aspects of
place
These properties speak to the paper’s central claim: that the structural composition of a place
is a useful, self-contained modality for a geospatial foundation model. Unlike the dynamic-signal
and imagery models that dominate the field (Section 2), PlacePulse requires no behavioral traces
(which are sparse, privacy-sensitive, and unevenly available) and no imagery, yet it encodes who
lives and works in a place together with its risk profile, information those modalities capture only
indirectly. The downstream comparison with PDFM supports reading the two as complementary
rather than competing. At ZCTA resolution PlacePulse leads on Public Health (0.610 versus 0.573)
and Economic status (0.633 versus 0.605), is at parity on Population Activity (0.863 versus 0.855) and
Social capital, and trails on Points of Interest (0.784 versus 0.906), Physical Geography (0.628 versus
0.744), and Entrepreneurship (0.765 versus 0.822). The split is systematic: PlacePulse is stronger
where outcomes depend on persistent socioeconomic, demographic, and institutional structure, and
weaker where they depend on directly observable land use, physical form, or point-level activity
intensity.
The spatial support of each comparison matters for its interpretation. At ZCTA, PlacePulse is
evaluated after area-weighted aggregation from H3 resolution 7, whereas PDFM is scored on its
native spatial support. At precinct and tract level, where both representations are transferred away
from their native supports, PlacePulse leads in all three categories: 2024 presidential vote share at
precinct level (0.737 versus 0.709), intergenerational economic mobility at tract level (0.546 versus
0.508), and social-vulnerability and resilience scores (0.435 versus 0.302). These results should
28

be interpreted with the transfer in mind: PDFM reaches the target units from coarser ZCTAs
that largely nest them, whereas PlacePulse reaches them from finer H3 cells that either cut across
them or contain several of them within a single cell (Section 4.4), so the comparison reflects each
representation together with its native support. The absolute performance on social vulnerability and
resilience shows that both representations leave substantial variance unexplained. Testing whether
a concatenated structural-plus-dynamic representation outperforms either alone is the natural next
experiment, and we leave it to future work. A second extension is to evaluate targets at coarser units,
such as counties. Counties are larger than both native supports, so both representations would be
aggregated rather than disaggregated, removing the boundary-misalignment and shared-embedding
effects described above.
6.3 Implications for practice and responsible use
For practitioners, the appeal is a single reusable national representation that replaces the laborious,
per-task feature engineering described inSection 1. Rather than assembling, cleaning, and joining
hundreds of variables for each new study, an analyst attaches a 256-dimensional vector to each H3
cell. Because the embeddings lie on the unit sphere, cosine similarity reduces to a dot product, so
retrieval tasks such as twin-area discovery run at national scale as a single matrix operation. The
neighborhood-coherence result also gives a practical licence for the aggregation step most applied
work requires: area-weighted means over ZCTAs average coherent local vectors rather than unrelated
ones, which supports the use of aggregated embeddings for ZCTA-level analyses such as those in
Section 5.2.2.
Because the embeddings are learned by reconstructing sociodemographic inputs, they encode
attributes, such as race and ethnicity, income, and a diversity index; and can act as proxies for
them even when those attributes are never used explicitly downstream. This is a general property
of representations learned from demographic data rather than a characteristic of this model in
particular. The representation describes areas rather than individuals, although aggregation does not
by itself remove the property. We intend the embeddings for spatial analysis, not for individual-level
eligibility decisions in regulated domains, and those who deploy the embeddings are responsible
for complying with applicable law, including any disparate-impact testing required in high-stakes
settings, under CARTO’s licensing terms. Treating the representation as attribute-free because no
protected attribute appears in the model interface would be a serious misreading of what it contains.
6.4 Limitations
Five limitations bound the scope of these claims. First, the inputs are proprietary, modelled, single-
vintageestimates: theAGSfeaturesarecommercialestimatesfor2025ratherthandirectobservations,
so their own estimation error propagates into the embeddings and into every downstream result,
and their licence limits full reproducibility. We do not bound that input uncertainty here, and
cross-validating core AGS variables against an independent source with published margins of error,
such as the American Community Survey, remains outstanding. Second, coverage is limited to the
United States on a single national grid, so transferability to other countries and data regimes is
untested.
Third, the scope of the evaluation is transductive: we produce embeddings for a fixed, fully
observed grid and evaluate them as features over that grid. The encoder can be applied to new
inputs, but we do not validate its behaviour on unseen cells, vintages, or geographies, and we make
no claim of inductive generalization. Fourth, we report a single configuration selected from an
exploratory sweep. This follows from the scope set inSection 4.1, which treats the encoder as a
29

conventional means to the representation rather than as a contribution in itself. The sensitivity
of the results to architecture and hyperparameters therefore remains only partially characterized.
Fifth, some downstream targets share covariates with the inputs of PlacePulse, and in some cases
PDFM (Table 2). Several were included deliberately, to check whether the embeddings preserve the
socio-economic and health gradients present in the inputs (Section 3.4), but cross-model differences
on these targets may partly reflect input-target overlap rather than representation quality alone; a
controlled comparison excluding the overlapping inputs is left for future work.
7 Conclusions
We introduced PlacePulse, a structural geospatial foundation model that compresses 572 AGS at-
tributes (expanded to 2,288 inputs through H3 ring aggregates) into 256-dimensional, L2-normalized
embeddings for 1,055,537 H3 resolution-7 cells in the United States. The model uses no behavioral
traces, imagery, or other dynamic inputs. Intrinsically, the resulting embeddings provide a compact,
well-conditioned, spatially coherent, and nearly lossless representation of the static composition
of place. Extrinsically, they serve as a competitive general-purpose feature representation across
74 downstream regression targets. At the model’s native resolution, PlacePulse outperforms a
dimensionality-matched feature-selection baseline on targets unrelated to the training inputs. After
transfer to non-native spatial units, it matches or exceeds PDFM on health, economic, election,
mobility, and social-vulnerability outcomes.
The main contribution of this work is evidential rather than architectural. Current geospatial
foundation models are typically built around behavioral traces, mobility signals, or satellite imagery,
while structural attributes are often treated as auxiliary covariates. Our results show that structural
composition alone can support a representation that is competitive with a dynamic-signal model
on comparable spatial prediction tasks. Together with a national-scale evaluation protocol that
separates intrinsic representation quality from downstream predictive utility, these findings position
structural embeddings as a distinct and complementary modality for geospatial foundation modeling,
rather than merely as a substitute when behavioral or imagery data are unavailable.
Several directions follow from these results. The most immediate is multimodal fusion. Because
structural and dynamic representations appear to capture complementary aspects of place, future
work should directly test combinations of PlacePulse with PDFM-style, mobility-based, or Earth-
observation embeddings; the category-level results reported here suggest where each modality is likely
to contribute most. A related direction is to characterize the contribution of each input family to
the representation. Ablation studies that retrain the encoder with individual AGS products removed
or used in isolation would clarify which thematic domains drive performance on each category of
downstream task, help quantify the extent to which overlap between input covariates and evaluation
targets contributes to that performance, and could guide the design of leaner or domain-specific
variants of the model. Another direction is temporal representation learning. Extending PlacePulse
to multiple data vintages would make it possible to learn temporally indexed embeddings of the same
cells, separating persistent structural context from trajectories of change and enabling applications
such as neighborhood change detection, early-warning indicators, and longitudinal comparison of
places. More explicitly, temporal encoders could also model sequences of structural states rather
than treating each vintage independently. Applying the approach in other countries would further
test its portability across national data regimes.
On the modeling side, set-based or transformer-based encoders that omit masked inputs directly,
rather than using the replace-in-place scheme adopted here, may improve both efficiency and
representation quality. A further direction concerns the geometry of the embedding space. Although
30

PlacePulse uses nearly all 256 dimensions, variance remains concentrated in a smaller number
of directions, so the embeddings occupy only a narrow region of the unit sphere. Future work
could test uniformity- or entropy-based regularizers, such as the uniformity objective of Wang
and Isola (2020) or the Kozachenko–Leonenko entropy regularizer of Sablayrolles et al. (2019), to
spread representations while preserving local spatial structure. However, greater uniformity is not
necessarily preferable: the current density structure supports interpretable clustering, and some
concentration likely reflects real structure in the input data. Whether a more uniform embedding
improves retrieval and downstream prediction, or instead removes meaningful variation, remains an
open empirical question.
Finally, the unit-norm embedding geometry motivates dedicated retrieval applications, such as
twin-area discovery and market-whitespace analysis, as well as systematic evaluation of methods
for aggregating cell-level embeddings to policy-relevant spatial units and quantifying how much
fine-scale structure is lost in that process.
Acknowledgements
We thank Applied Geographic Solutions for granting access to the data products described in
Section 3, and for reviewing our description of those products. We thank Esteban Moro and
Hamish Gibbs (Network Science Institute, Northeastern University) for insightful discussions on this
work. We also thank Alex Singleton (University of Liverpool) for suggesting downstream evaluation
targets, and Bruno Sánchez-Andrade (LGND) for discussions on the modeling approach.
We further thank Google Research for the public release of the Population Dynamics Foundation
Model embeddings and benchmark targets, and the providers of the open data used as downstream
evaluation targets (Section 3.4): the Overture Maps Foundation; OpenCellID; the Earth Observa-
tion Group at the Payne Institute for Public Policy, Colorado School of Mines; the U.S. Department
of Agriculture Economic Research Service; the National Renewable Energy Laboratory and the U.S.
Department of Energy; The New York Times; Opportunity Insights (Opportunity Atlas and Social
Capital Atlas); the Federal Emergency Management Agency; and the Startup Cartography Project.
Declaration of competing interest
The authors declare the following financial interests and personal relationships which may be
considered as potential competing interests. All authors are employees of CARTO, which developed
the PlacePulse embeddings reported in this paper and holds a commercial interest in their distribution
as a data product. The input features are licensed from Applied Geographic Solutions, a commercial
data provider with which CARTO has a commercial partnership for the distribution of Applied
Geographic Solutions data products. Applied Geographic Solutions reviewed the description of its
own data products inSection 3and had no role in the study design, the evaluation protocol, the
analysis or interpretation of the results, or the decision to submit this article for publication.
Funding
This work was funded by CARTO as part of its internal research programme. We acknowledge the
EuroHPC Joint Undertaking for awarding two projects (EHPC-AIF-2025PG01-473 and EHPC-AIF-
2026PG01-587) access to the EuroHPC supercomputer MareNostrum 5, hosted by the Barcelona
Supercomputing Center (Spain), through the EuroHPC AI Factory Playground Access mode.
31

Apart from this computing allocation, the work received no specific grant from external funding
agencies. CARTO was involved in the study design, the analysis and interpretation of the results, the
writing of the article, and the decision to submit it for publication; the EuroHPC Joint Undertaking
had no role in any of these.
Data availability
The input features are licensed from Applied Geographic Solutions and cannot be redistributed by
the authors; access requires a licence agreement with the provider. The trained embeddings are a
CARTO data product and are not publicly redistributable, and the code that implements the model
is not publicly available. The downstream evaluation targets are drawn from the public sources
listed inTable 2, with the exception of the six AGS Health targets, and each remains available
from its original provider under that provider’s terms. The Population Dynamics Foundation Model
embeddings used for comparison are distributed by Google Research under their own access terms.
Declaration of generative AI and AI-assisted technologies in the
manuscript preparation process
During the preparation of this work the authors used ChatGPT (OpenAI) and Claude (Anthropic)
in order to enhance the readability and language of the manuscript. After using these tools, the
authors reviewed and edited the content as needed and take full responsibility for the content of the
published article.
Author Contributions (CRediT)
Lucía García-Duarte:Conceptualization, Data curation, Formal analysis, Investigation, Method-
ology, Software, Validation, Visualization, Writing - original draft, Writing - review & editing.
Miguel Álvarez:Conceptualization, Funding acquisition, Project administration, Supervision,
Writing - original draft, Writing - review & editing.Diego Vicente:Conceptualization, Data
curation, Formal analysis, Writing - review & editing.Javier Pérez Trufero:Conceptualization,
Supervision.Javier de la Torre:Conceptualization, Funding acquisition, Supervision.
32

A Supplemental clustering structure evaluation
Section 5.1.3reports that finer K-means partitions refine coarser ones rather than reorganizing
them. This appendix presents the evidence behind that statement, for the three transitions in
granularityk= 10→50,k= 10→100, andk= 50→100.
The nesting matrices are strongly block-diagonal (Figure A.1a): most fine clusters draw the
majority of their cells from a single coarse cluster, and mixing across parents is limited in all three
scenarios.
Purity quantifies the pattern: the empirical cumulative distribution inFigure A.1bshows
fine-cluster purity, defined as the largest share of a fine cluster’s cells coming from a single coarse
cluster. Higher purity means that a fine cluster is mostly nested within one coarse parent, rather
than being assembled from multiple coarse clusters. Median purity is 68.4% fork = 10→ 50, 70.8%
for k = 10→ 100, and 54.6% fork = 50→ 100, indicating that a typical fine cluster draws the
majority of its cells from one parent partition. The chance baseline is the cell share of the largest
cluster in the source partition, 18.5% fork = 10and 3.7% for k = 50, so the observed medians
exceed chance by3.7×,3 .8×, and14.7×, showing that the nesting pattern is far stronger than would
be expected from random overlap. Because purity depends on the relative granularities of the two
partitions, the three medians should be interpreted against their own baselines rather than compared
directly. In particular,k = 50→ 100has the lowest absolute median purity but is furthest above
chance, indicating that even the finest transition retains substantial hierarchical structure. Overall,
the purity distributions confirm that finer K-means solutions are not arbitrary reorganizations
of the data; they largely preserve the structure of coarser partitions while introducing additional
subdivision.
Figure A.1cshows how larger coarse clusters tend to produce more fine-cluster descendants.
The relationship between coarse-cluster size and number of children is positive for all transitions,
with Pearson correlations of 0.85 fork = 10→ 50, 0.88 fork = 10→ 100, and 0.49 fork = 50→ 100.
This indicates that larger coarse clusters are generally subdivided into more fine clusters, while
smaller coarse clusters tend to remain represented by fewer descendants. The weaker correlation for
k = 50→ 100suggests that, at finer granularities, splitting is less determined by size alone and may
reflect additional internal heterogeneity within the coarse clusters. Overall, the pattern supports
the interpretation that increasingk primarily refines existing clusters, with larger parent clusters
receiving more subdivisions rather than the partition being globally reorganized.
Taken together, the three views show that K-means solutions at increasingk are not arbitrary
reorganizations of the data. They preserve the structure of coarser partitions and add subdivision,
even though K-means imposes no hierarchical constraint.
B Supplemental downstream predictive evaluation
Section 5.2reports downstream performance aggregated by category. This appendix gives the
result for every individual target, so a reader can see which targets drive each category mean.
Table B.1covers the 20 targets at the model’s native H3 resolution 7,Table B.2the 50 targets at
ZCTA resolution, andTable B.3the 4 targets at voting-precinct and census-tract resolution.
Every value is the per-foldR2, the mean± standard deviation of R2 computed within each
held-out fold of the 5-fold spatially-blocked cross-validation, where every state is held out entirely
in one fold. This is the same viewSection 5.2reports at category level. Both representations are
always scored on the same GEOIDs, the intersection of the units each one covers, so neither is ed
with an easier test set.
33

0 2 4 6 8
k = 10 cluster (by size)
0
10
20
30
40 k = 50 cluster
k = 10 →  50
0 2 4 6 8
k = 10 cluster (by size)
0
20
40
60
80 k = 100 cluster
k = 10 →  100
0 10 20 30 40
k = 50 cluster (by size)
0
20
40
60
80 k = 100 cluster
k = 50 →  100
0.0
0.2
0.4
0.6
0.8
1.0
share of fine cluster's cells
Nesting matrices: share of each fine cluster's cells by coarse cluster
0 20 40 60 80 100
Largest share of a fine cluster from one coarse cluster (%)
0
20
40
60
80
100Fine clusters at or below (%)
Purity distribution: how cleanly each fine cluster sits inside one coarse cluster
3.7%
18.5%
k=10 → 50  (median 68.4%)
k=10 → 100  (median 70.8%)
k=50 → 100  (median 54.6%)
chance for k=50
chance for k=10
104 105
Cells in the coarse cluster
2.5
5.0
7.5
10.0
12.5
15.0
17.5Number of children
Splitting behaviour: number of fine clusters per coarse cluster against its size
k=10 → 50  (r = 0.85, n = 10)
k=10 → 100  (r = 0.88, n = 10)
k=50 → 100  (r = 0.49, n = 50)
(a)
(b) (c)
Figure A.1. Finer K-means partitions mostly refine coarser partitions rather than reorganizing them.
We compare three transitions in clustering granularity:k = 10→ 50, k = 10→ 100, andk = 50→ 100. (a) Nesting
matrices. Rows represent fine clusters and columns represent coarse clusters, ordered by coarse-cluster size. Shading
indicates the share of each fine cluster’s cells that fall within each coarse cluster. Rows are sorted by their dominant
coarse “parent”, and dashed lines separate the resulting parent blocks. (b) Empirical cumulative distribution of
fine-cluster purity, defined as the largest share of a fine cluster’s cells coming from a single coarse cluster. Dashed
vertical lines mark the median of each transition, and dotted vertical lines mark the chance baseline, the cell share of
the largest cluster in the source partition. (c) Number of fine-cluster descendants against coarse-cluster size, on a
logarithmic x-axis. Marker shape and color identify the transition, and the legend gives the Pearson correlationr and
the number of coarse clustersn.
Table B.1. Per-target downstream performance at native H3 resolution 7.PlacePulse (256-d) against the
target-blind, dimensionality-matched baseline, under 5-fold spatially-blocked cross-validation with every state held out
entirely in one fold. Points of Interest targets are scored in log space. In every row the higher per-fold mean is set in
bold; the one row where the two means agree to three decimals is left unmarked.
Category Source Target Description PlacePulseR 2 BaselineR 2
Public
Health
Applied Geographic
Solutions
High blood
pressure (risk)
Adults with high
blood pressure
0.729±0.0200.759±0.020
Cancer (risk) Adults with cancer,
excluding skin cancer
0.712±0.0230.741±0.021
High cholesterol
(risk)
Adults with high
cholesterol
0.767±0.0150.791±0.012
Diabetes (risk) Adults with
diagnosed diabetes
0.670±0.0360.710±0.028
Obesity (risk) Adults classified
obese
0.705±0.0180.733±0.006
34

Category Source Target Description PlacePulseR 2 BaselineR 2
Stroke (risk) Adults who have had
a stroke
0.661±0.0180.695±0.015
Points of
Interest
Overture Maps POI Total All POI categories
combined
0.820±0.016 0.790±0.017
POI Retail Shops and retail
outlets
0.803±0.018 0.757±0.019
POI Healthcare Clinics, hospitals,
pharmacies
0.823±0.017 0.760±0.018
POI Offices Office and
professional-services
premises
0.833±0.015 0.776±0.017
POI Food and
drink
Restaurants, cafes,
bars
0.797±0.023 0.737±0.025
POI Financial Banks, ATMs,
financial services
0.790±0.022 0.716±0.023
POI Leisure Sports, recreation,
entertainment
0.779±0.025 0.740±0.025
POI Education Schools, universities,
training
0.762±0.028 0.716±0.027
POI Public
services
Government and
civic facilities
0.727±0.022 0.678±0.021
POI Tourism Hotels, attractions,
tourist services
0.689±0.037 0.667±0.034
POI
Transportation
Stations, stops,
transport hubs
0.671±0.035 0.622±0.036
Population
Activity
CARTO Spatial
Features
Human activity
index
Composite human-
presence proxy
0.930±0.009 0.911±0.007
Nighttime lights Nighttime lights:
VIIRS average
radiance
0.769±0.059 0.758±0.050
Cell-tower
density
Cell-tower density0.704±0.024 0.696±0.023
Table B.2. Per-target downstream performance at ZCTA resolution.PlacePulse embeddings are area-
weighted from H3 resolution 7 to ZCTAs; PDFM embeddings are used at their native ZCTA resolution. Reporting
conventions matchTable B.1. Population Activity, Points of Interest, and Entrepreneurship targets are scored in log
space.
Category Source Target Description PlacePulseR 2 PDFMR 2
Public
Health
PDFM benchmark
conus27
Poor physical
health
Adults reporting
poor physical health
0.741±0.021 0.683±0.019
Poor mental
health
Adults reporting
poor mental health
0.669±0.045 0.642±0.036
High blood
pressure
Adults with high
blood pressure
0.689±0.023 0.666±0.021
High cholesterol Adults with high
cholesterol
0.516±0.062 0.481±0.074
Diabetes Adults with
diagnosed diabetes
0.673±0.012 0.627±0.022
35

Category Source Target Description PlacePulseR 2 PDFMR 2
Obesity Adults classified
obese
0.642±0.076 0.621±0.078
Cancer Adults with cancer,
excluding skin cancer
0.638±0.043 0.568±0.044
Stroke Adults who have had
a stroke
0.669±0.023 0.601±0.038
Coronary heart
disease
Adults with coronary
heart disease
0.647±0.044 0.562±0.073
Chronic kidney
disease
Adults with chronic
kidney disease
0.635±0.027 0.554±0.029
COPD Adults with COPD0.683±0.063 0.627±0.059
Asthma Adults with current
asthma
0.562±0.053 0.498±0.091
Arthritis Adults with arthritis0.668±0.043 0.636±0.043
Smoking Adults who currently
smoke
0.698±0.045 0.642±0.027
Binge drinking Adults reporting
binge drinking
0.381±0.039 0.332±0.058
Physical
inactivity
Adults reporting no
leisure-time physical
activity
0.685±0.013 0.638±0.056
Sleep under 7 h Adults sleeping
under 7 hours
0.599±0.055 0.585±0.056
Annual checkup Adults who had a
routine checkup
0.378±0.181 0.346±0.146
Dental visit Adults who visited a
dentist
0.684±0.043 0.651±0.057
Cholesterol
screening
Adults screened for
cholesterol
0.367±0.2710.392±0.200
Blood-pressure
medication
Hypertensive
adults taking BP
medication
0.597±0.0410.686±0.023
Economic
status
USDA ERS Food
Access Research
Atlas (2019)
Median family
income
Median family
income, ACS-derived
(USD)
0.796±0.011 0.743±0.034
Low food access
share
Share of population
far from a
supermarket (>1
mi urban />10 mi
rural)
0.594±0.0320.625±0.035
Poverty rate Share of population
below the federal
poverty line
0.658±0.025 0.611±0.026
PDFM benchmark
conus27
Median
household
income
Median household
income (USD)
0.656±0.057 0.561±0.064
Median home
value
Median value of
owner-occupied
homes (USD)
0.750±0.026 0.683±0.021
NREL / U.S. DOE
LEAD Tool (2022)
Energy burden Average household
energy cost as a
share of income
0.572±0.080 0.572±0.059
36

Category Source Target Description PlacePulseR 2 PDFMR 2
Energy cost Average annual
household energy
cost (USD)
0.407±0.0990.438±0.081
Population
Activity
PDFM benchmark
conus27
Population Resident population
count
0.723±0.0270.825±0.023
Population
density
Population density,
log10
0.933±0.008 0.865±0.011
Nighttime lights Nighttime lights
radiance, log10
0.955±0.004 0.903±0.012
CARTO Spatial
Features
Human activity
index
Human Activity
Index: composite
human-presence
proxy
0.935±0.037 0.834±0.038
Cell-tower
density
Cell-tower density in
the unit
0.768±0.0160.850±0.007
Physical
Geography
PDFM benchmark
conus27
Elevation Mean ground
elevation (m)
0.555±0.2180.821±0.112
Tree cover Share of area under
tree canopy
0.702±0.054 0.667±0.064
Points of
Interest
Overture Maps POI Total All POI categories
combined
0.810±0.0170.933±0.005
POI Retail Shops and retail
outlets
0.803±0.0200.928±0.005
POI Healthcare Clinics, hospitals,
pharmacies
0.812±0.0200.932±0.005
POI Offices Office and
professional-services
premises
0.823±0.0160.925±0.005
POI Food and
drink
Restaurants, cafes,
bars
0.806±0.0180.923±0.004
POI Financial Banks, ATMs,
financial services
0.796±0.0160.919±0.006
POI Leisure Sports, recreation,
entertainment
0.806±0.0190.918±0.004
POI Education Schools, universities,
training
0.766±0.0210.886±0.007
POI Public
services
Government and
civic facilities
0.728±0.0220.862±0.004
POI Tourism Hotels, attractions,
tourist services
0.742±0.0190.869±0.010
POI
Transportation
Stations, stops,
transport hubs
0.736±0.0240.870±0.004
Social
capital
Social Capital Atlas Economic
connectedness
Share of high-
socioeconomic-status
friends among low-
status residents
0.741±0.024 0.740±0.027
Friending
clustering
Friendship clustering
coefficient: how
interconnected a
resident’s friends are
0.689±0.027 0.686±0.025
37

Category Source Target Description PlacePulseR 2 PDFMR 2
Entrepre-
neurship
Startup
Cartography
Project
Startup
formation rate
Startup Formation
Rate: new business
registrations (log1p)
0.779±0.0340.848±0.025
RECPI Regional
Entrepreneurship
Cohort Potential
Index (log)
0.751±0.0250.796±0.030
Table B.3. Per-target downstream performance at non-native target resolutions.Both PlacePulse and
PDFM are area-weighted from their native spatial supports to voting precincts or census tracts. Reporting conventions
matchTable B.1.
Category Source Target Description PlacePulseR 2 PDFMR 2
Elections New York Times
2024 presidential
precinct map
Democratic lead Democratic
minus Republican
vote share, 2024
presidential
0.737±0.054 0.709±0.055
Economic
Mobility
Opportunity Atlas Upward mobility
(p25)
Mean adult income
rank for children
raised at the 25th
income percentile
0.546±0.046 0.508±0.020
Social
Vulnera-
bility and
Resilience
FEMA National
Risk Index
Social
vulnerability
FEMA NRI social
vulnerability score
0.384±0.040 0.269±0.034
Community
resilience
FEMA NRI
community resilience
score
0.486±0.063 0.335±0.117
38

References
M. Agarwal, M. Sun, C. Kamath, et al. General geospatial inference with a population dynamics
foundation model, 2024.
Applied Geographic Solutions. AGS data products, 2025a. URLhttps://appliedgeographic.com.
Applied Geographic Solutions. Database documentation, 2025b. URLhttps://appliedgeographic.
com/database-documentation/.
R. Bommasani, D. A. Hudson, E. Adeli, et al. On the opportunities and risks of foundation models,
2021.
C. S. Bretherton, M. Widmann, V. P. Dymnikov, J. M. Wallace, and I. Bladé. The effective number
of spatial degrees of freedom of a time-varying field.Journal of Climate, 12(7):1990–2009, 1999.
doi:10.1175/1520-0442(1999)012<1990:TENOSD>2.0.CO;2.
C. F. Brown, M. R. Kazmierski, V. J. Pasquarella, et al. AlphaEarth foundations: An embedding
field model for accurate and efficient global mapping from sparse label data, 2025.
J. Cao, J. Chen, X. Wang, and Q. Li. UrbanMMCL: Urban region representations via multi-modal
and multi-graph self-supervised contrastive learning.ISPRS Journal of Photogrammetry and
Remote Sensing, 232:75–93, 2026. doi:10.1016/j.isprsjprs.2025.11.012.
Y. Chen, W. Huang, K. Zhao, Y. Jiang, and G. Cong. Self-supervised representation learning for
geospatial objects: A survey.Information Fusion, 123:103265, 2025. doi:10.1016/j.inffus.2025.
103265.
Clay Foundation. Clay foundation model: An open source ai model for earth, 2024. URLhttps:
//madewithclay.org.
Y.Cong, S.Khanna, C.Meng, P.Liu, E.Rozi, Y.He, M.Burke, D.B.Lobell, andS.Ermon. SatMAE:
Pre-training transformers for temporal and multi-spectral satellite imagery. InAdvances in Neural
Information Processing Systems 35 (NeurIPS 2022), 2022. doi:10.48550/arXiv.2207.08051.
M. Del Giudice. Effective dimensionality: A tutorial.Multivariate Behavioral Research, 56(3):
527–542, 2021. doi:10.1080/00273171.2020.1743631.
C. Elbers, J. O. Lanjouw, and P. Lanjouw. Micro-level estimation of poverty and inequality.
Econometrica, 71(1):355–364, 2003. doi:10.1111/1468-0262.00399.
P. Elliott and D. Wartenberg. Spatial epidemiology: Current approaches and future challenges.
Environmental Health Perspectives, 112(9):998–1006, 2004. doi:10.1289/ehp.6735.
Z. Feng, C. Atzberger, S. Jaffer, et al. TESSERA: Temporal embeddings of surface spectra for earth
representation and analysis. InProceedings of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition (CVPR), pages 34818–34831, 2026. doi:10.48550/arXiv.2506.20380.
A. Getis and J. K. Ord. The analysis of spatial association by use of distance statistics.Geographical
Analysis, 24(3):189–206, 1992. doi:10.1111/j.1538-4632.1992.tb00261.x.
K. He, X. Chen, S. Xie, Y. Li, P. Dollár, and R. Girshick. Masked autoencoders are scalable
vision learners. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 16000–16009, 2022. doi:10.1109/CVPR52688.2022.01553.
39

M. O. Hill. Diversity and evenness: A unifying notation and its consequences.Ecology, 54(2):
427–432, 1973. doi:10.2307/1934352.
W. Huang, L. Cui, M. Chen, D. Zhang, and Y. Yao. Estimating urban functional distributions with
semantics preserved POI embedding.International Journal of Geographical Information Science,
36(10):1905–1930, 2022. doi:10.1080/13658816.2022.2040510.
J. Jakubik, S. Roy, C. E. Phillips, et al. Foundation models for generalist geospatial artificial
intelligence, 2023.
K. Janowicz, S. Gao, G. McKenzie, Y. Hu, and B. Bhaduri. GeoAI: spatially explicit artificial
intelligence techniques for geographic knowledge discovery and beyond.International Journal of
Geographical Information Science, 34(4):625–636, 2020. doi:10.1080/13658816.2019.1684500.
N. Jean, S. Wang, A. Samar, G. Azzari, D. Lobell, and S. Ermon. Tile2Vec: Unsupervised
representation learning for spatially distributed data. InProceedings of the AAAI Conference on
Artificial Intelligence, volume 33, pages 3967–3974, 2019. doi:10.1609/aaai.v33i01.33013967.
G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y. Liu. LightGBM: A highly
efficient gradient boosting decision tree. InAdvances in Neural Information Processing Systems
30 (NIPS 2017), pages 3146–3154, 2017.
D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. In3rd International
Conference on Learning Representations (ICLR 2015), San Diego, CA, 2015. URL https:
//arxiv.org/abs/1412.6980. arXiv:1412.6980.
K. Klemmer, E. Rolf, C. Robinson, L. Mackey, and M. Rußwurm. SatCLIP: Global, general-purpose
location embeddings with satellite imagery. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 39, pages 4347–4355, 2025. doi:10.1609/aaai.v39i4.32457.
E. Levina and P. J. Bickel. Maximum likelihood estimation of intrinsic dimension. InAdvances in
Neural Information Processing Systems 17 (NIPS 2004), pages 777–784, Cambridge, MA, 2005.
MIT Press.
S. Li, S. Dragicevic, F. Antón Castro, et al. Geospatial big data handling theory and methods: A
review and research challenges.ISPRS Journal of Photogrammetry and Remote Sensing, 115:
119–133, 2016. doi:10.1016/j.isprsjprs.2015.10.012.
Y. Lin, H. Wan, S. Guo, and Y. Lin. Pre-training context and time aware location embeddings from
spatial-temporal trajectories for next location prediction. InProceedings of the AAAI Conference
on Artificial Intelligence, volume 35, pages 4241–4248, 2021. doi:10.1609/aaai.v35i5.16548.
W. Luo and F. Wang. Measures of spatial accessibility to health care in a GIS environment.
Environment and Planning B: Planning and Design, 30(6):865–884, 2003. doi:10.1068/b29120.
B. C. Mitchell and J. Chakraborty. Landscapes of thermal inequity: disproportionate exposure to
urban heat in the three largest US cities.Environmental Research Letters, 10(11):115005, 2015.
doi:10.1088/1748-9326/10/11/115005.
P. A. P. Moran. Notes on continuous stochastic phenomena.Biometrika, 37(1–2):17–23, 1950.
doi:10.1093/biomet/37.1-2.17.
40

F. Noardo. Multisource spatial data integration for use cases applications.Transactions in GIS, 26
(7):2874–2913, 2022. doi:10.1111/tgis.12987.
J. K. Ord and A. Getis. Local spatial autocorrelation statistics: Distributional issues and an
application.Geographical Analysis, 27(4):286–306, 1995. doi:10.1111/j.1538-4632.1995.tb00912.x.
C. J. Reed, R. Gupta, S. Li, S. Brockman, C. Funk, B. Clipp, K. Keutzer, S. Candido, M. Uytten-
daele, and T. Darrell. Scale-MAE: A scale-aware masked autoencoder for multiscale geospatial
representation learning. InProceedings of the IEEE/CVF International Conference on Computer
Vision (ICCV), 2023. doi:10.1109/ICCV51070.2023.00378.
N. Roig-Tierno, A. Baviera-Puig, J. Buitrago-Vera, and F. Mas-Verdu. The retail site location
decision process using GIS and the analytical hierarchy process.Applied Geography, 40:191–198,
2013. doi:10.1016/j.apgeog.2013.03.005.
A. Sablayrolles, M. Douze, C. Schmid, and H. Jégou. Spreading vectors for similarity search. In7th
International Conference on Learning Representations (ICLR 2019), 2019. doi:10.48550/arXiv.
1806.03198.
D. Sculley. Web-scale k-means clustering. InProceedings of the 19th International Conference on
World Wide Web (WWW ’10), pages 1177–1178, Raleigh, NC, 2010. ACM. doi:10.1145/1772690.
1772862.
C. E. Shannon. A mathematical theory of communication.Bell System Technical Journal, 27(3):
379–423, 1948. doi:10.1002/j.1538-7305.1948.tb01338.x.
A. D. Singleton and S. E. Spielman. The past, present, and future of geodemographic research
in the united states and united kingdom.The Professional Geographer, 66(4):558–567, 2014.
doi:10.1080/00330124.2013.848764.
A. D. Singleton and S. E. Spielman. Geodemographics and residential differentiation: A methodolog-
ical review and future directions for learned representations of the social landscape.Computers,
Environment and Urban Systems, 125:102396, 2026. doi:10.1016/j.compenvurbsys.2025.102396.
S. A. Stouffer, E. A. Suchman, L. C. DeVinney, S. A. Star, and R. M. Williams.The American
Soldier: Adjustment During Army Life, volume 1 ofStudies in Social Psychology in World War
II. Princeton University Press, Princeton, NJ, 1949.
Uber Technologies. H3: A hexagonal hierarchical geospatial indexing system, 2018. URLhttps:
//h3geo.org.
C. Wang and L. Yin. Defining urban big data in urban planning: Literature review.Journal of
Urban Planning and Development, 149(1), 2023. doi:10.1061/(ASCE)UP.1943-5444.0000896.
T. Wang and P. Isola. Understanding contrastive representation learning through alignment and
uniformity on the hypersphere. InProceedings of the 37th International Conference on Machine
Learning (ICML 2020), volume 119 ofProceedings of Machine Learning Research, pages 9929–9939,
2020. doi:10.48550/arXiv.2005.10242.
X. Wang, T. Cheng, S. Law, Z. Zeng, L. Yin, and J. Liu. Multi-modal contrastive learning of urban
space representations from POI data.Computers, Environment and Urban Systems, 120:102299,
2025. doi:10.1016/j.compenvurbsys.2025.102299.
41

Z. Wang, H. Li, and R. Rajagopal. Urban2Vec: Incorporating street view imagery and POIs for
multi-modal urban neighborhood embedding. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 34, pages 1013–1020, 2020. doi:10.1609/aaai.v34i01.5450.
N. Waters. Tobler’s first law of geography. In Douglas Richardson, Noel Castree, Michael F.
Goodchild, Audrey Kobayashi, Weidong Liu, and Richard A. Marston, editors,The International
Encyclopedia of Geography. Wiley, 2017. doi:10.1002/9781118786352.wbieg1011.
Y. Wen and Y. Zhou. Demo2Vec: Learning region embedding with demographic information.
InProceedings of the 7th ACM SIGSPATIAL International Workshop on AI for Geographic
Knowledge Discovery (GeoAI ’24), pages 71–74, 2024. doi:10.1145/3687123.3698289.
M. C. Whitlock. Combining probability from independent tests: The weighted z-method is superior
to fisher’s approach.Journal of Evolutionary Biology, 18(5):1368–1373, 2005. doi:10.1111/j.
1420-9101.2005.00917.x.
Y. Yan, H. Wen, S. Zhong, W. Chen, H. Chen, Q. Wen, R. Zimmermann, and Y. Liang. UrbanCLIP:
Learning text-enhanced urban region profiling with contrastive language-image pretraining from
the web. InProceedings of the ACM Web Conference 2024 (WWW ’24), 2024. doi:10.1145/
3589334.3645378.
Z. Yao, Y. Fu, B. Liu, W. Hu, and H. Xiong. Representing urban functions through zone embedding
with human mobility patterns. InProceedings of the 27th International Joint Conference on
Artificial Intelligence (IJCAI-18), pages 3919–3925, 2018. doi:10.24963/ijcai.2018/545.
W. Zhang, J. Han, Z. Xu, H. Ni, H. Liu, and H. Xiong. Urban foundation models: A survey. In
Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining
(KDD ’24), 2024. doi:10.1145/3637528.3671453.
B. Zhou, X. Huang, S. Wang, et al. Measuring the spatial explicitness of GeoAI and geospatial
foundation models: A systematic review and future roadmap.ISPRS Journal of Photogrammetry
and Remote Sensing, 240:601–622, 2026. doi:10.1016/j.isprsjprs.2026.08.001.
42
