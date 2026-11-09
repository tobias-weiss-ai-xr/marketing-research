---
title: Recovering Business Rules as Cascade Lookups for Enterprise Field Prediction
url: https://doi.org/10.1007/978-3-032-37682-4_6
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: Lecture notes in computer science
authors:
- Changxu Duan
source: openalex-oa
pdf_url: https://arxiv.org/pdf/2610.34258
pages: 18
chars: 48888
fetched_at: '2026-11-08T20:03:27+00:00'
kb_version: 1
---

# Recovering Business Rules as Cascade Lookups for Enterprise Field Prediction

Recovering Business Rules as Cascade Lookups
for Enterprise Field Prediction
Changxu Duan () [0000−0003−0547−0901]
Technische Universität Darmstadt
Darmstadt, Germany
duan@linglit.tu-darmstadt.de
Abstract.Enterprise sales-order systems rely on manually maintained
configuration rules to determine fields such as payment terms, shipping
points, and sales ownership. When these rules are incomplete or stale,
operators must enter values by hand, and downstream errors spread into
billing, logistics, and reporting. This paper studies whether missing or
outdated rules can be recovered from historical transactions instead of
beingrelearnedasopaquestatisticalpatterns.Weintroduceaknowledge-
graph-guided workflow in which an LLM agent proposes candidate busi-
ness keys, meaning column combinations such as customer and document
type, validates them through SQL profiling, and compiles the resulting
evidence into deterministic cascade lookups. The LLM is used only dur-
ing offline rule discovery. At inference time, prediction is a transparent
key lookup with no model-serving requirement. Experiments on enter-
prise sales-order prediction and public relational benchmarks show that
cascades are most effective when fields follow stable business rules, while
learnedgraphmodelsremainpreferablewhenpredictiondependsontem-
poral or neighborhood patterns. Drift analysis further turns residual er-
rors into diagnostics for configuration maintenance.
Keywords:Enterprise AI·Knowledge Graphs·Relational prediction
·ERP systems·LLM agents
Code and data.https://github.com/Fireblossom/CascadER
1 Introduction
Enterprise Resource Planning (ERP) systems orchestrate business operations,
spanning procurement, manufacturing, sales, and finance, by maintaining a uni-
fiedtransactionaldatabaseacrossorganizationalfunctions.Inasales-orderwork-
flow, the system must fill business fields before an order can be billed, shipped,
and reported. These fields include payment terms that determine invoice due
dates, shipping points that identify the warehouse or dispatch location, In-
coterms that allocate shipping cost and risk, and sales ownership fields that
assign the responsible sales team. These values are not arbitrary labels. In well-
configured ERP systems, they are determined by business rules over customers,
arXiv:2610.34258v1  [cs.LG]  25 Oct 2026

2 C. Duan
materials, document types, and organizational units such as sales offices, sales
groups, and plants.
SAP, the dominant ERP vendor serving over 400,000 customers worldwide,
implementssuchfield-leveldeterminationthroughitsConditionTechnique,SAP’s
rule mechanism for assigning default field values from ordered lookup tables
called Access Sequences [13,14]. Each table is keyed by a combination of busi-
ness attributes such as customer, material, and organizational context. However,
these Access Sequences must be manually configured and maintained by domain
experts. When configurations are incomplete, outdated after system migrations,
or invalidated by organizational restructuring, the system either leaves fields
blank or applies coarse defaults, forcing sales representatives to select values
manually [8].
This configuration gap has tangible business consequences. An incorrect ship-
ping point routes goods from the wrong warehouse and causes fulfillment delays.
Mismatched payment terms create billing disputes. Wrong Incoterms misallocate
shipping risk between buyer and seller, and inaccurate sales group assignments
distort commission calculations. Systematic reviews of enterprise and manufac-
turing data ecosystems confirm that such data quality defects are a persistent
and costly problem [2,19]. Furthermore, these errors are not static because even
well-configured rules degrade over time as organizations restructure and cus-
tomer relationships evolve. On the SALT-KG benchmark [15], which captures
2.3M historical order items from a single SAP S/4HANA ERP system instance,
between 17% and 44% of customers changed their most frequently assigned field
value within a two-year window, depending on the field (Section 4.5). Because
each affected customer generates many orders, stale defaults can propagate er-
rors across thousands of transactions before anyone notices.
A prediction system that suggests correct field values during order entry
would reduce the need for manual correction, catch configuration drift before
it propagates, and provide configuration owners with continuous visibility into
which rules are still valid and which have silently broken. Here, configuration
drift means that a formerly valid default no longer matches current business as-
signments because contracts, organizational responsibilities, or logistics settings
have changed. We focus on cascade lookups as a practical representation for such
suggestions. A cascade lookup is an ordered list of lookup tables, from specific
rules to general fallbacks. For example, the system may first try a customer-by-
document-type rule, then a customer-only rule, and finally a global default.
Existing approaches treat field prediction as a standard supervised learning
problem, but each family of methods encounters a characteristic barrier when
applied to rule-governed enterprise data. Gradient-boosted ensembles [1,18,4]
perform well on fields with few possible values but struggle on high-cardinality
targets whose correct value depends on specific multi-column business rules
rather than broad feature correlations. For example, on the SALT-KG bench-
mark, predicting which internal sales team handles an account (589 possible
teams) requires knowing the exact combination of customer and organizational
unit that the company’s assignment policy prescribes, and the best tree-based

Business Rule Cascades for Field Prediction 3
model achieves only 51% MRR on this field. Heterogeneous GNNs [7,20] learn re-
lational embeddings by propagating signals along primary-foreign key edges, yet
they too fail on fields where the correct value is determined by a specific lookup
rule rather than by neighborhood similarity. On SALT-KG, a GNN achieves only
15.8%accuracyonsalesteamassignmentand37.5%oncustomerpaymentterms.
KG-enhanced embeddings [15] inject domain metadata as auxiliary features, but
yield only modest accuracy gains (<2 percentage points) when limited to field
definitions without encoding the determination rules themselves. The common
limitation is that these methods model the problem as statistical pattern recogni-
tion, while the underlying signal is often configured determinism. By configured
determinism, we mean that field values follow explicit lookup rules keyed by
specific combinations of customer, document type, material, and organizational
unit.
DirectlyusingLLMsatinferencetimeisalsoimpractical.Evenwithretrieval-
augmented approaches, per-order LLM calls introduce latency and cost incom-
patible with high-throughput transactional systems, and enterprise deployments
require that identical inputs always produce identical outputs with full audit
trails, a guarantee that stochastic generation cannot provide.
Our key observation is that configured rules, even when missing from the live
system, leave recoverable traces in historical transaction data. The challenge is
that the space of possible key combinations is combinatorially large, making
exhaustive search difficult, while identifying which combinations carry business
meaning requires domain knowledge that is not encoded in table schemas alone.
We address this by using an LLM agent guided by a Knowledge Graph [15] that
provides field-level descriptions and dependency hints derived from SAP’s inter-
nal ontology. The KG helps prioritize semantically meaningful key combinations,
while SQL profiling against the full transaction history validates each candidate
rule with coverage and accuracy statistics. The output is a set of deterministic
JSON lookup cascades that require no GPU or LLM at inference time, provide
built-in interpretability, and can be rebuilt as configurations change.
This paper makes three contributions.
1. A KG-guided rule discovery workflow in which an LLM proposes candidate
business keys, profiles them via SQL, and codifies the selected rules as hierar-
chical cascade lookups, achieving the best results among evaluated baselines
on all 8 SALT-KG fields.
2. A generalization study on two public RelBench v2 datasets (rel-arxiv, rel-
stack)thatcharacterizeswhencascadesmatchorunderperformGNNs,show-
ing that the method’s advantage is specific to domains with stable, recover-
able rules.
3. A drift root-cause analysis linking many residual errors to organizational
restructuring and showing how cascade failures can support configuration
maintenance.
Application setting.An SAP sales order consists of a header and one or more
line items. The header stores order-wide attributes, while each line item stores

4 C. Duan
T able 1.Target field classification. Header-level fields apply to the entire order. Item-
level fields are set per product line. Downstream consequence describes the operational
impact of an incorrect value.
Field Level Downstream consequence of error
CustomerPaymentTermsHeader Incorrect invoice due dates and early/late
payment disputes
SalesGroupHeader Misattributed revenue reporting and in-
correct commission assignment
SalesOfficeHeader Distorted regional sales analytics
HeaderIncotermsHeader Wrong allocation of shipping risk and
cost between buyer and seller
ShippingConditionHeader Suboptimal carrier selection and delivery
delays
ItemIncotermsItem Per-line risk allocation inconsistent with
contract
ShippingPointItem Goods dispatched from wrong warehouse
and fulfillment delay
PlantItem Wrongproductionorsourcingsiteandin-
ventory discrepancy
product-specific attributes for one ordered product. The 8 target fields in SALT-
KG span both levels (Table 1). Our system targets cases where configured Access
Sequences fail to resolve a value. The cascade lookup provides an editable sugges-
tion based on statistically recovered rules, with cascade-level provenance visible
to the operator.
2 Related Work
Relational deep learning.RelBench [20] established standardized benchmarks
for prediction on multi-table relational databases, proposing heterogeneous GNN
baselines that construct message-passing graphs from primary and foreign key
relationships. RelBench v2 [6] extends this with autocomplete tasks, temporal
splits, and stronger GNN/LightGBM baselines. Our method differs fundamen-
tally because instead of learning node embeddings via gradient descent, we gen-
erate deterministic lookup tables guided by domain knowledge.
Knowledge graphs for structured prediction.KGs have been used to inject do-
main semantics into ML pipelines, e.g., as entity embeddings [22], relation-aware
features,orconstraintlayers.RecentvisionsincreasinglyemphasizeunifyingKGs
with LLMs to enable synergistic reasoning [16]. In enterprise settings, ontologies
can describe business concepts and determination dependencies [14]. Our ap-
proach uses the KG as a search guide rather than as an embedding source. The
LLM uses KG-provided descriptions to propose SQL profiling candidates, while
accepted rules are selected by deterministic validation.

Business Rule Cascades for Field Prediction 5
LLM-based code generation for data tasks.Recent work applies LLMs as au-
tonomous data analysts, generating SQL queries [17,5], reasoning directly over
tabular data [24], writing feature engineering code, and performing iterative
data exploration [10]. ReAct [23] demonstrated that interleaving reasoning traces
with actions improves task grounding. Our method builds on this paradigm but
targets a specific outcome, namely the systematic discovery and codification
of deterministic business rules into deployable prediction cascades rather than
general-purpose analysis.
Tabular foundation models.TabPFN [9] introduced in-context learning for tab-
ular prediction, achieving strong results on small-to-medium datasets without
task-specific training. ConTextTab [21] extends this paradigm with semantic
embeddings from pretrained language models. However, both architectures face
scalability constraints that preclude direct application to enterprise transaction
data. TabPFN’s in-context mechanism is designed for datasets with up to tens
of thousands of samples, while ConTextTab requires 80GB GPU memory with
a context window of 8,192 rows and bagging for larger tables. SALT-KG’s 2.3M
rows and targets with up to 589 classes fall outside these operating regimes.
Our cascade approach sidesteps these limitations. Rule discovery uses an LLM
offline, and the resulting JSON lookups require no model serving at inference
time.
Enterprise field prediction.The SALT benchmark [13] introduced the task of
predicting SAP sales order fields with tree-based and GNN baselines. SALT-
KG [15] extended it with a metadata Knowledge Graph extracted from SAP’s
internal ontology via curated SPARQL queries, showing that KG-derived em-
beddings yield modest MRR improvements. The FMSLT vision [14] argues that
enterprise prediction should integrate declarative knowledge, such as ontologies,
with procedural knowledge, such as determination procedures. Our approach
operationalizes part of the declarative layer through KG-guided SQL profiling,
while the drift analysis shows where transaction history alone cannot capture
later procedural or organizational changes.
3 Method
3.1 Problem Formulation
We consider a temporal relational autocomplete task. For a target fieldf, each
historical transactionicontains an input tuplex i, a timestampti, and a target
valuey i ∈ Yf. Training records satisfyt i < T, and evaluation records satisfy
ti ≥T, whereTis the temporal cutoff. The task is to predicty i from the fields
available at order-entry time.
A composite keyK= (c1, . . . , cd)selects a small set of input columns. For a
recordi,x i[K]denotes the corresponding key value. A lookup table forKmaps
each observed key valuekto target values ranked by their empirical frequency
among training records withxi[K] =k, subject to a minimum support threshold.

6 C. Duan
Ofﬂine Rule Discovery
Step 1: Read KG
"the loading group, the plant and the
shipping condition determine
the shipping point"
ShippingPoint →  f(Plant, SC, LG)
KG determines which ﬁelds to test
Step 2: SQL Proﬁling
GROUP BY Plant, ShippingCondition
→  59 composite keys, 98.6% MRR
GROUP BY Plant
→  12 keys, 97.2% MRR
SQL validates KG-suggested keys
Step 3: Codify as JSON Cascade
L0: (Plant, SC) → 59 keys [98.6%]
L1: (Plant) → 12 keys [97.2%]
L2: global MODE → 1 key [fallback]
No LLM at inference time
Static lookup
Runtime Deployment (per order, <1 ms)
New Sales Order
Customer, Material, SalesOrg, ...
Cascade Key Lookup
L0 match? →  use it
L0 miss →  try L1 →  L2
Editable Default
ShippingPoint = 0300
matched at Plant × SC level
with cascade-level provenance
Drift Monitoring (periodic batch)
Current Transactions
new orders since last cascade build
Compare vs. Cascade
Measure per-key accuracy drift
Detect co-drift patterns
Governance Alert
Plant reassignment detected →
review ShippingPoint conﬁg (95% co-drift)
triggers
re-discovery
Fig. 1.System overview. The top panel shows offline rule discovery producing JSON
cascade files. The middle panel shows runtime key lookup providing editable sugges-
tions during order entry. The bottom panel shows drift monitoring comparing current
transactions against cascade mappings and surfacing alerts for governance review.
A cascade is an ordered list of lookup tables, from more specific keys to more
general fallbacks. At inference time, the system first tries the most specific key.
If no matching entry exists, it falls back to the next level, and eventually to the
global target distribution. The objective is to choose a short cascade that gives
accurate, high-coverage, temporally valid, and auditable predictions.
Figure 1 provides an overview of the end-to-end workflow, from offline rule
discovery through runtime deployment.
3.2 Rule Discovery (Explore)
For each target fieldf, the LLM operates as a rule discovery agent in an iter-
ative propose, profile, score, and refine loop inspired by ReAct [23]. The agent
consumes, as a read-only input, the metadata Knowledge Graph published by
SALT-KG [15], which was constructed by the SALT-KG authors through cu-
rated SPARQL queries against SAP’s internal ontology. These queries are used
as published and were not authored or modified for this work. At each iteration
the agent maintains a state consisting of (i) semantic hints extracted from the
KG’s natural-language descriptions offand its related entities, (ii) a set of can-
didate composite keys under consideration, (iii) SQL profiling evidence such as
coverage, purity, and support counts, and (iv) validation accuracy and residual
error buckets for the current cascade. SQL profiling refers to grouped aggregate
queries that estimate how often a candidate key is observed and how consistently
it maps to a single target value.
The agent’s action space consists of four operations.Proposeadds a new
candidate key from KG hints or error analysis.Profileevaluates the candidate
via SQL aggregation against temporally valid training data.Scoreranks the

Business Rule Cascades for Field Prediction 7
Algorithm 1:KG-Guided Cascade Discovery
Input:Target fieldf, KG descriptionsG f, training tablesDtrain, validation
splitD val, improvement thresholdϵ, minimum supportm, maximum
depthL max
Output:Ordered cascade(K 1, . . . , KL)
H ←extract semantic hints fromGf;
F ←initialize candidate frontier fromH;
cascade←[ ];
repeat
foreachcandidate keyK∈ Fdo
mappingK ←
SQL: GROUP BYK, f; COUNT(*) and rankfby frequencyon
Dtrain where support≥m;
accK ,cov K ←evaluate mapping K onD val;
K ∗ ←arg maxK accK among candidates with covK >0;
ifacc K∗ −acc current > ϵthen
AppendK ∗ to cascade;
Analyze residual errors→updateFwith error-driven candidates;
untilno candidate improves validation accuracy by> ϵor|cascade| ≥Lmax;
Append global target distribution as final level;
returncascade
candidate by validation accuracy, coverage, and minimum support.Refineup-
dates the cascade by appending, reordering, or pruning levels. Throughout this
paper,MODE(·)denotes the most frequent value within each group. The key
property is that the output of this loop is a deterministic lookup artifact, not a
learned model. The LLM is used only during the offline discovery phase and is
not needed at prediction time.
Candidate generation policy.Candidate keys are drawn from two sources.
The first source is entities and attributes explicitly mentioned in the SALT-
KG-provided description of fieldf, such as the KG record thatShippingPoint
depends on plant, shipping condition, and loading group. The second source is
error-driven refinements, where the agent inspects which input features distin-
guish correctly predicted rows from errors and proposes additional key columns
accordingly. Candidates are evaluated as single-entity keys, KG-suggested pair-
wise keys, or higher-order composites. The agent escalates to higher-order keys
only when the accuracy gain exceeds a thresholdϵ.
The loop terminates when (i) no candidate improves validation accuracy by
more thanϵ, (ii) candidate support falls belowm, or (iii) the maximum cascade
depthL max is reached. In practice, cascades converge within 3 to 5 iterations
per field.
Example trace forCustomerP a ymentTerms.The SALT-KG-provided
description of this field says that the system defaults to the key specified in
the customer or vendor master record, which is the central ERP record for a
business partner, while users can still enter a key during document entry. The

8 C. Duan
agent interprets this as evidence that (1) the customer identity is the primary
determinant, and (2) the document type may override the default. The following
compressed trace shows one complete run of Algorithm 1.
1. The KG hint points to defaults from the customer master. The agent queries
GROUP BY SoldToParty. The result is 80.0% accuracy with 10K keys, so the
key is retained as fallback levelL1.
2. The KG hint indicates that document type may override the default. The
agent queriesGROUP BY SoldToParty, SalesDocType. The result is 82.9%
accuracy with 69K keys and 95.3% coverage, so the key is promoted toL0.
3. Error analysis suggests broader organizational keys. The agent queriesGROUP
BY SalesOrg, DocType. The gain is belowϵ, so the key is rejected.
4. The coverage check shows that uncovered rows remain. The agent appends
the global target distribution and finalizes the cascade.
WithoutKGguidance,aminimalentity-levelbaselinewouldtryonlyper-customer
MODE,achieving80.0%(seeablation,Section4.3).TheKGhintaboutdocument-
type override directly leads to the composite key that yields+2.9%.
3.3 Cascade Codification (Build)
A finalized cascade for fieldfis a sequence of levels(K 1, . . . , KL), where each
Kl is a composite key. For each level we extract an empirical ranked list.
mapping[l][k] = [(y1, n1),(y 2, n2), . . .], n1 ≥n 2 ≥ · · ·,
wheren j isthetrainingsupportoftargetvaluey j underkeyvaluek,andthetotal
support forkmust exceed min_support l. The top-ranked valuey1 is the statis-
tical mode and is used for top-1 accuracy, while the full ranked list is used for
MRR. At prediction time, levels are queried in order, and the first match returns
the ranked list for that level. This mirrors SAP’s Access Sequence mechanism
but is derived statistically rather than read from system configuration. ForCus-
tomerPaymentTerms, the cascade usesL0 = (SoldToParty,SalesDocType),
thenL 1 = (SoldToParty), and finallyL2 =global distribution.
3.4 Inference (Predict)
The output of Phase 2 is a set of JSON lookup files. Prediction requires only
key lookup, so no LLM, KG, or model inference is needed at runtime. Cascade
sizes range from 88 keys (Plant) to 174K keys (HeaderIncoterms).
Why cascades work in configured enterprise data.The method is effective when
the target field has low conditional entropy given a small set of business keys.
In such cases, historical transactions contain repeated evidence of the same con-
figuration rule. A cascade lookup estimates this conditional distribution directly
and preserves exact high-cardinality keys that embedding models may smooth

Business Rule Cascades for Field Prediction 9
away. The knowledge graph helps reduce the combinatorial search over column
subsets by pointing to keys that have business meaning. The LLM does not re-
place statistical validation. It acts as a controller that translates semantic hints
and residual errors into SQL candidates, while every accepted rule is selected by
deterministic validation on held-out data.
4 Experiments
4.1 Setup
We evaluate primarily on SALT-KG [15], covering 8 autocomplete tasks across
4 SAP tables with temporal split at 2020-07-01 (train with 1.9M rows and test
with 403K rows). For the generalization study (Section 4.4), we evaluate on
two additional RelBench v2 [6] datasets, namely rel-arxiv for academic papers
with 53-class author-category prediction and rel-stack for StackOverflow with
3-class badge-type prediction. We compare against the baselines reported in
SALT [13] and SALT-KG [15], and the heterogeneous GraphSAGE GNN from
RelBench v2 [6]. All cascade lookups use only temporally valid data before the
evaluation split cutoff to prevent data leakage.
Metrics.Accuracy measures whether the top-ranked predicted value equals the
held-out target value. MRR measures the reciprocal rank of the true value in
the returned candidate list. For cascade methods, each matched lookup table
stores target values ranked by their training frequency. The top-ranked value is
the statistical mode and is used for accuracy, while the full ranked list is used
for MRR. Thus, MODE is not an evaluation metric, but the estimator used to
construct lookup entries from temporally valid training data.
Rule discovery implementation.The offline rule discovery agent (Section 3.2)
uses Claude Opus 4.6 with temperature 0. Because every proposed candidate is
evaluateddeterministicallybySQLontemporallyvaliddata,theLLMaffectsthe
search process but not the scoring rule. To check sensitivity, we re-ran discovery
on two representative fields (CustomerPaymentTerms,Plant) with GPT-
5.3-Codex and obtained identical cascade structures and test accuracy. This does
not constitute a full LLM-sensitivity study, but it suggests that the accepted
rules are primarily constrained by the data and KG evidence.
4.2 SALT-KG Results
Our method outperforms the evaluated GNN baseline on all 8 fields (Tables 2
and 3). The largest gains occur on high-cardinality, semantically complex fields
(SalesGroup,CustomerPaymentTerms),wheretheGNN’smessage-passing
mechanism does not capture well the business logic encoded in SAP’s Condition
Technique. For near-deterministic organizational mappings (Plant,Shipping-
Point,SalesOffice), both methods converge above 98%.

10 C. Duan
T able 2.MRR on rel-salt. Top rows report baselines from SALT [13] without KG.
Best (w/ KG)is the per-field maximum after adding KG-derived text embeddings [15],
computed from published base MRR +∆MRR at 2-decimal precision. Bottom row
reports our cascade method.
Method PayTrm Sales Grp. Hdr Inc. Item Inc. ShipCond ShipPt Plant Sales Off. Avg
Majority Class 0.23 0.05 0.62 0.62 0.41 0.54 0.59 0.99 0.51
XGBoost [1] 0.57 0.51 0.70 0.70 0.68 0.95 0.99 0.99 0.76
LightGBM [11] 0.10 0.02 0.73 0.73 0.51 0.28 0.61 0.99 0.50
CatBoost [18] 0.44 0.16 0.81 0.80 0.71 0.80 0.99 0.99 0.71
CARTE [12] 0.62 0.46 0.77 0.75 0.74 0.97 0.99 0.99 0.79
AutoGluon [4] 0.52 0.34 0.78 0.78 0.74 0.98 0.99 0.99 0.77
GraphSAGE [7] 0.39 0.20 0.59 0.64 0.59 0.97 0.99 0.99 0.67
Best (w/ KG) 0.65 0.51 0.81 0.80 0.78 0.98 0.991.00 0.815
Ours (cascade)0.852 0.760 0.840 0.840 0.798 0.986 0.9930.997 0.883
T able 3.Accuracy comparison with RelBench v2 baseline. GNN accuracy values are
taken directly from the RelBench v2 leaderboard [6] using its default heterogeneous
GraphSAGE [7] architecture, hyperparameters, and training protocol. We did not re-
train or tune the GNN.
Target Field Ours (Acc) GNN (Acc)
CustomerPaymentTerms82.86%37.47%
SalesGroup70.00%15.76%
HeaderIncoterms77.22%62.23%
ItemIncoterms77.15%69.36%
ShippingCondition69.56%56.85%
ShippingPoint98.65%98.39%
Plant99.68%99.46%
SalesOffice99.91%99.88%
To connect accuracy to operational impact, considerCustomerPayment-
Terms. The GNN assigns the correct payment term to only 37.5% of orders,
meaning that 62.5% would require manual correction. The cascade achieves
82.9%,reducingthemanualcorrectionrateto17.1%.ForSalesGroup(commission-
relevant), the GNN’s 15.8% accuracy is insufficient for operational use, while the
cascade’s 70.0% makes it viable as a default suggestion.
4.3 Semantic Key-Selection Ablation
To quantify the value of semantic key selection, we compare a schema-only entity
MODE baseline with a restricted KG-guided cascade that uses the initial KG-
suggested keys but not the full error-driven refinement and fallback optimization
used in Tables 2 and 3. This ablation is intended to isolate whether KG-provided
hintspointthesearchtowardmoreusefulkeys.Itisnotanexhaustivecomparison
against all possible rule-mining methods.

Business Rule Cascades for Field Prediction 11
Fig. 2.(a) Semantic key-selection ablation before full error-driven refinement. (b) Final
cascade vs. GNN using heterogeneous GraphSAGE from RelBench v2 [6], with per-field
test accuracy on SALT-KG. Numbers above bars indicate absolute accuracy difference.
T able 4.AblationofsemantickeyselectiononSALT-KGtestset(accuracy).Restricted
KGdenotes a KG-guided cascade before the full error-driven refinement and fallback
optimization used in the main results.
Field Schema-only Restricted KG∆
Plant76.6% 99.5%+22.9
ShippingPoint67.0% 78.9%+11.9
HeaderIncoterms69.1% 73.0% +3.8
ItemIncoterms69.1% 72.9% +3.8
ShippingCondition56.6% 59.3% +2.6
SalesGroup68.9% 71.0% +2.2
CustomerPaymentTerms80.0% 81.8% +1.8
SalesOffice99.8% 99.9% +0.1
A verage 74.1% 79.5% +5.4
The value of semantic key selection varies by field type. Cross-entity fields
(Plant,ShippingPoint) show the largest gains because the KG points to
combinations of plants, shipping conditions, and loading groups, a relationship
invisible from table schemas alone. Composite-key fields (HeaderIncoterms,
ItemIncoterms,ShippingCondition,SalesGroup) gain between 2% and
4% because KG hints indicate which additional columns may disambiguate the
target. Already-simple fields (SalesOffice,CustomerPaymentTerms) gain
little because they are nearly determined by a single entity without KG guidance.
4.4 Generalization Study
To test whether cascade lookups generalize beyond enterprise data, we apply the
same cascade principle to two public RelBench v2 [6] autocomplete tasks. These
datasets do not provide expert enterprise KGs analogous to the SAP ontology,

12 C. Duan
T able 5.Generalization study (accuracy on RelBench v2 val and test sets).
Dataset Task Classes Ours (Val) GNN (Val) Ours (Test) GNN (Test)
rel-arxiv author-cat. 53 52.8% 52.6% 50.3% 50.7%
rel-stack badges-cls. 3 77.6% 80.0% 79.3% 82.8%
so these experiments use task-specific temporal and entity-level keys rather than
the full KG-guided discovery loop. They therefore serve primarily to identify
the boundary conditions under which cascades are and are not effective. All
aggregation queries are temporally filtered to use only data before the evaluation
cutoff, ensuring no label leakage.
rel-arxiv / author-category (53-class).For each author, we compute a temporal-
weighted MODE(category) from their publications, giving higher weight to re-
cent papers (4×/3×/2×/1×for last 1/2/3/older years). This recency weighting
improves test accuracy from 49.7% (uniform MODE) to 50.3%. On the vali-
dation set it achieves 52.8%, slightly exceeding GNN (52.6%). Citation- and
coauthor-based fallbacks proved inferior to global mode due to topic breadth in
cited papers and adjacent subfields among coauthors.
rel-stack / badges-class (3-class, gold/silver/bronze).After RelBench removes
the target and metadata columns, badges contain only (Id, UserId, Date). The
strongest cascade is per-user MODE(Class). Multi-hop enrichment through user
activity(posts,votes,comments)wasineffectivebecausebronzebadgesdominate
the distribution so heavily that MODE returns bronze for every activity level,
including the most active users.
Why cascades match but do not surpass GNNs on non-enterprise data.Unlike
SALT-KG’s configured determinism, these tasks lack explicit business rules that
cascade lookups can exploit.
1. Cold-start entities dominate. On rel-arxiv, 29% of test authors have no publi-
cations before the evaluation cutoff. The cascade can only predict the global
mode for these authors (∼2%accuracy). GNNs face the same cold-start
problem, explaining why both methods achieve only∼50%accuracy.
2.MODE(·)is a lossy aggregation. On rel-stack, bronze badges constitute 86%
of training data, soMODE(·)returns bronze for every feature combination.
GNNs overcome this through learned aggregation functions that amplify
minority-class signals, achieving 82.8% vs. our 79.3%.
3. No configured determinism to recover. On rel-arxiv, an author’s future cat-
egory is correlated with past publications, not determined. On rel-stack,
badge class is determined by threshold rules such as Great Answer requir-
ing≥100 upvotes. These rules require per-instance temporal reasoning, not
entity-level aggregation.

Business Rule Cascades for Field Prediction 13
Fig. 3.Drift analysis. (a) Cross-drift conditional correlation matrix, where asymmetric
cells showP(column drifts|row drifts). (b) Drift rate vs. test accuracy, with bubble
size proportional to field cardinality.
4.5 Drift Root-Cause Analysis
The temporal split (train<2020-07-01<test) exposes concept drift, with per-
customer MODE values changing between training and test periods. For each of
the 5,576 customers present in both splits, we compute (1) the per-field drift rate,
defined as the fraction whose dominant value changed, and (2) the cross-drift
correlation, defined as the fraction of customers who drifted in fieldBamong
those who drifted in fieldA. Figure 3 summarizes both analyses.
Cross-drift structure.Three structural patterns emerge.
1. Coupledpairsmoveinlockstep.HdrIncoterms↔ItmIncotermsco-driftreaches
between 98% and 99%, confirming they are governed by the same business
decision. Plant→ShipPoint co-drift reaches 95%, so when the plant changes,
the shipping point almost always follows.
2. Upstream-downstreamasymmetryrevealscausaldirection.Plant→ShipPoint
is 95%, but ShipPoint→Plant is only 58%, which indicates that shipping
point reassignment frequently occurs without changing the plant. Similarly,
CustPayment→ShipCond is 57%, but ShipCond→CustPayment is only 23%.
3. Stable fields are nearly drift-free. SalesOffice drifts in only 0.3% of customers
(14/5,576).
Drift as a performance ceiling.Among the four non-trivial fields (accuracy
<95%), drift rate and test accuracy are consistent with a linear anti-correlation
(slope=−0.54pp accuracy per pp drift,R 2 = 0.98). Because this fit is based
on only four fields, the highR2 should be interpreted as directionally suggestive

14 C. Duan
rather than statistically conclusive.CustomerPaymentTermshas the low-
est drift (17.8%) and highest accuracy (82.9%), whileShippingConditionhas
the highest drift (43.8%) and lowest accuracy (69.6%). This ceiling is method-
agnostic because both cascades and GNNs face the same organizational changes.
ForHeaderIncoterms, drifted customers show a directional DDP→DAP
transition (495 vs. 89 customers), consistent with documented supply chain risk
reallocation during COVID-19 disruptions [3]. ForSalesGroup, 76% of drifted
customers retained the same Sales Area entirely, confirming that drift is driven
by internal team reassignment rather than customer behavior changes.
4.6 Error Analysis and Case Studies
Success case with payment terms resolved by customer×document type.Con-
sider a customer who places standard orders (document type TA). The cascade’s
finest level (SoldToParty×SalesDocumentType) maps this combination to pay-
ment term 03 (net 30 days), a mapping stable across the entire training period
that correctly predicts all test-period orders. The cascade directly encodes the
business rule that this customer’s contract specifies net-30 for standard orders.
Failure cases are structurally tied to drift. As shown in Section 4.5, organi-
zational restructuring (e.g., sales team reassignment) renders historical lookup
rules obsolete in a way that no method can predict from transaction data alone.
Governance case with correlated drift revealing upstream configuration depen-
dency.The cross-drift analysis (Figure 3a) reveals that when a customer’s
Plantassignment changes,ShippingPointco-drifts 95% of the time, but the
reverse holds only 58%. This asymmetry tells configuration owners that plant re-
assignmentshouldtriggershippingpointreview,butnotviceversa.Similarly,co-
drift betweenHeaderIncotermsandItemIncotermsreaches between 98%
and 99%, confirming they are governed by the same business decision, a valida-
tion that individual field-level audits might miss.
5 Discussion
When to use cascades in practice.The central lesson from our three-domain
evaluation is that the quality of available domain knowledge matters more than
the sophistication of the model. The differentiator is the alignment between do-
main knowledge and observable data. Cascades excel when a domain-expert KG
provides determination hints that correspond to available data columns, match
GNNs when no such expert KG or stable rule structure exists (rel-arxiv with
50.3% vs. 50.7%), and underperform when prediction requires per-instance tem-
poral reasoning that GNNs learn implicitly (rel-stack with 79.3% vs. 82.8%).
Practitioners should prefer GNNs when discriminative signal resides in graph
neighborhoods or temporal patterns, and use drift analysis as an operational di-
agnostic regardless of method, since the observed relationship between drift rate
and accuracy (Section 4.5) enables proactive identification of entities requiring

Business Rule Cascades for Field Prediction 15
configuration review. In this sense, the method recovers part of the declarative
rule structure visible in historical transactions, while procedural configuration
changes and organizational restructurings remain outside the observable data.
Practical advantages.Beyond accuracy, cascades offer interpretability (each pre-
diction traces to a specific composite key), no model-serving cost at inference
time (JSON key lookup on CPU, with 12 MB total storage for 8 fields vs.
∼200 MB model weights), and rapid updates (rebuild in minutes vs. hours of
GPU retraining). We recommend field-specific deployment modes, including ed-
itable suggestions for all fields, conservative auto-fill for near-deterministic fields
(>99% accuracy), and audit-only logging for high-drift fields.
Prototype-to-production path.The current evaluation is offline. A production de-
ployment should first run in shadow mode, where cascade suggestions are logged
but not automatically applied. Operational metrics should include suggestion ac-
ceptance rate, operator override rate, post-entry correction rate, lookup latency
under concurrent load, and the precision of drift alerts as judged by configura-
tion owners. These measurements are required before claiming realized workload
reduction in production.
Reproducibility.All code, cascade JSON files, evaluation scripts, and the drift
analysis toolkit are publicly released. Experiments are reproducible from the
released code and public SALT-KG data [15].
Ethics and governance.All experiments use pseudonymized keys (integer IDs)
without access to personally identifiable information. Cascade mappings should
be audited for correlations with protected attributes before deployment. Cas-
cades require periodic rebuilding (e.g., quarterly), with drift alerts flagging cus-
tomers exceeding historical change rates. Predictions are surfaced as editable
suggestions rather than autonomous overwrites, and operators retain full over-
ride authority. Each prediction logs the matched cascade level and composite
key, supporting post-hoc analysis and regulatory compliance.
Threats to validity.SALT-KG represents a single SAP S/4HANA ERP system
instance. The generalization study partially addresses this, but neither public
dataset has comparable configuration richness. The public datasets do not con-
tain expert-curated determination KGs comparable to the enterprise setting,
so the generalization study evaluates the cascade principle rather than the full
KG-guided workflow. GNN baselines use RelBench v2’s default protocol without
task-specific tuning. The LLM sensitivity check covers only two representative
fields, and weaker models may fail to translate KG hints effectively. The tem-
poral split at 2020-07-01 coincides with COVID-19, and observed drift patterns
may reflect pandemic-specific disruptions.

16 C. Duan
Limitations.(1) Cascades require configured determinism to outperform GNNs.
On general relational data they match but do not exceed GNN performance.
(2) Cold-start entities fall through to coarse defaults with no viable relational
fallback. In deployment, predictions that reach only coarse organizational fall-
backs or the global mode should be surfaced as low-confidence suggestions rather
than auto-filled values. (3) The system has been validated offline on historical
data and has not yet been deployed in a production ERP environment. (4) We
did not include classical rule-mining baselines such as association rules, FP-
Growth, RuleFit, or decision lists. This limits our ability to separate the benefit
of KG-guided key selection from the benefit of symbolic rule extraction in gen-
eral.
Future directions.Two extensions are most promising. The first is temporal cas-
cades that perform per-instance temporal-windowed aggregation, enabling rule
reconstruction for threshold-based systems like StackOverflow badges. The sec-
ond is hybrid cascade-GNN architectures that use cascade predictions as features
or priors for GNN training, potentially combining interpretability with learned
generalization for unseen or recently reorganized entities.
6 Conclusion
The results show that KG-grounded cascade lookups, produced by LLM-guided
SQL profiling and deployed as lightweight JSON files, outperform evaluated
GNN baselines on all 8 SALT-KG enterprise fields. A generalization study on
two public datasets reveals clear boundary conditions. Cascades match GNNs
when field values are governed by stable, recoverable rules, but underperform
when prediction requires temporal graph reasoning. The drift analysis demon-
strates that many residual errors are associated with organizational changes,
providing configuration owners with actionable diagnostics. For practitioners,
the results suggest that investing in domain knowledge assets can be more valu-
able than adopting more complex models when the underlying data is governed
by recoverable configuration rules.
AcknowledgmentThe author was funded by the InsightsNet project (funded
by the Federal Ministry of Education and Research (BMBF) under grant no.
01UG2130A). I gratefully acknowledge the Research group Corpus and Compu-
tationalLinguistics,InstituteofLinguisticsandLiteraryStudies,TUDarmstadt.
I gratefully acknowledge support from the hessian.AI Service Center (funded by
the Federal Ministry of Research, Technology and Space, BMFTR, grant no.
16IS22091) and the hessian.AI Innovation Lab (funded by the Hessian Ministry
for Digital Strategy and Innovation, grant no. S-DIW04/0013/003). I gratefully
acknowledge the computing time granted by the Resource Allocation Board and
provided on the supercomputer Emmy/Grete at NHR-Nord@Göttingen as part
of the NHR infrastructure. The calculations for this research were conducted
with computing resources under the projectnhr_he_starter_25563.

Business Rule Cascades for Field Prediction 17
AI Usage.LLMs were used as part of the proposed offline rule-discovery work-
flow, as described in Section 3.2. For manuscript preparation, LLMs were used
only for readability and grammar assistance. The author reviewed all content
and takes full responsibility.
Disclosure of Interests.The author has no competing interests to declare
that are relevant to the content of this article.
References
1. Chen, T., Guestrin, C.: Xgboost: A scalable tree boosting system. In: Proceedings
of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and
Data Mining. p. 785–794. KDD ’16, Association for Computing Machinery, New
York, NY, USA (2016),https://doi.org/10.1145/2939672.2939785
2. Cui, Y., Kara, S., Chan, K.C.: Manufacturing big data ecosystem: A systematic
literature review. Robotics and Computer-Integrated Manufacturing62, 101861
(Apr 2020),http://dx.doi.org/10.1016/j.rcim.2019.101861
3. Davis, J., Vogt, J.: Hidden supply chain risk and incoterms®: Analysis and mit-
igation strategies. Journal of Risk and Financial Management14(12), 619 (Dec
2021),http://dx.doi.org/10.3390/jrfm14120619
4. Erickson, N., Mueller, J., Shirkov, A., Zhang, H., Larroy, P., Li, M., Smola, A.:
Autogluon-tabular:Robustandaccurateautomlforstructureddata(2020),https:
//arxiv.org/abs/2003.06505
5. Gao, D., Wang, H., Li, Y., Sun, X., Qian, Y., Ding, B., Zhou, J.: Text-to-sql
empowered by large language models: A benchmark evaluation. Proc. VLDB En-
dow.17(5),1132–1145(Jan2024).https://doi.org/10.14778/3641204.3641221,
https://doi.org/10.14778/3641204.3641221
6. Gu, J., Ranjan, R., Kanatsoulis, C., Tang, H., Jurkovic, M., Hudovernik, V.,
Znidar, M., Chaturvedi, P., Shroff, P., Li, F., Leskovec, J.: Relbench v2: A large-
scale benchmark and repository for relational data (2026),https://arxiv.org/
abs/2602.12606
7. Hamilton, W.L., Ying, R., Leskovec, J.: Inductive representation learning on large
graphs. In: Proceedings of the 31st International Conference on Neural Information
Processing Systems. p. 1025–1035. NIPS’17, Curran Associates Inc., Red Hook,
NY, USA (2017)
8. Haug, A., Stentoft Arlbjørn, J., Pedersen, A.: A classification model of erp system
data quality. Industrial Management & Data Systems109(8), 1053–1068 (Sep
2009),http://dx.doi.org/10.1108/02635570910991292
9. Hollmann, N., Müller, S., Eggensperger, K., Hutter, F.: Tabpfn: A transformer that
solves small tabular classification problems in a second. In: International Confer-
ence on Learning Representations 2023 (2023)
10. Hong, S., Lin, Y., Liu, B., Liu, B., Wu, B., Zhang, C., Li, D., Chen, J., Zhang,
J., Wang, J., Zhang, L., Zhang, L., Yang, M., Zhuge, M., Guo, T., Zhou, T.,
Tao, W., Tang, R., Lu, X., Zheng, X., Liang, X., Fei, Y., Cheng, Y., Ni, Y.,
Gou, Z., Xu, Z., Luo, Y., Wu, C.: Data interpreter: An LLM agent for data
science. In: Che, W., Nabende, J., Shutova, E., Pilehvar, M.T. (eds.) Find-
ings of the Association for Computational Linguistics: ACL 2025. pp. 19796–
19821. Association for Computational Linguistics, Vienna, Austria (Jul 2025).
https://doi.org/10.18653/v1/2025.findings-acl.1016

18 C. Duan
11. Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., Liu, T.Y.:
Lightgbm: a highly efficient gradient boosting decision tree. In: Proceedings of
the 31st International Conference on Neural Information Processing Systems. p.
3149–3157. NIPS’17, Curran Associates Inc., Red Hook, NY, USA (2017)
12. Kim, M.J., Grinsztajn, L., Varoquaux, G.: Carte: pretraining and transfer for tab-
ular learning. In: Proceedings of the 41st International Conference on Machine
Learning. ICML’24, JMLR.org (2024)
13. Klein, T., Biehl, C., Costa, M., Sres, A., Kolk, J., Hoffart, J.: SALT: Sales autocom-
pletion linked business tables dataset. In: NeurIPS 2024 Third Table Representa-
tion Learning Workshop (2024),https://openreview.net/forum?id=UZbELpkWIr
14. Klein, T., Hoffart, J.: Position: Foundation models for tabular data within systemic
contexts need grounding (2026),https://arxiv.org/abs/2505.19825
15. Mulang’, I.O., Sasaki, F., Klein, T., Kolk, J., Grechanov, N., Hoffart, J.: Salt-kg:
A benchmark for semantics-aware learning on enterprise tables. In: Proceedings of
the AI for Tabular Data workshop at EurIPS 2025 (2025)
16. Pan, S., Luo, L., Wang, Y., Chen, C., Wang, J., Wu, X.: Unifying large lan-
guagemodelsandknowledgegraphs:Aroadmap.IEEETransactionsonKnowledge
and Data Engineering36(7), 3580–3599 (2024).https://doi.org/10.1109/TKDE.
2024.3352100
17. Pourreza, M., Rafiei, D.: Din-sql: decomposed in-context learning of text-to-sql
with self-correction. In: Proceedings of the 37th International Conference on Neural
Information Processing Systems. NIPS ’23, Curran Associates Inc., Red Hook, NY,
USA (2023)
18. Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A.V., Gulin, A.: Catboost:
unbiased boosting with categorical features. In: Proceedings of the 32nd Inter-
national Conference on Neural Information Processing Systems. p. 6639–6649.
NIPS’18, Curran Associates Inc., Red Hook, NY, USA (2018)
19. Riahi, Y., Saikouk, T., Gunasekaran, A., Badraoui, I.: Artificial intelligence ap-
plications in supply chain: A descriptive bibliometric analysis and future re-
search directions. Expert Systems with Applications173, 114702 (Jul 2021),
http://dx.doi.org/10.1016/j.eswa.2021.114702
20. Robinson, J., Ranjan, R., Hu, W., Huang, K., Han, J., Dobles, A., Fey, M.,
Lenssen, J.E., Yuan, Y., Zhang, Z., He, X., Leskovec, J.: Relbench: A bench-
mark for deep learning on relational databases. In: The Thirty-eight Conference on
Neural Information Processing Systems Datasets and Benchmarks Track (2024),
https://openreview.net/forum?id=WEFxOm3Aez
21. Spinaci, M., Polewczyk, M., Schambach, M., Thelin, S.: Contexttab: A semantics-
aware tabular in-context learner. In: Advances in Neural Information Processing
Systems (NeurIPS) (2025)
22. Wang, X., Gao, T., Zhu, Z., Zhang, Z., Liu, Z., Li, J., Tang, J.: KEPLER: A
unified model for knowledge embedding and pre-trained language representation.
Transactions of the Association for Computational Linguistics9, 176–194 (2021),
https://aclanthology.org/2021.tacl-1.11/
23. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K.R., Cao, Y.: React:
Synergizing reasoning and acting in language models. In: The Eleventh Interna-
tional Conference on Learning Representations (2023),https://openreview.net/
forum?id=WE_vluYUL-X
24. Zhang, X., Luo, S., Zhang, B., Ma, Z., Zhang, J., Li, Y., Li, G., Yao, Z., Xu, K.,
Zhou, J., Zhang-Li, D., Yu, J., Zhao, S., Li, J., Tang, J.: TableLLM: Enabling
tabular data manipulation by LLMs in real office usage scenarios pp. 10315–10344
(Jul 2025),https://aclanthology.org/2025.findings-acl.538/
