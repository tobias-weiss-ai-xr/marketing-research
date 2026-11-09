---
title: 'Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored
  in MMM'
url: https://arxiv.org/abs/2606.16878
category: analytics
subcategory: measurement
date: 2026-06
venue: arXiv (Cornell University)
authors:
- Meghana Bhat
- Ankit Umare
- Utsav Aggarwal
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.16878
pages: 11
chars: 23600
fetched_at: '2026-11-08T12:57:29+00:00'
kb_version: 1
---

# Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM

Integrated Marketing Attribution: A Bayesian
Framework for Privacy-Safe Granular Measurement
Anchored in MMM
Meghana R. Bhat, Ankit Umare, Utsav Aggarwal, Richard Vecsler,
Arunkumar Mani, Karthik Nair, and Chandhu Nair
Lowe’s Companies, Inc.
Abstract
Retail marketing measurement increasingly requires granular campaign-level
insights without relying on user-level tracking. However, the two dominant ap-
proaches, Marketing Mix Modeling (MMM) and Multi-Touch Attribution (MTA),
often produce fragmented insights. MMM is privacy-safe and robust for channel-
level planning but is too coarse for campaign optimization, while MTA provides
granular attribution but has become less reliable under increasing privacy re-
strictions. We proposeIntegrated Marketing Attribution (IMA), a unified
framework that combines MMM with channel-specific Bayesian attribution mod-
els to derive campaign-level effects from aggregated data. By leveraging MMM-
informed priors, IMA delivers granular, privacy-safe attribution while preserving
consistency with MMM.
Keywords: Marketing Mix Modeling (MMM), Multi-Touch Attribution (MTA)
1 Introduction
Modern marketing measurement is increasingly defined by a tradeoff between robust-
ness and granularity. Retailers and brands need measurement systems that can guide
strategic budget allocation while also supporting tactical campaign optimization. Two
approaches have traditionally dominated this space: MMM and MTA. While both
provide valuable insights, they operate at different levels of granularity and rely on
distinct data sources and assumptions, often resulting in fragmented measurement and
misalignment between strategic planning and tactical execution.
MMM estimates the impact of marketing activities using aggregated data over long
time horizons, making it a robust and privacy-safe approach for measuring channel-level
effectiveness across both digital and offline media. MMM is therefore widely used to in-
form longer-horizon budget planning and channel-level investment decisions. However,
1
arXiv:2606.16878v3  [cs.LG]  18 Jun 2026

it is poorly suited for evaluating individual campaigns. At the campaign-level granu-
larity, model dimensionality increases substantially, correlations across campaigns in-
tensify, and the number of observations becomes limited, leading to unstable parameter
estimates and overfitting. As a result, MMM alone cannot reliably support short-term
decision-making.
MTA was introduced to address these limitations by assigning conversion credit to
individual digital touchpoints along a customer journey. By leveraging user-level data,
MTA provides quick feedback for campaign optimization. However, the ongoing shift
toward a privacy-centric digital ecosystem, including the deprecation of third-party
cookies and restrictions on cross-site tracking, has significantly reduced the reliabil-
ity and scalability of MTA. As customer journeys become increasingly incomplete or
unobservable, MTA models suffer from biased attribution and operational fragility.
These limitations reveal a critical gap in modern marketing measurement: the
absence of a privacy-safe framework that delivers granular, actionable insights while
remaining consistent with MMM outcomes. To address this gap, we propose Integrated
Marketing Attribution (IMA), a unified modeling framework that delivers granular at-
tribution using aggregated data and is tightly integrated with MMM. IMA decomposes
channel-level incremental contributions estimated by MMM into campaign-level effects
using channel-specific attribution models. By adopting MMM-informed Bayesian pri-
ors, IMA mitigates high dimensionality and multicollinearity while preserving consis-
tency with MMM outputs.
The contributions of this paper are threefold: (1) we introduce IMA as a unified
and privacy-safe attribution framework; (2) we propose a channel-specific Bayesian
modeling approach guided by MMM priors; and (3) we demonstrate the effectiveness
of IMA using real-world marketing data.
2 Related Work
MTA has been widely used for granular digital measurement. However, the loss of
third-party cookies and restrictions on cross-site tracking reduce visibility into com-
plete customer journeys, rendering user-level attribution models increasingly infeasible
[Churchill et al., 2025]. As a result, MTA suffers from incomplete data, biased attri-
bution, and reduced reliability, limiting its usefulness in a privacy-centric environment
[Greenfield, 2022].
In response, alternative approaches to marketing measurement have gained promi-
nence. MMM has re-emerged as a scalable and privacy-safe approach based on aggre-
gated data, supported by recent advances in Bayesian MMM and related methodolo-
gies [Jin et al., 2017, Chan and Perry, 2017]. At the same time, Gordon et al. [2019]
show that incrementality-based methods based on randomized experiments provide a
principled framework for measuring causal effects. More recently, Google [2022] pro-
pose a unified measurement framework that integrates MMM, MTA, and experimen-
tation within a Bayesian setting, emphasizing knowledge transfer via priors, modeling
2

cross-channel interactions, and generating consistent probabilistic insights for improved
decision-making. Related work also explores aggregate-data approaches motivated by
privacy constraints [Churchill et al., 2025], combining elements of MMM and machine
learning.
These developments are also reflected in industry perspectives. For example, Forbes
Tech Council [2023, 2022] highlight MMM, incrementality experiments, and hybrid
frameworks as practical alternatives to MTA, emphasizing trade-offs between granu-
larity, scalability, and causal rigor, while Skai [2022] advocate for incrementality-based
measurement to isolate true marketing impact under privacy constraints.
Several works position MMM as a central component of future measurement sys-
tems. MASS Analytics [2022] argue that MMM will play a key role due to its reliance on
aggregated data and privacy-safe design, highlighting advances such as increased gran-
ularity, faster refresh cycles, and Bayesian methods. Lau [2022] describe how American
Express is adopting MMM as a privacy-safe foundation while extending it to support
more granular, campaign-informed decisions through geo-level analysis and richer dig-
ital signals. However, neither work provides a reproducible, end-to-end methodology
validated across diverse campaign types.
While incrementality-based approaches provide strong causal insights, they remain
difficult to scale in practice, particularly for large retail organizations running thou-
sands of campaigns across channels and geographies. Designing, executing, and main-
taining experiments at this scale is often operationally and economically infeasible.
Motivated by these constraints, we adopt a granular MMM-based approach in IMA.
Unlike prior proposals that often lack end-to-end validation on real-world campaign
data at scale, IMA is a concrete methodology validated using real-world marketing
data.
3 Integrated Marketing Attribution (IMA) Frame-
work
IMA is designed to decompose channel-level incremental contributions estimated by
MMM into granular campaign-level effects. Guided by Bayesian priors derived from
MMM, the framework estimates separate models for each channel, mitigating high di-
mensionality and cross-channel multicollinearity without relying on user-level tracking.
As illustrated in Figure 1, the IMA framework consists of three stages: (1) MMM
estimation, (2) temporal disaggregation, and (3) channel-specific attribution model-
ing. Table 1 summarizes the underlying data schema and modeling structure used
throughout the framework. While MMM operates on weekly channel-level data, IMA
produces daily campaign-level attribution by disaggregating channel-level incremental
sales contributions using daily media series and channel-specific models.
First, a weekly MMM model is estimated using aggregated sales, pricing, promotion,
macroeconomic variables, and weekly channel-level media series. MMM produces two
3

key outputs: (i) weekly channel-level incremental sales contributions and (ii) channel-
level adstock parameters and coefficients.
Second, the weekly channel-level incremental contributions are temporally disaggre-
gated to daily resolution. Rather than applying a na ¨ ıve proportional split, we leverage
the adstock transformations learned by MMM. For each channel, the MMM-estimated
adstock parameters are converted from weekly to daily scale and tuned where neces-
sary to reflect daily signal dynamics. These daily adstock parameters are then applied
to daily channel-level media data to generate adstock-transformed daily media series
which are subsequently used to distribute weekly channel-level incremental sales into
daily channel-level incremental contributions. This preserves the carryover structure
learned by MMM while enabling daily-level modeling.
Finally, IMA trains independent attribution models for each channel.
Figure 1: IMA Model Architecture
Table 1: Data schema and modeling structure used in the IMA framework
Field Description
Modeling window 3 years historical data
MMM intervals Weekly
IMA intervals Daily
Channels Search, Social, Display,...
Media series Impressions, clicks, or spend
Outcome Campaign-level incremental sales
Evaluation Channel-level aggregated IMA vs. MMM contributions
4

3.1 Channel-Specific Attribution Models
For each channelc, we estimate a separate Bayesian regression model. The target vari-
able (ModelY) is the daily channel-level incremental sales contribution obtained from
temporal disaggregation. The input variables (ModelX) consist of daily campaign-
level media series within channelc, such as spend, impressions, and clicks. The es-
timated campaign-level contributions are computed using the fitted coefficients from
the channel-specific IMA model and the corresponding adstock-transformed campaign-
level media series. Channel-level coefficients estimated by MMM serve as informative
priors for the corresponding channel-specific model, guiding campaign-level estimates
while reducing overfitting when campaign-level data are sparse or highly correlated.
This formulation ensures that the estimated campaign-level contributions aggregate to
the daily channel-level incremental sales anchored by MMM.
3.2 IMA Model Specification
We do not elaborate on the MMM specification itself, as MMM is a well-established
modeling framework and the focus of this paper is the downstream attribution layer
that uses MMM outputs as anchors.
Adstock Transformation.Media effects on sales may lag behind the original expo-
sure and persist over several periods. Following Jin et al. [2017] and He [2020], we model
this carry-over effect using an adstock transformation with parametersL(length of the
media effect window),P(peak/delay of the effect), andD∈(0,1) (decay/retention
rate).
For a campaign-level media input series{x t}, wherex t denotes the raw media
exposure at timet, the adstock-transformed valuex ∗ t is computed as a normalized
weighted average over the current and previousL−1 periods. The weight at laglis
defined as:
wt−l =D (l−P) 2 ,for eachl∈[0, L) (1)
where larger values ofDproduce a more dispersed (longer-lasting) effect, andPcon-
trols how many periods the peak effect lags behind the initial exposure. The adstock-
transformed series is then:
x∗ t = Adstock(xt, . . . , xt−(L−1);L, P, D) =
PL−1
l=0 wt−l ·x t−l PL−1
l=0 wt−l
(2)
Bayesian Regression.For each channelc, we estimate a Bayesian linear regres-
sion overMcampaigns using PyMC [Salvatier et al., 2016]. Lety t denote the daily
channel-level incremental sales contribution (obtained from temporal disaggregation in
Stage 2), and letx ∗ j,t denote the adstock-transformed daily media series for campaign
j∈ {1, . . . , M}at timet. The interceptαcaptures residual channel-level incremental
5

contribution not explained by the campaign media inputs, andβ j denotes the effec-
tiveness coefficient for campaignj. Following the Bayesian regression formulation in
Bishop and Nasrabadi [2006], the likelihood is specified as a Normal distribution with
meanµ t and varianceσ 2, following the notation used in the PyMC documentation
[Salvatier et al., 2016]:
Likelihood:
yt ∼ N(µt, σ2) (3)
µt =α+
MX
j=1
βj ·x ∗ j,t (4)
Priors:
βj ∼TruncatedNormal(β c, σβ; lower = 0) forj= 1, . . . , M(5)
α∼TruncatedNormal(α c, σα; lower = 0) (6)
σ∼HalfNormal(10) (7)
whereβ c is the aggregate channel-level media effectiveness coefficient derived from
MMM, shared as the prior mean across allMcampaign-level coefficients, andα c is
the corresponding MMM-derived channel-level offset. The non-negativity constraint
onαandβ j encodes the economic assumption that baseline contribution and media
exposure do not reduce sales, while anchoring the prior means to MMM-derived esti-
mates regularizes the model toward aggregate channel effects. The prior scalesσ α and
σβ are weakly informative hyperparameters set to be sufficiently diffuse to allow the
data to dominate posterior inference while preserving the economic constraints. The
observation noise prior onσfollows a half-normal distribution [Salvatier et al., 2016].
Inference.Posterior inference is performed using Automatic Differentiation Varia-
tional Inference (ADVI) [Kucukelbir et al., 2017] as implemented in PyMC [Salvatier
et al., 2016], chosen for computational scalability when fitting independent models
across multiple channels every week.
4 Experiments & Results
IMA was evaluated using three years of historical daily data across media channel.
For benchmarking, daily IMA predictions are aggregated to weekly resolution and
compared against the corresponding weekly MMM-derived channel contributions, since
MMM outputs and benchmark error metrics are defined at the weekly level. Due to
privacy constraints, channel names, dates, and absolute revenue magnitudes are not
disclosed.
6

4.1 Campaign-Level Multicollinearity
We begin by illustrating the structural challenge of campaign-level modeling. Figure 2
presents a correlation heatmap of campaign-level adstock-transformed media variables
within a representative channel. Campaigns are ordered alphabetically along both
axes, and each cell represents pairwise correlation.
The heatmap reveals substantial off-diagonal correlations, including visible block
structures corresponding to campaign families and overlapping flighting patterns. Such
high multicollinearity is typical in large-scale marketing environments. Under standard
regression approaches, this degree of correlation would result in unstable coefficients,
inflated variance, sign reversals, and overfitting.
This structural challenge led to the usage of Bayesian regression in IMA. By incorpo-
rating MMM-informed priors at the channel level, campaign coefficients are regularized
toward economically consistent values, reducing variance while allowing data-driven
differentiation where signal strength exists.
Figure 2: Correlation heatmap of campaigns within a representative channel
4.2 Channel-Level Model Fit
Although IMA is trained at the daily level, model evaluation is conducted at the weekly
level to ensure comparability with MMM benchmarks. Daily predicted incremental
contributions are aggregated to weekly totals and compared against the correspond-
ing weekly MMM-derived channel contributions. Despite the high dimensionality and
multicollinearity observed at the campaign level, IMA demonstrates strong consistency
with the MMM-derived channel contribution target. Figure 3 illustrates model fit for
a representative channel. The aggregated IMA predictions closely track weekly MMM
incremental contributions, achieving an R²of 0.98. This confirms that IMA preserves
7

the aggregate channel signal while operating at campaign-level granularity. This high
fit is notable given that IMA represents a second-stage model, estimating incremental
contributions at a lower signal-to-noise ratio than the primary MMM model.
Figure 3: IMA model fit for a representative channel
4.3 Campaign-Level Results
Figure 4 illustrates the distribution of campaign-level incremental sales contributions
for the same representative channel shown in Figure 3 over the most recent quarter.
Each point represents a campaign, with the x-axis corresponding to aggregated adstock-
transformed impressions and the y-axis representing IMA-estimated incremental sales
contribution.
Although campaign coefficients are anchored to a common MMM-derived chan-
nel prior, posterior estimates diverge meaningfully based on observed campaign-level
signal. The resulting dispersion highlights heterogeneous campaign effectiveness, in-
cluding low performers, moderate contributors, and high-impact outliers. This demon-
strates that Bayesian shrinkage stabilizes estimates without enforcing proportional al-
location. Campaign-level contributions are allowed to deviate from the MMM anchor
where supported by the data, while remaining consistent with channel-level constraints.
4.4 Error Metrics Across Channels
Using weekly-aggregated predictions for benchmarking, IMA achieves the following
Mean Absolute Percentage Error (MAPE) scores across a subset of representative and
commonly used channels:
1. Search: 4.1%
2. Social: 5.97%
3. Display: 3.25%
8

Figure 4: IMA campaign-level results
These error rates are modestly higher than primary MMM benchmark ( 2 %), which
is expected for several reasons:
1. IMA models incremental channel contributions whereas MMM is optimized on
total sales
2. The incremental contribution targets has lower signal magnitude and higher
volatility than total sales
3. Campaign-level modeling introduces high dimensionality and multicollinearity
4. IMA operates independently per channel without cross-channel smoothing
Given these structural constraints, sub-6% weekly MAPE represents strong consis-
tency with MMM-derived channel-level contributions. The results indicate that IMA
introduces only a limited degradation in aggregate predictive accuracy while deliver-
ing substantial gains in campaign-level granularity. Overall, the experiments demon-
strate that IMA maintains alignment with MMM at the weekly channel level while
enabling stable, differentiated attribution at the campaign level within a fully aggre-
gated, privacy-safe framework.
5 Conclusions
This paper introduced IMA as a scalable, privacy-safe framework for deriving campaign-
level attribution from MMM outputs. IMA addresses the limitations of both user-level
attribution and large-scale experimentation need by decomposing MMM-estimated
channel contributions into granular campaign-level effects using independent Bayesian
models with MMM-anchored priors.
The empirical results demonstrate that IMA maintains strong alignment with MMM
at the weekly channel level while enabling differentiated campaign-level attribution.
9

Despite operating at a more granular level, IMA achieves low weekly MAPE (3–6%)
and high reconstruction accuracy (R²). These results indicate that granular attribu-
tion can be achieved with only limited degradation in aggregate predictive accuracy.
IMA provides stability, interpretability, and scalability without relying on user-level
tracking.
IMA is not a conceptual blending of methodologies but a concrete and operational
framework validated on three years of real-world marketing data. It is designed to
scale across large organizations managing thousands of campaigns concurrently, where
experimentation alone may be impractical and user-level attribution infeasible.
Several avenues for future work remain. First, extending IMA to incorporate struc-
tured cross-channel interactions could further enhance tactical coordination across me-
dia channels. Second, future work may explore dynamic updating of MMM-informed
priors through rolling or sequential Bayesian estimation, enabling faster adaptation
to changing market conditions and evolving channel effectiveness. Third, integrating
experimental results directly into the Bayesian framework as structured prior updates
could strengthen causal grounding. Finally, a natural extension of IMA involves in-
corporating geo-level variation through hierarchical Bayesian modeling. By estimating
campaign effects across geographies with partial pooling, IMA could capture regional
heterogeneity while preserving statistical stability and improving robustness in sparse
data settings.
IMA represents a step toward a durable measurement paradigm: one that de-
livers granular campaign-level attribution without relying on deterministic user-level
tracking, while preserving consistency with aggregate MMM measurement. By using
MMM-derived channel effects as anchors, IMA produces stable campaign-level decom-
positions that allow meaningful differentiation without estimating each campaign in
isolation.
References
Christopher M Bishop and Nasser M Nasrabadi.Pattern recognition and machine
learning. Springer, 2006.
David Chan and Mike Perry. Challenges and opportunities in media mix modeling.
Google Research, 2017.
Victor Churchill, H. Alice Li, and Dongbin Xiu. Modeling aggregate consumer journeys
in a cookie-free environment: A two-stage framework for marketing mix models,
2025. Working paper.
Forbes Tech Council. Media mix modeling or incrementality measurement: Which will
replace multi-touch attribution?https://www.forbes.com/councils/forbeste
chcouncil/2022/07/08/media-mix-modeling-or-incrementality-measurement
-which-will-replace-multi-touch-attribution/, July 2022. Forbes.
10

Forbes Tech Council. A comparison of marketing measurement approaches in a cook-
ieless world, January 2023. URLhttps://www.forbes.com/councils/forbestech
council/2023/01/11/a-comparison-of-marketing-measurement-approaches-i
n-a-cookieless-world/. Forbes.
Google. Unified marketing measurement: The power of blending methodologies. Tech-
nical report, Think with Google, 1 2022. URLhttps://www.thinkwithgoogl
e.com/_qs/documents/15401/UnifiedMarketingMeasurement.pdf. Accessed:
2024-05-22.
Brett R Gordon, Florian Zettelmeyer, Neha Bhargava, and Dan Chapsky. A comparison
of approaches to advertising measurement: Evidence from big field experiments at
facebook.Marketing Science, 2019.
Jeff Greenfield. What is the impact of losing third-party cookies on mta?, 2022. URL
https://provalytics.com/what-is-the-impact-of-losing-3rd-party-cooki
es-on-mta/. Provalytics.
Sibyl He. Python/STAN implementation of multiplicative marketing mix model.http
s://github.com/sibylhe/mmm_stan, 2020. GitHub repository.
Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan, and Jim Koehler. Bayesian
methods for media mix modeling with carryover and shape effects.Google Research,
pages 1–34, 2017.
Alp Kucukelbir, Dustin Tran, Rajesh Ranganath, Andrew Gelman, and David M.
Blei. Automatic differentiation variational inference.Journal of Machine Learning
Research, 18(1):430–474, 2017.
Allison D. Lau. Amex is planning for the cookieless future with an eye on mmm, 2022.
URLhttps://www.adexchanger.com/advertiser/amex-is-planning-for-the
-cookieless-future-with-an-eye-on-mmm/. AdExchanger.
MASS Analytics. What is the future of mmm in a cookieless world?, 2022. URL
https://mass-analytics.com/marketing-mix-modeling-blogs/what-is-the
-future-of-mmm-in-a-cookiesless-world/. MASS Analytics Blog.
John Salvatier, Thomas V. Wiecki, and Christopher Fonnesbeck. Probabilistic pro-
gramming in Python using PyMC3.PeerJ Computer Science, 2:e55, 2016.
Skai. Attribution in a cookieless world, 2022. URLhttps://skai.io/blog/attribu
tion-in-a-cookieless-world/. Skai Blog.
11
