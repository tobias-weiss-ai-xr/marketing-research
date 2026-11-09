---
title: 'Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization'
url: https://arxiv.org/abs/2609.01861
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yuhan Chen
- Zhihua Tian
- Mahavir Dabas
- Charith Peris
- Rahul Gupta
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01861
pages: 15
chars: 69339
fetched_at: '2026-11-08T13:35:11+00:00'
kb_version: 1
---

# Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization

Belief-Calibrated Optimization:
An Explicit World Model for Agentic Optimization
Yuhan Chen1, Zhihua Tian1, Mahavir Dabas1, Charith Peris2, Rahul Gupta2,
Ming Jin1, Feiyang Kang1, Siyuan Zhang3, Nan Wang3, Ruoxi Jia1
1Virginia Tech,2Amazon, 3Independent Researcher
Abstract
The performance of an LLM agent depends on thescaffold
aroundafrozenmodel.Acommonwaytoimprovethatscaffold
istouseacodingagentasanoptimizer:itreadscurrentscores
and traces and iteratively edits the source, producing a new
candidateeachround.Eacheditischosenaccordingtoabelief
about how the environment will respond: what went wrong,
andwhichchangeshould help.Thatbelief istypicallyimplicit.
It lives in the coding agent’s reasoning on the current call,
or remains latent in its parameters, rather than as something
written down. Later calls therefore see scores and traces, but
they do not use that belief. We introduce Belief-Calibrated
Optimization (bco), a method that writes that belief down
as a persistent in-context document and continually revises
that document as new candidates are evaluated. The resulting
document is aworld model: the current account of how the
environmentrespondstoedits.Addedtoanotherwisestandard
loop,bcoreaches a higher train passrate than a matched
control that lacks only the world model, on five benchmarks
spanningmemoryQA,tool-useQA,code-as-actionappagents,
and terminal agents. The gap remains on every held-out split,
which is not used to select the candidate. After a target-model
swap,inwhichthefrozenmodelisreplacedandthescaffoldis
not,theselectedbcoscaffoldleadsonthetaskswetest,except
where context-window overruns leave it unfinished. An offline
ablationthenaskswhetherthatgapcomesfromwhattheworld
modelsays.Afreshpredictorgiventheaccumulateddocument
forecasts how the environment will respond more accurately
than predictors given either no document or a same-form copy
whose content has been falsified. The comparison indicates
that the document carries reusable information in its content,
not only in its form.
1 Introduction
The performance of an LLM agent is determined by both
its weights and thescaffoldaround them. Strong models are
typically served as frozen, closed endpoints, so the scaffold
is what a practitioner can actually change. A recent line of
work uses a coding-agentproposeras an optimizer: it reads
the current scaffold’s scores and traces, diagnoses what went
wrong, and edits the source to produce a new candidate,
whose evaluation outcome then informs the next round (Hu,
Lu, and Clune 2024; Zhang et al. 2024; Yang et al. 2023; Lee
et al. 2026; Chen et al. 2026; Liu et al. 2026; Zhang et al.
Correspondence to: yuhan@vt.edu
2025). Throughout, the frozen model is not updated; only the
surrounding program evolves.
Each edit is chosen according to a belief about how the
environmentwillrespond:wherethebottleneckis,andwhich
changeshouldhelpwhichtasks.Thatbelieftypicallyremains
in the proposer’s reasoning or parameters, so later rounds see
scores and traces without using the belief that produced the
last edit.
WeintroduceBelief-CalibratedOptimization(bco),which
writes that belief down as a persistent in-context document
and continually revises that document as new candidates are
evaluated(Figure1).Theresultingdocumentisaworldmodel:
the current account of how the environment responds to edits.
Withinarunthetargetmodel,tasks,andevaluationstayfixed,
so how the environment responds can be accumulated rather
than relearned. This is the setting of a Bayes-Adaptive MDP,
from which we inherit one fact: what to carry forward is a
belief about that response (Duff 2002; Ghavamzadeh et al.
2015).
Our contributions are as follows:
1. Belief-CalibratedOptimization.Wepresentbco,which
maintains a world model as a persistent in-context docu-
ment (§3).
2. Gains across four task families, and evidence for the
mechanism behind them.Against a matched control
that lacks only the world model,bcoreaches a higher
trainpassrateonallfivebenchmarks,andthegapremains
on every held-out split. After a target-model swap, the
selected scaffold leads on the tasks we test, except where
context-window overruns leave it unfinished. An offline
ablation indicates that a fresh predictor given the ac-
cumulated document forecasts environmental responses
more accurately than predictors given no document or a
same-form copy whose content has been falsified, so the
reusable information is in the content, not only the form
(§4).
2 Iterative Agentic Optimization
We defineagentic optimizationas an iterative process in
which an LLM-based agent improves an artifact by propos-
ing modifications, evaluating their outcomes, and using the
resulting evidence to guide subsequent proposals. An artifact
may be a prompt, program, workflow, or agent scaffold. At
arXiv:2609.01861v1  [cs.AI]  1 Sep 2026

Figure 1:Overview of BCO.vanilla(top) updates the scaffold from scores and traces.bcomaintains a persistent world model
and repeats three steps: predict task-level effects before evaluation (1), apply and evaluate a mechanism-level edit (2), and correct
beliefs from observed traces (3).
iteration t the proposer sees the artifacts already evaluated
and chooses one as the parent to edit. An editat of that
parent yields a new candidatext. The environment evaluates
xt on a fixedscoredtask set Q, drawn once from a task
distribution Q,andreturnsanoutcome ot:anaggregatescore,
task-level results, execution traces, and tool outputs. After
T iterations the optimizer returns one of the candidates it
actually evaluated, selected by the only utility it can observe:
ˆx= arg max
x∈{x1,...,xT }
bUQ(x), bUQ(x) =U(x) +ε x,(1)
where U denotes the population utility overQ. In our experi-
ments, it is estimated on a held-out task set disjoint fromQ.
The noise termεx collects split-specific and evaluation noise.
Selecting on bUQ while being judged onU is the optimizer’s-
curse setting (Smith and Winkler 2006): the candidate that
scores highest onQ is the one whoseεx is most favourable,
so hill-climbing bUQ alone can lose utility onQ. An explicit
model of the environment is meant to help the proposer tell a
real effect from a favourableεx.
3 Belief-Calibrated Optimization
3.1 Overview
How the environment will respond to an edit is unknown
at the start of a run. Within a run the frozen target model,
the scored setQ, and the evaluation procedure stay fixed,
so each outcome remains evidence about the same response.
bcocarries a belief about that response as a persistent world
model Wt. This unknown-but-fixed response, in this loop, is
the setting of a Bayes-Adaptive MDP, from which we inherit
the decision to carry a belief (Duff 2002; Ghavamzadeh et al.
2015). Figure 1 illustrates the overall workflow ofbco. At
iteration t,theoptimizerconsidersthepriorinteractionhistory
ht (artifacts, edits, scores, and traces so far) andWt, chooses
a parent from those artifacts, and proposes an edit:
at ∼π opt (· |ht, Wt).(2)
That edit yields a new candidate. Before evaluation, the
optimizer records a prediction for that candidate at the granu-
larity supported by the protocol (typically a task subset). The
candidate is then executed to obtain scores and traces.
Beforethenextiterationbegins,bcocomparesthepredicted
andobservedcandidateoutcomesandusestheirdiscrepancies
to update the world model:
Wt+1 = Update

Wt, bOt,O t

,(3)
where bOtand Otdenotethepredictedandobservedoutcomes,
respectively. The predictionbOt is included because it makes
the update local. It specifies which beliefs were staked on
the candidate and what outcomes they implied. The resulting
discrepancy can therefore identify the beliefs implicated by
theobservedoutcome,ratherthanmerelyindicatingthatsome
revision is necessary. The calibratedWt+1 is then provided
to the optimizer when proposing the next candidate.bcothus
retains the standard propose-and-evaluate optimization loop
whilemaking thebeliefsbehindcandidate generation explicit
and continually revising them against experimental evidence.
Instantiation. Wt is a single Markdown document,
world_model_calibration.md, copied into the pro-
poser’s workspace at the start of an iteration and written
back at its end. The proposer’s instructions are aSKILL.md
file assembled by including other files. One included file,
thecalibration module, tells the proposer how to maintain
that document and how to run the predict–observe–correct
loop.Removingthisincludeyieldsvanilla,usedasthecom-
parison method throughout our experiments. Both methods
receive thesame evidence surface: every previous iteration’s
diff, evaluation output, traces, and full source snapshot, plus
the cross-iteration task–score matrix, all readable on demand.
vanillalacks a persistent place to record its conclusions, so
each of its calls must reconstruct its understanding from the
raw evidence.

3.2 Belief Construction
The documentWt records reusable beliefs formed from the
current artifact, task-level scores and traces, and previous
candidate evaluations. We distinguishexecution beliefsfrom
evaluation beliefsaccording to which part of the environ-
ment’s response they describe.
• Execution beliefscharacterize how an edit is expected
to affect agent behavior under particular conditions. They
connect properties of themodel, current scaffold, task, and
externalenvironmenttoanticipatedchangesintheexecution
trajectory.Forexample,theymaycapturearecurringmodel
limitation, a bottleneck in the current scaffold, a capability
required by a class of tasks, or a constraint imposed by an
externaltool.Thesebeliefshelptheoptimizerestimatehow
a candidate edit is likely to affect agent behavior and task
performance.
• Evaluationbeliefscharacterizehowreliablytheevaluation
systemmapsanexecutiontrajectorytoanobservedoutcome.
They record recurring limitations or errors of the evaluator
revealed by previous evaluations, as well as the conditions
under which its feedback may be unreliable. These beliefs
help the optimizer account for evaluation limitations when
comparing predicted and observed performance.
We representWt as a collection of atomic beliefs:
Wt ={β t,i}mt i=1,
βt,i =

ϕt,i,C t,i, ct,i, st,i, E+ t,i, E− t,i, µt,i  , (4)
where ϕt,i is a falsifiable claim about the execution or eval-
uation process, Ct,i specifies the conditions under which
it applies, ct,i ∈[0,1] denotes its confidence, st,i ∈
{hypothesis,confirmed,refuted} its status, E+ t,i and E− t,i
record supporting and contradictory evidence, andµt,i is
themassof the belief: the approximate number of observed
failuresitexplains.Thisquantityhelpsprioritizeexperimental
budgetacrossbeliefs. mtisthenumberofbeliefsiniteration t.
Scores and trace events provide the evidence for these beliefs,
while the beliefs themselves capture explanations and gener-
alizations that can inform future candidate generation.bco
retains a task-specific diagnosis inWt only when it supports
such a reusable claim. In the document these atoms are its
Beliefssection, one entry perβt,i, beside anExperiments
section recording which edits already probed each belief and
with what verdict, so an edit that paid no information or gain
is not tried again. The document startsempty: it is filled only
from the run’s own evidence, and pre-seeding guessed failure
modes is forbidden, since that would place confidence on
claims no observation supports.
3.3 Belief Calibration
After evaluation, the proposer compares the prediction with
the observed outcome and updatesWt one belief at a time.
Beliefs that this outcome does not address are left unchanged.
The update is a short list of operations onWt:
∆Wt = (δ1, . . . , δkt ),
δj ∈ {Add,Revise,Merge,Remove},
Wt+1 = Apply(Wt,∆W t).
(5)
Addinserts a new belief.Revisechanges an existing belief’s
claim, scope, confidence, status, or evidence.Mergecom-
bines overlapping beliefs.Removedeletes a belief that the
accumulated evidence has refuted.
This update runs at the start of the next iteration, before
a new edit is chosen. The proposer first grades the previous
prediction fileprediction.md against the raw outcome,
using per-task results relative to the parent and the execution
traces, not the scaffolded agent’s final message. It applies
∆Wt to the Beliefs section and appends one record to an
append-onlyHistory,soarefutedbeliefremainsontherecord.
It then chooses the next edit: a probe of an uncertain belief,
or an action on a well-supported one. Only then does it write
the nextprediction.md, before any source change.
The prediction names the belief at stake, the mechanism of
the edit, and a claim about asubsetof tasks. The candidate
code remains general: a prediction may name task IDs, but
the source may not branch on them.
Example 1 instantiates this loop on GAIA; Listings 2–3
give the same files verbatim.
Example 1 (GAIA, iterations 15–16)
Predict.At iteration 15, the world model identifies buried
evidenceinlonginteractionhistories.Itpredictsthatanswering
from a compressed evidence summary will improve that long-
context subset by at least0.10.
Observe.That summary recovers five tasks but causes four
regressions: it runs after every episode and replaces main-loop
answers that were already correct.
Correct.Iteration 16 runs the summary turn only when the
main-loop answer is empty or a placeholder, and accepts only
aconcreteoutput.Fivemoretaskspass,noneregress,andtrain
passrate rises from0.450to0.575.
Algorithm 1 in Appendix A states the complete procedure,
marking whatbcoadds relative tovanilla. Appendix B
gives the fragment sizes, the grading axes, and one instance
of each artifact.
4 Experiments
We organize the evaluation around three questions.RQ1
asks whetherbcodiscovers stronger scaffolds and whether
their gains persist on held-out tasks (§4.2).RQ2asks how
the resulting scaffolds behave when the frozen target model
is replaced by an unseen model (§4.3).RQ3asks whether
the accumulated world model contains reusable information
abouthowscaffoldeditsaffecttaskbehavior(§4.4).Westudy
these questions with matched optimization runs across five
benchmarks, target-model swaps, and a controlled offline
prediction ablation.
4.1 Experimental Setup
Matched comparison.For each benchmark, the two meth-
ods share the initial scaffoldx0, the editable source surface,
the frozen targetM (the open-weight model DeepSeek-V4-
Flash on the memory, tool-use, and code benchmarks, and
MiniMax-M3 on Terminal-Bench 2.0; frozen within every
matched pair), the train/test split, the evaluation harness, and
the iteration budgetT. Both methods start from the same

iteration-0 artifact; the comparison measures the protocol-
leveleffectofaddingthecalibrationlayerin§3.1.Theproposer
is a fixed strong coding LLM at maximum reasoning effort
and runs in a sandbox1; it is identical across the two methods
within each matched pair.
Benchmarks and splits.We evaluate on five benchmarks
spanning four task families.
• Memory QA:LongMemEval-s(LME) (Wu et al. 2025)
(train100/test400)andLoCoMo(Maharanaetal.2024)
(train 80 / test 1449) test memory across long, multi-
session conversations, including temporal and causal rea-
soning;thescaffoldisalong-term-memoryontologywith
retrieval and context packing.
• Tool-use QA:GAIA(Mialon et al. 2024) (train 40 /
test 99) poses real-world questions requiring reasoning,
browsing, multimodal understanding, and tool use; the
scaffold is a function-calling loop over real tools.
• Code-as-action agents:AppWorld(Trivedi et al. 2024)
(a scenario-disjoint train 45 / test 372 split drawn from
the challenge pool, so no test scenario is seen in training);
the scaffold is a ReAct code agent that completes tasks in
simulated everyday apps by writing Python against the
environment’s APIs.
• Terminal agents:Terminal-Bench 2.0(TB2.0) (The
Terminal-Bench Team 2026) (train 20 / test 66) contains
realistic, execution-verified command-line tasks; the scaf-
fold is a terminal-use agent loop (Terminus-2) driving a
live shell in a sandboxed container.
Because train score guides the search, we apply a pre-
optimization stability screen before fixing the AppWorld
and Terminal-Bench 2.0 train subsets. The screen removes
oscillatingtasks whose repeated trials disagree under an
identical scaffold, providing a more consistent optimization
signal. Appendix C documents the screen, the Spider2-lite
diagnostic, and results on the initial Terminal-Bench split.
Graders.Each benchmark keeps its own standard grader,
fixed across methods and identical on train and held-out; Ap-
pendixCliststhem.Candidatesareevaluatedattemperature0,
one repeat per task except Terminal-Bench 2.0 (k=2).
Metric and candidate selection.The reported number
is held-out passrate. On GAIA, AppWorld and Terminal-
Bench 2.0 each method contributes its top-1 train-frontier
candidate, ties broken by the earliest iteration. Both memory
benchmarks run 30 iterations, and their large headroom over
theinitialscaffoldleavesagroupofcandidatesbunchedatthe
top of the train split; there each method’sthreehighest-train
candidates are evaluated held-out and the best is reported.
That procedure selects partly on the held-out split, so the
two memory rows report best-of-three estimates. The same
selection rule is applied to both methods, and Appendix C
lists every evaluated candidate with its train and held-out
score. Appendix F provides a complementary three-method
1Concretely, the memory-QA runs use Kimi-K2.6, GAIA and
AppWorld Kimi-K2.7, and the Terminal-Bench 2.0 pair a Codex
proposer (GPT-5.6 at maximum reasoning effort).
diagnostic with free-form persistent notes, and Appendix E
reports proposer token usage.
4.2 RQ1: Does BCO Improve Optimization and
Held-Out Performance?
This experiment measures both search progress and gener-
alization. The best-so-far train passrate shows how far each
optimizermovesthescaffoldonthesplitthatguidesitssearch;
the held-out passrate shows whether the selected scaffold re-
tains that improvement on unseen tasks. We comparebco
withvanillaunder the matched protocol of §4.1 across all
five benchmarks.
Optimizationresult.Bothmethodsraisetrainpassrateover
the initial scaffold. On every benchmark,bcoends higher
thanvanilla(left halfof Table 1),from +0.025onTB2.0 to
+0.150on GAIA. Figure 2 shows the best-so-far trajectory.
Held-out result.Each method’s selected candidate is then
evaluatedonthesplitunusedforsearch(righthalfofTable1).
Held-out passrate is lower than train on every row. The
ordering is unchanged:bcoremains higher thanvanilla,
from+0.022(TB2.0) to+0.152(GAIA).
4.3 RQ2: How Do the Scaffolds Transfer to an
Unseen Target Model?
Scaffold edits can depend on the target used during optimiza-
tion.Wethereforeholdeachselectedartifactandtheheld-out
tasks fixed, and replace only the target with a model from
a different family and provider. The comparison separates
scores under the original target from scores after that swap.
Protocol.For GAIA and AppWorld, we re-evaluate the
initial artifact and thevanillaandbcoselected candidates
from Table 1, using each run’s original source snapshot. The
newtargetisgpt-5.6-luna,ateachofitsthreereasoning-effort
tiers (high, medium, and low). On GAIA the agent loop is
capped at 30 iterations for all three scaffolds, because the
swapped target takes more turns per task. Figure 3 reports
twosets:thefullsplit,countinganon-completionasafailure,
and the tasks that all three scaffolds complete. Exact values
are in Appendix D (Table 6).
GAIA.All three scaffolds complete every task, so the two
sets coincide.bcohas the highest passrate at high, medium,
andloweffort(Figure3).Athigheffort,vanillascored 0.111
below the initial scaffold. The traces show longer searches
that overwrite answers found earlier in the trajectory; this
study does not isolate that mechanism.
AppWorld.The two sets diverge. Thebcoscaffold re-
injects its entire natural-language scratchpad at every turn,
with no length bound. That design stays within the context
budget of the original, terser target, but not of the more
verbose swapped target: the scaffold returns no output on
99/77/65 of the372 tasks at high/medium/low effort. The
initial andvanillascaffolds complete every task;vanilla
keeps a sliding window of16 recent exchanges. Counting
non-completions as failures,bcoscores 0.516, 0.524, and
0.532 versus 0.685, 0.608, and0.538 forvanilla, sobcois
last at high and medium effort and matchesvanillaat low

0 10 20 30
0.00
0.25
0.50
0.75
1.00
train passrate
(best-so-far)
LongMemEval-s
0 10 20 30
LoCoMo
0 10 20
iteration
GAIA
0 5 10
AppWorld
0 5 10
Terminal-Bench 2.0
BCO Vanilla held-out (marker, Table 1)
Figure 2: Best-so-far train passrate by iteration (lines); stars mark the held-out passrate of each selected candidate.bcofinishes
higher thanvanillaon both train and held-out across all five benchmarks.
H M L
0.0
0.4
0.8Passrate
(a) GAIA
H M L
(b) AppWorld
Initial V anilla BCO
Figure3:Target-modelswaptogpt-5.6-lunaatthreereasoning-
effort tiers (H/M/L). Solid bars include all tasks and count
non-completions as failures; hatched extensions restrict to
tasks completed by all three scaffolds. See Appendix D
(Table 6) for exact values and completion counts.
effort. Restricting to tasks all three complete,bcois first at
every tier, by+0.007,+0.031, and+0.091. The completed-
runorderingisconsistentwithatransferabletaskstrategy;the
full-set ordering shows that transfer also depends on context
consumption.
4.4 RQ3: Does the World Model Carry Predictive
Information?
Train and held-out scores measure the scaffold, not what the
world model contains. We therefore freeze each candidate
and its realized outcome, and vary only the document given
to a predictor that did not design the candidate. The predictor
forecasts, for each question type, whether that candidate’s
edit will help (Upside) or hurt (Downside).
Protocol.All predictors receive the same parent
source, diff, and base per-type passrates.Nonere-
ceives no document;Intactreceives the run’s final
world_model_calibration.md with that candidate’s
outcome block removed;Scrambledkeeps the file’s length,
format, and vocabulary but falsifies its mechanism verdicts
and type-level effects. Two blind judges compare each pair
of predictions to the realized per-type changes; upside hit
rate and downside precision are a judge-free cross-check
(Appendix G).
Result.Table 2 gives the same ordering on every mea-
sure: None< Scrambled < Intact. Scrambled over None is
consistent with a benefit from structure and from naming
regressions. Intact over Scrambled is consistent with addi-
tional information in the learned content. Both judges agree
with the mechanical metrics; the largest mechanical gap is
downsideprecision.Candidatesarenestedinfourruns,sothe
run is the independent unit (Appendix G; two-sided sign-test
p= 0.125 ). The comparison shows that a predictor that did
not write the document can use its content to forecast out-
comes of candidates from those runs; it does not test whether
the same document would transfer to a new optimization
trajectory.
4.5 Additional Ablation: Persistence Without
Calibration
Theofflineablationisolatesdocumentcontent.Itdoesnottest
whether any persistent file would suffice. On LongMemEval-
s we therefore add a third method,Notes: one freely ed-
itable agent_notes.md that persists across iterations,
with no prediction, grading, or predict–observe–correct up-
date.vanillaremains the comparison method;bcois the
full protocol.
Three independent ten-iteration trajectories per method on
the 100-example training split give means0.430 (vanilla),
0.427(Notes), and0.467(bco), with within-method ranges
0.11, 0.07, and 0.13 (Table 3). Persistence alone does not
reproducebco’s mean on this diagnostic, but three short
trajectories cannot show that free-form notes are ineffective.
The paired held-out comparison and the content-controlled

Table 1: Held-out generalization across five benchmarks. Each method uses the same initial scaffold, editable source, train/test
split, target model, proposer, evaluation harness, and optimization budget. Train and held-out entries are passrates; the held-out
split is never used to optimize the scaffold except for the disclosed best-of-three selection on the two memory benchmarks.
Train Held-out
Benchmark Scaffold Train/Test Target Proposer Initialvanilla bcoInitialvanilla bco
LME Memory retrieval 100/400 DeepSeek- V4-Flash Kimi-K2.6 0.160 0.5900.7100.148 0.5330.608
LoCoMo Memory retrieval 80/1449 DeepSeek- V4-Flash Kimi-K2.6 0.288 0.4120.4750.295 0.3750.453
GAIA Tool-calling 40/99 DeepSeek- V4-Flash Kimi-K2.7 0.400 0.4250.5750.283 0.3430.495
AppWorld ReAct code 45/372 DeepSeek- V4-Flash Kimi-K2.7 0.600 0.8000.9330.694 0.7660.796
TB2.0 Terminus-2 20/66 MiniMax-M3 Codex (GPT-5.6) 0.450 0.5250.5500.477 0.4700.492
World model None Scrambled Intact
Upside hit rate 0.441 0.4600.538
Downside precision 0.142 0.1810.217
Judge wins vs. None — 26–12 / 24–936–4 / 35–2
Judge wins vs. Scrambled — —26–12 / 26–12
Table 2: Offline prediction ablation on 40 candidates. Upper
rowsarejudge-free;lowerrowsreportblindwins–lossesunder
Kimi-K2.6 / DeepSeek-V4-Flash. Ties are excluded. Because
candidates are nested within four optimization runs, the run
is the independent unit; all four runs favor the same ordering,
giving a two-sided sign-testp= 0.125(Appendix G).
ablation remain the primary evidence.
5 Related Work
LLM-drivenoptimizationoftheprogramaroundafrozen
model.Closest to our setting is work that optimizes the
harness: end-to-end harness optimization (Lee et al. 2026),
composable and evolvable foundries (Chen et al. 2026), sus-
tained self-improvement on open-ended task streams (Liu
et al. 2026), accelerated self-evolution loops (Hu et al. 2026),
and dedicated evaluation environments (Zheng et al. 2026),
extending earlier agents that rewrite their own scaffold or
code (Zhang et al. 2025; Yin et al. 2024; Shang et al. 2024;
Zhou et al. 2024; Zweiger et al. 2025). A parallel line opti-
mizesagentsystemsandprompts:agentic-systemdesign(Hu,
Lu, and Clune 2024), graph-structured topologies (Zhuge
et al. 2024), workflow generation (Zhang et al. 2024), LLM-
as-optimizer (Yang et al. 2023) and evolutionary (Guo et al.
2023; Fernando et al. 2023) prompt search, and compiling
declarativeLMprogramsbyoptimizingtheirinstructionsand
demonstrations(Khattabetal.2023;Opsahl-Ongetal.2024).
These methods show that an LLM can improve the program
around a frozen model using observed scores, often together
with free-form reflection, to guide edits over program space.
A concurrent analysis separates producing useful updates
from benefiting from them at solve time and finds update
Method Run 1 Run 2 Run 3 Mean
vanilla0.37 0.44 0.48 0.430
Notes0.43 0.460.39 0.427
bco0.42 0.430.55 0.467
Table3:Persistent-stateablationonLongMemEval-s.Entries
are the best-so-far training passrate over successfully evalu-
atedcandidatesinthreeindependenttrajectories(100training
examples; nominal ten-iteration proposer budget).
quality roughly flat across base-model tiers. This pattern
suggests that theupdate protocol, rather than the evolver’s
raw capability alone, is an important lever (Lin et al. 2026).
Belief-Calibrated Optimization changes what the optimizer
carries from one iteration to the next.
Verbal self-reflection and memory.Agents can also
improve by writing natural-language reflections on their
own behavior—repeated self-feedback on a single out-
put (Shinn et al. 2023; Madaan et al. 2023), tool-verified self-
correction (Gou et al. 2023), a persistent skill library (Wang
et al. 2023), or a streamed memory of experience (Park et al.
2023).Theseapproachesuseepisodicorfree-formmemoryto
retainusefulexperienceacrossinteractions.Belief-Calibrated
Optimizationinsteadorganizespersistentstatearoundexplicit
predictions, observations, and revisions of an environment
model.
POMDPs, Bayes-adaptive RL, and Bayesian optimization.
The setting is that of a Bayes-adaptive MDP: the environ-
ment’sresponseisunknownbutfixedwithinarun,sowhatto
carry between iterations is a belief about that response (Duff
2002; Ghavamzadeh et al. 2015; Åström 1965; Kaelbling,
Littman, and Cassandra 1998). Sample-based planners that
search the belief-augmented state space instantiate the same
idea in parametric form (Guez, Silver, and Dayan 2012).
The optimization loop can also be read as Bayesian opti-
mization (Shahriari et al. 2016): the world model plays a
surrogate-like role, and the choice between probing an un-
certain belief and acting on a well-supported one plays an

acquisition-like role. We instantiate those roles in natural
language and in context, without a parametric surrogate or
a learned solver. That choice follows the view of in-context
learning as implicit Bayesian inference (Xie et al. 2021).
6 Conclusion
Belief-Calibrated Optimization writes the optimizer’s belief
about how the environment responds to edits as a persistent
world model, and revises that document by predict–observe–
correct. On five benchmarks spanning memory QA, tool-use
QA, code-as-action app agents, and terminal agents,bco
reaches a higher train passrate thanvanillaand keeps that
gap on every held-out split.
When the target is replaced with an unseen model, thebco
scaffold ranks first across all GAIA settings and on the com-
moncompleted-tasksetsinAppWorld.Itsunboundedcontext
use, however, reduces full-set AppWorld performance. A
fresh predictor given the accumulated world model also fore-
casts outcomes more accurately, indicating that the document
contains information usable beyond the run that produced it.
More broadly, an optimizer’s knowledge of its environment
neednotremainimplicitanddisposable.Whenmadeexplicit,
falsifiable, and calibration-tracked, it becomes an artifact that
can be maintained and improved.
7 Limitations
• The belief is approximate, and its self-assessment is
heuristic.The world model Wt is an LLM’s natural-
language summary of evidence, not a statistically cali-
brated posterior. Our analysis therefore focuses on de-
noised, subset-averaged behavior, since single-task pass/-
fail sits below the evaluation noise floor; raising the per-
task repeat count would admit stable single-task claims at
proportionally higher cost.
• Theenvironment’sresponseistreatedasfixedwithina
run,andthescaffoldcanoverfitthetarget.Wefreezethe
target model and the benchmark for a run, so the response
does not drift by design. A target swap or external-tool
driftchangestheresponseandwouldrequiredetectingthe
shift and discounting older evidence, which the current
protocol does not include. The AppWorld transfer result
in §4.3 also shows that target-dependent resource use can
affectfull-setperformance.Futurevariantscouldoptimize
against multiple targets or score a candidate’s resource
envelope alongside its passrate.
• The evaluation covers five screened benchmarks.Four
benchmarks share one proposer family and one target
model, while Terminal-Bench 2.0 uses an independent
stack. Each matched comparison contains one trajec-
tory per method, so the aggregate evidence measures
consistency across five benchmarks rather than within-
benchmarkrepetition;thetransferstudychangesthetarget
atevaluationtime.Wealsoscreenedinitial-scaffoldbehav-
ior before fixing the AppWorld and Terminal-Bench 2.0
train subsets, which narrows the claim to environments
with sufficient repeatable failure mass and may favor
benchmarks on which score-guided optimization is easier
(Appendix C).

References
Åström, K. J. 1965. Optimal control of Markov processes
with incomplete state information.Journal of Mathematical
Analysis and Applications, 10(1): 174–205.
Chen, T.; Lu, S.; Zhao, K.; Meng, W.; Teng, H.; Li, T.; Li,
C.; Liu, X.; Liang, J.; Zhang, Z.; Xie, Y.; Qu, H.; Shao,
K.; and Luan, J. 2026. HarnessX: A Composable, Adap-
tive, and Evolvable Agent Harness Foundry.arXiv preprint
arXiv:2606.14249.
Duff, M. O. 2002.Optimal Learning: Computational Proce-
dures for Bayes-Adaptive Markov Decision Processes. Ph.D.
thesis, University of Massachusetts Amherst.
Fernando, C.; Banarse, D.; Michalewski, H.; Osindero, S.;
and Rocktäschel, T. 2023. Promptbreeder: Self-Referential
Self-Improvement Via Prompt Evolution.arXiv preprint
arXiv:2309.16797.
Ghavamzadeh,M.;Mannor,S.;Pineau,J.;andTamar,A.2015.
Bayesian Reinforcement Learning: A Survey.Foundations
and Trends in Machine Learning, 8(5–6): 359–483.
Gou, Z.; Shao, Z.; Gong, Y.; Shen, Y.; Yang, Y.; Duan, N.;
and Chen, W. 2023. CRITIC: Large Language Models Can
Self-Correct with Tool-Interactive Critiquing.arXiv preprint
arXiv:2305.11738. Published at ICLR 2024.
Guez, A.; Silver, D.; and Dayan, P. 2012. Efficient
Bayes-AdaptiveReinforcementLearningusingSample-Based
Search.Advances in Neural Information Processing Systems,
25: 1034–1042. NIPS 2012.
Guo, Q.; Wang, R.; Guo, J.; Li, B.; Song, K.; Tan, X.; Liu,
G.; Bian, J.; and Yang, Y. 2023. EvoPrompt: Connecting
LLMswithEvolutionaryAlgorithmsYieldsPowerfulPrompt
Optimizers.arXiv preprint arXiv:2309.08532. Published at
ICLR 2024.
Hu, S.; Lu, C.; and Clune, J. 2024. Automated Design of
Agentic Systems.arXiv preprint arXiv:2408.08435.
Hu,Z.;Lu,M.;Wang,Z.;Ruan,J.;Chen,C.;Pan,Z.;Guan,Y.;
Wang,R.;Yu,Z.;Zhang,C.;andDing,Y.2026. FlashEvolve:
Accelerating Agent Self-Evolution with Asynchronous Stage
Orchestration.arXiv preprint arXiv:2605.08520.
Kaelbling, L. P.; Littman, M. L.; and Cassandra, A. R. 1998.
Planningandactinginpartiallyobservablestochasticdomains.
Artificial Intelligence, 101(1–2): 99–134.
Khattab, O.; Singhvi, A.; Maheshwari, P.; Zhang, Z.; San-
thanam, K.; Vardhamanan, S.; Haq, S.; Sharma, A.; Joshi,
T.T.;Moazam,H.;Miller,H.;Zaharia,M.;andPotts,C.2023.
DSPy: Compiling Declarative Language Model Calls into
Self-Improving Pipelines.arXiv preprint arXiv:2310.03714.
Lee, Y.; Nair, R.; Zhang, Q.; Lee, K.; Khattab, O.; and Finn,
C. 2026. Meta-Harness: End-to-End Optimization of Model
Harnesses.arXiv preprint arXiv:2603.28052.
Lin, M.; Wu, J.; Wang, Z.; Shi, Z.; Sang, Y.; He, B.; Liu, Z.;
Wei, T.; Wang, D.; Zhang, X.; Dumoulin, B.; Xie, C.; Zhou,
Y.; Wang, S.; and Lu, H. 2026. Harness Updating Is Not
HarnessBenefit:DisentanglingEvolutionCapabilitiesinSelf-
Evolving LLM Agents.arXiv preprint arXiv:2605.30621.
Liu, Z.; Shi, Z.; Sang, Y.; He, B.; Lin, M.; Wei, T.; Wang,
D.; Dumoulin, B.; Jin, W.; and Lu, H. 2026. Adaptive Auto-
Harness: Sustained Self-Improvement for Agentic System
Deployment on Open-Ended Task Streams.arXiv preprint
arXiv:2606.01770.
Madaan, A.; Tandon, N.; Gupta, P.; Hallinan, S.; Gao, L.;
Wiegreffe, S.; Alon, U.; Dziri, N.; Prabhumoye, S.; Yang, Y.;
Gupta,S.;Majumder,B.P.;Hermann,K.;Welleck,S.;Yazdan-
bakhsh, A.; and Clark, P. 2023. Self-Refine: Iterative Refine-
ment with Self-Feedback.arXiv preprint arXiv:2303.17651.
Maharana, A.; Lee, D.-H.; Tulyakov, S.; Bansal, M.; Barbieri,
F.; and Fang, Y. 2024. Evaluating Very Long-Term Conversa-
tional Memory of LLM Agents. InProceedings of the 62nd
Annual Meeting of the Association for Computational Lin-
guistics(Volume1:LongPapers),13851–13870.Association
for Computational Linguistics.
Mialon, G.; Fourrier, C.; Wolf, T.; LeCun, Y.; and Scialom,
T. 2024. GAIA: A Benchmark for General AI Assistants.
InInternational Conference on Learning Representations
(ICLR).
Opsahl-Ong, K.; Ryan, M. J.; Purtell, J.; Broman, D.; Potts,
C.; Zaharia, M.; and Khattab, O. 2024. Optimizing Instruc-
tions and Demonstrations for Multi-Stage Language Model
Programs.arXiv preprint arXiv:2406.11695. Published at
EMNLP 2024.
Park,J.S.;O’Brien,J.C.;Cai,C.J.;Morris,M.R.;Liang,P.;
andBernstein,M.S.2023.GenerativeAgents:InteractiveSim-
ulacra of Human Behavior.arXiv preprint arXiv:2304.03442.
Shahriari, B.; Swersky, K.; Wang, Z.; Adams, R. P.; and
de Freitas, N. 2016. Taking the Human Out of the Loop: A
Review of Bayesian Optimization.Proceedings of the IEEE,
104(1): 148–175.
Shang, Y.; Li, Y.; Zhao, K.; Ma, L.; Liu, J.; Xu, F.; and Li,
Y. 2024. AgentSquare: Automatic LLM Agent Search in
Modular Design Space.arXiv preprint arXiv:2410.06153.
Shinn,N.;Cassano,F.;Berman,E.;Gopinath,A.;Narasimhan,
K.;andYao,S.2023.Reflexion:LanguageAgentswithVerbal
Reinforcement Learning.arXiv preprint arXiv:2303.11366.
Published at NeurIPS 2023.
Smith,J.E.;andWinkler,R.L.2006. TheOptimizer’sCurse:
Skepticism and Postdecision Surprise in Decision Analysis.
Management Science, 52(3): 311–322.
The Terminal-Bench Team. 2026. Terminal-Bench: Bench-
marking Agents on Hard, Realistic Tasks in Command Line
Interfaces. InInternational Conference on Learning Repre-
sentations (ICLR).
Trivedi, H.; Khot, T.; Hartmann, M.; Manku, R.; Dong,
V.; Li, E.; Gupta, S.; Sabharwal, A.; and Balasubramanian,
N. 2024. AppWorld: A Controllable World of Apps and
People for Benchmarking Interactive Coding Agents. In
Proceedings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers),
16022–16076. Association for Computational Linguistics.
Wang, G.; Xie, Y.; Jiang, Y.; Mandlekar, A.; Xiao, C.; Zhu,
Y.; Fan, L.; and Anandkumar, A. 2023. Voyager: An Open-
Ended Embodied Agent with Large Language Models.arXiv
preprint arXiv:2305.16291.

Wu, D.; Wang, H.; Yu, W.; Zhang, Y.; Chang, K.-W.; and Yu,
D. 2025. LongMemEval: Benchmarking Chat Assistants on
Long-Term Interactive Memory. InInternational Conference
on Learning Representations (ICLR).
Xie, S. M.; Raghunathan, A.; Liang, P.; and Ma, T. 2021.
An Explanation of In-context Learning as Implicit Bayesian
Inference.arXiv preprint arXiv:2111.02080. Published at
ICLR 2022.
Yang, C.; Wang, X.; Lu, Y.; Liu, H.; Le, Q. V.; Zhou, D.;
and Chen, X. 2023. Large Language Models as Optimizers.
arXiv preprint arXiv:2309.03409. Published at ICLR 2024.
Yin, X.; Wang, X.; Pan, L.; Lin, L.; Wan, X.; and Wang,
W. Y. 2024. Gödel Agent: A Self-Referential Agent Frame-
work for Recursive Self-Improvement.arXiv preprint
arXiv:2410.04444.
Zhang, J.; Hu, S.; Lu, C.; Lange, R.; and Clune, J. 2025.
Darwin Gödel Machine: Open-Ended Evolution of Self-
Improving Agents.arXiv preprint arXiv:2505.22954.
Zhang, J.; Xiang, J.; Yu, Z.; Teng, F.; Chen, X.; Chen,
J.; Zhuge, M.; Cheng, X.; Hong, S.; et al. 2024. AFlow:
Automating Agentic Workflow Generation.arXiv preprint
arXiv:2410.10762. Published at ICLR 2025.
Zheng, C.; Xue, C.; Liang, B.; Yang, J.; and Zhang, C. 2026.
SEAGym: An Evaluation Environment for Self-Evolving
LLM Agents.arXiv preprint arXiv:2606.17546.
Zhou, W.; Ou, Y.; Ding, S.; Li, L.; et al. 2024. Symbolic
Learning Enables Self-Evolving Agents.arXiv preprint
arXiv:2406.18532.
Zhuge, M.; Wang, W.; Kirsch, L.; Faccio, F.; Khizbullin, D.;
and Schmidhuber, J. 2024. Language Agents as Optimizable
Graphs.arXivpreprintarXiv:2402.16823. PublishedatICML
2024; project name GPTSwarm.
Zweiger, A.; Pari, J.; Guo, H.; Akyürek, E.; Kim, Y.; and
Agrawal, P. 2025. Self-Adapting Language Models.arXiv
preprint arXiv:2506.10943.
A The Optimization Loop
Algorithm 1 is the procedure of Section 3 of the main paper.
Every black line is shared with the matched control; the blue
lines are whatbcoadds.
B The Protocol, Verbatim
This appendix shows the artifacts the main text describes:
what separates the two methods, what a world model and
a prediction actually look like, and how the blind judge of
Section 4.4 of the main paper is configured.
B.1 What separates the two methods
Each proposer is a SKILL.md assembled by textual in-
clusion from three fragments. For the GAIA pair, for
instance, both methods include a 61-line environment
surface (the editable source files and the shape of the
returned outcome) and a 123-line base contract (read
the evidence, design one mechanism-level edit, write
the candidate). Thebcomethod adds one more line,
<!-- INCLUDE: _calib_addon.md --> , pulling in
Algorithm 1 Belief-Calibrated Optimization.bco-specific
operations and inputs are shown in blue; every black line is
shared with the matched control, includingSelectParent,
in which the proposer chooses which previously evaluated
candidate to build on.
Require: Initial artifactx0, scored task setQ, and iteration
budgetT
Ensure:Selected artifactˆxand world modelW
1:o 0 ←Evaluate(x 0, Q);h 1 ←(x 0, o0)
2:W←ConstructBeliefs(x 0, o0)
3:fort= 1, . . . , Tdo
4:x par t ←SelectParent(h t)▷proposer picks any
evaluated ancestor
5:a t ←Propose(x par t , ht, W)
6: bOt ←Predict(W, at, Q)
7:x t ←a t(xpar t );o t ←Evaluate(x t, Q)
8:∆W t ←Calibrate(W, at, bOt, ot)
9:W←Apply(W,∆W t)
10:h t+1 ←h t ∪(a t, ot, xt)
11:end for
12:returnˆx←arg max x∈{x1,...,xT } bUQ(x),W
a 169-line calibration module; thevanillafile is otherwise
identical, including the task description. The module is the
only difference between the two methods. It specifies the
two regions ofworld_model_calibration.md and
their invariants, the predict–observe–correct order within an
iteration,thegradingrule(gradeagainstrawtool-calloutputs
andharnesscontrolflow,nevertheagent’sownfinalmessage;
exclude tasks whose cross-iteration score row disagrees with
itself), the four honest causes a missed prediction can have,
and the template forprediction.md reproduced below.
It imposes no scheduling rule, no coverage quota, and no list
of failure modes to look for.
B.2 The world model
Listing 1 shows theheadof
world_model_calibration.md from the Terminal-
Bench 2.0bcorun at its final iteration, abridged to three of
ninebeliefsandthreeofnineexperimentrecords.Eachbelief
is one instance of the tuple in Eq. 4 of the main paper: claim
ϕ, confidence c, status s, evidence E± given as file paths
into the stored trajectories, and massµ. Evidence strings are
elided at[...]; nothing else is edited.
Listing 1:headof world_model_calibration.md,
Terminal-Bench 2.0, abridged.
## Beliefs
[E3] Byte-exact workspace memory is a material
,→bottleneck when an ordinary stateful
read destroys the only useful input before the
,→solver recognizes the loss; a
concrete loss report plus a recoverable pristine
,→object changes behavior and can
change stable task outcomes
| conf:0.96 | status:confirmed
| evidence:base_eval/dumps/

,→iter003_bounded_workspace_journal/db-wal-recovery/
trajectory.json (steps 3-6: two
,→WORKSPACE_MEMORY_LOSS_DETECTED reports followed
by exact WAL/SHM restoration); seed_eval/[...] (
,→steps 5-8: SQLite removes the
only WAL and the solver begins guessing); [...]
,→ctrf.json (7/7 versus seed 5/7)
| mass:~1
[E4] Comparison-ready artifact history is not a
,→demonstrated bottleneck on this train
split: when a post-command ledger surfaced
,→recoverable candidates, the solver
usually continued the same branch without the
,→requested criterion table
| conf:0.26 | status:refuted
| evidence:reference_iterations/iter_007/dumps
,→/[...]/largest-eigenval/
trajectory.json (checkpoint steps
,→9,18,20,25,28,30 followed by further unranked
rewrites); [...]; task_score_matrix.json (train-
,→fasttext remains stable 0)
| mass:~0
[E9] Repeated external failure output is an earlier and
,→more objective stagnation
signal than plan wording: the same normalized
,→failure can recur across
substantively different commands while the solver
,→continues modifying parameters
| conf:0.91 | status:hypothesis
| evidence:seed_eval/dumps/terminus2_tb2/adaptive-
,→rejection-sampler/
trajectory.json (steps 19,21,23,24,29,30 repeat
,→"failed to accept a sample after
100 iterations" across parameter changes and a
,→rewrite); [...]
| mass:~3
## Experiments
- E3: bounded pre-command content-addressed workspace
,→journal with explicit deletion
/truncation reports -> held (db-wal-recovery
,→moved stably 0->1, the three-task
stable subset mean rose +0.333, and no stable
,→task regressed)
- E4: overwritten/deleted-path variant ledger with a
,→third-version checkpoint -> inert
(the edited source and initial prompt were live,
,→but no checkpoint fired on the
only evaluated target; source inspection shows
,→the ledger compared only
pre-existing paths, so the environment claim
,→remains ungraded)
- E6: post-stall action quarantine -> VOID (the
,→iteration-6 score moved, but no
WORKSPACE_PROGRESS_GATE signature appears in any
,→candidate trace; without a
candidate-distinctive live signature, those
,→numbers do not update E6)
Two features are worth noting because they are what the
protocol asks for rather than what an LLM writes by de-
fault. E4is retained atstatus:refutedinstead of being
deleted,sothedirectionisnotre-proposedlater.The E6entry
recordsacandidatewhosescoremovedbutwhosemechanism
left no trace signature, and refuses to credit the belief with
the movement.
B.3 A prediction and its grading
Listing2is prediction.mdfromiteration16oftheGAIA
bcorun—thecandidatethatbecamethetrain-frontierselected
candidate and the scaffold behind the GAIA row of Table 1
in the main text—and Listing 3 is the distill block appended
at the start of the next iteration, grading it. Both are abridged;
one marker token is rewritten as<|tool_calls|> for
typesetting.
Listing 2:prediction.md, GAIA iteration 16, abridged.
# iter_016 prediction
## Mode
refine -- the ‘long_context / evidence_noise‘ cell is
,→open with one partial attempt
(evidence-summary-memory in iter_015). This round
,→refines the same family by gating the
summary turn on placeholder answers and adding a
,→quality guard, which should eliminate
the regressions while keeping the breakthroughs.
## Candidate
conservative_quality_gated_summary -- after the FC loop
,→, run the evidence-summary
final-answer turn only when the current answer is empty
,→, a <|tool_calls|> marker, or a
placeholder; only adopt the summary answer if it is
,→concrete.
## Base
iter_015 -- I copied the iter_015 source snapshot into
,→the editable tree because the
mechanism is a direct refinement of its evidence-
,→summary-memory scaffold.
## Failure mode attacked
‘long_context / evidence_noise‘ (~10-15 train tasks per
,→the map; attempts so far: 1).
## Assumption audit
Not triggered for this cell (<3 attempts). The lower-
,→layer assumptions are: (1) the
scaffold can extract tool-call results from message
,→history, (2) a compact evidence
summary preserves enough information for the model to
,→answer, and (3) a clean summary
context produces a better final answer than a bloated
,→one for episodes whose main loop
emitted a placeholder.
## Mechanism -- the behavioral change
[...] 5. Adopt the summary answer only if it is non-
,→empty AND not itself a placeholder;
otherwise keep ‘original_answer‘. Any exception during
,→the summary turn also falls back
to ‘original_answer‘. [...] It does NOT change behavior
,→on episodes that already
produced a concrete answer, preventing the iter_015

,→regressions.
## Behavioral prediction (graded from traces)
On the subset, the agent will now keep its concrete
,→direct answers when they exist and
run the clean-context summary turn only when the main
,→loop returns a placeholder/marker.
## Aggregate prediction (graded on the subset, de-
,→noised)
- expected: the subset’s mean stable-pass / mean score
,→rises by >=0.10. This is
plausible if the 5 iter_015 breakthroughs are
,→retained and the 4 regressions are
eliminated by the placeholder gate.
- downside bound: <=1 currently-stable-passing task
,→regresses, enforced by construction.
## Anchors (optional, STABLE episodes only --
,→illustration, not the bet)
No stable anchors are available; the relevant episodes
,→oscillate across iterations due
to endpoint stochasticity and marker noise. The
,→mechanism is justified by the general
failure family, not by a single stable episode.
## Falsification
If long-context level-2 episodes that produced
,→placeholders still fail after the summary
turn, or if concrete-answer episodes regress because
,→the summary turn overwrites them,
the mechanism is refuted.
Listing 3: The distill block grading Listing 2, abridged.
## iter_015 -> iter_016 distill
- Mode: refine
- Behavioral check (self): predicted the agent would
,→gate the evidence-summary turn on
placeholder/empty/marker answers and preserve
,→concrete direct answers. The mechanism
is wired correctly: comparing per-episode traces, all
,→18 tasks that passed in iter_015
also passed in iter_016 (zero regressions), and the
,→final predictions for
previously-regressed tasks like gaia#4fc2f1ae and
,→gaia#3f57289b returned to their
correct direct answers rather than being overwritten
,→by a summary. -> behavior changed
as predicted on the targeted subset.
- Aggregate check (self): ‘long_context /
,→evidence_noise‘ subset (~15-20 episodes) --
predicted the subset would gain and the 4 iter_015
,→regressions would be eliminated.
Actual: 5 additional tasks passed vs iter_015, 0
,→regressions, overall passrate
0.45 -> 0.575. Verdict: works.
- Unstable (multi-run, excluded): many tasks have
,→oscillated across prior iterations due
to marker stochasticity. The zero-regression result
,→vs iter_015 is treated as the
stable signal; individual episode flips are noise.
- Blind-spot regressions: none -- no task that passed
,→in iter_015 failed in iter_016.
- What was learned: Conservative gating is the key to
,→evidence-summary-memory: only run
the summary turn when the main-loop answer is
,→unusable, and only adopt the summary
answer when it is concrete.
- Belief update: ‘long_context / evidence_noise‘ is
,→still the only open, harness-fixable
cell, and it has stable headroom. The remaining
,→placeholder episodes after summary
suggest the summary prompt is too permissive -- it
,→lets the model emit another
"unknown" instead of forcing a best guess.
B.4 Blind-judge configuration
Both judges are run as sandboxed agents, one judgement per
candidate pair, in a fresh context, with no repeats and no self-
consistency voting; there is no temperature sweep, and each
judge runs at the same reasoning-effort setting as the predic-
tors.Thejudgeseesonefile, judge_input.md,containing
the mechanically computed per-type deltas as ground truth
and the two predictions anonymized asPrediction A
and Prediction B ; the A/B assignment is drawn per can-
didate from a generator seeded byseed + iteration ,
and the method-to-label map is stored so the verdict can be
decoded afterwards. The judge never sees which method is
which, the method names, or the world models themselves.
The cross-provider replication replays the byte-identical
judge_input.mdwith the same stored A/B assignment,
so the judge model is the only variable. The instruction is
reproduced in full:
Listing 4: The judge prompt, verbatim.
You are an impartial judge comparing the ACCURACY of
,→two predictions. Read
‘./judge_input.md‘ in your working directory. It
,→contains, for ONE proposed scaffold
change:
- the OBJECTIVE realised outcome (which question types
,→actually improved / regressed,
measured after evaluation -- this is ground truth);
- two independent predictions of that change,
,→anonymised as ‘Prediction A‘ and
‘Prediction B‘.
Decide which prediction was MORE ACCURATE about reality
,→: it named the question types
that truly moved (gains AND regressions), caught the
,→real regressions rather than
missing them, and got the overall net direction right.
,→Penalise predictions that claimed
improvements that did not happen or missed regressions
,→that did. Judge ACCURACY only --
not writing style or how good the patch was.
Write your verdict to ‘./judge_verdict.md‘ with EXACTLY
,→this shape:
WINNER: <A|B|TIE>
REASONING: <2-4 sentences: which types each got right/
,→wrong vs the objective outcome,
and why the winner is more accurate>
A verdict is counted as a tie when the judge writestieor

Benchmark Method Candidate Train Held-out
LongMemEval-s
bco
iter0270.710 0.5925
iter0250.6900.6075
iter0200.690 0.5950
vanilla
iter0300.590 0.5300
iter0290.5600.5325
iter0250.560 0.4825
iter0180.460 0.4275
iter0150.490 0.4000
iter0120.450 0.3950
LoCoMo
bco
iter0170.47500.4534
iter0230.4625 0.4493
iter0260.4625 0.4451
vanilla
iter0130.41250.3754
iter0160.4125 0.3692
iter0210.4125 0.3596
iter0230.4125 0.3437
iter0150.3875 0.3796
Table 4: Every candidate evaluated on the memory held-out
splits, both methods. Bold is the value reported in Table 1 in
themaintext:thebestheld-outscoreamongthemethod’sthree
highest-train candidates. Rows below each method’s train
threshold were also evaluated and are listed for completeness,
but are not eligible under that rule. LoCoMo’svanillatrain
scores are a five-way tie, of which four were evaluated.
when nowinnerline can be parsed; ties are excluded from
the sign test and reported in parentheses in Table 2 in the
main text.
C Initial-Scaffold Stability and Excluded
Optimization Diagnostics
Every memory-benchmark candidate we evaluated held-
out.Table 4 lists them, for both methods, with the train
score that made a candidate eligible and the held-out score it
returned.ThereportednumberinTable1inthemaintextisthe
best held-out score among each method’s three highest-train
candidates, and the table shows what that choice costs: on
LongMemEval-stheeligiblespreadis 0.5925–0.6075forbco
and 0.4825–0.5325forvanilla,onLoCoMo 0.4451–0.4534
and 0.3437–0.3754.Theselectionmoveseachmethodbyless
than the gap between the methods, but it does select partly on
the held-out split and the memory rows should be read as a
best-of-three.
Two candidates were evaluated despite falling outside their
method’s top three and are therefore not eligible:vanilla’s
LoCoMo iter015(train 0.3875againsta 0.4125threshold)
scored 0.3796 held-out, the highest number either method
produced on that benchmark outside the eligible set, and
bco’s LongMemEval-siter014 (train 0.66 against 0.71)
scored 0.6300, the highest either method produced on that
benchmark. Quoting either would raise the corresponding
method’s number while abandoning the train threshold that
makes the rule a rule, so neither is used.
Method Campaign Train Held-out
bco1 0.581 0.635
bco2 0.548 0.558
bco3 0.581 0.567
vanilla1 0.645 0.577
vanilla2 0.548 0.587
Table 5: All retained Spider2-lite selected-candidate evalua-
tions. Train has 31 tasks; held-out has 104 database-disjoint
tasks. Unequal numbers of completed runs are shown rather
than silently dropping a campaign.
Spider2-lite.We repeated the identical initial scaffold four
times on the 104-task database-disjoint held-out split. Ag-
gregate passrates were0.577, 0.519, 0.558, and 0.462. At
the task level,45/104 tasks (43.3%) received both a pass
and a fail across the four repeats. This makes a candidate’s
observed delta a weak attribution target: the proposer may
revise a belief in response to a change that would also occur
without an edit.
Table 5 reports every completed selected-candidate evalua-
tionretainedforthisdiagnostic.Themethodorderingchanges
across campaigns, so we do not include Spider2 among the
five main benchmarks or summarize it with a single winner.
These runs were exploratory and were not used to define the
main Terminal-Bench split.
Terminal-Bench split selection.The recorded dataset is
Terminal-Bench 2.0 (89 tasks), not Terminal-Bench 2.1. An
initial uncurated train split was dominated by unstable and
timeout-bound tasks; its held-out scores were initial0.470,
bco 0.463,andvanilla 0.455.Wesubsequentlyranrepeated
initial-scaffold diagnostics and selected a 20-task training
subset with more repeatable failures and usable optimization
headroom. The main table reports that stability-screened
optimization pair. Because this selection was made after
inspecting initial-scaffold behavior, it remains a potential
source of benchmark and split-selection bias even though it
preceded comparison of the optimized methods.
D Full Target-Swap Results
Table 6 gives the exact values underlying Figure 3 in the
maintext.“All”countsacontext-windowoverrunasafailure;
“common” restricts every method to tasks all three scaffolds
complete. GAIA has no differential completion, so its two
analyses coincide. On AppWorld the common-set restriction
excludes 99, 77,and 65 bconon-completionsathigh,medium,
and low effort, respectively.
E Proposer Token Cost
bco’scostprofileisnotpartofthepaper’sclaim,butwereport
it because the hypothesis thatbcois additional prompting
would predict uniformly higher proposer token consumption,
while a compact-belief account would instead predict lower
consumption when the document reduces re-reading of accu-
mulated evidence. We reporttotalproposer tokens (input+
output) relative tovanillaon matched pairs (Table 7). We

Benchmark / effort SetNInitialvanilla bco
GAIA / high all 99 0.586 0.4750.657
GAIA / medium all 99 0.556 0.5450.566
GAIA / low all 99 0.444 0.4650.485
AppWorld / high all 372 0.5560.6850.516
AppWorld / high common 273 0.590 0.6960.703
AppWorld / medium all 372 0.5000.6080.524
AppWorld / medium common 295 0.546 0.6310.661
AppWorld / low all 372 0.4380.5380.532
AppWorld / low common 307 0.489 0.5540.645
Table6:Target-modelswaptogpt-5.6-lunaatthreereasoning-
effort tiers. The three scaffolds are evaluated unchanged. One
measurement per cell; non-completions count as failures in
the full set.
quotetokensratherthandollarsbecausethedollarfiguretracks
thismetricbutisprovider-andcache-pricing-dependent;each
row compares the two methods of one pair under a single
metering stack, so the Codex-stack Terminal-Bench 2.0 row
is internally consistent even though its absolute token counts
are not comparable to the Kimi rows.
The observed pattern is a read–write trade.bcoreads the
raw rollout traces less often (raw-trace reads down20–69%),
consistent with the compact append-only belief reducing the
needtore-derivethesameinformationfromthebulkyhistory
each iteration; it writes somewhat more, since each iteration
emits the updated belief and the prediction. Where the run’s
evidenceinducesheavyre-reading,thereaditsavesoutweighs
the write it adds and thetotaltoken count falls.
The split across benchmarks appears to track the shape of
theevidenceratherthanthehorizon.Totalsfallonthememory
runs (LongMemEval-s−27.4%, LoCoMo−24.7%) and on
GAIA (−12.4%), and sit at or above parity on AppWorld
(+5.2%) and Terminal-Bench 2.0 (+26.2%), even though
raw-trace reads fall everywhere (Figure 4). A within-run
control separates the two explanations for the three runs long
enough to admit it: truncating the memory and GAIA pairs
at iteration 10 already reproduces the split (LongMemEval-s
−37.1%,LoCoMo −24.4%,GAIA −10.0%byiteration10),
so on those pairs the saving is not an amortization effect that
accrues with horizon—it is set within the first iterations by
how much redundant re-reading the benchmark’s evidence
induces. (The AppWorld and Terminal-Bench 2.0 pairs run
T=10 to begin with, so the truncation is vacuous there.)
Memory-QA evidence is many compact per-task artifacts
from whichvanillare-derives its understanding each iter-
ation, and the result is consistent with reduced re-reading
almost immediately; the agentic environments expose a few
bulky trajectories that both methods read once, leaving little
redundant reading to replace while the belief’s write cost
recurs every iteration. The Terminal-Bench 2.0 pair, whose
metering exposes per-session diagnostics, makes the decom-
position explicit:bcoissuesfewertool calls and file reads
per iteration thanvanillayet emits +45% more output
tokens—thesurplusisbeliefwriting,notevidencere-reading.
bcois thus not uniformly more costly under the additional-
prompting hypothesis, though it is more expensive where
history re-reading does not dominate the proposer’s budget.
F Persistent Memory Without Calibration
The main comparison removes the world-model layer as a
whole.Todistinguishthecalibrationprotocolfromthesimpler
benefitofgivingtheproposeranycross-iterationmemory,we
run a three-method diagnostic on LongMemEval-s.vanilla
is the comparison method of the main experiments: each
proposercallstartsfromtherawscore,trace,anddiffevidence,
with no separately maintained state. TheNotesmethod adds
exactly one persistent file,agent_notes.md, which the
proposermayrewriteororganizehoweveritwishes.Itimposes
no prediction, falsifiable belief structure, confidence or status
field, self-grading, or predict–observe–correct update.bcois
the full protocol. The middle method therefore controls for
persistence and summarization without imposing calibration
discipline.
Table 8 reports the best training passrate found in three
independent optimization trajectories per method. Each tra-
jectoryhasanominalten-iterationproposerbudget;thescore
is taken over all candidates successfully evaluated within
that trajectory. This is an online search diagnostic on the
100-example training split, not a substitute for the held-out
comparison in Table 1 in the main text.
bcohasamodestmeanlead,butthediagnosticisnoisy.
The three-run means are0.430 (vanilla), 0.427 (Notes) and
0.467 (bco), sobcoleads by 0.037 overvanillaand 0.040
over Notes. However, the dispersionwithineach method
exceeds both gaps. Notes spans0.39 to 0.46 across its three
trajectories: it has the highest score in Runs 1 and 2 but the
lowestinRun3.Threetrajectoriesofaten-iterationsearchon
100 training examples are therefore too noisy to establish that
Notes is ineffective or that the calibration protocol reliably
outperforms free-form persistent memory. We report the
diagnostic because we ran it, not because it resolves the
question.Whatdoesbearonitiselsewhere:Section4.2ofthe
main paper is a paired held-out comparison over400–1449
test examples, and Section 4.4 of the main paper isolates the
document’scontentagainstacontrolthatholdsformat,length
and vocabulary fixed—a cleaner contrast than one protocol
against another, since it varies only the thing in dispute.
G Per-Run Breakdown of the Offline Ablation
Table 2 in the main text aggregates 40 paired candidates.
Table 9 breaks the same judgements down by run, for both
judges.Therunistheunitatwhichthecandidatesareactually
independent:withinaruntheyshareoneworldmodelandone
search trajectory. Every one of the three pairings favours the
same method in all four runs, under both judges—twelve run-
levelcomparisons,twelveinthepredicteddirection.Withfour
runs,arun-levelsigntestcannotfallbelow p= 0.125 however
consistentthedirectionis,sowereadthisasreplicationacross
runs and judges rather than as a smallp-value. Per-run win
rates are not directly comparable across runs, since each
run contributes a different candidate set sampled at different
iterations.

BenchmarkTProposer tokens∆%Raw-trace reads∆%
LongMemEval-s 30−27.4−20
LoCoMo 30−24.7−69
GAIA 20−12.4−46
AppWorld 10+5.2−23
Terminal-Bench 2.0 10+26.2−42
Table 7: Total proposer tokens (input+output) and raw-trace reads,bcorelative tovanilla, across matched pairs (∆%; negative
is fewer). Totals fall on the benchmarks whose evidence induces heavy history re-reading (memory QA, GAIA) and sit at or
above parity on the agentic environments whose evidence is a few bulky trajectories; on the three pairs withT >10 the split is
already present when the run is truncated at iteration 10 (§E), so on those it is not a horizon effect. Each row is a within-pair
comparison under one metering stack (Terminal-Bench 2.0 uses the Codex stack).
Method Run 1 Run 2 Run 3 Mean
vanilla0.37 0.44 0.48 0.430
Notes0.43 0.460.39 0.427
bco0.42 0.430.55 0.467
Table8:Persistent-stateablationonLongMemEval-s.Entries
are the best-so-far training passrate over successfully evalu-
atedcandidatesinthreeindependentoptimizationtrajectories
(100 training examples; nominal ten-iteration proposer bud-
get). Notes adds cross-iteration memory but no calibration
protocol. Each method’s within-method range (0.11, 0.07,
0.13) is as large as or larger than any between-method differ-
ence in means. Thus, althoughbcohas the highest mean, the
diagnostic does not establish that Notes is ineffective.
We report downsideprecisionrather than recall in Table 2
in the main text for two reasons. First, recall alone rewards
naming many downside types, which a scrambled document
can do without using the original content—demonstrating
that regressions happen is one of the channels scrambling
deliberately preserves. Second, recall is undefined whenever
a batch contains no realized-regressed type at all, which is
the case for one of the four runs; precision is defined for all
40 candidates.
A concrete LongMemEval-s prediction.One candidate
from LongMemEval-s run 1 replaces tier-priority-first con-
text ordering with score-first ordering and removes an ar-
tificial score boost for core and summary hits. None and
Intact name the same four Upside types but disagree on
the downside. None predicts that ten-word compression will
hurt single-session-preference,whichinsteadim-
proves by +0.25. Intact uses a belief that tier-score mis-
calibration suppresses evidence and predicts that remov-
ing the boost will let archival or recall hits crowd out
single-session-assistant;thattypeistheonethat
regresses, by −0.09. The blind judge therefore selects In-
tact. This final-document example illustrates what downside
precision measures; it is not additional independent evidence.
H Why Belief Fidelity Is Measured Offline
A cheaper-looking way to ask whether the belief improves
would be to read theonlineprediction scores—the per-
Run Judge Ivs.N Svs.N Ivs.S
LME 1 Kimi 10–0 5–4 (1) 8–1 (1) DeepSeek 9–1 5–4 (1) 9–1
LoCoMo 1 Kimi 9–1 7–3 6–3 (1) DeepSeek 10–0 8–1 (1) 5–3 (2)
LME 2 Kimi 8–2 7–3 6–4 DeepSeek 6–1 (3) 5–3 (2) 6–4
LoCoMo 2 Kimi 9–1 7–2 (1) 6–4 DeepSeek 10–0 6–1 (3) 6–4
Total Kimi36–4 26–12 (2) 26–12 (2) DeepSeek35–2 (3) 24–9 (7) 26–12 (2)
Table9:Blind-judgewins–losses(tiesinparentheses)perrun,
tencandidateseach,underbothjudges.I,SandNaretheIntact,
Scrambled and None conditions; LME is LongMemEval-s
andthedigitistherun.Thetwojudgesreplayidenticalinputs,
including the same A/B position assignment, so the judge
model is the only difference between the two rows of a run.
All twelve run-level comparisons favour the same condition;
the two judges return the same verdict on97of the120pairs.
iterationgradestheproposerassignsitsownpriorprediction—
and check whether they rise over a run. They do not rise, and
the reason is that the online score is not an instrument for
belief quality: what it measures drifts systematically over a
run, in two ways we can quantify (Table 10).
Thepredictionisoptimisticbyconstruction.Theprotocol
asksforoneimprovementperiteration,sotheproposernames
Upsidetypesandstakesapositiveneteffectessentiallyalways:
the predicted net-bet midpoint is positive in60/60 iterations
across the two runs whose protocol version logs per-type
scores.Apredictorthatmustbetonimprovementeveryround
cannot raise its score by predicting fewer improvements, only
by placing them better.
Thepositiveclassshrinksastherunapproachesitsceiling.
The upside hit rate is a precision-style metric, measured
against the set of question types that actually improved—and
that set thins out as the incumbent gets stronger. The fraction
of types realized-improved falls from0.389 to 0.267 on
LongMemEval-sandfrom 0.200to 0.083onLoCoMo,while
realized regressions become more frequent (1.6→2.6 and

0 10 20 30
0
150
300
cumulative proposer
tokens (M)
LongMemEval-s
0 10 20 30
0
150
300
LoCoMo
0 10 20
iteration
0
60
120
GAIA
0 5 10
0
40
80
AppWorld
0 5 10
0
30
60
Terminal-Bench 2.0
BCO Vanilla
Figure4:Cumulativeproposertokensvs.iterationforbcoandvanilla(fivematchedpairs;Table7).Onthememorybenchmarks
thebcocurve separates belowvanillawithin the first iterations and stays below—the token accounting is consistent with
reducedhistoryre-readingfromearlyon,notvialateamortization.OnAppWorldthetwolinesnearlycoincide,withbcocrossing
slightly above only at the final iteration, and on Terminal-Bench 2.0bcorises above mid-run: with a few bulky trajectories there
is little redundant reading to save, while the belief’s write cost recurs every iteration.
LME (run 2) LoCoMo (run 2)
Per-iteration quantity 1st 2nd 1st 2nd
Upside hit rate 0.464 0.244 0.267 0.133
Base rate: types improved 0.389 0.267 0.200 0.083
Hit rate−base rate 0.076−0.0220.067 0.050
Types regressed (count) 1.6 2.6 0.9 1.5
Predicted net effect>015/15 15/15 15/15 15/15
Table 10: First and second half of two 30-iterationbcoruns;
LME is LongMemEval-s. The online upside hit rate falls,
but so does the fraction of question types that improve at all;
the hit rate’s excess over that base rate falls much less. The
predicted net effect is positive in every iteration of both runs,
so the online score cannot separate a better belief from an
easier or harder round.
0.9→1.5 types per iteration). Against a shrinking positive
class, a predictor of constant skill mechanically loses hit rate.
Both effects are visible in the numbers. The raw upside
hit rate falls (0.464→0.244 and 0.267→0.133 between
the halves of the two runs), but once the base rate is
subtracted the decline is much smaller (0.076→ −0.022
and 0.067→0.050 ), and on LoCoMo it is almost entirely
base-rate drift. The mirror image appears in the same logs:
downside recall, whose base rategrowsas regressions
become more common, is flat or rising (0.427→0.431 and
0.682→0.875 ).Bothcurvestracktheirownbaseratesmore
closelythantheytrackanythingaboutthebelief,whichiswhy
the paper measures belief fidelity with the offline comparison
of Section 4.4 of the main paper, where every predictor faces
the same fixed candidates and the base rate is held constant
by construction. The recomputation is reproducible with
scripts/analysis/e1_base_rate_drift.py,
which re-derives each iteration’s per-type deltas from the
stored score tables and recovers the logged hit rates exactly.
