---
title: 'ERPBench: Evaluating LLM Agents for Enterprise Decision-Making Across Competitive Market Ecologies'
url: https://arxiv.org/abs/2609.04667
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Xinran Zhang
- Pengrui Lu
- Lyumanshan Ye
- Pengfei Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.04667
pages: 10
chars: 41077
fetched_at: '2026-11-08T13:20:08+00:00'
kb_version: 1
---

# ERPBench: Evaluating LLM Agents for Enterprise Decision-Making Across Competitive Market Ecologies

SII-GAIR
ERPBench: Evaluating LLM Agents for Enterprise
Decision-Making Across Competitive Market Ecologies
Xinran Zhang1,2,4,* Pengrui Lu1,3,4,* Lyumanshan Ye3,4 Pengfei Liu1,3,4,†
1Shanghai Innovation Institute 2Beijing Institute of Technology
3Shanghai Jiao Tong University 4GAIR Lab
*Equal contribution. †Corresponding author.
Abstract
Large language model (LLM) agents are increasingly proposed for enterprise workflows, yet existing
evaluations rarely test whether business-decision conclusions transfer across competitive market ecologies.
WeintroduceERPBench,anexecution-instrumentedbenchmarkforenterprisedecisionagentsinasix-round
Enterprise Resource Planning (ERP) simulation with coupled pricing, production, procurement, inventory,
finance, and shared-market competition. ERPBench evaluates the same 100 fixed problems in two matched
competitive market ecologies:Solo, where each evaluated LLM agent competes against fixed rule-based
opponents, andArena, where six evaluated LLM agents compete in a shared market. Across six model
families, this yields 1,200 model-level trajectories spanning 7,200 decision rounds. Under the observed
service configuration, the leading model differs between ecologies: DeepSeek leads inSolo(252.29M
mean valuation; mean rank 1.67), whereas Gemini leads inArena(263.95M; 1.76). The two ecologies
identify the same task-level winner on only 21 of 100 problems, and Gemini’s bottom-rank rate falls from
22% to 0% inArena. ERPBench supports paired evaluation of whether enterprise-agent rankings transfer
across competitive market ecologies, supplemented by aggregate execution-intervention analysis. Code
and benchmark resources are available in our GitHub repository.
1 Introduction
LLM-agent evaluation has moved from static question answering toward stateful digital environments, including
tool use, code repair, web navigation, desktop control, and workplace workflows (Liu et al., 2024; Jimenez et al.,
2024; Zhou et al., 2024; Xie et al., 2024; Yao et al., 2025; Xu et al., 2025). Enterprise decision agents require a
complementaryformofreliability: theyrepeatedlyallocatescarceresourceswhilepricing,production,procurement,
inventory, and finance decisions compound over time. In competitive markets, these decisions are also strategically
coupled, because one agent’s price or inventory policy changes the demand landscape faced by the others. We call
the composition and behavior of opponents that share a market with an evaluated LLM agent thecompetitive market
ecology(orecologyfor short). Thus, the relevant benchmark question is not only whether an agent can produce a
high-scoring business plan, but whether conclusions about the agent remain stable when the same business problem
is embedded in a different ecology.
Formally, ERPBench asks:does the selected model differ across matched competitive market ecologies for the same
enterprise task?To answer it, we need three measurement ingredients. First, aprimary outcome metric: terminal
company valuation computed by a dividend discount model (DDM) at the end of six decision rounds. Second,
complementary reliability indicators: mean within-problem rank, bottom-rank rate (the fraction of problems on
which a model ranks last), and normalized regret (the gap to the best model scaled by the within-problem valuation
range). Third, anexecution audit layer: logged decision records and execution-audit information, where available,
linking parsed decisions, feasibility checks, clamping, fallback, and runtime recovery so that a terminal score can be
qualified by how it was produced. Three structural challenges make this measurement non-trivial: (1)multi-round
compounding—decisions span six rounds of thirty simulated days each, so early pricing or production errors
propagate forward; (2)joint constraint satisfaction—pricing, production, procurement, inventory, and finance
decisions are mutually constrained by capacity, cash, and demand, so a locally plausible action may be globally
infeasible; and (3)strategic coupling under competition—in a shared market, one agent’s price or inventory policy
changes every other agent’s demand, so identical decisions can yield different outcomes against different opponents.
1
arXiv:2609.04667v1  [cs.AI]  4 Sep 2026

ERPBench
SII-GAIR
Figure 1: ERPBench overview. The same 100 ERP problems are evaluated under matchedSoloandArena
competitive market ecologies. The protocol matches problem configurations and model-family labels while
changingtheopponentcomposition; sixdecisionroundsyieldterminaloutcomesandexecution-auditrecordswhere
available.
Aconventionalbenchmarkdesignwouldfixasinglecompetitivemarketecologyandreportoneterminalleaderboard.
This design is attractive because it is simple and reproducible, but it is incomplete for enterprise competition:
opponent behavior is not background noise. It changes prices, demand allocation, inventory pressure, market share,
and downstream cash-flow outcomes. As a result, a model can be strong against stable rule-based competitors yet
lose its advantage when other evaluated LLM agents shape the same market; conversely, a model with weak isolated
performance may become more reliable in a shared market. Enterprise-agent benchmarks should therefore treat
competitive market ecology as a controlled measurement condition rather than incidental setup.
A second challenge is that enterprise decisions must be executable, not merely plausible. A model may return a
syntactically valid action that violates production capacity, requests unavailable investment, over-orders under cash
constraints, or requires fallback parsing. Terminal valuation alone does not reveal whether the score was produced
through direct execution or through repeated repair. For this reason, an enterprise benchmark should record parsed
decisions, feasibility checks, clamping, fallback, simulation updates, and terminal outcomes.
We introduce ERPBench, an execution-instrumented benchmark for measuring enterprise decision agents under
controlled competitive market ecologies. ERPBench uses an independently constructed Enterprise Resource
Planning (ERP) simulation covering production, supply chain, inventory, finance, market competition, and carbon
costs. Each of the same 100 ERP problems is evaluated under two matched ecologies:Solo, where each evaluated
LLM agent competes against fixed rule-based opponents, andArena, where six evaluated LLM agents compete in a
shared market. The paired design matches problem instances and model-family labels across ecologies, yielding
1,200 model-level trajectories spanning 7,200 decision rounds across six model families.
ERPBench makes three contributions. First, it provides a controlled ERP-agent task substrate in which pricing,
production, procurement, inventory, and finance decisions are jointly constrained over a six-round horizon. Second,
its central measurement contribution is a paired ecology protocol that evaluates the same model-family–problem
pairs under fixed-opponentSoloand shared-marketArenaconditions. Third, it supplements outcome comparisons
with logged execution-intervention evidence: DeepSeek leadsSolowhile Gemini leadsArena, the two ecologies
identify the same task-level winner on only 21 of 100 problems, and tail-risk profiles differ.
The resulting benchmark treats both competitive market ecology and execution-audit information as part of the
measurement specification. This goes beyond a terminal score: for ERP agents, the scoring path includes whether a
structured action could be parsed, whether it respected capacity, procurement, inventory, and finance constraints,
and whether the simulator required repair, clamping, fallback, or runtime recovery. ERPBench therefore supports
not only outcome comparison, but also process-level characterization of how outcomes were produced.
2 Related Work
Stateful executable agent benchmarks.Recent agent benchmarks have moved evaluation beyond static question
answering toward interactive, stateful, and executable tasks. AgentBench, SWE-bench, WebArena, OSWorld, and
𝜏-bench evaluate agents in environments where actions change state and outcomes can be checked through code,
web interfaces, desktop applications, or tool-mediated user interactions (Liu et al., 2024; Jimenez et al., 2024; Zhou
et al., 2024; Xie et al., 2024; Yao et al., 2025). This line of work establishes a central baseline for ERPBench: agent
evaluation should be reproducible, stateful, and outcome-verifiable. However, these benchmarks usually hold the
surrounding competitive market ecology fixed. ERPBench asks a complementary question: whether conclusions
about the same enterprise decision task remain stable when the competitive market ecology changes.
Enterprise and professional agent benchmarks.A second line of work evaluates agents in professional software
and workplace settings. TheAgentCompany and WorkArena++ study agents completing realistic workplace tasks,
2

ERPBench
SII-GAIR
while CRMArena and CRMArena-Pro move this direction into business-facing CRM environments with realistic
enterprise data, roles, and interactions (Xu et al., 2025; Boisvert et al., 2024; Huang et al., 2025, 2026). These
benchmarks are important because they test whether agents can operate inside professional workflows rather than
isolatedtoytasks. ERPBenchdiffersintheobjectofmeasurement: itevaluatescoupledenterpriseresourceplanning
decisions rather than CRM or office-task completion. In ERPBench, pricing, production, procurement, inventory,
capacity, finance, and final valuation are jointly constrained by the simulator, so a plausible plan is not sufficient
unless it can be executed.
Economic and competitive agents.Economic-agent benchmarks study LLM behavior in markets, financial
decisions, retail operations, and competitive environments. CompeteAI, EconAgent, InvestorBench, RetailBench,
and Market-Bench provide evidence that LLM agents can be evaluated as economic decision-makers rather than
only language or tool users (Zhao et al., 2024; Li et al., 2024, 2025; Zhang et al., 2026; Zheng et al., 2026).
ERPBench builds on this direction but changes the measurement target. Its central comparison is not only which
model performs best in a business domain, but whether the same model–problem pair yields the same conclusion
under the fixed-opponentSoloecology and the shared-marketArenaecology populated by evaluated LLM agents.
This paired design makes competitive market ecology an explicit experimental factor.
Benchmark validity, trajectories, and protocol sensitivity.Recent work also argues that benchmark conclusions
depend on evaluation design, interaction protocol, and trajectory evidence.𝜏2-Bench studies dynamic multi-
party trajectories (Barres et al., 2025), benchmark-sensitivity analyses show that model rankings can shift under
protocol changes (Alzahrani et al., 2024), and benchmark-design studies such as BetterBench emphasize validity,
reproducibility, and lifecycle quality in evaluation artifacts (Reuel et al., 2024). ERPBench operationalizes these
concerns for enterprise agents by retaining round-level decision records and execution-audit information, where
available, and reporting paired outcome changes across controlled competitive market ecologies. The audit records
show not only what an agent proposed, but also whether the action could be parsed, repaired, clamped, or executed
under ERP constraints. In this sense, ERPBench treats both competitive market ecology and execution-audit
information as part of the measurement specification.
Figure 2: Aggregate outcomes under matched competitive market ecologies. Gray bars:Solomean valuation across
100 matched problems; colored bars:Arenamean valuation on the same problems. Numbers above bars report
mean rank (lower is better). Arrows show rank-shift magnitude and direction (green improves; red worsens).
3 ERPBench
3.1 Operational Simulation and Executable Interface
ERPBench is designed around three measurement requirements. First, the task must be operationally coupled:
pricing, production, procurement, inventory, capacity, cash, and valuation should affect one another rather than
appear as isolated subtasks. Second, decisions must be executable: an agent should not receive credit for a
plausible business plan unless it can be parsed and run under ERP constraints. Third, the benchmark must support
ecological comparison: the same model-family–problem pair should be measurable under different competitive
market ecologies while holding the underlying task fixed.
To instantiate these requirements, ERPBench builds on ERPsim-style business games (Léger et al., 2007, 2011)
and simulates a cereal manufacturing firm over six rounds of 30 simulated days each. Agents decide SKU prices,
productionquantities,procurement,marketingallocation,andfinancialactionsfor12SKUsacrossthreedistribution
channels. The environment includes batch production with capacity and lot-size constraints, supplier lead times,
warehouse inventory, cash-flow and credit dynamics, carbon costs, and a multinomial competitive interaction (MCI)
demand model (Cooper and Nakanishi, 1988). These components make terminal performance depend on both
strategicchoicesandoperationalfeasibility: apricingplanthatignoresinventory,forexample,canincreasenominal
margin while losing demand or creating stockouts.
3

ERPBench
SII-GAIR
Each evaluated model family uses the same single-agent scaffold and the same executable interface. Before each
decision, the LLM agent receives the current ERP state and may query tools for finance, inventory, market price,
demand, raw materials, and carbon information. It then returns a structured JSON action containing SKU prices,
production quantities, purchase orders, marketing allocation, and finance actions. The simulator parses the action,
checks feasibility, repairs or clamps infeasible fields when necessary, executes the round, and records the resulting
ERP state. Where execution audit logs are available, they contain both the proposed decision and the interventions
required to make that decision executable.
This interface is intentionally stricter than a natural-language planning task. ERP decisions are not merely
recommendations; they must survive capacity, cash, inventory, and availability constraints. The action space is
also deliberately coupled. Prices influence demand through the competitive market model, but demand can only
be converted into value if the agent has produced and stocked the right SKUs in the right channels. Procurement
choices affect future production rather than only the current round, and finance actions can preserve cash viability
but may not be available in every state. These dependencies allow early mistakes to propagate through inventory,
capacity, and cash-flow constraints before appearing in the final valuation.
3.2 Paired Ecologies and Measurement Protocol
ERPBench evaluates each model family on the same 100 ERP problem instances under two matched competitive
market ecologies. InSolo, the focal LLM agent competes against five deterministic rule-based opponents with
conservative, aggressive, balanced, growth-oriented, and risk-averse policies. InArena, six evaluated LLM agents
compete in a shared market. The matched comparison preserves the problem identifier, seed, difficulty stratum,
scenario category, agent scaffold, decision horizon, outcome metrics, and model-family label while changing the
opponent composition.Soloranks are computed by comparing the six model families’ separate fixed-opponent
trajectories on the same problem; rule-based opponents do not enter the reported model ranking. We useLLM
agentfor a deployed decision-making instance that receives ERP state and tool outputs and returns structured
multi-round decisions;model familydenotes the underlying evaluated LLM condition, andmodelis shorthand only
when reporting rankings. Each model–problem–ecology trajectory spans six rounds.
The primary outcome is sixth-round terminal company valuation, which aggregates profitability, financial viability,
and expected future cash flows. We also report within-problem rank, task-level winner agreement, normalized
regret, bottom-rank rate, difficulty-stratified effects, and logged execution-intervention categories. For each model
𝑚and problem𝑝, the paired ecology effect is
Δ 𝑝,𝑚 =𝑉 Arena 𝑝,𝑚 −𝑉 Solo 𝑝,𝑚 .(1)
We report model-level mean effects with 95% percentile-bootstrap confidence intervals over problems. Paired
valuation tests use two-sided Wilcoxon signed-rank tests with Benjamini–Hochberg correction across the six
model-wise tests. Logged execution-intervention categories are non-exclusive process diagnostics, not causal
decompositions of final valuation. For the descriptive reliability–performance panel, theL2 operational reliability
scorefor model family𝑚 inArenais 1−𝑟 𝑚/max𝑚′ 𝑟𝑚′, where𝑟𝑚 is its logged operational-intervention rate per
model-leveltrajectory. Thiswithin-panelnormalizationisanauditsummary,notaprimaryoutcomemetricorcausal
measure. TheDecisionQualityPyramidinFigure1isanorganizingtaxonomy,notacompositescore: L1structural
validity summarizes parser-related interventions; L2 operational feasibility is summarized by the operational
reliability score; L3 financial quality is rank-derived terminal performance; L4 disruption response restricts that
performance to hard and random-hard tasks; and L5 short-horizon adaptation is the average improvement in
within-problem rank from Round 1 to Round 6. L3–L5 are descriptive proxies.
The 100 problems cover baseline, dual-pressure, and harder operational scenarios. We use these strata to check
whether an ecology effect is robust across problem families rather than driven by a single scenario type. This
matters because an ERP benchmark can otherwise reward a model that specializes in one high-variance slice while
being unreliable in routine or constraint-heavy settings. ERPBench therefore reports both aggregate performance
and structured heterogeneity across task families.
4 Experiments
4.1 Setup
We evaluate six model families—Claude Opus 4.6, DeepSeek-V4-Flash, Gemini 3.1 Pro Preview, GPT-5.5, Doubao
Seed 2.0 Pro, and Qwen 3.7 Max—under the paired ecology protocol described above. All models were evaluated
with the same agent scaffold and six-round protocol.
The analysis uses the same 100 problem identifiers in bothSoloandArena. Each ecology contains 600 model-level
terminal outcome records and 3,600 ordered model-level decision-round records. Thus, the benchmark contains
4

ERPBench
SII-GAIR
1,200 model-level trajectories and 7,200 model-level decision rounds. Operationally, these correspond to 600
independentSolosimulator executions and 100 shared six-modelArenaexecutions, or 700 simulator executions in
total. Terminal valuations are read from the sixth-round decision record. Coverage, duplicate, and missing-record
checks confirm 100/100 problem coverage, no duplicate model–problem records, and no missing expected records.
This design makes the comparisons below paired rather than cross-sectional. When we report that a model gains
or loses valuation inArena, the quantity is computed on the same problem set with the same model-family label
and problem seed. It is therefore a paired benchmark contrast under the observed service configuration, not a
comparison between separately sampled leaderboards.
4.2 Ecology Reorders Aggregate Performance
Table 1 and Figure 2 show that the aggregate leaderboard changes
across ecologies. DeepSeek leadsSolowith 252.29M mean valuation
and mean rank 1.67, whereas Gemini leadsArenawith 263.95M and
mean rank 1.76. Because the comparison is paired by problem, the
reversal is not a difference between unrelated samples: Gemini gains
+94.54M on the same problems, while DeepSeek and Qwen decrease
by 17.58M and 18.74M, respectively.
The benchmark implication is that a single-ecology leaderboard gives
an incomplete conclusion:Soloselects DeepSeek, whileArenaselects
Gemini. ERPBench exposes this discrepancy by treating competitive
market ecology as a measurement variable rather than assuming one
model is universally superior.
Table1: Matched-ecologyaggregateperformance. Val. ismean
terminal valuation (M); lower rank is better;Δ𝑉 isArena–Solo.
Confidence intervals appear in Appendix B.
Model Solo ArenaΔ𝑉 𝑞
Val. Rank Val. Rank M
DeepSeek252.29 1.67234.71 2.36−17.58.0116
Gemini 169.41 3.51263.95 1.76+94.54 1.28×10 −15
GPT-5.5 186.43 3.87 194.82 3.91+8.39.126
Qwen 205.87 3.27 187.13 4.01−18.74.0061
Doubao 181.27 4.10 188.17 4.28+6.90.557
Claude 176.78 4.58 173.95 4.68−2.83.866
Figure 3: Execution-intervention summary.
Most logged events are production-capacity
skips; fallback decisions and tracebacks indicate
output-pipeline or runtime recovery.
4.3 Terminal Scores Need Trace Qualification
A terminal valuation is necessary for ranking ERP agents, but it is not sufficient for diagnosing enterprise-agent
reliability. Thesamefinalscorecanbereachedthroughacleanexecutablepathorthroughrepeatedparsingrecovery,
feasibility repair, clamping, or fallback. These two cases are both valid simulator outcomes, but they imply different
reliability profiles for deployment.
ERPBench therefore uses execution-audit records behind terminal valuations where logging is available. These
records link model outputs, parsing results, feasibility checks, repair or clamping events, fallback paths, executed
actions, and resulting ERP states. The audit layer lets the analysis separate three questions that would otherwise be
conflated: which model obtains the highest value, whether that conclusion transfers across competitive market
ecologies, and whether aggregate performance coincides with substantial execution-intervention burden.
4.4 Execution Audit Exposes Execution Fragility
Logged execution-audit records show where the executable decision pipeline required intervention. Among the
five displayed intervention types in Figure 3, production-capacity skips account for the largest share (3,761 events,
82.5%),followedbyunavailableinvestmentchoices(355,7.8%),fallbackdecisions(275,6.0%),production-quantity
clamping (118, 2.6%), and tracebacks (48, 1.1%). Panel (b) poolsSoloandArenatrajectories, whereas Figure 5
usesArena-only rates. The displayed shares exclude five omitted run-level failures.
These logged categories should be interpreted as process diagnostics rather than causal decompositions of terminal
valuation. A capacity skip often means that a requested production item could not be scheduled under machine
capacity, lot-size, or material constraints; it may reflect an aggressive production plan in a constrained plant rather
5

ERPBench
SII-GAIR
than a malformed decision. By contrast, fallback decisions and tracebacks more directly indicate output-pipeline or
runtime fragility. Execution audit therefore qualifies the aggregate outcome measurement by summarizing how
often the executable pipeline required intervention.
4.5 Task-Level Rankings Disagree
The aggregate reversal is not only a mean-score artifact. At the individual-task level, the two ecologies identify the
same task-level winner on only 21 of 100 problems, and the mean within-problem Spearman rank correlation is
0.182 with bootstrap CI [0.090, 0.273]. The largest transition is from DeepSeek to Gemini: 35 problems won by
DeepSeek inSoloare won by Gemini inArena.
Figure4showsthatecologychangesboththeidentityofthebestmodelandtherankorderingwithinmanyproblems.
This matters for benchmark interpretation. If the aggregate reversal were driven by a few extreme outliers, it
would be weaker evidence of ecology-sensitive measurement. Broad winner disagreement instead shows that the
competitive market ecology changes many local judgments about which model is best for the same ERP task.
Figure 4: Task-level disagreement betweenSoloandArenaacross the same 100 matched ERP problems. The two
ecologies identify the same task-level winner on only 21 problems and often produce different rankings.
4.6 Reliability Qualifies Terminal Scores
Ecologyalsochangeslower-tailreliability. Gemini’sbottom-rankratefallsfrom22%inSoloto0%inArena,andits
P90normalizedregretfallsfrom0.73to0.27. DeepSeekshowstheoppositetailpattern,withP90regretrisingfrom
0.16 to 0.39. Figure 5 provides a descriptive view of execution-audit intervention burden and terminal valuation:
models with fewer logged interventions tend to achieve higher Arena valuations, yet the six-model relationship
admits substantial variation and is not inferential.
This result gives the paired ecology protocol a deployment-oriented interpretation.Solomeasures whether a model
can independently produce high-quality plans against stable opponents.Arenameasures whether the same model
remains competitive when peer evaluated LLM agents change prices, demand allocation, and market outcomes. A
model with high average valuation but frequent lower-tail collapse may be less reliable than its mean score suggests;
conversely, a model that becomes stable in a shared market may exhibit strengths missed by fixed opponents.
6

ERPBench
SII-GAIR
Figure5: Descriptivereliability–performancepatternsundertheArenaecologyacrosssixmodelfamilies. (a)Logged
execution-intervention burden versus mean terminal valuation; (b) L2 operational reliability score versus mean
terminal valuation. The L2 score is a within-panel normalization of logged operational-intervention rates; these
six-point associations are descriptive, not inferential.
4.7 Difficulty Conditions the Ecology Effect
Difficulty-stratified analysis tests whether the ecology effect is a single global shift or a task-conditioned change.
Figure 6 shows that the pairedArena–Soloeffects vary across difficulty strata. Gemini consistently benefits across
the displayed strata, whereas the other model families show smaller, mixed-direction shifts; uncertainty also varies
with stratum size and operational difficulty.
This heterogeneity is important for benchmark validity. If the result were caused only by a few extreme easy or
hard cases, the benchmark would provide weaker evidence about enterprise-agent reliability. Instead, the stratified
view shows that the direction of the main ecology effect is visible across the problem design, while the scale of the
effect depends on the operational pressure imposed by the task. ERPBench should therefore be read as a structured
problem-family benchmark rather than a single undifferentiated score pool.
Figure 6: Difficulty-stratified paired effects. Ecology effects are heterogeneous across task strata, showing that the
Arenashift is not a uniform offset applied to every problem type. Points show paired mean effects; horizontal lines
show 95% bootstrap confidence intervals; bold intervals exclude zero.
5 Discussion and Limitations
ERPBench shows that single-ecology leaderboards can be incomplete for enterprise agents.Solomeasures
performance against stable rule-based competitors;Arenameasures behavior when other evaluated LLM agents
7

ERPBench
SII-GAIR
also shape prices, demand allocation, inventory, and market outcomes. Neither ecology is universally superior or
uniquely correct. The paired comparison instead tests whether conclusions about a model transfer across explicitly
specified competitive market ecologies.
The empirical pattern suggests two different forms of enterprise-agent competence. DeepSeek appears strongest
as an independent optimizer: it leadsSolo, has very low lower-tail exposure in that setting, and often produces
high-quality decisions against fixed opponents. Gemini appears strongest as a competitive responder: it has higher
tailriskinSolo, butbecomes theclearaggregateleader inArenaand avoids bottom-rankoutcomes. This distinction
would be invisible in a benchmark that reports only one competitive market ecology.
Outcomepanelsandexecution-auditsummariesplaycomplementaryroles. Terminalvaluationandrankestablishthe
benchmark comparison, while aggregate audit summaries characterize parsing recovery, feasibility repair, clamping,
and runtime recovery. Logged interventions should not be overread as causal mechanisms or interchangeable
model-errorunits;theyconstraininterpretationandsupportprocess-levelanalysis. Inparticular,production-capacity
skipscanreflectabindingenvironmentconstraintratherthanamalformeddecision,whereasfallbacksandtracebacks
are stronger evidence of output-pipeline fragility.
The ecology effect also varies by problem: models with near-neutral aggregate changes can improve on some
tasks and worsen on others. It is therefore a problem-dependent interaction, not a constant shift applied to each
model. ERPBenchremainsacontrolledERP-inspiredsimulation,withafixed100-problemslice,six-roundhorizon,
and one six-modelArenacomposition; results may differ under additional ecologies, fixed-opponent sets, longer
horizons, orinformationregimes. Service-sideroutingandmodelendpointsmaychangeovertime, somodel-family
labels do not guarantee immutable or route-identical vendor snapshots across ecologies. The paired results should
therefore be read as benchmark contrasts under the observed service configuration rather than as route-invariant
causal effects. Finally, logged interventions are audit evidence rather than a mechanism model. Future work should
test candidate mechanisms involving price following, capacity, inventory, and market share.
6 Conclusion
ERPBench evaluates enterprise decision agents under paired competitive market ecologies with logged intervention
evidence. Across 100 matched ERP problems, six model families, and 1,200 model-level trajectories, the leading
modelchangesfromDeepSeekinSolotoGeminiinArena;task-levelwinners,difficultyeffects,andtail-riskprofiles
also change. These results suggest that enterprise-agent evaluation should report not only terminal scores, but also
whether model-selection conclusions transfer across competitive market ecologies and how executable decisions are
produced.Additional details, including the problem-set coverage audit, the full confidence-interval table, and the
trace taxonomy, are provided in Appendices A–C.
7 Acknowledgments
We thank Professor Senchun Chai for valuable suggestions on the ERP system and its system-level design. We
thank Professor Qiuju Yin of the School of Management, Beijing Institute of Technology, for supporting system
testing, sharing the SAP competition rules, and providing strategic feedback that helped shape this project. We also
thank the Beijing Institute of Technology students who participated in the SAP ERPSIM competition for their early
testing and practical feedback on ERP-market competition.
References
[1] Norah Alzahrani, Hisham Alyahya, Yazeed Alnumay, Sultan AlRashed, Shaykhah Alsubaie, Yousef Almushayqih, Faisal
Mirza, Nouf Alotaibi, Nora Al-Twairesh, Areeb Alowisheq, M. Saiful Bari, and Haidar Khan. 2024. When benchmarks are
targets: Revealing the sensitivity of large language model leaderboards. InProceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 13787–13805.
[2] Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan. 2025.𝜏2-Bench: Evaluating conversational
agents in a dual-control environment.arXiv preprint arXiv:2506.07982.
[3] Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart,
Nicolas Chapados, Alexandre Lacoste, and Alexandre Drouin. 2024. WorkArena++: Towards compositional planning and
reasoning-based common knowledge work tasks. InAdvances in Neural Information Processing Systems, volume 37.
[4] LeeG.CooperandMasaoNakanishi.1988.Market-ShareAnalysis: EvaluatingCompetitiveMarketingEffectiveness. Kluwer
Academic Publishers, Boston, MA.
8

ERPBench
SII-GAIR
[5] Kung-Hsiang Huang, Akshara Prabhakar, Sidharth Dhawan, Yixin Mao, Huan Wang, Silvio Savarese, Caiming Xiong,
Philippe Laban, and Chien-Sheng Wu. 2025. CRMArena: Understanding the capacity of LLM agents to perform professional
CRM tasks in realistic environments. InProceedings of the 2025 Conference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 3830–3850.
[6] Kung-Hsiang Huang, Akshara Prabhakar, Onkar Thorat, Divyansh Agarwal, Prafulla Kumar Choubey, Yixin Mao, Silvio
Savarese, Caiming Xiong, and Chien-Sheng Wu. 2026. CRMArena-Pro: Holistic assessment of LLM agents across diverse
business scenarios and interactions.Transactions on Machine Learning Research.
[7] Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. 2024.
SWE-bench: Can language models resolve real-world GitHub issues? InProceedings of the Twelfth International Conference
on Learning Representations.
[8] Pierre-Majorique Léger, Timothy Paul Cronan, Patrick Charland, Robert Pellerin, Gilbert Babin, and Jacques Robert. 2011.
Using a simulation game approach to teach enterprise resource planning concepts.Journal of Information Systems Education,
22(3):235–248.
[9] Pierre-Majorique Léger, Jacques Robert, Gilbert Babin, Robert Pellerin, and Beverly Wagner. 2007. ERPsim: A simulation
game for teaching SAP ERP. Technical report, HEC Montréal.
[10] HaohangLi,YupengCao,YangyangYu,ShashidharReddyJavaji,ZhiyangDeng,YueruHe,YuechenJiang,ZiningZhu,K.P.
Subbalakshmi, Jimin Huang, Lingfei Qian, Xueqing Peng, Jordan W. Suchow, and Qianqian Xie. 2025. INVESTORBENCH:
A benchmark for financial decision-making tasks with LLM-based agent. InProceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 2509–2525.
[11] Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin Liao. 2024. EconAgent: Large language model-empowered agents
for simulating macroeconomic activities. InProceedings of the 62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 15523–15536.
[12] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan
Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun,
Minlie Huang, Yuxiao Dong, and Jie Tang. 2024. AgentBench: Evaluating LLMs as agents. InProceedings of the Twelfth
International Conference on Learning Representations.
[13] AnkaReuel,AmeliaHardy,ChandlerSmith,MaxLamparth,MalcolmHardy,andMykelJ.Kochenderfer.2024. BetterBench:
Assessing AI benchmarks, uncovering issues, and establishing best practices. InAdvances in Neural Information Processing
Systems, volume 37.
[14] Tianbao Xie, Danyang Zhang, Yixuan Chen, Shitao Xia, Yifan Liang, Zhuxin Li, Hanchao Zeng, Yiduo Xu, Rui Zhou,
Zhuoyun Geng, et al. 2024. OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments.
InAdvances in Neural Information Processing Systems, volume 37.
[15] Frank F. Xu, Yufan Song, Boxuan Li, Yuxuan Tang, Kritanjali Jain, Mengxue Bao, Zora Z. Wang, Xuhui Zhou, Zhitong
Guo, Murong Cao, Mingyang Yang, Hao Yang Lu, Amaad Martin, Zhe Su, Leander Maben, Raj Mehta, Wayne Chi, Lawrence
Jang, Yiqing Xie, Shuyan Zhou, and Graham Neubig. 2025. TheAgentCompany: Benchmarking LLM agents on consequential
real-world tasks. InAdvances in Neural Information Processing Systems, volume 38.
[16] Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. 2025.𝜏-bench: A benchmark for tool-agent-user
interaction in real-world domains. InProceedings of the Thirteenth International Conference on Learning Representations.
[17] Linghua Zhang, Jun Wang, Jingtong Wu, and Zhisong Zhang. 2026. RetailBench: Evaluating long-horizon autonomous
decision-making and strategy stability of LLM agents in realistic retail environments.arXiv preprint arXiv:2603.16453.
[18] Qinlin Zhao, Jindong Wang, Yixuan Zhang, Yiqiao Jin, Kaijie Zhu, Hao Chen, and Xing Xie. 2024. CompeteAI:
Understanding the competition dynamics of large language model-based agents. InProceedings of the 41st International
Conference on Machine Learning, volume 235 ofProceedings of Machine Learning Research, pages 61092–61107.
[19] Yushuo Zheng, Huiyu Duan, Zicheng Zhang, Yucheng Zhu, Xiongkuo Min, and Guangtao Zhai. 2026. Market-Bench:
Benchmarking large language models on economic and trade competition.arXiv preprint arXiv:2604.05523.
[20] Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk,
Daniel Fried, Uri Alon, and Graham Neubig. 2024. WebArena: A realistic web environment for building autonomous agents. In
Proceedings of the Twelfth International Conference on Learning Representations.
9

ERPBench
SII-GAIR
A Problem Set and Coverage Audit
The 100-problem slice is assembled as a matched benchmark panel rather than as independent ad hoc runs. Each problem
specifiesaseed,difficultystratum,scenariocategory,initialoperationalstate,andmarketparameters. TheSolo100andArena100
panels use the same problem identifiers so that every model–problem pair has a direct ecology comparison. Each ecology
contains 600 terminal outcome records, corresponding to 100 problems times six evaluated model families. Internal consistency
checks found 100/100 problem coverage, zero duplicate model–problem records, and zero missing expected records.
The main paper reports terminal valuations from the sixth-round record. During analysis, ordered per-round records were used
to associate model identity, problem identifier, round number, parsed decisions, feasibility events, and resulting simulation states.
Execution-intervention summaries were computed from logged events where available.
The consistency checks cover problem–model coverage, duplicate pairs, missing expected records, and source-identifier
associations where identifiers are present. Coverage requires each problem to appear for all six models, while duplicate and
missing-record checks enforce exactly 600 terminal outcome records per ecology. These checks support the paired design
without changing the terminal valuation or ranking definitions.
B Metrics and Statistical Protocol
Valuation is reported in millions. Mean rank is computed within each problem and ecology among the six evaluated model
families, with lower rank indicating better terminal valuation. Normalized regret is computed within a problem as the gap to the
best model under the same ecology, scaled by the observed within-problem valuation range. Bottom-rank rate is the fraction of
problems on which a model ranks last among the evaluated families.
Table 2: Paired ecology effects with 95% confidence intervals and Benjamini–Hochberg-adjusted𝑞-values. Values
match Table 1; intervals are percentile-bootstrap confidence intervals over problems.
ModelΔ𝑉(M)95% CI (M)𝑞
DeepSeek−17.58[−29.79,−5.36].0116
Gemini+94.54[+78.74,+110.40]1.28×10 −15
GPT-5.5+8.39[−2.84,+19.54].126
Qwen−18.74[−29.89,−7.56].0061
Doubao+6.90[−4.90,+19.04].557
Claude−2.83[−14.60,+8.42].866
For paired effects, the unit of resampling is the problem, not the individual row. This preserves the matched design because each
resampled problem contributes the correspondingSoloandArenaoutcomes for the same model. Statistical tests use two-sided
Wilcoxon signed-rank tests on paired valuation differences and apply Benjamini–Hochberg correction across the six model-wise
tests. We treat these tests as descriptive evidence for ecology sensitivity rather than as a claim about all possible ERP markets.
The same principle applies to pairwise win rates and winner-disagreement summaries: they are benchmark statistics for this
controlled 100-problem panel, not estimates of universal model superiority. Their role is to show whether the paired protocol
produces stable or unstable conclusions under a defined measurement condition.
C Trace Taxonomy and Audit Scope
Trace interventions are divided into six logged categories.Production-capacity skipdenotes an attempted production item that
could not be scheduled under available machine capacity, lot-size, or material constraints.Investment unavailabledenotes
a requested financial action that was not available in the current state.Fallback decisiondenotes recovery from missing or
malformed model output into a valid default action.Production quantity clampeddenotes a numeric production field adjusted to
an allowed range.Tracebackdenotes runtime recovery captured by the execution log, andexperiment faileddenotes a run-level
execution failure. Figure 3 displays the five most frequent categories; the fiveexperiment failedevents are omitted and excluded
from the displayed-share denominator.
These categories are intentionally not summed into a single “error rate.” They occur at different layers of the pipeline and may
overlap. Capacity skips are often normal consequences of the ERP environment, whereas fallback and traceback events are
closer to interface robustness failures. We therefore use them only as aggregate process diagnostics that qualify, rather than
replace or causally explain, the terminal outcome analysis.
10
