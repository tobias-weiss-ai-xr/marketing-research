---
title: 'Fill-Side Behavioral Concentration on Polymarket: Identification Limits under Record-Level Attribution'
url: https://arxiv.org/abs/2605.11640
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Maksym Nechepurenko
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.11640
pages: 9
chars: 23993
fetched_at: '2026-11-08T13:08:51+00:00'
kb_version: 1
---

# Fill-Side Behavioral Concentration on Polymarket: Identification Limits under Record-Level Attribution

Fill-Side Behavioral Concentration on Polymarket:
Identification Limits under Record-Level Attribution
Maksym Nechepurenko ∗
July 29, 2026
Abstract
This paper studies behavioral concentration in Polymarket’s public executed-fill record
and formalizes what that record can and cannot identify. A pre-publication reconciliation
corrects the empirical scope: the archived extraction covers the legacy CTF Exchange over
Polygon blocks 86,008,447–86,107,178, approximately 25 April 2026 17:09 UTC through 28
April 2026 00:00 UTC, rather than the full 21–27 April week stated previously. It contains
13,356,931 OrderFilled records, 77,204 addresses with at least five attributed records,
and 43,116 token identifiers; negative-risk markets are absent.
The archived feature construction credits both maker and taker addresses on each
OrderFilled record. This convention is not invariant to match fragmentation: one
aggressive order can generate several maker records plus a taker summary, inflating record
intensity and altering mean record notional. Moreover, mint and burn executions do
not admit a conventional one-buyer/one-seller directional interpretation. Consequently,
the reported one-cluster density-based result is retained only as a null under the original
record-level representation, not as evidence that the participant population is intrinsically
unimodal. The concentration table is likewise interpreted as attribution-weighted arithmetic
under that convention.
Two methodological results remain independent of these measurement corrections. First,
public fills do not identify the address-level quote lifecycle required to infer continuous
market making, spoofing, or strategic withdrawal. Second, a one-cluster result rejects
density separation in an observed feature space, not latent economic heterogeneity. A
clustering-independentthresholdsystemstillrecordssubstantialconcentration: thearchived
high-scale/high-intensity subtotal contains 12.6% of addresses and 81.4% of attributed
notional. A match-normalized, mint-aware, multi-window replication is required before
treating either the cluster null or exact tier shares as stable venue properties.
∗Founder and Director of Research, ForesightFlow, the Research Department of Devnull FZCO, Dubai,
United Arab Emirates. Email:maksym@devnull.ae.
1
arXiv:2605.11640v2  [q-fin.TR]  30 Jul 2026

Keywords:prediction markets; Polymarket; central limit order book; market microstructure;
behavioral concentration; clustering; on-chain data.
JEL:G14, G23, G24.
1 Introduction
Prediction markets require informed traders, arbitrageurs, liquidity suppliers, and large
directional participants (Glosten and Milgrom, 1985; Wolfers and Zitzewitz, 2004), but public
data do not observe these roles symmetrically. Executed trades are often visible. Unexecuted
intentions are not. On a hybrid central limit order book (CLOB), an on-chain fill log may
reveal addresses associated with an execution while leaving order submission, modification,
queue position, and cancellation off-chain.
This asymmetry creates two distinct empirical hazards. The first is conceptual: repeated
maker-side fills may be consistent with professional liquidity supply, but they do not establish
continuous two-sided quoting, posted-spread choice, inventory control, or quote withdrawal.
The second is representational: anOrderFilled record is not necessarily one economic decision,
one conventional transfer, or one independently directed trade leg. Record-level attribution
can therefore alter the geometry on which unsupervised clustering operates.
The present revision corrects the empirical window and makes the attribution convention
load-bearing rather than incidental. It does not rerun the original computation. Its purpose
is to identify which conclusions remain valid under the archived run and which require a
match-normalized and mint-aware replication.
The main conclusions are:
1. Public settlement logs support exact arithmetic on the archived execution records but not
address-level quote-lifecycle inference.
2. The archived density-based null is conditional on a 2.285-day, legacy-CTF-only, record-
attributed feature space.
3. Threshold cohorts show strong attribution-weighted concentration, but the exact shares are
not stable venue parameters without sensitivity to match aggregation and execution type.
4. Fill-side evidence can support surveillance and risk calibration only when its unit of
observation and direction semantics are stated explicitly.
The paper is the fourth study in a series on event-linked perpetual futures (Nechepurenko,
2026a,b,c). Papers 1–3 use the present evidence only within its observability boundary: as a
source of executed-flow scale and concentration, not as direct proof of market-making roles or
manipulation intent.
2 Corrected empirical scope
2.1 Block range and time interval
The authoritative extraction range is Polygon blocks 86,008,447–86,107,178 on the legacy
Polymarket CTF Exchange. A pre-publication reconciliation of this range against an inde-
pendent reconstruction reproduced all three headline quantities to within 0.1% and showed
that the first in-range fill occurs at approximately 25 April 2026 17:08:58 UTC, while the
upper boundary lies at the transition into 28 April UTC. The archived run therefore covers
approximately 2.285 days, not the full seven-day interval previously stated.
The corrected scope is:
The intended design targeted a dense complete week because local compute, storage, and
processing capacity were limited. The effective archived extraction that generated the reported
outputs is nevertheless the block range above, consistent with a truncated or resumed backfill
rather than the intended calendar window. The present revision therefore treats the block
2

Table 1:Corrected archived sample scope.
Field Archived run
Exchange Legacy CTF Exchange only
Polygon blocks 86,008,447–86,107,178
Approximate UTC interval 25 Apr 2026 17:09–28 Apr 2026 00:00
Duration 2.285 days
OrderFilledrecords 13,356,931
Token identifiers 43,116
Addresses with at least five attributed records 77,204
Negative-risk markets absent from the extraction
range as authoritative. Any statement previously framed as a seven-day or one-week population
result must be read as an archived partial-window result.
2.2 Venue-family exclusion
The extraction includes only the legacy CTF Exchange contract and excludes the contem-
poraneous negative-risk exchange. The 43,116 token identifiers therefore represent binary
CTF activity under this contract filter, not the full Polymarket market family. Multi-outcome
and negative-risk markets—including many candidate, nominee, and mutually exclusive event
structures—are outside the sample by construction.
This exclusion is separate from short-window selection. Extending the same block range
without adding the negative-risk contract would still omit that market family.
2.3 Versioned extraction beyond the sample
A full-history replication must use a versioned contract and event-signature registry. Polymar-
ket’s official documentation records a CLOB V2 cutover on 28 April 2026 with new CTF and
negative-risk exchange contracts (Polymarket, 2026). A query fixed to the legacy contract or
legacy topic can silently return no post-cutover activity. The present paper does not combine
V1, V2, negative-risk, or later combinatorial exchange data.
3 The unit of observation
3.1 Record-level two-sided attribution
The archived pipeline counts eachOrderFilled record once and credits both the maker and
taker address appearing on that record. Define asource record attributionas one address–record
incidence produced by this rule.
This is a reproducible convention, but it is not a count of independent trading decisions. In a
fragmented match, one aggressive order can interact with several resting orders. The aggressive
address can then appear repeatedly across maker records and again in a taker-summary record.
Proposition 1(Record attribution is not match invariant).Consider one aggressive decision
that executes total notionalV against N resting orders. Under a record-level convention that
credits both addresses on every maker record and also credits the taker summary, the aggressor’s
attributed-record count depends onN, even though the number of aggressive decisions and total
economic notional remain fixed. Consequently, record intensity and mean attributed-record
notional are not invariant to order-book fragmentation.
3

Proof. Holding the aggressive order and total notional fixed, increasing the number of resting
counterparties increases the number of emitted maker records. Under two-sided attribution,
the same aggressor is credited on each such record and on the summary record. The attributed
count therefore changes withN. Any feature that divides total or attributed notional by that
count also changes, although the underlying aggressive decision is unchanged.
The proposition identifies a directional measurement distortion, not generic isotropic noise.
Record intensity rises with fragmentation while mean notional per attributed record falls. A
density algorithm can therefore see a connected cloud created partly by venue mechanics.
3.2 Mints, burns, and direction semantics
An execution record can represent a conventional transfer, a mint of complementary claims, or
a burn/merge. In a mint, both economic participants acquire complementary outcome claims;
the event does not have the same directional meaning as one buyer acquiring an existing claim
from one seller. In a burn, complementary claims are extinguished against collateral.
The archived feature construction did not separate all three execution semantics before
forming the directional feature. Accordingly, that feature is retained only as arecord-side
imbalance proxy. It cannot be interpreted as a validated net-buying or net-selling measure
across the whole sample.
4 Observed and unobserved evidence
4.1 Fill-side and quote-lifecycle observability
Definition 1(Fill-side observability).An address-level quantity is fill-side observable if it is a
deterministic function of the public execution records and the stated attribution convention.
Definition 2(Quote-lifecycle observability).An address-level quantity is quote-lifecycle
observable if the data identify order submission, modification, queue state, cancellation, and
execution status for that address’s orders.
Table 2:Evidence hierarchy after the scope correction.
Layer Observable examples Unsupported claims without
additional data
Execution records record count, attributed notional,
market breadth, intraday activity,
maker/taker appearance
independent decision count,
conventional direction for all
mints/burns, complete inventory
policy
Market-level
books
best bid/ask, depth snapshots,
spread changes, aggregate
withdrawal
identity of withdrawing supplier,
address-level coordination
Quote lifecycle placement, modification,
cancellation, non-fill behavior
unavailable from the public
on-chain fill ledger
External and
oracle evidence
event outcome, proposal/dispute
records, public-information timing
beneficial ownership, duty, intent
Proposition 2(Non-identification of quote behavior from fills).LetFa denote the executed-fill
history attributed to addressa. In the absence of address-attributed placement and cancellation
records, there exist distinct quote processesQa and Q′ a that generate the sameFa but differ
4

in quote intensity, lifetime, two-sidedness, and cancellation behavior. Therefore those quote-
lifecycle properties are not identified byFa.
Proof. Construct Qa as a process containing only orders that eventually execute, andQ′ a as
the same executed orders plus any number of additional unfilled or cancelled orders. Both
induce the same fill history, while quote intensity and cancellation statistics differ arbitrarily.
The map from quote processes to fill histories is many-to-one.
The proposition rules out address-level spoofing detection from fills alone and prevents
repeated maker-side appearance from being treated as direct identification of a market maker.
5 Archived behavioral representation
For addressa, the archived six-dimensional vector is
f rec(a) = (f rec 1 ,f rec 2 ,f rec 3 ,f 4,f 5,f 6),
where
f rec 1 (a) = log
(
1 +nrec a
ha
)
record intensity,(1)
f rec 2 (a) = log(1 + ¯N rec a )mean attributed-record notional,(2)
f rec 3 (a) = V rec a,+ −V rec a,− V rec a,+ +V rec a,− record-side imbalance proxy,(3)
f4(a) =
∑
m
s2 a,m market concentration,(4)
f5(a) =−
23∑
r=0
pa,r logp a,r intraday entropy,(5)
f6(a) = log(1 +M a)market breadth.(6)
Here nrec a counts address–record attributions, not independent orders or matches. The first
two coordinates share the fragmentation dependence described above. The third coordinate is
not uniformly directional across mint, burn, and transfer semantics.
Criterion 1(Role-label discipline).A label is admissible as a primary empirical label only if
its defining properties are observed in the active data layer. Otherwise it must be presented as
a transparent threshold cohort, behavioral proxy, or hypothesis.
Accordingly, the paper does not identify market makers, passive liquidity providers, spoofers,
or institutional firms from the archived feature vector.
6 Clustering result and its corrected interpretation
The archived run applied density-based spatial clustering of applications with noise (DBSCAN)
(Ester et al., 1996) to robustly scaled versions offrec(a). Across fifteen registered configurations,
every run returned one dense cluster and zero noise. An exploratoryk-means partition with
k= 5had silhouette score 0.227 (Rousseeuw, 1987).
These are exact statements about the archived transformation. They are not yet robust
statements about the participant population because:
1. the interval is 2.285 days rather than seven days;
2. the sample excludes negative-risk markets;
3. record count and mean record notional depend on match fragmentation;
5

4. the direction proxy mixes transfer, mint, and burn semantics.
Proposition 3(One-cluster output does not imply one economic type).Suppose observed
features satisfyf(a) =g(za,u a), whereza is a latent economic role andua contains scale, event
mix, attribution convention, and measurement effects. A connected support forf(a)can arise
even whenza takes multiple values. Therefore a one-cluster result rejects density separation in
the specified observed feature space, not latent economic heterogeneity.
The proposition remains valid independently of whether a future match-normalized rerun
produces one or several clusters. The archived one-cluster result should now be read as a
benchmark configuration that future sensitivity analysis must reproduce before changing one
design axis at a time.
7 Threshold cohorts and concentration
The original threshold system partitions addresses by observed scale, attributed-record intensity,
breadth, and attributed notional. The numerical cohorts are retained as archived arithmetic
under the original convention.
Table 3:Archived threshold cohorts under record-level two-sided attribution. Whale status is an
overlay.
Cohort Addresses Population share Attributed-notional share
Whale overlay 68 0.09% 28.0%
High-frequency operator 2,952 3.82% 23.5%
Power trader 6,738 8.73% 29.9%
Active lower-scale 2,062 2.67% 10.6%
High-breadth operator 2,025 2.62% 1.1%
Episodic low-notional 63,358 82.07% 6.8%
High-scale/high-intensity
subtotal
9,758 12.64% 81.4%
Define the archived concentration multiplier
χrec k = attributed-notional sharek population sharek .
For the high-scale/high-intensity subtotal,χrec ≈ 6.44; for the episodic low-notional cohort,
χrec ≈0.083. The ratio of these average attribution intensities is approximately 77.
This is not a claim about the share of unique economic decisions, entity-level activity,
or venue-wide notional. It is a concentration result under the archived record-attribution
convention. Match normalization can change cohort membership because it directly changes
intensity and average record-notional features.
8 Microstructure signatures that remain usable
8.1 Breadth, timing, and concentration
Market breadth, active-hour distribution, and market concentration remain deterministic
properties of the archived address–record table, conditional on the contract and window filters.
Their economic interpretation remains limited by address splitting and entity aggregation.
6

8.2 Adverse-selection proxies
For a record with validated execution direction, a signed markout can be written
Aj =s j(pj+∆ −p j).
Such a measure is valid only whensj has a well-defined economic direction. Mint and burn
records require separate treatment rather than forced classification under a transfer convention.
8.3 Price impact
A reduced-form Kyle-type coefficient (Kyle, 1985) may be estimated from
∆pm,t =α m +λ mqm,t +ε m,t.
In thin bounded markets, raw estimates can be unstable. Winsorized values can be descriptive
but should not be treated as structural parameters. Signed flow must also inherit the execution-
type restrictions above.
8.4 Surveillance candidates
Large gross attributed volume combined with low net attributed position can generate candidate
flags. It does not establish self-trading or manipulation because intermediation, hedging, cross-
market arbitrage, fragmented matching, and multiple addresses can generate similar records.
9 Required replication design
A stronger replication should treat the archived configuration as rung zero and change one
dimension at a time.
9.1 Window axis
Use:
1. the exact archived block range;
2. the full 21–27 April UTC week;
3. one month;
4. one quarter;
5. full contract history;
6. rolling and non-overlapping windows within each longer horizon.
Rolling and non-overlapping windows are needed because a single nested history confounds
participant persistence with venue and infrastructure changes.
9.2 Attribution and direction axis
At minimum compare:
1. the archived record-level two-sided attribution;
2. match-normalized counts and mean notional;
3. the feature vector with the direction proxy removed;
4. a mint/burn-aware direction specification;
5. a transfer-only direction specification.
For each cell report cluster count, noise share, silhouette diagnostics, tier stability, transition
matrices across windows, concentration, and address-level persistence. If the one-cluster null
survives match normalization, execution-type separation, and longer windows, it becomes
materially stronger. If clusters emerge, the original null remains a valid statement only about
the archived representation.
7

10 Implications for leveraged event markets
The corrected evidence constrains, rather than directly calibrates, leveraged-event design.
First, concentrated address-level activity means a homogeneous synthetic trader population
is a weak default. However, concentration parameters should be recalculated on match-
normalized data before use in a risk engine.
Second, public books are not committed liquidation capacity, and fills do not reveal the
cancellation process that determines whether depth survives stress.
Third, halt timing cannot be calibrated from address-level quote withdrawal using public
fill data. At most, match-normalized fill-density decay can supply a weaker execution proxy.
Fourth, manipulation surveillance must be channel-specific. Fill anomalies can motivate
investigation; quote-side allegations require quote-lifecycle evidence; oracle conduct requires
resolution logs; outcome manipulation requires external-event evidence.
11 Evidence discipline
Criterion 2(Evidence-grade rule).Every empirical statement should be assigned to one of
four grades:
1. direct identity or arithmetic under a stated source and attribution convention;
2. deterministic feature or cohort derived under that convention;
3. descriptive statistical association;
4. role, intent, causal, or population-general interpretation requiring additional evidence.
Only grades 1–3 are claimed as findings in this paper, and grade 2 must name the measurement
convention on which it depends.
This rule and Proposition 2 are the durable contributions of the paper. They remain valid
whether later replication preserves or rejects the archived clustering null.
12 Limitations
Partial window.The extraction covers approximately 2.285 days, not one week. Persistent
archetypes cannot be inferred from this horizon.
Legacy CTF only.Negative-risk and multi-outcome market families are absent.
Record attribution.Both maker and taker are credited perOrderFilled record; intensity
and mean record notional are not invariant to match fragmentation.
Direction semantics.The archived direction proxy does not fully distinguish conventional
transfers, mints, and burns.
Address pseudonymity.Addresses are execution entities, not necessarily independent
traders or firms.
No address-level quote lifecycle.Posted spread, quote lifetime, cancellations, quote
stuffing, and spoofing are not identified.
No causal identification.Concentration and microstructure associations do not establish
market-quality or welfare effects.
13 Conclusion
The corrected archival result is narrower than a population taxonomy of Polymarket partici-
pants. The study observes a dense 2.285-day slice of legacy-CTF execution records under a
two-sided record-attribution convention. It documents strong attribution-weighted concentra-
tion and a one-cluster output under that representation. The feature space is affected by match
fragmentation, execution-type semantics, contract-family exclusion, and the short horizon.
8

What survives these corrections is methodologically useful. Public fills do not reveal the
quote lifecycle. A one-cluster output does not imply one economic type. Threshold cohorts
are transparent measurement rules, not natural participant classes. Empirical claims must
name both the observed data layer and the transformation that creates the feature space.
A match-normalized, mint-aware, multi-window rerun is therefore not a cosmetic robustness
check; it is the required test of whether the archived null reflects the population or the
measurement design.
Data and code statement
This revision performs no new empirical run. It corrects the time interval, contract-family
scope, unit-of-observation description, feature interpretation, and claim class of the archived
results. The original numerical outputs are retained only as results under the legacy-CTF,
record-level two-sided attribution convention. A future public release should provide exact
block and contract registries, match-construction rules, execution-type classification, aggregate
cohort outputs, processing manifests, and a reconstruction procedure without publishing
ranked address-level profiles.
References
Ester, Martin, Hans-Peter Kriegel, Jorg Sander, and Xiaowei Xu (1996). “A Density-Based
Algorithm for Discovering Clusters in Large Spatial Databases with Noise”. In:Proceedings
of KDD, pp. 226–231.
Glosten, Lawrence and Paul Milgrom (1985). “Bid, Ask and Transaction Prices in a Specialist
Market with Heterogeneously Informed Traders”. In:Journal of Financial Economics14.1,
pp. 71–100.
Kyle, Albert (1985). “Continuous Auctions and Insider Trading”. In:Econometrica53.6,
pp. 1315–1335.
Nechepurenko, Maksym (2026a).A Taxonomy of Event-Linked Perpetual Futures. arXiv:
2605.10428.
— (2026b).Manipulation, Informed Trading, and Regulation in Leveraged Event-Linked
Markets. arXiv:2605.10486.
— (2026c).Resolution-Aware Perpetual Futures on Binary Prediction Markets. arXiv:2605.
10400.
Polymarket (2026).Migrating to CLOB V2. Official developer documentation.url:https:
//docs.polymarket.com/v2-migration(visited on 07/29/2026).
Rousseeuw, Peter (1987). “Silhouettes: A Graphical Aid to the Interpretation and Validation
of Cluster Analysis”. In:Journal of Computational and Applied Mathematics20, pp. 53–65.
Wolfers, Justin and Eric Zitzewitz (2004). “Prediction Markets”. In:Journal of Economic
Perspectives18.2, pp. 107–126.
9
