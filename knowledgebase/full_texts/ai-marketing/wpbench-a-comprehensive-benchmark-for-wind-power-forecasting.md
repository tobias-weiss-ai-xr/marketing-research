---
title: 'WPBench: A Comprehensive Benchmark for Wind Power Forecasting'
url: https://arxiv.org/abs/2609.24444
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yuhan Zhu
- Jilin Hu
- Xinying Cai
- Yingshan Li
- Li Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.24444
pages: 15
chars: 87329
fetched_at: '2026-11-08T13:24:37+00:00'
kb_version: 1
---

# WPBench: A Comprehensive Benchmark for Wind Power Forecasting

WPBench: A Comprehensive Benchmark
for Wind Power Forecasting
Yuhan Zhu1, Jilin Hu 1, Xinying Cai 1, Yingshan Li 1, Li Ma 1, Xiangfei Qiu 1
Linsen Li 2,3, Kai Zhang 1,3, Yao Fu 3, Weihao Jiang 3, Bin Yang 1
1School of Data Science & Engineering, East China Normal University, Shanghai, China
2College of Computer Science and Technology, Zhejiang University, Hangzhou, China
3Hangzhou Hikvision Digital Technology Co., Ltd., Hangzhou, China
1{yhzhu, 10245501404, 10245501444, 10245501419, xfqiu}@stu.ecnu.edu.cn, 1{jlhu, byang}@dase.ecnu.edu.cn
3{lilinsen, zhangkai23, fuyao, jiangweihao5}@hikvision.com
Abstract—Accurate, reliable, and deployable wind power fore-
casting is critical for power system dispatch, renewable energy
integration, and electricity market operations. Progress in this
field hinges on the ability to empirically and comprehensively
benchmark forecasting methods. Yet existing benchmarks fall
short of supporting systematic evaluation in four key aspects:
1) limited coverage of wind power scenarios across turbine
scale, variable composition, and spatial structure; 2) incomplete
coverage of forecasting model families; 3) evaluation metrics mis-
aligned with wind power requirements; and 4) limited structure-
aware diagnostics beyond individual temporal patterns. To ad-
dress these limitations, we propose WPBench, a comprehensive,
fair, and extensible benchmark for wind power forecasting.
WPBench integrates 26 public datasets organized by turbine scale
and variable composition, spanning single-turbine, multi-turbine,
univariate, and multivariate settings. Under unified processing,
training, and evaluation protocols, it benchmarks 19 representa-
tive models covering traditional methods, deep temporal models,
spatio-temporal models, and foundation models. Beyond point-
wise errors, WPBench assesses forecast-curve fidelity and com-
putational efficiency, and delivers structure-aware diagnostics
across temporal, variable-dependency, and spatial-dependency
perspectives. Together, these capabilities enable systematic model
comparison across diverse wind scenarios and provide a reusable
platform for future research.
I. INTRODUCTION
Wind power has become a pivotal renewable energy source
in the global transition toward low-carbon power systems,
evolving from a supplementary resource into an indispensable
component of modern power grids as installed capacity contin-
ues to grow [1]–[3]. However, wind power generation is highly
dependent on wind speed, wind direction, and meteorologi-
cal conditions, exhibiting strong stochasticity, intermittency,
and volatility [4]–[6]. Such characteristics bring considerable
difficulties to grid stability, supply-demand balancing, and
system operation, making accurate and reliable wind power
forecasting a fundamental requirement for renewable energy
integration and power system management [5]–[8].
Although wind power forecasting can be formulated as a
time series prediction problem, wind power data differ fun-
damentally from ordinary single-sequence time series. Unlike
traffic flow, electricity load, or meteorological observations,
wind power data are jointly shaped by weather regimes,
turbine operating states, wind farm layouts, control strategies,
and grid dispatch requirements. As a result, forecasting tasks
in this domain vary substantially in structure: some datasets
contain only a single turbine with one target power channel;
others incorporate SCADA variables, NWP covariates, or ad-
ditional weather and operating-state features; and wind-farm-
level datasets typically involve multiple turbines with intricate
spatial and spatio-temporal dependencies. These structural
differences directly affect the information available to fore-
casting models and the dependencies they are expected to
capture. Moreover, forecasting objectives extend well beyond
minimizing point-wise errors, as predictions must support grid
integration, operational scheduling, market participation, and
real-time decision making. Together, these properties establish
wind power forecasting as a dedicated application scenario
rather than a simple subcase of general time series forecasting.
Given this distinctive nature, wind power forecasting cannot
be properly evaluated by directly applying general-purpose
time series benchmarks. Merely appending a few wind datasets
to an existing evaluation suite fails to reflect the diverse
data structures, model applicability, and operational constraints
that characterize wind power scenarios. This calls for a
dedicated and systematic benchmark tailored to wind power
forecasting. However, as summarized in Figure 1, existing
studies and benchmarks remain limited in four key aspects:
scenario coverage gap, incomplete model-family evaluation,
metric mismatch, and limited structure-aware diagnostics. We
elaborate on each of these limitations in the following.
Issue 1: Limited coverage of wind power scenarios.Wind
power forecasting is not a single homogeneous scenario. Fol-
lowing the benchmarking insight that different domains exhibit
different time-series characteristics [9], [10], wind forecasting
also requires coverage of diverse structures within the same
domain. Wind datasets can be naturally organized along two
axes, the number of turbines and the number of observed
variables, yielding four representative scenarios: single-turbine
univariate, single-turbine multivariate, multi-turbine univariate,
and multi-turbine multivariate forecasting. These scenarios
evaluate different model capabilities, including target-series
temporal modeling, covariate-aware modeling with SCADA,
NWP, or meteorological variables, cross-turbine dependency
modeling, and their combination. Thus, wind scenario cov-
arXiv:2609.24444v1  [cs.LG]  21 Sep 2026

1 Scenario Coverage Gap
l Underrepresented wind scenarios
l Biased toward multivariate / multi-turbine
Univariate Multivariate
Single-
turbine
Multi-
turbine
1T1V 1TMV
MT1V MTMV
2 Incomplete Model Evaluation
l Partial model landscape
l No unified cross-family protocol
Stat/ML
 Deep
Temporal TSFM
Deep ST
 STFM
3 Metric Mismatch
l Beyond point-wise error
l Deployment cost matters
Accuracy
MAE,RMSE Truth
Forecast
Shape
 Efficiency
4 Limited Diagnostics
l Mostly temporal-only
l Missing variable & spatial views
Temporal
 Variable
 Spatial
WPBench
Fig. 1. In wind power forecasting, existing benchmark frameworks often
face four issues: scenario coverage gap, incomplete model-family evaluation,
metric mismatch, and limited structure-aware diagnostics.
erage is not merely about including more wind datasets, but
about covering structurally different tasks that reflect different
forecasting requirements.
General-purpose TSF benchmarks such as TFB [11], fev-
bench [12], and GIFT-Eval [13] include broad cross-domain
forecasting tasks and some wind-related datasets or tasks.
However, these wind tasks are usually treated as ordinary
time series or multivariate time series within a general evalu-
ation suite, rather than being organized around wind-specific
structural diversity. In particular, they lack a systematic multi-
turbine perspective for evaluating spatial relationships among
turbines and the corresponding spatio-temporal or graph-based
modeling requirements. Within the wind domain, public re-
sources such as SDWPF [14], GEFCom 2012 [15], GEFCom
2014 [16], and OpenWPF [17] have advanced wind forecast-
ing evaluation, but their coverage remains concentrated on
specific settings, such as large-scale multi-turbine wind-farm
forecasting, multivariate wind forecasting, or neural cross-
dataset evaluation. They still lack balanced structural con-
trasts across target-only temporal modeling, covariate-aware
modeling, spatial dependency modeling, and the combined
multi-turbine multivariate setting. This imbalance makes it
difficult to separate model weakness from dataset-structure
bias, and limits analysis of how different wind scenarios affect
forecasting requirements and model behavior.
Issue 2: Incomplete coverage of forecasting model fam-
ilies.The diversity of wind data structures also complicates
model selection. Single-turbine tasks can often be modeled
as ordinary temporal forecasting problems, where statistical
models, machine learning methods, and deep temporal models
use historical power, SCADA variables, or meteorological
covariates [18]–[20]. In contrast, multi-turbine, multi-farm,
and regional tasks contain spatial correlations induced by
turbine locations, wind propagation, wake effects, and similar
operating states, making spatio-temporal or graph-based mod-
els relevant [21]–[24]. Existing studies have explored these
110 120 130 140 150 160 170 180
Time
0.5
0.6
0.7
0.8
0.9
1.0Normalized Power
A: nMAE=0.050, nDTW=0.035B: nMAE=0.048, nDTW=0.016
Similar nMAE, different temporal fidelity
Ground Truth Prediction A Prediction B
Fig. 2. Point-wise error alone can be insufficient for wind power forecasting
evaluation. Predictions with similar MAE may still differ in fluctuation
alignment and forecast-curve fidelity.
directions separately, but few benchmarks compare them under
the same data processing, training, and evaluation protocol.
As a result, current WPF benchmarks provide only a partial
view of model suitability. Statistical WPF benchmarks mainly
focus on statistical models [25]; OpenWPF [17] promotes
cross-dataset evaluation for neural networks, but still em-
phasizes deep temporal models rather than jointly covering
temporal and spatio-temporal paradigms. Meanwhile, time-
series foundation models and spatio-temporal foundation mod-
els are rapidly developing and claim strong domain general-
ization ability [26]–[29], yet they have not been systemati-
cally evaluated for wind forecasting. A comprehensive wind
benchmark should therefore cover statistical learning, machine
learning, deep temporal models, deep spatio-temporal models,
time-series foundation models, and spatio-temporal foundation
models under a unified protocol.
Issue 3: Metrics misaligned with wind-power require-
ments.Point-wise error metrics such as MAE, RMSE, MAPE,
nMAE, and nRMSE are widely used in WPF studies [30].
However, low point-wise error does not guarantee that the
predicted curve preserves critical wind power patterns. As
illustrated in Figure 2, two predictions with similar MAE
may still differ substantially in the temporal alignment of
fluctuations and forecast-curve fidelity. Prior TSF research
has similarly shown that similar MSE values may correspond
to very different forecast shapes, especially for abrupt or
non-stationary sequences, where point-wise metrics can miss
differences in fluctuation alignment and curve shape [31].
This issue is more consequential in wind forecasting, where
operators care whether forecasts track fluctuations, preserve
trend shapes, and capture ramp events that affect dispatch and
grid operation [32], [33].
In addition, WPF is a deployment-oriented industrial task.
As deep temporal models, spatio-temporal models, and foun-
dation models are introduced, models differ substantially in
training cost, inference latency, memory usage, and parameter
size. A model with slightly better numerical accuracy may

still be unsuitable for real-time forecasting or large-scale
wind-farm deployment if its computational cost is too high.
Therefore, wind benchmarks should evaluate models in terms
of numerical accuracy, forecast-curve fidelity, and efficiency.
Issue 4: Limited structure-aware diagnostics beyond indi-
vidual temporal patterns.Structure-aware diagnostics aim to
explain how data-structural factors in a forecasting task affect
model behavior, rather than only reporting average errors or
rankings. In wind power forecasting, this means analyzing
not only the temporal patterns of individual target power
series, but also the relationships between auxiliary variables
and power output, as well as spatial relationships among
turbines. Recent TSF benchmarks have begun to move toward
diagnostic benchmarking. For example, TFB [11] and TIME
[34] analyze temporal properties of target series, such as
trend, seasonality, stability, and predictability, together with
variable correlations. These analyses are valuable, but they still
provide a limited view of wind forecasting because they do not
explicitly diagnose how covariate relationships and turbine-
level spatial structures affect model behavior.
This perspective is not sufficient to describe the structure of
wind forecasting tasks. For example, two wind datasets may
have target power series with similar seasonality or volatility,
but differ in whether they provide informative covariates such
as wind speed or NWP variables, or whether they contain
meaningful cross-turbine dependencies. Thus, task difficulty is
not determined only by non-stationarity, volatility or season-
ality of the target series; it also depends on target–covariate
relationships and turbine-level spatial dependencies. A wind
benchmark should therefore extend dataset characterization
beyond individual temporal patterns and organize diagnostics
across richer dimensions, including temporal patterns of target
power series, variable dependencies between power and auxil-
iary covariates, and spatial relationships among turbines. Such
structure-aware diagnostics can better explain why temporal,
spatio-temporal, channel-independent, channel-dependent, and
foundation models behave differently under different wind data
organizations.
To address these limitations, we presentWPBench, a com-
prehensive and fair benchmark for wind power forecasting.
WPBench treats wind power forecasting as a first-class fore-
casting scenario rather than a small subset of general time
series prediction. It organizes open wind datasets according
to wind-specific data structures, evaluates broad forecasting
model families under a unified protocol, and assesses perfor-
mance from multiple perspectives that reflect both forecasting
accuracy and operational requirements. In addition, WPBench
provides structure-aware diagnostics to better understand how
temporal patterns, variable dependencies, and spatial structures
affect different forecasting models. In this way, WPBench is
designed not only to rank methods, but also to clarify which
types of models are reliable under different wind data organi-
zations. The benchmark artifact further supports reproducible
comparison and future extension with new datasets, models,
metrics, and diagnostic protocols.
Our contributions are summarized as follows.
•Comprehensive Wind Power Dataset Organization.We
curate and organize 26 open-source wind power datasets
along two dimensions—number of turbines and number of
variables—yielding a balanced coverage of single-turbine
univariate, single-turbine multivariate, multi-turbine uni-
variate, and multi-turbine multivariate settings. This is
the first benchmark to explicitly cover all four structural
categories, enabling controlled analysis of how data orga-
nization affects model behavior.
•Comprehensive Evaluation of Model Families.We
benchmark 19 representative models across five fami-
lies—statistical/ML models, deep temporal models, time-
series foundation models, deep spatio-temporal models,
and spatio-temporal foundation models—under unified
experimental protocols. This is the most comprehensive
model-family comparison in wind power forecasting to
date, revealing which model types are suited to which
data structures.
•Multi-dimensional Evaluation Aligned with Opera-
tional Requirements.We adopt a diverse set of evaluation
metrics that go beyond point-wise errors to jointly assess
numerical accuracy, forecast-curve fidelity, and compu-
tational efficiency. Unlike existing benchmarks that rely
solely on MAE/MSE, these metrics reflect forecasting
quality dimensions that directly matter for grid dispatch,
market participation, and real-time deployment.
•Structure-aware Diagnostic Analysis.We provide sys-
tematic diagnostic experiments that attribute model per-
formance to three structural factors: temporal patterns in
target power series, dependencies between power output
and auxiliary covariates, and spatial correlations among
turbines. These diagnostics produce interpretable explana-
tions of why certain model families succeed or fail under
specific wind data organizations.
II. RELATEDWORK
A. Time Series and Spatio-Temporal Forecasting Benchmarks
Time series describe temporally ordered numerical mea-
surements and serve as a fundamental data representation for
capturing the dynamic behavior of real-world systems [35].
Such data arise extensively in practical domains, including
energy, transportation, environmental monitoring, industrial
applications, and healthcare [36]–[44]. Research on time series
covers a variety of analytical problems, ranging from forecast-
ing [45], [46] and anomaly detection [10], [47], [48] to other
temporal modeling tasks. Among these problems, multivariate
time series forecasting has received substantial attention, with
the goal of estimating future values of multiple variables based
on their past observations. As forecasting techniques continue
to grow in both number and diversity, unified and dependable
evaluation frameworks are increasingly needed to support fair
model comparison and to reveal the respective strengths and
weaknesses of different approaches.
To this end, time series forecasting benchmarks provide
a unified basis for evaluating forecasting methods and have
played an important role in promoting standardized model

TABLE I
COMPARISON OFWPBENCH WITH REPRESENTATIVE FORECASTING
BENCHMARKS.
Benchmark Wind- spec. Struct. cov. Temp. models ST models Found. models Shape eval. Struct. diag.
TFB [11]× ×✓× × × ◦
fev-bench [12]× ×✓×✓× ◦
GIFT-Eval [13]× ×✓×✓× ◦
TIME [34]× × × ×✓× ◦
OpenWPF [17]✓◦✓× × × ×
SDWPF [14]✓◦ × × × × ×
Statistical WPF [25]✓◦✓× × × ◦
WPBench✓ ✓ ✓ ✓ ✓ ✓ ✓
×: absent;✓: present;◦: partial or limited support.
comparison. Early benchmarks, such as M3 [49], M4 [50],
and Monash [51], mainly focused on univariate forecasting and
cross-domain dataset collection. Later benchmarks, including
LTSF-Linear [52], TSlib [53], BasicTS [54], and TFB [11],
extended evaluation to long-term forecasting, multivariate
forecasting, and deep learning methods. With the rise of time-
series foundation models and realistic forecasting evaluation,
GIFT-Eval [13], TSFM-Bench [55], fev-bench [12], and TIME
[34] further emphasize zero-shot or few-shot evaluation [56],
cross-domain generalization, covariate-rich tasks, realistic task
settings, and diagnostic analysis.
Spatio-temporal forecasting benchmarks evaluate models
on data with both temporal dynamics and spatial structures
[57]. For example, LibCity [58] focuses on urban spatio-
temporal prediction, while BasicTS [54] and BasicTS+ [59]
provide unified support for multivariate and spatio-temporal
forecasting methods. These benchmarks show the importance
of jointly modeling temporal evolution and spatial dependen-
cies. However, their scenarios are still largely concentrated
on broad domains such as traffic, urban computing, and
weather forecasting. Wind power forecasting therefore remains
underrepresented as a distinct energy-domain scenario.
B. Wind Power Forecasting Datasets and Benchmarks
Several public datasets, competitions, and benchmarks have
promoted standardized comparison in wind power forecast-
ing. GEFCom 2012/2014 provided classical wind forecasting
competition tasks [15], [16]; SDWPF [14] released a large-
scale multi-turbine dataset with SCADA variables and turbine
spatial information; OpenWPF integrated multiple public wind
power datasets for cross-dataset evaluation of neural network-
based WPF [17]; and statistical WPF benchmarks have sup-
ported standardized comparison of statistical forecasting mod-
els [25]. These efforts have advanced data openness and
comparative evaluation in the wind forecasting community.
Nevertheless, existing wind-domain resources are usually
centered on specific task settings, partial data structures, or
limited model families. Table I summarizes the positioning of
WPBench against representative forecasting benchmarks.
C. Wind Power Forecasting Methods
Wind power forecasting has been studied under diverse
modeling paradigms. One line of work formulates WPF
as a temporal or multivariate temporal forecasting problem,
where historical power records, SCADA variables, NWP co-
variates, and meteorological observations are used to model
temporal dependencies, variable interactions, and nonlinear
dynamics [37], [38]. Early approaches primarily relied on
statistical models and classical machine learning methods [60].
With the rapid advances of deep learning and its strong
representation learning capability demonstrated across areas
such as computer vision and video generation [61]–[64], deep
neural networks have been increasingly adopted for wind
power forecasting. Representative deep forecasting architec-
tures include LSTM, GRU, CNN, TCN, and Transformer-
based models [65]–[67].
Another line of work focuses on multi-turbine, multi-farm,
or regional forecasting, where turbines, wind farms, or regions
are represented as nodes and graph neural networks, spatio-
temporal graph models, or spatio-temporal Transformers are
used to capture cross-node dependencies [23], [28], [41], [68],
[69]. Recent studies such as PowerMistral and WindLLM also
explore pre-trained large models for WPF [70], [71].
These method families are often evaluated in separate
experimental settings, making it difficult to compare temporal
models, spatio-temporal models, and foundation models under
a unified protocol. WPBench is complementary to existing
forecasting benchmarks and wind-domain studies: it focuses
on organizing open wind datasets by data structure, evaluating
broad model families consistently, and supporting structure-
aware diagnostics for wind-specific forecasting scenarios.
III. PRELIMINARIES
A. Wind Power Forecasting Setting
LetX ∈RN×T×C denote a wind power time series dataset,
whereNis the number of turbines or spatially separated wind
power series,Tis the number of time steps, andCis the
number of observed channels. The first channel is the target
wind power series, denoted byY∈R N×T , and the remaining
channels, when available, are auxiliary covariates such as wind
speed, wind direction, temperature, or turbine operating states.
Given a look-back window of lengthL, the forecasting task
is to predict the target power values over the nextHsteps,
whereY :,t+1:t+H ∈R N×H :
bY:,t+1:t+H =f θ(X:,t−L+1:t,:),(1)
whereHis the forecasting horizon. This unified formulation
covers single-turbine and multi-turbine datasets, as well as
settings with or without auxiliary covariates.
B. Dataset Characterization Metrics
Existing forecasting benchmarks have shown that dataset
characteristics help explain why different models succeed
under different temporal patterns [11], [34]. For wind power
forecasting, however, the relevant structure is not limited to the
target power sequence. A dataset may also contain auxiliary
SCADA or meteorological variables, multiple turbine nodes,
and spatially organized power series. WPBench therefore
characterizes each dataset from three perspectives: temporal

Algorithm 1Calculating shifting for a target power series.
Require:Target seriesx∈R T ; number of thresholdsm
Ensure:Shifting(x)
1: Normalizexby z-score transformation to obtainz
2:z min ←min(z),z max ←max(z)
3:S ← {zmin + (i−1)(z max −z min)/m|1≤i≤m}
4:foreach thresholds i ∈ Sdo
5:K i ← {j|zj > si,1≤j≤T}
6:M i ←median(K i)
7:end for
8:M ′ ←MinMaxNormalize(M 1, . . . , Mm)
9:returnShifting(x)← |median(M ′)|
patterns of the target power series, dependencies between
target power and auxiliary variables, and spatial dependencies
among turbine targets.
1) Temporal Characteristics:For each turbine, the first
column in its variable group is treated as the target power
seriesx∈R T . Following the common practice of time-
series characterization, WPBench uses STL decomposition to
separate recurring, long-term, and residual components:
xt =S t +G t +R t,(2)
whereS t,G t, andR t denote the seasonal, trend, and residual
components, respectively. Candidate periods are generated
from FFT peaks and a default period set, and the decomposi-
tion with the strongest seasonal component is retained.
Seasonality.Seasonality measures the strength of recurring
patterns in the target power series and is computed as an
explained-variance ratio:
Seasonality(x) = max

0,1− Var(R) Var(x−G)  .(3)
Dataset-level seasonality is obtained by averaging valid
turbine-level values.
Shifting.Shifting describes how strongly the distribution of a
target power series drifts over time. In wind power data, such
drift may be caused by changing weather regimes, turbine op-
erating states, curtailment, or abnormal events. Larger values
indicate stronger deviation from a stable temporal distribution.
Algorithm 1 summarizes the threshold-exceedance procedure
used to compute this descriptor.
Short-term and long-term JSD.WPBench further measures
distributional irregularity with Jensen–Shannon divergence
(JSD). Short-window JSD captures local non-Gaussian fluctua-
tions and abrupt irregularity, while long-window JSD captures
broader regime-level distributional deviation. For a window
sizes, letW s(x)be the set of non-overlapping complete
windows fromx. For each windoww∈ W s(x), an empirical
densityP w is estimated with a Stone-rule histogram, and a
Gaussian referenceQ w is fitted using the same window’s mean
and standard deviation. The window-level divergence is
JSD(Pw, Qw) = 1 2 KL(Pw∥Mw) + 1 2 KL(Qw∥Mw),
Mw = 1 2 (Pw +Q w). (4)
The score for window sizesis
JSDs(x) = 1 |Ws(x)| X w∈Ws(x) JSD(Pw, Qw).(5)
WPBench reports short-term and long-term JSD usings= 30
ands= 336, respectively, and averages the resulting scores
over valid turbine targets.
2) Variable Dependency Characteristics:Variable depen-
dency metrics describe how strongly the target power series is
associated with auxiliary variables.
VarCorr.For a turbine with targetyand covariatesZ=
[z1, . . . , zV−1 ], VarCorr measures the average absolute target-
covariate correlation over the full aligned series:
VarCorr(y, Z) = 1 V−1
V−1X
v=1
|ρ(y, zv)|.(6)
Variable TGV and GSD.Static correlation alone cannot show
whether the role of covariates changes over time. WPBench
therefore builds a dynamic target-covariate graph over non-
overlapping windows of lengths= 576. For each window
w, lety w andz v,w denote the target and thev-th covariate
restricted to that window. The target-covariate edge weights
are defined by
aw,v = cos(yw, zv,w), v= 1, . . . , V−1,(7)
wherecos(·,·)denotes cosine similarity, matching the
implementation of the dynamic descriptors. Leta w =
[aw,1, . . . , aw,V−1 ]⊤. These weights define a symmetric star-
shaped adjacency matrixA var w ∈R V×V :
(Avar w )1,v+1 = (Avar w )v+1,1 =a w,v, v= 1, . . . , V−1,(8)
with zero diagonal entries and zero covariate-covariate entries.
The corresponding unnormalized graph Laplacian is
Lvar w =D var w −A var w , D var w = diag(Avar w 1).(9)
Letλ(L var w )be the sorted real eigenvalue vector. WithKcom-
plete windows, the dynamic variable-dependency descriptors
are
Var-TGV = 1 K−1
K−1X
w=1
∥aw+1 −a w∥2√
V−1 ,(10)
Var-GSD = 1 K−1
K−1X
w=1
∥λ(Lvar w+1)−λ(L var w )∥2
V .(11)
Var-TGV measures how rapidly target-covariate edge weights
change, while Var-GSD measures structural change through
the Laplacian spectrum. Dataset-level values are averaged
over turbines with valid covariates and at least two complete
windows.

Algorithm 2Calculating temporal graph volatility (TGV).
Require:Window-level dependency representations{G w}K w=1; normaliza-
tion constantd TGV
Ensure:TGV
1:V ← ∅
2:forw= 1toK−1do
3:v w ← ∥Gw+1 −G w∥/dTGV
4:V ← V ∪ {vw}
5:end for
6:returnTGV←mean(V)
Algorithm 3Calculating graph spectral divergence (GSD).
Require:Window-level adjacency matrices{A w}K w=1; normalization con-
stantd GSD
Ensure:GSD
1:forw= 1toKdo
2:L w ←diag(A w1)−A w
3:ℓ w ←sorted eigenvalues ofL w
4:end for
5:D ← ∅
6:forw= 1toK−1do
7:d w ← ∥ℓw+1 −ℓ w∥2/dGSD
8:D ← D ∪ {dw}
9:end for
10:returnGSD←mean(D)
3) Spatial Dependency Characteristics:Spatial depen-
dency metrics describe relationships among turbine target
power series.
SpatialCorr.For a multi-turbine dataset, letY= [y 1, . . . , yN ]
collect theNturbine targets. SpatialCorr measures the average
absolute Pearson correlation over all turbine pairs:
SpatialCorr(Y) = 2 N(N−1) X 1≤i<j≤N |ρ(yi, yj)|.(12)
Spatial TGV and GSD.To characterize time-varying spatial
interactions, WPBench constructs a turbine graph in each non-
overlapping window of lengths= 576. Lety i,w denote the
target series of turbineirestricted to windoww. The spatial
adjacency matrixA spa w ∈R N×N is defined elementwise as
(Aspa w )ij = cos(yi,w, yj,w), i̸=j,(A spa w )ii = 1,(13)
which follows the cosine-similarity matrix used in the imple-
mentation. With
Lspa w =D spa w −A spa w , D spa w = diag(Aspa w 1),(14)
the spatial dynamic descriptors are
Spatial-TGV = 1 K−1
K−1X
w=1
∥Aspa w+1 −A spa w ∥F
N ,(15)
Spatial-GSD = 1 K−1
K−1X
w=1
∥λ(Lspa w+1)−λ(L spa w )∥2
N
√
N
.(16)
Spatial-TGV measures volatility in turbine-to-turbine edge
weights, and Spatial-GSD measures spectral changes in the
turbine interaction graph. The general TGV and GSD compu-
tations are summarized in Algorithms 2 and 3.
IV. WPBENCH
Figure 3 presents the overall workflow of WPBench, cov-
ering data collection and preprocessing, model organization,
unified evaluation, and benchmarking with structure-aware
diagnostics. The following subsections describe these compo-
nents in detail.
A. Dataset Collection and Preprocessing
WPBench contains 26 publicly accessible wind power
datasets collected from public repositories, forecasting com-
petitions, and datasets released with prior studies. These
datasets differ in sampling frequency, variable composition,
turbine scale, and data quality. To support unified modeling
and evaluation, we standardize them into a turbine–time–
channel representation, where each dataset contains one or
more target power series at the turbine or site level and, when
available, auxiliary covariates such as SCADA variables or
meteorological measurements.
The preprocessing pipeline follows a consistent but mini-
mally intrusive strategy. We align timestamps and sampling
frequencies, check temporal continuity, handle missing or
unreliable segments, identify the target wind power channel,
and retain semantically meaningful covariates. For multi-
turbine datasets, we further verify turbine alignment and
remove turbine records with severe missingness, long constant
periods, abnormal jumps, or clear temporal inconsistency.
Finally, visual sanity checks are conducted to detect artifacts
that are difficult to capture by rules alone. This process
removes obvious data artifacts while preserving valid temporal
variation, covariate information, and turbine-level structure.
B. Wind-Specific Dataset Organization
Wind power datasets differ not only in scale but also in
the structure of the forecasting problem. WPBench organizes
datasets along two wind-specific axes: the number of turbines
and the number of observed variables. The turbine axis deter-
mines whether the task contains spatial dependencies, while
the variable axis determines whether the model can exploit
target-covariate relationships. This yields four task types:
single-turbine univariate (1T1V), single-turbine multivariate
(1TMV), multi-turbine univariate (MT1V), and multi-turbine
multivariate (MTMV). Table II summarizes the 26 datasets
under this organization. All datasets are chronologically split
into training, validation, and testing sets according to the ratios
indicated in the Split column (e.g., 7:1:2).
Compared with existing wind forecasting resources, WP-
Bench emphasizes systematic coverage of wind-data organi-
zations. Existing public resources are usually concentrated on
specific representative scenarios: GEFCom focuses mainly on
competition-style wind power forecasting [15], [16], SDWPF
emphasizes multi-turbine wind farm forecasting [14], and
OpenWPF [17] mainly covers multivariate and multi-turbine
forecasting datasets. In contrast, WPBench covers single-
turbine univariate, single-turbine multivariate, multi-turbine
univariate, and multi-turbine multivariate tasks, enabling uni-
fied evaluation under target-series modeling, covariate-aware

MAE MSE
RMSE nMAE
EDF DTW
nDTW nDDTW
Parameters
Inference Time
Memory usage
Error Metrics Pattern Metrics Efficiency
WPBench:Wind Power Forecasting Benchmark
Data Sources
Repositories Competitions Prior Studies
Temporal Standardization
TimeStamp
Alignment
Frequency
Standardization
Missing Segment
Handling
Task-oriented Quality Control
Target / Covariate
Identification
Turbine
Filtering
Visual
Sanity Check
Unified Turbine-Time-Channel Representation
Data Collection & Preprocessing
Single-turbine
Univariate
Multi-turbine
Univariate
Single-turbine
Multivariate
Multi-turbine
Multivariate
Number of Variables
Number of Turbines
Modeling Evaluation
Model Family
TSFM STFM ST ML DeepTS
Zero-shot Few-shot Full-shot
Train Test
Time
Training Sample Generation Test Rolling Evaluation
Input series Target series input Forecast horizon
Overlapping sliding windows Stride = horizon (h)
Benchmarking & Diagnostics
Analysis / Diagnostics
Benchmarking
Error Ranking
MAE / RMSE / nMAE
Shape Ranking
DTW / nDTW / nDDTW
Best accuracy model Best shape-aware model
Structure Indicators
Temporal Variable Spatial
Indicators              Strong / Weak Tags
Performance Comparison
Alg 1
Alg 2
Alg 3
…
Alg n
Strong / Weak Tag
Weak               Strong
Data Set 1 Data Set 2
Performances under certain characteristics
Task-group Diagnostics
1T-1V 1T-MV MT-1V MT-MV
shape / error / ranking / efficiency
Unified Forecasting Sample
B:batch, N:turbines, T:look-back, C:variables
Temporal Modeling Spatio-Temporal Modeling
Flatten node dimension
into batch
Node-independent
forecasting
Preserve node dimension
Cross-turbine
Dependency modeling
Statistical / ML
LR , VAR
Deep Temporal
Dlinear , DUET,
iTransformer , etc
TS Foundation
Timer , Toto,
SEMPO , TTM , etc
Deep ST Models
STDN, STID ,
TGGC , etc
ST Foundation
Models
OpenCity, FlashST
Optuna Hyperparameter Tuning
Learning rate, dropout,
hidden layers, etc
Fairness
Val
Fig. 3. Overview of the WPBench benchmark workflow. WPBench transforms heterogeneous public wind power datasets into structure-aware forecasting
tasks, evaluates representative model families, and supports multi-dimensional performance and diagnostic analysis.
modeling, spatial dependency modeling, and their combined
setting.
Figure 4 further compares WPBench with representative
wind forecasting resources in terms of temporal patterns,
variable relationships, spatial dependencies, and data scale.
Compared with existing resources, WPBench provides a
broader and more balanced coverage envelope, with stronger
coverage of dataset characteristics involving complex variable
relationships, spatial dependencies, and scale variations.
C. Forecasting Models
To compare different forecasting paradigms in WPF, WP-
Bench includes 19 representative models from five categories:
1) statistical and machine learning models: LR [84], [85]
and V AR [86]; 2) deep temporal models: DLinear [87],
XLinear [88], DUET [89], PatchTST [90], iTransformer [91],
and xPatch [92]; 3) time-series foundation models: Timer
[93], TTM [94], TOTO [95], and SEMPO [96]; 4) deep
spatio-temporal models: STID [97], STDN [98], TGGC [99],
and BigST [100]; and 5) spatio-temporal foundation models:
OpenCity [101], FactoST-UTP [102], and FactoST-STA [102].
For foundation models, WPBench further provides three adap-
tation settings: zero-shot, few-shot, and full-shot.
D. Evaluator
Forecasting Protocol.WPBench evaluates models under a
fixed-window multi-step forecasting protocol. Given a look-
back window ofL= 576, each model predictsH∈
{12,24,72,144}future steps, covering short-term and longer-
horizon settings. Sliding windows are constructed from the
Temporal
Spatial
Shifting Seasonality
Features
Turbines
Short JSD
Long JSD
VarCorr
VarTGV
VarGSD
SpatialGSD
Points
SpatialTGV SpatialCorr Variable
Scale
WPBench
GEFCom
State Grid
OpenWPF
Fig. 4. Dataset-characteristic coverage of WPBench and representative wind
forecasting resources. The radar chart compares normalized coverage profiles
across temporal patterns, variable dependencies, spatial dependencies, and
data scale. Solid contours denote group-wise maximum values, while dashed
contours denote group-wise minimum values.
training split, while testing follows a non-overlapping rolling
protocol where each test window advances byHsteps. All
models are compared on the same splits, dataset-horizon units,
and rolling windows. For fair comparison, key hyperparame-
ters of trainable models are tuned on the validation split using
Optuna [103], and the best validation configuration is fixed for
test evaluation. The experiments are implemented in PyTorch

TABLE II
STATISTICS OFWPBENCH DATASETS.
Dataset Frequency LengthN CSplit
Single-turbine univariate datasets
Wind Farm A [72] 10mins 72,158 1 1 7:1:2
Wind Farm B [72] 10mins 22,615 1 1 7:1:2
Chalmers [73] 1min 142,761 1 1 7:1:2
Maelstrom 1 [74] 10mins 239,028 1 1 7:1:2
Maelstrom 2 [74] 10mins 239,019 1 1 7:1:2
Maelstrom 3 [74] 10mins 239,028 1 1 7:1:2
Maelstrom 4 [74] 10mins 239,028 1 1 7:1:2
Single-turbine multivariate datasets
Yalova [75] 10mins 52,560 1 4 7:1:2
Wind Farm Site 1 [76] 15mins 70,176 1 12 7:1:2
Wind Farm Site 2 [76] 15mins 70,176 1 11 7:1:2
Wind Farm Site 3 [76] 15mins 70,176 1 12 7:1:2
Wind Farm Site 4 [76] 15mins 70,176 1 12 7:1:2
Wind Farm Site 6 [76] 15mins 70,176 1 12 7:1:2
Kaggle1 [77] 10mins 15,984 1 19 7:1:2
SCADA Fault [78] 10mins 47,427 1 64 7:1:2
Multi-turbine univariate datasets
Wind Farm C [72] 10mins 10,007 21 1 7:1:2
AEMO [79] 5mins 210,479 22 1 7:1:2
COSMO [80] 1hour 26,304 38 1 7:1:2
ECMWF [80] 1hour 26,304 38 1 7:1:2
Multi-turbine multivariate datasets
GEFCom2012 [15] 1hour 26,244 7 5 7:1:2
GEFCom2014 [16] 1hour 17,538 10 5 7:1:2
Kelmarsh [81] 10mins 197,977 6 3 7:1:2
Penmanshiel [82] 10mins 245,232 14 3 7:1:2
SDWPF [14] 10mins 35,280 134 10 7:1:2
UEPS [83] 10mins 52,560 20 3 7:1:2
UEBB [83] 10mins 52,560 32 3 7:1:2
2.6.0+cu124 [104] with Python 3.11 and run on NVIDIA A800
80GB GPUs.
Evaluation Metrics.WPBench evaluates numerical accuracy
and forecast-curve fidelity. We use six error metrics, including
MAE, MSE, nMAE, nMSE, nRMSE, and nMBE, together
with four shape-aware metrics, including DTW, nDTW, nD-
DTW, and EDF. For one testing window, lete i,k =F i,k −Y i,k
and˜ei,k =e i,k/Ci, whereY i,k andF i,k are the ground-truth
and forecast target values of turbine or siteiat horizon step
k, andC i is the rated capacity or a capacity-like normalizer
of the corresponding target when available; otherwise, it is
approximated by the maximum target value in the training
split. The error metrics are defined as follows:
MAE= 1 N H
NX
i=1
HX
k=1
|ei,k|,MSE= 1 N H
NX
i=1
HX
k=1
e2 i,k,
nMAE= 1 N H
NX
i=1
HX
k=1
|˜ei,k|,nMSE= 1 N H
NX
i=1
HX
k=1
˜e2 i,k,
nRMSE=
√
nMSE,nMBE= 1 N H
NX
i=1
HX
k=1
˜ei,k.
For forecast-curve fidelity, we show the core DTW alignment
cost and the EDF definition:
DTW(Yi, Fi) = min πi
X
(p,q)∈πi
d(Yi,p, Fi,q),
EDF= nRMSE nMAE ,
whereNis the number of turbines or site-level target series,H
is the forecasting horizon,Y i andF i denote the corresponding
ground-truth and forecast target curves of turbine or site
i,π i is a warping path,(p, q)denotes an aligned pair of
horizon indices betweenY i andF i alongπ i, andd(·,·)is
the point-wise distance. Dataset-level DTW is computed by
averagingDTW(Y i, Fi)overi. The normalized DTW, nDTW,
is computed by replacingY i andF i with capacity-normalized
curves ¯Yi =Y i/Ci and ¯Fi =F i/Ci, while nDDTW applies
DTW to the first-order change sequences∆ ¯Yi and∆ ¯Fi. EDF
characterizes the dispersion pattern of forecasting errors: a
larger EDF indicates that large deviations contribute more
strongly to the overall error, while an EDF closer to 1
indicates a more uniform error distribution. For single-turbine
datasets,N= 1. In the main experiments, nMAE/nRMSE and
nDTW/nDDTW are used as the primary accuracy and shape-
aware metrics, respectively.
V. EXPERIMENTS
Rather than treating WPBench as a static leaderboard, our
experiments use it as a diagnostic instrument to study how
model families respond to wind-specific temporal patterns,
target-covariate dependencies, and turbine-level spatial struc-
tures. We first report overall performance across the four wind
data structures, and then use the characterization metrics de-
fined in the preliminaries to analyze when different modeling
assumptions hold or fail.
A. Overall Results under Scope-aware Ranking
WPBench covers four forecasting settings: single-turbine
univariate (1T1V), single-turbine multivariate (1TMV), multi-
turbine univariate (MT1V), and multi-turbine multivariate
(MTMV). Because model families differ in structural applica-
bility, we report detailed nMAE results separately for single-
turbine and multi-turbine datasets. Tables III and IV show the
nMAE results for these two groups; models such as V AR have
missing entries where the corresponding data structure is not
applicable. Each dataset is reported with two horizon groups:
Short averages horizons 12 and 24, while Long averages
horizons 72 and 144.
For cross-dataset comparison, we further use a GIFT-style
normalized evaluation. Each model score is divided by the Sea-
sonalNaive score on the same structure–dataset–horizon unit,
then aggregated by a geometric mean within each structure and
by a structure-balanced summary across applicable structures.
Figure 5 summarizes two representative normalized leader-
boards, using nMAE for numerical accuracy and nDTW for
forecast-curve fidelity. Under nMAE, foundation models such
as TOTO, FactoST-UTP, and TTM achieve the best normal-
ized scores. Under nDTW, TOTO and FactoST-UTP remain

TABLE III
NMAEDETAILED RESULTS ON SINGLE-TURBINE DATASETS.
Type Dataset Horizon DLinear XLinear DUET Patch iTrans xPatch LR V AR Timer TTM TOTO SEMPO STID TGGC BigST FUTP
nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE
1T1V
Wind Farm A Short 0.096 0.095 0.100 0.107 0.104 0.089 0.096 – 0.101 0.0910.0810.100 0.102 0.110 0.107 0.082 Long 0.179 0.1680.167 0.183 0.178 0.171 0.179 – 0.212 0.1730.1670.188 0.185 0.195 0.214 0.170
Wind Farm B Short 0.098 0.106 0.105 0.130 0.124 0.110 0.095 – 0.108 0.1000.093 0.112 0.116 0.114 0.137 0.093 Long 0.170 0.173 0.179 0.186 0.190 0.206 0.165– 0.224 0.184 0.178 0.186 0.173 0.182 0.226 0.170
Chalmers Short 0.003 0.002 0.001 0.003 0.004 0.001 0.004 – 0.002 0.0010.001 0.002 0.005 0.006 0.722 0.001 Long 0.011 0.004 0.0040.0040.0040.004 0.014 – 0.005 0.008 0.005 0.004 0.013 0.008 0.568 0.005
Maelstrom 1 Short 0.069 0.068 0.072 0.086 0.076 0.069 0.069 – 0.071 0.0750.067 0.072 0.072 0.070 0.072 0.065 Long 0.117 0.1140.111 0.120 0.117 0.120 0.118 – 0.133 0.1150.1100.125 0.118 0.124 0.121 0.117
Maelstrom 2 Short 0.060 0.059 0.060 0.071 0.065 0.058 0.060 – 0.059 0.0610.057 0.060 0.059 0.060 0.061 0.056 Long 0.093 0.0880.0860.095 0.090 0.092 0.094 – 0.099 0.0890.087 0.095 0.094 0.094 0.098 0.093
Maelstrom 3 Short 0.078 0.076 0.080 0.085 0.084 0.076 0.077 – 0.076 0.0780.075 0.080 0.077 0.079 0.079 0.074 Long 0.123 0.1210.119 0.130 0.130 0.122 0.123 – 0.138 0.1230.1180.131 0.125 0.127 0.127 0.127
Maelstrom 4 Short 0.0760.074 0.078 0.081 0.081 0.075 0.076 – 0.076 0.078 0.074 0.078 0.079 0.077 0.078 0.072 Long 0.126 0.1230.122 0.134 0.129 0.126 0.128 – 0.144 0.1230.1210.136 0.127 0.133 0.135 0.132
1TMV
Wind Farm Site 1 Short 0.096 0.096 0.129 0.109 0.117 0.098 0.096 0.095 0.103 0.0990.092 0.106 0.101 0.108 0.118 0.090 Long 0.172 0.170 0.182 0.186 0.191 0.187 0.1670.167 0.201 0.1730.167 0.185 0.174 0.175 0.188 0.191
Wind Farm Site 2 Short 0.108 0.107 0.160 0.128 0.126 0.109 0.105 0.104 0.112 0.1070.095 0.116 0.120 0.115 0.136 0.094 Long 0.209 0.212 0.233 0.220 0.222 0.218 0.1980.209 0.245 0.2130.203 0.220 0.214 0.214 0.235 0.237
Wind Farm Site 3 Short 0.067 0.066 0.098 0.083 0.078 0.067 0.069 0.068 0.064 0.0640.061 0.070 0.075 0.073 0.104 0.059 Long 0.133 0.125 0.125 0.131 0.129 0.126 0.143 0.133 0.137 0.1280.1180.136 0.138 0.139 0.173 0.118
Wind Farm Site 4 Short 0.073 0.076 0.124 0.102 0.102 0.074 0.079 0.074 0.079 0.0730.0680.089 0.083 0.081 0.102 0.068 Long 0.185 0.185 0.211 0.216 0.202 0.198 0.1890.181 0.247 0.1820.1720.207 0.195 0.191 0.240 0.190
Wind Farm Site 6 Short 0.062 0.059 0.095 0.070 0.071 0.059 0.096 0.057 0.059 0.0570.0530.061 0.064 0.072 0.176 0.056 Long 0.1450.1070.125 0.140 0.139 0.136 0.201 0.127 0.154 0.1350.110 0.135 0.169 0.153 0.278 0.160
Kaggle1 Short 0.109 0.116 0.136 0.133 0.137 0.118 0.123 0.119 0.120 0.1090.1080.122 0.118 0.126 0.135 0.113 Long 0.1520.160 0.178 0.174 0.183 0.177 0.167 0.157 0.2120.152 0.155 0.171 0.161 0.166 0.165 0.168
SCADA Fault Short 0.121 0.124 0.148 0.139 0.150 0.125 0.141 0.125 0.128 0.1200.114 0.129 0.129 0.130 0.191 0.113 Long 0.211 0.218 0.251 0.231 0.249 0.230 0.230 0.219 0.250 0.2140.1970.234 0.215 0.226 0.503 0.241
Yalova Short 0.107 0.111 0.140 0.133 0.143 0.111 0.105 0.104 0.116 0.1050.0960.123 0.119 0.116 0.145 0.102 Long 0.221 0.229 0.244 0.237 0.257 0.226 0.213 0.216 0.257 0.2170.2070.251 0.226 0.226 0.262 0.222
1T1V/1TMV-only nMAE results. Short averages horizons 12 and 24; Long averages horizons 72 and 144. Red bold entries denote the best results, and blue
italic underlined entries denote the second-best results in each dataset–horizon-group row; “–” indicates unavailable results.
0.0 0.5 1.0
TOTO
FUTP
TTM
xPatch
XLinear
STDN
DLinear
OpenC
SEMPO
DUET
(a)
normalized nMAE
0.533 avgR=3.431
0.539 avgR=4.369
0.564 avgR=6.291
0.564 avgR=6.990
0.566 avgR=6.059
0.575 avgR=6.741
0.587 avgR=7.334
0.601 avgR=6.915
0.601 avgR=11.194
0.602 avgR=9.123
0.0 0.5 1.0
DLinear
XLinear
TTM
STID
TGGC
FUTP
xPatch
TOTO
SEMPO
Patch
(b)
normalized nRMSE
0.562 avgR=3.400
0.570 avgR=5.954
0.571 avgR=5.984
0.577 avgR=6.302
0.590 avgR=9.139
0.591 avgR=8.497
0.593 avgR=10.816
0.594 avgR=11.253
0.595 avgR=10.578
0.596 avgR=9.660
0.0 0.5 1.0
TOTO
FUTP
STDN
xPatch
OpenC
XLinear
TTM
SEMPO
DLinear
STID
(c)
normalized nDTW
0.517 avgR=1.605
0.562 avgR=3.573
0.588 avgR=5.326
0.590 avgR=6.408
0.599 avgR=5.701
0.603 avgR=6.890
0.608 avgR=8.000
0.621 avgR=9.372
0.622 avgR=7.795
0.649 avgR=9.554
0.0 0.5 1.0
FUTP
STDN
OpenC
xPatch
FSTA
TTM
DUET
Timer
iTrans
SEMPO
(d)
normalized nDDTW
0.753 avgR=4.736
0.753 avgR=4.071
0.759 avgR=4.786
0.771 avgR=6.295
0.776 avgR=10.268
0.785 avgR=7.665
0.786 avgR=8.962
0.789 avgR=5.824
0.790 avgR=10.207
0.796 avgR=8.536
Geometric mean relative to SeasonalNaive
Deep Temporal Stat/ML TSFM Deep ST STFM Top-1
Fig. 5. Normalized leaderboard under SeasonalNaive-based scaling. Bars show structure-balanced geometric means relative to SeasonalNaive, and avgR labels
report scope-aware average ranks.
highly competitive, while larger and more structurally complex
spatio-temporal models such as STDN and OpenCity also
move into the leading group. Meanwhile, several linear/MLP-
style temporal models that perform strongly under point-wise
errors, such as DLinear and TTM, show some degree of rank
degradation under forecast-curve fidelity evaluation.
The remaining normalized metrics further support this ob-
servation. For numerical error metrics, nRMSE tends to favor
linear/MLP-style temporal models such as DLinear, XLinear,
and TTM, possibly because these models produce smoother
forecasts and suppress large prediction deviations, as nRMSE
is more sensitive to extreme errors. Overall, the best model
under numerical accuracy is not necessarily the best model
under forecast-curve fidelity. WPBench therefore reports these
two perspectives separately rather than merging them into a
single score.
B. Structure-aware Diagnostic Analysis
To further understand how dataset characteristics affect fore-
casting behavior, we analyze model responses using the char-
acterization metrics defined in Section III-B, covering tempo-
ral patterns, variable dependencies, and spatial dependencies.
For each metric, datasets are ranked by the corresponding
metric value, and LowQ and HighQ groups are formed from
the bottom and top 20%, respectively. To reduce the influence
of individual horizons and outlier datasets, we report shifted-
geometric-mean nMAE aggregated over the selected dataset–
horizon units.
Figure 6 first shows that temporal characteristics affect most
model families in a similar direction. Strong seasonality gen-
erally corresponds to lower forecasting error, suggesting that
periodic wind-power patterns provide exploitable regularity.
In contrast, metrics related to distributional shift and temporal

TABLE IV
NMAEDETAILED RESULTS ON MULTI-TURBINE DATASETS.
Type Dataset Horizon DLinear XLinear DUET Patch iTrans xPatch LR V AR Timer TTM TOTO SEMPO STID TGGC BigST STDN FUTP OpenC FSTA
nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE nMAE
MT1V
Wind Farm C Short 0.105 0.110 0.112 0.140 0.126 0.108 0.105 – 0.114 0.1010.097 0.118 0.116 0.138 0.188 0.102 0.095 0.106 0.123 Long 0.198 0.193 0.192 0.225 0.237 0.206 0.196 – 0.232 0.1910.191 0.213 0.204 0.224 0.234 0.222 0.199 0.1870.262
ECMWF Short 0.074 0.073 0.069 0.076 0.080 0.070 0.074 – 0.075 0.073 0.067 0.075 0.074 0.079 0.0800.065 0.064 0.073 0.078 Long 0.104 0.099 0.093 0.103 0.107 0.098 0.106 – 0.107 0.1000.093 0.104 0.106 0.108 0.114 0.104 0.092 0.096 0.111
COSMO Short 0.088 0.086 0.082 0.090 0.093 0.082 0.087 – 0.085 0.087 0.079 0.088 0.088 0.089 0.0920.077 0.077 0.085 0.091 Long 0.119 0.114 0.105 0.118 0.120 0.109 0.120 – 0.125 0.1160.105 0.119 0.120 0.125 0.127 0.118 0.104 0.109 0.126
AEMO Short 0.079 0.078 0.097 0.088 0.082 0.075 0.079 – 0.079 0.080 0.076 0.080 0.077 0.079 0.0770.072 0.074 0.078 0.079 Long 0.175 0.175 0.180 0.183 0.177 0.171 0.176 – 0.196 0.172 0.174 0.204 0.171 0.167 0.1690.166 0.166 0.169 0.197
MTMV
GEFCom2012 Short 0.208 0.211 0.220 0.222 0.217 0.210 0.1950.193 0.208 0.207 0.204 0.211 0.217 0.217 0.2230.195 0.199 0.209 0.218 Long 0.266 0.2690.263 0.268 0.275 0.274 0.2640.260 0.279 0.268 0.269 0.275 0.268 0.266 0.277 0.299 0.276 0.275 0.291
GEFCom2014 Short 0.208 0.207 0.270 0.221 0.223 0.208 0.1940.192 0.206 0.208 0.196 0.211 0.212 0.232 0.2260.193 0.196 0.211 0.210 Long 0.263 0.269 0.274 0.269 0.275 0.272 0.2540.256 0.278 0.264 0.271 0.271 0.262 0.274 0.278 0.282 0.269 0.268 0.285
Kelmarsh Short 0.092 0.091 0.100 0.100 0.098 0.090 0.093 0.093 0.091 0.093 0.088 0.094 0.093 0.096 0.0990.088 0.086 0.092 0.093 Long 0.175 0.165 0.168 0.174 0.172 0.166 0.174 0.176 0.1840.163 0.1570.191 0.171 0.173 0.179 0.166 0.170 0.165 0.193
Penmanshiel Short 0.099 0.097 0.103 0.101 0.104 0.094 0.097 0.097 0.098 0.098 0.092 0.103 0.103 0.104 0.1020.091 0.091 0.096 0.103 Long 0.189 0.182 0.177 0.199 0.190 0.183 0.185 0.184 0.218 0.1810.1700.202 0.188 0.189 0.1920.171 0.187 0.174 0.209
SDWPF Short 0.095 0.092 0.098 0.106 0.118 0.088 0.145 0.091 0.093 0.0850.0760.108 0.105 0.110 0.1400.076 0.079 0.087 0.105 Long 0.181 0.176 0.178 0.191 0.197 0.169 0.267 0.163 0.1890.161 0.1490.180 0.197 0.197 0.197 0.189 0.176 0.172 0.208
UEPS Short 0.083 0.085 0.091 0.086 0.093 0.087 0.087 0.086 0.087 0.0850.083 0.089 0.088 0.095 0.105 0.093 0.080 0.470 0.088 Long 0.132 0.132 0.135 0.136 0.138 0.142 0.139 0.158 0.151 0.133 0.141 0.137 0.1310.144 0.145 0.151 0.135 0.135 0.151
UEBB Short 0.107 0.107 0.107 0.109 0.113 0.108 0.117 0.114 0.110 0.109 0.110 0.109 0.107 0.112 0.1120.105 0.103 0.110 0.110 Long 0.141 0.1410.144 0.147 0.147 0.150 0.163 0.199 0.159 0.148 0.154 0.148 0.145 0.150 0.149 0.168 0.142 0.148 0.155
MT1V/MTMV-only nMAE results including multi-turbine-only models. Short averages horizons 12 and 24; Long averages horizons 72 and 144. Red bold
entries denote the best results, and blue italic underlined entries denote the second-best results in each dataset–horizon-group row; “–” indicates unavailable
results.
0.105 0.12 0.135
TOTO
TTM
XLinear
DLinear
LR
STID
TGGC
Seasonality
0.105 0.12 0.135 0.15
TOTO
TTM
XLinear
DLinear
LR
STID
TGGC
Shifting
0.04 0.08 0.12 0.16
TOTO
TTM
XLinear
DLinear
LR
STID
TGGC
Short-term JSD
0.04 0.08 0.12 0.16
TOTO
TTM
XLinear
DLinear
LR
STID
TGGC
Long-term JSD
0.12 0.135 0.15 0.165
TOTO
TTM
XLinear
DLinear
LR
STID
TGGC
VarCorr
0.12 0.15 0.18 0.21
TOTO
TTM
XLinear
DLinear
LR
STID
TGGC
Var-GSD
0.105 0.12 0.135 0.15
TTM
XLinear
FUTP
STDN
STID
FSTA
OpenC
BigST
SpatialCorr
0.105 0.12 0.135 0.15
TTM
XLinear
FUTP
STDN
STID
FSTA
OpenC
BigST
Spatial-TGV
Fig. 6. Extreme dataset-characteristic w.r.t representative models. Blue and red markers denote shifted-geometric-mean nMAE on LowQ and HighQ datasets,
respectively. The distance between markers indicates the model’s response difference to the corresponding dataset characteristic. Lower nMAE is better. LowQ
and HighQ are formed by the bottom and top 20% datasets ranked by each characterization metric.
divergence tend to increase error, indicating that non-stationary
temporal patterns remain a major difficulty for wind-power
forecasting. This contrast suggests that temporal regularity
and temporal drift should be treated separately: periodicity
is useful, while changing operating regimes or distributional
divergence can weaken model robustness.
We next examine variable-dependency patterns. High Var-
Corr can reduce forecasting error for several representative
models, showing that stable target–covariate relationships pro-
vide useful predictive information. However, when variable
relationships become more dynamic, as reflected by Var-GSD,
the benefit becomes less stable. This indicates that multivariate
information is helpful only when the dependency pattern is
sufficiently consistent; otherwise, models may capture tran-
sient or noisy correlations.
Figure 7 further compares representative channel-
independent and channel-dependent model pairs. Under
stronger or more dynamic variable relationships, some
channel-dependent models outperform their structurally
similar channel-independent counterparts, indicating that
explicit channel-dependency modeling can help exploit
information from relationships between the target and
covariates. However, this advantage is not universal:
although iTransformer performs competitively under VarCorr,
it weakens under Var-TGV and Var-GSD and can be
outperformed by PatchTST. This suggests that variable

0.20 0.00 0.20
DLinear XLinear
PatchTST iTrans
Timer TOTO
TTM TOTO
VarCorr
0.20 0.00 0.20
DLinear XLinear
PatchTST iTrans
Timer TOTO
TTM TOTO
Var-TGV
0.20 0.00 0.20
DLinear XLinear
PatchTST iTrans
Timer TOTO
TTM TOTO
Var-GSD
LowQ HighQ lower raw nMAE
Fig. 7. Paired CI/CD model comparison w.r.t. variable-dependency conditions.
Each panel corresponds to one variable-dependency descriptor, and each row
compares a matched channel-independent (CI) and channel-dependent (CD)
model pair. Bars extending left and right report the nMAE of the CI and CD
models, respectively, under LowQ and HighQ groups; red triangles mark the
lower-error side.
UEPS Kelmarsh COSMO Wind Farm C
0.10
0.15raw nMAE (SGM)
Weak Strong
Spatial-TGV: Weak →  Strong
UEPS GEFCom2014 COSMO Wind Farm C
0.1
0.2raw nMAE (SGM)
Weak Strong
Spatial-GSD: Weak →  Strong
Deep temporal Foundation temporal ST STFM
Fig. 8. Dataset-level spatial w.r.t model group. Bars report shifted-geometric-
mean nMAE for temporal, foundation temporal, deep spatio-temporal, and
spatio-temporal foundation model groups on weak and strong spatial-dynamic
datasets. Red triangles mark the best group on each dataset.
dependency is useful, but current channel-dependent designs
still need stronger dynamic relation modeling to exploit it
reliably.
Finally, we analyze spatial dependency characteristics. Un-
like temporal periodicity, spatial characteristics do not lead to
a simple monotonic conclusion. SpatialCorr measures static
cross-turbine correlation, whereas Spatial-TGV reflects how
spatial relations change over time. As shown in Figure 6,
higher spatial dependency does not consistently correspond
to lower forecasting error. Instead, it may also reveal model
sensitivity to unstable or mismatched spatial assumptions.
Figure 6 and Figure 8 show that spatially aware models are
often more sensitive to changes in spatial dependency patterns.
Models such as OpenCity, FactoST-STA, STDN, and BigST
react more strongly to spatial descriptors than purely temporal
references, but their responses are not uniform. One possible
explanation is that spatial relations in wind farms are less
stable than the road-network structures commonly assumed
in traffic forecasting. These relations can vary with wind
conditions, terrain, wake effects, and turbine operating states.
As a result, spatial modeling can help when its assumptions
match the data, but it may also amplify errors when the learned
spatial prior is unstable or mismatched.
Overall, these diagnostics show that WPBench contains
diverse dataset characteristics rather than a single homoge-
neous forecasting setting. Temporal periodicity is generally
beneficial, variable dependency is useful but requires robust
dynamic modeling, and spatial dependency introduces addi-
tional sensitivity rather than guaranteed gains. This explains
why the overall leaderboard does not simply favor spatially
2 4 6 8 10 12 14
Dataset-level error avg rank
2
4
6
8
10
12
14Dataset-level shape avg rank
Model
Top error-aware
Top shape-aware
Task type
1T1V
1TMV
MT1V
MTMV
Top error-aware (DLinear): N=26, r=0.64
Top shape-aware (FactoST-UTP): N=26, r=0.41
Fig. 9. Dataset-level comparison between Error Rank and Shape Rank for
representative models. Error Rank averages ranks over nMAE and nRMSE,
and Shape Rank averages ranks over nDTW and nDDTW. Shaded regions
summarize the rank distributions of the top-ranked models under numerical
accuracy and forecast-curve fidelity.
complex models: models that ignore unstable spatial relations
can sometimes be more robust, while spatial models require
better adaptation to wind-specific dependency dynamics.
C. Numerical Accuracy vs. Forecast-Curve Fidelity
We further examine whether numerical accuracy and
forecast-curve fidelity lead to consistent model conclusions.
Figure 9 compares the dataset-level Error Rank and Shape
Rank of the top-ranked models under these two evaluation
views. The two representatives show clearly different rank
distributions: the top-ranked model under numerical accuracy
usually maintains stronger numerical accuracy, but its Shape
Rank can degrade; the top-ranked model under forecast-curve
fidelity better preserves curve similarity, but its Error Rank
varies more substantially. This suggests that current models
often favor one evaluation objective and struggle to simulta-
neously achieve both numerical accuracy and forecast-curve
fidelity.
Figure 10 further shows a representative forecast segment
on GEFCom2012. DLinear is closer to the average level of
the true power curve and therefore obtains lower nMAE,
but its forecasts are overly smooth and tend to miss local
ramps, short-term fluctuations, and peak and trough variations.
FactoST-UTP better follows the temporal shape of the true
sequence in some segments and thus obtains lower nDTW;
however, it can still exhibit temporal lag, excessive fluctuation,
or amplitude offset, which increases point-wise error.
These results show that lower numerical error does not nec-
essarily imply better forecast-curve fidelity. WPBench there-
fore reports Error Rank and Shape Rank as complementary
views rather than merging them into a single overall ranking.

0 25 50 75 100 125 150 175
0.0
0.5
1.0Power
(a) Similar nMAE, different shape fidelity
nMAE  DLinear 0.190  vs.  FactoST-UTP 0.203
nDTW  DLinear 2.541  vs.  FactoST-UTP 2.172
0 25 50 75 100 125 150 175
Concatenated forecast step
0
50
100
150
200Power
(b) Lower nMAE, weaker shape fidelity
nMAE  DLinear 0.135  vs.  FactoST-UTP 0.149
nDTW  DLinear 1.983  vs.  FactoST-UTP 1.955
Ground truth DLinear FactoST-UTP GT mean
Fig. 10. Forecast-curve case study on GEFCom2012.
0 5 10 15 20 25 30 35 40 45
Mean improvement over zero-shot (%)
TOTO (TSFM)
TTM (TSFM)
FactoST-STA (STFM)
OpenCity (STFM)
Timer (TSFM)
FactoST-UTP (STFM)
SEMPO (TSFM)
1.8
2.0
2.0
1.4
29.0
23.8
32.2
25.7
35.9
33.9
38.5
36.2
38.7
37.5
Few-shot
Full-shot
Fig. 11. Model-level foundation adaptation summary. Bars show the relative
nMAE reduction of few-shot and full-shot adaptation over zero-shot perfor-
mance, averaged over each model’s applicable wind data structures.
D. Foundation Model Adaptation
We compare temporal and spatio-temporal foundation mod-
els under zero-shot, few-shot (10% uniformly sampled training
data), and full-shot settings. Figure 11 reports the relative
nMAE reduction of each model after adaptation, using its zero-
shot performance as the reference.
Figure 11 shows that adaptation gains are largest for models
with ample zero-shot calibration room (SEMPO, FactoST-
UTP, Timer), while TTM and TOTO improve little, likely due
to strong zero-shot baselines. Notably, many models achieve
few-shot gains comparable to or slightly above full-shot,
suggesting that a small representative subset can capture key
wind-farm patterns, whereas full-shot introduces more low-
wind, volatile, curtailed, or abnormal segments. Adaptation
thus depends on sample representativeness, regularization, and
validation, not just data volume.
Beyond data volume, FactoST-UTP outperforms STA, sug-
gesting that stronger cross-turbine aggregation does not nec-
2.3
0.270
0.265
0.260
0.255
0.250
0.245
0.240
0.235
NRMSE
Inference time (ms)
(a)
Timer
SEMPO
iTrans
DLinear
Xlinear
DUET
BigST TGGC
xPatch
STID
F-UTP
F-STA
TTM
PatchTST OpenCity
STDN
Toto
2.2
2.1
2.0
1.9
1.8
0.4 0.5 0.6 0.8 1 2 5 20 100 300
(b)
NDTW
Inference time (ms)
Timer
SEMPO
iTrans
BigST
TGGC
STID
xPatch
DLinear
Xlinear
DUET
F-STA
TTM
F-UTP
PatchTST
OpenCity
STDN Toto
Model parameters
10M1M >100M
Deep temporal models
Spatio-temporal models
TS foundation models
ST foundation models
0.275
Fig. 12. Efficiency–accuracy on GEFCom2012 with horizon 12. Bubble size
denotes the number of model parameters. Panel (a) compares inference time
with nRMSE, while Panel (b) compares inference time with nDTW.
essarily improve adaptation. Given the complex and non-
stationary spatio-temporal dependencies in wind farms, joint
channel modeling may overfit unstable spatial relations,
whereas channel-independent adaptation can be more robust.
E. Model Efficiency
Figure 12 compares the efficiency–accuracy trade-off from
the perspectives of numerical accuracy and forecast-curve fi-
delity. In Figure 12(a), lightweight linear or MLP-style models
such as DLinear, XLinear, STID, and TTM achieve low in-
ference cost with competitive nRMSE, suggesting that simple
architectures can already provide stable numerical forecasts.
This is consistent with Sec. V-C, where DLinear tends to
produce smoother predictions and thus more stable numerical
errors. In Figure 12(b), however, larger or more complex
models such as STDN and TOTO show stronger forecast-
curve fidelity under nDTW, indicating that models with larger
capacity, especially spatio-temporal and time-series foundation
models, are more capable of preserving temporal dynamics
and curve shape. Notably, TOTO achieves strong shape-aware
performance but incurs much higher inference latency, which
may be partly related to its probabilistic forecasting interface
that produces quantile outputs or sample-based outputs before
deriving point forecasts for evaluation. Under rolling eval-
uation, this additional inference cost becomes more visible
because forecasts must be repeatedly generated for many test
windows. Such latency can be less suitable for scenarios with

strict real-time requirements, such as frequent rolling updates,
online dispatch, or large-scale turbine monitoring. In contrast,
faster models may be more suitable for deployment when a
small sacrifice in curve fidelity leads to substantial savings
in response time. Overall, the figure highlights a trade-off
between efficient numerical prediction and stronger forecast-
curve modeling at a higher computational cost.
VI. CONCLUSIONS
This paper presents WPBench, a comprehensive bench-
mark for wind power forecasting across diverse wind data
structures. WPBench evaluates a broad range of forecasting
models, including statistical baselines, deep temporal mod-
els, spatio-temporal models, time-series foundation models,
and spatio-temporal foundation models, under unified pro-
tocols. Beyond conventional point-wise accuracy, WPBench
incorporates shape-aware metrics for forecast-curve fidelity,
evaluates computational efficiency, and provides structure-
aware diagnostics from temporal, variable-dependency, and
spatial-dependency perspectives. Through diagnostic analy-
sis, we show that model performance is strongly affected
by wind data organization, variable dependency, and spatial
structure. Overall, WPBench provides a reproducible eval-
uation framework for understanding the strengths and lim-
itations of existing forecasting models and offers guidance for
developing more robust wind-specific forecasting methods.
REFERENCES
[1] J. Cuesta, U. Leturiondo, Y . Vidal, and F. Pozo, “A review of prog-
nostics and health management techniques in wind energy,”Reliability
Engineering & System Safety, vol. 260, p. 111004, 2025.
[2] D. Zhu, X. Huang, Z. Ding, and W. Zhang, “Estimation of wind
turbine responses with attention-based neural network incorporating
environmental uncertainties,”Reliability Engineering & System Safety,
vol. 241, p. 109616, 2024.
[3] X. Wang, H. Jia, X. Jin, Y . Mu, W. Wei, X. Yu, and S. Liang, “Bi-level
optimal operations for grid operator and low-carbon building prosumers
with peer-to-peer energy sharing,”Applied Energy, vol. 359, p. 122723,
2024.
[4] Y . Jia, C. Wan, W. Cui, Y . Song, and P. Ju, “Peer-to-peer energy
trading using prediction intervals of renewable energy generation,”
IEEE Transactions on Smart Grid, vol. 14, no. 2, pp. 1454–1465, 2022.
[5] F. Ying, L. Huang, Y . Liu, L. Liu, and Y . Fu, “Condition-based oppor-
tunistic maintenance strategy for offshore wind farmbased on accurate
condition assessment results,”Reliability Engineering & System Safety,
p. 112107, 2025.
[6] T. Jain and K. Verma, “Reliability based computational model for
stochastic unit commitment of a bulk power system integrated with
volatile wind power,”Reliability Engineering & System Safety, vol.
244, p. 109949, 2024.
[7] C. Kan, Y . Devrim, and S. Eryilmaz, “On the theoretical distribution of
the wind farm power when there is a correlation between wind speed
and wind turbine availability,”Reliability Engineering & System Safety,
vol. 203, p. 107115, 2020.
[8] D. Fan, M. Liu, Y . Shao, L. Yang, Y . Liu, Y . Zhang, Y . Ren,
and Z. Wang, “Domain-specific large language model for mainte-
nance decision-making on wind farms by labeled-data-supervised fine-
tuning,”Engineering, 2025.
[9] Z. Shao, F. Wang, Y . Xu, W. Wei, C. Yu, Z. Zhang, D. Yao, T. Sun,
G. Jin, X. Caoet al., “Exploring progress in multivariate time series
forecasting: Comprehensive benchmarking and heterogeneity analysis,”
IEEE Transactions on Knowledge and Data Engineering, vol. 37, no. 1,
pp. 291–305, 2024.
[10] X. Qiu, Z. Li, W. Qiu, S. Hu, L. Zhou, X. Wu, Z. Li, C. Guo,
A. Zhou, Z. Sheng, J. Hu, C. S. Jensen, and B. Yang, “TAB: Unified
benchmarking of time series anomaly detection methods,” inProc.
VLDB Endow., 2025, pp. 2775–2789.
[11] X. Qiu, J. Hu, L. Zhou, X. Wu, J. Du, B. Zhang, C. Guo, A. Zhou,
C. S. Jensen, Z. Sheng, and B. Yang, “TFB: Towards comprehensive
and fair benchmarking of time series forecasting methods,” inProc.
VLDB Endow., 2024, pp. 2363–2377.
[12] O. Shchur, A. F. Ansari, C. Turkmen, L. Stella, N. Erickson, P. Guerron,
M. Bohlke-Schneider, and Y . Wang, “fev-bench: A realistic benchmark
for time series forecasting,”arXiv preprint arXiv:2509.26468, 2025.
[13] T. Aksu, G. Woo, J. Liu, X. Liu, C. Liu, S. Savarese, C. Xiong, and
D. Sahoo, “Gift-eval: A benchmark for general time series forecasting
model evaluation,”arXiv preprint arXiv:2410.10393, 2024.
[14] J. Zhou, X. Lu, Y . Xiao, J. Tang, J. Su, Y . Li, J. Liu, J. Lyu, Y . Ma, and
D. Dou, “Sdwpf: A dataset for spatial dynamic wind power forecasting
over a large turbine array,”Scientific Data, vol. 11, no. 1, p. 649, 2024.
[15] T. Hong, P. Pinson, and S. Fan, “Global energy forecasting competition
2012,” pp. 357–363, 2014.
[16] T. Hong, P. Pinson, S. Fan, H. Zareipour, A. Troccoli, and R. J.
Hyndman, “Probabilistic energy forecasting: Global energy forecasting
competition 2014 and beyond,” pp. 896–913, 2016.
[17] X. Xu, Q. Cao, R. Deng, Z. Guo, Y . Chen, and J. Yan, “A cross-
dataset benchmark for neural network-based wind power forecasting,”
Renewable Energy, vol. 254, p. 123463, 2025.
[18] K. Szostek, D. Mazur, G. Drałus, and J. Kusznier, “Analysis of
the effectiveness of arima, sarima, and svr models in time series
forecasting: A case study of wind farm energy production,”Energies,
vol. 17, no. 19, p. 4803, 2024.
[19] J. Shi, J. Teh, and C.-M. Lai, “Wind power prediction based on im-
proved self-attention mechanism combined with bi-directional temporal
convolutional network,”Energy, vol. 322, p. 135666, 2025.
[20] W. Fan, Y . Fu, S. Zheng, J. Bian, Y . Zhou, and H. Xiong, “Dewp: Deep
expansion learning for wind power forecasting,”ACM Transactions on
Knowledge Discovery from Data, vol. 18, no. 3, pp. 1–21, 2024.
[21] S. Daenens, T. Verstraeten, P.-J. Daems, A. Now ´e, and J. Helsen,
“Spatio-temporal graph neural networks for power prediction in off-
shore wind farms using scada data,”Wind Energy Science, vol. 10,
no. 6, pp. 1137–1152, 2025.
[22] L. Yang, F. Tsung, K. Wang, and J. Zhou, “Wind power forecasting
based on a spatial–temporal graph convolution network with limited
engineering knowledge,”IEEE Transactions on Instrumentation and
Measurement, vol. 73, pp. 1–13, 2024.
[23] X. Liang, Q. Gu, and X. You, “Wpformer: A spatial-temporal graph
transformer with auto-correlation for wind power forecasting,”IEEE
Transactions on Sustainable Energy, vol. 16, no. 3, pp. 1491–1503,
2024.
[24] M. Ma, J. Hu, C. S. Jensen, F. Teng, P. Han, Z. Xu, and T. Li,
“Learning time-aware graph structures for spatially correlated time
series forecasting,” in2024 IEEE 40th International Conference on
Data Engineering (ICDE). IEEE, 2024, pp. 4435–4448.
[25] J. M. G. Sope ˜na, V . Pakrashi, and B. Ghosh, “A benchmarking frame-
work for performance evaluation of statistical wind power forecasting
models,”Sustainable Energy Technologies and Assessments, vol. 57,
p. 103246, 2023.
[26] S. R. K. Kottapalli, K. Hubli, S. Chandrashekhara, G. Jain, S. Hubli,
G. Botla, and R. Doddaiah, “Foundation models for time series: A
survey,”arXiv preprint arXiv:2504.04011, 2025.
[27] Y . Liang, H. Wen, Y . Xia, M. Jin, B. Yang, F. Salim, Q. Wen, S. Pan,
and G. Cong, “Foundation models for spatio-temporal data science:
A tutorial and survey,” inProceedings of the 31st ACM SIGKDD
Conference on Knowledge Discovery and Data Mining V . 2, 2025, pp.
6063–6073.
[28] G. Liu, Y . Zhang, P. Zhang, and J. Gu, “Spatiotemporal graph con-
trastive learning for wind power forecasting,”IEEE Transactions on
Sustainable Energy, 2025.
[29] H. Zhang, C. Xu, Y .-F. Zhang, Z. Zhang, L. Wang, and J. Bian,
“Timeraf: Retrieval-augmented foundation model for zero-shot time
series forecasting,”IEEE Transactions on Knowledge and Data Engi-
neering, 2025.
[30] P. Piotrowski, I. Rutyna, D. Baczy ´nski, and M. Kopyt, “Evaluation met-
rics for wind power forecasts: A comprehensive review and statistical
analysis of errors,”Energies, vol. 15, no. 24, p. 9657, 2022.

[31] V . Le Guen and N. Thome, “Shape and time distortion loss for training
deep time series forecasting models,”Advances in neural information
processing systems, vol. 32, 2019.
[32] C. Gallego-Castillo, A. Cuerva-Tejero, and O. Lopez-Garcia, “A review
on the recent history of wind power ramp forecasting,”Renewable and
Sustainable Energy Reviews, vol. 52, pp. 1148–1157, 2015.
[33] R. Meng, G. Smet, D. V . d. Bleeken, A. Van Poecke, H. Tabari,
P. Hellinckx, P. Termonia, and J. V . d. Bergh, “Evaluating the prediction
of wind power ramping events in the belgian offshore zone,”arXiv
preprint arXiv:2510.15474, 2025.
[34] Z. Qiao, S. Pan, A. Wang, V . Zhukova, Y . Liu, X. Jiang, Q. Wen,
M. Long, M. Jin, and C. Liu, “It’s time: Towards the next generation of
time series forecasting benchmarks,”arXiv preprint arXiv:2602.12147,
2026.
[35] X. Wu, J. Lu, Z. Li, X. Qiu, J. Hu, C. Guo, C. S. Jensen, and
B. Yang, “TimeART: Towards agentic time series reasoning via tool-
augmentation,”arXiv preprint arXiv:2601.13653, 2026.
[36] X. Wu, X. Qiu, H. Gao, J. Hu, B. Yang, and C. Guo, “K 2V AE: A
koopman-kalman enhanced variational autoencoder for probabilistic
time series forecasting,” inICML, 2025.
[37] X. Qiu, Y . Zhu, Z. Li, X. Wu, B. Yang, and J. Hu, “DAG: A
dual correlation network for time series forecasting with exogenous
variables,” inICML, 2026.
[38] Z. Li, X. Qiu, Y . Zhu, X. Wu, J. Hu, C. Guo, and B. Yang, “GCGNet:
Graph-consistent generative network for time series forecasting with
exogenous variables,” inICLR, 2026.
[39] X. Qiu, K. Yan, X. Liu, X. Wu, and J. Hu, “Bridging time and
frequency: A joint modeling framework for irregular multivariate time
series forecasting,” inICML, 2026.
[40] X. Liu, X. Qiu, X. Wu, Z. Li, C. Guo, J. Hu, and B. Yang, “Rethinking
irregular time series forecasting: A simple yet effective baseline,” in
AAAI, 2026.
[41] X. Liu, X. Qiu, H. Cheng, X. Wu, C. Guo, B. Yang, and J. Hu, “ASTGI:
Adaptive spatio-temporal graph interactions for irregular multivariate
time series forecasting,” inICLR, 2026.
[42] X. Wu, X. Qiu, H. Cheng, Z. Li, J. Hu, C. Guo, and B. Yang,
“Enhancing time series forecasting through selective representation
spaces: A patch perspective,” inNeurIPS, 2025.
[43] X. Qiu, X. Wu, H. Cheng, X. Liu, C. Guo, J. Hu, and B. Yang,
“DBLoss: Decomposition-based loss function for time series forecast-
ing,” inNeurIPS, 2025.
[44] F. Cheng, H. Liu, and X. Lv, “Metagnsdformer: Meta-learning en-
hanced gated non-stationary informer with frequency-aware attention
for point-interval remaining useful life prediction of lithium-ion bat-
teries,”Advanced Engineering Informatics, vol. 69, p. 103798, 2026.
[45] C. Yu, F. Wang, Z. Shao, T. Qian, Z. Zhang, W. Wei, Z. An, Q. Wang,
and Y . Xu, “Ginar+: A robust end-to-end framework for multivariate
time series forecasting with missing values,”IEEE Transactions on
Knowledge and Data Engineering, vol. 37, no. 8, pp. 4635–4648, 2025.
[46] C. Yu, F. Wang, C. Yang, Z. Shao, T. Sun, T. Qian, W. Wei, Z. An,
and Y . Xu, “Merlin: Multi-view representation learning for robust
multivariate time series forecasting with unfixed missing rates,” in
SIGKDD, 2025, pp. 3633–3644.
[47] X. Wu, X. Qiu, Z. Li, Y . Wang, J. Hu, C. Guo, H. Xiong, and B. Yang,
“CATCH: Channel-aware multivariate time series anomaly detection
via frequency patching,” inICLR, 2025.
[48] B. Zhang, T. Kieu, X. Qiu, C. Guo, J. Hu, A. Zhou, C. S. Jensen,
and B. Yang, “An encode-then-decompose approach to unsupervised
time series anomaly detection on contaminated training data-extended
version,” 2026.
[49] S. Makridakis and M. Hibon, “The m3-competition: results, conclu-
sions and implications,”International journal of forecasting, vol. 16,
no. 4, pp. 451–476, 2000.
[50] S. Makridakis, E. Spiliotis, and V . Assimakopoulos, “The m4 compe-
tition: Results, findings, conclusion and way forward,”International
Journal of forecasting, vol. 34, no. 4, pp. 802–808, 2018.
[51] R. Godahewa, C. Bergmeir, G. I. Webb, R. J. Hyndman, and
P. Montero-Manso, “Monash time series forecasting archive,”arXiv
preprint arXiv:2105.06643, 2021.
[52] A. Zeng, M. Chen, L. Zhang, and Q. Xu, “Are transformers effective
for time series forecasting?” inProceedings of the AAAI conference on
artificial intelligence, vol. 37, no. 9, 2023, pp. 11 121–11 128.
[53] K. Wei, T. Li, F. Huang, J. Chen, and Z. He, “Cancer classification with
data augmentation based on generative adversarial networks,”Frontiers
of Computer Science, vol. 16, no. 2, p. 162601, 2022.
[54] Y . Liang, Z. Shao, F. Wang, Z. Zhang, T. Sun, and Y . Xu, “Basicts: An
open source fair multivariate time series prediction benchmark,” inIn-
ternational symposium on benchmarking, measuring and optimization.
Springer, 2022, pp. 87–101.
[55] Z. Li, X. Qiu, P. Chen, Y . Wang, H. Cheng, Y . Shu, J. Hu, C. Guo,
A. Zhou, C. S. Jensenet al., “Tsfm-bench: A comprehensive and
unified benchmark of foundation models for time series forecasting,”
inProceedings of the 31st ACM SIGKDD Conference on Knowledge
Discovery and Data Mining V . 2, 2025, pp. 5595–5606.
[56] Y . Cheng, C. Guo, K. Chen, K. Zhao, B. Yang, J. Xie, C. S. Jensen,
F. Huang, and K. Zheng, “Gaussian process latent variable modeling
for few-shot time series forecasting,”IEEE Transactions on Knowledge
and Data Engineering, 2025.
[57] Q. Huang, X. Wang, S. X. Rao, Z. Han, Z. Zhang, Y . He, Q. Xu,
Y . Zhao, Z. Zheng, and J. Jiang, “Benchtemp: A general benchmark
for evaluating temporal graph neural networks,” in2024 IEEE 40th
International Conference on Data Engineering (ICDE). IEEE, 2024,
pp. 4044–4057.
[58] J. Wang, J. Jiang, W. Jiang, C. Li, and W. X. Zhao, “Libcity: An open
library for traffic prediction,” inProceedings of the 29th international
conference on advances in geographic information systems, 2021, pp.
145–148.
[59] Z. Shao, F. Wang, Y . Xu, W. Wei, C. Yu, Z. Zhang, D. Yao, T. Sun,
G. Jin, X. Caoet al., “Exploring progress in multivariate time series
forecasting: Comprehensive benchmarking and heterogeneity analysis,”
IEEE Transactions on Knowledge and Data Engineering, vol. 37, no. 1,
pp. 291–305, 2024.
[60] P. Jiang, Y . Wang, and J. Wang, “Short-term wind speed forecasting
using a hybrid model,”Energy, vol. 119, pp. 561–577, 2017.
[61] Y . Ma, Y . He, X. Cun, X. Wang, S. Chen, X. Li, and Q. Chen,
“Follow your pose: Pose-guided text-to-video generation using pose-
free videos,” inAAAI, vol. 38, no. 5, 2024, pp. 4117–4125.
[62] Y . Ma, H. Liu, H. Wang, H. Pan, Y . He, J. Yuan, A. Zeng, C. Cai,
H.-Y . Shum, W. Liuet al., “Follow-your-emoji: Fine-controllable and
expressive freestyle portrait animation,” inSIGGRAPH Asia, 2024, pp.
1–12.
[63] Y . Ma, K. Feng, Z. Hu, X. Wang, Y . Wang, M. Zheng, X. He, C. Zhu,
H. Liu, Y . Heet al., “Controllable video generation: A survey,”arXiv
preprint arXiv:2507.16869, 2025.
[64] Y . Ma, J. Wang, Y . Wang, X. Wang, Z. Li, X. Wang, H. Liu,
R. Liang, S. Zhang, Y . Xueet al., “Livelight: Real-time streaming video
relighting with interactive control,”arXiv preprint arXiv:2608.01771,
2026.
[65] H. Yin, Z. Ou, S. Huang, and A. Meng, “A cascaded deep learning
wind power prediction approach based on a two-layer of mode decom-
position,”Energy, vol. 189, p. 116316, 2019.
[66] Y . Xiao, C. Zou, H. Chi, and R. Fang, “Boosted gru model for
short-term forecasting of wind power with feature-weighted principal
component analysis,”Energy, vol. 267, p. 126503, 2023.
[67] M. Gong, C. Yan, W. Xu, Z. Zhao, W. Li, Y . Liu, and S. Li, “Short-
term wind power forecasting model based on temporal convolutional
network and informer,”Energy, vol. 283, p. 129171, 2023.
[68] Y . Song, D. Tang, J. Yu, Z. Yu, and X. Li, “Short-term forecasting
based on graph convolution networks and multiresolution convolution
neural networks for wind power,”IEEE Transactions on Industrial
Informatics, vol. 19, no. 2, pp. 1691–1702, 2022.
[69] P. Yi, Z. Bao, F. Huang, J. Wang, J. Peng, and L. Zhang, “Towards
effective long-term wind power forecasting: A deep conditional gener-
ative spatio-temporal approach,”IEEE Transactions on Knowledge and
Data Engineering, vol. 36, no. 12, pp. 9403–9417, 2024.
[70] Q. Meng, Y . Gao, Y . He, S. Hussain, J. Lu, Y . Chen, C. Qin, F. Luo, and
J. M. Guerrero, “Powermistral: A data-efficient wind power forecasting
framework leveraging pre-trained large language models,”Applied
Energy, vol. 411, p. 127625, 2026.
[71] Y . Fan, T. Song, C. Feng, C. Liu, and D. Jiang, “Wind power prediction
using foundation large time series models enhanced by time series
prompt in exogenous and tuning forms,”Applied Energy, vol. 400, p.
126535, 2025.
[72] C. G ¨uuck, C. Roelofs, and S. Faulstich, “Care to compare: A real-world
dataset for anomaly detection in wind turbine data,”arXiv preprint,
2024.

[73] S. Fogelstr ¨om, H. Johansson, and O. Carlson, “Bj ¨ork¨o wind turbine
version 1 (45kw) scada,” Zenodo, 2023, version v1; Accessed: 2026-
05-22. [Online]. Available: https://doi.org/10.5281/zenodo.8213270
[74] 4castRenewables, “CliMetLab Plugin A6: Weather Data and Power
Production from Renewables,” https://github.com/4castRenewables/
climetlab-plugin-a6, 2024, gitHub repository; Apache-2.0 license; Ac-
cessed: 2026-05-22.
[75] N. Effenberger and N. Ludwig, “A collection and categorization of
open-source wind and wind power datasets,”Wind Energy, vol. 25,
no. 10, pp. 1659–1683, 2022.
[76] Y . Chen and J. Xu, “Solar and wind power data from the chinese state
grid renewable energy generation forecasting competition,”Scientific
data, vol. 9, no. 1, p. 577, 2022.
[77] TheForceCoder, “Wind Power Forecasting,” https://www.kaggle.com/
datasets/theforcecoder/wind-power-forecasting, n.d., kaggle dataset;
Accessed: 2026-05-22.
[78] Wasurat Me96, “IIOT Data of Wind Turbine,” https://www.kaggle.com/
datasets/wasuratme96/iiot-data-of-wind-turbine, n.d., kaggle dataset;
Accessed: 2026-05-22.
[79] J. Dowell and P. Pinson, “Very-short-term probabilistic wind power
forecasts by sparse vector autoregression,”IEEE Transactions on Smart
Grid, vol. 7, no. 2, pp. 763–770, 2015.
[80] T. V . Jensen, H. de Sevin, M. Greiner, and P. Pinson, “The RE-Europe
Data Set,” Zenodo, 2017, version v3; Accessed: 2026-05-22. [Online].
Available: https://doi.org/10.5281/zenodo.999150
[81] C. Plumley, “Kelmarsh Wind Farm Data,” Zenodo, 2022,
accessed: 2026-05-22. [Online]. Available: https://doi.org/10.5281/
zenodo.5841834
[82] ——, “Penmanshiel Wind Farm Data,” Zenodo, 2022, accessed: 2026-
05-22. [Online]. Available: https://doi.org/10.5281/zenodo.5946808
[83] J. Passos, Y . Sakagami, and P. Santos, “Coastal Operating Wind
Farms: Two Datasets with Concurrent SCADA, Lidar and Turbulent
Fluxes,” Zenodo, 2019, accessed: 2026-05-22. [Online]. Available:
https://doi.org/10.5281/zenodo.1475197
[84] J. Herzen, F. L ¨assig, S. G. Piazzetta, T. Neuer, L. Tafti, G. Raille,
T. Van Pottelbergh, M. Pasieka, A. Skrodzki, N. Hugueninet al.,
“Darts: User-friendly modern machine learning for time series,”Jour-
nal of Machine Learning Research, vol. 23, no. 124, pp. 1–6, 2022.
[85] B. Kedem and K. Fokianos,Regression models for time series analysis.
John Wiley & Sons, 2005.
[86] H. Y . Toda and P. C. Phillips, “Vector autoregression and causality:
a theoretical overview and simulation study,”Econometric reviews,
vol. 13, no. 2, pp. 259–285, 1994.
[87] A. Zeng, M. Chen, L. Zhang, and Q. Xu, “Are transformers effective
for time series forecasting?” inProceedings of the AAAI conference on
artificial intelligence, vol. 37, no. 9, 2023, pp. 11 121–11 128.
[88] X. Chen, H. Jin, Y . Huang, and Z. Feng, “Xlinear: A lightweight and
accurate mlp-based model for long-term time series forecasting with
exogenous inputs,”arXiv preprint arXiv:2601.09237, 2026.
[89] X. Qiu, X. Wu, Y . Lin, C. Guo, J. Hu, and B. Yang, “DUET: Dual
clustering enhanced multivariate time series forecasting,” inSIGKDD,
2025, pp. 1185–1196.
[90] Y . Nie, N. H. Nguyen, P. Sinthong, and J. Kalagnanam, “A time series
is worth 64 words: Long-term forecasting with transformers,”arXiv
preprint arXiv:2211.14730, 2022.
[91] Y . Liu, T. Hu, H. Zhang, H. Wu, S. Wang, L. Ma, and M. Long,
“itransformer: Inverted transformers are effective for time series fore-
casting,” inInternational conference on learning representations, vol.
2024, 2024, pp. 11 116–11 140.
[92] A. Stitsyuk and J. Choi, “xpatch: Dual-stream time series forecasting
with exponential seasonal-trend decomposition,” inProceedings of the
AAAI Conference on Artificial Intelligence, vol. 39, no. 19, 2025, pp.
20 601–20 609.
[93] Y . Liu, H. Zhang, C. Li, X. Huang, J. Wang, and M. Long, “Timer:
Generative pre-trained transformers are large time series models,”arXiv
preprint arXiv:2402.02368, 2024.
[94] V . Ekambaram, A. Jati, P. Dayama, S. Mukherjee, N. H. Nguyen,
W. M. Gifford, C. Reddy, and J. Kalagnanam, “Tiny time mixers
(ttms): Fast pre-trained models for enhanced zero/few-shot forecasting
of multivariate time series,”Advances in Neural Information Processing
Systems, vol. 37, pp. 74 147–74 181, 2024.
[95] B. Cohen, E. Khwaja, Y . Doubli, S. Lemaachi, C. Lettieri, C. Masson,
H. Miccinilli, E. Ram ´e, Q. Ren, A. Rostamizadehet al., “This time
is different: An observability perspective on time series foundation
models,”Advances in Neural Information Processing Systems, vol. 38,
pp. 50 907–50 951, 2026.
[96] H. He, K. Yi, Y . Ma, Q. Zhang, Z. Niu, and G. Pang, “Sempo:
Lightweight foundation models for time series forecasting,”Advances
in Neural Information Processing Systems, vol. 38, pp. 161 846–
161 879, 2026.
[97] Z. Shao, Z. Zhang, F. Wang, W. Wei, and Y . Xu, “Spatial-temporal
identity: A simple yet effective baseline for multivariate time series
forecasting,” inProceedings of the 31st ACM international conference
on information & knowledge management, 2022, pp. 4454–4458.
[98] L. Cao, B. Wang, G. Jiang, Y . Yu, and J. Dong, “Spatiotemporal-aware
trend-seasonality decomposition network for traffic flow forecasting,”
inProceedings of the AAAI Conference on Artificial Intelligence,
vol. 39, no. 11, 2025, pp. 11 463–11 471.
[99] M. Jin, G. Shi, Y .-F. Li, B. Xiong, T. Zhou, F. D. Salim, L. Zhao,
L. Wu, Q. Wen, and S. Pan, “Towards expressive spectral-temporal
graph neural networks for time series forecasting,”IEEE Transactions
on Pattern Analysis and Machine Intelligence, 2025.
[100] J. Han, W. Zhang, H. Liu, T. Tao, N. Tan, and H. Xiong, “Bigst: Linear
complexity spatio-temporal graph neural network for traffic forecasting
on large-scale road networks,”Proc. VLDB Endow., vol. 17, no. 5, pp.
1081–1090, 2024.
[101] Z. Li, L. Xia, L. Shi, Y . Xu, D. Yin, and C. Huang, “Opencity: Open
spatio-temporal foundation models for traffic prediction,”CoRR, vol.
abs/2408.10269, 2024.
[102] S. Zhong, J. Qiu, Y . Wu, Y . Liu, Y . He, Z. Rao, B. Yang, C. Guo,
H. Xu, and Y . Liang, “Learning to factorize and adapt: A versatile
approach toward universal spatio-temporal foundation models,”CoRR,
vol. abs/2601.12083, 2026.
[103] T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama, “Optuna: A
next-generation hyperparameter optimization framework,” inProceed-
ings of the 25th ACM SIGKDD international conference on knowledge
discovery & data mining, 2019, pp. 2623–2631.
[104] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan,
T. Killeen, Z. Lin, N. Gimelshein, L. Antigaet al., “Pytorch: An
imperative style, high-performance deep learning library,”Advances
in neural information processing systems, vol. 32, 2019.
