---
title: 'OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst
  querying'
url: https://arxiv.org/abs/2609.08869
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Furqan Nasir
- Muhammad Atif Saeed
- Muhammad Ehsan
- Sher Jeel Ahmad
- Abdul Moiz Altaf
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.08869
pages: 31
chars: 162977
fetched_at: '2026-11-08T13:20:21+00:00'
kb_version: 1
---

# OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying

OntoKG-EQ: Evidence-boundary auditing for analytical knowledge graphs
Furqan Nasira,b,∗, Muhammad Atif Saeedb, Muhammad Ehsana, Sher Jeel Ahmadc, Abdul Moiz Altafa
aCity University of Science and Information Technology (CUSIT), Peshawar, Pakistan
bNational University of Computer and Emerging Sciences (F AST-NUCES), Islamabad, Pakistan
cUniversity of Engineering and Technology (UET), Peshawar, Pakistan
Abstract
An analytical knowledge-graph result can be supported in its ambient graph while its delivered explanation omits deciding
observations. OntoKG-EQ connects competency-question requirements to an executable audit of ambient observations,
declared finding support and delivered evidence. A bounded declarative interpreter distinguishes positive, false and
unknown numerical status, with same-witness unit readiness reported separately. A public-data application reconstructs
England’s August 2026 provider-level referral-to-treatment statistical screen. Independent source recomputation reconciles
532 providers with the publisher workbook: 91 meet the inclusive 92% threshold and 441 do not. One additional roster
entry remains unavailable rather than zero-filled. All 533 application frames agree with an independently implemented
standards-based validation and availability baseline. Transfer requires a disclosed source adapter and arithmetic
compilation, but no change to the core interpreter. Twenty-six constructed analytical cases yield 78 status/readiness
agreements. Actual financial release replay reproduces two omitted-volume defects: support and delivery suffice for 19 of
21 original findings and all 21 repaired findings after interface adaptation. A separate replay agrees on 487 overlapping
financial records. Source audits expose scaling errors and unresolved comparator and temporal assumptions, so financial
examples do not establish authenticated market effects. The contribution is a reproducible analytical audit interface and
source-reconciled application, not new sufficiency logic or first evidence-boundary isolation. Historical ratings measure
preference only; objective human audit benefits and independent production deployment remain untested.
Keywords:Knowledge graphs, Provenance, Evidence auditing, SHACL, Ontology engineering, Reproducibility
1. Introduction
Analytical knowledge graphs combine heterogeneous
observations with executable queries, but reproducing an
answer requires more than recovering its result entities. An
auditor must identify the query conditions, the observa-
tions that decided those conditions, their temporal context,
and their sources. OntoKG-EQ investigates the following
question:How can competency-question requirements gov-
ern the construction and validation of analytical knowledge
graphs so that query results carry inspectable supporting
evidence?
Equity analysis provides the original case study. Ana-
lysts compare reported fundamentals with market response,
examine exchange-rate associations, compare company re-
turns with sector and benchmark returns, and inspect
announcement-window activity. These tasks combine nu-
merical computation with requirements for temporal align-
ment and source traceability. Figure 1 illustrates the in-
tended evidence path for one relative-outperformance result.
∗Corresponding author.
Email addresses:furqan.nasir@cusit.edu.pk(Furqan Nasir),
atif.saeed@isb.nu.edu.pk(Muhammad Atif Saeed),
me@cusit.edu.pk(Muhammad Ehsan),Sherjeel4all@gmail.com
(Sher Jeel Ahmad),moizaltaf8080@gmail.com(Abdul Moiz Altaf)
The financial setting supplies concrete requirements and
evaluation data; the reusable design concerns the orga-
nization of requirements, semantic artifacts, and result
evidence.
The additional public-data application asks an
externally specified question about incomplete referral-
to-treatment pathways in England. Unlike the aligned
financial fixtures, it starts from a publisher’s raw aggregate
reporting schema and independently reconciles the deciding
counts with the publisher’s workbook. This tests whether
the audit interface can retain explicit source, entity,
reporting-period and evidence-boundary distinctions in
a nonfinancial task. It does not assume that technical
portability establishes practitioner uptake.
We treat this as a problem ofdata and knowledge engi-
neering, not prediction. The goal is not to forecast prices or
recommend trades. It is to make analyst-oriented queries
over heterogeneous market datareproducible, evidence-
linked, temporally explicit, structurally valid, and
inspectable. Every materialized finding can be inspected
together with its explicit supporting observations and tem-
poral context. Source attribution is checked separately; a
company disclosure linked as context does not establish
the source of every numerical observation.
Our approach builds on established knowledge-graph
arXiv preprint, version 2 November 2026
arXiv:2609.08869v2  [cs.ET]  1 Nov 2026

Figure 1: A worked example (Indonesia, CQ3, corrected financial-v2 graph). ISAT is returned as a relative outperformer because its window
return exceeds both same-window comparators. The evidence-boundary audit finds the condition positive in the ambient graph, the declared
support and the delivered bundle, with declared units on the same witness. Numeric values trace to recorded workbook cells; the FY2025 IDX
disclosure is contextual evidence and does not establish those values. SHACL conformance concerns structure only. Values are demonstrator
fixtures, not authenticated market returns.
foundations and surveys [1, 2], SPARQL query semantics
[3], and the explainable-AI literature [4], adapting them to
the bounded, provenance-first setting of analyst querying.
The novelty question concerns the explicit connection be-
tween CQ requirements, executable analytical conditions,
and inspectable result evidence; the individual standards
and the general idea of provenance-based explanation are
established. Financial-domain ontologies such as FIBO
model the concepts of finance comprehensively, but do
not, on their own, provide a bounded, executable path
from a parameterised query to the evidence and prove-
nance that justify each result. Recent financial knowledge
graphs emphasise large-scale, often LLM-driven, extrac-
tion, and explicitly flag interpretability and provenance as
open challenges [5, 6]. Graph-based retrieval-augmented
generation (GraphRAG) grounds language-model answers
in retrieved subgraphs, but its faithfulness is estimated
rather than guaranteed, because a generated answer may
not be entailed by the retrieved evidence.
We presentOntoKG-EQ, a knowledge-based system
that operationalises explainable analyst querying over eq-
uity data. OntoKG-EQ is built around five frozen com-
petency questions (CQ1–CQ5) that bound its scope: no
ontology class, property, SHACL shape, derived metric, or
inference rule exists unless it is required to answer one of
them. Given a market’s data, the system (i) materialises it
into a provenance-aware RDF knowledge graph aligned to a
compact core ontology; (ii) computes the derived analytical
metrics the questions require (window returns, year-on-
year growth, sector and benchmark returns, exchange-rate
association, and event-window abnormal return and vol-
ume); (iii) validates structure with SHACL; (iv) answers
each competency question with SPARQL that computes
its stated condition; (v) applies inference rules that de-
rive typed, queryable analytical findings (e.g., relative-
outperformer, fundamentals–market divergence, abnormal-
event reaction); and (vi) generates, automatically and
for every result, an evidence bundle that exposes the in-
spectable path from the executed query to its supporting
observations, evidence items, official sources, and prove-
nance. Deterministic rendering avoids stochastic changes
during transcription, but consistency and completeness
depend on the correctness of the selected observations and
links.
A secondary claim concernsreuse of the apparatus
over structurally aligned datasets, not arbitrarily hetero-
geneous reporting structures. We demonstrate it on three
market-specific demonstrator datasets: the Pakistan Stock
Exchange (PSX, KSE-100 index), Bursa Malaysia (MSX,
FBM KLCI index), and the Indonesia Stock Exchange
(IDX, Jakarta Composite). The core ontology, SHACL
shapes, the five competency-question queries, and the infer-
ence rules are reused byte-identical across all three markets.
Only the data and a small per-market adapter configura-
2

tion change. Every market is SHACL-conformant under
the declared shapes. The revision separately checks finding
dependencies and workbook-level lineage.
The contributions are threefold:
1. An evidence-boundary audit protocol that evaluates
an analytical condition independently over ambient
observations, declared finding support and the actu-
ally delivered explanation bundle, without borrowing
omitted observations across these boundaries.
2. An RDF/SPARQL implementation with preserved
financial replay and a bounded, declaratively config-
ured audit interpreter. Witness sufficiency, metadata
readiness, recorded source paths and external source
truth remain distinct properties; the interpreter is
not a general provenance calculus.
3. A source-reconciled public NHS statistical-screen
application with explicit eligibility and missingness,
alongside a diagnostic benchmark with matched
SHACL-SPARQL comparison and paired financial
replay. The NHS application uses a new adapter
and arithmetic compilation, rather than claiming
unchanged whole-pipeline reuse. Existing complete-
query, withholding and source audits provide
complementary evidence rather than additional
independent samples. Historical participant ratings
provide preference evidence only.
The method instantiates established semantic technologies.
Its value must be assessed through the explicit organization
and verifiability of requirements and evidence, rather than
by claiming that provenance or deterministic explanations
are unique to knowledge graphs. The original and revision
code and data are publicly released (see Data and code
availability).
2. Related work
OntoKG-EQ sits at the intersection of four lines of
work. We review each line of work and state precisely what
OntoKG-EQ adds.
2.1. Financial ontologies and knowledge graphs
The Financial Industry Business Ontology (FIBO) [7, 8]
is the de-facto OWL standard for finance, governed by the
EDM Council and OMG and paired with triplestores for
inference and property-path querying. FIBO targets broad
conceptual coverage. Recentworkextendsitinspecificdirec-
tions: FinCaKG-Onto, for instance, uses FIBO as a scaffold
to depict financial expertise as a causality knowledge graph
[9]. OntoKG-EQ takes the opposite stance. It is a bounded,
competency-question-scoped core in which every term ex-
ists to answer one of five frozen analyst questions, and
it provides anexecutable, inspectable analytical-querying
capabilityrather than a domain vocabulary.
A fast-growing parallel line builds financial knowledge
graphs by automated extraction. FinReflectKG constructs
a graph from SEC filings with agentic, reflection-driven
extraction and a rule-, statistical-, and LLM-as-judge eval-
uation pipeline [5]. FinKario adds event-enhanced auto-
mated construction coupled to a two-stage graph retrieval
strategy for stock-trend prediction [10]. A comprehen-
sive survey of the field [6] catalogues applications such as
fraud, credit risk, anti-money-laundering, and compliance,
while explicitly naming interpretability and provenance as
open challenges. Notably, this concern is not new to the
extraction community itself: Kertkeidkachorn and Ichise
argue that automatically constructed financial graphs, lack-
ing a well-defined ontology, suffer degraded reasoning and
quality, and respond with FinKG, an expert-verified core
ontology [11]. Financial KG construction also includes ex-
plicit source attribution and multidimensional evaluation.
FinReflectKG–EvalBench separates faithfulness, precision,
relevance and comprehensiveness for financial extraction
[12]. Consequently, evidence and governance are not absent
from this research line. OntoKG-EQ targets a different
operational task: checking the typed observations and tem-
poral bindings that suffice for a particular analytical condi-
tion. Competency questions have also been used to evaluate
financial graphs [13]; our frozen question set bounds the
demonstrator and its artifacts without establishing a new
general ontology-engineering principle.
2.2. Competency-question-driven ontology engineering
Competency questions (CQs) are a long-standing device
for scoping and validating ontologies [14, 15], embedded
in ontology-engineering methodologies such as NeOn [16].
A recent survey of 63 practitioners confirms that CQs are
used mainly to define scope and evaluate a conceptualiza-
tion, but also that engineers still lack guidance for writing
and managing them [17], and Keet and Khan argue that
CQs serve manifold roles across the engineering lifecycle
beyond mere fact-seeking [14]. In practice, however, CQs
are seldom published alongside the ontologies they shaped
[18], which leaves their governing intent implicit. There is
also active work on formalising CQs as SPARQL/SPARQL-
OWL queries [19] and tooling that mints CQ→SPARQL
pairs for question answering over knowledge graphs [20].
Recent work makes the requirement-to-ontology connection
explicit: CQ4OE publishes CQ-to-term and CQ-to-axiom
provenance and distinguishes partial from full requirement
coverage [21]; MASEO records CQ and validation rationale
during ontology construction [22]. OntoKG-EQ therefore
does not introduce CQ-based provenance. It evaluates a
bounded runtime contract connecting analytical metric
roles, selection conditions, matching windows and sufficient
finding evidence. Documented CQ labels and executable
sufficiency checks establish different properties. The five
frozen questions remain a reproducibility boundary, not
proof that the domain requirements are exhaustive or un-
ambiguous.
3

2.3. Provenance and structural validation
Semantic answer explanation is an established research
topic. Inference Web represents justifications for retrieved
and inferred answers through provenance and derivation
information [23]. Dividino et al. formalize and implement
querying RDF together with source, trust, uncertainty,
and other meta-knowledge [24]. Consequently, per-answer
explanation and queryable provenance are not new capa-
bilities introduced by OntoKG-EQ.
The PROV model provides interoperable provenance
representation [25, 26]; it does not establish that source
records or reported values are true. SHACL provides
declared graph constraints and validation reports [27].
Recent work studies validation efficiency and semantics
[28, 29, 30], and provenance of graph construction [31].
Native Provenance Computation for SPARQL provides
fine-grained provenance of query results, including non-
monotonic queries [32]. Analytical conditions can be en-
coded in queries or SHACL-SPARQL; they are not inher-
ently beyond these mechanisms.
The closest evidence-oriented predecessors impose a
stronger novelty boundary. Delva et al. establish sufficient
SHACL neighborhoods and shape fragments, including
nonconformance explanations [33]. Fierro’s Shifty returns
satisfaction traces and failure witnesses, including Boolean
alternatives and an application-input example with unit
requirements [34]. Ontological Knowledge Blocks combine
declarative obligations, evidence and executable constraints
[35]; manufacturing trust infrastructure combines temporal
state, provenance and decision records [36]. Thus neither
sufficient evidence, branch-sensitive justification, declara-
tive contracts nor temporal-provenance integration alone is
our novelty claim. We operationalize a narrower audit task:
independently check the ambient observations, declared
finding support and actually delivered bundle under the
same analytical condition, while retaining separate meta-
data and source qualifications. Whether this organization
provides an engineering advantage must be evaluated, not
inferred from standards choice.
Scope separation itself also has direct predecessors.
SHACL-DS evaluates declared graph views; its railway
study shows that merging graphs can mask a missing ref-
erence by borrowing it from another contributor [37]. ES-
Glass separates internal evidence assembly from public
rendering and proposes incomplete-bundle diagnostics [38];
it is an unreviewed concept paper rather than an executed
equivalent comparator in the inspected source. These works
prevent a first-boundary-isolation claim. Our distinction
is the concrete application-specialized analytical interface
and its executed paired tests, not discovery of a previously
unknown need for scoped evidence or abstention.
2.4. Explainable querying, GraphRAG and faithfulness
Graph-based retrieval-augmented generation [39], which
extends retrieval-augmented generation [40], retrieves sub-
graphs to ground language-model answers, and a rich family
of systems now refines this idea: HybridRAG combines
graph and vector retrieval for financial question answering
over earnings calls [41], and Think-on-Graph 2.0 interleaves
graph and text retrieval to deepen reasoning [42]. There
is also explicit work on explaining KG-RAG [43] and on
detecting hallucinations in retrieval-augmented generation
[44]. The recurring difficulty across all of these isfaith-
fulness: even with retrieval, a generated answer may not
be entailed by the retrieved context. Recent evaluation
work makes the point sharply. Ahmad and Khan show
that lexical metrics such as BLEU and ROUGE correlate
only weakly with structural grounding, and that removing
graph retrieval preserves lexical accuracy while eliminating
traceable evidence altogether [45]. Faithfulness, in other
words, is a structural property that text-overlap scores do
not capture. This is also increasingly recognised outside
the evaluation literature: Sequeda et al., writing from en-
terprise practice, argue that knowledge graphs provide the
formal frame to check a generated query’s validity, the
foundation for explaining a result, and access to governed,
trusted data, precisely the roles a bare language model
cannot fill [46].
Recent ontology-guided GraphRAG evaluates canon-
icalisation, traceability and verifiability separately [47].
This prevents a blanket contrast in which generative graph
systems lack traceable sources. OntoKG-EQ uses deter-
ministic query execution and rendering, conditional on
correct queries, evidence selection and rendering. It does
not resolve source truth by construction. Work on non-
generative answering [48] is a relevant predecessor. The
historical transcription panel holds retrieval fixed and is
excluded from the revised main quantitative evaluation
because generated answer texts were not archived.
2.5. Positioning and novelty
Table 1 identifies specific predecessors and the rela-
tionship of their verified objectives to this system. An
unreported capability is not evidence that a system lacks it.
The scope of the present comparison is the analytical work-
flow implemented here, rather than firstness of explanation
or provenance.
Executable competency questions also have established
precedents. Wisniewski et al. publish and analyze CQs
with SPARQL-OWL formalizations [49]. Our traceability
matrix documents the association of requirements with
artifacts; it does not prove ontological minimality or cor-
rect interpretation of every natural-language question. We
assess the composition through declared constraints, result
dependencies, numerical checks, and reproducible artifact
reuse.
The resulting research question is not whether prove-
nance can explain an answer, but whether a delivered
analytical explanation contains an admissible witness with-
out borrowing omitted observations from its ambient graph.
A finding can be numerically true in the graph while its
delivered bundle is incomplete or contains only nonpassing
candidates. Conversely, deleting one observation from a
4

Table 1: Named predecessors and the contribution boundary. NR
means not established by the inspected source, not absent.
Work Established mecha-
nism
Relationship to
OntoKG-EQ
Inference Web [23] Provenance and
derivations explain-
ing answers
Direct predecessor
for individual-
answer justification;
current CQ-to-
metric contract NR
Dividino et al. [24] Representation and
querying of RDF
meta-knowledge
Direct predeces-
sor for queryable
source/provenance
information; cur-
rent analytical
contract NR
PROV rationale
[26]
General provenance
representation and
design
Foundation for at-
tribution, not a
competing equity-
analysis system
Wisniewski et al.
[49]
Published CQs and
SPARQL-OWL for-
malizations
Prior executable re-
quirement artifacts
CQ4OE / MASEO
[21, 22]
CQ-to-ontology
provenance and
construction ratio-
nale
Prior design trace-
ability; distinct
from runtime an-
alytical witness
checks
NPCS [32] Fine-grained
SPARQL result
provenance
Generic derivation
provenance; no
untested claim of
inferior domain
validation
SHACL neighbor-
hoods [33]
Sufficient sub-
graphs and non-
conformance
provenance
Direct predecessor;
no new sufficiency
theorem claimed
Shifty [34] Passing/failing evi-
dence, Boolean wit-
nesses, application-
input contracts
Direct predecessor;
three-pool analyti-
cal audit is the eval-
uated task, not an
expressiveness sepa-
ration
OKB / manufactur-
ing trust [35, 36]
Executable obliga-
tions, evidence and
temporal decision
provenance
Prior integration
mechanisms; no
first-contract or
first-temporal-
provenance claim
SHACL-DS [37] Scoped graph
views and observed
merged-graph
masking
Direct predecessor
for evidence-scope
isolation; our obser-
vation pools retain
ambient metadata
ESGlass [38] Conceptual inter-
nal/public evidence
separation and
incomplete-bundle
tests
Prior agenda; imple-
mented analytical
diagnostics, not
conceptual firstness,
distinguish this
study
Ontology-guided
GraphRAG [47]
Canonicalisation
and traceability
audits
Relevant source-
verification dis-
tinction; different
end-to-end answer-
ing task
OntoKG-EQ CQ-linked analyti-
cal contracts and
sufficient-witness re-
play
Bounded role, win-
dow and predicate
checks; source-cell
linkage evaluated
separately
bundle need not invalidate it when an independent suffi-
cient branch remains. These are diagnostic distinctions to
test against a semantically matched encoding, not evidence
that existing validation languages cannot express them.
3. Preliminaries and formal model
3.1. Frozen competency questions
The scope of OntoKG-EQ is fixed by five competency-
question (CQ) families, frozen before modelling. They are
the functional requirements the system must answer and
the governance boundary for every modelling decision: no
ontology term, data field, SHACL shape, derived metric, or
inference rule is admitted unless at least one CQ requires
it.
• CQ1. Fundamentals versus market response.
Which companies show stronger reported fundamen-
tals but a weaker subsequent market response over a
defined post-reporting window?
• CQ2. Exchange-rate context and market be-
haviour.How is movement in a selected local cur-
rency pair associated with company-, sector-, or
benchmark-level market measures over a predefined
window?
• CQ3. Relative outperformance versus sec-
tor and benchmark.Which companies outper-
form their sector comparator and the selected broad-
market benchmark over the same period?
• CQ4. Official announcements versus market
reaction.Which official announcements and asso-
ciated disclosures are coincident, within short event
windows, with abnormal return or trading-volume
activity in short event windows such as (−1, +1) and
(−3, +3) trading days?
• CQ5. Explainability and provenance.What
evidence, intermediate relations, metric values, tem-
poral context, sources, and provenance explain why
an entity appears in an executed CQ1–CQ4 result?
CQ1–CQ4 areanalyticalquestions over the data. CQ5
is theexplainabilityquestion that the other four must be
answerable against.
3.2. Core constructs
Let the core ontology beO = (C, P) where C is the set
of classes and P the object and datatype properties, and
let S be a separate validation schema (the SHACL shape
set) layered overO. Both areCQ-bounded: each element
of C∪P∪S is justified by at least oneq∈Q = {CQ1,
..., CQ5}.
Observation.An observation is a tupleo = (e, m,
v,τ, X, r) where e is the observed entity (a Company,
an IndustrySectorClassifier, a MarketIndex, or a currency
pair), m a metric name,v∈R its value,τ a temporal
context (a ReportingPeriod, an AnalysisWindow, or an
5

EventWindow), X a possibly empty set of supporting Evi-
denceItems, and r a ProvenanceRecord. Three subclasses
specialise the entity and temporal context: Fundamen-
talObservation, MarketObservation, and ExchangeRateOb-
servation.
Derived metrics and inference rules.A derived
metric φ: (2ˆObs, W)→Obs maps a set of base obser-
vations and a window to a new, first-class (derived) obser-
vation, and OntoKG-EQ defines nine CQ-justified metrics.
An inference ruleρ: Pattern→Finding maps a graph
pattern encoding a CQ condition over these metrics to
a typed AnalyticalFinding f. The nine-metric list and
the finding tuplef = (e, t,ρ_id, q, O_f) are given in
Online Resource 1 (Section D).
Evidence bundle and explanation.For a result
entity e, an evidence bundleb = (e, O_b, X_b) collects
the supporting observations O_b and evidence items
X_b. A query execution qe = (q, id,π, b) records
an executed CQ instance with parameters π bound to
b. Theexplanationof e is the closure E(e) = { (o,
m, v,τ, x, src, R) : o∈O_b, x∈evidence(o),
src = source(x) }, where R = prov(o)∪prov(x) is
the set of provenance records linking observation o to
its supporting evidence item x. R denotes a set, distinct
from the single ProvenanceRecord r of an individual
finding above; restricting x to evidence(o) avoids forming
unrelated observation–evidence pairs.
3.3. Quality properties
We distinguish five properties.Structural confor-
mitymeans that a particular graph snapshot satisfies the
declared SHACL shapes; this is relative to the coverage
of those shapes.Evidence availabilitymeans that an
answer resolves to an observation and a source.Depen-
dency completenessis stronger: the explanation includes
all observations needed to check the actual query or rule
condition, including matching temporal and comparator
bindings.Analytical correctnessrequires independent
verification of the derived quantities.Source fidelityre-
quires checking that observations and source associations
faithfully represent the originating records.
For a fixed graph snapshot, deterministic rendering
is consistent with its selected evidence only if the ren-
derer copies and labels those values correctly. A complete
explanation additionally assumes correct query/rule imple-
mentations and complete dependency selection. Neither
determinism nor SHACL conformance proves source truth
or analytical correctness. In particular, a well-typed incor-
rect number or an unrelated but well-formed source may
satisfy all declared shapes. The evaluation therefore treats
these properties separately. A non-empty evidence path
alone does not establish a complete justification.
3.4. Executable finding-evidence contracts
Each finding classification has a versioned contract spec-
ifying its metric roles, entity relations, temporal-context
predicates, expected units and selection condition. A
machine-readable manifest identifies the related queries,
builder, rule implementation, documented rules, shapes
and ontology. Artifact hashes identify versions; a hash
match does not establish semantic correctness. Design
provenance connects requirements to these artifacts, while
execution provenance connects a finding to observations
and source cells.
Let Kq denote a declared contract andBf the obser-
vations included in the actual evidence bundle for finding
f, restricted to its declared support. A sufficient witness
W⊆B f assigns compatible observations to the contract’s
roles and makes its predicate true. CQ1 requires positive
growth and a company statistic below its same-window
benchmark. CQ3 requires the company statistic to exceed
both same-window comparators. The R2 contract checks
the FX-sensitive classification only; it does not validate
every field of the broader CQ2 answer. R4 permits either
a passing event-return branch or a passing volume branch.
Both operands need not be necessary evidence for an OR
condition. Expected units are contract assumptions when
the graph lacks explicit unit declarations.
The checker separately replays declared finding support
and observations available in the correctly targeted bundle,
without importing the production SPARQL rules. Missing
roles produce an explicit incomplete status; a complete role
assignment that fails the predicate produces a predicate-
false status. A missing bundle dependency can therefore
be detected even when the finding’s support links remain
intact. The operational complete-bundle rate is the share of
inspected positive findings whose actual bundle contains at
least one sufficient witness. This is relative to the declared
predicate, not proof of global minimality, recall of all correct
answers, or complete domain knowledge.
For a source-linked witness, every recorded dependency
cell of each witness observation must resolve to one regis-
tered source with a matching identifier. This checks path
integrity rather than original-source truth or completeness
of upstream computation. R1 reporting-period-to-window
anchoring and R4 finding-to-event anchoring remain un-
verified where explicit links are absent. The checker writes
separate witness/status overlays and preserves the archived
graphs. Contract coverage is restricted to these finding
classifications; it is not a validator for arbitrary SPARQL
or all five complete CQ outputs.
Operational interface and reuse boundary..The checker
receives a graph snapshot, a finding identifier, its selected
versioned contract and optionally a separate lineage graph.
It enumerates typed metric-role candidates under declared
entity/window relations and evaluates numeric conditions
withDecimalarithmetic. Outputsseparatefull-graphtruth,
finding-support sufficiency, actual-bundle status, witness
identifiers and recorded source-path status; unknown as-
sumptions are not promoted to verified source facts. The
preserved financial checker has a manually specified role vo-
cabulary and four predicate implementations. An additive
6

interpreter instead reads bounded role bindings and numer-
ical branches from configuration; the two implementations
are distinguished in the evaluation. Adding a domain still
requires authored mapping, contract and test work. Nei-
ther implementation is a general provenance calculus or an
empirically validated cross-domain analytical system.
3.5. Evidence-boundary auditing
For a fixed graph snapshotG, entitye and contract
K, letA be the ambient observation pool,S the finding-
declared support andB the declared bundle membership.
The delivered pool isD = B∩S only when the bundle
association identifies the finding’s entity unambiguously;
otherwise D is empty and an association diagnostic is
returned. Extraneous bundle members are reported rather
than admitted as silent repairs. The same role-binding and
numerical checks are applied independently toA, S and
D.
The bounded contract fragment is a disjunction of
conjunctions of numerical comparisons over named roles,
constants, absolute values and addition. Configuration
supplies RDF vocabulary, bounded focus-relative paths,
observation/subject types, metric identifiers and optional
window/unit requirements; predicate evaluation contains
no financial rule-ID branches. Unsupported expressions
and exceeded assignment budgets raise errors rather than
produce analytical verdicts. This is an implementation
fragment, not a new expressive formalism or automatic
translation of natural-language CQs.
For poolP, letCj(P )be the complete compatible as-
signments for branchj, andWj(P )⊆C j(P )those satis-
fying its comparisons. The audit reports positive if some
Wj(P )is nonempty; false if everyCj(P )is nonempty and
everyWj(P )is empty; otherwise it reports unknown. False
therefore describes the inspected finite candidate pool un-
der an explicit complete-input policy, not an open-world
refutation or a general negation semantics. A passing OR
branch suffices without the other branch; missing evidence
is never replaced with zero. No globally minimal witness
or complete failure proof is claimed.
Numerical status and declared-unit readiness are sepa-
rate outputs; matching unit labels do not perform conver-
sion or authenticate a measurement. The positive-readiness
check requires all unit declarations on one and the same
passing assignment: a qualified nonpassing alternative can-
not supply the units of an unqualified passing witness. For
a false diagnostic, readiness requires a complete unit-ready
assignment for each branch; this remains a finite-pool pol-
icy, not a proof over unknown candidates. The observation
pools restrict membership, while entity/path/window meta-
data is read from the fixed ambient snapshot. Consequently
this audit checks delivered observation sufficiency relative
to that metadata, not whether an exported standalone RDF
subgraph is self-sufficient. Local graph/contract/checker
hashes identify experiment artifacts, not signed certificates
or general blank-node canonicalizations. These explicit
boundaries make the audit testable against an equivalent
SHACL-SPARQL encoding without claiming greater ex-
pressiveness.
4. The OntoKG-EQ method and system architec-
ture
OntoKG-EQ is organised as a seven-layer pipeline fol-
lowed by an audit layer (Fig. 2).
Layers L0–L1 onboard a market’s data; L2 computes the
analytical metrics; L3 validates; L4 answers the competency
questions; L5 derives findings; and L6 generates explana-
tions. The evidence-boundary audit (A; Sections 3.4–3.5)
then checks each finding’s condition over the ambient graph,
its declared support and its delivered bundle. The ontol-
ogy, shapes, queries, and rules (L1–L6 logic) are market-
independent; only the data (L0) and a small adapter con-
figuration vary between markets.
4.1. CQ-bounded core ontology
The core ontology provides a compact vocabulary suffi-
cient to express the five competency questions and no more.
Its principal classes are Company, ObservedEntity, Ob-
servation (with subclasses FundamentalObservation, Mar-
ketObservation, ExchangeRateObservation), ReportingPe-
riod, AnalysisWindow, EventWindow, IndustrySectorClas-
sifier, IndustrySectorClassificationScheme, MarketIndex,
Currency, Announcement/Disclosure (as EvidenceItem),
Publisher, EvidenceSource, ProvenanceRecord, Validation-
Status, EvidenceBundle, and QueryExecution. Object and
datatype properties connect observations to their entities,
temporal contexts, metric values, evidence, and provenance.
Each term is traceable to at least one CQ (Section 7.4),
and the ontology classifies without inconsistency under an
OWL 2 EL reasoner. A small alignment module maps the
core to standard upper concepts where a CQ requires it,
keeping the core itself compact.
4.2. L0–L1: Per-market data onboarding and materializa-
tion
A market is supplied as nine tabular sheets (scope/se-
lection, company master, fundamentals, market windows,
comparators, exchange rates, announcements/disclosures,
provenance, and query cases), each row carrying its source.
The materializer reads these sheets and emits a provenance-
aware RDF graph aligned to the core ontology: companies
and their sector classifiers; reporting periods and analy-
sis/event windows; fundamental, market, comparator, and
exchange-rate observations; announcements as evidence
items linked to publishers and evidence sources; and prove-
nance records. To remain reasoner-free at query time,
parent-class type assertions are materialized explicitly, so
SPARQL and SHACL operate without an external rea-
soner.
7

Figure 2: The OntoKG-EQ pipeline. Layers L0–L6 build, validate, query and explain each market graph; only the L0 data and a small
per-market adapter vary, while the ontology, shapes, CQ queries and rules are reused byte-identical. The evidence-boundary audit (A) checks
findings against versioned contracts and is also applied to the NHS public-data application through a separate source adapter and contract.
4.3. L2: Derived analytical metrics
L2 computes the nine derived metrics of Section 3.2 as
first-class observations. The released builder computes
the arithmetic sum of daily simple returns, multiplied
by 100, over each company’s post-report window when
daily returns are available. This is a cumulative simple-
return statistic, not a compounded holding-period return;
when daily returns are unavailable, the builder uses the
endpoint price return. These conventions must be distin-
guished when interpreting the demonstrator metrics; sector
and benchmark returns are computed over the same win-
dow dates as the company they are compared against, so
that CQ1 and CQ3 compare like with like; exchange-rate
association is the Pearson correlation of daily exchange-
rate returns with daily company and benchmark returns
over the shared window (of length n days; because such
short-window correlations are sensitive to outliers and non-
stationarity, the |r|≥ 0.3 flag is a descriptive screen, and
Spearman and multi-window robustness checks are rec-
ommended on licensed data, Section 8.2), alongside the
window-level exchange-rate change. The event statistic cur-
rently labelledcumulative abnormal returnin the archived
vocabulary is implemented as the arithmetic sum of sup-
plied eventdaily_return cells, multiplied by 100. The
builder does not subtract benchmark returns at this step.
Whether these cells already contain abnormal rather than
ordinary returns requires upstream verification. Accord-
ingly, we interpret the archived result as an event-window
input-return statistic and do not claim that the current
implementation independently performs a market-adjusted
event study. The separate abnormal-volume ratio divides
mean nonzero event volume by mean nonzero post-report
volume. The lineage overlay records the actual cells used
by these computations and leaves missing-value defaults
unresolved.
For IDX, the acquisition assembler computes ordinary
company returns as consecutive close-price ratios and writes
them unchanged to event rows. Thus the IDX archived
event statistic is a cumulative company-return sum, not
market-adjusted CAR. A market-adjusted event study
would require aligned daily company and benchmark re-
turns with explicit subtraction. A market-model extension
would additionally estimate parameters over a prior win-
dow [50, 51, 52]. Neither refinement should be inferred
from the current graph’s metric label.
4.4. L3: Structural validation
SHACL shapes encode the structural contract implied
by the ontology: e.g., every Observation carries exactly
one metric name, one decimal metric value, and at least
8

one temporal context; a FundamentalObservation is of
a Company and observed in a ReportingPeriod; an Ex-
changeRateObservation has base and dealt currencies; an
EvidenceBundle explains a result entity and includes at
least one observation or evidence item; and a QueryExe-
cution has a family identifier, an instance identifier, and
an evidence bundle. Validation is a gate: a market is only
admitted to querying once its graph reports Conforms =
True.
4.5. L4: Answering the competency questions
Each competency question is a parameterised SPARQL
template thatcomputes its stated conditionrather than
merely retrieving rows. CQ1 selects companies whose year-
on-year profit growth is positive but whose post-report win-
dow return is below the benchmark return over the same
window; CQ2 returns the exchange-rate-versus-company
and exchange-rate-versus-benchmark return correlations
together with the window-level exchange-rate change; CQ3
selects companies whose window return exceeds both their
sector and benchmark returns over the same window (joined
on a shared window so the comparison is period-consistent);
CQ4 returns announcements whose event-window cumula-
tive abnormal return exceeds a threshold in magnitude or
whose abnormal volume ratio exceeds a threshold; and CQ5
assembles, for an executed result, the supporting observa-
tions with their metric values, the evidence items, and their
official sources. The same five templates run unchanged on
every market.
4.6. L5: Rule-based inference
L5 applies SPARQL CONSTRUCT rules thatmate-
rialiseeach CQ condition as an explicit, queryable typed
AnalyticalFinding (Table 2). This is convenience packaging
rather than a novel inference mechanism: each rule evalu-
ates a deterministic predicate over the derived metrics (no
rule interaction, conflict resolution, or learned parameter),
whose contribution is that a boolean condition becomes
a first-class, provenanced object rather than a transient
query row. A finding records the result entity, its type,
the rule and CQ that produced it, and the observations
that triggered it, so the derivation itself is provenanced
and explainable. The event-window thresholds used by
R4 (|cumulative abnormal return|≥ 2%, abnormal volume
ratio≥1.5) instantiate an operational event-study screen
(fixed thresholds we do not tune) following [50, 51] and are
fixed a priori rather than tuned to the data.
4.7. L6: Automated explanation generation
For every materialized finding, L6 generates an Evi-
denceBundle and QueryExecution that link its result entity
to the observations explicitly supported by the rule. All
matching company announcements are retained as con-
textual evidence, instead of selecting an arbitrary last
announcement. These announcement links alone do not
establish which source supplied each metric.
Table 2: Rule layer (L5): deterministic materialisation of each CQ
condition as a typed, queryable AnalyticalFinding (not a learned or
interacting rule system).
Rule CQ Finding type Condition
R1 CQ1 fundamentals–market di-
vergence
YoY profit growth > 0
and company window re-
turn < benchmark return
R2 CQ2 FX-sensitive abs(FX-vs-company re-
turn correlation)≥0.3
R3 CQ3 relative-outperformer company window return
> sector and > bench-
mark return
R4 CQ4 abnormal-event reaction abs(cumulative abnormal
return)≥2%orabnormal
volume ratio≥1.5
The revised pipeline checks the final graph after adding
findings, bundles, and executions, in addition to the initial
structural gate. It also audits whether explicit finding
supports and generated bundle supports agree and satisfy
the stated rule condition. These checks are distinct from
observation-level source attribution. In particular, the
original R4 rule could select a finding through abnormal
volume while attaching only the return observation; the
revised rule includes the available volume observation. The
final-graph audit in Section 7.11 reports this correction and
the remaining attribution boundary.
4.8. The portable construction methodology
The pipeline doubles as a reusable methodology for
onboarding a new market: (Step 0) freeze the CQs; (Step
1) fix the market-independent core (ontology, shapes, CQ
templates, inference rules); (Step 2) acquire the market’s
nine sheets, each row sourced; (Step 3) provide a small
adapter configuration(namespace, identifier and metric
column names, exchange-rate field, local currency, a growth-
units scale, and the benchmark label); (Step 4) materialize
and derive; (Step 5) validate, answer, infer, and explain;
(Step 6) quantify portability. Only Steps 2–3 are market-
specific. Theportability invariantis that, across markets,
the ontology, shapes, queries, and rules are byte-identical
and only the data and the adapter differ, a property we
measure directly in Section 7.5.
5. Implementation and reproducibility
5.1. Software components
OntoKG-EQ is implemented in Python with a small,
standard semantic-web stack. The core ontology, alignment
module, and demonstrator data are authored in Turtle.
SHACL shapes are validated with pySHACL. The RDF
graph is built and queried with RDFLib. The nine input
sheets are read with openpyxl. The pipeline is realised
by three components that correspond to the layers of Sec-
tion 4: a unified builder that performs materialization
(L1), derived-metric computation (L2), and assembly of
the worked CQ instances; the SHACL shapes and CQ tem-
plates that drive validation (L3) and answering (L4); and
9

an inference-and-explanation generator that applies the
rules (L5) and auto-generates the evidence bundles and
query executions (L6). The inference rules are addition-
ally published as standalone SPARQL CONSTRUCT files
and a small findings vocabulary, so the reasoning layer is
inspectable independently of the driver code.
5.2. One pipeline, a per-market adapter
The builder contains a single code path; each market
is described by one configuration record (Supplementary
Table S1), the only thing that changes between markets
apart from the data. A new market is onboarded by adding
one such record and supplying its nine sheets.
5.3. Recorded environment and availability
The original deterministic results were produced with
Python 3.10 and pinned versions of RDFLib, pySHACL,
openpyxl, pandas, and pyoxigraph (Oxigraph) on a single
workstation (2 vCPU, 3.8 GB RAM); the exact package
versions and hardware are recorded insoftware_environ
ment.md; core dependencies are specified inrequiremen
ts.txt and exactly pinned inrequirements-lock.txt .
The eight-model LLM faithfulness panel was run sepa-
rately on a Kaggle GPU. Its notebook pins the package
versions in the install cell and records the exact resolved
versions, CUDA/GPU, and Hugging Face model revisions
in environment_lock.json . The pipeline is determin-
istic: rebuilding a market from its sheets reproduces the
same graph, SHACL verdict, and competency-question
results. The complete reproducibility package (ontology,
alignment, SHACL shapes, the five CQ templates, the in-
ference rules and findings vocabulary, the unified builder
and the inference/explanation generator, the per-market
data and materialized graphs for all three markets, the
evaluation scripts and outputs, a data dictionary, and the
recorded environment) is openly released in a public repos-
itory with citable Zenodo archives (original releasehttps:
//doi.org/10.5281/zenodo.21569316 ; revision release
v2.0.0 https://doi.org/10.5281/zenodo.23860671 ).
For Indonesia, the exact data-acquisition scripts, the strict
exact-date intersection builder, and a source manifest are
included. Earlier revision checks used Windows, Python
3.13, RDFLib 7.6.0, pySHACL 0.31.0 and openpyxl 3.1.5.
Final local verification used Python 3.13.5, RDFLib 7.6.0,
pySHACL 0.40.1, openpyxl 3.1.5 and Oxigraph 0.5.11; the
separate revision dependency file and run ledger record this
environment. Script outputs record graph hashes and cover-
age. Historical performance measurements were not rerun
in this environment. Participant-level study data remain
private under the original consent terms, and historical
model answer texts were not archived. These limitations
constrain independent reproduction.
6. Experimental setup
6.1. Markets and companies
We evaluate on three independent emerging equity mar-
kets, each onboarded through the nine-sheet process of
Section 4.8 with two sectors and two companies per sector
(Supplementary Table S2). The two-sector, two-company
design keeps the slice small enough to audit end to end
while still exercising sector peer-baskets (needed by CQ3)
and cross-sector comparison.
6.2. Data sources and provenance
Each market integrates company fundamentals (annual
EPS and year-on-year profit growth), daily market windows
(close and volume around the reporting anchor), sector
peer-basket and broad-market benchmark comparators, a
daily local-currency/USD exchange-rate series, and official
annual-report announcements with disclosure references.
Fundamentals come from public annual-report summaries,
market and exchange-rate series from public historical price
sources, and announcement anchors from official exchange
disclosures; benchmark and sector-basket comparators are
transparent demonstrator constructions. PSX benchmark
rows declare interpolation/forward-filling, and MSX bench-
mark rows declare a damped selected-universe proxy, not
an official KLCI series. Their findings test stored-data
semantics rather than empirical market reactions. Every
row records its source, retrieval date, and field, carried
into the RDF provenance layer. Indonesia is the strongest
provenance case: its six daily series were downloaded from
a public endpoint andstrictly intersected on exact trad-
ing dates(no interpolation, forward-fill, or synthetic rows),
yielding 83 common trading dates spanning 2026-01-15 to
2026-05-29; one telecom constituent (TLKM) was replaced
by TOWR because its FY2025 results were released too
late for a completed post-event window, a decision recorded
in the bundle.
6.3. Tasks, metrics, and baselines
The original financial tasks are the five competency
questions of Section 3.1, executed on each market. The
additional public-data task applies the evidence-boundary
interface to a provider-month statistical screen rather than
reusing the financial ontology. It selects all eligible pub-
lished August 2026 records, not a sample chosen for pos-
itive findings. A source oracle and a separately written
source adapter parse the original CSV and workbook in-
dependently; neither imports the audit interpreter. Exact
aggregate counts, reporting month and source selectors are
comparedbeforethegeneratedRDFviewsareaudited. The
matched comparator executes an independently authored
SHACL-SPARQL constraint and availability/unit queries
on the same evidence boundaries. Primary outcomes are
source reconciliation, numerical status, same-witness unit
readiness and baseline agreement, not clinical accuracy,
human task speed or causal impact. Section 7.1 reports
10

population, missingness and adaptations. We report the
source-reconciled application and corrected contract eval-
uation first, followed by archived coverage, portability,
relational and structural controls, ablations, scalability and
the historical perception study (Section 7.9). Archived exe-
cution results refer to their recorded environment. Private
participant responses and missing historical model-answer
texts limit independent reproduction; they are not claimed
to be reconstructible from the public bundle.
7. Results and evaluation
7.1. Strengthened evaluation: corrected metrics and explicit
failure cases
Genuine public-data application: NHS waiting-time statis-
tics..The nonfinancial application reconstructs NHS Eng-
land’s August 2026 provider-level incomplete referral-to-
treatment (RTT) screen from its original CSV archive and
provider workbook [53, 54]. The publisher-defined ques-
tion is whether at least 92% of incomplete pathways are
within 18 weeks, not a hospital-quality ranking or a clinical
decision. The numerator sums eighteen weekly bands, 0–1
through 17–18 weeks; the denominator isTotal All. The
exact predicate isT >0∧ 100N≥ 92T, avoiding rounded-
percentage threshold decisions. AllPart_2, all-specialty
rows are included except commissionerNONC; commissioner
rows are aggregated once per provider and month. A dated
protocol preceded provider-outcome inspection, but is not
preregistration.
A source oracle independent of the RDF adapter and
checker reconciles all 532 eligible providers against the
publisher workbook: eighteen weekly counts, the numer-
ator and denominator agree exactly; stored ratios agree
within the fixed10 −12 tolerance in ratio units. Exact
cross-products classify 91 providers at or above 92% and
441 below. The workbook roster contains one additional
provider, D1V5N, with zero published denominator but no
selected CSV records. Its CSV-derived counts remain un-
available, rather than being zero-filled or interpreted as
a failed target or missing submission. The primary units
are 532 eligible provider-month records and one unavail-
able roster record, not three independent observations per
evidence pool.
The application-specific engineering is explicit: a new
source adapter, a two-role RDF vocabulary and contract,
and bounded fixed-integer scaling compiled into balanced
repeated addition. The existing bounded interpreter is
unchanged; no multiplication operator or financial ontol-
ogy reuse is claimed. Aggregation of the eighteen input
bands occurs in the recorded source adapter, not inside the
two-role interpreter. Generated evidence views contain the
deciding counts and selectors for original CSV rows and
columns, anchored by source-file hashes. These are our out-
puts over genuine source records, not publisher-provided ex-
planation bundles. The recorded selectors reference 242,934
source cells; this is neither that many independently col-
lected observations nor authenticated patient-level lineage.
All 533 application frames agree with an indepen-
dently authored, executed SHACL-SPARQL and explicit
availability/unit-readiness baseline on all three pools:
91 are positive, 441 false and one unknown. Complete
generated views deliberately carry the same deciding
observations across the three pools, so these are 533
matched frames, not 1,599 independent successes. The
baseline reuses identical within-frame pool results and
executes 533 actual SHACL validations. Its SPARQL
arithmetic uses explicitly sufficient Decimal precision;
this is disclosed comparator configuration, not a stronger
SHACL semantics. The generated dataset contains
18,095 RDF triples. These measurements show successful
technical execution and traceable deciding evidence, not
superiority to the matched baseline.
This establishes a reproducible externally specified sta-
tistical task and source-to-evidence traceability beyond fi-
nancial fixtures. The CSV and workbook share a reporting
collection, so their reconciliation is not independent data
collection. No natural reconciliation defect, independent
production deployment, clinical benefit or improvement in
human audit performance is established. Information reuse
follows the publisher’s OGL terms and exceptions; original
branded binaries are retained locally, not redistributed as
an endorsed NHS product [55, 56].
Requirement changes on the public-data application..A
separately recorded protocol replays six threshold/operator
policies on the same 533 NHS application frames. Only the
inclusive 92% screen is official; all alternatives are counter-
factual requirements, not changes to NHS policy or report-
ing errors. An exact-integer oracle computes expectations
from the existing adapter records. An independently pa-
rameterized direct comparator executes prepared SPARQL
queries with provider bindings. Both implementations cen-
tralize policy parameters; neither is forced to duplicate
manual edits. All provider identities, numerical statuses,
unit-readiness values and exact affected-provider sets agree.
Table 3 reports sensitivity; all policies preserve the same
unavailable roster entry.
Table 3: Policy replay on the same 533 frames. Only the inclusive
92% rule is official. Changes are counterfactual reclassifications, not
source errors.
Policy Positive Changed from official
Official≥92%91 0
Counterfactual≥90%118 27
Counterfactual>90%117 26
Counterfactual>92%91 0
Counterfactual≥95%67 24
Counterfactual>95%67 24
Fourteen constructed controls per policy exercise equal-
ity, missing evidence, shared months, delivered omission
and same-witness units, including 252 actual SHACL pool
validations; cohort SPARQL execution is not counted as
SHACL validation, and repeated policies do not enlarge
the independent sample. Re-executing the official policy
11

restores every status/readiness result, and source-derived
records, earlier outputs and implementation files retain
their recorded hashes with no core-interpreter edit. This
is deterministic replay, not stateful deployment rollback.
An initially unbound query attempt was interrupted be-
fore completing a policy; its retained note documents the
switchtoprovider-boundevaluationofthesamequerytexts.
The experiment establishes bounded change-conformance
and affected-result traceability. The direct implementa-
tion succeeds equally, so reduced authoring effort, superior
maintainability and practitioner benefit do not follow.
Declarative evidence-boundary diagnostics..The additive
interpreter of Section 3.5 executes twenty constructed sen-
sor cases with independently specified ambient, support
and delivered labels. All sixty pool-level results agree
with those expectations and with a separately authored
SHACL-SPARQL positive-witness constraint plus availabil-
ity queries. The comparator independently reconstructs
pool membership from the fixture RDF; it does not reuse
the interpreter’s selections. Its coverage is the sensor OR
configuration and ordinary-decimal lexical inputs, not all
financial predicates, metadata readiness or arbitrary RDF
numeric terms. Agreement establishes functional parity on
this diagnostic subset, not better accuracy or expressiveness
than SHACL-SPARQL.
A second, independently specified analytical suite closes
part of that coverage gap. Twenty-six constructed cases
yield 78 paired pool comparisons with no numerical-status
or unit-readiness disagreement against explicit expecta-
tions and manually authored SHACL-SPARQL/availability
queries. All four financial finding families are exercised
through the full audit entry point, including conjunctions,
absolute values, addition, shared-window joins, typed role/-
path decoys and invalid bundle associations. R3 uses an
explicit diagnostic margin of one percentage point without
modifying the frozen zero-margin configuration. A passing
but unit-unqualified witness cannot borrow units from a
qualified nonpassing alternative; adding a qualified pass-
ing alternative does establish readiness. Three regression
methods check the suite, a wrong-label failure guard and
this witness-coherence case. The comparator independently
selects its observation pools from RDF.
Primary parity is restricted to the tested short-precision
decimal fixtures (at most five significant digits and four
decimal places), not general numeric equivalence. A sepa-
rately retained precision stress case lies outside that subset:
with sector2.00000000000000000000000000001, company
3.00000000000000000000000000001and margin one, exact
replay is false but the default-precision RDFLib SPARQL
comparison is positive due to addition rounding. This
mismatch is recorded separately, not silently discarded or
counted among the 78 agreements. Increased comparator
precision can address this example; it is not a SHACL
expressiveness limitation. The expanded diagnostics re-
main constructed workload evidence, not a new empir-
ical sample or a proof of conceptual novelty. Queries,
parameters, hashes and outcomes are released separately
inboundary_analytical_v1/.
Table 4: Selected constructed evidence-boundary cases. These are
examples from twenty diagnostics, not observed failure frequencies;
metadata remains ambient.
Controlled change Ambient Support Delivered
All deciding observa-
tions included
Positive Positive Positive
Removedeliveredobser-
vations only
Positive Positive Unknown
Deliver only nonpassing
candidates
Positive Positive False
Remove declared sup-
port only
Positive Unknown Unknown
Seven additional regression methods exercise the di-
agnostic suite, unit readiness, bundle association, invalid
configurations, enumeration bounds, all four financial con-
figurations, incompatible joint windows and exact addi-
tion/absolute value under reduced ambient Decimal pre-
cision. These tests are not an external comparator for
every supported expression. The same interpreter con-
sumes financial and synthetic sensor vocabularies without
code changes: that synthetic experiment alone establishes
configuration-level reuse, not real-domain validation; the
NHS application is reported separately. Single-run diag-
nostic timings include comparator setup and are not used
to claim a speed advantage.
A separate paired replay evaluates the frozen financial
experiment pools with the declarative numerical interpreter.
All 487 existing records agree on support/delivered sta-
tus and ambient truth. This comparison uses direct pool
evaluation, explicit in-memory company-to-index lookup
adapters and the frozen R4 event scope; it does not test new
bundle-link selection, metadata readiness or source-path
parity. Input hashes remain unchanged. The records are
overlapping archived/corrected experiment versions, not
an additional independent sample. Diagnostic and paired
results are recorded separately inboundary_audit_v1/
andboundary_legacy_parity_v1/.
Actual stored-release evidence omissions..The audit en-
try point is also run on the actual original and repaired
three-market releases, not only on constructed findings.
Original bytes retrieved from a fixed Git commit and re-
paired files match their preceding release-audit hash ledgers.
Explicit in-memory adapters link findings to already ex-
isting generated bundles and expose the archived implicit
index lookup; no numerical value, support link or bundle
member is repaired by the adapter. Support and delivered
sufficiency are 19/21 in the original release and 21/21 af-
ter repair. Exactly the two previously documented PSX
R4 volume omissions change from unknown to positive.
These are 21 paired findings, not 42 independent examples,
and the experiment requires the recorded source history
rather than the source-only review ZIP alone. Original R4
event identity is insufficient for independently anchored
12

ambient replay, so ambient positives are not treated as
event-specific truth guarantees. The synthetic matched
baseline is a separate experiment, not a comparator run
on these release findings. Results and adapter details are
recorded inboundary_release_replay_v1/.
Financial fixture recomputation and qualification..The
archived results reported later remain historical controls.
A separate financial-v2 release recomputes company, sector
and benchmark price returns by compounding consecutive
close-price intervals over exactly the same company dates.
Missing comparator endpoints produce an incomplete re-
sult, not a silently shortened window. These are price
returns, not authenticated dividend-adjusted total returns.
Event CAR is now explicitly the sum of supplied company
daily returns minus same-date benchmark returns, in per-
centage points; missing operands are incomplete. Volume
ratios retain legitimate zeros and disclose baseline overlap.
FX association uses identical intervals with at least three
pairs. Growth uses matching current/prior profit fields
where available, with an absolute prior-value denomina-
tor; supplied growth otherwise remains explicitly identified.
Currency context is separate from metric units. This revi-
sion does not change archived workbooks or graphs.
Across four corrected datasets, 404 metrics were re-
computed and 17 marked incomplete; 5,237 supplied daily-
return/adjacent-price checks agree. A bounded primary-
source spot audit found monetary scaling errors in EN-
GROH and FFC workbook fields. Eight reviewed cells
now carry separately recorded normalized values, multipli-
ers and source citations; the raw cells remain unchanged.
Common scaling may cancel in a growth ratio but does
not make the monetary extraction accurate. This audit
does not authenticate all prices, financial facts, dates or
upstream derivations.
Expanded evaluation enumerates all company classifi-
cation cases rather than inspecting positives alone. The
corrected 64-company cohort contains 42 numerical posi-
tives, 147 negatives and three incomplete cases for R1–R3;
its 64 event classifications are separately not applicable be-
cause event observations are absent. The corrected curated
cohorts contain 16 positives. Curated IDX overlaps the
scaled cohort, and original/corrected datasets are paired, so
these counts must not be summed as independent samples.
R2 remains a classification test, not validation of the entire
CQ2 answer.
Original unbound CQ1/CQ3 queries evaluated on com-
plete graphs agree with an independent Decimal traversal
for all 16 dataset/query result sets. Separate experiment
findings and actual bundles replay all enumerated classifi-
cations. Removing decisive evidence yields the expected
response in 122/122 corrected scaled-cohort and 38/38
corrected curated-cohort variants; an independently suffi-
cient OR branch remains valid. Eleven synthetic bound-
ary/branch controls are reported separately from natural
cases. These checks establish stored-data semantics, not
external financial truth.
A subsequent categorical-accounting run preserves every
input hash and numerical cohort count while checking sta-
tusaswellasbinarysufficiency. All487replayrecordsagree
on positive/sufficient/true, negative/predicate-false/false
or incomplete/incomplete-bundle/unknown status, under
the explicitly tested R4 missing-branch convention. All
sixteen complete-query comparisons and 330 withholding
variants across the paired cohorts agree. These totals
include overlapping versions and constructed experiment
bundles, not 487 independently collected findings or 330
natural observations. Seventeen synthetic graph configura-
tions separately exercise categorical and branch behavior.
Frozen v1 artifacts remain unchanged; the stricter run is
recorded inexpanded_evaluation_v2/.
An independent metadata audit checks role-specific
units, comparator currency contexts, R1 report-to-window
linkage and R4 explicit event-window linkage. Only 22/42
scaled positives and 15/16 curated positives satisfy all
applicable declarations. Twenty scaled R1 cases use a
recent-analysis anchor different from their recorded report
date. Curated TOWR records 18 March 2026 as the report
date but 25 March as the window anchor. They remain
numerical positives, not validated report-anchored findings.
Dates are not rewritten to manufacture agreement. Five
synthetic metadata controls pass; archived cases without
required declarations remain unverified. Declaration con-
sistency is weaker than date authenticity or knowledge of
announcement time.
Source qualification beyond arithmetic..Stored-data re-
play, matching declarations and authentic source inputs
are separate claims. Versioned repairs now authenticate
twelve OGDC/PPL annual facts: eight monetary cells agree
only after a factor of one million corrects their declared
thousand-PKR scale, while four EPS cells match directly.
The original wrong-period links and raw workbooks remain
preserved. FY2024 values are checked as FY2025 com-
parative columns, not against separate original releases.
Company/separate and unconsolidated accounting scopes
are retained. Growth ratios remain unchanged because
common scaling cancels, but this does not validate mone-
tary unit labels.
The supplied PSX comparator declares interpolation
and forward-filling, and MSX declares a damped selected-
universe proxy rather than official KLCI data. Their classi-
fications are illustrative predicate tests, not authenticated
market reactions. Authentic KSE100 total-return levels
cannot substitute for KSE100PR in a company price-return
comparison. A PSX company-page definition applies only
to that feed, not automatically to original SECP closes
or other providers. Maybank’s unexplainedunadjusted
=0 parameter is not treated as an adjustment definition.
Corporate-action review remains incomplete.
Systematic dependency coverage..An executed audit of
the frozen 52-case, 29-stratum frame enumerates 2,357
unique recorded workbook-cell inputs. Of these, 2,271 have
13

Table 5: Current source-backed evidence and its limits. Counts
describe different units and overlapping subsets; they are not an
independent sample total.
Evidence Executed coverage Remaining qualifica-
tion
OGDC/PPL
annual facts
12 facts across two
companies and two
year columns
Eight require scale
correction; scope
and comparative-
year limits remain
Maybank
company
closes
32 required dates
present; all 30
archived post-report
closes match
Issuer republication;
adjustment conven-
tion unresolved
SECP PSX
reports
Fouroriginalreports;
six KSE100 levels
and two FFC closes
KSE100 total return
is not a price-only
benchmark; FFC
baseline missing
Disclosure
dates
Two official dates
match FFC/May-
bank anchors
Document/annual-
report dates do
not establish
first earnings-
publication times
Source-
backed
comparisons
Two existing cohort
subsets replayed;
zero eligible market-
relative comparisons
Missing compatible
benchmarks, defini-
tions and baseline
coverage; labels
withheld
Frozen
source sam-
ple
52 cases; 2,357
unique recorded
workbook-cell in-
puts
Zero cases have com-
plete reviewed cov-
erage under the all-
recorded-input pol-
icy
recorded lineage but no independent review, 46 are declared
proxies, and two reconstructed KSE100 values disagree with
original regulator observations. The workbook records
157,496.1 for both 12 and 13 March 2026, whereas the orig-
inal report’s explicitly dated columns give 154,421.43 and
153,866.17. Theremaining38inputshavedifferentbounded
qualifications: four exact scale-corrected PAT values, two
rounded narrative agreements, thirty issuer-republished
Maybank closes with unresolved adjustment basis, and
two regulator numeric agreements without transfer of the
workbook’s basis. These are not equivalent authenticity
statuses.
No sampled case has complete independently reviewed
coverage under the conservative all-recorded-input policy.
This is not a claim that all cases are false, nor a minimal
sufficient-branch AND/OR proof or population accuracy
estimate. Dependencies are deduplicated by exact work-
book/hash/sheet/row/field identity; overlapping datasets
and repeated cells are not independent observations. The
six newly verified PPL facts fall outside this frozen depen-
dency selection and are not added to its coverage count.
OGDC review uses a separate repair overlay and does not
silently fix historical graph source links. Thirteen asser-
tions check the frozen frame, graph/source hashes, joins
and coverage accounting. The result qualifies the paper as
a semantic-contract and provenance evaluation on explicit
financial fixtures, not a source-authenticated empirical mar-
ket study.
Temporal eligibility and bounded recomputation..All 20
scaled R1 positives are quarantined from report-event use
because their workbooks explicitly identify recent-analysis
windows and use fiscal year-end as a purported report
date. Curated TOWR’s 18/25 March mismatch is also
quarantined. The 22 retained scaled positives are non-R1
classifications, not authenticated earnings events. Among
all eight PSX/MSX candidates, three numerical R1 posi-
tives and five negatives are retained in the ledger; only FFC
and Maybank match official document/annual-report dates.
Four lack matching verified dates and OGDC/PPL lack
September 2025 price coverage for their corrected annual
sources.
The two matched cases contain 30 post-disclosure
closes and 29 observed intervals. Recovered company-only
endpoints can support descriptive arithmetic, but not a
complete initial-reaction baseline or a compatible market-
relative result. The consolidated source-backed replay
therefore leaves both market-relative labels unknown,
rather than converting missing evidence into negative
findings. These two cases overlap earlier cohorts and do not
increase the independent sample. Detailed formulas, values,
field/page locators, source hashes, acquisition failures and
successive repair stages appear in the supplement and
versioned ledgers. Original graphs remain unchanged; no
market data are silently interpolated or substituted.
14

7.2. Executed external provenance comparison
Weexecutedthepublished, unmodifiedNPCSStandard-
reification JAR at archived revisionb95bff3b56587b2a9e
f6655503aada19c844630d. Original and rewritten queries
use the same Oxigraph engine. For 1,044 observation tu-
ples, tuple multisets agree and each native provenance poly-
nomial identifies exactly four expected supporting facts.
For the full 15-pattern CQ3 basic graph pattern, all 12
candidates agree and each polynomial identifies exactly
15 facts. Explicit numerical post-filtering produces the
archived PSX/MSX/IDX selections of 2/0/2; contract in-
terpretation agrees on four positives and eight negatives.
The native numerical-FILTER rewrite was also tested:
the emitted query double-reifies object patterns, omits the
provenanceprojectionandreturnszerorowsontheseinputs.
Generated queries are retained. Consequently this is a
genuine external BGP provenance comparison with explicit
analytical post-processing, not an unmodified end-to-end
CQ3 benchmark or evidence of general superiority. NPCS
provides query-support lineage; contracts add application-
specific interpretation. The earlier constructed corruption
suite remains a policy ablation and must not be attributed
to NPCS. Single-run timings are descriptive, not a speed
ranking.
7.3. Objective human evaluation: prepared, not executed
The historical 17-person study measures perceived trust
and completeness only. A separate objective protocol now
provides 12 distinct company/window audit tasks: four
supported, fourcontradicted, andfourwithinsufficientcom-
parator evidence. Two displays contain identical facts and
source appendices, differing in role organization; neither
reveals a validator verdict. Four sequences counterbalance
display and order. Each participant sees each case once,
with six tasks per display and balanced truth categories.
Outcomes are decision accuracy, source-identification ac-
curacy and completion time, analyzed at participant level
with paired differences and participant bootstrap inter-
vals. Consent/ethics coverage, sample-size justification,
allocation and any preregistration must be settled before
recruitment. Packets and analysis software exist, but no
new participants or responses have been generated. Ob-
jective audit improvement is therefore an open empirical
question. Public provenance-interaction records can inform
secondary analysis and task design but cannot estimate the
effect of these displays without participants using them.
7.4. Competency-question coverage and governance
We first verify the governance invariant. Introspecting
the core ontology yields 24 classes, 22 object properties,
and 23 datatype properties; together with the 9 derived
metrics and 15 SHACL shapes,every term maps to at
least one competency question, with no uncovered
terms(the check is mechanical and ships in the bundle).
Conversely, each competency question is answerable end to
end: executing the five SPARQL templates returns results
on at least one market for every family. The ontology is
thus both sufficient (answers all CQs) and disciplined (no
term without a CQ). We claim traceability and controlled
growth, not formal ontological minimality.
7.5. Portability across three markets
Across PSX, MSX, and IDX,13 core artifacts are
reused byte-identical: the core ontology, project, and
alignment files, the SHACL shapes, the five CQ templates,
the inference rules and findings vocabulary, the unified
builder, and the inference/explanation generator. That is
100% of the ontology, shapes, queries, rules, and
code logic. Only the nine data sheets and a single adapter
record (Supplementary Table S1) differ per market. We
are explicit about what this does and does not show: each
market’s raw sources are firstmapped by hand into
the common nine-sheet schema, and only then is the
apparatus reused unchanged. The 100% figure therefore
measures reuse of the ontology, shapes, queries, and rules
over an already-aligned representation, not automatic inges-
tion of arbitrary raw data (onboarding a genuinely different
reporting structure would require new source mappings
whose effort we have not measured; Section 9). Table 6
reports the per-market outcomes under this identical appa-
ratus.
All three markets conform to the same SHACL shapes
and answer the competency questions with traceable ex-
planations. PSX and IDX, built independently, happen to
share the same CQ resultshape(0/4/2/6/3). With only
four firms per curated market, we read this asillustrative
rather than strong statistical evidence, resting the portabil-
ity claim on the byte-identical apparatus (100% reuse) and
the 64-stock scaled run (Section 7.5.1). The non-empty
cells are real analytical answers over demonstrator compara-
tors (all quoted returns are demonstrator quantities, not
licensed estimates, Section 8.2): for example, CQ3 on PSX
returns OGDC (+8.11% > sector +7.28% > benchmark
−9.11%) and ENGROH, CQ1 on MSX returns MAXIS
(+11.82% year-on-year profit growth but−6.31% return
versus a +0.16% benchmark), and CQ3 on IDX returns
ISAT and BMRI. Empty cells are honest data outcomes,
not failures. In a falling Jakarta market the large caps all
beat their benchmark, so CQ1’s set is empty, and different
families are non-empty across markets because the data
differ while the method does not.
7.5.1. Scaling to a 64-stock cross-section
To show the method is not confined to small demonstra-
tor slices, we scaled the Indonesia market to a64-stock
cross-sectionspanning11GICSsectors, acquiredfrom
public daily data over a common 2026-03-26 to 2026-06-29
window (real prices and volumes, the Jakarta Composite,
and USD/IDR, plus two years of fundamentals per stock for
year-on-year growth). The unchanged pipeline materialized
a 37,046-triple graph that is SHACL-conformant, and the
competency questions return substantive cross-sections: 17
15

Table 6: Three markets, one unchanged pipeline. CQ columns report the number of result rows. The CQ2 count isstructural(one exchange-
rate-association row per company by construction,≈one per firm), not a data-dependent outcome. CQ1/CQ3/CQ4 can legitimately return
empty. All quoted returns are demonstrator quantities (Section 8.2), and "benchmark return" is measured over each company’s own window.
Market RDF triples SHACL CQ1 CQ2 CQ3 CQ4 CQ5 Findings
PSX (KSE-100) 4,065 Conforms 0 4 2 6 3 9
MSX (Bursa) 2,618 Conforms 2 4 0 0 3 2
IDX (Jakarta) 4,185 Conforms 0 4 2 6 3 10
companies with positive reported growth yet a post-window
return below the−19.4% Jakarta Composite benchmark
(CQ1, on thesignof year-on-year growth at this scale; see
the caveat below); 24 companies that outperform both their
sector and the benchmark (CQ3, e.g. MAPI +31.6% vs sec-
tor +13.4% vs benchmark−19.4%); 63 FX-association rows
(one per company; one stock lacked sufficient overlapping
FX-returnobservations, so63of64)(CQ2); andtheexplain-
ability query (CQ5). Event-window observations (CQ4)
are not generated at this scale because per-stock announce-
ment anchors were not collected, so CQ4 remains exercised
on the curated four-stock set. The 64-stock demonstration
therefore exercises CQ1 (sign-restricted), CQ2, CQ3, and
CQ5 at scale. The two multi-join queries (CQ1, CQ3)
exceed RDFLib’s in-memory nested-loop engine at this
size (Section 7.8). We therefore executed theunchanged
SPARQL templates on a standard triplestore (Oxigraph),
where CQ1 returns its 17 rows in≈4 ms and CQ3 its 24
rows in≈5 ms over the full 37,046-triple graph (medians;
Supplementary Table S5) (the complete CQ1–CQ5 triple-
store latencies are reported in Section 7.8). These match
the counts from directly evaluating the same conditions
over the derived metrics, so the cross-sections come from
the system’s own query layer, not a bypass. One data
caveat: Yahoo-derived year-on-year net-income growth can
be extreme on small or recovering bases (a few firms exceed
several hundred percent), so CQ1 uses thesignof growth
rather than its magnitude; representative moderate cases
include CPIN (+52%) and JPFA (+33%). This removes
the small-demonstrator concern with the ontology, shapes,
queries, and rules byte-identical. The acquisition script is
released in the bundle.
7.6. Excluded historical measurements
The historical eight-model experiment supplied struc-
tured evidence to instruction-tuned language models and
scored their textual transcription, with retrieval held fixed.
The archived notebooks and score tables do not contain
the generated answer texts needed to apply the current, dif-
ferently defined scorer, so we exclude the historical model
ranking and make no quantitative claim from it. Historical
timings compared deterministic rendering of precomputed
answers with model generation on different hardware; these
are different tasks and establish no efficiency advantage.
Query-layer performance is assessed in Section 7.8. A re-
producible future transcription experiment must archive
each answer, input bundle, source identity, prompt, model
revision and scorer version.
7.7. Component-removal ablations
Component removal tests characterize implementation
dependencies. Removing evidence links reduces the histori-
cal evidence-availability score; removing rules removes the
findings produced by those rules; and removing bundles re-
moves bundle-query output. These outcomes establish that
the implementation uses the removed components. They
do not compare OntoKG-EQ with a capable provenance
system or establish that relational stores cannot provide
those functions.
Stronger final-graph interventions are reported in Sec-
tion 7.11.
7.8. Scalability
Replicating a market graph with constant schema and
multiplied instances, SHACL validation scales near-linearly
on RDFLib (≈0.11 s per 1k triples) and the single-pattern
competency questions stay flat, but the two multi-join
analytical queries (CQ1, CQ3) degrade sharply under RD-
FLib’s in-memory nested-loop join (not completing within
two minutes on the 37k-triple graph). This is anenginelim-
itation, not a method one: loading the 64-stock Indonesia
graph (37,046 triples) into a standard triplestore (Oxigraph
[57]) and running theunchangedSPARQL templates, all
five competency questions return in single-digit millisec-
onds (Supplementary Table S5). The scaled cross-sections
of Section 7.5.1 are therefore produced by the system’s
own query layer on a real triplestore, byte-identical to the
RDFLib configuration.
7.9. Historical exploratory perception study
Across the three curated markets the inference layer
derives 21 findings (9 PSX, 2 MSX, 10 IDX), each with
a generated explanation bundle. The final-graph audit
separates explicit dependency completeness from structural
conformity and source attribution. The original user study
evaluates the presentation of evidence-enriched displays
rather than validating every provenance link or financial
computation.
We conducted an exploratory within-subject perception
study.
Seventeen respondents(6 finance professionals, 5
academics, 3 students, 3 others; self-reported roles) each
rated8OntoKG-EQ statements first as a result-only note
(Version A) and then as thesamestatement with its
provenance-grounded evidence bundle (Version B), on ad-
hoc 7-pointtrust(informed conceptually by [58], not an
16

adaptation of its scale) andjustification-completenessrat-
ings, and chose a preferred version. Analysedat the
participant level(one mean per condition, n = 17, avoid-
ing pseudoreplication of the 136 item ratings), mean trust
ratings were higher for Version B by +2.87 (2.93→ 5.79;
participant bootstrap 95% CI [2.10, 3.52]; exact Wilcoxon
signed-rank p≈ 7.6×10-5), as were perceived-completeness
ratings by +3.35 (2.10→ 5.44; p≈ 6.1×10-5, n = 16 non-
zero pairs);16 of 17 preferred the evidence-grounded
version on all eight items, and all 17 on a majority
(sign test p≈ 1.5×10-5), with the same direction in the
finance-professional subgroup (six respondents; exploratory
trust∆= +3.42). Table 7 reports the overall panel, not a
separate subgroup test. These results show higher reported
trust and perceived completeness for the richer display
in this panel; objective verifiability and calibrated trust
were not measured. Because each item presents Version
A before the more-detailed Version B, part of the lift may
reflect added information or order rather than provenance
grounding specifically (Section 8.2). We therefore report
this as exploratory evidence of participant preference un-
der this presentation protocol, not a definitive causal or
professional-performance result.
Table 7: User study (n = 17; 8 real OntoKG-EQ statements; 7-
point scales; within-subject, Version A = result only, Version B
= same statement with its evidence bundle). Analysis is at the
participant level (one mean per participant per condition) to avoid
pseudoreplication.
Measure A (mean) B (mean) ∆(95% CI,
participant
bootstrap)
Test
(participant-
level, ex-
act)
Trust 2.93 5.79 +2.87 [2.10,
3.52]
Wilcoxon p
≈ 7.6×10-5
(n = 17)
Completeness
of justifica-
tion
2.10 5.44 +3.35 [2.61,
4.00]
Wilcoxon p
≈ 6.1×10-5
(n = 16)
Preferred
version —
B on all 8
items / on
a majority
— 16/17·17/17 — sign test p
≈ 1.5×10-5
7.10. Additional robustness checks
The following checks examine structural errors, execu-
tion scale, and numerical transformation separately.
Fault-injection.Injecting eight realistic data faults
one at a time into a valid, SHACL-conformant graph
(wrong-typed values, missing names, subjects, and sources,
malformed dates, a wrong reporting-period link, and a du-
plicate value),SHACL detected all 8/8(Supplementary
Table S6), genuine error-detection evidence rather than a
definitional dependency.
Controlled scaling.To probe scaling beyond the
64-stock graph we replicated it (distinct instance IRIs) to
larger sizes and re-ran theunchangedCQ1/CQ3 templates
on the Oxigraph triplestore (Table 8). Ingestion is near-
linear (~13 s per million triples). The single-pattern queries
(CQ4, CQ5) stay flat, while the two multi-join queries grow
with the size of their result set, which itself grows with
the graph, yet remain sub-second at ~106 triples. These
measurements characterize the archived SPARQL query
workload on replicated data, not the new contract checker
or source-lineage generation. The in-memory reference
engine remains a limit for this evaluated workload. (Full-
universe throughput, concurrent load, and 107–108 triples
on a clustered store remain future work.)
Table 8: Controlled scaling on Oxigraph (replicated 64-stock IDX
graph; unchanged CQ1/CQ3 templates; on-disk Oxigraph store, so
base-size latencies exceed the in-memory Supplementary Table S5
figures; representative run).
Triples Ingest (s) CQ1 latency (ms) CQ3 latency (ms)
37,046 0.2 9.4 11.9
111,130 0.8 31.8 39.4
1,111,264 14.4 468.6 690.5
Fidelity audit.The revised independent check reads
actual stored graph literals and compares them with arith-
metic sums recomputed directly from the source daily re-
turns. All 64 company window statistics match within10−6
percentagepoints, withmaximumabsoluteerror4 .98×10−7
percentage points, consistent with six-decimal serialization.
Node coverage and company association are also checked.
The earlier script compared two source-sheet calculations
without reading the graph; the revised audit repairs that
verification gap. The check covers these company statistics
only, not all financial metrics or original-source authentic-
ity.
7.11. Archived-graph dependency control
This subsection and the following legacy contract, cor-
ruption and financial requirement-change experiments use
archived metric conventions. They are historical controls,
not thecorrected primary financial evaluation in Section7.1.
Their counts must not be combined with corrected-cohort
counts. The revision evaluates the original and repaired
final graphs separately, recording input hashes and package
versions. All three original final graphs conform to the
existing SHACL shapes, yet two PSX R4 findings omit
the abnormal-volume observation that caused the rule to
select them. After including that observation and regener-
ating the finding bundles, all 21 findings across PSX, MSX,
and IDX pass the additional checks of declared supports,
matching windows, rule predicates, and bundle consistency.
Final SHACL conformance also holds for all three repaired
graphs.
Five controlled interventions preserve the surrounding
RDF graph and contextual evidence. The existing shapes
detect none of these five changes. The additional depen-
dency audit detects a numeric change that falsifies the
selection predicate, a swap to an existing but mismatch-
ing analysis window, and removal of one required bundle
observation. Neither check detects a plausible numeric
perturbation that preserves the predicate or a well-formed
17

wrong source assignment. A known-original snapshot iden-
tifies all five changes, but this is an intervention oracle, not
independent validation of source truth.
The repaired graphs contain 45 distinct declared sup-
porting observations across the three markets. These are
not all necessary operands: an OR condition can have alter-
native witnesses and attached context. All have temporal
context, but the base graphs contain no explicit observation-
level source or derivation links for these observations. Their
company announcement links provide context, not com-
plete numeric lineage. A separate workbook-lineage overlay
is evaluated as a revision artifact; it must not be conflated
with original-source authenticity. The dependency checks
cover materialized positive findings, not false negatives,
every possible CQ answer, or arbitrary derivations.
7.12. Canonical relational reuse control
The revision implements one constrained SQLite
schema, one CQ1 query, one CQ3 query, and one evidence-
dependency join without market-specific rewrites. SQL and
SPARQL return exactly matching sets, including numeric
values, across PSX, MSX, and IDX. CQ1 row counts are
0, 2, and 0; CQ3 counts are 2, 0, and 2; dependency-join
counts are 19, 6, and 20 respectively. Numeric CHECK
and unknown-entity foreign-key corruption tests are
rejected in each database. Schema, query, and input
hashes are recorded.
This control imports the same stored graph metrics. It
verifies query and join agreement, not independent financial
correctness, and empty sets provide weaker evidence than
exercised positive cases. Contextual announcement/source
joins are retained without treating them as complete nu-
meric provenance. A relational implementation can thus
provide constraints, provenance tables, materialized find-
ings, evidence joins and reuse after canonical mapping
(Table 9). We make no claim that RDF uniquely enables
these functions or reduces engineering effort; OntoKG-EQ
expresses them with shared semantic vocabularies, graph
identifiers, SPARQL and declarative shapes.
Table 9: Capabilities available in both representations. This compar-
ison describes implementation choices, not measured superiority.
Dimension Relational imple-
mentation
OntoKG-EQ
CQ1/CQ3 results Same results on
evaluated inputs
Same results on
evaluated inputs
Structural con-
straints
CHECK and
foreign-key con-
straints
SHACL shapes
Result evidence Tables and explicit
evidence joins
EvidenceBundle
and graph links
Derived findings Rows or material-
ized views
Typed finding indi-
viduals
Reuse after canoni-
cal mapping
Demonstrated with
one schema
Demonstrated with
shared semantic ar-
tifacts
Representation Relational schema
and SQL
RDF vocabulary
and SPARQL
7.13. Workbook-cell lineage overlay
A separate PROV overlay links value-matched obser-
vations to exact workbook fields identified by file SHA256,
worksheet, cell address, row identifiers, and explicit source-
register identifiers. Source-register URLs are recorded
rather than treated as authenticated sources. Recomputed
dependencies follow the actual implemented calculations;
numerical agreement is required before a mapping is emit-
ted.
Of 522 PSX observations, 500 have value-matched map-
pings; the corresponding counts are 319/321 for MSX,
542/542 for IDX, and 4944/4947 for scaled IDX. Every
mapped dependency cell has an explicit source identifier re-
solving to one register row. The 27 unresolved observations
across these datasets include values defaulted from missing
input cells, and they remain explicitly unresolved. For
observations explicitly supporting the 21 repaired findings,
44/45 map to workbook cells and source-register identi-
fiers (PSX 18/19, MSX 6/6, IDX 20/20). The remaining
PSX event statistic is zero despite having no supplied
event-return cells; its numeric provenance is unresolved.
These results establish workbook-level traceability for the
mapped observations, not accuracy of original sources or
independently verified upstream construction. Correlation
mapping uses the existing Pearson helper and is not an
independent test of that helper’s analytical correctness.
7.14. Executable contract and bundle replay
The contract checker independently interprets the four
declared finding predicates over typed observations and
actual explanation bundles. All 21 inspected findings (9
PSX, 2 MSX, 10 IDX) have sufficient declared support and
a sufficient witness in the correctly targeted bundle. Under
this bounded definition, the complete-bundle rate is 21/21.
Each bundle also has at least one sufficient witness whose
recorded dependency cells have consistent source identifier
paths. This does not mean all 45 declared supporting
observations have source mappings: one unresolved zero-
valued event statistic is unnecessary for a passing volume-
only R4 witness.
Six synthetic regression tests cover inclusive correlation
thresholds, strict comparison boundaries, missing compara-
tors, same-valued wrong-role observations, volume-only OR
evidence, and bundle-only evidence loss. Decimal arith-
metic preserves lexical decimal boundaries, including a CQ3
company value of 1.1 against a comparator of 0.1 with a one-
point strict margin. Source truth, absent unit declarations
and the unlinked temporal anchors identified in Section 3.4
remain unverified. Status and witness triples are written as
separate overlays, with graph, contract, query, rule, shape
and implementation hashes recorded in machine-readable
outputs.
7.15. Controlled semantic corruptions
The expanded suite includes 12 deliberately selected
PSX corruptions and two controls. Every corrupted base
18

graph conforms to the existing SHACL shapes. Finding-
condition replay flags seven corruptions; checking the actual
bundle flags eight; the combined condition, bundle and
recorded source-path policies flag ten. The controls accept
the original positive finding and a volume-only sufficient
R4 witness. These counts describe selected interventions,
not a detection-rate estimate for naturally occurring errors.
The cases include another valid company or analysis
window, a missing comparator, bundle-only comparator
loss, a wrong metric with its numeric value unchanged,
threshold equality, a result satisfying only one of CQ3’s
two comparisons, absent support, a broken source path
and an inconsistent source identifier. A plausible numeric
perturbation preserving the predicate remains undetected,
as does a false source attribution whose source edge and
identifier are changed coherently. Independent calculation
or trusted source comparison is required for those defects.
Currency/unit corruption is not evaluated because the
observations lack the necessary explicit metadata.
The comparison retains the same RDF evidence while
enabling or disabling these checking policies. It is a policy
ablation, not a head-to-head benchmark against NPCS or
another provenance implementation. A separate AND-to-
OR query edit is identified by artifact hash drift; valid
stored witnesses alone do not reveal which query version
generated them.
7.16. Bounded requirement change and replay
We change CQ3 from exceeding both same-window
comparators to exceeding both by strictly more than one
percentage point. Versioned query, documented-rule and
contract artifacts preserve the old and new predicates. The
new SELECT and CONSTRUCT results agree with an
independent imperative traversal of the same observations:
PSX changes from two selected companies to one, IDX from
two to one, and MSX remains empty. All four archived R3
finding supports replay consistently with the corresponding
old/new selection conditions.
Five synthetic boundary cases yield three original se-
lections and one revised selection; equality at either strict
threshold is excluded. These fixtures are not market obser-
vations. Replaying the archived original query reproduces
its results, while pairing it with the changed contract fails
the expected query hash. CQ1, CQ2 and CQ4 are read-only
same-snapshot controls with unchanged results; they do
not establish general regression freedom. Artifact impact
is declared for this threshold edit using manifest paths,
rather than inferred by a general change-impact algorithm.
The production inference code and market graphs remain
unchanged; adopting the revised threshold would require
deploying the corresponding inference version.
8. Discussion and threats to validity
8.1. Interpretation
The central result is a bounded executable connection
between analytical conditions and sufficient typed evidence
in actual finding bundles. The NHS application shows that
this connection can be applied to an externally specified
public statistical task with source reconciliation and explicit
missingness. The semantic corruption suite demonstrates
distinctions that the existing shapes do not encode, while
the financial margin and NHS policy replays demonstrate
reproducible evaluation of declared requirement changes.
These are task-specific checks, not new general provenance
or ontology-reasoning algorithms. Reuse of shared arti-
facts after canonical mapping remains useful engineering
evidence without establishing automatic interoperability or
reduced onboarding effort relative to a canonical relational
schema.
The intended benefit is inspectability with explicit fail-
ure states: insufficient roles, an incomplete actual bundle,
and inconsistent recorded source paths can be reported
separately. The 21/21 sufficient-witness result covers in-
spected positive findings under declared predicates, not
false-negative discovery, original-source authentication, or
full verification of every temporal and unit assumption.
Matching result counts across curated slices do not estab-
lish generality, and perceived trust should not be inter-
preted as calibrated trust or improved professional audit
performance.
8.2. Threats to validity
Construct validity.The derived metrics are standard
analyst proxies. The sector peer-baskets and broad-market
benchmarks are transparent demonstrator constructions,
documented per market, not licensed index feeds. The
CQ4/CQ2 thresholds (|CAR|≥ 2%, volume ratio≥ 1.5,
|correlation|≥ 0.3) are fixed a priori as an operational
screen informed by event-study practice [50, 51, 52] and
are not tuned to the data. Sector comparators are equal-
weighted demonstrator baskets, event dates anchor on the
reported announcement date without special after-hours
handling, and closes are unadjusted for corporate actions.
These are documented demonstrator simplifications, to be
replaced with licensed, adjusted feeds before any empirical
market claim.
Internal validity.Deterministic execution and
SHACL gating do not establish independent source
accuracy. The boundary benchmark is constructed to
isolate known failure modes; it does not estimate their
natural prevalence. The first matched comparator covers
the synthetic sensor OR configuration; an additional
analytical suite covers all four configured finding families,
numerical status and unit readiness under declared
diagnostic parameters. Neither establishes equivalence for
arbitrary RDF literals, expressions or full SHACL. The
large financial declarative replay uses explicit in-memory
adapters and direct pool evaluation, while the smaller
release comparison exercises the audit entry point after
interface adaptation. Neither is an unadapted replacement
of the archived pipeline. Small slices and overlapping
cohort versions must not be treated as independent
empirical samples. The NHS application independently
19

reconstructs a genuine publisher-defined task, but its
CSV and workbook originate from the same reporting
collection. Agreement verifies reconciliation with the
inspected published aggregates, not underlying patient
records, clinical quality or all upstream measurements.
Its explanation views are generated by this application;
no naturally occurring NHS explanation omission or
practitioner performance gain is established.
External validity.The curated per-market work uses
bounded slices (two sectors, two firms each); behaviour
on large constituent universes is exercised only through
the 64-stock Indonesia cross-section. The multi-join CQ
latency that is engine-bound on the in-memory reference
store is resolved on a standard triplestore (Section 7.8, Sup-
plementary Table S5), so the open question is ontological
fidelity at full-exchange breadth, not execution. Three in-
dependent markets and real, exactly-intersected Indonesian
data mitigate breadth, but generalization to full exchanges
remains future work. The separate NHS application pro-
vides real nonfinancial aggregate-data evidence for the
bounded audit interface, not for reuse of the financial on-
tology or inference rules. One month, one indicator and
an author-implemented adapter do not establish indepen-
dent adoption, longitudinal reliability or general domain
portability.
Conclusion validity.Structural conformity, depen-
dency completeness, and source fidelity are distinct claims.
Thewithin-subjectuserstudy(n=17, Section7.9)provides
exploratory evidence of higher perceived trust and com-
pleteness for evidence-enriched displays (both p < 0.001),
rather than establishing objective audit performance or
calibrated trust. Because each item presented the result-
only version before the evidence-grounded one, part of this
lift may be an order effect; the prepared counterbalanced
objective study (Section 7.3) is designed to address this.
Scope.OntoKG-EQ is a data-and-knowledge-
engineering contribution. It makes no predictive or
causal-economic claim; “outperformance” and “divergence”
are defined operationally over the stated windows and
metrics, not as economic causation.
8.3. Design implications
The contribution is a specialized, reproducible audit
system and diagnostic protocol, rather than a new suffi-
ciency logic or discovery of graph-scope effects. Matched
functional agreement establishes that the implemented in-
terface respects the tested conditions; it does not establish
lowerauthoringeffort, superiorusabilityorgreateraccuracy
than an equivalently specified validator. Those practical
advantages require independent deployment or objective
user evidence beyond the current evaluation. The value of
the artifacts is the explicit, inspectable pairing of finding,
support and delivery outcomes under analytical conditions,
with these limitations retained.
A further distinction is between sufficient evidence in
one selected snapshot and support across declared source
versions. A separate release-robustness extension keeps val-
ues from the same publication together and asks whether a
fixed comparison remains positive in every admitted release.
Two historical BEA examples illustrate a comparison that
reverses between releases and another whose positivity is
obscured by independent marginal bounds [59, 60, 61, 62].
Online Resource 1, section “Release-coherent robustness
of published comparisons,” gives the source bindings, re-
stricted procedure and replay. This is not an alteration of
the three-valued boundary audit or source authentication.
Existing provenance systems support dependent aggregate
comparisons [63]; the extension is a reproducible special-
ization, not a claim to introduce possible-world semantics
or a new general uncertainty method.
The evidence bundle can support deterministic presen-
tation of values and sources, with optional natural-language
assistance. However, even connective prose may introduce
unsupported causal, comparative, or temporal assertions.
A hybrid renderer would require separate claim-level check-
ing and evaluation; the current results do not establish that
such a design achieves perfect faithfulness.
Publishing CQ definitions, artifact mappings, con-
straints and result-evidence links lets others inspect the
intended contract; demonstrated reuse remains conditional
on canonical mapping.
9. Limitations and future work
The most important limitation isevidential scope.
The financial data are fixtures with demonstrator compara-
tors and partially reviewed sources, so they test stored-data
semantics rather than authenticated market effects. Li-
censed, adjusted index and constituent feeds and complete
primary-source review are required before any empirical
market claim. The NHS application covers one month, one
indicator and an author-implemented adapter; repeated
releases, further publishers and independent developers are
needed to assess longitudinal reliability and onboarding
effort.
Ontological fidelity at breadthremains untested.
The three markets share essentially the same data shape,
so 100% apparatus reuse shows that one ontology fits three
structurally similarmarkets, not genuinely heterogeneous
ones. Mapping raw sources into the nine-sheet schema is
manual and unmeasured; onboarding by an independent
developer is the decisive portability test.
Human benefitis unestablished. The historical rat-
ings measure preference only. The prepared counterbal-
anced objective study (Section 7.3) must be run, after ethics
review, to test decision accuracy, source identification and
completion time. A model transcription experiment would
need archived answers and claim-level scoring. The frozen
competency-question set can grow under the same gover-
nance, each new term justified by a new question.
20

10. Conclusion
OntoKG-EQ organizes analytical knowledge-graph con-
struction around explicit competency questions and audits
finding evidence through executable contracts that check
ambient observations, declared support and delivered obser-
vations separately. On a public NHS statistical screen, inde-
pendent source recomputation reconciles 532 providers with
the publisher’s aggregates, keeps one roster entry unavail-
able, and agrees with a matched SHACL-SPARQL baseline
on all 533 frames; six replayed threshold policies iden-
tify their exact affected providers without core-interpreter
changes. Constructed diagnostics yield 78 status/readiness
agreements over 26 analytical cases, actual release replay
reproduces two support/delivery omissions (19/21 to 21/21
after repair), and 487 paired financial records agree under
disclosed adapters. In the corrected 64-company finan-
cial cohort, all 16 complete CQ1/CQ3 comparisons match
independent traversal, but only 22 of 42 numerical posi-
tives satisfy the metadata policy, and source audits expose
scaling and temporal defects.
These results support bounded evidence sufficiency, ex-
plicit failure reporting and reproducible artifact versions,
built from established RDF, SPARQL, SHACL and prove-
nance mechanisms. They do not establish source truth,
an advantage over an equivalently specified validator or
relational implementation, authenticated market effects,
independent deployment or objective human audit benefit.
A predicate-preserving numeric error and a coherently false
source assignment remain outside the contract checks, and
the prepared human experiment has not been executed.
11. Statements and declarations
Funding.This research received no specific grant from
any funding agency in the public, commercial, or not-for-
profit sectors.
Competing interests.The authors have no compet-
ing interests to declare that are relevant to the content of
this article.
Ethics and consent.The historical perception study
(Section 7.9) was an anonymous online questionnaire com-
pleted by seventeen adult volunteers between 7 and 19 July
2026. Each participant confirmed being 18 or older and
gave consent in the form’s first, mandatory item; no names
or contact details were collected, and results are reported
only in aggregate. No ethics review was sought before data
collection. On 1 November 2026, after data collection, the
Research-Ethics Coordinator of the Department of Com-
puter Science, City University of Science and Information
Technology, confirmed in writing (ref. CUP-26-15E) that
under institutional policy the study does not require ethics
committee review and that its aggregate results may be
published. Participant-level records are kept private. The
prepared objective study has not recruited participants.
The NHS application uses public provider-level aggregates,
not individual patient records.
Data and code availability.The original repro-
ducibility package (ontology, SHACL shapes, the five
competency-question SPARQL templates, inference rules,
the unified builder and inference/explanation generator,
per-market data and materialized graphs, evaluation
scripts and outputs, a data dictionary, and the recorded
environment) is openly available on GitHub ( https:
//github.com/furqan-nr/OntoKG ) and archived on
Zenodo (https://doi.org/10.5281/zenodo.21569316),
including the Indonesia data-acquisition scripts and
exact-date intersection builder. The revision code,
contracts, corrected outputs, lineage overlays and
NHS application are released in the same repository
as v2.0.0 (https://github.com/furqan-nr/Onto
KG/releases/tag/v2.0.0 ) and archived on Zenodo
(https://doi.org/10.5281/zenodo.23860671 ). Public
NHS originals are linked by exact URL and hash in the
source manifest; attribution follows the Open Government
Licence v3.0, with logo and third-party exceptions.
Captured third-party source documents and inputs
whose redistribution rights are not established are not
redistributed; they are identified by URL and hash.
Participant-level survey records are not publicly shared
because consent specifies aggregate reporting.
Author contributions (CRediT). Furqan Nasir:
Conceptualization; Methodology; Software; Validation; For-
mal analysis; Data curation; Writing – original draft; Vi-
sualization.Muhammad Atif Saeed:Methodology;
Writing – review & editing.Muhammad Ehsan:Method-
ology; Writing – review & editing.Sher Jeel Ahmad:
Validation; Writing – review & editing.Abdul Moiz
Altaf:Data curation; Writing – review & editing.
Supplementary information.Online Resource 1 dis-
tinguishes historical supporting tables from the revision
checks. Revision scripts and machine-readable reports are
part of the released archive.
12. Declaration of generative AI and AI-assisted
technologies in the manuscript preparation pro-
cess
The original manuscript records use of Anthropic
Claude during 2025–2026 for prose and selected scripts.
The revision additionally used OpenAI Codex assistants in
October 2026 to review positioning, develop and execute
evaluation scripts, inspect outputs, repair evidence-support
generation, and revise the manuscript. New reported quan-
tities are computed from the documented inputs by the
accompanying scripts. All authors reviewed and approved
the revised manuscript and take full responsibility for its
content; AI assistance does not establish source accuracy.
References
[1] A. Hogan, E. Blomqvist, M. Cochez, C. d’Amato, G. de Melo, C.
Gutierrez, S. Kirrane, J. E. Labra Gayo, R. Navigli, S. Neumaier,
A.-C. Ngonga Ngomo, A. Polleres, S. M. Rashid, A. Rula, L.
21

Schmelzeisen, J. Sequeda, S. Staab, A. Zimmermann, Knowledge
graphs, ACM Computing Surveys 54 (4) (2021) 71. https:
//doi.org/10.1145/3447772.
[2] S. Ji, S. Pan, E. Cambria, P. Marttinen, P. S. Yu, A survey on
knowledge graphs: Representation, acquisition, and applications,
IEEE Transactions on Neural Networks and Learning Systems
33 (2) (2022) 494–514.https://doi.org/10.1109/TNNLS.2021
.3070843.
[3] J. Pérez, M. Arenas, C. Gutierrez, Semantics and complexity
of SPARQL, ACM Transactions on Database Systems 34 (3)
(2009) 16.https://doi.org/10.1145/1567274.1567278.
[4] R. Guidotti, A. Monreale, S. Ruggieri, F. Turini, F. Giannotti,
D. Pedreschi, A survey of methods for explaining black box
models, ACM Computing Surveys 51 (5) (2018) 93. https:
//doi.org/10.1145/3236009.
[5] A. Arun, F. Dimino, T. P. Agarwal, B. Sarmah, S. Pasquali,
FinReflectKG: Agentic construction and evaluation of financial
knowledge graphs, in: Proceedings of the 6th ACM International
Conference on AI in Finance (ICAIF ’25), ACM, Singapore, 2025.
https://doi.org/10.1145/3768292.3770363.
[6] B. P. Jeyaraman, B. T. Dai, Y. Fang, A comprehensive review
of financial knowledge graphs, World Scientific Annual Review
of Artificial Intelligence 3 (2025) 2530001.https://doi.org/10
.1142/S2811032325300014.
[7] EDM Council, Financial Industry Business Ontology (FIBO),
Enterprise Data Management Council.https://edmcouncil.o
rg/financial-industry-business-ontology/ (accessed June
2026).
[8] EDM Council, FIBO ontology viewer and specification, Object
Management Group. https://spec.edmcouncil.org/fibo/
(accessed June 2026).
[9] Z. Xu, K. Kim, T. Ito, FinCaKG-Onto: The financial expertise
depiction via causality knowledge graph and domain ontology,
Applied Intelligence 55 (2025).https://doi.org/10.1007/s104
89-025-06456-8.
[10] X. Li, P. Sun, W. Zhou, Z. Wei, Y. Zhang, X. Chu, FinKario:
Event-enhanced automated construction of financial knowledge
graph, in: Proceedings of the 64th Annual Meeting of the Asso-
ciation for Computational Linguistics (Volume 1: Long Papers),
Association for Computational Linguistics, San Diego, CA, USA,
2026, pp. 9826–9845.https://doi.org/10.18653/v1/2026.acl
-long.446.
[11] N. Kertkeidkachorn, R. Ichise, FinKG: A core financial knowl-
edge graph for financial analysis, in: Proceedings of the 2023
IEEE 17th International Conference on Semantic Computing
(ICSC), IEEE, 2023, pp. 90–93.https://doi.org/10.1109/IC
SC56153.2023.00020.
[12] F. Dimino, A. Arun, B. Sarmah and S. Pasquali, FinReflectKG–
EvalBench: Benchmarking Financial KG with Multi-
Dimensional Evaluation, arXiv preprint arXiv:2510.05710, re-
vised March 2026.https://arxiv.org/abs/2510.05710.
[13] S. F. Mohsin, S. K. Jami, S. Raza, S. M. Khalid, An automated
information extraction system from the knowledge graph based
annual financial reports, PeerJ Computer Science 10 (2024)
e1789.https://doi.org/10.7717/peerj-cs.1789.
[14] C. M. Keet, Z. C. Khan, On the roles of competency ques-
tions in ontology engineering, in: Knowledge Engineering and
Knowledge Management (EKAW 2024), Lecture Notes in Ar-
tificial Intelligence, vol. 15370, Springer, 2024, pp. 123–132.
https://doi.org/10.1007/978-3-031-77792-9_8.
[15] M. Grüninger, M. S. Fox, Methodology for the design and evalu-
ation of ontologies, in: IJCAI Workshop on Basic Ontological
Issues in Knowledge Sharing, 1995.
[16] M. C. Suárez-Figueroa, A. Gómez-Pérez, E. Motta, A. Gangemi
(Eds.), Ontology Engineering in a Networked World, Springer,
2012.https://doi.org/10.1007/978-3-642-24794-1.
[17] G. K. S. Quirino, M. P. Barcellos, R. A. Falbo, Use of competency
questions in ontology engineering: A survey, in: Conceptual
Modeling (ER 2023), Lecture Notes in Computer Science, vol.
14320, Springer, 2023, pp. 45–64.https://doi.org/10.1007/97
8-3-031-47262-6_3.
[18] R. Alharbi, V. Tamma, F. Grasso, T. R. Payne, An experiment
in retrofitting competency questions for existing ontologies, in:
Proceedings of the 39th ACM/SIGAPP Symposium on Applied
Computing (SAC ’24), ACM, 2024, pp. 1650–1658.https://do
i.org/10.1145/3605098.3636068.
[19] D. Wiśniewski, J. Potoniec, A. Ławrynowicz, C. M. Keet, Anal-
ysis of ontology competency questions and their formalisations
in SPARQL-OWL, Journal of Web Semantics 59 (2019) 100534.
https://doi.org/10.1016/j.websem.2019.100534.
[20] Y. Taghzouti, F. Michel, T. Jiang, L.-F. Nothias, F. Gandon,
Q2Forge: Minting competency questions and SPARQL queries
for question-answering over knowledge graphs, in: Proceedings of
the 13th Knowledge Capture Conference (K-CAP 2025), ACM,
2025.https://doi.org/10.1145/3731443.3771350.
[21] J. Li, Z. Wang, D. Garijo and M. Poveda-Villalón, CQ4OE: A
benchmark for assessing LLM-assisted ontology generation from
competency questions, arXiv preprint arXiv:2609.26029 (2026).
https://arxiv.org/abs/2609.26029.
[22] J. Li, Z. Wang, D. Garijo and M. Poveda-Villalón, MASEO: A
Multi-Agent System for Explainable Ontology Generation, in:
LLMS4KGOE and ELMKE Workshops at ESWC 2026, CEUR
Workshop Proceedings 4246 (2026) 67–87.https://ceur-ws.or
g/Vol-4246/.
[23] D. L. McGuinness and P. Pinheiro da Silva, Explaining answers
from the Semantic Web: the Inference Web approach, Journal
of Web Semantics 1(4) (2004) 397–413.https://doi.org/10.1
016/j.websem.2004.06.002.
[24] R. Dividino, S. Sizov, S. Staab and B. Schueler, Querying for
provenance, trust, uncertainty and other meta knowledge in
RDF, Journal of Web Semantics 7(3) (2009) 204–219.https:
//doi.org/10.1016/j.websem.2009.07.004.
[25] L. Moreau, P. Missier (Eds.), PROV-DM: The PROV data
model, W3C Recommendation, World Wide Web Consortium,
2013.https://www.w3.org/TR/prov-dm/.
[26] L. Moreau, P. Groth, J. Cheney, T. Lebo and S. Miles, The
rationale of PROV, Journal of Web Semantics 35 (2015) 235–257.
https://doi.org/10.1016/j.websem.2015.04.001.
[27] H. Knublauch, D. Kontokostas, Shapes Constraint Language
(SHACL), W3C Recommendation, World Wide Web Consortium,
2017.https://www.w3.org/TR/shacl/.
[28] J. Ke, A. Bigerl, L. Heling, A.-C. Ngonga Ngomo, Efficient
validation of SHACL shapes with reasoning, Proceedings of the
VLDB Endowment 17 (11) (2024) 2721–2733.https://doi.or
g/10.14778/3681954.3681957.
[29] S. Ahmetaj, M. Ortiz, A. Oudshoorn, M. Šimkus, Reconciling
SHACL and ontologies: Semantics and validation via rewriting,
in: Proceedings of the 26th European Conference on Artificial
Intelligence (ECAI 2023), IOS Press, 2023, pp. 27–34.https:
//doi.org/10.3233/FAIA230248.
22

[30] N. Ferranti, S. Ahmetaj, A. Polleres, J. F. de Souza, A. Steyskal,
Formalizing and validating Wikidata’s property constraints using
SHACL and SPARQL, Semantic Web 15 (6) (2024) 2333–2380.
https://doi.org/10.3233/SW-243611.
[31] E. Kleinsteuber, T. D. Nguyen, B. König-Ries, S. Samuel,
Managing provenance data in knowledge graph management
platforms, Datenbank-Spektrum 24 (2024) 133–143. https:
//doi.org/10.1007/s13222-024-00483-4.
[32] Z. Asma, D. Hernández, L. Galárraga, G. Flouris, I. Fundulaki
and K. Hose, Native Provenance Computation for Federated
and Non-Federated SPARQL Queries, Transactions on Graph
Data and Knowledge 4(1) (2026) 4:1–43.https://doi.org/10
.4230/TGDK.4.1.4.
[33] T. Delva, A. Dimou, M. Jakubowski and J. Van den Bussche,
Data Provenance for SHACL, in: Proceedings of EDBT 2023,
2023.https://doi.org/10.48786/edbt.2023.23.
[34] G. Fierro, Evidence-Carrying Validation for Knowledge Graphs,
arXiv preprint arXiv:2608.15948 (2026).https://arxiv.org/ab
s/2608.15948.
[35] A. K. Sharma and J. M. Kunkel, Ontological Knowledge Blocks:
Executable Compliance and Profile-Based Validation for Trust-
worthy AI Systems, arXiv preprint arXiv:2605.23297 (2026).
https://arxiv.org/abs/2605.23297.
[36] G. Chethan, Composable Trust Infrastructure for Manufac-
turing Knowledge Graphs: Cross-System Provenance, Tem-
poral Reasoning, and Decision Traceability, arXiv preprint
arXiv:2608.21418 (2026).https://arxiv.org/abs/2608.21418.
[37] D. C. Dao, G. Atemezing and C. Debruyne, Keeping track of
errors: A study of SHACL-DS for RDF dataset validation on the
ERA RINF Knowledge Graph, arXiv preprint arXiv:2605.10540
(2026).https://arxiv.org/abs/2605.10540.
[38] C. He, X. Zhou, D. Wang, H. Xu, W. Liu and C. Miao, ESGlass:
Glass-Box ESG and Sustainability Reports, unreviewed concept
preprint, Preprints.org, 27 March 2026.https://www.preprint
s.org/manuscript/202603.2187.
[39] B. Peng, Y. Zhu, Y. Liu, X. Bo, H. Shi, C. Hong, Y. Zhang, S.
Tang, Graph retrieval-augmented generation: A survey, ACM
Transactions on Information Systems 44 (2) (2026), Article 35.
https://doi.org/10.1145/3777378.
[40] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin,
N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, S.
Riedel, D. Kiela, Retrieval-augmented generation for knowledge-
intensive NLP tasks, in: Advances in Neural Information
Processing Systems 33 (NeurIPS 2020), 2020, pp. 9459–9474.
https://doi.org/10.48550/arXiv.2005.11401.
[41] B. Sarmah, B. Hall, R. Rao, S. Patel, S. Pasquali, D. Mehta,
HybridRAG: Integrating knowledge graphs and vector retrieval
augmented generation for efficient information extraction, in:
Proceedings of the 5th ACM International Conference on AI in
Finance (ICAIF ’24), ACM, 2024, pp. 608–616.https://doi.or
g/10.1145/3677052.3698671.
[42] S. Ma, C. Xu, X. Jiang, M. Li, H. Qu, C. Yang, J. Mao, J.
Guo, Think-on-Graph 2.0: Deep and faithful large language
model reasoning with knowledge-guided retrieval augmented
generation, in: Proceedings of the International Conference
on Learning Representations (ICLR), 2025. arXiv:2407.10805.
https://openreview.net/forum?id=oFBu7qaZpS.
[43] G. Balanos, E. Chasanis, K. Skianis, E. Pitoura, KGRAG-
Ex: Explainable retrieval-augmented generation with knowl-
edge graph-based perturbations, in: H. Takeda, et al. (Eds.),
Knowledge Graphs (IJCKG 2025), Lecture Notes in Computer
Science (LNAI), vol. 16297, Springer, Singapore, 2026, pp. 35–50.
https://doi.org/10.1007/978-981-95-5009-8_3.
[44] Z. Sun, X. Zang, K. Zheng, Y. Song, J. Xu, X. Zhang, W. Yu,
H. Li, ReDeEP: Detecting hallucination in retrieval-augmented
generationviamechanisticinterpretability, in: Proceedingsofthe
International Conference on Learning Representations (ICLR),
2025.https://openreview.net/forum?id=ztzZDzgfrh.
[45] A. Ahmad, M. A. Khan, Evaluating GraphRAG for traceable
and interpretable question answering, in: Proceedings of the 2026
International Conference on Artificial Intelligence, Computer,
Data Sciences and Applications (ACDSA), IEEE, 2026.https:
//doi.org/10.1109/ACDSA67686.2026.11468256.
[46] J. Sequeda, D. Allemang, B. Jacob, Knowledge graphs as a
source of trust for LLM-powered enterprise question answering,
Journal of Web Semantics 85 (2025) 100858.https://doi.org/
10.1016/j.websem.2025.100858.
[47] D. Benfenati and A. M. Rinaldi, Ontology-guided neuro-symbolic
GraphRAG for grounded query answering, Neural Computing
and Applications 38 (2026) 797.https://doi.org/10.1007/s0
0521-026-12495-0.
[48] K. Aneja, M. Srivastava, S. Das, N. Aneja, Interpretable
question answering with knowledge graphs, arXiv preprint
arXiv:2510.19181 (2025). https://doi.org/10.48550/arXiv
.2510.19181.
[49] D. Wisniewski, J. Potoniec, A. Lawrynowicz and C. M. Keet,
Competency Questions and SPARQL-OWL Queries Dataset
and Analysis, author preprint (2018), arXiv:1811.09529.https:
//arxiv.org/abs/1811.09529.
[50] A. C. MacKinlay, Event studies in economics and finance,
Journal of Economic Literature 35 (1) (1997) 13–39.https:
//www.jstor.org/stable/2729691.
[51] S. J. Brown, J. B. Warner, Using daily stock returns: The case
of event studies, Journal of Financial Economics 14 (1) (1985)
3–31.https://doi.org/10.1016/0304-405X(85)90042-X.
[52] J. Y. Campbell, A. W. Lo, A. C. MacKinlay, The Econometrics
of Financial Markets, Princeton University Press, 1997.
[53] NHS England, Referral to Treatment Waiting Times Data 2026–
27: August 2026 full CSV and incomplete-provider workbook,
2026. https://www.england.nhs.uk/statistics/statisti
cal- work- areas/rtt- waiting- times/rtt- data- 2026- 27/
(accessed 18 October 2026).
[54] NHS England, RTT Statistics User Guidance, operational stan-
dard and reproducibility guidance.https://www.england.nhs.
uk/statistics/statistical-work-areas/rtt-waiting-times
/rtt-statistics-user-guidance/(accessed 18 October 2026).
[55] NHS England, Terms and conditions, copyright and reuse.https:
//www.england.nhs.uk/terms-and-conditions-2/ (accessed
18 October 2026).
[56] The National Archives, Open Government Licence for public
sector information, version 3.0.https://www.nationalarchives
.gov.uk/doc/open-government-licence/version/3/ (accessed
18 October 2026).
[57] T. Pellissier Tanon, Oxigraph: A SPARQL 1.1 graph database,
software, 2024.https://github.com/oxigraph/oxigraph.
[58] J. D. Lee, K. A. See, Trust in automation: Designing for ap-
propriate reliance, Human Factors 46 (1) (2004) 50–80.https:
//doi.org/10.1518/hfes.46.1.50_30392.
23

[59] U.S. Bureau of Economic Analysis, Gross Domestic Product,
First Quarter 2024 (Second Estimate) and Corporate Profits
(Preliminary), 30 May 2024.https://www.bea.gov/index.php/
news/2024/gross-domestic-product-first-quarter-2024-s
econd-estimate-and-corporate-profits (accessed 20 October
2026).
[60] U.S. Bureau of Economic Analysis, Gross Domestic Product
(Third Estimate), Corporate Profits (Revised Estimate), and
GDP by Industry, First Quarter 2024, 27 June 2024.https:
//www.bea.gov/news/2024/gross-domestic-product-third-e
stimate-corporate-profits-revised-estimate-and-gdp-ind
ustry(accessed 20 October 2026).
[61] U.S. Bureau of Economic Analysis, GDP and the Economy:
Second Estimates for the Second Quarter of 2024, Survey of
Current Business, 5 September 2024, Table 4.https://apps.bea
.gov/scb/issues/2024/09-september/0924-gdp-economy.htm
(accessed 20 October 2026).
[62] U.S. Bureau of Economic Analysis, GDP and the Economy:
Third Estimates for the Second Quarter of 2024, Survey of
Current Business, 4 October 2024, Table 7.https://apps.b
ea.gov/scb/issues/2024/10-october/1024-gdp-economy.htm
(accessed 20 October 2026).
[63] ProvSQL contributors, Aggregation and Grouping, official soft-
ware documentation. https://provsql.org/docs/user/aggreg
ation.html(accessed 20 October 2026).
24

Online Resource 1: Supplementary material
This appendix is the supplementary material (Online Re-
source 1) referred to in the main text.
A. Historical model-transcription experiment (ex-
cluded)
This section documents the historical transcription ex-
periment, which is excluded from the revised main quan-
titative evaluation. Eight instruction-tuned checkpoints
received a structured evidence context and generated brief
answers using greedy decoding. The notebooks and ag-
gregate scores do not archive the generated answer texts
needed for retrospective rescoring. No new model scores
are inferred from those aggregates.
A future reproducible run must save the exact context
and answer, graph hash, case identifier, source identity,
prompt, model revision, and scorer version. Contextual
company announcements must be distinguished from the
actual sources of numeric observations.
B. Competency-question SPARQL templates (CQ1
and CQ3)
The two multi-join analytical queries are inlined be-
low exactly as executed, unchanged, on both the RDFLib
reference engine and the Oxigraph triplestore (main pa-
per, Scalability subsection). The full CQ1–CQ5 set, the
SHACL shapes, and the R1–R4 CONSTRUCT rules are
released verbatim in the reproducibility package (queries/,
shacl/shapes.ttl,rules/).
# CQ1 - stronger reported fundamentals, weaker market response than
the benchmark
PREFIX: <https://w3id.org/ontokg-eq#>
SELECT?company ?yoyProfitGrowth ?companyReturn ?benchmarkReturn
WHERE{
?fg :isObservationOf ?company ; :hasMetricName "YoY profit growth
%" ; :hasMetricValue ?yoyProfitGrowth .
?companya:Company .
?cr :isObservationOf ?company ; :hasMetricName "post-report
window return %" ;
:hasMetricValue ?companyReturn ; :observedOverWindow ?w .
?br :isObservationOf ?bm ; :hasMetricName "benchmark window
return %" ;
:hasMetricValue ?benchmarkReturn ; :observedOverWindow ?w .
?bma:MarketIndex .
FILTER(?yoyProfitGrowth > 0 && ?companyReturn < ?benchmarkReturn)
}ORDER BY DESC(?yoyProfitGrowth)
# CQ3 - outperforms BOTH sector comparator AND broad-market
benchmark over the same window
PREFIX: <https://w3id.org/ontokg-eq#>
SELECT?company ?companyReturn ?sectorReturn ?benchmarkReturnWHERE
{
?cr :isObservationOf ?company ; :hasMetricName "post-report
window return %" ;
:hasMetricValue ?companyReturn ; :observedOverWindow ?w .
?companya:Company ; :isClassifiedByIndustrySector ?sector .
?sr :isObservationOf ?sector ; :hasMetricName "sector window
return %" ;
:hasMetricValue ?sectorReturn ; :observedOverWindow ?w .
?br :isObservationOf ?bm ; :hasMetricName "benchmark window
return %" ;
:hasMetricValue ?benchmarkReturn ; :observedOverWindow ?w .
?bma:MarketIndex .
FILTER(?companyReturn > ?sectorReturn && ?companyReturn > ?
benchmarkReturn)
}ORDER BY DESC(?companyReturn)
C. Historical scorer and its limitations
Thehistoricalscorermeasurednumericprecision, lexical
unsupported-assertion cues, and a provenance indicator.
The currently released code adds numeric-value recall and
accepts a matching date or source token. These definitions
must not be conflated with the historical aggregate scores.
Numeric precision can assign a perfect score to an an-
swer with no numbers. Distinct-value recall does not dis-
tinguish two different metrics with the same numeric value.
A matching date does not establish correct source iden-
tity, and lexical cue detection does not establish entailment.
Sinceoriginalanswertextsarenotarchived, strongerseman-
tic scoring cannot be reconstructed for the historical panel.
The revision report evaluation_jws/llm_rescore.md
records this limitation.
D. Extended formal model
This section gives the full derived-metric and inference-
rule detail summarised in Section 3.2.
Derived metric.A derived metric is a function
φ : (2Obs,W )→Obs that maps a set of base observations
and a windowW to a new (derived) observation. OntoKG-
EQ defines nine CQ-justified derived metrics: post-report
window return, year-on-year profit growth, sector window
return, benchmark window return, exchange-rate window
change, exchange-rate-versus-company return correlation,
exchange-rate-versus-benchmark return correlation, the
event-window sum of supplied returns (historically labelled
cumulative abnormal return), and abnormal volume ratio.
Derived observations are first-class observations; their de-
clared structural constraints, deciding dependencies, and
source-cell lineage require separate checks.
Inference rule.An inference rule ρ : Pattern→
Finding maps a graph pattern encoding a CQ con-
dition over derived metrics to an AnalyticalFinding
f = (e,t,ρ id,q,O f), where e is the result entity,t the
finding type,ρid the rule identifier,q the CQ family, and
Of the set of observations whose values triggered the rule.
E. Supplementary tables
F. Final-graph, relational and lineage checks
The revised inference code includes abnormal-volume
observations in R4 support and validates the final graph
after generating findings and bundles. All 21 findings
acrossthethreecuratedmarketspasstheaddeddependency
checks. The original PSX graph contained two volume-
triggered findings lacking that support.
Five final-graph mutations retain contextual evidence.
Existing SHACL detects 0/5, while the additional depen-
dency audit detects 3/5. A source swap and a plausible
numeric change preserving the predicate remain undetected.
25

Table S1: Per-market adapter configuration: the analytical keys that
differ between markets (sheet-file prefix, data folder and display labels
are also configured). The ontology, shapes, queries, rules and code
are unchanged.
Adapter key PSX MSX IDX
namespace .../psx# .../msx# .../idx#
company iden-
tifier column
company_
symbol
stock_code stock_code
EPS column eps eps_myr eps
FX rate col-
umn / sheet
pkr_usd_rate
/ 06_sbp_fx
myr_usd_rate
/ 06_bnm_fx
idr_usd_rate /
06_fx
local currency PKR MYR IDR
growth-units
scale
×1 (percent)×100 (ratio)×1 (percent)
benchmark
comparator
type
market index broad_
market_
benchmark_
proxy
broad_
market_
benchmark
benchmark la-
bel
KSE-100 FBM KLCI
(proxy)
Jakarta Com-
posite (JCI)
Table S2: (PSX, MSX, and IDX are our internal dataset codes for
the Pakistan Stock Exchange, Bursa Malaysia, and Indonesia Stock
Exchange datasets, respectively.) Markets and constituents.
Market Exchange /
benchmark
Sector A (2 firms) Sector B (2 firms)
PSX Pakistan Stock
Exchange / KSE-
100
Fertilizer: EN-
GROH, FFC
Oil & Gas Explo-
ration: OGDC,
PPL
MSX Bursa Malaysia
/ FBM KLCI
(proxy)
Financial Ser-
vices: MAY-
BANK, CIMB
Telecommunications
& Media: TM,
MAXIS
IDX Indonesia Stock
Exchange /
Jakarta Compos-
ite
Banking: BBCA,
BMRI
Telecom: ISAT,
TOWR
Table S3: Historical timing comparison omitted from the main evalu-
ation.
Measurement Interpretation
Template retrieval/render-
ing and model generation
on different hardware
Different tasks; no like-for-
like efficiency advantage es-
tablished
Table S4: Component ablations on the PSX and MSX graphs (each
component removed in isolation).
Removed component Metric affected Full Ablated
Provenance layer historicalevidenceavail-
ability
1.00 0.00
Evidence-source links evidence coverage 1.00 0.00
Inference rules derived findings (PSX /
MSX)
9 / 2 0 / 0
Evidence bundles CQ5 explainability
rows (each market)
3 0
SHACL malformed observation
detected
yes no
Table S5: The unchanged CQ1–CQ5 SPARQL templates on the
64-stock Indonesia graph (37,046 triples), executed on the Oxigraph
triplestore. Latencies are medians of 20 runs (min–max in brackets)
after a 70 ms one-time load, for a representative run, and are hardware-
and run-dependent. The first-call JIT warm-up inflates the maximum.
CQ1 and CQ3 are the multi-join queries that do not complete on
RDFLib’s in-memory engine at this size.
Query Rows Latency (ms): median
[min–max]
CQ1 (fundamentals vs mar-
ket response)
17 3.8 [3.7, 4.3]
CQ2 (FX association) 63 0.3 [0.2, 0.6]
CQ3 (outperform sector and
benchmark)
24 5.0 [4.9, 5.6]
CQ4 (announcement event
windows)
0 1.6 [1.6, 2.9]
CQ5 (explainability / prove-
nance)
3 0.1 [0.1, 0.1]
Table S6: Fault-injection: injected data errors and whether SHACL
detects them (valid PSX graph, one fault per trial).
Injected fault Detected by SHACL
wrong metric-value datatype
(decimal→string)
yes
company missing name yes
market observation missing sub-
ject link
yes
malformed announcement date
(date→string)
yes
observation missing metric name yes
fundamental linked to wrong
reporting-period class
yes
duplicate metric value (violates
maxCount)
yes
evidence item missing source yes
26

Known-original snapshot checks are intervention oracles,
not independent source verification.
The independent source-to-graph return audit verifies
64/64 arithmetic company window statistics within10−6
percentage points. It does not verify compounded holding-
period returns, all metrics, or source truth. The event
builder sums supplied event returns without benchmark
subtraction. For IDX, the acquisition assembler writes
ordinary consecutive-close company returns to these rows,
so the archived event statistic is not market-adjusted CAR;
PSX/MSX upstream interpretation remains unverified.
One unchanged constrained SQLite schema and query
set matches SPARQL CQ1/CQ3 and evidence-dependency
joins on PSX, MSX, and IDX. This establishes canonical
relational reuse as a capable control, not RDF superiority.
The separate PROV overlay maps 44/45 deciding ob-
servations to exact workbook cells and registered source
identifiers. One missing-input PSX event statistic remains
unresolved. Full observation mapping counts are 500/522,
319/321, 542/542, and 4944/4947 for PSX, MSX, IDX,
and scaled IDX. Workbook lineage does not authenticate
original documents or numeric data.
Exact graph hashes, source-cell mappings, script ver-
sions, and detailed checks are recorded in the machine-
readable reports underreproducible_OntoKG/evaluati
on_jws/. They are part of the released revision archive.
G. Executable evidence contracts and semantic in-
terventions
The machine-readable registry specifies R1–R4 metric
roles, entity roles, compatible windows, predicate parame-
ters, expected units and related artifact paths. R2 concerns
the FX-sensitive classification rather than the full CQ2 an-
swer. CQ5 supplies the explanation policy. The checker
uses Decimal values and independently replays declared
finding support and observations available in the correctly
targeted actual bundle. R4 admits either passing OR
branch; unused operands are context rather than necessary
evidence. Missing graph units and undeclared temporal
anchors remain unverified.
All 21 inspected bundles pass the bounded sufficient-
witness policy, and each has a witness whose recorded
cell-to-source paths carry matching identifiers. This does
not authenticate sources or prove that all upstream com-
putational dependencies have been recorded. Six synthetic
tests cover threshold equality, role identity, missing evi-
dence, actual-bundle integrity and OR sufficiency.
The two undetected corruptions preserve the predicate
despite a small numeric change, or alter both a source edge
and identifier to create an internally consistent false attri-
bution. A separate inconsistent source edge is detected.
The same-data control disables contract policies; it is not
an evaluation of NPCS or another external provenance
implementation. Query AND-to-OR hash drift is reported
separately from witness validation. Currency/unit corrup-
Table S7: Selected semantic corruption suite: 12 corruptions plus two
acceptance controls. Counts are not estimates of naturally occurring
error detection.
Policy Corruptions flagged (of 12)
Existing SHACL shapes 0
Finding-condition replay 7
Actual-bundle sufficiency 8
Combined condition, bun-
dle and source-path poli-
cies
10
tion is not tested because explicit observation metadata is
absent.
H. Financial requirement-change scenario
Changing CQ3 to require more than one percentage
point over both comparators reduces selections from two to
one in PSX and IDX; MSX remains empty. Both versioned
SELECT and CONSTRUCT results match independent
graph traversal. Five synthetic boundary fixtures select
three companies under the original predicate and one under
the revised predicate. Old/new contracts, queries, rules
and hashes are preserved under the contract-evolution out-
puts. Read-only unchanged-CQ controls do not establish a
general regression theorem. Adopting the revised threshold
in production would require deploying the corresponding
inference implementation.
The complete local verification workflow is provided
by reproducible_OntoKG/run_jws_revision.py . It
regenerates audit artifacts without rebuilding or replacing
the archived market graphs.
I. Strengthened revision artifacts
The financial-v2 graphs are separate from archived in-
puts. See evaluation_jws/financial_v2/ for formulas,
missing-data policies, graph hashes, and primary-source
spot checks;expanded_evaluation/ and its categorical
rerun expanded_evaluation_v2/ for all cases, complete-
query oracle comparisons and evidence-withholding vari-
ants (330 in total across paired cohorts); andmetadata_v2/
for declaration checks and failures. The corrected scaled
cohort has 42 numerical positives but only 22 metadata-
qualified positives. Its 147 negatives, three incomplete
classifications and 64 event-not-applicable cases remain
separately visible. Corrected curated positives are 16 nu-
merically and 15 metadata-qualified; overlapping cohorts
are not independent replications.
external_provenance/ retains original and generated
queries, software identities and executed NPCS results.
The unmodified native FILTER path fails on the tested
CQ3 queries; reported successful comparisons concern BGP
provenance with disclosed post-filtering. This is not a
replacement of the earlier controlled policy ablation by an
external fault-detection experiment.
27

objective_study_v2/ contains the prepared, unreg-
istered protocol, four counterbalanced packets, facilitator
answer key (withheld from the public release) and empty
response template. Twelve distinct tasks contain identical
source material across displays. No objective participant
results exist. The analysis rejects the empty template;
synthetic software controls are never counted as partici-
pants. Responses and participant-level analysis must be
kept private according to consent and ethics requirements.
J. Current source-assurance artifacts
The current annual-fact evidence combines six OGDC
repairs in annual_source_repair/ and six completed
PPL repairs inppl_source_completion/ . The twelve
facts include eight monetary scale corrections and four
direct EPS agreements. Earlier source-period failures and
pending states remain historical records, not current unre-
solved PPL statuses. Ten PPL completion checks and five
annual-repair mutation checks pass. These reruns validate
preserved source bytes and reviewed transcriptions; they
do not independently interpret new documents.
The temporal_resolution/ overlay quarantines
twenty scaled R1 recent-analysis cases and the curated
TOWR mismatch. FFC’s issuer document date and
Maybank’s annual-report announcement match their
anchors, but no first-earnings publication timestamp
is authenticated. Exact source URLs, scopes and date
definitions are in the acquisition history below.
The authentic_prices_malaysia/ capture supplies
32 required Maybank company dates and matches all thirty
original post-report closes. The issuer republication’s ad-
justment convention remains unresolved. The separate
authentic_prices_psx/regulator_recovery.json ver-
ifies eight unique observations from four original SECP
reports: six KSE100 total-return levels and two FFC
closes. The earlier indexed-only ledger is historical. Nine
price-recovery controls pass. Missing FFC baselines, miss-
ing KSE100PR/KLCI series and corporate-action defini-
tions prevent valid market-relative classification. Cap-
tured PDFs, renderings and CSV remain local pending
redistribution-rights review; hashes are integrity checks,
not publisher signatures.
K. Frozen source-review frame and consolidated
cohort
The source_sampling/ manifest fixes 52 cases across
29 corrected dataset/rule/status strata using seed 20261016.
The exact source report is preserved asexpanded_evaluat
ion_frozen.json with a matching SHA256. This frame
includes positive, negative and incomplete classifications; it
was frozen after purposive checks and is not preregistration.
Selected cases are not assumed authenticated. Shared
dependencies, unequal sampling fractions and overlapping
IDX cohorts prohibit an unweighted pooled source-accuracy
estimate.
The separatesource_backed_cohort/ replay consoli-
dates FFC and Maybank as subsets of the eight-candidate
roster. Six controls check endpoint arithmetic, missing/-
conflicting observations, horizons and refusal to promote
absent benchmark results. Both source-qualified labels
remain unknown, not negative, and the two cases do not in-
crease the independent sample. A feed-specific adjustment
legend cannot be transferred to another provider. Details
of the definition audit are inprice_definition_audit/.
The executed systematic_source_audit/ reports
2,357 unique recorded workbook-cell inputs across the
frozen 52 cases. Coverage counts are 2,271 unreviewed lin-
eage inputs, 46 declared proxies, thirty issuer-republished
unknown-basis closes, four exact scale-corrected PAT facts,
two rounded narrative agreements, two regulator numeric
agreements with unresolved workbook basis, and two price
disagreements. The thirteen assertions pass; all four in-
put graph hashes match the frozen frame. No case has
complete coverage under the all-recorded-input criterion.
This does not test minimal source-authenticated AND/OR
sufficiency or prove that an unreviewed case is false. All
reviewed evidence remains purposive; no pooled population
error-rate estimate is made.
L. Public NHS application artifacts
The separately versionedexternal_applications/nh
s_rtt_v1/ contains the frozen task protocol, source mani-
fest, independent source-oracle records, adapter records and
application outputs. The source archive and provider work-
book are locally retained originals, protected by SHA256
hashes; they are not silently overwritten or included in a
public endorsed NHS release. The manifest supplies ex-
act publisher URLs and OGL attribution with logo and
third-party exceptions. CSV and workbook are different
representations of the same reporting collection, not inde-
pendent collections.
The source oracle and source adapter separately parse
the original CSV and workbook without importing the
RDF checker. They reconcile all 532 eligible provider
records; the extra workbook-only D1V5N roster entry is
explicitly unavailable from selected CSV rows, not zero-
filled. The adapter generates two deciding count roles
and recorded row/column selectors, while the contract
compiles fixed factors 100 and 92 into the existing addition
expression language. The interpreter itself is unchanged.
The dated implementation addendum explains why the
protocol’s anticipated optional arithmetic extension proved
unnecessary; the frozen protocol remains intact.
The actual SHACL-SPARQL/availability comparator
reconstructs its pools from RDF without checker selection
helpers. It agrees on all 533 frames, including the unavail-
able record; 533 actual SHACL validations are recorded,
with identical within-frame pools cached. Three matching
pool labels are not three independent samples. Source cells,
generated triples and code/configuration hashes document
execution and engineering scope, not human time savings.
28

The evidence views are generated by this application and
contain no patient records. No natural reconciliation de-
fects or objective human outcomes are claimed.
M. Public-data requirement-change replay
The protocol is contracts/nhs_change_protoco
l_2026-10-19.json . Modules docs/jws_nhs_chang
e_oracle.py , docs/jws_nhs_change_baseline.py
and docs/jws_nhs_change_replay.py separate inte-
ger expectations, independent parameterized queries and
interpreter replay. Four regression methods in docs/t
est_jws_nhs_change_replay.py pass. Outputs in
evaluation_jws/nhs_change_replay_v1/ retain each
contract, exact queries, all provider identities, affected
sets, source-derived artifact/code hashes and the execution-
plan note. Six policies reuse one cohort; 3,198 provider-
policy evaluations are not 3,198 independent observations.
Fourteen constructed controls per policy yield 252 actual
SHACL pool validations, separately from provider-bound
cohort SPARQL. The zero-denominator software guard
returns false for the guarded predicate, not a defined per-
centage or a failed target for an unavailable provider.
Both implementations parameterize the rule and agree
with the integer oracle. Original-policy re-execution re-
stores outputs without editing the interpreter or earlier
source-derived artifacts. This is not stateful deployment
rollback, a human maintenance comparison or a new NHS
policy. The interrupted initial query attempt supplies no
timing claim. The protocol predates variant execution,
not external preregistration or blinding. A parent-side
independent integer calculation reproduces every provider
status and exact affected set; a separate review verifies the
original ZIP/XLSX sizes and hashes at review time. These
are implementation/source-identity checks, not new data
collection or external practitioner validation. Unit readi-
ness concerns declared schema consistency, not independent
verification of clinical measurement accuracy.
N. Release-coherent robustness of published com-
parisons
Task and interpretation..Evidence sufficiency in a selected
snapshot does not establish stability across source versions.
A separate prototype asks whether a fixed, locally qualified
comparison passes in every admitted whole-release alterna-
tive. Itssemanticsis ∀ω∈ Ω∃Wω suchthat Wω isapassing
qualified witness; witnesses may change between worlds.
The outputs arecertain-qualified-positive or an ex-
plicit non-positive counterworld. Missing roles can cause
non-positivity, so a counterworld is not automatically the
main interpreter’s numericalfalse. This prototype neither
modifies that interpreter nor independently authenticates
source measurements.
Two purposively selected BEA examples use published
one-decimal real growth rates for the United States, percent
change from the preceding quarter at seasonally adjusted
annual rates. Each case has one source group: a mode
contains both values from one dated release. Superseded
estimates are historical versions, not equally valid current
truths. Theanalyst-definedquestionisretrospectiverobust-
ness over the listed initial releases, not an official policy test,
causal inference or robustness to all later updates. Pub-
lished decimals are exact inputs here; unpublished digits
and rounding uncertainty are not modeled.
Table S8: Selected historical release comparisons. Each pair is cen-
tre/comparator growth in percent; rows are coherent release modes,
not independent samples.
Comparison Release date (2024) Pair Strict
Q1 GDP>GDI 30 May, second 1.3/1.5 Does not pass
27 June, third 1.4/1.3 Passes
Q2 GDP>real PCE 25 July, advance 2.8/2.3 Passes
29 August, second 3.0/2.9 Passes
26 September, third 3.0/2.8 Passes
Q1’s GDP–GDI direction changes; the May release is
an explicit counterworld. The May and June BEA news
releases supply the GDP/GDI paragraphs and revision
tables.1 The advance release has no GDI estimate and is
explicitlyexcludedfromthispaired-completetask, notfilled
with zero. Q2 passes all three admitted modes, although
independent ranges cannot certify this: GDP’s minimum
2.8 does not exceed real PCE’s maximum 2.9. That pair
mixes July and August and is not an admitted mode. Val-
ues come from thechangecolumns of SCB Tables 4 and 7,
not adjacent GDP-contribution columns or the PCE price
index.2 The repeated August pair agrees across both ta-
bles. September incorporates an annual update, retaining
reference year 2017; each vintage’s own reported quarter-
on-quarter rates remain together. The two quarters are
evaluated separately, not assumed independent groups.
Restricted procedure..For fixed entity/window/pool,r≥ 1,
exact finite values and marginsδj, the supported query is
∃c∈C,s j∈S j : ⋀r j=1c > sj +δj. There is at least one
source group; each has a nonempty finite set of modes and
independently selects exactly one mode. Qualification and
compatible units are resolved beforehand. For modea of
groupg, construct
Iga,j = [maxC ga,minS ga,j +δ j], F j =
⋂
g
⋃
a
Iga,j.
Absent roles give structural unbounded endpoints; discard
reversed intervals. A finite pointt∈F j selects a covering
1Source: U.S. Bureau of Economic Analysis, Q1 second estimate,
https://www.bea.gov/index.php/news/2024/gross-domestic-pro
duct-first-quarter-2024-second-estimate-and-corporate-pro
fits; Q1 third estimate,https://www.bea.gov/news/2024/gross-d
omestic-product-third-estimate-corporate-profits-revised-e
stimate-and-gdp-industry. Accessed 20 October 2026.
2BEA,Survey of Current Business, 5 September 2024, Table 4,
https://apps.bea.gov/scb/issues/2024/09-september/0924-gdp
-economy.htm; 4 October 2024, Table 7,https://apps.bea.gov/scb
/issues/2024/10-october/1024-gdp-economy.htm . These articles
reflect the August and September releases, respectively. Accessed 20
October 2026.
29

original mode from every group: all centres are at most
t, and all comparator values plus margin are at leastt.
This is a coherent non-positive world. Conversely, any
world failing comparisonj supplies such a separator, in-
cluding absent-role cases. The same maximal centre can
serve every comparator, so the query is certain exactly
when everyFj is empty. Ordinary colored interval cover-
age usesO(N +rMlogM )comparison operations for N
values andM modes, apart from exact-rational bit costs
and output/checking costs. Cross-group constraints, addi-
tional compatibility joins, changing windows and arbitrary
arithmetic are unsupported. This is a restricted specializa-
tion, not a new geometric primitive or uncertainty seman-
tics. Existing ProvSQL documentation supports dependent
numeric-aggregate comparisons.3
Execution and reproduction..Both cases agree with inde-
pendent original-binding world enumeration and an exact
SAT encoding, and pass a separately recomputed output
check. All five modes are replayed. Fourteen test methods
include 625 exhaustive and 400 seeded controlled models
plus application guards; these are software checks, not ad-
ditional real observations. The positive trace is ordinary
execution evidence, not a signed or succinct certificate.
These one-group examples are trivially enumerable: no
practical speed advantage, native ProvSQL benchmark,
deployment or human benefit is established. Separate syn-
thetic timing trials are retained as prototype artifacts, not
main empirical results.
Run docs/jws_source_certainty_application.py ;
inputs, bindings, outputs and the exploratory protocol are
in evaluation_jws/source_certainty_application_
v1/. The source_coherent_certainty_v1/ sibling re-
tains synthetic checks. Manual primary-page inspection
supplies semantic/source review; executable bindings check
local transcription correspondence, not BEA’s measure-
ment process. Hashes identify local artifacts, not publisher
signatures. Attributed numeric transcriptions follow BEA’s
public-domain statement, subject to stated exceptions.4
These artifacts are part of the released revision archive.
O. Objective evidence boundary
The audit inobjective_study_v2/EVIDENCE_AUDI
T.md confirms that the private historical schemas contain
no correctness-scored task judgments or durations. Public
provenance and XAI participant datasets cannot estimate
an OntoKG display effect because the tasks and allocation
differ. Four instrument tests pass, but these are software
tests, not participants. No new objective sessions have
been conducted.
3ProvSQL,Aggregation and Grouping, https://provsql.org/do
cs/user/aggregation.html, accessed 20 October 2026.
4https://www.bea.gov/help/faq/147.
P. Detailed source verification and acquisition his-
tory
These paragraphs preserve the successive audit stages.
A pending status describes its stage, not the latest consoli-
dated evidence. In particular, the PPL completion overlay
supersedes six earlier pending facts. The main paper re-
ports current qualifications; historical inputs and reports
remain unchanged.
Comparator authenticity is separate from arithmetic cor-
rectness..The PSX benchmark rows explicitly declare
interpolation/forward-filling; MSX rows explicitly identify
a damped selected-universe proxy rather than an official
KLCI feed. Recomputing returns from those values does
notauthenticateamarketbenchmark. Classificationresults
using these comparators are illustrative applications of the
declared predicates, not verified market reactions. Source-
linked arithmetic replay, disclosure-date alignment and
authentic benchmark coverage must be reported indepen-
dently. Official replacements must preserve the predeclared
dates and horizon rather than substituting a convenient
interval.
Bounded issuer-original authentication..A further purpo-
sive review checks 16 workbook facts against four issuer-
authored documents. Four EPS cells match exactly in value
and unit; four FFC monetary cells match exactly only af-
ter a factor of one million is applied to the workbook’s
declared thousand-PKR scale. Two ENGROH standalone
PAT cells agree only at the issuer narrative’s rounded
million-PKR precision after scaling. Six OGDC/PPL an-
nual sales, PAT and EPS cells cite half-year documents for
December 2025 rather than the workbook year ended June
2025; these source-period mismatches are quarantined from
authenticated-source claims. This is not a representative
error-rate estimate. Reviewed transcriptions, exact cells,
accounting scope, page references and source-copy hashes
are retained separately. Automated reruns compare those
reviewed transcriptions with workbook values; they do not
independently read or authenticate the documents. Daily
prices, FX, volumes and remaining market sources are not
certified by this bounded review.
Versioned annual-source repair..The initial wrong-period
audit is preserved. A subsequent repair authenticates six
OGDC annual facts against issuer-original PSX document
259805, PDF page 3: FY2025 net sales and PAT are
401,177,969 and 169,903,614 thousand PKR, and EPS is
39.50 PKR; FY2024 comparative values are 463,697,861,
208,975,771 and 48.59. Four monetary cells require a factor
of one million; two EPS cells match directly. Correct PPL
annual-source candidates were located, but incomplete re-
trieval prevents visual financial-page authentication, so
six PPL cells remain pending. The overlay distinguishes
authenticated repairs from pending candidates and leaves
archived inputs unchanged. Growth recomputation con-
firms common scaling cancels in the four reviewed ratios,
30

but does not remove PPL’s pending source status. FY2024
is checked against comparative columns, not separate orig-
inal releases. OGDC’s issuer letter dated 23 September
2025 is not treated as an authenticated first-publication
timestamp or used to justify later windows.
Temporal quarantine rather than forced alignment..The
separate temporal-resolution overlay excludes all 20 scaled
R1 positives from report-event use: the workbooks ex-
plicitly label these anchors as recent-analysis windows,
and their purported report dates repeat fiscal year-end.
The TOWR mismatch is also quarantined. The 22 re-
tained scaled positives are non-R1 classifications, not 22
authenticated earnings events. Bounded primary-source
checks match Maybank’s official FY2025 annual-report
announcement of 1 April 2026 to its anchor (issuer an-
nouncement reference DCS-01042026-00004), and FFC’s
official financial-results document dated 29 January 2026
to its anchor (PSX document 269389). These are respec-
tively an annual-report announcement date and an issuer
document date, not authenticated first-earnings publica-
tion timestamps. Maxis remains declared-only: an AGM
notice date is insufficient publication evidence. Neither
fiscal period end nor an annual-report upload establishes
the first earnings-release timestamp. No dates or missing
price horizons are invented to recover excluded findings.
Bounded disclosure-dated cohort..A separate eligibility
ledger retains all eight PSX/MSX companies, rather than
selecting only successful cases. Exact observed-date Deci-
mal replay gives three numerical positives and five nega-
tives. Only FFC and Maybank have official dates match-
ing their anchors; four candidates lack verified matching
dates, and OGDC/PPL have wrong-period anchors without
September 2025 price coverage. FFC’s observed window
runs from 30 January to 13 March 2026: company return
is−14.8750361%versus supplied interpolated benchmark
−14.4853883%. Maybank’s runs from 2 April to 14 May:
company return is−2.4432810%versus proxy0 .3734215%.
Each contains 30 closes and 29 shared intervals, beginning
at the first post-disclosure close, not at a verified disclo-
sure baseline. FFC’s pre-anchor event closes are missing
and Maybank has no pre-anchor company prices. Both R1
positives are therefore illustrative disclosure-dated replays,
not authenticated initial reactions. No exact-date primary
benchmark replacement pair was obtained in the bounded
search. Eight controls pass, including rejection of missing
intermediate company or benchmark dates rather than
silent horizon truncation. These two cases are subsets of
earlier cohorts, not additional independent positives.
Issuer-published company-price recovery..A subsequent
source-acquisition pass recovered Maybank’s public
investor-relations CSV, containing 61 daily rows from 2
March to 29 May 2026. All 30 post-report company closes
match the archived values exactly. Additional as-published
closes are MYR11.360 on 31 March and MYR11.660 on 1
April; the 2 April and 14 May closes are MYR11.460 and
MYR11.180. Thus the earlier local absence of a baseline is
partially resolved by a separately hashed capture, without
altering historical graphs. Company-only endpoint returns
to 14 May are approximately−1.58451%from 31 March
and−4.11664%from 1 April, compared with−2.44328%
from the first post-report close. These are issuer-IR
republished values, not exchange-original authentication.
The export parameter unadjusted=0 is unexplained by
the viewed source, so adjustment basis remains unresolved.
No compatible primary KLCI observations were obtained;
neither a market-relative classification nor an initial
earnings reaction follows from this company-only recovery.
Source hashes, CSV field/line locators and four integrity
controls are retained; redistribution rights are not assumed.
Regulator-published PSX endpoint recovery..Normal pub-
lic attachment downloads subsequently recovered four origi-
nal SECP reports for 28–30 January and 13 March 2026. Vi-
sual review confirms eight unique observations: six KSE100
levels and FFC closes of PKR597.10 on 29 January and
PKR501.02 on 13 March. Repeated index values agree
across adjacent reports. The FFC endpoints give a de-
scriptive price change of approximately−16.09111%, not a
cash-distribution-adjusted return; the March row is explic-
itly marked XD. FFC is absent from the selected spot-price
tables in the recovered 28 and 30 January reports, so nei-
ther its required pre-disclosure baseline nor its first-post
close is filled by those documents. An opening price is not
substituted for a previous close. KSE100’s authenticated
levels remain total-return observations, incompatible with
the company price-only comparison; KSE100PR is still re-
quired. Thus original-source coverage improves, while the
market-relative finding remains unvalidated. The earlier
indexed-only ledger is retained as acquisition history; a sep-
arate source-hashed recovery ledger records the admitted
observations and five integrity/refusal controls.
PPL completion..The complete nine-page issuer results
letter was subsequently obtained fromhttps://www.ps
x.com.pk/psx/files-attachment/?file=259574.pdf .
Rendered page 3 confirms unconsolidated FY2025 revenue
242,516,363 and PAT 92,027,450 thousand PKR, and EPS
33.82; FY2024 comparatives are 288,797,413, 114,309,077
and 42.01. Four monetary cells need a factor of one million;
two EPS cells match. Ten validation checks pass. This
supersedes the earlier PPL pending status only through
the separate completion overlay. The issuer letter date of
19 September 2025 remains distinct from first-publication
time.
31
