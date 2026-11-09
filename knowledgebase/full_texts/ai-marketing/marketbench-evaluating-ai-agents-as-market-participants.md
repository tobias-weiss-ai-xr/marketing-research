---
title: 'MarketBench: Evaluating AI Agents as Market Participants'
url: https://arxiv.org/abs/2604.23897
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Andrey Fradkin
- Rohit Krishnan
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.23897
pages: 19
chars: 44408
fetched_at: '2026-11-08T12:59:18+00:00'
kb_version: 1
---

# MarketBench: Evaluating AI Agents as Market Participants

MarketBench:EvaluatingAIAgents
asMarketParticipants
AndreyFradkin,RohitKrishnan
April28,2026
Markets are a promising way to coordinate AI agent activity for similar reasons to those
usedtojustifymarketsmorebroadly.Inordertoeffectivelyparticipateinmarkets,agents
needtohaveinformativesignalsoftheirownabilitytosuccessfullycompleteataskand
the cost of doing so. We propose MarketBench, a benchmark for assessing whether AI
agentshavethesecapabilities.Weusea93‐tasksubsetofSWE‐benchLite,asoftwareen‐
gineeringbenchmark,withsixrecentlyreleasedLLMsasademonstration.TheseLLMs
are miscalibrated on both success probability and token usage, and auctions built from
these self‐reports diverge from a full‐information allocation. A follow‐up intervention
where we add information about capabilities from prior experiments to the context im‐
proves calibration, but only modestly narrows the gap to a full‐information benchmark.
Wealsodocumenttheperformanceofamarket‐basedscaffoldingwiththeseLLMs.Our
results point to self‐assessment as a key bottleneck for market‐style coordination of AI
agents.
AndreyFradkin:BostonUniversityandtheMITInitiativeontheDigitalEconomy.RohitKrishnan:Indepen‐
dentResearcher.
arXiv:2604.23897v1  [cs.AI]  26 Apr 2026

1. Introduction
Agent benchmarks mostly ask whether a model can finish a task. Under market‐style
rules, agents typically name a price and convey how likely they are to succeedbefore a
task is assigned, so allocation turns on self‐reported odds and expected cost, not only
on whether a run ultimately succeeds. We propose MarketBench, a benchmark for this
self‐assessmentonrealisticsoftware‐engineeringtasks.Ourinitialinstantiationuses 93
SWE‐benchLitetasksandsixrecentlyreleasedLLMs.Modelshaveweakself‐assessment:
current models are poor at forecasting both their success probability and their token
usage,andthoseerrorscarryoverintoauctionoutcomesbuiltfromthesameself‐reports.
Whyfocusonthiscapability?Multi‐agentsystemsarequicklybecomingthestandard
way to do complex work through tools such as Claude Code and OpenClaw. However,
thesesystemsarecomplexandhavead‐hocrulesfordeterminingwhenandwhichtypes
of agents are used across situations. In contrast, markets simplify complexity through
the price mechanism. They are attractive for coordinating heterogeneous agents when
task‐specificfit,cost,orspeedarelocaltotheworkerratherthanvisibletoacentralplan‐
ner.Butthislogiconlyworksifworkerscansaysomethinginformativeabouttheirown
likelyperformance.Withoutcalibratedself‐assessment,bidsarenoisyfromthestartand
downstreamallocationsuffers. 1
Onemightobjectthatthereislittlegenuinelyprivateinformationacrossmodels:fron‐
tier systems are few in number and the operator can in principle observe them directly.
Thatobjectionhastworesponses.Narrowly,heterogeneityinrealizedperformanceand
cost reflects high‐dimensional, task‐specific model behavior; even if the architecture is
public,theimpliedmappingfromatasktosuccessprobabilityandtokenuseisnotfully
predictable ex ante. More broadly, agents are bundles of a base model, execution envi‐
ronment, scaffolding, and operator‐provided state; when the operator differs from the
end user or principal, information about fit and cost is genuinely decentralized relative
toacentralmarketmaker.
MarketBenchisbasedonSWE‐benchLitesoftware‐engineeringtasks,andweintend
toextendittoothertasks.Initscurrentform,MarketBenchconsistsoftwotaskfamilies:
a. MarketBenchCalibration:Weaskagentstoforecastwhethertheycancompleteatask
in one attempt and the total token usage they expect that attempt to consume. We
thencomparethosereportstorealizedmodelrunsandmapthetokenforecastsinto
expecteddollarcostsusingmodel‐specificpricing.
b. MarketBenchAuction:Weusethe previouslyelicitedsuccessandtokenestimatesto
derive bids for a reserve‐price procurement simulation and measure the resulting
1Thisdifficultyiscompoundedbywhat Dell’Acquaetal. (2023)callthe“jaggedtechnologicalfrontier”:AI
capability boundaries are irregular and unpredictable, with models excelling at some tasks while failing at
othersofseeminglysimilardifficulty.
1

payoffsrelativetofullinformationaboutcapabilitiesandcosts.
Separately, we present an illustrative scaffold experiment that elicits beliefs to route
workacrossagents.Wefindthatthescaffoldbenefitsfromusingadiversityofagents,but
islimitedbytheweakself‐assessmentoftheseagents.Wetreatthisscaffoldasaprototype
ofasystemthatcanbeimprovedinthefuturewhenagentsimprovetheirself‐assessment
capabilities.
The rest of this paper proceeds as follows. Section2 reviews related work on multi‐
agentcoordination,LLMself‐evaluation,andmarketmechanismsforcomputationalre‐
source allocation. Section3 presents a simple model of market‐based task allocation
among heterogeneous AI agents and derives the conditions under which market coordi‐
nation outperforms fixed non‐market routing rules. Section4 introduces MarketBench,
describing the task sets, bidding protocols, evaluation metrics, and benchmark results.
Section 5 then presents our illustrative live scaffold experiment together with its empir‐
ical results. Section6 discusses the implications for AI agent design, hybrid market–AI
coordination,andthepathtowardmarket‐readyagents.
2. RelatedWork
A growing literature proposes multi‐agent LLM systems that decompose work across
role‐specializedagentsandcoordinatethroughexplicitprompting,messagepassing,and
hand‐designed workflows (Wu et al.2023; Hong et al.2023; Li et al.2023). Commercial
coding agents similarly rely on centralized scaffolds that route subtasks, manage tool
use,andimplementretrylogic( Anthropic2025;OpenAI2025).Moredynamicorchestra‐
tors replace static chains with planner–scheduler architectures, but the core paradigm
remains hierarchical: a central controller must decide decomposition, assignment, and
failure recovery (Song et al.2025; Tomašev, Franklin, and Osindero2026). Related work
alsoexploresmarket‐inspiredroutingrules.Forexample, Alazrakietal. (2026)uses“strat‐
egyauctions”toscoreagentplansandrouteworkamongheterogeneousmodels,butthis
isnotaliteralmarketmechanisminoursensebecausebidsdonotarisefromagentspric‐
ing their own expected success and cost under an incentive‐compatible allocation rule.
Our focus differs in asking whether coordination can be decentralized through market
mechanisms, taking inspiration from how markets have been used at scale in society,
andwhatagentcapabilitiessuchmechanismspresuppose.
Theideaofbid‐basedallocationinmulti‐agentsystemspredatesLLMs.Classicaldis‐
tributed AI introduced contracting and bidding protocols for task allocation, and the
computer‐systemsliteraturedevelopedmarket‐basedapproachestoallocatefungiblecom‐
putationalresources.Market‐orientedprogramming,forexample,computesallocations
viacompetitive‐equilibriumpricesinartificialeconomies( Wellman1993).Thosemecha‐
nismsworkwhenagentscanpricetheirowncostsandconstraintsaccurately.Inourset‐
2

ting, the traded object is heterogeneous cognitive labor whose quality and cost depend
onmodel,context,andtools,someaningfulbidsrequiremetacognitiveself‐assessment.
A second, related, literature evaluates frontier agents on complex tasks. A popular
example is METR’s time‐horizon methodology, which characterizes how long an agent
can sustain autonomous work at a given reliability level (Kwa et al.2025). GDPval mea‐
suresperformanceoneconomicallymeaningfultasksmappedtorealoccupationalwork
activities (Patwardhan et al.2025). The Holistic Agent Leaderboard (HAL) contributes
evaluation infrastructure that standardizes comparisons across models, scaffolds, and
benchmarks, while using large‐scale rollout logs to surface behavioral failure modes
that summary scores can miss (Kapoor et al.2025). Our closest reference isRabanser
et al.(2026), which argues that single success metrics obscure important dimensions of
agent performance and proposes a broader reliability profile spanning consistency, ro‐
bustness,predictability,andsafety.Thatpaperalsoelicitsthemodel’sconfidencethatits
answeriscorrectandevaluatesthoseforecastsusingtheBrierscore,aswedo.Nonethe‐
less,ourelicitation targetis different:we askforex antebeliefs abouttask‐level success
and expected cost, rather than confidence in the correctness of a realized answer. To‐
getherthesebenchmarksadvancemeasurementbeyondrawtasksuccesstowardtheop‐
erationalpropertiesthatdeterminewhetheragentscanbetrustedinrealdeployments.
This connects naturally to work on LLM confidence elicitation and calibration. Nu‐
merous papers document miscalibration and elicitation sensitivity (Xiong et al.2024;
Gengetal. 2024;Zhangetal. 2024).Weextendthisagendafromanswer‐levelconfidence
toagenticproduction:marketparticipationrequirescalibratedbeliefsabouttaskcomple‐
tionandexpectedcost,beyondcorrectnessalone.Finally,ourmotivationisgroundedin
classic arguments for decentralized coordination. Hayek emphasizes that prices aggre‐
gatedispersedlocalknowledge( Hayek1945).
3. ConceptualFramework
In this section, we walk through a stylized model in which the value of a market mech‐
anism for a principal looking to complete a task comes from task‐specific private infor‐
mation. We consider this framework an intuition pump, rather than a full model of a
market‐basedscaffolding.
A principal receives valuev > 0if a task is completed. There are two agents,Hand L.
AgentHisthe“better”agentonaveragebutisalsomoreexpensive:ithashigherbaseline
capability aH > aL and higher costcH > cL > 0. Each task has difficultyd. For agenti ∈
{H,L}, realized task fit isai + εi, whereεi is an idiosyncratic draw. The agent succeeds
if ai + εi ≥ d. IfF denotes the cumulative distribution function ofεi, then the ex ante
3

completionprobabilityofagent ionataskofdifficulty dis
pi(d) = 1 −F(d −ai),
so pH(d) ≥ pL(d)forevery d.
Consider first simple non‐market routing rules that ignore the task‐specific draw. If
theprincipalassignsthetaskonlytothebetteragent,theexpectedvaluenetofinference
costis
WH(d) = vpH(d) −cH,
andtheexpectedcostis
CH(d) = cH.
Ifinsteadtheprincipalassignsthetaskonlytotheworseagent,thecorrespondingobjects
are
WL(d) = vpL(d) −cL,
and
CL(d) = cL.
Thebetteragentispreferredtotheworseonewhen
v [pH(d) − pL(d)] > cH −cL.
Iftheprincipalrunsbothagentsinparallelandtakesasuccessfuloutputfromeither
one,thenunderindependenceofthetwocompletioneventstheprobabilityofsuccessis
QP(d) = 1 − (1 − pH(d)) (1 − pL(d)),
soexpectedvalueandcostare
WP(d) = vQP(d) −cH −cL
and
CP(d) = cH +cL.
Relativetoassigningonly H,parallelexecutionisworthwhilewhen v(1−pH(d))pL(d) > cL.
Relativetoassigningonly L,itisworthwhilewhen v(1 − pL(d))pH(d) > cH.Thus,parallel
executiontradesoffahighercompletionprobabilityagainstthewastecreatedbypaying
bothagents,especiallywhentheirsuccesseventsarehighlyredundant.
Now suppose that before bidding each agent observes its own task‐specific drawεi
andhencelearnswhetherthetasklieswithinitscurrentcapabilityfrontier.Tokeepthe
algebratransparent,assumethatafterobserving εi theagentknowswhetheritcancom‐
4

pletethetask,soitsrealizedcompletionprobabilityis
πi(d, εi) = 1{ai + εi ≥ d}.
Consider a success‐contingent procurement contract that paysbi only if the task is suc‐
cessfully completed. Agenti’s expected payoff from such a contract isπi(d, εi)bi − ci, so
a zero‐profit bid isbi = ci/πi(d, εi), interpreted as+∞when πi(d, εi) = 0. The principal
thereforeawardsthetasktothecheapestagentamongthosewhoknowtheycansolveit,
providedtheimpliedpaymentisbelow v.
Underindependence,thisyieldsasimpleexpressionforexpectedvalue.Let pi(d)de‐
note the ex ante probability that agenti declares itself able to solve the task. Since the
worseagentischeaper,itwinswheneveritiscapable;thebetteragentisusedonlywhen
theworseagentcannotsolvethetaskandthebetteronecan.Hencethemarketallocation
hasexpectedvalue
WM(d) = pL(d)(v −cL) + (1 − pL(d)) pH(d)(v −cH),
expectedcost
CM(d) = pL(d)cL + (1 − pL(d)) pH(d)cH,
andcompletionprobability
QM(d) = pL(d) + (1 − pL(d)) pH(d).
Themarketallocationisvaluablebecauseitconditionsonprivate,task‐specificinforma‐
tionratherthanonaveragesuccessratesalone.
Tocomparethewelfareofthedifferentallocationrulesmoretransparently,itisuseful
to work directly with ex post capability states. Letλℓh(d) = Pr(πL = ℓ, πH = h) for ℓ,h ∈
{0, 1}, where the first index refers toL and the second toH. Thusλ10 is the probability
that onlyL can solve the task,λ01 is the probability that onlyH can solve it,λ11 is the
probabilitythatbothcansolveit,and λ00 istheprobabilitythatneithercansolveit.The
expectedwelfareofthemarketmechanismcanthenbewrittenas
WM(d) = λ10(v −cL) + λ01(v −cH) + λ11(v −cL),
sincethemarketpicksthecheapestcapableagentineachstateanddoesnotallocatethe
taskwhenneitheragentcansolveit.
PROPOſıTıON 1.Suppose v > cH > cL > 0. Then the market allocation weakly dominates each
non-marketalternative.Moreover,thedominanceisstrictwheneverthereispositiveprobability
of a state in which the alternative either allocates the task to the wrong agent, pays a redundant
5

agent, or pays for an attempt when no agent can solve the task.
The intuition is straightforward. Relative to fixed assignment, the market preserves
the good states while correcting the bad ones: it usesL when onlyL can solve, usesH
when onlyHcan solve, uses the cheaper agent when both can solve, and avoids wasting
costwhenneithercansolve.Relativetoparallelexecution,themarketachievesthesame
completion outcome in every state but avoids paying redundant costs. The proof is in
AppendixB.
The assumption that agents perfectly observeεi is stronger than what practice re‐
quires. In realistic systems, agents only need a signal about likely success or cost that is
moreinformative,oratleastnotfullyredundant,relativetotheprincipal’sownsignal.If
anagent’sself‐assessmentisjustanoisyrestatementofwhattheprincipalalreadyknows,
biddingaddslittle.Butifself‐assessmentcontainsevenmodestincrementalinformation
abouttask‐specificfit,thenbiddingcanimproveallocationandreduceunnecessarypar‐
allelism.
4. MarketBench
MarketBenchisabenchmarkforAIagents’readinessformarketparticipation.Ourinitial
instantiationusesSWE‐benchLitetasks( Jimenezetal. 2024):realGitHubissue‐fixpairs
with executable test suites and a binary notion of success. Each SWE‐bench Lite task is
a single GitHub issue drawn from one of roughly a dozen mature open‐source Python
repositories (django, sympy, scikit-learn , sphinx, etc.); a given repository typi‐
cally contributes multiple tasks, so per‐repository performance priors are well‐defined.
ThenoveltyofMarketBenchliesinwhatweaskagentstorevealaboutthosetasksbefore
allocation. We study whether models can forecast their own success probabilities and
expectedresourceusewellenoughtosupportdecentralizedrouting.
4.1. Calibration
The calibration task asks a model to inspect a software‐engineering task and forecast
whether it can solve that task in one attempt, together with the total token budget it ex‐
pectstoconsume.Beforethesolveattempt,themodelispromptedasfollows:
Estimate the probability that you could complete this task correctly in one attempt.
Return JSON only with fieldsp_success (0..1), estimated_tokens_total (total
modeltokensforonefullsolveattempt), rationale (optional).
Wecomparethereported p_success torealizedpass/failoutcomesandmaptoken
forecasts into expected dollar costs using model‐specific blended pricing. Phase I uses
6

93SWE‐benchLitetasksandsixfrontiermodels,yielding558model‐taskrows.Theelic‐
itation prompt exposes the task ID, title, full problem statement, and acceptance com‐
mands, and responses are collected as strict JSON at temperature 0. Realized success
labels come from strong‐scaffold external SWE‐bench runs. By “external scaffold,” we
meanastrongerSWE‐benchexecutionenvironmentwithinteractiveshellaccess,direct
testexecutionandfeedback,structuredfileediting,andmulti‐turnrevision.
4.2. Auction
Thesecondtaskfamilyaskswhetherthoseself‐assessmentsaregoodenoughtosupport
bidding.Westudyasimplereserve‐priceprocurementsimulationinwhicheachmodel’s
bid is mechanically derived from its previously elicited success probability and token‐
costestimateratherthanfromaseparatebiddingprompt.Agivenauctiononlyincludes
one model as a participant, but is incentive‐compatible given that it is a second‐price
auctionwithanindependentlydrawnreserve.
Themodel‐specificbreakevenbidis
b∗ = tokencost +penalty × (1 − psuccess) psuccess .
The simulation uses model‐specific blended token pricing, a failure penalty of $2, and
reserve prices drawn independently from a Uniform[0, 1] distribution, with 100 reserve
drawsperrowanddeterministicseeds.Expectedprofitusesthemodel’sreported p_success ;
realizedprofitevaluatesthesamemechanicallyderivedbidagainsttheobservedpassin‐
dicator.
4.3. CalibrationResults
We begin by evaluating whether models can predict their own task success on 93 SWE‐
benchLitetasks.Table 1reportsmeanstatedsuccessprobability,realizedpassrate,Brier
skillrelativetoabase‐ratebenchmark,andtwosummarystatisticsfortokenforecasting.
The main fact from Phase I is miscalibration. All six models cluster between 75.3%
and 80.6% realized pass rates, yet their average stated success probabilities range from
61.4% to 92.9%. Gemini 3 Pro Preview is sharply overconfident, while GPT‐5.2 and GPT‐
5‐miniareunderconfidentrelativetotheirrealizedpassrates.Tosupporttheillustrative
live scaffold case study below, we select a common subset of 50 tasks that all six models
attempted; on that slice, GPT‐5.2 is the strongest single‐model baseline on the external
scaffold at 37/50 tasks, while a simple oracle that always picks the best model reaches
42/50. Token self‐estimates are also severely understated: the published global median
1Blendedpricingisasingledollars‐per‐tokenrateforeachmodel:wedividetherun’stotaldollarcostby
itstotaltokencount(inputandoutputpooled),soalltokencategoriesarevaluedatthatcommonaverage.
7

TABLE1.Calibrationon93SWE‐benchLitetasks
Model Mean p Passrate Skill Est.toks Realizedtoks
ClaudeOpus4.5 76.5% 80.6% +0.060 14,774 35,820
Gemini3ProPreview 92.9% 80.6% ‐0.111 1,801 55,969
GPT‐5.2 63.2% 80.6% ‐0.195 2,909 25,036
GPT‐5.2‐pro 66.3% 79.6% ‐0.111 2,647 3,970
ClaudeSonnet4.5 75.8% 77.4% +0.018 18,333 53,085
GPT‐5‐mini 61.4% 75.3% ‐0.305 2,595 28,276
Thepass‐ratespreadismuchnarrowerthantheconfidencespread.OnlyClaudeOpus4.5andClaudeSonnet
4.5 achieve positive Brier skill relative to a naive base‐rate forecast. The final two columns summarize the
magnitudeoftoken‐estimationerror:estimatedtokensarethemodel’sforecast,andrealizedtokensarethe
actualusageimpliedbydollarcostandmodel‐specificpricing.
estimated‐to‐actualtokenratiois0.02.Onthesame50‐taskslice,alaterCodexfollow‐up
routesthesameGPT‐5.2modelfamilythroughadifferentexecutionpath,called codex-
direct , with an 1800‐second budget; we return to that diagnostic harness comparison
below.
Wealsoassessedwhetherpromptmodificationcanpartiallyaddressthisbottleneck.
Foragiventask,wecomputedperformanceontheotherSWE‐benchtasksandprepended
it to the prompt. The performance metrics we included were pass rate, average stated
confidence, and typical token underestimation; AppendixA shows a representative ex‐
ample,andTable A1reportstheaggregatebefore‐and‐aftercalibrationsummary.Onthe
full six‐model rerun, the mean Brier score improves from 0.1835 to 0.1693 and ECE im‐
provesfrom0.1065to0.0616;tokenforecastsalsobecomelessseverelyunderstated.Even
asimpleself‐historycardthereforemakestheforecastsmoreuseful.
4.4. Reserve‐PriceAuctionResults
We next ask whether these self‐assessments, though noisy, are nevertheless sufficient
forprofitablebiddinginthereserve‐priceauctiondescribedabove.Table 2summarizes
simulatedoutcomesonthesame93‐taskcalibrationset.
Two patterns stand out. First, all models earn less than the oracle benchmark, often
by a wide margin. GPT‐5.2, for example, earns roughly $0.006 per task in realized profit
versus$0.385foritsoraclecounterpart.Second,poorcalibrationdistortsallocationeven
whenaverageprofitsremainpositive.Geminiwins84.6%ofsimulatedauctionsandearns
thelargestrealizedprofit,butthisdominanceisdrivenbyaggressivebiddingdespitethe
weak calibration signal documented above. The resulting auction is therefore far from
thefull‐informationoutcome.
The self‐knowledge follow‐up from the preceding subsection partly explains why. It
improves the underlying forecasts and shifts allocation in the predicted direction, but
8

TABLE2.Single‐modelreserve‐priceauctionoutcomes
Model N Winrate Exp.profit Realizedprofit Oracleprofit
ClaudeOpus4.5 93 28.2% $0.077 $0.080 $0.260
ClaudeSonnet4.5 93 29.3% $0.062 $0.064 $0.288
Gemini3ProPreview 93 84.6% $0.353 $0.303 $0.391
GPT‐5‐mini 93 21.6% $0.054 $0.050 $0.375
GPT‐5.2 93 5.4% $0.005 $0.006 $0.385
GPT‐5.2‐pro 93 5.3% $0.007 $0.007 $0.227
Profits are reported in dollars per task under the reserve‐auction simulation. The oracle column assumes
perfectknowledgeofwhichtasksareactuallysolvableandabstentionontherest.
the aggregate auction numbers move only at the margin (mean realized profit $0.085 to
$0.082,oraclegap0.24to0.23).Prompt‐levelself‐knowledgeisenoughtorepair whowins;
itisnotyetenoughtorepair howmuch theprincipalrecovers.Thissectiondoesnotreport
afullreserve‐distributionorpayment‐rulesensitivitysweep.Laterinformedcompetitive
auctionssuggestthatpromptframingchangedbiddingbehaviormorethanpayment‐rule
variation changed allocation accuracy. The deeper bottleneck still appears to be weak
task‐by‐taskself‐assessment.
5. IllustrativeScaffoldExperiment
5.1. Setup
Beyondthebenchmark,webuiltamarket‐inspiredscaffoldtotestwhetherthesemodel
submittedbidsimproveallocationinamulti‐agentsetting.Wecallitthe live scaffold,con‐
trasted with theexternal scaffoldused for benchmark labels and single‐model baselines.
The live scaffold treats each SWE‐bench issue as a single task and verifies a submitted
patch at the end. Each attempt is one shot — a single patch, with no interactive shell,
no test‐feedback loop, and no within‐attempt revision — but each task gets up to two at‐
tempts.Onafailedfirstattempt,ahardworker‐exclusionruleforcesthesecondattempt
to a different model. The live scaffold is therefore a case study in routing under imper‐
fectself‐assessment,notaliteralimplementationofthesuccess‐contingentprocurement
contractanalyzedinSection 3.
Our scaffold is operator‐run rather than a clean procurement auction with outside
suppliers. The operator chooses assignments, pays model‐run costs directly, and uses a
scoreas aninternalroutingheuristic.In this way,it isnota realmarketbutmarket‐like.
Thatsaid,wealsoenvisionfuturevariationswherethird‐partyagentsbidinadecentral‐
izedmannerandtheirownersbearthetokencostsincurredwhileperformingthetask.
Thescaffoldingworksasfollows.Eachavailableworkersubmitsanask,aself‐assessed
probabilityofsuccess,andanexpectedcompletiontime,althoughthecurrentimplemen‐
9

tationdoesnotyetusethetimefieldintheroutingscore(itisusedonlyasatie‐breaker).
We model the worker as expecting to receive its ask minus its cost upon winning and
successfullyexecutingthetask,andpayingapenaltyifitfails.
Theoperatorpaysexecutioncostsanddecideswhethertoassignataskandtowhom
basedonascore.Forbidder i,
Scorei = pi × (Utility −Aski) − (1 − pi) ×Penaltyi −E[Costi].
whereUtilityistheoperator’sper‐taskutility(ascaffold‐levelconstant),Ask i isbidder i’s
requestedpaymentonsuccess,andPenalty i isthescaffold’sexplicitlosswhenbidder i’s
attemptfails.2
Allbidswithpositivescoresremaineligible,andthehighest‐scoringavailableworker
receives the task. If that worker fails, the engine considers the next‐highest eligible bid.
Tasks are run with the same six frontier models used in the benchmark, a utility of 90
internal credits for every task, an explicit failure‐penalty settlement rule, a 90‐second
biddingwindow,a900‐secondexecutionlimit,andatmosttwoattemptspertask.Work‐
ers are required to submit bids on tasks, and a worker that fails a task is excluded from
retryingthatsametask.
5.2. ScaffoldPerformanceandExtensions
We evaluate the live scaffold on the common 50‐task subset introduced above. Table3
reports the published market‐versus‐solo comparison, which is best read as a scaffold‐
level comparison rather than as a clean mechanism test. “Market (our scaffold)” is the
six‐workerlive‐routingconditiondescribedabove.“SoloGPT‐5.2(ourscaffold)”usesthe
same internal scaffold but always assigns GPT‐5.2, including on retry. “Solo GPT‐5.2 (ex‐
ternal scaffold)” is the stronger SWE‐bench baseline from Section4, and the oracle ceil‐
ing asks what pass rate an omniscient router could reach on the external scaffold by al‐
wayspickingtherightmodelforeachtask.
The market‐versus‐solo comparison keeps the task slice and run policy fixed, but it
does not keep the worker pool fixed. Specifically, both conditions use the same 50 tasks,
verifier,900‐secondexecutionlimit,andcapoftwoattemptspertask.Butthemarketcon‐
dition has access to a six‐model worker pool and can route a retry to a different model,
whereasthesoloconditionalwaysusesGPT‐5.2.Underthoseconditions,themarketout‐
performsthesame‐scaffoldsolobaselineby5tasks,or10percentagepoints.18tasksare
solved by both systems, 11 by the market only, 6 by solo GPT‐5.2 only, and 15 by neither.
That pattern is consistent with gains from model diversity and retry, but the p‐value for
2In the implementation, the failure penalty is itself a function of the bidder’s statedpi: Penaltyi = ρ ⋅
Utility⋅ (0.5 +pi),with ρafixedscaffoldparameter.Overconfidentbiddersthereforefaceaheavierexpected
lossonfailure.
10

TABLE3.Illustrativelivescaffoldexperimentresultson50commontasks
Executionparadigm Passrate Passes
Market(ourscaffold) 58.0% 29/50
SoloGPT‐5.2(ourscaffold) 48.0% 24/50
SoloGPT‐5.2(externalscaffold) 74.0% 37/50
Oracleceiling(externalscaffold) 84.0% 42/50
Thesame‐scaffoldcomparisonkeepsthetaskslice,verifier,timeout,andtwo‐attemptcapfixed,butnotthe
worker pool: the market condition uses six workers and diverse‐model retry, whereas the solo condition
alwaysusesGPT‐5.2.
TABLE4.AlternativeScaffoldSpecifications
Follow‐up Passrate Passes
Matchedcentralizedrouter 54.0% 27/50
Matchedmarketrerun 46.0% 23/50
Marketwithself‐knowledgebiddingprior 56.0% 28/50
Codex+GPT‐5.2(1800sbudget) 70.0% 35/50
Allrowsusethecommon50‐taskslice.Thematchedcentralized‐routerandmatchedmarketrerunkeepthe
same six workers, verifier, and 900‐second execution limit. The self‐knowledge market row changes only
the private bidding context by adding a held‐out calibration prior and bidding guardrails before bidding.
TheCodexrowchangesbothexecutionpathandbudget,soitisadiagnosticratherthananapples‐to‐apples
replacementforthepublishedbenchmark.
the difference in means is0.3, so we cannot reject the hypothesis that the two systems
areequivalentonthisslice.Wethereforetreatthiscomparisonassuggestive—adiverse
worker pool plausibly helps on our scaffold — and rest the paper’s main claims on the
calibrationevidenceinSection 4ratherthanonthescaffold‐levelpass‐rategap.
Table3alsodemonstratestheunderperformanceofthelivescaffoldrelativetoexter‐
nal scaffolds: the same GPT‐5.2 loses 26 percentage points (13 tasks, 74% vs. 48%) when
movedfromtheexternalscaffoldtoours.Thereasonforthisdifferenceisthattheexter‐
nalscaffoldgivesthemodelaninteractiveshell,directtestexecutionandfeedback,multi‐
turniteration,andstructuredfile‐editingtools;thelivescaffoldoffersnoneoftheseand
limits each worker to a single patch (raw diff orBEGIN_FILE block) per attempt. The
marketrecoversabout10percentagepointsofthatgapthroughmodeldiversity;therest
wouldrequirescaffoldupgrades,notbetterbidding.
ThemarketrunalsousedmorecomputethansoloGPT‐5.2,becausemultipleworkers
inspecteachtaskbeforeclearingandsometaskstakeasecondattempt:about5.82Mtotal
tokensforthemarketrunversus4.37Mforthesolobaseline(200.8Kversus182.2Ktokens
persuccessfulpass).
There are two explanations for why our market scaffold can beat a solo model: the
market‐clearingrule,andthediverseworkerpool.
11

To separate these explanations, we ran a follow‐up that keeps everything identical,
butreplacesthemarket‐clearingrulewithacentralizedrouter.TherouterisasingleLLM
call(GPT‐5.2‐pro)thatreadsthetaskdescriptions,theavailableworkerswiththeirmodel
identifiers, expected cost hints, retry‐exclusion constraints, and other available context
such as discussion notes and worker reputation summaries, and then directly assigns a
workertoeachtask.Theassignedworkerstillexecutesthetaskthroughthesamepathas
inthemarketcondition;theonlydifferenceiswhochoosestheassignment.Underthose
matchedconditions,thecentralizedrouterreaches27/50whilethemarketreaches23/50.
The gain from the published market comparison therefore appears to come primarily
from model diversity rather than from the present bidding rule. This shouldn’t be sur‐
prising,sincemodelsperformpoorlyinself‐assessmentasmeasuredbyMarketBench.
Itisworthflaggingdirectlythatthe“Market(ourscaffold)”rowinTable 3(29/50)and
the “Matched market rerun” row in Table4 (23/50) are nominally the same condition,
run twice. The 6‐task gap between them is itself informative: at this sample size, run‐to‐
run variation from stochastic bids, retry ordering, and execution‐path noise is on the
sameorderasthedifferencesbetweenscaffoldswearetryingtomeasure.Comparisons
acrossrowsofTable 4shouldbereadwiththatnoisefloorinmind,andanysingle50‐task
scaffoldevaluation—oursincluded—shouldbetreatedasimpreciseonitsown.
Ifoverconfidentbiddingisthebottleneck,canbetterpriorshelp?Totestthis,weran
asecondfollow‐upthatkeepsthemarket‐clearingrulebutchangesonlytheprivatebid‐
ding context: each worker receives a held‐out calibration prior before bidding, summa‐
rizingitsownhistoricalpassrateandoverconfidencetendency.Thehard‐priorrule(for
therelatedcalibrationcardseeAppendix A)startsfromtheheld‐outpassrateminusany
historical overconfidence gap, then asks the worker to raisep_success only when the
current task gives direct evidence that it is easier than the held‐out average. Under that
intervention,themarketreaches28/50—upfrom23/50inthematchedrerunandslightly
abovethecentralizedrouterat27/50.Thisissuggestivethatbetterself‐knowledgewould
yieldevengreaterperformancebenefits.
Sensitivity to execution harness and time budget.Aseparatequestionishowmuchthelive
scaffold’s weaker execution environment constrains all of these results. To probe this,
weranadiagnosticonthesame50‐tasksliceusingGPT‐5.2throughadifferentexecution
route,calledthe codex-direct workerpath,withtheper‐tasklimitdoubledfrom900to
1800seconds.Underthosechangedconditions,thefollow‐upreaches35/50passes,com‐
pared to 23–29/50 for our market scaffold and 24/50 for solo GPT‐5.2 in our scaffold. The
costpictureisverydifferent,however.The codex-direct runconsumes321.3million
2The main driver of the market’s drop in the matched rerun is Gemini. Gemini bids aggressively, so the
market selects it more often. But its realized performance is weak. This is a bid‐calibration problem: an
overconfidentworkercrowdsoutbetter‐suitedalternatives.
12

total tokens, versus 4.37 million for the solo GPT‐5.2 run and 5.82 million for the market
run—roughly55–75 ×morecomputefor,atmost,a12‐taskimprovementoverourmarket
scaffoldandan11‐taskimprovementoversoloGPT‐5.2.
Two observations follow. First, when comparing models or scaffolds, the execution
path is first order: routing and bidding choices that move pass rates by a few tasks are
dwarfedbyexecution‐environmenteffects.Second,thesteeptokencostofthosegainsis
itself a reason to care about market‐style coordination: if substantial pass‐rate improve‐
ments available at the frontier come with order‐of‐magnitude compute increases, then
mechanismsthatrouteonlythetasksthatneedthatbudgettotheexpensivepathbecome
economicallyimportantratherthancosmetic.
6. Discussion
AsthenumberandvarietyofAIagentsbeingusedinproductionincreasesexponentially,
identifying ways for them to efficiently and successfully collaborate on hard problems
becomes a key bottleneck. For human agents, markets emerged as the dominant mech‐
anismforthiskindofcoordination,andtherearereasonstoexpectasimilarroleforAI
agents.
Yet current agents do not know enough about their own production functions. They
can solve complex tasks, but they cannot reliably say in advance which tasks they can
solve, how likely they are to succeed, and what the attempt will cost. But that informa‐
tion is exactly what a market is supposed to aggregate. If bids do not reflect informed
private information, the price system cannot do its job. Even though a brief summary
of a model’s own past behavior materially improves calibration, it is still far from the
theoreticalmaximum.
Theseobservationssuggestthattheoptimalsolutionforcoordinatingagentswilllikely
be a combination of markets and AI. Markets are useful when knowledge is local, dis‐
persed, and hard to centralize. That description fits agentic work rather well. Different
models have different strengths, different tool use, different failure modes, and differ‐
entcosts.Butwithimperfectself‐knowledgeandbehavior,agentsmaynotbereliablein
theirownassessmentsoftheirabilities.TheroleofAIinsuchasystemistoaugmentthe
market,scoringagentbidsbasedonmorecentralizedsourcesofinformation,especially
aboutthetrustworthinessofanagent’sbids.
An analogy to other types of auctions is useful. In procurement, buyers often care
about more than price. They care about quality, speed, reliability, and other attributes
ofperformance.Scoringauctionshandlethatproblemdirectly:thewinneristhebidder
offeringthebestcombinationofpriceandnon‐pricecharacteristics( Che1993).Similarly,
adauctionscombinethisideawithastatisticalmodelofrelevance( Varian2007).
A mature market for AI agents is likely to work similarly. An agent that is cheap but
13

unreliable should have a low quality score. In contrast, an agent that is more expensive
but bids accurately may be the efficient choice. When multiple agents bid, a scoring
function should appropriately weigh the bids to determine the winner. Concretely, the
qualityscoreinsuchamarketcouldcombineanagent’sheld‐outcalibrationrecordona
benchmarklikeMarketBench(howwellitsstated psuccesshastrackedrealizedoutcomes),
domain‐specificreputationaggregatedacrosspasttasksofsimilartype,and,whereveri‐
ficationispossible,therateatwhichathird‐partyverifieraccepteditsoutputs.Theseare
exactly the inputs that a centralized router currently uses ad hoc; making them explicit
andtradeableacrossoperatorsiswhatwouldturntheexistingscaffoldsintoamarket.
Recentevaluationsalsoshowthatmeasuredagentperformancecankeepimproving
at much larger inference budgets than standard setups typically allow (AI Security In‐
stitute 2026), and our owncodex-direct diagnostic in Section5 points the same way:
doubling the per‐task budget and changing the execution path adds substantial passes
at the price of roughly two orders of magnitude more compute. If pass‐rate gains at the
frontiercomefromspendingmorecomputeonaper‐taskbasis,thenasinglescalarbid
that quotes one expected cost is the wrong object. The right object is closer to a produc‐
tion schedule: a mapping from token budget to expected success probability, expected
wall‐clocktime,andasketchofhowtheagentwouldallocatethatcomputeacrosssearch,
tool use, and revision. A market that elicits such schedules can in principle let the prin‐
cipal buy the right point on each agent’s cost‐quality frontier, instead of being locked
intowhicheverbudgettheagenthappenedtoassumewhenitbid.Wedonotdevelopthis
here,butweviewitasthenaturalnextsteponceself‐assessmentofscalarsuccessisitself
reliableenoughtobuildon.
Theagendathatweproposehasthefollowingnextsteps.First,self‐assessmentshould
becomeatargetof trainingandevaluationinitsown right.Calibration,abstention,and
budgetdisciplineinbiddingarecorecapabilitiesfordecentralizedcoordination.Second,
richer market institutions will need to arise, including reputation, escrow, and other
mechanisms. Third, this benchmark should be extended beyond software engineering
intoothercomplexsettings.
References
AI Security Institute. 2026. “Evidence for inference scaling in AI cyber tasks: Increased
evaluation budgets reveal higher success rates.” AISI Blog. https://www.aisi.gov.
uk/blog/evidence-for-inference-scaling-in-ai-cyber-tasks-increased-
evaluation-budgets-reveal-higher-success-rates .
Alazraki,Lisa,WilliamF.Shen,YoramBachrach,andAkhilMathur.2026. “ScalingSmallAgents
Through Strategy Auctions.” arXiv preprint arXiv:2602.02751https://arxiv.org/abs/
2602.02751.
Anthropic.2025. “ClaudeCode.” https://docs.anthropic.com/en/docs/claude-code .
14

Che,Yeon‐Koo.1993. “DesignCompetitionThroughMultidimensionalAuctions.” The RAND Jour-
nal of Economics24(4):668–680.
Dell’Acqua,Fabrizio,EdwardMcFowlandIII,EthanR.Mollick,HilaLifshitz‐Assaf,KatherineKel‐
logg, Saran Rajendran, Lisa Krayer, François Candelon, and Karim R. Lakhani. 2023. “Navi‐
gatingtheJaggedTechnologicalFrontier:FieldExperimentalEvidenceoftheEffectsofAIon
KnowledgeWorkerProductivityandQuality.” Harvard Business School Technology & Operations
Mgt. Unit Working Paper(24‐013).
Geng, Jiahui, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, and Iryna Gurevych. 2024.
“ASurveyofConfidenceEstimationandCalibrationinLargeLanguageModels.”.
Hayek,FriedrichA.1945. “TheUseofKnowledgeinSociety.” TheAmericanEconomicReview 35(4):
519–530.
Hong,Sirui,MingchenZhuge,JonathanChen,XiawuZheng,YuhengCheng,CeyaoZhang,Jinlin
Wang,ZiliWang,StevenKaShingYau,ZijuanLin,etal.2023. “MetaGPT:MetaProgramming
forAMulti‐AgentCollaborativeFramework.” arXiv preprint arXiv:2308.00352.
Jimenez,CarlosE.,JohnYang,AlexanderWettig,ShunyuYao,KexinPei,OfirPress,andKarthikR.
Narasimhan. 2024. “SWE‐bench: Can Language Models Resolve Real‐world GitHub Issues?”
In The Twelfth International Conference on Learning Representations. https://openreview.
net/forum?id=VTF8yNQM66 .
Kapoor, Sayash, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir, Zachary S. Siegel, Boyi Wei, Tianci
Xue,ZiruChen,FelixChen,SaitejaUtpala,etal.2025. “HolisticAgentLeaderboard:TheMiss‐
ingInfrastructureforAIAgentEvaluation.” arXiv preprint arXiv:2510.11977https://arxiv.
org/abs/2510.11977.
Kwa, Thomas, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar,
MeganKinniment,NateRush,SydneyVonArx,etal.2025. “Measuringaiabilitytocomplete
longtasks.” arXiv preprint arXiv:2503.14499.
Li, Guohao, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard
Ghanem. 2023. “CAMEL: Communicative Agents for “Mind” Exploration of Large Language
ModelSociety.” arXiv preprint arXiv:2303.17760.
OpenAI.2025. “Codex.” https://openai.com/index/introducing-codex/ .
Patwardhan, Tejal, Rachel Dias, Elizabeth Proehl, Grace Kim, Michele Wang, Olivia Watkins,
Simón Posada Fishman, Marwan Aljubeh, Phoebe Thacker, Laurance Fauconnet, et al. 2025.
“GDPval: Evaluating AI Model Performance on Real‐World Economically Valuable Tasks.”
arXiv preprint arXiv:2510.04374https://arxiv.org/abs/2510.04374.
Rabanser, Stephan, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, and Arvind
Narayanan.2026. “TowardsaScienceofAIAgentReliability.” arXiv preprint arXiv:2602.16666
https://arxiv.org/abs/2602.16666.
Song, Xinyuan, Zeyu Wang, Siyi Wu, Tianyu Shi, and Lynn Ai. 2025. “Gradientsys: A Multi‐Agent
LLM Scheduler with ReAct Orchestration.”arXiv preprint arXiv:2507.06520https://arxiv.
org/abs/2507.06520.
Tomašev,Nenad,MatijaFranklin,andSimonOsindero.2026. “IntelligentAIDelegation.” https:
//arxiv.org/abs/2602.11865.
Varian, Hal R. 2007. “Position Auctions.”International Journal of Industrial Organization25 (6):
1163–1178.
15

Wellman, Michael P. 1993. “A market‐oriented programming environment and its application to
distributedmulticommodityflowproblems.” Journal of artificial intelligence research1:1–23.
Wu, Qingyun, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xu Zhang,
Siru Wang, Shujian Zhang, et al. 2023. “AutoGen: Enabling Next‐Gen LLM Applications via
Multi‐AgentConversation.” arXiv preprint arXiv:2308.08155.
Xiong, Miao, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, and Bryan Hooi. 2024. “Can
LLMsExpressTheirUncertainty?AnEmpiricalEvaluationofConfidenceElicitationinLarge
LanguageModels.” arXiv preprint arXiv:2306.13063.
Zhang, Mozhi, Mianqiu Huang, Rundong Shi, Linsen Guo, Chong Peng, Peng Yan, Yaqian Zhou,
and Xipeng Qiu. 2024. “Calibrating the Confidence of Large Language Models by Eliciting
Fidelity.” InProceedings of the 2024 Conference on Empirical Methods in Natural Language Pro-
cessing.
AppendixA. Self‐KnowledgeCardforDirectCalibration
Theself‐knowledgecalibrationfollow‐upprependedashortheld‐outhistorycardbefore
the standard direct calibration prompt. The exact numbers varied by model and by the
held‐outtasksavailableforthatmodel.
SWE‐benchinstancesaredrawnfromrealopen‐sourcerepositories,notsynthetictoy
problems. Task identifiers follow the usual convention: for example,sympy__sympy-
17630 denotes an issue from thesympy/sympy repository. The main experiments use
a fixed 93‐task subset of MarketBench; that subset contains multiple tasks from some
repositories, rather than a single task per repository. When we form the self‐knowledge
card for a given evaluation task, the held‐out statistics exclude the current task. The
figure “across 92 held‐out tasks” aggregates all other tasks in this setup for the same
model,spanningeveryrepositoryrepresentedinthesubset.Theline“onpriortasksfrom
sympy/sympy(21held‐outtasks)”isthesame‐repositorysliceofthatpool:amongthose
92 tasks, the ones that also come fromsympy/sympy. The repository‐specific line was
includedonlywhentherewasenoughheld‐outdataforthatrepository.
Thetemplateforthecardwas:
Usethehistoricalself‐knowledgesummarybelowasapriorforthismodel.
These statistics come from held‐out MarketBench tasks for this same model and ex‐
cludethecurrenttask.
Historicalself‐knowledgesummary:
• Across {N_held} held‐outtasks,yourpassratewas {pass_rate} .
• Yourmeanpreviouslystatedsuccessprobabilitywas {mean_p} ;youwerehistor‐
ically {over} or {under} confidentby {gap}.
• Youractualsolve‐tokenusagewastypically {ratio}xyourestimate.
16

TABLEA1.Aggregatesix‐modelcalibrationsummarywiththeself‐knowledgecard
Promptcondition Mean p Passrate Skill Est./actualtoks
Directcalibrationprompt 72.7% 79.0% −0.107 0.1929
Self‐knowledgecard+directprompt 80.6% 79.0% −0.022 0.2501
Bothrowsaggregatethesamesix‐model,93‐tasksetupratherthanreportingasinglemodel.“Skill”isaggre‐
gateBrierskillrelativetoabase‐ratebenchmark.“Est./actualtoks”isthemedianestimated‐to‐actualtoken
ratio,solargervaluesindicatelesssevereunderestimation.ThecorrespondingECEvalues,reportedinthe
text,improvefrom0.1065to0.0616.
• (Included when ≥5 held-out tasks from the same repository were available.)On prior
tasksfrom {repo} ({N_repo} held‐outtasks),yourpassratewas {repo_pass_rate}
andyourmeanstatedsuccessprobabilitywas {repo_mean_p} .
Startfromthesehistoricaltendencies,thenupdateusingthespecificevidenceinthe
currenttask.
Be willing to move away from the historical average when the task details clearly
supportit.
Atruntime,placeholderswerefilledpermodelusingleave‐one‐outstatisticsoverthe
93‐task calibration set:{N_held} was typically 92 (93 minus the current task, adjusted
for any missing rows for that model). Because SWE‐bench Lite tasks cluster by source
repository, the optional per‐repository line gave the model a more task‐relevant prior
whenenoughsame‐repodataexisted.
As a concrete example, the card saved for Claude Opus 4.5 on thesympy__sympy-
17630instancehad {N_held} =92, {pass_rate} =81.5%, {mean_p} =76.6%(undercon‐
fidentby4.9%), {ratio}=2.4x,andtheper‐repositorylinecovered21held‐out sympy/sympy
tasks(passrate85.7%,meanstatedprobability68.0%).
ThiscardwasthenfollowedbythesamedirectcalibrationpromptshowninSection 4.
Thelive‐scaffoldbiddingfollow‐upusedthesameheld‐outhistoryidea,butconvertedit
intothestricterhard‐priorbidruledescribedinSection 5.
AppendixB. ProofofProposition 1
PROOF. Underthethreealternativemechanisms,expectedwelfareis
WH(d) = λ10(−cH) + λ01(v −cH) + λ11(v −cH) + λ00(−cH),
WL(d) = λ10(v −cL) + λ01(−cL) + λ11(v −cL) + λ00(−cL),
and
WP(d) = (λ10 + λ01 + λ11)v −cH −cL.
17

Subtractingfrommarketwelfareyields
WM(d) −WH(d) = λ10(v +cH −cL) + λ11(cH −cL) + λ00cH,
WM(d) −WL(d) = λ01(v +cL −cH) + λ00cL,
and
WM(d) −WP(d) = λ10cH + λ01cL + λ11cH + λ00(cH +cL).
Each expression is weakly positive whenv > cH > cL > 0, and it is strictly positive when‐
everthecorrespondingalternativemakesamistakewithpositiveprobability.
18
