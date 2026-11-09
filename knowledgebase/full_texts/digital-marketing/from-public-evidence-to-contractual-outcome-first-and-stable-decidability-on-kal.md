---
title: 'From Public Evidence to Contractual Outcome: First and Stable Decidability on Kalshi'
url: https://arxiv.org/abs/2609.16642
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Maksym Nechepurenko
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.16642
pages: 13
chars: 26563
fetched_at: '2026-11-08T13:19:42+00:00'
kb_version: 1
---

# From Public Evidence to Contractual Outcome: First and Stable Decidability on Kalshi

ForesightFlow Research·Event-Linked Perpetuals·Paper 7.3
From Public Evidence to Contractual Outcome
First and Stable Decidability on Kalshi
Maksym Nechepurenko
Research Department of Devnull FZCO, Dubai, UAE
maksym@devnull.ae ORCID 0000-0002-9515-8841
September 2026 | Version r0.9.3
Abstract
Public evidence can become sufficient to settle a prediction-market contract before the
venue records its first determination, but the relevant boundary depends on the applicable
rule version, exact release object, source hierarchy, correction history, and unfinished contract
conditions. This paper defines two Kalshi clocks:first decidability, the earliest contempo-
raneous singleton in the rule–evidence mapping, andstable decidability, the retrospective
earliest time after which the same singleton remains unchanged through finalization.
A completed retrospective identification test establishes a narrow but consequential
feasibility result. In a frozen blind pilot, all 25 identities and blinding checks passed and
current rule text was recovered for all 25; no exact or bounded historical rule version and no
exact or bounded official source-release object was recovered. The full historical recovery
covered 152,694 ordinary tickers, 11,530 exact event identities, and 6,540 read-only official
requests, with zero historically eligible events and zero historically eligible tickers. This is an
observability result, not a claim that no market was decidable or that public evidence never
existed.
A completed prospective infrastructure shakedown established observation capability for
three source programmes across 25 markets, with integrity revalidation of 781,266 lifecycle
frames, 22 closed lower-bounded reconnect receipts, no unresolved reconnect gap, no due-but-
missed official release, and an inactive price layer. Production evidence enrollment is active.
The prospective sample is constructed only at enrollment close from prospectively frozen
identities and pre-outcome fields; its frozen target size is selected mechanically under the
registered full, reduced, exploratory, or no-go support disposition. No contractual-decidability
clock, human-adjudication, price, or cross-venue result is reported here.
Keywords:prediction markets; contractual decidability; adjudication; public evidence; Kalshi.
JEL:G13, G14, G18.
ELP — Kalshi Research Track.This paper forms part of the Kalshi-focused research track within the
Event-Linked Perpetuals series.
1
arXiv:2609.16642v1  [q-fin.TR]  15 Sep 2026

1 Introduction
A real-world event, a source publication, a contractually sufficient evidence set, and a venue
determination are different objects. They may occur close together, but no identification strategy
may assume that they do. Close-to-determination time can include source delay, contractual
waiting, ambiguity, venue review, or unobserved procedure. A useful decomposition requires a
clock upstream of venue action.
The phrase “the outcome was knowable” is too loose. This paper instead studies public
contractual sufficiency under the applicable recorded rules. A market is first-decidable when
contemporaneously available admissible evidence reduces the contract’s settlement mapping to
one value and no contract-required future condition remains. Because source corrections or rule
clarifications can reopen that mapping, the paper separately defines a retrospective stable clock.
This distinction prevents an early but later reversed singleton from being treated as permanent
certainty.
The problem is related to semantic non-fungibility: apparently similar event claims can
differ in source, temporal scope, exceptions, and resolution semantics (Gebele and Matthes,
2026). It is also distinct from settlement manipulation, which concerns incentives to alter the
evidence-generating process rather than when the archived evidence becomes sufficient under
the contract (Dai et al., 2026).
Manual adjudication is costly, so the paper does not promise exchange-wide clocks. It
constructs a reproducible probability sample with explicit weights, blind review, and a measured
attrition ladder. An inability to identify a clock is a property of public governance observability,
not a missing value to be replaced by the venue’s own timestamp.
Settlement legibility has recently been used to explain which uncertainties become prediction-
market contracts at all (Adegbenro, 2026). This paper moves to a later and more granular
boundary: conditional on a listed contract and its contemporaneous rule graph, when does the
public evidence set first and stably imply one admissible settlement value? The first/stable
distinction and blind upstream adjudication are the paper’s core conceptual claims.
2 Rule–evidence model
For marketi, letΓ i(t)be the rule graph applicable at valid timet,Ei(t)the admissible public
evidence objects available byt, andYi the settlement-value set. Define
Ψi(t) = Ψi
(
Γi(t),E i(t)
)
⊆Y i.
2

The graph includes contract/series terms, market-specific primary and secondary rules, exact
source declarations, threshold and time-zone predicates, early-close clauses, and dated additional
details. Precedence is encoded only when the recorded materials establish it.
Definition 2.1(First decidability).
tf irst decide,i = inf{t:|Ψ i(t)|= 1and no contract-required future condition remains att}.
The definition is contemporaneous. It does not assume that a later source correction is impossible.
Definition 2.2(Stable decidability).Let y∗ i be the final archived settlement value. Stable
decidability is the retrospective clock
tstable decide,i = inf{t: Ψ i(s) ={y ∗ i}for every observed rule/source versions∈[t,t f inal,i]}.
It is a robustness clock, not a real-time information set available to traders.
Contract /
series terms
Market-
specific rules
Additional details
Versioned re-
lease objects
Ψi(Γi(t),E i(t))
admissible outcomes
Singleton outcome
if unique
Figure 1:Contractual-decidability graph. A named source is one input; the rule–evidence mapping
determines whether the admissible outcome set is a singleton.
Proposition 2.3(Named-source insufficiency).A source name and publication timestamp do
not generally identify contractual decidability.
Different strikes, exception clauses, time windows, source hierarchies, or pending future
conditions can map the same release to different admissible outcome sets.
Proposition 2.4(Interval evidence induces latency bounds).Iftdecide∈ [ai,b i]and tdet is exact,
then
tdet−t decide∈[t det−b i, tdet−a i].
No point estimate is identified without an additional model for the location of the clock inside
the interval.
Criterion 2.5(No determination-defined decidability).Venue determination or final outcome
may not be used to construct the blind upstream clock. Doing so would mechanically force
determination latency toward zero and introduce hindsight.
3

3 Retrospective identification test
The historical ordinary-market frame remains a venue-side feasibility denominator. It contains
152,694 exact ordinary tickers and 11,530 exact event identities; the completed recovery issued
6,540 read-only official requests. In the frozen 25-market blind pilot, 25/25 identities were
auditable, 25/25 blinding checks passed, and current rule text was recovered for 25/25. Yet
exact or bounded historical rule versions were recovered for 0/25 and exact or bounded official
source-release objects for 0/25. Across the full historical recovery, the number of historically
eligible events is zero and the number of historically eligible tickers is zero.
The registered public historical record therefore did not identify the version-bound rule object
and official release object required to reconstruct the contractual-evidence clock at the accepted
evidence grade. This finding does not say that the contracts were not decidable, and it does not
assert that public evidence never existed. It says that the required historical binding cannot be
reconstructed from the available public record. The historical pilot is complete and is not an
active 500-market execution plan.
4 Prospective evidence-capture amendment
The prospective infrastructure shakedown started atTC0 = 2026-09-01T22:31:38Z and passed all
gates atTPROD = 2026-09-04T22:54:26Z after 260,568 seconds (72 hours 22 minutes 48 seconds)
of valid observation. It established observation capability for prospectively frozen market,
event, and series identities; English-locale rule versioning; official source-release observation;
exact and bounded publication-time semantics; and separate rule/source, venue-outcome, price,
and concurrent public metadata layers. The shakedown validated infrastructure and adapter
capability to preserve source corrections and revisions. It covered the BLS CPI, FOMC target-
rate, and Federal Register executive-order programmes across three events and 25 markets.
These programmes demonstrate observation capability only and are not an empirical cohort; the
Federal Register subset was conformance-only.
The shakedown recorded 781,266 lifecycle frames, completed a full integrity revalidation,
classified 22 reconnect receipts as closed lower bounds, and found no unresolved reconnect gap.
There were no due-but-missed official releases, and the price layer remained empty. Concurrent
public Polymarket metadata produced 1,405 preliminary candidates, none semantically accepted.
Sustainability checks passed for 30, 42, and 60 days. These facts establish observation capability,
not a source-programme sample or a contractual-decidability result.
Prospective enrollment begins atTPROD, 2026-09-04T22:54:26Z. The primary enrollment
interval starts at that instant and ends immediately before 2026-10-04T22:54:26Z. The registered
42-day total enrollment ceiling is 2026-10-16T22:54:26Z, a possible 12-day extension beyond
4

the 30-day primary enrollment rather than an additional 42-day extension. The event horizon
is 2026-10-19T22:54:26Z; hard follow-up ends 2026-11-03T22:54:26Z. Shakedown observations
are excluded by default unless a separately frozen no-outcome-leakage rule passes. Only post-
enrollment receipts may support the prospective study.
5 Sample design and prospective frame
The final prospective frame is built at enrollment close. It uses prospectively frozen identities
and only pre-outcome source class, market form, and expected horizon. Venue outcome,
determination, finalization, endpoint class, and price path are excluded from sampling and initial
blind adjudication.
Before outcome inspection, the registered support disposition selects a frozen targetn∗:
full support sets n∗ = 500when at least 500 blind-adjudicable markets, 100 independent
release/event clusters, ten rule/series families, three source classes, and 80 percent exact-or-
bounded rule/source support are present; reduced support setsn∗ = 150when at least 150
markets and 40 clusters are present; exploratory support setsn∗ = 50when at least 50 markets
and 20 clusters are present; otherwisen∗ = 0and the disposition is no-go. In a simple random
full-support sample,n∗ = 500gives a worst-case 95 percent margin of error of approximately
0.044for a proportion; stratification, clustering, weights, and adjudication attrition can widen
that precision. These rules are frozen before outcome inspection.
5.1 Pre-outcome strata and deterministic allocation
The primary stratum is constructed from variables known without venue outcome or post-
outcome latency: source-class bucket, binary/scalar market form, and expected horizon from the
recorded pre-outcome schedule. Sparse cells are deterministically merged into an explicit residual
cell within market form before allocation. LetNh be the resulting stratum size. Allocation uses
square-root size weights,
ah =
√
Nh, n (0) h =n ∗ ah∑
kak
,
with a minimum of two observations for an eligible non-empty stratum, a cap atNh, and
deterministic largest-remainder adjustment until∑ hnh = n∗. The inclusion probability is
πi =n h/Nh and the analysis weight is1/πi.
Within each stratum, prospectively enrolled market identities are ordered by
DeterministicOrder(sprod,market identifier),
where the deterministic production seed is defined in the sampling protocol supplied with the
5

replication materials. The lowestnh values are selected. The algorithm is specified here; the
actual registry is generated at enrollment close and receives an inclusion-probability audit.
5.2 Pilot and independent second review
A completed 25-market historical feasibility pilot tested packet construction, rule-version recovery,
exact release-object recovery, packet blinding, time per packet, clock grades, and disagreement
coding; it is not merged into the prospective frame. A future prospective process check, if
required, is governed by the same no-outcome-leakage and independent-selection rules.
At least 20 percent of the sample, with a target minimum of 100 eligible packets, receives
independent second review. Operationally, the independently selected count is nsecond =
min{n∗,max (⌈0.20n∗⌉,min (100,n ∗))}, so it cannot exceed the realised sample and 100 remains
a target rather than an achieved result. The subset is selected by deterministic order using a
third seed defined in the sampling protocol. A separate conflict-enriched audit can be added,
but it is not mixed with the probability-based reliability subset.
6 Population and lifecycle authorities for sampling
The KMVE V1 authority closes the seven-day MVE market-object population at 7,611,594
exact REST tickers, 5,262,526 exact event keys, three current-validated collection identities,
and 83,701 selected-leg primitives (Nechepurenko, 2026a). These objects are useful for depen-
dence diagnostics and a small exploratory MVE stratum, not for an unrestricted child-ticker
adjudication sample.
The historical venue-side frame provides a feasibility denominator but does not construct
contractual-decidability clocks or a historically admissible clock cohort. Paper 7.1 supplies the
152,694 ordinary-market frame and lifecycle/endpoint authority, while Paper 7.2 supplies the
MVE hierarchy relevant to dependence and pseudoreplication (Nechepurenko, 2026c; Nechep-
urenko, 2026b). The prospective programme provides infrastructure capability and an active
enrollment design; it does not yet report clock values. Table 1 separates completed evidence
from the registered follow-up.
6

Table 1:Evidence availability for Paper 7.3 after the historical feasibility test and prospective shakedown.
Layer Current state Consequence
Historical feasibility
denominator
152,694 exact ordinary
tickers; 11,530 exact
event identities
Completed recovery; not a prospective sampling
frame
Historical rule/source binding 0 historically eligible
events; 0 historically
eligible tickers
No historical contractual-decidability cohort at the
accepted evidence grade
MVE population hierarchy 7,611,594 objects with
exact parent/leg fields
Exploratory event/collection stratum; no
unrestricted child-ticker sampling
Prospective shakedown 72-hour capability check
passed across three
source programmes
Supports enrollment, not a clock estimate
Prospective enrolled frame Built at enrollment close
if support thresholds
pass
Frozen n∗ sample or registered reduced, exploratory,
or no-go disposition
First/stable decidability Not yet adjudicated
prospectively
Core Paper 7.3 outcome remains to be measured
Blind packet and review
protocol
Specified Human adjudication begins only after registered
prospective frame verification
6.1 Blinding boundary
Sampling and initial blind review may use exact identity, recorded pre-outcome rule fields,
source declarations, expected horizon, and market form. They may not expose the venue result,
determination time, finalization time, endpoint class, determination-to-endpoint duration, or
later price path. After the initial review record is preserved, later linkage reveals venue clocks
and final value for consistency checks and latency construction. A contradiction creates a new
adjudication version; it never overwrites the initial record.
6.2 No broad rules crawl
The packet builder uses prospectively archived versioned rule objects, prospectively archived
official source objects, contemporaneous receipts, and revision/supersession graphs for the
selected sample. Later retrieval may verify current availability; it cannot create missing valid-
time evidence after the fact. The 7.6-million-object MVE population is not a rules-crawl
denominator.
7

7 Blind adjudication protocol
Adjudication proceeds in two phases.
Initial blind review.The reviewer receives exact identities, rule versions, candidate source
declarations, and archived source releases, but not Kalshi’s result, determination timestamp, or
finalization timestamp. The reviewer selects the applicable release object, evaluates each rule
predicate, and records first and stable decidability as an exact time, interval, proxy, unmeasured,
or conflict.
Later venue linkage.After the initial review record is preserved, the venue clocks and final
value are introduced. Contradictions create a new adjudication version; they do not overwrite
the initial review.
At least 20 percent of the sample, with a target minimum of 100 eligible packets, receives
independent second review. The operational count is bounded by the realised sample, so
the target minimum is not described as achieved when fewer than 100 eligible packets are
available. A conflict-enriched secondary audit is reported separately and is not mixed with the
random reliability subset. Agreement is reported as raw agreement and Cohen’sκ for nominal
fields (Cohen, 1960); clock agreement uses interval overlap and absolute boundary differences.
Prevalence-sensitive interpretation ofκis explicit.
Eachpacketrecordssource-objectidentity, publicationtime/interval, rulepredicates, candidate
outcome set, first/stable clocks, exclusion category, reviewer, and version lineage.
Public source
First
decidability
Venue
determination
Finalization
LP F LF D venue path
Stable decidability
(retrospective)
rule and source revision history
Stable decidability is retrospective; its times-
tamp may precede or follow venue determination.
Figure 2:First and stable decidability under a partial order. Source publication precedes first decidability
under the accepted packet, and venue determination precedes finalization. Stable decidability can fall
before or after venue determination; the dashed relations are analytical dependencies, not chronological
arrows.
8

8 Estimands and partial identification
Primary latencies are
LF D i =t det,i−t f irst decide,i, L SD i =t det,i−t stable decide,i,
with publication-to-first-decidability
LP F i =t f irst decide,i−t pub,i
and stability gap
Vi =t stable decide,i−t f irst decide,i.
If stable decidability occurs after venue determination,LSD < 0is not interpreted as negative
delay; it is a conflict class indicating that the venue acted before the publicly archived rule–
evidence sequence became retrospectively stable.
Fortclose <t det andtf irst decide≤t det, the bounded share of close-to-determination time occurring
after first decidability is
Qpost i = tdet,i−max(t close,i,t f irst decide,i) tdet,i−t close,i ∈[0,1].
This replaces an unbounded ratio that could exceed one when decidability preceded close.
Exact and interval clocks are reported separately. For thresholdx, interval observations yield
lower and upper indicators
I L i (x) = 1[Li≤x], I U i (x) = 1[Li≤x],
which bound the share determined withinx units of decidability. Midpoints are absent from
primary analysis.
The attrition ladder is
Nsample→N named source →N release object →N publication→N f irst→N stable→N latency.
It is reported by stratum with sampling weights. Cluster bootstrap uses source release as the
primary dependence unit, with event/series sensitivity.
9

9 Registered empirical questions
Q1 — Identification yield.What weighted share of sampled markets produces an exact first
clock, interval first clock, stable clock, or no admissible clock? No adjective such as “nontrivial”
is specified in advance.
Q2 — Positive residual latency.What is the identified share for whichLF D exceeds the
timestamp/interval precision tolerance? Exact and bounded shares are reported.
Q3 — Revision sensitivity.How often isVi > 0, and which source or rule mechanisms
account for the gap between first and stable decidability?
Q4 — Heterogeneity.How do identification yield andLF D vary by source class, market
form, horizon, and pre-outcome rule features? These are descriptive, with multiplicity correction
or hierarchical shrinkage if many contrasts are retained.
Q5 — Reviewer reproducibility.What are raw agreement,κ, clock-interval overlap, and
adjudicated boundary differences on the random audit subset?
Pseudo-source releases and generic homepage timestamps provide negative controls. Venue
close is an anchor substitution, while determination-as-decidability is shown only as a mechanical
pathology, not a competing estimator.
10 Validity and reproducibility
The design requires reproducible sampling without post-outcome timing fields, recorded rule
versions, exact source-object identity or an explicit failure classification, blind initial adjudication,
and independent review. A market lacking the required timing evidence is excluded from
the corresponding timing analysis while remaining visible in the observability and attrition
accounting.
The analysis distinguishes sample and weights, source-object attrition, first/stable clock
grades, reviewer reliability, latency bounds, source/rule heterogeneity, revisions and conflict
cases, and negative controls.
11 Limitations
Contractual sufficiency can be genuinely ambiguous. Public source pages can be revised or
overwritten, and the venue may use evidence not visible to the researcher. Stable decidability is
retrospective and must not be described as traders’ real-time knowledge. Human adjudication
remains judgmental despite blinding and replication. A stratified sample supports sample-
weighted claims, not automatic exchange-wide generalization when coverage or nonresponse is
uneven. LongL F D is a public-evidence residual, not a causal estimate of venue inefficiency.
10

12 Conclusion
The completed historical test establishes that a clock may be economically well-defined yet
retrospectively unobservable from the available public historical record. The historical ordinary
frame remains an important venue-side feasibility denominator, but it cannot supply the version-
bound rule object and official release object required for the registered contractual-evidence
clock. The KMVE hierarchy remains available for a separately clustered exploratory MVE
extension without allowing millions of related child objects to dominate the statistical unit.
The prospective shakedown demonstrates source-observation capability and active evidence
enrollment. What remains is the paper’s core semantic measurement task: blind reviewers must
reconstruct exact rule versions and public release objects, identify first and stable decidability,
and preserve interval, unmeasured, and conflicting cases. The final prospective sample is
conditional on registered support thresholds at enrollment close. No human adjudication, clock
value, latency estimate, price study, or accepted cross-venue pair is reported.
This separation is the identification strategy. Population scale, venue finality, and public
contractual sufficiency are distinct layers. No endpoint count, determination timestamp, or final
result can substitute for a reproducible rule–evidence proof.
A Adjudication classifications
The minimum taxonomy is grouped as follows:
•exact or interval first/stable clocks;
•source found with rule ambiguity, and rule found with source unavailable;
•multiple plausible releases, conflicting primary evidence, and unmeasured cases.
Reconciliation creates a new version and never deletes initial reviewer judgments.
Data and Code Availability
The registered MVE population and hierarchy are available as theKalshi Multivariate Event
Market Materialization Dataset (KMVE), Mendeley Data, V1, doi: 10.17632/fn65786cg6.1. The
manuscript describes the prospective sampling and adjudication design. Raw active production-
enrollment capture is not distributed, and no empirical production-enrollment result dataset
yet exists. No sampled ticker identities, contractual-decidability clocks, adjudication outcomes,
price results, or accepted cross-venue pairs are released with this preprint.
11

Generative AI Disclosure
OpenAI ChatGPT and Codex were used for editorial and technical assistance during manuscript
preparation. The author made all substantive research decisions, reviewed the final manuscript,
and assumes full responsibility for its contents.
Funding
This research received no external funding.
Competing Interests
The author is affiliated with the Research Department of Devnull FZCO and leads the Fore-
sightFlow research programme. No external sponsor influenced the research design, analysis,
interpretation, or decision to publish. The article does not evaluate a commercial product or
make investment recommendations.
References
Adegbenro, A. (2026). “What Prediction Markets Can See: Market Formation, Settlement
Legibility, and the Geography of Tradable Uncertainty in Africa and Latin America”. In:
arXiv:2606.17503 [econ.GN].url:https://arxiv.org/abs/2606.17503.
Cohen, J. (1960). “A Coefficient of Agreement for Nominal Scales”. In:Educational and Psycho-
logical Measurement20.1, pp. 37–46.doi:10.1177/001316446002000104.
Dai, D., R. Jia, and S. Yu (2026). “Settlement Manipulation in Prediction Markets”. In: arXiv:
2606.31675 [q-fin.TR].url:https://arxiv.org/abs/2606.31675.
Gebele, J. and F. Matthes (2026). “Semantic Non-Fungibility and Violations of the Law of One
Price in Prediction Markets”. In: arXiv:2601.01706 [cs.CE].url: https://arxiv.org/
abs/2601.01706.
Nechepurenko, M. (2026a).Kalshi Multivariate Event Market Materialization Dataset (KMVE).
Version V1. Mendeley Data.doi: 10.17632/fn65786cg6.1 .url: https://doi.org/10.
17632/fn65786cg6.1.
Nechepurenko, M. (Sept. 2, 2026b).On-Demand Combinatorial Event Markets on Kalshi:
Instantiation, Concentration, and Effective Market Breadth. SSRN 7421260.doi:10.2139/
ssrn.7421260.url:https://ssrn.com/abstract=7421260.
12

Nechepurenko, M. (Sept. 1, 2026c).Outcome Determination and Settlement Finality on Kalshi:
Public State Paths, Prospective Measurement, and Empirical Identification. SSRN 7421258.
doi:10.2139/ssrn.7421258.url:https://ssrn.com/abstract=7421258.
13
