---
title: 'Declared but Unaccountable: Measuring the Seller-Identity Gap in Advertising Supply-Chain Transparency'
url: https://arxiv.org/abs/2610.14661
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Tommaso Grotto
- Alessandro Cantelli-Forti
- Alessio Merlo
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.14661
pages: 21
chars: 82562
fetched_at: '2026-11-08T13:22:51+00:00'
kb_version: 1
---

# Declared but Unaccountable: Measuring the Seller-Identity Gap in Advertising Supply-Chain Transparency

DECLARED BUTUNACCOUNTABLE:
MEASURING THESELLER-IDENTITYGAP
INADVERTISINGSUPPLY-CHAINTRANSPARENCY
Tommaso Grotto
Kopjra Srl, Bologna, Italy
tommaso.grotto@kopjra.com
Alessandro Cantelli-Forti
CNIT, RaSS Laboratory
Pisa, Italy
alessandro.cantelli.forti@cnit.it
Alessio Merlo
CASD, School for Advanced Defense Studies
Rome, Italy
alessio.merlo@unicasd.it
ABSTRACT
Public advertising transparency relies on a minimum accountability condition: an account authorized
by a publisher in ads.txt or app-ads.txt should appear in the applicable sellers.json registry.
When an available registry omits the declared seller ID, the authorization remains visible and machine-
readable, but its public verification path breaks. We call this failure theseller-identity gap.
We measure the gap using 233.4 million normalized advertising-transparency records and an absent-
only, coverage-aware evidence rule. An eligible declaration enters the numerator only when the
applicable registry is available and does not contain its normalized seller-ID key; unavailable,
malformed, confidential, and otherwise non-evaluable states remain separate. The resulting row-level
floor is 24.25% in a high-popularity, low-removal reference population and 30.71% among publishers
associated with at least 100 copyright-removal requests, a 6.45 percentage-point increase. The
gap then remains near one third at stricter cumulative thresholds. Standardizing the populations to
common weights over 1,469 shared ad systems reduces the primary contrast to 4.65 points: about
72% remains within systems, while 28% forms a composition-associated residual that also includes
restriction to shared system support.
We connect these population estimates to recurring seller-account coordinates, byte-identical dec-
laration configurations, and provenance-bearing case packets. We frame this declaration-centered
investigative use of public advertising records asAd Transparency Intelligence: it reconstructs de-
clared supply-chain relationships, identifies where public verification stops, and prioritizes evidence
for corroboration without equating correlation with attribution. The result is a reproducible path from
population-scale measurement to reviewable declaration evidence. Advertising transparency supports
accountability and investigation only when visible authorizations remain publicly verifiable.
Keywordsadvertising transparency·ads.txt·sellers.json·supply-chain accountability·Web measurement
1 Introduction
Online advertising finances much of the open Web, including sites associated with piracy, misinformation, illegal
streaming, scams, and other forms of online abuse [ 1–7]. For an advertiser, media buyer, regulator, or investigator,
following the money begins with a concrete question:which accounts and intermediaries are positioned to monetize
this publisher?A single impression may pass through publishers, supply-side platforms, exchanges, and resellers
before reaching a buyer. Reconstructing declared relationships is therefore a prerequisite to accountability, even when
execution and payment remain unobservable [8–10].
arXiv:2610.14661v2  [cs.CY]  14 Oct 2026

Declared but Unaccountable
Publisher
ads.txt / app-ads.txt
Ad system
sellers.json
Public seller record
seller ID present
declares seller ID registry lists seller ID
24.3% reference→30.7%≥100removals
Figure 1: The public seller-account chain. A publisher declares an account in ads.txt or app-ads.txt; the ad system
is expected to list the same seller ID in sellers.json. We measure failure only when the applicable registry is
available.
Publishers list authorized seller accounts in ads.txt, or app-ads.txt for applications; ad systems publish reciprocal
account records in sellers.json [11–13]. Together, these files create a public seller-account chain (Figure 1). A
declaration may remain visible and syntactically valid even when its normalized seller-ID key is absent from the
applicable registry. We call this dangling authorization reference theseller-identity gap. It breaks the minimum public
account-presence property but does not prove fraud, infringement, contractual invalidity, or the absence of a private
account.
Consider, for example, a publisher that declares the illustrative seller ID 74291 at an ad system. The declaration is
visible, syntactically valid, and consumable by automated tools. If the ad system’s available sellers.json contains
no record for 74291, however, the public chain stops before the account that the declaration is supposed to identify.
Buyers, auditors, exchanges, brand-safety systems, and investigators rely on these artifacts as public authorization
metadata. A missing record does not prove fraud, but it removes the mechanism’s minimum guarantee: an outside
verifier can no longer connect the declared authorization to a publicly recorded seller account.
Cross-file reconciliation and missing seller IDs are not new. Academic, standards, and industry work already measures
adoption, missing identifiers, relationship inconsistencies, pooling, and ecosystem-wide matching [14–22]. We instead
ask how much of the complete declared authorization surface fails this public account-presence check under an explicit
evidence rule, how the resulting population contrast is structured, and how the underlying evidence can support targeted
review.
We analyze 233,416,998 normalized advertising-transparency records. All eligible publisher declaration rows remain in
the denominator; registry records supply account-presence evidence rather than additional denominator rows. Only an
absent normalized seller-ID key in an applicable available registry enters the numerator. Unavailable, malformed, and
otherwise non-evaluable registries remain separate; evidence-backed aliases retain their provenance, and confidential
records count as account-present without revealing public identity. We compare a high-popularity, low-removal
reference with cumulative populations associated with at least 100, 1,000, and 10,000 Google copyright-removal
requests [23, 24]. These thresholds indicate enforcement attention, not culpability.
The result is both substantial and easy to state: the gap affects almost one in four declaration paths in the reference
population and almost one in three at the primary enforcement-linked threshold. The coverage-robust floor rises from
24.25% to 30.71% (a 6.45-percentage-point increase), then plateaus near one third. Standardization to common weights
over 1,469 shared ad systems reduces the contrast to 4.65 points. Approximately 72% of the observed difference
therefore remains within systems, while the remaining 28% is composition-associated and includes the small effect of
restricting standardization to shared systems. The decomposition localizes the contrast without identifying its cause.
Beyond measurement, the same public records provide an investigative surface. We useAd Transparency Intelligence
to describe this declaration-centered, ecosystem-level use of advertising-transparency artifacts: reconstructing declared
supply-chain relationships, identifying where public verification fails, and prioritizing evidence-bearing review. A
resolved coordinate can identify a seller account and the intermediary at which further verification can proceed; an
absent account interrupts that public path. This use supports correlation and review prioritization, but does not by itself
establish ownership, intent, contractual status, or economic benefit.
Accordingly, we ask:
RQ1: How much of the declared advertising surface fails the public seller-account check?
We estimate the coverage-robust row-level floor and compare the reference with cumulative enforcement-linked
populations.
2

Declared but Unaccountable
RQ2: How is the enforcement-linked difference structured?
We test observed popularity support and separate the contrast that remains under common ad-system weights from the
residual associated with ad-system composition.
This work makes three contributions:
C1 We formalize public seller-account presence as a distributed referential-integrity property and operationalize an
absent-only, provenance-preserving estimand.
C2 We measure a substantial reference floor and a 6.45-point enforcement-linked step, then localize that contrast
through a common-standard decomposition without causal attribution.
C3 We translate population-scale measurement into declaration-native investigative surfaces based on recurring
seller-account coordinates, byte-identical declaration configurations, and provenance-bearing case packets.
Identifier reuse, declaration clustering, and advertising intelligence are established practices [25–28]. Our contribution
is to make their declaration-centered use more controlled and verifiable by preserving the evidence path from population
estimates to the public records that produced them. The remainder defines the property and evidence model; positions
the work against its nearest neighbors; reports the data, estimand, RQ1, and RQ2; develops Ad Transparency Intelligence
through reviewable declaration-native evidence; and closes with implications, limitations, conclusions, ethics, and open
science.
2 Public Advertising Accountability
This section defines the public mechanism, the security property it is expected to provide, and the evidence available
to an outside verifier. The measured property is verifiable seller-account presence: whether a publisher’s declared
authorization reaches the public account record promised by the applicable registry. Legal identity, private authorization,
and auction execution require additional evidence.
2.1 The Public Authorization-to-Account Chain
An ads.txt row contains an ad-system domain, seller identifier, and relationship type, typically DIRECT or RESELLER;
app-ads.txt is analogous for applications. The reciprocal sellers.json maps seller IDs to account records or
marks identity information confidential [11–13]. The OpenRTB SupplyChain object describes parties in a bid-request
path, but it is a distinct execution-layer object [29–31]. Reselling is legitimate [32].
Seller identifiers are local to an ad system. The same identifier at two systems does not denote the same account.
The namespace-safe coordinate is (canonical ad system,seller ID) . At this coordinate, the publisher file expresses
authorization, and the registry establishes whether a public account record exists. A resolved coordinate gives an outside
verifier both a seller account and the public intermediary at which corroboration can continue; an absent coordinate
interrupts that path. We separate registry availability, account presence, identity disclosure, observable execution, and
economic outcome. The headline estimand ends at account presence. A confidential record is account-present without
providing full public identity disclosure.
The term advertising transparency also denotes platform-side explanations and public ad repositories [33–37]. Here it
refers only to supply-side declaration and registry files.
2.2 The Seller-Identity Gap
For ad systema, seller identifiers, and applicable registryR a, the minimum invariant is
declared(a, s)∧available(Ra) =⇒present(s, Ra).(1)
The seller-identity gap occurs when (a, s)is declared, Ra is available, and s is absent. If the registry cannot be retrieved
or parsed, public evidence is insufficient, and the declaration is not counted as absent. Evidence-backed aliases may
locate a registry but cannot create a missing ID match. Fuzzy matching, company-name similarity, and corporate
affiliation likewise cannot recover a missing coordinate.
Account resolution, identity disclosure, and entity accountability are successively stronger. Names and domains may
be missing, confidential, inconsistent, or associated with a parent company. A failed join can reflect a stale or copied
file, error, migration, registry omission, unpublished private account, or fabrication. Public artifacts do not reveal
which explanation applies. Account presence is necessary but insufficient for complete seller accountability. The gap
therefore measures a verifier-visible break in the public chain. It identifies where a declared relationship can no longer
be followed through the mechanism’s own records, without determining why the break occurred or who is responsible.
3

Declared but Unaccountable
2.3 Threat and Evidence Model
We consider an outside verifier, such as a buyer, publisher, ad system, standards body, researcher, regulator, or
investigator. The verifier observes public declarations, registries, endpoints, redirects, timestamps, hashes, retrieval
states, and parser outputs. It does not observe private contracts, onboarding or KYC records, internal account status,
auction logs, settlement, or payment. Its goal is to determine whether a public authorization terminates at the account
record promised by the public mechanism.
The design is fail-closed: missing evidence remains missing evidence. A registry that cannot be evaluated does
not become evidence of an absent account, and a resolved account does not by itself establish a legal entity, active
transaction, or economic outcome. These boundaries preserve the value of the public check without extending its
inference beyond the evidence available to the verifier. Industry analyses similarly show that public programmatic
records provide only part of end-to-end supply-chain accountability [8, 9, 38].
2.4 Enforcement-Linked Populations and Scope
Google copyright-removal requests are used only for population construction [24]. Removal volume reflects enforcement
attention and may depend on scale, visibility, rights-holder effort, reporting intensity, and duplicated URLs. It is neither
ground truth for infringement nor a measure of intermediary intent. The reference is high-popularity and low-removal
rather than verified benign. The enforcement-linked populations are cumulative observational strata, not causal
treatments. Results are conditional on usable transparency declarations and describe declaration rows, not all candidate
hosts, all removal targets, or publisher prevalence.
3 Related Work
We position this work by the quantity measured, the evidence retained, and the inference supported. The literature
established cross-file reconciliation, missing seller identifiers, identifier reuse, and declared-plus-observed advertising
analysis. Building on those foundations, we contribute a coverage-aware row-level floor for public seller-account non-
resolution, compare it across enforcement-stratified populations, decompose the observed contrast into within-system
and composition components, and preserve a path from aggregate estimates to reviewable declaration evidence.
3.1 Transparency Standards and Cross-File Consistency
The IAB transparency stack defines complementary declaration, registry, and execution-path layers [11–13, 29–31, 39].
Bashir et al. measured adoption, authorization compliance, and evolution of ads.txt [14]. CNIL/LINC recursively
mapped seller and intermediary relationships, while IAB Europe reported line-level cross-file matching under partial
ad-system coverage [17, 18]. These studies establish adoption and incompleteness but do not provide our absent-only
row-level population contrast.
The reported quantities also differ materially. IAB Europe found that approximately 79% of valid ads.txt lines
matched a sellers.json record, while registry collection succeeded for only about 61% of unique ad-system
domains [18]. DeepSee reported matches for roughly 60% of ads.txt entries across more than one million publishers
and for about 40% of unique reseller entries [19, 20]. Vekaria et al. reported the relevant missing-ID category for 65%
of 251 rank-matched control sites and 83% of 251 misinformation sites [15]. Sheaib et al. reported 169 missing seller
IDs and 418 domain mismatches among 587 unique DIRECT entries from 35 illegal-streaming sites [3]. A public audit
based on a May 2026 snapshot covered 86,357 publishers and 33.39 million publisher–system–seller triples; within its
6.43 million DIRECT claims, 30.51% failed to reconcile [22]. Its aggregate also includes broken registries, confidential
records, and registry-migration states that our resolver separates. These figures are not numerically interchangeable
with our floor because they differ in unit, relationship scope, population, registry-availability treatment, alias handling,
state aggregation, and denominator.
Vekaria et al. are the nearest academic comparison [15]. They classify seller IDs declared by publishers but absent
from corresponding registries and compare misinformation and control sites. Their endpoint is primarily site-level and
embedded in a broader dark-pooling study. One absent row and thousands can therefore have the same site-level outcome.
Sheaib et al. cross-check DIRECT declarations from illegal streaming services and report missing IDs and domain
mismatches [3]. Their population is similarly policy relevant, but their scope and denominator differ. Papadogiannakis
et al. audit related conformance failures at graph scale, including relationship mismatches, confidentiality, copied
registries, and hidden intermediation [16]. They do not report our availability-conditioned all-row floor, enforcement
gradient, clustered uncertainty, or common-standard decomposition.
4

Declared but Unaccountable
The estimand distinction is operational. A site-level indicator asks whether a publisher exposes at least one problematic
coordinate. A conditional match rate excludes unavailable evidence from its denominator. Analyses restricted to
DIRECT declarations exclude reseller relationships. Our floor instead measures absent seller accounts over the complete
declared authorization surface while preserving unavailable, malformed, aliased, confidential, and noncanonical states.
3.2 Abuse-Linked Advertising, Pooling, and Remediation
Advertising-funded piracy, misinformation, and illegal streaming have been studied through economic, ecosystem, and
follow-the-money analyses [1, 2, 4–7, 40–42]. Industry studies document opacity, waste, and untraceable spend [8–
10, 32, 38, 43]. Security research separately measures fraudulent exchanges, impression and click fraud, affiliate abuse,
ad injection, and malicious advertising [44–51]. We use this literature to motivate the population comparison, not to
label a publisher, coordinate, declaration, or impression as fraudulent.
Pooling concerns reuse of an account across publishers; account absence concerns whether the declared coordinate
exists in the applicable available registry. A pooled ID can resolve correctly, while a unique ID can be absent. Vekaria
et al. combine declarations with browser-observed delivery while studying dark pooling [15]. Papadogiannakis et al.
analyze shared identifiers, hidden intermediation, placement laundering, and potential revenue paths [ 16, 52]; their
Before & Afterstudy pairs declarations and registries with crawled advertising evidence [ 53]. Declared-plus-observed
measurement is therefore established. Vekaria et al. later evaluate multi-stakeholder notification and remediation [54];
we do not conduct notifications or estimate remediation effectiveness.
3.3 Identifiers and Advertising Intelligence
Advertising and analytics identifiers have long been used to connect sites and infer administration or campaign
structure [25–27]. Related studies examine tracking ecosystems, actor relationships, privacy leakage, and identity
entanglement [55–62]. Our fan-out and byte-identical-file analyses build on this practice and serve only as review
surfaces.
Vines et al. introduced ADINT in a different investigative setting: purchasing targeted advertisements to obtain
information about individuals, including location and use of potentially sensitive applications [28]. We study neither
targeted surveillance nor individual users. Our declaration-centered use of advertising intelligence reconstructs publisher–
intermediary–account relationships from public supply-chain artifacts, identifies where those relationships cease to be
publicly verifiable, and reduces the resulting surface to evidence-bearing review targets. In both settings, advertising
artifacts become an intelligence source; the object, evidence, and supported inference differ.
Infrastructure and registration data can reveal dependencies, but shared hosting, CDNs, certificates, and provider-level
features may connect unrelated sites [ 63–67]. Placement laundering further complicates inference from delivery
endpoints [52, 68]. We therefore keep the present analysis declaration-native: recurring seller coordinates and byte-
identical files preserve exact public relationships, while external technical similarity is not used as an account resolver
or ownership signal.
3.4 Declared and Observed Advertising Evidence
Prior work infers advertising relationships and auction behavior from retargeting, header bidding, auction observations,
and network flows [69–78]. Vekaria et al. and Papadogiannakis et al. further demonstrate the value of combining public
declarations with observed advertising delivery [5, 15, 53]. These studies establish declared-plus-observed measurement
as prior art. They also show that observation introduces a separate sampling and inference problem: visible requests,
bids, and transaction stages expose different evidence, while server-side paths may remain hidden. Signed transaction
chains and accountable exchanges pursue stronger execution-level properties [79–81]. We therefore confine this paper
to the declared public surface and treat systematic comparison with live RTB traffic as subsequent work requiring its
own coverage model and phase-aware identifiers.
3.5 Positioning of This Work
We do not claim priority for cross-file reconciliation, missing-ID detection, identifier reuse, advertising intelligence as a
general investigative idea, or declared-plus-observed measurement. We build on those foundations to contribute an
explicit public account-presence property; an absent-only, coverage-aware row-level estimand with publisher-clustered
uncertainty [82]; an enforcement-linked population comparison; a common-standard decomposition following the
rate-versus-composition logic of Kitagawa [83]; and provenance linking population estimates to recurring coordinates,
shared declaration configurations, and exact reviewable evidence. The novelty lies in this controlled combination of
measurement, comparative localization, and declaration-native traceability.
5

Declared but Unaccountable
Table 1: Populations and public-registry coverage. The removal populations are cumulative.
Population Candidate hosts Hosts with declarations Declaration rows Registry coverage
Tranco low-removal reference 972,214 78,686 40,384,095 96.54%
Google removals≥100485,920 8,998 6,344,799 95.34%
Google removals≥1,000100,836 2,227 2,626,098 95.14%
Google removals≥10,00011,182 374 691,380 95.08%
4 Data and Measurement Design
This section operationalizes the public account-presence property. It keeps acquisition, population, and analytical scales
separate and fixes evidence states, analytical unit, denominator, uncertainty, decomposition, and provenance before
examining outcomes.
4.1 Transparency Corpus
The canonical snapshot, frozen for analysis on September 28, 2026, contains 233,416,998 normalized records:
128,964,813 ads.txt rows, 100,558,277 app-ads.txt rows, and 3,893,908 sellers.json rows. The publisher-
declaration families describe authorization relationships; seller records provide the reciprocal registry context. The
retained observations span March 20–September 21, 2026, with the publisher-declaration families beginning March 26.
The surviving campaign ledger covers April 16–September 21: 3,307 artifact-family runs, 51,222,091 application-level
fetch attempts, and 24,000,178 present-valid artifact observations. These operational totals describe the surviving run
summaries, not a complete census of every historical attempt or the denominator of any analytical result.
The analytical unit is a frozen normalized declaration row, not a fetch attempt. For each declaration, we retain host,
artifact family, source hash, source run, parser status, line position, raw and canonical ad-system domains, seller ID, and
relationship type. Registry rows retain seller ID, declared name and domain, seller type, confidentiality state, source
hash, and parser provenance. Content hashes deduplicate identical bytes and make paper-facing results traceable to
frozen inputs. Repeated observations support provenance and reduce reliance on a one-off exposure, but headline
estimates remain cross-sectional. We do not describe them as longitudinal change.
4.2 Populations and Selection Boundary
The reference begins with Tranco top-1M [23] and excludes hosts with at least 100 removal requests. It can include
hosts with 1–99 requests and hosts for which the source has no evidence. Enforcement-linked populations contain hosts
with at least 100, 1,000, and 10,000 requests and are nested. The analysis is conditional on a host exposing at least one
usable publisher declaration. This occurs for 8.09% of candidate reference hosts, compared with 1.85%, 2.21%, and
3.34% of candidates in the cumulative removal populations. We therefore make no population-wide claim about all
copyright-removal targets. Differing declaration rates are a selection boundary, not an implementation detail.
A separately archived June 21 deep-mapping study contains 37,454 removal-linked hosts, 15.3 million grouped
declaration leads, and 321,097 seller-account clusters. Grouped leads are not raw normalized rows. Its fan-out statistics
provide a dated investigative illustration, not an additional population estimate or an extension of the four RQ1/RQ2
denominators. Exact-content membership and the four illustrative publishers in Section 7 are checked against the
canonical snapshot; their copyright-removal context remains separately dated. We fixed the historical case identities
independently of the population results. None of these surfaces changes the primary labels, denominators, common
weights, or resolution states.
4.3 Coverage-Aware Resolution
For each declaration row r, the resolver preserves the raw ad-system value, canonicalizes the domain, and seeks the
applicable registry. Direct registries and evidence-backed aliases are accepted. Alias rules cover verified redirects,
rebrands, and special registry hosts; each retains its source and raw endpoint. Registry retrieval terminates as available
directly, available through an evidence-backed alias, unavailable, malformed, or not materialized. When an applicable
registry is available, account resolution yields resolved, absent, confidential, or noncanonical.
Eligibility requires nonempty host, ad-system, and account-ID fields; ad-system tokens matching the fixed malformed-
domain pattern are excluded.1 Account presence is tested by exact equality of normalized seller-ID keys within the
1The analysis filter uses the regular expression^[0-9a-f]{12,}(?:[a-z0-9-]+\.)+[a-z]{2,}.
6

Declared but Unaccountable
Table 2: Registry and account states. Alias use is retrieval provenance rather than a mutually exclusive account outcome.
Only an absent account in an applicable available registry enters the primary numerator.
Layer State Effect on primary numerator
Registry available directly or through alias account evaluated
Registry unavailable, malformed, or not materialized no
Account resolved no
Account confidential but present no
Account absent yes
Account noncanonical no
applicable ad-system namespace, including evidence-backed registry aliases. Keys are trimmed and lowercased on both
declaration and registry sides; raw identifiers are retained. This is not fuzzy matching or byte-for-byte equality of raw
strings. Confidential records expose the account while withholding identity and comprise only 0.38–0.69% of rows
across the main populations. Unavailable, malformed, and not-materialized registries do not enter the numerator. This
prevents crawler coverage from becoming apparent publisher opacity.
4.4 Primary Estimand and Uncertainty
Let DP denote eligible declaration rows in population P . Let loaded(r) indicate an obtained applicable registry and
absent(r)that its normalized seller-ID key does not occur:
Gap(P) = |{r∈D P : loaded(r)∧absent(r)}| |DP | .(2)
All eligible declarations remain in the denominator. Unavailability can lower the floor but cannot increase its numerator.
Registry coverage is reported separately. The estimand is row-weighted and describes the declared authorization surface,
not publisher prevalence. Publishers with larger files contribute more rows. We obtain 95% intervals from 1,000
publisher-level bootstrap samples, retaining each sampled host’s complete row set [82].
4.5 Comparative Design and Decomposition
Popularity matching compares enforcement-linked and reference publishers within common Tranco rank buckets and
is a sensitivity analysis, not a causal adjustment. For population P and system a, let gP,a be its floor and wP,a its
row share. The common support consists of 1,469 systems present in all four populations. The weighting rule pools
declaration rows over these systems and all four population memberships, including the nested cohorts, then normalizes
the pooled totals to obtainw ∗ a:
Gap∗(P) = X
a
w∗ agP,a.(3)
For enforcement-linkedEand referenceR,
∆∗ within = X
a
w∗ a(gE,a −g R,a),∆ ∗ comp = ∆obs −∆ ∗ within.(4)
Thus ∆obs = ∆ ∗ within + ∆∗ comp exactly for the chosen standard. The observed contrast uses all eligible systems,
whereas standardization uses shared system support. Consequently, ∆∗ comp is a composition-associated residual that
also includes the effect of this support restriction; it does not isolate reweighting on an identical support. This follows
Kitagawa’s rate-versus-composition logic [83], but is not the unique symmetric decomposition. Both components are
descriptive and standard-dependent. A separately dated August registry check supplies historical retrieval context, not
contemporary validation of September registries. Leave-one-system-out and joint exclusions test influence. These
diagnostics do not redefine the estimand. Calculations use unrounded counts and rates; rounding occurs only in
presentation.
4.6 Failure Discipline, Provenance, and Validation
The resolver is fail-closed. Domain normalization never overwrites raw values; aliases retain evidence; parser failure
terminates in a non-evaluable registry state; duplicate records reduce to one presence fact; and arbitrary fuzzy matching
is excluded. Schema tests cover valid, malformed, confidential, duplicated, noncanonical, redirect, and alias cases.
Aggregate invariants require every declaration to terminate in exactly one account or non-evaluable registry state and
state totals to reconcile with population exports.
7

Declared but Unaccountable
Table 3: Coverage-robust seller-identity gap. Populations are cumulative; confidence intervals resample publisher hosts.
Pop. Rows Gap 95% CI
Ref. 40,384,095 24.25% 23.97–24.51%
≥1006,344,799 30.71% 29.98–31.40%
≥1k 2,626,098 31.55% 29.87–32.97%
≥10k 691,380 33.08% 31.40–34.56%
Reference
(<100)
≥ 100 ≥ 1,000 ≥ 10,000
Google copyright-removal requests (cumulative)
24
27
30
33
36
Seller-identity gap (%)
+6.45 pp
adjacent threshold CIs overlap
Figure 2: Coverage-robust row-level floor. The primary contrast is the 6.45-point increase from the reference to ≥100 ;
stricter-threshold intervals overlap.
The pipeline emits artifact, declaration, registry, resolution, and population objects. Canonical population results can be
traced from aggregate cells to normalized resolution rows, source hashes, line positions, parser versions, and collection
runs. Separately dated sources have their own provenance: the June grouped fan-out export, the August registry-check
log, historical removal inputs, and the surviving collection ledger are not silently treated as canonical resolution rows.
Appendix B.2 specifies what each source can reproduce and its limits. Removal weights and review-surface annotations
are attached only after transparency normalization. They support population assignment and bounded investigative
illustrations, but cannot alter terminal resolution states or the RQ1 and RQ2 estimands.
5 RQ1: Prevalence of the Seller-Identity Gap
RQ1 asks how much of the complete declared authorization surface fails the public seller-account check under the
coverage-aware evidence rule, and how the resulting floor differs between reference and enforcement-linked populations.
5.1 Baseline and Enforcement-Linked Step
Table 3 and Figure 2 show substantial non-resolution even in the reference: 24.25% of 40,384,095 declaration rows.
The floor rises to 30.71%, 31.55%, and 33.08% in cumulative enforcement-linked populations. The reference estimate
is central: almost one public authorization path in four stops before a public seller-account record, compared with
almost one in three at the primary enforcement-linked threshold. The gap is therefore widespread rather than exclusive
to enforcement-linked inventory.
The primary comparison is 6.45 percentage points, or 26.6% relative to reference. Estimates then remain near one
third. The reference interval separates from every enforcement-linked interval, whereas marginal intervals for adjacent
enforcement-linked thresholds overlap. Overlap alone is not a test of a difference. A supplementary paired host
bootstrap, sampling disjoint threshold-membership strata jointly (1,000 replicates, seed 1701), gives a ≥1,000 minus
≥100 contrast of 0.84 points, with a pointwise 95% interval of [−0.24,1.85] . The evidence therefore supports a
reference-to-enforcement-linked step, not a statistically separated increase at every threshold. Because the thresholds
are nested observational strata, this pattern is not interpreted as a smooth dose-response relation or a causal effect;
supplementary intervals are not adjusted for multiple comparisons.
8

Declared but Unaccountable
The unit is a declaration row. Publishers with larger files contribute more weight, and one publisher may contain
resolved and absent paths. A host-level any-gap indicator would erase the extent of mixed resolution. Conversely, row
prevalence is not the share of publishers affected.
5.2 Coverage, Uncertainty, and Selection
Publisher bootstrap preserves each host’s complete declaration set. Intervals widen as declaration-bearing hosts fall
to 374 at the highest threshold. The ten largest hosts contribute 14.74% of declaration weight in the ≥1,000 cohort,
illustrating why host counts alone do not determine precision. Public-registry coverage ranges from 96.54% to 95.08%.
This variation is smaller than the primary contrast. Unavailable registries cannot inflate a population’s absent-only
numerator, although differential availability can affect the contrast between floors. Coverage therefore remains a
separate diagnostic rather than evidence of publisher opacity.
The comparison remains conditional on participation in transparency. Only 8.09% of candidate reference hosts and
1.85–3.34% of candidate enforcement-linked hosts expose usable declarations. The reference is low-removal rather than
verified benign; thresholds are cumulative; and removal volume is an enforcement-attention signal. Percentages describe
declaration rows among participating hosts, not all candidate hosts, monetized publishers, or publisher prevalence.
5.3 Answer to RQ1
The seller-identity gap is widespread across the observed declaration surface and higher in the selected enforcement-
linked populations. It affects 24.25% of reference declaration paths and 30.71% at the primary enforcement-linked
threshold, a 6.45-point step, then remains near one third at stricter thresholds. Under the stated evidence rule, these
estimates quantify how often a visible authorization loses its minimum public account-verification path; they do not
assign wrongdoing or responsibility.
6 RQ2: Structure of the Enforcement-Linked Difference
RQ1 establishes a 6.45-point reference-to-≥100 contrast. RQ2 asks where that difference lies across popularity support,
within-system non-resolution, and ad-system composition. The analysis is descriptive: it localizes the contrast without
interpreting the components as causes.
6.1 Publisher Popularity
Restricting enforcement-linked hosts to those in Tranco and comparing within common rank buckets leaves positive
differences of +5.29, +7.48, and +8.92 points. These are differences from rank-matched references, not replacement
gap estimates. Their persistence indicates that observed rank alone does not account for ordering on common support.
The comparison is a sensitivity analysis over observed popularity. We exclude hosts outside Tranco, and unobserved
differences in scale, maintenance, professionalization, or selection remain possible.
6.2 Common-Standard Decomposition
Standardized rates are 24.71%, 29.37%, 30.06%, and 31.26%. In the primary comparison, 4.65 points, approximately
72.1%, remain as the within-system component. The remaining 1.80 points, approximately 27.9%, form the ad-
system-composition-associated residual. Together they reconstruct the 6.45-point observed contrast for the chosen
standard.
Under common ad-system weights, most of the observed step remains within systems rather than disappearing with
population composition. The remaining 1.80 points include both differences in declaration mix and the restriction to
shared systems. On shared support alone, the observed contrast is 6.343 points: the support restriction contributes 0.109
points to the official residual, and reweighting on that support contributes 1.689 points. Shared systems cover 99.06% of
reference rows and 99.71% of rows in the primary enforcement-linked cohort. We retain the official 1.80-point residual
and refer to it below as the composition residual, with this support qualification. The allocation is standard-dependent
and localizes the contrast; it does not identify mediation, mechanism, diligence, or responsibility [83].
6.3 System Heterogeneity and Dated Registry Checks
Within-system floors range from near-complete resolution to approximately 66–100% non-resolution in a smaller class
of video, CTV , native, and retargeting systems. In many systems, the enforcement-linked endpoint exceeds reference,
9

Declared but Unaccountable
24 26 28 30 32 34
Seller-identity gap (%)
Reference
≥ 100
≥ 1,000
≥ 10,000
6.45 pp observed
4.65 pp standardized
Observed gap Common-mix standardized
Figure 3: Observed and common-mix standardized gaps. The primary contrast falls from 6.45 to 4.65 points under
common system weights.
0 20 40 60 80 100
sharethrough
pubmatic
rubiconproject
openx
appnexus
video.unrulymedia
contextweb
indexexchange
yahoo
freewheel
Within-system seller-identity gap (%)
reference ≥ 10k removals
Figure 4: Within-system gap for ten high-volume systems. Open points show the reference, and filled points show the
cumulative≥10,000population.
which explains why common-mix standardization does not eliminate the contrast. System values are descriptive and do
not rank intent or responsibility. The ten systems in Figure 4 and the six excluded below form a fixed diagnostic panel,
not a newly selected top-ten ranking.
An independently logged check on August 13, 2026 preserves eight distinct-ID counts, HTTP outcomes, and redirect
destinations. Criteo’s redirect is retained as an alias, not treated as absence. The September frozen lookup contains
2,915 Outbrain IDs; the historical count of 1,000 cannot validate its completeness. The dated log is a limited retrieval
sanity check, not evidence of line-by-line equivalence or contemporary registry completeness. Original HTTP bodies
were not retained by that probe, so a byte-for-byte historical replay is unavailable. Neither registry size nor the check
explains why a particular coordinate is absent.
10

Declared but Unaccountable
Table 4: Distinct seller IDs in the canonical frozen registries, an independent August 13 count log, and canonical gap
floors (%). The August check is historical context, not a September validation.
System Frozen Aug. 13 Ref.≥10k
contextweb 46 46 68.7 73.4
yahoo 377 381 79.7 91.0
criteo∗ 1,652 1,651 92.3 99.6
outbrain 2,915 1,000 84.8 90.3
freewheel 2,260 2,250 81.5 95.1
indexexchange 4,065 4,072 65.7 75.3
pubmatic 6,515 6,476 7.9 13.1
sharethrough 5,205 5,191 1.2 2.1
∗criteo.com/sellers.jsonredirected tothemediagrid.com.
Table 5: Robustness checks. Popularity entries are deltas from rank-matched references. Other entries are floors.
Check Ref.≥100≥1,000≥10,000
Observed 24.25 30.71 31.55 33.08
Common mix 24.71 29.37 30.06 31.26
Popularity delta – +5.29 +7.48 +8.92
−freewheel 22.86 28.82 29.69 31.13
−criteo 23.86 30.26 31.08 32.59
−yahoo 23.76 30.03 30.81 32.33
−indexexchange 23.38 29.57 30.38 31.91
−outbrain 24.07 30.53 31.37 32.87
−contextweb 23.49 30.04 30.90 32.43
−all six 19.88 25.33 26.06 27.40
6.4 Influence Diagnostics
Dropping one panel system at a time preserves the step. Jointly dropping all six lowers absolute floors but leaves a 5.45-
point primary contrast and the ordering of point estimates. These systems therefore influence the level of non-resolution,
but neither a single system nor their joint exclusion accounts for the observed reference-to-enforcement-linked step.
Point-estimate ordering is not evidence of statistical separation between adjacent thresholds.
6.5 Answer to RQ2
The enforcement-linked difference persists on common popularity support and under common ad-system weights. Of the
6.45-point primary contrast, 4.65 points, approximately 72%, remain within systems, while 1.80 points, approximately
28%, form the composition residual, including the small support-restriction term. Registry-sparse systems raise absolute
floors but are not necessary for the population ordering. RQ2 therefore locates most of the difference within shared
systems, with a smaller composition-associated remainder, without attributing either component to a causal mechanism
or responsible actor.
7 Ad Transparency Intelligence and Reviewable Evidence
RQ1 and RQ2 measure the seller-identity gap at population scale. We next illustrate evidence-bearing investigation
without changing the estimand, common weights, or resolution states. We useAd Transparency Intelligenceto describe
this declaration-centered, ecosystem-level use of public advertising records: reconstructing and correlating declared
supply-chain relationships to identify recurring coordinates, shared configurations, and failed public joins. The objective
is not automatic attribution, but bounded public evidence that an analyst, intermediary, buyer, or regulator can inspect
and corroborate. Fan-out comes from the separately archived June 21 study; shared-content membership and four case
metrics use the canonical snapshot, with historical removal context identified separately. These illustrations are not
additional prevalence samples.
7.1 Recurring Seller-Account Coordinates
The June study groups declaration leads by (artifact family,canonical ad system,seller ID) . Keeping artifact family
in the key avoids merging coordinates from different declaration mechanisms without evidence. We count archived
grouped leads and distinct hosts; these leads are not interchangeable with raw normalized rows in the canonical snapshot.
Identifier-based linkage is an established practice [ 25–27]. The distribution compresses a large declaration surface
11

Declared but Unaccountable
Table 6: Seller-account fan-out in the archived June 21 removal-linked deep-mapping study. It does not compare
concentration with a matched reference or measure gap prevalence.
Metric Value
Seller-account clusters 321,097
Grouped declaration leads 15,269,683
Median hosts per account 2
99th percentile hosts 902
Maximum hosts 12,703
Fan-out Gini 0.920
Mixed DIRECT/RESELLER accounts 30,947
Table 7: Shared-content case. The selective link is one byte-identical ads.txt configuration published by 36 domains.
Property Value
Distinct domains 36
Shared content hashes 1
Accounts in shared file 4,120
Members with removal annotations 97.2%
Maximum removed URLs 98,759
into a smaller upper tail of reviewable coordinates. An ad system examining one high-fan-out coordinate can inspect
a relationship declared across hundreds or thousands of removal-linked hosts; a buyer or investigator can prioritize
coordinates affecting a large portion of the measured surface and identify the intermediary at which verification can
continue. This is investigative leverage grounded in declared reach, not evidence of misconduct. Fan-out includes
resolved and absent coordinates. A seller account may legitimately serve many publishers, and resale can create
broad reuse without concealing identity. Mixed relationship types can reflect legitimate differences in control, resale
paths, or file maintenance. The maximum-fan-out account resolves correctly. This counterexample demonstrates that
concentration and account absence are separate properties. The deep-mapping population has no matched concentration
reference, so the Gini and upper tail cannot be attributed specifically to enforcement-linked publishers.
7.2 Byte-Identical Declaration Configurations
A complementary surface asks whether distinct publishers expose the same complete authorization configuration. We
identify byte-identical declaration files by cryptographic hash. Unlike similarities inferred from names or external
technical properties, byte identity preserves the exact declared coordinates and ordering. One fixed hash is observed on
36 domains publishing the same ads.txt with 4,120 accounts; 97.2% of the matched historical member annotations
carry removal volume. The maximum removed-URL count is historical context, not a new September enforcement
observation. The canonical link is reproducible from the exact public bytes and exposes a common declaration
configuration that can be inspected once and traced across all observed members. It identifies a focused review surface
while retaining the underlying seller coordinates. Exact byte identity establishes a shared declaration configuration, not
common ownership, management, or coordinated misconduct. The same bytes may reflect common management, a
shared publishing service, distributed templates, or copying. The defensible finding is configuration identity.
7.3 Provenance-Bearing Case Packets
The four fixed illustrative publishers have declaration and resolution metrics recomputed under the canonical absent-
only floor. Their identities come from the historical case study, not from a search for extreme canonical outcomes.
Historical copyright-removal weights remain context, not contemporary traffic or prevalence evidence. Canonical source
hashes, declaration rows, registry provenance, alias decisions, and resolution states provide the available evidence
path; the manifest distinguishes these from historical annotations and does not promise that canonical inputs alone can
reconstruct every historical packet. The examples include small declared surfaces with high removal volume and broad
configurations that include both resolved and absent paths. Removal volume, declaration size, and gap fraction do not
move mechanically in tandem. A host-level binary would lose this internal structure. The cases demonstrate traceability,
not prevalence. Four selected publishers do not increase effective sample size or establish a case-level distribution.
Operationally, each packet identifies the exact publisher declaration, ad-system namespace, seller ID, registry state, and
evidence provenance for further review. It turns an aggregate result into a bounded, reproducible investigative lead
without extending inference beyond public records.
12

Declared but Unaccountable
Table 8: Four fixed anonymized cases with canonical declaration metrics and absent-only gap floors. Removed URLs
retain historical context. The cases are not used to estimate population rates.
Case Removed URLs Declarations Systems Accounts DIRECT rows Gap
High removal 51.9M 227 46 113 9 48.9%
Broad surface 1 10.9M 6,479 398 3,632 1,543 26.5%
Broad surface 2 5.5M 11,032 616 8,344 4,006 36.4%
Sparse surface 3.3M 138 46 138 2 18.1%
Table 9: Bounded follow-up actions at the public seller-account boundary.
Actor Bounded action
Ad system Reconcile declared coordinates; publish the account or an explicit invalid/stale state
Publisher Remove stale rows and obtain current coordinates
Buyer / DSP Prioritize unresolved paths without equating resale or concentration with abuse
Standards body Define outcomes for presence, confidentiality, aliases, malformed registries, and unavailable
evidence
Researcher / regulator Measure recurrence and remediation under comparable populations, versions, coverage, and
provenance
7.4 What the Investigative Surfaces Add
Recurring coordinates prioritize relationships by declared reach. Content identity identifies configurations replicated
across publishers. Canonical case metrics connect selected hosts to row- and registry-level evidence. These structures
offer complementary investigative paths, with distinct source dates and units; the historical fan-out export is not an
automatic row-level drill-down from a canonical population cell. This declaration-native workflow supports correlation,
corroboration, and review prioritization while preserving the distinction between a public lead and attribution. None
justifies automatic blocking, delisting, reputational labeling, ownership attribution, or a revenue claim. We do not
evaluate analyst performance, workload, prioritization gain, or an end-to-end investigative workflow.
8 Discussion and Implications
The results support one central interpretation: public participation in advertising transparency does not equal public
accountability. A declared path becomes minimally accountable only when its namespace-safe coordinate resolves in
the applicable available registry.
8.1 Participation Is Not Accountability
The important distinction is not visible versus invisible, but whether visible authorization terminates at the account
record promised by the standards. This property is orthogonal to pooling: a high-fan-out account may resolve correctly,
while a coordinate declared once may be absent. Account presence is necessary but insufficient for complete identity,
legal-entity attribution, contract validity, execution, or payment.
The substantial 24.25% reference floor means non-resolution is widespread rather than exclusive to enforcement-linked
inventory. Conversely, higher floors in enforcement-linked populations do not imply that individual publishers or
intermediaries caused the difference or acted improperly. The result identifies a supply-chain integrity problem: visible
authorization metadata can remain syntactically usable while the reciprocal public account control fails. Buyers,
exchanges, validators, brand-safety systems, regulators, and investigators can consume the declaration but cannot
complete the verification path the public mechanism promises. This verifier-visible break is the security-measurement
object studied here.
8.2 State-Aware Conformance and Path-Specific Remediation
A useful validator should preserve resolved, absent, confidential, aliased, malformed, unavailable, and otherwise
non-evaluable outcomes rather than collapse them into pass/fail. An absent ID under an available registry supports
account review; an unavailable registry supports endpoint remediation and retry; a confidential record preserves account
presence without disclosure; an alias should require a versioned rule.
13

Declared but Unaccountable
The check can run without inspecting personal data or creative content and can act on an affected seller path rather
than the entire publisher. Table 9 maps each evidence state to a bounded follow-up action: reconciliation for a missing
account, endpoint repair for unavailable evidence, disclosure-aware handling for confidential records, and versioned
treatment for aliases. These are implementable implications of the state model, not evaluated policies. We do not
estimate implementation cost, false-positive burden, analyst performance, adoption feasibility, or auction effects.
8.3 Interpreting the Decomposition
The 4.65-point within-system component points to follow-up on account and registry reconciliation within shared
systems. The 1.80-point composition-associated residual directs attention to declaration mix and the small contribution
of the shared-support restriction. Neither identifies mechanism or responsibility. Aggregate change can reflect resolved
accounts, removed declarations, new aliases, composition change, reduced participation, or lost coverage. A lower floor
caused only by lost registry coverage is not an improvement.
The distinction also provides a more informative basis for future longitudinal evaluation. Improvement within an ad
system should primarily reduce the within-system component, whereas changes in the intermediaries used by publishers
or buyers should primarily affect the composition residual. Tracking both quantities can distinguish repair of public
account resolution from a shift in declaration mix, provided populations, common support, common weights, parser
rules, and registry coverage remain comparable, and support changes are reported separately.
8.4 Ad Transparency Intelligence Without Automatic Attribution
Recurring coordinates, byte-identical files, and provenance-bearing case packets turn a large integrity surface into
reviewable evidence. In the Ad Transparency Intelligence framing introduced above, these surfaces support relationship
reconstruction, correlation, corroboration, and review prioritization by showing which seller coordinates recur, which
complete configurations are shared, where public joins fail, and which intermediary provides the next verifiable point of
inquiry.
This investigative value does not require equating correlation with attribution. Fan-out includes resolved and absent
coordinates; the maximum-fan-out account resolves. Byte-identical files establish configuration identity but may result
from shared services, templates, or copying. Case packets preserve the exact evidence path but do not reveal intent or
beneficial ownership. The surfaces therefore support targeted corroboration rather than automatic blocking, delisting,
reputational labeling, or claims of common control [25–27].
8.5 Remediation and the Declared–Observed Research Boundary
Prior notification work supplies a natural intervention-study design [ 54]. Vekaria et al. used contact information
exposed through ads.txt and sellers.json to reach relevant stakeholders, providing a concrete precedent for a
future notification study. Our paper neither sends notifications nor evaluates their effectiveness, and we do not assume
public contact information exists, is current, or is sufficient for remediation. A future snapshot can distinguish newly
published accounts, publisher-removed declarations, documented aliases, recovered availability, and persistent gaps.
Comparable populations, parser versions, canonicalization rules, alias rules, evidence states, common weights, and
registry coverage are necessary so lost observability isn’t mistaken for improvement.
A second research direction is systematic comparison between declared relationships and live RTB evidence. Recon-
structing the public seller-account graph establishes which paths are declared and publicly resolvable; the next question
is which of those paths become observable in request routing, bidding, winning, billable impressions, settlement, or
payout. These stages require a dedicated sampling frame, coverage model, and phase-aware identifiers, and must remain
analytically distinct [79–81]. The present paper establishes the declaration-side prerequisite for that comparison rather
than anticipating its empirical results.
9 Limitations
The study measures a specific public seller-account property under explicit construct, population, temporal, statistical,
and review boundaries. These limits define the inference supported by the declaration-side evidence rather than reducing
the value of the public-account check.
14

Declared but Unaccountable
9.1 Construct and Attribution Boundaries
The construct ends at exact public account presence. A present ID does not validate name, domain, legal entity,
beneficial owner, contract, authorization at auction time, or activity. A confidential record establishes presence while
withholding identity. An absent ID does not prove that no private account or contract exists. Public artifacts reveal
a state but not whether it stems from a stale or copied declaration, migration, error, registry omission, unpublished
private account, or fabrication. Pooling, relationship mismatch, account absence, identity disclosure, execution, and
payment are distinct. Fan-out, mixed relationships, byte-identical files, and case packets are declaration-native review
signals. They can identify recurring coordinates, shared configurations, and exact evidence paths, but do not establish
ownership, coordination, intent, or abuse.
9.2 Population, Participation, and Temporal Scope
The reference is high-popularity and low-removal, not verified benign. Copyright-removal counts reflect enforcement
attention and can depend on scale, visibility, rights-holder effort, reporting practice, and duplicated URLs. Populations
are cumulative observational strata, not treatments. Only hosts exposing usable declarations contribute rows. Participa-
tion differs substantially across candidate populations. Results characterize participating hosts’ declared surface, not all
candidates, all removal targets, all monetized publishers, or the share of publishers affected. Row weighting gives more
weight to declaration-heavy publishers. Host-level, unique-coordinate, DIRECT-only, and conditional estimands answer
different questions.
The estimator uses a frozen snapshot assembled from observations with different timestamps, not a simultaneous crawl.
Declarations, registries, redirects, aliases, confidentiality, and states change over time. The August count log and June
fan-out study are separately dated and do not validate September completeness or establish ecosystem-wide stability,
persistence, incidence, or remediation. The count-only August probe cannot be replayed byte for byte because it did not
retain response bodies.
9.3 Measurement and Statistical Uncertainty
Unavailable registries remain in the denominator and cannot enter the numerator, making that source of missingness
conservative. Other errors need not be one-sided: alias, canonicalization, parser, or materialization errors can move
rows between states. Raw values, hashes, bytes, versions, tests, and reason codes mitigate but do not eliminate these
risks.
Publisher-clustered bootstrap intervals address within-host dependence for the row estimand [ 82]. Publishers may
share files, accounts, providers, templates, or management, so not all ecosystem dependence is captured. Popularity
matching addresses observed Tranco support only. The common-standard decomposition is descriptive and depends on
the selected weights and shared support. The 4.65-point within-system component and 1.80-point composition residual
sum to the 6.45-point observed contrast under that standard; the residual includes 0.109 points from support restriction.
These components do not estimate mediation or causality [83].
9.4 Review-Surface and Case Boundaries
The historical deep-mapping population has no matched concentration reference. Its fan-out Gini and upper tail do not
show that concentration is distinctive of enforcement-linked inventory or predictive of absence. The maximum-fan-out
account was resolved in that dated study. Four cases illustrate available canonical evidence paths, not prevalence, ground
truth, or increased sample size. Historical removal context is not a new measurement of enforcement activity. Analyst
accuracy, workload, cost, prioritization gain, false-positive burden, notification, and remediation are not evaluated.
9.5 Boundary with Observable Execution
Public declarations record claimed authorization relationships; they do not establish that a seller account participated
in a live auction or received economic benefit. Request routing, returned bids, wins, billable impressions, settlement,
and publisher payout are separate evidentiary stages. A future declared–observed study must model their sampling,
coverage, identifiers, and inference independently rather than treating browser-visible traffic as a direct validation of the
declaration-row floor.
Scope of claims.On the frozen transparency-participating surface, a substantial fraction of authorizations point
to seller IDs absent from applicable available registries, and the floor is higher in the selected enforcement-linked
populations. The paper quantifies and localizes this public-account failure and connects it to reviewable declaration
15

Declared but Unaccountable
evidence. It does not establish why an account is absent, who is responsible, whether review signals indicate common
control, whether a declared path executed in live advertising traffic, or whether money changed hands.
10 Conclusion
Public advertising transparency becomes accountable only when a seller coordinate declared by a publisher resolves to
the account record promised by the applicable available registry. We formalize failure of this minimum property as the
seller-identity gap and measure it using 233,416,998 normalized advertising-transparency records under an absent-only,
coverage-aware evidence rule.
The result is substantial: the gap affects 24.25% of declaration paths in the high-popularity, low-removal reference
and 30.71% at the primary enforcement-linked threshold, a 6.45-point step, before remaining near one third at stricter
thresholds. Under common weights over 1,469 ad systems, 4.65 points, approximately 72%, remain within systems,
while 1.80 points, approximately 28%, form the composition residual, including the small support-restriction term. The
decomposition locates most of the observed difference within shared systems, with a smaller composition-associated
remainder, without assigning cause or responsibility.
Recurring seller-account coordinates, byte-identical declaration configurations, and provenance-bearing case packets
translate these population results into reviewable evidence. We frame this declaration-centered investigative use of
public advertising records as Ad Transparency Intelligence: a reproducible way to reconstruct declared relationships,
identify where public verification stops, and prioritize corroboration. These surfaces support investigation without
converting correlation into ownership, intent, misconduct, or economic attribution.
The resulting contribution is a controlled path from a public security property, to population-scale measurement, to
comparative localization, and finally to the exact declaration and registry evidence that produced the result. The next
step is a systematic comparison with live RTB traffic, which requires its own sampling frame, coverage model, and
phase-aware identifiers. Advertising transparency supports accountability and investigation only when declarations
remain publicly verifiable; measuring where that verification fails turns a nominal transparency mechanism into a
reviewable security surface.
A Ethical Considerations
This study analyzes public advertising-transparency artifacts to measure public seller-account non-resolution and
construct declaration-native review surfaces. The design minimizes operational impact and separates reproducible
findings from claims about identity, intent, ownership, coordination, or economic outcome. An absent public record is a
verifier-visible state, not a characterization of an actor.
Public-data acquisition and load minimization.Collection is rate-limited and preserves retrieval status, timestamps,
redirects, hashes, source runs, and parser provenance. Repeated requests are not substitutes for missing evidence. The
study does not bypass authentication, purchase advertising, click ads, submit conversions, or interfere with auctions.
Failed or challenged retrievals remain explicit measurement states rather than triggering aggressive recovery.
Data minimization and sensitive fields.The pipeline retains public declaration and registry artifacts, technical
metadata, hashes, account coordinates, and provenance needed for resolution and verification. The pipeline processes
exact identifiers and source records only as needed to reproduce the public-account check, construct review surfaces,
and support controlled case validation. Materials that are unnecessary for verification are aggregated, transformed,
restricted, or withheld. Public availability does not remove the obligation to minimize redistribution risk.
Population labels and reporting.Removal information constructs observational populations and is not ground truth
for infringement, intent, seller behavior, or intermediary knowledge. Results are reported in aggregate.Cases are reported
in anonymized form, with exact identifiers retained in a supervised evidence key. The fixed historical case identities
are independent of the canonical population results; their metrics are recomputed without outcome-based replacement.
Neither the selected cases nor the deep-mapping review surfaces constitute additional prevalence observations.
Responsible disclosure.Any notification is scoped to verifiable path, namespace, seller ID, registry state, source
hash, line position, retrieval provenance, and reason code. It must distinguish absent from unavailable, malformed,
confidential, aliased, and non-evaluable states. It does not claim fraud, infringement, common ownership, contractual
non-authorization, revenue, or payment without independent evidence. The manuscript must describe only disclosure
actually completed before submission.
16

Declared but Unaccountable
Risk of misuse.Recurring coordinates, byte-identical declaration configurations, and case packets can support
legitimate review but may be misinterpreted as blocklists or attribution evidence. We mitigate this risk by preserving
terminal states, presenting alternative explanations, anonymizing cases during review, and recommending path-specific
corroboration rather than automatic blocking, delisting, or reputational labeling. The artifact release applies the
same boundary: enough provenance to reproduce the aggregate findings and verify selected cases, without turning
investigative leads into unsupported accusations.
B Open Science
The accompanying artifact supports verification of the public-data measurements, common-standard decomposition,
and declaration-native investigative surfaces while respecting the disclosure boundaries in Appendix A. Availability and
reproducibility claims in this paper are limited to the materials identified in the artifact manifest.
B.1 Artifact Contents and Traceability
The release distinguishes five linked object families:
• Artifact objects: requested URLs, redirect chains, outcomes, timestamps, hashes, artifact families, parser
versions, and source runs;
• Declaration objects: hosts, source lines, raw and canonical ad-system domains, seller IDs, relationship types,
and source provenance;
• Registry objects: seller records, availability and parser states, confidentiality indicators, hashes, and prove-
nance;
•Resolution objects: declaration-to-registry links, alias decisions, terminal states, and reason codes;
•Population objects: frozen host labels and the corresponding removal and popularity inputs.
The artifact manifest identifies schemas, configurations, derived objects, analysis code, versions, file sizes, and
cryptographic digests, and assigns each aggregate to its actual source. Canonical population aggregates are traceable to
normalized resolution rows and, where disclosure permits, source hashes, line positions, parser versions, alias rules,
and collection runs. The historical grouped fan-out export and count-only registry log have different reproducibility
boundaries. Complete canonical exports, rather than selected case packets, remain the source of population estimates.
B.2 Reproducing the Main Claims
Canonical inputs support Tables 1, 3, 5, 10, and 11: RQ1 denominators, absent-only numerators, registry coverage and
host-bootstrap intervals, and RQ2 within-system floors, common weights, standardized rates, and the 4.65/1.80-point
decomposition. Tables 2 and 9 describe the method and bounded follow-up actions rather than empirical aggregates.
Separately dated sources are not attributed to the canonical snapshot. Table 4 combines canonical frozen-registry
counts and floors with the independently logged August 13 retrieval counts; the log reproduces eight counts and
retrieval outcomes, but not original response bodies. Table 6 uses the archived June 21 grouped lead export: its cluster
distribution and Gini can be recomputed from that export, not from a claim that every grouped lead is a canonical
resolution row. Table 7 revalidates a fixed exact-content group against canonical observations, retaining historical
removal context. Table 8 recomputes the declaration and resolution metrics for the four fixed case hosts; historical
removal weights come from a separate source. Table 12 sums the surviving lane summaries deduplicated by lane and
run identifier at the declared cutoff. It does not establish that every past acquisition is retained.
The provenance manifest preserves source dates, hashes, units, derivation rules, and access conditions. The June
full-frontier export lacks a historical output digest; a digest computed during recovery identifies the preserved file, not
contemporaneous proof of its completeness. Workflows keep acquisition quantities, normalized objects, grouped leads,
declaration rows, resolution states, population estimates, and review objects distinct, and report unavailable evidence
explicitly.
B.3 Review-Surface and Controlled Materials
The releasable review materials comprise schemas, derivation code, aggregate fan-out statistics, exact-content grouping
logic, anonymized case structures, and non-sensitive provenance fields identified in the artifact manifest. We transform,
restrict, or withhold exact operational identifiers, anonymization keys, supervised case mappings, and materials whose
17

Declared but Unaccountable
release could enable unsupported attribution. The manifest records the treatment and disclosure rationale applied to
each non-public material.
B.4 Supporting Measurement Results
Table 10: Within-system floors for five fixed high-volume diagnostic systems. The Rows column sums population
memberships, including nested cohorts, not globally distinct declarations. Values do not rank responsibility or
culpability.
System Rows Ref.≥100≥1k≥10k
pubmatic 4,084,298 7.94% 11.95% 11.94% 13.10%
rubiconproject 3,205,965 13.08% 18.24% 18.87% 21.58%
appnexus 2,480,941 29.15% 32.83% 32.78% 34.32%
openx 1,841,776 16.25% 20.46% 20.74% 23.40%
video.unrulymedia 1,413,551 25.00% 36.31% 37.83% 40.04%
Table 11: Within-system floors for the remaining five high-volume systems. This table continues Table 10.
System Rows Ref.≥100≥1k≥10k
freewheel 1,247,843 81.52% 92.23% 93.37% 95.08%
indexexchange 1,084,825 65.68% 73.33% 73.56% 75.26%
sharethrough 1,050,204 1.17% 1.64% 1.64% 2.13%
contextweb 846,964 68.75% 69.78% 70.46% 73.37%
yahoo 473,413 79.68% 87.38% 88.02% 91.04%
Table 12: Surviving transparency campaign summaries, April 16–September 21, deduplicated by lane and run ID at
September 28, 08:30:43 UTC. Acquisition quantities do not enter gap denominators or prove a complete acquisition
census.
Artifact Runs Fetches Candidates Valid
ads.txt1,422 34,389,408 28,208,567 18,252,554
app-ads.txt1,179 13,611,691 11,020,427 5,403,969
sellers.json706 3,220,992 2,647,009 343,655
Total 3,307 51,222,091 41,876,003 24,000,178
B.5 Release Statement
The artifact manifest records the repository or archive, version, license, and access conditions used for the submission.
It specifies which materials are released, transformed, restricted, or withheld and provides the corresponding disclosure
rationale. Claims of artifact availability, functionality, and reproducibility in this paper apply only to the contents and
access conditions recorded in that manifest.
Author Note
The affiliation identifies Tommaso Grotto’s current professional role. His contribution to this research was undertaken
in a personal capacity.
References
[1] Michail Batikas, Jorg Claussen, and Christian Peukert. Follow the Money: Online Piracy and Self-Regulation in
the Advertising Industry, 2019.
[2] M. Zubair Rafique et al. It Is Free for a Reason: Exploring the Ecosystem of Free Live Streaming Services, 2016.
[3] Hussein Sheaib, Anja Feldmann, and Ha Dao. Unmasking the Shadows: A Cross-Country Study of Online
Tracking in Illegal Movie Streaming Services, 2025.
[4] European Union Intellectual Property Office and White Bullet. Online Advertising on IPR-Infringing Websites
and Apps 2025, 2026.
18

Declared but Unaccountable
[5] Emmanouil Papadogiannakis et al. Who Funds Misinformation? A Systematic Analysis of the Ad-Related Profit
Routines of Fake News Sites, 2023.
[6] Digital Citizens Alliance and White Bullet. Breaking (B)ads: How Advertiser-Supported Piracy Helps Fuel a
Booming Illegal Market, 2021.
[7] Digital Citizens Alliance and White Bullet. From Piracy to Ads to Ransomware: How Illicit Actors Use Digital
Ads on Piracy Sites, 2022.
[8] Association of National Advertisers. Programmatic Media Supply Chain Transparency Study, 2023.
[9] ISBA, Association of Online Publishers, and PwC. Programmatic Supply Chain Transparency Study, 2020.
[10] Kroll. ANA Programmatic Media Supply Chain Transparency Study: Qualitative Insights, 2023.
[11] IAB Tech Lab. Authorized Digital Sellers (ads.txt), Specification v1.1, 2022.
[12] IAB Tech Lab. app-ads.txt: Authorized Sellers for Apps, 2019.
[13] IAB Tech Lab. sellers.json and the OpenRTB SupplyChain Object, 2019.
[14] Muhammad Ahmad Bashir, Sajjad Arshad, Engin Kirda, William Robertson, and Christo Wilson. A Longitudinal
Analysis of the ads.txt Standard, 2019.
[15] Yash Vekaria, Rishab Nithyanand, and Zubair Shafiq. The Inventory Is Dark and Full of Misinformation:
Understanding Ad Inventory Pooling in the Ad-Tech Supply Chain, 2024.
[16] Emmanouil Papadogiannakis, Nicolas Kourtellis, Panagiotis Papadopoulos, and Evangelos P. Markatos. Welcome
to the Dark Side: Analyzing the Revenue Flows of Fraud in the Online Ad Ecosystem, 2025.
[17] Benjamin Poilve. Discover the Advertising Web with Sellers.json Files, 2020.
[18] IAB Europe. Adoption of Supply Chain Transparency Standards in Europe, 2025.
[19] Rocky Moss. Evaluating the Ecosystem: What We Have Learned by Matching ads.txt Entries to sellers.json Files,
2021.
[20] Rocky Moss. Further Investigation into the Dark Pool Sales House Phenomenon, 2021.
[21] Kyle Smith. Correlation Study Between ads.txt and sellers.json, 2020.
[22] ivp5. ads.txt Framework Integrity Audit, 2026.
[23] Victor Le Pochat et al. Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation, 2019.
[24] Google. Content Delistings Due to Copyright: Google Transparency Report, 2026.
[25] Oleksii Starov et al. Betrayed by Your Dashboard: Discovering Malicious Campaigns via Web Analytics, 2018.
[26] Emmanouil Papadogiannakis et al. Leveraging Google Publisher-Specific IDs to Detect Website Administration,
2022.
[27] Adalytics. Using Network Analysis to Identify Related Websites, 2021.
[28] Paul Vines, Franziska Roesner, and Tadayoshi Kohno. Exploring ADINT: Using Ad Targeting for Surveillance on
a Budget, 2017.
[29] IAB Tech Lab. OpenRTB Specification v2.6, 2022.
[30] IAB Tech Lab. AdCOM: Advertising Common Object Model, 2024.
[31] IAB Tech Lab. Digital Video Ad Serving Template (V AST) v4.3, 2022.
[32] Jounce Media. The Marketer Guide to Programmatic Reselling, 2025.
[33] Athanasios Andreou et al. Investigating Ad Transparency Mechanisms in Social Media: A Case Study of Facebook
Explanations, 2018.
[34] Mozilla Foundation and CheckFirst. Full Disclosure: Stress Testing Tech Platforms Ad Repositories, 2024.
[35] Abir Benzaamia, Asmaa El Fraihi, Ines Abdelaziz, and Oana Goga. A Year Under the DSA: Ad Transparency
Uneven Landscape, 2026.
[36] Daniel Angus et al. Computational Methods for Improving the Observability of Platform-Based Advertising,
2024.
[37] Daniel Angus et al. The Australian Ad Observatory: Technical and Data Report, 2024.
[38] Interactive Advertising Bureau, Ernst, and Young. What Is an Untrustworthy Supply Chain Costing the U.S.
Digital Advertising Industry?, 2015.
19

Declared but Unaccountable
[39] IAB Tech Lab. Transparency Center and Supply-Chain Validation Tools, 2026.
[40] Lia Bozarth and Ceren Budak. Market Forces: Quantifying the Role of Top Credible Ad Servers in the Fake News
Ecosystem, 2021.
[41] Wajeeha Ahmad, Ananya Sen, Charles Eesley, and Erik Brynjolfsson. Companies Inadvertently Fund Online
Misinformation Despite Consumer Backlash, 2024.
[42] Jonathan Taplin. USC Annenberg Lab Ad Transparency Report: January, 2013.
[43] Google and White Ops. The Hunt for 3ve: Taking Down a Major Ad Fraud Operation, 2018.
[44] Brett Stone-Gross et al. Understanding Fraudulent Activities in Online Ad Exchanges, 2011.
[45] Kevin Springborn and Paul Barford. Impression Fraud in On-line Advertising via Pay-Per-View Networks, 2013.
[46] Paul Pearce et al. Characterizing Large-Scale Click Fraud in ZeroAccess, 2014.
[47] Vacha Dave, Saikat Guha, and Yin Zhang. Measuring and Fingerprinting Click-Spam in Ad Networks, 2012.
[48] Neha Chachra, Stefan Savage, and Geoffrey M. V oelker. Affiliate Crookies: Characterizing Affiliate Marketing
Abuse, 2015.
[49] Kurt Thomas et al. Ad Injection at Scale: Assessing Deceptive Advertisement Modifications, 2015.
[50] Apostolis Zarras et al. The Dark Alleys of Madison Avenue: Understanding Malicious Advertisements, 2014.
[51] Zhou Li et al. Knowing Your Enemy: Understanding and Detecting Malicious Web Advertising, 2012.
[52] Emmanouil Papadogiannakis et al. Ad Laundering: How Websites Deceive Advertisers into Rendering Ads Next
to Illicit Content, 2024.
[53] Emmanouil Papadogiannakis et al. Before and After: The Effect of EU 2022 Code of Practice on Disinformation,
2025.
[54] Yash Vekaria, Rishab Nithyanand, and Zubair Shafiq. Towards multi-stakeholder vulnerability notifications in
the ad-tech supply chain. In2026 IEEE 11th European Symposium on Security and Privacy (EuroS&P), pages
874–891. IEEE, 2026. doi:10.1109/EuroSP68448.2026.00061.
[55] Steven Englehardt and Arvind Narayanan. Online Tracking: A 1-Million-Site Measurement and Analysis, 2016.
[56] Sandra Siby et al. WebGraph: Capturing Advertising and Tracking Information Flows for Robust Blocking, 2022.
[57] Emmanouil Papadogiannakis et al. User Tracking in the Post-Cookie Era: How Websites Bypass GDPR Consent
to Track Users, 2021.
[58] Iskander Sanchez-Rola et al. Journey to the Center of the Cookie Ecosystem: Unraveling Actors Roles and
Relationships, 2021.
[59] Tobias Urban et al. Measuring the Impact of the GDPR on Data Sharing in Ad Networks, 2020.
[60] Giridhari Venkatadri et al. Privacy Risks with Facebook PII-Based Targeting: Auditing a Data Broker Advertising
Interface, 2018.
[61] Cumhur Oh, Chris Kanich, Damon McCoy, and Paul Pearce. Cart-ology: Intercepting Targeted Advertising via
Ad Network Identity Entanglement, 2022.
[62] Aleksandra Korolova. Privacy Violations Using Microtargeted Ads: A Case Study, 2011.
[63] Catherine Han, Deepak Kumar, and Zakir Durumeric. On the Infrastructure Providers That Support Misinformation
Websites, 2022.
[64] Austin Hounsel et al. Identifying Disinformation Websites Using Infrastructure Features, 2020.
[65] Frank Cangialosi et al. Measurement and Analysis of Private Key Sharing in the HTTPS Ecosystem, 2016.
[66] Sumayah Alrwais et al. Under the Shadow of Sunshine: Understanding and Detecting Bulletproof Hosting on
Legitimate Service Provider Networks, 2017.
[67] Chaoyi Lu et al. From WHOIS to WHOW AS: A Large-Scale Measurement Study of Domain Registration Privacy
under the GDPR, 2021.
[68] Jeffery Kline, Aaron Cahn, and Paul Barford. Placement Laundering and the Complexities of Attribution in Online
Advertising, 2018.
[69] Muhammad Ahmad Bashir, Sajjad Arshad, William Robertson, and Christo Wilson. Tracing Information Flows
Between Ad Exchanges Using Retargeted Ads, 2016.
20

Declared but Unaccountable
[70] Muhammad Ahmad Bashir and Christo Wilson. Diffusion of User Tracking Data in the Online Advertising
Ecosystem, 2018.
[71] John Cook, Rishab Nithyanand, and Zubair Shafiq. Inferring Tracker-Advertiser Relationships in the Online
Advertising Ecosystem Using Header Bidding, 2020.
[72] Michalis Pachilakis, Panagiotis Papadopoulos, Evangelos P. Markatos, and Nicolas Kourtellis. No More Chasing
Waterfalls: A Measurement Study of the Header Bidding Ad-Ecosystem, 2019.
[73] Waqar Aqeel et al. Untangling Header Bidding Lore: Some Myths, Some Truths, and Some Hope, 2020.
[74] Maaz Bin Musa and Rishab Nithyanand. ATOM: Ad-Network Tomography, 2022.
[75] Shuai Yuan, Jun Wang, and Xiaoxue Zhao. Real-Time Bidding for Online Advertising: Measurement and Analysis,
2013.
[76] Lukasz Olejnik, Minh-Dung Tran, and Claude Castelluccia. Selling Off Privacy at Auction, 2014.
[77] Panagiotis Papadopoulos et al. If You Are Not Paying for It, You Are the Product: How Much Do Advertisers Pay
to Reach You?, 2017.
[78] Eric Zeng, Rachel McAmis, Tadayoshi Kohno, and Franziska Roesner. What Factors Affect Targeting and Bids in
Online Advertising? A Field Measurement Study, 2022.
[79] Antonio Pastor, Ruben Cuevas, Angel Cuevas, and Arturo Azcorra. Establishing Trust in Online Advertising with
Signed Transactions, 2021.
[80] Ke Zhong, Yiping Ma, Yifeng Mao, and Sebastian Angel. Addax: A Fast, Private, and Accountable Ad Exchange
Infrastructure, 2023.
[81] Media Rating Council. Digital Advertising Auction Transparency Standards, 2026.
[82] A. Colin Cameron, Jonah B. Gelbach, and Douglas L. Miller. Bootstrap-Based Improvements for Inference with
Clustered Errors, 2008.
[83] Evelyn M. Kitagawa. Components of a Difference Between Two Rates, 1955.
21
