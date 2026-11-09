---
title: 'Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy Changes'
url: https://arxiv.org/abs/2609.29952
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Rahul Khedar
- Mayank Malhotra
- Avinash Karn
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.29952
pages: 19
chars: 79539
fetched_at: '2026-11-08T13:24:54+00:00'
kb_version: 1
---

# Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy Changes

Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product
and Policy Changes
Rahul Khedar Mayank Malhotra Avinash Karn
PayPal AI
Abstract
Before a product or policy change ships, the question that
matters is how people will react to it. Augur rehearses that
reaction offline: it builds a typed knowledge graph from the
change documents, populates a grounded persona market,
simulates the interaction, and returns an auditable decision
memorecommendingoneoffiveactions. WeassembleGold-
50, fifty real product and policy episodes whose real-world
outcome is known, adjudicated against the public record, and
score the five-way release verdict against it.
Our central finding is methodological and negative: most
ofthemeasuredgapbetweenfrontiercloudmodelsandopen-
weightmodelswefine-tuneandserveofflineisattributableto
an under-specified evaluation, not a difference in capability.
We show this three ways. First, the prompt envelope alone
can dominate the score: holding weights, cases and scorer
fixed, one system—a LoRA-SFT adapter on Qwen3-32B—
swingsfrom 0%to 73%. Second,inamatched 2×2 ablation,
definingthedecisiontaxonomyintheprompt—withnomodel
change—lifts every frontier model by+24to+34pp; under
the under-specified prompt, Qwen3-32B LoRA-SFT served
offlinebeatsall three frontier models (paired McNemar,
Holm-corrected), and once the prompt is fair no significant
difference from any of them is detected. Third, agreement
with the distillation teacher rises without accuracy following,
and the full pipeline amplifies a systematic “over-doom” bias
rather than improving the verdict. Separately, we validate
the reaction layer on its own terms: blind judges across four
modelfamiliesfindthesyntheticreactionrecovers 67–90%of
the concerns the public actually raised, and a pre-registered
ablation locates its value—largest where the decision is
hardest,redundantnearceiling. Thepipelinethatregenerates
every number and figure here is available from the authors.
1 Introduction
Organizations decide whether to ship changes—a pricing
update,apolicyrevision,afeaturelaunch—underuncertainty
about how the people affected will react. The evidence they
would most like to have, the reaction itself, does not exist
until after the decision is made. Augur is a system for manu-
facturing a usable proxy for that evidencebeforethe fact: it
reads the documents that define a change, constructs a mar-
ket of stakeholders grounded in those documents, simulates
their interaction [1, 2], and returns a decision memo that
recommends one of five release actions and shows its work.
Asystemlikethisisonlyastrustworthyasthemeasurement
used to judge it, and this is where the paper concentrates its
effort. It is easy to run a fleet of models through a decision
harness, read off a leaderboard, and conclude that frontier
cloud models are far ahead of anything one can fine-tune and
serve offline. We built that leaderboard, and then spent most
of our effort showing that the conclusion it invites is largely
an artifact ofhowthe models were asked, not of what they
can do.
Aim.Our goal is to establish, on a benchmark of real
decisions with verified outcomes, how much of the frontier-
versus-offlinegaponthistaskisrealcapabilityandhowmuch
is measurement, and to give a mechanism for the difference.
The answer,on these fifty cases, is that the gap is mostly
measurement: once the decision taxonomy is defined in
the prompt for everyone, a Qwen3-32B open-weight model
served offline shows no statistically significant difference
from the frontier models tested.
Contributions.
1. Gold-50, a benchmark of 50 real product and policy
episodes with manually verified real-world outcomes,
balanced ten per class across a five-way action taxonomy,
together with the Augur system that produces auditable
verdicts on it (Sections 2 and 3).
2. The prompt envelope can dominate the result.With
weights, cases and scoring code held fixed, changing only
the prompt moves one system—the deployed Qwen3-32B
LoRA-SFT (sft_v3)—from 0% to 73% (Section 5.2).
Anysingle-promptcomparisonofthistaskisthereforeun-
interpretable,andwereportthecomplianceratealongside
every accuracy.
3. A matched 2×2 ablation resolves most of the gap
(Section 5.3). On the same fifty report-stage contexts
through the same direct harness, appending a shared
taxonomy-definition block lifts every frontier model by
+24 to+34pp. Under the under-specified prompt the
offlineQwen3-32BLoRA-SFTsignificantlybeatsallthree
frontier models (Holm-corrected); under the fair prompt
1
arXiv:2609.29952v1  [cs.AI]  24 Sep 2026

no statistically significant difference from any of them is
detected. The mechanism differs by family, so the two
interventions are complementary rather than redundant.
4. Two failure modes with a formal account.Agreement
withthedistillationteacherclimbsfrom 10%to 70%across
fine-tuningroundswithnomatchingmovementinoutcome
accuracy (Section 5.7), and the full five-stage pipeline
amplifies an over-doom bias, scoring at or below the five-
way chance rate (Section 5.4). Section B proves why both
are expected: distillation collapses judge independence,
andanyexact-matchscorerimposesaschema-compliance
ceiling.
5. The reaction layer is faithful, and its value is located,
not flat.Blind judges across four model families find the
synthetic reaction anticipates67–90%of the concerns the
public actually raised (Section 5.5), and apre-registered
matched with/without-simulation ablation (Section 5.6)
shows the report-stage reaction signal helps most exactly
where the title-only baseline is weakest (+20pp for the
weakest solver) and is redundant near ceiling—so the
over-doom of the previous point is a property ofstacking
the generative stages, not of the reaction evidence itself.
6. Areproducibleartifact-to-PDFpipeline.Everynumber,
table cell and plotted mark in this paper is generated from
therunartifactsandthenre-assertedagainstthem;nothing
is transcribed by hand (Section 8).
2 The Augur System
Augur factors adecision into fivesingle-responsibility stages,
each of which reads the artifacts of the stages before it and
writes its own. The forward path isdocuments→graph→
personas→simulation→report , and a fifth interaction
stagesupportspost-hocinterrogationofanypersona. Figure1
shows the flow; Section A gives the formal operators, and we
summarize them here.
Stages.Graphbuildinfersatypedontologyfromthechange
documentsandextractsadirectedknowledgegraphofentities
and relations.Environmentsynthesizes a persona popula-
tion grounded in that graph—each persona references graph
entities, so the market is specific to the change rather than
a generic crowd.Simulationruns the personas for several
rounds on an OASIS-style engine [3], producing a timeline
ofposts,repliesandreactionswithpeer-influencedsentiment.
Reportretrieves graph-expanded evidence [7, 8], writes a
forecast, and emits the recommended action𝑎★ from the
five-way taxonomy
A={ship,revise,delay,segment,mitigate}.
Between stages, three pure-code auditors read the finished
transcript and can each buy at most one corrective round
under a global budget, and a cross-family critic gates the
verdict.
Engineered independence.Agents never call one another;
eachreadspersistedartifactsandwritesitsown,andaderived-
from dependency directed acyclic graph (DAG) makes re-
generation of any artifact cascade to everything downstream
(Section A). The ensemble that produces the verdict is drawn
cross-family: the critic and cross-check come from a model
family other than the report author’s [9]. Section B explains
why this matters—same-family voting forfeits most of the
amplification an ensemble can provide, and it is exactly the
propertythatdistillationdestroys. Figure2 shows thelayered
structure that enforces this: every agent reaches the rest of
the system only through an abstracted storage interface and
a single OpenAI-compatible model boundary, so the graph
store(Neo4jtoday)andthemodelbackend(ahostedgateway
oralocalruntime)arebothswappablewithouttouchingagent
code—the property that makes the fully offline deployment
of Section 2 a configuration change rather than a rewrite.
Offlinedeployment.Thesystemisdesignedtorunwithout
a cloud dependency. We fine-tune the generation stages with
low-rank adaptation (LoRA) [13] on distilled traces [10, 11]
and serve them on a single accelerator; the untuned cross-
family critic is kept off-the-shelf so that its errors are not the
generator’serrors. Trainingdetails,adaptersandservingcost
are in Section D.
3 The Gold-50 Benchmark
Judging a decision system requires cases whoserealized
outcome is known. Gold-50 is fifty real product and policy
episodes—each a change that a real organization actually
made—for which the real-world outcome was later observed
and can be mapped onto the five-way action taxonomy. Each
label records therealized dispositionof the episode (what
actually happened), not an abstract “optimal action.” Every
one of the50labels was adjudicated in a single author pass
against the public record, assisted by Claude Opus 4.8 (adju-
dicationrun2026-09-06),withamedianofthreeindependent
sources per case. Because Claude Opus 4.8 also appears as
oneof thebenchmarkedfrontier models, itsadjudication role
is a potential source of circularity in the frontier-model com-
parison; we disclose it here and read the Opus 4.8 Gold-50
numbers with that caveat. The labeling convention for each
of the five classes is given in Table 8, and the full per-case
ledger—label, outcome driver, year and source count—is
in Table 9. Each case is annotated with the mechanism
that actually decided its outcome, so that accuracy can be
stratified bywhya decision went the way it did. Because
the labels are a single-pass author adjudication rather than
a multi-annotator consensus, we treat Gold-50 as an author-
adjudicated retrospective benchmark and scope every claim
to it.
Every system is shown only thepre-decisioninformation
for a case—the policy or product document as it stood before
theoutcomewasknown. Therealizedoutcome,theoutcome-
2

Documents
PDF·MD·text
Graph Build
𝐺(𝐷) : ontol-
ogy + entities
Environment
𝑃(𝐺,𝑞) : per-
sonas + stance
Simulation
𝑆: OASIS rounds
Report
𝑅: evidence
+ forecast𝐹
𝑎★
Decision
1 2 3 4
5 Interaction
interview any persona·ask “why did you react?”·re-run
Figure 1.The Augur pipeline; symbols are the operators of Equation (2). Each forward stage persists an inspectable artifact; the interaction
stage feeds findings back into the graph or report.
Flask + Jinja frontend
PRESENTATION
Graph
routes
Sim.
routes
Report
routes
API·ORCHESTRATOR
NER +
Ontology
OASIS
sim
Graph
memory
Graph
tools
SERVICES·AGENTS
GraphStorage
interface
Neo4j 5.18
swappable
STORAGE
Gateway /
Hosted
Local
runtime
LLM BOUNDARY
Figure 2.Layered architecture. A Flask/Jinja frontend drives an
API and orchestrator layer; the single-responsibility agents (named-
entity recognition [NER] and ontology, OASIS simulation, graph
memory, graph tools) sit below it and interact with the rest of the
system only through an abstractedGraphStorageinterface (Neo4j
today, swappable) and one OpenAI-compatible model boundary
(a hosted gateway or a local runtime). Nothing above the storage
or model boundary knows which backend is in use, which is what
makes the fully offline deployment of Section 2 a configuration
change.
driverannotationandthesourcelistareheldoutofthemodel
input entirely and are used only for scoring, so no system can
read the answer off its own prompt.
The set is balanced at ten cases per class across
{ship,revise,delay,segment,mitigate} , which fixes the
five-way chance rate at exactly20% and makes a raw accu-
racy directly comparable to it. The verification annotations
sort the cases into four outcome drivers: publicreaction(28
cases),regulatoryaction( 11),engineeringreadiness( 7),and
businessperformance (4). The reaction stratum is both the
largest and the one the pipeline is architecturally aimed at,
and—as Section F shows—the one every system does worst
on, which is the honest limit of a reaction-simulating design.
Becausethetargetactionisparsedoutofastructuredfield,
we score two ways throughout: a conservative accuracy that
counts any unparseable output as wrong, and the accuracy
conditional on in-schema output, reported with its parsed
count. Section B makes precise why both are necessary.
4 Experimental Setup
Systems.We evaluate eleven systems on the report stage:
three frontier cloud models (Claude Sonnet 5, Claude
Opus 4.8, GPT-5.2) and eight open-weight configurations
spanning 1.7B to32B parameters, both untuned bases and
their adapters from LoRA supervised fine-tuning (SFT), plus
one variant extended with direct preference optimization
(DPO), the SFT→DPO configuration [14]. The base back-
bones are Qwen3-1.7B, Qwen3-8B and Qwen3-32B [21],
Llama-3-8B-Instruct [22] and Gemma-3-27B-it [23]; each
named result below identifies its exact configuration, and
Table 1 lists all eleven. The deployed open checkpoint
is a LoRA-SFT adapter on Qwen3-32B (sft_v3), and its
preference-tuned sibling is Qwen3-32B SFT→DPO (dpo);
their lineage and hyperparameters are in Section D.
Harness and prompt arms.Every comparison in this
paper holds the fifty cases and the scoring code fixed and
varies only the model and the prompt. Thedeployedreport-
stage prompt is the one the application serves. Thedebias
arm appends a single shared block that defines each of the
fiveactionsanddiscourageshedging. Theabstractarm,used
only as a schema-compliance probe (Section 5.2), asks for a
verdictthroughagenericinstructionprompt. Noarmchanges
model weights.
Statistics.Wilson score intervals give the 95%confidence
band on each accuracy [17]; at𝑛=50 these are wide and
overlap for most pairs, so we do not compare systems by
eyeballing intervals. Because every system sees thesame
cases, the correct paired test is the two-sided exact McNemar
3

test on the discordant pairs [18], which we use for every
head-to-head claim. Where a claim rests on a family of
paired tests—the leader-versus-frontier comparisons under
eachpromptarm,andthefine-tuningdeltas—wereportHolm-
corrected and Benjamini-Hochberg-corrected𝑝-values [19,
20] alongside the raw ones; our primary hypothesis family
is the leader-versus-frontier comparison under the shared-
taxonomy (debias) prompt. A non-significant McNemar
resultat 𝑛=50isafailuretodetectadifference,notevidenceof
equivalence: thesampleistoosmalltosupportanequivalence
test, and we never read “no significant difference” as “the
same.” Class-level performance is summarized by macro-F1.
Data hygiene.Gold-50 is an evaluation-only set and is
disjoint from everything used to build the open checkpoints.
Thefine-tuningcorpusissyntheticpersona-generationtraces;
it shares no case identifier with Gold-50 (0overlapping ids),
no case document matches any training document, and the
strongest cross-set link we find is a single shared company
nameinatmostonecase—consistentwithtwoindependently
constructed corpora that happen to mention the same well-
known organization. The audit is recomputed from the raw
splits by the metrics pipeline and reported in Section E; no
Gold-50 case was used for SFT, DPO, validation or model
selection.
5 Results
5.1 The report-stage leaderboard
Table 1 and fig. 3 give the report-stage leaderboard under
the deployed prompt. The deployed Qwen3-32B LoRA-
SFT (sft_v3) leads at31/50=62.0% (Wilson[48.2,74.1] ,
macro-F1 0.59);theQwen3-32BSFT →DPOvariantmatches
it, and the untuned Qwen3-8B base reaches54.0%. At the
bottom, the Qwen3-1.7B LoRA-SFT adapter collapses to
6.0% with 35/50unparseableoutputs—acompliancefailure,
not a judgment failure, and a first concrete instance of the
ceiling of Section B.
The Wilson intervals overlap for nearly every pair, so we
decide separation with the paired test. Exactly three systems
are separated from the leader (the Qwen3-32B LoRA-SFT)
at𝛼=0.05: the Qwen3-1.7B LoRA-SFT, the Llama-3-8B-
Instructbase,andtheGemma-3-27B-itbase;thesecond-place
Qwen3-32B SFT→DPO variant shows zero discordant pairs
withtheleader,andthe 60%Llama-3-8BLoRA-SFTadapter
shows no significant difference from it. In other words, the
top of the leaderboard is a cluster, not a ranking, at this
sample size.
Fine-tuning is not uniformly beneficial.Applying one
recipe and one dataset to five backbones (Table 2 and fig. 4)
produces effects that range from decisive to destructive:
+44pp on Llama-3-8B (𝑝=3.0×10 −6) and−40pp on
Qwen3-1.7B(𝑝=1.1×10 −5),withthethreemid-sizeeffects
Table 1. Gold-50 leaderboard, report stage.Five-way release
verdict against the verified real-world outcome,𝑛=50, ten cases
per class, five-way chance20%. “Acc” scores unparseable output
as wrong (the conservative choice); “in-sch.” is the accuracy
conditionalonin-schemaoutput, Pr[ˆ𝑎=𝑎★|ˆ𝑎∈A] ,withitsparsed
count in parentheses;∅ is the unparseable count. CI is the 95%
Wilson score interval. Generated from the computed metrics.
System Acc 95% CI in-sch. macro-F1∅
Qwen3-32B + LoRA-SFT•62[48.2,74.1]62(50)0.59 –
Qwen3-32B + SFT→DPO◦62[48.2,74.1]62(50)0.59 –
Llama-3-8B + LoRA-SFT•60[46.2,72.4]61.2(49)0.58 1
Qwen3-32B 56[42.3,68.8]56(50)0.56 –
Qwen3-8B 54[40.4,67]54(50)0.52 –
Qwen3-8B + LoRA-SFT•50[36.6,63.4]56.8(44)0.51 6
Gemma-3-27B + LoRA-SFT•50[36.6,63.4]50(50)0.44 –
Qwen3-1.7B 46[33,59.6]46(50)0.39 –
Gemma-3-27B-it 36[24.1,49.9]36(50)0.34 –
Llama-3-8B-Instruct 16[8.3,28.5]16(50)0.16 –
Qwen3-1.7B + LoRA-SFT•6[2.1,16.2]20(15)0.07 35
•LoRA-SFT◦SFT→DPO (unmarked) untuned base.
0 20 40 60 80 100
Qwen3-1.7B + LoRA-SFT
Llama-3-8B-Instruct
Gemma-3-27B-it
Qwen3-1.7B
Qwen3-8B + LoRA-SFT
Gemma-3-27B + LoRA-SFT
Qwen3-8B
Qwen3-32B
Llama-3-8B + LoRA-SFT
Qwen3-32B + SFT→DPO
Qwen3-32B + LoRA-SFT
chance=20%
6
16
36
46
50
50
54
56
60
62
62
accuracy vs. verified outcome (%)
Figure 3. Gold-50 leaderboard.Accuracy of the five-way release
verdict against theverifiedreal-world outcome on𝑛=50 cases,
balanced at 10 per class, all 50/50 labels manually re-verified (sec-
tion 3). Bars are teal for LoRA-SFT adapters, green for SFT→DPO
andgreyforuntunedbases;whiskersare95%Wilsonscoreintervals,
which are wide at this𝑛 and overlap for most pairs — hence the
pairedMcNemartestsintable2, whichconditiononthesamecases.
Unparseable outputs are scored as wrong, the conservative choice;
table 1 also reports the accuracy conditional on in-schema output.
4

Table 2. Paired base→LoRA-SFT effect, one recipe and one
dataset,eachbackbonescoredbeforeandafteronthesame50cases.
Δispercentagepoints;“fix/broke”arethediscordantMcNemarcells
(cases the adapter got right and the base wrong, and the reverse);𝑝
is the two-sided exact McNemar test, starred at𝛼=0.05. Generated
from the computed metrics.
Backbone Base+SFTΔpp fix/broke𝑝
Qwen3-1.7B 46 6 -40 1/21 1.1e-5 ∗
Llama-3-8B-Instruct 16 60 +44 23/1 3.0e-6 ∗
Qwen3-8B 54 50 -4 8/10 0.815
Gemma-3-27B-it 36 50 +14 15/8 0.210
Qwen3-32B 56 62 +6 9/6 0.607
Qwen3-1.7B
Llama-3-8B-Instruct
Qwen3-8BGemma-3-27B-it Qwen3-32B
0
20
40
60
80
𝑝<0.001
-40pp
𝑝<0.001
+44pp
𝑝=0.81
-4pp
𝑝=0.21
+14pp
𝑝=0.61
+6pp
46
16
54
36
56
6
60
50 50
62
Gold-50 accuracy (%)
untuned base + LoRA-SFT
Figure 4. The same fine-tune helps or destroys, depending on
the backbone.Each pair is one backbone evaluated before and
after LoRA-SFT onidenticaldata, recipe, seed and prompts, scored
on thesame50 cases;𝑝 is a two-sided exact McNemar test on the
discordant pairs (table 2), which is the correct test here because the
two systems see the same items. The effect ranges from+44pp
(Llama-3-8B)to−40pp(Qwen3-1.7B),andonlythosetwoextremes
are significant — the three mid-size gains are not distinguishable
fromnoiseat 𝑛=50 . Dashedlineisthe 20%five-waychancelevel.
not significantly different from noise at𝑛=50. The gain
on Llama-3-8B comes from the SFT fixing23 cases while
breaking 1; the collapse on the smallest backbone, Qwen3-
1.7B, is the mirror image, breaking21 while fixing 1, as
the adapter degrades the model’s already-fragile schema
compliance.
5.2 The prompt envelope can dominate the
result
Before comparing systems, we have to establish how much
of a measured difference is judgment and how much is the
harness. Figure 5 answers this on an answer-keyed subset:
the same weights and the same cases, scored the same way,
under two prompts. Through the deployed report-stage
prompt the three checkpoints (Qwen3-32B base, Qwen3-
8B LoRA-SFT, and the deployed Qwen3-32B LoRA-SFT)
score 54.5–72.7%; through a generic abstract prompt the
same weights emit actions outside the five-way schema and
accuracy collapses. The fine-tuned Qwen3-32B LoRA-SFT
Qwen3-32B base Qwen3-8B+SFT Qwen3-32B+SFT
0
20
40
60
80
18
9
0
55
64
73
accuracy on the same 11 cases (%)
abstract instruction prompt
deployed report-stage prompt
Figure 5. The evaluation harness can dominate the measure-
ment.The same three checkpoints, the same 11 answer-keyed
cases, the same scoring code — only the prompt envelope differs.
Asked for a verdict through a generic instruction prompt, the mod-
els emit actions outside the five-way schema (delay_release,
proceed_with_mitigations, rollback) and accuracy col-
lapses; asked through the exact report-stage prompt the app deploys,
the same weights score 54.5–72.7%. The fine-tuned Qwen3-32B
LoRA-SFT (sft_v3) is themostharness-sensitive of the three,
because SFT bound its output format tightly to the serving prompt:
it is worst under the abstract prompt and best under the deployed
one. We therefore report all headline numbers under the deployed
promptandtreattheabstractharnessasaschema-complianceprobe,
not a judgment measurement.
isthemostharness-sensitiveofthethree,becauseSFTbound
its output format tightly to the serving prompt: it is the worst
under the abstract prompt and the best under the deployed
one, swinging from0%to73%.
This is not a curiosity—it is the reason a single-prompt
leaderboard on this task cannot be trusted [15, 16], and it
motivates the matched ablation of Section 5.3. We therefore
report all headline numbers under the deployed prompt and
treattheabstractpromptasaschema-complianceproberather
than a judgment measurement.
5.3 The debias 2×2: most of the gap is the
prompt
The cleanest test of the paper’s thesis puts frontier and
open-weight models on identical footing: thesamefifty
report-stage contexts, thesamedirect harness, and a single
binaryintervention—whetherthesharedtaxonomy-definition
block is appended. Figure 6 and Table 10 give the full grid;
Table 3 settles the head-to-head with the paired test.
Defining the taxonomy, withno model change, lifts every
frontier model by+24 to+34pp, and every frontier gain
is significant at𝑝 <0.01: Sonnet 546→80% , Opus 4.8
44→68% , GPT-5.238→66% . The offline Qwen3-32B
LoRA-SFT moves62→78% and its DPO variant (Qwen3-
32B SFT→DPO) 62→76% . The low frontier scores under
the deployed prompt were therefore largely a prompt artifact,
not a capability gap.
The head-to-head makes the consequence precise. Un-
der the under-specified baseline prompt the offline Qwen3-
32B LoRA-SFT significantlybeatsall three frontier models
5

0 20 40 60 80 100
Qwen3-1.7B + LoRA-SFT
Llama-3-8B-Instruct
Qwen3-8B
Qwen3-8B + LoRA-SFT
Gemma-3-27B-it
Qwen3-1.7B
Gemma-3-27B + LoRA-SFT
Qwen3-32B
GPT-5.2
Claude Opus 4.8
Llama-3-8B + LoRA-SFT
Qwen3-32B + SFT→DPO
Qwen3-32B + LoRA-SFT
Claude Sonnet 5
chance=20%
24 (+18∗)
36 (+20∗)
40 (-14)
44 (-6)
44 (+8)
48 (+2)
50 (+0)
58 (+2)
66 (+28∗)
68 (+24∗)
68 (+8)
76 (+14∗)
78 (+16∗)
80 (+34∗)
accuracy vs. verified real-world outcome (%)
baseline prompt
+debias block
Figure 6. The debias 2×2: one prompt block, no model change, closes most of the frontier gap.Every bar is the same open-weight or
frontier model on thesame50 frozen report-stage contexts through thesamedirect harness (table 10); grey is the deployed report prompt,
teal appends the shared taxonomy-definition+ anti-hedge block. Whiskers are 95% Wilson intervals on the debias arm; the trailing number
is that accuracy and, in parentheses, the baseline→debias change, starred when the paired McNemar test is significant at𝛼=0.05. Defining
the taxonomy lifts every frontier model by+24 to+34pp and unwinds the mitigate-collapse (fig. 7). The Qwen3-32B LoRA-SFT (sft_v3,
78%) lands among the frontier: it shows no statistically significant difference from Sonnet (80%, 𝑝=1.000), Opus (68%, 𝑝=0.227) and
GPT-5.2 (66%,𝑝=0.180) once the prompt is fair, havingbeatenall three when it is not (table 3).
(𝑝=0.039/0.012/0.002 ; all significant after Holm cor-
rection, Table 3), winning10–13 discordant cases against
1–2. Once the taxonomy is defined for everyone, no statisti-
cally significant difference from any of the three is detected
(𝑝=1.000/0.227/0.180 ; Holm-corrected in Table 3) — a
failure to detect a difference at𝑛=50, not evidence of equiva-
lence. TheQwen3-32BLoRA-SFTservedofflinethusshows
no significant difference from the frontier when the prompt
is fair and wins whenever it is not.
Themechanismdiffersbyfamily.Thetwointerventions—
fine-tuning and the prompt block—are not redundant, be-
cause they fix different failures (Figure 7). For the frontier
models the block unwinds a genuinemitigate-collapse: over-
prediction ofmitigateagainst a true frequency of10/50 falls
sharply (Sonnet36→16 , Opus33→18 , GPT35→19 ).
The Qwen3-32B fine-tunes (sft_v3, dpo) never had that
collapse (sft_v314→16 ); their gain comes instead from
recoveringthesegmentclass,whichwasnearlyunreachableat
2/10recall and rises to8/10once the taxonomy names what
segmentmeans. Two distinct failures, two complementary
fixes.
5.4 The full pipeline amplifies over-doom
Adding the simulation stages ahead of the report does not
improvetheverdict;itmakesitworse. Figure8andtable4run
thecompletefive-stagepipelineoverthesamefiftydocuments
inthreeconfigurations: everystageonClaudeOpus4.8,every
stage on GPT-5.2, and the system’s defaultper-agentrouting
(auto), which assigns each stage the model best suited to
it—Sonnet 5 for the high-volume extraction and simulation
stages, Opus 4.8 for persona and report synthesis, and a
cross-family GPT-5.2 critic so the audit stays independent.
Opus scores40.0% and GPT36.0%—below every report-
only system above eighth place—and the default per-agent
auto configuration scores14.0%,belowthe 20% five-way
chance rate. The mechanism is a systematic over-doom bias:
the full pipeline answersmitigateon68%, 80%and 62%of
casesagainstatruefrequencyof 20%,andtheGPTrunnever
once recommendsship.
This comparison is confounded by model family (the
6

Table 3. Does the open fine-tune beat the frontier? A paired question.Qwen3-32B + LoRA-SFT (sft_v3) against each frontier model
on thesame50 cases, so the correct test is a two-sided exact McNemar on the discordant pairs, not a difference of accuracies — the Wilson
intervalsoverlapineverypair. Thisisthepaper’sprimaryhypothesisfamily; 𝑝Holm istheHolm-correctedvalueacrossthethreecomparisons
within each arm. Under the under-specified baseline prompt the Qwen3-32B LoRA-SFT wins all three, significant after correction; once the
taxonomy is defined no significant difference from any frontier model is detected (“n.s.”), which is a failure to detect a difference at𝑛=50,
not evidence of equivalence. Generated from the computed metrics.
Arm vs. frontier Acc (ft/cloud) Wins (ft–cloud)𝑝 𝑝 Holm
Baseline
Claude Sonnet 5 62/46 10–2 0.039 0.039 (beats)
Claude Opus 4.8 62/44 10–1 0.012 0.023 (beats)
GPT-5.2 62/38 13–1 0.002 0.005 (beats)
Debias
Claude Sonnet 5 78/80 4–5 1.000 1.000 (n.s.)
Claude Opus 4.8 78/68 8–3 0.227 0.539 (n.s.)
GPT-5.2 78/66 10–4 0.180 0.539 (n.s.)
baseline debias
Claude Sonnet 5
Claude Opus 4.8
GPT-5.2
Qwen3-32B + LoRA-SFT
Qwen3-32B + SFT→DPO
36 16
33 18
35 19
14 16
14 18
(a)mitigatepreds
baseline debias
1 10
1 7
1 6
2 8
2 7
(b)segmentrecall
Figure 7. What the block changes.For the five capable systems,
baseline vs debias. (a) The over-prediction ofmitigateagainst a
true frequency of 10/50 collapses for the frontier models (Sonnet
36→16, Opus33→18, GPT35→19); the fine-tunes never had it
(sft_v314→16),sotheirgaincomeselsewhere. (b)Itcomesfrom
segment: theclassthatwasnearlyunreachable( 1–2/10)isrecovered
to 6–10/10 once the taxonomy names whatsegmentmeans. Fine-
tuning and the prompt block therefore fix overlapping but distinct
failures — table 10 gives all fourteen systems.
Table 4.The Gold-50 set through thecompletefive-stage pipeline
underfrontiermodels,tobereadagainstthereport-stage-onlyresults
of table 1. Accuracy is reported once a run covers all 50 cases.
Mitigateshare is given because it is the diagnostic (fig. 8); the true
frequency is20%. Latency is the median per case, end to end over
all five stages. Regenerated from the run outputs on every build, so
the counts are current as of this document.
Config. Cases Medianmitig.Acc(95% CI)
/50 s/case
Claude Opus 4.8 50 162 68%40[27.6,53.8]
GPT-5.2 50 150 80%36[24.1,49.9]
Per-agentauto50 422 62%14[7.0,26.2]
best report-only50 — 28%62.0[48.2,74.1]
0
20
40
60
80
chance 20%
40 36
14
50 56 62
%
(a) Accuracy vs verified outcome
Opus 4.8 GPT-5.2 Per-agent auto Gemma+SFT Qwen3-32BQwen3-32B+SFT
0
20
40
60
80
100
true frequency 20%
68
80
62 64
32 28
% of cases
(b) Share of cases answeredmitigate
Figure 8. Adding the simulation stages amplifies over-doom
and does not improve the verdict. Orange: frontier models run
through thecompletefive-stage pipeline of eq. (2).Teal: open-
weight models judging thesame50 documents at the report stage
alone. (a) The full pipeline scores 40%, 36%, 14%; the per-agent
routing run fallsbelowthe 20% chance rate, and all three land
beneath every report-only system shown. (b) The mechanism is
visible: the full pipeline answersmitigateon 68%, 80%, 62% of
cases against a true frequency of20% — a systematic over-doom
bias. The comparison is confounded by model family (frontier vs
open-weight), so we read it as evidence about thebiasand treat
the accuracy ordering as the motivation for the matched ablation in
section 5.6.
full-pipeline runs are frontier, the report-only baselines open-
weight),sowereaditasevidenceaboutthebiasthesimulation
stages induce rather than as a clean accuracy ranking; Sec-
tion 5.3 already isolated the prompt component of the gap.
The practical reading is that more machinery is not more
accuracy on this task, and the extra stages cost latency—a
median of several minutes per case (Table 4). Whether the
harmisthereactionsignalorthestackingofstagesthatcarry
it is exactly what the matched ablation of Section 5.6 decides.
7

judge family direction agree concern recall
Opus 4.8 cloud 12/16 (75%) 67%
GPT-5.2 cloud 11/16 (69%) 80%
Qwen3-32B open 12/16 (75%) 86%
Gemma-3-27B-it open 12/16 (75%) 90%
Table 5. Blind fidelity of the synthetic reaction against the real
one, on the16reaction-driven cases, by four judges across families.
Directionagreementisafloor(seetext);concernrecall—whichhas
no trivial baseline—is the load-bearing signal and ishigherfor the
two open-weight judges.
5.5 The reaction simulation is a faithful proxy
Section 5.4 asks whether adding the simulation improves the
verdict;foratoolwhosepurposeistorehearsereactionbefore
a decision ships, the prior question is whether the synthetic
reactionit produces resemblesthe realone atall. At decision
time no real reaction exists, so the synthetic transcript is the
production artifact and its faithfulness is the construct the
whole system rests on. We test it directly on the16 cases—a
subsetofthe 28-casereactionstratum(Figure16)—forwhich
a real, outcome-scrubbed contemporaneous public reaction
could be sourced. Each reaction block—the exact personas-
and-timeline text the report stage consumes—is ratedblind:
the judge sees one block at a time, is never told whether it is
synthetic or real, and never sees the outcome. Four judges
spanning families do the rating (cloud: GPT-5.2, Opus 4.8;
open-weight: Qwen3-32B, Gemma-3-27B-it), which also
yields an inter-judge reliability check on the measurement
itself. Theload-bearingmetricisconcernrecall: thefraction
of the concerns raised in the real reaction that the synthetic
reaction anticipated.
Across all four judges the synthetic reaction anticipates
67–90% of the concerns the public actually raised (Table 5),
andthetwoopen-weightjudgesscoreithighest( 86–90%),so
the result is not a cloud-judge artifact. Inter-judge reliability
ishigh—acrossthesixjudgepairs,stanceratingsagreewithin
one point on75–100%of cases (the two cloud judges, Opus
andGPT,agreeonall 16)—sothemetricisstable,notasingle
model’sidiosyncrasy. Wearedeliberatelyconservativeabout
the weaker signals. Direction agreement (69–75%) reads
well but barely clears its own baseline: eleven of the sixteen
cases drew genuine backlash, so a majority-class “always
predict opposition” rule already scores about69%, and we
therefore report direction only as a floor and never as the
headline. The signed stance gap between synthetic and real
is small (|mean|≤0.56 on a[−2,2] scale) but itssignflips
by judge family—the two cloud judges find the synthetic
slightlymilderthan reality, the two open judges slightly
more negative—so we claim no robust “milder-” or “doom-
bias” direction, and the earlier presumption of a systematic
over-doom bias is not borne out. Finally the real sidecar
is a press-grade floor on the true concern set, which biases
recall up and leaves precision uncomputed; recall is thus
the trustworthy direction, not a two-sided estimate. Within
solvernosim withsimΔ𝑏/𝑐
Opus 4.8 84% 80%−4pp 4/6
GPT-5.2 46% 66%+20pp 15/5
Qwen3-32B 52% 56%+4pp 6/4
Gemma-3-27B-it 48% 50%+2pp 7/6
mean+5.5pp 3/4 with𝑏>𝑐
Table 6. Matched with/without-simulation ablation,50 cases,
exact-match against the verified outcome.𝑏 = cases the simulation
fixed (withsim right, nosim wrong);𝑐 = cases it broke. Read as
within-session deltas: thewithsim arm reproduces the Section 5.3
full-contextnumberexactlyforGPT( 66%),whilethegatewayOpus
run drifted+12pp across sessions (see text).
those bounds the reading is clean:the simulated reaction is a
faithful proxy for the substance of the real one, independent
of whether it moves the final label—the question we turn to
next.
5.6 Does the simulation improve the decision?
A matched with/without ablation
Section7namesthematchedwith/without-simulationarmas
the evidence gap that would isolate the simulation’s marginal
contribution to the verdict. We supply it, and because the
direction of the result was uncertain wepre-registeredthe
verdict rule before running: the rule was fixed before any of
these numbers were generated. The design holds everything
constant except the simulation: the same Gold-50 cases, the
samesystemprompt,thesamerequestedJSON,andthesame
taxonomy-definition block of Section 5.3 inbotharms; the
only variable is whether the persona-and-timeline simulation
is present. Thenosim arm gives the solver the decision title
alone;the withsimarmaddsthesimulation. Foursolvers(the
two cloud and two open-weight models above) answer each
arm,scoredbythesameexact-matchrule. Thepre-registered
threshold for “the simulation helps” was a meanΔ≥+6pp
with a majority of solvers showing more cases fixed than
broken by the simulation (𝑏>𝑐).
The mean effect is+5.5pp with three of four solvers
showing𝑏 > 𝑐(Table 6). By the pre-registered rule this
missesthe+6pp threshold, so the verdict is a null; we report
it as such rather than rounding half a point to clear our own
bar. But the null is structured, not noise, and the structure
is the finding: the simulation’s value scales inversely with
how much the solver already knows from the decision title.
GPT-5.2,weakfromthetitlealone( 46%),gains+20pp,with
the simulation fixing15 cases and breaking only5; the two
open-weight solvers gain modestly in the same direction;
and Opus, which already reaches84% from thetitle alone,
slightlyregresses(−4pp)astheextracontextgivesitmoreto
over-reason about. The simulation helps most exactly where
the decision is hardest for the model, and is redundant where
the label is already inferable from the decision itself.
Two consistency notes bound the reading. Thewithsim
8

0 20 40 60 80 100
0
20
40
60
80
𝑦=𝑥
Qwen3-32B base
Qwen3-32B+DPO
Llama-3-8B+SFT
Qwen3-8B+SFT
Qwen3-32B+SFT v3
agreement with the cloud teacher’s verdict,𝑛=10(%)
accuracy vs. outcome,𝑛=50(%)
Figure9. Agreeingwiththeteacherisnotthesameasbeingright.
Horizontal axis: how often a system reproduces the cloud teacher’s
verdict on the 10 archived runs it was distilled from. Vertical
axis: how often the same system matches the verified real-world
outcome on the Gold-50 set. Systems sit well below𝑦=𝑥 , and
the teacher itself agrees with itself 10/10 while its own verdicts are
not the outcome-correct answer on the cases where both are known
(section 5.7). Distillation-style metrics therefore measure imitation,
and we use them only as a training-progress signal, never as an
accuracy claim.
arm reproduces the Section 5.3 full-context resultexactlyfor
GPT-5.2 (33/50=66% ), confirming the ablation harness is
identicaltotheoneusedelsewhereinthepaper. Thegateway
Opus withsimrun,however,scored 80%hereagainst 68%in
theearlierdebiasrununderthenominallyidenticalcondition—
a 12pp single-seed drift that reinforces the repeated-seeds
gap of Section 7 and is why we read this ablation as within-
session paired deltas rather than absolute levels. Taken with
Section 5.4, the picture resolves: the harm from thefull
five-stage pipeline was the stacked stages amplifying over-
doom, not the reaction signal itself, which at the report stage
is net-neutral-to-helpful and, per Section 5.5, substantively
faithful.
5.7 Agreeingwiththeteacherisnotbeingright
Because the open checkpoints are distilled from a cloud
teacher,itistemptingtotracktrainingprogressbyagreement
with that teacher. Figure 9 shows why that metric is mis-
leading. Across successive SFT rounds, agreement with the
teacher’s verdict on the archived runs climbs from1/10 to
7/10while outcome accuracy on Gold-50 barely moves, and
the teacher agrees with itself10/10 while its own verdicts
are frequently not the outcome-correct answer. Distillation-
style metrics measure imitation [12], so we use them only
as a training-progress signal and never as an accuracy claim.
Section B gives the formal reason this pattern is expected.
5.8 Cost is flatter than quality
All eleven systems are instrumented for peak memory,
throughput and latency (Section F). Peak memory spans
16×, from4.32GB to69.13GB, and every configuration fits
on a single183GB accelerator, so the deployment question
is throughput, not capacity. The quality frontier is flatter
than the leaderboard suggests: the untuned Qwen3-8B base
reaches 54.0% at 17.70GB and46.6 tok/s—within 8pp of
the leader (the Qwen3-32B LoRA-SFT) and not significant
(𝑝=0.424 )—ataquarterofthememory. Fine-tuning,mean-
while, costs throughput at every scale, because the unmerged
adapteraddsworkateveryforwardpassandSFTalsoteaches
the model to emit a reasoning trace before the JSON.
6 Discussion
The core results reinforce one conclusion. A single-prompt
leaderboard on this task measures the prompt at least as
much as the model: the same weights swing0% to 73%
(Section 5.2), and defining the taxonomy for everyone closes
most of the frontier gap on these fifty cases (Section 5.3).
Underafairprompttheopen-weightQwen3-32BLoRA-SFT
served offline shows no statistically significant difference
from the frontier on this decision, and under an unfair one
it wins—not because it is stronger, but because it was tuned
to the exact envelope while the frontier models were left to
guess an under-specified rubric.
Two of the results are, at first sight, discouraging for the
system itself: distillation metrics do not track accuracy, and
stacking the full pipeline ahead of the report amplifies bias.
We think the honest framing is that these arepredictable
consequences of the design, not surprises. Section B shows
that distilling both the generator and the judges from one
teacher collapses the ensemble to the teacher’s error floor,
and that any exact-match scorer bounds accuracy by the
in-schema rate—so teacher-agreement and prompt-envelope
effects are exactly the confounds the theory says to expect.
The design response is the one already built in: source the
critic cross-family and off-the-shelf, and report compliance
alongside every accuracy.
Thereactionlayeritself,however,comesoutofthisscrutiny
better than the full-pipeline number alone suggests. The
matched ablation (Section 5.6) isolates the report-stage re-
action signal from the stack that carries it: the signal is net-
neutral-to-helpful—stronglyhelpful(+20pp)fortheweakest
title-only solver and neutral for one already near ceiling—so
the over-doom of Section 5.4 is a property ofstackingthe
generative stages, not of the reaction evidence they produce.
And that evidence is faithful on its own terms (Section 5.5):
the synthetic reaction anticipates67–90% of the concerns
the public actually raised. The system’s contribution is thus
the validated qualitative reaction, not a guaranteed lift on a
label a capable model can already infer from the decision.
7 Limitations and Evidence Gaps
The benchmark is small:𝑛=50 makes Wilson intervals wide
and leaves most pairwise differences undecidable except
by the paired test, and the smallest strata (𝑛=7 and 𝑛=4)
carry intervals too wide to rank. The Gold-50 labels are
9

a single annotation pass by the authors against each case’s
realized outcome in the public record: because the policies
studied were live and no external adjudicator was available,
no independent re-labeling or inter-annotator agreement was
possible, so the set is a best-effort verified benchmark rather
thananexternallyrefereedone. Thefull-pipelinecomparison
(Section 5.4) remains confounded by model family; the
matched with/without-simulation arm thatpriorversions of
this work still lacked is now supplied in Section 5.6, and its
verdict is a pre-registered null (+5.5pp, below the+6pp bar)
with a coherent heterogeneity underneath it—so we can now
say the report-stage reaction signal is net-neutral-to-helpful
and faithful, but we still cannot claim it reliably lifts the final
label for a model already near ceiling. Two residual caveats
attachtotheablation. First,thegatewayisnotseed-stable: the
Opus withsim arm drifted+12pp across nominally identical
sessions, so the ablation is read as within-session paired
deltas and the absolute levels should not be over-read; a
repeated-seeds study is the natural next step. Second, the
fidelity study of Section 5.5 validates thesubstanceof the
synthetic reaction (concern recall67–90%), but a separate
analysisfeedingthemodeltherealcontemporaneousreaction
in place of the synthetic one shows a calibration gap: the
report stage is tuned against the synthetic distribution, so
a synthetic-to-real handoff is not yet drop-in, and closing
that gap is future work. The preference-training set is small
and synthetic, and its downstream effect is null. Finally, all
offline serving numbers are single-accelerator, single-case-
sequential except where a batched wall-clock is stated. We
reportthesegapsratherthansmoothingoverthem,andwithin
this benchmark none of them overturns the paper’s central,
prompt-artifact reading.
8 Reproducibility
Nothing in this paper is transcribed by hand. A three-stage
buildpipelineclosestheloopfromtherunartifactstothisPDF.
A recomputation stage computes every statistic—Wilson
intervals, exact McNemar tests, per-class confusion, driver
strata—fromtheper-casepredictionfiles(bothpromptarms),
the verified Gold-50 labels, the per-step training logs and the
benchmark summaries, writing a single machine-readable
metricsfile. Arenderingstageturnsthatfileintoeveryfigure
and table macro spliced into this document. A verification
stage then re-asserts every quoted number, interval,𝑝-value
and plotted mark against the same file and fails loudly on
any drift. The corpus behind the checkpoints is457training
rows (292 unique) drawn from81 archived runs, with267
preference pairs (invalid-JSON, hallucination, and45 over-
doom triples) for the DPO pass. The system describes
standaloneon-diskartifactsandrecordsinterpreterandlibrary
versions.
9 Responsible Use
Augur manufactures a proxy for human reaction; it does
not observe one. Its personas are graph-grounded synthetic
constructs, not real people, and its forecasts are explicit
hypotheses to be backtested against reality, not predictions to
be acted on unexamined. The over-doom bias documented
in Section 5.4 is a concrete reason to treat any single verdict
as provisional. The appropriate use is to rehearse and stress-
test a decision and to surface constituencies a team might
overlook, with a human owner accountable for the decision
and its outcome.
10 Conclusion
Augur rehearses reactions to product and policy changes
offlineandreturnsanauditableverdict,butthepaper’slasting
contributioniswhatthemeasurementrevealed. Onthesefifty
real decisions with verified outcomes, most of the measured
gap between frontier cloud models and open-weight models
served offline is attributable to an under-specified evaluation:
define the taxonomy for everyone and a Qwen3-32B LoRA
shows no significant difference from the frontier; leave it
under-specified and the same model wins. The harness
can move a single system—the Qwen3-32B LoRA-SFT—
from 0%to 73%,teacher-agreementclimbswithoutaccuracy
following, and in the tested configuration more pipeline
brought more bias, not more accuracy—each a predictable
consequence we make formal. Where wecancredit the
reaction layer is on its own terms: the synthetic reaction is a
faithful proxy for the real one (concern recall67–90%across
four blind judges), and in a pre-registered matched ablation
it helps most exactly where the decision is hardest—+20pp
for the weakest title-only solver—while adding nothing for a
model already near ceiling. The methodological lesson we
draw, subject to this benchmark’s scale, is: on a structured
decisiontask,reportthepromptenvelopeandthecompliance
rate, or the leaderboard is measuring something other than
judgment.
A Formal Framework
Let𝐷={𝑑 1,...,𝑑 𝑚} be the documents defining a change
and𝑞the decision question. The action space is
A={ship,revise,delay,segment,mitigate}.(1)
Definition 1(Decision map).Augur realizesΦ:(𝐷,𝑞)↦→
(𝑎★,𝐹,E) producing a recommended action𝑎★ ∈ A, a
quantitative forecast𝐹, and an evidence setE, factored as
the composition of stage operators
Φ(𝐷,𝑞)=𝑅 𝑆(𝑃(𝐺(𝐷),𝑞),𝑞), 𝐺(𝐷), 𝑞 ,(2)
where 𝐺 (graph), 𝑃 (persona), 𝑆 (simulation), 𝑅 (report)
are LLM-realized maps, and a fifth operator𝐼 (interview)
supports post-hoc interrogation.
10

Each operator is realized by a single-responsibility agent
that reads priorartifactsand writes its own; agents never
invoke one another (Definition 4). The extracted graph is
𝐺=(𝑉,𝐸) withavertex-labelmap ℓ:𝑉→L whoseimage
ℓ(𝑉) is the set of audience segments, per-vertex topic sets
topics(𝑣), and induced topic universeT𝑉 = — 𝑣∈𝑉 topics(𝑣).
Persona space.
Definition 2(Persona).A persona is a tuple 𝑝=
(𝑔,𝑠,𝑏,𝛼,𝜌,𝜔,𝐻,T 𝑝)in the attribute space
X=ℓ(𝑉)×[−1,1] 2×[0,1] 2×R≥0×2{0,...,23} ×2T𝑉,(3)
with segment𝑔, stance𝑠, sentiment bias𝑏, activity𝛼, re-
sponse speed𝜌, influence weight𝜔, active hours𝐻, topics
T𝑝. The populationP={𝑝 1,...,𝑝 𝑛}=𝑃(𝐺,𝑞).
Assumption 1(Grounding).Every synthesized persona ref-
erences the graph:𝑔∈ℓ(𝑉) andT𝑝⊆T𝑉. HenceP is a
market for thespecificchange encoded in𝐺, not a generic
crowd.
Interaction dynamics.The simulation runs rounds 𝑡=
1,...,𝑇 , producing a timelineΘ of posts with expressed
sentiment𝑦𝑥∈[−1,1] (Θ𝑡−1 denotes the timeline through
the previous round). With topical relevancerel(𝑝,Θ)=
|T𝑝∩topics(Θ)|/|T 𝑝|, the activation propensity is
𝑎𝑝,𝑡 =clip 𝛼𝑝+𝜅𝑟 rel(𝑝,Θ 𝑡−1),0,1 , 𝜅 𝑟≥0,(4)
with𝜅𝑟≥0 the relevance-gain coefficient. Expressed senti-
ment tracks stance and bias, pulled toward prevailing thread
sentiment by a bounded conformity term𝜆∈[0,1],
E[𝑦𝑥]=clip

(1−𝜆)(𝑠 𝑝+𝑏 𝑝)+𝜆¯𝜎(Θ 𝑡−1),−1,1

,(5)
¯𝜎(Θ)= 1 |Θ| ˝ 𝑥′∈Θ𝑦𝑥′, the DeGroot/bounded-confidence
intuition [4, 5, 6] used as a conditioning signal. Engagement
isadeterministicfunctionofthepersonasandpostsentiment,
eng(𝑥)=𝜔 𝑝

𝛽0+𝛽1
∑︁
𝑝′∈P\{𝑝}
𝜔𝑝′ 1  sign(𝑠𝑝′)=sign(𝑦 𝑥)   .
(6)
with baseline weight𝛽0 ≥0 and peer-alignment weight
𝛽1≥0.
Transcript audit metrics.Three pure-code auditors read
the finished timeline; withPact the personas that posted,
𝑈=1−Var{𝑠 𝑝 :𝑝∈P act}𝛿max (uniformity),(7)
Gap=
˝
𝑔∈Γ\Γ act𝑐(𝑔)˝
𝑔∈Γ 𝑐(𝑔) (constituency gap),
(8)
𝜈𝑡 =

𝑊𝑡\ — 𝑢<𝑡𝑊𝑢

|𝑊𝑡|(round novelty).
(9)
Here𝛿max is the maximum attainable stance variance, the
normalizer that places𝑈∈ [0,1] ; Γ is the set of graph-
derived constituencies with active subsetΓact⊆Γ and𝑐(𝑔)
the size of constituency𝑔; and𝑊𝑡 is the set of distinct claims
raised in round𝑡. Each firing earns at most one corrective
round under a global budget𝐵(Section C).
Verdict aggregation.
Definition 3(Ensemble verdict). 𝑘 models re-analyze the
sametimeline,emitting 𝑎(𝑖)∈A . Theverdictandagreement
are
𝑎★=arg max
𝑎∈A
𝑘∑︁
𝑖=1
1

𝑎(𝑖)=𝑎  , 𝐴 ★= 1 𝑘 max 𝑎∈A 𝑘∑︁ 𝑖=1 1  𝑎(𝑖)=𝑎  .
(10)
Whenever𝐴★<1 the split is reported as a first-class uncer-
tainty signal.
An opposite-family critic returns𝑐∈ {0,...,10} ; QA
passes iff𝑐≥𝜃.
Definition 4(Run state and dependency DAG).A run state
is the partial mapΣ:N⇀Artifacts over nodesN=
{𝐺,P,Θ,𝑅,𝐼} . Thederived-fromDAGD =(N,→) has
edgesP→𝐺 ,Θ→P ,𝑅→Θ ,𝑅→𝐺 ,𝐼→P ,𝐼→Θ (anedge
𝑢→𝑤 reads “𝑢 derived from𝑤”). Writing or regenerating
𝑣 triggerscascade invalidation: delete{Σ(𝑢):𝑢∈anc(𝑣)} ,
i.e. every artifact derived from𝑣.
B Formal Properties
The two propositions the body relies on are the last two; we
state the ensemble result they build on first.
Proposition 1(Ensemble amplification).Let 𝑘=3 judges
vote independently, each correct with probability𝑝 >1 2. The
majority verdict is correct with probability𝑔(𝑝)=3𝑝 2−
2𝑝 3> 𝑝for𝑝∈( 1 2,1), and𝑔 is strictly increasing on[0,1] .
For general odd𝑘, majority accuracy is nondecreasing in𝑘
and→1as𝑘→∞(Condorcet).
Proof.𝑔(𝑝)= 3 2 𝑝2(1−𝑝)+𝑝 3=3𝑝 2−2𝑝 3,and 𝑔(𝑝)−𝑝=
𝑝(2𝑝−1)(1−𝑝)>0 for𝑝∈( 1 2,1);𝑔′(𝑝)=6𝑝(1−𝑝)≥
0 on[0,1] . The general-𝑘 claim is the Condorcet jury
theorem.□
Corollary 1(Correlation defeats amplification).The gain
𝑔(𝑝)−𝑝 is premised on independence. If judges’ errors are
correlated with coefficient𝜌𝑐, ensemble reliability degrades
toward the single-judge accuracy𝑝 as𝜌𝑐→1 . Sourcing the
critic and cross-check from adifferentmodel family lowers
𝜌𝑐, which is why Augur draws them cross-family (Section 2).
Proposition 2(Distillation collapses judge independence).
Let a teacher𝑇 select the correct action with probability𝑝𝑇.
Let𝑘 studentsbedistilledfrom 𝑇 suchthateachindependently
reproduces𝑇’s answer with fidelity𝜑∈[ 1 2,1] and otherwise
11

answers correctly with probability𝑝0, independently across
students. Let𝐴𝑘(𝜑) betheaccuracyofthestudents’majority
vote. Then
lim
𝜑→1
𝐴𝑘(𝜑)=𝑝 𝑇 for every𝑘,(11)
so the ensemble gain𝐴𝑘−𝑝 𝑇 vanishes as fidelity improves,
no matter how many judges vote.
Proof. Condition on𝑇’s answer. With probability𝜑𝑘 all
𝑘 students return𝑇’s answer, so the majority equals𝑇’s
answer and is correct with probability exactly𝑝𝑇. The
remaining mass is1−𝜑 𝑘→0 as𝜑→1 , and accuracy is
bounded in[0,1] there, so|𝐴𝑘(𝜑)−𝑝 𝑇|≤1−𝜑 𝑘 →0 .
The conditional independence premise of Proposition 1 fails
becauseallstudents’errorsaredrivenbythecommonvariable
𝑇’s answer; formally𝜌𝑐→1and Corollary 1 applies.□
Corollary 2(Never distil the critic).The critic and cross-
check must be obtained off-the-shelf from a family not used
to produce the training targets. Augur therefore fine-tunes
only the generation stages and leaves the judge untuned
(Section 2).
Proposition 2 is directly testable: 𝜑 is the teacher-
agreement rate and𝑝𝑇 the teacher’s own accuracy. Sec-
tion5.7measures 𝜑risingfrom 10%to 70%undersuccessive
SFT rounds with no corresponding movement in outcome
accuracy—the signature the proposition predicts.
Definition 5(Prompt envelope and out-of-schema rate).A
prompt envelopeW maps a case to the exact message se-
quence presented to the model, including system prompt,
context serialization and requested schema. For system𝑀
underW, let𝜂(𝑀,W)=Pr[ˆ𝑎∉A] be the out-of-schema
rate.
Proposition 3(Schema-compliance ceiling).Under any
scorer that credits only exact matches inA,
Acc(𝑀,W) ≤1−𝜂(𝑀,W),(12)
with equality iff every in-schema answer is correct. Hence
for two envelopes the measured difference decomposes into a
judgment term and a compliance term, and a cross-envelope
comparison is uninterpretable as a judgment comparison
unless𝜂is reported alongside it.
Proof.{ˆ𝑎=𝑎 ★} requires ˆ𝑎∈A , soAcc=Pr[ˆ𝑎=𝑎 ★]≤
Pr[ˆ𝑎∈A]=1−𝜂 ; equality holds when{ˆ𝑎∈A}⊆{ˆ𝑎=
𝑎★} up to null sets. WritingAcc=(1−𝜂)Pr[ˆ𝑎=𝑎 ★|ˆ𝑎∈
A] and comparing the two factors envelope-wise gives the
decomposition.□
Proposition 3 is the entire explanation of Section 5.2:
SFT drove𝜂 almost to zero on the deployed envelope while
leaving it high on an unfamiliar one, so the same weights
score 0/11 under one prompt and8/11 under another. It
also dictates the reporting rule we follow throughout: every
accuracy is accompanied by its unparseable count and both
the conservative and conditional scores.
Algorithm 1Autonomous run with budget-bounded self-
audit
Require: documents𝐷,question 𝑞,budget 𝐵,thresholds 𝜏𝑈,𝜏Γ,𝜏𝜈
1:𝐺←Extract(𝐷;Ontology(𝐷))
2:P←𝑃(𝐺,𝑞);Θ←𝑆(P,𝑞);𝑟←0
3:while𝑟 < 𝐵do
4:compute𝑈,Gap,{𝜈 𝑡}fromΘ(7)–(9)
5:ifGap>𝜏 Γ then
6:Θ←𝑆(P,𝑞;focus=Γ\Γ act,append)
7:else if𝑈≥𝜏 𝑈 then
8:Θ←𝑆(P,𝑞;moderator-steer,append)
9:else ifmin 𝑡𝜈𝑡≥𝜏𝜈 then
10:Θ←𝑆(P,𝑞;extend,append)
11:else break
12:end if
13:𝑟←𝑟+1
14:end while
15:(𝑎 ★,𝐴★,𝑐)←Verdict(Θ,𝐺,𝑞)
16:returnreport𝑅(Θ,𝐺,𝑞)with(𝑎 ★,𝐴★,𝑐,audit log)
Algorithm 2Verdict: critic-gated cross-family ensemble
Require: timelineΘ, graph𝐺, question𝑞; familiesF, threshold𝜃
1:for𝑖=1to𝑘do
2:𝑎 (𝑖)←𝑅 𝑖(Θ,𝐺,𝑞).action
3:end for
4:𝑎 ★,𝐴★←mode and agreement of{𝑎(𝑖)}(10)
5:𝑐←Critic ¯𝑓(𝑅,Θ)⊲opposite family ¯𝑓
6:if𝑐<𝜃then
7:spend one corrective action; recompute𝑎 ★
8:end if
9:return(𝑎 ★,𝐴★,𝑐)
C Algorithms and Complexity
Algorithm1istheautonomousrun: forwardpipeline,budget-
bounded self-audit, then the critic-gated ensemble verdict of
Algorithm 2.
With𝑛=|P| ,𝑇 rounds and𝑘 ensemble members, the
dominant terms areO(𝑛𝑇) generation calls in simulation
andO(𝑛 2𝑇) pure-CPU arithmetic for engagement(6); the
self-audit adds at most𝐵 generation rounds and the verdict
adds𝑘+1calls, both constant in𝑛,𝑇.
D Fine-Tuning Details
AlladaptersuseoneLoRArecipe(Table7); onlythetraining
data changes across the32B lineage v1→v2→v3, whose
validation set is frozen.
12

Table 7.The single LoRA-SFT recipe shared by every adapter;
only the training data differs across runs.
Hyperparameter Value
Method LoRA
Rank/𝛼16/32
Dropout0.05
Target modulesq,k,v,o_proj
Epochs3
Learning rate1×10 −4, cosine
Effective batch16
Sequence length8192
Early stopping patience3, reload best
Precision bf16
Figure 10 shows LoRA-SFT optimization on all five back-
bones under this recipe: loss is masked to assistant tokens,
so it measures only the target⟨think⟩+JSON, and held-out
loss is evaluated on twowholearchived runs withheld from
training so that no document appears on both sides of the
split.
1
1.5
2
2.5
cross-entropy
(a) Training loss (masked to assistant tokens)
Llama-3-8B-Instruct
Gemma-3-27B-it
Qwen3-32B (v3)
Qwen3-8B
Qwen3-1.7B
20 40 60 80
1
1.5
2
optimiser step
cross-entropy
(b) Held-out loss (2 whole runs, leakage-safe)
Llama-3-8B-Instruct
Gemma-3-27B-it
Qwen3-32B (v3)
Qwen3-8B
Qwen3-1.7B
Figure 10. LoRA-SFT optimisation on five backbones, identical
data, recipe and schedule (table 7); one adapter per backbone.
Loss is masked to assistant tokens, so it measures only the target
⟨think⟩+JSON. Held-out loss is evaluated on twowholearchived
runs withheld from training, so no document appears on both sides.
Llama-3-8B: 1.81→1.20 train, best held-out1.322; Gemma-3-
27B: 2.49→0.86 train, best held-out 1.099; Qwen3-32B (v3):
1.57→1.09 train, best held-out1.133; Qwen3-8B: 2.07→1.29
train, best held-out1.317; Qwen3-1.7B: 2.61→1.59 train, best
held-out 1.675. Every curve is read from the archived per-adapter
training logs.
Figure 11 isolates the recipe iteration on the fixed32B
backbone. It is the evidence that the v3 gain came from data
volume rather than a longer schedule: v2 reaches the lowest
trainingloss yet not the lowest held-out loss—the small-
corpus overfitting signature that motivates early stopping
with best-checkpoint reload.
0 20 40 60 80
0.8
1
1.2
1.4
1.6
optimiser step
cross-entropy
v1 train v1 held-out
v2 train v2 held-out
v3 train v3 held-out
Figure 11. Three SFT recipes on one fixed backbone(Qwen3-
32B), showing that the gain came from data volume, not from a
longer run. v1 and v2 take 27 and 39 steps; v3 takes 87. Best
held-out loss falls 1.163→1.134→1.133. v2 reaches the lowest
trainingloss (0.886) yet not the lowest held-out loss — the classic
small-corpus overfitting signature, and the reason early stopping
(patience 3) reloads the best checkpoint rather than the last.
Figure 12 is the DPO calibration pass layered on top of
the SFT adapter. Its optimization dynamics are healthy—the
reward margin widens because the rejected branch is pushed
down—but its downstream effect on Gold-50 is null, which
wereadasthepreferencesetbeingtoosmallandtoosynthetic
to move judgment.
13

0
0.2
0.4
0.6 ln 2: chance
−log𝜎(𝛽Δ)
(a) DPO loss
train
held-out
−5
0
5
𝑟𝑐−𝑟 𝑟
(b) Implicit reward margin
margin
𝑟chosen𝑟rejected
0 20 40 60 80 100
0
0.5
1
optimiser step
fraction correct
(c) Preference accuracy
Pr[𝑟 𝑐 > 𝑟𝑟]
Figure 12. DPO calibration passon top of the SFT adapter
(𝛽=0.1 ),therunthattargetstheover-doombias. Lossfallsfromthe
ln 2≈0.693 chance level to 0.081 over 93 steps (3641s), best held-
out 0.0895. Panel (b) separates the implicit rewards𝑟=𝛽log 𝜋𝜃 𝜋ref : the margin widens because the rejected branch is pushed down, the
diagnosticsignatureofapreferencepassthatislearningthecontrast
rather than merely raising likelihood everywhere. Panel (c) is the
fractionofpairsrankedcorrectlywithineachtrainingbatchofeight,
which is why it moves in steps of1/8; on the26held-out pairs the
same quantity is26/26at six of nine evaluations and never below
25/26.These dynamics are healthy but the downstream effect is
null(table 1): DPO leaves Gold-50 accuracy unchanged, which we
read as the preference set (over-doom, invalid-JSON, hallucination
triples) being too small and too synthetic to move judgment.
E Gold-50 Construction and Repro-
ducibility
Labeling convention.Table 8 states the disposition that
defineseachofthefiveclasses—therealized-outcomereading
a case must match to earn that label. Labels record what
the organization’s change actually did, not a normative “best
move.”
Table 8. The Gold-50 label convention.Each label records the
real-worlddispositionof the decision — what actually happened to
it,nothowloudthereactionwasandnottheactionanidealdecision-
maker “should” have taken. The convention is applied uniformly
across all fifty cases; the one boundary it resolves explicitly isship
vssegment(one universal rule vs two rules for two groups).
Action Assigned when the real-world decision...
ship launched as announced and persisted, with one rule
applied universally even if effects differ by user: no
reaction-driven rollback, postponement, or carve-out.
revise was itself materially changed or reversed (including
fully abandoned) in response to the reaction: what
shipped≠what was announced.
delay had its launch or enforcement postponed, then gener-
ally proceeded: a date moved.
segment ended in two different rules for two groups — by
region, size, or plan tier — that persisted: the dispo-
sition differs by segment, not just its effects.
mitigate was kept at its core, but concessions or safeguards
were bolted on to address objections: decision stands,
remedies added.
Per-case ledger.Table 9 is the full Gold-50 ledger: for
each case, its adjudicated label, the episode year and the
number of independent public sources consulted. These are
real, publicly documented decisions, and the label reports
the realized public-record outcome, not a judgment of the
organization. The outcome-driver stratification used in the
analysis (Section F) is reported only in aggregate, never
attached to a named case. The table is generated directly
from the benchmark file; the source counts have a median of
three per case.
Adjudication and circularity.The fifty labels were fixed
in a single author adjudication pass against the public record,
assisted by Claude Opus 4.8 (adjudication run 2026-09-06).
BecauseClaudeOpus4.8isalsooneofthethreebenchmarked
frontier models, its adjudication role is a potential source
of circularity in the frontier comparison, and the Opus 4.8
leaderboard row should be read with that caveat. The la-
bels are a single-pass adjudication, not a multi-annotator
consensus with an inter-rater statistic; a second independent
annotation is the most important addition a follow-up should
make.
Input isolation.Each system is prompted with only the
pre-decisioncasedocument(thepolicyorproductdescription
as it stood before the outcome). The realized outcome, the
outcome-driverannotationandthesourcelistareneverplaced
in the model input and are used only for scoring.
Contamination audit.Gold-50 is disjoint from the fine-
tuning, preference, validation and model-selection data. The
metrics pipeline recomputes the audit from the raw splits:
0Gold-50 case identifiers appear in the training corpus, no
Gold-50 case document matches any training document, and
14

Table 9. The Gold-50 case ledger.Every case, grouped by verified label.Yris the decision year;Srcis the number of cited public
sources behind the recorded outcome (139 in total, median 3). All fifty are real, publicly documented decisions whose realized outcome is
a matter of public record; the labels report that outcome, not a judgment of the organization. They were adjudicated against the public
record in a single manual adjudication pass, assisted by Claude Opus 4.8 (2026-09-06); full source URLs and per-case rationales live in
realworld_gold_50.jsonl. Generated from the computed metrics.
Case Label Yr Src
Amazon Prime Video — Introduce Ads for Existing U.S. Members ship 2023 3
Amazon Prime — Raise U.S. Annual Membership to $139 ship 2022 3
Etsy — Raise the Marketplace Transaction Fee to 6.5% ship 2022 3
Firefox Quantum — End Legacy Extension Support ship 2017 2
Google Photos — End Unlimited Free Photo Storage ship 2020 3
iPhone 7 — Remove the Headphone Jack ship 2016 3
Nintendo Switch Online — Introduce Paid Online Multiplayer ship 2018 3
Nintendo — Launch Tears of the Kingdom at $69.99 ship 2023 3
PlayStation Plus — Raise Annual Subscription Prices ship 2023 3
YouTube — Hide Public Dislike Counts ship 2021 3
Apple iCloud Photos — Abandon On-Device CSAM Detection revise 2021 3
Apple Music — Withhold Royalties During the Free Trial revise 2015 2
Dungeons & Dragons — Replace the Open Game License revise 2023 3
Helldivers 2 — Mandatory PlayStation Account Linking on PC revise 2024 3
Instagram — Expand the Full-Screen, Recommendation-Heavy Feed revise 2022 3
Patreon — Shift Payment Processing Fees to Patrons revise 2017 2
Spotify — Withdraw Artist-Conduct Restrictions on Promotion revise 2018 3
Twitch — Restrict Streamer-Controlled Sponsor Advertising revise 2023 2
Xbox Live Gold — Reverse the Subscription Price Increase revise 2021 3
Zoom — Reverse Paid-Only Access to End-to-End Encryption revise 2020 3
Android 11 Beta — Postpone the Public Rollout During U.S. Protests delay 2020 3
Apple AirPods — Postpone the October Retail Launch delay 2016 3
Apple App Tracking Transparency — Postpone Mandatory Enforcement delay 2020 3
Apple HomePod — Postpone the December Launch delay 2017 3
Cyberpunk 2077 — Postpone the April 2020 Release delay 2020 3
Google Find My Device — Postpone the Network for Cross-Platform Tracking Protections delay 2023 3
Halo Infinite — Postpone the Holiday 2020 Release delay 2020 3
OpenAI Advanced Voice — postpone the initial ChatGPT rollout delay 2024 3
Samsung Galaxy Fold — Postpone the First Retail Launch delay 2019 3
WhatsApp Privacy Update — postponing the acceptance deadline delay 2021 3
Apple App Store — Lower Commissions for Small Developers segment 2020 2
Apple iCloud — Transfer Mainland China Accounts to GCBD segment 2018 3
Apple iPhone 14 — Make US Models eSIM-Only segment 2022 3
Apple — Allow alternative iPhone app distribution in the EU segment 2024 3
Google Android — Unbundle App Licensing in the EEA segment 2018 3
Google Legacy G Suite — Exempt Personal Users from Paid Migration segment 2022 2
Google Play — Cut Fees on Developers’ First $1 Million segment 2021 3
Google Play — Permit Alternative Billing in South Korea segment 2021 2
Meta — Block News on Facebook and Instagram in Canada segment 2023 2
Slack — Limit Free Workspaces to 90 Days of History segment 2022 3
AMD–Xilinx — Complete the Acquisition with Competition Safeguards mitigate 2020 3
Apple AirTag — Keep Item Tracking with Stronger Anti-Stalking Safeguards mitigate 2021 2
Apple iPhone Performance Management — retain throttling with battery and transparency concessions mitigate 2017 3
Disney–Fox — Complete the Acquisition with Sports-Network Divestitures mitigate 2018 3
Facebook — Keep Authentic-Name Rules with Safer Reporting and Appeals mitigate 2015 2
Google–Fitbit — Complete the Acquisition with Binding Safeguards mitigate 2019 3
Microsoft–Activision Blizzard — Complete the Acquisition with Cloud-Gaming Safeguards mitigate 2023 3
Microsoft–LinkedIn — Complete the Acquisition with Interoperability Safeguards mitigate 2016 2
Spotify — Keep Joe Rogan and Add COVID-19 Safeguards mitigate 2022 3
T-Mobile–Sprint — Complete the Merger with Competition Safeguards mitigate 2019 3
15

Table 10. The debias 2×2, every system.Accuracy vs the verified outcome on the same 50 frozen contexts and the same direct harness; the
only change is the shared taxonomy-definition+anti-hedge block appended in the debias arm.Δ is percentage points;𝑝 is the two-sided
exact McNemar test on the paired baseline-vs-debias cases.∅counts unparseable generations (scored wrong). Generated from the computed
metrics.
System Baseline DebiasΔmacro-F1 McNemar
%[CI]%[CI]pp b→d𝑝
Frontier (cloud API)
Claude Sonnet 5 46[33,59.6]80[67,88.8]+34 0.43→0.79 7.6e-5 ∗
Claude Opus 4.8 44[31.2,57.7]68[54.2,79.2]+24 0.40→0.67 0.008 ∗
GPT-5.2 38[25.9,51.8]66[52.2,77.6]+28 0.36→0.64 0.003 ∗
Open-weight, fine-tuned (LoRA)
Qwen3-32B + LoRA-SFT 62[48.2,74.1]78[64.8,87.2]+16 0.59→0.78 0.039 ∗
Qwen3-32B + SFT→DPO 62[48.2,74.1]76[62.6,85.7]1∅+14 0.59→0.77 0.039 ∗
Llama-3-8B + LoRA-SFT 60[46.2,72.4]1∅68[54.2,79.2]+8 0.58→0.62 0.344
Gemma-3-27B + LoRA-SFT 50[36.6,63.4]50[36.6,63.4]2∅+0 0.44→0.46 1.000
Qwen3-8B + LoRA-SFT 50[36.6,63.4]6∅44[31.2,57.7]1∅-6 0.51→0.40 0.607
Qwen3-1.7B + LoRA-SFT 6[2.1,16.2]35∅24[14.3,37.4]17∅+18 0.07→0.23 0.035 ∗
Open-weight, untuned base
Qwen3-32B 56[42.3,68.8]58[44.2,70.6]+2 0.56→0.52 1.000
Qwen3-1.7B 46[33,59.6]48[34.8,61.5]+2 0.39→0.38 1.000
Gemma-3-27B-it 36[24.1,49.9]44[31.2,57.7]+8 0.34→0.34 0.481
Qwen3-8B 54[40.4,67]40[27.6,53.8]-14 0.52→0.28 0.065
Llama-3-8B-Instruct 16[8.3,28.5]36[24.1,49.9]+20 0.16→0.30 0.006 ∗
the strongest cross-set signal is a single shared company
name in at most one case. The training corpus is synthetic
persona-generation traces, constructed independently of the
retrospective episodes in Gold-50.
Decoding and hardware.All open-weight systems are
served under identical decoding: a4000-token generation
budget and provider-default sampling, with no per-model
tuning of temperature or top-𝑝. Adapters are served in bf16
on a single B200-class accelerator (183GB), whose capacity
holds every configuration with room to spare—per-system
peak memory is reported in Table 11—and with no cross-
device sharding. The frontier models are queried through
their vendor APIs at their default settings. Every number in
the paper is recomputed from the archived per-case artifacts,
re-rendered into the figure macros, and re-checked against
the artifacts by that same three-stage pipeline, which fails on
any mismatch.
F Additional Evaluation Detail
This section collects the per-system evaluation detail behind
the leaderboard and the cost discussion of the main text.
Per-class structure.Figure 13 gives confusion matrices
for three representative systems and Figure 14 the per-class
recall and prediction-bias fingerprint across all eleven. The
two views answer different questions: the confusion matrices
showwherea given system’s mass lands relative to the
verified outcome, while the heatmaps compare recall and
emission bias on a common scale so that themitigate-heavy,
segment-starved signature is visible as a pattern across the
whole population rather than an artifact of any one system.
Together they are the raw material for the over-doom claim:
the same off-diagonal mass that inflatesmitigateis the mass
missing fromsegment.
Whattheoutcomehingeson.Figure16stratifiesaccuracy
by the mechanism that actually decided each Gold-50 case—
public reaction, regulatory action, engineering readiness, or
business performance. The ordering is stable across systems
and is the honest limit of a reaction-simulating pipeline: the
reaction stratum, the one the architecture is aimed at, is
the one every system predicts worst, while regulatory- and
readiness-decided cases are recovered far more reliably.
16

shiprevisedelaysegmentmitigate none
ship
revise
delay
segment
mitigate
3 1 2 4
1 6 1 2
2 8
3 4 3
2 1 7
predicted
verified outcome
(a) Qwen3-32B base
shiprevisedelaysegmentmitigate none
3 4 3
2 8
1 9
4 2 2 2
1 9
predicted
(b) Qwen3-32B + LoRA-SFT
shiprevisedelaysegmentmitigate none
1 9
5 5
1 9
2 8
10
predicted
(c) Gemma-3-27B + LoRA-SFT
Figure 13. Confusion on the Gold-50 set, rows are the verified outcome (10 each), columns the predicted action,none the unparseable
bucket. The diagonal is accuracy; the informative structure is off-diagonal. All three systems concentrate mass in themitigatecolumn, and
thesegmentcolumn is nearly empty — models rarely propose splitting a release by cohort even when that is what the organisation actually
did. Fine-tuning (b vs a) sharpens the diagonal onshipandrevisebut does not createsegmentbehaviour, and on Gemma (c) it collapses
almost entirely intomitigate. fig. 14 quantifies this across all eleven systems.
ship revise delaysegmentmitigate
Qwen3-32B + LoRA-SFT
Qwen3-32B + SFT→DPO
Llama-3-8B + LoRA-SFT
Qwen3-32B
Qwen3-8B
Qwen3-8B + LoRA-SFT
Gemma-3-27B + LoRA-SFT
Qwen3-1.7B
Gemma-3-27B-it
Llama-3-8B-Instruct
Qwen3-1.7B + LoRA-SFT
3 8 9 2 9
3 8 9 2 9
4 8 8 1 9
3 6 8 4 7
1 5 9 3 9
5 7 10 3
1 5 9 10
8 5 10
7 4 7
4 4
2 1
verified outcome class
(a) Per-class recall (out of 10)
ship revise delaysegmentmitigate none
10 15 9 2 14
10 15 9 2 14
8 9 8 1 23 1
9 10 8 7 16
3 7 9 5 26
18 9 10 3 4 6
3 6 9 32
32 6 11 1
29 6 7 8
24 4 22
12 1 2 35
predicted action
(b) Predictions emitted (50 total)
Figure 14. What the systems get right, and what they say instead.Rows are the eleven systems ordered by overall accuracy. (a) Recall
per verified class, support 10 each: every system is strongest on the unambiguous ends (ship,revise) and weakest onsegment, where the best
system recovers 4/10 and four systems recover none. (b) The marginal distribution of what each systememitted, against a uniform truth
of 10 per class — a bias fingerprint that is independent of correctness. Values above 10 are over-prediction. Seven of the eleven systems
over-predictmitigate, by up to3.2× its true frequency (32/50, Gemma-3-27B+SFT), and it is the modal prediction of four of them — the
quantitative form of the “over-doom” failure this project has tracked since its local baseline, and the target of the DPO pass in fig. 12. The
segmentcolumn is the mirror image: eight systems emit that action at most twice in fifty attempts.
17

0 20 40 60 80
0
20
40
60
five-way chance, 20%
Qwen3-1.7B
Qwen3-1.7B+SFT
Qwen3-8B
Llama-3-8B-Instruct
Llama-3-8B+SFT
Qwen3-8B+SFT
Gemma-3-27B-it
Gemma-3-27B+SFT
Qwen3-32B
Qwen3-32B+SFT→DPO
Qwen3-32B+SFT
peak VRAM at inference (GB, bf16+adapter)
Gold-50 accuracy (%)
Figure 15. Cost–quality frontier over all eleven systems.• fine-tuned, ■ untuned; grey lines join each backbone to its own adapter.
Per-system throughput and latency are in table 11. All three cost measures are instrumented during the archived-run benchmark; accuracy
is the Gold-50 figure. Memory spans16×, from 4.32GB to 69.13GB, and every system fits on one B200 (183GB), so the deployment
question is throughput and latency rather than capacity. The frontier is flatter than the leaderboard suggests: the untuned Qwen3-8B base
reaches 54% at 17.7GB and 46.6tok/s, within 8pp of the leader (the Qwen3-32B LoRA-SFT; not significant,𝑝=0.424 paired, section 5.1)
for a quarter of the memory and over three times the throughput. Note that every adapter sitsright-and-slowerthan its own base: fine-tuning
costs throughput at every scale (table 11).
reaction (28) regulatory (11) readiness (7) business (4)
0
20
40
60
80
100
accuracy on stratum (%)
Qwen3-32B + LoRA-SFT Qwen3-32B + SFT→DPO Llama-3-8B + LoRA-SFT
Qwen3-32B Qwen3-8B Qwen3-8B + LoRA-SFT
Figure 16. Accuracy by what actually drove the outcome.Each
Gold-50 case is annotated during verification with the mechanism
that decided it: publicreaction,regulatoryaction, engineering
readiness, orbusinessperformance (stratum sizes in parentheses).
Theorderingisstableacrosssystems: casesdecidedbyregulatorsor
by shipping-readiness are predicted far better than cases decided by
how loudly users complained. This is the honest limit of a reaction-
simulating pipeline — the stratum it is architecturally aimed at is
the stratum it does worst on. The small strata (𝑛=7 and𝑛=4 )
carry very wide intervals and we draw no ranking conclusions from
them.
Costandserving.Figure15isthecost–qualityfrontierand
Table 11 the measured inference cost of every system—peak
memory, throughput, thinking-token count and end-to-end
latency—read directly from the archived-run benchmark
summaries. Figure17isolatesthethroughputandlatencytax
offine-tuningonthefivebackboneswetrained: theunmerged
LoRA adapter costs tokens per second at every scale, and the
reasoning trace SFT induces costs further latency per case.
The practical reading, consistent with Section 5.8, is that the
quality frontier is flat enough that the deployment choice is
dominated by these serving costs rather than by a few points
of Gold-50 accuracy.
Table 11.Measured inference cost for every system on the leader-
board, from the archived-run benchmark. “tok/s” and “s/case” are
sequential single-case generation; “think” is the mean count of
reasoning tokens emitted before the JSON, which is why the tuned
rows are slower per case than their throughput alone implies. “wall”
is a separate measurement: the end-to-end clock for the batched
Gold-50 run at batch 16, so it is not comparable tos/case×50 .
Every configuration fits on one B200.
System Acc tok/s VRAM s/ think wall
% GB case tok s
Qwen3-32B + SFT→DPO 62 17.6 68.04 133 541 962
Qwen3-32B + LoRA-SFT 62 13.7 69.13 178.9 604 1027
Llama-3-8B + LoRA-SFT 60 28.8 18.03 278.5 544 2607
Qwen3-32B 56 24.3 67.97 90.1 517 1255
Qwen3-8B 54 46.6 17.7 40.3 527 328
Gemma-3-27B + LoRA-SFT 50 12.2 58.66 177 546 1618
Qwen3-8B + LoRA-SFT 50 24.1 18.34 96.8 481 1963
Qwen3-1.7B 46 59.7 4.32 27.7 412 209
Gemma-3-27B-it 36 17.2 58.53 101.5 0 535
Llama-3-8B-Instruct 16 62.5 17.81 127.9 0 2327
Qwen3-1.7B + LoRA-SFT 6 38 4.96 182.2 647 1587
Full debias grid.Table 10 gives the complete debias2×2
for all fourteen systems, each under both arms, summarized
inSection5.3: baselineversusthetaxonomy-definingprompt
block, with accuracy, the paired McNemar𝑝, and themit-
igate/segmentshifts that drive it. It is the source table for
every debias number quoted in the body.
18

0
20
40
60
80
60 63
47
17
24
38
29 24
12 14
tokens/s
(a) Throughput
Qwen3-1.7B
Llama-3-8B-Instruct
Qwen3-8B
Gemma-3-27B-it
Qwen3-32B
0
100
200
300
28
128
40
102 90
182
279
97
177 179
seconds/case
(b) Latency
Figure 17. Fine-tuning costs throughput and latency on every
backbone we trained.■ untuned base,■ the same backbone with
its LoRA-SFT adapter. Same recipe, same data, measured on the
same hardware. (a) Tokens per second falls for all five backbones
— worst on Llama-3-8B-Instruct, to 46% of its untuned rate —
because the unmerged LoRA adapter adds work at every forward
pass. (b) Seconds per case rises further still, because SFT also
taught the models to emit a reasoning trace before the JSON: the
two backbones that emittednothinking tokens untuned (Llama-3-
8B-Instruct, Gemma-3-27B-it) emit 544 and 546 after it (table 11).
The+44pp accuracy gain on Llama-3-8B (table 2) therefore costs
2.2× the latency per case, which is the trade a deployment actually
faces.
References
[1] J. S. Parket al., “Generative Agents: Interactive Simulacra of
Human Behavior,” inProc. ACM UIST, 2023.
[2] G. Li, H. Hammoud, H. Itani, D. Khizbullin, and B. Ghanem,
“CAMEL: Communicative Agents for ‘Mind’ Exploration of
Large Language Model Society,” inNeurIPS, 2023.
[3] Z. Yanget al., “OASIS: Open Agent Social Interaction Simu-
lations with One Million Agents,”arXiv:2411.11581, 2024.
[4] M. H. DeGroot, “Reaching a Consensus,”J. Amer. Statist.
Assoc., vol. 69, no. 345, pp. 118–121, 1974.
[5] N. E. Friedkin and E. C. Johnsen, “Social Influence and
Opinions,”J. Math. Sociol., vol. 15, no. 3–4, pp. 193–206,
1990.
[6] R. Hegselmann and U. Krause, “Opinion Dynamics and
Bounded Confidence: Models, Analysis and Simulation,”
JASSS, vol. 5, no. 3, 2002.
[7] P. Lewiset al., “Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks,” inNeurIPS, 2020.
[8] D. Edgeet al., “From Local to Global: A Graph RAG Ap-
proachtoQuery-FocusedSummarization,”arXiv:2404.16130,
2024.
[9] A. Panickssery, S. R. Bowman, and S. Feng, “LLM
Evaluators Recognize and Favor Their Own Generations,”
arXiv:2404.13076, 2024.
[10] G.Hinton,O.Vinyals,andJ.Dean,“DistillingtheKnowledge
in a Neural Network,”arXiv:1503.02531, 2015.
[11] Y. Kim and A. M. Rush, “Sequence-Level Knowledge Distil-
lation,” inEMNLP, 2016.
[12] A. Gudibandeet al., “The False Promise of Imitating Propri-
etary LLMs,”arXiv:2305.15717, 2023.
[13] E. J. Huet al., “LoRA: Low-Rank Adaptation of Large
Language Models,” inICLR, 2022.
[14] R. Rafailovet al., “Direct Preference Optimization: Your
Language Model is Secretly a Reward Model,” inNeurIPS,
2023.
[15] M. Sclar, Y. Choi, Y. Tsvetkov, and A. Suhr, “Quantifying
LanguageModels’SensitivitytoSpuriousFeaturesinPrompt
Design,” inICLR, 2024.
[16] M.Mizrahietal.,“StateofWhatArt? ACallforMulti-Prompt
LLM Evaluation,”TACL, vol. 12, 2024.
[17] E. B. Wilson, “Probable Inference, the Law of Succession,
and Statistical Inference,”J. Amer. Statist. Assoc., vol. 22,
no. 158, pp. 209–212, 1927.
[18] Q. McNemar, “Note on the Sampling Error of the Difference
Between Correlated Proportions or Percentages,”Psychome-
trika, vol. 12, no. 2, pp. 153–157, 1947.
[19] S. Holm, “A Simple Sequentially Rejective Multiple Test
Procedure,”Scand. J. Statist., vol. 6, no. 2, pp. 65–70, 1979.
[20] Y. Benjamini and Y. Hochberg, “Controlling the False Dis-
covery Rate: A Practical and Powerful Approach to Multiple
Testing,”J. Roy. Statist. Soc. B, vol. 57, no. 1, pp. 289–300,
1995.
[21] Qwen Team, “Qwen3 Technical Report,”arXiv:2505.09388,
2025.
[22] A. Grattafioriet al., “The Llama 3 Herd of Models,”
arXiv:2407.21783, 2024.
[23] Gemma Team, “Gemma 3 Technical Report,”
arXiv:2503.19786, 2025.
19
