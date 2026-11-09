---
title: Methodological guidance for predictor variable selection for adolescent smoking outcomes in Global
  Youth Tobacco Survey using R and Python
url: https://doi.org/10.3389/fams.2026.1895038
category: social-media
subcategory: theory
date: 2026-08
venue: Frontiers in Applied Mathematics and Statistics
authors:
- Wingston F Ng'ambi
- Cosmas Zyambo
- Lawrence N. Kazembe
source: openalex-oa
pdf_url: https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1895038/pdf
pages: 19
chars: 84696
fetched_at: '2026-11-08T18:38:40+00:00'
kb_version: 1
---

# Methodological guidance for predictor variable selection for adolescent smoking outcomes in Global Youth Tobacco Survey using R and Python

TYPE Methods
PUBLISHED 17 August 2026
DOI 10.3389/fams.2026.1895038
OPEN ACCESS
EDITED BY
Ashis SenGupta,
Augusta University, United States
REVIEWED BY
Shiva Shankar Bugude,
Qassim University, Saudi Arabia
Abdulkadir Keskin,
Istanbul Medeniyet University, Türkiye
*CORRESPONDENCE
Wingston Felix Ng’ambi
wingston.ngambi@gmail.com
RECEIVED 29 May 2026
REVISED 08 July 2026
ACCEPTED 15 July 2026
PUBLISHED 17 August 2026
CITATION
Ng’ambi WF, Zyambo C and Kazembe L
(2026) Methodological guidance for
predictor variable selection for
adolescent smoking outcomes in Global
Youth Tobacco Survey using R and
Python.
Front. Appl. Math. Stat. 12:1895038.
doi: 10.3389/fams.2026.1895038
COPYRIGHT
© 2026 Ng’ambi, Zyambo and Kazembe.
This is an open-access article distributed
under the terms of theCreative
Commons Attribution License (CC BY).
The use, distribution or reproduction in
other forums is permitted, provided the
original author(s) and the copyright
owner(s) are credited and that the
original publication in this journal is
cited, in accordance with accepted
academic practice. No use, distribution
or reproduction is permitted which does
not comply with these terms.
Methodological guidance for
predictor variable selection for
adolescent smoking outcomes in
Global Youth Tobacco Survey
using R and Python
Wingston Felix Ng’ambi1,2,3*, Cosmas Zyambo2,3 and
Lawrence Kazembe4,5
1Health Economics Policy Unit, Department of Health Systems and Policy, Kamuzu University of Health
Sciences, Lilongwe, Malawi,2Department of Community and Family Medicine, University of Zambia,
Lusaka, Zambia,3Global Institute for Tobacco, Alcohol and Substance Use Research, Lusaka, Zambia,
4Department of Computing, Mathematical and Statistical Sciences, University of Namibia, Windhoek,
Namibia, 5Mathematical Sciences, University of Malawi, Zomba, Malawi
Background: The Global Youth Tobacco Survey is one of the most important
sources of data on adolescent tobacco use worldwide. However, studies using
these data often apply inconsistent statistical methods, particularly in how they
handle complex survey designs and select predictors for analysis. Many analyses
use simpliﬁed approaches or proprietary software, making results difficult to
reproduce or compare across countries and survey years. We developed a clear,
open-sourceworkﬂowtoguideresearchersinselectingpredictorsandmodeling
adolescentsmokingoutcomesinawaythatistransparent,theory-informed,and
reproducible in both R and Python.
Results: The framework is designed to incorporate the full two-stage
survey design, including weights, stratiﬁcation, and clustering, with the R
implementation serving as the reference platform for design-based inference.
Key demographic factors (age, sex, grade, and region or country) are retained
in all models, while other modiﬁable predictors are selected using a constrained
stepwise procedure guided by model ﬁt. We demonstrate the approach using
Zambia 2021 and pooled data from Ghana, Mauritius, Seychelles, and Togo,
2015–2019. The pooled dataset included 15,914 adolescents, of whom 13,360
had complete information for the complete-case modeling analysis. When
identical model speciﬁcations were applied, the R and Python implementations
selectedthesameﬁnalmodelandproducednearlyidenticaladjustedoddsratios,
with differences below 0.01. However, standard errors and conﬁdence intervals
differed slightly because Python’s implementation relied on survey weights only
anddidnotfullyaccountforclusteringandstratiﬁcation.Inthecurrentcigarette-
smoking model, the ﬁnal model showed adequate event support, with 1,479
current smokers and 33 estimated parameters, giving an events-per-variable
value of 44.82. Factors independently associated with current cigarette smoking
included intention to use tobacco in the next 5 years, ever trying cigarette
smoking, ownership of an item with a tobacco logo, seeing teachers smoking
at school, and being taught about the dangers of tobacco use.
Conclusions: This study provides a practical and generalizable framework
for analysing adolescent smoking using complex survey data. By combining
theoretical grounding, transparent variable selection, and open-source tools,
the workﬂow improves reproducibility, cross-country comparability, and policy
Frontiersin AppliedMathematicsandStatistics 01 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
relevance. It can be readily adapted to other large-scale health surveys to
strengthen evidence for tobacco control and prevention efforts.
KEYWORDS
adolescent smoking behavior, complex survey design, GYTS, multi-country
harmonization, predictor variablejustiﬁcation, Python, R,social cognitive theory
Background
Adolescent smoking remains a major public health concern
worldwide, with particularly serious implications in low- and
middle-incomecountrieswherepreventionandcessationresources
are often limited [1, 2]. Most adult smokers begin using tobacco
during adolescence, making this life stage critical for intervention.
The Global Youth Tobacco Survey (GYTS), led by the World
Health Organization and the US Centers for Disease Control
and Prevention, was designed to address this need by providing
standardized, comparable data on youth tobacco use across more
than 140 countries [3–5]. Globally, analyses of GYTS data have
documented wide variation in smoking prevalence and strong
associations with peer smoking, exposure to tobacco marketing,
and awareness of tobacco products [5–7]. However, despite the
richness of these data, published studies often apply simpliﬁed
analytical approaches, most commonly descriptive statistics or
logistic regression models that use survey weights only, while
ignoring clustering and stratiﬁcation. This practice can lead to
biased standard errors, overly narrow conﬁdence intervals, and
resultsthatarediﬃculttocompareacrosscountriesandstudies[ 8].
Methodologically, GYTS data present several recurring
challengesthatarenotalwayshandledconsistentlyintheliterature.
The survey uses a two-stage clustered sampling design, requiring
analysts to account for weights, strata, and primary sampling units
to obtain valid population level estimates [7]. In multi country
analyses, additional complexity arises from diﬀerences in school
systems, questionnaire wording, and variable coding, all of which
require careful harmonization [9]. At the same time, the survey
includes a large number of potential predictors, creating a tension
betweenbuildingparsimoniousmodelsandretainingvariablesthat
are theoretically important [10]. Many studies rely on automated
variableselectionbasedpurelyonstatisticalsigniﬁcance,whichcan
result in the exclusion of key demographic variables such as age
andsex,increasingtheriskofresidualconfounding[ 11].Although
Abbreviations: AIC, Akaike Information Criterion; aOR, Adjusted Odds Ratio;
CDC, Centers for Disease Control and Prevention; CI, Conﬁdence Interval;
CVD, Cardiovascular Disease; FCTC, Framework Convention on Tobacco
Control;GATS,GlobalAdultTobaccoSurvey;GLM,GeneralizedLinearModel;
GSHS, Global School-based Student Health Survey; GYTS, Global Youth
Tobacco Survey; ICC, Intra-class Correlation Coefficient; LMICs, Low- and
Middle-Income Countries; MPOWER, Monitor, Protect, Offer, Warn, Enforce,
Raise (WHO tobacco control framework); NCD, Noncommunicable Disease;
OR, Odds Ratio; PSU, Primary Sampling Unit; R, R Statistical Software; SADC,
Southern African Development Community; SES, Socioeconomic Status;
SPSS, Statistical Package for the Social Sciences; SAS, Statistical Analysis
System; STEPS, STEPwise Approach to NCD Risk Factor Surveillance; UK,
United Kingdom; WHO, World Health Organization.
SAS and SPSS dominate the published GYTS literature [12], open
source tools such as R and Python oﬀer greater transparency
and reproducibility, yet practical guidance on how to use them
correctlyforcomplexsurveyanalysisremainsfragmented[ 7].
This study responds to these gaps by presenting a clear
and reproducible analytical framework for explanatory modeling
of adolescent smoking behavior using GYTS data in both R
and Python [ 12, 13]. The objectives are ﬁvefold. First, we
standardize data preprocessing and harmonization procedures for
single country and pooled multi country analyses. Second, we
demonstrate comparable workﬂows for survey-weighted logistic
regression in R and Python, while recognizing that only the
R implementation fully accounts for weights, stratiﬁcation, and
clustering. Third, we apply constrained stepwise variable selection
methods that protect a priori demographic variables regardless of
marginal statistical signiﬁcance. Fourth, we assess cross platform
reproducibility by comparing results obtained from identical
model speciﬁcations in R and Python. Finally, we provide explicit
justiﬁcation for predictor selection, linking variables to established
behavioral theory and evidence from systematic reviews, rather
thanrelyingsolelyondatadrivenselection.
The initial predictor variable selection in this framework is
guided by Social Cognitive Theory that explains health behaviors
as the result of dynamic interactions between personal, behavioral,
and environmental factors in adolescence smoking [14, 15]. In the
context of adolescent smoking, personal factors include age, sex,
and perceptions about tobacco, behavioral factors capture prior
experimentation and intentions, and environmental factors reﬂect
peer inﬂuence, parental smoking, media exposure, and school-
basededucation.SocialCognitiveTheoryisparticularlywellsuited
toadolescenttobaccousebecauseadolescenceisaperiodofintense
social learning, identity formation, and sensitivity to norms [16,
17]. Young people are strongly inﬂuenced by what they observe
among peers and role models, while repeated exposure to tobacco
marketingandmediashapesawarenessandperceivedacceptability
of smoking. By organizing predictors within this framework, the
analysis moves beyond purely statistical associations [ 18] and
provides a coherent explanation of how social environments,
individual characteristics, and observed behaviors jointly shape
smokingriskamongadolescents[ 19,20].
Methods
Data sources and study design
This studyuseddatafromtheGlobalYouthTobaccoSurvey,a
school-based survey designed to produce nationally representative
Frontiersin AppliedMathematicsandStatistics 02 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
FIGURE 1
Dataset completeness at a glance for analysis of the 2021 Global
Youth Tobacco Survey dataset for Zambia. Demo refers to
demographic; missing supplement refers to missing outcomes and
non-demographic data.
estimates of tobacco related behaviors among adolescents [21–27].
GYTS applies a two-stage cluster sampling design, with schools
selected as primary sampling units and classrooms randomly
selected within schools [21–27]. All analyses accounted for survey
weights, stratiﬁcation, and clustering to ensure valid population
level inference [7]. In this study, we considered two GYTS data
analysisscenariosasoutlinedbelow:
Study 1: single country analysis, Zambia 2021
The ﬁrst analysis used the Zambia GYTS 2021 dataset,
which initially included 6,499 school-going adolescents [ 28].
After excluding participants with missing outcome or predictor
information required for the complete-case model, the ﬁnal
analytical sample comprised 2,959 adolescents aged 11 to 17 years
(see Figure1). The 2021 GYTS for Zambia was amongst the
ﬁrst surveys to collect data on shisha and electronic cigarettes
in the Southern Africa Development Community (SADC) region.
The survey instrument consisted of 56 standardized questions
covering cigarette smoking, use of other tobacco products,
exposure to second-hand smoke, access to tobacco, media and
marketing exposure, cessation attempts, and tobacco related
knowledge. Zambia used the standard GYTS core questionnaire
with limited country speciﬁc adaptations, allowing direct use
of core variables for most constructs. This analysis was used
to demonstrate the full analytical workﬂow in a context
where survey design variables and questionnaire structure were
fullyaligned.
Study 2: multi country analysis, 2015 to 2019
The second analysis pooled GYTS data from four Sub Saharan
Africancountriescollectedbetween2015and2019.Theseincluded
Ghanain2017with5,430participants[ 29],Mauritiusin2016with
4,123 participants [30], Seychelles in 2015 with 2,453 participants
[31], and Togo in 2019 with 3,908 participants [32]. The pooled
sample comprised 15,914 adolescents aged 11 to 17 years. These
countries were selected to reﬂect diversity in educational systems
and tobacco control contexts while maintaining suﬃcient overlap
in standardized GYTS core variables. Pooling the data allowed
assessmentofcross-countryconsistencyinpredictorsofadolescent
smokingandenabledrobustcrossplatformvalidation.Missingdata
wereassessedbeforemodeldevelopmentandweregenerallylowat
the individual variable level. Across the pooled dataset of 15,914
adolescents, 2,554 participants (16.1%) had at least one missing
value among variables considered for analysis, with country-
speciﬁc proportions ranging from 11.5% in Togo to 21.7% in
Seychelles.Consequently,13,360participants(83.9%)hadcomplete
information and were retained in the complete-case analytical
dataset(see Figure2).
Predictor variable selection framework
The primary outcome was current cigarette smoking, deﬁned
using the standard GYTS item asking: “During the past 30 days,
on how many days did you smoke cigarettes?” This corresponds to
GYTS core question C7, or the country-speciﬁc equivalent where
local questionnaire numbering diﬀered. Responses indicating
smoking on 0 days were coded as non-current smoking (0), while
responses indicating smoking on 1 or more days in the past
30 days were coded as current smoking (1). Participants with
missing, refused, or non-classiﬁable responses to this item were
excluded from the analytical model requiring the outcome. For
pooled analyses, country-speciﬁc variable names and response
categories were harmonized to this common binary deﬁnition
before model ﬁtting. The framework governing the predictor
variable selection is presented in Figure3. Predictor selection
followed a structured framework grounded in epidemiology and
behavioral science [33]. Four guiding principles informed this
process. First, theoretical coherence was ensured by mapping all
predictors to the domains of Social Cognitive Theory. Second,
empirical support was required, with variables drawn from
established GYTS methodology and systematic review evidence
[26]. Third, modiﬁability was considered to include both risk and
protective factors relevant for intervention. Fourth, cross cultural
validity was prioritized by focusing on standardized GYTS core
questionstoenablemeaningfulmulticountrycomparisons.
Demographic core
A core set of demographic variables was deﬁned a priori and
retained in all models regardless of statistical signiﬁcance [34].
Theseincludedage,sex,gradeoreducationallevel,andgeographic
regionorcountry.Thesevariablesarewellestablishedconfounders
Frontiersin AppliedMathematicsandStatistics 03 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
FIGURE 2
Dataset completeness at a glance for multi-country analyses of Global Youth Tobacco Survey outcomes. Rows w/ gaps refer to rows with missing
data.
in adolescent tobacco research and are explicitly recommended
for adjustment in GYTS analyses. Their deﬁnitions, theoretical
justiﬁcation, empirical support, and expected associations are
summarized in Table1. Excluding these variables could bias
estimates of modiﬁable risk factors, particularly when automated
variable selection procedures are used. Age was modeled to allow
non-linear eﬀects, reﬂecting evidence that susceptibility peaks in
earlytomid-adolescence.
Individual level predictors
Individual level predictors captured intrapersonal
characteristics related to susceptibility and behavioral intention
[35, 36]. These variables correspond to the personal factors’
domain of Social Cognitive Theory and are described inTable2.
They included prior experimentation with cigarettes, smokeless
tobacco, and shisha, intention to smoke in the next 12 months,
and a proxy measure of socioeconomic status. Prior tobacco use
reﬂectsreducedself-eﬃcacytoresistandincreasedfamiliaritywith
tobacco products, while intention represents the most proximal
predictoroffuturesmokingbehavior.
Social factors
Social environment predictors represented interpersonal
inﬂuences from peers, family, school, and the wider community
[37–39]. These variables, summarized inTable3, included having
close friends who smoke, parental or guardian smoking, exposure
to smoking at school, and exposure to smoking in public places.
Social Cognitive Theory highlights observational learning as a key
mechanism through which adolescents adopt behaviors observed
in signiﬁcant others. Consistent with the literature, peer smoking
emerged as the strongest and most consistent social predictor of
adolescentsmoking[ 38].
Media and marketing exposure
Media and marketing variables captured environmental
inﬂuences shaping awareness, social norms, and outcome
expectations [ 40–42]. As shown in Table4, these included
awareness of tobacco products, exposure to tobacco advertising
on television and radio, ownership of tobacco branded items,
and exposure to anti-tobacco media messages. Awareness was
treatedasaprerequisiteforexperimentation,whileadvertisingand
brandingreﬂectindustrydrivennormalizationoftobaccouse[ 43].
Anti-tobacco media exposure was included as a protective factor
thatmaycounterbalanceprotobaccoinﬂuences.
Policy and school based protection
Structural and policy related variables reﬂected protective
environments aligned with the WHO MPOWER framework [44–
46]. These predictors, described inTable5, included being taught
about the dangers of smoking in school and the presence of smoke
free policies in enclosed and public places. From a behavioral
perspective, these factors represent environmental restructuring
that reduces exposure, denormalizes smoking, and supports non-
smokingnorms.Thesevariablesaredirectlyrelevantforpolicyand
preventionplanning[ 47].
Variables excluded and rationale
Several variables were considered but excluded from the
primary analysis due to limited comparability or methodological
concerns. These exclusions and their rationale are summarized
in Table6. Mental health [48] indicators and sensation seeking
measureswereexcludedbecausetheyarenotconsistentlycaptured
across GYTS waves. Internet and social media exposure variables
were excluded due to inconsistent availability in earlier surveys.
Frontiersin AppliedMathematicsandStatistics 04 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
FIGURE 3
Framework for variable selection when analysing Global Youth Tobacco Survey data.
Frontiersin AppliedMathematicsandStatistics 05 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 1 Apriori variables: deﬁnition,justiﬁcation,and expected associations.
Variable GYTS question Theoretical justiﬁcation Empirical evidence Expected
direction
Age CR1/CR52 Criticaldevelopmentalperiodfor
tobaccoinitiation;non-linear
relationshipwithsmokingbehavior
duetocuriosityandsusceptibility
peaks.
Strongestempiricalsupport:younger
adolescents(13–14years)athigherrisk
thanolder(17–18years);age11–17
capturespeakexperimentationperiod[ 66]
Non-linear(peakat
13–15years)
Sex/Gender CR2/CR53 Consistentgenderdiﬀerentialin
tobaccouse;biologicalandsocial
factorsinﬂuenceproductappealand
access.
10/50studiesidentiﬁedmalegenderas
signiﬁcantriskfactor;however,some
contextsshowhigherfemalecuriosityat
youngerages[ 66]
Context-dependent
Grade/Educationallevel ZAR3/GHR3/MUR3/TGR3 Proxyforageandeducational
exposure;capturesschool-based
preventionprogramexposureand
peernetworkexpansion.
Schoolenvironmentsidentiﬁedascritical
riskfactor;gradelevelassociatedwithpeer
networkexpansionandriskbehavior
experimentation
Positive(+)
Geographic
region/Country
Stratum/Country Accountsforcontextualdiﬀerencesin
tobaccocontrolpolicies,cultural
norms,economicdevelopment,and
productavailability.
Regionalvariationinenforcementof
tobaccolawsandaccesstoproducts[ 67];
multi-countryanalysesrequirecountry
adjustmentforcomparability[ 52]
Context-speciﬁc
Product speciﬁc variables such as brand preferences were excluded
toavoidselectionbias,astheyapplyonlytocurrentusers[ 49].
Data harmonization procedures
Single country variable mapping
For the Zambia dataset, standardized GYTS core variables
were mapped to country speciﬁc adaptations using a systematic
extraction protocol [9]. Where country speciﬁc variables were
missing, fallback rules were applied to preserve sample size while
maintaining consistency. Age categories were harmonized into
singleyearvaluestoallowﬂexiblemodelingandcomparabilitywith
pooledanalyses.
Multi country educational system harmonization
Educational systems varied substantially across the four
countries included in the pooled analysis. To enable valid cross-
country comparison [50, 51], grade levels were harmonized to
a uniﬁed UK based year system (seeSupplementarymaterialS1 ).
This approach aligns educational stage with age and is widely used
in global health research. The harmonization protocol for each
country is presented inTable7, along with justiﬁcation based on
ageofentryandprogressionpatterns.
Why harmonize to UK system?
• International comparability: UK educational stages widely
understoodinglobalhealthresearch.
• Age-grade alignment: UK Years roughly correspond to age
(Year7 =11–12years,Year11 =15–16years).
• WHO recommendation: GYTS targeting ages 13–15
correspondstoUKYears8–10.
• Previous studies: Published multi-country GYTS analyses
usedsimilarharmonization[ 52].
Missing data management
Missing data were assessed before model development for
the outcome, a priori demographic covariates, and all candidate
predictors. Item-level missingness was summarized separately by
country and for the pooled dataset. For ease of interpretation,
missingness is presented graphically inSupplementaryFigureS1
rather than as a large table. The ﬁgure reports the percentage
missingforeachoutcomeandpredictorvariableacrosstheZambia
2021 dataset, each pooled-country dataset, and the combined
pooled dataset. Complete-case analysis was used for the primary
models because the purpose of the study was to demonstrate a
transparent, reproducible modeling workﬂow using harmonized
variables. However, because complete-case analysis can reduce
precision and may introduce selection bias when missingness is
associated with exposure or outcome status, the implications of
missingdataareconsideredinthelimitations.
Software environment
Analyses were conductedusing Rversion 4.2+withthe survey
package version 4.5 and Python version 3.10+ with statsmodels
version 0.13.1+. All scripts were run using a ﬁxed random seed of
123. The full computational environment is documented using an
Frontiersin AppliedMathematicsandStatistics 06 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 2 Individual-levelpredictors withassociatedtheoreticaland empiricaljustiﬁcation.
Variable GYTS
question
Construct Theoretical justiﬁcation Empirical
evidence
Expected
direction
Evertriedcigarette
smoking
CR5/CR8 Priortobacco
experimentation
Sharedliabilitytheoryandgatewayhypothesis;
adolescentswhoexperimentwithonetobacco
productmorelikelytotryothersdueto
reducedperceivedharmandestablished
procurementmethods.
Strongestpredictorin
systematicreviews;OR
typically2–5[ 66]
Positive(+)
Evertriedsmokeless
tobacco
CR9/CR13 Alternativetobacco
productuse
Indicatesbroadertobaccoproductacceptance
andrisk-takingpropensity;partof“any
tobaccouse”patternsuggestinggeneral
susceptibilitytonicotineproducts.
Moderateassociation;OR
1.5–3[66]
Positive(+)
Everused
shisha/waterpipe
SR1/CR8 Alternativetobacco
productuse
Shishausesharessocialcontextwithcigarettes;
bothperceivedassociallyacceptable;similar
demographicappeal.
Strongassociationin
severalcontexts;OR2–4
[68]
Positive(+)
Intentiontosmokein
next12months
CR40/ZAR
equivalent
Behavioral
intention
TheoryofPlannedBehaviorconstruct;
intentionisstrongestproximalpredictorof
behavior;reﬂectspositiveoutcome
expectationsandlowself-eﬃcacytoresist.
Consistentstrong
predictor;OR3–6[ 66,69]
Positive(+)
SocioeconomicStatus
(SES)
ZAR4/Income
questions
Disposable
income/family
wealth
Greaterﬁnancialresourcesenableproduct
purchase;cigarettesarerelativelyaﬀordablebut
stillrepresentdiscretionaryspending;mayalso
reﬂectparentaleducationandhealthliteracy.
Mixed:positivelinearor
U-shapedrelationship
[66,70]
Positive(+)or
U-shaped
TABLE 3 Socialenvironment predictorswithassociated theoreticaland empiricaljustiﬁcation.
Variable GYTS
source
Construct Theoretical justiﬁcation Empirical evidence Expected
direction
Closefriendssmoke CR39/ZAR55 Peerdescriptive
norms
Sociallearningtheory—behaviorsmodeledand
reinforcedbypeers;normativeperceptionthat
“everyoneisdoingit”;directsocialpressureand
sharedsocialcontexts
Strongestriskfactor
identiﬁedinsystematic
review(13/50studies);OR
3–8[66,71]
Positive(+)
Parent/guardian
smokes
OR15/CR12 Parentalsmoking
status
Familysmokingnormalizestobaccouseand
indicatesavailability;observationallearningfrom
primaryrolemodels;reducedparental
monitoringandanti-tobaccosocialization.
Secondstrongestriskfactor;
OR2–4[ 66,72]
Positive(+)
Exposedtosmokingat
school
CR22 School
environmental
exposure
Indicatesschool-levelnormativeclimate;teachers
smokingmodelsbehaviorforstudents;suggests
weakenforcementofsmoke-freepolicies.
Moderate-strong
association;OR2–3[ 73]
Positive(+)
Exposedtosmokingin
publicplaces
CR21 Community
environmental
exposure
Environmentalcueingtheory—visualreminders
triggerbehavior;indicatescommunitysmoking
normsandweakpolicyenforcement;increases
perceivedacceptability
Moderateassociation;OR
1.5–2.5[74]
Positive(+)
renv.lock ﬁle for R and an environment.yml ﬁle for Python. These
ﬁles, together with the analytical scripts, variable harmonization
ﬁles, model output tables, renv.lock, and environment.yml,
are archived in a public version-controlled GitHub repository
and in a DOI-linked Zenodo archive. The GitHub repository
is available at https://github.com/andreasngambi-star/GYTS_
analysis_R_Python.git, and the persistent Zenodo DOI is
10.5281/zenodo.21254547. Exact package versions and installation
instructionsareprovidedinthe SupplementarymaterialS4 .
Results
Analytical sample derivation
For Zambia 2021, 6,499 adolescents participated in the survey.
Of these, 225 participants were excluded because the current
smoking outcome could not be classiﬁed, and 3,315 were excluded
because they had missing information for one or more predictors
included in the complete-case modeling framework. The ﬁnal
Frontiersin AppliedMathematicsandStatistics 07 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 4 Mediaand marketing predictorswith theoreticaland empiricaljustiﬁcation.
Variable GYTS
source
Construct Theoretical justiﬁcation Empirical
evidence
Expected
direction
Awarenessoftobacco
products
Multipleitems Productawareness Gatewaytouse—awarenessprecedes
experimentation;productrecognitionindicates
marketingreachandculturalpenetration;
necessarybutnotsuﬃcientconditionforuse.
Strongestmarketing
predictor;OR4–6[ 66,75]
Positive(+)
Sawtobaccoadvertson
TV
CR34 Mediaadvertising
exposure
Advertisingincreasesproductappealand
normalizesuse;createspositiveoutcome
expectations;associatesproductswithdesirable
lifestylesandsocialstatus.
Consistentassociation;
OR1.5–3[ 66,76]
Positive(+)
Heardtobaccoadverts
onradio
CR35 Mediaadvertising
exposure
Multi-channelexposurereinforcesmessages;
radioprevalentinlow-resourcesettings;reaches
populationswithlimitedTV/internetaccess.
Moderateassociation;OR
1.5–2.5[77]
Positive(+)
Ownedtobaccologo
product
CR37/ZAR53 Tobaccobranding
exposure
Brandloyaltyandidentiﬁcationwithtobacco
culture;indicatesindustrytargetingofyouth;
walkingadvertisementeﬀect.
Moderate-strong
association;OR2–4[ 78]
Positive(+)
Anti-tobaccomedia
messages
CR30/CR31/
ZMR66
Counter-marketing
exposure
Protectivefactor;increasesriskperceptionand
self-eﬃcacytoresist;counteractspro-tobacco
norms;reinforcesnon-useassociallydesirable
Protective;OR0.4–0.7
[66,79]
Negative(-)
TABLE 5 Policyand educationpredictorswiththeoreticaland empirical justiﬁcation.
Variable GYTS
source
Construct Theoretical justiﬁcation Empirical
evidence
Expected
direction
Taughtaboutdangers
ofsmoking
CR33/CR48 School-basedhealth
education
Protectivefactor;increasesknowledgeandrisk
perception;buildsself-eﬃcacytoresist;
MPOWER“Warn”component;schoolas
primarypreventionsetting.
Protective;OR0.5–0.8
[66,80]
Negative(-)
Banonsmokingin
enclosedspaces
CR24 Smoke-freepolicies Environmentalprotection;reducesexposureand
denormalizessmoking;changessocialnorms;
MPOWER“Protect”component
Protective;OR0.6–0.9
[81]
Negative(-)
Banonsmokingin
publicplaces
CR25 Smoke-freepolicies Community-levelpolicyprotection;associated
withreducedyouthsmoking;reducesvisibility
andsocialacceptability.
Protective;OR0.5–0.8
[81]
Negative(-)
analytical sample for the Zambia model therefore comprised 2,959
adolescents (seeFigure1). For the pooled multi-country analysis,
the initial dataset included 15,914 adolescents from Ghana 2017,
Mauritius 2016, Seychelles 2015, and Togo 2019. A total of 2,554
participants had missing information for at least one outcome or
predictor variable required for the complete-case model. The ﬁnal
pooled analytical sample therefore comprised 13,360 adolescents.
Thefullparticipantﬂowisshownin Figure2.
Analytical framework implementation
To demonstrate the transferability of the proposed workﬂow,
tworelatedbutdistinctmodelingexampleswereused.TheZambia
2021 dataset was used to demonstrate the single-country workﬂow
for current cigarette smoking, while the pooled Ghana, Mauritius,
Seychelles, and Togo dataset was used to demonstrate the same
frameworkforcurrente-cigaretteuse.
Survey design speciﬁcation
All analyses explicitly accounted for the full complex survey
design, including stratiﬁcation, clustering at the school level,
and sampling weights. Applying weights alone was considered
insuﬃcient, as ignoring clustering leads to underestimated
standard errors and overly narrow conﬁdence intervals. Design
based variance estimation using Taylor series linearization was
therefore used to obtain valid standard errors and conﬁdence
intervals. This approach accounts for the design eﬀect arising
Frontiersin AppliedMathematicsandStatistics 08 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 6 Excludedvariables and rationale.
Excluded variable Reason for exclusion Alternative approach
Mentalhealthindicators
(depression,anxiety)
NotconsistentlymeasuredacrossGYTSwaves;limited
comparabilityformulti-countryanalysis;specializedscales
required.
Proxyviaschoolperformance(graderetention)oranalyzein
country-speciﬁcstudieswithavailabledata.
Sensationseeking/impulsivity NotmeasuredinstandardGYTS;requiresvalidated
psychometricscales(e.g.,ZuckermanSensationSeeking
Scale)
Proxyviamultipletobaccoproductuse(poly-tobaccouse)as
behavioralindicatorofrisk-taking.
Flavorpreferences Speciﬁctotobaccoproductusers;createsselectionbiasif
includedingeneralpopulationmodels;notapplicableto
non-users.
Includeas post-hocanalysisamongcurrentusersonly;analyzeas
outcomeratherthanpredictor.
Internet/socialmediause Emergingvariable;notavailableinolderGYTSwaves
(2015–2017);inconsistentmeasurementacrosscountries.
Traditionalmediavariables(TV,radio)asproxyformediaexposure;
includeinanalysesofrecentwavesonly.
TABLE 7 Educationalsystem harmonizationprotocol.
Country Original system UK equivalent Justiﬁcation
Ghana(2017) JHS1–3(JuniorHighSchool) Years8–10 JHScorrespondstolowersecondary(ages12–15);JHS1entryatage12
Mauritius(2016) Secondaryforms1–3 Years9–11 Form1entryatage13; +8oﬀsetalignswithUKsystem
Seychelles(2015) S1–S4(Secondarylevels) Years8–12 S1entryatage11–12;broaderagerangecaptured
Togo(2019) French6ème-3ème Years7–10 Frenchcolonialsystem;6èmecorrespondstoYear7(age11)
from school-based clustering, which is rarely negligible in
adolescentsurveys.
Why weights alone are insufficient
The majority of published GYTS analyses either apply only
sampling weights or ignore weighting entirely [7]. Because GYTS
uses stratiﬁed two-stage cluster sampling, valid inference requires
accounting for both weights and design structure (strata and
clusters)[8].Usingweightswithoutdesignleadstounderestimated
standard errors and artiﬁcially narrow conﬁdence intervals,
inﬂatingTypeIerror.
The design eﬀect quantiﬁes variance inﬂation from clustering:
it increases as average cluster size and intra-class correlation
rise. Ignoring clustering implicitly assumes zero intra-class
correlation, which is rarely true in school-based surveys [53].
We therefore specify the full complex survey design and use
design-based variance estimation (Taylor series linearization) to
obtain correct standard errors and conﬁdence intervals (see
SupplementarymaterialS2a ).
Weighted baseline characteristics
Baseline characteristics of the analytical samples were
summarized using survey weights. For each categorical variable,
we report unweighted numbers, unweighted percentages, and
weighted percentages. These descriptive analyses were conducted
separately for the Zambia 2021 sample (Table8) and the pooled
multi-country sample (Table9) to describe the distribution of
participantsretainedintheanalyticaldatasetsafterexclusions.
Statistical analysis
Constrained stepwise logistic regression
Survey weighted logistic regression was used to model current
smoking behavior. A constrained stepwise variable selection
approach was applied to balance parsimony with theoretical
integrity. A priori demographic variables were protected from
removal throughout the selection process [10, 18], while candidate
predictors from individual, social, media, and policy domains
were evaluated based on improvements in model ﬁt using the
Akaike Information Criterion. This approach avoids excluding key
confounders while still allowing data driven reﬁnement of the
ﬁnal model. The objective of this variable selection process was
not automated discovery, but disciplined reduction under theory-
informed constraints. Candidate predictors were pre-speciﬁed
based on Social Cognitive Theory and existing empirical evidence,
andselectionprocedureswereappliedsolelytoreduceredundancy
andoverﬁttingwhilepreservingconceptualcoherence.
Alternative variable selection methods, including Least
Absolute Shrinkage and Selection Operator (LASSO) and Elastic
Net regression, were considered during framework development.
These approaches are valuable for high-dimensional prediction
problems and situations involving large numbers of correlated
predictors. However, the primary objective of this study was
explanatory modeling rather than prediction. Because GYTS
Frontiersin AppliedMathematicsandStatistics 09 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 8 Descriptivecharacteristicsof adolescents in the fullZambia 2021GYTS sample, by region,n =6,499.
Characteristic Category Lusaka
n = 2,079
Rest of Zambia
n = 2,472
Tobacco Regions
n = 1,948
Overall
n = 6,499
Age, years 11 82(4.0%) 103(4.2%) 80(4.1%) 265(4.1%)
12 140(6.8%) 178(7.2%) 139(7.2%) 457(7.1%)
13 343(17%) 418(17%) 315(16%) 1,076(17%)
14 514(25%) 572(23%) 503(26%) 1,589(25%)
15 431(21%) 527(21%) 405(21%) 1,363(21%)
16 342(17%) 408(17%) 277(14%) 1,027(16%)
17 211(10%) 253(10%) 214(11%) 678(11%)
Sex Female 1,151(56%) 1,385(57%) 1,145(60%) 3,681(57%)
Male 902(44%) 1,045(43%) 778(40%) 2,725(43%)
Grade Grade7 688(34%) 866(36%) 717(37%) 2,271(35%)
Grade8 651(32%) 780(32%) 620(32%) 2,051(32%)
Grade9 708(35%) 789(32%) 584(30%) 2,081(33%)
Evertriedcigarettesmoking Yes 331(20%) 423(22%) 329(22%) 1,083(21%)
Parent/guardiansmokesinhome Yes 349(17%) 374(15%) 306(16%) 1,029(16%)
Intentiontousetobaccoinnext5years Yes 268(13%) 323(13%) 274(14%) 865(13%)
Exposuretoanti-tobaccomediamessages Yes 1,262(61%) 1,550(63%) 1,210(63%) 4,022(62%)
Taughtaboutdangersoftobaccouse Yes 975(48%) 1,148(47%) 881(46%) 3,004(47%)
Sawteacherssmokingatschool Yes 293(14%) 313(13%) 281(14%) 887(14%)
Friendssmoketobacco Yes 520(25%) 616(25%) 473(25%) 1,609(25%)
Valuesaren(%)forcategoricalvariables.Percentagesarecolumnpercentages.
analyses are intended to generate interpretable estimates for policy
and public health decision-making, we prioritized a theory-driven
framework in which key demographic and contextual variables
were retained regardless of statistical signiﬁcance. Furthermore,
implementation of design-based penalized regression remains
limited in complex survey settings. Consequently, a constrained
stepwise approach based on Akaike Information Criterion
was selected to balance model parsimony, interpretability, and
compatibilitywithsurvey-weightedregression.
Toassessthepotentialformodeloverﬁtting,eventspervariable
were calculated as the number of current cigarette-smoking events
divided by the number of estimated model parameters. In the
ﬁnal current cigarette-smoking model, there were 1,479 current
smokers and 33 estimated parameters, giving an EPV of 44.82.
This value exceeds the commonly used minimum threshold of
10 events per variable, suggesting adequate event support for the
ﬁnal explanatory model. Because the analysis was explanatory
rather than intended for individual risk prediction, EPV was
interpreted as a model-stability diagnostic rather than as evidence
ofpredictivevalidity.
Themultivariableweightedlogisticregressionmodelidentiﬁed
several factors associated with current cigarette smoking among
adolescents (Table10). Region, age, sex, and grade were retained
a priori, while other candidate predictors were selected using
stepwise selection from the full model. In the ﬁnal model,
currentcigarettesmokingwaspositivelyassociatedwithevertrying
cigarette smoking, intention to use tobacco in the next 5 years,
ownership of an item with a tobacco logo, and seeing teachers
smoking at school. Protective associations were observed for being
taught about the dangers of tobacco use, believing that long-term
tobacco use leads to cancer, and reporting ever use of shisha. The
multivariable weighted logistic regression results for current e-
cigaretteuseamongadolescentsinthepooledsamplefromGhana,
Mauritius,Seychelles,andTogoarepresentedin Table11.
Cross platform implementation and validation
Parallel analytical workﬂows were implemented in
R (see SupplementarymaterialS3a ) and Python (see
SupplementarymaterialS3b ). R used native complex survey
methods, while Python applied survey weighted generalized linear
models with normalized weights. Identical model speciﬁcations
were ﬁtted in both platforms, and point estimates were compared
to assess reproducibility. Cross-platform validation results are
presented in Table12 and demonstrate near-identical adjusted
odds ratios for key predictors. Although Python does not natively
account for survey stratiﬁcation and clustering, the present
comparison focused on reproducibility of point estimates. Formal
variance estimation and statistical inference were based on the
R implementation, which fully incorporated the complex survey
design. Therefore, validation was restricted to consistency of point
estimates rather than equivalence of statistical inference. Python’s
statsmodels.GLM with freq_weights implements survey-weighted
estimationbutdoesnotnativelysupportstratiﬁcationorclustering
adjustments. For full complex survey support in Python, use
Frontiersin AppliedMathematicsandStatistics 10 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 9 Descriptivecharacteristicsof adolescents includedin the pooledmulti-countryanalysis, Ghana, Mauritius,Seychelles, and Togo,2015–2019, n =15,914.
Variable Category Unweighted n Unweighted % Weighted %
Age, years 11 379 2.38 2.51
12 1,549 9.73 4.66
13 3,853 24.21 24.33
14 3,866 24.29 25.49
15 3,991 25.08 32.69
16 1,579 9.92 6.85
17 697 4.38 3.47
Sex Male 7,798 49.00 52.15
Female 8,116 51.00 47.85
Schoolgrade Year7 1,003 6.30 7.00
Year8 3,540 22.24 33.57
Year9 5,764 36.22 31.91
Year10 3,362 21.13 26.49
Year11 1,852 11.64 0.97
Year12 393 2.47 0.06
Evertriedcigarettesmoking No 12,926 81.22 90.27
Yes 2,988 18.78 9.73
Evertriedsmokelesstobacco No 14,888 93.55 91.82
Yes 1,026 6.45 8.18
Exposedtosmokinginpublicplaces Yes 15,914 100.00 100.00
Exposedtosmokingatschool No 11,051 69.44 76.13
Yes 4,863 30.56 23.87
Banonsmokinginenclosedspaces No 5,413 34.01 33.29
Yes 10,501 65.99 66.71
Banonsmokinginpublicplaces No 6,197 38.94 34.02
Yes 9,717 61.06 65.98
Taughtaboutdangersofsmokinginschool No 8,228 51.70 47.46
Yes 7,686 48.30 52.54
Sawtobaccoadvertisementsontelevision No 8,199 51.52 55.34
Yes 7,715 48.48 44.66
Heardtobaccoadvertisementsonradio No 13,606 85.50 84.34
Yes 2,308 14.50 15.66
Ownedanitemwithatobaccologo No 14,348 90.16 91.64
Yes 1,566 9.84 8.36
Closefriendssmoke No 14,349 90.17 92.80
Yes 1,565 9.83 7.20
Intendstosmokeinthenext12months No 14,644 92.02 94.27
Yes 1,270 7.98 5.73
Heardofe-cigarettes No 11,608 72.94 84.77
Yes 4,306 27.06 15.23
Everusedshisha No 14,388 90.41 91.74
Yes 1,526 9.59 8.26
Country Ghana 5,430 34.12 74.34
Mauritius 4,123 25.91 2.58
Seychelles 2,453 15.41 0.33
Togo 3,908 24.56 22.75
(Continued)
Frontiersin AppliedMathematicsandStatistics 11 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 9 (Continued)
Variable Category Unweighted n Unweighted % Weighted %
Surveyyear 2015 2,453 15.41 0.33
2016 4,123 25.91 2.58
2017 5,430 34.12 74.34
2019 3,908 24.56 22.75
Socioeconomicstatus Low 8,039 50.52 38.08
Middle 4,210 26.45 39.12
High 3,665 23.03 22.79
Currente-cigaretteuse No 14,938 93.87 95.11
Yes 976 6.13 4.89
specialized packages (samplics, surveystat) or interface with R
via rpy2. Our validation shows equivalent point estimates but
potentiallydiﬀerentstandarderrors.
The objective of the cross-platform comparison was not
to establish statistical equivalence between R and Python, but
rather to evaluate whether identical model speciﬁcations produced
similar substantive conclusions regarding predictor importance
and direction of association. Variance estimation remained the
responsibility of the R implementation, which fully accounted for
thecomplexsurveydesign.
Results of cross platform analysis
Cross platform validation was carried out using the pooled
multi country dataset comprising 15,914 adolescents. When
comparablemodelspeciﬁcations,convergencecriteria,andrandom
seeds were applied, the R and Python implementations produced
almost identical eﬀect estimates. Diﬀerences in adjusted odds
ratios were consistently below 0.01, indicating strong consistency
in point estimation across platforms. Although Python does
not natively account for survey stratiﬁcation and clustering, the
present comparison focused primarily on reproducibility of point
estimates. The adjusted odds ratios obtained from R and Python
were virtually identical, indicating consistency in substantive
conclusions across platforms. Formal variance estimation and
inference were based on the R implementation, which fully
incorporated the complex survey design. This validation step
strengthens conﬁdence in the reproducibility of point estimates
and supports the use of either platform for exploratory modeling,
provided that formal variance estimation and inference continue
to rely on software capable of incorporating the full complex
surveydesign.
Key methodological ﬁndings
The methodological contribution of this study lies in
formalizing a constrained, theory-informed variable selection
strategy for complex survey data that is reproducible across
softwareplatformsandtransferabletoothermulti-stagepopulation
surveys. Across both the single-country and pooled multi-country
analyses, the framework showed theory-constrained consistency,
with a priori demographic variables retained by design and several
modiﬁable predictors selected under the same modeling rules.
Because empirical selection frequencies, bootstrap resampling,
and cross-validation-based stability analyses were not performed,
these ﬁndings should not be interpreted as formal evidence of
algorithmic stability. Instead, the observed consistency reﬂects the
use of a constrained modeling framework, harmonized predictor
deﬁnitions,andpre-speciﬁedtheory-informedcovariates.
The results were also strikingly consistent across analytical
platforms. When identical constraints and harmonized inputs
were applied, the R and Python implementations produced
comparable point estimates and retained the same predictors.
This cross-platform agreement indicates that the framework
is driven by methodology rather than software choice, and
that substantive conclusions remain intact across computational
environments, provided that complex survey design features are
correctlyspeciﬁed.
Crucially, the constrained selection strategy ensured that key
confoundersparticularlydemographicanddesign-relatedvariables
were protected throughout the modeling process, regardless
of statistical signiﬁcance. This led to models that were both
interpretable and theoretically grounded, reducing redundancy
among correlated predictors without sacriﬁcing conceptual
coherence. In the ﬁnal current cigarette-smoking model, a priori
demographic variables were retained by design alongside selected
modiﬁablepredictors.Modeldiagnosticswerereportedtoimprove
transparency, but were interpreted descriptively because the
objective was explanatory modeling rather than individual-
level risk prediction. For the current cigarette-smoking model,
discrimination was good, with a C-statistic of 0.856 (95% CI: 0.841
to 0.870). The Brier score was 0.094, and the Hosmer-Lemeshow
test showed no strong evidence of poor calibration (P = 0.104).
For the secondary current e-cigarette-use model, discrimination
was also good, with a C-statistic of 0.847 (95% CI: 0.834 to 0.859),
and the Brier score was 0.050. However, the Hosmer-Lemeshow
test indicated calibration misﬁt for the e-cigarette model,χ2(8) =
117.57, P < 0.0001. These diagnostics support transparent model
reporting but should not be interpreted as evidence that either
modelisintendedforindividual-levelprediction.
Together, these ﬁndings highlight the value of disciplined,
theory-informed constraint when modeling adolescent smoking
behavior using complex survey data and point to the broader
applicabilityofthisapproachforpopulation-basedhealthresearch.
As a sensitivity check, selected predictors were compared under
AIC- and BIC-based selection. Predictors retained under both
Frontiersin AppliedMathematicsandStatistics 12 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 10 Multivariableweightedlogisticregression model of factorsassociated withcurrent
cigarettesmokingamong adolescents inZambia.
Predictor Adjusted OR
(95% CI)
P-value
Age, years
12vs.11 0.37 (0.18 to 0.79) 0.009
13vs.11 0.66(0.36to1.29) 0.205
14vs.11 0.69(0.38to1.34) 0.258
15vs.11 0.71(0.38to1.39) 0.301
16vs.11 0.81(0.43to1.60) 0.527
17vs.11 0.65(0.33to1.34) 0.233
Sex
Malevs.female 1.07(0.88to1.31) 0.494
School grade
Grade8vs.Grade7 0.94(0.74to1.19) 0.607
Grade9vs.Grade7 0.69 (0.52 to 0.90) 0.007
Region
ROCvs.Lusaka 0.98(0.78to1.24) 0.878
Tobaccoregionsvs.Lusaka 1.01(0.79to1.30) 0.925
Smoking behavior and susceptibility
Evertriedcigarettesmokingvs.no 1.53 (1.13 to 2.05) 0.005
Intentiontousetobaccoinnext5
yearsvs.no
1.89 (1.35 to 2.63) <0.001
Triedshishavs.no 0.55 (0.41 to 0.75) <0.001
Useofhand-rolledcigarettevs.no 0.82(0.49to1.31) 0.419
Social and school environment
Friendssmoketobaccovs.no 1.04(0.79to1.36) 0.775
Parent/guardiansmokesinhomevs.
no
0.84(0.59to1.16) 0.302
Peoplesmokeinschoolvs.no 0.95(0.74to1.22) 0.710
Sawteacherssmokingatschoolvs.
no
1.88 (1.35 to 2.58) <0.001
Media, advertising, and product exposure
Exposuretoanti-tobaccomedia
messagesvs.no
1.08(0.87to1.32) 0.492
Heardofelectroniccigarettevs.no 0.95(0.74to1.21) 0.676
Ownitemwithtobaccoproductvs.
no
1.69 (1.21 to 2.33) 0.002
Seepeopleusingtobaccoon
televisionvs.no
0.85(0.69to1.04) 0.118
Seetobaccoadvertvs.no 1.16(0.89to1.51) 0.257
Knowledge and tobacco-related beliefs
Long-termtobaccouseleadstodrug
usevs.no
0.82(0.65to1.03) 0.095
Long-termtobaccouseleadsto
cancervs.no
0.40 (0.32 to 0.50) <0.001
Taughtaboutdangersoftobaccouse
vs.no
0.42 (0.34 to 0.52) <0.001
(Continued)
TABLE 10 (Continued)
Predictor Adjusted OR
(95% CI)
P-value
Socioeconomic status
Middlevs.low 0.84(0.64to1.10) 0.219
Richvs.low 1.03(0.82to1.29) 0.829
OR,oddsratio;CI,conﬁdenceinterval.
The model was adjusted using stepwise selection starting from the full model, with region,
age,sex,andgraderetainedapriori.StatisticallysigniﬁcantassociationsatP <0.05areshown
inbold.Theevents-per-variableassessmentindicatedadequatemodelsupport:1,479 current
smokers divided by 33 estimated parameters, giving an EPV of 44.82. Model diagnostics for
the current cigarette-smoking model were: AIC= 2812.3, BIC= 3010.1, C-statistic= 0.856
(95%CI:0.841to0.870),Brierscore =0.094,andHosmer-LemeshowP =0.104.
criteria were interpreted as more robustly supported, while
predictors selected only under AIC were interpreted as more
model-dependent(see SupplementaryTablesS3 ,S4).
Discussion
Methodological innovations
This study contributes a practical and generalizable solution
to a long-standing methodological challenge in complex survey
analysis: how to reduce high-dimensional predictor sets without
sacriﬁcing theoretical coherence, confounding control, or design-
based validity. This framework introduces several important
methodological advances for analysing GYTS data in a way that is
both rigorous and practical. First, the use of constrained stepwise
selection allows key demographic variables to be retained in
the model while still permitting data driven selection of other
predictors. This approach strikes a balance between theory and
parsimony, and directly addresses well known weaknesses of fully
unconstrained stepwise methods that may drop variables of clear
publichealthimportance[ 54].Byprotectingapriorifactorssuchas
age, sex, and grade, the resulting models remain interpretable and
policy relevant [10]. Although modern regularization approaches
such as LASSO and Elastic Net can improve prediction accuracy,
theydonotnaturallypreservetheoreticallyimportantconfounders
and currently have limited support within design-based survey
analysis frameworks. Future work should explore survey-weighted
penalizedregressionasanextensionoftheproposedmethodology.
A second innovation relates to cross platform reproducibility
[55]. Providing parallel implementations in both R and Python
enables researchers to replicate ﬁndings across analytical
environments and select software based on institutional capacity
rather than technical constraints. This is particularly important
in global health settings where access to software, training, and
long-term support varies widely. The availability of parallel code
also strengthens transparency and reproducibility, which are
increasinglyexpectedinmulticountryepidemiologicalresearch.
The framework also introduces an educational harmonization
protocol that supports valid comparisons across countries
with diﬀerent schooling systems [ 50]. Mapping grades to
comparable educational stages reduces misclassiﬁcation and
improves the interpretability of cross-country estimates.
Frontiersin AppliedMathematicsandStatistics 13 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 11 Multivariableweightedlogisticregression model of factorsassociated withcurrent
e-cigarette use amongadolescents (n =15,914)inGhana, Mauritius,Seychelles, and Togo.
Predictor Adjusted OR
(95% CI)
P-
value
Age (years)∗
11(Reference) 1.00
12 0.75(0.37to1.51) 0.420
13 0.38 (0.21 to 0.68) 0.001
14 0.40 (0.22 to 0.71) 0.002
15 0.82(0.47to1.42) 0.470
16 0.76 (0.42 to 1.41) 0.390
17 0.41(0.20to0.83) 0.010
Sex∗
Male(Reference) 1.00
Female 1.13(0.94to1.36) 0.190
School grade∗
Year7(Reference) 1.00
Year8 4.27 (2.32 to 7.87) <0.001
Year9 2.50 (1.35 to 4.64) 0.004
Year10 3.57 (1.93 to 6.59) <0.001
Year11 2.60 (1.12 to 6.02) 0.026
Year12 0.66(0.03to12.77) 0.790
Knowledge and exposure
Heardaboute-cigarettes(Yesvs.No) 5.56 (4.60 to 6.70) <0.001
Sawtobaccobrandlogosonproducts(Yes
vs.No)
2.69 (2.17 to 3.34) <0.001
Sawsmokingontelevision(Yesvs.No) 0.66 (0.54 to 0.79) <0.001
Heardanti-smokingmessagesonradio
(Yesvs.No)
1.50 (1.21 to 1.86) <0.001
Smoking behavior and social inﬂuences
Evertriedcigarettes(Yesvs.No) 2.69 (2.15 to 3.36) <0.001
Friendsmokes(Yesvs.No) 2.44 (1.93 to 3.09) <0.001
Intendstosmokewithin12months(Yes
vs.No)
1.67 (1.29 to 2.15) <0.001
Everusedshisha(Yesvs.No) 1.56 (1.24 to 1.95) <0.001
Exposuretosmokingatschool(Yesvs.No) 1.32 (1.09 to 1.61) 0.005
Evertriedsmokelesstobacco(Novs.Yes) 0.18 (0.14 to 0.21) <0.001
School and policy factors
Smokingprohibitedinpublicplaces(Yes
vs.No)
0.56 (0.47 to 0.68) <0.001
Taughtaboutthedangersofsmokingin
school(Yesvs.No)
0.53 (0.43 to 0.64) <0.001
The asterisk (∗) identiﬁes the demographic variables—age, sex, and school grade—that were
retained a priori in the multivariable model regardless of statistical signiﬁcance; OR, odds
ratio;CI,conﬁdenceinterval.
Values are adjusted odds ratios from a weighted multivariable logistic regression model of
current e-cigarette use. The model was ﬁtted using stepwise selection starting from the full
model, with region, age, sex, and grade retained a priori. Statistically signiﬁcant associations
atP <0.05areshowninbold.Modeldiagnosticsforthee-cigarette-usemodelwere:C-statistic
=0.847(95%CI:0.834to0.859),Brierscore =0.050,andHosmer-Lemeshow χ2(8)=117.57,
P < 0.0001. The Hosmer-Lemeshow result indicates calibration misﬁt; therefore, this model
shouldbeinterpretedasanexplanatoryandmethodologicaldemonstrationratherthanasan
individual-levelpredictionmodel.
This step is often overlooked or inconsistently applied in
previous multi country GYTS analyses, yet it is critical
when comparing adolescent behaviors across diverse
educationalcontexts.
Software comparison and
recommendations
Table13 shows the comparison between R and Python
highlights clear strengths and trade oﬀs that are relevant for
GYTS analysis [56]. R oﬀers strong native support for complex
survey designs, including full speciﬁcation of weights, strata,
and clusters, making it the preferred option for producing
oﬃcial prevalence estimates and survey weighted descriptives
[57]. It also supports constrained stepwise selection through
established tools, which aligns well with the proposed modeling
framework (see Table13). Python, on the other hand, excels
in machine learning integration and advanced predictive
modeling, supported by a rapidly growing data science ecosystem
[58]. While its support for complex survey designs remains
limited, it is well suited for extending analyses into machine
learning applications once core survey-based estimates have
been established. Overall, R is recommended for primary GYTS
analysis and oﬃcial reporting, while Python is best positioned as
a complementary tool for exploratory modeling and advanced
analytics, depending on the research objective and available
expertise.
Predictor variable selection, lessons for
future studies
Several clear lessons emerge from the way predictors behaved
across countries and platforms. Age should always be treated as
a categorical variable rather than a continuous one, as risk does
not increase in a straight line and tends to peak in early to mid-
adolescence, particularly among those aged 13 to 14 years [34].
Core demographic factors such as age, sex, grade, and region
should be protected as a priori variables to reduce confounding
and improve comparability across settings. Awareness related
variables, especially awareness of tobacco products, consistently
showthestrongestassociationsandshouldbecentraltoanyGYTS
smoking model. Social context also matters deeply, with peer and
parental smoking repeatedly emerging as dominant predictors,
underscoring the need to capture the social environment in a
comprehensive way. Policy related variables should be retained
even when they are not statistically signiﬁcant, as they reﬂect
modiﬁableleversforpublichealthaction[ 46].Incontrast,product
speciﬁc variables such as brand or ﬂavor preferences are best
excluded from initiation models, as they introduce selection bias
andblurcausalinterpretation.
Strengths and limitations
This study has several notable strengths. First, it addresses a
major methodological gap in the GYTS literature by providing a
Frontiersin AppliedMathematicsandStatistics 14 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
TABLE 12 Cross-platform validationofadjusted oddsratios.
Predictor variable R (survey package),
OR (95% CI)
Exact
P-value,R
Python
(statsmodels), OR
(95% CI)
Exact P-value,
Python
Absolute
difference
Awarenessoftobacco
products(Yes)
5.61(4.65–6.78) 7.33×10−72 5.61(4.65–6.78) 7.33×10−72 <0.01
Friendsmokes(Probablyyes) 4.57(3.34–6.25) 1.98×10−21 4.57(3.34–6.25) 1.98×10−21 <0.01
Evertriedcigarettes(Yes) 2.62(2.09–3.28) 5.40×10−17 2.62(2.09–3.28) 5.40×10−17 <0.01
Taughtdangersofsmoking
(Yes)
0.54(0.44–0.66) 2.57×10−9 0.54(0.44–0.66) 2.57×10−9 <0.01
Anti-tobaccomediamessages
(Yes)
0.61(0.50–0.75) 1.76×10−6 0.61(0.50–0.75) 1.76×10−6 <0.01
TABLE 13 Platform comparisonfor GlobalYouthTobaccoSurvey analysis.
Feature R( s u r v e y ) Python (statsmodels) Recommendation
Nativecomplexsurveysupport ✓Excellent(fulldesignspeciﬁcation) χ Limited(frequencyweightsonly) Rforcomplexdesigns
Constrainedstepwiseselection ✓Native(stepAICwithscope) χ Requirescustomimplementation Rforstepwise;Pythonforcustomalgorithms
Survey-weighteddescriptives ✓Comprehensive(svymean,svytotal) χ Manualcalculationrequired Rforoﬃcialestimates
Machinelearningintegration /Delta1Growing(tidymodels,caret) ✓Excellent(scikit-learn,TensorFlow) PythonforMLextensions
Communitysupport ✓Strongepidemiology/biostatistics ✓Growingdatascience/ML Context-dependent
Reproducibilitytools ✓renv,packrat ✓pip,conda,poetry Equivalent
✓indicatesfull,native,orstrongsupport; χ indicateslimitedsupportorafeaturethatrequiresamanual/customimplementation;and /Delta1indicatesgrowingoremergingsupport.
transparent and reproducible framework for analysing complex
survey data. Second, predictor selection was guided by Social
CognitiveTheoryandempiricalevidenceratherthanrelyingsolely
on automated statistical procedures. Third, the framework
explicitly incorporates survey weights, stratiﬁcation, and
clustering, thereby improving the validity of population-level
inference. Fourth, all analytical workﬂows are implemented using
open-source software and accompanied by reproducible code.
Finally, the framework was evaluated using both single-country
and pooled multi-country datasets and is readily adaptable
to other large-scale health surveys that employ multi-stage
samplingdesigns.
This study has several important limitations that should be
considered when interpreting the ﬁndings. In Python, survey
weighted analysis relies on frequency weights and does not fully
account for stratiﬁcation and clustering, which may lead to small
diﬀerences in standard errors compared with full design-based
approaches [59]. Stepwise selection, while practical and widely
used in epidemiological modeling, can produce sample-dependent
variable selection and may increase the risk of overﬁtting.
We mitigated these concerns through theory-based predictor
speciﬁcation, protection of a priori confounders, AIC-based
selection criteria, comparison with BIC-selected predictors where
available, and transparent reporting of all candidate variables. The
cross-sectional nature of GYTS data also limits causal inference,
with temporal ordering inferred based on theory rather than
direct observation. The reliance on complete-case analysis is an
important limitation. Although some individual variables had low
item-levelmissingness,thecumulativeeﬀectofrequiringcomplete
information across all variables led to exclusion of a substantial
number of participants, particularly in the Zambia analysis. If
missingness was related to smoking status, social exposures, or
schoolattendancepatterns,complete-caseestimatesmaybebiased.
Future applications of the framework should consider multiple
imputation or inverse-probability weighting as sensitivity analyses
when missingness is substantial. Finally, tobacco use is self-
reported and may be underestimated due to social desirability,
although the anonymous design of GYTS helps reduce this
bias[60].
Implications for tobacco control
Despite these limitations, the ﬁndings have clear implications
for tobacco control policy and programming. The consistent
importance of awareness, peer inﬂuence, and marketing
exposure points to priority intervention areas. Strengthening
counter marketing campaigns can help reduce the appeal
of tobacco products among adolescents [ 61]. Enforcing
bans on smoking in public places and school environments
remains essential, both to reduce exposure and to shift social
norms. School based education programs continue to show
protective eﬀects and should be expanded and better integrated
into curricula [ 62]. Interventions that directly address peer
norms, including social network-based approaches, may be
Frontiersin AppliedMathematicsandStatistics 15 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
especially eﬀective during adolescence when social inﬂuence
isstrongest.
Replicability to other complex surveys
The proposed framework is highly transferable to other large-
scale surveillance systems that use stratiﬁed multi stage cluster
sampling with survey weights. Surveys such as GATS [63], WHO
STEPS [64], and GSHS [65] share core design features with GYTS,
making direct adaptation feasible. With appropriate mapping of
strata, primary sampling units, and weights, the same principles
ofharmonization,constrainedvariableselection,anddesign-based
analysis can be applied. While R remains the strongest option for
full survey speciﬁcation, Python can complement these analyses
where advanced modeling is required. Across all platforms and
surveys, careful attention to design eﬀects is essential, as ignoring
clustering and stratiﬁcation leads to underestimated uncertainty
andmisleadingconﬁdenceintervals.
Conclusion
This methodological framework provides researchers with
adaptable, reproducible workﬂows for GYTS smoking behavior
analysis that address critical gaps in current practice. The R
implementation serves as the reference standard, oﬀering robust,
well-validated native support for complex, two-stage survey
designs and oﬃcial variance estimation consistent with GYTS
methodological requirements. The Python implementation
is provided to enhance reproducibility, transparency, and
extensibility, particularly for custom algorithms and machine-
learning–based explorations, but is not intended as the primary
platform for variance estimation. Both platforms produce
highly comparable point estimates when properly conﬁgured,
although R remains the preferred platform for valid variance
estimation because it fully supports complex survey designs.
The comprehensive predictor variable justiﬁcation framework,
grounded in Social Cognitive Theory and supported by systematic
review evidence, ensures that analyses are theoretically coherent,
empirically supported, and policy relevant. By standardizing
variable selection and harmonization protocols, we enable
valid cross-country comparisons and meta-analytic synthesis,
strengthening the evidence base for adolescent tobacco
controlglobally.
Data availability statement
The original contributions presented in the study are included
in the article/Supplementarymaterial, further inquiries can be
directedtothecorrespondingauthor.
Ethics statement
The studies involving humans were approved by the various
countries using GYTS have respective local approvals from
Ministries of Health and WHO. The studies were conducted
in accordance with the local legislation and institutional
requirements. Written informed consent for participation in
this study was provided by the participants’ legal guardians/next
ofkin.
Author contributions
WN: Writing – review & editing, Writing – original draft,
Formal analysis, Visualization, Validation, Conceptualization,
Methodology. CZ: Methodology, Validation, Writing – review
& editing. LK: Supervision, Writing – review & editing,
Methodology,Validation.
Funding
The author(s) declared that ﬁnancial support was not received
forthisworkand/oritspublication.
Acknowledgments
The authors acknowledge the World Health Organization and
the United States Centers for Disease Control and Prevention for
makingtheGlobalYouthTobaccoSurvey(GYTS)datasetspublicly
available. We also thank the Ministries of Health and Education
in the participating countries for implementing the surveys and
facilitatingaccesstonationallyrepresentativedata.
Conﬂict of interest
The author(s) declared that this work was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construedasapotentialconﬂictofinterest.
Generative AI statement
The author(s) declared that Generative AI was not used in the
creationofthismanuscript.
Any alternative text (alt text) provided alongside ﬁgures in
this article has been generated by Frontiers with the support of
artiﬁcial intelligence and reasonable eﬀorts have been made to
ensureaccuracy,includingreviewbytheauthorswhereverpossible.
Ifyouidentifyanyissues,pleasecontactus.
Frontiersin AppliedMathematicsandStatistics 16 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsedbythepublisher.
Supplementary material
The Supplementary Material for this article can be found
online at: https://www.frontiersin.org/articles/10.3389/fams.2026.
1895038/full#supplementary-material
The GitHub repository is available at: https://github.com/
andreasngambi-star/GYTS_analysis_R_Python.git, and the
persistentZenodoDOIis 10.5281/zenodo.21254547.
References
1. Carrión-Valero F, Ribera-Osca JA, Martin-Moreno JM, Martin-Gorgojo A.
Prevention of tobacco use in an adolescent population through a multi-personal
interventionmodel. TobPrevCessat. (2023)9:37.doi:10.18332/tpc/162980
2 .X iB ,L i a n gY ,L i uY ,Y a nY ,Z h a oM ,M aC ,e ta l .T o b a c c ou s ea n ds e c o n d -
hand smoke exposure in young adolescents aged 12–15 years: data from 68
low-income and middle-income countries. Lancet Glob Health. (2016) 4:e795–
e805.doi:10.1016/S2214-109X(16)30187-5
3. WarrenCW,RileyL,AsmaS,EriksenMP,GreenL,BlantonC,etal.Tobaccouseby
youth:asurveillancereportfromtheGlobalYouthTobaccoSurveyproject. BullWorld
HealthOrgan. (2000)78:868–76.
4. Warren CW. The Global Youth Tobacco Survey (GYTS): linking data to the
implementationoftheWHOframeworkconventionontobaccocontrolpersonal .BMC
PublicHealth. (2008)8:S1.doi:10.1186/1471-2458-8-S1-S1
5. Sun J, Xi B, Ma C, Li Z, Zhao M, Bovet P. Cigarette access and purchase patterns
amongadolescentsmokersaged12-16yearsin140countries/territories, GlobalYouth
TobaccoSurvey2010-2018. JGlobHealth. (2022)12:04101.doi:10.7189/jogh.12.04101
6. Ciobanu A, Tarasenko Y, Lebedeva E. Global Youth Tobacco Survey: prevalence of
tobacco use in countries of the WHO European Region.Tob Prev Cessat.(2023) 9:
(Suppl.2):A107.doi:10.18332/tpc/172834
7. Gyeltshen T, Rahman M. Trends in prevalence and correlates of tobacco
use among school-going adolescents in Bhutan: a secondary data analysis of
the 2004-2019 Global Youth Tobacco Survey. PLoS Glob Public Health. (2024)
4:e0003544.doi:10.1371/journal.pgph.0003544
8. DeyD,HaqueMS,IslamMM,AishiUI,ShammySS,MayenMSA,etal.Theproper
application of logistic regression model in complex survey data: a systematic review.
BMCMedResMethodol .(2025)25:15.doi:10.1186/s12874-024-02454-5
9. Ng’ambi WF, Muula AS. A reproducible R workﬂow to preserve variable and value
labelsinStata,SPSS,andSASdatasetsfortransparentandreproduciblehealthresearch.
MalawiMedJJMedAssocMalawi. (2025)37:193–206.doi:10.4314/mmj.v37i3.10
10. Ng’ambiWF.Apracticalguidetokeyconsiderationsinlogisticregression. Malawi
MedJ. (2023)35:135–7.Availableonlineat:https://www.mmj.mw/?p=13527(Accessed
Feburary28,2026).
11. Kahlert J, Gribsholt SB, Gammelager H, Dekkers OM, Luta G. Control of
confounding in the analysis phase - an overview for clinicians.Clin Epidemiol.(2017)
9:195–204.doi:10.2147/CLEP.S129886
12. Masuadi E, Mohamud M, Almutairi M, Alsunaidi A, Alswayed A, Aldhafeeri
OF. Trends in the usage of statistical software and their associated study
designs in health sciences research: a bibliometric analysis. Cureus. (2021)
13:e12639.doi:10.7759/cureus.12639
13. Orhani S. Comparative analysis of statistical results generated by Python, R, SPSS,
andExcel. IntJProgressResEngManagSci. (2025)5:265–77.
14. Zhai S, Hash J, Ward TM, Yuwen W, Sonney J. Analysis, evaluation, and
reformulation of social cognitive theory: toward parent-child shared management in
sleephealth. JPed ia trNurs.(2023)73:e65–e74.doi:10.1016/j.pedn.2023.07.011
15. Luszczynska A, Schwarzer R. Social Cognitive Theory. In: Predicting Health
Behaviour,3rded. McGraw-Hill/OpenUniversityPress(2015).p.225–51.
16. NationalCenterforChronicDiseasePreventionandHealthPromotion(US)Oﬃce
on Smoking and Health. 4, Social, environmental, cognitive, and genetic inﬂuences on
the use of tobacco among youth. In:Preventing Tobacco Use among Youth and Young
Adults: A Report of the Surgeon General.Atlanta, GA: Centers for Disease Control
andPrevention(US)(2012).Availableonlineat:https://www.ncbi.nlm.nih.gov/books/
NBK99236/(AccessedFeburary20,2026).
17. Eisenberg ME, Toumbourou JW, Catalano RF, Hemphill SA. Social norms
in the development of adolescent substance use: a longitudinal analysis of
the International Youth Development Study. J Youth Adolesc. (2014) 43:1486–
97.doi:10.1007/s10964-014-0111-1
18. Kirkwood BR, Sterne JAC. Essential Medical Statistics. Oxford; Malden, MA:
BlackwellScientiﬁcPublications(2003).
19. Tate C, Kumar R, Murray JM, Sanchez-Franco S, Montgomery SC, Dunne L, et al.
Socio-environmental and psychosocial predictors of smoking susceptibility among
adolescents with contrasting socio-cultural characteristics: a comparative analysis.
BMCPublicHealth. (2021)21:2240.doi:10.1186/s12889-021-12351-x
20. Jaber R, Mzayek F, Madhivanan P, Khader Y, Maziak W. Predictors of cigarette
smoking progression among a school-based sample of adolescents in Irbid, Jordan: a
Longitudinal Study (2008-2011).Nicotine Tob Res Oﬀ J Soc Res Nicotine Tob.(2016)
18:403–9.doi:10.1093/ntr/ntv100
21. Aditama T, Pradono J, Rahman K, Warren CW, Jones NR, Asma S, et al.
Linking Global Youth Tobacco Survey (GYTS) data to the WHO Framework
Convention on Tobacco Control: the case for Indonesia.Prev Med. (2008) 47:S11–
4.doi:10.1016/j.ypmed.2008.05.003
22. Ayedi Y, Harizi C, Skhiri A, Fakhfakh R. Linking Global Youth Tobacco
Survey (GYTS) data to the WHO Framework Convention on Tobacco Control
(FCTC): the case for Tunisia. Tob Induc Dis. (2022) 20:7. doi: 10.18332/tid/
143994
23. El Dalatony MM, Elkhobby AA, Shubayr MA, Monshi SS, Al-Zalabani
AH, El Desouky ED, et al. Prevalence and predictors of tobacco use
among Saudi adolescents: the Global Youth Tobacco Survey (GYTS)
2022. BMC Public Health. (2025) 25:2733. doi: 10.1186/s12889-025-2
3974-9
24. Erguder T, Çakir B, Aslan D, Warren CW, Jones NR, Asma S. Evaluation
of the use of Global Youth Tobacco Survey (GYTS) data for developing
evidence-based tobacco control policies in Turkey. BMC Public Health. (2008)
8:S4.doi:10.1186/1471-2458-8-S1-S4
25. Sirichotiratana N, Techatraisakdi C, Rahman K, Warren CW, Jones NR, Asma
S, et al. Prevalence of smoking and other smoking-related behaviors reported by
the Global Youth Tobacco Survey (GYTS) in Thailand.BMC Public Health. (2008)
8:S3.doi:10.1186/1471-2458-8-S1-S3
26. WarrenW,GYTSCollaborativeGroup.DiﬀerencesinWorldwideTobaccoUseby
Gender.JSc hHealt h.(2003)73:207–15.
27. World Health Organization. Global Youth Tobacco Survey (GYTS). WHO
Noncommunicable Disease Surveillance, Monitoring and Reporting.(2025). Available
online at: https://www.who.int/teams/noncommunicable-diseases/surveillance/
systems-tools/global-youth-tobacco-survey(AccessedFebruary28,2026).
28. Ministry of Health, Zambia & World Health Organization Regional Oﬃce for
Africa.Zambia2021GlobalYouthTobaccoSurvey(GYTS)CountryReport .Brazzaville:
WHO Regional Oﬃce for Africa (2024). Available online at: https://www.afro.who.
int/countries/zambia/publication/zambia-2021-global-youth-tobacco-survey-gyts-
country-report
29. Logo D, Kyei-Faried S, Oppong FB, Ae-Ngibise KA, Ansong J, Amenyaglo S,
et al. Waterpipe use among the youth in Ghana: lessons from the Global Youth
Tobacco Survey (GYTS) 2017. Tob Induc Dis. (2020) 18:47. doi: 10.18332/tid/12
0937
30. World Health Organization & Ministry of Health and Quality of Life, Mauritius.
Global Youth Tobacco Survey 2016, Mauritius, Variable CR23 (Think other people
smoking harmful). WHO NCD Microdata Repository. Geneva: World Health
Organization(2016).
31. MayenChaconAL,ViswanathanB,BovetP. 2015SeychellesGlobalYouthTobacco
Survey and Comparison with GYTS in 2007 and 2002 . (2016). Available online
at: https://extranet.who.int/fctcapps/sites/default/ﬁles/2023-04/seychelles_2018_
annex-1_GYTS_report_2015.pdf(AccessedMarch02,2026).
32. World Health Organization and Tobacco Control Unit, Togo.Togo 2019 Global
Youth Tobacco Survey (GYTS) Dataset. WHO NCD Microdata Repository. Geneva:
WorldHealthOrganization(2019).
Frontiersin AppliedMathematicsandStatistics 17 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
33. Sallis J, Owen N, Fotheringham M. Behavioral epidemiology: a systematic
framework to classify phases of research on health promotion and disease prevention.
AnnBehavMedPublSocBehavMed. (2000)22:294–8.doi:10.1007/BF02895665
34. Velicer WF, Redding CA, Sun X, Prochaska JO. Demographic variables, smoking
variables, and outcome across ﬁve studies.Health Psychol Oﬀ J Div Health Psychol Am
Psychol Assoc.(2007)26:278–87.doi:10.1037/0278-6133.26.3.278
3 5 .L i nM ,C h uM ,L iX ,M aH ,F a n gZ ,M a oL ,e ta l .F a c t o r si n ﬂ u e n c i n g
adolescent experimental and current smoking behaviors based on social
cognitive theory: a cross-sectional study in Xiamen. Front Public Health. (2023)
11:1093264.doi:10.3389/fpubh.2023.1093264
36. Jawad M, Li W, Filippidis FT. Sociodemographic inequalities in cigarette,
smokeless tobacco, waterpipe tobacco, and electronic cigarette use among adolescents
aged 12–16 years in 114 countries: a cross-sectional analysis.Tob Induc Dis.(2024)
22:1–8.doi:10.18332/tid/191824
37. Kelly AB, O’Flaherty M, Connor JP, Homel R, Toumbourou JW,
Patton GC, et al. The inﬂuence of parents, siblings and peers on pre-
and early-teen smoking: a multilevel model. Drug Alcohol Rev. (2011)
30:381–7.doi:10.1111/j.1465-3362.2010.00231.x
38. Do EK, Bradley K, Fudate-Laus K, Kaur K, Halquist MS, Ray L, et al.
An examination of social and environmental determinants of secondhand
smoke exposure among non-smoking adolescents. Tob Prev Cessat. (2021)
7:1–12.doi:10.18332/tpc/131875
39. Erbaydar T, Lawrence S, Dagli E, Hayran O, Collishaw N. Inﬂuence of social
environment in smoking among adolescents in Turkey.Eur J Public Health.(2005)
15:404–10.doi:10.1093/eurpub/cki040
40. Sardana M, Goel S, Gupta M, Sardana V, Singh BS. Is exposure to tobacco
advertising, promotion and sponsorship associated with initiation of tobacco use
among Current Tobacco Users in Youth in India?Asian Pac J Cancer Prev. (2015)
16:6299–302.doi:10.7314/APJCP.2015.16.15.6299
41. Hébert ET, Vandewater EA, Businelle MS, Harrell MB, Kelder SH, Perry
CL, et al. Tobacco advertising exposure and product use among young
adults: an ecological momentary assessment approach. Addict Behav. (2023)
139:107601.doi:10.1016/j.addbeh.2022.107601
42. Odukoya O, Ladapo O, Okafor I, Osibogun O, Okuyemi K. Exposure
to tobacco advertisements, promotions, and sponsorships among in-school
adolescents in Lagos, Nigeria: a cross-sectional study. Ann Afr Med. (2023)
22:333–9.doi:10.4103/aam.aam_76_22
43. NationalCancerInstitute. Theroleofthemediainpromotingandreducingtobacco
use.Bethesda,MD:U.S.DepartmentofHealthandHumanServices,NationalInstitutes
ofHealth,NationalCancerInstitute(2008).
4 4 .C h i d o - A m a j u o y iO G ,O s a g h a eI ,A g a k uI T ,C h e nB ,M a n t e yD S .E x p o s u r et o
school-based tobacco prevention interventions in low-income and middle-income
countries and its association with psychosocial predictors of smoking among
adolescents: a pooled cross-sectional analysis of Global Youth Tobacco Survey data
from38countries. BMJOpen. (2024)14:e070749.doi:10.1136/bmjopen-2022-070749
45. World Health Organization.WHO Report on the Global Tobacco Epidemic, 2017:
monitoring tobacco use and prevention policies. (2017). Available online at: https://iris.
who.int/bitstream/handle/10665/255874/9789241512824-eng.pdf(AccessedMarch20,
2026).
46. de Looze ME, Henking C, Torsheim T, Currie DB, Weber MW, Alemán-Díaz AY.
The association between MPOWER tobacco control policies and adolescent smoking
across36countries:anecologicalstudyovertime(2006–2014). IntJDrugPolicy. (2022)
109:103871.doi:10.1016/j.drugpo.2022.103871
47. Koh H, Alpert HR, Judge CM, Caughey RW, Elqura LJ, Connolly GN,
et al. Understanding worldwide youth attitudes towards smoke-free policies: an
analysis of the Global Youth Tobacco Survey. Tob Control. (2011) 20:219–
25.doi:10.1136/tc.2010.038885
48. Kirkbride JB, Anglin DM, Colman I, Dykxhoorn J, Jones PB, Patalay P, et al.
The social determinants of mental health and disorder: evidence, prevention and
recommendations. W o r l dP s y c h i a t r yO ﬀJW o r l dP s y c h i a t rA s s o cW P A .(2024) 23:58–
90.doi:10.1002/wps.21160
49. WallachKA.Overcomingbigasbad:branddominanceandtheauthenticitydeﬁcit
ofsustainableproducts:anabstract.In:PantojaF,WuS,editors. FromM icrotoM acro:
Dealing with Uncertainties in the Global Marketplace. AMSAC 2020. Developments in
Marketing Science: Proceedings of the Academy of Marketing Science.C h a m :S p r i n g e r
(2022).p.537–8.
50. Yach D, Warren CM, De Arimatéia Silva VL, Riley L, Eriksen
MP, Henson R, et al. Tobacco use among youth: a cross country
comparisonTobacco control2002113252270175901312198280. Tob Control. (2002)
11:252–70.doi:10.1136/tc.11.3.252
51. MuulaA.Patternsofglobaltobaccouseinyoungpeopleandimplicationsforfuture
chronicdiseaseburdeninadults. Lancet.(2006)16:1.
52. Peiper N, Aramburú C, Thompson K, Abadi M. Diﬀerential patterns of
e-cigarette and tobacco marketing exposures among youth: associations with
substance use and tobacco prevention strategies. Int J Drug Policy. (2020)
86:102925.doi:10.1016/j.drugpo.2020.102925
53. Alimohamadi Y, Sepandi M. Considering the design eﬀect in cluster sampling.J
CardiovascThoracRes. (201911:78.doi:10.15171/jcvtr.2019.14
54. Breuer E, Lee L, De Silva M, Lund C. Using theory of change to design and
evaluate public health interventions: a systematic review. Implement Sci. (2016)
11:63.doi:10.1186/s13012-016-0422-6
55. Stodden V. Enabling reproducible research: open licensing for scientiﬁc
innovation.Science.(2009)13.
56. AbatanSM,OlayemiMS.Theroleofstatisticalsoftwareindataanalysis. IntJAppl
ResStud. (2014)3:1–15.
57. Sakshaug J, Aurelien G. Accounting for complex sampling in
survey estimation: a review of current software tools. JO ﬀS t a t .(2018)
34:721–52.doi:10.2478/jos-2018-0034
58. Abiola B, Pum M.A Comparative Study of Python and R for Data Science and
StatisticalAnalysis.(2024).
59. Diallo MS. Samplics: a comprehensive library for survey sampling in Python.
SurveyStat. (2022)86:32–43.
60. Singh PK, Jain P, Singh N, Singh L, Kumar C, Yadav A, et al. Social
desirability and under-reporting of smokeless tobacco use among reproductive age
women: evidence from National Family Health Survey.SSM Popul Health. (2022)
19:101257.doi:10.1016/j.ssmph.2022.101257
61. Goldberg M, Niedermeier K, Bechtel L, Gorn G. Heightening adolescent vigilance
toward alcohol advertising to forestall alcohol use. J Public Policy Mark. (2006)
25:147–59.doi:10.1509/jppm.25.2.147
62. Zyambo C, Olowski P, Mulenga D, Liamba F, Syapiila P, Siziya S. School tobacco-
related curriculum and behavioral factors associated with cigarette smoking among
school-goingadolescentsinZambia:resultsfromthe2011GYTSstudy. TobInducDis .
(2022)20:42.doi:10.18332/tid/146960
63. WakeﬁeldM,MorleyC,HoranJ,CummingsKM.Thecigarettepackasimage. Tob
Control.(2002)11:i73.
64. WHO.Noncommunicablediseasesurveillance,monitoringandreporting:STEPwise
ApproachtoNCDRiskFactorSurveillance(STEPS) .(2025).
65. Thomas RE, McLellan J, Perera R. School-based programmes for
preventing smoking. Cochrane Database Syst Rev. (2013) 2013:CD001293.
doi:10.1002/14651858.CD001293.pub3
66. Sreeramareddy CT, Acharya K, Manoharan A. Electronic cigarettes use and ‘dual
use’ among the youth in 75 countries: estimates from Global Youth Tobacco Surveys
(2014-2019).SciRep.(2022)12:20967.doi:10.1038/s41598-022-25594-4
67. Galiano A, Blasco J, Martín-Álvarez JM, Del Arco Osuna MA. Impact of
tobacco use and prevention laws on regional cigarette sales: an analysis of
provincial disparities and convergence patterns in Spain.Health Econ Rev. (2025)
15:44.doi:10.1186/s13561-025-00641-8
68. Yu Z, Wang M, Fu J. Association between waterpipe use and susceptibility
to cigarette smoking among adolescents and young adults who never
smoked: a systematic review and meta-analysis. Tob Induc Dis. (2023)
21:1–11.doi:10.18332/tid/159621
69. Song AV, Morrell HER, Cornell JL, Ramos ME, Biehl M, Kropp RY, et al.
Perceptions of smoking-related risks and beneﬁts as predictors of adolescent
smoking initiation.Am J Public Health.(2009) 99:487–92. doi: 10.2105/AJPH.2008.
137679
70. HarakehZ,ScholteRHJ,VermulstAA,deVriesH,EngelsRCME.Parentalfactors
and adolescents’ smoking behavior: an extension ofThe theory of planned behavior.
PrevMed. (2004)39:951–61.doi:10.1016/j.ypmed.2004.03.036
71. Simons-Morton BG, Farhat T. Recent ﬁndings on peer group inﬂuences on
adolescent smoking. JP r i mP r e v .(2010) 31:191–208. doi: 10.1007/s10935-010-
0220-x
72. Bricker JB, Peterson AV, Andersen MR, Leroux BG, Rajan KB, Sarason IG.
Close friends’, parents’, and older siblings’ smoking: reevaluating their inﬂuence
on children’s smoking. Nicotine Tob Res Oﬀ J Soc Res Nicotine Tob. 8:217–26.
(2006).doi:10.1080/14622200600576339
73. Page RM, Hammermeister J, Roland M. Are high school students accurate or
cluelessinestimatingsubstanceuseamongpeers? Adolescence.(2002)37:567.
74. Yang T, Xu X, Rockett IRH, Guo W, Zhou H. Eﬀects of household, workplace,
and public place smoking restrictions on smoking cessation.Health Place. (2011)
17:954–60.doi:10.1016/j.healthplace.2011.04.003
75. ChoiK,ForsterJ.Characteristicsassociatedwithawareness,perceptions,anduseof
electronic nicotine delivery systems among young US Midwestern adults.Am J Public
Health.(2013)103:556–61.doi:10.2105/AJPH.2012.300947
76. Wellman RJ, Sugarman DB, DiFranza JR, Winickoﬀ JP. The extent to
which tobacco marketing and tobacco use in ﬁlms contribute to children’s
use of tobacco: a meta-analysis. Arch Pediatr Adolesc Med . (2006) 160:1285–
96.doi:10.1001/archpedi.160.12.1285
77. Charlesworth A, Glantz SA. Smoking in the movies increases adolescent smoking:
areview. Pediatrics.(2005)116:1516–28.doi:10.1542/peds.2005-0141
Frontiersin AppliedMathematicsandStatistics 18 frontiersin.org

Ng’ambi et al. 10.3389/fams.2026.1895038
78. Wakeﬁeld M, Morley C, Horan JK, Cummings KM. The cigarette pack as
image: new evidence from tobacco industry documents. Tob Control. (2002)
11:i73.doi:10.1136/tc.11.suppl_1.i73
79. FlynnBS,WordenJK,Secker-WalkerRH,PiriePL,BadgerGJ,CarpenterJH,etal.
Mass media and school interventions for cigarette smoking prevention: eﬀects 2 years
aftercompletion. AmJPublicHealth. (1994)84:1148–50.doi:10.2105/AJPH.84.7.1148
80. Thomas RE, McLellan J, Perera R. School-based programmes
for preventing smoking. Cochrane Database Syst Rev . (2013)
2013:CD001293.doi:10.1002/14651858.CD001293.pub3
81. Levy DT, Ellis JA, Mays D, Huang A-T. Smoking-related deaths averted due
to three years of policy progress. Bull World Health Organ. (2013) 91:509–
18.doi:10.2471/BLT.12.113878
Frontiersin AppliedMathematicsandStatistics 19 frontiersin.org
