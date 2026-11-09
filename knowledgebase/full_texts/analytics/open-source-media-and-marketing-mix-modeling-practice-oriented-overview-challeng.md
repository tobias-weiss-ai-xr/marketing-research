---
title: 'Open-Source Media and Marketing Mix Modeling: Practice-Oriented Overview, Challenges, Opportunities'
url: https://doi.org/10.1007/s40547-026-00161-4
category: analytics
subcategory: measurement
date: 2026-04
venue: Customer Needs and Solutions
authors:
- Julian Runge
- Koen Pauwels
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s40547-026-00161-4.pdf
pages: 16
chars: 65838
fetched_at: '2026-11-08T17:04:13+00:00'
kb_version: 1
---

# Open-Source Media and Marketing Mix Modeling: Practice-Oriented Overview, Challenges, Opportunities

PERSPECTIVE
Customer Needs and Solutions            (2026) 13:3
https://doi.org/10.1007/s40547-026-00161-4
between the methodological advances documented in schol-
arly research and the tools readily available to practitioners,
possibly constraining organizations’ ability to align market-
ing resource allocation with evolving customer needs.
Recently, this gap has sprung to the forefront of digi -
tal marketing practice as privacy-enhancing technologies
are making it difficult, and in many cases impossible, to
directly measure and observe digital customer journeys
[6, 7]. Bottom-up approaches from user-specific data are
less feasible, making top-down approaches more appeal -
ing [8]. Many online and digital-first advertisers, however,
almost exclusively relied on these deterministic measure -
ment and attribution approaches that are increasingly being
rendered obsolete. The emergence of open-source m/MMM
tools offers a promising response to this challenge. Grass -
roots analytics communities and large online advertising
platforms such as Meta Platforms and Google have started
developing open-source packages that aim to fill this mea -
surement gap and support digital advertisers in adopting m/
MMM.1
1  The incentive for the largest online advertising platforms to start
developing these solutions is that measurement commonly is a
1 Introduction
Marketing organizations have long turned to media and mar-
keting mix modeling [1] as a systematic approach for quan-
tifying how marketing investments translate into customer
responses and revenue. These models have shaped not only
academic understanding of consumer behavior and market-
ing strategy but also organizational practices for budgeting,
forecasting, and evaluating the return on marketing spend -
ing [2–5]. Despite their importance, m/MMM implementa -
tions have historically been costly, opaque, and confined
to a limited set of specialized vendors. This creates a gap
  Julian Runge
julian.runge@northwestern.edu
  Koen Pauwels
k.pauwels@northeastern.edu
1 Medill School of Journalism, Media, Integrated Marketing
Communications, Northwestern University, Evanston, USA
2 D ❜Amore-McKim School of Business, Northeastern
University, Boston, USA
Abstract
Privacy-enhancing technologies are reshaping online advertising, making it increasingly difficult for advertisers to track
customer journeys and link marketing actions to economic outcomes. As a result, interest in probabilistic measurement
techniques such as media and marketing mix modeling (m/MMM) has surged, particularly among digital-first advertis -
ers. Many of these advertisers are small and midsize firms that rely heavily on digital channels yet lack the resources
to commission bespoke proprietary models. Against this backdrop, grassroots analytics communities and large online
advertising platforms such as Meta Platforms and Google have started developing open-source packages for m/MMM.
The packages share core principles but differ on important aspects such as their degree of automation, ease of use, and
modeling paradigms. This article provides a narrative review and practice-oriented synthesis of these developments and
discusses the challenges and opportunities that come with “packaged up” m/MMM. It concludes with an outline of topics
that marketing scholars can engage with to vet and extend open-source m/MMM, and to align its continued development
with its users’ needs.
Keywords Media mix modeling · Marketing mix modeling · Open source · Computational packages · Applied
marketing analytics
Received: 1 September 2025 / Accepted: 7 February 2026
© The Author(s) 2026
Open-Source Media and Marketing Mix Modeling: Practice-Oriented
Overview, Challenges, Opportunities
Julian Runge1 · Koen Pauwels2
1 3

Customer Needs and Solutions            (2026) 13:3
The first foray to offer an open-source package for
m/MMM was Facebook’s release of Robyn in the early
2020s [9–11]. Google followed suit with Lightweight [ 12]
and Meridian [ 13, 14]. PyMC is a longstanding package
for Bayesian modeling, first initiated in 2007. In Novem -
ber 2022, PyMC Labs released PyMC-Marketing that
specifically focuses on marketing analytics, including
PyMC-Marketing-mmm for m/MMM [ 15]. Robyn’s entry
triggered both enthusiasm and skepticism. On one hand, it
represents a philosophical and practical shift: from black-
box modeling to transparent and fast estimation with a
high degree of automation. On the other hand, it poses
methodological and managerial challenges: Is open-
source m/MMM “good enough” for high-stakes budget
decisions? Can firms without deep analytics teams use it
responsibly and understand model assumptions and per -
formance adequately?
Providing accurate and convincing automation for
causal inference problems such as m/MMM is chal -
lenging. Some components of the open-source pack -
ages are novel and unvetted, e.g., the multi-objective
optimization approach in Robyn [ 11]. By providing a
practice-oriented overview of open-source m/MMM,
this article aims to enable marketing scholars to gauge
strengths and weaknesses and facilitate dialogue and
collaboration towards vetting and testing these pack -
ages. It is a narrative review and conceptual integration
of recent developments in open-source m/MMM and
bridges marketing practice and scholarship to guide
and improve applied marketing measurement to meet
advertisers’ measurement needs [ 16]. A main goal of
the paper is to facilitate rigor in m/MMM while it is
becoming increasingly accessible to practitioners that
want to assess the incremental effect of marketing
activities and optimize future marketing decisions. We
also raise normative questions for scholars about the
role of transparency, model vetting, and automation in
probabilistic marketing measurement.
The article proceeds with conceptual and practical back-
ground on m/MMM before it provides a practice-oriented
overview of the different packages. We then discuss the
challenges and opportunities that come with “packaged up”
m/MMM and conclude with an outlook on future directions
in open-source m/MMM.
prerequisite for investment. If digital advertisers are unable to mea -
sure their advertising on these platforms (because the deterministic
attribution approaches they relied on are increasingly faulty and
obsolete), they may cut their advertising spend. Another explanation
is that the platforms could embrace methodological approaches in
their open-source packages that evaluate advertising on their plat -
form more favorably. In our review and testing of the packages, we
could not find evidence for this latter explanation.
2 Conceptual Background
2.1 The Origins of m/MMM and Its Renaissance
Media mix modeling (mMM), a narrower subdomain of
the broader marketing mix modeling (MMM), focuses spe -
cifically on media mix allocations, whereas MMM encom -
passes all “4Ps” of the marketing mix [ 1].2 Almost as old
as the term marketing mix itself that was coined by Neil in
1949 [2], MMM became a predominant analytical approach
to propose strategic refinements to a company’s market -
ing actions in pricing, promotion, product and distribu -
tion [3–5, 17–21]. In the historic marketing data landscape
where individual consumers could not be deterministically
tracked across media and company properties, m/MMM
(so, the combined practice of mMM and MMM) leverages
variation in sales and marketing mix data over time to esti -
mate the effects of a firm’s marketing strategy choices on
relevant outcomes. Advanced m/MMM integrates short-
term and long-term effects and models competitor actions
and dynamic synergy starting from an interactive market
system framework ( [ 22] Pauwels 2004; [ 23]). To reduce
bias and increase precision, models can also be calibrated
against experimental estimates [ 19, 21], albeit it is unclear
how widely adopted this practice is [24].
Recent accelerations in the rollout of privacy-enhancing
technologies [ 6, 7] are fundamentally changing the data
landscape in online advertising, challenging deterministic
measurement approaches and bringing traditional probabi -
listic techniques en vogue again [1]. While traditional large
advertisers and brands are accustomed to, and tend to have
deep expertise in, m/MMM, many digital-first and interac -
tive advertisers have no experience with these models and
often lack the resources to build the necessary expertise and
systems internally [11, 25]. These advertisers often heavily
relied on digital advertising [ 26] and its increasingly dated
measurement methods such as deterministic decision rules
or digital attribution requiring cross-platform tracking, e.g.,
via third-party cookies [27, 28]. The property of m/MMM to
not require user-level data is a foremost reason for its grow-
ing popularity among these smaller and midsize interactive
advertisers [1].
2.2 Incrementality and Choice of Counterfactual in
Marketing Measurement
Firms want to measure the incremental impact of their media
spending on outcomes (e.g., sales) to guide their future
budget and allocation decisions. Incremental outcomes are
2  We follow Arora et al. [1] and adopt m/MMM as an umbrella term
comprising both media and marketing mix modeling, so both mMM
and MMM.
1 3
    3  Page 2 of 16

Customer Needs and Solutions            (2026) 13:3
outcomes the firm would not have gotten without the ads,
i.e. the counterfactual. This counterfactual could be regions
where the ads did not run (geo-experiments), consumers
who were not exposed to the ad (RCTs), or time periods
when the firm spent less, more, or no money on the ad
strategy in question (m/MMM). Because the counterfac -
tual should be as similar as possible to the actual situation,
the choice in practice comes down to which comparison is
most feasible and cost effective. RCTs require a random -
ized hold-out sample of unexposed consumers, and cluster
level-randomized experiments of unexposed clusters (e.g.,
regions), while m/MMM requires variation of ad spending
in past periods of the historical data and control variables
to account for other ways these past periods differed from
each other. Modeling approaches that integrate variation
over time and from experiments can be particularly power -
ful [19, 21, 29–31].3
2.3 The Related Marketing Analytics Process
For effective data-driven decision-making in real-world
marketing operations, m/MMM needs to be embedded in
an analytics process that informs relevant actions, is under-
stood and agreed upon by key stakeholders, and updated
regularly. Marketing scholars may be less familiar with this
important process, which is scarcely discussed in academic
papers. We draw on Runge et al. [11] to conceptualize such
a marketing analytics process, as compatible with the open-
source implementations of m/MMM. Figure 1 depicts an
iterative five-step process that starts with the firm acting (1)
in the marketplace with media/marketing mix policy π (t),
running calibration experiments as planned, and making use
of suited attribution models. The media/marketing mix pol-
icy can be expressed as specific levels of spend allocated to
available media channels, tactical options within channels,
other marketing actions, planned calibration experiments,
and adopted attribution models, if any.
The firm then uses the observational, experimental, and
attribution data (in and up to period t) to estimate (2.1)
models of the causal effects of marketing actions on demand
with different specifications. We frame this as the estimation
of a set of specified models Mi (t), some or all of which
may include calibration against experimental or attribu -
tion results via priors (in Meridian [ 13]) or multi-objective
estimation (in Robyn [ 10]). The packages encourage users
to consider a set of model diagnostics to assess statistical
fit and business sensibility. We call this step inference as
modelers are asked to ensure that the specified model(s)
3  In m/MMM, this is often called calibration. Observational models
are “calibrated” against results from experiments that can be expected
to provide unbiased (albeit often only short-term) estimates of mar -
keting effectiveness. See Runge et al. [41] for a hands-on guide.
produce results that reasonably infer (2.2) the causal effects
of the firm’s media/marketing mix policy. If the diagnostics
do not look reasonable, a new set of models Mi+1 (t) is
specified and estimated (2.1), to then look at diagnostics and
infer (2.2) again (motivating our choice of a two-way arrow
between these steps).
In the third step, the firm needs to select a consensus
model m (t) that it believes to accurately model and reflect
the incremental effects of its advertising on the considered
outcomes, taking into account both statistical and business
considerations. This model serves to prescribe a new media/
marketing mix policy [13, 15] or budget allocation [10] for
the net period t +1 . Then, the modeling chain repeats.
For each step, the figure lists its key output to be passed
on to the next step, the key (human) skills needed to succeed
with the step, and the key risk introduced by automation that
needs to be mitigated through supervision by human exper-
tise. The cadence for iteration can be monthly, quarterly, and
sometimes weekly or half-yearly. Iteration cycles can be
shorter for direct response-focused interactive advertisers
and longer when longer-term efforts such as brand building
are an important part of the firm’s marketing strategy.
The aim of this conceptualization of the m/MMM analyt-
ics process is to connect the discussed open-source pack -
ages to marketing analytics practice and provide a basis for
structured analysis and comparison of the packages. Case
in point, Appendix A illustrates how the analytics process
in Fig. 1 maps onto the computational workflow of Robyn,
including code examples. We also refer the interested reader
to Runge et al. [11] that provides a more detailed exposition,
including best practice recommendations and six mini case
studies, in Sect. 4 of that paper.
3 Open-Source m/MMM Packages
3.1 A Practice-Oriented Overview of the Packages
There currently are four prominent open-source m/MMM
packages: Meridian [ 13], LightweightMMM [ 12], Robyn
[10], and PyMC-Marketing-mmm [ 15]. In our further
discussion, we focus on Meridian, Robyn, and PyMC-
Marketing-mmm as Meridian has replaced Lightweight -
MMM, which is no longer actively supported [ 12]. Table
1 compares the packages on key computational elements as
needed to support the analytics process depicted in Fig. 1.
Meridian [13], Google’s latest causal inference-based m/
MMM framework [14] and PyMC-Marketing-mmm [15] use
a Bayesian modeling approach that allows users to incorporate
prior knowledge, e.g., experiment results. One of the strengths
of hierarchical Bayesian models is their ability to leverage
variation across geographies or other relevant hierarchies,
1 3
Page 3 of 16     3

Customer Needs and Solutions            (2026) 13:3
for realistic estimations of long-term campaign effects.
Like Meridian, it does not allow for flexible estimation of
each period’s effect. Since it automates many aspects of m/
MMM, Robyn is ideal for practitioners and marketers who
need quick insights with minimal manual intervention. It
also offers model calibration against experiment results
via multi-objective optimization that is relatively easier to
use compared to Meridian’s and PyMC-Marketing-mmm’s
approach via priors. This approach is, however, also much
less understood and vetted (a point we will return to later).
PyMC-Marketing [15] offers a fully Bayesian and highly
customizable m/MMM solution with custom priors and
hierarchical models. 5 Unlike Robyn, which is optimized
for automation and ease of use, PyMC-Marketing-mmm is
geared toward advanced practitioners who want custom-
built MMM models to fit specific business needs. While
Robyn and Meridian assume static effects for the estimation
5  Hierarchical (multi-level) models estimate the same effect for many
groups (countries, regions, campaigns, cohorts, etc.) jointly instead of
separately. Each group has its own parameter, but those parameters
are regularized toward a common distribution, so groups with little
data “borrow strength” from groups with more data. That regulariza-
tion is often termed partial or hierarchical pooling.
making them a powerful tool for marketers running campaigns
across multiple regions and wanting to account for related
heterogeneity. The packages also include built-in support for
return-on-investment (ROI) estimation, trend and seasonality
adjustments, adstock and saturation4, and budget optimization
[33, 34]. Given their relatively higher level of customizabil-
ity, Meridian and especially PyMC-Marketing-mmm are best
suited for advanced users and marketing scientists.
Robyn [ 10] is the first-to-be-released and arguably the
most automated of the solutions. Unlike Google’s and
PyMC-Marketing-mmm’s Bayesian frameworks, Robyn is
based on Ridge regression [35] with hyperparameter tuning
via evolutionary algorithms, requiring less advanced sta -
tistical expertise to use the package. Robyn is particularly
useful for companies that need fast and automated media
mix analysis and budget allocation recommendations. Its
built-in carryover and diminishing returns modeling allows
4  In m/MMM, saturation describes how you model diminishing
returns to additional spend in a channel and adstock is a transforma -
tion of media spend or other input variables like impressions, views,
or clicks that addresses that (1) yesterday’s advertising still has some
effect today (carryover) and (2) the effect of past advertising gets
smaller as time passes (decay).
Fig. 1 A conceptualization of the analytics process that open-source m/
MMM packages can be embedded in, adapted from Runge et al. [ 11].
The process involves the steps (1) act, (2) estimate and infer (where
iterative model tuning, calibration, validation and backtesting play an
important role, hence the bidirectional arrow), (3) select, (4) prescribe
– and act again in the next period. For each step, we note key output,
key skills needed on the user(s)’ part, and the key risk originating from
automation and “packaged up” m/MMM

1 3
    3  Page 4 of 16

Customer Needs and Solutions            (2026) 13:3
allowing users without deeper statistics or marketing ana -
lytics knowledge to run an end-to-end m/MMM modeling
chain within less than a day. A notable strength are the con-
cise but comprehensive diagnostic one-pagers it outputs for
model candidates. However, the risk of model misspecifi -
cation from automation is relatively high. For practitioners
needing fast and automated insights and who have more
basic data science knowledge and coding skills, it is cur -
rently the best choice. Meridian provides the most “pack -
aged up” bayesian solution. Users need a robust command
of data science coding to adopt it successfully and can do so
within several days based on the authors’ experience. Some
modeling choices such as default uniform priors facilitate
broad adoption but introduce risk of misuse in the authors’
opinion. For advanced users comfortable with bayesian
time period, PyMC-Marketing-mmm allows to specify a
time-varying media baseline [ 32]. Its advanced customiz -
ability makes it most suited for researchers and profession -
als with strong Bayesian modeling expertise.
At the budget allocation/optimization step (step 4 per
Fig. 1), Meridian offers the most comprehensive set of
options, including: (i) working from a set budget to maxi -
mize ROI or another incremental KPI; (ii) working from a
flexible budget, targeting a set minimum ROI; (iii) working
from a flexible budget, targeting a set marginal ROI [ 36].
Robyn currently supports the first two options, and PyMC-
Marketing-mmm requires customization to support budget
allocation/optimization.
Table 2 compares the three packages on key usabil -
ity considerations. Robyn is the most automated solution,
Computational
element
Robyn Meridian PyMC-Marketing-mmm
2.1. Estimate
Channel / media
aggregations
Manual Manual Manual
Dynamic effects, sat-
uration, seasonality
Geometric and Weibull
adstock; saturation using
S-curves; seasonality via
time-series decomposition
Geometric and binomial
adstock; saturation
using Hill functions;
and seasonality through
time-varying intercepts
Customizable adstock
and saturation functions;
user-defined seasonality
modeling
Multi-collinearity Regularization through
Ridge regression
Bayesian priors to miti-
gate collinearity
Manages via Bayesian
priors and model structure
Reach & frequency
data
Supports reach and fre-
quency data
Supports reach and
frequency data
Requires manual
integration
Calibration
(experimens)
Calibration via multi-
objective optimization
(MAPE.LIFT)
Through priors Through priors
Calibration (business
plausibility)
Calibration vis-à-vis
business constraints via
multi-objective optimiza-
tion (Decomp.RSSD)
Through priors Through priors
Long-term effects
(baseline models)
Through adstock and satu-
ration curves
Via adstock weighting Requires explicit model-
ing of long-term effects
Dynamic coefficients Does not support time-
varying coefficients
Does not support time-
varying coefficients
Allows time-varying
media baseline [32]
Channel interactions Limited support; requires
manual feature engineering
Limited support;
requires manual feature
engineering
Limited support; requires
manual base code
adaptation
Hierarchical
modeling
No native support Hierarchical geo-level
modeling
Fully supports hierarchi-
cal modeling structures
2.2. Infer + 3. Select
Automated diagnostic
output
Model and convergence
diagnostics in one-pagers
Comprehensive diag-
nostics and uncertainty
quantification
Custom diagnostic plot-
ting and analysis (via
one-liners)
Model refresh /
updating
Model retraining only on
incremental data
Continuous modeling
with new data
Updating through model
retraining
4. Prescribe
Budget allocation /
optimization
Built-in budget allocator Budget optimization
tools with scenario
analysis
Advanced custom imple-
mentations possible
Scenario planning Built-in tools User-defined hypotheti-
cal scenarios
User-defined simulations
Table 1 Comparison of the
leading open-source m/MMM
packages on key computational
elements that underpin the analyt-
ics process in Figure 1 (see first
column for a mapping). None of
the packages currently support
implementing the prescribed
media/marketing mix policy,
running experiments, or attribu-
tion modeling, so step 1 “Act”
is missing from this table. Step
2a receives comparatively most
attention as risk from automa-
tion is highest per Figure 1, so
scholarly study and scrutiny of
what the packages offer here is
particularly important.

1 3
Page 5 of 16     3

Customer Needs and Solutions            (2026) 13:3
forked 416 times [10],7 and has seen more than 121,000 down-
loads [37]. The package is available in both R and Python and
distributed under the MIT open-source license which permits
private and commercial use free of charge.8
Robyn is designed as a “semi-automated” MMM solu -
tion – once the data is prepared, it automates model building
end-to-end: transforming variables, running hyperparameter
optimization for adstock and saturation, and outputting a set
of Pareto-optimal models and diagnostics. It also automates
common adjustments like detecting seasonality and provides
built-in model selection support. This high level of automation
means analysts do not need to manually tune lag or diminish-
ing return parameters, but the package identifies those.
This level of automation is novel in m/MMM specifically
and in causal inference more generally. Some modeling com-
ponents in the package further are unvetted. Two of these
7  PyMC-Marketing has 83 contributors, is starred 987 and forked 341
times, Meridian (with 13 contributors) 1200 and 209 times respec -
tively, per their Github pages as of November 27, 2025. Note that
PyMC-Marketing comprises other functionality beyond m/MMM,
which complicates this comparison, especially when it comes to the
number of contributors.
8  The authors recommend using the R version of Robyn – it was
more stable than the Python version when they used both in the first
half of 2025.
statistics, PyMC-Marketing-mmm provides the most flex -
ibility. To leverage it for a full m/MMM modeling chain,
users will need to customize it and be able to write custom
code. Completion of a first full modeling run can take up to
two weeks based on the authors’ experience.6 To effectively
do so, users need a good handle of bayesian modeling, espe-
cially priors. Appendix B provides an adoption guide for
advertisers who are new to m/MMM, helping them select
the appropriate package based on their organizational con -
tingencies and use cases.
3.2 The Most “Packaged Up” Solution: Robyn
Meta Platforms’ m/MMM package Robyn was the first pack-
age to be released and, as we assessed through use of all pack-
ages, offers the highest degree of automation and shortest,
easiest path to estimating a full model among the available
packages. As of November 27, 2025, it is being developed
by 34 contributors, starred on Github more than 1,400 times,
6 A friendly reviewer commented that the "two weeks" claim may
conflate "learning Bayesian statistics" with "using the package." We
agree that the two are conflated here to some extent. We tried to give
estimates for a novice user with advanced (but not expert) general
statistics knowledge.
Robyn Meridian PyMC-Marketing-mmm
Ease of use High; users need to know
basic R or Python and
consult the documentation
to adopt; full modeling
run possible within a day
(after data preparation is
completed)
Medium; users need good
command of Python and
a robust understanding of
Bayesian modeling; full
modeling run possible within
several days
Comparatively low;
users need good com-
mand of Python, a
robust understanding of
Bayesian modeling; full
modeling run possible
within one to two weeks
Degree of
automation
High; after data aggregation,
users can run an end-to-end
modeling chain even with-
out deeper understanding of
regression and statistics
Medium; human effort needed
repeatedly along the modeling
chain; chosen defaults make
more advanced modeling ele-
ments relatively easy to handle
for inexperienced users
Comparatively low;
users need to be able to
write custom code to run
a full modeling chain
Risk from
automation
High; risk of model mis-
specification is relatively
high; users need to carefully
consult documentation to
correctly read diagnostic
one-pagers
High; default uniform priors
make Bayesian modeling
relatively straightforward but
increase risk of improper use
and model misspecification
Low; users without
robust understanding
of statistics and coding
are unlikely to adopt
successfully
Notable
strengths
Concise but comprehensive
diagnostic one-pagers;
end-to-end automation
with minimal human effort
needed; the overall most
“packaged up” m/MMM
solution
Most “packaged up” Bayesian
m/MMM solution; makes a
Bayesian framework broadly
accessible, risk of misuse is
somewhat elevated as a result
Highly customizable and
extendable; can provide
a robust basis for
advanced modeling solu-
tions; part of the broader,
large and active PyMC
open-source community
Target users Small and midsize advertis-
ers with limited propri-
etary modeling experience
and marketing analytics
capabilities
Small and midsize advertisers
with more advanced market-
ing analytics experience;
advertisers with existing m/
MMM experience but new to
Bayesian modeling
Advertisers of all sizes
with substantial market-
ing analytics capabilities
and initial proprietary
modeling experience
Table 2 Comparison of the
leading open-source m/MMM
packages on key usability con-
siderations; appendix B provides
an adoption guide, substantiating
how target users were selected in
this table.

1 3
    3  Page 6 of 16

Customer Needs and Solutions            (2026) 13:3
or find insufficient buy-in with stakeholders. Different pack-
ages prioritize customer needs differently: Robyn is argu -
ably the most automated solution, easiest to adopt, and
hence democratizes access to m/MMM most broadly. On
the other hand, this easy accessibility may lead to misuse
and ill-informed decisions because users’ understanding of
the underlying methodologies is too limited. PyMC-Mar -
keting offers the most advanced and flexible solutions but
requires much more modeling proficiency from its users.
Meridian finds a middle ground. In conjunction, the differ -
ent packages serve a multitude of different customer needs
along a spectrum of sophistication. The opportunity here –
that is already realizing itself – is much broader access to
and adoption of m/MMM across small and midsize adver -
tisers, especially interactive digital-first ones.
Second, a key challenge for marketers is often the orches-
tration and integration of different measurement methods.
Information from attribution models, m/MMM, experi -
ments, and other sources needs to be integrated and aligned
to optimally support marketing decision experiments [ 19,
21]. A related challenge is how to integrate open-source m/
MMM with these other decision support tools. The oppor -
tunity here is to foster best practices in calibration and inte-
gration with a suite of measurement tools through built-in
workflows in the packages, detailed documentation, and
educational offerings [11, 41].
Third, a challenge is to vet and test new computational
approaches and pathways that some open-source commu -
nities have embarked on. E.g., Robyn applies optimization
across three distinct objectives, balancing statistical error
against the data, statistical error against trusted results from
other sources, and business error (by formalizing a preference
computational features warrant specific discussion.9 The first is
that Robyn currently works merely from time series of outcome
and media data, without consideration of additional cross-sec-
tional dimensions such as geographic clusters [38]. While this
approach facilitates data preparation, easy model estimation,
and broad accessibility, it can limit customer and advertising
insights. Meridian and PyMC-Marketing-mmm accept panel
data with cross-sectional hierarchies such as geo clusters. The
second component is the multi-objective optimization that is
available in Robyn’s model estimation step. Robyn allows users
to set two objectives in addition to (statistical) minimization of
NRMSE: avoidance of extreme results (producing more busi-
ness-plausible results) and minimization of mean absolute per-
centage error (MAPE) against estimates from experiments or
other trusted sources such as established attribution models [19,
21, 27, 39]. This approach is different from the other discussed
packages that use Bayesian estimation and priors to calibrate
models against estimates from experiments.
This multi-objective optimization essentially performs
model selection by generating a Pareto frontier of models
that trade off statistical fit (NRMSE), complexity (Decomp.
RSSD), and calibration (MAPE.LIFT).10 The package then
recommends the models closest to and on the Pareto frontier
to the user for review in the inference step (2.2) per Fig. 1.
The user might select the model that makes the most business
sense, e.g., avoiding a model that unrealistically attributes
zero effect to a major channel. While providing users with
a model for decision-making, this approach does not output
a single definitive model but a set of candidates, reflecting
ambiguity in model specification. This approach in Robyn
epitomizes a key challenge in “packaging up” mMM: find -
ing the right trade-off between automation and easy acces -
sibility on the one hand and customizability and rigor on the
other – which we will discuss in greater detail now.
4 Challenges and Opportunities in Open-
Source Marketing Mix Modeling
In this section, we comment on challenges and opportunities
offered by the developments in the open-source m/MMM
space. We thereby select challenge-opportunity pairs of
particular relevance to marketing scholars and analysts to
ensure the rigor and reliability of the developed methodolo-
gies. Table 3 provides an overview.
First, the trade-off between accessibility/automation and
rigor/customizability has long permeated the world of mar-
keting effectiveness [ 40]. Automation can generate large
time savings, but overly simplistic models can be imprecise
9  For a comprehensive introduction to Robyn’s architecture, see
Runge et al. [11].
10  See Runge et al. [11] for details.
Table 3 Challenges and opportunities in open-source m/MMM; prac -
tice-academy collaboration can help materialize the opportunity paired
to each challenge.
Challenge Opportunity
Finding the right trade-off
between automation and easy
accessibility versus customiz-
ability and rigor
Provide robust customer insight
and marketing strategy analytics
in a privacy-first era; democratize
access to m/MMM, especially for
small and midsize advertisers
Integrating m/MMM with other
marketing decision support tools
such as attribution models and
testing frameworks
Fostering best practices, e.g., in
calibration and integration with
a suite of measurement tools,
through built-in workflows,
detailed documentation and
educational offerings
Vetting and testing novel
approaches prior to broad
adoption by the open-source
community, e.g., Robyn's multi-
objective optimization
Harnessing the power of open-
source development, incor-
porating methodologies with
cross-disciplinary origin in m/
MMM
Ensuring rigorous use,
adequately quantifying and
communicating uncertainty
Facilitating good organizational
behaviors and outcomes through
package design
1 3
Page 7 of 16     3

Customer Needs and Solutions            (2026) 13:3
or unknown products and brands with little or no organic dis-
covery. The opportunity here is to facilitate good organizational
behaviors and outcomes through smart intentional package
design [11]. A close dialogue between marketing academics
and open-source m/MMM communities can be a fruitful path-
way to achieve a convergence between long-established and
-documented best practices and open-source development.
5 Outlook
In the past, the technology industry has witnessed a series
of transformative open-source “wars,” where community-
driven, transparent alternatives have challenged, and in
some domains displaced, long-standing proprietary solu -
tions [51]. These clashes – ranging from operating systems
(Linux vs. Windows), web browsers (Firefox vs. Internet
Explorer/Chrome), to infrastructure tooling (Kubernetes vs.
proprietary orchestrators) – have shaped the technological
foundations of today’s digital commerce, as many domains
in computer science and engineering have seen open source
triumph as a de facto standard.11 In contrast, marketing ana-
lytics – particularly m/MMM – is often still the domain of
closed, consultant-driven models. As a result, many compa-
nies continue to base marketing and media mix decisions on
multitouch attribution (MTA), including last-click methods
shown as inferior by several authors (e.g., [27, 28, 45, 46]).
By making state-of-the-art methods freely available, open-
source initiatives lower barriers to adoption, enhance trans-
parency, and enable reproducibility. They enable small and
midsize advertisers to adopt models that have thus far often
been beyond their reach and can accelerate the diffusion of
innovations in modeling approaches. This democratization
of m/MMM has the potential to improve how organizations
learn from data, design more relevant marketing strategies,
and respond more quickly to shifts in customer preferences.
It is all the more important given increasing demands for
privacy-enhancing technologies by platforms and regulators
that make deterministic attribution approaches – that many
digital-first advertisers relied on – increasingly obsolete [6, 7]
Open-source m/MMM has the potential to transform mar-
keting analytics and model building beyond small and midsize
companies. Past research has documented that open source
can lead firms more broadly to adopt levels of openness that
were previously unthinkable [52]. They thereby strategically
and selectively reveal parts of their proprietary development
effort, eliciting informal development support from other
firms; and, applied deliberately, the benefits of open develop-
ment via selective revealing can dominate. Strategic openness
11 Special thanks to William Grosso for a comment during friendly
review that encouraged us to relate the open-source developments in
m/MMM to other open-source “wars.”
for non-extreme outcomes in the estimation step). This
approach is novel and interesting as business plausibility is a
criterion often used in model evaluation as much as statistical
fit [42, 43]. On the other hand, this approach is unvetted and
a nontrivial degree of the resulting models may not approxi-
mate a reasonable data generating process but something
more arbitrary. Thus, while Robyn’s functionality provides
flexibility to users in an otherwise highly automated package
(a strength), it entails ambiguity in uncertainty specification
and methods that have not been rigorously studied. A risk
here is that Robyn evokes a sense of confidence in the results
that is not actually backed by the data and deep statistical
understanding on the side of the package’s users. The oppor-
tunity however may be equally large: Marketers can harness
the power of open-source development to incorporate new
methodologies with cross-disciplinary origin in m/MMM.
Fourth, m/MMMs are modeling complex and dynamic
market processes. Representing uncertainty appropriately and
ensuring rigorous use of open-source m/MMM is challenging.
Two key issues are often at play here: (1) Is there enough varia-
tion to estimate the associations between media spend and out-
comes? (2) Can the estimates be interpreted as causal? As to the
first issue: because the variation in marketing allocations over
time can be insufficient to generate well-identified estimates
[1, 42], it is important to consider intentionally amplifying it.
This can be achieved by regularly implementing well-thought-
out tactical changes and recording these changes in the mMM
data and taking action on mMM results, i.e., changing media
spend allocations. A further concern is the strategic timing of
advertising that tends to intensify around high-demand holi-
days. Parameters and data addressing systematic demand shifts
should hence always be included in the estimation. Speaking to
the second issue, the estimation of causally interpretable esti-
mates is a critical concern in m/MMM. Observational studies
of individual behavior are particularly prone to overestimat-
ing the causal impact of advertising due to “activity bias” and
“user-induced endogeneity” [44]. Customer-initiated ads [45]
are triggered by visiting a particular website (page), making
it challenging to attribute the resulting purchase to the ad ver-
sus the consumer self-selection. In aggregate models, a similar
bias arises from the strong correlation between many on- and/
or offline activities, complicating the establishment of cause-
effect relationships and potentially leading to systematic mis-
estimation of advertising effects.
To mitigate both types of risks, we encourage validation of
m/MMM results with experimental methods [19, 21, 29], such
as field experiments (e.g., [30, 31]), advertising experiments
[39, 46–49], or lower-level attribution results that the organiza-
tion has found to reflect incremental effects [27, 28, 50]. For
instance, last click-attributed outcomes may approximate the
causal incremental effects of campaigns, particularly when
baseline effects are minimal or absent, as might occur with new
1 3
    3  Page 8 of 16

Customer Needs and Solutions            (2026) 13:3
channels with high model uncertainty, to test dimin -
ishing returns and to calibrate model estimates. Open-
source models, and related artificial agents per the first
point in this list, can lead the way here. Reinforcement
learning can extend the recommended Model-Experi -
ment-Model-Experiment (MEME) iteration applied in
practice prize papers [29–31].
 ● It would be useful if the packages provided tools for
sensitivity analysis to evaluate how much unobserved
confounding or violations of key assumptions would
change recommendations. In the absence of theoretical
guarantees, such tools can provide confidence when us-
ing observational data to guide decision making.
 ● Relatedly, more comprehensive and explicit validation,
e.g., via stability checks and parameter recovery on sim-
ulated data, built into the packages could help provide
more robust modeling results.
 ● Finally, flexible long-term effects, competitive interactions
and dynamic synergy are absent from the currently avail-
able open-source packages but can yield important insight
in dynamic marketing environments [18, 23, 34, 60, 61].
We hope that the overview provided in this paper is a useful
starting point for interested scholars and practitioners and
can encourage collaboration, study, and contribution.
Appendix A: Robyn Workflow and Code
Example
This appendix demonstrates how the analytics process shown in
Fig. 1 can map onto the workflow of an m/MMM open-source
package. It adapts the workflow and code examples from the
package Robyn as presented in Appendix A of Runge et al.
[11]. Runge et al. [11] also provide a detailed walk-through of
the package and list six brief case studies from companies that
successfully adopted Robyn for their measurement.
The workflow provides a simplified overview of the
steps involved in a complete modeling run of Robyn, on the
simulated data available within the Robyn R package “dt_
simulated_weekly” [ 10]. The workflow comprises input
and output, from data loading to model estimation, budget
allocation, and model refresh. In the version here, we added
starred lines indicating how the workflow steps map to the
steps of the m/MMM modeling chain in Fig. 1.
Robyn’s documentation provides additional and deeper
walk-throughs and examples, e.g., at  h t t p  s : /  / g i t  h u  b . c  o m / f  a c e
b o o  k e x  p e r  i m e n  t a  l / R  o b y n  / b l  o b /  m a i n / d e m o / d e m o . R [10] and
at  h t t p  s : /  / d r i  v e  . g o  o g l e  . c o  m / fi   l e  / d /  1 L Y M  9 g  2 x P  5 Z G h  m G X  l c
Q  f - - 3 E y X U a M E 6 g 6 / v i e w ?   t s = 6 6 b 0 a b 0 9 for a demo video.
Meridian and PyMC-Marketing offer similarly detailed doc-
umentation and guidance at  h t t p  s : /  / g i t  h u  b . c  o m / g  o o g  l e /  m e r  i
can then develop into a new dimension of competition between
firms [53]. Such developments, if materializing, could bring
important innovations – e.g., external validation, faster feature
development, shared benchmarks, standardized pipelines – to
marketing analytics and ensure that they disseminate widely.
Note that this review is limited to publicly available
documentation and supported features as of November 27,
2025. We focus on core modeling features relevant for typi-
cal in-market users. As these packages are under continuous
development, new capabilities may emerge rapidly. At this
point, it is hard to anticipate whether open-source m/MMM
will become a lasting and integral part of applied marketing
measurement. Each package is likely to find its specific use
cases as shown in Table 2 and discussed in the text. E.g.,
Robyn may serve small and midsize businesses looking for
ease of use and automation and to cross-validate and tri -
angulate other modeling approaches. Meridian may serve
somewhat more sophisticated advertisers with interest in
Bayesian modeling. PyMC-Marketing and the wider PyMC
umbrella package may be a backbone for specialized and
tailored in-house models with custom extensions.
Marketing scholars can contribute to the open-source
development efforts directly or collaborate with practitio -
ners to help shape the future of applied marketing measure-
ment and define rigorous and valid best practices generally,
and for different verticals and organizational contingencies
specifically. We believe that a few areas are worthy of par -
ticular attention from scholars:
 ● Given recent developments in large language models
(LLMs) and LLM-based chatbots, LLMs trained on a
corpus including open-source m/MMM code and docu -
mentation can be expected to be able to apply this knowl-
edge and to estimate and output models as prompted by
the user. We believe this to be an area of particular inter-
est to scholars who could train related models and de -
sign m/MMM agents. This would also facilitate testing
and vetting of the ongoing developments in open-source
m/MMM via automation.
 ● Relatedly, methods from machine learning and artificial
intelligence provide interesting angles for innovation in
m/MMM [17, 54], e.g., to include unstructured, text, im-
age, audio, and video data in models directly [55].
 ● Third, extended functionality to estimate dynamic coef-
ficients, e.g., via Gaussian processes and with long-term
decomposition [ 15, 32, 56, 57], would be useful. Re -
lated models would be particularly useful to understand
and model long-term trends and brand effects in a firm’s
advertising [58].
 ● Fourth, m/MMM in general needs a deeper integration
with experimentation and other measurement sources
[19, 21, 59, 60], including setting up experiments for
1 3
Page 9 of 16     3

Customer Needs and Solutions            (2026) 13:3
Step 0: Setup environment.
 ● Input/Steps: Install Robyn and load into environment.
 ● Output: Robyn R package is downloaded installed. This
step ensures the latest stable (CRAN) or latest experi -
mental version of Robyn is used for compatibility and
new features.
 ● Example Command:
d i  a n / b  l o  b / m  a i n /  d e m  o / M  e r i  d i a  n _ G e  t t  i n g _ S t a r t e d . i p y n b and
h t t p  s : /  / g i t  h u  b . c  o m / p  y m c  - l a  b s / p y m c - m a r k e t i n g respectively.
Work flow and code example for Robyn 3.11.1.
MODELING STEPS ESTIMATE AND  INFER  PER
FIG. 1.
install.packages("Robyn") #Install thel atest stable versionf romC RAN
#r emotes::install_github("facebookexperimental/Robyn/R")# Installt he latest dev versionf romG itHub
library(Robyn)
 ● Input: Dataset, holiday data, and model configuration
parameters.
 ● Output: InputCollect object containing all model speci -
fications. This sets up the modeling system with all nec-
essary variables and configurations for Robyn MMM
analysis.
 ● Example Command:
Step 1: Load data.
 ● Input: Load in own or load the demo dataset dt_simu -
lated_weekly & demo holiday dt_prophet_holidays.
 ● Output: Data loaded into the R environment. In this step,
user loads into Robyn all the necessary data for model
building.
Step 2: Model specification.
1 3
    3  Page 10 of 16

Customer Needs and Solutions            (2026) 13:3
it is set to the range of c(0, 1) by default in hyperpa -
rameters and will be scaled to the proper altitude with
lambda_max and lambda_min_ratio.
Step 4: Model Calibration / Add Experimental Input.
 ● Input: Calibration data to align model outputs with
other trusted outcomes (from experiments or attribution
models).
 ● Output: Adjusted model parameters to reflect real-world
effects, Calibration helps in adjusting the model based
on ground truth data, enhancing predictive accuracy.
 ● Example Command:
Step 3: Define and Add Hyperparameters.
 ● Input: Definitions of model behavior parameters.
 ● Output: Configured hyperparameters added to InputCol-
lect. Hyperparameters like adstock and saturation define
how marketing inputs decay over time and how they
saturate, impacting model accuracy.
 ● Example Values: facebook_S_thetas = c(0, 0.3): Range
for the decay rate of Facebook spend, allowing for quick
to moderate decay.
 ● Note on regularization via ridge regression: Lambda
is the penalty term for regularised regression. Lambda
doesn’t need manual definition from the users, because
1 3
Page 11 of 16     3

Customer Needs and Solutions            (2026) 13:3
MODELING STEP SELECT PER FIG. 1.
Step 6: Select and save the model.
 ● Input: OutputModels object.
Step 5: Build initial model.
 ● Input: InputCollect object.
 ● Output: OutputModels object containing model results
and diagnostics.
 ● Output: Selected model saved and export. This steps
enables the user to choose the model that best fits their
business context and save it for future use.
 ● Example Command:
1 3
    3  Page 12 of 16

Customer Needs and Solutions            (2026) 13:3
 ● Output: Budget allocation recommendations. The bud -
get allocator provides insights on how to allocate mar -
keting budget effectively based on model predictions.
 ● Example Command:
MODELING STEP PRESCRIBE PER FIG. 1.
Step 7: Get budget allocation.
 ● Input: Selected model and budget scenarios.
FURTHER RELEV ANT COMPONENTS.
Step 8: Model refresh.
 ● Input: JSON file of a previously exported model, new
data.
 ● Output: Updated model based on new data. Regular
updates to the model ensure it remains accurate as new
data becomes available.
 ● Example Command:
1 3
Page 13 of 16     3

Customer Needs and Solutions            (2026) 13:3
main driver of adoption among small and midsize businesses.
In principle, all packages can be extended into MMM (so, mar-
keting mix modeling) by including data on relevant marketing
actions. As PyMC-Marketing-mmm offers the most flexibility
and customizability, it also provides the most comprehensive
basis for extension into MMM. In reality, mMM and MMM
will often coexist and complement each other, e.g., with mMM
informing more granular and tactical advertising decisions and
laddering up into broader and more strategically oriented MMM.
Here is a step-by-step decision guide for an advertiser
looking to adopt mMM for the first time via one of the pack-
ages. mMM should thereby complement, and not replace,
existing and other decision support solutions like attribution
models and advertising experiments. mMM can provide
more strategic guidance at lower decision cadence and pro-
vide a longer term “source of truth” that incorporates and is
calibrated against the other methods [41].
1) Have you been advertising on
more than two channels for more
than a year (better: two years)?
Yes: continue to
next row
No: use attribu-
tion models and
ad experiments
to inform your
advertising
operations;
reconsider m/
MMM when you
have reached suf-
ficient scale and
data availability
2) Do you have reliable adver-
tising spend and sales data per
day or week for at least a year
and at least two channels?
Yes: continue to
next row
No: work to
gather and pre-
pare data first
3) Do you have in-house
marketing analytics capabili-
ties and proprietary modeling
experience?
Yes: continue to
next row
No: use Robyn
4) Are you familiar with Bayes-
ian modeling?
Yes: continue to
next row
No: use Merid-
ian and/or
Robyn
5) Do you have advanced mod-
eling and Bayesian experience?
Yes: continue to
next row
No: use
Meridian
6) Do you have custom use
cases and the ability to write
custom code (e.g., for budget
optimization and allocation)?
Yes: use PyMC-
Marketing-
mmm and
continue to next
row
No: use
Meridian and
continue to
next row
7) Are you looking to inform
marketing decisions and strat-
egy beyond advertising?
Yes: prepare
data on rel-
evant market-
ing actions
and include in
modeling
No: revisit if
this changes
Acknowledgements The authors are grateful to Elea McDonnell Feit,
Carl Mela, Ken Wilbur, Igor Skokan, William Grosso, Mark Rieke,
Michael Kaminsky, Thomas Wiecki, Harikesh Nair, Brendan Sinnott,
Jordan Nafa, Martin Block, and Gufeng Zhou for comments on earlier
versions of the article.
Step 9: Get marginal returns.
 ● Input: Selected model, specific spend levels.
 ● Output: Marginal returns for additional spend. Helps
in understanding the incremental benefits of additional
marketing spend, aiding in decision-making.
 ● Example Command:
Optional: Recreate previous models and replicate results.
 ● Input: JSON file of a previously exported model.
 ● Output: Recreated model and outputs. Ensures consis -
tency and reproducibility by allowing users to reload
and rerun models from saved states.
Hyperparameters explanation:
 ● Geometric Adstock: Theta values typically range from 0
to 0.8, reflecting the percentage of impact carried over to
the next period. For example, a theta of 0.3 for TV means
that 30% of the advertising effect remains the next day.
 ● Weibull CDF Adstock: Shape and scale parameters allow for
a flexible decay rate. Shape influences the curve’s form (S-
shaped or L-shaped), while scale adjusts the inflection point
of decay. Common bounds are shape (0, 2) and scale (0, 0.1).
 ● Weibull PDF Adstock: Similar to CDF but allows for
lagged effects, with shape influencing the peak timing and
scale adjusting the peak’s position. Recommended bounds
are shape (0.0001, 10) and scale (0, 0.1) for varied effects.
 ● Hill Saturation Function: Alpha and gamma parameters
define the saturation curve’s shape and inflection point.
Typical bounds are alpha (0.5, 3) for curve shape and
gamma (0.3, 1) for the saturation point.
Appendix B: Choosing the Right m/MMM
Package
This appendix provides a decision aid for practitioners looking to
adopt open-source mMM. We thereby focus on mMM (so, media
mix modeling) as digital advertising measurement is currently a
1 3
    3  Page 14 of 16

Customer Needs and Solutions            (2026) 13:3
10. Meta Platforms (2024) Robyn. Github. [Last accessed on Novem-
ber 27, 2025 at  h t t p  s : /  / f a c  e b  o o k  e x p e  r i m  e n t  a l . g i t h u b . i o / R o b y n /]
11. Runge J, Skokan I, Zhou G, Pauwels K (2024) Packaging Up
Media Mix Modeling: An Introduction to Robyn’s Open-Source
Approach. Marketing Science Institute Working Paper Series
2024, Report No. 24–147. [Last accessed on November 27, 2025
at  h t t p  s : /  / w w w  . m  s i .  o r g /  w o r  k i n  g - p  a p e  r / p a  c k  a g i  n g - u  p - m  e d i  a - m  i x
-  m o d e  l i  n g -  a n - i  n t r  o d u  c t i  o n -  t o - r  o b  y n s - o p e n - s o u r c e - a p p r o a c h /]
12. Google (2023) Lightweight Bayesian marketing mix modeling.
Github repository. [Last accessed on September 3, 2025 at  h t t p  s :
/  / g i t  h u  b . c  o m / g  o o g  l e /  l i g h t w e i g h t _ m m m]
13. Google (2025) Meridian. Github repository. [Last accessed on
November 27, 2025 at  h t t p  s : /  / g i t  h u  b . c  o m / g  o o g  l e /  m e r i d i a n]
14. Nair H (2025) Meridian is now available to everyone. Google Ads
& Commerce Blog. [Last accessed on February 4, 2025 at  h t t p  s : /  /
b l o  g .  g o o  g l e /  p r o  d u c  t s /  a d s  - c o m  m e  r c e  / m e r  i d i  a n -  m a r  k e t  i n g -  m i  x - m
o d e l - o p e n - t o - e v e r y o n e /]
15. PyMC Labs (2025) PyMC-Marketing. Github repository. [Last
accessed on November 27, 2025 at https:  / / g  i t h  u b .  c o m  / p y  m c - l  a b  s
/ p y m c - m a r k e t i n g]
16. Deighton JA, Mela CF, Moorman C (2021) Marketing thinking
and doing. J Mark 85(1):1–6
17. Ding Y , DeSarbo WS, Hanssens DM, Jedidi K, Lynch JG, Lehm-
ann DR (2020) The past, present, and future of measurement and
methods in marketing analysis. Mark Lett 31:175–186
18. Jedidi K, Mela CF, Gupta S (1999) Managing advertising and
promotion for long-run profitability. Mark Sci 18(1):1–22
19. Little JD, Lodish LM (1969) A media planning calculus. Oper
Res 17(1):1–35
20. Mela CF, Gupta S, Lehmann DR (1997) The long-term impact of
promotion and advertising on consumer brand choice. J Mark Res
34(2):248–261
21. Vidale ML, Wolfe H (1957) An operations-research study of sales
response to advertising. Oper Res 5(3):370–381
22. Naik PA, Raman K (2003) Understanding the impact of synergy
in multimedia communications. J Mark Res 40(4):375–388
23. Cain PM (2022) Modelling short-and long-term marketing effects
in the consumer purchase journey. Int J Res Mark 39(1):96–116
24. Runge J, Geinitz S, Ejdemyr S (2020) Experimentation and per -
formance in advertising: an observational survey of firm practices
on Facebook. Expert Syst Appl 158:113554
25. Gordon BR, Jerath K, Katona Z, Narayanan S, Shin J, Wilbur
KC (2021) Inefficiencies in digital advertising markets. J Mark
85(1):7–25
26. Lee SY , Runge J, Yoo D, Bart Y , Gyurak A, Schneider JW (2025)
Social Media Advertising’s Role in Small Business Resilience
amid Lockdowns. J Interactive Mark 60(4):362-376
27. Berman R (2018) Beyond the last touch: attribution in online
advertising. Mark Sci 37(5):771–792
28. Li H, Kannan PK (2014) Attributing conversions in a multichan-
nel online marketing environment: an empirical model and a field
experiment. J Mark Res 51(1):40–56
29. Hanssens DM, Pauwels KH (2016) Demonstrating the value of
marketing. J Mark 80(6):173–190
30. Valenti A, Srinivasan S, Yildirim G, Pauwels K (2024) Direct mail
to prospects and email to current customers? Modeling and field-
testing multichannel marketing. J Acad Mark Sci 52(3):815–834
31. Wiesel T, Pauwels K, Arts J (2011) Practice prize paper—Market-
ing’s profit impact: quantifying online and off-line funnel pro -
gression. Mark Sci 30(4):604–611
32. PyMC Labs (2025a) MMM with time-varying media baseline.
PyMC-Marketing How-To. [Last accessed on September 3, 2025
at ]  h t t p  s : /  / w w w  . p  y m c  - m a r  k e t  i n g  . i o  / e n  / 0 . 7  . 0  / n o  t e b o  o k s  / m m  m / m
m m _  t i m e  _ v  a r y  i n g _  m e d  i a _  e x a m p l e . h t m l
Author Contributions  J.R. and K.P. conceived of the idea for the
manuscript. J.R. wrote the main manuscript text and prepared the fig -
ures and tables. K.P. edited the text in depth. All authors reviewed the
manuscript.
Funding Open access funding provided by Northeastern University
Library. This research received no external funding.
Data Availability No datasets were generated or analysed during the
current study.
Declarations
Competing interests The authors declare no competing interests.
Conflict of interest The authors declare no conflicts of interest.
Open Access   This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropri -
ate credit to the original author(s) and the source, provide a link to the
Creative Commons licence, and indicate if you modified the licensed
material. You do not have permission under this licence to share
adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Cre-
ative Commons licence, unless indicated otherwise in a credit line to
the material. If material is not included in the article’s Creative Com -
mons licence and your intended use is not permitted by statutory regu-
lation or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit
h t t p  : / /  c r e a  t i  v e c  o m m o  n s .  o r g  / l i  c e n  s e s /  b y  - n c - n d / 4 . 0 /.
References
1. Arora N, Berman R, Feit E, Hanssens D, Li A, Lovett M, Mela C,
Wilbur K, Lynch J (2023) Charting the Future of Marketing Mix
Modeling Best Practices. Marketing Science Institute  Blue Rib -
bon Panel Report. [Last accessed on February 10, 2025 at  h t t p  s : /
/ w w w  . m  s i .  o r g /  p r e  s e n  t a t  i o n  / m s i  - b  l u e  - r i b  b o n  - p a  n e l  - r e  p o r t  - c  h a r  t i n
g  - t h  e - f  u t u  r e -  o f - m  a r  k e t  i n g -  m i x  - m o  d e l i n g - b e s t - p r a c t i c e s /]
2. Borden NH (1964) The concept of the marketing mix. J Advertis-
ing Res 4(2):2–7
3. Jagpal HS, Brick IE (1982) The marketing mix decision under
uncertainty. Mark Sci 1(1):79–92
4. Lambin JJ (1972) A computer on-line marketing mix model. J
Mark Res 9(2):119–126
5. Little JD (1975) BRANDAID: A marketing-mix model, part 1:
structure. Oper Res 23(4):628–655
6. Johnson GA, Shriver SK, Du S (2020) Consumer privacy choice
in online advertising: who opts out and at what cost to industry?
Mark Sci 39(1):33–51
7. Johnson G, Runge J, Seufert E (2022) Privacy-centric digital
advertising: implications for research. Customer Needs Solutions
9(1–2):49–54
8. Pauwels K, Aksehirli Z (2025) Big data analytics democratized
with clean collaboration and customer privacy choice. J Bus Res
188:115112
9. CRAN (2025) CRAN page for Robyn. [Last accessed on Novem-
ber 27, 2025 at  h t t p  s : /  / c r a  n .  r s t  u d i o  . c o  m / w  e b /  p a c  k a g e  s /  R o b y n / i n d
e x . h t m l]
1 3
Page 15 of 16     3

Customer Needs and Solutions            (2026) 13:3
33. Dekimpe MG, Hanssens DM (1995) Empirical generaliza -
tions about market evolution and stationarity. Mark Sci
14(3supplement):G109–G121
34. Dekimpe MG, Hanssens DM (1999) Sustained spending and per-
sistent response: A new look at long-term marketing profitability.
J Mark Res 36(4):397–412
35. Hilt DE, Seegrist DW (1977) Ridge, a computer program for cal-
culating ridge regression estimates. Department of Agriculture,
Forest Service, Northeastern Forest Experiment Station
36. Google (2025a) Budget optimization scenarios. Google Developers
blog. [Last accessed on February 5, 2025 at  h t t p  s : /  / d e v  e l  o p e  r s . g  o o g
l e .  c o m  / m e  r i d i  a n  / d o  c s / u  s e r  - g u  i d e  / b u  d g e t  - o  p t i m i z a t i o n - s c e n a r i o s]
37. CRAN (2025a) CRAN download count for Robyn. [Last accessed
on November 27, 2025 at  h t t p  s : /  / c r a  n l  o g s  . r - p  k g .  o r g  / b a  d g e  s / g r  a n
d - t o t a l / R o b y n]
38. Aurier P, Broz-Giroux A (2014) Modeling advertising impact at
campaign level: empirical generalizations relative to long-term
advertising profit contribution and its antecedents. Mark Lett
25(2):193–206
39. Gordon BR, Zettelmeyer F, Bhargava N, Chapsky D (2019) A
comparison of approaches to advertising measurement: evidence
from big field experiments at Facebook. Mark Sci 38(2):193–225
40. Lautman M, Pauwels K (2009) What is important? Identifying
metrics that matter. J Advertising Res 49(3):339–359
41. RungeJ, Patter H, Skokan I (2023) A new gold standard for digital
ad measurement. Harv Bus Rev.  h t t p s :   /  / h b  r . o  r  g  / 2 0   2 3 /   0  3  / a -   n e w  -  g
o  l d -  s t a  n  d a  r  d -  f o  r - d i  g i  t a l - a d - m e a s u r e m e n t
42. Manchanda P, Rossi PE, Chintagunta PK (2004) Response mod-
eling with nonrandom marketing-mix variables. J Mark Res
41(4):467–478
43. Moorman C, Day GS (2016) Organizing for marketing excel -
lence. J Mark 80(6):6–35
44. Lewis RA, Rao JM, Reiley DH (2011) Here, there, and every -
where: correlated online behaviors can lead to overestimates of
the effects of advertising. In Proceedings of the 20th International
Conference on World Wide Web (pp. 157–166)
45. De Haan E, Wiesel T, Pauwels K (2016) The effectiveness of
different forms of online advertising for purchase conversion
in a multiple-channel attribution framework. Int J Res Mark
33(3):491–507
46. Blake T, Nosko C, Tadelis S (2015) Consumer heterogeneity and
paid search effectiveness: A large-scale field experiment. Econo-
metrica 83(1):155–174
47. Eastlack JO Jr, Rao AG (1989) Advertising experiments at the
Campbell soup company. Mark Sci 8(1):57–71
48. Johnson GA (2023) Inferno: A guide to field experiments in
online display advertising. J Econ Manag Strategy 32(3):469–490
49. Lewis RA, Rao JM (2015) The unfavorable economics of mea -
suring the returns to advertising. Q J Econ 130(4):1941–1973
50. Feit EM, Wang P, Bradlow ET, Fader PS (2013) Fusing aggregate
and disaggregate data with an application to multiplatform media
consumption. J Mark Res 50(3):348–364
51. Lerner J, Tirole J (2005) The economics of technology sharing:
Open source and beyond. J Econ Persp 19(2):99–120
52. Henkel J (2006) Selective revealing in open innovation processes:
The case of embedded Linux. Res Pol 35(7):953–969
53. Henkel J, Schöberl S, Alexy O (2014) The emergence of open -
ness: How and why firms adopt selective revealing in open inno-
vation. Res Pol 43(5):879–890
54. Proserpio D, Hauser JR, Liu X, Amano T, Burnap A, Guo T,
Yoganarasimhan H (2020) Soul and machine (learning). Mark
Lett 31:393–404
55. Mulc T, Anderson M, Cubre P, Zhang H, Liu I, Kumar S (2025)
NNN: Next-Generation Neural Networks for Marketing Mix
Modeling. arXiv preprint arXiv:2504.06212
56. Dew R, Ansari A, Li Y (2020) Modeling dynamic heterogeneity
using Gaussian processes. J Mark Res 57(1):55–77
57. Dew R, Padilla N, Shchetkina A (2024) Your MMM is Broken:
Identification of Nonlinear and Time-varying Effects in Market -
ing Mix Models. arXiv preprint arXiv:2408.07678
58. Kireyev P, Pauwels K, Gupta S (2016) Do display Ads influence
search? Attribution and dynamics in online advertising. Int J Res
Mark 33(3):475–490
59. Gordon BR, Moakler R, Zettelmeyer F (2023) Close enough? A
large-scale exploration of non-experimental approaches to adver-
tising measurement. Mark Sci 42(4):768–793
60. Zantedeschi D, Feit EM, Bradlow ET (2017) Measuring multi -
channel advertising response. Manage Sci 63(8):2706–2728
61. Pauwels KH (2018) Modeling dynamic relations among market -
ing and performance metrics. Found Trends® Mark 11(4):215–301
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
1 3
    3  Page 16 of 16
