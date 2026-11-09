---
title: 'The Amplifier Effect: Human-Factor Risks of AI-Suggested Correlation and Auto-Propagation in Multi-Framework
  GRC Self-Assessment'
url: https://arxiv.org/abs/2610.07866
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Nikolaos Kekatos
- Michael Ioannou
- Marina Korgiala-Karyda
- Alexios Lekidis
- Tom Nianios
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.07866
pages: 7
chars: 33560
fetched_at: '2026-11-08T13:22:42+00:00'
kb_version: 1
---

# The Amplifier Effect: Human-Factor Risks of AI-Suggested Correlation and Auto-Propagation in Multi-Framework GRC Self-Assessment

The Amplifier Effect: Human-Factor Risks of
AI-Suggested Correlation and Auto-Propagation
in Multi-Framework GRC Self-Assessment
N. Kekatos1, M. Ioannou 2, M. Korgiala-Karyda 3, A. Lekidis 3, T. Nianios 1
1Clone Systems, Cyprus –{nkekatos, tnianios}@clone-systems.com 2Bolton Technologies, Cyprus –michael@bts.com.cy
3University of Thessaly, Greece –alekidis@uth.gr, korgialamarina@gmail.com
Abstract—Multi-framework Governance, Risk and Compli-
ance (GRC) platforms increasingly automate the link between
an organisation’s self-assessment answer and the compliance
obligations that answer is said to satisfy. Cross-framework control
mapping, AI-suggested question correlation, and automatic prop-
agation of answers and evidence across correlated questions all
serve the legitimate efficiency goal of reducing duplicate work for
small and medium-sized enterprises (SMEs) under the EU Cyber
Resilience Act (CRA), NIS2 and GDPR. The same mechanisms,
however,amplifythe consequences of any human-factor bias in
a single answer: one optimistically-graded control, one rubber-
stamped attestation, or one AI-drafted answer can be silently
replicated as evidence of compliance with many obligations
across multiple frameworks. We call this theamplifier effect:
a platform-design property (coarse-grained attestation and un-
gated propagation) rather than a failing of individual users. Using
two EU-funded SME-facing GRC platforms, CYBERFORT and
CYBER-BRIDGE, as examples, we (i) describe the amplification
mechanism in concrete data-model terms, (ii) propose a six-
dimension scoring framework for evaluating any GRC tool’s
exposure to the effect, (iii) instantiate the framework on a
thirteen-tool comparison covering enterprise IRM, mid-market
platforms, compliance-automation tools, and the two EU SME
projects, and (iv) outline a measurement protocol that a con-
sortium with access to production self-assessment data can run.
The thirteen-tool comparison is a structured design assessment,
not an empirical measurement of user behaviour. The EU SME
platforms score lowest on the amplifier dimensions because their
burden-reduction design deliberately trades sign-off granularity
for throughput; we report this as a design trade-off, not a
verdict on the platforms. Our contribution is the framing and
the measurement protocol.
Index Terms—Cyber Resilience Act, NIS2, self-assessment,
GRC, human factors, compliance automation, cross-framework
mapping, AI-assisted assessment, SME cybersecurity
I. INTRODUCTION
The EU regulatory stack for cyber resilience is shifting from
periodic external audit towardcontinuous self-assessmentas
the default evidence of compliance. The Cyber Resilience Act
(CRA, Regulation (EU) 2024/2847) [1] obliges manufacturers
of products with digital elements to perform and update
© 2026 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
This work has been accepted for publication at the 2026 IEEE International
Conference on Cyber Security and Resilience (IEEE CSR 2026).
a cybersecurity risk assessment over the product lifecycle;
NIS2 (Directive (EU) 2022/2555) [2] requires essential and
important entities to adopt risk-management measures propor-
tional to exposure; DORA places equivalent recurring duties
on the financial sector [3]; the EU AI Act [4] adds AI-
system risk management to the same regulatory scope. Each
of these regimes ultimately depends onthe truthfulness and
the consistency of an organisation’s own answers.
Two structural responses to this shift are now visible in
the GRC tool market. First, modern GRC/IRM platforms [7]
converge on amulti-frameworkdata model: a single control
or evidence object is mapped against several frameworks
simultaneously, so an SME does not redo the same work for
CRA, ISO/IEC 27001, NIS2, and GDPR [21]. Second, AI
assistance is now embedded inside the assessment workflow
itself: LLM-drafted policies, AI-suggested mappings between
questions, AI-generated readiness narratives, and retrieval-
augmented advisory [22].
Both responses are legitimate gains inefficiency(though, as
we argue in §VIII, not necessarily in usability, which is the
broader property). They also, individually and especially in
combination, create a measurement problem that the human-
factor literature has not yet named. We call it theamplifier
effect: the property that, in a modern multi-framework GRC
platform, a single human assessment action can drive many
compliance assertions, across many frameworks, with no pro-
portional increase in human review.
Framed precisely, the amplifier effect is less a story about
unreliable humans than aboutdesign choices that create the
conditions for human error: an attestation surface too coarse
to localise a mistake, a propagation step with no confirmation
gate, and an AI layer whose suggestions are hard to tell
apart from verified fact. It is a domain-specific instance of
theerror-cascadeproblem studied in automated form-filling
and decision support [23]; what makes the GRC setting acute
is that the cascade terminates in regulatory assertions, so a
general design failure becomes a compliance failure.
A. Concrete amplification mechanism
Two EU-funded platforms make the mechanism easy to
inspect. CYBERFORT [5] is an open-source CRA-first GRC
platform for SMEs deployed under the Digital Europe Pro-
gramme. CYBER-BRIDGE [6] is a cross-border cybersecurity,
arXiv:2610.07866v1  [cs.CR]  6 Oct 2026

compliance and forensics platform under the same programme.
Both share aquestion-correlationlayer that, when a user
answers a question, finds all transitively correlated questions
inside the same scope andpropagates the user’s answer and
supporting evidence to every correlated question automat-
ically.1 The correlation graph is itself partly authored by
humans and partly suggested by an AI service that proposes
new correlations between questions. The resulting causal chain
is:
(user action)answers one question→(platform)
finds the transitive correlation group→(platform)
writes the same answer ontoNcorrelated questions
→(platform)copies the evidence object ontoN
correlated answers→(output)Ncompliance
claims across one or several frameworks.
Each link is defensible in isolation. Theamplifiedobject (one
human action,Ncompliance claims) is what the human-factor
literature on self-assessment reliability has not yet had to
confront.
B. Why the human-factor lens matters
Self-assessment reliability is already known to be limited by
social-desirability bias [8], Dunning–Kruger [9], the expert–
non-expert gap [10], and optimism bias under organisational
incentives [11], [12]. The HFaCS workshop topic list explicitly
namesuser compliance,adoption barriers,organisational cul-
tureandsocio-technical root-cause analysisas open questions.
The amplifier effect cuts across all four: it converts an indi-
vidual answer-level bias into an organisation-level compliance
posture with no intermediate review gate, and it does so
under a UI that presents the propagation as a productivity
feature rather than as a chain of inferences. The AI suggestion
layer adds a second amplification: when the correlation graph
itself is partly AI-authored, automation bias [13] affects which
propagations ever get scrutinised by a human.
C. Contributions
We do not run a controlled user study; we make a design-
level risk explicit and show how it would be measured.
Concretely: (1) we name and define theamplifier effectas
a property of multi-framework GRC platforms with cross-
question answer propagation, and identify the four code-
level mechanisms that produce it (transitive correlation, an-
swer synchronisation, evidence propagation, and AI-suggested
new correlations); (2) we propose asix-dimension scor-
ing framework(§V) for evaluating a tool’s exposure: at-
testation surface, AI-assistance depth, sign-off granularity,
favourability-bias mitigation, training-transfer measurement,
and self-report–telemetry corroboration; (3) we instantiate it
on a thirteen-tool comparison (§VI) spanning enterprise IRM,
mid-market, compliance-automation and quantification tools
plus CYBERFORT and CYBER-BRIDGE [7]; and (4) we
1Implemented assynchronize_correlated_answersand
copy_evidence_filesinquestion_correlation_service.py,
verified at commit3ec8b9dof the CYBER-BRIDGE code base; the same
service is present in CYBERFORT.
outline ameasurement protocol(§VII) a consortium can run
on production data, including five empirical questions.
The remainder of the paper reviews self-assessment reliabil-
ity and the cross-framework GRC data model (§II), describes
the amplifier mechanism in code-level detail (§IV), introduces
the six-dimension scoring framework (§V) and the thirteen-
tool comparison (§VI), sketches the measurement protocol
(§VII), and discusses design recommendations and threats to
validity (§VIII).
II. BACKGROUND
A. Self-Assessment Reliability
Self-assessment of cybersecurity posture inherits the same
biases that decades of psychometric work have documented in
survey research.Social-desirability bias[8] pushes respon-
dents toward answers that reflect well on themselves or their
organisation, particularly when the assessment is tied to a reg-
ulatory obligation. TheDunning–Kruger effect[9] predicts
that the respondents least equipped to evaluate a control are
also the least aware of their own gaps; Ion et al. [10] show this
concretely in security, where non-experts misjudge protective
behaviours relative to expert benchmarks.Optimism bias
under organisational incentives[11], [12] predicts further in-
flation when a favourable answer reduces individual workload;
Beautement et al. formalise this as thecompliance budget, a
finite quantity of effort employees will spend on security tasks
before declining further work.Automation bias[13] predicts
that respondents over-rely on a system-supplied answer even
when independent evidence is available, an effect that is
sharpened when the system speaks with the authority of an
AI assistant [19].
In a workflow where each question is reviewed indepen-
dently, these biases bound the reliability of one answer at a
time. In a workflow where one answer drives many, the same
biases bound the reliability of many answers at once.
B. The Multi-Framework GRC Data Model
Cross-framework mapping is a core capability of modern
integrated risk-management (IRM) suites [7]. ServiceNow
IRM, Archer and MetricStream maintain harmonised control
catalogues mapped to ISO/IEC 27001, NIS2, NIST CSF,
SOC 2, GDPR, DORA and the CRA. Compliance-automation
tools (Drata, Vanta, Secureframe, Hyperproof) provide similar
mappings tuned to SOC 2 and ISO 27001 attestations. EU-
funded SME projects, of which CYBERFORT and CYBER-
BRIDGE are two [5], [6], ship CRA-first mappings that
overlap with ISO/IEC 27001, NIS2 and GDPR. The reuse
pattern is the same across the market: a single control or
evidence object satisfies many obligations.
Continuous Control Monitoring (CCM) via integrations
closes part of this gap by replacing periodic self-attestation
with telemetry-driven evidence. CCM coverage is, however,
uneven: it works well for technical controls (identity, endpoint,
cloud) and poorly for organisational controls (training, aware-
ness, governance), which is where the workshop’sadoption

andorganisational culturetopics live. The amplifier effect
emerges precisely where CCM does not reach.
III. RELATEDWORK
Self-report in security.The HAIS-Q instrument [14] and
SeBIS [15] measure information-security awareness and in-
tended behaviour through Likert self-report; both have docu-
mented social-desirability ceilings. Pfleeger and Caputo [16]
review behavioural science approaches to security risk. Bada,
Sasse and Nurse [17] document why awareness campaigns
relying on self-attestation fail to change behaviour. The present
paper extends this line by examining how the modern GRC
stackmultipliesthe consequences of any one such answer.
AI-assisted decision-making.Buçinca, Malaya and
Gajos [19] show that cognitive forcing functions can reduce
overreliance on AI in decision-making, an effect relevant
to the AI-suggestion layer in §IV. Skitka, Mosier and
Burdick [13] establish the accountability–automation-bias
trade-off that underpins our recommendation R2. We use the
termfavourability bias(sometimes calledsycophancyin the
LLM literature) to denote the tendency of an AI assistant
to produce overly favourable answers when prompted to
advocate for the user.
Compliance critique.Herley’s analysis [18] frames non-
compliance as a rational rejection of advice; the compliance
budget of Beautement et al. [12] formalises the finite effort
employees will spend on security work. The amplifier effect
extends this line: a favourable answer with amplified con-
sequences yields a cheaper local outcome than careful per-
question scrutiny.
GRC tool evaluation.Gartner’s public market listing of
integrated risk-management and GRC tooling [7] provides a
vendor-neutral segmentation of GRC/IRM tooling and under-
pins our thirteen-tool selection (§VI). Existing comparisons
evaluate GRC platforms on functional breadth and on TCO;
we add a human-factor dimension to that comparison.
IV. THEAMPLIFIERMECHANISM
A. Walk-Through
Both platforms treat a singleansweras the unit of attesta-
tion: a value (Yes,No,Partial,Not Applicable) plus
an attached evidence document, tied to one question in one
assessment. When the user answers one question and saves,
which is the only human action in the chain, a stored graph
of question correlations drives four mechanisms that the user
never reviews individually (Fig. 1).
a) Transitive correlation:The platform gathers every
question transitively correlated with the answered one in the
same scope: ifq a is correlated withq b andq b withq c, all three
form one groupG(q).
b) Answer synchronisation:The same value is written
onto every question inG(q)across the organisation’s open
assessments. The user saw one save; the system records up to
|G(q)|answers.
Fig. 1. Assessment view of CYBERFORT. The COMMON INline below
the question lists the correlated assessments to which the user’s answer will
be propagated automatically bysynchronize_correlated_answers;
the AI SUGGESTANSWERSaction at the top right invokes the AI-suggestion
layer. The two mechanisms produce the amplifier effect described in this
paper.
c) Evidence propagation:The evidence document from
the original answer is copied onto every synchronised answer,
so one document now substantiates all|G(q)|claims with no
further review.
d) AI-suggested correlations:An “AI Suggest” action
asks the assistant to propose new correlation pairs. Accepted
suggestions enlargeG(q), so the reach of the next single
answer grows with no human review of the propagation itself.
B. Numerical Sensitivity
Let|F|be the number of frameworks active for the or-
ganisation and let ¯kbe the mean cross-framework correlation
degree of a question (empirically, ¯k∈[2,5]for CRA-anchored
question banks that also cover ISO/IEC 27001 and NIS2). The
amplification factor of a single user answer is then
A(q) =|G(q)| ≈1 + ¯k·(|F| −1),(1)
which for|F|= 4and ¯k= 3givesA≈10. One human
attestation supplies the evidentiary basis for ten compliance
claims.
C. A Worked Example
Consider an SME running CYBERFORT against CRA,
ISO/IEC 27001, and NIS2 simultaneously. Suppose the corre-
lation graph contains the following edges, generated partly by
human authors and partly by the AI suggestion service:
•q CRA-13a: “Does the cybersecurity risk assessment cover
known vulnerabilities?”↔q ISO-8.8: “Is technical vulnera-
bility management implemented?”
•q ISO-8.8 ↔q NIS2-21.2e: “Are vulnerability handling and dis-
closure measures in place?”
•q NIS2-21.2e ↔q CRA-Annex-I-2.1: “Are products placed on the
market without known exploitable vulnerabilities?”
The transitive closure groups all four questions. A user answer-
ingq CRA-13a asYesand attaching an OSV-Scanner report as
evidence triggerssynchronize_correlated_answers

Fig. 2. Assessment view of the CYBER-BRIDGE platform. The same propa-
gation pattern observed in CYBERFORT is visible here: the COMMON INline
below each question lists the tenant assessment(s) to which the user’s answer
is automatically copied, and the assigned policy plus evidence description are
propagated alongside the value. The sidebar shows the broader scope of the
platform (CRA scope, readiness, gap analysis, regulatory submissions, threat
intelligence) over which the same amplifier mechanism operates.
to writeYesonto the other three answers, and
copy_evidence_filesto attach the OSV-Scanner
report to each. The platform emits a single audit-trail entry
per database row, but the human-factor surface is one decision.
If the user mis-classified the scope of the OSV-Scanner run
(e.g., it covered only one of three product components), all
four claims inherit the error silently.
D. The CYBER-BRIDGE Variant
CYBER-BRIDGE runs the same correlation and propa-
gation mechanism as CYBERFORT, and adds a retrieval-
augmented AI assistant on top of it (Fig. 2). 2 The assistant
is asecondamplification path: it retrieves theKquestions
most similar to the one being answered, drafts answers for all
of them, and shows them in a single review pane; when the
user accepts,Kanswers update at once. CYBER-BRIDGE is
thus exposed to the amplifier effect through both the explicit
correlation graph and the retrieval assistant, yet the user sees
the same thing: one attestation, many claims.
V. SIX-DIMENSIONSCORINGFRAMEWORK
We score any GRC platform on six dimensions of exposure
to the amplifier effect. Each dimension admits a four-level
rubric: NONE, LIGHT, MODERATE, STRONG, where higher
is better. The per-tool aggregate in Table I is the rounded
mean across the six dimensions, scoring NONE=0, LIGHT=1,
MODERATE=2, STRONG=3.
1)Attestation surface (AS):fraction of controls corroborated
by Continuous Control Monitoring (CCM) rather than
self-attested; STRONG=CCM covers technical and most
organisational controls, NONE=all self-attested.
2Apgvectorembeddings store over the question bank, a localphi-4
model, and a regulatory-change search layer.
2)AI-assistance depth (AI):reverse-scored; STRONG=AI
only drafts text the human must rewrite, NONE=AI
suggests, propagates and persists with no review gate.
3)Sign-off granularity (SG):STRONG=each propagated
answer needs its own sign-off, NONE=one signature
covers a whole framework instance.
4)Favourability-bias mitigation (SM):whether the user
can steer the AI toward favourable answers (sycophancy);
STRONG=a fixed, audited system prompt the user cannot
override, NONE=the user can freely instruct the AI.
5)Training-transfer measurement (TT):STRONG=post-
training behavioural metrics feed back into the assessment,
NONE=only completion is recorded.
6)Self-report–telemetry corroboration (RT):STRONG=
contradictions between answers and telemetry are surfaced,
NONE=no corroboration.
VI. THIRTEEN-TOOLCOMPARISON
We instantiate the framework on thirteen representative tools
chosen to span the size-and-maturity buckets named in the
GRC market analysis [7]: three enterprise IRM suites, three
mid-market platforms, four compliance-automation tools, one
specialised quantification suite, and the two EU-funded SME
projects CYBERFORT and CYBER-BRIDGE. Scoring is
drawn from public product pages and from the market analysis
itself, and from direct code inspection for CYBERFORT and
CYBER-BRIDGE. The tool comparison is a structured design
assessment, not an empirical measurement of user behaviour.
Scores should be read as indicative design-risk ratings, not as
audited vendor evaluations; the evidence base for the EU SME
rows is the inspected development versions of the platforms
and may change as the projects mature.
Three patterns emerge from Table I.First, enterprise IRM
suites cluster at the top of the range because they couple deep
CCM integrations (high AS, high RT) with mature sign-off
workflows (SG), but they remain weak on training-transfer
measurement (TT) and on favourability-bias mitigation (SM).
Second, compliance-automation tools maximise CCM but
provide little human-attestation structure: the auto-generated
SOC 2 / ISO 27001 evidence packs come with weak SG and
no SM, so a single user can drive a complete framework attes-
tation.Third, EU SME projects CYBERFORT and CYBER-
BRIDGE score lowest. This is by design: their answer-
propagation exists precisely to cut SME workload, and that
is the feature the amplifier dimensions penalise. We flag our
own tools as the most exposed because we can inspect them
directly, which makes them the clearest place to measure the
effect. Their scanners (SAST/DAST/SBOM) corroborate tech-
nical controls but not organisational ones such as training, so
self-report there goes unchecked (RT = LIGHT/MODERATE).
The table describes where the risk sits; it is not a ranking
of good and bad tools. A LIGHTscore is the expected result
for a tool built to cut SME workload, so it is not a failing in
itself. The real concern is narrower: when weak per-answer
sign-off (SG) is combined with AI writing the answers, many
compliance claims can rest on very little human attestation, an

TABLE I
THIRTEEN-TOOL EXPOSURE TO THE AMPLIFIER EFFECT ACROSS SIX HUMAN-FACTOR DIMENSIONS. HIGHER IS BETTER. AS:ATTESTATION SURFACE;
AI: AI-ASSISTANCE MITIGATION; SG:SIGN-OFF GRANULARITY; SM:FAVOURABILITY-BIAS MITIGATION; TT:TRAINING-TRANSFER MEASUREMENT;
RT:SELF-REPORT–TELEMETRY CORROBORATION.
Bucket Platform AS AI SG SM TT RT Aggregate
Enterprise IRM ServiceNow IRM Strong Moderate Strong Light Light Strong Moderate
Archer Moderate Light Strong Light Light Moderate Moderate
MetricStream Strong Light Moderate Light Light Moderate Moderate
Mid-market LogicGate Moderate Light Moderate Light None Moderate Light–Mod
StandardFusion Moderate Light Moderate Light None Moderate Light–Mod
Onspring Light Light Moderate Light None Light Light
Compliance automation Drata Strong Light Moderate None None Strong Moderate
Vanta Strong Light Moderate None None Strong Moderate
Hyperproof Moderate Light Moderate None None Moderate Light–Mod
ControlMap Strong Light Moderate None None Strong Moderate
Quantification RiskLens Light Moderate Moderate Moderate None Light Light–Mod
EU SME projects CYBERFORT Light None Light None Light Light Light
CYBER-BRIDGE Light None Light None Light Moderate Light
outcome the regulation did not anticipate because it assumed
a human meaningfully stands behind each claim.
VII. MEASUREMENTPROTOCOL
A consortium that operates a production GRC deployment
(such as CYBERFORT’s cohort of43SME tenants,109users
and60framework instances [5]) can answer five empirical
questions directly from its database, under an aggregate-only
publication policy. Each question yields evidence on a different
facet of the amplifier effect.
a) Q1: answer distribution:For each
FrameworkQuestion, report the empirical distribution of
Answer.valueacross all users. A skew toward favourable
values (Pr[Yes]≫0.5) on questions for which no objective
telemetry exists is the headline optimism-bias signal.
b) Q2: time-to-answer:Compute the per-answer dwell
time as∆t i =updated_at i −created_at i. A short
∆twith a favourablevalueon a correlated question is the
headline rubber-stamp signal.
c) Q3: evidence reuse multiplicity:For eachEvidence
object linked to more than oneAnswer, report the count.
A heavy-tailed distribution indicates that a small number
of evidence objects substantiate a disproportionate share of
the platform’s compliance claims: the single-point-of-failure
signal.
d) Q4: AI-assisted vs. unassisted:Where the AI-
assistance invocation is logged per answer, compare the an-
swer distribution and the∆tdistribution between the AI-
assisted and unassisted strata. A leftward shift of∆twithout
a corresponding shift in the answer distribution is consistent
with automation acceleration without bias change; a shift in
both is consistent with automation bias.
e) Q5: favourability-bias probe:For ten representative
CRA questions, prompt the platform’s LLM (Mistral 7B for
CYBERFORT, phi-4 for CYBER-BRIDGE) twice: once with
a neutral-consultant system prompt, once with an “advise-the-
SME-favourably” prompt. Report divergence on the answer
rubric. A non-zero divergence quantifies the sycophancy attack
surface of the AI-assistance layer.
The five questions are mechanically reproducible once in-
strumentation is in place. Q1–Q3 require only existing tables;
Q4 may require adding a per-answer AI-invocation log; Q5 is
a one-day controlled probe.
VIII. DISCUSSION
A. A Usability-Heuristic Reading
The amplifier effect can be restated as a set of violated
usability heuristics [20]. Silent propagation breachesvisibility
of system status: the user is never shown that one answer
becameNcompliance claims; the absence of a per-target
confirmation breachesuser control and freedomanderror
prevention; and surfacing AI-suggested correlations indistin-
guishably from human-authored ones erodes the user’s model
of what the system actually knows. Read this way, the effect
is a predictable consequence of omitting the confirmation,
undo, and status-disclosure affordances that the human-factors
literature treats as baseline, which is why we describe the
propagation as an efficiency gain but not a usability one.
B. Design Recommendations
Three recommendations follow from the mechanism and
the matrix.(R1) Review gate on propagated answers.The
answer-synchronisation step should require an explicit per-
target acknowledgement when the propagated answer would
change a previously filled value, or when the target question
is mandatory and the source is not.(R2) AI-action audit log.
Every AI invocation that touches an answer, correlation, or
evidence record should be persisted with the originating user
ID, the system prompt, and a hash of the AI output, to support
both Q4 and external audit.(R3) Transfer measurement on

training.Cyber-range deliverables in both CYBERFORT and
CYBER-BRIDGE log completion but not behavioural transfer;
a mandatory post-training behavioural probe (e.g., a phishing
simulation rate measured before and after) would convert the
TT column from LIGHTto MODERATE.
C. Threats to Validity
The scoring in Table I is derived from public sources and
from direct code inspection of two platforms. We did not
conduct hands-on evaluation of the eleven commercial tools;
their scores reflect documented features and may be revised by
trial use or vendor input, and a vendor may legitimately dispute
a LIGHTscore. Only CYBERFORT and CYBER-BRIDGE
were assessed by direct inspection. The amplification factor
in (1) is a structural upper bound; the realised amplification
depends on the density of the correlation graph in deployment.
The measurement protocol is described but not executed; we
treat its execution as the natural next deliverable for the
CYBERFORT and CYBER-BRIDGE consortia.
D. Ethical and Deployment Considerations
Analysing production self-assessment data carries
workforce-monitoring implications. We assume the five-
question protocol is run under aggregate-only publication,
that no individual or tenant-identifiable rows leave the
consortium, and that the SME tenants are informed of
the analysis in their original data-sharing agreement. The
sycophancy probe (Q5) is conducted on synthetic vignettes
rather than on tenant answers, and poses no additional
disclosure risk.
IX. CONCLUSION
In this paper, we have introduced and characterised the
amplifier effectin multi-framework governance, risk, and
compliance platforms: the property that a single human self-
assessment action, combined with cross-framework mapping
and automatic answer/evidence propagation, drives many com-
pliance assertions without a proportional increase in human
review. We have described the mechanism in code-level detail
for two EU-funded production platforms, proposed a six-
dimension scoring framework for evaluating any GRC tool’s
exposure, instantiated the framework on thirteen representative
tools, and outlined a five-question measurement protocol that
a consortium with access to production self-assessment data
can execute. The amplifier effect is a structural property of the
modern GRC stack and is tractable to measure once named.
Future work will execute the measurement protocol on the
CYBERFORT first cohort, report the empirical distributions
ofA(q)and∆tacross the deployment, and complement
the log analysis withuser research(think-aloud sessions and
a controlled test of whether making the propagation scope
visible changes attestation behaviour) to close the end-user
perspective that this design-level analysis leaves open.
ACKNOWLEDGMENT
This work has received funding from the European
Union’s Digital Europe Programme under grant agreements
No 101249702 (CYBER-BRIDGE) and No 101190281 (CY-
BERFORT).
REFERENCES
[1] European Parliament and Council of the European Union, “Regulation
(EU) 2024/2847 on horizontal cybersecurity requirements for products
with digital elements (Cyber Resilience Act),”Official Journal of the
European Union, Nov. 2024.
[2] European Parliament and Council of the European Union, “Directive
(EU) 2022/2555 on measures for a high common level of cybersecu-
rity across the Union (NIS2),”Official Journal, L 333, pp. 80–152,
Dec. 2022.
[3] European Parliament and Council of the European Union, “Regulation
(EU) 2022/2554 on digital operational resilience for the financial sector
(DORA),”Official Journal, L 333, Dec. 2022.
[4] European Parliament and Council of the European Union, “Regulation
(EU) 2024/1689 laying down harmonised rules on artificial intelligence
(AI Act),”Official Journal, Jul. 2024.
[5] N. Kekatoset al., “CYBERFORT: A compliance-chain platform opera-
tionalising the Cyber Resilience Act for SMEs,” under submission, IEEE
CSR, 2026. Project page: https://cyber-fort.eu/.
[6] N. Kekatoset al., “The CYBER-BRIDGE project: an AI-powered
platform for cross-border cybersecurity, compliance and forensics in
the EU,” under submission, IEEE CSR, 2026. Project page: https:
//cyber-bridge.eu/.
[7] Gartner, “Integrated risk management solutions reviews and ratings,”
Gartner Peer Insights, 2025. [Online]. Available: https://www.gartner.
com/reviews/market/integrated-risk-management (accessed Jul. 2026).
[8] D. L. Paulhus, “Measurement and control of response bias,” inMeasures
of Personality and Social Psychological Attitudes, J. P. Robinson,
P. R. Shaver, and L. S. Wrightsman, Eds. Academic Press, 1991, pp. 17–
59.
[9] J. Kruger and D. Dunning, “Unskilled and unaware of it: how diffi-
culties in recognizing one’s own incompetence lead to inflated self-
assessments,”Journal of Personality and Social Psychology, vol. 77,
no. 6, pp. 1121–1134, Dec. 1999.
[10] I. Ion, R. Reeder, and S. Consolvo, “. . . no one can hack my mind:
comparing expert and non-expert security practices,” inProc. SOUPS,
2015, pp. 327–346.
[11] A. Adams and M. A. Sasse, “Users are not the enemy,”Communications
of the ACM, vol. 42, no. 12, pp. 40–46, Dec. 1999.
[12] A. Beautement, M. A. Sasse, and M. Wonham, “The compliance budget:
managing security behaviour in organisations,” inProc. NSPW, 2008,
pp. 47–58.
[13] L. J. Skitka, K. Mosier, and M. D. Burdick, “Accountability and
automation bias,”International Journal of Human-Computer Studies,
vol. 52, no. 4, pp. 701–717, Apr. 2000.
[14] K. Parsonset al., “The human aspects of information security question-
naire (HAIS-Q): two further validation studies,”Computers & Security,
vol. 66, pp. 40–51, 2017.
[15] S. Egelman and E. Peer, “Scaling the security wall: developing a security
behavior intentions scale (SeBIS),” inProc. ACM CHI, 2015, pp. 2873–
2882.
[16] S. L. Pfleeger and D. D. Caputo, “Leveraging behavioral science to
mitigate cyber security risk,”Computers & Security, vol. 31, no. 4,
pp. 597–611, 2012.
[17] M. Bada, A. M. Sasse, and J. R. C. Nurse, “Cyber security awareness
campaigns: why do they fail to change behaviour?” arXiv:1901.02672,
2019.
[18] C. Herley, “So long, and no thanks for the externalities: the rational
rejection of security advice by users,” inProc. NSPW, 2009, pp. 133–
144.
[19] Z. Buçinca, M. B. Malaya, and K. Z. Gajos, “To trust or to think:
cognitive forcing functions can reduce overreliance on AI in AI-assisted
decision-making,” inProc. ACM Human-Computer Interaction (CSCW),
vol. 5, no. CSCW1, art. 188, 2021.
[20] J. Nielsen, “Enhancing the explanatory power of usability heuristics,” in
Proc. ACM CHI, 1994, pp. 152–158.

[21] Secure Controls Framework Council, “Secure Controls Framework
(SCF): a cybersecurity and privacy metaframework mapping 1,500+
controls to 200+ laws, regulations and frameworks,” 2025. [Online].
Available: https://securecontrolsframework.com/ (accessed Jul. 2026).
[22] S. Hu, P. Wang, K. I. Chan, Y . Yao, and Z. Lu, “I always felt that
something was wrong: understanding compliance risks and mitigation
strategies when highly-skilled compliance knowledge workers use large
language models,” arXiv:2411.04576, 2024.
[23] K. Goddard, A. Roudsari, and J. C. Wyatt, “Automation bias: a system-
atic review of frequency, effect mediators, and mitigators,”Journal of the
American Medical Informatics Association, vol. 19, no. 1, pp. 121–127,
2012.
