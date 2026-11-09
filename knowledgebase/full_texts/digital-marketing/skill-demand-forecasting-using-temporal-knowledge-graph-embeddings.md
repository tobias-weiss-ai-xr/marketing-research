---
title: Skill Demand Forecasting Using Temporal Knowledge Graph Embeddings
url: https://arxiv.org/abs/2504.07233
category: digital-marketing
subcategory: empirical
date: 2025-04
venue: ''
authors:
- Yousra Fettach
- Adil Bahaj
- Mounir Ghogho
source: arxiv
pdf_url: https://arxiv.org/pdf/2504.07233
pages: 17
chars: 56036
fetched_at: '2026-11-08T13:15:17+00:00'
kb_version: 1
---

# Skill Demand Forecasting Using Temporal Knowledge Graph Embeddings

Skill Demand Forecasting Using Temporal Knowledge Graph
Embeddings
Yousra Fettacha,∗,1, Adil Bahajb,1 and Mounir Ghoghob,c
aGhent University, IDLab, Department of Electronics and Information Systems, Ghent Belgium
bCOLCOM, University Mohammed VI Polytechnic, Rabat Morocco
cFaculty of Engineering,University of Leeds, United Kingdom
ARTICLE INFO
Keywords:
Knowledge graphs
Labor Market
Temporal link prediction
Representation learning
ABSTRACT
Rapid technological advancements pose a significant threat to a large portion of the global
workforce,potentiallyleavingthembehind.Intoday’seconomy,thereisastarkcontrastbetween
the high demand for skilled labour and the limited employment opportunities available to those
who are not adequately prepared for the digital economy. To address this critical juncture and
gain a deeper and more rapid understanding of labour market dynamics, in this paper, we
approach the problem of skill need forecasting as a knowledge graph (KG) completion task,
specifically, temporal link prediction. We introduce our novel temporal constructed from online
job advertisements. We then train and evaluate different temporal KG embeddings for temporal
link prediction. Finally, we present predictions of demand for a selection of skills practiced
by workers in the information technology industry. The code and the data are available on our
GitHub repository (https://github.com/team611/JobEd).
1. Introduction
As the employment landscape transforms due to emerging technologies, students and employees must confront
the reality of skill gaps. This discrepancy between the skills possessed by the workforce and those sought after by
employers has the potential to result in millions of unfilled positions over the next decade Garcia de Macedo et al.
(2022) carrying significant economic and social consequences. Precise projections of future labour market conditions
can empower current learners to optimize their future productivity and align with employers’ requirements. Although
the ownership of this gap lies with individuals – students, and employees – numerous entities play a role in nurturing
andmanaginghumancapital.Educationalinstitutions,governmentbodies,andbusinessescanenhancetheirdecision-
making regarding human capital when equipped with accurate labour market forecasts. When decision-makers –
including students, educational institutions, government bodies, and businesses – rely on recent trends to guide their
choices, they implicitly make predictions about future developments Yazdanian et al. (2022).
Labourmarketdemandforecastingstartedasworkforcedemandforecasting.Inthistask,researcherstrytopredict
theevolutionoflabourdemandbasedonpreviousobservationsKwaketal.(1977)Ward(1996)Woolardetal.(2003)
Chanetal.(2006).Themeasureoflabourdemandinthesestudiesisthenumberofworkersrequiredforajob.However,
theseapproachessufferfrommultiplelimitationsthathinderthegeneralizationandadaptabilityofthesolutions.These
approaches try to model the evolution of labour demand which can be limited to a company, sector, region and other
contextual information. This stifles the generalization of the data and the approaches to other settings. In addition,
focusingonmodellingjobdemandandnotskilldemandignorestheever-changinglandscapeofthejobmarket,which
generates new job titles consistently and requires new skills for old job titles.
Standard forecasting models, like time series and machine learning methods, often treat skills and jobs as
isolated entities or rely on simple, direct relationships. KGs represent entities (such as skills and jobs) as nodes
and the relationships between them as edges. This structure naturally captures the intricate web of dependencies and
interactions, allowing for a more nuanced understanding of how skills are connected to job roles and industry trends
Chao et al. (2024).
∗Corresponding author
yousra.fettach@uir.ac.ma (Y. Fettach);adil.bahaj@uir.ac.ma (A. Bahaj);mounir.ghogho@uir.ac.ma (M. Ghogho)
ORCID(s):
1These authors contributed equally to this work. This work has been done at the International University of Rabat.
Y. Fettach et al.:Preprint submitted to Elsevier Page 1 of 16
arXiv:2504.07233v2  [cs.CY]  14 Apr 2025

In a practical setting traditional models require the availability of quantitative measures to be used in forecasting
for each job and its corresponding skills. This can present a limitation for new jobs, skills or job-skill pairs. However,
this is not the case for skill demand forecasting as a temporal link prediction.
Tomitigatesomeoftheselimitations,laterresearchtriedtosolveskilldemandforecastingbypredictingthedemand
for certain skills in a job title and how they evolve with time Wolf et al. (2023) Chao et al. (2024) Vaidya and Dhruv
(2021), Dawson et al. (2020) Jaramillo et al. (2020). These studies however assume the availability of sufficient data
thatquantifiesthedemandforaskillofagivenjobtitlewithtime,afterwhichtheycanonlymodelthatparticularskill
for that particular job title. Consequently, these studies only focus on a set of jobs with established skills and don’t
generalizetoemergingskills.Tosurpasstheselimitationswemodelthesemanticsofskillsandjobtitlesbyexploring
the high-level relations between them and other attributes that affect the flow of demand in the job market. Compared
to the previous settings, this setting allows for the forecasting of skill demands between jobs and skills that haven’t
been linked historically. To achieve this we model the interactions between jobs, skills and other related concepts as
a temporal knowledge graph Cai et al. (2024) and formulate the forecasting problem as a temporal knowledge graph
link prediction problem.
KnowledgeGraphs(KGs)playacrucialroleinstructuringreal-worldfacts,traditionallypresentingstaticsnapshots
ofcurrentknowledge.However,thereisagrowinginterestinTemporalKnowledgeGraphs(TKGs)thataimtocapture
the intricate temporal dynamics of information (Leblay and Chekol (2018),García-Durán et al. (2018), Lacroix et al.
(2020)). Recent endeavours in the field of TKGs focus on predicting future missing links, involving a query about a
specific time and associated historical facts. For example, a query could be "What team will win the World Cup in
2026?". The goal is to identify the most appropriate entity (such as a football team) from a set of options to complete
the missing information. Essentially, TKGs help predict future relationships in evolving knowledge contexts. In this
context, temporal KG completion can be useful in the discovery of new relationships between entities. For example,
new jobs have limited information available, to mitigate this, KG completion can be used to uncover the new jobs’
relation to existing skills or vice versa.
In this work, we explore temporal knowledge graph forecasting to predict the evolution of skill demand in the job
market. To achieve this objective we use JobEdKG, a KG introduced in Fettach et al. (2024). JobEdKG is extracted
frompublicjobpostingsandonlinecourses.Itcontainsaplethoraofentitiesandrelationsthatlinkjobsandskillsand
other related concepts (e.g. courses, companies, sectors...). JobEdKG facts have a temporal validity, which signifies
the timestamp of the first job posting where they occur in the source data. The contributions of this work include:
• We formulate the job skill forecasting problem as a temporal link prediction problem. This approach takes
advantageofexistinghigh-orderrelationshipsbetweenjobsandskillsviarelatedconcepts(e.g.sector,company,
course etc) to predict the evolution of link strength between jobs and skills.
• Introducing a novel temporal KG, which contains high-order relationships between jobs, skills and related
concepts. To our knowledge, this is the only temporal KG on the subject of job-skill evolution.
• Training and evaluating multiple models on the task of temporal link prediction and leveraging these models to
infer the temporal evolution of existing and unseen job-skill pairs.
The organization of this paper is outlined as follows: Section 2 provides an examination of the related literature.
Section3outlinesabriefrun-throughJobEdKG(Fettachetal.(2024))andthedescriptionandimplementationdetails
of our KG completion model. The experiments we conducted are presented in Section 4 where we also showcase the
results of our case study and discuss further implications of our work. Finally, we conclude the paper in Section 7.
2. Background and Related work
Therecentemphasisonskillshasbecomepossibleduetoadvancementsinnaturallanguageprocessing(NLP)and
the digitalization of texts related to the labour market. Job advertisements offer valuable insights into labour demand,
whileresumesandsocialmediaprofilesprovideinformationabouttheskillspossessedbydifferenttypesofworkers.In
the next few subsections, we explore skill demand forecasting, the use of knowledge graphs to analyze the job market
and temporal KG embeddings in comparison with time series forecasting.
Y. Fettach et al.:Preprint submitted to Elsevier Page 2 of 16

2.1. Skill Demand Forecasting
Research on predicting skill demand and supply can be broadly classified into two categories: expert-based and
learning-based methods. Expert-based approaches analyze skill shifts using survey data, often providing general
forecastingresultsbasedonexpertdomainknowledge.Learning-basedmethods,ontheotherhand,offermoredetailed
predictions by leveraging machine learning techniques to identify patterns and implications. Expert-based studies
started with studies such as Ward (1996) Woolard et al. (2003) Chan et al. (2006) that focused on workforce demand
forecasting which faced many limitations because of the lack of generalization in these methods.
Learning-based methods focused on skill demand forecasting. Studies like Vaidya and Dhruv (2021) used the
SVM model to predict the skills based on profession. Others like Dawson et al. (2020) used the XGBoost to predict
yearlyskillsshortagesinlabourmarkets.StudiessuchasJaramilloetal.(2020)builtaspatialrepresentationofthejob
market that allows for tracking change in skills’ demand, however, this representation didn’t incorporate any temporal
information. Similarly, Liu et al. (2021) used multiple neural networks to match jobs to skills. Time series analysis
approaches were also utilized in this direction of research, where Garcia de Macedo et al. (2022) used time series
for practical skills demand forecasting and Sibarani and Scerri (2020) presented a methodology for the discovery of
in-demand skillsets based on the observation of skills clusters in a time series.
2.2. Knowledge graphs in analyzing the job market
Studiessuchas(Luoetal.(2019))havetackledtheissueofemploymentrepresentationinKGs.Inordertocapture
the similarity and ordering relationships between job titles and business pairings, the authors created a representation
of employment roles. The Skills & Occupation KG developed in (de Groot et al. (2021)) is the most recent study
in this field of job advice. This KG was created by incorporating external job ads into the taxonomies of skills and
occupations that already existed. Another study created a KG to represent the artificial intelligence job market and
theaccompanyingnecessaryabilities(Jiaetal.(2018)).TheKGmadeiteasiertoinvestigatetheconnectionsbetween
variousAI-relatedkeycompetencies.JobEdKGisanotherimportantpieceofliteratureFettachetal.(2024)wherethe
authors built a KG based on job postings and Massive Open Online Courses (MOOCs) to recommend online courses
and predict in-demand skills based on uncertain KG embeddings.
2.3. Temporal KGs embedding
KG embeddings aim to generate low-dimensional representations of entities and relationships Wang et al. (2017).
These embeddings rely on different components such as the embedding space and the scoring function that measures
the plausibility of factual triples.
Recent methods have taken into consideration the temporal information for more accurate embeddings and better
link prediction. Inspired by the taxonomy in Han et al. (2021), we divide the literature on TKG embedding into three
categories: timestamp embedding, time-dependent entity embedding and deep temporal representation.
Timestampembedding(TE)modelslearnrepresentationforeachdiscretetimestamp.TTransELeblayandChekol
(2018) is an example, which extends TransE by adding one more embedding function mapping timestamps to hidden
representations.Thiskindofembeddinghasseverallimitationssinceitleadstomoresyntheticrelationsthannecessary
in the KG. Other models such as HyTE Dasgupta et al. (2018) explored projections. HyTE incorporates time in the
entity-relation space by associating each timestamp with a corresponding hyperplane.
Time-dependent entity embedding (TEE) models are built on taking time and the entity as inputs to the entity
embedding function and providing a hidden representation, that incorporates time, as an output. Such models include
DE-SimplE Goel et al. (2020), which was inspired by the success of the diachronic word embeddings, and AtiSe Xu
etal.(2020a),whichincorporatestemporalinformationintoentity/relationrepresentationsbyusingadditivetimeseries
decomposition. Other models such as TeRo Xu et al. (2020b), 3DRTE Wang et al. (2020) and RotateQVs Chen et al.
(2022) used rotations to incorporate time in the entity-relation embedding. TeRo applies this in the complex space
whereas 3DRTE and RotatQVS do the same in the quaternion space.
Using deep temporal representation (DTR) learning to integrate time was also an important direction that certain
studies have taken. García-Durán et al. (2018) utilized recurrent neural networks (RNN) to incorporate temporal
informationintotherelationrepresentationsofDistMultandTransE.Byfeedingtimecharactersandthestaticrelation
embedding to an LSTM, the model learns a temporal embedding for each relation.
Y. Fettach et al.:Preprint submitted to Elsevier Page 3 of 16

2.4. Time series forecasting vs. TKG link forecasting
There is a distinction between time series forecasting and TKG forecasting. Time series forecasting entails the
predictionoffuturemeasuresfrompastmeasuresChenetal.(2024),whileTKGforecastingisthetaskoflearningthe
temporaldynamicsandhowtheyaffectthesemanticsofTKGentitiesandrelationsDuetal.(2023).Specifically,intime
series forecasting time is used as an index to the observations of a measure to order them sequentially, while in TKG
forecasting it is considered a feature and its influence on the semantics of the TKG is modelled directly. From another
perspective, TKG forecasting is a self-supervised task, while time series forecasting is a supervised task, meaning
that time series forecasting requires the existence of high-quality supervision data to work, which can be a limiting
factor in the case of job/skill demand forecasting since they are significantly sparse Chen et al. (2024). However, by
directly modelling the temporal dynamics of entities and relations, TKG forecasting surpasses the inherent sequential
limitations of forecasting approaches and the need for supervised measures. In addition, since time series forecasting
andTKGforecastingsolvetotallydifferenttasksunderdifferentassumptions,comparingtheseapproachesispointless
and can’t be done practically.
3. Methodology
Inthissection,webrieflygothroughthepipelineofJobEdKGFettachetal.(2024)constructionbeforeweexplain
the temporal KG embedding methods we experimented with.
3.1. Data: JobEdKG
We constructed JobEdKG Fettach et al. (2024) using online job postings and courses. We compiled job postings
fromtheMoroccanwebsiteRekrute.com 2,spanningfromNovember2005toSeptember2022.Eachjobpostinginour
datasetincludesvariousdetailssuchasthejobtitle,cognitive(hard)andnon-cognitive(soft)skillsrequired,thehiring
company,theeconomicsectorassociatedwiththejob,thejob’slocation,educationalprerequisites,requiredexperience,
contract type, job function, posting date, and expiration date. To ensure data accuracy and prevent duplicate entries,
we used unique identifiers from recruiter companies found on the website. We retained only those job postings that
offeredpositionswithinMoroccancities.Thefinaldatasetconsistsof99,676jobpostings,encompassingbothEnglish
and French content. Additionally, we collected Massive Open Online Courses (MOOCs) from Coursera using the
website’sAPI.TheresultingMOOCdatasetcomprisesatotalof10,180courses,featuringcoursenames,descriptions,
specializations, and instructor information.
In order to extract hard skills from the different job postings and course descriptions we opted for a rule-based
approach that uses existing databases of hard skills and extracts skills using the Spacy library rule mining module3.
We extracted hard skills in both French and English. For the hard skills mentioned in English, we used an existing set
of rules from Jobzilla4. For the hard skills mentioned in French, we constructed our own set of rules based on the
ESCO 5 and ROME6 hard skills datasets.
For the rule-building process from raw skills data, for each hard skill, we applied an exact word-building process
and a POS (Part-of-speech) tagging-based process. After extracting the hard skills using the rules, we identify the
incompleteness of a significant number of them, so we apply sentence filtering using the TextAttack model7. Seeing
that this model is trained on English data, we translated the extracted skills using two translators: Argos translator8
and a transformer-based translator9. After translating the skills, we use the pre-trained TextAttack model to identify
if the sentence (skill in our case) is complete or not in addition to quantifying the degree of their completeness with
an acceptability score Fettach et al. (2024). Relations are extracted based on the co-occurrence of different types of
entities in the same job offer or the same course. For example, if a job offer describes a job title belonging to a certain
sector, then that job title and sector are linked. The outcomes of skill entity recognition were combined with relation
extraction to create a dataset that includes hard skills, soft skills, economic sector, recruiter company, function, and
courses for each job title.
2https://www.rekrute.com/
3https://spacy.io/usage/rule-based-matching
4https://github.com/pandmi/jobzilla_ai
5https://esco.ec.europa.eu
6https://www.pole-emploi.fr/employeur/vos-recrutements/le-rome-et-les-fiches-metiers.html
7https://huggingface.co/textattack/roberta-base-CoLA
8https://github.com/argosopentech/argos-translate
9https://huggingface.co/Helsinki-NLP/opus-mt-fr-en
Y. Fettach et al.:Preprint submitted to Elsevier Page 4 of 16

Entity types Number of nodes
Job titles 9736
Hard skills 32824
Soft skills 21
Courses 10180
Locations 35
Recruiters 2714
Sectors 133
Functions 75
Table 1
Entity types and number of nodes of T-JobEdKG
JobEdKGwasconstructedasanuncertainKG,meaningeachlinkbetweenthenodeshasascoreofuncertaintybut
for this work, we don’t consider these scores and we focus on the timestamps for each link that indicates the validity
of the fact at a certain time point so for example if the job "manager" required the skill "Excel" in the timestamp
"11/11/2006" that link would be present in the KG starting that time. To create some sort of differentiation between
the temporal JobEDKG and JobEDKG. We refer to the knowledge graph in this paper by T-JobEDKG.
Since the source data is well structured we didn’t need to apply advanced entity resolution techniques. For job
titles, we used fuzzy matching of job titles, such that if two job title names Levenshtein distance Navarro (2001) is
below a threshold they are considered similar. For all the other entities we used exact matching. We were able to use
exact matching in entities such as courses, companies, and soft skills because they are standardised from the source
websites. In the case of hard skills, the extraction process is rule-based and it maps the extracted hard skills to a finite
set of hard skills from the ESCO and ROME datasets. Consequently, we were able to use exact matching for entity
resolution.
The knowledge graph (KG) resulting from the process outlined in Figure 1 and discussed in the previous section
comprises a total of 55718 nodes. The number of nodes for each entity type is showcased in Table 1. These nodes are
interconnected by a network of 1296374 relations across 12 distinct types. The metamodel for our KG is in Figure 2.
Thelocationentitiescorrespondtothecitieswherecompaniesthatpostedjoboffersaresituated.Recruiters’entities
denotethenamesofthecompaniesthatpostedthejoboffers,whilesectornodesrepresenttheeconomicsectorsfeatured
on the Rekrute website. The relationships established between job titles and entities of the mentioned types convey
semantic significance. These relationships fall under the ’belongs_to’ relationship type, connecting job titles as the
primaryentitiestothecompaniesasthesecondaryentities.Thissignifiesthejob’sassociationwithaspecificcompany.
The’requires’relationlinksjobsasprimaryentitiestotheskillsassecondaryentities,indicatingtheskillsnecessary
foraparticularjob.The’located’relationassociatesjobsasprimaryentitieswithlocationsassecondaryentities,while
the ’has’ relation connects job titles as primary entities to their respective functions.
Other relation types link skills to one another, such as ’co_occurs_with,’ which establishes connections between
skill entities based on their co-occurrence in the same job offer, or to different types of entities, like ’acquired_by,’
whichconnectsskillsasprimaryentitiesandcoursesassecondaryentities.The’provides’relationassociatesMOOCs
as primary entities with skills as secondary entities to convey the skills offered by a specific course, while the ’favors’
relation links MOOCs as primary entities with job titles as secondary entities, indicating preferences or affinities
between them.
Data collection Data processing
Job Ads
MOOCs
Skill entity
recognition Triple extraction Confidence scoring T-JobEdKG
Figure 1: Overview of the methodology for building T-JobEdKG
Y. Fettach et al.:Preprint submitted to Elsevier Page 5 of 16

co-occurs_with
Soft skill
needed_for
co-occurs_with
acquired_by
Hard skill
locates
Location
needs
Recruiter
provides
favors Course
has
Sector
requires
requires
needed_for
is_located
belongs_to
belongs_to has
requiresJob title
co-occurs_with
co-occurs_with
by
co_occurs_with
Function
co_occurs_with
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
DD/MM/YYYY
Figure 2: Metamodel of T-JobEdKG. DD/MM/YYYY stands for the timestamps associated with links (day, month, year)
3.2. Temporal KG Link Prediction
Temporal KG forecasting predicts future links based on past facts. Practically, it implies predicting the tail𝑡based
on a question(ℎ,𝑟𝑞, ?,𝜏𝑞) and the previous facts𝜏𝑞, where𝑟𝑞,𝜏𝑞 denote the relation and timestamp of the question.
Temporal KG forecasting involves ranking all entities of the specific timestamp and obtaining the most likely links
given the timestamp. We present the preliminaries for this as follows:
Temporal KG. Suppose that, , and represent the entity set, relation set, and timestamp set, respectively. The
temporal KG is a collection of quadruples, which can be expressed as
 = {(ℎ,𝑟,𝑡,𝜏 ),ℎ,𝑡 ∈ ,𝑟 ∈ ,𝜏 ∈  } (1)
(ℎ,𝑟,𝑡,𝜏 )denotesaquadruple; ℎand𝑡representtheheadandtail,respectively. 𝑟representstherelation,and 𝜏represents
the time that the quadruple occurs.
The task of temporal KG forecasting. Suppose that facts happening before the selected time𝜏𝑘 can be expressed
as
𝜏𝑘 = {(ℎ𝑚,𝑟,𝑡 𝑛,𝜏𝑖) ∈ |𝜏𝑖<𝜏 𝑘} (2)
Temporal KG link prediction is the task of predicting missing links from existing ones. To achieve that we embed
entities and relations to low dimensional representation space and transform those structural representations using
Y. Fettach et al.:Preprint submitted to Elsevier Page 6 of 16

Positive Triples
𝒯
Negative triples
𝒯′
JobEd KG
𝒢=  ℎ,𝑟,𝑡,𝜏 𝑖 𝑖

Negative
Sampling
Forward
Backpropagation
Embedding
layer
Score
function
𝑓 ℎ,𝑟,𝑡,𝜏

Loss function
ℒ=   max 0,𝛼−𝑓 ℎ,𝑟,𝑡,𝜏
 ℎ′,𝑟′,𝑡′,𝜏′ ∈𝒯′ ℎ,𝑟,𝑡,𝜏 ∈𝒯
+𝑓 ℎ′,𝑟′,𝑡′,𝜏′

Score function
𝑓 ℎ,𝑟,𝑡,𝜏
Entities embedding
 𝒉,𝒕
Relation embedding 𝒓
 ℎ,𝑟,𝑡,𝜏
Training
Inference
Entities embedding
 𝐡,𝐭
Relation embedding 𝐫
Temporal Entities embedding
 𝒉𝝉,𝒕𝝉
Temporal Relation embedding
𝒓𝝉
Temporal Entities embedding
 𝒉𝝉,𝒕𝝉
Temporal Relation embedding
𝒓𝝉
Figure 3: Training and inference on temporal KGs. The model is trained on triples with timestamps. It learns temporal
embeddings to rank correct triples higher than incorrect ones. After training, it can predict missing or future relations.
temporal information to obtain temporal embeddings of entities or/and relations. These embeddings are then fed to
a scoring function to obtain the likelihood of the existence of a relation between the two entities given the time
of observation. Figure 3 summarizes the temporal KG link prediction training and inference process. The process
starts with training, where the model is provided with triples in the form of (head, relation, tail, timestamp). During
training,themodellearnstemporalembeddingsforentitiesandrelationsbyoptimizingascoringfunctionthatsampled
via negative sampling, which ranks the correct triples higher than incorrect (negative) triples. Temporal aspects are
integrated through methods such as time-aware embeddings (DE-TransE, DE-DistMult) or recurrent models (TA-
TransE,TA-DistMult)thataccountforchangesinrelationshipsovertime.Oncetrained,themodelundergoesinference
on unseen data. Given a query (e.g., predicting a future relation), the model generates predictions by ranking possible
tailsfora(head,relation)pairorpredictingmissingrelations.Inwhatfollowsthedetailtheapproachesusedtoembed
the temporal KG.
3.2.1. Embedding layer
Theobjectiveoftheembeddinglayeristorepresententitiesandrelationsinalow-dimensionalspacethatpreserves
the semantic and structural properties of the KG. This work explores multiple approaches that incorporate temporal
information in entity and relation embeddings. Goel et al. (2020) follows TEEs, by embedding entities and relations
in ℝ𝑑. Entities are embedded by having a portion being structurally dependent and a portion ofthe embedding is time
dependent as follows: the embedding𝐳𝜏 𝑒 of an entity𝑒is defined as
𝐳𝜏 𝑒 [𝑛] =
{
𝐚𝑒[𝑛]𝜎(𝐰𝑒[𝑛]𝜏 + 𝐛𝑒[𝑛]) if 1 ≤𝑛 ≤𝛾𝑑
𝐚𝑒[𝑛] if𝛾𝑑 <𝑛 ≤𝑑
where 𝐚𝑒 ∈ ℝ𝑑, 𝐰𝑒, 𝐛𝑒 ∈ ℝ𝛾𝑑 are entity specific embeddings,𝜎 is an activation function,0 ≤ 𝛾 ≤ 1 is a hyper-
parameter that controls the percentage of temporal features. García-Durán et al. (2018) follows DIR by incorporating
temporal information in the relation embedding. This is done by extending a relation𝑟 to a sequence𝑟𝑠𝑒𝑞, which
contains𝑟 along a sequence that represents time𝜏 as follows:𝑟𝑠𝑒𝑞 = (𝑟,𝑇 1𝑦,𝑇 2𝑦,𝑇 3𝑦,𝑇 4𝑦,𝑇 1𝑚,𝑇 2𝑚,𝑇 1𝑑,𝑇 2𝑑), where
the suffixes𝑦,𝑚, and𝑑 indicate whether the digit corresponds to the year, month, or day information. Let𝐫𝑠𝑒𝑞 ∈ ℝ𝑑
be the embedding of𝑟𝑠𝑒𝑞. In order to obtain𝐫𝑠𝑒𝑞 each token of the sequence𝑟𝑠𝑒𝑞 is first mapped to its corresponding
𝑑-dimensional embedding and the resulting sequence of embeddings used as input to the LSTM.𝐫𝑠𝑒𝑞 is presented by
the last hidden state of the LSTM. More recently, Xu et al. (2020b) proposed Tero, an approach that uses the complex
embeddingspace.Complexspaceapproacheshaveachievedstate-of-the-artperformanceinTKGembedding.InTero
each element of a triple(ℎ,𝑟,𝑡,𝜏 ) is represented by a complex vector𝐡, 𝐫, 𝐭,𝜏 ∈ ℂ𝑑. To obtain time-aware head and
Y. Fettach et al.:Preprint submitted to Elsevier Page 7 of 16

tail representations Tero uses the Hamiltonian product:
𝐳𝜏 ℎ = 𝐡◦𝜏 ; 𝐳𝜏 𝑡 = 𝐭◦𝜏 (3)
3.2.2. Scoring function
The objective of a score function is to quantify the likelihood of two entities being linked via a relation. There are
multiple classes of scoring functions in the literature that achieve that: mainly we have distance-based and semantic
scoring functions. Distance-based scoring functions evaluate the plausibility of a triple by measuring the distance
between transformed entity embeddings in the vector space. The goal is to make the embeddings of related entities
closetoeachotherafterapplyingarelationtransformation.Examplesofdistance-basedmodelsincludeTransEandits
variants.Semanticscoringfunctionsevaluatetheplausibilityofatriplebyusinginteractionsorsimilaritiesbetweenthe
embeddingsoftheentitiesandtherelation.Thesefunctionsofteninvolvemultiplicativeoradditiveinteractionsamong
the embeddings. Examples include DistMult, ComplEx, and RESCAL. In our case, we choose a scoring function for
each class: TransE is distance-based while DistMult is semantic.
The previously presented temporal embeddings of relations and entities are used in different scoring functions to
calculate the likelihood of a fact. These scoring functions are an extension of the TransE Bordes et al. (2013) and
the DistMult Yang et al. (2015) scoring function, which can be described as follows for a fact(ℎ,𝑟,𝑡 ) 𝑓 (ℎ,𝑟,𝑡 ) =
||𝐡 + 𝐫 − 𝐭||2 2 and𝑓 (ℎ,𝑟,𝑡 ) = 𝐡⊤⋅ (𝐫⊙ 𝐭) respectively where𝐡, 𝐫, 𝐭 ∈ ℝ𝑑 are embeddings ofℎ,𝑟, and𝑡 respectively. We experimented with the following scoring functions: let𝐳𝜏 𝑒 be the temporal embedding of an entity𝑒 at time𝜏, 𝐫 is
the static embedding of relation𝑟, 𝐫𝜏 is the dynamic embedding of relation𝑟, 𝐡and 𝐭 are static embeddings ofℎand𝑡
respectively.
• DE-TransE Goel et al. (2020):
𝑓 (ℎ,𝑟,𝑡,𝜏 ) = ||𝐳𝜏 ℎ + 𝐫 − 𝐳𝜏 𝑡||2 2 (4)
• DE-DistMult Goel et al. (2020):
𝑓 (ℎ,𝑟,𝑡,𝜏 ) = ( 𝐳𝜏 ℎ)⊤⋅ (𝐫⊙ 𝐳𝜏 𝑡 ) (5)
• TA-TransE García-Durán et al. (2018):
𝑓 (ℎ,𝑟,𝑡,𝜏 ) = ||𝐡 + 𝐫𝑠𝑒𝑞 − 𝐭||2 2 (6)
• TA-DistMult García-Durán et al. (2018):
𝑓 (ℎ,𝑟,𝑡,𝜏 ) = ( 𝐡)⊤⋅ (𝐫𝑠𝑒𝑞⊙ 𝐭) (7)
• Tero Xu et al. (2020b):
𝑓 (ℎ,𝑟,𝑡,𝜏 ) =∥ 𝐳𝜏 ℎ + 𝐫 −̄𝐳𝜏 𝑡 ∥ (8)
where⋅ is the dot product and⊙is the element-wise product.̄𝐳 is the conjugate of𝐳 ∈ ℂ𝑑.
3.2.3. Training objective
We trained the previously mentioned models using the Adam optimizer, to minimize the triplet loss:
 =
∑
(ℎ,𝑟,𝑡,𝜏)∈
∑
(ℎ′,𝑟′,𝑡′,𝜏′)∈Neg(ℎ,𝑟,𝑡,𝜏,,𝑛)
max{0,𝛼 −𝑓 (ℎ,𝑟,𝑡,𝜏 ) +𝑓 (ℎ′,𝑟 ′,𝑡 ′,𝜏 )} (9)
with 𝛼 is the margin hyperparameter, Neg is the negative sampling function, which generates𝑛 negative for each
quadruple (ℎ,𝑟,𝑡,𝜏 ) ∈  . In our experiments, we employed a random uniform negative sampling strategy where
either the head or the tail of a fact is replaced with a random entity to generate a ransom fact Bordes et al. (2013).
Y. Fettach et al.:Preprint submitted to Elsevier Page 8 of 16

3.2.4. Evaluation metrics
After training the model using the training objective, the model needs to be adequately evaluated on the temporal
link prediction task. In order to do so we use existing metrics from literature Goel et al. (2020). For a a dynamic fact
(ℎ,𝑟,𝑡,𝜏 )fromthetestset 𝑡𝑒𝑠𝑡 wecreatetwoqueries:1- (ℎ,𝑟, ?,𝜏 )and2- (?,𝑟,𝑡,𝜏 ).Forthefirstquery,werankallthe
entities using the scoring function. For each quadruple(ℎ,𝑟,𝑡,𝜏 ), we first take(?,𝑟,𝑡,𝜏 ) as the query and obtain the
filtered rank on the head:
rankℎ = ||| {𝑒 ∈  ∶ (𝑓 (𝑒,𝑟,𝑡,𝜏 ) ≥𝑓 (ℎ,𝑟,𝑡,𝜏 )) ∧ ((𝑒,𝑟,𝑡,𝜏 ) ∉ 𝑡𝑟𝑎𝑖𝑛 ∪ 𝑣𝑎𝑙)}||| + 1
Next, we take(ℎ,𝑟, ?,𝜏 )) as the query and obtain the filtered rank on the tail:
rank𝑡 = ||| {𝑒 ∈  ∶ (𝑓 (ℎ,𝑟,𝑒,𝜏 ) ≥𝑓 (ℎ,𝑟,𝑡,𝜏 )) ∧ ((ℎ,𝑟,𝑒,𝜏 ) ∉ 𝑡𝑟𝑎𝑖𝑛 ∪ 𝑣𝑎𝑙)}||| + 1
The following metrics are computed from both the head and tail ranks on all quadruples : (i) Mean reciprocal ranking
(MRR):
𝑀𝑅𝑅 = 1 2|𝑡𝑒𝑠𝑡| ∑ (ℎ,𝑟,𝑡,𝜏)∈𝑡𝑒𝑠𝑡
(
1
rankℎ
+ 1 rank𝑡
)
. (ii)𝐻@𝑘: ratio of ranks no larger than𝑘, i.e.,
𝐻@𝑘 = 1 2|𝑡𝑒𝑠𝑡| ∑ (ℎ,𝑟,𝑡,𝜏)∈𝑡𝑒𝑠𝑡 (𝕀(rankℎ ≤𝑘) + 𝕀(rank𝑡 ≤𝑘))
where 𝕀(𝑎) = 1 if𝑎 is true, otherwise0. (iii)𝑀𝑅: mean rank:
𝑀𝑅 = 1 2|𝑡𝑒𝑠𝑡| ∑ (ℎ,𝑟,𝑡,𝜏)∈𝑡𝑒𝑠𝑡 (rankℎ +rank𝑡 )
The larger the𝑀𝑅𝑅 or𝐻@𝑘, the better the embedding. The smaller the𝑀𝑅, the better the embedding.
4. Results
4.1. Implementation details
We conducted experiments on four 12GB GPUs. The code that we implemented is based on the TorchKGE
library, which we adapted to accommodate temporal knowledge graphs. We were motivated to implement our
version since the original implementations for the models were "prohibitively" slow. We made this library publicly
availableat https://github.com/BahajAdil/TempTorchKGE.Inaddition,thesourcecodeisavailableat https:
//shorturl.at/divxC, which is part of the larger JobEd projecthttps://github.com/BahajAdil/JobEd.
4.2. Experimental Setup
The aim is to compare the performances of different scoring functions on the T-JobEdKG knowledge graph for
the task of temporal link prediction. We conducted a grid search using multiple hyperparameters. For the two models,
thefollowinghyper-parameterspaceswereused:learningrate: (0.01, 0.001, 0.0001),numberofnegativesperpositive
example: (10, 30, 40),margin: (1, 5, 10, 20),embeddingdimension: (50, 100, 150, 200).Wefixedthebatchsizeto2000.
For diachronic embeddings, we experimented with two ratios for temporal representation(0.1, 0.2).
4.3. Performance Analysis
Tables 2 and 3 show the performance of different models on the task of temporal link prediction and the best-
performing hyperparameters. TA models have a compatible performance with each other in the same way DE models
have, demonstrating the limited advantage of changing the scoring function on this task. DistMult improved upon
the performance of TransE in TA and DE settings. The TA model family outperformed DE model family. The best-
performing model in TA-DistMult. We think that various factors explain why TA is better than DE even though DE is
themorerecentmodelandperformsbetterthanTAinvariousbenchmarkdatasets.Inwhatfollowswegivethesefacts
and our interpretation:
Y. Fettach et al.:Preprint submitted to Elsevier Page 9 of 16

Model Hit@1 hit@3 hit@10 MRR
DE-DistMult 54.82 70.54 91.37 65.79
DE-TransE 48.49 58.30 71.40 56.07
TA-TransE 61.26 79.56 90.08 71.65
Tero 48.15 49.53 50.82 49.17
TA-DistMult 61.77 84.53 95.08 74.20
Table 2
The evaluation metrics of the best performing models (%).
Model lr emb_dim margin n_neg s_rep_ratio
DE-DistMult 0.0010 100 1 10 0.1
DE-TransE 0.0001 100 1 40 0.1
TA-DistMult 0.0010 50 1 10 -
Tero 0.001 200 10 100
TA-TransE 0.0010 50 20 30 -
Table 3
The optimal hyperparameters for the different models. lr is the learning rate, emb_dim is the embedding dimension, n_neg
is the number of negative examples per positive, s_rep_ratio is the ratio of temporal features.
• Time-awareentityvs.relationembedding:TAincorporatesthetimeelementintherelationtohaveatime-aware
relation embedding. DE and Tero incorporate the time element in the head and tail entities to have time-aware
head and tail embedding. Consequently, TA models relations change with time while DE and Tero model the
changes of entities’ semantics with time. Our task is related to job/skill demand and not some task where the
meaning/semantics of skills or any other entity change (job transitioning, skill repurposing etc). This explains
why TA models performed significantly better in this task.
• Model complexity: TA models have a much higher computational complexity than DE models. In DE, time-
aware entity embeddings are created as a function of the raw timestamps. At the same time, TA embeds each
element of the timestamp into a low dimensional representation space which is then fed to an LSTM (giving it
evenmoreweights).Giventheknownphenomenonofbias-variancetrade-offandsinceTAmodelscontainmore
variance they tend to be more adept for larger TKGs (more bias), while DE models and Tero are more adequate
for sparser and smaller TKGs.
• Real embedding space vs. complex embedding space: Another distinctive characteristic along which we can
comparetheresultsistheembeddingspace.TheTeromodelrepresentsembeddingsinthecomplexspacewhile
DE and TA models represent their entities and relations in the real space. From the results, it seems that real
embeddingspacegivesbetterresults.Thismaybeattributedtotherotationoperationsperformedinthecomplex
space, which can "overshoot" entity representations in a denser representation space, resulting in entangled
representations. This is exactly the case of our KG, which is composed of a larger amount of facts, entities and
relations than the standard benchmarks.
4.4. Scalability and Convergence Speed
To embed our knowledge graph we use a framework that we implemented called TempTorckKGE10, which is an
adaptation of TorchKGE Boschin (2020) for temporal knowledge graphs. TempTorckKGE takes advantage of bulk
matrixoperationsinsteadofsingletripleoperationstocalculatethescores,whichmakesitsignificantlymoreefficient
thantheoriginalimplementationsofthemodelsthatweusedandothermorerecentmodels(e.g.TeRoXuetal.(2020b),
Atise Xu et al. (2019)).
10https://github.com/BahajAdil/TempTorchKGE
Y. Fettach et al.:Preprint submitted to Elsevier Page 10 of 16

4.5. Case study of relation inference
Toevaluatetheinferencecapabilitiesofthemodelonunseenjob-skillpairswegeneratedallpossiblefactsbetween
skills and specific job titles, then we removed from those facts all the facts that were seen during training. Time range
wasaddedtotheresultingfactsandfedtoTA-DistMulttoobtainfactualityscores.Tovisualizethesescoresdistinctively
we focused on a few skills in figures 4, 5, 6, 7.
Figures4and5showcasethetemporalevolutionoftheskills"dataanalysis"and"Java"respectivelyoveraspecified
time period (from January 1, 2010, to January 1, 2025). We calculate each data point by averaging all the skill scores
atacertaintimestamp.Theplotsdisplaythetemporalevolutionoftheaveragescoreforthe"dataanalysis"and"Java"
skills. The x-axis represents the date (timestamps generated quarterly between 2010 and 2025), and the y-axis shows
the average score, which indicates the strength or relevance of the "data analysis" and "Java" skills in relation to the
selectedjobtitleovertime.Theseplotshelptrackhowthesetwoskillsevolveinimportanceordemandovertheyears,
according to the model’s scores. The line shows a temporal trend, which may reveal periods of increased or decreased
importance. A highlighted range, from January 1, 2023, to January 1, 2025, is framed in red. This showcases the
inference of our model on unseen timestamps. We see that the skill of data analysis is highly sought after in 2023
however, it starts to see a decline in 2024. Java on the other hand continued to see a decline since 2022.
We also plot the inferred scores of skills of the job "Production Leader" throughout the years in Figure 6. Cooler
colorsrepresentlowervaluesofthescoreaveragesThissignalsaregionofminimaloccurrenceandrelevance.Warmer
colours represent higher values of the score averages indicating a high-importance region of the skill at a certain
timestamp. We see that skills such as teamwork (travail d’équipe) have been consistently high from 2011 until 2024.
Other skills like risk management (gérer less risques) started being less sought after in 2023. The job "Consulting
EngineerinITmanagement"(Figure7)isstartingtofocuslesson"managementsystems"(systèmedegestion)starting
31-01-2023.
Figure 4: Temporal evolution of the "data analysis" skill for the job "Consulting Engineer in IT Management". The red
square showcases the prediction of our model for the time range between 01-01-2023 and 01-01-2025.
4.6. Hyperparameter analysis
In this section, we explore the effects of different hyperparameter settings on the different models. Figures 8, 9
and10showhowmodelsperformonaverageunderdifferentsettingsofnegativeexamples,batchsizeandembedding
dimension respectively. We observe that a higher number of negative examples generally increases the performance
of the models. This can be attributed to the fact that negative examples play a role in regularisation and hence can
reduce overfitting and improve generalization. Increasing the batch size also increases the performance of various
models. Batch size also regularizes by counteracting the inherent variance of the models through the incorporation
of more bias. We notice that increasing the embedding dimension generally increases the performance but not to the
Y. Fettach et al.:Preprint submitted to Elsevier Page 11 of 16

Figure 5: Temporal evolution of the "Java" skill for the job "Consulting Engineer in IT Management". The red square
showcases the prediction of our model for the time range between 01-01-2023 and 01-01-2025
Figure 6: Heatmap showcasing the top skills for the job "Production Leader" and their level of importance through the
years.
same extent as the number of negative examples and the batch size. This shows that negative sampling and batch size
significantly influence model performance compared to the embedding dimension.
Y. Fettach et al.:Preprint submitted to Elsevier Page 12 of 16

Figure 7: Heatmap showcasing the top skills for the job "Consulting Engineer in IT Management" and their level of
importance through the years.
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
DE-DistMult
DE-TransE
TA-DistMult
TA-TransE
model_name
0.461515
0.210534
0.474673
0.315019
0.49191
0.223418
0.423241
0.358579
0.500902
0.223915
0.584757
0.571214
n_neg
10
30
40
Figure 8: The average filtered MRR performance of different models on the test set using various numbers of negative
examples (n_neg).
5. Discussion
In this paper, we use temporal knowledge graph embeddings to predict skill demand in the Moroccan job market.
We formulate the skill need prediction problem as a link forecasting problem. We experiment with several temporal
KG embedding models to achieve this task based on diachronic embeddings (DE models) and LSTM (TA models).
We hypothesise that the performance of the TA models is better than the DE models due to the size and completeness
of the KG. In fact, the TA approach encodes each element of the𝐫𝑠𝑒𝑞 in order and feed it to an LSTM to obtain𝐫𝑠𝑒𝑞 as
opposed to DE which splits the embedding of entities to contain temporal and structural information. Consequently,
Y. Fettach et al.:Preprint submitted to Elsevier Page 13 of 16

0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
DE-DistMult
DE-TransE
TA-DistMult
TA-TransE
model_name
0.453239
0.207396
0.422867
0.31259
0.529618
0.234735
0.500334
0.373684
b_size
2000
4000
Figure 9: The average filtered MRR performance of different models on the test set using various batch sizes (b_size).
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
DE-DistMult
DE-TransE
TA-DistMult
TA-TransE
model_name
0.480327
0.213998
0.443174
0.313576
0.496998
0.222814
0.464717
0.363985
0.490076
0.225926
0.474781
0.431666 emb_dim
50
100
150
Figure 10: The average filtered MRR performance of different models on the test set using various batch sizes (emb_dim).
TAhasasignificantlyhighernumberofparameterswhichmaycauseoverfittingespeciallyinsmallerKGs.Inourcase,
JobEDKG is endowed with significant richness in terms of concepts, concept types and facts, which made it suitable
for modelling using an overparameterized model (i.e. TA). This phenomenon is consistently measured and explored
in machine learning literature and is called the bias-variance tradeoff Briscoe and Feldman (2011)
Thepipelineproposedinthispaperholdspotentialvaluefororganizationsleveragingcurrentskillsdataforimplicit
forecasting. Many educational institutions, including community colleges and universities, use labour market data
providers like LinkedIn Talent Insights11 to shape their course selections and curricula. Subscribers could gain
advantages if these data providers integrate forecasting capabilities into their services.
Other organizations such as the National Center for O*NET Development, responsible for the U.S. Department
of Labor-sponsored Occupational Information Network (O*NET)12, ROME13 and ESCO14, all of which compile
occupation profiles. While these organisations already collaborate with data providers to monitor job posting data for
11https://business.linkedin.com/talent-solutions/talent-insights
12https://www.onetonline.org/
13https://www.francetravail.fr/employeur/vos-recrutements/le-rome-et-les-fiches-metiers.html
14https://esco.ec.europa.eu/en
Y. Fettach et al.:Preprint submitted to Elsevier Page 14 of 16

recent changes in skill demand, forecasts demonstrated in this paper could offer early warnings before skill demand
reaches a critical threshold.
Similarly, businesses operating in rapidly evolving technology sectors could find value in a skills forecasting
pipeline. To maintain a relevant workforce, these companies often grapple with deciding whether to lay off existing
workersandhirenewonesortoinvestinreskillingtheircurrentemployees.Layoffscanbechallengingforthoselosing
their jobs and detrimental to the morale of remaining employees, while hiring new workers incurs significant costs.
Reskilling, on the other hand, demands time, which companies often perceive as a luxury. Forecasts could provide
a time buffer for reskilling, enhancing workers’ well-being and improving labour market efficiency by preserving
established employer-employee matches.
6. Limitations and Future Directions
While this study provides valuable insights into using temporal KG embeddings for skill demand forecasting,
severallimitationsshouldbeconsideredwheninterpretingtheresults.Inwhatfollowswegivealistoflimitationsand
prospective future work to mitigate them:
• Advanced scoring functions:Ourworkdoesn’texploreotherscoringfunctionsotherthanTransEandDistMult.
This choice was further motivated by the computational complexity of the more sophisticated approaches and
the fact that the TA models gave satisfactory results that surpass what’s generally acceptable in literature by
publicbenchmarksasagoodperformance.Infuturework,weplanonexploringmoresophisticatedapproaches
to temporal KGE to design a temporal KGE model that’s adapted to job skill forecasting.
• Traditional time series: Incorporating time series data would also be an interesting direction to explore. We
intend on an extension of this approach that incorporates temporal KG embedding with traditional forecasting
to solve some traditional forecasting limitations, in this case, a comparison with other traditional forecasting
approaches will be conducted.
• Open-world extension:Thisworkisthefirstexploration oftheapplicabilityoftemporalKGembeddinginjob
skill forecasting. Consequently, we limit our problem to a closed world knowledge graph where we focus on a
fixed set of skills and jobs and how they interact semantically (e.g. is this skill that was never linked to a job
usefulforthisjob?)andtemporally(e.g.howisaskilldemandforajobevolvewithtime?).However,weintend
to explore the feasibility of working in an open world knowledge graph Shi and Weninger (2018) where we can
encounter unseen entities (jobs, skills, recruiters, sectors etc) and unseen relations among them or with seen
entities during training.
• Real-world integration: Integrating our model into real-world applications, such as labour market forecasting
andeducationalcurriculumdesign,presentsseveraltechnicalandoperationalchallenges.Onthetechnicalside,
issues like data interoperability, scalability, and real-time performance must be addressed to ensure the model
functionseffectivelywithdiverseandlarge-scaledatasources.Operationally,themodelwouldneedtobetailored
to specific domain requirements, such as adapting to evolving labour market trends and aligning educational
curricula with industry standards. Although this study focuses on validating the model within the JobEdKG
dataset, future research will explore these integration challenges, aiming to optimize the model for practical
deployment in dynamic environments.
7. Conclusion
Skill mismatch poses a significant challenge, adversely affecting recent graduates and, by extension, the global
economy. Our approach to associating skills with job titles is framed as a temporal link prediction problem. To tackle
this,weemployanadvancedtemporalknowledgegraphembeddingmodelknownforitsproficiencyinlinkprediction.
Utilizingthismodelallowsustodeducenewconnectionsbetweenentitieswithintheknowledgegraphandeventually
mitigate the skills gap, which can help students and workers pursue their professional pathways.
Y. Fettach et al.:Preprint submitted to Elsevier Page 15 of 16

CRediT authorship contribution statement
Yousra Fettach: Conceptualization, Software, Formal analysis, Investigation, Methodology, Writing - original
draft. Adil Bahaj:Software,Investigation,Methodology,Writing-originaldraft. Mounir Ghogho:Conceptualization,
Formal analysis, Project administration, Supervision, Validation, Writing - review & editing.
Declaration of Competing Interest
Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsorpersonalrelationshipsthatcouldhave
appeared to influence the work reported in this paper.
References
Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J., and Yakhnenko, O. (2013). Translating embeddings for modeling multi-relational data.
Advances in neural information processing systems, 26.
Boschin, A. (2020). Torchkge: Knowledge graph embedding in python and pytorch.arXiv preprint arXiv:2009.02963.
Briscoe, E. and Feldman, J. (2011). Conceptual complexity and the bias/variance tradeoff.Cognition, 118(1):2–16.
Cai,L.,Mao,X.,Zhou,Y.,Long,Z.,Wu,C.,andLan,M.(2024). Asurveyontemporalknowledgegraph:Representationlearningandapplications.
arXiv preprint arXiv:2403.04782.
Chan,A.P.,Chiang,Y.H.,Mak,S.W.,Choy,L.H.,andJames,M.(2006).Forecastingthedemandforconstructionskillsinhongkong. Construction
Innovation, 6(1):3–19.
Chao, W., Qiu, Z., Wu, L., Guo, Z., Zheng, Z., Zhu, H., and Liu, H. (2024). A cross-view hierarchical graph learning hypernetwork for skill
demand-supply joint prediction.arXiv preprint arXiv:2401.17838.
Chen, K., Wang, Y., Li, Y., and Li, A. (2022). Rotateqvs: Representing temporal information as rotations in quaternion vector space for temporal
knowledge graph completion.arXiv preprint arXiv:2203.07993.
Chen,X.,Qin,C.,Fang,C.,Wang,C.,Zhu,C.,Zhuang,F.,Zhu,H.,andXiong,H.(2024). Job-sdf:Amulti-granularitydatasetforjobskilldemand
forecasting and benchmarking.arXiv preprint arXiv:2406.11920.
Dasgupta,S.S.,Ray,S.N.,andTalukdar,P.(2018). Hyte:Hyperplane-basedtemporallyawareknowledgegraphembedding. In Proceedingsofthe
2018 conference on empirical methods in natural language processing, pages 2001–2011.
Dawson, N., Rizoiu, M.-A., Johnston, B., and Williams, M.-A. (2020). Predicting skill shortages in labor markets: A machine learning approach.
In 2020 IEEE International Conference on Big Data (Big Data), pages 3052–3061. IEEE.
deGroot,M.,Schutte,J.,andGraus,D.(2021). Jobposting-enrichedknowledgegraphforskills-basedmatching. arXivpreprintarXiv:2109.02554 .
Du,Z.,Qu,L.,Liang,Z.,Huang,K.,Cui,L.,andGao,Z.(2023). Imf:Interpretablemulti-hopforecastingontemporalknowledgegraphs. Entropy,
25(4):666.
Fettach, Y., Bahaj, A., and Ghogho, M. (2024). Jobedkg: An uncertain knowledge graph-based approach for recommending online courses and
predicting in-demand skills based on career choices.Engineering Applications of Artificial Intelligence, 131:107779.
Garcia de Macedo, M. M., Clarke, W., Lucherini, E., Baldwin, T., Queiroz Neto, D., de Paula, R. A., and Das, S. (2022). Practical skills demand
forecasting via representation learning of temporal dynamics. InProceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society,
pages 285–294.
García-Durán, A., Dumančić, S., and Niepert, M. (2018). Learning sequence encoders for temporal knowledge graph completion. InProceedings
of the 2018 Conference on Empirical Methods in Natural Language Processing, page 4816–4821.
Goel, R., Kazemi, S. M., Brubaker, M., and Poupart, P. (2020). Diachronic embedding for temporal knowledge graph completion. InProceedings
of the AAAI conference on artificial intelligence, volume 34, pages 3988–3995.
Han,Z.,Zhang,G.,Ma,Y.,andTresp,V.(2021).Time-dependententityembeddingisnotallyouneed:Are-evaluationoftemporalknowledgegraph
completion models under a unified framework. InProceedings of the 2021 Conference on Empirical Methods in Natural Language Processing,
pages 8104–8118.
Jaramillo, C. M., Squires, P., Kaufman, H. G., Da Silva, A. M., and Togelius, J. (2020). Word embedding for job market spatial representation:
tracking changes and predicting skills demand. In2020 IEEE International Conference on Big Data (Big Data), pages 5713–5715. IEEE.
Jia, S., Liu, X., Zhao, P., Liu, C., Sun, L., and Peng, T. (2018). Representation of job-skill in artificial intelligence with knowledge graph analysis.
In 2018 IEEE symposium on product compliance engineering-asia (ISPCE-CN), pages 1–6. IEEE.
Kwak, N., Garrett Jr, W. A., and Barone, S. (1977). A stochastic model of demand forecasting for technical manpower planning.Management
science, 23(10):1089–1098.
Lacroix, T., Obozinski, G., and Usunier, N. (2020). Tensor decompositions for temporal knowledge base completion. arXiv preprint
arXiv:2004.04926.
Leblay, J. and Chekol, M. W. (2018). Deriving validity time in knowledge graph. InCompanion Proceedings of the The Web Conference 2018,
pages 1771–1776.
Liu, L., Zhang, W., Liu, J., Shi, W., and Huang, Y. (2021). Learning multi-graph neural network for data-driven job skill prediction. In2021
International Joint Conference on Neural Networks (IJCNN), pages 1–8. IEEE.
Luo, H., Ma, S., Selvaraj, A. J. B., and Sun, Y. (2019). Learning job representation using directed graph embedding. InProceedings of the 1st
International Workshop on Deep Learning Practice for High-Dimensional Sparse Data, pages 1–5.
Navarro, G. (2001). A guided tour to approximate string matching.ACM computing surveys (CSUR), 33(1):31–88.
Y. Fettach et al.:Preprint submitted to Elsevier Page 16 of 16

Shi, B. and Weninger, T. (2018). Open-world knowledge graph completion. InProceedings of the AAAI conference on artificial intelligence,
volume 32.
Sibarani, E. M. and Scerri, S. (2020). Scodis: Job advert-derived time series for high-demand skillset discovery and prediction. InInternational
Conference on Database and Expert Systems Applications, pages 366–381. Springer.
Vaidya, D. M. and Dhruv, A. J. (2021). Data-science to predict entrepreneurial skills based on profession. In2021 International Conference on
Artificial Intelligence and Machine Vision (AIMV), pages 1–5. IEEE.
Wang, J., Zhang, W., Chen, X., Lei, J., and Lai, X. (2020). 3drte: 3d rotation embedding in temporal knowledge graph.IEEE Access, 8:207515–
207523.
Wang, Q., Mao, Z., Wang, B., and Guo, L. (2017). Knowledge graph embedding: A survey of approaches and applications.IEEE transactions on
knowledge and data engineering, 29(12):2724–2743.
Ward, D. (1996). Workforce demand forecasting techniques.Human Resource Planning, 19(1):54–56.
Wolf, V., Neubürger, F., and Lanwehr, R. (2023). Generating synthetic data for better prediction modeling in skill demand forecasting. In2023
IEEE World Conference on Applied Intelligence and Computing (AIC), pages 313–318. IEEE.
Woolard, I., Kneebone, P., and Lee, D. (2003). Forecasting the demand for scarce skills, 2001-2006.Human resources development review, pages
458–474.
Xu, C., Nayyeri, M., Alkhoury, F., Yazdi, H., and Lehmann, J. (2020a). Temporal knowledge graph completion based on time series gaussian
embedding. InInternational Semantic Web Conference, pages 654–671. Springer.
Xu, C., Nayyeri, M., Alkhoury, F., Yazdi, H. S., and Lehmann, J. (2019). Temporal knowledge graph embedding model based on additive time
series decomposition.arXiv preprint arXiv:1911.07893.
Xu, C., Nayyeri, M., Alkhoury, F., Yazdi, H. S., and Lehmann, J. (2020b). Tero: A time-aware knowledge graph embedding via temporal rotation.
arXiv preprint arXiv:2010.01029.
Yang, B., Yih, S. W.-t., He, X., Gao, J., and Deng, L. (2015). Embedding entities and relations for learning and inference in knowledge bases. In
Proceedings of the International Conference on Learning Representations (ICLR).
Yazdanian, R., Davis, R. L., Guo, X., Lim, F., Dillenbourg, P., and Kan, M.-Y. (2022). On the radar: Predicting near-future surges in skills’ hiring
demand to provide early warning to educators.Computers and Education: Artificial Intelligence, 3:100043.
Y. Fettach et al.:Preprint submitted to Elsevier Page 17 of 16
