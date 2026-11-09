---
title: 'AIx4Soccer: A Unified Platform Architecture for Football Club Management and Structured Athlete
  Development'
url: https://arxiv.org/abs/2607.28531
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Frederico Falconi Costa
- Salvador Cesar Costa
- Fabricio F. Costa
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.28531
pages: 25
chars: 64916
fetched_at: '2026-11-08T13:20:18+00:00'
kb_version: 1
---

# AIx4Soccer: A Unified Platform Architecture for Football Club Management and Structured Athlete Development

AIx4Soccer: A Unified Platform Architecture for
Football Club Management and Structured Athlete
Development
Frederico Falconi Costa 1,2,∗ Salvador Cesar Costa 1,2 Fabricio F. Costa 2,∗
1Empower FC, Belo Horizonte, MG, Brazil
2AIx4Soccer, LLC, Sunnyvale, California, USA
∗Corresponding authors: fcosta@aix4all.com, emp.empowerfc@gmail.com
Preprint: systems/position paper. arXiv category: cs.CY (Computers and Society).
Abstract
Football(soccer)clubs, academies, andfederationsoperateagrowingbutfragmentedportfolioof
digital tools: separate systems for video analysis, GPS/performance tracking, medical records,
scouting, and administration. This fragmentation is most acute outside the elite European
clubs that can afford integration, producing a digital divide that disadvantages grassroots clubs
and academies in developing football markets such as Brazil, paradoxically the world’s largest
exporter of professional players. This paper presents, at a conceptual level, the architecture
of “AIx4Soccer One Platform,” a multi-tenant cloud SaaS operating system designed to unify
club-management workflows and to embed a structured athlete-development methodology, the
PDI Framework (“Plano de Desenvolvimento Individual” / Individual Development Plan). We
further describe two companion components: “Tak Tik,” a certified two-sided marketplace con-
necting clubs with certified video analysts under a 75%/25% (analyst/platform) revenue split,
and the PDI/TBIL methodology, which links individual development plans to video evidence
and periodic review cycles. As Materials and Methods, we state the design as explicit require-
ments and give a formal, implementation-independent specification of the platform’s proposed
future substrate: an event-centric semantic data model in which every fact is a typed, immutable
event in an append-only log that induces a growing knowledge graph. We situate the design
against the literature on athlete development frameworks (LTAD, the English FA’s EPPP and
Four-Corner model, the Belgian and German federation reforms), sports-analytics workflows,
two-sided-market economics, and multi-tenant SaaS patterns, and discuss youth data-protection
obligations (Brazil’s LGPD and the 2025 Digital ECA; the EU GDPR), algorithmic-fairness risks
in talent evaluation, and why small, domain-specific models, rather than general-purpose fron-
tier LLMs, are the appropriate intelligence layer. This is a design and early-deployment paper,
not an empirical evaluation; we describe what has been built and outline a planned evaluation,
making no efficacy claims.
Keywords:sports informatics; multi-tenant SaaS; athlete development; event-centric data
model; knowledge graph; two-sided marketplace; youth football; data protection
Intellectual-property disclosure.The platform architecture (AIx4Soccer One Platform), the PDI (Plano
de Desenvolvimento Individual) methodology, the Tak Tik marketplace design, and the event-centric semantic data
model described in this paper are the subject of a patent application in preparation for filing with the United States
Patent and Trademark Office (USPTO). This preprint is published for scientific dissemination and to establish a
public, citable disclosure. It does not grant any license to the described intellectual property.
1
arXiv:2607.28531v1  [cs.CY]  30 Jul 2026

1 Introduction
Modern football is a data-intensive enterprise. An elite club’s performance department routinely
integrates match and training video, event and tracking data, GPS/inertial wearable telemetry,
medical and injury records, scouting databases, and athlete-management workflows. Yet these
capabilities are delivered by a patchwork of specialized vendors: video analysis and scouting from
Hudl and its Wyscout and InStat acquisitions, wearable GPS/load monitoring from Catapult and
STATSports, event data from Stats Perform and StatsBomb, and so on. Each is excellent within
its niche, but the niches do not compose into a single coherent record of a club or an athlete [31].
This fragmentation imposes three interacting problems that this paper addresses.
Tool fragmentation.Industry surveys of the football-software landscape consistently describe
a market segmented by function (video analysis, scouting, physical monitoring, and administration),
with integration left to the buyer. For a resourced Premier League department this is a solvable
staffing problem; for the overwhelming majority of the world’s clubs it is not. Access itself is strati-
fied: professional scouting platforms such as Wyscout and StatsBomb are described in practitioner
guidance as very expensive and typically licensed by clubs rather than individual analysts, pushing
independent and lower-budget actors toward cheaper entry-level tools.
A professionalization gap.The management maturity of clubs is highly uneven. Even in
Brazil, a football superpower by any sporting measure, the governing body itself has recently moved
to “urgently modernize” the sport. It restructured competition calendars, launched a financial fair-
play model, and professionalized refereeing. In 2025–2026 it also convened a nationwide youth-
development working group whose remit explicitly includes the certification and governance of
training clubs. The existence of such a working group is itself evidence of a recognized institutional
gap between the elite and the base of the pyramid.
An athlete-development documentation gap.The elite European game has converged on
structured, documented, multi-dimensional player development. Examples include the English FA’s
Four-Corner Model (technical/tactical, physical, psychological, social), the Elite Player Performance
Plan (EPPP), and the individual development plan (IDP) as an operational instrument. Outside
these environments, development is often undocumented, held in a coach’s head, and lost when the
coach or the player moves. The consequence is not only lost competitive value but lost duty of care.
A 2024 University of Essex study led by Dr Jason Moran (published in theInternational Journal
of Sports Science & Coaching) reports that “just four per cent of talented teen academy prospects
make it to the top tier of professional football,” with only about a further six per cent going on to
play in lower leagues [21]. The documentation that scaffolds a player’s development should therefore
also scaffold the education and welfare of the roughly nine in ten who do not turn professional.
These problems are especially consequential in developing football markets. Brazil is the world’s
largest exporter of players. FIFA’s official release on its 2024 Global Transfer Report states that
“Brazilian clubs were in the lead with 1,102 incoming and 1,113 outgoing transfers” [19], and the
CIES Football Observatory Monthly Report no100 (May 2025) found that Brazil leads all nations
with 3,020 expatriate footballers, comfortably ahead of France (2,293) and Argentina (2,171) [20].
Yet the Ernst & Young (EY) study commissioned by the CBF (“Impacto do Futebol Brasileiro,”
2018 data) counted 360,291 registered athletes across 7,020 clubs, of which only 1,430 were active
(874 professional, 556 amateur), spread across 1,499 municipalities, and just 45 clubs held the
CBF’s “Certificado de Clube Formador” (training-club certificate) in one recent year [28]. The
talent pipeline is vast; the digital and managerial infrastructure beneath it is thin.
Contribution.This paper contributes: (1) a requirements analysis, grounded in the cited
literature and practitioner context, for a unified football club-management platform serving institu-
tional (B2B) users; (2) a conceptual, non-proprietary architecture for “AIx4Soccer One Platform,” a
2

multi-tenant cloud SaaS system with an embedded athlete-development module; (3) the conceptual
design of the “PDI Framework,” a structured individual-development methodology mapped to estab-
lished development-science concepts; (4) the conceptual design of “Tak Tik,” a certified two-sided
marketplace for video-analysis labor; and (5) a formal, implementation-independent specification of
an event-centric semantic data model proposed as the platform’s future substrate (Sections 3 and 7).
We are explicit that this is a systems/position paper describing a design and an early deployment; it
reports no empirical results and makes no efficacy claims. The platform is developed by a Brazil–US
partnership: Empower FC and AIx4Soccer, LLC (California, USA).
2 Related Work
2.1 The club-management and sports-analytics software landscape
The performance-analysis workflow (capture, tagging/coding, analysis, reporting, and feedback) is
well described in the practitioner and applied-science literature [49, 50], and the video-analyst role
has professionalized around it, from live in-match feedback to post-match review and individual
player-development clips. The tooling, however, is siloed by function: Hudl for video and coach-
ing workflows (having absorbed Wyscout and InStat for scouting), Catapult and STATSports for
wearable GPS and load monitoring, Stats Perform/StatsBomb for event data. Reviews of athlete-
monitoring systems note that although data collection is now routine in professional team sport,
comparatively little work addresses the end-to-end process of planning, integrating, analyzing, and
communicating that data [14]. This is precisely the integration gap a unified platform targets.
Recent standardization efforts confirm that significant cross-vendor variation persists in what is
collected and how it is represented [31]. Recent web-application-based monitoring studies in youth
soccer illustrate both the appetite for lightweight, integrated tools and the engagement challenges
they face.
2.2 Athlete-development frameworks
The Long-Term Athlete Development (LTAD) model, originated by Istvan Balyi and colleagues [6],
organizes development into stages (FUNdamental, Learning to Train, Training to Train, Training
to Compete, Training to Win, and lifelong activity) keyed to maturation rather than chronolog-
ical age. LTAD has been influential and criticized for underweighting contextual factors such as
socioeconomic status and coaching quality, and for a physiological emphasis [7, 46]. In football
specifically, national reforms provide the most relevant precedents. The English FA’s Four-Corner
Model [9] frames development across technical/tactical, physical, psychological, and social corners,
and underpins the Premier League’s EPPP (introduced 2012) [8], which grades academies into cat-
egories 1–4 and has been studied for both its holistic ambitions and its administrative burdens on
coaches [10, 51]. Belgium’s reform, the “Golden Vision” project launched in 2001 after the nation co-
hosted Euro 2000, was led by Royal Belgian Football Association technical director Michel Sablon
with the consultancy Double PASS [11]; as CNN reported, Sablon’s team “analyzed data from
1,500 youth games, enlisted the cooperation of 70 coaches at all levels of the game and made 120
presentations to the clubs” [12], standardizing a national playing philosophy, small-sided game for-
mats, and “parallel teams” to counter relative age effects. Germany’s parallel reform made centrally
regulated youth academies a condition of professional licensing for Bundesliga and 2. Bundesliga
clubs from 2002 [13]. Underlying these frameworks is a substantial body of skill-acquisition science,
notably Ericsson and colleagues deliberate-practice theory [3, 4], which prescribes structured, ef-
fortful, feedback-rich practice targeted at specific weaknesses, and its subsequent critiques [5]. The
3

individual development plan (IDP) is the operational unit that translates these frameworks into
player-level action, using SMART goals, four-corner assessment, self-reflection for player ownership,
and bio-banding by biological maturity [45]. The broader talent-identification and development
literature underlines both the multidimensional, dynamic nature of talent and the methodologi-
cal limitations of one-off selection, reinforcing the case for longitudinal, documented development
records [41, 42, 43].
2.3 Two-sided markets and labor-platform economics
The Tak Tik marketplace draws on the economics of two-sided (multi-sided) platforms, formalized
by Rochet and Tirole [1, 2] and popularized in the platform-strategy literature [54], in which an
intermediary must get both sides “on board” and where the structure of prices across sides, not
only the level, determines participation and volume. Online labor (“gig”) platforms such as Upwork
and Fiverr instantiate these dynamics for services, relying on reputation systems, verified skills,
and reviews to let strangers assess quality under incomplete information; the HCI and economics
literatures document both the value and the biases (including discrimination) of these signals [17].
Certification functions as a stronger, platform-provided quality signal than crowd reputation alone.
It is a classic response to quality uncertainty [53] and operates as a costly signal in the sense of
Spence [52].
2.4 Multi-tenant SaaS architecture
The platform’s delivery model rests on well-established multi-tenancy patterns, in which a single
applicationinstanceservesmanytenantswithlogicaldataisolation, describedalongaspectrumfrom
fully isolated (“silo”) to fully shared (“pool”) with hybrid/bridge models in between, and analyzed
as encoding business strategy, isolation, and cost trade-offs into software design [16]. This literature
provides the vocabulary for describing AIx4Soccer’s tenancy at a conceptual level without exposing
implementation detail.
2.5 Positioning
AIx4Soccer’s contribution is not a new analytics algorithm or a new development theory. It is
an integration contribution: a single multi-tenant record spanning administration, squad, training,
development, and video for institutions that today cannot assemble or afford the elite tool stack,
coupled with an explicit methodology (PDI) and a labor marketplace (Tak Tik) that together aim
to democratize access to sports-science practice in developing markets. This aligns in spirit with
FIFA’s Talent Development Scheme, which frames global footballing inequality as the core problem
to solve [18].
3 Materials and Methods
3.1 Design approach
This work follows a design-science approach [62]: the artifact is the platform design itself, built and
refined against explicit requirements derived from the literature of Section 2 and from practitioner
context at the test club, with evaluation planned as staged empirical study (Section 8). The “ma-
terials” of this study are therefore (i) the published literature and public regulatory instruments
cited throughout; (ii) the operational context of a Brazilian club/academy (Empower FC) as design
environment; and (iii) the conceptual artifacts presented here: the requirements (Section 3.2), the
4

layered architecture (Section 4), the PDI methodology (Section 5), the marketplace design (Sec-
tion 6), and the formal event model (Section 3.3). No athlete data were collected or analyzed for
this paper.
3.2 Requirements
We synthesize the literature and practitioner context into design requirements. Functional require-
ments (R) and non-functional requirements (N) are stated so that later sections can be traced back
to them.
•R1: Single source of truth.The platform shall maintain one integrated record per club and
perathletespanningadministration, squad/roster, training, development, andvideo, replacing
siloed point tools.
•R2: Multi-stakeholder roles.It shall represent distinct roles (director, coordinator, coach,
analyst, athlete, guardian, federation officer) with appropriate, least-privilege permissions.
•R3: Structured athlete development.It shall operationalize a documented, multi-
dimensional development methodology (PDI) with assessment cycles, goal-setting, and review
cadence, mapped to established frameworks.
•R4: Video-evidence linkage.Development goals and assessments shall be linkable to video
evidence, so that feedback is concrete and progress is auditable.
•R5: Access to analysis capacity.The platform shall give clubs that lack in-house analysts
access to qualified analysis via a marketplace (Tak Tik), with certification as a quality signal.
•R6: Institutional/federation scale.It shall support hierarchical, multi-tenant use by
clubs, academies, and state/national federations, including oversight and aggregation across
subordinate tenants.
•R7: Affordability and low barrier to entry.The design shall target resource-constrained
clubs in developing markets, not only elite buyers.
•R8: Regulatory alignment.It shall support youth-data-protection obligations (LGPD,
Digital ECA, GDPR) and football-governance requirements (e.g., documentation relevant to
training-club certification).
•N1: Tenant isolation and security.Tenants’ data shall be logically isolated with least-
privilege access control.
•N2: Scalability and availability.The cloud SaaS deployment shall scale from a single club
to federation-wide populations.
•N3: Fairness and transparency.Any assistive evaluation features shall be designed to
mitigate known biases (e.g., relative age effect) and to keep human judgment accountable.
•N4: Interoperability.The platform shall be able to integrate with, rather than necessarily
replace, external data sources where clubs already use them.
3.3 A formal event-centric semantic data model
We now give an implementation-independent formal specification of the event-centric data model
that Section 7 proposes as the platform’s future substrate. The formalism fixes vocabulary and
makes the model’s properties (immutability, entity linkage through events, unbounded growth, deriv-
ability of application state) precise and checkable.
5

Events.LetAdenote the set of actors (people, devices, system agents),Vthe set of domain
entities (athletes, teams, matches, sessions, venues, staff, devices, documents),Ta finite set of
event types,Oa set of typed outcomes, andMa set of media/evidence objects. Aneventis a tuple
e=⟨ι, τ, α,Σ, t, λ, ω, E⟩,(1)
whereιis a globally unique identifier;τ∈ Tis the event type;α∈ Ais the actor (who);Σ⊆ Vis
the non-empty set of subject entities the event is about;t∈Tis the occurrence time (when), with
Ta totally ordered time domain optionally refined by match/session clocks;λ∈Λis the location
(where), spatial (pitch coordinates) and/or organizational (venue, club, category);ω∈ Ois the
outcome; andE⊆ Mis a (possibly empty) evidence set (video clips, documents, sensor streams)
(R4).
Type taxonomy.Tis organized by a subsumption partial order⪯(is-a) rooted at the abstract
typeEVENT, with seven top-level families:
τ⪯τ ′ ⪯EVENT, τ ′ ∈ {MATCH,TRAIN,MED,DEV,VID,ADM,MKT},(2)
covering match actions (pass, shot, tackle, goal, ...), training events (drill, load measurement, test),
medical events (screening, injury, treatment), development events (the PDI stages: assessment,
goal-setting, plan, evidence link, review), video events (clip, annotation, tag), administrative events
(registration, transfer, contract, consent), and marketplace events (Tak Tik engagement, delivery,
settlement). Match subtypes align with established event vocabularies such as SPADL and the
Common Data Format [29, 31].
The append-only log.For each tenantc(club, academy, or federation; N1), the system state of
record is theevent log
Lc(t) =

e1, e2, . . . , en(t)

, t(e 1)≤t(e 2)≤ · · · ≤t(en(t)),(3)
subject to theappend-only invariant: for allt≤t ′,
Lc(t)⊑L c(t′),(4)
where⊑denotes the prefix relation. Events are immutable; a correction is itself a new evente′ with
τ(e ′) =ADM:correctionand a reference toι(e), so the log is simultaneously the audit trail (R8).
The induced knowledge graph.Entities are relatedonly through events. The log induces, at
any timet, a labeled multigraph
Gc(t) =

Vc, Rc(t)

, R c(t) =

(u, e, v) :e∈L c(t), u̸=v, u, v∈ {α(e)} ∪Σ(e)

,(5)
whose edges are events: facts carrying type, time, location, outcome, and evidence. Any derived
inter-entity relation is a projection of (5): for a predicateρover events,
u∼ ρ v⇐ ⇒ ∃e∈L c(t) :ρ(e)∧(u, e, v)∈R c(t).(6)
For example, “coachudevelops athletev” is the projection withρ(e)≡τ(e)⪯DEV; the relation
is thereby always dated, attributable, and evidence-backed, and can be recomputedas ofany past
time.
6

Application state as folds.In the event-sourcing pattern [37, 38, 39], every module view of
Section 4 (athlete profile, PDI dashboard, squad load view, federation aggregate) is aprojection: a
read model computed by a left fold of a projection functionfP over the log from an initial states0,
SP (t) = fold

fP , s0, Lc(t)

=f P

· · ·fP

fP (s0, e1), e2

· · ·, en(t)

,(7)
and temporal (“as-of”) queries follow by folding the truncated logLc(t)|≤t∗. New views can be
defined retroactively over the full history. This property has direct value for compliance reporting
and longitudinal development review.
Growth.The model’s asymmetry is the volume argument of Section 7 made precise: for a club,
the entity set is bounded while the log is not,
|Vc(t)|=O(1)ast→ ∞,|L c(t)|= Ω(t),(8)
with, empirically, a single match contributing on the order ofE[Nmatch]≈1.6–2.0×10 3 recorded
events in commercial and open event datasets [30], before counting training, medical, development,
video, administrative, and marketplace events.
Event-derived analytics.Established analytics are functionals of the log, illustrating that event-
centric storage subsumes, rather than competes with, current practice. Action valuation in the
VAEP framework scores each on-the-ball event by the change in scoring and conceding probabilities
it induces [29],
V(e i) = ∆P score(ei)−∆P concede(ei),(9)
and recent Large Events Models and soccer foundation models are autoregressive sequence models
over event streams [35, 36],
pθ

L

=
nY
i=1
pθ

ei

 e1, . . . , ei−1  ,(10)
trained, in direct analogy to language models, to predict the next event given the sequence so far. A
platform whose native substrate satisfies (1)–(8) is, by construction, the ideal data source for both.
PDIandmarketplaceinstruments.Withinthisformalism, anathletea’sPDIisthedevelopment-
typed sub-logPDI a(t) ={e∈L c(t) :a∈Σ(e), τ(e)⪯DEV}, and a simple cycle-progress metric
over review cyclekis
ga(k) = #{goals met in cyclek} #{goals reviewed in cyclek} ∈[0,1],(11)
computable, with provenance, entirely from events. A Tak Tik settlement event with gross pricep
splits deterministically as
πanalyst = 0.75p, π platform = 0.25p,(12)
the design choice motivated in Section 6.
7

3.4 Evaluation plan
Consistent with the design-science cycle [62], evaluation is staged and explicitly deferred: (1) us-
ability and workflow-fit assessment with staff and athletes at the test club; (2) adoption and en-
gagement measurement, a known challenge for athlete-monitoring tools (Section 2.1); and (3) only
subsequently, with appropriate study design and ethics review, investigation of development or op-
erational outcomes. Section 8 states the current deployment status; no outcome data exist yet and
none are claimed.
4 Platform Architecture (Conceptual)
This section describes AIx4Soccer One Platform at a conceptual level only. It intentionally omits
proprietary algorithms, code, database schemas, pricing, and client data.
4.1 Layered architecture
The platform follows a conventional layered SaaS structure. Thepresentation layerprovides
role-adaptive web and mobile interfaces that render the same underlying record differently for a
director, a coach, an analyst, an athlete, or a guardian (R2); federation officers receive aggregate and
oversight views (R6). Theapplication/module layercomprises a set of cooperating functional
modules (Section 4.2) implementing club and development workflows (R1, R3). Thedata layeris a
tenant-isolated integrated data store holding the authoritative club and athlete records; all modules
read and write against it rather than maintaining private silos (R1, N1). Theintegration layer
provides connectors for selective import/export with external systems clubs may already use (N4)
and mediates the marketplace boundary with Tak Tik (R5). Theplatform/infrastructure layer
is cloud-hosted, multi-tenant infrastructure providing isolation, scaling, and availability (N1, N2).
Figure 1 depicts the stack.
4.2 Application modules
Table 1 summarizes the application modules.
T able 1:Module overview.
Module Purpose Primary roles Key req.
Club Administration Institutional records, staff, compli-
ance/registration documentation
Director, Coordina-
tor
R1, R8
Squad / Roster Man-
agement
Teams, categories, registrations, con-
tracts, availability
Coordinator, Coach R1, R2
Training & Periodiza-
tion
Session planning, load/training cal-
endars, periodization
Coach, Coordinator R1, R3
Athlete Development
/ PDI
Individual development plans, assess-
ment cycles, goals, reviews
Coach, Athlete,
Guardian
R3, R4
Video Analysis Inte-
gration
Linking video evidence to ath-
letes/goals; Tak Tik gateway
Analyst, Coach R4, R5
Communication Structured messaging among stake-
holders; review notifications
All roles R2, R3
8

Figure 1:Layered architecture of AIx4Soccer One Platform (conceptual). All module reads/writes pass
through the tenant-isolated data layer.
9

4.3 Multi-tenancy and federation hierarchy
Following the tenancy spectrum from the SaaS literature [16], the platform models each club or
academy as a tenant with logically isolated data (N1), formalized as the per-tenant logL c of
Eq. (3). Federations are represented as higher-order tenants able to view and aggregate across
their subordinate club tenants for oversight and development-pathway continuity (R6), subject
to permissioning. This mirrors the top-down, federation-to-club diffusion of playing philosophy
documented in the Belgian and German reforms but implemented as data architecture rather than
policy alone.
4.4 Roles, permissions, and data flow
Roles carry least-privilege permissions (R2, N1): guardians see their own athlete’s development and
welfare information; coaches see their squads; analysts see the material they are engaged to analyze;
directors and coordinators see club-wide administration; federation officers see aggregate/oversight
data. The athlete is a first-class participant in their own development record (consistent with IDP
“player ownership”). Figure 2 shows the stakeholder data flows around the integrated record.
Figure 2:Stakeholder roles and data flows (conceptual). Solid arrows denote writes; dashed arrows denote
scoped reads. Tak Tik connects through the Integration Layer.
4.5 Comparison with the fragmented status quo
Table 2 contrasts today’s fragmented tool categories with the unified approach. The point is not
that AIx4Soccer replaces specialized analytics vendors, but that it provides the connective record
10

those tools currently lack, and that it brings development documentation, today the least-tooled
category, into first-class support.
T able 2:Fragmented tool categories vs. unified platform. Vendor examples are drawn from the cited market
literature and illustrate categories, not endorsements.
Capability cate-
gory
Typical dedicated
tools
Integration bur-
den today
AIx4Soccer approach
Videoanalysis/cod-
ing
Hudl, Nacsport, Dart-
fish
Separate logins, ex-
ports
Native module + market-
place (R4, R5)
Scouting / match
database
Wyscout, StatsBomb,
InStat
Costly, club-licensed Out of scope as data ven-
dor; integrable (N4)
Physical / GPS load Catapult, STATSports Separate hard-
ware/software
Integrable via connectors
(N4)
Medical / availabil-
ity
Point solutions Manual reconcilia-
tion
Part of integrated record
(R1)
Athlete develop-
ment / IDP
Ad hoc documents,
spreadsheets
Uncaptured, coach-
held
PDI module (R3, R4)
Administration Generic office tools Disconnected from
sporting data
Club administration mod-
ule (R1)
5 The PDI Framework
ThePDI Framework(“Plano de Desenvolvimento Individual” / Individual Development Plan),
also referred to as thePDI/TBIL methodology, is the platform’s structured athlete-development
methodology. It is presented here as a conceptual methodology; no proprietary content is disclosed.
5.1 Rationale and grounding
PDI operationalizes the IDP concept documented in the sport-pedagogy literature and used by elite
academies: a per-athlete plan combining multi-dimensional assessment, specific measurable goals,
player self-reflection, and periodic review. It is grounded in three literatures: (a) multi-dimensional
development frameworks (the FA Four-Corner Model’s technical/tactical, physical, psychological,
social dimensions [9]; LTAD’s maturation-keyed staging [6]); (b) deliberate-practice theory (specific,
effortful, feedback-rich work on identified weaknesses [3]); and (c) the video-evidence and monitoring
practices of applied performance analysis [14, 47, 49].
5.2 The PDI cycle
PDI is a recurring cycle rather than a one-off document (R3):
1.Assessthe athlete across development dimensions, using biological as well as chronological
age where relevant (bio-banding [45]) to reduce maturation bias.
2.Set goalsthat are specific and measurable, co-authored with the athlete to build ownership.
3.Plantargeted training/practice addressing prioritized goals.
4.Evidenceprogress by linking video and monitoring data to specific goals (R4).
5.Reviewon a defined cadence with the athlete (and guardian, for minors), updating goals.
11

6.Returnto assessment, closing the loop.
In the formalism of Section 3.3, the cycle is the development-typed sub-logPDIa, with cycle progress
measurable as in Eq. (11). Figure 3 depicts the cycle.
Figure 3:The PDI cycle (conceptual). The athlete sits at the hub as owner of the plan; video evidence
links goal-setting and review; guardians participate in reviews for minors.
5.3 Mapping PDI to established concepts
Table 3 maps the PDI stages to the established development-science concepts of Section 2.2. The
“TBIL” designation denotes the methodology’s internal pedagogical structuring; its detailed content
is proprietary and is deliberately not disclosed here. The claim of this paper is only that the shape of
PDI (cyclical, multi-dimensional, video-evidenced, athlete-owned) is consistent with, and traceable
to, the cited development science.
6 Tak Tik: A Certified Video-Analysis Marketplace
Tak Tikis a two-sided marketplace connecting clubs (demand side) with certified video analysts
(supply side).
12

T able 3:PDI stages mapped to established development-science concepts.
PDI stage Established concept / source literature
Assess (multi-dimensional; bio-banding) FAFour-CornerModel[9]; LTADmaturationstag-
ing [6]; relative-age-effect research [44]
Set Goals (specific, measurable, co-
authored)
SMART goal-setting in IDP practice; deliberate-
practice specificity [3]
Plan (targeted practice) Deliberate practice (Ericsson et al.) [3]
Evidence (video + monitoring linkage) Performance-analysis feedback workflows [49];
athlete-monitoring systems [14]
Review (cadenced, athlete/guardian) IDP review and player-ownership practice; EPPP
holistic review [8]
Continuity across pathway Federation development-pathway models (Bel-
gium, Germany) [12, 13]
6.1 The gap it addresses
Section 2 established that professional analysis capacity is unevenly distributed: elite clubs employ
full-time analysts, while smaller clubs and academies, especially in developing markets, often cannot.
Simultaneously, there is a pool of trained and aspiring analysts (a professionalizing labor market)
without efficient access to paying institutional work. Tak Tik is designed to clear this two-sided
matching problem (R5).
6.2 Two-sided-market design
Following Rochet–Tirole [1, 2], a marketplace must bring both sides on board and must attend to
the structure of value distribution across sides, not merely its level. Tak Tik’s publicly stated design
choice is the75%/25% revenue splitof Eq. (12): 75% to the analyst and 25% to the platform.
The split is deliberately skewed toward the supply side to attract and retain qualified analysts. This
in turn makes the platform valuable to the demand side (the cross-side network effect). This split
is a design parameter disclosed as a matter of positioning; no other pricing is disclosed.
6.3 Certification as a quality signal
General gig platforms rely on crowd reputation and reviews, signals that are useful but subject to
bias [17]. Tak Tik instead usescertificationas a platform-provided quality signal layered on top of
reputation, mitigating the adverse-selection problem that arises under quality uncertainty [52, 53].
Certification addresses the incomplete-information problem (clubs cannot easily assess a stranger
analyst’s competence) more strongly than ratings alone, and it aligns with the broader standard-
ization gap in the analyst labor market noted in Section 2.1. Reputation/review mechanisms can
complement certification but are explicitly secondary to it. Figure 4 depicts the marketplace.
6.4 Coupling with the platform
Because Tak Tik delivers analysis directly into the club’s integrated record and can link outputs to
PDI goals (R4), it is not a standalone freelancing site but a capability extension of the platform:
the marketplace supplies labor, and the platform supplies the context (the athlete record, the
development plan) that makes the labor actionable.
13

Figure 4:Tak Tik two-sided market (conceptual): matching and certification at the center, cross-side
network effects, and the 75%/25% analyst/platform payment split.
14

6.5 The whole model at a glance
Figure 5 summarizes the complete model as a wheel. At the hub sits the athlete and their integrated
record; the inner ring is the PDI development cycle that continuously turns around the athlete;
the middle ring comprises the six platform modules that operationalize club workflows; and the
outer ring holds the stakeholder roles who read from and write to the record under least-privilege
permissions. Two orbitals complete the picture: Tak Tik (right), the certified analysis marketplace
that feeds labor into the wheel, and the governance layer (left), comprising LGPD, Digital ECA,
GDPR, and fair-evaluation constraints, which bounds how the wheel may turn.
Figure 5:The AIx4Soccer Wheel: athlete-centred hub, PDI cycle (inner ring), platform modules (middle
ring), stakeholder roles (outer ring), with Tak Tik and governance as orbitals.
7 Towards an Event-Centric Semantic Data Model
The architecture of Section 4 is deliberately conventional: modules over a shared record. In this
section we propose what we regard as the platform’s future data model: the semantic topology
formalized in Section 3.3, in which the central concept is not the athlete, the match, or the club,
but theEVENTof Eq. (1). This is a proposal and a design direction, not a description of the
current implementation.
15

7.1 Why events are the natural center
Football is, at bottom, a stream of events. The sports-analytics community already models the
match this way: commercial and open event-data specifications record every pass, shot, duel, and
foul with position, time, actor, and outcome [30, 31], and representation languages such as SPADL
normalize heterogeneous vendor catalogs into a uniform on-the-ball action vocabulary precisely so
that events become analyzable units [29]. Open tooling (e.g., the kloppy library) and the recently
proposed Common Data Format exist because the field converged on the event as the lingua franca
of match data, while suffering from vendor fragmentation around it [31, 32]. Ontological work in
the same direction, such as RDF-based football ontologies and knowledge graphs populated from
match event feeds, demonstrates that events map naturally onto graph semantics [33].
The volume argument is decisive, and Eq. (8) states it precisely. A single match yields on the
order of 1,600–2,000 recorded events; the open Wyscout corpus alone contains roughly three million
events for one season of seven competitions [30], and research corpora used for action-valuation
models span more than ten million actions across a few seasons [29]. A club’s daily life multiplies
this further: every training drill, load measurement, medical screening, PDI assessment, video
annotation, registration, and marketplace delivery is also an event. Whereas entity tables saturate
(a club has only so many athletes), the event stream grows without bound. It is the platform’s
naturally accumulating asset.
7.2 The proposed topology
Figure 6 sketches the proposed semantic topology, whose formal counterpart is Eqs. (1)–(6). At the
center sits the EVENT as the universal unit of record, carrying five semantic slots: who (actor),
what (typed action), when (timestamp), where (spatial or organizational location), and evidence
(an optional link to video, document, or sensor data), plus an outcome. Around it, anevent-
type taxonomy(Eq. (2)) specializes the concept: match events, training events, medical events,
development events (PDI assessments, goal-settings, reviews), video events, administrative events
(registrations, transfers, contracts), and marketplace events (Tak Tik engagements and deliveries).
Entities (athlete, team, match, session, venue, staff, device) are nodes of the graph that connect
to one another onlythroughevents (Eq. (5)): an athlete and a venue are related because events
occurred there; a coach and a player are related through the assessments, sessions, and reviews that
link them (Eq. (6)). The result is a knowledge graph whose edges are facts with provenance and
time, in the spirit of graph-based integration efforts in football and of spatio-temporal sports-data
research generally [33, 34].
7.3 Architectural analogue: the append-only event log
Software engineering offers a mature architectural analogue:event sourcing, in which system state
is not stored as mutable current values but derived by replaying an append-only log of immutable
domain events [37]. This is exactly the fold semantics of Eq. (7) under the invariant of Eq. (4).
Empirical studies of industrial event-sourced systems document the pattern’s benefits (complete
auditability, temporal “as-of” queries, and retroactive read models built from history) alongside its
real costs in schema evolution [38], and the append-only log is a foundational abstraction of modern
data-intensive systems generally [39]. These properties align remarkably well with the platform’s
obligations: an immutable event history is simultaneously a development record (what was assessed,
decided, and reviewed, and when), a compliance audit trail (who accessed or changed what, relevant
to LGPD/GDPR accountability), and a defensible evidence base for training-compensation and
formation-certification regimes that reward documented contribution over time (Section 9.3).
16

Figure 6:Proposed event-centric semantic data model: the EVENT (hexagon) as the universal unit of
record with who/what/when/where/outcome/evidence semantics; an event-type taxonomy (inner ring); en-
tities linked to one another only through events (outer ring); an append-only log that grows into a knowledge
graph as the platform is populated. Formal counterpart: Eqs. (1)–(8).
17

7.4 What a populated event graph enables
Finally, the event-centric model is forward-compatible with the most interesting current direction
in soccer analytics: treating the match, and potentially the whole life of a club, as alanguage of
events. Action-valuation frameworks such as VAEP already derive player contribution values purely
from event streams (Eq. (9)) [29]. More recently, Large Events Models and transformer-based
foundation models for soccer are trained, in direct analogy to large language models, to predict the
next event given the sequence so far (Eq. (10)), and are proposed as general simulation and analytics
backbones [35, 36]. A platform whose native substrate is a well-typed, ever-growing event log is,
by construction, the ideal data source for such models. In the long run this includes models that
learn not only match dynamics but development dynamics: which sequences of training, assessment,
and review events precede successful athlete outcomes. Interoperability principles (FAIR: findable,
accessible, interoperable, reusable) apply directly, arguing for typed, well-described events with
stable identifiers so that the graph remains machine-actionable as it grows [40]. We propose this
event-centric semantic model as the platform’s north star for data architecture, to be adopted
incrementally as the current module-over-record design is populated.
8 Deployment Context and Current Status
This is an early-deployment, honest-status section; it reports no efficacy metrics and invents no
results.
AIx4Soccer is developed by a Brazil–US partnership.Empower FCserves as the Brazilian
operational partner, the initial real-world environment in which the club-administration, squad,
training, and PDI workflows are exercised.AIx4Soccer, LLC(California, USA) is the technology
partner. The intended user base is institutional and B2B: football clubs, academies, and state and
national federations, not individual consumers.
At the time of writing, the work described is a platform design with an early deployment in
a single Brazilian club/academy context. We make no claims about adoption scale, retention,
competitive outcomes, or development efficacy. The staged evaluation plan of Section 3.4 applies;
we flag explicitly that no outcome data exist yet and that this paper should not be read as evidence
of effectiveness.
9 Discussion
9.1 Democratizing sports science in developing markets
The platform’s guiding thesis is that the binding constraint for most of the football world is not
analytical sophistication but integration and access. Brazil exemplifies the paradox: it is the largest
exporter of players in the world [19, 20], yet its base is under-tooled and under-professionalized,
and its own governing body is actively working to certify and modernize training clubs. A unified,
affordable, federation-scalable record, coupled with a methodology (PDI) and a labor marketplace
(Tak Tik), is a plausible lever precisely because it lowers the barrier that specialized elite tools raise.
This aligns with FIFA’s framing of global footballing inequality as the problem to solve [18], though
we claim alignment of intent, not demonstrated impact.
18

9.2 Youth data protection
Because the primary subjects are minors, data protection is central, not peripheral (R8). Brazil’s
LGPD(Lei Geral de Proteção de Dados, Lei no 13.709/2018) requires that processing of children’s
and adolescents’ data be conducted in theirbest interest, and, for children under 12, withspecific
and prominent consentfrom at least one parent or legal guardian, with controllers making
reasonable efforts to verify that consent (Art. 14) [25]. Brazil’sDigital Statute of the Child and
Adolescent(“Digital ECA,” Law No. 15.211/2025), in force from March 2026, adds design-stage
obligations and prohibits profiling for targeted advertising to minors [26]. This is directly relevant to
any platform holding youth-athlete data. The EUGDPRprovides a comparable but not identical
regime [27]; commentators note the LGPD tends to be more consent-protective for children, while
the GDPR permits legitimate-interest bases with balancing tests. LGPD’s extraterritorial reach
means a US technology partner processing Brazilian minors’ data is squarely within scope. Design
implications include guardian-mediated consent flows (represented as first-class consent events in
the model of Section 3.3), least-privilege access (N1), purpose limitation, data-minimization, and
records of processing. We present these as obligations the architecture must support, and note that
full compliance is an ongoing operational responsibility, not a solved problem.
9.3 Football-governance alignment
The platform’s documentation orientation is congruent with Brazilian formation regulation. The
Lei Pelé(Lei n o 9.615/1998), as amended by Lei no 12.395/2011, provides at Art. 29 that the
training entity may sign a player’s first professional contract from age 16 for a term of up to five
years [22]. The CBF’sCertificado de Clube Formador, regulated in January 2012 (following the
2011 amendment) and updated by later resolutions, attests which clubs meet the legal requirements
for the proper technical and social formation of athletes in Brazil, and entitles a certified club to
pursue the domestic training indemnity (“indenização por formação”) [23]. Internationally, FIFA’s
Regulations on the Status and Transfer of Players provide that training compensation is paid to
a player’s training club(s) when a player signs a first professional contract and on transfers up
to the end of the calendar year of the player’s 23rd birthday (Art. 20 and Annexe 4), while up
to 5% of a transfer fee is distributed as a solidarity contribution to clubs that trained the player
between ages 12 and 23 (Art. 21 and Annexe 5) [24]. Structured, auditable development records
of the kind PDI produces, immutable and datable under the append-only invariant of Eq. (4),
are exactly the evidence base such regimes reward, though we are careful to note that the FIFA
solidarity mechanism attaches to the player’s sporting passport rather than to the CCF, and we do
not overstate the platform’s role in any legal entitlement.
9.4 Algorithmic fairness in talent evaluation
Any system that assists talent evaluation risks encoding bias. Therelative age effectis the over-
selection of players born early in the selection year, documented across large youth-soccer samples
and confirmed meta-analytically [44]. It is the canonical example, and the Belgian reform’s “parallel
teams” [12] and bio-banding [45] were explicit countermeasures (N3). In a German talent-program
dataset of 16,138 U12–U15 players, both subjective and objective assessments of performance were
shown to be biased by relative age, with a skewed distribution toward early-born players [15]. Our
design stance is that assistive features should surface maturation and birth-quarter context, avoid
opaque single-score talent rankings, and keep human judgment accountable; we do not claim to have
solved algorithmic fairness, and we treat it as a first-order design constraint and an open research
problem.
19

9.5 Why general-purpose frontier models are not a substitute and why small,
domain-specific models fit
A natural objection to this entire enterprise is that frontier AI laboratories (e.g., OpenAI, Anthropic,
Google DeepMind) could simply replicate it: their large language models (LLMs) exhibit broad,
near-human competence across tasks [55], and “football knowledge” is abundantly represented in
their web-scale training corpora. We take this objection seriously and argue that it conflates two
different kinds of knowledge and two different kinds of product.
The knowledge that matters here is not in the training distribution.What frontier
models absorb from the web is football’spublicdiscourse: rules, history, punditry, and published
analytics. What this platform manages is football’sprivateoperational record: which drill athlete
Aperformed on Tuesday, what load her sensor registered, what her coach assessed in the last PDI
review, which video clip evidences her progress against goal three. These facts are proprietary,
longitudinal, and club-specific. Crucially, they do not exist anywhere until a system of record like
this one captures them. No amount of pre-training scale can recover data that was never written
down or never shared; the moat is the populated event graph of Section 7, not model capability. A
general model can be granted access to such data via retrieval or fine-tuning, but that presupposes
exactly the structured, well-typed, consented data substrate whose construction is this paper’s
subject: the platform is upstream of any model, frontier or otherwise.
System-of-record duties are hostile to generative behavior.LLMs are prone to halluci-
nation: fluent, plausible, unfounded output. This failure mode is extensively documented and only
partially mitigable [56]. In a system whose subjects are predominantly minors and whose records
feed development decisions, welfare duties, and (Section 9.3) formal training-compensation evidence,
fabricated content is not an inconvenience but a safeguarding and legal hazard. The platform’s core
must therefore be deterministic and auditable (the append-only event log of Section 7.3), with any
generative assistance strictly grounded in, and traceable to, recorded events. Data-protection law
compounds this: LGPD’s best-interest standard and the Digital ECA’s design-stage obligations for
minors’ data (Section 9.2) weigh heavily against routing children’s medical, biometric, and devel-
opmental records through third-party model APIs whose retention and training practices the club
does not control.
Small language models (SLMs) are the architecturally correct fit.The evidence is now
substantial that, for narrow and repetitive task distributions, small models fine-tuned on domain
data match or exceed frontier generalists: carefully curated training data lets sub-4B-parameter
models rival vastly larger ones [57, 58]; large-scale empirical studies report fine-tuned small models
outperforming GPT-4 on most tested specialized tasks [60, 61]; and a prominent position paper
argues that SLMs, being sufficiently powerful, operationally more suitable, and drastically more
economical, are the natural engine of agentic systems that perform “a small number of specialized
tasks repetitively and with little variation” [59], which is a precise description of club workflows
(summarize this session, draft this PDI review from these events, tag this clip). SLMs can be
deployed within the tenant boundary, on-premises or in the platform’s own cloud. This keeps minors’
data inside the LGPD compliance perimeter, at inference costs one to two orders of magnitude below
frontier APIs, and with an alignment surface small enough to audit. Notably, the most relevant
models in football analytics already follow this pattern: the Large Events Models and the soccer
foundation model of Section 7.4 are compact, domain-specific transformers trained on event streams,
not frontier LLMs [35, 36].
Our position is therefore not that frontier laboratories lack the capability to build such systems,
but that the binding constraints favor a vertical platform. These constraints are proprietary longitu-
dinal data, institutional relationships with clubs and federations, regulatory posture toward minors’
20

data, certification of a human labor market, and unit economics at grassroots price points. They
favor a platform whose intelligence layer is built from small, domain-specialized models trained on
its own event graph. In the heterogeneous-system framing of [59], frontier models may still play
a peripheral role for open-ended language tasks; the system of record, and the models that learn
football’s operational language from it, remain domain-native.
9.6 Limitations
This paper has clear limitations. It is a design and position paper: the architecture is described
conceptually and without proprietary detail, so it cannot be independently reproduced from this
text. There is no empirical evaluation and therefore no evidence of usability, adoption, or efficacy.
The deployment is early and confined to a single Brazilian club context, limiting external validity.
Claims about the value of integration and of the PDI/Tak Tik design are argued from the literature
andpractitionerreasoning, notdemonstrated. Finally, thefounders’involvementmeansthisaccount
is not disinterested; we have tried to constrain claims accordingly.
10 Conclusion and Future Work
We have presented a conceptual architecture for AIx4Soccer One Platform: a multi-tenant cloud
SaaS operating system for football club management with an embedded, literature-grounded athlete-
development methodology (the PDI Framework) and a certified two-sided marketplace for video-
analysis labor (Tak Tik, with a 75%/25% analyst/platform split). We accompany it with a formal
specification of the event-centric semantic data model proposed as its future substrate. The design
responds to three documented problems (tool fragmentation, a professionalization gap, and an
athlete-development documentation gap) that fall hardest on clubs and academies outside the elite
European game, and it is aimed squarely at institutional users in developing football markets such
as Brazil.
The contribution is integrative and methodological rather than algorithmic, and the claims are
correspondingly modest: this is what has been designed and begun to be built, grounded in the rele-
vant science, and it is not yet evidence that the approach works. Future work is therefore primarily
empirical: staged usability and adoption studies at the test club; measurement of engagement over
time; careful, ethics-reviewed study of whether structured, video-evidenced development documen-
tation changes practice; and evaluation of the marketplace’s ability to clear the analyst matching
problem and of its certification as a quality signal. Additional work should address fairness auditing
of any assistive evaluation features, interoperability with incumbent data vendors, and the opera-
tional realities of LGPD/Digital ECA/GDPR compliance for youth-athlete data at federation scale.
Architecturally, the priority future direction is the event-centric semantic data model of Sections 3.3
and 7: incrementally migrating the platform’s substrate to a typed, append-only event graph that
unifies match, training, medical, development, video, administrative, and marketplace events. As
it is populated, the graph becomes both the club’s institutional memory and the training ground
for the next generation of event-sequence models in football. Consistent with Section 9.5, we ex-
pect that intelligence layer to be built from small, domain-specialized models trained within the
platform’s compliance perimeter, rather than delegated to general-purpose frontier APIs.
Author’s note on scope and honesty.This is a systems/position paper. The AIx4Soccer plat-
form, the PDI/TBIL methodology, and the Tak Tik marketplace are described only at a conceptual
level. No proprietary algorithms, source code, database schemas, internal financial data, pricing
21

(other than the publicly stated 75%/25% marketplace split), or client identities are disclosed. All
quantitative claims about the football industry, existing tools, development frameworks, regulation,
and player-development statistics are attributed to the cited public sources; no empirical results
are claimed for the platform itself. The platform architecture, the PDI methodology, the Tak Tik
marketplace design, and the event-centric semantic data model are the subject of a patent applica-
tion in preparation for filing with the United States Patent and Trademark Office (USPTO); this
preprint constitutes a public scientific disclosure and grants no license to that intellectual property.
References
[1] Rochet, J.-C., &Tirole, J.(2003).PlatformCompetitioninTwo-SidedMarkets.Journal of the European
Economic Association, 1(4), 990–1029. doi:10.1162/154247603322493212
[2] Rochet, J.-C., & Tirole, J. (2006). Two-Sided Markets: A Progress Report.RAND Journal of Eco-
nomics, 37(3), 645–667.
[3] Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The Role of Deliberate Practice in the
Acquisition of Expert Performance.Psychological Review, 100(3), 363–406.
[4] Ericsson, K.A.(2008).DeliberatePracticeandAcquisitionofExpertPerformance: AGeneralOverview.
Academic Emergency Medicine, 15(11), 988–994. doi:10.1111/j.1553-2712.2008.00227.x
[5] Macnamara, B. N., & Maitra, M. (2019). The role of deliberate practice in expert performance:
revisiting Ericsson, Krampe & Tesch-Römer (1993).Royal Society Open Science, 6(8), 190327.
doi:10.1098/rsos.190327
[6] Balyi, I., Way, R., & Higgs, C. (2013).Long-Term Athlete Development. Human Kinetics.
[7] Ford, P., et al. (2011). The Long-Term Athlete Development model: Physiological evidence and appli-
cation.Journal of Sports Sciences, 29(4), 389–402. doi:10.1080/02640414.2010.536849
[8] Premier League. Elite Player Performance Plan (EPPP).https://www.premierleague.com/en/
footballandcommunity/youth-development/eppp
[9] The Football Association. The FA’s 4 Corner Model.https://www.thefa.com/bootroom/resources/
coaching/the-fas-4-corner-model
[10] Professional soccer players’ perceptions of the English FA 4-corner model in supporting first-team
transitions (2024).Journal of Sports Sciences. doi:10.1080/02640414.2024.2335583
[11] FIFA Training Centre. Michel Sablon: Communicating a national playing philosophy to professional
clubs.https://www.fifatrainingcentre.com/
[12] CNN (2021). The Belgian Blueprint: How a small nation became a European football superpower.
https://www.cnn.com/interactive/2021/06/sport/belgium-euro-2020-spt-intl/
[13] DFL Deutsche Fußball Liga. A brief history of German youth academies.https://www.dfl.de/en/
topics/youth-academies/
[14] Thornton, H. R., et al. (2019). Developing Athlete Monitoring Systems in Team Sports: Data Anal-
ysis and Visualization.International Journal of Sports Physiology and Performance, 14(6), 698–705.
doi:10.1123/ijspp.2018-0169
[15] Romann, M., et al. (2021). Relative Age-Related Biases in Objective and Subjective Assessments
of Performance in Talented Youth Soccer Players.Frontiers in Sports and Active Living, 3, 664231.
doi:10.3389/fspor.2021.664231
22

[16] Kalra, S., & Prabhakar, T. V. (2018). Implementation Patterns for Multi-Tenancy (SaaS design pat-
terns).
[17] Whiting, M. E., et al. (2020). Reputation Agent: Prompting Fair Reviews in Gig Markets.Proceedings
of The Web Conference. arXiv:2005.06022.
[18] FIFA. FIFA Talent Development Scheme.https://inside.fifa.com/talent-development
[19] FIFA. International transfers reach historic high in 2024 (Global Transfer Report 2024).https://
inside.fifa.com/
[20] CIES Football Observatory. Monthly Report no100 (May 2025): player-exporting nations 2020–2025.
https://football-observatory.com/
[21] Moran, J., et al. (2024). [Study on academy-to-professional progression rates.]International Journal of
Sports Science & Coaching. University of Essex.
[22] Lei no 9.615, de 24 de março de 1998 (Lei Pelé), Art. 29, as amended by Lei no 12.395/2011. Presidência
da República / Planalto.
[23] Confederação Brasileira de Futebol. Certificado de Clube Formador.https://portaldegovernanca.
cbf.com.br/certificado-clube-formador
[24] FIFA. Regulations on the Status and Transfer of Players (RSTP), Articles 20–21 and Annexes 4–5
(Training Compensation; Solidarity Mechanism).https://inside.fifa.com/
[25] Lei Geral de Proteção de Dados (LGPD), Lei no 13.709/2018, Art. 14 (children and adolescents). Brazil.
[26] Digital Statute of the Child and Adolescent (Digital ECA), Lei no 15.211/2025. Brazil.
[27] Regulation (EU) 2016/679 (General Data Protection Regulation, GDPR).
[28] Ernst & Young / CBF. Impacto do Futebol Brasileiro (2018 data). Confederação Brasileira de Futebol.
[29] Decroos, T., Bransen, L., Van Haaren, J., & Davis, J. (2019). Actions Speak Louder than Goals: Valuing
Player Actions in Soccer.Proceedings of the 25th ACM SIGKDD Conference (KDD ’19), 1851–1861.
doi:10.1145/3292500.3330758
[30] Pappalardo, L., Cintia, P., Rossi, A., Massucco, E., Ferragina, P., Pedreschi, D., & Giannotti, F.
(2019). A public data set of spatio-temporal match events in soccer competitions.Scientific Data, 6,
236. doi:10.1038/s41597-019-0247-7
[31] Anzer, G., Arnsmeyer, K., Bauer, P., Bekkers, J., Brefeld, U., Davis, J., Evans, N., Kempe, M.,
Robertson, S. J., Smith, J. W., & Van Haaren, J. (2025). Common Data Format (CDF): A Standardized
Format for Match-Data in Football (Soccer). arXiv:2505.15820.
[32] PySport. kloppy: standardizing soccer tracking and event data (open-source library).https://kloppy.
pysport.org
[33] An Ontology for the Common Data Format on Football Match Data (2025).CEUR Workshop Proceed-
ings, Vol. 4085.https://ceur-ws.org/Vol-4085/paper56.pdf
[34] Gudmundsson, J., & Horton, M. (2017). Spatio-Temporal Analysis of Team Sports.ACM Computing
Surveys, 50(2), 1–34. doi:10.1145/3054132
[35] Mendes-Neves, T., Meireles, L., & Mendes-Moreira, J. (2024). Towards a foundation large events model
for soccer.Machine Learning, 113, 8687–8709. doi:10.1007/s10994-024-06606-y
[36] Baron, E., Hocevar, D., & Salehe, Z. (2024). A Foundation Model for Soccer. arXiv:2407.14558.
23

[37] Fowler, M. (2005). Event Sourcing. martinfowler.com.https://martinfowler.com/eaaDev/
EventSourcing.html
[38] Overeem, M., Spoor, M., Jansen, S., & Brinkkemper, S. (2021). An empirical characterization of event
sourced systems and their schema evolution — Lessons from industry.Journal of Systems and Software,
178, 110970. doi:10.1016/j.jss.2021.110970
[39] Kleppmann, M. (2017).Designing Data-Intensive Applications. O’Reilly Media.
[40] Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and
stewardship.Scientific Data, 3, 160018. doi:10.1038/sdata.2016.18
[41] Williams, A. M., & Reilly, T. (2000). Talent identification and development in soccer.Journal of Sports
Sciences, 18(9), 657–667. doi:10.1080/02640410050120041
[42] Sarmento, H., Anguera, M. T., Pereira, A., & Araújo, D. (2018). Talent Identification and Development
in Male Football: A Systematic Review.Sports Medicine, 48, 907–931. doi:10.1007/s40279-017-0851-7
[43] Vaeyens, R., Lenoir, M., Williams, A. M., & Philippaerts, R. M. (2008). Talent Identification and
Development Programmes in Sport.Sports Medicine, 38(9), 703–714. doi:10.2165/00007256-200838090-
00001
[44] Cobley, S., Baker, J., Wattie, N., & McKenna, J. (2009). Annual Age-Grouping and Athlete Develop-
ment: A Meta-Analytical Review of Relative Age Effects in Sport.Sports Medicine, 39(3), 235–256.
doi:10.2165/00007256-200939030-00005
[45] Cumming, S. P., Lloyd, R. S., Oliver, J. L., Eisenmann, J. C., & Malina, R. M. (2017). Bio-banding in
Sport.Strength and Conditioning Journal, 39(2), 34–47. doi:10.1519/SSC.0000000000000281
[46] Bergeron, M. F., et al. (2015). International Olympic Committee consensus statement on youth athletic
development.British Journal of Sports Medicine, 49, 843–851. doi:10.1136/bjsports-2015-094962
[47] Bourdon, P. C., et al. (2017). Monitoring Athlete Training Loads: Consensus Statement.International
Journal of Sports Physiology and Performance, 12(s2), S2-161–S2-170. doi:10.1123/IJSPP.2017-0208
[48] Gabbett, T. J. (2016). The training—injury prevention paradox: should athletes be training smarter
and harder?British Journal of Sports Medicine, 50, 273–280. doi:10.1136/bjsports-2015-095788
[49] Mackenzie, R., & Cushion, C. (2013). Performance analysis in football: A critical review and implica-
tions for future research.Journal of Sports Sciences, 31(6), 639–676. doi:10.1080/02640414.2012.746720
[50] Hughes, M., & Franks, I. M. (Eds.) (2004).Notational Analysis of Sport(2nd ed.). Routledge.
[51] Relvas, H., Littlewood, M., Nesti, M., Gilbourne, D., & Richardson, D. (2010). Organizational Struc-
tures and Working Practices in Elite European Professional Football Clubs.European Sport Manage-
ment Quarterly, 10(2), 165–187. doi:10.1080/16184740903559891
[52] Spence, M. (1973). Job Market Signaling.The Quarterly Journal of Economics, 87(3), 355–374.
doi:10.2307/1882010
[53] Akerlof, G. A. (1970). The Market for “Lemons”: Quality Uncertainty and the Market Mechanism.The
Quarterly Journal of Economics, 84(3), 488–500. doi:10.2307/1879431
[54] Parker, G. G., Van Alstyne, M. W., & Choudary, S. P. (2016).Platform Revolution. W. W. Norton &
Company.
[55] Bommasani, R., et al. (2021). On the Opportunities and Risks of Foundation Models. arXiv:2108.07258.
[56] Ji, Z., et al. (2023). Survey of Hallucination in Natural Language Generation.ACM Computing Surveys,
55(12), 1–38. doi:10.1145/3571730
24

[57] Gunasekar, S., et al. (2023). Textbooks Are All You Need. arXiv:2306.11644.
[58] Abdin, M., et al. (2024). Phi-3 Technical Report: A Highly Capable Language Model Locally on Your
Phone. arXiv:2404.14219.
[59] Belcak, P., Heinrich, G., Diao, S., Fu, Y., Dong, X., Muralidharan, S., Lin, Y. C., & Molchanov, P.
(2025). Small Language Models are the Future of Agentic AI. arXiv:2506.02153.
[60] Zhao, J., et al. (2024). LoRA Land: 310 Fine-tuned LLMs that Rival GPT-4, A Technical Report.
arXiv:2405.00732.
[61] Bucher, M. J. J., & Martini, M. (2024). Fine-Tuned ‘Small’ LLMs (Still) Significantly Outperform
Zero-Shot Generative AI Models in Text Classification. arXiv:2406.08660.
[62] Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems
Research.MIS Quarterly, 28(1), 75–105. doi:10.2307/25148625
25
