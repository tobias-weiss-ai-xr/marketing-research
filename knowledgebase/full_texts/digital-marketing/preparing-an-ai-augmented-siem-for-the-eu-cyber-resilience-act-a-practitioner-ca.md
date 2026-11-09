---
title: 'Preparing an AI-Augmented SIEM for the EU Cyber Resilience Act: A Practitioner Case Study'
url: https://arxiv.org/abs/2610.07873
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Georgios Koutidis
- Nikolaos Kekatos
- Marina Korgiala-Karyda
- Alexios Lekidis
- Tom Nianios
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.07873
pages: 7
chars: 35674
fetched_at: '2026-11-08T13:22:06+00:00'
kb_version: 1
---

# Preparing an AI-Augmented SIEM for the EU Cyber Resilience Act: A Practitioner Case Study

Preparing an AI-Augmented SIEM for the EU
Cyber Resilience Act: A Practitioner Case Study
Georgios Koutidis∗, Nikolaos Kekatos ∗, Marina Korgiala Karyda †, Alexios Lekidis †, and Tom Nianios ∗
∗Clone Systems, Larnaca, Cyprus
{gkoutidis, nkekatos, tnianios}@clone-systems.com
†University of Thessaly, Larissa, Greece
korgialamarina@gmail.com, alekidis@uth.gr
Abstract—The EU Cyber Resilience Act (CRA), Regulation
(EU) 2024/2847, makes product cybersecurity a lifecycle obliga-
tion for products with digital elements on the EU market: risk as-
sessment, vulnerability handling, conformity documentation, and
Article 14 incident- and vulnerability-reporting readiness must be
operational before market placement. Small and medium-sized
enterprises that build security products are doubly exposed, since
their products are in scope while their customers expect them to
be exemplary. This case study documents a CRA preparedness
pilot for one such product,SEUXDR, an AI-augmented security
monitoring product with a large-language-model active-response
component, on the open-source CYBERFORT platform. We
contribute a reproducible six-step recipe (Scope and Classify,
Asset Registration, Produce Evidence, Map to CRA, Gap and
Actions, Audit Pack), two end-to-end traceability threads, and
a pilot snapshot tracing product risks through baseline and
AI-specific controls and policies to CRA objectives. It offers
practitioners a replicable starting point for translating CRA
legal text into operational preparedness for incident response,
vulnerability reporting, and conformity assessment.
Index Terms—Cyber Resilience Act, preparedness, situational
awareness, incident response readiness, conformity preparation,
SME cybersecurity, AI-augmented SIEM, case study.
I. INTRODUCTION
The EU Cyber Resilience Act (CRA) establishes mandatory
horizontal cybersecurity requirements for products with digital
elements made available on the EU market [1]. It entered
into force in December 2024; the Article 14 vulnerability-
and incident-reporting obligations apply from September 2026,
and the essential cybersecurity requirements (Annex I) from
December 2027. Manufacturers must document a cybersecu-
rity risk assessment, embed it in the product lifecycle, operate
a vulnerability-handling process, track actively exploited vul-
nerabilities and severe incidents, and prepare conformity doc-
umentation including the EU declaration of conformity. CRA
compliance is therefore not a one-off checklist but an ongoing
preparednessproblem: continuous visibility over assets, risks,
controls, evidence, and incident-response artefacts must be in
place before the regulation applies.
© 2026 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
This work has been accepted for publication at the 2026 IEEE International
Conference on Cyber Security and Resilience (IEEE CSR 2026).
Small and medium-sized enterprises (SMEs) that build
security products are doubly exposed. Their products are in
scope, since a Security Information and Event Management
(SIEM) system, an Extended Detection and Response (XDR)
tool, or an Endpoint Detection and Response tool is itself
software with digital elements, and many fall under Annex III
as important products, Class I in the case of SIEM sys-
tems. At the same time, customers expect security vendors
to lead on security, yet those same SMEs typically run on
small governance, risk, and compliance (GRC) teams with
spreadsheets and ad-hoc evidence collection; recent work by
the EU Agency for Cybersecurity (ENISA) documents how
low CRA awareness still is among small manufacturers [8].
A key observation motivates this work: an open-source SIEM
such as Wazuh1 detects, correlates, and responds to threats, but
produces none of the conformity artefacts the CRA requires.
The distance between a working SIEM and a CRA-ready prod-
uct is precisely the documentation, traceability, and reporting
workflow this case study builds, and bridging it is tractable
only once someone has done it end-to-end on a real product.
This case study documents that exercise forSEUXDR
(NextGen SIEM with AI Remediation), an AI-augmented
SIEM/XDR product developed by Clone Systems, on the
open-source CYBERFORT platform [2],2 built specifically for
SMEs preparing for the CRA. The central idea is thecom-
pliance chain, a traceable path linking each CRA obligation
through framework controls, product risk, policies, technical
evidence, and assessment status all the way to the technical-
documentation file and EU declaration of conformity, intro-
duced in [2] and applied end-to-end on a real product here.
The paper is intentionally narrative and screenshot-led: it
documents what we entered, what the platform produced, what
we changed, and what we wish we had known. At a high
level, the contributions are: (i) a reproducible six-step CRA
preparedness recipe aligned with SME engineering reality;
(ii) a concrete worked example on an AI-augmented secu-
rity product (SEUXDR), spanning both conventional SIEM
exposures and Large Language Model (LLM)-driven active-
response risks; (iii) an end-to-end traceability matrix from
1Wazuh, the open source security platform: https://wazuh.com/.
2Platform: https://cyber-fort.eu/; open-source code: https://github.com/
CloneSystems/cyberfort_v3; hosted instance, free after registration: https:
//access.cyber-fort.eu/.
arXiv:2610.07873v1  [cs.CR]  6 Oct 2026

product risks through controls and policies to CRA objectives,
including Article 14 reporting-readiness artefacts; (iv) a pilot
snapshot with quantitative coverage and the CRA-oriented
audit-pack reports; and (v) case-study lessons, advantages,
and limitations for AI-augmented security products under the
CRA. The remainder covers CRA background and positioning
(§II), pilot setup (§III), the recipe (§IV), results (§V), discus-
sion (§VI), and conclusion (§VII).
II. BACKGROUND ANDRELATEDWORK
Beyond the obligations and timelines of §I, the CRA’s An-
nex I states the essential requirements, Annex III lists impor-
tant products, and conformity routes range from manufacturer-
internal control to third-party assessment by product class.
Several resources translate this text into engineering vocab-
ulary: ENISA’s CRA-to-standards mapping [3] relates An-
nex I to harmonised standards, NIST CSF 2.0 [5] and
IEC 62443 [4] supply reusable control catalogues, and the
companion paper [2] describes the CYBERFORT platform and
the compliance-chain model in full.
Two gaps remain. First, the SME-readiness literature is
largely diagnostic: ENISA-aligned surveys report low aware-
ness among small manufacturers [8] but not what a manufac-
turer must actually produce before review. Second, standards
crosswalks describewhatmaps towhat, nothowa small team
assembles, links, and evidences those mappings on a concrete
product, still less one embedding AI in its decision loop. End-
to-end practitioner case studies on a real product with AI
components remain rare, the space this paper occupies.
The novelty is best stated against a traditional SIEM. A
conventional SIEM/XDR such as Wazuh is a securitycontrol:
it ingests logs, correlates events, scores severity, and can drive
active response, but it is not a compliance instrument. It does
not register the product as a CRA asset, map its residual
risks to Annex I obligations, maintain approved policies and
a provenance-tracked evidence index, or emit the technical
documentation and EU declaration of conformity. The ap-
proach here wraps such a SIEM in a GRC layer that produces
exactly those artefacts and the end-to-end traceability (the
compliance chain) an auditor consults, so an existing detection
tool becomes a CRA-ready product with one navigable source
of truth from each Common Vulnerabilities and Exposures
(CVE) entry and product risk to the CRA objective it touches,
without bespoke tooling or a dedicated compliance team.
III. PILOTSETUP: SEUXDRANDCRA SCOPE
This section fixes the two things that drive every later
artefact: what the product is (§III-A–§III-B) and what the CRA
says about it (§III-C).
Clone Systems CY LTD is a Managed Security Service
Provider based in Larnaca, Cyprus; it ships SEUXDR and acts
as the CRA manufacturer. The pilot began in October 2025
with six engineers (product, security, and GRC) executing the
six recipe steps described in Section IV.
CYBERFORT platform (Wrappers & AI helper)SEUXDR product (manufacturer boundary)
Customer endpoints (out of CRA product scope)
Next.js dashboard
(port 3000, JWT cookie)
FastAPI gateway
(port 8000, BFF & auth)
PostgreSQL
users, scans, invitations
SEUXDR / Wazuh manager
(TLS 8443, mTLS 8081)
OpenSearch indexer
(event store)
OW ASP ZAP
DAST
Semgrep
SAST
Syft & OSV
SBOM & SCA
Nmap
network
Ollamaphi4:14b
SOC analyst (ReAct)
Linux
agent
Windows
agent
macOS
agent . . .
cookie / JSON
audit HTTP/REST
SIEM proxy
events
alert
decision
Fig. 1: SEUXDR system view: SEUXDR manufacturer boundary on the left,
CYBERFORT tooling block (Wrappers & AI helper) on the right, customer-
side agents below. DAST: dynamic application security testing; SAST: static
application security testing; SBOM: software bill of materials; SCA: software-
composition analysis.
A. Architecture and Operator Surface
SEUXDR is delivered as a multi-tenant web application
whose SIEM workspace is organised into six tabs (Overview,
Alerts,Agents,Remediation,Installer, andMITRE ATT&CK)
covering host-based intrusion detection, log analysis, and
active response across Linux, Windows, and macOS endpoints.
Figure 1 shows the system view derived from the product’s
two open-source repositories, with two trust boundaries: the
SEUXDR manufacturer scope on the left, and the CYBER-
FORT platform (containerised scanners plus a local Ollama
phi4:14bsecurity operations centre (SOC) analyst) on the
right. The endpoint agents (dotted frame) communicate with
the manager over mutual Transport Layer Security (mTLS)
using a “smart manager / dumb agent” active-response pattern:
the manager generates OS-specific commands that agents run
through a whitelisted executor.
a) Endpoints / Agents:Self-updating agents on Win-
dows, Linux, and macOS provide log shipping and file-
integrity monitoring, registering via mTLS-anchored identities.
TheInstallertab generates a one-shot installer per platform;
registered endpoints appear under theAgentstab, each with a
Deactivateaction that revokes its certificate.
b) Manager:The manager runs Wazuh with an
OpenSearch backend for alert correlation, storage, and severity
scoring. TheAlertsdashboard (not pictured) exposes filtering
and severity views, and theMITRE ATT&CKtab lets analysts
pivot from a triggered alert into the corresponding adversary
technique.
c) AI Actions:An LLM-driven agent (a locally hosted
model, accessed via Ollama 3) consumes Wazuh alerts and
selects active-response actions using a ReAct-style reason-
then-act loop [6], falling back to rule logic when the model is
unavailable or the action lies outside its sanctioned playbook
scope. ARemediationtab (not pictured) lets the operator re-
view AI behaviour, trigger manual remediation, and audit per-
agent histories, with drill-downs exposing the Active Response
feed and Failed Alerts stream for human-in-the-loop oversight.
3Ollama, run large language models locally: https://ollama.com/.

TABLE I: SEUXDR component-to-threat-to-Annex I mapping
Component CRA-relevant threats Annex I obligation
Dashboard /
gateway
(Next.js &
FastAPI)
Broken authentication, session
fixation, API abuse, insecure
direct object reference
Annex I (2)(d) protection from
unauthorised access; (2)(e)
confidentiality
SIEM manager
(Wazuh &
indexer)
Tampered logs, lost integrity of
evidence, supply-chain
compromise of ruleset
Annex I (2)(f) integrity of data;
Part II (vulnerability handling)
AI SOC
analyst (Ollama
phi4:14b)
Emergent / unsafe autonomous
actions, model drift,
privileged-action escalation,
prompt manipulation
Annex I (2)(i) minimise
negative impact; Art. 13
(manufacturer duties)
Endpoint
agents (mTLS)
Credential theft, lateral
movement via active-response
channel, replay of remediation
commands
Annex I (2)(j) limit attack
surfaces; (2)(k) reduce impact
of incidents
TLS secures the web and application programming interface
(API) surface and mTLS the agent channel; authentication
uses JSON Web Tokens (JWT) with role-based access control
(RBAC), audit-logged throughout.
B. Threat Model and Why the Product Is Non-Trivial
SEUXDR is itself a security product placed on the EU
market by Clone Systems acting as manufacturer, and its AI
Actions component raises CRA-relevant risks (unsafe actions,
model drift, privileged automation) that go beyond the baseline
SIEM threat model and require additional controls from the
Secure Controls Framework (SCF) [11], specifically itsAI &
Autonomous Technologies(AAT) family. Table I maps the four
product components in Fig. 1 to the CRA-relevant threats they
expose and the Annex I obligation each triggers.
The threats in Table I were enumerated method-by-method
rather than ad hoc: we decomposed SEUXDR into its four
trust-bounded components (Fig. 1) and applied three estab-
lished methods per component: STRIDE [7] for the dashboard,
gateway, and manager data flows; the OW ASP Top 10 [9]
for the web and API surface; and MITRE ATT&CK [10]
techniques already encoded in the Wazuh ruleset for the
agent and active-response channel. Threats specific to the AI
Actions component (emergent or unsafe autonomous actions,
model drift, privileged-action escalation, prompt manipula-
tion), which none of the three baseline methods cover, were
drawn from the SCF AAT family. Each enumerated threat was
then mapped to the Annex I obligation it triggers, and that
mapping seeds the Step 4 risk register.
C. CRA Classification and Resource Footprint
SEUXDR is registered in CYBERFORT as software with
digital elements. Under CRA Annex III [1], SIEM systems
fall underImportant Products with Digital Elements, Class I.
Clone Systems acts as the manufacturer (Art. 13). The con-
formity route is internal control supplemented by the EU
declaration of conformity once the technical documentation
is complete (Art. 32). Internal control under Art. 32 is the
manufacturer-internal route applicable here; products falling
under Annex III Class II or the critical-products list would
instead require third-party assessment. Within CYBERFORT
this is selected during scope assessment and locked in for
downstream gap analysis and reporting.
a) Pilot goals:The pilot does not aim to declare confor-
mity. It targets four CRA obligation families (secure-by-design
and secure-by-default, vulnerability handling, conformity ev-
idence, and Article 14 reporting readiness) and produces a
product-boundary dossier, a control-mapping matrix, a policy
uplift plan, a risk-treatment mapping, and a management
decision pack.
b) Resource footprint:Because the CRA touches the
whole lifecycle, an SME must also know what the prepared-
ness layer costs to run. Compute is dominated by the local
Ollamaphi4:14bSOC analyst, which runs on a single
workstation-class GPU host and is invoked once per correlated
alert rather than once per raw event (with rule-based fall-
back), so detection latency is bounded by Wazuh correlation,
not model inference; the five containerised scanners run on
demand in Step 3, not continuously. Storage is dominated
by the OpenSearch event store sized to the retention policy,
while the evidence index (software bill of materials, or SBOM,
plus configuration exports and audit-event samples) and the
compliance-chain graph (1,775 edges) are small structured
documents. Communication is modest: heartbeat and event
shipping over mTLS, short HTTP/REST scanner bursts, and a
one-shot Article 14 submission. The preparedness layer thus
adds governance metadata and on-demand scanning to an
existing SIEM rather than a new always-on workload.
IV. METHODOLOGY: A SIX-STEPCRA PREPAREDNESS
RECIPE ONCYBERFORT
This section operationalises CRA legal obligations into a
six-step engineering recipe executed on CYBERFORT: Scope
and Classify→Asset Registration→Produce Evidence→
Map to CRA→Gap and Actions→Audit Pack. Each step
produces an artefact that closes one link in the compliance
chain so that, by Step 6, every CRA obligation traces back
through a policy, a control, a risk, and a product asset; the
resulting chain is rendered by the platform’sCompliance
Chain / Mapview (Fig. 2, shown later in Step 4 once the
necessary entities exist). Each step is reproducible from a fresh
CYBERFORT install once the framework seed data is loaded.
The remainder of this section follows CYBERFORT’sCRA
Start Exampleentry-point on SEUXDR, showing for each step
what the operator does and what the platform produces.
A. Step 1: Scope and Classify
The first decision in the recipe is what counts as “the prod-
uct”. The scope-assessment workflow elicits the economic-
operator role (Manufacturer), CRA applicability (in scope),
Annex classification (Annex III, Class I, SIEM systems), and
conformity route (internal control supplemented by EU decla-
rationunder Art. 32). The platform seeds the CRA framework
with its 42 objectives, control library, and policy templates,
locks the classification in, and emits a scope report that
becomes the entry point for the technical-documentation file.

Watch-out.The most consequential call is the product
boundary: we scoped SEUXDR as the manager, AI Actions
component, and agents, butnotcustomer log sources, host
OS, or deployment infrastructure. Because every downstream
artefact inherits it, we signed it off with engineering, product,
and legal before leaving Step 1.
B. Step 2: Asset Registration
With the scope locked in, the product, its components,
and its sub-assets are created as records in CYBERFORT.
SEUXDR is registered as a top-level Software asset, with
identity, license, and SBOM fields captured up-front as a stable
anchor for downstream evidence. Sub-assets are then attached:
the Wazuh manager image, the OpenSearch backend, the agent
binaries, the AI Actions container, the playbook repository,
and the third-party libraries pulled in via the SBOM. Each
sub-asset inherits support period and conformity route from
the scope unless overridden.
Watch-outs.Sub-assets should be registered at the granu-
larity of the smallest item that can independently fail a CRA
obligation: the AI Actions container, for instance, has its own
support period and conformity-relevant evidence (model card,
playbook hash) distinct from the manager.
C. Step 3: Produce Evidence
Step 3 produces theEvidenceobjects on which the
rest of the recipe depends. TheWrappersintegration layer
runs five containerised scanners: Syft (SBOM generation in
CycloneDX), OSV Scanner (software-composition analysis
(SCA) via CVE lookup against the Syft SBOM), Semgrep
(static application security testing (SAST) and policy-as-code
over the Wazuh customisations, AI Actions code, and play-
books), OW ASP ZAP (dynamic application security testing
(DAST) against the manager web/API), and Nmap (network-
segmentation verification), with an on-demand SBOM Gener-
ator helper alongside. In parallel, artefacts that already exist
outside CYBERFORT (mTLS certificate-issuance procedure,
Wazuh ruleset and version pin, audit-log samples, change-
management log, AI playbooks and kill-switch test records,
prior penetration-test reports) are bulk-loaded into the same
Evidence index. Both sources share the same provenance
schema (tool, version, scan date, target hash, signed result,
owner), so the downstream mapping module does not distin-
guish between them.
Watch-outs.Evidence must be measured against the CRA
support period, not the calendar year: an SBOM from an
unmaintained release is stale regardless of its date.
D. Step 4: Map to CRA: Risks, Controls, Policies
The mapping module connects Annex I obligations to the
CYBERFORT control library across six themes; ENISA’s
CRA-to-standards mapping [3], NIST CSF 2.0 [5], and
IEC 62443 [4] are useful starting points for the control library.
The six themes, with their main SEUXDR components and the
gap the pilot closed for each, were:identity and access(JWT,
RBAC, and session/role controls; gap: a product-specific
Fig. 2: The compliance chain as rendered by the CYBERFORT platform
for the SEUXDR scope: 1,775 many-to-many connections across five colour-
coded entity types (Assets to Risks to Controls to Policies to Objectives),
with per-link counters on the side and an entity-filter strip across the top.
Each node is clickable for evidence drill-down.
access-control standard operating procedure (SOP) and admin
hardening);cryptography and secure communications(mTLS,
certificate pinning, TLS; gap: an approved encryption policy
and release-baseline settings);vulnerability management and
updates(self-updating agents, Wazuh detections, patch work-
flows; gap: a formalised Product Security Incident Response
Team (PSIRT) workflow, service-level agreement (SLA), re-
lease evidence, and SBOM routine);logging and detection
(audit logs, Wazuh/OpenSearch, real-time alerts; gap: defined
CRA reporting-evidence fields and a retention strategy);supply
chain and vendors(OS and Wazuh packages, the Ollama
model, Docker images, third-party libraries; gap: a supplier in-
ventory and an SCA/SBOM cadence); andsecure development
and testing(input validation, rate limiting, rule testing, CI/CD;
gap: a Secure Software Development Life Cycle (SSDLC)
checklist, security-test sign-off, and release gates). Each row of
this mapping is realised by linked records under a fixed identi-
fier scheme that carries no meaning beyond grouping: risks are
prefixedRSK-, controls carry a control-family prefix (IAM-
identity and access,AAT-AI and autonomous technologies,
CHM-change management,GOV-governance), and policies
POL-. ARiskrecord (e.g.RSK-102emergent properties
from AI / autonomous technologies, severity Critical, treat-
ment Reduce) captures the exposure. AControlrecord (e.g.
AAT-02.2AI & Autonomous Technologies Internal Controls,
StatusImplemented, linked to Annex I (2)(i)) captures the
safeguard. APolicyrecord closes the triangle, e.g. theRisk
Management PolicyPOL-30, created inApprovedstatus with
the Chief Information Security Officer (CISO) as owner and
an effective date set up-front, linked to the CRA framework
so it is auto-discovered from the objective checklist.
Once every Risk–Control–Policy triangle is in place, CY-
BERFORT’sCompliance Chain / Mapview (Fig. 2) renders
the resulting graph as a single navigable picture; for SEUXDR
it spans 1,775 connections across the five entity types, each
clickable for evidence drill-down.

E. Step 5: Gap and Actions
With the chain rendered, Step 5 asks what is missing.
The readiness module turns the mapping into a gap list with
owner, due date, and closure criterion. A CRAConformity
assessment is opened against the SEUXDR asset and the
operator walks the questionnaire item by item, attaching
the matching policy and evidence record so the compliance
chain is complete by close. Each Annex I objective is then
markedCompliant,Partially Compliant, orNot Assessed, and
Generate AI Suggestionsproduces recommendations for items
not yet fully compliant. Most gaps in the SEUXDR pilot
weredocumentationgaps (a control was implemented but the
policy was not approved, the evidence was not indexed, or
the SLA was not written), the dominant failure mode for
security products with strong engineering culture and weak
GRC discipline.
F . Step 6: Audit Pack
Once the corrective-action register has driven each open
gap to closure, Step 6 closes the recipe by exporting the
seven CRA-oriented reports detailed in Section V-C. The
audit pack is the deliverable that goes to management for the
conformity decision and is the input to the internal declaration
of conformity.
V. RESULTS: THREADS, SNAPSHOT,ANDAUDITPACK
We report the six-step methodology’s output bottom-up:
two end-to-end traceability threads make the compliance chain
concrete (§V-A); the aggregate pilot snapshot then summarises
30 risks, 65 controls, and 27 CRA objectives across the
SEUXDR scope (§V-B); the audit pack and an Article 14
reporting-readiness rehearsal close the loop (§V-C).
A. Worked Traceability Threads
The compliance chain is easier to grasp through one full
thread than through any aggregate table. Table II reproduces
two threads side by side, one conventional and one AI-
specific. Thread 1 follows the Manager API, the component
most exposed to operator interaction: the residual risk of
broken or weak authentication (RSK-18) is reduced by a
secure-authentication baseline (IAM-5) and mandatory multi-
factor authentication (MFA,IAM-6), documented by the
Password Policy (POL-1) and evidenced so as to satisfy
Annex I (2)(d). Thread 2 follows the AI Actions compo-
nent, whose autonomous remediation (RSK-102) pulls in ten
SCF AAT controls on top of the baseline change-management
and privileged-access controls, with operational rather than
configurational evidence: AI decision logs, human approval
records, a kill-switch test report, and a rollback playbook.
B. Pilot Snapshot: Coverage and Severity
The SEUXDR pilot snapshot, as exported from CYBER-
FORT, is as follows. SEUXDR is registered as a Software asset
of CRA criticality Annex III, Class I, with Clone Systems
as manufacturer. The pilot identified 30 risks (from 104
templates, spanning 8 of 12 categories), mapped 65 controls
TABLE II: Two worked traceability threads from the SEUXDR matrix: a
conventional IAM thread and an AI active-response thread
Layer Thread 1: IAM Thread 2: AI active response
Component Manager API AI Actions (LLM-driven active
response)
RiskRSK-18, broken/weak authenti-
cation (High)
RSK-102, emergent properties
from AI / autonomous tech.
(Critical)
ControlsIAM-5(secure-auth baseline),
IAM-6(mandatory MFA: dash-
board, API, admin)
AAT-01(AI governance),
AAT-02.1/02.2(AI risk
mapping & internal controls),
GOV-3(controls monitoring),
IAM-4(privileged-action
approval),CHM-1/2/3
(playbook change tracking)
PolicyPOL-1(Password Policy)POL-30(Risk Mgmt.),
POL-11(Change Mgmt.),
POL-21(Information Security)
CRA objec-
tive
Annex I (2)(d), unauthorised-
access protection
Ch. II Art. 13 (manufacturer
duties, internal processes); An-
nex I (2)(i)
Evidence Auth/RBAC config export; lo-
gin audit events; password/MFA
screenshots
AI decision logs; human ap-
proval records; kill-switch test
report; rollback playbook
(55 from the CYBERFORT Baseline of 132 controls plus 10
from the SCF v2025.1 AAT family), engaged 25 of 48 policies,
and addressed 27 of 42 CRA objectives (including Annex I
and vulnerability handling). Two patterns stand out. The AI
and autonomous-operations focus area carries the smallest risk
count (4 risks) yet ties application and API security for the
largest control set (14 controls), so the cost of safe autonomous
operation is paid in control overhead. The severity profile (12
critical, 14 high, 4 medium) skews high, the expected profile
for a security product registered as manufacturer, because the
product itself is part of the attack surface.
C. Audit Pack and Reporting Readiness
At the end of the pilot, CYBERFORT auto-generates seven
CRA-oriented artefacts from the compliance chain: six reports
that constitute the audit pack (the CRA assessment, scanning-
tool, risks, controls, and policy reports, and the Annex I objec-
tive checklist), plus the EU declaration of conformity, which
remains in progress pending legal review of the manufacturer-
internal control assertion under Art. 32.
The pilot success criteria, set up-front, were: traceabil-
ity across the full chain, approved policies, a validated
vulnerability-handling workflow, and a reporting-readiness re-
hearsal under simulated Art. 14 conditions. All four were met
for the in-scope SEUXDR boundary.
Article 14 dry-run:As the final readiness check we re-
hearsed an Art. 14 reporting flow against a fabricated actively-
exploited CVE, tracing it through the chain (CVE→SBOM
component→sub-asset→control→CRA objective) to
notification drafting and ENISA single-reporting-platform sub-
mission, well inside the 24-hour early-warning clock. The re-
hearsal exposed workflow, not technical, gaps (a single-owner
ENISA-portal account, a missing customer-communications
template, an unwritten legal sign-off path), all closed that week
and now in the SEUXDR runbook.

VI. DISCUSSION
A. Key Findings
Three findings recur. First,documentation gaps dominate
over implementation gaps: the controls usually exist, but
policies are unapproved, evidence is not indexed, and SLAs
are unwritten, so the GRC engineer’s priority is policy ap-
proval and evidence collation, not new controls. Second,AI
adds irreducible control overhead: once an LLM sits in the
active-response loop, the ten SCF AAT controls become non-
optional, and a kill-switch test, a rollback playbook, and an
explicit boundary on unattended model actions must all be
evidenced, or an auditor will probe the emergent-behaviour,
value-drift, and human-in-the-loop gaps that generic IAM and
change-management controls miss. Third,reporting readiness
is a workflow problem, not a technical one: the Article 14
24-hour and 72-hour clocks are unforgiving, and our dry-run
failures were missing portal credentials, an unclear escalation
owner, and no notification template, so a rehearsal before the
clock starts is mandatory.
Underlying all three isscope discipline: the Step 1 product
boundary drives every downstream artefact, so mid-pilot scope
drift was our most expensive failure mode, and locking the
boundary behind engineering, product, and legal sign-off is
cheap insurance. The internal declaration of conformity is
likewise best drafted once scope is signed off, since legal
review is sequential and rarely shortens.
B. Advantages
The qualitative gains over the team’s spreadsheet-and-free-
form-draft baseline are threefold. (i)A single source of
truth: the compliance chain links risks, controls, policies,
evidence, and CRA objectives in one navigable graph the
baseline lacked. (ii)One-click report export: the audit pack
and EU declaration-of-conformity draft are generated from
the chain, not reassembled by hand. (iii)The chain doubles
as an incident-triage tool: when a CVE drops, the on-call
engineer pivots from CVE through SBOM component, sub-
asset, controls, and CRA objective to the Art. 14 decision
in a few clicks. These are the conformity capabilities (§II) a
detection tool alone does not provide.
C. Limitations
The study captures what a small manufacturer team pro-
duces internally before any external review, a deliberately
manufacturer-side scope; formal conformity with a notified
body, external-auditor sign-off, customer-side validation, and
a real (not tabletop) Article 14 cycle are out of scope, and
effort and timing claims are self-reported. External validity is
bounded by the single-case design (one product, one manufac-
turer, one country): CYBERFORT’s mapping library reflects
its seed data, so other GRC tools yield different mappings, and
the AI control family is sensitive to model and playbook scope,
so substitutions shift the control set and residual-risk profile.
We thus expect the recipe (§IV) to transfer, but not the absolute
numbers (§V). Matching product controls to CRA objectives
demonstrates preparedness, not a guarantee of conformity;
only a notified-body route can establish the latter.
D. Future Work
Follow-up work extends the study along four axes: multi-
team, multi-product replication with instrumented time-on-
task; an external-auditor walkthrough of the audit pack against
an entry-level conformity-readiness bar; a structured customer
survey on the operator surface; and a live Article 14 re-
porting cycle, with retrospective timings, on the next vul-
nerability disclosed in the SEUXDR supply chain. We also
plan to formalise the Coordinated Vulnerability Disclosure
channel Annex I Part II obliges—disclosure channel, advisory
pipeline, researcher-acknowledgement policy, and customer-
communications boilerplate—reusing the ISO/IEC 29147 [12]
and ISO/IEC 30111 [13] templates, and to regenerate the
SBOM on every release rather than every audit, tracked against
the CRA support period.
VII. CONCLUSION
We documented a six-step, reproducible recipe for CRA
conformity preparation and applied it end-to-end to SEUXDR
on the open-source CYBERFORT platform. The find-
ings (§VI-A) condense into one practitioner message: for
engineering-led SMEs the binding constraint is the documenta-
tion, traceability, and reporting workflow rather than missing
controls, and an AI-augmented product adds an irreducible
control overhead once an LLM sits in the active-response
loop. The traceability matrix behind these claims is released
alongside the open-source code, and the platform itself is open
to any SME after free registration, so that the recipe can be
reproduced end-to-end without bespoke setup.
ACKNOWLEDGMENT
This work has received funding from the Digital Europe
Programme under Grant Agreement No. 101190281 (CYBER-
FORT).
REFERENCES
[1] European Parliament and Council of the European Union, “Regulation
(EU) 2024/2847 (Cyber Resilience Act),”Official Journal of the Euro-
pean Union, 2024. [Online]. Available: https://eur-lex.europa.eu/eli/reg/
2024/2847/oj/eng
[2] N. Kekatos, G. Koutidiset al., “CYBERFORT: A Multi-Framework
Compliance Platform for Preparing SMEs for the EU Cyber Resilience
Act,” inProc. IEEE Int. Conf. Cyber Security and Resilience (CSR),
2026.
[3] ENISA, “Cyber Resilience Act Requirements Standards Mapping,”
2024. [Online]. Available: https://www.enisa.europa.eu/publications/
cyber-resilience-act-requirements-standards-mapping
[4] IEC, “IEC 62443: industrial communication networks, IT security for
networks and systems,” 2018–2024.
[5] National Institute of Standards and Technology, “The NIST Cybersecu-
rity Framework (CSF) 2.0,” 2024. [Online]. Available: https://www.nist.
gov/cyberframework
[6] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y . Cao,
“ReAct: Synergizing Reasoning and Acting in Language Models,”Proc.
ICLR, 2023.
[7] A. Shostack,Threat Modeling: Designing for Security. Indianapolis, IN:
Wiley, 2014.

[8] C. Szedlak, H. Reinemann, and S. Hatzelmann, “Ensuring Cybersecurity
Compliance: Assessing SME Awareness and Preparedness for the Cyber
Resilience Act,”Proc. 5th Asia Pacific Conf. Industrial Engineering and
Operations Management, 2024, doi: 10.46254/AP05.20240160.
[9] OW ASP Foundation, “OW ASP Top 10:2025 — The ten most critical web
application security risks,” 2026. [Online]. Available: https://owasp.org/
Top10/2025/
[10] B. E. Strom, A. Applebaum, D. P. Miller, K. C. Nickels, A. G.
Pennington, and C. B. Thomas, “MITRE ATT&CK: Design and philos-
ophy,” The MITRE Corporation, Tech. Rep., 2020. [Online]. Available:
https://attack.mitre.org/
[11] Secure Controls Framework Council, “Secure Controls Framework
(SCF) v2025.1 — AI & Autonomous Technologies (AAT) family,” 2025.
[Online]. Available: https://securecontrolsframework.com/
[12] ISO/IEC, “ISO/IEC 29147:2018 — Information technology — Security
techniques — Vulnerability disclosure,” 2018.
[13] ISO/IEC, “ISO/IEC 30111:2019 — Information technology — Security
techniques — Vulnerability handling processes,” 2019.
