---
title: Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats
  and Controls in Regulated Financial Systems
url: https://arxiv.org/abs/2606.29142
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Krishna Mohan
- Guda Nagavenkata Srinivasa
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.29142
pages: 11
chars: 53528
fetched_at: '2026-11-08T13:36:33+00:00'
kb_version: 1
---

# Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems

1

Abstract Large language model agents are entering regulated financial systems, yet the security literature characterizing their
attack surface is almost entirely laboratory -based, and the practitioner guidance on regulated deployment is neither peer -
reviewed nor connected to a formal threat model. We bridge the two from production experience. We map six established
agentic threat categories namely prompt injection, identity and authorization, action auditability, tool abuse, data residency, and
boundary policy enforcement onto the specific control obligations imposed by the US and the EU financial regulation (ECOA
and Regulation B, the EU AI Act, GDPR Article 22, and FINRA's 2026 agent guidance), showing how legal accountability
amplifies each threat relative to an unregulated deployment. We then document four architectural patterns from a production
Know Your Customer deployment for a consumer credit product (A2A compliance choreography, grounded -RAG-for-audit,
case-ID propagation, and an inference-boundary redaction proxy) that moved a multi-day manual process to same-day automated
resolution for roughly four in five cases. Finally, we report three negative results, including two control failures surfaced  only by
internal audit and a population of legitimate applicants the automated pipeline cannot serve. Securing agents under regulatio n,
we conclude, is less about novel attack classes than about making auditability, least -privilege authorization, and boundary policy
enforcement real at production scale—requirements current agent frameworks leave to the deploying engineer.

Index Terms— LLM agents, agent security, regulated finance, Know Your Customer (KYC), Model Context Protocol, retrieval -augmented
generation, prompt injection, action auditability, least-privilege authorization, data residency, ECOA, EU AI Act, AI governance.

I. INTRODUCTION1
Large language model (LLM) agents are moving rapidly
from experimental assistants into deployed, autonomous
components of production software. Unlike a
conversational model that answers a question and returns
control to a human, an agent perceives an environment,
plans, invokes external tools, and takes consequential
actions with limited or no human intervention. This
transition is now reaching regulated financial systems
(consumer credit, payments, fraud detection, and account
servicing), where the actor initiating a transaction may now
be a non-human agent operating on a person's behalf.
The security research community has responded with a
substantial body of work characterizing the agentic attack
surface. Layered models decompose the agent stack into
foundation, memory, tool, coordination, and governance
tiers [1]; systematizations catalogue prompt -injection
attacks and defenses [2]; and dedicated analyses examine
the Model Context Protocol (MCP) tool ecosystem [3],
agent identity and delegated authority [4], and memory -
state manipulation [5]. Collectively this literature
establishes that the agentic surface is qualitatively different
from that of stateless LLMs: attacks emerge not only at the

1
Krishna Mohan Guda Nagavenkata Srinivasa  is with VectorTech
Consulting Inc, 7100 Lakeway Drive, Suite 200, Sunnyvale, CA, 94085,
USA (e-mail: krishnamohanguda@gmail.com).
prompt interface but through persistent state, delegated
authority, and long-horizon interaction [1].
Yet this literature shares a structural limitation: it is
overwhelmingly laboratory-based. The systematizations are
built from literature review and benchmark evaluation, and
several state explicitly that they did not deploy or
independently replicate in production [3]. In parallel, a
separate body of non -peer-reviewed practitioner material
(vendor playbooks, compliance -consultant guides, and
governance frameworks such as the NIST AI Risk
Management Framework and the EU AI Act) addresses
how to deploy LLM s ystems under regulatory regimes such
as SOC 2, GDPR, and HIPAA [6, 7]. No peer -reviewed
work bridges the two: nobody has systematized how the
academic threat models map onto the concrete, legally
mandated control obligations of regulated financial
deployment, nor reported which mitigations survive contact
with production at scale.
When we deployed MCP/RAG/A2A agents to automate
Know Your Customer (KYC) onboarding for a consumer
credit product, (We describe only generally applicable
architectural patterns and publicly mandated regulatory
obligations, and disclose no proprietary, confidential, or
customer-identifying information of any organization; the
views are the author's own.) the academic frameworks told
us how an agent could be attacked but not what we would
be legally obligated to prove after it acted. The taxonomies
assumed the operative question was whether an action was
authorized; in a regulated consumer -finance setting the
Agent Security Meets Regulatory Reality: A Practitioner
Systematization of Autonomous-Agent Threats and Controls
in Regulated Financial Systems
Krishna Mohan Guda Nagavenkata Srinivasa, Member, IEEE

binding question was whether we could reconstruct, from a
single case identifier, exactly which factors drove an
applicant's outcome, and whether every policy the agent
applied was the current, approved version. Nothing in the
laboratory literature anticipated that our most consequential
failures would be surfaced not by adversaries but by
internal audit: a stale policy in the retrieval store causing
systematic over -verification of customers who no longer
required it, and tool -call logs that existed but cou ld not be
tied back to the case they decided. The gap we encountered
was not a missing attack class; it was the absence of any
mapping from the threat models we had read to the control
obligations we were audited against. In this paper, we
specifically focused on bridging this gap.
. The main contribution of this paper is not another
taxonomy; instead, we offer an experience -grounded
systematization in which we (i) map established agentic
threat categories onto the specific control obligations
imposed by financial regulation; (ii) document a set of
architectural patterns applied in a production regulated -
finance KYC deployment operating under formal internal
audit; and (iii) report which patterns held under audit and
operational load, and which did not. We intend it to be
reproducible in argument and transferable to other regulated
domains.
The remainder of the paper is organized as follows.
Section II reviews the agentic -security literature and the
regulated deployment guidance and states the gap precisely.
Section III presents a threat model under regulatory
constraint. Section IV describes architectural patterns
observed in production. Section V reports negative results
and open problems. Section VI discusses generalizations
beyond finance, and Section VII discusses our conclusions.
II. BACKGROUND AND RELATED WORK
A. Agent Architectures: MCP, RAG, and A2A
Modern production agents are commonly assembled
from three interoperating layers. The Model Context
Protocol (MCP) standardizes how an agent discovers and
invokes external tools and data sources through a typed and
scoped interface [3]. Retrieval -augmented generation
(RAG) grounds model output in an external corpus,
retrieving relevant documents at inference time to constrain
the model to verified information [8]. Agent -to-agent
(A2A) orchestration coordinates multiple specialized agents
through structured message passing, enabling division of
labor across a workflow [9]. Though each layer expands
capability, they each expand the attack surface in a distinct
way simultaneously.

 --First,
The graphics will stay in the “second” column, but you
can drag them to the first column. Make the graphic wider
to push out any text that may try to fill in next to the
graphic.
B. Agentic-Security Taxonomies
    Recent systematizations organize the agentic attack
surface along structural lines. Layered attack -surface
models decompose the stack into foundation, cognitive,
memory, tool -execution, multi -agent-coordination,
ecosystem, and governance layers, augmented by a
temporal axis distinguishing instantaneous, session -
persistent, and cross -session threats [1]. Prompt -injection
scholarship distinguishes direct injection from indirect
injection, in which malicious instructions are embedded in
external content which the agent later consumes [2, 10].
MCP focused work catalogues tool poisoning, tool -
description manipulation, and “rug -pull” attacks in which a
tool's behavior changes after it is trusted [3]. Memory -
centric analyses show that persistent state introduces
control-flow hijacking that stateless threat models do not
capture [5]. Identity -focused work argues that
authentication, authorization, and delegated authority
constitute a distinct frontier for agentic systems [4].
Community efforts such as the OWASP Top 1 0 for LLM
Applications consolidate these threat classes into
practitioner-facing risk catalogues [11].
C. Deployment Guidance for Regulated AI
A separate body of guidance addresses operating LLM
systems under regulatory regimes. Governance
frameworks—the NIST AI Risk Management Framework
(AI RMF 1.0, 2023), ISO/IEC 42001:2023, and the EU AI
Act's high -risk-system obligations define what
organizations must document and control [6]. In US
banking, the primary supervisory standard for model
governance is the interagency model risk management
guidance, most recently revised as SR 26 -2 (Federal
Reserve, OCC, and FDIC, April 17, 2026), which
supersedes SR 11 -7 (2011) and SR 21 -8 (2021) [12].
Practitioner guides translate these frameworks into
architectural prescriptions: VPC isolation, immutable audit
logging, data -residency controls, role -based access, and
gateway-layer policy enforcement [7].  These prescriptions
are organized around compliance requirements rather than
around the failure modes of agent ic architectures. They
enumerate what a compliant system must contain but do not
derive those requirements from a model of how an
autonomous, multi-agent system can be attacked or can fail.
As a result, they remain disconnected from the agentic
threat taxonomies of Section II -B, which characterize those
failure modes but do not map them to regulatory
obligations.
D. The Gap
 This disconnect extends to the regulatory frameworks
themselves. The academic taxonomies are rigorous but
abstract from the binding constraints (legal accountability,
audit obligation, data -residency law) that dominate a
regulated deployment. The practitioner guidance is concrete
but not grounded in a formal threat model. A concrete
marker of this gap emerged in April 2026: the revised

3

interagency model risk management guidance (SR 26 -2)
explicitly excludes generative AI and agentic AI models
from its scope, stating that they “are novel and rapidly
evolving” and deferring their governance to general
organizational risk management practices [12]. The primary
US bank supervisory framework for model governance
does not reach the autonomous agents now entering
consumer-facing financial systems.
Two recent papers narrow but do not close this gap.
Rashie and Rashi [13] encode financial regulatory
obligations (SEC Rule 15c3 -5, FINRA Rule 3110, OCC
Bulletin 2011 -12) as formal proof obligations for agentic
systems using Lean 4 theorem proving, but do not perform
adversarial threat -model analysis, leaving the question of
how attacks exploit the gap between architecture and
obligation unaddressed. Maiti et al., [14] performs exactly
the bridging operation for healthcare, mapping six threat
domains to specific HIPAA Security Rule provisions in a
nine-agent production deployment but does not address the
distinct regulatory obligations of financial services. Threat -
model frameworks for enterprise agents [15] and multi -
agent security taxonomies [16] omit regulatory mapping
entirely, and execution -grounded financial safety
benchmarks such as FinVault [17] describe compliance
constraints generically rather than grounding them in
named statutory obligations. No prior work provides a
threat-model-grounded security analysis that is
simultaneously (a) rooted in adversarially validated attack
taxonomies for LLM agents, (b) mapped to the specific
legally mandated control obligations of regulated financial
deployment, and (c) empirically validated in a production
financial system. This paper addresses that gap.
III. THREAT MODEL UNDER REGULATORY
CONSTRAINTS
 This section takes each established agentic threat
category and identifies its regulatory amplification: the way
in which legal accountability, audit obligation, or data -
protection law changes the severity, priority, or required
mitigation of the threat relative to an unregulated
deployment. The threat categories themselves are drawn
from the prior literature [1, 2, 3, 4, 5]; the amplification
analysis, and the production observations that ground it, are
the contribution. Fig. 1 summarizes the full mapping
developed in this section.
A. Prompt Injection Under Accountability
Prompt injection is the canonical agentic threat: an
attacker supplies instructions that the model treats as
authoritative, either directly through the user interface or
indirectly through external content the agent later consumes
[2, 10]. The indirect variant is more dangerous in an
automated compliance pipeline, because such pipelines
exist precisely to process untrusted external input at scale.
In this deployment, raw documents never reached the

Fig. 1.  Mapping from established agentic threat categories (left) through their regulatory amplification (center) to the legally mand ated control obligations of
regulated finance (right). Horizontal links pair each threat with its amplification; obligations C1 (auditability) and C2 (le ast-privilege authorization) are each
induced by multiple threats.

model—a structured -extraction stage passed only the
required fields, redacted of personally identifiable
information (See Section III.E) —so the indirect -injection
surface is narrowed but not closed: a crafted value within an
extracted field can still reach the model. This surviving
surface is the threat's bounded residual, the portion of an
attack surface that a mitigation reduces but does not
eliminate, and regulatory amplification is what makes even
this bounded residual consequential. An injected value t hat
alters the KYC determination does not merely cause an
unauthorized action; it produces an onboarding or adverse -
action decision whose actual basis diverges from the factors
the institution believes it applied. Under ECOA and
Regulation B, 15 U.S.C. §1691(d)(2) –(3) and 12 C.F.R.
§1002.9(b)(2) require that adverse -action reasons "relate to
and accurately describe the factors actually considered or
scored by a creditor" [18]. An injection that silently shifts
the decisioning path therefore creates a per -applicant
ECOA accuracy violation —the stated reason no longer
matches the real one —independent of any downstream
harm. In an unregulated chatbot, a successful injection is a
security incident that needs to be contained; in this setting it
is a compliance breach that the institution must be able to
detect and remediate after the fact, not merely prevent,
because the adverse -action notice has already been issued
on an inaccurate basis. This shifts the required defensive
posture from prevention alone to preventi on plus per -
decision attributability, the same requirement that motivates
the audit patterns of Section IV.
B. Identity and Authorization for Non-Human Actors
In unregulated deployments, agent identity and
authorization are primary security concerns: an attacker
who can impersonate an agent or escalate its permissions
can take unauthorized actions. The research community
addresses this through authentication protocols, capability -
bounded tool invocation, and delegated -authority
frameworks [4, 15]. The regulatory amplification in
consumer finance operates on two distinct axes namely
provisioning and attribution, each of which the academic
frameworks do not address.
The first axis is identity provisioning. In a regulated
consumer-finance deployment, every actor that touches
customer financial data must be provisioned in the
institution's identity and access management (IAM) system;
this is the assumption embedded in GLBA (Gramm –Leach–
Bliley Act) Safeguards Rule vendor -management controls
and in the access -review evidence that SOC 2 audits
demand. Agents do not fit this model. They require
machine credentials (service accounts or OAuth client
identifiers), but productio n IAM tooling had no workflow
for scoping those credentials to the bounded capability set
of a particular agent's intended function. The operational
default became production -level service accounts whose
permissions far exceeded what any single agent task
required. The regulatory consequence was direct and audit -
visible: access reviews found service -account grants for
which no role justification existed, because the role -based
model assumed a human employee with defined job duties,
not an autonomous agent w ith a bounded and time -limited
task. Over-privilege in that context is not merely a security
risk; it is a control failure that produces adverse audit
findings independent of whether any attack has occurred.
The second axis is decision attribution. Academic
literature treats agent identity as an authorization boundary
problem; in a production regulated -finance environment it
becomes an attribution problem with statutory
consequences. ECOA adverse -action requirements (15
U.S.C. §1691(d)(2)(3); 12 C.F.R. §1002.9(b)(2)) assume a
traceable decision -maker whose factors can be specifically
disclosed to the consumer [18]. When an orchestrating
agent delegates retrieval to a sub -agent whose output
influences a downstre am credit outcome, the decision -
maker in the audit trail becomes ambiguous across agent
boundaries, and that ambiguity is itself a regulatory
exposure. The consumer is owed a specific principal reason
grounded in the factors considered; a pipeline that returns a
score without attributing that score to an identifiable,
bounded decision process cannot satisfy this statutory
obligation regardless of the score's accuracy.
On the EU side, AI Act Article 14(1) translates these
concerns into a design obligation: high -risk AI systems
must be built so that natural persons can effectively oversee
them while in use [19]. Article 14(3) scales the obligation
with the system's level of autonomy: a more autonomous
agent triggers proportionately stronger oversight
requirements, implementable by the provider before market
placement or by the deployer after receipt. Article 14(4)
further requires that designated overseers hold actual
authority to halt the system in any situation. An agent
operating under a non -human identity with no human
principle empowered to stop it fails Article 14
independently of any adversarial action, making the identity
and authorization architecture a compliance artifact as well
as security control.
C. Action Auditability as a Legal Obligation
In unregulated deployments, audit logging is an
operational concern: logs support debugging, anomaly
detection, and incident response. The security literature
treats auditability as a defense -in-depth property, useful for
forensics after a compromise but not itself a threat category
[1, 15]. In regulated consumer finance, this framing inverts.
Action auditability is not a monitoring best practice; it is a
statutory obligation whose violation is independently
actionable regardless of whether any security eve nt has
occurred. This is the sharpest point of divergence between
laboratory threat models and regulated production.
The first axis of amplification is the legal -evidence
reframing of what a log must be. ECOA (15 U.S.C.
§1691(d)(2)(3)) and Regulation B (12 C.F.R.
§1002.9(a)(2)(i), §1002.9(b)(2)) require that any adverse
action notice specifically state the principal reason or
reasons for the action and accurately describe the factors

5

considered or scored by the creditor. CFPB Circular 2023 -
03 (September 19, 2023) confirmed that creditors using AI
or complex credit models may not substitute the sample -
form checklist of reasons unless those reasons specifically
and accurately reflect the actual factors relied upon [18].
FCRA adds parallel disclosure obligations when a credit
score from a consumer reporting agency contributes to the
outcome. The aggregate effect is that the audit trail for any
agent action touching a credit outcome must be  capable of
reconstructing the principal reasons in a consumer -
disclosable form, a requirement qualitatively different from
operational telemetry. Most agent frameworks produce logs
adequate for debugging; in a production regulated -finance
deployment, none natively produced a per -decision
evidence record that could satisfy an adverse -action
disclosure obligation without additional reconstruction
infrastructure built on top.
The second axis is the structural challenge that chained -
agent architectures posed to that reconstruction. In a single -
model system, the decision is a single inference call whose
inputs (prompt, context, parameters) can be captured
atomically. In an MCP/RAG/A2A pipeline, the decision is
distributed: a retrieval agent fetches documents, a reasoning
agent synthesizes them, and an orchestrator aggregates the
result into an outcome. The audit question is not merely
“what did the system output?” but “which retri eved
documents contributed which factors to which outcome,
and in what proportion?” Answering that question in a form
that satisfies the statutory standards required instrumenting
the inter-agent message boundaries, not the model calls, as
the primary unit of audit evidence. This is a non -obvious
architectural implication that does not appear in any of the
surveyed laboratory threat models, which treat the agent as
a unit rather than a pipeline of attributable sub-decisions.
EU AI Act Article 12(1) codifies this obligation on the
provider side: high -risk AI systems “shall technically allow
for the automatic recording of events (logs) over the
lifetime of the system” [19]. Article 12(2) further specifies
the purposes those logs must serve: traceability appropriate
to the system's intended purpose; identification of risk
situations under Article 79(1); post -market monitoring
under Article 72; and deployer operational monitoring
under Article 26(5). Article 26(6) separately requir es
deployers to retain automatically generated logs for at least
six months. The combined effect of Articles 12 and 26 is
that auditability is a design requirement binding on the
provider and a retention requirement binding on the
deployer, neither of which is satisfiable by general -purpose
observability tooling that was not designed with statutory
evidence reconstruction in mind.
D. Tool Abuse and Least Privilege Under Audit
The tool -execution layer is where agentic systems take
consequential action, and the security literature accordingly
treats tool abuse (privilege escalation, unauthorized
invocation, capability misuse) as a primary threat to be
contained through least -privilege bounding [1, 3]. In an
unregulated deployment, least -privilege is a hardening
recommendation: it reduces the blast radius of a
compromise. Regulation converts it into an evidentiary
obligation.
In the KYC pipeline, the orchestrator invoked MCP tools
for bureau retrieval, document verification, policy lookup,
and ACH checks. As described in Section III.B, these tools
were initially provisioned with broad service -account
permissions because the IAM model had no construct for
binding a credential to a single agent's task scope. The
audit-relevant finding was not that any tool had been
abused, but that the agent could invoke capabilities beyond
what an individual KYC case required, and that this laten t
over-privilege had no role justification in the access review.
The distinction is the amplification: in a regulated setting it
is not sufficient to bound and document what the agent did
and log it; one must be able to demonstrate to an auditor
that the agent could not have exceeded its mandate. EU AI
Act Article 26(1) codifies the deployer's side of this
obligation, requiring “appropriate technical and
organizational measures to ensure they use such systems in
accordance with the instructions for use,” an d Article 26(2)
requires that human oversight be assigned to persons with
“the necessary competence, training and authority” [19]. An
agent holding access to tools beyond those its instructions
for use contemplate is therefore in breach of the deployer
obligation before any attack occurs: least-privilege becomes
a precondition of compliant operation, not a plausible
defense-in-depth feature.
E. Data Residency and Sovereignty Constraints
Data residency is largely absent from the agentic -security
taxonomies, which treat the model as a fixed computational
resource rather than as a network endpoint whose physical
location carries legal consequence. In a regulated
deployment, where the data is processed is in itself a
controlled property. Even within a single jurisdiction, the
agent architecture introduced data -egress points that the
rules engine it replaced did not have: customer financial
data now transited through a RAG retrieval store and a
model inference endpoint, each a point at which regulated
data could cross the boundary of the environment
authorized to handle it. Establishing where customer data
was processed at each hop and being able to prove that it
stayed within the permitted boundary became a
precondition for deployment rather than an operational
afterthought.
The amplification is sharpest at the inference boundary,
because this model endpoint is the hardest hop to constrain:
it is frequently managed by a third -party service, often in a
different jurisdiction, and it consumes whatever context the
agent sends it. The pattern we adopted to bound this
exposure was to never send raw customer documents to the
model at all. Documents were processed through a
structured-extraction stage that pulled only the specific
fields the KYC determination required, and those field s
passed through a redaction proxy that removed or tokenized

personally identifiable information before any data reached
the inference endpoint. The model reasoned over redacted,
structured inputs; the mapping from tokens back to
identities never left the controlled environment. This kept
the inference hop free of resident PII, narrowing the
residency obligation to extraction and proxy components,
which were sited deliberately within the permitted
boundary.
The regulatory grounding makes the cost of getting this
wrong concrete. The CJEU's SCHUFA judgment (Case C -
634/21, ECLI:EU:C:2023:957) established that GDPR
Article 22(1) applies to AI -based credit scoring when a
third party “draws strongly” on the resulting value to
establish or terminate a contractual relationship [20],
bringing the entire processing pipeline including any cross -
border transfer to non -EU inference infrastructure within
the GDPR framework. A pipeline that routed an EU -
resident's unredacted  financial data to a non -EEA model
endpoint without a Chapter V transfer safeguard would
violate the transfer rules, and if the output drove a credit
denial, it meant
that Article 22 is violated as well. Under EU AI Act
Annex III, point 5(b), creditworthiness evaluation systems
are classified as high-risk (with a carve out enabled only for
pure fraud detection), so these residency obligations are
further amplified by the full suite of Annex III provider and
deployer duties [19]. The redaction -proxy pattern is, in
effect, a residency control: by ensuring that what crosses
the hardest -to-constrain boundary is no longer personal
data, it reduces the surface over which these  obligations
bind.
F. Policy Enforcement at the Request Boundary
Cloud security matured around a principle that agentic
architectures quietly dismantle: policy is enforced at the
boundary. In a network -security posture, every
consequential request traverses a control point (a gateway
or proxy) where it is inspected, authorized, and logged
before it reaches the resource it targets, and the workload
cannot bypass that point. Advancements in the cloud
security discipline in the last decade are predominantly
aimed at making the boundary comprehensive and
unforgeable.
Agent architectures dissolve this boundary. The
consequential action is no longer an outbound request that
crosses a gateway; it is a tool call emitted mid -reasoning,
internal to the agent's execution, with no natural choke
point between the model's decision and the tool's effect.
Reconstructing a boundary therefore required choosing one
deliberately. We treated the MCP tool -invocation layer as
the new policy enforcement point: the single place where a
request could be inspected, authorized against the agen t's
mandate, and logged with the originating case identifier
(Section IV-C). The regulatory amplification is that this one
boundary must now satisfy three regimes simultaneously.
EU AI Act Article 14(1) –(3) requires that high-risk systems
be designed so humans can effectively oversee them, with
oversight proportionate to autonomy [19], an obligation that
presupposes an interceptable enforcement point. FINRA's
2026 Annual Regulatory Oversight Report, the first to treat
AI agents as a distinct supervisory cat egory, identifies
“implementing guardrails to constrain or restrict AI agent
behaviors, actions, or decisions” as a required supervisory
consideration and holds that “firms remain responsible for
recommendations and decisions influenced by GenAI”
regardless of autonomy [21]. And the ECOA audit
obligations of Section III.C require that whatever crosses
the boundary be logged in a form that can later reconstruct
the decision. The tool -invocation boundary is thus
simultaneously a security control, an EU AI Act  oversight
surface, and a FINRA -mandated guardrail: three regimes
converging on a single architectural seam that the agent
frameworks do not expose by default.
IV. ARCHITECTURAL PATTERNS OBSERVED IN PRODUCTION
This section describes four architectural patterns applied
in a production deployment of MCP/RAG/A2A agents
supporting Know Your Customer (KYC) compliance for a
credit product in US regulated consumer finance. Each
pattern is tied to a threat -model category from Section III
and reported at the architectural level. The baseline against
which outcomes are measured was a mixed manual -and-
rules-based process handling on the order of 100 cases per
day at a median resolution time of roughly two to three
days per case. Fig. 2 shows how these four patterns
compose into the end -to-end KYC pipeline, from customer -
document intake through a pass/refer/reject outcome; each
component is annotated with the pattern that governs it.
A. A2A Compliance Choreography
Problem (Section III -C: Action Auditability). The pre -
agent KYC process combined automated rules with a
human review queue. Because human reviewers operated
across multiple systems and produced unstructured notes,
the per -case audit trail was inconsistent: some cases could
reconstruct the factors driving a refer or reject
recommendation; others could not. This created a recurring
adverse-action notice compliance risk: ECOA requires that
stated reasons accurately describe the factors considered,
and an unstr uctured human review record does not satisfy
that standard reliably at volume.
Mechanism. An orchestrating agent was introduced to
coordinate a deterministic sequence of sub -agent actions:
identity document verification, bureau data retrieval, ACH
policy applicability check, and KYC step -up determination.
Each sub -agent produced a structured output that fed the
next stage, with the orchestrator responsible for assembling
the final pass/refer/reject recommendation and its
supporting reasons. Human reviewers remained in the loop
for referred cases; the agent handled straight -through cases
end-to-end. Physical adverse -action letters were dispatched
within one week for all non-approved outcomes.
Observed outcome. Roughly four in five cases resolved
same-day through the automated path; the remaining one in

7

five entered a human review queue and completed within
one week. Against the pre -agent baseline of roughly two to
three days median for all cases, same -day resolution for the
majority of volume represents a quantitative shift in the
timeliness of credit decisions. The system scaled
horizontally without adding review staff; throughput ceiling
was determined by KYC API rate limits and cost, not
headcount. The audit trail produced by the orchestrator's
structured output consistently satisfied adverse -action
documentation requirements in subsequent internal reviews.
B. Grounded RAG for Audit
Problem (Section III -C: Action Auditability; Section III -
D: Tool Abuse). The KYC and ACH policy documents
governing which verification steps applied to a given
customer were maintained by a compliance team and
updated periodically. Without a controlled retrieval
mechanism, the orchestrating agent had no reliable way to
determine whether a policy provision was current,
superseded, or inapplicable to the specific product.
Applying a superseded policy provision (even in the
direction of over -verification) cons titutes a control failure
under SOC 2 access and change -management requirements,
because the agent is acting on information that does not
accurately reflect the institution's current compliance
posture.
Mechanism. Policy documents were ingested into a
retrieval store via an automated compliance team feed, but
with a human sign-off gate introduced before any document
version entered the production index. At retrieval time, a
policy-version check confirmed that the document being
used matched the current approved version rather than a
prior ingestion. Each tool call that retrieved a policy
document recorded the document identifier, version hash,
and retrieval timestamp as part of the case audit record,
making the policy basis for each step -up determination
explicitly traceable.
Observed outcome. The pattern was held under normal
operating conditions and produced an audit trail in which
every KYC step -up decision was grounded in a specific,
versioned, human -approved policy document. The human
sign-off gate introduced a processing lag when policies
changed—compliance updates could not take effect in the
agent until a reviewer approved the new document
version—but this lag was accepted as a deliberate control
rather than a defect. The pattern did not prevent the failure
described in Section V -A; it was the remediation that
followed that failure.
C. Case-ID Propagation Through MCP Tool Calls
Problem (Section III -C: Action Auditability; Section III -
B: Identity and Authorization). As described in Section III -
C, MCP tool calls in the initial deployment produced logs
that were adequate for operational debugging but were not

Fig. 2. Deployment architecture of the KYC onboarding pipeline. Customer documents are reduced to extracted fields and stripped of PI I by a redaction proxy
(Pattern D) before any data crosses the controlled boundary to the third -party inference endpoint. An orchestrating agent (Pattern A) coordinates four sub -agents
through an MCP tool layer that serves as the policy-enforcement point, propagating a case identifier on every call and logging it as the audit join key (Patterns C,
F). Policy retrieval is grounded in a versioned, human-approved RAG store (Pattern B). Referred cases and out-of-schema edge cases route to human review.

correlated to the case identifier that anchored the KYC
decision in the institution's system of record. An adverse -
action audit that started from a case ID could not reliably
traverse back through the MCP tool call logs to reconstruct
which document retrievals and policy checks had driven the
outcome for that specific applicant. The logs existed; the
linkage did not.
Mechanism. A case -ID propagation layer was added to
the MCP tool invocation path, requiring every tool call to
carry the originating case identifier as a mandatory header.
Tool responses were logged with the case ID attached,
creating a per -case chain of tool call records that could be
traversed forward from case open to recommendation and
backward from an adverse action to the specific policy
documents retrieved and checks performed. The case ID
became the primary audit join key across the orchestrator
log, the MCP tool call log, and the adverse-action record.
Observed outcome. Following the remediation, internal
audit was able to reconstruct the full tool call chain for any
case from the case ID alone. The pattern satisfied the
ECOA adverse -action audit requirement that the factors
considered be traceable and accurately described. The
implementation required changes to the MCP tool interface
contract—every tool had to accept and propagate the case
ID—which meant that tools developed without this
constraint needed to be updated before they could be used
in a compliant pipeline. This retrofitting cost is noted in
Section V-B.
D. Redaction Proxy at the Inference Layer
Problem (Section III -A: Prompt Injection; Section III -E:
Data Residency). Two distinct threats converge on the
model inference endpoint: it is the point at which untrusted
document content could carry an injected instruction
(Section III -A), and it is the hardest data -egress hop to
constrain, frequently managed by a third -party service in a
different jurisdiction (Section III -E). Sending raw customer
documents to the model would simultaneously expose the
widest injection surface and place resident personally
identifiable information (PII) on the least -controllable
boundary.
Mechanism. Raw documents were never sent to the
model. A structured -extraction stage pulled only the
specific fields the KYC determination required, and those
fields passed through a redaction proxy that removed or
tokenized PII before any data reached the inference
endpoint. The model reasoned over redacted, structured
inputs; the token -to-identity mapping was held within the
controlled environment and never transmitted to the model.
The proxy and extraction components were sited
deliberately within the permitted data -residency boundary,
so that the only hop reaching third -party inference
infrastructure carried no resident PII and no free -form
document text.
Observed outcome. The pattern bounded both threats at a
single architectural seam. The injection surface was
narrowed from arbitrary document bodies to the constrained
set of extracted field values (a residual we do not claim was
eliminated; see Section III -A). The residency obligation
was narrowed to the extraction and proxy components,
removing the third -party inference endpoint from the scope
of resident -PII handling. The cost was a loss of model
context: because the model saw only extracted fields rathe r
than full documents, edge cases requiring information
outside the predefined extraction schema could not be
adjudicated by the agent and were routed to human review,
part of the roughly one -in-five referral volume reported in
Section IV-A.
V. NEGATIVE RESULTS AND OPEN PROBLEMS
Honest reporting of what did not work is among the most
valuable contributions a practitioner systematization can
make, because it is precisely what laboratory studies cannot
observe. This section records three results from the
deployment described in Section IV: a control failure
caught by internal audit, an architectural gap whose
remediation carried an ongoing cost, and a fundamental
design limit that no mitigation resolved.
A. Stale Policy in the RAG Store Caused Systematic
Over Verification
The most consequential failure in the deployment was
not a security attack but a policy synchronization gap. The
compliance team updated the KYC policy to remove the
step-up verification requirement for applicants above a
specified credit score threshold. The automated compliance
feed delivered the updated document, but the human sign -
off gate described in Section IV -B had not yet approved the
new version for production ingestion. During the window
between the policy update and the gate approval, the agent
continued retrieving the prior policy version and applying
step-up KYC to customers who no longer required it under
current policy.
The failure was identified by internal audit, not by the
agent system or its operational monitoring. The audit
finding characterized it as a control gap: the agent was
acting on a superseded policy provision, producing
outcomes that did not accurately reflect the institution's
current compliance posture. The regulatory exposure was in
the direction of over -verification rather than under -
verification—affected customers were subjected to
additional friction that the updated policy did not require —
which raised a potential Unfair, Deceptive, or Abusive Acts
or Practices (UDAAP) concern independent of any security
incident.
The lesson is generalizable: a human sign -off gate
protects against ingesting bad content but does not protect

9

against the window before the gate closes. In a regulated
deployment, that window is a compliance gap, not merely
an operational lag. No agent framework currently provides
a native mechanism for policy-version synchronization with
a compliance document lifecycle; this remains an open
problem.
B. MCP Tool Interfaces Were Not Designed for Audit
The case-ID propagation layer described in Section IV -C
resolved the audit trail gap, but its implementation revealed
a structural problem in how MCP tools are specified and
developed. Tools built without audit requirements in scope
do not carry case identifiers, session context, or any
provenance information in their call signatures. Adding the
case-ID constraint to the production pipeline required
retrofitting every existing tool to accept and propagate the
identifier, a non -trivial change to the interfac e contract that
forced re -testing and re -validation of each tool before it
could be used in a compliant workflow.
The broader implication is that auditability in a regulated
MCP deployment is not a logging concern that can be
addressed at the infrastructure layer; it is an interface design
constraint that must be established before tools are built.
The academic literature on MCP security does not address
this: the systematizations surveyed in Section II treat tool
calls as atomic units to be authenticated and authorized,
without considering the provenance and traceability
requirements that regulated deployments impose on the tool
call record. Organizations adopting MCP in regulated
contexts will encounter this gap at the integration stage, not
the design stage, which is the worst time to discover it.
C. Roughly one in nine applicants could not be served by
the automated pipeline
The deployment assumed that applicants had at least two
active contact channels (a mobile number and an email
address) because two -factor authentication was effectively
mandatory for the consumer credit product. Roughly one in
nine applicants presented with only one active channel,
typically because they had lost access to or could not recall
a previously registered email address. These applicants
could not complete the automated KYC pipeline regardless
of their creditworthiness or identity verification status.
The pattern of accommodating single -channel applicants
was evaluated and abandoned. The security posture
required for a consumer credit product did not permit
single-channel 2FA, and the operational cost of building a
separate exception path for lost -credential recovery
exceeded what the product economics supported. The result
is a real population of legitimate applicants, roughly one in
nine, for whom the automated system provides no path to
approval. This is not a failure of the agent architecture; it is
a design limit that the architecture cannot resolve and that
the academic threat models do not surface, because
laboratory evaluations do not model the population of users
who cannot satisfy authentication preconditions.
The open problem this exposes is the absence of a
regulatory framework for what an institution owes
applicants who are excluded by the authentication
requirements of an automated system. ECOA prohibits
discrimination on specified bases; it does not address
systemic exclusion by technical precondition. Whether a
dropout rate of roughly one in nine attributable to 2FA
TABLE I
ARCHITECTURAL PATTERNS OBSERVED IN PRODUCTION, EACH MAPPED TO THE THREAT IT ADDRESSES (SECTION III), THE CONTROL OBLIGATION IT SATISFIES (FIG.
1), ITS MECHANISM, AND ITS OBSERVED OUTCOME. PATTERN F (BOUNDARY POLICY ENFORCEMENT) IS REALIZED BY THE MCP TOOL LAYER THAT PATTERNS C
AND D OPERATE THROUGH AND IS THEREFORE NOT LISTED AS A SEPARATE ROW.
    Pattern THREAT (§III) Obligation Mechanism Observed Outcome
A. A2A
compliance
choreography
III-C auditability C1 Orchestrator sequences
four sub-agents; each emits
structured output
assembled into
pass/refer/reject with
reasons.
≈4 in 5 same-day
automated; consistent
adverse-action audit
trail.

B. Grounded-
RAG-for-audit
III-C auditability;
III-D tool abuse
C1 Versioned policy store
with human sign-off gate;
version hash + timestamp
logged per retrieval.
Every step-up
grounded in a
specific approved
policy version; sign-
off lag accepted as
control.

C. Case-ID
propagation
III-C auditability;
III-B identity
C1 Mandatory case-ID header
on every MCP tool call;
responses logged with
case-ID as join key.
Full tool-call chain
reconstructable from
case-ID; tool-contract
retrofit required (§V-
B).

D. Redaction
proxy
III-A injection; III-E
residency
C4 Only extracted fields sent
to model; PII
tokenized/stripped before
the inference boundary.
Injection surface
narrowed; no resident
PII on third-party
endpoint; some edge
cases to human
review.
D. Redaction proxy

channel requirements constitutes a disparate impact concern
under the fair lending framework is a question that neither
the security literature nor current regulatory guidance has
resolved.
VI. GENERALIZING BEYOND FINANCE
The control obligations that dominate regulated finance
(auditability of automated decisions, data residency, least -
privilege authorization, and explainability for high -stakes
outcomes) are not unique to finance. They recur, with
sector-specific variation, across healthcare (HIPAA),
critical infrastructure, and the EU AI Act's high -risk
categories [6, 7]. The mapping developed in Section III and
the patterns of Section IV are therefore expected to transfer:
the threat categories are domain -independent, whil e the
regulatory amplification and the acceptable -cost frontier
shift by sector. We conjecture that auditability and least -
privilege tool authorization are the two controls whose
production realization is hardest and most generalizable,
since both require mechanisms (immutable per -action
evidence trails and enforced capability bounds) that the
base agent frameworks do not provide natively [1, 3]. A
systematic cross -domain validation of this conjecture is a
focus of our future work.
VII. CONCLUSIONS
Agentic AI is entering regulated financial systems faster
than the security literature has connected its threat models
to the binding obligations of that setting. We have argued
that the gap between laboratory taxonomy and regulated
production is itself the problem worth addressing and have
offered an experience -grounded bridge: a mapping from
established agentic threats to regulatory control obligations,
a set of architectural patterns observed in a production
regulated-finance deployment, and an honest ac count of
their limits. The central lesson is that securing agents under
regulation is less about novel attack classes than about
making auditability, least -privilege authorization, and
boundary policy enforcement real at production scale:
requirements that the current agent frameworks leave to the
deploying engineer. We hope this bridge invites further
peer-reviewed, deployment -grounded work at the
intersection of agent security and regulatory practice.
VIII. DISCLOSURE
We describe only generally applicable architectural
patterns and publicly mandated regulatory obligations, and
disclose no proprietary, confidential, or customer -
identifying information of any organization; the views are
the author's own.
REFERENCES
[1] K. Chu, “A Systematic Survey of Security Threats and Defenses in
LLM-Based AI Agents: A Layered Attack Surface Framework,”
arXiv:2604.23338, Apr. 2026
[2] P. Wang, X. Li, C. Xiang, J. Zhang, Y. Li, L. Zhang, X. Wang, and
Y. Tian, “The Landscape of Prompt Injection Threats in LLM
Agents: From Taxonomy to Analysis,” arXiv:2602.10453, Feb. 2026.
[3] S. Gaire, S. Gyawali, S. Mishra, S. Niroula, D. Thakur, and U.
Yadav, “Systematization of Knowledge: Security and Safety in the
Model Context Protocol Ecosystem,” arXiv:2512.08290, Dec. 2025.
[4] T. South et al., “Identity Management for Agentic AI: The New
Frontier of Authorization, Authentication, and Security for an AI
Agent World,” OpenID Foundation Whitepaper, arXiv:2510.25819,
Oct. 2025.
[5] Z. Xu, X. Zhu, Y. Yao, M. Xue, and Y. Song, “From Storage to
Steering: Memory Control Flow Attacks on LLM Agents,”
arXiv:2603.15125, Mar. 2026.
[6] E. Tabassi, “Artificial Intelligence Risk Management Framework (AI
RMF 1.0),” NIST AI 100 -1, National Institute of Standards and
Technology, Gaithersburg, MD, Jan. 2023,
doi:10.6028/NIST.AI.100-1.
[7] International Organization for Standardization / International
Electrotechnical Commission, “Information Technology —Artificial
TABLE II
NEGATIVE RESULTS FROM THE DEPLOYMENT: WHAT FAILED, HOW IT SURFACED, ITS ROOT CAUSE, AND THE OPEN PROBLEM OR GENERALIZABLE LESSON. TWO OF
THE THREE WERE SURFACED BY INTERNAL AUDIT OR PRODUCTION OBSERVATION RATHER THAN BY ADVERSARIAL TESTING OR OPERATIONAL MONITOR ING: THE
CLASS OF FAILURE LABORATORY STUDIES CANNOT OBSERVE.
    Pattern THREAT (§III) Obligation Mechanism Observed Outcome
A. Stale policy
→ systematic
over-verification
Internal audit (not
monitoring)
Window between policy
update and human sign-
off gate; agent retrieved
superseded version.
No native policy-version
synchronization with
compliance lifecycle; gate
guards content, not the pre-
approval window.
A. Stale policy →
systematic over-
verification

B. MCP tools not
designed for
audit
Integration /
remediation stage
Tool-call signatures carry
no case-ID, session, or
provenance; retrofit
forced re-validation.
Auditability is an interface-
design constraint, not an
infrastructure logging
concern; must precede tool
build.
B. MCP tools not
designed for audit

C. ≈1 in 9
applicants
unservable
Production
population
Two-channel 2FA
precondition; single-
channel applicants cannot
complete pipeline
regardless of identity.
No regulatory framework
for systemic exclusion by
technical precondition;
possible disparate-impact
question.
C. ≈1 in 9 applicants
unservable

11

Intelligence—Management System,” ISO/IEC 42001:2023, 1st ed.,
Geneva, Dec. 2023.
[8] P. Lewis et al., “Retrieval -Augmented Generation for Knowledge -
Intensive NLP Tasks,” in Proc. NeurIPS, 2020.
[9] Google, “Agent2Agent (A2A) Protocol: A New Era of Agent
Interoperability,” Google Developers Blog, 2025.
[10] K. Greshake et al., “Not What You’ve Signed Up For:
Compromising Real -World LLM -Integrated Applications with
Indirect Prompt Injection,” in Proc. ACM AISec, 2023.
[11] OWASP Foundation, “OWASP Top 10 for LLM Applications,”
2024–2025.
[12] Board of Governors of the Federal Reserve System, Office of the
Comptroller of the Currency, and Federal Deposit Insurance
Corporation, “Revised Guidance on Model Risk Management,” SR
Letter 26-2, Apr. 17, 2026 (superseding SR 11-7, 2011, and SR 21-8,
2021). [Online]. Available:
https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
[13] D. Rashie and V. Rashi, “Type -Checked Compliance: Deterministic
Guardrails for Agentic Financial Systems Using Lean 4 Theorem
Proving,” arXiv:2604.01483, Apr. 2026.
[14] S. Maiti, “Caging the Agents: A Zero Trust Security Architecture for
Autonomous AI in Healthcare,” arXiv:2603.17419, Mar. 2026.
[15] V. S. Narajala and O. Narayan, “Securing Agentic AI: A
Comprehensive Threat Model and Mitigation Framework for
Generative AI Agents,” arXiv:2504.19956, Apr. 2025.
[16] C. Schroeder de Witt et al., “Open Challenges in Multi -Agent
Security: Towards Secure Systems of Interacting AI Agents,”
arXiv:2505.02077, 2025.
[17] Z. Yang et al., “FinVault: Benchmarking Financial Agent Safety in
Execution-Grounded Environments,” arXiv:2601.07853, Jan. 2026.
[18] Consumer Financial Protection Bureau, “CFPB Circular 2023 -03:
Adverse Action Notification Requirements and the Equal Credit
Opportunity Act (ECOA),” Sep. 19, 2023.
[19] European Parliament and Council of the European Union,
“Regulation (EU) 2024/1689 Laying Down Harmonised Rules on
Artificial Intelligence (Artificial Intelligence Act),” Official Journal
of the European Union, Jun. 2024.
[20] Court of Justice of the European Union, “Judgment in Case C -
634/21, OQ v. Land Hessen (SCHUFA Holding),”
ECLI:EU:C:2023:957, Dec. 2023.
[21] Financial Industry Regulatory Authority, “2026 FINRA Annual
Regulatory Oversight Report: Generative AI —Agents,” FINRA,
Dec. 2025
