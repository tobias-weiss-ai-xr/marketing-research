---
title: A Multi-Agent Large Language Model Framework for Marketing Decision-Making with Auditable Attribution
  Analysis
url: https://doi.org/10.21203/rs.3.rs-9300129/v1
category: analytics
subcategory: measurement
date: 2026-04
venue: Research Square
authors:
- Qianxi Liu
- Hengguang Cui
- Yingzi Wang
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-9300129/latest.pdf
pages: 10
chars: 33232
fetched_at: '2026-11-08T17:02:51+00:00'
kb_version: 1
---

# A Multi-Agent Large Language Model Framework for Marketing Decision-Making with Auditable Attribution Analysis

A Multi-Agent Large Language Model Framework for
Marketing Decision-Making with Auditable
Attribution Analysis
Qianxi Liu 
University of South Florida
Hengguang Cui 
Brown University
Yingzi Wang 
University of Minnesota, Twin Cities
Chi Shing Lee 
Hunter College
Sheng Chen 
Northeastern University
Linghao Yang 
University of Chicago
Research Article
Keywords: Alignment of standards, auditable chain of evidence, budget constraint optimization, multi-
agent orchestration
Posted Date: April 3rd, 2026
DOI: https://doi.org/10.21203/rs.3.rs-9300129/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: The authors declare no competing interests.

AMulti-AgentLargeLanguageModel
FrameworkforMarketingDecision-Making
withAuditableAttributionAnalysis
ChiShingLee
HunterCollege
NewYork,USA
Abstract-This paper addresses the challenges of inconsistent indicator defini tions, complex attribution paths,
and difficulty in tracing decision-making criteria in multi-channel marke ting environments. It proposes a multi-
agent large-scale model framework for marketing decision-making, constructing an en d-to-end analysis loop
around problem parsing, definition alignment, and auditable output. The system con sists of a problem agent, an
Metric Agent, and a decision agent: the problem agent maps natural language require ments into structured task
specifications, clarifying target indicators, time windows, analysis dimen sions, and constraint sets; the Metric Agent
performs field mapping and indicator standardization on multi-source event data, uni fying window filtering,
deduplication rules, and cross-platform merging strategies, and providing validi ty judgments and consistent
aggregation criteria for fine-grained slices; the decision agent generates exec utable resource allocation suggestions
under budget and business constraints, and simultaneously outputs a recalc ulated evidence chain, ensuring the
traceability of suggestion sources, calculation paths, and definition version s. Comparative experimental results show
that the proposed method maintains strong robustness and reliable delivery c apabilities under a multi-dimensional
evaluation system, particularly excelling in constraint satisfaction, v erifiable output, and auditable coverage. It
provides an interpretable, traceable, and implementable decision support soluti on for marketing attribution
assessment and ROI optimization.
CCS CONCEPTS: Computing methodologies~Machine learning~Machine learning ap proaches
Keywords: Alignment of standards, auditable chain of evidence, budget constraint optimization, multi-agent
orchestration
I.INTRODUCTION
As digital marketing fully embraces data-driven approaches, businesses have accumulated massive
amounts of multi-source data in campaign management, growth operations, and user outreach, including
advertisingplatformlogs,on-siteandoff-sitebehaviora ltracking,customerrelationshipdata,andtransaction
data. The increasing complexity of marketing technology systems makes the decision-making chain, from
strategyformulationtoexecutionfeedback,highlydepend entonindicatorsystemsanddatainterpretation[1].
However, in real-world business environments, the increased number of channel touchpoints, longer paths,
and more dispersed conversions mean that the same result is often the result of multiple factors working
together. Traditional analysis methods, primarily based on rules and static reports, struggle to quickly
identify key drivers and provide consistent and reliable decision support in a rapidly changing market
environment[2].
In this context, ROI evaluation and attribution analysis have become core links connecting marketing
investment and business results. ROI answers whether the campaign was worthwhile, while attribution
answers who contributed the value; both jointly determine the direction of budget allocation, frequency
control strategies, creative iteration, and audience operations[3]. However, in reality, inconsistencies in
Qianxi Liu
University of South Florida
Tampa, USA
Hengguang Cui
Brown University
Providence, USA
Yingzi Wang
University of Minnesota, Twin
Cities
Minneapolis, USA
Linghao Y ang*
University of Chicago
Chicago, USA
Sheng Chen
Northeastern University
Seattle, USA

indicator definitions, differences in attribution windows, limitations in cross-platform identification, data
gaps, and abnormal biases are common problems, easily leading to inconsistent or even contradictory
conclusions, further amplifying decision-making risks. Especially when managers need to make budget
adjustments within a limited timeframe, the lack of verifiable evidence chains and clear assumption
boundaries often leads to decisions relying solely on experience or localized indicators, hindering the
developmentofreusable,systematiccapabilities[4].
In recent years, large language models have demonstrated potential in understanding complex problems,
organizing reasoning processes, and utilizing external tools, providing a new technological path for building
intelligent analysis systems for marketing decisions. Introducing large language models into marketing
analysis does not mean replacing statistical and causal methods with generative models, but rather allowing
the model to handle high-frequency and error-prone aspectssuch as task planning, calibrated reporting,
evidence retrieval, result interpretation, and risk warnings, thereby integrating information scattered across
multiple platforms and reports into structured decision-making support[5]. Furthermore, the multi-agent
framework can break down different capabilities into relatively independent yet collaborative modules,
enhancingthesystem'sscalabilityandmaintainabilitywh enfacingcomplexbusinessproblems.
Therefore, constructing a multi-agent large model framework for marketing decision-making and
conducting auditable attribution analysis is of great significance[6]. On the one hand, it helps standardize
problem-driven analysis processes, translating businesslanguage into actionable metrics and data tasks,
reducing ambiguity and communication costs, and improvinganalytical efficiency and consistency[7]. On
the other hand, by introducing an auditable mechanism, the system can provide data sources, calculation
paths, key assumptions, and uncertainty boundaries along with the output conclusions, enhancing the
credibilityandtraceabilityoftheconclusions,therebyp rovidingmorerobustsupportforbudgetoptimization
and strategy iteration. This approach not only improves enterprise marketing efficiency and resource
allocation quality but also provides a methodological foundation for exploring the reliable application of
large-scalemodelsinhigh-riskdecision-makingscenario s.
II.DATASETINTRODUCTION ANDANALYSIS
This paper selects the Criteo Attribution Modeling for Bidding Dataset as the research dataset. This
datasetisderivedfromanonymizedsamplingrecordsofreal displayadtraffic,covering30consecutivedays
of online campaign logs, sorted by timestamp, with data granularity at the single-display event level. Each
record includes a user identifier, an activity identifier,a display timestamp, whether a click occurred,
whether a conversion occurred within 30 days of the display,conversion timestamp, and conversion
identifier, and additionally provides a marker indicatingwhether the conversion was attributed by the
platform, thus supporting attribution modeling and verifiableanalysis of multi-touchpoint links. This dataset
is large, containing approximately 16.5 million impressions and approximately 45,000 conversions, and
provides9contextualcategoricalfeaturestocharacteriz ethecampaignenvironmentandreachconditions.
To support ROI-related decision analysis, this dataset also provides cost and value-related fields,
including display cost and the corresponding value signal when an attributed conversion occurs. Although
the values have been transformed, they can still be used for relative comparison, trend diagnosis, and
strategy evaluation. Atthelicensing level, thedataset isreleased underCreative Commons AttributionNon-
Commercial ShareAlike 4.0, suitable for open-source use and reproduction for research purposes. Based on
its structure, which simultaneously includes touchpoint sequences, conversion markers, attribution markers,
and cost-value signals, this dataset naturally aligns withthe multi-agent decision analysis framework
proposed in this paper, facilitating an end-to-end process from problem analysis, caliber alignment,
attribution, andcausalinference totheoutputofanaudita blechain ofevidence.Thestatistical analysisofits
datasetisshowninFigure1.
As can be seen from the figures, this dataset exhibits a typical long-tail structure and significant
heterogeneity in marketing campaigns: total spending is highly concentrated on a few top campaigns, while
the contributions of other campaigns are relatively dispersed, indicating that budget allocation has a clear
focus on key targets; the daily ROI and spending synchronization curves show strong intraday fluctuations
andperiodicupsanddowns,reflectingthatthecampaignper formanceissignificantlyaffectedbytime-series
factors and traffic competition, and that single-point indicators are easily disturbed by noise; the CPC violin
distributions of different channels differ significantly, with top channels having higher overall costs and
greater variance, indicating that differences in bidding environment and audience quality can lead to cost
instability; at the same time, the conversion rate heatmapsplotted by week and hour show several high-
response and low-response periods in a block structure, suggesting that conversions do not occur uniformly

but have obvious time-series patterns. These phenomena together provide an intuitive and auditable data
basisforsubsequentalignment,attributioninference,an dbudgetperiodoptimization.
Figure1.DatasetStatisticalAnalysis
III.PROBLEMAGENT
Intheanalyticsprocessgearedtowardsmarketingdecision s,thecoreroleoftheProblemAgentistomap
the decision problems posed by business stakeholders in natural language into actionable analytical tasks,
and to explicitly provide an auditable set of constraints and data dependencies. Let the user-input decision
problem be q. The Problem Agent parses the problem to obtain a structuredtask representation s, which
includes elements such as target metrics, time windows, segmentation dimensions, and constraints, and can
beformallywrittenas:
s=Φ(q)=<m,T,D,C> (1)
Here, m represents the target metric,T represents the analysis time range,D represents the business
dimensions to be expanded, andC represents the constraint set, thus ensuring that subsequent analysis can
correspondone-to-onewiththedatasetfieldsandhasrepro ducibility.
To ensure task executability and result reliability, the Problem Agent further transforms the structured
task sintoaset ofverifiable queriesandaggregationoperatorse quences π, andperforms consistencychecks
on data availability and caliber constraints during the generation process. Given a data tableX, this process
canberepresentedas:
π=Ψ(s,X), y=A(X;π) (2)
Here, A(∙) represents the executor, which consists of SQL aggregationor equivalent data processing
operators, and y is the analysis output (ROI curve by date). This mapping fromproblem to operator chain
allowseach step tobe recorded andreplayed, ensuringthat during auditing, thespecific fieldsused,filtering
conditions,andaggregationcriteriacanbetraced.
In decision-oriented scenarios, the Problem Agent also needs to define the analysis objective as an
optimizable utility function and encode business constraints as checkable conditions so that the Decision
Agent can provide budget recommendations and risk warningsunder the same caliber. Combining common
return on investmentobjectives, the Problem Agent definesROI as theratio ofvalue to costand declaresits
statisticalgranularityandaggregationrangeinthetask:

ROI(T,D)=
i∈Ω(T,D) revenuei
i∈Ω(T,D) spendi+ε (3)
WhereΩ(T,D) representsthesample set aftersatisfying thetime window and dimension slicing,andε is
a stable term to prevent the denominator from being zero. By explicitly writing the definition of the target
indicator and the slice set into the task representation, the Problem Agent can trigger constraint correction
and task reduction in advance when the data is sparse, the dimension expansion is too fine, or the field is
missing, thereby laying a unified and reusable task foundation for subsequent caliber alignment and
auditableattributionanalysis.
IV.METRICAGENT
TheMetricAgent'sresponsibilityistoalignthetargetmet ricswiththedatatablefieldsone-to-one,based
on the structured tasks=<m,T,D,C> given by the Problem Agent, and output an executable and auditable
unified measurement metric. Given a dataset setΩ(T,D), the Metric Agent first constructs standardized
metric mappingsM from theoriginal fields, for example,mapping fieldssuch asspend, revenue,clicks, and
conversionstometricfunctions,andwritestheresultsint oreusablemetricdefinitionobjects.
M(m)=(numm(Ω),denm(Ω),gm) (4)
Here, numm and denm representtheaggregationoperatorsofthenumeratorandde nominator,respectively,
and gm represents the grouping dimension. This mapping ensures that the same indicator maintains
consistent computational semantics across different slices, avoiding caliber drift caused by changes in field
naming or aggregation granularity, and providing a standard interface for subsequent evidence chain
recording.
In attribution and delivery analysis scenarios, the MetricAgent needs to further handle constraints such
as windowing, deduplication, and cross-platform merging to ensure the comparability and interpretability of
metrics within a given timeframe. Taking conversions as an example, each impression in the dataset may
correspond to a conversion tag or conversion time information. The Metric Agent uses constraintC to
perform windowing and deduplication on the conversion set,forming an auditable and valid conversion set
ΩΔ.
ΩΔ={i∈Ω(T,D)|0≤ti conv-ti imp≤Δ} (5)
Here, ti impand ti conv representexposureandconversiontime,respectively,and Tistheattributionwindow.
This step makes the differences in attribution windows commonly seen in business explicit, making the
statisticalscopeofindicatorssuchasCVRandROIclearand traceable.Italsofacilitatesthedegradationtoa
more robust statistical caliber through constraints when privacy is restricted or cross-platform identification
isincomplete.
Toimprovethereliabilityof conclusionsand reduce mislea ding decisions,theMetricAgentalso outputs
uncertainty and data quality signals for key metrics. This is especially important when analyzing data at
finer-grained dimensions such as campaign or hour, where insufficient sample size and excessive variance
can significantly impact ROI interpretation. Therefore, the Metric Agent calculates basic metrics and their
stability estimates for each group A, and only marks them as valid measures for decision-making when the
minimumsamplesizeconstraintismet.
CVR g= i∈Ωi conversionsi
i∈Ωi impressionsi , Valid(g)=1[|Ωg|≥nmin] (6)
Where Ωg is the sample set under groupg, andnmin is the minimum sample threshold given byC. By
unifying caliber alignment, window constraints, and validity judgment to the same metric layer, the Metric
Agent can provide the Decision Agent with consistent, traceable, and stable metric inputs, thereby
supporting an auditable decision analysis closed loop oriented towards ROI and attribution. Finally, this
paperpresentstheMetricAgentalgorithmflow,asshowninF igure2.

Figure2.MetricAgentAlgorithmFlow
V.DECISIONAGENT
The Decision Agentreceives auditablemetric packages fromtheMetric Agentas input,and completes a
closed-loop generation process from diagnosis to action recommendations under a unified standard. Let
z={zg} be the effective metric output by the Metric Agent on time window T and dimension setD, where
each group g corresponds to spend, revenue, clicks, conversions, and stability flags under slices such as
channel, campaign, device, and hour. The Decision Agent first explicitly expresses business objectives as
utility functions and incorporates constraints such as budget, minimum deployment volume, and risk
thresholds into the same decision space, thereby ensuring that recommendations improve ROI without over-
adjustingindata-sparseorhighlyvolatileunits.
At the execution level, the Decision Agent uses the grouped budget vector b={bg} as the decision
variable to rank and allocate candidate slice units, maximizing overall revenue while satisfying audit
constraints.Asimplifiedandeasilyauditableoptimizati onformcanbewrittenas:
b*=argmax
b∈B g bg∙rg s.t. g bg≤B (7)
Where B represents the total budget ceiling,rgis the estimated grouped marginal return derived from
metricpackage z, whichcan beobtained by combininghistoricalROI,CVR,and conversionvalue, etc.,and
rg representsthesetofbusinessconstraints,suchaschannel shareceilings,minimumexposurerequirements,
or no reduction in investment for specific campaigns. Sinceboth the goal and constraints can be directly
obtained by aggregating fields such as spend and revenue, each budget recommendation from the Decision
Agentcanbeverifiedthroughrecalculationusingthesamed atacaliber,meetingauditabilityrequirements.
To avoid generating aggressive recommendations on slices with high noise or insufficient samples, the
Decision Agent also performs risk calibration on the recommendations based on the validity label and
uncertainty signal of the Metric Agent, and outputs rollback-capable action boundaries. Letug represent the
uncertainty or risk score of groupg, which can be obtained by combining sample size, ROI variance, or
transformationsparsity.Then,therecommendedbudgetadj ustment∆bg adoptsarisk-gatedform:
Δbg=η∙Score(zg)∙1[Valid(g)=1]∙1[ug≤τ] (8)
Where η represents the adjustment step size,Score(zg) can be composed of unit consumption revenue,
conversion efficiency, and cost indicators, and τ represents the risk threshold. Through this gating
mechanism,theDecisionAgentonly providessuggestionsfo r increasingordecreasinginvestmentingroups
withconsistentcriteriaandstablestatistics,andsimult aneouslyincludesthecorrespondingindicatorsources,

window settings, and group segment information in the output, thereby forming a consistent closed loop of
actionablesuggestionsandauditableevidencechainsform arketingdecisions.
VI.EXPERIMENTALRESULTS ANDANALYSIS
A. Experimental setup
This study completed training andevaluation inasingle-machine, multi-GPU environment.An NVIDIA
RTX 4090 24GB GPU was used for accelerated computation, witha 16-core or higher x86 processor and
64GB of memory. Data and logs were stored on an NVMe SSD to reduce I/O bottlenecks. The software
environmentconsistedofUbuntu22.04,Python3.10,andthe deeplearningframeworkPyTorch2.1withthe
corresponding CUDA 12.x driver. NumPy, Pandas, and Scikit-learn were used for data processing and
statistical analysis, and Matplotlib was used for result vi sualization. To ensure reproducibility, all
experiments were run repeatedly with a fixed random seed andthe same data partitioning and metric
configuration. Complete configuration files, runtime logs, and audit trail information were recorded during
the training process.Regarding hyperparameters, event-level delivery logs are divided into training,
validation,andtestsets accordingtotime windows,using d ata fromthepast30 daysby default.The first24
days are used for training, the last 3 days for validation, and the last 3 days for testing to avoid information
leakagecaused bytimetravel.Onthemodelside,amulti-age ntframeworkbasedonalarge language model
isadopted. Inferenceusesatemperatureof0.2,topp of0.9, andamaximumgenerationlengthof512. Strict
mode is enabled for tool calls to constrain the output format. The metric and caliber alignment module is
configuredwithanattribution windowof30days,deduplica tiongranularityattheuserandconversionevent
level, and a minimum sample size threshold of 500 to filter sparse groups. The decision-making module has
a budget adjustment step size of 0.05, a risk threshold of 0.7, and upper and lower limits for single
adjustmentstoavoidexcessivefluctuations.Theoptimize rusedwasAdamW,withalearningrateof0.0002,
weight decay of 0.01, batch size of 2048, and 20 training epochs. A cosine annealing learning rate
scheduling and a 5-epoch warm-up strategy were adopted, with a gradient pruning threshold of 1.0. Mixed
precisiontrainingwasenabledtoimprovethroughputandre duceGPUmemoryusage.
B. Experimental Results and Analysis
To evaluate the effectiveness and auditability of the proposed method in marketing decision-making
scenarios, this paper constructs a comparative evaluationsystem from dimensions such as return on
investment improvement, incremental consistency, robust ness of definitions, uncertainty calibration,
decision stability, constraint satisfaction, and audit coverage. The system is then compared with several
related methods under a unified data partitioning and indicator definition configuration. The experimental
resultsareshowninTable1.
Table1.Experimentalresultscomparedwithothermodels
Method ROI Lift Reven ue Lift Increme ntality Error Attribu tion Consist ency Calibra tion Error Decisio n Stabilit y Constrain t Violation Rate Audit Trace Coverage
Filippouet
al.[8]
0.794 0.796 0.747 0.935 0.893 0.882 0.961 0.786
Zhanget
al.[9]
0.874 0.755 0.755 0.812 0.744 0.785 0.873 0.878
Jianget
al.[10]
0.894 0.963 0.858 0.974 0.786 0.977 0.973 0.931
Yuet
al.[11]
0.861 0.786 0.911 0.794 0.812 0.732 0.946 0.963
Rasheedet
al.[12]
0.941 0.961 0.926 0.754 0.761 0.706 0.777 0.749
Lietal.[13] 0.724 0.717 0.904 0.826 0.815 0.854 0.959 0.772
Wanget
al.[14]
0.952 0.842 0.938 0.761 0.828 0.831 0.853 0.950
Ours 0.881 0.738 0.842 0.751 0.928 0.751 0.952 0.867

Different methods emphasize various dimensions, leading to trade-offs. For robustness indicators like
attribution consistency and decision stability, some methods perform better, suggesting output consistency
underperturbationsandtemporalfluctuations.However,t heircalibrationandauditcoveragemaynotalways
be simultaneously dominant. On the other hand, methods that excel in return-on-investment metrics
demonstrate stronger revenue-driven capabilities but aremore prone to data bias and window settings in
terms of incremental error and consistency. It ’ s evident that a single indicator is insufficient to
comprehensively characterize system quality, especiallyin marketing decision-making scenarios. Revenue
improvement should be accompanied by causal consistency and controllable constraints. Otherwise, while
the conclusion may appear more positive, it could lead to strategy rollback and risk contagion in actual
deployment. From the performance structure of the methods presented in this paper, their advantages are
more concentrated in calibration and constraint satisfaction, as well as the completeness of the audit chain.
This aligns with the previously emphasized goals of caliberalignment and auditable output, demonstrating
that the multi-agent collaborative indicator standardization and validity filtering mechanisms can indeed
reducetheaccumulationofbiasescausedbydatasparsityan ddifferencesinfieldcalibers.Atthesametime,
it is not leading in all aspects of production improvement and consistency-related indicators. Instead, it
seems to be taking a more conservative approach between robustness and action boundaries. This approach
is reasonable for MarTech scenarios that require a traceable decision-making basis, because it prioritizes
ensuring that the recommendations can be recalculated and explained and avoids excessive adjustments on
sliceswithhighuncertainty,therebymakingsubsequentst rategyiterationsandriskcontrolmorecontrollable.
The attribution window determines the time frame within which conversion signals are included in the
evaluation,directlyimpactingthestatisticalscopeandc omparabilityofproductionefficiencyimprovements.
Different window lengths alter the coverage and noise levels of long-tail conversions, thus affecting the
stability and interpretability of the ROI Lift. To test the robustness of our proposed method under varying
scopes, this section examines the sensitivity of the ROI Lift to changes in attribution window length. The
experimentalresultsareshowninFigure3.
Figure3.AttributionwindowlengthonROILiftsensitivity experiment
The curve shows that changes in the attribution window length significantly alter the trend of ROI Lift,
exhibiting a non-monotonic characteristic of initially increasing, then decreasing, and accompanied by local
reboundsasthewindowlengthens.Shorterwindowstendtoca ptureimmediateconversionsmoreaccurately,
resulting in a cleaner statistical caliber but potentiallyunderestimating the contribution of latency. As the
window gradually lengthens, more long-tail conversions are included, leading to an increase in ROI.
However, when the window is too long, the additional signalsmay contain more noise and historical
interferencethatareweaklycorrelatedwiththecurrentca mpaign,thusloweringthenetincrease.Theshaded
areainthegraphalsoindicatesthatthefluctuationamplit udevariesunderdifferentwindows,suggestingthat
windowsettingsnotonlyaffectthemeanlevelbutalsoalter thestabilityoftheestimate.
Combined with the previous observations of the dataset statistics, conversions are not uniformly
distributedovertimeandtimeperiods,andthecostdistrib utionacrossdifferentchannelsdifferssignificantly.
Therefore, window sensitivity essentially reflects the projection of the latency structure and cost recovery
rhythm of different touchpoint links onto the statistical caliber. The curve is relatively balanced around its
medium length, covering major delayed conversions withoutintroducing too many weakly correlated
samples, thus making it easier to generate interpretable ROI gains. Local upward spikes in the curve may
correspond to better alignment with the typical payback periods of certain channels or demographics,
allowing for more comprehensive accounting of value contributions. Overall, this experiment demonstrates
the necessity of explicitly declaring attribution windowsand conducting sensitivity verification within an

auditable framework, as it directly impacts the comparability and decision confidence of ROI lifts, and
providesamorerobustbasisforsubsequentbudgetadjustme nts.
VII.CONCLUSION
This paper proposes an end-to-end decision analysis process based on a multi-agent large-scale model
framework for marketing decision-making. This process uses problem-driven approaches as the entry point,
caliber alignment as the core, and auditable output as a constraint. By structuring decision problems into
executable tasks and completing attribution and return-to-production assessments under unified indicator
definitions, window constraints, and validity judgments, the system integrates information previously
scattered across multiple data sources and reports into a recalcifiable, traceable, and interpretable decision-
making basis. Overall, this framework emphasizes ensuringconsistency of caliber and completeness of
evidence in real-world business environments before outputting actionable recommendations. This reduces
therisk of misjudgmentscaused by indicator drift,data gaps,and noiseinterference, enhancing thecertainty
andcontrollabilityofmarketinganalysisinmovingfromre portinterpretationtoactionabledecision-making.
In comparative evaluations, the proposed method demonstrates strong stability and reliable output
capabilities. Its advantages are not only reflected in return-to-production performance but also in reliability
indicators for decision-making, including the degree of constraint satisfaction, risk mitigation capabilities,
and the completeness of audit coverage. This means that when providing budget and strategy
recommendations, the system can simultaneously offer clear supporting evidence and traceable calculation
methods. This allows the business side to move beyond relying solely on black-box conclusions or single
reports, enabling them to recalculate, verify, and define responsibilities for the recommendations. For
marketing organizations requiring cross-team collaboration, this auditable mechanism helps establish a
unified language and consistent standards, reducing the cost of repeated alignment, improving decision-
making efficiency, and accumulating reusable knowledge and process assets during campaign strategy
iterations.
From an application impact perspective, this work providesa path for intelligent upgrades in the
MarTech field that balances usability and credibility. Itsvalue extends beyond ad attribution and ROI
optimization, reaching into scenarios such as growth operations, user lifecycle management, channel mix
planning, and budget governance. It is particularly suitable for enterprise environments with multiple
channels, multiple platforms, multiple metrics, and frequently changing standards. By making the analysis
process explicit, encoding definitions and constraints into the system, and delivering conclusions as a chain
of evidence, this framework helps organizations establishhigher standards of data governance and decision
governance capabilities. It drives the transition of marketing campaigns from experience-driven to a
verifiable, traceable, and replicable strategy engineering system, while also providing a referable paradigm
fortheimplementationoflarge-scalemodelsinhigh-riskb usinessdecision-makingscenarios.
Looking to the future, several directions warrant further exploration. First, further strengthening the
system's robustness under privacy constraints and data fra gmentation, enhancing reliable reasoning
capabilities when cross-platform identification is limited, attribution signals are sparse, or data latency is
greater. Second, introducing a more robust closed-loop mechanism to ensure continuous iteration between
decisionrecommendationsandsubsequentactualimplement ationfeedback,therebyautomaticallycorrecting
discrepancies indefinitions and strategy biasesover long-termoperation. Third, expanding auditcapabilities
from resulttracing toprocess governance, providing more granular risk descriptionsand liability boundaries
when outputting recommendations, enhancing controllability, and compliance. Overall, as the scale of
marketing data, channel complexity, and compliance requirements continue to increase, the multi-agent big
data model frameworkfor marketing decision-making is expected toplay arole in awider range ofindustry
scenarios, enabling enterprises to achieve higher-quality resource allocation, a more transparent decision-
makingbasis,andmorestablebusinessgrowth.
REFERENCES
[1] Gordon B R, Moakler R, Zettelmeyer F. Close enough? A large-scale exploration of non-experimental approaches
toadvertisingmeasurement[J].MarketingScience,2023,42(4):768-793.
[2] Yao D, Gong C, Zhang L, et al. Causalmta: Eliminating the user confounding bias for causal multi-touch
attribution[C]//Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and DataMining.
2022:4342-4352.
[3] Shender D, Amini A N, Bao X, et al. A time to event framework for multi-touch attribution[J]. arXiv preprint
arXiv:2009.08432,2020.
[4] ZhangY,Ben-HarushO,ZhuS,etal.Neuralodeformulti-channelattribution[J].2024.

[5] Gong C, Yao D, Zhang L, et al. Causalmmm: Learning causal structure for marketing mix
modeling[C]//Proceedings of the 17th ACM International Conference on Web Search and Data Mining. 2024:
238-246.
[6] Yan Z, Wang S, Zhou G, et al. An end-to-end framework for marketing effectiveness optimization under budget
constraint[J].arXivpreprintarXiv:2302.04477,2023.
[7] Goldenberg D, Proença H M, Livne A, et al. Converted Data is All You Need for Causal Optimization of e-
Commerce Promotions[C]//Proceedings of the 34th ACM International Conference on Information and
KnowledgeManagement.2025:5666-5673.
[8] Filippou G, Quach B M, Lenghel D, et al. Causal-driven attribution (CDA): Estimating channel influence without
user-leveldata[J].arXivpreprintarXiv:2512.21211,2025.
[9] ZhangR,ElhamodM.Data-to-Dashboard:Multi-AgentLLMFramework forInsightful Visualiz ationinEnterprise
Analytics[J].arXivpreprintarXiv:2505.23695,2025.
[10]Jiang J, Xie H, Shen S, et al. Siriusbi: A comprehensive llm-powered solution for data analytics in business
intelligence[J].ProceedingsoftheVLDBEndowment,2025,18(12):4860-4873.
[11]Yu H Q, Sutton J, O'Neill S, et al. Case Studies on LLM Centric and Services Oriented Data Analytics Agent
Development[C]//Proceedings of the 2024 13th International Conference on Software and Information
Engineering.2024:69-76.
[12]Rasheed Z, Waseem M, Ahmad A, et al. Can large language models serve as data analysts? a multi-agent assisted
approachforqualitativedataanalysis[J].arXivpreprintarXiv:2402.01386,2024.
[13]Li Y, Sun L, Zhang Y. MetaAgents: Large Language Model Based Agents for Decision-Making on Teaming[J].
ProceedingsoftheACMonHuman-ComputerInteraction,2025,9(2):1-27.
[14]Wang L, Zhang J, Yang H, et al. User behavior simulation with large language model-based agents[J]. ACM
TransactionsonInformationSystems,2025,43(2):1-37.
