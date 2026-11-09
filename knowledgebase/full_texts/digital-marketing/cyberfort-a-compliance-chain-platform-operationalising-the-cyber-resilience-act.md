---
title: 'CYBERFORT: A Compliance-Chain Platform Operationalising the Cyber Resilience Act for SMEs'
url: https://arxiv.org/abs/2610.09918
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Nikolaos Kekatos
- Georgios Koutidis
- Mihaela Curcă
- Angelos Fountoulakis
- Marios Ioannou
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.09918
pages: 7
chars: 32997
fetched_at: '2026-11-08T13:22:10+00:00'
kb_version: 1
---

# CYBERFORT: A Compliance-Chain Platform Operationalising the Cyber Resilience Act for SMEs

CYBERFORT: A Compliance-Chain Platform
Operationalising the Cyber Resilience Act for SMEs
N. Kekatos1, G. Koutidis 1, M. Curca 2, A. Fountoulakis 3, M. Ioannou 4, M. Ioannou 5,
E. Iosif 6, P. Lacatus 7, A. Lekidis 8, A. Michael 9, T. Nianios 1
1Clone Systems, Cyprus,{nkekatos, gkoutidis, tnianios}@clone-systems.com; 2Directoratul Nat,ional de Securitate Cibernetic ˘a,
Romania,Mihaela.Curca@dnsc.ro; 3Eximprod Engineering, Romania,angelos.fountoulakis@epg.ro; 4Columbia Shipmanagement,
Cyprus,marios.ioannou@csmcy.com; 5Bolton Technologies, Cyprus,michael@bts.com.cy; 6Dealio, Cyprus,
elias.iosif@dealio.ai; 7I-EnergyLink, Romania,paul.lacatus@i-energylink.eu; 8University of Thessaly, Greece,
alekidis@uth.gr; 9Elias Neocleous & Co. LLC, Cyprus,Avgi.michael@neo.law
Abstract—The EU Cyber Resilience Act (CRA) turns product
cybersecurity into a lifecycle compliance obligation for manu-
facturers, importers, distributors, and integrators of products
with digital elements on the EU market, a load that falls largely
on small and medium-sized enterprises (SMEs) that rarely have
dedicated governance, risk, and compliance (GRC) capacity. We
present CYBERFORT, an open-source CRA-first compliance
platform developed under the EU Digital Europe Programme
and one of twelve projects in the EU CRA cluster. CYBERFORT
operationalises the CRA through a guided scope self-assessment,
a question bank tied to Annex I and the vulnerability-handling
obligations, and a compliance-checking engine that links every
answer to controls, policies, and machine-attested evidence,
reusing ISO/IEC 27001, NIS2, and GDPR controls only where
they coincide with CRA obligations. Its central contribution is
thecompliance chain, a traceable structure linking each product
risk through its controls and policies to the CRA obligations
it satisfies, and onward through evidence to the technical-
documentation file and EU declaration of conformity, so that
every operational gap is traceable and can be closed before
market placement. Deployed at https://access.cyber-fort.eu/ for
a first cohort of 43 organisations, the platform is presented
with the engineering behind the chain, measured results from a
completed end-to-end case study on a SIEM/XDR product with
AI-driven remediation spanning the CRA obligation chapters,
and the controlled effort study that remains in progress.
Index Terms—EU Cyber Resilience Act, SME cybersecurity,
GRC platform, compliance automation, AI-augmented SIEM,
conformity preparation.
I. INTRODUCTION
The Cyber Resilience Act (CRA), Regulation
(EU) 2024/2847, establishes horizontal cybersecurity
requirements for products with digital elements placed on
the EU market [1]. Obligations span the product lifecycle,
from secure-by-design development and risk assessment
through vulnerability handling and reporting to technical
documentation and EU conformity assessment [1]. The burden
falls disproportionately on SMEs: ENISA notes that SMEs
Open-source code (free to use), CRA seed data, framework mappings, and
pilot artefacts: https://github.com/CloneSystems/cyberfort_v3.
© 2026 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
This work has been accepted for publication at the 2026 IEEE International
Conference on Cyber Security and Resilience (IEEE CSR 2026).
make up the bulk of manufacturers, distributors, importers,
and suppliers of products with digital elements in Europe [2],
yet only 12.3% of surveyed SMEs were aware of the CRA
in 2024 compared with 83.5% of very large enterprises [3].
These SMEs typically run security governance on fragmented
spreadsheets, isolated ticketing systems, ad-hoc policies, and
disconnected scanners.
CRA compliance is therefore an ongoing operational task,
not a one-off legal checklist: the SME must track assets, risks,
vulnerabilities, controls, evidence, incidents, and obligations
across overlapping regimes (ISO/IEC 27001, NIS2, GDPR),
where a single CRA control often reuses controls already
implemented for another framework. Without structured map-
ping, that overlap is rarely captured.
This paper presents CYBERFORT, an open-source multi-
framework GRC platform that operationalises CRA require-
ments into a repeatable workflow. CYBERFORT is de-
veloped under the EU Digital Europe Programme (Grant
No. 101190281) and is one of twelve EU-funded projects
in the CRA cluster. Its central design contribution is the
compliance chain(Section III-B), which makes every oper-
ational gap traceable so it can be assigned, monitored, and
closed before market placement. CYBERFORT is deployed at
https://access.cyber-fort.eu/ with first-cohort SME tenants.
A. Contributions
•Acompliance-chain modelthat treats products, risks,
controls, policies, CRA obligations (articles and Annex I
requirements), framework mappings, evidence, corrective
actions, and conformity documents as connected nodes
rather than parallel artefacts.
•FourCRA-oriented modules(compliance mapping and
gap analysis, risk assessment, control and policy man-
agement, and EU conformity) on a multi-framework
data model that reuses ISO/IEC 27001, NIS2, and
GDPR controls and links one evidence object to
many requirements, plus anintegrated scanner layer
(OW ASP ZAP, Semgrep, Syft, OSV Scanner, Nmap) 1 that
1Scanner tools. OW ASP ZAP: https://www.zaproxy.org/; Semgrep: https:
//semgrep.dev/; Syft: https://github.com/anchore/syft; OSV-Scanner: https://
github.com/google/osv-scanner; Nmap: https://nmap.org/
arXiv:2610.09918v1  [cs.CR]  7 Oct 2026

turns SAST/DAST/SBOM/SCA/network findings into Ev-
idence objects attributable to Annex I obligations, with a
dedicated AI-control family (SCF v2025.1 AAT [4]) for
autonomous-operation risks.
•Adeployed, open-source platformserving 43 organi-
sations, with an engineering account of the chain (Sec-
tion III-C) and measured results from a completed case
study on a SIEM/XDR product with AI-driven remediation
(Section V).
II. BACKGROUND ANDRELATEDWORK
a) CRA in brief:The CRA entered into force in Decem-
ber 2024; reporting (Art. 14) applies from September 2026 and
the full essential requirements (Annex I) from December 2027
[5]. Manufacturers must conduct a risk assessment, embed it
into the lifecycle, operate vulnerability handling, and prepare
technical documentation and an EU declaration of conformity
[1]. Legal-analytic work frames the CRA as a hybrid regime
of command-and-control duties, risk-based calibration, har-
monised standards, and enforced self-regulation [6].
b) SME preparedness:CRA awareness among SMEs
is low [3], and Conceicao et al. apply design science to a
lightweight mapping linking commonly implemented controls
to CRA, ISO/IEC 27001, and CIS for resource-constrained
SMEs [7]. Prior EU SME-security initiatives and open-source
CRA-automation work address parts of this problem but rarely
deliver an end-to-end, traceable CRA workflow.
c) EU CRA cluster:CYBERFORT is one of twelve
EU-funded CRA-cluster projects, most supported for MSME
compliance under the Digital Europe Programme [8], [9].
Some coordinate harmonised standards and build SME cyber-
resilience capacity (CYBERSTAND, STAN4CRA, and SE-
CURE4SME)2, while most provide open-source tools and
conformity solutions for SMEs, spanning SBOM, confor-
mity assessment, compliance automation, AI-driven confor-
mity, IoT and microelectronics certification, an SME com-
pliance wizard, and SaaS certification (OCCTET, OSCRAT,
CONFIRMATE, CRACY , CRA-AI, CURIUM, CRACoWi,
and TRUSTBOOST) 3. CYBERFORT complements these
standards- and tool-focused efforts by emphasising an end-
to-end integration layer, the compliance chain, which is not
the primary deliverable of the other cluster projects.
d) Multi-framework GRC market:Commercial GRC
tooling broadly falls into enterprise suites, compliance-
automation tools, and supplier-rating, risk-quantification, and
ecosystem-native suites, each covering only part of the CRA
lifecycle: enterprise suites are organisation-centric and high-
cost, with no product scope, criticality class, operator role,
2Standards and SME-capacity projects. CYBERSTAND: https://cyberstand.
eu/; STAN4CRA: https://www.stan4cra.eu/; SECURE4SME: https://www.
secure4sme.eu/
3Tools- and solutions-for-SME projects. OCCTET: https://occtet.eu/;
OSCRAT: https://oscrat.eu/; CONFIRMATE: https://confirmate-project.eu/;
CRACY: https://cra-cy.eu/; CRA-AI: https://www.cybercertlabs.com/cra-ai/;
CURIUM: https://curium-project.eu/; CRACoWi: https://www.cracowi.eu/;
TRUSTBOOST: https://www.trustboost.eu/
Fig. 1: CYBERFORT objectives checklist: a CRA Chapter II
economic-operator obligation linked to policies, evidence, and
compliance status, i.e. the compliance chain in the UI, with
the CRA-oriented navigation.
or declaration drafting; attestation tools (Drata, Vanta, Se-
cureframe)4 target SOC 2 and ISO 27001 and lack CRA
technical-file or declaration support; SBOM/SCA scanners
and CVE feeds produce findings unmapped to CRA articles,
evidence, or owners; and ENISA crosswalks are read-only
catalogues [9]. Unlike these tools, CYBERFORT ties every
artefact to a specific CRA Annex I obligation and to a line
item of the EU declaration of conformity, integrating standards
mapping, SBOM, risk, controls, evidence, and conformity in
a single compliance chain aligned with the NIST CSF 2.0
functions [10].
III. CYBERFORT PLATFORMOVERVIEW
CYBERFORT is a web-based GRC platform built on a
FastAPI backend, a React front end, and a PostgreSQL
database, with role-based access control, framework seed data,
and integrations to containerised security-assessment tools. Its
data model treats organisations, users, frameworks, objectives,
assets, products, risks, controls, policies, assessments, and
documents as first-class entities. The live deployment (Fig. 1)
exposes a left-side navigation that groups the CRA-relevant ca-
pabilities: Assessments, Frameworks, Assets/Products, Risks,
Controls, Documents (policies, architecture, evidence, EU
declaration of conformity), Technical File, Compliance Chain,
Security Tools, and Audit Engagements, with headline coun-
ters reporting the current first-cohort load (Table I).
A. High-Level Architecture
Figure 2 renders the architecture in five layers: aninput
layer(SME profile, products, assets, scan results); aframework
layer(CRA as primary framework, with ISO/IEC 27001,
NIS2, and GDPR as reusable control sources, GDPR only
where personal-data handling intersects CRA); aservice layer
of sixteen modules in four rows (governance, compliance-
chain data, operations, automation); anintegration layer
(theWrappersbus exposing OW ASP ZAP, Semgrep, Syft,
OSV Scanner, Nmap as Evidence producers); and anoutput
4Attestation-automation tools. Drata: https://drata.com/; Vanta: https://www.
vanta.com/; Secureframe: https://secureframe.com/

layer(technical documents, risk and gap reports, audit pack,
EU declaration draft). Every output traces back to a product,
requirement, risk, control, policy, and evidence object.
B. The Compliance Chain
Traditional GRC tools store requirements, controls, policies,
and evidence as separate artifacts. The compliance chain
instead treats them as connected nodes in a traceable path. The
platform stores this path from a product to its CRA obligations
and the conformity artefacts:
product/asset→product risk→mapped control→
policy/procedure→CRA obligation (Annex I ob-
jective)→assessment answer with linked evidence
→gap or conformity status→corrective action
→technical documentation→EU declaration of
conformity.
A concrete instance from the NextGen SIEM Pro case study
(Section V) traverses the same path end to end:
product SBOM component(vulnerable third-party dependency)
→product risk“known-vulnerable dependency shipped”→con-
trolISO/IEC 27001 A.8.8, technical-vulnerability management→
vulnerability- and patch-management policy→CRA obligation
Annex I Part I §(2)(a), no known exploitable vulnerabilities
→assessment answerpartially covered, evidenced by anOSV-
Scanner report over the SBOM→open corrective action (up-
grade pending)→technical-file vulnerability-handling record→
EU declaration line item.
The chain lets SMEs answer audit questions directly: which
CRA requirement a control satisfies, which product risk jus-
tifies it, what evidence proves implementation, and which
gap blocks readiness. It also supports cross-framework evi-
dence reuse: a single penetration-test report can support CRA
secure-by-design, ISO/IEC 27001 vulnerability-management,
and NIS2 risk-management obligations, so the platform stores
one evidence object linked to many requirements rather than
duplicating uploads.
C. Implementation and Engineering
a) Chain representation:The compliance chain is stored
relationally in PostgreSQL rather than in a separate graph
database. Each chain node type (product, asset, risk, control,
policy, objective, evidence, assessment answer, corrective ac-
tion, document) is a first-class table, and each chain edge
is a typed association row (for example asset–risk, risk–
control, control–policy, policy–objective) carrying the map-
ping metadata used by gap analysis (mapping type, coverage
level, owner, review status, evidence type). A chain query is
therefore a parameterised join, expressed as recursive common
table expressions over the association tables, returning every
node and edge on the product-to-declaration path. A relational
design is appropriate because the chain has bounded, well-
typed depth and the dominant access pattern is typed traversal
and roll-up rather than open-ended path search; it also lets
an SME self-host one database engine instead of a dedicated
graph store.
b) API and backend:The backend is layered as routers,
services, repositories, and models, with typed data-transfer
objects validating every request and response and an auto-
generated OpenAPI specification documenting the REST sur-
face. Role-based access-control middleware enforces per-
tenant isolation, so a single deployment serves many SMEs.
Scan execution is asynchronous: the Orchestrator enqueues
scan jobs through theWrappersbus and the API returns
immediately, so long-running scans never block the request
path.
c) Deployment and scale:The platform and its scan-
ner wrappers are packaged as containers and deployed with
Docker Compose behind a reverse proxy, so an SME can self-
host on a single virtual machine or use the hosted instance at
access.cyber-fort.eu. That instance sustains the first
cohort of 43 organisations on a modest single node; the API
workers are stateless and scale horizontally, and because scans
run out of band the request path is decoupled from scan cost.
Systematic load benchmarking (concurrent assessments, large-
SBOM scans, and chain-traversal latency as the graph grows)
is planned.
IV. PROPOSEDCRA MODULES
A. Compliance Mapping and Gap Analysis
The compliance-mapping module is the core of
the multi-framework approach [1], [10]. It maintains
mappings between CRA provisions and controls from other
frameworks: CRA secure-by-default requirements may
map to configuration-management, secure-development,
and vulnerability-management controls in ISO/IEC 27001,
and NIS2 incident-handling and vulnerability-disclosure
obligations to CRA vulnerability handling and reporting.
Mappings are structured objects (source requirement, target
control, mapping type, coverage level, evidence type, owner,
review status), and each requirement is classified as fully,
partially, or not covered, not applicable, or requiring review.
Gap analysis then computes missing controls, missing
evidence, outdated policies, open corrective actions, and
unassessed products.
B. Risk Assessment
The CRA explicitly requires cybersecurity risk assessment
for products with digital elements [1]. CYBERFORT’s risk
module links product assets, threats, vulnerabilities, impacts,
likelihood, severity, residual risk, and treatment actions, sup-
porting both organisational and product-specific risks; product
records additionally capture intended purpose, foreseeable use,
operational environment, support period, components, and
third-party dependencies. Risk outputs feed the compliance
chain: a risk of shipping known exploitable vulnerabilities,
for instance, can require a vulnerability-management control,
a patch-management policy, scan evidence, and a corrective
action.

EU CRA ISO/IEC 27001 NIS2 GDPR
Enter name
Enter Organization
Define assets
Choose frameworks
Check scope, requirements
Maturity
Maritime Energy
Finance SOC / MSSP
Assessments Documents Policies Compliance Advisory
Risks Evidences Objectives Report Generator
Controls Incidents Auditor Assignment Scope Assessment
Orchestrator AI Engine Compliance Mapping Gap Analysis
Wrappers (integration bus)
DAST
(dynamic)
SAST
(static)
SBOM
generation
SCA &
vuln. scan
Network
discovery
Technical Documents
Risk Results
Declaration of Conformity
Audit Pack
Assessment Results
Artifacts (PDF / Word / Excel)
SMEs Feedback /
Content Improvement
Primary framework Additional reusable frameworks
User / SME
Pilots
CYBERFORT Platform
Assessment tools (containerized)
Outputs
onboarding
inputs
traceable
outputs
scan evidence
feedback
Fig. 2: CYBERFORT architecture. The regulatory layer (top) splits the primaryEU CRAframework from reusable frameworks
(ISO/IEC 27001, NIS2, GDPR). The central platform exposes sixteen modules in four rows (governance, compliance-chain
data, operations, automation) over aWrappersbus connecting the containerised assessment tools. SME inputs and pilots sit
left, CRA-oriented outputs right, with a dashed feedback loop.
C. Control and Policy Management
The controls and policies module maintains the operational
implementation layer required by CRA lifecycle governance
and technical-documentation obligations [1]: controls link
to risks and requirements, policies document how controls
are implemented, and evidence demonstrates implementation.
Representative policies span product cybersecurity, secure
software development lifecycle, vulnerability and patch man-
agement, product lifecycle support, risk-management method-
ology, logging and monitoring, and market-surveillance com-
munication. Beyond templates that reduce drafting effort, the
module tracks ownership, approval, version history, review
dates, applicability, mapped requirements, linked evidence,
and open exceptions, so that each policy is linked to CRA
obligations and product risk rather than merely stored.
D. EU Conformity Support
The EU conformity module supports the technical docu-
mentation and declaration material required before placing
products on the EU market [1]. It collects product informa-
tion, operator role, criticality class, applicable requirements,
conformity route, standards, risk assessment, test evidence,
vulnerability-handling procedures, user instructions, and dec-
laration content, and generates a readiness package (technical-
documentation checklist, declaration draft, evidence index,
open gaps, corrective-action plan). It does not replace notified-
body or legal review; it provides structured preparation and
traceability so SMEs can see what is missing before formal
assessment.
E. Scanner Integration and Evidence Automation
The scanner-integration module realises theWrapperslayer
of Fig. 2: it embeds containerised security-assessment tools
(dynamic and static application testing, software-composition
analysis, and network discovery) into the compliance chain
so that technical findings become first-class evidence. Each
wrapper is a microservice with a uniform REST interface,
so additional tools can be added without changing the plat-
form core. Each scan execution is anchored to a product,
an assessment, and one or more CRA objectives; the Or-
chestrator schedules scans, normalises results, and creates
evidence objects that the mapping and conformity modules
attribute to specific Annex I requirements and product risks.
Evidence records retain provenance (tool, version, scan date,
target hash, signed result) so auditors can verify freshness
against the CRA support period. Figure 3 shows the aggregate
Scan Findings view for one onboarded product: 463 findings
across dependency (232), web-application (140), code (72),
and network (19) scanners, rolled up by severity (13 high,
286 medium, 164 informational) and by risk linkage (52, i.e.
11%, already tied to product risks), with each finding available
as an Evidence object for the compliance chain.
F . End-to-End Workflow
The five modules are run as a six-step workflow that
embeds risk assessment across the product lifecycle [1]: (i)
import the CRA framework template; (ii) register products and
identify operator role and criticality; (iii) perform a product
risk assessment; (iv) run a conformity assessment, linking

Fig. 3: Aggregate Scan Findings view: multi-scanner evidence
normalised into one register, rolled up by severity and risk
linkage, available as Evidence objects for Annex I Part II.
answers to evidence and policies; (v) compute coverage and
gaps and assign corrective actions; and (vi) export a readiness
package.
V. EVALUATION
We evaluate whether CYBERFORT reduces CRA prepa-
ration effort and improves traceability for SMEs. The evalu-
ation reuses pilot scenarios from CYBERFORT deliverables
rather than synthetic requirements, and spans four SME pro-
files covering the economic-operator roles and product types
SMEs most commonly encounter: (i) a managed-security-
services manufacturer (Clone Systems) ofNextGen SIEM
Pro(SEUXDR), a Wazuh 4.x and OpenSearch SIEM/XDR 5
with a ReAct-based [11] active-response agent, classified as
an Annex III Class I important product; (ii) a regulated
fintech (Dealio) for continuous compliance management; (iii)
a maritime operator (Columbia) for shipboard and operational-
value-chain preparedness; and (iv) an energy-sector provider
(Eximprod Engineering) for vulnerability assessment and re-
mediation reporting on hardware-plus-software products. Only
the NextGen SIEM Pro case has been executed end-to-end on
the live platform; it yields the measured results below, while
the other three pilots are provisioned and in progress.
A. Metrics
The evaluation records five metrics:requirement cover-
age and gap detection(share of applicable CRA objec-
tives mapped to controls, policies, risks, and evidence,
and the number and severity of gaps);time-to-assessment
(time to complete the first CRA conformity assessment and
export a report);evidence completeness and reuse(share
of answers with linked evidence, and evidence artifacts
reused across CRA, ISO/IEC 27001, NIS2, GDPR, and
NIST CSF 2.0);conformity-document readiness(complete-
ness of the technical-documentation checklist, evidence index,
records, and EU declaration draft); anduser acceptance(us-
ability, clarity, and confidence in outputs).
B. Measured Results: NextGen SIEM Pro
The NextGen SIEM Pro scenario was executed end-to-
end on the live CYBERFORT instance with Clone Systems
5Wazuh: https://wazuh.com/; OpenSearch: https://opensearch.org/
TABLE I: Measured results for the completed NextGen SIEM
Pro case study and the live first-cohort deployment
Metric Measured value
Requirement coverage 27 of 42 CRA objectives (64%) mapped to≥1
control, spanning the CRA obligation chapters
Gap detection 15 uncovered objectives flagged as assignable
gaps; 30 risks at severity 12 critical, 14 high,
4 medium
Risk selection 30 product risks narrowed from a 104-item
template library
Control mapping 65 controls (55 baseline plus 10 SCF AAT
controls for autonomous operation)
Policy linkage 32 policies linked as compliance-chain nodes
Automated evidence Multi-scanner findings (dependency, code,
web-application, network) ingested as Evi-
dence objects mapped to Annex I Part II
Traceability complete-
ness
100% of covered answers linked to≥1 control,
policy, and objective; every covered objective
linked to≥1 risk
Conformity-document
readiness
Technical-file checklist, evidence index, and
EU declaration draft generated
Deployment scale
(live)
43 organisations, 109 users, 60 frameworks,
918 policies, 1213 risks
acting as the manufacturer. The product was registered as
software with digital elements, classified as an Annex III
Class I important product, and given an attached SBOM; a
CRA risk register, control register, policy set, and confor-
mity assessment were then built on the same instance, and
Table I reports the measured outcomes against the metrics
above. CYBERFORT’s CRA framework template decomposes
Annex I (Parts I and II) together with the Article-level lifecycle
duties into 42 assessable objectives; for this product 27 were
mapped to at least one control and the remaining 15 surfaced
as gaps. Covered objectives concentrated on application and
API security, identity and access control, automation oversight,
vulnerability exploitation, supply chain, governance, data se-
curity, and operational resilience. The integrated scanner layer
was run and its findings ingested as Evidence: an SBOM
(Syft) was attached and analysed for known-vulnerable de-
pendencies (OSV-Scanner), with static analysis (Semgrep),
dynamic application testing (OW ASP ZAP), and network
discovery (Nmap) contributing further findings. Each finding
is stored as an Evidence object carrying its provenance (tool,
version, scan date, target) and mapped to the relevant Annex I
Part II vulnerability-handling obligation. Every assessment
answer links to at least one control, one policy, and one CRA
objective, and every covered objective links back to at least
one product risk, giving full intra-chain traceability for the
covered scope; the 15 remaining objectives surface as explicit,
assignable gaps. The same instance concurrently sustains the
first cohort of 43 organisations (Table I), indicating multi-
tenant scale rather than a single case.
C. Threats to Validity and Planned Controlled Study
The principal limitation is that the completed case study
was performed by Clone Systems, the SME that also de-
velops CYBERFORT, so it is an existence proof for end-to-
end traceability rather than independent evidence of usability
and effectiveness; we accordingly restrict its claims to chain

TABLE II: CRA obligation coverage by CYBERFORT mod-
ules
CRA obligation family Support Primary CYBERFORT arti-
fact
Product scoping and
economic-operator role
(Arts. 3, 13)
Full Product registry, scope-
assessment screen
Essential cybersecurity
requirements (Annex I,
Part I)
Full Framework objectives,
conformity self-assessment,
control mapping
Vulnerability handling
(Annex I, Part II)
Full Vulnerability-management pol-
icy, SBOM linkage, evidence
records
Cybersecurity risk assess-
ment (Art. 13)
Full Product risk register, residual
risk, treatment plan
Technical documentation
(Annex VII)
Partial Technical-file checklist,
evidence index
EU declaration of confor-
mity (Annex V)
Partial Declaration draft generator and
evidence references
Conformity assessment
procedures (Art. 32)
Partial Routing per criticality class;
notified-body workflow planned
Reporting obligations
(Art. 14)
Partial Vulnerability and incident
records; ENISA portal
integration planned
Market surveillance and
CE marking (Art. 30,
Ch. V)
Partial CE marking checklist; market-
surveillance workflow planned
Authorised representative,
importer, distributor duties
(Arts. 18–20)
Partial Role attributes on product; per-
role workflows planned
expressiveness for a realistic scenario combining conventional
and AI/autonomous-operation risks, and full intra-chain trace-
ability for the covered scope. The three independent pilots
(Dealio, Columbia, Eximprod Engineering) are provisioned to
supply the external evidence this case cannot.
The metrics that require a baseline (time-to-assessment,
cross-framework evidence-reuse magnitude, and user-
acceptance ratings) are not reported here because the
controlled study is still running. That study pairs each pilot
SME against a spreadsheet-and-free-form baseline and adds
a structured expert review in which two to four practitioners
(SME consultants, internal CISOs, and a notified-body-facing
assessor) audit the generated compliance chain, declaration
draft, technical-file checklist, and evidence index and rate
usability and trustworthiness. Consistent with prior SME
compliance work [3], [7], we expect reduced duplicate
evidence handling, higher traceable coverage, and shorter
time to a readiness package, and report it as an indicative
effort study rather than a controlled experiment.
D. Coverage of CRA Obligations
Table II summarises which CRA obligation families are
operationally supported by CYBERFORT today and which
remain partial or out of scope, making explicit which artifacts
the platform produces for each obligation family.
VI. DISCUSSION, CONCLUSION,ANDFUTUREWORK
This paper presented CYBERFORT, a CRA-first
compliance-chain platform for SMEs, with four CRA-
oriented modules and an integrated scanner layer that turns
technical findings into Evidence objects linked to CRA
Annex I obligations and an EU declaration of conformity.
The engineering account (Section III-C) realises the chain
on a relational data model with typed association tables, an
asynchronous scan orchestrator, and a self-hostable container
deployment, while the completed case study (Section V)
demonstrates full intra-chain traceability across 27 of 42 CRA
objectives for a SIEM/XDR product spanning conventional
and AI/autonomous-operation risks, at multi-tenant scale.
Four directions remain: making cross-mapping evidence-
aware, with each mapping object carrying strength, assump-
tions, evidence types, and review status; extending evidence
automation from the scanner wrappers to CI/CD pipelines,
ticketing systems, and signed approvals, with freshness mea-
sured against the CRA support period; adding role-specific
conformity workflows for importers, distributors, and au-
thorised representatives, and integrating the ENISA single-
reporting platform for Art. 14; and running the controlled
effort study and expert-review audit of Section V across the
three independent pilots to supply the comparative and external
evidence the present case study cannot.
ACKNOWLEDGMENT
This work has received funding from the European
Union’s Digital Europe Programme under grant agreement
No 101190281 (CYBERFORT). The authors thank the whole
CYBERFORT consortium and SME stakeholders whose re-
quirements informed the platform design.
REFERENCES
[1] European Parliament and Council of the European Union, “Regulation
(EU) 2024/2847 on horizontal cybersecurity requirements for products
with digital elements (Cyber Resilience Act),” Official Journal of the
European Union, 2024. [Online]. Available: https://eur-lex.europa.eu/
eli/reg/2024/2847/oj/eng
[2] ENISA, “SME Cyber Resilience Act Survey,” 2025. [Online]. Avail-
able: https://www.enisa.europa.eu/topics/awareness-and-cyber-hygiene/
sme-cyber-resilience-act-survey
[3] C. Szedlak, H. Reinemann, and S. Hatzelmann, “Ensuring Cybersecurity
Compliance: Assessing SME Awareness and Preparedness for the Cyber
Resilience Act,” inProceedings of the 5th Asia Pacific Conference on
Industrial Engineering and Operations Management, 2024.
[4] Secure Controls Framework, “SCF v2025.1: AI & Autonomous
Technologies (AAT) family,” 2025. [Online]. Available: https://
securecontrolsframework.com/
[5] European Commission, “Cyber Resilience Act,” 2025. [Online]. Avail-
able: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
[6] F. Teichmann and B. S. Sergi, “The EU Cyber Resilience Act: Hybrid
governance, compliance, and cybersecurity regulation in the digital
ecosystem,”Computer Law & Security Review, vol. 59, p. 106209, 2025.
[7] F. Conceicao, M. Rocha, and F. Almeida, “Security Compliance as a
Catalyst for Sustainable Partnerships: A Design Science Approach for
SMEs,”Journal of Cybersecurity and Privacy, vol. 6, no. 2, p. 53, 2026.
[8] European Commission, “The Cyber Resilience Act and MSMEs: EU-
funded projects supporting SME compliance,” Shaping Europe’s digital
future, 2025. [Online]. Available: https://digital-strategy.ec.europa.eu/
en/policies/cra-msmes
[9] ENISA, “Cyber Resilience Act Requirements Standards Mapping,”
2024. [Online]. Available: https://www.enisa.europa.eu/publications/
cyber-resilience-act-requirements-standards-mapping
[10] National Institute of Standards and Technology, “The NIST
Cybersecurity Framework (CSF) 2.0,” 2024. [Online]. Available:
https://www.nist.gov/cyberframework

[11] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y . Cao,
“ReAct: Synergizing Reasoning and Acting in Language Models,” in
Proceedings of the International Conference on Learning Representa-
tions (ICLR), 2023.
