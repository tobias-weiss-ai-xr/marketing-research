---
title: Self-Evolving Multi-Agent Symbolic Discovery for Financial Fundamental Analysis
url: https://arxiv.org/abs/2609.32746
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Kelvin J. L. Koa
- Filip Orestav
- Shengqiong Wu
- Michael J. Wooldridge
- Ke-Wei Huang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.32746
pages: 22
chars: 78531
fetched_at: '2026-11-08T13:22:09+00:00'
kb_version: 1
---

# Self-Evolving Multi-Agent Symbolic Discovery for Financial Fundamental Analysis

Self-EvolvingMulti-AgentSymbolicDiscoveryforFinancialFundamentalAnalysis
Kelvin J.L. Koa1, 2∗, Filip Orestav3, Shengqiong Wu4∗, Michael J. Wooldridge4, Ke-Wei Huang1, 2
1National University of Singapore 2Asian Institute of Digital Finance
3KTH Royal Institute of Technology 4University of Oxford
kelvin.koa@u.nus.edu, orestavfilip@gmail.com, shengqionggwu@gmail.com
michael.wooldridge@cs.ox.ac.uk, dishkw@nus.edu.sg
Abstract
While symbolic regression (SR) has been successfully used
in science to discover new equations, its use in financial val-
uation is hindered by several limitations. Whereas the natural
sciences provide objectively correct relationships, financial
valuation constitutes a distinct class of symbolic discovery
problems, as it admits multiple valid perspectives, operates
under non-stationary market conditions, and involves noisy,
continuous performance signals. In this work, we propose
Multi-AgentFundamentalAnalysis withSymbolicAdaptive
learning (mufasa), a hierarchical multi-agent framework for
symbolic discovery in finance.mufasaintroduces (1) disen-
tangled equation discovery via specialized agents represent-
ingdistinctvaluationperspectives,(2)ameta-coordinatorthat
performs hierarchical-level reasoning over market context in-
formation, and (3) a memory mechanism that reasons over
statistical performance summaries (e.g.,accuracy, stability,
and tail risk) to guide learning under noisy feedback. Ex-
periments across datasets from multiple countries show that
mufasaachieves state-of-the-art performance on the valu-
ation task compared to classical finance methods, financial
large language models, and SR approaches, while simultane-
ouslyproducinginterpretableequations,whichwesharewith
the community. We also make publicly available the distilled
learnings across evolution iterations and context-dependent
strategy weights, which might offer useful insights for future
research on financial fundamental analysis.
Introduction
Fundamental analysis (FA) aims to estimate the intrinsic
value of a company using accounting information such as
earnings,cashflows,andassets,andplaysacentralroleinin-
vestment decision-making (Bauman 1996). A long-standing
goal in this domain is to derive interpretable relationships
(expressedasvaluationformulas)thatconnectfinancialvari-
ables to future returns, which provides actionable insights
for decision-making (Shmueli 2010). However, constructing
such relationships remains a largely manual and iterative
process, often relying on domain expertise to propose, test,
and refine hypotheses. Symbolic regression (SR) offers a
promising direction for automating this process by discov-
ering mathematical expressions directly from data (Cran-
mer2023).Recentadvancesfurtherintegratelargelanguage
∗Corresponding authors.
models(LLMs)intoSRpipelines,enablingmoreefficienthy-
pothesis generation and search by leveraging learned priors
(Grayelietal.2024;Shojaeeetal.2025;Savelievetal.2026).
Thesemethodshavebeenparticularlysuccessfulinscientific
domains (Romera-Paredes et al. 2024; Novikov et al. 2025;
Xie et al. 2026), where the objective is to recover a single,
stable governing equation from data.
However, unlike the natural sciences,financial valuation
constitutes a fundamentally different class of symbolic
discoveryproblems,forwhichexistingSRformulationsare
structurally misaligned. Specifically, symbolic discovery in
the financial domain exhibits three defining characteristics:
•Multiple valid perspectives.Unlike physical systems,
financial valuation does not admit a single ground-truth
equation.Differentvaluationphilosophies(e.g.,earnings-
based (Buffett and Cunningham 2001), cash flow-based
(Damodaran 2012), growth-based (Asness, Liew, and
Stevens 1997)) can simultaneously provide equally valid
but distinct explanations of asset prices. Current agent-
based SR methods (Shojaee et al. 2025; Romera-Paredes
et al. 2024) that search for a single equation may largely
limit expressiveness and display reduced generalizability
across different market conditions.
•Non-stationary environments.The relationship be-
tweenfinancialsignalsandoutcomesvariesacrossmarket
conditions,suchasmarketregimesandcompanysectors.
Because of this, the same actions could lead to different
results across learning iterations. The reward pipeline is
confounded by the unstable environment, making it diffi-
cult to reliably transfer or reuse past experience.
•Noisy, continuous feedback.Candidate expressions are
evaluatedthroughnoisyandcontinuousperformancesig-
nalsratherthanbinarycorrectnesssignals.Currentagent
memory systems (Ouyang et al. 2026; Zhang et al. 2026;
Allard et al. 2026; Xiong et al. 2026) that distill lessons
from binary success and failure signals may misattribute
success to spurious patterns arising from noise or distill
learnings that are not robust across the noisy dataset.
Importantly,thesechallengesalsocompoundacrossstages
of the agent self-evolving loop (see Figure 1), making the
overall symbolic FA progressively harder as a whole.
To address these challenges, we proposeMulti-Agent
FundamentalAnalysis withSymbolicAdaptive learning
arXiv:2609.32746v1  [cs.MA]  26 Sep 2026

Noisy & Continuous Feedback
Evaluation signals are not binary success/ failure;
they contain spurious signals.
3
Non-Stationary Environment
Same actions leads to different outcomes; past
experience does not generalize.
2
AgentAction (New equation) Environment
Bull
Market
Bear
Market
Learnings
Growth
perspective
Earnings
perspective
Cash Flow
perspective
…
Multiple Valid Perspectives
There is no single discovered ground-truth
equation for the financial valuation task.
✕
1
✕ ✕
Outcome Outcome
Feedback (noisy signal)
Score
?
Self-Evolving Loop
Figure 1: Overview of the challenges in financial SR across different levels of the self-evolving loop.
(mufasa),ahierarchicalmulti-agentframeworkforsymbolic
discovery in finance. First, instead of searching for a single
universalequation,mufasaperformsdisentangled symbolic
discovery via a set of specialized agents, each operating un-
deradistinctvaluationperspective(e.g.,cashflow,earnings,
etc.)Thisdesignencouragesdiversityinthediscoveredsym-
bolic relationships while maintaining interpretability within
eachperspective.Second,toaccountfornon-stationarymar-
ket conditions, we perform hierarchical-levelreasoning by
introducingameta-coordinatoragentthatconditionsoncon-
textual information (e.g.,sectors, regimes) to dynamically
weightheoutputsofspecialistagents.Thisenablesanadap-
tive combination of perspective-specific knowledge across
varying environments. Third, to cope with noisy and con-
tinuous feedback, each agent maintains a structured mem-
oryofpreviouslyexploredequationsandsummariesoftheir
statistical performance. By reasoning over signals such as
accuracy, stability, tail risk,etc., agents can identify robust
candidates and refine their search strategies despite noisy
supervision from individual observations.
To demonstrate the effectiveness ofmufasa, we perform
extensiveexperimentsacrosscompaniesfrommultiplecoun-
tries (e.g.,US, UK, China), using their fundamental infor-
mationobtainedfromBloomberg.Ourmodelachievesstate-
of-the-artvalueforecastingperformancecomparedtoclassic
financial valuation methods,financial LLMs, andsymbolic
regressionmethods,whilealsoproducinginterpretableequa-
tions, which we share with the research community. In ad-
dition, we also make publicly available the distilled lessons
across evolution iterations and the importance weights of
each valuation method across regimes and sectors, which
contain insights that could be useful for financial practition-
ers. In summary, our contributions in this work are:
•We identify financial valuation as a distinct class of
symbolic regression problems, characterized by multi-
perspective validity, non-stationary environments, and
noisy, continuous feedback.
•We introducemufasa, a hierarchical framework that de-
composes symbolic discovery across specialized agents,
performs hierarchical-level reasoning over environmen-
tal signals, and distills lessons from statistical feedback
rather than binary signals.
•We show thatmufasaachieves state-of-the-art valua-
tion forecasting performance across multiple global mar-
kets, while recovering interpretable and economically
grounded symbolic relationships.
•Wereleasearichsetofartifacts,includingthediscovered
symbolicequations,distilledlessonsacrossself-evolving
iterations, and context-dependent importance of differ-
entvaluationperspectives,offeringinsightsforfuturere-
search on financial fundamental analysis.
Related Work
FinancialFundamentalAnalysis.Traditionalfinancelit-
erature defines fundamental analysis (FA) as the evaluation
ofacompany’saccountinginformation(Bauman1996),such
as the information found in financial statements or balance
sheets. The aim is to understand the intrinsic value of the
company(Grahametal.1951)andidentifystocksthatmaybe
undervaluedtomakeaprofit.Therearemultipleapproaches
to fundamental investing, such as value investing (Graham
2003;BuffettandCunningham2001),factorinvesting(Fama
and French 1992; Asness, Liew, and Stevens 1997), or in-
vestingaroundmacroeconomictrends(Dalio2018).Eachof
theseinvolvesanalyzingdifferenttypesoffinancialinforma-
tionandmayresultindifferentinvestmentoutcomes(Capaul
etal.1993;Asnessetal.2000;PetkovaandZhang2005).Un-
liketraditionaldeep-learningmethods(XuandCohen2018;
Hu et al. 2018; Lin et al. 2021), financial approaches em-
phasize economic interpretability (Shmueli 2010). Recent
works have also explored using financial LLMs to perform
interpretable analysis over structured accounting data (Qian
etal.2025;Liuetal.2025),butthesefocusonfinancialQA,
and do not deal with forecasting or financial valuation.
Symbolic Regression.Symbolic regression (SR) aims to
discover mathematical expressions that describe relation-
ships in data (Cranmer 2023). Classical SR approaches
(Schmidt and Lipson 2009a,b) are often based on evolu-
tionary algorithms, such as genetic programming, which it-
erativelyevolvecandidateexpressionsthroughmutationand
recombination. While effective, these methods often suffer
fromlargesearchspacesandcomputationalinefficiency.The
emergence of large language models (LLMs) advanced SR
byenablingknowledge-guidedhypothesisgeneration,where
models can propose equations informed by prior scientific
knowledge (Grayeli et al. 2024; Shojaee et al. 2025). These
approaches have demonstrated strong performance in redis-
covering known physical laws and uncovering novel rela-
tionships in scientific domains (Romera-Paredes et al. 2024;
Novikov et al. 2025; Xie et al. 2026).

Self-EvolvingLLMAgents.Earlyworkshaveshownthat
LLMscanfunctionasagentsthatinteractwithexternaltools
andenvironments(Yaoetal.2022;Schicketal.2023),which
established the foundation for LLM agents, unlocking exter-
nalcapabilitiesbeyondlearningmodelweights.Laterworks
show that LLM agents can self-improve through various
techniques: For example, self-reflective frameworks enable
agents to improve by learning from feedback signals from
theenvironment(Shinnetal.2023;Zelikmanetal.2022).In
contrast, agent memory enables agents to accumulate expe-
rience over time and refine reasoning and decision-making
strategies (Zhang et al. 2026; Cao et al. 2025; Long et al.
2026).ThisideaofusingLLMsasagentsisfurtherextended
to self-evolving multi-agent systems, where multiple agents
can collectively improve through coordination (Wang et al.
2025;Zhaietal.2025;Xiaetal.2025).Withinthesesystems,
differentagentscantakeonspecializedroles,whiletheover-
all system would improve through environment feedback,
experiential memory, and interaction across the agents (Qiu
et al. 2025b,a; Zhang et al. 2025).
ThemufasaFramework
In this section, we first study the interpretable fundamental
analysis problem and its challenges as compared to the stan-
dardsymbolicregressiontask.Wethenexplaintheproposed
Multi-AgentFundamentalAnalysiswithSymbolicAdaptive
learning (mufasa) framework, shown in Figure 2.
Problem Formulation
Given a universe of companies and an accounting informa-
tiondatabaseX t fortimet,ourgoalistoproducevaluations
for each companyi, which are evaluated against their look-
ahead stock pricesy i,t+1. Importantly, we aim to identify
aninterpretablesymbolicrelationship,formalizedbyasym-
bolic expression ˜f, that explains how company valuations
are derived from accounting data.
This setting differs from the standard symbolic regres-
sion task (Cranmer 2023; Shojaee et al. 2025) in two ways.
Firstly, the relevant explanatory variablesxi,t ⊆ Xt are not
explicitly specified a priori, but must instead be identified
from the information database during the discovery process.
Secondly, the underlying financial relationships are context-
dependent,i.e.,the symbolic expression ˜fcan vary across
market conditions. We define a context variableC(·), which
canincorporatemultiplecontextualfactors.Inthiswork,we
defineC(i, t) = (s(i), r(t)), representing company sectors
s(i)and market regimesr(t), respectively. More formally,
givenX t and observedyi,t+1 for all companiesi, our model
seeks to discover a set of explanatory variablesˆ xi,t and the
context-dependent symbolic expressions˜fC(i,t) such that:
˜fC(i,t) (ˆ xi,t)≈y i,t+1,∀i, t.(1)
The discovered variables and expressions should not only
accurately fit the observed targets, but also maintain strong
generalizability across unseen out-of-sample data while re-
maining interpretable.
Disentangled Symbolic Discovery
Unlike the natural sciences, financial valuation does not ad-
mit a single universal functional form. To capture this het-
erogeneity, we disentangle the symbolic discovery process
using a set of perspectives, each associated with a specific
valuation philosophy established in finance literature (Buf-
fettandCunningham2001;Dalio2018).Then,eachperspec-
tive is incorporated into an LLM agent, which seeks to find
the best equation based on its beliefs. Each agent operates
autonomously: it can propose hypotheses, retrieve relevant
financial variables via external tools, and evaluate candidate
expressions based on observed outcomes via code.
Perspective Decomposition.Formally, we define a set of
valuationphilosophiesathatconstrainsthehypothesisspace.
Each philosophy induces inductive biases over candidate
equations, including preferred variables and structural pat-
terns, which prevents the collapse of expression diversity.
Hypothesis Generation.For each perspectivea, we em-
ploy an LLMπθ to iteratively generate candidate symbolic
expressions ˜f (a). At each step, a new hypothesis is sam-
pled as: ˜f (a) ∼π θ(· |p(a)), wherep (a) is the constructed
prompt. The prompt encodes the investing philosophyaand
accumulated learningsZ (a) derived from historical interac-
tions and statistical feedback.
ToolUse:DataRetrieval.Eachcandidateexpression ˜f (a)
implicitly defines a set of variablesˆ x(a) i,t that the agent may
retrieve from the databaseXt using external tools. Specifi-
cally, the agent first queries a semantic retrieval mechanism
to obtain candidate variable names and descriptions, and
subsequently selects and retrieves the corresponding data.
If a retrieval attempt fails (e.g.,due to unavailability or in-
sufficient coverage), the model receives structured feedback
(Schicketal.2023)andadaptsitshypothesisaccordingly,ei-
therbyrefiningthevariablesusedormodifyingtheproposed
expression.
ToolUse:CodeEvaluation.Eachcandidateexpressionis
representedasanexecutableprogram,enablingdirectevalu-
ation. Given the hypothesized expression˜f (a) and retrieved
variablesx (a) i,t , the expression is evaluated to compute pre-
dicted values:
ˆy(a) i,t+1 = ˜f (a)

x(a) i,t

.(2)
Similarly,iftheexpressionfailstoexecute(e.g.,duetosyntax
errors, invalid operations, or non-finite outputs), the system
returns structured feedback (Gao et al. 2023), which is in-
corporated into the promptp(a). The agent then revises its
subsequent hypothesis accordingly.
Hypothesis Optimization and Assessment.Similar to
LLM-SR (Shojaee et al. 2025), we refine candidate expres-
sions through numerical optimization of their coefficients.
Given a proposed expression˜f (a), we treat any scalar mul-
tipliers or parameters as continuous variables and optimize
themdirectlywithrespecttothetrainingdata.Thisdecouples
structure discovery from parameter fitting: the LLM defines

“Value is decided by how much
cash the company has.”
Hypothesis
generation
Tool: Search for
relevant data
Tool: Write +
Execute code
Tool: Access
memory base
Cash Flow Agent
“Value is decided by how much
the company is earning.”
Hypothesis
generation
Tool: Search for
relevant data
Tool: Write +
Execute code
Tool: Access
memory base
Earnings Agent
“Value is decided by how fast
the company is growing.”
Hypothesis
generation
Tool: Search for
relevant data
Tool: Write +
Execute code
Tool: Access
memory base
Growth Agent
Meta-Coordinator Agent
Hypothesis generation (Meta-level)
Tool: Run evaluations using code
Tool: Read/Write to memory base
Disentangled, Self-EvolvingAgents
…
Hierarchical
Level Reasoning
Reasons over
environment
Reasons over
perspectives
2
1
Statistical Agent Memory
…Variance90thPct (Tail Risk)Sector AvgMAPEAgent
…0.028928.1212.4010.38Growth
3
Statistical Insights:
•Cash flow ratios produce high variance in asset-light firms.
•Growth terms amplify tail risk in high-growth sectors.
Cash Flow Memory
…MAPEEquation
…3.99𝐹𝐶𝐹!"#	%&’#"÷4×CAPEX
…1.38𝐹𝐶𝐹!"#	%&’#"×17.48
………
Insights: CAPEX misaligned with philosophy…
Earnings Memory
…MAPEEquation
…1.37𝐸𝐵𝐼𝑇!"#	%&’#"÷EY
…0.52𝐸𝑃𝑆()*×14.90
………
Insights: Model overlook capital efficiency…
Growth Memory
…MAPEEquation
…1.90𝑅𝑒𝑣!"#	%&’#"×(1+	𝑔#"+)
…0.81𝑔#"+×SGR	×1.051
………
Insights: Capture long-term growth potential…
Figure2:Overviewofthemufasaframework.mufasausesdisentangledmulti-agentsystemstoencouragesymbolicexpression
diversity. A meta-coordinator agent reasons over the non-stationary environment to integrate these expressions. Each agent
maintains a memory to identify past statistical patterns.
the functional form of ˜f (a), while numerical routines ad-
just its coefficients to improve empirical performance. We
usedifferentialevolution(StornandPrice1997)asouropti-
mization approach.
Followingoptimization,weassessthefitnessofeachcan-
didate expression by evaluating its predictive performance
on observed data. Given the predicted target valuesˆy(a) i,t+1,
we define a fitness evaluation score as the prediction error
against ground truth:
L(a) =MAPE  ˆy(a) i,t+1, yi,t+1  .(3)
Here, the output of the philosophy-constrained function is
evaluated against the overall look-ahead pricesyi,t+1 to en-
surethatthemostgeneralizablefunctionforeachphilosophy
is obtained, as detailed in Algorithm 1 of Appendix A.
Hierarchical-Level Reasoning
Financialmarketenvironmentsareinherentlynon-stationary.
Because of this, the relationship between candidate solu-
tions and their evaluation outcomes is unstable, making it
difficult for learning experience to accumulate. To account
for this, we introduce hierarchical-level reasoning, where a
meta-coordinator agent learns to reason over market condi-
tions to contextualize the different agent outputs.
For each contextC(i, t), the goal of the meta-coordinator
agentπ ϕ istoproduceaweightvectorthatshowstherelative
importanceoftheagentsduringthatcontext.Ateachstep,the
meta-coordinator constructs a promptpmeta which includes
the current context, the agent-level performancesL(a) and
the accumulated learningsZmeta. It then selects a subset of
agents,andcomputestheirweightvector˜ wC(i,t) viaSLSQP-
based (Kraft 1988) constrained optimization.
Given the agent outputs and the weight vector, we define
the aggregated valuation in each context as:
ˆyi,t+1 =˜ w⊤ C(i,t) · ˆyi,t+1,(4)
where ˆyi,t+1 denotes the vector collectingˆy(a) i,t+1 for the set
of philosophy-disentangled agentsa.
Similarly, we assess the quality of each candidate weight
vector by evaluating its predictive error:
Lmeta =MAPE(ˆyi,t+1, yi,t+1).(5)
This hierarchical design enables continual adaptation of
agent weights under non-stationary feedback.
Statistical Performance Memory
Unlike the natural sciences, which seek a single correct ex-
pression, or agent-based tasks with binary outcomes, finan-
cial expressions are evaluated through noisy and continuous
performance measures. This complicates the ability of cur-
rent agent memory (Ouyang et al. 2026; Zhang et al. 2026)
to effectively learn from past experience, as they typically
rely on signals derived from successful or failed attempts at
completingatask.Tocopewiththis,weaugmentagentmem-
ory withstructured statistical informationthat captures the
statistical behavior of previously explored equations. Rather
than storing only a scalar loss, memory records each hy-
pothesis together with a statistical summary of its observed
behavior, as demonstrated in Table 1.
Fromthememory,wedistillasetoflearningsZ (a).which
guide the generation of new hypotheses at the beginning of

Category What is stored Why
Accuracy Mean MAPE, Median MAPE Captures overall predictive accuracy while reducing sensi- tivity to outliers and skewed observations.
Stability Standard Deviation, IQR, Coefficient of Variation Measureswhetherperformanceisconsistentorhighlyvari- able across samples or time periods.
Tail Riskp90/p95Error, Worst-Decile Mean Exposes extreme failure modes that are often hidden by average performance metrics.
Complexity Variable + Operator Count, Prediction Coverage Reflects interpretability and numerical reliability of the ex- pression in practical use.
Bias Mean Signed Percentage Error (MSPE) Detects systematic over- or under-prediction across obser- vations rather than isolated errors.
Ranking Spearman Rank Correlation Captures whether the expression preserves cross-sectional ordering beyond absolute scale accuracy.
Calibration Signed Pct Error by Quartiles of Actual Price Reveals whether the expression systematically misprices cheap or expensive stocks.
Table 1: Statistical information collected bymufasato enable learning under continuous feedback.
the loop. These learnings capture recurring statistical regu-
larities that are not apparent from individual binary pass or
fail signals, where a single evaluation could be dominated
by noise and lead to unreliable scoring of candidate expres-
sions.Byaggregatingoutcomesacrossrepeatedevaluations,
the system can recover more reliable estimates of relative
performance, including properties such as variance and tail
behavior that are not observable from isolated observations.
Through this process (detailed in Algorithm 2 of Ap-
pendix A),mufasainfers heuristically effective strategies
that demonstrate consistent performance across its evalu-
ations, improving the overall robustness of the symbolic
search.
Experiments
Dataset.We evaluatemufasaacross five equity markets.
The primary dataset consists of all S&P 500 constituents
from 1990 Q1 to 2023 Q2, with constituent entry and exit
dates included to prevent survivorship bias. To demonstrate
generalisabilityacrossgeographiesandmarketstructures,we
additionally evaluate on the CSI 300 (2002-2021), STOXX
600(1995-2025),Russell2000(1990-2025),andFTSEAsia
Pacific ex-Japan (1996-2025), beginning each series at the
earliest date with sufficient data coverage. For all markets,
data is split chronologically: the first 80% of quarters form
the training set and the remaining 20% form the held-out
test set. The fundamental data is sourced from Bloomberg
andthemacroeconomicdataprimarilyfromFactSet.Weuse
data from original quarterly filings only, preventing look-
ahead bias from subsequent restatements, and define the tar-
get variable as the stock price at the end of the fiscal quarter
immediately following each filing period. The forecasting
resolution is quarterly, as fundamental analysis is typically
used for long-term stock investment. (Graham 2003).
Market Settings.For regime context, bull and bear mar-
kets are defined at the index level following the standard
practitioner convention (Pagan and Sossounov 2003): a bull
marketisdeclaredwhentheindexhasrisenatleast20%from
itsmostrecenttrough,andabearmarketwhenithasfallenat
least 20% from its most recent peak. Regimes are computed
from the index prices sourced from Yahoo Finance.
Baselines.Wecomparemufasaagainstthreecategoriesof
closely-related benchmark models.
1.Traditional machine learning methods: Random For-
est(Breiman2001),HistGBM(Keetal.2017),andNeu-
ralNet (Rumelhart, Hinton, and Williams 1986).
2.Symbolic regression: PySR (Cranmer 2023), FunSearch
(Romera-Paredes et al. 2024), and LLM-SR (Shojaee
et al. 2025). These models do symbolic discovery for
scientific equations using evolutionary algorithms or an
iterative single-LLM loop.
3.Financial reasoning LLMs: Fin-R1 (Liu et al. 2025) and
Fino1 (Qian et al. 2025). These pre-trained LLMs were
originally finetuned to perform reasoning over financial
accounting data, but they do not deal with forecasting.
4.Financial valuation: We compare with some classi-
cal financial valuation approaches, including the sector-
median P/E, EV/EBIT, EV/EBITDA, and P/B ratios, and
also the Dividend Discount Model (DDM), Free Cash
Flow to Equity (FCFE), and Free Cash Flow to Firm
(FCFF) models (Damodaran 2012).
5.Financial agentic frameworks: FinCon (Yu et al. 2024);
FinVision (Fatemi and Hu 2024)
ImplementationDetails.AllLLMsareservedlocallyus-
ing vLLM on NVIDIA RTX A5000 GPUs, which takes ~10
mins per agent on each processing unit. We use Qwen3-4B-
Thinking (Team 2025) for all agents, with a temperature of
0.7 for the agents and 0.3 for the memory components. The
model context window is 32,768 tokens; we set a maximum
generation length of 16,384 tokens. We evaluate the models
onMean Absolute Percentage Error (MAPE). The lower
the results, the better.
Results
PerformanceComparison.Table2reportstheforecasting
performance. We observe the following:

Model S&P 500 Russell 2000 STOXX 600 FTSE APAC CSI 300 All Data Avg∆
Machine Learning Based Methods
Random Forest 0.4812 0.6551 0.7490 0.8436 0.5605 0.6579 0.1498
HistGBM 0.5916 0.8121 0.9774 1.3771 0.6041 0.8725 0.3644
NeuralNet 0.6130 1.0302 0.8963 1.5292 0.5242 0.9186 0.4105
Financial LLMs
Fino1 (Qian et al. 2025) 1.0230 2.1244 1.0958 1.2587 1.3388 1.3681 0.8600
Fin-R1 (Liu et al. 2025) 0.5263 0.7324 0.7437 0.8862 0.8095 0.7396 0.2315
Financial Valuation
P/E 0.5127 0.8450 0.6209 0.7439 0.6035 0.6652 0.1571
EV/EBIT 0.5580 0.9907 0.6099 0.9150 0.6698 0.7487 0.2406
EV/EBITDA 0.5558 1.1589 0.6808 0.9314 0.6472 0.7948 0.2867
P/B 0.7177 0.8727 2.3048 0.8371 0.8401 1.1145 0.6064
DDM 0.7991 0.9370 1.0324 0.8691 0.6358 0.8547 0.3466
FCFE 0.9865 1.1827 1.3975 0.8700 0.8196 1.0513 0.5432
FCFF 1.2434 1.4313 1.5155 0.9097 0.8412 1.1882 0.6801
Symbolic Regression
PySR (Cranmer 2023) 0.6394 0.5892 0.6741 0.7514 0.5215 0.6351 0.1270
FunSearch (Romera-Paredes et al. 2024) 0.7146 1.1524 0.7693 0.7855 0.5735 0.7991 0.2910
LLM-SR (Shojaee et al. 2025) 0.4761 0.7822 0.8269 0.9534 0.5967 0.7271 0.2190
Financial Agentic Frameworks
FinCon (Yu et al. 2024) 0.9581 0.9746 1.1822 0.6358 0.5784 0.8658 0.3577
FinVision (Fatemi and Hu 2024) 0.8203 0.5842 1.2521 0.9974 0.9956 0.9299 0.4218
mufasa(Ours)0.4465 0.5718 0.5064 0.5814 0.4343 0.50810.3702 (Avg)
Table 2: Performance comparison. The best baselines are underlined, and the best results are bolded.
•Fin-R1 consistently outperforms Fino1, likely because its
emphasis on generalization and transfer better matches
the forecasting setting. Nevertheless, both LLMs under-
perform most specialized baselines.
•Traditional valuation ratios (e.g.,P/E, EV/EBIT) compet-
itive across most markets. Their simple structure makes
them relatively robust to estimation error, although their
performance varies considerably across regions, suggest-
ing that markets rely on different fundamental signals.
•More complex discounted cash-flow methods, including
FCFF and FCFE, perform less well because they depend
on noisy estimates such as growth rates and discount fac-
tors.Weusethesingle-stageGordonGrowthModel(Gor-
don1962),whichassumesconstantgrowth;moreaccurate
parameter estimation may improve these methods.
•Among the SR baselines, PySR performs strongly, unlike
the typical advantage of LLM-based SR. Scientific priors
encodedbyLLMsmaybelessusefulinfinance,whererela-
tionships are context-dependent and lack stable governing
laws. PySR’s evolutionary search may therefore be better
suited to identifying empirically effective expressions.
•mufasaachieves the best performance across all datasets,
with an average improvement of 19.65%. Existing finan-
cial agentic frameworks, FinCon and FinVision, perform
competitively in selected markets but generalize incon-
sistently across regions. In contrast,mufasaoutperforms
the better agentic baseline in every market, reducing its
error by 27.67% on average. This advantage stems from
perspective-specific hypothesis generation and statistical
memory that retains empirically robust expressions.
Moredetailsonthestatisticalsignificanceoftheexperiments
can be found in Appendix B.
Model Variant S&P 500 Russell 2000 STOXX 600 FTSE APAC CSI 300
S.P Agent 0.4971 0.8994 0.7608 0.6095 0.5928
M.P (Equal Weights) 0.4652 0.8768 0.5448 0.6442 0.5309
M.P (No Stats Memory) 0.4702 0.7525 0.5398 0.5852 0.4852
M.P (Best Single Agent) 0.4676 1.9173 0.5256 0.5833 0.4739
mufasa(Ours)0.4465 0.5718 0.5064 0.5814 0.4343
Table 3: Ablation study on perspective variant. S.P and M.P
denote the single-/multiple perspective, respectively. Best
results are bolded, second best are underlined.
Ablation Study.We conduct an ablation study to demon-
strate the effectiveness of the model design.
•TheSingle-Perspective Agentuses one LLM agent to
search for a unified valuation expression. It is outper-
formed by the equal-weight multi-perspective variant on
fourofthefivemarkets,suggestingthatrepresentinghet-
erogeneousvaluationsignalswithinasinglesearchspace
limits effective exploration.
•Multi-Perspective (Equal Weights)progresses to multi-
perspective agents, but without hierarchical reasoning. It
improves over the single-perspective variant. Disentan-
glingintospecializedagentshelpsoptimizationbyfocus-
ing each agent on a subset of variables and relationships,
enabling more diverse exploration and better generaliza-
tion even when combined using simple averaging.
•Multi-Perspective (No Stats Memory)adds hierarchical
reasoning with the meta-coordinator agent, but without
statistical memory. It outperforms equal weighting on
four of the five markets, demonstrating the benefit of hi-
erarchical coordination. Nevertheless, without statistical
memory, the system relies primarily on coarse outcome
feedback and cannot reliably distinguish consistently ef-
fective expressions from those that succeed by chance.
•Multi-Perspective (Best Single Agent)retains the spe-

Model Equation Theory Equation Theory
Fino1 EV /EBIT DA·(1 +gEP S/100) EV /EBIT DAmkt ·EBIT DA - -
Fin-R1EP S T T M·P E EP S·P EEarnings Multiple
PySR
r
1.79· |BV P S| ·
qp
|T ax|+T ax·

EP S·e2.43 −e √Y30 + (eP Bmkt,med +EP S)·4.23

 - -
FunSearch0.40·EBIT DA ps + 0.30·Revenue ps + 0.20·ROE+ 0.10·P E- -
LLM-SR0.01·P E−0.03· EV EBIT −0.04· EV EBIT DA+ 0.58·P B+ 13.99·N Ips −0.01·Revenue ps Ri =α+β 1X1,i +β 2X2,i +· · ·Linear Factor
mufasaagents
EarningsN I ps ·(1 + 0.01·gEP S)·P E·0.88 EP S r−g Gordon Growth
CashflowF CF ps · EV EBIT DA· 100 88.38 P∞ t=1 F CFt (1 +r)t Discounted Cash Flow
AssetBV P S·

1 + 1.01· R&D Assets  ·  1−13829.10· R&D Assets  · P B−7.24×10 −4 1.34 BV P S·P BBook Multiple
Growth(P/F CF) mkt ·

F CFps + 0.29· P/F CF (P/F CF)mkt

·(1−14.80·(F CF ps <1.08))·0.01M etric·M ultipleRelative Valuation
QualityN I ps ·P/F CF·(1 + log(1 +ROE/100)·0.87)BV+ P∞ t=1 (ROEt −r)·BV t−1 (1 +r)t Residual Income
Table 4: Learnt equationsvs.related valuation forms in finance literature, for the S&P500 dataset.
cialized agents and statistical memory but uses only the
strongest individual agent. It obtains the second-best re-
sult on three markets but degrades substantially on Rus-
sell 2000, showing that reliance on a single perspective
isunstableandrequiresanagent-selectionrulethatisnot
available in advance.
•Themufasaframework achieves the best performance
across all datasets. We see that integrating multiple
perspectives shows improvement over any of the best
agents. Overall, combining multi-perspective agents,
hierarchical-level reasoning, and statistical memory pro-
duces the best results.
A more comprehensiveablation study and additional exper-
iments can be found in Appendix F, G.
Figure 3: Best error trajectories over the self-evolving itera-
tions for each perspective agent.
Self-Evolving Agents.Figure 3 shows the best error tra-
jectoriesoveriterationsforeachagent.Eachagentexhibitsa
decreaseinthelowesterrorovertime,indicatingthatthesym-
bolic search process iteratively refines candidate equations.
Althoughthegeneralsingleagentalsoimproves,itsfinalbest
error remains higher than those achieved by the specialized
agents. This result is consistent with the difficulty of search-
ing for a single expression that simultaneously captures het-
erogeneousvaluationmechanisms.Byrestrictingeachagent
to a specific valuation perspective, the disentangled design
enables more focused exploration of the symbolic search
space and yields stronger final solutions.
DiscoveredEquations.Table4showsthelearntequations
on the S&P 500 dataset, together with the most closely re-
lated valuation forms that can be found in finance literature
(Damodaran 2012; Graham et al. 1951). We observe:
•Fin-R1 largely reproduces the standard earnings-multiple
formulaEP S·P E.Whileinterpretable,thisfixedformof-
ferslimitedadaptationtotheobserveddataandrepresents
only one valuation perspective.
•PySR discovers a high-performing but financially opaque
expression, reflecting its primarily heuristic search. LLM-
SRinsteadcombinesvariablesfromseveralperspectivesin
alinearform,butdoesnotrecovertheperspective-specific
structures observed in classical valuation models.
•In contrast,mufasa’s specialized agents recover adapted
forms of earnings-multiple, discounted-cash-flow, book-
value, relative-valuation, and residual-income models.
This suggests that perspective disentanglement promotes
economicallygroundedequationdiscovery,whileallowing
the learned forms to adapt to the data.
Released Artifacts.The learnt equations for other
datasets,themeta-coordinatorweights,andthedistilledagent
learningsZ (a) are in Appendices C, D, and E, respectively.
Conclusion
Inthiswork,westudysymbolicdiscoveryforfinancialfunda-
mentalanalysis,whichconstitutesadistinctclassofsymbolic
regression problems. Unlike the natural sciences, financial
valuation admits multiple valid perspectives, operates under
non-stationarymarketconditions,andreliesonnoisy,contin-
uousperformancesignals.Toaddressthis,weintroducemu-
fasa,ahierarchicalmulti-agentframeworkthatdecomposes
thediscoveryprocessintospecializedagents,integratesthem
through hierarchical-level context reasoning, and leverages
statistical-based memory to guide learning. We conduct ex-
tensive experiments across global markets and show that
mufasaachieves strong forecasting performance while pro-
ducing interpretable and economically grounded symbolic
expressions. We release the learnt symbolic expressions and
the distilled agent learnings to the public.

References
Allard, M.-A.; Teinturier, A.; Xing, V.; and Viaud, G.
2026. Experientialreflectivelearningforself-improvingllm
agents.arXiv preprint arXiv:2603.24639.
Andrews, D. W. 1991. Heteroskedasticity and autocorrela-
tionconsistentcovariancematrixestimation.Econometrica:
Journal of the Econometric Society, 817–858.
Asness, C. S.; Liew, J. M.; and Stevens, R. L. 1997. Paral-
lels between the cross-sectional predictability of stock and
country returns.Journal of Portfolio Management, 23(3):
79.
Asness,C.S.;etal.2000. Styletiming:Valueversusgrowth.
Journal of Portfolio Management.
Bauman, M. P. 1996. A review of fundamental analysis
research in accounting.Journal of Accounting Literature,
15: 1.
Breiman,L.2001.Randomforests.Machinelearning,45(1):
5–32.
Buffett, W.; and Cunningham, L. A. 2001.The essays of
Warren Buffett: lessons for corporate America. HeinOnline.
Cao,Z.;etal.2025. Rememberme,refineme.arXivpreprint
arXiv:2512.10696.
Capaul,C.;etal.1993. Internationalvalueandgrowthstock
returns.Financial Analysts Journal.
Cranmer, M. 2023. Interpretable machine learning for sci-
ence with PySR and SymbolicRegression. jl.arXiv preprint
arXiv:2305.01582.
Dalio, R. 2018.Principles. Simon & Schuster.
Damodaran, A. 2012.Investment valuation: Tools and tech-
niques for determining the value of any asset. John Wiley &
Sons.
Diebold, F. X.; and Mariano, R. S. 2002. Comparing pre-
dictive accuracy.Journal of Business & economic statistics,
20(1): 134–144.
Fama, E. F.; and French, K. R. 1992. The cross-section of
expected stock returns.the Journal of Finance, 47(2): 427–
465.
Fatemi,S.;andHu,Y.2024.FinVision:Amulti-agentframe-
work for stock market prediction. InProceedings of the 5th
ACM International Conference on AI in Finance, 582–590.
Gao, L.; Madaan, A.; Zhou, S.; Alon, U.; Liu, P.; Yang,
Y.; Callan, J.; and Neubig, G. 2023. Pal: Program-aided
language models. InInternational conference on machine
learning, 10764–10799. PMLR.
Gordon, M. J. 1962. The savings investment and valuation
of a corporation.The Review of Economics and Statistics,
37–51.
Graham, B. 2003.The intelligent investor. HarperBusiness.
Graham,B.;Dodd,D.L.F.;Cottle,S.;andTatham,C.1951.
Security analysis: Principles and technique. McGraw-Hill
New York.
Grayeli, A.; Sehgal, A.; Costilla-Reyes, O.; Cranmer, M.;
andChaudhuri,S.2024. Symbolicregressionwithalearned
conceptlibrary.AdvancesinNeuralInformationProcessing
Systems, 37: 44678–44709.
Harvey, D.; Leybourne, S.; and Newbold, P. 1997. Testing
theequalityofpredictionmeansquarederrors.International
Journal of forecasting, 13(2): 281–291.
Hu, Z.; Liu, W.; Bian, J.; Liu, X.; and Liu, T.-Y. 2018. Lis-
tening to chaotic whispers: A deep learning framework for
news-oriented stock trend prediction. InProceedings of the
eleventh ACM international conference on web search and
data mining, 261–269.
Ke, G.; Meng, Q.; Finley, T.; Wang, T.; Chen, W.; Ma, W.;
Ye,Q.;andLiu,T.-Y.2017. Lightgbm:Ahighlyefficientgra-
dientboostingdecisiontree.Advancesinneuralinformation
processing systems, 30.
Kraft, D. 1988. A software package for sequential quadratic
programming.Forschungsbericht- Deutsche Forschungs-
und Versuchsanstalt fur Luft- und Raumfahrt.
Lin, H.; Zhou, D.; Liu, W.; and Bian, J. 2021. Learning
multiplestocktradingpatternswithtemporalroutingadaptor
and optimal transport. InProceedings of the 27th ACM
SIGKDDconferenceonknowledgediscovery&datamining,
1017–1026.
Liu, Z.; et al. 2025. Fin-R1: A Large Language Model for
FinancialReasoningthroughReinforcementLearning.arXiv
preprint arXiv:2503.16252.
Long, L.; et al. 2026. Seeing, listening, remembering, and
reasoning: A multimodal agent with long-term memory. In
International Conference on Learning Representations.
Newey, W. K.; and West, K. D. 1987. A Simple, Positive
Semi-Definite,HeteroskedasticityandAutocorrelationCon-
sistent Covariance Matrix.Econometrica, 55(3): 703–708.
Novikov, A.; V˜u, N.; Eisenberger, M.; Dupont, E.; Huang,
P.-S.; Wagner, A. Z.; Shirobokov, S.; Kozlovskii, B.; Ruiz,
F. J.; Mehrabian, A.; et al. 2025. Alphaevolve: A coding
agentforscientificandalgorithmicdiscovery.arXivpreprint
arXiv:2506.13131.
Ouyang, S.; Yan, J.; Hsu, I.-H.; Chen, Y.; Jiang, K.; Wang,
Z.; Han, R.; Le, L. T.; Daruki, S.; Tang, X.; et al. 2026.
Reasoningbank: Scaling agent self-evolving with reasoning
memory. InInternational Conference on Learning Repre-
sentations.
Pagan, A. R.; and Sossounov, K. A. 2003. A simple frame-
workforanalysingbullandbearmarkets.Journalofapplied
econometrics, 18(1): 23–46.
Petkova,R.;andZhang,L.2005.Isvalueriskierthangrowth?
Journal of Financial Economics.
Qian, L.; et al. 2025. Fino1: On the transferability
of reasoning enhanced llms to finance.arXiv preprint
arXiv:2502.08127.
Qiu,J.;etal.2025a.Alita-G:Self-EvolvingGenerativeAgent
for Agent Generation.arXiv preprint arXiv:2510.23601.
Qiu,J.;etal.2025b.Alita:Generalistagentenablingscalable
agentic reasoning.arXiv preprint arXiv:2505.20286.
Romera-Paredes, B.; Barekatain, M.; Novikov, A.; Balog,
M.; Kumar, M. P.; Dupont, E.; Ruiz, F. J.; Ellenberg, J. S.;
Wang, P.; Fawzi, O.; et al. 2024. Mathematical discoveries
from program search with large language models.Nature,
625(7995): 468–475.

Rumelhart, D. E.; Hinton, G. E.; and Williams, R. J. 1986.
Learningrepresentationsbyback-propagatingerrors.nature,
323(6088): 533–536.
Saveliev,E.;Holt,S.;Seedat,N.;Bentley,D.L.;Weatherall,
J.;andvanderSchaar,M.2026. Influence-GuidedSymbolic
Regression: Scientific Discovery via LLM-Driven Equation
SearchwithGranularFeedback. InForty-thirdInternational
Conference on Machine Learning.
Schick, T.; et al. 2023. Toolformer: Language models can
teach themselves to use tools.Advances in Neural Informa-
tion Processing Systems.
Schmidt, M.; and Lipson, H. 2009a. Distilling free-form
natural laws from experimental data.science, 324(5923):
81–85.
Schmidt, M.; and Lipson, H. 2009b. Symbolic regression
of implicit equations. InGenetic programming theory and
practice VII, 73–85. Springer.
Shinn, N.; et al. 2023. Reflexion: Language agents with ver-
bal reinforcement learning.Advances in Neural Information
Processing Systems.
Shmueli, G. 2010. To explain or to predict?Statistical
science, 289–310.
Shojaee, P.; Meidani, K.; Gupta, S.; Farimani, A. B.; and
Reddy,C.K.2025. Llm-sr:Scientificequationdiscoveryvia
programming with large language models. InInternational
Conference on Learning Representations.
Storn,R.;andPrice,K.1997.Differentialevolution–asimple
andefficientheuristicforglobaloptimizationovercontinuous
spaces.Journal of global optimization, 11(4): 341–359.
Team,Q.2025.Qwen3TechnicalReport.arXiv:2505.09388.
Wang, Y.; et al. 2025. Evoagentx: An automated framework
for evolving agentic workflows. InProceedings of the 2025
ConferenceonEmpiricalMethodsinNaturalLanguagePro-
cessing: System Demonstrations.
Xia,P.;etal.2025. Agent0:Unleashingself-evolvingagents
from zero data.arXiv preprint arXiv:2511.16043.
Xie, Z.; Li, W.; Luo, M.; Jiang, J.; and Chen, L. 2026. Lan-
guagemodelsguidesymbolicequationdiscoverybycontrol-
ling search.arXiv preprint arXiv:2607.04156.
Xiong, Z.; Lin, Y.; Xie, W.; He, P.; Liu, Z.; Tang, J.;
Lakkaraju, H.; and Xiang, Z. 2026. How memory manage-
ment impacts llm agents: An empirical study of experience-
followingbehavior. InProceedingsofthe64thAnnualMeet-
ingoftheAssociationforComputationalLinguistics(Volume
1: Long Papers).
Xu, Y.; and Cohen, S. B. 2018. Stock movement prediction
from tweets and historical prices. InProceedings of the
56th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 1970–1979.
Yao,S.;etal.2022. React:Synergizingreasoningandacting
inlanguagemodels.InInternationalConferenceonLearning
Representations.
Yu, Y.; Yao, Z.; Li, H.; Deng, Z.; Jiang, Y.; Cao, Y.; Chen,
Z.; Suchow, J. W.; Cui, Z.; Liu, R.; et al. 2024. Fincon:
A synthesized llm multi-agent system with conceptual ver-
bal reinforcement for enhanced financial decision making.
Advances in Neural Information Processing Systems, 37:
137010–137045.
Zelikman, E.; et al. 2022. STAR: Bootstrapping reasoning
with reasoning.Advances in Neural Information Processing
Systems.
Zhai, Y.; Tao, S.; Chen, C.; Zou, A.; Chen, Z.; Fu, Q.; Mai,
S.; Yu, L.; Deng, J.; Cao, Z.; et al. 2025. Agentevolver:
Towards efficient self-evolving agent system.arXiv preprint
arXiv:2511.10395.
Zhang, G.; Ren, H.; Zhan, C.; Zhou, Z.; Wang, J.; Zhu, H.;
Zhou, W.; and Yan, S. 2026. Memevolve: Meta-evolution of
agent memory systems. InForty-third International Confer-
ence on Machine Learning.
Zhang, W.; Cui, C.; Zhao, Y.; Hu, R.; Liu, Y.; Zhou, Y.;
andAn,B.2025. Agentorchestra:Ahierarchicalmulti-agent
framework for general-purpose task solving.arXiv e-prints,
arXiv–2506.

Table of Contents
A Detailed Methods..................................................................................... 10
B Statistical Significance Analysis........................................................................ 11
C Learnt Symbolic Expressions.......................................................................... 12
D Learnt Context Weighting............................................................................. 13
E Distilled Agent Learnings............................................................................. 15
F Extended Ablation Study.............................................................................. 20
G Additional Statistical Results.......................................................................... 21
H Limitations of the work............................................................................... 22
A Detailed Methods
Here, we provide the detailed algorithm for philosophy agent training and meta-coordinator training.
Algorithm 1: Philosophy Agent Training
Require:LLMπ θ, databaseXt, targetsy i,t+1, perspectivea, memoryM(a), learningsZ(a)
1: // Initialization
2: ˜f (a),x (a) i,t ←SeedEquation(a)
3:L (a) ←MAPE  ˜f (a)(x(a) i,t ), yi,t+1 
4:for alliterationsdo
5: // Hypothesis Generation
6:p (a) ←(a, ˜f (a),Z (a))
7: ˜f (a) ∼πθ(· |p(a))
8: // Tool use: Data Retrieval
9:ˆ x (a) i,t ←Retrieve(X t)
10:ifRetrieveErrorthen
11:p (a) ←p (a) ∪ErrorFeedback
12:end if
13: // Tool use: Code Evaluation
14:ˆy (a) i,t+1 ←Evaluate  ˜f (a),ˆ x(a) i,t 
15:ifEvaluateErrorthen
16:p (a) ←p (a) ∪ErrorFeedback
17:end if
18: // Hypothesis Optimization
19:ˆy (a) i,t+1 ←Optimize  ˆy(a) i,t+1 
20:L (a) ←MAPE  ˆy(a) i,t+1, yi,t+1 
21: // Memory Update
22:M (a) ←M (a) ∪ {(˜f (a),L (a))}
23:Z (a) ←UpdateLearnings(M (a))
24:end for
25:return ˜f (a)

Algorithm 2: Meta-Coordinator Training
Require:LLMπ ϕ, specialist forecastsˆy(a) i,t+1, targetsyi,t+1, memoryMmeta, learningsZmeta
1:for allC(i, t)do
2:˜ w C(i,t) ←InitWeights()
3:for alliterationsdo
4: // Hypothesis Generation
5:p meta ←(C(i, t),L(a),˜ wC(i,t) ,Z meta)
6:˜ w C(i,t) ∼π ϕ(· |pmeta)
7: // Tool use: Code Evaluation
8:ˆy i,t+1 ←˜ w⊤ C(i,t) · ˆyi,t+1
9:L meta ←MAPE(ˆyi,t+1, yi,t+1)
10: // Memory Update
11:M meta ←M meta ∪ {(˜ wC(i,t) ,L meta}
12:Z meta ←UpdateLearnings(M meta)
13:end for
14:end for
15:return˜ wC(i,t)
B Statistical Significance Analysis
To assess the statistical significance ofmufasa’s performance results, we apply the Diebold–Mariano (DM) test (Diebold and
Mariano 2002) under absolute percentage error loss. We incorporate two corrections.
First, we use a Newey–West heteroskedasticity and autocorrelation consistent (HAC) variance estimator (Newey and West
1987) to account for serial correlation in the loss differential series across quarters. Specifically, we employ a Bartlett kernel
with bandwidth selected according to Andrews’ rule (Andrews 1991):
L=
$
4
 T
100
2/9%
,(6)
whereTdenotes the number of test quarters. This adjustment is necessary because macroeconomic conditions that make one
quarterdifficulttoforecastoftenpersist,inducingautocorrelationinthelossdifferentialsandleadingtounderestimatedstandard
errors if uncorrected.
Second,weapplytheHarvey–Leybourne–Newbold(HLN)small-samplecorrection(Harvey,Leybourne,andNewbold1997),
whichadjuststheDMteststatisticandevaluatesitagainstat T−1 referencedistributionratherthanastandardnormaldistribution.
This accounts for the small number of test quarters available per market.
Table5:Diebold–Mariano(DM)testscomparingmufasaagainstvaluationandlearning-basedbaselines.Entriesreportmufasa
minus baseline in decimal form. Negative values indicate lower error (better performance). Significance: ***p <0.001, **
p <0.01, *p <0.05.
Baseline S&P 500 Russell 2000 STOXX 600 FTSE Asia CSI 300
Financial LLMs
Fino1 -0.7283*** -0.4515*** -0.3067*** -0.7925*** -0.3408***
Fin-R1 -0.1207*** -0.0375*** -0.1801*** -0.5919*** -0.4835***
Financial Valuation
P/E -0.1628*** -0.0371*** -0.0691*** -0.3519*** -0.1158***
EV/EBITDA -0.1174*** -0.1622*** -0.0802*** -0.2941*** -0.0933***
EV/EBIT -0.1235*** -0.0949*** -0.0531*** -0.2965*** -0.0982***
P/B -0.2535*** -0.0967*** -0.1894*** -0.1466*** -0.0618***
DDM -0.2476*** -0.0924*** -0.1514*** -0.1402*** -0.0321**
FCFE -0.2890*** -0.2154*** -0.1698*** -0.1001** -0.3787***
FCFF -0.2534*** -0.1774*** -0.1454*** -0.2862*** -0.2745***
Symbolic Regression
PySR -0.2695*** -0.0326*** -0.0857*** -0.3287*** -0.0956***
FunSearch -0.3992*** -0.3872*** -0.1696*** -0.4040*** -0.1365***
LLM-SR -0.1101*** -0.1751*** -0.2345*** -0.4354*** -0.1442***
Across all pairwise comparisons,mufasaachieves statistically significant improvements in MAPE, indicating that the
observed gains are mostly robust and not driven by random variations.

C Learnt Symbolic Expressions
We present the learnt symbolic expressions in Tables 6–9. Overall, we observe thatmufasaconsistently discovers structured
andinterpretableexpressionsthatalignwithwell-establishedfinancialvaluationprinciples,whileadaptingthemtodata-specific
and context-dependent variations.
A key observation is that the expressions discovered bymufasaclosely resemble classical financial valuation formulas, such
as discounted cash flow, book multiples and residual income models, as shown in the “Theory” column. Rather than directly
reproducing these formulas,mufasaoften recovers their core structural components (e.g.,scaling by cash flow or book value)
andaugmentsthemwithcorrectiontermsthatreflectempiricalpatternsinthedata.Thesedeviationsfromcanonicalformulasare
expectedinthefinancialsetting.Unliketheoreticalvaluationmodelsthatrelyonsimplifyingassumptions(e.g.,constantgrowth
rates or discount factors), real-world financial data is often noisy, non-stationary, and subject to market-specific distortions.
Theadditionalmultiplicativeoradditiveadjustmentslearnedbymufasacanthusbeinterpretedasdata-drivenrefinementsthat
account for such complexities, rather than arbitrary artifacts of overfitting.
In contrast, baseline methods such as PySR and FunSearch often produce expressions that are either overly complex or
difficult to interpret, lacking clear correspondence to established financial theories. Similarly, LLM-SR capture only coarse
additive relationships and fail to represent the non-linear structures commonly used in financial valuation. These comparisons
highlight thatmufasastrikes a balance between interpretability and flexibility, yielding expressions that are both theoretically
groundedandempiricallyadaptive.Importantly,weobserveconsistentstructuralpatternsacrossdifferentdatasets(e.g.,Russell
2000, STOXX 600, FTSE Asia, and CSI 300), suggesting that the learnt symbolic forms capture generalizable valuation
principles rather than dataset-specific artifacts.
Model Equation Theory Equation Theory
Fino1 EV /EBIT DA·(1 +gEP S/100) EV /EBIT DAmkt ·EBIT DA - -
Fin-R1EP S T T M·P E EP S·P EEarnings Multiple
PySR(P B mkt,mean + 0.16)·
p
|BV P S|+|e0.98 −BV P S|+ 2.09−BV P S −0.55 −2.09  −0.29- -
FunSearch2·BV P S+ 10·N I ps - -
LLM-SR0.11·(P E−Y 1)−0.01·Y 2 + 0.20·N I R i =α+β 1X1,i +β 2X2,i +· · ·Linear Factor
mufasaagents
EarningsN I ps ·P E·

1 +SustainGrowth 100  ·  1−1.12·(0.19−1.35×10 −3 ·SustainGrowth)  EP S r−g Gordon Growth
CashflowF CF ps ·EV /F CF·(1 + 0.23·(EV /EBIT DA−1.00)) P∞ t=1 F CFt (1 +r)t Discounted Cash Flow
AssetT BV P S·P B·(1−0.24·(P B−1.00))BV P S·P BBook Multiple
GrowthRevenue ps ·

1 +gRevenue
100

Revenue0 ·(1 +g)Revenue Growth
QualityEBIT DA ps ·P/F CF·

1 +EBIT DAps −46.35 100  BV+ P∞ t=1 (ROEt −r)·BV t−1 (1 +r)t Residual Income
Table 6: Learnt equations for the Russell 2000 dataset.
Model Equation Theory Equation Theory
Fino1 EV /EBIT DA·(1 +gEP S/100) EV /EBIT DAmkt ·EBIT DA - -
Fin-R1EP S T T M·P E EP S·P EEarnings Multiple
PySR

 ((−0.99 +Div−(EBIT DA+R&D+|N I|)−N I)·P B mkt,std) + (EBIT DA−(0.30·Rev+IntInc)) Shares

 + 0.68- -
FunSearch0.25·EBIT DA ps + 0.35·OCF ps + 0.20·ROE+ 0.20·BV P Slag4 - -
LLM-SR−0.01·P E+ 0.37·P B+ 0.22·(EV /EBIT) + 0.36·P B R i =α+β 1X1,i +β 2X2,i +· · ·Linear Factor
mufasaagents
Earnings N Ips ·P E·(1 +g EP S/100) 1 +EBIT DAps/100 + (P/F CF/100)·1.19 EP S r−g Gordon Growth
CashflowOCF ps ·3.88· P/F CF 5.27 ·  1 + 0.02·gEBIT DA·  1− OCF ps −6.66 0.05  P∞ t=1 F CFt (1 +r)t Discounted Cash Flow
Asset Assets−Liabilities Shares · P B 28435.60 + 1.42·LT Invest+ 5316.09·(LT Invest/Assets−12.78) BV P S·P BBook Multiple
GrowthRevenue ps ·(1 +g Revenue/100)·

1 +
 Revenueps
809734.00
34086.20!
·

1−

1− EV /EBIT DA 100  ·0.54  Revenue0 ·(1 +g)Revenue Growth
QualityN I ps ·(P E·0.86)·

1 +OCF ps,lag1/Assetslag4
100

BV+ P∞ t=1 (ROEt −r)·BV t−1 (1 +r)t Residual Income
Table 7: Learnt equations for the STOXX 600 dataset.

Model Equation Theory Equation Theory
Fino1 EV /EBIT DA·(1 +gEP S/100) EV /EBIT DAmkt ·EBIT DA - -
Fin-R1EP S T T M·P E EP S·P EEarnings Multiple
PySR 1√
e−1.27 ·log



 BV P S·Debtps −2.91×10 −3 − Debtps −InterestExpense R&D+P Bmkt,mean · 1 log(P Bmkt,mean)

 + 1.00   - -
FunSearch0.20·EBIT DA ps + 0.15·BV P Slag4 + 0.10·ROE lag8 + 0.10·EBIT ps + 0.10·EP Slag1 + 0.05· EV EBIT - -
LLM-SR5.86×10 −4 ·(EBIT−InterestExpense)−0.21·R&D−4.00×10 −3 ·GrossP rof it+ 0.76·BV P S R i =α+β 1X1,i +β 2X2,i +· · ·Linear Factor
mufasaagents
EarningsN I ps ·P E·(1 + 0.001·gEP S)·

1−1.79· σEV /EBIT
100

·

1 + 0.03·(σEV /EBIT >0.78)
 EP S
r−g Gordon Growth
CashflowOCF ps ·

1 +0.16·g EBIT
100

·
 EV /F CF
(EV /F CF)mkt
·6.87
 P∞
t=1
F CFt
(1 +r)t Discounted Cash Flow
Asset BV P Slag1 ·P B·1.34 P B BV P S·P BBook Multiple
GrowthRevenue ps ·(1 +g Revenue/100)·

1 +EV /EBIT DA−(EV /EBIT DA)mkt
(EV /EBIT DA)mkt

Revenue0 ·(1 +g)Revenue Growth
QualityN I ps ·P E·(1 +ROE/100) BV+ P∞ t=1 (ROEt −r)·BV t−1 (1 +r)t Residual Income
Table 8: Learnt equations for the FTSE Asia ex Japan dataset.
Model Equation Theory Equation Theory
Fino1 EV /EBIT DA·(1 +gEP S/100) EV /EBIT DAmkt ·EBIT DA - -
Fin-R1EP S T T M·P E EP S·P EEarnings Multiple
PySR
s

 P Bmkt,mean ·0.10·BV P S EBIT DA−0.03 + 0.17·EP S+ 0.48 + 2.16·Debtps

 +

 BV P S 0.06−GrossP rof it

 +EP S- -
FunSearch2·BV P S+ 10·N I ps - -
LLM-SR−0.02·Debt ps + 1.53×10 −4 ·g Revenue + 0.54·EV /Sales+ 0.52·Revenue ps Ri =α+β 1X1,i +β 2X2,i +· · ·Linear Factor
mufasaagents
EarningsN I ps ·(1 +g EP S/100)·(P E·3.37)·0.23 EP S r−g Gordon Growth
Cashflow0.09·P/OCF+ 4.99·OCF ps ·(1 + 852.52·(OCF ps <0))·(1 + 0.63·(P/OCF >14.69)) P∞ t=1 F CFt (1 +r)t Discounted Cash Flow
AssetBV P S·(P B−0.15·P B mkt)·1.00BV P S·P BBook Multiple
GrowthRevenue ps ·(1 +g Revenue/100)Revenue 0 ·(1 +g)Revenue Growth
QualityEBIT ps ·(1 +ROE/100)·P/F CF·

1−0.94·
 Revenueps
EBIT ps
−1

BV+ P∞ t=1 (ROEt −r)·BV t−1 (1 +r)t Residual Income
Table 9: Learnt equations for the CSI 300 dataset.
D Learnt Context Weighting
Weillustratethe learntcontext-dependentagentweightingovervaluation perspectivesinFigure4across thefivedatasets.Each
heatmap shows howmufasadynamically allocates importance to the different agent perspectives (e.g.,earnings, cash flow,
asset,growth,andquality)conditionedoncompanysectorandmarketregime(bullvs.bear).Severalconsistentpatternsemerge:
•First, the model assigns distinct weights across sectors, reflecting domain-specific valuation preferences. For example, asset-
orcashflow-basedsignalsareoftenemphasizedinsectorswithsubstantialbalancesheetcomponents(e.g.,realestate),while
earnings-based signals are frequently assigned higher weights in sectors with more stable profitability profiles.
•Second,theweightsshiftacrossbullandbearregimes,indicatingthatmufasaadaptsitsvaluationstrategytochangingmarket
conditions. For example, it can be noticed that certain perspectives (e.g.,growth or earnings) are more emphasized in some
bullish settings, while asset- or cash flow-based signals tend to receive relatively higher weights in some bearish contexts.
These patterns are not uniform, but reflect a context-dependent reallocation of importance across valuation perspectives.
•Importantly, we observe recurring tendencies across geographically distinct markets, including the U.S. (S&P 500, Russell
2000), Europe (STOXX 600), and Asia (FTSE Asia Pacific ex Japan, CSI 300), where certain valuation perspectives (e.g.,
earnings or cash flow) are frequently assigned higher importance. While the exact weighting patterns vary across sectors
and regimes, these recurring trends suggest that the learnt weighting mechanism is able to capture generalizable financial
intuitions rather than purely dataset-specific artifacts.
Overall, the results demonstrate that the meta-coordinator effectively learns to combine multiple valuation perspectives across
diverse market conditions, in a context-aware and interpretable manner.

Figure 4: Learnt agent weighting across company sectors and market regimes for all datasets.

E Distilled Agent Learnings
Earnings Agent Learnings
Summary.Beststructureusesearnings*PEwithcappedgrowth.Themostpromisingdirectionisrisk-adjustedsectorgrowthcaps.Avoid
uncapped growth and raw PE multiples due to the persistent Technology sector gap.
Key Insights
•Earnings-based structures require growth caps to avoid overprediction.
•Sector-specific adjustments are necessary for high-PE sectors.
•Raw PE-based formulations lead to systematic bias.
•Growth signals improve performance only when bounded.
Statistical Diagnostics
•Technology sector shows persistent overprediction relative to the global baseline.
•High-PE sectors exhibit systematic bias in earnings-based models.
•Growth variables without caps lead to unstable predictions.
•Performance degrades when sector variation is not accounted for.
What Works
•Using capped growth adjustments in earnings formulations.
•Applying sector-specific growth caps.
•Combining earnings with sector median PE.
•Using bounded multiplicative structures,e.g.,growth caps.
What Fails
•Using IS_EPS_GROWTH_YOY without cap.
•Using SECTOR_MEDIAN_PE without growth cap.
•Using IS_RD_EXPEND_TTM as a standalone multiplier.
•Using uncapped growth-based formulations.
Important Variables
Variable Observed Role
NET_INCOME_TTM_PER_SHARE Core earnings driver.
SECTOR_MEDIAN_PE Sector anchoring for valuation.
IS_EPS_GROWTH_YOY Growth signal requiring bounding.
IS_RD_EXPEND_TTM High-impact but unstable when standalone.
Agent Adaptation Behavior
•Introduces sector-specific growth caps after detecting overprediction.
•Replaces uncapped growth terms with bounded structures.
•Combines earnings with sector anchoring variables.
•Moves away from standalone multipliers toward structured combinations.
Design Principle.Earnings-based models require sector-aware growth caps and bounded multiplicative structures to avoid systematic
overprediction.

Cash Flow Agent Learnings
Summary.Best structure uses cash flow with a sector-adjusted EV/EBITDA multiple. The most promising direction is a Consumer
Discretionary discount factor. Avoid static multipliers without growth adjustments due to large sector gaps.
Key Insights
•Sector-specific adjustments are required to correct extreme underprediction in Consumer Discretionary.
•Growth-adjusted factors improve performance compared to static multipliers.
•Cash flow quality adjustments are needed for early-stage companies with negative cash flow.
•CF_base * (1 + growth_cap) structures outperform pure multiples by incorporating growth dynamics.
Statistical Diagnostics
•Consumer Discretionary exhibits extreme underprediction driven by growth volatility.
•Technology and Financials show systematic deviation due to differences in growth stability and regulatory complexity.
•SECTOR_MEDIAN_EV_EBITDA is unstable in asset-light companies due to denominator effects.
•Ignoring negative cash flow via max() leads to systematic underestimation in early-stage firms.
What Works
•Using sector-adjusted EV/EBITDA multiples.
•Applying growth-adjusted scaling using SALES_REV_TURN_TTM_LAG4.
•Incorporating cash flow quality adjustments for negative cash flow companies.
•Using bounded structures,e.g.,CF_base * (1 + growth_cap).
What Fails
•Using EBITDA_YOY as a standalone multiplier.
•Using static multipliers without growth adjustments.
•Ignoring negative cash flow through truncation via max().
Important Variables
Variable Observed Role
TRAIL_12M_FREE_CASH_FLOW_PER_SH Core valuation base.
SECTOR_MEDIAN_EV_EBITDA Sector-adjusted valuation multiplier.
SALES_REV_TURN_TTM_LAG4 Growth-adjustment factor with high sensitivity.
NEGATIVE_CASH_FLOW_FACTOR Adjustment for early-stage companies.
CONSUMER_DISCRETIONARY_FLAG Sector-specific discount control.
Agent Adaptation Behavior
•Introduces sector-specific discount factors after detecting extreme underprediction.
•Replaces static multipliers with growth-adjusted scaling.
•Incorporates adjustments for negative cash flow rather than truncating values.
•Proposes new combinations integrating growth, sector, and cash flow quality signals.
Design Principle.Cash flow models require sector-aware adjustments, growth scaling, and explicit handling of negative cash flow to
avoid systematic underestimation.

Asset Agent Learnings
Summary.The best structure uses multiplicative adjustment for R&D intensity and sector anchoring, avoiding invalid predictions and
leveraging high-impact variables. The most promising direction is a Technology-specific R&D multiplier. Avoid log-based adjustments
and standalone BS_CUR_LIAB multipliers due to the persistent Technology sector gap.
Key Insights
•Sector-specific multipliers are required to correct overprediction in the Technology sector.
•R&D intensity relative to assets is a high-impact adjustment factor.
•Log-based adjustments introduce invalid predictions and should be avoided.
•Liquidity adjustments improve stability in high-variance sectors.
•max(BOOK_VAL_PER_SH * x, BOOK_VAL_PER_SH - y) * max(1, z) structures outperform pure multiples.
Statistical Diagnostics
•Technology sector exhibits extreme overprediction due to overreliance on R&D multipliers.
•Log-based transformations result in invalid predictions.
•BS_CUR_LIAB as a denominator causes invalid predictions in asset-light companies.
•SECTOR_MEDIAN_P_BOOK shows high volatility in Technology, leading to high CV and MAPE.
•Consumer Staples shows underprediction due to underweighting of book value.
What Works
•Using multiplicative adjustments for R&D intensity.
•Applying sector-specific adjustments using SECTOR_MEDIAN_P_BOOK.
•Using bounded structures,e.g.,max(1, ...) to avoid invalid predictions.
•Incorporating liquidity buffer terms to reduce variance.
What Fails
•Using BS_CUR_LIAB as a standalone multiplier.
•Using log(1 + BOOK_VAL_PER_SH / SECTOR_MEDIAN_P_BOOK).
•Using BS_CUR_LIAB as a denominator in asset-light companies.
•Using unbounded R&D multipliers in the Technology sector.
Important Variables
Variable Observed Role
BOOK_VAL_PER_SH Core asset value and primary anchor.
SECTOR_MEDIAN_P_BOOK Sector anchoring variable.
BS_CUR_LIAB Liquidity risk adjustment and variance driver.
IS_RD_EXPEND_TTM R&D intensity has a high impact but is prone to overuse.
BS_TOT_ASSET Scaling factor for asset normalization.
MARKET_MEDIAN_P_BOOK Market context variable with secondary importance.
Agent Adaptation Behavior
•Introduces Technology-specific multipliers after detecting overprediction.
•Replaces log-based adjustments with bounded multiplicative structures.
•Adds liquidity buffer terms to reduce high variance.
•Explores combinations of R&D intensity and sector anchoring variables.
Design Principle.Asset-based models require bounded multiplicative structures, sector-specific adjustments, and controlled use of
high-impact variables to avoid instability and invalid predictions.

Growth Agent Learnings
Summary.The best structure uses MARKET_MEDIAN_P_FCF with growth-capped FCF scaling. The most promising direction is a
Consumer Discretionary discount factor. Avoid EBITDA_YOY as a standalone multiplier due to persistent sector misfits.
Key Insights
•Sector-specific discounts are required to correct extreme bias in Consumer Discretionary.
•Growth elasticity improves performance compared to static multiples.
•Piecewise growth structures improve flexibility over min/max formulations.
•CF_base * (1 + growth_cap) structures improve MAPE by capturing growth dynamics.
Statistical Diagnostics
•Consumer Discretionary exhibits extreme prediction error driven by FCF volatility.
•Technology sector shows systematic overestimation due to growth effects.
•TRAIL_12M_FREE_CASH_FLOW_PER_SH as a denominator causes invalid predictions.
•SECTOR_MEDIAN_P_FCF / MARKET_MEDIAN_P_FCF shows high volatility in unstable sectors.
What Works
•Using MARKET_MEDIAN_P_FCF as a core multiplier.
•Applying growth-capped scaling on free cash flow.
•Using sector-specific scaling for Consumer Discretionary.
•Replacing min/max structures with piecewise growth formulations.
What Fails
•Using EBITDA_YOY as a standalone multiplier.
•Using SALES_REV_TURN_YOY in multiplicative models.
•Using TRAIL_12M_FREE_CASH_FLOW_PER_SH as a denominator.
•Using SECTOR_MEDIAN_P_FCF / MARKET_MEDIAN_P_FCF in unstable sectors.
Important Variables
Variable Observed Role
MARKET_MEDIAN_P_FCF Core multiplier for valuation.
TRAIL_12M_FREE_CASH_FLOW_PER_SH Core growth-sensitive signal.
SECTOR_MEDIAN_P_FCF Sector adjustment factor.
MARKET_MEDIAN_P_SALES Alternative multiplier with instability in low-growth sectors.
EBITDA_TTM_PER_SHARE High-sensitivity variable with instability in high-growth sectors.
Agent Adaptation Behavior
•Introduces sector-specific discount factors after detecting extreme bias.
•Replaces min/max structures with piecewise growth formulations.
•Shifts from static multiples to growth-velocity models.
•Explores combinations of growth scaling and sector adjustment.
Design Principle.Growth-based models require sector-specific adjustments, growth elasticity, and bounded scaling to avoid instability
and extreme prediction errors.

Quality Agent Learnings
Summary.The best structure uses income * P_FCF with growth adjustments. The most promising direction is a Technology-specific
growthcap.AvoidEBITDA_TTM_PER_SHAREasastandalonemultiplierandfixedPEthresholdsduetoinstabilityingrowthregimes.
Key Insights
•Sector-specific scaling is required to reduce bias in Technology.
•Piecewise growth functions improve performance in high-return regimes.
•Sector-agnostic growth caps improve stability and reduce overfitting.
•CF_base * (1 + growth_cap) structures improve MAPE by balancing growth and stability.
•Sector-agnostic growth modifiers improve performance when applied to income * P_FCF structures.
Statistical Diagnostics
•Technology sector shows bias due to the underestimation of growth.
•Utilities show lower error driven by low growth expectations.
•RETURN_COM_EQY causes invalid predictions in asset-light companies.
•SECTOR_MEDIAN_P_FCF introduces high CV in high-growth sectors.
What Works
•Using income * P_FCF as a base structure.
•Applying piecewise growth functions instead of log growth.
•Introducing sector-agnostic growth caps.
•Using sector-specific scaling for high-growth sectors.
What Fails
•Using EBITDA_TTM_PER_SHARE as a standalone multiplier.
•Using SECTOR_MEDIAN_PE with fixed thresholds.
•Using RETURN_COM_EQY in unstable regimes without constraints.
Important Variables
Variable Observed Role
OPER_CF_TTM_PER_SHARE Strong signal when combined with P_FCF.
SECTOR_MEDIAN_P_FCF Core multiplier with sector adjustment role.
RETURN_COM_EQY Growth signal with instability in high-return regimes.
NET_INCOME_TTM_PER_SHARE Core valuation base.
SECTOR_MEDIAN_PE Alternative multiplier with overfitting risk.
EBITDA_TTM_PER_SHARE High-volatility variable with unstable performance.
Agent Adaptation Behavior
•Introduces sector-specific scaling after detecting bias in Technology.
•Replaces log growth with piecewise linear growth functions.
•Adds sector-agnostic growth caps to reduce overfitting.
•Explores combinations of income, growth, and sector multipliers.
Design Principle.Quality-based models require growth-aware scaling, bounded transformations, and sector-specific adjustments to
balance stability and predictive performance.

Analysis of Agent Learnings.We highlight consistent patterns observed across the learnings:
•Many candidate formulations fail not due to poor average accuracy, but due to instability or invalid behavior under specific
conditions. This is reflected in the statistical diagnostics such as high variance, high CV, or invalid outputs arising from
denominator effects (e.g.,cash flow or liability terms in asset-light firms). Such failure modes would not be identifiable from
scalar loss alone, highlighting the necessity of the statistical memory in guiding the search toward robust expressions.
•Instability is consistently conditional on firm type and sector interactions rather than global. For instance, sector-based
multiples exhibit high volatility in certain sectors, and variables such as free cash flow or liabilities lead to breakdowns in
early-stage or asset-light companies. This explains why a single global expression is insufficient, and also motivates the use
of context-dependent aggregation across specialized agents.
•A recurring observation is the presence of systematic over- and underestimation across sectors. For example, Technology
frequently exhibits persistent overprediction (earnings, asset, growth agents), while Consumer Discretionary shows extreme
underprediction orvolatility-driven errors (cashflow, growthagents). These directionalbiases justify theneed forsector- and
regime-aware weighting.
•Variables are rarely discarded outright, but instead require structured use to remain effective. Several high-impact features
(e.g.,growth signals, R&D intensity, sector multiples) are repeatedly identified as unstable or biased when used in isolation,
butbecomeusefulwhencombinedwithanchoringoradjustmentterms.Thisindicatesthatthestatisticaldiagnosticsnotonly
identify failure modes, but also guide the construction of stable compositions within each valuation perspective.
F Extended Ablation Study
Model Variant S&P 500 Russell 2000 STOXX 600 FTSE APAC CSI 300
Binary Memory (Pass/Fail Signals Only)
Single-Perspective Agent 0.5699 0.7527 0.7220 0.6095 0.5735
Multi-Agent (Equal Weights) 0.5466 1.0459 0.6454 0.7088 0.5599
Multi-Agent (Best Single Agent) 0.5127 1.5160 0.62120.60830.5761
Multi-Agent (Meta-Coordinator)0.4646 0.6445 0.57590.60860.5070
MAPE-Only Memory (No Additional Statistics)
Single-Perspective Agent 0.4983 0.7208 0.5858 0.5947 0.5517
Multi-Agent (Equal Weights) 0.5333 0.9027 0.5881 0.6393 0.5175
Multi-Agent (Best Single Agent) 0.51270.69480.6212 0.5926 0.5929
Multi-Agent (Meta-Coordinator)0.47020.75250.5398 0.5852 0.4852
Full Statistical Memory (Variance, Tail Risk,etc.)
Single-Perspective Agent 0.4971 0.8987 0.7608 0.6095 0.5928
Multi-Agent (Equal Weights) 0.4652 0.8831 0.5448 0.6442 0.5309
Multi-Agent (Best Single Agent) 0.4676 1.9170 0.5256 0.5833 0.4739
mufasa(Ours)0.4465 0.5718 0.5064 0.5814 0.4343
Table 10: Extended ablation study. We compare strategies under different memory settings.
We extend the ablation study on the statistical agent memory in Table 10.Single-Perspective Agentuses only a single LLM
agenttosearchforthebestexpression,Multi-Agent (Equal Weights)usemultipleagentswithouthierarchical-levelcoordination,
Multi-Agent (Best Single Agent)reports the best post-hoc performance out of the multiple agents. Across all memory settings,
Multi-Agent (Meta-Coordinator)generally achieves the strongest performance, often outperforming all of the best individual
agents. This suggests that the gain does not come simply from finding the single strongest perspective in the agent pool, but
from learning how to combine the complementary perspectives.
Across the memory variants,Binary Memoryrefers to storing past equations with binary pass/fail signals only,MAPE-Only
Memorystores their MAPE performance, whileFull Statistical Memorystores the full suite of statistical information listed in
Table 1. We find that using the full statistical memory typically result in the strongest performance across all model variants.
Full statistical memory provides information about not only the average error, but also the reliability and risk profile of each
agent’s expressions. This allows the agents to distinguish equations that perform well consistently and those that perform well
only occasionally, resulting in more robust expressions.
Overall,theresultsshowthatmufasabenefitsfromusingmulti-perspectiveagents,hierarchical-levelcoordinationandricher
statistical feedback, leading to more consistent symbolic discovery across markets. We do a deeper analysis of the statistical
memory performance in the following section.

G Additional Statistical Results
In Table 1, we show that the full statistical memory stores information such as Spearman Rank Correlation, Percentile Errors,
andMeanSignedPercentageError(MSPE),amongothers.Weperformadeeperanalysisofthedifferentstatisticalperformances
of the learnt symbolic expressions.
Figure 5: Predictedvs.True log prices across Symbolic Regression models on the S&P 500 dataset.
Spearman Correlation.Many of the learnt symbolic expressions are non-linear and multiplicative (see Table 4), and the
MAPE metric might not be fully indicative of their quality. For example, a mismatched multiplier would result in high MAPE,
but could still be correlated with the true symbolic relationship. We additionally analyze the Spearman correlation between the
predicted and true prices.
Notably,inFigure5,wefindthatMAPEandrankcorrelationcapturedifferentaspectsofperformance:PySRachievedbetter
MAPEthanFunSearchintheS&P500dataset(seeTable2)butshowslowerrankcorrelation.Thismightsuggestthatitsheuristic
search methodology fits average values without preserving meaningful structural relationships, in contrast to FunSearch, which
uses LLM reasoning.
We see fewer outlier points going from left to right, given that PySR simply fits average MAPE, while LLM methods like
FunSearch search for structural expressions but only evaluate them over the MAPE metric. Our memory structure captures a
more holistic set of statistical performances, which includes the rank correlation metric. Overall,mufasaachieved the highest
Spearman correlation.
Figure6:Errordistributionacrosssectors.Thecenterlinesshowmedianerrors,whilethetopandbottomedgesoftheboxplots
show the 25th and 75th percentile errors, respectively. Lower is better.
Error Percentiles.In Figure 6, we do a deeper analysis using a breakdown by company sectors.
mufasaachieves the strongest performance in sectors such as Utilities, Industrials, Real Estate, and Consumer Staples,
whereerrordistributionsarebothlowerandmoreconcentrated.Thesesectorsaretypicallycharacterizedbytheirfundamentals,
making them well-aligned with the accounting information used by the model. The stability of these sectors allows the model
to effectively perform symbolic discovery without being disrupted by the high variability of the stock prices used in evaluation.
Whilemufasaimproves performance across most sectors, it shows slightly higher upper- and lower-percentile errors in the
Communications and Consumer Discretionary sectors. A possible explanation is that these sectors are less directly driven by

Model 25 th pct. (↓) Median (↓) 75 th pct. (↓)
PySR 0.4103 0.6249 0.8322
FunSearch 0.6136 0.7500 0.8283
LLM-SR 0.2663 0.4475 0.6086
mufasa0.1725 0.3382 0.5556
Figure 7: Aggregate APE distributions.
fundamental signals and are more influenced by forward-looking expectations, intangible assets, and market sentiment. As a
result, it could fail to capture unexpected jumps caused by news events, which were not considered in our work. However, our
median error is still lower or close to benchmark performance in these sectors.
In general,mufasaachieves the lowest averaged errors across all percentiles of the distribution, including the median, as
shown in Table 7. Similarly, our memory structure (Table 1) also captures and learns from tail errors, allowing it to produce
more robust expressions compared to baselines.
Figure 8: Mean Signed Percentage Error across valuation quartiles (Q1: Cheap to Q4: Expensive).
DirectionalBias.InFigure8,wefurtheranalyzedirectionalbiasacrossvaluationquartiles,usingthemeansignedpercentage
error (MSPE) metric. Across all markets, we find thatmufasatends to overestimate value for cheaper companies (Q1) and
underestimate value for expensive ones (Q4).
However, compared to baselines,mufasaexhibits lower directional bias overall, with errors remaining closer to zero across
all quartiles. This indicates that the model not only improves absolute accuracy (as seen in MAPE), but also avoids systematic
mispricing across different valuation regimes.
Notably,thebiaspatternsarealsomorestableacrossmarketsformufasa,whilecompetingmethodsdisplaygreatervariability.
This might be attributed to the statistical memory, which also tracks bias-related signals such as MSPE, enabling the agent
to reduce systematic over- or under-prediction across the different price regimes. These could be seen in the distilled agent
learnings (see Statistical Diagnostics in Section E), which often mention observations on over- and under-estimations.
H Limitations of the work
The evaluation of classical valuation baselines depends on a set of modeling assumptions that are standard in finance, but
not uniquely defined. For example, our baseline methods require specifying how future cash flows or dividends evolve over
time (Damodaran 2012). In this work, we adopt commonly used approaches such as the constant-growth assumption (Gordon
1962)forconsistencyandinterpretability.Importantly,evaluatingacrossallpossibleassumptionvariantscouldbeintractablein
practice.Exploringdifferentorevenadaptivemethodstoselecttheseassumptionscouldbeapossibledirectionforfuturework.
Some components in our framework are manually designed, such as the number of agent perspectives or market contexts,
which might not capture the full range of heterogeneity present in real-world markets. However, our proposed framework is
modular and extensible: additional agents or contexts could be incorporated without modifying any of the core architecture.
Future work could also explore higher-level coordination mechanisms that adaptively decide the composition of agents and
contexts.
