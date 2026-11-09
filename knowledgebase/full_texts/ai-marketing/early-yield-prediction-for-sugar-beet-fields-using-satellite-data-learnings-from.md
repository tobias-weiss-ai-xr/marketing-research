---
title: Early Yield Prediction for Sugar Beet Fields using Satellite Data -- Learnings from Specialized
  Vision Transformers
url: https://arxiv.org/abs/2607.17661
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Philipp Vaeth
- Bhumika Laxman Sadbhave
- Denise Dejon
- Gunther Schorcht
- Magda Gregorova
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.17661
pages: 16
chars: 44453
fetched_at: '2026-11-08T13:26:50+00:00'
kb_version: 1
---

# Early Yield Prediction for Sugar Beet Fields using Satellite Data -- Learnings from Specialized Vision Transformers

Early Yield Prediction for Sugar Beet Fields
using Satellite Data - Learnings from Specialized
Vision Transformers
Philipp Vaeth1,2(),
Bhumika Laxman Sadbhave1,
Denise Dejon3,
Gunther Schorcht3, and
Magda Gregorová1
1 Center for Artificial Intelligence and Robotics, Technical University of Applied
Sciences Wuerzburg-Schweinfurt, Franz-Horn-Strasse 2, Wuerzburg, Germany
{philipp.vaeth,magda.gregorova}@thws.de
2 Bielefeld University, Universitaetsstrasse 25, Bielefeld, Germany
3 green spin GmbH, Magdalene-Schoch-Strasse 5, Wuerzburg, Germany
Abstract.Remote sensing has become an increasingly valuable tool for
agricultural monitoring, particularly through the use of publicly avail-
able satellite imagery. However, effectively integrating domain knowledge
into machine learning methods remains challenging. This study presents
a real-world example of early sugar beet harvest yield forecasting from
purely optical Sentinel-2 imagery, demonstrating how a tight integration
of domain knowledge and machine learning can lead to synergistic gains.
We empirically find that using very small vision transformer patch sizes
and all available Sentinel-2 spectral bands improves our model despite
being uncommon design choices in the domain. As a practical contri-
bution, we were able to identify a large fraction of low-yield fields in a
different year early on in the growth cycle through a modified training
setup and a ranking-based detection of underperforming fields.
Keywords:Remote sensing·Sentinel-2·Satellite·Vision Transformer
·ViT·Yield Prediction.
1 Introduction
Remote sensing, especially satellite imagery, has gained interest from the ma-
chine learning community in recent years [27]. The scalability of modern machine
learning methods, in combination with the large volume of satellite imagery,
has led to improvements in many areas, for example in optical crop yield es-
timation [29, 20]. The domain presents several technical challenges, including
incomplete time series, varying object sizes, high-dimensional inputs, measure-
ment errors, extremely large data volumes, and scarce labels. These challenges
require non-trivial task-specific adaptations of standard computer vision models.
Unfortunately, such adaptations are rarely transferable to other tasks, because
arXiv:2607.17661v1  [cs.CV]  20 Jul 2026

2 Vaeth et al.
different applications may require fundamentally different receptive fields, time
resolutions, and spectral bands.
This study focuses on sugar beet yield prediction purely from optical satellite
imagery, a prominent, inexpensive, and scalable resource in remote sensing that
is nevertheless rarely used as the sole source of information. We gather a data set
of several thousand sugar beet field locations in Bavaria, Germany, for the years
2019 and 2024, the corresponding yield in tons per hectare (t/ha) at the end of
the harvest, and the publicly available Sentinel-2 satellite images of the fields
throughout the growth cycle. The sugar beet (beta vulgaris) is an important
crop in Europe for various industries such as livestock, fermentation, biofuel and
export. The amount of sugar in the harvest depends largely on location, weather
conditions, as well as prevalence of diseases or other stress factors that occur
during the growth cycle [21].
Many existing deep-learning yield predictors rely on multi-source data such
as climate data [13, 16, 22], multi-spectral information from other sources [17],
data from Unmanned Aerial Vehicle (UAVs) [32, 18], soil data [13] or fine-grained
labels [10]. The models also use task-specific combinations of spectral bands [16,
22, 17, 18, 10] and custom receptive fields [16, 17, 32, 10] for their models. These
modeling prerequisites make their design choices and results hard to transfer to
other yield prediction tasks. Instead of providing a new competitive prediction
system, we isolate the yield prediction performance to a purely optical, single-
label-per-field setting and empirically validate critical design choices. We make
the following contributions:
–We formulate the sugar beet yield prediction task based on purely optical
Sentinel-2 satellite data as a supervised regression problem at the field level
across several thousand fields in Bavaria and a held-out test year motivated
by the practical application.
–We systematically study ViT design choices (patch size, number of spectral
bands, positional encodings, embedding size and heads) for this setting and
show that very small patches and using all Sentinel-2 bands are critical for
performance.
–We extend the model with temporal encodings to enable early prediction
and a ranking-based detection of underperforming fields. Our results show
that, even though the absolute yield prediction is extremely challenging on
purely optical data, a large fraction of low-yield fields can be detected well
before the harvest.
2 Methods
In this section, we describe the dataset, the prediction task, pre-processing steps,
the model setup, training details, the experimental setup, the evaluation, and
the limitations.
Data setThis paper uses publicly available Sentinel-2 Level 2A satellite im-
ages [4]. The Sentinel-2 satellite takes an image every 5 days (called temporal

Early Sugar Beet Yield Prediction using Satellite Data 3
instances) with bands of different spatial resolutions. Four bands at 10 meter
resolution contain the classic RGB values and a "near-infrared" (NIR) band. Six
bands at 20 meter resolution contain four "visible and near-infrared" (VNIR)
bands and two "short-wave infrared" (SWIR) bands for applications such as
snow, ice, cloud detection or vegetation moisture stress assessment. Three bands
at 60 meter spatial resolution focus on cloud screening, atmospheric correction
and cirrus detection. The 20 m bands are resampled to 10 m spatial resolution
for input consistency. The three 60 m bands are discarded due to redundancy
with a cloud mask described in the following paragraph. For reference, a patch of
16 pixels in the data at a ground resolution of 10 m corresponds to a real-world
area of over three and a half soccer fields (25600m2).
Task definitionIn addition to the publicly available satellite images, we have a
cloud mask, a field mask and the corresponding harvest yield available in the
project. This custom data set contains 2614 fields from the year 2019 and 5695
fields from the year 2024. The goal is to predict the field-level sugar yield based
on the last Sentinel-2 satellite image before the harvest. We purposefully do not
usethetemporalnatureofthesatellitedatauntillaterinthepaper(section4),in
order to empirically test design choices when using only the optical information
in the images. This means we formulate the task as an image regression problem
with only spatial and channel information from the satellite just before the
harvest. We are unable to disclose the data set of the project at the current
time due to contractual constraints with the industrial partner and privacy of
farm locations, but we will explain our pre-processing and modeling choices as
clearly as possible.
Pre-processingThe Sentinel-2 data is provided as chunks of1000×1000px
images with 10 channels. To be able to use machine learning techniques on this
data, we need to first pre-process the images. We deliberately chose to keep the
pre-processing steps minimal and rather rely on the end-to-end training of our
model to extract information. We provide a full overview of the pre-processing
steps in figure 1. First, we filter defective measurements through a cloud mask.
Afterwards, we extract each field into a separate field image. The locations and
shapes of the fields are given by the field mask. Due to inconsistent field sizes,
the pixels are placed on the top left and padded to the model input size of
128×128px, such that there is always only one complete field per field image and
shapes of fields are preserved. We chose this input size to fit the largest field in
the data set, which however leads to additional compute overhead for fields that
are much smaller. To prevent the model from inferring implicit information from
the surrounding context (such as the field location), we remove non-field pixels
during the padding operation. For the empirical study in section 3, we select
the last temporal instance before the harvest for each field. Later in section 4,
we extend the model to train on all temporal instances through time encodings
to enable early prediction. We do not condition the model on other information
such as acquisition dates, longitude or latitude in order to prevent the model

4 Vaeth et al.
Fig.1: Data pre-processing pipeline
from overly relying on this conditioning information rather than purely on the
optical data.
Model setup & trainingWe mainly consider deep neural networks for the end-
to-end feature extraction but also include two non-deep baselines in our exper-
iments. The simplest baseline is predicting the mean yield of the fields in the
training set. For a simple domain-specific baseline, we train a linear regression
model on statistics (min, mean, max) of the NDVI, EVI, MSI vegetation indices
(see section 3.3). Convolution-based models are directly applied with only minor
modifications in the first layer to accommodate for the 10 Sentinel-2 channels
and treat them exactly as in a three channel RGB setup. The Vision Trans-
former [5] operates over a sequence of non-overlapping patches of a field image.
Inspired by the class embedding from the original ViT, we add an extra token
to aggregate information from all patches during the attention operation into a
single embedding. We also considered predicting a harvest yield per patch and
aggregating this information across all patches in a field by simply adding the
values, but this would lead to a strong model assumption that all patches are
similarly important as the gradients in the backwards pass would be equally dis-

Early Sugar Beet Yield Prediction using Satellite Data 5
tributed across all patches. Preliminary experiments showed better performance
through the learned token aggregation.
After the feature extraction by the models, a single linear layer predicts the
harvest yield per field image based on the final feature vector. For faster training
convergence, the bias of the regression layer is initialized to the mean yield of
the training set. We intentionally kept this regression layer simple to limit the
influence of the classifier and to enable clear design conclusions about the end-
to-end feature extractor. The 2019 data will be split into training and validation
sets (70:30), and the 2024 data will be the test set for the evaluation of the
model. We train all models with an RMSE objective on the harvest yield, a
learning rate of 0.001, a batch size of 128, a maximum of 150 epochs and include
early stopping based on a running average of the validation RMSE loss.
Experimental setup & evaluationFor our experiments, we initially predict the
harvest yield from the last satellite image before the harvest (section 3) and
then extend the model to early prediction based on images from early on in
the growth cycle (section 4). We measure the performance of the harvest yield
prediction through an RMSE objective as a standard metric in the machine
learning community. We train the model on the 2019 training data and report
the 2019 validation RMSE for different models and hyperparameter configura-
tions. We use the 2024 data as a hold-out test set to align with the practical
application, as models are trained on historical data to predict the yield for
new satellite images of an upcoming season. In our setup, this also serves as an
out-of-distribution test to ensure the learned optical features are truly capturing
yield-specific features, as the 2019 and 2024 seasons had fundamentally different
climate and growth conditions. For the early prediction in section 4, we intro-
duce a ranking-based metric to identify underperforming fields. We compare the
complexity of all baselines and model design choices by reporting the parameter
count and an estimate of compute requirements for a single forward pass (in
GFLOPS). We show a pareto-style plot for the performance versus complexity
trade-off for all experiments in figure 2.
LimitationsAs a result of our purely optical-based data set and the task-driven
experimental setup across two years, comparison with previous work is challeng-
ing. Adapting previous work to our data set would not lead to a fair comparison,
as methods require specific choices of spectral bands and task-dependent recep-
tive fields (for example [31, 28, 30, 19, 17, 14]). Previous methods are also usually
built on additional sources of information and more conditioning variables such
as longitude, latitude, acquisition dates, climate data [24, 13], multi-spectral in-
formation from other sources [17], lidar data [15], soil data [13], or additional
crop growth models [2, 33]. We also considered using recent foundational models
(such as [9, 23, 3, 7, 1]) as pre-trained feature extractors, but adapting them
to our prediction task with our limited size data set would require substantial
model modifications and is beyond the scope of this study. We instead aim to
provide rigorous experiments starting from multiple simpler baseline models that
are all adapted to our specific task and then further modified by testing criti-

6 Vaeth et al.
cal design choices that may help future work to develop specialized models for
remote sensing tasks.
3 Experiments
In this section, we empirically test important design choices in a hypothesis
driven way. We compare simple baseline model architectures in section 3.1, ex-
perimentally test the importance of the receptive field in section 3.2, assess the
relevance of Sentinel-2 bands in section 3.3, question whether positional encod-
ings are beneficial for the task in section 3.4, and show the complexity versus
performance trade-off in section 3.5. We conclude this section by summarizing
our findings and putting them into broader context in section 3.6.
3.1 Which baseline architecture is most suitable for the task?
Recentyieldpredictionapproachesusedeeplearningtoleveragethelargeamount
of data in the remote sensing field for more accurate forecasting [28, 25, 14, 31,
30, 11, 19]. Methods are commonly tailored to the task and auxiliary data avail-
able in their projects, making comparisons challenging. Especially convolution-
based neural networks are popular in the domain, whereas newer transformer
architectures are becoming more popular in recent years [12].
We start our experimental analysis with the simplest baseline, which predicts
the mean yield of the fields in the training set. For a domain-specific baseline
similar to hand-crafted feature engineering approaches [29], we train a linear
regression model on min, mean and max values of the NDVI, EVI and MSI veg-
etation indices with negligible model parameters and compute requirements. We
consider standard convolution-based models for our sugar beet yield prediction
including SqueezeNet [8], ResNet-18 and ResNet-50 [6]. SqueezeNet was chosen
as a light-weight convolution-based model. We also include a single-layer vision
transformer (ViT [5]) with one 64-dimensional head and a patch size of eight.
The hyperparameter choices for the ViT model were inspired by standard config-
urations for natural images and by preliminary experiments. Although there are
no direct comparisons to previous methods, we provide a comparison of widely
used image backbones with varying capacities and simple, non-deep baselines.
The results in table 1 show that, despite being the smallest model both in
terms of trainable parameters and floating point operations, the ViT baseline
outperforms all other models. We hypothesize this is due to different inductive
priors in the architectures that can be exploited in combination with domain
knowledge. The ViT allocates most compute on the attention mechanism be-
tween patches of the input as a fixed receptive field to learn differences between
parts of the field. The CNN counterparts spread out compute over an increasing
receptive field through network depth, while compressing spatial information
with the assumption that close pixels are more related. For our specific yield
prediction task where each pixel already represents many plants, we hypothesize
that aggregating information over an increasing receptive field is likely not as
important as for natural RGB images.

Early Sugar Beet Yield Prediction using Satellite Data 7
Table 1: The performance and computational requirements for various baseline
models on the sugar beet yield prediction task.
Validation
RMSE
Test
RMSE
Parameters
(million) GFLOPS
Train set mean 18.50 22.06 - -
Linear Regression 18.49 22.06 0 0
ResNet-50 17.96 22.30 23.66 366
ResNet-18 18.08 20.73 11.23 175
SqueezeNet 17.59 20.70 0.759 25
ViT baseline17.50 20.480.322 21
3.2 How important is the receptive field for the model quality?
It is common in previous work to adapt the models to the task at hand, specifi-
cally the receptive field of the model through hyperparameter configurations [31,
28, 30, 19, 17, 14]. We believe this is an important design consideration and
should be motivated by domain knowledge. The patch size of the vision trans-
former in our case defines the receptive field for the model and is a major factor
for compute requirements. A larger patch size leads to fewer patches for the
attention mechanism and a higher compression rate as more input pixels are
represented by a fixed dimensional vector. For natural RGB images, the higher
compression rate is usually not critical, as objects used for downstream tasks
are made up of multiple pixels. In our case, we hypothesize that the patch size
is much more important as each pixel already represents a large part of a field
with extremely many plants (1 pixel = 100m 2), where small differences be-
tween areas of the fields are important indicators for the harvest yield. The
recommended ViT patch size for natural images isp= 16[5] and many re-
mote sensing foundational models choose similar patch sizes for the Sentinel-2
data [3, 9, 23]. We show the effect of the vision transformer patch size on the
performance of our specific harvest yield prediction in table 2. We consider the
patch sizesp∈[1,2,4,8,16,32]with the common notation of ViT/p.
The results in table 2 confirm our hypothesis that smaller patch sizes are
critical for performance. The model error on both the validation and the test set
generally decreases with a lower patch size, whereas the compute requirements
increase due to a higher amount of patches for the attention mechanism. The
best model has a patch size ofp= 2. Interestingly, the model with a patch size of
p= 1, which results in self-attention on a pixel level, shows worse performance
than some models operating over patched inputs. We hypothesize this is due to
the high amount of compute required to train the pixel-level model, which would
require longer training times, a larger data set and different hyperparameters.
We will continue our experiments with the best ViT/2 model and leave the
limitations of the pixel-level transformer to future work.

8 Vaeth et al.
Table 2: A comparison of the simple vision transformer across different patch
sizes for the sugar beet yield prediction task.
Validation
RMSE
Test
RMSE
Parameters
(million) GFLOPS
ViT/32 18.20 21.64 0.937 3
ViT/16 18.00 21.07 0.445 7
ViT/8 17.50 20.48 0.322 21
ViT/4 17.45 20.64 0.292 75
ViT/217.12 20.410.284 295
ViT/1 17.65 20.81 0.282 1172
Table 3: Performance comparison across different Sentinel-2 input band varia-
tions (all, S4, RGB) and vegetation indices (NDVI, EVI, MSI) for the ViT/2
model on the sugar beet yield prediction task.
Sentinel-2
Bands
Input
Channels
Validation
RMSE
Test
RMSE
All 1017.12 20.41
S4 4 17.66 20.56
NDVI,EVI,MSI 3 17.43 20.58
RGB 3 18.24 21.10
NDVI 1 18.49 22.13
EVI 1 18.49 22.13
MSI 1 18.07 21.32
3.3 Are all Sentinel-2 input bands necessary for a good model?
It is common in previous work to use task-specific combinations of spectral
bands [16, 22, 17, 18, 10]. Common combinations include the Normalized Dif-
ference Vegetation Index (NDVI= NIR−RED NIR+RED), the MODIS Enhanced Vegeta-
tion Index (EVI = 2.5× (NIR−Red) (NIR+6×Red−7.5×Blue)) and the Moisture Stress Index
(MSI= SWIR1 NIR ). In this experiment, we compare the end-to-end feature extrac-
tion on the full Sentinel-2 band spectrum to single input channels, common com-
binations and domain-specific vegetation indices. The channel combinations are:
all Sentinel-2 input channels including RGB and all available near-infrared chan-
nels as in the previous experiment; S4 for the red, blue, and two near-infrared
channels, which are used in the vegetation index calculation; NDVI, EVI and
MSI as common domain-specific vegetation indices calculated through a linear
combination of the S4 channels; RGB as only the three common color channels
without near infrared information.
As shown in table 3, training on all Sentinel-2 bands outperforms any other
hand-selected bands or combinations. We hypothesize that, given the difficulty
of the purely optical prediction task, removing channels limits the model’s abil-

Early Sugar Beet Yield Prediction using Satellite Data 9
ity to learn nuanced differences across fields. Interestingly, even domain-specific
vegetation indices fall short of the learned band combinations from end-to-end
training. We hypothesize this is due to the linear nature of band combinations
in the vegetation indices and the task-specific constants in the index computa-
tions that would require hyperparameter tuning. The difference in the amount
of parameters (281k-284k) and compute across the band configurations is neg-
ligible (292-295 GFLOPS) in our setting, as only the first patch embedding
layer is affected. Future work will include employing explainability techniques to
understand what channel combinations were learned by the model through end-
to-end training and how these relate to the domain-specific vegetation indices.
This knowledge could guide the development of even more specialized models.
3.4 How informative are the relative positions of field patches?
So far in our experiments, we have only relied on the optical data and excluded
standard relative positional encodings for the patches. Without positional encod-
ings, the spatial relationships between the patches and the shapes of the fields
are lost in the attention mechanism. Since the yield per field is already normal-
ized by the field size (t/ha), the field size should not affect the yield. As the
model could simply predict a yield per patch and aggregate the predictions for
the entire field, we hypothesize that adding the relative positions of the patches
does not influence performance.
To test if the relative positional encodings for the patches benefit the model,
we compare no positional encoding, a learned positional encoding and the fixed
sinusoidal positional encoding [26]. The results in table 4 indicate that adding
positional encodings does not improve the model. For the case of the learned
encodings, the trainable parameter count almost doubles, which is difficult to
optimize with the current size of the data set. The fixed sinusoidal encodings
do not add any meaningful computational overhead but also do not improve
the model. We hypothesize that the knowledge of relative patch positions is not
necessary for our prediction task. The padding may also play a role as the model
does not need to first learn to separate fields from non-fields, for which relative
positions could be beneficial. Excluding relative positional encodings further
prevents potential data leakage between the 2019 train set and the 2024 test set
becauseinformationabouttheorderofthefieldpatches,andthereforetheshapes
ofthefields,islost.Wewillomitpositionalencodingsforthecurrentexperiments
and explore possible explicit yield aggregation and positional encoding synergies
in future work.
3.5 How does model complexity affect task performance?
After the task-specific model design, scaling up the model to trade-off compute
and performance is a possible next step. A common approach to scale the vision
transformer is the embedding dimensionality for each patch and the amount
of attention heads for the multi-head self-attention. We explore the embedding
dimensionalityd∈[64,128,192,256,320]and the number of attention headsh∈

10 Vaeth et al.
Table 4: A comparison of different positional encoding strategies for the ViT/2
model on the sugar beet yield prediction task.
Positional
Encodings
Validation
RMSE
Test
RMSE
Parameters
(million)
None17.12 20.410.284
Learned 17.48 21.00 0.546
Sinusoidal 17.44 20.44 0.284
Table 5: The influence of a higher embedding dimensiondand more attention
headshon the ViT/2 model performance for the sugar beet yield prediction.
dimensions GFLOPS validation RMSE loss test RMSE loss
h=1 2 4 8 16h=1 2 4 8 16
64 295 17.12 17.16 17.10 17.02 17.10 20.41 20.33 20.21 20.29 20.01
128 625 17.02 17.06 17.06 17.01 17.13 20.40 20.6919.8520.41 20.41
192 989 17.06 17.20 17.00 17.07 17.03 20.46 20.55 20.95 20.23 20.22
256 1387 17.04 17.14 17.15 17.0316.9620.35 20.55 20.12 20.20 19.96
320 1820 17.01 16.98 17.04 17.05 17.07 20.63 20.35 20.24 20.06 20.21
[1,2,4,8,16]. We also tested multiple attention layers in sequence, but this lead
to consistently worse performance with greatly increased compute requirements.
Table 5 shows the different ViT configurations with compute requirements
and the respective performance. The configuration from the previous experi-
ments is highlighted in gray and the best performing configuration is shown in
bold. Comparing different columns per row in table 5 shows that simply adding
more attention heads does not improve performance. Similarly, when comparing
the rows in the same column, increasing the embedding dimensionality of each
patch does not consistently lead to a lower error, but greatly increases the re-
quired compute. We hypothesize that a higher embedding dimensionality, more
attention heads and even more transformer layers would require a bigger data
set to improve performance without overfitting on the fields in the training set.
3.6 Learnings from the specialized vision transformer
To put our findings into context, the pareto-style plot in figure 2 shows the
performance versus compute trade-off. The first baseline ViT model from table 1
with a patch size of eight provides decent performance at very low compute. The
best performance is achieved be the ViT configuration with a small patch size of
two with four attentions heads and a 128-dimensional embedding dimensionality.
The best compromise configuration is the ViT/2-16h-64d model with a small
patch size of two, all spectral bands and additional attention heads. For our goal
to extract as much information as possible from purely optical Sentinel-2 data
without extra conditioning information, we can conclude the following:

Early Sugar Beet Yield Prediction using Satellite Data 11
0 200 400 600 800 1000 1200
Forward-pass GFLOPS
20.0
20.5
21.0
21.5
22.0
Test RMSE
T rain set mean
Linear VI Regression
ResNet-50
ResNet-18SqueezeNet
ViT/8-1h-64d
ViT/32-1h-64d
ViT/16-1h-64d
ViT/4-1h-64d
ViT/2-1h-64d
ViT/1-1h-64d
ViT/2-1h-64d
ViT/2-2h-64d
ViT/2-4h-64d
ViT/2-8h-64d
ViT/2-16h-64d
ViT/2-1h-128d
ViT/2-2h-128d
ViT/2-4h-128d
ViT/2-8h-128d
ViT/2-16h-128d ViT/2-1h-192d
ViT/2-2h-192d
ViT/2-4h-192d
ViT/2-8h-192d
ViT/2-16h-192d
ViT/2-1h-64d-B10
ViT/2-1h-64d-B4
ViT/2-1h-64d-NDVI+EVI+MSI
ViT/2-1h-64d-RGB
ViT/2-1h-64d-NDVI
ViT/2-1h-64d-EVI
ViT/2-1h-64d-MSI
Architecture
-
CNN
ViT
Pareto front
Fig.2: Compute requirements vs test set performance of multiple baselines and
various vision transformer design choices on the sugar beet yield prediction task.
–Incorporating domain knowledge into the model selection can lead to syn-
ergies. Our task requires fine-grained details between parts of the field, for
which the transformer model operating over field patches performed the best.
–Thereceptivefieldofthemodelneedstobespecifictothetask.Asthespatial
resolution of our data at 10 m includes many plants, further compressing the
information through larger patch sizes is detrimental to performance.
–End-to-end feature extraction should be explored alongside domain-specific
input channel configurations. We have seen on our task that feature extrac-
tion on all bands outperforms band subsets or combinations. While this may
have been due to the specific data setup and task, experiments on the full
band spectrum can provide valuable insights for future model developments.
4 Model Application
For the final section, we put our model to use and predict the yield before the
harvestthroughtemporalencodings(section4.1)andfindunderperformingfields
through a ranking-based metric (section 4.2). We use the simple ViT/2-1h-64d
model to keep compute requirements modest and to avoid overfitting when in-
troducing additional temporal parameters. We first expand the training to all
time steps leading up to the harvest, not just the last one as in the previous
experiments. For the model training, we randomly sample one of the available
temporal instances for each field per mini-batch and predict the harvest yield
at the end of the growth cycle. It is important to note that the model still only
receives a single temporal instance for a prediction. With the added temporal in-
stances before the harvest to the training set and corresponding time encodings,

12 Vaeth et al.
the model can additionally learn how fields look like during the growth cycle
given the yield after the harvest. The satellite images for a field at different time
steps can be vastly different depending on the growth cycle. We evaluate mul-
tiple encoding strategies in section 4.1 to assess the influence of time encodings
on the ability of the model to learn time-aware features for the early prediction.
In our very restrictive setup, estimating the magnitude of yield purely based
on a single optical satellite image is challenging by design (R2 = 0.137for the
best model on the test data). However, we hypothesize that the model may have
learned to rank fields based on the harvest yield as it still outperforms simple
baselines and does capture some variance of the test labels. In this scenario, the
correct magnitude is not important as long as the relative order of the yield
predictions is correct. We therefore use the model for the detection of low-yield
fields early on in the growth cycle in section 4.2.
4.1 Early yield prediction through time encodings
The results for different time encoding strategies are displayed in figure 3. We
test no temporal encoding (red line), a learned temporal encoding (yellow line)
and a fixed sinusoidal temporal encoding (blue line), which is added to each
temporal instance before passing it to the transformer layer. For the learned
temporal encodings, almost no additional parameters are added to the model as
there are only 26 distinct time steps in the growth cycle. To evaluate the model,
we iterate over the time steps and select all fields which have a temporal instance
at that time step. We only show predictions for time steps with a large enough
sample size, where at least 20% of the fields have a valid temporal instance.
The results in figure 3 show the performance of different temporal encoding
strategies over different time steps in the growth cycle on the top (red, blue,
yellow line). The corresponding sample sizes are shown on the bottom (green
line). We can see that the sinusoidal time encoding consistently improves per-
formance. Despite filtering time steps with low sample size, the results still show
high variance across the growth cycle, especially for the test set. We hypothesize
this is due to an inconsistent amount of temporal instances per time step during
training. Furthermore, as the test set was recorded in 2024, whereas the training
data was from 2019, the dates do not perfectly align and differences in weather
conditions lead to a different distribution of valid temporal instances across the
time steps. The "day 0" also differs between years as the growth seasons did not
start at exactly the same time. However, the low error very early in the growth
cycle (day 30 on the validation set and day 40 on the test set) indicates that
early prediction is possible and interesting for future work.
4.2 Early detection of underperforming fields
For the final experiment, we will only use the harvest yield as a proxy metric to
find underperforming fields through our model. First, we defineunderperforming
fieldsas the fields in the lower quartile of harvest yield. As the harvest yield is

Early Sugar Beet Yield Prediction using Satellite Data 13
0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130
Days since beginning of growth cycle (2019 validation set)
14
15
16
17
18
19
20Validation RMSE
No time encoding Learned time encoding Sinusoidal time encoding T raining set mean prediction
0.0
0.5
1.0
Samples (thousands)
0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130
Days since beginning of growth cycle (2024 test set)
10
12
14
16
18
20
22
24Test RMSE
No time encoding Learned time encoding Sinusoidal time encoding T raining set mean prediction
0.0
2.5
5.0
Samples (thousands)
Fig.3: Early detection performance for the single layer single head ViT/2 model
and different time step encodings for the validation set (top) and the test set
(bottom). The amount of valid instances is displayed in green for each data set.
given in tons per hectare, so already normalized by the area of each field, the
differences in yield should be independent of the field size.
In our experiment, we predict the yield for all available temporal instances
for the validation and test set at multiple time steps, similarly as in the previ-
ous section 4.1. We then rank the fields by harvest yield, compare the lowest
quartile of predicted fields to the underperforming fields based on the ground-
truth labels, and report the percentage of fields in both sets. As 25% of fields
are underperforming based on this definition and the ground-truth harvest yield,
a random prediction of underperforming fields should identify a quarter of the
real underperforming fields, or 6.25%, indicated by the dotted line in figure 4.
Classifying all fields as underperforming would lead to a 25% detection rate,
shown as a dashed line in figure 4. Note that we only select the time steps where
there are a lot of fields with a valid temporal instance for both validation and
test sets, such that the quantity of predictions is comparable to the amount of
ground-truth underperforming fields. However, not every underperforming field
necessarily has a valid temporal instance at each selected time step, which can
reduce the observed detection rate.
Despite this strong data limitation, the results in figure 4 show that almost
50% of underperforming fields were already found one third of the way into the
growth cycle. In practice, this could be used to alert farmers that their field is
underperforming way before the harvest when interventions are still possible.
Surprisingly, this was possible through purely optical data. Integrating more
sources of information and further developing the approach will be subject to
future work.

14 Vaeth et al.
10 30 45 95 105 110 115
Days since beginning of growth cycle
0
10
20
30
40
50
60
underperforming ﬁeld detection (%)
V alidation (2019) T est (2024) Random prediction All underperforming prediction
Fig.4: Detection percentage of the fields in the lowest quartile of harvest yield
across time steps by the ViT/2-1h-64d model with sinusoidal time encodings.
5 Conclusion
Applying machine learning methods to real-world tasks is non-trivial. Practi-
tioners must balance generic deep neural network architectures against domain-
specific pre-processing steps, such as band selection, that can both constrain and
enhance model performance. This paper should provide a real-world example of
this trade-off. We showed that modeling choices driven by domain knowledge
can lead to synergistic effects and even surprising results. Our experiments show
that small input patches lead to consistently better performance, which contrasts
with most previous, predominantly convolution-based work that relies on pro-
gressively larger receptive fields. We also find that using all Sentinel-2 spectral
bands, without extensive pre-processing or custom band combinations, is benefi-
cial - another uncommon design choice in the field. The goal of the paper was not
to provide a new prediction system that outperforms previous approaches, but
instead highlight the marginal improvements of key design choices as insights
for future practitioners. Despite the limited direct practical use of our absolute
yield predictions, the study allowed us to systematically question critical de-
sign choices and demonstrate performance improvements grounded in domain
knowledge. An important promising result of our study is the ability for the
same models to detect underperforming fields well before the harvest when com-
bined with an appropriate training setup and a ranking-based detection. Our
study is limited by the small dataset size, the focus on specific years, a sin-
gle geographical region, one crop type, and one satellite mission. Future work
will verify these findings in broader settings; a more detailed discussion of the
limitations is provided at the end of section 2.
References
1. Brown, C.F., Kazmierski, M.R., Pasquarella, V.J., Rucklidge, W.J., Samsikova, M.,
Zhang, C., Shelhamer, E., Lahera, E., Wiles, O., Ilyushchenko, S., Gorelick, N.,
Zhang, L.L., Alj, S., Schechter, E., Askay, S., Guinan, O., Moore, R., Boukouvalas,
A., Kohli, P.: Alphaearth foundations: An embedding field model for accurate and
efficient global mapping from sparse label data. arXiv:2507.22291 (2025)

Early Sugar Beet Yield Prediction using Satellite Data 15
2. Chen, J., Liu, J., Xia, Z., Su, W., Huang, J., Wang, P., Li, Y.: Coupling of weather
generator and crop model for enhanced low-temperature stress sample augmenta-
tion in henan province, pr china. COMPAG (2024)
3. Cong, Y., Khanna, S., Meng, C., Liu, P., Rozi, E., He, Y., Burke, M., Lobell, D.B.,
Ermon, S.: SatMAE: Pre-training transformers for temporal and multi-spectral
satellite imagery. NeurIPS (2022)
4. Copernicus Sentinel-2, E.S.A.: Msi level-2a boa reflectance product. collection 1.
European Space Agency (2021),https://doi.org/10.5270/S2_-znk9xsj
5. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner,
T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., et al.: An image is worth
16x16 words: Transformers for image recognition at scale. ICLR (2021)
6. He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition.
CVPR (2016)
7. Hong, D., Zhang, B., Li, X., Li, Y., Li, C., Yao, J., Yokoya, N., Li, H., Ghamisi,
P., Jia, X., et al.: Spectralgpt: Spectral remote sensing foundation model. IEEE
PAMI (2024)
8. Iandola, F.N., Moskewicz, M.W., Ashraf, K., Han, S., Dally, W.J., Keutzer, K.:
Squeezenet: Alexnet-level accuracy with 50x fewer parameters and<1mb model
size. arXiv:1602.07360 (2016)
9. Jakubik, J., Yang, F., Blumenstiel, B., Scheurer, E., Sedona, R., Maurogiovanni,
S., Bosmans, J., Dionelis, N., Marsocci, V., Kopp, N., Ramachandran, R., Fraccaro,
P., Brunschwiler, T., Cavallaro, G., Bernabe-Moreno, J., Longépé, N.: Terramind:
Large-scale generative multimodality for earth observation. ICCV (2025)
10. Jeong, S., Ko, J., Yeom, J.M.: Predicting rice yield at pixel scale through synthetic
use of crop and deep learning models with satellite data in south and north korea.
Sci. Total Environ. (2022)
11. Jiang, H., Hu, H., Zhong, R., Xu, J., Xu, J., Huang, J., Wang, S., Ying, Y., Lin,
T.: A deep learning approach to conflating heterogeneous geospatial data for corn
yield estimation: A case study of the us corn belt at the county level. GCB (2020)
12. Joshi, A., Pradhan, B., Gite, S., Chakraborty, S.: Remote-sensing data and deep-
learning techniques in crop mapping and yield prediction: A systematic review.
Remote Sens. (2023)
13. Kaur, A., Goyal, P., Rajhans, R., Agarwal, L., Goyal, N.: Fusion of multivariate
time series meteorological and static soil data for multistage crop yield prediction
using multi-head self attention network. Expert Syst. Appl. (2023)
14. Li, X., Geng, H., Zhang, L., Peng, S., Xin, Q., Huang, J., Li, X., Liu, S., Wang, Y.:
Improving maize yield prediction at the county level from 2002 to 2015 in china
using a novel deep learning approach. COMPAG (2022)
15. Li, Z., Xuan, F., Dong, Y., Huang, X., Liu, H., Zeng, Y., Su, W., Huang, J., Li, X.:
Performance of gedi data combined with sentinel-2 images for automatic labelling
of wall-to-wall corn mapping. Int. J. Appl. Earth Obs. Geoinf. (2024)
16. Liu, F., Jiang, X., Wu, Z.: Attention mechanism-combined lstm for grain yield
prediction in china using multi-source satellite imagery. Sustainability (2023)
17. Lu, J., Li, J., Fu, H., Tang, X., Liu, Z., Chen, H., Sun, Y., Ning, X.: Deep learning
for multi-source data-driven crop yield prediction in northeast china. Agriculture
(2024)
18. Maimaitijiang, M., Sagan, V., Sidike, P., Hartling, S., Esposito, F., Fritschi, F.B.:
Soybean yield prediction from uav using multimodal data fusion and deep learning.
Remote Sens. Environ. (2020)
19. Mathivanan, S.K., Jayagopal, P.: Utilizing satellite and uav data for crop yield
prediction and monitoring through deep learning. Acta Geophys. (2022)

16 Vaeth et al.
20. Radočaj, D., Jurišić, M., Plaščak, I., Galić, L.: Satellite remote sensing for crop
yield prediction: A review. Agriculture (2026)
21. Sadbhave, B.L., Vaeth, P., Dejon, D., Schorcht, G., Gregorová, M.: Sugar-beet
stress detection using satellite image time series. ICPRAM (2025)
22. Schwalbert, R.A., Amado, T., Corassa, G., Pott, L.P., Prasad, P.V., Ciampitti,
I.A.: Satellite-based soybean yield forecast: Integrating machine learning and
weather data for improving crop yield prediction in southern brazil. Agric. For.
Meteorol. (2020)
23. Siméoni, O., Vo, H.V., Seitzer, M., Baldassarre, F., Oquab, M., Jose, C., Khalidov,
V., Szafraniec, M., Yi, S., Ramamonjisoa, M., et al.: Dinov3. arXiv:2508.10104
(2025)
24. Song, J., Huang, J., Huang, H., Xiao, G., Li, X., Li, L., Su, W., Wu, W., Yang, P.,
Liang, S.: Improving crop yield estimation by unified model parameters and state
variable with bayesian inference. Agric. For. Meteorol. (2024)
25. Tao, W., Xie, Z., Zhang, Y., Li, J., Xuan, F., Huang, J., Li, X., Su, W., Yin, D.:
Corn residue covered area mapping with a deep learning method using chinese gf-1
b/d high resolution remote sensing images. Remote Sens. (2021)
26. Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,Kaiser,
Ł., Polosukhin, I.: Attention is all you need. NeurIPS (2017)
27. Victor, B., Nibali, A., He, Z.: A systematic review of the use of deep learning in
satellite imagery for agriculture. IEEE JSTARS (2025)
28. Wang, X., Huang, J., Feng, Q., Yin, D.: Winter wheat yield prediction at county
level and uncertainty analysis in main wheat-producing regions of china with deep
learning approaches. Remote Sens. (2020)
29. Xiao, G., Huang, J., Zhuo, W., Huang, H., Song, J., Du, K., Wang, J., Yuan, W.,
Sun, L., Zeng, Y., et al.: Progress and perspectives of crop yield forecasting with
remote sensing: A review. IEEE GRSS (2025)
30. Xiao, G., Zhang, X., Niu, Q., Li, X., Li, X., Zhong, L., Huang, J.: Winter wheat
yield estimation at the field scale using sentinel-2 data and deep learning. COM-
PAG (2024)
31. Xie, Y., Huang, J.: Integration of a crop growth model and deep learning methods
to improve satellite-based yield estimation of winter wheat in henan province,
china. Remote Sens. (2021)
32. Yang, W., Nigon, T., Hao, Z., Dias Paiao, G., Fernández, F.G., Mulla, D., Yang,
C.: Estimation of corn yield based on hyperspectral imagery and convolutional
neural network. Comput. Electron. Agric. (2021)
33. Zhuo, W., Huang, H., Gao, X., Li, X., Huang, J.: An improved approach of winter
wheat yield estimation by jointly assimilating remotely sensed leaf area index and
soil moisture into the wofost model. Remote Sens. (2023)
