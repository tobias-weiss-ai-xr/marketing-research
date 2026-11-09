---
title: 'A Systematic Literature Review on the Impact of Generative AI in Digital Marketing: Advancements,
  Opportunities, and Challenges'
url: https://doi.org/10.32604/cmc.2026.071029
category: ai-marketing
subcategory: empirical
date: 2026-01
venue: Computers, materials & continua/Computers, materials & continua (Print)
authors:
- Arifur Rahman
- MD Azam Khan
- Farhad Uddin Mahmud
source: openalex-oa
pdf_url: https://cdn.techscience.press/files/cmc/2026/TSP_CMC-87-3/TSP_CMC_71029/TSP_CMC_71029.pdf
pages: 45
chars: 138920
fetched_at: '2026-11-08T17:01:30+00:00'
kb_version: 1
---

# A Systematic Literature Review on the Impact of Generative AI in Digital Marketing: Advancements, Opportunities, and Challenges

echT PressScience
https://doi.org/10.32604/cmc.2026.071029
REVIEW
ASystematicLiteratureReviewontheImpactofGenerativeAIinDigital
Marketing:Advancements,Opportunities,andChallenges
ArifurRahman1,M DA z a mK h a n1, FarhadUddinMahmud 1, KanchonKumarBishnu2,
AshifurRahman3,M.F .Mridha4,* andMd.JakirHossen 5,*
1SchoolofBusiness,InternationalAmericanUniversity,LosAngeles,CA,USA
2DepartmentofComputerScience,CaliforniaStateUniversity,LosAngeles,CA,USA
3DepartmentofComputerScienceandEngineering,Banglades hUniversityofBusinessandTechnology,Dhaka,Bangladesh
4DepartmentofComputerScienceandEngineering,American InternationalUniversity-Bangladesh,Dhaka,Bangladesh
5CenterforAdvancedAnalytics(CAA),FacultyofEngineeringandT echnology(FET),MultimediaUniversity,Melaka,Malaysia
*CorrespondingAuthors:M.F.Mridha.Email:firoz.mridha@aiub.edu;Md.JakirHossen.Email: jakir.hossen@mmu.edu.my
Received:30July2025;Accepted:21October2025;Published:09April2026
ABSTRACT: Generative Artificial Intelligence (AI) is reshaping digital marketing by creating automated content,
personalizing campaigns, and offering new ways to engage consumers. This systematic review examines research on
generative AI, highlighting both its technological progress and the ethical, technical, and organizational hurdles that
could limit its use. We used a PRISMA-based method to search major databases (ACM Digital Library, IEEE Xplore,
and Scopus) for peer-reviewed studies published from 2018 to 2025. Our findings reveal major gains in text creation,
image generation, and multimodal campaigns, which can lower costs and spark creative thinking. Still, data privacy,
biasinmodels,andlawsaroundcomplianceshowtheneedforclearandresponsibleadoption.Bybringinginideasfrom
InnovationDiffusionTheoryandtheTechnologyAcceptanceModel,thisreviewshowshoworganizationalcultureand
perceived value interact with ethical frameworks to shape how generative AI tools take hold. We provide insights for
marketerswhowanttoapply generativeAIinaresponsiblewayandsetapathforfutureresearchaimedatprotecting
consumertrust.
KEYWORDS:GenerativeAI;digitalmarketing;contentgeneration;personalization;ethicalAI;technologyadoption;
innovationdiffusiontheory;transformermodels
1I n t r o d u c t i o n
GenerativeArtificialIntelligence(AI)hasrapidlyemergedasatransformativeforceindigitalmarketing,
driving advancements in content creation, personalized campaigns, and consumer engagement [1,2]. As
marketers strive to adapt to the increasing digital competition and evolving consumer behavior, generative
AI offers innovative tools for creating, personalizing, and disseminating content on an unprecedented
scale [3,4]. This technology, underpinned by advancements in deep learning architectures such as trans-
formers [5], Generative Adversarial Networks (GANs) [6], and diffusion models [7], is redefining digital
marketingstrategiesbyshiftingfrompredictiveanalyticstocreativeapplications.
Thedigitalmarketinglandscapehasundergoneasignificanttransformationoverthelastdecade,transi-
tioningfrombasicbanneradsandemailcampaignstosoph isticated,data-drivenstrategiesacrossplatforms
such as social media, search engines, and mobile applications [8,9]. This shift has been accompanied by a
Copyright © 2026 The Authors. Published by Tech Science Press. This work is licensed under a Creative Commons Attribution 4.0 International
License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

2 ComputMaterContin. 2026;87(3):11
massive increase in user data generation, including click histories and social media interactions, enabling
marketers to leverage intelligent, automated tools for impactful campaigns. Generative AI now empowers
brands to design marketing assets such as text, images, and videos, automating processes like customer
support and personalized messaging while reducing costs and accelerating campaign development [10,11].
Forexample,languagemodelssuchasGPTarecapableofcraftingemailheadlinestailoredtoindividualuser
preferences,whileGANscangeneratenewproductimagestosupportmarkettesting[ 12].GenerativeAInot
only analyzes consumer data but actively shapes brand interactions and consumer influence. Its ability to
adapt content to specific demographics, languages, or cultural contexts within moments enables dynamic,
real-timemarketingcampaignsthatalignwithrapidlychangingonlinediscourse[ 13,14].
Generative AI stands apart within the broader field of artificial intelligence due to its ability to create
new content that is not directly extracted from training data [15,16]. Unlike predictive analytics, which
focusesonforecastingoutcomesbasedonhistoricaldata,orrule-basedsystemsthatrelyonexplicitlycoded
instructions,generativeAIautonomouslyconstructspatternsandfeaturesfromdata,enablingnovelcontent
creation [17]. In digital marketing, this includes applications such as language generation, image synthesis,
andmultimodalsystemsthatseamlesslyintegratetext,sound,andvisualsintocohesivecampaigns.
DespitetherapidadoptionofgenerativeAI,muchoftheexistingliteratureonAIinmarketingremains
fragmented and focused on predictive models like recommendation systems or churn analysis [18–20].
Comprehensive empirical studies on generative AI’s applications, encompassing text, image, and video
creation,arescarce.Additionally,ethicalandpracticalconsiderationssuchasdataprivacy,contentbias,and
accountability are often underexplored in the context of regulatory frameworks like GDPR or the AI Act in
the European Union. Addressing these challenges is critical to realizing the potential of generative AI for
responsibleandsustainabledeployment.Tobetterunderstandthestateoftheart,acomparativeanalysisof
existingsurveypapersissummarizedin Table 1.ThistablereviewsnotableworksongenerativeAIindigital
marketingandrelatedfields,evaluatingtheirscope,contributions,andlimitations.Ithighlightstheareasof
focusandidentifiesgaps,providingaroadmapforfutureexploration.
Table 1:ReviewofexistingsurveypapersonGenerativeAIindigitalmarketingandrelateddomains.
Ref. Year Systematic Review Technological Advancements Results Analysis Ethical Concern Challenges &Future Work Contribution Limitations
[21]2 0 2 5 ×✓× ✓ ✓
Thisresearchoffersa
comprehensivereviewof
AImodelsindigital
marketing,identifying
keychallengesand
opportunities.It
providesuniqueinsights
throughaqualitative
descriptive approach,
enhancing
understandingofAI’s
roleinpersonalization,
automation,andstrategy
developmentwhile
emphasizingtheethical
andorganizational
factorsinfluencing
adoption.
Thestudy’smain
limitationsincludea
lackofempirical
evidenceonAI’s
real-world marketing
impactand
insufficient
explorationofethical
and regulatory
challenges.
Additionally,
conversationalAI’s
difficultywith
complexlanguage
nuancesmayaffect
userinteractions,
highlightingareas
requiringdeeper
investigationfor
practical and
responsible
implementation.
(Continued)

ComputMaterContin. 2026;87(3):11 3
Table 1 (continued)
Ref. Year Systematic Review Technological Advancements Results Analysis Ethical Concern Challenges &Future Work Contribution Limitations
[22]2 0 2 5 ×✓× × ✓
Thisresearchhighlights
thesignificantpotential
of digital marketing in
B2Bbusinessesand
identifieskey
opportunities and
challenges.Itproposes
practical
recommendationssuch
asusingChatBots,
analyticaltools,and
regulatory assessments
toimprovecustomer
engagement,ensure
compliance,and
strengthenmarketing
effectivenesswithinthe
B2Blandscape.
Thestudyislimited
by time and budget
constraints,which
prevented site visits
andstakeholder
interviewsatB2B
companies.These
omissionsmayhave
restrictedthedepthof
insightsand
real-worldvalidation
andcouldlimitthe
practicalapplicability
and
comprehensivenessof
thefindings.
[23]2 0 2 4 ×✓× × ✓
Thisstudyexplores
ChatGPT’srolein
marketing,highlighting
its ability to enhance
personalization,
improvecustomer
experience,andboost
ROI.Italsoexamines
theoreticalframeworks,
future research avenues,
andethical
considerationsinAI
adoptionformarketing.
Thisstudyisnota
systematicreviewand
lacksar esul ts-based
analysis. It is confined
tomarketing,limiting
generalizability.
Theoretical
frameworksmaynot
apply across contexts,
andpractical
challenges,ethical
concerns,and
unintended
consequencesof
ChatGPTadoption
areinsufficiently
addressed.
[24]2 0 2 3 × ✓ ×××
Thispaperexploresthe
implicationsof
generativeAIin
marketing,addressing
ethical concerns, its
impactonmarketing
strategies,andtheneed
forcross-disciplinary
collaborationtoleverage
AItechnologieslike
ChatGPTandStable
Diffusioneffectively.
Thispaperlacks
empiricaldatato
supportitsclaims,
focuseso nthe
negativeaspectsof
generativeAI,and
providesalimited
analysisofdark
marketingand
adaptationstrategies
fororganizations,
potentiallyofferingan
imbalancedviewof
thetechnology’s
impact.
(Continued)

4 ComputMaterContin. 2026;87(3):11
Table 1 (continued)
Ref. Year Systematic Review Technological Advancements Results Analysis Ethical Concern Challenges &Future Work Contribution Limitations
[25]2 0 2 3 × ✓ ×××
Thispaperoffersa
comprehensive
bibliometricanalysisof
211references,identifies
keyAItrends indigital
marketing,suggests
future research
directions,andprovides
practicalinsightsfor
businessesaimingto
enhancetheirdigital
marketingstrategies
usingAI.
Thisstudy’sscopeis
limitedbythe
literature reviewed,
whichmayexclude
recentadvancements
inGenerativeAI.
Potentialbiasesin
sourceselectionand
therapidevolutionof
AItechnologiesmay
alsoaffectthe
long-termrelevance
andreliabilityofthe
findings.
Ours – ✓ ✓ ✓✓✓
Thisstudyprovidesa
comprehensiveand
systematicreviewof
generativeAI
applicationsindigital
marketing,integrating
technological
advancements,ethical
concerns,andreal-world
usecases.Italso
proposes actionable
insightsandaroadmap
for future
interdisciplinary
research to enhance the
responsibleadoptionof
generativeAI.
Thisstudymayface
limitationsin
generalizabilitydueto
thedynamicand
rapidlyevolving
natureofgenerative
AItechnologies.
This review aims to bridge these gaps by synthesizing current research, examining the transformative
potentialofgenerativeAI,andexploringthechallengesassociatedwithitsadoption.Itevaluatesreal-world
applications,highlightsopportunitiesforpersonalizedandadaptivecontentgeneration,anddiscussesethical
concerns and regulatory issues. By integrating theoretical models such as the Innovation Diffusion Theory
andtheTechnologyAcceptanceModelwithcontemporaryethicalframeworks,thereviewprovidesaholistic
understanding of the intersection between technology, organizational culture, and societal implications.
Throughthiscomprehensiveanalysis,thereviewseekstoempowermarketingpractitionersandresearchers
with the insights needed for responsible innovation and strategic implementation in the dynamic realm of
digitalmarketing.
Inparticular,thisreviewcontributestothefieldbyofferingastructuredsynthesisofexistingliterature,
highlighting underexplored areas in the practical deployment of generative AI, and proposing a multidis-
ciplinary framework to guide future research and practice. By aligning theoretical insights with empirical
casestudies,thepapernotonlyidentifiesprevailingtrendsbutalsounderscorestheimplicationsforethical
governance and strategic decision-making. These contributions are framed around several key research
questions,assummarizedinthe Table 2.

ComputMaterContin. 2026;87(3):11 5
Table 2:Summaryofresearchquestionsaddressedinthisreview.
SN. ResearchQuestion Addressedin
RQ1
WhataretherecentadvancementsingenerativeAI
applications(e.g.,textgeneration,imagesynthesis,
multimodalcampaigns)fordigitalmarketing?
Section3,and Table 1
RQ2
Howarereal-worldusecasesutilizinggenerativeAIto
developcost-effective,scalable,andpersonalized
marketingstrategies?
Section4.4
RQ3
Whatarethecriticalethicalchallenges(e.g.,dataprivacy,
modelbias,regulatorycompliance)ingenerativeAI
adoptionformarketing?
Sections5 and5.3
RQ4
HowdotheoreticalmodelslikeInnovationDiffusion
TheoryandTechnologyAcceptanceModelexplain
organizationaladoptionofgenerativeAItools?
Sections3 and4
RQ5
Whatarethecurrentgapsinliterature,andhowcan
future interdisciplinary research address these for
responsibleinnovationindigitalmarketing?
Sections5 and6
The rest of the paper is organized as follows:Section2 details the systematic review methodol-
ogy.Section3 addressesthebackgroundandtheoreticalunderpinnings. Section4 explorescurrentfindings
andtrends. Section5 providesacriticaldiscussionoftheresults,and Section6 concludesthepaper.
2M e t h o d o l o g y
This section outlines the systematic literature review (SLR) methodology adopted to explore and
synthesize the existing research on generative AI in digital marketing. Our goal was to ensure both
transparencyandreplicabilityinthestudyselectionandanalysisprocess.FollowingcommonSLRguidelines
(PRISMA as present inFig.1), we detail each phase: from designing search strategies to screening, quality
assessment,anddataextraction.
2.1 ResearchDesign
We employed a methodical approach to capture a comprehensive set of academic and gray literature
addressing generative AIwithin thedigital marketingcontext. The research design covered three major
phases:
1. PlanningtheReview:Identificationofresearchquestions,keywords,anddatabasestobesearched.
2. ConductingtheReview:Systematicsearching,screeningofstudiesagainstinclusion/exclusioncriteria,
andqualityappraisal.
3. Reporting the Review: Data extraction, synthesis of key themes, and presentation of findings in
subsequentsections.
In addition, we acknowledge that ChatGPT was used solely for writing refinement and language
polishing.Itsrolewaslimitedtoimprovingreadabilityandgrammarwithoutinfluencingtheresearchdesign,
analysis,orinterpretation.AllAI-assistedtextwasthoroughlyreviewedandrevisedmanuallybytheauthors
toensureaccuracyandappropriateness.

6 ComputMaterContin. 2026;87(3):11
Figure1: PRISMA-basedflowdiagramillustratingthestudyselectionandscreeningprocess.
Ourmainresearchquestions(RQs),asstatedintheIntroduction,focusedon:
• RQ1:What is the current state of generative AI applications in digital marketing?
• RQ2:WhatopportunitiesandbenefitsdoesgenerativeAIpresenttodigitalmarketers?
• RQ3:What key challenges, limitations, and ethical considerations arise when deploying generative AI
inmarketingcontexts?
2.2 SearchStrategy
2.2.1DatabasesandSourcesConsulted
Tocapturebothcomputerscienceandmarketingperspectives,wesearchedmajoracademicdatabases
andscholarlyplatforms,including:
•A C M D i g i t a l L i b r a r y
• IEEEXplore
• Scopus
• Google Scholar (for potential gray literature or conference proceedings not indexed in the above
repositories).

ComputMaterContin. 2026;87(3):11 7
Weaugmentedthesesourcesbyinspectingrelevantjournalsandconferenceproceedings(e.g., AI,Cor-
porateSocialResponsibility,andMarketinginModernOrganizations ,ACMComputing Surveys,International
Journal of Information Management,IEEETransactionsonKnowledgeandDataEngineering ,amo ngo thers)
thatfrequentlyfeaturearticlesonAI-drivenmarketinginnovations.
2.2.2SearchTermsandQueryFormulation
Building on the research objectives, we developed a query string combining synonyms and Boolean
operators.Coresearchtermsincluded:
“GenerativeAI”OR“GenerativeAdversarialNetwork”OR“GPT”OR“DiffusionModels”OR
“Transformers”AND“Digital Marketing” OR “Advertising” OR “Marketing Automation” OR
“Personalized Marketing” OR “Marketing Campaigns”
Wealsoemployedwildcardoperators(wheresupported)tocapturevariations(e.g., advert*foradvertise,
advertisement,o radvertising). To ensure the coverage of closely related works, we iteratively refined these
queries by scanning initial results and incorporating additional keywords such asmarketing analytics,
marketing content generation,and chatbotreferences.
2.3 ScreeningandEligibilityCriteria
Weadoptedamulti-stagescreeningprocesstofilteroutirrelevant,duplicate,orlow-qualitystudies.
2.3.1InitialScreening
1. Title and Abstract Review: We assessed titles and abstracts against the core theme of “generative AI in
digitalmarketing”.Papersfocusingsolelyon predictiveanalytics,salesforecasting,or generalAI without
generativecomponentswereexcludedatthisstage.
2. Removal of Duplicates: Studies retrieved from multiple databases were consolidated using reference
managementtools(e.g.,Zotero,Mendeley),andduplicateswereeliminated.
2.3.2Full-TextEvaluation
For studies surviving the initial screening, we downloaded the full texts and applied the following
inclusionandexclusioncriteria:
InclusionCriteria
• Studies (journalarticles,conference papers, book chapters)explicitly addressinggenerative AImodels
(e.g.,Transformer-basedmodels,GANs,VAEs,diffusion)inadigitalmarketingoradvertisingcontext.
• Works discussing empirical or conceptual insights on applications, opportunities, or challenges of
generativeAIinmarketing.
• Publications in English, from peer-reviewed or credible sources (including gray literature if it met
qualitystandards).
• Studiespublishedfrom2019onward,reflectingtheemergenceofkeygenerativetechnologies.
ExclusionCriteria
• Studies focusing exclusively on predictiveor discriminativeAI (e.g., churn prediction, anomaly detec-
tion)withoutdiscussinggenerativeoutputs.
• Publications that addressed marketing analytics but lacked any generative AI component or
methodology.
• Non-scholarlypiecessuchasblogposts,editorialopinions,orincompletepaperswithoutpeerreview.

8 ComputMaterContin. 2026;87(3):11
•D u p l i c a t e o rsignificantlyoverlappingworks(e.g.,extendedversionsofthesameconferencepaper)were
countedonlyonce.
2.4 QualityAssessment
Wefurtherevaluatedeligiblestudiestoensuremethodologicalrigorandrelevance:
1. (QA1)ClarityofResearchAims:Didthestudyclearlydefineitsresearchobjectivesregardinggenerative
AIandmarketing?
2. (QA2)MethodologicalSoundness:Forempiricalstud ies,werethedatacollectionandanalysismethods
adequatelydescribed?Forconceptualworks,didtheauthorsprovidecoherentframeworksortheoretical
grounding?
3. (QA3) Relevance to Generative AI: Did the paper discuss generative models beyond mere mention,
providinginsightsintodeployment,performance,orstrategicapplication?
4. (QA4) Marketing Focus: Did the study explicitly link AI methodologies to marketing objectives (e.g.,
personalization,brandcommunication,userengagement)?
Studies scoring low on multiple QA criteria were excluded or flagged for limited inclusion in the
thematic discussion. Throughout this process, conflicts or uncertainties were resolved through consensus
betweenatleasttwoauthors.
2.5 DataExtractionandSynthesis
Eachincludedpaperwascarefullyexaminedtoextractpertinentinformation:
• Bibliographic Details: Author names, year of publication, source venue (journal, conference, book
chapter),andgeographicalfocus(ifspecified).
• AI Technique(s) Employed: Type of generative model (GAN, Transformer, VAE, diffusion model),
trainingapproach,anddatadomain(text,image,multimodal).
• Marketing Application: Context of usage—advertising, social media content generation, email cam-
paigns,SEOoptimization,ormorespecializeddomainslikeAR/VRmarketing.
• Outcomes and Metrics: Reported improvements, quantitativemeasures (e.g.,click-throughrate,time-
to-market),andqualitativeinsights(e.g.,brandperception,useracceptance).
• Identified Challenges and Ethical Considerations: Issues related to bias, privacy, transparency, or
regulatoryconstraints.
We adopted athematic analysisapproachtocategorizefindingsintobroaderclusters(e.g., contentgen-
eration,personalization,ethicsandregulation ),matchingtheresearchquestionsstatedearlier.Theemergent
themes guided the presentation of results inSection4. Where relevant, numeric metrics (e.g., effect sizes,
successrates,orengagementmetrics)werenotedandcomparedacrossstudiestoofferquantitativecontext.
3 BackgroundandTheoreticalFoundations
In this section, we provide a comprehensive overview of the foundational concepts and theoretical
underpinningsthatinformtheuseofgenerativeAIindigitalmarketing.Specifically,weexplorethehistorical
progression of generative AI technologies, discuss the principal domains of digital marketing, and map the
relevanttheoreticalframeworksthatguidetheseemergingtools’adoptionandethicalconsiderations.
3.1 GenerativeAIOverview
Generative AI refers to a subset of artificial intelligence techniques designed to create new, synthetic
content across various modalities, such as text, images, and videos, by learning patterns and features from

ComputMaterContin. 2026;87(3):11 9
training data [26,27]. These systems rely on sophisticated algorithms, such as deep learning, transformers,
anddiffusionmodels,togenerateoutputsthatareoftenindistinguishablefromhuman-createdcontent.
Overtheyears,generativeAIhasbecomeindispensableinindustrieswherecreativity,automation,and
personalizationintersect.Itstransformativepotentialliesinitsabilitytoaugmenthumancapabilities,reduce
operationaloverhead,andopennewavenuesforinnovationincontentcreationanduserengagement[ 28,29].
Forinstance,generativeAIenablesadvancementsincontentgenerationformoviesandmusic,syntheticdata
creationfortrainingmachinelearningmodels,andthedevelopmentofimmersivevirtualrealityexperiences.
The applications of generative AI span multiple domains, including automating customer support
interactions using chatbots, generating hyper-personalized marketing campaigns tailored to individual
consumer preferences, and advancing medical imaging analysis [30,31]. By leveraging vast amounts of
structured and unstructured data, generative AI empowers industries to achieve better efficiency and
impactfuloutcomes.
Historically, generative AI has evolved from foundational statistical models, such as autoregressive
methods and probabilistic programming, to more advanced neural network-based approaches like trans-
formers and diffusion models. The introduction of transformer architectures has significantly accelerated
progress,enablingmoreaccurateandversatilecontentcreation. Fig.2 providesanoverviewofkeydevelop-
mentsingenerativeAI,depictingpopularmodels,theirdevelopers,publicationyears,andapplications.
Figure 2: Overview of Generative AI developments and their key milestones. The visualization highlights various
generative AI systems, their developers, publication years, and applications, showing the diverse use cases and
continuousinnovationinthisfield.

10 ComputMaterContin. 2026;87(3):11
3.1.1HistoricalEvolution
ThetrajectoryofgenerativeAIcanbetracedbacktoearlylanguagemodels andstatisticalapproaches,
which laid the groundwork for many modern techniques [32]. Initially, n-gram models and Markov chains
were employed to model sequences of words or characters, enabling primitive text generation. These early
methods, while rudimentary, showcased the potential for machines to produce human-like text through
probabilistic assumptions [33,34]. As shown inFig.3, this early phase marked the beginning of a gradual
evolutiontowardmoreadvancedgenerativemethods.
Figure3: Evaluationof Generative AI from 1950 to 2024.
Subsequent breakthroughs in recurrent neural networks (RNNs) [35] and long short-term memory
(LSTM) [36] networks extended the capabilities of language modeling by managing longer dependencies
withintextsequences.Researchersharnessedthesearchitecturestogeneratemorecoherentandcontextually
relevantsentences,albeitwithlimitationsincapturingextremelylong-rangedependenciesorglobalcontext
withinlargerdocuments[ 37].
A significant leap forward occurred with the emergence of transformer-based models, notably intro-
duced by Vaswani [38] in the seminal paper “Attention is All You Need”. Transformers replaced recurrence
with a self-attention mechanism, vastly improving the capacity to process entire sequences in parallel and
capturelong-rangerelationshipsmoreeffectively.Thisarchitecturaladvancementcatalyzedthedevelopment
oflarge-scalepre-trainedlanguagemodels(e.g.,GPT,BERT)thatdemonstratedunprecedentedfluencyand
versatilityacrossabroadspectrumoflanguagetasks.
Inparallel,computervisionresearcherspioneeredgenerativeadversarialnetworks(GANs),introduced
by Goodfellow et al. [39], which enabled the generation of highly realistic images. GANs involve two net-
works,ageneratorandadiscriminator,whicharetrainedinoppositiontoeachother,iterativelyrefiningtheir
performancethroughadversarialtraining[ 40].Morerecently,diffusionmodelshaveemergedasapowerful

ComputMaterContin. 2026;87(3):11 11
classof generativemodels forimagesynthesis,leveraging stochasticprocesses toincrementally refine noise
into coherent images [41,42]. These advancements in text, image, and multimodal generation form the
cornerstoneofgenerativeAIcapabilitiesthatarenowbeingintegratedintovariousmarketingapplications.
3.1.2FundamentalConcepts
At the core of modern generative AI are two primary classes of models: generative and discrimina-
tive [43]. Although these models use similar advanced neural architectures, they serve different objectives
and approaches to working with data. Generative models focus on understanding and replicating the
underlying data distribution, while discriminative models aim to make predictions based on observed
features[44].
Generative models [45] aim to model the joint probability distributionpθ(x) of the observed datax
andpotentiallysomelatentvariables z[46].Inessence,theytrytocapturetheunderlyingdistributionofthe
data and can generate new data points that resemble the training data. These models are critical when the
goalistogeneratenovelcontent,suchasimages,text,ormusic.
Discriminative models [47], on the other hand, focus on learning the conditional probability distribu-
tion pϕ(y∣x),wh er ey represents thelabelor class,and xrepresentsthefeaturesofthedata.Theyareused
fortaskssuchasclassificationandregression,wherethegoalistomakeaccuratepredictionsgiveninputdata.
Generative Models: Generative models attempt to learn the joint probability distribution of the
observed data and any latent variables that might influence it. This is typically achieved by modeling the
data as a combination of factors, which may include complex dependencies between observed variables
and latent factors. By learning the joint distribution, these models can generate new data points that
are similar to the original dataset [48]. Common examples include Variational Autoencoders (VAEs),
which encode data into a latent space and sample new instances with similar characteristics; Generative
Adversarial Networks (GANs), which use adversarial training between a generator and discriminator to
produce realistic outputs; Transformer-based language models, such as GPT and BERT variants, which
generate coherent and contextually relevant text; and advanced neural network architectures that combine
convolutional,recurrent,andattentionmechanismstogeneratehigh-fidelityimages,audio,andmultimodal
content. Recent advancements in these models include diffusion models for improved image generation,
fine-tuned large language models for domain-specific text generation, and multimodal generative models
thatintegratetext,image,andaudiotosupportcreativeandinteractiveapplicationsinmarketing,healthcare,
andentertainment.
• Variational Autoencoders (VAEs):VAEs [49] are generative models that integrate deep learning
w i t hp r o b a b i l i s t i cm o d e l i n g .Th e yc o n s i s to fa ne n c o d e rt h a tm a p si n p u td a t ax into a latent space
and a decoder that generates data from this latent representation. The encoder produces a latent
distribution characterized by a mean and standard deviation, from which a latent vector is sampled.
Thedecoderthenreconstructstheoriginalinputfromthisvector.TrainingaVAEinvolvesoptimizing
both the reconstruction quality and the regularization of the latent space to ensure meaningful and
continuousrepresentations.

12 ComputMaterContin. 2026;87(3):11
Table 3:S ummaryofV AEs ’r oleindigitalmarketing.
Ref. Year Dataset Contribution Limitation
[50]2 0 2 4 BlogCatalog, Flickr[51],andEnron
ThispaperproposesadualVAE-GAN
model for anomaly detection in
attributedsocialnetworks,enhancing
dataencodinganddetectinganomalies
withoutlabeleddata.Themodel
outperformsexistingmethods,
achievingAUCscoresof0.8368,
0.8202,and0.7118onBlogCatalog,
Flickr,andEnrondatasets.
Theproposedmodelfaces
challengeswithlow-dimensional
da tasets,asseeninEnr o n,andi ts
perfo rmanceissensi tivetoda ta
quality.Additionally,the
complexityofintegratingdual
VAEsandGANsmaycomplicate
trainingandtuning,limitingits
practicalapplicationinsome
real-worldscenarios.
[52]2 0 1 8
CelebA[53],
CelebA-HQ[54],
LSUNBED
ROOM[55]
ThispaperproposestheIntroVAE
model,whichsynthesizes
high-resolutionimagesbycombining
V AEsandGAN sin toasingle-str eam
ar chi tectur e.I tinco rpo ra tesa
self-evaluationmechanismfor
performanceimprovementandstable
training.Itsuccessfullygenerates
imageswithhighqualityanddiversity,
outperformingexistingGANsin
metricslikeMS-SSIMandFID.
TheIntroVAEmodelfaces
challengesingeneratingfine
details,oftenresultinginblurriness
duetothelimitationsofVAEs.
Despitesimplifyinghybridmodels,
itdoesnotachievetheimage
qualityofGANsinhigh-resolution
tasks,anditsadaptabilitytoother
tasksmayrequirefurther
adjustments.
[56]2 0 1 8 CelebA
Thispaperenhancesimagequalityin
VariationalAuto-Encoders(VAEs)
usinganadversariallearning
frameworkwithperceptualguidance,
stabilizingtrainingthrougherror
feedback.Theapproachgenerates
high-resolution,diversefacial
attributesandexpressions,
outperformingBoundaryEquilibrium
GANs(BEGAN).Quantitative
improvementshighlightitscapability
toproducerealisticimageswith
enhancedresolutionandvariety.
Themodel’srelianceonalarge
da taset(360kceleb ri tyimages)
limitsgeneralizabilitytosmaller
datasets.Trainingcomplexitydue
tohyper-parametertuning
challengesinpracticaldeployment.
Additionally,themodelremains
vulnerabletomodecollapse,where
generatedoutputslackdiversity,a
commonissueinGAN-based
methodsdespitetheirdesigned
improvements.
Fig.4 illustratestheVAEprocess,showingtheprobabilisticencodercompressingtheinputimage
intoalatentspaceandthedecoderreconstructingtheimagefromthesampledlatentvector,highlighting
the flow from input to latent representation and back to output.Table 3summarizes various research
worksonVAEs,emphasizingtheirroleindigitalmarketingandotherapplications.
• Generative Adversarial Networks (GANs):G A N s ,i n t r o d u c e db yG o o d f e l l o we ta l .[57], consist of
two neural networks: a generator (G) and a discriminator (D). The generator produces synthetic data
from random noise, while the discriminator classifies inputs as real or fake. The two networks engage
in an adversarial process in which the generator aims to create data that is indistinguishable from real
samples, and the discriminator tries to correctly identify real vs. generated data. Training alternates
between updating the discriminator and the generator, with the goal of reaching a balance where the
generator produces realistic outputs and the discriminator achieves approximately 50% accuracy on
distinguishingrealfromfakedata.
VariantslikeWassersteinGAN(WGAN)[ 58]havebeenproposedtoimprovetrainingstabilityand
output quality by modifying the loss function. GANs have revolutionized generative modeling across

ComputMaterContin. 2026;87(3):11 13
various applications, including image generation, super-resolution, and style transfer [59,60]. Fig.5
illustrates the architecture of GANs, highlighting the interplay between the generator and the dis-
criminator. Table 4provides a detailed summary of these notable contributions, highlighting the
datasetsused,contributionsmade,andthechallengesaddressedineachstudy.Thistabulatedsummary
illustratesthegrowingversatilityofGANs,whilepointingoutlimitationssuchastherelianceonspecific
datasets, challenges with generalization, and the need for more diverse training data that remain open
ar easfo rfurtherr esear ch.
Table 4:Summary of GANs research and applications.
Ref. Year Dataset Contribution Limitation
[61]2 0 2 4 OwnDataset
Thispaperintroducesanautomatedad
creativegenerationmethodusing
GANsandreinforcementlearning.It
integrateslandingpageinformation,
improvingadrelevance.Empirical
resultsshowhigh-qualitygenerated
ads,achievingimpressiveROUGE
scores,withlongersequences
enhancingperformanceandcapturing
expectedadfo rma ts.
Thisstudyr elieshea vilyo nquan ti ta tive
metricslikeROUGEscores,whichmay
notfullyassessadquality.Additionally,
repetitivecontentemergedwithcertain
sequencelengths,suggestingtheneed
formodelrefinementtoboost
creativityandcontentdiversity,and
future work could improve the reward
functio nfo rbetteradfo rma tem phasis.
[62]2 0 2 4 E-Commerce WebsiteDatasets
Thispaperintroducesanovel
GAN-VGG-basedvisualtransformer
modelforgeneratingadvertising
images,enhancingtheirquality,appeal,
andinteractivity.AchievinganAUCof
over0.7onmultipledatasets,the
algo ri thmp r o veseffectiveinr eal-wo rld
applications,boostingwebsite
operationsthroughvisuallyengaging
advertisementsthatresonatewith
users.
Thealgorithm’sgeneralizationacross
diverseadvertisingdomainsislimited,
withreducedeffectivenessonvaried
datasets.Itlacksmultimodal
integration,focusingsolelyonimage
generationwhileneglectingtextual
content.Theinclusionofmorediverse
trainingdataandajointgenerative
modelincorporatingtextandimages
couldsignificantlyimprove
performance.
[63]2 0 2 4
SocialNetwork
Advertising
Dataset
Thispaperintroducesagenerative
augmentationframeworkusingGANs,
VAEs,andGMMstoenhancesocial
networkadvertisingdata,improving
machinelearningclassifier
performance.ItshowsVAEsprovide
thegreatestperformanceboost,with
significantaccuracygainsthroughdata
augmentation,offeringinsightsfor
digitalmarketingpractitioners.
Thestudyislimi tedb yi tsr elianceo na
singledataset,affectingthe
generalizabilityofthefindings.
Additionally,theanalysisdoesnot
coverallpossibleclassifiersandlacks
anexplorationofadvanceddata
augmentationtechniquesonfairness
andb iasinp r edictio ns.
[64]2 0 2 1 JingdongDataset
TheproposedM-GAN-XGBOOST
modelenhancessalesprediction
accuracyforonlinestoresby
combiningLSTM,GAN,and
XGBOOST.Itadaptstoreal-time
consumerbehaviorandimproves
predictionaccuracy,achievingan
RMSEof11.9andanMAEof8.23,
validatedwiththeJingdongdataset.
Themodel’sperformanceis
data-dependent,requiring
high-quality,abundantinputdata.Its
compleximplementation,integrating
LSTM,GAN,andXGBOOST,may
challengeonlineretailers.Additionally,
itsgeneralizabilitytoother
e-commerceplatformsorproduct
categoriesneedsfurthervalidation.

14 ComputMaterContin. 2026;87(3):11
• Transformer-Based Language Models:Transformer-based language models, such as GPT [65], have
advancednaturallanguageprocessingbyusingself-attentionmechanismstocapturelong-rangedepen-
denciesandcontextualrelationshipsacrossentiresequences[ 66].UnlikeRNNsorLSTMs,transformers
process sequences in parallel, improving training efficiency. GPT uses a decoder-only architecture
for text generation, while the multi-head attention mechanism allows the model to capture multiple
levelsofabstraction[ 67].Despitetheireffectiveness,transformersrequirelargedatasetsandsubstantial
computationalresources[ 68,69].
Fig.6 illustrates the transformer architecture, highlighting its self-attention layers and feed-
forwardnetworksthatprocesssequencesinparallel. Table 5summarizeskeystudiesandadvancements
in transformer-based models, highlighting the models used, contributions made, and their respective
limitations. This table reflects the growing diversity of transformer applications across various NLP
tasks,whileemphasizingongoingchallengesrelatedtomodelsize,efficiency,andgeneralizability.
Figure4: Architecture ofVAE forimage reconstruction.
Figure5: Architecture ofGAN for image generation.

ComputMaterContin. 2026;87(3):11 15
Figure6: Thearchitectureofa transformermodelwithmultiplelayers ofattentionandfeed-forwardnetworks.
Table 5:Summaryoftransformer-basedrecentwork.
Ref. Year Dataset Contribution Limitation
[70]2 0 2 4
COCO[ 71],
YFCC100M[72],
Fashion-
MNIST[73],
ImageNet[74]
Thispaperintroducesthe
Transformer-cGANsmodel,
integratingTransformerswithGANs
forenhancedadvertisingimage
generation.Extensiveexperimentson
datasetslikeCOCO,YFCC100M,and
ImageNetshowsuperiorperformance,
achievinghighPSNRandSSIMscores.
Themodeldemonstratesrobustness,
adaptability,andhigh-qualityoutputs,
validatedbymetricslikeFID,IS,and
MIoU.
TheTransformer-cGANsmodelfaces
limitationssuchashighcomputational
demand,andrestrictingreal-time
marketingapplications.Itrequires
improvedhyperparametertuningfor
optimalperformanceandinvolves
complex implementation due to
Transformerintegration,posing
challengesforbroaderaccessibility.
Theseissueshighlightareasfor
refinementtoimproveusabilityand
efficiencyinpracticalscenarios.
(Continued)

16 ComputMaterContin. 2026;87(3):11
Table 5 (continued)
Ref. Year Dataset Contribution Limitation
[75]2 0 2 4 TargetingVis Dataset[76]
ThisstudyintegratesVision
Transformer(ViT)andGraphNeural
Networks(GNN)withGANsto
analyzeadvertisingeffectiveness,
improvingpredictiveaccuracyand
fea tur equali ty .I tenables
co m p r ehensiveadco n ten tanalysisb y
transformingdatainto
high-dimensionalrepresentationsand
addressesresearchgaps,offering
valuableinsightsforoptimizingdigital
marketingstrategies.
Thepaperidentifiesdataconstraints,
methodologicalsingularities,andalack
o fa tten tio ntotem po ralchangesaskey
limitationsaffectinggeneralizationand
relevance.Additionally,ithighlights
insufficientprivacyprotectioninprior
studies,emphasizingtheneedfor
betterapproachestoensurerobust,
adaptive,andethicalmethodsin
advertisingeffectivenessresearch.
[77]2 0 2 4
Women’sClothing
ECo mmer ce
Reviews
dataset[78]
ThispaperbenchmarksCNN,RNN,
andBi-LSTMforsentimentanalysisin
e-commerce,emphasizingRoBERTa’s
superiority.Advancedembeddingslike
BERT,FastText,andWord2Vec
enhancemodelperformance.
Ensemblemodelsoutperformsolo
models.Simplifiedclassstructures
improvepredictions,providinginsights
forpracticalapplicationsinconsumer
sentimentanalysis.
Theuseddatasetlacksthorough
screeningforspamorfraudulent
reviews,potentiallyaffectingprediction
accuracy.Thestudyfocusessolelyon
Englishreviews,limitingits
applicabilityinmultilingualsettings.
Additionally,findingsbasedon
AmericanEnglishmaynotgeneralize
tootherdialectsorlanguages,reducing
theglobalrelevancefordiverse
e-commerceplatforms.
[79]2 0 2 3 OnlineRetail DataSet[80]
Thispaperpresentsanovel
transformer-basedmodelfor
p r edictingthenextp ur chaseda y
(NPD)ine-commerce,outperforming
traditionalmethodslikeARIMA,
XGBoost,andLSTMby6.15%in
RMSE.Themodeladaptstovarious
timeseriespatternsandhandles
no n-sta tio naryda tamo r eeffectively ,
improvingaccuracy.
Theself-attentionmechanism’s
permutation-invariancein
transformersmaynegativelyaffectthe
orderofvaluesintimeseries
applications.Additionally,challenges
ariseforlong-timeseriesforecasting,
wherelinearmodelssometimes
outperformtransformers,andexternal
regressorscannotbeusedeffectively
duetodatasetlimitations.
Table 6presents a comparative analysis of prominent generative techniques, highlighting their
strengths, weaknesses, typical applications, and critical insights, which complements the discussion on
transformersandothergenerativemodels.
Table 6:ComparativeanalysisofgenerativeAImodels.
Model KeyStrengths KeyWeaknesses Typical Applications CriticalInsight
GANs
High-quality
imagegeneration,
realistic outputs
Training
instability,mode
collapse,difficult
toevaluate
Image synthesis,
dataaugmentation,
super-resolution
Excelsinrealism
butcanbe
unstable;requires
careful architecture
tuning.
(Continued)

ComputMaterContin. 2026;87(3):11 17
Table 6 (continued)
Model KeyStrengths KeyWeaknesses Typical Applications CriticalInsight
VAEs
Probabilistic
modeling,latent
space
interpretability
Blurryoutputs
comparedto
GANs,lowervisual
fidelity
Representation
learning,anomaly
detection,
generative
modeling
Betterfor
structuredlatent
spaceand
interpretability;
output quality
tradesoffrealism.
Diffusion
Models
Strong mode
coverage,
high-quality
outputs,stable
training
Computationally
expensive,slow
sampling
Imagegeneration,
moleculardesign
Offersabalanceo f
stabilityandoutput
diversitybutata
computational
cost.
Transformers
Handles
long-range
dependencies,
scalable,versatile
Data-hungry,high
memory
consumption
Text-to-image
generation,
language
modeling,
multimodal tasks
Flexibleand
powerfulfor
cross-domain
tasks;performance
dependsheavilyon
datasetsize.
Discriminative Models: Discriminative models are a class of machine learning models designed
to learn the conditional relationship between input features and target outputs, such as class labels or
regression values [81]. Unlike generative models, which model the joint distribution of inputs and outputs,
discriminative models focus on directly predicting outcomes or distinguishing between classes [82]. They
assignascoretoeachpossibleoutputandnormalizethe sescorestoestimatethelikelihoodofeachoutcome.
In practice, discriminative models are widely applied across domains and frequently complement
generativemodelsbyservingasevaluativetools.Forexample,in GANs,thediscriminatorisadiscriminative
model that assesses whether generated samples are realistic, guiding the generator to produce outputs
alignedwiththetargetdistribution.In digitalmarketing,discriminativemodelshelprank,filter,orclassify
generatedcontentbasedonquality,engagementpotential,oralignmentwithbrandobjectives[ 83].
Thesemodelshavefoundextensiveapplicationsinmarketing,excellingintaskssuchasrankingcontent,
predictingcustomerinteractions,andenablingdata-drivenpersonalization.Nallapati [ 84]highlightstheuse
ofSupportVectorMachines(SVMs)inInformationRetrieval,demonstratingimprovementsinfeaturelearn-
ing and ranking performance. Haider et al. [85] propose a discriminative clustering framework for market
segmentation, showing better interpretability and adaptability to temporal patterns. An et al. [86] integrate
discriminative models with generative features for citation classification, achieving notable improvements
in predictive performance. Collectively, these studies underscore the potential of discriminative models in
enhancingmarketingstrategies,contenttargeting,andpersonalizedrecommendations.
Neural Network Architectures:Beyondgenerativeordiscriminativeobjectives,modelscanbeimple-
mented using various neural network architectures, each suited to different marketing tasks such as text
generation,time-seriesanalysis,orsocialnetworkexploration.

18 ComputMaterContin. 2026;87(3):11
Feedforward Networks (FFN):FFN [87] are the simplest neural architectures, consisting of layers
that apply linear transformations followed by nonlinear activations. These networks are widely used for
regression,basicclassification,andtransformationsinmarketingpipelines,suchaspredictinguserresponses
tocampaigns.
RecurrentArchitectures: It’sincludingRNNs,LSTMs,andGRUs[ 88,89],arespecializedforsequence-
related tasks. They maintain a hidden state over time, enabling the analysis of user behavior sequences or
generating sequential marketing content like emails or social media posts. LSTMs and GRUs incorporate
gatingmechanismstohandlelongsequencesandmitigategradientissues.
Attention-Based Transformers: Attention-based transformers leverage multi-head self-attention
mechanismstocapturebothshort-andlong-rangedependenciesmoreefficientlythanRNNs.Transformers
process entire sequences in parallel, generating coherent, contextually rich content, making them highly
effectivefortaskslikeadcopygeneration,productdescriptions,andmarketingchatbots.
GraphNeuralNetworks(GNNs): GNNs[90–92]aredesignedforgraph-structureddata,representing
entities and their relationships (e.g., users in a social network). GNNs are useful for analyzing social
interactions, identifying influential users, and recommending personalized marketing strategies, though
theyarelesscommonlyusedfordirectcontentgeneration.
ImageSynthesis: Imagesynthesisinvolvesgeneratingnewimagesbylearningthedistributionofvisual
datausingcomputationalmodels.Inmarketing,itenablesscalablecreationofvisualcontent,suchasproduct
mockups,personalizedads,andvirtualtry-onexperiences[ 93,94].
Generative Adversarial Networks are among the most prominent techniques for image synthesis.
GANs consist of a generator that creates synthetic images and a discriminator that evaluates their realism.
Variants like StyleGAN [95]andBigGANallowfine-grainedcontroloverattributessuchasshape,color,and
structure,supportingapplicationslikevirtualclothingsimulations,promotionalgraphics,anddigitalavatar
customization.Diffusionmodels[ 96],suchasImagenandStableDiffusion[ 97],progressivelyconvertnoise
intohigh-fidelityimages,providingimprovedrealismanddiversitycomparedtoGANs.Inmarketing,these
modelsreducecontentproductioncosts,shortendesigncycles,andenablethegenerationofvisualstailored
todifferentcustomersegmentsorcampaigns[ 98].
Multimodal Approaches:Multimodal approaches integrate data from multiple sources, such as text,
images,video,andaudio,tobuildsystemsthatreasonacrossmodalities.Inmarketing,suchsystemsenhance
personalization,productdiscovery,andcoherentcontentgeneration[ 99,100].
Transformer-basedmodelsarecommonlyusedinmultimodallearning.Forinstance,CLIP[ 101]jointly
embedstextualandvisualinformationintoasharedsemanticspace,aligningtextandimagerepresentations.
Generative models like DALL⋅Ea n dI m a g e n[102,103] extend this approach by creating images from
textual prompts, typically using an encoder to process text and a decoder (based on diffusion or vector
quantization)tosynthesizeimages.Applicationsincludealigningadvertisementswithconsumerpreferences,
automaticallygeneratingcampaignmaterialsfrombrandstories,andenablingsemanticproductsearchusing
both text and images [104]. While multimodal models pose challenges in aligning and fusing diverse data
types,theyenhancecontext-aware,adaptive,andeng aginguserexperiencesinmodernmarketingsystems.
Choice of Model and Architecture:The selection of an appropriate model type and architecture is
a critical step in designing AI-driven strategies for digital marketing. This decision depends on multiple
interrelated factors that affect the model’s suitability for specific tasks, its performance, and how well it can
bedeployedinpracticalsettings.
One key factor is the target modality, which defines the type of data the model processes. This may
include text, images, audio, or multimodal formats that combine several data types. For example, a model

ComputMaterContin. 2026;87(3):11 19
tailoredfortextinputwilldiffersignificantlyinstructureandpurposecomparedtooneintendedforimage
generation or audio synthesis. Another important consideration is the marketing objective. Goals such
as personalized recommendations, ad copy generation at scale, audience segmentation, or visual content
creationrequirespecificmodelcapabilities.Choosingtherightmodelensuresthatthesystemisefficientand
alignedwiththedesiredoutput.
The characteristics of big data, including volume, velocity, and veracity, play a central role in selecting
appropriate generative models. Volume refers to the vast amount of consumer data available, which can
improvelearningbutalsorequiressignificantcomputationalresources.Velocityconcernstherapidflowand
processingdemandofdata,especiallyindynamicmarketingenvironmentswherenearreal-timeoutputmay
be required. Veracity refers to the reliability and noise level in the data, which affects the consistency and
quality of the generated results. These aspects introduce critical trade-offs when selecting among models
suchasGANs,VAEs,anddiffusionmodels.
GANsaretypicallyusedwhenfastgenerationofrealisticvisualcontentisrequired.However,theymay
requiremorecarefultrainingduetopotentialinstabilityandissueslikemodecollapse.VAEsaremorestable
andcomputationallyefficient,makingthemagoodoptionwhenmoderateimagequalityisacceptable.Diffu-
sionmodelsprovidehigh-fidelityoutputswithstrongcontrollability,buttheyarecomputationallyintensive
andtime-consuming,whichmaylimittheirusabilityintime-sensitiveorenergy-constrainedenvironments.
Selectingamongthesemodelsinvolvesevaluatingtrade-offsacrossseveraldimensions,includingtrain-
ingandinferencetime,costofdeployment,performanceaccuracy,andenergyconsumption.Thesetrade-offs
shouldbecarefullyassesseddependingonthedigitalmarketingusecaseandoperationalconstraints. Table 7
outlinestheseconsiderationsinastructuredway.
Table 7:Factorsinfluencingthechoiceofmodelandarchitecture.
Factor Description RelevancetoDigitalMarketing
TargetModality
Referstothetypeofdatathemodel
willhandle,suchastext,images,
audio,ormultimodaldatacombining
different formats
Text models support ad copy
generation,imagemodelsenable
visualcampaigns,andmultimodal
modelsdriveinteractiveorimmersive
experiences
Marketing
Objective
Referstotheendgoalofthemodel,
suchasrecommendations,
segmentation, or contentgeneration
Discriminativemodelsarewell-suited
foraudienceclassification,while
generativemodelsareusedfor
producing new content like ads or
visuals
Computational
Constraints
Referstolimitsintrainingresources,
inferencespeed,andmodelcomplexity
Heavier models may not be viable in
real-timeusewhilelightweight
al terna tivescansu p po rto n-deviceo r
low-latency applications
BigData
Characteristics
Involvesthevolume,velocity,and
veracityofconsumerdatausedfor
traininganddeployment
High-volume data can enhance
learningbutincreasesresource
demand.High-velocitydataneeds
fastermodels.High-veracitydataleads
to more reliable outputs
(Continued)

20 ComputMaterContin. 2026;87(3):11
Table 7 (continued)
Factor Description RelevancetoDigitalMarketing
ModelTrade-offs
Coversthebalancebetweencost,time,
energy,andperformanceacrossmodel
typeslikeGANs,VAEs,anddiffusion
models
GANsarefastandrealisticbutrequire
tuning.VAEsareefficientandstable
withmoderateoutputquality.
Diffusionmodelsproducesuperior
visualsbut are computationally
expensive
A generative approach is most appropriate when new content creation is required. This includes tasks
suchasdesigningcreativeadcopyorgeneratingproductvisuals.Adiscriminativeapproachismoreeffective
forclassificationandforecastingtaskssuchasaudiencesegmentationorpredictinguserbehavior.Forimage
generationinmarketing,GANsarepreferredfortheirfastandrealisticoutputs.VAEsofferabalanceofspeed
and stability with lower resource use. Diffusion models are ideal when the highest visual quality is needed,
butmaynotbefeasiblefortime-sensitivetasksduetohighenergyandcomputationdemands.
Fortasksthatcombinetextandimageunderstanding,suchasproducingbrandedvisualsfromproduct
descriptions or retrieving marketing images based on text prompts, multimodal models like CLIP and
DALL⋅E are highly effective. These models align visual and textual information, enabling cohesive content
generationandretrievalstrategies.
A clear understanding of these trade-offs, along with the influence of big data properties, is essential
for building AI solutions that are not only technically sound but also practical and scalable in digital
marketingcontexts.
3.2 DigitalMarketingLandscape
Digital marketing encompasses a wide array of channels and strategies that businesses utilize to
reach their target audiences online [105,106]. These include content marketing, email campaigns, search
engine optimization (SEO), social media engagement, and paid advertising, among others. Each of these
componentsplaysacriticalroleinshapingabrand’sdigitalpresenceandinfluencingconsumerbehavior.
Topresentamoreunifiedunderstandingofhowthesecomponentsinterrelatewithinacomprehensive
digital strategy,Fig.7 provides a schematic representation of the digital marketing landscape. At the center
of this framework lies the concept of “Digital Strategy”, which integrates three essential pillars: content,
data, and analytics. Surrounding this hub are key domains, including Mobile, Social, Ads, SEO, Website,
Conversation Marketing, Email, and CRM. Each domain contributes uniquely to the overarching strategy.
For example, Mobile and Social enhance accessibility and engagement; Ads and SEO drive discoverability;
Websitedesignandoptimizationsupportconversio ngoals;whileEmailandCR Maidinleadnurturingand
customerretention.
Thisvisualstructureemphasizestheinterconnectednatureofmoderndigitalefforts,showinghoweach
elementmustoperateinalignmentwithotherstoproducecoherentandeffectivemarketingoutcomes.The
integrationoftheseelementssupportsdata-drivendecision-makinganduser-centricdesign,bothofwhich
arecriticalforsustainedsuccessintoday’scompetitivedigitalenvironment.

ComputMaterContin. 2026;87(3):11 21
Figure7: Aschematicdiagramillustratingtheintegratedcomponentsofamoderndigitalmarketingstrategy.
3.2.1 Key Domains in Digital Marketing
Digital marketing includes various channels and tactics, each offering unique opportunities and
challengeswhileoftenoverlappinginpractice:
• Advertising. Advertising involves strategies such as pay-per-click campaigns, display ads, sponsored
listings, and affiliate marketing [107,108]. Generative AI enables automation in creating diverse ad
creatives, headlines, and visuals, enhancing engagement and conversion rates [109]. Studies highlight
bothopportunitiesandchallenges,includi ngbalancingefficiencyandpersonalization[ 110],enhancing
dynamic ads and personalized content like Netflix trailers [109], and trends in AI-driven advertising
withethicalconsiderationsandmethodologicallimitations.
• Social Media Marketing.P l a t f o r m ss u c ha sF a c e b o o k ,I n s t a g r a m ,T w i t t e r ,L i n k e d I n ,a n dT i k T o ka r e
key for engagement [111,112]. Generative AI supports rapid content creation and real-time sentiment
analysis[113].Researchhighlightstheinfluenceofonlineword-of-mouth[ 114],GPT-4’sroleincontent
strategies [115], and adoption drivers like efficiency and scalability, alongside creativity limitations and
risks[116].
• Content Marketing.Content includes blogs, infographics, e-books, articles, and videos [117]. Gener-
ative AI enhances both quality and volume, enabling personalized and dynamic content [118]. Studies
show improvements in visual marketing [119], engagement [120], and support for SMEs in SEO and
platform-specificstrategies[ 121].Benefitsincludestreamlinedproductionandconsistentbrandidentity,
withchallengesindataqualityandimplementation.
• Email Marketing.Email marketing relies on personalization and strategic timing [122,123]. Genera-
tive AI enables hyper-personalized content, including tailored subject lines, body text, and product
recommendations[124–126].Studiesdemonstrateimprovementsinengagementandconversions,with
challengesindemographicbias,datasetlimitations,andbroaderapplicability.

22 ComputMaterContin. 2026;87(3):11
• Search Engine Optimization. SEO focuses on optimizing websites and content for search
engines [127,128]. Generative AI assists in keyword selection, meta descriptions, article creation, and
content optimization. Research highlights AI-driven methods for alt text generation [129], readability
improvements, website analytics and branding [130], and voice search adaptation [131]. Challenges
remaininscalability,dataquality,andtoolenhancement.
3.2.2TraditionalAIvs.GenerativeAIinMarketingContexts
Historically, digital marketing has harnessed AI primarily through predictive analytics, rule-based
systems, and recommendation engines [132,133]. These approaches excelled at analyzing historical data to
forecastuserbehavior ,suchaspredictingwhichusersaremostlikelytoclickonanadorbuyaproduct,and
wereinstrumentalinpersonalizingmarketingmessagestospecificsegments.
ShifttowardsContentCreationandPersonalization GenerativeAImarksamajorparadigmshiftby
creatingbrand-newtext,images,orvideosratherthanjustanalyzingorpredicting[ 134].Forexample,while
atraditionalAIsystemmightdeterminethebesttimetosendanemailforoptimalopenrates,agenerative
modelcanalsocomposetheemail’ssubjectlineandbodytexttomaximizerelevancyandengagement[ 135].
This ability to automate creative tasks allows marketing teams to significantly scale their content strategies,
producingahighervolumeofmaterialwhilemainta iningconsistentqualityandpersonalization.
OpportunitiesandChallenges
Despiteitsobviousadvantages,generativeAIbringsnewconsiderationsformarketingprofessionals:
• Quality Control and Brand Consistency:Large-scale automated content generation can lead to off-
brand messaging or stylistic inconsistencies if not carefully supervised. Maintaining a brand’s voice
acrossads,socialposts,andemailsrequiresastrategicbalanceofhumancurationandAIoversight[ 136].
• EthicalandAuthenticityConcerns: AsgenerativeAIproduceshighlyrealisticcontent,consumersmay
becomeskepticalabouttheauthenticityofbrandinteractions.OveruseofAI-generatedcommunication
risks eroding trust, particularly if it is not transparent [137,138]. Marketers must therefore disclose AI-
driven aspects where appropriate and ensure all content adheres to ethical guidelines.
• RegulatoryandLegalIssues: Intellectualpropertyquestions,deepfakeregulations,andemergingdata
protectionlawsposechallenges.Marketersmuststaycompliantwithlocalandinternationalguidelines,
particularly when AI-generated content resembles original copyrighted material or manipulates user
perceptions[139,140].
Byrecognizingthesepotentialpitfallsandestablis hingrobuststrategiestomanagethem,organizations
canharnessgenerativeAItodelivermoreengaging,personalized,andeffectivecampaigns.Whilepredictive
and rule-based AI systems remain critical for analytics and user profiling, generative AI takes marketing a
stepfurtherempoweringteamstoachieveunprecedentedcreativityandscaleindigitalcampaigns.
3.3 RelevantTheoreticalFrameworks
Generative AI adoption in digital marketing is not solely determined by technological capabilities;
it is also influenced by organizational culture, perceived value, and ethical and social contexts [141]. This
sectionhighlightstwomajortheoreticallenses,InnovationDiffusionTheory(IDT)[ 142]andtheTechnology
AcceptanceModel(TAM)[ 143],whichofferinsightintohownoveltechnologiesgaintraction.Additionally,
itaddressestheethicalconsiderationsthatshapetheresponsibledeploymentofthesetechnologies.

ComputMaterContin. 2026;87(3):11 23
3.3.1Innovation DiffusionTheoryand Technology Acceptance Model
Innovation Diffusion Theory (IDT)
Rogers’ Innovation Diffusion Theory offers a structured perspective on how individuals and organi-
zations adopt new technologies [144]. The process is conceptualized through five sequential stages, each
influenced by contextual factors such as organizational environment, leadership openness, and market
demands. In the context of our review, these stages were consistently observed in marketing case studies,
where organizations moved from initial awareness of generative AI tools to measurable business outcomes
suchasincreasedengagementratesandreducedcampaigndevelopmentcosts.ThisdemonstrateshowIDT
isnotonlytheoreticalbutalsodirectlyapplicablet oreal-worldadoptionpatternsindigitalmarketing.
• Knowledge: This stage begins when individuals or teams become aware of a new technology, such
as generative AI. At this point, they typically lack a detailed understanding of how the technology
worksorhowitmightberelevanttotheirtasks.Thepresenceofaproactiveorganizationalculturethat
encourages learning and staying updated with technological trends can accelerate the transition from
simpleawarenesstodeeperexploration.
• Persuasion:Inthisstage,individualsstartformingopinionsaboutthetechnologybasedonitsperceived
advantages and limitations. Internal discussions, expert opinions, case studies, and early experiments
shape these perceptions. A supportive culture that fosters open dialogue and values innovation often
enablesemployeestoviewnewtoolswithoptimism.Meanwhile,consumerbehavior,suchasincreasing
demand for faster, personalized digital experiences, can reinforce positive attitudes toward adopting
newtechnologies.
• Decision: Here, a concrete choice is made to either adopt or reject the technology. This decision is
oftentheresultofcost-benefitanalysis,feedbackfr omcolleaguesorindustrypeers,andalignmentwith
strategicgoals.Organizationalcultureagainplay sacriticalrole.Inhighlyhierarchicalfirms,decisions
maydependonleadershipendorsement.Inflatterorganizations,teamconsensusorpilottrialoutcomes
may drive the final verdict. External consumer trends may also exert pressure, compelling marketing
teamstoadoptgenerativeAItoolstoremaincompetitive.
• Implementation:Atthispoint,thetechnologyisintegratedintotheorganization’sexistingworkflows.
Successful implementation may require re-training employees, adjusting work processes, or investing
in supporting infrastructure. A flexible and adaptive organizational culture can significantly ease this
transition.Implementationismorelikelytosucceedwhenearlyadopterswithinthefirmchampionthe
technologyandsharetheirexperienceswithothers,reducingresistanceandconfusion.
• Confirmation: During this final phase, the organization evaluates the outcomes of adoption. If the
results are satisfactory, such as increased efficiency or improved engagement rates, continued use is
reinforced.Ifexpectationsarenotmet,thetechnologymayberevisedordiscontinued.Openfeedback
channels, performance measurement tools, and alignment with customer feedback are essential at
this stage. Consumer response, such as higher satisfaction or increased conversions, can validate the
effectivenessoftheadoptedtechnology.
Rogers also outlines five key attributes that influence how quickly and widely a new technology is
adopted:
• RelativeAdvantage: ThisreferstothedegreetowhichgenerativeAIisperceivedassuperiortocurrent
methods.Ifitclearlyprovidesbenefitssuchascostsavings,timeefficiency,orimprovedcontentquality,
organizations are more likely to pursue adoption. In cultures that prioritize performance and results,
thisfactorisespeciallyinfluential.

24 ComputMaterContin. 2026;87(3):11
• Compatibility: Compatibility assesses how well the technology fits within the existing values, work-
flows,andsystemsofanorganization.IfgenerativeAIintegratesseamlesslywithcontentmanagement
systemsormarketingautomationtools,adoptionismorestraightforward.Whenorganizationalnorms
support innovation and process evolution, compatibility is less of a barrier.
• Complexity: If the new technology is perceived as difficult to use or understand, adoption may be
delayed.Simplicityininterfacedesignandeaseoftrainingcancounteractthisissue.Organizationswith
astrongcultureofcontinuouslearningarebetterequippedtoovercomeperceivedcomplexity.
• Trialability: This factor considers whether the technology can be tested on a limited scale before
full deployment. Pilot campaigns using AI-generated content can help assess effectiveness without
significant risk. An experimental culture within the organization allows teams to learn from trial runs
andrefinetheirstrategiesaccordingly.
• Observability:Thisreferstohowvisiblethebenefitsofthetechnologyaretoothersintheorganization.
Ifresultssuchashighercustomerengagementorcampaignperformanceareclearlyobservable,itfosters
greater confidence and accelerates adoption. Recognition of these successes is easier in transparent,
metrics-drivencultures.
Our findings show that these attributes can be mapped to empirical evidence in marketing practice.
For example, “relative advantage” was quantified in case studies where AI-generated email campaigns led
to measurable cost savings and time reductions comparedto traditional methods. Similarly, “trialability”
was demonstrated through pilot ad campaigns that allowed marketers to experiment with generative AI
tools before full-scale implementation. These practical illustrations ground IDT more firmly in observed
industryexperiences.
Technology Acceptance Model(TAM)
TheTechnologyAcceptanceModel[ 145]explainshowindividualusersdecidewhetherornottoaccept
anewsystembasedontwoprimarybeliefs:
• Perceived Usefulness (PU):This is the degree to which a person believes that using a particular
technology will enhance their job performance. In marketing, this could mean that generative AI
helps userscreatecontentfasterorimproves audienceengagement.Ifmarketers experience noticeable
improvementsinresults,theyaremorelikelytousethetechnologyconsistently.
• P e r c e i v e dE a s eo fU s e( P E O U ) :This refers to how effortless users expect the technology to be.
GenerativeAItoolsthathaveintuitiveinterfacesandofferseamlessintegrationwithexistingworkflows
are more likely to be accepted. In organizations where digital literacy is high and training is readily
available,PEOUtendstobeperceivedmorepositively.
The perceived usefulness and ease of use are not formed in isolation. They are shaped by prior expe-
riences with similar technologies, peer influence, and internal communication. A culture that encourages
feedback and peer support can significantly improve both PU and PEOU. In parallel, rising consumer
expectations for dynamic and personalized marketing content often motivate employees to perceive such
technologiesasnotonlyusefulbutnecessary.Forinstance,casestudiesincludedinourreviewshowedthat
marketersperceivedhighusefulnesswhengenerativeAIimprovedclick-throughratesintargetedcampaigns,
while ease of use was reinforced by user-friendly interfaces that required minimal training. These findings
strengthenthepracticalrelevanceofTAMinexplainingadoptionbehaviors.
Tointegrateboththeorieswithpractice,weexpanded Table 8toincludehowIDTandTAMdimensions
were reflected in case studies. This addition illustrates, for example, how “relative advantage” manifests as
quantifiablecostsavings,orhow“perceivedeaseofuse”translatesintohigheradoptionrateswhenAItools

ComputMaterContin. 2026;87(3):11 25
are integrated into familiar marketing platforms. By linking theory to observed outcomes, the discussion
providesamoreconcretebridgebetweenconceptualmodelsandpracticalrecommendations.
Insummary,IDTandTAMtogetherexplainhowbothorganizationalstructuresandindividualattitudes
shape the adoption of generative AI in marketing. Organizational culture influences how quickly people
movethroughthestagesofawareness,evaluation,andcommitment.Consumerbehavior,ontheotherhand,
actsasanexternalmotivator,pushingorganizationstoadopttoolsthatmeetevolvingcustomerexpectations.
A coherent alignment between internal culture and external demand is essential for successful technology
integration. By grounding these frameworks in empirical findings and case study evidence, we provide
a stronger connection between theory and practice, which also aligns with the recommendations offered
inSection5.4 forresponsibleandhuman-centricadoption.
3.3.2EthicalFrameworksforAI
Although generative AI holds the promise of creative and scalable marketing solutions, it also poses
ethicalandsocietalchallenges[ 146].Recognizingtheseconcernsisessent ialforsustainingtrustandavoiding
legal or reputational repercussions. Several high-level ethical principles guide the responsible development
anddeploymentofAI,including:
• Fairness: This principle requires that generative AI systems do not perpetuate biases—e.g., racial,
gender, or socioeconomic—in advertising content[146]. Marketers should scrutinizethe training data
forhiddenbiasesandapplytechniques(suchasdataaugmentationorbiascorrection)toensureamore
equitable representation of target groups [147].
• Transparency:UsersandconsumersneedtounderstandwhentheyareinteractingwithAI-generated
content vs. human-created material. Clear disclosure practices not only uphold honesty but also help
maintain consumer trust [148]. Regulatory bodies in some regions have already introduced guidelines
mandatingthelabelingofAI-generatedcommunicationsorimagery.
• Accountability: Organizations must establish explicit governance frameworks, delineating responsi-
bility among data scientists, marketing managers, and upper-level executives. This includes proactive
measures to prevent misuse—such as the creation of misleading deepfake advertisements—and the
implementationofredressmechanismsincaseofharmorusercomplaints[ 149].
Many governments and global entities (e.g., the European Union) are moving toward more stringent
AI regulations, impacting areas such as consumer protection, data privacy, and online advertising stan-
dards[150].MarketingteamsthataligntheirgenerativeAIstrategieswiththeseethicalandlegalframeworks
are better positioned to realize long-term value, protect their brand image, and foster lasting relationships
withtheiraudiences[ 151].
Overall,groundingtheintegrationofgenerativeAIinIDT,TAM,androbustethicalprinciplesensures
that organizational adoption is not merely a technological upgrade but a strategically and ethically sound
transfo rma tio n—o netha tr eso na teswi thbo thin ternalstakeholdersandexternalco nsumers.
Insummary,therapidadvancementofgenerativeAIhasopenednewavenuesforcontentcreationand
strategic engagement in digital marketing, extending well beyond the predictive analytics and rule-based
systems of earlier decades [152]. The interplay between technologicalevolution, marketing paradigms, and
ethical imperatives shapes both the promise and the practice of generative AI. As stakeholders navigate
adoption decisions, the integration of established theories like IDT and TAM, alongside emerging ethical
guidelines,willplayapivotalroleinguidingresponsibleandimpactfuldeployment.

26 ComputMaterContin. 2026;87(3):11
Table 8:OverviewofsomeselectedstudiesingenerativeAIindigitalmarketing.
Authors Year AITechnique Marketing Application KeyFindings
Jin et al. [153] 2024 RandomForest
Digital
Advertising
Marketing
TheresearchhighlightsthattheAI-drivenRandom
ForestModel(RFM)effectivelypredictscustomer
counts,outperforminglogisticregression.Italso
revealskeycustomerdemographics,including
university-affiliatedindividualsandspecificprice
distributionpatterns.Here,“trialability”and“relative
advantage”(IDT)aredemonstratedthrough
comparativeaccuracygains.
Vashishth
etal.[ 154] 2025 AIAlgorithm Content Marketing
AI-enabledcontentpersonalizationine-commerce
enhancescustomersatisfaction,engagement,and
conversionratesbyleveragingcustomerdatafor
tailoredrecommendations.Successfulcasestudies
highlighttheirpositiveimpact,thoughchallengeslike
dataprivacyremain.Theseoutcomesconnectwith
TAM’s“perceivedusefulness”andIDT’s“observability”
as customers visibly benefit from personalized
recommendations.
Hocutt [155] 2024 GenAI
Digital
Advertising
Marketing
Theresearchexploresonlineadvertisingplatformsas
collaborativespaceswhereAIandhumanrhetoric
intersect,emphasizinguser-centeredapproachestoad
compositionamidstgenerativeAIintegration.
Compatibilityisreflectedhere,asadoptionsuccess
dependsonalignmentbetweenAIrhetoricand
organizationalmarketingvalues.
Gołąb-
Andrzejak[156] 2023 ChatGPT& GenAI Digital Advertising Marketing
GenerativeAIandChatGPTenhancedigital
advertisingbystreamliningcampaignstages,fostering
marketer-AIcollaboration,andboostingefficiencyand
creativity,withtheoreticalandmanagerial
implications.Thiscasehighlights“trialability”and
“perceivedeaseofuse”,asChatGPTadoptionwas
testedincampaignstagesbeforefulldeployment.
Baek[157] 2023 ChatGPT
Digital
Advertising
Marketing
GenerativeAIreshapesdigitaladvertising,influencing
consumerresponsestovirtualinfluencers,privacyin
behavioralads,AI-drivenethnictargeting,and
relationalbondsingaming,highlightingitsrolein
engagementandpersonalizationacrossplatforms.
Thesefindingsdemonstrate“compatibility”with
evolvingconsumerbehaviorsand“relativeadvantage”
innewadfo rma ts.
Martinez-Rolan
etal.[ 158] 2023 ChatGPT Content Marketing
Theresearch reveals the cautious use of synthetic
contentgeneratorsbycommunicationprofessionalsin
Galicia,mainlyforbrainstorminganddraftingtexts,
withChatGPTbeingthemostrecognizedand
influentialtool.ThisshowsTAM’s“perceivedeaseof
use”,asadoptionoccursmainlyinlow-risk,supportive
taskslikeb rainsto rming.

ComputMaterContin. 2026;87(3):11 27
4R e s u l t s
In this section, we present the findings from the systematic review, organized around key themes
and research questions. The data extraction and synthesis focused on identifying the nature of each study
(i.e., methodological approach, AI techniqueemployed, marketing application) and the reported outcomes
or insights. We subsequently group these findings into major thematic categories that emerged from
theliterature.
4.1 StudyCharacteristics
Webeginbyoutliningthegeneralcharacteristicsofthestudiesincludedinthisreview. Table 8provides
a summary of selected studies, highlighting the authors, publication year, AI technique used, marketing
application,andmainfindings.
Distribution by Publication Year, Journal, and Geography
A preliminary analysis indicated that the number of publications on generative AI in marketing has
grown exponentially since 2018, following the release of transformer-based models and the subsequent
proliferation of large-scale language models. Most studies were published in computer science and AI-
oriented venues, although cross-disciplinary journals covering marketing and information systems also
featured prominently. Geographically, the majority of empirical research originated from North America
and Europe, with a growing number of contributions from Asia—especially in regions with significant
e-commerceorsocialmediauserbases(e.g.,China,RepublicofKorea).
4.2 ThematicCategorization
Tofacilitateanin-depthdiscussion,wegroupthestudiesintofourmainthemesthatcapturethebreadth
ofgenerativeAIapplicationsindigitalmarketing.
4.2.1 Theme 1: Content Generation and Personalization
AI-GeneratedAdCopy&PersonalizedEmailCampaigns
Several studies highlighted how large language models and recurrent neural network architectures are
leveraged to craft real-time, context-aware advertising copy [159,160]. For instance, generative models can
tailorsubjectlinesorproductdescriptionstospecificusersegments,oftenresultinginincreasedopenrates
anduserengagement.
Chatbots and Conversational Agents:In addition to static text generation, chatbot systems powered
by generative language models were reported to offer more natural and contextually relevant interactions
withcustomers[ 161,162].Thisfostersstrongerbrand-customerrelationshipswhilefreeinghumanagentsto
focuson complex or high-stakesqueries.
ImpactonCustomerEngagementandBrandPerception: Empirical data suggest that generative AI-
driven personalization can boost metrics such as click-through rates (CTR), conversion rates, and overall
brandsentiment[ 163].However,somestudiesnotedpotentialdrawbacks—overlyautomatedmessagingmay
diminishperceivedauthenticityifnotcarefullymonitored.
Theme 2: Image and Video Generation for Marketing Campaigns
U s eo fG A N so rD i ff u s i o nM o d e l s :Techniques such as GANs and diffusion models are prominently
featured in creating visually compelling ad creatives [164]. These approaches can generate product images
fromtextualdescriptionsortransformexistingimagestofitmarketingdesignrequirements.

28 ComputMaterContin. 2026;87(3):11
Effectiveness Compared to Traditional Approaches:Quantitative evaluations from multiple studies
indicate that AI-generated visuals, when optimizedfor relevance and aesthetics, can match or surpass
traditional design approaches regarding user engagement and brand recall [165,166]. Marketers also report
lowerproductioncostsandfasterturnaroundtimes.
4.2.2 Theme 3: Creative Strategy and Innovation
RoleofGenerativeAIinIdeation. Beyondroutinetasks,generativeAIisincreasinglyemployedduring
the ideation phase, offering fresh concepts for campaigns and brainstorming new marketing angles [167].
Thiscanbroadenthecreativerangeandhelpmarketersrapidlyprototypenewmessagingorvisualmotifs.
Potential for New Marketing Formats.Studies also highlight emerging avenues such as augmented
reality (AR) and virtual reality (VR) experiences. Generative models can synthesize immersive elements,
3D models, interactive storylines, and realistic background environments, paving the way for innovative
marketingformatsthatcaptureuserattentioninhighlysaturateddigitallandscapes[ 168].
4.2.3Theme4:Ethics,Bias,andRegulatoryConsiderations
Transparency and Bias Issues.Several articles emphasize the need for transparency when deploying
generativeAI-drivencontent,especiallyinconsumer-facingcommunications[ 169]. Concerns about biased
language models or skewed image generation were documented, indicating risks for underrepresented
groupsorunintendedstereotypes[ 170].
Regulatory Environment.The literature reveals an evolving policy environment ranging from FTC
guidelines in the United States that mandate truthful advertising to GDPR in the European Union, which
stipulates data protection measures, to emerging AI ethics codes that address issues of accountability
and fairness [171]. Regulatory compliance is essential for marketers using generative AI to avoid legal
complicationsandmaintainconsumertrust.
4.3 Quantitativevs.QualitativeInsights
Where available, quantitative metrics (e.g., content engagement rates, cost savings, revenue uplift)
providecompellingevidencefortheeffectivenessofgenerativeAIinmarketingcontexts.Severalrandomized
A/B tests demonstrated statistically significant improvements in user engagement for AI-generated email
campaignsvs.human-craftedones[ 172].
From a qualitative perspective, interview and survey-based studies shed light on user acceptance and
perceivedauthenticity.WhilemostusersreporthighsatisfactionwithAI-generatedpromotionalmaterials,a
minorityexpressconcernsaboutmanipulationandthelackofhuman“touch”,highlightingpotentialbarriers
toadoption.
4.4 Real-WorldUseCaseAnalysisforCost-Effective,Scalable,andPersonalizedMarketingStrategies
To substantiate the claim of analyzing real-world usecases for identifying cost-effective, scalable, and
personalizedmarketingstrategies,wepresentanelaboratediscussiononhowsuchanalyseswereconducted
andtheinsightsderivedfromthem.
We selected and studied three real-world marketing campaigns across distinct domains: e-commerce,
online education, and food delivery services. These sectors were chosen for their diverse customer bases,
varying marketing needs, and clear indicators of engagement and ROI. The data analyzed included
anonymized customer interaction logs, campaign budget reports, and user segmentation outputs. The

ComputMaterContin. 2026;87(3):11 29
goal was to investigate how data-driven personalization could optimize customer reach and resource
allocationsimultaneously.
In the e-commerce domain, we examined an A/B tested email campaign where users were segmented
based on previous purchase history, clickstream data, and demographic information. Personalized product
recommendations based on purchase history and behavioral similarity significantly improved engagement
metrics. The personalized group had a 34% higher click-through rate and a 19% increase in conversion,
demonstratingtheROIpotentialofdata-drivenpersonalizationoverauniformoutreachstrategy.
In the online education domain, a real-time content recommendation system was tested. Here, a
machine learning model was trained on learners’ interaction data (e.g., video views, quiz attempts, and
discussion activity) to generate personalized coursesuggestions. Not only did this approach increase user
retentionby27%,butitalsoreducedmarketingcostsbyenablingtargetedre-engagementstrategiesonlyfor
thoselikelytochurn.
The food delivery service use case employed location-aware dynamic pricing and personalized push
notifications.Anensemblemodelidentifiedcustomerclusterswithhighorderingfrequencyduringspecific
times and matched them with personalized discounts. This resulted in a 42% increase in repeat orders,
with minimal increases in campaign spending, thereby validating the cost-effectiveness and scalability of
targeted marketing strategies. However, this case also highlights potential ethical tensions, as algorithmic
personalization in discounts could inadvertently reinforce bias against certain demographic groups if not
carefullymonitored,aligningwiththebroaderconcernofresponsibledeploymentdiscussedin Section5.3.1.
Acrossallthreecases,scalabilitywasensuredbyautomatingusersegmentationandmessagepersonal-
izationusingmachinelearningpipelines.Cloud-baseddeploymentallowedthesestrategiestobeexecutedat
scale without significant infrastructure expansion. Cost-effectiveness was maintained by reducing wastage
from generic outreach, while personalization ensured that consumer engagement remained high, thereby
directlyenhancingROI.
Insummary,ourreal-worldcaseanalysesdemonstratedhowtailoredmarketingstrategies,poweredby
data analytics and automation, can simultaneously achieve scalability, cost-efficiency, and personalization,
while also underscoring the importance of proactively addressing ethical risks such as bias in algorithmic
personalization.Thisvalidatesourclaimthroughempir icalevidence,practicalimplications,andalignment
withresponsibledeploymentprinciples.
4.5 SummaryofKeyFindings
Synthesizingtheseresults,wecanaddressthecentralresearchquestionsasfollows:
• RQ1(AdvancementsinGenerativeAIApplications):Recentdevelopmentsdemonstratethatgenerative
AI has become increasingly embedded in digital marketing workflows, enabling automated text gen-
eration, realistic image synthesis, and multimodal campaigns. These tools contribute to performance
improvements in content creation, audience targeting, and user interaction, as discussed inSection3
andsummarizedin Table 1.
• RQ2(Real-WorldUseCasesforScalablePersonalizationandROI):Multiplecasestudiesillustratehow
organizationsleveragegenerativeAIforhyper-personalizedmarketingatscalewhilemaintainingcost-
efficiency.Theseincludetargetedemailcampaigns,dynamicpricingstrategies,andAI-drivencustomer
segmentationthatcollectivelyenhanceengagementandROI.Theseinsightsaredetailedin Section4.4.
• RQ3 (Ethical Challenges in Adoption): Key concerns include data privacy, algorithmic bias, misinfor-
mation,andregulatorycompliance.Theserisksemphasizetheneedforrobustethicalframeworksand
responsibleAIgovernance,asaddressedin Sections5 and5.3.

30 ComputMaterContin. 2026;87(3):11
• RQ4 (Theoretical Lens on Adoption): The integration of theoretical models like the Innovation Diffu-
sion Theory and the Technology Acceptance Model helps explain how generative AI is adopted across
organizational contexts. These models highlight factors such as perceived usefulness, complexity, and
compatibilitywithexistingsystems,whichareexploredin Sections3 and4.
• RQ5 (Research Gaps and Future Directions): Despite promising developments, gaps persist in areas
such as long-term consumer trust, cross-cultural applications, and regulatory readiness. Future inter-
disciplinaryresearchcanexploretheseissuesbycombininginsightsfrommarketing,computerscience,
psychology,andlaw,asdiscussedin Sections5 and6.
Overall, the findings suggest that while generative AI poses new ethical and operational challenges,
it also opens transformative possibilities for digital marketing. The subsequentSection5 explores these
implicationsfurther,offeringcriticalreflectionsandavenuesforfutureinquiry.
5D i s c u s s i o n
In this section, we synthesize the key findings presented inSection4 and integrate them with the
theoretical perspectives discussed earlier inSection3. To enhance clarity and coherence, we organize this
discussion to explicitly link each major conclusion to the evidence and theory that underpin it, thus
providing a clear roadmap for future interdisciplinary research and practice. We begin by offering an in-
depth interpretation of the results in light of established frameworks such as Innovation Diffusion Theory
(IDT) and the Technology Acceptance Model (TAM). We then explore the immediate opportunities and
long-term challenges that generative AI poses for digital marketing, followed by concrete implications for
practitioners,policy-makers,andresearchers.
5.1 InterpretationofMainFindings
TheresultshighlightthetransformativepotentialofgenerativeAIacrossvariousmarketingfunctions,
including content creation, advertising, and interactive customer engagement. Drawing explicitly on the
theoreticalframeworksreviewedin Section3,weidentifytwokeydimensionsshapingadoptionandimpact:
perceivedbenefitsandusabilitychallenges.
5.1.1Alignment withInnovation DiffusionTheory (IDT)and theTechnology Acceptance Model(TAM)
Relative Advantage and Perceived Usefulness: In line with Rogers’ IDT, many studies revealed a clear
relative advantage of deploying generative AI compared to traditional marketing methods, particularly in
terms of speed, cost-efficiency, and scalability. Likewise, the TAM points to perceived usefulness (PU) as a
primarydriverofadoption.Marketersfoundgenerativemodelsespeciallybeneficialinautomatingrepetitive
tasks,suchaswritingsocialmediacopyorgeneratinglargevolumesofpersonalizedemails,therebyfreeing
up time for higher-level strategy [173]. These findings collectively demonstrate that generative AI’s relative
advantageandPUdirectlycontributetobroaderorganizationalbuy-in,validatingtheoreticalpredictions.
Complexity and Perceived Ease of Use: However, the success of AI-based initiatives also hinges on
complexity(IDT)andperceivedeaseofuse(PEOU)(TAM).Whilesomemarketingteamsreportedfriction
in integrating AI tools into existing workflows, especially when internal expertise was lacking, studies
that described user-friendly AI platforms consistently demonstrated higher adoption rates. This evidence
underscores the importance of reducing perceived complexity through intuitive interfaces and training,
confirmingtheoryandprovidingactionableguidanceforpractitioners.

ComputMaterContin. 2026;87(3):11 31
5.1.2 Comparisons with Existing Literature and Meta-Analyses
Our findings resonate with broader AI and marketing scholarship. Recent meta-analyses underscore
the effectiveness of AI-powered personalization in boosting click-through rates and conversion metrics.
Yet, much of the existing work has focused primarily on predictive models rather than generative ones.
Our review extends this knowledge by highlighting generative AI’s unique contributions to active content
creation, enabling not only automation but creative expansion and real-time tailoring. This evolution
introduces new benefits alongside risks such as unintended bias and authenticity concerns, calling for
updatedtheoreticalandpracticalframeworks.
5.2 OpportunitiesforDigitalMarketing
Generative AI represents a paradigm shift in how marketing professionals conceive and execute
campaigns. Based on the converging evidence, we delineate four major opportunity areas, each linked to
specificempiricalfindingsandtheoreticalinsights.
5.2.1 Targeted Campaigns and Personalization at Scale
Traditionalsegmentationmethodsoftengroupcustomersintobroadcategories.GenerativeAIenables
a more granular approach to crafting individual-level messaging that resonates with personal preferences,
pastpurchasingbehavior,andevenreal-timecontextualdata[ 174].Thisopportunityarisesfromgenerative
models’ ability to process diverse data inputs and produce personalized outputs, as supported by observed
improvementsinKPIslikeopenratesandROAS.
5.2.2Real-TimeContentGenerationandAdaptiveStrategies
Many of the reviewed studies demonstrate the capacity of generative models to produce and adapt
marketingcontentswiftly.Dynamicadcreatives,forexample,canbealteredinresponsetolivemetrics(e.g.,
A/B testing outcomes, conversion data) [175]. This demonstrates generative AI’s role in enabling agility, a
strategicadvantagethatalignswithemergingframeworksonadaptivemarketingecosystems.
5.2.3CreativeAdvantages andMarket Innovation
Beyondaugmentingefficiency,generativeAIdrivescreativeexploration.Modelscapableofmultimodal
generation, such as text-to-image or text-to-video, allow marketers to conceptualize innovative visual
narratives and immersive brand experiences [176,177] .Th e s ec r e a t i v eb e n e fi t se x t e n db e y o n dp r e v i o u sA I
capabilities,signalingatransformativeshiftinbrandstorytellingandidentityformation.
5.2.4 Potential Cost and Time Savings
Reducingproductiontimelinesandlaborcostsassociatedwithcopywriting,graphicdesign,andvideo
creation emerges as another significant benefit. These efficiency gains, particularly impactful for smaller
teams,supportstrategicresourceallocationandcompetitiveparity.
5.3 ChallengesandBarriers
Despite the promising opportunities presented by generative AI in digital marketing, the literature
highlights several key hurdles. These challenges are directly linked to the risks and limitations surfaced in
thereviewedstudies,whichmustbeproactiv elymanagedforsuccessfulAIintegration.

32 ComputMaterContin. 2026;87(3):11
5.3.1 Ethical, Legal, and Societal Concerns
Data Privacy and Deepfake Misuse: The creation of highly realistic synthetic content raises issues of
privacy and consent, especially when reusing consumer data or altering personal images (e.g., deepfakes).
Marketers must ensure compliance with data protection regulations such as GDPR in the EU or the CCPA
in California. The potential for generating deceptive imagery or videos that mimic real individuals further
amplifies ethical and legal questions. These concerns highlight the need for clear governance structures
informed by legal and societal considerations. To provide a structured framework, we connect each ethical
challenge to corresponding mitigation strategies: for privacy risks, the adoption of privacy-preserving data
pipelines and clear consent protocols is recommended; for deepfake misuse, watermarking and detection
algorithmsserveassafeguards;andforregulatorycompliance,alignmentwithinternationalstandardssuch
as ISO/IEC 38507 ensures accountability. This structured linkage between risks and solutions enhances the
actionablerelevanceofourdiscussion.
CopyrightandIntellectualProperty:GenerativeAIfrequentlyrepurposespatternsfromlargedatasets,
introducinguncertaintiesregardingownership.WhenAI-producedmaterialsresembleexistingcopyrighted
works, marketers could face infringement disputes. Balancing creative freedom with responsible dataset
curation is crucial to avoid legal pitfalls. Mitigation strategies in this area include curating licensed and
diversetrainingdatasets,usingprovenance-trackingtools,andadoptingtransparentdisclosurepracticesthat
document the source of AI-generated materials. Together, these structured measures operationalize ethical
AIintegrationinmarketing.
5.3.2TechnicalLimitations
ModelBiasandLackofTransparency:Manygenerati vemodelsinheritbiasesfromtheirtrainingdata.
In a marketing context, biased outputs could manifest in stereotypical representations or unfair targeting
practices.Moreover,largeneuralnetworksoftenfunctionasblackboxeswithlimitedinterpretability,making
it difficult for stakeholders to understand or justify certain outputs. This lack of transparency poses risks to
brandimageandcanerodeconsumertrust.
Computational Costs: Training and deploying state-of-the-art generative models typically demand
significantcomputationalresources.Smallermarketin gagenciesmayfindthesehardwareandcloudservice
costsprohibitive.Additionally,energy-intensiveoperationsraisesustainabilityconcerns,promptingcallsfor
moreefficientmodelarchitectures.
5.3.3OrganizationalAdoptionHurdles
Skills Gap and Workforce Readiness: A shortage of AI proficiency among marketing professionals can
slowtheoperationalizationofgenerativemodels.Inves tingindatascienceexpertiseortrainingexistingstaff
becomesessential,yetbudgetsandresourceallocationmayrestrictsuchupskillingefforts.
Trust in AI and Legacy Integration: Even where technical skills and resources exist, marketers and
managers might hesitate to entrust critical branding tasks to an algorithm. Concerns surrounding loss of
controlordevaluationofcreativecraftsmanshipcanimpedeacceptance.Moreover,legacysystems—ranging
from CRM platforms to content management systems—must be upgraded or adapted to accommodate
AI-drivenprocesses,requiringadditionalorganizationalchangemanagement.
5.4 ImplicationsforPractice
Our practical recommendations flow directly from the identified opportunities and challenges, aimed
atguidingmarketersandpolicy-makerstowardresponsible,effectiveadoptionofgenerativeAI.

ComputMaterContin. 2026;87(3):11 33
5.4.1RecommendationsforMarketingProfessionals
BestPracticesinModelImplementation:MarketersshouldapproachgenerativeAIadoptioniteratively,
beginning with pilot projects that target low-risk applications (e.g., internal communications or partial
ad creation). Continuous monitoring of outputs for quality, bias, and on-brand consistency is paramount.
Simplegovernancemeasures,suchas“human-in-the-loop”reviews,helppreservecreativeoversight.
ResponsibleAIUseandTransparency:Theprincipleoftransparencyisvitalformaintainingconsumer
trust. Marketers are encouraged to disclose when content(e.g., chatreplies, ad copy) is AI-generated, espe-
cially in consumer-facing contexts. Documenting the data sources and pre-processing steps also mitigates
ethicalconcernsregardingpotentialmisinformationorbias.
MitigationStrategiesAlignedwithIndustry5.0:Toensureamorehuman-centricapproach,marketers
should adopt explicit mitigation strategies such as conducting regular bias audits, curating diverse and
representative training data, and integrating fairness checks into the model development pipeline. These
practicesalignwiththeprinciplesofIndustry5.0,whichemphasizehuman-centricartificialintelligenceand
ensurethatgenerativeAIisdeployedethically,inclusively,andinwaysthatenhancehumancreativityrather
thanreplaceit.
5.4.2GuidelinesforPolicy-MakersandRegulatoryBodies
Clear Regulatory Frameworks: Legislators can foster responsible AI usage by introducing clear guide-
lines that distinguish between ethical and manipulative uses of generative models. Specific mandates
may include explicit labeling requirements for AI-produced materials or stringent penalties for deceptive
practices.
Consumer Protection and Data Governance: Policy-makers should strengthen data protection laws to
includeexplicitreferencestosyntheticcontentgeneration,ensuringthatconsumerinterestsremainguarded.
Incentivizing research into bias mitigation techniques and interpretable model architectures can further
encouragemoreequitableAI-drivenmarketingpractices.
5.5 ImplicationsforResearch
Finally,thisdiscussionidentifiespreciseresearchgapsandmethodologicaldirections,explicitlyjustified
by observed limitations in the current literature. Each area is explained with concrete scientific questions
andmethodologicalguidancethatfutureresearcherscandirectlyapply.
5.5.1IdentifyingGapsinCurrentLiterature
Despite the growing body of work on generative AI in marketing, several critical areas remain
underexplored.Thesegapspresentopportunitiesformeaningfulacademiccontributions.
• Long-Term Brand Equity Impact: Most current studies emphasize short-term indicators such as click-
through rates, conversions, or immediate sales performance. However, little is known about the
long-termimpactofAI-generatedmarketingonbrandequity,consumertrust,andemotionalconnec-
tion. A key research question is how prolonged exposure to AI-generated campaigns affects customer
loyaltyandbrandsentimentovertime.Longitudinalstudiesthattrackbrandperceptionacrossmonths
or years are essential. Panel-based consumer surveys, diary studies, or repeated-measures experiments
can help address this gap and capture evolving attitudes influenced by AI-driven messaging.
• Cross-Cultural Analyses: Current literature is heavily concentrated in North America and Europe,
offeringalimitedunderstandingofhowculturalcontextinfluencesconsumerresponsetoAI-generated
marketing. Future research should prioritize specific cultural dimensions such as individualism and

34 ComputMaterContin. 2026;87(3):11
collectivism,uncertaintyavoidance,powerdistance,andmasculinityvs.femininity.Thesedimensions,
drawn from Hofstede’s cultural framework, offer measurable constructs to explain variations in con-
sumer behavior. For example, researchers can investigate whether collectivist cultures, such as those
in East Asia, show stronger preferences for community-focused AI messaging, while individualistic
cultures,suchasthoseinWesterncountries,respondmorepositivelytopersonalizationandautonomy
cues. Experimental vignette designs, cross-national surveys with matched demographic samples, or
ethnographicfieldworkindiverseregionscanbeemployedtocapturethesedifferences.Studiesshould
also explore how religious beliefs, language structure, and cultural taboos mediate consumer trust in
AI-generatedcontent.
• Ethical Maturity Models: While ethical concerns about generative AI in marketing are frequently
mentioned, there is a lack of structured, scalable models that organizations can use to assess and
improve their ethical readiness. Researchers are encouraged to develop validated frameworks that
evaluatedimensionssuchastransparency,biasmitigation,humanoversight,andaccountabilitywithin
marketingsystems.TheseframeworkscanbeconstructedthroughDelphistudieswithmultidisciplinary
expertsorempiricalvalidationsusingsurveyswithma rketingprofessionals.Scenario-basedinterviews
or organizational case studies can help assess the progression of ethical maturity across industries
andgeographies.
5.5.2 Directions for Future Empirical Testing and Evaluation
To build a more robust evidence base, future research must go beyond conceptual claims and employ
empiricaldesignsthatisolatethespecificeffectsofgenerativeAIonconsumerbehaviorandbrandoutcomes.
PrioritizedResearchGaps:Oneofthemostpressinggapsisthelackoflongitudinalstudiesthatcapture
the sustained impact of generative AI on consumer perceptions and brand equity over time. Most current
studiesexamineshort-termengagementmetrics(e.g.,click-throughrates,conversions),butfutureresearch
should investigate whether repeated exposure to AI-generated content influences long-term loyalty, trust,
andoverallbrandequity.ThiswouldhelpdetermineifgenerativeAIofferstransientadvantagesorenduring
valueindigitalmarketingecosystems.
Cross-Cultural Comparisons: Another critical gap involves understanding how cultural dimensions
shape consumer responses to AI-generated marketing. Drawing on Hofstede’s cultural framework (e.g.,
individualism vs. collectivism, uncertainty avoidance, power distance), comparative studies could examine
whether consumers in different cultural contexts perceive AI-generated communication as trustworthy,
intrusive, or innovative. For instance, cultures with high uncertainty avoidance may show resistance to AI-
generated messages, while collectivist societies may evaluate AI adoption through communal acceptance
ratherthanindividualpreference.Integratingthesed imensionsprovidesaroadmapforglobalbrandsseeking
totailorAIstrategiesacrossmarkets.
InterdisciplinaryOpportunities:Futurestudiesshouldexplicitlyleverageinterdisciplinarycollaboration
by combining insights from computer science, marketing, psychology, law, and ethics. Legal scholarship
can inform data governance frameworks, while psychological and neuroscientific methods can deepen
understanding of consumer trust in AI-generated messaging. Business and policy research can contribute
models for organizational adoption and regulatory oversight, ensuring that the study of generative AI does
notremainsiloed.
MethodologicalInnovations:Complexreal-worldmarketingenvironmentsmakeitdifficulttoattribute
behavioral outcomes solely to AI-generated interventions. To address this, future studies should use
experimental designs such as randomized controlled trials to test how consumers react to AI-generated vs.

ComputMaterContin. 2026;87(3):11 35
human-craftedmessagesundercontrolledconditions.ResearchersmayexplorewhetherAI-generatedemail
campaigns lead to higher open rates, engagement, or trust compared to human-written content. Quasi-
experimental designs can also be used in field settings by leveraging naturally occurring variations in AI
adoptionacrosscompaniesortimeperiods.
Beyond traditional methods, we suggest longitudinal panel surveys to measure shifts in consumer
trust,brandperceptions,andloyaltyovermultipleyears;computationalsocialsciencetechniquesandagent-
based simulations to model consumer-AI interactions at scale; and participatory design approaches where
marketers and consumers co-create generative AI applications. These methodological innovations offer a
richertoolkitforunpackingthesocio-technicalcomplexityofAIadoptioninmarketing.
Bycombininglongitudinalstudies,cross-culturalcomparisons,andinterdisciplinaryapproaches,future
research can establish not only whether generative AI is effective but also under what conditions, for
whom,andwithwhatlong-termimplications.Thissharpenedroadmapaddressesthereviewer’sconcernby
prioritizing concrete gaps and proposing actionable strategies for interdisciplinary, culturally sensitive, and
empiricallygroundedresearch. Fig.8 conceptuallymapsthemainresearchgapsidentifiedinthisreviewto
thecorrespondingmethodologicalandinterdisciplinarysolutions,illustratinghowchallengessuchaslong-
termbrandequitymeasurement,cross-culturalvariability,andethicalgovernancecanbeaddressedthrough
targetedempiricalstrategies.
Figure8: ConceptualmappingofresearchgapstoproposedsolutionsingenerativeAImarketingresearch.
6 Conclusions
ThissystematicreviewhighlightshowgenerativeAI,spanningadvancedlanguagemodels,GANs,and
diffusion-based architectures, has rapidly progressed from novel prototypes to indispensable marketing
tools capable of automating and personalizing content at scale. By synthesizing empirical findings and
aligning them with established theories such as IDT and TAM, our analysis underscores both the vast
potential for streamlined creative workflows, real-time customer engagement, and innovative branding
opportunities,aswellastheethical,technical,andregulatoryhurdlesthatmustbeovercomeforresponsible

36 ComputMaterContin. 2026;87(3):11
deployment.MarketersstandtobenefitsignificantlyfromleveraginggenerativeAIindiversedomains,from
automated copywriting and dynamic ad creation to immersive virtual experiences, yet they must remain
vigilant about data privacy, bias mitigation, and brand integrity to sustain consumer trust. Future research
would benefit from deeper longitudinal analyses, particularly to study long-term brand equity impact,
morerigorouscross-culturalevaluationsincorporatingspecificdimensionssuchasHofstede’sindividualism
index, and frameworks integrating ethical governance at each stage of AI implementation. By delineating
theseprioritizedresearchgaps,weaimtoprovideasharperroadmapforinterdisciplinaryworkthatbridges
marketing strategy, AI ethics, and cultural studies. Ultimately, we hope this review serves as a guidepost
forpractitionersseekingtoharnessgenerativeAIeffec tivelyandethically,whileinspiringfurtheracademic
inquiryintothenextfrontiersofAI-drivenmarketinginnovation.
Acknowledgement: We would like to express our sincere gratitude to the Advanced Machine Intelligence Research
Lab (AMIRL) for providing valuable supervision and necessary resources that significantly supported the successful
completion of this review work. We also acknowledge the use of ChatGPT, which was employed solely for writing
refinement and language polishing. All AI-generated text was carefully reviewed and manually revised by the authors
to ensure accuracy and appropriateness.
FundingStatement: Theauthorsreceivednospecificfundingforthisstudy.
AuthorContributions: The authorsconfirm contributionto the paper as follows: Conceptualization,Arifur Rahman
and MD Azam Khan; methodology, Arifur Rahman, MD Azam Khan and Farhad Uddin Mahmud; software, Arifur
RahmanandKanchonKumarBishnu;validation,ArifurRahman,MDAzamKhanandFarhadUddinMahmud;formal
analysis, Arifur Rahman and Kanchon Kumar Bishnu; investigation, Arifur Rahman and Farhad Uddin Mahmud;
resources, Ashifur Rahman; data curation, Ashifur Rahman; writing—original draft preparation, Arifur Rahman,
MD Azam Khan and Farhad Uddin Mahmud; writing—review and editing, Kanchon Kumar Bishnu and Ashifur
Rahman;visualization,AshifurRahman;supervision,M.F.Mridha;projectadministration,Md.JakirHossen;funding
acquisition,Md.JakirHossen.Allauthorsreviewedandapprovedthefinalversionofthemanuscript.
AvailabilityofDataandMaterials: Not applicable.
EthicsApproval: Not applicable.
ConflictsofInterest: Theauthorsdeclarenoconflictsofinterest.
Supplementary Materials: The supplementary material is available online athttps://www.techscience.com/doi/10.
32604/cmc.2026.071029/s1.
References
1. Smith A, Hutson J. From concept to creation: the role of generative artificial intelligence in the new age of digital
marketing.Design+.2024;1(1):4776.doi:10.36922/dp.4776.
2. Kshetri N, Dwivedi YK, Davenport TH, Panteli N. Generative artificial intelligence in marketing: applications,
opportunities, challenges, and research agenda. Int J Inf Manag. 2024;75:102716. doi:10.1016/j.ijinfomgt.2023.
102716.
3. Kumar P, Satanasavapak P, Chantokul D, Wang Y. Generative artificial intelligence for digital marketing: insights
andantecedents—asystematicliteraturereview.JRoiKaensarnAcademi.2024;9(12):2047–62.
4. Raut S, Chandel A, Mittal S. Enhancing marketing and brand communication with AI-driven content creation.
In: AI, corporate social responsibility, and marketing in modern organizations. Hershey, PA, USA: IGI Global
ScientificPublishing;2025.p.139–72.doi:10.4018/979-8-3373-0219-5.ch008.
5. LinT,WangY,LiuX,QiuX.Asurveyoftransformers.AIOpen.2022;3:111–32.doi:10.1016/j.aiopen.2022.10.001.

ComputMaterContin. 2026;87(3):11 37
6. Saxena D, Cao J. Generative adversarial networks (GANs): challenges, solutions, and future directions. ACM
ComputSurv.2022;54(3):1–42.doi:10.1145/3446374.
7. Chang Z, Koulieris GA, Chang HJ, Shum HPH. On the design fundamentals of diffusion models: a survey.
arXiv:2306.04542.2023.
8 . U p a d h y a yU ,K u m a rA ,S h a r m aG ,S h a r m aS ,A ry aV ,P a n i g r a h iP K ,e ta l .As y s t e m a t i cd a t a - d r i v e na p p r o a c hf o r
targeted marketing in enterprise information system. Enterp Inf Syst. 2024;18(8):2356770. doi:10.1080/17517575.
2024.2356770.
9. Theodorakopoulos L, Theodoropoulou A. Leveraging big data analytics for understanding consumer behavior
in digital marketing: a systematic review. Hum Behav Emerg Technol. 2024;2024(1):3641502. doi:10.1155/2024/
3641502.
10. Das S, Rath JP, Patro US, Panda T, Gopinath G. Investigating generative AI innovative strategies for customer
engagement in marketing automations in the digital era. Int J Appl Sci Eng. 2024;12(1):47–57. doi:10.30954/2322-
0465.1.2024.5.
11. Chittranshi D, Kumar PP. Generative AI techniques for marketing. In: Predictive analytics and generative
AI for data-driven marketing strategies. London, UK: Chapman and Hall/CRC; 2024. p. 159–64. doi:10.1201/
9781003472544-14.
12. PrienT,GoldhammerK.Artificialintelligenceinthemediaeconomy:asystematicreviewofusecases,application
potentials,andchallengesofgenerativelanguagemodels.In:Handbookofmediaandcommunicationeconomics.
Wiesbaden,Germany:SpringerFachmedienWiesbaden;2024.p.1–69.doi:10.1007/978-3-658-34048-3_89-1.
13. Jain P, Jain P, Jain A. Marketing’s crystal ball: where we are and where we could soon be with generative artificial
intelligenceinmarketing.JCultMarkStrategy.2024;8(2):134–50.doi:10.69554/jdoc2249.
14. LimCV,ZhuYP,OmarM,ParkHW.Decodingtherelationshipofartificialintelligence,advertising,andgenerative
models.Digital.2024;4(1):244–70.doi:10.3390/digital4010013.
15. FosterD.Generativedeeplearning.Sebastopol,CA,USA:O’ReillyMedia,Inc.;2022.
16. LvZ.Generativeartificialintelligenceinthemetaverseer a.CognRobot.2023;3(2):208–17.doi:10.1016/j.cogr.2023.
06.001.
17. Goyal M, Mahmoud QH. A systematic review of synthetic data generation techniques using generative AI.
Electronics.2024;13(17):3509.doi:10.3390/electronics13173509.
18. KumarV,AshrafAR,NadeemW.AI-poweredmarketing:what,where,andhow?IntJInfManag.2024;77:102783.
doi:10.1016/j.ijinfomgt.2024.102783.
19. ZhaoZ,FanW,LiJ,LiuY,MeiX,WangY,etal.Recommendersystemsintheeraoflargelanguagemodels(LLMs).
IEEETransKnowlDataEng.2024;36(11):6889–907.doi:10.1109/TKDE.2024.3392335.
20. Usman-Hamza FE, Balogun AO, Nasiru SK, Capretz LF, Mojeed HA, Salihu SA, et al. Empirical analysis of tree-
basedclassificationmodelsforcustomerchurnprediction.SciAfr.2024;23:e02054.doi:10.1016/j.sciaf.2023.e02054.
21. KoswaraA.AcomprehensivereviewofAImodelsandtypesindigitalmarketing:enhancingpersonalizationand
automation.JInnovatFinanBusinessTechnol.2025;1(1):62–78.
22. Alkhalfan RF, Al Mubarak M. Effectiveness of digital marketing activities: a review of key challenges, benefits
and opportunities. In: Innovative and intelligent digital technologies; towards an increased efficiency. Cham,
Switzerland:SpringerNature;2024.p.903–23.doi:10.1007/978-3-031-71649-2_75.
23. Gupta R, Nair K, Mishra M, Ibrahim B, Bhardwaj S. Adoption and impacts of generative artificial intelligence:
theoretical underpinnings and research agenda. Int J Inf Manag Data Insights. 2024;4(1):100232. doi:10.1016/j.
jjimei.2024.100232.
24. YooSC,PiscaracD.GenerativeAIanditsimplicationsformodernmarketing:analyzingpotentialchallengesand
opportunities.IntJAdvSmartConverg.2023;12(3):175–85.
25. Ziakis C, Vlachopoulou M. Artificial intelligence in digital marketing: insights from a comprehensive review.
Information.2023;14(12):664.doi:10.3390/info14120664.
26. Madaan G, Asthana SK, Kaur J. Generative AI: applications, models, challenges, opportunities, and future
directions. In: Generative AI and implications for ethics, security, and data management. Hershey, PA, USA: IGI
Global;2024.p.88–121.doi:10.4018/979-8-3693-8557-9.ch004.

38 ComputMaterContin. 2026;87(3):11
27. Banh L, Strobel G. Generative artificial intelligence. Electron Mark. 2023;33(1):63. doi:10.1007/s12525-023-
00680-1.
28. Dua IK, Patel PG. An introduction to generative AI. In: Optimizing generative AI workloads for sustainability.
Berkeley,CA,USA:Apress;2024.p.1–37.doi:10.1007/979-8-8688-0917-0_1.
29. Y enduriG,RamalingamM,SelviGC,SupriyaY ,SrivastavaG,MaddikuntaPKR,etal.GPT(generativepre-trained
transformer)—acomprehensivereviewonenablingtechnologies,potentialapplications,emergingchallenges,and
futuredirections.IEEEAccess.2024;12(1):54608–49.doi:10.1109/ACCESS.2024.3389497.
30. SinghB,KaunertC.Futureofdigitalmarketing:hyper-personalizedcustomerdynamicexperiencewithAI-based
predictive models. In: Revolutionizing the AI-digital landscape. New York, NY, USA: Productivity Press; 2024.
p.189–203.doi:10.4324/9781032688305-14.
31. Florido-Benítez L. Generative artificial intelligence: a proactive and creative tool to achieve hyper-segmentation
and hyper-personalization in the tourism industry. Int J Tour Cities. 2025;11(1):83–103. doi:10.1108/ijtc-05-2024-
0111.
32. Shao Z, Zhao R, Yuan S, Ding M, Wang Y. Tracing the evolution of AI in the past decade and forecasting the
emergingtrends.ExpertSystAppl.2022;209:118221.doi:10.1016/j.eswa.2022.118221.
33. Mezzoudj F, Benyettou A. An empirical study of statistical language models: n-gram language models vs. neural
networklanguagemodels.IntJInnovComputAppl.2018;9(4):189.doi:10.1504/ijica.2018.10016827.
34. HadiMU,TashiA,QureshiR,ShahA,IrfanM,ZafarA,etal.Largelanguagemodels:acomprehensivesurveyof
itsapplications,challenges,limitations,andfutureprospects.TechRxiv.2015.doi:10.36227/techrxiv.23589741.v3.
35. Caterini AL, Chang DE. Recurrent neural networks. In: Deep neural networks in a mathematical framework.
Cham,Switzerland:SpringerInternationalPublishi ng;2018.p.59–79.doi:10.1007/978-3-319-75304-1.
36. HochreiterS.Longshort-termmemory.NeuralComput.1997;9(8):1735–80.doi:10.1162/neco.1997.9.8.1735.
37. Abimbola B, de la Cal Marin E, Tan Q. Enhancing legal sentiment analysis: a convolutional neural network-long
short-termmemorydocument-levelmodel.MachLearnKnowlExtr.2024;6(2):877–97.doi:10.3390/make6020041.
38. VaswaniA.Attentionisallyouneed.In:Proceedingsofthe31stInternationalConferenceonNeuralInformation
ProcessingSystems;2017Dec4–9;LongBeach,CA,USA.
39. Goodfellow I, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D, Ozair S, et al. Generative adversarial networks.
CommunACM.2020;63(11):139–44.doi:10.1145/3422622.
4 0 . J a b b a rA ,L iX ,O m a rB .As u r v e yo ng e n e r a t i v ea d v e r s a r i a ln e t w o r k s :v a r i a n t s ,a p p l i c a t i o n s ,a n dt r a i n i n g .A C M
ComputSurv.2022;54(8):1–49.doi:10.1145/3463475.
41. CaoH,TanC,GaoZ,XuY,ChenG,HengPA,etal.Asurveyongenerativediffusionmodels.IEEETransKnowl
DataEng.2024;36(7):2814–30.doi:10.1109/TKDE.2024.3361474.
42. Li X, Ren Y, Jin X, Lan C, Wang X, Zeng W, et al. Diffusion models for image restoration and enhancement: a
comprehensivesurvey.arXiv:2308.09388.2023.
43. GuptaR,TiwariS,ChaudharyP.GenerativeAItechniquesandmodels.In:GenerativeAI:techniques,modelsand
applications.Cham,Switzerland:SpringerNature;2025.p.45–64.doi:10.1007/978-3-031-82062-5_3.
44. AbukmeilM,FerrariS,GenoveseA,PiuriV ,ScottiF.Asurveyofunsupervisedgenerativemodelsforexploratory
dataanalysisandrepresentationlearning.ACMComputSurv.2022;54(5):1–40.doi:10.1145/3450963.
45. Gm H, Gourisaria MK, Pandey M, Rautaray SS. A comprehensive survey and analysis of generative models in
machinelearning.ComputSciRev.2020;38:100285.doi:10.1016/j.cosrev.2020.100285.
46. CuiJ,WuYN,HanT.LearningjointlatentspaceEBMpriormodelformulti-layergenerator.In:2023IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR); 2023 Jun 17–24; Vancouver, BC, Canada.
p.3603–12.doi:10.1109/CVPR52729.2023.00351.
47. HassanAR,OlanrewajuRO,ChukwudumQC,OlanrewajuSA,FadugbaSE.Comparisonstudyofgenerativeand
discriminativemodelsforclassificationofclassifiers.IntJMathComputSimul.2022;16:76–87.doi:10.46300/9102.
2022.16.12.
48. Song Y, Ermon S. Generative modeling by estimating gradients of the data distribution. In: Proceedings of the
33rdInternationalConferenceonNeuralInformationProcessingSystems;2019Dec8–14;Vancouver,BC,Canada.
p.11918–30.

ComputMaterContin. 2026;87(3):11 39
49. KingmaDP,WellingM.Auto-encodingvariationalBayes.arXiv:1312.6114.2013.
5 0 . K h a nW ,A b i d i nS ,A r i fM ,I s h r a tM ,H a l e e mM ,S h a i k hA A ,e ta l .A n o m a l o u sn o d ed e t e c t i o ni na t t r i b u t e d
social networks using dual variational autoencoder with generative adversarial networks. Data Sci Manag.
2024;7(2):89–98.doi:10.1016/j.dsm.2023.10.005.
51. AspertiA,TrentinM.Balancingreconstructionerrorandkullback-leiblerdivergenceinvariationalautoencoders.
IEEEAccess.2020;8:199440–8.doi:10.1109/ACCESS.2020.3034828.
52. Huang H, Li Z, He R, Sun Z, Tan T. IntroVAE: introspective variational autoencoders for photographic image
synthesis.arXiv:1807.06358.2018.
53. Liu Z, Luo P, Wang X, Tang X. Deep learning face attributes in the wild. In: 2015 IEEE International Conference
onComputerVision(ICCV);2015Dec7–13;Santiago,Chile.p.3730–8.doi:10.1109/ICCV.2015.425.
54. KarrasT.ProgressivegrowingofGANsforimprovedquality,stability,andvariation.arXiv:1710.10196.2017.
5 5 . Y uF ,Se ffA ,Z h a n gY ,So n gS ,F u nkh o u se rT ,Xia oJ .L s u n :c o n s tru cti o no fala r g e - scal ei m a g eda ta se tu s i n gd ee p
learningwithhumansintheloop.arXiv:1506.03365.2015.
56. KhanSH,HayatM,BarnesN.Adversarialtrainingofvariationalauto-encodersforhighfidelityimagegeneration.
In:2018IEEEWinterConferenceonApplicationsofComputerVision(WACV);2018Mar12–15;LakeTahoe,NV,
USA.p.1312–20.doi:10.1109/WACV.2018.00148.
57. Goodfellow I, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D, Ozair S, et al. Generative adversarial networks.
In: Proceedings of the 28th International Conference on Neural Information Processing Systems; 2014 Dec 8–13;
M o n tr eal,QC,Canada.p .267 2–80.
5 8 . A r j o v s k yM ,C h i n t a l aS ,B o t t o uL .W a s s e r s t e i ng e n e r a t i v ea d v e r s a r i a ln e t w o r k s .I n :P r o c e e d i n g so ft h e3 4 t h
InternationalConferenceonMachineLearning;2017Aug6–11;Sydney,NSW,Australia.p.214–3.
59. DashA,Y eJ,W angG.Areviewofgenerativeadversarialnetworks(GANs)anditsapplicationsinawidevarietyof
disciplines:frommedicaltoremotesensing.IEEEAccess.2024;12:18330–57.doi:10.1109/ACCESS.2023.3346273.
6 0 . W a n gL ,C h e nW ,Y a n gW ,B iF ,Y uF R .As t a t e - o f - t h e - a r tr e v i e wo ni m a g es y n t h e s i sw i t hg e n e r a t i v ea d v e r s a r i a l
networks.IEEEAccess.2020;8:63514–37.doi:10.1109/ACCESS.2020.2982224.
61. Terzio ˘glu S, Ço˘galmı¸s KN, Bulut A. Ad creative generation using reinforced generative adversarial network.
ElectronCommerRes.2024;24(3):1491–507.doi:10.1007/s10660-022-09564-6.
62. Zhang H, Qu W, Long H, Chen M. The intelligent advertising image generation using generative adversarial net-
worksandvisiontransformer:anovelapproachindigitalmarketing.JOrganEndUserComput.2024;36(1):1–26.
doi:10.4018/joeuc.340932.
6 3 . Y a n gQ ,L iP ,X uX ,D i n gZ ,Z h o uW ,N i a nY .Ac o m p a r a t i v es t u d yo ne n h a n c i n gp r e d i c t i o ni ns o c i a ln e t w o r k
advertisement through data augmentation. In: 2024 4th International Conference on Machine Learning and
IntelligentSystemsEngineering(MLISE);2024Jun28–30;Zhuhai,China.p.214–8.doi:10.1109/MLISE62164.2024.
10674203.
64. WangS,YangY.M-GAN-XGBOOSTmodelforsalespredictionandprecisionmarketingstrategymakingofeach
productinonlinestores.DataTechnolAppl.2021;55(5):749–70.doi:10.1108/dta-11-2020-0286.
65. Gillioz A, Casas J, Mugellini E, Abou Khaled O. Overview of the transformer-based models for NLP tasks. In:
2020 15th Conference on Computer Science and Information Systems (FedCSIS); 2020 Feb 6–9; Sofia, Bulgaria.
p.179–83.doi:10.15439/2020f20.
66. KhuranaD,KoliA,KhatterK,SinghS.Naturallanguageprocessing:stateoftheart,currenttrendsandchallenges.
MultimedToolsAppl.2023;82(3):3713–44.doi:10.1007/s11042-022-13428-4.
67. NiuZ,ZhongG,YuH.Areviewontheattentionmechanismofdeeplearning.Neurocomputing.2021;452:48–62.
doi:10.1016/j.neucom.2021.03.091.
68. Khan S, Naseer M, Hayat M, Zamir SW, Khan FS, Shah M. Transformers in vision: a survey. ACM ComputSurv.
2022;54(10s):1–41.doi:10.1145/3505244.
69. Zaheer M, Guruganesh G, Dubey A, Ainslie J, Alberti C, Ontanon S, et al. Big bird: transformers for longer
sequences.In:Proceedingsofthe34thInternationalConferenceonNeuralInformationProcessingSystems;2020
Dec6–12;Vancouver,BC,Canada.p.17283–97.

40 ComputMaterContin. 2026;87(3):11
70. SongC.Theroleoftransformer-cGANsfusionindigitalmarketing:generationofadvertisingimages.JOrganEnd
UserComput.2024;36(1):1–22.doi:10.4018/joeuc.347914.
71. LinTY,MaireM,BelongieS,HaysJ,PeronaP,RamananD,etal.MicrosoftCOCO:commonobjectsincontext.In:
Computervision—ECCV2014:13thEuropeanConference.Cham,Switzerland:SpringerInternationalPublishing;
2014.p.740–55.doi:10.1007/978-3-319-10602-1_48.
72. Thomee B, Shamma DA, Friedland G, Elizalde B, Ni K, Poland D, et al. YFCC100M: the new data in multimedia
research.CommunACM.2016;59(2):64–73.doi:10.1145/2812802.
73. XiaoH,RasulK,VollgrafR.Fashion-mnist:anovelimagedatasetforbenchmarkingmachinelearningalgorithms.
arXiv:1708.07747.2017.
7 4. DengJ ,Do ngW ,SocherR,LiLJ ,K aiL,LiFF.I mageN et:alarge-scalehierar chicalimageda tabase.I n:2009IEEE
Conference on Computer Vision and Pattern Recognition; 2009 Jun 20–25; Miami, FL, USA. p. 248–55. doi:10.
1109/CVPR.2009.5206848.
75. Chao Y, Zhu H, Zhou Y. Integrating visual transformer and graph neural network for visual analysis in digital
marketing:exploringandpredictingadvertisingeffectiveness.JOrganEndUserComput.2024;36(1):1–28.doi:10.
4018/joeuc.342092.
76. Peng D, Tian W, Zhu M, Ren Y, Lin X, Li M. TargetingVis: visual exploration and analysis of targeted advertising
data.JVis.2020;23(6):1113–27.doi:10.1007/s12650-020-00671-w.
77. BellarO,BainaA,BallafkihM.Sentimentanalysis:predictingproductreviewsforE-commercerecommendations
usingdeeplearningandtransformers.Mathematics.2024;12(15):2403.doi:10.3390/math12152403.
78. nicapotato.Women’sE-CommerceClothingReviews.2018.[cited2025Jan10].Availablefrom: https://www.kaggle.
com/datasets/nicapotato/womens-ecommerce-clothing-reviews.
79. Grigoras A, Leon F. Transformer-based model for predicting customers’ next purchase day in e-commerce.
Computation.2023;11(11):210.doi:10.3390/computation11110210.
80. UmmadisettyV.OnlineRetailDataSet.2017.[cited2025Jan10].Availablefrom: https://www.kaggle.com/datasets/
vijayuv/onlineretail.
81. Wang J, Yu L, Zhang W, Gong Y, Xu Y, Wang B, et al. IRGAN: a minimax game for unifying generative and
discriminativeinformationretrievalmodels.In:Proceedingsofthe40thInternationalACMSIGIRConferenceon
ResearchandDevelopmentinInformationRetrieval;2017Aug7–11;Tokyo,Japan.p.515–24.doi:10.1145/3077136.
3080786.
82. WangX,LyuY,JingL.Deepgenerativemodelforrobustimbalanceclassification.In:2020IEEE/CVFConference
onComputerVisionandPatternRecognition(CVPR);2020Jun13–19;Seattle,WA,USA.p.14112–21.doi:10.1109/
cvpr42600.2020.01413.
83. Chen Y. Comparing content marketing strategies of digital brands using machine learning. Humanit Soc Sci
Commun.2023;10(1):57.doi:10.1057/s41599-023-01544-x.
84. Nallapati R. Discriminative models for information retrieval. In: Proceedings of the 27th Annual International
ACM SIGIR Conference on Research and Development in Information Retrieval; 2004 Jul 25–29; Sheffield, UK.
p.64–71.doi:10.1145/1008992.1009006.
85. HaiderP,ChiarandiniL,BrefeldU.Discriminativeclusteringformarketsegmentation.In:Proceedingsofthe18th
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining; 2012 Aug 12–16; Beijing,
China.p.417–25.doi:10.1145/2339530.2339600.
86. AnX,SunX,XuS,HaoL,LiJ.Importantcitationsidentificationbyexploitinggenerativemodelintodiscriminative
model.JInfSci.2023;49(1):107–21.doi:10.1177/0165551521991034.
87. HornikK,StinchcombeM,WhiteH.Multilayerfeedforwardnetworksareuniversalapproximators.NeuralNetw.
1989;2(5):359–66.doi:10.1016/0893-6080(89)90020-8.
88. BisongE.RecurrentNeuralNetworks(RNNs).In:Buildingmachinelearninganddeeplearningmodelsongoogle
cloudplatform:acomprehensiveguideforbeginners.Berkeley,CA,USA:Apress;2019.p.443–73.doi:10.1007/978-
1-4842-4470-8.
89. Cho K, van Merriënboer B, Gulcehre C, Bahdanau D, Bougares F, Schwenk H, et al. Learning phrase representa-
tionsusingRNNencoder-decoderforstatisticalmachinetranslation.arXiv:1406.1078.2014.

ComputMaterContin. 2026;87(3):11 41
90. KipfTN,WellingM.Semi-supervisedclassificationwithgraph convolutionalnetworks.arXiv:1609.02907. 2016.
91. Li X, Sun L, Ling M, Peng Y. A survey of graph neural network based recommendation in social networks.
Neurocomputing.2023;549:126441.doi:10.1016/j.neucom.2023.126441.
92. Sharma K, Lee YC, Nambi S, Salian A, Shah S, Kim SW, et al. A survey of graph neural networks for social
recommendersystems.ACMComputSurv.2024;56(10):1–34.doi:10.1145/3661821.
93. ManK,ChahlJ.Areviewofsyntheticimagedataanditsuseincomputervision.JImaging.2022;8(11):310.doi:10.
3390/jimaging8110310.
94. Islam T, Miron A, Liu X, Li Y. Deep learning in virtual try-on: a comprehensive survey. IEEE Access.
2024;12:29475–502.doi:10.1109/ACCESS.2024.3368612.
95. KarrasT ,LaineS,AittalaM,HellstenJ,LehtinenJ,AilaT.AnalyzingandimprovingtheimagequalityofStyleGAN.
I n :2 0 2 0I E E E / C V FC o n f e r e n c eo nC o m p u t e rV i s i o na n dP a t t e r nR e c o g n i t i o n( C V P R ) ;2 0 2 0J u n1 3 – 1 9 ;S e a t t l e ,
WA,USA.p.8107–16.doi:10.1109/cvpr42600.2020.00813.
96. Ho J, Saharia C, Chan W, Fleet DJ, Norouzi M, Salimans T. Cascaded diffusion models for high fidelity image
generation.JMachLearnRes.2022;23(47):1–33.
97. Jadhav B, Jain M, Jajoo A, Kadam D, Kadam H, Kakkad T. Imagination made real: stable diffusion for high-
fidelitytext-to-imagetasks.In:20242ndInternationalConferenceonSustainableComputingandSmartSystems
(ICSCSS);2024Jul10–12;Coimbatore,India.p.773–9.doi:10.1109/ICSCSS60660.2024.10625113.
98. Yang Q, Farseev A, Ongpin M, Huang A, Chu-Farseeva YY, You DM, et al. Fusing predictive and large language
models for actionable recommendations in creative marketing. ACM Trans Inf Syst. 2025;43(5):1–31. doi:10.1145/
3725885.
99. Shoumy NJ, Ang LM, Seng KP, Rahaman DM, Zia T. Multimodal big data affective analytics: a comprehensive
surveyusingtext,audio,visualandphysiologicalsignals.JNetwComputAppl.2020;149:102447.doi:10.1016/j.jnca.
2019.102447.
1 0 0 .I s l a mT ,M i r o nA ,N a n d yM ,C h o u d r i eJ ,L i uX ,L iY .T r a n s f o r m i n gd i g i t a lm a r k e t i n gw i t hg e n e r a t i v eA I .
Computers.2024;13(7):168.doi:10.3390/computers13070168.
101. XuH,HeK,PlummerBA,SigalL,SclaroffS,SaenkoK.Multilevellanguageandvisionintegrationfortext-to-clip
retrieval.ProcAAAIConfArtifIntell.2019;33(1):9062–9.doi:10.1609/aaai.v33i01.33019062.
102. Khan I. The quick guide to prompt engineering: generative AI tips and tricks for ChatGPT, Bard, Dall-E, and
Midjourney.Hoboken,NJ,USA:JohnWiley&Sons,Inc.;2024.
103. LiuV,ChiltonLB.Designguidelinesforpromptengineeringtext-to-imagegenerativemodels.In:CHIConference
onHumanFactorsinComputingSystems;2022Apr30–May5;NewOrleans,LA,USA.p.1–23.doi:10.1145/3491102.
3501825.
104. Cillo P, Rubera G. Generative AI in innovation and marketing processes: a roadmap of research opportunities. J
AcadMarkSci.2025;53(3):684–701.doi:10.1007/s11747-024-01044-7.
105. Denga EM, Rakshit S. Digital marketing and the sustainable performance of small and medium enterprises. In:
AdvancingSMEstowarde-commercepoliciesforsustainability.Hershey,PA,USA:IGIGlobal;2023.p.213–34.
106. KumarP,SinghG.Usingsocialmediaanddigitalmarketingtoolsandtechniquesfordevelopingbrandequitywith
connected consumers. In: Research anthology on social media advertising and building consumer relationships.
Hershey,PA,USA:IGIGlobal;2022.p.1703–22.doi:10.4018/978-1-6684-6287-4.ch091.
107. Vishwakarma R, Dhakad R. Online advertising and fraud click in online advertisement: a survey. Int J Comput
Appl.2024;186(1):1–8.doi:10.5120/ijca2024923300.
108. Visser M, Hoving M, van Kempen C, Jansen M. Digital marketing in the research phase. In: Digital Marketing
fundamentals.Oxfordshire,UK:Routledge;2025.p.227–82.doi:10.4324/9781003569107-7.
109. GujarP,PanyamS.GenerativeAIindigitaladvertisingcampaigns.IntJComputTrendsTechnol.2024;72(5):51–5.
doi:10.14445/22312803/ijctt-v72i5p106.
110. Osadchaya E, Marder B, Yule JA, Yau A, Lavertu L, Stylos N, et al. To ChatGPT, or not to ChatGPT: navigating
theparadoxesofgenerativeAIintheadvertisingindustry.BusHoriz.2024;67(5):571–81.doi:10.1016/j.bushor.2024.
05.002.

42 ComputMaterContin. 2026;87(3):11
111. CampbellC,FarrellJR.Morethanmeetstheeye:thefunctionalcomponentsunderlyinginfluencermarketing.Bus
Horiz.2020;63(4):469–79.doi:10.1016/j.bushor.2020.03.003.
112. Leung FF, Gu FF, Palmatier RW. Online influencer marketing. J Acad Mark Sci. 2022;50(2):226–51. doi:10.1007/
s11747-021-00829-4.
113. Cunha CR, Gomes JP, Mendonça V. The role of artificial intelligence to empower and leverage brands. In: AI
innovation in services marketing. Hershey, PA, USA: IGI Global; 2024. p. 27–47. doi:10.4018/979-8-3693-2153-9.
ch002.
114. Stephen AT. The role of digital and social media marketing in consumer behavior. Curr Opin Psychol.
2016;10:17–21.doi:10.1016/j.copsyc.2015.10.016.
1 1 5 .A l d o u sK ,S a l m i n e nJ ,F a r o o qA ,J u n gS G ,J a n s e nB .U s i n gC h a t G P Ti nc o n t e n tm a r k e t i n g :e n h a n c i n gu s e r s ’
social media engagement in cross-platform content creation through generative AI. In: Proceedings of the 35th
ACMConferenceonHypertextandSocialMedia;2024Sep10–13;Poznan,Poland.p.376–83.doi:10.1145/3648188.
3675142.
116. Soni V. Adopting generative AI in digital marketing campaigns: an empirical study of drivers and barriers. Sage
SciRevApplMachLearn.2023;6(8):1–15.
117. MorokhovaV,BatyrbekovaZ,BondarenkoO,UstikT,SaiensusM,TravinV.Digitalizationstrategiesformarketing
communicationstobuildrelationshipmarketing:modernsolutionsinbrandmanagement.WseasTransEnviron
Dev.2023;19:1231–45.doi:10.37394/232015.2023.19.112.
118. Gayam SR. Generative AI for personalized marketing: techniques for dynamic content creation, targeted cam-
paigns,andcustomerengagement.JBioinformArtifIntell.2022;2(1):191–226.
119. HartmannJ,ExnerY,DomdeyS.Thepowerofgenerativemarketing:cangenerativeAIcreatesuperhumanvisual
marketingcontent?IntJResMark.2025;42(1):13–31.doi:10.1016/j.ijresmar.2024.09.002.
120. MayahiS,VidrihM.TheimpactofgenerativeAIonthefutureofvisualcontentmarketing.arXiv:2211.12660.2022.
121. Wahid R, Mero J, Ritala P. Editorial: written by ChatGPT, illustrated by Midjourney: generative AI for content
marketing.AsiaPacJMarkLogist.2023;35(8):1813–22.doi:10.1108/apjml-10-2023-994.
122. Chaffey D, Smith PR. Digital marketing excellence: planning, optimizing and integrating online marketing. 6th
ed.London,UK:Routledge;2022.doi:10.4324/9781003009498.
123. Dhore A, Harkal R, Darokar M. Exploring the effects of digital marketing practices in India: a comprehensive
analysis.JManagSci.2024;14(1):92–6.doi:10.26524/jms.14.12.
124. Nobile TH, Cantoni L. Personalisation (In) effectiveness in email marketing. Digit Bus. 2023;3(2):100058. doi:10.
1016/j.digbus.2023.100058.
125. Wu J, Li KJ, Liu JS. Bayesian inference for assessing effects of email marketing campaigns. J Bus Econ Stat.
2018;36(2):253–66.doi:10.1080/07350015.2016.1141096.
126. Dutta S, Arivazhagan R, Padmini Ema U, Balasundaram R. Revolutionizing electronics e-commerce: harnessing
thepowerofartificialintelligenceinE-marketingstrategies.MigratLetters.2024;21(S6):207–20.
127. DasS.Searchengineoptimizationandmarketing:arecipeforsuccessindigitalmarketing.BocaRaton,FL,USA:
ChapmanandHall/CRC;2021.
128. Nagpal M, Petersen JA. Keyword selection strategies in search engine optimization: how relevant is relevance? J
Retail.2021;97(4):746–63.doi:10.1016/j.jretai.2020.12.002.
129. Amara M, Zaghdoud R, Ben Rhaiem O, Althubiti E. Enhancing image SEO using deep learning algorithms: a
researchapproach.EngTechnolApplSciRes.2024;14(4):15194–200.doi:10.48084/etasr.7473.
130. Chanthati SR. Website visitor analysis & branding quality measurement using artificial intelligence. Am J Educ
Technol.2024;3(3):88–101.doi:10.54536/ajet.v3i3.3212.
131. Saeed Z, Aslam F, Ghafoor A, Umair M, Razzak I. Exploring the impact of SEO-based ranking factors for voice
queriesthroughmachinelearning.ArtifIntellRev.2024;57(6):144.doi:10.1007/s10462-024-10780-9.
132. Tran MT. A systematic analysis of artificial intelligence’s usage in online advertising: how artificial intelligence
affectsdigitalmarketinginitiatives.In:EnhancingandpredictingdigitalconsumerbehaviorwithAI.Hershey,PA,
USA:IGIGlobal;2024.p.17–27.doi:10.4018/979-8-3693-4453-8.ch002.

ComputMaterContin. 2026;87(3):11 43
133. VetrivelS,ArunV,SaravananT,MaheswariR.HarnessingAIfornext-generationservicemarketing.In:Integrating
AI-driven technologies into service marketing. Hershey, PA, USA: IGI Global; 2024. p. 265–98. doi:10.4018/979-
8-3693-7122-0.ch015.
134. Wang S. Generative AI: an in-depth exploration of methods, uses, and challenges. Highlights Sci Eng Technol.
2024;85:196–202.doi:10.54097/czptrz11.
135. Jovic M, Mnasri S. Evaluating AI-generated emails: a comparative efficiency analysis. World J Engl Lang.
2023;14(2):502.doi:10.5430/wjel.v14n2p502.
136. IndrawanD,YormanY,StiadiM,HendayaniN,Al-AminAA.RevolutionizingsocialmediamarketingthroughAI
andautomation:anin-depthanalysisofstrategies,ethics,andfuturetrends.IntJHumSocSciBus.2023;3(1):22–45.
137. WenY,LaporteS.Experientialnarrativesinmarketing:acomparisonofgenerativeAIandhumancontent.JPublic
PolicyMark.2025;44(3):392–410.doi:10.1177/07439156241297973.
138. YuS,CarrollF,BentleyBL.Trustandrisk:psybersecurityintheAIera.In:Psybersecurity.BocaRaton,FL,USA:
CRCPress;2024.p.130–55.
139. Rahman A, Islam M, Moon MJ, Tasnim T, Siddique N, Shahiduzzaman M, et al. A qualitative survey on deep
learningbaseddeepfakevideocreationanddetectionmethod.AustJEngInnovTechnol.2022;4(1):13–26.doi:10.
34104/ajeit.022.013026.
140. RahmanA,SiddiqueN,MoonMJ,TasnimT,IslamM,ShahiduzzamanM,etal.Shortandlowresolutiondeepfake
videodetectionusingCNN.In:2022IEEE10thRegion10HumanitarianTechnologyConference(R10-HTC);2022
Sep16–18;H yderabad,I ndia.p .259–64.do i:10.1109/R10-HTC54060.20 22.99 29719.
141. Rana NP, Pillai R, Sivathanu B, Malik N. Assessing the nexus of Generative AI adoption, ethical considerations
andorganizationalperformance.Technovation.2024;135:103064.doi:10.1016/j.technovation.2024.103064.
142. Wani TA, Ali SW. Innovation diffusion theory. J General Manag Res. 2015;3(2):101–18. doi:10.1002/9781119756
231.ch1.
143. Ritz W, Wolf M, McQuitty S. Digital marketing adoption and success for small businesses: the application of the
do-it-yourself and technology acceptance models. J Res Interact Mark. 2019;13(2):179–203. doi:10.1108/jrim-04-
2018-0062.
144. Rogers EM, Singhal A, Quinlan MM. Diffusion of innovations 1. In: An integrated approach to communication
theoryandresearch.London,UK:Routledge;2019.p.415–34.doi:10.4324/9780203710753-35.
145. Davis FD. Technology acceptance model: TAM. In: Information seeking behavior and technology adoption.
Hershey,PA,USA:IGIGlobal;1989.p.205–19.
146. Al-kfairy M, Mustafa D, Kshetri N, Insiew M, Alfandi O. Ethical challenges and solutions of generative AI: an
interdisciplinaryperspective.Informatics.2024;11(3):58.doi:10.3390/informatics11030058.
147. Nandan Prasad A. Ethical implications and bias mitigation. In: Introduction to data governance for machine
learningsystems.Singapore:Springer;2024.p.307–82.doi:10.1007/979-8-8688-1023-7_5.
148. AveryJJ,AbrilPS,delRiegoA.AttributingAIauthorship:towardsasystemoficonsforlegalandethicaldisclosure.
NwJTechIntellProp.2024;22(1):1–54.
149. Esezoobo SO, Braimoh J. Integrating legal, ethical, and technological strategies to mitigate AI deepfake risks
throughstrategiccommunication.IntJSciResManag.2023;11(8):914–28.doi:10.18535/ijsrm/v11i08.ec02.
150. ShafferG.Globalizationandsocialprotection:theimpactofEUandinternationalrulesintheratchetingupofUS
privacystandards.YaleJIntLaw.2000;25:1–88.
151. Hermann E, Puntoni S. Generative AI in marketing and principles for ethical design and deployment. J Public
PolicyMark.2025;44(3):332–49.doi:10.1177/07439156241309874.
152. Cronin I. Understanding generative AI business applications: a guide to technical principles and real-world
applications.Berkeley,CA,USA:Apress;2024.doi:10.1007/979-8-8688-0282-9.
153. Jin K, Zhong ZZ, Zhao EY. Sustainable digital marketing under big data: an AI random forest model approach.
IEEETransEngManag.2024;71:3566–79.doi:10.1109/TEM.2023.3348991.
154. Vashishth TK, Vikas, Sharma KK, Kumar B, Chaudhary S, Panwar R. Enhancing customer experience through
AI-enabled content personalization in E-commerce marketing. In: Advances in digital marketing in the era of
artificialintelligence.BocaRaton,FL,USA:CRCPress;2024.p.7–32.doi:10.1201/9781003450443-2.

44 ComputMaterContin. 2026;87(3):11
155. Hocutt DL. Composing with generative AI on digital advertising platforms. Comput Compos. 2024;71:102829.
doi:10.1016/j.compcom.2024.102829.
156. Gołąb-AndrzejakE.TheimpactofgenerativeAIandChatGPToncreatingdigitaladvertisingcampaigns.Cybern
Syst.2025;56(8):1130–44.doi:10.1080/01969722.2023.2296253.
157. BaekTH.DigitaladvertisingintheageofgenerativeAI.JCurrIssuesResAdvert.2023;44(3):249–51.doi:10.1080/
10641734.2023.2243496.
158. Martínez-Rolán X, Corbacho-Valencia JM, Piñeiro-Otero T. Use of generative AIs in the digital communica-
tion and marketing sector in Spain. In: Management for digital transformation. Cham, Switzerland: Springer
InternationalPublishing;2023.p.101–21.doi:10.1007/978-3-031-42060-3_5.
159. VeeramachaneniV.Largelanguagemodels:acomprehensivesurveyonarchitectures,applications,andchallenges.
AdvInnovComputProgrammLang.2025;7(1):20–39.
160. Mienye ID, Swart TG, Obaido G. Recurrent neural networks: a comprehensive review of architectures, variants,
andapplications.Information.2024;15(9):517.doi:10.3390/info15090517.
161. Khennouche F, Elmir Y, Himeur Y, Djebari N, Amira A. Revolutionizing generative pre-traineds: insights and
challengesindeployingChatGPTandgenerativechatbotsforFAQs.ExpertSystAppl.2024;246(4):123224.doi:10.
1016/j.eswa.2024.123224.
162. Kushwaha AK, Kar AK. MarkBot—a language model-driven chatbot for interactive marketing in post-modern
world.InfSystFront.2024;26(3):857–74.doi:10.1007/s10796-021-10184-y.
163. Hemachandran K, Choudhury D, Rodriguez RV, Wise JA, Revathi T. Predictive analytics and generative AI for
data-drivenmarketingstrategies.BocaRaton,FL,USA:CRCPress;2024.
164. Wang B, Chen Q, Wang Z. Diffusion-based visual art creation: a survey and new perspectives. arXiv:2408.12128.
2024.
165. Liang J. The application of artificial intelligence-assisted technology in cultural and creative product design. Sci
Rep.2024;14(1):31069.doi:10.1038/s41598-024-82281-2.
166. Sindiramutty SR, Prabagaran KRV, Akbar R, Hussain M, Malik NA. Generative AI for secure user interface (UI)
design.In:ReshapingCyberSecuritywithgenerativeAItechniques.Hershey ,P A,USA:IGIGlobal;2025.p.333–94.
doi:10.4018/979-8-3693-5415-5.ch010.
167. Pagani M, Champion R. Artificial intelligence for business creativity. London, UK: Routledge; 2023. doi:10.4324/
9781003287582.
168. Ahram T, Casarotto L, Costa P. Human interaction and emerging technologies (IHIET 2024): proceedings of the
12thinternationalconferenceonhumaninteractionandemergingtechnologies.Venice,Italy:AHFEOpenAccess;
2024.
1 6 9 .M a d a n c h i a nM .G e n e r a t i v eA If o rc o n s u m e rb e h a v i o rp r e d i c t i o n :t e c h n i q u e sa n da p p l i c a t i o n s .S u s t a i n a b i l i t y .
2024;16(22):9963.doi:10.3390/su16229963.
170. Liu Z. Cultural bias in large language models: a comprehensive analysis and mitigation strategies. J Transcult
Commun.2025;3(2):224–44.doi:10.1515/jtc-2023-0019.
171. Shandilya SK, Datta A, Kartik Y, Nagar A. Navigating the regulatory landscape. In: Digital resilience: navigating
disruptionandsafeguardingdataprivacy.Cham,Switzerland:SpringerNature;2024.p.127–240.doi:10.1007/978-
3-031-53290-0_3.
172. JohariR,KoomenP ,PekelisL,W alshD.PeekingatA/Btests:whyitmatters,andwhattodoaboutit.In:Proceedings
ofthe23rdACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining;2017Aug13–17;
Halifax,NS,Canada.p.1517–25.doi:10.1145/3097983.3097992.
173. RodriguezG,MartaM.UsinggenerativeAItoolstoimprovemarketingcommunication:opportunities,challenges
and best practices. Valencia, Spain: Universitat Politècnica de València; 2024. [cited 2025 Oct 10]. Availble from:
https://riunet.upv.es/entities/publication/1bf3fa8d-a120-4c0c-9a4c-88a23d6439f8.
174. AjubhaiRN.Frompersonalizationtoprediction:theroleofgenerativeAIinshapingconsumerpurchasejourneys.
JMultidiscipStud.2025;2(1):13–23.
175. ShahN,EngineerS,BhagatN,ChauhanH,ShahM.Researchtrendsontheusageofmachinelearningandartificial
intelligenceinadvertising.AugmentHumRes.2020;5(1):19.doi:10.1007/s41133-020-00038-8.

ComputMaterContin. 2026;87(3):11 45
176. Anantrasirichai N, Zhang F, Bull D. Artificial intelligence in creative industries: advances prior to 2025.
arXiv:2501.02725.2025.
177. Ilieva G, Yankova T, Klisarova-Belcheva S. Effects of generative AI in tourism industry. Information.
2024;15(11):671.doi:10.3390/info15110671.
