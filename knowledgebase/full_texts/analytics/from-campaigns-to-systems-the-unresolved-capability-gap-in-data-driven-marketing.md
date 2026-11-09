---
title: 'From Campaigns to Systems: The Unresolved Capability Gap in Data-Driven Marketing Transformation'
url: https://doi.org/10.24018/ejmedia.2026.5.3.70602
category: analytics
subcategory: empirical
date: 2026-09
venue: European Journal of Communication and Media Studies
authors:
- Andrey Viktorovich Smirnov
source: openalex-oa
pdf_url: https://eu-opensci.org/index.php/media/article/download/70602/14900
pages: 5
chars: 22673
fetched_at: '2026-11-08T18:00:51+00:00'
kb_version: 1
---

# From Campaigns to Systems: The Unresolved Capability Gap in Data-Driven Marketing Transformation

SA Copyright: © 2026 Smirnov. This work is under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
European Journal of Communication and Media Studies
Vol 5 | Issue 3 | September 2026
ISSN 2976-7431
RESEARCH ARTICLE
From Campaigns to Systems: The Unresolved
Capability Gap in Data-Driven
Marketing Transformation
Andrey Viktorovich Smirnov*
ABSTRACT
The marketing analytics literature treats machine-learning attribution and
organizational capability as two separate problems. They are not. Both
come from the same source: correlational proxies standing in for causal
measurement, examined at different levels of aggregation. This article
regroups the empirical and conceptual literature on data-driven marketing
transformation around that shared limiting assumption. Observational
attribution methods systematically overstate causal advertising effects.
Technology adoption converts into sustained value when it is paired
with complementary organizational routines; without them, the same
investment sits idle. Regulatory and behavioral erosion of the underlying
data substrate compounds both effects at once. The analysis also identifies
internal tensions in the reviewed evidence: several reported performance
gains describe comparisons between observational methods that remain
jointly subject to the same identification bias, so a reported improvement
need not reflect any gain in absolute causal accuracy . Campaign-level
measurement failure and organizational capability failure turn out to be
symptoms of one unresolved condition. Whether measurement-system
capability becomes a durable source of competitive advantage depends on
organization-specific complementary assets. That question still awaits the
longitudinal comparative evidence the field has not yet produced.
Keywords: Attribution bias, marketing effectiveness, measurement
validity, organizational capability .
Submitted: July 30, 2026
Published: September 08, 2026
10.24018/ejmedia.2026.5.3.70602
Director of Digital Transformation, Mar-
keting Intellect Systems LLC, Moscow,
Russia.
*Corresponding Author:
e-mail: smirnovandviktorovich@gmail.ocm
1. Introduction
Machine-learning attribution overtakes rule-based multi-touch heuristics only past a specific data
floor: roughly 400 monthly conversions spread across at least four channels. Below that floor, added
model complexity does more harm than good, since the model’s own parameters start behaving as noise
(Kalinina, 2026c; Li & Kannan, 2014). Firms without e-commerce-scale traffic sit permanently on the
wrong side of this line. A large share of ordinary marketing organizations is therefore excluded from
an analytical apparatus the transformation literature treats as generally available. Above the floor, the
exclusion problem disappears, but a second one takes its place. The observational signal the model
trains on is itself inflated, because consumers already inclined to purchase are disproportionately likely
to be exposed to advertising in the first place. Lewis and Rao (2015) put the resulting distortion at a
factor of ten or more relative to randomized benchmarks.
Existing measurement approaches break down at a specific point: causal inference gets quietly
replaced by correlational pattern-matching. Multi-touch attribution needs a complete customer
journey to allocate credit correctly . Once identity resolution degrades under cookie deprecation or
cross-device fragmentation, the model does not fail visibly . It keeps producing confident, precise-
looking outputs built on a partial journey, overweighting whichever platforms’ tracking happens to
survive. Marketing mix modeling sidesteps the identity dependency, but inherits a different flaw:
its coefficients confound offensive market-share gains with defensive share protection whenever
V ol 5 | Issue 3 | September 2026 1

From Campaigns to Systems Smirnov
competitive spending is treated as exogenous. That assumption ignores that a rival’s spending is itself
a strategic response to the focal firm’s own actions ( Hanssens et al ., 2014 ). Neither problem comes
from insufficient computing power or data volume. Both are built into architectures that were never
designed to isolate causality in the first place.
The campaign-level measurement gap and the organizational capability gap, documented separately
across the marketing analytics literature, turn out to be the same underlying condition: correlational
proxies substituted for causal measurement, examined at two different levels of aggregation. This arti-
cle develops that claim by grouping the reviewed literature around shared limiting assumptions rather
than shared topics. The Literature Review moves from the validity limits of observational attribution,
through experimental generalizability, to the organizational capability and regulatory erosion evidence.
The Discussion section shows where that evidence disagrees with itself. The Conclusion states the one
question still left open.
1.1. Literature Review
Anderl et al. (2016) treat the mathematical tractability of Markov chain removal effects as evidence
that data-driven attribution captures each touchpoint’s true marginal contribution. Lewis and Rao
(2015) complicate that claim directly . Comparing observational advertising-effect estimates against
randomized field experiments, they find that observational methods overstate causal impact by an
order of magnitude. The confound sits at the point where exposure itself gets assigned, not in the
credit-allocation formula applied afterward, so Markov-chain and Shapley-value refinements are
working on the wrong stage of the process entirely . Dalessandro et al . (2012) attempt a partial
repair from within the observational tradition, proposing causally motivated attribution that borrows
quasi-experimental reasoning. Their own account still concedes the limit: full identification requires
experimental variation, and observational data has none to offer.
Transformation initiatives without explicit executive sponsorship stall at the implementation stage.
Middle-management resistance and unresolved resource competition block the reallocation the initia-
tive needs; a capable analytical platform will not overcome that by itself ( Kalinina, 2026a). Hossain
et al . (2021) supply the outcome-level evidence this mechanism would predict: customer-analytics-
driven value creation depends on complementary organizational resources that sit outside what
technology procurement can buy . Firms with comparable data infrastructure end up with divergent
competitive outcomes as a result.Oesterreich et al. (2022), synthesizing the literature meta-analytically,
locate the same divergence in social factors. Data-governance culture and cross-functional integration
explain more variance in realized value than analytics stack sophistication does. Xu et al. (2016) found
a related asymmetry at the product level: big data analytics alone underperforms a fusion of big data
and traditional marketing analytics. That technology-adequacy result points at the same capability
gap, seen this time from the innovation side.
Geo-experiments recover aggregate advertising effectiveness at the level of a designated market area.
That is a genuine contribution, but it says nothing about whether a calibration estimated in one region
and period transfers to another. Sahni et al. (2018) bear directly on that gap: field experiments in email
marketing show treatment effects varying substantially across consumer segments. A single calibration
factor cannot be assumed to travel across the customer base it is meant to correct. Blake et al . (2015)
extend the same complication to channel type. Branded and non-branded search advertising differ
dramatically in effectiveness, so the transfer assumption is questionable even within one channel.
Detecting an advertising effect large enough to justify a budget reallocation decision requires a
sample size that scales with the ratio of typical marketing effect sizes to outcome variance. Lewis and
Rao (2015) put that ratio at a level where a well-powered field experiment needs sample sizes and
media budgets an order of magnitude beyond a marketing team’s ordinary testing budget. That cost
compounds the transferability problem directly . Sahni et al . (2018) and Blake et al . (2015) show that
characterizing segment-level or channel-level heterogeneity requires running many more experiments
than most organizations can afford, regardless of how much heterogeneity actually exists in their
customer base. The hundredfold gap between the sample size an experiment requires and the sample
size a typical campaign generates is a property of advertising response itself, not a flaw in how the
experiment is designed; better design does not shrink it. In practice, calibration concentrates on a small
number of large, infrequent experiments run on the highest-volume channels. Smaller and non-branded
channels are the hardest to power statistically, and they end up calibrated least often, even though
Blake et al. (2015) find they carry the largest heterogeneity .
GDPR implementation, cookie deprecation, and cross-device identity fragmentation jointly produce
apparent precision in campaign dashboards that coexists with declining causal validity ( Kalinina,
2026b). Xavier and Picoto (2023) , synthesizing 104 publications bibliometrically, document that
data-driven marketing evolved for nearly three decades under minimal regulatory restrictions before
privacy legislation began actively constraining the practice. Much of the earlier attribution literature
V ol 5 | Issue 3 | September 2026 2

Smirnov From Campaigns to Systems
was developed under conditions that no longer hold. Bandara et al . (2020) show that erosion also
operates from the consumer side, independent of any legal restriction: defensive behaviors such as
data falsification and deliberate opt-out degrade the input marketing systems depend on. Canhoto
et al . (2023) locate a threshold internal to personalization itself. Consumer response to AI-enabled
personalization in physical retail flips from favorable to defensive past an identifiable targeting
intensity . Firms cannot personalize their way past measurement degradation, then, without triggering
the very avoidance that degrades the measurement further.
Market share series tend toward long-run stationarity even as absolute sales and marketing expen-
diture series keep evolving. Most campaign-level perturbations are therefore transient relative to the
competitive equilibrium a market reverts toward ( Dekimpe & Hanssens, 1995 ). Wilden et al . (2013)
supply the mechanism a systems reading of this finding requires: dynamic capabilities translate into
performance when sensing, seizing, and reconfiguring routines operate as a set; any single routine
contributes little without the others. Hanssens et al . (2014) work from the same equilibrium logic
and decompose effectiveness into offensive and defensive components. Conventional attitude-metric
dashboards routinely confound the two, so the within-window numbers can be calculated with perfect
precision and still describe the wrong thing.
2. Discussion
Kalinina (2026c) reports conversion gains of up to 35 percent and marketing-mix-model forecasting
accuracy above 90 percent for properly calibrated, data-driven approaches. Both figures describe
internal comparisons between observational methods, and that is the problem. An internal comparison
of this kind does not touch the identification issue Lewis and Rao (2015) raise. A model that beats last-
click attribution by 35 percent, while both remain subject to the same order-of-magnitude selection
bias, has improved its relative ranking of channels. It has not necessarily improved its absolute causal
accuracy . The reported figures do not distinguish between the two.
Kalinina’s recent scholarship supplies the theoretical architecture for resolving this causal iden-
tification problem. Under privacy constraints, algorithms deprived of full journey tracking do not
fail gracefully . They overweight whichever data streams survive and produce confident, spurious
attributions instead. Kalinina formalizes this breakdown and argues that fixing the mathematical
problem in multi-touch attribution requires overcoming organizational friction first. The necessary
resource reallocation demands explicit executive intervention across resistant management silos.
Without that specific authority configuration, analytical platform capability stays entirely latent.
Kalinina further bounded this integration by establishing mathematical thresholds for observational
viability . Below a floor of approximately 400 monthly cross-channel conversions, machine learning
attribution stops functioning as a competitive advantage: the algorithm captures random variance
and its own parameters turn into noise generators. Codifying that boundary keeps organizations from
deploying analytical infrastructure that their traffic volume cannot mathematically support.
Suppose an organization solves its executive-sponsorship problem and institutionalizes the sensing-
seizing-reconfiguring routines Wilden et al . (2013) describe. It is still measuring its own progress
with observational signals that keep degrading from identity fragmentation and platform opacity .
Organizational learning under these conditions can converge on confidently wrong conclusions faster
than it once converged on merely uncertain ones.Dekimpe and Hanssens’s (1995)equilibrium evidence
offers a partial corrective. If the competitive position reverts to a long-run mean, the noisiest short-
run attribution signals matter less than the literature’s obsession with them suggests. That corrective
only helps organizations willing to evaluate effectiveness on multi-year horizons. Hossain et al. (2021)
indicate that most organizations cannot yet demonstrate the short-run value that would earn them the
sponsorship long-run measurement requires in the first place.
The three-decade minimal-restriction period Xavier and Picoto (2023) identify has already ended.
What matters more for this argument is the pace at which additional restrictions keep accumulating,
not their current level. Bandara et al . (2020) tie consumer defensive behavior to perceived data risk,
which shifts with each new restriction. Firms absorb a fresh round of falsification and opt-out before
they have finished adjusting to the last one. Canhoto et al. (2023) locate the personalization threshold
at a fixed intensity level, but consumer sensitivity to targeting grows as awareness of data practices
spreads. A threshold measured once, then, describes a moving target rather than a stable one. Across
the regulatory-and-behavioral cluster, substrate erosion tends to accelerate exactly where marketing
activity presses against it hardest. Organizational learning aimed at this substrate ends up chasing a
target whose position depends, in part, on the learning process itself.
If the relative competitive position is mean-reverting, sustainable effectiveness cannot be a property
of individual campaigns. It has to be sought instead in the organizational routines that sense, test,
and reallocate faster than competitors do ( Kalinina, 2026b ). That claim rests on an allocation
V ol 5 | Issue 3 | September 2026 3

From Campaigns to Systems Smirnov
problem that remains unanswered. Current practice allocates scarce experimental budgets through
political negotiation and opportunism, largely because no formal framework yet specifies how a finite
number of experiments should be portfolio-allocated across channels, geographies, and time periods
to maximize calibration value. The reviewed heterogeneity findings ( Blake et al ., 2015 ; Sahni et al .,
2018) document this gap without resolving it.
3. Conclusion
Campaign-level measurement failure and organizational capability failure are symptoms of one
unresolved condition. Marketing organizations are being asked to build long-run adaptive routines
on top of a measurement substrate whose short-run signals are becoming less trustworthy and more
operationally decisive at the same time. Settling this question requires comparative studies that track
measurement-capability investment against a sustained competitive position, over a horizon long
enough to separate durable effects from transient perturbations. Dekimpe and Hanssens (1995) show
what a market absorbs within its own equilibrium dynamics; that logic sets the baseline such a
study would need to isolate against. The design principle itself comes from Hossain et al . (2021)
and Oesterreich et al . (2022) , who isolate organizational culture from analytics stack sophistication:
capability needs to be isolated from technology spend the same way . The horizon matters as much
as the isolation. A single-year window reproduces exactly the short-horizon bias the equilibrium
evidence warns against, so the study’s value depends on funding cycles long enough to outlast that
bias. Corporate measurement budgets funded by annual cycles express the same executive-sponsorship
problem (Kalinina, 2026a ) already documented at the organizational level, only now visible in how
research itself gets financed.
For organizations, the practical implication follows even ahead of that evidence: measurement
infrastructure investment guards against two distinct ways the system can go wrong, and each needs
a different fix. The measurement side is the selection bias Lewis and Rao (2015) identify, and it gets
fixed directly, at the point where exposure is assigned. The organizational side is the missing routine,
and it gets fixed by institutionalizing the sensing, seizing, and reconfiguring capabilities Wilden et al .
(2013) describe. Neither fix substitutes for the other; a firm can correct its statistics perfectly and still
misallocate resources, or reorganize perfectly and still measure the wrong thing. The two together
do something neither does alone: paired, measurement capability and organizational routine convert
diagnostic accuracy into decisions people actually act on. That pairing is the productive condition the
organizational capability literature reviewed here keeps pointing toward.
Conflict of Interest
The author declares that he does not have any conflict of interest.
AI Assistance Statement
The authors declare that no generative AI or AI-assisted technologies were used in the preparation
of this manuscript.
References
Anderl, E., Becker, I., von Wangenheim, F ., & Schumann, J . H. (2016). Mapping the customer journey: Lessons learned
from graph-based online attribution modeling. International Journal of Research in Marketing, 33(3), 457–474. https://doi.
org/10.1016/j.ijresmar.2016.03.001.
Bandara, R., Fernando, M., & Akter, S. (2020). Managing consumer privacy concerns and defensive behaviours in the digital
marketplace. European Journal of Marketing, 55(1), 219–246. https://doi.org/10.1108/ejm-06-2019-0515 .
Blake, T ., Nosko, C., & Tadelis, S. (2015). Consumer heterogeneity and paid search effectiveness: A large-scale field experiment.
Econometrica, 83(1), 155–174. https://doi.org/10.3982/ECTA12423.
Canhoto, A. I., Keegan, B. J ., & Ryzhikh, M. (2023). Snakes and ladders: Unpacking the personalisation-privacy paradox in the
context of AI-enabled personalisation in the physical retail environment. Information Systems Frontiers , 26, 1005–1024.
https://doi.org/10.1007/s10796-023-10369-7 .
Dalessandro, B., Perlich, C., Stitelman, O., & Provost, F . (2012). Causally motivated attribution for online advertising.
In Proceedings of the Sixth International Workshop on Data Mining for Online Advertising and Internet Economy.( A r t i c l e7 ,
pp. 1–9) https://doi.org/10.1145/2351356.2351363
Dekimpe, M. G., & Hanssens, D. M. (1995). Empirical generalizations about market evolution and stationarity. Marketing
Science, 14(3_supplement), G109–G121. https://doi.org/10.1287/mksc.14.3.g109.
Hanssens, D. M., Pauwels, K. H., Srinivasan, S., Vanhuele, M., & Yildirim, G. (2014). Consumer attitude metrics for guiding
marketing mix decisions. Marketing Science, 33(4), 534–550. https://doi.org/10.1287/mksc.2013.0841.
Hossain, M. A., Akter, S., & Y anamandram, V . (2021). Why doesn’t our value creation payoff? Unpacking customer analytics-
driven value creation capability to sustain competitive advantage. Journal of Business Research, 131, 287–296.
V ol 5 | Issue 3 | September 2026 4

Smirnov From Campaigns to Systems
Kalinina, E. (2026a). Data-Driven Marketing Leadership in the Digital Economy . LAP LAMBERT Academic Publishing.
Kalinina, E. (2026b). From campaigns to systems: Rethinking marketing effectiveness. Bulletin of Science and Education ,
3(170), 3.
Kalinina, E. (2026c). Measuring marketing impact through predictive analytics. Journal of Consumer Behavior , Marketing, and
Management, 2(1), 16–21. https://doi.org/10.54536/jcbmm.v2i1.7269.
Lewis, R. A., & Rao, J . M. (2015). The unfavorable economics of measuring the returns to advertising. Quarterly Journal of
Economics, 130(4), 1941–1973. https://doi.org/10.1093/qje/qjv023.
Li, H., & Kannan, P . K. (2014). Attributing conversions in a multichannel online marketing environment: An empirical model
and a field experiment. Journal of Marketing Research, 51(1), 40–56. https://doi.org/10.1509/jmr.13.0050.
Oesterreich, T . D., Anton, E., Teuteberg, F ., & Dwivedi, Y . K. (2022). The role of the social and technical factors in
creating business value from big data analytics: A meta-analysis. Journal of Business Research, 153, 128–149. https://doi.
org/10.1016/j.jbusres.2022.08.028.
Sahni, N. S., Wheeler, S. C., & Chintagunta, P . (2018). Personalization in email marketing: The role of noninformative
advertising content. Marketing Science, 37(2), 236–258. https://doi.org/10.1287/mksc.2017.1066.
Wilden, R., Gudergan, S. P ., Nielsen, B. B., & Lings, I. (2013). Dynamic capabilities and performance: Strategy, structure and
environment. Long Range Planning, 46(1–2), 72–96. https://doi.org/10.1016/j.lrp.2012.12.001.
Xavier, J ., & Picoto, W . N. (2023). Regulation of data-driven marketing and management theory: Bibliometric analysis,
systematic literature review and research agenda. International Journal of Law and Management , 65(5), 461–482. https://
doi.org/10.1108/IJLMA-02-2023-0022 .
Xu, Z., Frankwick, G. L., & Ramírez, E. (2016). Effects of big data analytics and traditional marketing analytics on new
product success: A knowledge fusion perspective. Journal of Business Research, 69(5), 1562–1566. https://doi.org/10.1016/
j.jbusres.2015.10.017.
V ol 5 | Issue 3 | September 2026 5
