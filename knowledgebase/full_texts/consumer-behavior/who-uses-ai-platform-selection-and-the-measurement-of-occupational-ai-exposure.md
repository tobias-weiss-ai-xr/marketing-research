---
title: Who Uses AI? Platform Selection and the Measurement of Occupational AI Exposure
url: https://arxiv.org/abs/2605.21743
category: consumer-behavior
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Michelle Yin
- Burhan Ogut
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.21743
pages: 73
chars: 173316
fetched_at: '2026-11-08T12:59:58+00:00'
kb_version: 1
---

# Who Uses AI? Platform Selection and the Measurement of Occupational AI Exposure

Who Uses AI? Platform Selection and the Measurement of Occupational AI
Exposure
MichelleYinandBurhanOgut ∗
Abstract
ConversationlogsfromAIplatformsareincreasinglyusedtomeasureoccupationalexposuretoartifi-
cialintelligence,buttheusersobservedintheselogsarenotarepresentativesampleoftheworkforce.
Thispapershowsthatplatform-derivedexposurescorescombinetask-levelAIapplicabilitywiththe
occupationalcompositionoftheplatform’suserbase. Holdingtheempiricaldesignfixed,changing
only the platform input changes the post-ChatGPT employment coeﬀicient by a factor of 1.9, and
consumerandenterprisechannelswithinthesamevendordisagreeinsign. Weformalizetheresult-
ing non-classical measurement error, decompose it into between- and within-occupation selection,
and construct workforce-reweighted partial-identification bounds. Reweighting to Bureau of Labor
Statistics employment shares attenuates estimates by 42 to 93 percent. The bias captures augmenta-
tionamongobservedusersmoredirectlythansubstitutionintheworkforce.
JEL:C18,C26,C81,J23,J24,O33
Keywords:Artificialintelligence;measurementerror;occupationalexposure;non-probabilitysam-
pling;partialidentification;technologyandlabormarkets
∗ Yin: SchoolofEducationandSocialPolicy,NorthwesternUniversity,2120CampusDrive,Evanston,IL60208(email: michelle.yin@northwestern.edu); Ogut:
AmericanInstitutesforResearchandSchoolofEducationandSocialPolicy,NorthwesternUniversity(email: burhan.ogut@northwestern.edu). WethankAlieGoldblatt,
Megan Ashley Morrell, and Maggie Liao for excellent research assistance, and David Figlio, Peter Steiner, Hoa Vu, Regina Seo, Diego Guerrero, Ruhan Circi, and
participantsintheRISEILabSeminarSeriesatNorthwesternUniversityforhelpfulcommentsandsuggestions. WearegratefultoAlexanderBick,AdamBlandin,and
David Deming for sharing the Real-Time Population Survey AI module micro release. The contents of this study were developed under Grant No. H421D220008 from
theU.S.DepartmentofEducation,RehabilitationServicesAdministration. TheDepartmentdoesnotmandateorprescribepractices,models,orotheractivitiesdescribed
or discussed in this document. The contents of this study may contain examples of, adaptations of, and links to resources created and maintained by another public or
privateorganization. TheDepartmentdoesnotcontrolorguaranteetheaccuracy,relevance,timeliness,orcompletenessofthisoutsideinformation. Thecontentofthis
studydoesnotnecessarilyrepresentthepolicyoftheDepartment. Thispublicationisnotintendedtorepresenttheviewsorpolicyoforbeanendorsementofanyviews
expressedormaterialsprovidedbyanyFederalagency(EDGAR§75.620). Theauthorsdeclarethattheyhavenorelevantormaterialfinancialintereststhatrelatetothe
researchdescribedinthispaper. Dataandreplicationmaterialsareavailableuponrequestfromthecorrespondingauthor.
1
arXiv:2605.21743v2  [cs.AI]  27 May 2026

A growing empirical literature measures occupational exposure to artificial intelligence using conver-
sation logs from platforms such as Anthropic’s Claude (Handa et al. 2025; Appel et al. 2025), OpenAI’s
ChatGPT (Chatterji et al. 2025), and Microsoft Copilot (Tomlinson et al. 2025). These measures represent
an important advance because they move exposure measurement from hypothetical capability toward ob-
served use. The measurement problem is that observed platform use is not drawn from the workforce, but
from the users who enter a particular platform. A platform-derived exposure score therefore combines the
task content of an occupation with the occupational composition of the platform’s user base. When plat-
formparticipationdifferssystematicallyfromworkforceemployment,estimatesbuiltonthesescoresinherit
platform-specificselection.
This distinction matters because occupational AI exposure measures increasingly enter empirical work
on employment, wages, and labor-demand reallocation as fixed regressors. A measure used in this way is
implicitlytreatedasastablecharacteristicoftheoccupation. Underthatinterpretation,changingtheplatform
sourceshouldnotmateriallychangethecoeﬀicientoncetheempiricaldesignisheldfixed. Inourestimates,
changingonlytheplatforminputchangestheemploymentcoeﬀicientsubstantiallyinmagnitudeandreverses
itssigninseveralcomparisons,evenwhentheregressiondesignisheldfixed. Theregressorthereforevaries
withbothoccupationalexposuretoAIandtheoccupationalcompositionoftheplatformthatproducedit.
ThemeasurementproblemfollowsfromhowtheAIexposureliteraturehasevolvedoutofthetask-based
tradition in labor economics.Autor, Levy, and Murnane (2003)treat an occupation as a bundle of tasks
andaskwhichtasksatechnologycansubstitutefororcomplement. Thatframeworkshapedtheautomation
and job-polarization literature, where the choice of routine-task index affected downstream estimates and
interpretation (Acemoglu and Autor 2011; Goos, Manning, and Salomons 2014; Acemoglu and Restrepo
2020). EarlyAIexposuremeasuresadaptedthistask-basedlogicusinginputsexternaltoobservedplatform
use, including expert ratings (Frey and Osborne 2017), patent-text matching (Webb 2020), AI-capability
benchmarks (Brynjolfsson, Mitchell, and Rock 2018; Felten, Raj, and Seamans 2021), and the task-level
applicabilityrubricof Eloundouetal.(2024) ,whichhasbecomeoneofthecentralcapability-basedmeasures
intheliterature.
Platform logs add a second source of measurement by observing where AI appears in use rather than
onlywhatAIcoulddo. Recentworkhasbeguntocombinethesemargins. MassenkoffandMcCrory(2026) ,
forexample,weighttheEloundourubricbyAnthropicconversationsharesandreportthattheresultingcom-
posite predicts Bureau of Labor Statistics employment projections while the rubric alone does not. This
findingexplainswhyplatformdatahavebecomemorepopular. Theybringexposuremeasurementcloserto
economic use, but they also change the source of variation in the measure. Once conversation shares enter
2

the score, measured exposure reflects task-level AI applicability together with the occupations the platform
reaches.
Existinglabor-marketdataleaveroomforplatformmeasuresbecausenosinglesourcecapturescapability,
adoption,andtaskintensityatscale. WorkersurveysmeasureAIadoptioninapopulationframeandobserve
bothusersandnonusers. Bick,Blandin,andDeming(2026) andtheU.S.CensusBureau’sHouseholdTrends
and Outlook Pulse Survey (U.S. Census Bureau 2025) field such measures nationally, and the Organisation
for Economic Co-operation and Development (OECD) has developed cross-national instruments for man-
ufacturing and finance workers (Lane, Williams, and Broecke 2023). These surveys identify the extensive
margin of use, but their per-wave samples are often too small for detailed occupation-level rates and pro-
videlesstask-leveldetailthanplatformlogs. Administrativerecordsandfieldexperimentsobserveusemore
precisely in specific settings (Noy and Zhang 2023; Brynjolfsson, Li, and Raymond 2023; Cui, Demirer,
Jaffe, Musolff, Peng, and Salz 2024; Dell’Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran,
Krayer,Candelon,andLakhani2023 ),buttheirworkforcesandtaskdomainslimitgeneralizability. Platform
logssitbetweenthesesourcesbecausetheyproviderevealedtask-levelbehavioratlargescale,whilethescale
itselfcomesfromaselectedplatformpopulationratherthanfromaworkforcesample.
The selection embedded in platform logs is large enough to change inference. A platform’s conversa-
tion distribution is shaped by pricing, product launches, enterprise contracts, competitive position, and the
occupations for which the platform is useful enough to generate repeated use. Computer and Mathematical
occupations generate 32 percent of consumer Claude conversations and 52 percent of enterprise conversa-
tions (Handa et al. 2025; Appel et al. 2025), compared with 3.4 percent of U.S. employment. Food Prepa-
ration workers hold 8.8 percent of employment but generate only 0.7 percent of conversations. Across the
22StandardOccupationalClassificationmajorgroups,theratioofconversationdensitytoemploymentden-
sity spans a factor of 72, and no platform-derived measure correlates with BLS employment shares above a
Spearmanrankcorrelationof0.33. AregressionusingsuchameasureloadsonbothunderlyingAIapplica-
bility and platform penetration. We show formally that the resulting coeﬀicient generally does not identify
thestructuralemploymentelasticity.
Our empirical design isolates the user-base channel by rebuilding the composite exposure score of
Massenkoff and McCrory (2026), which weights the Eloundou et al. (2024) per-task rubric by each
occupation’s platform conversation share. We hold fixed the specification, sample, outcome, estimator, and
task-capability rubric, and vary only the source of the conversation shares. The ten variants come from
Anthropic Claude consumer and enterprise channels across several waves and from Microsoft Copilot.
Holdingtherubricfixedisolatesthecontributionofplatformconversationshares,whichisimportantbecause
3

capability ratings are themselves sensitive to the model used to rate them (Yin, Vu, and Persico 2026). We
estimate the resulting specifications on a 2015 to 2024 American Community Survey panel of 13.1 million
person-year observations merged at the six-digit occupation level, using a difference-in-differences design
commonintheAI-and-laborliterature.
The estimates move in ways that are diﬀicult to reconcile with a platform-independent occupational ex-
posure measure. Across the ten variants, the post-2022 employment coeﬀicient ranges by a factor of 1.9.
Within Anthropic, replacing the consumer channel with the enterprise channel reverses the sign of the em-
ployment estimate at every observed release, even though the two channels share the same vendor, model
family, classification procedure, and task rubric. This comparison leaves user-base composition as the re-
mainingeconomicallyrelevantsourceofvariation. Theexposuremeasurealsochangesovertimewithinthe
same channel. A researcher using the earliest Claude consumer release would estimate that a one-standard-
deviation increase in exposure lowers employment by 0.12 percentage points, while a researcher using the
latest release would estimate a decline of 0.22 percentage points. The difference comes only from the wave
ofplatformdatausedtoconstructexposure.
Weformalizethisinstabilityasnon-classicalmeasurementerror( Bound,Brown,andMathiowetz2001 ;
Meng2018). Theplatformproxycombinestrueoccupationalexposurewithplatform-specificselection,and
that selection is correlated with the task structure the measure is intended to capture. The framework de-
composes the bias into a between-occupation margin, which captures which occupations enter the platform
user base, and a within-occupation margin, which captures which tasks workers perform once observed on
the platform. Because the between-occupation component is observed in platform and workforce occupa-
tion shares, reweighting platform shares to BLS workforce shares removes that component under the main-
tained condition that within- and between-occupation selection move in the same direction. The baseline
and workforce-reweighted estimates then define endpoints of a partial-identification interval for the struc-
tural employment elasticity (Manski 2003). The width of the interval measures how much of the estimated
association is attributable to observable platform selection rather than to the relationship between AI expo-
sureandemployment.
The empirical results follow the ordering implied by the framework. Measures drawn from user bases
farther from the workforce move more after reweighting. For the Anthropic composite, reweighting atten-
uates the employment coeﬀicient by 93 percent and leaves an estimate statistically indistinguishable from
zero. For Microsoft Copilot, whose user base is closer to workforce employment shares, the coeﬀicient at-
tenuatesby42percentandremainsstatisticallysignificant. Thesamechannelalsoappearsinthepublished
cross-occupation specification. Reweighting theMassenkoff and McCrory (2026)composite to workforce
4

shares reduces the projected employment-growth association from 0.70 to 0.38 percentage points for a one-
standard-deviationincreaseinexposure. Thisimpliesthat45percentofthepublishedmagnitudedisappears
whentheplatform’soccupationalcompositionisreplacedwithworkforcecomposition.
The paper contributes to the literature in four ways. It identifies a measurement problem specific to
platform-derived AI exposure, where the error is selected on the same occupation-level task structure the
measureisintendedtocapture. Itthenprovidesempiricaldiagnosticsshowingthatplatformsource,product
channel, and platform wave change downstream coeﬀicients even when the regression design is fixed. The
workforce-reweighting procedure and partial-identification bounds convert this instability into an estimable
component of the coeﬀicient. Finally, the distributional analysis shows that platform selection is correlated
withwages,education,andoccupationaladvantage,implyingthatexposurerankingsbasedonplatformlogs
canunderweightoccupationswherelowvisibilityreflectslimitedaccess,lowadoption,ordisplacementrisk
ratherthanlowexposure.
The findings clarify the parameter that platform data can support rather than diminishing the value of
platform logs. Platform data are informative about task intensity among active users, especially at a scale
and frequency unavailable in surveys or administrative records. They are less informative about nonusers,
workers weakly represented on the platform, and tasks or workers displaced from the observed occupation-
platform pair. Usage-based measures therefore recover augmentation among observed users more directly
thansubstitutionin theworkforce. Thisdistinctionchangesbothinferenceandallocation. Ina hypothetical
retrainingexercise,aplatform-weightedrankingdirects39percentofaten-billion-dollarfundtooccupations
thataworkforce-weightedrankingdoesnotidentifyasexposed. Moregenerally,appliedworkusingplatform-
derived exposure should report workforce-reweighted counterparts, test sensitivity to platform source, and
distinguish task capability, worker adoption, and use conditional on adoption. Without these distinctions,
variation in measured exposure can reflect platform adoption across occupations rather than variation in
underlyingAIapplicability.
The rest of the paper proceeds as follows. Section I develops the measurement framework. Section
IIdocumentsplatform-workforcedivergence. SectionIIIestimatesitsconsequencesforlabor-marketcoeﬀi-
cientsandpartial-identificationbounds. SectionIVexaminesdistributionalincidence,andSectionVreports
robustnesschecks.
I. Conceptual Framework
Let 𝑜indexthesix-digitoccupationalcategoriesusedthroughoutthepaper,andlet 𝐸𝑜 denotetrueAIexpo-
sure. Wedefine 𝐸𝑜astheshareofanoccupation’staskbundleforwhichAIcansubstitutefororcomplement
5

workerinputatcomparablequality. Therelationshipofinterestis
𝑌𝑜 = 𝛽𝐸 𝑜 + 𝑋 ′ 𝑜𝛿 + 𝜀 𝑜, (1)
where 𝑌𝑜 is a labor-market outcome,𝑋𝑜 is a vector of controls, and𝐸[𝜀𝑜 ∣ 𝐸 𝑜, 𝑋𝑜] = 0 . In practice,
𝐸𝑜 is unobserved. Researchers instead condition on a platform-derived proxy,𝐸𝑜,𝑝, constructed from con-
versation logs on platform𝑝. The central measurement question is whether𝐸𝑜,𝑝 can be treated as a fixed
occupational characteristic, analogous to a routine-task index or a robot-exposure measure. It cannot when
theproxydependsonwhichoccupationsentertheplatform’suserbase.
Thedeparturefromworkforceexposurehastwomargins. Betweenoccupations,let 𝑓𝑝(𝑜)betheshareof
platform 𝑝’sconversationsassociatedwithoccupation 𝑜,andlet 𝑓(𝑜) betheoccupation’semploymentshare
intheBLSOccupationalEmploymentandWageStatistics. Define
𝜓𝑜,𝑝 ≡ 𝑓𝑝(𝑜) 𝑓(𝑜) . (2)
Theparameter 𝜓𝑜,𝑝 measuresplatformrepresentationrelativetotheworkforce. Itexceedsoneforoccu-
pationsoverrepresentedontheplatformandfallsbelowoneforoccupationsunderrepresentedontheplatform.
Withinoccupations,let 𝜃𝑜,𝑘,𝑝 measurehowtheplatformshareoftask 𝑘withinoccupation 𝑜differsfromthe
correspondingworkforcetaskshare. Thetwoparameterscapturedistinctsourcesofselection. Theplatform-
selection parameter𝜓𝑜,𝑝 governs which occupations appear in platform data. The task-selection parameter
𝜃𝑜,𝑘,𝑝 governswhichtasksworkersperformconditionalonappearingthere.
Withthisnotation,theplatform-derivedproxycanbewrittenas
𝐸𝑜,𝑝 = 𝜓 𝑜,𝑝𝐸𝑜 + 𝜂𝑜,𝑝 + 𝑢𝑜,𝑝, (3)
where 𝜂𝑜,𝑝 collects within-occupation task-selection differences and𝑢𝑜,𝑝 is classical noise. Appendix
A.2 derives this expression from task-level conversation shares. The between-occupation component,𝜓𝑜,𝑝,
is observed from platform and workforce occupation shares. The within-occupation component,𝜃𝑜,𝑘,𝑝, is
not observed with current data because no worker-representative source links task-time use to theO*NET
taskcategoriesusedbytheplatformmeasures.
Equation (3) implies non-classical measurement error. The error is not random noise around a fixed
occupationalexposure. Itiscorrelatedwithtrueexposurewhenoccupationsoverrepresentedontheplatform
arealsooccupationswithhightask-levelAIapplicability. Thedatadisplayexactlythispattern. Computerand
6

Mathematical occupations are far more represented in platform conversations than in the workforce, while
many service and manual occupations are underrepresented. A platform-derived exposure score therefore
combinestaskexposurewithplatformpenetration.
To see the implication for regression coeﬀicients, suppose a researcher estimates equation (1) after re-
placing 𝐸𝑜with 𝐸𝑜,𝑝. Afterresidualizingwithrespectto 𝑋𝑜,writethelinearprojectionoftheproxyontrue
exposureas
𝐸𝑜,𝑝 = 𝜆 𝑝𝐸𝑜 + 𝑣𝑜,𝑝, Cov(𝐸𝑜, 𝑣𝑜,𝑝) = 0.
Let 𝜅𝑝 = Var(𝐸𝑜)/Var(𝑣𝑜,𝑝). Theprobabilitylimitofthecoeﬀicientontheplatformproxyis
plim ̂𝛽𝑝 = 𝛽𝜆𝑝𝜅𝑝 𝜆2𝑝𝜅𝑝 + 1 . (4)
AppendixA.3givesthederivation. Theexpressiondiffersfromtheclassicalerrors-in-variablesformula
because 𝜆𝑝neednotequalone. Whentheplatformuserbasemirrorstheworkforce, 𝜆𝑝 = 1,andequation(4)
reducestoclassicalattenuation. Whenplatformrepresentationisskewedtowardhigh-exposureoccupations,
𝜆𝑝differsfromone,andthecoeﬀicientbecomesplatform-specific. Aregressionwiththesameoutcome,con-
trols,sample,andestimatorcanthereforerecoverdifferentcoeﬀicientssolelybecausetheexposuremeasure
isdrawnfromadifferentplatformorproductchannel.
This logic has two empirical implications. First, coeﬀicients should vary across platforms and product
channels if those platforms and channels reach different occupations. Second, coeﬀicients should move
over time within a platform when product launches, pricing changes, or enterprise contracts shift the user
base. Additional conversations from the same selected platform improve precision for the platform-specific
measure, but they do not change the population represented in the proxy. The probability limit remains
platform-specific.
The framework also points to a correction. Because𝜓𝑜,𝑝 is observed, we can remove the between-
occupationcomponentbyreweightingtheproxytotheworkforce:
̃𝐸𝑜,𝑝 ≡ 𝐸𝑜,𝑝 𝜓𝑜,𝑝 . (5)
Substitutingequation(3)gives
̃𝐸𝑜,𝑝 = 𝐸 𝑜 + 𝜂𝑜,𝑝 𝜓𝑜,𝑝 + 𝑢𝑜,𝑝 𝜓𝑜,𝑝 . (6)
7

If within-occupation task selection is absent, so that𝜂𝑜,𝑝 = 0, the reweighted proxy recovers true expo-
sure up to classical noise. If within-occupation task selection remains, reweighting does not identify𝛽 by
itself, but it removes the observable between-occupation channel. Under the maintained ordering condition
that within-occupation selection moves in the same direction as between-occupation selection, the baseline
and workforce-reweighted estimates form endpoints of a partial-identification interval for the structural em-
ploymentelasticity. Thewidthofthisintervalmeasuresthecontributionofobservableplatformcomposition
tothecoeﬀicient.
This framework locates platform-derived AI exposure outside the standard treatment of occupational
exposure as predetermined. Routine-task indices and robot-exposure measures are fixed by construction.
Platform-derivedmeasuresmovewithproductdesign,pricing,anduseradoption. Theyarethereforecloser
to non-probability samples, where the relevant distortion depends on the correlation between selection and
thevariableofinterestratherthanonsamplesize( Meng2018). Inthissetting,thecorrespondingobjectisthe
relationshipbetween 𝜓𝑜,𝑝and 𝐸𝑜. Ifhigh-exposureoccupationsarealsooverrepresentedontheplatform,the
platformproxydoesnotconvergetotheworkforceexposuremeasuresimplybyaddingmoreconversations.
II. Platform Exposure Measures and the Workforce Benchmark
This section describes the exposure measures, workforce benchmarks, and analytical samples used in the
empiricalanalysis. Itthenestablishesthecentralempiricalpremiseofthepaper: platform-derivedexposure
measuresarenotworkforce-representativemeasuresofoccupationalAIexposure. Wedocumentthisinthree
ways. First,platformoccupationsharesdiffersharplyfromworkforceemploymentshares. Second,platform
exposure rankings change over time within the same vendor. Third, workforce reweighting changes which
occupationsareclassifiedasmostexposed.
A. AI Exposure Measures and Benchmark Data
TheprimaryplatformsourceistheAnthropicEconomicIndex(AEI, Handaetal. 2025 ,Appeletal. 2025 ),
which maps anonymized Claude conversation transcripts toO*NET task descriptions and aggregates them
toper-occupationconversationsharesatthesix-digitStandardOccupationalClassification(SOC)level. The
mapping uses the Clio classifier (Tamkin et al. 2024), which embeds conversation text and theO*NET
task descriptions in a shared vector space and assigns each conversation to its nearest task. The AEI has
five publicly released waves from December 2024 to February 2026. These waves span five Claude model
versions,fromClaude3.5SonnetinWave1toOpus4.6inWave5. ThelastthreeseparatelyreportClaude.ai
consumeruseandenterprisefirst-partyApplicationProgrammingInterface(API)use.
8

The timing of the Anthropic waves is useful for this study because the period includes changes that
plausiblyshifttheuserbase. ClaudeCodelaunchedinMarch2025,ClaudeProjectsexpandedinmid-2025,
pricingchangedatleasttwice,andtheenterprisecustomerbaseexpandedsubstantially. Thesechangesmean
thatcross-wavevariationisnotonlyacomparisonofmodelreleases. Itisalsoacomparisonoftheworkers
andoccupationsthatentertheplatformconversationpool. Ifmeasuredoccupationalexposurechangesaround
theseevents,thechangereflectsplatformadoptionaswellastask-levelAIapplicability.
We also use several platform-derived measures outside Anthropic. The Microsoft Copilot AI applica-
bilityscoreisasix-digitoccupation-levelmeasureconstructedfromroughly200,000Copilotconversations
sampledinSeptember2024andscoredonazero-to-oneapplicabilityscale. WeusetheCopilotmeasurein
raw and workforce-reweighted form. OpenAI ChatGPT plays a different role. We use the public ChatGPT
occupational distribution as a second-platform reference distribution, but it does not enter the ten-measure
regression set because the public release reports occupational shares at the SOC major-group level rather
thanatthesix-digitSOClevel.
TheMassenkoffandMcCrory(2026) compositeaggregatesAEIconversationsharestooccupationsusing
O*NET task-time weights and theEloundou et al. (2024)GPT-4 applicability rubric. Three composite
variants enter the analysis. The first is the published baseline composite. The second replaces platform
conversationdensitywithOEWSworkforcedensityandthethirdreplacestheoriginalconversationweights
with Wave 5 AEI weights. Together with three Claude.ai consumer waves, two enterprise API waves, and
two Copilot variants, these three composites make up the ten platform-derived exposure measures. The
composite enters the paper in two roles. In the measurement and DiD exercises, the composite is one of
the ten platform-derived exposure measures used to test cross-platform dispersion. In the cross-occupation
exercise, we return to the between-occupation regression for which the composite was originally proposed
andaskwhetherthesameuser-basechannelchangesthatpublishedestimate.
We draw on three benchmark data sources. The BLS OEWS May 2024 release supplies the workforce
density, 𝑓(𝑜), used to construct𝜓𝑜,𝑝 and implement the workforce reweighting. The BLS Employment
Projectionsfor2024to2034supplythedependentvariableforthebetween-occupationregression. TheReal-
Time Population Survey (RPS) fromBick, Blandin, and Deming (2026)provides an independent worker-
reported measure of at-work AI use at the six-digit SOC level (Online Appendix Table B.12 documents the
RPSmicroreleaseattheSOCmajor-groupandsix-digit-SOClevel).
Arelatedmeasurementconcernisthemappingfromconversationstotasks. Bick,Blandin,Deming,and
Schumacher (2026)show that chat-based task shares diverge from worker-survey task shares because the
chat-to-task step over-attributes conversations to genericO*NET tasks. More than 15 percent of OpenAI
9

chatsareassignedtoËditwrittenmaterialsordocuments,älthoughonly1.6percentofworkersareemployed
in occupations containing that task. In their RPS data, the top 5 percent of tasks account for 19 percent of
generative AI use, compared with 57 percent in chat-based data. The correlation between chat-based and
survey-basedmeasuresisbelow0.4.
Our mechanism is distinct. Their distortion arises within occupations, through the mapping from con-
versations to tasks. Ours arises between occupations, through which occupations enter the platform conver-
sation pool. The two mechanisms can operate together. The workforce reweighting in Section I removes
the between-occupation component, while any remaining gap reflects within-occupation task selection and
classificationdifferences.
B. Analytical Sample
The worker-level analysis uses a 2015 to 2024 ACS person-year panel constructed from Integrated Public
Use Microdata Series (IPUMS). We restrict the sample to civilian wage-and-salary workers ages 16 to 64
with a valid six-digit SOC code and at least one of the ten exposure measures defined for the worker’s oc-
cupation. The panel contains 13.1 million person-year observations across 553 occupations and ten survey
years. Eachrecordlinkstheworker’soccupationtoaplatform-derivedexposuremeasure,workforcedensity,
demographiccontrols,andlabor-marketoutcomes.
Five of the ten measures, the three composite variants and the two Copilot variants, need a crosswalk
between the ACS occupation code and the National Employment Matrix (NEM) code that the composite
andtheCopilotreleaseuse. Thecrosswalkreducestheanalyticalsampleto65.9percentofthefull(Online
Appendix Table B.3 documents crosswalk coverage by SOC major group). The matched sample is more
female (0.50 against 0.39), younger (39.6 against 41.5), and less educated (0.31 against 0.47 Bachelor’s or
higher) than the dropped records, which concentrate in higher-skill occupations the Anthropic and Copilot
releasescoveratsix-digitSOC.Table3reportssamplesizesalongsidecoeﬀicientstodifferentiatecoverage-
drivenfromuser-base-drivendispersion.
The cross-domain test in Section IV uses ten occupation-level outcomes, five from the ACS 2011 to
2022 (hours worked, three education shares, and disability prevalence) and five from the National Health
InterviewSurvey(NHIS)SampleAdultfilesfor2017and2018(Kessler-6distress,smoking,drinking,short
sleep, and self-rated health). Employment, labor-force participation, and log weekly wages stay out of this
setbecausetheyarethemainDiDoutcomes. OnlineAppendixBaddsthosethreebackforafifteen-outcome
family with full multiple-testing corrections, and Online Appendix B.1 documents the variables and cross-
walks. Table 1 reports summary statistics for the analytical sample, the NEM-matched subsample, and the
10

ten measures. Online Appendix Table B.1 gives variable definitions, and Online Appendix Table B.2 Panel
Breportsoccupation-levelmeansbySOCmajorgroup.
C. Platform-Workforce Divergence
Theplatformmeasuresdiffersharplyfromtheworkforcebenchmark. Atthesix-digitSOClevel,noplatform-
derivedmeasurehasaSpearmancorrelationwithBLSemploymentsharesabove 𝜌 = 0.33,whileAnthropic
wavescorrelatemuchmorestronglywithoneanother,withpairwisecorrelationsrangingfrom0.84to0.98.
Theplatformmeasuresalsodifferfromtheworker-reportedRPSbenchmark,withnocorrelationabove 𝜌 =
0.41. Figure 1 summarizes these pairwise correlations. The pattern is consistent with the framework in
SectionI:platform-derivedmeasuresareclosertooneanotherthantoaworkforcepopulationframe.
Theoccupationalcompositionofthegapissystematic. Table2reports 𝜓𝑜,𝑝 bySOCmajorgroupacross
platforms (Online Appendix Table B.2 Panel A reports the full per-platform composition by SOC major
group). ComputerandMathematical,OﬀiceandAdministrativeSupport,andBusinessandFinancialOpera-
tionsoccupationsareoverrepresented,whileTransportation,Production,Construction,andFoodPreparation
occupationsareunderrepresented. Thismattersbecausetheoverrepresentedgroupsarealsothegroupsthat
AIcapabilityrubricstendtorateashighlyapplicable. Platformdatathereforeplacegreaterweightonoccu-
pationswheretherubricalreadypredictshighexposure,whichispreciselythecovariancebetweenplatform
selectionandtaskapplicabilitythatgeneratesnon-classicalmeasurementerror.
The same user-base imbalance changes the exposure profile itself. Figure 2 compares theMassenkoff
and McCrory (2026)composite with theEloundou et al. (2024)capability rubric across the 22 SOC major
groups. The consumer composite tracks the rubric closely for Computer and Mathematical, Business and
Financial, and Oﬀice and Administrative Support occupations, but falls below the rubric for Personal Care,
Food Preparation, and Transportation, where consumer platform users are sparse. The enterprise API tilts
further toward Computer and Mathematical occupations, which account for more than half of its conversa-
tions. Copilotremainsclosertotherubricbecauseitsuserbaseisclosertotheworkforce. Acrosspanels,the
exposureprofiledepartsmorefromtherubricwhentheplatform’susersdepartmorefromtheworkforce.
Thesecomparisonsestablishthefirstempiricalimplicationoftheframework. Platform-derivedmeasures
arenotalternativenoisyestimatesofthesameworkforceexposureprofile. Theyembedoccupation-specific
platformrepresentation. Downstreamestimatesbasedonthesemeasuresthereforeinheritapopulationchoice
thatisusuallyleftimplicit.
11

D. Temporal Instability Within a Platform
The divergence from the workforce is not only a fixed difference across vendors. It also changes within a
vendor over time, which means that vendor fixed effects cannot absorb the user-base component when the
compositionofusersshiftsacrosswaves.
The Anthropic Economic Index waves appear stable when summarized by rank correlations. Pairwise
Spearman correlations range from 0.92 to 0.98 for adjacent waves and from 0.84 to 0.90 for non-adjacent
waves. Even Wave 1 and Wave 5, which are fourteen months apart, have a correlation of𝜌 = 0.85. Yet this
aggregatestabilitymaskssubstantialoccupationalmovement. BetweenWave1andWave5,41.8percentof
occupations move to a different exposure quartile, and 4.4 percent move by two or more quartiles (Online
Appendix Figure B.2 traces SOC major-group rank trajectories across waves, and Online Appendix Table
B.4reportsthewave-pairquartiletransitions).
Thetimingoftheseshiftspointstochangesintheuserbaseratherthangradualimprovementsinmodel
capability. Claude Code launched between Waves 2 and 3, and Claude Projects expanded between Waves 3
and 4. Over the same period, the Computer and Mathematical conversation share rose from 28 percent in
Wave1to36percentinWave3beforesettlingat32percentinWave5,whileOﬀiceandAdministrativeSup-
port moved 6 percentage points in the opposite direction. These movements are more naturally interpreted
as changes in who used the platform and what they used it for than as changes in the underlying capability
rubric. Theyneverthelessentertheexposurescoresthatdownstreamresearchersoftentreatasfixedoccupa-
tionalmeasures.
The implication is that a researcher using Wave 1 obtains a different occupational ranking than a re-
searcher using Wave 5, even though both rely on the same vendor. We interpret this within-platform move-
ment as a special case of equation (3), where𝜓𝑜,𝑝 varies across waves. The movement combines the𝜓
channel, which captures which occupations enter the platform user base, and the𝜃 channel, which captures
which tasks users perform within occupations. Section III.F separates these channels empirically, and Ap-
pendixTableB.11reportsdiagnosticsonwithin-occupationtask-sharestability.
E. Workforce Reweighting and Occupational Rankings
If platform representation is the source of the divergence, removing it should change which occupations
appearmostexposed. Thereweightedexposuremeasure, ̃𝐸𝑜,𝑝 ≡ 𝐸 𝑜,𝑝/𝜓𝑜,𝑝,rescaleseachoccupationfrom
its platform share to its workforce share, as defined in Section I. For the composite measure, the correction
preserves the rubric and task-time content but evaluates that content over the workforce rather than over
platform users. For a pure platform-share measure, the same correction collapses the measure to workforce
12

employmentdensity.
The raw and reweighted composites correlate at 0.78 across six-digit SOC codes, suggesting moderate
agreement in the full ranking. The economically relevant changes, however, occur at the top of the distri-
bution. The raw ranking places statistical assistants, computer programmers, and actuaries among the most
exposedoccupations. Afterreweighting,thetopoccupationsbecomecustomerservicerepresentatives,oﬀice
clerks, and cashiers, which are large occupations in the workforce but relatively rare in platform conversa-
tions. OnlineAppendixFigureB.5tracesthesemovementsoccupationbyoccupation. StatisticalAssistants
fall 340 ranks after reweighting, while Customer Service Representatives rise 145 ranks and Oﬀice Clerks
rise132ranks.
The rank reversals change the interpretation of the exposure measure. The raw ranking concentrates AI
exposureinhigh-skill,high-wagework,whilethereweightedrankingshiftsexposuretowardlarge,mid-skill
service and administrative occupations. The two rankings are not noisy versions of the same object. The
rawmeasuredescribesexposureamongplatformusers,whilethereweightedmeasuredescribesexposurein
theworkforce. Downstreamstudiesthatrelyonasingleplatform-derivedrankingimplicitlychoosebetween
thesepopulations.
The measurement evidence establishes that platform-derived exposure differs from workforce exposure
in levels, over time, and after reweighting. Section III asks whether these differences are large enough to
changedownstreamlabor-marketcoeﬀicients.
III. Downstream Estimates and Bounds
We estimate a standard difference-in-differences specification and vary only the exposure measure. We
then isolate the user-base channel using within-vendor channel substitution and event-study timing. We
apply workforce reweighting and decompose cross-wave variation into the between-occupation and
within-occupation channels. We return to the published cross-occupation specification and construct
partial-identificationbounds.
A. Difference-in-Differences Specification
WeuseaDiDspecificationcommonintheAI-and-laborliteratureasadiagnosticformeasurementinstability.
Equation(7)isdefinedattheoccupationlevel. Forperson 𝑖workinginoccupation 𝑜,state 𝑠,andyear 𝑡,the
DiDspecificationis
𝑦𝑖,𝑜,𝑠,𝑡 = 𝛼 𝑜 + 𝛾𝑠 + 𝛿𝑡 + 𝛽 ⋅ (𝐸 (𝑝) 𝑜 ×Post𝑡) + 𝑋 ′ 𝑖,𝑜,𝑠,𝑡𝜃 + 𝜀𝑖,𝑜,𝑠,𝑡 (7)
13

where 𝑦𝑖,𝑜,𝑠,𝑡 is the labor-market outcome (binary employment in the main specification),𝐸(𝑝) 𝑜 is the
platform-derivedexposuremeasureforoccupation 𝑜underplatform 𝑝, 𝑃 𝑜𝑠𝑡𝑡 equalsonefor2023and2024
with 2022 treated as a pre-period year,𝛼𝑜 is a six-digit SOC fixed effect,𝛾𝑠 is a state fixed effect,𝛿𝑡 is a
year fixed effect, and𝑋𝑖,𝑜,𝑠,𝑡 includes the demographic controls. Regressions are weighted by ACS person
weightsandstandarderrorsareclusteredatthestatelevel.
Equation(4)givestheprobabilitylimitfortheDiDcoeﬀicientandforthelevelregressionin(1),because
𝐸(𝑝) 𝑜 × 𝑃 𝑜𝑠𝑡 𝑡 = 𝜓 𝑜(𝐸𝑜 × 𝑃 𝑜𝑠𝑡 𝑡) + (𝜂 𝑜 + 𝑢 𝑜) × 𝑃 𝑜𝑠𝑡 𝑡 and the scaling by𝜓𝑜 is the same in both.
Paralleltrendsarenotneededforthedispersiontobeinformative. Cross-platformvariationinthepost-2022
coeﬀicient and in pre-period behavior both trace to the user-base channel, and both show that the regressor
isnotafixedoccupationalcharacteristic.
Theeventstudyreplacesthepostindicatorwithyear-by-treatmentinteractions,
𝑦𝑖,𝑜,𝑠,𝑡 = 𝛼 𝑜 + 𝛾𝑠 + 𝛿𝑡 + ∑
𝑘≠2022
𝛽𝑘 (𝐸𝑜,𝑝 × 1{𝑡 = 𝑘}) + 𝑋 ′ 𝑖,𝑜,𝑠,𝑡𝜃 + 𝜀𝑖,𝑜,𝑠,𝑡 (8)
with 2022 as the reference year. The pre-period coeﬀicients test for differential trends across high- and
low-exposure occupations through a Granger-style joint Wald𝐹-test, and the post-period coeﬀicients trace
thetimingofthepost-2022differential.
To make coeﬀicients comparable, we z-score each𝐸(𝑝) 𝑜 within the analytic sample using ACS person
weights before estimation. Each measure then runs through the same sample, controls, and estimator, and
theonlythingthatchangesacrosscolumnsistheper-occupationexposurescore.
B. Cross-Platform Dispersion
The downstream coeﬀicients inherit the platform source used to construct exposure. Table 3 reports the
post-2022coeﬀicientsforemployment,labor-forceparticipation,andlogweeklywages,withonecolumnfor
each exposure measure (Online Appendix Table B.6 reports the full coeﬀicient grid). The ten employment
coeﬀicients are uniformly negative, but their magnitudes differ by a factor of 1.9. Under the composite,
a one-standard-deviation increase in exposure lowers employment by 0.14 percentage points, near the per-
thousand-robots effect inAcemoglu and Restrepo (2020)and about one quarter of the youth-employment
effect inBrynjolfsson, Chandar, and Chen (2025). The estimate is economically plausible. The problem is
thatitsmagnitudedependsonwhichplatformsuppliestheconversationshares.
ThesamepatternappearswithintheClaude.aiconsumerchannelovertime. Thecoeﬀicientrisesmono-
tonicallyacrossthefivewaves,mostsharplybetweenWaves3and5,whenClaudeCodeadoptionaccelerated
andtheenterprisebaseexpanded. TheWave5estimateof0.22percentagepointsisnearlytwicetheWave1
14

estimate of 0.12 percentage points, although the regressions differ only in the date of the conversation data.
IntheframeworkofSectionI,thestructuralcoeﬀicientandtrueexposureareheldfixedacrosstheseregres-
sions. Thecoeﬀicientmovesbecausetheslopeoftheplatformproxyontrueexposurechangeswiththeuser
base.
This dispersion is not sampling noise. A Cochran Q test rejects a common coeﬀicient across the ten
measuresonlabor-forceparticipationandwages,andnearlysoonemployment. Pairwisecontrastsseparate
the platforms at the extremes. The measures also bear little relation to what workers themselves report.
Whenwecorrelateeachagainsttheat-workAIuserateinthe Bick,Blandin,andDeming(2026) survey,the
correlationstayslowthroughout. Eventheplatformclosesttotheworkforcestandswellapartfromreported
use,andfartherfromtrueexposure.
C. Within-Vendor Channel Substitution and Event-Study Timing
To isolate the mechanism, we compare two channels of the same platform. The Claude.ai consumer and
enterprise API channels run on the same model in the same wave and differ only in which workers reach
Claude through each. Table 3 Panel B reports the comparison across Waves 3 through 5 under the compos-
ite. At every observed wave, the consumer and enterprise coeﬀicients carry opposite signs. The consumer
channel produces negative and significant coeﬀicients, while the enterprise channel produces positive and
insignificantcoeﬀicients.
Thiswithin-vendorsignreversalisdiﬀiculttoattributetochat-to-taskclassificationerror. Bothmeasures
use the same Clio classifier applied to the same Claude model family and rubric. Any over-attribution in
mapping conversations to tasks, including the type of error emphasized byBick, Blandin, Deming, and
Schumacher(2026),shouldaffecttheconsumerandenterprisemeasuressimilarly. Thesignreversaltherefore
points to the input the two channels do not share: their user base. We trace the difference to occupational
composition,sincetheenterprisechannelconcentratesmoreheavilyinoccupationsratedashighlyapplicable
bythe Eloundouetal. (2024) rubric,andthedownstreamcoeﬀicientinheritsthatcomposition.
The timing of the coeﬀicients helps distinguish measurement instability from treatment-effect hetero-
geneity. A competing interpretation is that the dispersion reflects real differences in how AI affected the
occupations emphasized by different platforms. Figure 3 weighs against that interpretation. The year-by-
year interaction coeﬀicients from equation (8) are close to zero between 2015 and 2020 across the seven
exposure variants. Granger-style joint Wald tests of the pre-treatment interactions yield F-statistics ranging
from0.34to2.18,withthelargestp-valueat0.21. Noneofthesevenspecificationsrejectsparalleltrendsat
the5percentlevel. Theexposurevariantsthenseparatesharplyin2023andremainapartthereafter.
15

Thetimingisinformativebecausegenuinepost-ChatGPTtreatmentheterogeneitywouldbeexpectedto
emergeasworkers,firms,andplatformusersadjustedtothenewtechnology. Instead,theseparationappears
at the onset of the post period and persists. That pattern is more consistent with measurement bias loading
on time-invariant differences in platform user composition than with treatment effects that evolve gradually
after 2022. We therefore interpret the event study as a diagnostic for the user-base channel, not as evidence
thatcross-measuredispersionisinnocuous.
The framework also predicts which variants should exhibit clean pre-period behavior. When𝜓𝑜,𝑝 is
stable, the pre-period coeﬀicients should be close to zero. This is true by construction for the workforce-
reweighted composite and empirically for adjacent Anthropic waves, whose cross-wave rank correlations
exceed 0.95. By contrast, when𝜓𝑜,𝑝 changes during the pre-period as in variants spanning the Claude
Codelaunchorsimilarproducttransitions,thepre-periodcoeﬀicientscandifferfromzero. Weinterpretthe
asymmetric rejection in the full ten-measure test reported in Section V and Table B.8 as evidence of this
mechanism.
D. Subgroup Heterogeneity
Online Appendix Figure B.6 reports DiD coeﬀicients for fifteen demographic and occupation subgroups
under five platform-derived exposure measures, totaling 75 cells (Online Appendix Table B.7 reports the
same coeﬀicients in tabular form). The composite produces a statistically significant negative coeﬀicient
in nine of fifteen subgroups, the Claude.ai consumer channel produces eight significant negatives, and the
enterpriseAPIchannelproducesthreesignificantpositivesandfoursignificantnegatives. Signdisagreement
across measures is most pronounced for three subgroups, with the coeﬀicient on workers with disabilities
positive under Claude.ai consumer and negative under the composite, the coeﬀicient on workers under age
25positiveunderthecompositeandnegativeunderMicrosoftCopilot,andthecoeﬀicientonfemaleworkers
positiveundertheenterpriseAPIandnegativeunderallothermeasures.
Thesubgroupresultsmatterbecausetheappliedliteratureoftenconditionsonasingleplatform-derived
measurewithouttestingsensitivitytoplatformchoice. The75-cellgridshowsthatsubgroupcontrastscanbe
partlydrivenbytheplatformfromwhichexposureisconstructed. Aresearcherstudyingworkerswithdisabil-
ities,forexample,wouldreachoppositeconclusionsunderthecompositeandClaude.aiconsumermeasures.
Thisisthesamefragilitydocumentedintheaggregateestimates,projectedontosubgroupcomparisons.
Thesubgrouppatternraisesasecondconcerndistinctfromcoeﬀicientdispersion. Platformconversation
data observes only workers who use the platform, and workers who do not use the platform are invisible to
thedata,withtheDiDcoeﬀicientforagivensubgroupdependingontwoobjects,thetrueeffectofAIonthat
16

subgroupandthesubgroup’srepresentationintheplatformuserbase. Subgroupslessvisibletotheplatform
entertheregressionthroughtheirworkforceshareratherthanthroughtheiractualAI-usepatterns,andtheir
estimated coeﬀicient inherits the user-base composition of the platform that supplied the exposure score.
Thedisagreementobservedinthedisability,age-under-25,andfemalerowsisthereforeconsistentwithtwo
mechanismsoperatingatoncethattheregressioncannotseparate,trueheterogeneityintheAI-employment
relationshipacrosssubgroupsanddifferentialplatformvisibilityacrossthesamesubgroups.
The distinction matters for policy interpretation because the platform-visible workforce overrepresents
workers with higher income, more education, urban residence, and non-Hispanic ethnicity, and underrepre-
sentsthecorrespondingdisadvantagedsubpopulations(OnlineAppendixFigureB.3plotsoccupationsalong
thejointdimensionsofeconomicvulnerabilityandplatformvisibility). Asubgroupthatisbotheconomically
disadvantaged and underrepresented on the platform sits in the quadrant of Figure B.3 where the DiD coef-
ficientisleastinformativeaboutthetrueeffect,becausetheplatform’sviewofthatsubgroupisconstructed
from a small and likely non-representative sample of its members. Policy rankings that condition on a sin-
gle platform-derived exposure will therefore systematically underweight the populations whose AI-related
labor-marketriskstherankingsareintendedtoidentify.
E. Workforce Reweighting in the DiD Specification
Section I implies that reweighting platform conversation density to match workforce density addresses the
between-occupationcomponentofthebias. Table3reportsthiscorrectionfortwoofthetenexposurevariants.
Forthecompositemeasure,thecoeﬀicientfallsfrom-0.139,significantatthe1percentlevel,to-0.010and
statistically insignificant. This is a 93 percent attenuation. For Microsoft Copilot, the coeﬀicient falls from
-0.191to-0.110. Theattenuationissmaller,at42percent,andtheestimateremainsstatisticallysignificant.
Thedifferencebetweenthetwocorrectionsisinformative. Copilotistheplatform-derivedmeasureclos-
esttoworkforceemployment,withacorrelationof 𝜌=0.33,anditscoeﬀicientmoveslessafterreweighting.
Thecompositeliesfartherfromtheworkforceandattenuatesmore. Thisorderingisexactlywhattheframe-
workpredicts. Thefarthertheplatform’susersarefromtheworkforce,themoreofthecoeﬀicientshouldbe
attributabletothebetween-occupationuser-basecomponent.
WeusethebaselineandreweightedcompositeestimatestoboundtheemploymentelasticityintheDiD
setting. A one-standard-deviation increase in exposure is associated with an employment decline between
0.01and0.14percentagepointsunderthemaintainedorderingcondition. Thewidthoftheintervalmeasures
the contribution of observable platform composition to the baseline coeﬀicient. In this case, the baseline
estimateisalmostentirelydrivenbythecomponentremovedbyworkforcereweighting.
17

F. Decomposing Cross-Wave Variation into the 𝜓 and 𝜃 Channels
The within-platform movement can arise from two sources. Product changes may alter which occupations
entertheplatformuserbase,capturedby 𝜓,ortheymayalterwhichtasksusersperformwithinoccupations,
capturedby 𝜃. Reweightingseparatesthesechannelsbecauseitremovesthebetween-occupationcomponent
whileleavinganywithin-occupationtask-selectionresidual.
We implement this decomposition by taking each Anthropic Economic Index wave in turn, substitut-
ing that wave’s conversation share into theMassenkoff and McCrory (2026)composite, and re-estimating
the DiD models for employment, labor-force participation, and log wages. We then repeat the exercise af-
ter reweighting the composite to match workforce density. Any cross-wave variation that disappears after
reweightingisattributabletoshiftsinoccupationalrepresentation. Anyvariationthatremainsreflectswithin-
occupationtaskselectionorresidualclassificationdifferences.
Table 4 reports the decomposition. Reweighting closes 51 percent of the cross-wave span in the em-
ployment coeﬀicient, 15 percent in labor-force participation, and 32 percent in log wages. The remaining
variation is the part not explained by shifts in occupational representation. This residual is consistent with
within-occupation task selection and classification differences that reweighting cannot remove. Appendix
TableB.11providesdiagnosticsonwithin-occupationtask-sharestability.
The between-occupation channel is also visible in worker-reported use. The framework predicts that
occupations overrepresented in platform data should be occupations where workers report greater at-work
AI use. The RPS microdata support this prediction. Across Claude.ai consumer, Claude enterprise API,
and Microsoft Copilot, the correlation between platform representation and survey-reported at-work AI use
is positive and statistically significant, ranging from 0.25 to 0.39 (Online Appendix Figure B.7 plots the
three measures across SOC majorgroups). Platform data therefore overweightoccupations where AI use is
alreadymorecommon. Thistestdoesnotaddressthewithin-occupationversionofthemaintainedordering
condition,butitconfirmsthatbetween-occupationcompositionisempiricallyrelevant.
G. Cross-Occupation Estimates
The same user-base channel appears in the cross-occupation specification for which the composite measure
was originally proposed.Massenkoff and McCrory (2026)regress each occupation’s BLS-projected em-
ployment growth from 2024 to 2034 on standardized composite exposure, weighted by 2024 OEWS em-
ployment. The coeﬀicient is the change in projected decadal employment growth associated with a one-
standard-deviationincreaseinexposure. Thissettingisusefulbecausethedependentvariable,weights,and
occupationaluniversecanbeheldfixedwhiletheexposuremeasureisreweightedorreplaced.
18

In the published estimate, a one-standard-deviation increase in composite exposure is associated with
projecteddecadalemploymentgrowthlowerby0.70percentagepoints. Weapplytheworkforce-reweighting
operationdirectlytothecomposite,leavingthedependentvariable,weights,andoccupationaluniversefixed.
Figure 4 Panel A shows that the employment-growth differential falls from 0.70 to 0.38 percentage points
afterreweighting. Thedifferenceof0.32percentagepointsmeansthat45percentofthepublishedmagnitude
disappearswhenplatformconversationdensityisreplacedwithworkforcedensity.
The redistribution across major groups follows the same logic. Figure 4 Panel B shows that the largest
downwardshiftsunderreweightingoccurinComputerandMathematical,OﬀiceandAdministrativeSupport,
and Sales occupations, the groups most overrepresented in the platform user base. Reweighting therefore
reducesexposuremostwhereplatformrepresentationdepartsmostfromworkforcerepresentation. Thecross-
occupation attenuation of 45 percent falls within the DiD reweighting range of 42 to 93 percent, indicating
thatthesamechannelappearsinbothempiricalsettings.
We next substitute alternative platform-derived measures into the same between-occupation regression.
Table5PanelBreportsestimatesfromthetenregressionmeasuresandtwobenchmarkdistributions(Online
AppendixTableB.10reportstheparallelsubstitutionacrossfivepublishedapplied-AItargetmethods). The
dependentvariable,employmentweights,andoccupationaluniverseremainfixed. Onlytheoccupation-level
exposure score changes. The substitution moves the estimate across both signs. A one-standard-deviation
increaseinexposureisassociatedwithprojecteddecadalemploymentgrowthlowerby1.50percentagepoints
under Microsoft Copilot and higher by 1.74 percentage points under OpenAI ChatGPT, with the Anthropic
measuresspanningbothsignsacrosswaves. Thisrangedoesnotimplythatthestructuralemploymenteffect
of AI differs across platforms. It shows that the same cross-occupation regression inherits the occupational
compositionoftheplatformusedtoconstructexposure.
We also re-estimate the between-occupation regression using the RPS measure of at-work AI use at
the six-digit SOC level. A one-standard-deviation increase in survey-reported at-work AI use is associated
with projected decadal employment growth higher by 1.67 percentage points, with a standard error of 0.46
percentagepoints. Thisestimateliesnearthepositiveendoftheplatform-derivedrange,closetotheOpenAI
ChatGPT estimate and opposite in sign to the published composite estimate. The mixed signs therefore do
not arise only from platform logs. They also appear when the right-hand-side variable is a survey-based
measureofat-workAIuse. Table5PanelBandAppendixTableB.9reporttheRPSestimatealongsidethe
platform-derivedmeasuresandtheSOC-major-expandedSWAArow.
19

H. Partial-Identification Bounds
We use the baseline composite coeﬀicient and its workforce-reweighted counterpart to construct a partial-
identificationintervalforthestructuralemploymentelasticity. Theintervalreliesonthemaintainedordering
condition stated in Section I and proved in Appendix A.5. Under this condition, the baseline composite
containsboth task exposureand platform selection, while the workforce-reweightedcomposite removesthe
between-occupation selection component. The interval implies that a one-standard-deviation increase in
composite exposure is associated with projected decadal employment growth lower by between 0.38 and
0.70 percentage points. Its width is 0.32 percentage points. This width is the estimated contribution of
between-occupation platform selection to the published coeﬀicient. Equivalently, nearly half of the pub-
lished association disappears when the platform’s occupational composition is replaced with the workforce
composition.
This changes the interpretation of the published estimate. Reporting only the baseline coeﬀicient treats
the0.70percentagepointdeclineasapointestimateofthestructuralemploymentelasticity. Thereweighting
exerciseshowsthatthesamespecificationsupportsasmallerdeclineoncetheplatform’soccupationaldensity
isreplacedwiththeworkforcedensity. Thedatathereforeidentifyarangeofelasticitiesunderthemaintained
orderingconditionratherthanasingleplatform-specificcoeﬀicient.
Thecross-platformsubstitutesinTable5PanelsBandCserveadifferentpurpose. Theyshowhowfarthe
between-occupationestimatemoveswhentheplatformsourcechanges. Theestimatesrangefromprojected
decadal employment growth lower by 1.50 percentage points under Microsoft Copilot to growth higher by
1.74percentagepointsunderOpenAIChatGPT.Thecross-platformspanis3.24percentagepoints,whichis
severaltimeslargerthanthepublishedcompositeestimateitself.
We do not interpret this span as a partial-identification interval because the substitutes are not the same
object as the composite. They enter as raw conversation densities rather than rubric-weighted task aggre-
gates, and their reweighted versions no longer measure AI applicability. We report the span as descriptive
evidencethatthebetween-occupationspecificationishighlysensitivetotheplatformsourceusedtoconstruct
exposure.
The DiD and cross-occupation exercises deliver the same substantive conclusion. In both settings, the
workforce-reweightedestimatereducesthecomponentofthecoeﬀicientdrivenbybetween-occupationplat-
formselection. Thebaselineestimate,bycontrast,dependsonwhichplatformsuppliestheoccupationalex-
posuremeasure. Therelevantempiricalobjectisthereforenotasinglecoeﬀicientfromoneplatform-derived
regressor. Itistherangeofestimatesthatremainsonceplatformselectionismadeexplicit.
This framing follows the taxonomy ofTamer (2010). The bounds are not outcome bounds generated by
20

limitedsamplesize. Theyareselection-mechanismboundsgeneratedbytheunobservedplatform-selection
process. Theintervalcollapsesonlywithanexternalsourceofvariationthatbreaksthedependencebetween
true exposure, platform representation, and within-occupation task selection. In the absence of such an in-
strument,theintervalwidthhasadirecteconomicinterpretation. Itisthepartoftheprojectedemployment-
growthassociationthatdisappearswhentheplatform’soccupationalcompositionisreplacedwiththework-
forcecomposition.
IV. Distributional Incidence
TheresultsinSectionIIIshowthatplatformselectionchangesdownstreamemploymentestimates. Thissec-
tionaskswherethatselectionfallsintheworkforce. Ifplatformrepresentationiscorrelatedwithoccupation-
levelsocioeconomicstatus,thenplatform-derivedexposurecantransmittheuser-basechannelintooutcomes
beyondemploymentandintopolicyrankingsthatdependonmeasuredexposure. Wetestthisimplicationin
threesteps. Wefirstcompareplatformandworkforcerankingsagainstadditionaloccupation-leveloutcomes.
We then describe the demographic composition of the platform-visible workforce. We finally examine how
populationweightingchangesaretrainingallocationbasedonthesameexposureconcept.
A. Cross-Domain Outcomes
If platform visibility is correlated with occupational socioeconomic status, the user-base channel should
appear outside the employment regressions. We test this implication using ten occupation-level outcomes
fromtheACSandtheNationalHealthInterviewSurvey. TheACSoutcomescover2011to2022andinclude
hours worked, three education shares, and disability prevalence. The NHIS Sample Adult outcomes cover
2017and2018andincludetheKessler-6distressscore,current-smokerprevalence,drinkingbehavior,short-
sleepprevalence,andself-ratedhealth.
The diagnostic compares two occupation rankings. The first ranks occupations by Anthropic Wave 5
Claude.ai consumer conversation share. The second ranks occupations by OEWS workforce employment
share. For each outcome, we compute how strongly the outcome is associated with each ranking and ex-
amine the difference. If platform representation were unrelated to occupational socioeconomic status, the
platformrankingandtheworkforcerankingwouldhavesimilarrelationshipswithwages,education,health,
and distress. A systematic difference means that the platform ranking carries information about the compo-
sitionoftheoccupationsitoverrepresents.
When the three main labor-market outcomes are added to this set, five of the fifteen outcomes show
nominally significant platform-versus-workforce gaps at the 5 percent level. These outcomes are log real
21

hourlywages,Bachelor’s-or-highershare,short-sleepprevalence,current-smokerprevalence,andK6severe-
distressprevalence. Theeconomicpatternistheimportantresult. TheAnthropicconsumerrankingismore
aligned than the workforce ranking with high-wage and high-education occupations. It is less aligned with
occupationsthathavehighersmokingrates,moreshortsleep,andhigherseveredistress. Theexactgapstatis-
tics are largest for log wages, short sleep, current smoking, Bachelor’s-or-higher share, and severe distress,
withallfivesignsinthedirectionpredictedbyplatformselection.
ThispatternmeansthattheplatformrankingdoesnotonlyorderoccupationsbymeasuredAIexposure. It
alsoordersthemalongasocioeconomicgradient. Occupationsthataremorevisibleontheplatformaremore
advantagedonaverage,whileoccupationsthatarelessvisibleontheplatformaremorelikelytohavelower
wages and worse health-related outcomes. This is consistent with the platform overrepresenting Computer
andMathematicaloccupationsandunderrepresentingserviceandmanual-laboroccupations.
We interpret these results as evidence on the pattern of selection rather than as five separate outcome-
specificfindings. Becausewetestfifteenoutcomes,theindividualp-valuesshouldnotbereadasindependent
confirmationforeachoutcome. OnlineAppendixFigureB.1reportsthefamily-wiseandfalse-discovery-rate
adjustments. Under the most conservative interpretation, no single outcome should carry the argument on
its own. The relevant evidence is that the outcomes most tied to occupational socioeconomic status move
in the predicted direction. Wages and education are more strongly aligned with the platform ranking, while
smoking, short sleep, and severe distress are more strongly aligned with occupations underrepresented on
theplatform.
B. Composition of the Platform-Visible Workforce
We next ask which workers are represented when the platform conversation distribution is mapped onto the
workforce. We construct the platform-visible workforce using the Anthropic Wave 5 Claude.ai consumer
conversationdensityatthesix-digitSOClevelandthe2024OEWSemploymentdistributionwithinoccupa-
tions. Thisconstructioncombinesthedemographiccompositionofworkerswithineachoccupationwiththe
platform’s between-occupation density. We then compare the resulting population with the BLS workforce
usingACS2024demographics.
Theplatform-visibleworkforcedifferssystematicallyfromtheU.S.workforce. Itoverrepresentsworkers
in higher-wage occupations and workers with Bachelor’s-or-higher degrees. It underrepresents workers in
occupations with high disability prevalence and high non-Hispanic Black workforce representation (Online
AppendixFigureB.4reportsthefulldemographicprofileofthe95most-populousSOCs). Thedirectionof
thesedifferencesmatchesthecross-domainevidence. Theplatformplacesgreaterweightonoccupationsthat
22

aremoreadvantagedintheworkforceandlessweightonoccupationsthataremoreeconomicallyvulnerable.
This composition clarifies why the cross-domain gaps arise. The platform-visible workforce is tilted
toward high-wage and high-education occupations, and away from lower-wage, disability-prevalent, and
manual-labor occupations. The outcomes with nominally significant platform-workforce gaps are precisely
the outcomes tied to this occupational divide. They include wages, education, health behavior, mental dis-
tress, and sleep. The implication for interpretation is direct. A platform-derived exposure measure is least
informativeforworkersinoccupationsthatarebothweaklyrepresentedontheplatformandmoreeconomi-
callyvulnerableintheworkforce.
Online Appendix Figure B.3 plots occupations by economic vulnerability and platform visibility. The
high-vulnerability, low-visibility quadrant is the key region for interpretation. These occupations are eco-
nomicallyexposedintheworkforcebutweaklyrepresentedinplatformdata. Forthem,theplatform-derived
coeﬀicientisleastinformativeaboutthetrueeffectbecausetheplatformobservesfewworkersandobserves
them selectively. This quadrant disproportionately includes personal-care, food-preparation, and building-
maintenanceoccupations.
C. Allocation Implications
The distributional consequences become concrete when exposure rankings are used for allocation. Online
Appendix C reports a hypothetical ten-billion-dollar retraining-fund simulation (Figure C.1). The exercise
is not a welfare calculation. It holds the budget fixed and asks how the allocation changes when the same
exposureconceptisweightedbyplatformvisibilityratherthanworkforcerepresentation.
The platform-weighted rule directs 3.87 billion dollars to occupations with above-median wages and
Bachelor’s-or-higher shares above 60 percent. Under the workforce-weighted rule, the same dollars shift
toward middle-wage occupations whose Bachelor’s-or-higher shares are closer to the workforce mean. The
differencebetweenthetworulesisthereforenotonlyatechnicalchangeinweights. Itchangeswhichworkers
are treated as exposed. Platform weighting shifts resources toward occupations already visible in AI data,
whileworkforceweightingshifts resources towardlargerworkforceoccupations that are less represented in
platformconversations.
The exercise illustrates the policy relevance of the measurement problem. Exposure rankings are often
interpreted as rankings of labor-market risk. When those rankings are built from selected platform use,
low platform visibility can be mistaken for low exposure. Yet low visibility may reflect limited access, low
adoption, or the absence of workers whose tasks have already been displaced. For policy purposes, the
relevant population is not only current platform users. It is the workforce facing adjustment costs as AI
23

changestaskdemand.
D. Implications for Cross-Domain Applied Work
The cross-domain and composition results imply that platform-derived AI exposure can transmit user-base
selection into any occupation-level outcome correlated with socioeconomic status. This concern extends
beyond employment. Wages, education, disability prevalence, mental health, sleep, and smoking all vary
systematicallyacrossoccupations. Severaloftheseoutcomesalsoaligndifferentlywithplatform-basedand
workforce-basedrankings.
The implication for applied work is methodological. A regression that treats platform-derived exposure
asafixedoccupationalcharacteristicmayrecoverpartoftheplatformuser-basechannelratherthanonlythe
structuralrelationshipbetweenAIexposureandtheoutcome. Theconcernisstrongestwhentheoutcomeis
correlatedwith 𝜓𝑜,𝑝,sincetheexposuremeasurethenembedsboththeplatform’soccupationalcomposition
andtheoutcome’ssocioeconomicgradient.
The workforce-reweighting and partial-identification procedure extends directly to this setting. For any
downstreamoutcome,researcherscanreportthebaselinecoeﬀicientandtheworkforce-reweightedcoeﬀicient
as endpoints of an identified set under the maintained ordering condition. The width of the interval gives
the contribution of the user-base channel for that outcome and specification. This procedure does not solve
thewithin-occupationtask-selectionproblem,butitseparatesthecomponentofbiasthatisobservablefrom
workforceandplatformoccupationshares.
V. Robustness
The preceding sections show that platform-derived exposure measures differ from workforce exposure and
thatthisdifferencecarriesintodownstreamcoeﬀicients. Wenowaskwhetherthecoeﬀicientdispersioncan
beexplainedbystandardspecificationchoicesratherthanbytheuser-basechannel. Acrosstheexercises,we
holdfixedtheanalyticsampleandthetenexposuremeasures,thenvaryonefeatureoftheempiricaldesign.
The statistic we track is the spread in the post-2022 coeﬀicient across exposure measures. In the baseline
employmentspecification,thelargestabsolutecoeﬀicientis1.9timesthesmallest.
A natural concern is that the post-2022 dispersion reflects differential pre-period trends rather than plat-
formselection. Weestimatetheevent-studyspecificationinequation(8)foreachexposuremeasureandtest
thesevenpre-periodinteractionsfrom2015through2021,with2022omitted. Sixofthetenmeasuresreject
thezero-pre-trendnullatthe5percentlevel. Thispatternisconsistentwiththeframework. Theexposurere-
gressorpartlyreflectstheplatformuserbase,andplatformrepresentationiscorrelatedwithoccupation-level
24

trendsthatpredatethebroaddiffusionofgenerativeAI.Therelevantquestioniswhetherthecross-platform
dispersiondependsonthepandemicyearsoronthechoiceof2022asthereferenceyear. Itdoesnot. When
wedrop2020and2021andnormalizetheeventstudyto2019,thedispersionratiois1.8,nearlyidenticalto
thebaselineratioof1.9.
The dispersion also appears beyond the employment margin. Table 3 reports the same exercise for em-
ployment,labor-forceparticipation,andlogweeklywages. Thecross-platformrangeis1.9foremployment,
2.5 for labor-force participation, and 3.7 for log weekly wages. These margins need not move in the same
direction, since AI exposure can affect employment, participation, and wages through different adjustment
mechanisms. The relevant result is that platform choice generates substantial dispersion for each outcome.
Theinstabilityisthereforeattachedtotheexposuremeasureratherthantoaparticularlabor-marketoutcome.
One might also worry that the full ACS sample combines workers whose platform visibility and labor-
market responses differ in ways that mechanically widen the coeﬀicient range. We address this by re-
estimatingthespecificationforprime-ageworkers,non-Hispanicwhiteworkers,andwomen. Thedispersion
ratios are 1.8, 2.1, and 2.0, close to the full-sample ratio of 1.9. These subsamples change the demographic
composition of the estimating sample while leaving the exposure measures unchanged. The dispersion re-
mains,anditisatleastaslargeingroupsclosertotheplatform-visibleworkforce. Thatpatternisconsistent
withtheuser-basechannelratherthanwithanidiosyncrasyofthefullsample.
A further possibility is that the coeﬀicient range reflects the way the regression absorbs occupation, ge-
ography, and demographics. We estimate five versions of the model. The baseline includes year, state, and
six-digitoccupationfixedeffectswithdemographiccontrols. Wethendropdemographiccontrols,dropstate
fixed effects, replace six-digit occupation fixed effects with two-digit SOC major-group fixed effects, and
add state-by-year interactions. Across these specifications, the dispersion ratio ranges from 1.7 to 2.1. The
levels of the estimates change, as expected when the identifying comparisons change. The cross-platform
spreaddoesnot. Theresultisnotanartifactofonecontrolsetoronefixed-effectstructure.
Thesamelogicappliestothecapabilityrubricembeddedinthecomposite. Iftheinstabilityweredriven
mainlybythe Eloundouetal. (2024) rubric,replacingthatrubricshouldmateriallyreducethecross-platform
range. Wetestthisbysubstitutingthe Felten,Raj,andSeamans(2021) AIoccupational-impactscore,which
isconstructeddifferentlyandhasarankcorrelationof0.74withtheEloundourubricacrossoccupations. The
cross-platformdispersionratioremains1.8. Changingthecapabilitymeasurechangesthelevelofexposure,
butitdoesnotremovetheplatform-compositioncomponentembeddedintheconversationshares.
Because our preferred specification clusters standard errors by state, we also check whether inference
with a moderate number of clusters affects the conclusions. The baseline specification has 51 clusters, in-
25

cluding the District of Columbia. We re-estimate the preferred specification using wild-cluster bootstrap
confidence intervals with 999 replications. The confidence intervals for the composite and the Anthropic
Wave 5 Claude.ai consumer coeﬀicient are substantively unchanged. The within-Anthropic sign disagree-
mentisthereforenotaproductofconventionalcluster-robustinference.
The remaining concern is that the within-Anthropic time pattern may reflect model changes rather than
changes in the user base. Adjacent-wave comparisons help separate these forces. The Wave 4 to Wave
5 transition is close to a model-refresh comparison. It spans three months, has no major product launch,
and leaves the occupational ranking almost unchanged, with a rank correlation of 0.98. The employment
coeﬀicientchangesbyonly0.008. TheWave2toWave3transitionisdifferent. ItcoincideswiththeClaude
CodelaunchandtheSonnet4update,achangelikelytoshiftbothcapabilitiesandtheoccupationsusingthe
platform. The occupational ranking becomes less stable, with the rank correlation falling to 0.92, and the
coeﬀicientchangesby0.031. Theeconomicmagnitudeisthereforeaboutfourtimeslargerwhenthetransition
includesaproductchangelikelytoaltertheuserbase. Thiscomparisondoesnotruleoutamodelcontribution,
butitshowsthatmostofthewithin-platformmovementoccurswhentheplatform’soccupationalcomposition
ismostlikelytochange.
Takentogether,therobustnessexercisesnarrowthesetofplausibleexplanations(OnlineAppendixTable
B.5 summarizes significance counts across the seven dimensions). The cross-platform dispersion remains
when we change the reference year, the outcome, the sample, the controls, the fixed effects, the capability
rubric, and the inference method. It also remains after bounding the role of adjacent model changes. The
common element across the exercises is the platform-derived exposure measure. The evidence therefore
supportstheinterpretationthatcoeﬀicientdispersionisafeatureofplatform-basedmeasurementratherthan
aconsequenceofasingleregressionchoice.
VI. Conclusion
Platform conversation logs have moved occupational AI exposure measures closer to observed use, but the
move changes the interpretation of the measure. A measure built from platform conversations does more
than summarize which tasks AI can perform. It also weights those tasks by the occupations that appear
on a particular platform. When platform representation is correlated with occupational task structure, the
resulting error is non-classical and the coeﬀicient inherits the platform source used to construct exposure,
evenwhentheregressiondesignisheldfixed.
The framework separates what current data can correct from what remains unidentified. The between-
occupation gap between platform conversation shares and workforce employment shares is observed, and
26

workforce reweighting removes that component under the maintained ordering condition. The remaining
within-occupation task-selection residual cannot be removed without worker-task data measured on a com-
mon taxonomy. The baseline and workforce-reweighted coeﬀicients therefore define a partial-identification
intervalforthestructuralemploymentelasticity. Theintervalisnotacausalestimate. Itsroleistoshowhow
muchofthecoeﬀicientissupportedoncetheobservableplatform-compositioncomponentisremoved.
The same logic clarifies why observed use should not be interpreted as displacement. Platform conver-
sations are generated by workers and tasks that remain visible in the occupation-platform pair. They do not
recover nonusers, infrequent users, or workers and tasks that leave that pair. Reweighting corrects occupa-
tionalcomposition,butitdoesnotrecovertheshareofworkertasktimeperformedbyAI,theproductivityof
thatuse,orthelabor-demandresponsewhentaskcostsfall. Employmentandwageeffectsthereforerequire
adoptionandusemeasuresinaworkforceframe,togetherwithcrediblevariationinexposureoradoption.
The policy implication is not that exposure rankings should be discarded. It is that rankings built from
selectedplatformuseshouldnotbetreatedasrankingsofworkforcerisk. Retrainingfunds,careeradvising,
curriculuminvestment,andworkforceplanningallrequirejudgmentsaboutwhereadjustmentcostsarelikely
to arise. If platform visibility is correlated with wages, education, and occupational advantage, a platform-
weighted ranking can direct attention toward occupations where AI use is easy to observe and away from
occupationswhereriskislessvisibleinplatformdata. Fortheseuses,therelevantobjectisexposureamong
theworkforceatrisk,notexposureamongcurrentplatformusers.
The value of platform logs is that they observe task use at a scale and frequency unavailable in surveys
oradministrativerecords. Thelimitationisthatscaledoesnotchangethepopulationrepresentedinthedata.
Additional conversations can make a platform-specific exposure measure more precise without making it
workforcerepresentative. Thenextempiricalstepisthereforetolinkplatformlogstoworker-representative
adoption measures, task-time data, and research designs that distinguish exposure, adoption, use, and dis-
placement. Withoutthatlink,estimatesofAIexposuremaycontinuetomeasuretheplatform’soccupational
compositionasmuchasthelabor-marketexposuretheliteratureseekstoexplain.
27

Tables
28

Table 1. Analytical Sample and Exposure Measures
Panel A. American Community Survey analytic sample versus full sample (2015 to 2024, ages 16 to 64)
Variable Analytic mean Analytic SD Full ACS mean Full ACS SD Diff SMD
Employed 0.844 0.363 0.844 0.363 -0.000 -0.000
Age 39.169 13.467 39.649 13.461 -0.480 -0.036
Female 0.507 0.500 0.5 0.5 +0.007 +0.014
Bachelor'sorhigher 0.335 0.472 0.308 0.462 +0.027 +0.057
Married 0.474 0.499 0.481 0.5 -0.007 -0.014
Adultswithdisability 0.075 0.264 0.076 0.265 -0.001 -0.003
Non-Hispanicwhite 0.591 0.492 0.596 0.491 -0.005 -0.009
Non-HispanicBlack 0.125 0.331 0.115 0.319 +0.010 +0.031
Hispanic 0.182 0.386 0.187 0.39 -0.005 -0.013
Numberofobservations 13,104,072 14,546,824 -1,442,752 -9.9%
Panel B. Ten exposure-measure variants (occupation-level)
Variable Mean SD Min Max
BaselineComposite(Anthropic) 0.076 0.133 0.000 0.745
CompositeReweighted 0.006 0.033 0.000 0.461
Claude.aiWave1 0.100 0.328 0.000 5.912
Claude.aiWave3 0.099 0.354 0.000 5.635
Claude.aiWave5 0.100 0.312 0.000 5.499
1PAPIWave3 0.103 0.474 0.000 10.734
1PAPIWave5 0.101 0.551 0.000 14.218
Copilotraw 0.162 0.096 0.000 0.492
Copilotreweighted 0.163 0.040 0.000 0.479
CompositewithWave5AEIweights 0.067 0.127 0.000 1.070
Panel C. Key benchmark data sources
Source T ype Period Role in analysis
IPUMS-USAACS1-year Householdsurvey 2015to2024 Person-yearoutcomepanel
(𝑁 = 13,104,072)
AnthropicEconomicIndex(Claude.ai+1PAPI) Platformusage Dec2024toFeb2026 Primaryplatformexposuremeasure
(𝑝)
BLSOEWSMay2024 Establishmentsurvey 2024 Workforcedensity 𝑓(𝑜) for 𝜓𝑜,𝑝
BLSEmploymentProjections2024to2034 Administrative 2024to2034 Dependentvariablefor
cross-occupationregression
Real-TimePopulationSurvey( Bick,Blandin,andDeming2026 ) Populationsurvey AugtoNov2024 Independentworker-reportedAIuse
rate
MicrosoftCopilot( Tomlinsonetal. 2025) Platformusage Sept2024 Cross-platformrobustness
comparison
Notes: Panel A reports person-weighted means and standard deviations on the canonical analytical sample (American Community Survey wage-and-salary workers ages 16 to 64, 2015 to 2024)
compared with the full American Community Survey universe of working-age adults. SMD denotes the standardized mean difference between samples. Panel B reports occupation-level descriptive statistics
for the ten artificial-intelligence exposure variants used in the regression analysis (Baseline Composite; Composite Reweighted; Claude.ai consumer Waves 1, 3, and 5; first-party Application Programming
Interface enterprise Waves 3 and 5; Microsoft Copilot raw and reweighted; Composite with Wave 5 AEI weights). Panel C lists the key benchmark data sources entering the analysis. Online Appendix
Table B.1 reports the full variable definitions, the Anthropic Economic Index wave characteristics, the complete data-source inventory, the occupation-crosswalk coverage statistics, and the National Health
Interview Survey cross-domain outcome summary statistics. Abbreviations: SOC = Standard Occupational Classification; AEI = Anthropic Economic Index; API = first-party Application Programming
Interface enterprise; Composite = AI exposure score constructed following Massenkoff and McCrory (2026) ; BLS = Bureau of Labor Statistics; OEWS = Occupational Employment and Wage Statistics;
ACS = American Community Survey.
29

Table 2. Occupational Composition of the Platform-Visible Workforce and the U.S. Workforce
Major group BLS workforce % Claude.ai W5 % 1P API W5 % ChatGPT pct_work†
Microsoft Copilot
score‡ BBD GenAI use %§
Management 7.1 4.3 3.4 50.0 0.135 45.2
BusinessandFinancial 6.7 4.8 3.5 50.0 0.235 40.0
ComputerandMathematical 3.4 32.3 51.7 57.0 0.295 47.9
ArchitectureandEngineering 1.7 2.0 1.7 48.0 0.215 26.4
Life,Physical,andSocialScience 0.9 6.3 4.4 48.0 0.189 26.4
CommunityandSocialService 1.7 3.2 0.5 44.0 0.251 23.0
Legal 0.8 0.6 0.2 44.0 0.135 23.0
EducationalInstructionandLibrary 5.8 13.5 3.1 44.0 0.208 33.5
Arts,Design,Entertainment,Sports,Media 1.4 10.4 5.2 44.0 0.243 31.0
HealthcarePractitionersandTechnical 6.2 3.0 1.0 44.0 0.120 30.2
HealthcareSupport 4.8 0.3 0.2 40.0 0.047 11.9
ProtectiveService 2.4 0.4 0.5 40.0 0.123 11.9
FoodPreparationandServing 8.8 0.7 0.1 40.0 0.169 11.9
BuildingandGroundsCleaning 2.9 0.2 0.1 40.0 0.076 11.9
PersonalCareandService 2.0 1.2 0.4 40.0 0.183 11.9
SalesandRelated 8.7 4.9 4.1 40.0 0.292 20.9
OﬀiceandAdministrativeSupport 11.8 9.4 17.6 40.0 0.262 18.5
Farming,Fishing,andForestry 0.3 0.5 0.1 40.0 0.058 n/a
ConstructionandExtraction 4.1 0.2 0.3 40.0 0.074 20.4
Installation,Maintenance,andRepair 3.9 0.7 0.4 40.0 0.104 20.4
Production 5.7 0.7 1.2 40.0 0.107 20.4
TransportationandMaterialMoving 8.9 0.2 0.2 40.0 0.097 20.4
Notes: How to read this table: Columns are grouped by measurement type. BLS workforce % is the population benchmark , the May 2024 Bureau of Labor Statistics Occupational Employment and Wage
Statistics employment share at the 2-digit Standard Occupational Classification major-group level. Claude.ai W5 % and 1P API W5 % are Wave 5 Anthropic Economic Index conversation shares (consumer
Claude.ai and first-party Application Programming Interface enterprise, respectively); these three columns are directly comparable (each sums to 100 percent across the 22 major groups). The remaining
three columns use different unit conventions and should NOT be cross-compared row-by-row to the share columns: † ChatGPT pct_work is the Chatterji et al. (2025) 5-occupation-group distribution
mapped step-wise within parent group (so all rows in the same Chatterji parent group receive an identical value); ‡ Microsoft Copilot score is the Tomlinson et al. (2025) artificial-intelligence applicability
score on a 0-to-1 index (employment-weighted to Standard Occupational Classification major group), not a share; § BBD GenAI use % is the Bick, Blandin, and Deming (2026) Real-Time Population Survey
December 2024 share of workers using generative artificial intelligence at work in the past month, a population survey use rate, not a conversation share. marks BBD values from aggregated occupation
groups (17_19 Architecture/Engineering/Science = 26.4%; 21_23 Legal/Social Services = 23.0%; 31-39 Personal Services (Healthcare Support, Protective, Food Prep, Building/Grounds, Personal Care)
= 11.9%; 47-53 Blue Collar (Construction, Installation, Production, Transportation) = 20.4%), Bick, Blandin, and Deming (2026) collapsed these Standard Occupational Classification major groups in
their published table 2 due to small sample sizes; the same aggregated rate applies to every sub-major within the group. Major group 45 (Farming, Fishing, Forestry) is too small for any reliable BBD
estimate even after aggregation; n/a denotes not surveyed. The systematic over-representation of Computer and Mathematical (15) occupations in platform-visible data (32.3% Claude.ai W5; 51.7% 1P
API W5) relative to the underlying U.S. workforce (3.4% BLS) and the corresponding under-representation of Oﬀice and Administrative Support (43), Sales and Related (41), Food Preparation and Serving
(35), and Transportation and Material Moving (53) are the central composition findings discussed in Section IV.
30

Table 3. Difference-in-Differences Estimates of AI Exposure on Three Labor-Market Outcomes
Panel A. Cross-source DiD on three labor-market outcomes Panel B. Within-vendor channel substitution
Variant Emp. LFP Log wage Variant Emp. LFP Log wage
BaselineComposite(Anthropic) -0.139*** +0.056* -0.355*** ConsumerClaude.ai(W3) -0.087* +0.082* -0.716***
(0.035) (0.032) (0.107) (0.052) (0.041) (0.155)
CompositeReweighted -0.010 +0.028 +0.204 ConsumerClaude.ai(W4) -0.098** +0.094** -0.358***
(0.045) (0.039) (0.131) (0.047) (0.039) (0.126)
Claude.aiconsumer(W1) -0.116*** +0.005 -0.445*** ConsumerClaude.ai(W5) -0.076* +0.094** -0.550***
(0.035) (0.030) (0.099) (0.043) (0.041) (0.129)
Claude.aiconsumer(W3) -0.163*** -0.045 -0.383*** 1PAPIenterprise(W3) +0.015 +0.080 -0.089
(0.033) (0.030) (0.106) (0.058) (0.048) (0.143)
Claude.aiconsumer(W5) -0.222*** -0.126*** -0.322*** 1PAPIenterprise(W4) +0.041 +0.080** +0.051
(0.042) (0.037) (0.109) (0.047) (0.035) (0.113)
1PAPIenterprise(W3) -0.144*** -0.029 -0.141 1PAPIenterprise(W5) +0.055 +0.115*** -0.204
(0.035) (0.031) (0.089) (0.044) (0.037) (0.128)
1PAPIenterprise(W5) -0.152*** -0.032 -0.165* PooledW3(Claude.ai+1PAPI) -0.064 +0.074* -0.392***
(0.033) (0.030) (0.085) (0.046) (0.039) (0.142)
MicrosoftCopilot(raw) -0.191*** -0.028 +0.009 PooledW4(Claude.ai+1PAPI) -0.098** +0.059* -0.422***
(0.042) (0.036) (0.100) (0.038) (0.032) (0.135)
MicrosoftCopilot(reweighted) -0.110*** +0.026 -0.681*** PooledW5(Claude.ai+1PAPI) -0.039 +0.089*** -0.492***
(0.039) (0.034) (0.073) (0.038) (0.033) (0.135)
CompositewithWave5AEIweights -0.155*** +0.049 -0.752***
(0.031) (0.031) (0.119)
N (range across variants) 8,630,961 to
12,279,674
8,630,961 to
12,279,674
7,862,841 to
11,181,713
N (range across variants) 4,498,101 to
6,172,181
4,498,101 to
6,172,181
4,139,500 to
5,662,442
Notes: Each cell reports a beta-times-100 coeﬀicient with the cluster-robust standard error in parentheses below. Individual-level weighted least squares on the canonical American Community Survey
analytical sample (wage-and-salary workers, ages 16 to 64, 2015 to 2024); two-way fixed effects on year, state, and 6-digit Standard Occupational Classification 2018; controls for sex, marital status, three
educational-attainment indicators, age, age squared, number of own children. Exposure z-scored within sample using employment-weighted means; person-weighted by perwt; standard errors clustered
on state (51 states including the District of Columbia). Post-treatment indicator = 1 if year is 2023 or later. Panel A: cross-source dispersion across ten platform-input variants on three labor-market
outcomes (binary employment, labor-force participation, log weekly wage conditional on positive earnings). Panel B: within-vendor channel substitution under the Baseline Composite (Anthropic) recipe
at Anthropic Economic Index Waves 3, 4, and 5 across three channels (Claude.ai consumer, first-party Application Programming Interface enterprise, pooled). Each panel's last row reports the range of
person-year observations across variants per outcome. Robustness to dropping 2020 and 2021 (COVID-19 disruption years) is reported in Online Appendix Table B.6. *** p<0.01, ** p<0.05, * p<0.10.
31

Table 4. Wave-by-Wave Reweighted Composite Difference-in-Differences as a𝜓 versus 𝜃 Channel Diagnostic
Wave (release) Employment LFP Log wage Baseline Reweighted Baseline Reweighted Baseline Reweighted
W1(Dec2024) -0.113*** -0.014 +0.049* +0.001 -0.478*** +0.135***
(0.027) (0.012) (0.028) (0.011) (0.091) (0.040)
W2(Feb2025) -0.120*** -0.017 +0.047* +0.002 -0.605*** +0.104***
(0.028) (0.013) (0.029) (0.012) (0.098) (0.038)
W3(Aug2025) -0.110*** -0.009 +0.047* +0.003 -0.492*** +0.076**
(0.026) (0.009) (0.027) (0.008) (0.090) (0.030)
W4(Nov2025) -0.091*** -0.003 +0.047** -0.000 -0.462*** +0.100***
(0.026) (0.013) (0.024) (0.011) (0.085) (0.036)
W5(Feb2026) -0.083*** -0.021* +0.054** -0.002 -0.478*** +0.038
(0.024) (0.012) (0.023) (0.011) (0.082) (0.035)
Cross-wave span 0.037 0.018 0.007 0.006 0.143 0.097
Span ratio 0.49 0.85 0.68
Notes: For each Anthropic Economic Index wave we substitute that wave's conversation share into the Massenkoff and McCrory (2026) composite formula (rubric × task-time × within-occupation
task share) and re-estimate the DiD on each labor-market outcome. The baseline block uses the resulting composite directly; the workforce-reweighted block multiplies by 𝑓BLS/𝑓 (𝑤) 𝑝 , where 𝑓(𝑤) 𝑝 is the
wave-𝑤 cross-occupation conversation density. Coeﬀicients report 𝛽 × 100 per standard deviation with cluster-robust standard errors clustered at the state level in parentheses on the row beneath, from
individual-level weighted least squares on the 2015 to 2024 American Community Survey panel (13.1 million person-year observations) with six-digit Standard Occupational Classification, state, and year
fixed effects and the demographic controls of Section II.D. Cross-wave span is the maximum minus minimum coeﬀicient across the five waves for each outcome × specification combination; the span ratio
is the reweighted span divided by the baseline span. A span ratio near zero indicates that the cross-occupation user-base channel ( 𝜓) accounts for most of the cross-wave coeﬀicient variation; a span ratio
near one would indicate that within-occupation behavior change (𝜃) is the central source. Supporting diagnostic evidence on 𝜓 and 𝜃 is reported in Table B.11. Significance levels: * p < 0.10, ** p < 0.05,
*** p < 0.01.
32

Table 5. Replication of Massenkoff and McCrory (2026) Composite Construction and Workforce Reweighting
Exposure measure N Original BLS-reweighted Attenuation in |Coef|
PanelA.Massenkoff-McCrorybaselinecompositereweightingtest
M-Mbaselinecomposite(Massenkoff-McCrory2026) 756/766 -70.09*** -38.28** 45.4%
(17.90) (17.35)
PanelB.Alternative-rubricandalternative-platformexposures(unreweighted;reweighted
versionsinOnlineAppendixTableB.9)
AnthropicClaude.aiconsumerWave1(Dec2024) 582 +43.30
(33.64)
AnthropicClaude.aiconsumerWave2(Feb2025) 579 -8.16
(34.23)
AnthropicClaude.aiconsumerWave3(Aug2025) 538 -12.10
(35.08)
AnthropicClaude.aiconsumerWave4(Nov2025) 559 -28.12
(33.46)
AnthropicClaude.aiconsumerWave5(Feb2026) 561 -68.01**
(28.80)
Anthropic1PAPIenterpriseWave3(Aug2025) 480 +27.61
(37.16)
Anthropic1PAPIenterpriseWave4(Nov2025) 485 +23.88
(36.38)
Anthropic1PAPIenterpriseWave5(Feb2026) 480 +34.00
(36.03)
MicrosoftBingCopilot2024( Tomlinsonetal. 2025) 785 -150.04***
(24.00)
OpenAIChatGPT2024( Chatterjietal. 2025 ,SOC-major-expanded) 1112 +174.00***
(13.61)
Bick,Blandin,andDeming(2026) ,SWAASOC-major-expanded 1091 +102.26***
(13.28)
Bick,Blandin,andDeming(2026) ,RPSsix-digitSOCmicro 270 +166.81***
(45.80)
Manskipartial-identificationboundson|CoefperSD|(x100)
Lowerbound: M-Mbaselinecomposite,BLS-reweighted 38.28
Upperbound: OpenAIChatGPT2024( Chatterjietal. 2025 ,SOC-major-expanded) 174.00
Identified-setwidth 135.72
Notes: Panel A reports the Massenkoff and McCrory (2026) baseline composite and its workforce-reweighted version. Panel B reports alternative-platform and alternative-rubric exposures, un-
reweighted, in the same between-occupation specification. Two Bick, Blandin, and Deming (2026) rows appear in Panel B for methodological comparison. The BBD-SWAA row uses the SOC-major-
aggregated public release expanded to NEM (n = 1,091). The BBD-RPS six-digit micro row uses the early-2026 micro release at the native six-digit SOC level (n = 270). The RPS is a national online
survey fielded on Qualtrics with awareness-adjusted demographic weights, not a probability sample of the U.S. workforce. Coeﬀicients are scaled per standard deviation of the exposure measure times 100.
Employment-weighted standard errors in parentheses. *** p<0.01, ** p<0.05, * p<0.10.
33

Figures
34

Figure 1. Pairwise Spearman rank correlations across eleven occupational AI-exposure measures
and the BLS workforce.
          
          
          
          
          
          
          
          
          
          
          
          
&ODXGH:DYH
'HF

&ODXGH:DYH
)HE

&ODXGH:DYH
$XJ

&ODXGH:DYH
1RY

&ODXGH:DYH
)HE

$QWKURSLF
3$3,:
$QWKURSLF
3$3,:
$QWKURSLF
3$3,:
0LFURVRIW
%LQJ&RSLORW
2SHQ$,
&KDW*37
%%'SRSXODWLRQ
VXUYH\
%/6
HPSOR\PHQW
&ODXGH:DYH'HF

&ODXGH:DYH)HE

&ODXGH:DYH$XJ

&ODXGH:DYH1RY

&ODXGH:DYH)HE

$QWKURSLF3$3,:
$QWKURSLF3$3,:
$QWKURSLF3$3,:
0LFURVRIW%LQJ&RSLORW
2SHQ$,&KDW*37
%%'SRSXODWLRQVXUYH\
%/6HPSOR\PHQW
$QWKURSLFSODWIRUPGDWD
&ODXGHDLZDYHV3$3,ZDYHV

0LFURVRIW
%LQJ&RSLORW
2SHQ$,
&KDW*37
3RSXODWLRQ
VXUYH\
(PSOR\PHQW
FHQVXV
/ RZ 
GLYHUJHQW

+ LJK
DOLJQHG

     
Notes: Each cell reports the Spearman rank correlation between two AI-exposure measures across 22 SOC major occu-
pational groups. The five Anthropic Claude.ai waves plus three Anthropic API waves cluster at correlations above 0.85;
correlations with Microsoft Copilot, OpenAI ChatGPT, and the BBD population survey fall in the 0.43 to 0.79 range. The
red-bordered BLS employment row and column highlight that no platform-derived measure correlates with the workforce
above 𝜌 = 0.33 .
35

Figure 2. Theoretical AI capability versus each platform’s published main exposure measure.
0DQDJHPHQW
%XVLQHVV	ILQDQFH
&RPSXWHU	PDWK
$UFKLWHFWXUH	HQJLQHHULQJ
/LIH	VRFLDOVFLHQFHV
6RFLDOVHUYLFHV
/HJDO
(GXFDWLRQ	OLEUDU\
$UWV	PHGLD
+HDOWKFDUHSUDFWLWLRQHUV
+HDOWKFDUHVXSSRUW
3URWHFWLYHVHUYLFH
)RRG	VHUYLQJ
*URXQGVPDLQWHQDQFH
3HUVRQDOFDUH
6DOHV
2IILFH	DGPLQ
$JULFXOWXUH
&RQVWUXFWLRQ
,QVWDOODWLRQ	UHSDLU
3URGXFWLRQ
7UDQVSRUWDWLRQ





3DQHO$0DVVHQNRII	0F&URU\

RULJLQDOFRPSRVLWHPHDVXUH
0DQDJHPHQW
%XVLQHVV	ILQDQFH
&RPSXWHU	PDWK
$UFKLWHFWXUH	HQJLQHHULQJ
/LIH	VRFLDOVFLHQFHV
6RFLDOVHUYLFHV
/HJDO
(GXFDWLRQ	OLEUDU\
$UWV	PHGLD
+HDOWKFDUHSUDFWLWLRQHUV
+HDOWKFDUHVXSSRUW
3URWHFWLYHVHUYLFH
)RRG	VHUYLQJ
*URXQGVPDLQWHQDQFH
3HUVRQDOFDUH
6DOHV
2IILFH	DGPLQ
$JULFXOWXUH
&RQVWUXFWLRQ
,QVWDOODWLRQ	UHSDLU
3URGXFWLRQ
7UDQVSRUWDWLRQ





3DQHO%$QWKURSLF(FRQRPLF,QGH[

3$3,:DYHVKDUH
0DQDJHPHQW
%XVLQHVV	ILQDQFH
&RPSXWHU	PDWK
$UFKLWHFWXUH	HQJLQHHULQJ
/LIH	VRFLDOVFLHQFHV
6RFLDOVHUYLFHV
/HJDO
(GXFDWLRQ	OLEUDU\
$UWV	PHGLD
+HDOWKFDUHSUDFWLWLRQHUV
+HDOWKFDUHVXSSRUW
3URWHFWLYHVHUYLFH
)RRG	VHUYLQJ
*URXQGVPDLQWHQDQFH
3HUVRQDOFDUH
6DOHV
2IILFH	DGPLQ
$JULFXOWXUH
&RQVWUXFWLRQ
,QVWDOODWLRQ	UHSDLU
3URGXFWLRQ
7UDQVSRUWDWLRQ





3DQHO&0LFURVRIW&RSLORW7RPOLQVRQ

$,DSSOLFDELOLW\VFRUH
7KHRUHWLFDO$,FRYHUDJH(ORXQGRXHWDO*37UXEULF

 2EVHUYHG$,FRYHUDJHSODWIRUPVSHFLILFSXEOLVKHGPHDVXUH

Notes: Three-panel polar visualization. Each panel plots one platform’s published main exposure measure (radial position) against the theoretical capability benchmark
from Eloundou et al. (2024) (angular position), with each point one of the 22 SOC major groups. Panel A reports the Baseline Composite (Anthropic); Panel B the
Anthropic 1P API Wave 5 share; Panel C the Tomlinson Microsoft Copilot AI applicability score.
36

Figure 3. Event-study coeﬀicients on the employment indicator by exposure variant, 2015 to 2024.
−0.6
−0.4
−0.2
0.0
0.2
0.4
0.6
βk × 100
Panel A. Full sample - event-study levels
−0.6
−0.4
−0.2
0.0
0.2
0.4
0.6
βk × 100
Panel B. Excluding 2020-2021 - levels
2016 2018 2020 2022 2024
Calendar year (event time relative to 2022)
−0.6
−0.4
−0.2
0.0
0.2
0.4
βk − βM-M k  (×100)
Panel C. Full sample - deviation from Baseline Composite (Anthropic)
2016 2018 2020 2022 2024
Calendar year (event time relative to 2022)
−0.6
−0.4
−0.2
0.0
0.2
0.4
βk − βM-M k  (×100)
Panel D. Excluding 2020-2021 - deviation from Baseline Composite (Anthropic)
Baseline Composite (Anthropic)
Composite Reweighted
Composite with Wave 5 AEI
Claude.ai W1
Claude.ai W5
1P API W5
Microsoft Copilot
Notes: Year-by-year interaction coeﬀicients on the employment indicator from the event-study extension of the main DiD
specification (equation 6) for seven exposure variants, 2015 to 2024 with 2022 as the reference year. Pre-period coeﬀi-
cients are statistically indistinguishable from zero for all seven variants; post-treatment coeﬀicients diverge immediately
in 2023.
37

Figure 4. Slope attenuation under workforce reweighting in the cross-occupation BLS Projections regression.

 
 
      
$,H[SRVXUH]VWDQGDUGL]HGZLWKLQVDPSOH







%/6SURMHFWHG\HDUHPSOR\PHQWJURZWK

6ORSHDWWHQXDWLRQ
3DQHO$6ORSHDWWHQXDWLRQXQGHUUHZHLJKWLQJELQQHGVFDWWHUELQVHDFK

2ULJLQDO006' 
%/6UHZHLJKWHG6' 
$QFKRUELQVQ 

00B5:ELQVQ 


     
(PSOR\PHQWZHLJKWHGDYHUDJHH[SRVXUH]VFRUH
7UDQVSRUWDWLRQ
3URGXFWLRQ
%XLOGLQJ0DLQWHQDQFH
)RRG3UHSDUDWLRQ
)DUPLQJ)LVKLQJ)RUHVWU\
&RQVWUXFWLRQ
,QVWDOODWLRQ5HSDLU
+HDOWKFDUH6XSSRUW
3HUVRQDO&DUH
3URWHFWLYH6HUYLFH
$UFKLWHFWXUH(QJLQHHULQJ
&RPPXQLW\6RFLDO6HUYLFH
+HDOWKFDUH3UDFWLWLRQHUV
/LIH3K\VLFDO6RFLDO6FLHQFH
0DQDJHPHQW
$UWV'HVLJQ(QWHUWDLQPHQW
(GXFDWLRQ/LEUDU\
/HJDO
6DOHV
%XVLQHVV)LQDQFLDO
2IILFH$GPLQ
&RPSXWHU0DWK












































3DQHO%([SRVXUHUDQNUHGLVWULEXWLRQE\62&PDMRUJURXS
$QFKRU]VFRUH
00B5:]VFRUH
Notes: Panel A is a binned scatter (25 equal-size bins) of BLS-projected 2024 to 2034 employment growth against the standardized composite exposure, with the published
unreweighted slope of −0.70 per standard deviation and the workforce-reweighted slope of −0.38 overlaid. Panel B reports the cross-occupation redistribution at
the SOC major-group level, where the largest negative shifts under reweighting fall on Computer and Mathematical, Oﬀice and Administrative Support, and Sales.
38

References
Acemoglu, Daron, and David Autor. 2011. ”Skills, Tasks and Technologies: Implications for Employment
andEarnings.”In Handbook of Labor Economics,Vol. 4B,editedbyOrleyAshenfelterandDavidCard,
1043–1171. Amsterdam: Elsevier.
Acemoglu, Daron, and Pascual Restrepo. 2020. ”Robots and Jobs: Evidence from US Labor Markets.”
Journal of Political Economy 128(6): 2188–2244.
Appel, Ruth, Peter McCrory, Alex Tamkin, Miles McCain, Tyler Neylon, and Michael Stern. 2025. ”An-
thropicEconomicIndexReport: UnevenGeographicandEnterpriseAIAdoption.”arXiv:2511.15080.
Autor, David H., Frank Levy, and Richard J. Murnane. 2003. ”The Skill Content of Recent Technological
Change: AnEmpiricalExploration.” Quarterly Journal of Economics 118(4): 1279–1333.
Bick, Alexander, Adam Blandin, and David J. Deming. 2026. ”The Rapid Adoption of Generative AI.”
NBERWorkingPaper32966.
Bick, Alexander, Adam Blandin, David J. Deming, and Tyler Schumacher. 2026. ”What Work Does Gener-
ativeAIDo?”FederalReserveBankofSt. LouisWorkingPaper,April27,2026.
Bound,John,CharlesBrown,andNancyMathiowetz. 2001. ”MeasurementErrorinSurveyData.”In Hand-
book of Econometrics,Vol. 5,editedbyJamesJ.HeckmanandEdwardLeamer,3705–3843. Amsterdam:
Elsevier.
Brynjolfsson, Erik, Tom Mitchell, and Daniel Rock. 2018. ”What Can Machines Learn, and What Does It
MeanforOccupationsandtheEconomy?” AEA Papers and Proceedings 108: 43–47.
Brynjolfsson,Erik,DanielleLi,andLindseyR.Raymond. 2023. ”GenerativeAIatWork.”NBERWorking
Paper31161.
Brynjolfsson,Erik,BharatChandar,andRuyuChen. 2025. ”CanariesintheCoalMine? SixFactsaboutthe
RecentEmploymentEffectsofArtificialIntelligence.”StanfordDigitalEconomyLabWorkingPaper.
Chatterji,Aaron,ThomasCunningham,DavidJ.Deming,ZoeHitzig,ChristopherOng,CarlYanShan,and
KevinWadman. 2025. ”HowPeopleUseChatGPT.”NBERWorkingPaper34255.
Chen,Danqing,CarinaKane,AustinKozlowski,NadavKunievsky,andJamesA.Evans. 2025. ”The(Short-
Term)EffectsofLargeLanguageModelsonUnemploymentandEarnings.”arXiv:2509.15510.
Cui, Zheyuan (Kevin), Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, and Tobias Salz. 2024. ”The
39

EffectsofGenerativeAIonHigh-SkilledWork: EvidencefromThreeFieldExperimentswithSoftware
Developers.”SSRNWorkingPaper4945566.
Dell’Acqua, Fabrizio, Edward McFowland III, Ethan R. Mollick, Hila Lifshitz-Assaf, Katherine Kellogg,
SaranRajendran,LisaKrayer,FrançoisCandelon,andKarimR.Lakhani. 2023. ”NavigatingtheJagged
Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowl-
edgeWorkerProductivityandQuality.”HarvardBusinessSchoolWorkingPaper24-013.
Eloundou, Tyna, Sam Manning, Pamela Mishkin, and Daniel Rock. 2024. ”GPTs are GPTs: Labor Market
ImpactPotentialofLLMs.” Science384(6702): 1306–1308.
Felten,EdwardW.,ManavRaj,andRobertSeamans. 2021. ”Occupational,Industry,andGeographicExpo-
sure to Artificial Intelligence: A Novel Dataset and Its Potential Uses.”Strategic Management Journal
42(12): 2195–2217.
Frey,CarlBenedikt,andMichaelA.Osborne. 2017. ”TheFutureofEmployment: HowSusceptibleareJobs
toComputerisation?” Technological Forecasting and Social Change114: 254–280.
Goos, Maarten, Alan Manning, and Anna Salomons. 2014. ”Explaining Job Polarization: Routine-Biased
TechnologicalChangeandOffshoring.” American Economic Review 104(8): 2509–2526.
Handa, Kunal, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah Heck, Jared Mueller, et
al. 2025. ”WhichEconomicTasksarePerformedwithAI?EvidencefromMillionsofClaudeConversa-
tions.”AnthropicTechnicalReport.
Lane, Marguerita, Morgan Williams, and Stijn Broecke. 2023. ”The Impact of AI on the Workplace: Main
Findings from the OECD AI Surveys of Employers and Workers.” OECD Social, Employment and Mi-
grationWorkingPapersNo. 288. Paris: OECDPublishing.
Manski,CharlesF.2003. Partial Identification of Probability Distributions. NewYork: Springer.
Massenkoff, Maxim, and Peter McCrory. 2026. ”Labor Market Impacts of AI: A New Measure and Early
Evidence.”AnthropicResearch,March5.
Meng, Xiao-Li. 2018. ”Statistical Paradises and Paradoxes in Big Data (I): Law of Large Populations, Big
DataParadox,andthe2016USPresidentialElection.” Annals of Applied Statistics 12(2): 685–726.
Noy,Shakked,andWhitneyZhang. 2023. ”ExperimentalEvidenceontheProductivityEffectsofGenerative
ArtificialIntelligence.” Science381(6654): 187–192.
Tamer,Elie. 2010. ”PartialIdentificationinEconometrics.” Annual Review of Economics 2: 167–195.
40

Tamkin, Alex, MilesMcCain, KunalHanda, Esin Durmus, LianeLovitt, Ankur Rathi, SaffronHuang, et al.
2024. ”Clio: Privacy-PreservingInsightsintoReal-WorldAIUse.”AnthropicTechnicalReport.
Tomlinson, Kiran, Sonia Jaffe, Will Wang, Scott Counts, and Siddharth Suri. 2025. ”Working with AI:
Measuring the Applicability of Generative AI to Occupations.” Microsoft Research Technical Report
(arXiv:2507.07935).
U.S.CensusBureau. 2025. ”HouseholdTrendsandOutlookPulseSurvey(HTOPS):Public-UseDataFiles.”
Washington,DC:U.S.DepartmentofCommerce.
Webb, Michael. 2020. ”The Impact of Artificial Intelligence on the Labor Market.” SSRN Working Paper
3482150.
Yin, Michelle, Hoa Vu, and Claudia Persico. 2026. ”How (un)Stable Are LLM Occupational Exposure
Scores? EvidencefromMulti-ModelReplication.”NBERWorkingPaper35110.
41

Appendix A. Derivation of the Probability Limit and Proofs
This appendix collects the derivations supporting Section I. Appendix A.1 states the setup. Appendix A.2
derives the additive decomposition of the platform-derived proxy. Appendix A.3 derives the probability
limit for the OLS coeﬀicient. Appendix A.4 verifies the special cases discussed in the main text. Appendix
A.5 derives the reweighted proxy and states the maintained ordering condition used for partial identifica-
tion. Appendix A.6 shows how cross-platform aggregation can reduce between-occupation selection when
platform-selection parameters are imperfectly correlated. Appendix A.7 gives the monotonicity prediction
usedinthereweightingtests. AppendixA.8givessupplementaryremarksonadoptionconfounding,effective
samplesize,andthescopeoftheframework.
A.1. Setup
Allvariablesareresidualizedwithrespecttothecontrols 𝑋𝑜 anddemeaned. Thestructuralequationis
𝑌𝑜 = 𝛽𝐸 𝑜 + 𝜀𝑜, (A.1)
with Cov(𝐸𝑜, 𝜀𝑜) = 0 . The researcher observes a platform-derived proxy,𝐸𝑜,𝑝, not true exposure𝐸𝑜.
The proxy is constructed from platform conversations and therefore reflects both the task composition of
occupation 𝑜andtherepresentationofoccupation 𝑜intheplatformuserbase.
Thederivationassumesthatthestructuralresidualisorthogonaltotheobservedproxyafterconditioning
onthecontrolsusedintheestimatingequation:
Cov(𝜀𝑜, 𝐸𝑜,𝑝) = 0. (A.2)
This assumption isolates the measurement problem in the regressor. It is the analogue of exogeneity for
thediagnosticregressionsusedinthepaper. Theclassicalnoisetermintheproxysatisfies
Cov(𝐸𝑜, 𝑢𝑜,𝑝) = 0. (A.3)
The within-occupation task-selection residual,𝜂𝑜,𝑝, may be correlated with𝐸𝑜. That correlation is one
reasonthemeasurementerrorisnon-classical.
A.2. Platform Proxy Decomposition
Let 𝑞𝑜,𝑘 denote the workforce task-time share of task𝑘 in occupation𝑜, with∑𝑘 𝑞𝑜,𝑘 = 1. Let 𝜏𝑘 denote
thetask-levelAIcapabilityscore. Trueoccupationalexposureis
42

𝐸𝑜 = ∑
𝑘
𝑞𝑜,𝑘𝜏𝑘. (A.4)
Let 𝑞𝑜,𝑘,𝑝 denotethewithin-occupationtaskshareobservedinplatform 𝑝’sconversationsforoccupation
𝑜. Definethewithin-occupationtask-selectionparameter
𝜃𝑜,𝑘,𝑝 ≡ 𝑞𝑜,𝑘,𝑝 𝑞𝑜,𝑘 . (A.5)
Let 𝑓𝑝(𝑜)betheplatformconversationshareofoccupation 𝑜,andlet 𝑓(𝑜) betheworkforceemployment
shareofoccupation 𝑜. Thebetween-occupationplatform-selectionparameteris
𝜓𝑜,𝑝 ≡ 𝑓𝑝(𝑜) 𝑓(𝑜) . (A.6)
Aplatform-derivedexposureproxythatweightstaskcapabilitybyplatformconversationdensitycanbe
writtenas
𝐸𝑜,𝑝 = 𝜓 𝑜,𝑝 ∑
𝑘
𝑞𝑜,𝑘,𝑝𝜏𝑘 + 𝑢𝑜,𝑝. (A.7)
Substituting 𝑞𝑜,𝑘,𝑝 = 𝜃 𝑜,𝑘,𝑝𝑞𝑜,𝑘 gives
𝐸𝑜,𝑝 = 𝜓 𝑜,𝑝 ∑
𝑘
𝜃𝑜,𝑘,𝑝𝑞𝑜,𝑘𝜏𝑘 + 𝑢𝑜,𝑝. (A.8)
Addandsubtract 𝜓𝑜,𝑝 ∑𝑘 𝑞𝑜,𝑘𝜏𝑘. Since𝐸𝑜 = ∑ 𝑘 𝑞𝑜,𝑘𝜏𝑘,
𝐸𝑜,𝑝 = 𝜓 𝑜,𝑝𝐸𝑜 + 𝜓𝑜,𝑝 ∑
𝑘
(𝜃𝑜,𝑘,𝑝 − 1)𝑞𝑜,𝑘𝜏𝑘 + 𝑢𝑜,𝑝. (A.9)
Define
𝜂𝑜,𝑝 ≡ 𝜓 𝑜,𝑝 ∑
𝑘
(𝜃𝑜,𝑘,𝑝 − 1)𝑞𝑜,𝑘𝜏𝑘. (A.10)
Then
𝐸𝑜,𝑝 = 𝜓 𝑜,𝑝𝐸𝑜 + 𝜂𝑜,𝑝 + 𝑢𝑜,𝑝. (A.11)
This is equation (3) in the main text. The first term is the between-occupation component. The second
43

termisthewithin-occupationtask-selectionresidual. Thethirdtermisclassicalnoise.
The parameter 𝜓𝑜,𝑝 is identified from platform occupation shares and OEWS workforce shares. The
parameter 𝜃𝑜,𝑘,𝑝 requires worker-representative task-time data measured on the same task taxonomy as the
platform. Current survey data do not provide such a crosswalk at theO*NET task level, so𝜂𝑜,𝑝 remains
unobserved.
A.3. OLS Probability Limit
Theresearcherestimates
𝑌𝑜 = 𝛽 𝑝𝐸𝑜,𝑝 + 𝜉𝑜 (A.12)
usingtheplatformproxy. Letthelinearprojectionoftheproxyontrueexposurebe
𝐸𝑜,𝑝 = 𝜆 𝑝𝐸𝑜 + 𝑣𝑜,𝑝, Cov(𝐸𝑜, 𝑣𝑜,𝑝) = 0, (A.13)
where
𝜆𝑝 =
Cov(𝐸𝑜,𝑝, 𝐸𝑜)
Var(𝐸𝑜) . (A.14)
Let
𝜎2 𝑣,𝑝 ≡ Var(𝑣𝑜,𝑝), 𝜅 𝑝 ≡ Var(𝐸𝑜) 𝜎2𝑣,𝑝 . (A.15)
TheprobabilitylimitoftheOLScoeﬀicientis
plim ̂𝛽𝑝 = Cov(𝑌𝑜, 𝐸𝑜,𝑝) Var(𝐸𝑜,𝑝) . (A.16)
Using 𝑌𝑜 = 𝛽𝐸 𝑜 + 𝜀𝑜 andCov (𝜀𝑜, 𝐸𝑜,𝑝) = 0,
Cov(𝑌𝑜, 𝐸𝑜,𝑝) = 𝛽 Cov(𝐸𝑜, 𝐸𝑜,𝑝) = 𝛽𝜆 𝑝Var(𝐸𝑜). (A.17)
Fromequation(A.13),
Var(𝐸𝑜,𝑝) = 𝜆 2 𝑝Var(𝐸𝑜) + 𝜎2 𝑣,𝑝. (A.18)
Combiningequations(A.16)through(A.18),
44

plim ̂𝛽𝑝 = 𝛽𝜆𝑝Var(𝐸𝑜) 𝜆2𝑝Var(𝐸𝑜) + 𝜎2𝑣,𝑝 . (A.19)
Dividingnumeratoranddenominatorby 𝜎2 𝑣,𝑝 yields
plim ̂𝛽𝑝 = 𝛽𝜆𝑝𝜅𝑝 𝜆2𝑝𝜅𝑝 + 1 . (A.20)
Thisisequation(4)inthemaintext.
A.4. Special Cases
Classical measurement error. If the platform proxy is a classical noisy measure of true exposure, then
𝜆𝑝 = 1. Equation(A.20)becomes
plim ̂𝛽𝑝 = 𝛽𝜅𝑝 𝜅𝑝 + 1 , (A.21)
whichisthestandardattenuationformula.
Overrepresentation of high-exposure occupations. Suppose 𝜆𝑝 > 1. This occurs when the platform
overrepresents occupations with high true exposure. With no residual projection error,𝜎2 𝑣,𝑝 = 0, equation
(A.19)becomes
plim ̂𝛽𝑝 = 𝛽 𝜆𝑝 . (A.22)
For 𝛽 > 0, thisissmallerthan 𝛽. For𝛽 < 0, itisclosertozeroinmagnitude. Withresidualprojection
error,thecoeﬀicientisfurtherscaledbythesignal-to-noiseratioinequation(A.20). Thus,overrepresentation
of high-exposure occupations changes the magnitude of the coeﬀicient through𝜆𝑝 and generally produces
attenuationrelativetothestructuralcoeﬀicientwhen 𝜆𝑝 > 1 andthesignal-to-noiseratioissuﬀicientlylarge.
Underrepresentation of high-exposure occupations. Suppose 0 < 𝜆 𝑝 < 1. With no residual projec-
tionerror,
plim ̂𝛽𝑝 = 𝛽 𝜆𝑝 , (A.23)
whichexceeds 𝛽 inabsolutevaluewhen 𝛽 ≠ 0. Underrepresentationofhigh-exposureoccupationscan
therefore amplify the coeﬀicient rather than attenuate it. This is not possible under classical measurement
error,whereattenuationisalwaystowardzero.
Platform-specific probability limits. Iftwoplatforms 𝑝and 𝑝′ havedifferent 𝜆parametersordifferent
45

residualvariances,then
plim ̂𝛽𝑝 ≠ plim ̂𝛽𝑝′
even when both regressions use the same outcome, controls, sample, and estimator. This is the formal
sourceofthecross-platformcoeﬀicientdispersiontestedinthepaper.
A.5. Reweighting and the Maintained Ordering Condition
Definetheworkforce-reweightedproxy
̃𝐸𝑜,𝑝 ≡ 𝐸𝑜,𝑝 𝜓𝑜,𝑝 . (A.24)
Usingequation(A.11),
̃𝐸𝑜,𝑝 = 𝐸 𝑜 + 𝜂𝑜,𝑝 𝜓𝑜,𝑝 + 𝑢𝑜,𝑝 𝜓𝑜,𝑝 . (A.25)
Thus reweighting removes the between-occupation component exactly. If𝜂𝑜,𝑝 = 0 and 𝑢𝑜,𝑝 = 0 ,
then ̃𝐸𝑜,𝑝 = 𝐸 𝑜. With classical noise but no within-occupation task selection, the reweighted proxy is
a classical noisy measure of true exposure. With within-occupation task selection, the reweighted proxy
remainscontaminatedby 𝜂𝑜,𝑝/𝜓𝑜,𝑝.
Let ̃𝜆𝑝 denotetheprojectioncoeﬀicientof ̃𝐸𝑜,𝑝 on 𝐸𝑜:
̃𝜆𝑝 = Cov(̃𝐸𝑜,𝑝, 𝐸𝑜) Var(𝐸𝑜) . (A.26)
Let ̃ 𝑣𝑜,𝑝 = ̃𝐸𝑜,𝑝 − ̃𝜆𝑝𝐸𝑜 and ̃ 𝜅𝑝 = Var(𝐸𝑜)/Var( ̃ 𝑣𝑜,𝑝). The probability limit of OLS using the
reweightedproxyis
plim ̃𝛽𝑝 = 𝛽 ̃𝜆𝑝 ̃ 𝜅𝑝 ̃𝜆2𝑝 ̃ 𝜅𝑝 + 1 . (A.27)
Thereweightedcoeﬀicientidentifies 𝛽 onlyunderadditionalconditions. Asuﬀicientconditionis
𝜂𝑜,𝑝 = 0, 𝑢 𝑜,𝑝 = 0. (A.28)
More generally, reweighting removes the observable between-occupation component but leaves the
within-occupation residual. The empirical bounds in the paper rely on the following maintained ordering
46

condition.
Maintained ordering condition. Within-occupation task selection biases the coeﬀicient in the same
direction as between-occupation platform selection and does not reverse the ordering between the baseline
andreweightedcoeﬀicients.
Under this maintained condition, the structural coeﬀicient lies between the baseline platform-derived
coeﬀicientandtheworkforce-reweightedcoeﬀicient. Theidentifiedsetistherefore
𝛽 ∈ [min{ ̂𝛽𝑝, ̃𝛽𝑝},max{ ̂𝛽𝑝, ̃𝛽𝑝}] . (A.29)
When the outcome coeﬀicient is reported in absolute-value terms, the corresponding interval is defined
over magnitudes. The width of the interval measures the contribution of observable between-occupation
platformselectiontothereportedcoeﬀicient.
The maintained ordering condition cannot be verified with current platform releases alone. It would re-
quireworker-representativetask-timedataandplatformtask-timedatameasuredonthesametasktaxonomy.
The condition is economically plausible when early adopters select high-payoff tasks both across occupa-
tions and within occupations, but the bounds reported in the paper remain conditional on this maintained
assumption.
A.6. Cross-Platform Aggregation
Let 𝑝 = 1, … , 𝑃 indexplatforms. Forplatform 𝑝,
𝐸𝑜,𝑝 = 𝜓 𝑜,𝑝𝐸𝑜 + 𝜂𝑜,𝑝 + 𝑢𝑜,𝑝. (A.30)
Consideranaggregateproxy
̄𝐸𝑜 =
𝑃
∑
𝑝=1
𝑤𝑝𝐸𝑜,𝑝, 𝑤 𝑝 ≥ 0,
𝑃
∑
𝑝=1
𝑤𝑝 = 1. (A.31)
Substitutingequation(A.30),
̄𝐸𝑜 = (
𝑃
∑
𝑝=1
𝑤𝑝𝜓𝑜,𝑝) 𝐸𝑜 +
𝑃
∑
𝑝=1
𝑤𝑝𝜂𝑜,𝑝 +
𝑃
∑
𝑝=1
𝑤𝑝𝑢𝑜,𝑝. (A.32)
Define
𝜓𝑤 𝑜 ≡
𝑃
∑
𝑝=1
𝑤𝑝𝜓𝑜,𝑝, 𝜂 𝑤 𝑜 ≡
𝑃
∑
𝑝=1
𝑤𝑝𝜂𝑜,𝑝, 𝑢 𝑤 𝑜 ≡
𝑃
∑
𝑝=1
𝑤𝑝𝑢𝑜,𝑝. (A.33)
47

Then
̄𝐸𝑜 = 𝜓 𝑤 𝑜 𝐸𝑜 + 𝜂𝑤 𝑜 + 𝑢𝑤 𝑜 . (A.34)
The aggregate proxy has the same structural form as a single-platform proxy. It identifies true exposure
onlyif 𝜓𝑤 𝑜 = 1 foralloccupationsand 𝜂𝑤 𝑜 = 0 foralloccupations. Exactcancellationofplatformselection
is generally infeasible when the number of occupations exceeds the number of platforms. However, aggre-
gation can reduce between-occupation selection variance when platform-specific selection parameters are
imperfectlycorrelated.
Toseethis,let Δ𝑜,𝑝 = 𝜓 𝑜,𝑝 − 1 and Δ𝑤 𝑜 = ∑ 𝑝 𝑤𝑝Δ𝑜,𝑝. Then
Var(Δ𝑤 𝑜 ) = ∑
𝑝
𝑤2 𝑝Var(Δ𝑜,𝑝) + 2 ∑
𝑝<𝑞
𝑤𝑝𝑤𝑞Cov(Δ𝑜,𝑝, Δ𝑜,𝑞). (A.35)
If selection parameters are imperfectly correlated across platforms, aggregation can reduce Var(Δ𝑤 𝑜 )
relativeto a single platform. This result motivatescross-platform aggregation as a partial correction, not as
asubstituteforworkforce-representativemeasurement.
A.7. Skew-Attenuation Monotonicity
The reweighting exercise implies a testable prediction. Platforms whose occupation distributions are closer
totheworkforceshouldexhibitsmallerattenuationwhenreweighted.
Letbetween-occupationskewbemeasuredbyVar (𝜓𝑜,𝑝)orbyStd (log 𝜓𝑜,𝑝). Supposethat,acrossplat-
forms, the within-occupation task-selection residual𝜂𝑜,𝑝 is held fixed or is small relative to the between-
occupationcomponent. AsVar (𝜓𝑜,𝑝) → 0 and 𝐸[𝜓𝑜,𝑝] → 1,theproxyapproaches
𝐸𝑜,𝑝 → 𝐸 𝑜 + 𝜂𝑜,𝑝 + 𝑢𝑜,𝑝. (A.36)
If 𝜂𝑜,𝑝 is also invariant across platforms, then the platform-specific movement in the probability limit
is driven primarily by𝜓𝑜,𝑝. The reweighting correction approaches the identity as𝜓𝑜,𝑝 → 1. Hence the
attenuationfromreweightingismonotoneinthedistancebetweentheplatformuserbaseandtheworkforce,
providedthebetween-occupationcomponentdominatestheplatform-specificvariation.
This prediction is tested empirically in Section III.E by comparing reweighting attenuation across the
compositeandMicrosoftCopilotmeasures. Theplatformclosertoworkforceemploymentsharesattenuates
lessafterreweighting.
48

A.8. Supplementary Remarks
Adoption confounding. The main derivation treats the structural equation as a relationship between labor-
market outcomes and true exposure. If adoption enters the structural equation separately, the relationship
becomes
𝑌𝑜 = 𝛽𝐸 𝑜 + 𝜌𝐴𝑜 + 𝜀𝑜, (A.37)
where 𝐴𝑜 is AI adoption. If the platform proxy is correlated with adoption, then the probability limit
includesanadditionalterm:
plim ̂𝛽𝑝 = 𝛽Cov(𝐸𝑜, 𝐸𝑜,𝑝) + 𝜌Cov(𝐴𝑜, 𝐸𝑜,𝑝) Var(𝐸𝑜,𝑝) . (A.38)
Themaintextfocusesonthemeasurementproblemin 𝐸𝑜,𝑝,holdingthedownstreamspecificationfixed.
Equation (A.38) shows that adoption can create an additional channel when adoption is itself an omitted
determinant of outcomes. This does not remove the platform-selection problem. It adds another reason to
distinguishcapability,adoption,andconditionaluse.
Effective sample size. Themeasurement-errorproblemisnotgovernedbythenumberofindividualsin
the downstream ACS regression. The exposure measure varies at the occupation level. Thus, the relevant
variation is the number of distinct occupational exposure cells, not the number of person-year observations.
Adding more individuals improves precision for outcome means conditional on occupation, but it does not
changetheprobabilitylimitgeneratedbyaselectedoccupation-levelproxy.
Scope of the framework. The framework applies to several sources of variation used in the paper. It
applies across platforms, such as Anthropic, OpenAI, Microsoft, and survey-based measures. It applies
acrossproductchannelswithinthesameplatform,suchasClaude.aiconsumeruseandtheenterpriseAPI.It
appliesacrosswaveswithinthesameplatformwhenproductlaunchesorpricingchangesshifttheuserbase.
It also applies to comparisons between survey and platform data, since each source represents a different
populationframeandadifferentmeasurementunit.
Interpretation of platform data. The framework does not imply that platform logs are uninformative.
Platform logs are informative about task use among observed users. The problem arises when observed
platform use is interpreted as workforce exposure without adjustment. The reweighting procedure removes
the part of this selection that is observed in occupation shares. The remaining component requires worker-
taskdatathatobservebothplatformusersandnonusersonacommontasktaxonomy.
49

Online Appendix B. Supplementary Tables and Figures
This online appendix contains supplementary tables (B.1 through B.12) and supplementary figures (B.1
throughB.7)referencedinthemaintext.
50

Table B.1. Variable Definitions, Data Sources, and Summary Statistics
Panel A. American Community Survey analytical sample variables: definitions and person-weighted summary statistics (wage-and-salary workers, ages 16 to 64, 2015 to 2024)
Variable Definition Mean SD Min Max
year Surveyyear(2015to2024) n/a n/a 2015 2024
statefip StateFIPScode(51levels) 51levels n/a 1 56
occsoc Six-digitSOCoccupationcode(SOC-2018) 553levels n/a 111021 999920
perwt Personweight(sample-to-populationscaling) 189.86 166.22 1.00 3,773
post Post-2022indicator(=1ifyear≥2023) 0.204 0.403 0.000 1.00
employed Binaryemploymentindicator(=1ifemployed;ACSempstat) 0.844 0.363 0.000 1.00
age Ageinyears(continuous;restrictedto16to64) 39.17 13.47 16.00 64.00
age2 Agesquared 1,716 1,094 256.00 4,096
female Femaleindicator(ACSsex) 0.507 0.500 0.000 1.00
married Currentlymarriedindicator(ACSmarst) 0.474 0.499 0.000 1.00
hsgrad High-schoolgraduate,nocollege(ACSeduc) 0.334 0.472 0.000 1.00
scoll Somecollege,nobachelor's(ACSeduc) 0.253 0.434 0.000 1.00
bachelor_higher Bachelor'sdegreeorhigher(ACSeduc) 0.335 0.472 0.000 1.00
nchild Numberofownchildreninhousehold(ACSnchild) 0.756 1.11 0.000 9.00
nhwhite Non-Hispanicwhite(ACSrace×hispan) 0.591 0.492 0.000 1.00
nhblack Non-HispanicBlack(ACSrace×hispan) 0.125 0.331 0.000 1.00
hisp Hispanic,anyrace(ACShispan) 0.182 0.386 0.000 1.00
disabled Adultwithdisability,unionofsixACSitems(diffrem,diffphys,diffmob,diffcare,
diffeye,diffhear)
0.075 0.264 0.000 1.00
incwage Wageandsalaryincome,current-yearUSD(ACS) 46,690 58,368 0.000 907,000
Panel B. National Health Interview Survey Sample Adult cross-domain outcome variables: definitions and source variable codes (2017 to 2018; N = 49,066; aggregated at Standard Occupational
Classification major-group level)
Variable Definition Source
k6_score Kessler6-itempsychological-distressscale(0to24) NHISKESSLER6
k6_distress =1ifK6score>=13(clinicallymeaningfuldistress) NHISKESSLER6>=13
smoke_ever =1ifeversmoked>=100cigaretteslifetime NHISSMOKEV=2
smoke_current =1ifcurrentdailyorsome-daysmoker NHISSMOKESTATUS2in{1,2}
drinker_pastyr =1ifanyalcoholconsumptioninpast12months NHISALCSTAT1>=2
drinks_per_day Meandrinksperday|past-yeardrinker NHISALCDAYSYR*ALCAMT/365
binge_any =1ifanybinge-drinkingepisodeinpastyear NHISALC5UPYR>=1
sleep_short =1ifusualsleep<6hourspernight NHISHRSLEEP<6
self_rated_poor =1ifself-ratedhealthisfair”or”poor”” NHISHEALTHin{4,5}
Panel C. Anthropic Economic Index wave characteristics and Computer & Mathematical share
Wave Period Model Product launch SOC cells C&M share
Wave1 Dec2024 Sonnet3.5 n/a 981 37%
Wave2 Feb2025 Sonnet3.7 n/a 999 40%
Wave3 Aug2025 Sonnet4 ClaudeCodelaunch 928 39%
Wave4 Nov2025 Sonnet4.5 Projectsexpansion 974 36%
Wave5 Feb2026 Opus4.6 n/a 964 32%
Panel D. Data sources
51

Source T ype Period Sample
AEIClaude.ai(Anthropic,consumer) Platformusage Dec2024-Feb2026 5waves
AEI1PAPI(Anthropic,enterprise) Platformusage Aug2025-Feb2026 3waves
OpenAIChatGPT( Chatterjietal. 2025 ) Platformusage May2024-Jun2025 5-groupoccupationdistribution
MicrosoftCopilot( Tomlinsonetal. 2025) Platformusage(consumer) Sept2024 AIapplicabilityatSOC-6
BBD-RPS(Bick,Blandin,andDeming2026) Populationsurvey Dec2024 Per-occupationGenAIuserate
BLSOES Establishmentsurvey May2024 ~1.1Mestablishments
BLSEmploymentProjections Administrative 2024-2034 10-yearoccupationprojections
IPUMS-USAACS1-year(analyticoutcomepanel) Householdsurvey 2015-2024 13,104,072person-years(16-64)
Eloundouetal. 2024 GPT-4binary 𝛽rubric Task-levelcapability 2023 Per-taskAIapplicability
NHISSampleAdult(cross-domain§VI) Householdsurvey 2017-2018 49,066adults
Panel E. Anthropic Economic Index coverage and Standard Occupational Classification match rate
Statistic Value
TotalBLSSOC2018detailedcells(OESMay2024) 831
AEIClaude.ainonzeroNEMcells(rangeW1-W5) 928-999
MicrosoftCopilotSOCcells( Tomlinsonetal. 2025) 1336
DistinctSOC-6codesinACSanalyticsample 553
ACSoccsoccodesmatchedtoBLSSOC2018 390of553(70.5%bycode)
ACSperson-year-weightedmatchratetoBLSSOC2018 68.06%(9,900,621of13,104,072)
Panel F. National Health Interview Survey Sample Adult 2017 to 2018 cross-domain outcomes
Variable Mean SD Min Max
K6distressscore(0to24) 2.777 0.436 1.992 3.762
K6severedistress(>=13) 0.036 0.015 0.009 0.064
Eversmoker 0.371 0.077 0.239 0.539
Currentsmoker 0.141 0.060 0.044 0.251
Drinker(pastyear) 0.676 0.077 0.549 0.846
Drinksperday|past-yeardrinker 2.327 0.392 1.804 3.246
Anybinge-drinkingepisode 0.387 0.056 0.289 0.498
Shortsleep(<6hrs) 0.096 0.025 0.043 0.153
Notes: Panels A and B document the definitions and weighted summary statistics for every variable used in the analysis on the canonical American Community Survey analytical sample (wage-and-
salary workers ages 16 to 64, 2015 to 2024) and on the cross-domain National Health Interview Survey Sample Adult sample. Panel C summarizes the five Anthropic Economic Index waves (period, model
version, notable product launch, number of nonzero Standard Occupational Classification 6-digit cells, and the share of conversations attributed to Computer and Mathematical occupations). Panel D
reports the complete data-source inventory. Panel E reports the occupation-crosswalk coverage between American Community Survey occupation codes and 2018 Standard Occupational Classification
6-digit codes. Panel F reports cross-domain outcome summary statistics from the National Health Interview Survey Sample Adult file (2017 to 2018) used in Section IV. Statistics are person-weighted
using the American Community Survey person weight (perwt). Mean and standard deviation are reported for binary and continuous variables; for categorical and identifier variables, the level count
is reported in place of mean and standard deviation. The disability indicator is constructed as the union of the six American Community Survey disability items (cognitive, ambulatory, hearing, vision,
self-care, independent living diﬀiculties: diffrem, diffphys, diffhear, diffeye, diffcare, diffmob). The post indicator equals one for survey years 2023 and 2024 (zero otherwise). Min and max report the
observed minimum and maximum values within the analytical sample. n/a denotes not applicable (typically for categorical or identifier variables where mean/SD are not meaningful). Abbreviations: SOC
= Standard Occupational Classification; AEI = Anthropic Economic Index; CAI = Claude.ai consumer; API = first-party Application Programming Interface enterprise; Composite = AI exposure score
constructed following Massenkoff and McCrory (2026) ; BBD = Bick-Blandin-Deming Survey of Working Arrangements and Attitudes; BLS = Bureau of Labor Statistics; OES = Occupational Employment
and Wage Statistics; CKK = Chen, Kane, Kozlowski et al. (2025); ACS = American Community Survey; CPS-MORG = Current Population Survey-Outgoing Rotation Group.
52

Table B.2. Cross-Platform Composition and Descriptive Correlates by SOC Major Group
Panel A. Cross-platform composition: conversation shares, use rates, and workforce share
SOC major group Claude.ai W5 (%) 1P API W5 (%) ChatGPT pct_work Microsoft Copilot score BBD GenAI use (%) BLS workforce (%)
ComputerandMathematical 32.3 51.7 57.0 0.29 47.9 3.4
EducationalInstructionandLibrary 13.5 3.1 44.0 0.21 33.5 5.8
Arts,Design,Entertainment,Sports,Media 10.4 5.2 44.0 0.24 31.0 1.4
OﬀiceandAdministrativeSupport 9.4 17.6 40.0 0.26 18.5 11.8
Life,Physical,andSocialScience 6.3 4.4 48.0 0.19 n/a 0.9
SalesandRelated 4.9 4.1 40.0 0.29 20.9 8.7
BusinessandFinancial 4.8 3.5 50.0 0.24 40.0 6.7
Management 4.3 3.4 50.0 0.14 45.2 7.1
CommunityandSocialService 3.2 0.5 44.0 0.25 n/a 1.7
HealthcarePractitionersandTechnical 3.0 1.0 44.0 0.12 30.2 6.2
ArchitectureandEngineering 2.0 1.7 48.0 0.22 n/a 1.7
PersonalCareandService 1.2 0.4 40.0 0.18 n/a 2.0
FoodPreparationandServing 0.7 0.1 40.0 0.17 n/a 8.8
Production 0.7 1.2 40.0 0.11 n/a 5.7
Installation,Maintenance,andRepair 0.7 0.4 40.0 0.10 n/a 3.9
Legal 0.6 0.2 44.0 0.13 n/a 0.8
Farming,Fishing,andForestry 0.5 0.1 40.0 0.06 n/a 0.3
ProtectiveService 0.4 0.5 40.0 0.12 n/a 2.4
HealthcareSupport 0.3 0.2 40.0 0.05 n/a 4.8
TransportationandMaterialMoving 0.2 0.2 40.0 0.10 n/a 8.9
ConstructionandExtraction 0.2 0.3 40.0 0.07 n/a 4.1
BuildingandGroundsCleaning 0.2 0.1 40.0 0.08 n/a 2.9
Panel B. Descriptive correlates by SOC major group: education, wages, disability, and platform exposure
SOC major group BA+ share Wage (2022 $) Disability share C&M conv. share psi
Management 0.57 92.3 0.05 0.075 0.55
BusinessandFinancial 0.68 84.3 0.05 0.087 0.99
ComputerandMathematical 0.67 97.4 0.05 0.32 9.41
ArchitectureandEngineering 0.72 94.5 0.04 0.052 1.86
Life,Physical,SocialScience 0.87 82.2 0.04 0.026 2.36
CommunityandSocialService 0.73 47.5 0.07 0.018 0.86
Legal 0.5 54.0 0.06 0.027 2.45
Education,Training,Library 0.75 45.6 0.06 0.046 0.78
Arts,Design,Entertainment 0.58 52.8 0.06 0.043 2.0
HealthcarePractitioners 0.58 81.2 0.05 0.024 0.32
HealthcareSupport 0.13 26.6 0.1 0.005 0.11
ProtectiveService 0.27 58.1 0.08 0.006 0.27
FoodPreparation 0.08 17.2 0.09 0.005 0.08
Building,GroundsCleaning 0.06 23.9 0.1 0.002 0.06
PersonalCare 0.16 20.0 0.08 0.005 0.18
Sales 0.25 46.0 0.08 0.024 0.3
OﬀiceandAdministrative 0.22 36.4 0.08 0.046 0.39
Farming,Fishing,Forestry 0.11 33.3 0.1 0.001 0.13
ConstructionandExtraction 0.06 45.5 0.08 0.005 0.1
Installation,Maintenance,Repair 0.08 51.9 0.08 0.011 0.32
Production 0.09 42.8 0.09 0.02 0.32
Transportation,MaterialMoving 0.09 35.3 0.1 0.011 0.13
Notes: Panel A is a wide-format companion to Table 3 (main text), restricted to the major groups with the highest platform conversation share or use rate. Panel B reports descriptive correlates of SOC major groups, including the share of workers with a Bachelor’s
degree or higher (BA+ share), annual wage and salary income in 2022 dollars (thousands), the share of adults with disability under the union-of-six American Community Survey disability items, the Anthropic Economic Index Wave 5 share of conversations attributed to
the Computer and Mathematical major group (C&M conv. share), and the Baseline Composite (Anthropic) exposure score (psi) from Eloundou et al. (2024) . All Panel B statistics are person-weighted using the American Community Survey person weight (perwt). Each
row reports a 2-digit Standard Occupational Classification major group with the per-platform conversation share, use rate, or applicability score. Claude.ai W5 (%) and 1P API W5 (%) are Wave 5 Anthropic Economic Index conversation shares for the consumer Claude.ai
and the first-party Application Programming Interface enterprise platforms, respectively. ChatGPT pct_work is the percentage-of-work-tasks measure from Chatterji et al. (2025) . Microsoft Copilot score is the artificial-intelligence applicability score ( Tomlinson et al.
2025) employment-weighted to Standard Occupational Classification major group; values range from 0 to 1. BBD GenAI use (%) is the total generative artificial-intelligence use rate from Bick, Blandin, and Deming (2026) Real-Time Population Survey December 2024;
n/a denotes major groups not surveyed. BLS workforce (%) is the May 2024 Occupational Employment and Wage Statistics employment share. Rows are ordered by descending Claude.ai Wave 5 share. Abbreviations: SOC = Standard Occupational Classification; AEI =
Anthropic Economic Index; CAI = Claude.ai consumer; API = first-party Application Programming Interface enterprise; Composite = AI exposure score constructed following Massenkoff and McCrory (2026); BBD = Bick-Blandin-Deming Survey of Working Arrangements
and Attitudes; BLS = Bureau of Labor Statistics; OES = Occupational Employment and Wage Statistics; CKK = Chen, Kane, Kozlowski et al. (2025); ACS = American Community Survey; CPS-MORG = Current Population Survey-Outgoing Rotation Group.
53

Table B.3. ACS to SOC 2018 Crosswalk Coverage
Major group (SOC-2) Distinct SOC-6 ACS records Share (%)
Management(11) 31 998599 7.6205
BusinessandFinancial(13) 30 795077 6.0674
ComputerandMathematical(15) 24 452665 3.4544
ArchitectureandEngineering(17) 19 214489 1.6368
Life,Physical,andSocialScience(19) 19 103348 0.7887
CommunityandSocialService(21) 17 254569 1.9427
Legal(23) 5 60588 0.4624
EducationalInstructionandLibrary(25) 13 989536 7.5514
Arts,Design,Entertainment,Sports,Media(27) 34 227508 1.7362
HealthcarePractitionersandTechnical(29) 45 871276 6.6489
HealthcareSupport(31) 13 415051 3.1673
ProtectiveService(33) 18 311014 2.3734
FoodPreparationandServing(35) 14 934168 7.1288
BuildingandGroundsMaintenance(37) 7 239148 1.825
PersonalCareandService(39) 24 356659 2.7217
Sales(41) 19 1396284 10.6553
OﬀiceandAdministrativeSupport(43) 54 1710984 13.0569
Farming,Fishing,andForestry(45) 7 21709 0.1657
ConstructionandExtraction(47) 33 606107 4.6253
Installation,Maintenance,andRepair(49) 29 391864 2.9904
Production(51) 62 615100 4.694
TransportationandMaterialMoving(53) 31 1070850 8.1719
n/a(55) 4 67479 0.5149
n/a(99) 1 0 0.0
Notes: This table documents the crosswalk coverage between American Community Survey occupation codes (occsoc) and 2018 Standard
Occupational Classification 6-digit codes used throughout the analysis. Each row reports a 2-digit Standard Occupational Classification major
group (with the 2-digit code in parentheses), the number of distinct 6-digit Standard Occupational Classification 2018 codes observed in the American
Community Survey 2015 to 2024 canonical analytical sample, the unweighted record count (person-years), and the share of the analytical sample.
The Military (55) row reflects the small set of military occupations retained in the wage-and-salary worker analytical sample. The 'n/a (99)' row
is a residual American Community Survey occupation category that does not map to a specific Standard Occupational Classification major group;
it is excluded from the regression analysis. n/a denotes not applicable. Abbreviations: SOC = Standard Occupational Classification; AEI =
Anthropic Economic Index; CAI = Claude.ai consumer; API = first-party Application Programming Interface enterprise; Composite = AI exposure
score constructed following Massenkoff and McCrory (2026); BBD = Bick-Blandin-Deming Survey of Working Arrangements and Attitudes; BLS =
Bureau of Labor Statistics; OES = Occupational Employment and Wage Statistics; CKK = Chen, Kane, Kozlowski et al. (2025); ACS = American
Community Survey; CPS-MORG = Current Population Survey-Outgoing Rotation Group.
54

Table B.4. Wave-Pair Exposure Quartile Transitions
Wave pair N occupations Same quartile One-quartile move
T wo-plus-quartile
move
Waves1to2 715 68.8% 29.9% 1.3%
Waves1to3 670 58.5% 37.5% 4.0%
Waves1to4 685 60.3% 35.3% 4.4%
Waves1to5 689 58.2% 37.4% 4.4%
Waves2to3 670 62.7% 34.3% 3.0%
Waves2to4 681 63.4% 33.6% 2.9%
Waves2to5 684 59.9% 37.0% 3.1%
Waves3to4 669 72.5% 26.3% 1.2%
Waves3to5 671 69.2% 29.1% 1.8%
Waves4to5 702 85.5% 14.5% 0.0%
Notes: This table assesses the temporal stability of platform-visible occupational exposure rankings by reporting wave-to-wave quartile transi-
tion rates across the five Anthropic Economic Index waves. Each row reports the share of 6-digit Standard Occupational Classification occupations
remaining in the same employment-weighted exposure quartile, moving by one quartile, or moving by two or more quartiles between two Anthropic
Economic Index waves. Quartiles are constructed within wave using the employment-weighted distribution of the Anthropic Economic Index con-
versation share, with weights from Bureau of Labor Statistics May 2024 Occupational Employment and Wage Statistics. N is the number of 6-digit
Standard Occupational Classification occupations with valid wave-pair exposure data. High wave-pair movement (low same-quartile shares, high
one- and two-plus-quartile move shares) indicates substantial month-to-month instability in occupation-level exposure rankings, motivating con-
cern about using a single wave's platform-visible distribution as a stationary measure of occupational exposure. Abbreviations: SOC = Standard
Occupational Classification; AEI = Anthropic Economic Index; CAI = Claude.ai consumer; API = first-party Application Programming Interface
enterprise; Composite = AI exposure score constructed following Massenkoff and McCrory (2026) ; BBD = Bick-Blandin-Deming Survey of Work-
ing Arrangements and Attitudes; BLS = Bureau of Labor Statistics; OES = Occupational Employment and Wage Statistics; CKK = Chen, Kane,
Kozlowski et al. (2025); ACS = American Community Survey; CPS-MORG = Current Population Survey-Outgoing Rotation Group.
55

Table B.5. Robustness Compendium of Significance Counts by Dimension
Source group
Sig at p<0.05 (full / excluding
2020-2021) Implication
Cross-platformraw(10canonicalvariants) 12/2 Cross-platformdispersioninmainDiD
coeﬀicient
Within-vendorchannelsubstitution(9cells) 2/1 compositerecipewithvendor-channel
substitutionatWaves3to5
Heterogeneity(5channelsx21subgroups) 59/46 SubgroupheterogeneityinmainDiD
coeﬀicient
Samplerestriction(3subsetsx7variants;fullsample) 10/notrun Robustnesstosamplerestrictions
(prime-age,non-Hispanicwhite,
female)
Fixed-effectsandspecificationsensitivity(5configsx7variants) 29/notrun Robustnesstofixed-effectsandcontrol
specifications
Wageoutcome(logofannualwageincome;7variants) 4/3 Intensive-marginwagerobustnessunder
canonicalspecification
Pre-trendjointWaldF-test(7variants) 6reject/notrun OnlyCompositeReweightedpasses
parallel-trendstest;allothervariants
rejectatplessthan0.05
Wild-clusterbootstrap(9variants;SOC-major-22cluster;legacy) 0/notrun ConservativeunderSOC-majorcluster
count;analyticstate-clusteredstandard
errorsarethecanonicalinference
Notes: This table compiles the counts of statistically significant DiD coeﬀicients at p < 0.05 across canonical variants within each robustness
dimension. The table is a summary index for the full robustness compendium documented in Tables B.7 to B.9 and the manuscript appendix. Counts
are reported separately for the full sample (American Community Survey 2015 to 2024) and the sample excluding 2020 and 2021 (a robustness
check that drops the two COVID-19 disruption years). Canonical variants comprise: Baseline Composite (Anthropic), Composite Reweighted,
Composite with Wave 5 AEI weights with Wave 5 Anthropic Economic Index weights, first-party Application Programming Interface enterprise Wave
5, Claude.ai consumer Wave 5, Microsoft Copilot, and Pooled Claude.ai consumer plus first-party Application Programming Interface enterprise
Wave 5. Robustness dimensions span outcome variation (employment vs labor-force participation vs log wage), fixed-effects and specification
sensitivity, sample restrictions (prime-age, non-Hispanic white, female), alternative wage outcomes, pre-trend joint Wald F-tests for parallel-trends
violation, and wild-cluster bootstrap inference under small-cluster-count regimes. The Implication column gives a one-line interpretation of each
robustness dimension. Abbreviations: SOC = Standard Occupational Classification; AEI = Anthropic Economic Index; CAI = Claude.ai consumer;
API = first-party Application Programming Interface enterprise; Composite = AI exposure score constructed following Massenkoff and McCrory
(2026); BBD = Bick-Blandin-Deming Survey of Working Arrangements and Attitudes; BLS = Bureau of Labor Statistics; OES = Occupational
Employment and Wage Statistics; CKK = Chen, Kane, Kozlowski et al. (2025); ACS = American Community Survey; CPS-MORG = Current
Population Survey-Outgoing Rotation Group.
56

Table B.6. Master Difference-in-Differences Coeﬀicient Grid Across Source, Recipe, and Channel
Variant Full sample Excluding 2020-2021
N (full / excluding
2020-2021)
Panel A. Raw Anthropic Economic Index conversation share (Claude.ai consumer / first-party Application Programming Interface enterprise /
pooled)
Claude.aiconsumer(Wave1) -0.116***
(0.035)
-0.017
(0.035)
10.95M/8.92M
Claude.aiconsumer(Wave3) -0.163***
(0.033)
-0.072*
(0.037)
11.00M/8.95M
Claude.aiconsumer(Wave5) -0.222***
(0.042)
-0.162***
(0.047)
11.18M/9.10M
1PAPIenterprise(Wave3) -0.144***
(0.035)
-0.062*
(0.035)
10.08M/8.22M
1PAPIenterprise(Wave5) -0.152***
(0.033)
-0.061*
(0.036)
10.16M/8.28M
Panel B. Baseline Composite (Anthropic) under cross-wave Anthropic Economic Index weighting
BaselineComposite(Anthropic) -0.139***
(0.035)
-0.003
(0.038)
8.63M/6.95M
CompositeReweighted -0.010
(0.045)
-0.020
(0.042)
8.63M/6.95M
CompositewithWave5AEIweights -0.155***
(0.031)
-0.001
(0.034)
8.63M/6.95M
Panel C. Microsoft Copilot artificial-intelligence applicability score (raw and reweighted)
MicrosoftCopilot(raw) -0.191***
(0.042)
-0.161***
(0.040)
12.28M/9.99M
MicrosoftCopilot(reweighted) -0.110***
(0.039)
-0.036
(0.041)
12.28M/9.99M
Panel D. Composite, channel-restricted (within-vendor channel substitution at Anthropic Economic Index Waves 3 to 5)
Claude.aiconsumer(Wave3) -0.087*
(0.052)
+0.006
(0.050)
4.73M/3.80M
Claude.aiconsumer(Wave4) -0.098**
(0.047)
+0.048
(0.048)
5.36M/4.31M
Claude.aiconsumer(Wave5) -0.076*
(0.043)
+0.069
(0.044)
5.77M/4.64M
1PAPIenterprise(Wave3) +0.015
(0.058)
-0.042
(0.052)
4.58M/3.69M
1PAPIenterprise(Wave4) +0.041
(0.047)
-0.047
(0.041)
4.60M/3.70M
1PAPIenterprise(Wave5) +0.055
(0.044)
+0.025
(0.043)
4.50M/3.63M
PooledCAI+API(Wave3) -0.064
(0.046)
-0.006
(0.041)
5.46M/4.39M
PooledCAI+API(Wave4) -0.098**
(0.038)
+0.020
(0.036)
6.17M/4.98M
PooledCAI+API(Wave5) -0.039
(0.038)
+0.091**
(0.038)
6.17M/4.97M
Notes: This table is the master grid of DiD coeﬀicients across all canonical variants used in the analysis, organized into four panels by source
family. Panel A reports raw Anthropic Economic Index conversation share variants (Claude.ai consumer at Waves 1, 3, 5; first-party Application
Programming Interface enterprise at Waves 3, 5). Panel B reports the Baseline Composite (Anthropic) under three weighting schemes (baseline
as published, employment-reweighted by Bureau of Labor Statistics, and Wave 5 Anthropic Economic Index weights substitution). Panel C reports
the Microsoft Copilot artificial-intelligence applicability score ( Tomlinson et al. 2025 ) in raw and reweighted forms. Panel D reports the within-
vendor channel-substitution variants under the composite construction at Anthropic Economic Index Waves 3 to 5 (Claude.ai consumer / first-party
Application Programming Interface enterprise / pooled). The regression specification is individual-level weighted least squares on the canonical
American Community Survey analytical sample (wage-and-salary workers, ages 16 to 64, 2015 to 2024). The dependent variable is a binary indicator
equal to one if the respondent is employed (American Community Survey empstat). The treatment variable is the standardized exposure measure
interacted with a post-treatment indicator (post = 1 if year is 2023 or later); coeﬀicients reported as beta-times-100 represent the percentage-point
change in employment per one-standard-deviation increase in exposure. Two-way fixed effects: year, state, and 6-digit Standard Occupational
Classification 2018 (SOC) occupation. Controls: sex (female indicator), marital status (married indicator), three educational-attainment indicators
(high-school graduate, some college, Bachelor's or higher), age, age squared, and number of own children. Exposure is z-scored within the analytical
sample using employment-weighted means and standard deviations. Regressions are person-weighted using the American Community Survey person
weight. Standard errors are cluster-robust at the state level (51 states including the District of Columbia) and reported in parentheses. Each cell
reports the coeﬀicient (beta times 100) with the cluster-robust standard error in parentheses. N reports unweighted person-year observation counts
in millions for the full and excluding-2020-2021 specifications. Significance: *** p < 0.01; ** p < 0.05; * p < 0.10. Abbreviations: SOC =
Standard Occupational Classification; AEI = Anthropic Economic Index; CAI = Claude.ai consumer; API = first-party Application Programming
Interface enterprise; Composite = AI exposure score constructed following Massenkoff and McCrory (2026) ; BBD = Bick-Blandin-Deming Survey
of Working Arrangements and Attitudes; BLS = Bureau of Labor Statistics; OES = Occupational Employment and Wage Statistics; CKK = Chen,
Kane, Kozlowski et al. (2025); ACS = American Community Survey; CPS-MORG = Current Population Survey-Outgoing Rotation Group.
57

Table B.7. Heterogeneity in Cross-Source Difference-in-Differences Coeﬀicients on Employment by Subgroup and Channel
Panel A. Demographics
Subgroup
Massenkoff
and
McCrory
baseline
(Full)
Massenkoff
and
McCrory
baseline
(Excluding
2020-2021)
Massenkoff
and
McCrory
reweighted
(Full)
Massenkoff
and
McCrory
reweighted
(Excluding
2020-2021)
Claude.ai
consumer
(Wave 5)
(Full)
Claude.ai
consumer
(Wave 5)
(Excluding
2020-2021)
1P API
enterprise
(Wave 5)
(Full)
1P API
enterprise
(Wave 5)
(Excluding
2020-2021)
Microsoft
Copilot
(2024) (Full)
Microsoft
Copilot
(2024)
(Excluding
2020-2021)
Pooled
Claude.ai +
1P API
(Wave 5)
(Full)
Pooled
Claude.ai +
1P API
(Wave 5)
(Excluding
2020-2021)
Disability
Hasdisability +0.148
(0.162)
+0.098
(0.158)
-0.101
(0.183)
-0.236
(0.172)
-0.521***
(0.160)
-0.559***
(0.188)
-0.174
(0.144)
-0.182
(0.155)
-0.119
(0.145)
-0.263*
(0.133)
-0.344**
(0.158)
-0.383**
(0.180)
Nodisability -0.138***
(0.035)
+0.016
(0.038)
+0.019
(0.043)
+0.023
(0.040)
-0.191***
(0.042)
-0.121***
(0.044)
-0.152***
(0.032)
-0.055
(0.033)
-0.157***
(0.044)
-0.107**
(0.040)
-0.172***
(0.035)
-0.093**
(0.036)
Education
Bachelor'sdegreeorhigher -0.004
(0.065)
+0.108
(0.069)
+0.069
(0.066)
+0.013
(0.066)
-0.089*
(0.050)
-0.044
(0.050)
-0.161***
(0.046)
-0.087*
(0.045)
+0.056
(0.055)
+0.098*
(0.052)
-0.134***
(0.046)
-0.075
(0.045)
Lessthanbachelor'sdegree -0.155***
(0.053)
-0.056
(0.053)
-0.058
(0.062)
-0.039
(0.059)
-0.319***
(0.060)
-0.277***
(0.062)
-0.128**
(0.058)
-0.061
(0.051)
-0.292***
(0.066)
-0.334***
(0.058)
-0.234***
(0.060)
-0.190***
(0.056)
Sex
Female +0.074
(0.051)
+0.228***
(0.053)
+0.008
(0.049)
+0.015
(0.054)
-0.129**
(0.059)
-0.082
(0.062)
-0.028
(0.050)
+0.063
(0.051)
+0.054
(0.051)
+0.103*
(0.052)
-0.072
(0.055)
-0.015
(0.057)
Male -0.388***
(0.046)
-0.263***
(0.057)
-0.035
(0.062)
-0.072
(0.068)
-0.307***
(0.049)
-0.237***
(0.051)
-0.235***
(0.045)
-0.140***
(0.037)
-0.454***
(0.052)
-0.443***
(0.060)
-0.268***
(0.044)
-0.187***
(0.041)
Raceandethnicity
Non-Hispanicwhite -0.053
(0.050)
+0.039
(0.055)
+0.026
(0.051)
+0.004
(0.052)
-0.177***
(0.042)
-0.147***
(0.044)
-0.162***
(0.048)
-0.107**
(0.048)
-0.066*
(0.037)
-0.069*
(0.039)
-0.175***
(0.046)
-0.138***
(0.047)
Non-HispanicBlack -0.062
(0.175)
+0.065
(0.161)
-0.082
(0.149)
-0.049
(0.143)
-0.535***
(0.136)
-0.485***
(0.141)
-0.244*
(0.132)
-0.135
(0.119)
-0.396**
(0.152)
-0.353**
(0.141)
-0.395***
(0.134)
-0.317**
(0.128)
Hispanic -0.074
(0.089)
+0.089
(0.093)
-0.080
(0.111)
-0.075
(0.113)
-0.233***
(0.071)
-0.115
(0.071)
-0.167***
(0.044)
+0.006
(0.057)
-0.094
(0.074)
-0.084
(0.066)
-0.208***
(0.048)
-0.065
(0.058)
Panel B. Wage, Occupation, Age, and Marital Status
Subgroup
Massenkoff
and
McCrory
baseline
(Full)
Massenkoff
and
McCrory
baseline
(Excluding
2020-2021)
Massenkoff
and
McCrory
reweighted
(Full)
Massenkoff
and
McCrory
reweighted
(Excluding
2020-2021)
Claude.ai
consumer
(Wave 5)
(Full)
Claude.ai
consumer
(Wave 5)
(Excluding
2020-2021)
1P API
enterprise
(Wave 5)
(Full)
1P API
enterprise
(Wave 5)
(Excluding
2020-2021)
Microsoft
Copilot
(2024) (Full)
Microsoft
Copilot
(2024)
(Excluding
2020-2021)
Pooled
Claude.ai +
1P API
(Wave 5)
(Full)
Pooled
Claude.ai +
1P API
(Wave 5)
(Excluding
2020-2021)
Wagequartile
Wagequartile1(lowest) -0.166
(0.103)
-0.180*
(0.099)
-0.268**
(0.112)
-0.285**
(0.109)
-0.386***
(0.089)
-0.323***
(0.092)
-0.217**
(0.085)
-0.269***
(0.090)
-0.591***
(0.111)
-0.664***
(0.110)
-0.379***
(0.089)
-0.386***
(0.093)
Wagequartile2 -0.110*
(0.056)
-0.044
(0.057)
-0.063
(0.047)
-0.035
(0.047)
-0.077**
(0.037)
-0.075*
(0.042)
-0.043
(0.045)
-0.017
(0.050)
-0.100*
(0.056)
-0.137**
(0.055)
-0.064
(0.042)
-0.057
(0.047)
Wagequartile3 -0.127***
(0.032)
-0.059
(0.036)
-0.040
(0.045)
-0.046
(0.048)
-0.048
(0.030)
-0.029
(0.030)
-0.023
(0.036)
-0.005
(0.037)
-0.072**
(0.031)
-0.052
(0.035)
-0.031
(0.035)
-0.014
(0.035)
Wagequartile4(highest) -0.166***
(0.025)
-0.109***
(0.025)
-0.054
(0.042)
-0.052
(0.039)
-0.119***
(0.023)
-0.088***
(0.019)
-0.077***
(0.022)
-0.051***
(0.018)
-0.152***
(0.021)
-0.101***
(0.020)
-0.092***
(0.022)
-0.065***
(0.019)
Occupationmajorgroup
ManagementandProfessional
(SOC11-29)
+0.005
(0.062)
+0.132**
(0.064)
+0.166**
(0.071)
+0.044
(0.066)
-0.102*
(0.053)
-0.076
(0.052)
-0.186***
(0.050)
-0.127***
(0.047)
+0.102*
(0.051)
+0.196***
(0.052)
-0.162***
(0.051)
-0.115**
(0.049)
Service(SOC31-39) -0.172
(0.131)
-0.259**
(0.125)
-0.186
(0.114)
-0.040
(0.112)
-0.000
(0.145)
-0.091
(0.163)
-0.502***
(0.116)
-0.226*
(0.115)
+0.071
(0.113)
-0.315***
(0.112)
-0.226
(0.139)
-0.163
(0.151)
58

Subgroup
Massenkoff
and
McCrory
baseline
(Full)
Massenkoff
and
McCrory
baseline
(Excluding
2020-2021)
Massenkoff
and
McCrory
reweighted
(Full)
Massenkoff
and
McCrory
reweighted
(Excluding
2020-2021)
Claude.ai
consumer
(Wave 5)
(Full)
Claude.ai
consumer
(Wave 5)
(Excluding
2020-2021)
1P API
enterprise
(Wave 5)
(Full)
1P API
enterprise
(Wave 5)
(Excluding
2020-2021)
Microsoft
Copilot
(2024) (Full)
Microsoft
Copilot
(2024)
(Excluding
2020-2021)
Pooled
Claude.ai +
1P API
(Wave 5)
(Full)
Pooled
Claude.ai +
1P API
(Wave 5)
(Excluding
2020-2021)
SalesandOﬀice(SOC41-43) +0.119
(0.072)
+0.006
(0.073)
-0.071
(0.071)
-0.097
(0.069)
-0.336***
(0.086)
-0.424***
(0.090)
+0.156**
(0.068)
+0.182**
(0.073)
+0.036
(0.064)
-0.046
(0.063)
-0.152*
(0.076)
-0.200**
(0.082)
Blue-collar(SOC45-53) +0.051
(0.085)
-0.004
(0.086)
+0.189*
(0.106)
+0.142
(0.103)
-0.162
(0.114)
-0.065
(0.124)
-0.290**
(0.135)
-0.124
(0.145)
-0.161**
(0.068)
-0.234***
(0.070)
-0.211
(0.133)
-0.060
(0.145)
Agestrata
Youngerthan35 -0.148**
(0.072)
-0.050
(0.069)
+0.036
(0.077)
+0.001
(0.080)
-0.294***
(0.081)
-0.255***
(0.088)
-0.194***
(0.046)
-0.095*
(0.048)
-0.358***
(0.075)
-0.376***
(0.076)
-0.253***
(0.062)
-0.196***
(0.068)
Age35to50 -0.175***
(0.056)
+0.025
(0.061)
-0.115*
(0.068)
-0.103
(0.078)
-0.161***
(0.055)
-0.070
(0.056)
-0.181***
(0.047)
-0.092*
(0.048)
-0.083
(0.060)
+0.033
(0.060)
-0.175***
(0.051)
-0.089*
(0.052)
Age50orolder +0.000
(0.060)
+0.109**
(0.051)
+0.083
(0.067)
+0.107
(0.072)
-0.153***
(0.056)
-0.095*
(0.054)
-0.041
(0.065)
+0.032
(0.059)
+0.002
(0.054)
+0.018
(0.053)
-0.083
(0.061)
-0.018
(0.056)
Maritalstatus
Married +0.013
(0.044)
+0.146***
(0.044)
+0.031
(0.062)
+0.047
(0.067)
-0.083**
(0.038)
-0.014
(0.044)
-0.068*
(0.040)
+0.009
(0.041)
+0.017
(0.037)
+0.102**
(0.041)
-0.071*
(0.041)
-0.000
(0.042)
Notes: Each cell reports the coeﬀicient on the interaction of standardized exposure with the post-treatment indicator (post = 1 if year is 2023 or later) from individual-level weighted least squares
subset regressions on the canonical American Community Survey analytical sample. Six channels: (1) Baseline Composite (Anthropic); (2) Massenkoff and McCrory reweighted (Bureau of Labor Statistics
population weights); (3) Claude.ai consumer Wave 5; (4) first-party Application Programming Interface enterprise Wave 5; (5) Microsoft Copilot 2024; (6) Pooled Claude.ai consumer plus first-party
Application Programming Interface enterprise Wave 5. Standard errors clustered on state in parentheses. Significance: *** p<0.01, ** p<0.05, * p<0.10.
59

Table B.8. Robustness Dispersion in Outcome and Specification Sensitivity
Perturbation beta x 100 range max/min ratio
Sign split (neg /
pos) Interpretation
Panel A. Outcome invariance across three labor-market outcomes (employment, labor-force participation, log wage)
Employment,fullsample 0.010to0.222 22.4x 10/0 Allnegative;
magnitudesdiverge
Employment,excluding2020-2021 0.001to0.162 >100x 10/0 Allnegative;
magnitudesdiverge
Labor-forceparticipation,fullsample 0.005to0.126 25.8x 5/5 Signmixingacross
variants
Labor-forceparticipation,excluding2020-2021 0.006to0.153 27.2x 2/8 Cross-source
dispersionpreserved
Logwage,fullsample 0.009to0.752 84.4x 5/2 Cross-source
dispersionpreserved
Logwage,excluding2020-2021 0.042to0.616 14.6x 5/2 Cross-source
dispersionpreserved
Panel B. Pre-treatment parallel-trends joint Wald F-test
JointWaldF-teston7pre-periodcoeﬀicients(fullsample) F=1.54to23.72 n/a 6reject/1passatp
<0.05
OnlyComposite
Reweightedvariant
passes
parallel-trendstest
JointWaldF-teston5pre-periodcoeﬀicients(excluding
2020-2021)
F=1.35to11.27 n/a 6reject/1passatp
<0.05
Sameconclusionas
fullsample;
pre-trendtestrobust
toCOVID-period
exclusion
Panel C. Sample-restriction robustness
Fullsample(16-64) 0.010to0.222 22.4x 10/0 Baseline
Prime-age(25-54) 0.017to0.182 10.6x 7/0 Allnegative;
magnitudesdiverge
Non-Hispanicwhiteonly 0.026to0.177 6.7x 6/1 Cross-source
dispersionpreserved
Femaleonly 0.008to0.129 16.5x 2/5 Cross-source
dispersionpreserved
Panel D. Specification-sensitivity robustness (fixed effects and controls)
Baseline(year+state+occupationfixedeffects;fullcontrols) 0.010to0.222 22.4x 7/0 Allnegative;
magnitudesdiverge
Dropdemographiccontrols 0.024to0.221 9.1x 6/1 Robusttodropping
controls
State-by-yearsaturatedfixedeffects 0.009to0.222 25.4x 7/0 Robustto
state-by-yearfixed
effects
Dropyearfixedeffects 0.028to0.202 7.2x 7/0 Robust;allnegative
Dropoccupationfixedeffects 0.069to0.613 8.8x 3/4 Signflipswithout
occupationfixed
effects
Notes: This table summarizes the dispersion of the cross-source DiD coeﬀicient across ten canonical variants under four classes of robustness
perturbation, organized into four panels. Panel A reports outcome invariance (employment, labor-force participation, log wage, each in full and
excluding-2020-2021 samples). Panel B reports the pre-treatment parallel-trends joint Wald F-test (the F-statistic and pass/reject count at p <
0.05 for each variant). Panel C reports sample-restriction robustness (prime-age 25 to 54, non-Hispanic white only, female only). Panel D reports
specification-sensitivity robustness (alternative fixed-effects configurations and dropping demographic controls). Each row reports: the range of
beta-times-100 coeﬀicients across variants; the maximum-to-minimum absolute-magnitude ratio (a dispersion index where 1 means perfect cross-
source agreement and >10 means an order-of-magnitude or larger spread); the sign split (negative count / positive count among variants); and
a one-line interpretation. The 'Full' label indicates the full 2015 to 2024 sample; 'excluding 2020-2021' drops 2020 and 2021. The robustness
dispersion grid shows that cross-source dispersion is preserved under nearly all perturbations, motivating the manuscript's central conclusion that
platform-visibility distortion is the dominant source of variation in estimated treatment effects rather than specification choices. Abbreviations: SOC
= Standard Occupational Classification; AEI = Anthropic Economic Index; CAI = Claude.ai consumer; API = first-party Application Programming
Interface enterprise; Composite = AI exposure score constructed following Massenkoff and McCrory (2026) ; BBD = Bick-Blandin-Deming Survey
of Working Arrangements and Attitudes; BLS = Bureau of Labor Statistics; OES = Occupational Employment and Wage Statistics; CKK = Chen,
Kane, Kozlowski et al. (2025); ACS = American Community Survey; CPS-MORG = Current Population Survey-Outgoing Rotation Group.
60

Table B.9. Massenkoff-McCrory Cross-Occupation Regression Coeﬀicients by Platform Family
Exposure measure N Coef per SD (x100)
PanelA.M-Mbaselinecomposite: publishedanchorand
BLS-reweighted
M-Mbaselinecomposite(publishedanchor) 756 -70.09***
(17.90)
M-Mbaselinecomposite,BLS-reweighted(MM_RW) 766 -38.28**
(17.35)
PanelB.AnthropicClaude.aiconsumer(rawconversationshare)
AnthropicClaude.aiconsumerWave1(Dec2024) 582 +43.30
(33.64)
AnthropicClaude.aiconsumerWave2(Feb2025) 579 -8.16
(34.23)
AnthropicClaude.aiconsumerWave3(Aug2025) 538 -12.10
(35.08)
AnthropicClaude.aiconsumerWave4(Nov2025) 559 -28.12
(33.46)
AnthropicClaude.aiconsumerWave5(Feb2026) 561 -68.01**
(28.80)
PanelC.Anthropic1PAPIenterprise(rawconversationshare)
Anthropic1PAPIenterpriseWave3(Aug2025) 480 +27.61
(37.16)
Anthropic1PAPIenterpriseWave4(Nov2025) 485 +23.88
(36.38)
Anthropic1PAPIenterpriseWave5(Feb2026) 480 +34.00
(36.03)
PanelD.MicrosoftBingCopilot2024(rawconversationshare)
MicrosoftBingCopilot2024( Tomlinsonetal. 2025) 785 -150.04***
(24.00)
PanelE.Externalcross-platformsources(SOC-majoraggregated,
expandedtoNEM)
OpenAIChatGPT2024( Chatterjietal. 2025 ,
SOC-major-expanded)
1112 +174.00***
(13.61)
Bick,Blandin,andDeming(2026) ,RPSSOC-major-expanded 1091 +102.26***
(13.28)
Bick,Blandin,andDeming(2026) ,RPSsix-digitSOCmicro 270 +166.81***
(45.80)
Manskipartial-identificationboundson|CoefperSD|(x100)
Lowerbound: M-Mcomposite,BLS-reweighted 38.28
Upperbound: OpenAIChatGPT2024( Chatterjietal. 2025 ,
SOC-major-expanded)
174.00
Identified-setwidth 135.72
Notes: Each row reports the WLS coeﬀicient from a regression of 2024-2034 BLS occupational employment-projection growth on the platform's
AI exposure measure, weighted by 2024 occupational employment. Coeﬀicients are scaled per standard deviation of the exposure measure times
100, with employment-weighted standard errors in parentheses. The new RPS micro row at the bottom of Panel E reports the coeﬀicient on the
six-digit SOC workforce AI use rate from the pooled August and November 2024 micro release. The RPS is a national online survey conducted on
Qualtrics with awareness-adjusted demographic weights and is not a probability sample of the U.S. workforce. The sample for the RPS micro row
is restricted to the 270 SOC cells with at least five RPS respondents. *** p<0.01, ** p<0.05, * p<0.10.
61

Table B.10. Cross-Platform Substitution across Five Published Target Methods
Paper / target / substitute Value Delta from published N
PanelA.YaleBudgetLab(2025): top-quintileshare Top-quintileoccupational
employmentshare(%)
535
Originalpublished 16.40%
Ourreplication(YalePCAcomposite) 23.41% +7.01pp
Cross-platformsubstitutes(rawexposure):
Originalcompositescore 30.46% +14.06pp
Claude.aiconsumerWave1 30.34% +13.94pp
Claude.aiconsumerWave5 36.42% +20.02pp
1PAPIenterpriseWave5 37.65% +21.25pp
MicrosoftBingCopilot2024 22.65% +6.25pp
PanelB. Chen-Kane-Kozlowskietal. (2025): SDiDlogearnings SyntheticDiD
above-medianATTinJan
2010dollars/week
1,391,824
Originalpublished +$89.00/wk 353
Cross-platformsubstitutes(rawexposure):
Originalcompositescore +$57.79(w)/+$49.05(s) -$31.21(w)
CompositewithWave5AEIweights +$58.63(w)/+$48.00(s) -$30.37(w)
Claude.aiconsumerWave1 +$50.94(w)/+$67.68(s) -$38.06(w)
Claude.aiconsumerWave5 +$43.76(w)/+$51.17(s) -$45.24(w)
1PAPIenterpriseWave5 +$44.69(w)/+$62.72(s) -$44.31(w)
MicrosoftBingCopilot2024 +$16.67(w)/+$10.44(s) -$72.33(w)
PanelC. Brynjolfsson-Chandar-Chen(2025): Q5employment
growth
Percentage-pointchangein
employment,ages22-25
196
Originalpublished -10.00%[-8.00,-12.00]
Cross-platformsubstitutes(rawexposure):
1PAPIenterpriseWave5 -7.62%[-6.78,-8.46] +2.38pp
PanelD. MassenkoffandMcCrory(2026) ,CPSunemployment
DiD
Setoverlap(Jaccard)with
originaltop-quartile
treatment
245
Originalpublished(own-method) 1.00
Cross-platformsubstitutes(rawexposure):
Claude.aiconsumerWave1 0.19 -0.81
Claude.aiconsumerWave5 0.19 -0.81
1PAPIenterpriseWave5 0.21 -0.79
MicrosoftBingCopilot2024 0.28 -0.72
PanelE. Tomlinson,Jaffe,Wang,Counts,Suri(2025) : AI
applicability
Setoverlap(Jaccard)with
originaltop-quintile
occupations
192
Originalpublished(own-method) 1.00
Cross-platformsubstitutes(rawexposure):
Claude.aiconsumerWave5 0.20 -0.80
1PAPIenterpriseWave5 0.16 -0.84
Notes: Each panel reports a separate published target method and the result of substituting platform-derived AI-exposure inputs into that
method, holding the rest of the published specification fixed. Companion to main-text Table 5, which reports the analogous substitution exercise for
the BLS Employment Projections specification. Per the analytical correction documented in Section I, reweighted versions of the alternative-rubric
(Eloundou tau-alpha) exposures show unstable sign-flip behavior under occupation-level reweighting because the bias enters at the task level rather
than the occupation level. Only raw (baseline) cross-platform substitutes are reported here. Main-text Table 5 reports the𝜏𝑏 reweighting (reweighted composite score) which is methodologically appropriate for the BLS Projections specification alone. Yale Budget Lab (Panel A): published exposure
is a principal components composite across multiple AI inputs; we replicate at 6-digit Standard Occupational Classification level (n=535) and
substitute platform-derived exposure inputs. CKK (Panel B): synthetic DiD on monthly Current Population Survey Outgoing Rotation Group data;
the +$89/wk anchor is not reproduced within the +/-5 percent tolerance because of methodology differences (per-treated-unit balanced donor
pool retains four of thirty-three post-period months; exposure-metric difference between Anthropic Economic Index conversation share and Handa
task-coverage aggregation). BCC (Panel C): only one substitute reported because the rest of the platform inputs were not aggregated to the BCC
age-restricted occupation sample. Massenkoff and McCrory CPS (Panel D) and Tomlinson Jaccard (Panel E): set-overlap (Jaccard) statistics rather
than coeﬀicient substitution; report the fraction of top-quartile (Massenkoff and McCrory CPS) or top-quintile (Tomlinson) occupations preserved
across the substitution. Significance stars and standard errors are not reported because the underlying methods use heterogeneous estimators
(PCA composite for Yale; synthdid jackknife for CKK; DiD with bootstrapped intervals for BCC; set-overlap for Massenkoff and McCrory CPS and
Tomlinson).
62

Table B.11. Diagnostic Evidence on the Composition ( 𝜓) versus Behavior (𝜃) Channels in Cross-Wave Instability
Panel A. Within-Occupation Task-Share Stability (Spearman 𝜌)
Wave pair N occupations Mean 𝜌 Median 𝜌 Share with 𝜌 > 0.7
Waves3to4(Projects+Sonnet4to4.5) 404 0.683 0.800 65.3%
Waves4to5(Opus4.6minorrefresh) 411 0.863 0.943 87.8%
Waves3to5(acrossproductcycle) 403 0.700 0.808 67.0%
ComputerandMathematical(SOC15)subset:
Waves3to4 18 0.866 0.898 94.4%
Waves4to5 18 0.912 0.967 94.4%
Waves3to5 18 0.901 0.896 100.0%
Panel B. Conversation-Share Compositional Shifts at Wave Transitions
Wave pair
Product event between
waves Six-digit SOC L1 SOC-major L1 SOC 15 share change
Waves1to2 Sonnet3.5to3.7minor
refresh
33.73pp 10.58pp +0.26pp
Waves2to3 ClaudeCodelaunch 45.92pp 11.29pp +4.27pp
Waves3to4 Projectsexpansion+Sonnet
4to4.5
27.91pp 12.15pp -2.33pp
Waves4to5 Opus4.6minorrefresh 20.51pp 14.45pp -4.48pp
Panel C. Sub-Occupation Heterogeneity in Computer and Mathematical (SOC 15) Major-Group Share Movement
Wave pair N sub-occupations Mean growth ratio Cross-sub-occ CV SOC 15 share change
Waves1to2 21 1.019 0.396 +0.26pp
Waves2to3 21 1.415 0.848 +4.27pp
Waves3to4 21 0.985 0.315 -2.33pp
Waves4to5 21 1.046 0.200 -4.48pp
Waves1to3(acrossClaudeCodelaunch) 21 1.274 0.988 +4.53pp
Notes: Panel A reports the Spearman rank correlation between within-occupation task-share distributions in two Anthropic Economic Index waves, computed for each six-digit Standard Occupational
Classification (SOC) occupation with at least three tasks. Within-occupation task share is the share of each O*NET task in total Claude.ai consumer conversations attributed to that occupation (global
geographic aggregation). The Computer and Mathematical subset is reported separately. Waves 1 and 2 use a different raw task-level aggregation and are not directly comparable to the W3 to W5 window.
Panel B reports cross-wave compositional shifts at each consecutive wave-pair transition. L1 distance is the sum of absolute share changes across all occupation cells (six-digit SOC, or 22 SOC major
groups) between the two waves. The SOC 15 share change is the percentage-point movement in the Computer and Mathematical major-group share of total Claude.ai consumer conversations. Panel C
decomposes the cross-wave movement of the SOC 15 share into its six-digit sub-occupation components. For each wave pair, the growth ratio is the wave-(k+1) sub-occupation share divided by the wave-k
share, computed within each SOC 15 sub-occupation with positive share in both waves; the cross-sub-occupation coeﬀicient of variation is the standard deviation of growth ratios divided by their mean.
A coeﬀicient of variation near zero would indicate proportional growth across sub-occupations (consistent with within-occupation behavior-channel 𝜃 effects acting uniformly); a coeﬀicient of variation
well above zero indicates heterogeneous growth and is consistent with cross-occupation composition-channel 𝜓 effects driven by new-user entry into specific sub-occupations. The three sub-occupations
contributing the largest positive share change between Waves 1 and 3 are Database Architects (2.2×); Software Developers (1.8×); Software Quality Assurance Analysts and Testers (1.1×). Cluster-robust
standard errors for the corresponding wave-by-wave reweighted DiD are reported in Table 4.
63

Table B.12. Bick, Blandin, and Deming (2026) Real-Time Population Survey Micro Release
Panel A. RPS AI use rates at work, by SOC major group
SOC Major Group N Use at work (ever)
Use at work (last
wk) Use at work (daily)
Management 1363 0.524 0.468 0.158
ComputerandMathematical 544 0.547 0.463 0.146
BusinessandFinancial 475 0.477 0.399 0.095
Farming,Fishing,Forestry 57 0.388 0.345 0.048
Education,Training,Library 304 0.399 0.340 0.065
HealthcarePractitioners 300 0.372 0.292 0.134
ConstructionandExtraction 284 0.353 0.280 0.084
Arts,Entertainment,Sports,Media 265 0.340 0.278 0.079
ArchitectureandEngineering 150 0.313 0.274 0.094
CommunityandSocialService 157 0.295 0.249 0.026
Life,Physical,SocialScience 95 0.319 0.211 0.040
Sales 536 0.256 0.201 0.043
Installation,Maintenance,Repair 171 0.315 0.195 0.060
OﬀiceandAdministrativeSupport 656 0.227 0.195 0.046
Production 354 0.262 0.193 0.033
HealthcareSupport 287 0.181 0.150 0.016
BuildingandGroundsCleaning 142 0.230 0.140 0.038
PersonalCare 180 0.158 0.137 0.000
ProtectiveService 68 0.133 0.133 0.010
TransportationandMaterialMoving 303 0.167 0.126 0.044
Legal 68 0.198 0.124 0.006
FoodPreparation 263 0.096 0.075 0.008
Panel B. AI product shares among at-work AI users, n = 1,785
AI Product National share
ChatGPT 0.731
Gemini 0.460
Embedded 0.403
GitHubCopilot 0.173
Claude 0.123
Midjourney 0.120
DALL-E 0.072
Perplexity 0.063
Scribe 0.052
Other 0.049
Synthesia 0.037
Panel C. Between-occupation alignment of platform user base with RPS use rate
Platform Spearman rho p-value N occupations
Claude.aiconsumer(Wave5) +0.389 <0.001 239
1PAPIenterprise(Wave5) +0.279 <0.001 216
MicrosoftCopilot +0.252 <0.001 270
Notes: The RPS is a national online survey of working-age adults conducted on Qualtrics with awareness-adjusted demographic weights. It
is not a probability sample of the U.S. workforce. Panel A reports weighted AI use rates at work by SOC major group from the pooled August
and November 2024 micro release. Panel B reports the share of at-work AI users employing each AI product, n = 1,785, with multiple products
per respondent permitted. Panel C reports the between-occupation Spearman correlation between the platform-to-workforce density ratio psi (per-
occupation platform share divided by OEWS workforce share) and the RPS at-work AI use rate at the six-digit SOC level. Sample for Panel C
restricted to SOC cells with at least five RPS respondents.
64

Figure B.1. Holm-Bonferroni and Benjamini-Hochberg forest plot for the fifteen-outcome
cross-domain family.

 
   
5 DQNFRUUHODWLRQJDS o = AEI BLSQ 62 & P DMRUJURXSV ERRWVWUDS& ,

/RJUHDOKRXUO\ZDJHV
6KRUWVOHHSSUHYDOHQFH
&XUUHQWVPRNHUSUHYDOHQFH
.VHYHUHGLVWUHVVSUHYDOHQFH
%DFKHORU
VRUKLJKHUVKDUH
+LJKVFKRRORUOHVVVKDUH
(YHUVPRNHUSUHYDOHQFH
3DVW\HDUGULQNHUSUHYDOHQFH
'ULQNVSHUGD\LQWHQVLW\
+RXUVZRUNHGPHDQZHHNO\

/DERUIRUFHSDUWLFLSDWLRQUDWH
(PSOR\PHQWLQGLFDWRU
'LVDELOLW\SUHYDOHQFH
6RPHFROOHJHVKDUH
6HOIUDWHGKHDOWKIDLUSRRU
















8QDGMXVWHGS 0 DUJLQDO S
 1RWVLJQLILFDQW =HURHIIHFW
Notes: Each row is one of fifteen occupation-level outcomes drawn from the ACS 2011-2022 and NHIS Sample Adult 2017-
2018, ordered by absolute Spearman rank-correlation gap Δ𝑜 = 𝜌 𝐴𝐸𝐼 − 𝜌𝐵𝐿𝑆 at the 22 SOC major-group level (n=22).
Horizontal bars are 95-percent cluster-bootstrap CIs from 5,000 replications. Red filled circles mark unadjusted-significant
outcomes (p<0.05); navy filled squares mark marginal outcomes (0.05 ≤ p<0.15); light gray hollow circles mark not signif-
icant. Under Holm-Bonferroni FWER=0.05, zero outcomes survive; under BH-FDR q=0.10, zero survive; under BH-FDR
q=0.20, seven outcomes survive.
65

Figure B.2. SOC major-group rank trajectories across five Anthropic Economic Index waves.
Wave 1
Dec 2024
Wave 2
Feb 2025
Wave 3
Aug 2025
Wave 4
Nov 2025
Wave 5
Feb 2026
Q1 — highest AI exposure
Q2
Q3
Q4
Q5 — lowest AI exposure
Management Management
Business & Financial
Business & Financial
Computer & Math Computer & Math
Life, Physical & Soc. Sci. Life, Physical & Soc. Sci.
Education & Library
Education & LibraryArts, Design & Media
Arts, Design & Media
Healthcare Practitioners Healthcare Practitioners
Healthcare Support
Healthcare Support
Protective Service Protective Service
Building & Grounds
Building & Grounds
Office & Admin Office & Admin
Installation & Repair
Installation & Repair
Transportation
Transportation
Food Prep & Serving
Food Prep & Serving  ↑2
Personal Care
Personal Care  ↑4
Sales & Related
Sales & Related  ↑5
Farming, Fishing & Forestry
Farming, Fishing & Forestry  ↑5Construction
Construction  ↓4
Architecture & Eng
Architecture & Eng  ↓4
Production
Production  ↓5
Community & Social Service
Community & Social Service  ↑3
Legal
Legal  ↓3
Within Claude.ai alone, 9 of 22 occupation groups crossed a quintile between Wave 1 (Dec 2024) and Wave 5 (Feb 2026)
Bluish-green: climbers (gained AI-exposure rank).   Vermillion: fallers.   Gray: 13 groups that stayed inside their Wave 1 quintile.
Δ on right edge = net rank change W1 → W5.   Vertical orange shading marks Claude Code launch (Mar 2025), between Waves 2 and 3.
Notes: Each line tracks one SOC major group’s Anthropic Claude.ai conversation-share rank across the five publicly released
AEI waves (Wave 1 December 2024 through Wave 5 February 2026). Rank 1 = highest share; rank 22 = lowest. Vertical
reference lines mark the Claude Code launch (between Waves 2 and 3) and the Claude Projects expansion (between Waves 3
and 4), the two product events that drove the largest cross-wave compositional shifts.
66

Figure B.3. Economic vulnerability versus platform visibility across 95 detailed occupations.
0.01 0.1 1 10
←  Underrepresented           Platform visibility  ψ = Claude share  /  BLS share   (log scale)           Overrepresented →
−2
−1
0
1
2
3
Economic vulnerability  z-score
(low BA + low wage + high disability)
ψ = 1
Invisible + vulnerable
Workers the AI debate ignores —
low BA, low wage, often physically demanding;
the platform barely registers them.
Visible + privileged
Workers loudest in AEI data —
high BA, high wage, professional jobs;
the platform amplifies them many-fold.
Invisible but cushioned
(pilots, executives, lawyers)
Visible but exposed
(counselors, social workers, tour guides)
Food processing
Textile & apparel
Plant & system operators
Agricultural workers
Grounds maintenance
Architects &
surveyors
Operations specialty mgrs
Business operations
specialists
Religious workers
Tour & travel guides
Art & design workers
Personal-care supervisors
Home health &
nursing aides
Warehouse &
material movingJanitors &
building cleaners
Cooks
Other
food prep
Food &
beverage servers
Bus, taxi & truck
drivers
Construction
trades
Computer
occupationsMathematical
science
Media &
communication
Life sciences
Air transport
(pilots)
Top executives
Lawyers &
judges
Engineers
Counselors &
social workers
Overall: Spearman ρ(visibility, vulnerability) = -0.52    (N = 95 SOC-minor groups, p = 7.0e-08)
Technology & science Office & professional Service & care Manual labor Healthcare W1 →  W5 trajectory Marker size ∝ √ BLS share
Notes: Horizontal axis: economic vulnerability index combining wage rank, displacement risk, and unemployment-insurance recipiency. Vertical axis: platform-visibility
share (Anthropic Wave 5 Claude.ai conversation share divided by BLS OES employment share). Each point is one of the 95 most-populous six-digit SOC occupations. The
lower-left quadrant (high vulnerability, low visibility) contains occupations whose DiD coeﬀicient inherits the largest user-base bias.
67

Figure B.4. Occupational composition and demographic profile across the 95 most-populous detailed
SOC occupations.
Notes: Each row is one of the 95 most-populous six-digit SOC occupations ranked by BLS workforce employment. Cells report
the BLS workforce share, Anthropic Wave 5 Claude.ai conversation share, over-representation ratio 𝜓, and demographic
composition from ACS 2024. The over-representation ratio𝜓 exceeds ten for several Computer and Mathematical occupations
and falls below 0.05 for Transportation, Food Preparation, and Construction occupations.
68

Figure B.5. Occupation rank flow from platform-derived to workforce-reweighted exposure rankings.
Notes: Alluvial flow diagram of rank movement at the six-digit SOC level. Left axis: Anthropic Wave 5 Claude.ai conversation-
share ranking. Right axis: Composite Reweighted ranking. The top decile under the unreweighted ranking is dominated by
Computer and Mathematical occupations; under reweighting, that decile shifts toward Oﬀice and Administrative Support,
Sales, and Customer Service occupations.
69

Figure B.6. Within-platform heterogeneity in the post-2023 employment coeﬀicient across fifteen demographic and occupation subgroups.
−0.8 −0.6 −0.4 −0.2 0.0 0.2 0.4
DiD coefficient ̂β × 100 on employment
Has disability
No disability
Bachelor's degree or higher
Less than bachelor's degree
Female
Male
Non-Hispanic white
Non-Hispanic Black
Hispanic
Wage quartile 1 (lowest)
Wage quartile 4 (highest)
Management and Professional
Service
Sales and Office
Blue-collar
Panel A. Full sample (2015-2024)
Disability
Education
Sex
Race and ethnicity
Wage quartile
Occupation major group
−0.8 −0.6 −0.4 −0.2 0.0 0.2 0.4
DiD coefficient ̂β × 100 on employment
Panel B. Excluding 2020-2021
Composite Reweighted (benchmark) Baseline Composite (Anthropic) Claude.ai consumer (Wave 5) 1P API enterprise (Wave 5) Microsoft Copilot
Notes: Forest plot of post-2023 DiD coeﬀicient (𝛽×100 ) on the employment indicator from equation (7). Panel A: full sample. Panel B: excluding 2020 and 2021. Subgroups
are stratified by disability, education, sex, race-ethnicity, wage quartile, and occupation major group. Five exposure variants plotted per subgroup: Composite Reweighted
(red open circle, benchmark), Baseline Composite (Anthropic) (open triangle), Claude.ai consumer Wave 5 (filled square), 1P API Wave 5 (open diamond), Microsoft Copilot
raw (open inverted triangle). Bars are 95-percent cluster-robust CIs at the six-digit SOC.
70

Figure B.7. Three measures per SOC major group from the RPS micro release.
      
6KDUHRUUDWH
)RRG3UHSDUDWLRQ
/HJDO
2IILFHDQG$GPLQLVWUDWLYH6XSSRUW
7UDQVSRUWDWLRQDQG0DWHULDO0RYLQJ
3URWHFWLYH6HUYLFH
3HUVRQDO&DUH
%XLOGLQJDQG*URXQGV&OHDQLQJ
+HDOWKFDUH6XSSRUW
6DOHV
3URGXFWLRQ
,QVWDOODWLRQ0DLQWHQDQFH5HSDLU
/LIH3K\VLFDO6RFLDO6FLHQFH
&RPPXQLW\DQG6RFLDO6HUYLFH
$UFKLWHFWXUHDQG(QJLQHHULQJ
$UWV(QWHUWDLQPHQW6SRUWV0HGLD
+HDOWKFDUH3UDFWLWLRQHUV
&RQVWUXFWLRQDQG([WUDFWLRQ
(GXFDWLRQ7UDLQLQJ/LEUDU\
%XVLQHVVDQG)LQDQFLDO
)DUPLQJ)LVKLQJ)RUHVWU\
0DQDJHPHQW
&RPSXWHUDQG0DWKHPDWLFDO
%LFN%ODQGLQDQG'HPLQJ

536DWZRUN$,XVHUDWH &ODXGHDLFRQVXPHU:DYHFRQYHUVDWLRQVKDUH 2(:6ZRUNIRUFHVKDUH
Notes: Each row reports three points by SOC major group, ordered by spread (max minus min) descending. The red circle is
the RPS at-work AI use rate from the pooled August and November 2024 micro release. The blue diamond is the Anthropic
Claude.ai consumer Wave 5 conversation share. The gray square is the OEWS workforce employment share. The thin gray
line connects the minimum and maximum across the three measures, indicating the spread within each occupation.
71

Online Appendix C. Implied Incidence of a Retraining Program (Policy Simulation)
Toillustratethepolicyimplicationsoftheplatform-selectionbiasdocumentedinthemaintext,weconducta
hypothetical$10-billionAIretrainingfundallocationexercise. Tworulesarecompared. Undertheplatform-
weightedrule,theallocationfollowsAnthropicWave5Claude.aiconversationshares: occupationswiththe
highest platform exposure receive proportionally more retraining dollars. Under the workforce-reweighted
rule,theallocationfollowsBLSMay2024OEWSemploymentshares: dollarstrackwhereworkersare,not
whereplatformconversationsare.
Theplatform-weightedruleredirectsapproximately$3.87billion(39percentofthefund)tooccupations
with above-median wages and Bachelor’s-degree-or-higher shares above 60 percent, primarily Computer
and Mathematical, Business and Financial Operations, and Oﬀice and Administrative Support occupations.
Theworkforce-reweightedruledirectsthesamedollarstowardmiddle-wageoccupationswithBachelor’s-or-
highersharesclosertotheworkforcemean,primarilySales,OﬀiceSupport,Transportation,Production,and
FoodPreparation.
Figure C.1 visualizes the incidence shift. The platform-weighted bars show a redistribution of dollars
toward high-skill occupations; the workforce-reweighted bars match the underlying workforce composition.
The$3.87-billionshiftistheimpliedcompositionalbiaswhenapolicymakerusesplatform-derivedexposure
as an allocation key without workforce reweighting. The exercise treats the platform-weighted rule as a
benchmark for what would happen if the published Anthropic conversation shares were taken as a direct
measureoftrainingneed,holdingtotalprogramdollarsfixed.
The simulation is illustrative rather than prescriptive. The Bureau of Labor Statistics workforce distri-
bution is the relevant denominator if the policy aim is workforce-wide coverage, but a policy specifically
targeting workers most likely to be affected by AI productivity gains may have different weighting objec-
tives. The $3.87-billion gap quantifies the magnitude of the user-base channel in a concrete dollar amount
andisolatesthecompositionalcomponentfromthesubstantivequestionofhowAIexposuremapstoretrain-
ingneed.
72

Figure C.1. Implied incidence of a hypothetical $10-billion AI retraining fund (policy simulation).
Notes: Each bar reports the share of the $10-billion fund directed to a SOC major-group bin under two allocation
rules. The platform-weighted rule allocates dollars in proportion to Anthropic Wave 5 Claude.ai conversation shares;
the workforce-weighted rule allocates in proportion to BLS May 2024 OEWS employment shares. The platform-weighted
rule directs approximately $3.87 billion (39 percent) to high-wage, high-education occupations; the workforce-weighted
rule directs the same dollars to middle-wage occupations with workforce-mean education shares.
73
