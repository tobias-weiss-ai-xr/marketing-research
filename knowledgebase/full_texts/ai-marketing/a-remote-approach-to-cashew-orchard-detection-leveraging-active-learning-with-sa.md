---
title: 'A Remote Approach to Cashew Orchard Detection: Leveraging Active Learning with Satellite Imagery
  in Guinea-Bissau'
url: https://arxiv.org/abs/2608.11996
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Miguel Pereira
- Sofia C. Pereira
- Maria J. P. Vasconcelos
- Patrícia Guedes
- Luke L. Powell
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.11996
pages: 29
chars: 45360
fetched_at: '2026-11-08T13:30:11+00:00'
kb_version: 1
---

# A Remote Approach to Cashew Orchard Detection: Leveraging Active Learning with Satellite Imagery in Guinea-Bissau

Highlights
A Remote Approach to Cashew Orchard Detection: Leveraging
Active Learning with Satellite Imagery in Guinea-Bissau
Miguel Pereira, Sofia C. Pereira, Maria J.P. Vasconcelos, Patr ´ ıcia Guedes,
Luke L. Powell, Jo˜ ao P. Pedroso
•Cashew cultivation dominates Guinea-Bissau’s land cover and economic
structure
•Mapped cashew orchards using 10m Sentinel-2 satellite imagery
•Improved cashew detection performance with a new Active Learning
based approach
•Produced the first countrywide and openly accessible cashew map using
2021 data
arXiv:2608.11996v2  [cs.CV]  18 Aug 2026

A Remote Approach to Cashew Orchard Detection:
Leveraging Active Learning with Satellite Imagery in
Guinea-Bissau
Miguel Pereiraa,∗, Sofia C. Pereira b, Maria J.P. Vasconcelosc, Patr ´ ıcia
Guedesd, Luke L. Powelld, Jo˜ ao P. Pedrosoe
aDepartment of Computer Science, Faculty of Sciences, University of Porto, Rua do
Campo Alegre, 4169-007 Porto, Portugal
bINESC-TEC, Faculty of Engineering, University of Porto, Rua Dr. Roberto Frias,
4200-465 Porto, Portugal
c Forest Research Centre, School of Agriculture, University of Lisbon, Tapada da Ajuda,
1349-017 Lisbon, Portugal
dCIBIO and BIOPOLIS, InBIO Associated Laboratory, Vair˜ ao Campus, University of
Porto, Rua do Crasto, 4485-661 Vair˜ ao, Portugal
eCMUP and Department of Computer Science, Faculty of Sciences, University of Porto,
Rua do Campo Alegre, 4169-007 Porto, Portugal
Abstract
Cashew production is a widespread economic activity in Guinea-Bissau,
as well as other countries in West Africa. However, unregulated cashew
production can be directly associated with increasing regionwide deforesta-
tion rates, biodiversity losses, and a fragile economic structure. There is no
nationwide database for listing or georeferencing cashew orchards, so there
is a clear need to remotely map their locations. In recent years, multiple
methods for detecting orchards have been developed, though they have only
been applied on a regional level. This work expands regional analyses to a
nationwide scale. It develops a scalable and cost-effective remote approach,
based on Sentinel-2 satellite imagery, using Machine Learning techniques to
detect cashew orchards automatically. Margin-based Active Learning tech-
niques were employed to develop an optimal training set in terms of the
number of points and their informativeness, leading to a cashew map with
94.0% balanced accuracy obtained entirely off-site. We created two datasets
∗Corresponding author. Email address: up201906711@edu.fc.up.pt
1

and a 2021 cashew map with 10m spatial resolution that are openly acces-
sible through GitHub 1. The results demonstrate the possibility of a broader
cashew orchard mapping, creating a new stepping stone for this environmen-
tal application.
Keywords:Land cover, Cashew orchards, Remote Sensing, Machine
Learning, Guinea-Bissau, West Africa
1 Introduction
Guinea-Bissau, West Africa, is suffering from an escalating environmental
crisis related to increasing deforestation [1]. Although the expansion of the
energy sector and illegal logging are associated with this phenomenon, defor-
estation in the region occurs mainly due to the conversion of forests to agricul-
tural fields, primarily for the production of cashew, rice, and peanuts [1, 2, 3]
(Figure 1). Cashew nut cultivation and commerce employs many thousands
of Guineans, accounts for over 90% of the national exported goods, and
covers between 18%−55% of the entire planted land, depending on the
region [4, 5, 6]. In addition to sustainability considerations, this overre-
liance on the cashew sector leads to a fragile single-crop economic structure.
The subsistence of the country and multiple families is heavily dependent
on market shifts and production values, which can be affected by pests, cli-
mate conditions, and the age of the orchard [6, 7, 8, 9, 10]. The associated
habitat conversion also imposes a major biodiversity threat that could have
irreversible long-term consequences [11, 12].
Efforts to map cashew orchards have been limited due to the difficulty
in differentiating between orchards and woodlands [13]. However, one recent
study combined Machine Learning models and Sentinel-2 images to success-
fully characterize cashew orchards in Cantanhez National Park, showing how
much this crop has encroached into the park [14]. Due to the expansion of
cashew orchards across the country, more comprehensive national mapping
is needed.
In this work, we propose an innovative fully remote method to detect
cashew orchards and the subsequent production of a cashew map, based on
the application of Machine Learning classifiers trained on remote sensing
1GitHub link:https://github.com/mrp2106/ALFICC
2

Figure 1: Transformation of a forested area into a cashew plantation. Note the structured
row pattern in some portions of the orchard. Google Earth, Maxar Technologies/Airbus.
data. Land cover classes were also acquired remotely, completely eliminating
the need for any on-site procedures during the project’s execution.
The remote annotation process still represents a considerably time-consuming
step. Motivated by this difficulty, our study explores the capacity of Active
Learning (AL) techniques to optimize the class acquisition process. These
techniques are applied when the learning algorithm is allowed to query an
expert for labels (also called classes, in our case being land cover types) of
certain samples [15]. This is an iterative process, where at each step, a small
batch of the currently most valuable points are passed onto the expert, which
then assigns a class to each of them — called the annotation or labeling pro-
cess — and uses them to expand the current training dataset. This way, an
optimal training set with non-redundant data samples is created, which can
3

positively impact the performance of associated ML classifier. This iterative
procedure is typically repeated until either we are satisfied with the perfor-
mance of the ML model, or have reached the time and/or resource budget
allocated to the labeling process.
The remainder of the article is organized as follows: Section 2 contains
a brief review of previous cashew monitoring and detection work, as well as
the application of AL for remote data classification. Section 3 describes the
proposed methodology for analyzing the defined region of interest. Section 4
presents the results of the project’s experiments, notably the AL performance
and the production of a cashew map, together with a brief discussion of the
obtained results. Section 5 concludes the article.
2 Related Work
Monitoring land use and land use changes (LULUC) is essential to un-
derstand the impact of primary sector activities on habitats and biodiversity
changes. The advancements of satellite or aerial imagery, in terms of avail-
ability and spatiotemporal resolution, paired with more powerful geoprocess-
ing tools, significantly improve the monitoring capabilities [16]. This has led
to the expansion of cashew detection research in recent years [14, 16, 17, 18].
The main difficulty in detecting cashew remotely comes from the identical
spectral signatures of cashew and forests, as well as the typical placement
of cashew trees in already forested areas, which creates a spatial mixture
of both land cover types [13, 14, 16]. Despite these issues, past research
has shown the aptitude of ML classifiers to identify cashew orchards based
on medium-high spatial resolution imagery, using either Sentinel-2 or Plan-
etScope satellite-acquired data [14, 16], or sub-meter aerial images [16, 17,
18]. Ensemble-based algorithms or Support Vector Machines appear as ca-
pable classifiers [14, 16], despite their inability to work with non-tabular
datasets. In contrast, deep learning algorithms are better suited for matrix-
based rasters typically associated with remote sensing imagery, and can use
this to extract latent spatial features that are valuable to the classification
task [17]. Either way, these studies agree that the addition of non-spectral
variables containing either temporal or spatial-based information about each
sample and its neighboring region typically helps any type of classifier in
overcoming the difficulty of distinguishing spectrally similar classes, such as
cashew orchards and forest woodlands, and improving overall classification
performance.
4

The main contributions of our work to the cashew detection problem
come in two fronts: the technique used and the spatial coverage. Firstly,
we applied Active Learning (AL) heuristics in order to optimize the labeling
process — that is, the process of assigning labels (in our case, land cover
classes) to certain selected samples (in our case, pixels). We focused on pool-
based sampling techniques, which deal with large amounts of raw, unlabeled
data [19]. Despite the clear applicability in remote sensing classification
projects with access to large amounts of raw unlabeled satellite imagery, no
previous work has ever attempted to apply AL to create refined datasets
for cashew mapping, which made us eager to evaluate the impact of these
techniques for this specific use case. Secondly, we took advantage of the
scalability aspect of a fully remote approach to perform a cashew mapping
for a larger region, contrasting pre-existing work that focused on monitoring
smallholder farms or protected areas [14, 16, 17, 18]. To our knowledge, no
cashew orchard map for the entire country of Guinea-Bissau has ever been
created or made publicly available; thus, filling this gap was the major goal
of our study. Both these fronts create an innovative approach to the study
of cashew cultivation and associated effects in Guinea-Bissau, in an efficient
and scalable way that is capable of keeping up with the nationwide cashew
expansion and changes.
3 Data and Methods
3.1 Study area and datasets
The project’s region of interest (ROI) corresponds to the entire country
of Guinea-Bissau — mainland and islands off the western coast, as shown
in Figure 2 —, covering an extent of 34,800 km 2. The region’s land cover is
formed by savanna woodlands, tropical and sub-tropical forests, and other
open or closed-canopy landscapes [2]. This vegetation is marked by two
seasonal behaviors: a rainy season from May to October, and a dry season
from November to April. Despite its smaller area, the country holds a large
plant and animal diversity and includes key biodiversity areas, which have
been threatened by the habitat conversion accelerated by cashew cultiva-
tion [11, 12]. Two datasets were created for the development of the study’s
ML and AL procedures. Samples were acquired not only in Guinea-Bissau,
but also in a 2,700 km 2 neighboring region down to theKogonriver in the
Republic of Guinea — also shown in Figure 2 — which contains very similar
5

Figure 2: Visualization of the main study area and region of interest, the country of
Guinea-Bissau, West Africa. A smaller region in the Republic of Guinea, down to the
Kogonriver, is also represented. Data samples were collected in both areas. Made with
QGIS [20].
environmental and land cover patterns [12]. The datasets followed different
sampling techniques, namely:
•Random Sampling (RS) dataset:corresponds to 4498 samples
(pixels) randomly selected for labeling. This heuristic represents the
simplest form of expanding a training set, which is useful as a baseline
comparison with other AL algorithms [21]. Further, the unbiased and
scattered selection of new samples likely ensures a diverse and repre-
sentative data selection.
•Margin Sampling (MS) dataset:is comprised of 1816 points (pix-
els) selected by the Margin Sampling AL heuristic. This technique re-
quests the unlabeled samples with the smallest margin values, that is,
those closest to the ML classifier’s stipulated decision boundary [15, 22].
6

The heuristic was chosen for its compatibility with the SVM classifier
that was considered in the remainder of the project (more details in
sections 3.4 and 4.1).
Both datasets consider pixels from eight land cover classes. Our clas-
sification system follows the one utilized in the Forest Reference Emission
Level report (FREL) for Guinea-Bissau [23], which was further expanded by
RSeT [24] to include more land cover types. Namely, the eight classes we
considered are: Closed-canopy Forest, Open-canopy Forest, Mangrove, Sa-
vanna woodlands/ Sparse vegetation, Cashew orchards, Non-Forest, Water,
and Other (Non-Cashew). Non-Forest is considered an ”umbrella class”, as it
aggregates pixels corresponding to buildings, roads, farm fields, and empty
land. Meanwhile, Other (Non-Cashew) is used to describe pixels that are
definitely not cashew, but which do not fall under the scope of any other
class — for example, pixels that encompass forest and urban areas, or man-
grove and water, or any other combination of multiple land cover types that
thus cannot be attributed to any other individual class. These pixels can be
useful in a Cashew vs. Non-Cashew classification setting, but should be dis-
carded in any other context (more details in section 4.1). Figure 3 shows the
geographical distribution of each dataset, and Table 1 presents the respective
pixel counts per class.
7

Figure 3: Geographical distribution of the Random Sampling (top) and Margin Sampling
(bottom) datasets.
3.2 Satellite image processing
Remote sensing imagery from Copernicus Sentinel-2 (S2) was used as the
base satellite data [25]. This mission is composed of two orbiting satellites
8

Table 1: Number of pixels per class in the two obtained datasets.
Nºof pixels
Random Sampling Margin Sampling
Closed Forest 9 0
Open Forest 289 132
Mangrove 417 57
Savanna 1303 511
Cashew 993 503
Non-Forest 1024 261
Water 111 9
Other (non-cashew) 352 436
Total 4498 1909
phased at 180 ◦, producing a new image with almost global coverage with a
five-day revisiting time. The satellites collect radiance measurements across
13 discrete bands in the electromagnetic spectrum’s visible, near-infrared,
and shortwave-infrared regions, with spatial resolutions of either 10m, 20m,
or 60m. In our work, every non-10m band was resampled to a 10m spatial
resolution, which matches the resolution of every considered additional band
— thus, the produced cashew map also presents a 10m spatial resolution.
Satellite image processing and feature extraction were performed in Google
Earth Engine (GEE), a cloud-based platform that combines open-access im-
agery with distributed computational resources for advanced processing [26].
Figure 4 presents a flowchart of this procedure.
An image collection was considered using the S2 images from March 2017
up to April 2021. These data were collected and stored in tiles — 109.8km×
109.8km segments of the Earth’s surface —, which can be assembled to form
a spatially continuous image for the entire region of interest through a process
called mosaicking [14]. From the resulting 13-band raster collection, training
features were extracted to develop the ML classifiers. They are categorized
and shown in the flowchart across three different branches according to the
nature of the information they represent:
•Spectral features:Four Sentinel-2 bands were discarded from the
analysis: bands B1, B9, and B10 are typically ignored in surface-level
applications, as they account for atmospheric effects; also, band B8A
9

was dropped due to its spectral similarity and overlap with band B8.
Four bands related to different vegetation indices were added to the
base image collection, corresponding to the NDVI, NBR, EVI, and
EVI2 indices. Spectral overlap between different land cover types is a
typical concern during the classification procedure, noticeably between
cashew orchards and certain types of forest woodlands. This overlap
is not the same at every time of the year and is typically smaller by
the end of the dry season, which spans from November to April [14].
Therefore, we combined all the base S2 images from April 2021 and ex-
tracted the median image with the 13 spectral bands through a process
called compositing — using an aggregation function to merge spatially
overlapping imagery into a single image.
•Temporal features:Temporal information can highlight other dis-
tinctive characteristics of land cover types, such as the seasonal vari-
ability of savanna woodlands or the stability of a closed-canopy forest,
thus enhancing the predictive capacity of an associated classifier. For
this purpose, we applied the Continuous Change Detection and Classi-
fication (CCDC) algorithm to the S2 2017-2021 image collection [27].
The procedure works in two stages: initially, a change detection algo-
rithm identifies breaks in the typical behavior of each pixel — which
can be associated with a land cover change —, partitioning a pixel’s
time series into segments; secondly, a harmonic regression is applied to
each of the resulting segments for each pixel. The coefficients of the
harmonic regression can then be extracted and used as temporal predic-
tors for the classification procedure. For each pixel, we extracted 104
coefficients of the time segment overlapping with the 30th of April 2021,
plus nine other bands that were also added during the preprocessing
phase of GEE’s CCDC implementation regarding Elevation, Rainfall,
and other geographic-related features, creating a 113-band image.
•Spatial features:The most common type of manually extracted
features for multispectral image classification regard spatial informa-
tion [14]. The similarity or contrast with neighboring pixels can be
used to detect, for example, the sparse pattern of savanna woodlands
in the dry season, as well as the structured tree pattern that concerns
certain cashew orchards, such as the one shown in Figure 1. We utilized
the Gray-Level Co-Occurrence Matrix (GLCM) algorithm to calculate
10

spatial statistics [28]. This method works with gray-scale intensities —
valued between 0 and 255 — to describe a central pixel’s neighboring
region, using metrics like the sum average, entropy, local contrast, and
dissimilarity between pairs of pixels. The GEE implementation calcu-
lates 18 statistics per input band and thus was only applied to the April
2021 median composite. This resulted in a 234-band image, which was
merged with the spectral April 2021 median composite and the CCDC
image to produce the final image asset, containing 360 features for every
pixel in the region of interest.
Figure 4: Satellite image processing and feature acquisition flowchart.
3.3 Active Learning and label acquisition
Figure 5 shows a flowchart of the sampling techniques and AL proce-
dures that led to the creation of the Random Sampling and Margin Sam-
pling datasets. An initial training set common to both sampling heuristics
was stipulated before any other data acquisition process because the evolu-
tion of the AL iterative procedure is directly influenced by its training data.
We separated 11 randomly acquired polygons — 93 pixels — for this purpose,
having at least one polygon of each of the eight annotated classes to ensure
11

that every classifier does not have to discover new classes during the iter-
ative labeling process, and two polygons for Savanna, Cashew, Non-Forest,
and Other (Non-Cashew).
The labeling process was accompanied by RSeT researchers [24] with pre-
vious experience from other remote or on-site projects in the area. Google
Earth Pro’s Historical Imagery tool (Landsat/Copernicus/Maxar Technolo-
gies/Airbus) was used to view the terrain and assign classes according to
each pixel’s land cover in April 2021, at the end of the dry season. In each
Random and Margin Sampling iteration, after the algorithm requested pixels
for labeling, the entire 3×3 patch of the immediate neighboring pixels was
also stored and given to the annotator (the first author) for labeling, which
sped up the annotation process. Often, cases were too difficult to classify
with confidence, mostly due to the fuzzy nature of land cover over such a
large and diverse area (multiple pixels contained mixed behaviors and were
thus not suited to be categorized into one single class), or the lack of high-
resolution imagery in Google Earth Pro to assess the land cover type in 2021.
In such cases, the samples were discarded.
Figure 5: Schema of the Active Learning and dataset creation process.
The final step of the AL process is the stopping criteria, which stipu-
late when the iterations and dataset creation end. The literature typically
suggests stopping the acquisition process either when the associated model
performance reaches satisfactory levels or when the time and labeling bud-
gets have been exhausted. However, we also considered the possibility of
stopping if a significant portion of the samples requested by the heuristic
12

became overwhelmingly hard to annotate and/or had to be discarded. Thus,
we decided that the AL procedure should be terminated when one of the
three aforementioned criteria was reached.
3.4 Machine Learning workflow and post-processing
All Machine Learning and image classification procedures were imple-
mented in Python [29]. This includes the stipulation of a test set, feature
selection, and hyperparameter tuning for model selection, with every step be-
ing performed after the creation of the Random Sampling (RS) dataset, but
before the acquisition of Margin Sampling (MS) data, since this heuristic’s
iterative selection of points is dependent on these choices. A train-test split
of the RS data was performed using a grouped stratified sampling strategy,
which deals with data representation in each set with stratified sampling; the
approach keeps all the pixels from the same patch together in either training
or testing to avoid spatial autocorrelation affecting the test scores [14]. The
dataset was split 50−50 to ensure a highly representative test set. Mean-
while, the MS dataset was only used for model training - every MS result
was also evaluated on the RS test set to ensure the comparability with the
RS results.
Due to the high number of bands in the raster described in section
3.2 (360), feature selection was performed on the RS training set, follow-
ing two different procedures:scikit-learn’s [30] recursive feature elimina-
tion algorithm, which iteratively removes the least prominent features that
have little to no impact on the model’s predictive performance; a feature-
importance based approach, where we utilized scikit-learn’s Random Forests
feature importancesattribute to get an estimate of each variable’s usefulness
with a value between 0 and 1, and only kept those with a score above the
threshold of 1 360 , which represents the average importance in a random classi-
fier scenario (where every feature would have the same impact on the model’s
performance).
Hyperparameter tuning followed the bayesian optimization strategies of
thehyperoptPython library [31]. Two types of classifiers were considered
for optimization: Support Vector Machines (SVMs) and Random Forests
(RFs). SVMs had already shown the highest cashew detection performance
in previous research [14]. RFs have been considered in the aforementioned
research as well, and despite not presenting the best results, they are one of
the few ML algorithms implemented in GEE’s native Machine Learning tools,
which can facilitate the transition between the satellite image processing and
13

ML sections. The hyperparameter search was performed optimizing mean
F1-Cashew on 5-fold cross-validation in the RS training set for both models.
During hyperparameter tuning, we explored two different classification
scenarios: firstly, we discarded the samples from the eighth class (Other
non-cashew) and worked with 7-class classifiers; after, we considered binary
classifiers to work in a Cashew vs. Non-Cashew classification setting (this
time including the eighth class into the broader Non-Cashew category). We
performed hyperparameter tuning separately for each case to observe if a
noticeable performance difference could arise from this label change. As
discussed in section 4.1, the binary SVM classifier outperforms the 7-class
model, and as such was the considered model for the AL section.
The final classifier of the MS experiments, trained on the full MS dataset,
was used to create a prediction-based land cover map for the entire region of
interest. A final post-processing step was performed by applying a sieve filter
to the land cover map. This filter removes raster polygons that are smaller
than a pre-defined threshold and replaces them with the pixel value (class)
of the largest neighboring polygon, thus smoothing the land cover map. The
optimal threshold value will be discussed in section 4.3.
4 Results and Discussion
4.1 Feature selection and hyperparameter tuning
During the feature selection process, the recursive feature elimination
algorithm selected 250 of the initial 360 variables, while the above-average
importance process kept only 67 features. Figure A.8 in Appendix A shows
that the latter does not translate to any performance drop in comparison
to the recursive feature elimination procedure or the usage of the total 360
features, even presenting a slightly higher median score than the other two.
Hence, we only kept the 67 features selected by the above-average procedure
for the remaining ML procedures and the training of the Active Learning
classifiers.
The details of the hyperparameter tuning section, including the search
spaces for each classifier type and the architecture of the best classifier in
both 7-class and 2-class scenarios, are available in Appendix A. Table 2
shows the test scores of the best 7-class algorithm, a Random Forest, and
the 2-class model, an SVM. Both balanced accuracy and Cashew F1 scores
are higher for the binary SVM classifier. Naturally, the binary prediction
task is less complex: collapsing the original Non-Cashew land cover classes
14

into just a single category erases minority classes - such as Closed Forest and
Water (Table 1) - which typically drag the metrics down.
Table 2: RS test results for the best 7-class and 2-class classifiers. Hyperparameter search
was made for maximizing mean F1-Cashew on 5-fold cross-validation in the RS training set.
Balanced Accuracy F1-score Cashew
Best 7-class model (RF)0.803 0.814
Best 2-class model (SVM)0.905 0.843
Due to our main goal of detecting cashew cultivation, we have decided to
work with the binary classification approach and the best 2-class model from
this point onward. Because the best binary classifier is an SVM, we opted
to use a margin-based heuristic, specifically MS, as the AL heuristic to build
the dataset.
4.2 Active Learning results
After optimizing a classifier on the Random Sampling train set and select-
ing an initial training set for the Active Learning process, we advanced to the
acquisition of newly labeled samples to form the Margin Sampling dataset.
We also simulated an AL evolution on the RS training data by iteratively
selecting larger portions of this dataset, to serve as a baseline comparison.
The results are presented in Figure 6.
Both selection procedures lead to improvements of the associated ML
classifiers — that is, the performance of the ML model increases as we add
new labeled pixels to the training set in each RS or MS iteration, until
it stagnates. However, MS does so more efficiently, with steeper increases
during the early iterations: just after two AL steps, the classifier obtained
an F1-score of 81.2% using MS, in comparison to the 71.2% score using
randomly selected data. Peak performance is also higher with MS labeled
training data, reaching 87.2% Cashew F1-score with 1254 training samples
— in comparison, RS’s peak is 85.4% F1-score with 1599 samples.
The results of the final iterations show a degree of oscillation. This could
mean the classifier is reaching the maximum predictive performance, though
we cannot claim this with certainty, considering this behavior is only observed
for a small number of final iterations. However, during the MS annotation
task, the performance decay after the fifth iteration’s peak was noticeably
15

Figure 6: Cashew F1-score evolution during the Active Learning procedure
accompanied by the request of more intricate samples and the increase in
sample rejection rates (the proportion of requested samples by the AL heuris-
tic for which the annotators could not attribute a land cover class), as shown
in Figure B.9 in Appendix B. Thus, even if we hadn’t already reached the
performance cap, we would have stopped the annotation process due to the
increased difficulty in labeling new pixels with confidence, which could steeply
increase the risk of mislabeling and data intrusion, whilst also adding little
new informative samples to the train set.
Therefore, the AL experiments finished with a Balanced Accuracy of
92.2% and F1-score of 85.7% after nine iterations, with 1909 samples. Ran-
dom Sampling finalizes with 90.9% Balanced Accuracy and 85.0% F1-score,
using 2274 training samples. The results show the power of Active Learning
in the context of multi-spectral image classification and cashew detection, as
it allows for a more efficient training sample selection, which helps improve a
classifier’s maximum predictive performance and also leads to better results
with fewer labeled data.
16

4.3 Post-processing and final land cover map
With the final Margin Sampling classifier (the SVM trained on the full
MS dataset), we obtained a cashew land cover map from the predictions for
every pixel in the ROI. In order to apply the sieve filter to smoothen the
map, we first needed to stipulate the minimum polygon sizep. Since this
is a user-defined threshold, we searched for the optimal value in a grid. As
shown in Figure C.10 in Appendix C, the best results are obtained with
p= 350, which leads to a Cashew F1-score of 89.5% and balanced accuracy
equal to 94.0%, an improvement of both metrics over the unfiltered results,
as interpreted in the figure.
Table 3: Area estimates and percentage of Cashew and Non-Cashew in Guinea-Bissau.
Cashew (ha) Non-Cashew (ha) Cashew (%) Non-Cashew (%)
902,149 2,575,932 25.9 74.1
The filtered 2021 land cover map for cashew monitoring, based on SVM
predictions, is shown in Figure 7. In total, 25.9% of the country’s area is
identified as Cashew, as presented in Table 3, almost equal to the percentage
of terrestrial protected areas [14]. The northwest quadrant of the country
contains the most cashew, followed by the southwest and northeast. Cashew
plantations are scarcer in the southeast. These results constitute the basis
for an accurate assessment of the state of the cashew sector in the country,
which then allows the implementation of appropriate measures to control its
prevalence.
Further insights can be drawn from this study, and particularly from the
cashew land cover map. For example, the relationship between cashew culti-
vation and human activity becomes clear in the overlay presented in Figure
C.11 in Appendix C, as it highlights the geographical relationship between
cashew orchards and communities. Another example is presented in Fig-
ure C.12, which shows the spatial intersection between the cashew map and
Guinea-Bissau’s terrestrial protected areas (PAs). This example highlights
an opposite relation to that of the communities overlay, as the PAs typi-
cally intersect regions with fewer cashew plantations (aside from Cantanhez
National Park, whose case was studied in [14]). This visual interpretation
already hints at the correlation of cashew cultivation with both phenom-
ena, though further analysis is needed to draw out causal effects from these
interactions, if they exist.
17

Figure 7: Final 2021 Land cover map. Obtained with a post-processing 350psieve filter
applied to the SVM predictions map.
5 Conclusions
This study is the first attempt at an openly accessible cashew mapping for
Guinea-Bissau, West Africa. Through the combined use of an SVM classifier
paired with an Active Learning procedure that developed a minimal but
optimized training dataset, we were able to produce a fully remote and cost-
effective approach to detect cashew orchards. Margin Sampling proved to be
an efficient sample selection algorithm, resulting in 89.5% Cashew f1-score
and 94.0% balanced accuracy test results after a sieve filter was applied to
the predictions map.
Cashew cultivation has a deep environmental, economic, and humani-
tarian impact in many West African countries, including Guinea-Bissau [11].
This effect is exacerbated by the unregulated expansion of plantations, which
in turn complicates the accurate estimation of cultivation areas and produc-
tion values. Recently, researchers have identified mapping and monitoring
cashew orchards as a priority for a sustainable future in West Africa [11, 14].
Our work directly contributes to this by serving as the basis for a deeper
assessment of the state of the cashew sector in the area, which can lead to
18

more adequate and effective action focused on the country’s sustainable de-
velopment. Further, our approach can be applied to other Western African
countries where cashew orchard expansion is a threat to biodiversity, facili-
tating an accurate measure of the area this crop currently occupies.
Further developments can be made to expand the approach presented
in this study. Cashew mapping accuracy might increase with the usage of
more advanced patch-based classifiers [32], or through the creation of a new
training dataset based on a different AL heuristic. It would also be valuable
to map land cover across years to develop a change detection system that
could then be used to monitor the expansion of cashew orchards in Guinea-
Bissau and beyond.
19

Appendix A Feature selection and hyperparameter tuning
Figure A.8 compares the results obtained using every feature with two
variable selection procedures: recursive feature elimination (RFECV) and
selecting features with an importance score above the 1/360 threshold that
corresponds to the mean (average) importance. Considering the performance
similarity between the different scenarios, the boxplots demonstrate that we
can reduce the dimensionality of the feature space without sacrificing model
performance. This justifies our choice of working with the smallest feature
space composed of the 67 variables with an above-average importance score.
Figure A.8: Performance with three different variable sets: every feature (360), the selec-
tion through recursive feature elimination RFECV (250), and features with above average
importance value (67). Results were obtained with stratified grouped 10-fold on the Ran-
dom Sampling training set.
Regarding the hyperparameter tuning process, Table A.4 shows the con-
sidered hyperparameters for RFs and SVMs, and the respective search spaces.
A separate search was performed for 7-class and 2-class classification paradigms,
with the best models from each scenario being detailed in Table A.5. The
AL results that followed were obtained using the best binary SVM classifier
due to its higher cashew prediction scores, as shown in Table 2.
20

Table A.4: Hyperparameter search space for Random Forests and Support Vector Ma-
chines. The search space was equivalent for the 7-class and 2-class classification paradigms.
Hyperparameters Search range
Random Forests
Number of estimators 50−450, with steps of 10
Maximum depth 1−12
Max features per split 3−70, with steps of 3
Support Vector Machines
C (regularization parameter) 10 −3 −10 1
Kernel Linear,poly, orrbf
Gamma 10 −10 −10 1 (forrbforpolykernel)
Degree 2, 3, or 4 (forpolykernel)
Table A.5: Best classifiers after hyperparameter tuning, for both 2-class and 7-class clas-
sification scenarios.
2 class 7 class
Best model SVM Best model RF
C 0.0117 Number of estimators 73
Kernel poly Maximum depth 10
Gamma 0.6439 Max features per split 2
Degree 4
Appendix B AL experiments and MS rejection rates
Figure B.9 highlights the increase in labeling difficulty after the peak per-
formance iteration, for the MS labeling process. After the peak, the heuristic
started requesting more and more difficult pixels, often with a mixture of land
cover classes, which translated in an increase in the number of discarded sam-
ples. This was especially evident during the final iteration, where over a third
of the pixels requested by the model could not be labeled.
21

Figure B.9: Percentage of the number of requested pixels per MS iteration that could not
be labeled and were thus discarded.
Appendix C Sieve filter and communities overlay
Figure C.10 shows how the map scores vary with the sieve filter polygon
size threshold. The first data point represents the scenario where no filter
is applied to the map. The results show that the application of such a filter
is beneficial, since the test scores are always higher when applying a sieve
filter, no matter the value of the polygon size threshold.
22

Figure C.10: Test scores obtained after applying a sieve filter with different polygon size
thresholdpparameter values. The first point, with minimum polygon size thresholdp
equal to 0, represents the test scores obtained with no filter applied.
Figure C.11 shows the spatial overlap between the largest cashew pre-
dominant regions and existing urban locations, overlaying Guinea-Bissau’s
2017 census data on a land cover map processed with a 350psieve filter.
This evidence is clearer in the Northern part of the country. In addition,
Figure C.12 presents the overlay with Guinea-Bissau’s terrestrial protected
areas (PAs), showing the opposite tendency: most protected areas appear
in southeastern regions, with little cashew orchards (aside from Cantanhez
National Park). The northwest quadrant, which shows the highest orchard
density, also coincides with the absence of any terrestrial PAs.
23

Figure C.11: Land cover map with an overlay of Guinea-Bissau communities according to
the 2017 national census. [24]
Figure C.12: Land cover map with an overlay of Guinea-Bissau Terrestrial and Inland
Waters Protected Areas. [33]
24

Acknowledgements
We want to thank Lu ´ ıs Palma for his valuable insights and input about
the results and project applicability, as well as RSeT [24] for providing us
with supporting technical documentation and datasets that were crucial for
the early project development.
This work was co-funded by the European Union’s Horizon 2020 research
and innovation programme under grant agreement No 854248 and by the
project TROPIBIO NORTE-01-0145-FEDER-000046, supported by Norte
Portugal Regional Operational Programme (NORTE2020), under the POR-
TUGAL 2020 Partnership Agreement, through the European Regional De-
velopment Fund (ERDF).
The author Jo˜ ao Pedro Pedroso was partially supported by CMUP, mem-
ber of LASI, which is financed by national funds through FCT – Funda¸ c˜ ao
para a Ciˆ encia e a Tecnologia, I.P., under the projects with reference
UIDB/00144/2020 and UIDP/00144/2020.
References
[1] A. I. Seca, et al., Expansion of Cashew Cultivation and its Environ-
mental and Economic Impacts on Guinea-Bissau, Brazilian Journal of
Environmental Sciences (RBCIAMB) 56 (2021) 385–397. doi:10.5327/
Z21769478950.
[2] Republic of Guinea-Bissau, Updated Nationally Determined Contri-
bution In The Framework Of The Paris Climate Agreement, United
Nations Climate Change (2021).
[3] L. Powell, et al., EU deforestation law overlooks emerging crops, Science
379 (2023) 340–341. doi:10.1126/science.adf9994.
[4] World Food Programme Executive Board, Guinea-Bissau coun-
try strategic plan (2023–2027), 2022 (last accessed: 2025-03-
28). URL:https://executiveboard.wfp.org/document download/
WFP-0000142930.
[5] Y. Kone, Improving cashew cultivation: F AO supports re-
search activities in Guinea-Bissau, 2022 (last accessed: 2025-03-
28). URL:https://www.fao.org/africa/news-stories/news-
25

detail/Improving-cashew-cultivation-FAO-supports-research-
activities-in-Guinea-Bissau/en.
[6] E. Djassi, Cashew nuts production in Guinea-Bissau (2022) 3–12.
doi:10.52270/27132447 2022 12 3.
[7] UNDP, COVID-19 Socio Economic Impact Assessment in
Guinea-Bissau, 2020 (last accessed: 2025-04-26). URL:https:
//www.undp.org/guinea-bissau/news/covid-19-socio-economic-
impact-assessment-guinea-bissau.
[8] P. Sierra-Baquero, et al., Insights into the cashew production sys-
tem in Guinea-Bissau: implications for agroecosystem sustainability,
Frontiers in Sustainable Food Systems 8 (2024) 1439820. doi:10.3389/
fsufs.2024.1439820.
[9] S. Vasconcelos, et al., New records of insect pest species associated with
cashew, Anacardium occidentale L.(Anacardiaceae), in Guinea-Bissau,
African Entomology 22 (2014) 673–677. doi:10520/EJC160231.
[10] P. Havik, et al., Agro-Economic Transitions in Guinea-Bissau (West
Africa): Historical Trends and Current Insights, Sustainability 10 (2018)
3408. doi:10.3390/su10103408.
[11] P. Guedes, et al., At the tipping point: Can biodiversity and rural liveli-
hoods endure uncontrolled cashew expansion in West Africa?, Biotropica
56 (2024). doi:10.1111/btp.13374.
[12] L. Palma, et al., Updating the conservation status of the forest ele-
phant Loxodonta cyclotis in Guinea-Bissau, Oryx (2023). doi:10.1017/
S0030605323000674.
[13] M. P. Temudo, M. Abrantes, The cashew frontier in Guinea-Bissau,
West Africa: changing landscapes and livelihoods, Human ecology 42
(2014) 217–230. doi:10.1007/s10745-014-9641-0.
[14] S. C. Pereira, et al., Mapping Cashew Orchards in Cantanhez National
Park (Guinea-Bissau), Remote Sensing Applications: Society and En-
vironment 26 (2022) 100746. doi:10.1016/j.rsase.2022.100746.
26

[15] D. Tuia, et al., A survey of active learning algorithms for supervised
remote sensing image classification, IEEE Journal of Selected Topics in
Signal Processing 5 (2011) 606–617. doi:10.1109/JSTSP.2011.2139193.
[16] A. Rege, et al., Mapping cashew monocultures in the Western Ghats
using optical and radar imagery in Google Earth Engine, Remote
Sensing Applications: Society and Environment 28 (2022) 100861.
doi:10.1016/j.rsase.2022.100861.
[17] L. Yin, et al., Mapping smallholder cashew plantations to inform sus-
tainable tree crop expansion in Benin, Remote Sensing of Environment
295 (2023) 113695. doi:10.1016/j.rse.2023.113695.
[18] Nitidae, A pilot study of remote sensing by drone and satellite to
strengthen the cashew sector in Mozambique, 2022 (last accessed:
2025-03-28). URL:https://www.nitidae.org/en/actualites/une-
etude-pilote-de-teledetection-par-drone-et-satellite-pour-
renforcer-la-filiere-anacardier-au-mozambique.
[19] R. Thoreau, et al., Active learning for hyperspectral image classification:
A comparative review, IEEE geoscience and remote sensing magazine
10 (2022) 256–278. doi:10.1109/MGRS.2022.3169947.
[20] QGIS development team, QGIS Geographic Information System, 2009
(last accessed: 2025-04-26). URL:http://qgis.org.
[21] Z. Lei, et al., Active deep learning for hyperspectral image classification
with uncertainty learning, IEEE geoscience and remote sensing letters
19 (2021) 1–5. doi:10.1109/LGRS.2020.3045437.
[22] J. Kremer, et al., Active learning with support vector machines, Wi-
ley Interdisciplinary Reviews: Data Mining and Knowledge Discovery 4
(2014) 313–326. doi:10.1002/widm.1132.
[23] V. Cassama, et al., Proposed Forest Reference Emission Level
for the National System of Protected Areas of Guinea-Bissau,
2019 (last accessed: 2025-04-26). URL:https://redd.unfccc.int/
submissions.html?country=gnb.
27

[24] RSeT, NGO for international cooperation in renewable natural resource
management and adaptation to climate change, 2011 (last accessed:
2025-04-26). URL:https://www.rset.eu/.
[25] ESA, Sentinel-2, Colour vision for Copernicus, 2024 (last ac-
cessed: 2025-03-28). URL:https://www.esa.int/Applications/
Observing the Earth/Copernicus/Sentinel-2.
[26] N. Gorelick, et al., Google Earth Engine: Planetary-scale geospatial
analysis for everyone, Remote Sensing of Environment 202 (2017) 18–
27. doi:10.1016/j.rse.2017.06.031.
[27] Z. Zhu, C. E. Woodcock, Continuous change detection and classifica-
tion of land cover using all available Landsat data, Remote Sensing of
Environment 144 (2014) 152–171. doi:10.1016/j.rse.2014.01.011.
[28] G. Ajmera, Feature extraction of images using GLCM (gray level
cooccurrence matrix), 2024 (last accessed: 2025-03-28). URL:https:
//medium.com/@girishajmera/feature-extraction-of-images-
using-glcm-gray-level-cooccurrence-matrix-e4bda8729498.
[29] G. Van Rossum, F. L. Drake, Python 3 Reference Manual, CreateSpace,
2009.
[30] Scikit-learn development team, Scikit-learn: Machine Learning in
Python, 2007 (last accessed: 2025-04-26). URL:https://scikit-
learn.org/stable/.
[31] Hyperopt development team, Hyperopt: Distributed Asynchronous
Hyper-parameter Optimization, 2021 (last accessed: 2025-04-26). URL:
https://hyperopt.github.io/hyperopt/.
[32] X.-Y. Tong, et al., Land-cover classification with high-resolution re-
mote sensing images using transferable deep models, Remote Sensing of
Environment 237 (2020) 111322. doi:10.1016/j.rse.2019.111322.
[33] UNEP-WCMC and IUCN, Protected Planet: The World Database on
Protected Areas (WDPA) and World Database on Other Effective Area-
based Conservation Measures (WD-OECM), 2025 (last accessed: 2025-
05-01). URL:www.protectedplanet.net.
28
