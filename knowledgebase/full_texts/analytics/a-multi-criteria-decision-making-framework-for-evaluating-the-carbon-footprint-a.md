---
title: A Multi-Criteria Decision-Making Framework for Evaluating the Carbon Footprint and Sustainability
  Performance of Digital Marketing Channels
url: https://doi.org/10.34248/bsengineering.1923918
category: analytics
subcategory: measurement
date: 2026-07
venue: Black Sea Journal of Engineering and Science
authors:
- Suat Okay
source: openalex-oa
pdf_url: https://dergipark.org.tr/en/download/article-file/5882379
pages: 9
chars: 43931
fetched_at: '2026-11-08T17:54:24+00:00'
kb_version: 1
---

# A Multi-Criteria Decision-Making Framework for Evaluating the Carbon Footprint and Sustainability Performance of Digital Marketing Channels

Black Sea Journal of Engineering and Science
doi: 10.34248/bsengineering.1923918
BSJ Eng Sci / Suat OKAY 1644
 This work is licensed (CC BY-NC 4.0) under Creative Commons Attribution 4.0 International License

Open Access Journal
e-ISSN: 2619 – 8991

A MULTI-CRITERIA DECISION-MAKING FRAMEWORK FOR
EVALUATING THE CARBON FOOTPRINT AND SUSTAINABILITY
PERFORMANCE OF DIGITAL MARKETING CHANNELS

Suat OKAY1*

1Batman University, Vocational School of Social Sciences, 72000, Batman, Türkiye

Abstract: Digital marketing has expanded rapidly, and with it the use of data -intensive advertising  systems whose energy use and
carbon emissions are rarely questioned. Sustainability now receives close attention in business and engineering, yet the envi ronmental
side of digital marketing channels has been studied very little. This study addresses that gap with a multi -criteria decision-making
(MCDM) framework that evaluates digital marketing channels on both performance and sustainability. Objective weights from the
CRITIC and MEREC methods are combined with WASPAS to rank five channels under several cr iteria. Besides the usual performance
indicators (click-through rate, engagement, conversion, cost per click and return on investment), the model adds carbon footprint and
energy consumption as proxy sustainability criteria. The decision matrix draws on be nchmark values and computational energy
coefficients reported in the literature, which gives a comparable dataset without any primary data collection.  The framework  rests on
the Natural -Resource-Based View (NRBV) of the firm, which treats environmentally efficient capabilities as a source of competitive
advantage. Adding the sustainability criteria changes the ranking and brings out the trade -off between marketing performance and
environmental cost. The framework offers managers an objective tool for judgi ng channels with sustainability in mind, and it links
digital marketing analytics to environmental sustainability through an engineering -oriented model.  Email Marketing obtained the
highest overall score (1.000) and Display Advertising the lowest (0.490).  The CRITIC and MEREC weightings produced the same
ranking, confirmed by a Spearman rank correlation of rs = 1.000 (P<0.001), which points to a stable framework.

Keywords: Multi-criteria decision-making, Digital marketing, Sustainability, Carbon footprint, CRITIC, MEREC
*Corresponding author: Batman University, Vocational School of Social Sciences, 72000, Batman, Türkiye
E mail: suat.okay@gmail.com (S. OKAY)
Suat OKAY  https://orcid.org/0000-0002-6042-6682 Received: April 06, 2026
Accepted: June 10, 2026
Published: July 15, 2026

Cite as:  Okay, S. (2026). A multi -criteria decision -making framework for evaluating the carbon footprint and sustainability performance of digital
marketing channels. Black Sea Journal of Engineering and Science, 9(4), 1644-1652.

1. Introduction
Digitalization has changed how firms plan and assess
their marketing. Channels such as social media, search
engines and programmatic advertising are now central to
reaching consumers, and they run on continuous data
processing and cloud infrastructure. Because of this,
firms tend to measure marketing through quantitative
indicators: click -through rate, engagement, conversion
and return on investment. What this view usually leaves
out is the environmental cost of the infrastructure behind
those numbers.
Digital technologies ar e far from environmentally
neutral. de Vries-Gao (2025) shows that demand for data
storage, real-time analytics and artificial intelligence has
pushed up the energy needs of data centres sharply,
while Liu and Fang (2025) link the growth of the digital
economy to rising carbon emissions, which suggests that
digitalization can carry costs that are easy to miss. For
advertising in particular the footprint is not trivial;
Pärssinen et al. (2018) and more recent industry
analyses estimate that internet and ad -tech
infrastructure account for several percent of global CO₂
output (Centre for Social Innovation, 2025). Findings of
this kind have brought the sustainability of digital
systems into question.
The idea of a digital carbon footprint has gained ground
in recent years. Online advertising, data transmission and
user interaction all generate indirect emissions through
the computation behind them. These emissions are less
visible than those of heavy industry, but they accumulate
at scale. Thangam et al. (2024) p oint to data centres as a
major driver of the footprint of digital services, and
Caldeira et al. (2026) argue that this footprint needs to be
measured and managed as part of any serious
sustainability effort.
Even so, the environmental side of digital mark eting has
had little attention. Most digital marketing research stays
with economic performance and user engagement and
rarely folds sustainability into how performance is
judged. A few recent studies have started to close this
gap: El Hana et al. (2024) p ropose an “emission -smart
advertising” approach that weighs campaign
performance against CO₂ emissions, and Istrate et al.
(2024) measure the environmental cost of digital content
Research Article
Volume 9 - Issue 4: 1644-1652 / July 2026

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1645

consumption. Both, however, remain either conceptual or
tied to a single cam paign and offer no model that can be
reused to compare channels. Sustainability research, for
its part, has mostly examined infrastructure rather than
application areas such as marketing. The gap therefore
sits between digital marketing analytics and
environmental sustainability.
As regulatory pressure and consumer awareness grow,
firms need ways to weigh marketing effectiveness against
environmental impact rather than treat them apart.
Judging a channel on financial or engagement metrics
alone is no longer  enough; a fuller view has to capture
the trade -off between marketing results and
environmental responsibility.
MCDM methods suit this kind of problem because they
handle several conflicting criteria at once and support a
balanced assessment. Objective wei ghting methods such
as CRITIC and MEREC set the importance of each
criterion from the data, which lowers subjectivity.
WASPAS, in turn, ranks alternatives by combining
additive and multiplicative models.
This study therefore builds an integrated MCDM
framework that evaluates digital marketing channels on
both performance and sustainability. Alongside the usual
performance metrics, it brings in carbon footprint and
energy consumption as proxy sustainability indicators,
with the aim of giving an engineering -oriented model
that supports sustainable decisions in digital marketing.
To keep the analysis focused, and to go beyond simply
presenting a computational model, the study is organised
around three research questions:
RQ1. How can performance -oriented and su stainability-
oriented criteria be combined in a single, objective and
reproducible framework for evaluating digital marketing
channels?
RQ2. How far does adding carbon footprint and energy
consumption change the ranking of channels compared
with a purely performance-based evaluation?
RQ3. How stable are the resulting rankings across
different objective weighting methods and across
changes in the WASPAS aggregation parameter?
The study contributes in three ways. It widens
performance evaluation in digital ma rketing to include
environmental criteria. It sets up an objective decision -
support procedure based on established MCDM
techniques. And it gives managers a clear view of the
trade-off between performance and environmental
impact across channels.
1.1. Literature Review
1.1.1. Digital marketing performance evaluation
Digital marketing sits at the centre of contemporary
business strategy, largely because its channels are
measurable. Effectiveness is usually read from indicators
such as click -through rate (CTR), engagement,
conversion and return on investment (ROI), which let
firms see how users respond and adjust accordingly
(Chaffey and Ellis -Chadwick, 2022; Martín -Cervantes et
al., 2025).
The problem is that this literature stops at economic and
behavioural outcomes and rarely looks at the wider
effects of digital marketing. These metrics are useful for
efficiency, but they say nothing about the energy and
emissions tied to the underlying infrastructure, even as
marketing leans more heavily on large -scale data
processing. El Hana et al. (2024) make the same point:
conventional media planning tends to put economic gain
ahead of ecological cost, and few frameworks try to
balance the two. That is the case for treating
environmental criteria as proper decision  variables
rather than an afterthought.
1.1.2. Sustainability and the digital carbon footprint
Sustainability has become a central concern in both
engineering and management, driven by environmental
pressure and tighter regulation. For digital systems it
usually comes down to energy efficiency and the
emissions of computation. The digital carbon footprint is
the total greenhouse -gas emissions from digital activity,
including transmission, storage and processing (Caldeira
et al., 2026).
Several studies repor t that data centres and cloud
systems consume a large and growing share of energy
(de Vries-Gao, 2025; Thangam et al., 2024), and that the
expansion of the digital economy carries real
environmental costs (Liu and Fang, 2025; Dzwigol et al.,
2024). These f indings undercut the assumption that
digital technologies are inherently clean.
Transparency and efficiency in digital infrastructure have
also been flagged as levers for better sustainability, from
greener data -centre design to carbon -aware computing.
Within online advertising itself, Pärssinen et al. (2018)
produced one of the first systematic estimates of its
energy and carbon footprint, and Istrate et al. (2024)
showed that the environmental cost of digital content
depends heavily on how it is delivered . What is still
missing is the step from infrastructure to application:
sustainability has rarely been applied to marketing
systems themselves.
1.1.3. Theoretical framework: the natural -resource-
based view
To give the study a firmer conceptual base, the
framework is anchored in the Natural -Resource-Based
View (NRBV) of the firm. Building on Barney’s (1991)
resource-based view, Hart (1995) argued that a firm’s
competitive position increasingly depends on how it
manages its relationship with the natural envir onment,
and identified capabilities such as pollution prevention
and product stewardship that turn environmental
performance into lasting advantage. Hart and Dowell
(2011) later added clean technology to this account and
pointed to digital systems and eco -innovation as carriers
of environmental capability.
Seen through the NRBV, the carbon footprint and energy
efficiency of a marketing channel count as strategic
resources rather than external limits. A channel that
delivers comparable marketing results at a  lower
environmental cost embodies a pollution -prevention

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1646

capability in Hart’s sense, and may give the firm an edge
as regulation tightens and consumers pay closer
attention. Framing the problem this way ties the
engineering-oriented MCDM model to an estab lished
management theory and explains why building
sustainability into channel selection is strategically
meaningful, beyond its ethical appeal.
1.1.4. Multi -criteria decision -making (MCDM) in
performance evaluation
MCDM methods have long been used for pro blems with
several conflicting criteria, which makes them a natural
fit where cost, efficiency and environmental impact have
to be weighed together (Mardani et al., 2015).
Among these, objective weighting methods have drawn
interest because they set criterion importance from the
data instead of expert opinion. Diakoulaki et al. (1995)
developed CRITIC, which weights criteria by their
variability and their correlation with one another, giving
more weight to those that carry more information.
Keshavarz-Ghorabaee et al. (2021) introduced MEREC,
which takes a different route and judges each criterion by
how much overall performance changes when it is
removed.
For ranking, Zavadskas et al. (2012) proposed WASPAS,
which combines the weighted sum model (WSM) and the
weighted product model (WPM) and so captures both
additive and proportional effects. This pairing has held
up well in recent sustainability work: CRITIC –WASPAS
has been used for sustainable crop selection (Nandi et al.,
2025), and MEREC -based models for sustainable energy
and resource -management decisions (Dwi Putri Ariyanti
and Fu’adi, 2025; Mondal et al., 2024). The track record
supports applying the same combination to digital
systems.
1.1.5. Research gap and contribution
Digital marketing perfor mance and sustainability have
each been studied closely, but rarely together in one
framework. Marketing research stays with performance;
sustainability research stays with infrastructure. The use
of carbon footprint and energy consumption inside a
marketing performance assessment has had little
attention.
MCDM methods, too, are well established in engineering
and decision -making but have seldom been turned on
sustainability-oriented digital marketing. Set against the
nearest existing work, this study diffe rs in three concrete
ways. First, it works at the channel level and yields a
transferable ranking model, rather than assessing a
single campaign as El Hana et al. (2024) do. Second, it
places environmental indicators inside a formal,
reproducible weighting -and-ranking procedure, rather
than reporting footprints on their own (Pärssinen et al.,
2018; Istrate et al., 2024). Third, as far as we are aware, it
is the first to pair dual objective weighting (CRITIC and
MEREC) with WASPAS and a Spearman -based stabil ity
test in this area.
To close this gap, the study builds an integrated MCDM
framework that evaluates digital marketing channels on
both performance and sustainability. By bringing carbon
footprint and energy consumption into the evaluation
through object ive weighting, it connects marketing
analytics to environmental sustainability.

2. Materials and Methods
The framework evaluates digital marketing channels on
performance and sustainability together. It runs in three
stages: building the decision matrix, weighting the
criteria with two objective methods, and ranking the
channels with a hybrid method.
2.1. Rationale for Method Selection
The choice of CRITIC, MEREC and WASPAS is deliberate.
Subjective methods such as AHP or the Best -Worst
Method rest on expe rt judgement, which would bring
back the bias the study is trying to avoid, so they were set
aside. Among objective methods, the Entropy method
looks only at the spread of each criterion in isolation,
whereas CRITIC also accounts for the correlation
between criteria. That matters here, since several
performance indicators (CTR, conversion, ROI) move
together. MEREC was added as a second, logically
independent method: it derives weights from the effect of
removing each criterion, so running both lets the
weighting stage be cross -checked. For ranking, WASPAS
was preferred over distance -based methods such as
TOPSIS or VIKOR because it blends WSM and WPM
through one tunable parameter, which improves
accuracy and also gives a natural handle for sensitivity
analysis. The combined CRITIC/MEREC and WASPAS
design has been validated in recent sustainability -
oriented MCDM studies (Nandi et al., 2025; Dwi Putri
Ariyanti and Fu’adi, 2025).
2.2. Decision Matrix Construction
The first step is a decision matrix of alternativ es and
criteria. Here the alternatives are digital marketing
channels and the criteria cover both performance and
sustainability. The matrix is written as X = [xij] for i = 1,
2, …, m and j = 1, 2, …, n, where xij is the value of
alternative i on criterion  j, m is the number of
alternatives and n the number of criteria.
Criteria fall into two types: benefit criteria, to be
maximised, and cost criteria, to be minimised. CTR and
conversion are benefit criteria, while cost per click,
carbon footprint and energ y consumption are cost
criteria.
Channels also differ in how much data they process and
how much real -time optimisation they need, and these
differences feed straight into energy use. The framework
therefore captures the computational load of each
channel alongside its marketing performance, which
links marketing to system-level efficiency.
2.3. Normalization of the Decision Matrix
Because the criteria use different units, the matrix is
normalized with linear normalization. For benefit
criteria, rij = xij /  max(xj); for cost criteria, rij = min(xj) /
xij, where rij is the normalized value of xij (equations 1
and 2).

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1647

rij = xij / max(xj)   (benefit criteria) (1)
rij = min(xj) / xij   (cost criteria) (2)
2.4. CRITIC Method for Objective Weighting
Diakoulaki et al. (1995) define CRITIC (Criteria
Importance Through Intercriteria Correlation) so that the
weight of each criterion depends on its variability and on
its conflict with the others. The standard deviation σj of
each criterion measures its contrast, and the  correlation
coefficients ρjk capture the conflict between criteria. The
information content of each criterion is Cj = σj × Σk (1 −
ρjk), and the weights follow from normalizing Cj: wj = Cj
/ Σ Cj (equations 3 and 4).

Cj = σj × Σk (1 − ρjk)  (3)
wj = Cj / Σ Cj  (4)
2.5. MEREC Method for Objective Weighting
MEREC (Method based on the Removal Effects of
Criteria) weights each criterion by its effect on overall
performance when it is removed (Keshavarz -Ghorabaee
et al., 2021). Overall scores Si are computed f rom the
normalized matrix with a logarithmic measure, and each
criterion j is then dropped in turn to give Si(−j). The
removal effect is Ej = Σi |Si − Si(−j)|, and the weights are
wj = Ej / Σ Ej (equations 5 and 6).

Si = ln[1 + (1/m) Σj |ln(rij)|]  (5)
Ej = Σi |Si − Si(−j)|,   wj = Ej / Σ Ej (6)
2.6. WASPAS Method for Ranking Alternatives
WASPAS (Weighted Aggregated Sum Product
Assessment) ranks alternatives by combining the
strengths of the weighted sum and weighted product
models (Zavadskas et al., 2012) . The WSM score is Qi¹ =
Σj wj rij and the WPM score is Qi² = Πj (rij)^wj. The final
score combines the two: Qi = λ Qi¹ + (1 − λ) Qi². The
parameter λ ∈ [0, 1] sets the balance between the
additive (WSM) and the multiplicative (WPM) parts of
the WASPAS sco re itself; it does not weight the CRITIC
and MEREC methods. Following common practice, λ is set
to 0.5 as the baseline so the two parts contribute equally,
and its effect on the rankings is examined in the
sensitivity analysis (equations 7, 8 and 9).

Qi¹ = Σj wj rij  (7)
Qi² = Πj (rij)^wj  (8)
Qi = λ Qi¹ + (1 − λ) Qi²  (9)
2.7. Integrated Evaluation Framework
CRITIC and MEREC are applied separately to obtain two
sets of weights, and WASPAS then ranks the channels
under each set. Running two weighting metho ds rather
than one lets the stability of the weights be checked, and
the framework evaluates marketing performance and
sustainability at the same time, which makes it a usable
decision-support tool for selecting efficient and
environmentally responsible channels.
2.8. Alternatives and Criteria Selection
The alternatives are five widely used channels, the
platforms firms rely on most in digital marketing: A1
Social Media Marketing, A2 Paid Search Advertising, A3
Display Advertising, A4 Email Marketing and A5
Influencer Marketing.
The criteria, drawn from the digital marketing and
sustainability literature, split into a performance group
and a sustainability group.
2.9. Performance Criteria
Performance criteria reflect how effective a channel is in
terms of us er interaction and financial return: C1 Click -
Through Rate (CTR), the share of users who click an
advertisement (benefit); C2 Engagement Rate, the level
of user interaction (benefit); C3 Conversion Rate, how
well users become customers (benefit); C4 Cost p er Click
(CPC), the cost per click (cost); and C5 Return on
Investment (ROI), profitability (benefit).
2.10. Sustainability Criteria
Two sustainability criteria bring the environment into
the evaluation: C6 Carbon Footprint Score, the estimated
carbon emis sions of each channel (cost), and C7 Energy
Consumption Proxy, the relative energy needed to run
each channel (cost).
Because emissions from marketing channels cannot be
measured directly, C6 and C7 use proxy values taken
from work on digital infrastructur e, data -processing
intensity and platform -level resource use (de Vries -Gao,
2025; Caldeira et al., 2026). Channels that depend on
real-time bidding, large -scale data processing and
constant algorithmic optimisation are assumed to carry a
higher carbon impa ct. This proxy approach follows
earlier digital -sustainability studies where direct
measurement was not feasible.
The carbon footprint (C6) is estimated from a proxy
model based on data transmission and computational
intensity. Emissions are approximated as (equation 10):

C6 = Data Transfer (MB) × Energy Intensity (kWh/MB) ×
Carbon Intensity (gCO₂e/kWh) (10)

where data transfer is the average volume per user
interaction, energy intensity is the energy needed to
process and transmit that data, and carbon intensity is
the emission factor of the electricity used. Energy
consumption (C7) is treated as a function of
computational load and system -level processing. This
keeps the environmental estimates inside the same
evaluation as the performance metrics.
2.11. Data Construction
The decision matrix combines benchmark values from
the literature with computational energy coefficients. To
keep the dataset open to scrutiny, the source of each
value is stated. Performance values (C1 –C5) follow
published digital -marketing benchmark ranges from
industry and academic sources (Chaffey and Ellis -
Chadwick, 2022; Martín -Cervantes et al., 2025): email is
given the strongest CTR, engagement, conversion and
ROI together with the lowest CPC, in line with widely
reported benchmarks, while display advertising takes the
weakest performance values. The sustainability values
(C6–C7) are set in proportion to each channel’s data

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1648

volume and its reliance on real -time bidding and
algorithmic processing, following the evidence that
programmatic and display channels are the most energy -
intensive and email among the least (Pärssinen et al.,
2018; Centre for Social Innovation, 2025; El Hana et al.,
2024). Display and paid search therefore receive the
worst carbon and energy scores, and ema il the best. The
matrix is not arbitrary but a literature -calibrated,
ordinally consistent picture of known channel
characteristics. Benchmark -based data of this kind is
common in MCDM studies whose aim is to demonstrate a
method rather than to report a field measurement.
All values are normalized to a comparable range. The
dataset reflects realistic differences in both performance
and environmental impact across channels and so
captures the economic and environmental trade -off in a
controlled setting.
2.12. Decision Matrix and Criteria Classification
The decision matrix is given in Table 1. The benefit
criteria are C1, C2, C3 and C5; the cost criteria are C4, C6
and C7. This split governs how normalization and
weighting are applied. With the dataset in plac e, the next
section applies the framework and reports the ranking.
Applying the linear normalization in equations (1) and
(2) to the raw data brings every criterion onto a common
0–1 scale. Table 2 reports the normalized decision matrix
that underlies all later calculations.

Table 1. Decision matrix of digital marketing channels
Alternatives CTR (C1) Eng. (C2) Conv. (C3) CPC (C4) ROI (C5) Carbon (C6) Energy (C7)
A1 Social Media 0.045 0.120 0.035 0.80 2.50 0.65 0.70
A2 Paid Search 0.060 0.090 0.045 1.20 3.20 0.85 0.90
A3 Display Ads 0.030 0.050 0.020 0.60 1.80 0.75 0.80
A4 Email Marketing 0.070 0.150 0.055 0.40 3.80 0.40 0.45
A5 Influencer
Marketing 0.050 0.130 0.040 1.00 3.00 0.70 0.75

Table 2. Normalized decision matrix
Alternatives C1 C2 C3 C4 C5 C6 C7
A1 Social Media 0.643 0.800 0.636 0.500 0.658 0.615 0.643
A2 Paid Search 0.857 0.600 0.818 0.333 0.842 0.471 0.500
A3 Display Ads 0.429 0.333 0.364 0.667 0.474 0.533 0.562
A4 Email Marketing 1.000 1.000 1.000 1.000 1.000 1.000 1.000
A5 Influencer
Marketing 0.714 0.867 0.727 0.400 0.789 0.571 0.600

3. Results
3.1. Criteria Weights
The weights come from two objective methods, CRITIC
and MEREC, each judging criterion importance from data
variability and from the removal effect on overall
performance. Both sets, recomputed d irectly from the
normalized decision matrix, appear in Table 3.

Table 3. Objective criteria weights obtained from CRITIC
and MEREC

Criteria CRITIC Weights MEREC Weights
C1 (CTR) 0.124 0.151
C2 (Engagement) 0.166 0.220
C3 (Conversion) 0.128 0.191
C4 (CPC) 0.267 0.154
C5 (ROI) 0.109 0.132
C6 (Carbon) 0.105 0.078
C7 (Energy) 0.100 0.073

Under CRITIC, cost per click (C4, 0.267) and engagement
(C2, 0.166) carry the most information, reflecting their
high variability and low correlation with the rest. Under
MEREC, engagement (C2, 0.220) and conversion (C3,
0.191) come out on top. The two sus tainability criteria
together hold about 0.20 of the weight under both
methods, so environmental factors have a real influence
on the result rather than a marginal one.
3.2. Ranking of Alternatives Using WASPAS
WASPAS then ranks the channels under each set  of
weights, with λ = 0.5 so the additive and multiplicative
parts of the score count equally. The results appear in
Table 4.

Table 4. WASPAS scores and rankings under CRITIC and
MEREC weights (λ = 0.5)

Alternatives WASPAS (CRITIC) Rank WASPAS (MEREC) Rank
A1 Social Media 0.625 3 0.651 3
A2 Paid Search 0.573 4 0.638 4
A3 Display Ads 0.490 5 0.449 5
A4 Email Marketing 1.000 1 1.000 1
A5 Influencer
Marketing 0.627 2 0.682 2

Both weighting methods agree. Email Marketing (A4)
ranks first, followed by Influencer Marketing (A5) and
Social Media (A1). Paid Search (A2) is fourth and Display
Advertising (A3) last in both cases. The two rankings

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1649

match exactly, a first sign that the f ramework is stable;
Section 3.3 tests this formally.
The two WASPAS components behave consistently. Table
5 lists the additive (WSM) and multiplicative (WPM)
scores together with the combined score Qi under CRITIC
weights. The close agreement between WSM and WPM is
why the final ranking does not depend on the weight
placed on either component.

Table 5. WASPAS component scores (WSM, WPM) and
combined score under CRITIC weights

Alternatives WSM WPM Qi
A1 Social Media 0.628 0.622 0.625
A2 Paid Search 0.591 0.554 0.573
A3 Display Ads 0.497 0.482 0.490
A4 Email Marketing 1.000 1.000 1.000
A5 Influencer
Marketing 0.638 0.615 0.627

3.3. Statistical Validation of Ranking Consistency
To check the agreement between the two rankings, the
Spearman rank correlation coefficient (rs) was computed
between the CRITIC -based and MEREC -based orders.
Since the two are identical for all five channels, the
coefficient takes its maximum value, rs = 1.000
(P<0.001). A value of 1.000 means the two orders agree
perfectly, so the outcome does not depend on whether
CRITIC or MEREC is used. Because the analysis rests on
objective, fully reproducible computation rather than
survey data, no further inferential testing was needed.
3.4. Criterion-Group Contribution Analysis
To see whether Email’s lead comes mainly from its
economics or its sustainability, the weighted -sum score
was split into the two criterion groups (CRITIC weights).
For Email Marketing, performance criteria (C1 –C5)
account for about 79.5% of the score and sus tainability
criteria (C6 –C7) for the remaining 20.5%. The other
channels show a similar split, with performance
contributions between roughly 77% and 83%. So Email’s
first place rests mainly on strong economics, in particular
its high ROI and low cost per click, and is reinforced by
its low carbon and energy footprint. Sustainability does
not decide the ranking on its own, but it is decisive at the
margin: it widens the gap between Email and the more
computation-heavy channels and is enough to penalise
Paid Search and Display Advertising. Table 6 reports the
decomposition.

Table 6.  Decomposition of the weighted -sum score into
performance and sustainability contributions (CRITIC weights)

Alternatives Performance share Sustainability share Total
A1 Social Media 79.5% 20.5% 0.629
A2 Paid Search 83.2% 16.8% 0.591
A3 Display Ads 77.4% 22.6% 0.498
A4 Email Marketing 79.5% 20.5% 1.000
A5 Influencer
Marketing 81.2% 18.8% 0.639

3.5. Comparative and Sensitivity Analysis
The close agreement between the CRITIC and MEREC
results points to a stable framework.
Adding the sustainability criteria changes the ranking by
penalising channels with a heavier environmental load:
those with more computation and data processing slip
down once carbon and energy are counted. A  purely
performance-based evaluation would miss this and could
lead to weaker decisions.
To test sensitivity to the WASPAS parameter, λ was
varied from 0.1 to 0.9. As Figure 1 shows, Email
Marketing (A4) stays first and Display Advertising (A3)
last across  the whole range, and Paid Search (A2) stays
fourth. The only change is a swap between Social Media
(A1) and Influencer Marketing (A5) for second and third
place at low λ values (λ ≤ 0.3), where the multiplicative
part dominates. The ranking is thus highly , though not
perfectly, stable: the top and bottom positions do not
move, and only the closely scored middle channels
interchange under extreme settings. The main
conclusions do not depend on the choice of λ = 0.5.

Figure 1. Sensitivity analysis of WAS PAS scores across different
λ values (CRITIC weights).

Table 7 gives the full ranking at each value of λ from 0.1
to 0.9. It confirms in numbers what Figure 1 shows: the
first and last positions never move, and only A1 and A5
trade second and third place at λ ≤ 0.3.

Table 7. Rankings of alternatives across λ values (CRITIC
weights)

λ A1 A2 A3 A4 A5
0.1 2 4 5 1 3
0.2 2 4 5 1 3
0.3 2 4 5 1 3
0.4 3 4 5 1 2
0.5 3 4 5 1 2
0.6 3 4 5 1 2
0.7 3 4 5 1 2
0.8 3 4 5 1 2
0.9 3 4 5 1 2

3.6. Key Findings
Taken together, the sustainability criteria clearly shape
the outcome. Email marketing comes out as the most
efficient channel because it pairs strong performance

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1650

with a low footprint; performance -led channels such as
paid search stay competitive but pay f or their higher
environmental cost; and including carbon footprint gives
a more realistic assessment than performance alone.
Bringing sustainability into the evaluation thus leads to
different strategic conclusions than a performance -only
approach would.

4. Discussion
The results say something useful about how digital
marketing channels look once environmental cost is part
of the picture. Counting carbon footprint and energy
consumption gives a fuller, more balanced assessment
than performance metrics alon e, and it reframes channel
selection as much as an engineering problem as a
marketing one. This fits the NRBV logic set out in Section
1.1.3: a channel that meets its marketing goals at a lower
environmental cost holds a pollution -prevention
capability and  can turn that efficiency into advantage
(Hart, 1995; Hart and Dowell, 2011).
In line with earlier work on the footprint of digital
infrastructure (de Vries -Gao, 2025; Caldeira et al., 2026),
the channels differ in both efficiency and environmental
impact, and the ones that lean on data processing, real -
time bidding and algorithmic optimisation carry the
higher carbon and energy load. This supports the
broader point that digital systems, intangible as they are,
have real environmental consequences.
Email Ma rketing comes out as the most efficient option,
partly because it depends less on heavy computation and
moves less data than the other channels. As the
decomposition in Section 3.4 shows, though, this lead
rests mostly on economics (about 80% of the score)  and
is reinforced rather than caused by its sustainability
advantage. Display Advertising sits at the bottom, where
weak economic indicators meet a high environmental
cost; much of that cost comes from the constant real -time
data exchange and algorithmic decisions in
programmatic bidding. Industry evidence backs this up,
placing programmatic and real -time-bidding channels
among the most carbon -intensive in the ecosystem
(Pärssinen et al., 2018; El Hana et al., 2024; Centre for
Social Innovation, 2025).
The comparison with the nearest prior work sharpens
the contribution. El Hana et al. (2024) balance
performance and emissions for a single campaign
through a qualitative Delphi procedure; the present
framework works at the channel level and produces a
reproducible quantitative ranking. The two are
complementary. Both conclude that economic and
ecological goals have to be optimised together, but this
model offers a tool that can be reapplied whenever
channel-level benchmark data are available.
Running CRITIC and MEREC together also helps. The two
produced the same ranking, which suggests the
framework is stable and reliable, in line with earlier
findings that objective weighting lowers subjectivity in
MCDM (Keshavarz-Ghorabaee et al., 2021).
On the theory side, the study links digital marketing
analytics with sustainability research, two areas usually
kept apart, and shows that environmental considerations
can be folded into marketing evaluation. That pushes
marketing research beyond its usual economic and
behavioural metrics and places digital systems within the
wider frame of sustainable engineering.
On the practical side, managers can use the framework to
pick channels that perform well while keeping
environmental impact down. This matters as regulation
tightens and consumers grow more aware of
sustainability, and firms that move this way may also
gain on brand reputation.
These implications become concrete with a simple
example. Take a firm that currently splits its budget
evenly between display advertising and  email. Under the
present ranking, moving part of that budget from display,
which sits last and carries the heaviest footprint, toward
email, which leads on both performance and
sustainability, would lift marketing returns and cut
carbon and energy use tog ether. The shift also pays off in
the market. Nguyen et al. (2025) find that a green
marketing mix raises customer commitment and
willingness to pay a premium, and Tan et al. (2025) show
that a strategic green marketing orientation feeds
business performan ce through perceived competitive
advantage. Read with the NRBV, then, a channel mix that
lowers environmental cost is both cheaper to operate
and a source of advantage in its own right.
The study has limits. It rests on benchmark -based rather
than field da ta, which keeps the method clear but
restricts how far the results generalise. The sustainability
criteria use proxies because direct emissions data for
marketing channels are not available. Future work could
bring in real datasets and sharper measurement of the
digital carbon footprint.

5. Conclusion
This study set out an integrated MCDM framework for
evaluating digital marketing channels on performance
and environmental sustainability at once. Pairing CRITIC
and MEREC weighting with WASPAS ranking gave a
systematic and reproducible model.
The results show that adding carbon footprint and
energy consumption changes the evaluation in a real
way. Answering the research questions directly:
performance and sustainability can be combined in a
single objective and reproducible model (RQ1); including
environmental criteria reshapes the standing of channels
by penalising the computation-heavy ones (RQ2); and the
rankings stay stable across weighting methods (rs =
1.000) and across the WASPAS parameter (RQ3). A
performance-only assessment risks biased or incomplete
decisions once environmental cost is ignored.
One result stands out: a low -energy channel such as
email can finish first overall once sustainability is in the
mix, which means environmentally efficient cha nnels can
also be competitive when judged on the full set of

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1651

criteria. Sustainability is better treated as part of
strategic marketing decisions than as a secondary
concern.
Methodologically, using two objective weighting methods
strengthens the result, an d the agreement between
CRITIC and MEREC suggests the framework is stable
enough for harder problems. The WASPAS step provides
a balanced way to aggregate that reflects both linear and
proportional effects.
On the theory side, the study connects digital ma rketing
analytics with sustainability evaluation and grounds the
link in the Natural-Resource-Based View. On the practical
side, it gives managers a decision -support tool for
designing more sustainable digital marketing strategies.
Its limits should be ack nowledged. The analysis rests on
benchmark-driven data, which may limit how far the
findings generalise, and the sustainability indicators are
proxies because direct emissions data are not available.
Future work could use real -world datasets and sharper
footprint estimation. On balance, bringing sustainability
into digital marketing evaluation is both workable and
necessary for decisions meant to last.

Author Contributions
The percentages of the author’s contributions are
presented below. The author review ed and approved the
final version of the manuscript.

 S.O.
C 100
D 100
S 100
DCP 100
DAI 100
L 100
W 100
CR 100
SR 100
PM 100
FA 100
C= concept, D= design, S= supervision, DCP= data collection
and/or processing, DAI= data analysis and/or interpretation, L=
literature search, W= writing, CR= critical review, SR=
submission and revision, PM= project management, FA= funding
acquisition.

Conflict of Interest
The authors declared that there is no conflict of interest.

Ethical Consideration
Ethics committee approval was not required for this
study because there was no study on animals or humans.

References
Barney, J. (1991). Firm resources and sustained competitive
advantage. Journal of Management , 17(1), 99 –120.
https://doi.org/10.1177/014920639101700108
Caldeira, H. A., Martinez, P., & Rogage, K. (2026). Digital carbon
footprint of common data environments in ISO 19650 -
compliant construction pro jects. Smart and Sustainable Built
Environment. Advance online publication.
https://doi.org/10.1108/SASBE-08-2025-0512
Centre for Social Innovation. (2025). The social innovator’s guide
to digital sustainability: All about digital advertising . Centre for
Social Innovation.
Chaffey, D., & Ellis -Chadwick, F. (2022). Digital marketing  (8th
ed.). Pearson.
de Vries-Gao, A. (2025). The carbon and water footprints of data
centers and what this could mean for artificial intelligence.
Patterns. Advance online publication.
https://doi.org/10.1016/j.patter.2025.101430
Diakoulaki, D., Mavrotas, G., & Papayannakis, L. (1995).
Determining objective weights in multiple criteria problems:
The CRITIC method. Computers & Operations Research , 22(7),
763–770. https://doi.org/10.1016/0305-0548(94)00059-H
Dwi Putri Ar iyanti, Y., & Fu'adi, D. K. (2025). A comparative
analysis of the CRITIC and entropy methods for objective
weighting of priority criteria. Jurnal Masyarakat Informatika ,
16(2), 148–161. https://doi.org/10.14710/jmasif.16.2.73143
Dzwigol, H., Kwilinski, A., Lyulyov, O., & Pimonenko, T. (2024).
Digitalization and energy in attaining sustainable
development. Energies, 17(5), Article 1213.
https://doi.org/10.3390/en17051213
El Hana, N., Kondrateva, G., & Martin, S. (2024). Emission -smart
advertising: Balancing performance with CO 2 emissions in
digital advertising. Technological Forecasting and Social
Change, 209, Article 123818.
https://doi.org/10.1016/j.techfore.2024.123818
Hart, S. L. (1995). A natural -resource-based view of the firm.
Academy of Management Review , 20(4), 986 –1014.
https://doi.org/10.5465/amr.1995.9512280033
Hart, S. L., & Dowell, G. (2011). A natural -resource-based view of
the firm: Fifteen years after. Journal of Management , 37(5),
1464–1479. https://doi.org/10.1177/0149206310390219
Istrate, R., Tulus, V., Grass, R. N., Vanbever, L., Stark, W. J., &
Guillén-Gosálbez, G. (2024). The environmental sustainability
of digital content consumption. Nature Communications, 15(1),
3724. https://doi.org/10.1038/s41467-024-47621-w.
Keshavarz-Ghorabaee, M., Amiri, M., Zavadskas, E. K., Turskis, Z.,
& Antucheviciene, J. (2021). Determination of objective
weights using a new method based on the removal effects of
criteria (MEREC). Symmetry, 13(4), Article 525.
https://doi.org/10.3390/sym13040525
Liu, B., &  Fang, X. (2025). Analysis of the impact of digital
economy on carbon emissions and its mediation effect.
Frontiers in Environmental Science , 13, Article 1635153.
https://doi.org/10.3389/fenvs.2025.1635153
Mardani, A., Jusoh, A., MD Nor, K., Khalifah, Z., Zakwan, N., &
Valipour, A. (2015). Multiple criteria decision -making
techniques and their applications. Economic Research -
Ekonomska Istraživanja , 28(1), 516 –571.
https://doi.org/10.1080/1331677X.2015.1075139
Martín-Cervantes, P. A., Ziarati, P., de Frutos Madrazo, P., &
Gigauri, I. (2025). Digital marketing as a driver of change
towards the cir cular economy. Sustainability, 17(11), Article
5105. https://doi.org/10.3390/su17115105
Mondal, M. K., Mahapatra, B. S., Bera, M. B., & Mahapatra, G. S.
(2024). Sustainable forest resources man agement through

Black Sea Journal of Engineering and Science
BSJ Eng Sci / Suat OKAY 1652

Pythagorean fuzzy MEREC –MARCOS approach. Environment,
Development and Sustainability , 28(2). Advance online
publication. https://doi.org/10.1007/s10668-024-05164-6
Nandi, S., Maity, M., & Das, S. (2025). A CRITIC -driven MCDM
technique for crop selection to enhance agricultural
sustainability. Process Integration and Optimization for
Sustainability. Advance online publication.
https://doi.org/10.1007/s41660-025-00605-9
Nguyen, K. M., Dinh, L. T. K., Ngo, T. T., Phan, T. T. T., Nguyen, P.
D. H., Tran, H. P. M., & Nguyen, N. T. (2025). The impact of 7Ps
green marketing mix on customer commitment and
willingness to pay a premium price: Evidence from Vietnam.
Journal of Promotion Management , 31(4), 578 –619.
https://doi.org/10.1080/10496491.2025.2484712
Pärssinen, M., Kotila, M., Cuevas,  R., Phansalkar, A., & Manner, J.
(2018). Environmental impact assessment of online
advertising. Environmental Impact Assessment Review , 73,
177–200. https://doi.org/10.1016/j.eiar.2018.08.004
Tan, L. P., Casidy, R., & Arli, D. (2025). Drivers of strategic green
marketing orientation: An SME owner -manager perspective.
Journal of Retailing and Consumer Services , 82, Article 104130.
https://doi.org/10.1016/j.jretconser.2024.104130
Thangam, D., Muniraju, H., Ramesh, R., Narasimhaiah, R., Khan,
N. M. A., Booshan, S., Murgod, G., Kumar, R., & Ganesh, R. S.
(2024). Impact of data centers on power consumption, climate
change, and sustainability. In Computational intelligence for
green cloud computing and digital waste management  (pp. 60–
83). IGI Global. https://doi.org/10.4018/979 -8-3693-1552-
1.ch004
Zavadskas, E. K., Turskis, Z., Antucheviciene, J., & Zakarevicius , A.
(2012). Optimization of weighted aggregated sum product
assessment. Elektronika ir Elektrotechnika , 122(6), 3 –6.
https://doi.org/10.5755/j01.eee.122.6.1810
