---
title: Physics-Based Deep Spatiotemporal Hyperlocal Radar Nowcasting with a Multi-Variable U-Net for High-Resolution
  Precipitation Forecasting
url: https://arxiv.org/abs/2607.16080
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Akshay Sunil
- Muhammed Rashid
- Raja Sekhar Sivaraju
- Sushma Nair
- Subimal Ghosh
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.16080
pages: 10
chars: 47454
fetched_at: '2026-11-08T13:28:05+00:00'
kb_version: 1
---

# Physics-Based Deep Spatiotemporal Hyperlocal Radar Nowcasting with a Multi-Variable U-Net for High-Resolution Precipitation Forecasting

1
Physics-Based Deep Spatiotemporal Hyperlocal
Radar Nowcasting with a Multi-Variable U-Net for
High-Resolution Precipitation Forecasting
Akshay Sunil, Muhammed Rashid, Raja Sekhar Sivaraju, Sushma Nair, and Subimal Ghosh
Abstract—Precipitation nowcasting over the immediate 10-
90 min period is important for flood management and real-
time decision-making in urban regions. Conventional short-range
forecasting with high-resolution numerical weather prediction
requires frequent data assimilation, model initialization, and
spin-up, introducing computational latency that limits rapid
operational guidance. Machine learning provides an alternative
by learning storm evolution directly from high-frequency ob-
servations and producing forecasts quickly after training. This
is particularly relevant for Mumbai, India, where monsoon
convection, land-sea interactions, and localized intense rainfall
make short-term prediction difficult. Here, we develop a compact
radar-only nowcasting framework that combines multi-elevation
reflectivity, Doppler radial velocity, and radial-velocity-gradient
proxy features within an encoder-decoder U-Net. Using the most
recent radar volume scan, the model predicts 12 future composite
reflectivity fields at 7.5-min intervals up to 90 min lead time.
The derived velocity magnitude, divergence-like, directional-
shear, and vorticity-like channels represent kinematic signatures
associated with convergence and boundary interactions without
requiring full wind-field retrieval. A high-reflectivity attention
module is used to improve sensitivity to convective cores, and
physics-guided attribution to examine whether the learned sen-
sitivities are meteorologically meaningful. The model is trained
using Mumbai Doppler radar observations from May to August
2023 and evaluated on temporally independent events. At 90
min lead time, Critical Success Index values are 0.437, 0.332,
and 0.193 for≥10,≥20, and≥30 dBZ thresholds, respectively.
Compared with persistence, the model gives lower RMSE and
higher spatial correlation at longer lead times. Once trained, it
runs on a standard computer, generating nowcasts within seconds
for real-time use.
Index Terms—Nowcasting, Machine Learning, Radar-based
Forecasting, Spatio-temporal U-Net, Feature Attribution.
I. INTRODUCTION
A
CCURATE precipitation prediction is fundamental for
reducing weather-related risks in cities, particularly for
flood management, aviation operations, emergency response,
and transport planning. Within this broader prediction prob-
lem, nowcasting focuses on the immediate few minutes to
hours ahead, typically up to about 0-90 min, when rainfall sys-
tems can evolve rapidly and decisions must be made with min-
imal lead time [1], [2]. This window is especially important for
Akshay Sunil, Subimal Ghosh, and Muhammed Rashid are with the
Centre for Climate Studies, Indian Institute of Technology Bombay, Mumbai,
India (e-mail: akshaysunil172@gmail.com; subimal@iitb.ac.in; muhamme-
drashid.edu@gmail.com).
Raja Sekhar Sivaraju and Sushma Nair are with the Regional
Meteorological Centre (RMC) in Colaba, Mumbai, India (e-mail:
sivaraju.rajasekhar@gmail.com;sushma.nair@imd.gov.in).
short-duration, high-intensity rainfall spells, which can trigger
flash flooding in densely built urban catchments within less
than an hour. In coastal megacities such as Mumbai, rapidly
evolving monsoon convection, land-sea interactions, and local-
ized cloudbursts can overwhelm stormwater drainage, inundate
low-lying roads and underpasses, disrupt transport, and affect
aviation operations. The extreme rainfall event of 26 July 2005
in Mumbai underscored the need for neighbourhood-scale
nowcast guidance on where intense convective cells are likely
to initiate, intensify, and move over the next one to two hours
[3]. In addition, extreme rainfall over Mumbai exhibits strong
intra-urban spatial variability, with earlier work showing that
urban-induced intensification can occur in localized pockets
and that rainfall correlations between stations may become
statistically insignificant beyond distances of about 10 km
[4]. Producing such guidance using radar-assimilated regional
numerical models remains operationally challenging because
frequent data assimilation, initialization, and model spin-up
must be completed within a short decision window. A fast
radar-based machine-learning framework therefore offers a
practical route for generating localized nowcasts with the
latency required for real-time urban response.
At nowcast horizons, numerical weather prediction (NWP)
faces structural limitations: kilometre-scale convection is
highly sensitive to initial-condition errors and model spin-
up, while microphysics and boundary-layer parameterizations
introduce biases. In addition, data assimilation and I/O latency
can exceed decision windows for fast-evolving storms [5].
Even convection-allowing models can improve storm morphol-
ogy yet still exhibit substantial timing and placement errors
for convective initiation at 0-3 h lead times [6]. Weather
radar remains the backbone of operational nowcasting be-
cause it provides high-resolution, near-real-time depictions of
storm structure and motion. Classical radar-based approaches,
including Tracking Radar Echoes by Correlation [7] and
optical-flow extrapolation [8], estimate a motion field and
advect reflectivity forward under a Lagrangian persistence
assumption. While computationally efficient and skilful at very
short lead times, these techniques degrade rapidly beyond 30-
60 min because they cannot represent convective initiation,
growth, or decay [1]. Probabilistic ensemble schemes such
as STEPS merge extrapolation with stochastic perturbations
and downscaled NWP to quantify uncertainty, but they remain
constrained by persistence [9].
Open-source libraries such as pysteps have standardized
probabilistic extrapolation, verification, and benchmarking for
arXiv:2607.16080v1  [cs.LG]  17 Jul 2026

2
radar nowcasting [2]. Recent probabilistic and generative ap-
proaches, including DGMR, produce sharper ensembles with
improved spatial structure and categorical skill relative to
traditional extrapolation methods [10], [11].
Recent advances in deep learning have shifted radar now-
casting from extrapolation-based methods toward data-driven
spatiotemporal prediction. Early models such as ConvLSTM
demonstrated improved skill by jointly learning spatial and
temporal evolution [12], while encoder-decoder architectures
such as U-Net preserved fine-scale morphology through mul-
tiscale representations and skip connections [13]. Subsequent
developments, including TrajGRU, PredRNN, attention-based
encoder-forecasters, and large-context models such as MetNet
and MetNet-2, further improved storm evolution, temporal
coherence, and forecast skill across extended lead times [14]–
[17].
More recently, physics-informed nowcasting frameworks
have incorporated continuity constraints, transport-aware evo-
lution, and conservation principles to improve long-lead sta-
bility, probabilistic calibration, and representation of con-
vective evolution. Representative examples include Nowcast-
Net, LUPIN, and ClimODE, which integrate physical con-
straints through complementary deterministic, stochastic, or
continuous-time formulations [18]–[20]. Collectively, these
studies demonstrate the benefits of embedding physical con-
sistency within deep-learning nowcasting systems.
Current radar nowcasting frameworks often rely on reflec-
tivity alone and miss the kinematic signatures of convergence,
shear, and boundary interactions that precede convective
growth. Also, existing deep learning models frequently lack
scientific interpretability, which limits operational trust. To
address these gaps, in this study, we develop a radar-only deep
learning nowcasting framework tailored to Mumbai’s monsoon
convection. We construct multi-elevation, multi-variable input
tensors that combine reflectivity, Doppler radial velocity, and
physically motivated proxy predictors derived from spatial
gradients of radial velocity. In contrast to reflectivity-only
encoder-decoder baselines, this design injects dynamically
informative cues into the learned representation while avoiding
the need for full wind retrieval from single-Doppler mea-
surements. The forecasting core is an encoder-decoder U-Net
that maps the most recent radar volume scan to a 12-step
composite-reflectivity forecast sequence at 7.5-min intervals
(up to 90 min). To improve scientific interpretability and
operational trust, we additionally apply physics-guided feature
attribution to assess whether learned sensitivities concentrate
on meteorologically meaningful precursor structures, such as
boundary signatures and convergence-like patterns.
In the present analysis, our goal is to develop a radar-based
nowcasting framework for Mumbai using a machine learning
approach. The proposed method is computationally efficient,
requires minimal processing effort, and can be rapidly updated
with each new radar scan generated every 7.5 minutes, offering
strong potential for real-time applications. Building on this
framework, we address four key objectives: (i) to demonstrate
that multi-elevation, multi-variable inputs improve skill rel-
ative to reflectivity-only baselines across standard thresholds
and lead times; (ii) to evaluate whether radial-velocity-gradient
proxy features improve representation of convective growth
and moderate-to-heavy echoes; (iii) to show that attribution
maps provide meteorologically consistent explanations that are
useful for practitioners; and (iv) to verify that the gains are
robust across temporally disjoint events and feasible within a
7.5-min operational update cycle.
II. METHODS
This section details the end-to-end methodology under-
pinning the radar-based nowcasting system. We first con-
struct physics-aware inputs by transforming multi-elevation
Doppler radar measurements into multi-channel tensors, in-
cluding reflectivity, radial velocity, and radial-velocity-gradient
kinematic proxy fields, and we define multi-step composite-
reflectivity targets at fixed lead times. We then describe a
feed-forward U-Net that maps the most recent multi-elevation
radar volume scan to a sequence of future reflectivity fields,
augmented with a high-reflectivity attention mechanism to
emphasize convective cores. The learning objective combines
intensity-weighted reconstruction with structural similarity and
threshold-aware terms to align training with both spatial real-
ism and exceedances skill at operational reflectivity thresholds.
We conclude with data preparation, channel-wise normaliza-
tion, and temporally disjoint training/validation/test splits.
A. Radar data & preprocessing
Radar data for this study are sourced from the Doppler
weather radar operated by the India Meteorological Depart-
ment (IMD) at the Veravali site near Mumbai (≈19.1° N, 72.9°
E). The C-band volume-scan radar typically performs 10 ele-
vation sweeps per volume, providing reflectivity and Doppler
radial-velocity measurements over the Mumbai metropolitan
region and adjacent coastal/offshore areas. IMD surveillance
extends to roughly 400-450 km; however, beam broadening,
attenuation, and increasing sampling volume degrade effective
resolution with distance. Accordingly, echoes within 250 km
are retained and mapped to a1 km×1 kmCartesian grid.
Preprocessing follows a standard pipeline for converting
polar radar volumes into quality-controlled Cartesian products
suitable for deep learning. Reflectivity and radial-velocity
fields undergo quality control, including ground-clutter and
anomalous-propagation suppression, masking of low signal-to-
noise gates, and radial-velocity dealiasing using IMD opera-
tional procedures. Data at each elevation are then interpolated
from polar coordinates onto a Cartesian grid using bilinear
interpolation at 1 km spacing in both x and y, yielding a 501
x 501 domain (≈500 km×500 km); scans with incomplete
azimuthal coverage or severe artefacts are discarded [2], [11],
[21]. Reflectivity is clipped to a physically plausible range
(e.g., -5 to 55 dBZ) to limit outliers, while radial velocity is
scaled to a fixed interval prior to feature derivation. For model
input, each 2-D Cartesian field is resampled to128×128
to match the network resolution [22]. Finally, volume scans
are aligned to a regular 7.5-min temporal grid via linear
interpolation in time, and sequences with gaps exceeding one
scan interval are excluded from training and evaluation.

3
B. Physics-Aware Feature Engineering
The forecasting framework employs physics-aware fea-
ture engineering to incorporate kinematic information from
Doppler radar observations. This is motivated by theoretical
and observational evidence that low-level convergence, shear,
and rotation influence convective initiation, organization, and
storm evolution [23]–[25]. For each radar elevation, six input
channels are derived: horizontal reflectivity Z, radial velocity
Vr, radial-velocity magnitude|V r|, a divergence-like radial-
velocity-gradient proxyS, a directional shear proxyθ, and a
vorticity-like proxyω.
Xe = [Ze, Vr,e,|V r,e|, Se, θe, ωe].(1)
whereX e denotes the multi-channel input tensor for elevation
e. The radial-velocity magnitude is defined as
|Vr,e|=
q
V 2r,e +V 2 θ,e,(2)
whereV θ,e is the tangential velocity component at elevation
e.
The divergence-like radial-velocity-gradient proxy is com-
puted as
Se = ∂Vr,e ∂x + ∂Vr,e ∂y .(3)
The directional shear proxy is defined as
θe = 1 π atan2  ∂Vr,e ∂y , ∂Vr,e ∂x  .(4)
which represents the orientation of the local radial-velocity
gradient normalized to [-1,1]. The vorticity-like radial-
velocity-gradient proxy is computed as
ωe = ∂Vr,e ∂y − ∂Vr,e ∂x .(5)
Spatial gradients are estimated on the Cartesian radar grid
using central differences:
∂Vr,e
∂x

i,j
= Vr,e(i, j+ 1)−V r,e(i, j−1) 2∆x .(6)
∂Vr,e
∂y

i,j
= Vr,e(i+ 1, j)−V r,e(i−1, j) 2∆y .(7)
where∆xand∆yare the Cartesian grid spacing. Where
necessary, a light smoothing filter is applied toV r before
differencing to reduce noise amplification.
Together, these channels provide a compact representation
of reflectivity structure and radial-velocity-derived kinematic
signatures associated with convergence, divergence, shear, and
rotation, all of which are relevant to convective initiation and
storm growth. The six channels are constructed independently
for each radar elevation and then stacked acrossN eleveleva-
tion angles, giving a total input depth of6N elev. The resulting
multi-elevation tensor is resampled to a128×128spatial grid
before being supplied to the network. The prediction targets
are column-maximum reflectivity fields at 12 future lead times,
sampled every 7.5 min and extending to a maximum lead time
of 90 min.
C. Network Architecture
The forecasting model is a feed-forward spatio-temporal
U-Net, designed to predict the full reflectivity evolution se-
quence from a single input time slice. This architecture is
chosen for its ability to simultaneously handle the spatial
complexity of storm structures and the temporal evolution of
convective systems, which is crucial for accurate short-term
precipitation nowcasting. The encoder-decoder backbone con-
sists of convolution-batch normalization-LeakyReLU blocks,
with two downsampling stages to capture multi-scale spatial
features and bilinear upsampling in the decoder to reconstruct
high-resolution predictions. Skip connections are employed
to preserve high-frequency storm structures across scales,
which ensures that fine-grained details (such as the edges of
convective cells) are maintained throughout the network.
We developed a U-Net-based encoder-decoder model to
forecast short-term radar reflectivity. The network ingests the
most recent128×128gridded fields at timet 0 of radar
reflectivity (dBZ) and Doppler radial velocity (m s−1) sampled
at the native radar scan cadence (≈7min). To enrich
the dynamical information available to the model, additional
kinematic predictors are computed from the radial-velocity
fields and concatenated with the raw inputs prior to encoding,
including velocity magnitude|v|, a divergence-like gradient
proxy∂v/∂y, and a direction proxy derived from the gradient
orientation defined byatan2(∂v/∂y, ∂v/∂x)/π.
The encoder comprises two convolutional stages with3×3
kernels and increasing channel depth (64 and 128). Each
stage is followed by batch normalization and LeakyReLU
activation, and max pooling is used for spatial downsampling.
A 256-channel bottleneck layer captures compact, high-level
representations of the input fields. The decoder reconstructs
full resolution using bilinear upsampling followed by3×3
convolutions, and integrates skip connections from the cor-
responding encoder stages to preserve fine-scale spatial struc-
ture. A final1×1convolution produces the forecast sequence,
yielding 12 future reflectivity frames (≈90min lead time at
scan-time intervals).
To emphasize intense precipitation regions that are most
relevant for convective nowcasting, we incorporate a high-
reflectivity attention (HRA) module at the bottleneck and
after the final decoding stage. Given a reflectivity feature
representation, the attention mapAis computed using global
spatial pooling followed by a two-layer gating function:
A=σ

W2 ReLU(W1 ¯Z)  .(8)
where ¯Zis the spatially averaged reflectivity feature map,
W1 andW 2 are trainable parameters implemented as fully
connected layers or equivalently1×1convolutions, andσ
denotes the sigmoid activation. The attended feature tensor is
then obtained through residual reweighting:
ˆF=F⊙(1 +αA)(9)
where F is the input feature tensor,⊙denotes element-wise
multiplication, andαcontrols the strength of attention-based
amplification. In this study,αis set to 1.2. By selectively

4
Fig. 1. U-Net architecture for radar-based weather nowcasting. Multi-elevation radar reflectivity and Doppler radial-velocity fields from the most recent
volume scan (≈7min scan cadence) are provided as input and augmented through feature engineering to derive kinematic descriptors, including velocity
magnitude, divergence, direction, and vorticity. The network employs a two-level encoder-decoder structure with skip connections to preserve multiscale spatial
information, while a bottleneck layer captures compact representations. During decoding, bilinear upsampling and feature concatenation progressively restore
spatial resolution. A high-reflectivity attention module is applied after the final decoding stage to emphasize regions associated with intense precipitation. The
model outputs T future reflectivity frames corresponding to a 90-min forecast horizon at approximately scan-time (≈7min) intervals.
amplifying features associated with high reflectivity, the HRA
mechanism increases the network’s sensitivity to convective
cores and improves the reconstruction and prediction of rapidly
evolving storm structures.
D. Loss Functions
Training minimizes a composite objective that balances
amplitude fidelity, spatial structure, and operational skill at
precipitation thresholds:
L=λ iwLiwMSE +λ SSIM(1−SSIM) +λ thrLthr.(10)
where SSIM denotes the Structural Similarity Index Mea-
sure, which quantifies the similarity between predicted and
observed reflectivity fields in terms of luminance, contrast,
and structural consistency. This formulation combines an
amplitude-focused reconstruction term, a structural similarity
term, and a threshold-aware term, so that training is aligned
with both pixel-wise accuracy and operational verification
metrics. The weighting coefficientsλ iw,λ SSIM, andλ thr are
chosen such that no single component dominates the gradient,
yielding forecasts that retain realistic storm morphology while
maintaining skill at application-relevant reflectivity thresholds.
Through the reflectivity-dependent weighting inL iwMSE, the
loss places larger penalties on errors in moderate and high
reflectivity regions (≥25–35 dBZ), so the optimizer concen-
trates capacity on convective cells and heavy rain rather than
weak, low-impact echoes.
To emphasize convective echoes, the reconstruction error is
weighted by reflectivity in dBZ. The weights are computed in
physical reflectivity space, while the errors are evaluated in the
model’s normalized space for numerical stability. LetZ t(x, y)
and ˆZt(x, y)denote the observed and predicted reflectivity
fields at lead timet= 1, . . . , T. The reflectivity-aware weight
is defined as
w(Z) =



α0, Z <15 dBZ,
α1,15≤Z <25 dBZ,
α2,25≤Z <35 dBZ,
α3, Z≥35 dBZ
(11)
with
α={1.0,1.3,1.8,2.5}.

5
The intensity-weighted mean squared error is then computed
over all forecast lead times and spatial grid points as
LiwMSE = 1 T HW
TX
t=1
WX
x=1
HX
y=1
w

Z dBZ t (x, y) 
×

ˆZ norm t (x, y)−Z norm t (x, y) 2 . (12)
where “dBZ” and “norm” denote the physical and normal-
ized domains, respectively. The affine normalization is inverted
only for computing the reflectivity-dependent weightw(·).
E. Training Configuration
Training data are drawn from Doppler radar observations
collected over Mumbai between May and August 2023, with
an 80–10–10 split for training, validation, and testing. Input
variables are standardized by channel to ensure consistent
scaling across the dataset. During training, data augmentation
techniques such as random cropping and horizontal flipping
are applied to increase model robustness to spatial variability.
The model is trained using the Adam optimizer (learning rate
1×10 −4) with early stopping based on validation SSIM to
prevent overfitting. Additionally, a learning rate scheduler is
used to adjust the learning rate during training to enhance
convergence and optimize training efficiency. The model runs
on an NVIDIA GPU (CUDA-enabled) with a batch size of 8
and generates reflectivity predictions every 7.5 min up to 90
min ahead. Validation performance is continuously monitored
using metrics such as SSIM and the Critical Success Index
(CSI), ensuring that the model not only fits well but also
generalizes effectively. Test data, withheld from training and
validation, are used to assess the model’s ability to generalize
to unseen radar scans and to evaluate performance on a real-
world test set.
F . Evaluation metrics
Model performance was assessed using both categorical and
continuous verification metrics. Categorical skill was evaluated
at reflectivity thresholds of≥10,≥20, and≥30dBZ
using the Critical Success Index (CSI), Equitable Threat Score
(ETS), frequency bias, Probability of Detection (POD), False
Alarm Ratio (FAR), and False Positive Rate (FPR). LetH,
M,F, andCNdenote hits, misses, false alarms, and correct
negatives, respectively. These metrics are defined as
CSI = H H+M+F (13)
ETS = H−H r
H+M+F−H r
(14)
Hr = (H+M)(H+F) H+M+F+CN (15)
Bias = H+F H+M (16)
POD = H H+M (17)
F AR = F H+F (18)
FPR = F F+CN (19)
Continuous performance was evaluated using the domain-
averaged root-mean-square error (RMSE) and spatial correla-
tion of composite reflectivity:
RMSE =
vuut 1
N
NX
i=1
(Pi −O i)2 (20)
r=
PN
i=1(Pi − ¯P)(O i − ¯O)qPN
i=1(Pi − ¯P) 2
qPN
i=1(Oi − ¯O)2
(21)
whereP i andO i denote predicted and observed reflectivity
values at grid pointi, respectively; ¯Pand ¯Oare their spatial
means; andNis the total number of grid cells. To assess
scale-dependent structural realism, radially averaged power
spectral density (PSD) was compared between forecasts and
observations at selected lead times. Observed event support
was also reported to provide context on threshold-dependent
sample prevalence.
III. RESULTS
This section reports the evaluation of the proposed radar
nowcasting framework on an independent test set. We sum-
marize performance across reflectivity thresholds using cate-
gorical and continuous verification metrics, examine how skill
changes with lead time relative to a persistence baseline, and
assess scale dependent structure using spectral and neigh-
bourhood verification. Representative case diagnostics are also
provided to illustrate dominant error modes.
A. Overall nowcasting performance and intensity dependence
The spatiotemporal U-Net was evaluated on an independent
test dataset using standard categorical and continuous verifica-
tion metrics across reflectivity thresholds of≥10,≥20, and
≥30 dBZ. Unless otherwise noted, reported values are ag-
gregated across all 12 forecast steps (7.5-90 min). The model
shows strongest skill for weaker and moderate echoes, with
performance gradually decreasing as the reflectivity threshold
increases, consistent with the greater difficulty of predicting
compact and rapidly evolving convective cores. Across thresh-
olds, the model maintains useful categorical skill while false-
alarm behaviour remains controlled, indicating good discrimi-
nation between precipitating and non-precipitating regions de-
spite pronounced class imbalance. Overall, the results indicate
robust performance for weak-to-moderate precipitation, with
reduced skill for the most intense echoes.

6
Fig. 2. Radar nowcasting verification diagnostics for an extreme precipitation event on 25 September 2024 (lead= 85min). This specific high-impact case
was selected as a stress test for the model; on this day, rapid convective intensification delivered over 100 mm of rainfall in a few hours, triggering an
IMD Red Alert and severe urban flooding in Mumbai. Composite reflectivity fields,Z(dBZ), are shown over the study domain with coastline overlay and
latitude/longitude axes. The top row shows (a) the last input frame att 0, (b) the verifying observation att 0 + 85min, and (c) the model prediction for the
same valid time; all panels use an identical reflectivity color scale. The bottom row presents (d) the spatial error field,∆Z=Z pred −Z truth (dBZ), where
positive (negative) values indicate overprediction (underprediction); (e) marginal reflectivity distributions over finite-overlap pixels for the truth and prediction;
and (f) the pixel-wise truth–prediction joint density (hexbin; log-scaled counts) for pixels with truth≥10dBZ, with the 1:1 reference line. The footer reports
categorical verification at the 10 dBZ exceedance threshold (hits, misses, false alarms, and correct negatives) and derived scores (POD, FAR, FPR, CSI, and
frequency bias), together with continuous intensity errors (MAE and MSE).
B. Spectral characteristics (PSD) and loss of small-scale
power
To assess whether forecasts preserve spatial structure across
spatial scales, we compare the radially averaged power spectral
density (PSD) of the predicted fields against the verifying
observations at selected lead times shown in Figure 4, span-
ning approximately 8, 31, 62, and 85 min. At 8 min,
the model spectrum is close to the observed spectrum at
larger wavelengths, while showing reduced power at shorter
wavelengths, indicative of smoothing and attenuation of fine-
scale variability. With increasing lead time (≈31,≈62, and
≈85 min), the deficit in short-wavelength power becomes more
pronounced, consistent with progressive weakening of sharp
gradients and compact convective features. The optical-flow
baseline generally retains more short-wavelength power than
the model, although both methods diverge increasingly from
the observed spectrum as lead time increases. Overall, the PSD
diagnostics complement the categorical metrics by indicating
that forecast degradation is associated primarily with loss of
small-scale structure and intensity damping, rather than the
introduction of spurious variability.

7
Fig. 3. Radially averaged power spectral density (PSD) of composite reflectivity (10logR) as a function of wavelength for the observations, optical-flow
extrapolation, and the proposed model at selected lead times of approximately 8, 31, 62, and 85 min.
C. Lead time dependence of categorical skill
To further examine the temporal robustness of the proposed
framework, we next evaluate how categorical skill varies
with forecast lead time across weak, moderate, and intense
reflectivity thresholds. Figure 5 shows that the proposed
model maintains useful categorical skill throughout the 90-
min forecast horizon, with 90-min CSI values of 0.437, 0.332,
and 0.193 for the≥10,≥20, and≥30dBZ thresholds,
respectively. Forecast skill decreases gradually with increasing
lead time, indicating stable temporal behaviour rather than an
abrupt loss of predictability. For≥20dBZ, CSI declines from
0.501 at 7.5 min to 0.387 at 60 min, and to 0.332 at 90 min.
ETS (Equitable Threat Score, which corrects CSI for random
hits) follows the same pattern, decreasing from 0.484 at 7.5
min to 0.367 at 60 min and 0.314 at 90 min. Frequency bias for
≥20dBZ remains above unity at all lead times (for example,
1.168 at 7.5 min and 1.228 at 90 min), indicating persistent
overprediction of areal coverage for moderate echoes even as
CSI decreases.
For≥10dBZ, CSI decreases from 0.596 at 7.5 min to
0.496 at 60 min, and to 0.437 at 90 min, with bias remaining
close to unity (approximately 1.07–1.10), indicating only slight
overcoverage. In contrast, intense echoes (≥30dBZ) show
the strongest degradation and clear underprediction at long
lead times. CSI decreases from 0.423 at 7.5 min to 0.283 at
60 min, and to 0.193 at 90 min. Frequency bias drops from
0.723 at 7.5 min to 0.492 at 90 min. This confirms that the
primary limitation at extended lead times is the representation
of compact high-reflectivity cores.
D. Continuous verification against a persistence baseline
We next examine lead time dependence using continuous
verification against a persistence baseline (Fig. 5), based on
domain-averaged RMSE and spatial correlation of composite
reflectivity. Persistence is most competitive at the shortest
horizon: at 7.5 min, it achieves RMSE 2.315 dBZ and cor-
relation 0.897, compared with 3.411 dBZ and 0.846 for the
model. This short-lead advantage of persistence is expected
and consistent with the literature, since no learned model can
improve upon the trivial first-step extrapolation before storm
structures have had time to evolve. By approximately 31 min,
the model becomes competitive with persistence, with slightly
lower RMSE (4.275 dBZ versus 4.310 dBZ) and higher spatial
correlation (0.774 versus 0.748). Beyond roughly 35 to 40
min, persistence degrades more rapidly. At approximately 54
min, the model shows lower RMSE (4.416 dBZ versus 4.801
dBZ) and higher correlation (0.768 versus 0.712), and by
85 min the separation increases further, with model RMSE
4.746 dBZ and correlation 0.714 relative to persistence RMSE
5.461 dBZ and correlation 0.629. Overall, the model maintains
stronger spatial agreement and lower error at longer horizons,
indicating improved representation of evolving storm structure
relative to pure persistence.
E. Station-Wise Multi-Event Validation
To further evaluate operational applicability, the proposed
framework was additionally validated against rainfall obser-
vations from 35 automatic weather stations across the Mum-
bai metropolitan region during three independent high-impact
rainfall events (17–19 August 2025). The model reproduced
the observed spatial distribution of moderate-to-heavy rainfall
and showed a gradual reduction in station-wise agreement with
increasing lead time. Detailed station-wise comparisons and
lead-time correlation analyses are provided in the Supplemen-
tary Material (Section S1).
Overall, the station-wise validation across multiple extreme-
rainfall days demonstrates that the proposed framework ef-
fectively captures moderate-to-heavy rainfall variability at the
station scale. The model shows consistent performance across
independent high-impact events, with strong agreement in
moderate-rainfall regimes and controlled underestimation in
extreme cases. These results reinforce the model’s general-
ization capability and highlight its suitability for urban-scale
operational nowcasting, where accurate spatial representation
of rainfall distribution is critical. In addition, the lead-time
correlation analysis shows that station-wise agreement de-
grades gradually across successive 15-minute windows rather
than collapsing abruptly, indicating stable temporal behaviour
across all three validation days.
IV. DISCUSSION
The results indicate that fusing multi-elevation radar ob-
servations with Doppler radial velocity–derived kinematic
proxy channels within a U-Net-style encoder–decoder can

8
Fig. 4. Lead-time evolution of categorical verification metrics for the proposed model and a persistence baseline across reflectivity thresholds of≥10,
≥20, and≥30dBZ. Panels show (a) Critical Success Index (CSI), (b) Equitable Threat Score (ETS), (c) frequency bias, and (d) observed event support as
functions of forecast lead time. Solid lines denote the proposed model, and dashed lines denote persistence. The model retains useful skill across the 90-min
forecast horizon, with the highest performance at lower reflectivity thresholds and increasing underprediction for intense echoes at longer lead times.
yield robust short-range precipitation nowcasts in a monsoon-
dominated coastal environment. Traditional extrapolation
methods are effective at very short lead times, but skill often
degrades beyond∼30–60 min because Lagrangian persistence
cannot represent convective initiation, intensification, or decay
[1], [7], [8]. Deep learning nowcasting models can partially
address this limitation by learning nonlinear structure and
evolution from radar archives, as demonstrated by ConvLSTM
sequence learners and encoder–decoder families such as U-
Net [12], [13]. Consistent with prior work, our evaluation
shows gradual skill degradation with lead time, controlled
false-alarm behaviour, and near-neutral frequency bias for
light-to-moderate echoes. These characteristics suggest that
the model captures storm-scale organization and displacement
while limiting spurious precipitation, a behaviour commonly
reported for deterministic radar nowcasts that preserve coher-
ent morphology even as intensity errors grow with forecast
horizon [16], [17].
A pronounced intensity dependence remains evident. Skill
decreases at higher reflectivity thresholds, and intense convec-
tive cores are underpredicted at longer lead times. Such attenu-
ation and smoothing of sharp reflectivity gradients are a widely
recognized limitation of deterministic point prediction in radar
nowcasting, particularly for rare, compact extremes that evolve

9
Fig. 5. Lead-time evolution of continuous verification metrics for composite reflectivity, comparing the proposed model (solid) with a persistence baseline
(dashed): (a) domain-averaged RMSE (dBZ) and (b) spatial correlation between forecast and observation. Persistence is most competitive at the shortest lead
times, while the proposed model retains lower RMSE and higher spatial correlation at longer horizons.
rapidly through nonlinear growth and decay processes [1],
[10], [16], [17]. Importantly, the dominant error mode in the
present study is weakening or missing of intense echoes rather
than widespread false echoes, as reflected by persistently low
false positive rates and high specificity across thresholds. This
conservative error behaviour is operationally meaningful in
applications such as urban flood early warning and aviation
support, where false alarms can be costly and where reliable
spatial guidance is often preferred over aggressive intensity
amplification.
In addition to categorical verification, the spectral diag-
nostics provide an objective view of scale-dependent realism.
Fig. 3 shows that the radially averaged power spectral density
progressively under-represents short-wavelength variance with
increasing lead time, indicating smoothing and loss of fine-
scale structure, while larger-scale variability is comparatively
better retained. This behaviour is consistent with a known
limitation of deterministic encoder–decoder nowcasting, where
optimization with pixel-wise objectives tends to damp sharp
gradients and compact convective maxima. The PSD result
therefore supports the interpretation that the dominant er-
ror mode is intensity attenuation and boundary smoothing
rather than widespread generation of spurious echoes, and
it motivates future extensions that better preserve small-scale
variability (e.g., scale-aware losses, multi-scale supervision, or
probabilistic/generative formulations).
Within the broader methodological landscape, the proposed
framework occupies a complementary position. Large-context
models such as MetNet and MetNet-2 improve regional consis-
tency through multiscale context aggregation [16], [17]. Gen-
erative and physics-constrained approaches, including DGMR,
NowcastNet, LUPIN, and ClimODE, focus on probabilistic
forecasting and physically constrained evolution to enhance
uncertainty representation, calibration, and long-lead forecast
skill [10], [18]–[20]. In contrast, the present study empha-
sizes a compact, deterministic, radar-only architecture that
incorporates radial-velocity-gradient proxy channels without
requiring full wind retrieval. The ability to preserve mesoscale
structure, orientation, and coherent displacement at extended
lead times suggests that these proxies regularize the learned
evolution during organized monsoon convection, consistent
with evidence that convergence- and shear-related signatures
contain useful information for convective initiation and storm
evolution [23], [24], [26], [27]. A further objective of this
study is to improve operational trust through interpretability.
The attribution analysis links model sensitivity to recognizable
storm-scale features, including convergence-line signatures
and gust-front-like boundaries, and verifies that the network
learns physically meaningful cues rather than artefacts, con-
sistent with recent work in interpretable machine learning
for weather and climate applications [28], [29]. Case-based
diagnostics (Fig. 2) further show that the model reproduces the
location, orientation, and spatial extent of organized systems,
with errors primarily arising from intensity damping and mod-
est displacement rather than widespread spurious precipitation.
Despite these strengths, underprediction of intense cores
remains the primary limitation and motivates clear direc-
tions for improvement. Promising pathways include hybrid
deterministic–stochastic formulations, explicit evolution con-
straints, and training objectives that better emphasize rare ex-
tremes while preserving the conservative false-alarm behaviour
observed here [10], [18]. Incorporating the proposed kinematic
proxy representation into probabilistic or generative frame-
works may be particularly beneficial, as it offers a mechanism
to retain the spatial reliability and dynamical structure captured
by the deterministic model while improving representation of
high-intensity convection.
V. CONCLUSIONS
This study presents a compact, radar-only deep learning
framework for short-range precipitation nowcasting tailored
to Mumbai’s monsoon convection. The approach fuses multi-
elevation reflectivity with Doppler radial velocity and radial-
velocity–gradient proxy channels within a spatiotemporal U-
Net, and produces 12-step composite-reflectivity forecasts at
7.5 min intervals up to approximately 90 min lead time. The
proxy representation is designed to encode convergence- and
shear-related kinematic signatures from single-Doppler obser-
vations without requiring retrieval of a full two-dimensional

10
wind field, while a high-reflectivity attention mechanism im-
proves sensitivity to convective cores.
Evaluation on temporally disjoint events shows that fore-
cast skill degrades gradually with lead time, while false
alarms remain controlled across thresholds, indicating stable
behaviour beyond the∼30–60 min range where extrapolation-
based methods typically deteriorate. The model retains useful
categorical skill throughout the forecast horizon, with 90-
min CSI values of 0.437, 0.332, and 0.193 at≥10,≥20,
and≥30dBZ, respectively. Performance remains intensity
dependent, with the strongest skill at lower thresholds and
systematic underprediction of compact high-reflectivity cores
at longer lead times. Continuous verification further shows
that although persistence is strongest at the shortest lead
time, the proposed model achieves lower RMSE and higher
spatial correlation at longer horizons, indicating improved
representation of evolving storm structure.
Physics-guided attribution indicates that the network’s sen-
sitivity is concentrated in physically interpretable regions,
highlighting kinematic precursor patterns near developing cells
and along boundary-like features consistent with convergence
lines and gust fronts. Together, these findings support the value
of physics-aware, multi-variable radar inputs for improving de-
terministic nowcast robustness and interpretability in a tropical
coastal setting.
Future work should focus on improving extreme-core pre-
diction through probabilistic or hybrid deterministic–stochastic
formulations, incorporating explicit evolution or continuity
constraints, and refining objective functions and sampling
strategies to better represent rare, high-intensity convection
while preserving the conservative false-alarm characteristics
demonstrated here.
ACKNOWLEDGMENTS
This project has received funding and support from the
HDFC ERGO - IIT Bombay Innovation Lab, a partnership
between HDFC ERGO General Insurance Company Ltd. and
Indian Institute of Technology Bombay committed to support
innovation and entrepreneurship in insurance and related ar-
eas.
REFERENCES
[1] J. W. Wilson, N. A. Crook, C. K. Mueller, J. Sun, and M. Dixon,
“Nowcasting thunderstorms: A status report,”Bulletin of the American
Meteorological Society, vol. 79, pp. 2079–2099, 1998.
[2] S. Pulkkinen, D. Nerini, A. P ´erez Hortal, C. Velasco-Forero, U. Ger-
mann, A. Seed, and L. Foresti, “Pysteps: an open-source Python library
for probabilistic precipitation nowcasting (v1.0),”Geoscientific Model
Development, vol. 12, pp. 4185–4219, 2019.
[3] S. Mohanty, M. Swain, R. Nadimpalli, K. K. Osuri, U. C. Mohanty,
P. Patel, and D. Niyogi, “Meteorological conditions of extreme heavy
rains over Mumbai,”Journal of Applied Meteorology and Climatology,
vol. 62, pp. 191–208, 2023.
[4] S. Paul, S. Ghosh, M. Mathew, A. Devanand, S. Karmakar, and
D. Niyogi, “Increased spatial variability and intensification of extreme
monsoon rainfall due to urbanization,”Scientific Reports, vol. 8, p. 3918,
2018.
[5] P. Bauer, A. Thorpe, and G. Brunet, “The quiet revolution of numerical
weather prediction,”Nature, vol. 525, pp. 47–55, 2015.
[6] A. J. Clark, W. A. Gallus Jr., M. Xue, and F. Kong, “Convection-
allowing models for forecasting convective weather: An overview and
status report,”Bulletin of the American Meteorological Society, vol. 97,
pp. 1703–1723, 2016.
[7] R. E. Rinehart and E. T. Garvey, “Three-dimensional storm motion
detection by conventional weather radar,”Nature, vol. 273, pp. 287–
289, 1978.
[8] N. E. Bowler, C. E. Pierce, and A. W. Seed, “Development of a
precipitation nowcasting algorithm based upon optical flow techniques,”
Journal of Hydrology, vol. 288, pp. 74–91, 2004.
[9] ——, “Steps: A probabilistic precipitation forecasting scheme which
merges extrapolation nowcast and downscaled NWP,”Quarterly Journal
of the Royal Meteorological Society, vol. 132, pp. 2127–2155, 2006.
[10] S. Ravuriet al., “Skilful precipitation nowcasting using deep generative
models,”Nature, vol. 597, pp. 672–677, 2021.
[11] A. Augst and M. Hagen, “Interpolation of operational radar data to a
regular Cartesian grid exemplified by Munich’s airport radar configu-
ration,”Journal of Atmospheric and Oceanic Technology, vol. 34, pp.
495–510, 2017.
[12] X. Shi, Z. Chen, H. Wang, D.-Y . Yeung, W.-K. Wong, and W.-C.
Woo, “Convolutional LSTM network: A machine learning approach for
precipitation nowcasting,” inAdvances in Neural Information Processing
Systems, vol. 28, 2015.
[13] O. Ronneberger, P. Fischer, and T. Brox, “U-Net: Convolutional net-
works for biomedical image segmentation,” inMedical Image Comput-
ing and Computer-Assisted Intervention – MICCAI 2015, ser. Lecture
Notes in Computer Science, vol. 9351, 2015, pp. 234–241.
[14] X. Shi, Z. Gao, L. Lausen, H. Wang, D.-Y . Yeung, W.-K. Wong, and
W.-C. Woo, “Deep learning for precipitation nowcasting: A benchmark
and a new model (TrajGRU),” 2017.
[15] Y . Wang, M. Long, J. Wang, Z. Gao, and P. S. Yu, “Predrnn: Recurrent
neural networks for predictive learning using spatiotemporal lstms,” in
Proceedings of the 31st International Conference on Neural Information
Processing Systems (NIPS’17), ser. NIPS’17. Red Hook, NY , USA:
Curran Associates, Inc., 2017, pp. 879–888, location: Long Beach,
California, USA.
[16] C. K. Sønderby, L. Espeholt, J. Heeket al., “MetNet: A neural weather
model for precipitation forecasting,” 2020.
[17] R. Lam, A. Sanchez-Gonzalez, M. Willsonet al., “GraphCast: Learning
skillful medium-range global weather forecasting,” 2022.
[18] Y . Zhang, M. Long, J. Chenet al., “Skilful nowcasting of extreme
precipitation with NowcastNet,”Nature, vol. 619, pp. 526–532, 2023.
[19] P. Pavl ´ık, M. V ´yboh, A. Bou Ezzeddine, and V . Rozinajov ´a, “Fully
differentiable Lagrangian convolutional neural network for continuity
consistent physics informed precipitation nowcasting,” 2024.
[20] Y . Verma, M. Heinonen, and V . Garg, “ClimODE: Climate and weather
forecasting with physics-informed neural ODEs,” inProceedings of the
International Conference on Learning Representations (ICLR 2024),
2024.
[21] K. O ´sr´odka and J. Szturc, “Quality-based generation of weather radar
Cartesian products,”Atmospheric Measurement Techniques, vol. 8, pp.
2173–2181, 2015.
[22] S. Ochoa-Rodriguez, L.-P. Wang, A. Gires, R. D. Pina, R. Reinoso-
Rondinel, G. Bruniet al., “A review of radar–rain gauge data merging
methods and their potential for hydrological applications,”Water Re-
sources Research, vol. 55, pp. 6356–6391, 2019.
[23] T. M. Weckwerth and D. B. Parsons, “A review of convection initiation
and motivation for IHOP 2002,”Monthly Weather Review, vol. 134, pp.
5–22, 2006.
[24] J. R. Mecikalski and K. M. Bedka, “Forecasting convective initiation by
monitoring the evolution of moving cumulus in daytime GOES imagery,”
Monthly Weather Review, vol. 134, pp. 49–78, 2006.
[25] P. Markowski and Y . Richardson,Mesoscale Meteorology in Midlati-
tudes. Chichester, UK: John Wiley & Sons, 2010.
[26] J. R. Mecikalski, W. M. MacKenzie, R. A. Kohrs, C. P. Jewett,
T. G. Chronis, and G. J. Jedlovec, “Aviation applications for satellite-
based observations of convective initiation,”Bulletin of the American
Meteorological Society, vol. 96, pp. 181–196, 2015.
[27] Y . Zeng, G. Huang, Q. Meng, J. Sun, and Y . Zhang, “Nowcasting
convective storm initiation with machine learning methods,”Weather
and Forecasting, vol. 34, pp. 1035–1052, 2019.
[28] I. Ebert-Uphoff and K. Hilburn, “Evaluation, tuning, and interpretation
of neural networks for working with images in meteorological applica-
tions,”Bulletin of the American Meteorological Society, vol. 101, pp.
E2149–E2170, 2020.
[29] R. Yang, J. Hu, Z. Li, J. Mu, T. Yu, J. Xia, X. Li, A. Dasgupta,
and H. Xiong, “Interpretable machine learning for weather and climate
prediction: A review,”Atmospheric Environment, vol. 338, p. 120797,
2024.
