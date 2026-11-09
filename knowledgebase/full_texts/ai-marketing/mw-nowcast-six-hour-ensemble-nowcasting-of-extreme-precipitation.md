---
title: 'MW-Nowcast: Six-hour ensemble nowcasting of extreme precipitation'
url: https://arxiv.org/abs/2609.34836
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Ning Wang
- Zuliang Fang
- Weixin Jin
- Zhongjian Lv
- Shuang Qin
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.34836
pages: 62
chars: 124235
fetched_at: '2026-11-08T13:25:38+00:00'
kb_version: 1
---

# MW-Nowcast: Six-hour ensemble nowcasting of extreme precipitation

MW-Nowcast: Six-hour ensemble nowcasting of
extreme precipitation
Ning Wang1,2†, Zuliang Fang1†, Weixin Jin1†, Zhongjian Lv1,
Shuang Qin1, Pengcheng Zhao1, Siqi Xiang1, Jiang Bian1,
Haoyi Xiong1, Nan Guan2, Bin Zhang1, Liangjie Zhang1,
Denvy Deng1, Qi Zhang1, Matt Corey1, Jitu Keshri1,
Sridhar Iyer1, Hongyu Sun1, Kit Thambiratnam1,
Jonathan Weyn1, Richard E. Turner3, Haiyu Dong1*
1Microsoft Corporation.
2City University of Hong Kong.
3University of Cambridge.
*Corresponding author(s). E-mail(s): haiyu.dong@microsoft.com;
†These authors contributed equally to this work.
Abstract
Extending reliable nowcasting of extreme precipitation could provide critical
additional time for warnings and emergency response during high-impact events
such as flash floods. Radar-based generative machine-learning models have
enabled skilful hyperlocal precipitation nowcasting, but accurate prediction of
intense precipitation remains confined to the first few hours. Because storm-scale
structure is predictable for longer than individual cells, a natural strategy is
to predict that structure while generatively modelling only the uncertain local
growth, decay, reorganisation and initiation of storms. Here we present Microsoft
Weather Nowcast (MW-Nowcast), a six-hour ensemble radar nowcasting model
that jointly learns a deterministic predictor to capture organised precipitation
structure shared across ensemble members, and a generator to produce diverse
local residuals around this shared prediction. Across independent test data from
the United States, Europe and China, MW-Nowcast achieves higher detection
skill than leading methods for heavy and extreme precipitation throughout the
6 h horizon. For the most intense rainfall, MW-Nowcast doubles the available
warning time across all three regions, delivering 6 h forecasts with skill pre-
viously limited to 3 h for the leading generative baseline. A cost–loss decision
analysis shows that MW-Nowcast retains substantial value for a broad range of
applications even at 4–6 h, where alternative methods offer little benefit. These
additional hours can give forecasters and emergency managers the time to warn
and act before extreme rainfall strikes, helping to protect lives and property.
1
arXiv:2609.34836v1  [physics.ao-ph]  28 Sep 2026

1 Introduction
Precipitation nowcasting aims to provide weather forecasts for the next few hours,
translating available information into guidance that is local and early enough to sup-
port immediate proactive mitigation. The World Meteorological Organisation frames
nowcasting as local weather prediction from the present to up to 6 h ahead [1]. Within
this window, predicting hazardous precipitation reliably can broaden the range of
possible responses, including issuing warnings, positioning emergency resources, and
managing drainage systems, roads, aviation and energy operations. This need is espe-
cially acute for extreme precipitation, because assessing its potential impacts requires
forecasts that extend far enough to characterize the likely duration of intense rainfall
over affected locations [2].
Operational nowcasting requires forecasts to be updated frequently as new obser-
vations arrive and to resolve rapidly-evolving precipitation at convective scales.
Numerical weather prediction provides physically-grounded forecasts and can assim-
ilate recent radar observations. However, its computational cost makes updates at
radar cadence challenging [3, 4]. These constraints have motivated methods that infer
future precipitation directly from recent radar sequences. Advection-based statisti-
cal methods such as STEPS provide fast and interpretable ensemble nowcasts by
combining the extrapolation of recent radar echoes with stochastic, scale-dependent
evolution [5, 6]. However, their reliance on transported recent echoes limits their abil-
ity to represent local growth, decay, reorganisation and initiation, especially as lead
time extends beyond 3 h.
Over the last decade, machine-learning methods have become the gold standard
for radar nowcasting, retaining the speed and radar-native character of extrapolation
while learning nonlinear precipitation evolution from data. Early machine-learning
approaches based on deep learning generally formulated this task as supervised
sequence prediction, training deterministic networks with grid-cell losses on observed
future radar sequences [7–9]. They improved the representation of nonlinear spatiotem-
poral evolution beyond extrapolation, but forecasts often became smooth at longer
lead times, with weakened intense cores and limited uncertainty information. Deep
Generative Models of Radar (DGMR) marked an important step towards probabilistic
nowcasting by learning a conditional generative model for entire future precipita-
tion fields, producing sharper and more useful ensemble forecasts [10]. NowcastNet
extended this direction by conditioning the generative network on an advection-
informed deterministic evolution network [11]. It was also strongly preferred by
professional meteorologists in 3 h case evaluations.
Despite these advances, DGMR and NowcastNet reported results for forecast hori-
zons of 90 min and 3 h, respectively, while the full 0–6 h nowcasting window remains
less explored for extreme precipitation [10, 11]. At longer lead times, future precipita-
tion evolution remains partly constrained by the observed radar history, whereas its
conditional distribution becomes increasingly broad. Existing generative systems typ-
ically sample complete future radar sequences, even when a deterministic prediction
is supplied as conditioning information. In this formulation, the generative component
must simultaneously preserve the storm-scale structure supported by recent obser-
vations and represent uncertainty in local cell evolution. Coupling these roles may
2

make it harder to maintain coherent storm placement and organisation while gener-
ating sufficient ensemble variability at longer lead times. Inspired by scale-dependent
precipitation predictability and stochastic representations of unresolved weather vari-
ability, a promising direction is to make the allocation between predictable dynamics
and stochastic variability itself learnable [12–14].
We show that long-lead-time ensemble nowcasting benefits from an explicit,
jointly-learned separation between a deterministic forecast shared across members and
member-dependent probabilistic residuals. We developed Microsoft Weather Nowcast
(MW-Nowcast), a radar nowcasting model that couples two decoders, one producing
the deterministic prediction and the other modelling the probabilistic residual relative
to it. The two are trained jointly rather than as a fixed two-stage cascade, so that the
allocation between shared storm-scale structure and local evolution adapts throughout
training. Across radar networks in the United States (US), Europe (EU) and China
(CN), MW-Nowcast extends skilful detection of heavy and extreme precipitation from
the previously demonstrated 3 h to the full 6 h operational window while preserv-
ing the multiscale structure of the observations. In two recent high-impact events, the
storm that spawned an EF4 tornado in Mississippi and the July 2025 extreme rainfall
over Beijing, MW-Nowcast kept the intense rain cores over the affected areas for longer
than baselines, which weakened or displaced them. A cost–loss analysis shows that
this advantage translates into value at 4–6 h lead times across the full range of protec-
tive decisions. Within these hours, authorities can issue warnings, manage drainage
and transport systems, and position emergency resources before flash floods develop.
2 MW-Nowcast
MW-Nowcast is a 6 h ensemble radar nowcasting framework that predicts the
future radar sequence X1:T = ( X1, . . . ,XT ) from an observed radar history H =
(X−T0+1, . . . ,X0), with T0 = 9 and T = 36 at 10 min intervals, by combining a
deterministic prediction with sampled probabilistic residuals. As shown in Fig. 1, the
model first encodes the radar history with a shared encoder parameterised by ψ, then
branches into a deterministic decoder and a flow-matching residual decoder. We denote
the full-horizon mappings by Sψ,θ for deterministic prediction and Rψ,ϕ for residual
sampling. Both mappings include the shared encoder; “deterministic decoder” and
“residual decoder” refer only to the trainable modules after the encoder. Stochastic-
ity is introduced by initialising the residual flow with a Gaussian noise tensor Z(k) for
each ensemble member. The k-th ensemble member can therefore be written as
X(k) 1:T = S1:T + R(k) 1:T , (1)
where S1:T := Sψ,θ(H) is the full-horizon deterministic prediction, and R(k) 1:T :=
Rψ,ϕ(Z(k), H) is the probabilistic residual generated for the k-th ensemble member.
The noise tensor satisfies Z(k) ∈ RT ×S×S with Z (k) t,i,j i.i.d. ∼ N(0, 1), independently across
ensemble member k, physical lead-time index t and spatial indices ( i, j). The residual
decoder is conditioned on the shared radar-history representation.
3

Deterministic
Decoder
Residual Decoder
t−dimensionDeterministic Prediction
τ−dimension
⊕⊕⊕
X1 X2 XT
⊕⊕⊕ ⊕⊕⊕
···
···
···
···
···
···
Probabilistic Residual
ODE Solver
Residual Decoder
ODE Solver ODE Solver
ODE Solver ODE Solver ODE Solver
···
···
···
···
···
History
Encoder
Fig. 1 MW-Nowcast for 6 h ensemble precipitation nowcasting. A history encoder provides
the deterministic and residual decoders with a shared representation of the observed radar sequenceH.
The deterministic decoder produces the common full-horizon forecast S1:T , while the flow-matching
residual decoder transforms Gaussian noise Z(k) into sampled residuals through an ODE solver. At
each lead time t, the sampled residual is added to St to obtain X(k) t ; different noise draws yield the
forecast ensemble.
During training, the shared encoder, deterministic decoder and residual decoder
are optimised as one model. The encoder is trained to provide a radar-history rep-
resentation that supports both the deterministic decoder and the residual decoder.
Through joint optimisation, the deterministic decoder and residual decoder co-adapt
to allocate future radar evolution between a common predictable component and con-
ditional residuals designed to represent plausible local variability over the 6 h horizon.
In the Supplementary Information, we show that joint optimisation yields stronger
long-lead-time high-threshold skill than training the deterministic decoder before the
residual decoder, a cascade-style strategy analogous to residual correction in generative
downscaling [15].
4

Training combines two objectives. The first penalises deviations between the deter-
ministic prediction and the observed future sequence. The second is a probabilistic-
residual flow-matching loss, with the target dynamically recomputed as
R⋆ 1:T = X1:T − S1:T , (2)
so the distribution of learned probabilistic residuals changes as the deterministic
prediction is updated. The residual decoder is implemented with flow matching.
Unlike GAN-based nowcasting, which encourages realism through a discriminator, flow
matching trains the residual decoder to predict a velocity field at intermediate states
along a probability path from Gaussian noise to the target residual distribution [16].
Recent diffusion and flow-matching nowcasting models have improved sample diversity
and uncertainty quantification compared to GAN-based systems [17–19].
During sampling, we integrate the learned probability-flow ODE to transform each
independent noise tensor into a plausible residual sequence conditioned on the observed
radar history. Adding this residual sequence to the deterministic prediction yields an
ensemble member with detailed local structure, rather than an average over possible
futures.
3 Experimental Setup
We train and evaluate MW-Nowcast on three regional radar datasets covering the US,
EU and CN domains. All datasets are converted to a common 6 h nowcasting task
defined above over a 256 km× 256 km domain at 2 km resolution. The US dataset pairs
NOAA/NCEI Storm Events reports with MRMS Seamless Hybrid Scan Reflectivity
radar composites [20, 21]; the EU dataset pairs European Severe Weather Database
records with OPERA radar mosaics [22, 23]; and the CN dataset is constructed from
China Meteorological Administration composite reflectivity data using radar-native,
peak-anchored strong-precipitation sampling. Training sets contain 130,000–175,000
training sequences per region. Each region is evaluated on 4,000 test sequences drawn
from a strictly later observation period, selected under matching criteria to focus the
benchmark on strong-precipitation and severe convective regimes (Methodology).
We compare MW-Nowcast against three representative baselines spanning opera-
tional extrapolation, deterministic deep prediction and probabilistic ensemble nowcast-
ing. We use the STEPS implementation in PySTEPS as a widely used advection-based
ensemble nowcasting baseline [5, 6]. SimVPv2 is a recent deterministic spatiotem-
poral prediction model that has served as a strong, state-of-the-art baseline across
prediction benchmarks [24]. NowcastNet is a leading generative ensemble nowcast-
ing model that showed strong performance for extreme precipitation in both US and
CN evaluations [11]. We retrain SimVPv2 and NowcastNet using their official model
implementations and evaluate all baselines under the same protocol.
Evaluation combines threshold-based, probabilistic, structural, and decision-
analytic diagnostics. Threshold-based verification uses rain-rate exceedances at 16, 32
and 64 mm h −1 via the Critical Success Index within a 5 × 5 grid-cell neighbourhood
(CSIN) [11, 25]. All ensemble methods are evaluated with four members and aggre-
gated using Probability Matched Mean (PMM) wherever a single field is required [26].
5

Probabilistic forecasts are evaluated using the Continuous Ranked Probability Score
(CRPS) and the Continuous Ranked Probability Skill Score (CRPSS), which mea-
sures how well the ensemble distribution agrees with the observations [27, 28]. Power
Spectral Density (PSD) is used separately as a threshold-free diagnostic of spatial
structure [29]. Practical decision utility is quantified using Relative Economic Value
(REV) across cost–loss ratios [10, 30].
4 Precipitation Cases
We present two high-impact precipitation cases from contrasting storm regimes:
a rapidly-evolving tornadic convective system in the United States and persistent
mountainous heavy rainfall in China. We assess how well each method retains the pre-
cipitation system’s organisation and embedded intense cores as lead time increases,
and how MW-Nowcast allocates the forecast between shared, predictable storm-scale
structure and uncertain local evolution across ensemble members. Additional cases
from all three domains are presented in Extended Data Figs. 1–9.
The convective storm over Walthall County, Mississippi, on 15 March 2025 (Fig. 2a)
spawned an EF4 tornado. The event was documented by an NWS Storm Survey, with
3 fatalities, 8 injuries and approximately $5.0 million in reported property damage.
We initialise the forecast at 17:30 UTC. In the lead-time diagnostics (Fig. 2b), MW-
Nowcast maintains higher CSIN than the baselines at 32 and 64 mm h −1 over much
of the final three hours, with the separation clearest at 64 mm h −1. It also better
preserves multiscale spatial variability and achieves higher probabilistic skill than the
ensemble baselines over most lead times.
The forecast fields show how MW-Nowcast overcomes the characteristic failure
modes of existing baselines (Fig. 2c). Throughout the forecast window, a southwest–
northeast–oriented organised precipitation band remains identifiable, while multiple
embedded intense cores undergo local intensification, weakening, fragmentation and
reorganisation. MW-Nowcast preserves rain-band continuity, concentrated heavy-rain
cores and the overall spatial extent of the system at longer lead times, with member-
wise scores confirming that the late-lead heavy-precipitation signal is carried by
individual ensemble members (Fig. 2d). By contrast, PySTEPS advects part of the
early motion, but its intensity fades progressively within the domain. SimVPv2 keeps
the band continuous, but smooths the embedded convective cores into a broad, uni-
form region of heavy rain. NowcastNet produces sharper local structures at early and
middle leads, but its later forecasts substantially underestimate heavy-core intensity
while spreading light-to-moderate rain over an excessively broad area. These are pre-
cisely the modes that the design of MW-Nowcast targets. Its deterministic predictor
learns the predictable storm-scale structure from data rather than transporting recent
echoes, and its generator adds the small-scale detail as sampled residuals, which keeps
the forecast sharp while remaining anchored to that structure rather than generating
the entire field.
Comparing the deterministic prediction of MW-Nowcast with its ensemble mem-
bers reveals this scale-dependent structure of forecast uncertainty (Fig. 2e). The deter-
ministic branch captures the rain-band location, orientation and overall organisation
6

AL
LA
MS
Start: 2025-03-15 17:30 UTC
Center: 31.10°N, 90.26°W
Patch: 29.81°N-32.39°N | 91.55°W-88.97°W
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.3
0.5
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.3
0.5
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.3
0.6
0.9
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.2
0.3
0.4
0.5
CSIN5@32 (↑ better)
0.1
0.2
0.3
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.1
0.2
0.3
0.4
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.1
0.2
0.3
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Fig. 2 Case study of a US tornado event over the 6 h forecast horizon. The case shows a
convective storm over Walthall County, Mississippi, on 15 March 2025 that spawned an EF4 tornado;
the forecast is initialised at 17:30 UTC. a, Geographic and radar context, with the forecast domain
outlined in orange. b, Forecast diagnostics: CSIN in a 5 × 5 grid-cell neighbourhood at rain-rate
thresholds of 32 and 64 mm h −1, CRPS, CRPSS, and radially averaged PSD at lead times of 3 and
6 h. “Deterministic” denotes the output of the deterministic decoder of MW-Nowcast. c, Observed
and predicted rain-rate fields at hourly lead times from 1 to 6 h. Rows show observations, PySTEPS,
SimVPv2, NowcastNet and MW-Nowcast. d, CSIN and POD at thresholds of 32 and 64 mm h −1 for
the four MW-Nowcast ensemble members and their PMM summary. e, The deterministic prediction
and four ensemble members at lead times of 2, 4 and 6 h.
shared across the ensemble, while the residual branch generates member-dependent
variations in the locations, intensities and morphologies of the embedded convective
cores. Rather than merely adding spatial detail to the deterministic forecast, the resid-
ual branch represents multiple possible pathways of local convective intensification,
weakening and reorganisation while preserving the storm-scale evolution supported by
the observed history.
MW-Nowcast likewise maintains its advantage in a contrasting convective pre-
dictability regime, where organised storm structure progressively scatters and deter-
ministic predictability is rapidly lost (Fig. 3a). The late-July 2025 event over the
northern Miyun district of Beijing and adjacent Hebei caused 30 deaths and led to the
relocation of 80,332 people. For a forecast initialised at 11:00 UTC (19:00 local time)
7

on 26 July 2025, during the evening-to-night development of the storm, MW-Nowcast
retains markedly higher skill than the baselines over the final three hours, especially at
64 mm h −1, while achieving the highest probabilistic skill and closest spectral agree-
ment with observations (Fig. 3b). In the forecast fields, the baselines exhibit the same
error modes as in the previous case, and NowcastNet, although generative, likewise
loses the intense cores at later lead times, whereas MW-Nowcast retains the sustained
heavy-rainfall signal over Miyun to about 5 h (Fig. 3c).
The comparison between the deterministic prediction and the ensemble mem-
bers shows how the allocation learned by MW-Nowcast shifts as predictability is lost
(Fig. 3e). Over the first 4 h, the observed rainfall over the Miyun region is rela-
tively concentrated, the deterministic prediction carries a coherent rainfall signal there,
and the members largely agree on its location while differing in core detail. As the
observed rainfall becomes increasingly scattered, the deterministic prediction fades to
a faint patch by 6 h, whereas the members continue to produce intense cores in varied
locations, often where the deterministic forecast shows almost nothing. This differs
substantially from the Mississippi case, in which the deterministic branch carried most
of the forecast throughout (Fig. 2e). The diagnostics quantify the shift: determinis-
tic CSIN at 64 mm h −1 falls to zero within about 3 h, whereas the ensemble retains
skill to about 5 h (Fig. 3b), with member-wise scores confirming that this signal is
carried by individual ensemble members at middle lead times (Fig. 3d). By the final
hour, with little storm-scale structure left to hold onto, the residual branch still sup-
plies most of the heavy-rainfall signal as diverse scenarios. While the widening spread
marks the limit of local predictability in this case, with individual members increas-
ingly diverging from the observed cores towards 6 h, the ensemble still conveys a
sustained likelihood of heavy rain over the region, an important signal that supports
continued monitoring rather than de-escalation.
8

Start: 2025-07-26 11:00 UTC
Center: 40.69°N, 116.69°E
Patch: 39.41°N-41.97°N | 115.41°E-117.97°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.4
0.0
0.4
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
0.75
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Fig. 3 Case study of the Beijing Miyun mountainous extreme-rainfall event over the
6 h forecast horizon. Extreme rainfall over the northern Miyun district of Beijing and adjacent
Hebei during the late-July 2025 episode; forecast initialised at 11:00 UTC on 26 July 2025 (19:00
local time). Panel descriptions are as in Fig. 2.
5 Quantitative Evaluation
Figure 4 summarises verification over the complete US, EU and CN test sets. MW-
Nowcast achieved the highest CSIN at every evaluated lead time and threshold across
all three regions (Fig. 4a). Whereas baseline CSIN rapidly approached zero after
approximately 3 h at a threshold of 64 mm h −1, MW-Nowcast retained measurable
skill throughout the 6 h horizon. NowcastNet was originally evaluated over a 3 h fore-
casting horizon, whereas we retrain it here to predict the full 6 h sequence. Using the 3
h CSIN of this retrained baseline as the reference, MW-Nowcast sustained equivalent
skill for an additional 2.3 to more than 3 h across the nine region–threshold combi-
nations, with larger gains for more extreme precipitation. These gains are supported
by structured, member-dependent residual adjustments to the common prediction,
illustrated by residual sampling and ensemble-spread visualisations (Supplementary
Sections 3.1 and 3.2). Consistently, the PMM ensemble better recovers the observed
high-intensity rain-rate tail than the deterministic prediction across all three regions
(Extended Data Fig. 10). Both generating the complete future sequence without a
9

0.0
0.2
0.4
0.6
US +2.5 h +2.3 h ≥ 3.0 h
0.0
0.2
0.4
0.6
EU +2.7 h ≥ 3.0 h ≥ 3.0 h
0 1 2 3 4 5 6
0.0
0.2
0.4
0.6
CN +2.7 h
0 1 2 3 4 5 6
+2.6 h
0 1 2 3 4 5 6
≥ 3.0 h
0
5
10US
0
5
10EU
0 1 2 3 4 5 6
0
5
10CN
256 64 16 4
−20
0
25
50 Observed
256 64 16 4
Observed
256 64 16 4
Observed
10−2 10−1 100
0.0
0.1
0.2
0.3
0.4 ≥ 16 mm h−1
≥ 32 mm h−1
10−2 10−1 100
≥ 16 mm h−1
≥ 32 mm h−1
10−2 10−1 100
≥ 16 mm h−1
≥ 32 mm h−1
a Neighbourhood CSI (5 x 5) b Ensemble CRPS
c PSD over US
d REV over US
≥  16 mm h−1 ≥  32 mm h−1 ≥  64 mm h−1
T+2h T+4h T+6h
T+2h T+4h T+6h
Lead time (h) Lead time (h) Lead time (h) Lead time (h)
Wavelength (km) Wavelength (km) Wavelength (km)
Cost-loss ratio Cost-loss ratio Cost-loss ratio
MW-Nowcast NowcastNet SimVPv2 PySTEPS
Fig. 4 Quantitative evaluation of 6 h precipitation nowcasts. Curves compare MW-Nowcast,
NowcastNet, SimVPv2 and PySTEPS. a, Critical Success Index in a 5 × 5 grid-cell neighbourhood
over the 6 h forecast horizon for the US, EU and CN test sets at rain-rate thresholds of 16, 32 and
64 mm h −1; higher values are better. b, grid-point Continuous Ranked Probability Score (CRPS) of
the four-member ensembles for the three regions; lower values are better. c, radially averaged power
spectral density (PSD) over the US at lead times of 2, 4 and 6 h, with the observed spectrum shown
for reference. d, relative economic value (REV) over the US as a function of cost–loss ratio at lead
times of 2, 4 and 6 h for rain-rate exceedances of 16 and 32 mm h −1.
10

deterministic branch and training the deterministic and residual models sequentially
reduce long-lead high-threshold skill (Supplementary Section 2 and Supplementary
Table 1). These results support jointly-learned residual generation as a key contributor
to sustained extreme-precipitation skill at longer forecast horizons.
We next evaluated the four-member ensembles directly using grid-point contin-
uous ranked probability score (CRPS), which measures the agreement between the
predictive distribution and the observation at each location (Fig. 4b). MW-Nowcast
achieved lower CRPS than both NowcastNet and PySTEPS across all three regions,
indicating a better balance between individual-member accuracy and ensemble spread.
PySTEPS nevertheless outperformed NowcastNet in CRPS. Because domain-averaged
grid-point CRPS weights every location equally and does not specifically emphasise
intense precipitation, conservative forecasts can remain competitive even when they
lose high-threshold skill.
We further assessed scale-dependent precipitation variability in all three regions
using radially averaged PSD at lead times of 2, 4 and 6 h. Figure 4c shows the US
results. SimVPv2 progressively lost spectral power at medium and short wavelengths,
consistent with increasingly smooth forecasts. By contrast, MW-Nowcast remained
close to the observed spectrum throughout the 6 h horizon, outperforming NowcastNet
and more closely matching observations than PySTEPS at 2 and 4 h, with comparable
agreement at 6 h. Similar spectral behaviour was observed in EU and CN (Supplemen-
tary Section 4.2). These results indicate better retention of precipitation variability
across spatial scales.
Beyond standard verification metrics, we assessed whether improved forecast skill
could better support protective decision-making using the relative economic value
(REV) framework adopted in previous probabilistic forecasting studies [10, 31]. REV
measures whether forecast-based action can reduce expected expense in a stylised
cost–loss decision problem and is normalised such that 1 represents a perfect forecast
and 0 represents no improvement over the optimal climatological strategy (Methodol-
ogy). DGMR [10] evaluated REV for precipitation accumulated over a 90 min forecast
window, whereas we evaluated the instantaneous value separately at lead times of 2,
4 and 6 h to examine whether forecasts retain decision value at longer lead times
and could therefore support earlier protective action. At each lead time, we calcu-
lated REV across cost–loss ratios for rain-rate exceedances of 16 and 32 mm h −1 in
all three regions. Across these regions, MW-Nowcast provided substantially greater
REV overall than the baselines at both thresholds and all three lead times (Fig. 4d
and Supplementary Information). The US results in Fig. 4d show that, at 4 and 6 h,
MW-Nowcast retained positive value over a broad range of cost–loss ratios, whereas
the baseline values were close to zero. These results suggest that the long-lead-time
skill of MW-Nowcast can support useful protective decisions across users with dif-
ferent action costs, extending the time available for preparation throughout the 6 h
nowcasting window.
11

6 Conclusion
The value of extreme-precipitation nowcasting depends not only on producing realistic
precipitation fields, but also on retaining useful skill far enough ahead to support early
warning and emergency response, yet the latter has remained a difficult frontier. We
have presented MW-Nowcast, which jointly learns a shared deterministic prediction
and conditional probabilistic residuals around it to provide six-hour ensemble radar
nowcasting. Controlled experiments show that learning this division end-to-end is
essential to sustaining skill at longer lead times. Across radar datasets from the United
States, Europe and China, MW-Nowcast delivers skilful ensemble nowcasts of extreme
precipitation across the full 6 h window, doubles the available warning time for the
most intense rainfall from three hours to six, and retains decision value at 4–6 h, where
existing methods offer little.
Future work should extend precipitation nowcasting beyond the information avail-
able from radar alone. Combining radar with geostationary satellite imagery and
numerical-weather-prediction guidance could provide earlier information about cloud
development and environmental conditions, with particular potential for improving
forecasts of convective initiation and rapidly evolving storms. Our evaluation spans
three regions with dense radar networks, but radar observations could also serve as
training targets for models driven by satellite and numerical inputs which are avail-
able more widely, bringing nowcasting to regions with sparse or no operational radar
coverage. Such approaches could improve both the accuracy and geographical reach of
long-lead precipitation nowcasting and extend the decision value demonstrated here
to communities with the most limited early-warning capabilities.
References
[1] Wang, Y., et al.: Guidelines for Nowcasting Techniques. World Meteorological
Organization, Geneva (2017)
[2] Georgakakos, K.P., Modrick, T.M., Shamir, E., Campbell, R., Cheng, Z., Jubach,
R., Sperfslage, J.A., Spencer, C.R., Banks, R.: The flash flood guidance sys-
tem implementation worldwide: A successful multidecadal research-to-operations
effort. Bulletin of the American Meteorological Society 103(3), 665–679 (2022)
https://doi.org/10.1175/BAMS-D-20-0241.1
[3] Sun, J.: Convective-scale assimilation of radar data: progress and challenges.
Quarterly Journal of the Royal Meteorological Society: A journal of the atmo-
spheric sciences, applied meteorology and physical oceanography 131(613),
3439–3463 (2005)
[4] Sun, J., et al.: Use of nwp for nowcasting convective precipitation: recent progress
and challenges. Bulletin of the American Meteorological Society 95(3), 409–426
(2014) https://doi.org/10.1175/BAMS-D-11-00263.1
[5] Bowler, N.E., Pierce, C.E., Seed, A.W.: Steps: A probabilistic precipitation
12

forecasting scheme which merges an extrapolation nowcast with downscaled
nwp. Quarterly Journal of the Royal Meteorological Society: A journal of the
atmospheric sciences, applied meteorology and physical oceanography 132(620),
2127–2155 (2006)
[6] Pulkkinen, S., Nerini, D., P´ erez Hortal, A.A., Velasco-Forero, C., Seed, A.,
Germann, U., Foresti, L.: Pysteps: An open-source python library for probabilis-
tic precipitation nowcasting (v1. 0). Geoscientific Model Development 12(10),
4185–4219 (2019)
[7] Shi, X., Chen, Z., Wang, H., Yeung, D.-Y., Wong, W.-K., Woo, W.-c.: Convolu-
tional lstm network: A machine learning approach for precipitation nowcasting.
In: Advances in Neural Information Processing Systems, vol. 28 (2015)
[8] Wang, Y., Long, M., Wang, J., Gao, Z., Philip, S.Y.: Predrnn: Recurrent neu-
ral networks for predictive learning using spatiotemporal lstms. In: Advances in
Neural Information Processing Systems, vol. 30 (2017)
[9] Gao, Z., Shi, X., Wang, H., Zhu, Y., Wang, Y., Li, M., Yeung, D.-Y.: Earthformer:
Exploring space-time transformers for earth system forecasting. In: Advances in
Neural Information Processing Systems (2022). https://arxiv.org/abs/2207.05833
[10] Ravuri, S., Lenc, K., Willson, M., Kangin, D., Lam, R., Mirowski, P., Fitzsi-
mons, M., Athanassiadou, M., Kashem, S., Madge, S., et al.: Skilful precipitation
nowcasting using deep generative models of radar. Nature 597(7878), 672–677
(2021)
[11] Zhang, Y., Long, M., Chen, K., Xing, L., Jin, R., Jordan, M.I., Wang, J.: Skilful
nowcasting of extreme precipitation with nowcastnet. Nature 619(7970), 526–532
(2023)
[12] Germann, U., Zawadzki, I.: Scale-dependence of the predictability of precipitation
from continental radar images. part i: description of the methodology. Monthly
Weather Review 130, 2859–2873 (2002)
[13] Lorenz, E.N.: The predictability of a flow which possesses many scales of motion.
Tellus 21(3), 289–307 (1969) https://doi.org/10.1111/j.2153-3490.1969.tb00444.
x
[14] Palmer, T.N.: Predicting uncertainty in forecasts of weather and climate. Reports
on Progress in Physics 63(2), 71 (2000) https://doi.org/10.1088/0034-4885/63/
2/201
[15] Mardani, M., Brenowitz, N., Cohen, Y., Pathak, J., Chen, C.-Y., Liu, C.-C.,
Vahdat, A., Nabian, M.A., Ge, T., Subramaniam, A., Kashinath, K., Kautz, J.,
Pritchard, M.: Residual Corrective Diffusion Modeling for Km-scale Atmospheric
Downscaling (2023). https://doi.org/10.48550/arXiv.2309.15214 . https://arxiv.
13

org/abs/2309.15214
[16] Lipman, Y., Chen, R.T., Ben-Hamu, H., Nickel, M., Le, M.: Flow match-
ing for generative modeling. In: 11th International Conference on Learning
Representations, ICLR 2023 (2023)
[17] Gao, Z., Shi, X., Han, B., Wang, H., Jin, X., Maddix, D., Zhu, Y., Li, M., Wang,
Y.: Prediff: Precipitation nowcasting with latent diffusion models. In: Advances in
Neural Information Processing Systems (2023). https://arxiv.org/abs/2307.10422
[18] Leinonen, J., Hamann, U., Nerini, D., Germann, U., Franch, G.: Latent diffu-
sion models for generative precipitation nowcasting with accurate uncertainty
quantification. arXiv preprint arXiv:2304.12891 (2023)
[19] Ribeiro, B.P., Pucer, J.F.: Flowcast: Advancing precipitation nowcast-
ing with conditional flow matching. In: International Conference on
Learning Representations (2026). https://doi.org/10.48550/arXiv.2511.09731 .
https://arxiv.org/abs/2511.09731
[20] NOAA National Centers for Environmental Information: Storm Events Database.
Accessed March 18, 2026 (2026). https://www.ncei.noaa.gov/stormevents/
[21] Zhang, J., Howard, K., Langston, C., Kaney, B., Qi, Y., Tang, L., Grams,
H., Wang, Y., Cocks, S., Martinaitis, S., Arthur, A., Cooper, K., Brogden, J.,
Kitzmiller, D.: Multi-radar multi-sensor (mrms) quantitative precipitation esti-
mation: Initial operating capabilities. Bulletin of the American Meteorological
Society 97(4), 621–637 (2016) https://doi.org/10.1175/BAMS-D-14-00174.1
[22] Dotzek, N., Groenemeijer, P., Feuerstein, B., Holzer, A.M.: Overview of ESSL’s
severe convective storms research using the European Severe Weather Database
ESWD. Atmospheric Research 93(1–3), 575–586 (2009) https://doi.org/10.1016/
j.atmosres.2008.10.020
[23] K¨ ock, K., Leltne, T., Randeu, W., Divjak, M., Schrelber, K.-J.: Opera: Opera-
tional programme for the exchange of weather radar information. first results and
outlook for the future. Physics and Chemistry of the Earth, Part B: Hydrology,
Oceans and Atmosphere 25(10-12), 1147–1151 (2000)
[24] Tan, C., Gao, Z., Li, S., Li, S.Z.: Simvpv2: Towards simple yet powerful
spatiotemporal predictive learning. IEEE Transactions on Multimedia (2025)
[25] Schaefer, J.T.: The critical success index as an indicator of warning skill. Weather
and forecasting 5(4), 570–575 (1990)
[26] Ebert, E.E.: Ability of a poor man’s ensemble to predict the probability and
distribution of precipitation. Monthly Weather Review129(10), 2461–2480 (2001)
https://doi.org/10.1175/1520-0493(2001)129⟨2461:AOAPMS⟩2.0.CO;2
14

[27] Gneiting, T., Raftery, A.E.: Strictly proper scoring rules, prediction, and esti-
mation. Journal of the American statistical Association 102(477), 359–378
(2007)
[28] M¨ uller, W., Appenzeller, C., Doblas-Reyes, F., Liniger, M.: A debiased ranked
probability skill score to evaluate probabilistic ensemble forecasts with small
ensemble sizes. Journal of Climate 18(10), 1513–1523 (2005)
[29] Harris, D., Foufoula-Georgiou, E., Droegemeier, K.K., Levit, J.J.: Multiscale
statistical properties of a high-resolution precipitation forecast. Journal of
Hydrometeorology 2(4), 406–418 (2001)
[30] Richardson, D.S.: Skill and relative economic value of the ECMWF ensemble pre-
diction system. Quarterly Journal of the Royal Meteorological Society 126(563),
649–667 (2000) https://doi.org/10.1002/qj.49712656313
[31] Price, I., Sanchez-Gonzalez, A., Alet, F., Andersson, T.R., El-Kadi, A., Masters,
D., Ewalds, T., Stott, J., Mohamed, S., Battaglia, P., Lam, R., Willson, M.:
Probabilistic weather forecasting with machine learning. Nature637(8044), 84–90
(2025) https://doi.org/10.1038/s41586-024-08252-9
[32] Fulton, R.A., Breidenbach, J.P., Seo, D.-J., Miller, D.A., O’Bannon, T.: The
WSR-88D rainfall algorithm. Weather and Forecasting 13(2), 377–395 (1998)
https://doi.org/10.1175/1520-0434(1998)013⟨0377:TWRA⟩2.0.CO;2
[33] Ruzanski, E., Chandrasekar, V., Wang, Y.: The casa nowcasting system. Journal
of Atmospheric and Oceanic Technology 28(5), 640–655 (2011)
[34] Sun, H., Yang, Y., Han, W., Huang, W., Chen, H., Gao, Z., Li, Z., Huo, Z., Niu, Z.:
Stormdit: A generative ai model bridges the 2–6 hour gray zone in precipitation
nowcasting. arXiv preprint arXiv:2601.20342 (2026)
[35] Gong, J., Bai, L., Ye, P., Xu, W., Liu, N., Dai, J., Yang, X., Ouyang, W.: Cas-
cast: Skillful high-resolution precipitation nowcasting via cascaded modelling.
In: Proceedings of the International Conference on Machine Learning (2024).
https://arxiv.org/abs/2402.04290
[36] Yu, D., Li, X., Ye, Y., Zhang, B., Luo, C., Dai, K., Wang, R., Chen, X.: Diffcast: A
unified framework via residual diffusion for precipitation nowcasting. In: Proceed-
ings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
(2024). https://arxiv.org/abs/2312.06734
[37] Roberts, N.M., Lean, H.W.: Scale-selective verification of rainfall accumulations
from high-resolution forecasts of convective events. Monthly Weather Review
136(1), 78–97 (2008) https://doi.org/10.1175/2007MWR2123.1
15

7 Methodology
We use this section to define the architecture, training objective and sampling pro-
cedure with the same notation as the main text. A temporal stack X(a,b] denotes
the left-open, right-closed sequence ( Xa+1, . . . ,Xb). The observed history is H =
(X−T0+1, . . . ,X0), equivalently H = X(−T0, 0], and therefore contains exactly T0 = 9
frames, including the issue-time frame X0. The future target sequence is X1:T =
(X1, . . . ,XT ), equivalently X(0, T], with T = 36. The parameterised full-horizon
mappings for deterministic prediction and residual sampling areSψ,θ and Rψ,ϕ, respec-
tively. Both mappings include the shared encoder, and neither symbol denotes a
decoder module alone. Their outputs are S1:T := Sψ,θ(H) and R(k) 1:T := Rψ,ϕ(Z(k), H).
Throughout, calligraphic symbols denote mappings, whereas bold symbols denote
tensor-valued inputs and outputs. Thus, Eq. (1) is the single top-level definition of the
model used in both the main text and Methods. For physical lead time t, we write
X(k) t := [X(k) 1:T ]t, St := [S1:T ]t and R(k) t := [R(k) 1:T ]t. We omit the member index k when
referring to a generic probabilistic residual.
7.1 Deterministic-probabilistic formulation
For the discrete forecasting task, Xt ∈ RS×S denotes the reflectivity field at physical
lead index t, and bold uppercase symbols such as X(a,b] denote sequences stacked
along the time dimension. The deterministic prediction mappingSψ,θ produces the full
T -frame output S1:T in parallel from H, avoiding autoregressive error accumulation.
During training, this deterministic prediction defines the probabilistic residual target
in Eq. (2). This target is not an observed physical forcing; it is precisely the part of
the future sequence not represented by the current deterministic prediction. Because
the model components underlying Sψ,θ and Rψ,ϕ are trained jointly, the probabilistic
residual target evolves as the deterministic decoder improves.
The residual sampling map Rψ,ϕ is defined by a residual decoder trained with
conditional flow matching and an ODE solver used at inference. Physical lead time
t ∈ {1, . . . , T} indexes forecast frames, whereas generative time τ ∈ [0, 1] indexes an
internal trajectory from a Gaussian noise tensor to a probabilistic residual. To keep
Eqs. (3)–(6) compact, we write r⋆ := R⋆ 1:T for the full-sequence probabilistic residual
target and r(τ ) for the full sequence-valued flow state; the physical lead dimension is
therefore implicit in both symbols. For a noise tensor Z drawn as specified in Eq. (1)
and τ ∼ U[0, 1], the linear probability path is
r(τ ) = (1 − τ )Z + τ r⋆. (3)
Its target velocity is
u⋆ = dr(τ ) dτ = r⋆ − Z. (4)
The residual decoder, parameterised by ϕ and conditioned on the history representa-
tion produced by the shared encoder parameterised by ψ, predicts this velocity from
16

the current flow state, generative time and observed history:
vψ,ϕ(r(τ ), τ,H) ≈ u⋆. (5)
At inference, a probabilistic residual is obtained by solving
dr(τ )
dτ = vψ,ϕ(r(τ ), τ,H), r(0) = Z, R1:T := Rψ,ϕ(Z, H) = r(1). (6)
This last identity connects the terminal ODE state directly to the probabilistic residual
in Eq. (1). For numerical inference, we discretise generative time as τn = n/N, n =
0, . . . , N, with N = 20 and step size ∆ τ = 1/N, and write rn := r(τn). At a discrete
solver state, the residual decoder predicts vn := vψ,ϕ(rn, τn, H). The fixed-step Heun
integrator advances the flow by
˜rn+1 = rn+∆τ vn, vp n+1 = vψ,ϕ(˜rn+1, τn+1, H), rn+1 = rn+ ∆τ 2  vn+vp n+1  .
(7)
For ensemble member k, r(k) 0 = Z(k) and R(k) 1:T = r(k) N , while the deterministic
prediction remains shared across members.
7.2 Model details
For all experiments, each sample covers a 256 km × 256 km physical domain, while
the model input is represented on a square radar grid with side length S = 128. The
input history has shape ( T0, S, S,1) = (9 , 128, 128, 1) and the target future sequence
has shape ( T, S, S,1) = (36 , 128, 128, 1), corresponding to 1.5 h of history and 6 h
of prediction at 10 min resolution. A stride-4 patch projection gives feature-grid side
length s = S/4 = 32, and the token feature dimension is c = 256. The Gaussian noise
tensor Z has mathematical shape ( T, S, S) = (36, 128, 128) and implementation shape
(36, 128, 128, 1). Its 36 temporal slices are sampled independently.
MW-Nowcast contains three trainable modules: a shared history encoder Eψ, a
deterministic decoder parameterised by θ, and a residual decoder parameterised by ϕ.
The latter two are the post-encoder modules, whereas Sψ,θ and Rψ,ϕ remain reserved
for the corresponding end-to-end mappings. The encoder supplies the flattened history
context Chist to both decoders. The deterministic decoder produces S1:T , while each
residual-decoder evaluation maps ( rn, τn, Chist) to the probability-flow velocity vn.
Table 1 summarises the symbols, tensor shapes and repeated-module counts used in
Fig. 5.
The history encoder patchifies each observed frame with a strided 4 × 4 con-
volution, reducing the spatial grid from S × S to s × s and projecting the single
input channel to width c = 256. The flattened history-token sequence has shape
(T0, s2, c) = (9 , 1024, 256). The encoder applies ME = 3 stacked Temporal–Spatial–
Frequency (TSF) blocks. Each block uses temporal attention, spatial mixing, AFNO
frequency mixing and a second temporal-attention layer. Temporal attention uses 4
heads at width 256; the spatial modules alternate shifted-window and global-token
attention, and AFNO uses g = 8 channel groups. All attention and MLP sublayers
17

T able 1Architecture and discrete-inference notation.
Symbol Meaning Value
T0, T Numbers of history and future frames 9 , 36
K Number of ensemble members 4
N Number of Heun intervals 20
S, s, c Radar-grid side, feature-grid side and feature width 128 , 32, 256
g Number of AFNO channel groups 8
ME Number of repeated TSF blocks in each context backbone 3
MT Number of temporal-upsample stages in the deterministic
decoder
2
H Observed radar history (9 , 128, 128, 1)
Chist Flattened history-context tokens (9 , 1024, 256)
S1:T Deterministic prediction (36 , 128, 128, 1)
Z(k) Initial noise for ensemble member k (36, 128, 128, 1)
τn Discrete generative time at solver state n 0, 0.05, . . . ,1
rn Probabilistic-residual flow state at τn (36, 128, 128, 1)
vn Velocity predicted from rn at τn (36, 128, 128, 1)
R(k) 1:T Terminal probabilistic residual for ensemble member k (36, 128, 128, 1)
use pre-normalisation, SwiGLU activations and residual connections. The output is
Chist ∈ RT0×s2×c.
The deterministic decoder predicts all T = 36 future frames in parallel. Four 1D
temporal convolution blocks with kernel size 3 and dilation rates 1 , 2, 4, 8 aggregate
the history tokens at width c. The temporal decoder uses MT = 2 transposed 1D
convolution stages to expand the temporal axis from T0 = 9 to T = 36. Two Pix-
elShuffle stages then increase the feature grid from s = 32 to S = 128, followed by the
convolutional output head. The result is S1:T ∈ RT ×S×S×1.
At solver state n, the residual decoder receives rn ∈ RT ×S×S×1, τn and Chist.
A stride-4 projection produces ( T, s2, c) future tokens, and the sinusoidal embed-
ding of τn is projected to width c. The residual pathway applies ME = 3 TSF
blocks with cross-attention to the history context. Four dilated temporal-convolution
blocks then mix information across the T = 36 future positions without chang-
ing their number. Because the residual decoder has equal input and output lengths,
its temporal-upsample operator is the identity; the same two-stage spatial upsam-
pler reconstructs the radar grid from s = 32 to S = 128. The decoder output is
vn := vψ,ϕ(rn, τn, H) ∈ RT ×S×S×1.
The shared encoder, deterministic decoder and residual decoder contain approx-
imately 18.6M, 11.2M and 23.4M trainable parameters, respectively. Diversity is
introduced exclusively through the frame-wise independent noise tensor Z in the resid-
ual decoder. Consequently, ensemble spread represents conditional uncertainty in local
growth, decay and structural reorganisation around a shared deterministic prediction,
rather than stochasticity injected into the deterministic decoder.
18

(T, s, s, c)
⊗⊗⊗
(T,S,S,1)
(T,S,S,1)
Gated Attn
Attention
SwiGLU
⊕⊕⊕
⊕⊕⊕
Temp Aggr Temp Up Spat Up
T Conv1D
Conv1D
ReLU
⊕⊕⊕
(T,s2,c)
(T0,s2,c)
(T,S,S,1)
Tem p Aggr
Tem p Up
Spat Up
Conv2D
PixShuffle
ReLU
×log(S/s)
(T,S,S,c)
(T, s, s, c)
Conv2D
Conv2D
Tem p Attn
Spat Block
Tem p Attn
Future
Decoder
Deterministic
 Decoder
Residual Decoder
a) MW-Nowcast main blocks.
c) Future-decoder architecture and its modules.
Context
Encoder
(T,S,S,1)
(T,S,S,1)
×4
D Conv1D
Conv1D
ReLU
⊕⊕⊕
(T0,s2,c)
(T0,s2,c)
Cross Attn
×ME
×MT
Linear
⊕⊕⊕
SwiGLU
SiLU
Linear
Linear
⊗⊗⊗
(T0,s2,c)
Context Encoder
Future Decoder
(·,S ,S ,1)
(·, s, s, c)
(·,s2,c)
History
Encoder
Context
Encoder
(T0,S ,S ,1)
(T0,s2,c)
Future
Decoder
(T0,s2,c)
Temp Attn
Gated Attn
(s2,·,c)
Spat Block
×2
Adpt FNO
Gated Attn
(·, s, s, c)
(·,s2,c)
AFNO
(·, s, s, c/k)
FFT
/obar/obar/obar
MLP MLP
iFFT
(·, s, s, c)
(·, s, s, c)
···
b) Context encoder and its modules.
Trainable layer
Trainable module
Main block ⊕⊕⊕Add operation
Multiply operation
Non-trainable layer
/obar/obar/obarSplit operation
©©©
©©©Concat operation
Fig. 5 Network architecture of MW-Nowcast. The history encoder maps H to Chist, and the
deterministic decoder produces S1:T . At discrete ODE state ( rn, τn), the residual decoder uses the
shared history context to predict vn. In panel c, Tin = T0 for the deterministic decoder and Tin = T
for the residual decoder. The dashed temporal-upsample block is applied only in the deterministic
decoder and is bypassed as an identity operation in the residual decoder. The Heun solver iterates
from r(k) 0 = Z(k) to R(k) 1:T = r(k) N . Symbols, shapes and repeated-module counts are defined in Table 1.
7.3 Training objective function
The three modules are optimised jointly. The deterministic decoder is supervised by
an intensity-weighted reconstruction loss, while the residual decoder is supervised by
the conditional flow-matching objective. The total loss is
L = λdetLdet + LFM, (8)
where λdet = 0.2 in all experiments.
7.3.1 Deterministic loss
Let St = [ S1:T ]t be the deterministic prediction at physical lead time t. The
deterministic loss is
Ldet = sdet T
TX
t=1
ℓdet(St, Xt), (9)
where sdet = 0.5. The per-frame loss combines weighted MSE and MAE terms:
ℓdet(S, X) = 1 S2
SX
i=1
SX
j=1
W (X)i,j

λmse(Si,j − Xi,j)2 + λmae |Si,j − Xi,j|  , (10)
19

with λmse = λmae = 1. The intensity weight is
[W (X)]i,j = qki,j , k i,j =
6X
m=1
1{Xi,j > θm}, (11)
where ( i, j) indexes a grid cell, θ = ( −0.4, 0, 0.2667, 0.4667, 0.6667, 0.9) and q =
(1, 1, 2, 4, 6, 8, 10) for normalised reflectivity values in [ −1, 1].
7.3.2 Probabilistic-residual flow-matching loss
Using the probabilistic residual target in Eq. (2), the interpolation in Eq. (3) and the
target velocity in Eq. (4), we train the residual decoder with
LFM = E(H,X1:T )∼pdata, τ,Z
 1
T S2 ∥vψ,ϕ(r(τ ), τ,H) − u⋆∥2 2

. (12)
We train for 200,000 optimisation steps with a batch size of 8 using AdamW (β1 =
0.9, β2 = 0.999, ϵ = 10−8 and weight decay 0.01). The learning rate is linearly increased
from 10−5 to a peak of 2×10−4 over the first 10% of training and then cosine-decayed to
10−5 over the remaining steps. Training uses mixed precision and DeepSpeed gradient
clipping with a global-norm threshold of 1.0. No data augmentation beyond random
sample shuffling is used.
7.4 Datasets
We evaluate all methods on three regional radar datasets from the US, EU and CN
domains. Although the three datasets are constructed from different event sources and
radar archives, they are converted to a common nowcasting protocol. Each sample
contains 9 historical radar frames and 36 future target frames at 10 min cadence,
corresponding to a 1.5 h input window and a 6 h forecast horizon. Radar fields are
represented on a common spatial grid and extracted over a fixed 256 km × 256 km
physical domain. Models use preprocessed radar reflectivity as input and predict future
reflectivity. Reflectivity is then converted to rain rate for verification and precipitation
visualisation.
The US dataset is constructed by pairing NOAA/NCEI Storm Events reports with
MRMS Seamless Hybrid Scan Reflectivity radar composites [20, 21]. The NCEI records
provide the occurrence time, location, event type and impact information for severe
weather events, while MRMS provides the corresponding high-resolution precipitation
structure within the event-centred radar window. We extract radar sequences using the
reported event time and location as anchors, and construct the training and evaluation
samples after quality control and de-duplication. The training period spans January
2021 to September 2024 and contains 152,408 samples. The evaluation period spans
October 2024 to February 2026. For the main evaluation, we use a compact test
set of 4,000 samples constructed from the future holdout period; this set preserves
spatiotemporal diversity while prioritising high-impact events.
20

The EU dataset follows a similar event-record-driven strategy, but uses the Euro-
pean Severe Weather Database (ESWD) as the event source and OPERA radar
mosaics as the radar source [22, 23]. ESWD provides event-level records for severe con-
vective weather, including wind, hail, heavy precipitation, tornadoes and lightning. We
retain events that fall within the OPERA radar coverage and have a complete now-
casting time window, and then extract the corresponding radar sequences. Because
the reported event time and location do not necessarily coincide with a pronounced
precipitation echo in the radar field, we apply radar-signal quality control to remove
samples with little or no precipitation signal. The training period spans January 2020
to December 2023 and contains 131,761 samples. The evaluation period spans January
2024 to 23 July 2024. The main evaluation uses a compact 4,000-sample test set that
balances event diversity and high-impact event coverage.
The CN dataset is rebuilt from China Meteorological Administration composite
reflectivity data using a radar-native, peak-anchored sampling strategy. The sampler
first identifies spatially organised future strong-echo peaks in the radar sequence by
requiring both local window-mean and window-maximum reflectivity to satisfy strong-
precipitation criteria, reducing the chance that isolated noisy pixels trigger candidate
samples. For each retained peak, the forecast initialisation time is generated by shifting
backward from the peak time using sparse lead-to-peak buckets of 60, 120, 180 and
240 min. This peak-anchored design samples near-peak, mid-growth and early-growth
stages, allowing the evaluation to probe 6 h forecasts of heavy-precipitation growth,
maintenance and reorganisation.
To reduce near-duplicate samples from the same storm system, we apply frame-
and peak-level non-maximum suppression and limit both the daily number of samples
and the number of issue times retained for each peak. Training samples are additionally
required to retain late-label strong-echo activity, ensuring that the 6 h target win-
dow contains meaningful heavy-precipitation evolution. The CN training period spans
November 2021 to June 2025 and contains 174,753 samples. The evaluation period
spans July 2025 to June 2026, and the main evaluation uses a temporally held-out
strict compact test set of 4,000 samples. This compact test set requires strong-echo
activity in every forecast hour and future centre-region reflectivity maxima of at least
45 dBZ. It is stratified by month, convective-growth stage and lead-to-peak bucket,
and uses a 2 h / 200 km time-space diversity rule to reduce near-duplicate samples.
Together, the three regional datasets support a common evaluation goal: testing
long-lead radar nowcasting skill for heavy precipitation and high-impact convective
weather. The US and EU datasets provide event-record-centred evaluations, while the
CN dataset provides a complementary radar-native evaluation of strong-precipitation
processes. Despite these differences in event definition, all three datasets are converted
to the same input-output protocol, allowing models and baselines to be compared
under a consistent technical setting. This design also determines the focus of our
evaluation: high rain-rate thresholds, long forecast lead times and the preservation of
organised strong-echo structure, rather than average performance over all precipitation
intensities.
21

T able 2 Regional radar datasets used in this study . All datasets are converted to a common
9-frame input and 36-frame forecast protocol at 10 min cadence.
Region Construction Training set Evaluation set
US NOAA/NCEI Storm Events + MRMS SeamlessHSR Jan. 2021–Sep. 2024 152,408 samples Oct. 2024–Feb. 2026 4,000 samples
EU ESWD severe-weather records + OPERA radar mosaics Jan. 2020–Dec. 2023 131,761 samples Jan. 2024–23 Jul. 2024 4,000 samples
CN Radar-native strong-precipitation sampling + CMA reflectivity Nov. 2021–Jun. 2025 174,753 samples Jul. 2025–Jun. 2026 4,000 samples
7.5 Baselines
We compare against three representative baselines spanning classical extrapolation,
deterministic deep prediction and physics-guided generative nowcasting. All methods
use the same 9-frame history length, 36-frame forecast horizon, reflectivity preprocess-
ing and 128 × 128 verification targets over a 256 km × 256 km domain. The learned
models receive the corresponding 128 × 128 input histories. As described below, PyS-
TEPS is intentionally supplied with a larger 256 × 256 spatial context before its
forecasts are centre-cropped to the common verification domain.
7.5.1 PySTEPS
PySTEPS [6] is used as the classical transport-based ensemble baseline. We apply the
STEPS nowcasting method [5] through the official PySTEPS implementation, using
Lucas–Kanade motion estimation and a second-order autoregressive model. For each
sample, PySTEPS receives the 9-frame, 256 × 256 radar history and predicts the
subsequent 36 frames. The forecasts are then centre-cropped to the common 128 × 128
verification domain. This setting provides PySTEPS with broader spatial context than
the learned models, including upstream precipitation that may subsequently advect
into the verification domain. We generate four ensemble members using independent
random seeds for probabilistic evaluation.
7.5.2 SimVPv2
SimVPv2 [24] is used as the deterministic deep-learning baseline. We train it on the
same training split as MW-Nowcast using the official model implementation, with the
input and output lengths adjusted to 9 and 36 frames, respectively, and the input
tensor shape fixed at 128 × 128. To provide a strong deterministic baseline for the
high-intensity precipitation regime considered here, SimVPv2 is trained with the same
per-frame intensity-weighted MSE-plus-MAE reconstruction loss as the deterministic
pixel head of MW-Nowcast, including identical intensity-bin weights and equal coeffi-
cients for the MSE and MAE terms. This setting places the same emphasis on intense
precipitation in both deterministic predictors, allowing their comparison to focus more
directly on differences in model architecture. All other hyperparameters follow the
default optimiser and scheduler settings of the released code unless adjustment is
required by the modified input–output configuration.
22

7.5.3 NowcastNet
NowcastNet [11] is used as the physics-guided generative baseline. We retrain it on
our dataset using the official released code, with the input/output length adapted to
the 9-frame history and 36-frame forecast setting used in this paper. We then evaluate
the retrained model on the corresponding chronological held-out split under the same
preprocessing and reflectivity-space evaluation protocol as the other methods.
7.6 Evaluation settings and metrics
The primary forecast object in this paper is the ensemble itself. For selected figures
and thresholded summary comparisons that require a single field, we also report Prob-
ability Matched Mean (PMM) [26]. For a grid with S2 cells and K ensemble members,
let mi = K −1 PK k=1 x(k) i be the ensemble mean at cell i, and let ri be the rank of mi
among the S2 mean-field values. If Qens(p) denotes the empirical quantile of the pooled
ensemble values {x(k) j : j = 1, . . . , S2; k = 1, . . . , K}, the PMM field is computed as
˜xi = Qens
 ri − 1/2
S2

. (13)
Equivalently, PMM ranks the grid cells of the ensemble mean and replaces them with
values drawn from the pooled ensemble-value distribution according to the same rank
order. This retains the spatial organisation of the ensemble mean while avoiding some
intensity damping caused by arithmetic averaging.
All models operate in reflectivity-space (dBZ). When rain-rate-based thresholds
are needed for evaluation, we convert reflectivity to rain rate using the WSR-88DZ–R
relation [32]
Z = 300R1.4, Z = 10dBZ/10, (14)
which yields
R =
 10dBZ/10
300
1/1.4
. (15)
This conversion is applied only in evaluation and figure labelling, not in model training.
7.6.1 Grid metrics
Critical Success Index Neighbourhood (CSIN).Following the neighbourhood verifica-
tion used by NowcastNet [11], CSIN allows limited spatial displacement when assessing
threshold exceedances. We first convert the forecast and observation to rain rate and
form binary exceedance masks 1{R ≥ ρ}. Each mask is then dilated by taking the
maximum over a centred w × w grid-cell neighbourhood. Hits (TP w), false alarms
(FPw) and misses (FN w) are accumulated from the resulting neighbourhood masks
over all grid cells in the test set, giving
CSIN(ρ, w) = TPw
TPw + FPw + FNw
. (16)
23

We use the 5 × 5 neighbourhood adopted by NowcastNet unless a different window
is specified. For the regional quantitative comparison in Figure 4, we report CSIN at
ρ ∈ {16, 32, 64} mm h −1; other case and ensemble figures use ρ ∈ {32, 64} mm h −1.
When a method produces an ensemble, CSIN is reported on the PMM summary field
unless otherwise specified in a figure caption. Curves by forecast lead are computed
first and, where a single score is needed, averaged over the reported lead times.
Probability of Detection (POD).POD measures the fraction of observed threshold
exceedances that are detected by the forecast. Using the original pointwise threshold
masks, it is defined as
POD(ρ) = TP TP + FN. (17)
7.6.2 Probabilistic metrics
Continuous Ranked Probability Score (CRPS).CRPS [27] is computed directly from
the empirical ensemble distribution rather than from a fitted Gaussian. It measures
the distance between the forecast distribution and the observation, with lower val-
ues indicating better probabilistic forecasts. For an ensemble forecast {x(k)}K k=1 and
observation y, the grid-cell CRPS is
CRPS({x(k)}, y) = 1 K
KX
k=1

x(k) − y

 − 1 2K 2 KX k=1 KX l=1

x(k) − x(l)

 . (18)
We use K = 4 members for MW-Nowcast, PySTEPS, and NowcastNet when proba-
bilistic evaluation is reported. CRPS is computed in precipitation-space at the original
grid resolution, then averaged over all grid cells and lead times. Deterministic base-
lines are excluded from CRPS tables unless explicitly converted to a one-member
degenerate forecast.
Continuous Ranked Probability Skill Score (CRPSS).CRPSS reports the relative
improvement in CRPS over a reference forecast. We use a persistence forecast, obtained
by holding the latest observed radar field constant over the forecast horizon, as the
reference forecast when computing CRPSS. For a method with score CRPS model and
a reference score CRPS ref , we compute
CRPSS = 1 − CRPSmodel
CRPSref
. (19)
Higher CRPSS values indicate better probabilistic skill relative to the reference fore-
cast; a value of zero indicates equal skill to the reference, and negative values indicate
worse skill.
7.6.3 Relative economic value
Following the cost–loss decision framework used by DGMR [10] and standard ensemble
verification [30], we evaluate whether probabilistic forecasts can reduce the expense
of protective decisions. At a fixed region, forecast lead and rain-rate threshold ρ, each
24

grid cell and issue time defines a binary event. For aK-member forecast, the predicted
event probability is
bp = 1 K
KX
k=1
1
n
r(k) ≥ ρ o , (20)
where r(k) is the rain rate of member k; the verifying event is y = 1{robs ≥ ρ}. A user
takes protective action when bp ≥ γ, where γ ∈ [0, 1] is a probability decision threshold.
Taking action incurs cost C, whereas failing to act when the observed event occurs
incurs loss L. If NTP, NFP, NTN and NFN are the resulting contingency counts, the
mean forecast expense is
Ef (γ) = (NTP + NFP)C + NFNL NTP + NFP + NTN + NFN . (21)
Let pc be the observed climatological event frequency. The minimum expense of the
optimal climatological strategy and the expense of a perfect forecast are, respectively,
Ec = min(C, pcL), E p = pcC. (22)
Because the value depends on C and L only through the cost–loss ratio α = C/L,
we set L = 1 and C = α. For each α ∈ (0, 1), we sweep the attainable probability
thresholds γ and report the maximum relative economic value
REV(α) = max
γ
Ec − Ef (γ)
Ec − Ep
. (23)
This normalisation is algebraically equivalent to that used by DGMR: REV = 1 for a
perfect forecast, REV = 0 for the optimal climatological strategy, and negative values
indicate worse expense than climatology. We use K = 4 members and evaluate rain-
rate exceedances at ρ ∈ {16, 32} mm h−1 for lead times of 2, 4 and 6 h in each region.
Counts and climatological frequencies are pooled over all grid cells and samples in the
corresponding chronologically held-out compact test set. Deterministic predictions are
treated as degenerate one-member probabilities.
7.6.4 Structural diagnostic
Power Spectral Density (PSD).PSD [29] is used as a diagnostic of spatial structure.
For each lead time and field X ∈ RS×S, we compute the two-dimensional discrete
Fourier transform F (X) and its power spectrum
P (kx, ky) = 1 S2 |F (X)(kx, ky)|2 . (24)
The PSD curve is obtained by radially averaging P (kx, ky) over spatial wave number
k =
q
k2x + k2y. In figures, we plot forecast and observation PSD curves together at
selected forecast lead times. PSD is used as a structural diagnostic curve rather than
collapsed into a single scalar score.
25

7.7 Motivation for the residual formulation
All model inputs and outputs are radar reflectivity composites in dBZ on a fixed
Cartesian grid after preprocessing. Observed radar sequences combine relatively pre-
dictable storm-scale displacement with less predictable local growth, decay, merging,
splitting and convective initiation. For the following conceptual continuous-time state-
ment, X(t) denotes the continuously indexed reflectivity field corresponding to Xt,
and v(t) denotes the standard advection velocity. We express the physical motivation
as
∂X(t)
∂t = −v(t) · ∇X(t)| {z }
St (transport-dominated)
+ R(k) t|{z}
source-like residual
, (25)
where the underbraces indicate the modelling correspondence to the previously defined
deterministic prediction St and probabilistic residual R(k) t . Equation (25) is used only
as physical motivation: the model does not explicitly estimate v(t) or impose the
transport equation as a training constraint.
Radar reflectivity evolution over several hours contains components with different
predictability. Storm-scale displacement and broad precipitation organisation are often
partly constrained by the recent radar history, whereas local growth, decay, merging,
splitting and convective initiation become increasingly uncertain with lead time. This
motivates the decomposition in Eq. (1): the deterministic prediction S1:T represents
the shared forecast structure supported by the observed history, while the probabilistic
residual R(k) 1:T represents member-dependent local departures from that shared struc-
ture. This decomposition is not imposed by an explicit advection equation; instead,
the allocation between deterministic structure and probabilistic residual variability is
learned jointly from data.
8 Data availability
The US severe-weather event records used in this study were obtained from the
NOAA/NCEI Storm Events Database through the official NCEI bulk-data archive
(https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/). The correspond-
ing radar observations were obtained from the NOAA Multi-Radar/Multi-Sensor
(MRMS) system, for which official data-access information is available at https://
www.nssl.noaa.gov/projects/mrms/MRMS data.php. The European severe-weather
event records were obtained from the European Severe Weather Database (ESWD;
https://www.eswd.eu/), operated by the European Severe Storms Laboratory, and
were used in accordance with the ESWD User’s Agreement. The European maximum-
reflectivity radar mosaics were obtained from EUMETNET OPERA under licence;
access to these data requires application to and approval by EUMETNET. The China
dataset was constructed from composite reflectivity data provided by the China Mete-
orological Administration (CMA); access to these data requires application to and
approval by CMA.
26

9 Code availability
The model code and trained checkpoints for MW-Nowcast will be made publicly avail-
able upon publication at https://github.com/microsoft/MW-Nowcast. The baseline
implementations are based on PySTEPS (https://github.com/pySTEPS/pysteps),
NowcastNet (https://doi.org/10.24433/CO.0832447.v1) and OpenSTL (https://
github.com/chengtan9907/OpenSTL).
10 Acknowledgements
We acknowledge the National Centers for Environmental Information (NCEI) for the
NOAA Storm Events Database, the National Oceanic and Atmospheric Administra-
tion (NOAA) for the Multi-Radar Multi-Sensor (MRMS) products, the European
Severe Storms Laboratory (ESSL) for the European Severe Weather Database
(ESWD), EUMETNET OPERA for the European radar mosaics, and the China
Meteorological Administration (CMA) for the composite reflectivity data used in this
study.
11 Contributions
H.D., N.W. and Z.F. conceived the study and designed the overall methodology. Z.F.
and Z.L. curated and processed the datasets. Z.F. and N.W. implemented the exper-
imental pipeline, performed the experiments and analysed the results. S.Q., P.Z. and
S.X. maintained the operational data pipelines. N.W. drafted the initial manuscript.
W.J. substantially revised the manuscript and led its scientific framing, including the
central story, claims and interpretation of the results. J.W., R.E.T., K.T., N.W., Z.F.
and H.D. contributed to the scientific framing, interpretation of the results and revi-
sion of the manuscript. J.B. and H.X. reviewed the manuscript and provided feedback.
M.C., H.S., J.K. and K.T. contributed to product requirements and operational con-
text. N.G., B.Z., L.Z., D.D., Q.Z., H.S., K.T. and S.I. provided scientific and strategic
guidance and project oversight. H.D. supervised and coordinated the study. All authors
reviewed and approved the final manuscript.
12 Competing interests
The authors declare no competing interests.
27

Extended Data Figures
AL
AR
MS
TN
Start: 2025-06-19 09:10 UTC
Center: 35.42°N, 89.55°W
Patch: 34.13°N-36.71°N | 90.84°W-88.26°W
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
4
8
12
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
0.75
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.00
0.25
0.50
0.75
CSIN5@32 (↑ better)
0.0
0.2
0.4
0.6
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 1 US flash-flood precipitation forecast. The case is located in Tipton
County, Tennessee, on 19 June 2025, and the forecast is initialised at 09:10 UTC. The observed
sequence shows an organised heavy-precipitation band moving from the northwestern part of the
forecast patch towards the southeast. The band remains relatively continuous during the first half of
the 6 h window, before the main precipitation shifts towards the southern to southeastern part of the
patch and locally weakens at later lead times. Embedded intense cores repeatedly reorganise during
this evolution, making the case sensitive to rain-band displacement, core retention and late-lead
structural evolution. All Extended Data case figures use the same five-panel layout:a, Geographic and
radar context, with the forecast domain outlined in orange. b, Forecast diagnostics: CSIN in a 5 × 5
grid-cell neighbourhood at rain-rate thresholds of 32 and 64 mm h −1, CRPS, CRPSS, and radially
averaged PSD at lead times of 3 and 6 h. “Deterministic” denotes the output of the deterministic
decoder of MW-Nowcast. c, Observed and predicted rain-rate fields at hourly lead times from 1 to 6
h. Rows show observations, PySTEPS, SimVPv2, NowcastNet and MW-Nowcast. d, CSIN and POD
at thresholds of 32 and 64 mm h −1 for the four MW-Nowcast ensemble members and their PMM
summary. e, The deterministic prediction and four ensemble members at lead times of 2, 4 and 6 h.
28

CT
DEMD
MA
NH
NJ
PA
RI
VT
Start: 2025-07-14 19:30 UTC
Center: 41.10°N, 74.02°W
Patch: 39.81°N-42.39°N | 75.31°W-72.73°W
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.3
0.5
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.3
0.5
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.3
0.6
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.1
0.2
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 2 US thunderstorm-wind convective precipitation forecast. The case
is located in Rockland County, New York, on 14 July 2025, and the forecast is initialised at 19:30
UTC. The observed sequence shows convective precipitation moving generally eastward and becoming
more organised into a coherent rain band during the first half of the forecast window. At later lead
times, the precipitation coverage contracts, and the embedded intense cores weaken and become
more fragmented. This case tests whether a model can retain rain-band structure during convective
organisation while representing the subsequent contraction and decay of high-intensity cores. Panel
descriptions are as in Extended Data Fig. 1.
29

IA
KS MO
NE
Start: 2025-04-24 21:20 UTC
Center: 41.20°N, 96.03°W
Patch: 39.91°N-42.49°N | 97.32°W-94.74°W
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
4
8
12
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
0.75
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 3 US hail-associated convective precipitation forecast. The case is
located in Douglas County, Nebraska, on 24 April 2025, and the forecast is initialised at 21:20 UTC.
The observed sequence shows a convective echo field moving generally eastward and expanding across
the forecast patch, with intense precipitation organised as several compact local cores rather than a
single continuous rain band. These cores repeatedly develop, split and reorganise during the 6 h win-
dow, making the case sensitive to convective-core initiation, displacement and multi-core structural
retention. Panel descriptions are as in Extended Data Fig. 1.
30

Start: 2025-07-24 14:50 UTC
Center: 39.19°N, 115.15°E
Patch: 37.91°N-40.47°N | 113.87°E-116.43°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
4
8
12
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.8
−0.4
0.0
0.4
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 4 Mountainous heavy-rainfall forecast over western Hebei. The fore-
cast patch is centred near Yi County, Baoding, and is initialised at 14:50 UTC on 24 July 2025.
The observed sequence shows persistent heavy precipitation that remains active within the forecast
patch and gradually expands, while the main rain area retains broad spatial continuity. Peak inten-
sity weakens at later lead times, but embedded local intense cores continue to reorganise. This case
tests whether a model can retain rain-area extent and structure in a persistent mountainous rainfall
setting while representing the weakening and reorganisation of local intense cores. Panel descriptions
are as in Extended Data Fig. 1.
31

Start: 2026-05-17 08:20 UTC
Center: 29.67°N, 111.73°E
Patch: 28.39°N-30.95°N | 110.45°E-113.01°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.3
0.0
0.3
0.6
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 5 Hunan Shimen mountainous heavy-rainfall forecast. This forecast
window forms part of the May 2026 heavy-rainfall episode in Shimen County, Hunan, during which
public reports documented six deaths and ten missing people. The forecast is initialised at 08:20
UTC on 17 May 2026. The observed sequence shows a persistent heavy-precipitation system moving
generally eastward and expanding across the forecast patch. Embedded intense cores remain strong
through the 6 h window and locally reorganise as the rain area expands. This case tests whether a
model can retain high-intensity cores and coherent rain-area structure in a moving and expanding
mountainous rainfall system. Panel descriptions are as in Extended Data Fig. 1.
32

Start: 2026-05-14 22:10 UTC
Center: 25.41°N, 107.57°E
Patch: 24.13°N-26.69°N | 106.29°E-108.85°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
4
8
12
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 6 Guizhou Guiding–Majiang heavy-rainfall forecast. This forecast
window forms part of the 15–20 May 2026 rainstorm episode in Guizhou; an official disaster summary
reported 19 people dead or missing across Guiding, Majiang and several other counties. The forecast
is initialised at 22:10 UTC on 14 May 2026. The observed sequence shows a heavy-precipitation
system moving generally eastward and gradually contracting after the middle of the forecast window.
Although precipitation coverage decreases, embedded intense cores persist and locally reorganise.
This case tests whether a model can retain the placement, intense cores and late-lead organisation of
a moving heavy-rainfall system during contraction and structural adjustment. Panel descriptions are
as in Extended Data Fig. 1.
33

Start: 2024-05-23 12:44 UTC
Center: 47.85°N, 9.51°E
Patch: 46.57°N-49.13°N | 8.24°E-10.79°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.2
0.4
CSIN5@32 (↑ better)
0.1
0.2
0.3
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.2
0.4
0.6
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 7 European lightning-associated convective precipitation forecast.
The case is located in southern Germany on 23 May 2024, and the forecast is initialised at 12:44
UTC. The observed sequence shows organised convective precipitation moving generally eastward and
expanding through the first two-thirds of the forecast window. The precipitation area then contracts
modestly, while embedded intense cores persist and locally reorganise along the main rain area. This
case tests whether a model can retain rain-area continuity and intense-core structure in a moving and
expanding convective system while representing the later modest contraction. Panel descriptions are
as in Extended Data Fig. 1.
34

Start: 2024-03-03 00:30 UTC
Center: 43.70°N, 7.25°E
Patch: 42.42°N-44.98°N | 5.97°E-8.53°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
4
8
12
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.50
−0.25
0.00
0.25
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.2
0.4
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 8 European tornado-associated convective precipitation forecast.
The case is located in southern France on 3 March 2024, and the forecast is initialised at 00:30 UTC.
The observed sequence shows a slowly moving precipitation system that expands through the 6 h
window. Intense precipitation is organised mainly as multiple compact cores that repeatedly develop,
split and reorganise, rather than as a stable single rain band. This case tests whether a model can
represent local core initiation, displacement and morphology changes within a slowly moving but
expanding convective system. Panel descriptions are as in Extended Data Fig. 1.
35

Start: 2024-06-08 18:00 UTC
Center: 44.07°N, 0.45°W
Patch: 42.79°N-45.35°N | 1.73°W-0.83°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.8
−0.4
0.0
0.4
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.0
0.2
0.4
0.6
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Extended Data Fig. 9 European heavy-precipitation forecast over southwestern F rance.
The case is located in southwestern France on 8 June 2024, and the forecast is initialised at 18:00 UTC.
The observed sequence shows a slowly moving heavy-precipitation area that expands substantially
through the 6 h window, gradually forming a broader and more continuous rain region. Embedded
intense cores continue to reorganise within the main rain area rather than rapidly moving out of the
forecast patch. This case tests whether a model can retain rain-area extent, spatial continuity and
local intense-core evolution in a slowly moving and steadily expanding heavy-precipitation system.
Panel descriptions are as in Extended Data Fig. 1.
36

0.1 16 32 64 96 128
10
−6
10
−5
10
−4
10
−3
10
−2
10
−1
10
0
10
1
Density
a US
R ≥ 16
0.1 16 32 64 96 128
Rain rate (mm h−1)
b EU
R ≥ 16
P(R ≥ 16)
Deter  4.0%
Label  7.4%
0.1 16 32 64 96 128
c CN
R ≥ 16
P(R ≥ 16)
Deter
PMM
Label
Deterministic prediction PMM ensemble Label
PMM 11.1%
P(R ≥ 16)
Deter  2.8%
Label  7.5%
PMM 6.4% 7.4%
10.5%
4.3%
Extended Data Fig. 10 Regional rain-rate distributions and high-intensity-tail recov-
ery . a–c, Conditional rain-rate densities pooled over 4,000 held-out events in the United States
(US), Europe (EU) and China (CN), respectively. Densities use effective-rain pixels with 0 .1 ≤ R <
128 mm h −1. Blue solid curves show the deterministic branch, orange solid curves show the Proba-
bility Matched Mean (PMM) ensemble summary, and black dashed curves show ground truth. The
shaded region marks the high-intensity tail, R ≥ 16 mm h −1, corresponding to the lower high-rain
threshold used in the regional quantitative evaluation. Insets report pooled pixel–time exceedance
probability conditional on the displayed rain-rate range. Across all three regions, PMM recovers sub-
stantially more high-intensity probability mass than the deterministic branch and closely approaches
the observed tail.
37

Supplementary Information
1 Related works
1.1 Historical perspective
Precipitation nowcasting has developed along two complementary lines: extrapolating radar-echo motion
and learning nonlinear evolution from radar sequences. Classical radar nowcasting starts from the obser-
vation that short-lead precipitation fields often contain a strong advective component. Echo motion is
estimated from recent radar frames and then extrapolated into the future. STEPS and its PySTEPS
implementation extend this idea by combining scale-dependent extrapolation with stochastic perturba-
tions, yielding fast and interpretable ensemble forecasts [5, 6]. Related optical-flow and radar-tracking
methods also exploit motion information in recent radar observations and remain valuable in rapidly
updated operational settings [33]. Their limitation is that severe convective precipitation is not a pas-
sive tracer. As lead time extends towards 3–6 h, local growth, decay, merging, splitting and initiation
become increasingly important, making pure extrapolation insufficient for maintaining intense cores and
organised precipitation structure [1, 3].
Deep learning broadened the modelling capacity of radar nowcasting by learning nonlinear spa-
tiotemporal evolution from large radar archives. ConvLSTM formulated precipitation nowcasting as
convolutional recurrent sequence prediction, and later models such as PredRNN, EarthFormer and
SimVPv2 further improved the representation of spatiotemporal dependencies [7–9, 24]. These deter-
ministic models can capture morphology beyond linear extrapolation, but point-wise training losses tend
to average over multiple plausible futures, weakening intense echoes at longer lead times. Generative
radar nowcasting models address this limitation by sampling multiple future fields. DGMR showed that
deep generative models can produce useful probabilistic precipitation nowcasts, and NowcastNet further
demonstrated the value of incorporating physical structure for extreme-precipitation nowcasting [10, 11].
Together, these studies show that long-lead extreme-precipitation nowcasting requires both the retention
of predictable structure supported by the recent radar history and the representation of uncertain local
evolution.
1.2 Diffusion-based and flow-based nowcasting
Recent diffusion and flow-based nowcasting studies extend generative radar forecasting along complemen-
tary directions. PreDiff and LDCast use latent diffusion to make probabilistic precipitation nowcasting
tractable while representing forecast uncertainty [17, 18]. StormDiT brings latent rectified-flow transform-
ers into the 2–6 h precipitation nowcasting grey zone, and FlowCast explores conditional flow matching
for precipitation nowcasting [19, 34]. CasCast and DiffCast use cascaded or residual formulations to con-
nect deterministic evolution with stochastic refinement [35, 36]. Together, these studies suggest a useful
principle for longer-range nowcasting: forecast uncertainty should be represented explicitly, while the
more predictable component of storm evolution should remain structurally anchored.
MW-Nowcast follows this principle but makes a different set of modelling choices. Several existing
diffusion nowcasting systems operate in latent space, which improves tractability but can make the
recovery of compact high-intensity radar structures more dependent on the decoder. Other cascaded or
residual systems separate deterministic prediction from stochastic refinement, so the residual model is
trained relative to a fixed or separately trained forecast. In contrast, MW-Nowcast is a pixel-level, end-
to-end flow-matching ensemble nowcaster. It pairs a deterministic decoder, which provides the shared
predictable forecast structure, with a probabilistic residual decoder, which samples local growth, decay,
reorganisation and initiation around that shared forecast. Because the residual target is recomputed as
the deterministic prediction changes during joint training, the two branches learn the decomposition
together rather than forming a fixed post-processing cascade.
This distinction motivates the ablation experiments reported below. We compare pixel- and
latent-space configurations, and use controlled comparisons to test an explicit deterministic-prediction–
probabilistic-residual decomposition against a single generative head, joint end-to-end training against a
two-stage residual cascade, and flow matching against an EDM diffusion objective.
2 Ablation study
The ablation study evaluates which modelling choices contribute to the skill of MW-Nowcast. All compar-
ison variants are evaluated on the held-out US test set described in the main text, using the same 9-frame
38

input, 36-frame output and 6 h nowcasting protocol as the main quantitative comparison. We compare
MW-Nowcast with five variants:Latent, OneStage, TwoStage, EDM-ODE and EDM-SDE. These comparisons
examine generation space, decoder decomposition, training strategy and probabilistic objective.
2.1 Decoder coupling and training strategy
The OneStage and TwoStage variants examine the design hypotheses underlying the deterministic-
prediction–probabilistic-residual formulation and the way this decomposition is learned. OneStage
removes the explicit deterministic decoder and uses a single flow-matching generative head to produce
the complete future sequence directly. Its lower CSIN 5 across all reported thresholds and lead times
suggests that directly generating the full forecast sequence provides a less effective basis for detecting
intense precipitation. One possible explanation is that a single generator must represent both the large-
scale, relatively predictable evolution and the smaller-scale uncertain departures, whereas the explicit
decomposition allows these components to be handled by specialised decoders.
TwoStage retains the deterministic decoder and residual decoder but trains them sequentially: the
deterministic decoder is trained first, and the residual decoder is then trained against a fixed residual
target. Compared with OneStage, this configuration recovers part of the skill at the 32 and 64 mm h −1
thresholds, supporting the value of an explicit deterministic forecast anchor. However, it remains weaker
than MW-Nowcast at all representative lead times and in the mean over the full forecast horizon reported
in Supplementary Table 1. This remaining gap may arise because the residual decoder is learned from
predictions produced by a fixed deterministic model. Joint optimisation in MW-Nowcast instead allows
the shared representation, deterministic prediction and probabilistic residual target to adapt together
during training.
2.2 Generation space and diffusion objective
The Latent variant represents an alternative generative design that moves forecasting from radar-pixel
space to a compact V AE latent space. Its consistently lower CSIN 5 suggests that this configuration
retains less information relevant to intense-precipitation detection. A plausible contributing factor is the
compression and reconstruction process, which may smooth compact precipitation cores or attenuate
local extremes, causing fewer locations to exceed the high rain-rate thresholds after decoding. This effect
is particularly relevant at high thresholds, where even modest attenuation can change whether an intense
precipitation feature is detected.
The EDM-ODE and EDM-SDE variants retain the two-branch architecture and joint training setting, but
replace the flow-matching residual objective used in MW-Nowcast with an EDM diffusion objective. They
differ only in the sampling procedure: EDM-ODE uses deterministic ODE sampling, whereas EDM-SDE uses
stochastic sampling with added noise. MW-Nowcast achieves higher CSIN 5 than both EDM variants in
every reported column, indicating a consistent advantage for flow matching under the evaluated setting.
The absolute differences are nevertheless modest, particularly at the highest threshold and longest lead
times, and are consistent with flow matching being well suited to learning the residual transformation
rather than identifying the probabilistic objective as the dominant source of improvement.
Taken together, the ablation results provide consistent empirical support for the main design hypothe-
ses of MW-Nowcast. The clearest gains are associated with combining an explicit deterministic forecast
anchor with probabilistic residual generation and optimising the two components jointly. The full pixel-
space configuration performs best among the evaluated generation designs, while flow matching provides
a further, more modest improvement over the EDM alternatives.
Supplementary Table 1 summarises the quantitative comparison using CSIN 5 at representative lead
times and as a mean over the complete 6 h forecast horizon.
Supplementary Fig. 1 complements these aggregate results with a qualitative comparison for a rep-
resentative strong-precipitation case. The example illustrates how the alternative configurations differ
in their ability to retain compact intense precipitation cores and organised storm structure as lead time
increases.
39

Supplementary T able 1 CSIN5 comparison of MW-Nowcast ablation variants on the held-
out US test set. Neighbourhood Critical Success Index with a 5 × 5 neighbourhood is reported at
rain-rate thresholds of 16, 32 and 64 mm h −1 for representative lead times T+2 h, T+4 h and T+6 h,
together with the arithmetic mean of the unsmoothed per-lead scores over all 36 lead times from T+10
min to T+6 h. Higher is better. The best displayed value in each column is shown in bold.
Model T+2 h T+4 h T+6 h Mean
16 32 64 16 32 64 16 32 64 16 32 64
MW-Nowcast 0.284 0.214 0.160 0.197 0.129 0.085 0.095 0.055 0.032 0.256 0.194 0.147
Latent 0.216 0.147 0.099 0.155 0.100 0.062 0.072 0.038 0.021 0.204 0.144 0.103
OneStage 0.239 0.168 0.118 0.164 0.096 0.058 0.078 0.039 0.021 0.225 0.164 0.121
TwoStage 0.233 0.174 0.129 0.163 0.114 0.079 0.073 0.044 0.027 0.218 0.169 0.130
EDM-ODE 0.247 0.181 0.129 0.187 0.126 0.085 0.075 0.046 0.027 0.235 0.178 0.134
EDM-SDE 0.244 0.178 0.127 0.186 0.126 0.085 0.068 0.042 0.025 0.234 0.177 0.133
40

Observation
 T + 1h
 T + 2h
 T + 3h
 T + 4h
 T + 5h
 T + 6h
Latent
OneStage
TwoStage
EDM-ODE
EDM-SDE
MW-Nowcast
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
Supplementary Fig. 1 Visual comparison of MW-Nowcast ablation variants for a held-out US
strong-precipitation case. The forecast is initialised at 09:00 UTC on 13 February 2025 for a patch centred
near 29.4 ◦N, 87.5 ◦W. The figure includes the input context and the subsequent 6 h forecast evolution. Rows
compare the observed fields, MW-Nowcast and the comparison variantsLatent, OneStage, TwoStage, EDM-ODE and
EDM-SDE. The case illustrates how the ablated design choices affect the retention of compact intense precipitation
cores and organised storm structure over the forecast horizon.
41

3 Flow-matching visualisation
This section visualises how the residual decoder in MW-Nowcast constructs ensemble members. Sup-
plementary Figs. 2 and 3 show single-member residual trajectories, illustrating how Gaussian noise is
transformed into a structured probabilistic residual and then added to the deterministic prediction. Sup-
plementary Figs. 4 and 5 show how multiple members diverge along the same learned flow, revealing
where ensemble uncertainty is concentrated.
3.1 Single-member residual construction
For a fixed forecast lead time, the residual flow evolves from a Gaussian sample atτ = 0 to a probabilistic
residual at τ = 1, using the same Heun ODE solver as in deployment. Adding this probabilistic residual
to the deterministic prediction yields the final prediction for that ensemble member. Supplementary
Figs. 2 and 3 show this construction for a US hail case and a European thunderstorm case, each at lead
times T+4 h, T+5 h and T+6 h.
In every panel, the top row traces the probabilistic residual as it evolves from noise at τ = 0 .00
to a structured field at τ = 1.00, and the bottom row shows the corresponding prediction obtained by
adding the evolving probabilistic residual to the deterministic prediction. The right-hand column reports
the deterministic prediction and the ground-truth observation for reference. The trajectories show that
the probabilistic residual is not unstructured noise, but a spatially organised correction that modifies
precipitation cores and fine-scale structure around the deterministic forecast.
42

= 0.00
 = 0.15
 = 0.35
 = 0.50
 = 0.65
 = 0.85
 = 1.00
Probabilistic Residual Deterministic transport
Prediction Ground truth
(a) Lead time T+4 h.
= 0.00
 = 0.15
 = 0.35
 = 0.50
 = 0.65
 = 0.85
 = 1.00
Probabilistic Residual Deterministic transport
Prediction Ground truth
(b) Lead time T+5 h.
= 0.00
 = 0.15
 = 0.35
 = 0.50
 = 0.65
 = 0.85
 = 1.00
Probabilistic Residual Deterministic transport
Prediction Ground truth
(c) Lead time T+6 h.
Supplementary Fig. 2 Flow-matching construction of the probabilistic residual for a US hail case.
The case was reported at 23:07 UTC on 19 October 2024 near 33.87 ◦N, 104.59◦W, with the radar clip spanning
20:07 UTC on 19 October to 05:07 UTC on 20 October over a patch of approximately 31.29–36.45◦N and 107.17–
102.01◦W. For each lead time, the top row shows the probabilistic residual evolving along the flow-matching
trajectory from a Gaussian sample at τ = 0.00 to its terminal state at τ = 1.00, and the bottom row shows the
prediction formed by adding the evolving probabilistic residual to the deterministic prediction. The right-hand
column gives the deterministic prediction (top) and the ground-truth observation (bottom).
43

= 0.00
 = 0.15
 = 0.35
 = 0.50
 = 0.65
 = 0.85
 = 1.00
Probabilistic Residual Deterministic transport
Prediction Ground truth
(a) Lead time T+4 h.
= 0.00
 = 0.15
 = 0.35
 = 0.50
 = 0.65
 = 0.85
 = 1.00
Probabilistic Residual Deterministic transport
Prediction Ground truth
(b) Lead time T+5 h.
= 0.00
 = 0.15
 = 0.35
 = 0.50
 = 0.65
 = 0.85
 = 1.00
Probabilistic Residual Deterministic transport
Prediction Ground truth
(c) Lead time T+6 h.
Supplementary Fig. 3 Flow-matching construction of the probabilistic residual for a European
thunderstorm case. The radar clip spans 07:50–15:50 UTC on 15 May 2024 over the Alpine region, with
the patch centred near 46.04 ◦N, 8.67 ◦E and covering approximately 43.38–48.50 ◦N and 6.31–11.43 ◦E. Layout
follows Supplementary Fig. 2: the top row of each panel traces the probabilistic residual along the flow-matching
trajectory and the bottom row shows the resulting prediction, with the deterministic prediction and ground-truth
observation in the right-hand column.
44

3.2 Ensemble divergence along the flow
The single-member trajectories above show how one realisation of the probabilistic residual is constructed,
but they do not show how ensemble members separate from one another. Because all members share the
same deterministic prediction and differ only in the Gaussian sample drawn atτ = 0, member-to-member
spread is a direct visualisation of the conditional uncertainty represented by the residual decoder.
Supplementary Figs. 4 and 5 show four independently sampled members for the same two cases and
lead times. Section A shows residual fields at τ = 0.75 and τ = 1.00, when the residual has developed
structured precipitation-related features. Section B summarises the converged residual ensemble using
the per-pixel ensemble mean and standard deviation at τ = 1.00. The standard deviation concentrates
near precipitation cores and edges rather than spreading uniformly across the domain, indicating that
the residual decoder expresses uncertainty around meteorologically active structures.
45

member 1
 member 2
 member 3
 member 4
 mean ( = 1)
std ( = 1)
= 0.75
= 1.00
A  Ensemble members B  Mean & std
(a) Lead time T+4 h.
member 1
 member 2
 member 3
 member 4
 mean ( = 1)
std ( = 1)
= 0.75
= 1.00
A  Ensemble members B  Mean & std
(b) Lead time T+5 h.
member 1
 member 2
 member 3
 member 4
 mean ( = 1)
std ( = 1)
= 0.75
= 1.00
A  Ensemble members B  Mean & std
(c) Lead time T+6 h.
Supplementary Fig. 4 Ensemble divergence of the probabilistic residual for a US hail case.The case
was reported at 23:07 UTC on 19 October 2024 near 33.87◦N, 104.59◦W. Four members (seeds 1–4) are integrated
along the flow from independent Gaussian samples. Section A: the probabilistic residual for each member at
flow positions τ = 0 .75 (top row) and τ = 1 .00 (bottom row). Section B: the per-pixel ensemble mean (top)
and standard deviation (bottom) of the probabilistic residual at τ = 1.00. The standard deviation localises along
precipitation cores and edges, showing where the probabilistic residual contributes the most uncertainty.
46

member 1
 member 2
 member 3
 member 4
 mean ( = 1)
std ( = 1)
= 0.75
= 1.00
A  Ensemble members B  Mean & std
(a) Lead time T+4 h.
member 1
 member 2
 member 3
 member 4
 mean ( = 1)
std ( = 1)
= 0.75
= 1.00
A  Ensemble members B  Mean & std
(b) Lead time T+5 h.
member 1
 member 2
 member 3
 member 4
 mean ( = 1)
std ( = 1)
= 0.75
= 1.00
A  Ensemble members B  Mean & std
(c) Lead time T+6 h.
Supplementary Fig. 5 Ensemble divergence of the probabilistic residual for a European thunder-
storm case. The case occurred on 15 May 2024 over the Alpine region, with the patch centred near 46.04 ◦N,
8.67◦E. Layout follows Supplementary Fig. 4: Section A shows four members at τ = 0 .75 and τ = 1 .00, and
Section B shows the ensemble mean and standard deviation of the probabilistic residual at τ = 1.00.
47

4 Additional quantitative results
4.1 Supplementary verification metrics
The main text defines the core metrics used in its figures and quantitative results, including CSIN, POD,
CRPS, CRPSS, REV and PSD. Here we give additional details for the supplementary diagnostic metrics
reported below.
False Alarm Ratio (F AR).F AR measures the fraction of forecast threshold exceedances that are not
observed. Using the pooled threshold-contingency counts, it is defined as
F AR(ρ) = FP TP + FP, (S1)
where lower values are better.
Neighbourhood Critical Success Index (CSIN).CSIN allows a spatial tolerance around threshold
exceedances. Let Oρ(p) = 1{y(p) ≥ ρ} and Fρ(p) = 1{x(p) ≥ ρ} be the observed and forecast binary
fields at grid cell p, and let Nn(p) denote the centred n × n neighbourhood of p. We dilate both binary
fields using
Omax ρ,n (p) = max q∈Nn(p) Oρ(q), F max ρ,n (p) = max q∈Nn(p) Fρ(q). (S2)
After pooling the contingency counts TP n, FPn and FNn from these dilated fields over the test set, we
compute
CSINn(ρ) = TPn TPn + FPn + FNn . (S3)
Values outside the domain are treated as non-events. In the tables and figures below, the subscript
denotes the centred neighbourhood width in grid cells.
Fractions Skill Score (FSS).FSS [37] compares neighbourhood event fractions. For the same binary
fields, define
oρ,n(p) = 1 n2 X q∈Nn(p) Oρ(q), f ρ,n(p) = 1 n2 X q∈Nn(p) Fρ(q). (S4)
The score for one forecast field is
FSSn(ρ) = 1 −
P
p [fρ,n(p) − oρ,n(p)]2 P
p fρ,n(p)2 + P p oρ,n(p)2 . (S5)
Higher values are better and a perfect forecast has value 1. We compute FSS per sample and lead time
and then average the valid scores for each reported threshold and neighbourhood window.
4.2 Regional quantitative diagnostics
To complement the lead-time curves in the main text, Supplementary Table 2 reports neighbourhood
Critical Success Index with a 5 × 5 neighbourhood (CSIN 5) at the three high rain-rate thresholds (16, 32
and 64 mm h −1). The table gives both representative lead-time values at T+2 h, T+4 h and T+6 h and
the mean over all 36 lead times from T+10 min to T+6 h. These values are computed from the same
regional evaluation data as the main-text high-threshold comparison and provide a compact numerical
reading of the regional CSIN5 curves. Across all regions and thresholds, MW-Nowcast retains the highest
CSIN5, with the advantage remaining clear at later lead times and heavier precipitation thresholds.
Supplementary Figs. 6–8 provide diagnostic views that complement the main-text CSIN 5 and CRPS
results. Supplementary Fig. 6 shows that MW-Nowcast maintains substantially higher POD across
regions and thresholds, while its F AR is generally lower than that of PySTEPS and comparable to that
of NowcastNet. Although SimVPv2 often produces a lower F AR, this is accompanied by markedly lower
POD, indicating more frequent missed events.
Supplementary Fig. 7 shows that the advantage of MW-Nowcast persists as the FSS neighbourhood
broadens from 5 × 5 to 25 × 25 grid cells. From T+1 h onwards, it achieves the highest FSS for every
evaluated region–threshold–neighbourhood combination, indicating that the improvement is not specific
to the neighbourhood used in the main comparison.
Supplementary Fig. 8 extends the PSD and REV diagnostics to EU and CN. MW-Nowcast remains
closer to the observed spectra at T+2 h, T+4 h and T+6 h, while retaining positive economic value over
a broader range of cost–loss ratios than the baselines, particularly at the longer lead times.
48

0.0
0.5
1.0 Precip. ≥  16 mm h−1
0.0
0.5
1.0 Precip. ≥  16 mm h−1Precip. ≥  32 mm h−1 Precip. ≥  32 mm h−1Precip. ≥  64 mm h−1 Precip. ≥  64 mm h−1
0.0
0.5
1.0
0.0
0.5
1.0
0 1 2 3 4 5 6
Lead time (h)
0.0
0.5
1.0
0 1 2 3 4 5 6
Lead time (h)
0.0
0.5
1.0
0 1 2 3 4 5 6
Lead time (h)
0 1 2 3 4 5 6
Lead time (h)
0 1 2 3 4 5 6
Lead time (h)
0 1 2 3 4 5 6
Lead time (h)
USEUCN
POD FARa b
MW-Nowcast NowcastNet SimVPv2 PySTEPS
Supplementary Fig. 6 Pointwise detection and false-alarm characteristics across regions.Rows show
the US, EU and CN test sets, and columns show rain-rate thresholds of 16, 32 and 64 mm h −1. a, Probability of
detection (POD). b, False alarm ratio (F AR). Both metrics are computed from pointwise threshold exceedances
over lead times from T+10 min to T+6 h. Curves compare MW-Nowcast with NowcastNet, SimVPv2 and
PySTEPS. Higher values are better for POD, whereas lower values are better for F AR.
49

0.0
0.5
1.0 Precip. ≥  16 mm h−1
0.0
0.5
1.0 Precip. ≥  16 mm h−1Precip. ≥  32 mm h−1 Precip. ≥  32 mm h−1Precip. ≥  64 mm h−1 Precip. ≥  64 mm h−1
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0.0
0.5
1.0
0 1 2 3 4 5 6
Lead time (h)
0.0
0.5
1.0
0 1 2 3 4 5 6
Lead time (h)
0.0
0.5
1.0
0 1 2 3 4 5 6
Lead time (h)
0 1 2 3 4 5 6
Lead time (h)
0 1 2 3 4 5 6
Lead time (h)
0 1 2 3 4 5 6
Lead time (h)
USEUCN
a FSS: 5 × 5 grids FSS: 11 × 11 grids
FSS: 17 × 17 grids FSS: 25 × 25 grids
b FSS: 5 × 5 grids FSS: 11 × 11 grids
FSS: 17 × 17 grids FSS: 25 × 25 grids
c FSS: 5 × 5 grids FSS: 11 × 11 grids
FSS: 17 × 17 grids FSS: 25 × 25 grids
MW-Nowcast NowcastNet SimVPv2 PySTEPS
Supplementary Fig. 7 FSS sensitivity to neighbourhood size across regions. a, US; b, EU; c, CN.
Within each regional block, the upper row reports FSS for 5×5 and 11×11 grid-cell neighbourhoods, and the lower
row reports FSS for 17 × 17 and 25 × 25 neighbourhoods. For each neighbourhood size, columns show rain-rate
thresholds of 16, 32 and 64 mm h −1. Curves compare MW-Nowcast with NowcastNet, SimVPv2 and PySTEPS
over lead times from T+10 min to T+6 h. Higher values indicate better neighbourhood-scale forecast skill.
50

−20
0
25
50
T+2h
0.0
0.1
0.2
0.3
0.4
T+2hT+4h T+4hT+6h T+6h
256 64 16 4
Wavelength (km)
−20
0
25
50
10−2 10−1 100
Cost-loss ratio
0.0
0.1
0.2
0.3
0.4
256 64 16 4
Wavelength (km)
10−2 10−1 100
Cost-loss ratio
256 64 16 4
Wavelength (km)
10−2 10−1 100
Cost-loss ratio
EUCN
a b
PSD REV
≥ 16 mm h−1 ≥ 32 mm h−1
Observed MW-Nowcast NowcastNet SimVPv2 PySTEPS
Supplementary Fig. 8 Structural and relative economic value diagnostics for the EU and CN
regions. The upper row shows the EU test set and the lower row shows the CN test set. a, Radially averaged
power spectral density (PSD) at T+2 h, T+4 h and T+6 h. The observed spectrum is shown together with forecast
spectra from MW-Nowcast, NowcastNet, SimVPv2 and PySTEPS; closer agreement with the observed spectrum
indicates better preservation of multiscale precipitation structure. b, Standard pixel-wise relative economic value
(REV) at the same lead times as a function of cost–loss ratio. Solid and dashed curves denote rain-rate thresholds
of 16 and 32 mm h−1, respectively. Positive REV indicates lower expected expense than the optimal climatological
strategy, and higher values indicate greater economic value under the corresponding cost–loss setting.
51

5 Additional extended precipitation cases
The main text and appendix show representative examples from the US, EU and CN regions. Here we
add two additional cases for each region and two additional US ablation examples. The regional cases
broaden the qualitative coverage across storm types and geographic settings, whereas the ablation cases
complement Supplementary Fig. 1 by showing how the comparison variants behave in additional US
strong-precipitation settings.
5.1 Additional regional forecast examples
Supplementary Figs. 9–14 provide additional 6 h forecast examples. Each case follows the same five-panel
layout as the case figures in the main text. a, Geographic and radar context, with the 256 km × 256 km
forecast domain outlined. b, Lead-time diagnostics comprising CSIN 5 at rain-rate thresholds of 32 and
64 mm h −1, CRPS, CRPSS and radially averaged PSD at lead times of 3 and 6 h. c, Observed and
predicted rain-rate fields from PySTEPS, SimVPv2, NowcastNet and MW-Nowcast at hourly lead times
from 1 to 6 h. d, CSIN5 and POD at thresholds of 32 and 64 mm h−1 for the four MW-Nowcast ensemble
members and their PMM summary. e, The MW-Nowcast deterministic prediction and four ensemble
members at lead times of 2, 4 and 6 h.
52

Supplementary T able 2 Regional CSIN5 comparison of baseline models. Neighbourhood Critical
Success Index with a 5 × 5 neighbourhood is reported at rain-rate thresholds of 16, 32 and 64 mm h −1 for repre-
sentative lead times T+2 h, T+4 h and T+6 h, together with the mean over all 36 lead times from T+10 min to
T+6 h. Values are computed from the same regional evaluation data as the main-text quantitative comparison.
Higher is better; the best value within each region and column is shown in bold.
Region Model T+2 h T+4 h T+6 h Mean
16 32 64 16 32 64 16 32 64 16 32 64
US
NowcastNet 0.192 0.144 0.070 0.075 0.037 0.004 0.038 0.016 0.002 0.171 0.129 0.064
SimVPv2 0.043 0.023 0.006 0.005 0.001 0.000 0.000 0.000 0.000 0.065 0.047 0.025
PySTEPS 0.089 0.043 0.022 0.037 0.017 0.009 0.026 0.014 0.007 0.099 0.064 0.045
MW-Nowcast 0.284 0.214 0.160 0.197 0.129 0.085 0.095 0.055 0.032 0.256 0.194 0.147
EU
NowcastNet 0.171 0.123 0.087 0.081 0.051 0.028 0.036 0.022 0.011 0.158 0.118 0.086
SimVPv2 0.147 0.083 0.070 0.046 0.039 0.043 0.034 0.038 0.045 0.122 0.086 0.075
PySTEPS 0.122 0.072 0.039 0.069 0.037 0.020 0.048 0.026 0.014 0.130 0.085 0.055
MW-Nowcast 0.288 0.213 0.150 0.188 0.132 0.095 0.111 0.080 0.063 0.254 0.192 0.144
CN
NowcastNet 0.184 0.128 0.067 0.074 0.034 0.004 0.034 0.012 0.002 0.166 0.118 0.067
SimVPv2 0.109 0.022 0.002 0.014 0.001 0.000 0.001 0.000 0.000 0.095 0.042 0.020
PySTEPS 0.134 0.067 0.028 0.071 0.034 0.014 0.052 0.027 0.013 0.140 0.086 0.053
MW-Nowcast 0.293 0.197 0.129 0.195 0.123 0.077 0.112 0.063 0.033 0.264 0.184 0.130
53

GA
Start: 2025-10-27 05:30 UTC
Center: 30.50°N, 86.33°W
Patch: 29.23°N-31.78°N | 87.62°W-85.07°W
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.3
0.5
CSIN5@32 ( ↑  better)
0
4
8
12
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.3
0.5
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.25
0.00
0.25
0.50
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Supplementary Fig. 9 Convective heavy-precipitation forecast over the US Gulf Coast.The fore-
cast is initialised at 05:30 UTC on 27 October 2025 for a patch centred near 30.50 ◦N, 86.33 ◦W. The observed
sequence shows convective precipitation developing over the Gulf Coast region and generally expanding eastward
to southeastward across the forecast patch. Rainfall intensity increases during the first half of the 6 h window,
while the strongest precipitation is organised as multiple compact, discrete cores that merge, split and locally
reorganise during the evolution.
54

KS
OK
Start: 2025-07-17 06:00 UTC
Center: 38.17°N, 96.93°W
Patch: 36.91°N-39.46°N | 98.22°W-95.67°W
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.25
0.00
0.25
0.50
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.0
0.2
0.4
0.6
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Supplementary Fig. 10 Convective heavy-precipitation forecast over the central US.The forecast
is initialised at 06:00 UTC on 17 July 2025 for a patch centred near 38.17 ◦N, 96.93 ◦W. The observed sequence
shows organised convective precipitation over the central US, with the rain area first advancing eastward to south-
eastward and then extending mainly towards the southern part of the patch. The high-intensity area broadens
through the forecast window, but its embedded cores become increasingly fragmented, producing a multi-core
structure rather than a single continuous rain band.
55

Start: 2024-07-07 02:15 UTC
Center: 45.95°N, 9.09°E
Patch: 44.67°N-47.23°N | 7.81°E-10.37°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
4
8
12
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.8
−0.4
0.0
0.4
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.2
0.4
0.6
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.2
0.4
0.6
0.8
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Supplementary Fig. 11 Heavy-precipitation forecast over northern Italy .The forecast is initialised at
02:15 UTC on 7 July 2024 and is associated with a precipitation report near 45.95 ◦N, 9.09◦E in northern Italy.
The observed sequence shows Alpine convective precipitation that remains concentrated near the main rain area
rather than translating as a single coherent band. Localised intense echoes are repeatedly renewed and reorganised
during the 6 h window, giving the case a compact but intermittently multi-core structure.
56

Start: 2024-06-03 12:00 UTC
Center: 47.62°N, 11.22°E
Patch: 46.34°N-48.90°N | 9.94°E-12.50°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0.0
2.5
5.0
7.5
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
−0.25
0.00
0.25
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
0.75
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Supplementary Fig. 12 Heavy-precipitation forecast over southern Germany .The forecast is initialised
at 12:00 UTC on 3 June 2024 and is associated with a precipitation report near 47.62 ◦N, 11.22 ◦E in southern
Germany. The observed sequence shows organised heavy precipitation along the Alpine region, with the main
precipitation area remaining relatively coherent through the forecast window. Intense echoes persist within this
broader system, while local cores are renewed and rearranged along the rain area instead of separating into fully
isolated cells.
57

Start: 2026-06-17 18:00 UTC
Center: 21.93°N, 112.05°E
Patch: 20.65°N-23.21°N | 110.77°E-113.33°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
6
12
18
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6 CSIN5@32 (↑ better)
0.0
0.2
0.4
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
0.75
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Supplementary Fig. 13 Heavy-precipitation forecast over southern China.The forecast is initialised at
18:00 UTC on 17 June 2026 for a patch centred near 21.93◦N, 112.05◦E. The observed sequence shows developing
heavy precipitation over southern China, with the rain area expanding mainly towards the eastern to northeastern
part of the patch. The intense precipitation area strengthens through the first half of the forecast window and
then forms a broader, semi-continuous core region with smaller embedded maxima that reorganise locally.
58

Start: 2026-05-25 11:10 UTC
Center: 31.77°N, 117.87°E
Patch: 30.49°N-33.05°N | 116.59°E-119.15°E
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
0.0
0.2
0.4
0.6
CSIN5@32 ( ↑  better)
0
5
10
15
CRPS (↓ better)
−20
0
20
40
60 PSD@T+3h
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CSIN5@64 ( ↑  better)
6 12 18 24 30 36
Lead time (10 min)
0.0
0.2
0.4
0.6
CRPSS (↑ better)
256128 64 32 16 8 4
Wavelength (km)
−20
0
20
40
60 PSD@T+6h
0.0
0.2
0.4
0.6
CSIN5@32 (↑ better)
0.0
0.2
0.4
0.6
CSIN5@64 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
0.75
POD@32 (↑ better)
6 12 18 24 30 36
Lead time (10 min)
0.00
0.25
0.50
0.75
POD@64 (↑ better)
a b
c
T+1h T+2h T+3h T+4h T+5h T+6h
TruthPySTEPSSimVPv2NowcastNetMW-Nowcast
d
e
T+2h T+4h T+6h
DeterministicMember 1Member 2Member 3Member 4
PySTEPS SimVPv2 NowcastNet Deterministic MW-Nowcast Member 1 Member 2 Member 3 Member 4
Supplementary Fig. 14 Heavy-precipitation forecast over eastern China.The forecast is initialised
at 11:10 UTC on 25 May 2026 for a patch centred near 31.77 ◦N, 117.87 ◦E. The observed sequence shows an
organised precipitation system over eastern China that progresses eastward to southeastward across the forecast
patch. The high-intensity precipitation expands and becomes more connected during the first half of the window,
before the strongest region shifts downstream and breaks into several embedded cores at later lead times.
59

5.2 Additional ablation examples
To extend the single ablation example in Supplementary Fig. 1, Supplementary Figs. 15 and 16 show
the same two US cases under the ablation variants. Each grid follows the same visualisation style as
Supplementary Fig. 1: rows give the observation and the ablation variants, and columns give the input
context and forecast lead times through T+6 h.
60

Observation
 T + 1h
 T + 2h
 T + 3h
 T + 4h
 T + 5h
 T + 6h
Latent
OneStage
TwoStage
EDM-ODE
EDM-SDE
MW-Nowcast
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
Supplementary Fig. 15 Ablation forecast grid for the US strong-precipitation case initialised at
05:30 UTC on 27 October 2025.The patch is centred near 30.50◦N, 86.33◦W. Rows show the observation and
the MW-Nowcast, Latent, OneStage, TwoStage, EDM-ODE and EDM-SDE variants; columns show the input
context and forecast lead times through T+6 h.
61

Observation
 T + 1h
 T + 2h
 T + 3h
 T + 4h
 T + 5h
 T + 6h
Latent
OneStage
TwoStage
EDM-ODE
EDM-SDE
MW-Nowcast
1.0
2.0
5.0
10
16
32
64
Rain rate (mm h−1)
Supplementary Fig. 16 Ablation forecast grid for the US strong-precipitation case initialised at
06:00 UTC on 17 July 2025.The patch is centred near 38.17 ◦N, 96.93 ◦W. Layout follows Supplementary
Fig. 15: rows give the observation and the MW-Nowcast, Latent, OneStage, TwoStage, EDM-ODE and EDM-
SDE variants, and columns give the input context and forecast lead times through T+6 h.
62
