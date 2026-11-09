---
title: 'PAWS: Policy-driven Agentic World Simulation'
url: https://arxiv.org/abs/2609.28547
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Tiviatis Sim
- Jia Hui Woon
- Xinming Gao
- Chen Gao
- Fengbin Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28547
pages: 50
chars: 157613
fetched_at: '2026-11-08T13:22:14+00:00'
kb_version: 1
---

# PAWS: Policy-driven Agentic World Simulation

: Policy-driven Agentic World Simulation
Tiviatis Sim,1∗, Woon Jia Hui1, Xinming Gao2, Chen Gao2, Fengbin Zhu1, Zheng Huanhuan3
Chua Tat Seng1, Kenji Kawaguchi1
1National University of Singapore,2 Tsinghua University,3 City University of Hong Kong
tiviatis@u.nus.edu
Abstract
Policy interventions propagate through public communica-
tion, institutional decisions, and stakeholder responses, yet
datasets for financial multi-agent simulation rarely connect
theseprocessestotemporallyalignedhistoricalevidence.We
introducePAWS, aPolicy-drivenAgenticWorldSimulation
dataset covering 36 verified U.S. financial and economic pol-
icy episodes, 12,727 policy-linked news records, and 65,291
source-groundedstakeholderactions.Eachactionislinkedto
its supporting news and represented by a multi-layer event
frame capturing its interaction mode, financial-action family
andsubtype,semanticattributes,andconditionalmappingsto
external taxonomies. Entities are resolved to normalized or-
ganizations, and actions are aligned with daily market-return
context to support policy-agent simulation replay. On 2,522
stratified action samples, independent AI and human review-
ers achieved 89.4% initial agreement on interaction mode,
withdisagreementssubsequentlyadjudicated.Casestudiesof
the 2008 short-selling ban and 2001 decimalization recover
documented policy timelines and associated market patterns
acrossbothdenseandsparsenewssettings.Areplaystudyfur-
ther shows that high accuracy can mask failure to detect rare
stakeholder actions, identifying action timing and calibration
as central challenges. PAWS provides an auditable substrate
for evaluating agent influence, policy-response cascades, and
action-outcome alignment in historically grounded financial
simulations.
1 Introduction
Financial crises are driven not only by prices and balance
sheets, but also by policy announcements, institutional re-
sponses, public communication, and rapidly changing ex-
pectations. Classical agent-based finance models can repro-
ducestylizedmarketdynamics,buttheiragentsoperateover
numerical states and hand-coded rules that ignore natural
language data (Lebaron 2006; Farmer and Foley 2009); fi-
nancial language models and trading-agent frameworks can
process news and other textual signals, but are rarely eval-
uated in historical settings where policy intent, stakeholder
actions, and market context are aligned over time (Liu et al.
2023;Lietal.2025;Sunetal.2023;Liuetal.2021).Asare-
sult,itremainsdifficulttoaskwhethersimulatedagentsreact
plausibly to a real policy shock, whether their actions match
∗Corresponding author.
the behaviour of relevant institutions, or whether a simula-
tioncapturesthedifferencebetweenanintendedpolicyeffect
and the outcome later observed in the market.
We introducePAWS, aPolicy-drivenAgenticWorld
Simulation dataset for studying policy-centered multi-agent
behavior in financial markets. PAWS uses discrete U.S. fi-
nancial and economic policy interventions whose intended
goals and real market effects are grounded in finance re-
search. For each policy, PAWS aligns policy metadata with
dated news articles, extracted stakeholder actions, normal-
ized action types, entity/organization mappings and daily
market-return context. This allows researchers to move be-
yondisolatednewsclassification/pricepredictionandinstead
evaluateagentsintemporallygroundedpolicyenvironments.
The current PAWS database contains 36 verified policy
episodes, 301 policy-specific query keys, 12,727 policy-
linked news rows, 65,291 extracted action rows, and 65,291
corresponding action-frame rows. The core design choice
in PAWS is to represent policy response as a structured re-
source rather than as a single label. Each extracted action is
groundedinoneormorenewsarticlesandisrepresentedwith
a multi-layer event frame: an interaction mode, a financial-
action family, a family-constrained subtype, modality and
statusattributes,andconditionalcrosswalkstoexternalevent
taxonomies.
The main contributions of this work can be summarized
as follows.
•Weintroducethefirstcohesivepolicy-drivenmulti-agent
simulation (MAS) dataset that aligns historical policy
shocks, policy-relevant news, stakeholder actions, and
market-return context.
•Weprovidedatasetanalysisandafocusedvalidationstudy
on class labelling and action validity while presenting
casestudiestocheckifnewseventsmatchacademiccon-
clusion of several financial events.
•We provide resources, with the necessary pipeline for
replicatingthedatasetcollectionandrelatedexperiments,
as well as an example on how PAWS can be used to do a
simulation study.
•Unlike prior financial or political simulation, this dataset
aligns verified financial-policy episodes with news evi-
dence,stakeholderactions,andmarketdata.Moreover,it
is designed to allow both traditional MAS methods and
arXiv:2609.28547v1  [cs.AI]  23 Sep 2026

modern LLMMAs.
2 Related Works
TocontextualizePAWS,wedrawuponthreedistinctbutcom-
plementarylinesofresearch.First,weexaminefinancialand
LLM-basedagentsimulationstohighlightthegrowingneed
forgrounded,historicallyaccuratepolicyenvironments.Sec-
ond, we review financial text and event resources to identify
the gap in datasets that explicitly link policy interventions
with structured stakeholder actions. Finally, we discuss lit-
erature on policy shocks and market responses, demonstrat-
ing how PAWS provides the structured data necessary to
bridge qualitative policy analysis with quantitative market
outcomes.
Financial and LLM-based agent simulationTraditional
Agent-BasedComputationalFinancemodelsarestructurally
robust for demonstrating systemic risk and policy failures
during crises but are inherently text-blind (Lebaron 2006;
Farmer and Foley 2009). Modern simulation platforms like
ABIDES,FinRL,andTradeMasterenablehigh-fidelitymar-
ket simulation and trading-agent research (Byrd, Hybinette,
andBalch2019;Liuetal.2021;Sunetal.2023),andLLM-
based agents such as FinGPT, QuantAgents, and TradingA-
gents have advanced reasoning and domain-specific collab-
orative trading (Park et al. 2023; Zhou et al. 2023; Liu et al.
2023;Lietal.2025;Xiaoetal.2024).However,theseexist-
ing systems lack curated historical evidence linking policy
announcements, policy intent, stakeholder behavior, and re-
alized market context.
Financial text, event, and timeline resourcesFinancial
NLP datasets support tasks such as numerical reasoning, re-
lationextraction,andeventextractionoverreports,news,and
earnings calls (Chen et al. 2022; Sharma et al. 2023; Zheng
et al. 2019; Huang et al. 2024). These resources provide
valuable supervised targets for extracting finance-relevant
facts, but their units are typically documents, relations, or
eventmentionsratherthanpolicyepisodeswithexplicitinter-
vention windows. Broader event resources such as GDELT,
ICEWS, and EventRegistry provide large-scale actor-event
streams, while timeline summarization work studies how to
identify and order salient events across document collec-
tions (Ward et al. 2013; Kwak and An 2016; Hu, Moon, and
Ng 2024; Sim et al. 2026). While useful for extracting or or-
ganizingevents,theyarenotcuratedaroundfinancial-policy
interventions and do not jointly preserve policy motiva-
tion, stakeholder action traces and market outcomes; PAWS
bridges policy intent, news evidence, stakeholder actions,
and market context as a single auditable resource.
Policy shocks and market responsesFinance research
commonlyuseseventstudiestoestimatethemarketimpactof
discrete economic events (MacKinlay 1997). Work on eco-
nomic policy uncertainty and monetary-policy event-study
databases further demonstrate the importance of systemati-
cally connecting policy communication to financial-market
responses (Baker, Bloom, and Davis 2016; Acosta et al.
2025). PAWS complements this literature: rather than esti-
mating a single treatment effect, it provides structured, tem-
porally grounded evidence for studying how policy shocks
propagate through stakeholders, actions, and downstream
market context. This design enables PAWS to be used for
studyinghowstakeholdersrespondtofinancialinterventions,
and a basis for downstream replay or simulation studies
A more detailed comparison between PAWS and existing
work is provided in Appendix J.
3 Methodology
PAWS is constructed as a policy-centered event resource for
MAS. The pipeline selects policy shocks episodes, retrieves
dated news within policy windows, extracts and coalesces
stakeholderactions,mapseachactionintoamulti-layerevent
frame, resolves entities, and links the resulting records to
daily financial market context.
3.1 Dataset Generation
PolicySelectionWhilenumerousfinancialpoliciesareen-
acted annually, not all of them produce measurable or sep-
arable market effects. PAWS therefore focuses on policies
that satisfy three criteria: the episode has an identifiable an-
nouncementorimplementationdate,itisrelevanttofinancial
marketsorfinancialintermediation,andithasenoughpublic
documentation to support external verification. The current
database snapshot contains 36 verified policy episodes and
301 policy-specific query keys.
Candidate policies are initially compiled withGPT-5.5,
prompted to act as a tenured finance professor and to priori-
tize measurable policy impacts. These candidates are then
manually verified against reputable finance research and
official policy documentation, then manually checked for
dates, scope, and policy description. Each retained policy is
recorded with its announcement window, policy source, in-
tendedeffect,anddocumentedactualoutcome.Thepolicies’
intended outcomes, actual impacts, prompt template, and an
alternativeunderperformingpolicy-identificationvariantare
documented in Appendices A, B, and C.
Market DataMarket data is retrieved from the publicly
available financial dataset factors, industry portfolios, and
size portfolios (Fama and French 1993, 1997; French 2023).
Themarkettablesarenotusedaslabelsforactionextraction.
Instead,theyprovidecontemporaneouscontextforlateranal-
ysis, including event-window summaries, descriptive com-
parisons across industries, and replay tasks that condition
stakeholder behavior on daily market state.
NewsCollectionForeachverifiedpolicy,wedefineapol-
icy window from the policy start date to its documented end
date. When an end date is unavailable, we use a fixed post-
announcement window and report this choice in the dataset
analysis. We then issue date-bounded Google News queries
usingpolicy-specifickeywordsandsourceinformationstored
inPolicyKey. Queries are run over daily intervals so that
retrieved articles can be aligned with the policy timeline.
The retrieval stage resolves Google News links to canon-
ical article URLs and stores the publication date, head-
line, article body, source domain, and retrieval count. If
a canonical article is unavailable, we attempt to recover

Figure 1:PAWS construction framework. Policy-centered news is collected over event windows, converted into stakeholder action records,
resolved to normalized organizations, aligned with market context, and structured into replay-ready agent-day panels for MAS.
the page through the Internet Archive’s Wayback Machine.
Articles that cannot be fully recovered are retained only
when their metadata is sufficient for provenance and are
flagged for manual inspection and backfilling. The accepted
records are stored in theNewstable withpolicy_id,
date,headline,content,source, andcount. Du-
plicatesource-daterecordsareconsolidatedbyincrementing
count, with questionable or policy-irrelevant articles re-
moved through human-in-the-loop review. This design pre-
serves article provenance and allows every downstream ac-
tion to be traced back to the specific policy-relevant sources
from which it was extracted.
Action Extraction, Coalescing and ClassificationThe
action-extractionstageidentifiesstakeholdersandtheactions
attributed to them in policy-window news. Each extracted
row stores an actor string, acting entity, normalized orga-
nization identifier when available, action text, date, source
newsidentifiers,location,legacyactiontypeandastructured
event-frame representation. Some articles may be relevant
to multiple policies, thus articles are grouped by canonical
source before extraction. TheGPT-5.5extraction model is
then called once per source group and returns a structured
JSON list of actions, which are linked back to all associated
news_idsandpolicy_ids.
PAWS represents each extracted action as a structured
event frame rather than a single flat class. For an action
mentiona, the event frame can be summarized as,
F(a) =⟨m a, fa, sa;x CAMEO a , xFed a , xACE a , xMon a ,
xiMaPP a , xIMF a ;z a⟩, (1)
wherem a is the interaction mode,f a is the financial-
action family,sa is a family-constrained subtype, the sixxa
termsareindependentlygatedcrosswalks,andz acontainsat-
tributes such as modality, status, direction, actor role, target,
instrument,amount,andevidencespan,andx acontainscon-
ditional crosswalks to external event or policy taxonomies.
Togeneratetheabove,theGPT-5.5-generatedlabelpro-
vides a context-sensitive interpretation of the full source
group. Second, AllenNLP, OpenIE, and spaCy perform se-
manticrolelabelling(SRL)andareusedtorecoverpredicate-
argument structures and classify action predicates (Gardner
et al. 2018; Honnibal et al. 2020). Third, formal semantic
resources including FrameNet, VerbNet, and FIBO provide
ontology-groundedevidenceforthesameaction(Baker,Fill-
more, and Lowe 1998; Schuler 2005; EDM Council 2024).
The full multi-layer event-frame categories can be accessed
in Appendices L and D.1.
Next, coreference resolution and organization identifica-
tion are applied to extracted entities, since the same stake-
holder may appear under different abbreviations or aliases.
We build a knowledge graph from Wikidata (Vrandečić and
Krötzsch 2014) to map these variants to normalized orga-
nizations and to capture multilingual aliases and translitera-
tions.Thespecificsoftheknowledge-graphconstructionare
provided in the supplementary appendix.
Finally, raw extracted actions are coalesced into a daily
action table. Records with the same normalized organiza-
tion, event date, and action type are merged into a single
DailyActionrow. During coalescing, PAWS preserves
the union of linked policy IDs, news IDs, and raw action
IDs, and assigns sentiment by untied plurality when multi-
ple source records are available. The resulting daily table is
the primary temporal substrate used for agent selection and
simulation.
Actor and Action Quality ControlThe actor classifica-
tion is completed by a primary annotator, followed by ver-
ification from another annotator. All disagreements will be
discussedandresolved.Allstakeholderdataundergoesidem-
potency check after classification.
However, due to the scale of the action set, action classi-
fication proceeds in two stages: AI verification and human
validation.Sol-5.6wasusedastheAIverifier,whereran-
dom class-stratified samples were selected; balanced com-
binations across differing classes were selected. The human
verifier looks into the same samples, fills in the event-frame
and cross-checks with the AI’s output. For difficult samples
with disagreements, the human will reassess the samples
before attaching the golden label.
All samples and adjudication will be available in the re-
sources.

3.2 Derived Replay View
We have provided a simple full-process replay for the
September 2008 short-selling ban within this paper. In this
experimental setup, each selected stakeholder is treated as
an agent capable of individual decision making, and each
policy-agent-day tuple is a decision point. The target label
is one ofno action,Communication, orDirect Intervention.
We utilized expressive replay models: a majority baseline,
a per-agent Markov transition baseline (Rabiner 1989), a
network-threshold agent-based model inspired by threshold
models of collective behavior (Granovetter 1978), a hybrid
temporal-networkagent-basedmodel,astructuredclassifier,
and a boundedGPT-4oLLM-agent replay. More informa-
tion on the design can be found in Appendix F.
4 Dataset Overview
PAWS contains 36 verified policy episodes, 301 policy-
specific query keys, 12,727 policy-linked news rows, 65,291
extracted action rows, and 65,291 corresponding action-
frame rows. Figure 2 showcases the timelines of all 36 poli-
cies,andFigure3indicatestherelativestakeholderstoaction
distribution across policies. The most frequent stakeholders
can be found in the appendix (Figure 13).
Figure 2: The proportion of actions done by different types
of actors for each policy.
4.1 Multi-Layer Event-Frame Actions
We represent each extracted action as a structured event
frame rather than as a single mutually exclusive label. The
design separates (i) the way in which an event is realized,
(ii) its domain-level financial function, and (iii) its fine-
grained mechanism. Six external crosswalk systems then
expose compatible views of the same event for political-
event, monetary-policy, macroprudential-policy, and crisis-
response analyses. The motivation of each event-frame can
be found in Appendix D.2.
Figure3:Policy-levelstakeholderdiversityrelativetocorpus
size.Circlesdenoteuniquenormalizedstakeholders,vertical
ticks denote Action rows, and triangles denote ActionFrame
rowswhenthecountsdiffer.Countsareshownonalogarith-
mic scale.
Interaction ModeThe 8-valued interaction mode records
how the event is performed or where it lies in its realization
lifecycle. It distinguishes communicative reporting, an ac-
tor’splanorcommitment,aformalinstitutionalact,directed
influence or pressure, a material resource transfer, use of a
policyinstrument,anorganizational/businessoperation,and
an observed market or economic state. The inventory is a
project-specific synthesis than a one-to-one reproduction of
the earlier cited ontologies. Its purpose is to prevent cases
such as an ‘entity’s promise to provide funding’ from being
treated as though ‘funding had already been provided’.
Financial-actionfamily.The21-valuedfamilyrecordsthe
broad domain function of the event. It contains communica-
tive and policy-process families, public financial and regu-
latory interventions, private organizational and market op-
erations, legal/enforcement events, and observed economic
outcomes. The family layer is coarser than a mechanism but
more finance-specific than a general event ontology. It is a
projectsynthesisinformedbyCAMEO,policy-toolinvento-
ries, and recurring predicates in the corpus. The distribution
ratio across all policies can be found in Figure 10 from the
appendix.
Financial-actionsubtype.The99-valuedsubtyperecords
the most specific supported mechanism, such as a rate
change, liquidity facility, capital injection, asset transac-
tion, disclosure, merger, default, investigation, or market
movement.Subtypevaluesarenotgloballyinterchangeable:
each is licensed only under one or more specified families.
Thefamily–subtypeconstraintpreventsimpossiblecombina-

Figure 4: Within-policy composition of action representa-
tionsacross36policyepisodes.Rowsdenotepolicies,while
columns group the corresponding action type, interaction
mode, and financial action family. Each cell shows the pro-
portion of actions assigned to that class, normalized sepa-
ratelywithineachrepresentationlayer;darkerblueindicates
greater prevalence. The family panel presents the eight most
frequent financial-action families, with all remaining cate-
gories pooled asOther families.
tions and makes the subtype suitable as an optional, higher-
resolution prediction target. The distribution ratio across all
policies can be found in Figure 11 from the appendix.
Six external crosswalk systemsThe external systems are
views rather than rival ground truths. A crosswalk is popu-
lated only when its eligibility conditions are satisfied; oth-
erwisenot_applicableisameaningfulstructuralvalue
rather than a low confidence fallback.
1.CAMEO/GDELT.TheCAMEOviewrecordsanofficial
root,optionalchildcode,andderivedverbal/materialco-
operation/conflict quadrant. It is appropriate for actor-to-
actor political interactions (Schrodt 2012), but not every
financial state change.
2.Federal Reserve policy tools.This view identi-
fies a recognized monetary-policy implementation in-
strument or facility using a 24-tool inventory plus
not_applicable(Board ofGovernors ofthe Federal
Reserve System 2025). It should not be inferred merely
because the Federal Reserve is mentioned.
3.ACE/ERE-style events.A general event view supplies
an event type and subtype for events licensed by the
ACE/ERE-style inventory (Walker et al. 2006). It pre-
servesinteroperabilitywithgeneraleventextractionwhile
leavingfinance-specificdistinctionstotheprimarylayers.
4.Monetary-policy event class.This view distinguishes
target actions, policy-path or forward-guidance informa-
tion, implementation tools, and observed outcomes, fol-
lowing the empirical distinction between policy actions
and information about the expected policy path (Gürkay-
nak, Sack, and Swanson 2005).
Table 1: Independent-reviewer agreement for interaction
mode.
Comparison Agree Rate
Sol–Human, initial 2255/2522 89.4%
Human–final resolved 2437/2522 96.6%
Sol–final resolved 2334/2522 92.5%
Final label among 267 initial conflicts
Matched Human only 182 68.2%
Matched Sol only 79 29.6%
Matched neither 6 2.2%
Table 2: Deterministic Database Corrections.
Correction class Rows DB share
Resolved interaction mode 1204 3.8%
Hard frame constraints 1464 4.7%
Legacy type synchronization 1674 5.3%
Any corrected action 3814 12.1%
5.iMaPP macroprudential tools.This view maps eligi-
ble actions to the IMF’s 17 macroprudential instrument
groups plusnot_applicable(Alam et al. 2019). It
is activated by the instrument described, not by generic
claims that a policy is “macroprudential.”
6.IMF crisis response.This view captures eight systemic
banking-crisisresponseformsplusnot_applicable,
including liquidity support, guarantees, recapitalization,
asset management, and resolution measures (Laeven and
Valencia 2018).
4.2 Validation Results
Actor ValidationTable 4 in appendix summarizes actor
identity resolution and its coverage across the corpus.In all
organisational classifications, manual verification identified
only two incorrect actor assignments among the 4530 or-
ganisation strings (including textual), corresponding to an
observedaccuracyof99%.Thetwoerrorswerecorrectedin
the final database.
Action ValidationTable 1 indicates the amount of times
wheretheSolandtheannotatoragreedwiththelabelsfrom
GPT-5.5. The remaining conflicts were adjucated by the
human again.
Table 2 showcases the amount of timesGPT-5.5clas-
sifications flouted the deterministic rule and had to undergo
auto-repair.
5 Case Studies
We conduct a focused case study validation of two policies;
the September 2008 short-selling ban (Policy 5) (Boehmer,
Jones, and Zhang 2013) and the move to decimalization in
2001 (Policy 10) (Bessembinder 2003). The short-selling
ban involves a tightly defined regulatory intervention within
ashortcrisis-periodeventwindow,aclearlyaffectedfinancial
sector, and clearly defined timelines and outcomes found in
threehighlycitedfinancepapers.Therewerelotsofnewsand
contrastingopinionsaboutthispolicy,amongbroaderdiscus-
sionsofthe2008financialcrisis.Meanwhile,decimalization

was implemented almost a year after it was first announced,
with low news coverage and no obvious effects on the stock
market. Validation on these two policies demonstrates the
fidelity of the dataset across both a complex dynamic within
a tight window, and a sparse information landscape across a
longer time period.
Figure 5: The proportion of actions done by different types
of actors for each policy.
Policy5has62differentnewsarticles,fromwhich639ac-
tionshavebeenextracted.Policy10has21newsarticlesand
191 actions. Using the broadest categorisation of the actors
(1stdigithierarchycode),thedistributionofactorsisshown
inFigure5.Asexpected,bothpolicieshaveahighproportion
ofactorsincategory1(UnitedStatesOfficialBodies),which
includeentitiessuchastheUSFederalgovernmentandSEC,
who create and announce the financial policies. Policy 5 has
alargepeakatcategory8(Banks,InsuranceandBrokerages)
since the short-selling ban targeted financial stocks. Policy
10 does not have any actors in categories 2 and 3 (Non-US
Countries, and Global Bodies) since the decimalization pol-
icy only targeted the US, whereas short-selling bans were
also implemented in the UK and discussed globally during
the 2008 crisis.
5.1 Policy 5: Short-selling ban
Researchpublishedintopfinancejournalsoutlinedthetime-
line of the 2008 short-selling ban and found that while the
banwasmeanttostabilizepricesduringthecrisis,itactually
severelydegradedmarketqualitybyfurtherreducingliquid-
ity measured through widened bid-ask spreads (Boehmer,
Jones, and Zhang 2013; Beber and Pagano 2013; Battalio
andSchultz2011).Eachoftheeventsinthepaper’stimeline
is accurately reflected in PAWS. On September 18, 2008,
theUnitedKingdomimplementedatemporarybanonshort-
selling of 32 financial stocks, and the US followed with a
temporarybanonallshortsalesin797financialstocks.This
is accurately reflected by 17 actions in theActionFrame
tablefromSept18-19,byactorsaccuratelycategorizedasthe
SEC,theUSfederalgovernment,andtheUK.OnSeptember
22, the major exchanges announced additions to the list of
banned stocks, (action 777), then on October 2, the ban was
extended(action962)andfinallyendedonOctober8(action
1053). A detailed list of the exactaction_ids is provided
in Appendix E.
Since the link is not obvious, there are no actions that ex-
plicitly blame the ban as a cause of the decrease in liquidity,
but there is one action which discusses the liquidity crunch
Figure 6: The bid-ask spread increased during and after the
short-selling ban.
after the ban. The effect is also seen in numerical data. We
use the Corwin-Schultz method (Corwin and Schultz 2012)
to estimate bid-ask spreads using publicly available daily
high and low prices from Yahoo finance across 11 represen-
tative finance stocks. Figure 6 shows that liquidity degraded
(bid-ask spreads increased) after the short-selling ban was
implemented, and persists even after the ban ended.
Figure 7: Average cumulative returns of the market, the fi-
nance industry, and a non-finance industry around the 2008
financial crisis.
Beyond the ground truths provided in literature, PAWS
provides information on the complex actions of other actors
during the same period. By manually looking through the
rest of the 639 actions for Policy 5, we find some interesting
insights and dynamics. Non-finance stock seemed to experi-
ence some positive returns, as opposed to bank stocks. Fig-
ure 7 shows that the market and industry returns provided in
PAWSalsoreflectthatthoughtheentiremarketwasplunging,
the finance industry was hit harder. We also find many in-
stancesofbankrepresentativesandothermarketparticipants
blaming short-sellers for the downfall of several large banks
and the overall market. However, there were also dissenters
opposing the short-selling bans. A particularly interesting
story was found in three actions, where a representative of
Morgan Stanley lobbied for the short-sale restriction, anger-
ing many hedge funds, and led to retaliatory short-selling
attacks after the ban was lifted. This is also reflected in the
numerical stock price data shown in Figure 8.
5.2 Policy 10: Decimalization
Bessembinder(2003)foundthatdecimalizationsubstantially
reduced quoted bid-ask spreads, reducing trade execution

Figure 8: Morgan Stanley’s stock price from September to
November 2008. The dates of large stock price movements
extracted from the news are highlighted and shown to corre-
spond with the numerical data.
Model N Acc. Macro- Active- Active
F1 F1 Recall
Majority 8341 .980 .330 .000 .000
Transition 8341 .979 .330 .012 .006
Threshold ABM 8341 .969 .349 .080 .067
Hybrid ABM 8341 .947 .375 .095 .139
Structured classifier 8341 .877 .356 .112 .382
GPT-4oreplay 50 .240 .205 .718 .560
Table 3: Minimal multi-policy replay results from
minimal_first_study_outputs_llm. The
GPT-4oreplay is bounded to a 50-row sample and
should not be compared to full-panel models by raw
accuracy.
costsforsmalltrades.Thiseffectwasaccuratelypredictedin
action 4388 by the Owen Graduate School of Management,
which is accurately classified as a University (hierarchical
code7210).TheSECordertostartphasingindecimalization,
the time when the NYSE completed the implementation,
the news of delays, and when the Nasdaq exchange also
completed implementation, are all accurately reflected on
the correct dates with the right hierarchical classifications.
Other interesting actions include suspicions and denial of
insidersprofitingfromthepreviousfractionalpricing(1/16th
ofadollar),andexplanationsofthebenefitsdecimalpricing
will bring to investors from both academic institutions and
government bodies pushing for decimalization.
These two case studies show that PAWS is able to ac-
curately extract dated actions from sparse news for policies
morethan20yearsago,aswellasaccuratelyreflectthecom-
plexanddynamicactionstakenbyavarietyofactorsduring
a dense policy window.
6 Simulation Study
WeshowanexampleofhowthePAWSdatasetcanbeusedto
study multi-agent behaviour and interaction by showcasing
how stakeholder actions can be predicted from the policy-
agent-day panel.
Policy5full-processreplayNo-actiondiffusionbaselines
reachhighaccuracy(.939)butzeroactive-F1.TheGPT-4o
LLM-agent variant reaches .824 active recall but only .122
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
Score
Markov
LT
IC
Voter
DeGroot
Bass
Classifier
LLM
0.19
0.09 0.36
0.23 0.48
0.15 0.66
Active-F1 Active recall
Figure 9: Policy 5 full-process replay action recovery. The
structured classifier offers the best active-F1, while the
GPT-4oLLM agent obtains the highest active recall but
over-triggers relative to the observed action rate.
active-F1, while the structured classifier is more conserva-
tive, with .069 active-F1 and .176 active recall. Figure 9
reportsthefull-processreplayfortheSeptember2008short-
selling ban. The no-action diffusion baselines obtain high
accuracy because the true active rate is only 8.7%, but fail
torecoveractivestakeholderresponses.Moreinformationof
the replay can be found in Appendix F.
7 Conclusions and Future Work
WeintroducedPAWS,apolicy-centereddatasetthatconnects
verified financial-policy episodes with dated news evidence,
source-grounded stakeholder actions, normalized organiza-
tions, structured event frames, and daily market context.
The validation and case-study results support the useful-
ness of this design while also revealing the difficulty of the
task. Independent AI and human reviewers achieved 89.4%
initialagreementoninteraction-modelabels,afterwhichdis-
agreementswereadjudicated.Thecasestudiesrecoverdocu-
mentedinterventiontimelinesandassociatedmarketpatterns
undersubstantiallydifferentlevelsofnewscoverage.There-
playstudyadditionallydemonstratesthataggregateaccuracy
is misleading in sparse policy-agent-day panels: models can
achieve high accuracy by predictingno actionwhile failing
to recover the stakeholder responses that matter. Meaning-
fulevaluationmustthereforeemphasizeactive-actionrecall,
timing, and the fidelity of resulting response cascade.
PAWS should be interpreted as a curated observational
and replay resource than a causal estimate of policy effects.
Future work should expand the range of policies and juris-
dictions,strengthenhumanvalidation,improveagentcalibra-
tion,andincorporatehigher-fidelitymarketmechanismsand
counterfactual evaluation. These extensions would support
more rigorous studies of selective agent influence, policy-
responsedynamics,andtheexpectedandunexpectedconse-
quences of financial interventions.
Acknowledgements
This research is supported by Tsinghua University Initiative
Scientific Research Program.

References
Acosta,M.;Ajello,A.;Bauer,M.D.;Loria,F.;andMiranda-
Agrippino, S. 2025. The Financial Market Effects of
FOMC Communication: Evidence from a New Event-Study
Database.Federal Reserve Bank of San Francisco Working
Paper Series.
Alam, Z.; Alter, A.; Eiseman, J.; Gelos, R. G.; Kang, H.;
Narita, M.; Nier, E.; and Wang, N. 2019. Digging Deeper—
Evidence on the Effects of Macroprudential Policies from
a New Database. IMF Working Paper 19/66, International
Monetary Fund.
Baker, C. F.; Fillmore, C. J.; and Lowe, J. B. 1998. The
Berkeley FrameNet Project. InProceedings of the 36th An-
nual Meeting of the Association for Computational Linguis-
tics and 17th International Conference on Computational
Linguistics, 86–90. Association for Computational Linguis-
tics.
Baker, S. R.; Bloom, N.; and Davis, S. J. 2016. Measuring
Economic Policy Uncertainty.The Quarterly Journal of
Economics, 131(4): 1593–1636.
Battalio, R.; and Schultz, P. 2011. Regulatory Uncertainty
and Market Liquidity: The 2008 Short Sale Ban’s Impact
on Equity Option Markets.The Journal of Finance, 66(6):
2013–2053.
Beber,A.;andPagano,M.2013. Short-SellingBansAround
the World: Evidence from the 2007–09 Crisis.The Journal
of Finance, 68(1): 343–381.
Bessembinder, H. 2003. Trade Execution Costs and Market
Quality after Decimalization.The Journal of Financial and
Quantitative Analysis, 38(4): 747–777.
Board of Governors of the Federal Reserve System. 2025.
Policy Tools. Federal Reserve Board. Last updated 2025-
12-15; accessed 2026-07-28.
Boehmer, E.; Jones, C. M.; and Zhang, X. 2013. Shack-
ling Short Sellers: The 2008 Shorting Ban.The Review of
Financial Studies, 26(6): 1363–1400.
Breiman, L. 2001. Random Forests.Machine Learning,
45(1): 5–32.
Byrd, D.; Hybinette, M.; and Balch, T. H. 2019. ABIDES:
Towards High-Fidelity Market Simulation for AI Research.
arXiv:1904.12066.
Chen, Z.; Chen, W.; Smiley, C.; Shah, S.; Borova, I.; Lang-
don, D.; Moussa, R.; Beane, M.; Huang, T.-H.; Routledge,
B.; and Wang, W. Y. 2022. FinQA: A Dataset of Numerical
Reasoning over Financial Data. arXiv:2109.00122.
Corwin, S. A.; and Schultz, P. 2012. A Simple Way to
EstimateBid-AskSpreadsfromDailyHighandLowPrices.
The Journal of Finance, 67(2): 719–760.
EDMCouncil.2024. FinancialIndustryBusinessOntology.
Fama, E. F.; and French, K. R. 1993. Common risk factors
in the returns on stocks and bonds.Journal of Financial
Economics, 33(1): 3–56.
Fama,E.F.;andFrench,K.R.1997. Industrycostsofequity.
Journal of Financial Economics, 43(2): 153–193.
Farmer, J.; and Foley, D. 2009. The Economy Needs Agent-
Based Modeling.Nature, 460: 685–6.
French, K. R. 2023. Kenneth R. French - Data Library.
Accessed: 1 Jan 2026.
Gardner,M.;Grus,J.;Neumann,M.;Tafjord,O.;Dasigi,P.;
Liu,N.F.;Peters,M.;Schmitz,M.;andZettlemoyer,L.2018.
AllenNLP: A Deep Semantic Natural Language Processing
Platform. InProceedingsofWorkshopforNLPOpenSource
Software, 1–6. Association for Computational Linguistics.
Granovetter, M. 1978. Threshold Models of Collective Be-
havior.American Journal of Sociology, 83(6): 1420–1443.
Gürkaynak, R. S.; Sack, B.; and Swanson, E. T. 2005. Do
Actions Speak Louder Than Words? The Response of Asset
Prices to Monetary Policy Actions and Statements.Interna-
tional Journal of Central Banking, 1(1): 55–93.
Honnibal, M.; Montani, I.; Landeghem, S. V.; and Boyd, A.
2020. spaCy:Industrial-strengthNaturalLanguageProcess-
ing in Python.
Hu, Q.; Moon, G.; and Ng, H. T. 2024. From Moments to
Milestones: Incremental Timeline Summarization Leverag-
ing Large Language Models. In Ku, L.-W.; Martins, A.; and
Srikumar, V., eds.,Proceedings of the 62nd Annual Meeting
oftheAssociationforComputationalLinguistics(Volume1:
Long Papers), 7232–7246. Bangkok, Thailand: Association
for Computational Linguistics.
Huang, Y.; Hu, N.; Li, K.; Wang, N.; and Lin, Z. 2024. Ex-
tractingFinancialEventsfromRawTextsviaMatrixChunk-
ing. InProceedings of the 2024 Joint International Con-
ference on Computational Linguistics, Language Resources
and Evaluation, 7035–7044. ELRA and ICCL.
Kwak, H.; and An, J. 2016. Two Tales of the World: Com-
parison of Widely Used World News Datasets GDELT and
EventRegistry. InProceedings of the Tenth International
AAAI Conference on Web and Social Media, 619–622.
Laeven,L.;andValencia,F.2018. SystemicBankingCrises
Revisited. IMF Working Paper 18/206, International Mone-
tary Fund.
Lebaron, B. 2006. Agent-Based Computational Finance.
Handbook of Computational Economics, 2: 1187–1233.
Li,X.;Zeng,Y.;Xing,X.;Xu,J.;andXu,X.2025. QuantA-
gents: Towards Multi-agent Financial System via Simulated
Trading. arXiv:2510.04643.
Liu, X.-Y.; Wang, G.; Yang, H.; and Zha, D. 2023. Fin-
GPT: Democratizing Internet-scale Data for Financial Large
Language Models. arXiv:2307.10485.
Liu,X.-Y.;Yang,H.;Gao,J.;andWang,C.D.2021. FinRL:
deep reinforcement learning framework to automate trading
in quantitative finance. InProceedings of the Second ACM
International Conference on AI in Finance, ICAIF’21, 1–9.
ACM.
MacKinlay, A. C. 1997. Event Studies in Economics and
Finance.Journal of Economic Literature, 35(1): 13–39.
Park, J. S.; O’Brien, J. C.; Cai, C. J.; Morris, M. R.; Liang,
P.;andBernstein,M.S.2023. GenerativeAgents:Interactive
Simulacra of Human Behavior. InProceedings of the 36th
Annual ACM Symposium on User Interface Software and
Technology, 1–22. ACM.

Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.;
Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss,
R.;Dubourg,V.;VanderPlas,J.;Passos,A.;Cournapeau,D.;
Brucher, M.; Perrot, M.; and Duchesnay, E. 2011. Scikit-
learn: Machine Learning in Python.Journal of Machine
Learning Research, 12: 2825–2830.
Rabiner, L. R. 1989. A Tutorial on Hidden Markov Models
and Selected Applications in Speech Recognition.Proceed-
ings of the IEEE, 77(2): 257–286.
Schrodt, P. A. 2012.CAMEO: Conflict and Mediation
EventObservations—EventandActorCodebook.EventData
Project,DepartmentofPoliticalScience,PennsylvaniaState
University. Version 1.1b3; updated 2012-03-16.
Schuler, K. K. 2005.VerbNet: A Broad-Coverage, Compre-
hensive Verb Lexicon. Ph.D. thesis, University of Pennsyl-
vania.
Sharma, S.; Nayak, T.; Bose, A.; Meena, A. K.; Dasgupta,
K.;Ganguly,N.;andGoyal,P.2023. FinRED:ADatasetfor
RelationExtractioninFinancialDomain.arXiv:2306.03736.
Sim, T.; Yang, K.; Xin, S.; and Kawaguchi, K. 2026. Who’s
important? – SUnSET: Synergistic Understanding of Stake-
holder, Events and Time for Timeline Generation.
Sun,S.;Qin,M.;Zhang,W.;Xia,H.;Zong,C.;Ying,J.;Xie,
Y.; Zhao, L.; Wang, X.; and An, B. 2023. TradeMaster: A
Holistic Quantitative Trading Platform Empowered by Re-
inforcement Learning. In Oh, A.; Naumann, T.; Globerson,
A.; Saenko, K.; Hardt, M.; and Levine, S., eds.,Advances in
Neural Information Processing Systems, volume 36, 59047–
59061. Curran Associates, Inc.
Tibshirani,R.1996. RegressionShrinkageandSelectionvia
the Lasso.Journal of the Royal Statistical Society: Series B,
58(1): 267–288.
Vrandečić, D.; and Krötzsch, M. 2014. Wikidata.Commu-
nications of the ACM, 57(10): 78–85.
Walker, C.; Strassel, S.; Medero, J.; and Maeda, K. 2006.
ACE 2005 Multilingual Training Corpus. Linguistic Data
Consortium, LDC2006T06.
Ward,M.D.;Beger,A.;Cutler,J.;Dickenson,M.;Dorff,C.;
and Radford, B. J. 2013. Comparing GDELT and ICEWS
Event Data.
Xiao, Y.; Sun, E.; Luo, D.; and Wang, W. 2024. Tradin-
gAgents: Multi-Agents LLM Financial Trading Framework.
arXiv:2412.20138.
Zheng,S.;Cao,W.;Xu,W.;andBian,J.2019. Doc2EDAG:
An End-to-End Document-level Framework for Chinese Fi-
nancialEventExtraction. InProceedingsofthe2019Confer-
enceonEmpiricalMethodsinNaturalLanguageProcessing
and the 9th International Joint Conference on Natural Lan-
guage Processing, 337–346. Association for Computational
Linguistics.
Zhou, X.; Zhu, H.; Mathur, L.; Zhang, R.; Yu, H.; Qi, Z.;
Morency,L.-P.;Bisk,Y.;Fried,D.;Neubig,G.;Sap,M.;and
Yang,D.2023. SOTOPIA:InteractiveEvaluationforSocial
Intelligence in Language Agents. arXiv:2310.11667.

A Prompt used for Policy Identification
Prompt for Policy Identification
You are a renown tenured finance professor at a prestigious university. You
have been researching various financial topics for decades, and are an expert
at identifying changes in financial policies that had large impacts on the
financial market. You often leverage these as "exogenous shocks" to
investigate causality in your research.
Please provide a list of policy changes from that have made large impacts on
the US financial markets, no matter if they were simply short-term effects
or long-term effects. For each policy, provide the reason the policy was
implemented and the intended outcomes of the policy. Also provide any
published/working papers from reputable sources (i.e. published in top
finance journals or written by authors from prestigious universities) that
studied the effects of the policy and summarize their established impact(s)
on the financial markets. For policies that were not used in any research
papers, provide your own summary on their impacts on the financial markets,
and relate to the intended outcomes of the policy. Try to focus on impacts
that can be measured using stock market returns.
Be as comprehensive as possible, covering as many policies as possible, but
keep the summaries of the impacts concise and succinct.
Output your response in a single text block in the following JSON format:
{
"policy_name": "the name of the policy",
"announcement_date": "YYYY-MM-DD",
"implementation_date": "YYYY-MM-DD",
"description": "a brief description of what the policy does and why it was
implemented",
"intended_outcomes": "a summary of the intended outcomes of the policy",
"research_papers": [
{
"title": "title of the research paper",
"authors": ["name1", "name2"],
"link": "link to the paper",
"findings": "a concise summary of what the authors found to be the
impact of the policy"
}
]
"llm_analysis": "your own analysis of the impact of the policy"
}

B Policy Details
In order of announcement/implementation date, numbered bypolicy_id.
B.1 10: Decimalization
On 9 April 2001, US markets switched from fractional pricing (1/16th of a dollar) to decimal pricing (pennies), reducing the
minimumticksize.Thiswasdonetoimprovemarketefficiencybyallowingpricestomoreaccuratelyreflectstockvalue(1/100th
instead of 1/16th precision). Research documented that quoted bid-ask spreads fell dramatically, reducing transaction costs and
increasing liquidity for small trades (Bessembinder 2003).
B.2 12: JGTRRA
Congress approved the Jobs and Growth Tax Relief Reconciliation Act of 2003 on 23 May 2003, and it was signed into law
on 28 May 2003. The act reduced the maximum tax rate on capital gains from 20% to 15% and the maximum tax rate on
dividendsfrom38.1%to15%.Literaturefounda20%increaseindividendpaymentsbynonfinancial,nonutilitypubliclytraded
corporations following the tax cut (Chetty and Saez 2005).
B.3 8: Term Auction Facility (TAF)
Announced on 12 December 2007, the Term Auction Facility’s (TAF) primary objective was to provide emergency liquidity,
reduce the liquidity risk premium in the interbank market, and consequently lower the significantly elevated London interbank
offered rate (Libor). Literature documented mixed results, but seems to imply that the policy effectively relieved the liquidity
strains and brought down the Libor (McAndrews, Sarkar, and Wang 2015).
B.4 5: Short-Selling Bans
On18September2008,theUKandUSbannedshortsellingonfinancialstockstostabilizeprices,andthisbanwaseffectiveuntil
8October2008fortheUSmarket.However,thispolicywaslargelycounterproductive,severlydegradingmarketquality(spreads
widened,priceimpactincreased,andintradayvolatilityrose)(Boehmer,Jones,andZhang2013),slowedpricediscovery(Beber
and Pagano 2013), and dramatically increased bid-ask spreads(Battalio and Schultz 2011).
B.5 7: Commercial Paper Funding Facility (CPFF)
On 7 October 2008, the Federal Reserve announced the Commercial Paper Funding Facility (CPFF) to provide a liquidity
backstop; to ensure that firms have enough liquidity to meet their operational needs and not go bankrupt. The literature found
thatfirmseligiblefortheCPFFwereabletomitigatefinancingdisruptionsandledtoanincreaseinprofitabilityandshort-term
earnings forecasts, with spillover effects also leading to an increase in general public liquidity (Gao and Yun 2012).
B.6 6: Term Asset-Backed Securities Loan Facility (TALF)
On 25 November 2008, the Term Asset-Backed Securities Loan Facility (TALF) was announced. The TALF was intended
to increase demand for asset-backed securities (ABS) and encourage more lending to households and small businesses. The
literature document that TALF played a critical role in preventing the shutdown of lending to consumers and small businesses
(Campbell et al. 2011).
B.7 18: The Durbin Amendment
Announced on 29 June 2001 and implemented on 1 October 2011, the Durbin Amendment capped interchange fees charged to
merchants for processing debit card transactions to reduce retailer costs with the hope that those savings would be passed to
consumers as lower prices. Research found that banks offset $6.5 billion in losses by increasing maintenance fees and reducing
free checking availability (Mukharlyamov and Sarin 2025), hence consumers ultimately paid more through increased banking
fees than they saved at the register.
B.8 23: Say-on-Pay Mandates
Announced on 21 July 2010 and implemented on 1 April 2011, the Say-on-Pay Mandates required public companies to hold
advisoryshareholdervotesonexecutivecompensationinanefforttocurbexcessivecompensationandalignexecutiveincentives
with shareholder interests. Literature found that implementation in April 2011 led to a 4.6% increase in firm market value and
improved long-term operational productivity (Cuñat, Giné, and Guadalupe 2016).

B.9 21: Budget Control Act / S&P Sovereign Downgrade
Announced on 2 August 2011 and implemented on 5 August 2011, the Budget Control Act (BCA) was enacted to resolve
debt ceiling crisis while the S&P subsequently downgraded U.S. credit to AA+. The BCA aimed for deficit reduction and the
downgrade reflected political and fiscal governance concerns. Research found that when the US Federal government repeatedly
reached the legally binding debt limits, the financial market only initially charged a small default risk premium to the Treasury
securities but no significant overall price effect, suggesting that the financial market gradually perceived the budget standoffs as
"the boy who cried wolf" (Liu, Shao, and Yeager 2009).
B.10 13: Operation Twist (Maturity Extension Program)
Announced on 21 September 2011 and implemented on 1 October 2011, Operation Twist was a sterilized monetary initiative
where the Fed sold $400 billion in short-term Treasuries to purchase long-term Treasuries, with the aim to flatten the yield
curve, reduce long-term interest rates, and encourage portfolio rebalancing into riskier assets without expanding the balance
sheet.Literaturefoundasignificant15basispointdeclineinlong-termTreasuryyieldsanda2-4basispointdeclineincorporate
bond yields (Swanson, Wright, and Reichlin 2011), indicating that the program was successful.
B.11 20: G-SIFI Designations
On 1 November 2011, specific institutions were designated as ’too big to fail,’ subjecting them to capital surcharges. This
was done in an effort to internalize negative externalities and reduce the probability of systemic failures. Research found that
designated entities faced higher capital costs, leading to lower stock valuations compared to non-designated peers (Scott 2012),
creating a ’regulatory discount’ on major bank stocks and forcing a retrenchment from capital-intensive activities.
B.12 16: Dollar Liquidity Swap Line Rate Reduction
Announced on 30 November 2011 and implemented on 5 December 2011, the Fed and other central banks lowered the pricing
ondollarliquidityswaparrangementsby50basispoints,inhopesofrelievingoffshoredollarfundingstressandpreventingfire
sales of dollar assets by European banks. Research found that it reduced Covered Interest Parity (CIP) deviations and stabilized
cross-border investment flows (Bahaj and Reis 2022), acting as a crucial global lender-of-last-resort mechanism, and removing
systemic tail risk during the European debt crisis.
B.13 22: Jumpstart Our Business Startups (JOBS) Act
On 5 April 2012, the JOBS Act eased securities regulations and auditing requirements for ’Emerging Growth Companies’
(EGCs) to encourage IPOs and lower capital formation barriers for high-growth startups. Literature found that it boosted IPO
volume by 25%, particularly in biotech, but led to significantly higher IPO underpricing (Dambra, Field, and Gustafson 2015).
B.14 19: U.S. Implementation of Basel III
Announced on 7 June 2012 but implemented a year later on 1 July 2013, the US increased the quantity and quality of required
Common Equity Tier 1 (CET1) capital for banks to ensure banks maintain high-quality capital buffers to absorb losses during
economic stress. Research found that after the announcement, banks had lowered return on equity and accelerated migration of
credit provision to the shadow banking sector, moving outside the regulatory perimeter (Fritsch and Siedlarek 2022).
B.15 15: Quantitative Easing 3 (Open-Ended LSAP)
On13September2012,theUSmadeopen-endedmonthlypurchasesof$40billioninagencymortgage-backedsecurities(MBS)
ineffortstocompressmortgagerates,stimulatehousing,andcreateawealtheffectthroughhigherequityprices.Researchfound
thatitincreasedglobalequityprices,loweredtheVIX,andinducedmassivecapitalinflowsintoemergingmarkets(Eichengreen
and Gupta 2015).
B.16 14: State-Contingent Forward Guidance (The Evans Rule)
Announced and implemented on 12 December 2012, the Evans Rule replaced calendar-based guidance with explicit economic
thresholds: 6.5% unemployment and 2.5% inflation, to eliminate interest rate uncertainty and provide an ’automatic stabilizer’
formarketpsychology.ResearchfoundthatitfunctionedasanOdysseancommitmentmechanism,recalibratingfuturescontracts
and private forecasts (Justiniano et al. 2012), ensuring monetary accommodation would persist through economic weakness.
B.17 24: Unconventional Monetary Policy Tapering Announcement (Taper Tantrum)
On22May2013,FederalReserveChairmanBenBernankeannouncedtheFed’sintentiontobeginscalingbackits$85billion-
a-monthbond-buyingprogram(QuantitativeEasing3).TheactualtaperingofassetpurchasesbeganinJanuary2014.Thiswas
tonormalizeU.S.monetarypolicy,gracefullyexittheunprecedentedquantitativeeasingmeasuresimplementedpost-2008,and
prevent the U.S. economy from overheating as macroeconomic indicators showed sustained recovery. Literature found that the

tapering announcement functioned as a major monetary shock that dramatically increased required risk compensation, trigger-
ing massive capital outflows from emerging markets, disproportionately depressing emerging market equities and currencies
compared to physical capital flows (Chari, Dilts Stedman, and Lundblad 2021).
B.18 25: Title II of the JOBS Act (General Solicitation)
Announced on 10 July 2013 and implemented 23 September 2013, this was a structural deregulatory action by the SEC that
eliminated the long-standing ban on ’general solicitation and general advertising’ for private placements conducted under Rule
506(c), provided all purchasers are verified accredited investors. The intention was to democratize private capital formation,
allowing startups and small businesses to utilize the internet and public media to reach a broader base of accredited investors,
thereby expanding capital access and lowering early-stage costs. Literature found that after accounting for selection bias,
issuers using general solicitation are less likely to succeed in raising capital, obtaining venture capital funding, or exiting via
IPO (Agrawal and Lim 2026). For the public stock market, this dynamic reduced the average quality of incoming small-cap
companies, characterized by higher return volatility and an increased rate of exchange delistings.
B.19 26: The Volcker Rule (Dodd-Frank Act Section 619)
Announcedon10December2013andimplementedon1April2014,thisrulerestrictsU.S.depositoryinstitutionsfrommaking
speculativeinvestmentsthatdonotbenefittheircustomers.Itexplicitlyprohibitscommercialbanksfromengaginginproprietary
trading and severely limits their investments in hedge funds and private equity funds. Research found that the Volcker Rule
decreased corporate bond liquidity during times of stress, with dealers affected by the rule curtailing their market-making
activities, and non-affected dealers not fully offseting this loss, leading to significantly increased illiquidity when bonds were
downgraded (Bao, O’Hara, and (Alex) Zhou 2018).
B.20 27: 2014 SEC Money Market Fund Reform
Announced 23 July 2014 and implemented 14 October 2016, the SEC adopted structural reforms requiring institutional prime
moneymarketfunds(MMFs)tofloattheirnetassetvalue(NAV)ratherthanmaintainingastable$1.00NAV.Italsoprovidedfund
boards the tools to impose liquidity fees and redemption gates if a fund’s weekly liquid assets fell below regulatory thresholds.
Research demonstrated that the regulation reduced the ’money-likeness’ of prime MMFs by increasing their information
sensitivity, with investors shifting over $1 trillion from prime to government MMFs, revealing a significant 20-30 basis point
premium that investors are willing to pay for money-like stability (Cipriani and La Spada 2021).
B.21 28: Department of Labor (DOL) Fiduciary Rule
Announced on 14 April 2015, but never implemented, the rule expanded the definition of ’investment advice fiduciary’ under
ERISA,legallyrequiringadvisorsandbroker-dealerstoactinthebestinterestsoftheirclientsonretirementaccounts.Research
revealedthatvariableannuitysaleswerehighlysensitivetobrokercommissions,withsalesofhigh-expenseannuitiesplummeting
by 52% post-rule announcement, shifting capital toward lower-cost products and improving investor welfare overall (Egan, Ge,
andTang2022).LiteraturealsodemonstratedthatETFpricesandtheequityvaluationsofETFsponsorsreactedwithsignificant
positive abnormal returns following the DOL rule announcements (Wang 2019).
B.22 29: Repeal of the U.S. Crude Oil Export Ban
Announcedon15December2015andimplemented2dayslater,theUSlegislativerepealedthe1970s-erastatutoryprohibition
on exporting domestically produced crude oil to global markets, in an effort to relieve transportation and refining bottlenecks
causedbytheshaleboom,closethepricingspreadbetweenWTI(USoilprice)andBrentcrude(globaloilprice),andstimulate
domestic energy exploration and production. Literature found that repealing the export ban led to increased global trade and
long-term efficiency in the global oil market (Ã‡akÄ±r Melek and Ojeda 2017), stabilized oil prices (Shao 2020), and relieved
artificially low light oil prices in the U.S., allowing exports to expand and correcting inefficient production mandates on U.S.
refineries (Langer, Huppmann, and Holz 2016).
B.23 30: Federal Reserve Zero Lower Bound (ZLB) Liftoff
On16December2015,theFOMCraisedthetargetrangeforthefederalfundsratefrom0.00-0.25%to0.25-0.50%,endingseven
consecutiveyearsofZeroInterestRatePolicy.Literaturedocumentedtheabruptdisappearanceofthe’pre-FOMCannouncement
drift’(wherethestockmarketsawsignificantabnormalpositivereturnswithin24hoursbeforeFederalOpenMarketCommittee
(FOMC)meetings)inequitymarkets,aphenomenonthatvanishedpreciselycoincidingwiththeZLBliftoff(Kurov,Olson,and
Wolfe 2024).
B.24 31: Treasury Department Section 385 Regulations (Anti-Inversion and Earnings Stripping Rules)
Announced on 4 April 2016 and implemented on 21 October 2016, the IRS broad administrative was granted the authority to
recharacterizecertainintercompanydebtinstrumentsasequitytostop’earningsstripping’practicesduringcorporateinversions,
in an effort to halt corporate tax inversions (specifically targeting the pending Pfizer-Allergan mega-merger) and to protect the

U.S. corporate tax base from erosion via cross-border related-party debt structuring. Literature demonstrates that U.S. firms
engaged in offshore re-domiciling experience significant negative cumulative abnormal returns when the U.S. government
unexpectedly tightens the tax code (Reyes and Upadhyay).
B.25 32: The Tax Cuts and Jobs Act (TCJA)
Announced on 20 December 2017 and implemented on 1 January 2018, the TCJA was a comprehensive overhaul of the US tax
codethatreducedthestatutorycorporateincometaxratefrom35%to21%,shiftedtheUStoaterritorialtaxsystem,mandated
atransitiontaxonaccumulatedforeignearnings,andlimitedinterestexpensedeductibility.Literaturefoundthatdomesticfirms
historicallypayinghigheffectivetaxratesexperiencedsignificantpositiveabnormalreturns,whileinternationallyorientedfirms
suffered due to the unexpected magnitude of the repatriation transition tax, and median effective tax rates fell from 31.7% to
20.8% (Wagner, Zeckhauser, and Ziegler 2020).
B.26 33: U.S.-China Trade War Tariff (1)
On22March2018,thiswasthefirstofaseriesofunilateralandescalatingretaliatoryimporttariffsleviedbytheUSandChina
against each other’s goods, spanning multiple tranches throughout 2018 and 2019. This was when the Trump administration
issued the presidential memorandum proposing tariffs on up to $50 billion of Chinese imports. US firms exposed to China
experienced immediate and persistent stock return declines; within 2 days of the announcement date, a one standard deviation
increase in a firm’s share of sales to China led to a 0.48% lower cumulative return, while a one standard deviation increase in
directinputsfromChinaledtoa0.29%lowercumulativereturn(Huangetal.2023).Withina7-daywindowoftheannouncement
date, the market experienced a cumulative return of -3.39%, of which -2.62% was directly cause by the tariff announcement,
and firms exposed to the Chinese market saw an additional -0.04% impact (Amiti, Kong, and Weinstein 2020). At 40 days after
the announcement, a 10 percentage-point increase in a firm’s share of revenue from China is associated with a 2.3% lower
cumulative stock return, and remains significant up till 80 days post announcement (Huang et al. 2023).
B.27 36: Economic Growth, Regulatory Relief, and Consumer Protection Act (EGRRCPA)
Announcedon22May2018andimplemented2dayslater,thislegislationrolledbackspecificDodd-FrankActprovisions,most
notably raising the asset threshold for strict regulatory stress tests from $50 billion to $250 billion and exempting community
banks from the Volcker Rule. This was to reduce compliance costs for small and mid-sized banks, free up capital for economic
growth and consumer lending, and slow down community bank consolidations. After the EGRRCPA on 22 March 2018, small
banks(under$10billioninassets)reactedmostfavorably,showingtangiblesubsequentgrowthinlendingandassetgrowth,but
no observed effects on large banks (Coffee 2022).
B.28 34: U.S.-China Trade War Tariff (2)
On 17 September 2018, the second of a series of unilateral and escalating retaliatory import tariffs levied by the US and China
againsteachother’sgoods,spanningmultipletranchesthroughout2018and2019.Thiswastheannouncementoftariffson$200
billion of Chinese imports. This announcement had very little net impact on the market. It generated a mild negative effect on
theentiremarket(-0.60%)alongsideasmallpositivedifferentialeffect(+0.26%)forexposedfirms(Amiti,Kong,andWeinstein
2020), suggesting it may have been less protectionist than market participants initially anticipated.
B.29 35: U.S.-China Trade War Tariff (3)
On 10 May 2019, the third of a series of unilateral and escalating retaliatory import tariffs levied by the US and China against
each other’s goods, spanning multiple tranches throughout 2018 and 2019. The U.S. escalated the September 2018 tariffs on
the $200 billion list from 10% to 25%. This announcement heavily penalized China-exposed firms via a -1.36% drop in returns
(especiallyhurtingfirmswithhighrevenueexposuretoChinaorreliantonChineseimports).,andsimultaneouslydraggeddown
the broader market by -1.62% (Amiti, Kong, and Weinstein 2020).
B.30 37: The September 2019 Repo Market Intervention and FOMC Policy Pivot
On 17 September 2019, the Federal Reserve implemented emergency interventions in the repurchase agreement (repo) market
to inject liquidity after overnight borrowing rates spiked above 5%. This catalysed a pivot away from quantitative tightening
and toward interest rate cuts. This was done to stabilize the Secured Overnight Financing Rate (SOFR), restore liquidity to
short-term funding markets, and prevent downward pressure on the broader economy. Textual analysis reveals a causal effect of
the stock market on Fed policy, where negative stock returns are strongly correlated with Fed growth expectation downgrades,
whichdictateaccommodatingmonetarypolicy(the’FedPut’,themarket’sbeliefthatthecentralbankwillstepintostopsevere
stock market drops) (Cieslak and Vissing-Jorgensen 2020).

B.31 38: Final Rule Implementing Amendments to the Volcker Rule (Volcker 2.0 / 2.1)
Announcedon14November2019andeffective1January2020,theseregulatoryrevisionssimplifiedVolckerRulecompliance
by creating an objective safe harbor (instruments held over 60 days are presumed not to be proprietary trading) and removing
highly subjective intent tests. Research found that the original Volcker Rule structurally impaired liquidity and the 2019/2020
revisions were enacted to successfully reverse this illiquidity (Bao, O’Hara, and (Alex) Zhou 2018).
B.32 39: Federal Reserve Emergency Rate Cuts and Corporate Credit Facilities (PMCCF/SMCCF)
Announced on 23 March 2020 and implemented on 16 June 2020, these were unprecedented emergency monetary policy in
response to COVID-19, cutting rates to zero and establishing facilities that authorized the central bank to directly purchase
corporatedebtandcorporatebondETFs.Researchfoundthatthefacilityannouncementsreducedcreditspreadsoneligiblebonds
by70 basispoints within10 daysandrestored thenormal yieldcurve, whileactualphysical purchasesafter theimplementation
date lowered eligible bond spreads by an additional 11 basis points immediately, with persistent effects for low-quality bonds
(Gilchrist et al. 2024). The announcement also triggered an immediate, dramatic stabilization of the corporate bond market by
substantially lowering the default risk premium, with average secondary market credit spreads droppinf by over 90 basis points
within three days, and strictly eligible investment-grade bonds experiencing an additional differential decline of 52 basis points
(Boyarchenko, Kovner, and Shachar 2022). The announcement effectively functioned as a "buyer of last resort," significantly
reducing fire-sale incentives by narrowing bid-ask spreads for highly-rated and BBB eligible bonds by more than 45 cents and
30 cents, respectively (Boyarchenko, Kovner, and Shachar 2022).
B.33 40: Coronavirus Aid, Relief, and Economic Security (CARES) Act
Announced on 25 March 2020 and implemented on 13 April 2020, the act enacted a $2.2 trillion emergency fiscal stimulus
package addressing the COVID-19 lockdowns, which included direct Economic Impact Payments (stimulus checks) sent to US
households. The arrival of stimulus checks on April 13, 2020, triggered a massive spike in retail trading targeting low-priced,
high-volatility stocks, with retail-concentrated portfolios seeing 5.62% abnormal returns immediately on the first day, growing
to 10.73% cumulative abnormal returns over 3 days and 14.74% over three weeks (Greenwood, Laarits, and Wurgler 2022).
B.34 41: American Rescue Plan Act of 2021 (Third Round Stimulus Checks / EIP3)
Announced on 11 March 2021 and implemented the next day, the American Rescue Plan authorized a massive fiscal package
thatincludedathirdroundofdirectEconomicImpactPayments(EIP3)ofupto$1,400pereligibleindividual.Thisconstituted
a sudden wealth shock distributing over $391 billion to U.S. households. Research found that while the first two rounds of
stimulus checks generated massive abnormal returns in retail-dominated stock portfolios, the third round of stimulus produced
no significant positive portfolio return effects, and point estimates were insignificantly negative (Greenwood, Laarits, and
Wurgler 2022).
B.35 42: CHIPS and Science Act
Announcedon18May2021andimplementedon9August2022,thiswasalegislativepackagecommitting$52.7billionindirect
federal funding, subsidies, and investment tax credits to revitalize domestic semiconductor research, design, and fabrication, in
anefforttoreversethedeclineinU.S.semiconductormanufacturingcapacity,reducerelianceonforeignsupplychains,stimulate
private capital expenditure, and create high-paying domestic manufacturing jobs. Research revealed significant abnormal stock
returns for semiconductor firms on May 19, 2021, precisely when the precursor bill was introduced, but zero abnormal returns
upon the actual passage and signing of the Act in 2022(Erten, Stiglitz, and Verhoogen 2026). The act generated approximately
15,000 direct jobs (Erten, Stiglitz, and Verhoogen 2026).
B.36 43: Infrastructure Investment and Jobs Act (IIJA)
Announced on 10 August 2021 and implemented on 15 November 2021, this was a generational infrastructure package
authorizing approximately $1.2 trillion in total spending, including $550 billion in newly allocated federal investments across
transportation, broadband, water systems, and power grids. Analyses on previous similar ’Buy American’ provisions show that
these legislations significantly inflated the cost of federal procurement, and macroeconomic models show that the aggregate
impact onthe Fedfunds rate and10-year Treasury yieldsis quantitativelysmall due tothe spending beingspread overa decade
(Bombardini et al. 2024).
C Alternative Policy Identification LLM
PAWS uses an LLM acting as a tenured finance professor to identify impactful policies by leveraging the prevalent use of
policies as causal identification strategies in finance research. To examine if a finance research background is necessary, we
test an alternative LLM for identifying policies; one that acts as a renowned manager at a top U.S. hedge fund with decades of
experience.

As expected, this alternative policy identification LLM frequently hallucinates research papers and their documented policy
effects. Interestingly, this alternative policy identification LLM also misidentified the announcement and implementation dates
of approximately 30% of the identified policies, and even hallucinated a policy that does not exist.
D Event-Frame
D.1 Event-Frame Forms
Priortomulti-layerevent-frameclassification,eachactionisnormalizedintothreeclasses:Communication,DirectIntervention,
andObserved Effect. The normalized classification can be viewed as a legacy label, purely for reference.
The interaction-mode layer records how the event is realized, for examplecommunication,intent_or_plan,
institutional_action,request_or_pressure,material_action,legal_or_enforcement_action,
market_or_economic_state, orother. The family and subtype layers record the domain-level financial function and
more specific mechanism. This separation is important for policy analysis: a plan to provide liquidity, a legal authorization to
provide liquidity, and an actual liquidity transfer may share a policy function while differing in interaction mode and evidential
status.
The external crosswalks expose compatible views of the same action when applicable: CAMEO/GDELT-style actor interac-
tions (Schrodt 2012), Federal Reserve policy tools (Board of Governors of the Federal Reserve System 2025), ACE/ERE-style
event types (Walker et al. 2006), monetary-policy event classes (Gürkaynak, Sack, and Swanson 2005), IMF iMaPP macro-
prudential tools (Alam et al. 2019), and IMF crisis-response categories (Laeven and Valencia 2018). A crosswalk value of
not_applicablemeansthattheexternalontologyisnotstructurallylicensedfortheaction;itdoesnotmeanthattheaction
is missing or invalid.
Thefullcategoricalinventorycanbefoundinsupplementaryappendix(CategoricalInventory)attachedinthesupplementary
material.
D.2 Motivation
The first source is frame-semantic event representation. Frame semantics describes lexical meaning relative to a structured
situation (Fillmore 1982); FrameNet groups lexical units by the frame they evoke and identifies their participants (Baker,
Fillmore, and Lowe 1998). PropBank and Abstract Meaning Representation similarly motivate predicate–role representations
that abstract away from some changes in syntax and surface wording (Palmer, Gildea, and Kingsbury 2005; Banarescu et al.
2013). These traditions support representing an actor, target, transferred resource, instrument, and amount separately from the
event’s label. Thus,paid,provided funding, andinjected capitalmay instantiate closely related support/transfer semantics even
though their lexical realizations differ.
The second source is the separation of event content from communicative force and factual status. Speech-act theory
distinguishes assertions, directives, commitments, and declarations by their illocutionary point (Searle 1976). ACE, FactBank,
and TimeML separately motivate event typing, modality/factuality, and temporal or lifecycle information (Walker et al. 2006;
Saurí and Pustejovsky 2009; Pustejovsky et al. 2003). This distinction underliesinteraction\_mode: announcing an
intendedtransfer,authorizingit,andexecutingitcanconcernthesamesubstantivepolicyfunctionwhiledifferinginrealization
and commitment.
The third source is policy-instrument theory. The tools-of-government tradition distinguishes governing resources such as
information, legal authority, finance, and organizational capacity (Hood and Margetts 2007). Work on policy design further
separates the substantive instrument from the stage or procedure through which it is adopted (Howlett 2009). Financial-policy
practice supplies more domain-specific tool inventories: Federal Reserve policy tools, target and path information in monetary-
policy news, the IMF’s iMaPP macroprudential categories, and systemic-crisis response categories (Board of Governors of the
Federal Reserve System 2025; Gürkaynak, Sack, and Swanson 2005; Alam et al. 2019; Laeven and Valencia 2018).
Finally, the intended downstream use is agent-based simulation. BDI models and automated planning represent actions
as choices or operators available to an actor, with interpretable conditions and effects (Rao and Georgeff 1995; McDer-
mott 2000). This motivates a proposedevent\_routethat distinguishes intentionalagent\_actionevents from
environment_state_or_outcomeevents. A fall in prices is normally an environment transition; a central bank’s
sale of assets is an action that may contribute to that transition.
D.3 Dataset Statistics
EntityStarting from 13,720 unique nonblank entity strings, 7,810 (56.9%) were assigned to an organization. Alias consoli-
dation produced 4,317 canonical organization labels, of which 2,578 (59.7%) were linked to distinct Wikidata QIDs.
Event-FrameDistributionsFigure10revealsfinancial-actionfamilycompositionbypolicywhileFigure11showstheoverall
distribution of financial-action subtypes
News InformationFigure 12 shows the per-keyword daily origin-news distributions by policy.
Stakeholder InformationFigure 13 shows the organisations with the widest policy coverage.

Table 4: Actor identity-resolution and action-row coverage. Entity-level percentages use 13,720 unique entity strings as the
denominator, except Wikidata coverage, which uses 4,317 canonical labels. Row-level percentages use 31,460 action rows.
Measure Count Share
Identity resolution
Unique nonblank entity strings 13,720 100.0%
Entity strings assigned to an organization 7,810 56.9%
Canonical organization labels 4,317 –
Distinct Wikidata QIDs 2,578 59.7%
Action and ActionFrame coverage
Action / ActionFrame rows 31,460 / 31,460 100.0%
Rows linked to an organization 20,708 / 20,708 65.8%
Rows linked to a Wikidata QID 13,845 / 13,845 44.0%
Rows without an organization 10,752 / 10,752 34.2%
E Detailed Case Study Data
List of action_ids of the US announcing and implementing the short-selling ban: [598, 679, 671, 674, 687, 696, 707, 712,
758, 776].
List of action_ids of the UK announcing and implementing the short-selling ban: [625, 627, 686, 724, 672, 695, 702].
Some action_ids showing positive returns for non-finance stocks: [677, 812, 817, 818, 820, 822, 1069, 1071, 1072].
Some action_ids blaming short-sellers:[616, 648, 766, 797].
Some action_ids opposed to the short-selling bans: [10744, 1154].
Action_ids related to the MorganStanley retaliatory shorting: [1052, 1054, 1055].
Decimalization timeline: phase-in announcement (4391, 4392), delays (4399), NYSE completed (4468, 4469), Nasdaq
completed (4470, 4400), US all completed (4401).
Action_ids related to the suspicion of profit from fractional pricing: [4394, 4395, 4472, 4473].
Action_ids related to decimal pricing benefits for investors: [4396, 4397, 4472, 4474].
F Additional Simulation Diagnostics
This appendix reports compact simulation and feature-discovery diagnostics that support Section 6. We keep only plots that
directly clarify replay difficulty, model calibration, or feature signal.
G Additional Comparison to Related Work
Table7summarizeshowPAWSdiffersfromexistingsimulators,financialNLPdatasets,event-streamresources,andevent-study
databases. The comparison focuses on whether each line of work provides the ingredients needed for policy-driven multi-agent
simulation: temporally grounded policy evidence, policy intent, stakeholder actions, entity relevance, and realized market
context.
H Detailed Research Questions and Use Cases
PAWS is motivated by research questions that require policy context, stakeholder actions, and market outcomes to be studied
together. The dataset does not by itself solve causal identification in MAS, but it provides the temporally aligned evidence
needed to define and evaluate such questions.
Agent-to-Agent ImpactHow reliably can agents affect one another in bottom-up simulations? This question is crucial for
interpretable multiagent modelling, because a simulation should not only produce a final aggregate outcome but also explain
which agents influenced which other agents, and when. PAWS supports this line of work by linking policy-relevant actions to
datedstakeholdersandorganizations,enablingmulti-turnanalysisofagent-to-agentinteractions.Futureworkcanusethesetraces
to study topological mechanisms for selective influence, where only certain agents are expected to affect specific downstream
agents at particular timestamps.
Action-Outcome AlignmentDisregarding the efficiency of agent-to-agent causality, can a multiagent system generate out-
comes that are aligned with agentic actions? PAWS provides action types, actor identities, event dates, and surrounding policy
contextthatcanbeusedtotestwhethersimulatedoutcomesareconsistentwiththeactionsagentstake.Thisenablesresearchon
theparametersanddesignchoicesneededforalignedaction-outcomegeneration,includingagentmemory,interactiontopology,
policy conditioning, and temporal update rules.

Line of work Representative examples Primary focus Limitation for policy-driven MAS
Agent-based financial
simulation
ACF models, ABIDES, FinRL,
TradeMaster (Lebaron 2006;
Farmer and Foley 2009; Byrd,
Hybinette, and Balch 2019; Liu
et al. 2021; Sun et al. 2023)
Simulatingtraderbehavior,order-
book dynamics, market mecha-
nisms, or reinforcement-learning
trading policies.
Providessimulationinfrastructure,but
typicallydoesnotcuratehistoricalpol-
icy episodes with policy intent, stake-
holder responses, and realized market
context.
LLM-agent simulation Generative Agents, SOTOPIA,
QuantAgents, TradingA-
gents (Park et al. 2023; Zhou
et al. 2023; Li et al. 2025; Xiao
et al. 2024)
Modeling interactive agents that
communicate, remember, plan, or
collaborate in social and financial
settings.
Enables agent interaction, but still re-
quires grounded evidence to evaluate
whether simulated behavior matches
real policy episodes.
Financial language re-
sources
FinGPT, FinQA, FinRED,
Doc2EDAG,FINEED(Liuetal.
2023; Chen et al. 2022; Sharma
et al. 2023; Zheng et al. 2019;
Huang et al. 2024)
Financial text modeling, numeri-
cal reasoning, relation extraction,
and document-level event extrac-
tion.
Supports extraction and reasoning
overfinancialtext,butdoesnotjointly
align policy motivation, stakeholder
actions, entity relevance, and market
outcomes.
News event streams and
timelines
GDELT,ICEWS,EventRegistry,
timeline summarization (Ward
et al. 2013; Kwak and An 2016;
Hu, Moon, and Ng 2024; Sim
et al. 2026)
Broad event coverage, event clus-
tering,temporalorganization,and
timeline generation from news
streams.
Captures event structure at scale, but
is not specialized for finance-policy
interventions or downstream market
simulation.
Policy-shock and event-
study resources
Event studies, economic pol-
icyuncertainty,monetary-policy
event-study databases (MacKin-
lay 1997; Baker, Bloom, and
Davis 2016; Acosta et al. 2025)
Estimating or organizing the mar-
ket impact of discrete policy and
economic events.
Connects policy events to market re-
sponses, but is usually designed for
treatment-effectestimationratherthan
stakeholder-level simulation traces.
PAWSThis work Curated policy-centered episodes
with policy intent, natural-
language evidence, stakeholder
actions, entity relevance, and
financial-market context.
Provides a temporally grounded sub-
strate for studying policy-shock prop-
agation in multi-agent financial simu-
lation.
Table 5: Comparison between PAWS and related work. PAWS is designed to support policy-driven multi-agent simulation by
jointly preserving policy intent, stakeholder behavior, entity relevance, and realized market context.
ExpectedandUnexpectedPolicyOutcomesHowcanmultiagentAIsystemsrobustlycapturebothexpectedandunexpected
outcomes of policies? PAWS is designed around policies with documented intentions and observed market effects, allowing
models to compare intended policy goals with subsequent stakeholder reactions and market context. This supports future work
oncounterfactualpolicysimulation,robustnessunderregimeshifts,andtheabilityofagentpopulationstomodelunanticipated
second-order effects.

Figure 10: Financial-action family composition by policy. Each bar shows the shares of the seven most frequent families, with
remaining families pooled. Numeric codes correspond to the accompanying category key.

Figure 11: Overall distribution of financial-action subtypes. Bars show the shares of the eight most frequent subtypes, with
remaining subtypes pooled. Numeric codes correspond to the accompanying category key.

Figure12:Per-keyworddailyorigin-newsdistributionsbypolicy.Dotsdenotemedians,diamondsdenotemeans,thicksegments
showinterquartileranges,andthinsegmentsshowthe10th–90thpercentilesacrossobservedpolicy-days.Thedashedlinemarks
the 20-item per-keyword reference.

Figure 13: Organisations with the widest policy coverage. Bar length shows the number of distinct policies, whileAreports the
corresponding number of Action rows. Generic actors, countries, markets, and indices are excluded.

Model N Acc. Macro-F1 Active-F1 Active Recall
Majority 8341 .980 .330 .000 .000
Transition 8341 .979 .330 .012 .006
Threshold ABM 8341 .969 .349 .080 .067
Hybrid ABM 8341 .947 .375 .095 .139
Structured classifier 8341 .877 .356 .112 .382
GPT-4oreplay 50 .240 .205 .718 .560
Table 6: Minimal multi-policy replay results fromminimal_first_study_outputs_llm. TheGPT-4oreplay is
bounded to a 50-row sample and should not be compared to full-panel models by raw accuracy.
I Additional Simulation Diagnostics
We ran a full-process replay for the September 2008 short-selling ban over a larger selected agent set. This setting evaluates
additional diffusion and opinion-dynamics baselines, including linear-threshold and independent-cascade models (Kempe,
Kleinberg, and Tardos 2003), a voter model (Holley and Liggett 1975), DeGroot consensus dynamics (DeGroot 1974), Bass
diffusion (Bass 1969), structured-classifier, andGPT-4oLLM-agent variants. Models are compared using trigger prediction,
action-type accuracy, responder recall, timing error, action-distribution fit, and cascade-shape similarity.
This appendix reports compact simulation and feature-discovery diagnostics. We keep only plots that directly clarify replay
difficulty, model calibration, or feature signal.
Thissimulationdesignisintentionallymodular.Futureworkcanreplacethecurrentdecisionruleswithricheragentmemory,
role-conditioned prompts, selective agent-to-agent influence, counterfactual policy interventions, or explicit market-feedback
modules. Thus, the methodology defines both the PAWS dataset construction procedure and the replay interface needed to test
whether multi-agent systems can reproduce expected and unexpected responses to financial policy shocks.
I.1 Minimal Multi-Policy Replay
Table 6 reports theGPT-4o-augmented minimal study over five policy events. The majority and transition baselines achieve
highaccuracybypredictingalmostallrowsasnoaction,buttheiractive-actionF1isnearzero.ThethresholdandhybridABM
variants recover some active days, while the structured classifier has the highest active recall among full-panel models. The
boundedGPT-4oreplay is evaluated only on a 50-row subset and is therefore not directly comparable by raw accuracy.
Figure 14: Core metrics for the minimal multi-policy replay. This figure is moved from the main text because it supports the
same imbalance argument as Table 6.
Thestructuredclassifierprovidesthebestactive-F1andmacro-F1,whiletheGPT-4oLLM-agentvariantobtainsthehighest
active recall but substantially over-triggers. The Markov baseline produces the closest action-distribution fit, suggesting that

(a) Top feature signals
 (b) Feature-group strength
Figure 15: Feature-discovery diagnostics for action triggering. Identity, prior state, network structure, and neighbor context
provide the strongest trigger signal.
simpletemporalpersistencecanmatchaggregateactionratesevenwhenitmissesmanyspecificresponders.Table6reportsthe
GPT-4o-augmented minimal study over policy five. The majority and transition baselines achieve high accuracy by predicting
almost all rows asno action, but their active-action F1 is near zero. The threshold and hybrid ABM variants recover some
active days, while the structured classifier has the highest active recall among full-panel models. The boundedGPT-4oreplay
is evaluated only on a 50-row subset and is therefore not directly comparable by raw accuracy. The post-calibration Policy
5 split in the same output directory contains 560 panel rows and confirms this interpretation. No-action diffusion baselines
again reach high accuracy (.939) but zero active-F1. TheGPT-4oLLM-agent variant reaches .824 active recall but only .122
active-F1, while the structured classifier is more conservative, with .069 active-F1 and .176 active recall. These results suggest
that calibration remains the central challenge for action-triggering models.
Feature-discoverydiagnosticsWealsorunafeature-discoverystudyovertheLLM-augmentedpanelusingbalancedlogistic
regression, L1-regularized logistic regression, and random forests (Tibshirani 1996; Breiman 2001; Pedregosa et al. 2011).
Rather than introducing another simulator, this study diagnoses which PAWS fields are predictive for downstream simulation
tasks.
The top-ranked discovered features further clarify the dataset signal. For trigger prediction, the highest-ranked features are
org_id, previous label, weighted degree, neighbor context score, and policy identity. For action-type prediction, the leading
features areorg_id, article count, recent policy activity, recent policy context activity, and previous label. For sentiment,
the leading features areorg_id, weighted degree, relevance score, policy-level intervention count, and policy identity. These
diagnostics support placing feature discovery in the simulation-results section: it evaluates the replay interface by identifying
which dataset fields models actually use.
I.2 Feature-Discovery Diagnostics
Figures17–18providecompactfeature-discoverydiagnosticsforthereplaytasks.Theseplotsidentifywhichinputgroupscarry
the strongest signal for action triggering, action-type prediction, and sentiment prediction.

(a) Top feature signals
 (b) Feature-group strength
Figure 16: Feature-discovery diagnostics for action-type prediction. Agent identity and article-frequency features dominate,
indicating that organizations have stable action-mode tendencies in the current panel.
(a) Top feature signals
 (b) Feature-group strength
Figure 17: Feature-discovery diagnostics for sentiment prediction. The weak and diffuse signal is consistent with the validation
finding that policy-event sentiment is often target-dependent and unstable.

(a) Top feature signals
(b) Feature-group strength
Figure 18: Feature-discovery diagnostics for action triggering. Identity, prior state, network structure, and neighbor context
provide the strongest trigger signal.

Line of work Representative examples Primary focus Limitation for policy-driven MAS
Agent-based financial
simulation
ACF models, ABIDES, FinRL,
TradeMaster (Lebaron 2006;
Farmer and Foley 2009; Byrd,
Hybinette, and Balch 2019; Liu
et al. 2021; Sun et al. 2023)
Simulatingtraderbehavior,order-
book dynamics, market mecha-
nisms, or reinforcement-learning
trading policies.
Providessimulationinfrastructure,but
typicallydoesnotcuratehistoricalpol-
icy episodes with policy intent, stake-
holder responses, and realized market
context.
LLM-agent simulation Generative Agents, SOTOPIA,
QuantAgents, TradingA-
gents (Park et al. 2023; Zhou
et al. 2023; Li et al. 2025; Xiao
et al. 2024)
Modeling interactive agents that
communicate, remember, plan, or
collaborate in social and financial
settings.
Enables agent interaction, but still re-
quires grounded evidence to evaluate
whether simulated behavior matches
real policy episodes.
Financial language re-
sources
FinGPT, FinQA, FinRED,
Doc2EDAG,FINEED(Liuetal.
2023; Chen et al. 2022; Sharma
et al. 2023; Zheng et al. 2019;
Huang et al. 2024)
Financial text modeling, numeri-
cal reasoning, relation extraction,
and document-level event extrac-
tion.
Supports extraction and reasoning
overfinancialtext,butdoesnotjointly
align policy motivation, stakeholder
actions, entity relevance, and market
outcomes.
News event streams and
timelines
GDELT,ICEWS,EventRegistry,
timeline summarization (Ward
et al. 2013; Kwak and An 2016;
Hu, Moon, and Ng 2024; Sim
et al. 2026)
Broad event coverage, event clus-
tering,temporalorganization,and
timeline generation from news
streams.
Captures event structure at scale, but
is not specialized for finance-policy
interventions or downstream market
simulation.
Policy-shock and event-
study resources
Event studies, economic pol-
icyuncertainty,monetary-policy
event-study databases (MacKin-
lay 1997; Baker, Bloom, and
Davis 2016; Acosta et al. 2025)
Estimating or organizing the mar-
ket impact of discrete policy and
economic events.
Connects policy events to market re-
sponses, but is usually designed for
treatment-effectestimationratherthan
stakeholder-level simulation traces.
PAWSThis work Curated policy-centered episodes
with policy intent, natural-
language evidence, stakeholder
actions, entity relevance, and
financial-market context.
Provides a temporally grounded sub-
strate for studying policy-shock prop-
agation in multi-agent financial simu-
lation.
Table 7: Comparison between PAWS and related work. PAWS is designed to support policy-driven multi-agent simulation by
jointly preserving policy intent, stakeholder behavior, entity relevance, and realized market context.
J Additional Comparison to Related Work
Table7summarizeshowPAWSdiffersfromexistingsimulators,financialNLPdatasets,event-streamresources,andevent-study
databases. The comparison focuses on whether each line of work provides the ingredients needed for policy-driven multi-agent
simulation: temporally grounded policy evidence, policy intent, stakeholder actions, entity relevance, and realized market
context.

K Detailed Research Questions and Use Cases
PAWS is motivated by research questions that require policy context, stakeholder actions, and market outcomes to be studied
together. The dataset does not by itself solve causal identification in MAS, but it provides the temporally aligned evidence
needed to define and evaluate such questions.
Agent-to-Agent ImpactHow reliably can agents affect one another in bottom-up simulations? This question is crucial for
interpretable multiagent modelling, because a simulation should not only produce a final aggregate outcome but also explain
which agents influenced which other agents, and when. PAWS supports this line of work by linking policy-relevant actions to
datedstakeholdersandorganizations,enablingmulti-turnanalysisofagent-to-agentinteractions.Futureworkcanusethesetraces
to study topological mechanisms for selective influence, where only certain agents are expected to affect specific downstream
agents at particular timestamps.
Action-Outcome AlignmentDisregarding the efficiency of agent-to-agent causality, can a multiagent system generate out-
comes that are aligned with agentic actions? PAWS provides action types, actor identities, event dates, and surrounding policy
contextthatcanbeusedtotestwhethersimulatedoutcomesareconsistentwiththeactionsagentstake.Thisenablesresearchon
theparametersanddesignchoicesneededforalignedaction-outcomegeneration,includingagentmemory,interactiontopology,
policy conditioning, and temporal update rules.
ExpectedandUnexpectedPolicyOutcomesHowcanmultiagentAIsystemsrobustlycapturebothexpectedandunexpected
outcomes of policies? PAWS is designed around policies with documented intentions and observed market effects, allowing
models to compare intended policy goals with subsequent stakeholder reactions and market context. This supports future work
oncounterfactualpolicysimulation,robustnessunderregimeshifts,andtheabilityofagentpopulationstomodelunanticipated
second-order effects.

L Complete EventFrame Category Inventory
Applicability convention.The stored valuenot_applicable, shown hereafter asn/a, denotes structural ineligibility rather
than missingness or uncertainty. It is available to every independently gated crosswalk (CAMEO, Federal Reserve tools,
ACE/ERE, monetary policy, iMaPP, and IMF crisis response) and, where appropriate, to status and direction. CAMEO and
ACE child fields inheritn/afrom their parent. To avoid ten repetitive rows, this shared value is declared once here and omitted
from the inventory below.
Table 8: Substantive category inventory for the EventFrame representation. The shared structuraln/avalue is defined above
rather than repeated under every eligible field. Proposed layers are not yet adjudicated; external crosswalks are independently
gated.
Layer Category Parent or constraint Meaning Provenance
event_route
(proposed)
agent_action— An intentional choice attributable to an actor and
potentially available in the MAS action space.
Project synthesis
from BDI/planning
event_route
(proposed)
environment_state_or_
outcome
— An observed transition or outcome that normally be-
longs to the environment rather than an actor’s se-
lectable action set.
Project synthesis
from BDI/planning
underlying_
policy_function
(proposed)
information_signal_or_
disclosure
— Provide, disclose, forecast, warn, endorse, criticize,
orotherwisechangetheinformationavailabletoother
agents.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
influence_request_or_
pressure
— Try to induce another actor to act or refrain from
actingthroughanappeal,request,demand,rejection,
threat, or protest.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
coordination_consultation_
or_commitment
— Consult, negotiate, agree, or express a commitment
to cooperate. When a concrete embedded policy ac-
tionexists,thatpolicyfunctionshouldsupersedethis
fallback.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
monetary_stance— Set or signal the current/future monetary-policy
stance.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
market_and_reserve_
management
— Conduct open-market, repo, reserve-framework, or
related balance-sheet operations.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
liquidity_or_credit_
support
— Provide or operate central-bank or public liquidity
and credit facilities.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
fiscal_or_public_
financial_support
— Transferpublicresources,guarantees,subsidies,cap-
ital, asset purchases, tax support, or fiscal spending.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
regulation_or_supervision— Create, change, apply, approve, or supervise binding
financial rules.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
investigation_enforcement_
or_legal_remedy
— Investigate, charge, sue, adjudicate, penalize, settle,
or otherwise use a legal/enforcement process.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
authorization_or_
governance
— Vote, enact, authorize, or make a formal governance
decision. If the authorized policy’s substantive func-
tion is known, store it separately.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
market_transaction_or_
financing
— Buy, sell, issue, repay, lend, or otherwise transact in
financial claims.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
restructuring_resolution_
or_insolvency
— Merge, restructure, resolve, nationalize, liquidate, or
enter insolvency.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
business_operations— Change production, employment, plants, supply, or
other firm operations.
Project synthesis:
frames, policy tools,
MAS
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
underlying_
policy_function
(proposed)
other_agent_action— An intentional actor choice outside the listed func-
tions.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
market_price_or_liquidity_
state
— An environment state/outcome involving prices,
spreads, volatility, liquidity, volume, or flows.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
credit_or_balance_sheet_
state
— Anenvironmentstate/outcomeinvolvingratings,de-
fault, losses, earnings, or balance-sheet liquidity.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
macroeconomic_or_real_
activity_state
— An environment state/outcome involving employ-
ment, production, inflation, or demand.
Project synthesis:
frames, policy tools,
MAS
underlying_
policy_function
(proposed)
other_environment_state— Anobservedenvironmentoutcomeoutsidethelisted
states.
Project synthesis:
frames, policy tools,
MAS
legacy_action_
type
Communication— Legacy broad communicative event. Original project
three-way schema
legacy_action_
type
Direct Intervention— Legacy broad intentional intervention. Original project
three-way schema
legacy_action_
type
Observed Effect— Legacy observed outcome or state. Original project
three-way schema
interaction_
mode
communication— A statement, announcement, disclosure, forecast,
opinion, warning, consultation, or other primarily
communicative act.
Project extension;
speech acts and event
factuality
interaction_
mode
intent_or_plan— A proposal, plan, consideration, commitment, goal,
or future course of action that is not yet completed.
Project extension;
speech acts and event
factuality
interaction_
mode
request_or_pressure— A request, demand, appeal, lobbying effort, pressure
tactic, or threat directed toward another actor.
Project extension;
speech acts and event
factuality
interaction_
mode
material_action— A completed or ongoing resource transfer, transac-
tion, funding operation, investment, business opera-
tion, or other concrete act.
Project extension;
speech acts and event
factuality
interaction_
mode
institutional_action— A formal policy, legislative, regulatory, governance,
authorization, monetary-policy, or institutional-
resolution decision.
Project extension;
speech acts and event
factuality
interaction_
mode
market_or_economic_state— An observed price, yield, spread, liquidity, volume,
production,financial-result,credit,rating,default,or
macroeconomic state.
Project extension;
speech acts and event
factuality
interaction_
mode
legal_or_enforcement_
action
— An investigation, charge, lawsuit, adjudication, fine,
settlement,arrest,sentence,orenforcementproceed-
ing.
Project extension;
speech acts and event
factuality
interaction_
mode
other— The event does not fit the seven more specific inter-
action modes with sufficient semantic support.
Project extension;
speech acts and event
factuality
financial_
action_family
cameo_01_make_public_
statement
— CAMEO root 01 MAKE PUBLIC STATEMENT Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_02_appeal_or_10_
demand
— CAMEO root 02 APPEAL or root 10 DEMAND Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_03_express_intent_
to_cooperate
— CAMEOroot03EXPRESSINTENTTOCOOPER-
ATE
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_04_consult— CAMEO root 04 CONSULT Project synthe-
sis: CAMEO, Fed,
finance extensions
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
financial_
action_family
fed_monetary_policy_rate_
guidance
— Federal Reserve monetary policy implementa-
tion/rate guidance
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
fed_open_market_and_
reserve_operations
— Federal Reserve Policy Tools: open market opera-
tions, reserve requirements, IORB, ON RRP, term
deposits, liquidity swaps, FIMA repo, standing repo
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
fed_lending_and_liquidity_
facilities
— Federal Reserve Policy Tools and Expired Policy
Tools:discountwindowandliquidity/creditfacilities
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_07_provide_aid_or_
public_support
— CAMEO root07 PROVIDEAID, extended topublic
financial support
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_17_coerce_or_
financial_regulation
— CAMEO root 17 COERCE, extended to binding fi-
nancial regulation/supervision
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_09_investigate_or_
legal_enforcement
— CAMEO root 09 INVESTIGATE, extended to legal
enforcement outcomes
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_11_disapprove_or_12_
reject
— CAMEO root 11 DISAPPROVE or root 12 REJECT Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_13_threaten— CAMEO root 13 THREATEN Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
cameo_14_protest— CAMEO root 14 PROTEST Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
financial_market_
transaction
— Finance-specific extension for market transactions
not covered by CAMEO/Fed tools
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
financial_resolution_
restructuring_or_
bankruptcy
— Finance-specificextensionforinsolvency,resolution,
restructuring, and control-change events
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
business_operations_
adjustment
— Finance-specific extension for firm operational
changes
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
market_price_or_liquidity_
effect
— Finance-specific world-state extension for observed
marketprices,spreads,volatility,liquidity,andflows
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
credit_rating_or_balance_
sheet_effect
— Finance-specific world-state extension for credit rat-
ings, defaults, losses, earnings, and liquidity
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
macroeconomic_real_
activity_effect
— Finance-specific world-state extension for employ-
ment, production, inflation, and demand
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
legislative_policy_
authorization
— Finance-specificcategoryforlegislativevotes,enact-
ment, and public-policy authorization
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_family
other_financial_event— Fallback for financially relevant events that do not fit
the anchored taxonomy
Project synthe-
sis: CAMEO, Fed,
finance extensions
financial_
action_subtype
statement cameo_01_make_public_
statement
Fine-grained mechanism: statement. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
pessimistic_comment cameo_01_make_public_
statement
Fine-grained mechanism: pessimistic comment. Project finance-
specific mechanism
vocabulary
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
financial_
action_subtype
optimistic_comment cameo_01_make_public_
statement
Fine-grained mechanism: optimistic comment. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
warning cameo_01_make_public_
statement; cameo_13_
threaten
Fine-grained mechanism: warning. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
forecast cameo_01_make_public_
statement
Fine-grained mechanism: forecast. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
denial cameo_01_make_public_
statement; cameo_11_
disapprove_or_12_reject
Fine-grained mechanism: denial. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
disclosure_report cameo_01_make_public_
statement
Fine-grained mechanism: disclosure report. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
testimony cameo_01_make_public_
statement
Fine-grained mechanism: testimony. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
proposal cameo_02_appeal_or_
10_demand; cameo_03_
express_intent_to_
cooperate; cameo_04_
consult; legislative_
policy_authorization
Fine-grained mechanism: proposal. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
demand_request cameo_02_appeal_or_10_
demand
Fine-grained mechanism: demand request. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
support_endorsement cameo_01_make_public_
statement; cameo_02_
appeal_or_10_demand
Fine-grained mechanism: support endorsement. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
opposition_criticism cameo_01_make_public_
statement; cameo_02_
appeal_or_10_demand;
cameo_11_disapprove_
or_12_reject; cameo_14_
protest
Fine-grained mechanism: opposition criticism. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
negotiation_meeting cameo_02_appeal_or_10_
demand; cameo_04_consult
Fine-grained mechanism: negotiation meeting. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
agreement cameo_02_appeal_or_
10_demand; cameo_03_
express_intent_to_
cooperate; cameo_04_
consult
Fine-grained mechanism: agreement. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
plan_intent cameo_03_express_intent_
to_cooperate
Fine-grained mechanism: plan intent. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
threat cameo_02_appeal_or_
10_demand; cameo_03_
express_intent_to_
cooperate; cameo_13_
threaten
Fine-grained mechanism: threat. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
rejection_refusal cameo_11_disapprove_or_
12_reject
Fine-grained mechanism: rejection refusal. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
protest_action cameo_14_protestFine-grained mechanism: protest action. Project finance-
specific mechanism
vocabulary
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
financial_
action_subtype
target_rate_change fed_monetary_policy_
rate_guidance
Fine-grained mechanism: target rate change. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
rate_guidance fed_monetary_policy_
rate_guidance
Fine-grained mechanism: rate guidance. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
open_market_purchase fed_open_market_and_
reserve_operations
Fine-grained mechanism: open market purchase. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
open_market_sale fed_open_market_and_
reserve_operations
Fine-grained mechanism: open market sale. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
repo_operation fed_open_market_and_
reserve_operations
Fine-grained mechanism: repo operation. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
reverse_repo_operation fed_open_market_and_
reserve_operations
Fine-grained mechanism: reverse repo operation. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
standing_repo_operation fed_open_market_and_
reserve_operations
Fine-grained mechanism: standing repo operation. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
term_deposit_operation fed_open_market_and_
reserve_operations
Fine-grained mechanism: term deposit operation. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
reserve_requirement_change fed_open_market_and_
reserve_operations
Fine-grained mechanism: reserve requirement
change.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
interest_on_reserve_
balances_change
fed_monetary_policy_
rate_guidance
Fine-grainedmechanism:interestonreservebalances
change.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
discount_window_primary_
credit
fed_lending_and_
liquidity_facilities
Fine-grained mechanism: discount window primary
credit.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
discount_window_secondary_
credit
fed_lending_and_
liquidity_facilities
Fine-grained mechanism: discount window sec-
ondary credit.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
discount_window_seasonal_
credit
fed_lending_and_
liquidity_facilities
Fine-grained mechanism: discount window seasonal
credit.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
central_bank_liquidity_
swap
fed_open_market_and_
reserve_operations
Fine-grained mechanism: central bank liquidity
swap.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
fima_repo_facility fed_open_market_and_
reserve_operations
Fine-grained mechanism: fima repo facility. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
term_auction_facility fed_lending_and_
liquidity_facilities
Fine-grained mechanism: term auction facility. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
commercial_paper_funding_
facility
fed_lending_and_
liquidity_facilities
Fine-grained mechanism: commercial paper funding
facility.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
primary_dealer_credit_
facility
fed_lending_and_
liquidity_facilities
Fine-grainedmechanism:primarydealercreditfacil-
ity.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
money_market_liquidity_
facility
fed_lending_and_
liquidity_facilities
Fine-grainedmechanism:moneymarketliquidityfa-
cility.
Project finance-
specific mechanism
vocabulary
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
financial_
action_subtype
term_asset_backed_
securities_loan_facility
fed_lending_and_
liquidity_facilities
Fine-grained mechanism: term asset backed securi-
ties loan facility.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
term_securities_lending_
facility
fed_lending_and_
liquidity_facilities
Fine-grained mechanism: term securities lending fa-
cility.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
maturity_extension_
reinvestment
— Fine-grained mechanism: maturity extension rein-
vestment.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
corporate_credit_facility fed_lending_and_
liquidity_facilities
Fine-grained mechanism: corporate credit facility. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
municipal_liquidity_
facility
fed_lending_and_
liquidity_facilities
Fine-grainedmechanism:municipalliquidityfacility. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
main_street_lending_
program
fed_lending_and_
liquidity_facilities
Fine-grained mechanism: main street lending pro-
gram.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
paycheck_protection_
liquidity_facility
fed_lending_and_
liquidity_facilities
Fine-grainedmechanism:paycheckprotectionliquid-
ity facility.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
public_bailout cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: public bailout. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
capital_injection cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: capital injection. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
guarantee cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: guarantee. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
asset_purchase_program cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: asset purchase program. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
tax_change cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: tax change. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
fiscal_spending cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: fiscal spending. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
subsidy cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: subsidy. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
lending_support fed_lending_and_
liquidity_facilities;
cameo_07_provide_aid_or_
public_support
Fine-grained mechanism: lending support. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
collateral_policy fed_open_market_and_
reserve_operations; fed_
lending_and_liquidity_
facilities
Fine-grained mechanism: collateral policy. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
rule_change cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: rule change. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
trading_restriction cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: trading restriction. Project finance-
specific mechanism
vocabulary
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
financial_
action_subtype
short_selling_ban cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: short selling ban. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
capital_requirement cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: capital requirement. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
liquidity_requirement cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: liquidity requirement. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
disclosure_requirement cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: disclosure requirement. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
supervisory_approval cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: supervisory approval. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
merger_approval cameo_17_coerce_or_
financial_regulation
Fine-grained mechanism: merger approval. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
enforcement_investigation cameo_09_investigate_or_
legal_enforcement
Fine-grained mechanism: enforcement investigation. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
lawsuit cameo_09_investigate_or_
legal_enforcement
Fine-grained mechanism: lawsuit. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
fine_penalty cameo_09_investigate_or_
legal_enforcement
Fine-grained mechanism: fine penalty. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
settlement cameo_09_investigate_or_
legal_enforcement
Fine-grained mechanism: settlement. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
criminal_charge cameo_09_investigate_or_
legal_enforcement
Fine-grained mechanism: criminal charge. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
bankruptcy_filing financial_resolution_
restructuring_or_
bankruptcy
Fine-grained mechanism: bankruptcy filing. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
bankruptcy_protection financial_resolution_
restructuring_or_
bankruptcy
Fine-grained mechanism: bankruptcy protection. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
liquidation financial_resolution_
restructuring_or_
bankruptcy
Fine-grained mechanism: liquidation. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
nationalization financial_resolution_
restructuring_or_
bankruptcy
Fine-grained mechanism: nationalization. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
merger_acquisition financial_resolution_
restructuring_or_
bankruptcy
Fine-grained mechanism: merger acquisition. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
asset_sale financial_resolution_
restructuring_or_
bankruptcy
Fine-grained mechanism: asset sale. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
divestiture financial_resolution_
restructuring_or_
bankruptcy
Fine-grained mechanism: divestiture. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
share_buyback financial_market_
transaction
Fine-grained mechanism: share buyback. Project finance-
specific mechanism
vocabulary
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
financial_
action_subtype
dividend_change financial_market_
transaction
Fine-grained mechanism: dividend change. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
debt_issue financial_market_
transaction
Fine-grained mechanism: debt issue. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
equity_issue financial_market_
transaction
Fine-grained mechanism: equity issue. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
security_purchase financial_market_
transaction
Fine-grained mechanism: security purchase. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
security_sale financial_market_
transaction
Fine-grained mechanism: security sale. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
short_sale financial_market_
transaction
Fine-grained mechanism: short sale. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
loan_origination financial_market_
transaction
Fine-grained mechanism: loan origination. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
loan_repayment financial_market_
transaction
Fine-grained mechanism: loan repayment. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
credit_rating_change credit_rating_or_
balance_sheet_effect
Fine-grained mechanism: credit rating change. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
default credit_rating_or_
balance_sheet_effect
Fine-grained mechanism: default. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
loss_write_down credit_rating_or_
balance_sheet_effect
Fine-grained mechanism: loss write down. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
earnings_profit_loss credit_rating_or_
balance_sheet_effect
Fine-grained mechanism: earnings profit loss. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
price_move market_price_or_
liquidity_effect
Fine-grained mechanism: price move. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
yield_spread_move market_price_or_
liquidity_effect
Fine-grained mechanism: yield spread move. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
volatility_move market_price_or_
liquidity_effect
Fine-grained mechanism: volatility move. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
liquidity_condition market_price_or_
liquidity_effect;
credit_rating_or_
balance_sheet_effect
Fine-grained mechanism: liquidity condition. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
volume_flow_change market_price_or_
liquidity_effect
Fine-grained mechanism: volume flow change. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
employment_change business_operations_
adjustment;
macroeconomic_real_
activity_effect
Fine-grained mechanism: employment change. Project finance-
specific mechanism
vocabulary
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
financial_
action_subtype
production_output_change business_operations_
adjustment;
macroeconomic_real_
activity_effect
Fine-grained mechanism: production output change. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
inflation_price_level_
change
macroeconomic_real_
activity_effect
Fine-grainedmechanism:inflationpricelevelchange. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
consumer_business_demand_
change
macroeconomic_real_
activity_effect
Fine-grained mechanism: consumer business de-
mand change.
Project finance-
specific mechanism
vocabulary
financial_
action_subtype
legislative_vote legislative_policy_
authorization
Fine-grained mechanism: legislative vote. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
law_enactment legislative_policy_
authorization
Fine-grained mechanism: law enactment. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
policy_authorization legislative_policy_
authorization
Fine-grained mechanism: policy authorization. Project finance-
specific mechanism
vocabulary
financial_
action_subtype
no_subtype cameo_01_make_public_
statement; cameo_02_
appeal_or_10_demand;
cameo_03_express_intent_
to_cooperate; cameo_04_
consult; fed_monetary_
policy_rate_guidance;
fed_open_market_and_
reserve_operations; fed_
lending_and_liquidity_
facilities; cameo_07_
provide_aid_or_public_
support; cameo_17_
coerce_or_financial_
regulation; cameo_09_
investigate_or_legal_
enforcement; cameo_
11_disapprove_or_
12_reject; cameo_13_
threaten; cameo_14_
protest; financial_
market_transaction;
financial_resolution_
restructuring_or_
bankruptcy; business_
operations_adjustment;
market_price_or_
liquidity_effect;
credit_rating_or_
balance_sheet_effect;
macroeconomic_real_
activity_effect;
legislative_policy_
authorization; other_
financial_event
Fine-grained mechanism: no subtype. Project finance-
specific mechanism
vocabulary
cameo_root_code 01 quad=verbal_cooperationmake_public_statement:Anactormakesapublicver-
bal or written statement.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 02 quad=verbal_cooperationappeal: An actor appeals for another actor to act vol-
untarily.
CAMEO/GDELT
(Schrodt 2012)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
cameo_root_code 03 quad=verbal_cooperationexpress_intent_to_cooperate: An actor expresses an
intention to cooperate in the future.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 04 quad=verbal_cooperationconsult: Actors consult, meet, discuss, or negotiate. CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 05 quad=verbal_cooperationengage_in_diplomatic_cooperation: Actors engage
in diplomatic cooperation, such as agreements or
diplomatic support.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 06 quad=material_
cooperation
engage_in_material_cooperation: Actors engage in
materialcooperationotherthanaid,suchasjointma-
terial activity.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 07 quad=material_
cooperation
provide_aid: An actor provides material aid or sup-
port to another actor.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 08 quad=material_
cooperation
yield:Anactoryieldsormakesasubstantiveconces-
sion.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 09 quad=verbal_conflictinvestigate: An actor investigates another actor or an
alleged act.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 10 quad=verbal_conflictdemand:Anactordemandsthatanotheractortakeor
stop an action.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 11 quad=verbal_conflictdisapprove: An actor publicly disapproves of, criti-
cizes, or denounces another actor.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 12 quad=verbal_conflictreject:Anactorrejectsorrefusesarequest,proposal,
or cooperation.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 13 quad=verbal_conflictthreaten:Anactorthreatensafuturecoerciveorharm-
ful action.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 14 quad=material_conflictprotest: An actor protests or demonstrates. CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 15 quad=material_conflictexhibit_force_posture: An actor displays military or
coercive force posture without attacking.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 16 quad=material_conflictreduce_relations:Anactorformallyreducesorbreaks
relations with another actor.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 17 quad=material_conflictcoerce: An actor coerces another actor through non-
violent restrictions or forceful measures.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 18 quad=material_conflictassault: An actor physically assaults or attacks an-
other actor.
CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 19 quad=material_conflictfight: Actors engage in armed fighting. CAMEO/GDELT
(Schrodt 2012)
cameo_root_code 20 quad=material_conflictuse_unconventional_mass_violence: An actor uses
unconventional mass violence.
CAMEO/GDELT
(Schrodt 2012)
cameo_code official child code must begin with cameo_
root_code
Most-specific two-to-four digit CAMEO code when
theofficialhierarchysupportsmoredetail;otherwise
the root is copied.
CAMEO/GDELT
(Schrodt 2012)
cameo_quad_
class
verbal_cooperation— Verbal cooperative interaction (roots 01–05). Derived from
CAMEO roots
(Schrodt 2012)
cameo_quad_
class
material_cooperation— Material cooperative interaction (roots 06–08). Derived from
CAMEO roots
(Schrodt 2012)
cameo_quad_
class
verbal_conflict— Verbal conflict interaction (roots 09–13). Derived from
CAMEO roots
(Schrodt 2012)
cameo_quad_
class
material_conflict— Material conflict interaction (roots 14–20). Derived from
CAMEO roots
(Schrodt 2012)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
fed_policy_
tool_class
open_market_operations— Federal Reserve purchases or sales of securities in
open markets.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
discount_window— Federal Reserve primary, secondary, or seasonal
credit to depository institutions.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
reserve_requirements— Federal Reserve requirements governing depository-
institution reserve balances.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
interest_on_reserve_
balances
— Federal Reserve changes to interest paid on reserve
balances (IORB).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
overnight_reverse_
repurchase_agreement_
operations
— Federal Reserve overnight reverse repo operations
(ON RRP).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
term_deposit_facility— FederalReservetermdepositsusedtoabsorbreserve
balances.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
central_bank_liquidity_
swaps
— Federal Reserve dollar-liquidity swap lines with for-
eign central banks.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
fima_repo_facility— Federal Reserve repo facility for Foreign and Inter-
national Monetary Authorities.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
standing_repurchase_
agreement_operations
— Federal Reserve standing repo operations (SRF). Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
commercial_paper_funding_
facility
— TheFederalReserveCommercialPaperFundingFa-
cility (CPFF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
primary_dealer_credit_
facility
— The Federal Reserve Primary Dealer Credit Facility
(PDCF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
fed_policy_
tool_class
money_market_mutual_fund_
liquidity_facility
— The Federal Reserve Money Market Mutual Fund
Liquidity Facility (MMLF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
primary_market_corporate_
credit_facility
— The Federal Reserve Primary Market Corporate
Credit Facility (PMCCF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
secondary_market_
corporate_credit_facility
— The Federal Reserve Secondary Market Corporate
Credit Facility (SMCCF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
term_asset_backed_
securities_loan_facility
— The Federal Reserve Term Asset-Backed Securities
Loan Facility (TALF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
paycheck_protection_
program_liquidity_facility
— The Federal Reserve Paycheck Protection Program
Liquidity Facility (PPPLF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
municipal_liquidity_
facility
— The Federal Reserve Municipal Liquidity Facility
(MLF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
main_street_lending_
program
— The Federal Reserve Main Street Lending Program. Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
money_market_investor_
funding_facility
— TheFederalReserveMoneyMarketInvestorFunding
Facility (MMIFF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
abcp_money_market_mutual_
fund_liquidity_facility
— The Federal Reserve ABCP Money Market Mutual
Fund Liquidity Facility (AMLF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
term_securities_lending_
facility
— The Federal Reserve Term Securities Lending Facil-
ity (TSLF).
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
term_auction_facility— The Federal Reserve Term Auction Facility (TAF). Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
fed_policy_
tool_class
maturity_extension_
program_and_reinvestment_
policy
— Federal Reserve maturity-extension or balance-sheet
reinvestment policy.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
fed_policy_
tool_class
other_fed_tool— A clearly evidenced Federal Reserve instrument not
represented by another listed class.
Federal Reserve tool
catalogue (Board of
GovernorsoftheFed-
eral Reserve System
2025)
ace_event_type life— A person-level life event such as birth, marriage, in-
jury, or death.
ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_type movement— The physical transport or movement of a person or
artifact.
ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_type transaction— A transfer of money or ownership between partici-
pants.
ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_type business— Organization formation, merger, bankruptcy, or dis-
solution.
ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_type conflict— A physical attack or demonstration. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_type contact— A meeting, correspondence, or public broadcast by
participants.
ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_type personnel— A person starting, ending, being nominated for, or
elected to a position.
ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_type justice— Alegal-processeventsuchasarrest,charge,trial,suit,
conviction, or fine.
ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
life_be_born lifeACE/ERE-style life be born event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
life_marry lifeACE/ERE-style life marry event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
life_divorce lifeACE/ERE-style life divorce event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
life_injure lifeACE/ERE-style life injure event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
life_die lifeACE/ERE-style life die event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
movement_transport movementACE/ERE-style movement transport event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
transaction_transfer_
ownership
transactionACE/ERE-styletransactiontransferownershipevent. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
transaction_transfer_money transactionACE/ERE-style transaction transfer money event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
ace_event_
subtype
business_start_org businessACE/ERE-style business start org event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
business_merge_org businessACE/ERE-style business merge org event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
business_declare_
bankruptcy
businessACE/ERE-style business declare bankruptcy event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
business_end_org businessACE/ERE-style business end org event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
conflict_attack conflictACE/ERE-style conflict attack event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
conflict_demonstrate conflictACE/ERE-style conflict demonstrate event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
contact_meet contactACE/ERE-style contact meet event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
contact_phone_write contactACE/ERE-style contact phone write event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
contact_broadcast contactACE/ERE-style contact broadcast event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
personnel_start_position personnelACE/ERE-style personnel start position event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
personnel_end_position personnelACE/ERE-style personnel end position event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
personnel_nominate personnelACE/ERE-style personnel nominate event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
personnel_elect personnelACE/ERE-style personnel elect event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_arrest_jail justiceACE/ERE-style justice arrest jail event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_release_parole justiceACE/ERE-style justice release parole event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_trial_hearing justiceACE/ERE-style justice trial hearing event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_charge_indict justiceACE/ERE-style justice charge indict event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_sue justiceACE/ERE-style justice sue event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_convict justiceACE/ERE-style justice convict event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
ace_event_
subtype
justice_sentence justiceACE/ERE-style justice sentence event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_fine justiceACE/ERE-style justice fine event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_execute justiceACE/ERE-style justice execute event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_extradite justiceACE/ERE-style justice extradite event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_acquit justiceACE/ERE-style justice acquit event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_appeal justiceACE/ERE-style justice appeal event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
ace_event_
subtype
justice_pardon justiceACE/ERE-style justice pardon event. ACE/ERE-style
crosswalk (Walker
et al. 2006)
monetary_
policy_event_
class
target_rate_action— Acurrentcentral-bankpolicy-rateortarget-rangede-
cision.
Fed tools and tar-
get/path literature
(Gürkaynak, Sack,
and Swanson 2005)
monetary_
policy_event_
class
policy_path_forward_
guidance
— Communication about the expected future path of
monetary policy.
Fed tools and tar-
get/path literature
(Gürkaynak, Sack,
and Swanson 2005)
monetary_
policy_event_
class
balance_sheet_asset_
purchase_qe
— QE, asset purchases or sales, maturity extension, or
reinvestment policy.
Fed tools and tar-
get/path literature
(Gürkaynak, Sack,
and Swanson 2005)
monetary_
policy_event_
class
liquidity_facility_
operation
— A central-bank lending, repo, swap, discount-
window, or liquidity-facility operation.
Fed tools and tar-
get/path literature
(Gürkaynak, Sack,
and Swanson 2005)
monetary_
policy_event_
class
reserve_framework_
operation
— Areserve-requirement,reserve-interest,ON-RRP,or
term-deposit framework action.
Fed tools and tar-
get/path literature
(Gürkaynak, Sack,
and Swanson 2005)
imapp_
macroprudential_
tool_class
countercyclical_capital_
buffer
— Acountercyclicalcapitalbuffer(CCyB)requirement. IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
capital_conservation_
buffer
— Acapitalconservationbuffer,includingtheBaselIII
buffer.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
capital_requirement— Bank capital requirements, risk weights, systemic-
risk buffers, or minimum ratios.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
leverage_limit— Aregulatorylimitonbankleverageorleverageratios. IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
loan_loss_provision— Dynamic, sectoral, or other macroprudential loan-
loss provisioning.
IMF iMaPP (Alam
et al. 2019)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
imapp_
macroprudential_
tool_class
limit_on_credit_growth— Limits or penalties on aggregate or sectoral credit
growth or volume.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
loan_restriction— Loanprohibitionsorlimitsconditionedonloan,bor-
rower, or bank characteristics.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
limit_on_foreign_currency_
lending
— Limits, rules, or recommendations on foreign-
currency lending.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
loan_to_value_limit— Limits on loan-to-value (LTV) ratios. IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
debt_service_to_income_
limit
— Limits on DSTI, DTI, or loan-to-income ratios. IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
tax_measure— A macroprudential tax or levy on specified transac-
tions, assets, or liabilities.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
liquidity_requirement— Systemic-liquidityrequirementssuchasLCR,NSFR,
or liquid-asset ratios.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
loan_to_deposit_limit— Limits or penalties tied to loan-to-deposit ratios. IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
foreign_exchange_position_
limit
— Limits on FX positions, exposures, funding, or cur-
rency mismatches.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
reserve_requirement— Reserverequirementsusedforamacroprudentialpur-
pose.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
sifi_measure— Measures targeting systemically important institu-
tions, including surcharges.
IMF iMaPP (Alam
et al. 2019)
imapp_
macroprudential_
tool_class
other_macroprudential— Anexplicitlymacroprudentialsystemic-riskmeasure
not covered above.
IMF iMaPP (Alam
et al. 2019)
imf_crisis_
response_class
deposit_freeze_bank_
holiday
— Adepositfreeze,withdrawalrestriction,orbankhol-
iday used in a banking crisis.
IMF crisis-response
database (Laeven and
Valencia 2018)
imf_crisis_
response_class
bank_nationalization— Government takeover or controlling ownership of a
bank during a crisis response.
IMF crisis-response
database (Laeven and
Valencia 2018)
imf_crisis_
response_class
bank_restructuring_fiscal_
cost
— Public recapitalization, restructuring, or bailout cost
for distressed banks.
IMF crisis-response
database (Laeven and
Valencia 2018)
imf_crisis_
response_class
liquidity_support— Emergencyliquiditysupporttobanksorthefinancial
system during crisis stress.
IMF crisis-response
database (Laeven and
Valencia 2018)
imf_crisis_
response_class
bank_liability_guarantee— A public guarantee of bank deposits, debt, or other
liabilities during a crisis.
IMF crisis-response
database (Laeven and
Valencia 2018)
imf_crisis_
response_class
asset_purchase— Crisis-response purchase or transfer of impaired
banking-system assets.
IMF crisis-response
database (Laeven and
Valencia 2018)
imf_crisis_
response_class
expansionary_monetary_
policy
— Broad monetary easing used as part of a banking-
crisis response.
IMF crisis-response
database (Laeven and
Valencia 2018)
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
imf_crisis_
response_class
expansionary_fiscal_policy— Broad fiscal expansion used as part of a banking-
crisis response.
IMF crisis-response
database (Laeven and
Valencia 2018)
modality actual— actual Project attribute;
ACE/FactBank
motivation
modality announced— announced Project attribute;
ACE/FactBank
motivation
modality planned— planned Project attribute;
ACE/FactBank
motivation
modality proposed— proposed Project attribute;
ACE/FactBank
motivation
modality considered— considered Project attribute;
ACE/FactBank
motivation
modality forecast— forecast Project attribute;
ACE/FactBank
motivation
modality threatened— threatened Project attribute;
ACE/FactBank
motivation
modality denied— denied Project attribute;
ACE/FactBank
motivation
modality hypothetical— hypothetical Project attribute;
ACE/FactBank
motivation
modality reported— reported Project attribute;
ACE/FactBank
motivation
modality uncertain— uncertain Project attribute;
ACE/FactBank
motivation
status completed— completed Project lifecycle at-
tribute
status ongoing— ongoing Project lifecycle at-
tribute
status announced— announced Project lifecycle at-
tribute
status proposed— proposed Project lifecycle at-
tribute
status planned— planned Project lifecycle at-
tribute
status failed— failed Project lifecycle at-
tribute
status cancelled— cancelled Project lifecycle at-
tribute
status rumored— rumored Project lifecycle at-
tribute
status unknown— unknown Project lifecycle at-
tribute
direction ease— ease Project policy/effect
direction attribute
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
direction tighten— tighten Project policy/effect
direction attribute
direction increase— increase Project policy/effect
direction attribute
direction decrease— decrease Project policy/effect
direction attribute
direction maintain— maintain Project policy/effect
direction attribute
direction support— support Project policy/effect
direction attribute
direction oppose— oppose Project policy/effect
direction attribute
direction positive— positive Project policy/effect
direction attribute
direction negative— negative Project policy/effect
direction attribute
direction mixed— mixed Project policy/effect
direction attribute
direction neutral— neutral Project policy/effect
direction attribute
direction unknown— unknown Project policy/effect
direction attribute
actor_role central_bank— central bank Project semantic-
role/authority at-
tribute
actor_role treasury_or_finance_
ministry
— treasury or finance ministry Project semantic-
role/authority at-
tribute
actor_role regulator_supervisor— regulator supervisor Project semantic-
role/authority at-
tribute
actor_role legislature— legislature Project semantic-
role/authority at-
tribute
actor_role executive_government— executive government Project semantic-
role/authority at-
tribute
actor_role court_or_legal_authority— court or legal authority Project semantic-
role/authority at-
tribute
actor_role international_organization— international organization Project semantic-
role/authority at-
tribute
actor_role bank_financial_firm— bank financial firm Project semantic-
role/authority at-
tribute
actor_role nonfinancial_firm— nonfinancial firm Project semantic-
role/authority at-
tribute
actor_role investor_fund— investor fund Project semantic-
role/authority at-
tribute
actor_role rating_agency_researcher— rating agency researcher Project semantic-
role/authority at-
tribute
actor_role market_index_asset— market index asset Project semantic-
role/authority at-
tribute
Continued on next page

Table 8 — continued
Layer Category Parent or constraint Meaning Provenance
actor_role public_media— public media Project semantic-
role/authority at-
tribute
actor_role other— other Project semantic-
role/authority at-
tribute
actor_role unknown— unknown Project semantic-
role/authority at-
tribute
Appendix References
Acosta, M.; Ajello, A.; Bauer, M. D.; Loria, F.; and Miranda-Agrippino, S. 2025. The Financial Market Effects of FOMC
Communication: Evidence from a New Event-Study Database.Federal Reserve Bank of San Francisco Working Paper Series.
Agrawal, A.; and Lim, Y. 2026. Does General Solicitation Improve Access to Equity Capital for Small Businesses? Evidence
from the JOBS Act.Journal of Financial and Quantitative Analysis, 1–43.
Alam, Z.; Alter, A.; Eiseman, J.; Gelos, R. G.; Kang, H.; Narita, M.; Nier, E.; and Wang, N. 2019. Digging Deeper—Evidence
on the Effects of Macroprudential Policies from a New Database. IMF Working Paper 19/66, International Monetary Fund.
Amiti, M.; Kong, S. H.; and Weinstein, D. 2020. The Effect of the U.S.-China Trade War on U.S. Investment. Working Paper
27114, National Bureau of Economic Research.
Bahaj, S.; and Reis, R. 2022. Central Bank Swap Lines: Evidence on the Effects of the Lender of Last Resort.The Review of
Economic Studies, 89(4): 1654–1693.
Baker, C. F.; Fillmore, C. J.; and Lowe, J. B. 1998. The Berkeley FrameNet Project. In36th Annual Meeting of the Association
for Computational Linguistics and 17th International Conference on Computational Linguistics, Volume 1, 86–90. Montreal,
Quebec, Canada: Association for Computational Linguistics.
Baker,S.R.;Bloom,N.;andDavis,S.J.2016. MeasuringEconomicPolicyUncertainty.TheQuarterlyJournalofEconomics,
131(4): 1593–1636.
Banarescu,L.;Bonial,C.;Cai,S.;Georgescu,M.;Griffitt,K.;Hermjakob,U.;Knight,K.;Koehn,P.;Palmer,M.;andSchneider,
N. 2013. Abstract Meaning Representation for Sembanking. InProceedings of the 7th Linguistic Annotation Workshop and
Interoperability with Discourse, 178–186. Sofia, Bulgaria: Association for Computational Linguistics.
Bao,J.;O’Hara,M.;and(Alex)Zhou,X.2018. TheVolckerRuleandcorporatebondmarketmakingintimesofstress.Journal
of Financial Economics, 130(1): 95–113.
Bass, F. M. 1969. A New Product Growth for Model Consumer Durables.Management Science, 15(5): 215–227.
Battalio, R.; and Schultz, P. 2011. Regulatory Uncertainty and Market Liquidity: The 2008 Short Sale Ban’s Impact on Equity
Option Markets.The Journal of Finance, 66(6): 2013–2053.
Beber, A.; and Pagano, M. 2013. Short-Selling Bans Around the World: Evidence from the 2007–09 Crisis.The Journal of
Finance, 68(1): 343–381.
Bessembinder, H. 2003. Trade Execution Costs and Market Quality after Decimalization.The Journal of Financial and
Quantitative Analysis, 38(4): 747–777.
Board of Governors of the Federal Reserve System. 2025. Policy Tools. Federal Reserve Board. Last updated 2025-12-15;
accessed 2026-07-28.
Boehmer, E.; Jones, C. M.; and Zhang, X. 2013. Shackling Short Sellers: The 2008 Shorting Ban.The Review of Financial
Studies, 26(6): 1363–1400.
Bombardini, M.; Gonzalez-Lira, A.; Li, B.; and Motta, C. 2024. The Increasing Cost of Buying American. Working Paper
32953, National Bureau of Economic Research.
Boyarchenko, N.; Kovner, A.; and Shachar, O. 2022. It’s what you say and what you buy: A holistic evaluation of the corporate
credit facilities.Journal of Financial Economics, 144(3): 695–731.
Byrd, D.; Hybinette, M.; and Balch, T. H. 2019. ABIDES: Towards High-Fidelity Market Simulation for AI Research.
arXiv:1904.12066.
Campbell, S.; Covitz, D.; Nelson, W.; and Pence, K. 2011. Securitization markets and central banking: An evaluation of the
termasset-backedsecuritiesloanfacility.JournalofMonetaryEconomics,58(5):518–531. Carnegie-RochesterConferenceon
public policy: Normalizing Central Bank Practice in Light of the credit Turmoi, 12–13 November 2010.

Chari,A.;DiltsStedman,K.;andLundblad,C.2021. TaperTantrums:QuantitativeEasing,ItsAftermath,andEmergingMarket
Capital Flows.The Review of Financial Studies, 34(3): 1445–1508.
Chen, Z.; Chen, W.; Smiley, C.; Shah, S.; Borova, I.; Langdon, D.; Moussa, R.; Beane, M.; Huang, T.-H.; Routledge, B.; and
Wang, W. Y. 2022. FinQA: A Dataset of Numerical Reasoning over Financial Data. arXiv:2109.00122.
Chetty, R.; and Saez, E. 2005. Dividend Taxes and Corporate Behavior: Evidence from the 2003 Dividend Tax Cut.The
Quarterly Journal of Economics, 120(3): 791–833.
Cieslak, A.; and Vissing-Jorgensen, A. 2020. The Economics of the Fed Put. Working Paper 26894, National Bureau of
Economic Research.
Cipriani, M.; and La Spada, G. 2021. Investors’ appetite for money-like assets: The MMF industry after the 2014 regulatory
reform.Journal of Financial Economics, 140(1): 250–269.
Coffee, J. C. J. 2022. Rolling Back Dodd-Frank: Investors’ and Banks’ Responses to Financial Market Deregulation.
Cuñat, V.; Giné, M.; and Guadalupe, M. 2016. Say Pays! Shareholder Voice and Firm Performance.Review of Finance, 20(5):
1799–1834.
Dambra, M.; Field, L. C.; and Gustafson, M. T. 2015. The JOBS Act and IPO volume: Evidence that disclosure costs affect the
IPO decision.Journal of Financial Economics, 116(1): 121–143.
DeGroot, M. H. 1974. Reaching a Consensus.Journal of the American Statistical Association, 69(345): 118–121.
Egan, M.; Ge, S.; and Tang, J. 2022. Conflicting Interests and the Effect of Fiduciary Duty: Evidence from Variable Annuities.
The Review of Financial Studies, 35(12): 5334–5386.
Eichengreen, B.; and Gupta, P. 2015. Tapering talk: The impact of expectations of reduced Federal Reserve security purchases
on emerging markets.Emerging Markets Review, 25: 1–15.
Erten, B.; Stiglitz, J. E.; and Verhoogen, E. 2026. Employment Impacts of the CHIPS Act. Working Paper 34625, National
Bureau of Economic Research.
Farmer, J.; and Foley, D. 2009. The Economy Needs Agent-Based Modeling.Nature, 460: 685–6.
Fillmore, C. J. 1982. Frame Semantics. In Linguistic Society of Korea, ed.,Linguistics in the Morning Calm, 111–137. Seoul:
Hanshin Publishing Company.
Fritsch, N.; and Siedlarek, J.-P. 2022. How Do Banks Respond to Capital Regulation? — The Impact of the Basel III Reforms
in the United States.SSRN Electronic Journal.
Gao, P.; and Yun, H. 2012. Liquidity Backstop, Corporate Borrowings, and Real Effects.SSRN Electronic Journal.
Gilchrist, S.; Wei, B.; Yue, V. Z.; and Zakrajšek, E. 2024. The Fed takes on corporate credit risk: An analysis of the efficacy of
the SMCCF.Journal of Monetary Economics, 146: 103573.
Greenwood,R.;Laarits,T.;andWurgler,J.2022. StockMarketStimulus. WorkingPaper29827,NationalBureauofEconomic
Research.
Gürkaynak,R.S.;Sack,B.;andSwanson,E.T.2005. DoActionsSpeakLouderThanWords?TheResponseofAssetPricesto
Monetary Policy Actions and Statements.International Journal of Central Banking, 1(1): 55–93.
Holley, R. A.; and Liggett, T. M. 1975. Ergodic Theorems for Weakly Interacting Infinite Systems and the Voter Model.The
Annals of Probability, 3(4): 643–663.
Hood, C. C.; and Margetts, H. Z. 2007.The Tools of Government in the Digital Age. Basingstoke: Palgrave Macmillan. ISBN
978-0-230-00143-5.
Howlett,M.2009.GovernanceModes,PolicyRegimesandOperationalPlans:AMulti-LevelNestedModelofPolicyInstrument
Choice and Policy Design.Policy Sciences, 42(1): 73–89.
Hu, Q.; Moon, G.; and Ng, H. T. 2024. From Moments to Milestones: Incremental Timeline Summarization Leveraging
Large Language Models. In Ku, L.-W.; Martins, A.; and Srikumar, V., eds.,Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), 7232–7246. Bangkok, Thailand: Association for
Computational Linguistics.
Huang, Y.; Hu, N.; Li, K.; Wang, N.; and Lin, Z. 2024. Extracting Financial Events from Raw Texts via Matrix Chunking. In
Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation,
7035–7044. ELRA and ICCL.
Huang,Y.;Lin,C.;Liu,S.;andTang,H.2023. Tradenetworksandfirmvalue:EvidencefromtheU.S.-Chinatradewar.Journal
of International Economics, 145: 103811.
Justiniano, A.; Evans, C. L.; Calomiris, C.; Campbell, J.; Fisher, J. D.; and Woodford, M. 2012. Macroeconomic Effects of
FOMC Forward Guidance.
Kempe, D.; Kleinberg, J.; and Tardos, E. 2003. Maximizing the Spread of Influence through a Social Network. InProceedings
of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 137–146.

Kurov,A.;Olson,E.;andWolfe,M.H.2024. Havethecausaleffectsbetweenequities,oilprices,andmonetarypolicychanged
over time?Journal of Commodity Markets, 36: 100446.
Kwak,H.;andAn,J.2016.TwoTalesoftheWorld:ComparisonofWidelyUsedWorldNewsDatasetsGDELTandEventRegistry.
InProceedings of the Tenth International AAAI Conference on Web and Social Media, 619–622.
Laeven, L.; and Valencia, F. 2018. Systemic Banking Crises Revisited. IMF Working Paper 18/206, International Monetary
Fund.
Langer, L.; Huppmann, D.; and Holz, F. 2016. Lifting the US crude oil export ban: A numerical partial equilibrium analysis.
Energy Policy, 97: 258–266.
Lebaron, B. 2006. Agent-Based Computational Finance.Handbook of Computational Economics, 2: 1187–1233.
Li,X.;Zeng,Y.;Xing,X.;Xu,J.;andXu,X.2025. QuantAgents:TowardsMulti-agentFinancialSystemviaSimulatedTrading.
arXiv:2510.04643.
Liu,P.;Shao,Y.;andYeager,T.J.2009. DidtherepeateddebtceilingcontroversiesembeddefaultriskinUSTreasurysecurities?
Journal of Banking & Finance, 33(8): 1464–1471.
Liu, X.-Y.; Wang, G.; Yang, H.; and Zha, D. 2023. FinGPT: Democratizing Internet-scale Data for Financial Large Language
Models. arXiv:2307.10485.
Liu, X.-Y.; Yang, H.; Gao, J.; and Wang, C. D. 2021. FinRL: deep reinforcement learning framework to automate trading in
quantitative finance. InProceedings of the Second ACM International Conference on AI in Finance, ICAIF’21, 1–9. ACM.
MacKinlay, A. C. 1997. Event Studies in Economics and Finance.Journal of Economic Literature, 35(1): 13–39.
McAndrews,J.;Sarkar,A.;andWang,Z.2015. TheEffectoftheTermAuctionFacilityontheLondonInterbankOfferedRate.
SSRN Electronic Journal.
McDermott, D. M. 2000. The 1998 AI Planning Systems Competition.AI Magazine, 21(2): 35–55.
Mukharlyamov, V.;and Sarin, N. 2025. Priceregulation in two-sided markets:Empirical evidence from debitcards.Journal of
Financial Economics, 172: 104094.
Palmer,M.;Gildea,D.;andKingsbury,P.2005. ThePropositionBank:AnAnnotatedCorpusofSemanticRoles.Computational
Linguistics, 31(1): 71–106.
Park, J. S.; O’Brien, J. C.; Cai, C. J.; Morris, M. R.; Liang, P.; and Bernstein, M. S. 2023. Generative Agents: Interactive
SimulacraofHumanBehavior. InProceedingsofthe36thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology,
1–22. ACM.
Pustejovsky, J.; Castaño, J. M.; Ingria, R.; Saurí, R.; Gaizauskas, R. J.; Setzer, A.; Katz, G.; and Radev, D. R. 2003. TimeML:
Robust Specification of Event and Temporal Expressions in Text. InNew Directions in Question Answering, number SS-03-07
in AAAI Technical Report, 28–34. Menlo Park, California: AAAI Press.
Rao,A.S.;andGeorgeff,M.P.1995. BDIAgents:FromTheorytoPractice. InProceedingsoftheFirstInternationalConference
on Multiagent Systems, 312–319. San Francisco, California: AAAI Press.
Reyes, R.; and Upadhyay, A. ????Tax benefits, Peer Pressure and Corporate Inversions.
Saurí, R.; and Pustejovsky, J. 2009. FactBank 1.0. Linguistic Data Consortium, LDC2009T23.
Schrodt, P. A. 2012.CAMEO: Conflict and Mediation Event Observations—Event and Actor Codebook. Event Data Project,
Department of Political Science, Pennsylvania State University. Version 1.1b3; updated 2012-03-16.
Scott, H. S. 2012. Interconnectedness and Contagion. Technical report, Committee on Capital Markets Regulation.
Searle, J. R. 1976. A Classification of Illocutionary Acts.Language in Society, 5(1): 1–23.
Shao,Y.2020. DoesCrudeOilMarketEfficiencyImproveAftertheLiftoftheU.S.ExportBan?EvidenceFromTime-Varying
Hurst Exponent.Frontiers in Physics, Volume 8 - 2020.
Sharma,S.;Nayak,T.;Bose,A.;Meena,A.K.;Dasgupta,K.;Ganguly,N.;andGoyal,P.2023. FinRED:ADatasetforRelation
Extraction in Financial Domain. arXiv:2306.03736.
Sim, T.; Yang, K.; Xin, S.; and Kawaguchi, K. 2026. Who’s important? – SUnSET: Synergistic Understanding of Stakeholder,
Events and Time for Timeline Generation.
Sun, S.; Qin, M.; Zhang, W.; Xia, H.; Zong, C.; Ying, J.; Xie, Y.; Zhao, L.; Wang, X.; and An, B. 2023. TradeMaster:
A Holistic Quantitative Trading Platform Empowered by Reinforcement Learning. In Oh, A.; Naumann, T.; Globerson, A.;
Saenko, K.; Hardt, M.; and Levine, S., eds.,Advances in Neural Information Processing Systems, volume 36, 59047–59061.
Curran Associates, Inc.
Swanson, E. T.; Wright, J. H.; and Reichlin, L. 2011. Let’s Twist Again: A High-Frequency Event-Study Analysis of Operation
Twist and Its Implications for QE2.
Wagner, A. F.; Zeckhauser, R. J.; and Ziegler, A. 2020. The Tax Cuts and Jobs Act: Which Firms Won? Which Lost?SSRN
Electronic Journal.

Walker,C.;Strassel,S.;Medero,J.;andMaeda,K.2006. ACE2005MultilingualTrainingCorpus. LinguisticDataConsortium,
LDC2006T06.
Wang, X. 2019. DOL Fiduciary Rule and ETF Performance.Journal of Accounting and Finance, 19.
Ward, M. D.; Beger, A.; Cutler, J.; Dickenson, M.; Dorff, C.; and Radford, B. J. 2013. Comparing GDELT and ICEWS Event
Data.
Xiao, Y.; Sun, E.; Luo, D.; and Wang, W. 2024. TradingAgents: Multi-Agents LLM Financial Trading Framework.
arXiv:2412.20138.
Zheng, S.; Cao, W.; Xu, W.; and Bian, J. 2019. Doc2EDAG: An End-to-End Document-level Framework for Chinese Financial
Event Extraction. InProceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Processing, 337–346. Association for Computational Linguistics.
Zhou, X.; Zhu, H.; Mathur, L.; Zhang, R.; Yu, H.; Qi, Z.; Morency, L.-P.; Bisk, Y.; Fried, D.; Neubig, G.; Sap, M.; and Yang,
D. 2023. SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents. arXiv:2310.11667.
Ã‡akÄ±rMelek,N.;andOjeda,E.2017. LiftingtheU.S.CrudeOilExportBan:ProspectsforIncreasingOilMarketEfficiency.
Economic Review, None(Q II): 51–74.
