---
title: Investigating Inductive Biases for Machine Learning Emulation of Sudden Stratospheric Warmings
  in Idealised Isca Simulations
url: https://arxiv.org/abs/2606.18857
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Oskar Bohn Lassen
- Simon Driscoll
- Stephen I. Thomson
- Sebastian Schemm
- Francisco C. Pereira
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.18857
pages: 36
chars: 100539
fetched_at: '2026-11-08T13:27:10+00:00'
kb_version: 1
---

# Investigating Inductive Biases for Machine Learning Emulation of Sudden Stratospheric Warmings in Idealised Isca Simulations

INVESTIGATINGINDUCTIVEBIASES FORMACHINELEARNING
EMULATION OFSUDDENSTRATOSPHERICWARMINGS IN
IDEALISEDISCASIMULATIONS
A PREPRINT
Oskar Bohn Lassen
Department of Technology,
Management, and Economics
Technical University of Denmark
obola@dtu.dk
Simon Driscoll
Department of Applied Mathematics
and Theoretical Physics
University of Cambridge
sd2136@cam.ac.uk
Stephen I. Thomson
Department of Mathematics
and Statistics
University of Exeter
s.i.thomson@exeter.ac.uk
Sebastian Schemm
Department of Applied Mathematics
and Theoretical Physics
University of Cambridge
ss3299@cam.ac.uk
Francisco C. Pereira
Department of Technology,
Management, and Economics
Technical University of Denmark
camara@dtu.dk
ABSTRACT
Machine-learning emulators are increasingly used for weather prediction and have the potential to
extend skill on subseasonal-to-seasonal timescales by learning dynamically important sources of
predictability. A key challenge is whether the models can exploit predictability anchors, such as
stratospheric variability, that influence tropospheric circulation beyond short lead times. We test how
architectural inductive bias affects emulation of sudden stratospheric warming (SSW) dynamics using
paired idealised Isca simulations that differ only in an imposed wave-2 heating perturbation. Across
convolutional, transformer, and graph-based architectures trained for one-step prediction, model
differences are modest when the stratosphere is dynamically quiet but widen substantially when SSW-
like variability is active. Our results identify explicit three-dimensional vertical coupling as a key
inductive bias for machine-learning emulation of stratospheric dynamics. However, Eliassen–Palm
flux diagnostics show that low forecast error does not guarantee physically faithful wave–mean-flow
interaction, with coherent errors remaining in stratospheric wave-driving structure.
KeywordsClimate emulation·Machine learning·Atmospheric dynamics·Stratospheric variability
1 Introduction
Physics-based general circulation models (GCMs) have been used for decades in weather prediction and climate
simulation. These models evolve atmospheric states through numerical integration of governing equations for large-
scale dynamics, together with parameterised representations of unresolved processes Stensrud [2011], Bauer et al.
[2015], Bordoni et al. [2025]. Because model fidelity and computational cost depend on resolution and on the treatment
of subgrid processes, atmospheric scientists use model hierarchies, ranging from comprehensive operational Earth
System Models (ESMs) to idealised dynamical-core configurations Held and Suarez [1994], Jeevanjee et al. [2017],
Maher et al. [2019].
Despite sustained progress in numerical modelling, the cost of high-resolution simulation and the limitations of physics-
based parameterisations have motivated machine-learning (ML) approaches aimed at accelerating and improving
atmospheric models Dueben and Bauer [2018], Kashinath et al. [2021]. One prominent direction is hybrid physics-ML
modelling, in which ML components emulate or replace expensive parameterisations Rasp et al. [2018], Brenowitz
and Bretherton [2018], Yuval and O’Gorman [2020], Wang et al. [2022], Bertoli et al. [2025]. A closely related line
arXiv:2606.18857v1  [cs.LG]  17 Jun 2026

A PREPRINT
of work develops end-to-end hybrid neural GCMs that combine a dynamical solver with learned components in a
differentiable framework Kochkov et al. [2024]. In parallel, purely data-driven models trained directly on reanalysis
have demonstrated competitive medium-range forecast skill, including graph-based architectures such as GraphCast,
Earth-specific transformers as Pangu-Weather, spectral/Fourier-inspired approaches as FourCastNet, and operational
systems as AIFS Lam et al. [2023], Bi et al. [2023], Pathak et al. [2022], Moldovan et al. [2026]. Foundation models
such as Aurora have extended this paradigm by pretraining on Earth-system datasets and fine-tuning to downstream
forecasting tasks Bodnar et al. [2025]. A related line of work is simulator emulation, where a ML model is trained on
outputs of a given numerical simulator to learn its state-transition map Scher and Messori [2019], Gunawardena et al.
[2021].
However, accurately modelling the stratosphere and its influence on the troposphere remains challenging for ML
systems Lam et al. [2023], Bodnar et al. [2025], Ozdemir et al. [2026] with recent evaluations finding that ML weather
models struggle to capture stratosphere-troposphere coupling during sudden stratospheric warmings (SSWs) Wu [2026].
SSWs are large disruptions of the polar vortex caused by planetary-wave forcing and wave-mean-flow interaction,
and represent an example of complex stratospheric dynamics Matsuno [1971], Baldwin et al. [2021]. Stratospheric
anomalies from SSWs can descend and project onto tropospheric circulation regimes, affecting surface weather on
subseasonal timescales Baldwin and Dunkerton [2001], Kidston et al. [2015]. Hence, stratospheric variability is an
important source of subseasonal predictability, but exploiting this source in ML models depends in part on accurately
representing vertically propagating waves and wave-mean-flow interaction. This motivates our central hypothesis:
ML architectures that more naturally encode vertically coupled, multiscale dynamics should show relatively larger
gains when stratospheric wave dynamics are active. Because observational records confound many factors, we use
an idealised Isca GCM configuration in which SSW-like variability can be either suppressed or enhanced through
modifications to the imposed forcing of the stratosphere by tropospheric wave sources Jucker et al. [2014], Mudhar
et al. [2024].
We generate paired datasets with and without frequent SSW-like disturbances, holding all other model settings fixed.
We then train a suite of ML emulator architectures separately for each regime, spanning 2D and 3D CNNs, transformers,
and graph-based models. We compare aggregate errors, vertical and latitudinal error structure, and EP-flux diagnostics
to test whether vertical-coupling and wave-propagation biases are most beneficial under active SSW-like dynamics.
Using single-timestep diagnostics isolates architectural inductive bias from the rollout-training strategies used in current
ML weather models to achieve long-lead skill Lam et al. [2023]. Ultimately, this study aims to clarify which design
choices are most important for faithfully capturing stratospheric dynamics in ML weather and climate emulation.
2 Methodology and experimental setup
2.1 Isca dynamics & Eliassen-Palm fluxes
We use the Isca atmospheric modelling framework to generate controlled idealised simulations of stratospheric
variability Vallis et al. [2018]. Isca is well suited for this purpose because it allows individual physical mechanisms to
be isolated in simplified dynamical-core configurations. Here, the atmospheric state xt contains temperature T , zonal
wind u, and meridional wind v on a latitude–longitude–pressure grid. The simulator defines a discrete time-evolution
operator,
xt+∆t =M(x t),(1)
which the machine-learning emulator will be trained to approximate.
The simulations use a dry spectral dynamical-core configuration based on Mudhar et al. [2024], with T42 horizontal
resolution, 60 vertical pressure levels (38 above 100 hPa), and a 240 s atmospheric time step. The troposphere follows a
Held–Suarez-style setup, with temperature relaxed toward a prescribed equilibrium profile and low-level winds damped
by Rayleigh friction Held and Suarez [1994]. The stratosphere follows a modified Polvani–Kushner equilibrium-
temperature formulation Polvani and Kushner [2002]. This means the Isca configuration has no explicit radiation
scheme, moisture, or sea-surface temperature as these processess are represented implicitly by the relaxation profile.
The simulations are run in perpetual-winter configuration, such that one hemisphere remains in winter throughout the
integration meaning that our 6 years of run-time is effectively 20 winters. To generate SSW-like variability, we activate
a prescribed zonal wave-2 heating perturbation constant in time, centered near 45◦N and 400 hPa, following Mudhar
et al. [2024] and Lindgren et al. [2018]. This forcing generates stationary planetary-scale Rossby waves that propagate
upward into the stratosphere and disturb the winter polar vortex. The paired no-SSW and SSW-enabled datasets are
identical except for this imposed wave-heating perturbation.
This paired design is intended as a controlled test of emulator behaviour under two dynamical regimes, rather than
as a climatological sampling study of real-world SSW diversity. The three-hourly output provides more than 15,000
2

A PREPRINT
a) c)b)
Figure 1: The upper panel shows zonal wind at 60 ◦N and 10 hPa for the no-SSW and SSW-enabled configurations.
Highlighted time steps are shown in the lower panel as polar maps of absolute vorticity: (a) a compact vortex from the
no-SSW simulation, (b) a split SSW event from the SSW-enabled simulation, and (c) a displacement SSW event from
the SSW-enabled simulation.
supervised one-step state transitions, while comparing the two experiments isolates a specific mechanism: dry planetary-
wave forcing, upward wave propagation, and polar-vortex disruption. By excluding additional sources of variability such
as the quasi-biennial oscillation (QBO), volcanic forcing, solar variability, topography, and moist processes, the setup
makes it possible to attribute differences in emulator performance directly to the presence of SSW-like wave–mean-flow
dynamics. Using the standard zonal-mean zonal-wind reversal criterion at 60 ◦N and 10 hPa, the no-SSW dataset
contains no detected SSW events, while the SSW-enabled dataset has an SSW frequency of 0.32 events per 100 model
days Charlton and Polvani [2007].
Figure 1 places selected vortex snapshots within the full simulated time series. The no-SSW configuration maintains
a strong, positive zonal-mean zonal wind at 60 ◦N and 10 hPa, indicating a persistent polar vortex, while the SSW-
enabled configuration exhibits vortex weakening and reversals. The selected maps show representative 10 hPa vortex
morphologies: a compact vortex in the no-SSW simulation, and split and displacement events in the SSW-enabled
simulation. For both simulations, the first 1000 three-hourly output steps are discarded as spin-up, after which the
trajectories are converted into supervised one-step prediction pairs (xt,x t+∆t) with ∆t= 3 hours. The data are split
chronologically into training ( N= 2000 ), validation ( N= 250 ), and test ( N= 250 ) periods, and normalization
statistics are computed from the training set only, separately for each variable and pressure level. The training set
size was chosen as a feasible compromise for large hyperparameter sweeps across architectures, with the data-scaling
experiment in the Supporting Information showing that performance continued to improve but with diminishing returns
at larger sample sizes.
To evaluate whether the emulators capture physically meaningful wave dynamics, we use Eliassen–Palm flux diag-
nostics Andrews et al. [1987]. These diagnostics summarize wave–mean-flow interaction through eddy covariance
terms u′v′ and v′T ′, where primes denote deviations from the zonal mean and overbars denote zonal averaging. In the
quasi-geostrophic approximation, the EP-flux vectorF= (F ϕ, Fp)is proportional to these eddy fluxes, with
Fϕ ∝ −u′v′, F p ∝ v′T ′.(2)
Its divergence, ∇ ·F, indicates where wave activity interacts with and forces the zonal-mean flow. Because SSW
development is associated with enhanced upward and poleward wave propagation into the winter stratosphere, EP-flux
diagnostics provide a mechanism-aware complement to pointwise forecast error. They test whether an emulator captures
not only the local values of T , u, and v, but also the covariance structure responsible for realistic wave–mean-flow
interaction. A more elaborate explanation of the EP-flux diagnostics in spherical coordinates and Isca configuration is
found in the Supporting Information.
3

A PREPRINT
Figure 2: Schematic overview of the architecture families used in this study. Two-dimensional convolutional and
transformer models operate on latitude–longitude structure while stacking pressure levels and variables in the channel
dimension, whereas three-dimensional variants act directly across latitude, longitude, and pressure and therefore encode
explicit vertical coupling. Graph-based models represent the atmosphere on either a spherical grid graph or a spherical
mesh while stacking pressure levels and variables in the node features.
2.2 Machine-Learning Emulation
Given simulator-generated trajectories {xt}T t=1, emulator learning aims to approximate the one-step time-evolution
operator of the simulator. We train a neural networkf θ to predict
ˆxt+∆t =f θ(xt),(3)
where xt is the atmospheric state and ∆t= 3 hours. The model parameters are optimized on paired examples
(xt,x t+∆t)by minimizing a prediction loss over the training set,
θ∗ = arg min
θ
1
N
NX
i=1
L

fθ(x(i) t ),x (i) t+∆t

.(4)
The central question is how architectural inductive bias affects this approximation. We compare convolutional, graph-
based, and transformer-based emulators that differ in how they represent horizontal structure, vertical coupling, and
long-range interaction. In particular, 2D models operate on latitude–longitude fields while stacking pressure levels and
variables, whereas 3D models operate directly over latitude, longitude, and pressure. Graph-based models represent the
atmosphere on spherical grid or mesh graphs while stacking pressure levels and variables in node features. This design
allows us to test whether explicit vertical coupling becomes more important when SSW-like wave dynamics are active.
A schematic overview of the architecture families is shown in Figure 2.
All models are trained for the same one-step forecasting task, predicting temperature, zonal wind, and meridional
wind jointly over the full grid. Within each architecture family, we run a fixed-size hyperparameter sweep of 50
configurations and select the model with the lowest validation MAE. Model skill is evaluated on the held-out test period
using per-variable mean absolute error over the full atmosphere and over the mid-upper stratosphere, defined here as
pressure levels with pressures lower than 30 hPa. To test whether low pointwise error also corresponds to physically
meaningful dynamics, we additionally compute Eliassen–Palm flux diagnostics from the predicted and true fields.
Further details of the preprocessing, model families, hyperparameter sweeps, and implementation choices are provided
in the Supporting Information.
4

A PREPRINT
Table 1:Best model per architecture on the no-SSW and SSW-enabled Isca datasets. Reported values show mean absolute error
(MAE) for temperature, zonal wind, and meridional wind over the full atmosphere and over the stratosphere (p <30 hPa).Dark,
medium, and light green text indicate the best, second-best, and third-best values in each column, respectively.
No SSW With SSW
Full atmosphere Stratosphere (<30 hPa) Full atmosphere Stratosphere (<30 hPa)
Architecture
Temp
[K]
Z. wind
[m/s]
M. wind
[m/s]
Temp
[K]
Z. wind
[m/s]
M. wind
[m/s]
Num.
params
Temp
[K]
Z. wind
[m/s]
M. wind
[m/s]
Temp
[K]
Z. wind
[m/s]
M. wind
[m/s]
Num.
params
Persistence 0.244 0.581 0.621 0.352 0.790 0.778 – 0.235 0.608 0.678 0.316 0.818 0.863 –
Simple CNN2D 0.088 0.170 0.146 0.127 0.241 0.192 154M 0.119 0.263 0.251 0.164 0.373 0.348 157M
CNN2D U-Net 0.080 0.173 0.164 0.119 0.252 0.226 36M 0.123 0.284 0.288 0.176 0.419 0.418 147M
Simple CNN3D 0.081 0.151 0.122 0.114 0.208 0.154 6M 0.084 0.190 0.195 0.117 0.277 0.282 6M
CNN3D U-Net 0.060 0.111 0.082 0.083 0.152 0.1003M0.070 0.150 0.141 0.095 0.214 0.1955M
Trf.-2D GA 0.083 0.179 0.161 0.119 0.244 0.203 679M 0.118 0.281 0.267 0.162 0.395 0.365 214M
Trf.-2D Swin 0.080 0.181 0.167 0.115 0.247 0.217 217M 0.109 0.267 0.267 0.154 0.381 0.375 259M
Trf.-3D GA 0.0460.090 0.0750.0630.122 0.093101M0.055 0.126 0.129 0.078 0.181 0.187134M
Trf.-3D Swin0.0440.103 0.1010.0600.132 0.121 82M 0.074 0.167 0.171 0.104 0.244 0.246 82M
Grid MPNN 0.096 0.213 0.206 0.145 0.308 0.289 9M 0.140 0.349 0.357 0.200 0.508 0.511 8M
Mesh MPNN 0.094 0.205 0.191 0.143 0.300 0.271 31M 0.129 0.295 0.278 0.180 0.428 0.398 21M
3 Results
3.1 Overall summary
Table 1 summarizes the best tuned model within each architecture family on the no-SSW and SSW-enabled datasets.
Across both regimes, but most clearly in the SSW-enabled case and in the stratosphere-focused metrics, explicitly
three-dimensional models perform best, especially the 3D U-Net and the 3D global transformer. By contrast, the 2D
and graph-based models are generally less competitive in the stratosphere-focused metrics, despite in some cases having
substantially more parameters. The model sizes were selected by the validation-based hyperparameter tuning procedure,
rather than imposed manually.
3.2 Performance differences widen in the SSW-enabled regime
Figure 3 shows mean absolute error as a function of pressure level for temperature and zonal wind in the no-SSW
and SSW-enabled regimes. The learned models are clearly separated from the persistence baseline, indicating that all
architectures learn meaningful predictive structure beyond simply carrying the previous state forward. The persistence
errors are pronounced in both the no-SSW and with-SSW regimes, despite the lack of zonal-mean variability in the
no-SSW case as seen in Figure 1. The reason the no-SSW configuration has a large persistence error aswell is that
small displacements in the sharp wind structure generate large grid-point errors.
In the no-SSW case, the learned models themselves remain relatively clustered, with only moderate architecture-
dependent differences in their vertical error profiles. By contrast, in the SSW-enabled regime, the spread between
learned architectures increases markedly in the upper troposphere and stratosphere. This is particularly clear for zonal
wind, where the strongest vertically structured models maintain substantially lower error than the weaker 2D and
graph-based models. Hence, the SSW-enabled regime does not simply increase error uniformly across all models; rather,
it amplifies the performance differences between model classes. This suggests that vertically structured architectures
provide not only a lower domain-averaged MAE, but also a more accurate representation of the complex stratospheric
dynamics.
3.3 EP-flux diagnostics
Accurate pointwise prediction of these variables does not necessarily imply that the learned emulator preserves the
physical relationships between them. This is particularly important for EP-flux diagnostics, which depend on the
eddy covariance terms u′v′ and v′T ′. Thus, a model may reproduce the individual fields well while still distorting the
wave-driving structure that controls wave-mean-flow interaction.
Figure 4 shows EP-flux diagnostics averaged over the 10 days preceding the vortex-weakening event shown in Figure 1
(c). The event is chosen as a clear example of vortex weakening, identified from the zonal-mean zonal wind at 60◦N
and 10 hPa, and occurs more than 125 days after the training, validation, and test periods. This pre-event period is used
because anomalous upward and poleward wave activity is expected before the vortex weakening Baldwin et al. [2021].
For each model, we compute EP fluxes from the predictions and compare them with the corresponding diagnostic
5

A PREPRINT
Figure 3:Mean absolute error as a function of pressure level for temperature and zonal wind. Colored lines denote learned
architectures and the dashed black line denotes persistence.
computed from the true simulator trajectory. Rather than evaluating an autoregressive rollout, the EP-flux diagnostics
are averaged over the t+ 1 outputs of 80 independent one-step predictions during the 10-day pre-event period. This
avoids attributing diagnostic errors to accumulated trajectory drift, where small state errors can move the predicted
flow away from the event being diagnosed. Instead, the errors shown in these diagnostics provide a short-lead-time
test of physical consistency, assessing whether the emulator preserves the wind–temperature covariance relationships
needed to reproduce the EP-flux structure central to stratospheric wave-mean-flow interaction. The upper row shows
the EP-flux vectors and EP-flux divergence, while the lower row shows the divergence error, defined as true minus
predicted divergence. The upper panels show that the emulators preserve the EP-flux structure at a broad level where
the predicted divergence fields place the largest positive and negative regions in approximately the right parts of the
latitude-pressure domain. The largest errors occur in the high-latitude stratosphere (1-10 hPa), especially near the
region where the true fields show strong pre-SSW EP-flux divergence. These errors are coherent regions of over- and
under-predicted divergence, indicating that the models misplace or misestimate part of the wave forcing. By contrast,
tropospheric errors are generally smaller, even though the true tropospheric EP-flux divergence is also large. This
suggests that the stratospheric EP-flux diagnostic is not harder merely because the diagnostic amplitude is larger, but
because the relevant covariance structure is more difficult to reproduce during SSW development.
We decompose the EP fluxes by scale by recomputing them using only zonal wave1, wave 2, and wave 3 separately
using a spatial Fourier-Transform over longitude Jucker [2021] and define residual smaller-scale contributions as the full
diagnostic minus the contributions from waves 1-3. Figure 5 shows this decomposition for the true simulation and for
selected emulators. In the Isca simulation, the pre-SSW stratospheric EP-flux divergence is dominated by waves 1 and
2. However, the emulator error is not distributed in proportion to the EP-flux divergence strength across wavenumbers,
but is especially large for the wave-1 component in the high-latitude stratosphere. The contrast between waves 1 and 2
is particularly intriguing given that the main source of tropospheric planetary-scale variability comes from our imposed
wave-2 heating. Therefore, any significant wave-1 component of the EP-flux must come from internal atmospheric
interactions, which are likely to be more difficult for the emulators to predict. However, it is not simply the case that
wave 1 is intrinsically hard to predict - the wave-1 tropospheric EP-flux anomalies are predicted with low error by the
emulators, as is the total EP-flux divergence from all waves.
The contrast we observe between waves 1 and 2 in the EP-flux divergence error is consistent with previous research.
Lindgren and Sheshadri [2020] showed that stratospheric wave-wave interactions can transfer energy between wavenum-
bers, producing SSW structures in a wave number different from that of the tropospheric forcing. Furthermore Lindgren
and Sheshadri [2020], showed that selectively removing wave-wave interactions in the upper stratosphere significantly
alters SSW frequencies. The wave-1 stratospheric EP-flux signal in our SSW-enabled simulation, despite imposed
wave-2 tropospheric forcing, could be expected to arise predominantly from in-stratosphere wave-wave interactions.
Seeing that the emulators reproduce tropospheric wave-1 EP-flux structure but systematically misplace stratospheric
6

A PREPRINT
Figure 4:EP-flux diagnostics for selected architectures averaged over the 10 days preceding a held-out SSW event. The upper row
shows EP-flux vectors overlaid on EP-flux divergence for the true simulator trajectory and model predictions. The lower row shows
divergence error, defined as true minus predicted divergence. The dashed contour marks the dynamical tropopause, defined here as
the zonal- and time-mean contour of absolute potential vorticity.
wave-1 EP-flux divergence therefore suggests a specific failure mode where architectures capture the wave-mean-flow
response to the imposed wave-2 forcing but struggle with the nonlinear stratospheric processes responsible for the
wave-1 signal. Because the training period already contains disturbed vortex states, including both split-like and
displacement-like configurations, this error is unlikely to be resolved simply by exposing the models to more event
morphologies. Instead, the diagnostic points to a need for architectures that better preserve the physical covariance
structure underlying wave activity.
A narrow error band near 10 hPa appears for 3D architectures in Figures 4–5. This discretization-related artifact arises
from including an exact 10 hPa diagnostic level close to an existing 10.24 hPa model level. We retain it as a useful
emulator-design example: physically derived diagnostics can expose artifacts caused by seemingly minor preprocessing
choices, even when pointwise forecast errors appear unaffected. The artifact is removed to proof this point and discussed
more in the Supporting Information.
4 Limitations & future research
Our results show that explicit vertical coupling is particularly important when stratospheric dynamics are active.
However, the EP-flux diagnostics highlight the need for more physically consistent emulators. Firstly, physically
informed objectives could combine EP-flux or tendency-consistency terms with vortex-geometry measures such as
orientation, ellipticity, and centroid, which are particularly relevant for wave-1 variability Mitchell et al. [2011], Seviour
et al. [2013], Waugh [1997]. Secondly, because this study deliberately focuses on one-step predictions to isolate
architectural inductive biases, multi-step and event-conditioned training objectives are a natural next step. Third, the
relatively good qualitative behaviour of the mesh-based GNN in some diagnostics suggests that spherical geometry may
matter even when its aggregate MAE remains less competitive, especially if combined with explicit vertical structure.
Finally, the models are trained using a relatively short model timeseries which was possible since the Isca configuration
was constantly disrupting the vortex in the simulation. However, one focus for future work would be to study the various
7

A PREPRINT
Figure 5:Zonal-wavenumber decomposition of EP-flux divergence during the 10 days preceding a held-out SSW event. Columns
show how the EP-flux divergence is split by wave scale: all waves together, wave1, wave 2, wave 3, and the remaining smaller-scale
waves. The top row shows the true simulator diagnostic, while lower rows show divergence errors for selected emulators, defined as
true minus predicted divergence. The largest coherent errors are concentrated in the wave-1 component.
types and precursors of different SSWs, and to look specifically at how these different classes of SSWs are handled by
the various architectures Baldwin et al. [2021].
5 Conclusion
We benchmarked machine-learning emulator architectures on idealised Isca simulations with and without SSW-like
dynamics. While model differences are relatively modest in the no-SSW regime, they widen substantially in the
SSW-enabled regime, where architectures with explicit three-dimensional structure perform best. At the same time,
mechanism diagnostics show that low forecast error alone is not sufficient: even strong models can still fail to fully
8

A PREPRINT
preserve the relevant wave-driving structure during active events. In particular, the largest coherent diagnostic errors
occur in the high-latitude stratosphere and are concentrated in the long-wave divergence structure. Together, these
results show that robust atmospheric emulation requires both appropriate architectural inductive biases, especially
explicit vertical coupling, and evaluation metrics that test physically consistent behaviour beyond grid-point error.
Code and Data Availability
The fork of ISCAand the configuration files used to generate the no-SSW and SSW-enabled simulations are available in
the Isca data-generation repository. The machine-learning and analysis code is available in the Isca emulation repository.
This repository contains scripts for preprocessing raw ISCAoutput, constructing train-validation-test datasets, training
the emulator models, evaluating predictions, computing Eliassen–Palm flux diagnostics, and reproducing the figures
in this paper. The corresponding experiment logs, final training runs, validation metrics, model configurations, and
selected model artifacts are available in the accompanying Weights & Biases report. The code for computing EP fluxes
was adapted from aostools Jucker [2021]. Together, these repositories provide the code required to regenerate the
simulation data products and reproduce the experiments reported here.
Acknowledgments
This work is supported by Novo Nordisk Foundation grant NNF23OC0085356 and Pioneer Centre for AI, DNRF grant
number P1.
References
David J. Stensrud.Parameterization schemes: Keys to understanding numerical weather prediction models, volume
9780521865401. Cambridge University Press, 2011. ISBN 0521865409. doi:10.1017/CBO9780511812590.
Peter Bauer, Alan Thorpe, and Gilbert Brunet. The quiet revolution of numerical weather prediction.Nature, 525:
47–55, 09 2015. doi:10.1038/nature14956.
Silvia Bordoni, S. Kang, Tiffany Shaw, I. Simpson, and Laure Zanna. The futures of climate modeling.npj Climate
and Atmospheric Science, 8, 03 2025. doi:10.1038/s41612-025-00955-8.
Isaac M. Held and Max J. Suarez. A proposal for the intercomparison of the dynamical cores of atmospheric general
circulation models.Bulletin of the American Meteorological Society, 75(10):1825 – 1830, 1994. doi:10.1175/1520-
0477(1994)075<1825:APFTIO>2.0.CO;2.
Nadir Jeevanjee, Pedram Hassanzadeh, Spencer Hill, and Aditi Sheshadri. A perspective on climate model hierarchies.
Journal of Advances in Modeling Earth Systems, 9(4):1760–1771, 2017. doi:https://doi.org/10.1002/2017MS001038.
Penelope Maher, Edwin P. Gerber, Brian Medeiros, Timothy M. Merlis, Steven Sherwood, Aditi Sheshadri, Adam H.
Sobel, Geoffrey K. Vallis, Aiko V oigt, and Pablo Zurita-Gotor. Model hierarchies for understanding atmospheric
circulation.Reviews of Geophysics, 57(2):250–280, 2019. doi:https://doi.org/10.1029/2018RG000607.
P. D. Dueben and P. Bauer. Challenges and design choices for global weather and climate models based on machine
learning.Geoscientific Model Development, 11(10):3999–4009, 2018. doi:10.5194/gmd-11-3999-2018.
K. Kashinath, M. Mustafa, A. Albert, J-L. Wu, C. Jiang, S. Esmaeilzadeh, K. Azizzadenesheli, R. Wang, A. Chat-
topadhyay, A. Singh, A. Manepalli, D. Chirila, R. Yu, R. Walters, B. White, H. Xiao, H. A. Tchelepi, P. Marcus,
A. Anandkumar, P. Hassanzadeh, and Prabhat. Physics-informed machine learning: case studies for weather and
climate modelling.Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering
Sciences, 379(2194):20200093, 02 2021. ISSN 1364-503X. doi:10.1098/rsta.2020.0093.
Stephan Rasp, Michael S. Pritchard, and Pierre Gentine. Deep learning to represent subgrid processes in climate models.
Proceedings of the National Academy of Sciences, 115(39):9684–9689, 2018. doi:10.1073/pnas.1810286115.
N. D. Brenowitz and C. S. Bretherton. Prognostic validation of a neural network unified physics parameterization.
Geophysical Research Letters, 45(12):6289–6298, 2018. doi:https://doi.org/10.1029/2018GL078510.
Janni Yuval and Paul A. O’Gorman. Stable machine-learning parameterization of subgrid processes for climate modeling
at a range of resolutions.Nature Communications, 11(1), 2020. ISSN 2041-1723. doi:10.1038/s41467-020-17142-3.
Xin Wang, Yilun Han, Wei Xue, Guangwen Yang, and Guang Zhang. Stable climate simulations using a realistic general
circulation model with neural network parameterizations for atmospheric moist physics and radiation processes.
Geoscientific Model Development, 15:3923–3940, 05 2022. doi:10.5194/gmd-15-3923-2022.
9

A PREPRINT
Guillaume Bertoli, Salman Mohebi, Firat Ozdemir, Jonas Jucker, Stefan Rüdisühli, Fernando Perez-Cruz, Mathieu
Salzmann, and Sebastian Schemm. Revisiting machine learning approaches for short- and longwave radiation
inference in weather and climate models.Journal of Advances in Modeling Earth Systems, 17(9):e2025MS004956,
2025. doi:https://doi.org/10.1029/2025MS004956. e2025MS004956 2025MS004956.
Dmitrii Kochkov, Janni Yuval, Ian Langmore, Peter Norgaard, Jamie Smith, Griffin Mooers, Milan Klöwer, James
Lottes, Stephan Rasp, Peter Düben, Sam Hatfield, Peter Battaglia, Alvaro Sanchez-Gonzalez, Matthew Willson,
Michael P. Brenner, and Stephan Hoyer. Neural general circulation models for weather and climate.Nature, 632
(8027):1060–1066, 2024. ISSN 1476-4687. doi:10.1038/s41586-024-07744-y. URL http://dx.doi.org/10.
1038/s41586-024-07744-y.
Remi Lam, Alvaro Sanchez-Gonzalez, Matthew Willson, Peter Wirnsberger, Meire Fortunato, Ferran Alet, Suman
Ravuri, Timo Ewalds, Zach Eaton-Rosen, Weihua Hu, Alexander Merose, Stephan Hoyer, George Holland, Oriol
Vinyals, Jacklynn Stott, Alexander Pritzel, Shakir Mohamed, and Peter Battaglia. Learning skillful medium-range
global weather forecasting.Science, 382(6677):1416–1421, 2023. doi:10.1126/science.adi2336.
Kaifeng Bi, Lingxi Xie, Hengheng Zhang, Xin Chen, Xiaotao Gu, and Qi Tian. Accurate medium-range global weather
forecasting with 3d neural networks.Nature, 619:1–6, 07 2023. doi:10.1038/s41586-023-06185-3.
Jaideep Pathak, Shashank Subramanian, Peter Harrington, Sanjeev Raja, Ashesh Chattopadhyay, Morteza Mardani,
Thorsten Kurth, David Hall, Zongyi Li, Kamyar Azizzadenesheli, Pedram Hassanzadeh, Karthik Kashinath, and
Animashree Anandkumar. Fourcastnet: A global data-driven high-resolution weather model using adaptive fourier
neural operators. 02 2022.
G. Moldovan, E. Pinnington, A. Prieto Nemesio, S. Lang, Z. Ben Bouallègue, J. Dramsch, M. Alexe, M. Santa Cruz,
S. Hahner, H. Cook, H. Theissen, M. Clare, C. O’Brien, J. Polster, L. Magnusson, G. Mertes, F. Pinault, B. Raoult,
P. de Rosnay, R. Forbes, and M. Chantry. Aifs single 1.1.0: an update to ecmwf’s machine-learned weather forecast
model aifs.Geoscientific Model Development, 19(10):4703–4724, 2026. doi:10.5194/gmd-19-4703-2026.
Cristian Bodnar, Wessel Bruinsma, Ana Lucic, Megan Stanley, Anna Allen, Johannes Brandstetter, Patrick Garvan,
Maik Riechert, Jonathan Weyn, Haiyu Dong, Jayesh Gupta, Kit Thambiratnam, Alexander Archibald, Chun-Chieh
Wu, Elizabeth Heider, Max Welling, Richard Turner, and Paris Perdikaris. A foundation model for the earth system.
Nature, 641:1180–1187, 05 2025. doi:10.1038/s41586-025-09005-y.
S. Scher and G. Messori. Weather and climate forecasting with neural networks: using general circulation models
(gcms) with different complexity as a study ground.Geoscientific Model Development, 12(7):2797–2809, 2019.
doi:10.5194/gmd-12-2797-2019.
Nipun Gunawardena, Giuliana Pallotta, Matthew Simpson, and Donald D. Lucas. Machine learning emulation of spatial
deposition from a multi-physics ensemble of weather and atmospheric transport models.Atmosphere, 12(8), 2021.
ISSN 2073-4433. doi:10.3390/atmos12080953.
Firat Ozdemir, Yun Cheng, Salman Mohebi, Fanny Lehmann, Simon Adamov, Zhenyi Zhang, Leonardo Trentini, Dana
Grund, Oliver Fuhrer, Torsten Hoefler, Siddhartha Mishra, Sebastian Schemm, Benedikt Soja, and Mathieu Salzmann.
Earth system foundation model (esfm): A unified framework for heterogeneous data integration and forecasting,
2026. URLhttps://arxiv.org/abs/2605.00850.
Zheng Wu. Assessing subseasonal predictions of stratosphere-troposphere coupling of graphcast.Journal of Geophysical
Research: Atmospheres, 131(6):e2025JD044852, 2026. doi:https://doi.org/10.1029/2025JD044852.
Taroh Matsuno. A dynamical model of the stratospheric sudden warming.Journal of Atmospheric Sciences, 28(8):1479
– 1494, 1971. doi:10.1175/1520-0469(1971)028<1479:ADMOTS>2.0.CO;2.
Mark P. Baldwin, Blanca Ayarzagüena, Thomas Birner, Neal Butchart, Amy H. Butler, Andrew J. Charlton-Perez,
Daniela I. V . Domeisen, Chaim I. Garfinkel, Hella Garny, Edwin P. Gerber, Michaela I. Hegglin, Ulrike Langematz,
and Nicholas M. Pedatella. Sudden stratospheric warmings.Reviews of Geophysics, 59(1):e2020RG000708, 2021.
doi:https://doi.org/10.1029/2020RG000708.
Mark P. Baldwin and Timothy J. Dunkerton. Stratospheric harbingers of anomalous weather regimes.Science, 294
(5542):581–584, 2001. doi:10.1126/science.1063315.
Joseph Kidston, Adam Scaife, Steven Hardiman, Daniel Mitchell, Neal Butchart, Mark Baldwin, and L. Gray. Strato-
spheric influence on tropospheric jet streams, storm tracks and surface weather.Nature Geoscience, 8:433–440, 05
2015. doi:10.1038/ngeo2424.
M. Jucker, S. Fueglistaler, and G. K. Vallis. Stratospheric sudden warmings in an idealized gcm.Journal of Geophysical
Research: Atmospheres, 119(19):11,054–11,064, 2014. doi:https://doi.org/10.1002/2014JD022170.
10

A PREPRINT
Regan Mudhar, William J. M. Seviour, James A. Screen, Ruth Geen, Neil T. Lewis, and Stephen I. Thomson. Exploring
mechanisms for model-dependency of the stratospheric response to arctic warming.Journal of Geophysical Re-
search: Atmospheres, 129(10):e2023JD040416, 2024. doi:https://doi.org/10.1029/2023JD040416. e2023JD040416
2023JD040416.
G. K. Vallis, G. Colyer, R. Geen, E. Gerber, M. Jucker, P. Maher, A. Paterson, M. Pietschnig, J. Penn, and S. I. Thomson.
Isca, v1.0: a framework for the global modelling of the atmospheres of earth and other planets at varying levels of
complexity.Geoscientific Model Development, 11(3):843–859, 2018. doi:10.5194/gmd-11-843-2018.
Lorenzo M. Polvani and Paul J. Kushner. Tropospheric response to stratospheric perturbations in a
relatively simple general circulation model.Geophysical Research Letters, 29(7):18–1–18–4, 2002.
doi:https://doi.org/10.1029/2001GL014284.
E. A. Lindgren, A. Sheshadri, and R. A. Plumb. Sudden stratospheric warming formation in an idealized general
circulation model using three types of tropospheric forcing.Journal of Geophysical Research: Atmospheres, 123
(18):10,125–10,139, 2018. doi:https://doi.org/10.1029/2018JD028537.
Andrew J. Charlton and Lorenzo M. Polvani. A new look at stratospheric sudden warmings. part i: Climatology and
modeling benchmarks.Journal of Climate, 20(3):449 – 469, 2007. doi:10.1175/JCLI3996.1.
D G Andrews, J R Holton, and C B Leovy.Middle atmosphere dynamics. Academic Press Inc.,Orlando, FL, 01 1987.
Martin Jucker. Scaling of eliassen-palm flux vectors.Atmospheric Science Letters, 22(4):e1020, 2021.
doi:https://doi.org/10.1002/asl.1020.
E. A. Lindgren and A. Sheshadri. The role of wave–wave interactions in sudden stratospheric warming formation.
Weather and Climate Dynamics, 1(1):93–109, 2020. doi:10.5194/wcd-1-93-2020.
Daniel M. Mitchell, Andrew J. Charlton-Perez, and Lesley J. Gray. Characterizing the variability and extremes of the
stratospheric polar vortices using 2d moment analysis.Journal of the Atmospheric Sciences, 68(6):1194 – 1213,
2011. doi:10.1175/2010JAS3555.1.
William J. M. Seviour, Daniel M. Mitchell, and Lesley J. Gray. A practical method to identify dis-
placed and split stratospheric polar vortex events.Geophysical Research Letters, 40(19):5268–5273, 2013.
doi:https://doi.org/10.1002/grl.50927.
Darry N. W. Waugh. Elliptical diagnostics of stratospheric polar vortices.Quarterly Journal of the Royal Meteorological
Society, 123(542):1725–1748, 1997. doi:https://doi.org/10.1002/qj.49712354213.
Geoffrey K. Vallis.Atmospheric and Oceanic Fluid Dynamics: Fundamentals and Large-Scale Circulation. Cambridge
University Press, 2 edition, 2017.
P. Martineau, J. S. Wright, N. Zhu, and M. Fujiwara. Zonal-mean data set of global atmospheric reanalyses on pressure
levels.Earth System Science Data, 10(4):1925–1941, 2018. doi:10.5194/essd-10-1925-2018.
H. J. Edmon, B. J. Hoskins, and M. E. McIntyre. Eliassen-palm cross sections for the troposphere.Journal of
Atmospheric Sciences, 37(12):2600 – 2616, 1980. doi:10.1175/1520-0469(1980)037<2600:EPCSFT>2.0.CO;2.
Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-net: Convolutional networks for biomedical image segmen-
tation. In Nassir Navab, Joachim Hornegger, William M. Wells, and Alejandro F. Frangi, editors,Medical Image
Computing and Computer-Assisted Intervention – MICCAI 2015, pages 234–241, Cham, 2015. Springer International
Publishing. ISBN 978-3-319-24574-4.
Jonathan A. Weyn, Dale R. Durran, and Rich Caruana. Improving data-driven global weather prediction using
deep convolutional neural networks on a cubed sphere.Journal of Advances in Modeling Earth Systems, 12(9):
e2020MS002109, 2020. doi:https://doi.org/10.1029/2020MS002109. e2020MS002109 10.1029/2020MS002109.
Jonathan A. Weyn, Dale R. Durran, Rich Caruana, and Nathaniel Cresswell-Clay. Sub-seasonal forecasting with a
large ensemble of deep-learning weather prediction models.Journal of Advances in Modeling Earth Systems, 13(7):
e2021MS002502, 2021. doi:https://doi.org/10.1029/2021MS002502. e2021MS002502 2021MS002502.
Ryan Keisler. Forecasting global weather with graph neural networks, 2022.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and
Illia Polosukhin. Attention is all you need. In I. Guyon, U. V on Luxburg, S. Bengio, H. Wallach, R. Fergus,
S. Vishwanathan, and R. Garnett, editors,Advances in Neural Information Processing Systems, volume 30. Curran
Associates, Inc., 2017.
Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, and Baining Guo. Swin transformer:
Hierarchical vision transformer using shifted windows, 2021.
11

A PREPRINT
A Detailed dynamics of Isca and elaboration of Eliassen–Palm fluxes
Isca is a modular atmospheric modelling framework designed to support controlled experiments across a hierarchy
of model complexities, from idealised dry dynamical cores to more comprehensive GCM configurations Vallis et al.
[2018]. This makes it particularly suitable for studying how specific physical processes affect atmospheric dynamics
while minimizing confounding effects from unrelated model components.
At each time t, the simulator state is represented by a collection of atmospheric variables defined on a spherical
latitude-longitude-pressure grid,
xt ∈R V×L ϕ×Lλ×Lp ,(5)
where V denotes the number of atmospheric variables, Lϕ the number of latitudes, Lλ the number of longitudes, and
Lp the number of vertical pressure levels. In our experiments, these variables include temperature T , zonal wind u,
and meridional wind v, evaluated on a regular T42 grid corresponding to 64×128 latitude-longitude points and 60
vertical levels. The simulator advances the atmospheric state in discrete time by numerically integrating the underlying
governing equations, producing,
xt+∆t =M(x t),(6)
whereMdenotes the one-step time-evolution operator induced by the chosen ISCAconfiguration.
In this work, we use a dry spectral dynamical-core configuration based on Mudhar et al. [2024]. This setup follows
the Held-Suarez style idealization in the troposphere, where temperature is relaxed toward a prescribed radiative-
equilibrium profile and low-level winds are damped through Rayleigh friction Held and Suarez [1994]. Abstractly, the
continuous-time evolution may be written as,
∂x
∂t =D(x;T eq) +F wave,(7)
where D(·) denotes the dry dynamical-core tendencies, including advection, pressure-gradient forces, Newtonian
relaxation toward the equilibrium temperature profile Teq, and frictional damping, while Fwave denotes additional
imposed forcing terms which for the SSW-disabled case is set to0.
The equilibrium temperature profile is piecewise defined by tropospheric and stratospheric components,
Teq(p, ϕ) =
T trop eq (p, ϕ), p≥p T ,
T strat eq (p, ϕ), p < pT , (8)
where p denotes pressure, ϕ latitude, and pT the tropopause transition pressure. The tropospheric part follows the
standard Held-Suarez relaxation profile, while the stratospheric part follows a modified Polvani-Kushner formula-
tion Polvani and Kushner [2002]. A key control parameter is the stratospheric lapse-rate parameter γ, which controls
the vertical temperature structure of the stratospheric equilibrium profile and thereby influences the mean strength and
variability of the winter polar vortex. The full functional form ofT strat eq is given in Mudhar et al. [2024].
To generate the more dynamically challenging SSW-enabled regime used in this paper, we activate the additional
prescribed heating perturbation following Mudhar et al. [2024] and Lindgren et al. [2018]. This perturbation enters
equation (7) as the imposed tendency Fwave and increases stratospheric wave activity and variability. The perturbation
takes the form of a zonal wave-2 heating pattern in longitude, centred at approximately 45◦N and 400 hPa. This acts to
generate stationary planetary-scale Rossby waves, which propagate upward into the stratosphere and disturb the winter
polar vortex. Such a forcing is required in this model because, in the real atmosphere, planetary waves are generated in
part by flow over topography, which we omit in our idealised setup. However, prescribing the planetary-wave forcing in
this way allows us to control the magnitude of the stratospheric wave forcing and to create two parallel datasets with
and without strong stratospheric variability.
This distinction is visualized in the main text as Figure 1, which shows the zonal-mean zonal wind at 60◦N and 10
hPa over time for the two configurations used in this study as well as absolute vorticity for selected time-indices.
The configuration without additional forcing exhibits a stronger and more stable polar vortex, whereas the forced
configuration displays larger temporal fluctuations and intermittent vortex weakening events characteristic of an
SSW-enabled regime. These two settings form the basis of our machine-learning benchmark: a relatively simple
regime without pronounced stratospheric disruptions, and a more challenging regime in which vertically coupled wave
dynamics are active.
The full planetary configuration is intentionally idealised: there is no land surface, no topography, and no moisture.
Although simplified, this setup is not arbitrary. It is designed to isolate large-scale dry dynamical mechanisms relevant
for stratosphere-troposphere coupling. Although the wind fields are not identical, the idealised model produces a
qualitatively similar large-scale structure, including a strong Northern Hemisphere winter polar vortex.
12

A PREPRINT
A.1 Wave-mean-flow interactions & Eliassen-Palm fluxes
To understand sudden stratospheric warmings, it is not sufficient to consider only the zonal-mean flow. One must
also account for waves and eddies in the flow, since they can transport momentum and heat and thereby influence
the zonal-mean circulation. In atmospheric science, this is typically done by decomposing fields such as temperature
T , zonal wind u, and meridional wind v into a zonal mean and a deviation from that mean. At a fixed latitude,
pressure level, and time, these deviations describe how the fields vary around the globe in longitude. We refer to these
longitude-dependent deviations as eddy fields, which include the planetary-scale waves central to SSW dynamics.
Each field can be decomposed into a mean and a deviation from that mean, for example for zonal wind,
u(λ, ϕ, p, t) =u(ϕ, p, t) +u′(λ, ϕ, p, t),(9)
and similarly for v and T . The zonal mean u represents the background flow, while the deviation u′ captures the
longitudinal wave structure. In this setting, planetary or Rossby waves correspond to large-scale wave-like patterns in
these deviations, that is, coherent alternating structures in wind and temperature around a latitude circle Vallis [2017].
These waves are present in both ISCAconfigurations, but the additional imposed heating perturbation strengthens them
and makes their interaction with the winter stratosphere more pronounced. This matters because the waves do not simply
create local anomalies in T , u, and v; they also transport momentum and heat through the atmosphere. For example,
if poleward meridional wind anomalies v′ tend to occur at the same longitudes as positive zonal-wind anomalies u′,
then the wave field transports zonal momentum poleward. Likewise, if poleward meridional wind anomalies tend to
co-occur with warm temperature anomalies T ′, then the wave field transports heat. These effects are summarized by the
eddy covariances,
u′v′ and v′T ′,(10)
which are zonal averages of products of the longitude-dependent deviations from the zonal mean, evaluated at fixed
time, latitude, and pressure. Here, u′v′ measures the covariance between zonal-wind and meridional-wind anomalies,
while v′T ′ measures the covariance between meridional-wind and temperature anomalies.
Wave-mean-flow interaction refers to the fact that these waves propagate through the atmosphere and can transfer
momentum to the zonal-mean flow when they are absorbed or dissipated. In the winter hemisphere, much of the
wave activity remains confined to the troposphere, but some propagates upward into the stratosphere. When this
upward-propagating wave activity becomes strong enough, it can disturb and weaken the polar vortex. This is one of
the central dynamical ingredients of SSW-like events, and it is therefore highly relevant for the present benchmark.
To analyze the process of wave-mean-flow interaction, we use Eliassen-Palm (EP) flux diagnostics Andrews et al.
[1987]. The first part of the diagnostics is the EP-flux arrow, defined as a vector field in the latitude-pressure space,
F= (F ϕ, Fp),(11)
where Fϕ is the component in the meridional direction and Fp is the component in the vertical pressure direction. In the
present work we make use of the quasi-geostrophic (QG) approximation of the EP-fluxes, meaning that the components
are proportional to the eddy covariances of both momentum and heat,
Fϕ ∝ −u′v′ Fp ∝ v′T ′.(12)
The full implementation of these QG EP-fluxes further accounts for spherical geometry and static stability (see e.g.,
Martineau et al. [2018]), and can be found in the attached code. The direction of the EP flux arrows indicate the relative
importance of the eddy fluxes of heat and momentum. In the case where the eddy dynamics is purely Rossby waves,
the EP-flux arrows indicate how wave activity propagates through latitude-pressure space. An upward arrow indicates
upward propagation, while a poleward arrow indicates propagation toward high latitudes Edmon et al. [1980]. In our
SSW-enabled ISCAconfiguration, stronger upward and poleward propagation into the winter stratosphere is expected,
particularly toward the polar vortex region.
The second part of the diagnostic is the EP-flux divergence term,
∇ ·F= 1 acosϕ ∂(Fϕ cosϕ) ∂ϕ + ∂Fp ∂p ,(13)
where a is the Earth’s radius. The divergence of F measures how the EP-flux arrows change across latitude-pressure
space. Mathematically, the divergence is the sum of the spatial derivatives of the meridional and vertical components
of the vector field, so it compares how much EP-flux enters a small latitude-pressure region with how much leaves
it. If the inflow and outflow are locally balanced, the divergence is zero; if they are not, the divergence is nonzero
and indicates a net accumulation or net export of wave activity. This is physically useful because regions where wave
13

A PREPRINT
activity accumulates or is removed are precisely the regions where it interacts most strongly with the mean flow and can
therefore influence the zonal-mean zonal wind.
In the context of SSWs, one typically expects enhanced upward and poleward EP-flux into the winter stratosphere
together with strong wave forcing in the polar-vortex region. Hence, from a physical perspective, accurately predicting
the atmospheric state prior to and during an SSW is closely related to reproducing the correct wave-mean-flow
interactions. This makes EP-flux diagnostics a useful mechanism-aware complement to standard error metrics. In
particular, they test whether a model predicts not only the correct pointwise values ofT , u, and v, but also the covariance
structure between them that governs realistic wave propagation and mean-flow forcing.
B Machine-learning emulator architectures used in the study
Given simulator-generated trajectories {xt}T t=1, the goal of emulator learning is to approximate the one-step time-
evolution operator of the simulator. That is, we seek a parametric functionf θ such that,
ˆxt+∆t =f θ(xt),(14)
where xt denotes the atmospheric state at time t, ˆxt+∆t the predicted state at the next time step, and θ the learnable
model parameters. In our setting, fθ is implemented by a neural network trained on paired input-target examples
(xt,x t+∆t)extracted from the ISCAsimulations.
Training is performed by optimizing the model parameters to minimize the average prediction loss over the simulator-
generated training set,
θ∗ = arg min
θ
1
N
NX
i=1
L

fθ(x(i) t ),x (i) t+∆t

,(15)
where L is a prediction loss, N is the number of training samples, and the optimization is performed with gradient-based
methods. Thus, the emulator does not explicitly solve the governing physical equations, but instead learns a statistical
approximation of the simulator time-step map from data.
A central question in this work is how the choice of neural-network architecture affects the quality of this approximation.
Although all models ultimately map tensors to tensors, different architecture families encode different assumptions about
spatial locality, vertical coupling, long-range interaction, and the symmetry structure of the data. These architectural
assumptions define the model’sinductive bias, and may become particularly important when the underlying atmospheric
dynamics are more difficult to emulate.
The models differ primarily in how they represent the atmospheric state: 2D architectures operate on the horizontal
latitude-longitude grid while treating pressure levels as channels, 3D architectures operate directly over latitude,
longitude, and pressure, and graph-based models replace the regular grid with either a spherical grid graph or a spherical
mesh.
B.1 Convolutional neural networks
Convolutional neural networks (CNNs) are designed for data defined on regular grids, such as images, videos, or
geophysical fields represented on regular latitude-longitude grids. Their core idea is to learn small local filters that are
applied repeatedly across the domain using the same weights. In this way, the model does not learn a separate set of
parameters for every grid point, but instead learns spatial patterns that can appear anywhere in the field. This makes
CNNs particularly well suited for atmospheric data, where nearby locations are often strongly related and where similar
spatial structures may occur in different regions.
Mathematically, a convolutional layer computes each output value as a weighted sum of values in a local neighborhood
of the input,
Yi,j,cout =
X
a,b,cin
Ka,b,cin,cout Xi+a,j+b,cin +b cout ,(16)
where X is the input tensor, Y is the output tensor, K is a learnable kernel, bcout is a bias term, (i, j)indexes the
spatial grid location, cin and cout index input and output channels, and (a, b)indexes offsets within the local patch
of grid points. For a 3D convolution, the same expression is extended by replacing the horizontal location (i, j)with
a three-dimensional location (i, j, z)and the horizontal offsets (a, b)with three-dimensional offsets (a, b, d), so that
the sum is also taken over neighboring pressure levels. Intuitively, for each grid location (i, j), the layer looks only
at a small surrounding patch of the input, combines these nearby values with learned weights, and produces a new
14

A PREPRINT
representation at that location. The same kernel is used across all grid locations, which is the source of both the
efficiency and the spatial inductive bias of CNNs.
In this benchmark, the 2D CNN treats latitude and longitude as the spatial grid and stacks the atmospheric variables,
and also vertical levels, along the channel dimension. This is computationally efficient, but vertical interactions are
then represented only indirectly through channel mixing. By contrast, a 3D CNN treats the atmosphere as a genuine
three-dimensional field over latitude, longitude, and pressure, so that the convolutional kernels act directly across
vertical as well as horizontal neighborhoods. This gives the model a stronger inductive bias toward local vertical
coupling, at the cost of higher computational and memory requirements.
A related methodological issue is that standard convolutions are approximately translation equivariant. This is useful
for parameter sharing, but it assumes that the same local pattern should be processed similarly at different locations.
For atmospheric fields, this assumption is only partly valid, since the dynamics depend on latitude, pressure level, and
grid geometry. A common relaxation is to augment the prognostic state with fixed positional features such as latitude,
longitude, pressure-level indicators, or sinusoidal coordinate encodings. This retains convolutional weight sharing while
allowing the learned mapping to depend explicitly on position.
Padding defines how the field is extended beyond the computational domain before applying the convolution. For
longitude, periodicity motivates circular padding, whereas latitudinal and vertical boundaries require additional
modelling choices, such as zero, replicated, reflected, or geometry-aware padding.
A particularly important convolutional architecture is the U-Net, which combines local convolutions with an encoder-
decoder structure and skip connections Ronneberger et al. [2015]. By progressively coarsening the spatial resolution
and then reconstructing it, U-Nets can capture both fine-scale and larger-scale structure, making them well suited for
dense prediction tasks on atmospheric fields. Hence, U-Net-based architectures have been widely used as backbones for
data-driven weather and climate prediction, including deep convolutional models applied to gridded global atmospheric
fields Weyn et al. [2020, 2021].
B.2 Graph neural networks
Graph neural networks (GNNs) extend neural-network computation from regular grids to data represented as a graph. A
graph consists of nodes and edges: the nodes represent locations or entities, while the edges specify which of these are
allowed to exchange information. In contrast to CNNs, which assume a fixed rectangular grid and local stencil, GNNs
allow the connectivity structure itself to be chosen by the model designer. This makes them attractive for atmospheric
problems, where one may wish to represent interactions not only on the native latitude-longitude grid, but also on
alternative meshes or multi-resolution spatial discretizations. They are also appealing when working with data naturally
defined on a sphere, since a graph or mesh representation can avoid some of the geometric distortions introduced by
regular latitude-longitude grids, especially toward the poles.
In a GNN, each node carries a feature vector describing the local state, and the network updates these node features
by repeatedly exchanging information along the graph edges. This process is calledmessage passing: at each layer, a
node receives information from its neighbors, combines these incoming messages, and uses them to update its own
representation. A generic message-passing layer can be written as,
h(ℓ+1) i =ϕ (ℓ)

h(ℓ) i ,AGG j∈N(i) ψ(ℓ)(h(ℓ) i ,h (ℓ) j ,e ij)  ,(17)
where h(ℓ) i denotes the feature vector of node i at layer ℓ, N(i) its set of neighboring nodes, eij optional edge features,
ψ(ℓ) a function that computes messages between connected nodes, AGG an aggregation operator such as summation,
and ϕ(ℓ) an update function. Intuitively, this means that each node updates its state by combining its current information
with information received from nearby connected nodes.
For atmospheric emulation, the node features correspond to physical variables such as temperature and wind, edge
features can encode geometric information such as relative distance and direction, and the graph structure specifies
which spatial locations interact directly. Nodes may be placed directly on the latitude-longitude grid, or on a mesh-based
discretization that provides more flexible or multi-scale connectivity. In both cases, we account for the spherical
geometry of the domain by treating longitude as periodic and by using spherical connectivity near the poles, rather than
treating the latitude-longitude grid as a flat rectangular image.
Many modern weather-oriented graph architectures use an encoder-processor-decoder structure: an encoder first maps
the raw atmospheric variables to latent node representations, a graph-based processor performs several rounds of
message passing, and a decoder maps the final latent features back to predicted physical variables. One prominent
example is GraphCast Lam et al. [2023], which uses message passing on a multi-scale spherical mesh for medium-range
15

A PREPRINT
weather prediction; another related example is the graph-based weather forecasting model of Keisler Keisler [2022],
which also represents global atmospheric fields using GNNs. Compared with CNNs, GNNs offer greater flexibility in
how spatial interactions are represented and can naturally accommodate non-regular connectivity patterns, although
they do not exploit regular-grid structure as directly.
A practical issue when applying GNNs to latitude-longitude fields is that the graph connectivity alone does not encode
the orientation or spherical geometry of neighboring nodes. For example, a message-passing layer can aggregate
information from connected nodes, but without positional or edge information it cannot distinguish whether a neighbor
lies to the east, west, north, or south, nor can it account for longitude periodicity or polar geometry. We therefore
augment the graph representation with geometric information. For regular-grid graphs, nodes are assigned trigonometric
latitude-longitude features, and edges are assigned relative displacement and distance features. Longitude is treated
as periodic, and pole-crossing neighbors are handled using spherical wrapping. For mesh-based graphs, nodes are
represented by their Cartesian coordinates on the unit sphere together with trigonometric latitude-longitude features,
while edge attributes encode either global Cartesian displacement and great-circle distance or the sender position
expressed in a receiver-local frame. These features make the message-passing operation direction- and geometry-aware,
while preserving the flexibility of the graph representation.
B.3 Transformers
Transformers operate on data represented as a sequence oftokensrather than directly on a grid Vaswani et al. [2017].
For atmospheric fields, a token is a learned representation of a local patch of the input state. More concretely, the input
tensor is divided into non-overlapping patches, and each patch is mapped to a latent vector of fixed dimension. If xt
denotes the input state, this tokenization step can be written abstractly as
H(0) = Tokenize(xt) +P,(18)
where H(0) ∈R N×d is the resulting sequence of N tokens with embedding dimension d, and P denotes positional
information added to retain the spatial arrangement of the original field. Intuitively, each token summarizes the
information in one local patch of the atmosphere, while the positional encoding tells the model where that patch came
from.
In a 2D transformer, the atmosphere is represented on a latitude-longitude grid with variables and vertical levels stacked
along the channel dimension, so each token corresponds to a spatial patch in latitude and longitude together with all
channels at those locations. In a 3D transformer, the tokenization instead acts on latitude, longitude, and pressure
jointly, so each token represents a three-dimensional atmospheric volume. Thus, analogous to the distinction between
2D and 3D convolutions, the choice of tokenization determines whether vertical structure is handled implicitly through
channels or explicitly as part of the spatial input representation.
The core operation of the transformer is self-attention, which allows tokens to exchange information based on their
learned similarity. Given token representations collected in a matrixH, self-attention computes
Attention(Q,K,V) = softmax
 QK⊤
√
d

V,(19)
where queries Q, keys K, and values V are learned linear projections of H and d is the dimension of the query and key
vectors. Inglobalattention, each token can attend to all other tokens, which allows the model to represent broad spatial
dependencies across the full atmospheric field. Inwindowedattention, as used in Swin-style transformers Liu et al.
[2021], attention is computed only within local windows, which reduces computational cost and introduces a stronger
locality bias. By shifting the window partition between layers, Swin attention still allows information to propagate
across larger spatial scales while retaining much of the efficiency of local processing.
After several layers of attention and nonlinear transformations, the final token representations are mapped back to the
original atmospheric grid through a decoding orde-tokenizationstep,
ˆxt+∆t = DeTokenize(H(L)),(20)
where H(L) denotes the token representations after the final transformer layer. This step reconstructs the predicted
atmospheric field from the sequence of latent patch representations.
Transformer-based architectures have become increasingly common in data-driven weather and climate modelling,
including 3D transformer models for global weather forecasting such as Pangu-Weather Bi et al. [2023] and foundation
models for Earth-system prediction such as Aurora Bodnar et al. [2025].
Relative to CNNs, transformers impose a weaker hard-coded locality bias and can in principle represent broader spatial
dependencies more easily. The distinction between global and windowed attention is therefore important: the former
16

A PREPRINT
emphasizes unrestricted interactions, whereas the latter trades some of this flexibility for greater efficiency and a more
local inductive bias.
C Experimental design and implementation details
This section summarizes the emulator benchmark pipeline, including Isca data generation, model-specific preprocessing,
details on machine learning architectures, training protocols, and evaluation.
C.1 Implementation details of Isca configuration
The two datasets are generated from the same idealized dry Isca configuration and differ only in whether the additional
wave-heating perturbation is active. The no-SSW dataset omits this forcing, while the SSW-enabled dataset includes the
prescribed wave-2 heating perturbation used to enhance planetary-wave activity and stratospheric variability. All other
simulator settings, including horizontal resolution, vertical levels, time step, retained variables, spin-up removal, and
train-validation-test split, are held fixed across the two datasets. The Isca configuration follows Mudhar et al. [2024],
with implementation details provided in the accompanying code repository. A compact summary of the simulator
configuration and preprocessing choices is provided in Table 2.
C.2 Preprocessing of input representation
All input representations are constructed from the same raw Isca output fields. For each dataset, we retain temperature
T , zonal wind u, and meridional wind v on the full pressure–latitude–longitude grid. The raw variables are stored with
dimensions (t, p, ϕ, λ), and the preprocessing selects the same time window, variables, and train-validation-test split.
Specifically, we discard the first 1000 output steps, retain 2500 consecutive states, and split these chronologically into
training, validation, and test states. Normalization statistics are computed from the training split only, separately for
each variable–pressure-level channel over time, latitude, and longitude, and then applied to the validation and test splits.
One-step prediction pairs (xt,x t+1) are formed within each split, so transitions across split boundaries are excluded.
The main difference between model families is therefore not the underlying physical data, but how the atmospheric
state is represented for the neural network.
C.2.1 2D tensor representation
For the 2D convolutional and transformer models, pressure is flattened into the channel dimension rather than retained
as an explicit spatial axis. Each Isca state is therefore stored as a latitude–longitude tensor with variables and pressure
levels stacked as channels, xt ∈R 180×64×128, where 180 = 3×60 corresponds to three prognostic variables on
60 pressure levels. This representation allows the models to operate directly on horizontal structure, while vertical
interactions are represented through channel mixing.
The coordinate features are appended dynamically to the input at load time. They consist of four trigonometric latitude–
longitude channels, sinϕ , cosϕ , sinλ , and cosλ . Thus, the runtime input has 184 channels on the latitude–longitude
grid, while the target remains the 180 prognostic variable–level channels.
C.2.2 3D tensor representation
For the 3D convolutional and transformer models, pressure is retained as an explicit spatial axis rather than flattened
into channels. Each Isca state is therefore stored as a tensor with variables, pressure, latitude, and longitude dimensions,
xt ∈R 3×60×64×128. This representation allows the models to apply local operations directly across neighboring
pressure levels as well as across latitude and longitude.
The coordinate features are appended dynamically to the input at load time. They consist of four trigonometric
latitude–longitude channels,sinϕ , cosϕ , sinλ , and cosλ , together with two pressure-coordinate channels. The pressure
channels are constructed by min–max normalizing pressure p and log-pressure logp across the retained pressure
levels, and then broadcasting these values over latitude and longitude. Thus, the runtime input has 9 channels over the
pressure–latitude–longitude volume, while the target remains the 3 prognostic variables.
C.2.3 Grid MPNN representation
For the grid MPNN, each Isca state is represented as a graph on the native latitude–longitude grid. Each horizontal grid
point is treated as a node, giving N= 64×128 = 8192 nodes. At each node, the three prognostic variables across 60
pressure levels are stacked into a dynamic node-feature vector with 3×60 = 180 features. The saved dynamic state
17

A PREPRINT
tensor therefore has shape Nt ×N×F dyn =N t ×8192×180 , where Nt denotes the number of saved time steps, the
second axis indexes graph nodes, and the last axis indexes dynamic variable–pressure-level features.
The graph connectivity is fixed across time. Nodes are connected using a fixed 8-neighbor connectivity pattern on the
latitude–longitude grid, with periodic wrapping in longitude and spherical wrapping across the poles. For neighbors
that cross a pole, the implementation wraps the connection across the spherical grid by shifting the longitude by
180◦, so that the neighbor is placed consistently on the other side of the pole. This gives a directed regular graph
with 8192×8 = 65536 edges. Each edge is assigned four geometric features. For an edge from sender node j to
receiver node i, these are the normalized Euclidean edge length and the three normalized components of the Cartesian
displacement xj −x i, expressed in a local coordinate basis at the receiver node. This basis consists of the outward
surface-normal direction and the local eastward and northward tangent directions. All four quantities are normalized by
the maximum edge length in the graph.
Static node-coordinate features are appended dynamically to the model input at load time. These consist of sinϕ , cosϕ ,
sinλ , and cosλ , increasing the runtime input from 180 to 184 node features, while the target remains the 180 prognostic
variable–level features.
C.2.4 Mesh MPNN representation
For the mesh MPNN, each Isca state is first represented on the native latitude–longitude grid with Ngrid = 64×
128 = 8192 grid nodes. At each grid node, the three prognostic variables across 60 pressure levels are stacked
into a dynamic feature vector with 3×60 = 180 features. The saved dynamic state tensor therefore has shape
Nt ×N×F dyn =N t ×8192×180 , where Nt denotes the number of saved time steps, the second axis indexes graph
nodes, and the last axis indexes dynamic variable–pressure-level features.
The mesh MPNN then uses a static spherical mesh as an intermediate representation. The model first maps information
from the latitude–longitude grid to nearby mesh nodes, performs message passing on the mesh, and finally maps the
mesh representation back to the original grid. The mesh is constructed by starting from an icosahedron and refining it
four times, giving 2562 nodes at the finest level. The mesh-to-mesh graph uses connections from all refinement levels,
so the processor can exchange information across multiple spatial scales rather than only between neighboring nodes on
the finest mesh.
The static graph contains three edge sets. Grid-to-mesh edges connect each grid node to nearby finest-mesh nodes using
a radius query in unit-sphere Cartesian space. For this configuration, the radius is set to 0.8 times the maximum edge
length of the finest mesh. Mesh-to-mesh edges connect nodes within the multi-resolution mesh. Mesh-to-grid edges
connect each grid node to the three vertices of the finest-mesh triangle that contains it. In this setup, the graph contains
22960 grid-to-mesh edges, 20460 mesh-to-mesh edges, and 24576 mesh-to-grid edges.
Static node-coordinate features are included for both grid and mesh nodes. They consist of Cartesian coordinates on the
unit sphere, x, y, and z, together with trigonometric latitude–longitude features, sinϕ , cosϕ , sinλ , and cosλ . Each
edge is assigned four geometric features. For an edge from sender node j to receiver node i, these are the normalized
Euclidean edge length and the three normalized components of the Cartesian displacement xj −x i, expressed in a
local coordinate basis at the receiver node. This basis consists of the outward surface-normal direction and the local
eastward and northward tangent directions. All four quantities are normalized by the maximum edge length within the
corresponding edge set.
C.3 Selected model configurations
For each architecture and dataset, the final model used in the reported test-set results is the run with the lowest validation
MAE from the corresponding hyperparameter sweep. The sweep spaces are summarized in Tables 4–6. The subsections
below summarize the selected configurations for each architecture family, while the full run logs, validation histories,
and complete module printouts are available at the public Weights & Biases projects linked in the accompanying code
repository.
C.3.1 Simple CNN2D
For the no-SSW dataset, the selected Simple CNN2D used a hidden dimension of 1024, three hidden convolutional
layers, kernel size 7×7 , SiLU activations, lon-lat padding, and no batch normalization. Lon-lat padding means that
longitude is padded circularly to respect periodicity, while latitude is padded by replicating the boundary values. The
model first projects the 184 input channels to 1024 hidden channels using a 1×1 convolution, applies three 7×7
convolutions over the latitude–longitude grid, and then maps back to the 180 prognostic target channels using a final
18

A PREPRINT
1×1 convolution. It was trained with MSE loss, the Adam optimizer, learning rate 10−4, weight decay 10−4, batch
size 5, and 50 epochs. The selected model had154.5M trainable parameters.
For the SSW-enabled dataset, the selected Simple CNN2D used the same hidden dimension, activation, padding,
optimizer, loss, learning rate, weight decay, batch size, and number of epochs, but used six hidden convolutional layers
with kernel size5×5. The selected SSW-enabled model had157.7M trainable parameters.
C.3.2 CNN2D U-Net
For the no-SSW dataset, the selected CNN2D U-Net used a base hidden dimension of 256, max-pooling downsampling,
SiLU activations, lon-lat padding, no batch normalization, and a bottleneck dilation of 3. The model uses an encoder–
decoder structure with skip connections, with channel widths increasing from 256 to 512 and 1024 in the downsampling
path. Both CNN2D U-Net models use 5×5 convolutions at the highest-resolution encoder level, 3×3 convolutions at
the lower-resolution encoder/decoder levels, and dilated 3×3 convolutions in the bottleneck. It was trained with L1
loss, the AdamW optimizer, learning rate 10−3, weight decay 10−4, batch size 5, and 50 epochs. The selected model
had approximately36M trainable parameters.
For the SSW-enabled dataset, the selected CNN2D U-Net used the same activation, padding, downsampling method,
batch-normalization setting, loss, weight decay, batch size, and number of epochs, but increased the base hidden
dimension to 512 and used a bottleneck dilation of 4. This gives channel widths of 512, 1024, and 2048 across the
encoder. It was trained with the Adam optimizer and learning rate 10−4. The selected model had approximately 147M
trainable parameters.
C.3.3 Simple CNN3D
For the no-SSW dataset, the selected Simple CNN3D used a hidden dimension of 64, four hidden convolutional layers,
kernel size 7×7×7 , SiLU activations, lon-lat padding, and no batch normalization. The model first projects the 9
input channels to 64 hidden channels using a 1×1×1 convolution, applies four 3D convolutional layers over pressure,
latitude, and longitude, and then maps back to the 3 prognostic target channels using a final 1×1×1 convolution. For
3D convolutions, lon-lat padding uses circular padding in longitude and replicated padding in latitude and pressure. The
model was trained with MSE loss, the Adam optimizer, learning rate 10−4, weight decay 10−4, batch size 5, and 50
epochs. The selected model had5.6M trainable parameters.
For the SSW-enabled dataset, the selected Simple CNN3D used the same hidden dimension, number of layers, kernel
size, padding, batch-normalization setting, learning rate, weight decay, batch size, number of epochs, and parameter
count. The main differences were that it used GELU activations, L1 loss, and the AdamW optimizer.
C.3.4 CNN3D U-Net
For the no-SSW dataset, the selected CNN3D U-Net used a base hidden dimension of 40, strided-convolution down-
sampling, GELU activations, lon-lat padding, no batch normalization, and a bottleneck dilation of 3. The model uses
an encoder–decoder structure with skip connections, with channel widths increasing from 40 to 80 and 160 in the
downsampling path. Both CNN3D U-Net models use 5×5×5 convolutions at the highest-resolution encoder level,
3×3×3 convolutions at the lower-resolution encoder/decoder levels, and dilated 3×3×3 convolutions in the
bottleneck. It was trained with L1 loss, the Adam optimizer, learning rate 10−3, weight decay 10−4, batch size 5, and
50 epochs. The selected model had approximately3M trainable parameters.
For the SSW-enabled dataset, the selected CNN3D U-Net used the same activation, padding, batch-normalization setting,
optimizer, weight decay, batch size, and number of epochs, but used a base hidden dimension of 50, mean-pooling
downsampling, and a bottleneck dilation of 2. This gives channel widths of 50, 100, and 200 across the encoder. It
was trained with SmoothL1 loss and learning rate 5×10 −4. The selected model had approximately 5M trainable
parameters.
C.3.5 Transformer 2D Global Attention
The Transformer 2D Global Attention model uses the same two-dimensional latitude–longitude representation as the
CNN2D models. The input consists of 180 prognostic channels, corresponding to three variables across 60 pressure
levels, plus four trigonometric coordinate channels. The 64×128 grid is partitioned into non-overlapping 4×2 patches,
which are embedded by a convolution with matching kernel size and stride. This gives a 16×64 token grid, flattened
into 1024 tokens. After adding learned positional embeddings, the tokens are processed by transformer blocks with
pre-normalized eight-head global self-attention, MLP layers, and residual connections. The decoded tokens are mapped
to 180×4×2 values, rearranged to the full spatial grid, and added as a residual update to the prognostic input channels.
19

A PREPRINT
For the no-SSW dataset, the selected model used 10 transformer blocks, hidden dimension 2048, MLP expansion ratio
6, GELU activations, and no dropout or attention dropout. It was trained with SmoothL1 loss, AdamW, learning rate
3×10 −4, weight decay5×10 −4, batch size 5, and 50 epochs, giving679.5M trainable parameters.
For the SSW-enabled dataset, the selected model kept the same patch size, number of blocks, attention heads, activation,
dropout settings, loss, optimizer, weight decay, batch size, and number of epochs, but used hidden dimension 1024,
MLP expansion ratio 8, and learning rate5×10 −4. The selected model had213.9M trainable parameters.
C.3.6 Transformer 2D Swin
The Transformer 2D Swin model uses the same 184-channel two-dimensional input representation as the Transformer
2D Global Attention model. The 64×128 grid is partitioned into non-overlapping 2×2 patches, embedded by
a convolution with matching kernel size and stride, producing a 32×64 token grid with 2048 tokens. Learned
positional embeddings are added before the tokens are processed by Swin transformer blocks adapted from the
torchvision implementation (https://github.com/pytorch/vision/blob/main/torchvision/models/swin_
transformer.py). Instead of applying attention globally, each block applies multi-head self-attention within local
windows, alternating between unshifted and shifted windows to exchange information across window boundaries.
Attention uses learned relative-position biases, followed by MLP layers, pre-normalization, and residual connections. A
linear decoder maps each token to 180×2×2 values, reconstructs the full grid, and adds the result as a residual update
to the prognostic input state.
For the no-SSW dataset, the selected model used hidden dimension 1152, eight transformer blocks, eight attention
heads, MLP expansion ratio 8, GELU activations, no dropout or attention dropout, and 2×4 -token attention windows.
It was trained with SmoothL1 loss, AdamW, learning rate 10−3, weight decay 5×10 −4, batch size 5, and 50 epochs.
The selected model had216.5M trainable parameters.
For the SSW-enabled dataset, the selected model kept the same hidden dimension, patch size, attention heads, activation,
dropout settings, optimizer, weight decay, batch size, and number of epochs, but used 12 transformer blocks, MLP
expansion ratio 6, 4×4 -token attention windows, L1 loss, and learning rate 5×10 −4. The selected model had 259.1M
trainable parameters.
C.3.7 Transformer 3D Global Attention
The Transformer 3D Global Attention model is the direct three-dimensional analogue of the Transformer 2D Global
Attention model. Instead of stacking pressure levels as channels, it operates on the full pressure–latitude–longitude
grid. The input consists of three prognostic state channels and six coordinate channels: sine and cosine encodings of
latitude and longitude, and normalized linear and logarithmic pressure coordinates. This gives nine input channels on a
60×64×128grid.
As in the 2D global-attention model, a strided convolution embeds non-overlapping patches as tokens, learned positional
embeddings are added, and ten transformer blocks apply pre-normalized eight-head global self-attention followed by
MLP layers and residual connections. The only architectural difference is that patching, attention tokens, and decoding
are defined over three-dimensional pressure–latitude–longitude patches. The decoder maps each processed token back
to the three prognostic variables within its patch, reconstructs the full grid, and adds the result as a residual update to
the input state.
For the no-SSW dataset, the selected model used 4×4×4 patches, giving a 15×16×32 token grid, or 7680 tokens.
It used hidden dimension 768, MLP expansion ratio 6, GELU activations, and no dropout or attention dropout. It was
trained with SmoothL1 loss, AdamW, learning rate 10−3, weight decay 5×10 −4, batch size 5, and 50 epochs. The
selected model had101.0M trainable parameters.
For the SSW-enabled dataset, the selected model kept the same number of transformer blocks, attention heads, MLP
expansion ratio, activation, dropout settings, optimizer, learning rate, weight decay, batch size, and number of epochs,
but used hidden dimension 896, 6×4×4 patches, and L1 loss. This gives a 10×16×32 token grid, or 5120 tokens.
The selected model had134.2M trainable parameters.
C.3.8 Transformer 3D Swin
The Transformer 3D Swin model is the three-dimensional analogue of the Transformer 2D Swin model. It operates
directly on the pressure–latitude–longitude grid instead of stacking pressure levels as channels. The input consists of
three prognostic state channels and six coordinate channels: sine and cosine encodings of latitude and longitude, and
normalized linear and logarithmic pressure coordinates, giving nine input channels on a60×64×128grid.
20

A PREPRINT
As in the 3D global-attention transformer, a strided three-dimensional convolution embeds non-overlapping pressure–
latitude–longitude patches as tokens, and a linear decoder reconstructs the full grid as a residual update to the
input state. The difference is that attention is applied locally using three-dimensional shifted windows, adapted
from the torchvision video Swin transformer implementation: https://raw.githubusercontent.com/pytorch/
vision/main/torchvision/models/video/swin_transformer.py. Blocks alternate between unshifted and
shifted windows, allowing information to propagate across window boundaries while keeping attention local in pressure,
latitude, and longitude.
For the no-SSW dataset, the selected model used 4×4×4 patches, giving a 15×16×32 token grid. It used hidden
dimension 768, eight transformer blocks, eight attention heads, MLP expansion ratio 6, GELU activations, no dropout
or attention dropout, and 3×2×4 -token attention windows. It was trained with L1 loss, AdamW, learning rate 10−3,
weight decay5×10 −4, batch size 5, and 50 epochs. The selected model had82.1M trainable parameters.
For the SSW-enabled dataset, the selected model kept the same hidden dimension, patch size, number of blocks,
attention heads, MLP expansion ratio, activation, dropout settings, learning rate, batch size, and number of epochs,
but used3×4×2-token attention windows, SmoothL1 loss, and weight decay10 −4. The selected model had82.1M
trainable parameters.
C.3.9 Grid MPNN
The regular-grid MPNN 2D uses the grid-graph representation described in Section C.2.3. It therefore operates on
8192 latitude–longitude nodes with 184 input features per node: 180 dynamic prognostic features and four static
trigonometric coordinate features. The graph has fixed eight-neighbour directed connectivity with65,536edges, each
carrying four geometric edge features.
The selected model is a gated graph convolutional network with six residual message-passing layers and hidden
dimension 500. In each layer, sender-node, receiver-node, and edge embeddings are combined to update an edge gate,
which controls the contribution of each neighbouring node before aggregation. A decoder predicts a 180-dimensional
residual at each node, which is added to the current prognostic state.
For the no-SSW dataset, the selected configuration used SiLU activations, no dropout, a three-layer node encoder, a
three-layer edge encoder, and a three-layer decoder. It was trained with Adam, learning rate 5×10 −4, and had 8.73M
trainable parameters.
For the SSW-enabled dataset, the selected configuration used SiLU activations, dropout 0.1, a three-layer node encoder,
a two-layer edge encoder, and a two-layer decoder. It was trained with AdamW, learning rate 10−3, and had 8.48M
trainable parameters.
C.3.10 Mesh MPNN
The mesh-based MPNN 2D uses the grid–mesh representation described in Section C.2.4. It follows a grid-to-mesh,
mesh-to-mesh, and mesh-to-grid architecture, where information is first transferred from the native latitude–longitude
grid to the spherical mesh, processed on the multi-resolution mesh graph, and then mapped back to the original grid.
Separate MLP encoders map grid-node features, mesh-node features, and the three edge-feature sets into a common
hidden dimension. The mesh processor then applies gated graph convolutional layers over the multi-resolution mesh
graph. For each edge, sender-node, receiver-node, and edge embeddings are combined to update an edge gate, which
weights the sender message before aggregation. Residual connections are used for both node and edge updates. After
the mesh-to-grid stage, an MLP decoder predicts a 180-dimensional residual update at each grid point, which is added
to the current prognostic state.
For the no-SSW dataset, the selected model used hidden dimension 640, two grid-to-mesh layers, nine mesh-to-mesh
layers, and two mesh-to-grid layers. It used LeakyReLU activations, dropout 0.1, two-layer node encoders, three-layer
edge encoders, and a three-layer decoder. The selected model had31.1M trainable parameters.
For the SSW-enabled dataset, the selected model used hidden dimension 512, three grid-to-mesh layers, nine mesh-to-
mesh layers, and two mesh-to-grid layers. It used SiLU activations, no dropout, two-layer node encoders, three-layer
edge encoders, and a three-layer decoder. The selected model had21.2M trainable parameters.
C.4 Training budget and computational constraints
To make the architecture comparison as controlled as possible, all model families were trained under a shared one-step
forecasting protocol and a fixed hyperparameter-sweep budget. For each architecture and dataset, we ran a Bayesian
21

A PREPRINT
sweep with a run cap of 50 configurations and selected the model with the lowest validation MAE. The corresponding
search spaces are reported in Tables 4–6.
The goal of this setup is not to optimize each architecture family to its absolute performance limit, but to compare
representative implementations under comparable tuning effort. This is important because the model classes differ
substantially in parameter count, memory footprint, and optimization behavior. Using the same sweep budget reduces
the risk that observed differences are driven mainly by unequal architecture-specific tuning effort rather than by the
inductive biases being tested.
All selected models were trained for 50 epochs with batch size 5, mixed-precision training, and a fixed random seed.
Training was performed on a single GPU per run, primarily using an NVIDIA RTX 5080.
22

A PREPRINT
Figure 6: Pressure–latitude structure of persistence mean absolute error for temperature, zonal wind, and meridional
wind in the no-SSW and SSW-enabled regimes in the hold-out test set. Persistence errors are substantial in both regimes,
showing that even over the 3-hour prediction horizon the grid-point fields undergo appreciable local evolution. The
largest errors are concentrated in the Northern Hemisphere stratosphere and are generally stronger in the no-SSW regime,
especially for the wind components. This likely reflects the stronger and more coherent polar vortex in the unforced
configuration, where small displacements of sharp wind gradients can produce large grid-point errors. Persistence
provides a useful reference for short-term local variability, but should not be interpreted as a complete measure of
dynamical difficulty.
23

A PREPRINT
Figure 7: Latitude–pressure structure of temperature mean absolute error for all emulator architectures. This diagnostic
complements the main-text by showing how prediction errors vary with latitude and pressure for the temperature
component.
24

A PREPRINT
Figure 8: Latitude–pressure structure of zonal wind mean absolute error for all emulator architectures. This diagnostic
complements the main-text by showing how prediction errors vary with latitude and pressure for the zonal wind
component.
25

A PREPRINT
Figure 9: Latitude–pressure structure of meridional wind mean absolute error for all emulator architectures. This
diagnostic complements the main-text by showing how prediction errors vary with latitude and pressure for the
meridional wind component.
26

A PREPRINT
Figure 10: EP-flux diagnostics for 3D architectures averaged over the 10 days preceding the held-out SSW event
described in section 3.3 in the main text. The upper row shows EP-flux vectors overlaid on EP-flux divergence for the
true simulator trajectory and model predictions. The lower row shows divergence error, defined as true minus predicted
divergence. The dashed contour marks the dynamical tropopause, defined here as the zonal- and time-mean contour of
absolute potential vorticity.
27

A PREPRINT
Figure 11: EP-flux diagnostics for 2D architectures averaged over the 10 days preceding the held-out SSW event
described in section 3.3 in the main text. The upper row shows EP-flux vectors overlaid on EP-flux divergence for the
true simulator trajectory and model predictions. The lower row shows divergence error, defined as true minus predicted
divergence. The dashed contour marks the dynamical tropopause, defined here as the zonal- and time-mean contour of
absolute potential vorticity.
28

A PREPRINT
Figure 12: EP-flux diagnostics for graph-based architectures averaged over the 10 days preceding the held-out SSW
event described in section 3.3 in the main text. The upper row shows EP-flux vectors overlaid on EP-flux divergence
for the true simulator trajectory and model predictions. The lower row shows divergence error, defined as true minus
predicted divergence. The dashed contour marks the dynamical tropopause, defined here as the zonal- and time-mean
contour of absolute potential vorticity.
29

A PREPRINT
Figure 13: EP-flux diagnostics for the 3D U-Net after removing the explicit 10 hPa input level, which otherwise
lies close to an existing 10.24 hPa level and causes the interesting artifact shown in the main text. The upper panels
show EP-flux vectors overlaid on EP-flux divergence for the true simulator trajectory and model prediction, while the
lower panels show the divergence error. The narrow 10 hPa error band seen in Figure 10 disappears, supporting its
interpretation as a discretization-related artifact rather than a dynamical EP-flux error.
30

A PREPRINT
Figure 14: Data-scaling experiment for the selected training configuration. Test MAE decreases monotonically with
training set size, with diminishing improvements at larger sample sizes. The training set size of 2000 was chosen to
make it computationally feasible to experiment and hyperparameter-tune across many architectures.
31

A PREPRINT
Table 2: Summary of the ISCAconfiguration and dataset construction used for emulator training. The two datasets share
the same base simulator configuration and differ only in whether the additional wave-heating perturbation is active.
Attribute Configuration
ISCAsimulationBase simulator ISCAdry spectral dynamical core with Held–Suarez troposphere and Polvani–
Kushner stratosphere Held and Suarez [1994], Polvani and Kushner [2002]
Horizontal resolution T42 (64×128latitude–longitude equivalent)
Vertical levels 60 pressure levels spanning 0.02–900 hPa; 38 levels above 100 hPa
Simulation length∼6 years
No-SSW dataset Additional wave forcing absent
SSW-enabled dataset Additional wave forcing present Mudhar et al. [2024]
Data processingVariables retainedT,u,v
Sampling interval 3 hours
Spin-up removal First 1000 3-hourly time steps removed
Prediction pairs(x t,x t+3h)
Data split Chronological2500training,249validation,249test samples
Normalization Per-variable and per-pressure-level normalization using training statistics
32

A PREPRINT
Table 3: Model families included in the benchmark and the main inductive-bias dimension each is intended to test.
Model family Input Model Inductive bias Explicit vertical
coupling
Baseline Full atmospheric state Persistence Identity forecast No
2D convolution Latitude–longitude tensor with pressure levels and
variables as channels
SimpleCNN2D Local horizontal convolutions No
U-Net2D Local multi-scale horizontal con-
volutions
No
3D convolution Latitude–longitude–pressure tensor with variables
as channels
SimpleCNN3D Local 3D convolutions Yes
U-Net3D Local multi-scale 3D convolu-
tions
Yes
2D transformer Latitude–longitude tensor with pressure levels and
variables as channels. 2D patches used for tok-
enization.
Global ViT-2D Global self-attention No
Swin ViT-2D Windowed self-attention No
3D transformer Latitude–longitude–pressure tensor with variables
as channels. 3D patches used for tokenization.
Global ViT-3D Global self-attention Yes
Swin ViT-3D Windowed self-attention Yes
Grid GNN Regular-grid graph with pressure levels and vari-
ables as node features and relative position and
distance as edge features
Encoder–MPNN–
decoder
Message passing on regular-grid
graph
No
Mesh GNN Grid-to-mesh-to-grid representation with pressure
levels and variables stacked in node features and
relative position and distance as edge features
GraphCast-style
mesh model
Message passing on spherical
mesh
No
33

A PREPRINT
Table 4: Hyperparameter search spaces for the convolutional models. The same search spaces were used for both the
SSW-enabled and no-SSW datasets. All sweeps used Bayesian optimization with a run cap of 50 and selected the
configuration with the lowest validation MAE.
Model Hidden
dim.
Num. lay-
ers
Convolution Batch
norm
Activation Loss Optimizer Learning rate
SimpleCNN2D
128
256
512
1024
2
3
4
5
6
Kernel size:
3
5
7
true
false
GELU
ReLU
SiLU
L1
SmoothL1
MSE
AdamW
Adam
Yogi
10−3
5×10−4
10−4
U-Net2D
Base:
64
128
256
512
–
Bottleneck
dilation:
1, 2, 3, 4
Downsampling:
strided conv
max pool
mean pool
true
false
GELU
ReLU
SiLU
L1
SmoothL1
MSE
AdamW
Adam
Yogi
10−3
5×10−4
10−4
SimpleCNN3D
16
32
64
2
3
4
Kernel size:
3
5
7
true
false
GELU
SiLU
ReLU
L1
SmoothL1
MSE
AdamW
Adam
Yogi
10−3
5×10−4
10−4
U-Net3D
Base:
16
32
40
50
–
Bottleneck
dilation:
1, 2, 3
Downsampling:
mean pool
max pool
strided conv
true
false
SiLU
GELU
LeakyReLU
L1
SmoothL1
MSE
AdamW
Adam
Yogi
10−3
5×10−4
10−4
34

A PREPRINT
Table 5: Hyperparameter search spaces for the graph-based models. The same search spaces were used for both the
SSW-enabled and no-SSW datasets. All sweeps used Bayesian optimization with a run cap of 50 and selected the
configuration with the lowest validation MAE.
Model Hidden
dim.
Node en-
coder
Edge en-
coder
De-coder Message passing Drop-out Activa-tion Loss Optimizer Learning rate
Grid
GNN
256
300
350
400
450
500
2
3
2
3
2
3
GNN layers:
4
6
8
0
0.1
SiLU
GELU
Leaky-
ReLU
L1
SmoothL1
MSE
AdamW
Adam
2.5×10−3
10−3
5×10−4
2×10−4
Mesh
GNN
256
512
640
768
2
3
2
3
2
3
Grid–mesh:
2
3
Mesh–mesh:
5
7
8
9
10
Mesh–grid:
2
3
0
0.1
GELU
ReLU
SiLU
Leaky-
ReLU
L1
SmoothL1
MSE
AdamW
Adam
5×10−3
2.5×10−3
10−3
5×10−4
35

A PREPRINT
Table 6: Hyperparameter search spaces for the transformer models. The same search spaces were used for both the
SSW-enabled and no-SSW datasets. All sweeps used Bayesian optimization with a run cap of 50 and selected the
configuration with the lowest validation MAE.
Model Hidden dim. Num. lay-
ers
Num.
heads
MLP ra-
tio
Patch size Window size Loss Optimizer Learning
rate
Weight decay
Global ViT-
2D
512
1024
1280
1536
2048
4
6
8
10
12
4
8
3
4
6
8
Height:
4
8
Width:
2
4
8
– SmoothL1 L1 AdamW
10−4
3×10−4
5×10−4
10−3
10−4
5×10−4
Swin ViT-
2D
768
896
1024
1152
1280
1536
1792
2048
8
10
12
4
8
6
8
Height:
2
4
Width:
2
4
Height:
2
4
Width:
2
4
SmoothL1
L1 AdamW
3×10−4
5×10−4
10−3
10−4
5×10−4
Global ViT-
3D
640
768
896
1024
1280
8
10
12
– 4 6
Depth:
4
5
6
Height:
4
8
Width:
4
8
– SmoothL1 L1 AdamW
10−4
3×10−4
5×10−4
10−3
10−4
5×10−4
Swin ViT-
3D
768
896
1024
8
10
12
– 6 8
Depth:
4
5
Height:
4
8
Width:
4
8
Height:
2
4
Width:
2
4
SmoothL1
L1 AdamW
3×10−4
5×10−4
10−3
10−4
5×10−4
36
