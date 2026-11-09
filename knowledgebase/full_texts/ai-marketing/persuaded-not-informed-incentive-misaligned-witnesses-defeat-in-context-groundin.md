---
title: 'Persuaded, Not Informed: Incentive-Misaligned Witnesses Defeat In-Context Grounding'
url: https://arxiv.org/abs/2609.28854
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Rahul Balakavi
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28854
pages: 9
chars: 43200
fetched_at: '2026-11-08T13:31:51+00:00'
kb_version: 1
---

# Persuaded, Not Informed: Incentive-Misaligned Witnesses Defeat In-Context Grounding

Persuaded, Not Informed:
Incentive-Misaligned Witnesses Defeat In-Context
Grounding
Rahul Balakavi
AmpUp Research
rahulb@ampup.ai
Abstract—Language-model agents are increasingly
deployed over customer-relationship management
(CRM) records to answer operational questions such
as whether a sales lead should be qualified. We identify
a failure mode not addressed by a stronger model:
when the context contains an assertion by a party
with an incentive toward optimism—here the sales
representative, a witness recorded in the CRM—the
model treats the assertion as evidence and clears deals
the company’s own records deem unacceptable. Across
100 lead-qualification tasks from CRMArena-Pro, the
representative asserts an acceptable timeline in every
call and an acceptable budget in 76; on the 31 tasks
where such an assertion contradicts the price list and
installation policy, a model reading only the transcript
clears the deal in 29 of 31 cases. The signature is
consistent across seven models from four providers
(misled on 87–97%); scale and explicit reasoning confer
no resistance. Only 3 of 35 genuine failures involve no
assertion, so the failure is one ofpersuasion, distinct
from missing information. Our contribution is a
diagnostic method, not a new architecture: (i) a bucket
analysis that separates persuasion from information
gaps, (ii) a same-information control demonstrating
that supplying the records to the modellowers
strict accuracy from 41 to 18 while raising recall—
precision collapses—and (iii) a compute-step control
that holds the extraction fixed and varies only who
computes Budget and Timeline, isolating the operative
component. The margin ranges from 42 points on an
inexpensive model to 2–5 points on models that
already compute correctly; on the strongest models
the arms are within confidence intervals, so the pattern
is best read as a consistent direction and a soundness
property rather than a proved performance floor.
We pre-specify a generalization test that returns a
negative result, characterize the precondition (policy
exactly specifiedandidentifiable from inputs), and
release all evaluation artifacts.
Index Terms—in-context grounding, knowledge
conflict, source reliability, extract-then-compute,
CRMArena-Pro, evaluation.
I. The Finding: Persuaded, Not Informed
Language-model agents are increasingly pointed at com-
pany CRMs to answer everyday questions—whether a lead
is worth pursuing, whether a quote follows policy, which
deals are at risk—and benchmarks such as CRMArena-
Pro [1] score them against known answers. On the harder
tasks these agents underperform, and the common re-
sponse is to reach for a larger model or a more elaborate
prompt. We argue that the problem lies elsewhere, and we
measure where. The failure we document sits in a small
overlap between three studied phenomena and matches
none exactly. Sycophancy [4], [5], [6] concerns deference
to theuser’sstated view; here the persuasive party is
a witness whose testimony sits in the context, not the
questioner. Knowledge conflict [13] concerns deference to
in-context evidence that contradicts parametric knowl-
edge; here the model has no parametric prior about a
specific deal’s price and there is no explicit conflict, only
an unverified claim. Indirect prompt injection [15] and
misinformation pollution [14] concern adversarial content;
here the content is not adversarial, merely optimistic. We
call this theincentive-misaligned witnesscase—a source
recorded in the context whose incentives are not aligned
with correctness—and show that supplying the records to
the model does not neutralize it.
The task on which this is clearest islead qualifica-
tion. Each task provides a sales-call transcript and asks
whether the lead can be qualified; if not, which of the
four factors of the BANT sales-qualification framework—
Budget, Authority, Need, Timeline—are at fault. Two are
answerable from what was said (whether the contact has
purchasing authority; whether a genuine need exists).
The other two are traps: whether the order actually fits
the stated budget, and whether the promised timeline is
achievable. Both depend on the company’s own catalog
prices and installation policy, not on anything contained
in the transcript.
We therefore posed a sharper question than aggregate
accuracy. For all 100 calls we sorted every genuine Budget-
or-Timeline failure into three cases: (a) the representative
explicitly claims the deal is acceptable while the records
say otherwise; (b) the representative makes no claim; and
(c)therepresentativeflagstheproblem.Wethenmeasured
how often a model, reading only the transcript, misses the
failure in each case. If case (a) is large and the model
fails there, the model is being misled rather than merely
deprived of data.
The representative asserts that the timeline is feasible in
every call, and that the budget is met in three of four. Of
arXiv:2609.28854v1  [cs.CL]  23 Sep 2026

TABLE I
What the representative claims versus what the records say, across 100 lead-qualification calls. The claim that the deal
is acceptable is asserted almost always; on the deals where it is false, the model accepts it.
Dimension Claims acceptable Genuinely fails ... and claimed acceptable Model misled
Timeline 100/100 12 12 12/12
Budget 76/100 23 19 17/19
Contradiction cases (pooled)— 3531 29/31 (94%)
the 35 deals that genuinely fail on budget or timeline, 31
are cases in which the representative claimed the opposite;
only 3 involve no claim, and 1 is a claim consistent with
the records. This excludes the mundane explanation: the
model does not fail for lack of the price list—31 of 35 failed
deals contain a claim in the transcript that contradicts
the records. That the model then accepts those claims
is a strong descriptive coincidence, not, on this design, a
proved causal effect: the assertion cannot be manipulated
without changing other properties of the transcript. The
counterfactual test that would isolate the assertion is left
as future work. A representative example: the transcript
states “that fits your budget, and we can install in a day,”
whereas the records show the order is $1,400 over budget
and the installation requires three days. A model reading
only the transcript records the claim and clears the deal.
The remedy is to change the model’s task rather than its
size. Given the same transcript, the model is restricted to
extractingtheplainfactsasstructureddata—theproducts
and quantities, the stated budget, the required timeline—
after which a small amount of deterministic code checks
those facts against the catalog price and the policy. On the
identical 31 contradiction cases, this procedure catches 28;
the model’s own end-to-end reasoning caught 2 (Fig. 1).
A. The Failure Is Model-Independent
The result in Fig. 1 is not particular to one model
or one provider. We repeated the measurement on the
same 31 contradiction cases with seven models from
four providers (OpenAI, Anthropic, Moonshot, Alibaba)
spanning current-generation and prior-generation OpenAI
models, Claude Sonnet 5 and Claude Fable 5.1 [19],
Kimi K2.6, and Qwen 3.8 Max [20]. Specific model iden-
tifiers are held in the supplementary material to keep
the paper current as models turn over—reporting the
fraction misled by the pitch and the fraction the grounded
procedure recovers, with 95% Wilson confidence intervals
[16], [17] (Table II). Every model is misled on at least 87%
of the cases, two of them (Claude Sonnet 5 and Qwen
3.8 Max) miss all but one. Explicit reasoning confers no
resistance, the frontier model is no exception, and the
effect does not depend on the provider. The grounded
procedure recovers 81–90% of the cases for every model, so
both the failure and its remedy are properties of the task
rather than of a particular model. The intervals are wide
because the contradiction set is small (n= 31, the most
that this benchmark’s 100 lead-qualification tasks admit);
we therefore read the table as evidence of a consistent
direction rather than of precise rates. The remainder of
the paper develops why the procedure works, its cost, what
component is responsible for the result, and the boundary
beyond which it does not apply.
II. The Fix: Inform the Verdict
If the failure is one of persuasion, the remedy is to
change the object the model is asked to produce. We
divide labor across two components under a single rule: the
model reads, code decides. The mechanism, which we call
extract-then-computeafter prior work on program-aided
reasoning [7], [8], [9], [2], has three parts (Fig. 2): (i) a
knowledge base of the organization’s exact, stated facts—
catalog prices, written policies—already present in the un-
derlying database; (ii) an extractor that converts natural-
language records into a small structured schema; and (iii)
a deterministic compute step that applies the policy to
the extracted facts. When the facts are already structured
rows, the extractor is omitted. We claim no novelty for this
architecture. Our contribution is diagnostic: the controls
in Section III show that supplying the records to the model
as text does not substitute for the code path, and isolate
the compute step as the operative component.
A. Cost Implications
Answering one lead-qualification query in the extract-
then-compute path is one extraction call. The ladder (Ta-
ble III) shows the inexpensive reader matches the GPT-5
within 5 points (84 versus 89), so there is no accuracy
reason to pay frontier per-query prices in this path. A
tool-using agent [2] answers the same query with several
frontier-priced calls over accumulating context (schema
inspection, query, rows, re-query, reason) and, as Fig. 1
shows, is more likely to be wrong. We do not report
absolute dollar figures; the cost ratio between the two
paths is roughly two orders of magnitude on our traces
(a few hundred fold at the extremes).
III. The Controlled Comparison
Figure1contraststwoextremes.Thefullladderbetween
them holds the input fixed and varies only the method. We
evaluate on all 100 B2B lead-qualification tasks, develop-
ing the method on the CRMArena 80/20 training split and
reporting the held-out test split. Grading is strict exact
match on the set of failing factors; where it is diagnostic

0 25 50 75 100
Of 31 deals the records call unacceptable, how many does each method catch?
90%Extract facts, code checks them
6% (2 / 31)Model reasons over the transcript
Same model, same transcript. The only difference is which component applies the price list and policy.
Fig.1. Thecentralresult.Reasoningoverthetranscripttoananswer,amodelcatchesalmostnoneofthedealstherecordsdeemunacceptable,
because the representative states that they are acceptable. Extracting the facts and checking them in code catches nearly all of them, with
no change of model or input.
TABLE II
Contradiction persists across model families. On the 31 contradiction cases, the fraction of deals each model clears
despite the records (“misled by the pitch”) and the fraction the grounded extract-then-compute procedure recovers, with
95% Wilson confidence intervals (n= 31). Every model is misled on at least 87%. Kimi K2.6 and Qwen 3.8 Max permit only
temperature 1, so those rows are one sample of a non-deterministic run; all others are temperature 0. Figure 4 carries
two older OpenAI models (GPT-4o-mini and o3-mini) that we keep for the compute-step chart because they show what code
does when the model is worst at the arithmetic.
Model Provider Misled % [95% CI] Caught % [95% CI]
Current-generation
GPT-5 OpenAI 90.3 [75–97] 80.6 [64–91]
gpt-5.6-sol OpenAI 90.3 [75–97] 90.3 [75–97]
Claude Sonnet 5 Anthropic 96.8 [84–99] 83.9 [67–93]
Claude Fable 5.1 Anthropic 93.5 [79–98] 87.1 [71–95]
Kimi K2.6 Moonshot 87.1 [71–95] 83.9 [67–93]
Qwen 3.8 Max Alibaba 96.8 [84–99] 87.1 [71–95]
Prior generation (reference)
GPT-4o OpenAI 93.5 [79–98] 90.3 [75–97]
TABLE III
The method ladder. Train and test are the CRMArena
80/20 split; “full” is all 100 tasks.
Rung — method Reader Tr. Te. Full
Direct from transcript efficient 44 40 41
+ chain-of-thought standard 56 — —
+ records, model does arithmetic standard 28 — —
Extract→compute in codestandard88 90 89
same, GPT-4o-mini efficient — —84
we also report the loosercontainmetric (all gold factors
present, extra factors tolerated), since the two diverge in
a way that exposes the failure mechanism.
The shape of the ladder is the argument. Chain-of-
thought [22] helps (41→56) but plateaus, because no
amount of reasoning over the transcript can supply a
price that is not present in it. The revealing rung is the
third: providing the model with the missing records and
asking it to reason to an answer reduces strict accuracy to
28% (GPT-4o, training split). This is not an information
problem, and it is not the credulity of Section I either;
it is the opposite failure. Handed the price list and policy,
the model swings from believing every claim to distrusting
every case: it over-reports Budget and Timeline and cor-
rupts the Authority andNonecases it previously answered
correctly. The two metrics make the mechanism explicit.
On the same-information runs of Table IV—one model, all
100 tasks, so nothing is mixed across readers—giving the
model the recordsraisescontain (58→67) whilelowering
strict (41→18). Recall of true failures improves, precision
collapses, and exact-set grading punishes the spurious
extra factors. The records help the model find failures;
they do not help it stop at the right ones. The effect
replicates and is not an artifact of the inexpensive reader:
a repeat run on the GPT-4o-mini gives41→20strict
and59→71contain, and on the GPT-4o the collapse
is larger,53→20strict against56→68contain (95%
intervals 43–62 and 13–29), with Authority falling from
25/27 to 8/27 andNonefrom 15/20 to 6/20. Differences
of one to two points between repeated temperature-zero
runs reflect provider-side nondeterminism [23].
The correction is architectural, and we state precisely
what it changes. The model’s task becomes extraction
into four narrow per-factor fields; deterministic code then
computes exactly two of them—Budget, by summing
quantity×price against the stated budget, and Timeline,
by mapping total unit volume to an installation tier
against the required window. Authority and Need remain
the model’s own booleans, relayed unchanged; code never

NL activity records
transcript·email·case
Structured rows
quotes·cases·orders
Inexpensive extractor
text→facts (JSON)
Deterministic compute
code applies the rule
Answer
verdict / value
Knowledge base
Catalog prices·Policies·Routing rules
EXACT·STATED·REUSED
no extraction needed
Fig. 2. The extract-then-compute pipeline. Text records pass through an inexpensive extractor into a small structured schema; already-
structured rows bypass it. In either path the verdict is produced by code applying the organization’s exact, stated policy, rather than by a
model reasoning over that policy internally.
TABLE IV
Same-information control (all 100 tasks; strict shown with 95% Wilson intervals,n=100). Upper block: an GPT-4o-mini
throughout. Strict = exact set match; contain = all gold factors present, extras tolerated. Handing the model the
records raises contain and lowers strict: recall up, precision down. Lower block: the compute step isolated on five
models from three providers—identical extraction, only who computes Budget/Timeline differs. Code never lowers
either metric; the margin is largest on the inexpensive model, 14–19 points pooled over two runs on the frontier and
reasoning models, shrinks to 2–4 points on Claude Sonnet 5 (three runs) and 5 on Kimi K2.6.†4 Claude Sonnet 5 responses
were not parseable JSON and 5 Kimi K2.6 calls timed out; each is graded wrong in both arms. Over parsed rows only, the
pairs are 79/83 (Claude) and 79/84 (Kimi). Kimi runs at temperature 1. Confidence intervals are marginal Wilson intervals
on each arm. Because both arms score the same 100 cases, the correct uncertainty for the arm-to-arm difference is a
paired McNemar-style interval; the marginal intervals shown here are an upper bound on it. Per-case outcomes are
released so the paired test can be computed.
Condition Records go to Strict % [95% CI] Contain
Transcript only — 41 [32–51] 58
+ records, model reasons to verdict model 18 [12–27] 67
same, conservative prompt model 11 [6–19] 62
Extract→compute code85[77–91]86
Compute-step control: one extraction, same four fields, catalog in context; only who computes Budget/Timeline differs
GPT-4o-mini, model computes model 43 [34–53] 60
GPT-4o-mini, code computes code85[77–91]85
o3-mini, model computes model 62 [52–71] 71
o3-mini, code computes code80[71–87]81
GPT-5, model computes model 64 [54–73] 78
GPT-5, code computes code81[72–88]81
Claude Sonnet 5, model computes† model 76 [67–83] 81
Claude Sonnet 5, code computes† code80[71–87]82
Kimi K2.6, model computes† model 75 [66–82] 79
Kimi K2.6, code computes† code80[71–87]80
decides them. Two consequences follow. First, one might
attribute the gain to decomposition—asking four narrow
questions instead of one holistic verdict—rather than to
computation. We tested this directly by holding every-
thing but the compute step fixed: one extraction call,
the same four fields, the catalog in context, and from
the identical extracted JSON we graded the model’s own
budget_fail/timeline_failagainst code’s recomputa-
tion from the same products (Table IV, lower block). With
the model computing, strict accuracy is 43%; with code
computing from the very same extraction, 85%. Decom-
position alone moves Authority only from 13/27 to 15/27;
it reaches 27/27 only once code computes Budget and
Timeline correctly, because the model’s spurious Budget
and Timeline flags were contaminating otherwise-correct
Authority andNonesets. The gain is the computation,
not the question format.
Stronger models narrow this gap but do not close it,
and the margin replicates: the o3-mini gives 62%/80%
(model/code); the frontier reader 64%/81%. Because these
models are not deterministic at temperature zero, we
repeated both: reasoning gives 71%/82% on a second run,
frontier 58%/79%, so the model-computes arm swings by
6–9 points between runs while the code arm moves by 2,
and the pooled margins are+14and+19. These models
now perform the arithmetic themselves—both match code

0 25 50 75 100
41direct
56+ chain-of-thought
28+ records, model computes
90extract, then compute
84same, inexpensive model
Fig. 3. Accuracy on lead qualification by method (strict set match;
readers and splits as in Table III). The decisive rung is the last:
applying the policy in code. Providing the model with the records
and asking it to reason makes it less accurate under strict grading
than providing nothing: the records raise recall of true failures but
the model over-flags.
0 25 50 75 100
43GPT-4o-mini (model)
85GPT-4o-mini (code)
62o3-mini (model)
80o3-mini (code)
64GPT-5 (model)
81GPT-5 (code)
87gpt-5.6-sol (model)
87gpt-5.6-sol (code)
76Claude Sonnet 5 (model)
80Claude Sonnet 5 (code)
87Claude Fable 5.1 (model)
88Claude Fable 5.1 (code)
75Kimi K2.6 (model)
80Kimi K2.6 (code)
80Qwen 3.8 Max (model)
80Qwen 3.8 Max (code)
Fig. 4. Compute-step control across eight models, four providers.
Each pair holds the extraction fixed and varies only who computes
Budget and Timeline: red bar = model, green bar = code. The grey
dashed line at 41 is what the transcript alone gets you; the green
dashed line at 85 is where GPT-4o-mini’s code arm lands, both from
Table IV. Across the eight displayed runs, code did not lower either
metric; the observed differences range from+42on GPT-4o-mini to
0–+5on models that already compute correctly. Two seeds per model
on o3-mini and GPT-5 are insufficient to characterize stability, so we
report an observed pattern, not a guaranteed performance floor.
on Timeline (9/11 in every run; the GPT-5 scored 11/11
once), and reasoning comes within two of code on Budget,
though frontier still trails there (9–11/19 against 16/19)—
so computation is a much smaller part of their loss, and
code’s advantage is not uniform across factors. What
remains is over-flagging of qualified deals (None10–19/20
and 14–15/20 across runs, against 20/20 in every code run)
and the Authority sets it contaminates (19–23/27 against
27/27), which code eliminates.
On the second provider the margin nearly closes:
Claude Sonnet 5 computes Budget and Timeline almost as
well as code does (16/19 and 7/10 against 17/19 and 7/10)
and over-flags almost nothing (None17/18), so its pair
is 76% against 80%, and+2to+4over three runs—well
inside the interval. Kimi K2.6 behaves like Claude, not like
GPT-5: 75% against 80%, with code’s gain again coming
from Authority (25/27 to 27/27) andNone(15/17 to
17/17) rather than from arithmetic. Figure 4 presents this
pattern. We therefore state the claim at its true strength:
code’s advantage is largest on the GPT-4o-mini (+42),
persists at+14to+19pooled over two runs on the frontier
and reasoning models, where it is a precision advantage
rather than an arithmetic one, and narrows to+2to+5on
the two models in our set that already compute correctly
and rarely over-flag. What code guarantees on every model
is a soundness property, not a lift: it never lowered either
metric. The intervals in Table IV calibrate this: on the
efficient reader the model-versus-code intervals are well
separated (34–53 against 77–91), whereas on o3-mini and
GPT-5 they meet or barely overlap at their boundary
(52–71 against 71–87; 54–73 against 72–88). Each of those
margins is therefore only marginally resolved atn=100on
its own; what makes it credible is that two independent
models reproduce the same sign and magnitude. A paired
McNemar test on matched per-case outcomes would settle
the arm-to-arm difference at the samen; we report the
marginal intervals here and release the per-case outcomes
for that analysis.
The second consequence is that the code path isfail-safe
against fabrication: when an extracted product name does
not match the catalog, code refuses to flag Budget rather
than inventing a verdict from an unknown price. This is
a soundness property, not a recall property; a genuine
budget failure can still be missed when extraction itself
fails.
A. Two Implementation Details
Two details each affected accuracy more than any
change of model. First, tier direction: the installation
policy assigns a timeline tier byfloor, the highest volume
threshold not exceeded (4 units remain in the 1-day tier;
9 units fall in the 3-day tier). Encoding it as a ceiling
inverted small orders into false Timeline failures and cost
approximately 50 points on the training split. Second,
grader flattening: multi-factor gold answers are stored as
a single comma-joined string, so a naive set comparison
scores a correct answer as incorrect; splitting both sides
before comparison recovered several points that were never
model errors.
Prior to any evaluation, we classified all 22 B2B task
types by a rule committed to a timestamped file before
any score was observed: is the answer derivable from
the natural-language content of activity records, with-
out arithmetic over rows, a numbered rulebook, or data
outside the ingested scope? Only two types qualify; lead
qualification is the one we carry to completion because it
lies on the boundary. One caveat applies to the other con-

TABLE V
Per-factor accuracy at the top of the ladder (GPT-4o).
Budget and Timeline are computed by code from the
extracted quantities; Authority, Need, andNoneare the
model’s own narrow booleans, relayed by code. The
computed factors become answerable; the residual Need
misses are model judgments.
Factor Correct Answerable from...
Authority 27/27 transcript content
None (qualifies) 20/20 transcript content
Budget 18/19 catalog prices + computation
Need 12/15 transcript (subjective)
Timeline 9/11 install policy + computation
tent type,knowledge_qa: CRMArena grades it by token-
overlap F1 in the manner of extractive question answering
[24], which on its approximately 50-character reference an-
swers penalizes a correct answer that is phrased differently.
Even a strong model that selects the correct source article
and answers correctly averages about 0.04 F1, so we do
not interpret that metric as an answerability rate.
IV. Where the Approach Ceases to Apply
A mechanism is only as useful as the boundary of its
applicability. To locate that boundary we pre-specified,
in the manner of a pre-registration [33], a generalization
test: before writing any code or observing any score,
we recorded a prediction that a second task type would
also succeed. The task,invalid_config, audits a quote
against company regulations and returns the identifier of
the violated policy article. Its facts are already structured
and its policy is a short rulebook, so we predicted at least
85% accuracy.
The prediction was wrong, for a reason worth stating
precisely: the correct answer cannot be recovered from
the information the task provides. The same violation
is marked differently in different tasks. A quote with
CloudLink Designer at 20 units, against a stated limit
of 15, is marked a quantity-limit violation in one task,
compliant in another, and a missing-bundle violation in
a third—yet every field that could indicate which rule to
apply is identical across all three. No rule we constructed
from the visible fields exceeded approximately 68%, and
three quotes with identical extracted inputs (CloudLink
Designer at 20 units against a stated limit of 15) receive
three different labels across task instances—compliant,
quantity-limit violation, and missing-bundle violation. We
do not claim a formal impossibility bound, and we did not
exhaustively search rule space; we claim only that no rule
we found recovers the labels, and that this failure appears
to be a property of the inputs rather than of the approach.
This is not a claim that the benchmark is mislabeled
in the sense of [34]. The likely cause is benign: each
quote was constructed to exercise one intended rule, and
the answer key records that intention, which the inputs
do not expose. We report the conclusion provisionally,
TABLE VI
The precondition, stated as a rule.
Extract-then-compute requires a policy that is exactly
specifiedandidentifiable from the inputs, not merely
documented in prose. Lead qualification satisfies this;
invalid_configdoes not, which bounds what any deter-
ministic method can achieve on it.
since we could find no rule that recovers the labels,
which is weaker than proving that none exists. A second
candidate,policy_violation_identification(does a
case resolution conflict with a knowledge article?), has
the same character: the label is determined neither by
the article’s recommended-solution text nor by the one
quantitative rule the articles state, the eligibility window
in days between the order date and the case, whose values
for violated and compliant cases of the same issue overlap
completely. We therefore did not build a solver for it, and
we count it as a second underdetermined type rather than
as a generalization result in either direction.
V. Related Work
Sycophancy and knowledge conflicts.Sycophancy
[4], [5], [6] concerns deference to theuser’sstated view.
Knowledge conflict [13], [14] concerns deference to in-
context evidence that contradicts a model’s parametric
prior. Our setting is neither: the persuasive party is a
witness recorded in the context, not the questioner, and
the model has no parametric prior about a specific deal’s
price. Kadavathet al.[36] argue that models can be
trained to know when they do not know; we measure a
case where the model has no calibrated signal that the
source itself is unreliable, and where the correction is at
the pipeline level rather than the model level.
Motivated testimony.The closer neighbor is work on
what happens when the text a model is reading was writ-
ten by someone with a stake in the answer. Knowledge-
conflict work [13] shows the model shifts once the source
is flagged as unreliable; misinformation-pollution work [14]
shows it absorbs the claim anyway when the source has
an adversarial motive. Our case is quieter: the source is
a sales representative whose incentive to sound optimistic
is a stable fact of the role, but the context never flags it
that way. We did not try prompts that make the incentive
obvious, and that is the natural comparator we owe.
Offloading computation to code.The remedy is not
new. Transformers are unreliable at exactly the multi-step
arithmetic the verdict requires [26], [27]. PAL [7] has the
model write a program as its reasoning trace and a Python
runtime execute it; Chain of Code [8] extends this to
semantic sub-steps an interpreter cannot run; Toolformer
[9] teaches models to call calculators and other tools;
ReAct [2] interleaves reasoning with tool calls. Extract-
then-compute is the same division of labor, specialised: the
model produces structured facts rather than a program,

and a fixed, audited policy—not model-written code—
performs the computation. We claim no novelty for the
architecture. Our contribution is the diagnosis ofwhyit
is required here (persuasion, not missing information),
the controls showing that supplying the records to the
model does not substitute for it, and the isolation of the
computation step as the operative component.
Enterprise agent benchmarks.CRMArena-Pro [1]
is one of several recent benchmarks that place agents
insidebusinesssoftware:τ-bench[10]testspolicy-following
in tool–agent–user dialogues, WorkArena [11] tests web
agents on ServiceNow, and AppWorld [12] tests interactive
coding agents across applications. These report aggregate
task success; we instead take one task type, characterize its
failure mechanism, and use pre-specified controls to isolate
thecausalcomponent.Retrieval-augmentedgeneration[3],
[28] is the standard means of bringing records into context;
agent memory systems [29], [30], [31] extract and consol-
idate them. Neither line prescribes whether the ultimate
verdict is drawn from the model’s reading of the retrieved
textorfromadeterministiccomputationoveritsextracted
contents. Our controls quantify the accuracy consequence
of that choice.
VI. Limitations and Conclusion
The central finding rests onone task type(lead quali-
fication,n=100) fromone benchmark(CRMArena-Pro),
and the single pre-specified generalization test returned a
negative result. Accuracy is reported against one grader,
and the cost figures pertain to a 101-account corpus and a
single embedding model. The scope is narrow by construc-
tion: B2B, single-turn, and synthetic. We do not evaluate
multi-turn interaction, business-to-consumer settings, or
the benchmark’s privacy-rejection tasks, and synthetic
data flatters a deterministic approach that is more brittle
than an agent to the noisy, custom-field reality of a
production system. One caution is specific to the finding:
although the effect holds across seven models from four
providers, spanning current and prior-generation OpenAI,
Anthropic (Sonnet 5, Fable 5.1), Moonshot, and Alibaba,
with open-weights families (Table II), the contradiction set
is small (n= 31), so the table establishes a direction rather
than precise rates; confirming them on a larger set remains
future work. The compute-step control is reported on five
modelsbutrestsonn= 100perarm,anditsmarginonthe
strongest models is resolved only at the boundary of the
intervals. On Claude Sonnet 5 and Kimi K2.6 the code arm
is within the model arm’s confidence interval; the honest
reading is that on models that already compute correctly
and rarely over-flag, code shows a consistent direction
rather than a measured lift. We report the pattern as
a directional soundness result and do not claim uniform
superiority.
Three conditions must hold before any unsupervised
deployment, and none is established here. First, access
control: a compiled solver that issues SQL directly by-
passes field-level security and record sharing, and in a
production system the same query must execute under
the caller’s permissions. Second, abstention: we report
point accuracy rather than a calibrated “escalate when
uncertain” signal [36], and acting on an 84–90% answer
without such a gate will misroute the tail. Third, trust in
extraction: the extractor remains a language model, and
an incorrectly extracted quantity—a hallucination in the
strict sense [37]—yields a confidently incorrect computed
answer, so the structured facts require validation. The
mechanism moves the error from reasoning into extraction;
it does not remove it. In particular, the extractor itself is
a language model reading the same optimistic transcript,
and a systematic bias in extracted budgets or timelines
would not be caught by any downstream code. Our per-
factor decomposition (Table V) shows Budget and Time-
line extraction agree with code’s re-derivation from the
same JSON, but this is not a proof of extractor calibration
under adversarial conditions.
We contribute a diagnostic method. When a model
answers a question over records that include an in-context
assertion by an incentive-misaligned witness, the danger is
not that it cannot reason but that it treats the assertion as
evidence, and the failure has a specific signature (recall up,
precision down) that supplying the records to the model
does not correct. Our bucket analysis separates persuasion
from missing information; our same-information control
shows the direction of the effect; our compute-step con-
trol isolates the operative component. The pattern is a
consistent direction rather than a uniform lift: on models
that already compute correctly and rarely over-flag, the
gain narrows to within confidence intervals. The precon-
dition for the correction is that the policy be exact and
identifiable from the inputs. When it is not—as our pre-
specified generalization test shows forinvalid_config—
no method, in-context or in-code, exceeds the ceiling the
inputs impose. The question to ask before reaching for a
larger model is which of these two regimes the task is in. If
the policy is written down precisely and the inputs make
it identifiable, take the arithmetic out of the model and
put your effort into the extraction step. If the policy is
not written down precisely, no model and no amount of
in-context grounding will help; either write the policy or
accept what the inputs can support.
Appendix A
A Traced Response, Both Paths
The same lead-qualification request is executed two
ways. The values are illustrative.
A.1 Extract-then-compute
[request] qualify this lead? if not, which BANT factors fail?
wants 9x "PulseSim Pro", budget ~$4,000,
needs it within 1 day, "I’ll run it by my VP";
rep: "that fits your budget, we install in a day"
[extract] inexpensive LLM ->
{"products":[{"name":"PulseSim Pro","qty":9}],
"stated_budget":4000,"required_days":1,
"authority_fail":true,"need_fail":false}

[lookup] catalog["PulseSim Pro"] = $599.99/unit
policy: 9 units -> 3-day tier (5+ -> 3 days)
[compute] 9 x 599.99 = $5,399.91 > $4,000 -> FAIL
3-day tier > 1 day required -> FAIL
authority defers to VP -> FAIL
need genuine -> ok
[answer] Authority, Budget, Timeline CORRECT
1 inexpensive call, ~$0.0002/query
A.2 Tool-using agent—reason in the loop
[step 1] plan: "inspect the schema first" . model
[step 2] describe Lead, Product2, Pricebook . model+tool
[step 3] write SOQL for products and prices . model
[step 4] execute query, read rows . tool
[step 5] budget needs a pricebook join -> re-run . model+tool
[step 6] reason over the numbers -> answer . model
[answer] "None - the lead is qualified" INCORRECT
(accepted "fits your budget" / "install in a day")
6 GPT-5 calls, ~$0.08/query (est.)
Reproducibility
All accuracy figures are measured. The evaluation
harnesses, the pre-specified task classification, the
generalization-test pre-specification (written down
before any code was run or score observed, though not
deposited with an external timestamping service), the
extraction prompts, and the per-run result files are
included as ancillary files with this submission. Model
identifiers used: OpenAIgpt-4o-mini,gpt-4o,o3-mini,
gpt-5,gpt-5.6-sol; Anthropicclaude-sonnet-5,
claude-fable-5-1; Moonshotkimi-k2.6; Alibaba
qwen/qwen3.8-max-0902(via OpenRouter). Kimi and
Qwen permit only temperature 1; all other extractions
run at temperature 0. The data split is the CRMArena
80/20 split (seed 42). This is an independent analysis
using the CRMArena-Pro B2B tasks and data; it is not
affiliated with or endorsed by the benchmark’s authors.
Data provenance and license.Interactive access to
the benchmark’s live Salesforce organization is restricted,
so the B2B records (transcripts, catalog, policies) were
read from the benchmark’s offline SQLite materialization
(crmarenapro_b2b_data.db) as redistributed in public
GitHub mirrors of the CRMArena code; the task set
is the Hugging Face release. CRMArena-Pro is licensed
CC BY-NC 4.0. This is non-commercial research, and no
benchmark records are redistributed with this paper.
Conflict of interest.The author is employed by Am-
pUp, which sells sales software that uses the extract-then-
compute architecture this paper argues for.
References
[1] K. Huanget al., “CRMArena-Pro: Holistic assessment of LLM
agents across diverse business scenarios,” Salesforce Research,
2025, arXiv:2505.18878.
[2] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and
Y. Cao, “ReAct: Synergizing reasoning and acting in language
models,” inProc. Int. Conf. Learning Representations (ICLR),
2023, arXiv:2210.03629.
[3] P. Lewiset al., “Retrieval-augmented generation for knowledge-
intensive NLP tasks,” inAdvances in Neural Information Pro-
cessing Systems (NeurIPS), 2020, arXiv:2005.11401.
[4] M. Sharmaet al., “Towards understanding sycophancy in lan-
guage models,” inProc. Int. Conf. Learning Representations
(ICLR), 2024, arXiv:2310.13548.
[5] E. Perezet al., “Discovering language model behaviors with
model-written evaluations,” inFindings of the Association for
Computational Linguistics (ACL), 2023, arXiv:2212.09251.
[6] J. Wei, D. Huang, Y. Lu, D. Zhou, and Q. V. Le, “Simple
synthetic data reduces sycophancy in large language models,”
2023, arXiv:2308.03958.
[7] L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, J.
Callan, and G. Neubig, “PAL: Program-aided language mod-
els,” inProc. Int. Conf. Machine Learning (ICML), 2023,
arXiv:2211.10435.
[8] C. Liet al., “Chain of Code: Reasoning with a language model-
augmented code emulator,” inProc. Int. Conf. Machine Learn-
ing (ICML), 2024, arXiv:2312.04474.
[9] T. Schicket al., “Toolformer: Language models can teach
themselves to use tools,” inAdvances in Neural Information
Processing Systems (NeurIPS), 2023, arXiv:2302.04761.
[10] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan, “τ-bench:
A benchmark for tool-agent-user interaction in real-world do-
mains,” 2024, arXiv:2406.12045.
[11] A. Drouinet al., “WorkArena: How capable are web agents at
solving common knowledge work tasks?” inProc. Int. Conf.
Machine Learning (ICML), 2024, arXiv:2403.07718.
[12] H. Trivediet al., “AppWorld: A controllable world of apps and
people for benchmarking interactive coding agents,” inProc.
Annu. Meeting Assoc. Computational Linguistics (ACL), 2024,
arXiv:2407.18901.
[13] J. Xie, K. Zhang, J. Chen, R. Lou, and Y. Su, “Adaptive
chameleon or stubborn sloth: Revealing the behavior of large
language models in knowledge conflicts,” inProc. Int. Conf.
Learning Representations (ICLR), 2024, arXiv:2305.13300.
[14] Y. Pan, L. Pan, W. Chen, P. Nakov, M.-Y. Kan, and W. Y.
Wang, “On the risk of misinformation pollution with large lan-
guage models,” inFindings of EMNLP, 2023, arXiv:2305.13661.
[15] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz,
and M. Fritz, “Not what you’ve signed up for: Compromising
real-world LLM-integrated applications with indirect prompt
injection,” inProc. ACM Workshop on Artificial Intelligence
and Security (AISec), 2023, arXiv:2302.12173.
[16] E. B. Wilson, “Probable inference, the law of succession, and
statistical inference,”J. Amer. Statist. Assoc., vol. 22, no. 158,
pp. 209–212, 1927.
[17] L. D. Brown, T. T. Cai, and A. DasGupta, “Interval estimation
for a binomial proportion,”Statistical Science, vol. 16, no. 2,
pp. 101–133, 2001.
[18] OpenAI, “GPT-5 system card,” Aug. 2025.
[19] Anthropic, “Claude Sonnet 5 model documentation,” 2026.
[20] Kimi Team, “Kimi K2: Open agentic intelligence,” 2025,
arXiv:2507.20534.
[21] OpenAI, “API pricing,” https://openai.com/api/pricing, ac-
cessed Sept. 2026.
[22] J. Weiet al., “Chain-of-thought prompting elicits reasoning
in large language models,” inAdvances in Neural Information
Processing Systems (NeurIPS), 2022, arXiv:2201.11903.
[23] S. Ouyang, J. M. Zhang, M. Harman, and M. Wang, “LLM is
like a box of chocolates: The non-determinism of ChatGPT in
code generation,” 2023, arXiv:2308.02828.
[24] P. Rajpurkar, J. Zhang, K. Lopyrev, and P. Liang, “SQuAD:
100,000+questionsformachinecomprehensionoftext,”inProc.
EMNLP, 2016, arXiv:1606.05250.
[25] N. F. Liuet al., “Lost in the middle: How language models use
long contexts,”Trans. Assoc. Computational Linguistics, vol.
12, 2024, arXiv:2307.03172.
[26] N. Dziriet al., “Faith and fate: Limits of transformers on com-
positionality,” inAdvances in Neural Information Processing
Systems (NeurIPS), 2023, arXiv:2305.18654.
[27] K. Cobbeet al., “Training verifiers to solve math word prob-
lems,” 2021, arXiv:2110.14168.
[28] V. Karpukhinet al., “Dense passage retrieval for open-domain
question answering,” inProc. EMNLP, 2020, arXiv:2004.04906.
[29] J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and
M. S. Bernstein, “Generative agents: Interactive simulacra of

human behavior,” inProc. ACM Symp. User Interface Software
and Technology (UIST), 2023, arXiv:2304.03442.
[30] C. Packeret al., “MemGPT: Towards LLMs as operating sys-
tems,” 2023, arXiv:2310.08560.
[31] P. Chhikara, D. Khant, S. Aryan, T. Singh, and D. Yadav,
“Mem0: Building production-ready AI agents with scalable
long-term memory,” 2025, arXiv:2504.19413.
[32] P. Christen,Data Matching: Concepts and Techniques for
Record Linkage, Entity Resolution, and Duplicate Detection.
Berlin: Springer, 2012.
[33] B. A. Nosek, C. R. Ebersole, A. C. DeHaven, and D. T. Mellor,
“Thepreregistrationrevolution,”Proc.Nat.Acad.Sci.,vol.115,
no. 11, pp. 2600–2606, 2018.
[34] C. G. Northcutt, A. Athalye, and J. Mueller, “Pervasive la-
bel errors in test sets destabilize machine learning bench-
marks,” inNeurIPS Datasets and Benchmarks Track, 2021,
arXiv:2103.14749.
[35] T. Yuet al., “Spider: A large-scale human-labeled dataset for
complex and cross-domain semantic parsing and text-to-SQL
task,” inProc. EMNLP, 2018, arXiv:1809.08887.
[36] S. Kadavathet al., “Language models (mostly) know what they
know,” 2022, arXiv:2207.05221.
[37] Z. Jiet al., “Survey of hallucination in natural language
generation,”ACM Computing Surveys, vol. 55, no. 12, 2023,
arXiv:2202.03629.
[38] T. C. Redman, “Bad data costs the U.S. $3 trillion per year,”
Harvard Business Review, Sept. 2016.
