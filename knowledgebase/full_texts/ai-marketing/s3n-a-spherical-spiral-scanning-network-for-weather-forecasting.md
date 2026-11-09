---
title: 'S³N: A Spherical Spiral Scanning Network for Weather Forecasting'
url: https://arxiv.org/abs/2610.04338
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Fan Yan
- Chen Hui
- Weisi Lin
- Haiqi Zhu
- Feng Jiang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.04338
pages: 5
chars: 24688
fetched_at: '2026-11-08T13:25:28+00:00'
kb_version: 1
---

# S³N: A Spherical Spiral Scanning Network for Weather Forecasting

S3N: A SPHERICAL SPIRAL SCANNING NETWORK FOR WEA THER FORECASTING
Fan Yan1 Chen Hui1,∗ Weisi Lin2 Haiqi Zhu3
Feng Jiang1 Sun-Yuan Kung4 Wei Zhang5
1Nanjing University of Information Science and Technology 2Nanyang Technological University
3Harbin Institute of Technology 4Princeton University 5Karolinska Institutet
ABSTRACT
Machine learning–based weather prediction (MLWP) has
achieved strong performance in global weather forecast-
ing. Recent Hierarchical Equal Area isoLatitude Pixelation
(HEALPix)-based methods use the HEALPix (HP) grid
to avoid area distortion near the poles of conventional lat-
itude–longitude (LL) grids. However, existing HP-based
approaches often use pointwise mapping methods and process
HP pixels within separate base faces or local windows. Con-
sequently, the mapping may introduce reconstruction errors
and cross-face communication depends on handcrafted bound-
ary handling or shifted windows. We propose the Spherical
Spiral Scanning Network (S 3N) to address both limitations.
First, L2Proj provides a bidirectional method for mapping
atmospheric fields between the LL and HP grids through an
L2 projection of their continuous finite-element representa-
tions. Second, the Attention-Guided Quad-Spiral State-Space
Scanning (AQSS) block uses cross-latitude attention to guide
selective state-space updates along four global pole-to-pole
spiral paths. This design enables continuous information prop-
agation across HP base-face boundaries without additional
boundary-processing mechanisms. Experiments show that
S3N achieves better results at 4-, 7-, and 10-day lead times,
and exhibits slower error growth in long-range forecasting.
Index Terms—Weather Forecasting, Deep Learning,
HEALPix, Mamba, Attention
1. INTRODUCTION
Machine-learning weather prediction (MLWP) has made great
progress in recent years, represented by Pangu-Weather, Four-
CastNet, GraphCast, NeuralGCM, and Aurora [1 –5]. Most
MLWP methods still use the regular latitude–longitude (LL)
grid [6–12]. But the physical area represented by each LL
grid cell decreases as latitude increases toward the poles, and
most methods use latitude-weighted objectives to compensate
for the unequal sampling during optimization. However, this
only adjusts the training weights and does not change the LL-
grid representation, which remains physically nonuniform and
oversamples the polar regions.
∗Corresponding author:chui@nuist.edu.cn.
No padding design.
Continuous ordering
across all pixels.
Bilinear
Avg  MSE：0.002
L2Proj（Ours）
Avg  MSE：0.0003
Mapping error
Latitude-Longitude(LL)  gird
HEALPix(HP) gird
(a)
Require handcrafted
shifting/padding design.
Stack together0 1 2 3
4 5 6 7
8 9 10 11
(b)
Treat as sequence
Flattened HEALPix sphere Spiral scan
Patches
Visualization of
2 meter temperature
L2Proj
Bilinear
Fig. 1. Comparison of various methods. (a) The average error
of L2Proj is much lower than that of bilinear interpolation.
(b) We treat HEALPix pixels from the twelve base faces as a
sequence rather than stacking the twelve base faces as patches,
thereby avoiding handcrafted boundary handling.
HEALPix provides an alternative equal-area representation
of the sphere [13], which has been adopted by deep learning
methods such as DeepSphere, HEALPix CNNs, OSLO, SCE-
Depth, and HEALPix-guided diffusion models [14–18], and
weather forecasting models including DLWP-HPX, HEAL-
ViT, ESyM [19 –21]. However, existing HEALPix-based
weather forecasting methods still face two practical limita-
tions. First, their LL–HP mapping usually relies on pointwise
or learned resampling, while the two grids differ in sampling
density and spatial resolution [19, 20, 22]. Second, most
methods organize the HP grid into separate patches, which
limits the propagation of information across adjacent faces
and requires additional mechanisms such as rotated or copied
padding, shifted windows, masks, or layout-specific indexing
for cross-boundary communication [19, 20, 23].
To address these two limitations, we develop a unified
framework that combines LL–HP data mapping with a global
cross-face information propagation mechanism.
First, we introduce L2Proj, a bidirectional mapping method
based on surface finite-element principles [24, 25]. L2Proj
represents the LL and HP data as continuous piecewise-linear
fields on the unit sphere and maps between them through an
arXiv:2610.04338v1  [cs.LG]  3 Oct 2026

L2 projection. This provides a unified mapping method for the
two nonmatching spherical grids.
Second, we introduce the Attention-Guided Quad-Spiral
State-Space Scanning (AQSS) block, inspired by selective
state-space models and multidirectional visual scanning [26,
27]. As shown in Fig. 1(b), AQSS arranges all HP pixels along
four global pole-to-pole spiral paths. Cross-latitude attention
guides the state-space updates and the fusion of the four scan
outputs. This design enables the propagation of information
across HP base-face boundaries without handcrafted padding,
shifted windows, or layout-specific boundary operations.
Our main contributions are as follows:
• We present S3N, a spherical weather forecasting frame-
work that combines finite-element-based LL–HP map-
ping with an attention-guided cross-face state-space
scanning mechanism. S3N achieves a mean normalized
RMSE (nRMSE) of 0.5177 at a 240-hour lead time, com-
pared with 0.6398 for OneForecast [28], demonstrating
slower error growth during long-range forecasting.
• We introduce L2Proj, a bidirectional mapping method
based on surface finite-element principles. It represents
LL and HP data as continuous piecewise-linear fields on
the unit sphere and maps between them through an L2
projection. L2Proj achieves lower errors than bilinear
interpolation when mapping atmospheric fields from the
LL grid to the HP grid and then back to the LL grid.
• We propose the Attention-Guided Quad-Spiral State-
Space Scanning (AQSS) block, which uses cross-
latitude attention to guide selective state-space updates
along four global pole-to-pole spiral paths. This design
allows hidden states to propagate directly across HP
base-face boundaries without face-wise padding or
shifted-window processing.
2. METHOD
2.1. Overview
Our framework, shown in Fig. 2(a), consists of two compo-
nents: the L2Proj mapping module and the AQSS forecasting
backbone. We use L2Proj to map atmospheric fields between
the LL grid and the HP grid. The AQSS block receives the
input field and performs multiscale spherical feature modeling
through four global spiral scans and attention-guided state-
space processing. Cross-latitude attention provides spatial
context, which is used to guide the Mamba updates and the
weighted fusion of the four path features.
2.2. SphericalL 2 Finite-Element Projection
Given an atmospheric field defined on an LL grid with spatial
resolution HL ×W L, we use a HEALPix grid with 12n2 side
pixels for its spherical representation. On the LL grid, all
longitude points in each polar row correspond to the same
physical location at the pole; therefore, each polar row is
merged into a single finite-element node. After processing, the
LL grid contains NL nodes while the HEALPix grid contains
NH nodes. The two grids are then mapped onto the unit sphere
and triangulated independently.
For any point ω on the sphere, we find the triangle con-
taining it on each mesh and then compute the weights of the
vertices of this triangle using first-order linear interpolation.
This allows the discrete values defined at the grid nodes to be
extended to a continuous field over the entire sphere. For an
atmospheric variable, let xi denote its value at LL node i and
za denote its value at HP node a. The continuous fields of the
LL and the HP grids are defined as:
fL(ω;x) =
NLX
i=1
xiϕi(ω), f H (ω;z) =
NHX
a=1
zaψa(ω),(1)
where ϕi and ψa are the P1 basis functions associated with LL
nodeiand HP nodea, respectively.
We determine the HP representation z by minimizing the
global difference between the two continuous fields over the
entire unit sphere:
J(z) = 1 2 Z S2 [fH (ω;z)−f L(ω;x)] 2 dΩ,(2)
where S2 denotes the unit sphere and dΩ denotes its surface-
area element. Because the continuous HP field fH is linear
with respect to z, this can be written as the quadratic form:
J(z) = 1 2 zTMH z−z TBx+c(x),(3)
where c(x) is independent of z. The two matrices that deter-
mine the optimal HP representation are:
(MH )ab =
Z
S2
ψa(ω)ψb(ω) dΩ, Bai =
Z
S2
ψa(ω)ϕi(ω) dΩ, (4)
the HP mass matrix MH encodes the overlap of the HP P1
basis functions over the sphere. The cross-grid coupling matrix
B measures the overlap between the LL and HP P1 basis
functions over the sphere. Setting the derivative of Eq. (3)
with respect tozto zero gives:
MH z=Bx,(5)
MH and B depend only on the positions of the spherical nodes
and the resolutions of the two grids. Therefore, they can be
precomputed offline and reused during training and inference,
without mesh-intersection processing or numerical integration
at runtime. Similarly, the HP-to-LL mapping is constructed
independently in the same way.
2.3. Attention-Guided Quad-Spiral Scanning Block
After L2Proj mapping, the atmospheric state is represented
on the HP grid. For one stage, let X∈R C×N denote the
input feature, where C is the number of feature channels and
N= 12n 2 side is the number of HP pixels. An AQSS block
first computes local spherical context and then propagates this
information globally through four complete spiral scans.
For each HP pixelxi, we sample eight cross-latitude neigh-
bors exik, with four located northward and four southward

(c) Attention-guided Quad-spiral State-space Scanning Block
𝑁𝐻 × 𝐶
𝐲𝐭 = ෨𝐂𝐡𝐭 + 𝐃෦𝐮𝑡
𝐡𝐭 = 𝑒 ෩Δ𝐀𝐡𝐭−𝟏 + ෩Δ𝐁𝐮𝐭
𝑁𝐻 × 𝐶
Weighted Merge
projection
Δ
𝐵
𝐶
+
෩Δ
෨𝐵
ሚ𝐶
(b)L2Proj
𝑁𝐿 × 𝐶 𝐻 × 𝑊 × 𝐶
𝑋𝑡 ෠𝑋𝑡+6ℎ
Δ ෠𝑋𝑡+6ℎ
+
L2Proj
𝑁𝐻
16 × 𝐶3
 𝑁𝐻
4 × 𝐶2
Projection
𝑁𝐻 × 𝐶
AQSS Block
x2
Down sampling
AQSS Block
x2
Down sampling
𝑁𝐻
4 × 𝐶2
AQSS Block
x2
AQSS Block
x2
Up sampling
Skip Connection
𝑁𝐻 × 𝐶1
 𝑁𝐻 × 𝐶1
 𝑁𝐻 × 𝐶1
L2Proj
Projection
(a) Model architecture
projection
Four direction scan
Attention
Block
AQSS4D
minimize: 𝐽 𝐳 = 1 2 න 𝑆𝟚 𝑓𝐻 𝝎, 𝐳 − 𝑓𝐿 𝝎, 𝐱 2d Ω
𝑓𝐻 𝜔, 𝑧
𝑓𝐿 𝜔, 𝑥
Unit sphere
Known HP
representation
Unknown LL
representation
？
𝑁𝐿 × 𝐶 𝑁𝐻 × 𝐶
Unknown HP
representation
Known LL
representation
？
𝑁𝐿 × 𝐶 𝑁𝐻 × 𝐶
Encode LL to HP
Decode HP to LL
LN
Gather cross-latitude
information
LN
FFN+
𝐮𝐭
Order by index……………………
linear
DW Conv
SiLU
LN
linear +
+
AQSS4D block
Selective Scan
Up sampling
AQSS Block
x2 𝑁𝐿 × 𝐶 𝐻 × 𝑊 × 𝐶
𝑥𝑖 (ℎ) = ෍
𝑘=1
8
𝑎𝑖,𝑘𝑉𝑖,𝑘
Δ𝑥
𝐵𝑥
𝐶𝑥
Update scanning
paramaters
𝑥𝑖 attn
𝑓𝐻 𝜔, 𝑧
𝑓𝐿 𝜔, 𝑥
Unit sphere
𝛼1
𝛼2
𝛼3
𝛼4
Fig. 2. Overview of our S3N framework. (a) The overall pipeline of our model, which follows an encoder-processor-decoder
architecture. (b) Illustration of the L2Proj computation. We use L2Proj as the encoder and decoder for projecting atmospheric
fields between the LL and the HP grids. (c) Details of the proposed AQSS block. Cross-latitude information is collected from
eight cross-latitude neighbors to guide the Mamba updates and the weighted fusion of the four path features.
at offsets of one to four HP pixel intervals, as illustrated in
Fig. 2(c). The sampling follows the corresponding great circle
and remains continuous across a geographic pole. The center
feature is then used as the query, while the eight neighbor
features are used as keys and values for multi-head attention.
For each attention headh, the computation is:
a(h) ik = softmaxk

q(h)T i k(h) ik√
d
+b (h) ik
!
,x (h) i =
8X
k=1
a(h) ik v(h) ik , (6)
where q(h) i =W (h) Q xi is the query of pixeli, k(h) ik =W (h) K exik
and v(h) ik =W (h) V exik are the key and value of its k-th cross-
latitude neighbor, while b(h) ik is a learned bias that describes the
relative direction and distance between the center pixel and its
neighbor on the sphere. The coefficient a(h) ik is the normalized
attention weight of neighbork.
The outputs of all H attention heads are concatenated and
projected to obtain the final context feature:
xattn i =W O Concat  x(1) i , . . . ,x(H) i  ,(7)
where xattn i is the fused attention context of pixel i from all H
heads, and WO projects the concatenated multi-head features
back to the original channel dimension. The context feature is
computed before spiral scanning and is used to guide the se-
lective state-space model. The context feature first modulates
the scan input through a residual connection:
ui =x i +λ xFx(xattn i ),(8)
where Fx is a learned projection and λx controls the strength
of the context contribution. The cross-latitude context also
adjusts the dynamic Mamba parameters:
e∆(p) = ∆(p) +λ ∆ tanh  F∆(xattn i )  ,
eB(p) =B (p) +λ B tanh  FB(xattn i )  ,
eC(p) =C (p) +λ C tanh  FC(xattn i )  ,(9)
where e∆(p), eB(p), and eC(p) control state retention, input writ-
ing, and state readout, respectively.
To propagate information globally, we construct four direc-
tional spiral paths: PN2S+ , PN2S− , PS2N+ , and PS2N− . The
four scan paths are constructed using the HEALPix RING or-
dering. Specifically, PN2S+ and PN2S− scan from the North
Pole to the South Pole in clockwise and counterclockwise di-
rections, respectively, while PS2N+ and PS2N− scan from the
South Pole to the North Pole in clockwise and counterclock-
wise directions, respectively. Each path visits every HP pixel
exactly once, forming a continuous pole-to-pole spiral. The
selective scan process is represented as:
h(p) t =e e∆(p) t A ⊙h (p) t−1 + e∆(p) t eB(p) t u(p) t ,
y(p) t = eC(p) t h(p) t +D⊙u (p) t ,(10)
where p indexes the different scan paths, and t indexes the
position along the path; h(p) t is the corresponding hidden state;
e e∆(p) t A indicates how much of the previous state is retained
along the scan path, whileD indicates how much of the current
input is passed directly to the output without going through
the state. After scanning, each path output is restored to the
original HP pixel order and merged using weights generated
fromx attn i , as illustrated in Fig. 2(c).

3. EXPERIMENTS
3.1. Dataset and Implementation Details
We use ERA5 reanalysis data [29] from WeatherBench 2 [30],
produced by the European Centre for Medium-Range Weather
Forecasts (ECMWF) [31]. The dataset has a spatial resolution
of 1.5◦ (121×240 grid points), a temporal resolution of 6
hours, and 69 atmospheric fields. We use 1979–2017 for
training, 2018–2019 for validation, and 2020 for testing. The
HP representation uses nside = 64 and contains 49,152 equal-
area pixels. S 3N is trained for one-step prediction followed
by long-range autoregressive fine-tuning. Training takes less
than 12 days on one NVIDIA RTX 6000D GPU with 84 GB
memory. All comparative experiments are conducted under
the same conditions.
3.2. Bidirectional Mapping Evaluation
Table 1. Mean squared error (MSE) of atmospheric fields after
mapping from the LL grid to the HP grid and then back to the
LL grid. Lower is better.
Method Bilinear Interpolation L2Proj
Average MSE 0.0021530.000252
We evaluate the mapping performance of L2Proj and bi-
linear interpolation using data from 2017 and 2020. For
both methods, the 69 standardized atmospheric fields are first
mapped from the LL grid to the HP grid and then remapped
back to the LL grid, where the reconstructed fields are com-
pared with the original LL fields. Table 1 presents the average
MSE over all variables after bidirectional mapping. L2Proj
achieves a lower reconstruction error.
3.3. Main Results
Table 2. Comparison of mean normalized RMSE (lower is
better) across different lead times. The best result in each
column is in bold, and the second best is underlined.
Method 6-hour 1-day 4-day 7-day 10-day
Pangu-Weather [1] 0.1182 0.1859 0.4509 0.6960 0.7582
FuXi [6] 0.1258 0.2050 0.4742 0.6484 0.7831
Fengwu [7] 0.1252 0.2028 0.4860 0.6887 0.8143
GraphCast [3] 0.0784 0.1519 0.3599 0.5521 0.7006
OneForecast [28]0.0754 0.13930.3275 0.5042 0.6398
S3N (Ours) 0.1009 0.16630.3171 0.4411 0.5177
Table 2 compares the mean normalized RMSE of different
forecasting models across lead times. S 3N achieves the best
performance at 4-, 7-, and 10-day lead times, with nRMSE
values of 0.3171, 0.4411, and 0.5177, respectively. In partic-
ular, its advantage becomes more pronounced as the forecast
horizon increases, reducing the 10-day nRMSE by 19.1% com-
pared with the second-best OneForecast. Although S3N is less
competitive at short lead times of 6 hours and 1 day, the results
demonstrate its stronger capability in maintaining forecast
accuracy over longer horizons.
Table 3. Absolute nRMSE growth between adjacent lead times
and total growth from 6 hours to 10 days. Lower is better.
Method
6-hour 1-day 4-day 7-day 6-hourto to to to to1-day 4-day 7-day 10-day 10-day
Pangu-Weather 0.0677 0.2650 0.24510.06220.6400
FuXi 0.0792 0.2692 0.1742 0.1347 0.6573
Fengwu 0.0776 0.2832 0.2027 0.1256 0.6891
GraphCast 0.0735 0.2080 0.1922 0.1485 0.6222
OneForecast0.06390.1882 0.1767 0.1356 0.5644
S3N (Ours) 0.0654 0.1508 0.12400.0766 0.4168
Table 3 further compares absolute nRMSE growth across
forecast horizons. S3N achieves the lowest growth from 1 to
4 days (0.1508), from 4 to 7 days (0.1240), and from 6 hours
to 10 days (0.4168). It also ranks second in the remaining
intervals, indicating slower error accumulation and stronger
long-range forecasting stability.
3.4. Ablation Study
Table 4. Component ablation study of our AQSS. Mean nor-
malized RMSE (lower is better) across different lead times.
The best result is in bold, and the second best is underlined.
“w/o” means “without” , “F. W.” means “Fixed-Weight”.
Method 6-hour 1-day 4-day 7-day 10-day
S3N (Full)0.1009 0.1663 0.3171 0.4411 0.5177
Fixed-Weight Path Fusion 0.2536 0.4428 0.5657 0.5936 0.6135
F. W. w/o SSM Guidance 0.2934 0.5681 1.1924 1.6932 2.1993
F. W. w/o Attention 0.4314 0.7548 1.3075 1.6489 1.9567
w/o SSM Guidance 0.1663 0.4241 1.2322 1.7837 2.3103
w/o Input Fusion 0.3585 0.6569 0.9055 1.0418 1.1598
We ablate the main components of AQSS, including
weighted path fusion, cross-latitude attention, attention-guided
SSM modulation, and input fusion. As shown in Table 4,
the full model achieves the lowest nRMSE at all lead times.
Replacing weighted path fusion with fixed weights sub-
stantially degrades short-range accuracy, while disabling
attention-guided SSM parameter modulation causes the largest
long-range deterioration, increasing the 10-day nRMSE from
0.5177 to 2.3103. Removing input fusion also increases the
10-day nRMSE to 1.1598. These results indicate that weighted
path fusion mainly benefits short-range prediction, while
attention-guided SSM parameter modulation is critical for
suppressing autoregressive error accumulation.
4. CONCLUSION
We presented an MLWP network named S 3N, combining
L2Proj and AQSS. L2Proj is an L2 finite-element mapping
method, while AQSS models HP fields through attention-
guided global spiral scans. Experiments show that S 3N
achieves strong performance in long-range forecasting with
lower error accumulation. Future work will focus on im-
proving the mapping resolution between the two grids and
short-range forecasting performance.

5. REFERENCES
[1] K. Bi, L. Xie, H. Zhang, X. Chen, X. Gu, and Q. Tian,
“Accurate medium-range global weather forecasting with
3D neural networks,”Nature, vol. 619, no. 7970, pp.
533–538, 2023.
[2] J. Pathak et al., “FourCastNet: A global data-driven high-
resolution weather model using adaptive fourier neural
operators,”arXiv preprint arXiv:2202.11214, 2022.
[3] R. Lam et al., “Learning skillful medium-range global
weather forecasting,”Science, vol. 382, no. 6677, pp.
1416–1421, 2023.
[4] D. Kochkov et al., “Neural general circulation models
for weather and climate,”Nature, vol. 632, no. 8027, pp.
1060–1066, 2024.
[5] C. Bodnar et al., “A foundation model for the earth
system,”Nature, vol. 641, no. 8065, pp. 1180–1187,
2025.
[6] L. Chen et al., “FuXi: A cascade machine learning
forecasting system for 15-day global weather forecast,”
npj Clim. Atmos. Sci., vol. 6, 2023, Art. no. 190.
[7] K. Chen et al., “The operational medium-range deter-
ministic weather forecasting can be extended beyond a
10-day lead time,”Commun. Earth Environ., vol. 6, 2025,
Art. no. 518.
[8] T. Nguyen, J. Brandstetter, A. Kapoor, J. K. Gupta, and
A. Grover, “ClimaX: A foundation model for weather
and climate,” inProc. 40th Int. Conf. Mach. Learn.
(ICML), 2023, vol. 202, pp. 25904–25938.
[9] T. Nguyen et al., “Scaling transformer neural networks
for skillful and reliable medium-range weather forecast-
ing,” inAdv. Neural Inf. Process. Syst., 2024, vol. 37, pp.
68740–68771.
[10] B. Bonev et al., “Spherical fourier neural operators:
Learning stable dynamics on the sphere,” inProceed-
ings of the 40th International Conference on Machine
Learning, 2023, vol. 202, pp. 2806–2823.
[11] S. Lang et al., “AIFS—ECMWF’s data-driven forecast-
ing system,”arXiv preprint arXiv:2406.01465, 2024.
[12] I. Price et al., “Probabilistic weather forecasting with
machine learning,”Nature, vol. 637, no. 8044, pp. 84–90,
2025.
[13] K. M. G´orski et al., “HEALPix: A framework for high-
resolution discretization and fast analysis of data dis-
tributed on the sphere,”The Astrophysical Journal, vol.
622, no. 2, pp. 759–771, 2005.
[14] N. Perraudin, M. Defferrard, T. Kacprzak, and R. Sgier,
“DeepSphere: Efficient spherical convolutional neural
network with HEALPix sampling for cosmological appli-
cations,”Astron. Comput., vol. 27, pp. 130–146, 2019.
[15] N. Krachmalnicoff and M. Tomasi, “Convolutional neu-
ral networks on the HEALPix sphere: A pixel-based
algorithm and its application to CMB data analysis,”As-
tron. Astrophys., vol. 628, 2019, Art. no. A129.
[16] N. Mahmoudian Bidgoli, R. G. de A. Azevedo,
T. Maugey, A. Roumy, and P. Frossard, “OSLO: On-
the-sphere learning for omnidirectional images and its
application to 360-degree image compression,”IEEE
Transactions on Image Processing, vol. 31, pp. 5813–
5827, 2022.
[17] Y . Zhu, H. Xiong, L. Xiao, R. Shi, Q. Gu, and L. Gu,
“SCE-Depth: A spherical compound eye framework for
wide FOV depth estimation,” inProc. IEEE/CVF Conf.
Comput. Vis. Pattern Recognit. (CVPR), 2026, pp. 26964–
26973.
[18] Z. Bao, S. Shen, X. Shen, C. Liang, and C. Xiao, “Illumi-
nation explorer: All-frequency illumination estimation
via HEALPix-guided diffusion,”IEEE Trans. Image
Process., vol. 35, pp. 8456–8469, 2026.
[19] M. Karlbauer et al., “Advancing parsimonious deep
learning weather prediction using the HEALPix mesh,”
J. Adv. Model. Earth Syst., vol. 16, no. 8, 2024, Art. no.
e2023MS004021.
[20] V . Ramavajjala, “HEAL-ViT: Vision transformers on a
spherical mesh for medium-range weather forecasting,”
arXiv preprint arXiv:2403.17016, 2024.
[21] N. Cresswell-Clay et al., “A deep learning earth system
model for efficient simulation of the observed climate,”
AGU Adv., vol. 6, no. 4, 2025, Art. no. e2025A V001706.
[22] H. Linander, C. Petersson, D. Persson, and J. E. Gerken,
“PEAR: Equal area weather forecasting on the sphere,”
arXiv preprint arXiv:2505.17720, 2025.
[23] O. Carlsson et al., “HEAL-SWIN: A vision transformer
on the sphere,” inProc. IEEE/CVF Conf. Comput. Vis.
Pattern Recognit. (CVPR), 2024, pp. 6067–6077.
[24] G. Dziuk, “Finite elements for the beltrami operator on
arbitrary surfaces,” inPartial Differential Equations and
Calculus of V ariations, vol. 1357 ofLect. Notes Math.,
pp. 142–155. Springer, Berlin, Germany, 1988.
[25] G. Dziuk and C. M. Elliott, “Finite element methods for
surface PDEs,”Acta Numer ., vol. 22, pp. 289–396, 2013.
[26] A. Gu and T. Dao, “Mamba: Linear-time sequence
modeling with selective state spaces,” inProc. 1st Conf.
Lang. Model. (COLM), 2024.
[27] Y . Liu et al., “VMamba: Visual state space model,” in
Adv. Neural Inf. Process. Syst., 2024, vol. 37, pp. 103031–
103063.
[28] Y . Gao et al., “OneForecast: A universal framework
for global and regional weather forecasting,” inProc.
42nd Int. Conf. Mach. Learn. (ICML), 2025, vol. 267, pp.
18658–18697.
[29] H. Hersbach et al., “The ERA5 global reanalysis,”Quar-
terly Journal of the Royal Meteorological Society, vol.
146, no. 730, pp. 1999–2049, 2020.
[30] Stephan Rasp, Stephan Hoyer, Alexander Merose,
Ian Langmore, Peter Battaglia, Tyler Russell, Alvaro
Sanchez-Gonzalez, Vivian Yang, Rob Carver, Shreya
Agrawal, et al., “Weatherbench 2: A benchmark for the
next generation of data-driven global weather models,”
Journal of Advances in Modeling Earth Systems, vol. 16,
no. 6, pp. e2023MS004019, 2024.
[31] F. Molteni, R. Buizza, T. N. Palmer, and T. Petroliagis,
“The ECMWF ensemble prediction system: Methodol-
ogy and validation,”Quarterly Journal of the Royal
Meteorological Society, vol. 122, no. 529, pp. 73–119,
1996.
