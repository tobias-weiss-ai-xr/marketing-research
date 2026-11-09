---
title: Synthetic Customer 360 Benchmark for Customer Data Quality, Identity Resolution, and Survivorship
  in Omnichannel Retail
url: https://doi.org/10.21203/rs.3.rs-10525890/v1
category: cx-retail
subcategory: framework
date: 2026-07
venue: ''
authors:
- PRADEEP ARONKAR
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10525890/latest.pdf
pages: 18
chars: 56271
fetched_at: '2026-11-08T17:24:53+00:00'
kb_version: 1
---

# Synthetic Customer 360 Benchmark for Customer Data Quality, Identity Resolution, and Survivorship in Omnichannel Retail

Synthetic Customer 360 Benchmark for Customer
Data Quality, Identity Resolution, and Survivorship
in Omnichannel Retail
PRADEEP ARONKAR 
Independent Researcher https://orcid.org/0009-0000-0152-869X
Research Article
Keywords: customer data quality, customer data uniﬁcation architecture, omnichannel retail, Customer
360, identity resolution, entity resolution, record linkage, master data management, synthetic data
generation, benchmark datasets, survivorship rules, golden record, data lineage, data integration, data
engineering
Posted Date: July 31st, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10525890/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: The authors declare no competing interests.

Synthetic Customer 360 Benchmark for Customer
Data Quality,
Identity Resolution, and Survivorship in Omnichannel
Retail
Pradeep Aronkar
Independent Researcher
────────────
Abstract
In omnichannel retail, customer data quality and unification architecture encompasses the syste ms
and controls that turn fragmented customer observations into trusted, unified profiles, yet rigorous
evaluation is constrained by limited access to shareable records with known identity, defect, data-
lineage, and survivorship ground truth. This paper presents a synthetic Customer 360 benchmark
and generation method for controlled evaluation of identity resolution, data-quality transformations,
and golden-record survivorship rules. The benchmark models persons, households, accounts,
contact points, addresses, source observations, and transaction or order context across four profiles:
ecommerce, loyalty or mobile, physical-store transaction, and service or fulfillment. It gener ates
structural duplicates and eight auditable defect, ambiguity, and conflict mechanisms while preserving
separate ground truth for duplicate clusters, transformation lineage, and expected outputs under
verification-first, source-authority-first, recency-first, and mixed-conditional regi mes. The study
evaluates the benchmark through 335 predeclared runs organized into identity-difficulty,
survivorship-conflict, single-factor-sensitivity, and scale experiments. Three transparent identit y
baselines are reported with pairwise and B-cubed measures; survivorship is assessed through
applicability, evaluability, union and pairwise disagreement, conditional disagreeme nt rate, and
population-level burden. All 335 confirmatory runs passed validation. In 40 paired seeds, the easy
identity condition exceeded the hard condition for weighted-similarity pairwise F1 at the primary 0.85
threshold, with a median paired difference of 0.5846 and a Holm-adjusted one-sided p value of 1.82
× 10 ⁻„†. The direction held at predeclared thresholds of 0.80, 0.85, and 0.90. High-conflict
survivorship conditions exceeded low-conflict conditions in all 40 paired seeds, with a median
conditional-disagreement increase of 0.0577 and the same adjusted p value. These findings
demonstrate reproducible condition separation and auditable ground truth under the disclosed
synthetic design. They do not establish real-retailer prevalence, operational effectiveness,
production scalability, or universal superiority of any resolution or survivorship rule.
Keywords: customer data quality; customer data unification architecture; omnichannel retail;
Customer 360; identity resolution; entity resolution; record linkage; master data management;
synthetic data generation; benchmark datasets; survivorship rules; golden record; data lineage; data
integration; data engineering
1. Introduction
Customer data quality and unification architecture in omnichannel retail comprises the data
engineering, data integration, master data management, and governance methods that assess,
resolve, and manage fragmented customer observations as reliable unified profiles. Evaluation of
identity resolution and survivorship rules requires more than a collection of plausible customer rows.
It requires known answers about which observations belong to the same person or household, which

values were changed, why a conflict exists, and what value a declared policy should select for the
golden record. Those answers are rarely available in shareable customer data because the records
are sensitive, operational rules are organization-specific, and the true identity structure i s only
partially observed.
Entity resolution addresses the problem of determining which records refer to the same real-w orld
entity. The field includes probabilistic record linkage, deterministic and learned matching, blocking,
clustering, and canonicalization (Fellegi & Sunter, 1969; Christen, 2012; Binette & Steorts,  2022).
Evaluation is difficult because pairwise links and entity clusters expose different error structures, and
common measures can rank the same results differently (Menestrina et al., 2010). Pairwis e
precision, recall, and F1 are useful for link-level errors, whereas B-cubed measures provide a
record-centered view of cluster structure and satisfy formal constraints that several alternative
clustering measures do not (Amigó et al., 2009). A defensible benchmark should therefore retain
exact ground truth and report more than one evaluation perspective.
Synthetic data generation can produce shareable records and exact labels, but general-purpose
systems commonly emphasize either statistical similarity to a source dataset or configurable
generation and corruption without representing the full decision context of customer unification.
GeCo supports personal-data generation and configurable corruption (Tran et al., 2013), while the
Synthetic Data Vault models multi-table data learned from real datasets (Patki et al. , 2016). Recent
work emphasizes transparent generation and structured validation of synthetic tabular data
(ApellÆniz et al., 2024; Schram et al., 2025). These contributions establish important capabilities, but
they do not jointly supply omnichannel source profiles, identity-cluster truth, transformation lineage ,
source authority, verification state, and regime-specific survivorship truth in one benchmark design.
This study addresses that bounded gap through a benchmark/resource-method contribution. It asks
four research questions: (RQ1) Can a configurable generator reproducibly create customer entities,
source observations, controlled data-quality defects, and internally consistent ground truth? (RQ2)
Do controlled parameter changes produce distinguishable identity-resolution conditions whil e
keeping duplicate-cluster topology fixed? (RQ3) Do controlled conflict changes produce
distinguishable survivorship conditions while keeping the evaluable candidate set fixed? (RQ4) What
limitations remain because the data are synthetic, deliberately simplified, and not cali brated to a
representative retail population?
The paper makes five contributions. First, it defines a Customer 360 benchmark design space that
connects customer entities, omnichannel source profiles, quality defects, ambiguity, confl icts, and
decision ground truth. Second, it provides a deterministic generation method with fixed seeds,
separated truth outputs, data lineage, hashes, manifests, and executable validation. Third, it
demonstrates three identity baselines and four survivorship regimes under predeclared conditions.
Fourth, it reports replicated evidence from 335 runs, including paired statistical tests, threshold
robustness, parameter sensitivity, and bounded scale characteristics. Fifth, it documents a stopped
execution attempt and narrow implementation correction, preserving failure evidence rather t han
silently replacing it.
The Related Work section positions the benchmark against entity-resolution evaluation,  synthetic-
data generation, data fusion and truth discovery, and computational benchmarking. The Benchmark
Design section defines the entities, profiles, transformations, and ground truth. The Generator an d
Validation Method section explains reproducibility, code execution, and validation gates. The
Experimental Design section defines conditions, baselines, metrics, hypotheses, and statistical
procedures. The Results section reports identity, survivorship, sensitivity, and scale findings. The
Discussion states the contribution, architectural implications, limitations, and release conditions.

2. Related Work
2.1 Entity Resolution and Evaluation
When dependable unique keys are absent, record linkage and entity-resolution methods infer which
records describe a common underlying entity. The Fellegi-Sunter model established a probabilistic
decision framework based on field-agreement patterns (Fellegi & Sunter, 1969). Later work
expanded the field across preprocessing, indexing, comparison, classification, clustering,
uncertainty, and privacy (Christen, 2012; Binette & Steorts, 2022). Contemporary experimental
studies compare language-model embeddings across established entity-resolution datasets (Zeak is
et al., 2023) and show that entity-matching performance and fairness can differ across demogra phic
groups and representation conditions (Shahbazi et al., 2023). These studies reinforce the value of
benchmark diversity: a method that appears strong under one record distribution may behave
differently when ambiguity, missingness, or similarity patterns change.
Evaluation requires explicit attention to the unit of error. Pairwise measures count correct ly and
incorrectly linked record pairs, which makes false merges costly because a large incorrect cluster
creates many false-positive pairs. Cluster-oriented measures instead evaluate how each record is
placed relative to its true entity. Menestrina et al. (2010) show that entity-resolution measures can
disagree, while Amigó et al. (2009) show that B-cubed precision and recall satisfy a set of formal
clustering constraints. This paper therefore reports pairwise and B-cubed measures together. It does
not treat either as a complete characterization of performance.
2.2 Synthetic Data Generation and Validation
Synthetic data can support research when real records are unavailable, restricted, or unsuitable for
redistribution. General-purpose approaches range from explicit generators and corruption functions
to models learned from real relational datasets. The generator associated with FEBRL produces
synthetic personal and household populations, applies controlled duplication and corruption, and
preserves links between original and altered records (Christen & Pudjijono, 2009). GeCo cre ates
personal records and configurable corruptions for data-matching experiments (Tran et al., 2013).
The Synthetic Data Vault models multi-table data and samples synthetic relati onal records (Patki et
al., 2016). Metasyn emphasizes transparent generation with explicit metadata and privacy-oriented
controls (Schram et al., 2025). Pseudopeople constructs a large simulated population and exposes it
through census, survey, and administrative-style data products, with configurable distortions and
identifiers that support linkage experiments (Haddock et al., 2024). RetailSynth instead simul ates
customer shopping behavior for pricing, promotion, and recommendation experiments (Xia et al.,
2023). These systems demonstrate distinct uses of synthetic data, but none by itself supplies a
Customer 360 benchmark dataset with omnichannel source profiles, identity truth, attribute -event
lineage, and survivorship truth.
Validation is not a single similarity score. Data-quality research distinguishes d imensions such as
completeness, accuracy, consistency, timeliness, uniqueness, and validity (Batini et al., 2009 ; Batini
& Scannapieco, 2016). Synthetic-data validation research likewise warns that marginal compari sons
alone can miss multivariate structure; divergence-based approaches seek to capture broader
distributional differences (ApellÆniz et al., 2024). The present benchmark has a different ob jective. It
does not attempt to imitate a confidential retailer distribution. It validates a declared synthetic world:
requested mechanisms must be realized as specified, references must remain consistent, truth must
cover every applicable case, and controlled conditions must change the intended evaluation
difficulty.

2.3 Data Fusion, Truth Discovery, and Survivorship
Survivorship is a form of data fusion: after records referring to the same entity have been grouped,
conflicting attribute values must be reconciled into a consistent representation. Data-fusion research
formalizes this task through conflict-resolution functions such as source precedence, recency,
voting, and source-reliability estimation (Bleiholder & Naumann, 2009). Truth- discovery methods
extend the same problem by jointly estimating source reliability and likely true values from conflicting
multi-source observations (Li et al., 2016). The four regimes evaluated here are transparent,
declared fusion rules rather than learned truth-discovery algorithms. Their methodological role i s to
create auditable expected golden-record outcomes and to measure when plausible decision rules
disagree under controlled customer-data conditions.
2.4 Computational Benchmark Design
Computational benchmarks are most useful when configurations are standardized, failures are
retained, and comparisons can be reproduced without hidden tuning. AMLB illustrates reproduci ble
benchmark governance through shared tasks, standardized execution, publicly inspectable tools,
and documented treatment of unsuccessful framework runs (Gijsbers et al., 2024). The same logic
applies here: the benchmark configuration, seeds, code version, outputs, validation status, and
analysis rules must be frozen before confirmatory execution.
2.5 Closest Prior Work and Bounded Novelty
Closest prior work spans synthetic personal and household generators, generated entity-matching
tests, census-scale population simulators, reusable person-level duplicate datasets, entity-centric
evaluation, privacy-preserving linkage generation, data-fusion and truth-discovery methods, general
relational synthesis, and retail behavior simulation. EMBench generates controlled matching tests
(Ioannou et al., 2013); entity-centric evaluation organizes reusable entity-level label ing and
performance analysis (Binette et al., 2024); SPIDER supplies a fixed person-level bench mark with
explicit duplicate lineage (Chinnappa et al., 2025; Chinnappa et al., 2026); and Roh de et al. (2025)
combine privacy-preserving linkage dataset generation with detailed result analysis. Table 1
compares these contributions against the specific evidence contract of the present benchmark. The
comparison is bounded to the reviewed sources and does not support an absolute first-of-kind claim.
Work Primary focus Identity truth Transformation
trace
Retail source
semantics
Survivorship
truth
Condition
comparison
FEBRL generator
(Christen &
Pudjijono, 2009)
Synthetic personal,
family, and
household records
with configurable
errors
Original and
duplicate
identifiers
Configured error
generation; no
attribute-event
lineage
No retail source-
profile semantics
No Generator
evaluation and
linkage tests
GeCo (Tran et al.,
2013)
Personal-record
generation and
corruption
Original/corrupted
linkage
Configured
corruption
No No Generated test
cases
EMBench
(Ioannou et al.,
2013)
Entity-matching
benchmark
generation
Yes Test-case structure No No Matching-system
comparison
Synthetic Data
Vault (Patki et al.,
2016)
Learned relational
synthesis
No task-specific
cluster truth
No injected-event
lineage
No No Fidelity/utility
oriented
RetailSynth (Xia
et al., 2023)
Retail shopping-
behavior simulation
Behavioral latent
state, not ER
clusters
Simulation state Retail behavior; not
omnichannel
identity sources
No Policy
experiments
Entity-centric
evaluation
(Binette et al.,
2024)
Reusable ER labeling
and evaluation
Yes Error-analysis
framework
No No Evaluation and
simulation studies
SPIDER v2
(Chinnappa et al.,
2025)
Person-level ER
dataset
Cluster identifiers Original record and
duplication rule
Person records; no
source-profile
architecture
No Benchmark script
and fixed dataset
Data fusion and
truth discovery
(Bleiholder &
Naumann, 2009;
Conflict resolution
and likely-value
estimation across
Assumes
resolved objects
or data items;
not ER-cluster
Source claims
and conflict
inputs; not
injected attribute-
Generic multi-
source
integration; not
retail source
Truth-
estimation
objectives,
not four
Method
taxonomies and
comparative

Work Primary focus Identity truth Transformation
trace
Retail source
semantics
Survivorship
truth
Condition
comparison
Li et al., 2016) sources benchmark truth event lineage profiles declared
customer
survivorship
regimes
evaluation
Pseudopeople
(Haddock et al.,
2024)
Census-scale
simulated population
and administrative-
style records
Ground-truth
identifiers
Configurable field-
level noise; no
event-level
before/after/cause
lineage linked to
survivorship truth
Census, survey,
and administrative
context; not retail
No Entity-resolution
development and
testing
PPRL framework
(Rohde et al.,
2025)
Privacy-preserving
linkage datasets and
analysis
Yes Record/pair
descriptive tags
Population and
household
structure; not retail
No Dataset-variation
analysis
This study Customer 360
quality, identity, and
survivorship
benchmark
Yes Attribute-event
lineage
Four omnichannel
retail source
profiles
Four declared
regimes
335 predeclared
runs
Table 1. Bounded comparison with closest prior benchmark, generation, evaluation, and conflict-resolution work. “No”
denotes that the feature is outside the cited work’s stated contribution, not a defect in that work.
The novelty is integrative and methodological rather than algorithmic. A central methodol ogical
distinction is denominator-aware survivorship evaluation: the benchmark separates truth applicability
from valid-candidate evaluability, counts the union and all six pairwise regime disagree ments, and
reports both conditional disagreement and population-level burden across four declared regimes.
Within this bounded comparison, no reviewed resource combines those measures with omnichannel
customer-source profiles, controlled customer-data defects and ambiguity, identity-cluster truth,
attribute-level transformation lineage, four golden-record survivorship regimes, and repl icated
condition-separation experiments. The present study therefore contributes a task-specific
benchmark design and executed evidence package; it does not claim a new matching algorithm, a
representative retail population, or universal precedence rules.
3. Benchmark Design
3.1 Intended Users and Evaluation Tasks
The benchmark is intended for researchers and technically competent practitioners who need
controlled customer-data conditions without using proprietary or personal data. Its initial tasks are:
entity-cluster recovery; comparison of transparent matching baselines; analysis of false merges and
false nonmatches; survivorship-rule comparison; defect and conflict sensitivity; and reproducibi lity
testing. The benchmark is deliberately small enough for manual inspection and fast reruns, wh ile its
configuration model supports larger scale experiments.
3.2 Entity Model and Source Profiles
The latent model contains persons, households, customer or loyalty accounts, contact points,
addresses, source observations, and minimal transaction or order context. Source records are
produced through four profiles that differ in authority, verification probability, and field presence.
Together, ecommerce, loyalty or mobile, physical-store transaction, and service or fulfillment
observations create the heterogeneous cross-channel inputs that omnichannel customer-data
integration must unify. Table 2 summarizes the fixed profile design used in the replicated study.
The benchmark represents omnichannel retail at the customer-record and source-integration layer.
Minimal transaction or order context anchors source observations, but the model does not simulate
product catalogs, baskets, promotions, demand, or complete customer journeys. This boundary
preserves the paper’s focus on customer data quality, identity resolution, and golden -record
survivorship rather than retail-behavior simulation.

Source profile Authority
rank
Verification
rate
Characteristic field availability Architectural role
Loyalty/mobile 1 (highest) 0.75 Name, email, and phone are
relatively rich; address is less
frequent.
Enrolled identity anchor and
verified contact source.
Ecommerce 2 0.55 Name and email are rich; address
is common; phone is moderate.
Digital account and transaction
identity.
Service/fulfillment 3 0.45 Name, phone, and address are
rich; email is moderate.
Operationally maintained
contact and delivery
observations.
Physical-store
transaction
4 (lowest) 0.10 Most person fields are sparse;
records often remain weakly
identified.
Low-signal transaction context.
Table 2. Source-profile design used to generate heterogeneous customer observations. Authority ranks and
verification rates are benchmark assumptions, not estimates of industry prevalence.
3.3 Defects, Ambiguities, Conflicts, and Structural Duplicates
The generator first assigns multiple observations to selected persons, creating true duplicate
clusters. Same-source repeats may occur through source-profile allocation, but the executed
generator does not use a separate within-source-rate control. It then applies eight auditab le
transformation mechanisms. Table 3 separates data-quality defects from ambiguity and conflict
mechanisms because their evaluation roles differ: defects degrade observations, ambiguity creates
plausible cross-entity similarity, and conflicts create competing values for survivorship.
Class Mechanism Affected content Retained truth
Structural
duplication
Multiple observations for
one person; same-source
repeats may arise through
profile allocation
Source-record allocation and cluster
size
Canonical person and duplicate-
cluster membership
Quality defect Missing value Name, email, phone, or address Original value, affected field, event,
final value
Quality defect Invalid format Email, phone, or postal code Valid source value and invalid
transformed value
Quality defect Typographical variant Name, street, or email Edit operation, prior value, and
transformed value
Quality defect Stale value Email, phone, or address Event time and current versus stale
state
Ambiguity Shared identifiers Household-shared or cross-
household email/phone
Requested and realized units,
affected persons, affected records
Ambiguity Household/person
ambiguity
Competing person and household
attribution
Group membership and affected
records
Conflict Cross-record competing-
value conflict (legacy code
C-XSR)
Name, email, phone, or address Competing observations and
record/source context
Conflict Source authority versus
recency
Email, phone, or address Older authoritative and newer lower-
authority candidates
Table 3. Benchmark transformations and their retained ground truth. The eight lineage mechanisms exclude
structural duplicate allocation, which is generated as part of the record topology.
3.4 Ground Truth and Survivorship Regimes
Ground truth is stored separately from ordinary benchmark inputs to prevent accidental leakage.
Identity truth maps every source record to a canonical person and cluster. Transformation truth
records the mechanism, affected field, before value, after value, event time, and source context.
Survivorship truth is generated for each applicable person-attribute combination under four declared
regimes. A combination is truth-applicable when at least one non-null candidat e exists; it is
evaluable when at least one candidate also passes the attribute-validity rule.
The four regimes are deliberately simple and explainable. Verification-first orders candid ates by
validity, verification, authority, and recency. Source-authority-first places authority before verification.
Recency-first places event time before verification and authority. Mixed conditional a pplies attribute-

specific rules: verification then recency for email and phone; verification then authority for address;
and authority then verification for first and last name. A deterministic source-record identi fier breaks
remaining ties. Same-rule agreement between a baseline and its generated truth is treated o nly as
an implementation-consistency check.
Figure 1 presents the complete generation and evaluation path. The design keeps source records
and ground truth connected through explicit lineage while placing them in separate outputs.

Figure 1. Benchmark generation and evaluation pipeline. Latent entities generate heterogeneous source
observations; controlled transformations create benchmark inputs and independent ground truth; transparent
baselines and validation produce auditable findings. Author-constructed from executed code.
4. Generator and Validation Method
4.1 Configuration, Seeds, and Determinism
Each run is controlled by a machine-readable configuration that records population size, so urce
profiles, duplicates, ambiguity, defects, conflicts, survivorship rules, baseline thresholds, val idation
controls, output options, reference time, and a master seed. Deterministic child seeds govern
separate generation stages. The resolved configuration is written with each run so that the executed
values, rather than a template, define the evidence.
The materialized input configurations retain a provisional 0.2.0-dev schema label, while t he runtime-
resolved configurations, manifests, and executed code identify benchmark version 0.3.1. The
resolved configuration and manifest are the authoritative records for each run. The provisional input
label is retained unchanged as part of the audit history and does not indicate mixed-code executio n.
They were preserved unchanged because they are hash-linked inputs in the execution audit trail;
regenerating them solely to update the label would break direct correspondence with the retained
run manifests.
Canonical output tables are sorted before hashing. A run manifest records the benchmark version,
Python environment, configuration hash, output hashes, counts, validation status, runtime, and peak
resident memory. Fixed seed and configuration must reproduce the same canonical hashes. A
different seed must change the data while preserving schema and integrity. These requirements
were tested before the replicated experiment and again in the confirmatory package.

4.2 Output Contract and Audit Materials
The package writes latent entity tables, ordinary source records, identity truth, defect and confl ict
lineage, survivorship truth, identity predictions, survivorship predictions, metric tables, validation
results, a resolved configuration, a manifest, and file hashes. Ground truth is excluded from ordinary
benchmark inputs by directory and file contract. The retained audit materials include cod e, software
version, configurations, seeds, run logs, failed-run records, tests, expected outcomes, and exact
result-generation commands.
4.3 Validation Levels
Validation is layered so that a plausible aggregate metric cannot hide a structural error. Sche ma
tests verify required columns and types. Referential checks verify that records resolve to existing
entities and that primary keys are unique. Domain checks verify value ranges and controlled
vocabularies. Truth checks verify complete coverage of applicable combinations, duplicate-cluster
consistency, and continuous transformation lineage. Rate checks compare requested and realized
mechanisms using declared units. Metamorphic checks confirm that parameter changes move
realized behavior in the intended direction. Baseline checks confirm that designed conditions remain
distinguishable. Reproducibility checks compare hashes and clean-environment execution.
Critical validation failures stop confirmatory execution. Failed directories are retained; they are not
silently overwritten or removed. A rerun is permitted only after a defect is identified in dependently of
the research outcome, documented, narrowly corrected, regression-tested, and followed by a
complete restart when the correction could affect generated data.
4.4 AI-Assisted Computational Support
AI-assisted tools supported development of the executable code used to generate and analyze the
synthetic benchmark. All reported data and results were produced by executing version-controlled
code under documented configurations and fixed seeds. The author defined the research questions,
benchmark design, experimental conditions, and analysis plan and reviewed and verified the
implementation, tests, outputs, analyses, and interpretation.
5. Experimental Design
5.1 Experiment Families and Pairing
The replicated design separates identity difficulty, survivorship conflict, single-factor sens itivity, and
scale characterization. This separation prevents population size, candidate availability, and record-
topology changes from being misinterpreted as difficulty effects. Table 4 summarizes the frozen
matrix.
Family Conditions Seeds Runs Controlled interpretation
E1 identity difficulty Easy, baseline, hard 40 paired 120 Persons, records, allocation, and duplicate
topology fixed within seed; defects and
ambiguity increase.
E2 survivorship
conflict
Low, medium, high 40 paired 120 Candidate availability and evaluability fixed
within seed; cross-record and authority-recency
conflict increase.
E3 single-factor
sensitivity
Missingness, typo, shared
identifiers, conflict;
low/high
10 paired per
factor
80 One factor changes per pair; findings are
descriptive expected-direction checks.
E4 scale
characterization
100, 200, 400 persons 5 per size 15 Baseline configuration fixed; runtime and
memory are descriptive only.
Table 4. Predeclared replicated experiment matrix. The confirmatory set contains 335 runs.

5.2 Identity Baselines
Three transparent identity baselines test whether the benchmark conditions are distinguishabl e.
Exact normalized matching links records sharing an exact normalized email or phone. Det erministic
rules add exact normalized name-plus-postal matching. Weighted similarity computes fiel d-level
similarity over name, email, phone, and address with weights 0.30, 0.30, 0.20, and 0.20.  Phone
similarity is exact; other fields use normalized string similarity. Pairs at or above  the threshold are
joined through transitive union-find clustering. The primary threshold is 0.85, with predeclared
robustness thresholds of 0.80 and 0.90.
These baselines are not proposed as competitive production systems. The unindexed weighted
method compares all record pairs and is intentionally simple so that condition effects remain
interpretable. The same baseline is applied to every condition and seed.
5.3 Identity and Survivorship Measures
Identity evaluation reports pairwise precision, recall, and F1; B-cubed precision, recall, and F1; t rue-
positive, false-positive, and false-negative pair counts; and predicted versus true cluster co unts.
Pairwise F1 emphasizes link errors, while B- cubed F1 evaluates each record’s overlap between its
predicted and true cluster. Reporting both limits the risk that one aggregation hides the error
structure.
Survivorship evaluation reports truth-applicability coverage, evaluable coverage, the union of
person-attribute cases where any declared regimes disagree, all six regime-pair disagreements,
conditional disagreement rate, and population-level disagreement burden. Conditional disagreement
divides union disagreement cases by evaluable cases. Population burden divides the same union by
all possible person-attribute cases. Raw counts are retained but are not compared without
denominators.
5.4 Hypotheses and Statistical Analysis
H1 states that the hard identity condition will reduce weighted-similarity pairwise F1 rel ative to the
easy condition at threshold 0.85. H2 states that high conflict will increase the conditional
survivorship-rule disagreement rate relative to low conflict. Both contrasts are paired by seed. The
analysis uses an exact one-sided sign test on non-tied differences and controls familywise error
across H1 and H2 with the Holm procedure (Holm, 1979). It reports positive, negative, and tied pairs;
median and interquartile range of paired differences; and a 95% percentile-bootstrap interval f or the
median using 10,000 resamples from a fixed analysis seed. Threshold 0.80 and 0.90 comparisons
are secondary robustness checks, not additional confirmatory hypotheses.
6. Results
6.1 Execution Integrity and Attempt History
The confirmatory execution completed 335 of 335 frozen runs under benchmark version 0.3.1. All
335 runs passed validation; no run failed, was excluded based on its result, or was selectively rerun.
The execution inventory, resolved configurations, manifests, analysis files, and hashes are retained.
An earlier execution attempt was stopped after 94 run directories because ten runs failed a critic al
defect-lineage test. The failure occurred when an authority-recency conflict could overwrite a shared-
identifier transformation without a continuous lineage endpoint. No hypothesis, aggregate, or
threshold analysis was conducted before the stop. The correction excluded already-protected fields
from that overwrite path, added a regression test using the first failing seed, and passed five un it

tests. The entire 335-run matrix was then restarted from zero with unchanged configurations, seeds,
hypotheses, metrics, and analysis rules. Table 5 records the integrity decision.
Record Observed status Research decision
Attempt 1 94 directories: 84 pass, 10 critical lineage failures Stop before aggregate outcome analysis; retain
all directories separately.
Correction Narrow candidate-selection fix; first failing seed
added as regression test; 5/5 tests pass
Version code to 0.3.1; preserve frozen
experiment design.
Confirmatory attempt 2 335/335 runs pass; one code version; complete
matrix
Use as confirmatory result set; no attempt-1
result is reused.
Invariant checks E1 topology invariant 40/40; E2 evaluable
denominator invariant 40/40
Interpret paired condition contrasts as designed.
Table 5. Execution-integrity and correction record. The stopped attempt is retained as failure evidence, not merged
with the confirmatory set.
6.2 Identity-Difficulty Results
Table 6 reports median pairwise and B-cubed F1 across the three identity conditions. Every baseline
declines as the condition becomes harder. The weighted baseline shows the largest pairwise
separation, partly because false merges create many pairwise false positives in the hard all-pai rs
setting. B-cubed values remain higher because they measure record-centered cluster overlap. Both
views are necessary for interpretation.
Condition Baseline Median pairwise
F1
Pairwise IQR Median B-cubed F1 B-cubed IQR
Easy Exact normalized 0.716 0.704–0.739 0.828 0.823–0.841
Easy Deterministic rules 0.764 0.749–0.775 0.857 0.853–0.862
Easy Weighted 0.85 0.754 0.742–0.771 0.860 0.857–0.868
Baseline Exact normalized 0.642 0.622–0.661 0.786 0.779–0.796
Baseline Deterministic rules 0.691 0.670–0.711 0.819 0.812–0.828
Baseline Weighted 0.85 0.655 0.604–0.684 0.828 0.818–0.834
Hard Exact normalized 0.386 0.372–0.398 0.650 0.644–0.661
Hard Deterministic rules 0.422 0.414–0.435 0.671 0.664–0.680
Hard Weighted 0.85 0.170 0.141–0.209 0.669 0.660–0.692
Table 6. Identity baseline results across 40 paired seeds per condition. Values summarize condition behavior; the
confirmatory H1 contrast uses the weighted baseline at 0.85.
Figure 2 shows the pairwise measure. The median weighted-similarity F1 falls from  0.754 in the
easy condition to 0.655 in the baseline condition and 0.170 in the hard condition. Exact normali zed
and deterministic baselines also decline, which indicates that the manipulation is not specific to the
weighted method.

Figure 2. Median pairwise F1 across identity-difficulty conditions for three transparent baselines. Author-constructed
from the 335-run result set.
Figure 3 shows the structural companion measure. Median weighted B-cubed F1 falls from  0.860 to
0.828 to 0.669 across the same conditions. The smaller numerical decline does not contradict the
pairwise result; it reflects the different error aggregation of record-centered cluster evaluation.

Figure 3. Median B-cubed F1 across identity-difficulty conditions. B-cubed is reported alongside pairwise F1 to
expose cluster structure without treating either metric as complete. Author-constructed from executed results.

6.3 Primary Identity Contrast and Threshold Robustness
For H1, easy-condition weighted-similarity pairwise F1 exceeded hard-condition F1 in 40 of  40
paired seeds, with no negative or tied differences. The median easy-minus-hard difference w as
0.5846, with an interquartile range of 0.5396–0.6054 and a bootstrap 95% interval of 0.5653–0.5899.
The exact one-sided p value was 9.09 × 10⁻„‡; the Holm-adjusted p value was 1.82 × 10⁻„†.
Table 7 shows that the predeclared direction holds at all three thresholds. This supports a condition-
separation claim rather than a claim that 0.85 is an optimal operational threshold.
Threshold Role Favorable pairs Median easy–hard difference Bootstrap 95% interval
0.80 secondary robustness 40/40 0.4404 0.4183–0.4565
0.85 primary 40/40 0.5846 0.5653–0.5899
0.90 secondary robustness 40/40 0.5763 0.5505–0.5900
Table 7. Weighted-similarity threshold robustness. Threshold 0.85 is primary; 0.80 and 0.90 are predeclared
secondary checks.
6.4 Survivorship-Conflict Results
Truth-applicability and evaluable coverage are identical across low, medium, and high conflict wi thin
every paired seed. Conflict injection therefore changes the competing values without changing the
candidate denominator. Table 8 reports median union disagreement counts and both denominator-
aware rates.
Conflict condition Applicability Evaluability Union cases Conditional
disagreement
Population burden
Low 79.3% 79.3% 6 0.76% 0.60%
Medium 79.3% 79.3% 28 3.58% 2.80%
High 79.3% 79.3% 52 6.56% 5.20%
Table 8. Survivorship disagreement across 40 paired seeds per condition. Union cases count each person-attribute
case once when at least two of the four regimes select different values. Each column reports its own median across
seeds; therefore, a median rate is not expected to equal the ratio of the reported median numerator and median
denominator.
Figure 4 shows the conditional disagreement rate. The median rises from 0.76% under low conflict
to 3.58% under medium conflict and 6.56% under high conflict.

Figure 4. Median conditional disagreement rate across survivorship-conflict conditions. The evaluable denominator is
invariant within each paired seed. Author-constructed from executed results.
For H2, high-conflict conditional disagreement exceeded low-conflict disagreement in 40 of 40 paired
seeds, with no negative or tied differences. The median paired increase was 0.0577, or
approximately 5.77 percentage points. The bootstrap 95% interval was 0.0555 –0.0625; the Holm-
adjusted one-sided p value was 1.82 × 10 ⁻„†. The result shows that the benchmark can create
controlled rule-disagreement conditions. It does not identify a universally correct survivorship policy.
6.5 Sensitivity and Scale Characterization
The single-factor sensitivity experiment is descriptive and lies outside the H1-H2 confirmatory family.
Each elevated factor increased its intended realized mechanism measure in all ten paired seeds.
Table 9 reports the median high-minus-low realized difference. The values are generator-beh avior
checks, not estimates of prevalence.
Factor Realized measure Expected-direction
pairs
Median high–low
difference
Missing realized D-MISS events 10/10 526.0
Typo realized D-TYPO events 10/10 274.5
Conflict realized cross-record competing-value events
(legacy C-XSR code)
10/10 65.0
Shared Identifiers realized declared A-SHARED units 10/10 31.5
Table 9. Single-factor expected-direction results for configurations with 200 persons and approximately 600 source
records per run. No inferential claim is made for these ten-seed sensitivity checks.
Scale characterization used the baseline configuration and changed only the number of persons.
Median runtime was 1.03 seconds at 100 persons, 4.01 seconds at 200 persons, and 16.49 seconds
at 400 persons. Figure 5 shows the steep increase expected from an unindexed all-pairs
comparison. Median peak resident set size ranged from approximately 99 to 105 MiB, equival ent to
approximately 104 to 110 MB, across the tested sizes. These measurements characterize execution
at the tested sizes; reproducibility is supported separately by fixed-seed, configuration-hash, and
clean-environment checks.

Figure 5. Median runtime by population size for the disclosed unindexed implementation. Five seeds were executed
per size. Author-constructed from executed results.
7. Discussion
7.1 Benchmark and Resource-Method Contribution
The study demonstrates that a synthetic Customer 360 artifact can be evaluated as a benchmark
rather than presented as a generator alone. Its novelty is integrative and methodological rather than
algorithmic: it joins a justified entity and omnichannel-source model; controlled data-qual ity,
ambiguity, and conflict mechanisms; separate identity, data-lineage, and survivorship truth;
transparent baselines; reproducibility controls; and executed evidence showing condition separation.
Its most distinctive evaluation contribution is the denominator-aware survivorship de sign, which
distinguishes unavailable or invalid candidate surfaces from disagreement among rules that can
actually make a decision. The output is useful because users can inspect why a record or attribute is
difficult, not only observe that a baseline score changed.
The H1 result establishes identity-condition distinguishability across multiple base lines and across
three weighted thresholds. Reporting B-cubed with pairwise F1 clarifies why the absolute wei ghted
pairwise result becomes low under hard all-pairs conditions: large false-merge clusters create m any
incorrect pairs, while record-centered cluster overlap remains materially higher. The benchmark i s
therefore not judged by a single headline score. Its role is to expose method behavior under
controlled, auditable conditions.
The H2 result establishes survivorship-condition distinguishability without a moving candidate
denominator. The benchmark separates truth applicability, valid-candidate evaluability, r ule
disagreement among evaluable cases, and population-level burden. It also reports the union of all
regime disagreements and every named regime-pair disagreement. This distinction is important f or
customer-data architecture because a low raw disagreement count can arise either because rules
agree or because few attributes are available or valid enough to evaluate. A benchmark that retai ns
each denominator and disagreement surface supports more precise interpretation.

7.2 Implications for Customer Data Quality and Unification Architecture
The benchmark connects three decision layers that are often evaluated separately. First, customer
data quality controls affect whether identity signals exist and whether they remain valid. Second,
identity resolution determines which observations may be consolidated through data integration.
Third, survivorship rules determine which competing values become the golden record in master
data management and Customer 360 pipelines. Errors at one layer change the evidence available to
the next. The generated data lineage makes those dependencies explicit.
For data architects and data engineering teams, the source-profile model provides a design-time
way to test whether rules depend too heavily on a rich digital source and fail when physical- store or
fulfillment observations are sparse. For identity-resolution researchers, controlled shared ident ifiers
and household ambiguity expose false-merge conditions that exact identifiers can create. For master
data management and Customer 360 teams, the four survivorship regimes demonstrate that
verification, authority, and recency can produce different outputs even when all candidates are valid.
The mixed regime shows how attribute-specific precedence can be encoded and audited without
claiming that its ordering is universally preferable.
The benchmark can also support contract and pipeline testing. Because each transformation has an
expected attribute, event, and lineage endpoint, a pipeline can be checked for whether it preserves
identity truth, records the cause of change, and applies a declared precedence order. Those uses
require organizational calibration before operational adoption; the current results establish only
reference behavior under synthetic conditions.
7.3 Limitations and Failure Cases
Nine limitations bound the findings. First, the records are synthetic and are not learned from ,
calibrated to, or representative of a retail population. Second, source-profile authority, veri fication,
field presence, and defect rates are design assumptions. Third, the retail scope is limi ted to the
customer-record and source-integration layer: minimal transaction or order context does not model
product catalogs, baskets, promotions, demand, complete customer journeys, or broader retail
behavior. Fourth, the identity baselines are transparent demonstrations rather than state-of-t he-art
comparisons. Fifth, the unindexed weighted baseline has quadratic pair comparison and is not a
production architecture. Sixth, paired seeds characterize stability within the declared generator and
do not support statistical inference about organizations. Seventh, independent third-party
reproduction has not yet been completed. Eighth, the executed generator does not implement a
distinct within-source-rate parameter; same-source repeats arise only through source-profile
allocation. Ninth, the legacy identifier C-XSR denotes a cross-record competing-valu e mechanism
and does not guarantee that every selected pair comes from different source profiles.
The stopped first attempt is an additional implementation lesson. A generator can pass schema and
aggregate checks while carrying a subtle lineage inconsistency. Retaining the failed attempt ,
blocking analysis, and restarting the full matrix after a narrow correction reduced the risk of reporting
results from internally inconsistent evidence. Future versions should preserve regression tests for
every discovered failure and should add adversarial configurations that intentionally combine
transformations at the same attribute.
7.4 Reproducibility and Public-Release Boundary
The author retains code v0.3.1, configurations, fixed seeds, environment records, manifests, hashes,
validation outputs, run logs, analysis scripts, raw and aggregate results, the stopped-attempt
inventory, and exact recreation commands. The complete raw output corpus is substantially larger
than the compact review package and remains archived separately.

Public deposit is deferred pending final repository preparation, citation metadata, final rel ease-
package verification, and review of the selected venue’s software and data policies. The select ed
software and data/documentation licenses are included in the release candidate. The study does not
use employer data, proprietary schemas or code, operational thresholds or metrics, or confidential
system designs. Public release will remain paused if any ownership or disclosure uncertainty arises.
8. Conclusion
This paper presents a synthetic Customer 360 benchmark and generation method for customer data
quality, identity resolution, and survivorship evaluation in omnichannel retail. The bench mark joins
heterogeneous source profiles, controlled defects and ambiguities, exact identity clusters, attribut e-
level data lineage, four regime-specific survivorship outcomes, and denominator-aware
disagreement measures in one auditable design.
The 335-run confirmatory study shows that the benchmark creates stable and meaningfully dif ferent
evaluation conditions. Identity performance declined from easy to hard conditions in all 40 paired
seeds for the primary weighted baseline, with the direction preserved across three predeclared
thresholds and supported by pairwise and B-cubed evidence. Survivorship-rule disagreement
increased from low to high conflict in all 40 paired seeds while the evaluable denominator re mained
fixed. Single-factor and scale experiments further demonstrated expected generator behavior and
bounded computational reproducibility.
The contribution is a benchmark/resource-method study with executed findings, not a claim of
representative retail data or field-validated effectiveness. Its value lies in controlled ground truth,
transparent assumptions, retained failures, and reproducible analysis. The next steps are
independent reproduction, release and licensing review, and evaluation with additional matchin g
methods and calibrated public conditions where suitable data become available.
Statements and Declarations
Competing Interests. The author declares no competing interests.
Funding. No funding was received for conducting this study.
Data Availability. The study generated and analyzed synthetic data only. The full reproducibility
corpus is retained by the author. Public availability is planned after repository preparation and final
release-package verification.
Code Availability. Versioned Python source code, configurations, seeds, tests, manifests, hashes,
logs, and analysis scripts are retained. Public release is planned after repository preparation an d
final release-package verification.
Ethics Approval.  Not applicable. The study did not involve human participants, personal data,
animals, or biological materials.
Consent to Participate. Not applicable.
Author Contributions. Pradeep Aronkar is the sole author and was responsible for the research
questions, scope, benchmark design decisions, execution verification, interpretation, citation
verification, and final manuscript accountability.
Use of AI-Assisted Tools.  AI-assisted tools were used during preparation of this work to support
development of the executable code used to generate and analyze the disclosed synthetic
benchmark and to improve grammar, readability, formatting, style, and consistency. The author
supplied and controlled the research problem, benchmark design, experimental conditions,

interpretation, and conclusions. The author reviewed and verified the implementation, synthetic data,
analyses, citations, tables, figures, and final manuscript and accepts full responsibilit y for the
accuracy, originality, and integrity of the work. No AI tool is listed as an author, and no generative-AI
photographic, illustrative, or pictorial image was used.
References
Amigó, E., Gonzalo, J., Artiles, J., & Verdejo, F. (2009). A comparison of extrinsic clustering evaluation metrics based on formal
constraints. Information Retrieval, 12(4), 461–486. https://doi.org/10.1007/s10791-008-9066-8
ApellÆniz, P. A., JimØnez, A., Arroyo Galende, B., Parras, J., & Zazo, S. (2024). Synthetic tabular data validation: A divergence-
based approach. IEEE Access, 12, 103895–103907. https://doi.org/10.1109/ACCESS.2024.3434582
Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. ACM
Computing Surveys, 41(3), Article 16, 1–52. https://doi.org/10.1145/1541880.1541883
Batini, C., & Scannapieco, M. (2016). Data and Information Quality: Dimensions, Principles and Techniques. Springer.
https://doi.org/10.1007/978-3-319-24106-7
Bleiholder, J., & Naumann, F. (2009). Data fusion. ACM Computing Surveys, 41(1), Article 1, 1–41.
https://doi.org/10.1145/1456650.1456651
Binette, O., & Steorts, R. C. (2022). (Almost) all of entity resolution. Science Advances, 8(12), eabi8021.
https://doi.org/10.1126/sciadv.abi8021
Binette, O., Baek, Y., Engineer, S., Jones, C., Dasylva, A., & Reiter, J. P. (2024). How to evaluate entity resolution systems: An
entity-centric framework with application to inventor name disambiguation. arXiv:2404.05622. https://arxiv.org/abs/2404.05622
Chinnappa, P., Arokiya Dass, R. M., & Mathur, Y. (2025). SPIDER (v2): Synthetic Person Information Dataset for Entity Resolution
(Version 2) [Data set]. figshare. https://doi.org/10.6084/m9.figshare.30472712
Chinnappa, P., Mathur, Y., & Arokiya Dass, R. M. (2026). Descriptor: Synthetic Person Information Dataset for Entity Resolution
(SPIDER). IEEE Data Descriptions, 3, 121–131. https://doi.org/10.1109/IEEEDATA.2026.3663349
Christen, P. (2012). Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection.
Springer. https://doi.org/10.1007/978-3-642-31164-2
Christen, P., & Pudjijono, A. (2009). Accurate synthetic generation of realistic personal information. In T. Theeramunkong, B.
Kijsirikul, N. Cercone, & T.-B. Ho (Eds.), Advances in Knowledge Discovery and Data Mining (Lecture Notes in Computer
Science, Vol. 5476, pp. 507–514). Springer. https://doi.org/10.1007/978-3-642-01307-2_47
Fellegi, I. P., & Sunter, A. B. (1969). A theory for record linkage. Journal of the American Statistical Association, 64(328), 1183–
1210. https://doi.org/10.1080/01621459.1969.10501049
Gijsbers, P., Bueno, M. L. P., Coors, S., LeDell, E., Poirier, S., Thomas, J., Bischl, B., & Vanschoren, J. (2024). AMLB: An AutoML
benchmark. Journal of Machine Learning Research, 25(101), 1–65.
Haddock, B., Pletcher, A., Blair-Stahn, N., Keyes, O., Kappel, M., Bachmeier, S., et al. (2024). Simulated data for census-scale
entity resolution research without privacy restrictions: A large-scale dataset generated by individual-based modeling. Gates
Open Research, 8, 36. https://doi.org/10.12688/gatesopenres.15418.2
Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70.
Ioannou, E., Rassadko, N., & Velegrakis, Y. (2013). On generating benchmark data for entity matching. Journal on Data Semantics,
2, 37–56. https://doi.org/10.1007/s13740-012-0015-8
Li, Y., Gao, J., Meng, C., Li, Q., Su, L., Zhao, B., Fan, W., & Han, J. (2016). A survey on truth discovery. ACM SIGKDD Explorations
Newsletter, 17(2), 1–16. https://doi.org/10.1145/2897350.2897352
Menestrina, D., Whang, S. E., & Garcia-Molina, H. (2010). Evaluating entity resolution results. Proceedings of the VLDB
Endowment, 3(1–2), 208–219. https://doi.org/10.14778/1920841.1920871
Patki, N., Wedge, R., & Veeramachaneni, K. (2016). The Synthetic Data Vault. In 2016 IEEE International Conference on Data
Science and Advanced Analytics (DSAA) (pp. 399–410). IEEE. https://doi.org/10.1109/DSAA.2016.49
Rohde, F., Christen, V., & Rahm, E. (2025). Exploring privacy-preserving record linkage: A holistic framework for dataset generation
and detailed result analysis. Proceedings of the 14th International Workshop on Quality in Databases (QDB’25).
https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/QDB/QDB25_2.pdf
Schram, R., Spithorst, S., & van Kesteren, E.-J. (2025). Metasyn: Transparent generation of synthetic tabular data with privacy
guarantees. Journal of Open Source Software, 10(105), 7099. https://doi.org/10.21105/joss.07099
Shahbazi, N., Danevski, N., Nargesian, F., Asudeh, A., & Srivastava, D. (2023). Through the fairness lens: Experimental analysis
and evaluation of entity matching. Proceedings of the VLDB Endowment, 16(11), 3279–3292.
https://doi.org/10.14778/3611479.3611525
Tran, K.-N., Vatsalan, D., & Christen, P. (2013). GeCo: An online personal data generator and corruptor. In Proceedings of the 22nd
ACM International Conference on Information and Knowledge Management (pp. 2473–2476). ACM.
https://doi.org/10.1145/2505515.2508207
Xia, Y., Arian, A., Narayanamoorthy, S., & Mabry, J. (2023). RetailSynth: Synthetic data generation for retail AI systems evaluation.
arXiv:2312.14095. https://arxiv.org/abs/2312.14095
Zeakis, A., Papadakis, G., Skoutas, D., & Koubarakis, M. (2023). Pre-trained embeddings for entity resolution: An experimental
analysis. Proceedings of the VLDB Endowment, 16(9), 2225–2238. https://doi.org/10.14778/3598581.3598594
