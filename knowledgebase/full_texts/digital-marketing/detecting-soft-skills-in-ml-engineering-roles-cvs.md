---
title: Detecting Soft Skills in ML Engineering Roles CVs
url: https://arxiv.org/abs/2608.10046
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Aidin Azamnouri
- Nouran Ayad
- Justus Bogner
- Stefan Wagner
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.10046
pages: 28
chars: 149047
fetched_at: '2026-11-08T13:20:29+00:00'
kb_version: 1
---

# Detecting Soft Skills in ML Engineering Roles CVs

Detecting Soft Skills in ML Engineering Roles CVs
Aidin Azamnouria,∗, Nouran Ayada, Justus Bognerb and Stefan Wagnera
aChair of Software Engineering, TUM School of Computation, Information and Technology, Technical University of Munich, Heilbronn, Germany
bSoftware and Sustainability (S2) Group, Vrije Universiteit Amsterdam, Amsterdam, The Netherlands
ARTICLE INFO
Keywords:
Soft Skills
CV
Resume
ML Engineers
Data Scientists
Software Engineers
ABSTRACT
Soft skills shape collaboration among ML engineers, data scientists, and software engineers building
ML-enabled systems, yet what we know about them comes almost entirely from the demand side.
Job advertisements, surveys, and hiring manager interviews capture what employers ask for. How
candidates themselves articulate these competencies has not been studied, and existing CV-mining
work is both keyword-based, so it cannot see skills conveyed through narrative, and descriptive,
reporting frequency rankings without testing whether group differences exceed sampling variation.
Weclosebothgaps.Usingabalancedcorpusof300curatedCVsspanningthethreeroles,weextract
explicitly listed and implicitly narrated soft skills with an LLM-based pipeline validated against a
human-annotated ground truth, a distinction that existing extractors were not designed to make. We
then convert the demand-side literature’s claims into 13 falsifiable hypotheses about role signatures,
seniority progression, and disclosure style, and test them with effect sizes under family-wise error
control, so that candidate-side data can corroborate or contradict the demand-side account rather
than merely illustrate it. Eleven hypotheses are supported, one partially, and one refuted. Candidates
disclosesoftskillsthroughnarrativeratherthankeywordlistsbyroughlythreetoone,andmostsofor
thecompetenciesemployersvaluemost:leadership,coordination,andmentoring(88–96%narrative).
Seniority nearly triples the odds of articulating leadership. That competency, assumed universal in
priorwork,isarticulatedbysoftwareengineersathalftherateoftheirpeers.Technicalcandidatesdo
articulate soft skills, in a form keyword-based screening systematically misses.
1. Introduction
The development of machine learning (ML)-enabled
systems increasingly demands collaboration and communi-
cation acrossmultiple engineeringroles, includingsoftware
engineers, ML engineers, and data scientists [37, 3, 21].
While these roles differ in their technical responsibilities,
they share a common dependency. Successful delivery re-
quires effective collaboration and communication among
team members, not just the correct implementation of the
requirementsandneeds[37,32,7].AsMLsystemsbecome
moredeeplyembeddedinbusiness-criticalproducts,organi-
zations face challenges that are not purely technical. Hence,
these challenges make soft skills an increasingly important
complementtotechnicalexpertiseinmodernartificialintel-
ligence (AI) and software engineering work [36, 10].
Soft skills have been repeatedly recognized as key pre-
dictors of career success and project effectiveness [39, 13,
36, 44]. Prior work suggests that while technical expertise
provides the baseline for employability, long-term profes-
sional success is heavily shaped by soft skills such as lead-
ership, collaboration, and communication [39, 42, 50]. In
highlyinterdisciplinarydomainslikeAI,thesecompetencies
become even more critical because the work is inherently
distributed[37,6,3].MLpractitionersmusttranslatemodel
outcomesintoactionableinsights,justifytrade-offstoprod-
uct teams, and collaborate with software and DevOps engi-
neers to ensure maintainability and robustness of deployed
pipelines[21].Asaresult,jobpostingsforML-relatedroles
∗Corresponding author
aidin.azamnouri@tum.de(A. Azamnouri)
ORCID(s):0009-0004-8409-2316(A. Azamnouri);0000-0001-5788-0991
(J. Bogner);0000-0002-5256-8429(S. Wagner)
increasinglyemphasizesoftskillsalongsidetechnicalquali-
fications[50].Despitethisdemand,theindustrycontinuesto
report a persistent soft-skills gap, particularly among early-
careerapplicants,raisingconcernsabouthowtechnicalpro-
fessionalsaretrained,evaluated,andhired[37,7,44].Atthe
same time, understanding soft skill expectations and work-
forcereadinessremainschallenging.Mostempiricalstudies
thatexaminesoftskillsinengineeringlabormarketsrelyon
job postings or survey instruments, which capture employer
intentratherthancandidateself-presentation[8,49,31,27].
Another major body of work focuses on resume mining and
automated skill extraction, yet these approaches often de-
pendondictionary-basedkeywordmatching[18,54,52,47].
Suchmethodsarebrittleandfailtocapturethenuancedand
variedwayscandidatesdescribesoftskillsinreal-worldCVs
(Curriculum Vitae).
Despite the centrality of soft skills to collaboration in
ML-enabled system development, most empirical evidence
to date has been drawn from job postings or surveys, which
reflect employer expectations rather than how candidates
themselves articulate these competencies. As a result, rel-
atively little is known about how ML engineers, data sci-
entists, and software engineers (three important roles for
buildingML-enabledsystems)actuallypresentsoftskillsin
theirCVs,howthispresentationvariesacrossroles,andhow
itevolveswithseniority.Understandingthecandidatesideof
thispicturemattersforseveralreasons.Forhiringmanagers
and recruiters, it reveals whether the soft skills demanded
in job postings are actually surfaced in applications, and
where screening pipelines built on keyword matching may
systematically miss competencies that candidates convey
A. Azamnouri et al.:Preprint submitted to ElsevierPage 1 of 28
arXiv:2608.10046v1  [cs.LG]  10 Aug 2026

Detecting Soft Skills in ML Engineering Roles CVs
through narrative rather than explicit labels. For practi-
tioners, particularly early-career ML and MLOps engineers
facing the well-documented soft skills gap, it provides con-
creteevidenceofhowexperiencedprofessionalsinthesame
rolecommunicatecollaboration,leadership,andmentoring,
offering a reference point for their own self-presentation.
For educators and curriculum designers, role-specific and
seniority-specific patterns indicate which competencies are
most visibly rewarded in practice and where training pro-
grams may need to place stronger emphasis. And for re-
searchers studying the socio-technical dimensions of ML
engineering, CV-side evidence complements the existing
job-postingliteraturebyshowingwhetherthecollaboration,
communication, and coordination needs identified in prior
work on ML-enabled system development are reflected in
how practitioners describe their own contributions.
Crucially,thedemand-sideliteraturedoesnotmerelyde-
scribeemployerpreferences;itadvancesexplanatoryclaims
aboutwhyparticularcompetenciesmatterforparticularroles
and career stages. Data scientists are described as occupy-
ing a translational position between analytical results and
business stakeholders [37, 6]; ML engineers as bridging
softwareengineeringanddatascienceteams[37,21];senior
roles as demanding strategic competencies that junior roles
do not [40]; and leadership as a universal rather than role-
specificexpectationinsoftwarework[14,34].Eachofthese
claims implies a testable prediction about what candidate-
authoreddocumentsshouldlooklike.Treatingthosepredic-
tionsashypothesesratherthanonlyasinterpretiveframingis
whatallowsacandidate-sidestudytocorroborateorcontra-
dict the demand-side account, rather than merely illustrate
it. We therefore state the predictions explicitly, test them
inferentially, and report which survive.
This paper addresses these gaps through an empirical
studyof300professionals’CVsspanningthethreeroles.To
enable analysis at scale, we develop a supporting generative
information-extraction pipeline based on a large language
model (LLM). Compared with traditional dictionary-based
or rule-based extraction methods, generative models are
bettersuitedtointerpretingthecontextualandoftenimplicit
ways in which soft skills are expressed in CVs [35, 20]. We
treat this pipeline as a methodological enabler rather than
the central contribution of the paper. It makes comparative
analysis tractable across 300 heterogeneous documents, but
the empirical findings on role and seniority differences are
ultimately what this work is about. In summary, this paper
makes the following contributions:
1.A confirmatory empirical analysis of soft skill ar-
ticulationacross ML engineers, data scientists, and
software engineers. We derive 13 falsifiable hypothe-
ses from the demand-side literature, covering role
signatures,seniorityprogression,anddisclosurestyle,
and test them with inferential statistics under family-
wise error control, reporting odds ratios, risk differ-
ences, and standardized effect sizes with 95% con-
fidence intervals. We complement this with false-
discovery-controlled exploratory contrasts across the
fulltaxonomy,andwithsensitivityanalysesthatquan-
tify how much extraction error would be required to
overturn each conclusion.
2.A reproducible curation methodologyincluding
role-specificfilteringrules,atri-partyannotationpro-
tocolforresolvingroleambiguity,duplicate-detection
procedures, and the search queries used to source
contemporary CVs from public web indexes. We
applythismethodologytoconstructabalancedcorpus
of 300 CVs by combining a previously established
multi-labeled CV corpus with a supplementary set of
contemporary CVs sourced from publicly accessible
sources.
3.A supporting LLM-based extraction pipelinethat
elicits both explicit and implicit soft skill mentions
fromunstructuredCVnarratives,validatediteratively
against a human-annotated ground truth. We include
this pipeline to make the analysis tractable and re-
producible at scale, not as a contribution to the skill-
extraction literature.
Our findings offer actionable guidance for practitioners
preparing CVs for ML-related roles, educators designing
professional development curricula, and researchers study-
ing workforce readiness in AI-intensive fields.
The remainder of this paper is structured as follows.
Section 2 reviews related work on soft skills in software
engineeringandautomatedCVanalysis.Section3describes
our research questions, hypotheses, dataset, LLM-based ex-
tractionmethodology,andstatisticalanalysisplan.Section4
presents the evaluation design of the extraction approach.
Section 5 reports results across role, seniority, and rhetor-
ical patterns, including the outcomes of all hypothesis tests
and the accompanying robustness analyses. Section 6 dis-
cusses the results and implications, while Section 7 de-
scribes threats to validity. Section 8 concludes and outlines
future research directions.
2. Related Work
A substantial body of research demonstrates that soft
skills are not peripheral but central to professional success
in software and AI-intensive environments [38, 42, 37, 32,
3]. Empirical analyses of job advertisements consistently
reveal that employers explicitly demand interpersonal and
behavioral competencies alongside technical expertise. For
instance, a large-scale study of software engineering job
advertisements in New Zealand found that more than four-
fifths of postings explicitly required soft skills, with com-
munication emerging as the most frequently cited require-
ment across company sizes and position types [14]. Be-
yond job advertisements, qualitative investigations provide
complementaryevidence.Throughin-depthinterviewswith
practicing software professionals, Malinen et al. [34] report
strong consensus regarding the importance of communi-
cation, teamwork, and leadership, while also highlighting
less visible yet critical competencies such as resilience and
self-awareness.Together,thesefindingsunderscorethatsoft
A. Azamnouri et al.:Preprint submitted to ElsevierPage 2 of 28

Detecting Soft Skills in ML Engineering Roles CVs
skills are not merely symbolic additions in job descriptions
but reflect genuine workplace expectations.
Skillrequirementsalsoevolvesubstantiallyacrosscareer
stages. Research examining AI professionals across junior
and senior levels shows a clear shift in emphasis. Early-
career roles prioritize foundational programming and ana-
lyticalcapabilities,whereasseniorrolesincreasinglyrequire
strategic competencies, including leadership, stakeholder
communication, and business-oriented thinking [40]. This
transitionsuggeststhatsoftskillsbecomeprogressivelycen-
tralasprofessionalsassumegreaterresponsibility,influence,
and cross-functional coordination. Importantly, hiring man-
ager perspectives further illuminate a discrepancy between
candidate preparation and employer expectations. An ex-
ploratory casestudy conductedwithin softwareengineering
recruitment contexts [30] found that hiring managers often
prioritizenon-technicalcompetenciesoverspecifictechnical
tools when evaluating entry-level applicants. Collectively,
these studies motivate the need for systematic, data-driven
analyses of how soft skills are actually articulated in CVs.
A separate line of work has developed computational
methods for identifying skills in unstructured recruitment
text. Early resume parsing frameworks relied on rule-based
pipelines and Named Entity Recognition [45], which han-
dled clearly delineated fields such as education and listed
skills but struggled with implicitly expressed competen-
cies.Ontology-basedsystems[41]andsyntax-awareextrac-
tors [48] extended this work by modeling semantic rela-
tionshipsandleveragingdependencystructure,respectively,
while the SkillSpan dataset [56] established Transformer-
based benchmarks for span-level hard and soft skill anno-
tation in job postings. More recent systems, such as Skill-
GPT[29],combineLLM-basedsummarizationwithembed-
dingsimilaritytomapskillsontostructuredtaxonomies.We
build on this lineage rather than adopt any of these systems
directly, because our study imposes a requirement that they
were not designed to meet, which is how a candidate dis-
closedsoftskills,explicitlyorimplicitly.Existingextractors
target the former and are not constructed to separate listed
competencies from narrated ones. We therefore implement
a generative extraction pipeline that elicits both forms and
ties each extracted skill to its supporting phrase, enabling
the explicit-versus-implicit distinction our analysis depends
on. The pipeline is a means to that analysis rather than a
contribution to skill extraction in its own right.
Taken together, prior work establishes that soft skills
matter,thatemployerdemandforthemiswell-documented,
and that increasingly capable tools exist to extract them
from text. What remains underexplored is the candidate
side of the picture. Three gaps are particularly salient. First,
existing empirical analyses of soft skills in technical la-
bor markets [8, 14, 34, 40, 30] draw almost exclusively
on job advertisements, survey instruments, or practitioner
interviews; none systematically examine how candidates
themselves articulate soft skills in their CVs. Second, the
comparative dimension is missing. While differences be-
tween junior and senior AI professionals have been studied
at the level of job-posting requirements [40], there is no
comparable evidence on how soft skill articulation varies
acrossMLengineers,datascientists,andsoftwareengineers,
or how it evolves with seniority, when observed directly
from candidate-authored documents. Third, and method-
ologically, the CV-mining literature is overwhelmingly de-
scriptive. Studies report frequency rankings of extracted
skillsbutrarelytestwhetherthedifferencesbetweengroups
exceed what sampling variation would produce, and rarely
reporteffectsizesthatwouldallowthepracticalimportance
ofadifferencetobejudged.Thispaperaddressesthesegaps
through a hypothesis-driven analysis of 300 CVs spanning
the three roles, examining role-specific emphasis, seniority-
basedprogression,andtherhetoricalpatternscandidatesuse
to present soft skills.
3. Methodology
This section presents the research design and technical
framework for examining how soft skills are mentioned in
professionalCVs.Toovercomethelimitationsoftraditional
keyword-based parsing approaches, this study adopts a gen-
erativeinformationextractionstrategythatleveragesLLMs’
semantic reasoning capabilities. In particular, models from
theGeminifamilyareemployedtointerpretunstructuredCV
narratives and identify behavioral competencies embedded
indescriptionsofprofessionalexperienceandachievements.
The methodological approach is supported by a hybrid data
collection strategy that combines a previously established
multi-labeled CV corpus with a supplementary dataset of
contemporary PDF CVs. This combination ensures both
methodologicalrobustnessandtemporalrelevance,enabling
the analysis to capture both established patterns and emerg-
ingtrendsinhowprofessionalspresentsoftskillsintechnical
CVs. The steps of the study process are depicted in Fig. 1.
To address the gap in the literature, this paper aims to
answer the following research questions:
RQ1:Whatsoftskillsaremostcommonlymentionedby
ML engineers, software engineers, and data scientists, and
howdoestheemphasisontheseskillsdifferacrossthethree
roles?
This question characterizes the overall landscape of soft
skill articulation in the dataset and identifies role-specific
patterns. Answering it reveals which behavioral competen-
ciesaremostvisibletorecruitersacrossML-relatedCVsand
highlights where each role places distinctive emphasis.
RQ2: How do soft skills mentions vary by seniority
level?
This question examines whether and how the articula-
tion of soft skills evolves as professionals advance in their
careers. Comparing junior and senior candidates reveals
whether CVs shift from emphasizing collaborative partici-
pation to leadership, coordination, and strategic competen-
cies as seniority increases.
RQ3: Do candidates present soft skills explicitly as
keywords in dedicated skills sections, or implicitly through
narrative descriptions of their professional experience?
A. Azamnouri et al.:Preprint submitted to ElsevierPage 3 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Figure 1:An overview of the study process
This question investigates the rhetorical patterns candi-
dates use to present soft skills, distinguishing between ex-
plicitmentions,inwhichskillsarelistedaskeywordsinded-
icated sections, and implicit mentions, in which behavioral
competencies are conveyed through narrative descriptions
of professional experience. The answer indicates whether
candidates rely primarily on keyword-based self-labeling or
storytelling-based disclosure, and how this balance varies
across roles and seniority levels.
3.1. Hypotheses
The three research questions above are stated as open
questions because no prior study has examined soft skill
articulation from the candidate side. Prior work on the de-
mandside,however,doeslicensespecificexpectationsabout
whatcandidate-sidedatashouldlooklikeifthemechanisms
proposedinthatliteratureoperateasdescribed.Wetherefore
translate each research question into a set of falsifiable
hypotheses, so that our analysis can confirm or disconfirm
those expectations rather than only describe frequencies.
Table1summarizesthehypotheses,theirgroundinginprior
work, and the statistical test used for each; their outcomes
are reported in Table 7.
We distinguish two classes of hypotheses.Confirmatory
hypotheses are derived from published findings that predate
our analysis; for these, we fix the comparison and the di-
rection in advance and control the family-wise error rate.
Exploratorycontrastsaretheremainingcomparisons,which
we report with false-discovery-rate control and interpret as
hypothesis-generating. We note explicitly that the hypothe-
ses were derived from the literature but were not preregis-
tered,andthatalltestsareperformedonasinglesample;the
confirmatory label therefore refers to derivation from prior
theory, not to preregistration. The distinction is nonetheless
consequential for interpretation. The confirmatory set fixes
13 comparisons in advance out of the several hundred that
A. Azamnouri et al.:Preprint submitted to ElsevierPage 4 of 28

Detecting Soft Skills in ML Engineering Roles CVs
the taxonomy would permit, so that the analysis can fail,
whereastheexploratorysetisexplicitlyframedasgenerating
claims for future studies to test.
Role signatures (RQ1).Studies of ML-enabled sys-
tem development describe data scientists as occupying a
translationalpositionbetweenanalyticalresultsandbusiness
stakeholders [37, 6], and communication is the single most
frequentlydemandedcompetencyinsoftwarejobadvertise-
ments [14]. If this translational burden is reflected in self-
presentation, it should be visible as a role difference in
communication.
•H 1a:Data scientists mention communication more
frequentlythanMLengineersandsoftwareengineers.
•H 1b:ML engineers mention mentoring more fre-
quently than data scientists and software engineers.
•H 1c:The proportion of CVs with no detectable soft
skills differs across roles.
•H 1d:Data scientists frame problem-solving as a be-
havioral competency more frequently than ML engi-
neers.
•H 1e:Leadership prevalence does not differ across the
three roles.
Because H1e predicts the absence of an effect, a non-
significantomnibustestwouldbeuninformativeonitsown.
Failure to reject the null is not evidence for it. We therefore
accompanytheomnibustestwithtwoone-sidedequivalence
tests (TOST) on each pairwise risk difference, using an
equivalence margin of±20 percentage points. The margin
is set to the smallest role difference we consider practically
meaningful for the applications this paper addresses. A
gap below 20 percentage points would not change how a
curriculum or a screening pipeline is designed for one role
versus another, whereas a gap above it would. H1e is treated
as supported only if the omnibus test is non-significant and
all pairwise contrasts are statistically equivalent within that
margin.
Seniority progression (RQ2).Prior analysis of junior
and senior AI job advertisements [40] reports that senior
roles demand strategic competencies (leadership, stake-
holder communication, business orientation) that junior
advertisements do not, while junior advertisements priori-
tize foundational technical skills. An exploratory study of
software engineering recruitment [30] reports that hiring
managers treat non-technical competencies as decisive at
the entry level even though candidates rarely surface them.
If these demand-side patterns have candidate-side counter-
parts, the following should hold.
•H 2a:Senior professionals mention leadership more
frequently than junior professionals.
•H 2b:Seniorprofessionalsmentioncoordinationmore
frequently than junior professionals.
•H 2c:Senior professionals mention strategic thinking
more frequently than junior professionals.
•H 2d:The proportion of CVs with no detectable soft
skills is lower among senior than among junior pro-
fessionals.
•H 2e:Two competing accounts make opposite predic-
tionsforcollaboration.Asubstitutionaccountpredicts
that collaboration is mentioned less often by senior
professionalsasleadershipdisplacesit.Anaccumula-
tionaccountpredictsthatseniorprofessionalsmention
collaboration at least as often as they do.
•H 2f:The seniority effect on leadership is not an arti-
fact of role composition.
Disclosure style (RQ3).A substantial share of CV
screening infrastructure matches keywords against prede-
fined skill vocabularies [18, 54], which presupposes that
candidates label competencies explicitly. Qualitative work
reports instead that soft skills are vaguely described and
inconsistently framed in candidate documents [34, 30].
•H 3a:Within the same CV, soft skills are disclosed
through narrative more often than through explicit
labels in a dedicated skills section.
•H 3b:Disclosurestyledependsonrole,withMLengi-
neers relying on narrative disclosure most heavily.
3.2. Data Collection
The foundational dataset for this study is the multi-
labeled CV corpus developed by Jiechieu and Tsopze [24],
whichispubliclyavailableonGitHubandhasbeenusedfor
benchmarking NLP tasks on professional documents. The
corpus provides three properties that are particularly valu-
able for the present work: (1) full-text CVs in plain.txtfor-
mat, which allow direct computational processing without
theneedforopticalcharacterrecognition;(2)expert-labeled
occupationtags,whichserveasaground-truthreferencefor
role-based analysis; and (3) a normalization file that maps
raw job titles to a smaller set of standardized professional
classes.
Although the corpus contains 19,465 CVs spanning a
broad range of occupations, its built-in normalization file
was found to be unsuitable for this study. In that file, the
expert curators collapsed both “ML Engineer” and “Data
Scientist” into a single broad “Software Developer” cate-
gory, which would make it impossible to distinguish the
three target roles of this work. The normalized file was
thereforediscardedinfavoroftherawarchive,inwhicheach
CV is stored as a three-field record separated by the “:::”
delimiter: a reference identifier, a semicolon-separated list
of raw occupation titles as written by domain experts, and
the full text of the CV. Working from the raw occupation
list rather than the normalized classes allowed us to design
a more granular filtering procedure tailored to the three
roles of interest. All filtering steps described below were
A. Azamnouri et al.:Preprint submitted to ElsevierPage 5 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Table 1
Confirmatory hypotheses, their grounding in prior work, and the statistical test applied to each.
ID Prediction Grounding Test
H1a Communication: data scientists>ML +
software engineers
[37, 6, 14] Fisher’s exact,2 × 2
H1b Mentoring:MLengineers>datascientists
+ software engineers
[37, 21] Fisher’s exact,2 × 2
H1c No-skill rate differs across roles [37] Pearson𝜒 2,3×2; planned contrast
H1d Problem solving: data scientists>ML
engineers
[37] Fisher’s exact,2 × 2
H1e Leadership: no difference across the three
roles
[14, 34] Pearson𝜒 2,3×2+pairwiseTOST
(±20 pp)
H2a Leadership: senior>junior (primary hy-
pothesis)
[40] Fisher’s exact,2 × 2
H2b Coordination: senior>junior [40] Fisher’s exact,2 × 2
H2c Strategic thinking: senior>junior [40] Fisher’s exact,2 × 2
H2d No-skill rate: senior<junior [30, 44] Fisher’s exact,2 × 2
H2e Collaboration: substitution vs. accumula-
tion (non-directional)
[40] Fisher’s exact,2 × 2
H2f Seniority effect on leadership survives ad-
justment for role and is homogeneous
across roles
[40] Logistic regression (LR test),
CMH, Breslow–Day
H3a Within a CV, narrative disclosure>key-
word disclosure
[18, 54, 34] Exact McNemar; Wilcoxon signed-
rank
H3b Disclosure style depends on role; ML en-
gineers most narrative-reliant
[30, 34] Pearson𝜒 2,3×4; planned contrast
implemented as case-insensitive queries, applied either to
the raw occupation list or to the full CV text, depending on
the step.
MLengineers.AfirstpassretrievedallCVswhosetext
matched the pattern “ML” or “machine learning”, yielding
204 candidates. Because the token “ML” is highly polyse-
mous in technical CVs, i.e., it frequently appears as a listed
toolorlibraryratherthanasajobtitle,asecondpassrequired
thestricterpattern“ML”(withatrailingwhitespace)sothat
matches would fire only when “ML” prefixed another word,
asin“MLEngineer”.Thisreducedthecandidatepoolto115
CVs.Eachofthesewasthensubjectedtoamanualheuristic
review designed to confirm that ML development was the
candidate’s primary occupation rather than a secondary ac-
tivity. The review consisted of a qualitative assessment of
three CV components:
1.Professionalsummaryorabstract.Candidateprofiles
were evaluated based on self-identification in their
introductory narrative. A CV was retained only if
the summary explicitly described the individual as
an “ML Engineer” or used a synonymous technical
title,e.g.,“MachineLearningEngineer”,“AI/MLEn-
gineer”, “MLOps Engineer”, “Deep Learning Engi-
neer”, or “Applied Machine Learning Engineer”.
2.Work experience.The professional history of each
candidate was examined to verify that their primary
or most recent roles involved the core development,
deployment, or maintenance of ML models. Candi-
dateswhoseexperiencesuggestedonlyincidentaluse
of ML tools within non-engineering roles, e.g., data
analystsapplyingpre-builtmodelsforreporting,were
excluded.
3.Technical skills.A distinction was drawn between
ML as a tool and ML as a core competency. This
involvedverifyingwhetherlistedtechnicalskills,such
as Scikit-learn or TensorFlow, were supported by ev-
idence of participation in the full ML lifecycle, in-
cluding feature engineering, model evaluation, and
MLOps practices, rather than appearing as a bare list
of library names.
Data scientists.A single-pass keyword filter for the job
title“DataScientist”identified105CVs.EachCVwasthen
manually reviewed using the same three-component proto-
col described above, with the retention criterion adapted to
thedatasciencerole.Thisreviewyielded94usableprofiles.
Software engineers.A broader initial filter for “Soft-
ware Developer” and “Software Engineer” returned 5,322
CVs, reflecting the size and heterogeneity of this role in
the corpus. To balance dataset size across roles and ensure
higherrelevance,thesearchwasnarrowedtocandidateswho
listed “Software Engineer” as their primary (first) occupa-
tion,reducingthesetto363CVs.Finally,topreventoverlap
with the ML and data-science subsets, any CV whose text
also matched the ML or data-science patterns above was
removed, leaving 357 CVs for the software engineering
subset.
Because the Jiechieu and Tsopze corpus was compiled
in 2020 [24], it does not reflect the most recent shifts in
howtechnicalprofessionalsdescribethemselvesinCVs.To
bridge this five-year gap and bring the dataset in line with
A. Azamnouri et al.:Preprint submitted to ElsevierPage 6 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Figure 2:An example of ML engineer/data scientist role ambiguity in a CV
current labor-market practices, a supplementary dataset of
contemporary CVs was manually curated.
For that, publicly hosted CVs were collected through
targeted Google queries using thefiletype:pdfoperator to
restrictresultstoPDFdocuments.Then,theyweremanually
checked to remove the sample ones. The specific queries
used were:
•ML CV filetype:pdf and Machine Learning CV file-
type:pdf
•data scientist CV filetype:pdf
•software engineer CV filetype:pdf
In contrast to the GitHub corpus, where role assign-
ment relied on expert-labeled occupation tags, supplemen-
tary CVs were selected based on the role explicitly stated
in the candidate’s document title or header. Documents
were retained only when (1) the file represented a genuine
individualCVratherthanatemplate,sample,orjobposting,
and (2) the role declared in the title or header matched one
of the three target roles. Some profiles remained ambiguous
after this initial pass, particularly at the boundary between
datascienceandMLengineering,andwereresolvedthrough
the classification procedure described below.
Thirteen CVs were identified in which candidates ex-
plicitly self-identified as belonging to both the data science
and ML engineering roles. This ambiguity is illustrated in
Fig. 2, which shows a professional summary in which a
candidate simultaneously describes themselves as a “Senior
Data Scientist and Machine Learning Engineer”. To assign
these CVs to a mutually exclusive role, a voting mechanism
wasemployedinvolvingtwohumanresearchersandanLLM
(Gemini 2.5 Pro) acting as a third annotator. Each annotator
independently classified the 13 disputed profiles, and the
final assignment was determined by majority vote.
The decision to include an LLM as a supplementary
annotator is motivated by a growing body of empirical evi-
dence [9]. Recent work in software engineering research [1,
51, 22] has shown that mixed human–LLM evaluation
designs can achieve inter-rater agreements comparable to
human-only settings, particularly when high-performance
models are used, which tend to reflect a majority opinion
distilled from their training corpora [1]. The use of a 2-to-1
majority voting rule for difficult cases similarly aligns with
established practice for subjective and nuanced annotation
tasks, where even professional raters frequently disagree.
Current guidance in the literature is that LLMs should
not yet fully replace human annotators in software engi-
neering studies, but can serve as effective supplementary
annotators that reduce human effort while maintaining data
reliability [1]. The tri-party design adopted here follows
the recommendation that the LLM never act as the sole
arbiter and that no case be decided by the LLM alone, as
each outcome requires agreement from at least one human
annotator.
To validate the classification procedure, the degree of
consensus among the three annotators was analyzed for
the 13 overlapping cases. In 9 of the 13 cases (69.2%),
all three annotators independently converged on the same
role, indicating professional narratives that, despite surface-
level ambiguity, were substantively aligned with a single
role. In the remaining 4 cases (30.8%), a 2-to-1 majority
was required; these CVs typically described hybrid profiles
withsignificanttechnicaloverlapbetweenthetworoles.The
LLM’s assignment aligned with the final majority decision
in 11 of 13 cases (84.6%), indicating strong agreement with
theaggregatedhumanconsensuswithoutdominatingit.The
two cases in which the LLM diverged from the final clas-
sification were both resolved by the two human annotators
agreeingagainsttheLLM,confirmingthathumanjudgment
remained the decisive factor.
To enable a fair comparative analysis across the three
roles, the dataset was balanced to include exactly 100 CVs
per role. The choice of 100 CVs per role reflects an upper
bound on what was practically feasible to curate at the
level of quality required for this study, while remaining
sufficient to support the comparative analyses; Section 3.6
reports the resulting sensitivity of the design in terms of
the smallest differences it can reliably detect. Three prac-
tical constraints shaped this decision. First, every CV in
the dataset was subject to manual review by the same two
human researchers who carried out the role disambigua-
tion procedure described above. As described in the role-
specificfilteringanddisambiguationstepsabove,thisreview
involved reading the professional summary, the most recent
work experience entries, and the listed competencies for
each candidate, both to confirm the primary occupation and
to verify narrative completeness. Scaling this human-in-
the-loop process beyond a few hundred CVs would have
compromised the consistency of role assignment, which is
a prerequisite for the comparative claims this paper makes.
Second, the supply of suitable contemporary CVs was itself
verylimited.Afterfilteringouttemplates,sampleCVspub-
lished by career-services websites, job postings, duplicates,
A. Azamnouri et al.:Preprint submitted to ElsevierPage 7 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Table 2
Final balanced dataset composition
Profession GitHub Corpus (2020) Manual (2025) Total Analyzed
ML Engineer 47 53 100
Data Scientist 62 38 100
Software Engineer 53 47 100
Total 162 138 300
non-English documents, and CVs whose declared role did
not unambiguously match one of the three target roles, the
pool of remaining publicly accessible CVs was effectively
saturated. We also made concerted efforts to solicit CVs
from the MLOps community by clearly communicating our
research objectives; however, no submissions were received
from communitymembers. Additional queries withbroader
keywords returned fewer new, high-quality candidates and
a higher proportion of already collected or out-of-scope
documents, indicating that the relevant public web cor-
pus had been substantially covered. Third, 100 CVs per
groupisconsistentwithsamplesizesusedinpriorempirical
studies of soft-skill articulation in technical labor-market
documents [25], thereby supporting comparability with the
existing literature.
FortheMLengineeringsubset,the47validatedprofiles
from the GitHub corpus were combined with 53 manually
collectedcontemporaryCVs,reachingthetargetof100.For
the data science and software engineering subsets, where
the corpus pool was substantially larger than required, a
purposeful manual selection was applied instead of random
sampling: 62 CVs were selected for data science and 53
for software engineering, based on text completeness. Text
completeness refers to CVs that contain the full set of
expected sections (summary, experience, skills, education).
Theseselectionswerethencombinedwiththecontemporary
supplementary set, which added 38 data science CVs and
47 software engineering CVs, bringing the total to 100 CVs
per role. The final balanced corpus comprises 300 CVs
and serves as the foundation for the comparative analyses
presented in the remainder of this paper.
To prevent accidental duplication between the corpus-
derived and contemporary subsets, each contemporary CV
collected via the queries was checked against the GitHub
corpus prior to inclusion. Specifically, for each candidate’s
CV,wecomputednormalizedtextoverlapagainstallcorpus
CVsofthesametargetroleusingatoken-levelJaccardsim-
ilarity and fuzzy matching over the professional summary
and the most recent two work experience entries; any can-
didate exceeding a similarity threshold of 0.5 was manually
inspected, and exact or near-exact matches were excluded.
No duplicates were identified through this procedure. The
final dataset composition is shown in Table 2.
All CVs analyzed in this study originate from publicly
accessible sources, and the analysis uses them solely for ag-
gregate, role-level statistical purposes; no individual candi-
dateisnamedoridentifiedinanyartifactreleasedalongside
this paper. The CVs themselves are not redistributed, both
because a subset of the contemporary documents include
explicitauthorstatementsagainstrepublicationandbecause
anonymizingpubliclyindexedCVswouldoffernomeaning-
ful privacy protection while leaving the originals traceable
through web search.
3.3. Soft Skill Extraction and Standardization
After constructing the balanced dataset, a structured
extractionpipelinewasimplementedtoconvertrawCVtext
into a standardized set of soft skill categories. The pipeline
relies on a generative information extraction approach in
which an LLM processes full CV narratives and identifies
behavioral competencies expressed within them. In contrast
to traditional NLP pipelines, no extensive preprocessing
techniquessuchaslemmatizationorstop-wordremovalwere
applied. This design choice was motivated by the observa-
tionthatmoderngenerativemodelsperformmoreeffectively
when provided with complete contextual sentences rather
than fragmented tokens [55]. For CVs originally stored
in PDF format, the PyMuPDF (fitz)1 library was used to
extractrawtextualcontent.Thispopularlibrarywasselected
because it preserves the reading order of textual blocks,
allowing the model to correctly interpret relationships be-
tweensectionssuchasjobtitles,roledescriptions,andlisted
competencies.
Soft skill identification was performed using models
fromtheGeminifamily.EachCVwasprovidedtothemodel
as a complete text document accompanied by a structured
prompt2 instructing the model to identify and extract soft
skills present in the candidate’s professional narrative. The
model’s task was to detect both explicit skill mentions and
implicit behavioral competencies and map them to a pre-
defined taxonomy of soft skills, TaxoSoft [25]. This taxon-
omy was developed to address the terminology gap com-
monly observed in professional documents, where equiva-
lentcompetenciesaredescribedusingvariedlanguage,e.g.,
“Collaboration” versus “Teamwork”. TaxoSoft constructs a
structuredrepresentationofsoftskillsbycombiningknowl-
edge graph resources such as DBpedia3 with distributional
semanticsderivedfromWord2Vec 4.Theresultingtaxonomy
definesrelationshipsbetweenskillsusinghierarchicalstruc-
tures derived from social network analysis, where central
skills act as parent nodes and related competencies are
represented as subordinate nodes, e.g., “Communication” is
aparentto“ActiveListening”and“VerbalCommunication”.
1https://pymupdf.readthedocs.io/en/latest/
2can be found inhttps://doi.org/10.5281/zenodo.21873447
3https://www.dbpedia.org/
4https://code.google.com/archive/p/word2vec/
A. Azamnouri et al.:Preprint submitted to ElsevierPage 8 of 28

Detecting Soft Skills in ML Engineering Roles CVs
This extraction strategy follows the generative information
extraction paradigm, which represents a shift away from
traditionalsequencelabelingmethods[55].Inthisparadigm,
LLMs directly generate structured information from un-
structured input, enabling more flexible and context-aware
extraction in real-world textual environments where rigid
patterns are insufficient.
Several factors motivated the use of LLM-based extrac-
tion for this task. First, generative models support zero-
shot and few-shot generalization, allowing them to perform
complex information extraction tasks using only natural
language instructions and minimal examples. This capabil-
ity reduces the dependence on large task-specific labeled
datasets, which are often unavailable for CV analysis. Sec-
ond, LLMs can simultaneously address multiple extrac-
tion subtasks, such as identifying entities and interpret-
ing contextual relationships, within a single unified frame-
work [12]. This capability is particularly valuable in CV
parsing, which is an extreme multi-label problem in which
numerous overlapping competencies may appear within a
single document. Furthermore, unlike rule-based systems
that rely on rigid pattern matching, LLMs leverage seman-
tic knowledge acquired during pretraining, enabling them
to distinguish between a skill listed as a keyword and a
competency demonstrated through professional experience.
Finally, LLM-based extraction offers significant scalability
advantages compared with manual annotation processes,
which are time-consuming and costly when applied to large
text corpora.
To facilitate downstream analysis, the LLM was in-
structed to return extraction results in a structured JSON
format. The schema required the model to produce a list of
skill objects containing two fields: a standardized skill label
derivedfromthetaxonomyandtheexactphrasefromtheCV
thatsignaledthepresenceofthecorrespondingcompetency
(see listing 1). Including the original textual phrase along-
side the normalized skill label improves interpretability and
enables verification of the model’s reasoning. This design
allows us to confirm whether an identified skill is gen-
uinely supported by textual evidence rather than resulting
from model hallucination. Moreover, comparing extracted
phrases with their assigned categories provided valuable
feedback during iterative prompt refinement, thereby im-
provingextractionaccuracy.Tomaintainconsistencyacross
the dataset, an additional verification step by the first and
secondauthorensuredthatallextractedcompetenciescorre-
sponded to entries within the selected taxonomy. When the
model produced alternative linguistic variants, these were
automatically mapped to their canonical taxonomy labels,
therebystandardizingtherepresentationofsoftskillsacross
all CVs in the dataset.
[
{
"skill": "Collaboration",
"phrase": "Collaborated with cross-functional teams"
},
{
"skill": "Communication",
"phrase": "Maintained positive communication with product
owners"
}
]
Listing 1: An example of structured json output format for
skill extraction
3.4. Seniority Level Elicitation
To analyze how soft skill articulation evolves across
career stages, each CV in the dataset was assigned a senior-
ity label. Industry hiring standards for advanced technical
roles, particularly in data science and ML, often require
approximately 5 years of relevant professional experience
before candidates are considered for senior-level responsi-
bilities [23, 15, 28, 43]. These positions typically involve
technical execution, project coordination, mentoring, stake-
holder interaction, and competencies that are rarely devel-
oped within less than a five-year timeframe. Consequently,
to better reflect industry practice and improve statistical
balance,thisstudyadoptsafive-yearthresholdtodetermine
seniority. Under this framework, professionals with fewer
than five years of relevant experience are categorized as
junior, whereas those with five or more years are classified
as senior. Although professional job titles vary across or-
ganizations, e.g., associate, lead, or principal, this binary
classification provides a consistent analytical baseline for
examining changes in soft skill expression across career
progression. Because dichotomizing a continuous variable
discards information and can distort effect estimates, we
additionally retain the underlying estimate of total years of
experience and use it in a robustness analysis (Section 5.5).
To accomplish this, an automated extraction procedure
was implemented using the Gemini 3 Pro Preview model.
The model was instructed to determine a candidate’s expe-
rience level through two complementary strategies. First, it
attempteddirectextractionbyidentifyingexplicitstatements
indicating total years of professional experience within sec-
tionssuchastheprofessionalsummaryorprofile.Whensuch
informationwasunavailable,themodelappliedacalculated
summation approach, identifying employment start and end
dates for each listed position and computing the cumulative
duration of the candidate’s professional experience. This
approach grounds the seniority classification in the chrono-
logical timeline of the CV rather than relying on potentially
ambiguous titles.
To maintain temporal accuracy when calculating expe-
rience durations, the extraction pipeline incorporated fixed
reference dates corresponding to the time at which each
dataset was collected. This step was particularly necessary
forrolesmarkedas“Present”wheretheenddateofemploy-
ment is unspecified. For CVs originating from the GitHub
corpus, which was collected on June 20, 2020, ongoing
A. Azamnouri et al.:Preprint submitted to ElsevierPage 9 of 28

Detecting Soft Skills in ML Engineering Roles CVs
positionswerecalculatedrelativetothisdate.Forthesupple-
mentaryCVsgatheredthroughtargetedwebsearches,aref-
erencedateofDecember1,2025wasusedasanapproxima-
tionofthedatacollectionperiod.Bycombiningexperience-
basedinferencewithexplicittemporalanchors,themethod-
ologyensuresaconsistentandreproducibleclassificationof
junior and senior professionals across the dataset.
3.5. Soft Skill Presentation Styles
InadditiontoidentifyingwhichsoftskillsappearinCVs,
thisstudyalsoexamineshowcandidatespresenttheseskills.
Specifically, the methodology distinguishes between skills
explicitly listed as keywords and those implicitly conveyed
through narrative descriptions of professional experience.
To enable this analysis, a two-stage extraction strategy was
implemented to separate structurally declared competencies
from those inferred through contextual storytelling.
First, a constrained section extraction procedure was
applied to isolate skills that candidates explicitly highlight.
Using the Gemini 3 Pro Preview model, the extraction
promptwasrestrictedtospecificCVsegmentstypicallyded-
icated to competency summaries. The model was instructed
to identify soft skills only within sections labeled Skills,
Technical Competencies, or Core Strengths. At the same
time, the model was explicitly prevented from extracting
information from other narrative sections such as Work
Experience, Professional History, Projects, or Education.
This restriction ensures that the extracted skills represent
deliberateself-labelingbythecandidate,typicallyexpressed
as keywords or bullet-point lists.
The second stage focuses on implicit skill identifica-
tion. During the initial extraction phase of the pipeline,
the model processed the full CV text and extracted all
identifiablesoftskills,includingthoseembeddedwithinde-
scriptionsoftasks,achievements,andresponsibilities.These
comprehensive results constitute the total set of detected
skills. To distinguish narrative-based skills from explicitly
declaredones,adeductivecomparisonwasappliedbetween
the two extraction outputs. Skills obtained from the con-
strainedskills-sectionextractionwerecategorizedasexplicit
mentions (𝐸), while the complete set extracted from the
entire document was defined as total mentions (𝑇). The set
ofimplicitmentions(𝐼)wasthenderivedbysubtractingex-
plicitmentionsfromthetotalset(𝐼=𝑇−𝐸).Thisanalytical
procedure enables the quantification of different soft skill
disclosure styles within professional CVs. For example, if
acompetency,suchasleadership,appearsindescriptionsof
projectcoordinationorteammanagementbutisabsentfrom
the candidate’s skills section, it is classified as an implicit
mention.Suchcasesindicatethatthecandidatedemonstrates
the skill through professional narratives rather than directly
labelingit.Byseparatingthesetwoformsofexpression,the
methodologyallows forasystematic analysisofthebalance
between keyword-based self-presentation and storytelling-
based skill communication across roles and seniority levels.
Because𝐸and𝐼are disjoint by construction and jointly
exhaust𝑇, the two disclosure channels can be compared
within the same CV as a paired observation, which is what
H3a requires.
3.6. Statistical Analysis
Thissubsectionspecifiestheanalysisplanappliedtothe
extracted data. All analyses are conducted at the level of the
individual CV. For each CV and each taxonomy label, we
record a binary indicator of whether that competency was
detected, so that a candidate who describes collaboration in
four separate bullet points contributes one positive observa-
tion rather than four. This de-duplication makes the unit of
analysis the candidate rather than the sentence, which is the
appropriatelevelforclaimsabouthowprofessionalspresent
themselves. It yields 1,354 unique skill–CV pairs from the
1,367rawmentionsextractedbythepipeline;ofthesepairs,
347 are disclosed as keywords in a dedicated skills section
and 1,007 through narrative. Frequencies reported as per-
centages throughout Section 5 are therefore the proportion
of CVs in a group in which a competency was detected at
least once, not counts of mentions.
Tests.For2 × 2comparisons of a binary outcome
betweentwoindependentgroups,weuseFisher’sexacttest,
which remains valid for the sparse cells that arise for lower-
frequency competencies, for example, strategic thinking ap-
pearsinonly6juniorCVs.Foromnibuscomparisonsacross
the three roles, and for the3 × 4comparison of disclosure
style by role, we use Pearson’s𝜒2 test without continuity
correction;expectedcellcountswereverifiedtobeadequate
(≥3.3in the sparsest cell of the disclosure-style table, and
≥8elsewhere). H 3a compares two measurements made on
thesameCVandisthereforetestedwiththeexactMcNemar
test on the discordant pairs, complemented by a Wilcoxon
signed-rank test on the per-CV counts of implicitly versus
explicitlydisclosedcompetencies.H 2f istestedwithlogistic
regression. We compare nested models by likelihood-ratio
test to assess the seniority effect adjusted for role, and
the seniority×role interaction to assess homogeneity. As
a non-parametric check on the same question, we report
the Cochran–Mantel–Haenszel (CMH) common odds ratio
stratified by role, together with the Breslow–Day test of
homogeneity of odds ratios across strata. Differences in the
number of competencies per CV are tested with Kruskal–
Wallis (role) and Mann–Whitney𝑈(seniority), since these
counts are right-skewed and zero-inflated. All tests are two-
sided,includingthoseattachedtodirectionalhypotheses,so
thataresultinthedirectionoppositetothepredictioncanbe
detected rather than absorbed into a non-significant tail.
Effect sizes.Reporting significance without magnitude
wouldleavethepracticalquestionunanswered,soeverytest
is accompanied by an effect size with a 95% confidence in-
terval.For2 × 2tables,wereporttheconditionalmaximum-
likelihood odds ratio with its exact confidence interval,
the risk difference in percentage points with a Newcombe
hybrid-score interval, and Cohen’sℎ. For omnibus𝜒2 tests,
we report Cramér’s𝑉. For the rank-based tests, we report
therank-biserialcorrelationand𝜖 2.Proportionsreportedon
their own carry Wilson score intervals.
A. Azamnouri et al.:Preprint submitted to ElsevierPage 10 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Multiplicity.The13confirmatoryhypothesesinTable1
form a single family, and we control the family-wise error
rate across them at𝛼= 0.05using the Holm–Bonferroni
procedure.Whereahypothesisincludesaplannedfollow-up
contrast (H1c, H1e, H3b), the contrast is corrected separately
within its own small family. The exploratory analyses test
every competency detected in at least 15 CVs (24 labels)
against role and against seniority; these form two further
families, each controlled at a 5% false discovery rate using
theBenjamini–Hochbergprocedure.Wereportbothrawand
adjusted𝑝-values throughout, and we do not describe an
exploratoryresultasafindingunlessitsurvivesadjustment.
Sensitivity of the design.The sample size was fixed by
curationconstraintsratherthanbyapowercalculation,sowe
report the resulting sensitivity rather than a post-hoc power
estimate. At𝛼= 0.05and 80% power, against a baseline
prevalence of 30%, the design can detect a difference of
19.2 percentage points between two roles (100 vs. 100),
16.6 points between one role and the other two combined
(100 vs. 200), and 16.1 points between senior and junior
professionals (186 vs. 114). Differences smaller than these
are not reliably resolvable in this corpus, which is why we
report confidence intervals for every contrast and why H1e
is evaluated by equivalence testing rather than by a non-
significant𝑝-value.
Robustness.Three sensitivity analyses accompany the
confirmatory results and are reported in Section 5.5. First,
because the seniority variable is a dichotomization, we re-
estimate the primary hypothesis using the underlying con-
tinuous estimate of years of experience. Second, because
longer CVs offer more opportunities for a competency to be
detected, we re-estimate the primary hypothesis, adjusting
for document length. Third, and most importantly, because
the outcome variable is produced by an imperfect extractor,
we conduct a quantitative bias analysis that propagates the
pipeline’s measured sensitivity and specificity through the
estimates,andwecomputehowlargeadifferentialextraction
error between groups would have to be before each conclu-
sion reverses.
4. Validation of the Extraction Pipeline
This section describes the evaluation framework used to
assess the effectiveness of the proposed soft skill extraction
approach.BecausetheempiricalclaimsinSection5areonly
as reliable as the extraction that produces them, this section
validates the pipeline against a human-annotated ground
truth before applying it to the full corpus. The measured
precision and recall reported here are not only a quality
statement about the pipeline; they are inputs to the quanti-
tative bias analysis in Section 5.5, which propagates them
through every confirmatory estimate. The evaluation relies
onstandardinformationextractionmetrics,precision,recall,
and F1-score, to measure the accuracy and completeness of
theextractedskills[16].Thesemetricsarewidelyadoptedin
informationextractionandskillminingresearchandprovide
abalancedassessmentofsystemperformance[19,25,26,2].
In this study, the F1-score serves as the primary evaluation
metric because it simultaneously penalizes false positives
(hallucinated skills not present in the text) and false nega-
tives(skillspresentintheCVbutnotdetectedbythemodel).
Consequently, it provides a balanced measure of both preci-
sion, the proportion of correctly extracted skills, and recall,
theproportionofrelevantskillssuccessfullyidentified.This
evaluation framework enables direct comparison with prior
research in skill extraction and information extraction sys-
tems.
To ensure rigorous assessment, the development of the
extraction pipeline followed an iterative refinement process
rather than a single implementation step. The system was
progressivelyimprovedthrough22experimentaltrialsorga-
nizedintofourdevelopmentalphases,trackingthetransition
from an initial baseline configuration to a highly optimized
prompt-based extraction system. This iterative design was
necessary due to the non-deterministic behavior of genera-
tive AI models and the linguistic complexity of CVs, which
frequentlycontainambiguousphrasing,technicalnoise,and
varied terminology for similar competencies. Each iteration
focused on refining the prompt structure, improving tax-
onomy alignment, and introducing additional constraints to
reduce hallucinations while preserving high recall.
In addition, a human-validated ground truth dataset was
constructed to provide a reliable benchmark for evaluating
each experimental iteration. This dataset consists of a ran-
domly selected sample of 100 CVs drawn from the original
corpus. The size of this evaluation subset aligns with prior
research on skill extraction systems [25], ensuring method-
ological comparability. During the annotation process, each
CVwasmanuallyreviewedbyhumanannotatorswhoidenti-
fiedsoftskillsbasedexclusivelyonthelabelsandalternative
labels defined in the adopted TaxoSoft taxonomy [25]. For
every identified skill, the annotators also recorded the exact
phrase in the CV that signaled the presence of that compe-
tency. These phrase–skill pairs served as the gold standard
for evaluating the extraction results generated by the LLM.
During the annotation process, each of the 100 CVs was
independently reviewed by the first and second authors,
who carried out the role disambiguation procedure. Both
annotatorsworkedfromthesameinstructionsandidentified
soft skills based exclusively on the labels and alternative
labels defined in the adopted TaxoSoft taxonomy [25].
Given the exploratory and interpretive nature of the
annotation task, we did not compute a formal inter-coder
reliability statistic. Instead, reliability was ensured through
repeatedjointcalibrationandconsensus-basedresolutionof
disagreements, which are widely used strategies in qualita-
tive research to ensure analytical rigor [17, 46]. Conflicts
between the two annotators fell into three categories, each
handledbyanexplicitrule:(1)casesinwhichoneannotator
identified a skill that the other had not noted were resolved
through joint re-examination of the CV, with the skill re-
tained only if both annotators agreed that the supporting
phrase met the taxonomy’s criteria; (2) cases in which both
annotators identified the same skill but cited different sup-
portingphraseswereresolvedbyretainingthephrasejudged
A. Azamnouri et al.:Preprint submitted to ElsevierPage 11 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Table 3
Evolution of extraction performance across all refinement phases. F1 is the harmonic mean of the precision and recall values
computed before rounding.
Phase / Milestone Precision Recall F1-score Key Refinements / Models
Baseline (Trial 1) 0.32 0.60 0.41 Flash-Lite (v2.5); initial taxonomy sample
Scaling (Trial 6) 0.31 0.84 0.45 Gemini 2.5 Flash; architecture upgrade
Constrained (Trial 8) 0.35 0.82 0.49 Gemini 2.5 Flash; negative examples; variant pruning
Optimized (Trial 12) 0.63 0.80 0.70 Gemini 2.5 Pro; explicit grounding rules; final refinement
Peak Performance (Trial 13) 0.69 0.74 0.72 Gemini 3 Pro Preview
Table 4
Comparative Benchmarking of Soft Skill Extraction Performance
Study/Methodology Data Source Approach F1-score
This Study (Optimized Gemini) CVs Generative Information Extraction 0.72
Akkasi [2] Job Ads Transformer Ensemble 0.67
TaxoSoft [25] Job Ads Hybrid Dictionary 0.84
Knowledge Base (Baseline) [33] Job Ads Wikipedia/DBpedia 0.54
ESCO Taxonomy (Baseline) [11] Job Ads Manual/Keyword 0.17
to most directly express the competency, with ties broken
by selecting the earlier occurrence in the CV; and (3) cases
in which the two annotators assigned different taxonomy
labels to the same phrase were resolved through discussion,
referring back to the TaxoSoft alternative-label definitions
todeterminethecanonicalcategory.Thereconciledphrase–
skill pairs served as the gold standard for evaluating the
extraction results generated by the LLM.
Following each experimental trial, the system’s JSON
output was automatically compared with the ground truth
dataset. Precision, recall, and F1-score were calculated by
comparing the extracted skill–phrase pairs with the anno-
tated reference set. Any discrepancies were carefully ana-
lyzed to identify the underlying causes of false positives
and false negatives. These analyses informed subsequent
prompt adjustments, such as introducing stronger extraction
constraints, refining taxonomy variants, and incorporating
negative examples to prevent misclassifying technical tasks
asbehavioralcompetencies.Thisfeedbackloopensuredthat
each prompt revision resulted in measurable improvements
in extraction accuracy.
The refinement process progressed through four major
phases. The progression of performance metrics across
these phases is summarized in Table 3. The first phase
established the baseline configuration and integrated the
TaxoSoft taxonomy into the prompt structure. Early exper-
iments relied on simple natural language instructions and
partial taxonomy samples, which resulted in relatively low
performance. Subsequent trials introduced few-shot exam-
ples and expanded the taxonomy coverage, improving the
model’s ability to recognize skill–phrase relationships. The
secondphasefocusedonconstraintengineering,introducing
explicit exclusion rules and negative examples to reduce
hallucinated extractions from technical descriptions. The
thirdphaseinvolvedmodelscalingandpromptoptimization,
transitioning to larger Gemini architectures and applying
automated prompt optimization techniques to improve ex-
tractionconsistency.Thefinalphaseconductedcross-model
benchmarking, evaluating a variety of large-scale open-
source and proprietary language models, e.g., openai-gpt-
oss-120b, deepseek-r1-0528, and llama-3.1-sauerkrautlm-
70b-instruct, using the optimized prompt configuration.
Despitetestingseveralhigh-capacityarchitectures,thetuned
Gemini 3 Pro Preview configuration achieved the highest
performance, reaching a precision of 0.69, a recall of 0.74,
and an F1-score of 0.72.
The selection of comparison models was guided by
three considerations. First, all benchmarked models were
available through the institutional API infrastructure used
in this study, which provided consistent access conditions
and reproducible inference settings across configurations.
Second, the comparison set was deliberately weighted to-
ward open-weight models, which together cover the largest
publicly inspectable architectures available at the time of
the study and align with the recommendation of Baltes et
al. [5] to include open LLM baselines in empirical software
engineering studies. Third, the comparison was designed
to test whether the optimized prompt generalized across
model families rather than to benchmark every available
frontier proprietary model. Models such as OpenAI’s GPT-
5 and Anthropic’s Claude Opus 4 were not included in this
comparison because they were not part of the institutional
API access available during the study period; we view their
evaluationasanaturaldirectionforfuturework,particularly
as their pricing and access conditions evolve.
Finally, to confirm that extraction quality is adequate
for the comparative analysis that follows, we situate the
pipeline’s performance relative to prior soft skill extraction
approaches (Table 4). Notably, the proposed generative in-
formation extraction approach achieves higher performance
than several traditional baselines while effectively address-
ingtheterminologygapinherentinunstructuredCVs.While
the TaxoSoft framework [25] reported a higher F1-score,
A. Azamnouri et al.:Preprint submitted to ElsevierPage 12 of 28

Detecting Soft Skills in ML Engineering Roles CVs
several methodological differences explain this gap. First,
the TaxoSoft system employed a hybrid methodology com-
bining DBpedia and Word2Vec to build a comprehensive
dictionaryofexact-matchtermsandmorphologicalvariants
foreachskillcategory.Second,theTaxoSoftevaluationwas
conducted on job advertisements, where recruiters typically
usestandardizedprofessionalkeywordstoimprovesearcha-
bilityandvisibility.Incontrast,CVscontainfarmorediverse
and personalized language, making skill identification con-
siderablymorechallenging.AshighlightedbyXuetal.[55],
generative information extraction from highly unstructured
documents introduces additional complexity due to var-
ied formatting and narrative expression. Also, the current
methodology emphasized rigorous evaluation by relying on
explicit textual grounding, deliberately limiting skill extrac-
tion to those directly supported by phrases to reduce the
hallucination issues commonly seen in LLMs. As a result,
althoughthefinalF1-scoreisslightlylowerthandictionary-
based systems evaluated on structured job advertisements,
the proposed approach provides a more realistic and robust
solution for extracting soft skills from heterogeneous CV
narratives. These findings validate the effectiveness of the
proposedLLM-basedpipelineandjustifytheuseofthefinal
optimized configuration for the subsequent analysis of the
full CV dataset.
5. Results
This section presents the results obtained from applying
the optimized soft skill extraction pipeline to the balanced
datasetof300professionalCVs.Theanalysisreliesonthefi-
nalconfigurationoftheGemini3ProPreviewmodel,which
demonstrated the highest performance during the iterative
evaluation process described in the previous section. Each
RQ subsection first characterizes the descriptive pattern
and then reports the confirmatory tests associated with it;
Section 5.4 consolidates all hypothesis outcomes and the
exploratorycontrasts,andSection5.5reportstherobustness
analyses.
5.1. Soft Skills Across Roles (RQ1)
Beforeexaminingwhichspecificcompetenciesaremost
prevalent, we first characterize the overall density of soft
skill articulation in the dataset. Across the 300 CVs, the
optimizedextractionpipelineidentified1,367softskillmen-
tionsintotal,correspondingto1,354uniqueskill–CVpairs,
an average of approximately 4.5 distinct competencies per
CV across the full corpus, or 5.2 when restricting to the
262 CVs (87.3%, 95% CI [83.1, 90.6]) that contain at least
one detectable soft skill. The remaining 38 CVs (12.7%
[9.4, 16.9]) contained no extractable soft skills at all; this
no-skill group is concentrated in two roles, ML engineers
(18.0%)andsoftwareengineers(16.0%),withdatascientists
exhibiting only 4.0% no-skill CVs.
The density of soft skill articulation differs notably
across the three roles, and the difference is larger than
sampling variation would produce. Data scientist CVs are
the densest, with a mean of 5.74 distinct competencies per
CV (𝑆𝐷= 3.79), followed by software engineers (𝑀=
4.07,𝑆𝐷= 3.11) and ML engineers (𝑀= 3.73,𝑆𝐷=
3.15); a Kruskal–Wallis test on the per-CV counts rejects
equality across roles,𝐻(2) = 17.39,𝑝<0.001,𝜖 2 = 0.058.
Data scientist CVs also have the longest right tail of skill
mentions and the lowest no-skill rate. ML engineering CVs
are the sparsest in soft skill content, both because of their
high no-skill rate and because the most frequent soft skills
among ML engineers (collaboration at 50%, leadership at
42%) appear at lower rates than the corresponding figures
fordatascientists(collaboration68%,communication54%).
The two plausible interpretations of this pattern are that
the conservative extraction pipeline requires explicit textual
evidence for each skill and that ML engineers more often
foregroundtechnicaltoolsandframeworksattheexpenseof
behavioralnarrative;Section5.5showsthatthefirstofthese
cannot account for the observed differences.
To address RQ1, the extracted skills were aggregated
acrosstheentirecorpusof300CVs.Theresultingfrequency
distribution highlights the most prevalent behavioral com-
petencies reported by professionals in the dataset, as shown
in Fig. 3. Collaboration is the most commonly reported soft
skill, appearing in 61.3% of the analyzed CVs (184/300,
95%CI[55.7,66.7]).Thisfindingsuggeststhatcollaborative
capabilities remain a central expectation within modern AI
andsoftwaredevelopmentenvironments,whereprojectsare
typically conducted in multidisciplinary teams. The second
most frequent skill is leadership, which appears in 38.3% of
CVs (115/300, [33.0, 43.9]), followed by communication,
reported in 34.3% of the documents (103/300, [29.2, 39.9]).
Although the most frequently reported skills appear
across all roles, the comparative analysis reveals several
role-specific variations in the prominence of secondary
competencies. These differences, which are depicted in
Fig. 4, reflect the distinct responsibilities and collaborative
contexts associated with each profession, and four of them
were predicted in advance.
H1a (communication).Communicationisreportedsub-
stantially more often in data science CVs, appearing in
54.0% of profiles, against 18.0% of ML engineering and
31.0% of software engineering CVs. Pooling the two com-
parison roles, the contrast is 54.0% versus 24.5%, a risk dif-
ferenceof+29.5percentagepoints(95%CI[+17.8,+40.4]),
OR (odds ratio)= 3.60([2.11, 6.21]), Cohen’sℎ= 0.62,
Fisher’s exact𝑝 <0.001(Holm-adjusted𝑝 <0.001). H 1a
is supported, and the effect is the largest role difference
we observe. It survives adjustment for seniority (adjusted
OR2.59[1.45, 4.64] relative to software engineers,𝑝=
0.001),whileMLengineersfallsignificantlybelowsoftware
engineers on the same outcome (adjusted OR0.51[0.26,
0.99],𝑝= 0.047).
H1b (mentoring).Mentoring is emphasized more fre-
quently in ML engineering profiles, where it appears in
28.0% of CVs, compared with 18.0% for data scientists and
13.0% for software engineers. Against the pooled compar-
ison group the contrast is 28.0% versus 15.5%, a risk dif-
ference of+12.5points ([+2.8,+22.9]), OR= 2.11([1.13,
A. Azamnouri et al.:Preprint submitted to ElsevierPage 13 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Collaboration
Leadership
CommunicationProblem solving
PresentationCoordination
Mentoring
Time management
Creativity
Self-organized
Soft Skill
0
25
50
75
100
125
150
175Frequency
184
115
103
84 80 77
59
45 40 39
Figure 3:Top 10 soft skills mentioned across all roles
Collaboration
Leadership
CommunicationProblem solving
PresentationCoordination
Mentoring
Time management
Creativity
Self-organized
Coaching Writing Passion Initiative Speaking
Soft Skill
0
10
20
30
40
50
60
70Frequency
68
47
54
34
40
30
18
10
21 21
11 13
16
9
3
50
42
18
15
30
22
28
6
10
6
16 14
9 7
14
66
26
31
35
10
25
13
29
9
12
6
2 4
11
1
Role
Data Scientist
ML Engineer
Software Engineer
Figure 4:The number of soft skills mentioned by each role
3.94]),ℎ= 0.31,𝑝= 0.013(Holm-adjusted𝑝= 0.029).H 1b
is supported, though with a considerably smaller effect than
H1a, and the confidence interval admits differences as small
as three percentage points.
H1c (no-skill rate).The distribution of CVs without
identifiable soft skills varies across the three roles: 18 ML
engineering CVs (18.0%), 16 software engineering CVs
(16.0%), and only 4 data science CVs (4.0%). The omnibus
test rejects homogeneity,𝜒2(2) = 10.37,𝑝= 0.006(Holm-
adjusted𝑝= 0.029), Cramér’s𝑉= 0.19. The planned
contrast confirms the predicted direction: data scientists are
far less likely than the other two roles combined to produce
aCVwithnodetectablebehavioralcontent(4.0%vs.17.0%,
OR= 0.20[0.05,0.60],riskdifference−13.0points[−19.3,
−5.6],𝑝 <0.001). H 1c is supported. The effect persists
when seniority is held constant (adjusted OR0.22[0.07,
0.69],𝑝= 0.010), whereas ML engineers are statistically
indistinguishable from software engineers once seniority
is controlled (adjusted OR1.03[0.48, 2.20],𝑝= 0.94),
indicating that the apparent ML–software difference in the
rawratesisattributabletothelargerjuniorshareamongML
engineers rather than to the role itself.
H1d (problem solving).In the dataset, 34.0% of data
science CVs describe problem solving as a behavioral com-
petency, whereas the skill appears in only 15.0% of ML
engineering CVs: a risk difference of+19.0points ([+7.1,
+30.3]), OR= 2.90([1.40, 6.25]),ℎ= 0.45,𝑝= 0.003
(Holm-adjusted𝑝= 0.020).H 1d issupported.Thisdisparity
suggeststhatdatascientistsaremorelikelytopresentanalyt-
ical reasoning and experimentation as behavioral strengths,
A. Azamnouri et al.:Preprint submitted to ElsevierPage 14 of 28

Detecting Soft Skills in ML Engineering Roles CVs
emphasizing their ability to approach complex data chal-
lenges through structured problem-solving processes.
H1e (leadership: predicted invariance) is refuted.We
had predicted, following job-advertisement and interview
studies that treat leadership as a universal expectation [14,
34],thatleadershipprevalencewouldnotdifferacrossroles.
It does. Leadership appears in 47.0% of data science CVs,
42.0% of ML engineering CVs, and 26.0% of software
engineering CVs; the omnibus test rejects homogeneity,
𝜒 2(2) = 10.18,𝑝= 0.006(Holm-adjusted𝑝= 0.029),
𝑉= 0.18. Pairwise contrasts (Holm-corrected within the
three) locate the difference. Data scientists exceed software
engineers (OR= 2.51[1.34, 4.79],𝑝 Holm = 0.010) and
ML engineers exceed software engineers (OR= 2.05[1.09,
3.93],𝑝 Holm = 0.0496), while data scientists and ML
engineers do not differ (OR= 0.82[0.45, 1.48],𝑝= 0.57).
Theequivalencetestsagreewiththisreading:ata±20-point
margin,onlytheML–data-sciencepairisstatisticallyequiv-
alent (𝑝TOST = 0.016), whereas the two contrasts involving
software engineers are not (𝑝TOST = 0.27and0.56). The
role difference also survives adjustment for seniority, with
bothdatascientistsandMLengineersshowingroughlytwo-
and-a-half times the odds of software engineers (adjusted
ORs2.55[1.38, 4.69] and2.41[1.29, 4.49]). Leadership
is therefore consistently prominent in the two ML-adjacent
rolesbutmarkedlylesssoinsoftwareengineeringCVs,and
thedemand-sideassumptionofuniversalitydoesnottransfer
to candidate self-presentation.
Key takeaways for RQ1
•Collaboration, leadership, and communica-
tion dominate across all roles.
•Communication and problem solving are
markedly more prominent in data scientist
CVs than in the other two roles (H1a, H1d
supported), and mentoring is more prominent
in ML engineer CVs (H1b supported).
•ML engineer CVs are the most “soft-skill-
silent,” and data scientist CVs the least (H1c
supported);theML–softwaredifferenceisex-
plained by seniority composition rather than
by role.
•Contrarytoprediction,leadershiparticulation
is not role-invariant (H1e refuted): software
engineers report it at roughly half the rate of
the other two roles.
5.2. Variation by Seniority (RQ2)
To answer RQ2, candidates were categorized using a
five-year experience threshold. Professionals with less than
five years of experience were classified as junior, whereas
thosewithfiveormoreyearswerecategorizedassenior.The
resulting split is 114 junior and 186 senior CVs. Within the
software engineering cohort, 36 profiles were classified as
junior and 64 as senior. In the data science group, 32 candi-
dates were junior, and 68 were senior. The ML engineering
cohortexhibitsthehighestproportionofjuniorprofiles,with
46 juniors and 54 seniors. This comparatively larger share
ofearly-careerprofessionalsmayindicatearelativelyrecent
expansion of entry-level opportunities in the ML domain.
Senior CVs are denser in behavioral content overall.
Senior professionals report a mean of 4.99 distinct compe-
tencies (𝑆𝐷= 3.48) against 3.74 (𝑆𝐷= 3.31) for junior
professionals,Mann–Whitney𝑈= 12,971,𝑝= 0.001,rank-
biserial𝑟= 0.22.Table5summarizesthe10mostfrequently
mentioned soft skills across junior and senior cohorts for
the entire dataset. Four of the five directional predictions
concern specific competencies within this shift.
H2a(leadership)issupported,withthelargestsenior-
ity effect in the study.Aggregated across roles, leadership
appearsin23.7%ofjuniorCVs(27/114)and47.3%ofsenior
CVs (88/186): a risk difference of+23.6points (95% CI
[+12.5,+33.5]), OR= 2.88([1.68, 5.06]),ℎ= 0.50,
Fisher’s exact𝑝 <0.001(Holm-adjusted𝑝 <0.001). This
shiftindicatesthatasindividualsgainexperience,theirCVs
evolvefromdocumentingindividualtechnicalcontributions
toward demonstrating team guidance, project coordination,
and strategic impact.
H2b (coordination) and H2c (strategic thinking) are
supported.Coordination rises from 16.7% to 31.2% (OR
= 2.26[1.23, 4.30], risk difference+14.5points [+4.5,
+23.5],ℎ= 0.34,𝑝= 0.006, Holm-adjusted𝑝= 0.029),
andstrategicthinkingfrom5.3%to14.0%(OR= 2.92[1.12,
8.96], risk difference+8.7points [+1.6,+15.1],ℎ= 0.30,
𝑝= 0.020, Holm-adjusted𝑝= 0.029). Strategic thinking is
the rarest of the confirmatory outcomes, and its wide odds-
ratio interval reflects that; the direction is nonetheless the
predicted one, and the interval excludes unity.
H2d (no-skill rate) is supported.Among senior pro-
fessionals, only 7.5% (14/186) of CVs lacked detectable
behavioral competencies, against 21.1% (24/114) of junior
CVs: OR= 0.31([0.14, 0.65]), risk difference−13.5points
([−22.4,−5.5]),ℎ= −0.40,𝑝= 0.001(Holm-adjusted
𝑝= 0.009). The discrepancy is particularly evident among
junior ML engineers, where the no-skill rate reaches 30.4%
against 7.4% for senior ML engineers.
H2e adjudicates between substitution and accumu-
lation, and accumulation wins.Collaboration does not
recede as leadership language grows; it increases alongside
it, from 50.9% among junior professionals to 67.7% among
seniorprofessionals(OR= 2.02[1.22,3.37],riskdifference
+16.9points [+5.5,+27.9],ℎ= 0.35,𝑝= 0.005, Holm-
adjusted𝑝= 0.029). The substitution account, which would
have required a negative difference, is therefore refuted.
Senior CVs add directional language to collaborative lan-
guage rather than replacing one with the other. This has
a direct practical implication, discussed in Section 6, for
whatjuniorcandidatesshouldinferabouthowtowriteabout
collaboration.
H2f (the seniority effect is not an artifact of role
composition) is supported.Because the three roles differ
A. Azamnouri et al.:Preprint submitted to ElsevierPage 15 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Table 5
Top 10 Soft Skills by Seniority Level. In the senior column, self-organization ties strategic thinking at rank 10 (26 CVs, 14.0%);
strategic thinking is listed because it is the subject of a confirmatory hypothesis.
Junior Professionals (N=114) Senior Professionals (N=186)
Soft Skill Count Percentage Soft Skill Count Percentage
Collaboration 58 50.9% Collaboration 126 67.7%
Communication 30 26.3% Leadership 88 47.3%
Leadership 27 23.7% Communication 73 39.2%
Presentation 24 21.1% Problem solving 61 32.8%
Problem solving 23 20.2% Coordination 58 31.2%
Coordination 19 16.7% Presentation 56 30.1%
Mentoring 17 14.9% Mentoring 42 22.6%
Time management 16 14.0% Creativity 29 15.6%
Adaptive 15 13.2% Time management 29 15.6%
Motivated 15 13.2% Strategic thinking 26 14.0%
both in leadership prevalence (H1e) and in seniority com-
position, the aggregate seniority effect could in principle be
a compositional artifact. It is not. In a logistic model with
role held constant, seniority remains a strong predictor of
leadership articulation, adjusted OR= 3.06(95% CI [1.80,
5.23]), likelihood-ratio𝜒 2(1) = 18.21,𝑝 <0.001(Holm-
adjusted𝑝 <0.001). The non-parametric analogue agrees:
theCochran–Mantel–Haenszelcommonoddsratiostratified
by role is3.04([1.79, 5.17]),𝜒2 = 17.40,𝑝<0.001.
The second component of H2f concerns homogeneity,
and here the inferential analysis corrects an impression that
thedescriptivestatisticsinvite.Readasrawpercentages,the
seniority transition looks most dramatic among ML engi-
neers,whereleadershipmentionsrisefrom23.9%(11/46)to
57.4%(31/54),against34.4%to52.9%fordatascientistsand
13.9% to 32.8% for software engineers. The corresponding
stratum-specific odds ratios are4.22([1.67, 11.30]) for ML
engineers,3.00([0.96, 11.30]) for software engineers, and
2.13([0.83,5.71])fordatascientists.Theseintervalsoverlap
heavily, and both formal tests of homogeneity fail to reject.
The seniority×role interaction contributes nothing to the
model (likelihood-ratio𝜒 2(2) = 1.22,𝑝= 0.54), and
the Breslow–Day test gives𝜒 2(2) = 1.22,𝑝= 0.54.
The data are therefore consistent with a single, common
seniority effect operating in all three roles; the apparent
concentrationamongMLengineersisaconsequenceoftheir
lower junior baseline, not evidence of a steeper trajectory.
We flagthisexplicitlybecause thedescriptive readingis the
one a frequency-only analysis would have produced, and it
would have been wrong.
Key takeaways for RQ2
•Leadership mentions roughly double from ju-
nior to senior CVs (23.7%→47.3%; OR
2.88), and the effect survives adjustment for
role (adjusted OR3.06).
•Coordination, strategic thinking, and the dis-
appearance of soft-skill-silent CVs follow the
same direction (H2b–H2d supported).
•Collaboration accumulates rather than being
displaced by leadership (H2e): senior CVs re-
port both more often.
•The seniority effect is statistically homoge-
neousacrossroles;theapparentlysteeperML
engineering trajectory reflects a lower junior
baseline, not a different slope.
5.3. Presentation Style (RQ3)
Concerning RQ3, the extracted skills were analyzed
according to their presentation style within the CV. As de-
scribedinthemethodology,theextractionpipelinedifferen-
tiates between explicit mentions, where soft skills appear in
dedicated sectionssuch as“Skills”, andimplicit demonstra-
tions, where behavioral competencies are conveyed through
professional narratives in sections such as work experi-
ence or project descriptions. This distinction enables the
identification of how technical professionals communicate
their behavioral capabilities and whether they rely more on
structured keyword lists or contextual storytelling.
Theresultsrevealastrongpreferencefornarrative-based
disclosureofsoftskills.Acrossthedatasetof300CVs,can-
didates were nearly three times more likely to demonstrate
soft skills through professional narratives than to explicitly
list them as standalone keywords. Overall, only 3.3% of
candidates (10/300) relied exclusively on explicit keyword
lists as illustrated in Fig. 5. In contrast, 59.0% of the CVs
(177/300) communicated behavioral competencies entirely
throughcontextualdescriptionsoftheirprofessionalexperi-
enceswithoutlistingthemindedicatedskillssections.When
A. Azamnouri et al.:Preprint submitted to ElsevierPage 16 of 28

Detecting Soft Skills in ML Engineering Roles CVs
0 10 20 30 40 50 60 70 80
Percentage of CVs (N = 300)
Implicit only
(narrative only)
Explicit + implicit
(hybrid)
No skills
(neither)
Explicit only
(keywords only)
59.0%  (177/300)
25.0%  (75/300)
12.7%  (38/300)
3.3%  (10/300)
Figure 5:Distribution of soft skill disclosure styles across the CVs.
examining each disclosure style in more detail, explicit
mentions were identified in 28.3% of CVs (85/300). The
most frequently listed skills within these structured sections
were communication (15.7%) and collaboration (13.7%),
indicatingthatcandidatesoccasionallyhighlightwidelyrec-
ognizedinterpersonalcompetenciesasexplicitlabels.How-
ever,implicitdemonstrationswereconsiderablymorepreva-
lent, appearing in 84.0% of CVs (252/300). The skills most
frequently conveyed through narrative descriptions were
collaboration(47.7%),leadership(33.7%),andcoordination
(24.7%), typically illustrated through statements describ-
ing collaboration on projects, team leadership responsibil-
ities, or cross-functional coordination. Additionally, 25.0%
of candidates (75/300) adopted a hybrid disclosure strategy,
combining explicit skill listings with supporting narrative
evidence in their professional experience sections.
H3a is supported by a very large margin.Because
explicit and implicit disclosure are recorded on the same
document, the comparison is paired. Of the 187 CVs whose
two channels disagree, 177 disclose behavioral competen-
cies only through narrative and 10 only through keyword
lists, a discordant share of 94.7% (95% CI [90.4, 97.1]); the
exact McNemar test gives𝑝 <0.001with an odds ratio of
17.7. The same conclusion holds when the comparison is
made on counts rather than presence. The per-CV number
of narratively disclosed competencies exceeds the number
of keyword-disclosed competencies in the large majority of
the 250 CVs where the two differ, Wilcoxon signed-rank
𝑝<0.001,𝑟= 0.60.
This aggregate result conceals an asymmetry that mat-
tersmoreforpracticethantheaggregateitself.Disaggregat-
ingbycompetency(Table6)showsthatnarrativedominance
is not uniform across the taxonomy but is concentrated
in precisely those competencies employers describe as de-
cisive. Coaching (100% narrative), coordination (96.1%),
mentoring (94.9%), presentation (90.0%), and leadership
(87.8%) are disclosed almost exclusively through narrative,
and all remain significant after false-discovery correction.
At the other end, communication (54.4% narrative,𝑞=
0.54), problem-solving (59.5%,𝑞= 0.15), adaptability
(52.8%), self-organization (51.3%), and analytical ability
(34.4% narrative, i.e., predominantly keyword-listed) are as
likely or more likely to be stated as labels. In other words,
the competencies that candidates put in a skills section are
largelythegenericones,whilethespecific,evidence-bearing
competenciesthatdistinguishaseniorcandidatearetheones
that only appear in prose.
H3b is partially supported.The keyword–narrative ra-
tiovariesacrossthethreeanalyzedroles,asshowninFig.6,
and the3 × 4test of disclosure style by role rejects in-
dependence,𝜒 2(6) = 42.46,𝑝 <0.001(Holm-adjusted
𝑝 <0.001),𝑉= 0.27. Disclosure style, therefore, does
depend on role. The second clause of the hypothesis, that
ML engineers rely on narrative most heavily, is not con-
firmed at conventional levels. ML engineers show the high-
est narrative-only rate, with 66.0% of CVs demonstrating
soft skills solely through descriptions of professional activ-
ities, against 60.0% for software engineers and 51.0% for
datascientists,butneithertheomnibuscontrastonnarrative-
only rates (𝜒2(2) = 4.71,𝑝= 0.095) nor the planned
contrast of ML engineers against the other two roles (66.0%
vs. 55.5%, OR= 1.55[0.92, 2.66],𝑝= 0.083) reaches
significance. What the significant3 × 4result reflects is a
different contrast: data scientists are far more likely to use
both channels (44.0%, against 15.0% for ML engineers and
16.0% for software engineers) and far less likely to use nei-
ther. These candidates frequently label competencies such
as communication directly and then reinforce them through
examples of presenting analytical findings or collaborating
with stakeholders. Software engineers, meanwhile, show a
slightly higher tendency toward structured keyword presen-
tation,with8.0%ofCVsrelyingexclusivelyonexplicitskill
lists,against1.0%ineachoftheothertworoles.Only16.0%
A. Azamnouri et al.:Preprint submitted to ElsevierPage 17 of 28

Detecting Soft Skills in ML Engineering Roles CVs
ofMLengineeringCVslistanybehavioralcompetencyina
dedicated skills section.
Disclosure style does not vary significantly with senior-
ity.Narrative-onlydisclosurerisesfrom53.5%amongjunior
professionals to 62.4% among senior professionals, but the
differenceisnotsignificant(𝑝= 0.15),andtheproportionof
CVs containing any explicit skills section is essentially flat
(25.4% junior vs. 30.1% senior,𝑝= 0.43). What changes
with seniority is the amount and kind of behavioral content,
not the channel through which it is delivered.
Overall, these findings indicate that the communica-
tion of soft skills in technical CVs relies predominantly on
contextual storytelling rather than simple keyword enumer-
ation. As professionals accumulate experience, their CVs
shift from listing basic collaborative traits toward narrating
morecomplexresponsibilities,suchasleadership,coordina-
tion, and project orchestration. Furthermore, the substantial
number of implicitly disclosed competencies in the corpus
(1,007 skill–CV pairs) compared with explicitly listed ones
(347) indicates that roughly three-quarters (74.4%) of the
soft skill evidence in these CVs takes a form that keyword
matching cannot detect. This is a property of the documents
themselves rather than of any particular tool. Any screening
approach restricted to explicit labels observes only a small
fraction of the competencies candidates actually convey,
and, as Table 6 shows, the fraction it does observe is biased
toward the least discriminating competencies.
Key takeaways for RQ3
•Soft skills are predominantly conveyed
through narrative storytelling, not keyword
lists (H3a; 94.7% of discordant CVs, exact
McNemar𝑝<0.001).
•Narrative dominance is concentrated in the
highest-value competencies: leadership,
coordination, mentoring, and coaching are
88–100% narrative, whereas communication,
problem solving, and analytical ability are as
often keyword-listed.
•Disclosure style depends on role (H3b, first
clause), but the driver is the data scientists’
dual-channelstyleratherthanasignificantML
engineering excess in narrative-only disclo-
sure (second clause not confirmed).
•Disclosure style does not change significantly
with seniority; the volume and kind of behav-
ioral content do.
5.4. Summary of Hypothesis Tests and
Exploratory Contrasts
Table 7 consolidates the outcome of every confirma-
tory test. Eleven of the 13 hypotheses are supported, one
(H3b) is partially supported, and one (H1e) is refuted. All
13 raw𝑝-values remain significant after Holm–Bonferroni
correctionacrossthefamily,sothefamily-wiseerrorcontrol
does not change any conclusion; we report the adjusted
values nonetheless because the strength of evidence differs
substantially across the family, ranging from𝑝Holm <10 −5
for H3a and H1a to𝑝 Holm = 0.029for six hypotheses that sit
close to the corrected threshold.
Twooftheoutcomesdeserveemphasisbecausetheyrun
against the interpretation that a descriptive analysis would
have produced. First, H1e was formulated as a prediction
of no role difference, taken directly from the demand-side
literature, and it is refuted. Leadership articulation is not
universal across roles but concentrated in the two ML-
adjacentones.Second,H 2f’shomogeneityclauseshowsthat
theseniorityeffectonleadershipdoesnotdifferacrossroles,
whichcontradictsthenaturalreadingoftherawpercentages.
Astudythatreportedfrequenciesalonewouldplausiblyhave
claimed both that leadership is a universal baseline and that
MLengineersshowadistinctivesenioritytrajectory;neither
claim survives testing.
Beyond the confirmatory family, we tested every com-
petency detected in at least 15 CVs (24 labels) against role
and against seniority, controlling the false discovery rate
at 5% within each family. Seventeen competencies differ
significantly across roles after correction. The strongest are
communication (𝑉= 0.31,𝑞 <0.001), presentation (𝑉=
0.28,𝑞 <0.001), and time management (𝑉= 0.28,𝑞 <
0.001), the last of these running in the opposite direction
to most role effects: it is a software engineering signature
(29%vs.10%and6%).Speaking(𝑉= 0.24,𝑞= 0.001)and
writing (𝑉= 0.18,𝑞= 0.016) are disproportionately ML
engineering markers, while strategic thinking (𝑉= 0.23,
𝑞= 0.002), decision making (𝑉= 0.18,𝑞= 0.016), self-
organization (𝑉= 0.18,𝑞= 0.016), curiosity (𝑉= 0.18,
𝑞= 0.019), and passion (𝑉= 0.17,𝑞= 0.028) cluster
in data science CVs. In the seniority family, only leadership
survives correction (𝑞= 0.001); coordination and collabo-
ration fall just outside the threshold (𝑞= 0.0501for both),
andcommunication,strategicthinking,andproblemsolving
aresuggestivebutnotsignificantafteradjustment(𝑞= 0.098
each).Wenotethisasymmetryplainlythattherolesignature
isbroadanddistributedacrossmanycompetencies,whereas
the seniority signal, when the entire taxonomy is scanned
without prior direction, is carried overwhelmingly by lead-
ershipalone.TheconfirmatoryresultsforH 2b,H 2c,andH 2e
are not undermined by this, since they were specified in
advance and belong to a family of 13 rather than 24, but
their exploratory counterparts are a reminder that they are
the weaker members of the confirmatory set.
5.5. Robustness and Sensitivity Analyses
Three analyses probe whether the confirmatory conclu-
sions depend on choices made in the measurement pipeline.
We focus them on H2a, the primary hypothesis, and on H1a,
the largest role effect.
Dichotomization of seniority.The five-year threshold
discards information. Re-estimating the primary hypothesis
withtheunderlyingcontinuousestimateoftotalexperience,
A. Azamnouri et al.:Preprint submitted to ElsevierPage 18 of 28

Detecting Soft Skills in ML Engineering Roles CVs
0 20 40 60 80 100
Percentage of CVs within each role (n = 100 per role)
Data Scientists
ML Engineers
Software Engineers
51.0% 44.0% 4.0% 1.0%
66.0% 15.0% 18.0% 1.0%
60.0% 16.0% 16.0% 8.0%
Implicit only Explicit + implicit No skills Explicit only
Figure 6:Soft skill disclosure styles by role.
Table 6
Disclosure channel by competency. “Keyword” and “Narrative” partition the CVs in which the competency was detected, so their
sum is the competency’s total prevalence. “Narrative share” is the percentage of those CVs disclosing it through narrative rather
than a dedicated skills section, with a 95% Wilson interval.𝑝is the two-sided exact binomial test against a 50/50 split;𝑞is the
Benjamini–Hochberg adjusted value. Competencies detected in fewer than 15 CVs are omitted.
Competency Keyword Narrative Narrative share 95% CI 𝑝 𝑞
Coaching 0 33 100.0% [89.6, 100.0] <0.001 <0.001
Coordination 3 74 96.1% [89.2, 98.7] <0.001 <0.001
Mentoring 3 56 94.9% [86.1, 98.3] <0.001 <0.001
Accountability 1 15 93.8% [71.7, 98.9] <0.001 0.001
Presentation 8 72 90.0% [81.5, 94.8] <0.001 <0.001
Initiative 3 24 88.9% [71.9, 96.1] <0.001 <0.001
Speaking 2 16 88.9% [67.2, 96.9] 0.001 0.002
Leadership 14 101 87.8% [80.6, 92.6] <0.001 <0.001
Writing 4 25 86.2% [69.4, 94.5] <0.001 <0.001
Strategic thinking 6 26 81.3% [64.7, 91.1] <0.001 0.001
Time management 9 36 80.0% [66.2, 89.1] <0.001 <0.001
Creativity 8 32 80.0% [65.2, 89.5] <0.001 <0.001
Goal orientation 5 18 78.3% [58.1, 90.3] 0.011 0.018
Collaboration 41 143 77.7% [71.2, 83.1] <0.001 <0.001
Curiosity 9 23 71.9% [54.6, 84.4] 0.020 0.032
Passion 11 18 62.1% [44.0, 77.3] 0.265 0.353
Problem solving 34 50 59.5% [48.8, 69.4] 0.101 0.152
Communication 47 56 54.4% [44.8, 63.7] 0.431 0.544
Adaptive 17 19 52.8% [37.0, 68.0] 0.868 0.992
Self-organized 19 20 51.3% [36.2, 66.1] 1.000 1.000
Decision making 11 11 50.0% [30.7, 69.3] 1.000 1.000
Motivated 16 15 48.4% [32.0, 65.2] 1.000 1.000
Social skills 10 7 41.2% [21.6, 64.0] 0.629 0.755
Analytical 21 11 34.4% [20.4, 51.7] 0.110 0.156
in a logistic model adjusting for role, reproduces the effect.
Each additional year of experience is associated with a 22%
increase in the odds of articulating leadership, OR= 1.22
per year (95% CI [1.13, 1.33]),𝑝 <0.001,𝑛= 295(five
CVslackausableexperienceestimate).Theseniorityresult
isthereforenotanartifactofwherethethresholdwasplaced.
Documentlength.LongerCVsoffermoreopportunities
for a competency to be detected, and senior CVs are longer
on average. Adding document length to the model leaves
theseniorityeffectessentiallyunchanged(adjustedOR2.82
[1.60,4.97],𝑝<0.001),andlengthitselfisnotasignificant
predictor once seniority and role are in the model (OR1.02
per 1,000 characters,𝑝= 0.41).
Extractionerror.Themostsubstantivethreatisthatthe
outcomevariableisproducedbyapipelinewithameasured
recall of 0.74 and precision of 0.69. We address it in two
steps rather than by argument alone.
First, we propagate the measurement error through the
estimates. Treating extraction as a diagnostic test applied
to each competency–CV cell, the measured precision and
A. Azamnouri et al.:Preprint submitted to ElsevierPage 19 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Table 7
Outcomes of the 13 confirmatory hypothesis tests. Effect sizes are odds ratios (OR) with exact 95% confidence intervals for2 × 2
contrasts, Cramér’s𝑉for omnibus𝜒 2 tests.𝑝 Holm is corrected across the family of 13. Data Scientist (DS), Software Engineer
(SE). Percentage triples are reported in the order ML / DS / SE.
ID Contrast Observed Effect size [95% CI] 𝑝 𝑝Holm Outcome
H1a Communication: DS vs.
ML+SE
54.0% vs. 24.5% OR 3.60 [2.11, 6.21] <0.001 <0.001 Supported
H1b Mentoring: ML vs. DS+SE 28.0% vs. 15.5% OR 2.11 [1.13, 3.94] 0.013 0.029 Supported
H1c No-skill rate across roles 18 / 4 / 16% 𝑉= 0.19; contrast OR 0.20 [0.05,
0.60]
0.006 0.029 Supported
H1d Problem solving: DS vs. ML 34.0% vs. 15.0% OR 2.90 [1.40, 6.25] 0.003 0.020 Supported
H1e Leadership across roles
(predicted equal)
42 / 47 / 26% 𝑉= 0.18; DS vs. SE OR 2.51
[1.34, 4.79]
0.006 0.029 Refuted
H2a Leadership: senior vs. junior 47.3% vs. 23.7% OR 2.88 [1.68, 5.06] <0.001 <0.001 Supported
H2b Coordination: senior vs.
junior
31.2% vs. 16.7% OR 2.26 [1.23, 4.30] 0.006 0.029 Supported
H2c Strategic thinking: senior
vs. junior
14.0% vs. 5.3% OR 2.92 [1.12, 8.96] 0.020 0.029 Supported
H2d No-skill rate: senior vs.
junior
7.5% vs. 21.1% OR 0.31 [0.14, 0.65] 0.001 0.009 Supported
H2e Collaboration: senior vs.
junior
67.7% vs. 50.9% OR 2.02 [1.22, 3.37] 0.005 0.029 Accumulation
H2f Leadership∼seniority∣role adjusted OR 3.06 [1.80, 5.23]; interaction
𝑝= 0.54
<0.001 <0.001 Supported
H3a Narrative vs. keyword
within CV
177 vs. 10
discordant
OR 17.7; 94.7% [90.4, 97.1] <0.001 <0.001 Supported
H3b Disclosure style×role 3 × 4table 𝑉= 0.27; ML contrast𝑝= 0.083 <0.001 <0.001 Partial
recalltogetherwiththeobservedcell-levelprevalenceimply
a specificity of approximately 0.967 (the value ranges from
0.958 to 0.973 across plausible assumptions about the ef-
fective size of the taxonomy). Applying the standard matrix
correctionfornon-differentialmisclassification,𝜋= (𝑝 obs +
𝑆𝑝−1)∕(𝑆𝑒+𝑆𝑝−1),everyconfirmatorycontrastbecomes
larger, not smaller. The leadership seniority gap widens
from+23.6to+33.4percentage points, the communication
role gap from+29.5to+41.7points, the leadership gap
betweendatascientistsandsoftwareengineersfrom+21.0to
+29.7points,andthecollaborationsenioritygapfrom+16.9
to+23.9points. Varying sensitivity over[0.65,0.85]and
specificity over[0.95,0.99]places the corrected leadership
senioritygapbetween+28.1and+39.4points,ineverycase
above the uncorrected estimate. Imperfect extraction atten-
uates the observed differences toward zero, so the reported
effects are conservative rather than inflated.
Second, non-differential error is the favorable case; the
real concern is differential error, in which the pipeline de-
tects competencies more readily in one group than another.
We therefore compute how large such a differential would
have to be to eliminate each effect. For H2a, no differential
favoring senior CVs can do it; even a pipeline with perfect
sensitivity on senior CVs and the measured sensitivity of
0.74 on junior CVs would leave a corrected gap of 16.7
percentagepoints,andclosingthegapentirelywouldrequire
a sensitivity above 1.0, which is impossible. Running the
correction in the other direction, sensitivity on junior CVs
would have to fall to 0.36, less than half the value measured
on the evaluation set, while remaining 0.74 on senior CVs.
ForH 1a thecorrespondingfiguresare1.72(impossible)and
0.33. Differential extraction error of that magnitude is not
credible for a pipeline whose prompt is identical across
groups and whose evaluation sample spans all three roles
and both seniority levels.
Two limits of this analysis should be stated. It assumes
thatthepipeline’saggregatesensitivityandspecificity,mea-
sured over the taxonomy as a whole, apply to each compe-
tency individually, which will not be exactly true for rare
labels; and it corrects prevalences, not the tests themselves,
sothecorrectedriskdifferencesshouldbereadasindicating
the direction and rough magnitude of the bias rather than
as replacement point estimates. Neither limit affects the
qualitative conclusion, which is that the reported effects are
attenuated by extraction noise rather than manufactured by
it.Finally,theexplicit-versus-implicitcomparisoninRQ3is
internallyconsistentinawaythatmakesitespeciallyrobust.
Both branches rely on the same extraction model and the
same taxonomy, so systematic extraction bias affects both
sides of the comparison and largely cancels in the implicit-
to-explicit ratio.
6. Discussion
The findings of this study provide several insights into
how soft skills are articulated in technical CVs across ML-
related professions. First, the aggregated analysis confirms
that collaboration, leadership, and communication repre-
sentthemostprominentbehavioralcompetenciesacrossthe
dataset. The strong presence of collaboration-related skills
supports the view that modern AI and software engineer-
ing projects rely heavily on multidisciplinary collaboration,
A. Azamnouri et al.:Preprint submitted to ElsevierPage 20 of 28

Detecting Soft Skills in ML Engineering Roles CVs
whereMLengineers,datascientists,andsoftwareengineers
must work closely to deliver complex systems. Leadership
andcommunicationalsoappearfrequently,reinforcingprior
research suggesting that interpersonal competencies are in-
creasingly valued alongside technical expertise in engineer-
ing roles.
6.1. Role signatures and where the demand-side
account holds
Threeofthefourdirectionalrolepredictionswederived
frompriorworkareborneoutonthecandidateside,andwith
effects large enough to be practically meaningful. Data sci-
enceprofilesplacegreateremphasisoncommunication(OR
3.60) and problem solving (OR 2.90), reflecting the need
to interpret analytical findings and communicate insights to
non-technical stakeholders. ML engineering CVs highlight
mentoring more frequently (OR 2.11), which may reflect
the bridging role that ML engineers often play between
software engineering and data science teams. That these
candidate-side patterns match what the job-advertisement
and interview literature attribute to the same roles is a non-
trivial corroboration. The two data sources are collected
independently, from different populations, using different
instruments, and there was no guarantee that employer-side
roledescriptionswouldleaveasignatureinhowindividuals
write about themselves.
The one prediction that fails is instructive precisely
because it fails. H1e held that leadership would be role-
invariant, onthe strength of studiesthat report leadershipas
a universal expectation in software and AI work [14, 34]. In
ourcorpus,itisnot:softwareengineersarticulateleadership
at roughly half the rate of data scientists and ML engineers
(26.0% vs. 47.0% and 42.0%), and the gap persists when
seniorityisheldconstant.Tworeadingsareavailable.Onthe
first, the demand-side observation remains correct and the
divergence is one of self-presentation. Software engineers
may be as likely to exercise leadership but less likely to
frame it as such in a document that competes for space with
technical depth. On the second, the universality claim was
alwaysanaggregationartifactofjob-advertisementcorpora,
in which the leadership language of senior and managerial
postings is averaged over a role population that is much
broader than the individual-contributor software engineers
our sampling captured. Our data cannot separate these, but
either reading has the same consequence for practice. A
software engineering candidate who leads work and does
not say so is systematically less visible than a data science
candidatedoingthesameamountofleading.Thisisthekind
ofclaimthatonlycandidate-sidedatacanproduce,andonly
inferential analysis can support.
6.2. Soft-skill-silent CVs and the articulation gap
Anotherimportantobservationconcernsthepresenceof
CVs without detectable soft skills. Although the majority
of CVs (87.3%) included at least one behavioral compe-
tency,asubset,particularlywithinMLengineering,focused
almost exclusively on technical content. This pattern may
reflect differences in self-presentation strategies, with some
candidates prioritizing the listing of tools, frameworks, and
technicalachievementsoverthedescriptionofinterpersonal
competencies. The relatively higher no-skill rate among
ML engineers may also indicate that behavioral traits are
sometimes expressed using language that falls outside ex-
isting taxonomy variants. The inferential analysis adds a
qualification that the raw rates obscure. Once seniority is
held constant, ML engineers and software engineers are
statistically indistinguishable on this outcome (adjusted OR
1.03,𝑝= 0.94), and it is data scientists who stand apart
(adjusted OR 0.22,𝑝= 0.010). The elevated ML no-skill
rate is thus largely a consequence of that cohort containing
the most junior professionals, not of something intrinsic to
the ML engineering role.
This pattern has practical implications for ML and
MLOps practitioners preparing CVs for the technical labor
market.Priorworkonhiringmanagerperspectivesindicates
that non-technical competencies frequently weigh heavily
in evaluation decisions for engineering roles, particularly at
the early-career stage [30], and analyses of job advertise-
ments consistently show that employers explicitly require
interpersonal and behavioral skills alongside technical ex-
pertise [8, 14]. The 18% no-skill rate observed among ML
engineering CVs in our dataset, and the 30.4% rate among
junior ML engineers in particular, therefore represents a
meaningful gap between what hiring managers value and
what a substantial subset of candidates choose to surface in
theirCVs.PractitionerswhoconcentratetheirCVcontenton
tools, frameworks, and model architectures while omitting
any behavioral narrative may be underselling competencies
that recruiters actively look for, and that the candidates
themselves likely demonstrate in practice through team
collaboration, mentoring, and stakeholder communication.
We therefore encourage ML and MLOps practitioners,
especially those at earlier career stages, to make space in
their CVs for explicit or narrative evidence of how they
collaborate, lead, mentor, and communicate, even briefly,
alongside the technical content.
6.3. What changes with seniority, and what does
not
The analysis of seniority levels further highlights the
evolution of soft skill narratives throughout a professional
career. Junior professionals tend to emphasize collabora-
tive participation, whereas senior professionals increasingly
highlight leadership, coordination, and strategic competen-
cies. The effect on leadership is substantial and robust. An
adjusted odds ratio of 3.06, equivalent to a 23.6-point rise
inprevalence,whichsurvivesadjustmentforrole,replicates
when experience is treated as a continuous variable, and
would require an implausible degree of differential extrac-
tion error to explain away.
Theinferentialanalysiscorrectstheaggregatepicturein
twowaysthatmatter.First,wehadexpected,andthedescrip-
tivepercentagesappeartoshow,thatthesenioritytransition
issharpestamongMLengineers,whoseleadershipmentions
A. Azamnouri et al.:Preprint submitted to ElsevierPage 21 of 28

Detecting Soft Skills in ML Engineering Roles CVs
rise from 23.9% to 57.4%. The homogeneity tests do not
supportthatreading.Thestratum-specificoddsratiosaresta-
tistically indistinguishable (interaction𝑝= 0.54; Breslow–
Day𝑝= 0.54), and the apparent steepness among ML
engineers follows from their unusually low junior baseline
ratherthanfromadifferentrateofchange.Theprofessional-
ization pattern is best described as a single effect operating
across all three roles. Second, the competing accounts of
what happens to collaboration are adjudicated cleanly in
favor of accumulation. Collaboration does not recede as
leadership grows; both increase together, and senior CVs
report collaboration at 67.7% against 50.9% among juniors.
The framing of a career transition “from participation to
direction” is therefore misleading as a description of what
candidates write: senior CVs are not less collaborative in
their language, they are more of both.
An alternative interpretation of the whole seniority pat-
ternisalsoworthnoting.Ratherthandevelopingfundamen-
tally new competencies, senior professionals may primarily
develop the ability to articulate competencies they already
practiced as juniors. The sharp drop in the no-skill rate
from21.1%to7.5%overall,andfrom30.4%to7.4%among
ML engineers, even though juniors clearly engage in col-
laborative, team-based work, supports this articulation-gap
interpretation.Thecompetencieswerearguablypresent,but
the language for surfacing them was not. The accumulation
result strengthens this reading. If seniors were genuinely
trading participation for direction, we would expect collab-
orativelanguagetogiveway;thatitinsteadgrowsalongside
leadership language is more consistent with seniors having
simply become better at describing what they do. This dis-
tinction matters because it reframes the seniority transition
aspartlyaCV-writingskillratherthanpurelyacompetency-
acquisitionskill,andCV-writingskillisteachableonamuch
shorter timescale than five years of experience.
6.4. Implications for education and curriculum
design
The findings also carry implications for educators and
curriculum designers preparing students for AI-related ca-
reers. Three patterns in particular warrant attention. First,
the strong professionalization gap observed between junior
and senior CVs, namely that leadership mentions roughly
double from 23.7% to 47.3% and the no-skill rate drops
from 21.1% to 7.5%, suggests that articulating leadership,
coordination, and stakeholder communication is something
many professionals appear to learn in industry rather than
duringformaleducation.Curriculaincomputerscienceand
data science programs could narrow this gap by integrating
explicit instruction on how to identify, develop, and com-
municatebehavioralcompetenciesacquiredthroughcourse-
work,capstoneprojects,andteam-basedassignments,rather
than treating these as implicit byproducts of technical train-
ing[4].Second,therole-specificdifferencesobservedinthe
dataset suggest that program designers should not treat soft
skill development as a single homogeneous topic. Programs
targeting different specializations may benefit from empha-
sizingthespecificbehavioralcompetenciesthatpractitioners
inthoserolesmostfrequentlydemonstrate,e.g.,stakeholder
communication and analytical problem framing for data
science tracks, and team mentoring and cross-functional
coordination for ML engineering and MLOps tracks. The
refutation of H1e adds a further, less obvious recommen-
dation: because software engineering candidates articulate
leadership least often despite leadership being a general ex-
pectationinthefield,softwareengineeringprogramsinpar-
ticularmaybenefitfromtreatingleadershiparticulationasan
explicit learning outcome rather than assuming it emerges.
Third, the high no-skill rate among junior ML engineers
(30.4%)suggestsagapnotonlyinsoftskilldevelopmentbut
also in CV-writing instruction. Career-services support and
professional development modules embedded in technical
curricula could equip students with concrete strategies for
narrating behavioral competencies in their CVs, including
the kind of narrative phrasing identified in Section 5 as the
dominant disclosure style among practitioners. Such inter-
ventions would address both the development of behavioral
competencies, a long-standing concern in the soft skills
literature [44], and the ability to articulate them visibly in
CVs, which the present paper identifies as a distinct and
previously underexplored dimension of the soft skills gap.
6.5. Implications for screening pipeline design
Finally, the results demonstrate that soft skills are pre-
dominantly communicated through narrative descriptions
rather than explicit keyword lists. The roughly three-to-one
ratio between implicitly and explicitly disclosed competen-
cies (1,007 vs. 347) is not merely a stylistic observation;
it has direct consequences for how CVs are processed in
modern hiring pipelines. A substantial fraction of recruit-
ment systems, including applicant tracking systems and CV
screening tools, rely heavily on keyword matching against
predefined skill vocabularies [18, 54]. If candidates pre-
dominantly express soft skills through narrative rather than
explicitlabels,suchsystemswillsystematicallyunder-detect
interpersonal competencies.
The per-competency breakdown in Table 6 sharpens
this concern considerably, and is, in our view, the most
actionable finding in the paper. Narrative dominance is
not uniform. It is concentrated in exactly the competencies
that differentiate candidates. Coaching, coordination, men-
toring, presentation, and leadership are disclosed through
narrative in 88–100% of the CVs that disclose them at
all, whereas communication, problem-solving, adaptability,
self-organization,andanalyticalabilityareaslikely,ormore
likely,tobestatedasbarelabels.Akeyword-basedscreener,
therefore,doesnotsimplyseeasmallersampleofeachcan-
didate’s behavioral profile; it sees a systematically distorted
one, in which the generic self-descriptors that almost every
candidate can claim are visible, and the specific, evidence-
bearing competencies that would distinguish a senior can-
didate from a junior one are invisible. Since leadership is
alsothecompetencythatchangesmostwithseniority(H 2a),
A. Azamnouri et al.:Preprint submitted to ElsevierPage 22 of 28

Detecting Soft Skills in ML Engineering Roles CVs
a keyword-based screener is close to blind on precisely the
dimension along which it is being asked to discriminate.
This raises a concrete fairness concern. Candidates
whose CV-writing conventions favor storytelling may be
disadvantaged relative to candidates who happen to list the
same competencies as keywords, even when both groups
demonstratethemequallyinpractice.Theeffectisnotevenly
distributed. ML engineers, at 66.0% narrative-only disclo-
sure and only 16.0% listing any behavioral competency in
a skills section, are most exposed, while data scientists,
44.0% of whom use both channels, are best protected. We
note for accuracy that the role difference in narrative-only
rates specifically did not reach significance in our data (𝑝=
0.083),sothisshouldbereadasapatternthatwarrantsrepli-
cation rather than an established disparity; the difference in
dual-channel use, by contrast, is unambiguous. Generative-
LLM-based extraction approaches, as developed in this
paper, offer one path toward closing this gap by recovering
competencies from narrative context. However, building
this capability into production-grade screening tools also
requires careful attention to the precision–recall trade-offs
and hallucination risks, and to the fairness properties of the
extractor itself, since an extractor that recovers narrative
evidence unevenly across groups would replace one bias
with another.
A methodological observation also follows from these
findings. The substantial gap between implicitly (1,007)
and explicitly (347) disclosed competencies in our corpus
providesdirectempiricaljustificationforthechoiceofLLM-
based generative extraction over dictionary or keyword-
based approaches. Had we relied on keyword matching
alone, we would have captured at most 347 of the 1,354
unique skill–CV pairs in the corpus, missing nearly three-
quarters (74.4%) of the soft skill articulation present in
candidateCVs.Thisisnotahypotheticaladvantage;itisthe
differencebetweenconcludingthatMLengineeringCVsare
largely silent on soft skills, which a keyword-based system
would suggest, and concluding that ML engineering CVs
are heavily narrative-driven, which our analysis revealed.
More concretely still, a keyword-only analysis would have
observed 14 of the 115 leadership disclosures in the corpus
and would have had no power whatsoever to detect the
seniority effect that constitutes our primary finding. The
pipelinethusenablesafindingthatthemethodologyofmuch
prior work would not have investigated.
7. Threats to Validity
This section outlines the potential limitations of the
study and discusses threats to validity to provide a transpar-
ent interpretation of the findings.
7.1. Construct Validity
A first concern regarding construct validity relates to
how soft skills are operationally defined and measured in
this study. We rely on the TaxoSoft taxonomy [25] as the
canonical inventory of soft skill categories. While TaxoSoft
is grounded in real labor-market language and has been
used as a reference in prior soft-skill extraction research,
any taxonomy is inherently constrained by the categories
it defines. Behavioral competencies expressed in language
that falls outside the taxonomy’s variants are systemati-
cally excluded from our analysis, which may particularly
affect candidates whose self-presentation uses non-standard
or domain-specific phrasing.
A second construct concern is the operationalization of
seniority through a binary five-year threshold. While this
alignswithcommonindustrylevelingstandards,itabstracts
away nuanced differences in expertise within each cohort.
We mitigated this by re-estimating the primary hypothesis
with the underlying continuous experience variable, which
reproduced the effect (OR 1.22 per year, [1.13, 1.33]); con-
tinuousormulti-tierclassificationsmightnonethelessrefine
this measurement in future work.
A third concern is that our outcome measures articula-
tion,notcompetence.ACVthatdoesnotmentionleadership
is evidence about the document, not about the candidate.
All claims in this paper are, therefore, claims about self-
presentation, where we discuss the underlying competen-
cies,weflagtheinferenceexplicitlyasaninterpretationthat
our data support but do not establish.
7.2. Internal Validity
A primary internal validity threat concerns extraction
noise. The optimized Gemini 3 Pro Preview configura-
tion achieved a precision of 0.69 and a recall of 0.74 on
the human-annotated evaluation set, meaning that approx-
imately30%ofextractedskillslackdirecttextualgrounding
and approximately 25% of genuinely present skills are
missed.Thereportedprevalencesshouldthereforebereadas
estimatesratherthanexactmeasurements.Section5.5quan-
tifies the consequence rather than merely acknowledging
it. Under non-differential misclassification, the correction
moves every confirmatory contrast away from the null, and
eliminating the primary effect would require differential
sensitivity between senior and junior CVs so extreme (0.74
vs. 0.36, or above 1.0 in the other direction) that it is not
attainable. The comparative claims also rely on relative
ratherthanabsolutefrequencies,sotheyarepreservedunder
any extraction error that is approximately uniform across
groups.
Furthermore, a threat arises from annotator subjectivity
in the construction of the ground truth dataset. The 100-CV
evaluation sample was annotated by two human researchers
following the TaxoSoft taxonomy, with disagreements re-
solvedbytheexplicitrulesdescribedinSection4;wedidnot
compute a formal inter-coder reliability coefficient, which
limits how precisely the reliability of the gold standard can
be characterized. Moreover, a threat concerns the LLM-
as-a-judge step in the role disambiguation procedure. For
13 CVs in which candidates self-identified as both data
scientistsandMLengineers,Gemini2.5Proactedasathird
annotator alongside the two human researchers. While the
LLM aligned with the final majority decision in 11 of 13
cases (84.6%), generative models may inherit stereotypes
A. Azamnouri et al.:Preprint submitted to ElsevierPage 23 of 28

Detecting Soft Skills in ML Engineering Roles CVs
from their training data about role boundaries that human
annotators do not share. We mitigated this risk through the
tri-party majority-voting design, in which the LLM never
acted as the sole arbiter and no case was decided with-
out agreement from at least one human annotator. Because
the 13 affected CVs represent 4.3% of the corpus and are
confined to the ML–data-science boundary, any residual
misassignment would attenuate rather than create the role
contrasts between those two groups, and cannot affect the
seniority results at all.
7.3. Conclusion Validity
Four threats specific to the inferential analysis warrant
discussion.First,thehypothesesinSection3.1werederived
from prior literature but were not preregistered, and they
wereformulatedbyresearcherswhohadalreadyconstructed
the corpus. We mitigate this by fixing the comparison and
the predicted direction for each hypothesis before testing,
by controlling the family-wise error rate across the confir-
matory family, and by reporting the exploratory contrasts
separately under false-discovery control. Readers should
nonetheless treat the confirmatory label as denoting deriva-
tionfrompriortheoryratherthanthestrongerguaranteethat
preregistration provides.
Second, the study has limited power for small effects.
At𝛼= 0.05and 80% power, the design detects differ-
ences of roughly 16–19 percentage points depending on the
contrast (Section 3.6). Non-significant results in this study,
particularly the ML engineering narrative-only contrast in
H3b (𝑝= 0.083) and the homogeneity tests in H2f, should
thereforenotbereadasestablishingtheabsenceofaneffect.
The homogeneity conclusion in H2f is best stated as the
absence of evidence for role-specific seniority slopes given
a sample that could only have detected large ones.
Third, several confirmatory results sit close to the cor-
rectedsignificancethreshold.Fiveofthesupportedhypothe-
ses(H 1b,H 1c,H 2b,H 2c,H 2e),togetherwiththerefutedH 1e,
have Holm-adjusted𝑝-values of 0.029, and H2c additionally
hasawideodds-ratiointervalreflectingtherarityofstrategic
thinking in junior CVs (6 occurrences). These should be
regarded as the weakest members of the confirmatory set,
and they are exactly the results we would expect to be most
fragile under replication. The exploratory scan reinforces
this: when the whole taxonomy is tested against seniority
without prior direction, only leadership survives correction.
Fourth, the tests treat CVs as independent observations.
Thisisreasonableforacorpusofdocumentsauthoredbydis-
tinct individuals, but the corpus is drawn from two sources
collectedfiveyearsapart,andthesourceisnotfullyorthog-
onal to role and seniority. We cannot rule out that some
portion of the role or seniority contrasts reflects period
effects in CV-writing convention rather than the constructs
of interest. Disentangling the two would require a corpus
stratified by collection period within each role, which we
identify as a target for replication.
7.4. External Validity
A first external validity threat concerns the boundary
betweenMLengineeringanddatascienceroles.Theseroles
overlap substantially in many organizations, with title con-
ventions varying across industries and regions. Treating
them as mutually exclusive categories may therefore intro-
duceclassificationnoiseinthecomparativeanalysis.Ourtri-
party disambiguation procedure addresses this for explicitly
ambiguous CVs but does not eliminate borderline cases
where role identity is implicit rather than self-declared.
Another threat is dataset composition. The 300-CV cor-
pus is constructed from two sources: a publicly available
GitHub corpus collected in 2020 [24] and a contemporary
supplementary set collected through Google queries be-
tween November and December 2025. Both sources have
theirownselectionbiases.TheGitHubcorpusreflectswhat-
ever distribution of professionals chose to publish CVs on
a public platform around 2020, while the contemporary set
reflectscandidateswhoseCVsweresufficientlydiscoverable
through public web search. Both subsets are biased toward
candidates who have actively chosen to make their CVs
publiclyaccessible,whichisitselfaself-selectioneffectthat
may not represent the broader workforce.
In addition, another threat is the dataset’s English-only
nature.Non-EnglishCVswereexcludedduringfiltering,and
publiclysourcedwebCVsarelikelytooverrepresentregions
and conventions where publishing CVs online is common
practice.Soft-skillarticulationisshapedbyculturalconven-
tionsofprofessionalself-presentation,andourfindingsmay
not generalize to labor markets where different rhetorical
norms prevail. Cross-cultural extensions of the analysis are
a natural direction for future work.
The final external threat is sample size. The 300 CV
corpus,whilebalancedacrossthethreetargetroles,captures
only a small slice of the global technical workforce and
cannot resolve small effects. As described in Section 3, the
choice of 100 CVs per role reflects an upper bound on what
waspracticallyfeasibletocurateatthequalitylevelrequired
for this study; Section 3.6 states precisely which effect sizes
this permits us to detect.
7.5. Reliability
The reliability threat concerns model availability. The
extraction pipeline relies on Gemini 3 Pro Preview, a Pre-
viewmodelwhoseparameters,behavior,oravailabilitymay
change without notice. Future replications using the same
prompt may obtain different results because the underly-
ing model has been updated, deprecated, or replaced. To
decouple the statistical findings from this dependency, the
replication package includes the per-CV outcome matrix
producedbythepipelinealongsidetheanalysisscript,sothat
every test reported in Section 5 can be reproduced exactly
without re-running the extraction.
8. Conclusion
This paper investigated how soft skills are expressed in
technical CVs through an empirical study of 300 CVs from
A. Azamnouri et al.:Preprint submitted to ElsevierPage 24 of 28

Detecting Soft Skills in ML Engineering Roles CVs
software engineers, data scientists, and ML engineers, en-
abled by a generative extraction pipeline that identifies both
explicitandimplicitrepresentationsofbehavioralcompeten-
cies. Rather than reporting frequencies alone, we translated
the claims of the demand-side literature into 13 falsifiable
hypotheses and tested them inferentially with effect sizes,
confidence intervals, and family-wise error control, com-
plemented by false-discovery-controlled exploratory con-
trasts and by sensitivity analyses that quantify how much
extraction error each conclusion could withstand. Eleven
hypotheses were supported, one partially, and one refuted.
Four findings stand out. First, role signatures on the
candidate side largely mirror the role descriptions in the
demand-side literature. Data scientists articulate communi-
cation (OR 3.60) and problem solving (OR 2.90) more than
the other roles, ML engineers articulate mentoring more
(OR 2.11), and data scientists are least likely to produce
a CV with no behavioral content at all. Second, the ex-
pectation that leadership would be a role-invariant baseline
is refuted. Software engineers articulate it at roughly half
the rate of the other two roles, and the gap survives ad-
justment for seniority. Third, soft-skill articulation grows
with career progression, with the odds of articulating lead-
ership roughly tripling from junior to senior professionals
(adjusted OR 3.06 [1.80, 5.23]); this effect is statistically
homogeneousacrossthethreerolesratherthanconcentrated
among ML engineers as the raw percentages suggest, and
collaboration accumulates alongside leadership rather than
being displaced by it. Fourth, candidates convey soft skills
predominantly through narrative, with 1,007 implicit skill
markers against 347 explicit mentions, and this narrative
dominance is concentrated in exactly the competencies that
discriminate between candidates. Leadership, coordination,
mentoring, and coaching are conveyed through narrative in
88–100% of cases, while the competencies candidates do
list as keywords are the generic ones. Overall, the study
suggests that the much-discussed soft skills gap in ML-
relatedprofessionsis,atleastinpart,anarticulationgap.The
competencies are present in candidate narratives but remain
invisibletokeyword-basedscreening,andinvisibleinaway
thatissystematicallybiasedagainstthemostdiscriminating
evidence.
Several directions for future work remain. First, the
analysis could be extended beyond CVs to professional pro-
files on platforms such as LinkedIn, enabling comparisons
of self-presentation across document types. Second, cross-
cultural and multilingual corpora would test whether the
patterns observed here generalize beyond English-language
CVs. Third, a preregistered replication on a corpus strati-
fied by collection period would separate role and seniority
effects from period effects in CV-writing convention, and
would convert the hypotheses tested here into genuinely
confirmatory tests. Fourth, on the methodological side, the
extraction pipeline could be strengthened by benchmark-
ing emerging model architectures and exploring retrieval-
augmented generation (RAG) to improve robustness, and
evaluated for whether its recovery of narrative evidence is
equally effective across candidate groups.
CRediT authorship contribution statement
Aidin Azamnouri:Writing – original draft, Writing –
review & editing, Visualization, Validation, Methodology,
Investigation, Formal analysis, Data curation, Conceptual-
ization, Supervision.Nouran Ayad:Writing – review &
editing, Visualization, Validation, Methodology, Investiga-
tion, Formal analysis, Data curation.Justus Bogner:Writ-
ing–review&editing.StefanWagner:Writing–review&
editing, Funding acquisition.
Statement on open data and ethics
All artifacts containing the approach implementation,
fullextractionoutputs,prompts,codes,theper-CVoutcome
matrix, and the complete statistical analysis script are avail-
able athttps://doi.org/10.5281/zenodo.21873447.
All CVs analyzed in this study originate from publicly
accessible sources. The corpus-derived subset is taken from
the multi-labeled resume corpus released by Jiechieu and
Tsopze [24], which was published as a research artifact for
academicNLPtasksandisopenlyavailableonGitHub.The
contemporary subset consists of CVs that the candidates
themselves made publicly available on the web, retrieved
through targeted web queries restricted to documents the
authors explicitly chose to publish in indexed and freely ac-
cessibleform.Becausebothsourcesarealreadyinthepublic
domain, no personal data was recollected, reidentified, or
republished as part of this study. The analysis uses these
CVs solely for aggregate statistical purposes. All findings
reported in this paper are presented at the role or cohort
level, and no individual candidate is named, profiled, or
identified in the paper, the figures, the tables, or any artifact
released alongside it. Any verbatim text used to illustrate
examples (e.g., Fig. 2) shows only short excerpts that do
notcontainidentifyinginformationsuchaspersonalnames,
email addresses, employer names, or phone numbers; these
elementswereredactedbeforeinclusioninthefigure.Wedo
notredistributetheCVsthemselves;thereplicationpackage
consists of the extraction outputs (skill labels) along with
code and prompts. A subset of contemporary CVs also
includes explicit author statements stating that the docu-
ment should not be redistributed or republished, which we
honor without exception. We further note that anonymizing
publicly indexed CVs before redistribution would offer no
meaningfulprivacyprotection,becausetheoriginalsremain
freely accessible through the same web channels through
which they were collected; any redacted derivative would
stillbetraceablebacktoitssourceviasearchengineretrieval
of the unmodified original. We therefore consider analysis-
only use, with no redistribution of the underlying CVs, the
mostdefensibleethicalpositionforthiswork.Thisapproach
is consistent with established practice in empirical software
engineering research that uses publicly available web data
asasourceofanalysis[53],andwearguethattheaggregate,
A. Azamnouri et al.:Preprint submitted to ElsevierPage 25 of 28

Detecting Soft Skills in ML Engineering Roles CVs
comparativenatureoftheanalysisposesminimaladditional
privacy risk beyond what already follows from the public
availability of the source documents.
It is also worth noting that the LLMs employed in this
study are designed to comply with stringent data protection
requirements by ensuring that sensitive conversational data
is neither retained nor transmitted to any external servers.
Declaration of competing interest
The authors declare that they have no known competing
financial interests or personal relationships that could have
appeared to influence the work reported in this paper.
Acknowledgements
The project on which this work is based was sponsored
bytheFederalMinistryofEducationandResearch(BMBF)
under the funding code 01IS23069.
References
[1] Ahmed, T., Devanbu, P., Treude, C., Pradel, M., 2025. Can llms
replace manual annotation of software engineering artifacts?, in:
2025IEEE/ACM22ndInternationalConferenceonMiningSoftware
Repositories(MSR),IEEE.p.526–538. URL:http://dx.doi.org/10.
1109/msr66628.2025.00086, doi:10.1109/msr66628.2025.00086.
[2] Akkasi, A., 2024. Job description parsing with explainable trans-
former based ensemble models to extract the technical and non-
technical skills. Natural Language Processing Journal 9, 100102.
URL:http://dx.doi.org/10.1016/j.nlp.2024.100102, doi:10.1016/j.
nlp.2024.100102.
[3] Azamnouri,A.,2025. Cocochallengesinmlengineeringteams:How
tocollaborativelybuildml-enabledsystems,in:2025IEEE/ACM4th
International Conference on AI Engineering – Software Engineering
forAI(CAIN),IEEE.p.241–243. URL:http://dx.doi.org/10.1109/
cain66642.2025.00036, doi:10.1109/cain66642.2025.00036.
[4] Azamnouri, A., Hörauf, D., Schönberger, B., Bogner, J., Wagner,
S., 2026. Teaching ai competencies: Experiences from coaching
interdisciplinary teams to develop ai prototypes. Computers and
Education: Artificial Intelligence 10, 100580. URL:http://dx.doi.
org/10.1016/j.caeai.2026.100580, doi:10.1016/j.caeai.2026.100580.
[5] Baltes, S., Angermeir, F., Arora, C., Barón, M.M., Chen, C., Böhme,
L., Calefato, F., Ernst, N., Falessi, D., Fitzgerald, B., et al., 2025.
Guidelines for empirical studies in software engineering involving
large language models. arXiv preprint arXiv:2508.15503 .
[6] Busquim, G., Araújo, A.A., Lima, M.J., Kalinowski, M., 2024a.
Towards effective collaboration between software engineers and data
scientists developing machine learning-enabled systems, in: Anais
do XXXVIII Simpósio Brasileiro de Engenharia de Software (SBES
2024), Sociedade Brasileira de Computação. p. 24–34. URL:http:
//dx.doi.org/10.5753/sbes.2024.3027, doi:10.5753/sbes.2024.3027.
[7] Busquim, G., Villamizar, H., Lima, M.J., Kalinowski, M., 2024b.
On the Interaction Between Software Engineers and Data Scien-
tists When Building Machine Learning-Enabled Systems. Springer
Nature Switzerland. p. 55–75. URL:http://dx.doi.org/10.1007/
978-3-031-56281-5_4, doi:10.1007/978-3-031-56281-5_4.
[8] Calanca, F., Sayfullina, L., Minkus, L., Wagner, C., Malmi, E.,
2019. Responsible team players wanted: an analysis of soft
skill requirements in job advertisements. EPJ Data Science 8.
URL:http://dx.doi.org/10.1140/epjds/s13688-019-0190-z, doi:10.
1140/epjds/s13688-019-0190-z.
[9] Croxford,E.,Gao,Y.,First,E.,Pellegrino,N.,Schnier,M.,Caskey,J.,
Oguss,M.,Wills,G.,Chen,G.,Dligach,D.,Churpek,M.M.,Mayam-
purath, A., Liao, F., Goswami, C., Wong, K.K., Patterson, B.W., Af-
shar, M., 2025. Evaluating clinical ai summaries with large language
models as judges. npj Digital Medicine 8. URL:http://dx.doi.org/
10.1038/s41746-025-02005-2, doi:10.1038/s41746-025-02005-2.
[10] De Morais Leça, M., De Souza Santos, R., 2025. Curious, critical
thinker, empathetic, and ethically responsible: Essential soft skills
for data scientists in software engineering, in: 2025 IEEE/ACM
47th International Conference on Software Engineering: Software
Engineering in Society (ICSE-SEIS), IEEE. p. 151–162. URL:
http://dx.doi.org/10.1109/icse-seis66351.2025.00021, doi:10.1109/
icse-seis66351.2025.00021.
[11] De Smedt, J., le Vrang, M., Papantoniou, A., 2015. Esco: Towards a
semantic web for the european labor market. Ldow@ www 144.
[12] Decorte, J.J., Verlinden, S., Hautte, J.V., Deleu, J., Develder, C.,
Demeester, T., 2023. Extreme multi-label skill extraction training
using large language models. URL:https://arxiv.org/abs/2307.
10778,arXiv:2307.10778.
[13] Deming, D.J., 2017. The growing importance of social skills
in the labor market*. The Quarterly Journal of Economics 132,
1593–1640. URL:http://dx.doi.org/10.1093/qje/qjx022, doi:10.
1093/qje/qjx022.
[14] Galster, M., Mitrovic, A., Malinen, S., Holland, J., 2022. What soft
skills does the software industry *really* want? an exploratory study
ofsoftwarepositionsinnewzealand,in:Proceedingsofthe16thACM
/ IEEE International Symposium on Empirical Software Engineering
and Measurement, ACM. p. 272–282. URL:http://dx.doi.org/10.
1145/3544902.3546247, doi:10.1145/3544902.3546247.
[15] Glassdoor, 2026. Senior data scientist jobs in berlin.https:
//www.glassdoor.com/Job/berlin-senior-data-scientist-jobs-SRCH_
IL.0,6_IM1020_KO7,28.htm. Accessed: 2026-01-24.
[16] Goutte, C., Gaussier, E., 2005. A Probabilistic Interpretation of Pre-
cision, Recall and F-Score, with Implication for Evaluation. Springer
Berlin Heidelberg. p. 345–359. URL:http://dx.doi.org/10.1007/
978-3-540-31865-1_25, doi:10.1007/978-3-540-31865-1_25.
[17] Guest, G., MacQueen, K., Namey, E., 2012. Applied Thematic
Analysis. SAGEPublications,Inc. URL:http://dx.doi.org/10.4135/
9781483384436, doi:10.4135/9781483384436.
[18] Gugnani, A., Misra, H., 2020. Implicit skills extraction using
document embedding and its use in job recommendation. Pro-
ceedings of the AAAI Conference on Artificial Intelligence 34,
13286–13293. URL:http://dx.doi.org/10.1609/aaai.v34i08.7038,
doi:10.1609/aaai.v34i08.7038.
[19] Gugnani, A., Reddy Kasireddy, V.K., Ponnalagu, K., 2018. Gener-
ating unified candidate skill graph for career path recommendation,
in: 2018 IEEE International Conference on Data Mining Workshops
(ICDMW), IEEE. p. 328–333. URL:http://dx.doi.org/10.1109/
icdmw.2018.00054, doi:10.1109/icdmw.2018.00054.
[20] Harnad, S., 2025. Language writ large: Llms, chatgpt, grounding,
meaning and understanding. URL:https://arxiv.org/abs/2402.
02243,arXiv:2402.02243.
[21] Haug, M., Azamnouri, A., Fritz, M., Woltmann, L., Schriever, C.,
Wagner,S.,2025.MLOpsAdoptionintheManufacturingIndustry:A
CaseStudywithZeissSMT.SpringerNatureSwitzerland. pp.16–36.
URL:http://dx.doi.org/10.1007/978-3-032-07313-6_2, doi:10.1007/
978-3-032-07313-6_2.
[22] He, J., Shi, J., Zhuo, T.Y., Treude, C., Sun, J., Xing, Z., Du, X., Lo,
D.,2025. Fromcodetocourtroom:Llmsasthenewsoftwarejudges.
URL:https://arxiv.org/abs/2503.02246,arXiv:2503.02246.
[23] Indeed,2026. Seniordatascientistjobsinberlin.https://de.indeed.
com/q-senior-data-scientist-l-berlin-jobs.html. Accessed: 2026-
01-24.
[24] Jiechieu, K.F.F., Tsopze, N., 2020. Skills prediction based on
multi-label resume classification using cnn with model predictions
explanation. Neural Computing and Applications 33, 5069–5087.
URL:http://dx.doi.org/10.1007/s00521-020-05302-x, doi:10.1007/
s00521-020-05302-x.
A. Azamnouri et al.:Preprint submitted to ElsevierPage 26 of 28

Detecting Soft Skills in ML Engineering Roles CVs
[25] Khaouja, I., Mezzour, G., Carley, K.M., Kassou, I., 2019. Building
a soft skill taxonomy from job openings. Social Network Analysis
and Mining 9. URL:http://dx.doi.org/10.1007/s13278-019-0583-9,
doi:10.1007/s13278-019-0583-9.
[26] Kolluru, K., Adlakha, V., Aggarwal, S., Mausam, Chakrabarti, S.,
2020. Openie6: Iterative grid labeling and coordination analy-
sis for open information extraction, in: Proceedings of the 2020
Conference on Empirical Methods in Natural Language Processing
(EMNLP),AssociationforComputationalLinguistics.p.3748–3761.
URL:http://dx.doi.org/10.18653/v1/2020.emnlp-main.306, doi:10.
18653/v1/2020.emnlp-main.306.
[27] Kovacs, I., Vamosi Zarandne, K., 2022. Digital marketing employ-
ability skills in job advertisements – must-have soft skills for entry
level workers: A content analysis. Economics &amp; Sociology 15,
178–192. URL:http://dx.doi.org/10.14254/2071-789x.2022/15-1/
11, doi:10.14254/2071-789x.2022/15-1/11.
[28] Levels.fyi, 2026. The levels.fyi standard: Career level framework.
https://www.levels.fyi/2020/. Accessed: 2026-01-24.
[29] Li,N.,Kang,B.,Bie,T.D.,2023.Skillgpt:arestfulapiserviceforskill
extraction and standardization using a large language model. URL:
https://arxiv.org/abs/2304.11060,arXiv:2304.11060.
[30] Loufek, S.B., Santos, F., Trinkenreich, B., 2025. Beyond the job
posting:Whathiringmanagersseekinentry-levelsoftwareengineer-
ing candidates, in: 2025 ACM/IEEE International Symposium on
Empirical Software Engineering and Measurement (ESEM), IEEE.
p. 01–11. URL:http://dx.doi.org/10.1109/esem64174.2025.00055,
doi:10.1109/esem64174.2025.00055.
[31] Lyu,W.,Liu,J.,2021. Softskills,hardskills:Whatmattersmost?evi-
dencefromjobpostings. AppliedEnergy300,117307. URL:http://
dx.doi.org/10.1016/j.apenergy.2021.117307,doi:10.1016/j.apenergy.
2021.117307.
[32] Mailach, A., Siegmund, N., 2023. Socio-technical anti-patterns in
building ml-enabled software: Insights from leaders on the forefront,
in: 2023 IEEE/ACM 45th International Conference on Software En-
gineering (ICSE), IEEE. p. 690–702. URL:http://dx.doi.org/10.
1109/icse48619.2023.00067, doi:10.1109/icse48619.2023.00067.
[33] Malherbe, E., Aufaure, M.A., 2016. Bridge the terminology gap
between recruiters and candidates: A multilingual skills base built
fromsocialmediaandlinkeddata,in:2016IEEE/ACMInternational
Conference on Advances in Social Networks Analysis and Mining
(ASONAM), IEEE. p. 583–590. URL:http://dx.doi.org/10.1109/
asonam.2016.7752295, doi:10.1109/asonam.2016.7752295.
[34] Malinen,S.,Galster,M.,Mitrovic,A.,Iyer,S.S.,Peirisand,P.,Clarke,
A., 2025. Soft skills in software engineering: Insights from the
trenches,in:2025IEEE/ACM47thInternationalConferenceonSoft-
ware Engineering: Software Engineering in Practice (ICSE-SEIP),
IEEE.p.296–306. URL:http://dx.doi.org/10.1109/icse-seip66354.
2025.00032, doi:10.1109/icse-seip66354.2025.00032.
[35] Mohamed, A., Rashid, M.E., Shaalan, K., 2025. In-context learning
inlargelanguagemodels(llms):Mechanisms,capabilities,andimpli-
cations for advanced knowledge representation and reasoning. IEEE
Access 13, 95574–95593. URL:http://dx.doi.org/10.1109/access.
2025.3575303, doi:10.1109/access.2025.3575303.
[36] Mohammed,F.S.,Ozdamli,F.,2024.Asystematicliteraturereviewof
soft skills in information technology education. Behavioral Sciences
14, 894. URL:http://dx.doi.org/10.3390/bs14100894, doi:10.3390/
bs14100894.
[37] Nahar, N., Zhou, S., Lewis, G., Kästner, C., 2022. Collabora-
tion challenges in building ml-enabled systems: communication,
documentation, engineering, and process, in: Proceedings of the
44th International Conference on Software Engineering, ACM. p.
413–425. URL:http://dx.doi.org/10.1145/3510003.3510209, doi:10.
1145/3510003.3510209.
[38] Niva, D., Yariv, I., 2020. In The AI Era, Soft Skills Are The New
Hard Skills. Emerald Publishing Limited. p. 55–78. URL:http:
//dx.doi.org/10.1108/book-978-1-64802-075-920251007, doi:10.1108/
book-978-1-64802-075-920251007.
[39] Patacsil,F.,S.Tablatin,C.L.,2017. Exploringtheimportanceofsoft
and hard skills as perceived by it internship students and industry: A
gap analysis. Journal of Technology and Science Education 7, 347.
URL:http://dx.doi.org/10.3926/jotse.271, doi:10.3926/jotse.271.
[40] Peretz, O., Nakash, M., 2025. From junior to senior: Skill require-
ments for ai professionals across career stages. Proceedings of the
International Conference on Research in Business, Management and
Finance 2, 9–20. URL:http://dx.doi.org/10.33422/icrbmf.v2i1.
1178, doi:10.33422/icrbmf.v2i1.1178.
[41] Phan, T.T., Pham, V.Q., Nguyen, H.D., Huynh, A.T., Tran, D.A.,
Pham, V.T., 2021. Ontology-Based Resume Searching System
for Job Applicants in Information Technology. Springer Interna-
tional Publishing. p. 261–273. URL:http://dx.doi.org/10.1007/
978-3-030-79457-6_23, doi:10.1007/978-3-030-79457-6_23.
[42] Piorkowski,D.,Park,S.,Wang,A.Y.,Wang,D.,Muller,M.,Portnoy,
F., 2021. How ai developers overcome communication challenges in
a multidisciplinary team: A case study. Proceedings of the ACM on
Human-Computer Interaction 5, 1–25. URL:http://dx.doi.org/10.
1145/3449205, doi:10.1145/3449205.
[43] Robert Half, 2026. Senior Software Engineer Salary (Up-
dated for 2026).https://www.roberthalf.com/us/en/job-details/
senior-software-engineer. 2026SalaryGuide;accessed2026-01-24.
[44] Romanenko, Y.N., Stepanova, M., Maksimenko, N., 2024. Soft
skills: students and employers crave. Humanities and Social
Sciences Communications 11. URL:http://dx.doi.org/10.1057/
s41599-024-03250-8, doi:10.1057/s41599-024-03250-8.
[45] Sajid, H., Kanwal, J., Bhatti, S.U.R., Qureshi, S.A., Basharat, A.,
Hussain, S., Khan, K.U., 2022. Resume parsing framework for
e-recruitment, in: 2022 16th International Conference on Ubiqui-
tousInformationManagementandCommunication(IMCOM),IEEE.
p. 1–8. URL:http://dx.doi.org/10.1109/imcom53663.2022.9721762,
doi:10.1109/imcom53663.2022.9721762.
[46] Saldana, J., 2021. The Coding Manual for Qualitative Re-
searchers. SAGEPublicationsLtd. URL:http://dx.doi.org/10.4135/
9781036235611, doi:10.4135/9781036235611.
[47] Sinha, A.K., Amir Khusru Akhtar, M., Kumar, A., 2021. Re-
sume Screening Using Natural Language Processing and Ma-
chine Learning: A Systematic Review. Springer Singapore. p.
207–214. URL:http://dx.doi.org/10.1007/978-981-33-4859-2_21,
doi:10.1007/978-981-33-4859-2_21.
[48] Smith, E., Braschler, M., Weiler, A., Haberthuer, T., 2019. Syntax-
based skill extractor for job advertisements, in: 2019 6th Swiss
Conference on Data Science (SDS), IEEE. p. 80–81. URL:http:
//dx.doi.org/10.1109/sds.2019.000-3, doi:10.1109/sds.2019.000-3.
[49] Succi, C., 2019. Are you ready to find a job ranking of a list
of soft skills to enhance graduates’ employability. International
Journal of Human Resources Development and Management 19,
281. URL:http://dx.doi.org/10.1504/ijhrdm.2019.100638, doi:10.
1504/ijhrdm.2019.100638.
[50] Vu,A.,Oppenlaender,J.,2026. Promptengineer:Analyzinghardand
softskillrequirementsintheaijobmarket. URL:https://arxiv.org/
abs/2506.00058,arXiv:2506.00058.
[51] Wang,R.,Guo,J.,Gao,C.,Fan,G.,Chong,C.Y.,Xia,X.,2025. Can
llms replace human evaluators? an empirical study of llm-as-a-judge
in software engineering. Proceedings of the ACM on Software En-
gineering 2, 1955–1977. URL:http://dx.doi.org/10.1145/3728963,
doi:10.1145/3728963.
[52] Wang, Y., Allouache, Y., Joubert, C., 2021. Analysing cv corpus
for finding suitable candidates using knowledge graph and bert, in:
DBKDA2021TheThirteenthInternationalConferenceonAdvances
in Databases, Knowledge,and Data Applications, Valencia, Spain.
URL:https://hal.science/hal-03325062.
[53] Wohlin, C., Runeson, P., Höst, M., Ohlsson, M.C., Regnell, B.,
Wesslén, A., 2024. Experimentation in Software Engineering.
Springer Berlin Heidelberg. URL:http://dx.doi.org/10.1007/
978-3-662-69306-3, doi:10.1007/978-3-662-69306-3.
[54] Wosiak, A., 2021. Automated extraction of information from polish
resume documents in the it recruitment process. Procedia Computer
A. Azamnouri et al.:Preprint submitted to ElsevierPage 27 of 28

Detecting Soft Skills in ML Engineering Roles CVs
Science 192, 2432–2439. URL:http://dx.doi.org/10.1016/j.procs.
2021.09.012, doi:10.1016/j.procs.2021.09.012.
[55] Xu, D., Chen, W., Peng, W., Zhang, C., Xu, T., Zhao, X., Wu, X.,
Zheng, Y., Wang, Y., Chen, E., 2024. Large language models for
generative information extraction: a survey. Frontiers of Computer
Science 18. URL:http://dx.doi.org/10.1007/s11704-024-40555-y,
doi:10.1007/s11704-024-40555-y.
[56] Zhang, M., Jensen, K., Sonniks, S., Plank, B., 2022. Skillspan:
Hard and soft skill extraction from english job postings, in: Pro-
ceedings of the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics: Human Lan-
guage Technologies, Association for Computational Linguistics. p.
4962–4984. URL:http://dx.doi.org/10.18653/v1/2022.naacl-main.
366, doi:10.18653/v1/2022.naacl-main.366.
A. Azamnouri et al.:Preprint submitted to ElsevierPage 28 of 28
