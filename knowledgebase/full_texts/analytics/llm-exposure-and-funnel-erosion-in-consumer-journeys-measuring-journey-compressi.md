---
title: 'LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering
  in passive behavioral logs'
url: https://doi.org/10.1057/s41270-026-00488-w
category: analytics
subcategory: empirical
date: 2026-05
venue: Journal of Marketing Analytics
authors:
- Chris J. Vargo
- Shahed Rahman
- Tobias Hopp
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00488-w.pdf
pages: 16
chars: 68460
fetched_at: '2026-11-08T17:25:31+00:00'
kb_version: 1
---

# LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in passive behavioral logs

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00488-w
  Chris J. Vargo
christopher.vargo@colorado.edu
1 Leeds School of Business, OLIA, University of Colorado
Boulder, 1B15 Armory Building, Boulder, CO 80303, USA
2 CMDI Advertising, University of Colorado Boulder, Boulder,
CO, USA
Abstract
LLM assistants increasingly mediate product discovery, yet most journey analytics and attribution systems still assume
that discovery begins with search, retailer browsing, or direct brand visits. That assumption misstates the observed jour -
ney. When evaluation moves into conversational interfaces, passive behavioral logs undercount early-stage activity and
standard journey reconstruction can resemble funnel erosion. We develop a measurement framework that treats LLM
usage as a first-class touchpoint in de-identified passive event logs linked to a post-trace survey. The framework detects
observed LLM exposure from domain and app signals, operationalizes a non-linear stage codebook (consideration, intent,
conversion-proximate), and computes journey metrics for compression, timing, channel mix, and transition structure with -
out imposing a canonical path. A production-scale, no-lookahead labeling system combines deterministic cues, model-
assisted classification, locked holdouts, and targeted adjudication audits to deliver reproducible measurement in noisy
passive logs. In a one-month observation window, the most stable empirical result is a shift in visible pre-intent discovery:
LLM-exposed journeys show substantially higher observable LLM share and higher review/UGC share, while unadjusted
compression and time-to-intent differences shrink after adjustment. Conversational discovery changes what marketing
analytics systems observe, and journey measurement must be updated accordingly.
Keywords Customer journey analytics · Clickstream analysis · Marketing attribution · Generative AI · Conversational
search · Funnel measurement
Received: 20 February 2026 / Accepted: 4 May 2026
© The Author(s) 2026
LLM exposure and funnel erosion in consumer journeys: measuring
journey compression and reordering in passive behavioral logs
Chris J. Vargo1  · Shahed Rahman2 · Tobias Hopp2
touchpoint is a conversation rather than a query, standard
funnel reconstructions can misstate where discovery began
and how much evaluation occurred before downstream vis-
its. Analytics dashboards may not simply miss a channel;
they may misclassify the strategic meaning of the visible
path. What appears to be a shorter or more efficient funnel
may instead reflect the migration of early-stage consider -
ation into a less observable interface. This matters because
touchpoint identification and optimization frameworks in
digital retail depend on accurate observation of sales-rel -
evant interactions (Zimmermann and Auinger 2023). We
therefore treat LLM exposure as an observability-boundary
problem for marketing analytics systems, not simply as an
AI-use issue.
Figure 1 contrasts a familiar search-led trace with an
LLM-mediated trace for a shopper seeking noise-canceling
headphones under $200. In the search-led path, discov -
ery unfolds across queries, reviews, category browsing,
product detail pages, and checkout. In the LLM-mediated
path, the shopper may begin with a prompt that generates a
Introduction
Customer-journey analytics depends on observing discov -
ery and evaluation in the order consumers encounter them.
Measurement choices shape resource allocation decisions
(Iacobucci et al. 2019), yet digital analytics can also pro -
duce analytics myopia when visible behaviors are mistaken
for strategically meaningful stages of the customer decision
journey (V ollrath and Villegas 2022). That risk has intensi -
fied as LLM assistants (e.g., ChatGPT, Claude, Gemini, Per-
plexity, Copilot) become entry points for product research,
comparison, and narrowing a choice set. When the first

C. J. Vargo et al.
shortlist and then move directly to a small set of product and
price-check pages. Passive logs can therefore show fewer
early-stage touches, fewer distinct domains, and shorter
time-to-intent even when substantial evaluation occurred
inside the conversational interface.
This paper establishes LLM usage as a distinct touch -
point class and shows how conventional funnel reconstruc -
tion breaks when conversational discovery is omitted from
the trace. Rather than imposing a linear funnel, we analyze
path- and time-based signals that capture (i) compression
(a smaller observable interval from consideration to intent),
(ii) reordering (more direct observable transitions to intent
or conversion-proximate behavior), and (iii) discovery mix
shifts (visible substitution away from classic search toward
conversational agents or direct retailer visits).
These patterns can arise through several concrete mecha-
nisms. LLMs can front-load shortlist formation before any
external browsing begins. They can move comparison steps
that previously occurred across multiple review sites into
one conversational interface. They can also redirect down -
stream validation toward a smaller set of price, shipping,
or retailer pages. Each mechanism simplifies the visible
journey. The measurement implication is straightforward:
journey analytics must account for consideration that occurs
inside an interface recorded as a single touchpoint (Fig. 2).
The paper makes four measurement contributions:
 ● A reproducible LLM detection registry for passive logs.
User-level observed exposure is identified from domain/
app signals with first-observed timing.
 ● Journey diagnostics that expose hidden consideration.
We operationalize compression, transition structure,
and discovery-mix measures without forcing a legacy
search-led funnel.
 ● A production-scale labeling and audit stack.  The mea -
surement system combines deterministic rules, model-
assisted classification, no-lookahead labeling, locked
holdouts, and targeted audits to turn noisy multi-source
traces into reproducible journey data.
 ● A guardrail design for interpretation.  Survey-linked
adjustment and the G0/G1/G2 decomposition separate
user exposure from journey augmentation and prevent
over-attribution.
Background and related work
Funnels, journeys, and non-linearity
Marketing theory continues to inform journey measurement
through staged models that move from awareness to action,
including hierarchy-of-effects formulations (Lavidge and
Steiner 1961; Wijaya 2012) and DAGMAR-style manage -
rial objectives (Colley 1961). Observed decision sequences,
however, are rarely linear. Reviews of advertising effects
emphasize indirect and context-dependent pathways
(Vakratsas and Ambler 1999), customer journey research
conceptualizes experience as distributed across interac -
tions among consumers, firms, partners, and external actors
(Lemon and Verhoef 2016), and practitioner frameworks
describe iterative exploration and evaluation rather than
one-way funnels (Mckinsey and Company 2009; Rennie
and Protheroe 2020).
For passive trace data, stages are best treated as an opera-
tional codebook rather than as a literal behavioral script. Our
operational funnel therefore uses three stages—consider -
ation, intent, and conversion-proximate behavior—because
Fig. 2 Compression (count) distribution by exposure group

Traditional( search-led) trace LLM-mediated trace
1. Search engine queryf or budgetA NC head-
phones
1. LLM prompt for budgetA NC headphones pri-
oritizingc omfort
2. Review site(s) and comparisona rticles 2. Shortlist generatedi nsideL LM
3. Marketplacec ategory browsing 3. Direct jumpst oa few productp ages (PDPs)
4. Multiple PDP views across brands 4. Price/shipping checks fort he shortlist
5. Cart/ checkout 5. Cart/ch eckout
Fig. 1 Illustrative journeys. When evaluation moves into an LLM interface, passive logs may show fewer early-stage touches and shorter time-to-
intent, even if the consumer explored many options conversationally

LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in…
awareness is rarely observable in passive clickstreams
(Fig.  3).
Touchpoint systems must also remain aligned with how
customers are actually observed. Conversion rate optimiza-
tion research formalizes the need to identify sales-impacting
touchpoints along the customer journey accurately (Zim -
mermann and Auinger 2023), while touchpoint research
shows that different touchpoints contribute differently
to brand consideration and resource-allocation decisions
(Baxendale et al. 2015). Broader analytics work also warns
against tool-centric measurement that drifts away from
decision-journey strategy (V ollrath and Villegas 2022). We
build on that logic by treating LLM usage as a first-class
touchpoint and by showing when apparent funnel erosion
reflects changed observability rather than changed behavior.
Clickstream-based journey and attribution
modeling
Event-level logs are routinely used to reconstruct journeys
and estimate how touchpoints relate to conversion. Graph-
based attribution modeling shows that adjacency and order
carry information about pre-conversion structure (Anderl
et al. 2016). Multichannel models further demonstrate that
paths can be treated as dynamic sequences with measurable
effects on downstream outcomes (Li and Kannan 2014).
Touchpoint studies also show that different channels con -
tribute differently to consideration and choice (Baxendale
et al. 2015).
Our work stays within this tradition but updates a key
measurement assumption. Discovery and evaluation may
now occur inside an LLM interface that appears in pas -
sive logs as a single domain/app event. A conversational
assistant can operate simultaneously as information source,
comparison interface, recommendation agent, and redirect
mechanism. The theoretical issue is therefore not only that
LLMs add another touchpoint to the journey, but that they
may consolidate several formerly separate touchpoints into
one conversational interaction. If that touchpoint is omitted
or misclassified, downstream product pages, retailer visits,
or price-checking pages may appear to initiate the journey,
leading analytics systems to over-credit lower-funnel touch-
points. That shift can change inferred funnel length, timing,
and channel contribution even when underlying cognitive
effort is unchanged.
Conversational AI and product evaluation
Conversational agents have been shown to influence pur -
chase intention, perceived information value, and engage -
ment in commerce contexts (Lo Presti et al. 2021; Le 2023;
Luo et al. 2023). Recent work comparing generative-AI
chatbots with search engines finds meaningful differences
in how consumers evaluate products and disclose informa -
tion (Kim and Priluck 2025). These findings indicate that
LLM-mediated discovery should be measured as its own
touchpoint class rather than absorbed into search.
The key behavioral link for this paper is not that LLMs
eliminate evaluation, but that they can relocate evaluation
and change how much of it remains externally visible. A
parsimonious consumer-search account is that conversa -
tional interfaces can front-load option screening, compress
visible exploration, and redirect validation activity toward
a smaller set of downstream pages. In decision-aid terms,
the technology may change the distribution of visible effort
across interfaces rather than simply changing final choices.
Because our data do not observe the conversational content
itself, we treat these pathways as theory-consistent inter -
pretations of the journey patterns rather than as identified
mechanisms.
Data
Multi-source passive behavioral logs
The empirical setting combines multi-source event logs
from a third-party passive measurement panel with sur -
vey data linked at the user level ( caseid). The trace data
record event-level touchpoints across web and app contexts,
including domain/app bundle, URL fields when available,
timestamps, and auxiliary metadata. The survey contributes
demographics, media-attitudinal measures (news frequency
items NEWS1a–f, media consumption/distrust items CME-
DIA1–4, digital media self-efficacy items MDSE1–3, and
political/news interest and ideology), and survey weights.
The provider applies de-identification and aggressive PII
reduction before delivery. All analyses therefore operate on
de-identified traces, and we do not perform additional PII Fig. 3 Kaplan–Meier survival curves for time-to-intent (solid: non-
exposed; dashed: LLM-exposed)

C. J. Vargo et al.
scrubbing beyond the provider’s process. The trace window
spans October 4, 2024–November 5, 2024 (based on file
timestamps), and the survey field period is November 21,
2024–December 6, 2024.
Unit of analysis
The analysis uses two linked units. We construct (i) a user-
day panel for first observed exposure timing and within-
user comparisons and (ii) journey-level sequences (paths)
for transition-structure and timing analyses. A “journey” is
defined as an ordered sequence of events within a rolling
window, segmented by a fixed inactivity gap and maximum
window length; robustness checks vary the gap/cap choices.
The unit of statistical inference is the user ( caseid), and
uncertainty is clustered accordingly.
Measurement and methods
Detecting LLM exposure
LLM exposure is detected from domain/app bundle sig -
nals and light text cues when available. Examples include
domains such as chat.openai.com, claude.ai,
gemini.google.com, and perplexity.ai, and
corresponding mobile app bundles. Detection uses only
current-event fields (never future context), which preserves
a strict no-lookahead rule and avoids label leakage.
We define:
 ● User-level observed exposure  ( Ei): whether user i
has any detected LLM touchpoint in the observation
window.
 ● First observed exposure timing:  the first observed day/
week with an LLM touchpoint (first observed, not nec -
essarily first-ever use).
 ● LLM intensity (continuous):  LLM touches and/or min -
utes per week when duration is available.
Exposure taxonomy: user exposure versus journey
augmentation
The measurement design separates a broad user-level
exposure registry from a narrower journey-level augmen -
tation signal. User-level observed exposure is Ei ∈{ 0, 1}
as defined above and follows the paper’s primary AI/
LLM detection registry, which can include canonical LLM
domains/apps as well as adjacent conversational surfaces
detectable in passive logs. Journey-level augmentation is
stricter and is based only on canonical in-journey LLM
channel matches before first intent:
Apre, j = iff journey j contains at least one LLM touch -
point before first intent.
If a journey has no observed intent event, the full jour -
ney is treated as the pre-intent window for this indicator.
We enforce hierarchy Apre,j ≤ Ei in all reporting artifacts
so that journey augmentation cannot be positive for users
without observed exposure.
We report a three-group decomposition in Results to
separate exposure propensity from journey augmentation:
 ● G0: E =0 , Apre =0  (non-exposed users),
 ● G1: E =1 , Apre =0  (exposed users, non-augmented
journeys),
 ● G2: E =1 , Apre =1  (exposed users, pre-intent LLM-
augmented journeys).
This decomposition separates user-level exposure propen -
sity from within-journey augmentation and avoids treating
all exposed-user journeys as LLM-augmented.
Stage codebook for trace events
Awareness is not reliably observable in clickstreams, so we
operationalize a three-stage funnel. Stages are assigned at
the event level, and non-linear paths (repeats, backtracking,
and out-of-order transitions) are allowed (Table 1).
Table 1 Operational funnel stages and illustrative trace signals
Stage Behavioral signals Examples in traces
Consideration Information seek-
ing, browsing,
reviews, com-
parisons, category
exploration
Review articles,
“best-of” lists,
YouTube reviews,
retailer category
pages, general
brand-site browsing,
LLM prompts asking
for recommendations
Intent Preference forma-
tion, price/ship-
ping checks, store
locator, repeated
product views,
cart additions
“price” or “ship-
ping” pages, “where
to buy,” cart events,
repeated visits to a
small set of PDPs,
LLM prompts like
“compare X vs Y”
Conversion-proximate Checkout/pay-
ment flows, order
confirmation,
account/order
tracking, subscrip-
tion start
Checkout URL
patterns, payment
domains, order
confirmation pages,
app events consis-
tent with purchase
completion
 PDP = Product detail page

LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in…
Journey metrics
We compute several journey-level metrics to represent dis -
tinct forms of “funnel erosion” without imposing a canoni -
cal path.
Funnel compression. Let Nj,s be the number of events
in journey j labeled as stage s. A count-based compression
metric is
C(count) j = Nj,intent + Nj,conv Nj,total . (1)
We also compute time-based variants using dwell-time or
inter-event time when available.
Stage timing. We compute time-to-event outcomes such
as:
∆t(intent) j = tj,ﬁrst intent − tj,ﬁrst consid , (2)
and analogous measures for first conversion-proximate
behavior, with right-censoring when not observed.
Discovery mix. For pre-intent events, we compute touch-
point shares across channel classes: LLM, classic search,
retailer/marketplace, direct brand, review/UGC, and other.
We also compute any-touch indicators by channel class.
Transition structure. We compute stage-to-stage transi -
tion frequencies and transition probabilities
P (a → b)= #( a → b)∑
b′ #( a → b′) , (3)
including direct consideration →conversion-proximate
jumps and looping intensity (e.g., consideration↔intent).
Consideration breadth.  When entity extraction cover -
age permits, we measure breadth as the number of unique
sources visited before first intent.
Hypotheses
Directional predictions are used only where the measure -
ment logic is reasonably clear; elsewhere, tests are framed
as difference hypotheses. H1–H5 and H7 are journey-level
outcomes; H6 is user-level profiling.
H1 (Compression):  Journey compression differs by observed 
LLM exposure state, with decomposition by journey aug -
mentation state (G0/G1/G2).
H2a (Shorter observable interval): Observed LLM exposure
is  associated  with  a  shorter  trace-level  interval  from first 
consideration to first intent.
H2b (Longer observable interval):  In some settings,
observed LLM exposure is associated with a longer trace-
level interval to intent if LLM-mediated comparison induces
additional validation loops.
H3 (Discovery mix shift):   Pre-intent  channel  shares  differ 
by observed exposure state, with explicit decomposition for
LLM-augmented versus non-augmented journeys among
exposed users.
H4 (Transition structure):   Stage-transition  patterns  differ 
by observed exposure state, including patterns consistent
with more direct jumps or fewer loops, interpreted with the
G0/G1/G2 decomposition.
H5 (Breadth): Breadth of sources explored prior to intent
differs  by  observed  exposure state,  with  decomposition  by 
journey augmentation state.
H6 (Survey alignment): User-level observed LLM exposure
is systematically related to survey measures of media use
and digital media self-efficacy, indicating consistent profil-
ing rather than random noise.
H7 (Moderation):   Tech  affinity/involvement  moderates 
associations between observed LLM exposure and funnel
outcomes (when available).
Labeling pipeline (conceptual overview)
The labeling pipeline is a hybrid system designed for pro -
duction-scale measurement rather than one-off annotation.
Deterministic behavioral cues handle semantically crisp
trace patterns, model-assisted classification handles stage
and entity cases that require context, and targeted manual
audits test the boundaries where failure risk is highest. The
pipeline enforces a strict no-lookahead rule, preserves audit-
able intermediate artifacts, and supports high-agreement
subset analyses without rewriting the underlying trace. The
result is a reproducible, repeatable journey measurement
system for noisy multi-source behavioral logs.
Low-level implementation details (token budgets, price-
verification tolerances, and infrastructure settings) are pro -
vided in Appendix B.
Empirical strategy and statistical inference
Our primary estimands are differences in journey-level
outcomes between LLM-exposed and non-exposed

C. J. Vargo et al.
observations.1 Because event logs contain repeated mea -
sures within users, the unit of statistical inference is the user
(caseid) rather than individual events. We therefore report
uncertainty using standard errors clustered at the caseid
level for regression models and caseid-level bootstrapping
for non-parametric estimands such as differences in transi -
tion probabilities (Cameron and Miller 2015; MacKinnon
et al. 2023). The empirical design follows the measurement
architecture: user-level inference, clustered uncertainty, and
separate exposure-versus-augmentation estimands.
To keep constructs distinct, we report (i) exposure-state
contrasts using Ei and (ii) journey-augmentation decom -
position using G0/G1/G2. The first estimand addresses
whether users with observed LLM exposure exhibit differ -
ent journey traces overall. The second estimand addresses
whether differences are concentrated in journeys that are
themselves LLM-augmented ( Apre =1 ) versus non-aug -
mented journeys among exposed users (Apre =0 ). We treat
this decomposition as a core identification guardrail against
user-level selection being mistaken for journey-level aug -
mentation effects.
We report both unadjusted and adjusted associations.
Adjusted models include a pre-specified set of covari -
ates: demographics, digital media self-efficacy (MDSE),
media consumption/distrust (CMEDIA), news frequency
(NEWS), and baseline trace intensity (total events and
active days observed). Where survey weights are available,
we report weighted estimates as a robustness check along -
side unweighted estimates.
For fractional outcomes such as count-based compres -
sion and pre-intent channel shares, we estimate fractional
response models (Papke and Wooldridge 1996) with caseid-
clustered standard errors. For time-to-event outcomes (time-
to-intent and time-to-conversion-proximate), we estimate
Kaplan–Meier curves and Cox proportional hazards models
(Kaplan and Meier 1958; Cox 1972), using robust variance
clustered by caseid. For transition-structure differences, we
compute stage-to-stage transition probabilities and obtain
95% confidence intervals for differences via nonparametric
bootstrapping over caseids.
Because observed LLM exposure is not randomly
assigned, we supplement regression adjustment with pro -
pensity-based reweighting. Specifically, we estimate a pro -
pensity model for observed exposure using pre-specified
covariates and compute inverse-probability weights; covari-
ate balance is assessed using standardized mean differences.
These analyses are intended to reduce observable differences
between groups rather than to claim causal identification.
1 The full specification registry (outcomes, estimands, covariate sets,
optimization defaults, weights, and inference settings) is provided in
Appendix D.
Technique selection rationale and parameterization
details
Estimator choice follows outcome support and censoring
structure rather than preferred findings. Fractional-response
GLMs (logit link) are used for bounded outcomes in [0, 1]
(compression shares and discovery-mix shares). Cox pro -
portional hazards models are used for time-to-event out -
comes with right censoring. Poisson GLMs are used for
non-negative count breadth outcomes. Survey-alignment
models are estimated with weighted least squares because
those outcomes are case-level survey means with provided
sample weights.
Specification is pre-declared as unadjusted (outcome
∼ LLM) and adjusted (outcome ∼ LLM+demographics +
MDSE + CMEDIA + NEWS + baseline activity). Baseline
activity is total events and active days. Demographics enter
as available indicator dummies after coding harmonization.
We do not use user-supplied starting values; model fitting
uses library defaults for initialization and optimizer settings.
Uncertainty is cluster-robust at the caseid level for regres-
sion models. Transition-difference uncertainty uses caseid
bootstrap resampling (main specification: 500 draws). For
Cox models, convergence fallback uses a penalizer ladder
(0.00, 0.01, 0.10, 1.00) when needed. Propensity weighting
uses unstabilized inverse-probability weights from a logis -
tic observed-exposure model with the same pre-specified
covariates used in adjustment models.
Timing outcomes are defined in minutes from first
consideration within journey. Right-censored records are
retained when the target event is not observed. Negative
observed lags are treated as invalid ordering artifacts and
recast to censored observations; non-positive durations are
clipped to a small positive constant for Cox/KM compat -
ibility. Baseline journey segmentation for the main analysis
uses a 24-hour inactivity gap and 168-hour cap; robustness
checks vary gap and cap as reported in Table 5.
Adjusted models use complete-case estimation for
required covariates, which produces model-specific sample
sizes. We therefore report caseid/journey counts for each
hypothesis family in the table notes to make missingness
and effective sample changes explicit. As an additional
robustness design, we emphasize within-user comparisons
among exposure-positive users who have both Apre =0
and Apre =1  journeys, so user-level stable differences are
differenced out when interpreting augmentation-specific
patterns.

LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in…
Validation
The measurement system is evaluated in three layers. First,
we use a consolidated expert-label pool with fixed dev/hold-
out splits for stage and price, plus held-out guided-choice
audits for product name, brand, and category. Second, we
retain a targeted manual-adjudication packet focused on the
known failure boundaries (stage boundaries, entity ambi -
guity, price semantics, and exposure substrings) and treat
it as a stress test rather than a representative performance
estimate. Third, one domain expert hand-reviewed 100 rows
from each final inference layer (stage classification, entity
extraction, price semantics, and observed LLM exposure
detection). Together, these layers characterize both held-
out quality and deployed-output behavior after remediation;
because the key metrics are already stated directly below,
the manuscript keeps the validation evidence in prose rather
than as separate standalone tables.
On the reaudited expert pool, stage classification reaches
accuracy 0.914 and macro-F1 0.808 (κ =0 .858) on dev and
accuracy 0.879 and macro-F1 0.834 (κ =0 .808) on holdout.
Residual uncertainty is now concentrated in a small number
of consideration-versus-intent boundary rows rather than in
systematic conversion failure. The final 100-row production
audit also shows exact agreement 1.000 (κ =1 .000), which
places the stage layer above the paper’s ship gate for both
held-out performance and deployed-output agreement.
Entity extraction is now reported as three audited fields
rather than as a single all-fields exact-match construct. On
held-out guided-choice audits, micro-F1 is 0.844 for prod -
uct name, 0.906 for brand, and 0.875 for category. In the
100-row expert audit, exact agreement is 0.880/0.970/1.000
and κ is 0.874/0.968/1.000 for product name, brand, and
category, respectively. The targeted entity packet shows that
the remaining error is dominated by product-title over-spec-
ification and normalization rather than brand or category
confusion.
Price semantics is evaluated on the consolidated expert
pool and the final thresholded price layer. The current price
pass reaches positive-class F1 1.000 and κ =1 .000 on both
dev and holdout splits. In the 100-row final-output audit,
price-present agreement is 0.970, κ =0 .917, precision is
1.000, recall is 0.880, and F1 is 0.936. The targeted price
packet was useful because it isolated semantic false posi -
tives from non-price dollar mentions; those cases motivated
the stricter thresholding now used in the final stack.
Observed-LLM exposure detection is evaluated with the
targeted 48-row boundary packet and a 100-row final-output
audit. The packet localized the remaining risk to ambiguous
substring/search cases rather than canonical domain or app
hits, and the final detector reaches exact agreement 0.960,
κ =0 .919, precision 0.911, recall 1.000, and F1 0.953. This
is the basis for the stricter canonical-exposure robustness
check reported later.
Results
Sample composition and group sizes
The final analysis dataset comprises 587 distinct users
(caseids), 3,360 journeys, and 2,917,655 trace events within
the observation window. Of these users, 185 are exposure-
positive (at least one observed LLM touchpoint), and 402
have no observed LLM touchpoint. At the journey level,
1,102 journeys belong to exposure-positive users and 2,258
belong to non-exposed users. Table 2 reports the G0/G1/G2
decomposition, which separates user-level exposure from
journey-level augmentation; 91 exposure-positive users
contribute both augmented and non-augmented journeys,
allowing within-user contrasts. Table 3 summarizes sample
characteristics by exposure group, and Table 4 reports unad-
justed and adjusted model estimates with caseid-clustered
uncertainty.
Table 2  Exposure versus augmentation decomposition (guardrail
against construct conflation)
Group definition Users Journeys Jour-
ney
share
(%)
G0: E =0 , Apre =0  (non-exposed
users)
402 2,258 67.20
G1: E =1 , Apre =0  (exposed users;
non-augmented journeys)
180 890 26.49
G2: E =1 , Apre =1  (exposed users;
pre-intent LLM-augmented journeys)
96 212 6.31
E = User-level observed LLM exposure (any AI/LLM touch in-win -
dow under the primary registry). Apre  = Journey-level pre-intent
LLM augmentation indicator under the stricter canonical in-journey
channel mapping. Exposed users with both Apre =0  and Apre =1
journeys: 91 of 185. Raw parser exceptions ( E =0 , raw pre-intent
LLM signal=1) before hierarchy gating: 2 journeys
Table 3 Sample descriptives by exposure group
Metric LLM-exposed Non-exposed
N caseids 185 402
N journeys 1,102 2,258
N events 1,691,708 1,225,947
Median journeys per user 5.000 5.000
MDSE mean 4.937 4.796
CMEDIA mean 4.160 4.152
NEWS mean 4.059 3.915
Total events per user 9,144.368 3,049.619
Active days 25.676 21.965
Counts are integers with comma grouping.  MDSE  = Digital media
self-efficacy, CMEDIA  = Media consumption/distrust,  NEWS  =
News-frequency scale

C. J. Vargo et al.
H1 Compression
Compression differences are not robust after adjustment.
Descriptively, LLM-exposed journeys show slightly higher
count compression (0.0236 vs 0.0201) and higher time com-
pression (0.498 vs 0.370). The unadjusted count-compres -
sion AME is +0.003 (95% CI [− 0.002, 0.009], p =0 .227)
and the adjusted AME is +0.003 (95% CI [− 0.004, 0.010],
p =0 .379). Time-based compression is positive before
adjustment (AME +0.126, 95% CI [0.073, 0.179], p< 0.001
) and returns to zero after adjustment (AME −0.010, 95% CI
[− 0.069, 0.049], p =0 .740). H1 therefore does not provide
adjusted support for a headline acceleration result.
H2 Timing
Timing estimates point in the same raw direction as compres-
sion but remain imprecise after adjustment. Time-to-intent
is shorter for exposure-positive journeys in the censored
survival frame (mean follow-up 3,501 vs 3,756 min), but
the Cox contrasts do not separate clearly: HR = 1.192 unad-
justed (95% CI [0.974, 1.458], p =0 .089) and HR = 1.203
adjusted (95% CI [0.956, 1.513], p =0 .116). The data
therefore do not establish faster progression to intent once
covariates are included.
For conversion-proximate timing, no observed events
remain in the survival frame after censoring and negative-
lag recoding, so we do not report a Cox contrast or Kaplan–
Meier panel for this endpoint. Combined with the weaker
validation of the conversion-proximate class, this outcome
Table 4 Main model estimates with caseid-clustered uncertainty (unadjusted and adjusted), Panel A
Unadjusted Adjusted
 Outcome Model Estimate (SE) 95% CI p Estimate (SE) 95% CI p
H1: Compression (count) Frac. logit (AME) 0.003 (0.003) [− 0.002,
0.009]
0.227 0.003 (0.003) [− 0.004, 0.010] 0.379
H1: Compression (time) Frac. logit (AME) 0.126 (0.027) [0.073, 0.179] < 0.001 − 0.010 (0.030) [− 0.069, 0.049] 0.740
H2: Time to intent Cox PH (HR) 1.192 (—) [0.974, 1.458] 0.089 1.203 (—) [0.956, 1.513] 0.116
H2: Time to conversion-proximate Cox PH (HR) – – – – – –
H3: Pre-intent LLM share Frac. logit (AME) 0.010 (0.002) [0.005, 0.015] < 0.001 0.009 (0.002) [0.005, 0.014] < 0.001
H3: Pre-intent classic-search share Frac. logit (AME) 0.022 (0.013) [− 0.004,
0.048]
0.094 0.017 (0.016) [− 0.015, 0.049] 0.292
H3: Pre-intent retailer/marketplace
share
Frac. logit (AME) − 0.003
(0.006)
[− 0.014,
0.009]
0.638 −  0.004
(0.008)
[− 0.019, 0.011] 0.622
H3: Pre-intent direct-brand share Frac. logit (AME) − 0.000
(0.000)
[− 0.000,
0.000]
1.000 −  0.000
(0.000)
[− 0.000, 0.000] 1.000
H3: Pre-intent review/UGC share Frac. logit (AME) 0.029 (0.011) [0.008, 0.051] 0.008 0.028 (0.013) [0.003, 0.053] 0.027
H3: Pre-intent other share Frac. logit (AME) − 0.057
(0.017)
[− 0.090,
− 0.023]
< 0.001 − 0.048 (0.021) [− 0.090,
− 0.006]
0.024
Main model estimates with caseid-clustered uncertainty (unadjusted and adjusted), Panel B.
Unadjusted Adjusted
 Outcome Model Estimate (SE) 95% CI p Estimate (SE) 95% CI p
H4: Transition C → I Bootstrap diff 0.053 (—) [− 0.070,
0.188]
– – – –
H4: Transition C → V Bootstrap diff 0.000 (—) [0.000, 0.000] – – – –
H4: Transition C → C Bootstrap diff − 0.055 (—) [− 0.185,
0.074]
– – – –
H5: Breadth (IRR) Poisson (IRR) 0.994 (—) [0.936, 1.056] 0.855 0.980 (—) [0.911, 1.054] 0.589
H6: MDSE score WLS 0.098 (0.092) [− 0.081,
0.278]
0.283 0.088 (0.096) [− 0.101, 0.277] 0.362
H6: CMEDIA score WLS − 0.002
(0.106)
[− 0.210,
0.207]
0.988 0.056 (0.112) [− 0.163, 0.276] 0.614
H6: NEWS score WLS 0.164 (0.088) [− 0.009,
0.338]
0.063 0.212 (0.094) [0.028, 0.397] 0.025
H7: MDSE interaction Frac. logit
(interact.)
– – – 0.010 (0.128) [− 0.241, 0.261] 0.939
AME = Average marginal effect,  HR = Hazard ratio,  IRR = Incidence rate ratio,  WLS = Weighted least squares,  CI = Confidence interval,  SE
= Standard error . Em dashes indicate not estimated for that specification. Caseids/journeys ( unadjusted; adjusted) : H 1/H3/H5 = 587 /3,360;
395/2,216. H2 = 346/1,270; 234/870. H4 = 587/3,360; not adjusted. H6 MDSE = 491/491; 491/491. H6 CMEDIA = 456/456; 456/456. H6 NEWS
= 528/528; 528/528. H7 = not unadjusted; 491/2,815

LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in…
remains outside the paper’s primary interpretive results in
the current window.
H3 Discovery mix
Discovery mix is the most stable empirical result in the
paper. Pre-intent LLM share is higher in exposure-positive
journeys descriptively (0.00546 vs 0.00002) and in both
unadjusted and adjusted models (adjusted AME +0.009,
95% CI [0.005, 0.014], p< 0.001). Review/UGC share is
also higher after adjustment (AME +0.028, 95% CI [0.003,
0.053], p =0 .027). Classic-search share is positive but not
distinguishable from zero after adjustment (AME +0.017,
p =0 .292), and retailer/marketplace and direct-brand
shares remain null. Figure 4 shows the corresponding com-
positional shift: the visible pre-intent mix changes by adding
detectable LLM and review/UGC activity, not by collapsing
retailer or direct-brand traces.
H4 Transition structure
Transition estimates are directionally consistent with more
direct trace-level progression, but they are not precise. Con-
sideration→intent transitions are more common among
exposure-positive journeys (0.252 vs 0.199), and consid -
eration→consideration loops are less common (0.748 vs
0.801). The bootstrap difference for C → I is +0.053 (95%
CI [−0.070, 0.188]) and the C → C difference is −0.055
(95% CI [−0.185, 0.074]); direct C → V  transitions are zero
in both groups in the current run. The direction is stable, but
the interval width keeps H4 secondary to the discovery-mix
result in the current window.
H5 Breadth
Breadth shows no adjusted difference. Measured as the
number of unique pre-intent sources, the Poisson model
yields an adjusted incidence rate ratio of 0.980 (95% CI
[0.911, 1.054], p =0 .589). Because breadth depends on the
secondary entity-extraction layer, we use it as a descriptive
cross-check rather than a core test. On that standard, breadth
differences are negligible in this observation window.
H6 Survey alignment
Survey alignment is limited to NEWS scores. LLM exposure
is associated with higher NEWS scores in adjusted models
(0.215, 95% CI [0.030, 0.400], p=0.023), while MDSE and
CMEDIA differences are not statistically distinguishable
from zero. The results indicate a measurable link to news
frequency, not a broad split in digital media self-efficacy or
media distrust in this sample.
H7 Moderation
Moderation is null in the current sample. The interaction
between LLM exposure and MDSE in predicting compres -
sion is effectively null (interaction coefficient 0.010, 95%
CI [−0.241, 0.261], p =0 .939) and does not warrant a
main-text figure.2
Robustness checks across exposure definitions, reweight-
ing, label restrictions, within-user augmentation contrasts,
and journey segmentation are summarized in Table 5.
Full segmentation and within-user tables are provided in
Appendix E.
Table 5 leaves the main interpretation unchanged. First,
at the reported precision shown in the table, the IPW sensi -
tivity row is numerically unchanged from the main adjusted
model, which indicates that reweighting does not alter the
reported compression, timing, or pre-intent LLM-share
conclusions in this sample. The stricter canonical exposure
definition weakens compression and timing further (count-
compression AME +0.002, p =0 .538; intent HR 1.142,
p =0 .274) but strengthens the pre-intent LLM-share effect
(AME +0.039, p< 0.001). Second, aggressive high-agree -
ment restrictions do not rescue a stronger acceleration story:
they preserve only a noisy compression estimate and do not
yield an interpretable timing contrast. Third, the within-
user G2 − G1 contrast among the 91 exposure-positive
users who contribute both journey types is especially deci -
sive: augmented journeys show higher visible LLM share
(∆ = +0 .030, 95% CI [0.022, 0.038]) and slightly lower
compression ( ∆= − 0.006, 95% CI [− 0.015, 0.000]).
Together with the segmentation grid, where H1 AMEs
remain small (+ 0.000 to + 0.002), H2 intent HRs remain
only modestly above 1.0 (1.114 to 1.185), and C → I
2 The fitted marginal-effects profile is nearly flat: predicted compres -
sion changes little across low versus high MDSE, and the exposed/
non-exposed lines remain close to parallel.
Fig. 4  Pre-intent channel shares by exposure group (stacked bars
labeled by channel class)

C. J. Vargo et al.
differences remain tightly clustered (+ 0.052 to + 0.053),
the stable result is the visible pre-intent LLM-share shift. A
broad acceleration claim does not survive the more restric -
tive specifications.
Discussion
LLM assistants have changed the observable structure of
discovery. If analysts continue to assume search-led jour -
neys, they will read missing early-stage touches as higher
funnel efficiency or weaker consideration when those activi-
ties have shifted into a conversational interface. The con -
tribution of this paper is to treat LLM usage as a first-class
touchpoint and to provide journey diagnostics that keep
attribution and funnel reporting aligned with the current
observability boundary.
The stage codebook is deliberately pragmatic. Classic
hierarchy-of-effects and goal-based funnel models (Lavidge
and Steiner 1961; Colley 1961; Wijaya 2012) remain use -
ful as managerial language, but clickstream traces rarely
provide reliable signals for awareness. Consistent with cus-
tomer journey research on non-linear movement and loop -
ing (Vakratsas and Ambler 1999; Lemon and Verhoef 2016)
and practitioner frameworks that emphasize iterative explo-
ration (Mckinsey and Company 2009; Rennie and Protheroe
2020), we operationalize three stages (consideration, intent,
conversion-proximate) and analyze path structure and tim -
ing rather than impose a single canonical sequence.
The observed patterns are consistent with several mech -
anisms. LLMs can front-load shortlist formation, move
comparison activity into one conversational interface, and
redirect downstream validation toward a smaller set of
price, shipping, retailer, or checkout-adjacent pages. In pas-
sive logs, each pathway changes the visible journey even
when deliberation continues.
A useful distinction is between behavioral compres -
sion and observable compression. Behavioral compres -
sion would imply that LLMs reduce the actual amount of
consumer deliberation or decision effort. Observable com -
pression means that the traceable portion of the journey
becomes shorter because some discovery and evaluation
activities move into less visible environments. The current
study is designed to measure observable compression. Pas -
sive behavioral logs can reveal changes in the structure of
observed touchpoints, but they cannot fully capture cogni -
tive effort, conversational search depth, or within-interface
comparison.
The empirical result is correspondingly narrow and clear.
The stable finding is a shift in visible pre-intent discovery,
not a universal acceleration effect. Pre-intent LLM share
rises sharply, review/UGC share also rises, and that pattern
survives adjustment and robustness checks. Compression
and timing move in the expected raw direction, but they
do not survive adjustment as headline behavioral results.
The within-user G2 − G1 contrast sharpens the interpreta -
tion: augmented journeys show higher visible LLM share
without higher compression. That pattern is consistent with
observability change. The paper therefore makes a measure-
ment claim rather than a behavioral acceleration claim: once
conversational discovery enters the path, standard journey
analytics understate early-stage activity and overstate the
apparent role of downstream visible touchpoints.
This interpretation is consistent with prior evidence that
conversational agents affect perceived information value
and purchase-related intentions in commerce contexts (Lo
Presti et al. 2021; Le 2023; Luo et al. 2023) and with work
Table 5 Structured sensitivity checks (IPW, exposure definition, label
restriction, within-user augmentation, and segmentation summary)
Specification Compression Time to
intent
Pre-intent
LLM share
Transi-
tion
C → I
Main adjusted
model (primary
broad exposure
registry)
AME 0.003,
p = 0.379
HR 1.203
[0.956,
1.513],
p = 0.116
AME
0.009,
p = < 0.001
0.053
[− 0.070,
0.188]
IPW-adjusted
sensitivity
(unchanged
at reported
precision)
AME 0.003,
p = 0.379
HR 1.203
[0.956,
1.513],
p = 0.116
AME
0.009,
p = < 0.001
–
Strict canonical
LLM exposure
definition
AME 0.002,
p = 0.538
HR 1.142
[0.900,
1.449],
p = 0.274
AME
0.039,
p = < 0.001
0.062
[− 0.063,
0.207]
High-agreement
journeys only
(unclear =0
; unadjusted
subset)
AME 0.065,
p = 0.539
– AME
− 0.000,
p = 1.000
–
Within-user
augmentation
contrast (paired
G2 − G1
among both-
state exposed
users)
∆ − 0.006
[− 0.015,
0.000]
– ∆ 0.030
[0.022,
0.038]
–
Segmentation
grid (9 gap/cap
combinations;
unadjusted
range)
AME range
[0.000, 0.002]
HR range
[1.114,
1.185]
– ∆ range
[0.052,
0.053]
IPW = Inverse-probability weighting. At the displayed precision, the
IPW row is numerically identical to the main adjusted model. C → I
denotes the transition from consideration to intent. The main/IPW/
strict rows report model-based estimates; the high-agreement row
reports an unadjusted subset analysis with unclear =0 ; the within-
user row reports paired user-level mean differences comparing G2
and G1; the segmentation row summarizes the full grid reported in
Appendix E. Em dashes indicate not reported or not estimable for
that specification

LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in…
showing that generative-AI chatbots and search engines
produce different evaluation behaviors (Kim and Priluck
2025). The manuscript measures observable journey struc -
ture, not internal cognitive effort, and the interpretation
remains bounded to that distinction.
Managerial implications
In path-based marketing analytics, adjacency and order are
treated as informative signals about channel roles (Li and
Kannan 2014; Anderl et al. 2016) and touchpoint contribu-
tions to consideration (Baxendale et al. 2015). When con -
versational discovery becomes a common first touch, two
failure modes follow. First, path-based models may attribute
upstream influence to the first observable non-LLM touch -
point (for example, a retailer product detail page), inflating
the apparent marginal contribution of lower-funnel interac -
tions. Second, common “funnel health” diagnostics that rely
on counts of early-stage touches (for example, the number
of review sites visited) can register reduced upper-funnel
engagement when those behaviors have migrated into the
LLM interface.
This issue is operational rather than hypothetical. Mar -
ketplace advertisers increasingly manage and allocate spend
using stage-specific funnel metrics (e.g., awareness, consid-
eration, purchase) at scale (Qin, Pauwels and Zhou, 2024).
If conversational discovery moves consideration into an
LLM interface that collapses multiple steps into a single
observed event, then early-stage activity can be systemati -
cally undercounted. A sudden increase in direct product-
page visits, faster apparent movement to intent, or fewer
visible review-site visits may appear to indicate improved
funnel efficiency. Among LLM-exposed users, however,
those same patterns may signal that consideration has
moved into conversational interfaces. That undercount can
inflate the apparent marginal contribution of lower-funnel
touchpoints and steer budget reallocation toward tactics that
merely appear to start the journey in clickstream logs. The
guardrail metrics proposed here are intended to identify that
measurement drift before it affects spend decisions. This
complements calls to keep analytics aligned with decision-
journey strategy rather than optimizing only what is most
visible in dashboards (V ollrath and Villegas 2022; Iacobucci
et al. 2019).
Operational controls for journey dashboards. For teams
running journey analytics in production, the following con-
trols can be implemented as routine diagnostics:
1. Treat LLM as a separate channel class.  Maintain a ver-
sioned list of LLM domains/app bundles and monitor
user-level first observed exposure timing.
2. Track observability alarms, not just performance KPIs.
Add time-to-intent distributions, direct transition prob -
abilities ( C → I, C → V ), and pre-intent LLM-touch
share as measurement-health indicators.
3. Stratify attribution outputs by LLM exposure.  Report
channel contributions separately for LLM-exposed and
non-exposed journeys to reduce first-observed-touch
misattribution.
4. Audit conversion-proximate evidence routinely.  Run
recurring targeted checks on checkout/cart/retailer-link
signals and escalate drift before model refreshes.
These measures function as observability guardrails. Com -
pression and transition directness indicate how much of
the journey may have become unobservable under con -
ventional channel taxonomies, while transition matrices
retain the non-linear structure of browsing. In practice, they
complement attribution models by indicating when the mea-
surement environment has changed. A shift toward higher
direct transitions and shorter time-to-intent may reflect
increased exposure to conversational intermediaries rather
than a genuine improvement in media efficiency. Journey
dashboards should therefore treat unusually direct consid -
eration-to-intent movement as an observability alarm, not
automatic evidence of improved media performance. In this
setting, the limiting factor is often not model complexity but
whether the measurement layer still reflects how discovery
is actually observed.
Limitations and future research
This paper makes a descriptive measurement claim, and the
evidence is matched to that claim. It does not claim causal
identification. Users self-select into LLM usage, and the
exposure-timing construct is first observed usage within the
observation window rather than first-ever adoption. Passive
logs do not observe conversational content, within-interface
comparison, or cognitive effort, so the analysis is about
observable journey structure. The main inferential claims
therefore rest on the best-validated layers: stage for consid-
eration and intent, and canonical exposure detection. Con -
version-proximate classification, entity breadth, and price
semantics remain secondary audited layers. The observation
window is one month and should be replicated across longer
windows, categories, and platforms.
Future work can extend this framework in three direc -
tions. First, replication across longer windows and addi -
tional datasets would allow more stable estimation of
channel substitution in the pre-intent discovery mix. Second,
quasi-experimental exposure-timing designs (for example,
within-user event studies around first observed LLM usage)
could better separate behavioral change from selection.

C. J. Vargo et al.
Third, richer instrumentation, including consented capture
of conversational intent signals, could connect trace-level
compression to consumer-perceived effort and satisfaction.
Conclusion
LLM assistants are changing the observable structure of con-
sumer discovery. Journey analytics and attribution systems
that continue to assume search-led discovery will misstate
funnel length, timing, and channel roles once consideration
shifts into conversational interfaces. This paper provides
a measurement correction: it treats LLM usage as a first-
class touchpoint detectable in passive logs, operationalizes
a non-linear stage codebook suited to clickstream evidence,
and introduces journey-level metrics for compression, tim -
ing, discovery mix, and transition structure. The empirical
conclusion is equally bounded. Observed LLM exposure
reshapes the visible pre-intent discovery mix, and that result
survives adjustment and robustness checks. Broad accelera-
tion claims do not. The practical response is to update mea-
surement, channel taxonomies, and dashboard diagnostics
so that hidden consideration is not mistaken for genuine
funnel improvement.
A survey covariates and analysis plan
A.1 Survey covariates
Table 6 lists survey constructs and item groups used for
adjustment and profiling.
Table 6 Survey covariates used for adjustment and profiling
Construct Variables (codebook labels)
News frequency NEWS1a–NEWS1f (newspaper,
broadcast, cable, social, radio,
political websites/blogs)
Media consumption/distrust CMEDIA1–CMEDIA4 (exist
outside, criticize, oppose, chal-
lenge mainstream news)
Digital media self-efficacy MDSE1–MDSE3 (spot fake
news, distinguish fake vs. legiti-
mate, identify inaccurate content)
Political/news interest APOL, newsint
Demographics birthyr, gender, race, educ, fam-
inc_new, employ, marstat, own-
home, urbanicity2, inputstate,
child18, immigrant, smoke100
Weights weight
 NEWS = News-frequency scale, CMEDIA = Media consumption/dis-
trust scale,  MDSE = Digital media self-efficacy scale
A.2 Analysis plan mapping
Table 7 maps each hypothesis to outcomes, model classes,
and primary reported outputs. Table 8 reports standardized
mean-difference diagnostics.
Table 7 Hypotheses mapped to outcomes, models, and outputs
Hyp. Outcome Model Primary
outputs
H1 Funnel compression (count
+ time)
Frac-
tional
response
models
Coefficient
table, com-
pression
distribution
H2a/H2b Time to intent/
conversion-proximate
Survival
(Cox),
KM
curves
Hazard
ratios, tim-
ing plot
H3 Discovery mix (pre-intent
shares)
Frac-
tional
response
Discovery
mix bar
chart
H4 Transition structure Transi-
tion
deltas +
boot-
strap CIs
Transition
table and
anno-
tated text
summary
H5 Breadth (unique sources) Poisson Breadth
model
estimate
H6 Survey alignment Linear
profiling
(WLS)
SMD table,
profile
summary
H7 Moderation Interac-
tion
models
Interaction
coefficient
and sum-
mary text
KM = Kaplan–Meier,  CI  =  C o n fi d e n c e  i n t e r v a l , WLS  = Weighted
least squares
Table 8 Covariate balance diagnostics (standardized mean differences)
Covariate Mean
(LLM)
Mean (Non) SMD
MDSE (mean) 4.937 4.796 0.141
CMEDIA (mean) 4.160 4.152 0.007
NEWS (mean) 4.059 3.915 0.151
Birth year 1,973.757 1,972.199 0.099
Total events 9,144.368 3,049.619 0.431
Active days 25.676 21.965 0.372
Gender: male 0.546 0.478 0.137
Race: Black 0.146 0.139 0.019
Race: Hispanic 0.081 0.067 0.053
Race: Middle Eastern 0.000 0.002 − 0.071
Race: Native American 0.011 0.020 − 0.074
Race: Other 0.022 0.012 0.071
Race: Two or more races 0.054 0.032 0.107
Race: White 0.649 0.694 − 0.097
Education: 4-year 0.330 0.221 0.244
Education: High school
graduate
0.195 0.289 − 0.220
Education: No HS 0.038 0.047 − 0.047

LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in…
Table 8 Covariate balance diagnostics (standardized mean differences)
Covariate Mean
(LLM)
Mean (Non) SMD
Education: Post-grad 0.178 0.127 0.143
Education: Some college 0.178 0.216 − 0.095
SMD = Standardized mean difference (unweighted). Weighted SMDs
are not shown because weighted means were not exported in the cur -
rent analysis artifact
Appendix B: Implementation details for
labeling pipeline
This appendix consolidates low-level implementation
details referenced in the Methods section. The labeling sys-
tem uses strict no-lookahead context construction, stable
event_hash identifiers, and deterministic domain/app
hinting. Timeline context is trimmed to a fixed token budget
for batch inference to keep throughput stable across hard -
ware. Entity extraction includes a high-precision price pass
that restricts to rows with explicit currency/price tokens and
retains a price only when the output matches a token within
a fixed tolerance (±2%, ±5%, ±10%, ±15% in verification).
A token-only fallback is not used in the high-agreement
training set; unmatched or ambiguous multi-price records
remain missing. Additional infrastructure parameters (batch
sizes, GPU memory settings, and endpoint configuration)
are maintained in internal runbooks to preserve reproduc -
ibility without exposing implementation-specific creden -
tials or vendor identifiers.
Appendix C: LLM exposure definitions
The primary exposure definition used in the paper follows a
broader AI/LLM registry that underlies the user-level expo-
sure counts. It includes canonical LLM domains/apps as
well as adjacent conversational surfaces and wrappers that
can be identified in observed domain, URL, bundle, or text
fields. The stricter robustness definition retains only canoni-
cal LLM domains and app bundles that map directly to the
in-journey llm channel class (e.g., chat.openai.com,
claude.ai, gemini.google.com, perplexity.
ai) and their mobile app bundles. Table 5 compares head-
line results under the primary broad registry and the stricter
canonical definition.
Appendix D: Model specification registry
and reproducibility parameters
Table 9 documents the estimator-to-outcome mapping, core
specification, and operational settings used in the manu -
script’s reported models. This appendix is intended to make
model-choice rationale, parameters, and weighting/infer -
ence settings auditable in one place.
Table 9 Specification registry for main hypotheses
Hyp. Outcome(s) Model Specification
and parameter
settings
H1 Compression (count; time) Frac-
tional
logit
(GLM
Bino-
mial,
logit
link)
Unadjusted:
outcome
∼llm_
exposed
(exposure-state
contrast using
E). Adjusted:
adds baseline
activity (total
events, active
days), survey
covariates
(MDSE, CME-
DIA, NEWS),
and available
demographic
indicators.
Decomposition
table reports
G0/G1/G2
counts for
Apre  separa-
tion. Caseid-
clustered SE.
No user-spec-
ified starting
values
H2 Time-to-intent;
time-to-conversion-proximate
Cox pro-
portional
hazards
Durations in
minutes from
first consid-
eration; right
censoring
retained. Neg-
ative observed
lags recast
to censored;
durations ≤ 0
clipped to
10−6. Caseid-
clustered
robust vari-
ance. Penalizer
fallback lad-
der: 0.00, 0.01,
0.10, 1.00 if
convergence
fails

C. J. Vargo et al.
Table 9 Specification registry for main hypotheses
Hyp. Outcome(s) Model Specification
and parameter
settings
H3 Pre-intent channel shares (LLM,
classic search, retailer/mar-
ketplace, direct brand, review/
UGC, other)
Frac-
tional
logit
(GLM
Bino-
mial,
logit
link)
One model per
share outcome.
Same unad-
justed/adjusted
covariate
pattern as H1
(exposure-state
contrast). Apre
decomposition
is reported
separately to
avoid journey-
versus-user
conflation.
Caseid-clus-
tered SE. No
user-specified
starting values
H4 Transition deltas (C → I,
C → V , C → C)
Caseid
bootstrap
Differences
computed
as (LLM-
exposed minus
non-exposed)
transition
probabilities
from consid-
eration. Main
run uses 500
bootstrap
draws for 95%
percentile CIs
H5 Breadth (unique pre-intent
sources)
Poisson
GLM
(log link)
Unadjusted
and adjusted
specifica-
tions parallel
H1. Caseid-
clustered SE.
IRR reported
for adjusted
model
Table 9 Specification registry for main hypotheses
Hyp. Outcome(s) Model Specification
and parameter
settings
H6 Survey alignment (MDSE,
CMEDIA, NEWS)
Weighted
least
squares
Case-level
models with
provided sur-
vey weight.
Unadjusted:
outcome
∼ llm_
exposed.
Adjusted:
adds baseline
activity and
available
demographics
H7 Moderation (LLM × MDSE on
compression)
Frac-
tional
logit
interac-
tion
model
Model
includes llm_
exposed,
mdse_mean,
interaction
term, and
baseline activ-
ity controls.
Caseid-
clustered SE
for interaction
coefficient
 Main journey segmentation parameters are inactivity gap = 24 h
and maximum journey cap = 168 h. The summary sensitivity table
appears in Table 5; the full segmentation grid is reported in Table 10
Appendix E: Sensitivity analyses
Table 10 reports the full gap/cap grid summarized in the
main-text robustness discussion. Table 11 reports paired
within-user contrasts between non-augmented ( G1) and
augmented (G2) journeys for the 91 exposure-positive users
who contribute both states.
Table 10 Segmentation sensitivity grid (unadjusted)
Segmentation H1
compression
(AME)
H2 intent
(HR)
H4
C → I
diff
Gap 10 m; cap 6 h 0.002 1.116 0.052
Gap 10 m; cap 24 h 0.002 1.117 0.052
Gap 10 m; cap 72 h 0.002 1.117 0.052
Gap 30 m; cap 6 h 0.001 1.127 0.053
Gap 30 m; cap 24 h 0.001 1.114 0.053
Gap 30 m; cap 72 h 0.001 1.114 0.053
Gap 60 m; cap 6 h 0.000 1.185 0.053
Gap 60 m; cap 24 h 0.000 1.147 0.053
Gap 60 m; cap 72 h 0.000 1.149 0.053
Each row re-segments journeys with a different inactivity gap and
maximum journey cap, then re-estimates unadjusted H1 and H2
models and recomputes the C → I transition difference

LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in…
Table 11 Within-user augmentation contrasts among exposure-posi -
tive users with both G1 and G2 journeys
Outcome Paired
difference
95% CI Users
Compression (count) − 0.006 [− 0.015,
0.000]
91
Compression (time) − 0.155 [− 0.236,
− 0.085]
91
Pre-intent LLM share 0.030 [0.022, 0.038] 91
Pre-intent review/UGC share 0.013 [− 0.013,
0.040]
91
Breadth (unique pre-intent
sources)
0.044 [0.012, 0.083] 91
Paired differences are computed as user-level mean( G2) − mean(G1),
with bootstrap confidence intervals over caseids. Positive values
indicate larger metrics in augmented journeys
Execution parameters and software stack.  Main-paper
artifacts were generated with:
 python run_all.py –gap-hours 24 –cap-
hours 168
–bootstrap 500 –min-km-events-per-
group 10
The environment used Python 3.12.3 and core packages:
pandas 2.3.3, numpy 2.2.6, statsmodels 0.14.6, lifelines
0.30.1, matplotlib 3.10.8, and seaborn 0.13.2.
Author contributions  All authors contributed to conceptualization,
methodology, analysis, and writing.
Funding No external funding was received.
Data availability The data analyzed in this study are proprietary and
subject to third-party restrictions. Aggregated results and analysis code
availability are described below.
Code availability Analysis code is available upon request; repository
link available on request.
Declarations
Conflict of interest The authors declare no conflict of interest.
Ethical approval The study uses de-identified behavioral trace data
provided by a third-party passive measurement panel provider. The
protocol received exempt institutional review board approval.
Consent to participate Informed consent was obtained under the ap -
proved exempt protocol.
Consent for publication Not applicable.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t i  v e c o m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
References
Anderl E, Becker I, von Wangenheim F and Schumann JH (2016)
Mapping the customer journey: lessons learned from graph-based
online attribution modeling. Int J Res Market.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1
0 1 6 / j . i j r e s m a r . 2 0 1 6 . 0 3 . 0 0 1
Baxendale S, Macdonald EK and Wilson HN (2015) The impact of
different touchpoints on brand consideration. J Retail.  h t t  p s : /  / d o  i .
o  r g / 1 0 . 1 0 1 6 / j . j r e t a i . 2 0 1 4 . 1 2 . 0 0 8
Cameron AC and Miller DL (2015) A practitioner’s guide to cluster-
robust inference. J Human Res. 50 (2): 317–372.  h t t  p s : /  / d o  i . o  r g /
1 0 . 3 3 6 8 / j h r . 5 0 . 2 . 3 1 7
Colley RH (1961) Defining advertising goals for measured advertis -
ing results (DAGMAR). New York, NY: Association of National
Advertisers
Cox DR (1972) Regression models and life-tables. J R Stat Soc Ser B
(Methodol). 34 (2): 187–220.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 1 1 / j . 2 5 1 7 - 6 1 6
1 . 1 9 7 2 . t b 0 0 8 9 9 . x
Iacobucci D, Petrescu M, Krishen A and Bendixen M (2019) The state
of marketing analytics in research and practice. J Market Anal.
7:152–181. https:/ /doi.or g/10.10 57/s4 1270-019-00059-2
Kaplan EL and Meier P (1958) Nonparametric estimation from incom-
plete observations. J Am Stat Assoc. 53 (282): 457–481.  h t t  p s : /  / d
o  i . o  r g / 1 0 . 1 0 8 0 / 0 1 6 2 1 4 5 9 . 1 9 5 8 . 1 0 5 0 1 4 5 2
Kim S and Priluck R (2025) Consumer responses to generative AI
chatbots versus search engines for product evaluation. J Theor
Appl Electron Commer Res. 20 (2): 93.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 9 0
/ j t a e r 2 0 0 2 0 0 9 3
Lavidge RJ and Steiner GA (1961) A model for predictive measure -
ments of advertising effectiveness. J Market. 25 (6): 59–62.
https:/ /doi.or g/10.23 07/12 48516
Le XC (2023) Inducing AI-powered chatbot use for customer pur -
chase: the role of information value and innovative technology. J
Syst and Inform Technol. 25 (2): 219–241.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 0
8 / J S I T - 0 9 - 2 0 2 1 - 0 2 0 6
Lemon KN and Verhoef PC (2016) Understanding customer experi -
ence throughout the customer journey. J Market. 80 (6): 69–96.
https:/ /doi.or g/10.15 09/jm .15.0420
Li H and Kannan PK (2014) Attributing conversions in a multichan -
nel online marketing environment: an empirical model and a field
experiment. J Market Res. 51 (1): 40–56.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 5 0 9
/ j m r . 1 3 . 0 0 5 0
Lo Presti L, Maggiore G and Marino V (2021) The role of the chatbot
on customer purchase intention: toward digital relational sales.
Ital J Market. https:/ /doi.or g/10.10 07/s4 3039-021-00029-6
Luo X, et al (2023) Chatbots in e-commerce: the effect of chatbot lan-
guage style on customers’ continuance usage intention and atti -
tude toward brand. J Retail Consum Ser. 71:103209.  h t t  p s : /  / d o  i . o
r g / 1 0 . 1 0 1 6 / j . j r e t c o n s e r . 2 0 2 2 . 1 0 3 2 0 9
MacKinnon JG, Nielsen MO and Webb MD (2023) Cluster-robust
inference: a guide to empirical practice. J Econ. 232 (2): 272–
299. https:/ /doi.or g/10.10 16/j. jeconom.2022.04.001
McKinsey and Company (2009) ‘The consumer decision journey’.
Available at:  h t t  p s : /  / w w  w . m  c k i  n s e  y . c o  m /  c a p  a b i l  i t i  e s /  g r o w t h - m
a r k e t i n g - a n d - s a l e s / o u r - i n s i g h t s / t h e - c o n s u m e r - d e c i s i o n - j o u r n e y
(Accessed: 29 January 2026)
Papke LE and Wooldridge JM (1996) Econometric methods for frac -
tional response variables with an application to 401(k) plan par -
ticipation rates. J Appl Econ. 11 (6): 619–632

C. J. Vargo et al.
Qin V , Pauwels K and Zhou B (2024). Data-driven budget allocation of
retail media by ad product, funnel metric, and brand size. J Market
Anal. 12:235–249. https:/ /doi.or g/10.10 57/s4 1270-024-00294-2
Rennie A and Protheroe J (2020) ‘How people decide what to buy
lies in the "messy middle" of the purchase journey’, think with
google. Available at:  h t t  p s : /  / b u  s i n  e s s  . g o  o g l e  . c  o m /  a u n z  / t h  i n k  / c o n
s u m e r - i n s i g h t s / n a v i g a t i n g - p u r c h a s e - b e h a v i o r - a n d - d e c i s i o n - m a k i
n g /     (Accessed: 29 January 2026)
Vakratsas D and Ambler T (1999) How advertising works: what do we
really know?, journal of marketing, 63(1), pp. 26–43. Available
at: https:/ /www.js tor.org /stab le/1251992 (Accessed: 29 January
2026)
V ollrath MD and Villegas SG (2022) Avoiding digital marketing ana-
lytics myopia: revisiting the customer decision journey as a stra -
tegic marketing framework. J Market Anal. 10:106–113.  h t t  p s : /  / d
o  i . o  r g / 1 0 . 1 0 5 7 / s 4 1 2 7 0 - 0 2 0 - 0 0 0 9 8 - 0
Wijaya BS (2012) The development of hierarchy of effects model in
advertising. Int Res J Bus Stud. 5 (1): 73–85.  h t t  p s : /  / d o  i . o  r g / 1 0 . 2
1 6 3 2 / i r j b s . 5 . 1 . 7 3 - 8 5
Zimmermann R and Auinger A (2023) Developing a conversion rate
optimization framework for digital retailers–case study. J Market
Anal. 11:233–243. https:   //d oi. or g/10 .105 7/ s41 270-0 22-00161-y
Publisher's Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Chris J. Vargo  is an associate professor at the University ofColo -
rado Boulder. His research focuses on data analytics, digital adver -
tising, computational social science, social media data, machine
learning,content analysis, APIs, and advertising analytics.
Shahed Rahman is a PhD student in Advertising, Public Relations,
and Media Design at theUniversity of Colorado Boulder. His research
focuses on AI-generated advertising content, programmatic advertis -
ing, advertising technology, and factors that shape engagement with or
annoyance toward social media advertising.
Tobias Hopp is an associate professor in Advertising, Public Rela -
tions, and Media Design at the University of Colorado Boulder. His
research examines the uses and effects of digital and interactive media,
uncivil online communication, online political communication, and
organizational transparency.
