---
title: 'Aries: A Proprietary Medium-Range Weather Prediction Model for the Energy Industry'
url: https://arxiv.org/abs/2609.13292
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Lukas Hedegaard Morsing
- Arian Bakhtiarnia
- Jonas Lynge Olesen
- Tómas Bragi Björnsson Leth
- Christian Gøbel Bach
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.13292
pages: 8
chars: 20245
fetched_at: '2026-11-08T13:28:40+00:00'
kb_version: 1
---

# Aries: A Proprietary Medium-Range Weather Prediction Model for the Energy Industry

1
Aries: A Proprietary Medium-Range Weather
Prediction Model for the Energy Industry
Lukas Hedegaard Morsing, Arian Bakhtiarnia, Jonas Lynge Olesen,
T´omas Bragi Bj ¨ornsson Leth, and Christian Gøbel Bach
InCommodities∞
Abstract—Medium-range weather forecasting underpins op-
erational and planning decisions across the energy industry.
Developing competitive weather models was once the domain of
national meteorological centers, but recent advances in machine-
learned weather prediction (MLWP) have opened the field to
industry. We present Aries, a SwinTransformer-based MLWP
model developed at InCommodities. Aries is trained on ERA5
reanalysis data at 0.25° resolution, predicting 74 prognostic and
11 diagnostic atmospheric variables. We evaluate the model on
2025 ECMWF Analysis initializations, ensuring a recent and
strictly out-of-sample test period for all models compared. On
10-metre wind speed, Aries outperforms both ECMWF HRES
and AIFS in terms of RMSE for lead times up to four days,
while on 2-metre temperature it achieves RMSE on par with
AIFS operational. These results demonstrate that proprietary
development of competitive weather models is technically viable,
supporting a broader set of forecasts available for operational
and planning applications in the energy industry.
I. INTRODUCTION
Weather conditions determine renewable generation and
electricity demand. Together with transmission constraints,
they shape regional power balances and cross-border flows,
ultimately driving power prices. Accurate weather forecasts
from hours to weeks ahead are therefore critical infrastructure
for energy markets, translating directly into improved price
forecasts and more efficient market outcomes. Renewables
supplied 32% of global electricity in 2024 [1], with the
European Union reaching 47.5% [2], and as renewable pene-
tration grows the sensitivity of the power system to forecast
accuracy intensifies [3]. Short- and medium-range weather
forecasts govern auction-based trading for next-day delivery
and continuous intraday trading, where forecast errors translate
directly into imbalances between supply and demand.
Numerical weather prediction (NWP) has served this role
for decades, but the past three years have seen machine-
learned weather prediction (MLWP) models emerge as a
credible alternative. Several systems now match or surpass
the deterministic skill of leading NWP models at a fraction
of the computational cost and latency [4]–[6], and publicly
available training data (ERA5 [7]) combined with commodity-
GPU inference has lowered the barrier to entry well beyond
national meteorological agencies.
Industry players have begun to follow suit, developing
in-house MLWP systems alongside the established public-
sector providers. At InCommodities we developed Aries as an
∞https://incommodities.com
2 4 60
1
2
3
aries_v0.1.1_ec_opr aifs_opr ec_opr
EUROPE
10si
Lead Time (days)
RMSE
Fig. 1. Latitude-weighted RMSE of 10 m wind speed forecasts over Europe
for operational 2025 runs with—Aries,—AIFS, and—HRES against
ERA5. Shaded regions denote 25th–75th percentile ranges.
independently trained alternative. We present evaluations on
two central weather variables: 2 m temperature, which strongly
informs energy demand, and 10 m wind speed, which drives
wind turbine power generation. We demonstrate deterministic
skill that surpasses ECMWF HRES and AIFS on 10 m wind
speed at lead times up to four days and matches AIFS on 2 m
temperature.
II. BACKGROUND: FROMNWPS TOMLWPS
NWP produces forecasts by solving discretized partial dif-
ferential equations (PDEs) of atmospheric dynamics on a
global grid. ECMWF’s Integrated Forecasting System (IFS),
and in particular its high-resolution deterministic configuration
(HRES), has long been the gold standard for medium-range
forecasting, but each cycle requires hours of computation on
dedicated supercomputers.
Since 2022, data-driven models trained on ERA5 reanalysis
[7] have rapidly closed this gap. FourCastNet [8], Pangu-
Weather [9], GraphCast [4], FuXi [10], Aurora [5], and
ECMWF’s own AIFS [6] now match or exceed HRES on most
evaluation targets, while Jua.ai’s EPT-2 [11] demonstrates that
startup players can produce competitive MLWPs. Because
inference requires only a single forward pass, a 10-day global
forecast takes seconds on a commodity GPU, dramatically
lowering the barrier to entry.
A shared limitation of deterministic MLWPs trained with
MSE or MAE losses is spectral blurring at longer lead times:
arXiv:2609.13292v1  [physics.ao-ph]  9 Sep 2026

2
The loss penalizes sharp but misplaced features, incentivizing
smooth predictions [4], [12]. Multi-step autoregressive fine-
tuning improves RMSE but can exacerbate this effect [6],
[12]. Frequency-domain losses offer a partial remedy [13],
[14], while CRPS-based and generative approaches such as
GenCast [15] and AIFS-CRPS [16] mitigate the problem by
incentivizing realistic ensemble spread rather than a smoothed
mean.
III. MODELARCHITECTURE ANDOPERATIONALSETTING
A. Architecture Overview
Aries is built on the Shifted Window Transformer archi-
tecture derived from SwinV2 [17]. The backbone isnon-
hierarchical: All layers operate at the same spatial feature
resolution, avoiding the down-sampling stages typical of vision
transformers. The input atmospheric state is split into patches
that serve as tokens; shifted-window self-attention is then
applied with periodic zonal wrap-around padding to respect
the spherical topology of the globe. Table I summarizes the
model configuration.
TABLE I
ARIES MODEL CONFIGURATION.
Parameter Value
Depth 14 layers
Attention heads 16
Embedding dimension 3,584
Total parameters 2.4 B
B. Formulation
Aries ingests asingleatmospheric state and predicts the
next state in one forward pass. The model predicts a residual
update that is added to the input state:
˜X t+∆t =f θ(X t) +r(X t)(1)
wheref θ denotes the learned update mapping,ris a residual
transformation, andX t is the atmospheric state at timet,
and∆t= 6h. We employ a modified residual connectionr
inspired by low-pass filtering approaches in the literature [14],
[18].
C. Training
The model is trained on ERA5 reanalysis data [7] at 0.25°
resolution (720×1440grid points). The training period spans
1979–2022, with 2023 reserved for validation and 2024 for
testing. Training proceeds in two distinct phases: (i)single-
step training, in which the model learns to predict one 6 h
step ahead, and (ii)multi-step autoregressive fine-tuning, in
which the model is unrolled over successively more steps and
optimized end-to-end. We trained Aries up to 10 roll-out steps
(60 h lead time).
Training uses a latitude-weighted MSE loss for the single-
step phase, switching to a latitude-weighted L1 loss during
autoregressive fine-tuning. In both phases, we use channel-
wise weights that follow the scheme of Lam et al. [4], with
increased weight on wind components given their direct rele-
vance to energy applications. An auxiliary frequency-domain
penalty term is applied at low weight to mitigate spectral
degradation at longer lead times [14]. This term operates on
the power spectral density of each channel:
Lfreq = 1 C
CX
c=1
X
kx, ky ≥k min

 Sc( ˜X) kx,ky −S c(X) kx,ky Zc

 ,(2)
whereS c(X) =|F c(X)| 2 is the 2D power spectral density
of channelc,Fdenotes the discrete Fourier transform over
latitude and longitude,Z c =

meankx,ky Sc(X) kx,ky

 normal-
izes per channel, and wavenumbers belowk min are excluded
to focus penalization on fine-scale structure.
IV. BENCHMARKSETUP
All models are evaluated over the full calendar year 2025,
initialized from ECMWF operational analysis at the 00Z and
12Z cycles. Forecasts are verified against ERA5 reanalysis
[7]. The year 2025 predictions stem from operational runs
for all models. We compare Aries against ECMWF HRES
(the operational NWP gold standard) and AIFS [6]. Note
that unlike HRES and AIFS, Aries was never fine-tuned with
ECMWF operational analysis inputs.
Metrics are computed over Europe and the USA 1, latitude-
weighted over all grid points. We evaluate 10 m wind speed
(10si) and 2 m temperature (2t).
Lete i(t) = ˜Xi(t)−X i(t)denote the forecast error at grid
pointiand initialization timet, with latitude-weighted spatial
mean
¯e(t) =
P
i wi ei(t)P
i wi
, w i = cos(lati),(3)
which also corresponds to theBias. The latitude-weighted root
mean square error (RMSE) is defined as
RMSE=
s P
i wi e2 iP
i wi
.(4)
V. DETERMINISTICFORECASTINGRESULTS
A. 10m Wind Speed
Figures 1 and 2 show the latitude-weighted RMSE of 10 m
wind speed forecasts out to 168 h (7 days). Note that the ”zig-
zag” patterns are an artifact of daily error-patterns, where the
two daily periods reflect the temporal shift between the 00
and 12 model runs. Aries achieves lower RMSE than both
HRES and AIFS up to approximately 96 h (4 days) in both
Europe and the USA. This horizon aligns with the time frame
over which forecasts of weather-driven supply and demand
are most relevant for short-term market clearing and system
operation. In liberalized power systems, market outcomes drive
generation schedules and interconnector flows. Consequently,
improved forecast accuracy in this range has the potential to
enhance dispatch efficiency and system balancing. The four-
day crossover reflects the autoregressive training depth of 10
steps (60 h); competitive performance extends to roughly 96 h
1Europe latitude [32.2, 72.0], longitude [-15.6, 36.4]. USA latitude [23.8,
52.2], longitude [-125.6, 58.4].

3
2 4 60
0.5
1
1.5
2
2.5
aries_v0.1.1_ec_opr aifs_opr ec_opr
USA
10si
Lead Time (days)
RMSE
2 4 6
−0.6
−0.4
−0.2
0
0.2
aries_v0.1.1_ec_opr aifs_opr ec_opr
USA
10si
Lead Time (days)
Bias
2 4 60
0.5
1
1.5
2
2.5
aries_v0.1.1_ec_opr aifs_opr ec_opr
EUROPE
2t
Lead Time (days)
RMSE
2 4 6
−0.6
−0.4
−0.2
0
0.2
aries_v0.1.1_ec_opr aifs_opr ec_opr
EUROPE
2t
Lead Time (days)
Bias
2 4 60
1
2
3
aries_v0.1.1_ec_opr aifs_opr ec_opr
USA
2t
Lead Time (days)
RMSE
2 4 6
−0.6
−0.4
−0.2
0
0.2
0.4
aries_v0.1.1_ec_opr aifs_opr ec_opr
USA
2t
Lead Time (days)
Bias
Fig. 2. Latitude-weighted RMSE (top) and bias (bottom). Left: 10 m wind speed, USA. Middle: 2 m temperature, Europe. Right: 2 m temperature, USA.
Shaded regions denote 25th–75th percentile ranges.—Aries,—ECMWF AIFS,—ECMWF HRES.
before error growth accelerates relative to AIFS. Bias profiles
(Fig. 2, right) show excellent calibration for HRES; initially
small but increasing negative bias for Aries; and significant
negative bias for AIFS. Qualitative global maps and a storm
case study (Storm ´Eowyn, initialized 2025-01-21) are shown
in the Supplementary Material (Figs. 4, 6, and 8).
B. 2m Temperature
Figure 2 presents the latitude-weighted RMSE for 2 m
temperature. Aries achieves RMSE on par with AIFS during
the first 96 h, with both ML systems generally outperforming
HRES against ERA5. As shown in the bias plots on the right-
hand side of Fig. 2, the RMSE discrepancy can be largely
attributed to a constant negative HRES bias, due to its cali-
bration to ECMWF Analysis rather than ERA5. Corresponding
qualitative snapshots for 2 m temperature are provided in the
Supplementary Material (Figs. 3, 5, and 7).
VI. LIMITATIONS ANDFUTUREWORK
Several directions remain for future work. Verification is
performed against ERA5 reanalysis only and over a single cal-
endar year (2025) of operational runs; station-level verification
would strengthen confidence in the reported skill. The four-day
crossover on 10-metre wind speed reflects an autoregressive
training depth of ten roll-out steps (60 h); extending this
training horizon would push skill further into the medium
range. Aries also predicts variables of direct relevance to
energy applications such as surface solar radiation downwards
(SSRD) and total precipitation (TP), which warrant similar
evaluation.
VII. OUTLOOK
As renewable capacity expands and extreme weather be-
comes more frequent, the value of accurate, independent
forecasting compounds. Ultimately, this benefits a broad range
of entities that play an active role in modern energy systems.
More accurate short-term forecasts of wind, solar, and temper-
ature can improve generation scheduling and reduce balancing
volumes and associated system costs. Energy trading aids this
scheduling by clearing the market at a price that balances
supply and demand.
We introduced Aries, a SwinTransformer-based machine-
learned weather prediction model developed in industry set-
tings. Aries outperforms both ECMWF HRES and AIFS on
10-metre wind speed in terms of RMSE for lead times up to
four days. On 2-metre temperature, Aries achieves RMSE on
par with AIFS.
We believe that diverse, independently developed weather
models improve social welfare for energy suppliers and con-
sumers alike. Aries represents a step toward that goal, and we
view the broader growth of the MLWP ecosystem as a positive
development for the energy industry.
REFERENCES
[1] International Energy Agency, “Global energy review 2025,” https://
www.iea.org/reports/global-energy-review-2025, 2025.
[2] Eurostat, “Electricity from renewable sources reaches 47% in
2024,” https://ec.europa.eu/eurostat/web/products-eurostat-news/w/
ddn-20250319-1, 2025.
[3] I. Staffell and S. Pfenninger, “The increasing impact of weather on
electricity supply and demand,”Energy, vol. 145, pp. 65–78, 2018.
[4] R. Lam, A. Sanchez-Gonzalez, M. Willson, P. Wirnsberger, M. Fortu-
nato, F. Alet, S. Ravuri, T. Ewalds, Z. Eaton-Rosen, W. Hu, A. Merose,
S. Hoyer, G. Holland, O. Vinyals, J. Stott, A. Pritzel, S. Mohamed, and
P. Battaglia, “GraphCast: Learning skillful medium-range global weather
forecasting,”Science, vol. 382, no. 6677, pp. 1416–1421, 2023.
[5] C. Bodnar, W. P. Bruinsma, A. Lucic, M. Stanley, J. Brandstetter,
P. Garvan, M. Riechert, J. Weyn, H. Dong, A. Vaughan, J. K. Gupta,
K. Tambiratnam, A. Archibald, E. Heider, M. Welling, R. E. Turner, and
P. Perdikaris, “Aurora: A foundation model of the atmosphere,”Nature,
vol. 641, pp. 1180–1187, 2025.
[6] G. Moldovan, E. Pinnington, A. P. Nemesio, S. Lang, Z. B. Bouallegue,
J. Dramsch, M. Alexe, M. S. Cruz, S. Hahner, H. Cook, H. Theissen,
M. Clare, C. O’Brien, J. Polster, L. Magnusson, G. Mertes, F. Pinault,
B. Raoult, P. de Rosnay, R. Forbes, and M. Chantry, “An update
to ECMWF’s machine-learned weather forecast model AIFS,”arXiv
preprint, 2025, arXiv:2509.18994.

4
[7] H. Hersbach, B. Bell, P. Berrisford, S. Hirahara, A. Hor ´anyi, J. Mu ˜noz-
Sabater, J. Nicolas, C. Peubey, R. Radu, D. Schepers, A. Simmons,
C. Soci, S. Abdalla, X. Abellan, G. Balsamo, P. Bechtold, G. Biavati,
J. Bidlot, M. Bonavita, G. D. Chiara, P. Dahlgren, D. Dee, M. Dia-
mantakis, R. Dragani, J. Flemming, R. Forbes, M. Fuentes, A. Geer,
L. Haimberger, S. Healy, R. J. Hogan, E. H´olm, M. Janiskov´a, S. Keeley,
P. Laloyaux, P. Lopez, C. Lupu, G. Radnoti, P. de Rosnay, I. Rozum,
F. Vamborg, S. Villaume, and J.-N. Th ´epaut, “The ERA5 global reanal-
ysis,”Quarterly Journal of the Royal Meteorological Society, vol. 146,
no. 730, pp. 1999–2049, 2020.
[8] J. Pathak, S. Subramanian, P. Harrington, S. Raja, A. Chattopadhyay,
M. Mardani, T. Kurth, D. Hall, Z. Li, K. Azizzadenesheli, P. Hassan-
zadeh, K. Kashinath, and A. Anandkumar, “FourCastNet: A global data-
driven high-resolution weather forecasting model,”arXiv preprint, 2022,
arXiv:2202.11214.
[9] K. Bi, L. Xie, H. Zhang, X. Chen, X. Gu, and Q. Tian, “Accurate
medium-range global weather forecasting with 3D neural networks,”
Nature, vol. 619, pp. 533–538, 2023.
[10] L. Chen, X. Zhong, F. Zhang, Y . Cheng, Y . Xu, Y . Qi, and H. Li,
“FuXi: A cascade machine learning forecasting system for 15-day global
weather forecast,”npj Climate and Atmospheric Science, vol. 6, no. 1,
p. 190, 2023.
[11] R. Molinaro, N. Siegenheim, N. Poulsen, J. D. Daubinet, H. Martin,
M. Frey, K. Thiart, A. J. Dautel, A. Schlueter, A. Grigoryev, B. Danciu,
N. Ekhtiari, B. Steunebrink, L. Wagner, and M. V . Gabler, “EPT-2
technical report,”arXiv preprint, 2025, arXiv:2507.09703.
[12] J. D. Willard, P. Harrington, S. Subramanian, A. Mahesh, T. A. O’Brien,
and W. D. Collins, “Analyzing and exploring training recipes for
large-scale transformer-based weather prediction,”arXiv preprint, 2024,
arXiv:2404.19630.
[13] C. Subich, S. Husain, L. Separovic, and J. Yang, “Fixing the double
penalty in data-driven weather forecasting through a modified spherical
harmonic loss function,”arXiv preprint, 2025, arXiv:2501.19374.
[14] A. Chattopadhyay, Y . Q. Sun, and P. Hassanzadeh, “Challenges of
learning multi-scale dynamics with AI weather models: Implications for
stability and one solution,”arXiv preprint, 2024, arXiv:2304.07029.
[15] I. Price, A. Sanchez-Gonzalez, F. Alet, T. R. Andersson, A. El-Kadi,
D. Masters, T. Ewalds, J. Stott, S. Mohamed, P. Battaglia, R. Lam, and
M. Willson, “Probabilistic weather forecasting with machine learning,”
Nature, 2024.
[16] S. Lang, M. Alexe, M. C. A. Clare, C. Roberts, R. Adewoyin, Z. B.
Bouall`egue, M. Chantry, J. Dramsch, P. D. Dueben, S. Hahner, P. Ma-
ciel, A. Prieto-Nemesio, C. O’Brien, F. Pinault, J. Polster, B. Raoult,
S. Tietsche, and M. Leutbecher, “AIFS-CRPS: Ensemble forecasting
using a model trained with a loss function based on the continuous
ranked probability score,”arXiv preprint, 2024, arXiv:2412.15832.
[17] Z. Liu, H. Hu, Y . Lin, Z. Yao, Z. Xie, Y . Wei, J. Ning, Y . Cao, Z. Zhang,
L. Dong, F. Wei, and B. Guo, “Swin Transformer V2: Scaling up
capacity and resolution,” inProceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, 2022, pp. 12 009–12 019.
[18] D. Kochkov, J. Yuval, I. Langmore, P. Norgaard, J. Smith, G. Mooers,
M. Kloewer, J. Lottes, S. Rasp, P. Dueben, S. Hatfield, P. Battaglia,
A. Sanchez-Gonzalez, M. Willson, M. P. Brenner, and S. Hoyer, “Neural
general circulation models for weather and climate,”Nature, 2024.

5
VIII. SUPPLEMENTARYMATERIAL
This section presents qualitative forecast snapshots that complement the aggregate skill metrics of the main text. All examples
use the forecast initialized on 2025-01-21 at 00 UTC, which spans the passage of Storm ´Eowyn, a record-breaking windstorm
that struck Ireland, the United Kingdom, and the North Sea around 24 January 2025.
Aries  +24 h
 Aries  +72 h
Aries  +96 h
 Aries  +120 h
−30
−20
−10
0
10
20
2 m temperature (°C)
Fig. 3. Global Aries 2 m temperature forecasts at 24, 72, 96, and 120 h lead time.
Aries  +24 h
 Aries  +72 h
Aries  +96 h
 Aries  +120 h
0
2
4
6
8
10
12
14
10 m wind speed (m s−1)
Fig. 4. Global Aries 10 m wind speed forecasts at 24, 72, 96, and 120 h lead time.

6
24 h
Aries
 AIFS
 HRES
 ERA5
72 h
96 h
120 h
−15
−10
−5
0
5
10
15
2 m temperature (°C)
Fig. 5. 2 m temperature forecasts over Europe at 24, 72, 96, and 120 h lead time (rows) for Aries, AIFS, HRES, and ERA5 (columns). ERA5 is the ground-truth
reanalysis.

7
24 h
Aries
 AIFS
 HRES
 ERA5
72 h
96 h
120 h
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
10 m wind speed (m s−1)
Fig. 6. 10 m wind speed forecasts over Europe at 24, 72, 96, and 120 h lead time (rows) for Aries, AIFS, HRES, and ERA5 (columns). The 72 and 96 h
panels capture Storm ´Eowyn over the British Isles and the North Sea. ERA5 is the ground-truth reanalysis.

8
0 1 2 3 4 5 6 7
Lead Time (days)
2
3
4
5
6
7
8Air T emperature (°C)
Fig. 7. Time series of 2 m temperature forecasts at the Horns Rev offshore wind farm, Denmark (55.5 ◦N,7.8 ◦E) over the 0–168 h horizon. Point values
are bilinearly interpolated from each model’s native grid to the site; Aries and AIFS are output at 6-hourly steps, HRES and ERA5 at hourly steps, and the
curves are interpolated between steps with an Akima spline.—Aries,—AIFS,—HRES,- -ERA5 (ground truth).
0 1 2 3 4 5 6 7
Lead Time (days)
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
Wind Speed (m s−1)
Fig. 8. Time series of 10 m wind speed forecasts at the Horns Rev offshore wind farm, Denmark (55.5 ◦N,7.8 ◦E) over the 0–168 h horizon. The wind
maximum around day 3.5 corresponds to the passage of Storm ´Eowyn. Point values are bilinearly interpolated from each model’s native grid to the site;
Aries and AIFS are output at 6-hourly steps, HRES and ERA5 at hourly steps, and the curves are interpolated between steps with an Akima spline.—Aries,
—AIFS,—HRES,- -ERA5 (ground truth).
