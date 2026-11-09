---
title: 'Generative AI Use Cases In Real Estate Marketing: Adoption and Constraints in Germany'
url: https://arxiv.org/abs/2609.12684
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Victor Kolominsky-Rabas
- Leopold Müller
- Felicia Perpina
- Niklas Kühl
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.12684
pages: 10
chars: 44858
fetched_at: '2026-11-08T13:19:55+00:00'
kb_version: 1
---

# Generative AI Use Cases In Real Estate Marketing: Adoption and Constraints in Germany

GENERATIVEAI USECASESINREALESTATEMARKETING:
ADOPTION ANDCONSTRAINTS INGERMANY
PREPRINT
Victor Kolominsky-Rabas*1,2, Leopold Müller1,2, Felicia Perpina1, and Niklas Kühl1,2
1University of Bayreuth, Universitätsstraße 30, 95447 Bayreuth, Germany
2Fraunhofer FIT, Wittelsbacherring 10, 95444 Bayreuth, Germany
ABSTRACT
Generative artificial intelligence (GenAI) is changing how work is organized and performed. Real
estate marketing is a prime example of this, yet evidence of GenAI in real estate agents’ day-to-day
practice remains scarce. In this work, we report on our insights from a German-based empirical
study with eleven semi-structured interviews. GenAI is already utilized across different activities,
with marketing communication being the most prominent. Concrete use cases are emergent and
unevenly adopted, with writing exposé texts being the only widely established one. Interaction is
predominantly human-in-the-loop: GenAI drafts, structures, and retrieves, while real estate agents
curate, verify, and decide. Constraints stem less from model capability than from integration with
listings and documents, data availability, and compliance in sensitive tasks. The study contributes a
grounded map of existing and potential use cases and identifies tentative practical implications for
adoption.
KeywordsGenerative AI·real estate marketing·work transformation
1 Introduction
Generative artificial intelligence (GenAI) has become widely accessible in everyday and professional work [ 33].
Reported benefits include creativity support, fewer errors, and productivity gains across sectors [ 11, 15, 29]. Real
estate (RE) is information-intensive, yet many processes still depend on scattered listings, heterogeneous property
documents, local market knowledge, and manual coordination across portals, agencies, public records, and professional
service providers. Prior work describes RE as constrained by weak standardization and fragmented information
practices [4, 1, 13, 22]. This is especially relevant for RE marketing (REM), where agents transform incomplete
property information into exposés, listings, social media content, client communication, and sales material while
maintaining factual accuracy and regulatory compliance. Because REM is shaped by country-specific transaction
routines, data infrastructures, and regulation, this study has a single-country focus. As German RE agents (REAs) rely
on formal documents such as land register excerpts, cadastral maps, development plans, energy certificates, and notarial
transaction processes [20], Germany is an interesting setting. They also operate under European data-protection and
AI-governance requirements. At the same time, industry estimates suggest substantial GenAI potential in German
RE, while only a small share of firms report high digital maturity [12, 9]. Thus, the field is characterized by uneven
experimentation and limited routine organizational integration.
Evidence on how REAs actually use GenAI remains scarce. Kriegbaum et al. [22] provide an U.S.-based account of
REA sentiment, but RE practices vary across countries and cannot simply be transferred to Germany. We complement
this work with a task-level analysis that distinguishes current from potential REM use cases and links them to adoption
constraints. We ask:
RQ1 Which use cases of GenAI are already being applied by real estate agents in Germany?
RQ2 Which potential use cases does GenAI offer for real estate marketing?
∗victor.kolominsky-rabas@fit.fraunhofer.de
arXiv:2609.12684v1  [cs.AI]  11 Sep 2026

Generative AI Use Cases In Real Estate MarketingPREPRINT
We conduct eleven semi-structured interviews with REAs from different agencies and analyze them inductively
following Gioia et al. [16]. The study contributes, first, a grounded map of current and potential GenAI use cases in
German REM. Second, it shows that interaction is predominantly human-in-the-loop: GenAI drafts, structures, and
retrieves information, while REAs verify outputs, make judgments, and remain accountable. Third, it identifies adoption
challenges around listings, regulatory documents, data availability, and compliance-sensitive tasks. In doing so, it
extends U.S. evidence by showing which patterns travel across contexts, such as the centrality of marketing content, and
which become more salient in fragmented and strongly regulated settings, such as cross-portal aggregation, regulatory
document understanding, and compliance-aware screening.
2 Background and related work
This section introduces established tasks of REAs, which serve as the practical framework for situating GenAI use cases
in REM. It then defines GenAI and finally presents related work on the application of AI and GenAI in REM.
2.1 Core activities of real estate agents
REA activities follow the transaction flow [20]:acquisition(contacting owners intending to sell via channels such as
flyers, events, or partnerships),intake(capturing key property data, taking professional photos, assembling documenta-
tion like land register excerpts and cadastral maps),property analysis(market and location analyses based on intake
data),marketing(exposés, social media, listings, flyers; potentially home staging and outreach), viewings (pre-selection
and tours),contract closing(reviewing notarial drafts and accompanying clients), andhandover, as depicted in Figure 4.
2.2 Generative artificial intelligence in real estate marketing
AI refers to systems that interpret data, learn from it, and adapt their behavior to achieve specific goals [18]. GenAI is a
more specific class of AI that generates or transforms content such as text, images, audio, or video based on learned
patterns [10]. In this study, a use case is considered GenAI-related when GenAI generates, rewrites, summarizes,
interprets, or visually transforms real estate marketing content, or when it orchestrates such steps in an agentic workflow.
This boundary is important because several REM tasks also involve established technologies such as data analytics,
workflow automation, or rule-based software. We therefore do not assume that every technical step is uniquely
GenAI-based. Rather, we focus on tasks that REAs currently perform, or plausibly expect to perform, with GenAI
as a substantive component. Prior RE research still mainly addresses AI-based prediction, optimization, valuation,
visualization, or single technical systems rather than GenAI use cases in REA work [5, 6, 7, 17, 19, 23, 24, 30, 37, 36, 14].
Conceptual work proposes GenAI applications such as listings, virtual staging, routine client communication, screening,
lease management, and document generation, but often without empirical validation [28, 32]. Other studies discuss skills,
education, transparency, discrimination, governance, and market-level effects [6, 8, 31, 27, 34]. Empirical evidence on
GenAI in day-to-day REM remains limited. Existing work shows GenAI-supported social media marketing [26], agentic
property-description generation [35], and U.S. practitioner sentiment toward GenAI in real estate [ 22]. Kriegbaum
et al. [22] show that marketing material creation is a key adoption catalyst and that professionals associate GenAI
with efficiency gains, human intervention, ethical concerns, generational differences, relational work, and future
technological development. Building on this sentiment-oriented account, we examine how GenAI is incorporated into
concrete REM tasks, which applications are already routine rather than anticipated, and how adoption unfolds in the
German institutional setting. This shifts the focus from broad adoption sentiment to task-level workplace practice and
clarifies which patterns appear robust across contexts and which depend on fragmented and regulated national market
structures.
3 Methodology
To identify GenAI use cases in REM, we conducted eleven semi-structured interviews [25] between June and August
2025 (average duration: 29.6 minutes). Participants were recruited through convenience and snowball sampling [2, 3]
from different companies across Germany and cover mixed RE activities. Inclusion required active professional use of
AI because RQ1 asks for concrete current use cases; non-users are therefore less able to report practiced applications,
although their perspectives are important for studying resistance. The sample includes six men and five women with
an average of 11.2 years in the industry and 5–50 closed transactions annually. Table 1 summarizes variation in role,
employment status, seniority, transaction volume, and self-assessed IT and GenAI skills. Interviews were recorded with
consent, transcribed, and manually revised. Participants first described their role and understanding of GenAI before
discussing current and potential GenAI use cases. We analyzed the transcripts using an iterative Gioia-style coding
procedure [16]. Only passages referring to current or potential GenAI use cases in REM were coded. We derived
2

Generative AI Use Cases In Real Estate MarketingPREPRINT
first-order concepts through open coding, aggregated them into second-order themes, and distilled aggregate dimensions
through author workshops. Coding proceeded in two cycles, one for current and one for potential use cases. Because
new concepts emerged in the final interviews, full theoretical saturation is not claimed.
4 Results
This section reports the empirical findings. We distinguish current use cases, which describe how REAs employ GenAI
today, from potential use cases, which REAs consider feasible in the near future. All figures follow the same structure:
first-order concepts, second-order themes, and aggregate dimensions from left to right. Upright text denotes current use
cases,italicsdenote potential use cases, and * marks potential use cases that some REAs also cited as current.
4.1 Marketing communication
As shown in Figure 1, REAs use GenAI widely for property-facing marketing artifacts such as exposés, listings, visuals,
websites, and advertisements.
Writing exposé textsrefers to using GenAI to generate and refine property descriptions. Four REAs use property data
to generate complete exposé drafts from inputs ranging from textual facts to pre-generated PDFs from internal systems.
They also use GenAI for location details, exposé titles, stylistic refinement, and structural proposals. Several REAs
emphasize collaboration with the model through iterative prompting and human revision. For this theme, all mentions
describe current use.Editing property imagesinvolves modifying or enhancing images to improve presentation quality.
Current uses include changing wall colors, redesigning exterior elements, virtual staging, decluttering, and tailoring
interior styles to client preferences. One REA describes editing photos directly from on-site captures as a potential
workflow improvement. Such uses require caution because image edits can misrepresent the property’s actual condition
and create reputational risks if clients perceive exposé images as misleading during viewings.Developing social media
postsincludes creating platform-ready marketing content. REAs report current use for writing scripts for reels, captions,
and voiceover texts. One REA describes GenAI-generated posts from on-site photos and videos as a potential use case.
Visualizing property datarelates to transforming technical information into accessible visual formats. Current uses
include redesigning floor plans and generating floor plans from 360-degree recordings. Potential uses include interactive
walk-throughs of unbuilt properties from building plans and virtual tours compiled from short on-site videos. One
REA labels floor-plan redesign as potential, while another already practices it, indicating uneven adoption.Optimizing
websitesinvolves applying GenAI to improve agency web presence. A current example is generating images for blog
posts. As a potential use case, REAs suggest GenAI-based keyword proposals to enhance search engine optimization
and lead generation.Curating images for exposésrefers to the automated selection and integration of property photos
into exposés. REAs describe a potential use case in which GenAI chooses suitable images and inserts edited versions
directly into the exposé, removing manual steps after photography.Developing client presentations of available
propertiesdenotes a potential use case for GenAI-produced presentation material, for example by summarizing and
visualizing current listings for clients.Recommending advertisement locationscaptures a potential use case for
GenAI in identifying where to place advertisements. One example is proposing locations for advertisement walls based
on AI-provided information about “how many cars pass by there every day, how busy this supermarket [is]” (Agent ϵ).
Creating alternative marketing designs with the same contentcaptures the use of GenAI to produce stylistic or
layout variations for marketing material while keeping the content unchanged.Developing flyer and listing designs
Table 1: Expert List (EE = Employed, SE = Self-Employed, and confidence scores 0–3).
Expert Agent role Employment Years in industry # agencies # transactions IT- skills GenAI- skills
αseller SE 15 1 25–30 3 2–3
βseller EE 6 1 40–50 3 3
γseller/buyer EE 12 2 40–50 3 3
δseller/buyer SE 13 2 30 3 3
εseller/buyer EE 20 2 50 3 0
ζtrainee EE<11 50 3 2
ηseller EE 10 2 20–25 3 2
θseller/buyer SE 13 3 50 2 2
ιseller SE 15 2 10–15 3 2–3
κseller SE 3 2 50 3 3
λseller SE 15 1 6 3 2
3

Generative AI Use Cases In Real Estate MarketingPREPRINT
•Exposétexts(α, β, δ, ζ, κ, λ)
•Draftstructuresforexposéswithsubsequent manualediting(γ)
•Exposétextsin human-AI-collaboration(θ)
•Location descriptions for exposés (δ)
•Exposétextswithlocationalinformation(ε)
•Exposétextsenrichedwithinfrastructuralinformation(β)
•Market descriptions(δ)
•Exposésbased on property data (ι, η)
•Exposétexts based on PDFs created by real estate software (θ)
•Exposésbasedon datamanuallyprovidedtoreal estatesoftware(ζ)
•Image-to-text descriptions (δ)
•Exposéstitles (ζ)
•Enriched exposé texts (η)
•Stilistic refinement of existing exposé texts (κ)
•Iterative optimization of generated exposé texts (ζ)
•User-driven refinement of generated exposé texts (ζ)
•Textual variants for exposé texts  (ζ)
•Scripts for social media reels (λ)
•Socialmedia captions (κ, λ)
•Video voice-overtexts with pleasing wording in agent defined tone and targetgrouporientation(κ)
•Automaticgenerationofsocial media postsbasedon property photos and videos (η)
Writing exposé texts
Developingsocial media posts
Editingproperty images
Visualizingproperty data
Creatingalternative marketing
designs
Developingflyer and listing
design
Optimizingwebsites
•Alternative marketing material designs with the same content (α)
•Modification of wall colors (λ)
•Redesign of building exterior (λ)
•Virtual furniture staging (ζ, κ, λ, η)
•Virtual decluttering (ζ, η)
•Individual virtual homestaging (ε)
•Editing property photos only basedon agent-takenon-site photos (α)
•Redesign of existing floor plans (λ)
•Floor plans based on 360-degree recordings(η)
•Property tour videos from individual clips (λ)
•Interactive virtual walkthroughs ofnon-existingpropertiesfrombuildingplans(α)
•Redesign of existing floor plans in line with corporate identity* (θ)
•Property listing design (α)
•Flyer design (α)
•Images for blog posts (θ)
•Proposition ofkeywordsfor lead generation (γ)
Marketing
communication
Curatingimages for exposés
Recommendingadvertisement
locations
•Integrating property images into a finished exposé(α)
•Property photo selections for exposés (α)
•Advertising location recommendations based on traffic and visitor data (ε)
•Client-orientedcomparativeoverviewsoffilteredlistingsofnew-buildpropertiesforclients(α) Developingclientpresentations ofavailableproperties
Figure 1: GenAI use cases for marketing communication as derived from interview codes.
covers GenAI assistance in designing flyers and listings. One REA reports current use in which GenAI produces a
layout template that streamlines the design process.
4.2 Acquisition preparation
GenAI can support REAs in acquisition preparation (see Figure 2). Here, acquisition refers to proactively identifying
and approaching potential sellers, buyers, landlords, or tenants.
Aggregating acquisition targetsrefers to using GenAI to compile properties and contacts relevant for upcoming
acquisition activities. Two REAs report current aggregation of publicly available listings. Potential uses include
compiling new-build properties from the web, searching across portals, matching results to client requirements,
producing tabular overviews of listings from social media and online portals, flagging entries that may not be contacted
under local regulations, and summarizing candidate properties. Beyond properties, one REA envisions a regional
directory of RE developers with contact details and acquisition profiles to reduce preparation time.Filtering acquisition
targetsencompasses GenAI support for narrowing the aggregated pool based on specified criteria, such as client
preferences, to create a focused shortlist for outreach.
4.3 Property analysis
To market and sell a property, REAs conduct a series of analyses. GenAI supports several of these steps (see Figure 2).
Analyzing the property locationincludes cases where GenAI provides information on locational characteristics, such
as demographic indicators and local sales activity.Calculating investment KPIsconcerns quantitative indicators for
investment decisions. One REA reports using KPI reports for investors, including gross rental yield and return on
4

Generative AI Use Cases In Real Estate MarketingPREPRINT
Acquisition
preparation
•Aggregation ofpubliclyavailable listings (ι, κ)
•Aggregation ofoffersof new-buildproperties(α)
•Cross-portal property searches (θ)
•Aggregation ofon-marketand off-market site and landproposals(ε)
•Tabular representation of listings from social media and online portals, consideringcontactrestrictionsof§7 UWG*(λ)
•Textual summary of potential properties(κ)
•Real estatedeveloperdirectorywithcontactdetailsand acquisitionprofiles(λ)
•Filteredlists of publicly available listings (ι)
•Filteringofnew-buildpropertiesbasedon customercriteria(α)
•Filteringofon-marketand off-market site and land proposals based on customercriteria(ε)
Aggregatingacquisitiontargets
Filteringacquisitiontargets
Screening potential clients
•Generation ofprospectivetenantdossiersforsuitabilityassessment(α)
•Background check reportson rentalapplicantsthroughonline research(θ)
•Trustworthinessassessmentsofprospectivebuyerclientsbasedon publiconline informationtocomplyanti-money
launderingregulations(ε)
•Generation ofpre-contractualreservationtemplates (κ)
•Generation ofrentalcontracts (θ) Draftingtransactiondocuments
Sales
•Market priceassessment(δ)
•Comparativemarketanalyses(δ)
•Market analyses (δ)
•Complete property analysisreportto support market valuation (δ)
•Valuationsofcondomiums and rental appartements (θ)
•Location analyses(α, δ)
•Locational key figures (λ)
•KPI reports for real estate investors (λ)
•Construction cost reports for new development projects (λ)
Analyzingthemarketand
valuatingproperties
Analyzingthe property location
CalculatinginvestmentKPIs
Reviewingregulatory property
documents
•Extractionofregulatorykeyfiguresfromdevelopmentplans(λ)
•Extractionofbuildingconstraintsfromdevelopmentplans(λ)
•Generation ofreferencestolegallyrelevant buildingregulations(ε)
•Review oflandregisterentries(ε)
•Generation ofreferencestorelevant subsequent documentsduringlandregisterreview (ε)
•Generation ofconsolidatedrecordsfromdistributedlandregisterinformation(ε)
Property analysis
Figure 2: GenAI use cases for acquisition preparation, property analysis and sales as derived from interview codes.
equity, which reduces manual calculation effort. REAs also use GenAI to produce construction cost reports for new
development projects. Because general-purpose GenAI systems may produce erroneous calculations, KPI use should be
understood as drafting or explanation support rather than as a substitute for validated data analytics or spreadsheet-based
calculation tools.Reviewing regulatory property documentsrefers to support in understanding and analyzing legal
and regulatory texts. Current use focuses on development plans, where GenAI extracts regulatory key figures and
identifies building constraints. Potential use cases include land register reviews that reference applicable building
regulations and subsequent documents, reducing manual searches for REAs. Participants also point to consolidating
distributed land register-related documents into a single, navigable view.
4.4 Sales
REAs report several sales-related use cases, as depicted in Figure 2.
Screening potential clientsencompasses GenAI support for evaluating prospective tenants or buyers. A few REAs
report current use for scanning publicly available online information to flag risk indicators in support of anti-money
laundering obligations. Potential uses include background checks, verification of employment information, assessment
of publicly shared content, and applicant dossiers with suitability assessments based on information such as credit scores.
While participants expect reduced manual effort and more standardized evaluation, they emphasize that screening
involves sensitive personal data and express uncertainty about compliance with the EU AI Act and the General Data
Protection Regulation (GDPR). As a result, most screening-related use cases are discussed as potential rather than
established practice.Drafting transactional documentsrefers to using GenAI to create documents required in RE
transactions. One REA reports drafting non-binding reservation templates as a current use case. Others view the
generation of more formal documents, such as rental contracts, as a potential next step. Legal enforceability and liability
concerns were noted as reasons to keep humans in the loop even when drafting is automated [21, 32].
4.5 General communication
The data also reveal use cases in which GenAI supports REAs in daily work. As shown in Figure 3, these use cases
cluster into two domains. In contrast to marketing communication, general communication is not aimed at producing
property-facing promotional artifacts but at coordinating client relationships and transaction processes, such as inquiries,
appointments, viewings, negotiations, and follow-up.
5

Generative AI Use Cases In Real Estate MarketingPREPRINT
Automaticallyrespondingto
clientrequests
General
communication
Automaticallyorganizing
communication withclients
Developingand refiningdaily
communicationtexts
Developingbusinessstrategies
Referencinginformationfrom
documents
Answeringlegal questions
•Responses to client inquiries via real estate platforms, including exposé delivery and appointment confirmations (ι)
•Automated client feedback when property asking price is unrealistic (ε)
•Automated client feedback when property search criteria are unrealistic (ε)
•Automatedclientacquisitionmessages(κ)
•Formulationrefinementsofemails(α, ε, θ)
•Correctionofemailtexts(θ)
•Conflict-relatedinter-party communicationstrategies(θ)
•Templates forcontactingexternal agents(θ)
•Strategic formulationofemailtexts(κ)
•Formulationofroutineclientemails(α, δ, κ)
•Formulationofresponsestoroutineclientinquiriesvia email* (θ)
•Structured customer dataextractionfromvoicemail messages (δ)
•Message prioritizationbasedon contentanalysis(α, θ)
•Memory aid (θ)
•Answers to (specialized) questions (β, θ)
•Strategic and operational recommendations (λ)
•Non-bindinganswers to legal questions(e.g., building law) (ι, κ)
•Non-bindinganswersto legal questions* (β)
•Documentreferencing(λ)
Providing situational
knowledge General
knowledge
support
Figure 3: GenAI use cases for general communication and general knowledge support as derived from interview codes.
Developing and refining daily communication textscovers the formulation and strategic enhancement of written and
spoken messages. REAs report rephrasing emails, correcting errors, drafting replies to routine client inquiries, and
creating conversation templates for arranging viewings or requesting listing details. Participants also use GenAI for
strategic guidance in difficult interactions, for example in negotiations or tactical phrasing when interest in a property is
limited.Automatically responding to client requestsencompasses GenAI-generated replies to client requests. One
REA expects GenAI to process platform inquiries by delivering exposés or confirming appointments. Participants also
anticipate automated feedback that flags unrealistic expectations, such as informing owners when asking prices are too
high or when criteria cannot be met. One REA suggests that initial acquisition outreach could be automated after a
promising property is identified.Automatically organizing communication with clientsrefers to using GenAI to
structure and prioritize incoming messages. Participants describe potential uses in which GenAI extracts customer data
from voicemail, converts unstructured speech into records for documentation and follow-up, and highlights urgent
requests.
4.6 General knowledge support
The category of general knowledge support includes use cases that are not tied to a single REA task but provide
overarching support across different activities (Figure 3). Their relevance for REM lies in the RE-specific content being
retrieved or interpreted, such as property documents, building law, development plans, and market or presentation
decisions.
Developing business strategiescovers requests for strategic and operational recommendations. One REA reports
current use by asking GenAI for advice on business questions, including how to present a property more effectively.
To tailor outputs, the REA assigns GenAI a specific role, such as a RE assistant with marketing expertise.Providing
situational knowledgerefers to ad hoc information seeking. REAs describe current use as a memory aid for forgotten
details and as support for answering general and specific questions.Referencing information from documentsrelates
to retrieving and localizing details in lengthy or complex materials. One REA reports current use in which GenAI
extracts specific points from documents, such as development plans, and indicates where the relevant content appears,
which reduces manual review time.Answering legal questionscaptures preliminary, non-binding support on legal
matters. REAs report using GenAI to obtain first answers in areas such as building law, emphasizing reduced effort
in navigating legal texts: “Before I start leafing through legal codes or researching until I finally have the relevant
paragraphs together, using AI is definitely a major advantage.” (Agentι). Another REA mentions this as a potential
use case, indicating mixed adoption for this theme [32].
4.7 Code distribution
The use cases and corresponding activities that emerged from the interviews can be mapped across the core activities
identified by Helfrich [20], as shown in Figure 4.
Marketing, acquisition, and property analysis correspond directly to core REA activities. Sales use cases map to client
and contract-related activities, while general knowledge support spans the transaction flow. Based on participant-level
first-order use-case references, most use cases relate to marketing communication (47.7 %) (see Figure 5), followed
6

Generative AI Use Cases In Real Estate MarketingPREPRINT
Acquisition
Preparation
Marketing
Communication
Property
Analysis
Sales
General
Knowledge Support
General
Communication
Aggregating acquisition targets
Filtering acquisition targets
Analyzingthe market and valuating properties
Analyzingthe property location
Calculating investment KPIs
Reviewing regulatory property documents
Automatically responding to client requests
Developing flyer and listing designs
Automatically organizing communication with clients
Screening potential clients
Drafting transactional documents
Developing and refining daily communication texts
Writing exposé texts
Editing property images
Developing social media posts
Visualizing property data
Optimizing websites
Curating images for exposés
Developing client presentations of available properties
Recommending advertisement locations
Creating alternative marketing designs with the same content
Developing business strategies
Acquisition
Intake
Marketing
Property analysis
Contract closing
Viewings
Handover
Usecases(second-order themes)
Coreactivities
Providing situational knowledge
Referencinginformationfromdocuments
Answeringlegal questions
Activities
(aggregate dimension)
Figure 4: Use cases and activities identified in this work are mapped to the core activities of REAs as defined by Helfrich
[20].
by general communication (16.5 %), property analysis (14.7 %), acquisition preparation (9.2 %), general knowledge
support (7.3 %), and sales (4.6 %). These percentages are descriptive only and should not be read as representative
adoption rates. Across the overall set and the subset of current use cases, REAs most frequently refer to writing exposé
texts, developing and refining daily communication texts, and editing property images. Among potential use cases,
aggregation of acquisition targets shows the largest discrepancy between potential and current use and was mentioned
by five REAs, underscoring its perceived relevance.
Existing use cases Potential use cases
0 5 10 15 20 25
Writing exposé texts
Developing and refining daily communication texts
Editing property images
Aggregating acquisition targets
Reviewing regulatory documents
Developing social media posts
Visualizing property data
Analyzing the market and valuating properties
Automatically responding to client requests
Filtering acquisition targets
Analyzing the property location
Screening potential clients
Automatically organizing communication with clients
Answering legal questions
Providing situational knowledge
Developing flyer and listing design
Optimizing websites
Curating images for exposés
Calculating investment KPIs
Drafting transaction documents
Creating alternative marketing designs
Developing client presentations of available properties
Recommending advertisement locations
Referencing information from documents
Developing business strategies
7.3 % General knowledge
support
47.7 % Marketing
communication
14.7 % Property
analysis
16.5 % General
communication
4.6 % Sales
9.2 % Acquisition
preparation
Figure 5: Distribution of participant-level first-order use-case references across aggregate dimensions (left) and
distribution of current and potential references across second-order concepts (right).
5 Interpretation and discussion
Use is reported across all activities, with marketing communication dominating, followed by general communication.
We interpret this pattern as reflecting the comparatively low threshold of text-centric tasks: participants described GenAI
mainly as a drafting, structuring, and refinement aid in these areas, where outputs can be reviewed quickly by REAs. The
two categories differ in work function: marketing communication creates property-facing promotional material, whereas
7

Generative AI Use Cases In Real Estate MarketingPREPRINT
general communication coordinates inquiries, viewings, negotiations, and follow-up. This confirms the U.S. finding that
marketing material creation is a central entry point for GenAI adoption [22]. However, our data show that the German
field is not limited to content generation. Property analysis, acquisition preparation, and document-related knowledge
support are also salient because German REM depends on reliable integration of property facts, regulatory documents,
and locally distributed market information. Beyond communication, reported use cases include structured information
gathering, document interpretation, strategic advice, and ad hoc retrieval. As an author interpretation, lower adoption in
these areas appears to reflect heterogeneous data sources, regulatory knowledge requirements, and less standardized
outputs. Sales shows the fewest use cases. Here, participants explicitly raised uncertainty about personal data and legal
consequences, pointing to compliance concerns under the GDPR and the EU AI Act. Adoption is uneven overall: only
exposé writing is broadly established, while aggregation of acquisition targets stands out as a high-potential but not yet
routine use case. Compared with U.S. evidence, this surfaces cross-portal and document-integration problems as central
barriers alongside accuracy, ethics, and human intervention [22]. The findings suggest that GenAI fits best where tasks
are standardized, audience-facing, and largely textual. Where tasks require verifiable facts, personal data, or binding
commitments, participants more often describe GenAI as a drafting or retrieval aid than as an autonomous actor. Some
use cases are therefore GenAI-enabled workflows rather than tasks solved by GenAI alone, because complementary
technologies may be needed for data access, automation, calculation, or system integration. This matters for visually
edited marketing material and numerical KPI calculations, where misleading representations or incorrect outputs can
damage client trust and professional reputation. In most reported practices, GenAI drafts, structures, and retrieves while
REAs curate, verify, and decide. We therefore describe a partial shift toward editorial judgment and oversight, not a full
transformation of the REA role.
5.1 Practical and theoretical implications
For practical use, the findings indicate where REAs perceive GenAI as useful and where they remain cautious.
Marketing communication appears suitable for low-risk experimentation; acquisition preparation, especially cross-
portal aggregation and filtering, can be explored with human review and documented prompts. In domains involving
personal data, REAs should use only auditable, compliance-aware processes. Broader implications are tentative because
the study did not directly investigate system design, law, or training. Still, reported constraints point to demand for
cross-portal aggregation, document retrieval, reviewable outputs, and sector-specific AI literacy around prompt use,
output verification, data protection, disclosure of edited content, and when specialized analytics tools are preferable to
general-purpose GenAI. The study advances the literature by extending U.S. evidence to German REM and providing a
more granular structure of use cases [22]. More generally, the findings suggest that GenAI adoption in professional
services depends on task standardization, data accessibility, output verifiability, and compliance requirements.
5.2 Limitations and future work
The qualitative design and small sample limit statistical generalization. Because the sample includes only REAs with
AI experience, the study is suited to mapping practiced and anticipated use cases but cannot explain non-use, resistance,
or adoption barriers among REAs who have not yet experimented with AI. Future studies can test and extend these
findings with larger and more diverse samples from different regions, including non-users, and with quantitative designs.
Risk and legality were not the focus of this work. Several identified applications may raise discrimination or data
protection concerns in deployment, especially in screening scenarios. Future research should assess the legal feasibility
of specific use cases in light of the EU AI Act and the GDPR. Finally, the study maps what REAs do and what they
want to do rather than how to implement these systems. Technical work can evaluate pipelines for the most salient
opportunities, including acquisition target aggregation and document understanding in compliance critical contexts.
Work on adoption drivers can explain the observed heterogeneity across firms and roles and can support the transition
from isolated use to coherent practice.
6 Conclusion
This study offers the first empirical account of how REAs in Germany use GenAI in REM. Drawing on semi-structured
interviews and an inductive analysis, we find that GenAI already supports activities across the REA workflow. The
findings provide an overview of current and potential use cases in German REM and suggest that, in many reported
practices, GenAI shifts parts of the work toward review, verification, and oversight. They also identify practical
adoption challenges around data access, workflow integration, output verification, and compliance-sensitive tasks.
While participants already report GenAI use in REM, the field is at an early stage. Future work should track adoption
over time, evaluate governance approaches and AI-literacy programs, and develop implementable pipelines for the
high-value opportunities identified here.
8

Generative AI Use Cases In Real Estate MarketingPREPRINT
References
[1] Basheer Al-haimi, Haliyana Khalid, Nor Hidayati Zakaria, and Tuti Haryati Jasimin. 2025. Digital transformation
in the real estate industry: A systematic literature review of current technologies, benefits, and challenges.
International Journal of Information Management Data Insights5, 1 (June 2025), 100340. doi: 10.1016/j.
jjimei.2025.100340
[2] Earl R Babbie. 2020.The practice of social research. Cengage Au.
[3] Patrick Biernacki and Dan Waldorf. 1981. Snowball sampling: Problems and techniques of chain referral sampling.
Sociological methods & research10, 2 (1981), 141–163.
[4] Mario Bodenbender, Björn-Martin Kurzrock, and Philipp Maximilian Müller. 2019. Broad application of artificial
intelligence for document classification, information extraction and predictive analytics in real estate.Journal of
general management44, 3 (2019), 170–179.
[5] Tingting Chen and Shijing Si. 2024. Predicting Rental Price of Lane Houses in Shanghai with Machine Learning
Methods and Large Language Models. doi:10.48550/arXiv.2405.17505arXiv:2405.17505 [cs].
[6] Ka Shing Cheung. 2024. Real Estate Insights: Establishing transparency – setting AI standards in property
valuation.JPIF42, 4 (Aug. 2024), 406–408. doi:10.1108/JPIF-04-2024-0050
[7] Timothy Dombrowski and Cayman Seagraves. 2025. Optimizing Real Estate Portfolios: The Role of Generative
AI in Geographic Diversification.Journal of Real Estate Portfolio Management(July 2025), 1–33. doi: 10.1080/
10835547.2025.2513145
[8] David Dyason and Graham Squires. 2024. Real Estate Insights Navigating the future of property professionals: an
AI-enabled paradigm.JPIF42, 2 (April 2024), 207–210. doi:10.1108/JPIF-10-2023-0097
[9] Zentraler Immobilien Ausschuss e. V . (ZIA) and EY Real Estate. 2024. EY Real Estate Digitalisierungsstudie
2024. https://www.ey.com/de_de/insights/real-estate-hospitality-construction/
ey-real-estate-digitalisierungsstudie-2024
[10] Stefan Feuerriegel, Jochen Hartmann, Christian Janiesch, and Patrick Zschech. 2024. Generative AI.Bus Inf Syst
Eng66, 1 (Feb. 2024), 111–126. doi:10.1007/s12599-023-00834-7
[11] Marc-André Filz and Sebastian Thiede. 2024. Generative AI in Manufacturing Systems: Reference Framework
and Use Cases.Procedia CIRP130 (2024), 238–243. doi:10.1016/j.procir.2024.10.082
[12] Matt Fitzpatrick, Vaibhav Gujral, Ankit Kapoor, and Alex Wolkomir. 2023. The power of generative AI
in real estate | McKinsey. https://www.mckinsey.com/industries/real-estate/our-insights/
generative-ai-can-change-real-estate-but-the-industry-must-change-to-reap-the-benefits
[13] Nathalie Gardes. 2025. Ally or adversary? AI and the perceived threat to autonomy in services – The case of real
estate professions.Journal of Strategy & Innovation36, 1 (May 2025), 200533. doi: 10.1016/j.jsinno.2025.
200533
[14] Margot Geerts, Manon Reusens, Bart Baesens, Seppe vanden Broucke, and Jochen De Weerdt. 2025. On the
performance of LLMs for real estate appraisal. InJoint European Conference on Machine Learning and Knowledge
Discovery in Databases. Springer, 195–211.
[15] Shervin Ghaffari, Behnam Yousefimehr, and Mehdi Ghatee. 2024. Generative-AI in e-Commerce: Use-cases and
Implementations. In2024 20th CSI International Symposium on Artificial Intelligence and Signal Processing
(AISP). IEEE, 1–5.
[16] Dennis A. Gioia, Kevin G. Corley, and Aimee L. Hamilton. 2013. Seeking Qualitative Rigor in Inductive
Research: Notes on the Gioia Methodology.Organizational Research Methods16, 1 (Jan. 2013), 15–31.
doi:10.1177/1094428112452151
[17] Benedikt Gloria, Johannes Melsbach, Sven Bienert, and Detlef Schoder. 2025. Real-GPT: Efficiently Tailoring
LLMs for Informed Decision-Making in the Real Estate Industry.Journal of Real Estate Portfolio Management
31, 1 (Jan. 2025), 56–72. doi:10.1080/10835547.2024.2372748
[18] Michael Haenlein and Andreas Kaplan. 2019. A brief history of artificial intelligence: On the past, present, and
future of artificial intelligence.California management review61, 4 (2019), 5–14.
[19] Kasper Raupach Haurum, Ruiqi Ma, and Wen Long. 2024. Real Estate with AI: An agent based on LangChain.
Procedia Computer Science242 (2024), 1082–1088. doi:10.1016/j.procs.2024.08.199
[20] Oliver-D. Helfrich. 2021.Erfolgsstrategien für Immobilienmakler: Die wertvollsten Tipps für Akquise, Vermark-
tung und Abschluss. Springer Fachmedien Wiesbaden, Wiesbaden. doi:10.1007/978-3-658-35683-5
9

Generative AI Use Cases In Real Estate MarketingPREPRINT
[21] Ashok Kandipati. 2025. A Systematic Literature Review on Artificial Intelligence Based Techniques for Nurturing
Operations in Real Estate Sector.Journal of Real Estate Literature33, 2 (July 2025), 61–86. doi: 10.1080/
09277544.2025.2466370
[22] Alec Kriegbaum, Charles Ebert, and Kc Raghabendra. 2024. Chatbots Selling Condos: Generative Artificial
Intelligence in Real Estate.JMDC18, 4 (Dec. 2024).
[23] Jan-Peter Kucklick, Jennifer Müller, Daniel Beverungen, and Oliver Müller. 2021. Quantifying the impact of
location data for real estate appraisal–a GIS-based deep learning approach. (2021).
[24] Michal Kvet, Miroslav Potoˇcár, and Slavomír Tatarka. 2025. Real Estate Attribute Value Extraction Using Large
Language Models.IEEE Access13 (2025), 73076–73095.
[25] Michael Lewis-Beck, Alan Bryman, and Tim Futing Liao. 2004. Semistructured Interview. InThe SAGE
Encyclopedia of Social Science Research Methods. Sage Publications, Inc., 2455 Teller Road, Thousand Oaks Cal-
ifornia 91320 United States of America.
[26] Yanyi Li et al. 2025. AI-enabled real estate social media marketing: A new model and practical exploration.
Academic Journal of Business & Management7, 1 (2025), 244–249.
[27] Eric Justin Liu, Wonyoung So, Peko Hosoi, and Catherine D’Ignazio. 2024. Racial Steering by Large Language
Models: A Prospective Audit of GPT-4 on Housing Recommendations. InProceedings of the 4th ACM Conference
on Equity and Access in Algorithms, Mechanisms, and Optimization. 1–13.
[28] Juehui Ma and Ken Huang. 2023. Chatgpt in real estate. InBeyond AI: ChatGPT, Web3, and the business
landscape of tomorrow. Springer, 219–242.
[29] Uday Mittal, Siva Sai, Vinay Chamola, and Devika Sangwan. 2024. A comprehensive review on generative AI for
education.Ieee Access12 (2024), 142733–142759.
[30] Frances A Santos, Thiago H Silva, and Leandro A Villas. 2024. Real-up: Urban perceptions from lbsns helping
moving real-estate market to the next level. InCompanion Proceedings of the ACM Web Conference 2024.
1071–1074.
[31] Cayman Seagraves and Philip Seagraves. 2024. Revolutionizing real estate education: Integrating AI and LLMs
into undergraduate curriculum.Available at SSRN 5297493(2024).
[32] Nikodem Szumilo and Thomas Wiegelmann. 2024. Real Estate Insights AI: real estate’s new roommate–the good,
the bad and the algorithmic.Journal of Property Investment & Finance42, 2 (2024), 211–217.
[33] Constantin von Brackel-Schmidt, Stephan Leible, and Marina Hartig-Thiemann. 2025. Identifying and Assessing
Organizational Use Cases for Generative AI: A Procedure Model. (2025).
[34] Chongyu Wang, Jingfang Wang, and Tingyu Zhou. 2024. The Impact of Generative AI on Tenant-Driven
Commercial Real Estate Valuation.SSRN Journal(2024). doi:10.2139/ssrn.4885867
[35] Jibang Wu, Chenghao Yang, Yi Wu, Simon Mahns, Chaoqi Wang, Hao Zhu, Fei Fang, and Haifeng Xu. 2025. AI
Realtor: Towards Grounded Persuasive Language Generation for Automated Copywriting. doi:10.48550/ARXIV.
2502.16810Version Number: 5.
[36] Wenqian Zhao, Lavanya Pobbathi, Srinivasan Ramprasath, and Meghana Patibandla. 2024. Generative AI for
smart contracts in real estate business. In2024 11th International Conference on Dependable Systems and Their
Applications (DSA). IEEE, 49–59.
[37] Yun Zhao, Girja Chetty, and Dat Tran. 2023. Real estate price prediction on GenerativeLanguage models. In2023
IEEE Asia-Pacific Conference on Computer Science and Data Engineering (CSDE). IEEE, 1–7.
10
