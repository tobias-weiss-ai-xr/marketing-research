---
title: Agentic AI for Clustering, Relationship Discovery, and Semantic Trading in Prediction Markets
url: https://arxiv.org/abs/2512.02436
category: ai-marketing
subcategory: empirical
date: 2025-12
venue: ''
authors:
- Agostino Capponi
- Alfio Gliozzo
- Brian Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.02436
pages: 11
chars: 55862
fetched_at: '2026-11-08T13:18:37+00:00'
kb_version: 1
---

# Agentic AI for Clustering, Relationship Discovery, and Semantic Trading in Prediction Markets

Agentic AI for Clustering and Relationship Discovery in
Prediction Markets
Agostino Capponi
Columbia University
United States
ac3827@columbia.edu
Alfio Massimiliano Gliozzo
IBM Research
United States
gliozzo@us.ibm.com
Brian Zi Qi Zhu
Columbia University
United States
bzz2101@columbia.edu
Abstract
Prediction market platforms list thousands of contracts whose logi-
cal and economic connections are implicit in their resolution rules.
We introduce a hierarchical agentic reduction (HAR) pipeline for
constructing inspectable cross-event relation graphs and a behav-
ioral benchmark for evaluating their alignment with market prices.
This partitions a catalog of prediction markets, specified by question
and resolution text, into topic clusters, applies typed LLM reason-
ing to small batches, and proposes signed relations with rationales
between specific markets. We evaluate semantic relation graphs
spanning eight monthly Kalshi catalogs (February to September
2026). Using data from 30.3 million trades, we compute a benchmark
that compares linked pairs’ signed price-change correlations with
those of matched, unlinked controls from the same topic cluster on
identical timestamps. Under full-sample and leave-first-week-out
evaluation, relations identified by our pipeline exhibit higher signed
Pearson price-change correlations, with statistical significance, than
matched within-topic controls. This increase also appears under
Spearman correlation and becomes larger among relations labeled
as medium or high strength. This benchmark provides a criterion
for comparing relation-discovery methods against observations be-
yond their input text, and our results indicate the ability of agentic
AI and LLM reasoning to identify meaningful relations between
individual markets in connected Web marketplaces.
CCS Concepts
•Information systems → Graph-based database models;•
Computing methodologies→ Natural language processing;•
Applied computing→Economics.
Keywords
knowledge graph construction, hierarchical agentic reduction, pre-
diction markets, semantic relations, price correlation, temporal
evaluation
ACM Reference Format:
Agostino Capponi, Alfio Massimiliano Gliozzo, and Brian Zi Qi Zhu. 2027.
Agentic AI for Clustering and Relationship Discovery in Prediction Markets.
InProceedings of Submission to The ACM Web Conference 2027 (WWW ’27).
ACM, New York, NY, USA, 11 pages.
1 Introduction
Prediction-market contracts turn descriptions of future events into
individually addressable, tradable propositions. Each contract has a
question, an identifier, and a rule that specifies when its Yes outcome
holds. Across a platform, these descriptions form a fragmented rep-
resentation of connected uncertainties. For example, a central-bank
decision and a Treasury-yield threshold may share policy exposure,
resignation and early departure from office are naturally connected,
and two election questions may encode competing outcomes. These
relationships often cross the exchange’s event boundaries as well.
Recovering this structure is a Web knowledge-integration prob-
lem with practical consequences. Explicit cross-market relations
let traders and platforms detect incoherent prices across logically
linked contracts, construct hedges across separately listed events,
navigate and recommend related markets, and study how informa-
tion propagates through a market ecosystem. Yet platforms expose
contracts as isolated listings, and connections among their mean-
ings remain implicit in free-text resolution rules. A useful graph
must link propositions with different wording while respecting the
jurisdictions, deadlines, and thresholds that fix their meaning, and it
should be testable against evidence other than the text from which
its edges were inferred. Price changes provide an external measure
of a relation’s behavioral relevance. Their association reflects how
traders update valuations as information arrives, alongside differ-
ences in contract horizons and trading activity. Semantic validity
concerns the relationship between contract propositions; the price
benchmark measures how that relationship appears in observed
valuation changes.
We introduce HAR for constructing inspectable cross-event rela-
tion graphs and a behavioral benchmark for evaluating their align-
ment with market prices. HAR groups contracts through event-title
embeddings, reduces batches of markets to structured relation pro-
posals, and assembles validated proposals into a graph. Each edge
specifies two contract identities, an expected association sign, an
ordinal strength, and a rationale. The hierarchy consists of topic
partitioning, batch-level reasoning, and graph assembly. This design
makes each proposed relation inspectable and allows the model
to return an empty relation set when no connection is sufficiently
supported.
Our empirical question is whether selected edges, correspond-
ing to relations between prediction markets, align with price co-
movement more closely than comparable pairs drawn from the
same topic cluster.
We evaluate semantic relation graphs spanning eight monthly
Kalshi catalogs (Section 3.1). Our benchmark compares each linked
pair’s signed price-change correlation with that of activity-matched,
unlinked controls from the same topic cluster, computed on iden-
tical timestamps. Controls are matched on the first week of each
month; LFWO measures correlations over the remaining days. The
evaluated graph yields signed correlation advantages of +0.071
for three-hour changes and+0.033for daily changes under LFWO,
with a larger three-hour estimate of+0.107for medium/high re-
lations. The LLM used for relation generation has a documented
January 2025 knowledge cutoff [6], preceding February 2025 and
the 2026 evaluation period. Its inputs contain contract questions
1
arXiv:2512.02436v4  [cs.AI]  27 Oct 2026

WWW ’27, May 2027, Dublin, Ireland Capponi et al.
and resolution rules, excluding trade prices and settlement fields.
These results describe exploratory evidence from a retrospective
specification search; Section 4.4 gives the inference scope.
We make three contributions. First, we represent cross-event
propositions in a signed, attributed graph with exact contract iden-
tities, resolution conditions, and temporal scope. Second, we in-
troduce HAR, which combines topic partitioning and structured
LLM reasoning to propose individually justified relations from
contract descriptions. Third, we develop a behavioral benchmark
that measures signed price-correlation advantages over random
and activity-matched within-topic controls using identical obser-
vations. Analyses across temporal resolutions, relation strengths,
and sign assignments connect graph attributes to observed price
behavior. The construction workflow and benchmark together pro-
vide a reproducible task definition for comparing relation-discovery
methods.
2 Background and Related Work
Prediction markets and temporal evidence.Prediction markets
aggregate information through contingent claims [21]. A binary
market offers Yes and No contracts: a Yes contract pays $1 when its
proposition resolves affirmatively, and a No contract pays $1 when
it resolves negatively. These claims trade through mechanisms such
as limit order books and automated market makers. The resolution
rule ties each contract to a precisely specified proposition.
An individual contract in our catalog represents a binary propo-
sition, while an exchange event can contain several contracts de-
scribing alternative outcomes. For example, an election event may
offer separate Yes/No contracts for several candidates. When the al-
ternatives are mutually exclusive and collectively exhaustive, their
settlement indicators sum to one, creating a direct logical constraint
among contracts [8]. Other event structures permit overlapping
outcomes, so their resolution rules determine the applicable con-
straints. Our graph keeps contract identity separate from event
membership and focuses on relationships across distinct exchange
events.
We study the relationships implicit across separately listed con-
tracts. Recent LLM forecasting work evaluates probabilities against
realized outcomes [7], while ForecastBench emphasizes questions
beyond the forecaster’s available information [13]. Our correlation
benchmark evaluates an association between two evolving beliefs,
as a single pair of realized settlements offers limited evidence about
such an association, especially when an edge expresses shared
exposure rather than a strict logical constraint.
Related market-structure work combines topical embeddings,
temporal filters, and LLM judgments to identify combinatorial de-
pendencies on Polymarket [18]. Cross-platform semantic alignment
also relies on resolution conditions and temporal scope to establish
event identity [4]. Consistency checks for LLM forecasters eval-
uate logical constraints among their predicted probabilities [ 16].
Our benchmark asks how a signed cross-event graph, including
softer associations, aligns with observed price changes under shared
observation support and within-topic controls, and complements
these approaches through a behavioral criterion that can be applied
to alternative graph generators.
Knowledge graphs.Constructing a knowledge graph requires
choices about identity, schema, and context [9]. These choices are es-
pecially consequential for prediction markets: two questions about
the same person can be over different jurisdictions, have differ-
ent deadlines or thresholds, and use different resolution sources.
The unit of identity in our graph is the exchange contract. Event
membership and topic clusters are contextual attributes, while an
inferred relation is an additional, uncertain assertion about two
contract propositions.
Generative relation extraction methods, such as REBEL [1], map
text to structured ontologies. The Extract–Define–Canonicalize
method separates extraction, relation definition, and schema canon-
icalization for LLM-based graph construction [22]. Our setting adds
an external behavioral benchmark, as the endpoints denote con-
tracts with observable price histories. We note that our graph struc-
ture uses signed associations and rationales, and is less semantically
granular than a fully logical ontology.
Structured agentic workflows.Agentics expresses reasoning as
typed transductions between structured data objects [5]. We use
its batch-reduction abstraction to transform a set of market de-
scriptions into a selectively emitted set of edges. Compared with
a question-by-question forecasting system, the semantic output is
a relationship among propositions. Batching makes context size
manageable and creates a candidate-coverage trade-off that belongs
in the method specification.
3 Constructing the Semantic Relation Graph
3.1 Market sample and scope
We construct eight monthly Kalshi catalogs spanning February–
September 2026. The initial market selection uses Kalshi market
reports on Dune. For each report window, the query sums daily
volume by ticker and category, selects ticker–category groups with
cumulative reported volume of at least 10,000, and retrieves the
active and finalized subsets separately. Each query returns up to
10,000 ticker–category groups ordered by volume. We combine
these subsets and enrich the selected events with contract questions
and resolution rules. Enrichment also includes sibling contracts
within those events, so the volume threshold applies to the initial
selection. Appendix A.1 gives the exact query conditions.
The query excludes the source categories Crypto, Sports, Finan-
cials, Exotics, and Commodities, along with the KXHIGH, KXLOWT,
and KXRAIN ticker families for local weather outcomes. Our scope
emphasizes relationships that require interpreting context and res-
olution language across distinct events. Repeated sports fixtures,
cryptocurrency up/down questions, asset-price thresholds, and lo-
cal weather ladders can produce many closely templated contracts
whose connections follow directly from a common fixture, instru-
ment, or measurement. The exclusions reduce their influence on the
catalog and focus the benchmark on contextual relationships such
as political developments, institutional decisions, and economic
releases. The volume floor prioritizes observed market interest for
the later price-based evaluation. These choices define the scope
of the benchmark; the selected topics include politics, elections,
economics, companies, entertainment, and science and technology.
2

WWW ’27, May 2027, Dublin, Ireland
The evaluated catalogs contain 65,426 distinct market-month
observations and 47,075 unique tickers. The graph contains 5,667
monthly edges, corresponding to 5,315 distinct unordered ticker
pairs and 5,361 endpoint tickers. Of the monthly edges, 4,901 are
positive and 766 negative. This sign imbalance motivates the all-
positive sensitivity in Appendix D. Table 1 reports monthly catalog
and graph sizes alongside the trade-data coverage used for evalua-
tion.
3.2 Contract and edge representation
For a monthly catalog𝑚, we represent contract𝑖as
𝑥𝑚 𝑖 =(𝑡 𝑖,𝑒𝑖,𝑞𝑖,𝑟𝑖,𝜏𝑖),
where𝑡𝑖 is the ticker,𝑒𝑖 the exchange event,𝑞𝑖 the question,𝑟𝑖 the
resolution rule, and𝜏𝑖 the available temporal metadata. The latent
binary settlement proposition is𝑌𝑖. The LLM receives the market
information: a question about an event and its resolution criteria.
Note that the price series and settlement outcomes are excluded
from these input fields.
The graph𝐺𝑚 =(𝑉𝑚,𝐸𝑚) has ticker-addressed vertices and edge
assertions
𝑎𝑚 𝑖𝑗 =(𝑡 𝑖,𝑡𝑗,𝑜𝑖𝑗,𝑠𝑖𝑗,ℎ𝑖𝑗,𝑧𝑖𝑗),
The proposed endpoint ordering is 𝑜𝑖𝑗 , and the association sign
is𝑠𝑖𝑗 ∈ {−1,+ 1}. The ordinal strength ℎ𝑖𝑗 takes the values low,
medium, or high;𝑧𝑖𝑗 is the rationale.
The rationale describes the asserted mechanism under which the
markets are related. An implication, a shared macroeconomic expo-
sure, and a competitive relationship have distinct interpretations
even if two of them share a sign. Strength also remains separate
from relation type: a high-strength label is an ordinal judgment
rather than an estimated probability of correctness.
3.3 Topic clustering and relationship discovery
Clustering a monthly catalog by topic.We embed normalized
event titles using the Sentence-BERT modelall-MiniLM-L6-v2 [17,
19]. Unit-normalized vectors are reduced to ten dimensions by
UMAP using cosine distance with thirty neighbors and a zero mini-
mum distance [15]. We then use HDBSCAN to cluster the embed-
dings, requiring a minimum cluster size of four and a minimum sam-
ple size of two per cluster [14]. Distance-weighted nearest-neighbor
assignment places remaining markets, initially categorized as noise,
into established clusters where possible. Contracts inherit their
event’s cluster, and cluster labels are local to a monthly catalog,
with no shared cluster identity across months.
Within-cluster relationship discovery.Let 𝐶𝑚𝑐 contain the con-
tracts assigned to cluster𝑐. HAR partitions its contracts into batches
𝐵𝑚𝑐𝑘 of at most ten and applies the typed transducer𝑇𝜃 :
R𝑚𝑐𝑘 =𝑇𝜃(𝐵𝑚𝑐𝑘 ;I,S),
𝐸𝐻 𝑚 =V
 Ø
𝑐,𝑘
R𝑚𝑐𝑘
!
.
HereI gives the relation-selection instructions, S declares the
output fields, andV resolves identities and enforces graph con-
straints. A batch may emit zero edges. The model considers several
propositions together and chooses which relationships to express;
the output size is determined by selection rather than a required
edge quota.
We require the two endpoints of a proposed relation to belong to
different exchange events. Contracts within one event often share
a resolution source and describe mutually exclusive outcomes or
nested numerical thresholds. Their relationships can follow directly
from that event’s structure. The cross-event requirement focuses
discovery on connections across separately listed questions, such
as a policy decision and an economic release. The prompt requests
different event titles, and the validator checks distinct exchange
event tickers after resolving the endpoint descriptions. Topic-cluster
membership supplies candidate context while this event check
defines the pairs included in the evaluation.
Agentics’ areduce implementation wraps each batch as a typed
input and performs asynchronous batch transductions. Graph as-
sembly unions their outputs. The hierarchy consists of the catalog,
topic clusters, batches, and edge assertions. HAR evaluates rela-
tionships within each batch, so candidate coverage depends on the
cluster partition and batch ordering. Exhaustive pairwise inference
can assess pairs across batch boundaries within the same contract
universe.
3.4 Implementation details
Our prompt for the agentic pipeline requires exact reproduction
of each endpoint’s question and primary resolution rule. The val-
idator resolves these descriptions to unique exchange tickers and
checks distinct market tickers, distinct event tickers, and common
membership in a monthly topic cluster. For contemporaneous price
correlations, each unordered market pair contributes once, regard-
less of the order of its two tickers. Duplicate edges are collapsed,
and pairs with conflicting signs are excluded.
We use Gemini 3.1 Pro with zero temperature and a fixed seed.
Google reports a January 2025 knowledge cutoff [ 6], which pre-
cedes February 2025 and is more than a year before the evaluation
period. Model inputs contain contract questions and resolution
rules, excluding trade prices and settlement fields. The model rea-
sons without Web search or news retrieval. The cutoff describes its
learned information; graph construction and evaluation are retro-
spective, and temporal validity also depends on the versions and
dates of input metadata.
3.5 Worked example
As an illustrative example, consider four contracts from a March
2026 cluster of questions about Donald Trump’s term in office. Their
questions concern impeachment, impeachment and removal, res-
ignation, and early departure from office. Topic similarity places
them in a common search context, and resolution rules supply the
distinctions needed for relation selection. The removal contract re-
quires impeachmentandSenate conviction before 20 January 2029,
whereas the departure contract requires leaving office before that
date; the resignation contract concerns the elected 2025–2029 term.
Appendix A.2 contains the full input descriptions and a relation
example.
For removal and departure, the output assigns direction=true
and strength=high, and explains that conviction and removal
3

WWW ’27, May 2027, Dublin, Ireland Capponi et al.
Contract questions
and resolution rules
Event-title
embeddings
and topic clusters
Batches of up to ten
typed LLM reduction
Exact identity checks
and edge assembly
Pooled semantic
relation graph
Observed trades
February–
September 2026
First-week controls
and common
timestamps
Sign-aligned
price-change
correlation
benchmark
Figure 1: Graph construction and evaluation. The top path shows the HAR contribution to the semantic relation graph. Traded-
price data enters through another path, supplying controls and observations for correlation evaluation.
A: DJT impeached
before 20 Jan 2029
B: DJT impeached
and convicted
before 20 Jan 2029
C: DJT re-
signs during
the 2025–2029 term
D: DJT leaves office
before 20 Jan 2029
+
medium
+, high
+, high
Figure 2: An example semantic relation graph. Arrows indi-
cate the proposed ordering and carry association signs and
strength labels. Rationales distinguish the prerequisite re-
lation A to B from the departure mechanisms B to D and
C to D. Appendix A.2 gives exact descriptions and tickers.
Selection of this illustration is independent of correlation
performance.
entail leaving office within the specified horizon. A second high-
strength positive edge connects resignation to departure. These
edges express distinct mechanisms linking to the same departure
contract. Their rationales make the semantic basis inspectable be-
fore any correlation is calculated.
The impeachment-only contract adds a useful distinction. Its
edge to removal has medium strength: House impeachment is a pre-
requisite for Senate conviction, and subsequent conviction remains
uncertain. This rationale motivates a positive association while pre-
serving the extra condition in the removal rule. The strength label
indicates the generator’s judgment about that relationship. Each
edge includes its rationale alongside the label, allowing readers to
inspect the reasoning.
Figure 2 shows the resulting local graph (excluding other markets
in the cluster that would also be related). The removal-to-departure
relation, for example, is mapped to
KXTRUMPREMOVE→KXTRUMPOUT27-27-JAN2029
Correlation evaluation uses the validated tickers and association
sign; the contract text and rationale explain the semantic basis of
each edge.
4 A Trade-Price Correlation Benchmark
For assessing behavioral relevance, trade-price histories offer a
more direct empirical reference than annotator judgments. They
reflect transactions by financially exposed participants and provide
repeated observations of how market valuations change as infor-
mation arrives [21]. Fixed sampling rules and matched controls
Table 1: Monthly market sample and trade-data coverage.
Markets, clusters, and edges describe the graph catalogs.
Traded counts markets with at least one trade; Trades
counts trades in millions. Eligible pairs satisfy the shared-
observation and price-variation requirements in at least one
configuration at the reported intervals.
Markets Clusters Edges Traded Trades
Eligible
pairs
Feb 6,880 41 760 6,363 3.39 207
Mar 6,726 53 1,740 5,623 2.28 245
Apr 6,077 89 370 5,565 3.22 153
May 6,510 108 420 5,779 3.12 50
Jun 8,288 116 534 7,774 4.75 61
Jul 7,908 97 531 7,382 5.51 58
Aug 9,660 91 662 8,854 4.19 70
Sep 13,377 90 650 12,021 3.85 84
make the comparison repeatable across graph generators. Human
annotation assesses semantic plausibility and rationale quality;
price correlation measures how a proposed relation is expressed in
observed market behavior.
4.1 Trade histories and observed prices
For the monthly catalogs described in Section 3.1, we obtain trade
histories containing market tickers, execution timestamps, and Yes
prices in dollars [ 12]. Each monthly evaluation uses only trades
executed within that UTC calendar month, with prices in[0, 1]. The
resulting input contains 30,311,603 trade observations across 59,361
market-months with observed trades.Eligible relation pairshave
sufficient overlapping price observations and price variation for
correlation analysis. The observation requirements apply jointly
to each pair and its control (Section 4.2). Table 1 counts monthly
relation pairs eligible in at least one configuration at the reported
intervals.
For intervalℎ∈{ 3, 12, 24} hours,𝑝(ℎ) 𝑖,𝑡 is the last observed Yes
trade price in UTC bin𝑡, with empty bins excluded.1 A price change
over𝑘bins is defined as
𝑑(ℎ,𝑘) 𝑖,𝑡 =𝑝(ℎ) 𝑖,𝑡 −𝑝(ℎ) 𝑖,𝑡−𝑘, 𝑘∈{1,3}.
Dollar changes respect the bounded probability scale and remain de-
fined at zero. The main analysis uses one-bin price changes (𝑘= 1),
1Execution times within a common bin can differ across contracts.
4

WWW ’27, May 2027, Dublin, Ireland
so the horizon of change equals the sampling interval. Varying this
interval from three hours to one day examines co-movement across
temporal resolutions [3], while holding the change definition fixed.
Pearson measures linear association; Spearman evaluates ranked
changes using the same controls, timestamp rules, and aggrega-
tion. Three-bin changes provide another longer-horizon robustness
check, and may bridge a missing intermediate bin and overlap in
time, measuring changes over a longer horizon.
4.2 Random and matched controls
For edge(𝑖,𝑗) , market 𝑖 is the common anchor; we select up to
three control contracts𝑢 from its cluster. Control candidates must
belong to a different event from𝑖, have at least four observed first-
week hourly prices, and no known graph link to𝑖 in either source.
Thus, an omitted graph edge represents an unselected pair. Genuine
undiscovered relationships may remain among the controls. The
benchmark compares graph-selected pairs with these unselected
pairs under the same observation requirements.
We use two baselines: therandom baselinesamples control can-
didates uniformly, and thematched baselineranks candidates by
squared standardized distance from market𝑗 on first-week mean
price, log observed activity, and log root-mean-square hourly price
change. To compare the matching features on a common scale, we
divide each feature difference by its standard deviation across can-
didate control markets. At most 200 control candidates are sampled
for each anchor using a stable seed, with the closest three being se-
lected for the matched baseline. Appendix B gives the exact feature
definitions and sparse-history conventions.
We use the first seven UTC days of each month forcontrol match-
ing. Their price, activity, and variability features determine the
controls, whose identities are then kept fixed.LFWO (leave-first-
week-out)measures correlations from day eight through month-end.
LFWO separates first-week control matching from subsequent cor-
relation measurement. Full-month evaluation uses the complete
calendar month and provides greater observation coverage. Both
periods use the same selected controls. Graph construction and
specification selection are retrospective.
For each triple(𝑖,𝑗,𝑢) , where𝑖 is the common anchor market, 𝑗
is linked to𝑖 in the cluster relation graph, and𝑢 is a control market
assigned to𝑖, we calculate𝜌(𝑖,𝑗) and𝜌(𝑖,𝑢) usingthe same times-
tamp mask, requiring finite price changes for all three contracts.
We also require that each window has 12 common observations
spanning at least half its length, at least three nonzero changes in
each series, and positive variance. These requirements determine
whether a relation pair has sufficient shared observations and price
variation for comparison with that control, and all filtering applies
jointly to the triple.
4.3 Estimation and aggregation
For relation sign𝑠𝑖𝑗 , a triple’s signed correlation advantage is
𝛿𝑖𝑗𝑢,𝑤 =𝑠𝑖𝑗[𝜌𝑤(𝑖,𝑗)−𝜌 𝑤(𝑖,𝑢)].
We use Pearson correlation for one- and three-bin changes and
Spearman correlation for one-bin changes. For a positive edge, the
score increases when the linked pair’s correlation exceeds the con-
trol correlation; for a negative edge, it increases when the linked
pair’s correlation is more negative. A value of+0.1is an advantage
of one tenth of a correlation unit after applying the graph sign
to both terms. Separate sign and absolute-correlation sensitivities
evaluate polarity assignment and association magnitude. The eval-
uation window specifies the period over which each correlation is
estimated.Full monthuses the entire UTC calendar month, includ-
ing the control-matching week.LFWOuses the remaining month to
estimate one correlation per pair and control. Both endpoint prices
of every included LFWO change must lie on or after the start of
day eight. The7-dayand14-day rollingsensitivities estimate corre-
lations separately in windows of those lengths after the matching
week, advancing by seven days and averaging the valid window
correlations.
Windows are averaged within each triple, valid controls within
each edge, and edges within each month-cluster. Let ¯𝛿𝑚𝑐 be that
cluster mean andC𝑚 the clusters containing eligible relation pairs.
The reported effect is
bΔ= 1 𝑀 𝑀∑︁ 𝑚=1 1 |C𝑚| ∑︁ 𝑐∈C 𝑚 ¯𝛿𝑚𝑐.(1)
Months and their eligible clusters receive equal weight. A market
appearing in several months can contribute several edge-month
observations; the count describes coverage rather than independent
replications. Strength restrictions use the same control assignments
and recalculate cluster and month means using eligible pairs in
each strength subset.
4.4 Statistical inference
Market pairs share contracts, respond to common news, and recur
across months [2]. Our main inference uses each month’s equal-
cluster mean, bΔ𝑚, as one observation, allowing dependence among
all comparisons within that month. Let𝑠Δ be the sample standard
deviation of the𝑀 monthly effects. We report the two-sided month-
level statistic
𝑇=
bΔ
𝑠Δ/
√
𝑀
, bΔ±𝑡 𝑀−1,0.95 𝑠Δ√ 𝑀 .
The second expression gives the pointwise 90% confidence interval.
The main table uses a Student 𝑡 reference with𝑀− 1degrees of
freedom; its comparisons have 𝑀= 8and seven degrees of free-
dom. This grouped approach assumes approximately independent,
Gaussian monthly estimates [11]; recurring markets and serial news
transmission are relevant to that assumption.
We apply the same test and interval to Pearson and Spearman,
all three intervals, both measurement periods, and each strength
restriction. We conduct a retrospective specification analysis across
these choices [20]. The𝑝-values describe exploratory evidence for
individual settings. Appendix F gives the evaluation scope and
complementary month-level checks.
5 Results
The primary results report signed Pearson price-change correla-
tion advantages for all strengths at 3, 12, and 24 hours under Full
month and LFWO evaluation. Table 2 gives the effects and two-sided
month-level𝑝-values; Figure 3 shows the corresponding pointwise
5

WWW ’27, May 2027, Dublin, Ireland Capponi et al.
Table 2: Signed Pearson price-change correlation advantages,
all strengths, against matched controls. Hours gives sam-
pling interval and change horizon; Δ is signed correlation
advantage;𝑁 counts eligible edge-months. All 𝑝-values are
two-sided month-level 𝑡-test values with seven degrees of
freedom.∗𝑝<0.10, ∗∗𝑝<0.05, ∗∗∗𝑝<0.01.
Period HoursΔ𝑝 𝑁
Full month 3 +0.0260.2813342
Full month 12 +0.0420.0024 ∗∗∗ 599
Full month 24 +0.0420.0369 ∗∗ 692
LFWO 3 +0.0710.0027 ∗∗∗ 301
LFWO 12 +0.0200.2739517
LFWO 24 +0.0330.0019 ∗∗∗ 595
90% intervals. A three-hour LFWO comparison examines rank as-
sociation and relation strength under the same controls and ob-
servation rules. Appendix C provides the complete Spearman and
strength analyses.
5.1 Temporal resolution
Table 2 shows positive full-month Pearson advantages at each re-
ported interval, ranging from+0.026to+0.042. The 12-hour effect is
positive in all eight months (𝑝= 0.0024); the daily effect is positive
in seven (𝑝= 0.0369). These comparisons link the graph’s cross-
event connections to price associations beyond matched within-
topic controls. Each interval measures ordinary one-bin changes,
giving the same interpretation to its sampling interval and change
horizon.
Under LFWO, three-hour Pearson gives +0.071on 301 edge-
months across 97 month-clusters, with seven positive months (𝑝=
0.0027). Daily changes give+0.033on 595 edge-months, positive in
all eight months (𝑝= 0.0019). These settings demonstrate comple-
mentary strengths: a larger three-hour association advantage and
consistent daily effects across the sample period. Figure 3 places
these findings within the complete interval sequence and shows
the variation in precision across settings.
5.2 Robustness checks
Table 3 keeps the three-hour LFWO design fixed and changes the
association statistic and strength restriction. Spearman yields an
advantage of+0.073(𝑝= 0.0131), supporting the finding through
ranked price changes. Medium/high relations yield+0.107under
Pearson (𝑝= 0.0112) and+0.100under Spearman (𝑝= 0.0282). All
four comparisons are positive in seven of eight months. The re-
striction includes 223 of the 301 eligible edge-months and increases
the observed advantage by0 .036under Pearson and0 .028under
Spearman.
Medium/high strength labels identify pairs with larger correla-
tion advantages under both Pearson and Spearman. Appendix C
reports the full interval and strength grids, and Appendix E fixes
eligible edge membership across intervals. On that common cohort,
three-hour LFWO Spearman gives+0.072.
Table 3: Three-hour LFWO robustness against matched con-
trols. Δ is signed correlation advantage; 𝑁 counts eligible
edge-months. All𝑝-values are two-sided month-level 𝑡-test
values with seven degrees of freedom. ∗𝑝< 0.10,∗∗𝑝< 0.05,
∗∗∗𝑝<0.01.
Statistic StrengthΔ𝑝 𝑁
Pearson All +0.0710.0027 ∗∗∗ 301
Pearson Medium/high +0.1070.0112 ∗∗ 223
Spearman All +0.0730.0131 ∗∗ 301
Spearman Medium/high +0.1000.0282 ∗∗ 223
6 Discussion
Our piepeline organizes contract descriptions into topic clusters,
proposes cross-event relations through structured reasoning, and
anchors each assertion to an exact tradable proposition. The be-
havioral benchmark evaluates whether a relation graph captures
signed price associations beyond matched within-topic controls. For
the evaluated graph, three-hour Pearson and Spearman yield posi-
tive signed correlation advantages, with larger point estimates for
medium/high relations. These findings provide behavioral evidence
for graph-selected links under the stated controls and observation
rules. Controlled comparisons between graph generators can quan-
tify the contribution of individual construction steps.
The worked example shows how this structure becomes inter-
pretable. A resolution rule fixes the proposition, a ticker fixes its
identity, and a rationale explains the proposed mechanism. The
removal and resignation edges express distinct routes to early de-
parture; the impeachment edge indicates a prerequisite with an
additional condition. Each proposed relation can be checked against
the contracts’ resolution rules.
The resulting benchmark supports controlled comparisons of
graph-construction methods. Applying the same model and schema
to direct pairs on a fixed contract universe can quantify the contri-
bution of grouping and batch reasoning. Global candidate retrieval
offers a complementary comparison, and blinded annotation can
measure semantic precision and rationale faithfulness.
Explicit contract identities, relation signs, and rationales sup-
port inspection of the semantic assertions alongside behavioral
evaluation. The generating LLM’s documented pre-February-2025
knowledge horizon and exclusion of price inputs define its informa-
tion boundary. LFWO separately partitions control matching and
correlation measurement. A prospective study would additionally
fix graph membership, metadata, and evaluation specifications be-
fore observing the measurement period. Section 4.4 specifies the
retrospective inference scope used here.
7 Conclusion
Our pipeline turns contract language into a structured graph of
cross-event relationships with exact identities, resolution condi-
tions, and inspectable rationales. The accompanying benchmark
tests the behavioral relevance of graph-selected links through signed
price-correlation advantages over within-topic controls. For the
evaluated graph, three-hour Pearson advantages under LFWO are
+0.071overall and +0.107for medium/high relations; Spearman
6

WWW ’27, May 2027, Dublin, Ireland
3 12 24
Sampling interval / change horizon (hours)
0.000
0.025
0.050
0.075
0.100Signed correlation advantage
Full month
3 12 24
Sampling interval / change horizon (hours)
LFWO
Figure 3: Signed Pearson price-change correlation advantages for all strengths at 3-, 12-, and 24-hour intervals against matched
controls. Full month uses the complete calendar month; LFWO uses the period after the first control-matching week. Bars are
pointwise 90% month-level𝑡-intervals corresponding to the tests in Table 2.
gives+0.073and+0.100. All four comparisons are positive in seven
of eight months. Full-month 12-hour Pearson advantages and daily
Pearson advantages under LFWO are positive in all eight months.
Overall, our pipeline and the benchmark make the relationships
implicit in prediction-market contracts explicit, inspectable, and em-
pirically testable against the collective beliefs expressed in market
prices.
References
[1] Pere-Lluís Huguet Cabot and Roberto Navigli. 2021. REBEL: Relation Extraction
By End-to-End Language Generation. InFindings of the Association for Com-
putational Linguistics: EMNLP 2021. Association for Computational Linguistics,
2370–2381. doi:10.18653/v1/2021.findings-emnlp.204
[2] A. Colin Cameron and Douglas L. Miller. 2015. A Practitioner’s Guide to Cluster-
Robust Inference.Journal of Human Resources50, 2 (2015), 317–372. doi:10.3368/
jhr.50.2.317
[3] Thomas W. Epps. 1979. Comovements in Stock Prices in the Very Short Run.J.
Amer. Statist. Assoc.74, 366a (1979), 291–298. doi:10.1080/01621459.1979.10482508
[4] Jonas Gebele and Florian Matthes. 2026. Semantic Non-Fungibility and Violations
of the Law of One Price in Prediction Markets. arXiv:2601.01706 doi:10.48550/
arXiv.2601.01706
[5] Alfio Gliozzo, Naweed Khan, Christodoulos Constantinides, Nandana Mihin-
dukulasooriya, Nahuel Defosse, and Junkyu Lee. 2025. Transduction Is All You
Need for Structured Data Workflows.arXiv preprint arXiv:2508.15610(2025).
doi:10.48550/arXiv.2508.15610
[6] Google. 2026. Gemini 3 Developer Guide. Model table documents a January
2025 knowledge cutoff for gemini-3.1-pro-preview; accessed October 23, 2026.
https://ai.google.dev/gemini-api/docs/gemini-3
[7] Danny Halawi, Fred Zhang, Chen Yueh-Han, and Jacob Steinhardt. 2024.
Approaching Human-Level Forecasting with Language Models. InAdvances in
Neural Information Processing Systems, Vol. 37. https://proceedings.neurips.
cc/paper_files/paper/2024/hash/5a5acfd0876c940d81619c1dc60e7748-Abstract-
Conference.html
[8] Robin Hanson. 2003. Combinatorial Information Market Design.Information
Systems Frontiers5, 1 (2003), 107–119. doi:10.1023/A:1022058209073
[9] Aidan Hogan, Eva Blomqvist, Michael Cochez, Claudia d’Amato, Gerard de
Melo, Claudio Gutierrez, José Emilio Labra Gayo, Sabrina Kirrane, Sebastian
Neumaier, Axel Polleres, Roberto Navigli, Axel-Cyrille Ngonga Ngomo, Sabbir M.
Rashid, Anisa Rula, Lukas Schmelzeisen, Juan Sequeda, Steffen Staab, and Antoine
Zimmermann. 2021. Knowledge Graphs.Comput. Surveys54, 4, Article 71 (2021),
37 pages. doi:10.1145/3447772
[10] Sture Holm. 1979. A Simple Sequentially Rejective Multiple Test Procedure.
Scandinavian Journal of Statistics6, 2 (1979), 65–70. https://www.jstor.org/stable/
4615733
[11] Rustam Ibragimov and Ulrich K. Müller. 2010. t-Statistic Based Correlation and
Heterogeneity Robust Inference.Journal of Business & Economic Statistics28, 4
(2010), 453–468. doi:10.1198/jbes.2009.08046
[12] Kalshi. 2026. Get Trades and Get Historical Trades: API Documentation. See
also https://docs.kalshi.com/api-reference/market/get-trades; accessed October
23, 2026. https://docs.kalshi.com/api-reference/historical/get-historical-trades
[13] Ezra Karger, Houtan Bastani, Chen Yueh-Han, Zachary Jacobs, Danny Ha-
lawi, Fred Zhang, and Philip E. Tetlock. 2025. ForecastBench: A Dynamic
Benchmark of AI Forecasting Capabilities. InInternational Conference on Learn-
ing Representations. https://proceedings.iclr.cc/paper_files/paper/2025/hash/
ea74e45a229dac70b5b63b28d8934db6-Abstract-Conference.html
[14] Leland McInnes, John Healy, and Steve Astels. 2017. hdbscan: Hierarchical
Density Based Clustering.Journal of Open Source Software2, 11 (2017), 205.
doi:10.21105/joss.00205
[15] Leland McInnes, John Healy, Nathaniel Saul, and Lukas Großberger. 2018. UMAP:
Uniform Manifold Approximation and Projection.Journal of Open Source Software
3, 29 (2018), 861. doi:10.21105/joss.00861
[16] Daniel Paleka, Abhimanyu Pallavi Sudhir, Alejandro Alvarez, Vineeth Bhat, Adam
Shen, Evan Wang, and Florian Tramèr. 2025. Consistency Checks for Language
Model Forecasters. InInternational Conference on Learning Representations. https:
//arxiv.org/abs/2412.18544
[17] Nils Reimers and Iryna Gurevych. 2019. Sentence-BERT: Sentence Embeddings
Using Siamese BERT-Networks. InProceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the 9th International Joint Conference
on Natural Language Processing. Association for Computational Linguistics, 3982–
3992. doi:10.18653/v1/D19-1410
[18] Oriol Saguillo, Vahid Ghafouri, Lucianna Kiffer, and Guillermo Suarez-Tangil.
2025. Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets. In7th
Conference on Advances in Financial Technologies (AFT 2025) (Leibniz International
Proceedings in Informatics (LIPIcs), Vol. 354). Schloss Dagstuhl – Leibniz-Zentrum
für Informatik, Dagstuhl, Germany, 27:1–27:24. doi:10.4230/LIPIcs.AFT.2025.27
[19] Sentence Transformers. 2021. all-MiniLM-L6-v2 Model Card. Accessed October
23, 2026. https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
[20] Uri Simonsohn, Joseph P. Simmons, and Leif D. Nelson. 2020. Specification Curve
Analysis.Nature Human Behaviour4 (2020), 1208–1214. doi:10.1038/s41562-020-
0912-z
[21] Justin Wolfers and Eric Zitzewitz. 2004. Prediction Markets.Journal of Economic
Perspectives18, 2 (2004), 107–126. doi:10.1257/0895330041371321
[22] Bowen Zhang and Harold Soh. 2024. Extract, Define, Canonicalize: An LLM-
based Framework for Knowledge Graph Construction. InProceedings of the 2024
Conference on Empirical Methods in Natural Language Processing. Association for
Computational Linguistics, 9820–9836. doi:10.18653/v1/2024.emnlp-main.548
7

WWW ’27, May 2027, Dublin, Ireland Capponi et al.
A Graph Construction Details
We construct the graph as follows. Its batch boundary defines which
contracts the model considers jointly; union and validation assem-
ble those decisions into the graph.
Input:monthly contract catalog 𝑋 ; batch size𝑏= 10; model
𝜃; typed edge schema.
1. Embed unique event titles and assign topic clusters.
2. For each cluster 𝐶, partition its ordered contracts into
batches𝐵 𝑘 of size at most𝑏.
3. Apply the typed LLM transducer to each𝐵𝑘 with event
title, question, and primary resolution rule as inputs. Allow
an empty relation list.
4. For every proposed edge, resolve its endpoint texts to
unique tickers and enforce the event and cluster eligibility
rules.
5. Canonicalize each unordered pair, collapse duplicates, and
exclude sign conflicts.
Output:signed relation edges with strength and rationale,
indexed by month and source.
The generation prompt asks the model to select related pairs,
reproduce their endpoint descriptions exactly, assign a Boolean
for likely same/different outcomes, provide a low/medium/high
strength, and justify each choice. It requires different event titles
and imposes no edge quota. This schema supports a selective graph
while distinguishing an outcome judgment from a measured price
correlation.
A.1 Market selection query
The market-selection query selects reports whose timestamps fall
between DateStart and DateStop, with both endpoints included.
It groups by ticker and category, sums daily_volume, and selects
groups with total volume at least 10,000. The status filter uses
the group’s maximum reported status string, as implemented by
MAX(status); separate calls request active and finalized. The
query excludes the report categories Crypto, Sports, Exotics, Un-
known, and Financials, and tickers containingKXHIGH,KXLOWT, or
KXRAIN. Results are ordered by total volume and limited to 10,000
ticker–category groups per call. The date predicate concerns report
timestamps; trade-price evaluation uses the UTC calendar-month
restriction in Section 4.
The category and volume conditions define the initial market
sample. Event enrichment retrieves sibling contracts and API meta-
data, so individual contracts in the expanded catalogs can have
lower reported volume, and API category labels can differ from the
source-report categories. For example, the April report classifies
ticker KXROCKANDROLLHALLOFFAME-26-MAR as Entertainment; API
enrichment labels its event Sports. Selection uses the report ta-
ble’s taxonomy. The monthly counts describe the clustered catalogs
assembled retrospectively after event enrichment.
A.2 Worked-example details
Table 4 gives the four input descriptions behind Figure 2. The three
illustrated edges are LLM outputs for the March 2026 catalog: B
to D and C to D have direction=true and high strength; A to B
has direction=true and medium strength. The node letters are
presentation aids. Contract identity is fixed by the ticker, and a
description match uses the complete question and rule.
For B to D, market_info_leader contains B’s complete descrip-
tion. The field market_info_follower contains D’s. The Boolean
directionis true, andstrengthis high. The rationale reads:
If Trump is impeached and convicted by the Senate, he will
be removed from office, meaning he will leave office before
January 20, 2029. The leader market resolving to Yes guar-
antees the follower market resolves to Yes.
The rationale asserts an implication from removal to departure. The
sign specifies the proposed association; conditional probability and
temporal price leadership require separate estimation. For A to B,
the rationale identifies impeachment as a necessary prerequisite
for removal and predicts a positive association. These rationales
distinguish two mechanisms behind edges with the same sign.
B Control Features and Observation Rules
Let𝑝(1) 𝑖,𝑡 be an observed hourly price in the first seven UTC days.
The features for market𝑖 are its observed mean price, log(1+𝑛𝑖)
with𝑛𝑖 observed first-week hourly prices, and log(𝑣𝑖+ 10−5). Here
𝑣𝑖 =
√︄˝
𝑡∈O 𝑖(𝑝(1) 𝑖,𝑡 −𝑝(1) 𝑖,𝑡−1)2
max(1,|O 𝑖|) ,
andO𝑖 requires both adjacent prices. Means use a denominator of
at least one, so a history with no observations has mean and RMS
change zero. Such a market can occur as a relation endpoint; control
candidates require𝑛𝑖≥ 4. The convention permits matching for a
sparse endpoint while limiting the interpretation of feature balance
in that case.
Squared feature distance divides each coordinate by its standard
deviation among control candidates. Coordinates with scale below
10−8 use scale one. The candidate cap is 200, and the maximum num-
ber of controls per edge is three. Stable hash-derived seeds make
control sampling reproducible; the configuration seed is 20261022.
Matches are selected at hourly frequency once and held fixed across
all measurement specifications.
Eligible relation pairs have sufficient overlapping price obser-
vations and price variation for correlation analysis with a control.
For each triple, a missing observation in any of its three series
removes that timestamp from both correlations. At least 12 shared
observations must span at least half the window. Each change series
must contain three changes exceeding10−10 in absolute value. The
correlation denominator must exceed10−12. Spearman ranks are
computed within the common mask. Per-edge relation scores can
vary across controls because their common masks vary. Scores are
averaged using the sequence in Equation (1).
C Correlation and Strength Robustness
Table 5 and Figure 4 evaluate Pearson and Spearman at 3-, 12-, and
24-hour intervals under Full month and LFWO. All-strength and
medium/high comparisons cover all eight months. The high-only
three-hour settings cover seven months; the high-only 12- and 24-
hour settings cover eight. Each restriction uses the same control
assignments and recomputes cluster and month means over the
selected edges. This applies the same benchmark to each strength
subset, allowing comparison of effect size and precision.
Under three-hour LFWO, Pearson gives+0.107for medium/high
relations and+0.071overall. Spearman gives +0.100and +0.073.
8

WWW ’27, May 2027, Dublin, Ireland
Table 4: Exact contract descriptions for the worked construction example. Questions and primary resolution rules are reproduced
from the relation endpoints. Each row maps to a unique exchange ticker.
Node Ticker Question and primary resolution rule
AKXIMPEACH-29-JAN20 Will the President be impeached before Jan 20, 2029? If the President of the United States has been impeached
before Jan 20, 2029, then the market resolves to Yes.
BKXTRUMPREMOVE Will Trump be impeached and removed from office? If the President of the United States has been impeached
and convicted by the U.S. Senate before Jan 20, 2029, then the market resolves to Yes.
CKXTRUMPRESIGN Will President Trump resign before his term is up? If the President of the United States elected for the
2025-2029 term resigns the office, then the market resolves to Yes.
DKXTRUMPOUT27-27-
JAN2029
Will Donald Trump leave office before January 20, 2029? If Donald Trump leaves office before January 20,
2029, then the market resolves to Yes.
Table 5: Complete correlation and strength results against matched controls. Hours gives sampling interval and change horizon;
Δ is signed correlation advantage; 𝑁 counts eligible edge-months. All 𝑝-values are two-sided month-level 𝑡-test values. All
and medium/high use eight months; high-only uses seven months at three hours and eight at the other intervals. ∗𝑝< 0.10,
∗∗𝑝<0.05, ∗∗∗𝑝<0.01.
All strengths Medium/high High only
Period HoursΔ𝑝 𝑁Δ𝑝 𝑁Δ𝑝 𝑁
Pearson price-change correlation
Full month 3 +0.0260.2813342 +0.0390.0804 ∗ 244 +0.1370.0852 ∗ 130
Full month 12 +0.0420.0024 ∗∗∗ 599 +0.0420.1596373 +0.0290.5083192
Full month 24 +0.0420.0369 ∗∗ 692 +0.0470.0985 ∗ 410 +0.0580.4058215
LFWO 3 +0.0710.0027 ∗∗∗ 301 +0.1070.0112 ∗∗ 223 +0.2130.0103 ∗∗ 120
LFWO 12 +0.0200.2739517 +0.0270.4665342 +0.0510.4387177
LFWO 24 +0.0330.0019 ∗∗∗ 595 +0.0540.1486368 +0.1330.2699194
Spearman price-change correlation
Full month 3 +0.0260.2590342 +0.0320.0819 ∗ 244 +0.1290.0975 ∗ 130
Full month 12 +0.0240.0442 ∗∗ 599 +0.0250.3399373 +0.0060.8758192
Full month 24 +0.0200.2216692 +0.0140.4798410 +0.0400.5363215
LFWO 3 +0.0730.0131 ∗∗ 301 +0.1000.0282 ∗∗ 223 +0.1870.0226 ∗∗ 120
LFWO 12 +0.0150.4304517 +0.0260.4503342 +0.0250.7133177
LFWO 24 +0.0180.0873 ∗ 595 +0.0280.2184368 +0.0880.4174194
Full-month Pearson means are also larger in the restricted subset
at each interval. These comparisons connect the graph’s strength
attribute to observed associations and document the resulting cov-
erage.
D Signs, Baselines, and Monthly Stability
Table 6 gives monthly effects for the three-hour LFWO robustness
comparison. Each cell is an equal-cluster mean within the stated
month. Seven of eight monthly effects are positive for both statistics
and both strength subsets. The reported overall estimates average
these monthly means equally.
The all-positive comparison preserves endpoints, windows, and
observation masks while assigning every edge sign+1. The absolute
score takes the absolute value of each window/triple correlation
before aggregation. Table 7 applies both comparisons to three-hour
LFWO. They distinguish alignment with the graph’s proposed sign
from the magnitude of association among its selected endpoints.
E Change Horizons and Evaluation Windows
Figure 5 evaluates one-bin Pearson, one-bin Spearman, and three-
bin Pearson changes at 3-, 12-, and 24-hour sampling intervals. Each
specification uses its own eligible relation pairs. Available period
means the full calendar month for Full month and the remaining
month for LFWO. The 7- and 14-day rows use windows of those
lengths, advancing by seven days and averaging valid window
correlations. Three-bin changes extend the change horizon to 9, 36,
and 72 hours, respectively.
A common-cohort check uses pairs eligible at all three inter-
vals within each measurement regime and metric. With 289 edge-
months, full-month three-bin Pearson advantages at 3, 12, and 24
hours are0.057,0.090, and0 .111. With 298 edge-months, LFWO
one-bin Spearman advantages are0.072,0.019, and0.019. The three-
hour rank-association advantage persists with edge membership
fixed. Masks and change horizons follow their interval-specific
definitions.
9

WWW ’27, May 2027, Dublin, Ireland Capponi et al.
−0.05
0.00
0.05
0.10
0.15
Pearson: Full month
 Pearson: LFWO
3 12 24
Sampling interval / change horizon (hours)
−0.05
0.00
0.05
0.10
0.15
Spearman: Full month
3 12 24
Sampling interval / change horizon (hours)
Spearman: LFWO
Signed correlation advantage
All strengths Medium/high
Figure 4: Pearson and Spearman robustness against matched controls, for all strengths and medium/high relations. Columns
use Full month and LFWO; rows use Pearson and Spearman. Bars show pointwise 90% month-level 𝑡-intervals. Table 5 gives the
corresponding𝑝-values and high-only results.
Table 6: Monthly three-hour LFWO effects against matched controls. MH denotes medium/high strength. 𝑁 counts eligible
edge-months, shared by the two statistics within each strength subset.
Pearson advantage Spearman advantage Edge-months
Month All MH All MH𝑁 All 𝑁MH
Feb +0.038 +0.065 +0.031 +0.038 90 67
Mar +0.133 +0.120 +0.157 +0.132 74 66
Apr +0.085 +0.076 +0.080 +0.074 54 51
May +0.042 +0.074 +0.012 +0.026 11 9
Jun +0.109 +0.192 +0.114 +0.111 14 8
Jul -0.005 -0.034 -0.029 -0.030 23 9
Aug +0.093 +0.100 +0.116 +0.142 16 8
Sep +0.073 +0.262 +0.101 +0.311 19 5
Table 7: Three-hour LFWO polarity and magnitude on the
same eligible comparisons. All𝑝-values are two-sided month-
level𝑡-test values. ∗𝑝<0.10, ∗∗𝑝<0.05, ∗∗∗𝑝<0.01.
Statistic Score Relation ControlΔ𝑝
Pearson Graph signs 0.045 -0.026 +0.0710.0027 ∗∗∗
Pearson All positive 0.043 -0.016 +0.0590.0193 ∗∗
Pearson Absolute 0.193 0.185 +0.0090.5885
Spearman Graph signs 0.042 -0.031 +0.0730.0131 ∗∗
Spearman All positive 0.052 -0.026 +0.0780.0114 ∗∗
Spearman Absolute 0.182 0.177 +0.0050.7194
Removing any one month leaves the three-hour LFWO Pearson
advantage between+0.062and+0.082, and the Spearman advan-
tage between+0.061and+0.087. Both pooled advantages remain
positive under every single-month omission. Together, the monthly
table, common-cohort comparison, and omission checks character-
ize the temporal stability of the graph’s behavioral associations.
F Month-Level Inference
The primary test uses the dispersion of the eight monthly effects and
a Student𝑡 reference with seven degrees of freedom. Exact month
sign flips provide a complementary check: all effects in a month
change sign together, preserving dependence within that month.
Under independent, symmetric monthly effects, all2 8 = 256sign
patterns form the null reference. Two-sided values are0.0156for
three-hour LFWO Pearson,0.0078for full-month 12-hour Pearson,
0.0078for daily LFWO Pearson, and0 .0234for three-hour LFWO
Spearman.
10

WWW ’27, May 2027, Dublin, Ireland
Available period
14 days
7 days
Full month
+0.03 +0.04 +0.04
+0.02 +0.00 +0.01
+0.00 -0.01
One-bin Pearson
+0.03 +0.02 +0.02
+0.03 -0.00 -0.02
+0.03 -0.02
One-bin Spearman
+0.05 +0.07 +0.08
+0.04 +0.03 +0.04
+0.05 +0.04
Three-bin Pearson
3 12 24
Sampling interval (hours)
Available period
14 days
7 days
LFWO
+0.07 +0.02 +0.03
+0.04 +0.02 +0.05
+0.01 +0.02
3 12 24
Sampling interval (hours)
+0.07 +0.01 +0.02
+0.04 +0.02 +0.02
+0.03 +0.00
3 12 24
Sampling interval (hours)
+0.06 +0.08 +0.06
+0.04 +0.05 +0.08
+0.04 +0.08
−0.10
−0.05
0.00
0.05
0.10
Advantage
Figure 5: Price-change sensitivities against matched controls at 3-, 12-, and 24-hour sampling intervals. Available period uses
the complete calendar month in the Full month panels and the remaining month in the LFWO panels. The 7- and 14-day
windows advance weekly. The color scale is shared across all panels.
A sensitivity to dependence between adjacent months averages
February–March, April–May, June–July, and August–September,
using a𝑡 reference with three degrees of freedom. Two-sided values
are0.0029for three-hour LFWO Pearson,0 .0437for full-month 12-
hour Pearson, and0.0356for daily LFWO Pearson. This sensitivity
assumes approximately independent, Gaussian block means. Exact
four-block sign flips have a minimum two-sided value of0.125.
The retrospective evaluation comprises 1,344 combinations of
source, statistic, period, controls, and score. Across this search, ev-
ery eight-month setting has a Holm-adjusted value above0.05[ 10].
Displayed𝑝-values characterize individual settings. The reported
settings and inference methods are data-informed, and the compar-
isons are exploratory.
11
