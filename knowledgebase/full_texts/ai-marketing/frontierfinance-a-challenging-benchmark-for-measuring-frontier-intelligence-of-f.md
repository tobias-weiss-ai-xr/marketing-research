---
title: 'FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents'
url: https://arxiv.org/abs/2608.11683
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Yuhao Zhang
- O. Ozan Koyluoglu
- Thejas Venkatesh
- Richard Diehl Martinez
- Vishank Bhatia
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.11683
pages: 35
chars: 93384
fetched_at: '2026-11-08T13:34:57+00:00'
kb_version: 1
---

# FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents

FrontierFinance: A Challenging Benchmark for
Measuring Frontier Intelligence of Finance Agents
Yuhao Zhang, O. Ozan Koyluoglu, Thejas Venkatesh, Richard Diehl Martinez, Vishank Bhatia,
Arash Alidoust, Ashwin Paranjape
Samaya AI
AI agents are increasingly deployed for professional investment research, yet no benchmark
capturesthecomplexityofthefullinvestorworkflow. Existingbenchmarksmainlytargetfinancial
data extraction—a narrow slice that current models have largely saturated—while reference-based
metrics and generic LLM-as-a-judge scoring fall short on the open-ended, long-form answers
that real analyst queries demand. We introduce FrontierFinance, a fully open benchmark of 220
expert-crafted queries and 11,543 source-attributed rubrics spanning six crucial use cases across
the full investor workflow. FrontierFinance is both broader and harder than existing public finance
benchmarks. Evaluating frontier models and agent systems under a common harness restricted to
publicly available data, we find that the tool harness, not the model alone, strongly shapes quality
andefficiency;thatSamaya’sin-housesystemleadsat56.0%,aheadofthestrongestfrontiermodel
(Claude Fable 5, 49.2%) at roughly 2.2×lower cost; and that the best open-weight model (Kimi
K3, 46.4%) nearly matches the best proprietary model at 4.5×lower cost.Screening & Discovery
andSector, Industry & Macroremain the hardest use cases across all systems, where even the best
systems reach only 33% and 39%. We make the dataset and grading code publicly available.
Date:August 13, 2026Correspondence:research@samaya.ai
Website:https://research.samaya.ai/benchmarks/frontier-finance
1 Introduction
Large language models are becoming increasingly capable at agentic tasks: they create multi-step
plans, call external tools, retrieve evidence from large corpora, and produce long-form outputs
combining structured and unstructured content. Finance is among the most demanding settings for
suchsystems. Professionalinvestmentresearchisopen-endedandchallenging: itspansideascreening
anddiscovery,companyandmarketresearch,financialdataextraction,portfoliotracking,andcatalyst
monitoring. Answering a real-world financial query often requires retrieving and synthesizing
qualitative and quantitative evidence from many sources, performing causal analysis, and drafting a
comprehensive report that meets a strict standard of factual accuracy.
Existing benchmarks capture only a fraction of this work (Table 1). Most public finance evaluation
suites focus primarily on financial data extraction, e.g., retrieving a reported figure from a filing
or computing a ratio from a table [1, 2, 3, 4]. These tasks are well-defined but narrow, and recent
models have largely saturated them. Performance on these static benchmarks is further confounded
by data memorization, where models rely on memorized training data rather than true reasoning.
Meanwhile, benchmarks probing complex, open-ended financial research remain scarce. The field
therefore lacks a shared and sufficiently difficult benchmark for real-world finance agent evaluation.
To fill this gap, we introduce FrontierFinance, a publicly released benchmark for evaluating finance
agents on professional investment research. It consists of 220 queries and 11,543 rubrics authored
throughafour-stagecurationandauditpipelinebyfinancedomainexperts—includingformerbuy-side
A Samaya AI technical report1
arXiv:2608.11683v1  [cs.AI]  12 Aug 2026

analysts, sell-side research associates, and investment banking professionals—organized into six use
cases spanning the investor workflow (Section 3.1). Each rubric is a binary criterion attributed to a
publicly available data source, enabling objective, reproducible scoring via a rubric qualification
rate—the majority verdict of three independent LLM judges (Section 5). Compared to existing
benchmarks, FrontierFinance is more diverse in use case coverage and significantly harder, and to our
knowledge is the largest of its kind (Section 4.2).
We benchmark frontier models and agent systems under a common harness restricted to publicly
available data, measuring quality, cost, and latency (Section 6). We find that the harness system, not
the underlying model alone, strongly shapes both quality and efficiency. Samaya’s in-house system
leads at 56%, ahead of the strongest frontier model deployed under an open-source harness (Claude
Fable 5, 49.2%) at roughly 2.2× lower cost. The best open-weight model (Kimi K3, 46.4%) nearly
matches frontier performance at 4.5×lower cost. Across all tested systems, we find two use cases,
both open-ended in nature, prove hardest and remain largely unsolved:Screening & Discoveryand
Sector, Industry & Macro, where the best systems reach only 33% and 39%.
Beyond aggregate scores, we analyze agent trajectories to understand how systems differ in behavior
(Section 7). Our analysis reveals that tool use follows a common three-phase structure across all
systems: data gathering, mid-rollout synthesis and analysis, and answer preparation. Despite very
different tool-call volumes, top systems tend to display more efficient tool use and converge on
similar token budgets. We also uncover failure patterns that may inspire future research: models that
navigate directly to known financial sources from parametric knowledge—rather than discovering
them through search—incur significantly higher URL error rates, causing token waste and context
pollution.
To summarize, our contributions are as follows:
• We release FrontierFinance, an open benchmark of 220 expert-crafted queries and 11,543
source-attributed rubrics spanning six use cases across the full investor workflow, the largest
open finance agent benchmark of its kind.
• We characterize the benchmark’s coverage and difficulty through detailed analysis, showing
it is both broader and significantly harder than existing public finance benchmarks.
• We systematically evaluate frontier models and agent systems along the quality, cost, and
latency dimensions, and report findings on the role of the tool harness, the quality–cost
frontier, and the competitiveness of open-weight models.
•Through agent trajectory analysis, we identify common behavior patterns as well as pitfalls
that point to opportunities for improving future models.
2 Related Work
Early financial QA benchmarks.Financial benchmarks have evolved from document-grounded
question answering toward open-ended, agentic research tasks. Early datasets primarily evaluate
numerical reasoning over bounded financial documents: FinQA represents solutions as executable
programs, TAT-QA combines tabular and textual evidence, and ConvFinQA extends numerical
reasoning to multi-turn conversations [2, 3, 4]. FinanceBench evaluates question answering over
public-company filings, while DocFinQA and FinanceReasoning introduce longer contexts and
more challenging numerical derivations [1, 5, 6]. Broader suites such as FinBen aggregate multiple
financial-language tasks into a common evaluation [7]. These benchmarks provide controlled tests
of component capabilities, but most supply a bounded evidence set and expect a compact answer,
2

Table 1. Comparison of representative finance-agent benchmarks.Rows are grouped by their primary
evaluation target. The first five columns indicate whether each benchmark centrally evaluates:open-domain
discovery, in which the agent must locate evidence from open search rather than receive a fixed document
corpus;long-form output, in which the principal deliverable is a structured research report;workflow breadth,
meaning coverage of multiple stages of the professional investor workflow rather than a single task family;
expert criteria, meaning task-specific grading requirements authored by finance-domain experts; andsource
labels, meaning criterion-level annotation of the expected evidence category. The final column reports the
number of publicly released examples.
Benchmark Primary emphasis Open domain Long- form Workflow breadth Expert criteria Source labels Public examples
Document-grounded question answering
FinanceBench[2023] Filing-grounded financial QA ◦ ◦ ◦ ◦ ◦150
Agentic retrieval and derivation
Finance Agent
Benchmark[2025]
SEC filings and web
research • •◦•◦27
BigFinanceBench[2026] Auditable financial derivations •◦ ◦•◦50
Hedge-Bench[2026] Expert steps in a fixed corpus ◦ ◦ ◦•◦102
Open-ended research reports
FinResearchBench
II[2026]
Rubric-scored research
reports • •◦ ◦ ◦0
FrontierFinance Full investor research workflow • • • • • 220
numerical value, or derivation. Consequently, none measures whether an agent can discover relevant
evidence, scope the research, and synthesize a comprehensive response to an open-ended analyst
request.
Agenticfinancebenchmarks.Morerecentbenchmarksexplicitlyevaluatefinancialagentsequipped
with search and specialized tools. The Finance Agent Benchmark contains expert-authored research
problems requiring agents to use recent filings and web evidence, while FinSearchComp evaluates
time-sensitive retrieval, historical lookup, and complex open-domain financial investigation [8,12].
FinAgentBenchandFin-RATEfocusonagenticretrievalandlongitudinalorcross-companyreasoning
over regulatory filings [13, 14]. Other benchmarks broaden the domain beyond filing research:
FinGAIA evaluates multi-tool financial agents, FORCE-Bench targets operational and enterprise-
finance workflows, Herculean covers various financial-intelligence tasks, and FinanceComplexQA
evaluates complex reasoning over industrial financial documents [15, 16, 17, 18]. Together, these
works extend evaluation to include retrieval systems, tools, and agent orchestration.
Evaluating open-ended research answers.Evaluating open-ended, long-form research answers
challenges standard methodology. Open-ended analyst requests admit multiple valid choices of
evidence,organization,peerset,andanalyticalpath,makingexactmatchandlexicalreferencemetrics
insufficient [19]. Holistic LLM judges offer greater flexibility and can align with human preferences,
but their scores may be sensitive to the judge model, prompt, presentation order, response style, and
verbosity,whilerevealinglittleaboutwhatasystemactuallymissed[ 20,21]. Fine-grainedevaluation
avoids these pitfalls by decomposing quality into independently assessable requirements. Such
3

checklist-based methods improve interpretability and inter-judge reliability, and recent long-form
research benchmarks increasingly employ task-specific criteria rather than a single overall rating
[22, 23, 24, 25]. In earlier work, we proposed Criteria-Eval [26], a checklist-based framework in
which finance experts author binary criteria and score systems by the fraction satisfied—an approach
that jointly handles retrieval and generation, admits multiple valid answers, and aligns scoring with
expert judgment.
Open-ended financial research benchmarks.The closest precedents to our setting evaluate
open-endedfinancialresearchorprofessionalworkproducts. BigFinanceBenchdecomposesfinancial
research into point-weighted, independently checkable derivation steps, while FinResearchBench
evaluatesreportsthroughanintermediatelogictreeandFinResearchBenchIIconstructsquery-specific
rubrics from model-generated reports [9, 27, 11]. FinDeepResearch evaluates standardized company-
analysisreportsacrossmarketsandlanguages,DeepFinResearchBenchcomparesgeneratedresearch
with professional analyst reports, and Hedge-Bench scores verified expert reasoning steps within
controlled evidence environments [28,29,10]. Complementary artifact-oriented benchmarks focus
on constructing financial spreadsheets and models rather than research reports [30, 31].
3 Data Collection and Statistics
3.1 Data collection
WebuildFrontierFinancethroughafour-stagecurationandauditpipelineexecutedentirelybyfinance
experts—including former buy-side equity analysts, sell-side research associates, and investment
banking professionals. Figure 1 illustrates this pipeline. We include examples of the resulting
annotations in Appendix A.
EXPERT AI EXPERT + AI
01 EXPERT

Financial query authoring
Finance experts draft realistic,
challenging queries, guided by
real-world financial workflows.

0 2 EXPERT

Expert rubric annotation
Finance experts author grading
rubrics; supervisors verify the
result and remove annotations
not passing quality bar.

0 3 EXPERT + AI

Agent-guided cleanup
Finance experts guide AI agents
to clean up grading rubrics and
remove subjectivity in the
wording.

04 EXPERT + AI

Taxonomy-based
rebalancing
Final dataset derived by
rebalancing across use cases,
capabilities, and difficulty levels.
Figure 1.The four-stage data collection process used to construct FrontierFinance, spanning query drafting,
dense rubric authoring, multi-expert auditing, and dataset rebalancing.
Stage 1: Workflow mapping and query drafting.Domain experts first mapped the end-to-end
investment workflow, identified six use cases (Figure 2), and simulated investment decision-making
to craft open-ended queries reflecting real analyst tasks. To test agent robustness, queries deliberately
preserve real-world ambiguity: using company names and ticker symbols interchangeably without
explicit mapping, specifying multi-quarter or dynamic timeframes that require resolving historical
date bounds against filing dates, and framing tasks requiring unbounded retrieval across market caps
and peer groups rather than closed context windows.
Stage 2: Rubric authoring and source attribution.For each query, experts constructed binary
evaluation rubrics that decompose open-ended research deliverables into independently checkable
criteria. Each rubric is annotated withsource attribution, tying it to a primary public data source tier
4

Figure 2.FrontierFinance focuses on 6 use cases that span the entire investment decision-making workflow.
such as SEC filings, call transcripts, or market data (Section 4.1). Queries average 52.5 rubrics each,
enabling thorough grading of long-form answers.
Stage 3: Expert review and multi-stage auditing.Under the help of AI agents, a first panel of
experts reviews drafted queries and rubric sets to eliminate subjective phrasing, repeated information,
and language that requires a single source when multiple are possible. A secondary panel verifies
that every criterion can be objectively evaluated as fulfilled (1) or unfulfilled (0) against public
evidence, consolidates redundant rubrics to prevent over-weighting repeated facts, and confirms
that all attributed evidence is accessible via public web or regulatory channels without proprietary
paywalls. We also tag each rubric along two dimensions:essentiality(mandatorymust-havevs.
supplementary) andrubric category(an eight-category functional taxonomy; Section 3.2).
Stage 4: Rebalancing and dataset stratification.Steps 1 through 3 yielded over4,500 fully
annotated research queries. From this pool, we assembled the 220 released queries (11,543 total
rubrics) comprising FrontierFinance via stratified sampling, reserving the remaining∼4,300 queries
for internal development and future releases. The public set is balanced across three axes:use cases
(ensuring sufficient coverage across all six),capabilities(stratifying across reasoning and search
modalities like temporal filtering and cross-entity triangulation), anddifficulty(calibrating across
Bradley–Terry difficulty terciles; Section 4.2).
Timestamped annotation.One design decision runs through every stage of this pipeline: how
we handle time. Time is central to finance, shaping both how a query should be interpreted (a
request for the “latest quarter” resolves to different periods depending on when it is asked) and what
constitutes a good answer (prices, filings, and consensus estimates change continuously). Handling
this time-variant nature of real-world questions is a long-standing challenge, and existing benchmarks
address it in one of three ways: restricting to time-invariant queries [32,33], which sharply limits
querydiversityandisespeciallyrestrictiveforfinancetasks;freezingthedatasourcetoapoint-in-time
corpus [34, 35], which is much smaller and less diverse than the open web and often does not reflect
how an agent is deployed in practice; or annotating timestamped queries and rubrics [8], where each
query carries a date and the agent answers as if at that date.
We follow this third approach: every FrontierFinance query carries a date field, and its rubrics reflect
5

This benchmark Comparison benchmarks (public set)
FrontierFinance n=220 FinanceBench n=150
BigFinanceBench n=50
Finance Agent Benchmark v2 n=27
Financial Data Extraction Company Research Earnings & Events Sector, Industry & Macro
Coverage & Catalyst Screening & Discovery Other
Figure 3.Use-case coverage of FrontierFinance versus public finance benchmarks. Each dot is one query,
colored by its use case (grey = outside the six use cases). FrontierFinance spreads its 220 queries across all six
use cases, whereas existing benchmarks concentrate almost entirely in financial-data extraction.
the state of the world up to that date. We further exclude predictive queries (for example, forecasting
the outcome of a future event), which keeps the benchmark robust to the exact web snapshot an agent
sees even when data postdating the query date is accessible.
3.2 Use cases, capabilities, and rubric categories
ExamplesinFrontierFinancearefurthertaggedalongthreecomplementaryaxes: eachquerycarriesa
singleusecaseandoneormorecapabilities,andeachrubricisassignedarubriccategory. Together
they characterize what the benchmark asks of an agent and what a correct answer must contain.
Use cases.Each query is labelled with exactly one of six use cases spanning the investor workflow
(Figure 2; full counts and descriptions in Appendix B, Table 6). Financial data extraction is the most
common (32% of queries), but no use case dominates, and the open-ended use cases—screening
and discovery, and sector, industry, and macro—are well represented. In comparison, existing
finance benchmarks concentrate almost entirely on financial-data-extraction queries, leaving harder,
open-ended use cases largely untested (Figure 3).
Capabilities.Each query is also tagged with the reasoning and retrieval capabilities it requires.
Queriesaverage1.9capabilitieseach(410tagsover220queries),reflectingthatrealistictaskscombine
skills. Qualitative synthesis and the three modes of exhaustive retrieval (temporal, cross-entity, and
thematic; 147 queries combined) are the most common (see Appendix B, Table 7 for full counts and
definitions).
Rubric categories.Each of the 11,543 rubrics is classified by content type using an eight-category
taxonomy (Table 8, in Appendix B). Factual data extraction is the plurality (74%), consistent with
rubrics being written as objective, checkable criteria; the remaining quarter covers qualitative,
forward-looking, analytical, and comparative content.
4 Data Analysis
We analyze the collected queries and rubrics in depth to characterize their data-source demands and
difficulty relative to existing benchmarks.
6

Financial data and modeling 59 21 15
Sector, industry and macro 25 15 32 13
Screening and discovery 19 29 12
Earnings and events 68 16
Coverage and catalyst monitoring 19 57 13
Company research 34 31 16
All use cases 39 25 19
SEC filing Company originated content Professional knowledge Market data
News and media sources Regulatory and legal data Others
Figure 4.Rubric-level data source distribution per use case. Each bar shows how a use case’s rubrics break
down across data sources (row-normalized to 100%); the bottom bar is all use cases combined. SEC filings are
the plurality overall (39%) yet under 40% of rubrics, and the distribution shifts sharply by use case—from
filings-driven financial data extraction to company-issued content for earnings and market/professional sources
for screening. Full distribution data shown in Appendix B, Table 9.
4.1 Data sources distribution
Weassignadatasourcetoeachrubricusingataxonomyof10top-levelsourcecategories. Attributing
evidence at the rubric level, rather than the query level, lets us characterize the evidence demands of
individual queries, use cases, or the benchmark as a whole. The resulting distribution (Appendix B)
shows that no single document type dominates.
FrontierFinance covers diverse data sources demanded by professional finance work.SEC
filings are the single largest source category, yet they account for under 40% of all rubrics. The
remainder spans company-issued material (earnings-call transcripts, investor presentations, earnings
releases, annual reports), the analyst’s own professional knowledge (valuation work, model estimates,
domain synthesis), live market data, news and media, and regulatory filings.
The source mix shifts substantially across use cases(Figure 4), mirroring how an analyst’s
evidence needs change across the workflow. Financial data extraction is overwhelmingly filings-
driven (59% SEC); earnings & events leans on company-issued content (68%, transcripts and
releases); sector/industry & macro is carried by professional knowledge (32%) and market data
(13%); and screening & discovery is the most source-diverse use case, pulling from market data
(29%), professional knowledge (20%), regulatory data (10%), and news (12%) rather than any single
dominant source.
4.2 Difficulty analysis
We definedifficultyas the data-gathering and reasoning effort a financial analyst would need to
produce a complete, defensible answer. To place every query on a single scale, we use pairwise
judgmentsaggregatedviaaBradley–Terry(BT)model—awell-establishedapproachusedbyChatbot
Arena to rank models [21,36] and underlying alignment methods such as DPO [37]. Unlike those
model-ranking uses, here we rank queries by difficulty. We score each pair using a consensus of
three independent LLM judges reasoning over five axes:retrieval breadth,reasoning depth,entity
scope,time scope, andqualitative ambiguity. From∼77K pairwise judgments across 4K internal
queries, we fit a confidence-weighted BT model [38] (Appendix C), yielding one latent difficulty
score per query.
7

Table 2.Difficulty terciles of the FrontierFinance public set (220 queries), by consensus Bradley-Terry (BT)
score (higher means more difficult). On all FrontierFinance queries, we see a mean score of 4.84 and standard
deviationof7.16. Thebucketcutoffsareeasy/mediumat BT=+0.94 andmedium/hardat BT=+7.25 . Inthe
last column, we also include Samaya system’s performance for queries in each difficulty bucket as a reference
(using must-have qualification rate as defined in experiments).
Bucket Queries Share BT median BT std Agent performance
Hard 73 33.2%+12.963.62 0.37
Medium 74 33.6%+3.731.85 0.63
Easy 73 33.2%−1.033.23 0.80
Table 3.Example queries and rubric statistics for each difficulty bucket in FrontierFinance. Note that some
queries shown have been significantly simplified to fit into the space.
Bucket BT Rubrics Query (simplified) Main difficulty driver
Easy−9.97 “What is the total employee count for US Steel
Corporation?”
Single fact, one entity, one filing
Easy−5.737 “What EPS guidance did Delta provide in its
latest earnings call?”
Many rubrics, but all from one earn-
ings call
Medium+3.721 “Which publicly traded US firms have exposure
to robotics?”
Unbounded entity scope, but shallow
per entity
Medium+5.419 “What have NEE, DUK, SO, and D said about
load-growth expectations in the last year?”
Multi-entity, multi-quarter transcript
synthesis
Hard+15.921 “IdentifyNike’snewlyannouncedFY2025part-
ner;thentriangulatethatpartner’srevenueexpo-
sureacrossNike’s,thepartner’s,andAdidas/UA
filings.”
Multi-hop conditional reasoning,
cross-entity
Hard+22.0300 “Screen $10B+ biotechs with 2025 Phase-3
readouts,rankbyanalystprice-targetdispersion,
thendecomposetheleader’srealizedvs.implied
volatility and 13F flows.”
Unbounded screening + multi-source
retrieval + computation
Wesplitthe220FrontierFinancequeriesintoeasy/medium/hardtercilesbyBTscore,withcutoffs
at BT=+0.94 and+7.25; Table 2 shows the three buckets are well separated. Note that difficulty
is not simply a function of rubric count—the two correlate only moderately (Spearman𝜌=0.71 ).
The examples in Table 3 illustrate that the key driver is the type of work required: easy queries
resolve inside a single document even when the rubric is long (37 rubrics, all from one earnings
call), whereas hard queries require cross-entity resolution, unbounded search, multi-hop reasoning,
or causal analysis.
Correlation with agent performance and human effort.Table 2 also reports the performance of
Samaya’s agent system (defined in Section 5) averaged across each difficulty bucket. The BT score
inversely correlates with system performance: qualification rate declines monotonically across easy,
medium, and hard (0.80→0.63→0.37 ; Spearman𝜌=−0.47 ). The BT score also correlates with
human effort: using expert solve times from the 27 Finance Agent Benchmark v2 queries [8], the
median time rises20→40→45→60 minutes across BT score quartiles (Spearman𝜌=0.67 ),
confirming the score tracks genuine task difficulty.
Comparison to existing finance benchmarks.We compare FrontierFinance against the three
most similar public finance benchmarks—FinanceBench [1], BigFinanceBench [9], and Finance
8

-8 -6 -4 -2 0 2 4 6 8 10 12 14
Difficulty Score (higher = harder)
FinanceBench
(n=150)
BigFinanceBench
(public set, n=50)
Finance Agent Benchmark v2
(public set, n=27)
FrontierFinance
(n=220)
3.7
IQR (25–75%)
Median
Mean
10–90%
Figure 5.Bradley–Terry difficulty distribution per benchmark on the shared consensus scale. The IQR box
represents interquartile range. The background color bands mark FrontierFinance’s easy/medium/hard buckets
(cutoffs+0.94 /+7.25). FrontierFinance has the highest median and mean and by far the widest spread,
reaching well into the hard band, while the three compared benchmarks sit mostly in the easy/medium range.
Agent Benchmark v2 [8]—positioning all queries onto the same BT scale via anchor pairings
(Appendix C). Figure 5 shows FrontierFinance is substantially harder and spans a wider range, with
thehighestmedianandwidestspread;thethreecomparedbenchmarksclusterintheeasyandmedium
ranges. Only 0–2% of Finance Agent v2 and BigFinanceBench queries fall in the hard category,
and FinanceBench—designed as single-fact 10-K lookups—is entirely easy. This gap reflects task
design: FrontierFinance targets multi-source synthesis tasks rather than single-document lookups.
Full statistics are in Appendix C (Tables 13 and 14).
5 Experiment Setup
FrontieragenticAIsystemshavetwoessentialparts: theLLMbackbone,whichdecideswhattoolcalls
to make and what responses to generate, and the agent harness—the surrounding software (prompts,
tools, execution environments, and the orchestration loop) through which the LLM perceives and acts
on its environment.
With FrontierFinance, we benchmark frontier models and systems using three distinct types of
harnesses:
• Web search harness: a minimal harness pairing each model with its built-in web search
tool, providing a baseline for web-search-only performance.
• Finance Agent v2 harness: an open-source harness connecting the model to six specialized
tools: the SEC EDGAR API, a market price data API, web search, HTML parsing, long-
HTML search, and a calculator [8]. Included as a reproducible agent harness created
specifically for finance tasks.
• In-house Samaya agent harness: a production-grade harness combining Samaya’s custom
models, tools, data index, and retrieval engines, optimized for both quality and efficiency.
Included to benchmark how a highly optimized finance harness performs.
Implementation Details.For the web search harness, we evaluated Claude Opus 4.8, GPT 5.5, and
Gemini 3.1 Pro paired with their built-in web search APIs, with reasoning effort at each model’s API
default.
FortheFinanceAgentv2harness,weadapteditsoriginalimplementation 1andmadetwochanges. First,
1https://github.com/vals-ai/finance-agent-v2
9

we re-implemented the agent orchestration with the LangChain library for maximum compatibility
with existing models and frameworks. Second, we introduced tool call limits of 200 tool calls and
300 seconds, ensuring evaluation under a realistic finite budget. These limits are included in the
system prompt; when either is hit, the model is prompted to provide a final response. We applied the
same limits to the in-house Samaya agent harness for fair comparison. We include the system and
user prompts in Appendix E.
For all model calls, we set the temperature to 1.0 wherever required. We enable thinking or reasoning
mode and leave the reasoning effort at each model’s API default, as listed in Table 4. We leave all
other decoding parameters, such as top𝑘 or top𝑝, to their API defaults. We include additional API
endpoint information in Appendix D.
Query Date Handling.For all tested systems, we provide both the query and its associated query
date as input, and prompt the system to anchor its research on that date. For Samaya’s in-house
harness, we additionally apply the query date as a retrieval cut-off for any data indexed in-house.
5.1 Evaluation Metrics
We evaluate systems along three dimensions: answer quality, cost, and latency.
Answer Quality. We measure answer quality using theRubric Qualification Rate. Let𝑁 represent
the total number of queries in FrontierFinance. Each query𝑞𝑖 has a set of expert-authored binary
rubrics 𝑅𝑖 ={𝑟 𝑖,1,...,𝑟 𝑖,𝑀 𝑖}, with𝑀𝑖 =|𝑅 𝑖|. Given a system’s answer𝑎𝑖 to query𝑞𝑖, a group of
LLM judges evaluates each rubric independently and returns a binary verdict
𝑠(𝑟𝑖,𝑗,𝑎𝑖)∈{0,1},(1)
where1indicates that𝑎 𝑖 satisfies𝑟𝑖,𝑗 and0otherwise.
We define per-query qualification rate as the fraction of that query’s rubrics satisfied by the answer:
𝑄𝑖 = 1 𝑀𝑖 𝑀𝑖∑︁ 𝑗=1 𝑠(𝑟𝑖,𝑗,𝑎𝑖)∈[0,1].(2)
At dataset level, we then calculateMacro-averaged Rubric Qualification Rateas the mean of the
per-query rates over all queries and use it to represent a system’s performance:
R= 1 𝑁 𝑁∑︁ 𝑖=1 𝑄𝑖 = 1 𝑁 𝑁∑︁ 𝑖=1 1 𝑀𝑖 𝑀𝑖∑︁ 𝑗=1 𝑠(𝑟𝑖,𝑗,𝑎𝑖).(3)
We report two variants:𝑅all over all rubrics and𝑅must-haveover the must-have subset. We usemacro
overmicroaveraging so that the metric rewards consistent performance across all queries, rather than
excelling on a few high-rubric-count queries at the expense of others.
We score each rubric by majority vote across three independent LLM judges: GPT 5.4, Gemini 3.1
Pro, and Claude Sonnet 4.6. We chose this ensemble to avoid single-provider bias and because their
majority votes closely matched a larger committee of nine judges in preliminary experiments. The
judgepromptincludesfinance-specificinstructions. WeincludetheLLMjudgepromptinAppendixF
and open-source our grading pipeline for reproducibility.
Latency. We measure per-query latency as wall-clock time from query receipt to full answer,
averaged over all queries.
10

Table 4.System performance on FrontierFinance, grouped by harness and ranked by rubric qualification rate
within each group.𝑅all represents macro-averaged qualification rate over all rubrics and𝑅must-haverepresents
qualification rate over the must-have subset of rubrics.Reasoning effortis the API default for the underlying
model. Overall best results are highlighted with boldface, and best results within each harness category are
underlined. Average cost for Gemini 3.1 Pro under Web Search Harness is not shown because we were not able
to obtain a fair estimate of the LLM cost from their search-grounded API.
System Reasoning effort𝑅 all (%)𝑅 must-have(%) Avg. latency (s) Avg. cost ($)
Web Search Harness
Claude Opus 4.8 high 33.0 40.6 53.9 1.47
Gemini 3.1 Pro high 30.7 39.4 91.1 –
GPT 5.5 medium 20.7 26.5 192.1 0.55
Finance Agent v2 Harness
Claude Fable 5 high 49.2 57.6 164.5 4.06
GPT 5.6 Sol medium 46.8 57.2 170.7 3.03
Kimi K3 max 46.4 56.4 336.0 0.90
Gemini 3.6 Flash medium 46.3 54.2 163.6 2.41
Claude Opus 4.8 high 45.0 53.7 155.8 2.61
GPT 5.5 medium 43.5 53.2 233.0 2.80
GLM 5.2 max 42.8 50.1 296.5 0.63
DeepSeek V4 Pro high 40.5 50.1 202.6 0.68
Gemini 3.1 Pro high 30.5 39.7 221.9 1.72
Samaya In-house Harness
Samaya (high effort) –56.0 61.7277.8 1.81
Samaya – 52.9 58.5 218.1 0.93
Cost. We measure per-query cost as the API cost of the agentic LLM, excluding external APIs,
storage, and data-index pricing for which precise estimates are hard to obtain. We account for cached
and non-cached input tokens at their respective rates, crediting models that offer lower cached-token
pricing.
6 Results
The harness shapes performance and cost more than the underlying model.Harness type is
the dominant factor in system performance (Table 4). The best system under the Samaya harness
outperforms the best under the Finance Agent v2 harness, which in turn outperforms the best web
search system—and this ordering holds across all six use cases and rubric categories (Figure 7). The
Samaya harness also achieves its advantage at lower cost: Samaya (high effort) leads at 56% while
the best FA-v2 system (Claude Fable 5) reaches 49.2%.
Top proprietary models show non-linear quality–cost scaling but no latency penalty.Among
proprietary models under the Finance Agent v2 harness, Claude Fable 5 leads at 49.2%, followed
closely by GPT 5.6 Sol at 46.8% (Figure 6). Quality and cost do not scale linearly: Fable 5 achieves
a relative 9% gain over Claude Opus 4.8 while incurring 56% more cost, and a further 5% gain
over GPT 5.6 Sol at 34% more cost. Notably, this quality advantage does not come with a latency
11

Figure 6.Model performance under the open-source Finance Agent v2 harness. Left: rubric qualification rate
versus cost per query. Right: rubric qualification rate versus latency per query. In both figures, models toward
the top-left offer a better quality-cost (or quality-latency) tradeoff.
Figure 7.Radar charts showing how system performance varies by use case (left) and rubric categories (right).
For use case we report macro-averaged rubric qualification rate, as main results. For rubric breakdown we
report micro-averaged rubric qualification rate. For readability, we only include best systems under each
harness type.
penalty—both Fable 5 and GPT 5.6 Sol are among the fastest systems under this harness, a pattern
we trace to their more efficient tool use in Section 7.
Open-weight models match proprietary quality at a fraction of the cost, within two months
of release.Kimi K3, the best open-weight model, reaches 46.4%—just 0.4pp behind GPT 5.6
Sol (46.8%) and 2.8pp behind Claude Fable 5 (49.2%)—at $0.90 per query versus $3.03 and $4.06
respectively. Two of the four models on the quality–cost Pareto frontier are open-weight: GLM 5.2
($0.63, 42.8%) and Kimi K3 ($0.90, 46.4%) offer the best quality-per-dollar among all systems, with
no proprietary model matching their efficiency at comparable quality levels. Figure 8 shows the gap
is closing fast: GLM 5.2 nearly matched GPT 5.5 (42.8% vs 43.5%) within 1.8 months of its release,
and Kimi K3 surpassed Claude Opus 4.8 (46.4% vs 45.0%) within 1.6 months, with an average
open-to-proprietary gap of just 4.8 percentage points.
Modelperformancescaleswithreasoningeffort,butwithdiminishingreturns.Thisholdsacross
harnesses and models. Within the Samaya harness, the high-effort variant improves qualification
12

40%
44%
48%
52%
~1.8 months (GPT 5.5 GLM 5.2)
~1.6 months (Claude Opus 4.8 Kimi K3)
May ʼ26 Jun ʼ26 Jul ʼ26 Aug ʼ26
Model Release Date
Rubric Qualification Rate
GPT 5.5
DeepSeek V4 Pro
Claude Opus 4.8
Claude Fable 5
GLM 5.2
GPT 5.6 Sol
Kimi K3 Gemini 3.6 Flash
Avg. gap: 4.8 pp
Proprietary model frontier
Open-weights model frontier
Figure 8.FrontierperformanceonFrontierFinancefromproprietaryversusopen-weightmodelsagainstmodel
release date. All models shown are evaluated under the Finance Agent v2 harness.
$0 $1 $2 $3 $4 $5
Cost per query (USD)
38%
40%
42%
44%
46%
48%Rubric qualification rate
low
medium
high (default)
xhigh
low
medium (default) high xhigh
low
max (default)
high
Claude Opus 4.8
GPT 5.6 SolKimi K3
0.2 0.3 0.4 0.5
Rubric qualification rate
(all rubrics)
0.3
0.4
0.5
0.6
Rubric qualification rate
(must-have rubrics)
r = 0.99
Samaya Harness Finance Agent v2 Harness Web Search Harness
Figure 9.Further analysis of model performance under Finance Agent v2 harness. Left: performance of
GPT 5.6 Sol, Opus 4.8 and Kimi K3 under varying reasoning effort settings. Right: correlation of model
qualification rate for all rubrics and must-have rubrics under different system harnesses.
rate by a relative 6% over the default but at roughly 2× the cost. Among FA-v2 models, Figure 9
(left) shows the same pattern: all three selected models produce higher qualification rates as effort
increases, but returns diminish beyond each model’s default level. GPT 5.6 Sol plateaus atmedium
effort with a slight downward trend at higher settings. Kimi K3 shows an unconventional pattern: at
maxeffort, its qualification rate rises while its cost falls—higher reasoning induces more efficient
tool use, reducing tool calls from 26.7 athighto 19.6 atmax.
Must-have and all-rubric qualification rates are near-perfectly correlated.All rubrics carry
a boolean must-have label indicating whether an answer is significantly incomplete without that
criterion. Figure 9 (right) plots𝑅all against𝑅must-havefor all systems. The two correlate at𝑟=0.99
across all evaluated systems, suggesting that𝑅must-haveis a reliable proxy for overall qualification rate.
7 Model Trajectory Analysis
We analyze model trajectories in depth to understand how behavioral differences drive efficiency
and performance differences. For consistency, we restrict this analysis to systems using the Finance
Agent v2 harness. Our analysis reveals the key findings below.
Modelsvarysharplyinparallelismandtool-callvolume,yettopperformersconvergeonsimilar
13

Table 5.Trajectory statistics for different models under the Finance Agent v2 harness, ordered by qualification
rate. 𝑅all is the macro-averaged qualification rate over all rubrics.Total output,Answer tokens,Tool calls, and
Turnsrepresent per-query mean statistics over all answered queries, where total output tokens include output
tokens for thinking, tool calls and final answers, and each turn could have multiple parallel tool calls.Avg. tool
/ turnis calculated by dividing total tool calls over total turns and then taking macro average, excluding the
closing submit turn.
System𝑅 all (%) Total output Answer tokens Tool calls Turns Avg. tools / turn
Claude Fable 5 49.2 14,119 1,753 16.6 7.5 2.55
GPT 5.6 Sol 46.8 12,545 1,930 46.3 8.9 5.86
Kimi K3 46.4 15,828 1,854 19.6 10.4 2.09
Gemini 3.6 Flash 46.3 24,820 1,946 24.8 25.9 1.00
Claude Opus 4.8 45.0 12,445 1,644 16.1 8.0 2.32
GPT 5.5 43.5 14,406 1,814 33.7 18.6 1.92
GLM 5.2 42.8 22,673 2,580 26.9 13.3 2.19
DeepSeek V4 Pro 40.5 11,464 2,162 41.1 21.3 2.03
Gemini 3.1 Pro 30.5 3,276 859 16.1 15.6 1.10
latency.Table 5 presents overall trajectory statistics for various models. Models differ most sharply
in tools per turn: GPT 5.6 Sol batches most aggressively at 5.86 tools/turn, finishing in just 8.9
turns; Gemini 3.6 Flash is at the opposite extreme, issuing every call sequentially (1.00 tools/turn)
across 25.9 turns—roughly3× longer than its peers. The two best-performing models sit at opposite
ends of total tool-call volume: Claude Fable 5 (49.2%) issues only 16.6 calls per query while GPT
5.6 Sol (46.8%) issues 46.3—nearly3× more—suggesting that tool-call volume alone does not
determine quality. Total output tokens vary considerably (3k–25k), but answer tokens are stable
across top models at 1.6k–1.9k per query; the remainder is thinking and tool invocation tokens, with
thinking tokens likely dominating since invocations are short by nature. Despite these differences
in parallelism and output volume, Fable 5 (164.5s), GPT 5.6 Sol (170.7s), and Gemini 3.6 Flash
(163.6s) post nearly identical latencies—suggesting the two strategies trade off in wall-clock time.
We find no clear correlation between answer token length and qualification rate.
Systems share a similar tool mix, with characteristic model-family differences.Web search
dominates tool usage in nearly every system, followed by page parsing and retrieval; price history
is negligible throughout (Figure 10 left; full split in Appendix G). Within this common shape,
model-family patterns emerge: GPT 5.6 Sol directs 44.8% of calls to web search, the highest of the
four; Gemini systems and GLM 5.2 allocate the most to EDGAR full-text search; and Claude Fable
5’s most-used tool is page parsing.
Tool use follows a common three-phase trajectory.Figure 10 (right) plots tool-call composition
over each system’s rollout, normalized to query length. All four systems open with a data-gathering
phase in which web and EDGAR search account for at least 80% of calls in the first 10% of the
rollout. A research phase follows, with page parsing and corpus retrieval dominating mid-rollout
activity as systems read the sources their searches surfaced. The final phase is answer preparation,
marked by a sharp shift toward the calculator—for Fable 5, 80% of calls in the last 10% of the rollout.
This structure holds irrespective of rollout length and call volume, suggesting the phase boundaries
reflect task structure more than any one model’s policy. Systems differ mainly in how decisively they
transition: Fable 5 shows the sharpest phase separation, while GPT 5.6 Sol continues issuing web
searches well into the final quarter.
14

20%
40%
Web Search
Parse HTML
Page
Retrieve
Information
EDGAR
Search
Calculator
Price
History
Claude Fable 5 GPT 5.6 Sol
Kimi K3 Gemini 3.6 Flash
Web Search Parse HTML Page Retrieve Information
EDGAR Search Calculator Price History
Claude Fable 5 16.8 calls/q · 8.4 turns/q
GPT 5.6 Sol 46.6 calls/q · 9.9 turns/q
Kimi K3 20.7 calls/q · 11.3 turns/q
Gemini 3.6 Flash 24.9 calls/q · 26.9 turns/q
0% 25% 50% 75% 100%
Progress through rollout
Share of tool calls in slice
Figure 10.Tool-use behavior under the Finance Agent v2 harness, for four top-performing models. Left:
share of each system’s tool calls going to each of the six tools. Right: evolution of the tool mix over the rollout,
normalized to each query’s own rollout length.
Sometop-performingmodelsrecallsourcesfromparametricknowledge,sidesteppingdiscovery.
We track the origin of every HTML page a model attempts to crawl and parse, classifying each
link as coming from apast search(its domain appeared previously in the same trace) or from the
model’sparametric knowledge(the domain appears without prior search history). The two Claude
models and Kimi K3 draw on parametric knowledge at substantially higher rates than the rest: 26.7%
of Fable 5’s parses target self-produced domains, roughly half that rate for Kimi K3 and Claude
Opus 4.8, while every other system sits below 5% (Gemini 3.6 Flash produces zero across 1,093
parses; Figure 11 left). These models navigate directly to canonical financial sources—sec.gov,
fred.stlouisfed.org, macrotrends.net—rather than discovering them through search. While
this may appear as a good property of the model, we uncover a particular failure pattern that results
from it: URLs from parametric knowledge incur significantly higher access error rates—due to
hallucinated URLs or pages blocking crawling—than search-discovered URLs (Figure 11 right),
causing token waste and context pollution.
8 Limitations
FrontierFinance anchors each query to a specific date (Section 3.1), which ensures reproducible
evaluation today but introduces a temporal limitation as models advance. As future LLMs are trained
on data postdating the query dates, they may answer from parametric knowledge rather than through
active retrieval and tool use—the very capabilities the benchmark is designed to test. This risk
mirrors the failure pattern we observe in current models (Section 7), but will grow more acute over
time. Periodic re-annotation with newer query dates is one way to mitigate this issue.
Use cases such asScreening & Discoveryare inherently subjective: two analysts might produce
different yet equally valid answers. A system whose answer overlaps with the rubric may outscore
one with an equally correct but differently framed response. We note, however, that this limitation is
mitigated by statistical power: averaged across a large number of uncorrelated query-rubric pairs,
a higher qualification rate still indicates stronger alignment with the analysis process that reflects
financial best practices. The evaluation is therefore fair at scale even where individual queries are
subjective. In this work we spread the annotation budget over more queries; future work could collect
15

From parametric knowledge From past searches
0% 25% 50% 75% 100%
Claude Fable 5 (906) 26.7%
GPT 5.6 Sol (1,726) 2.8%
Kimi K3 (1,121) 14.7%
Gemini 3.6 Flash (1,093) 0.0%
Claude Opus 4.8 (959) 13.9%
GPT 5.5 (1,949) 4.6%
GLM 5.2 (1,692) 3.1%
DeepSeek V4 Pro (1,916) 0.5%
Gemini 3.1 Pro (747) 2.0%
From parametric knowledge From past searches
0% 10% 20% 30% 40%
Claude Fable 5 (242) 18.5 27.7
GPT 5.6 Sol (49) 15.7 38.8
Kimi K3 (165) 25.0 30.3
Claude Opus 4.8 (133) 20.5 33.8
GPT 5.5 (90) 15.2 18.9
GLM 5.2 (53) 14.3 20.8
Figure 11.Origin of the links each system attempts to crawl and parse with theparse_html_page tool and
the distribution of URL parse errors resulting from it. Left: share of URL links coming from parametric
knowledge rather than past search tool calls (total URL attempts in brackets). Right: parse error rate by link
origin, for systems with more than 2.5% of parses from parametric knowledge (parametric-knowledge parse
count in brackets).
multiple rubrics per subjective query to score systems more precisely.
9 Conclusion
WepresentedFrontierFinance,anopenbenchmarkforevaluatingAIagentsonprofessionalinvestment
research. By spanning six use cases across the full investor workflow and scoring long-form answers
against expert-authored, source-attributed rubrics, FrontierFinance measures capabilities that existing
finance benchmarks largely overlook. Our evaluation shows that the benchmark is broad and difficult,
that the tool harness shapes performance as much as the underlying model, and that substantial
headroom remains, particularly on use cases requiring broad screening and macro-oriented research.
We release the dataset and grading code, and we hope FrontierFinance serves as a shared standard for
measuring progress on finance AI agents. As models and systems advance, we plan to expand the
benchmark from our larger internal annotation pool and to report results on new systems over time.
10 Acknowledgement
We thank Christos Baziotis, Jack Hessel, Jack Santos Silva and Mingyi Yang for their contribution to
early data collection process, and Suharsh Sivakumar, Kyle Chang and Bram Mulders for providing
engineering and infrastructure support.
References
[1] Pranab Islam, Anand Kannappan, Douwe Kiela, Rebecca Qian, Nino Scherrer, and Bertie
Vidgen. FinanceBench: A new benchmark for financial question answering, 2023. URL
https://arxiv.org/abs/2311.11944.
[2] ZhiyuChen,WenhuChen,ChareseSmiley,SameenaShah,IanaBorova,DylanLangdon,Reema
Moussa, Matt Beane, Ting-Hao Huang, Bryan Routledge, and William Yang Wang. FinQA: A
16

dataset of numerical reasoning over financial data. InProceedings of the 2021 Conference on
Empirical Methods in Natural Language Processing, pages 3697–3711, Online and Punta Cana,
Dominican Republic, November 2021. Association for Computational Linguistics. doi: 10.
18653/v1/2021.emnlp-main.300. URL https://aclanthology.org/2021.emnlp-main.
300/.
[3] Fengbin Zhu, Wenqiang Lei, Youcheng Huang, Chao Wang, Shuo Zhang, Jiancheng Lv,
Fuli Feng, and Tat-Seng Chua. TAT-QA: A question answering benchmark on a hybrid of
tabular and textual content in finance. InProceedings of the 59th Annual Meeting of the
Association for Computational Linguistics and the 11th International Joint Conference on
Natural Language Processing (Volume 1: Long Papers), pages 3277–3287, Online, August
2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.254. URL
https://aclanthology.org/2021.acl-long.254/.
[4] Zhiyu Chen, Shiyang Li, Charese Smiley, Zhiqiang Ma, Sameena Shah, and William Yang
Wang. ConvFinQA: Exploring the chain of numerical reasoning in conversational finance
question answering. InProceedings of the 2022 Conference on Empirical Methods in Natural
Language Processing, pages 6279–6292, Abu Dhabi, United Arab Emirates, December 2022.
Association for Computational Linguistics. doi: 10.18653/v1/2022.emnlp-main.421. URL
https://aclanthology.org/2022.emnlp-main.421/.
[5] Varshini Reddy, Rik Koncel-Kedziorski, Viet Dac Lai, Michael Krumdick, Charles Lovering,
and Chris Tanner. DocFinQA: A long-context financial reasoning dataset. InProceedings of
the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short
Papers), pages 445–458, Bangkok, Thailand, August 2024. Association for Computational
Linguistics. doi: 10.18653/v1/2024.acl-short.42. URLhttps://aclanthology.org/2024.
acl-short.42/.
[6] Zichen Tang, Haihong E, Ziyan Ma, Haoyang He, Jiacheng Liu, Zhongjun Yang, Zihua
Rong, Rongjin Li, Kun Ji, Qing Huang, Xinyang Hu, Yang Liu, and Qianhe Zheng. Fi-
nanceReasoning: Benchmarking financial numerical reasoning more credible, comprehensive
and challenging. InProceedings of the 63rd Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), pages 15721–15749, Vienna, Austria, July
2025. Association for Computational Linguistics. doi: 10.18653/v1/2025.acl-long.766. URL
https://aclanthology.org/2025.acl-long.766/.
[7] Qianqian Xie, Weiguang Han, Zhengyu Chen, Ruoyu Xiang, Xiao Zhang, Yueru He, Mengxi
Xiao, Dong Li, Yongfu Dai, Duanyu Feng, Yijing Xu, Haoqiang Kang, Ziyan Kuang, Chenhan
Yuan, Kailai Yang, Zheheng Luo, Tianlin Zhang, Zhiwei Liu, Guojun Xiong, Zhiyang Deng,
Yuechen Jiang, Zhiyuan Yao, Haohang Li, Yangyang Yu, Gang Hu, Jiajia Huang, Xiao-Yang
Liu, Alejandro Lopez-Lira, Benyou Wang, Yanzhao Lai, Hao Wang, Min Peng, Sophia
Ananiadou, and Jimin Huang. FinBen: A holistic financial benchmark for large language
models. InAdvancesinNeuralInformationProcessingSystems,volume37,pages95716–95743.
Curran Associates, Inc., 2024. URLhttps://proceedings.neurips.cc/paper_files/
paper/2024/hash/adb1d9fa8be4576d28703b396b82ba1b-Abstract-Datasets_and_
Benchmarks_Track.html.
[8] AntoineBigeard,LangstonNashold,RayanKrishnan,andShirleyWu. Financeagentbenchmark:
Benchmarking LLMs on real-world financial research tasks, 2025. URLhttps://arxiv.
org/abs/2508.00828.
17

[9] Alex Wang, Georg Meinhardt, Jacob Katz, Joseph H. Kim, Pratyush K. Chaudhary, Chase
Blagden, and Eric Xu. BigFinanceBench: A workflow-grounded benchmark for financial-
research agents, 2026. URLhttps://arxiv.org/abs/2606.03829.
[10] Eric Cho, Shawn Huang, Alice Lu, and Andy Lyu. Hedge-Bench: Benchmarking agents on
hard, realistic tasks pertaining to financial reasoning, 2026. URLhttps://arxiv.org/abs/
2606.03918.
[11] Beidi Luan, Rui Sun, Sinuo Wang, Yan Gu, Chao Li, Zhenliang Xiong, Jing Li, and Zuo Bai.
FinResearchBench II: A deep research benchmark with consensus-derived gold rubrics for
distinguishing financial report quality, 2026. URLhttps://arxiv.org/abs/2607.12252.
[12] Liang Hu, Jianpeng Jiao, Jiashuo Liu, Yanle Ren, Zhoufutu Wen, Kaiyuan Zhang, Xuanliang
Zhang, XiangGao, TianciHe, FeiHu, YaliLiao, ZaiyuanWang, ChenghaoYang, Qianyu Yang,
Mingren Yin, Zhiyuan Zeng, Ge Zhang, Xinyi Zhang, Xiying Zhao, Zhenwei Zhu, Hongseok
Namkoong,WenhaoHuang,andYuwenTang. FinSearchComp: Towardsarealistic,expert-level
evaluation of financial search and reasoning, 2025. URLhttps://arxiv.org/abs/2509.
13160.
[13] Chanyeol Choi, Jihoon Kwon, Alejandro Lopez-Lira, Chaewoon Kim, Minjae Kim, Juneha
Hwang, Jaeseon Ha, Hojun Choi, Suyeol Yun, Yongjin Kim, and Yongjae Lee. FinAgentBench:
A benchmark dataset for agentic retrieval in financial question answering, 2025. URLhttps:
//arxiv.org/abs/2508.14052.
[14] Yidong Jiang, Junrong Chen, Eftychia Makri, Jialin Chen, Peiwen Li, Ali Maatouk, Leandros
Tassiulas, Eliot Brenner, Bing Xiang, and Rex Ying. Fin-RATE: A real-world financial
analytics and tracking evaluation benchmark for LLMs on SEC filings, 2026. URLhttps:
//arxiv.org/abs/2602.07294.
[15] Lingfeng Zeng, Fangqi Lou, Zixuan Wang, Jiajie Xu, Jinyi Niu, Mengping Li, Yifan Dong,
Qi Qi, Wei Zhang, Ziwei Yang, Jun Han, Ruilun Feng, Ruiqi Hu, Lejie Zhang, Zhengbo
Feng, Yicheng Ren, Xin Guo, Zhaowei Liu, Dongpo Cheng, Weige Cai, and Liwen Zhang.
FinGAIA: A chinese benchmark for AI agents in real-world financial domain, 2025. URL
https://arxiv.org/abs/2507.17186.
[16] Wolfgang M. Pauli, Sarah Panda, Kidus Admassu, Said Bleik, Ademola Okerinde, and Jeremy
Reynolds. FORCE-Bench: A benchmark, dataset, and evaluation harness for agentic AI in
enterprise finance, 2026. URLhttps://arxiv.org/abs/2607.19409.
[17] Xueqing Peng, Zhuohan Xie, Yupeng Cao, Haohang Li, Lingfei Qian, Yan Wang, Vincent Jim
Zhang, Huan He, Xuguang Ai, Linhai Ma, Ruoyu Xiang, Yueru He, Yi Han, Shuyao Wang,
Yuqing Guo, Mingyang Jiang, Yilun Zhao, Youzhong Dong, Xiaoyu Wang, Yankai Chen,
YeYuan,QiyuanZhang,FuyuanLyu,HaolunWu,YonghanYang,ZichenZhao,YuyangDai,Fan
Zhang,RaniaElbadry,AyeshaGull,MuhammadUsmanSafder,NuoChen,FengbinZhu,Tianshi
Cai, Zimu Wang, Polydoros Giannouris, Yuechen Jiang, Zhiwei Liu, Mohsinul Kabir, Yuyan
Wang, Yixiang Zheng, Yangyang Yu, Weijin Liu, Wenbo Cao, Anke Xu, Peng Lu, Jerry Huang,
FengranMo,MingquanLin,PrayagTiwari,YijiaZhao,VictorGutierrezBasulto,Xiao-YangLiu,
Kaleb E. Smith, Jiahuan Pei, Arman Cohan, Jimin Huang, Yuehua Tang, Alejandro Lopez-Lira,
Xi Chen, Xue Liu, Junichi Tsujii, Jian-Yun Nie, and Sophia Ananiadou. Herculean: An agentic
benchmark for financial intelligence, 2026. URLhttps://arxiv.org/abs/2605.14355.
18

[18] Xianfu Cheng, Shiwei Zhang, Jiyu Zhao, Jian Yang, Xinyuan Wang, Ming Zhou, Weixiao
Zhou, Xiangyuan Guan, Xiang Li, Zhenhe Wu, Ziyi Ni, Zhoujun Li, and Bingjing Xu.
FinanceComplexQA: Benchmarking agentic reasoning on industrial-grade financial documents,
2026. URLhttps://arxiv.org/abs/2607.19238.
[19] Fangyuan Xu, Yixiao Song, Mohit Iyyer, and Eunsol Choi. A critical evaluation of evaluations
forlong-formquestionanswering. InProceedingsofthe61stAnnualMeetingoftheAssociation
for Computational Linguistics (Volume 1: Long Papers), pages 3225–3245, Toronto, Canada,
July 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.acl-long.181.
URLhttps://aclanthology.org/2023.acl-long.181/.
[20] Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. G-
Eval: NLG evaluation using GPT-4 with better human alignment. InProceedings of the
2023 Conference on Empirical Methods in Natural Language Processing, pages 2511–2522,
Singapore, December 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.
emnlp-main.153. URLhttps://aclanthology.org/2023.emnlp-main.153/.
[21] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao
Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez,
and Ion Stoica. Judging LLM-as-a-judge with MT-Bench and chatbot arena. InAdvances in
Neural Information Processing Systems, volume 36, pages 46595–46623. Curran Associates,
Inc.,2023. URL https://proceedings.neurips.cc/paper_files/paper/2023/hash/
91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html.
[22] Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-
Candela, Foivos Tsimpourlas, Michael Sharman, Meghan Shah, Andrea Vallone, Alex Beutel,
Johannes Heidecke, and Karan Singhal. HealthBench: Evaluating large language models
towards improved human health. 2025. URLhttps://arxiv.org/abs/2505.08775.
[23] Yukyung Lee, JoongHoon Kim, Jaehee Kim, Hyowon Cho, Jaewook Kang, Pilsung Kang,
and Najoung Kim. CheckEval: A reliable LLM-as-a-judge framework for evaluating text
generation using checklists. InProceedings of the 2025 Conference on Empirical Methods
in Natural Language Processing, pages 15771–15798, Suzhou, China, November 2025.
Association for Computational Linguistics. doi: 10.18653/v1/2025.emnlp-main.796. URL
https://aclanthology.org/2025.emnlp-main.796/.
[24] Manasi Sharma, Chen Bo Calvin Zhang, Chaithanya Bandi, Clinton Wang, Ankit Aich, Huy
Nghiem, Tahseen Rabbani, Ye Htet, Brian Jang, Sumana Basu, Aishwarya Balwani, Denis
Peskoff, Marcos Ayestaran, Sean M. Hendryx, Brad Kenstler, and Bing Liu. ResearchRubrics:
A benchmark of prompts and rubrics for evaluating deep research agents, 2025. URLhttps:
//arxiv.org/abs/2511.07685.
[25] Jie Ruan, Inderjeet Nair, Shuyang Cao, Amy Liu, Sheza Munir, Micah Pollens-Dempsey,
Tiffany Chiang, Lucy Kates, Nicholas David, Sihan Chen, Ruxin Yang, Yuqian Yang, Jasmine
Gump, Tessa Bialek, Vivek Sankaran, Margo Schlanger, and Lu Wang. ExpertLongBench:
Benchmarking language models on expert-level long-form generation tasks with structured
checklists, 2025. URLhttps://arxiv.org/abs/2506.01241.
[26] ChristosBaziotis.Criteria-Eval: Evaluatinglong-formanswerstocomplexquestions.SamayaAI
TechnicalBlog,June2025. URL https://samaya.ai/blog/criteria-eval. Contributors
include Ashwin Paranjape, Jack Hessel, Jack Silva, and Mingyi Yang. Accessed 2026-07-31.
19

[27] Rui Sun, Zuo Bai, Wentao Zhang, Yuxiang Zhang, Li Zhao, Shan Sun, and Zhengwen Qiu.
FinResearchBench: A logic tree based agent-as-a-judge evaluation framework for financial
research agents. InProceedings of the 6th ACM International Conference on AI in Finance,
pages 656–664. Association for Computing Machinery, 2025. doi: 10.1145/3768292.3770364.
URLhttps://doi.org/10.1145/3768292.3770364.
[28] Fengbin Zhu, Xiang Yao Ng, Ziyang Liu, Chang Liu, Xianwei Zeng, Chao Wang, Tianhui Tan,
Xuan Yao, Pengyang Shao, Min Xu, Zixuan Wang, Jing Wang, Xin Lin, Junfeng Li, Jingxian
Zhu, Yang Zhang, Wenjie Wang, Fuli Feng, Richang Hong, Huanbo Luan, Ke-Wei Huang,
and Tat-Seng Chua. FinDeepResearch: Evaluating deep research agents in rigorous financial
analysis, 2025. URLhttps://arxiv.org/abs/2510.13936.
[29] Mirazul Haque, Antony Papadimitriou, Samuel Mensah, Zhiqiang Ma, Zhijin Guo, Joy Prakash
Sain, Simerjot Kaur, Charese Smiley, and Xiaomo Liu. Deep FinResearch bench: Evaluating
AI’sabilitytoconductprofessionalfinancialinvestmentresearch, 2026. URL https://arxiv.
org/abs/2604.21006.
[30] Thomson Yen, Julian Poeltl, Harshith Srinivas Gear, Yilin Meng, Joshua Fan, Adam Shen,
Yili Liu, Ali Bauyrzhan, Siri Du, Haoyang Liu, Daniel Guetta, and Hongseok Namkoong.
MBABench: Evaluating LLM agents on end-to-end spreadsheet tasks in finance, 2026. URL
https://arxiv.org/abs/2605.22664.
[31] Michael Krumdick, Varshini Reddy, Shivani Chaudhary, William Day, Maarij Ahmed, Hayan
Haqqi, Muhammad Ahsen Fahim, Hanzallah Amjad, Ahmad Orakzai, Aqsa Gul, and Chris
Tanner. FrontierFinance: A long-horizon computer-use benchmark of real-world financial tasks,
2026. URLhttps://arxiv.org/abs/2604.05912.
[32] Jason Wei, Zhiqing Sun, Spencer Papay, Scott McKinney, Jeffrey Han, Isa Fulford, Hyung Won
Chung, Alex Tachard Passos, William Fedus, and Amelia Glaese. BrowseComp: A simple
yet challenging benchmark for browsing agents, 2025. URLhttps://arxiv.org/abs/2504.
12516.
[33] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas
Scialom. GAIA: a benchmark for general ai assistants, 2023. URLhttps://arxiv.org/
abs/2311.12983.
[34] Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Andrew Liu, Joshua Green,
Kshama Patel, Ruoxi Meng, Mingyi Su, Sahel Sharifymoghaddam, Yanxi Li, Haoran Hong,
Xinyu Shi, Xuye Liu, Nandan Thakur, Crystina Zhang, Luyu Gao, Wenhu Chen, and Jimmy
Lin. BrowseComp-Plus: A more fair and transparent evaluation benchmark of deep-research
agent, 2025. URLhttps://arxiv.org/abs/2508.06600.
[35] Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, and Zhendong Mao. DeepResearch
Bench: A comprehensive benchmark for deep research agents, 2025. URLhttps://arxiv.
org/abs/2506.11763.
[36] Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li,
Dacheng Li, Hao Zhang, Banghua Zhu, Michael I. Jordan, Joseph E. Gonzalez, and Ion Stoica.
Chatbot arena: An open platform for evaluating LLMs by human preference. InProceedings of
the 41st International Conference on Machine Learning (ICML), volume 235 ofProceedings of
Machine Learning Research, pages 8359–8388. PMLR, 2024.
20

[37] Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
InAdvances in Neural Information Processing Systems 36 (NeurIPS 2023), 2023.
[38] Ralph Allan Bradley and Milton E. Terry. Rank analysis of incomplete block designs: I. the
method of paired comparisons.Biometrika, 39(3/4):324–345, 1952. doi: 10.2307/2334029.
21

A Sample queries and rubrics by use case
The following six examples are the queries featured on the FrontierFinance benchmark page, one
per use case. For each query we show the first seven rubric items as displayed on the benchmark
page (must-have rubrics markedM; supplementary markedS), along with the total rubric count. The
complete set of 220 queries and all 11,543 rubrics is available via the Hugging Face data viewer at
https://huggingface.co/datasets/samaya-ai/FrontierFinance.
Screening & Discovery
Query:Which MedTech companies stand to gain from the new US presidential regime in 2025,
especially regarding tariffs and manufacturing flexibility, and which are expected to be negatively
impacted?Query date: 2025-05-24
S Summarizes all the information relating to the impact of the new US presidential regime
in 2025 on MedTech companies as bullet points under the headers of respective company
names.
M Provides information about Becton Dickinson and Co (BDX) stating that the company is
expected to not benefit under the Trump Administration of 2025.
S Provides information about Becton Dickinson and Co (BDX) stating that the company
is known for developing and manufacturing a wide range of medical devices, instrument
systems, and reagents used in various healthcare settings.
S Provides information about Becton Dickinson and Co (BDX) stating that the company
reported total sales of USD 5.27 billion for Q1 2025.
S Provides information about Becton Dickinson and Co (BDX) stating that the company cut its
2025 profit forecast.
S ProvidesinformationaboutBectonDickinsonandCo(BDX)statingthatthecompanyexpects
its 2025 profit per share to be between USD 14.06 and USD 14.34.
M Provides information about Becton Dickinson and Co (BDX) stating that the company cut its
2025 profit forecast due to potential tariff hit.
···+27 more rubric items
Company Research
Query:What has driven the slowdown in Intel’s revenues over the past two years?Query date:
2025-05-18
MStates that Intel Corporation (INTC) reported total revenue of USD 54.20 billion in 2023.
MStates that Intel Corporation (INTC) reported total revenue of USD 53.10 billion in 2024.
S States that Intel Corporation (INTC) reported a 5.00% decline in notebook volume in 2023.
SStates that Intel Corporation (INTC) reported a 9.00% decline in desktop volume in 2023.
M States that Intel Corporation (INTC) experienced a decline in client notebook volume due to
weak consumer demand in 2023.
22

M States that Intel Corporation (INTC) experienced a decline in client desktop volume due to
soft education and small and medium-sized business (SMB) markets in 2023.
M States that Intel Corporation (INTC) reported a reduction in average selling prices for
notebooks in 2023.
···+33 more rubric items
Sector, Industry & Macro
Query:How do room nights booked and revenue compare across Booking Holdings, Expedia,
Airbnb, and other top Online Travel Agencies (OTAs)?Query date: 2025-03-29
M States that the other top Online Travel Agencies are Trip.com Group Limited (TCOM) and
MakeMyTrip Limited (MMYT) based on their market capitalizations of more than USD 10
billion.
S Summarizes all the information relating to revenue and the number of nights booked for
Booking Holdings Inc. (BKNG), Expedia Group, Inc. (EXPE), Airbnb, Inc. (ABNB),
Trip.com Group Limited (TCOM) and MakeMyTrip Limited (MMYT) in a table format.
M Provides information for Booking Holdings Inc. (BKNG) stating that the total room nights
for full year 2024 were 1,144 million.
M Provides information for Booking Holdings Inc. (BKNG) stating that the total room nights
for full year 2023 were 1,049 million.
M Provides information for Booking Holdings Inc. (BKNG) stating that the total room nights
for full year 2022 were 896 million.
S Provides information for Booking Holdings Inc. (BKNG) stating that the total room nights
for full year 2024 increased by 9% year over year.
S Provides information for Booking Holdings Inc. (BKNG) stating that the total room nights
for full year 2023 increased by 17% year over year.
···+56 more rubric items
Financial Data Extraction
Query:Provide a breakdown of BP’s upstream, downstream, and integrated gas and renewables
segments’ operating metrics over the past 6 years.Query date: 2025-10-09
S Presents BP p.l.c. (BP) operating metrics from 2019 to 2024 in a structured or tabular format.
S Presents a footnote below the table for BP p.l.c. (BP) stating that for 2022, the Biogas supply
volumes exclude Archaea Energy.
M Provides information for BP p.l.c. (BP) stating that the Upstream Production for the year
2024 was 2.4 mmboe/d (million barrels of oil equivalent per day).
M Provides information for BP p.l.c. (BP) stating that the Upstream Production for the year
2023 was 2.3 mmboe/d.
M Provides information for BP p.l.c. (BP) stating that the Upstream Production for the year
2022 was 2.3 mmboe/d.
23

M Provides information for BP p.l.c. (BP) stating that the Upstream Production for the year
2021 was 2.2 mmboe/d.
M Provides information for BP p.l.c. (BP) stating that the Upstream Production for the year
2020 was 2.4 mmboe/d.
···+69 more rubric items
Coverage & Catalyst Monitoring
Query:In what ways have the AI strategies of Alphabet and Microsoft diverged across the past 8
quarters?Query date: 2025-06-09
M States that Alphabet Inc (GOOGL) defines Artificial Intelligence (AI) as a profound platform
shift central to its mission in 2024.
M States that Alphabet Inc (GOOGL) launched Gemini 1 and Gemini 1.5 in 2024 as next-
generation AI models.
S States that Alphabet Inc (GOOGL) designed Gemini models to process and combine text,
images, audio, video, and code in 2024.
M States that Alphabet Inc (GOOGL) integrated Gemini models into Search, Ads, Chrome,
Gmail, Maps, and YouTube in 2024.
S States that Alphabet Inc (GOOGL) enabled Gemini models to serve billions of users across
its core product suite in 2024.
M States that Alphabet Inc (GOOGL) uses Vertex AI in Google Cloud to help developers build
and scale generative AI applications in 2024.
S StatesthatAlphabetInc(GOOGL)incorporatesGeminiandDuetAIintoGoogleWorkspace
to enhance productivity tools in 2024.
···+46 more rubric items
Earnings & Events
Query:What positive and negative aspects came out of ABBV’s last earnings call?Query date:
2025-05-01
S Clearly separates the positive points and negative points from AbbVie Inc.’s (ABBV) last
earnings call transcript.
SStates that AbbVie Inc. (ABBV)’s latest earnings call was for Q1 2025.
M Providesa“NegativePoint”forAbbVieInc.(ABBV)fromitsQ12025earningscalltranscript
stating that global sales of Humira were down 49.5% on an operational basis.
S Provides a “Negative Point” for AbbVie Inc. (ABBV) stating that global sales of Humira
were down due to faster share erosion from biosimilar competition.
M Provides a “Negative Point” for AbbVie Inc. (ABBV) stating that aesthetics global sales were
down 10.2% on an operational basis.
S Provides a “Negative Point” for AbbVie Inc. (ABBV) stating that Botox cosmetic revenues
were down 10.7%.
24

S Provides a “Negative Point” for AbbVie Inc. (ABBV) stating that Juvederm sales were down
20%.
···+29 more rubric items
B Dataset statistics
Use cases.Each query carries exactly one of six use cases spanning the investor workflow; Table 6
gives the full counts and descriptions.
Table 6.Use case descriptions and distribution.
Use case Queries Share Description
Financial Data Extraction 70 31.8% Quantitative data extraction and modeling from
regulatory filings
Sector, Industry & Macro 38 17.3% Sector, industry, and macroeconomic research
across many entities
Earnings & Events 36 16.4% Queries centered on a corporate communication
event (earnings call or release, investor day, 8-K)
Company Research 32 14.5% Company-level research: business, strategy, and
operations
Coverage & Catalyst Monitoring 27 12.3% Tracking a name or topic over time across sources
Screening & Discovery 17 7.7% Open-ended screening and discovery over an un-
bounded set of entities
Capabilities.Each query is additionally tagged with the reasoning and retrieval capabilities it
requires. The raw counts and definitions for these capability categories are provided below in Table 7.
Table 7.Capability descriptions and distribution (a query may carry several, so counts sum to more than 220).
Capability Queries Share Description
Qualitative Synthesis 99 45.0% Curate and synthesize qualitative material across
documents
Exhaustive Retrieval/Temporal 71 32.3% Retrieve every qualifying item across multiple
time periods
Exhaustive Retrieval/Cross-Entity 44 20.0% Retrieve every qualifying item across multiple
entities
Exhaustive Retrieval/Thematic 32 14.5% Collect every instance of a theme or category
Numerical Reasoning 59 26.8% Compute or derive figures from multiple inputs
Multi-hop Workflows 53 24.1% Chained, conditional, multi-step tasks
Causal Reasoning 14 6.4% Explain the drivers behind an outcome
Simple Retrieval 38 17.3% Single-fact lookup or verification
Rubric content categories.Each of the 11,543 public-benchmark rubrics is classified into one of
eight content categories describing the kind of content the rubric demands (Table 8). Factual data
extractionistheplurality(74%),consistentwithrubricsbeingwrittenasobjective,checkablecriteria;
the remaining quarter spans the qualitative, forward-looking, analytical, and comparative content that
a complete answer must also deliver.
Rubric data source categories.In our annotation guideline, we define a ten-category data source
taxonomy. Each top-level data source category is paired with examples and a finer set of second-level
25

Table 8.Rubric category descriptions and distribution.
Rubric category Rubrics Share Description
Factual Data Extraction 8,547 74.0% Specific, verifiable data points (values, dates, names)
from primary sources
Qualitative & Contextual Information 1,039 9.0% Descriptive, non-numeric content: definitions, de-
scriptions, commentary
Forward-Looking Information 814 7.1% Future-oriented content: guidance, forecasts, projec-
tions
Analysis & Interpretation 558 4.8% Synthesis, causal reasoning, and interpretive insight
Comparative Analysis 264 2.3% Side-by-side comparison of entities, metrics, or peri-
ods
Format & Presentation 131 1.1% How information is structured or presented
Source & Methodology 112 1.0% Required sources, research scope, or calculation
method
Inquiry & Question Generation 78 0.7% Formulating questions for management or further
research
Table 9.Distribution of rubric data sources by use case. Each cell gives the number of rubric items drawn
fromthatdatasource,withthatsource’sshareoftherowinparentheses(%);Totalisthenumberofrubricitems
for that use case. Shares are rounded to whole numbers summing to 100 within each row. Column headings
abbreviate the data sources: SEC = SEC filings; Company = company originated content (e.g., transcripts,
investor presentations, press releases); Professional = professional knowledge; Market = market price data;
News = news and media sources; Regulatory = regulatory and legal data; Other = other categories.
Use case SEC Company Professional Market News Regulatory Other Total
Financial Data Extraction 3,378 (59) 1,222 (21) 863 (15) 97 (2) 28 (0) 2 (0) 167 (3) 5,757
Sector, Industry & Macro 643 (25) 378 (15) 825 (32) 334 (13) 78 (3) 26 (1) 269 (11) 2,553
Screening & Discovery 81 (8) 107 (11) 194 (19) 291 (29) 120 (12) 97 (10) 106 (11) 996
Earnings & Events 65 (8) 568 (68) 135 (16) 12 (2) 1 (0) 9 (1) 44 (5) 834
Coverage & Catalyst 136 (19) 408 (57) 95 (13) 54 (8) 3 (0) 0 (0) 24 (3) 720
Company Research 235 (34) 214 (31) 108 (16) 54 (8) 38 (6) 0 (0) 34 (5) 683
All use cases4,538 (39) 2,897 (25) 2,220 (19) 842 (7) 268 (3) 134 (1) 644 (6) 11,543
categories for clarity (e.g., 10-K or 10-Q as second-level categories for company filings). At
annotation time, we ask the annotator to record the data source categories that each written rubric
demands. For example, if the data in a specific rubric is drawn from a company 10-K document, the
rubric should be tagged as using company filing as top-level source and 10-K as second-level source.
We include this data source tag in the final released dataset, and show their detailed distributions by
use cases in Table 9.
C Difficulty analysis details
C.1 Methodology
What the score measures.Our difficulty score is a Bradley–Terry (BT) latent score [38] fit over
pairwise “which query is harder?” judgments across five reasoning axes (retrieval breadth, reasoning
depth, entity scope, time scope, qualitative ambiguity) on Samaya’s internal pool (𝑛=4,212 ).
We estimate latent difficulties𝜃 by minimizing the confidence-weighted, regularized negative
26

log-likelihood
ˆ𝜃=arg min
𝜃
−
∑︁
𝑘
𝑐(𝑚𝑘)log𝜎 𝜃𝑤𝑘−𝜃 ℓ𝑘  +𝜆∥𝜃∥ 2 2,
where 𝜃𝑖 is query𝑖’s difficulty,(𝑤𝑘,ℓ𝑘) are the winner/loser query in judgment𝑘 for difficulty,
𝑚𝑘 its confidence margin,𝜎 the logistic function,𝑐(1,2,3)=(0.3,1.0,1.3) the margin weights,
and𝜆=10 −3. To place external benchmarks on the same scale, we pair their 227 queries with
Samaya-dataset anchors into 6,810 comparison pairs, score them with the judges, and include them
in the BT fit; each external query’s percentile and bucket are then read off the shared scale.
Judging protocol and consensus fit.For every query in a pair, the judge sees the query text, its
date, use-case and capability tags, and the full criteria rubric (each criterion labelled by essentiality,
content type, and expected data source). The prompt defines difficulty as the retrieval and cognitive
effort an analyst would need for a complete, defensible answer, tells the judge to weigh the five axes
above, and warns against difficulty proxies—rubric count, query length, single-document extraction
breadth—so a long but shallow query is not scored as hard. The judge returns a winner (ties
allowed but discouraged), a 1–3 confidence margin, a per-axis vote, and a brief rationale; pairs are
judged independently. Three judges—Gemini 3.1 Flash Lite, Gemini 3 Flash, and Claude Sonnet
4.5—score every pair; we merge themper pairby signed-average (the pair is a tie if the mean is
within 0.5), then fit the single confidence-weighted Bradley–Terry model above to the resulting
consensus verdicts—each judgment weighted by its margin at𝑐(1,2,3)=(0.3,1.0,1.3) so close
calls count for a fraction of clear ones.
C.2 Robustness
Robustness to the judge model.Fit separately, each judge’s own ratings reproduce the consensus
approximately (Table 10): Spearman0.95–0.97 on the scores and 83–88% easy/medium/hard label
agreement. We also observed that Claude Sonnet is the steadiest judge—it flips the fewest verdicts
under order swap and ties most often.
Table 10.Each judge’s individual BT fit vs. the three-judge consensus, over the full pairwise set.
Judge BT-score Spearman𝜌vs. consensus Bucket-label agreement
Gemini 3 Flash 0.974 87.8%
Gemini 3.1 Flash Lite 0.955 83.1%
Claude Sonnet 4.5 0.946 82.5%
Position bias.Re-judging a fixed 20,000-pair sample with the two queries in swapped A/B order
flips the winner on 7% of consensus results, concentrated in low-confidence calls—28/11/2% at
margins 1/2/3 (Table 11). Because the confidence-weighted fit already discounts those close calls
(margin-1judgmentsenteratweight0.3),theresultbarelychanges: Refittingontheswappedverdicts
preserves the ranking (Spearman0.996) and 95.4% of easy/medium/hard labels.
Robustness to judgment volume.We probe the judgment budget two ways. First,per query: The
full set averages about 35 comparisons per query, so we subsample to𝑘 comparisons each, refit,
and compare to the full-data fit (Fig 12); returns diminish quickly—the ranking is essentially locked
by∼16 comparisons per query (Spearman0.99) and tercile labels reach 97% agreement by∼27.
Second,overall: Refitting on random 50% and 75% subsamples of all judgments (three draws each)
reproduces the full-data scores at Spearman0.99 and 0.996 and flips only 8.0% and 4.3% of labels,
respectively. These results show that we have sufficient pairwise samples to assign reliable scores.
27

Table 11.A/B position-swap flip rate by the judge’s own confidence margin, per judge and for the consensus
(20,000-pair sample).
Judge Margin 1 (close) Margin 2 (clear) Margin 3 (very clear) Overall
Gemini 3.1 Flash Lite 44% 28% 5% 21%
Gemini 3 Flash 33% 17% 3% 14%
Claude Sonnet 4.5 27% 12% 2% 11%
Consensus 28% 11% 2% 7%
60
70
80
90
100
0.70
0.80
0.90
1.00
2
4.7k
4
9.2k
6
13.7k
9
22.1k
16
40.9k
27
68.1kBT pairs
60.1%
0.716
84.4%
0.962
97.0%
0.998
Bucket match to full-data fit (%)
Spearman ρ  vs full-data fit
Comparisons per query (median)
Bucket match (left)
Spearman ρ  (right)
Figure 12.Difficulty-scale stability vs. judgment volume. Bucket match (left axis) and Spearman𝜌 (right
axis)ofasubsampledBTfitagainstthefull-dataconsensusfit,asafunctionofcomparisonsperquery(median;
total BT pairs in parentheses). Both saturate well before the full budget—the ranking is essentially locked by
∼16 comparisons per query.
Per-query score uncertainty.We draw 𝐵=20 bootstrap resamples of the judgment set (sampling
pairwise judgments with replacement to the original size), refit the BT model on each, and take the
standard deviation of a query’s score across the refits as its uncertainty. Scores are well-determined:
On a scale spanning∼36 units (−14to+22), the median per-query standard deviation is 0.67 and the
90th percentile 1.37 (2–4% of the range). About one query in five sits within one standard deviation
of an easy/medium or medium/hard cutoff, so near-boundary labels should be read as soft.
C.3 Analysis with resulting difficulty scores
Difficulty is not criteria count.Rubric count only moderately predicts difficulty (Spearman
𝜌=0.712 ,𝜌2≈0.51 ), explainingabouthalfoftherankvariance; thedepthandbreadthofreasoning
a query demands matter more than its raw rubric count.
Whichaxesdrivethejudgment.Restrictingtonon-tiepairsandpoolingallthreejudges,reasoning
depth and retrieval breadth agree with the overall winner most often (88.0% and 85.0%), followed by
qualitativeambiguity(74.2%),whiletimescope(53.0%)andentityscope(35.4%)agreeleast—mainly
because those two axes are themselves tied far more often (entity 62%, time 43% of pairs, versus
12–15% for the two dominant axes). Retrieval and reasoning demands discriminate between queries
far more often than entity or temporal scope.
Per-use-case difficulty.Difficulty varies systematically by use case (Table 12). Screening &
discovery and sector/industry & macro are the two hardest use cases across the board—open-ended,
unbounded-scope tasks that demand synthesis over many sources—while earnings & events and
company research are comparatively more tractable.
28

Table 12.Per-use-case difficulty, hardest to easiest.
Use case Queries Median difficulty pctile Hard / Med / Easy
Sector, Industry & Macro 38 98.3 28 / 7 / 3
Screening & Discovery 17 93.9 10 / 4 / 3
Financial Data Extraction 70 86.1 23 / 31 / 16
Coverage & Catalyst Monitoring 27 68.2 5 / 9 / 13
Earnings & Events 36 52.7 4 / 11 / 21
Company Research 32 47.5 3 / 12 / 17
Externalbenchmarks.Tables13givesthefullbox-plotstatisticsforthethreeexternalbenchmarks
discussed in Section 4.2.
Table 13.Bradley–Terry difficulty distribution per benchmark (box-plot statistics; higher = harder).
Benchmark𝑛10th Q1 (25%) Median Mean Q3 (75%) 90th IQR
FrontierFinance(ours) 220−4.01 0.19 3.734.8410.56 15.8810.38
Finance Agent v2 (public) 27−2.62−1.53−0.25 0.50 2.86 3.70 4.39
BigFinanceBench (public) 50−4.18−2.57−1.26−0.35 2.29 6.32 4.86
FinanceBench ([1]) 150−8.31−6.96−5.10−5.42−3.75−2.61 3.21
Table 14 reports where each benchmark’s median query falls as a percentile of Samaya’sentirepool
(𝑛=4,212 queries) and how its queries split across difficulty buckets. FrontierFinance’s median
query sits at the80th percentileof the internal corpus while the external benchmarks sit between the
16th and 49th percentile; correspondingly, a third of FrontierFinance falls in the hard tercile versus
0–2% for the externals.
Table 14.Difficulty positioning on the shared BT scale (percentile vs. Samaya’s internal distribution; higher =
harder). Hard/Medium/Easy are FrontierFinance’s own BT terciles.
Benchmark𝑛Median diff. pctile Hard Medium Easy
FrontierFinance(ours) 22080.073 (33.2%) 74 (33.6%) 73 (33.2%)
Finance Agent v2 (public) 27 48.6 0 (0.0%) 11 (40.7%) 16 (59.3%)
BigFinanceBench (public) 50 41.2 1 (2.0%) 14 (28.0%) 35 (70.0%)
FinanceBench (Islam et al., 2023) 150 15.9 0 (0.0%) 0 (0.0%) 150 (100.0%)
D LLM API Endpoints Details
We used the Microsoft Azure OpenAI API endpoints for accessing the GPT series models. This
also includes the GPT 5.5 Web Search harness, for which we used Azure OpenAI’s built-in search-
grounded API. We used the Google Vertex AI API endpoints for accessing the Gemini and Claude
seriesmodels,aswellastheirWebSearchharnessversions. WeusedtheFireworksAIAPIendpoints
for accessing the open-weight models, including the Kimi K3, GLM 5.2 and DeepSeek V4 Pro
models.
29

E System and user prompts for the adapted Finance Agent v2 harness
We include the system and user prompts of our re-implementation of the Finance Agent v2 harness
below. Compared to the original implementation, the only change is the added tool call limit
paragraph in the middle of the system prompt.
System prompt
You are a financial agent . You are given a question and you need to answer
it using the tools provided . You will not be able to interact with the
user or ask clarifications , you must answer the question only based on the
information provided .
You should answer all questions as if the current date is { date }.
You will have access to a data storage system . You can use this system to
store parsed contents of HTML pages retrieved from the web. You can then
use the retrieve_information tool to apply answer questions or gather
information from the stored documents using LLM - based prompts . This data
storage system is designed to help you avoid context window issues .
When you have the final answer , you should call the ‘submit_final_result ‘
tool with it. Your submission will not be processed unless you call this
tool .
When making tool calls , you need to make sure you stay within the
following limits :
- The maximum number of tool calls allowed ( None for no limit ): {
max_tool_calls }
- The maximum wall - clock seconds allowed for tool calling ( None for no
limit ): { max_tool_call_time }
If you are told that you have reached either of these limits , you must
call the ‘submit_final_result ‘ tool with the best answer you have gathered
so far.
IMPORTANT : If any tool response returns with instructions indicating that
tool call limit or time limit has reached , your VERY NEXT action MUST be
to call ‘submit_final_result ‘ with the best answer you have gathered so
far. Do not make any other tool calls except ‘submit_final_result ‘.
Failure to do so will cause the entire run to fail with no answer recorded
.
You should include any necessary step -by - step reasoning , justification ,
calculations , or explanation in your answer . You will be evaluated both on
the accuracy of the final answer , and the correctness of the supporting
logic .
When possible , please provide any calculated answers to at least two
decimal places (e.g. 18.78%
SEC filings are the most authoritative source of financial data . If a
number appears in both an SEC filing and another source (e.g., a press
release or company website ), use the SEC filing ’s figure . You may freely
use and cite non -SEC sources for information not available in SEC filings .
For historical price data not available in SEC filings , use the ‘
price_history ‘ tool as your primary source . Fall back to ‘web_search ‘ if
the price tool is not working . You should always use the raw , unadjusted
30

price data from the ‘price_history ‘ tool , unless the question specifically
asks for the adjusted price . Share prices should be reported in dollars
with 2 decimal places , e.g. $10 .25 per share . Stock indices (^ IXIC , ^GSPC ,
^SOX , etc .) are not covered by ‘price_history ‘ - for index historical
levels , start with an authoritative source such as the data provided by
FRED . If the question references a specific source , make sure to
incorporate information from that source , but still cross - reference SEC
filings where relevant .
When reporting financial figures , use the same scale and units as
presented in the SEC filing (e.g., if the filing reports values "in
millions ," report your answer in millions ), unless otherwise specified in
the question .
At the end of your answer , you should provide your sources in a dictionary
with the following format :
{
" sources ": [
{
"url ": " https :// example .com",
" name ": " Name of the source "
},
...
]
}
User prompt
Question :
{ question }
F System and user prompts for the grading LLM judge in FrontierFinance
We include the system and user prompts used for the LLM judges below. The same prompts are used
in our code release.
System prompt
You are a senior financial analyst . Your task is to evaluate a financial
report against a list of pre - defined rubrics . The report presented to you
is generated to answer a specific financial query . For each given rubric ,
you are expected to produce a binary judgement on whether the rubric is
satisfied or not by the financial report .
For each task , you will be given the following :
1. A financial query , which specifies the information the user is seeking .
2. The date the query was made . This is important for assessing the time
understanding of the system . Whenever necessary , you should use this date
as the temporal anchor for interpreting relative date terms in both the
query and the rubrics .
3. A financial report which aims to answer that query .
31

4. One or more natural language rubrics , each checking a specific aspect
of the report .
All of the input will be clearly marked in XML tags . Your task is to judge
whether the report adequately satisfies each of the given rubrics . You
must evaluate the report objectively and thoroughly .
Pay special attention to the following aspects when making your judgement :
1. ** Each rubric should be judged independently **. Even in the case that
one rubric seems related to another , you need to give your judgement of
whether each rubric is satisfied independently .
2. ** Pay attention to numerical units **. The report and the rubric might
use different units to represent the same number . Take this into account
when making your judgement . For example , "USD 2.1 billion " is equivalent
to "USD 2 ,100 million ".
3. ** Accept reasonable numerical approximation **. A figure in the report
is acceptable if it equals the rubric ’s figure after rounding the rubric ’s
figure to the ( coarser ) precision the report uses . A figure stated at the
same or finer precision than the rubric ’s, but with a different value , is
NOT acceptable -- even if numerically close . For example , against a
rubric value of "3 ,098 million ": "3.1 billion " is acceptable (a correct
rounding to two significant figures ), but "3 ,105 million " is not (it
asserts a precise , different value ). Likewise against "7.14%
User prompt
You will evaluate the report below against the given set of rubrics . The
report has been written to answer a specific query .
The query is provided below within the <query > tags .
<query >
{ query }
</query >
The date the query was submitted is provided below within the <date > tags .
This is important for assessing whether the report correctly understands
the time aspect of the query .
<date >
{ query_date }
</date >
The financial report is provided below within the <report > tags .
<report >
{ report }
</report >
Now that you have read the query and the report , please evaluate whether
the report satisfies each of the following rubrics . The list of rubrics is
provided below within the <rubrics > tags . Each rubric is annotated with a
unique ID , which you should use in your output to refer to that rubric .
<rubrics >
{ rubrics }
</ rubrics >
32

For each rubric , determine if the report adequately satisfies it. As a
reminder , pay attention to the following aspects mentioned before :
- Each rubric should be judged independently .
- Pay attention to numerical units .
- Accept reasonable numerical approximation .
Your output must be ONLY a valid JSON object with the following structure :
‘‘‘json
{
"0": {
" reason ": " concise 1- sentence reason for your judgement on rubric 0",
" label ": true / false
},
"1": {
" reason ": " concise 1- sentence reason for your judgement on rubric 1",
" label ": true / false
},
...
}
G Tool call distribution for all models
We provide the tool call distribution statistics of all models under the Finance Agent v2 harness in
Table 15.
Table 15.Share of each system’s tool calls going to each tool available in the harness (%). Calls per query
represents the average number of tool calls over all answered queries.𝑅all represents the macro-averaged
qualification rate over all rubrics.
Web Parse Retrieve EDGAR Calcu- Price Calls /𝑅 all
System search HTML info. search lator history query (%)
Claude Fable 5 24.4 25.1 19.3 6.4 23.3 1.5 16.6 49.2
GPT 5.6 Sol 44.8 16.9 13.1 4.7 20.0 0.4 46.3 46.8
Kimi K3 36.5 26.6 18.7 6.8 9.9 1.5 19.6 46.4
Gemini 3.6 Flash 31.1 20.0 21.8 11.0 15.4 0.7 24.8 46.3
Claude Opus 4.8 29.6 27.0 20.5 6.1 15.6 1.1 16.1 45.0
GPT 5.5 27.7 26.2 14.6 7.7 23.1 0.7 33.7 43.5
GLM 5.2 28.8 29.1 22.3 11.8 7.3 0.7 26.9 42.8
DeepSeek V4 Pro 45.2 21.4 18.5 4.5 9.9 0.5 41.1 40.5
Gemini 3.1 Pro 41.3 21.1 22.0 13.4 1.0 1.0 16.1 30.5
H Performance breakdown by use case
Table 16 reports the macro-averaged rubric qualification rate for each system broken down by use
case. Table 17 reports the micro-averaged rubric qualification rate for each system broken down by
rubric categories.
33

Table 16.Macro-averaged rubric qualification rate (%) per use case for all evaluated systems, grouped by
harness and ranked by𝑅all within each group. Use case abbreviations:Fin.= Financial Data Extraction;
Earn.= Earnings & Events;Co.= Company Research;Cov.= Coverage & Catalyst Monitoring;Sec.= Sector,
Industry & Macro;Scr.= Screening & Discovery.
System𝑅 all Fin. Earn. Co. Cov. Sec. Scr.
Web Search Harness
Claude Opus 4.8 33.0 31.3 45.6 32.5 28.1 30.6 27.4
Gemini 3.1 Pro 30.7 29.1 41.3 29.7 32.1 25.0 27.2
GPT 5.5 20.7 17.3 26.1 24.5 27.0 14.0 21.7
Finance Agent v2 Harness
Claude Fable 5 49.2 55.6 63.9 40.5 49.0 38.1 33.3
GPT 5.6 Sol 46.8 48.9 58.0 42.1 46.7 40.9 36.5
Kimi K3 46.4 46.5 61.0 45.9 46.9 36.6 36.9
Gemini 3.6 Flash 46.3 56.2 54.0 41.2 36.5 36.4 36.1
Claude Opus 4.8 45.0 51.0 57.7 38.9 43.2 35.2 30.2
GPT 5.5 43.5 47.6 53.7 39.7 41.5 34.7 34.8
GLM 5.2 42.8 47.5 52.0 38.5 46.4 34.4 24.9
DeepSeek V4 Pro 40.5 45.3 54.5 32.1 38.5 32.7 28.1
Gemini 3.1 Pro 30.5 31.4 42.5 29.1 27.4 25.0 21.6
Samaya In-house Harness
Samaya (high effort) 56.0 59.5 75.1 56.5 58.3 38.5 36.2
Samaya 52.9 55.3 71.0 52.8 57.8 38.7 28.6
34

Table 17.Micro-averaged rubric qualification rate (%) per rubric category for all evaluated systems, grouped
by harness and ranked by𝑅all within each group.𝑅all is the overall macro-averaged qualification rate (as in
Table 16), included for system ranking purposes. Category columns aremicro-averaged over all rubrics in
each category. Category abbreviations:Fact.= Factual Data Extraction;Qual.= Qualitative & Contextual
Information;Anly.= Analysis & Interpretation;Comp.= Comparative Analysis;Fwd.= Forward-Looking
Information;Fmt.= Format & Presentation.
System𝑅 all Fact. Qual. Anly. Comp. Fwd. Fmt.
Web Search Harness
Claude Opus 4.8 33.0 17.4 32.4 41.5 38.1 23.8 56.6
Gemini 3.1 Pro 30.7 20.0 25.6 41.9 42.9 25.9 53.4
GPT 5.5 20.7 16.0 29.9 40.2 39.5 24.6 59.3
Finance Agent v2 Harness
Claude Fable 5 49.2 43.1 41.2 49.9 50.2 48.0 74.4
GPT 5.6 Sol 46.8 35.7 44.2 52.5 53.0 43.4 79.4
Kimi K3 46.4 29.7 42.6 49.7 49.4 35.5 65.9
Gemini 3.6 Flash 46.3 38.0 36.5 48.6 45.5 39.2 74.1
Claude Opus 4.8 45.0 38.3 36.7 49.8 50.4 38.7 73.3
GPT 5.5 43.5 38.3 40.4 48.4 45.6 40.7 77.5
GLM 5.2 42.8 28.7 38.9 43.9 45.5 38.2 67.2
DeepSeek V4 Pro 40.5 30.2 36.5 44.3 39.8 29.6 65.1
Gemini 3.1 Pro 30.5 20.2 25.7 38.5 37.9 20.0 47.3
Samaya In-house Harness
Samaya (high effort) 56.0 46.6 48.6 54.7 48.9 51.5 75.6
Samaya 52.9 40.7 47.1 55.7 52.3 46.0 69.5
35
