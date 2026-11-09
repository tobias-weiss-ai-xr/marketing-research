---
title: 'Generative AI and Formal Deductive Planning for Port-City Transformation: A Wild Scenario Methodology
  Applied to Cork 2050'
url: https://doi.org/10.55121/upc.v4i2.101659
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: Urban Planning and Construction
authors:
- Suresh C. Sood
- Hugh Pattinson
source: openalex-oa
pdf_url: https://ojs.bilpub.com/uploads/8/copyediting_typesetting/2026/09/copyediting_typesetting_51042c09af26500a534fe0223c15c0ab.pdf
pages: 16
chars: 62859
fetched_at: '2026-11-08T19:53:45+00:00'
kb_version: 1
---

# Generative AI and Formal Deductive Planning for Port-City Transformation: A Wild Scenario Methodology Applied to Cork 2050

Urban Planning and Construction |Volume04|Issue02|November2026
Urban Planning and Construction
https://ojs.bilpub.com/index.php/upc
ARTICLE
Generative AI and Formal Deductive Planning for Port-City
Transformation: A Wild Scenario Methodology Applied to Cork 2050
Suresh Sood 1*
 , Hugh Pattinson 2
1 Faculty of Engineering and Information Technology, Australian Artificial Intelligence Institute (AAII), University of
Technology Sydney, Ultimo 2007, Australia
2 School of Business, Western Sydney University, Penrith 2751, Australia; h.pattinson@westernsydney.edu.au
ABSTRACT
Portcitiesfaceplanninghorizonsthatconventionalframeworks,anchoredinpresentconditionsandinsufficiently
imaginative, are ill-equipped to navigate. This paper develops and demonstrates the artificial intelligence (AI)-driven
wildscenarioplanningwithformaldeductiveimplementation(AWSPFD)framework,integratinggenerativeAIscenario
generationwithHornclause-basedformalplanningtobridgevisionaryurbanfuturesandimplementablestrategicplans.
DrawingonScenarioPlanningforMarketingAction(SPMA),service-dominant(S-D)logic,andaGedankenthought-
experimentmethodology,weapplyChatGPT-4otogeneratewildscenariosforCorkCityandPortfor2050,formalisea
compositescenariothroughHornclauses,andoperationalizeviaaPythonDataloginferenceengine. Themethodology
yieldsacompositescenario—‘Cork2050: NexusofInnovationandSustainability’—positioningCorkasaglobalBrainport,
integrating renewable energy,AI-driven logistics, spaceport capability, and knowledge-economy institutions. Formal
planningdemonstratesfiveofsevenscenariogoalsarelogicallyachievablegivencurrentCorkassets,andidentifiesprecise
enablingconditionsfortheremainingtwo. AWSPFDisamongthefirstapplicationsofHornclause-basedformalplanning
toAI-generatedurbanfutures,offeringportauthorities,urbanplanners,andpolicymakersageneralisabletoolfortranslating
visionaryscenariosintoactionableimplementationpathways(Inthispaper,“logicallyachievable”denotesthattheHorn
clausedependencychainissatisfiableunderthedefinedknowledgebase—notthatpractical,political,orfinancialfeasibility
*CORRESPONDINGAUTHOR:
SureshSood,FacultyofEngineeringandInformationTechnology,AustralianArtificialIntelligenceInstitute(AAII),UniversityofTechnology
Sydney,Ultimo2007,Australia;Email: suresh.sood@uts.edu.au
ARTICLEINFO
Received: 10June2026|Revised: 13August2026|Accepted: 20August2026|PublishedOnline: 27August2026
DOI:https://doi.org/10.55121/upc.v4i2.101659
CITATION
Sood,S.,Pattinson,H.,2026. GenerativeAIandFormalDeductivePlanningforPort-CityTransformation: AWildScenarioMethodologyApplied
toCork2050. UrbanPlanningandConstruction. 4(2): 1–16. DOI:https://doi.org/10.55121/upc.v4i2.101659
COPYRIGHT
Copyright © 2026 by the author(s). Published by Japan Bilingual Publishing Co. This is an open access article under the Creative Commons
Attribution4.0International(CCBY4.0)License(https://creativecommons.org/licenses/by/4.0).
1

Urban Planning and Construction |Volume04|Issue02|November2026
isguaranteed). Thisstudypresentsamethodologicalproof-of-concept;empiricalvalidationthroughprimarydatacollection
andstakeholderengagementisidentifiedasanecessaryandplannedsubsequentphase.
Keywords: Urban Planning; GenerativeAI; Scenario Planning; Brainport; Port-City Transformation; Horn Clauses;
Service-DominantLogic;Cork2050
1. Introduction
Portcitiesoccupyauniquelycontestedpositioninthe
globaleconomy. Asgatewaysfortrade,migration,andcul-
ture,theysimultaneouslyanchorindustriallegacyandfron-
tiersofurbanreinvention. Yettheplanningframeworksavail-
able to port authorities and city governments, comprising
masterplans,transportimpactassessments,SWOT(strength,
weakness,opportunity,threat)analyses,andmore,aretypi-
callyill-equippedforthecomplexityoftransformationde-
mandedbya2050horizon. Theplansandframeworkstend
to be incremental, constrained by present conditions, and
insufficientlyimaginativeaboutfuturesworthyofpursuit.
This paper proposes and demonstrates a methodol-
ogy that addresses this gap. We combine two capabilities
rarely brought together in the planning literature: genera-
tiveartificialintelligence(AI)’scapacitytoproducecreative,
boundary-pushingscenarios,andformallogic’scapacityto
subject scenarios to rigorous, dependency-aware analysis.
TheresultisaframeworkwetermAI-drivenwildscenario
planningwithformaldeductiveimplementation(AWSPFD),
enablingplannerstoenvisionambitiousfuturesandsystem-
atically work backwards from the futures to identify the
conditions,investments,andsequencingrequiredtomake
themareality. Thepaperpresentsaconceptualdemonstra-
tionofthiscombinationusingCorkasanillustrativecase;
it does not claim to provide an empirically validated plan-
ningoutcome,butratherageneralisablemethodologywhose
validationistheworkofasubsequentresearchphase.
WeapplythisframeworktoCorkCityandPortinIre-
land,usingtheCork2050plan [1],thePortofCorkMaster-
plan 2050[2], and the Ringaskiddy Port Redevelopment[3]
as source documents. Cork is a compelling case: one of
Europe’slargestnaturalharbours,ananchortechnologypres-
ence in the Apple European headquarters, strong higher-
educationinstitutions,andaportauthoritywithacommit-
menttodecarbonizationyetofficialplanningdocumentsstop
well short of the transformative ambition these city assets
couldsupport.
The paper makes three contributions. First, we ex-
tendtheSPMA(ScenarioPlanningforMarketingAction) [4]
frameworkwithaGedankenvariantenablingexpert-ledwild
scenariogenerationwithoutrequiringlivestakeholderwork-
shops. Second, we demonstrate ChatGPT-4o as a tool for
generatingwildscenariosexceedingconventionalplanning
imagination. Third, we introduce Horn clause backward
chainingasamechanismfortranslatingthescenariosinto
formal,verifiableimplementationplans,atechniquefrom
logic programming applied here to strategic planning not
previouslydocumented,totheauthors’knowledge,incom-
binationwithAI-generatedurbanscenarios.
Section 2 reviews the theoretical background. Sec-
tion 3 presents the Cork context. Section 4 describes the
methodology. Section5presentsresults. Section6discusses
contributions and implications. Sections 7 and 8 address
limitationsandconclusions.
2. Theoretical Background
2.1. The Brainport Concept
A Brainport[5,6] is an innovation region with
knowledge-intensive industries, research institutions, and
government agencies collaborating to generate economic
growth and societal progress. The defining characteristic
is triple-helix governance sustaining collaboration among
business,academia,andgovernmentratherthansimpleco-
location[7]. BrainportEindhoven,hometoPhilips,ASML,
andover5,000technologycompanies,istheparadigmatic
case: a region transformed from single-company depen-
dence to diversified innovation leadership over roughly
two decades through deliberate institutional design (see
Appendix A,T able A1foracomparativeoverviewofglobal
Brainportmodels).
Appliedtoportcities,theBrainportconceptrequires
layeringknowledgeanddigitalinfrastructureontoexisting
maritime and logistics operations. The article posted by
IDB[8] frames this as the transition “from ports to innova-
2

Urban Planning and Construction |Volume04|Issue02|November2026
tionecosystems”alreadywellunderwayinRotterdamand
Singapore,withportauthoritiesinvestingininnovationlabs,
sustainability research, and start-up incubation alongside
conventionalcargooperations.
2.2. Scenario Planning for Marketing Action
ScenarioPlanningforMarketingAction(SPMA)isa
structuredframeworkforenvisioningandplanningacross
multiple futures[4]. Developed and refined through appli-
cationinexecutiveeducationcontextsandurbanplanning,
eight principles (SP01–SP08) guide practitioners from en-
vironmentalscanningthroughstrategiccommitment,with
particularemphasisongeneratingdivergentfuturesrather
thanextrapolatingfrompresenttrends. Wildscenariosinter-
nallyconsistent,logicallypossible,butsubstantiallybeyond
conventionalplanningassumptionsareadistinctivesigna-
tureandSPMAoutput. Thescenariossurfaceunexamined
assumptions,expandtheoptionspace,andtestorganisational
flexibility.
2.3. Service-Dominant Logic and Storytelling
Service-dominant (S-D) logic reconceptualizes eco-
nomicexchangeasfundamentallyaserviceprocesswherein
actorsco-createvaluethroughtheapplicationofknowledge
andskills [9]. Inplanning,S-Dlogicreframesinfrastructure
developmentasanongoingvalue-creatingrelationshipbe-
tweenports,cities,businesses,andcommunitiesratherthan
asdiscretecapitalprojects. IntegratingstorytellingwithS-D
logicproducesscenarionarrativesthatcapturenotjustwhat
afuturecitymightlooklike,buthowitwouldfunctionasa
value-creatingsystem.
2.4. Gedanken Scenario Planning
AGedankenexperimentisathoughtexperiment,amen-
talsimulationofhypotheticalconditionsconductedwithout
physicalexecution [10]. Inscenarioplanning,theGedanken
approachenablesexpertresearcherstogenerateandevaluate
scenariosusingexistingknowledgeanddocumentation,with-
outrequiringlivestakeholderengagement. Thisismethod-
ologicallysignificantbecauseitallowsscenarioplanningto
proceedefficientlyanditeratively,withresearchersserving
asbothmoderatorsandparticipants. Thisexperimentation
doesnotreplacestakeholderengagement;itprovidesarigor-
ousprecursorandresultsthatcanbeachievedinafraction
ofthetimeofaconventionalworkshop.
2.5. Horn Clauses and Formal Planning
Hornclausesarearestrictedformoflogicalexpression
usedinlogicprogrammingandautomatedreasoning [11]. A
HornclausetakestheformA←B 1 ∧B2 ∧... ∧Bn,where
AisaconclusionorgoalandB 1 throughB n areconditions.
Thepoweroftheselogicalexpressionsforplanningliesin
supportofbackwardchaining. Givenadesiredgoal,aninfer-
enceenginesystematicallyidentifiestheconditionsrequired
for achievability, then the conditions for those conditions,
untilreachingknownfactsoridentifyinggapsthatrepresent
planningrequirements.
Python Datalog (pyDatalog)[12] provides a practical
implementationenvironmentforHornclauses,enablingre-
searchers to define facts, rules, and goals in Python and
query the resulting knowledge base. This makes the logic
of a strategic plan explicit, auditable, and communicable.
Suchpropertiesareparticularlyvaluableinmulti-stakeholder
contexts. TheapplicationofthisapparatustoAI-generated
urbanscenariosis,toourknowledge,amongthefirstinex-
tending prior knowledge. Formal methods and constraint
programminghavebeenappliedincomputationalurbanplan-
ningcontexts [12,13],includinganswersetprogrammingfor
theconstraint-basedplanningproblems [14] butthespecific
combinationoflargelanguagemodels(LLM)-generatedsce-
narioswithHornclausebackwardchainingrepresentsadis-
tinctmethodologicalcontributionnotpreviouslydocumented
intheurbanplanningliterature.
3. Cork City and Port: Context and
Strategic Position
3.1. The Port of Cork Today
ThePortofCorkisIreland’ssecond-largestportbyton-
nageandtheprimarydeep-waterfacilityontheisland’ssouth
coast. The natural harbor, among the largestin Europe by
waterarea,comparabletoSydneyandHalifax [15],provides
asignificantgeographicalendowment. Operationsspandry
andliquidbulk,containers,roll-on/roll-off,andpassenger
servicesacrossCityQuays,Tivoli,Ringaskiddy,andCobh
3

Urban Planning and Construction |Volume04|Issue02|November2026
terminals. Theportalsohandlescruisetrafficbasedonthe
2024cruiseschedule [16],May–Octoberpassengervolumes
totalapproximately195,648,implyinganestimatedannual
figure of around 391,000. The Cobh dedicated quayside
berth,adjacenttotheCobhHeritageCentre,providesadis-
tinctivearrivalexperienceconventionalportcomparisonsdo
notcapture. High-valuetouristassetsofBlarneyCastle,the
EnglishMarket,andtheLeeValleyremainanunderexploited
competitiveadvantage. (Estimationnote: monthlypassenger
countswereaggregatedfromthe2024cruiseschedule [16]us-
ingaMay–Octoberoperationalwindow;thisconstitutesthe
onlyquantitativefigurederivedbytheauthorsfromdirect
sourcetabulationratherthandocumentcitation).
3.2. Planning Frameworks and Gaps
Two strategic documents frame Cork’s development
trajectory: Cork 2050[1] and the Port of Cork Masterplan
2050[2],supplementedbytheRingaskiddyRedevelopment
project[3]. Cork 2050 addresses holistic city and regional
development—housing,transport,culture,economicdiversi-
fication,andenvironmentalresilience—withexplicitatten-
tiontocommunitywell-being. ThePortMasterplanfocuses
onoperationalandcapacityimprovements: relocatingactiv-
itiesfromCityQuaysandTivolitoRingaskiddy,upgrading
forlargervessels,achievingnet-zeroby2050,andreleasing
centralwaterfrontlandformixed-useredevelopment.
Bothdocumentsarecredibleandwell-evidenced. Yet
bothshareacharacteristiclimitation: theyareanchoredin
current conditions and project relatively modest improve-
mentsfromthem,ratherthanaskingwhatanentirelydifferent
modeofoperatingmightmakepossible. T able 1summarizes
thekeydimensionsofeachplanandidentifiestheBrainport
conceptasapotentialbridge.
3.3. Cork as an Emerging Brainport
SeveralexistingassetspositionCorkcredibly. Apple’s
EuropeanHeadquartersemploysover6,000peopleon100%
renewableenergy [17],anchoringabroadertechnologyclus-
ter. University College Cork (UCC) and MunsterTechno-
logical University provide research capacity and graduate
talent. The Ringaskiddy transition will release substantial
centralwaterfrontlandformixed-useregeneration,mirror-
ingthetrajectoriesofRotterdam,Seattle,andLosAngeles.
TheAtlanticSmartPortsBlueAccelerationNetwork [18]con-
nects Cork with European peers in port digitalization and
decarbonization. Cork’spositionasanodeontheAtlantic
maritimecorridorofferspotentialasagatewayfortechand
tradebetweenEuropeandNorthAmerica.
Whatismissingisasufficientlyambitiousvisionfor
whattheseassets, combinedandextended, mightproduce
by2050. Thefollowingsectionsdevelopanddemonstrate
suchavision.
Table 1. CorkCity2050andPortMasterplan2050: KeyDimensionsandtheBrainportBridgeSynthesis.
Dimension Cork 2050 Port Masterplan 2050 Brainport Synthesis
Primaryfocus City-wide&regionaldevelopment Portoperations&capacity Knowledge-intensiveecosystem
Sustainability Low-carboncity;greeninfrastructure Net-zero2050;greenenergy Blueeconomyleadership;circularport
Economicmodel Diversifiedsectors;FDI Maritimetrade;logistics High-valueservices;innovation
Communityengagement Central;participatory Limited;operationalfocus Co-created;culturallyembedded
Technology Smartcity;digitalinfrastructure IoT,automation,blockchain Quantum,AI,digitaltwins,biotech
Keyassets AppleHQ;UniversityCollegeCork; culturalheritage Deepharbour;Ringaskiddysite Atlanticgateway+knowledgebase
Note: FDI:Foreigndirectinvestment;IoT:InternetofThings;HQ:Headquarters.
4. Methodology
4.1. The A WSPFD Framework
TheAI-drivenwildscenarioplanningwithformalde-
ductive implementation (AWSPFD) framework integrates
fivecomponents: (1)expertknowledgepreparation,(2)AI-
drivenscenariogenerationusingChatGPT-4o,(3)composite
wildscenariodevelopmentguidedbySPMAandS-Dlogic,
(4)formalimplementationplanningusingHornclausesand
PythonDatalog,and(5)expertsynthesisandvalidationof
AIoutputsagainstresearcherdomainknowledge. Figure 1
illustratestheoverallworkflow.
4.2. Expert Knowledge Preparation
Prior toAI engagement, the researchers review the
threecoreplanningdocumentstodevelopdomainknowl-
4

Urban Planning and Construction |Volume04|Issue02|November2026
edgesufficienttoevaluateandconstrainAIoutputs. This
stepismethodologicallycriticalaslargelanguagemodels
are known to hallucinate, generating confident but factu-
ally incorrect outputs[19]. Without prior domain knowl-
edge,researcherscannotdistinguishgroundedfromspec-
ulative content. The workflow employs three learning
modes: zero-shot(noexamples;testingmodelpriors),few-
shot (two to five examples to calibrate format and style),
and many-shot (full document upload to maximise con-
textualgrounding). Table 2summarizestheinputs,learn-
ing modes, and validation approaches for each prompt
stage.
Figure 1. AWSPFDWorkflow: FromPlanningDocumentstoFormalImplementationPlan.
Note: SPMAframework[4];service-dominantlogic [9];brainportconcept [5–7].
Table 2. AWSPFDWorkflow: Inputs,AILearningModes,andValidationApproaches.
Stage/Prompt # Prompt Objective Learning Mode Prompt Length (Chars/Words) Session Date/Model Version Validation Approach
1 SWOTanalysisforCorkCity andPortasof2024 Many-shot(Cork2050 [1], PortMasterplan [2] EIB[3]
uploadedinfull)
301chars
52words
June2024
ChatGPT-4o
(OpenAI,June2024release) [20]
Expertcross-checkagainstallthree
sourcedocuments;allSWOTelements
verifiedtosourcepage;hallucinated
statisticsremovedbeforeinclusion
2
Fivetosevenoverarching
strategicthemesacross
documents
Many-shot
(samethreedocumentsin
context)
264chars
41words
June2024
ChatGPT-4o
(OpenAI,June2024release) [20]
Cross-documenttriangulation;researchers
independentlyidentifiedthemes,then
reconciledthem;onlythemessupported
by≥2documentswereretained
3
Cohesivestrategicoverview
ofCork’sdevelopment
trajectoryto2050
Many-shot
(Stages1–2outputsretained
incontextwindow)
271chars
41words
June2024
ChatGPT-4o
(OpenAI,June2024release) [20]
Expertsynthesischeck;validatedagainst
researchers’priorBrainport
knowledge[5];unsupported
generalisationsremoved
4 FiveSPMA/S-Dlogic scenariosforCork2050 Few-shot (2workedSPMAscenario examplesprovided) 336chars 49words June2024 ChatGPT-4o (OpenAI,June2024release) [20] SPMAprinciplesSP01–SP08compliance check;eachscenarioevaluatedfor internalconsistencyandplausibilityby bothresearchersindependently
5 FivewildscenariosforCork 2050 Zero-shot (boundary-pushinginstruction only;noexamples) 375chars 56words June2024 ChatGPT-4o (OpenAI,June2024release) [20] Internalconsistencyreview;eachscenario anchoredto≥1demonstrableCorkasset; implausibleorungroundedelements removed
6
Compositewildscenariowith
Brainportframing(seven
pillars)
Few-shot
(Stage5outputsasinput
examples)
422chars
61words
June2024
ChatGPT-4o
(OpenAI,June2024release) [20]
Brainportalignmentverifiedagainst
Eindhovenmodel [5–7];composite
sign-offrequiredfrombothresearchers
beforeformalisation
Note: AllsixpromptsweresubmittedinasinglecontinuousChatGPT-4osessiontomaintaincontextwindowcontinuity;eachpromptbuiltonprioroutputs. Prompttextsare
reproducedverbatimin Appendix B.Charactercountsexcludeem-dash(—)renderingvariants. ChatGPT-4odoesnotexposeasessiontimestamp;“June2024”reflectsthe
citedmodelversion [20]. Replicationshouldspecifymodel: gpt-4o,temperature: 1.0(default).
5

Urban Planning and Construction |Volume04|Issue02|November2026
The researchers collectively bring over four decades
of combined experience in scenario planning, marketing
strategy,andport-citydevelopmentresearch. SoodandPat-
tinsondevelopedtheSPMAframeworkthroughsustained
engagement with executive education and urban planning
contexts[4];PattinsonandSoodappliedBrainportanalysis
specificallytoSydneyandKualaLumpur [5]. Thispriorex-
pertiseconstitutestheprimaryknowledgebaseagainstwhich
allAI outputs were evaluated and represents the principal
expertknowledgeresourceinthisGedankenapproach [10].
Thevalidationprotocolrequiredunanimousresearcher
consensusbeforeanyAIoutputwasacceptedforinclusion.
WhereAIoutputscontainedfactualclaimsnottraceableto
thethreesourceplanningdocuments—theCork2050plan [1],
PortofCorkMasterplan2050 [2],andRingaskiddyproject
documentation[3] claimswereremovedorexplicitlyflagged
asspeculative. EachAIresponsewascross-checkedagainst
thesourcedocumentsparagraphbyparagraph;hallucinated
statistics,misattributedfacts,orunsupportedcausalclaims
were excised before incorporation. This expert-mediated
filterrepresentstheprimaryqualitygateofthemethodology
andisdocumentedstagebystagein Table 2.
4.3. Gedanken Scenario Planning
Our SPMA application takes the Gedanken form
whereintheresearchersplaybothmoderatorandparticipant,
using existing planning documentation as the knowledge
proxyratherthanconveningstakeholderworkshops. Thisis
justifiedasamethodologicalproofofconcept;theplanning
documents represent the outputs of extensive community
andexpertconsultation. Gedankenscenarioplanningisnota
replacementforparticipatoryengagementbutacomplement.
Itisatoolforexploringthefullpossibilityspacebeforenar-
rowing it through stakeholder deliberation. The approach
isfurtherstrengthenedbythepre-mortemtechnique [21] by
imaginingafuturestateindetailandreasoningbackwards
exposestheassumptionsanddependenciesthatmusthold
forthatfuturetoberealisedorfail,whichispreciselywhat
Hornclausebackwardchainingformalises.
Scenariofilteringfollowedatwo-stageprocessapplied
aftereachAIpromptoutput. InStage1,eachAI-generated
scenariowasassessedagainstfourcriteria: (i)internalcon-
sistency,thescenariofollowslogicallyfromitsownpremises
withoutcontradiction;(ii)Corkassetgrounding,thescenario
isanchoredinatleastonedemonstrableexistingCorkassetor
geographicalendowmentdocumentedinthethreesourcedoc-
uments;(iii)temporalplausibility,thestateddevelopments
areconceivablewithina25-yearhorizongiventechnologi-
caltrajectoriesvisiblein2024;and(iv)non-redundancy,the
scenariooccupiesadistinctpositioninthepossibilityspace
andisnotsubstantivelyduplicativeofanotherretainedsce-
nario. Scenariosfailinganycriterionwerediscardedintheir
entirety. InStage2,elementssurvivingfromalltenprompt
outputs (five SPMAand five wild scenarios) were synthe-
sisedintothecompositescenario;onlyelementsmeetingthe
grounding criterion were carried forward. Researcher dis-
agreementsatbothstageswereresolvedthroughstructured
discussiontoconsensusbeforeanyelementwasincorporated.
Thistwo-stagefilteristheprimarymechanismtranslating
rawAIoutputintothevalidatedcompositescenariousedfor
formalplanning.
4.4. Formal Planning with Horn Clauses
Once a composite wild scenario is validated, transla-
tionintogoals,facts,andrulesisexpressedasHornclauses.
Goals correspond to high-level scenario outcomes. Facts
representknownpresent-dayCorkconditions. Rulesdefine
dependenciesbetweengoalsandenablingconditions. The
pyDatalog[12] libraryexecutestheseclausesinPython,per-
formingbackwardchainingtodeterminewhethereachgoal
isachievablegivendefinedfactsandrules. Whengoalsare
notachievablewithcurrentfacts,thesystemidentifiesmiss-
ingconditionsdirectlyinformingtheinvestmentandpolicy
prioritiesthatplannersshouldaddress. Thistransformsthe
scenariofromanarrativeaspirationintoastructuredimple-
mentationroadmapwithexplicitdependencies.
Animportantboundaryconditiongovernstheformal
planning exercise: the pyDatalog inference engine evalu-
ates logical consistency and internal coherence under the
statedassumptionsnotempiricalorpracticalfeasibility. A
planning goal deemed “achievable” by the system means
Horn clause dependency chain is satisfiable given the de-
finedfacts;itisnotaguaranteeofreal-worldimplementation
ability. Politicalfeasibility,financialviability,institutional
capacity, regulatory environments, and temporal sequenc-
ing constraints lie entirely outside the scope of the formal
model. Thesystemidentifieslogicallycoherentimplemen-
tationpathwaysconditionalonspecifiedpremises; itdoes
6

Urban Planning and Construction |Volume04|Issue02|November2026
notpredict,confirm,orendorseanyspecificoutcomeinthe
actualplanningenvironment.
5. Results
5.1. AI-Generated Scenario Analysis
Attributionnote: AllscenariotextinSections5.1and
5.2wasgeneratedbyChatGPT-4oinresponsetothestruc-
tured prompt sequence documented inTable 2 and repro-
ducedverbatimin Appendix B.Thecompositescenarioin
Section5.2.3isaresearchersynthesisintegratingelements
acrossAI-generatedoutputs;itisnotaverbatimAIoutput.
The Horn clause rulesets in Section 5.3 were authored en-
tirely by the researchers based on the composite scenario;
theywerenotAI-generated. AllAIoutputsweresubjectto
theexpertvalidationprotocoldescribedinSection4.2before
inclusion.
SWOT Analysis and Strategic Themes
TheAI-generatedSWOTanalysis,validatedbyexpert
review, identified Cork’s key strengths as its deep-water
harbour, theApple HQ presence, strong higher-education
institutions,andtheRingaskiddyinfrastructureinvestment
programmebytheEuropeanUnion(EU).Coreweaknesses
include scale limitations relative to major European ports,
skills gaps in emerging maritime technologies, and transi-
tionmanagementcomplexity. Opportunitiescentreonthe
IrishAtlanticpositioning,EUdecarbonisationfunding,and
growingtech-sectorinterestinsustainablelogisticsinfras-
tructure. KeythreatsincludecompetitionfromRotterdam
andAntwerpforgreenenergyhubstatusandpoliticalrisk
acrossa25-yearplanninghorizon.
Acrossthethreesourcedocuments,fiveoverarching
strategicthemesemerged: physicaltransition(relocatingop-
erationstoenableurbanrenewal);decarbonisation(net-zero
throughrenewableintegration);digitaltransformation(IoT,
big data, automation); community integration (mixed-use
waterfrontregeneration);andinstitutionalcollaboration(port
authority,citygovernment,universities,industry).
5.2. Wild Scenario Generation
5.2.1. Five SPMA Scenarios
The five SPMA-structured scenarios ranged from a
conservative “Green Maritime Hub”, a credible extension
oftheMasterplan2050trajectorythroughtoanambitious
“AtlanticKnowledgeGateway”centredonCorkbecominga
Europeanheadquarterscityforemergingtechnologycompa-
nies. Eachscenariowasvalidatedforinternalconsistency
andSPMAframeworkalignment.
5.2.2. Five Wild Scenarios
The five wild scenarios substantially exceeded con-
ventionalplanningimagination,envisagingCorkas: (1)a
commercialspaceportandaerospaceinnovationhub;(2)a
floating-city laboratory for climate adaptation, deploying
modularmarinehabitatsintheharbour;(3)aglobalbiotech
capitalusingCork’smarinebiodiversityasapharmaceutical
researchresource;(4)aquantumcomputingcentreanddigi-
taltwincity;and(5)aglobalcultural-innovationdestination
blendingIrishheritagewithimmersivetechnologyexperi-
ences. Eachscenarioisinternallycoherentandanchorsinat
leastonedemonstrableCorkasset.
5.2.3. Composite Wild Scenario
Thecompositewildscenario,“Cork2050: Nexusof
InnovationandSustainability”(tagline: “PioneeringTomor-
row: WhereTechnologyMeets Sustainability”) integrates
elementsfromallfivewildscenarioswiththeBrainportcon-
ceptasanorganisingframework. Sevenpillarscharacterise
thecompositevision( Table 3).
Table 3. CompositeWildScenario: Cork2050Brainport—SevenStrategicPillars.
Pillar Description
QuantumComputingCapital Europe’sleadingquantumcomputingcluster,supportedbygovernmentinvestment,globaltech partnerships,andUniversityCollegeCork(UCC)researchinstitutes.
SustainableUrbanLiving Integratedrenewableenergy(wind,solar,tidal)powersasmartcitygrid;zero-emissionpublic transportsetsnewEuropeanbenchmarks.
FloatingCityResilience Modularharbourhabitatsprovideclimate-adaptivelivingandworkingenvironments,incorporating verticalfarmingandAI-managedsystems.
CulturalHeritageDestination BlarneyCastle,theEnglishMarket,andCobhmaritimehistorywovenintoimmersivetechnology experiencesforglobalculturaltourism.
ConnectedCity Autonomousvehiclenetworksanddigitaltwinmanagementdeliverseamlessconnectivity; ultra-fastinfrastructuresupportsglobaloperations.
7

Urban Planning and Construction |Volume04|Issue02|November2026
Table 3. Cont.
Pillar Description
CommercialSpaceport AmongthefirstEuropeancommercialspaceports,exploitingtheharbour’sspatialfootprintand establishedaerospacesupplychains.
BrainportEcosystem Atriple-helixinnovationecosystem—UCC/MunsterTechnologicalUniversity(MTU),globaltech companies,andgovernment—drivescontinuousknowledgecreationandeconomicrenewal.
5.3. Formal Planning with Horn Clauses
5.3.1. Goals, Facts, and Representative Rules
Table 4 belowitemisesthefivebasefactsrepresent-
ingCork’scurrentdocumentedassetbasethatgroundthe
formal planning knowledge base. For each fact,Table 4
specifies the corresponding Cork asset, its source docu-
mentation, the evidence status (Documented = explicitly
stated in source material; Extrapolated = inferred from
plansorstatedpolicydirections),andtheHornclausepred-
icates that the fact enables. This mapping allows read-
ers to critically assess whether the asset assumptions un-
derlying the logical deduction are reasonable and trace-
able.
Table 4. CorkCurrentAssetBase: PredicateGroundingforHornClauseFormalisation.
Predicate Cork Asset Source Documentation Evidence Status Horn Clause Predicates Enabled
Cork_Has_Univer-
sity_Cluster UCC+MTU
Cork2050 [1] §3.2;
UCC/MTUinstitutional
records
Documented
Educational_Excellence,
Research_Institutions,
Community_Involvement,Startups
Cork_Has_Tech_An-
chor
AppleEuropean
Headquarters: >6,000
employees,100%renewable
energy[17]
AppleNewsroom [17];
Cork2050 [1] Documented
Partnership_with_Tech_Companies,
Autonomous_Vehicles,
Tech_Companies,AI_Management
Cork_Has_Deep_Har-
bour
CorkHarbour—among
Europe’slargestnatural
harboursbywaterarea,
comparabletoSydneyand
Halifax[15]
PortMasterplan2050 [2];
CorkHarbour
Wikipedia[15]
Documented Floating_City_Resilience(harbour engineeringbase)
Cork_Has_Renew-
able_Base
Existingwind,solar,andtidal
resourcebase;portnet-zero
2050commitment
PortMasterplan2050 [2]
§2;Cork2050 [1] §4
Documented
(resourcebase);
Extrapolated(full
deploymentby
2050)
Sustainable_Urban_Living
Floating_City_Resilience
Cork_Has_EU_Fund-
ing
ASPBANmembership [7];
EIBRingaskiddyinvestment
€54.7M [6];EU
decarbonisationfund
eligibility
EIB[3];ASPBAN [18];Port
Masterplan[2]
Documented
(existing);
Extrapolated
(continuation)
Government_Support,
Engineering_Partnerships,
Ultra_Fast_Broadband,
Offer_Incentives
Note: EvidenceStatus: Documented=explicitlystatedincitedsourcematerial;Extrapolated=inferredfromstatedplansorpolicydirectionsinsourcedocuments. ASPBAN:
AtlanticSmartPortsBlueAccelerationNetwork.
The composite scenario yields seven planning goals,
fivebasefactsrepresentingcurrentCorkconditions,anda
systemofHornclauserulesspecifyinggoaldependencies.
Threerepresentativerulesetsillustratetheapproach:
Quantum Computing Capital:
Quantum_Advancement ← Investment_in_Quan-
tum_Research∧ Attract_Global_Talent.
Investment_in_Quantum_Research ← Govern-
ment_Support∧ Partnership_with_Tech_Companies.
Attract_Global_Talent←Establish_Research_Facili-
ties∧ Offer_Incentives.
Commercial Spaceport:
Spaceport ← Launch_Space_Initiative ∧ De-
velop_Spaceport_Infrastructure∧ Space_Traffic_Manage-
ment.
Launch_Space_Initiative ← Government_Support
∧ Partnership_with_Space_Agencies.
Space_Traffic_Management ← AI_Management
∧ Safety_Protocols.
Brainport Ecosystem:
Brainport ← Knowledge_Economy ∧ Innova-
tion_Ecosystem∧ Educational_Excellence.
8

Urban Planning and Construction |Volume04|Issue02|November2026
Knowledge_Economy ← Research_Institutions
∧ Global_Talent_Attraction.
Innovation_Ecosystem←Startups ∧ Tech_Companies
∧ Government_Support.
Reproducibilitynote: Theformalplanningmodelwas
implemented in Python 3.10 using pyDatalog v0.17.4[12].
Goals were queried via pyDatalog’s backward-chaining
inference engine using the syntax pyDatalog.ask(‘Goal-
Name()’)—for example, pyDatalog.ask(‘Quantum_Ad-
vancement()’) returns a non-null result set when all Horn
clausepreconditionsaresatisfiablegiventheassertedfacts,
and None when one or more preconditions cannot be de-
rived. Sensitivityscenarioswereimplementedbyselectively
assertingorretractingenabling-conditionfacts(e.g.,+Gov-
ernment_Support() for High Commitment; omitting it for
LowCommitment)andre-runningthefullquerysetagainst
thesamerulebase. Thecompleteknowledgebase—allfact
assertions,ruledefinitions,andquerycalls—isreproduced
verbatimin Appendix C,enablingdirectreplication.
5.3.2. Query Results and Planning Implications
Acriticalinterpretiveboundaryappliestothequeryre-
sultsthatfollow. Theterms“Achievable”and“Conditional”
inTable 5 referexclusivelytologicalachievabilitywithin
thepyDatalogknowledgebase—thatis,whethertheHorn
clausedependencychainforeachgoalissatisfiablegiven
thefivebasefactsin Table 4. Thisisameasureoflogical
coherenceunderspecifiedpremises,notapredictionofprac-
tical,political,orfinancialfeasibility. Politicalconstraints,
fundingrequirements,institutionalcapacity,regulatoryap-
provalpathways,andtemporalsequencingallfalloutsidethe
scopeoftheformalmodel. Therefore,“achievable”should
be read throughout as “logically coherent given the stated
assetpremise”—notas“guaranteedtobeimplemented.”The
formal model’s contribution is to make dependency struc-
turesexplicitandtestable;whetherthosedependenciescan
be satisfied in practice is a question for subsequent stake-
holderengagementandfeasibilityanalysis.
Table 5. FormalPlanningQueryResults: FeasibilityandCriticalDependencies.
Planning Goal Feasibility Critical Conditions/Investment Priorities
QuantumAdvancement Conditional Governmentcommitment;techcompanypartnerships;researchfacilityestablishment
SustainableUrbanLiving Achievable Baseconditions(wind,solar,tidal,transport)availablewithexistingCorkassets
FloatingCityResilience Achievable Engineeringpartnershipsandgovernmentco-investmentrequired;renewablebaseexists
CulturalHeritageDestination Achievable Governmentculturalfundingandactivecommunityinvolvementarekeylevers
ConnectedCity Achievable Autonomousvehicledeployment;smartcitytechnologyintegration;ultra-fastbroadband
CommercialSpaceport Conditional Governmentpolicymandate;spaceagencypartnerships;AImanagementinfrastructure
BrainportEcosystem Achievable Researchinstitutionspresent;talentattractionprogrammesandsustainedgovernmentsupport arekey
Executing the pyDatalog knowledge base against
Cork’scurrentassetbaseyieldsstructuredfeasibilityassess-
mentsforallsevenplanninggoals( Table 5). Fivegoalsare
achievablewithexistingconditions;twoareconditionalon
specificpolicyandpartnershipdevelopments.
Thequeryresultsdemonstratethatfiveofsevenplan-
ning goals are achievable given current Cork conditions.
Quantumadvancementandthecommercialspaceportare
conditional on explicit government policy commitments
and international partnership development, the two most
demandingitemsonthestrategicagenda. Notably,govern-
ment support appears as a critical enabling condition for
threeseparategoalsofquantumadvancement, spaceport,
and brainport ecosystem, providing a concentrated argu-
mentforpolicystabilityandlong-terminstitutionalcommit-
ment.
Whenthemodelisqueriedwithgradedconditionsdis-
tinguishing, for instance, ‘high’from ‘medium’levels of
governmentcommitment,thedifferentialfeasibilityofgoals
across policy scenarios becomes visible. This sensitivity
analysisfunction, testingtherobustnessofplanninggoals
tovariationsinenablingconditions,isapowerfulcapabil-
ityforstrategicriskmanagementthatconventionalscenario
planning frameworks do not provide.Table 6 reports the
resultsofsensitivitytestingacrossthreegovernmentcom-
mitmentscenarios. Goalsrequiringgovernmentsupportas
acriticalenablingconditionshowthegreatestsensitivityto
policyvariation,confirmingconcentratedpolicyriskandthe
strategicimportanceofsustainedgovernmentalcommitment
acrossa25-yearplanninghorizon.
9

Urban Planning and Construction |Volume04|Issue02|November2026
Table 6. SensitivityAnalysis: PlanningGoalFeasibilityunderGradedGovernmentCommitmentScenarios.
Planning Goal (Brainport Pillar)
High Commitment Medium Commitment Low Commitment
Sustained Multi-term Policy
+ Dedicated Funding
Current Trajectory
+ Selective Support
Passive or Fragmented
Governmental Engagement
QuantumAdvancement
(Prompt6,Pillar1) Achievable Conditional NotAchievable
SustainableUrbanLiving
(Prompt6,Pillar2) Achievable Achievable Achievable
FloatingCityResilience
(Prompt6,Pillar3) Achievable Conditional Conditional
CulturalHeritageDestination
(Prompt6,Pillar4) Achievable Achievable Conditional
ConnectedCity
(Prompt6,Pillar5) Achievable Achievable Conditional
CommercialSpaceport
(Prompt6,Pillar6) Achievable Conditional NotAchievable
BrainportEcosystem
(Prompt6,Pillar7) Achievable Conditional Conditional
Goalsachievable(of7) 7/7 3/7 1/7
Note: Achievable(allHornclausepreconditionssatisfiable);Conditional(satisfiableonlyunderpartialenablingconditions);NotAchievable(oneormorecriticalpreconditions
unsatisfiable). AnalysisderivedfrompyDatalogbackwards-chainingqueriesrununderthreecommitment-levelfactconfigurations. N=7planninggoals.
6. Discussion
6.1. Theoretical Contributions
Thispapermakesthreecontributionstotheintersect-
ingliteraturesonstrategicplanning,AIinbusinessresearch,
andport-citydevelopment. First,weextendSPMAwitha
Gedankenvariantenablingsystematic,document-grounded
wild scenario generation without live stakeholder engage-
ment. Thisvariantismethodologicallyvaluablewherever
planning expertise is concentrated, time is constrained, or
the objective is to establish a scenario space before an ex-
penseofdeliberationbegins. TheGedankenapproachrepo-
sitionsstakeholderengagementasasubsequentratherthan
apriorstep,notdiminishingtheimportancebutsequencing
moreefficiently. Second,weintroduceHornclause-based
formalplanningasatoolforstrategicimplementationanal-
ysis in long-horizon urban contexts. Logic programming
has established Horn clauses as powerful tools for knowl-
edgerepresentationandinference [11],buttheirapplicationin
strategicplanning,particularlycombiningwithAI-generated
scenarios, remains rare in the strategic planning literature,
asdistinctfromthecomputationalplanningandAIinurban
systemsliteratures. Ourdemonstration,Hornclauseback-
wardchaining,cantranslatecompositewildscenariosinto
structureddependencymapsandtestthosemapsagainstcur-
rentconditions,openinganewmethodologicalavenuefor
research at the intersection of business strategy and urban
planning. Third, we operationalise the Brainport concept
withinaformallogicalframework. ByexpressingBrainport
asasetofHornclauses,thus,Knowledge_Economy ∧ Inno-
vation_Ecosystem∧ Educational_Excellence,wemakethe
constructdependenciesexplicitandtestable. Thisisamean-
ingful advance over prior treatments of Brainport, which
previouslyremainedlargelyqualitative [5–7],withoutspeci-
fyingtheconditionsthatmustholdforaregiontoachieve
thestatusofaBrainport.
The sensitivity analysis reported inTable 6 demon-
stratesafurthermethodologicalcapability: systematictest-
ingofplanninggoalrobustnessacrosspolicyscenarios. Un-
derlowgovernmentalcommitment,fiveofsevengoalsbe-
comeconditionalorunachievable,confirmingthatgovern-
mentpolicycontinuityisnotmerelyoneenablingcondition
among many but the structural prerequisite for the Cork
Brainportvision. Thisfunction,absentfromconventional
narrativescenarioplanningprovidesplannerswithstructured
riskanalysisattheimplementationstage,directlyinforming
strategicprioritisationdecisions.
Asecondtheoreticalclarificationconcernsthelimitsof
formaldeductiveplanningasappliedhere. TheHornclause
frameworkmakesdependencystructuresexplicitandtestable
within a deliberately simplified knowledge representation.
Thebinaryachievable/conditionalframingdoesnotcapture
10

Urban Planning and Construction |Volume04|Issue02|November2026
thepoliticaleconomyofurbandevelopment,distributional
impactsofinfrastructureinvestment,temporalsequencingre-
quirements,financialresourcedemandsateachdependency
node,orinstitutionalpathdependenciesthatmayconstrain
real-world implementation. These are genuine and poten-
tiallybindingconstraintsthatmayoverridelogicalfeasibility.
The formal planning exercise is therefore best understood
as a rigorous starting-point analysis—a structured map of
whatmustlogicallyholdforascenariogoaltobeachievable
ratherthanasanimplementationguarantee. Thedependency
map does not replace, but rather informs, the stakeholder
deliberation, institutionaldesign, andpoliticalnegotiation
processesthatmustfollowinanyrealplanningcontext.
6.2. Practical Implications
Forportauthoritiesandurbanplanners,AWSPFDof-
fers a practical escape from what we term the tyranny of
thecurrentbaseline,thetendencyofformalplanningtoan-
chor scenarios in present conditions and extrapolate mod-
estly. ByusinggenerativeAItoproducewildscenariosand
formally testing their feasibility, planners can identify the
ambitiousgoalswithinreachwithtargetedinvestmentand
requiring more fundamental capability development. For
policymakers,theHornclausedependencyanalysisprovides
a structured basis for prioritisation. The concentration of
governmentsupportasacriticalenablingconditionacross
three planning goals (Table 5) provides a clear, evidence-
grounded argument for policy continuity and institutional
commitment,thekindofstructuralinsightnarrativeplanning
rarelysurfaces. FromtheCorkperspectivespecifically,the
methodologyindicatesBrainportstatusisnotadistantaspi-
rationbutalogicallyachievablegoal,conditionalonthree
specificactions: sustainedgovernmentpolicycommitment,
deliberate cultivation of international technology partner-
ships,andactiveintegrationofUCCandMTUintotheport
innovation ecosystem. These are specific, actionable, and
directlymappabletoexistinggovernancestructures.
6.3. AI as a Strategic Planning Tool
ThispaperdoesnotpositionAIasasubstituteforhu-
man strategic judgment. Rather, it demonstrates theAI’s
valueasacreativeamplifier,expandingthescenariospace
beyondwhathumanplanners,constrainedbyexperienceand
cognitive heuristics, would typically generate. The expert
validationstepsembeddedthroughouttheworkflow( Table
2)ensurethatAIoutputsareevaluated,notsimplyaccepted.
Themethodologyishuman-in-the-loopbydesign. Thisar-
chitectureaddressesthehallucinationriskdocumentedinthe
LLMliteraturenotbyconstraininggenerativescopebutby
subjectingoutputstosystematicexpertreviewandformal
logicaltesting,combiningcreativefreedomwithstructural
discipline.
7. Limitations and Future Research
TheGedankenapproach,whilemethodologicallypro-
ductive, isathoughtexperimentbytworesearcherswork-
ing from public documents. The approach does not cap-
turethedistributedknowledgeofcommunities,businesses,
governmentagencies,andportworkerswhoseperspectives
areessentialtolegitimateplanning. Futureresearchshould
embedAWSPFD in live workshops, testing whether real-
time stakeholder knowledge generates richer or different
scenarioprofiles. Furthermore,themethodologyrelieson
ChatGPT-4o at a specific point in time development. Dif-
ferentLLMsmaygeneratedifferentscenarioprofiles. The
sensitivityofthemethodologytomodelchoiceisuntested
andwarrantssystematicinvestigation. Futureworkshould
compare outputs across models and develop protocols for
model selection appropriate to specific planning contexts.
Thisabsenceofprimaryempiricaldataisacknowledgedas
theprincipalmethodologicallimitationofthepresentstudy.
The Gedanken approach is explicitly designed as Phase 1
of a two-phase research programme; Phase 2 will embed
AWSPFD in live workshops with Port of Cork authority
planners and Cork City Council urban development staff,
withthedualpurposeofvalidatingtheAI-generatedscenario
space against practitioner knowledge and testing whether
real-time stakeholder input generates materially different
scenarioprofiles.
TheHornclauseformalizationisnecessarilyasimpli-
ficationofrealurbandevelopmentcomplexity. Thebinary
feasibilityframingof T able 5isastartingpoint;moresophis-
ticatedtreatmentswouldincorporateprobabilisticreasoning,
temporalsequencing,andresourceconstraints. Integration
withconstraintlogicprogrammingorprobabilisticDatalog
extensionsrepresentsaproductivedirectionformethodolog-
11

Urban Planning and Construction |Volume04|Issue02|November2026
icaldevelopment.
The framework should also be understood as a tech-
nicaltoolwithinabroadersocio-politicalplanningprocess,
not a substitute. Power dynamics, distributional concerns,
politicalfeasibility,andculturalspecificityofplanningas-
pirationsarenot addressedby thecurrent implementation.
Finally,GPT-4o’smultimodalcapabilitiesofprocessingau-
dio,images,andvideoalongsidetextremainuntestedinthis
workflow. Real-time integration of transcribed workshop
audio represents a significant future direction, potentially
enablingafullydynamicAI-augmentedplanningworkshop
whereinscenariosaregeneratedandtestedinthepresence
ofparticipants.
8. Conclusions
This paper has developed and demonstrated the
AWSPFDframework,integratinggenerativeAI,structured
scenarioplanning,service-dominantlogic,andHornclause
reasoningtoproduceambitious,formallygroundedplansfor
long-horizonport-citydevelopment. AppliedtoCorkCity
andPortby2050,theframeworkgeneratesacompositewild
scenariopositioningCorkasaglobalBrainportandidentifies
fiveofsevenscenariogoalsaslogicallycoherentimplemen-
tationpathwaysgivencurrentassetconditions,whileidenti-
fyingpreciselytheconditionsrequiredfortheremainingtwo.
Theframeworkdemonstratesacorestrengthofcombining
creative scope and analytical rigour. ChatGPT-4o’s gener-
ativecapacityproducesscenariosexceedingwhatconven-
tionalplanningtypicallyentertains. Hornclausebackward
chaining subjects the scenarios to structured, dependency-
aware analysis, transforming the scenarios from narrative
provocationsintoactionableplans. Together,thesecompo-
nents address a persistent gap: the difficulty of connect-
ing visionary futures with credible implementation path-
ways.Insuchafutureforportcities“…challengesaresignif-
icant,butcarefulplanningandimplementationcansurmount
them”[22].
AWSPFDisexplicitlydesignedtobetransferable. Any
portcityfacingalongplanninghorizon—adescriptionthat
fitshundredsofcitiesnavigatingdecarbonization,digitaliza-
tion,andeconomicrestructuring—canapplythemethodol-
ogy to its own context using existing planning documents
andinstitutionalassetsasinputs. Inthissense,Corkisboth
thesubjectofthisstudyandaproofofconceptforamethod-
ology with broader applicability. Port cities have always
been where futures are negotiated. Where goods, people,
and ideas arrive, transform, and depart. The methodology
shownhereis,atitscore,atoolformakingnegotiationsand
brainstormingmoresystematic,imaginative,andgrounded,
enablingplannerstoasknot“whatwillprobablyhappen?”
but“whatistrulypossibleinthebrain’seyeandhowtomake
theunbridledvisionareality.
Author Contributions
Conceptualization,S.S.;methodology,S.S.andH.P.;
writing—originaldraft,S.S.;reviewandediting,H.P.Both
authorshavereadandagreedtothepublishedversionofthe
manuscript.
Funding
Thisworkreceivednoexternalfunding.
Institutional Review Board Statement
Notapplicable.
Informed Consent Statement
Notapplicable.
Data Availability Statement
This study does not generate primary empirical data.
Theanalysisdrawsonthreepubliclyarchivedplanningdoc-
uments that are freely accessible online: the Cork 2050
Main Report (Cork County Council and Cork City Coun-
cil, 2017,https://www.corkcoco.ie/sites/default/file
s/2022-03/cork-2050-main-report-pdf.pdf ), the Port
of Cork Masterplan 2050 (PoCC, 2023,https://www.po
rtofcork.ie/wp-content/uploads/2023/05/Port-of-Cor
k-Masterplan-2050-Final-E-mail.pdf ), and the Ringask-
iddyPortRedevelopmentprojectdocumentation(EIB,2024,
https://www.eib.org/en/projects/all/20150383). ThePortof
CorkcruisescheduledatareferencedinSection3.1ispub-
liclyavailableat https://www.portofcork.ie/cruise-schedule/.
TheAI-generatedscenariooutputs(ChatGPT-4o,prompts
12

Urban Planning and Construction |Volume04|Issue02|November2026
1–6) are reproduced in full within the manuscript andTa-
ble 2 . The Python Datalog code implementing the Horn
clauseinferenceenginedescribedinSections4.4and5.3is
availablein Appendix C.Nodatasetsweredepositedina
third-partyrepository.
Acknowledgments
We thank Dr Conor Drummond at Cork University
Business School (https://research.ucc.ie/en/organisatio
ns/cork-university-business-school-9/ , https://orcid.or
g/0000-0002-6435-4292,tohostapresentationonourAI
useofgenerativeAI,scenarioplanningforurbanplanning
and providing feedback on creating an implementable yet
creativevisionofCork2050.
Conflicts of Interest
Theauthorsdeclarenoconflictofinterest.
AI Use Statement
Artificialintelligencetoolswereusedinboththesub-
jectandexecutionofthisresearch. Asacorecomponentof
theAWSPFDmethodologydescribedinSection4,ChatGPT-
4o(OpenAI,June2024version)wasusedtogenerateSWOT
analyses,strategicthemes,scenarionarratives,andthecom-
positewildscenarioforCorkCityandPort. AllAI-generated
outputsweresubjecttoexpertvalidationandreviewbythe
authorspriortoinclusion, asdocumentedin Table 2. The
AIwaspromptedusingthestructuredsequencedescribedin
Sections4.1and4.2;allpromptsarereproducedverbatimin
themanuscript. ThePythonDatalog(pyDatalog)inference
engineusedforformalplanninginSections4.4and5.3isa
logicprogrammingtool,notagenerativeAIsystem. Theau-
thorstakefullresponsibilityfortheintegrityoftheresearch,
thevalidityoftheAI-generatedcontentasreported,andfor
ensuringthatallconclusionsweredrawnwithouttheuseof
AI.
Appendix A
Table A1. GlobalBrainportComparators.
Location Model Type Key Characteristics Core Strengths Relevance to Cork
Europe
Eindhoven,
Netherlands
Triple-helixecosystem;
organictransformation
fromindustrial
dependence
5,000+techcompanies(Philips,
ASML);medicaltechnology,
renewableenergy,smart
systems;highinternational
talentdensity;multilingual
Two-decadetransitionfrom
single-companyreliance;
sustainedbusiness–
academia–government
collaboration;globalR&D
leadership
Mostdirectlyapplicable
model;mirrorsCork’s
anchor-company(Apple)
startingpointand
harbour-to-innovation
trajectory[7]
MiddleEast
NEOM,Saudi
Arabia
State-ledgreenfieldcity;
maximum-ambition
Brainportconcept
170-kmlinearcity(TheLine);
9millionresidentstarget;
100%renewableenergy;AI,
IoT,androboticsthroughout;
Vision2030diversification
Demonstratescapacityof
sovereigncommitmentto
generateradicalurban
innovation;zerolegacy
constraints;globaltalent
attractionatscale
Inspirationalceilingcase;
illustrateswhatsustained
statecommitmentcan
achievebutnotwithoutrisk
offailure;notareplication
template[23]
NordicOulu,
Finland
Health-techBrainport;
mid-sizeduniversitycity
Digitalhealthcluster;
OuluHealthecosystem;Oulu
UniversityHospital5Gsmart
hospital;living-labmodel;
strong
public–private–university
collaboration[24]
ProvesBrainportmodelworks
atmid-cityscale;flagship5G
hospitalapplication;integrates
healthcare,tech,andresearch
institutions
Comparablecityscaleto
Cork;demonstrates
university-anchored
innovationclusterwithout
megacityresources
Asia-Pacific
Singapore
State-directedknowledge
economy;globalhub
strategy
SustainedR&Dinvestment;
multinationalanchorpresence;
brainsciencesandneural
networkresearch;NTS-Group
linktoEindhovensupplychain
Showshowsustainedstate
investmentamplifies
location-specificresearch;
cross-Brainportknowledge
networkeffects;talent
attractionpolicy
Demonstratesthat
knowledgenetworks
amplifysingle-location
investment;relevantto
Cork–Atlanticcorridor
positioning[6,25]
NorthAmerica
SiliconValley,
USA
University-proximate
ventureecosystem;
self-reinforcinginnovation
culture
Stanford,UCBerkeley,San
JoseState;denseventure
capital;permissiveregulatory
culture;globaltechleadership;
significantsocio-economic
inequalityandhousingcosts
Archetypefor
research–capital–talent
proximity;demonstratespower
ofinnovationculture;
cautionaryevidenceon
inequalityanddisplacement
Benchmarkmodelwith
knownfailuremodes;Cork
shouldemulateecosystem
densitywhileexplicitly
managingequity
risks[26–28]
13

Urban Planning and Construction |Volume04|Issue02|November2026
Table A1. Cont.
Location Model Type Key Characteristics Core Strengths Relevance to Cork
EastAsia
Zhangjiang
Hi-TechPark,
Shanghai
Government-ledindustrial
policyBrainport;targeted
sectordevelopment
Est. 1992;2,500+foreign
enterprises(Roche,DuPont);
biotechnology,software,
electronics;MadeinChina
2025alignment;open
supply-chainmodel
DemonstratesrapidBrainport
creationthroughtargeted
policywhenmatchedwith
institutionalcapacity;proves
government-ledmodelatscale
Illustrateshowindustrial
policycanaccelerate
Brainportdevelopment;
relevantforCork’s
renewableenergyand
biotechsectorambitions [29]
Appendix B
Table A2. AIPrompts—VerbatimSequence(ChatGPT-4o,June2024).
Stage Prompt Text (Verbatim) Learning Mode Date/Version
1
Youareanexperturbanandportplanner. UsingthefulltextoftheCork2050Submission
totheNationalPlanningFramework,thePortofCorkMasterplan2050,andtheEIB
Ringaskiddyprojectdocumentation—alluploadedabove—produceacomprehensive
SWOTanalysisforCorkCityandPortasof2024.
Many-shot(full
documents[1–3]
uploaded)
June2024/GPT-4o
2
BasedonthethreeCorkplanningdocumentsuploaded,identifythefivetoseven
overarchingstrategicthemesthatcutacrossallthreedocuments. Presenteachthemewith
atitleandtwotothreesupportingsentencesdrawingonspecificevidencefromthe
documents.
Many-shot June2024/GPT-4o
3
SynthesiseacohesivestrategicoverviewofCorkCityandPort’sdevelopmenttrajectory
to2050,drawingontheSWOTanalysisandthestrategicthemesidentifiedintheprevious
steps. Theoverviewshouldreadasaunifiedanalyticalnarrativeofapproximately400
words.
Many-shot June2024/GPT-4o
4
UsingtheScenarioPlanningforMarketingAction(SPMA)frameworkand
service-dominantLogicprinciples,generatefivedistinctscenariosforCorkCityandPort
in2050. Eachscenarioshouldbeinternallyconsistent,groundedintheCorkassetbase,
andexploreadifferentplausiblefuturetrajectory. Labeleachscenariowithatitle.
Few-shot+
framework
examples[4]
June2024/GPT-4o
5
NowgeneratefivewildscenariosforCorkCityandPortin2050. Wildscenariosare
internallyconsistentandlogicallypossible,butsubstantiallybeyondconventional
planningassumptions. DonotbeconstrainedbycurrentCorkconditions. Eachscenario
mustanchorinatleastonerealCorkassetorgeographicaladvantage. Provideatitleand
150-worddescriptionforeach.
Zero-shot June2024/GPT-4o
6
Synthesisethefivewildscenariosintoasinglecompositewildscenariofor“Cork2050:
NexusofInnovationandSustainability”usingtheBrainportconceptastheorganising
framework. Structurethecompositearoundsevenstrategicpillars. Foreachpillar,provide
anameanda50-worddescriptionofthetargetstate. Thecompositeshouldbeambitious,
internallyconsistent,andgroundedinCork’sdemonstrableassets.
Few-shot(Stage5
elements
provided)
June2024/GPT-4o
Appendix C. Full pyDatalog Knowledge Base—Cork 2050 Brainport Imple-
mentation
Logicprogrammingtoolsused: pyDatalogv0.17.4,Python3.x [12].
FrompyDatalogimportpyDatalogpyDatalog.create_terms(#Facts—currentCorkconditions“Cork_Has_Univer-
sity_Cluster,Cork_Has_Tech_Anchor,Cork_Has_Deep_Harbour,”“Cork_Has_Renewable_Base,Cork_Has_EU_Fund-
ing,”#Enablingconditions“Government_Support,Partnership_with_Tech_Companies,”“Partnership_with_Space_Agen-
cies, Research_Institutions,” “Establish_Research_Facilities, Offer_Incentives,” “AI_Management, Safety_Protocols,
Autonomous_Vehicles,”“Smart_City_Tech,Ultra_Fast_Broadband,Cultural_Funding,”“Community_Involvement,Engi-
neering_Partnerships,”“Startups,Tech_Companies,Global_Talent_Attraction,”#Intermediategoals“Investment_in_Quan-
tum_Research, Attract_Global_Talent,” “Launch_Space_Initiative, Develop_Spaceport_Infrastructure,” “Space_Traf-
fic_Management,Knowledge_Economy,”“Innovation_Ecosystem,Educational_Excellence,”#Planninggoals“Quan-
14

Urban Planning and Construction |Volume04|Issue02|November2026
tum_Advancement,Sustainable_Urban_Living,”“Floating_City_Resilience,Cultural_Heritage_Destination,”“Connected_
City,Spaceport,Brainport”)#──BaseFacts(currentCorkconditions)────────────────────────────
+Cork_Has_University_Cluster()#UCC+MTU+Cork_Has_Tech_Anchor()#AppleEuropeanHQ+Cork_Has_Deep_Har-
bour()#OneofEurope’slargestnaturalharbours+Cork_Has_Renewable_Base()#Wind,solar,tidalresources+Cork_Has_
EU_Funding()#ASPBAN,EIBRingaskiddyinvestment#──Rules—QuantumAdvancement─────────────
───────────────────────Quantum_Advancement()<=(Investment_in_Quantum_Research()&Attract_
Global_Talent()) Investment_in_Quantum_Research() <= (Government_Support() & Partnership_with_Tech_Compa-
nies())Attract_Global_Talent() <= (Establish_Research_Facilities() & Offer_Incentives()) Government_Support() <=
Cork_Has_EU_Funding()Partnership_with_Tech_Companies()<=Cork_Has_Tech_Anchor()#──Rules—Sustainable
Urban Living ─────────────────────────────── Sustainable_Urban_Living() <= (Cork_Has_Re-
newable_Base() & Smart_City_Tech() & Autonomous_Vehicles()) Smart_City_Tech() <= Cork_Has_EU_Funding()
Autonomous_Vehicles()<=Cork_Has_Tech_Anchor()#──Rules—FloatingCityResilience────────────────
───────────────Floating_City_Resilience()<=(Cork_Has_Deep_Harbour()&Engineering_Partnerships()&
Cork_Has_Renewable_Base())Engineering_Partnerships()<=Cork_Has_EU_Funding()#──Rules—CulturalHeritage
Destination───────────────────────────Cultural_Heritage_Destination()<=(Cultural_Funding()&
Community_Involvement())Cultural_Funding()<=Government_Support()Community_Involvement()<=Cork_Has_Uni-
versity_Cluster()#──Rules—ConnectedCity──────────────────────────────────────────
Connected_City()<=(Autonomous_Vehicles()&Smart_City_Tech()&Ultra_Fast_Broadband())Ultra_Fast_Broadband()
<=Cork_Has_EU_Funding()#──Rules—CommercialSpaceport───────────────────────────────
─────Spaceport()<=(Launch_Space_Initiative()&Develop_Spaceport_Infrastructure()&Space_Traffic_Manage-
ment())Launch_Space_Initiative()<=(Government_Support()&Partnership_with_Space_Agencies())Space_Traffic_Man-
agement()<=(AI_Management()&Safety_Protocols())AI_Management()<=Cork_Has_Tech_Anchor()#──Rules—
BrainportEcosystem─────────────────────────────────────Brainport()<=(Knowledge_Econ-
omy()&Innovation_Ecosystem()&Educational_Excellence())Knowledge_Economy()<=(Research_Institutions()&
Global_Talent_Attraction()) Innovation_Ecosystem() <= (Startups() & Tech_Companies() & Government_Support())
Educational_Excellence() <= Cork_Has_University_Cluster() Research_Institutions() <= Cork_Has_University_Clus-
ter()Tech_Companies()<=Cork_Has_Tech_Anchor()Startups()<=(Cork_Has_Tech_Anchor()&Cork_Has_Univer-
sity_Cluster()) Global_Talent_Attraction() <= (Government_Support() & Offer_Incentives()) Offer_Incentives() <=
Cork_Has_EU_Funding()#──Queries─────────────────────────────────────────────
────────────goals=[(“QuantumAdvancement”,Quantum_Advancement()),(“SustainableUrbanLiving”,Sus-
tainable_Urban_Living()),(“FloatingCityResilience”,Floating_City_Resilience()),(“CulturalHeritageDestination”,Cul-
tural_Heritage_Destination()),(“ConnectedCity”,Connected_City()),(“CommercialSpaceport”,Spaceport()),(“Brainport
Ecosystem”,Brainport()),]forname,queryingoals: result=queryprint(f“{name}: {‘Achievable’ifresultelse‘Condi-
tional/NotAchievable’}”)
References
[1] CorkCountyCouncil,CorkCityCouncil,2017.Cork
2050: RealisingtheFullPotential.CorkCountyCoun-
cil,CorkCityCouncil: Cork,Ireland.Availablefrom:
https://www.corkcoco.ie/sites/default/files/2022-03/co
rk-2050-main-report-pdf.pdf
[2] PoCC(ThePortofCorkCompany),2023.PortofCork
Masterplan 2050: Executive Summary. The Port of
CorkCompany: Cork,Ireland.Availablefrom: https:
//www.portofcork.ie/wp-content/uploads/2023/05/Por
t-of-Cork-Masterplan-2050-Exec-Summary.pdf
[3] EIB(EuropeanInvestmentBank),2024.PortofCork:
RingaskiddyPortRedevelopment.EIB:Luxembourg,
Luxembourg.Availablefrom: https://www.eib.org/en
/projects/all/20150383
[4] Sood,S.C.,Pattinson,H.M.,2010.Marketersexpress-
ingthefuture: Scenarioplanningformarketingaction.
Futures.42(4),417–426.
[5] Pattinson,H.M.,Sood,S.C.,2006.Urbanrenewalin
Asia-Pacific: Acomparativeanalysisofbrainportsfor
Sydney and Kuala Lumpur. Journal of Business Re-
search.59(6),701–708.
[6] BrainportEindhoven,n.d.BrainportEindhoven.Avail-
15

Urban Planning and Construction |Volume04|Issue02|November2026
ablefrom: https://brainporteindhoven.com/en/(cited
10June2026).
[7] Bronneberg,M.,Pieterse,J.,Post,G.,2023.Brainport
Eindhoven: Bornfromcrisis—25yearsasaTripleHe-
lixGovernedEcosystem.JournalofInnovationMan-
agement.11(1),36–67.
[8] Inter-AmericanDevelopmentBank(IDB),2023.From
portstoinnovationecosystems: ACriticalTransforma-
tion.Availablefrom: https://www.iadb.org/en/blog/tra
de-and-investment/ports-innovation-ecosystems-criti
cal-transformation (cited10June2026).
[9] Lusch,R.,Vargo,S.,2006.Servicedominantlogic: Re-
actions,reflections,andrefinements.MarketingTheory.
6(3),281–288.
[10] Boute, R., 2008. Simple Gedanken Experiments in
LeveragingApplicationsofFormalMethods.In: Mar-
garia,T.,Steffen,B.(Eds.).LeveragingApplicationsof
FormalMethods,VerificationandValidation(ISoLA
2008): Communications in Computer and Informa-
tionScience,Vol17.Springer: Berlin/Heidelberg,Ger-
many.
[11] Ciatto,G.,Sabbatini,F.,Agiollo,A.,etal.2024.Sym-
bolic Knowledge Extraction and Injection with Sub-
symbolicPredictors: ASystematicLiteratureReview.
ACM Computing Surveys. 56(6), 161. DOI:https:
//doi.org/10.1145/3645103
[12] Carbonnelle, P., 2022. pyDatalog 0.17.4. Available
from: https://pypi.org/project/pyDatalog/ (cited
10June2026).
[13] Ligmann-Zielinska,A., Church, R.L., Jankowski, P.,
2008.Spatialoptimisationasagenerativetechniquefor
sustainable multiobjective land-use allocation. Inter-
nationalJournalofGeographicalInformationScience.
22(6),601–622.
[14] Erdem, E., Gelfond, M., Leone, N., 2016. Applica-
tionsofAnswerSetProgramming.AIMagazine.37(3),
53–68.Availablefrom: https://www2.cs.sfu.ca/Cours
eCentral/721/jim/aimag2016fall-dl.pdf
[15] Wikipedia,2024.CorkHarbour.Availablefrom: https:
//en.wikipedia.org/wiki/Cork_Harbour(cited10June
2026).
[16] PortofCork, 2024.Cruiseschedule.Availablefrom:
https://www.portofcork.ie/cruise-schedule/ (cited10
June2026).
[17] Apple,2020.Apple’sCorkcampuscelebrates40years
ofcommunity.Availablefrom: https://www.apple.co
m/au/newsroom/2020/11/apples-cork-campus-celebra
tes-40-years-of-community-and-looks-to-the-future/
(cited10June2026).
[18] ASPBAN,2021.ASPBAN—AtlanticSmartPorts: At-
lanticSmartPortsBlueAccelerationNetwork.Avail-
ablefrom: https://aspban.eu/en/home/(cited10June
2026).
[19] Malhotra,T.,2023.WhatIfLLMHallucinationsWere
aFeature?AndNotABug? MeetdreamGPT:AnOpen-
SourceGPT-BasedSolutionThatUsesHallucinations
from Large Language Models (LLMs) as a Feature.
Availablefrom: https://www.marktechpost.com/2023/
05/20/what-if-llm-hallucinations-were-a-feature-and
-not-a-bug/ (cited10June2026).
[20] OpenAI,2024.ChatGPT-4o(June2024version).Ope-
nAI:SanFrancisco,CA,USA.Availablefrom: https:
//openai.com/index/gpt-4o-and-more-tools-to-chatgpt
-free/
[21] Klein,G.,2007.Performingaprojectpremortem.Har-
vardBusinessReview.85(9),18–19.
[22] Chu,F.,Gailus,S.,Liu,L.,etal.,2018.Thefutureof
automatedports.Availablefrom: https://www.mckins
ey.com/industries/logistics/our-insights/the-future-o
f-automated-ports (cited10June2026).
[23] NEOM,2024.NEOMofficialwebsite.Availablefrom:
https://www.neom.com/en-us (cited10June2026).
[24] Oulu, 2026. Nordic Shine!—Oulu 2035: Oulu City
Strategy2035.OuluCityCouncil: Oulu,Finland.Avail-
ablefrom: https://www.ouka.fi/en/media/18648/dow
nload
[25] McGilvray,A.,2016.Singapore: Thebrain-gaingame.
Nature.537(7618),S16–S17.DOI: https://doi.org/10
.1038/537S16a
[26] Saxenian,A., 2014. The Silicon Valley model: Eco-
nomic dynamism, social exclusion. In: Castells, M.,
Himanen,P.(Eds.).ReconceptualizingDevelopmentin
theGlobalInformationAge.OxfordUniversityPress:
Oxford,UK.
[27] Gavet,M.,2020.What’snextforSiliconValley? Avail-
ablefrom: https://hbr.org/2020/09/whats-next-for-sil
icon-valley (cited10June2026).
[28] Fuerlinger,G.,Garzik,L.,2022.SiliconValleyinnova-
tionsystem.In: Garzik,L.(Ed.).SuccessfulInnovation
Systems.Springer: London,UK.pp.123–141.
[29] Kennedy, S., 2015. Made in China 2025. Centre for
StrategicandInternationalStudies: Washington,DC,
USA.Availablefrom: https://www.csis.org/analysis/
made-china-2025 (cited10June2026).
16
