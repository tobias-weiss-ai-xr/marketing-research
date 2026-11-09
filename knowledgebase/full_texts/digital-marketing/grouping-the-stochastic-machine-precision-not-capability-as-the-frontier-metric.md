---
title: 'Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems'
url: https://arxiv.org/abs/2608.19140
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- George Andrikopoulos
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.19140
pages: 6
chars: 23568
fetched_at: '2026-11-08T13:21:43+00:00'
kb_version: 1
---

# Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems

GroupingtheStochasticMachine
Precision,NotCapability,astheFrontierMetricforAISystems
GeorgeAndrikopoulos
Independentresearcher,London,UnitedKingdom
https://github.com/george-andrikopoulos
August2026
Abstract
Frontierlanguagemodelsarecompared,marketed,andbenchmarkedoncapability—whattheir
bestoraverageoutputcanachieve. Iarguethismeasuresthewrongaxis. Themodelshavesaturated
accuracy: theirmeanoutputlandsonthetarget. Whatnowseparatesonesystemfromanotherin
practice—andwhatdetermineswhetherasystemisusableforengineeringwork—is precision: how
tightlyconcentratedtheiroutputsarearoundthattargetacrossrepeated,identicalrequests. Borrow-
ingthemarksman’sdistinction, capabilityiswheretheaverageshotlands; reliabilityisthesizeof
thegroup. Imakethreeclaims. First,precision,notcapability,isthefrontierdifferentiatorbetween
systems(Devin,Claude,Grok,andtheirsuccessors),andtheindustry’sbenchmarkculturesystemati-
callyfailstomeasureitbecausebenchmarksreportcentraltendency,notspread. Second,precisionis
measurable,cheaplyandwithoutcircularity,byrunningafixedsuiteof deterministically scoredtasks
manytimesatfixedtemperatureandcomputingtheper-taskconsistencyofoutcomes—nomodel-in-
the-loopgraderrequired. Third,themeasurementisnotmerelydescriptivebutdecision-guiding: it
separates consistentfailures(atightgroupoff-centre,correctablebytheoperatingdisciplineofPaper
1—asightadjustment)from scatteredfailures(awidegroup,correctableonlybychangingthemodel
oritssampling—arifleproblem). Idefineagroupingmetric,specifyaharnessthatreusesexisting
challenge-trialinfrastructure,andshowhowtrackingahuman-AIpair’sgroupingovertimeyieldsthe
compoundingsignalthatPaper1’sfieldstudyrequires. Afirstrealrun,sincereplicated,illustrates
boththemethodanditsmostimportantlimit: onemeasuredgapwasclosedcompletelybyasingle
rule(0/5→5/5),whileasuiteoftasks authored from the rules themselves foundnovalue,because
afrontiermodelalreadyembodiesexplicitgoodpractice—establishingthatadiscipline’sworthis
foundbymeasurementonrealwork,notconstructedfromitsownrulebook.
1 Thewrongaxis
Ask which model is “best” and the answer ar-
rivesinthelanguageofcapability: benchmark
scores, reasoning depth, context length, the
impressiveness of the best output anyone has
coaxedoutofit. Thislanguagedescribeswhere
theaverageshotlands. Itissilentontheques-
tioneverypractitioneractuallyliveswith: will
it do this again, the same way , the next time I
ask?
Thetwoquestionsarethemarksman’stwoaxes,
and they are independent.Accuracy is close-
ness of the mean to the target — bias.Pre-
cisionis the tightness of the grouping — vari-
ance. A rifle can be accurate and imprecise
(shots centred on the bullseye but widely scat-
tered)orpreciseandinaccurate(atightcluster
inthecorner). Theyarenotthesameproperty,
theyarenotmeasuredthesameway,and—the
pointofthispaper—theyhavedivergedinex-
actlythismanneracrossthefrontier. Thelead-
ingmodelshaveconvergedonaccuracy: fora
well-specifiedengineeringtask,the bestoutput
of any of them is excellent, and theiraverage
outputisontarget. Whatseparatesthemisthe
width of the group. One returns a correct, id-
iomaticsolutionninetimesintenandsomething
wild on the tenth; another is merely good but
almostneverwild. Forproductionengineering
thesecondismorevaluable, andnocapability
benchmarkwilltellyouso.
ThisconnectsdirectlytoPaper1’sruletojudge
the tail, not the average. Here I make the
sharper claim: the tailis the group, precision
isthefrontiermetric,andthefailureofthefield
is that it advertises capability-at-best while its
userssuffercapability-in-expectation.
2 Why skills presuppose precision:
thezeroingargument
Thereisareasonprecision,notaccuracy,isthe
propertythatmattersforasystemthatwillbe
operatedratherthanmerelyadmired. Inmarks-
manshipyoucanzeroatightgroup: iftheshots
cluster but land low and left, you adjust the
sightsandthewholeclustermovesontocentre.
Youcannotzeroascatteredgroup—thereisno
adjustmentthatcorrectsshotslandingindiffer-
1
arXiv:2608.19140v1  [cs.AI]  19 Aug 2026

Accurate,precise
ontarget,tight
Accurate,imprecise
centred,scattered
Inaccurate,precise
tight,off-centre
Inaccurate,imprecise
scatteredandoff
Thetwoaxesareindependent. Capabilitybenchmarksreportthefirst;productionreliabilityde-
pendsonthesecond. ThelibraryofPaper1movesagroupontothetarget—itcannottightenone.
Figure 1:Accuracyiswherethemeanshotlands; precisionisthesizeofthegroup. Frontiermodelshave
convergedonthefirstandstilldifferonthesecond,whichistheaxisthispaperarguesshoulddecideselection.
entplaces,becausethereisnothingconsistent
tocorrect.
Paper 1’s operating discipline — versioned
skills,theerrorloop,“adjustthesights,notthe
memory”—issight-zeroing. Itmovesagroup-
ingontothetarget. Ittherefore presupposes a
precision floor.Askillcanmakeaprecisemodel
accurate; itcannotrescueascatteredone, be-
cause a correction written against a scattered
errornevergeneralises—theerrordoesnotre-
cur in the same place, so the rule never fires
againstthesamemisstwice. Thisyieldsaclean
divisionoflabourandacleandecisionrule:
• The model’s job is precision — a tight
group.
• Theoperator’sjob,throughskills,isaccu-
racy—zeroingthatgroupontothetarget.
Andtherefore: beforeinvestinginguardrails
for a failure, measure whether the failure
is consistent. A consistent failure is a tight
groupoff-centre—writetheskill,zeroit.Ascat-
teredfailureisawidegroup—noskillwillhelp;
change the rifle (model, or sampling tempera-
ture). Themeasurementin§4iswhattellsthe
twoapart.
3 Related work and the precise
claim
Theingredientsexist.Repeated-samplingevalu-
ationisestablished: pass@kmeasureswhether
anyofksamplessucceeds,anditsseverecousin
—theprobabilitythat allksucceed—isacon-
sistencymeasure[1]. Self-consistencyexploits
output variance deliberately [2]. On the arti-
factside, theinstructionlibrarieswhosevalue
this paper sets out to price are now a docu-
mented practice: Jiang and Nam characterise
thepersistentrulefilesdeveloperswriteforcod-
ingassistantsacross401open-sourcereposito-
ries [4], which establishes that such libraries
exist at scale but not what they are worth.
The reliability and evaluation literature is in-
creasingly aware that single-shot benchmark-
ingoverstatesdeployedperformance,andtem-
perature’s role in the accuracy-diversity trade-
off is well understood. Zhou et al. put the
sharpest version of this on record: across sev-
eral model families, scaling and instruction-
tuning raised average performance whilelow-
eringreliability—larger,shaped-upmodelsde-
clinedfewerquestionsandreturnedconfident,
plausible,wronganswersmoreoften,including
onitemstheirhumansupervisorsfailedtocatch
[5]. Thatisthestrongestexistingstatementof
thepremisethispaperbeginsfrom:themeanis
notthequantitythatmatters. WhatIhavenot
found stated plainly is theframing— that pre-
cisionistheaxisonwhichfrontiersystemsnow
differandshouldbeselected—coupledtoan op-
erational consequence: that measured consis-
tencypredictswhethertheoperatingdiscipline
ofPaper1canhelpatall. Myclaimisnarrow
andpractical: notthatvarianceisunmeasured
intheliterature,butthatitisthedecisiveselec-
tioncriterioninpractice,thatitischeaplymea-
surable without a stochastic grader, and that
itsmeasurementisadecisionprocedureforthe
human-AI operating loop, not merely a leader-
boardcolumn.
4 Measuringthegroup
The clean move: score deterministically.
Precisioncannotbemeasuredwithamodel-in-
the-loopgrader, becausetherulerwoulditself
scatterandthemeasurementwouldinheritthe
circularity that dooms self-graded evaluation.
Theescapeistomeasuregroupingonlyontasks
with a deterministic, binary outcome: does it
compile, do the tests pass, is the linter clean,
doesittypecheck. Thesesignalshavenomodel
inthescoringloop;theyarecheap,repeatable,
andbeyonddispute.
The harness. Fix a small suite of verifiable
tasksT={t_1…t_m}. Fixacandidateconfig-
2

Runtask N ×,
freshagents,de-
terministicscorer
pi ≈ 1? Keep
Dothefailures
shareonecause?
Zeroable
writetherule
Notzeroable
changemodel
ortemperature
yes
no
yes no
The pass rate screens; the causes decide. A
low-but-nonzero rate whose failures share
one cause is a tight group with a stray shot.
Figure 2:Thecorrectedprocedure. Anearlierver-
sionofthispaperkeyedthediagnosisonthepassrate
alone;thereplicationin§4.1showedthataratethe
naiverulecalledscatterwasclosedcompletelybya
singlerule.
uration C — a model, optionally with the skill
library loaded (thepair), at a fixed, recorded
samplingtemperature. Foreachtask,runitN
times on fresh, independent agents, recording
the binary outcome of each run. This reuses,
essentially unchanged, the challenge-trial har-
nessofPaper1: independentfresh-agentruns
ofafixedtask,differingonlyinthattheaxisof
variationistherandomseed,notthepresence
ofarule.
The metrics. For task t_i let p_i be the ob-
served pass rate over N runs. -Accuracy of
Coverthesuite: themeanpassrate,mean(p_i).
Howmanytargetsarehit. - Precision/group-
ing score: the fraction of tasks that landde-
cisively — p_i ≥ (1−ε) or p_i ≤ ε for a small
ε (e.g. tasks passing ≥9/10 or ≤1/10). A high
groupingscoremeansoutcomesareconsistent,
whicheverwaytheyfall;themushymiddle(p_i
near 0.5) is scatter. Per-task scatter is well
summarised by the variance p_i(1−p_i), maxi-
malatp_i=0.5.- Worst-case/reliability :min
over tasks of p_i, and the all-pass rate (Π p_i,
iftherunsareindependent)—theproduction-
relevant“doesitholdeverytime”figure.
Thedecisiontable thisproduces,whichisthe
harness’srealoutput:
The middle row is where the operating disci-
pline earns its keep; the bottom row is where
noamountofdisciplinewill,andknowingwhich
rowafailureisin—beforespendingeffort—is
thepoint.
Thepassratealonedoesnotdecidetherow,
and an earlier version of this table said it
did. Itistemptingtoreadamid-range(p_i)as
scatterandanear-zero(p_i)asatightoff-centre
group,andforafirstscreeningpassthatheuris-
ticisserviceable. Itisnotsufficient. Scatterin
thesensethatmattershereis causal,notmerely
statistical: four failures for one identical rea-
son,withonesampleslippingthrough,isatight
groupwithastrayshot,andasinglerulemoves
thewholecluster. Fourfailuresforfourdiffer-
entreasonsatthesamerateisgenuinelywide,
and no rule will collect them.So (p_i) is the
screening signal; homogeneity of the fail-
urecausesistheconfirmingtest. Readthe
failing samples before deciding the row. This
correctionwasnotanticipated—itwasforced
bythereplicationreportedin§4.1,whereafail-
ureratethenaivetableclassedasscatterwas
closedcompletelybyonerule.
4.1 A worked example: measure, find the
miss,zeroit,re-measure
Thefollowingisarealrunofthisharness(six-
task Rust suite, N=5, provider-default temper-
ature — see §7 on why the temperature is
recorded but not controlled). The raw model
wasOpus4.8.
The suite scoredaccuracy 0.833, grouping
1.000, worst-case 0.000: five tasks decisive-
pass, one decisive-fail (p_i = 0 ), zero scatter.
Note the pairing of aperfect grouping score
withan imperfectaccuracy—thisisnotacon-
tradiction but the ideal operator state. A per-
fectlytightgroupwithonedecisivemissisthe
best position to be in, precisely because the
missisdecisiveandthereforezeroable; ascat-
tered model at the same accuracy would be
worse,becauseitsmisseswouldnotbe.
Thesinglemiss(aparse-validationtask)failed
5/5 for one identifiable cause: every sample
declared the requiredOutOfRange error variant,
then parsed the input directly into the target
narrowtype( u16),soanout-of-rangevaluelike
“70000” overflowed to aparse error and re-
turned NotANumber—leaving OutOfRangeunreach-
ableforthevalueitexiststoname. Themodel
reasoned itself into the same collapse every
time; one sample’s own documentation stated
the bug it was committing. That signature —
decisive, reproducible, self-explained — is the
mark of a systematic error a sight-adjustment
corrects,notascatteredone.
Asinglerulewasaddedtotheoperatinglibrary
(parseintoatypewideenoughto representthe
out-of-range value, then range-check), and the
identicalfrozentaskwasre-measured:
Same task, same suite hash, same determinis-
ticscorer; therulewastheonlyvariable. Δ =
+1.000,raw→ruled. Mechanismwasverified
rather than assumed: all five re-run samples
nowparseintothewidertype,andthesurviving
documentationreproducestherule’sreasoning
wheretherawrun’sdocumentedthebug. This
isthecompoundingloopofPaper1closedand
3

Table 1:The corrected decision procedure. The pass rate screens; the homogeneity of the failure causes
decides. Readingthefailingsamplesisnotoptional.
Task outcome pat-
tern
Failurecauses Diagnosis Action
Passes decisively (p_i
≈1)
— Ontarget,tight Keep
Fails at any rate be-
lowpass
onesharedcause Tight group, off-
centre
Zeroable — write a
skill (Paper 1’s re-
learnloop)
Failsatanyratebelow
pass
heterogeneouscauses Widegroup Not zeroable —
change model or
lower sampling tem-
perature
0.0
0.5
1.0
raw
(nolibrary)
library
beforerule
library
withrule
replication
(latermodel)
0/5
1/5
5/5 5/5
passrate
Figure 3:One gap, found by measurement rather
than authored, closed completely by a single ver-
sionedrule—andreplicatedonalaterdefaultmodel
againstthesamefrozentaskandscorer.
Table2: Theworkedexample:onegapfoundbymea-
surement,closedbyonerule.
Configuration passrateonthetask
raw(nolibrary) 0.000(0/5)
pair,library beforetherule 0.200(1/5)
pair,library withtherule 1.000(5/5)
measured end to end — a gap found by mea-
surement, named as an error class, retired by
oneversionedrule,andconfirmedretiredbyre-
measurement.
Replication, and what it corrected.There-
sult was replicated on a later default model
against the same frozen suite and scorer: the
unassisted arm returned 0.200 and the library
arm1.000,matchingtherecordedbaselinefor
that model exactly. The centrepiece therefore
is not an artefact of a single N=5 draw. But
thereplicationalsofalsifiedaclaimthispaper
madeaboutitsownmethod. At0.200theunas-
sistedarmis,onanaivereadingofthedecision
tablein§4, scattered—andthetablesaidscat-
tered failures are not zeroable. A single rule
nonetheless closed it to 1.000. Inspection of
the failing samples resolved the apparent con-
tradiction: every failure had thesame cause,
the narrow parse, with one sample passing by
luck. That is a tight group with a stray shot,
not a wide one. The table has been corrected
accordingly(§4): thepassratescreens,theho-
mogeneityofcausesdecides. Itisworthstating
plainlythattheinstrumentcaughttheoversim-
plificationinitsownauthor’srule,whichisthe
behaviourthemethodissupposedtohaveand
thereasonforreportingreplicationsatall.
A second, quieter lesson came from the same
exercise. Two runs on different models each
produceda 1/5figure—onone,theunassisted
arm; on the other, the library arm — and a
bare 1/5 quoted in prose was momentarily at-
tached to the wrong pairing. No recorded fig-
urewaswrong; theambiguitylivedentirelyin
citinganumberwithoutitsrunandarm. Cross-
run comparisons must therefore be pinned by
runidentifier andarm,neverbythebarevalue.
A measurement programme accumulates num-
bersfasterthanitaccumulatesthecontextthat
makes them mean something, and the context
isthepartthatdecays.
5 Two groupings: the rifle and the
zeroedrifle
Runtheharnessintwoconfigurationsandthe
difference is itself informative. Raw model
(no skills loaded) measures the rifle’s intrin-
sic grouping — the property to select a model
on, alongside cost-per-completed-task. The
pair (skills loaded) measures the grouping af-
terzeroing—thepropertythatgovernsday-to-
day work. The gap between them is the mea-
sured value of the operating discipline: how
muchtighterthelibrarymakesthegroup. And
tracked over time,thepair’sgroupingonafixed
suiteisthecompoundingsignalPaper1’sfield
studyneeds—asthelibrarymatures,tasksfail-
ingforoneconsistentcauseshouldmigrateto
decisive-pass(eachaskillthatzeroedaconsis-
tentmiss),andthegroupingscoreshouldclimb.
Arisinggroupingscoreonafrozensuiteiswhat
“thepairisgettingbetter”lookslikeasanum-
ber.
4

6 Found,notauthored: thelimitof
aconstructedsuite
The worked example above closed a gap com-
pletely. An attempt to measure the library’s
value across the board produced the more im-
portant result, by failing. To price the operat-
ing library, one is tempted to construct a tar-
geted suite — one task per rule, each built to
elicit that rule’s error class — and measure
the raw→pair delta. Five such tasks were au-
thored, one per major rule (borrow-not-clone,
typed-errors, typestate ordering, illegal-states-
unrepresentable,andparse-wide—thelastan
authored instance of the very class thefound
task of §4.1 had exposed). All five failed
theirownadmissiongate: therawfrontier
modelalreadypassedeveryone ,acrosssuc-
cessive attempts to make them harder, includ-
ingaprobethatstrippedatask’srequirement
toitsintentalone(“makemisuseimpossiblefor
callers”)—themodelstillproducedthecompile-
time-safedesignunprompted.
The conclusion is a caution for anyone mea-
suring a discipline’s value:you cannot au-
thoryourwaytoadelta. Constructingtasks
fromyourownrulebookselectsforexactlythe
classesthemodelalreadyhandles,becauseaca-
pablemodelhasinternalisedmostexplicitgood
practice; the constructed suite therefore mea-
suresthemodel’sbaselinecompetence,notthe
library’smarginalcontribution,andthedeltait
reports is structurally near zero regardless of
thelibrary’srealworth. Valueappearsonlyat
the residualgaps—theclassesevenafrontier
modelgetswrong—andthosearenotknowable
in advance. The parse-validation miss of §4.1
was found by measurement onarepresentative
task, not designed; it was the only task of the
whole exercise that discriminated. The practi-
calcorollary: topriceanoperatinglibrary,mea-
sureitonrepresentativeworkandminethede-
cisive failures, rather than assembling a suite
fromtherulesyoualreadywrote. Thelibrary’s
valuelivesinwhatyouhavenotyetthoughtto
encode,andonlymeasurementfindsthat.
Thisalsoboundstheenterprisehonestly. Ona
sufficiently capable model, the marginal value
ofacomprehensiveexplicitrulebooktrendsto-
ward zero, because the model already embod-
ies the discipline; the rules that continue to
matter are the few that cover residual, model-
specific gaps. A skills library is therefore not
a monument to be grown, but a small, live,
measurement-fedsetofpatchesovertheplaces
the current model still scatters or consistently
misses—anditmustbere-measuredasmodels
change,becauseagaponemodelhasisagap
thenextmaynot.
7 Cost, confounds, and honest lim-
its
The harness is N× the cost of a single evalua-
tion, so the suite stays small and the runs pe-
riodic (a quarterly precision review, or a pre-
selectiongatebeforeadoptingamodel),never
continuous — subject, like all of Paper 1’s ma-
chinery,toitsownoverheadbudget.
Scorer bias is the dominant threat, and it
runsoneway. Inbuildingtheharness,several
scoring defects were found, and every one bi-
ased againstthediscipline—asystematicdirec-
tionworthnaming. Twoexamples: aforbidden-
construct check scanned test code and so pe-
nalisedthelibraryforwriting moretests(where
.expect() is legitimate); and doc-tests were
scored against a template whose crate name
couldnotresolve,failinganydocumentationthe
disciplined config produced. A residual case
survived: hidden acceptance tests bind exact
signatures, so a task’s “pass” can require a
worsetypethanthelibrarycorrectlychooses(a
plainintegerwherethedisciplinedoutputisa
non-zeronewtype),andthebettercodefailsto
typecheckagainstthefixture. Thelessongener-
alises:naivedeterministicscorerssystemat-
icallyundercountdiscipline,becausedisci-
plinechangestheshapeofthecodeinways
a shape-blind scorer punishes.Correcting
two such defects on already-collected data —
with no new runs — moved a paired grouping
scorefrom0.167to0.500;thepairedconfigura-
tion’sinitialscoreonthatsuite(0.167grouping,
apparentlyfarworsethantherawmodel’s)had
beenmostlyinstrument,notsignal. Arepresen-
tativesuitesoafflictedpricesthemodel,notthe
library,andmustnotbeusedforthelatter.
Temperature could not be independently
controlled in the environment used (the tool
exposed no temperature parameter); it was
recorded honestly as provider-default and un-
verified rather than invented. This does not
voidthe§4.1result, butitboundswhatthere-
sultmayclaim. Withinasinglerun-pair—the
two arms executed back to back, against the
samefrozentaskandscorer,onthesamemodel
— the sampling configuration is the same un-
knownconstant,sotheraw→ruleddeltaisvalid
eventhoughtheabsolutep_ivaluesarenotan-
choredtoaknowntemperature. Thatguaran-
tee does not extend across run-pairs.The
replicationranonalaterdefaultmodel,whose
provider-sidedefaultmaydifferfromtheearlier
one; eachpairisthereforeinternallycompara-
ble, and the two pairs are comparable only in
theweakersensethatbothproducedthesame
outcome. Claims should be stated in exactly
that form: deltas within a pair, agreement be-
tweenpairs,andnocross-runstatementabout
5

absoluterates.
Three further limits apply. One further caveat
belongs with them, since §4’s correction intro-
duces it: judging cause-homogeneity requires
reading the failing samples , which is a human
ormodeljudgementandthereforenotdetermin-
istic in the way the pass/fail scoring is. The
screening signal is objective; the confirming
test is not. Where the two disagree, the dis-
agreement should be recorded rather than re-
solved silently. Determinism of scoring con-
strainsthesuitetoverifiabletasks—afeature,
sincethosearethetasksthedisciplinetargets,
but it means the method says nothing about
open-endedgenerativework,where(perPaper
1’sprincipleonopen-endedwork, P7)asingle
target may not exist and scatter may be desir-
able. Independence of the N runs is assumed;
sharedcachingcancorrelatethem,andthehar-
nessmustrunthemgenuinelyfresh. AndNwas
smallinthereportedrun;thenumbersillustrate
mechanism,noteffectsize.
8 Conclusion
Theindustryaskshowsmartthemachinesare
and has its answer: smart enough. The ques-
tion that now decides their worth is older and
quieter, and every marksman knows it — not
where the best shot lands, but how tight the
group. Precisionisthefrontiermetric;itismea-
surable without a stochastic ruler by counting
decisiveoutcomesoverrepeateddeterministic
trials; andthecountdoesnotmerelyranksys-
temsbuttellstheoperatorwhetheragivenmiss
ishistofixwithaskillortherifle’stofixwitha
changeofmodel.Paper1gavethedisciplinefor
zeroingthegroup. Thispapergivestheinstru-
ment for measuring it — and the two together
makeaclaimtheleaderboardscannot: thatthe
unit of performance is not the model’s intelli-
gencebutthetightness,andthetractability,of
itsscatter. Thefirstrealrunborethisouttwice
over: where a gap existed, one rule closed it
from0/5to5/5,measured;andwheregapswere
authoredratherthanfound,thefrontiermodel
hadalreadyclosedthem,sothelibrary’svalue
showed as zero — teaching that a discipline’s
worthisprovennotbycataloguingwhatamodel
doeswell,butbyfinding,andretiring,thefew
thingsitreliablydoeswrong.
8.1 References
[1] Chen, M. et al. (2021). Evaluating
Large Language Models Trained on Code.
arXiv:2107.03374. (pass@k.) [2] Wang, X. et
al. (2022). Self-Consistency Improves Chain
of Thought Reasoning in Language Models.
arXiv:2203.11171.[3]Andrikopoulos,G.(2026).
Tuning the Stochastic Machine: A Systems Engi-
neer’s Operating Model for Human-AI Engineer-
ing. (Paper 1 — the operating discipline this
measurementserves.) [4]Jiang,S.andNam,D.
(2026). Beyond the Prompt: An Empirical Study
of Cursor Rules. arXiv:2512.18925. Toappear,
MSR2026.
[5] Zhou, L., Schellaert, W., Martínez-Plumed,
F., Moros-Daval, Y., Ferri, C., and Hernández-
Orallo,J.(2024). Larger and more instructable
language models become less reliable. Nature
634, 61–68. https://doi.org/10.1038/s41586-
024-07930-y
6
