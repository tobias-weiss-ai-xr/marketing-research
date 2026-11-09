---
title: 'Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries'
url: https://arxiv.org/abs/2610.23362
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Junchi Liao
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.23362
pages: 8
chars: 39006
fetched_at: '2026-11-08T13:33:35+00:00'
kb_version: 1
---

# Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries

Monitor-Validity Failures: LLM Safety Evidence Paths
at Evolving Framework Boundaries
Junchi Liao
Abstract
Modern LLM applications rely on runtime monitors that in-
spect tool calls, traces, streams, detector outputs, and verifier
inputs. This creates an interface-reliability problem: a frame-
work path may remain operational while policy-relevant ev-
idence never reaches its decision point. In one representa-
tive case, a regex detector returned a positive match, but the
framework stranded the result before the block decision. This
differs from jailbreaks and detector errors because the evi-
dence is already recognized yet disconnected from enforce-
ment. We study this repair-boundary signature with canary
contracts: parent/fixed confirmation units that place a known
payload only on the changed evidence surface and record
monitor visibility together with the downstream decision for
action-boundarycases.Applyingtheprotocoltopublicframe-
work repairs, we confirm 18 evidence-path failures across 11
LLM or agent safety project groups and four implementa-
tionecosystems.Nineareestablished-boundaryrepairs,eight
arenew-surfacepolicy-coveragegaps,andoneisaboundary-
only evidence case. Fourteen reach E1 enforcement bound-
aries: seven native action outcomes, six configured enforce-
ment boundaries, and one synthetic-consumer consequence.
The remaining cases affect verifier, safety-prompt, or observ-
ability channels. The cases form carrier, adapter, authority,
and surface families and show how ordinary application be-
haviorcanremainintactwhileasafety-specificevidencepath
misses its decision. Exact revisions, deterministic outcomes,
negative controls, and a frozen prospective audit document
theconfirmationrule.Monitorassumptionsthereforeneedre-
gressiontestsattheschemas,streams,tools,andadaptersthat
frameworks evolve.
Introduction
A guardrail in a modern LLM application is rarely just a
prompt wrapper. Before it blocks, routes, redacts, or re-
ports,itmayreadrequestobjects,tool-callarguments,stream
events, generated files, detector outputs, or verifier inputs.
Safety therefore depends on structured evidence that sits be-
tween the prompt and the final response (Inan et al. 2023;
Han et al. 2024; Wang, Poskitt, and Sun 2025).
AreproducedNeMoGuardrailsrepairshowstheproblem
in miniature. The regex detector returned a structured posi-
tive result withis_match=true. The parent framework still
allowed the output, because that positive result was never
mapped to the block decision. The fixed revision added the
missing output mapping, and the same canary was blocked.
Nothing here calls fora stronger jailbreak prompt or abetter
regex. The detector had seen the evidence; the framework
had dropped it before enforcement.
The NeMo case is only one instance of a broader soft-
ware problem. Request schemas change, tool-call represen-
tationsexpand,multimodalfieldsappear,streamingsurfaces
areadded,andpolicyadaptersarerefactored.Agentandtool-
use systems make these surfaces part of ordinary execution
(Yao et al. 2022; Schick et al. 2023; Qin et al. 2023). A
monitor can stay configured and stay in the loop while the
evidence it relies on moves to a new field, loses metadata,
reaches a different adapter, or is materialized only after the
safety check. We use monitor-validity failure for the observ-
ableparent/fixedrepaircontrastandreservemonitor-validity
drift for its longitudinal working-to-failing subtype.
Thatfailureiseasytomisswhentheproblemisframedas
another jailbreak or guardrail benchmark (Wei, Haghtalab,
and Steinhardt 2023; Mazeika et al. 2024; Zhan et al. 2024;
Debenedettietal.2024;Andriushchenkoetal.2024).Those
evaluations ask whether unsafe behavior can be elicited or
recognized through a specified interface. Our question is
different: once evidence is recognized, does the exercised
framework path carry it to the policy boundary? A strong
detector, policy DSL, verifier, or LLM-as-judge component
cannot protect a reproduced boundary when the parent path
doesnotdelivertheevidenceorpositiveresultitwasdesigned
to use.
Source diffs and issue reports are not enough to confirm
thismiss.Theparentrevisionmustalreadyhaveanintended
boundary, a deterministic payload must cross the changed
surface, and the parent and fixed revisions must differ in
visibility or decision behavior. We use canary contracts as
the confirmation unit. Each contract places a known policy-
relevant payload only on the changed evidence surface and
recordsmonitorvisibilitytogetherwithdownstreamdecision
behavior when the case claims an action boundary.
Using canary contracts, we study 18 confirmed repair-
boundarycasesacross11frameworkprojectgroupsandfour
implementation ecosystems. We keep the evidence strata
explicit: 9 are established-boundary repair cases, eight are
new-surface validity gaps, and one remains boundary-only
evidence. We also keep reproduction strength separate from
impact:14casesreachE1enforcementboundaries,compris-
ingsevennativeactionoutcomes,sixconfiguredenforcement
arXiv:2610.23362v1  [cs.AI]  16 Oct 2026

Figure 1: Monitor-validity failure at a repair boundary. The parent monitor still runs but reads an incomplete evidence surface;
the repaired child reconnects the same canary payload to monitor visibility and decision.
boundaries,andonesynthetic-consumerconsequence,while
theremainingcasesaffectverifier,safety-prompt,orobserv-
abilitychannels.Weorganizethecasesintofourdependency
families, depending on where the hidden assumption broke:
the payload carrier, the detector-to-action adapter, the au-
thorityamongcompetingchannels,orthemonitoredsurface
itself.
This framing also fixes the unit of evaluation. We do not
ask whether a model is unsafe in general. We ask whether
a specific safety boundary still receives the evidence it was
builttouse.Thatdistinctionmattersforregressiontesting:the
failing object is often a schema, adapter, stream, or callback
rather than a prompt.
This paper makes three contributions:
•We provide a case-level corpus of 18 repair-boundary
confirmations across 11 framework project groups, with
exact revisions, deterministic canaries, and explicit evi-
dence, impact, subtype, and oracle records.
•Weorganizethecasesintofourstructuralfailurefamilies
that explain how hidden evidence-to-decision assump-
tions break under framework evolution.
•We use canary contracts as safety-specific differen-
tial regression-test templates, and we report a five-case
runnable diagnostic comparison of full canary contracts
with partial checks.
Background and Problem Setting
Theexamplesaboveshareasimpleshape:safetylogicreadsa
frameworkrepresentation,nottheworlddirectly.Thissection
fixes the vocabulary for the runtime objects, decisions, and
change patterns used in the study.
Runtime Safety Monitors
We treat a runtime monitor as any component that observes
framework state and can affect a safety-relevant decision.
The state may be a message, tool call, stream delta, trace
metadata field, detector result, provider metadata object, or
artifact path. The decision may block a request, redact out-
put, interrupt a tool call, route a filter result, cap automatic
tool execution, or produce a verifier finding. The important
dependency is structural: the policy boundary only works
if it still sees the runtime representation that carries policy-
relevant state.
Monitor-Validity Failures at Repair Boundaries
Monitor validity is relative to the representation and routing
path that a policy boundary actually uses. We empirically
study repair-boundary failures: in a reproduced parent revi-
sion, a policy-relevant canary is absent from the monitor-
visible evidence or fails to reach the expected decision; in
the fixed revision, the same canary reaches the correspond-
ing visibility or decision oracle. This two-point contrast es-
tablishes a failing parent and repaired child, not an earlier
working revision.
For example, a request guardrail may inspect user text in
amessagesfieldwhileasupportedrequestpathcarriesthe
policy-relevant payload throughinput. The application path
cancompletenormallyeventhoughtheguardrailreceivesan
empty or stale view. Other cases preserve the evidence but
strand a detector result, skip a configured hook, or select the
wrong authority before the decision boundary.
Thefailureissilentinthismechanicalsense.Thechanged
framework path need not crash, and the monitor need not
disappear from configuration. Instead, policy-relevant state
crosses a dependency boundary that the monitor treats as
complete. For a given monitor, only part of the frame-
workstateisvisible:messagefields,tool-callobjects,stream
chunks, detector outputs, callback arguments, or verifier in-
puts. When several fields describe the same event, the mon-
itor also depends on which field the framework treats as
controlling, such as free-text content or structured tool-call
metadata.
Wereservemonitor-validitydriftforaworking-to-failing-
to-repaired temporal subtype; none of our 18 cases estab-
lishes that full interval. Our cases establish only failing-

parent/repaired-childrepaircontrasts.Acanarycontracttests
that contrast by placing the same payload on the exercised
surface and checking visibility and, where applicable, deci-
sion behavior.
Aconfirmedrepair-boundarycasecomparesaparentrevi-
sionandafixedrevisionaroundapublicrepair.Therelevant
parent-sideframeworkpathmustremainoperational,butthe
payloadmustbeabsentfrommonitor-visibleevidenceorfail
to reach the decision. The fixed side must connect the same
payload to the corresponding visibility or decision oracle.
We do not require that the parent revision introduced the
failing condition; it is the nearest reproduced failing side of
a public repair boundary. A canary contract packages this
check into a small before/after assertion over visibility and,
whenever the case reaches an action boundary, block, route,
redact, interrupt, or finding behavior.
Scope
The study is targeted and deterministic rather than
prevalence-oriented. The empirical contribution is a docu-
mented set of 18 confirmed repair-boundary cases where a
safety monitor and an evolving framework disagree about
the evidence that reaches a policy boundary. Cases were se-
lectedforfeasibilityanddeterminism,andthecorpusreports
confirmation, reproduction strength, impact, and subtype as
separate axes. Detailed provenance and reproduction proto-
cols are provided with the case records and artifact.
Canary Contracts: A Method for Confirming
Silent Boundary Failures
Suspicious patches are easy to find; confirmed failures are
not. For each candidate, we need to show that the parent
versionalreadyhadarelevantsafetyboundary,thatapolicy-
relevant payload crossed the changed surface, and that the
fixed version reconnects that payload to visibility or action.
We use a canary contract for this check: one payload, one
repaired boundary, and two observations about the same ex-
ecution.
The contract isolates interface reliability from prompt or
model quality. It places a known payload exactly on the
changedcarrier,adapterresult,stream,orauthoritychannel,
thencompareswhattheparentandfixedversionsexposeand
which decisions they make. In our cases, that payload is a
smalldeterministicmarkerchosenfortheboundary:adenied
tool name, a regex-matching token, a synthetic credential, a
tool argument, or a vulnerable code snippet. Its important
property is placement, not linguistic difficulty.
The Confirmation Problem
Silentfailuresleavelittleobviousevidenceinordinaryexecu-
tion. The application may return normally, the monitor may
still be configured, and logs may show that some guardrail
code ran. A source diff or issue title is therefore not enough.
The same patch could repair a real monitor miss, remove an
old boundary, add a new feature, or refactor code without
changing behavior. We only count the first case, so the pro-
tocol has to isolate the evidence-to-decision path: the parent
Table 1: Canary-contract fields used for confirmation.
Contract field Role in confirmation
Version pair fix the parent/repaired revisions
Boundary exclude new features or removed policies
Canary place payload only on the changed surface
Visibility oracle check monitor visibility of the payload
Decision oracle check whether the intended action fires
must miss the payload, and the fixed version must restore
visibility or enforcement.
Canary Contract Definition
Inpractice,acontractrecordsfivethings:therepairedversion
pair,theintendedmonitorboundary,thecanaryplacement,a
visibilitycheck,andadecisioncheck.Thecanarypayloadis
a tracer for the evidence path, not an attack prompt: the test
askswhethersafety-relevantevidencestillreachesthepolicy
boundary. The version pair fixes the software change under
study. The boundary explains why the parent should already
haveobservedorenforcedthepayload.Theplacementkeeps
the payload off legacy surfaces, so a passing fixed result
cannot be explained by an unrelated detector path. The two
checks separate seeing the evidence from acting on it.
Visibility and decision are separate because they fail in
differentplaces.Adetectorcanreturnapositivematchwhile
an adapter lets the output through; a blocking path can work
forchatmessageswhileanewerrequestshaperemainsinvis-
ible. In the regex example, the visibility check asks whether
thedetectormatched,whilethedecisioncheckaskswhether
thatmatchblockedtheoutput.Acaseisconfirmedonlywhen
theparentshowsthemissandthefixedversionshowsthere-
pair. Candidates that crash, fail closed, or depend on model
sampling are recorded separately.
Viewed this way, a canary contract is a regression test
with a safety-specific oracle. Ordinary regression tests ask
whether functional behavior is preserved. This test asks
whether a policy intent is still connected to the evidence
surface that changed. The useful part is the placement: put
the payload only on the new carrier, stream, adapter result,
or authority channel, then record monitor visibility and, at
action boundaries, the safety action.
Case Selection and Corpus Construction
Webuiltthecorpusfrompublicrepairreferences,issuetrails,
commit scans, and project-specific triage. A reconstructed
denominatorpasscontributed195high-signalpublicPRand
issue references using monitor and failure-indicator queries;
every candidate source was subjected to the same confirma-
tionrule.AppendixBrecordsthequeryflow,candidate-entry
routes, and exclusions (Table 9).
Promising references moved forward only after a deter-
ministic parent/fixed contrast could be reproduced. Other-
wise they stayed as notes, boundary cases, or negative con-
trols. A case is counted only when all six conditions hold:
identifiable parent and fixed revisions; evidence of an in-
tended safety contract for the affected or equivalent surface;

a deterministic payload placed only on the changed surface;
execution of the parent-side monitor path; a parent miss in
visibilityordecision;andafixed-siderepairofthesamevis-
ibility or decision. We treated a boundary as intended only
when supported by configuration semantics, prior behavior
on an equivalent surface, an upstream or fixed regression
test, documentation, or issue/PR discussion. Loud crashes,
unmerged PRs, ordinary feature additions, generic auth or
rate-limit bugs, and fail-closed parents were excluded. Ap-
pendixDrecordstheintent-evidencetypeforeachconfirmed
case (Table 13).
Subtype assignment is separate from confirmation.
Established-boundarycaseshaveanintendedaffectedbound-
aryontheparentside;new-surfacecasesconnectanexisting
policy expectation to a newly supported representation. The
boundary-only row preserves a deterministic repair contrast
while keeping its temporal subtype separate from the estab-
lished and new-surface groups.
We record the primary source of intent evidence for ev-
ery case: an existing test or fixture for eight cases, issue or
pull-requestdiscussionforfive,configurationordocumented
semantics for four, and equivalent-surface behavior for one.
Appendix D preserves the richer case-level source descrip-
tions.
For each promoted candidate, we wrote or backported a
canary that places the payload on the changed surface and
checks visibility and decision whenever the case claims an
enforcement boundary. The confirmed corpus contains 18
casesacross11frameworkprojectsandfourimplementation
ecosystems. Project counts use framework-level groups: for
example, Semantic Kernel Python and .NET are one project
group, and the LiteLLM/Dynamiq stream case is counted
under the LiteLLM boundary. Together, these procedures
produceaconfirmedcross-frameworkcorpuswithauniform
parent/fixed behavioral oracle.
Evidence and Impact Tiers
Table 2 summarizes the corpus. We report two axes: re-
production strength and demonstrated impact. Reproduction
strengthrecordshowdirectlythecanaryreachesthechanged
monitor boundary: Tier A uses framework-level or module-
level execution; Tier B isolates the changed logic with stubs
aroundunrelateddependencies.Impactrecordsthestrongest
safety boundary shown by the canary: E1 for enforcement,
blocking, interruption, rewrite, filter, or routing decisions;
E2 for verifier or safety-prompt evidence decisions; E3 for
evidence visible only in an observability channel.
The table also reports known-pattern fixture patterns.
These small local fixtures check whether a metadata emitter
can express the same visibility and decision contract shape
across all four observed pattern classes.
The rows serve different parts of the empirical claim. The
18confirmedcasessupportthebefore/afterbehaviorclaims;
the project, ecosystem, tier, and impact rows describe the
breadthandboundaryofthosecases.Thefixtureanddenom-
inatorrowsareauditrecords:theycheckcontractexpression
and candidate selection, but they are not additional failures
or a prevalence sample.
Table 2: Summary of the confirmed corpus and validation
records.
Study item Count
Confirmed before/after cases 18
Established / new-surface / boundary-only 9 / 8 / 1
Framework projects 11
Implementation ecosystems 4
Tier A / Tier B confirmations 17 / 1
E1 / E2 / E3 impact boundaries 14 / 3 / 1
Known-pattern fixture families 14
Manually labeled denominator refs 195
Figure 2: Distribution of the 18 cases by first broken
evidence-to-decision dependency; percentages are descrip-
tive corpus shares.
Theseaxesdistinguishexecutiondepthfromdemonstrated
impact.TierAexecutesframeworkormodulemonitorcode,
whileTierBisolateschangedlogicaroundunrelateddepen-
dencies. E1 cases exercise action boundaries and E2 cases
exerciseverifierorsafety-promptevidence.All18casesmeet
the canary-contract confirmation rule.
Experiments
The confirmation protocol gives us a concrete unit of ev-
idence: a parent miss and fixed repair for a specific mon-
itor boundary. The experiments ask four questions in the
order a skeptical reader needs them answered: what breaks,
whether confirmed repair-boundary cases span frameworks,
how far misses reach into safety decisions, and what con-
trols bound the method claims. The confirmed case remains
theunitthroughout;project-levelcountsmeasureonlycross-
framework breadth.
RQ1: What Assumptions Break Under Framework
Evolution?
Wefirstcharacterizewhatbreakswhentheserepair-boundary
evidence-path failures occur. We organize the 18 confirmed
repair-boundary cases into four structural failure families,
each corresponding to a different hidden assumption about
the path from evidence to decision. The family label marks
the first broken dependency on the exercised evidence-to-
decision path.
Figure 2 gives the descriptive split in this targeted cor-
pus.Wedonotusethesecountsasprevalenceevidence.The
useful distinction is where the hidden assumption breaks
and where the canary must be placed. A carrier canary tests

Table 3: Failure families and the canary focus used to test
each hidden assumption.
Family Hidden assumption Canary focus
Carrier payload location new carrier only
Adapter result-to-action map positive result
Authority channel priority disagreement
Surface materialization order new surface only
Figure3:Representativecanarycontractsfromtheconfirmed
corpus, one per failure family. The full 18-case audit matrix
appears in Appendix D.
whetherthepayloadremainsattachedtotheobjectthemon-
itorreads;anadaptercanarytestswhetherapositivemonitor
resultreachesanaction;anauthoritycanaryforcestwochan-
nelstodisagree;andasurfacecanaryplacesthepayloadonly
on the newly materialized request or stream surface.
The established-boundary subset sharpens the repair
claim. Restricted to the 9 cases where an existing intended
monitor boundary misses evidence or action on the repro-
duced parent side, the corpus has Adapter, Authority, and
Carrier failures (4, 3, and 2 cases respectively), all at E1
action boundaries, across eight project groups. The Surface
casesinthiscorpusarenew-surfacevaliditygaps,sowetreat
themasrelatedrepair-boundaryfailuresratherthantemporal
regressions.
Figure 3 shows one representative contract per family.
Each card records the assumption being tested, the targeted
canary placement, the parent-to-fixed outcome, and the re-
production/impact badge.
Carrier failures are silent because the monitored object
still exists, but the policy-relevant payload has moved to a
different carrier. Invariant is the canonical example: the pol-
icy analyzer matched a nested tool call, but pending-trace
metadata was attached only to the top-level message, so the
violation was filtered as not pending. The correct canary
therefore puts the forbidden payload only on the nested car-
rier and checks both metadata visibility and policy decision.
Adapterfailurespreservedetectionbutbreakenforcement.
In the NeMo regex case, the detector returned a structured
positive result, but the parent action lacked the output map-
ping that turns that result into a block. The monitor path
therefore looked alive: the detector ran and returned a re-
sult. The missing contract was the detector-output-to-action
adapter, so the canary must force a positive result and assert
Figure4:Descriptivecompositionofthe18confirmedrepair-
boundary cases; these convenience-corpus counts are not
prevalence estimates.
that it reaches the blocking decision.
Authority failures arise when a framework exposes mul-
tiple plausible channels for the same event. A tool call may
appear in structured metadata while a text field remains be-
nign,orapublicagentidentitymaybereplacedbyaninternal
execution clone. These cases are silent because downstream
policy logic reads a valid-looking but lower-authority rep-
resentation. Their canaries make two channels disagree and
assert that the monitor uses the channel intended by the pol-
icy boundary.
Surface failures occur when frameworks add or reorder
request, stream, or multimodal surfaces. A monitor that still
inspectstextmessagescanmissimageparts,ResponsesAPI
inputs, or live stream chunks if those surfaces are material-
ized after inspection. The surface canary keeps the payload
absent from the legacy surface and places it only on the
newly supported surface. This makes the failure a structural
coverage miss rather than a detector-quality miss.
Each family requires a different regression contract. A
generic jailbreak prompt may put the same payload in every
field and make both parent and fixed versions pass. These
canaries are small because placement, not prompt strength,
is the test.
RQ2: Do Confirmed Cases Appear Across
Frameworks?
Thetaxonomyabovewouldbelessimportantifitdescribeda
pathologyinonelibrary.Wenextaskwhethertheconfirmed
repair-boundarycasesappearacrossprojects,monitorforms,
and implementation ecosystems.
We use three breadth checks. The figure summarizes
projectandmonitorboundaries,theecosystemmatrixchecks
whether observed families appear outside one implementa-
tion language, and the project table checks whether the cor-
pus is dominated by a single large repository. Together, the
three views distinguish structural recurrence from concen-
tration in one repository or language.
Figure 4 and Tables 5 and 6 show that the curated corpus
containsexamplesfrommultipleprojects,monitortypes,and
implementation ecosystems. The largest individual project
contributesfourcases,whiletheremainingcasesspanpolicy
analyzers,outputrails,proxyguardrails,verifiers,toolhooks,
stream adapters, and model-client parsers. Six cases occur
outside Python, across TypeScript, Java, and C#/.NET. The
CSV records 13 raw project labels, which we group into 11

Table4:Impact-boundarybreakdownforconfirmedmisses.E1issplitbyenforcementform;its14casescomprisesevennative
actions, six configured boundaries, and one synthetic-consumer consequence.
Tier Boundary type Cases Broken safety effect Example
E1 block / filter / rewrite 5 unsafe content passes in parent; repair blocks or rewrites it NeMo regex
E1 interrupt / HITL route 3 tool execution or routing bypasses the intended stop point Haystack
E1 hook / cap / policy state 6 configured enforcement hook, cap, or rule update does not
fire
CrewAI
E2 verifier / safety prompt 3 evidence is missing from evaluator or safety-prompt input Promptfoo
E3 observability channel 1 structured evidence is hidden from a policy-relevant con-
sumer
AutoGen
Table 5: Breadth of failure families across implementa-
tionecosystems.Languagecolumnscountconfirmedrepair-
boundary cases; Projects counts distinct framework project
groups touched by each family.
Family Py TS Java C# Projects
Carrier 3 2 0 0 4
Adapter 4 0 0 1 3
Authority 2 2 0 0 4
Surface 3 0 1 0 4
Table6:Descriptiveconfirmed-casecountsbyprojectfamily.
Project group Cases Boundary
LiteLLM 4 proxy, stream, policy
Promptfoo 3 verifier, tool-use
NeMo Guardrails 2 output, multimodal
Semantic Kernel 2 termination, filters
Single-case projects 7 analyzer, client, hook
frameworkprojectfamilies;theestablished-boundarysubset
still spans eight project groups.
This breadth matrix matters because it separates family
fromframework.Thesameprojectcanexposemultiplefam-
ilies at different safety integration points: request parsing,
structured tool evidence, downstream policy consumers, or
policy-stateupdates.Conversely,thesamefamilycanappear
in unrelated frameworks. Carrier cases appear across policy
analyzers, verifiers, stream callbacks, and breakpoint logic;
adapter cases appear across output rails, proxy guardrails,
and connector filters. This descriptive pattern illustrates
how the same dependency problem can arise at different
safety/frameworkinterfaces;itisnotapopulation-levelcon-
centration result.
The project concentration table gives a second check on
this interpretation. LiteLLM contributes the largest number
of cases, but those four cases exercise different boundaries:
proxy guardrail input construction, stream-derived tool evi-
dence, in-memory policy updates, and pass-through lifecy-
cle hooks. Promptfoo contributes verifier and tool-cap cases
rather than output-rail cases; NeMo contributes both out-
put mapping and multimodal prompt materialization. This
within-projectheterogeneityshowsthatthecuratedsetisnot
merely multiple instances of one subsystem-level repair.
The language split is also not the main claim, but it is
a useful guardrail against overfitting the taxonomy to one
implementation style. Python projects dominate the avail-
able LLM safety ecosystem, so Python cases are expected.
The curated examples also include TypeScript, Java, and
C#/.NET implementations, where safety logic likewise con-
sumes a structured representation whose shape or routing
differs across framework boundaries.
RQ3: How Far Do the Misses Reach?
Breadth alone does not establish safety impact. We next ask
how far each confirmed repair-boundary failure reaches into
the monitor stack: does it merely affect an observable trace
field, or does it reach a blocking, routing, filtering, or ver-
ifier decision? Table 4 separates E1 into operational forms
alongside the E2 and E3 boundaries.
Table 7 is not a second taxonomy. It summarizes the ob-
servable parent-to-fixed outcome shapes that appear across
the families above.
SeventeencasesareTierAconfirmationsoverframework-
or module-level boundaries; one isolates the changed
logic. Fourteen reach E1 enforcement: five block-
ing/filtering/rewriting surfaces, three interrupt or HITL
routes, and six hook/cap/policy-state boundaries. They span
fourfamilies,tenframeworkprojectgroups,andfourimple-
mentation ecosystems, with seven native actions, six config-
ured boundaries, and one synthetic-consumer consequence.
Thus E1 captures operational decisions—not merely inter-
nal trace differences—that the parent misses and the fixed
versionrestores. AppendixTable 11gives theper-case7/6/1
mapping.
Operationally, the blocking/filtering/rewriting cases per-
mitoremitcontentthatthefixedversionstopsortransforms;
interrupt/HITL cases continue tool execution past a config-
ured stop point; and hook/cap/policy-state cases fail to in-
voke, bind, or refresh an existing enforcement mechanism.
These distinct outcomes share one structure: the framework
continues while the configured policy boundary misses the
decision restored by the fixed revision.
E2 cases show verifier or safety-prompt inputs losing ev-
idence that downstream evaluation relies on, while E3 cap-
turesstructuredevidencevisibilityatanobservabilitybound-
ary. Reporting these strata separately keeps the operational
action results distinct from evidence-channel results.
Table 7 summarizes the reproduced contrasts. In the par-
ent,evidenceisabsent,stranded,misrouted,orevaluatedun-

Table 7: Before/after outcome patterns observed in the re-
produced cases.
Outcome Evidence Decision Repair
Evidence invisible absent none restore carrier
Enforcement skipped visible none restore adapter
Wrong authority stale wrong select channel
Policy state stale stale stale rebind rule
Table 8: Validation checks for the confirmation rule and
canary-contract schema.
Validation check Reviewed Result Contribution
High-signal de-
nominator
195 refs 9 newly pro-
moted
candidate ex-
pansion
Random merged
PR batch
55 PRs none con-
firmed
random-
batch control
Held-out high-risk
audit
8 candidates none con-
firmed
conservative
promotion
Reviewed nega-
tives
13 candi-
dates
excluded boundary
discipline
Known-pattern
fixtures
14 fixtures 14 contracts contract ex-
pressiveness
Rejectedboundary
cases
3 cases excluded exclusion
consistency
Mixed-candidate
audit
21 candi-
dates
18 / 3 split rule stability
derstalepolicystate;inthefixedrevision,thecanaryreaches
theexpectedfieldand,whereapplicable,theintendedaction
fires.
RQ4: How Does the Protocol Validate Confirmed
Cases?
Weevaluatetheconfirmationrulewithcandidateaudits,neg-
ative controls, known-pattern fixtures, a runnable diagnostic
comparison, and a frozen prospective pass.
The 195-reference audit expands the candidate pool, the
mixedauditreproducesthe18/3boundarysplit,andtheneg-
ative controls exclude adjacent changes. Known-pattern fix-
tures independently express all four family schemas with
visibility and decision metadata.
Across five representative cases—Invariant, NeMo regex
output mapping, CrewAI, Haystack, and LangChain stream
redaction—ordinary functional checks pass without the ca-
naryoracle.VisibilityaloneisinsufficientfortheNeMoand
Haystack adapter/decision misses; partial oracles also fail to
record the fixed repair. The full contract combines changed-
surface placement and parent/fixed visibility with decision
assertions at action boundaries. Appendix Table 10 reports
the case-level comparison; the artifact includes its machine-
readable records.
We also froze a follow-up audit rule before reviewing re-
centchanges.Afirstpassover300recentclosedpullrequests,
186merged,produced27term-matchedcandidates.Ofthese,
23 were excluded, three remained under reproduction, and
one additional repair-boundary case was confirmed outside
the retrospective 18-case corpus.
Related Work
Guardrailsandagentsafety.Guardrailandred-teamingwork
evaluatesdetectiononceevidencereachesanexpectedinter-
face (Wei, Haghtalab, and Steinhardt 2023; Mazeika et al.
2024; Inan et al. 2023; Han et al. 2024); agent studies ex-
pand that interface to actions, traces, tool calls, streams, ar-
tifacts, and provider schemas (Yao et al. 2022; Schick et al.
2023; Qin et al. 2023; Zhan et al. 2024; Debenedetti et al.
2024; Andriushchenko et al. 2024). We instead ask whether
a supported framework representation leaves evidence out-
side the monitor’s view or strands a positive result before
action,evenwhilethepathremainsoperational.Thedistinc-
tion is operational: model-centric evaluation asks whether a
model or detector recognizes a payload once it is presented
through the chosen interface. A framework-validity check
asks whether the exercised representation reaches that in-
terface and whether a positive result reaches the intended
action. The two can diverge: recognition can succeed while
an adapter, stream normalizer, or authority choice prevents
enforcement.
Runtimemonitoringandsoftwareevolution.Runtimever-
ification studies enforcement, API evolution studies client
breakage, and differential or metamorphic testing compares
related executions (Leucker and Schallhart 2009; Falcone,
Fernandez, and Mounier 2012; Dig and Johnson 2006;
Rothermel and Harrold 1997; McKeeman 1998; Chen et al.
2018); ML systems work documents hidden interface cou-
pling (Sculley et al. 2015; Breck et al. 2017; Amershi et al.
2019).CanarycontractsspecializetheseideastoLLMsafety
withthreeconstraints:apolicy-intentanchor,payloadplace-
ment only on the changed framework surface, and separate
visibilityandenforcementoracles.Togethertheydistinguish
an evidence-path failure from an arbitrary revision differ-
ence. Runtime verification supplies enforcement semantics,
software-evolutiontestingsuppliestheparent/fixedcontrast,
andML-systemsworkmotivatesscrutinyofhiddencoupling.
Canarycontractsjointhosepiecesatthechangedrepresenta-
tion, making evidence placement and action routing explicit
rather than treating every behavioral difference as equally
relevant.
Our unit is the policy-linked evidence path through a
framework boundary, enabling deterministic oracles across
schemas, streams, adapters, authority channels, and policy-
state updates.
Conclusion
Monitor-validity failure is a framework-interface failure: an
operational path fails to carry evidence or a positive detec-
tor result to its policy boundary. Across 18 confirmed cases
and11frameworkprojectgroups,thepatternrecursincarri-
ers,adapters,authoritychannels,andnewsurfaces;14cases
reachE1enforcementboundaries.Canarycontractsexposeit
bycombiningchanged-surfacepayloadplacement,visibility
evidence,andaction-boundarydecisionchecksacrossparent
and fixed revisions, turning hidden safety assumptions into
explicit contracts for schemas, streams, tools, adapters, and
policy-update paths in evolving LLM and agent infrastruc-
ture.

References
Amershi, S.; Begel, A.; Bird, C.; DeLine, R.; Gall, H.; Ka-
mar,E.;Nagappan,N.;Nushi,B.;andZimmermann,T.2019.
Software engineering for machine learning: A case study.
In2019 IEEE/ACM 41st International Conference on Soft-
ware Engineering: Software Engineering in Practice (ICSE-
SEIP), 291–300. IEEE.
Andriushchenko, M.; Souly, A.; Dziemian, M.; Duenas, D.;
Lin, M.; Wang, J.; Hendrycks, D.; Zou, A.; Kolter, Z.;
Fredrikson, M.; et al. 2024. Agentharm: A benchmark
for measuring harmfulness of llm agents.arXiv preprint
arXiv:2410.09024.
Breck, E.; Cai, S.; Nielsen, E.; Salib, M.; and Sculley, D.
2017. TheMLtestscore:ArubricforMLproductionreadi-
ness and technical debt reduction. In2017 IEEE interna-
tional conference on big data (big data), 1123–1132. IEEE.
Chen,T.Y.;Kuo,F.-C.;Liu,H.;Poon,P.-L.;Towey,D.;Tse,
T.; and Zhou, Z. Q. 2018. Metamorphic testing: A review
of challenges and opportunities.ACM Computing Surveys
(CSUR), 51(1): 1–27.
Debenedetti, E.; Zhang, J.; Balunovic, M.; Beurer-Kellner,
L.; Fischer, M.; and Tramèr, F. 2024. Agentdojo: A dy-
namic environment to evaluate prompt injection attacks and
defenses for llm agents.Advances in Neural Information
Processing Systems, 37: 82895–82920.
Dig, D.; and Johnson, R. 2006. How do APIs evolve? A
story of refactoring.Journal of software maintenance and
evolution: Research and Practice, 18(2): 83–107.
Falcone, Y.; Fernandez, J.-C.; and Mounier, L. 2012. What
canyouverifyandenforceatruntime?International Journal
on Software Tools for Technology Transfer, 14(3): 349–382.
Han,S.;Rao,K.;Ettinger,A.;Jiang,L.;Lin,B.Y.;Lambert,
N.; Choi, Y.; and Dziri, N. 2024. Wildguard: Open one-stop
moderation tools for safety risks, jailbreaks, and refusals of
llms.Advances in neural information processing systems,
37: 8093–8131.
Inan, H.; Upasani, K.; Chi, J.; Rungta, R.; Iyer, K.; Mao,
Y.; Tontchev, M.; Hu, Q.; Fuller, B.; Testuggine, D.; et al.
2023. Llama guard: Llm-based input-output safeguard for
human-ai conversations.arXiv preprint arXiv:2312.06674.
Leucker, M.; and Schallhart, C. 2009. A brief account of
runtime verification.The journal of logic and algebraic
programming, 78(5): 293–303.
Mazeika, M.; Phan, L.; Yin, X.; Zou, A.; Wang, Z.; Mu,
N.; Sakhaee, E.; Li, N.; Basart, S.; Li, B.; et al. 2024.
Harmbench: A standardized evaluation framework for au-
tomated red teaming and robust refusal.arXiv preprint
arXiv:2402.04249.
McKeeman, W. M. 1998. Differential testing for software.
Digital Technical Journal, 10(1): 100–107.
Qin, Y.; Liang, S.; Ye, Y.; Zhu, K.; Yan, L.; Lu, Y.; Lin, Y.;
Cong,X.;Tang,X.; Qian,B.;etal.2023. Toolllm:Facilitat-
inglargelanguagemodelstomaster16000+real-worldapis.
InInternational Conference on Learning Representations,
volume 2024, 9695–9717.
Rothermel, G.; and Harrold, M. J. 1997. A safe, efficient re-
gressiontestselectiontechnique.ACM Transactions on Soft-
ware Engineering and Methodology (TOSEM), 6(2): 173–
210.
Schick, T.; Dwivedi-Yu, J.; Dessì, R.; Raileanu, R.; Lomeli,
M.;Hambro,E.;Zettlemoyer,L.;Cancedda,N.;andScialom,
T.2023. Toolformer:Languagemodelscanteachthemselves
to use tools.Advances in neural information processing
systems, 36: 68539–68551.
Sculley, D.; Holt, G.; Golovin, D.; Davydov, E.; Phillips, T.;
Ebner,D.;Chaudhary,V.;Young,M.;Crespo,J.-F.;andDen-
nison, D. 2015. Hidden technical debt in machine learning
systems.Advances in neural information processing systems,
28.
Wang, H.; Poskitt, C. M.; and Sun, J. 2025. Agentspec:
Customizable runtime enforcement for safe and reliable llm
agents.arXiv preprint arXiv:2503.18666.
Wei, A.; Haghtalab, N.; and Steinhardt, J. 2023. Jailbro-
ken: How does llm safety training fail?Advances in neural
information processing systems, 36: 80079–80110.
Yao,S.;Zhao,J.;Yu,D.;Du,N.;Shafran,I.;Narasimhan,K.;
and Cao, Y. 2022. React: Synergizing reasoning and acting
in language models.arXiv preprint arXiv:2210.03629.
Zhan,Q.;Liang,Z.;Ying,Z.;andKang,D.2024.Injecagent:
Benchmarking indirect prompt injections in tool-integrated
large language model agents. InFindings of the Association
for Computational Linguistics: ACL 2024, 10471–10506.
