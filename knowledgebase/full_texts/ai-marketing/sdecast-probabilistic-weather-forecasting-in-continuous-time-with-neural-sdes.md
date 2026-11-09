---
title: 'SDECast: Probabilistic Weather Forecasting in Continuous Time with Neural SDEs'
url: https://arxiv.org/abs/2610.03313
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: NeurIPS 2026
authors:
- Maria Marchenko
- Martin Andrae
- Fredrik Lindsten
- Christian A. Naesseth
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.03313
pages: 14
chars: 29881
fetched_at: '2026-11-08T13:25:08+00:00'
kb_version: 1
---

# SDECast: Probabilistic Weather Forecasting in Continuous Time with Neural SDEs

SDECast: Probabilistic Weather Forecasting in
Continuous Time with Neural SDEs
Maria Marchenko∗
University of Amsterdam
maria.m.m.marchenko@gmail.com
Martin Andrae∗
Linköping University, Sweden
martin.andrae@liu.se
Fredrik Lindsten†
Linköping University, Sweden
fredrik.lindsten@liu.se
Christian A. Naesseth †
University of Amsterdam
christian.a.naesseth@uva.nl
Abstract
Existing machine learning weather forecasting models typically generate forecasts
through autoregressive rollouts at a fixed temporal resolution. While highly ef-
ficient for long-range prediction, this formulation can suffer from severe error
accumulation when used with shorter time steps and does not explicitly encode the
locality and temporal continuity of atmospheric dynamics. To address these limi-
tations, we introduceSDECast, a Neural Stochastic Differential Equation (SDE)
framework for continuous-time probabilistic weather forecasting. SDECast extends
SDE Matching to learn stochastic dynamics directly in physical space, without
requiring repeated SDE simulation during training. On a simulated geophysical
flow, we show that SDECast recovers meaningful drift dynamics and faithfully
reproduces the underlying continuous-time behavior. We then demonstrate its scal-
ability to global weather forecasting at hourly resolution, where SDECast produces
skillful probabilistic forecasts for lead times of up to five days.
1 Introduction
Weather forecasting is a problem with broad societal impact: it informs early warning systems,
supports energy planning, and shapes the daily choices of billions of people. While physics-based
Numerical Weather Prediction (NWP) has been the dominant approach for decades, data-driven
methods have recently matched or exceeded NWP accuracy at a fraction of the computational cost.
This progress spans both deterministic and probabilistic forecasting, with state-of-the-art models
relying on generative methods to model the distribution of possible atmospheric states [1–4].
Despite this progress, current machine-learning approaches have several limitations. Unlike physics-
based models, which evolve the atmosphere by solving Partial Differential Equations (PDEs), Machine
Learning Weather Prediction (MLWP) models rely on autoregressive rollouts of a learned one-step
predictor pθ(xt|xt−1). While this enables efficient long-range forecasting, it can suffer from severe
error accumulation when applied with shorter timesteps [5]. Moreover, it fails to exploit the inductive
biases of locality and temporal continuity that are naturally encoded in differential equations. Neural
Ordinary Differential Equations (ODEs) have been explored as an alternative for weather modeling,
but they are deterministic [6–8] or expensive to train due to their simulation-based loss [9].
A related but relatively unexplored class of models is Neural Stochastic Differential Equations
(SDEs). Like Neural ODEs, these models parameterize the system dynamics through a drift term, but
∗Equal contribution
†Equal advising
40th Conference on Neural Information Processing Systems (NeurIPS 2026). Workshop: AI for Stochastic Dynamics /
Sim2Science.
arXiv:2610.03313v1  [stat.ML]  2 Oct 2026

additionally introduce stochasticity via a diffusion term, enabling principled probabilistic forecasting
and efficient ensemble generation. Neural SDEs have traditionally been learned from either finely
resolved trajectories [10] or objectives that require repeated SDE simulation during training [11],
limiting their application to high-dimensional systems. Recently, SDE Matching [12] introduced
a simulation-free objective for learning latent SDEs from discrete time observations. In this work,
we adapt this framework to learn stochastic dynamics directly in physical space and investigate its
application to high-dimensional weather forecasting.
1.1 Contributions
We presentSDECast, a Neural SDE framework for probabilistic weather forecasting. In summary,
the strength and novelty of SDECast lie in its following capabilities:
(i) Continuous-time forecasting, enabling ensemble generation at arbitrary lead times through
stochastic trajectories from a single learned dynamical model.
(ii) Interpretable physical-space dynamics, encoding the locality and temporal continuity
inherent to differential equations through explicit drift and diffusion functions.
(iii) Simulation-free training, scaling Neural SDE learning to high-dimensional weather fore-
casting without repeated SDE simulation during optimization.
2 Method
SDECast adapts SDE Matching [12] to learn stochastic continuous-time dynamics in a scalable way.
Our objective is to learn an SDE that governs the evolution of the physical state xt. However, the
simulation-free training objective of SDE Matching is formulated in terms of an auxiliary latent
process zt. We therefore introduce such a process to construct the training objective, but constrain it
to coincide with the physical state at observation times. This makes the learned prior SDE directly
interpretable as a model of the physical dynamics.
We first describe the simulation-free SDE Matching framework and then introduce our physical-space
posterior parameterization.
2.1 Simulation-free SDE Learning
Let X={x ti }N i=0, 0 =t 0 < t1 <· · ·< tN =T denote a discretely observed trajectory of the
physical system. We introduce a latent processz t governed by thePrior SDE
dzt =h θ(zt, t) dt+gθ(zt, t) dWt,(1)
where hθ and gθ parameterize the drift and diffusion, respectively. This is the SDE used to generate
forecasts at inference times. Following SDE Matching, we introduce thePosterior SDE
dzt =f φ,θ(zt, t;X) dt+gθ(zt, t) dWt,(2)
which shares its diffusion coefficient with the prior SDE, but conditions its drift on the observed
trajectory X. The posterior SDE can be interpreted as a variational approximation of the true posterior
over trajectories induced by the prior equation 1 coupled with an observation likelihood pθ(xt |z t).
It can also be seen as a controlled version of the prior SDE, modifying its dynamics to be consistent
with the observed trajectory X. Since the prior and posterior share the same diffusion coefficient, this
controlu θ,φ is defined implicitly by
fφ,θ(zt, t;X) =hθ(zt, t) +gθ(zt, t)uθ,φ(zt, t,X).(3)
The variational objective penalizes the norm of the control while also reconstructing the observations:
Ldyn =E qφ(Z|X)
"Z T
0
1
2 ∥uθ,φ(zt, t,X)∥2 2 dt
#
,L rec =E qφ(Z|X)
" NX
i=0
−logp θ(xti |z ti )
#
.(4)
Both terms are minimized jointly with respect to θ and φ. Direct evaluation of this objective
would normally require repeatedly simulating the posterior SDE. SDE Matching avoids this by
parameterizing its marginalsq φ(zt|X)directly as
zt =F φ(ε, t,X),ε∼ N(0,I).(5)
2

Assuming that Fφ is differentiable with respect to t and ε, and invertible with respect to ε, this
induces an analytical expression for the posterior drift fφ,θ in equation 3. Consequently, the loss in
equation 4 can be estimated by sampling (t,ε) and evaluating Fφ, without integrating the posterior
SDE. For more details on this we refer to Appendix section A.
2.2 Physical-space SDE
The general SDE Matching formulation remains a latent-variable model: the latent state zt need not
correspond to the physical state, and the posterior qφ(zt |X) may depend on the complete observed
trajectory. We instead seek an SDE whose state can be identified with the physical state of the system.
To establish this connection, we choose the highly concentrated observation model
pθ(xt |z t) =N(x t;z t, δ2I),(6)
where δ≪1 is a fixed, small constant. For sufficiently small δ, the posterior at an observation
time concentrates near the corresponding physical state. Consequently, the posterior between two
consecutive observations is expected to depend predominantly on the observations that bracket that
interval, rather than on the entire trajectory. Motivated by this, we restrict the variational family qφ,
imposing a Markovian conditional independence structure:
qφ(zt |X) =q φ(zt |x ti ,x ti+1 ), t∈(t i, ti+1), q φ(zti |X) =q φ(zti |x ti ).(7)
This restriction avoids conditioning on the complete trajectory and allows the posterior to be evaluated
independently on each observation interval.
For t∈[t i, ti+1], define the normalized time αt = t−ti ti+1−ti . We realize the local variational family
using a Gaussian posterior
Fφ(ε, t,X) = (1−α t)xti +α txti+1 +δε
+α t(1−α t)

µφ(t,x ti ,x ti+1 ) +σ φ(t,x ti ,x ti+1 )ε

(8)
The linear term connects the neighboring observations, while µφ and σφ model the conditional mean
correction and uncertainty between them. The factor αt(1−α t) makes both corrections vanish at
the interval endpoints, ensuring that zti ∼ N(xti , δ2I). This anchors the variational posterior to the
concentrated observation model at each observation time, while allowing flexible stochastic dynamics
between observations. Inserting this parametrization into the reconstruction term yields
Lrec =
NX
i=0
Eqφ(zti |X)
 1
2δ2 ∥xti −z ti ∥2 2 + d 2 log(2πδ 2)  = (N+ 1)d 2  1 + log(2πδ2)  .(9)
Since δ is fixed, this term is constant with respect to the learnable parameters and can therefore be
omitted during optimization. At inference time, we initialize the prior SDE in equation 1 from the
latest observed physical state and simulate it forward. Its trajectories provide forecasts at arbitrary
lead times, while independent Wiener paths produce probabilistic forecast ensembles.
3 Experiments
To assess its performance across both simulated and real-world settings, we evaluate SDECast on the
Surface Quasi-Geostrophic (SQG) system [13] and on global weather forecasting using ERA5 [14].
Further experimental and implementation details are provided in Appendix section B.
3.1 Surface Quasi-Geostrophic Dynamics
We first evaluate SDECast on the SQG system, a widely used model of turbulent geophysical flows.
Despite its relative simplicity, SQG captures key properties of geophysical turbulence, including sen-
sitivity to initial conditions and interactions across multiple scales, while remaining computationally
tractable [13]. Moreover, because the data are generated by a known numerical simulator, this setting
allows us to evaluate not only forecast quality but also whether SDECast recovers the underlying
continuous-time dynamics.
We compare SDECast with an autoregressive conditional flow-matching model (CFM). We also
consider an ablation in which the learnable correctionsµφ and σφ are removed from Fφ, such that the
3

Figure 1: The RMSE (↓), CRPS (↓), SSR for experiments on SQG.
Figure 2: Comparison of the true drift, SDECast drift, and the six-hour finite-difference estimate.
prior SDE is learned against a fixed linear variational posterior. Since the SQG system is autonomous,
we remove the explicit time conditioning from the prior drift and diffusion. We parameterize gθ and
σφ as diagonal matrices, and further restrictg θ to be constant and independent of the state.
We train all models using snapshots separated by six hours, but evaluate their forecasts at one-hour
resolution. As shown in fig. 1, SDECast produces stable and skillful rollouts over multiple forecast
steps. Compared with the autoregressive flow-matching baseline, SDECast obtains higher RMSE and
CRPS, but maintains an almost ideal spread-skill ratio (SSR). Crucially, it generates forecasts at a
substantially finer temporal resolution than that observed during training, whereas CFM is restricted
to its trained resolution. Replacing the learned posterior with the fixed linear posterior substantially
degrades performance, highlighting the importance of a learnable posterior.
Access to the numerical SQG simulator allows us to compare the learned prior drift with the true drift.
In fig. 2, we compare both quantities alongside a six-hour finite-difference estimate. The learned
drift closely resembles the true drift and provides a more faithful description of the instantaneous
dynamics than the finite-difference estimate, indicating that SDECast can recover continuous-time
behavior from coarsely sampled observations. The learned drift nevertheless underrepresents the
highest spatial frequencies, as expected: under coarse temporal sampling the fastest dynamics are only
weakly resolved, and SDECast may attribute part of this high-frequency variability to stochasticity
rather than to the deterministic drift. Thus, although the underlying SQG simulator is deterministic,
the learned SDE provides an effective stochastic representation of its unresolved chaotic dynamics.
Consistent with this, removing the diffusion at inference time, denoted SDECast (deterministic),
substantially degrades forecast performance and produces overly smooth, mean-like trajectories.
3.2 Global Weather Forecasting with ERA5
We additionally evaluate SDECast on global weather forecasting at one-hour resolution for lead times
of up to five days. We use the ERA5 reanalysis dataset [14], spatially downsampled to a resolution of
5.625◦. We consider five atmospheric variables: 500 hPa geopotential (z500), 850 hPa temperature
(t850), 2 m temperature (t2m), and the 10 m wind components (u10andv10).
We compare SDECast with four data-driven and continuous-time forecasting approaches.AR-1his a
conditional diffusion model trained to predict one-hour transitions and rolled out autoregressively.
ARCI-24-1h[5] is trained directly across lead times from one to 24 hours.DYffusion[15] is trained
on the same range of lead times and uses an iterative forecasting procedure. Finally,ClimODE[6]
4

Figure 3: The RMSE (↓), CRPS (↓), SSR oft850for experiments on ERA5.
Figure 4: Continuity of dynamics in Northwest Europe ERA5 square. Mean and standard deviation
(denotedσ) are computed from a 24-member rollout.
learns continuous-time weather dynamics using a physics-informed Neural ODE. All models are
trained and evaluated using hourly ERA5 data, although we report ClimODE only from six-hour lead
times because results at shorter lead times are unavailable.
We use the same SDECast parameterization as in the SQG experiment, but condition the drift and
diffusion on the time of day and time of year to account for diurnal and seasonal variability. We
further allow the diffusion coefficient gθ to vary spatially, enabling the model to represent differences
in forecast uncertainty across locations, such as between land and ocean. The learned diffusion
magnitude is visualized in fig. 6 and exhibits meaningful spatial variation.
As shown in fig. 3, SDECast produces stable and skillful probabilistic forecasts throughout the
evaluation horizon. Crucially, despite being trained on the same hourly data, SDECast substantially
outperforms the one-hour autoregressive baseline at longer lead times. This demonstrates that its
continuous-time formulation supports high temporal resolution without suffering from the severe
error accumulation observed in repeated one-hour autoregressive rollouts. SDECast further improves
on ClimODE and is comparable to DYffusion, while remaining behind the specialized ARCI-24-1h
model. This difference may be partly explained by the model inputs: SDECast and DYffusion
assume Markovian dynamics and propagate a single state, whereas ARCI-24-1h conditions on the
two previous states, providing access to additional temporal information.
To examine the learned continuous-time behavior more closely, we visualize SDECast trajectories
for a single spatial location in fig. 4. The generated trajectories follow the overall evolution of the
ground truth while exhibiting meaningful ensemble variation, illustrating how SDECast represents
both temporal evolution and forecast uncertainty at an hourly resolution.
4 Conclusions
We introducedSDECast, a simulation-free Neural SDE framework for continuous-time probabilistic
weather forecasting. By adapting SDE Matching to physical-space dynamics, SDECast learns explicit
drift and diffusion functions from discretely observed trajectories and generates forecast ensembles at
arbitrary temporal resolutions.
5

Experiments on SQG and ERA5 demonstrate SDECast’s ability to recover continuous-time dynamics
and scale to global weather forecasting, highlighting Neural SDEs as a promising alternative to fixed-
step autoregressive models. Current limitations include simplified posterior and diffusion-coefficient
parameterizations and a limited experimental scope, motivating future work in this direction.
Acknowledgments and Disclosure of Funding
This research is financially supported by the Swedish Research Council (grant no: 2024-05011), the
Wallenberg AI, Autonomous Systems and Software Program (W ASP) funded by the Knut and Alice
Wallenberg Foundation, and the Excellence Center at Linköping–Lund in Information Technology
(ELLIIT). Our computations were enabled by the Berzelius resource at the National Supercomputer
Centre, provided by the Knut and Alice Wallenberg Foundation.
References
[1] Kaifeng Bi et al. “Accurate Medium-Range Global Weather Forecasting with 3D Transformer”.
In:Nature619.7970 (2023), pp. 533–538.
[2] Remi Lam et al. “Learning skillful medium-range global weather forecasting”. In:Science
382.6677 (2023), pp. 1416–1421.
[3] Ilan Price et al. “Probabilistic weather forecasting with machine learning”. In:Nature637.8044
(Jan. 2025), pp. 84–90.ISSN: 1476-4687.DOI: 10 . 1038 / s41586 - 024 - 08252 - 9.URL:
https://doi.org/10.1038/s41586-024-08252-9.
[4] Ferran Alet et al.Skillful joint probabilistic weather forecasting from marginals. 2025. arXiv:
2506.10772 [cs.LG].URL:https://arxiv.org/abs/2506.10772.
[5] Martin Andrae et al. “Continuous Ensemble Weather Forecasting with Diffusion models”. In:
The Thirteenth International Conference on Learning Representations (ICLR 2025), Singapore,
April 24–28, 2025. OpenReview.net, 2025.URL: https://openreview.net/forum?id=
ePEZvQNFDW.
[6] Yogesh Verma et al. “ClimODE: Climate and Weather Forecasting with Physics-informed
Neural ODEs”. In:The Twelfth International Conference on Learning Representations. 2024.
URL:https://openreview.net/forum?id=xuY33XhEGR.
[7] Yeeun Seong et al. “RainODE: Continuous-Time Precipitation Forecasting with Latent Neural
ODEs”. In:arXiv preprint arXiv:2606.29855(2026).
[8] Shuangshuang He et al. “FlowCast-ODE: Continuous Hourly Weather Forecasting with Dy-
namic Flow Matching and ODE Solver”. In:arXiv preprint arXiv:2509.14775(2025).
[9] Dmitrii Kochkov et al. “Neural general circulation models for weather and climate”. In:Nature
632.8027 (Aug. 2024), pp. 1060–1066.ISSN: 1476-4687.DOI: 10 . 1038 / s41586 - 024 -
07744-y.URL:https://doi.org/10.1038/s41586-024-07744-y.
[10] Peter Craigmile et al. “Statistical inference for stochastic differential equations”. In:Wiley
Interdisciplinary Reviews: Computational Statistics15.2 (2023).
[11] Xuechen Li et al. “Scalable Gradients for Stochastic Differential Equations”. In:International
Conference on Artificial Intelligence and Statistics. 2020.
[12] Grigory Bartosh et al. “SDE Matching: Scalable and Simulation-Free Training of Latent
Stochastic Differential Equations”. In:Forty-second International Conference on Machine
Learning. 2025.URL:https://openreview.net/forum?id=0Hd1lh52Fi.
[13] Ross Tulloch and K. Shafer Smith. “Quasigeostrophic Turbulence with Explicit Surface
Dynamics: Application to the Atmospheric Energy Spectrum”. In:Journal of the Atmospheric
Sciences66.2 (2009), pp. 450–467.DOI: 10 . 1175 / 2008JAS2653 . 1.URL: https : / /
journals.ametsoc.org/view/journals/atsc/66/2/2008jas2653.1.xml.
[14] Hans Hersbach et al. “The ERA5 Global Reanalysis”. In:Quarterly Journal of the Royal
Meteorological Society146.730 (2020), pp. 1999–2049.
[15] Salva Rühling Cachay et al. “DYffusion: A Dynamics-informed Diffusion Model for
Spatiotemporal Forecasting”. In:Advances in Neural Information Processing Systems.
6

Ed. by A. Oh et al. V ol. 36. Curran Associates, Inc., 2023, pp. 45259–45287.URL:
https : / / proceedings . neurips . cc / paper _ files / paper / 2023 / file /
8df90a1440ce782d1f5607b7a38f2531-Paper-Conference.pdf.
[16] Stephan Rasp et al. “WeatherBench 2: A Benchmark for the Next Generation of Data-Driven
Global Weather Models”. In:Journal of Advances in Modeling Earth Systems16.6 (2024).
e2023MS004019 2023MS004019, e2023MS004019.DOI: https://doi.org/10.1029/
2023MS004019. eprint: https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.
1029/2023MS004019.URL: https://agupubs.onlinelibrary.wiley.com/doi/abs/
10.1029/2023MS004019.
7

A Details on SDE Matching
For each t and X, the map Fφ transports samples from p(ε) to the posterior marginal qφ(zt |X) .
Provided that Fφ is differentiable with respect tot and ε, and invertible with respect toε, the posterior
process admits an SDE representation whose drift is given by
fφ,θ(zt, t;X) = ˙Fφ(F −1 φ (zt, t,X), t,X) +Gθ(zt, t)∇zt logq φ(zt |X) +∇ zt ·G θ(zt, t)(10)
where Gθ(zt, t) =1 2 g(zt, t)g⊤ θ (zt, t). Consequently, samples and posterior-drift evaluations can be obtained from Fφ without numerically integrating equation 2 during training. Since Fφ is invertible
with respect toε, the score can be computed via the change-of-variables formula
∇zt logq φ(zt |X) =∇ zt
"
logp(ε)

ε=F −1 φ (zt,t;X) + log

det ∂F −1 φ (zt, t;X) ∂zt

 # .(11)
All relevant quantities can be computed using automatic differentiation. For our choice ofF φ as
Fφ(ε, t,X) = ¯µφ(t,X) + ¯σφ(t,X)ε,(12)
the score admits the simple closed-form expression
∇zt logq φ(zt |X) = [ ¯σφ(X, t)¯σφ(X, t)⊤]−1( ¯µφ(X, t)−zt) =− ¯σφ(X, t)−1ε.(13)
Finally, wheneverg θ is state-independent, the divergence term∇ zt ·G θ(zt, t)in eq. (10) vanishes.
A.1 SDECast algorithm
Algorithm 1 summarises one training step of SDECast with thelearnableposterior of eq. (8).
On each interval [ti, ti+1] the posterior marginal qφ(zt |x ti ,x ti+1 ) is Gaussian: its mean is the
linear interpolation of the two bracketing observations plus a learnable correction µφ , and its
scale is δ plus a learnable correction σφ . Both corrections are multiplied by αt(1−α t) and
therefore vanish at the observation times, anchoring zti ∼ N(xti , δ2I) as required by eq. (6). The
simplifiedlinear-interpolantvariant is recovered by fixing µφ =0 and σφ =1 , which leaves a
Brownian-bridge-shaped posterior with no learnable parameters.
Algorithm 1SDECast training step
Require:X={x ti }N i=0 observed at0 =t 0 <· · ·< tN =T
Require:h θ,g θ – prior drift and diffusion networks
Require:µ φ,σ φ – learnable posterior corrections
1:whilenot convergeddo
2:i∼ U {0, . . . , N−1},α∼ U(0,1),ε∼ N(0,I)
3:t←t i +α(t i+1 −t i)▷physical time
4:# Sample the posterior marginalz t =F φ(ε, t,X)of eq. (8)
5: ¯µφ ←(1−α t)xti +α txti+1 + αt(1−α t) µφ(t,x ti ,x ti+1 )
6: ¯σφ ←δ+ αt(1−α t) σφ(t,x ti ,x ti+1 )
7:z t ← ¯µφ + ¯σφε
8:# Posterior drift atz t via eq. (10)
9: ˙Fφ ←∂z t/∂t ▷autograd
10:G θ ← 1 2 gθ(zt, t)g⊤ θ (zt, t)
11:∇ zt logq φ(zt |X)← −¯σ−1 φ ε▷eq. (13)
12:f φ,θ ← ˙Fφ +G θ∇zt logq φ(zt |X) +∇ zt ·G θ
13:# Control and simulation-free dynamics loss
14:u θ,φ(zt, t,X)←g −1 θ (zt, t)  fφ,θ(zt, t;X)−h θ(zt, t) 
15: ˆLdyn ← 1 2 uθ,φ(zt, t,X) 2 2
16:Gradient step onθ, φw.r.t. ˆLdyn
17:end while
8

B Experimental Details
B.1 ERA5
We train SDECast on the WeatherBench-1 [16] copy of ERA5 at 5.625◦ resolution, a 32×64
latitude–longitude grid, on the five variables z500, t850, t2m, u10 and v10, each standardised to
zero mean and unit variance using statistics computed over the training period (1979–2015; validation
2016, test 2018). Longitude is periodic, so the convolutions wrap along the longitude axis only.
The drift and interpolant networks receive 12 conditioning channels (6 spatial, 2 static surface, 4
temporal). The input to the drift network is therefore the 5 state channels plus 12 conditioning
channels; the interpolant network takes the two endpoint states (2×5 ) plus the same 12 conditioning
channels. The diffusion field gθ has 5×32×64 entries. Parameter counts are given in Table 1.
During inference, the SDE is solved with 64 Euler-Maruyama steps.
For details on the baseline implementations we refer to [5].
B.2 SQG
For the SQG experiments the state is the scaled surface potential temperature on the two bounding
surfaces (z= 0 and z=H ), giving C= 2 channels on a 64×64 doubly-periodic grid; the
convolutions therefore wrap along both spatial axes. There is no extra static or temporal conditioning.
We use the same backbone and model size as for ERA5 (Table 1) for prior drift and learnable
interpolant, but parametrize the diffusion coefficient as a single scalar. We train models with both the
linear and the learnable interpolant. During inference, the SDE is solved with 200 Euler-Maruyama
steps.
C Training and Optimisation
SDECast is trained with the simulation-free objective in eq. (4) using AdamW, with a linear learning-
rate warmup followed by cosine annealing. The δ parameter is chosen to be small enough to not
affect the results, while still being non-zero to avoid division by zero in eq. (13). This equates to
δ= 0.001in both experiments. Optimisation settings are summarised in Table 3.
D Additional results on ERA5
We provide additional visualizations for the ERA5 experiments including forecast residuals in fig. 5
and learned volatility in fig. 6. Additional scores for all variables are also provided in tables 4 and 5
and fig. 7.
Table 1: ERA5 model configuration (5.625◦,32×64grid).
Component Value
Grid (lat×lon)32×64
State variablesC5(z500, t850, t2m, u10, v10)
Conditioning channels12(6spatial+2static+4temporal)
Padding circular in longitude only
Posterior interpolant learnable
V olatilitygθ state-independent, scalar per variable and grid cell
Drift networkh θ 3,556,741params
Interpolant networkF φ 3,563,946params
Diffusion fieldg θ 10,240params (5×32×64)
9

Table 2: SQG model configuration (64×64doubly-periodic grid).
Component Value
Grid64×64(doubly periodic)
State channelsC2(surfacesz= 0, z=H)
Conditioning none
Padding circular in both axes
Posterior interpolant linear / learnable
V olatilitygθ state-independent, one scalar
Drift networkh θ 3,542,050params
Interpolant networkF φ 3,544,932params
Diffusion fieldg θ 8,192params (2×64×64)
Figure 5: Predicted and ground truth change in u10 and z500 for the following lead times (from top
to bottom): 1, 2, 3, 6, 12, 24 and 48 hours. Predicted changes were obtained from a single trajectory.
10

Table 3: Training and optimisation settings.
Setting ERA5 SQG
Optimiser AdamW AdamW
Learning rate5×10 −4 5×10 −4
Weight decay1×10 −4 1×10 −4
LR warmup500steps, linear500steps, linear
LR schedule cosine→10 −5 cosine→10 −5
Epochs50 20
Batch size128 128
Precision fp32 fp32
Hardware2×A100 (∼24 h)2×H100 (∼7 h)
Forecast lead time1h6h
Loss weighting uniform uniform
Figure 6: Learned volatility magnitude visualization.
Table 4: Latitude-weighted RMSE ( ↓) on ERA5 in physical units (z500 in m 2/s2, t850/t2m in K,
u10/v10 in m/s) at 1, 6 and 24 h lead times.
Variable Time (h) SDECast Persistence ARCI-24-1h AR-1h DYffusion ClimODE
z500
1 24.8 50.9 29.020.065.8 –
6 66.7 235.361.768.5 93.9 102.9
24 172.0 603.1142.9206.7 186.5 193.4
t850
1 0.32 0.40 0.340.260.39 –
6 0.94 1.590.890.93 0.96 1.16
24 1.44 3.091.261.69 1.43 1.55
t2m
1 0.40 0.66 0.420.370.56 –
6 0.91 2.760.880.92 1.00 1.21
24 1.30 2.131.141.57 1.40 1.40
u10
1 0.44 0.59 0.520.390.47 –
6 1.26 2.22 1.22 1.301.141.41
24 1.99 4.061.722.14 1.81 2.01
v10
1 0.46 0.65 0.550.400.49 –
6 1.34 2.51 1.28 1.381.191.53
24 2.03 4.711.752.18 1.86 2.04
11

Figure 7: Latitude-weighted RMSE, CRPS and SSR. RMSE and CRPS are given in physical units;
z500 in m2/s2, t850/t2m in K, u10/v10 in m/s) at 1, 6 and 24 h lead times. ClimODE paper does not
report its CRPS and SSR so we omit it from the corresponding plots.
12

Table 5: Latitude-weighted CRPS ( ↓) on ERA5 in physical units (z500 in m 2/s2, t850/t2m in K,
u10/v10 in m/s) at 1, 6 and 24 h lead times. ClimODE is deterministic and is therefore not evaluated
here.
Variable Time (h) SDECast Persistence ARCI-24-1h AR-1h DYffusion
z500
1 13.4 38.6 16.812.740.7
6 34.0 169.233.140.6 53.5
24 86.1 352.670.6121.7 96.7
t850
1 0.16 0.26 0.180.130.22
6 0.48 1.060.470.52 0.58
24 0.73 2.020.660.98 0.79
t2m
1 0.16 0.33 0.180.150.30
60.411.51 0.42 0.47 0.53
24 0.59 1.300.540.87 0.71
u10
1 0.22 0.37 0.260.190.26
60.641.45 0.64 0.68 0.68
24 1.00 2.640.881.12 0.96
v10
1 0.22 0.39 0.280.190.27
6 0.69 1.610.680.73 0.71
24 1.02 3.070.911.16 0.99
13

E Additional results on SQG
Additional scores for SQG are provided in tables 6 to 8.
Table 6: Root-mean-square error (RMSE) by forecast lead time, on SQG in physical (denormalized)
units. Values are the mean over 24 test trajectories.
RMSE↓
Model Lead time 1 h 3 h 6 h 12 h 24 h 48 h 96 h
Persistence – 1.635 3.803 5.319 6.756 7.967 8.925 9.665
CFM 6 h – –0.832 1.107 1.664 3.004 5.301
SDECast (linear) 6 h 1.494 2.733 2.284 2.873 3.918 5.535 7.726
SDECast 6 h0.561 1.0551.280 1.584 2.277 3.803 5.863
Table 7: Continuous ranked probability score (CRPS) by forecast lead time, on SQG in physical
(denormalized) units. Values are the mean over 24 test trajectories.
CRPS↓
Model Lead time 1 h 3 h 6 h 12 h 24 h 48 h 96 h
Persistence – 1.150 2.741 3.915 5.107 6.188 7.077 7.771
CFM 6 h – –0.441 0.591 0.879 1.561 2.822
SDECast (linear) 6 h 0.907 1.729 1.402 1.677 2.172 2.989 4.112
SDECast 6 h0.303 0.5990.717 0.868 1.195 1.956 3.163
Table 8: Spread–skill ratio (SSR) by forecast lead time (dimensionless;SSR = 1 indicates a calibrated
ensemble). Values are the mean over 24 test trajectories. This is an ensemble-only metric, so the
deterministic baseline (Persistence) report 0 and are excluded from highlighting; dashes denote leads
the model does not produce.
SSR
Model Lead time 1 h 3 h 6 h 12 h 24 h 48 h 96 h
Persistence – 0.000 0.000 0.000 0.000 0.000 0.000 0.000
CFM 6 h – –0.854 0.8330.810 0.833 0.935
SDECast (linear) 6 h 0.211 0.179 0.334 0.440 0.583 0.817 1.419
SDECast 6 h0.622 0.5520.641 0.7890.945 0.981 0.966
14
